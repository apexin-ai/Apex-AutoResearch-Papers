# research libero benchmark

**action cond info bottleneck** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 248
- **Recorded user turns:** 3
- **Tool calls:** 79
- **Original source:** `logs/workers/worker_research_libero-benchmark_20260515T111137.log`
- **Structured JSON:** [`e6fc28621227921bab70.json`](../../sessions/e6/e6fc28621227921bab70.json)

## Before a recorded user message

6 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
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
  "uuid": "e8a6019c-062b-42e6-8379-5c39eeadd8ba",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-3-projects-action-cond-info-bottleneck/memory/"
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
    "resetsAt": 1778860800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b9ca3891-1240-4aa2-bc7c-3eb8760f8459",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Assistant

_source line 4_

I'll research LIBERO Benchmark, LIBERO-Plus, and related topics in parallel using multiple agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "a90e10fa-81df-4052-9617-3763a8fa3b10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAU3tgzscA2UzDvFrTpVNL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11281,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11281
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

_source line 5_

<details open><summary>🔧 Tool call — Agent · `toolu_01HzxqFJcSQ9LxVeV3zrEHSz`</summary>

```json
{
  "description": "Research LIBERO Benchmark",
  "subagent_type": "general-purpose",
  "prompt": "Research the LIBERO Benchmark for robot manipulation. I need detailed information about:\n\n1. GitHub repo URL\n2. Installation method (pip or from source)\n3. The 5 task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90 — what each contains\n4. Data download method and size for each suite\n5. Data format: observation space dimensions/meaning, action space dimensions/meaning\n6. Evaluation scripts: how to run evaluation, what metrics are output\n\nUse WebSearch to find the LIBERO benchmark paper and GitHub repo. Then use WebFetch to read the GitHub README, installation docs, and key source files to get specific details about data format, task suites, and evaluation.\n\nBe thorough — I need exact commands, file paths, and API details. Report everything you find in a structured format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "e2518827-e059-43d9-b14a-18c346715d28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAU3tgzscA2UzDvFrTpVNL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11281,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11281
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

_source line 6_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Research LIBERO Benchmark",
  "task_type": "local_agent",
  "prompt": "Research the LIBERO Benchmark for robot manipulation. I need detailed information about:\n\n1. GitHub repo URL\n2. Installation method (pip or from source)\n3. The 5 task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90 — what each contains\n4. Data download method and size for each suite\n5. Data format: observation space dimensions/meaning, action space dimensions/meaning\n6. Evaluation scripts: how to run evaluation, what metrics are output\n\nUse WebSearch to find the LIBERO benchmark paper and GitHub repo. Then use WebFetch to read the GitHub README, installation docs, and key source files to get specific details about data format, task suites, and evaluation.\n\nBe thorough — I need exact commands, file paths, and API details. Report everything you find in a structured format.",
  "uuid": "fddf2d62-d6de-4439-a9c8-81709f70b20e",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

## Round 1

6 recorded events

### User

_source line 7 · 2026-05-15T11:11:49.711Z_

Research the LIBERO Benchmark for robot manipulation. I need detailed information about:

1. GitHub repo URL
2. Installation method (pip or from source)
3. The 5 task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90 — what each contains
4. Data download method and size for each suite
5. Data format: observation space dimensions/meaning, action space dimensions/meaning
6. Evaluation scripts: how to run evaluation, what metrics are output

Use WebSearch to find the LIBERO benchmark paper and GitHub repo. Then use WebFetch to read the GitHub README, installation docs, and key source files to get specific details about data format, task suites, and evaluation.

Be thorough — I need exact commands, file paths, and API details. Report everything you find in a structured format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "d07c16ae-40ff-48bf-a206-7affe51335ad"
}
```

</details>

---

### System

_source line 8_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Research LIBERO Benchmark",
  "usage": {
    "total_tokens": 14300,
    "tool_uses": 1,
    "duration_ms": 3533
  },
  "last_tool_name": "ToolSearch",
  "uuid": "2745bd75-4c3d-4290-8780-809b4c766a9c",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KNtoHFeNKVXbhjjeEhs3ff`</summary>

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
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "fee39005-7a4a-4365-b181-d34f80d5eb84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VF3K9wVu19VjvB9YfcGa5r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14279,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14279,
        "ephemeral_1h_input_tokens": 0
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

_source line 10 · 2026-05-15T11:11:53.249Z_

<details><summary>↩ Tool result · `toolu_01KNtoHFeNKVXbhjjeEhs3ff`</summary>

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
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "52897d0e-5efa-4416-8833-d57a3f5b8e8c"
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Agent · `toolu_016hJaz9VaWPx61DxYHc9fM9`</summary>

```json
{
  "description": "Research LIBERO-Plus perturbation",
  "subagent_type": "general-purpose",
  "prompt": "Research LIBERO-Plus, which is a perturbation-based evaluation extension for the LIBERO benchmark in robot manipulation.\n\nI need to find:\n1. What LIBERO-Plus is — what it adds on top of LIBERO\n2. GitHub repo or paper source\n3. The 4 perturbation dimensions: camera perturbation, lighting change, texture swap, sensor noise — exact definitions\n4. Installation and running instructions\n5. How it integrates with standard LIBERO evaluation\n\nAlso research whether LIBERO's simulation environment has built-in randomization options (camera jitter, color/lighting changes, background texture randomization). If it does, how to configure them. If not, whether LIBERO-Plus perturbation implementations can be reused as training-time data augmentation.\n\nUse WebSearch to find papers and repos related to \"LIBERO-Plus\" or \"LIBERO perturbation evaluation\" or \"LIBERO robustness\". Then use WebFetch to read relevant GitHub repos and paper details.\n\nReport everything in structured format with exact commands and code paths where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "1d3a0bfe-fd61-442e-b494-7532786fad11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAU3tgzscA2UzDvFrTpVNL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11281,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11281
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

_source line 12_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Research LIBERO-Plus perturbation",
  "task_type": "local_agent",
  "prompt": "Research LIBERO-Plus, which is a perturbation-based evaluation extension for the LIBERO benchmark in robot manipulation.\n\nI need to find:\n1. What LIBERO-Plus is — what it adds on top of LIBERO\n2. GitHub repo or paper source\n3. The 4 perturbation dimensions: camera perturbation, lighting change, texture swap, sensor noise — exact definitions\n4. Installation and running instructions\n5. How it integrates with standard LIBERO evaluation\n\nAlso research whether LIBERO's simulation environment has built-in randomization options (camera jitter, color/lighting changes, background texture randomization). If it does, how to configure them. If not, whether LIBERO-Plus perturbation implementations can be reused as training-time data augmentation.\n\nUse WebSearch to find papers and repos related to \"LIBERO-Plus\" or \"LIBERO perturbation evaluation\" or \"LIBERO robustness\". Then use WebFetch to read relevant GitHub repos and paper details.\n\nReport everything in structured format with exact commands and code paths where possible.",
  "uuid": "a94e8491-d17f-4b1e-9448-34330a3c8b4f",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

## Round 2

10 recorded events

### User

_source line 13 · 2026-05-15T11:11:54.413Z_

Research LIBERO-Plus, which is a perturbation-based evaluation extension for the LIBERO benchmark in robot manipulation.

I need to find:
1. What LIBERO-Plus is — what it adds on top of LIBERO
2. GitHub repo or paper source
3. The 4 perturbation dimensions: camera perturbation, lighting change, texture swap, sensor noise — exact definitions
4. Installation and running instructions
5. How it integrates with standard LIBERO evaluation

Also research whether LIBERO's simulation environment has built-in randomization options (camera jitter, color/lighting changes, background texture randomization). If it does, how to configure them. If not, whether LIBERO-Plus perturbation implementations can be reused as training-time data augmentation.

Use WebSearch to find papers and repos related to "LIBERO-Plus" or "LIBERO perturbation evaluation" or "LIBERO robustness". Then use WebFetch to read relevant GitHub repos and paper details.

Report everything in structured format with exact commands and code paths where possible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "4d5e06ef-c0fc-451a-a8a4-1ce7bda6a3f9"
}
```

</details>

---

### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Searching for LIBERO benchmark robot manipulation GitHub repo",
  "usage": {
    "total_tokens": 16264,
    "tool_uses": 2,
    "duration_ms": 7244
  },
  "last_tool_name": "WebSearch",
  "uuid": "d26a77c0-a95f-4682-a5c5-f1db5b360289",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### System

_source line 15_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Searching for LIBERO benchmark paper Lifelong Learning robot ma…",
  "usage": {
    "total_tokens": 16266,
    "tool_uses": 3,
    "duration_ms": 7506
  },
  "last_tool_name": "WebSearch",
  "uuid": "e5ffc898-243d-41cc-8d3c-fe7b5c501bc3",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### System

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Research LIBERO-Plus perturbation",
  "usage": {
    "total_tokens": 14342,
    "tool_uses": 1,
    "duration_ms": 3193
  },
  "last_tool_name": "ToolSearch",
  "uuid": "8b7d75a0-7707-4d6e-a7f4-3ce0ceb926f6",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CYE6qEsduGdJCSd6vXKo9c`</summary>

```json
{
  "query": "LIBERO benchmark robot manipulation GitHub repo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "d6579e14-ee42-4b75-98b6-7641cfb20291",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNCTfAUyq8hmkithMGGy2y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1960,
      "cache_read_input_tokens": 14279,
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

_source line 18_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NaFHSBYYZdqQiYoDkc4Kvq`</summary>

```json
{
  "query": "LIBERO benchmark paper Lifelong Learning robot manipulation task suites"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "b34d6d6a-27dc-485c-87f3-7a4a78dfa80a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNCTfAUyq8hmkithMGGy2y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1960,
      "cache_read_input_tokens": 14279,
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

_source line 19_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XRqEnpJu6K7JtZjw3ZpdFZ`</summary>

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
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "f1493836-ecb4-4065-b6ea-583c92a55e87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HscfT99oUBNzjyHLLPNHFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6065,
      "cache_read_input_tokens": 8256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6065,
        "ephemeral_1h_input_tokens": 0
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

_source line 20 · 2026-05-15T11:11:57.610Z_

<details><summary>↩ Tool result · `toolu_01XRqEnpJu6K7JtZjw3ZpdFZ`</summary>

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
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "6f7afe10-0410-4333-8d30-7543a987318a"
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Agent · `toolu_01DvNbgBP79dBVtsQLdBJJGb`</summary>

```json
{
  "description": "Research LeRobot LIBERO integration",
  "subagent_type": "general-purpose",
  "prompt": "Research the integration between LeRobot (HuggingFace's robot learning framework) and the LIBERO benchmark.\n\nI need to find:\n1. Does LeRobot natively support LIBERO datasets?\n2. If yes, what are the dataset names on HuggingFace Hub?\n3. What is the data conversion pipeline from LIBERO's native HDF5 format to LeRobot format?\n4. Any conversion scripts or utilities available\n\nUse WebSearch to search for:\n- \"LeRobot LIBERO\" \n- \"lerobot libero dataset\"\n- HuggingFace Hub LIBERO datasets\n- \"lerobot convert libero\"\n\nThen use WebFetch to check:\n- The LeRobot GitHub repo for LIBERO-related code\n- HuggingFace Hub for LIBERO datasets in LeRobot format\n- Any conversion scripts or documentation\n\nReport everything in structured format with exact dataset names, commands, and code paths."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "bd377f1a-e349-420c-a437-30f04cb64faa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAU3tgzscA2UzDvFrTpVNL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11281,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11281
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

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Research LeRobot LIBERO integration",
  "task_type": "local_agent",
  "prompt": "Research the integration between LeRobot (HuggingFace's robot learning framework) and the LIBERO benchmark.\n\nI need to find:\n1. Does LeRobot natively support LIBERO datasets?\n2. If yes, what are the dataset names on HuggingFace Hub?\n3. What is the data conversion pipeline from LIBERO's native HDF5 format to LeRobot format?\n4. Any conversion scripts or utilities available\n\nUse WebSearch to search for:\n- \"LeRobot LIBERO\" \n- \"lerobot libero dataset\"\n- HuggingFace Hub LIBERO datasets\n- \"lerobot convert libero\"\n\nThen use WebFetch to check:\n- The LeRobot GitHub repo for LIBERO-related code\n- HuggingFace Hub for LIBERO datasets in LeRobot format\n- Any conversion scripts or documentation\n\nReport everything in structured format with exact dataset names, commands, and code paths.",
  "uuid": "3f393312-566d-44fa-ab12-dc1c541a99a2",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

## Round 3

226 recorded events

### User

_source line 23 · 2026-05-15T11:11:58.759Z_

Research the integration between LeRobot (HuggingFace's robot learning framework) and the LIBERO benchmark.

I need to find:
1. Does LeRobot natively support LIBERO datasets?
2. If yes, what are the dataset names on HuggingFace Hub?
3. What is the data conversion pipeline from LIBERO's native HDF5 format to LeRobot format?
4. Any conversion scripts or utilities available

Use WebSearch to search for:
- "LeRobot LIBERO" 
- "lerobot libero dataset"
- HuggingFace Hub LIBERO datasets
- "lerobot convert libero"

Then use WebFetch to check:
- The LeRobot GitHub repo for LIBERO-related code
- HuggingFace Hub for LIBERO datasets in LeRobot format
- Any conversion scripts or documentation

Report everything in structured format with exact dataset names, commands, and code paths.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "8baa9b97-d89a-4a32-a36b-6d5f31ef8555"
}
```

</details>

---

### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Searching for LIBERO-Plus perturbation evaluation robot manipul…",
  "usage": {
    "total_tokens": 16315,
    "tool_uses": 2,
    "duration_ms": 6376
  },
  "last_tool_name": "WebSearch",
  "uuid": "41a124b4-e836-40cf-b278-fb6d88c63fc2",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A6mhyUFE9P8zgUTypbGNfp`</summary>

```json
{
  "query": "LIBERO-Plus perturbation evaluation robot manipulation benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "d73fed2d-d301-4c16-82c3-acdc8b781030",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012EUZP4boqB9ozLNdCRA5c7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1969,
      "cache_read_input_tokens": 14321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1969,
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

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Searching for LIBERO-Plus GitHub repo robustness perturbation",
  "usage": {
    "total_tokens": 16317,
    "tool_uses": 3,
    "duration_ms": 7149
  },
  "last_tool_name": "WebSearch",
  "uuid": "835869c3-dd87-47d9-bff9-dd9a6d382d09",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013NKXDr4xSgfHfazRsFCode`</summary>

```json
{
  "query": "LIBERO-Plus GitHub repo robustness perturbation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "74154388-ae5d-43de-bd12-71c6cf7b70d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012EUZP4boqB9ozLNdCRA5c7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1969,
      "cache_read_input_tokens": 14321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1969,
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

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Research LeRobot LIBERO integration",
  "usage": {
    "total_tokens": 14322,
    "tool_uses": 1,
    "duration_ms": 2990
  },
  "last_tool_name": "ToolSearch",
  "uuid": "e29a5a47-372f-494c-81bf-fc863eb4078f",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01S7kCrojDyrKsWoT2q9hKUA`</summary>

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
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "9d1bae40-fb64-4e92-94db-b8bb43d56445",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BF1e1vNWu6V2MBHTN3X6P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6051,
      "cache_read_input_tokens": 8256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6051,
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

_source line 30 · 2026-05-15T11:12:01.754Z_

<details><summary>↩ Tool result · `toolu_01S7kCrojDyrKsWoT2q9hKUA`</summary>

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
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "f48ad771-ecd0-477d-b627-a5f93c53641a"
}
```

</details>

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Searching for LIBERO benchmark robustness evaluation camera lig…",
  "usage": {
    "total_tokens": 16319,
    "tool_uses": 4,
    "duration_ms": 7645
  },
  "last_tool_name": "WebSearch",
  "uuid": "b884b572-3b15-49e0-8286-6759af98d88f",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017vWJBqAopQtDFKLeX5WN1b`</summary>

```json
{
  "query": "LIBERO benchmark robustness evaluation camera lighting texture noise perturbation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "9902aecd-014b-4bf2-a1ed-9155db9ffe18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012EUZP4boqB9ozLNdCRA5c7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1969,
      "cache_read_input_tokens": 14321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1969,
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

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Searching for LIBERO simulation environment randomization domai…",
  "usage": {
    "total_tokens": 16321,
    "tool_uses": 5,
    "duration_ms": 7728
  },
  "last_tool_name": "WebSearch",
  "uuid": "930fd8de-377d-4ff0-93b2-c3b5df82c752",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UBf9UkKwZgRTuZfMUn2iFz`</summary>

```json
{
  "query": "LIBERO simulation environment randomization domain randomization options"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "1e28fea5-669f-4be0-8000-c3ed1c7b9fd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012EUZP4boqB9ozLNdCRA5c7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1969,
      "cache_read_input_tokens": 14321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1969,
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

_source line 35 · 2026-05-15T11:12:03.328Z_

<details><summary>↩ Tool result · `toolu_01CYE6qEsduGdJCSd6vXKo9c`</summary>

```text
Web search results for query: "LIBERO benchmark robot manipulation GitHub repo"

Links: [{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO – LIBERO","url":"https://libero-project.github.io/main.html"},{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning – Sony AI","url":"https://ai.sony/publications/LIBERO-Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learning/"},{"title":"Research – LIBERO","url":"https://libero-project.github.io/research"},{"title":"LIBERO Benchmark: Lifelong Robot Learning","url":"https://www.emergentmind.com/topics/libero-benchmark"},{"title":"Documentation for Libero, a lifelong robot learning benchmark — libero 0.1.0 documentation","url":"https://lifelong-robot-learning.github.io/LIBERO/html/index.html"},{"title":"openvla/experiments/robot/libero/regenerate_libero_dataset.py at main · openvla/openvla","url":"https://github.com/openvla/openvla/blob/main/experiments/robot/libero/regenerate_libero_dataset.py"},{"title":"LIBERO | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/abs/10.5555/3666122.3668061"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"}]

Based on the search results, here's what I found about the LIBERO benchmark robot manipulation GitHub repository:

## Official LIBERO Repository

The main LIBERO GitHub repository is located at Lifelong-Robot-Learning/LIBERO, titled "Benchmarking Knowledge Transfer in Lifelong Robot Learning". You can access it at: **https://github.com/Lifelong-Robot-Learning/LIBERO**

## About LIBERO

LIBERO is a benchmark tailored to lifelong robot learning that can continually grow, designed to invite communities of machine learning and robotics people to study knowledge transfer.

## Key Features

- LIBERO provides a procedural generation pipeline that can generate an infinite number of manipulation tasks, with 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100
- The repository includes installation instructions using conda with Python 3.8.13
- High-quality human teleoperation demonstrations are provided for the task suites

## Related Repositories

There's also a fork by Hugging Face (huggingface/lerobot-libero) extended for LeRobot integration and large-scale robotics experiments, and LIBERO-PRO, an evaluation extension of the original LIBERO benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "09f010c7-d76e-451c-92f7-0658c4a6e263"
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
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Searching for LeRobot LIBERO dataset integration HuggingFace",
  "usage": {
    "total_tokens": 16288,
    "tool_uses": 2,
    "duration_ms": 5826
  },
  "last_tool_name": "WebSearch",
  "uuid": "0126ef8f-840b-484d-861f-30a794422982",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TsJz2ccCooccZUGmvNiuQL`</summary>

```json
{
  "query": "LeRobot LIBERO dataset integration HuggingFace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "8a64c383-5c03-4ddb-a10a-5f9e40bfb190",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KLtz1ND2hrDD45QCGY59m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 14307,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1962,
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

_source line 38 · 2026-05-15T11:12:04.841Z_

<details><summary>↩ Tool result · `toolu_01NaFHSBYYZdqQiYoDkc4Kvq`</summary>

```text
Web search results for query: "LIBERO benchmark paper Lifelong Learning robot manipulation task suites"

Links: [{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview","url":"https://openreview.net/forum?id=xzEtNSuDJk"},{"title":"[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/abs/2306.03310"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"LIBERO Benchmark: Lifelong Robot Learning","url":"https://www.emergentmind.com/topics/libero-benchmark"},{"title":"benchmarking knowledge transfer for lifelong robot learning","url":"https://dl.acm.org/doi/abs/10.5555/3666122.3668061"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning – Sony AI","url":"https://ai.sony/publications/LIBERO-Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learning/"},{"title":"LIBERO-Object: Lifelong Learning in Robotic Manipulation","url":"https://www.emergentmind.com/topics/libero-object"}]

Based on the search results, here's comprehensive information about the LIBERO benchmark paper and lifelong learning robot manipulation task suites:

## Overview

LIBERO is a novel benchmark of lifelong learning for robot manipulation. It is designed to study lifelong robot learning — the idea that robots need to keep learning and adapting with their users over time, not just be pretrained once.

## Task Suites

For benchmarking purposes, the benchmark creates four task suites with 130 tasks in total. More specifically, the 130 language-conditioned manipulation tasks are organized into 4 groups: Tasks with distribution shifts in object types (LIBERO-OBJECT), Tasks with distribution shifts in the spatial arrangement of objects (LIBERO-SPATIAL), Tasks with distribution shifts in the task goals (LIBERO-GOAL), and Tasks with a combination of the above three (LIBERO-100).

## Key Research Topics

LIBERO highlights five key research topics in lifelong learning for decision-making (LLDM): 1) how to efficiently transfer declarative knowledge, procedural knowledge, or the mixture of both; 2) how to design effective policy architectures and 3) effective algorithms for LLDM; 4) the robustness of a lifelong learner with respect to task ordering; and 5) the effect of model pretraining for LLDM.

## Demonstration Data

The benchmark provides high-quality, human-teleoperated demonstration data for all 130 tasks to support sample-efficient learning.

## Key Findings

Extensive experiments present several discoveries: sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder architecture excels at all types of knowledge transfer, and naive supervised pretraining can hinder agents' performance in the subsequent LLDM.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "90ddf04d-5ee4-4872-805d-d6e10a7d34b3"
}
```

</details>

---

### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Searching for lerobot convert libero HDF5 dataset script",
  "usage": {
    "total_tokens": 16290,
    "tool_uses": 3,
    "duration_ms": 6258
  },
  "last_tool_name": "WebSearch",
  "uuid": "0d8b4bcf-aea1-4a1e-ae86-b494ca171919",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018nr9gPtTUj5f9mGc3FUhLf`</summary>

```json
{
  "query": "lerobot convert libero HDF5 dataset script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "aa70719f-368b-4cdf-8e0e-622b2adef4b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KLtz1ND2hrDD45QCGY59m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 14307,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1962,
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

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Searching for huggingface hub lerobot libero dataset names",
  "usage": {
    "total_tokens": 16292,
    "tool_uses": 4,
    "duration_ms": 6727
  },
  "last_tool_name": "WebSearch",
  "uuid": "8460f4d8-07ab-44c8-9b6a-21e578536ebc",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BsBVPQpLgjmLPH42upLSR9`</summary>

```json
{
  "query": "huggingface hub lerobot libero dataset names"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "2f1065b6-14d0-4633-b7bc-95612b2a0bba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KLtz1ND2hrDD45QCGY59m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 14307,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1962,
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

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Searching for github huggingface lerobot libero conversion pipe…",
  "usage": {
    "total_tokens": 16294,
    "tool_uses": 5,
    "duration_ms": 7206
  },
  "last_tool_name": "WebSearch",
  "uuid": "d3fb9937-7b1b-4758-a662-423fd8526d0b",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y4bSZpfheLgMAxaQoBJPgR`</summary>

```json
{
  "query": "github huggingface lerobot libero conversion pipeline 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "a06954c5-7ea2-4471-bd1e-d577a41df88f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KLtz1ND2hrDD45QCGY59m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 14307,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1962,
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

_source line 45 · 2026-05-15T11:12:07.845Z_

<details><summary>↩ Tool result · `toolu_01A6mhyUFE9P8zgUTypbGNfp`</summary>

```text
Web search results for query: "LIBERO-Plus perturbation evaluation robot manipulation benchmark"

Links: [{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"}]

Based on the search results, here's comprehensive information about LIBERO-Plus:

## Overview

LIBERO-plus is a generalized benchmark for in-depth robustness analysis of vision-language-action models. LIBERO-Plus is an extensive benchmark with 10,030 tasks spanning seven perturbation dimensions, and includes a diverse training dataset with over 20,000 successful trajectories collected under systematically varied conditions.

## Key Perturbation Dimensions

The benchmark introduces controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

## Main Findings

The research exposes significant vulnerabilities in Vision-Language-Action models:

- **Extreme Sensitivity**: Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

- **Language Ignorance**: Models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

- **Compositional Failures**: Their learned representations are entangled and cannot handle the complex, multi-dimensional perturbations that characterize real-world environments.

## Benchmark Features

LIBERO-plus offers three key advancements: (1) Comprehensive evaluation across seven robustness dimensions and 21 sub-dimensions, ensuring a thorough assessment of model generalization, (2) Automated task generation, enabling the creation of a large number of diverse training and test samples, (3) Fine-grained incorporation of difficulty levels (L1–L5), providing detailed insights into when and how VLA models fail.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "a6666c3d-3b6d-4c94-9e79-1dda43d8ed51"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T11:12:07.877Z_

<details><summary>↩ Tool result · `toolu_013NKXDr4xSgfHfazRsFCode`</summary>

```text
Web search results for query: "LIBERO-Plus GitHub repo robustness perturbation"

Links: [{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"LIBERO-plus/index.html at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/index.html"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"}]

Based on the search results, here's information about the LIBERO-Plus GitHub repository and its robustness perturbation approach:

## Overview

LIBERO-Plus contains the official implementation and benchmark for a paper on "In-depth Robustness Analysis for Vision-Language-Action Models". LIBERO-Plus is a robustness benchmark for Vision-Language-Action (VLA) models built on top of LIBERO that systematically stress-tests policies by applying seven independent perturbation dimensions to the original LIBERO task set, exposing failure modes that standard benchmarks miss.

## Perturbation Dimensions

The benchmark introduces controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

## Key Findings

VLA models exhibit extreme sensitivity to camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations, models largely ignore language instructions, and combined perturbations reveal complex interaction effects beyond independent factors.

## Benchmark Scale

The benchmark construction follows a systematic two-stage process of expanding the original LIBERO benchmark through seven distinct perturbation factors, followed by task filtering and category balancing, and evaluating the resulting tasks using four representative models and stratifying them into five difficulty levels.

The GitHub repository is located at: **https://github.com/sylvestf/LIBERO-plus**


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "84a4a192-264d-4b8a-92a4-3f2d373d248e"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T11:12:08.735Z_

<details><summary>↩ Tool result · `toolu_017vWJBqAopQtDFKLeX5WN1b`</summary>

```text
Web search results for query: "LIBERO benchmark robustness evaluation camera lighting texture noise perturbation"

Links: [{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"Efficient Spatial Adaptation in VLA Models","url":"https://www.emergentmind.com/papers/2512.02902"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | Takara TLDR","url":"https://tldr.takara.ai/p/2510.13626"}]

I found comprehensive information about the LIBERO benchmark and its robustness evaluation capabilities. Here's what the search revealed:

## LIBERO-Plus: Robustness Evaluation Framework

LIBERO-Plus is an in-depth robustness analysis framework for Visual-Language-Action (VLA) models that performs systematic vulnerability analysis by introducing controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

### Key Findings

Analysis of VLA models reveals critical weaknesses, with models exhibiting extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

LIBERO-Plus offers a robust benchmarking framework with 7 perturbation dimensions and 21 sub-dimensions, providing a fine-grained difficulty scale from L1 to L5 for systematically assessing model performance across various challenges.

### Benchmark Composition

LIBERO-Plus was constructed as an extensive benchmark with 10,030 tasks spanning seven perturbation dimensions, created with a diverse training dataset with over 20,000 successful trajectories collected under systematically varied conditions.

### Specific Perturbation Types

The benchmark evaluates models across:
- Camera Viewpoints: changes to the viewpoint/pose and field-of-view of the third-person camera
- Light Conditions: variations in illumination intensity, direction, color, and shadow patterns
- Background Textures: scene and surface appearance changes, and Sensor Noise: photometric distortions and image degradation


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "897e6a87-eea7-4ae6-8ee8-2365afde5624"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T11:12:09.238Z_

<details><summary>↩ Tool result · `toolu_01UBf9UkKwZgRTuZfMUn2iFz`</summary>

```text
Web search results for query: "LIBERO simulation environment randomization domain randomization options"

Links: [{"title":"Domain Randomization for Sim2Real Transfer | Lil'Log","url":"https://lilianweng.github.io/posts/2019-05-05-domain-randomization/"},{"title":"Continual Domain Randomization","url":"https://arxiv.org/pdf/2403.12193"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"Flow-based Domain Randomization for Learning and Sequencing Robotic Skills","url":"https://arxiv.org/html/2502.01800v1"},{"title":"9.4. Domain Randomization for RL — Omniverse IsaacSim latest documentation","url":"https://docs.isaacsim.omniverse.nvidia.com/2023.1.1/isaac_gym_tutorials/tutorial_gym_domain_randomization.html"},{"title":"A Domain Data Pattern Randomization based Deep Reinforcement Learning method for Sim-to-Real transfer","url":"https://dl.acm.org/doi/fullHtml/10.1145/3461353.3461373"},{"title":"Cyclic policy distillation: Sample-efficient sim-to-real reinforcement learning with domain randomization - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0921889023000647"},{"title":"Flow-based Domain Randomization for Learning and Sequencing Robotic Skills | OpenReview","url":"https://openreview.net/forum?id=9JQXuyzdGL"},{"title":"2. Domain Randomization for RL — Omniverse IsaacSim latest documentation","url":"https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/tutorial_gym_domain_randomization.html"},{"title":"Domain Randomization","url":"https://stevengong.co/notes/Domain-Randomization"}]

Based on the search results, I found relevant information about LIBERO and domain randomization options. Here's what I discovered:

## LIBERO and Domain Randomization

LIBERO-PRO is a plug-and-play benchmark that incorporates carefully designed perturbations across four dimensions—manipulated objects, initial states, task instructions, and environments—and supports randomized combinations of these dimensions for more faithful evaluation.

### Specific Domain Randomization Dimensions in LIBERO:

The benchmark supports randomization across these key areas:

1. **Object Variation**: For object variation, new assets are created by modifying the appearance, size, and color of the original objects.

2. **Position Variation**: For position variation, alternative spatial regions are defined for all manipulable objects while strictly adhering to physical constraints and task definitions.

3. **Instruction Variation**: For instruction variation, three distinct paraphrased versions of each task description are provided.

4. **Task Variation**: For task variation, tasks are redesigned in a principled manner to ensure feasibility, and new sets of relevant objects and target states for each modified task are supplied.

5. **Environment Variation**: For environment variation, the five environment categories built into the LIBERO benchmark are leveraged and randomly substituted across tasks.

To avoid meaningless combinations, task variation is restricted from being combined with other types, while allowing all other dimensions of variation to be freely and randomly combined for more comprehensive evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "00f56bd1-d059-48e5-9c61-2db5045f3c07"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T11:12:10.560Z_

<details><summary>↩ Tool result · `toolu_01TsJz2ccCooccZUGmvNiuQL`</summary>

```text
Web search results for query: "LeRobot LIBERO dataset integration HuggingFace"

Links: [{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"lerobot/xvla-libero · Hugging Face","url":"https://huggingface.co/lerobot/xvla-libero"},{"title":"LeRobotDataset v3.0 · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3"},{"title":"HuggingFaceVLA/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/libero"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"LeRobot v0.4.0: Supercharging OSS Robot Learning","url":"https://huggingface.co/blog/lerobot-release-v040"}]

Based on the search results, here's what I found about LeRobot LIBERO dataset integration with HuggingFace:

## Overview

The LIBERO benchmark repository is now maintained by the Hugging Face team, with modifications for compatibility with LeRobot, simplified installation, and large-scale robotics experiments.

## Dataset Integration

LeRobot supports standard benchmarks like LIBERO and more, and LeRobot now officially supports LIBERO, one of the largest open benchmarks for Vision-Language-Action (VLA) policies, boasting over 130 tasks.

## Available Datasets

A preprocessed LIBERO dataset is provided that is fully compatible with the current LeRobot codebase and requires no additional manipulation, available at HuggingFaceVLA/libero. Additionally, datasets are chosen from libero_spatial, libero_object, libero_100, and libero_goal.

## Training and Evaluation

LeRobot uses a LeRobotDataset format with synchronized MP4 videos (or images) for vision and Parquet files for state/action data. The integration allows seamless training and evaluation through unified command-line interfaces for policy training and benchmarking on LIBERO tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "1dccf7a4-d1c5-4778-bfc1-bccc2a14d9e2"
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
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://github.com/Lifelong-Robot-Learning/LIBERO",
  "usage": {
    "total_tokens": 18261,
    "tool_uses": 4,
    "duration_ms": 21108
  },
  "last_tool_name": "WebFetch",
  "uuid": "ec305859-1c7c-4e49-8762-545463dafcc2",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011HKepMpNNxqpDkL9GY6vQ1`</summary>

```json
{
  "url": "https://github.com/Lifelong-Robot-Learning/LIBERO",
  "prompt": "Extract ALL technical details from this README: 1) Installation instructions (exact commands), 2) Task suite descriptions (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90), 3) Data download commands and URLs, 4) Data format details (observation space, action space, dimensions), 5) Evaluation commands, 6) Any code structure information. Be extremely thorough - capture every command, URL, and technical detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "5e1921f4-51da-4dc2-b8fd-c27fda06f6e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5RK2ucPzXxbSR7Yzpc3ui",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1983,
      "cache_read_input_tokens": 16239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1983,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T11:12:10.928Z_

<details><summary>↩ Tool result · `toolu_01BsBVPQpLgjmLPH42upLSR9`</summary>

```text
Web search results for query: "huggingface hub lerobot libero dataset names"

Links: [{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"HuggingFaceVLA/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/libero"},{"title":"LeRobotDataset v3.0 · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3"},{"title":"https://raw.githubusercontent.com/Physical-Intelli...","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"lerobot/libero_10_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_10_image"},{"title":"lerobot/xvla-libero · Hugging Face","url":"https://huggingface.co/lerobot/xvla-libero"}]

Based on the web search results, here are the LIBERO dataset names available on the Hugging Face Hub for LeRobot:

## LIBERO Task Suites

LIBERO provides 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100.

## Raw Dataset Names

The raw dataset names include "libero_10_no_noops", "libero_goal_no_noops", "libero_object_no_noops", and "libero_spatial_no_noops".

## LeRobot Processed Datasets

Several preprocessed datasets are available on the Hugging Face Hub:

1. "HuggingFaceVLA/libero" - a preprocessed LIBERO dataset fully compatible with the current LeRobot codebase
2. **lerobot/libero** - contains 40 tasks with 1,693 episodes
3. **lerobot/libero_10_image** - contains 10 tasks with 379 episodes
4. **lerobot/libero_object_image** - contains 10 tasks with 454 episodes

These datasets are designed for training and evaluating robot policies using LeRobot's framework.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "bfbb85f0-8de2-4449-8dc7-ddfd6418e8e6"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-15T11:12:11.408Z_

<details><summary>↩ Tool result · `toolu_018nr9gPtTUj5f9mGc3FUhLf`</summary>

```text
Web search results for query: "lerobot convert libero HDF5 dataset script"

Links: [{"title":"openpi/examples/libero/convert_libero_data_to_lerobot.py at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"IPEC-COMMUNITY/libero_90_no_noops_lerobot · Dataset converted ideas","url":"https://huggingface.co/datasets/IPEC-COMMUNITY/libero_90_no_noops_lerobot/discussions/2"},{"title":"GitHub - anarnuri/hdf5_to_lerobot_converter · GitHub","url":"https://github.com/anarnuri/hdf5_to_lerobot_converter"},{"title":"GitHub - muhamuttaqien/ALOHADataConverter: This repository contains scripts for converting an ALOHA HDF5 dataset into the Lerobot, RMB and GR00T formats.","url":"https://github.com/muhamuttaqien/ALOHADataConverter"},{"title":"https://raw.githubusercontent.com/Physical-Intelli...","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"Policy Post-training — isaaclab_arena 0.2","url":"https://isaac-sim.github.io/IsaacLab-Arena/main/pages/example_workflows/static_manipulation/step_4_policy_training.html"},{"title":"Question: Is There an Official or Recommended Way to Convert Isaac Lab HDF5 Data to LeRobot Schema? · Issue #2739 · isaac-sim/IsaacLab","url":"https://github.com/isaac-sim/IsaacLab/issues/2739"},{"title":"How to convert my own dataset to LerobotDataset format? · Issue #846 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/846"},{"title":"[Question] HDF5 to LeRobot convert pipeline in new release · Issue #2941 · isaac-sim/IsaacLab","url":"https://github.com/isaac-sim/IsaacLab/issues/2941"},{"title":"openvla/experiments/robot/libero/regenerate_libero_dataset.py at main · openvla/openvla","url":"https://github.com/openvla/openvla/blob/main/experiments/robot/libero/regenerate_libero_dataset.py"}]

Based on the search results, I found several relevant resources for converting LIBERO HDF5 datasets to LeRobot format:

## Primary LeRobot Conversion Script

There is a minimal example script for converting a dataset to LeRobot format in the Physical Intelligence OpenPi repository. You can run it with: `uv run examples/libero/convert_libero_data_to_lerobot.py --data_dir /path/to/your/data --push_to_hub`

To run the script, you need to install tensorflow_datasets with `uv pip install tensorflow tensorflow_datasets`, and you can download the raw Libero datasets from https://huggingface.co/datasets/openvla/modified_libero_rlds.

## Alternative Tools

The "any4lerobot" tool can be used to convert LIBERO hdf5 data to lerobot format, though it showed bugs sometimes related to videos decode.

There's also a general HDF5 to LeRobot converter that converts robotics datasets stored in custom HDF5 formats into the standardized LeRobot structure available at the GitHub repository `anarnuri/hdf5_to_lerobot_converter`.

## Processing Time

Running the conversion script will take approximately 30 minutes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "5f2e627d-4a87-40e5-abd7-c9cf80a1c306"
}
```

</details>

---

### System

_source line 54_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://lifelong-robot-learning.github.io/LIBERO/…",
  "usage": {
    "total_tokens": 18268,
    "tool_uses": 5,
    "duration_ms": 22743
  },
  "last_tool_name": "WebFetch",
  "uuid": "b9a7c028-9ae1-4754-9bc7-85ad3abd8c9e",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VZJKrdcqBMzjcz2L4H3XFv`</summary>

```json
{
  "url": "https://lifelong-robot-learning.github.io/LIBERO/html/index.html",
  "prompt": "Extract ALL technical documentation details: installation, API, data format, observation space, action space, evaluation methods, task suite descriptions, data download instructions, and any code examples. Be extremely thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "fdbd9b3d-96d5-478e-b30b-43c2c31cf269",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5RK2ucPzXxbSR7Yzpc3ui",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1983,
      "cache_read_input_tokens": 16239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1983,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
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

_source line 56_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Fetching https://github.com/sylvestf/LIBERO-plus/blob/main…",
  "usage": {
    "total_tokens": 20161,
    "tool_uses": 6,
    "duration_ms": 19368
  },
  "last_tool_name": "WebFetch",
  "uuid": "9b6a4cfc-ce3d-4fc2-a229-71b25562ec6c",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01L5mbVAKU4poVAfpeGpdbhC`</summary>

```json
{
  "url": "https://github.com/sylvestf/LIBERO-plus/blob/main/README.md",
  "prompt": "Extract the full README content including: installation instructions, perturbation dimensions with exact definitions, how to run evaluation, project structure, configuration options, and any code examples. Include all technical details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "b9bcfb13-814e-49bd-92bb-ad42849f472b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hgbj1ouCgXrztWAeWRCTda",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 16290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3840,
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

_source line 58_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://arxiv.org/abs/2306.03310",
  "usage": {
    "total_tokens": 18275,
    "tool_uses": 6,
    "duration_ms": 25570
  },
  "last_tool_name": "WebFetch",
  "uuid": "9dc0e87f-1a82-420e-9022-7e6bc48a4248",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JFfpdFjATHJrW7i5ee9g84`</summary>

```json
{
  "url": "https://arxiv.org/abs/2306.03310",
  "prompt": "Extract details about: 1) The 5 task suites (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90), their exact contents, number of tasks, 2) Observation space dimensions and meaning, 3) Action space dimensions and meaning, 4) Data format and demonstration details, 5) Evaluation protocol and metrics. Be extremely detailed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "648f9347-7896-4be7-acb7-91a635c9f398",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5RK2ucPzXxbSR7Yzpc3ui",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1983,
      "cache_read_input_tokens": 16239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1983,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T11:12:15.649Z_

<details><summary>↩ Tool result · `toolu_01Y4bSZpfheLgMAxaQoBJPgR`</summary>

```text
Web search results for query: "github huggingface lerobot libero conversion pipeline 2025 2026"

Links: [{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"GitHub - OpenDriveLab/AgiBot-World: [IROS 2025 Best Paper Award Finalist & IEEE TRO 2026] The Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems · GitHub","url":"https://github.com/OpenDriveLab/AgiBot-World"},{"title":"lerobot/xvla-libero · Hugging Face","url":"https://huggingface.co/lerobot/xvla-libero"},{"title":"Releases · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/releases"},{"title":"GitHub - starVLA/starVLA: StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing · GitHub","url":"https://github.com/starVLA/starVLA"},{"title":"lerobot/docs/source/pi05.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/pi05.mdx"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/main/en/libero"},{"title":"LeRobot · Hugging Face","url":"https://huggingface.co/docs/lerobot/index"}]

Based on the search results, here's what I found about the LeRobot LIBERO conversion pipeline:

## Overview

LIBERO provides a procedural generation pipeline that could in principle generate an infinite number of manipulation tasks, with 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100.

## LeRobot Integration

LeRobot ported LIBERO into its framework and used it mainly to evaluate SmolVLA, its lightweight Vision-Language-Action model. LeRobot supports standard benchmarks like LIBERO, MetaWorld and more to come.

## Data Conversion Pipeline

The pipeline involves downloading the raw LIBERO dataset from OpenVLA, then running a script to convert it into LeRobot dataset format. There's a referenced script `convert_libero_data_to_lerobot.py` that handles this conversion.

## Dataset Preprocessing

A preprocessed LIBERO dataset is provided that is fully compatible with the current LeRobot codebase and requires no additional manipulation.

## Key Resources

- The datasets hosted on HuggingFace are available
- The official GitHub repository: [huggingface/lerobot-libero](https://github.com/huggingface/lerobot-libero) - described as "A fork of the official LIBERO benchmark, extended for Hugging Face's LeRobot integration"


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "6c017f0c-66c5-4a71-b8e9-09d6b163d78d"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-15T11:12:16.224Z_

<details><summary>↩ Tool result · `toolu_01VZJKrdcqBMzjcz2L4H3XFv`</summary>

```text
# LIBERO Documentation Summary

Based on the provided webpage content, this is a **documentation index** rather than a technical reference page containing the requested details.

## Available Documentation Structure

The page outlines the following sections:

**Getting Started:**
- Installation procedures
- Code structure overview
- General orientation

**Technical Components:**
- Lifelong learning algorithms documentation
- Policy architecture specifications
- Dataset information

**Research Topics:**
- Knowledge transfer approaches (disentangled/entangled)
- Algorithmic design variations
- Architectural design options
- Task ordering strategies
- Pretraining methodology

**Generation Capabilities:**
- Scene creation procedures
- Task generation methods

**Practical Guides:**
- Experiment configuration instructions
- Custom algorithm/policy implementation
- Custom dataset creation

## Limitation

The extracted content provides **only navigation and section headings**, not the actual technical specifications. Details regarding API endpoints, observation/action spaces, evaluation metrics, task descriptions, download instructions, and code examples are referenced but not included in this excerpt.

To access the requested technical documentation (installation steps, API details, data formats, evaluation methods, and examples), you would need to navigate to the individual linked pages within the documentation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "3a550b63-f072-4cfb-abc1-80e36f6ddb3d"
}
```

</details>

---

### System

_source line 62_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Fetching https://arxiv.org/html/2510.13626v1",
  "usage": {
    "total_tokens": 20162,
    "tool_uses": 7,
    "duration_ms": 22193
  },
  "last_tool_name": "WebFetch",
  "uuid": "008d03c4-9b77-49f2-b129-1fe75474a6cf",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ULA9B8PqczvmkX3LtiFQVR`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.13626v1",
  "prompt": "Extract detailed information about: 1) All 7 perturbation dimensions and their exact definitions/sub-dimensions, 2) How perturbations are implemented in the simulation (MuJoCo/robosuite), 3) Difficulty levels L1-L5, 4) Training data augmentation details, 5) Integration with LIBERO's simulation environment, 6) Any details about camera, lighting, texture, sensor noise implementations specifically. Include technical specifics like parameter ranges."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "b42c9831-be67-4fb5-9f04-0d9a6cda15a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hgbj1ouCgXrztWAeWRCTda",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 16290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3840,
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

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Fetching https://sylvestf.github.io/LIBERO-plus/",
  "usage": {
    "total_tokens": 20163,
    "tool_uses": 8,
    "duration_ms": 23124
  },
  "last_tool_name": "WebFetch",
  "uuid": "6021b444-1d33-4ef1-bfb6-1286405fa1f9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U23B7oC9XDUA1Q53BwWsAc`</summary>

```json
{
  "url": "https://sylvestf.github.io/LIBERO-plus/",
  "prompt": "Extract all technical details about LIBERO-Plus: perturbation dimensions, implementation details, benchmark construction, evaluation protocol, and any information about how perturbations are applied in the simulation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "6e39f9f1-ca24-4d39-9ac7-6d90b6cf049f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hgbj1ouCgXrztWAeWRCTda",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 16290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3840,
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

_source line 66_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Fetching https://huggingface.co/docs/lerobot/en/libero",
  "usage": {
    "total_tokens": 20066,
    "tool_uses": 6,
    "duration_ms": 21174
  },
  "last_tool_name": "WebFetch",
  "uuid": "72c9b8d4-8b9c-4069-9c73-ecba15447806",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YFwoauSxTJ6sK13QtqBFCR`</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/en/libero",
  "prompt": "Extract ALL information about LIBERO integration: dataset names, conversion commands, training commands, evaluation commands, task suite names, dataset structure, any code examples. Be exhaustive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "ab70e452-7d67-44e7-bd53-c8dbb345f840",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcfN1RbSebvjnN3rA6VGUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3772,
      "cache_read_input_tokens": 16269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3772,
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

_source line 68 · 2026-05-15T11:12:20.178Z_

<details><summary>↩ Tool result · `toolu_01JFfpdFjATHJrW7i5ee9g84`</summary>

```text
# LIBERO Benchmark Details - Limited Information Available

Based on the provided arXiv page content, I can only extract minimal technical specifications:

## Available Information

**Task Suites:** The abstract mentions "four task suites (130 tasks in total)" but does not enumerate the specific suite names or their individual task counts. The suite names you listed (LIBERO-Spatial, LIBERO-Object, etc.) do not appear in this page content.

**Demonstration Data:** The paper notes it provides "high-quality human-teleoperated demonstration data for all tasks" to support sample-efficient learning, but specific formatting details are absent.

**Key Findings:** The research reveals that "sequential finetuning outperforms existing lifelong learning methods in forward transfer" and that "no single visual encoder architecture excels at all types of knowledge transfer."

## Missing Technical Details

The arXiv abstract page does not contain:
- Observation space dimensionality or specifications
- Action space dimensionality or specifications  
- Data format specifications
- Evaluation metrics and protocols
- Individual task suite compositions

## Recommendation

To obtain the detailed technical specifications you're seeking, you would need to access the full PDF paper (available via the provided link) or visit the project website referenced as "this https URL" in the abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "3c49e32f-178d-49c5-bf57-3b2a9668326a"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-15T11:12:20.439Z_

<details><summary>↩ Tool result · `toolu_011HKepMpNNxqpDkL9GY6vQ1`</summary>

````text
# LIBERO Technical Details Extraction

## Installation Instructions

The exact commands provided are:

```bash
conda create -n libero python=3.8.13
conda activate libero
git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git
cd LIBERO
pip install -r requirements.txt
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
pip install -e .
```

## Task Suite Descriptions

The README identifies four task suites with specific characteristics:

- **LIBERO-Spatial**: Requires transfer of spatial relationship knowledge with controlled distribution shifts
- **LIBERO-Object**: Focuses on object knowledge transfer with controlled shifts
- **LIBERO-Goal**: Goal-oriented knowledge transfer with controlled shifts
- **LIBERO-100**: Contains "100 manipulation tasks requiring entangled knowledge transfer"
- **LIBERO-90/LIBERO-10**: The 100-task suite split—first portion for pretraining, latter for downstream testing

## Data Download Commands and URLs

Standard download:
```bash
python benchmark_scripts/download_libero_datasets.py
```

Specific dataset selection:
```bash
python benchmark_scripts/download_libero_datasets.py --datasets DATASET
```
where DATASET ∈ `[libero_spatial, libero_object, libero_100, libero_goal]`

HuggingFace alternative:
```bash
python benchmark_scripts/download_libero_datasets.py --use-huggingface
```

**Data URL**: https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets

**Default storage location**: LIBERO folder (root directory)

## Data Format Details

The README does not explicitly specify observation space dimensions, action space details, or data format structures. However, it references:

- "camera_heights": 128
- "camera_widths": 128
- Action format: "dummy_action = [0.] * 7" (suggesting 7-dimensional action space)
- Reward function: Sparse ("+1 when task finished")

## Training/Evaluation Commands

Training command structure:
```bash
export CUDA_VISIBLE_DEVICES=GPU_ID && \
export MUJOCO_EGL_DEVICE_ID=GPU_ID && \
python libero/lifelong/main.py seed=SEED benchmark_name=BENCHMARK \
policy=POLICY lifelong=ALGO
```

Valid parameters:
- BENCHMARK ∈ `[LIBERO_SPATIAL, LIBERO_OBJECT, LIBERO_GOAL, LIBERO_90, LIBERO_10]`
- POLICY ∈ `[bc_rnn_policy, bc_transformer_policy, bc_vilt_policy]`
- ALGO ∈ `[base, er, ewc, packnet, multitask]`

Evaluation command:
```bash
python libero/lifelong/evaluate.py --benchmark BENCHMARK_NAME --task_id TASK_ID \
--algo ALGO_NAME --policy POLICY_NAME --seed SEED --ep EPOCH \
--load_task LOAD_TASK --device_id CUDA_ID
```

## Code Structure

The repository contains:
- `benchmark_scripts/`: Dataset download utilities
- `libero/`: Main package directory
- `notebooks/`: Example implementations
- `scripts/`: Utility scripts
- `templates/`: Configuration templates
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "df53a934-087b-452a-9253-f6550d837df3"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-15T11:12:20.434Z_

<details><summary>↩ Tool result · `toolu_01YFwoauSxTJ6sK13QtqBFCR`</summary>

````text
# LIBERO

LIBERO is a benchmark designed to study **lifelong robot learning** — the idea that robots need to keep learning and adapting with their users over time, not just be pretrained once. It provides a set of standardized manipulation tasks that focus on **knowledge transfer**: how well a robot can apply what it has already learned to new situations. By evaluating on LIBERO, different algorithms can be compared fairly and researchers can build on each other's work.

- Paper: [Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)
- GitHub: [Lifelong-Robot-Learning/LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO)
- Project website: [libero-project.github.io](https://libero-project.github.io)

![An overview of the LIBERO benchmark](https://libero-project.github.io/assets/img/libero/fig1.png)

## Available tasks

LIBERO includes **five task suites** covering **130 tasks**, ranging from simple object manipulations to complex multi-step scenarios:

| Suite          | CLI name         | Tasks | Description                                        |
| -------------- | ---------------- | ----- | -------------------------------------------------- |
| LIBERO-Spatial | `libero_spatial` | 10    | Tasks requiring reasoning about spatial relations  |
| LIBERO-Object  | `libero_object`  | 10    | Tasks centered on manipulating different objects   |
| LIBERO-Goal    | `libero_goal`    | 10    | Goal-conditioned tasks with changing targets       |
| LIBERO-90      | `libero_90`      | 90    | Short-horizon tasks from the LIBERO-100 collection |
| LIBERO-Long    | `libero_10`      | 10    | Long-horizon tasks from the LIBERO-100 collection  |

## Installation

After following the LeRobot installation instructions:

```bash
pip install -e ".[libero]"
```

LIBERO requires Linux (`sys_platform == 'linux'`). LeRobot uses MuJoCo for simulation — set the rendering backend before training or evaluation:

```bash
export MUJOCO_GL=egl  # for headless servers (HPC, cloud)
```

## Evaluation

### Default evaluation (recommended)

Evaluate across the four standard suites (10 episodes per task):

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```

### Single-suite evaluation

Evaluate on one LIBERO suite:

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_object \
  --eval.batch_size=2 \
  --eval.n_episodes=3
```

- `--env.task` picks the suite (`libero_object`, `libero_spatial`, etc.).
- `--env.task_ids` restricts to specific task indices (`[0]`, `[1,2,3]`, etc.). Omit to run all tasks in the suite.
- `--eval.batch_size` controls how many environments run in parallel.
- `--eval.n_episodes` sets how many episodes to run per task.

### Multi-suite evaluation

Benchmark a policy across multiple suites at once by passing a comma-separated list:

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_object,libero_spatial \
  --eval.batch_size=1 \
  --eval.n_episodes=2
```

### Control mode

LIBERO supports two control modes — `relative` (default) and `absolute`. Different VLA checkpoints are trained with different action parameterizations, so make sure the mode matches your policy:

```bash
--env.control_mode=relative   # or "absolute"
```

### Policy inputs and outputs

**Observations:**

- `observation.state` — 8-dim proprioceptive features (eef position, axis-angle orientation, gripper qpos)
- `observation.images.image` — main camera view (`agentview_image`), HWC uint8
- `observation.images.image2` — wrist camera view (`robot0_eye_in_hand_image`), HWC uint8

  LeRobot enforces the `.images.*` prefix for visual features. Ensure your
  policy config `input_features` use the same naming keys, and that your dataset
  metadata keys follow this convention. If your data contains different keys,
  you must rename the observations to match what the policy expects, since
  naming keys are encoded inside the normalization statistics layer.

**Actions:**

- Continuous control in `Box(-1, 1, shape=(7,))` — 6D end-effector delta + 1D gripper

### Recommended evaluation episodes

For reproducible benchmarking, use **10 episodes per task** across all four standard suites (Spatial, Object, Goal, Long). This gives 400 total episodes and matches the protocol used for published results.

## Training

### Dataset

We provide a preprocessed LIBERO dataset fully compatible with LeRobot:

- [HuggingFaceVLA/libero](https://huggingface.co/datasets/HuggingFaceVLA/libero)

For reference, the original dataset published by Physical Intelligence:

- [physical-intelligence/libero](https://huggingface.co/datasets/physical-intelligence/libero)

### Example training command

```bash
lerobot-train \
  --policy.type=smolvla \
  --policy.repo_id=${HF_USER}/libero-test \
  --policy.load_vlm_weights=true \
  --dataset.repo_id=HuggingFaceVLA/libero \
  --env.type=libero \
  --env.task=libero_10 \
  --output_dir=./outputs/ \
  --steps=100000 \
  --batch_size=4 \
  --eval.batch_size=1 \
  --eval.n_episodes=1 \
  --eval_freq=1000
```

## Reproducing published results

We reproduce the results of Pi0.5 on the LIBERO benchmark. We take the Physical Intelligence LIBERO base model (`pi05_libero`) and finetune for an additional 6k steps in bfloat16, with batch size of 256 on 8 H100 GPUs using the [HuggingFace LIBERO dataset](https://huggingface.co/datasets/HuggingFaceVLA/libero).

The finetuned model: [lerobot/pi05_libero_finetuned](https://huggingface.co/lerobot/pi05_libero_finetuned)

### Evaluation command

```bash
lerobot-eval \
  --output_dir=./eval_logs/ \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --policy.path=pi05_libero_finetuned \
  --policy.n_action_steps=10 \
  --env.max_parallel_tasks=1
```

We set `n_action_steps=10`, matching the original OpenPI implementation.

### Results

| Model               | LIBERO Spatial | LIBERO Object | LIBERO Goal | LIBERO 10 | Average  |
| ------------------- | -------------- | ------------- | ----------- | --------- | -------- |
| **Pi0.5 (LeRobot)** | 97.0           | 99.0          | 98.0        | 96.0      | **97.5** |

These results are consistent with the [original results](https://github.com/Physical-Intelligence/openpi/tree/main/examples/libero#results) reported by Physical Intelligence:

| Model              | LIBERO Spatial | LIBERO Object | LIBERO Goal | LIBERO 10 | Average   |
| ------------------ | -------------- | ------------- | ----------- | --------- | --------- |
| **Pi0.5 (OpenPI)** | 98.8           | 98.2          | 98.0        | 92.4      | **96.85** |


````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "7506bc69-1c71-4d44-a370-6948ac2c9626"
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
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Fetching https://huggingface.co/datasets/lerobot/libero",
  "usage": {
    "total_tokens": 20067,
    "tool_uses": 7,
    "duration_ms": 22571
  },
  "last_tool_name": "WebFetch",
  "uuid": "5a9d1eed-f2ff-4560-9f32-ece465fe4f54",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RRxe6Mx6qGds5WgQ7Jrzp3`</summary>

```json
{
  "url": "https://huggingface.co/datasets/lerobot/libero",
  "prompt": "Extract the full dataset card: dataset name, size, number of episodes, number of tasks, data format, column names, how to load it, any usage examples. Include all metadata."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "12de8fef-e160-4c06-b2d8-916ede2bfd18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcfN1RbSebvjnN3rA6VGUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3772,
      "cache_read_input_tokens": 16269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3772,
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

_source line 73 · 2026-05-15T11:12:22.453Z_

<details><summary>↩ Tool result · `toolu_01L5mbVAKU4poVAfpeGpdbhC`</summary>

```text
# LIBERO-Plus: Robustness Analysis Framework

## Overview

LIBERO-Plus is a comprehensive benchmark evaluating vision-language-action (VLA) models across multiple perturbation dimensions. The project functions as a drop-in replacement for the original LIBERO package, maintaining backward compatibility while adding extensive robustness testing capabilities.

## Installation

The setup process mirrors the original LIBERO system. Users should:

1. Clone the repository and navigate to the directory
2. Uninstall any existing LIBERO installation
3. Verify configuration paths at `/root/.libero/config.yaml`
4. Install via `pip install -e .`
5. Add system dependencies (libexpat1, libfontconfig1-dev, libmagickwand-dev)
6. Install additional Python packages from extra_requirements.txt

Assets must be downloaded from Hugging Face and extracted to `LIBERO-plus/libero/libero/assets/`, creating subdirectories for articulated objects, new objects, scenes, textures, and supporting files.

## Seven Perturbation Dimensions

The benchmark evaluates resilience across:

1. **Objects Layout** – "Confounding objects and target object displacement"
2. **Camera Viewpoints** – Position, orientation, and field-of-view modifications
3. **Robot Initial States** – Manipulator pose variations
4. **Language Instructions** – LLM-based instruction rewrites
5. **Light Conditions** – Intensity, direction, color, and shadow changes
6. **Background Textures** – Scene and surface appearance modifications
7. **Sensor Noise** – "Photometric distortions and image degradation"

## Evaluation Protocol

The evaluation methodology closely follows original LIBERO standards with one critical adjustment: modify `num_trials_per_task` from 50 to 1 in configuration files. Task classification mappings between IDs, perturbation categories, and difficulty levels are located in `.libero/libero/benchmark/task_classification.json`.

## Project Structure

The extracted asset directory should contain:
- articulated_objects/
- new_objects/
- scenes/
- stable_hope_objects/
- stable_scanned_objects/
- textures/
- turbosquid_objects/
- Supporting XML files (serving_region.xml, wall.xml, wall.stl)

## Key Findings

Research reveals that current VLA models demonstrate "extreme sensitivity to camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations." Additionally, models exhibit substantial language instruction ignorance and negative compositional generalization when multiple perturbations combine.

## Citation

For research using this benchmark, cite: Fei et al., "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models," arXiv:2510.13626 (2025).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "085d2d76-0f6a-4b23-b237-c1f026d0ebfb"
}
```

</details>

---

### System

_source line 74_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Fetching https://github.com/Physical-Intelligence/openpi/b…",
  "usage": {
    "total_tokens": 20068,
    "tool_uses": 8,
    "duration_ms": 24621
  },
  "last_tool_name": "WebFetch",
  "uuid": "f4a0ac4c-9d4a-4fc4-914c-cdf0765a8bd4",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 75_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XkrtTrt73iJhaJanKR9dzU`</summary>

```json
{
  "url": "https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py",
  "prompt": "Extract the FULL conversion script code. Show all imports, functions, the main conversion logic, command-line arguments, and how it maps LIBERO HDF5 fields to LeRobot format. Include every detail of the data mapping."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "4733bdee-7b38-4e53-a61a-f160210f368a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcfN1RbSebvjnN3rA6VGUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3772,
      "cache_read_input_tokens": 16269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3772,
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

_source line 76_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Fetching https://github.com/huggingface/lerobot-libero",
  "usage": {
    "total_tokens": 20069,
    "tool_uses": 9,
    "duration_ms": 25445
  },
  "last_tool_name": "WebFetch",
  "uuid": "ac4d2341-cf3b-4336-a4a2-3ccfca2beacb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BqhEA6bS8fXEvnN2egxkJH`</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot-libero",
  "prompt": "Extract all information about this repository: what it does, how it integrates with LeRobot, installation instructions, usage, any conversion scripts or utilities. Include all README content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "0f222f75-53f5-4545-aa1b-b2604f9ba804",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcfN1RbSebvjnN3rA6VGUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3772,
      "cache_read_input_tokens": 16269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3772,
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

_source line 78 · 2026-05-15T11:12:24.619Z_

<details><summary>↩ Tool result · `toolu_01U23B7oC9XDUA1Q53BwWsAc`</summary>

```text
# LIBERO-Plus Technical Details

## Seven Perturbation Dimensions

The study introduces controlled perturbations across: "(i) objects layout, (ii) camera viewpoints, (iii) robot initial states, (iv) language instructions, (v) light conditions, (vi) background textures and (vii) sensor noise."

## Benchmark Construction

The researchers employed a "systematic two-stage process": first, they expanded the original LIBERO benchmark through seven distinct perturbation factors, then filtered tasks and balanced categories based on empirical findings. Subsequently, they evaluated results using four representative models and stratified tasks into five difficulty levels (Level-1 to Level-5) according to accuracy distributions.

## Key Implementation Findings

**Language Perturbations:**
- Blank instruction tests removed valid language input entirely
- Goal replacement tests substituted target objects with alternatives
- Results showed models degrade into vision-action patterns, largely disregarding language signals

**Visual Perturbations:**
- Camera changes (position, orientation, field-of-view) caused dramatic performance drops
- Robot initial pose variations significantly impacted success rates
- Background and lighting changes showed surprising resilience, attributed to wrist camera stability

**Compositional Testing:**
The study measured interaction effects using: "Δij = P(Di=1, Dj=1 | Y=1) - P(Di=1 | Y=1) · P(Dj=1 | Y=1)" where negative values indicate negative interactions between perturbation pairs.

## Benchmark Scale

LIBERO-Plus comprises "10,030 tasks spanning seven perturbation dimensions" with over 20,000 successful trajectories collected under systematically varied conditions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "49ab52ce-af74-4ad0-a66c-1df43757a72a"
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
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://lifelong-robot-learning.github.io/LIBERO/…",
  "usage": {
    "total_tokens": 20247,
    "tool_uses": 7,
    "duration_ms": 35547
  },
  "last_tool_name": "WebFetch",
  "uuid": "602a564f-bb32-48fb-9edb-b6446c2ead0b",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 80_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014WAsA1V1tkrVryRAjzNwsX`</summary>

```json
{
  "url": "https://lifelong-robot-learning.github.io/LIBERO/html/algo_data/datasets.html",
  "prompt": "Extract ALL details about datasets: observation space, action space, dimensions, data format, HDF5 structure, image sizes, proprioceptive state dimensions, and any other technical details about the data."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "4ca9a017-b6fb-405d-b33d-2213c5ff9e8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TqvhG6UvVuS35sPpDdgQoG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 601,
      "cache_creation_input_tokens": 1364,
      "cache_read_input_tokens": 18222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1364,
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

_source line 81_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://lifelong-robot-learning.github.io/LIBERO/…",
  "usage": {
    "total_tokens": 20251,
    "tool_uses": 8,
    "duration_ms": 36003
  },
  "last_tool_name": "WebFetch",
  "uuid": "46b5aa12-1972-4143-abb7-17a7818b6b82",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 82_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UmY54WtSqZSRohF6tTDbSy`</summary>

```json
{
  "url": "https://lifelong-robot-learning.github.io/LIBERO/html/getting_started/installation.html",
  "prompt": "Extract complete installation instructions, all commands, dependencies, and requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "7854d716-64c9-4b7e-9bfa-2258c53fed38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TqvhG6UvVuS35sPpDdgQoG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 601,
      "cache_creation_input_tokens": 1364,
      "cache_read_input_tokens": 18222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1364,
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

_source line 83_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://huggingface.co/datasets/yifengzhu-hf/LIBE…",
  "usage": {
    "total_tokens": 20255,
    "tool_uses": 9,
    "duration_ms": 37519
  },
  "last_tool_name": "WebFetch",
  "uuid": "f6ff6922-6d5f-47fa-8a0c-c10e46e64a32",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 84_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019nb2sAzZWD1fTiueNUci2R`</summary>

```json
{
  "url": "https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets",
  "prompt": "Extract ALL details: dataset sizes for each suite, file names, download instructions, data format description, observation and action space details, number of demonstrations per task, and any other technical specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "df30aba6-900d-4098-b371-8f6d9d442a71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TqvhG6UvVuS35sPpDdgQoG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 601,
      "cache_creation_input_tokens": 1364,
      "cache_read_input_tokens": 18222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1364,
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

_source line 85 · 2026-05-15T11:12:28.771Z_

<details><summary>↩ Tool result · `toolu_01UmY54WtSqZSRohF6tTDbSy`</summary>

````text
# LIBERO Installation Instructions

## Prerequisites
The project requires **Python 3.8.13** and uses miniconda for environment management.

## Step-by-Step Installation

**1. Create Conda Environment**
```
conda create -n libero python=3.8.13
```

**2. Install Python Dependencies**
```
pip install -r requirements.txt
```

**3. Install PyTorch and Related Libraries**
```
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
```

**4. Install Robosuite**
The documentation notes that "robosuite" serves as the underlying simulation environment.
```
pip install robosuite
```

**5. Clone and Install LIBERO Package**
```
git clone git@github.com:Lifelong-Robot-Learning/LIBERO.git
pip install -e .
```

## Key Dependencies
- **Python**: 3.8.13
- **PyTorch**: 1.11.0 (with CUDA 11.3 support)
- **Robosuite**: Required simulation framework
- **Requirements.txt**: Contains additional package specifications (file contents not detailed in documentation)

The installation guide indicates the setup enables lifelong learning research upon completion.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "20084fa7-e7fc-4931-8cb0-91fd251bf30c"
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-15T11:12:29.466Z_

<details><summary>↩ Tool result · `toolu_01RRxe6Mx6qGds5WgQ7Jrzp3`</summary>

````text
# LeRobot LIBERO Dataset Card

## Dataset Overview
**Name:** `lerobot/libero`  
**Task:** Robotics  
**License:** Apache 2.0  
**Created by:** LeRobot

## Dataset Statistics
- **Total Episodes:** 1,693
- **Total Frames:** 273,465
- **Total Tasks:** 40
- **Rows:** 273,465 (273K)
- **Total Size:** 1.94 GB
- **Video Files Size:** ~500 MB
- **Data Files Size:** ~100 MB
- **FPS:** 10.0

## Data Format & Structure
- **Format:** Parquet (auto-converted)
- **Robot Type:** Panda
- **Chunks Size:** 1,000
- **Split:** Train (0:1693)

## Column Names & Features

### Observation Features
- `observation.images.image` - Video (256×256×3 RGB, AV1 codec, yuv420p)
- `observation.images.image2` - Video (256×256×3 RGB, AV1 codec, yuv420p)
- `observation.state` - Float32, shape [8] (robot state vector)

### Action & Metadata
- `action` - Float32, shape [7] (action vector)
- `timestamp` - Float32
- `frame_index` - Int64
- `episode_index` - Int64
- `task_index` - Int64 (0-39)
- `index` - Int64 (row index)

## How to Load

### Using Hugging Face Datasets Library
```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("lerobot/libero")

# Access training split
train_split = dataset["train"]

# View sample
print(train_split[0])
```

### Using Polars/Dask
The dataset is compatible with Polars and Dask libraries for distributed processing.

## Data Studio Access
- **Viewer:** Available at [Data Studio](/datasets/lerobot/libero/viewer/)
- **Interactive exploration** of all 273K rows

## Modalities
- **Tabular** (state vectors, actions, metadata)
- **Time-series** (sequential frame data)
- **Video** (RGB camera streams)

## Usage Notes
- Data is organized in parquet chunks for efficient loading
- Videos stored separately from structured data
- Each row represents a single timestep with corresponding observations and actions
- Suitable for training imitation learning and robotic control models

## Related Models
11+ models trained on this dataset, including:
- `lerobot/smolvla_libero`
- `alexanta/pi0.5_libero`
- Various fine-tuned variants
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "da505ef0-5246-4d8c-aca6-9fd73c3e48cf"
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-15T11:12:29.761Z_

<details><summary>↩ Tool result · `toolu_01XkrtTrt73iJhaJanKR9dzU`</summary>

````text
# LIBERO to LeRobot Conversion Script

## Overview
The script converts LIBERO dataset (stored in RLDS format via TensorFlow Datasets) to LeRobot format for robotics training.

## Full Code Structure

**Imports:**
```python
import shutil
from lerobot.common.datasets.lerobot_dataset import HF_LEROBOT_HOME
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
import tensorflow_datasets as tfds
import tyro
```

**Configuration:**
- `REPO_NAME`: "your_hf_username/libero" (output dataset identifier)
- `RAW_DATASET_NAMES`: Four LIBERO variants ("libero_10_no_noops", "libero_goal_no_noops", "libero_object_no_noops", "libero_spatial_no_noops")

## Data Mapping Details

The script maps LIBERO fields to LeRobot features as follows:

| LIBERO Field | LeRobot Feature | Type | Shape | Purpose |
|---|---|---|---|---|
| observation["image"] | image | image | (256, 256, 3) | Primary camera view |
| observation["wrist_image"] | wrist_image | image | (256, 256, 3) | Wrist camera view |
| observation["state"] | state | float32 | (8,) | Proprioceptive data |
| action | actions | float32 | (7,) | Robot joint commands |
| language_instruction | task | string | N/A | Task description |

## Main Conversion Logic

1. Cleans existing output directory
2. Creates LeRobot dataset with specified features and metadata (robot_type="panda", fps=10)
3. Iterates through four raw LIBERO datasets
4. For each episode and step, extracts observation and action data
5. Calls `dataset.add_frame()` with mapped fields
6. Saves completed episodes with `dataset.save_episode()`
7. Optionally pushes to Hugging Face Hub with tags and metadata

## Command-Line Interface

Uses `tyro.cli(main)` with arguments:
- `data_dir`: Path to LIBERO dataset directory (required)
- `push_to_hub`: Boolean flag for Hugging Face Hub upload (optional)

**Note:** Requires TensorFlow and tensorflow_datasets installation; processing takes ~30 minutes.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "76881ec9-473c-4c85-81e8-f6622bd9b992"
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-15T11:12:31.723Z_

<details><summary>↩ Tool result · `toolu_019nb2sAzZWD1fTiueNUci2R`</summary>

````text
# LIBERO Datasets - Extracted Details

## Dataset Structure

The LIBERO datasets are organized into **5 suites**:
- `libero_object/`
- `libero_spatial/`
- `libero_goal/`
- `libero_90/`
- `libero_10/`

## Key Specifications

| Metric | Value |
|--------|-------|
| **Total Size** | 100 GB |
| **Monthly Downloads** | 24,823 |
| **License** | Apache 2.0 |
| **Data Format** | HDF5 files |

## Data Format

- Demonstrations are stored in **HDF5 file format**
- Each task contains multiple demonstrations stored within HDF5 containers

## Download Instructions

For detailed download and configuration instructions, refer to the **official download script**:
```
https://github.com/Lifelong-Robot-Learning/LIBERO/blob/master/benchmark_scripts/download_libero_datasets.py
```

## Limitations of This Dataset Card

⚠️ **Note:** The dataset viewer is unavailable as the repository does not have auto-detected supported data files configured. Manual data file configuration may be required.

## Related Work

- **Models trained on this dataset:**
  - tanshh97/RIPT_VLA (May 29, 2025)
  - Youyi-Kou/rynnvla-002 (Jan 3)

- **Space using dataset:**
  - jacob314159/robot-episode-curator

---

**Missing Details:** The page content does not include observation/action space specifications, individual suite sizes, or per-task demonstration counts. Consult the [official LIBERO GitHub repository](https://github.com/Lifelong-Robot-Learning/LIBERO) for comprehensive technical documentation.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "89c9e6ff-79ac-44aa-9c8d-e147c7ef6b42"
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-15T11:12:32.818Z_

<details><summary>↩ Tool result · `toolu_01BqhEA6bS8fXEvnN2egxkJH`</summary>

```text
# LIBERO-LeRobot Repository Summary

## Overview
This is Hugging Face's fork of the official LIBERO benchmark, designed for studying knowledge transfer in multitask and lifelong robot learning. The repository extends the original LIBERO framework with "modifications for compatibility with LeRobot, simplified installation, and large-scale robotics experiments."

## Core Purpose
LIBERO provides a benchmarking framework that includes:
- A procedural generation pipeline for manipulation tasks
- 130 tasks organized into four suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100
- Five research topics and three visuomotor policy architectures
- Three lifelong learning algorithms with baseline implementations

## Installation
The setup requires:
1. Creating a conda environment with Python 3.8.13
2. Cloning the repository
3. Installing dependencies via `pip install -r requirements.txt`
4. Installing PyTorch with CUDA 11.3 support
5. Installing the package in editable mode: `pip install -e .`

## Dataset Acquisition
Datasets can be downloaded via:
- `python benchmark_scripts/download_libero_datasets.py` (default storage)
- Alternative: `python benchmark_scripts/download_libero_datasets.py --use-huggingface` (from Hugging Face hub)
- Specific dataset selection available through the `--datasets` flag

## Usage Workflow

**Task Retrieval:** Users import from `libero.libero` to access benchmark dictionaries and instantiate task suites, then retrieve specific tasks with associated BDDL files and language descriptions.

**Training:** Lifelong learning experiments require selecting a benchmark, policy type (bc_rnn_policy, bc_transformer_policy, bc_vilt_policy), and algorithm (base, er, ewc, packnet, multitask), then executing the training script with specified parameters.

**Evaluation:** Separate evaluation script available for resource-constrained scenarios, accepting benchmark name, task ID, algorithm, policy type, seed, epoch, and CUDA device specifications.

## Key Features
- Sparse reward functions (agent receives +1 upon task completion)
- Fixed initial states for benchmarking consistency
- Support for 128x128 off-screen rendered observations
- Focus on lifelong imitation learning rather than pure RL

## Licensing
- Codebase: MIT License
- Datasets: Creative Commons Attribution 4.0 International (CC BY 4.0)

## Repository Statistics
- 18 stars, 17 forks, 1 open issue
- 58 commits on main branch
- Composed of 53.9% Jupyter Notebooks and 46.1% Python code
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "181bbecf-91b6-4601-bf10-3deb75dcbe93"
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-15T11:12:33.362Z_

<details><summary>↩ Tool result · `toolu_014WAsA1V1tkrVryRAjzNwsX`</summary>

```text
# Dataset Details from LIBERO Documentation

Based on the provided webpage content, the available information about datasets is limited:

## Available Datasets

The documentation mentions four datasets for lifelong learning research:
- `libero_spatial` (10 tasks)
- `libero_object` (10 tasks)
- `libero_goal` (10 tasks)
- `libero_100` (100 tasks)

## Download Instructions

Datasets can be downloaded via Python scripts to a `./datasets` directory, with options to retrieve all datasets or specific ones individually.

## Technical Specifications

**Unfortunately, the provided webpage content does not include technical details** about:
- Observation space dimensions
- Action space specifications
- Data format or encoding
- HDF5 file structures
- Image resolutions
- Proprioceptive state dimensions
- Any other structural data specifications

The current page serves as a navigation hub rather than a comprehensive technical reference. To access detailed specifications about data format, dimensions, and structure, you would need to consult additional documentation pages, the actual dataset files, or the project's GitHub repository.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "74c5bc79-151f-4366-b865-a95cedbbb028"
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-15T11:12:35.550Z_

<details><summary>↩ Tool result · `toolu_01ULA9B8PqczvmkX3LtiFQVR`</summary>

```text
# LIBERO-Plus: Perturbation Framework Technical Details

## 1. Seven Perturbation Dimensions

**Objects Layout (O1-O2):**
- O1 adds "n additional unseen objects into the task scene" from a set of 416 distractor objects via BDDL modifications
- O2 applies "random perturbations to the target object's initial position (x,y,z) and orientation" while preserving semantic relationships

**Background Textures (B1-B2):**
- B1 changes "scene texture of the environment" using 950 curated textures via XML scene definition files
- B2 randomly alters "texture of the working surface (e.g., tabletop or floor)"

**Light Conditions (L1-L4):**
- L1: Diffuse color adjustment via RGB channels
- L2: Parallel light source direction changes
- L3: Specular highlight intensity (affecting reflective surfaces)
- L4: Boolean shadow casting control

**Camera Viewpoints (C1-C3):**
- C1: Distance scaling from 1.01× to 2.00× original value along optical axis
- C2: Spherical position changes with azimuth (Δθ) and elevation (Δφ) within 15°–75° cones
- C3: Camera orientation perturbation (yaw, pitch, roll) within 2°–10°

**Robot Initial States:**
- "Random perturbations are applied to the robot arm's initial joint positions" with magnitudes 0.1–0.5 via Problem class interface modifications

**Language Instructions (R1-R3):**
- R1: Distraction rewrites adding task-irrelevant contextual information
- R2: Commonsense-based object description replacements
- R3: Reasoning complexity alterations for multi-step tasks

**Sensor Noise (N1-N5):**
- Motion Blur: kernel radius (r=5 to 35), Gaussian σ (2 to 20), angle θ ∈ U(-45°, 45°)
- Gaussian Blur: σ from 1 to 10
- Zoom Blur: scaling factors [s_min, s_max, step] from [1, 1.11, 0.01] to [1, 1.56, 0.03]
- Fog: density α (0.5–5.0), decay rate β (1.3–3.0)
- Glass Blur: σ (0.5–2.5), pixel displacement δ (1–5), iterations (1–3)

## 2. Simulation Implementation

**Environment Framework:** LIBERO benchmark built on MuJoCo physics engine via robosuite

**Implementation Methods:**
- Object layout modifications: "modifying the task description files (BDDL)"
- Background/lighting: "modifying scene XML definition files" and "registering new scene classes"
- Camera changes: "modifying the Problem class interface, with parameters derived from task filenames"
- Robot initial states: "modifying the Problem class interface"
- Sensor noise: Applied via image-space post-processing (albumentations-style transformations)

No wrist camera distortions noted; perturbations target third-person camera observations primarily.

## 3. Difficulty Levels L1-L5

Stratification based on multi-model consensus from OpenVLA-OFT, π0, π0-fast, and UniVLA:

- **L1:** Solved by all four models
- **L2:** Solved by exactly three models
- **L3:** Solved by exactly two models
- **L4:** Solved by exactly one model
- **L5:** Solved by none

"Figure 7 illustrates the proportion of tasks at each difficulty level for every dimension," showing imbalanced distributions across perturbation types.

## 4. Training Data Augmentation

**Dataset Scale:** "Over 20,000 successful trajectories" generated from expanded LIBERO base

**Generation Process:**
- Objects: 2,400 trajectories with distractor variations (non-overlapping with test set)
- Other dimensions: 4,000 trajectories each (light, camera, background, language, noise)
- Total before filtering: 22,400 trajectories; "over 20,000 high-quality trajectories retained"

**Filtering:** "Only successful trajectories were retained, and any actions corresponding to no-ops were filtered out"

**Storage Format:** "All trajectories are stored in the rlds format, consistent with standard practices"

## 5. LIBERO Integration

**Benchmark Construction:**
- Started with 40 evaluation tasks, generated 500 instances per LIBERO sub-task (Spatial, Object, Goal, Long)
- Initial pool: 14,000 candidates; final test set: "10,030 tasks spanning seven perturbation factors with twenty-one low-level components"

**Task Filtering:** Tasks solved by all or large majorities were excluded; remaining tasks balanced across sub-dimensions

**Distribution:** Final dataset spans all four LIBERO suites with representation shown in Table 7 (approximately 1,500-2,600 tasks per dimension)

## 6. Technical Implementation Details

**Lighting Parameters (from Table 5 context):** XML-based control enabling precise diffuse/specular/direction/shadow manipulation

**Camera Parameters:** Spherical coordinate system with degree-based precision; first-person wrist camera (when present) receives fewer perturbations than third-person view

**Noise Application:** Image-space transforms applied post-rendering; fog and blur effects use standard computer vision parameterization

**Language Perturbations:** "LLMs to rewrite original task instructions" (specific LLM model not disclosed in excerpt)

---

**Key Finding:** "Models are most vulnerable to changes in camera viewpoint and robot initial state," while "background variations...constitute more superficial, low-level visual changes," suggesting the framework effectively stratifies perturbation semantic depth.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "023485b5-f9d2-4082-87bf-9e2fc30b13c0"
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
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://raw.githubusercontent.com/Lifelong-Robot-…",
  "usage": {
    "total_tokens": 21697,
    "tool_uses": 10,
    "duration_ms": 47729
  },
  "last_tool_name": "WebFetch",
  "uuid": "c789c0ee-76d1-489b-b0c7-9e0f7cfa04ad",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 93_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UpMi2Q7TtsS1NGe8JKHTaK`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/libero/envs/env_wrapper.py",
  "prompt": "Extract ALL details about observation space and action space: dimensions, meanings of each dimension, image sizes, proprioceptive state components, action components (position, rotation, gripper), and any other relevant specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "e4782021-dc19-423b-9526-2280f4c5a5e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkiyvFRQs4Mtv5a2aqdVrZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 804,
      "cache_creation_input_tokens": 1231,
      "cache_read_input_tokens": 19586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1231,
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

_source line 94_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Fetching https://huggingface.co/datasets/HuggingFaceVLA/li…",
  "usage": {
    "total_tokens": 24665,
    "tool_uses": 10,
    "duration_ms": 39043
  },
  "last_tool_name": "WebFetch",
  "uuid": "5ed5cd15-9d18-4b54-a0e5-fd67ac041b35",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 95_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012up7eAufC6DCPqD75Gt5GZ`</summary>

```json
{
  "url": "https://huggingface.co/datasets/HuggingFaceVLA/libero",
  "prompt": "Extract the full dataset card: exact dataset name, size, number of episodes, task suites included, how to load, data format, any instructions on usage with LeRobot. Include all metadata and statistics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "22105923-cdce-4222-8312-d0da1d398355",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ejiv15JiBk44Et2gVNZ5Vg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4594,
      "cache_read_input_tokens": 20041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4594,
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
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://raw.githubusercontent.com/Lifelong-Robot-…",
  "usage": {
    "total_tokens": 21701,
    "tool_uses": 11,
    "duration_ms": 49527
  },
  "last_tool_name": "WebFetch",
  "uuid": "905b3a58-7589-47cf-8470-4bf86865b237",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 97_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MxUY1crA6Dm5zFD6Me47w2`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/benchmark_scripts/download_libero_datasets.py",
  "prompt": "Extract the complete download script: URLs for each dataset, download methods, file sizes, dataset names, and any configuration options."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "c77c2dad-8d0f-4fde-85c7-bebd32615ba6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkiyvFRQs4Mtv5a2aqdVrZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 804,
      "cache_creation_input_tokens": 1231,
      "cache_read_input_tokens": 19586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1231,
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

_source line 98_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Fetching https://huggingface.co/docs/lerobot/main/libero_p…",
  "usage": {
    "total_tokens": 24666,
    "tool_uses": 11,
    "duration_ms": 40495
  },
  "last_tool_name": "WebFetch",
  "uuid": "a471f18a-20e8-4fac-be57-f1c986832cd3",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 99_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FZ3ftyF8G5PyBo2B5gzzTZ`</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/main/libero_plus",
  "prompt": "Extract ALL information about LIBERO-plus: what it is, how it differs from standard LIBERO, any new datasets, new tasks, commands, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "0709c693-308c-4f9d-bfe0-e7f7b37adde0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ejiv15JiBk44Et2gVNZ5Vg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4594,
      "cache_read_input_tokens": 20041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4594,
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

_source line 100 · 2026-05-15T11:12:39.660Z_

<details><summary>↩ Tool result · `toolu_01FZ3ftyF8G5PyBo2B5gzzTZ`</summary>

````text
# LIBERO-plus

LIBERO-plus is a **robustness benchmark** for Vision-Language-Action (VLA) models built on top of [LIBERO](./libero). It systematically stress-tests policies by applying **seven independent perturbation dimensions** to the original LIBERO task set, exposing failure modes that standard benchmarks miss.

- Paper: [In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626)
- GitHub: [sylvestf/LIBERO-plus](https://github.com/sylvestf/LIBERO-plus)
- Dataset: [lerobot/libero_plus](https://huggingface.co/datasets/lerobot/libero_plus)

![An overview of the LIBERO-plus benchmark perturbation dimensions](https://github.com/sylvestf/LIBERO-plus/raw/main/static/images/libero-plus.jpg)

## Perturbation dimensions

LIBERO-plus creates ~10 000 task variants by perturbing each original LIBERO task along these axes:

| Dimension             | What changes                                          |
| --------------------- | ----------------------------------------------------- |
| Objects layout        | Target position, presence of confounding objects      |
| Camera viewpoints     | Camera position, orientation, field-of-view           |
| Robot initial states  | Manipulator start pose                                |
| Language instructions | LLM-rewritten task description (paraphrase / synonym) |
| Light conditions      | Intensity, direction, color, shadow                   |
| Background textures   | Scene surface and object appearance                   |
| Sensor noise          | Photometric distortions and image degradation         |

## Available task suites

LIBERO-plus covers the same five suites as LIBERO:

| Suite          | CLI name         | Tasks | Max steps | Description                                        |
| -------------- | ---------------- | ----- | --------- | -------------------------------------------------- |
| LIBERO-Spatial | `libero_spatial` | 10    | 280       | Tasks requiring reasoning about spatial relations  |
| LIBERO-Object  | `libero_object`  | 10    | 280       | Tasks centered on manipulating different objects   |
| LIBERO-Goal    | `libero_goal`    | 10    | 300       | Goal-conditioned tasks with changing targets       |
| LIBERO-90      | `libero_90`      | 90    | 400       | Short-horizon tasks from the LIBERO-100 collection |
| LIBERO-Long    | `libero_10`      | 10    | 520       | Long-horizon tasks from the LIBERO-100 collection  |

  Installing LIBERO-plus **replaces** vanilla LIBERO — it uninstalls `hf-libero`
  so that `import libero` resolves to the LIBERO-plus fork. You cannot have both
  installed at the same time. To switch back to vanilla LIBERO, uninstall the
  fork and reinstall with `pip install -e ".[libero]"`.

## Installation

### System dependencies (Linux only)

```bash
sudo apt install libexpat1 libfontconfig1-dev libmagickwand-dev
```

### Python package

```bash
pip install -e ".[libero]" "robosuite==1.4.1" bddl easydict mujoco wand scikit-image gym
git clone https://github.com/sylvestf/LIBERO-plus.git
cd LIBERO-plus && pip install --no-deps -e .
pip uninstall -y hf-libero  # so `import libero` resolves to the fork
```

LIBERO-plus is installed from its GitHub fork rather than a pyproject extra — the fork ships as a namespace package that pip can't handle, so it must be cloned and added to `PYTHONPATH`. See `docker/Dockerfile.benchmark.libero_plus` for the canonical install. MuJoCo is required, so only Linux is supported.

Set the MuJoCo rendering backend before running evaluation:

```bash
export MUJOCO_GL=egl   # headless / HPC / cloud
```

### Download LIBERO-plus assets

LIBERO-plus ships its extended asset pack separately. Download `assets.zip` from the [Hugging Face dataset](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main) and extract it into the LIBERO-plus package directory:

```bash
# After installing the package, find where it was installed:
python -c "import libero; print(libero.__file__)"
# Then extract assets.zip into &lt;package_root>/libero/assets/
```

## Evaluation

### Default evaluation (recommended)

Evaluate across the four standard suites (10 episodes per task):

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero_plus \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```

### Single-suite evaluation

Evaluate on one LIBERO-plus suite:

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero_plus \
  --env.task=libero_spatial \
  --eval.batch_size=1 \
  --eval.n_episodes=10
```

- `--env.task` picks the suite (`libero_spatial`, `libero_object`, etc.).
- `--env.task_ids` restricts to specific task indices (`[0]`, `[1,2,3]`, etc.). Omit to run all tasks in the suite.
- `--eval.batch_size` controls how many environments run in parallel.
- `--eval.n_episodes` sets how many episodes to run per task.

### Multi-suite evaluation

Benchmark a policy across multiple suites at once by passing a comma-separated list:

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero_plus \
  --env.task=libero_spatial,libero_object \
  --eval.batch_size=1 \
  --eval.n_episodes=10
```

### Control mode

LIBERO-plus supports two control modes — `relative` (default) and `absolute`. Different VLA checkpoints are trained with different action parameterizations, so make sure the mode matches your policy:

```bash
--env.control_mode=relative   # or "absolute"
```

### Policy inputs and outputs

**Observations:**

- `observation.state` — 8-dim proprioceptive features (eef position, axis-angle orientation, gripper qpos)
- `observation.images.image` — main camera view (`agentview_image`), HWC uint8
- `observation.images.image2` — wrist camera view (`robot0_eye_in_hand_image`), HWC uint8

**Actions:**

- Continuous control in `Box(-1, 1, shape=(7,))` — 6D end-effector delta + 1D gripper

### Recommended evaluation episodes

For reproducible benchmarking, use **10 episodes per task** across all four standard suites (Spatial, Object, Goal, Long). This gives 400 total episodes and matches the protocol used for published results.

## Training

### Dataset

A LeRobot-format training dataset for LIBERO-plus is available at:

- [lerobot/libero_plus](https://huggingface.co/datasets/lerobot/libero_plus)

### Example training command

```bash
lerobot-train \
    --policy.type=smolvla \
    --policy.repo_id=${HF_USER}/smolvla_libero_plus \
    --policy.load_vlm_weights=true \
    --dataset.repo_id=lerobot/libero_plus \
    --env.type=libero_plus \
    --env.task=libero_spatial \
    --output_dir=./outputs/ \
    --steps=100000 \
    --batch_size=4 \
    --eval.batch_size=1 \
    --eval.n_episodes=1 \
    --eval_freq=1000
```

## Relationship to LIBERO

LIBERO-plus is a drop-in extension of LIBERO:

- Same Python gym interface (`LiberoEnv`, `LiberoProcessorStep`)
- Same camera names and observation/action format
- Same task suite names
- Installs under the same `libero` Python package name (different GitHub repo)

To use the original LIBERO benchmark, see [LIBERO](./libero) and use `--env.type=libero`.


````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "014b9c87-a47e-46fc-9d8a-e1da87c763c9"
}
```

</details>

---

### System

_source line 101_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Searching for huggingface datasets \"lerobot/libero_spatial\" OR …",
  "usage": {
    "total_tokens": 24667,
    "tool_uses": 12,
    "duration_ms": 41022
  },
  "last_tool_name": "WebSearch",
  "uuid": "4ec05e2b-9ff4-459c-85cd-f6f4017bc1d1",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 102_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015edgA3Z36xavAcV451e7Af`</summary>

```json
{
  "query": "huggingface datasets \"lerobot/libero_spatial\" OR \"lerobot/libero_object\" OR \"lerobot/libero_goal\" OR \"lerobot/libero_90\" site:huggingface.co"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "e5fc8004-6214-41a2-ad4d-f1d7c9cd8fdc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ejiv15JiBk44Et2gVNZ5Vg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4594,
      "cache_read_input_tokens": 20041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4594,
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

_source line 103_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://raw.githubusercontent.com/Lifelong-Robot-…",
  "usage": {
    "total_tokens": 21705,
    "tool_uses": 12,
    "duration_ms": 50201
  },
  "last_tool_name": "WebFetch",
  "uuid": "3549d88b-5be4-42a6-af63-c70edb43cac6",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 104_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GYTyUisRZp1RsmpXM1TYpr`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/lifelong/evaluate.py",
  "prompt": "Extract ALL details about evaluation: what metrics are computed, how success rate is calculated, how many episodes are run, evaluation protocol, output format, and command-line arguments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "b6cb266d-e645-4e59-b059-b0e32d0f0019",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkiyvFRQs4Mtv5a2aqdVrZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 804,
      "cache_creation_input_tokens": 1231,
      "cache_read_input_tokens": 19586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1231,
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

_source line 105_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Fetching https://github.com/sylvestf/LIBERO-plus",
  "usage": {
    "total_tokens": 23114,
    "tool_uses": 9,
    "duration_ms": 46017
  },
  "last_tool_name": "WebFetch",
  "uuid": "6a8c34fd-e192-45d5-94c5-f3cee52a7d44",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 106_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PBsuwnMvyKfQdEfvR9YP4Q`</summary>

```json
{
  "url": "https://github.com/sylvestf/LIBERO-plus",
  "prompt": "Extract the full repository structure, installation commands, configuration details, how to run evaluation, and any code examples. Include exact pip install commands, asset download links, and configuration file paths."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "9d7ed0d6-85c3-46ac-b444-2d73e070ee33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013eJ2NyPG9VENPy3EL2HLdN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 410,
      "cache_creation_input_tokens": 2540,
      "cache_read_input_tokens": 20130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2540,
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

_source line 107_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Searching for LIBERO robosuite MuJoCo built-in camera randomiza…",
  "usage": {
    "total_tokens": 23115,
    "tool_uses": 10,
    "duration_ms": 47009
  },
  "last_tool_name": "WebSearch",
  "uuid": "e2070b3b-db82-4655-89cf-102edb2a5af0",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 108_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016fwVuh2KUdmNnLe8tZkWZV`</summary>

```json
{
  "query": "LIBERO robosuite MuJoCo built-in camera randomization lighting randomization domain randomization config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "c5a2486e-7a44-4f63-8fd3-49c3ded605c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013eJ2NyPG9VENPy3EL2HLdN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 410,
      "cache_creation_input_tokens": 2540,
      "cache_read_input_tokens": 20130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2540,
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

_source line 109_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Searching for site:github.com Lifelong-Robot-Learning LIBERO do…",
  "usage": {
    "total_tokens": 23116,
    "tool_uses": 11,
    "duration_ms": 47422
  },
  "last_tool_name": "WebSearch",
  "uuid": "21e72ab2-b907-44dc-8452-f1c7526ab0fb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 110_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JciYF7tRfPJRqeRRAcxXdu`</summary>

```json
{
  "query": "site:github.com Lifelong-Robot-Learning LIBERO domain randomization camera jitter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "a60d5ca5-3f91-4570-bfd5-fb85b6aeda6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013eJ2NyPG9VENPy3EL2HLdN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 410,
      "cache_creation_input_tokens": 2540,
      "cache_read_input_tokens": 20130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2540,
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

_source line 111 · 2026-05-15T11:12:42.300Z_

<details><summary>↩ Tool result · `toolu_01UpMi2Q7TtsS1NGe8JKHTaK`</summary>

```text
# Observation and Action Space Analysis

Based on the provided code, here's what can be determined about the spaces:

## Observation Space

The code doesn't explicitly define observation dimensions. However, several clues exist:

- **Camera observations**: The environment supports multiple cameras with configurable parameters:
  - Default cameras: `"agentview"` and `"robot0_eye_in_hand"`
  - Resolution: 128×128 pixels (customizable via `camera_heights` and `camera_widths`)
  - Optional depth channels: `camera_depths=False` by default
  - Optional segmentation masks: `camera_segmentations=None` by default

- **Proprioceptive state**: Generated through `"_get_observations()"` and `"_update_observables(force=False)"`, but specific components aren't detailed in this excerpt.

## Action Space

No explicit action space definition appears in the provided code. However, the controller configuration suggests:

- Controller type: `"OSC_POSE"` (default) - indicates operational space control
- Likely includes: position commands, rotation/orientation, and gripper state
- The `"step(action)"` method accepts actions but doesn't specify their structure or dimensionality

## Key Limitation

The actual observation and action space specifications reside in the underlying `robosuite` library and task-specific implementations referenced via `"TASK_MAPPING[self.problem_name]"`, which aren't included in this excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "9bc72f4f-6152-4f27-93af-6340f9d38301"
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-15T11:12:43.258Z_

<details><summary>↩ Tool result · `toolu_01MxUY1crA6Dm5zFD6Me47w2`</summary>

```text
# LIBERO Dataset Download Script Analysis

## Script Overview
This Python script manages downloads for LIBERO robotic manipulation datasets. However, **the actual download URLs, file sizes, and implementation details are not contained in this code snippet**.

## Available Configuration Options

**Download Directory:**
- Default: `get_libero_path("datasets")`
- Customizable via `--download-dir` argument

**Dataset Choices:**
The script supports four dataset options via `--datasets`:
- "all" (default)
- "libero_goal"
- "libero_spatial"
- "libero_object"
- "libero_100"

**Download Source:**
- `--use-huggingface` flag toggles between two sources
- Default: Original download links with expiration warning
- Alternative: Hugging Face hosting

## Implementation Details

The script delegates actual downloading to `download_utils.libero_dataset_download()`, which is imported but not shown. Key functions referenced:
- `libero_dataset_download()` – performs the actual transfers
- `check_libero_dataset()` – verifies downloaded files

The script includes user prompts warning that "original links may lead to failures" and suggests switching to Hugging Face if users decline.

## Missing Information
**URLs, file sizes, and detailed download methods are located in the `download_utils` module**, which is not provided in this excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "deba2294-1748-4cba-b765-9e5348565e71"
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-15T11:12:44.125Z_

<details><summary>↩ Tool result · `toolu_015edgA3Z36xavAcV451e7Af`</summary>

```text
Web search results for query: "huggingface datasets "lerobot/libero_spatial" OR "lerobot/libero_object" OR "lerobot/libero_goal" OR "lerobot/libero_90" site:huggingface.co"

Links: [{"title":"IPEC-COMMUNITY/libero_90_no_noops_lerobot · Dataset converted ideas","url":"https://huggingface.co/datasets/IPEC-COMMUNITY/libero_90_no_noops_lerobot/discussions/2"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"lerobot/libero_spatial_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_spatial_image"},{"title":"Commits · lerobot/libero_goal_image","url":"https://huggingface.co/datasets/lerobot/libero_goal_image/commits/main"}]

Based on the web search results, I found references to LeRobot LIBERO datasets on Hugging Face. The search revealed:

1. lerobot/libero_object_image dataset was created using LeRobot

2. lerobot/libero_spatial_image dataset was created using LeRobot

3. lerobot/libero_goal_image is available on Hugging Face

These datasets appear to be part of the LeRobot framework's LIBERO dataset collection on Hugging Face. The search results also mention discussions about converting LIBERO datasets and comparisons between different LIBERO variants (spatial, goal, object, and the 90-task version). The results indicate that LIBERO has different variants including LIBERO 10, spatial, goal and object datasets.

If you need more specific information about any of these datasets, their documentation, or how to access them, I can search for additional details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "3489cfd3-cbf0-4fc4-a42f-74aba40c2d34"
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-15T11:12:44.399Z_

<details><summary>↩ Tool result · `toolu_01GYTyUisRZp1RsmpXM1TYpr`</summary>

````text
# Evaluation Details Extraction

## Metrics Computed
Two primary metrics are calculated:
1. **Loss**: Test dataset loss (initialized as 0.0, not actively computed in shown code)
2. **Success Rate**: Proportion of successful task completions across parallel environments

## Success Rate Calculation
The implementation runs "20 parallel environments" simultaneously. A task succeeds when the environment signals completion via the `done` flag. The success rate is calculated as: `num_success / env_num` (successful environments divided by total environments).

## Episodes and Evaluation Protocol
- **Parallel rollouts**: "env_num = 20" concurrent environments
- **Maximum steps per evaluation**: "cfg.eval.max_steps" (value not specified in code)
- **Physics simulation**: "5" initial steps with zero actions before policy control begins
- **Termination conditions**: Rollout ends when all environments signal completion or max steps reached

## Output Format
Results are saved as a PyTorch tensor dictionary containing:
```
{"loss": test_loss, "success_rate": success_rate}
```
Saved to: `{save_dir}/{benchmark}_{algo}_{policy}_{seed}_[ep/load]_{task_id}.stats`

## Command-Line Arguments
- `--benchmark`: Task suite selection (required)
- `--task_id`: Target task number (required)
- `--algo`: Learning algorithm (required)
- `--policy`: Policy architecture (required)
- `--seed`: Random seed (required)
- `--ep`: Episode for multitask checkpoints
- `--load_task`: Task checkpoint to load
- `--device_id`: GPU device selection
- `--save-videos`: Optional video recording flag
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "91c5922c-5c16-4e87-ab33-42371828c6a1"
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-15T11:12:47.581Z_

<details><summary>↩ Tool result · `toolu_01JciYF7tRfPJRqeRRAcxXdu`</summary>

```text
Web search results for query: "site:github.com Lifelong-Robot-Learning LIBERO domain randomization camera jitter"

Links: [{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"Issues · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues"},{"title":"Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning"},{"title":"Technical details Regarding LIBERO Dataset · Issue #95 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/95"},{"title":"Issues with Playback · Issue #16 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/16"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"LIBERO-Object image rendering issue: darker floors · Issue #88 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/88"},{"title":"LIBERO/README.md at master · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/blob/master/README.md"},{"title":"Activity · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/activity"},{"title":"collect_demonstrations.py · Issue #48 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/48"}]

The search returned results from the LIBERO GitHub repository and related pages. LIBERO is designed for studying knowledge transfer in multitask and lifelong robot learning problems. It provides a procedural generation pipeline that could generate an infinite number of manipulation tasks, with 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100.

While the search results contain general information about LIBERO, the specific terms "domain randomization" and "camera jitter" do not appear in the returned pages. The results show information about the benchmark structure, setup instructions, and some issues related to rendering and environment setup, but they don't specifically address domain randomization or camera jitter perturbations in LIBERO.

If you're looking for specific documentation about domain randomization or camera jitter features in LIBERO, you may need to check the actual LIBERO codebase files directly on the GitHub repository, or consult the paper or more detailed technical documentation associated with the project.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "e5e92419-de25-4f6a-893c-69a55d572236"
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-15T11:12:47.914Z_

<details><summary>↩ Tool result · `toolu_01PBsuwnMvyKfQdEfvR9YP4Q`</summary>

````text
# LIBERO-Plus Repository Summary

## Overview
LIBERO-Plus is "a generalized benchmark for in-depth robustness analysis of vision-language-action models" offering comprehensive evaluation across 7 perturbation dimensions with 10,030 tasks.

## Installation Commands

```bash
# Clone repository
git clone https://github.com/sylvestf/LIBERO-plus.git
cd LIBERO-plus

# Uninstall existing LIBERO if present

# Install package
pip install -e .

# Install system dependencies
apt install libexpat1
apt install libfontconfig1-dev
apt install libpython3-stdlib
apt-get install libmagickwand-dev

# Install additional Python requirements
pip install -r extra_requirements.txt
```

## Asset Download & Configuration

**Assets Location:** Download from [Hugging Face LIBERO-plus dataset](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main)

**Installation Path:** Extract `assets.zip` to `LIBERO-plus/libero/libero/`

**Configuration File:** `/root/.libero/config.yaml` (verify repo path in `libero/__init__.py`)

**Required Asset Structure:**
```
libero/libero/assets/
├── articulated_objects/
├── new_objects/
├── scenes/
├── stable_hope_objects/
├── stable_scanned_objects/
├── textures/
├── turbosquid_objects/
└── supporting XML/STL files
```

## Evaluation Setup

Modify configuration to set `num_trials_per_task: 1` (adjusted from original 50). Task mappings between IDs, perturbation categories, and difficulty levels are provided in `.libero/libero/benchmark/task_classification.json`.

## Additional Resources

- **RLDS Training Dataset:** Available on Hugging Face
- **Fine-tuned Model:** OpenVLA-OFT weights after mix-SFT provided
- **LeRobot Dataset:** Alternative training dataset available

## Key Performance Metrics

Top-performing model (OpenVLA-OFT+) achieves 79.6% average across perturbation categories, with particularly strong results in camera robustness (92.8%) and light conditions (94.9%).
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "58463115-31e4-4adc-a26d-b5a467a2a9fc"
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-15T11:12:48.674Z_

<details><summary>↩ Tool result · `toolu_016fwVuh2KUdmNnLe8tZkWZV`</summary>

```text
Web search results for query: "LIBERO robosuite MuJoCo built-in camera randomization lighting randomization domain randomization config"

Links: [{"title":"Demo Showcases — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/demos.html"},{"title":"robosuite/robosuite/utils/mjmod.py at master · ARISE-Initiative/robosuite","url":"https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/utils/mjmod.py"},{"title":"Environments — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/modules/environments.html"},{"title":"Sim-to-Real Transfer — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/algorithms/sim2real.html"},{"title":"Changelog — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/changelog.html"},{"title":"robosuite.utils package — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/source/robosuite.utils.html"},{"title":"robosuite | robosuite: A Modular Simulation Framework and Benchmark for Robot Learning","url":"https://robosuite.ai/"},{"title":"GitHub - ARISE-Initiative/robosuite: robosuite: A Modular Simulation Framework and Benchmark for Robot Learning · GitHub","url":"https://github.com/ARISE-Initiative/robosuite"},{"title":"robosuite · PyPI","url":"https://pypi.org/project/robosuite/"},{"title":"GitHub - Robot-Learning-Library/robolite: This is a fork of Surreal Robotics Suite that enables support to domain randomization and inverse kinematics (IK).","url":"https://github.com/Robot-Learning-Library/robolite"}]

Based on the search results, here's what I found about LIBERO, robosuite, MuJoCo, and domain randomization features:

## Domain Randomization in Robosuite

Domain randomization can be easily enabled by wrapping an environment with the DomainRandomizationWrapper, with randomization functionality focusing on visual variations, including colors, textures, and camera viewpoints.

## Randomization Modders

Robosuite provides three main Modders: CameraModder for controlling camera parameters including FOV and pose, TextureModder for controlling visual objects' appearances including texture and material properties, and LightingModder for controlling lighting parameters including light source properties and pose.

## Camera Randomization Parameters

The randomization system includes parameters like camera_names (list of camera names to use for randomization, with all cameras used if not provided) and rotation_perturbation_size (magnitude of camera rotation perturbations in axis-angle, defaulting to around 5 degrees).

## Documentation and Examples

The demo_domain_randomization.py script showcases domain randomization functionality.

The search results provide information about robosuite's built-in camera, lighting, and visual randomization capabilities, but don't include specific information about LIBERO itself. LIBERO is a benchmark that builds on top of robosuite, so these randomization features would be available for use with LIBERO environments as well.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "0c0bb3c2-d800-4325-bdad-a6e61f9a0b1d"
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
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://raw.githubusercontent.com/Lifelong-Robot-…",
  "usage": {
    "total_tokens": 23229,
    "tool_uses": 13,
    "duration_ms": 59444
  },
  "last_tool_name": "WebFetch",
  "uuid": "e6d21f33-c6d0-49d2-be24-29593b8abb70",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 119_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014Mr73JUFM8GX2NiRZSm6s6`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/libero/benchmark/libero_suite.py",
  "prompt": "Extract ALL details about the benchmark suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90, LIBERO-10. How many tasks in each? What are the task descriptions? How are they defined?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "97eb9901-4cc4-4248-b0e5-ef28046e2aab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XaLnE3c4KnzRgpW9v1WHHL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2321,
      "cache_read_input_tokens": 20817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2321,
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

_source line 120 · 2026-05-15T11:12:49.362Z_

<details><summary>↩ Tool result · reported error · `toolu_014Mr73JUFM8GX2NiRZSm6s6`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "a4e48c2d-e4df-4dc1-92a2-6f8cc52e946e",
  "tool_use_result": "Error: Request failed with status code 404"
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
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://raw.githubusercontent.com/Lifelong-Robot-…",
  "usage": {
    "total_tokens": 23232,
    "tool_uses": 14,
    "duration_ms": 60842
  },
  "last_tool_name": "WebFetch",
  "uuid": "4e64af38-fc29-4736-b74c-3f93e824040e",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 122_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GDu1zwtiF5uxqXDyw6QjPv`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/libero/benchmark/__init__.py",
  "prompt": "Extract all benchmark suite names, class definitions, task counts, and how benchmarks are registered or accessed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "e0aa1476-e7b4-423e-b58d-8e710c093ce1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XaLnE3c4KnzRgpW9v1WHHL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2321,
      "cache_read_input_tokens": 20817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2321,
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

_source line 123_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://raw.githubusercontent.com/Lifelong-Robot-…",
  "usage": {
    "total_tokens": 23235,
    "tool_uses": 15,
    "duration_ms": 61992
  },
  "last_tool_name": "WebFetch",
  "uuid": "98e03d46-ce29-4e44-b17b-ad65b02484fd",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 124_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BjfPHpyofVoKcU2kiwmrn6`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/lifelong/datasets.py",
  "prompt": "Extract ALL details about the dataset class: HDF5 data structure, observation keys, action dimensions, image dimensions, proprioceptive state components, how data is loaded and processed. Be extremely thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "b74eaa4b-a4f4-4d8a-9fc7-0a3eff6eb8d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XaLnE3c4KnzRgpW9v1WHHL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2321,
      "cache_read_input_tokens": 20817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2321,
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

_source line 125_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Fetching https://robosuite.ai/docs/algorithms/sim2real.html",
  "usage": {
    "total_tokens": 25584,
    "tool_uses": 12,
    "duration_ms": 58860
  },
  "last_tool_name": "WebFetch",
  "uuid": "740619c3-8fdb-4b02-b108-3464234713e6",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 126_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EQVJbHhLUGi7rXZfsu1QcS`</summary>

```json
{
  "url": "https://robosuite.ai/docs/algorithms/sim2real.html",
  "prompt": "Extract all details about domain randomization in robosuite: CameraModder, TextureModder, LightingModder parameters, DomainRandomizationWrapper usage, configuration options, parameter ranges, and code examples. Include exact API details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "5b8b5a3f-9028-4087-91cb-c8b67d5f9d9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BagSeBG8mMDsQNn9y1Jgtg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 802,
      "cache_creation_input_tokens": 2074,
      "cache_read_input_tokens": 22670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2074,
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

_source line 127 · 2026-05-15T11:12:54.462Z_

<details><summary>↩ Tool result · `toolu_01GDu1zwtiF5uxqXDyw6QjPv`</summary>

```text
# LIBERO Benchmark Suite Overview

## Benchmark Suite Names
The codebase defines five core suites: `libero_spatial`, `libero_object`, `libero_goal`, `libero_90`, and `libero_10`.

## Class Definitions
Six benchmark classes are registered via the `@register_benchmark` decorator:

- **LIBERO_SPATIAL**: Handles spatial reasoning tasks
- **LIBERO_OBJECT**: Focuses on object-centric tasks
- **LIBERO_GOAL**: Addresses goal-oriented tasks
- **LIBERO_90**: Contains 90 combined tasks (uses all available tasks)
- **LIBERO_10**: Manages 10-task suites with predefined orderings
- **LIBERO_100**: Includes 100 total tasks

## Task Counts
The `libero_spatial`, `libero_object`, and `libero_goal` suites each contain 10 tasks. The `libero_90` contains 90 tasks, while `libero_100` contains 100 tasks. Task counts are dynamically determined through `get_num_tasks()`.

## Registration & Access
The registration system uses a case-insensitive mapping: "benchmark names are registered automatically via the decorator and accessed through `get_benchmark()`" which queries `BENCHMARK_MAPPING`. The `get_benchmark_dict()` function provides the complete registry with optional help display.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "1c330cf6-03f1-4a02-9237-bb29d2db8b3d"
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-15T11:12:54.792Z_

<details><summary>↩ Tool result · `toolu_012up7eAufC6DCPqD75Gt5GZ`</summary>

````text
# LIBERO Dataset Card

## Dataset Overview

**Dataset Name:** `HuggingFaceVLA/libero`

**Source:** Hugging Face Datasets

**Task Category:** Robotics

**Modalities:** Image, Time-series

**Format:** Parquet

**License:** Apache 2.0

---

## Dataset Statistics

| Metric | Value |
|--------|-------|
| **Total Rows** | 273,000 |
| **Size Category** | 100K - 1M |
| **Splits** | 1 (train) |
| **Episodes** | 148 |
| **Tasks** | 10 |
| **Subset** | default |

---

## Data Structure

### Observation Fields
- **observation.images.image** - Primary camera image (256×256 pixels)
- **observation.images.image2** - Secondary camera image (256×256 pixels)
- **observation.state** - Robot state vector (8 floating-point values)

### Action Fields
- **action** - Action vector (7 elements representing robot control commands)

### Metadata Fields
- **timestamp** - float32 (0-45.4 range)
- **frame_index** - int64 (frame within episode)
- **episode_index** - int64 (0-147, 148 total episodes)
- **task_index** - int64 (0-9, 10 tasks)
- **index** - int64 (global row index)

---

## Sample Data Examples

From the viewer, sample observations show:
- Robot arm in tabletop manipulation scenario
- Dual RGB camera views of workspace
- Continuous 7-DOF joint commands
- State includes position, orientation, and gripper status

**Example action structure:** `[0.016, 0, 0, 0, 0, 0, -1]` (normalized joint velocities + gripper)

---

## How to Load the Dataset

### Using Hugging Face Datasets Library

```python
from datasets import load_dataset

# Load the full dataset
dataset = load_dataset("HuggingFaceVLA/libero")

# Access train split
train_data = dataset['train']

# Inspect a sample
sample = train_data[0]
print(sample.keys())
# Output: dict_keys(['observation.images.image', 'observation.images.image2', 
#                     'observation.state', 'action', 'timestamp', 'frame_index', 
#                     'episode_index', 'task_index', 'index'])
```

### Using LeRobot Integration

```python
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset

# Load with LeRobot
dataset = LeRobotDataset("HuggingFaceVLA/libero")

# Iterate through episodes
for episode in dataset:
    observations = episode['observation']
    actions = episode['action']
    # Process episode data
```

---

## Data Format Details

### Image Data
- **Resolution:** 256×256 pixels
- **Format:** RGB images
- **Encoding:** JPEG (auto-converted to Parquet)
- **Camera Count:** 2 (primary + secondary views)

### State Vector (8-dim)
Typically represents:
- 3D end-effector position (x, y, z)
- 4D orientation (quaternion or similar)
- Gripper state or additional joint angles

### Action Vector (7-dim)
Typically represents:
- 6 DOF continuous control (xyz position + rotation)
- 1 gripper binary/continuous command (-1 to 1)

---

## Tags & Libraries

- **Associated Library:** LeRobot
- **Data Format Support:** 
  - Datasets (HuggingFace)
  - Dask (for distributed processing)
  - Croissant (metadata format)

---

## Dataset Features

✅ **Multi-episode structure** - 148 episodes organized by task  
✅ **Dual camera views** - Enriched visual observations  
✅ **Long horizons** - Up to 454 frames per episode  
✅ **Parquet format** - Efficient columnar storage  
✅ **LeRobot compatible** - Integrated with robot learning framework  

---

## Usage Recommendations

### For Training Vision-Language-Action Models
```python
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
from torch.utils.data import DataLoader

# Load dataset
dataset = LeRobotDataset("HuggingFaceVLA/libero")

# Create dataloader for training
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

for batch in dataloader:
    images = batch['observation']['images']  # [B, T, 2, 256, 256, 3]
    actions = batch['action']                # [B, T, 7]
    # Train your model
```

### For Episode-Level Analysis
```python
dataset = load_dataset("HuggingFaceVLA/libero", split="train")

# Filter by task
task_0_data = dataset.filter(lambda x: x['task_index'] == 0)

# Group by episode
episodes = {}
for sample in dataset:
    ep_id = sample['episode_index']
    if ep_id not in episodes:
        episodes[ep_id] = []
    episodes[ep_id].append(sample)
```

---

## Key References

- **Organization:** HuggingFaceVLA (Vision Language Action Models Research)
- **Related Work:** LIBERO - Long Horizon Vision-Language-Action Benchmark
- **Community:** [Discussions](https://huggingface.co/datasets/HuggingFaceVLA/libero/discussions) available on dataset page
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "ace411ce-3a5b-41d0-b3fb-cb120e7bb8b9"
}
```

</details>

---

### System

_source line 129_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Fetching https://github.com/ARISE-Initiative/robosuite/blo…",
  "usage": {
    "total_tokens": 25585,
    "tool_uses": 13,
    "duration_ms": 60704
  },
  "last_tool_name": "WebFetch",
  "uuid": "ca1824d1-6393-4793-a814-a0831095321a",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 130_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Dvd7vLwaSK4nd3scbSqZNa`</summary>

```json
{
  "url": "https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/utils/mjmod.py",
  "prompt": "Extract the CameraModder, TextureModder, and LightingModder class definitions. Include all parameters they can modify, default values, and method signatures. Focus on what visual properties can be randomized."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "acf32032-82c0-47cf-beec-39552c1de4ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BagSeBG8mMDsQNn9y1Jgtg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 802,
      "cache_creation_input_tokens": 2074,
      "cache_read_input_tokens": 22670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2074,
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

_source line 131_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Fetching https://huggingface.co/datasets/Sylvest/LIBERO-pl…",
  "usage": {
    "total_tokens": 25586,
    "tool_uses": 14,
    "duration_ms": 61786
  },
  "last_tool_name": "WebFetch",
  "uuid": "4599b5f8-59ae-45b2-b0f9-899d1aa8ab5d",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 132_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GPqQRYBRGsJeYhttZTzWCi`</summary>

```json
{
  "url": "https://huggingface.co/datasets/Sylvest/LIBERO-plus",
  "prompt": "Extract all details about the LIBERO-plus dataset: file structure, download instructions, dataset contents, how the training data is organized, and any usage instructions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "1db165f1-52bd-464f-8c35-fa915fb533b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BagSeBG8mMDsQNn9y1Jgtg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 802,
      "cache_creation_input_tokens": 2074,
      "cache_read_input_tokens": 22670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2074,
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

_source line 133 · 2026-05-15T11:12:57.961Z_

<details><summary>↩ Tool result · `toolu_01BjfPHpyofVoKcU2kiwmrn6`</summary>

```text
# Dataset Class Details Analysis

## Data Loading Architecture

The code provides a wrapper around robomimic's `SequenceDataset` class. The primary function `get_dataset()` loads HDF5 demonstration files and initializes observation utilities.

## HDF5 Structure

The HDF5 file organization relies on:
- **Observation keys**: Dynamically extracted from `obs_modality` dictionary (which groups observations by modality type)
- **Action data**: Loaded as a standard dataset key labeled `"actions"`
- **Shape metadata**: Extracted via `FileUtils.get_shape_metadata_from_dataset()`, retrieving dimensions for all observation keys

The code explicitly notes: *"robomimic's SequenceDataset has two properties: seq_len and frame_stack, we should in principle use seq_len, but the paddings of the two are different"*, indicating the internal complexity of sequence handling.

## Data Processing Parameters

Configuration options include:
- **Sequence length** and **frame stacking**: Handled separately with independent padding strategies
- **Caching mode** (`hdf5_cache_mode="low_dim"`): Controls in-memory dataset caching to minimize file I/O
- **Padding**: Both sequence length and frame stack use padding; no pad masks are generated

## Observation Modality

The function accepts `obs_modality` as a nested dictionary where modality names map to lists of observation keys. Specific dimensions (image sizes, proprioceptive state components) are extracted from shape metadata but aren't hardcoded in this file.

## Dataset Wrapper Classes

Three wrapper implementations manage multi-task and truncated scenarios while preserving the underlying sequence structure and adding task embeddings or buffer constraints.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "edff0547-aea2-425c-8169-e01fc24f5c25"
}
```

</details>

---

### System

_source line 134_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Searching for site:huggingface.co/datasets/lerobot libero",
  "usage": {
    "total_tokens": 29165,
    "tool_uses": 13,
    "duration_ms": 59260
  },
  "last_tool_name": "WebSearch",
  "uuid": "25397150-357a-4277-a78c-b455255c5d55",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 135_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GX3R96zx3DnErZrK1jjrDn`</summary>

```json
{
  "query": "site:huggingface.co/datasets/lerobot libero"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "833cea9b-343c-40ef-a0fe-e73035cefaf0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGAKNCL7NpNnAWgFQfpZeY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2721,
      "cache_creation_input_tokens": 1776,
      "cache_read_input_tokens": 24635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1776,
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

_source line 136_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Searching for site:huggingface.co/datasets/physical-intelligenc…",
  "usage": {
    "total_tokens": 29166,
    "tool_uses": 14,
    "duration_ms": 60178
  },
  "last_tool_name": "WebSearch",
  "uuid": "3b7156c8-0cea-43cc-a274-c6167938484b",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 137_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JPTXTejJTpeKuxxGb1Yfdh`</summary>

```json
{
  "query": "site:huggingface.co/datasets/physical-intelligence/libero lerobot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "ac743b7a-1cfa-47fc-b7ad-aed10c8784cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGAKNCL7NpNnAWgFQfpZeY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2721,
      "cache_creation_input_tokens": 1776,
      "cache_read_input_tokens": 24635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1776,
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

_source line 138 · 2026-05-15T11:12:58.982Z_

<details><summary>↩ Tool result · `toolu_01EQVJbHhLUGi7rXZfsu1QcS`</summary>

```text
# Domain Randomization in robosuite

Based on the documentation, robosuite provides three primary `Modder` classes for visual domain randomization:

## Visual Modders

**CameraModder**: Handles camera parameters including field of view and positioning adjustments.

**TextureModder**: Controls the appearance of simulation objects through texture and material property modifications.

**LightingModder**: Manages lighting environment by adjusting light source characteristics and their spatial placement.

The documentation notes that these tools enable users to either "directly override default simulation settings, or to randomize their respective properties mid-sim."

## Dynamics Randomization

The `DynamicsModder` class addresses physics parameter variation across four categories:

**Global Parameters** (Opt): density and viscosity of the medium

**Body Parameters**: position, quaternion orientation, inertia components, and mass

**Geom Parameters**: friction coefficients (sliding, torsional, rolling), contact solver values (solref), and impedance settings (solimp)

**Joint Parameters**: stiffness, friction loss, damping, and armature values

## API Usage Pattern

The basic workflow involves creating the modder instance, calling `.mod()` to adjust parameters, then invoking `.update()` to propagate changes into the simulation. The documentation includes a code example demonstrating modification of cube mass and friction values, followed by restoration of defaults.

The system includes "sanity checks to prevent presumably undesired / non-sensical behavior" such as preventing damping additions to free joints.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "6a5ffa9d-a3ea-46d4-913e-7125ae2bd719"
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
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Fetching https://huggingface.co/datasets/lerobot/libero_10…",
  "usage": {
    "total_tokens": 29167,
    "tool_uses": 15,
    "duration_ms": 60968
  },
  "last_tool_name": "WebFetch",
  "uuid": "22fc194d-cb5b-4027-a7bf-2d6478984ccd",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 140_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013HpVbFEdpAw7pEi2TEpows`</summary>

```json
{
  "url": "https://huggingface.co/datasets/lerobot/libero_10_image",
  "prompt": "Extract dataset card info: name, size, episodes, tasks, features, format. Include all metadata."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "fcfa64b7-1bc0-4412-8652-d89d2138cf97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGAKNCL7NpNnAWgFQfpZeY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2721,
      "cache_creation_input_tokens": 1776,
      "cache_read_input_tokens": 24635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1776,
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

_source line 141 · 2026-05-15T11:13:01.308Z_

<details><summary>↩ Tool result · `toolu_01Dvd7vLwaSK4nd3scbSqZNa`</summary>

```text
# Visual Property Randomization in Robosuite

## LightingModder

The LightingModder class enables domain randomization for light sources. Key parameters include:

**Modifiable Properties:**
- Position (with `position_perturbation_size=0.1`)
- Direction (with `direction_perturbation_size=0.35`)
- Specular attribute (with `specular_perturbation_size=0.1`)
- Ambient attribute (with `ambient_perturbation_size=0.1`)
- Diffuse attribute (with `diffuse_perturbation_size=0.1`)
- Active status (on/off)

**Key Methods:** `randomize()`, `save_defaults()`, `restore_defaults()`, and individual getters/setters for each property.

## CameraModder

This modder adjusts camera viewing parameters during simulation. Configurable aspects are:

**Modifiable Properties:**
- Position (with `position_perturbation_size=0.01`)
- Rotation/orientation via quaternions (with `rotation_perturbation_size=0.087`)
- Field of view (fovy) in degrees (with `fovy_perturbation_size=5.0`)

**Key Methods:** `randomize()`, `_randomize_position()`, `_randomize_rotation()`, `_randomize_fovy()`, plus accessor methods for position, quaternion orientation, and fovy values.

## TextureModder

This comprehensive modder handles surface appearance changes. As noted, "in order for the textures to take full effect, you'll need to set the rgba values for all materials to [1, 1, 1, 1]."

**Modifiable Properties:**
- RGB colors (with `local_rgb_interpolation=0.1`)
- Texture patterns: RGB, checker, noise, gradient
- Material properties: reflectance, shininess, specular (with `local_material_interpolation=0.2`)
- Skybox textures (when `randomize_skybox=True`)

**Key Methods:** `randomize()`, `rand_rgb()`, `rand_checker()`, `rand_gradient()`, `rand_noise()`, plus material and texture management functions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "8249f956-94d0-469a-96a8-f0ac91e11816"
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-15T11:13:02.920Z_

<details><summary>↩ Tool result · `toolu_01JPTXTejJTpeKuxxGb1Yfdh`</summary>

```text
Web search results for query: "site:huggingface.co/datasets/physical-intelligence/libero lerobot"

Links: [{"title":"physical-intelligence/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/physical-intelligence/libero"},{"title":"README.md · physical-intelligence/libero at main","url":"https://huggingface.co/datasets/physical-intelligence/libero/blob/main/README.md"},{"title":"physical-intelligence/libero at main","url":"https://huggingface.co/datasets/physical-intelligence/libero/tree/main"},{"title":"physical-intelligence/libero · Description of the dataset features","url":"https://huggingface.co/datasets/physical-intelligence/libero/discussions/1"}]

I found results for the physical-intelligence/libero dataset on Hugging Face. Here's what the search revealed:

The libero dataset was created using LeRobot and combines four individual Libero datasets: Libero-Spatial, Libero-Object, Libero-Goal and Libero-10, all converted into LeRobot format. The dataset is available at https://huggingface.co/datasets/physical-intelligence/libero and has a size of approximately 34.9 GB.

The dataset is licensed under CC-BY-4.0 and is categorized as a robotics dataset with tags for LeRobot, libero, panda, and rlds. The data is stored in Parquet format.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "28bab1c7-a00c-40a6-b01b-c03a8247d371"
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-15T11:13:03.220Z_

<details><summary>↩ Tool result · `toolu_01GX3R96zx3DnErZrK1jjrDn`</summary>

```text
Web search results for query: "site:huggingface.co/datasets/lerobot libero"

Links: [{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"lerobot/libero_10_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_10_image"},{"title":"lerobot/libero_spatial_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_spatial_image"},{"title":"Commits · lerobot/libero_goal_image","url":"https://huggingface.co/datasets/lerobot/libero_goal_image/commits/main"},{"title":"lerobot/xarm_lift_medium at main","url":"https://huggingface.co/datasets/lerobot/xarm_lift_medium/tree/main"},{"title":"lerobot/config_examples · add_configs","url":"https://huggingface.co/datasets/lerobot/config_examples/discussions/1/files"},{"title":"lerobot/droid_1.0.1 at main","url":"https://huggingface.co/datasets/lerobot/droid_1.0.1/tree/main"},{"title":"lerobot/example_hil_serl_dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/example_hil_serl_dataset"},{"title":"lerobot/austin_sirius_dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/austin_sirius_dataset"}]

The search results show that there are several LIBERO-related datasets available on Hugging Face under the LeRobot organization. The search found:

1. **lerobot/libero** - The main LIBERO dataset
2. **lerobot/libero_object_image** - An image variant of the LIBERO dataset
3. **lerobot/libero_10_image** - Another image-based variant (last updated August 3, 2025)
4. **lerobot/libero_spatial_image** - A spatial image variant (last updated August 21, 2025)
5. **lerobot/libero_goal_image** - A goal-based image variant (last updated February 27, 2025)

All of these datasets are hosted on the Hugging Face platform as part of the LeRobot project. The search results indicate that they are advancing and democratizing artificial intelligence through open source and open science.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "a904f30c-8c50-4766-9940-59a08764de11"
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
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://raw.githubusercontent.com/Lifelong-Robot-…",
  "usage": {
    "total_tokens": 24523,
    "tool_uses": 16,
    "duration_ms": 73573
  },
  "last_tool_name": "WebFetch",
  "uuid": "867cc139-aa15-4fcd-ae07-b1067b29c9f2",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 145_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UbZp4kqYQgpbBNMLkSpkCp`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/lifelong/main.py",
  "prompt": "Extract ALL details: default configuration values for observation space (image size, obs keys like agentview_image, robot0_eye_in_hand_image, robot0_joint_pos, robot0_gripper_qpos, etc.), action dimensions, training parameters, evaluation settings (number of eval episodes, max steps), and any other technical specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "fd38556f-f2df-40a8-b2c6-4f5b56fbaa10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjWeGaDY8F64wnpK5JXb5b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1221,
      "cache_read_input_tokens": 23138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1221,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 146_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://raw.githubusercontent.com/Lifelong-Robot-…",
  "usage": {
    "total_tokens": 24590,
    "tool_uses": 17,
    "duration_ms": 75827
  },
  "last_tool_name": "WebFetch",
  "uuid": "08812a69-f8d2-4e36-b35a-6ead0851c349",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 147_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RHefgmEnT7wE6GzJNy6HN6`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/lifelong/algos/base.py",
  "prompt": "Extract details about: observation processing (what obs keys are used, dimensions), action space dimensions, policy output format, evaluation rollout procedure, success rate computation, and any other technical details about how the agent interacts with the environment."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "65d5848f-691b-40ac-9097-36ece90512bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjWeGaDY8F64wnpK5JXb5b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1221,
      "cache_read_input_tokens": 23138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1221,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 148_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Searching for LIBERO benchmark observation space action space 7…",
  "usage": {
    "total_tokens": 24657,
    "tool_uses": 18,
    "duration_ms": 76068
  },
  "last_tool_name": "WebSearch",
  "uuid": "21b06d0d-ac7e-4011-b9cb-c554338284da",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 149_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Wp4HWuywiywzByA2vgVEb2`</summary>

```json
{
  "query": "LIBERO benchmark observation space action space 7-dimensional joint position gripper robosuite hdf5 format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "47caf310-c8fd-48a5-ac2a-01272730da5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjWeGaDY8F64wnpK5JXb5b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1221,
      "cache_read_input_tokens": 23138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1221,
        "ephemeral_1h_input_tokens": 0
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

_source line 150 · 2026-05-15T11:13:07.228Z_

<details><summary>↩ Tool result · `toolu_01GPqQRYBRGsJeYhttZTzWCi`</summary>

````text
# LIBERO-plus Dataset Details

## Overview
LIBERO-plus is a comprehensive robustness benchmark for Vision-Language-Action (VLA) models containing **10,030 tasks** across 7 perturbation dimensions. It extends the original LIBERO benchmark with systematic robustness evaluation.

## File Structure

After extraction, the directory structure should be:

```
LIBERO-plus/
└── libero/
    └── libero/
        └── assets/
            ├── articulated_objects/
            ├── new_objects/
            ├── scenes/
            ├── stable_hope_objects/
            ├── stable_scanned_objects/
            ├── textures/
            ├── turbosquid_objects/
            ├── serving_region.xml
            ├── wall_frames.stl
            └── wall.xml
```

## Installation Instructions

```bash
# Clone the repository
git clone https://github.com/sylvestf/LIBERO-plus.git
cd LIBERO-plus

# Install system dependencies
apt install libexpat1
apt install libfontconfig1-dev
apt install libpython3-stdlib
apt-get install libmagickwand-dev

# Install Python package
pip install -e .
pip install -r extra_requirements.txt
```

**Note:** If you have the original LIBERO installed, uninstall it first. Update the config path at `/root/.libero/config.yaml`.

## Dataset Contents

### 7 Perturbation Dimensions

1. **Objects Layout** - Confounding objects and target object displacement
2. **Camera Viewpoints** - Position, orientation, and field-of-view changes
3. **Robot Initial States** - Manipulator initial pose variations
4. **Language Instructions** - LLM-based instruction rewriting
5. **Light Conditions** - Intensity, direction, color, and shadow variations
6. **Background Textures** - Scene and surface appearance changes
7. **Sensor Noise** - Photometric distortions and image degradation

### Total Size
**6.4 GB** with 1,591 downloads

## Training Data

**Location:** [LIBERO-plus RLDS Dataset](https://huggingface.co/datasets/Sylvest/libero_plus_rlds/tree/main)

**Pre-trained Model:** [OpenVLA-7B-OFT Fine-tuned](https://huggingface.co/Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata/tree/main)

## Download Instructions

1. Download assets from the [Hugging Face LIBERO-plus repository](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main)
2. Unzip `assets.zip` to `LIBERO-plus/libero/libero/` path
3. Update config file path if needed

## Usage Instructions

### Evaluation

```python
# Modify your configuration
# Change: num_trials_per_task: 50 → num_trials_per_task: 1
```

The evaluation method is nearly identical to LIBERO; only adjust `num_trials_per_task` from 50 to 1 in your configuration.

### Key Usage Note

> "You can simply replace the original `libero` with a `pip install -e .` without modifying your code."

## Evaluated Models

- OpenVLA and variants (OFT, OFT_w, OFT_m)
- π₀ and π₀-fast
- Nora, WorldVLA, UniVLA, RIPT-VLA

## Resources

- 📄 **Paper:** [arXiv:2510.13626](https://arxiv.org/pdf/2510.13626v1)
- 🏗️ **Repository:** [GitHub](https://github.com/sylvestf/LIBERO-plus)
- 🌐 **Website:** [Project Page](https://sylvestf.github.io/LIBERO-plus)
- 📁 **Training Dataset:** [LIBERO-plus RLDS](https://huggingface.co/datasets/Sylvest/libero_plus_rlds)

## Citation

```bibtex
@article{fei25libero-plus,
    title={LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models},
    author={Senyu Fei and Siyin Wang and Junhao Shi and others},
    journal = {arXiv preprint arXiv:2510.13626},
    year={2025},
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "ca567609-5b88-46b6-a5b4-97c1d6b9f928"
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-15T11:13:08.255Z_

<details><summary>↩ Tool result · `toolu_01UbZp4kqYQgpbBNMLkSpkCp`</summary>

```text
# Configuration Details Analysis

Based on the provided code, I cannot extract the specific default values you requested because **this script does not contain them**. Here's what I found:

## What the Code Does
This is a lifelong learning training orchestrator that loads configuration from external sources via Hydra: `"@hydra.main(config_path="../configs", config_name="config", version_base=None)"`

## Configuration Sources (Not Shown)
The actual defaults are defined in:
- YAML configuration files in the `../configs` directory
- The benchmark definitions loaded via `get_benchmark()`
- Dataset specifications from `get_dataset()`

## Parameters Referenced But Not Defined Here
The script *references* these config values without defining them:
- `cfg.data.obs.modality` (observation modality)
- `cfg.data.seq_len` (sequence length)
- `cfg.data.task_group_size` (grouping parameter)
- `cfg.train.n_epochs` (training epochs)
- `cfg.eval.n_eval` (evaluation episodes)
- `cfg.eval.eval_every` (evaluation frequency)
- `cfg.seed` (random seed)

## To Find Actual Specifications
You would need to examine:
1. The YAML configuration files in the `configs/` directory
2. The benchmark class implementation
3. The dataset loading module (`libero/lifelong/datasets`)

The code shows this is part of the LIBERO (Long-horizon Lifelong Robotic Learning) framework, but the technical specifications are stored elsewhere in the project structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "0aec0836-2910-4f26-b531-06f9faf3fca9"
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-15T11:13:08.722Z_

<details><summary>↩ Tool result · `toolu_013HpVbFEdpAw7pEi2TEpows`</summary>

````text
# LeRobot LIBERO-10 Dataset Card

## Basic Information
- **Name**: lerobot/libero_10_image
- **Organization**: LeRobot
- **License**: Apache 2.0
- **Repository**: Hugging Face Datasets

## Dataset Size & Structure
- **Total Rows**: 101,000 (101k rows)
- **Size Category**: 100K - 1M
- **Format**: Parquet (auto-converted)
- **Split**: Single training split

## Metadata

### Tasks
- **Primary Task**: Robotics
- **Task Count**: 10 tasks (indices 0-9)
- **Episodes**: 148 episodes (episode_index range: 0-147)

### Modalities
- Image (observation cameras)
- Time-series (state and action sequences)

### Features

#### Observations
- **observation.images.image**: 256×256 pixel RGB images (main camera)
- **observation.images.wrist_image**: 256×256 pixel RGB images (wrist camera)
- **observation.state**: List of 8 float values (robot state/joint positions)

#### Actions
- **action**: List of 7 float values (robot control commands)
  - Typically includes 6 continuous values + 1 discrete gripper value (-1, 0, 1)

#### Metadata
- **timestamp**: Float32 (0-45.4 range, in seconds)
- **frame_index**: Int64 (frame number within episode, 0-454)
- **episode_index**: Int64 (which episode, 0-147)
- **task_index**: Int64 (which task, 0-9)
- **index**: Int64 (global row index, 0-40.3k)

## Data Characteristics

### Sample Data Structure
```
Frame 0:
  - Timestamp: 0.0
  - State: [-0.053, 0.007, 0.678, 3.141, 0.002, -0.090, 0.039, -0.039]
  - Action: [0.016, 0, 0, 0, 0, 0, -1]
  - Episode: 0, Task: 0
```

### Action Space Pattern
- First 6 values: continuous control (typically normalized)
- Last value: discrete gripper control (-1 = open, 0 = maintain, 1 = close)

## Libraries & Tools
- **Datasets**: Hugging Face Datasets library
- **Dask**: Distributed computing support
- **Polars**: DataFrames support

## Availability
- **Viewer**: Interactive Data Studio available
- **Community**: 4 discussions/comments
- **Download**: Available via Hugging Face Hub (xet protocol supported)
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "ac53395d-c0b4-4f84-8ae4-92f092956a81"
}
```

</details>

---

### System

_source line 153_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Searching for robosuite DomainRandomizationWrapper example code…",
  "usage": {
    "total_tokens": 28036,
    "tool_uses": 15,
    "duration_ms": 76628
  },
  "last_tool_name": "WebSearch",
  "uuid": "d0aad6a3-1459-4a88-bee8-ea4cc5d58186",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 154_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BqbiFe79oqYoM9EKEEJnm2`</summary>

```json
{
  "query": "robosuite DomainRandomizationWrapper example code camera_names randomize_color randomize_camera"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "40102fe4-9856-47f3-8836-2428a669a2d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bcg3e7hKqM6XFSjemhxDjW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3249,
      "cache_read_input_tokens": 24744,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3249,
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

_source line 155_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Searching for LIBERO-Plus training augmentation reuse perturbat…",
  "usage": {
    "total_tokens": 28037,
    "tool_uses": 16,
    "duration_ms": 77142
  },
  "last_tool_name": "WebSearch",
  "uuid": "a1594840-7c31-452e-ad76-6541e66d006c",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 156_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011PMJHQNu2JmfTbUvAjCCtZ`</summary>

```json
{
  "query": "LIBERO-Plus training augmentation reuse perturbation training time data augmentation robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "0094bb74-c15f-4874-8be1-a4f8a924965b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bcg3e7hKqM6XFSjemhxDjW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3249,
      "cache_read_input_tokens": 24744,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3249,
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

_source line 157_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Searching for github huggingface lerobot \"convert_libero\" OR \"l…",
  "usage": {
    "total_tokens": 31257,
    "tool_uses": 16,
    "duration_ms": 73786
  },
  "last_tool_name": "WebSearch",
  "uuid": "a15da221-13bd-4556-a8a5-a974f0990e0f",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 158_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012cLX94GQVwoky5nrzNScrZ`</summary>

```json
{
  "query": "github huggingface lerobot \"convert_libero\" OR \"libero\" path:lerobot/common/datasets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "7e4a15a2-4f42-4799-a8c0-aadccdb5dd67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6kg8aZEahtsqAK8vVoKJT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4806,
      "cache_read_input_tokens": 26411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4806,
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

_source line 159 · 2026-05-15T11:13:12.603Z_

<details><summary>↩ Tool result · `toolu_01RHefgmEnT7wE6GzJNy6HN6`</summary>

```text
# Technical Details from Code Analysis

## Observable Processing
The code does not explicitly detail observation key specifications or dimensions. It references `cfg.shape_meta` passed to the policy class, suggesting metadata defines observation structure, but specifics are abstracted away.

## Action Space
No direct action space dimensionality is specified in this file. The policy class implementation (via `get_policy_class()`) would contain this information.

## Policy Output Format
The code emphasizes loss computation: `"loss = self.policy.compute_loss(data)"`. The policy produces loss values during training but doesn't explicitly detail action output formatting.

## Evaluation Rollout Procedure
The framework uses `"evaluate_one_task_success()"` to assess performance. Key parameters include task specification, task embeddings, and task IDs. The evaluation occurs at intervals defined by `"cfg.eval.eval_every"`.

## Success Rate Computation
Success rates are computed via the evaluation function and tracked across epochs. The framework calculates confidence intervals using `"confidence_interval(success_rate, self.cfg.eval.n_eval)"`, where n_eval specifies evaluation trials.

## Learning Dynamics
The algorithm employs an "Area under Curve" metric: `"cumulated_counter"` accumulates across evaluations, with success values frozen at peak performance to compute learning efficiency.

## Additional Details
- Model checkpoints save when success improves
- Learning continues until peak performance; no explicit early stopping beyond this heuristic
- The base `Sequential` class serves as a template for lifelong learning variants via metaclass registration
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "6e6adafb-7436-4733-8eeb-97a5314578e6"
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-15T11:13:13.019Z_

<details><summary>↩ Tool result · `toolu_01Wp4HWuywiywzByA2vgVEb2`</summary>

```text
Web search results for query: "LIBERO benchmark observation space action space 7-dimensional joint position gripper robosuite hdf5 format"

Links: [{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Benchmark Descriptions — RoboVerse 0.1.0 documentation","url":"https://roboverse.wiki/dataset_benchmark/tasks/descriptions"},{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"},{"title":"Real-World Data for LIBERO Lifelong Robot Learning | Claru","url":"https://claru.ai/benchmarks/libero"},{"title":"Robosuite Dataset: Robotic Manipulation Benchmarks","url":"https://www.emergentmind.com/topics/robosuite-dataset"},{"title":"RL with LIBERO Benchmark — RLinf documentation","url":"https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/libero.html"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview","url":"https://openreview.net/forum?id=xzEtNSuDJk"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"LIBERO – LIBERO","url":"https://libero-project.github.io/main.html"}]

Based on the search results, here's what I found about the LIBERO benchmark's observation space, action space, and data format:

## Action Space

LIBERO uses 7-DOF end-effector pose deltas (3D position delta, 3D orientation delta, gripper open/close) at 20 Hz control frequency on a simulated Franka Panda arm via robosuite's OSC controller.

## Data Format

Demonstrations are collected using a SpaceMouse teleoperator at 20 Hz with automatic filtering and validation pipelines, and are available as HDF5 for reproducibility. Additionally, LIBERO manages data loading and task execution through a combination of INIT (initialization files), BDDL (Behavior Description Definition Language), and HDF5 datasets, where HDF5 files store structured data such as object positions and robot actions for dynamic retrieval at runtime.

## Observation Space

Observations consist of RGB images (typical resolutions 128 × 128 or 224 × 224) captured by off-screen cameras placed around the workspace.

## Integration with RoboSuite

Tasks are realized atop the robosuite environment, which provides accurate physics and rich sensory input streams for robotic agents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "f285ea52-be9d-414c-8c74-fce8a977cb49"
}
```

</details>

---

### System

_source line 161_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Fetching https://huggingface.co/datasets/physical-intellig…",
  "usage": {
    "total_tokens": 31259,
    "tool_uses": 17,
    "duration_ms": 75267
  },
  "last_tool_name": "WebFetch",
  "uuid": "03bec7fb-7fad-4100-8803-f93324edb8f0",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 162_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014cy6kCYGqqeUJBrfdN3cE5`</summary>

```json
{
  "url": "https://huggingface.co/datasets/physical-intelligence/libero",
  "prompt": "Extract the full dataset card: how this dataset was created, what raw datasets it combines, size, format, features, conversion process details. Include everything about how it maps to LeRobot format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "3a93b86f-7f45-48f1-afb8-0b42e1ffb462",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6kg8aZEahtsqAK8vVoKJT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4806,
      "cache_read_input_tokens": 26411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4806,
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

_source line 163_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://rlinf.readthedocs.io/en/latest/rst_source…",
  "usage": {
    "total_tokens": 26636,
    "tool_uses": 19,
    "duration_ms": 87000
  },
  "last_tool_name": "WebFetch",
  "uuid": "dbe2a528-be1d-4c3e-b0c9-1094774f08e0",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 164_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018dNuHKHgmvWPZSPwZf2AF8`</summary>

```json
{
  "url": "https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/libero.html",
  "prompt": "Extract ALL technical details about LIBERO: observation space dimensions and keys (agentview_image, eye_in_hand_image, joint_pos, gripper_qpos, ee_pos, ee_quat), action space dimensions and meaning, HDF5 data structure, evaluation protocol, and any other specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "32be1d05-3c88-460b-b924-4f4a07a236fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Ty4UV4dpKySSoS6HxjBZB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 24359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 165 · 2026-05-15T11:13:17.872Z_

<details><summary>↩ Tool result · `toolu_01BqbiFe79oqYoM9EKEEJnm2`</summary>

````text
Web search results for query: "robosuite DomainRandomizationWrapper example code camera_names randomize_color randomize_camera"

Links: [{"title":"Demo Showcases — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/demos.html"},{"title":"robosuite/robosuite/utils/camera_utils.py at master · ARISE-Initiative/robosuite","url":"https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/utils/camera_utils.py"},{"title":"Sim-to-Real Transfer — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/algorithms/sim2real.html"},{"title":"robosuite/robosuite/demos/demo_segmentation.py at master · ARISE-Initiative/robosuite","url":"https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/demos/demo_segmentation.py"},{"title":"GitHub - quantumiracle/robolite: This is a fork of Surreal Robotics Suite that enables support to domain randomization and inverse kinematics (IK). · GitHub","url":"https://github.com/quantumiracle/robolite"},{"title":"robosuite | robosuite: A Modular Simulation Framework and Benchmark for Robot Learning","url":"https://robosuite.ai/"},{"title":"robosuite/robosuite/environments/manipulation/stack.py at master · ARISE-Initiative/robosuite","url":"https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/environments/manipulation/stack.py"},{"title":"robosuite.environments.manipulation package — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/source/robosuite.environments.manipulation.html"},{"title":"robosuite.utils package — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/source/robosuite.utils.html"},{"title":"Environments — robosuite 1.5 documentation","url":"https://robosuite.ai/docs/modules/environments.html"}]

Based on the search results, here's what I found about the DomainRandomizationWrapper in robosuite:

## DomainRandomizationWrapper Overview

The randomization functionality focuses on visual variations, including colors, textures, and camera viewpoints.

## Example Code

Here's an example of using the DomainRandomizationWrapper with parameters:

```python
default_dr_args = {
    "seed": 1,
    "randomize_camera": False,
    "randomize_every_n_steps": 10,
}
default_dr_args.update(dr_args)
env = DomainRandomizationWrapper(
    env=self.env,
    **default_dr_args,
)
```


## Related Randomization Tools

robosuite provides various Modder classes to control different aspects of the visual environment, including: CameraModder for controlling camera parameters like FOV and pose, TextureModder for controlling visual objects' appearances including texture and material properties, and LightingModder for controlling lighting parameters.

The demo_domain_randomization.py script showcases all of these modders being applied to randomize an environment during every sim step.

## Camera Names Parameter

The camera_names parameter specifies the name of camera to be rendered, and should either be a single string if the same name is to be used for all cameras' rendering or a list of cameras to render.

The search results show example usage of the wrapper with basic parameters, though specific documentation on all the detailed parameters like `randomize_color` wasn't fully detailed in these results. For complete parameter documentation, you may want to check the official robosuite GitHub repository or API documentation directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "b628a0f6-3291-4498-859c-53909ef27ee1"
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
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://medium.com/@deepkarkada/libero-simulation…",
  "usage": {
    "total_tokens": 26701,
    "tool_uses": 20,
    "duration_ms": 88488
  },
  "last_tool_name": "WebFetch",
  "uuid": "3ab8dd00-1935-4f76-a0e1-001e2502e8ae",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 167_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XaVr16NpGMVcwBUYZww3M5`</summary>

```json
{
  "url": "https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6",
  "prompt": "Extract ALL technical details about LIBERO: task suite descriptions (Spatial, Object, Goal, Long, 90), observation space, action space, data format, number of demonstrations, evaluation metrics, and any other specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "e8d99d28-f1b8-49b4-8ce3-74677adf2da9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Ty4UV4dpKySSoS6HxjBZB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 24359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 168 · 2026-05-15T11:13:18.333Z_

<details><summary>↩ Tool result · `toolu_012cLX94GQVwoky5nrzNScrZ`</summary>

```text
Web search results for query: "github huggingface lerobot "convert_libero" OR "libero" path:lerobot/common/datasets"

Links: [{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"openpi/examples/libero/convert_libero_data_to_lerobot.py at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"https://raw.githubusercontent.com/Physical-Intelli...","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"lerobot/xvla-libero · Hugging Face","url":"https://huggingface.co/lerobot/xvla-libero"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"HuggingFaceVLA/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/libero"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero/viewer/default/train"},{"title":"README.md · physical-intelligence/libero at main","url":"https://huggingface.co/datasets/physical-intelligence/libero/blob/main/README.md"}]

Based on the web search results, I found relevant information about LIBERO dataset conversion and LeRobot integration:

## Key Findings

LeRobot supports standard benchmarks like LIBERO, which is a benchmark for studying robot learning.

### LIBERO Dataset Resources

The dataset combines four individual Libero datasets: Libero-Spatial, Libero-Object, Libero-Goal and Libero-10, and all datasets were converted into LeRobot format.

### Conversion Scripts

For converting LIBERO data to LeRobot format, there's a conversion script available in the Physical Intelligence OpenPI repository. The script can be run with command `uv run examples/libero/convert_libero_data_to_lerobot.py --data_dir /path/to/your/data`, and running this conversion script will take approximately 30 minutes.

### Available Datasets

The LeRobot LIBERO repository is maintained by the Hugging Face team, with modifications for compatibility with LeRobot, simplified installation, and large-scale robotics experiments. Multiple converted LIBERO datasets are now available on the Hugging Face Hub, including libero_object_image, libero_spatial, libero_goal, and libero_10 variants.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "c7e9317b-c3e1-499e-8827-c87562cb9d7b"
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
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://raw.githubusercontent.com/Lifelong-Robot-…",
  "usage": {
    "total_tokens": 26766,
    "tool_uses": 21,
    "duration_ms": 89533
  },
  "last_tool_name": "WebFetch",
  "uuid": "27dd80bf-3f65-48a2-bbc2-3beaf4e152bc",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 170_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018Z1WPyGEzGvESgqCFzGvCU`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/lifelong/configs/config.yaml",
  "prompt": "Extract ALL configuration values: observation keys, image dimensions, action dimensions, evaluation settings (n_eval, max_steps), training parameters, and any other specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "8233405c-4a69-428c-9e48-4b4f07f86af4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Ty4UV4dpKySSoS6HxjBZB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 24359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 171 · 2026-05-15T11:13:19.437Z_

<details><summary>↩ Tool result · `toolu_011PMJHQNu2JmfTbUvAjCCtZ`</summary>

```text
Web search results for query: "LIBERO-Plus training augmentation reuse perturbation training time data augmentation robustness"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.06556v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"RL with LIBERO-Pro & LIBERO-Plus Benchmark — RLinf documentation","url":"https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/liberoplus_pro.html"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"}]

I've found comprehensive information about LIBERO-Plus and related research. Here's what the search reveals:

## LIBERO-Plus Overview

LIBERO-Plus is an extensive benchmark with 10,030 tasks spanning seven perturbation dimensions, with a diverse training dataset containing over 20,000 successful trajectories collected under systematically varied conditions.

## Training Data Augmentation and Diversity

Training strategies that emphasize diversity and exposure to varied data distributions consistently yield more robust models across multiple perturbation types. The research demonstrates that an automated generalization pipeline was used to construct an extensive training dataset comprising over 20,000 successful trajectories through substantial expansion of the original LIBERO benchmark, greatly increasing the number of trajectories and scene diversity.

## Perturbation Robustness Testing

The benchmark introduces controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise. Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

## Key Findings

Training data diversity significantly improves robustness. Additionally, models incorporating a first-person wrist camera demonstrate superior generalization compared to those reliant solely on a third-person view, and training strategies that emphasize diversity and co-training consistently yield more robust models across multiple perturbation types.

The research highlights that recent extensions reuse original training trajectories, introducing perturbations but model them independently, failing to capture complex distribution shifts, which LIBERO-Plus aims to address through its comprehensive augmentation approach.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "96a55e22-9bcd-43b3-b555-ee69a6b2323e"
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-15T11:13:19.456Z_

<details><summary>↩ Tool result · reported error · `toolu_018Z1WPyGEzGvESgqCFzGvCU`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "5edbaf00-69e1-4227-97f2-a24949091e58",
  "tool_use_result": "Error: Request failed with status code 404"
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-15T11:13:22.158Z_

<details><summary>↩ Tool result · `toolu_018dNuHKHgmvWPZSPwZf2AF8`</summary>

```text
# LIBERO Technical Specifications from Documentation

Based on the provided documentation, here are the available technical details:

## Observation Space
The documentation specifies that observations consist of **"RGB images (typical resolutions 128 × 128 or 224 × 224) captured by off-screen cameras placed around the workspace."** The data structure indicates **"Images: RGB tensors `[batch_size, 224, 224, 3]`"**

However, the specific observation keys mentioned in your query (agentview_image, eye_in_hand_image, joint_pos, gripper_qpos, ee_pos, ee_quat) are **not detailed in this document**.

## Action Space
The documentation clearly defines the action output as **"7-dimensional continuous actions"** consisting of:
- 3D end-effector position control (x, y, z)
- 3D rotation control (roll, pitch, yaw)  
- Gripper control (open/close)

Actions are described as **"Normalized continuous values converted to discrete tokens."**

## Task Format & Rewards
Task descriptions follow this structure: **"In: What action should the robot take to [task_description]? Out:"**

The reward mechanism involves **"Step-level rewards based on task completion"** with sparse rewards in practice—**"0 for all intermediate steps and 1 only at successful termination."**

## HDF5 Data Structure & Evaluation Protocol
The documentation does **not provide HDF5 structure details or comprehensive evaluation protocols** beyond noting that evaluation occurs across 500-6,500 environment instances depending on the LIBERO suite.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "0faee469-b4f4-4e90-9577-129f6373646b"
}
```

</details>

---

### System

_source line 174_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Fetching https://robosuite.ai/docs/demos.html",
  "usage": {
    "total_tokens": 30069,
    "tool_uses": 17,
    "duration_ms": 89227
  },
  "last_tool_name": "WebFetch",
  "uuid": "caea7fa2-5988-43d4-be31-c7d9aa6077b5",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 175_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RiDfFZebcFLHam2jDutLqe`</summary>

```json
{
  "url": "https://robosuite.ai/docs/demos.html",
  "prompt": "Extract the full domain randomization demo details: DomainRandomizationWrapper parameters, how to use it, what it randomizes (camera, texture, lighting, dynamics), code examples, and all configurable parameters with their defaults."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "ca9579e0-3a10-4ba7-a5be-1cfe8447ff37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014nBBJpzXWbgJoCiqjarh4c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2026,
      "cache_read_input_tokens": 27993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2026,
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

_source line 176 · 2026-05-15T11:13:23.704Z_

<details><summary>↩ Tool result · `toolu_01XaVr16NpGMVcwBUYZww3M5`</summary>

```text
# LIBERO Technical Specifications

## Task Suite Descriptions

LIBERO contains **130 language-conditioned manipulation tasks** organized into four groups:

- **LIBERO-OBJECT**: "Tasks with distribution shifts in object types"
- **LIBERO-SPATIAL**: "Tasks with distribution shifts in the spatial arrangement of objects"
- **LIBERO-GOAL**: "Tasks with distribution shifts in the task goals"
- **LIBERO-100**: "Tasks with a combination of the above three"

## Task Generation

Tasks are procedurally generated using:
- **Templated actions**: "pick, place, put on, take off etc"
- **Behavioral templates**: Extracted from the Ego4D human activity dataset, including "open, put, turn on"
- **PDDL configuration files** specifying: (1) objects and layouts, (2) initial object configurations, (3) goal states

## Observation & Action Space

The document does **not specify** observation or action space dimensions.

## Demonstrations

- **50 episodes** of high-quality human demonstrations per task used for behavior cloning training

## Evaluation Metrics

Three primary metrics are employed:

1. **FWT (Forward Transfer)**: Success rate improvement on new tasks after sequential training
2. **NBT (Negative Backward Transfer)**: Performance drop on earlier tasks after learning new ones (catastrophic forgetting measure)
3. **AUC**: Overall performance integrating both FWT and NBT

## Simulation Environment

- **MuJoCo-based** simulation framework
- Expandable benchmark supporting custom procedural generation pipelines
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "7451b650-9ab8-4173-bed0-e05637ad22d1"
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
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Fetching https://huggingface.co/docs/lerobot/main/libero_p…",
  "usage": {
    "total_tokens": 30072,
    "tool_uses": 18,
    "duration_ms": 90683
  },
  "last_tool_name": "WebFetch",
  "uuid": "5566d82a-15f5-4505-8e84-6b6ee75e9b25",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 178_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AGdrLDS92VXhX7N9wUnxbB`</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/main/libero_plus",
  "prompt": "Extract all details about LIBERO-plus integration with LeRobot: setup instructions, how to use the dataset, training commands, and any code examples for using LIBERO-plus perturbations during training."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "e6eaa64f-e15e-4c38-a451-866993ac8943",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014nBBJpzXWbgJoCiqjarh4c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2026,
      "cache_read_input_tokens": 27993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2026,
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

_source line 179 · 2026-05-15T11:13:25.100Z_

<details><summary>↩ Tool result · `toolu_01AGdrLDS92VXhX7N9wUnxbB`</summary>

````text
# LIBERO-plus

LIBERO-plus is a **robustness benchmark** for Vision-Language-Action (VLA) models built on top of [LIBERO](./libero). It systematically stress-tests policies by applying **seven independent perturbation dimensions** to the original LIBERO task set, exposing failure modes that standard benchmarks miss.

- Paper: [In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626)
- GitHub: [sylvestf/LIBERO-plus](https://github.com/sylvestf/LIBERO-plus)
- Dataset: [lerobot/libero_plus](https://huggingface.co/datasets/lerobot/libero_plus)

![An overview of the LIBERO-plus benchmark perturbation dimensions](https://github.com/sylvestf/LIBERO-plus/raw/main/static/images/libero-plus.jpg)

## Perturbation dimensions

LIBERO-plus creates ~10 000 task variants by perturbing each original LIBERO task along these axes:

| Dimension             | What changes                                          |
| --------------------- | ----------------------------------------------------- |
| Objects layout        | Target position, presence of confounding objects      |
| Camera viewpoints     | Camera position, orientation, field-of-view           |
| Robot initial states  | Manipulator start pose                                |
| Language instructions | LLM-rewritten task description (paraphrase / synonym) |
| Light conditions      | Intensity, direction, color, shadow                   |
| Background textures   | Scene surface and object appearance                   |
| Sensor noise          | Photometric distortions and image degradation         |

## Available task suites

LIBERO-plus covers the same five suites as LIBERO:

| Suite          | CLI name         | Tasks | Max steps | Description                                        |
| -------------- | ---------------- | ----- | --------- | -------------------------------------------------- |
| LIBERO-Spatial | `libero_spatial` | 10    | 280       | Tasks requiring reasoning about spatial relations  |
| LIBERO-Object  | `libero_object`  | 10    | 280       | Tasks centered on manipulating different objects   |
| LIBERO-Goal    | `libero_goal`    | 10    | 300       | Goal-conditioned tasks with changing targets       |
| LIBERO-90      | `libero_90`      | 90    | 400       | Short-horizon tasks from the LIBERO-100 collection |
| LIBERO-Long    | `libero_10`      | 10    | 520       | Long-horizon tasks from the LIBERO-100 collection  |

  Installing LIBERO-plus **replaces** vanilla LIBERO — it uninstalls `hf-libero`
  so that `import libero` resolves to the LIBERO-plus fork. You cannot have both
  installed at the same time. To switch back to vanilla LIBERO, uninstall the
  fork and reinstall with `pip install -e ".[libero]"`.

## Installation

### System dependencies (Linux only)

```bash
sudo apt install libexpat1 libfontconfig1-dev libmagickwand-dev
```

### Python package

```bash
pip install -e ".[libero]" "robosuite==1.4.1" bddl easydict mujoco wand scikit-image gym
git clone https://github.com/sylvestf/LIBERO-plus.git
cd LIBERO-plus && pip install --no-deps -e .
pip uninstall -y hf-libero  # so `import libero` resolves to the fork
```

LIBERO-plus is installed from its GitHub fork rather than a pyproject extra — the fork ships as a namespace package that pip can't handle, so it must be cloned and added to `PYTHONPATH`. See `docker/Dockerfile.benchmark.libero_plus` for the canonical install. MuJoCo is required, so only Linux is supported.

Set the MuJoCo rendering backend before running evaluation:

```bash
export MUJOCO_GL=egl   # headless / HPC / cloud
```

### Download LIBERO-plus assets

LIBERO-plus ships its extended asset pack separately. Download `assets.zip` from the [Hugging Face dataset](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main) and extract it into the LIBERO-plus package directory:

```bash
# After installing the package, find where it was installed:
python -c "import libero; print(libero.__file__)"
# Then extract assets.zip into &lt;package_root>/libero/assets/
```

## Evaluation

### Default evaluation (recommended)

Evaluate across the four standard suites (10 episodes per task):

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero_plus \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```

### Single-suite evaluation

Evaluate on one LIBERO-plus suite:

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero_plus \
  --env.task=libero_spatial \
  --eval.batch_size=1 \
  --eval.n_episodes=10
```

- `--env.task` picks the suite (`libero_spatial`, `libero_object`, etc.).
- `--env.task_ids` restricts to specific task indices (`[0]`, `[1,2,3]`, etc.). Omit to run all tasks in the suite.
- `--eval.batch_size` controls how many environments run in parallel.
- `--eval.n_episodes` sets how many episodes to run per task.

### Multi-suite evaluation

Benchmark a policy across multiple suites at once by passing a comma-separated list:

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero_plus \
  --env.task=libero_spatial,libero_object \
  --eval.batch_size=1 \
  --eval.n_episodes=10
```

### Control mode

LIBERO-plus supports two control modes — `relative` (default) and `absolute`. Different VLA checkpoints are trained with different action parameterizations, so make sure the mode matches your policy:

```bash
--env.control_mode=relative   # or "absolute"
```

### Policy inputs and outputs

**Observations:**

- `observation.state` — 8-dim proprioceptive features (eef position, axis-angle orientation, gripper qpos)
- `observation.images.image` — main camera view (`agentview_image`), HWC uint8
- `observation.images.image2` — wrist camera view (`robot0_eye_in_hand_image`), HWC uint8

**Actions:**

- Continuous control in `Box(-1, 1, shape=(7,))` — 6D end-effector delta + 1D gripper

### Recommended evaluation episodes

For reproducible benchmarking, use **10 episodes per task** across all four standard suites (Spatial, Object, Goal, Long). This gives 400 total episodes and matches the protocol used for published results.

## Training

### Dataset

A LeRobot-format training dataset for LIBERO-plus is available at:

- [lerobot/libero_plus](https://huggingface.co/datasets/lerobot/libero_plus)

### Example training command

```bash
lerobot-train \
    --policy.type=smolvla \
    --policy.repo_id=${HF_USER}/smolvla_libero_plus \
    --policy.load_vlm_weights=true \
    --dataset.repo_id=lerobot/libero_plus \
    --env.type=libero_plus \
    --env.task=libero_spatial \
    --output_dir=./outputs/ \
    --steps=100000 \
    --batch_size=4 \
    --eval.batch_size=1 \
    --eval.n_episodes=1 \
    --eval_freq=1000
```

## Relationship to LIBERO

LIBERO-plus is a drop-in extension of LIBERO:

- Same Python gym interface (`LiberoEnv`, `LiberoProcessorStep`)
- Same camera names and observation/action format
- Same task suite names
- Installs under the same `libero` Python package name (different GitHub repo)

To use the original LIBERO benchmark, see [LIBERO](./libero) and use `--env.type=libero`.


````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "de5cbc3b-e96b-4a27-b11e-1c90c1e10d39"
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
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://raw.githubusercontent.com/Lifelong-Robot-…",
  "usage": {
    "total_tokens": 28082,
    "tool_uses": 22,
    "duration_ms": 97261
  },
  "last_tool_name": "WebFetch",
  "uuid": "88e0c7b6-78bf-42c6-904a-c6814ca52a1e",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 181_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WS1LQM62x3oyRJFpdpnbWL`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/configs/config.yaml",
  "prompt": "Extract ALL configuration values: observation keys, image dimensions, action dimensions, evaluation settings, training parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "6a1c3ea1-4d36-49c9-a30c-48c4af33a08a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5o5hf9K9szbcCGYEfT3o2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 39,
      "cache_creation_input_tokens": 1206,
      "cache_read_input_tokens": 26273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1206,
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

### System

_source line 182_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://raw.githubusercontent.com/Lifelong-Robot-…",
  "usage": {
    "total_tokens": 28154,
    "tool_uses": 23,
    "duration_ms": 98030
  },
  "last_tool_name": "WebFetch",
  "uuid": "0f5de650-41b3-4ebc-bda8-e0ea549ca35a",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 183_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MiRC1UAs57krSKsxj2LNAr`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/lifelong/utils.py",
  "prompt": "Extract details about observation space processing, action space, evaluation rollout (evaluate_one_task_success function), success rate computation, number of evaluation episodes, max steps, and any other technical details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "a1c8717f-5d83-4461-a965-1f9f1fae9c1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5o5hf9K9szbcCGYEfT3o2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 39,
      "cache_creation_input_tokens": 1206,
      "cache_read_input_tokens": 26273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1206,
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

_source line 184 · 2026-05-15T11:13:27.871Z_

<details><summary>↩ Tool result · `toolu_014cy6kCYGqqeUJBrfdN3cE5`</summary>

````text
# LIBERO Dataset Card

## Overview
The LIBERO dataset is a robotic manipulation dataset published by Physical Intelligence and hosted on Hugging Face. It contains demonstration data for learning robot control policies.

## Dataset Statistics
- **Size**: 273,000 rows
- **Format**: Parquet (auto-converted from original format)
- **Task Categories**: Robotics
- **Modalities**: Image, Time-series
- **License**: CC-BY-4.0
- **ArXiv Reference**: 2306.03310

## Data Structure

### Raw Format
The dataset is organized hierarchically:
- **Subsets**: 1 (default)
- **Splits**: 1 (train)
- **Episodes**: 147 episodes
- **Total Frames**: ~273k frames

### Features

The dataset contains the following fields per frame:

| Field | Type | Description |
|-------|------|-------------|
| `image` | Image (256×256px) | RGB observation from main camera |
| `wrist_image` | Image (256×256px) | RGB observation from wrist-mounted camera |
| `state` | List (8 floats) | Robot joint positions/states |
| `actions` | List (7 floats) | Robot action command (likely 6-DOF + gripper) |
| `timestamp` | float32 | Frame timestamp |
| `frame_index` | int64 | Frame number within episode (0-454) |
| `episode_index` | int64 | Episode identifier (0-146) |
| `index` | int64 | Global row index (0-40.1k) |
| `task_index` | int64 | Task identifier (0-9, suggesting 10 tasks) |

### Data Example

```python
# Frame sample structure
{
  "image": <256×256 RGB image>,
  "wrist_image": <256×256 RGB wrist view>,
  "state": [-0.0534, 0.0070, 0.6783, 3.1408, 0.0018, -0.0899, 0.0388, -0.0388],
  "actions": [0.0161, 0, 0, 0, 0, 0, -1],
  "timestamp": 45.4,
  "frame_index": 0,
  "episode_index": 0,
  "task_index": 0
}
```

## Robot Hardware
- **Robot**: Franka Panda (indicated by "panda" tag)
- **State Dimension**: 8 (7 joint angles + gripper state)
- **Action Dimension**: 7 (6-DOF end-effector control + gripper command)

## LeRobot Integration

### Format Compatibility
The dataset includes tags for **LeRobot** integration:
- Supported by LeRobot framework
- Stored in RLDS format (standardized robot learning dataset format)
- Auto-converted to Parquet for accessibility

### Suggested LeRobot Mapping

```python
# Typical LeRobot episode structure
{
  "observations": {
    "image": [...],           # Main camera RGB
    "wrist_image": [...]      # Wrist camera RGB
  },
  "states": [...],            # Robot joint states
  "actions": [...],           # Control commands
  "episode_index": 0,
  "frame_index": [...],
  "timestamp": [...]
}
```

## Tasks
The dataset covers **10 different manipulation tasks** (task_index: 0-9), likely including:
- Grasping and placing objects
- Opening/closing drawers or containers
- Pushing or sliding objects
- Contact-rich manipulation tasks

## Access Methods

### HuggingFace Datasets Library
```python
from datasets import load_dataset

# Load the full dataset
libero = load_dataset("physical-intelligence/libero")

# Access training split
train_data = libero["train"]

# Iterate through episodes
for sample in train_data:
    episode_id = sample["episode_index"]
    image = sample["image"]
    action = sample["actions"]
    state = sample["state"]
```

### Direct Access
- **Dataset Viewer**: [HuggingFace Data Studio](https://huggingface.co/datasets/physical-intelligence/libero/viewer/)
- **Files**: Available via Git XET for efficient version control
- **Community**: 4 discussions available

## Related Tags
- `libero` - Dataset identifier
- `panda` - Franka Panda robot
- `rlds` - Robot Learning Dataset Standard format
- `LeRobot` - Integration framework

## Conversion Details
- Original format: RLDS (Robot Learning Dataset Standard)
- Converted to: Parquet (for accessibility and querying)
- Conversion maintains full compatibility with LeRobot framework
- Query support: SQL-based queries available via HuggingFace platform

## Use Cases
- Training imitation learning policies
- Behavior cloning models
- Multi-task robot learning
- Vision-based manipulation research
- Learning from demonstrations (LfD)
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "fe30dccd-7b29-4dc7-8bad-0718b2fb0c39"
}
```

</details>

---

### Tool result

_source line 185 · 2026-05-15T11:13:28.000Z_

<details><summary>↩ Tool result · `toolu_01RiDfFZebcFLHam2jDutLqe`</summary>

```text
# Domain Randomization Demo Details

Based on the provided documentation, the information available about the Domain Randomization demo is limited:

## What the Documentation States

The `demo_domain_randomization.py` script is described as showcasing "domain randomization functionality." According to the content, this feature "can be easily enabled by wrapping an environment with the DomainRandomizationWrapper."

The documentation specifies that **"the randomization functionality focuses on visual variations, including colors, textures, and camera viewpoints."**

## Limitations of Available Information

Unfortunately, the provided webpage content does not include:
- Specific parameters for the DomainRandomizationWrapper
- Code examples showing implementation
- Default values for any configurable settings
- Details on dynamics randomization (though it mentions visual variations only)
- Detailed usage instructions beyond wrapping an environment

## Recommendation

To obtain comprehensive details about DomainRandomizationWrapper parameters, code examples, and all configurable options, you would need to:
1. Consult the full robosuite source code repository
2. Review the `robosuite.wrappers` module documentation
3. Examine the actual `demo_domain_randomization.py` script in the [robosuite GitHub repository](https://github.com/ARISE-Initiative/robosuite)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "de363c52-98c1-424c-a0db-5b802d2dc8b3"
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
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Searching for LIBERO robot benchmark \"agentview\" \"eye_in_hand\" …",
  "usage": {
    "total_tokens": 28226,
    "tool_uses": 24,
    "duration_ms": 99116
  },
  "last_tool_name": "WebSearch",
  "uuid": "824b72b0-fdbd-46c6-b1c5-de9454fff7b4",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 187_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TdQtgZnF7R1G44jiaNxfuU`</summary>

```json
{
  "query": "LIBERO robot benchmark \"agentview\" \"eye_in_hand\" observation keys joint_pos action 7 dimensions hdf5 demo structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "d0df2234-3926-49e6-b7a0-6d07ae2bf199",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5o5hf9K9szbcCGYEfT3o2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 39,
      "cache_creation_input_tokens": 1206,
      "cache_read_input_tokens": 26273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1206,
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

_source line 188 · 2026-05-15T11:13:30.196Z_

<details><summary>↩ Tool result · `toolu_01WS1LQM62x3oyRJFpdpnbWL`</summary>

```text
# Configuration Extraction

Based on the provided YAML configuration file, here are the extracted values:

## Core Settings
- **Seed**: 10000
- **Device**: "cuda"
- **Benchmark**: "LIBERO_SPATIAL"
- **Task Embedding Format**: "bert"
- **Task Embedding Offset**: 1

## Flags & Paths
- **Weights & Biases Logging**: Disabled (use_wandb: false)
- **Pretraining**: Disabled (pretrain: false)
- **Load Previous Model**: false
- **Data Folder**: Uses default path (folder: null)
- **BDDL Folder**: Uses default path (bddl_folder: null)
- **Initial States Folder**: Uses default path (init_states_folder: null)

## Configuration References
The file references external configuration modules through defaults:
- Data configuration (data: default)
- Policy: BC Transformer
- Training configuration (train: default)
- Evaluation configuration (eval: default)
- Lifelong learning: base variant
- Test configuration: null (not specified)

## Notable Gaps
The provided excerpt does not contain **observation keys, image dimensions, or action dimensions**—these are likely defined in the referenced configuration modules (data/default, policy/bc_transformer_policy, train/default, eval/default).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "947282ce-84e5-4f96-bf07-b46996e242c6"
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
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "description": "Research LeRobot LIBERO integration",
  "usage": {
    "total_tokens": 33609,
    "tool_uses": 18,
    "duration_ms": 92543
  },
  "last_tool_name": "ToolSearch",
  "uuid": "2919c6c0-a2bd-4e09-927a-1b0ea9d5f2f0",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 190_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AgPifgvWFLAWJvyGCXz3Jx`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__append_idea",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "9fe8a956-bacf-49c4-851b-aef2f7ac19d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01679sPaXRnePAq8gb7CDKX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2348,
      "cache_read_input_tokens": 31217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2348,
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

_source line 191 · 2026-05-15T11:13:31.307Z_

<details><summary>↩ Tool result · `toolu_01AgPifgvWFLAWJvyGCXz3Jx`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "197f873b-1415-4b1b-9a99-7f8936036067"
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
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Fetching https://github.com/ARISE-Initiative/robosuite/blo…",
  "usage": {
    "total_tokens": 32866,
    "tool_uses": 19,
    "duration_ms": 97316
  },
  "last_tool_name": "WebFetch",
  "uuid": "10eff4b8-40ba-44d9-bb67-1f5c31e6cc40",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 193_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01H5fcnANzeubgqZen5nvqc7`</summary>

```json
{
  "url": "https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/wrappers/domain_randomization_wrapper.py",
  "prompt": "Extract the complete DomainRandomizationWrapper class definition including all constructor parameters, their defaults, and descriptions. Include the full docstring and all randomization-related parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "9ff26e6d-744d-410a-9146-f84207ace560",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CP6stPQt8vGELWxtjKhmDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2197,
      "cache_creation_input_tokens": 596,
      "cache_read_input_tokens": 30019,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 596,
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

_source line 194 · 2026-05-15T11:13:32.130Z_

<details><summary>↩ Tool result · `toolu_01MiRC1UAs57krSKsxj2LNAr`</summary>

```text
# Technical Details Extraction

Based on the provided code, here are the key technical details:

## Observation & Action Space
No explicit observation or action space definitions are present in this code snippet. The code focuses on utility functions rather than environment specifications.

## Evaluation Details
The code does not contain an `evaluate_one_task_success` function. There are no parameters for:
- Success rate computation methods
- Number of evaluation episodes
- Maximum evaluation steps

## Available Functions

**Data Loading**: The `get_train_test_loader` function splits datasets using a "train_ratio parameter, creating separate DataLoaders for training and testing phases with configurable batch sizes.

**Model Checkpointing**: The `torch_save_model` function preserves "state_dict, cfg, and previous_masks" in a checkpoint file, while `torch_load_model` retrieves these components.

**Computational Analysis**: A `compute_flops` function calculates model efficiency by measuring "macs, params" using the THOP profiler library.

**Task Embedding**: The `get_task_embs` function generates task representations from text descriptions using multiple transformer architectures (BERT, GPT-2, CLIP, RoBERTa).

## Missing Information
This utility module lacks evaluation-specific implementations. Additional files would be needed to identify rollout procedures, success metrics, and episode configurations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "a07e4f3e-0bbf-489c-bfc1-d47829b1f48f"
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-15T11:13:35.183Z_

<details><summary>↩ Tool result · `toolu_01TdQtgZnF7R1G44jiaNxfuU`</summary>

```text
Web search results for query: "LIBERO robot benchmark "agentview" "eye_in_hand" observation keys joint_pos action 7 dimensions hdf5 demo structure"

Links: [{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"Libero - LeRobot","url":"https://www.mintlify.com/huggingface/lerobot/simulation/libero"},{"title":"openvla/experiments/robot/libero/regenerate_libero_dataset.py at main · openvla/openvla","url":"https://github.com/openvla/openvla/blob/main/experiments/robot/libero/regenerate_libero_dataset.py"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"libero-mem/LIBERO-Mem · Datasets at Hugging Face","url":"https://huggingface.co/datasets/libero-mem/LIBERO-Mem"},{"title":"robosuite Datasets — robomimic 0.5 documentation","url":"https://robomimic.github.io/docs/datasets/robosuite.html"},{"title":"nvidia/LIBERO-Cosmos-Policy · Datasets at Hugging Face","url":"https://huggingface.co/datasets/nvidia/LIBERO-Cosmos-Policy"},{"title":"Real-World Data for LIBERO Lifelong Robot Learning | Claru","url":"https://claru.ai/benchmarks/libero"},{"title":"Dataset Contents and Visualization — robomimic 0.5 documentation","url":"https://robomimic.github.io/docs/tutorials/dataset_contents.html"},{"title":"Robot LIBERO 数据集 | LIAO JIAYI Blog","url":"https://www.liaojiayi.com/blog/robot-libero"}]

I found relevant information about the LIBERO robot benchmark with details about the HDF5 data structure and observation keys.

## LIBERO Benchmark Data Structure

Based on the search results, here's what I found about the LIBERO benchmark:

### HDF5 Demo Structure

LIBERO HDF5 files contain data organized as: actions (T, 7), dones (T,), and obs/ containing agentview_rgb, agentview_depth, agentview_seg, eye_in_hand_rgb, eye_in_hand_depth, eye_in_hand_seg, gripper_states, and joint_states.

### Camera Observations

The benchmark supports agentview_image and robot0_eye_in_hand_image camera observations, and RGB images come from an agentview camera (128x128) and eye-in-hand wrist camera (128x128).

### Proprioceptive State

Proprioceptive state includes 7 joint positions, 7 joint velocities, and gripper aperture.

### Action Dimensions

Actions consist of 7-DOF end-effector pose deltas (3D position delta, 3D orientation delta, gripper open/close) at 20 Hz control frequency.

### Data Format

Demonstrations are collected using a SpaceMouse teleoperator at 20 Hz with automatic filtering and validation pipelines; available as HDF5 for reproducibility.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "849b1628-c8c9-4fd7-a4cf-7d959061f00c"
}
```

</details>

---

### Tool result

_source line 196 · 2026-05-15T11:13:38.303Z_

<details><summary>↩ Tool result · `toolu_01H5fcnANzeubgqZen5nvqc7`</summary>

```text
# DomainRandomizationWrapper Class Definition

## Class Overview
The `DomainRandomizationWrapper` is designed to "allow for domain randomization mid-simulation" in robosuite environments.

## Constructor Parameters

**Core Parameters:**
- `env` (MujocoEnv): The environment being wrapped
- `seed` (int, optional): Used to create isolated `np.random.RandomState` instance

**Randomization Toggles:**
- `randomize_color` (bool, default=True): Controls geom and texture color randomization
- `randomize_camera` (bool, default=True): Controls camera location and parameter changes
- `randomize_lighting` (bool, default=True): Controls light location and property modifications
- `randomize_dynamics` (bool, default=True): Controls physics parameter randomization

**Configuration Dictionaries:**
- `color_randomization_args`: Includes geom names, local color sampling, material properties, texture variations, and skybox settings
- `camera_randomization_args`: Includes camera names, position/rotation/fovy randomization with perturbation sizes
- `lighting_randomization_args`: Includes light names and randomization flags for position, direction, specular, ambient, and diffuse properties
- `dynamics_randomization_args`: Includes body, geom, and joint parameters with density, viscosity, friction, and inertia controls

**Execution Parameters:**
- `randomize_on_reset` (bool, default=True): Applies randomization at episode reset
- `randomize_every_n_steps` (int, default=1): Sets randomization frequency during steps

## Key Methods
- `reset()`: Restores defaults, resets environment, saves parameters, applies randomization if enabled
- `step()`: Calls step randomization before delegating to superclass
- `randomize_domain()`: Executes randomization across all active modders
- `save_default_domain()`: Preserves current simulation parameters
- `restore_default_domain()`: Reverts to saved parameters
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "6094e08e-0a36-4a5e-a28e-7db37e7c55ad"
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
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://huggingface.co/docs/lerobot/libero",
  "usage": {
    "total_tokens": 30119,
    "tool_uses": 25,
    "duration_ms": 109918
  },
  "last_tool_name": "WebFetch",
  "uuid": "97f460d0-ab6a-4302-af59-87ebd0c68458",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 198_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017KNMbSLkMSQrkwjHSBSUJF`</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/libero",
  "prompt": "Extract ALL technical details about LIBERO: task suites (Spatial, Object, Goal, Long, 90), observation keys and dimensions, action dimensions, HDF5 structure, data download, evaluation protocol, number of demos per task, and any exact specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "f74be5b5-1035-4981-8939-ebff003376ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NNrw687NQUxGsyReivNNjc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1866,
      "cache_read_input_tokens": 27479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1866,
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

_source line 199 · 2026-05-15T11:13:40.107Z_

<details><summary>↩ Tool result · `toolu_017KNMbSLkMSQrkwjHSBSUJF`</summary>

````text
# LIBERO

LIBERO is a benchmark designed to study **lifelong robot learning** — the idea that robots need to keep learning and adapting with their users over time, not just be pretrained once. It provides a set of standardized manipulation tasks that focus on **knowledge transfer**: how well a robot can apply what it has already learned to new situations. By evaluating on LIBERO, different algorithms can be compared fairly and researchers can build on each other's work.

- Paper: [Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)
- GitHub: [Lifelong-Robot-Learning/LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO)
- Project website: [libero-project.github.io](https://libero-project.github.io)

![An overview of the LIBERO benchmark](https://libero-project.github.io/assets/img/libero/fig1.png)

## Available tasks

LIBERO includes **five task suites** covering **130 tasks**, ranging from simple object manipulations to complex multi-step scenarios:

| Suite          | CLI name         | Tasks | Description                                        |
| -------------- | ---------------- | ----- | -------------------------------------------------- |
| LIBERO-Spatial | `libero_spatial` | 10    | Tasks requiring reasoning about spatial relations  |
| LIBERO-Object  | `libero_object`  | 10    | Tasks centered on manipulating different objects   |
| LIBERO-Goal    | `libero_goal`    | 10    | Goal-conditioned tasks with changing targets       |
| LIBERO-90      | `libero_90`      | 90    | Short-horizon tasks from the LIBERO-100 collection |
| LIBERO-Long    | `libero_10`      | 10    | Long-horizon tasks from the LIBERO-100 collection  |

## Installation

After following the LeRobot installation instructions:

```bash
pip install -e ".[libero]"
```

LIBERO requires Linux (`sys_platform == 'linux'`). LeRobot uses MuJoCo for simulation — set the rendering backend before training or evaluation:

```bash
export MUJOCO_GL=egl  # for headless servers (HPC, cloud)
```

## Evaluation

### Default evaluation (recommended)

Evaluate across the four standard suites (10 episodes per task):

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```

### Single-suite evaluation

Evaluate on one LIBERO suite:

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_object \
  --eval.batch_size=2 \
  --eval.n_episodes=3
```

- `--env.task` picks the suite (`libero_object`, `libero_spatial`, etc.).
- `--env.task_ids` restricts to specific task indices (`[0]`, `[1,2,3]`, etc.). Omit to run all tasks in the suite.
- `--eval.batch_size` controls how many environments run in parallel.
- `--eval.n_episodes` sets how many episodes to run per task.

### Multi-suite evaluation

Benchmark a policy across multiple suites at once by passing a comma-separated list:

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_object,libero_spatial \
  --eval.batch_size=1 \
  --eval.n_episodes=2
```

### Control mode

LIBERO supports two control modes — `relative` (default) and `absolute`. Different VLA checkpoints are trained with different action parameterizations, so make sure the mode matches your policy:

```bash
--env.control_mode=relative   # or "absolute"
```

### Policy inputs and outputs

**Observations:**

- `observation.state` — 8-dim proprioceptive features (eef position, axis-angle orientation, gripper qpos)
- `observation.images.image` — main camera view (`agentview_image`), HWC uint8
- `observation.images.image2` — wrist camera view (`robot0_eye_in_hand_image`), HWC uint8

  LeRobot enforces the `.images.*` prefix for visual features. Ensure your
  policy config `input_features` use the same naming keys, and that your dataset
  metadata keys follow this convention. If your data contains different keys,
  you must rename the observations to match what the policy expects, since
  naming keys are encoded inside the normalization statistics layer.

**Actions:**

- Continuous control in `Box(-1, 1, shape=(7,))` — 6D end-effector delta + 1D gripper

### Recommended evaluation episodes

For reproducible benchmarking, use **10 episodes per task** across all four standard suites (Spatial, Object, Goal, Long). This gives 400 total episodes and matches the protocol used for published results.

## Training

### Dataset

We provide a preprocessed LIBERO dataset fully compatible with LeRobot:

- [HuggingFaceVLA/libero](https://huggingface.co/datasets/HuggingFaceVLA/libero)

For reference, the original dataset published by Physical Intelligence:

- [physical-intelligence/libero](https://huggingface.co/datasets/physical-intelligence/libero)

### Example training command

```bash
lerobot-train \
  --policy.type=smolvla \
  --policy.repo_id=${HF_USER}/libero-test \
  --policy.load_vlm_weights=true \
  --dataset.repo_id=HuggingFaceVLA/libero \
  --env.type=libero \
  --env.task=libero_10 \
  --output_dir=./outputs/ \
  --steps=100000 \
  --batch_size=4 \
  --eval.batch_size=1 \
  --eval.n_episodes=1 \
  --eval_freq=1000
```

## Reproducing published results

We reproduce the results of Pi0.5 on the LIBERO benchmark. We take the Physical Intelligence LIBERO base model (`pi05_libero`) and finetune for an additional 6k steps in bfloat16, with batch size of 256 on 8 H100 GPUs using the [HuggingFace LIBERO dataset](https://huggingface.co/datasets/HuggingFaceVLA/libero).

The finetuned model: [lerobot/pi05_libero_finetuned](https://huggingface.co/lerobot/pi05_libero_finetuned)

### Evaluation command

```bash
lerobot-eval \
  --output_dir=./eval_logs/ \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --policy.path=pi05_libero_finetuned \
  --policy.n_action_steps=10 \
  --env.max_parallel_tasks=1
```

We set `n_action_steps=10`, matching the original OpenPI implementation.

### Results

| Model               | LIBERO Spatial | LIBERO Object | LIBERO Goal | LIBERO 10 | Average  |
| ------------------- | -------------- | ------------- | ----------- | --------- | -------- |
| **Pi0.5 (LeRobot)** | 97.0           | 99.0          | 98.0        | 96.0      | **97.5** |

These results are consistent with the [original results](https://github.com/Physical-Intelligence/openpi/tree/main/examples/libero#results) reported by Physical Intelligence:

| Model              | LIBERO Spatial | LIBERO Object | LIBERO Goal | LIBERO 10 | Average   |
| ------------------ | -------------- | ------------- | ----------- | --------- | --------- |
| **Pi0.5 (OpenPI)** | 98.8           | 98.2          | 98.0        | 92.4      | **96.85** |


````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "17945526-b737-4e25-8567-9bca390ad01c"
}
```

</details>

---

### System

_source line 200_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://github.com/openvla/openvla/blob/main/expe…",
  "usage": {
    "total_tokens": 30184,
    "tool_uses": 26,
    "duration_ms": 111402
  },
  "last_tool_name": "WebFetch",
  "uuid": "5b9d8ee9-fa82-48c3-9b9b-2ac96ab2fe24",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 201_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015yE62iZaBZNb6QGo14zXXU`</summary>

```json
{
  "url": "https://github.com/openvla/openvla/blob/main/experiments/robot/libero/regenerate_libero_dataset.py",
  "prompt": "Extract ALL details about LIBERO data format: observation keys (agentview_image, eye_in_hand_image, robot0_joint_pos, robot0_gripper_qpos, ee_pos, ee_quat), action dimensions, HDF5 structure, image dimensions, and how data is loaded from LIBERO demos."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "55585c38-47c6-4e0e-ba7c-90ad78e85b38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NNrw687NQUxGsyReivNNjc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1866,
      "cache_read_input_tokens": 27479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1866,
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

### System

_source line 202_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "description": "Research LIBERO-Plus perturbation",
  "usage": {
    "total_tokens": 33500,
    "tool_uses": 20,
    "duration_ms": 107219
  },
  "last_tool_name": "ToolSearch",
  "uuid": "16d00e19-0346-4220-ba2d-f5d34063a4bd",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 203_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0173q63qhK6XB8QeKNj4hQFQ`</summary>

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
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "289de43c-d20a-474d-bf1f-78bb0b40d5c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQBadPYzkj6nJYWNELNhC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2828,
      "cache_read_input_tokens": 30615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2828,
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

_source line 204 · 2026-05-15T11:13:41.634Z_

<details><summary>↩ Tool result · `toolu_0173q63qhK6XB8QeKNj4hQFQ`</summary>

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
  "parent_tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "ab4add5b-f3a1-450c-ad6e-b1158428733b"
}
```

</details>

---

### System

_source line 205_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://robomimic.github.io/docs/tutorials/datase…",
  "usage": {
    "total_tokens": 30249,
    "tool_uses": 27,
    "duration_ms": 112815
  },
  "last_tool_name": "WebFetch",
  "uuid": "49959d8f-1f68-407f-9197-5ac9b16b0ae4",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 206_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xfo5xungq4i1MWfhdCSSKp`</summary>

```json
{
  "url": "https://robomimic.github.io/docs/tutorials/dataset_contents.html",
  "prompt": "Extract ALL details about robosuite/robomimic HDF5 dataset format: obs keys, action dimensions, data structure, demonstration format. Focus on information relevant to LIBERO which uses this format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "7e9d5ffb-eab4-4015-97f2-8c6591de5be2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NNrw687NQUxGsyReivNNjc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1866,
      "cache_read_input_tokens": 27479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1866,
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

_source line 207 · 2026-05-15T11:13:47.261Z_

<details><summary>↩ Tool result · `toolu_015yE62iZaBZNb6QGo14zXXU`</summary>

````text
# LIBERO Data Format Details

## Observation Keys
The script records multiple observation modalities from the environment:
- **Image observations**: `agentview_rgb` and `eye_in_hand_rgb` (both at 256x256 resolution)
- **Gripper state**: `gripper_states` from `robot0_gripper_qpos`
- **Joint configuration**: `joint_states` from `robot0_joint_pos`
- **End-effector pose**: `ee_states` combining position and axis-angle orientation, stored separately as `ee_pos` (3D) and `ee_ori` (3D axis-angle)
- **Robot state**: Full concatenation of gripper position, end-effector position, and quaternion

## Action Dimensions
Actions are 7-dimensional vectors where the final dimension represents gripper control. The script filters "no-op actions" when all movement dimensions are near zero (threshold <1e-4) and gripper action matches the previous timestep's gripper command.

## HDF5 Structure
Data is organized hierarchically:
```
data/
  demo_0/
    obs/
      gripper_states, joint_states, ee_states, ee_pos, ee_ori
      agentview_rgb, eye_in_hand_rgb
    actions, states, robot_states, rewards, dones
```

Each episode stores timestep sequences where "dones" and "rewards" are one-hot vectors marking successful task completion at the final transition.

## Data Loading Process
The script replays original demonstrations by: setting initial environment state from stored states, executing recorded actions sequentially, and capturing observations at each step—filtering unsuccessful episodes and no-op transitions in the process.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "28a3ec76-e43a-40c6-915c-7ea22d3d0690"
}
```

</details>

---

### Tool result

_source line 208 · 2026-05-15T11:13:47.833Z_

<details><summary>↩ Tool result · `toolu_01Xfo5xungq4i1MWfhdCSSKp`</summary>

```text
# robomimic HDF5 Dataset Format Overview

Based on the documentation provided, here's what's available about the robomimic HDF5 dataset structure:

## Key References

The page indicates that **"HDF5 Dataset Structure"** details are documented elsewhere in their [dataset overview section](../datasets/overview.html#dataset-structure), which would contain the authoritative specification.

## Available Information

The documentation mentions several components stored in datasets:

1. **Trajectory Statistics**: The `get_dataset_info.py` utility reveals "statistics about the trajectories (number, average length, etc.)"

2. **Metadata Elements**:
   - Filter keys (for data organization)
   - "Environment metadata in the dataset, which is used to construct the same simulator environment that the data was collected on"

3. **Data Types**: The tutorial demonstrates handling:
   - Image observations (agentview, robot0_eye_in_hand cameras)
   - Depth observations
   - Action recordings
   - Demonstration frames

## Practical Access

For detailed specifications on observation keys, action dimensions, and complete data structure, the documentation directs users to:
- The `get_dataset_info.py` script for structure inspection
- A Jupyter notebook at `examples/notebooks/datasets.ipynb` containing "useful python code snippets for working with robomimic hdf5 datasets"

**Note**: This webpage excerpt doesn't contain the actual field names or dimensional specifications—those appear to be documented in linked sections not included here.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "cc40725b-17ba-4b29-ad4a-ca55fd122c59"
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
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://raw.githubusercontent.com/Lifelong-Robot-…",
  "usage": {
    "total_tokens": 33612,
    "tool_uses": 28,
    "duration_ms": 122674
  },
  "last_tool_name": "WebFetch",
  "uuid": "a423bdc2-23cd-4c2f-b8c2-7b00ee31379f",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 210_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PLn3j11F8HZ17GHKMR6Kq2`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/configs/data/default.yaml",
  "prompt": "Extract ALL observation configuration: obs keys, image sizes, modalities, action dimensions, sequence length, and any other data specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "ceb88cf8-0314-4b4d-9143-5ab56ece15c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hw3LBedb6XqPShvrBosPZj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3361,
      "cache_read_input_tokens": 29345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3361,
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
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://raw.githubusercontent.com/Lifelong-Robot-…",
  "usage": {
    "total_tokens": 33613,
    "tool_uses": 29,
    "duration_ms": 123994
  },
  "last_tool_name": "WebFetch",
  "uuid": "21c21abe-df3a-426b-886e-901b633e8066",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 212_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016iySNFkgaiG38YX1yt8Na5`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/configs/eval/default.yaml",
  "prompt": "Extract ALL evaluation configuration: number of evaluation episodes, max steps, success metrics, and any other evaluation parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "2d965041-97ba-4977-8834-0c9b3a36fbfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hw3LBedb6XqPShvrBosPZj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3361,
      "cache_read_input_tokens": 29345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3361,
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
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Searching for LIBERO benchmark dataset size GB each suite liber…",
  "usage": {
    "total_tokens": 33614,
    "tool_uses": 30,
    "duration_ms": 124418
  },
  "last_tool_name": "WebSearch",
  "uuid": "2a117aa9-abce-4e2a-b52b-991db98e0b22",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 214_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XzxZ2apnwbURLoJNku4jZu`</summary>

```json
{
  "query": "LIBERO benchmark dataset size GB each suite libero_spatial libero_object libero_goal libero_90 libero_long download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "688ddc3f-7fc7-4304-9731-52af9e3fd7ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hw3LBedb6XqPShvrBosPZj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3361,
      "cache_read_input_tokens": 29345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3361,
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

_source line 215 · 2026-05-15T11:13:55.471Z_

<details><summary>↩ Tool result · `toolu_01PLn3j11F8HZ17GHKMR6Kq2`</summary>

```text
# Observation Configuration Extraction

**Observation Keys:**
- RGB images: "agentview_rgb", "eye_in_hand_rgb"
- Low-dimensional: "gripper_states", "joint_states"

**Image Specifications:**
- Resolution: 128×128 pixels
- Frame stacking: 1
- Number of keypoints: 64

**Data Modalities:**
The configuration includes "image" and "proprio" (proprioceptive) data types, with eye-in-hand and gripper observations enabled.

**Sequence & Temporal:**
- Sequence length: 10 steps
- Maximum word length: 25 characters

**Action Configuration:**
- Affine translation dimension: 4
- Action scale: 1.0
- Training/dataset split: 80% train ratio

**Additional Specifications:**
- Single task group (no multitasking)
- Task shuffling disabled
- Joint states and end-effector gripper information included
- State dimension: not predefined (null)

**Environment Mapping:**
Observations map to robosuite-compatible keys: agentview_image, robot0_eye_in_hand_image, robot0_gripper_qpos, and robot0_joint_pos.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "59e3d73e-aa19-4987-91e8-ede795e1ad1b"
}
```

</details>

---

### Tool result

_source line 216 · 2026-05-15T11:13:56.561Z_

<details><summary>↩ Tool result · `toolu_016iySNFkgaiG38YX1yt8Na5`</summary>

```text
# Evaluation Configuration Extracted

Based on the provided configuration file, here are the evaluation parameters:

**Evaluation Episodes & Frequency:**
- `"n_eval: 20"` — number of evaluation episodes per evaluation cycle
- `"eval_every: 5"` — evaluation conducted at 5-step intervals

**Maximum Steps:**
- `"max_steps: 600"` — training terminates at 600 steps total

**Processing Parameters:**
- `"batch_size: 64"` — samples processed per batch during evaluation
- `"num_workers: 4"` — parallel workers for data loading
- `"use_mp: true"` with `"num_procs: 20"` — multiprocessing enabled across 20 processes

**Additional Settings:**
- `"eval: true"` — evaluation mode activated
- `"save_sim_states: false"` — simulation states not preserved

**Note:** No explicit success metrics are defined in this configuration snippet. The document contains infrastructure and scheduling parameters but lacks threshold-based performance criteria.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "8f0f4dfd-93a5-4f2c-8c3e-a04d196e60e2"
}
```

</details>

---

### Tool result

_source line 217 · 2026-05-15T11:14:10.559Z_

<details><summary>↩ Tool result · `toolu_01XzxZ2apnwbURLoJNku4jZu`</summary>

```text
Web search results for query: "LIBERO benchmark dataset size GB each suite libero_spatial libero_object libero_goal libero_90 libero_long download"

Links: [{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"Libero-Object Benchmark","url":"https://www.emergentmind.com/topics/libero-object-benchmark"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"Libero - LeRobot","url":"https://www.mintlify.com/huggingface/lerobot/simulation/libero"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"LIBERO Datasets – LIBERO","url":"https://libero-project.github.io/datasets"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"}]

Let me search more specifically for dataset size information in GB.

Links: [{"title":"HuggingFaceVLA/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/libero"},{"title":"yifengzhu-hf/LIBERO-datasets · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"physical-intelligence/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/physical-intelligence/libero"},{"title":"HuggingFaceVLA/smol-libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/smol-libero"},{"title":"lerobot/libero_10_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_10_image"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"yilin-wu/libero-10 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yilin-wu/libero-10"},{"title":"allenai/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/allenai/libero"},{"title":"yfpeng1234/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yfpeng1234/libero"}]

Now let me search for the individual suite sizes and libero_90 information.

Links: [{"title":"LIBERO Datasets – LIBERO","url":"https://libero-project.github.io/datasets"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"Libero - LeRobot","url":"https://www.mintlify.com/huggingface/lerobot/simulation/libero"},{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"},{"title":"Code Structures — libero 0.1.0 documentation","url":"https://lifelong-robot-learning.github.io/LIBERO/html/getting_started/code_structure.html"},{"title":"physical-intelligence/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/physical-intelligence/libero"},{"title":"libero · PyPI","url":"https://pypi.org/project/libero/"},{"title":"yifengzhu-hf/LIBERO-datasets · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets"},{"title":"ML-GOD/libero_goal · Datasets at Hugging Face","url":"https://huggingface.co/datasets/ML-GOD/libero_goal"}]

Let me search for more specific size information for each suite.

Links: [{"title":"huiliu123/libero-spatial-dreamzero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/huiliu123/libero-spatial-dreamzero"},{"title":"openvla/openvla-7b-finetuned-libero-spatial at main","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-spatial/tree/main"},{"title":"lerobot/libero_spatial_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_spatial_image"},{"title":"physical-intelligence/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/physical-intelligence/libero"},{"title":"Storage limits · Hugging Face","url":"https://huggingface.co/docs/hub/storage-limits"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"yfpeng1234/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yfpeng1234/libero"},{"title":"Not enough disk space error when downloading a model from Hugging Face - Databricks","url":"https://kb.databricks.com/machine-learning/not-enough-disk-space-error-when-downloading-a-model-from-hugging-face"},{"title":"Hugging Face Dataset Upload Decision Guide · Hugging Face","url":"https://huggingface.co/docs/hub/datasets-upload-guide-llm"},{"title":"Calculating the size of all LFS files in a repo | Simon Willison’s TILs","url":"https://til.simonwillison.net/git/size-of-lfs-files"}]

Let me search for more specific information about libero_goal and libero_90 sizes.

Links: [{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/main/en/libero"},{"title":"physical-intelligence/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/physical-intelligence/libero"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"jesbu1/libero_90_lerobot · Datasets at Hugging Face","url":"https://huggingface.co/datasets/jesbu1/libero_90_lerobot"},{"title":"Libero - LeRobot","url":"https://www.mintlify.com/huggingface/lerobot/simulation/libero"},{"title":"IPEC-COMMUNITY/libero_90_no_noops_lerobot · Dataset converted ideas","url":"https://huggingface.co/datasets/IPEC-COMMUNITY/libero_90_no_noops_lerobot/discussions/2"},{"title":"ML-GOD/libero_goal · Datasets at Hugging Face","url":"https://huggingface.co/datasets/ML-GOD/libero_goal"}]

Based on my web search results, I can provide you with the LIBERO benchmark dataset size information:

## LIBERO Dataset Sizes

**Combined Dataset:**
The complete LIBERO dataset has a total file size of 34.9 GB, with 273,465 frames across 1,693 episodes and 40 tasks.

**Individual Suite Sizes:**

libero_object: 9.25 GB

libero_spatial: 6.61 GB

libero_10 (LIBERO-Long): 12.8 GB

**Note:** The search results indicate that an alternative LIBERO dataset repository shows a total of 100 GB, which appears to be the complete uncompressed/original version from the official LIBERO project.

**libero_long vs libero_10:** LIBERO-Long (libero_10) contains 10 long-horizon tasks from LIBERO-100, and LIBERO-90 (libero_90) contains 90 short-horizon tasks from LIBERO-100.

**Download:** The physical-intelligence/libero dataset on HuggingFace combines four individual datasets: Libero-Spatial, Libero-Object, Libero-Goal and Libero-10, totaling the 34.9 GB mentioned above.

I was unable to find exact GB sizes for libero_goal and libero_90 individual suites in the search results, but they are available on HuggingFace alongside the other datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "7bfa8eae-7165-4503-a67d-4fc7d08dc5da"
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
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://libero-project.github.io/datasets",
  "usage": {
    "total_tokens": 37291,
    "tool_uses": 31,
    "duration_ms": 144097
  },
  "last_tool_name": "WebFetch",
  "uuid": "795e5ec5-4768-4390-8416-6ccbe001a4e5",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 219_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Vkksn3VtQ8PnSh35hKnTFF`</summary>

```json
{
  "url": "https://libero-project.github.io/datasets",
  "prompt": "Extract ALL dataset details: size of each suite, number of demonstrations per task, total data sizes, download instructions, and any other specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "a148ff46-3a79-4b99-9cc6-b3efd05ccabb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YKuWVaAKvWNoVM3i22zoYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3615,
      "cache_read_input_tokens": 32706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3615,
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

_source line 220_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://huggingface.co/datasets/physical-intellig…",
  "usage": {
    "total_tokens": 37353,
    "tool_uses": 32,
    "duration_ms": 145841
  },
  "last_tool_name": "WebFetch",
  "uuid": "b7f90509-da30-4a11-918e-01cba3e0282f",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 221_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FJYWR2rz9xFGbUxnpwyd1H`</summary>

```json
{
  "url": "https://huggingface.co/datasets/physical-intelligence/libero",
  "prompt": "Extract dataset size information: total size, individual suite sizes (libero_spatial, libero_object, libero_goal, libero_10/libero_long, libero_90), number of episodes per suite, file counts, and any other size/format details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "dba33296-81fd-40d7-abc2-9c06b6d5fea0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YKuWVaAKvWNoVM3i22zoYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3615,
      "cache_read_input_tokens": 32706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3615,
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

_source line 222_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://raw.githubusercontent.com/Lifelong-Robot-…",
  "usage": {
    "total_tokens": 37415,
    "tool_uses": 33,
    "duration_ms": 146643
  },
  "last_tool_name": "WebFetch",
  "uuid": "7bfc0b7c-85b7-448c-a509-d669f248cde9",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 223_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Fnhy4RnpbxBEYhTyxhn6rb`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/configs/policy/bc_transformer_policy.yaml",
  "prompt": "Extract ALL policy configuration: observation dimensions, action dimensions, network architecture, and any other relevant specs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "d07cfddc-45a7-44d2-8246-3979fb03b717",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YKuWVaAKvWNoVM3i22zoYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3615,
      "cache_read_input_tokens": 32706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3615,
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

_source line 224_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a1a91bef0d6739352",
  "tool_use_id": "toolu_01DvNbgBP79dBVtsQLdBJJGb",
  "status": "completed",
  "output_file": "",
  "summary": "Research LeRobot LIBERO integration",
  "usage": {
    "total_tokens": 33918,
    "tool_uses": 18,
    "duration_ms": 137965
  },
  "uuid": "e27622b4-5649-430d-a07f-d4c393f920fb",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool result

_source line 225 · 2026-05-15T11:14:16.729Z_

<details><summary>↩ Tool result · `toolu_01DvNbgBP79dBVtsQLdBJJGb`</summary>

````text


Here is the structured research report.

---

## 1. Does LeRobot Natively Support LIBERO?

**Yes.** LIBERO is a first-class benchmark in LeRobot. It is installed via:

```bash
pip install -e ".[libero]"
```

LeRobot provides native environment wrappers (`--env.type=libero`), official documentation at [huggingface.co/docs/lerobot/en/libero](https://huggingface.co/docs/lerobot/en/libero), and a dedicated fork of the LIBERO codebase at [github.com/huggingface/lerobot-libero](https://github.com/huggingface/lerobot-libero).

LIBERO covers **130 tasks** across **5 task suites**:

| Suite | CLI name | Tasks | Description |
|-------|----------|-------|-------------|
| LIBERO-Spatial | `libero_spatial` | 10 | Spatial relation reasoning |
| LIBERO-Object | `libero_object` | 10 | Object manipulation |
| LIBERO-Goal | `libero_goal` | 10 | Goal-conditioned tasks |
| LIBERO-90 | `libero_90` | 90 | Short-horizon tasks |
| LIBERO-Long | `libero_10` | 10 | Long-horizon tasks |

There is also **LIBERO-plus** (`--env.type=libero_plus`), a robustness extension with ~10,000 perturbed task variants across 7 dimensions (camera, lighting, layout, language, etc.).

---

## 2. Dataset Names on HuggingFace Hub

### Primary datasets (recommended for training)

| Dataset ID | Episodes | Tasks | Size | Notes |
|------------|----------|-------|------|-------|
| `HuggingFaceVLA/libero` | 148 | 10 | ~1.9 GB | Official preprocessed dataset, recommended by LeRobot docs |
| `lerobot/libero` | 1,693 | 40 | ~1.94 GB | All 4 standard suites combined (video format, AV1 codec) |
| `physical-intelligence/libero` | 147 | 10 | ~34.9 GB | PI's conversion, RLDS-origin, CC-BY-4.0 |
| `lerobot/libero_plus` | — | — | — | LIBERO-plus training data |

### Per-suite image datasets

| Dataset ID | Tasks | Episodes |
|------------|-------|----------|
| `lerobot/libero_10_image` | 10 | 148 |
| `lerobot/libero_object_image` | 10 | 454 |
| `lerobot/libero_spatial_image` | 10 | — |
| `lerobot/libero_goal_image` | 10 | — |

### Community datasets

| Dataset ID | Notes |
|------------|-------|
| `IPEC-COMMUNITY/libero_90_no_noops_lerobot` | LIBERO-90 with no-ops removed |

---

## 3. Data Format Mapping (LIBERO HDF5/RLDS to LeRobot)

### Observation/Action schema

| LIBERO Field | LeRobot Feature | Type | Shape |
|---|---|---|---|
| `observation["image"]` / `agentview_image` | `observation.images.image` | Video/Image | (256, 256, 3) |
| `observation["wrist_image"]` / `robot0_eye_in_hand_image` | `observation.images.image2` (or `.wrist_image`) | Video/Image | (256, 256, 3) |
| `observation["state"]` | `observation.state` | float32 | (8,) |
| `action` | `action` | float32 | (7,) |
| `language_instruction` | `task` (task_index) | string/int | — |

### LeRobot dataset metadata

- **robot_type**: `panda`
- **fps**: `10`
- **Video codec**: AV1, yuv420p (for video datasets)
- **Storage**: Parquet for tabular data + MP4 for video streams

### State vector (8-dim)
End-effector position (3) + axis-angle orientation (3) + gripper qpos (2)

### Action vector (7-dim)
6D end-effector delta + 1D gripper command. Range: `Box(-1, 1, shape=(7,))`

---

## 4. Conversion Scripts and Utilities

### A. Physical Intelligence's OpenPI conversion script (primary)

**Path**: [`Physical-Intelligence/openpi/examples/libero/convert_libero_data_to_lerobot.py`](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py)

**Prerequisites**:
```bash
uv pip install tensorflow tensorflow_datasets
```

**Raw data source**: Download from `https://huggingface.co/datasets/openvla/modified_libero_rlds`

**Usage**:
```bash
uv run examples/libero/convert_libero_data_to_lerobot.py \
  --data_dir /path/to/your/data \
  --push_to_hub
```

**What it does**:
1. Reads 4 raw RLDS datasets: `libero_10_no_noops`, `libero_goal_no_noops`, `libero_object_no_noops`, `libero_spatial_no_noops`
2. Creates a `LeRobotDataset` with robot_type=panda, fps=10
3. Iterates episodes, calling `dataset.add_frame()` per step
4. Calls `dataset.save_episode()` per episode
5. Optionally pushes to HuggingFace Hub

**Processing time**: ~30 minutes.

**Key imports**:
```python
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
import tensorflow_datasets as tfds
```

### B. Generic HDF5 to LeRobot converter

**Repo**: [github.com/anarnuri/hdf5_to_lerobot_converter](https://github.com/anarnuri/hdf5_to_lerobot_converter)

Works with custom HDF5 formats including LIBERO's native format.

### C. Using pre-converted datasets (no conversion needed)

The simplest path is to use the already-converted datasets directly:

```python
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset

dataset = LeRobotDataset("HuggingFaceVLA/libero")
# or
dataset = LeRobotDataset("lerobot/libero")
```

### D. Training command (end-to-end example)

```bash
lerobot-train \
  --policy.type=smolvla \
  --policy.repo_id=${HF_USER}/libero-test \
  --policy.load_vlm_weights=true \
  --dataset.repo_id=HuggingFaceVLA/libero \
  --env.type=libero \
  --env.task=libero_10 \
  --output_dir=./outputs/ \
  --steps=100000 \
  --batch_size=4 \
  --eval.batch_size=1 \
  --eval.n_episodes=1 \
  --eval_freq=1000
```

### E. Evaluation command

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```

---

## Key Takeaways for This Project

1. **No conversion work needed** if using the pre-converted `HuggingFaceVLA/libero` or `lerobot/libero` datasets.
2. If you need LIBERO-90 data specifically, it is NOT in the standard pre-converted datasets. You would need the OpenPI conversion script or the community `IPEC-COMMUNITY/libero_90_no_noops_lerobot` dataset.
3. The LeRobot LIBERO env wrapper handles MuJoCo simulation natively (Linux only, `MUJOCO_GL=egl` for headless).
4. Control modes: `relative` (default) vs `absolute` -- must match your policy's action parameterization.

Sources:
- [LeRobot LIBERO Documentation](https://huggingface.co/docs/lerobot/en/libero)
- [LeRobot LIBERO-plus Documentation](https://huggingface.co/docs/lerobot/main/libero_plus)
- [lerobot/libero dataset](https://huggingface.co/datasets/lerobot/libero)
- [HuggingFaceVLA/libero dataset](https://huggingface.co/datasets/HuggingFaceVLA/libero)
- [physical-intelligence/libero dataset](https://huggingface.co/datasets/physical-intelligence/libero)
- [OpenPI LIBERO conversion script](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py)
- [huggingface/lerobot-libero fork](https://github.com/huggingface/lerobot-libero)
- [huggingface/lerobot main repo](https://github.com/huggingface/lerobot)
- [lerobot/libero_10_image](https://huggingface.co/datasets/lerobot/libero_10_image)
- [lerobot/libero_object_image](https://huggingface.co/datasets/lerobot/libero_object_image)
- [lerobot/libero_spatial_image](https://huggingface.co/datasets/lerobot/libero_spatial_image)
- [HDF5 to LeRobot converter](https://github.com/anarnuri/hdf5_to_lerobot_converter)

agentId: a1a91bef0d6739352 (use SendMessage with to: 'a1a91bef0d6739352' to continue this agent)
&lt;usage>total_tokens: 36471
tool_uses: 18
duration_ms: 137969&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "7ced5aba-bb85-44c7-b518-7eed96e90e1d",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Research the integration between LeRobot (HuggingFace's robot learning framework) and the LIBERO benchmark.\n\nI need to find:\n1. Does LeRobot natively support LIBERO datasets?\n2. If yes, what are the dataset names on HuggingFace Hub?\n3. What is the data conversion pipeline from LIBERO's native HDF5 format to LeRobot format?\n4. Any conversion scripts or utilities available\n\nUse WebSearch to search for:\n- \"LeRobot LIBERO\" \n- \"lerobot libero dataset\"\n- HuggingFace Hub LIBERO datasets\n- \"lerobot convert libero\"\n\nThen use WebFetch to check:\n- The LeRobot GitHub repo for LIBERO-related code\n- HuggingFace Hub for LIBERO datasets in LeRobot format\n- Any conversion scripts or documentation\n\nReport everything in structured format with exact dataset names, commands, and code paths.",
    "agentId": "a1a91bef0d6739352",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\nHere is the structured research report.\n\n---\n\n## 1. Does LeRobot Natively Support LIBERO?\n\n**Yes.** LIBERO is a first-class benchmark in LeRobot. It is installed via:\n\n```bash\npip install -e \".[libero]\"\n```\n\nLeRobot provides native environment wrappers (`--env.type=libero`), official documentation at [huggingface.co/docs/lerobot/en/libero](https://huggingface.co/docs/lerobot/en/libero), and a dedicated fork of the LIBERO codebase at [github.com/huggingface/lerobot-libero](https://github.com/huggingface/lerobot-libero).\n\nLIBERO covers **130 tasks** across **5 task suites**:\n\n| Suite | CLI name | Tasks | Description |\n|-------|----------|-------|-------------|\n| LIBERO-Spatial | `libero_spatial` | 10 | Spatial relation reasoning |\n| LIBERO-Object | `libero_object` | 10 | Object manipulation |\n| LIBERO-Goal | `libero_goal` | 10 | Goal-conditioned tasks |\n| LIBERO-90 | `libero_90` | 90 | Short-horizon tasks |\n| LIBERO-Long | `libero_10` | 10 | Long-horizon tasks |\n\nThere is also **LIBERO-plus** (`--env.type=libero_plus`), a robustness extension with ~10,000 perturbed task variants across 7 dimensions (camera, lighting, layout, language, etc.).\n\n---\n\n## 2. Dataset Names on HuggingFace Hub\n\n### Primary datasets (recommended for training)\n\n| Dataset ID | Episodes | Tasks | Size | Notes |\n|------------|----------|-------|------|-------|\n| `HuggingFaceVLA/libero` | 148 | 10 | ~1.9 GB | Official preprocessed dataset, recommended by LeRobot docs |\n| `lerobot/libero` | 1,693 | 40 | ~1.94 GB | All 4 standard suites combined (video format, AV1 codec) |\n| `physical-intelligence/libero` | 147 | 10 | ~34.9 GB | PI's conversion, RLDS-origin, CC-BY-4.0 |\n| `lerobot/libero_plus` | — | — | — | LIBERO-plus training data |\n\n### Per-suite image datasets\n\n| Dataset ID | Tasks | Episodes |\n|------------|-------|----------|\n| `lerobot/libero_10_image` | 10 | 148 |\n| `lerobot/libero_object_image` | 10 | 454 |\n| `lerobot/libero_spatial_image` | 10 | — |\n| `lerobot/libero_goal_image` | 10 | — |\n\n### Community datasets\n\n| Dataset ID | Notes |\n|------------|-------|\n| `IPEC-COMMUNITY/libero_90_no_noops_lerobot` | LIBERO-90 with no-ops removed |\n\n---\n\n## 3. Data Format Mapping (LIBERO HDF5/RLDS to LeRobot)\n\n### Observation/Action schema\n\n| LIBERO Field | LeRobot Feature | Type | Shape |\n|---|---|---|---|\n| `observation[\"image\"]` / `agentview_image` | `observation.images.image` | Video/Image | (256, 256, 3) |\n| `observation[\"wrist_image\"]` / `robot0_eye_in_hand_image` | `observation.images.image2` (or `.wrist_image`) | Video/Image | (256, 256, 3) |\n| `observation[\"state\"]` | `observation.state` | float32 | (8,) |\n| `action` | `action` | float32 | (7,) |\n| `language_instruction` | `task` (task_index) | string/int | — |\n\n### LeRobot dataset metadata\n\n- **robot_type**: `panda`\n- **fps**: `10`\n- **Video codec**: AV1, yuv420p (for video datasets)\n- **Storage**: Parquet for tabular data + MP4 for video streams\n\n### State vector (8-dim)\nEnd-effector position (3) + axis-angle orientation (3) + gripper qpos (2)\n\n### Action vector (7-dim)\n6D end-effector delta + 1D gripper command. Range: `Box(-1, 1, shape=(7,))`\n\n---\n\n## 4. Conversion Scripts and Utilities\n\n### A. Physical Intelligence's OpenPI conversion script (primary)\n\n**Path**: [`Physical-Intelligence/openpi/examples/libero/convert_libero_data_to_lerobot.py`](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py)\n\n**Prerequisites**:\n```bash\nuv pip install tensorflow tensorflow_datasets\n```\n\n**Raw data source**: Download from `https://huggingface.co/datasets/openvla/modified_libero_rlds`\n\n**Usage**:\n```bash\nuv run examples/libero/convert_libero_data_to_lerobot.py \\\n  --data_dir /path/to/your/data \\\n  --push_to_hub\n```\n\n**What it does**:\n1. Reads 4 raw RLDS datasets: `libero_10_no_noops`, `libero_goal_no_noops`, `libero_object_no_noops`, `libero_spatial_no_noops`\n2. Creates a `LeRobotDataset` with robot_type=panda, fps=10\n3. Iterates episodes, calling `dataset.add_frame()` per step\n4. Calls `dataset.save_episode()` per episode\n5. Optionally pushes to HuggingFace Hub\n\n**Processing time**: ~30 minutes.\n\n**Key imports**:\n```python\nfrom lerobot.common.datasets.lerobot_dataset import LeRobotDataset\nimport tensorflow_datasets as tfds\n```\n\n### B. Generic HDF5 to LeRobot converter\n\n**Repo**: [github.com/anarnuri/hdf5_to_lerobot_converter](https://github.com/anarnuri/hdf5_to_lerobot_converter)\n\nWorks with custom HDF5 formats including LIBERO's native format.\n\n### C. Using pre-converted datasets (no conversion needed)\n\nThe simplest path is to use the already-converted datasets directly:\n\n```python\nfrom lerobot.common.datasets.lerobot_dataset import LeRobotDataset\n\ndataset = LeRobotDataset(\"HuggingFaceVLA/libero\")\n# or\ndataset = LeRobotDataset(\"lerobot/libero\")\n```\n\n### D. Training command (end-to-end example)\n\n```bash\nlerobot-train \\\n  --policy.type=smolvla \\\n  --policy.repo_id=${HF_USER}/libero-test \\\n  --policy.load_vlm_weights=true \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --env.type=libero \\\n  --env.task=libero_10 \\\n  --output_dir=./outputs/ \\\n  --steps=100000 \\\n  --batch_size=4 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=1 \\\n  --eval_freq=1000\n```\n\n### E. Evaluation command\n\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n\n---\n\n## Key Takeaways for This Project\n\n1. **No conversion work needed** if using the pre-converted `HuggingFaceVLA/libero` or `lerobot/libero` datasets.\n2. If you need LIBERO-90 data specifically, it is NOT in the standard pre-converted datasets. You would need the OpenPI conversion script or the community `IPEC-COMMUNITY/libero_90_no_noops_lerobot` dataset.\n3. The LeRobot LIBERO env wrapper handles MuJoCo simulation natively (Linux only, `MUJOCO_GL=egl` for headless).\n4. Control modes: `relative` (default) vs `absolute` -- must match your policy's action parameterization.\n\nSources:\n- [LeRobot LIBERO Documentation](https://huggingface.co/docs/lerobot/en/libero)\n- [LeRobot LIBERO-plus Documentation](https://huggingface.co/docs/lerobot/main/libero_plus)\n- [lerobot/libero dataset](https://huggingface.co/datasets/lerobot/libero)\n- [HuggingFaceVLA/libero dataset](https://huggingface.co/datasets/HuggingFaceVLA/libero)\n- [physical-intelligence/libero dataset](https://huggingface.co/datasets/physical-intelligence/libero)\n- [OpenPI LIBERO conversion script](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py)\n- [huggingface/lerobot-libero fork](https://github.com/huggingface/lerobot-libero)\n- [huggingface/lerobot main repo](https://github.com/huggingface/lerobot)\n- [lerobot/libero_10_image](https://huggingface.co/datasets/lerobot/libero_10_image)\n- [lerobot/libero_object_image](https://huggingface.co/datasets/lerobot/libero_object_image)\n- [lerobot/libero_spatial_image](https://huggingface.co/datasets/lerobot/libero_spatial_image)\n- [HDF5 to LeRobot converter](https://github.com/anarnuri/hdf5_to_lerobot_converter)"
      }
    ],
    "totalDurationMs": 137969,
    "totalTokens": 36471,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 305,
      "cache_read_input_tokens": 33565,
      "output_tokens": 2598,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 305
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2598,
          "cache_read_input_tokens": 33565,
          "cache_creation_input_tokens": 305,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 305,
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
      "otherToolCount": 18
    }
  }
}
````

</details>

---

### Tool result

_source line 226 · 2026-05-15T11:14:16.885Z_

<details><summary>↩ Tool result · `toolu_01Vkksn3VtQ8PnSh35hKnTFF`</summary>

```text
# LIBERO Datasets Summary

Based on the webpage content provided, here's what can be extracted about the datasets:

## Available Suites

The page lists four dataset suites:
- **LIBERO-Spatial**: "10 tasks from LIBERO-Spatial suite"
- **LIBERO-Object**: "10 tasks from LIBERO-Object suite"
- **LIBERO-Goal**: "10 tasks from LIBERO-Goal suite"
- **LIBERO-100**: "100 tasks from LIBERO-100 suite" with data organized under LIBERO-90 and LIBERO-10 folders

## Data Included

Each dataset contains:
- "RGB images from workspace and wrist cameras"
- Proprioceptive sensor readings
- Language-based task descriptions
- PDDL scene representations

## Access Methods

The page provides direct download links for each suite via University of Texas Box storage, plus "a script for programmatic downloading the datasets" through their documentation portal.

## Limitations

The webpage does not specify demonstration counts per task, total storage sizes, or other granular specifications—only directing users to the full LIBERO documentation for comprehensive details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "0a805881-b17f-43a6-b032-30570158c39a"
}
```

</details>

---

### Tool result

_source line 227 · 2026-05-15T11:14:21.115Z_

<details><summary>↩ Tool result · `toolu_01Fnhy4RnpbxBEYhTyxhn6rb`</summary>

```text
# Policy Configuration Extraction

## Policy Type & Architecture
- **Policy Type**: BCTransformerPolicy
- **Extra Network Layers**: 0
- **Extra Hidden Size**: 128
- **Embedding Size**: 64

## Transformer Specifications
- **Number of Layers**: 4
- **Attention Heads**: 6
- **Head Output Size**: 64 per head
- **MLP Hidden Size**: 256
- **Dropout Rate**: 0.1
- **Maximum Sequence Length**: 10
- **Input Size**: Not specified (null)

## Default Component Configuration
The policy uses several standard modules:
- **Image Encoding**: ResNet-based encoder
- **Language Encoding**: MLP encoder
- **Temporal Positioning**: Sinusoidal position encoding
- **Policy Head**: Gaussian Mixture Model head
- **Data Augmentation**: Includes color jittering and translation augmentation

## Notable Gaps
The configuration does not explicitly specify observation or action dimensions—these are likely defined in referenced encoder and head configuration files (e.g., `resnet_encoder.yaml`, `gmm_head.yaml`).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "423cb002-e907-434d-bb15-a3764832513f"
}
```

</details>

---

### Tool result

_source line 228 · 2026-05-15T11:14:21.962Z_

<details><summary>↩ Tool result · `toolu_01FJYWR2rz9xFGbUxnpwyd1H`</summary>

```text
# LIBERO Dataset Size Information

Based on the webpage content, here's the dataset size information:

## Overall Dataset Statistics

- **Total Rows**: 273,000 frames
- **Total Episodes**: 147 episodes
- **Dataset Size Category**: 100K - 1M (parquet format)
- **Task Categories**: 10 distinct tasks
- **Data Format**: Parquet (auto-converted from original format)

## Dataset Structure

### Subsets
- **Default subset**: 273k rows

### Splits
- **Train split**: 273k rows (only split available)

## Data Modalities

The dataset includes:
- **Image data**: 256x256 pixel resolution
  - `image`: Main camera view
  - `wrist_image`: Wrist-mounted camera view
- **Time-series data**:
  - `state`: Robot state vector (8 dimensions)
  - `actions`: Action vectors (7 dimensions)
  - `timestamp`: Float32 values

## Frame-level Metadata

Each frame includes:
- `frame_index`: 0-454 (frames per episode)
- `episode_index`: 0-146 (episode identifier)
- `task_index`: 0-9 (10 tasks)
- `index`: 0-40.1k (global frame identifier)

## Related Information

- **Libraries**: Datasets, Dask, Croissant
- **License**: CC-BY-4.0
- **Organization**: Physical Intelligence
- **Related Tags**: LeRobot, libero, panda, rlds
- **Citation**: arXiv:2306.03310

The dataset appears to be a large-scale robotics manipulation dataset with multiple camera views and synchronized state-action pairs suitable for imitation learning and robot learning research.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "97bb1775-718e-49fb-b80c-2d473f418c98"
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
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://raw.githubusercontent.com/Lifelong-Robot-…",
  "usage": {
    "total_tokens": 38836,
    "tool_uses": 34,
    "duration_ms": 156667
  },
  "last_tool_name": "WebFetch",
  "uuid": "76c89497-f61d-4a87-9968-a4ceb10bc21a",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 230_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CUXfWpdLkw8bYM7EeHYfAi`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/libero/benchmark/libero_suite_task_map.py",
  "prompt": "Extract the complete task list for each suite: LIBERO-Spatial (all 10 task descriptions), LIBERO-Object (all 10 task descriptions), LIBERO-Goal (all 10 task descriptions). Show the exact task names/descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "c12a5ae8-70d6-40e3-87d2-991accbb0966",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EETyr9yjn7fH6fqPMsfthv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 290,
      "cache_creation_input_tokens": 1073,
      "cache_read_input_tokens": 36321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1073,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
      "service_tier": "standard",
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

_source line 231_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "description": "Fetching https://pypi.org/project/libero/",
  "usage": {
    "total_tokens": 38895,
    "tool_uses": 35,
    "duration_ms": 157165
  },
  "last_tool_name": "WebFetch",
  "uuid": "8e0f7f6f-693f-4a02-88f3-c1b0cb294a64",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool call

_source line 232_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017xwRmqtNU9LVcmdPT5qGVG`</summary>

```json
{
  "url": "https://pypi.org/project/libero/",
  "prompt": "Extract installation instructions, version info, dependencies, and any other details about the LIBERO pip package."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "e257da7c-6e1c-4f95-a39c-43246989c824",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EETyr9yjn7fH6fqPMsfthv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 290,
      "cache_creation_input_tokens": 1073,
      "cache_read_input_tokens": 36321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1073,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 233 · 2026-05-15T11:14:31.505Z_

<details><summary>↩ Tool result · `toolu_01CUXfWpdLkw8bYM7EeHYfAi`</summary>

```text
# LIBERO Task Suites

## LIBERO-Spatial (10 tasks)
1. "pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate"
2. "pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate"
3. "pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate"
4. "pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate"
5. "pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate"
6. "pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate"
7. "pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate"
8. "pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate"
9. "pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate"
10. "pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate"

## LIBERO-Object (10 tasks)
1. "pick_up_the_alphabet_soup_and_place_it_in_the_basket"
2. "pick_up_the_cream_cheese_and_place_it_in_the_basket"
3. "pick_up_the_salad_dressing_and_place_it_in_the_basket"
4. "pick_up_the_bbq_sauce_and_place_it_in_the_basket"
5. "pick_up_the_ketchup_and_place_it_in_the_basket"
6. "pick_up_the_tomato_sauce_and_place_it_in_the_basket"
7. "pick_up_the_butter_and_place_it_in_the_basket"
8. "pick_up_the_milk_and_place_it_in_the_basket"
9. "pick_up_the_chocolate_pudding_and_place_it_in_the_basket"
10. "pick_up_the_orange_juice_and_place_it_in_the_basket"

## LIBERO-Goal (10 tasks)
1. "open_the_middle_drawer_of_the_cabinet"
2. "put_the_bowl_on_the_stove"
3. "put_the_wine_bottle_on_top_of_the_cabinet"
4. "open_the_top_drawer_and_put_the_bowl_inside"
5. "put_the_bowl_on_top_of_the_cabinet"
6. "push_the_plate_to_the_front_of_the_stove"
7. "put_the_cream_cheese_in_the_bowl"
8. "turn_on_the_stove"
9. "put_the_bowl_on_the_plate"
10. "put_the_wine_bottle_on_the_rack"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "f798a64a-6aed-4b33-976c-a85e36d812f4"
}
```

</details>

---

### Tool result

_source line 234 · 2026-05-15T11:14:32.136Z_

<details><summary>↩ Tool result · `toolu_017xwRmqtNU9LVcmdPT5qGVG`</summary>

````text
# LIBERO Package Information

## Version & Release
- **Current Version:** 0.1.1
- **Release Date:** November 3, 2025
- **Python Requirement:** Python >=3

## Installation

The package supports two installation methods:

**Standard Installation:**
```bash
conda create -n libero python=3.8.13
conda activate libero
git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git
cd LIBERO
pip install -r requirements.txt
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
pip install -e .
```

**PyPI Installation:**
```bash
pip install libero
```

## Project Overview

"LIBERO is designed for studying knowledge transfer in multitask and lifelong robot learning problems." The benchmark provides 130 tasks organized into four suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100.

## Key Features

- Procedural generation pipeline for manipulation tasks
- Four task suites with controlled distribution shifts
- Three policy architectures: bc_rnn_policy, bc_transformer_policy, bc_vilt_policy
- Multiple lifelong learning algorithms

## Maintainers
- imstevenpmwork
- jadechoghari (Jade Choghari, HuggingFace)

## Licensing

| Component | License |
|-----------|---------|
| Codebase | MIT |
| Datasets | CC BY 4.0 |
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "9a6ee017-c786-4d8e-886d-204b2d559b5b"
}
```

</details>

---

### System

_source line 235_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "aada8a30ff0506204",
  "tool_use_id": "toolu_016hJaz9VaWPx61DxYHc9fM9",
  "status": "completed",
  "output_file": "",
  "summary": "Research LIBERO-Plus perturbation",
  "usage": {
    "total_tokens": 33883,
    "tool_uses": 20,
    "duration_ms": 182444
  },
  "uuid": "f3191d1e-7dc9-48ad-92e5-f812a86f7dbc",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool result

_source line 236 · 2026-05-15T11:14:56.862Z_

<details><summary>↩ Tool result · `toolu_016hJaz9VaWPx61DxYHc9fM9`</summary>

````text


Here is the structured research report.

---

## 1. What LIBERO-Plus Is

LIBERO-Plus is a robustness evaluation benchmark that extends the original LIBERO robot manipulation benchmark. It was published as "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models" (arXiv:2510.13626, accepted at CVPR 2026).

**What it adds on top of LIBERO:**
- **10,030 task variants** generated by applying systematic perturbations to original LIBERO tasks
- **7 perturbation dimensions** with **21 sub-dimensions**
- **5 difficulty levels** (L1-L5) stratified by multi-model consensus (how many of 4 reference models solve the task)
- **20,000+ training trajectories** collected under varied conditions (stored in RLDS format)
- Drop-in replacement for vanilla LIBERO — same Python interface, same camera names, same observation/action format

## 2. Source

- **Paper:** [arXiv:2510.13626](https://arxiv.org/abs/2510.13626)
- **GitHub:** [github.com/sylvestf/LIBERO-plus](https://github.com/sylvestf/LIBERO-plus)
- **Project page:** [sylvestf.github.io/LIBERO-plus](https://sylvestf.github.io/LIBERO-plus/)
- **Assets (HuggingFace):** [Sylvest/LIBERO-plus](https://huggingface.co/datasets/Sylvest/LIBERO-plus)
- **Training dataset (RLDS):** [Sylvest/libero_plus_rlds](https://huggingface.co/datasets/Sylvest/libero_plus_rlds)
- **LeRobot-format dataset:** [lerobot/libero_plus](https://huggingface.co/datasets/lerobot/libero_plus)

## 3. The 7 Perturbation Dimensions (Exact Definitions)

Note: The user asked about 4 dimensions. LIBERO-Plus actually defines **7**, not 4.

### 3.1 Objects Layout (O1, O2)
- **O1 — Confounding objects:** Adds n additional unseen distractor objects into the scene from a pool of 416 objects, implemented by modifying BDDL task description files.
- **O2 — Target displacement:** Applies random perturbations to the target object's initial position (x, y, z) and orientation while preserving semantic relationships.

### 3.2 Camera Viewpoints (C1, C2, C3)
- **C1 — Distance scaling:** Scales camera distance from 1.01x to 2.00x the original value along the optical axis.
- **C2 — Spherical position:** Changes azimuth (delta-theta) and elevation (delta-phi) within 15 to 75 degree cones.
- **C3 — Orientation perturbation:** Perturbs yaw, pitch, roll within 2 to 10 degrees.

Implementation: Modifies the `Problem` class interface; parameters derived from task filenames. Targets the third-person camera primarily (not wrist camera).

### 3.3 Robot Initial States
- Applies random perturbations to the robot arm's initial joint positions with magnitudes 0.1 to 0.5.
- Implementation: Modifies the `Problem` class interface.

### 3.4 Language Instructions (R1, R2, R3)
- **R1 — Distraction rewrites:** Adds task-irrelevant contextual information.
- **R2 — Commonsense substitution:** Replaces object descriptions with commonsense-based alternatives.
- **R3 — Reasoning complexity:** Alters reasoning complexity for multi-step tasks.
- Implementation: LLM-based instruction rewriting.

### 3.5 Light Conditions (L1, L2, L3, L4)
- **L1 — Diffuse color:** RGB channel adjustment of diffuse lighting.
- **L2 — Direction:** Parallel light source direction changes.
- **L3 — Specular intensity:** Specular highlight intensity (reflective surfaces).
- **L4 — Shadow casting:** Boolean shadow on/off control.
- Implementation: Modifies MuJoCo scene XML definition files, registers new scene classes.

### 3.6 Background Textures (B1, B2)
- **B1 — Scene texture:** Changes the environment scene texture using 950 curated textures via XML scene files.
- **B2 — Surface texture:** Randomly alters working surface texture (tabletop, floor).
- Implementation: Modifies XML scene definition files with new texture assets.

### 3.7 Sensor Noise (N1-N5)
Applied as image-space post-processing (not physics-level):
- **N1 — Motion blur:** Kernel radius r=5-35, Gaussian sigma=2-20, angle theta in U(-45, 45) degrees.
- **N2 — Gaussian blur:** Sigma from 1 to 10.
- **N3 — Zoom blur:** Scaling factors [s_min, s_max, step] from [1, 1.11, 0.01] to [1, 1.56, 0.03].
- **N4 — Fog:** Density alpha=0.5-5.0, decay rate beta=1.3-3.0.
- **N5 — Glass blur:** Sigma=0.5-2.5, pixel displacement delta=1-5, iterations=1-3.

### Difficulty Levels (L1-L5)
Stratified by how many of 4 reference models (OpenVLA-OFT, pi0, pi0-fast, UniVLA) solve each task:
- L1: All 4 solve it. L2: 3 solve. L3: 2 solve. L4: 1 solves. L5: None solve.

## 4. Installation and Running

### Installation

```bash
# System dependencies
sudo apt install libexpat1 libfontconfig1-dev libmagickwand-dev

# Clone and install
git clone https://github.com/sylvestf/LIBERO-plus.git
cd LIBERO-plus
pip install -e .
pip install -r extra_requirements.txt

# If vanilla LIBERO was installed, uninstall first
pip uninstall -y hf-libero

# Set rendering backend
export MUJOCO_GL=egl
```

### Download assets

Download `assets.zip` from [HuggingFace](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main) and extract to `LIBERO-plus/libero/libero/assets/`.

Expected structure:
```
libero/libero/assets/
├── articulated_objects/
├── new_objects/
├── scenes/
├── stable_hope_objects/
├── stable_scanned_objects/
├── textures/
├── turbosquid_objects/
├── serving_region.xml
├── wall_frames.stl
└── wall.xml
```

### Configuration

Verify config at `/root/.libero/config.yaml`. Key change for evaluation: set `num_trials_per_task: 1` (instead of 50).

Task-to-perturbation-category mappings: `.libero/libero/benchmark/task_classification.json`.

### Evaluation via LeRobot

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero_plus \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```

Observations: `observation.images.image` (agentview), `observation.images.image2` (wrist cam), `observation.state` (8-dim proprioception). Actions: `Box(-1, 1, shape=(7,))` — 6D EEF delta + 1D gripper. Control modes: `relative` (default) or `absolute`.

## 5. Integration with Standard LIBERO Evaluation

LIBERO-Plus is a **drop-in replacement** for vanilla LIBERO:
- Installs under the same `libero` Python package name (replaces it)
- Same `LiberoEnv` gym interface
- Same camera names (`agentview_image`, `robot0_eye_in_hand_image`)
- Same observation/action format
- Same task suite names (`libero_spatial`, `libero_object`, `libero_goal`, `libero_10`, `libero_90`)
- You can swap by doing `pip install -e .` in the LIBERO-plus repo without modifying evaluation code

**You cannot have both vanilla LIBERO and LIBERO-Plus installed simultaneously.** Switching back requires uninstalling the fork and reinstalling vanilla LIBERO.

## 6. LIBERO's Built-in Randomization (via robosuite)

LIBERO is built on **robosuite** (which uses MuJoCo). Robosuite **does** have built-in domain randomization via `DomainRandomizationWrapper` and three visual Modder classes. These are available to any robosuite-based environment, including LIBERO.

### DomainRandomizationWrapper

```python
from robosuite.wrappers import DomainRandomizationWrapper

env = DomainRandomizationWrapper(
    env=base_env,
    seed=42,
    randomize_color=True,        # Geom/texture color randomization
    randomize_camera=True,       # Camera position/orientation/FOV
    randomize_lighting=True,     # Light position/direction/color
    randomize_dynamics=True,     # Physics parameters
    randomize_on_reset=True,     # Randomize at episode reset
    randomize_every_n_steps=1,   # Frequency during rollout
    # Optional: pass detailed config dicts
    color_randomization_args={...},
    camera_randomization_args={...},
    lighting_randomization_args={...},
    dynamics_randomization_args={...},
)
```

### CameraModder (built-in)
- **Position** perturbation: default size 0.01
- **Rotation** perturbation (quaternion): default size 0.087 (~5 degrees)
- **FOV** perturbation: default size 5.0 degrees

### LightingModder (built-in)
- **Position** perturbation: default size 0.1
- **Direction** perturbation: default size 0.35
- **Specular** perturbation: default size 0.1
- **Ambient** perturbation: default size 0.1
- **Diffuse** perturbation: default size 0.1
- **Active** status: on/off toggle

### TextureModder (built-in)
- RGB color randomization (local interpolation 0.1)
- Texture patterns: RGB, checker, noise, gradient
- Material properties: reflectance, shininess, specular (local interpolation 0.2)
- Skybox randomization (optional)
- Note: For full effect, set all material RGBA to [1,1,1,1]

### Demo script
`robosuite/demos/demo_domain_randomization.py` showcases all modders.

## 7. Can LIBERO-Plus Perturbations Be Reused for Training-Time Augmentation?

**Yes, and the paper explicitly does this.** LIBERO-Plus provides both evaluation tasks AND a training dataset:

### What's already provided
- **22,400 training trajectories** (20,000+ after filtering) generated under varied perturbation conditions
- Breakdown: 2,400 with object layout variations + 4,000 each for light/camera/background/language/noise dimensions
- Stored in RLDS format, also available in LeRobot format at `lerobot/libero_plus`
- The paper shows that training with this diverse data ("mix-SFT") improves robustness — the OpenVLA-OFT+ model trained on this data achieves 79.6% average vs. much lower for vanilla-trained models

### Two paths for training-time augmentation

**Path A — Use LIBERO-Plus training data directly:**
```bash
lerobot-train \
    --policy.type=smolvla \
    --dataset.repo_id=lerobot/libero_plus \
    --env.type=libero_plus \
    ...
```

**Path B — Use robosuite's built-in DomainRandomizationWrapper for online augmentation during training:**
This covers camera jitter, lighting changes, texture/color randomization natively. Wrap the LIBERO environment:
```python
from robosuite.wrappers import DomainRandomizationWrapper
env = DomainRandomizationWrapper(env=libero_env, randomize_camera=True, randomize_lighting=True, randomize_color=True)
```

**Path C — Reuse LIBERO-Plus perturbation code for custom augmentation:**
- Lighting/texture perturbations: Modify scene XML files + register new scenes (same approach as LIBERO-Plus)
- Camera perturbations: Modify the `Problem` class interface
- Sensor noise (blur, fog, etc.): Image-space post-processing — trivially reusable as training-time augmentation since it's just image transforms applied after rendering

### Key distinction
- Robosuite's built-in randomization (Path B) is **online** — applies random perturbations every N steps during simulation. Good for training-time augmentation but less controllable.
- LIBERO-Plus perturbations (Path C) are **structured** with specific parameter ranges per sub-dimension and difficulty stratification. More suitable for systematic robustness training.
- Sensor noise (N1-N5) is pure image-space post-processing and can be applied as standard data augmentation on any stored trajectory without re-rendering.

### Paper's finding on augmentation effectiveness
Training strategies emphasizing diversity consistently yield more robust models. Models with wrist camera input show superior generalization. The paper demonstrates that combining perturbation-augmented training data with mix-SFT is the most effective approach.

---

Sources:
- [LIBERO-Plus paper (arXiv)](https://arxiv.org/abs/2510.13626)
- [LIBERO-Plus GitHub](https://github.com/sylvestf/LIBERO-plus)
- [LIBERO-Plus project page](https://sylvestf.github.io/LIBERO-plus/)
- [LIBERO-Plus HuggingFace dataset](https://huggingface.co/datasets/Sylvest/LIBERO-plus)
- [LIBERO-Plus LeRobot docs](https://huggingface.co/docs/lerobot/main/libero_plus)
- [robosuite Sim2Real / Domain Randomization](https://robosuite.ai/docs/algorithms/sim2real.html)
- [robosuite mjmod.py (Modder classes)](https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/utils/mjmod.py)
- [Original LIBERO repo](https://github.com/Lifelong-Robot-Learning/LIBERO)

agentId: aada8a30ff0506204 (use SendMessage with to: 'aada8a30ff0506204' to continue this agent)
&lt;usage>total_tokens: 37597
tool_uses: 20
duration_ms: 182445&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "c0629f71-11c2-4ab5-954b-9f543bc4cb23",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Research LIBERO-Plus, which is a perturbation-based evaluation extension for the LIBERO benchmark in robot manipulation.\n\nI need to find:\n1. What LIBERO-Plus is — what it adds on top of LIBERO\n2. GitHub repo or paper source\n3. The 4 perturbation dimensions: camera perturbation, lighting change, texture swap, sensor noise — exact definitions\n4. Installation and running instructions\n5. How it integrates with standard LIBERO evaluation\n\nAlso research whether LIBERO's simulation environment has built-in randomization options (camera jitter, color/lighting changes, background texture randomization). If it does, how to configure them. If not, whether LIBERO-Plus perturbation implementations can be reused as training-time data augmentation.\n\nUse WebSearch to find papers and repos related to \"LIBERO-Plus\" or \"LIBERO perturbation evaluation\" or \"LIBERO robustness\". Then use WebFetch to read relevant GitHub repos and paper details.\n\nReport everything in structured format with exact commands and code paths where possible.",
    "agentId": "aada8a30ff0506204",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\nHere is the structured research report.\n\n---\n\n## 1. What LIBERO-Plus Is\n\nLIBERO-Plus is a robustness evaluation benchmark that extends the original LIBERO robot manipulation benchmark. It was published as \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\" (arXiv:2510.13626, accepted at CVPR 2026).\n\n**What it adds on top of LIBERO:**\n- **10,030 task variants** generated by applying systematic perturbations to original LIBERO tasks\n- **7 perturbation dimensions** with **21 sub-dimensions**\n- **5 difficulty levels** (L1-L5) stratified by multi-model consensus (how many of 4 reference models solve the task)\n- **20,000+ training trajectories** collected under varied conditions (stored in RLDS format)\n- Drop-in replacement for vanilla LIBERO — same Python interface, same camera names, same observation/action format\n\n## 2. Source\n\n- **Paper:** [arXiv:2510.13626](https://arxiv.org/abs/2510.13626)\n- **GitHub:** [github.com/sylvestf/LIBERO-plus](https://github.com/sylvestf/LIBERO-plus)\n- **Project page:** [sylvestf.github.io/LIBERO-plus](https://sylvestf.github.io/LIBERO-plus/)\n- **Assets (HuggingFace):** [Sylvest/LIBERO-plus](https://huggingface.co/datasets/Sylvest/LIBERO-plus)\n- **Training dataset (RLDS):** [Sylvest/libero_plus_rlds](https://huggingface.co/datasets/Sylvest/libero_plus_rlds)\n- **LeRobot-format dataset:** [lerobot/libero_plus](https://huggingface.co/datasets/lerobot/libero_plus)\n\n## 3. The 7 Perturbation Dimensions (Exact Definitions)\n\nNote: The user asked about 4 dimensions. LIBERO-Plus actually defines **7**, not 4.\n\n### 3.1 Objects Layout (O1, O2)\n- **O1 — Confounding objects:** Adds n additional unseen distractor objects into the scene from a pool of 416 objects, implemented by modifying BDDL task description files.\n- **O2 — Target displacement:** Applies random perturbations to the target object's initial position (x, y, z) and orientation while preserving semantic relationships.\n\n### 3.2 Camera Viewpoints (C1, C2, C3)\n- **C1 — Distance scaling:** Scales camera distance from 1.01x to 2.00x the original value along the optical axis.\n- **C2 — Spherical position:** Changes azimuth (delta-theta) and elevation (delta-phi) within 15 to 75 degree cones.\n- **C3 — Orientation perturbation:** Perturbs yaw, pitch, roll within 2 to 10 degrees.\n\nImplementation: Modifies the `Problem` class interface; parameters derived from task filenames. Targets the third-person camera primarily (not wrist camera).\n\n### 3.3 Robot Initial States\n- Applies random perturbations to the robot arm's initial joint positions with magnitudes 0.1 to 0.5.\n- Implementation: Modifies the `Problem` class interface.\n\n### 3.4 Language Instructions (R1, R2, R3)\n- **R1 — Distraction rewrites:** Adds task-irrelevant contextual information.\n- **R2 — Commonsense substitution:** Replaces object descriptions with commonsense-based alternatives.\n- **R3 — Reasoning complexity:** Alters reasoning complexity for multi-step tasks.\n- Implementation: LLM-based instruction rewriting.\n\n### 3.5 Light Conditions (L1, L2, L3, L4)\n- **L1 — Diffuse color:** RGB channel adjustment of diffuse lighting.\n- **L2 — Direction:** Parallel light source direction changes.\n- **L3 — Specular intensity:** Specular highlight intensity (reflective surfaces).\n- **L4 — Shadow casting:** Boolean shadow on/off control.\n- Implementation: Modifies MuJoCo scene XML definition files, registers new scene classes.\n\n### 3.6 Background Textures (B1, B2)\n- **B1 — Scene texture:** Changes the environment scene texture using 950 curated textures via XML scene files.\n- **B2 — Surface texture:** Randomly alters working surface texture (tabletop, floor).\n- Implementation: Modifies XML scene definition files with new texture assets.\n\n### 3.7 Sensor Noise (N1-N5)\nApplied as image-space post-processing (not physics-level):\n- **N1 — Motion blur:** Kernel radius r=5-35, Gaussian sigma=2-20, angle theta in U(-45, 45) degrees.\n- **N2 — Gaussian blur:** Sigma from 1 to 10.\n- **N3 — Zoom blur:** Scaling factors [s_min, s_max, step] from [1, 1.11, 0.01] to [1, 1.56, 0.03].\n- **N4 — Fog:** Density alpha=0.5-5.0, decay rate beta=1.3-3.0.\n- **N5 — Glass blur:** Sigma=0.5-2.5, pixel displacement delta=1-5, iterations=1-3.\n\n### Difficulty Levels (L1-L5)\nStratified by how many of 4 reference models (OpenVLA-OFT, pi0, pi0-fast, UniVLA) solve each task:\n- L1: All 4 solve it. L2: 3 solve. L3: 2 solve. L4: 1 solves. L5: None solve.\n\n## 4. Installation and Running\n\n### Installation\n\n```bash\n# System dependencies\nsudo apt install libexpat1 libfontconfig1-dev libmagickwand-dev\n\n# Clone and install\ngit clone https://github.com/sylvestf/LIBERO-plus.git\ncd LIBERO-plus\npip install -e .\npip install -r extra_requirements.txt\n\n# If vanilla LIBERO was installed, uninstall first\npip uninstall -y hf-libero\n\n# Set rendering backend\nexport MUJOCO_GL=egl\n```\n\n### Download assets\n\nDownload `assets.zip` from [HuggingFace](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main) and extract to `LIBERO-plus/libero/libero/assets/`.\n\nExpected structure:\n```\nlibero/libero/assets/\n├── articulated_objects/\n├── new_objects/\n├── scenes/\n├── stable_hope_objects/\n├── stable_scanned_objects/\n├── textures/\n├── turbosquid_objects/\n├── serving_region.xml\n├── wall_frames.stl\n└── wall.xml\n```\n\n### Configuration\n\nVerify config at `/root/.libero/config.yaml`. Key change for evaluation: set `num_trials_per_task: 1` (instead of 50).\n\nTask-to-perturbation-category mappings: `.libero/libero/benchmark/task_classification.json`.\n\n### Evaluation via LeRobot\n\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero_plus \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n\nObservations: `observation.images.image` (agentview), `observation.images.image2` (wrist cam), `observation.state` (8-dim proprioception). Actions: `Box(-1, 1, shape=(7,))` — 6D EEF delta + 1D gripper. Control modes: `relative` (default) or `absolute`.\n\n## 5. Integration with Standard LIBERO Evaluation\n\nLIBERO-Plus is a **drop-in replacement** for vanilla LIBERO:\n- Installs under the same `libero` Python package name (replaces it)\n- Same `LiberoEnv` gym interface\n- Same camera names (`agentview_image`, `robot0_eye_in_hand_image`)\n- Same observation/action format\n- Same task suite names (`libero_spatial`, `libero_object`, `libero_goal`, `libero_10`, `libero_90`)\n- You can swap by doing `pip install -e .` in the LIBERO-plus repo without modifying evaluation code\n\n**You cannot have both vanilla LIBERO and LIBERO-Plus installed simultaneously.** Switching back requires uninstalling the fork and reinstalling vanilla LIBERO.\n\n## 6. LIBERO's Built-in Randomization (via robosuite)\n\nLIBERO is built on **robosuite** (which uses MuJoCo). Robosuite **does** have built-in domain randomization via `DomainRandomizationWrapper` and three visual Modder classes. These are available to any robosuite-based environment, including LIBERO.\n\n### DomainRandomizationWrapper\n\n```python\nfrom robosuite.wrappers import DomainRandomizationWrapper\n\nenv = DomainRandomizationWrapper(\n    env=base_env,\n    seed=42,\n    randomize_color=True,        # Geom/texture color randomization\n    randomize_camera=True,       # Camera position/orientation/FOV\n    randomize_lighting=True,     # Light position/direction/color\n    randomize_dynamics=True,     # Physics parameters\n    randomize_on_reset=True,     # Randomize at episode reset\n    randomize_every_n_steps=1,   # Frequency during rollout\n    # Optional: pass detailed config dicts\n    color_randomization_args={...},\n    camera_randomization_args={...},\n    lighting_randomization_args={...},\n    dynamics_randomization_args={...},\n)\n```\n\n### CameraModder (built-in)\n- **Position** perturbation: default size 0.01\n- **Rotation** perturbation (quaternion): default size 0.087 (~5 degrees)\n- **FOV** perturbation: default size 5.0 degrees\n\n### LightingModder (built-in)\n- **Position** perturbation: default size 0.1\n- **Direction** perturbation: default size 0.35\n- **Specular** perturbation: default size 0.1\n- **Ambient** perturbation: default size 0.1\n- **Diffuse** perturbation: default size 0.1\n- **Active** status: on/off toggle\n\n### TextureModder (built-in)\n- RGB color randomization (local interpolation 0.1)\n- Texture patterns: RGB, checker, noise, gradient\n- Material properties: reflectance, shininess, specular (local interpolation 0.2)\n- Skybox randomization (optional)\n- Note: For full effect, set all material RGBA to [1,1,1,1]\n\n### Demo script\n`robosuite/demos/demo_domain_randomization.py` showcases all modders.\n\n## 7. Can LIBERO-Plus Perturbations Be Reused for Training-Time Augmentation?\n\n**Yes, and the paper explicitly does this.** LIBERO-Plus provides both evaluation tasks AND a training dataset:\n\n### What's already provided\n- **22,400 training trajectories** (20,000+ after filtering) generated under varied perturbation conditions\n- Breakdown: 2,400 with object layout variations + 4,000 each for light/camera/background/language/noise dimensions\n- Stored in RLDS format, also available in LeRobot format at `lerobot/libero_plus`\n- The paper shows that training with this diverse data (\"mix-SFT\") improves robustness — the OpenVLA-OFT+ model trained on this data achieves 79.6% average vs. much lower for vanilla-trained models\n\n### Two paths for training-time augmentation\n\n**Path A — Use LIBERO-Plus training data directly:**\n```bash\nlerobot-train \\\n    --policy.type=smolvla \\\n    --dataset.repo_id=lerobot/libero_plus \\\n    --env.type=libero_plus \\\n    ...\n```\n\n**Path B — Use robosuite's built-in DomainRandomizationWrapper for online augmentation during training:**\nThis covers camera jitter, lighting changes, texture/color randomization natively. Wrap the LIBERO environment:\n```python\nfrom robosuite.wrappers import DomainRandomizationWrapper\nenv = DomainRandomizationWrapper(env=libero_env, randomize_camera=True, randomize_lighting=True, randomize_color=True)\n```\n\n**Path C — Reuse LIBERO-Plus perturbation code for custom augmentation:**\n- Lighting/texture perturbations: Modify scene XML files + register new scenes (same approach as LIBERO-Plus)\n- Camera perturbations: Modify the `Problem` class interface\n- Sensor noise (blur, fog, etc.): Image-space post-processing — trivially reusable as training-time augmentation since it's just image transforms applied after rendering\n\n### Key distinction\n- Robosuite's built-in randomization (Path B) is **online** — applies random perturbations every N steps during simulation. Good for training-time augmentation but less controllable.\n- LIBERO-Plus perturbations (Path C) are **structured** with specific parameter ranges per sub-dimension and difficulty stratification. More suitable for systematic robustness training.\n- Sensor noise (N1-N5) is pure image-space post-processing and can be applied as standard data augmentation on any stored trajectory without re-rendering.\n\n### Paper's finding on augmentation effectiveness\nTraining strategies emphasizing diversity consistently yield more robust models. Models with wrist camera input show superior generalization. The paper demonstrates that combining perturbation-augmented training data with mix-SFT is the most effective approach.\n\n---\n\nSources:\n- [LIBERO-Plus paper (arXiv)](https://arxiv.org/abs/2510.13626)\n- [LIBERO-Plus GitHub](https://github.com/sylvestf/LIBERO-plus)\n- [LIBERO-Plus project page](https://sylvestf.github.io/LIBERO-plus/)\n- [LIBERO-Plus HuggingFace dataset](https://huggingface.co/datasets/Sylvest/LIBERO-plus)\n- [LIBERO-Plus LeRobot docs](https://huggingface.co/docs/lerobot/main/libero_plus)\n- [robosuite Sim2Real / Domain Randomization](https://robosuite.ai/docs/algorithms/sim2real.html)\n- [robosuite mjmod.py (Modder classes)](https://github.com/ARISE-Initiative/robosuite/blob/master/robosuite/utils/mjmod.py)\n- [Original LIBERO repo](https://github.com/Lifelong-Robot-Learning/LIBERO)"
      }
    ],
    "totalDurationMs": 182445,
    "totalTokens": 37597,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 379,
      "cache_read_input_tokens": 33443,
      "output_tokens": 3772,
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
          "output_tokens": 3772,
          "cache_read_input_tokens": 33443,
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
      "otherToolCount": 20
    }
  }
}
````

</details>

---

### System

_source line 237_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a708484d135d02b9a",
  "tool_use_id": "toolu_01HzxqFJcSQ9LxVeV3zrEHSz",
  "status": "completed",
  "output_file": "",
  "summary": "Research LIBERO Benchmark",
  "usage": {
    "total_tokens": 40448,
    "tool_uses": 35,
    "duration_ms": 222708
  },
  "uuid": "4e68acd6-ef78-488b-b65b-4e5682c9ac67",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b"
}
```

---

### Tool result

_source line 238 · 2026-05-15T11:15:32.422Z_

<details><summary>↩ Tool result · `toolu_01HzxqFJcSQ9LxVeV3zrEHSz`</summary>

````text
Now I have comprehensive information. Let me compile the final report.

---

## LIBERO Benchmark: Comprehensive Technical Reference

### 1. GitHub Repo URL

**Official:** https://github.com/Lifelong-Robot-Learning/LIBERO

**Paper:** [arXiv:2306.03310](https://arxiv.org/abs/2306.03310) (NeurIPS 2023 Datasets & Benchmarks)

**Project website:** https://libero-project.github.io

**HuggingFace fork (LeRobot integration):** https://github.com/huggingface/lerobot-libero

---

### 2. Installation

**Method A: pip (simplest)**
```bash
pip install libero
```
Current version: 0.1.1. Requires Python >= 3.

**Method B: From source (recommended for development)**
```bash
conda create -n libero python=3.8.13
conda activate libero
git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git
cd LIBERO
pip install -r requirements.txt
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
pip install -e .
```

**Method C: Via LeRobot**
```bash
pip install -e ".[libero]"
```

Underlying simulator: **robosuite** (MuJoCo-based). For headless rendering: `export MUJOCO_GL=egl`.

Licenses: MIT (code), CC BY 4.0 (datasets).

---

### 3. The 5 Task Suites

All tasks are language-conditioned manipulation with a Franka Panda arm.

| Suite | CLI name | Tasks | Description |
|-------|----------|-------|-------------|
| **LIBERO-Spatial** | `libero_spatial` | 10 | Same goal (pick black bowl, place on plate) but bowl is in different spatial locations. Tests transfer of **spatial relationship knowledge**. |
| **LIBERO-Object** | `libero_object` | 10 | Same goal structure (pick X, place in basket) but with different objects (soup, cream cheese, ketchup, etc.). Tests transfer of **object knowledge**. |
| **LIBERO-Goal** | `libero_goal` | 10 | Same scene but different goals (open drawer, put bowl on stove, turn on stove, etc.). Tests transfer of **goal/procedural knowledge**. |
| **LIBERO-90** | `libero_90` | 90 | Short-horizon tasks from LIBERO-100. Entangled distribution shifts across spatial, object, and goal axes. Used for pretraining. |
| **LIBERO-Long** | `libero_10` | 10 | Long-horizon multi-step tasks from LIBERO-100. Used for downstream evaluation after pretraining on LIBERO-90. |

**LIBERO-Spatial example tasks** (all 10):
1. pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate
2. pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate
3. pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate
4. pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate
5. pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate
6. pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate
7. pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate
8. pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate
9. pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate
10. pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate

**LIBERO-Object example tasks**: pick_up_the_{alphabet_soup, cream_cheese, salad_dressing, bbq_sauce, ketchup, tomato_sauce, butter, milk, chocolate_pudding, orange_juice}_and_place_it_in_the_basket

**LIBERO-Goal example tasks**: open_the_middle_drawer_of_the_cabinet, put_the_bowl_on_the_stove, put_the_wine_bottle_on_top_of_the_cabinet, open_the_top_drawer_and_put_the_bowl_inside, put_the_bowl_on_top_of_the_cabinet, push_the_plate_to_the_front_of_the_stove, put_the_cream_cheese_in_the_bowl, turn_on_the_stove, put_the_bowl_on_the_plate, put_the_wine_bottle_on_the_rack

---

### 4. Data Download

**50 human teleoperation demonstrations per task**, collected via SpaceMouse at 20 Hz.

**Method A: Official script**
```bash
# All datasets
python benchmark_scripts/download_libero_datasets.py

# Specific suite
python benchmark_scripts/download_libero_datasets.py --datasets libero_spatial
python benchmark_scripts/download_libero_datasets.py --datasets libero_object
python benchmark_scripts/download_libero_datasets.py --datasets libero_goal
python benchmark_scripts/download_libero_datasets.py --datasets libero_100  # contains both libero_90 and libero_10

# Via HuggingFace (recommended, original links may expire)
python benchmark_scripts/download_libero_datasets.py --use-huggingface
```
Default download location: `./datasets/` under the LIBERO root.

**Method B: HuggingFace direct**

Multiple HF dataset repos exist:
- Original HDF5: https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets (~100 GB total)
- Physical Intelligence (LeRobot format): https://huggingface.co/datasets/physical-intelligence/libero (~34.9 GB, 4 suites, parquet)
- HuggingFace VLA (LeRobot format): https://huggingface.co/datasets/HuggingFaceVLA/libero

**Approximate sizes (original HDF5 format):**

| Suite | Approx Size |
|-------|-------------|
| libero_spatial | ~6.6 GB |
| libero_object | ~9.3 GB |
| libero_goal | ~6-9 GB |
| libero_10 (Long) | ~12.8 GB |
| libero_90 | ~60-70 GB |
| **Total** | **~100 GB** |

---

### 5. Data Format

**File format:** HDF5 (one `.hdf5` file per task)

**HDF5 structure:**
```
data/
  demo_0/
    obs/
      agentview_rgb          # (T, 128, 128, 3) uint8 — third-person camera
      eye_in_hand_rgb        # (T, 128, 128, 3) uint8 — wrist camera
      gripper_states         # (T, 1) — gripper aperture (from robot0_gripper_qpos)
      joint_states           # (T, 7) — 7 joint positions (from robot0_joint_pos)
      ee_states              # (T, 6) — end-effector position + axis-angle orientation
      ee_pos                 # (T, 3) — end-effector position
      ee_ori                 # (T, 3) — end-effector axis-angle orientation
    actions                  # (T, 7) — 7-DOF action
    states                   # (T, D) — full simulator state
    robot_states             # (T, D) — concatenation of gripper_pos, ee_pos, ee_quat
    rewards                  # (T,) — sparse: 0 everywhere, 1 at final success step
    dones                    # (T,) — 1 at episode end
  demo_1/
    ...
  demo_49/
    ...
```

**Observation space (used in default config):**

| Key | Dimension | Meaning |
|-----|-----------|---------|
| `agentview_rgb` (maps to `agentview_image`) | (128, 128, 3) | RGB from workspace camera |
| `eye_in_hand_rgb` (maps to `robot0_eye_in_hand_image`) | (128, 128, 3) | RGB from wrist-mounted camera |
| `gripper_states` (maps to `robot0_gripper_qpos`) | (1,) or (2,) | Gripper finger position(s) |
| `joint_states` (maps to `robot0_joint_pos`) | (7,) | 7 joint angles of the Franka Panda |
| `ee_pos` | (3,) | End-effector xyz position |
| `ee_ori` | (3,) | End-effector axis-angle orientation |

**In LeRobot format**, the proprioceptive state is an 8-dimensional vector: `observation.state` = [ee_pos (3) + ee_axis_angle (3) + gripper_qpos (2)] or [ee_pos (3) + ee_axis_angle (3) + gripper_qpos (1) + padding (1)].

**Action space:**

| Dimension | Meaning |
|-----------|---------|
| 0-2 | End-effector position delta (dx, dy, dz) |
| 3-5 | End-effector orientation delta (axis-angle or Euler) |
| 6 | Gripper command (1 = close, -1 = open) |

Total: **7-dimensional continuous**, Box(-1, 1, shape=(7,)). Control mode: **OSC_POSE** (Operational Space Control). Frequency: **20 Hz**. Supports both `relative` (delta, default) and `absolute` control modes.

**Reward:** Sparse — 0 for all intermediate steps, +1 only upon successful task completion.

**Default config values (from `libero/configs/data/default.yaml`):**
- Image resolution: 128x128
- Sequence length: 10
- Frame stacking: 1
- Obs modalities: `rgb` = [agentview_rgb, eye_in_hand_rgb], `low_dim` = [gripper_states, joint_states]
- Train ratio: 0.8

---

### 6. Evaluation

**Native LIBERO evaluation:**

```bash
python libero/lifelong/evaluate.py \
  --benchmark LIBERO_SPATIAL \
  --task_id 0 \
  --algo base \
  --policy bc_transformer_policy \
  --seed 10000 \
  --ep 50 \
  --load_task 0 \
  --device_id 0
```

Arguments:
- `--benchmark`: One of `LIBERO_SPATIAL`, `LIBERO_OBJECT`, `LIBERO_GOAL`, `LIBERO_90`, `LIBERO_10`
- `--task_id`: Task index within the suite
- `--algo`: Lifelong learning algorithm (`base`, `er`, `ewc`, `packnet`, `multitask`)
- `--policy`: Policy architecture (`bc_rnn_policy`, `bc_transformer_policy`, `bc_vilt_policy`)
- `--seed`: Random seed
- `--ep`: Epoch checkpoint to load (for multitask)
- `--load_task`: Which task's checkpoint to load
- `--device_id`: GPU ID
- `--save-videos`: Optional flag to record evaluation videos

**Evaluation protocol:**
- 20 parallel environments run simultaneously (`n_eval: 20`, `num_procs: 20`)
- Max 600 steps per episode (`max_steps: 600`)
- 5 initial zero-action steps for physics settling
- Episode terminates when `done` flag is set or max steps reached

**Output metrics:**
- **Success rate** = num_success / num_envs (per task)
- **Loss** = test set loss
- Saved to: `{save_dir}/{benchmark}_{algo}_{policy}_{seed}_[ep|load]_{task_id}.stats` (PyTorch tensor dict)

**Lifelong learning metrics (across task sequences):**
- **FWT (Forward Transfer)**: Success rate on new tasks after sequential training
- **NBT (Negative Backward Transfer)**: Performance degradation on earlier tasks (catastrophic forgetting)
- **AUC (Area Under Curve)**: Cumulative success rate integrating both FWT and NBT over the task sequence

**Native training command:**
```bash
export CUDA_VISIBLE_DEVICES=0 && \
export MUJOCO_EGL_DEVICE_ID=0 && \
python libero/lifelong/main.py seed=10000 \
  benchmark_name=LIBERO_SPATIAL \
  policy=bc_transformer_policy \
  lifelong=base
```

**LeRobot evaluation (alternative):**
```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```
Standard protocol: 10 episodes per task across all 4 standard suites = 400 total episodes.

agentId: a708484d135d02b9a (use SendMessage with to: 'a708484d135d02b9a' to continue this agent)
&lt;usage>total_tokens: 42739
tool_uses: 35
duration_ms: 222710&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "83653f9d-75ae-462b-84df-4b644c391c7e",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Research the LIBERO Benchmark for robot manipulation. I need detailed information about:\n\n1. GitHub repo URL\n2. Installation method (pip or from source)\n3. The 5 task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90 — what each contains\n4. Data download method and size for each suite\n5. Data format: observation space dimensions/meaning, action space dimensions/meaning\n6. Evaluation scripts: how to run evaluation, what metrics are output\n\nUse WebSearch to find the LIBERO benchmark paper and GitHub repo. Then use WebFetch to read the GitHub README, installation docs, and key source files to get specific details about data format, task suites, and evaluation.\n\nBe thorough — I need exact commands, file paths, and API details. Report everything you find in a structured format.",
    "agentId": "a708484d135d02b9a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the final report.\n\n---\n\n## LIBERO Benchmark: Comprehensive Technical Reference\n\n### 1. GitHub Repo URL\n\n**Official:** https://github.com/Lifelong-Robot-Learning/LIBERO\n\n**Paper:** [arXiv:2306.03310](https://arxiv.org/abs/2306.03310) (NeurIPS 2023 Datasets & Benchmarks)\n\n**Project website:** https://libero-project.github.io\n\n**HuggingFace fork (LeRobot integration):** https://github.com/huggingface/lerobot-libero\n\n---\n\n### 2. Installation\n\n**Method A: pip (simplest)**\n```bash\npip install libero\n```\nCurrent version: 0.1.1. Requires Python >= 3.\n\n**Method B: From source (recommended for development)**\n```bash\nconda create -n libero python=3.8.13\nconda activate libero\ngit clone https://github.com/Lifelong-Robot-Learning/LIBERO.git\ncd LIBERO\npip install -r requirements.txt\npip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113\npip install -e .\n```\n\n**Method C: Via LeRobot**\n```bash\npip install -e \".[libero]\"\n```\n\nUnderlying simulator: **robosuite** (MuJoCo-based). For headless rendering: `export MUJOCO_GL=egl`.\n\nLicenses: MIT (code), CC BY 4.0 (datasets).\n\n---\n\n### 3. The 5 Task Suites\n\nAll tasks are language-conditioned manipulation with a Franka Panda arm.\n\n| Suite | CLI name | Tasks | Description |\n|-------|----------|-------|-------------|\n| **LIBERO-Spatial** | `libero_spatial` | 10 | Same goal (pick black bowl, place on plate) but bowl is in different spatial locations. Tests transfer of **spatial relationship knowledge**. |\n| **LIBERO-Object** | `libero_object` | 10 | Same goal structure (pick X, place in basket) but with different objects (soup, cream cheese, ketchup, etc.). Tests transfer of **object knowledge**. |\n| **LIBERO-Goal** | `libero_goal` | 10 | Same scene but different goals (open drawer, put bowl on stove, turn on stove, etc.). Tests transfer of **goal/procedural knowledge**. |\n| **LIBERO-90** | `libero_90` | 90 | Short-horizon tasks from LIBERO-100. Entangled distribution shifts across spatial, object, and goal axes. Used for pretraining. |\n| **LIBERO-Long** | `libero_10` | 10 | Long-horizon multi-step tasks from LIBERO-100. Used for downstream evaluation after pretraining on LIBERO-90. |\n\n**LIBERO-Spatial example tasks** (all 10):\n1. pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\n2. pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\n3. pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\n4. pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\n5. pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\n6. pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\n7. pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\n8. pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\n9. pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\n10. pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\n\n**LIBERO-Object example tasks**: pick_up_the_{alphabet_soup, cream_cheese, salad_dressing, bbq_sauce, ketchup, tomato_sauce, butter, milk, chocolate_pudding, orange_juice}_and_place_it_in_the_basket\n\n**LIBERO-Goal example tasks**: open_the_middle_drawer_of_the_cabinet, put_the_bowl_on_the_stove, put_the_wine_bottle_on_top_of_the_cabinet, open_the_top_drawer_and_put_the_bowl_inside, put_the_bowl_on_top_of_the_cabinet, push_the_plate_to_the_front_of_the_stove, put_the_cream_cheese_in_the_bowl, turn_on_the_stove, put_the_bowl_on_the_plate, put_the_wine_bottle_on_the_rack\n\n---\n\n### 4. Data Download\n\n**50 human teleoperation demonstrations per task**, collected via SpaceMouse at 20 Hz.\n\n**Method A: Official script**\n```bash\n# All datasets\npython benchmark_scripts/download_libero_datasets.py\n\n# Specific suite\npython benchmark_scripts/download_libero_datasets.py --datasets libero_spatial\npython benchmark_scripts/download_libero_datasets.py --datasets libero_object\npython benchmark_scripts/download_libero_datasets.py --datasets libero_goal\npython benchmark_scripts/download_libero_datasets.py --datasets libero_100  # contains both libero_90 and libero_10\n\n# Via HuggingFace (recommended, original links may expire)\npython benchmark_scripts/download_libero_datasets.py --use-huggingface\n```\nDefault download location: `./datasets/` under the LIBERO root.\n\n**Method B: HuggingFace direct**\n\nMultiple HF dataset repos exist:\n- Original HDF5: https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets (~100 GB total)\n- Physical Intelligence (LeRobot format): https://huggingface.co/datasets/physical-intelligence/libero (~34.9 GB, 4 suites, parquet)\n- HuggingFace VLA (LeRobot format): https://huggingface.co/datasets/HuggingFaceVLA/libero\n\n**Approximate sizes (original HDF5 format):**\n\n| Suite | Approx Size |\n|-------|-------------|\n| libero_spatial | ~6.6 GB |\n| libero_object | ~9.3 GB |\n| libero_goal | ~6-9 GB |\n| libero_10 (Long) | ~12.8 GB |\n| libero_90 | ~60-70 GB |\n| **Total** | **~100 GB** |\n\n---\n\n### 5. Data Format\n\n**File format:** HDF5 (one `.hdf5` file per task)\n\n**HDF5 structure:**\n```\ndata/\n  demo_0/\n    obs/\n      agentview_rgb          # (T, 128, 128, 3) uint8 — third-person camera\n      eye_in_hand_rgb        # (T, 128, 128, 3) uint8 — wrist camera\n      gripper_states         # (T, 1) — gripper aperture (from robot0_gripper_qpos)\n      joint_states           # (T, 7) — 7 joint positions (from robot0_joint_pos)\n      ee_states              # (T, 6) — end-effector position + axis-angle orientation\n      ee_pos                 # (T, 3) — end-effector position\n      ee_ori                 # (T, 3) — end-effector axis-angle orientation\n    actions                  # (T, 7) — 7-DOF action\n    states                   # (T, D) — full simulator state\n    robot_states             # (T, D) — concatenation of gripper_pos, ee_pos, ee_quat\n    rewards                  # (T,) — sparse: 0 everywhere, 1 at final success step\n    dones                    # (T,) — 1 at episode end\n  demo_1/\n    ...\n  demo_49/\n    ...\n```\n\n**Observation space (used in default config):**\n\n| Key | Dimension | Meaning |\n|-----|-----------|---------|\n| `agentview_rgb` (maps to `agentview_image`) | (128, 128, 3) | RGB from workspace camera |\n| `eye_in_hand_rgb` (maps to `robot0_eye_in_hand_image`) | (128, 128, 3) | RGB from wrist-mounted camera |\n| `gripper_states` (maps to `robot0_gripper_qpos`) | (1,) or (2,) | Gripper finger position(s) |\n| `joint_states` (maps to `robot0_joint_pos`) | (7,) | 7 joint angles of the Franka Panda |\n| `ee_pos` | (3,) | End-effector xyz position |\n| `ee_ori` | (3,) | End-effector axis-angle orientation |\n\n**In LeRobot format**, the proprioceptive state is an 8-dimensional vector: `observation.state` = [ee_pos (3) + ee_axis_angle (3) + gripper_qpos (2)] or [ee_pos (3) + ee_axis_angle (3) + gripper_qpos (1) + padding (1)].\n\n**Action space:**\n\n| Dimension | Meaning |\n|-----------|---------|\n| 0-2 | End-effector position delta (dx, dy, dz) |\n| 3-5 | End-effector orientation delta (axis-angle or Euler) |\n| 6 | Gripper command (1 = close, -1 = open) |\n\nTotal: **7-dimensional continuous**, Box(-1, 1, shape=(7,)). Control mode: **OSC_POSE** (Operational Space Control). Frequency: **20 Hz**. Supports both `relative` (delta, default) and `absolute` control modes.\n\n**Reward:** Sparse — 0 for all intermediate steps, +1 only upon successful task completion.\n\n**Default config values (from `libero/configs/data/default.yaml`):**\n- Image resolution: 128x128\n- Sequence length: 10\n- Frame stacking: 1\n- Obs modalities: `rgb` = [agentview_rgb, eye_in_hand_rgb], `low_dim` = [gripper_states, joint_states]\n- Train ratio: 0.8\n\n---\n\n### 6. Evaluation\n\n**Native LIBERO evaluation:**\n\n```bash\npython libero/lifelong/evaluate.py \\\n  --benchmark LIBERO_SPATIAL \\\n  --task_id 0 \\\n  --algo base \\\n  --policy bc_transformer_policy \\\n  --seed 10000 \\\n  --ep 50 \\\n  --load_task 0 \\\n  --device_id 0\n```\n\nArguments:\n- `--benchmark`: One of `LIBERO_SPATIAL`, `LIBERO_OBJECT`, `LIBERO_GOAL`, `LIBERO_90`, `LIBERO_10`\n- `--task_id`: Task index within the suite\n- `--algo`: Lifelong learning algorithm (`base`, `er`, `ewc`, `packnet`, `multitask`)\n- `--policy`: Policy architecture (`bc_rnn_policy`, `bc_transformer_policy`, `bc_vilt_policy`)\n- `--seed`: Random seed\n- `--ep`: Epoch checkpoint to load (for multitask)\n- `--load_task`: Which task's checkpoint to load\n- `--device_id`: GPU ID\n- `--save-videos`: Optional flag to record evaluation videos\n\n**Evaluation protocol:**\n- 20 parallel environments run simultaneously (`n_eval: 20`, `num_procs: 20`)\n- Max 600 steps per episode (`max_steps: 600`)\n- 5 initial zero-action steps for physics settling\n- Episode terminates when `done` flag is set or max steps reached\n\n**Output metrics:**\n- **Success rate** = num_success / num_envs (per task)\n- **Loss** = test set loss\n- Saved to: `{save_dir}/{benchmark}_{algo}_{policy}_{seed}_[ep|load]_{task_id}.stats` (PyTorch tensor dict)\n\n**Lifelong learning metrics (across task sequences):**\n- **FWT (Forward Transfer)**: Success rate on new tasks after sequential training\n- **NBT (Negative Backward Transfer)**: Performance degradation on earlier tasks (catastrophic forgetting)\n- **AUC (Area Under Curve)**: Cumulative success rate integrating both FWT and NBT over the task sequence\n\n**Native training command:**\n```bash\nexport CUDA_VISIBLE_DEVICES=0 && \\\nexport MUJOCO_EGL_DEVICE_ID=0 && \\\npython libero/lifelong/main.py seed=10000 \\\n  benchmark_name=LIBERO_SPATIAL \\\n  policy=bc_transformer_policy \\\n  lifelong=base\n```\n\n**LeRobot evaluation (alternative):**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\nStandard protocol: 10 episodes per task across all 4 standard suites = 400 total episodes."
      }
    ],
    "totalDurationMs": 222710,
    "totalTokens": 42739,
    "totalToolUseCount": 35,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1841,
      "cache_read_input_tokens": 37394,
      "output_tokens": 3503,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1841
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3503,
          "cache_read_input_tokens": 37394,
          "cache_creation_input_tokens": 1841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1841,
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
````

</details>

---

### Assistant

_source line 239_

<details><summary>Logged reasoning block</summary>

```text
All three agents have returned comprehensive results. Let me now compile the final report and write it to the specified path.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "c825ea6f-1f9b-4187-a019-f45bebdfeb73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AsqznMtCNdspEULyo6rq5X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6565,
      "cache_creation_input_tokens": 4550,
      "cache_read_input_tokens": 23122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4550
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 240_

All three research agents returned comprehensive results. Writing the consolidated report now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "711cd119-d50d-43a2-8b50-75047f4e60c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AsqznMtCNdspEULyo6rq5X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6565,
      "cache_creation_input_tokens": 4550,
      "cache_read_input_tokens": 23122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4550
      },
      "output_tokens": 8,
      "service_tier": "standard",
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

_source line 241_

<details open><summary>🔧 Tool call — Bash · `toolu_0166WiuqUw5L1GnHyjYMaFfA`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/",
  "description": "Check artifacts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "f4ff6798-33e8-489f-b5e2-9488c45dde3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AsqznMtCNdspEULyo6rq5X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6565,
      "cache_creation_input_tokens": 4550,
      "cache_read_input_tokens": 23122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4550
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 242 · 2026-05-15T11:15:37.351Z_

<details><summary>↩ Tool result · reported error · `toolu_0166WiuqUw5L1GnHyjYMaFfA`</summary>

```text
Exit code 2
ls: cannot access '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/': No such file or directory
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "ccc677fe-5d3a-4a42-9992-a51e7463583b",
  "tool_use_result": "Error: Exit code 2\nls: cannot access '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/': No such file or directory"
}
```

</details>

---

### Tool call

_source line 243_

<details open><summary>🔧 Tool call — Bash · `toolu_018fwoX7PoXe5FVZxaNi1GLq`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts",
  "description": "Create artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "1eeddd23-8a98-40bd-8566-49a86b5ef94f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013rbdCPs5FHi7yuTRLTCwDK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6798,
      "cache_read_input_tokens": 27672,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6798
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 244 · 2026-05-15T11:15:39.455Z_

<details><summary>↩ Tool result · `toolu_018fwoX7PoXe5FVZxaNi1GLq`</summary>

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
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "8c6877a9-6401-4fd8-b850-340cdb0f7244",
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

_source line 245_

<details open><summary>🔧 Tool call — Write · `toolu_01LrSHXmQBaHspBqcmLQUt3W`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/research_libero_benchmark.md",
  "content": "# LIBERO Benchmark + LIBERO-Plus 调研报告\n\n调研日期：2026-05-15\n\n---\n\n## 1. LIBERO Benchmark\n\n### 1.1 基本信息\n\n| 项目 | 内容 |\n|------|------|\n| 论文 | [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310) (NeurIPS 2023 D&B) |\n| GitHub | https://github.com/Lifelong-Robot-Learning/LIBERO |\n| 项目主页 | https://libero-project.github.io |\n| License | MIT (代码), CC BY 4.0 (数据集) |\n| 模拟器 | robosuite (MuJoCo) |\n| 机器人 | Franka Panda 7-DOF |\n\n### 1.2 安装\n\n**方式 A：pip**\n```bash\npip install libero\n```\n\n**方式 B：from source（推荐）**\n```bash\nconda create -n libero python=3.8.13\nconda activate libero\ngit clone https://github.com/Lifelong-Robot-Learning/LIBERO.git\ncd LIBERO\npip install -r requirements.txt\npip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113\npip install -e .\n```\n\n**方式 C：通过 LeRobot**\n```bash\npip install -e \".[libero]\"\n```\n\n无头渲染需设置：`export MUJOCO_GL=egl`\n\n### 1.3 五个 Task Suite\n\n所有任务都是 language-conditioned manipulation，使用 Franka Panda 机械臂。\n\n| Suite | CLI 名称 | 任务数 | 描述 |\n|-------|----------|--------|------|\n| **LIBERO-Spatial** | `libero_spatial` | 10 | 同一目标（拿黑碗放盘子），碗在不同空间位置。测试 **空间关系知识** 迁移 |\n| **LIBERO-Object** | `libero_object` | 10 | 同一目标结构（拿 X 放篮子），不同物体。测试 **物体知识** 迁移 |\n| **LIBERO-Goal** | `libero_goal` | 10 | 同一场景，不同目标（开抽屉、放碗到炉子上等）。测试 **目标/程序知识** 迁移 |\n| **LIBERO-90** | `libero_90` | 90 | LIBERO-100 中的短期任务，跨 spatial/object/goal 的混合分布偏移。用于 **预训练** |\n| **LIBERO-Long** | `libero_10` | 10 | LIBERO-100 中的长期多步骤任务。用于预训练后的 **下游评测** |\n\n**LIBERO-Spatial 示例任务（全部 10 个）：**\n1. pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\n2. pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\n3. pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\n4. pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\n5. pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\n6. pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\n7. pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\n8. pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\n9. pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\n10. pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\n\n**LIBERO-Object 示例任务：** pick_up_the_{alphabet_soup, cream_cheese, salad_dressing, bbq_sauce, ketchup, tomato_sauce, butter, milk, chocolate_pudding, orange_juice}_and_place_it_in_the_basket\n\n**LIBERO-Goal 示例任务：** open_the_middle_drawer_of_the_cabinet, put_the_bowl_on_the_stove, put_the_wine_bottle_on_top_of_the_cabinet, open_the_top_drawer_and_put_the_bowl_inside, put_the_bowl_on_top_of_the_cabinet, push_the_plate_to_the_front_of_the_stove, put_the_cream_cheese_in_the_bowl, turn_on_the_stove, put_the_bowl_on_the_plate, put_the_wine_bottle_on_the_rack\n\n### 1.4 数据下载\n\n每个任务有 **50 条人类遥操作演示**，通过 SpaceMouse 以 20 Hz 采集。\n\n**方式 A：官方脚本**\n```bash\n# 全部下载\npython benchmark_scripts/download_libero_datasets.py\n\n# 下载特定 suite\npython benchmark_scripts/download_libero_datasets.py --datasets libero_spatial\npython benchmark_scripts/download_libero_datasets.py --datasets libero_object\npython benchmark_scripts/download_libero_datasets.py --datasets libero_goal\npython benchmark_scripts/download_libero_datasets.py --datasets libero_100  # 含 libero_90 + libero_10\n\n# 通过 HuggingFace 下载（推荐，原始链接可能过期）\npython benchmark_scripts/download_libero_datasets.py --use-huggingface\n```\n\n默认下载位置：LIBERO 根目录下的 `./datasets/`\n\n**方式 B：HuggingFace 直接下载**\n\n| 数据集 | 格式 | 大小 |\n|--------|------|------|\n| `yifengzhu-hf/LIBERO-datasets` | 原始 HDF5 | ~100 GB 总计 |\n| `physical-intelligence/libero` | LeRobot (Parquet) | ~34.9 GB |\n| `HuggingFaceVLA/libero` | LeRobot | ~1.9 GB |\n| `lerobot/libero` | LeRobot (视频 AV1) | ~1.94 GB |\n\n**各 suite 近似大小（原始 HDF5 格式）：**\n\n| Suite | 大小 |\n|-------|------|\n| libero_spatial | ~6.6 GB |\n| libero_object | ~9.3 GB |\n| libero_goal | ~6-9 GB |\n| libero_10 (Long) | ~12.8 GB |\n| libero_90 | ~60-70 GB |\n| **总计** | **~100 GB** |\n\n### 1.5 数据格式\n\n**文件格式：** HDF5（每个任务一个 `.hdf5` 文件）\n\n**HDF5 结构：**\n```\ndata/\n  demo_0/\n    obs/\n      agentview_rgb          # (T, 128, 128, 3) uint8 — 第三人称相机\n      eye_in_hand_rgb        # (T, 128, 128, 3) uint8 — 腕部相机\n      gripper_states         # (T, 1) — 夹爪开合度\n      joint_states           # (T, 7) — 7 个关节角度\n      ee_states              # (T, 6) — 末端执行器位置 + 轴角朝向\n      ee_pos                 # (T, 3) — 末端执行器 xyz 位置\n      ee_ori                 # (T, 3) — 末端执行器轴角朝向\n    actions                  # (T, 7) — 7-DOF 动作\n    states                   # (T, D) — 完整模拟器状态\n    robot_states             # (T, D) — gripper_pos + ee_pos + ee_quat 拼接\n    rewards                  # (T,) — 稀疏: 全 0，最后成功步为 1\n    dones                    # (T,) — episode 结束时为 1\n  demo_1/ ...\n  demo_49/ ...\n```\n\n**观测空间：**\n\n| 键 | 维度 | 含义 |\n|----|------|------|\n| `agentview_rgb` (→ `agentview_image`) | (128, 128, 3) | 工作区 RGB 图像 |\n| `eye_in_hand_rgb` (→ `robot0_eye_in_hand_image`) | (128, 128, 3) | 腕部 RGB 图像 |\n| `gripper_states` (→ `robot0_gripper_qpos`) | (1,) 或 (2,) | 夹爪指位置 |\n| `joint_states` (→ `robot0_joint_pos`) | (7,) | Franka Panda 7 关节角 |\n| `ee_pos` | (3,) | 末端执行器 xyz 位置 |\n| `ee_ori` | (3,) | 末端执行器轴角朝向 |\n\n**LeRobot 格式中** proprioceptive state 为 8 维：`observation.state` = [ee_pos (3) + ee_axis_angle (3) + gripper_qpos (2)]\n\n**动作空间：**\n\n| 维度 | 含义 |\n|------|------|\n| 0-2 | 末端执行器位置增量 (dx, dy, dz) |\n| 3-5 | 末端执行器朝向增量 (轴角 / 欧拉角) |\n| 6 | 夹爪命令 (1=闭合, -1=打开) |\n\n- 总计 **7 维连续动作**，Box(-1, 1, shape=(7,))\n- 控制模式：**OSC_POSE**（操作空间控制）\n- 频率：**20 Hz**（原始），LeRobot 格式 **10 Hz**\n- 支持 `relative`（增量，默认）和 `absolute` 两种控制模式\n- 奖励：稀疏 — 中间步全 0，任务完成时 +1\n\n### 1.6 评测\n\n**原生 LIBERO 评测：**\n\n```bash\npython libero/lifelong/evaluate.py \\\n  --benchmark LIBERO_SPATIAL \\\n  --task_id 0 \\\n  --algo base \\\n  --policy bc_transformer_policy \\\n  --seed 10000 \\\n  --ep 50 \\\n  --load_task 0 \\\n  --device_id 0\n```\n\n参数说明：\n- `--benchmark`: `LIBERO_SPATIAL` / `LIBERO_OBJECT` / `LIBERO_GOAL` / `LIBERO_90` / `LIBERO_10`\n- `--task_id`: suite 内的任务索引\n- `--algo`: 终身学习算法 (`base`, `er`, `ewc`, `packnet`, `multitask`)\n- `--policy`: 策略架构 (`bc_rnn_policy`, `bc_transformer_policy`, `bc_vilt_policy`)\n- `--save-videos`: 可选，录制评测视频\n\n**评测协议：**\n- 20 个并行环境同时运行 (`n_eval: 20`, `num_procs: 20`)\n- 每个 episode 最多 600 步 (`max_steps: 600`)\n- 开头 5 步零动作用于物理稳定\n- episode 在 `done=True` 或达到最大步数时终止\n\n**输出指标：**\n- **Success rate** = num_success / num_envs（每个任务）\n- **Loss** = 测试集损失\n- 结果保存路径：`{save_dir}/{benchmark}_{algo}_{policy}_{seed}_[ep|load]_{task_id}.stats`\n\n**终身学习指标（跨任务序列）：**\n- **FWT (Forward Transfer)**: 序列训练后在新任务上的成功率\n- **NBT (Negative Backward Transfer)**: 早期任务性能退化（灾难性遗忘）\n- **AUC (Area Under Curve)**: 综合 FWT 和 NBT 的累积成功率\n\n**原生训练命令：**\n```bash\nexport CUDA_VISIBLE_DEVICES=0 && \\\nexport MUJOCO_EGL_DEVICE_ID=0 && \\\npython libero/lifelong/main.py seed=10000 \\\n  benchmark_name=LIBERO_SPATIAL \\\n  policy=bc_transformer_policy \\\n  lifelong=base\n```\n\n**LeRobot 评测：**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n标准协议：每个任务 10 个 episode，4 个标准 suite = 400 个 episode。\n\n---\n\n## 2. LIBERO-Plus 扰动评测\n\n### 2.1 基本信息\n\n| 项目 | 内容 |\n|------|------|\n| 论文 | [LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626) (CVPR 2026) |\n| GitHub | https://github.com/sylvestf/LIBERO-plus |\n| 项目主页 | https://sylvestf.github.io/LIBERO-plus/ |\n| HF 资产 | https://huggingface.co/datasets/Sylvest/LIBERO-plus |\n| 训练数据 (RLDS) | https://huggingface.co/datasets/Sylvest/libero_plus_rlds |\n| LeRobot 格式 | https://huggingface.co/datasets/lerobot/libero_plus |\n\n### 2.2 LIBERO-Plus 是什么\n\n在原始 LIBERO 基础上增加了：\n- **10,030 个任务变体**，通过系统化扰动生成\n- **7 个扰动维度**，**21 个子维度**\n- **5 个难度级别** (L1-L5)，按多模型共识分层（4 个参考模型中几个能解决该任务）\n- **20,000+ 训练轨迹**（RLDS 格式）\n- 与 vanilla LIBERO 完全兼容的 drop-in replacement\n\n### 2.3 七个扰动维度（精确定义）\n\n#### 2.3.1 物体布局 (Objects Layout)\n- **O1 — 干扰物体 (Confounding objects):** 从 416 个物体池中随机添加 n 个未见过的干扰物体，通过修改 BDDL 任务描述文件实现\n- **O2 — 目标位移 (Target displacement):** 对目标物体初始位置 (x, y, z) 和朝向施加随机扰动，保持语义关系\n\n#### 2.3.2 相机视角 (Camera Viewpoints)\n- **C1 — 距离缩放 (Distance scaling):** 沿光轴将相机距离缩放 1.01x-2.00x\n- **C2 — 球坐标位置 (Spherical position):** 改变方位角 (delta-theta) 和仰角 (delta-phi)，范围 15-75 度\n- **C3 — 朝向扰动 (Orientation perturbation):** 扰动 yaw/pitch/roll，范围 2-10 度\n\n实现：修改 `Problem` 类接口；主要针对第三人称相机（非腕部相机）\n\n#### 2.3.3 机器人初始状态 (Robot Initial States)\n- 对机械臂初始关节位置施加随机扰动，幅度 0.1-0.5\n- 实现：修改 `Problem` 类接口\n\n#### 2.3.4 语言指令 (Language Instructions)\n- **R1 — 干扰改写 (Distraction rewrites):** 添加与任务无关的上下文信息\n- **R2 — 常识替换 (Commonsense substitution):** 用常识性替代描述替换物体名称\n- **R3 — 推理复杂度 (Reasoning complexity):** 改变多步骤任务的推理复杂度\n- 实现：基于 LLM 的指令改写\n\n#### 2.3.5 光照条件 (Light Conditions)\n- **L1 — 漫射颜色 (Diffuse color):** RGB 通道漫射光照调整\n- **L2 — 方向 (Direction):** 平行光源方向变化\n- **L3 — 镜面强度 (Specular intensity):** 镜面高光强度（反射表面）\n- **L4 — 阴影 (Shadow casting):** 阴影开关控制\n- 实现：修改 MuJoCo 场景 XML 定义文件，注册新场景类\n\n#### 2.3.6 背景纹理 (Background Textures)\n- **B1 — 场景纹理 (Scene texture):** 使用 950 张精选纹理通过 XML 场景文件替换环境纹理\n- **B2 — 表面纹理 (Surface texture):** 随机改变工作表面纹理（桌面、地板）\n- 实现：修改 XML 场景定义文件，添加新纹理资产\n\n#### 2.3.7 传感器噪声 (Sensor Noise)\n图像空间后处理（非物理层级）：\n- **N1 — 运动模糊 (Motion blur):** kernel 半径 r=5-35，高斯 sigma=2-20，角度 U(-45, 45)度\n- **N2 — 高斯模糊 (Gaussian blur):** sigma 1-10\n- **N3 — 缩放模糊 (Zoom blur):** 缩放因子 [s_min, s_max, step] 从 [1, 1.11, 0.01] 到 [1, 1.56, 0.03]\n- **N4 — 雾 (Fog):** 密度 alpha=0.5-5.0，衰减率 beta=1.3-3.0\n- **N5 — 毛玻璃模糊 (Glass blur):** sigma=0.5-2.5，像素位移 delta=1-5，迭代 1-3 次\n\n### 2.4 难度级别 (L1-L5)\n\n按 4 个参考模型（OpenVLA-OFT, pi0, pi0-fast, UniVLA）能否解决分层：\n- L1: 4 个都能解决\n- L2: 3 个能解决\n- L3: 2 个能解决\n- L4: 1 个能解决\n- L5: 无一能解决\n\n### 2.5 安装和运行\n\n**安装：**\n```bash\n# 系统依赖\nsudo apt install libexpat1 libfontconfig1-dev libmagickwand-dev\n\n# 克隆安装\ngit clone https://github.com/sylvestf/LIBERO-plus.git\ncd LIBERO-plus\npip install -e .\npip install -r extra_requirements.txt\n\n# 如果已装 vanilla LIBERO，需先卸载\npip uninstall -y hf-libero\n\nexport MUJOCO_GL=egl\n```\n\n**下载资产：**\n\n从 [HuggingFace](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main) 下载 `assets.zip`，解压到 `LIBERO-plus/libero/libero/assets/`。\n\n期望结构：\n```\nlibero/libero/assets/\n├── articulated_objects/\n├── new_objects/\n├── scenes/\n├── stable_hope_objects/\n├── stable_scanned_objects/\n├── textures/\n├── turbosquid_objects/\n├── serving_region.xml\n├── wall_frames.stl\n└── wall.xml\n```\n\n**配置：** 检查 `/root/.libero/config.yaml`。评测时设 `num_trials_per_task: 1`。\n\n任务到扰动类别映射：`.libero/libero/benchmark/task_classification.json`\n\n**LeRobot 评测：**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero_plus \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n\n### 2.6 与标准 LIBERO 的关系\n\nLIBERO-Plus 是 vanilla LIBERO 的 **drop-in replacement**：\n- 安装在同一个 `libero` Python 包名下（替换原版）\n- 相同的 `LiberoEnv` gym 接口\n- 相同的相机名称 (`agentview_image`, `robot0_eye_in_hand_image`)\n- 相同的观测/动作格式\n- 相同的 task suite 名称\n- **不能同时安装 vanilla LIBERO 和 LIBERO-Plus**，切换需要先卸载再安装\n\n---\n\n## 3. 数据增强相关\n\n### 3.1 robosuite 内置随机化\n\nLIBERO 基于 robosuite (MuJoCo)，robosuite 提供了 `DomainRandomizationWrapper` 和三个 Modder 类，可用于任何 robosuite 环境包括 LIBERO。\n\n**DomainRandomizationWrapper：**\n```python\nfrom robosuite.wrappers import DomainRandomizationWrapper\n\nenv = DomainRandomizationWrapper(\n    env=base_env,\n    seed=42,\n    randomize_color=True,        # 几何体/纹理颜色随机化\n    randomize_camera=True,       # 相机位置/朝向/FOV\n    randomize_lighting=True,     # 光源位置/方向/颜色\n    randomize_dynamics=True,     # 物理参数\n    randomize_on_reset=True,     # episode 重置时随机化\n    randomize_every_n_steps=1,   # rollout 中的频率\n)\n```\n\n**CameraModder（内置）：**\n- 位置扰动：默认 size 0.01\n- 旋转扰动（四元数）：默认 size 0.087 (~5 度)\n- FOV 扰动：默认 size 5.0 度\n\n**LightingModder（内置）：**\n- 位置扰动：默认 size 0.1\n- 方向扰动：默认 size 0.35\n- 镜面/环境光/漫射扰动：默认 size 0.1\n- 开关控制：on/off\n\n**TextureModder（内置）：**\n- RGB 颜色随机化 (local interpolation 0.1)\n- 纹理模式：RGB, checker, noise, gradient\n- 材质属性：反射率、光泽度、镜面反射 (local interpolation 0.2)\n- 天空盒随机化（可选）\n\nDemo 脚本：`robosuite/demos/demo_domain_randomization.py`\n\n### 3.2 LIBERO-Plus 扰动可否复用为训练时数据增强\n\n**可以，且论文已经这样做了。** LIBERO-Plus 同时提供评测任务和训练数据集：\n\n**已提供的训练数据：**\n- **22,400 条训练轨迹**（过滤后 20,000+），在各种扰动条件下生成\n- 分布：2,400 物体布局变体 + 各 4,000 光照/相机/背景/语言/噪声维度\n- RLDS 格式存储，LeRobot 格式见 `lerobot/libero_plus`\n- 论文证明混合 SFT (mix-SFT) 训练显著提升鲁棒性：OpenVLA-OFT+ 平均 79.6%\n\n**三条数据增强路径：**\n\n**路径 A — 直接使用 LIBERO-Plus 训练数据：**\n```bash\nlerobot-train \\\n    --policy.type=smolvla \\\n    --dataset.repo_id=lerobot/libero_plus \\\n    --env.type=libero_plus \\\n    ...\n```\n\n**路径 B — 使用 robosuite 内置 DomainRandomizationWrapper 在线增强：**\n```python\nfrom robosuite.wrappers import DomainRandomizationWrapper\nenv = DomainRandomizationWrapper(\n    env=libero_env,\n    randomize_camera=True,\n    randomize_lighting=True,\n    randomize_color=True\n)\n```\n在线随机化，每 N 步应用随机扰动。适合训练时增强但可控性较低。\n\n**路径 C — 复用 LIBERO-Plus 扰动代码做自定义增强：**\n- 光照/纹理扰动：修改场景 XML + 注册新场景\n- 相机扰动：修改 `Problem` 类接口\n- 传感器噪声 (N1-N5)：纯图像空间后处理，可直接作为标准数据增强应用于任何存储轨迹，无需重新渲染\n\n**关键区别：**\n- robosuite 内置随机化（路径 B）是 **在线** 的，可控性低\n- LIBERO-Plus 扰动（路径 C）是 **结构化** 的，有明确参数范围和难度分层，更适合系统性鲁棒性训练\n- 传感器噪声 (N1-N5) 是纯图像后处理，可以零成本复用为数据增强\n\n---\n\n## 4. 与 LeRobot 的集成\n\n### 4.1 原生支持\n\nLeRobot **原生支持** LIBERO，是一级基准测试环境。\n\n安装：`pip install -e \".[libero]\"`\n\n文档：https://huggingface.co/docs/lerobot/en/libero\n\nHuggingFace 维护了 LIBERO fork：https://github.com/huggingface/lerobot-libero\n\n### 4.2 HuggingFace Hub 数据集\n\n**主要数据集（推荐用于训练）：**\n\n| 数据集 ID | Episodes | 任务数 | 大小 | 说明 |\n|-----------|----------|--------|------|------|\n| `HuggingFaceVLA/libero` | 148 | 10 | ~1.9 GB | 官方预处理数据集，LeRobot 文档推荐 |\n| `lerobot/libero` | 1,693 | 40 | ~1.94 GB | 4 个标准 suite 合并（视频格式, AV1 编码） |\n| `physical-intelligence/libero` | 147 | 10 | ~34.9 GB | PI 的转换版本, RLDS 来源, CC-BY-4.0 |\n| `lerobot/libero_plus` | — | — | — | LIBERO-Plus 训练数据 |\n\n**每个 suite 的图像数据集：**\n\n| 数据集 ID | 任务数 |\n|-----------|--------|\n| `lerobot/libero_10_image` | 10 |\n| `lerobot/libero_object_image` | 10 |\n| `lerobot/libero_spatial_image` | 10 |\n| `lerobot/libero_goal_image` | 10 |\n\n**社区数据集：**\n- `IPEC-COMMUNITY/libero_90_no_noops_lerobot` — LIBERO-90 去除 no-op 版本\n\n### 4.3 数据格式映射\n\n| LIBERO 字段 | LeRobot 特征 | 类型 | 形状 |\n|-------------|-------------|------|------|\n| `agentview_image` | `observation.images.image` | Video/Image | (256, 256, 3) |\n| `robot0_eye_in_hand_image` | `observation.images.image2` | Video/Image | (256, 256, 3) |\n| `observation[\"state\"]` | `observation.state` | float32 | (8,) |\n| `action` | `action` | float32 | (7,) |\n| `language_instruction` | `task` (task_index) | string/int | — |\n\nLeRobot 元数据：robot_type=`panda`，fps=`10`，视频编码=AV1 yuv420p，表格数据用 Parquet 存储\n\n### 4.4 转换脚本\n\n**方式 A：Physical Intelligence 的 OpenPI 转换脚本（主要）**\n\n脚本路径：[`Physical-Intelligence/openpi/examples/libero/convert_libero_data_to_lerobot.py`](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py)\n\n```bash\n# 前置依赖\nuv pip install tensorflow tensorflow_datasets\n\n# 原始数据来源\n# https://huggingface.co/datasets/openvla/modified_libero_rlds\n\n# 执行转换\nuv run examples/libero/convert_libero_data_to_lerobot.py \\\n  --data_dir /path/to/your/data \\\n  --push_to_hub\n```\n\n处理流程：\n1. 读取 4 个 RLDS 数据集：`libero_10_no_noops`, `libero_goal_no_noops`, `libero_object_no_noops`, `libero_spatial_no_noops`\n2. 创建 `LeRobotDataset`，robot_type=panda, fps=10\n3. 逐 episode 迭代，每步调用 `dataset.add_frame()`\n4. 每个 episode 调用 `dataset.save_episode()`\n5. 可选推送到 HuggingFace Hub\n\n处理时间：约 30 分钟\n\n**方式 B：通用 HDF5 → LeRobot 转换器**\n\n仓库：https://github.com/anarnuri/hdf5_to_lerobot_converter\n\n支持 LIBERO 原生 HDF5 格式。\n\n**方式 C：直接使用预转换数据集（无需转换）**\n\n```python\nfrom lerobot.common.datasets.lerobot_dataset import LeRobotDataset\n\ndataset = LeRobotDataset(\"HuggingFaceVLA/libero\")\n# 或\ndataset = LeRobotDataset(\"lerobot/libero\")\n```\n\n### 4.5 端到端训练和评测示例\n\n**训练：**\n```bash\nlerobot-train \\\n  --policy.type=smolvla \\\n  --policy.repo_id=${HF_USER}/libero-test \\\n  --policy.load_vlm_weights=true \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --env.type=libero \\\n  --env.task=libero_10 \\\n  --output_dir=./outputs/ \\\n  --steps=100000 \\\n  --batch_size=4 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=1 \\\n  --eval_freq=1000\n```\n\n**评测：**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n\n---\n\n## 5. 关键注意事项\n\n1. **LIBERO-90 数据** 不在标准预转换数据集中。需要用 OpenPI 转换脚本或社区数据集 `IPEC-COMMUNITY/libero_90_no_noops_lerobot`\n2. **控制模式** (`relative` vs `absolute`) 必须与策略的动作参数化匹配\n3. **vanilla LIBERO 和 LIBERO-Plus 不能同时安装**，两者共用同一 Python 包名\n4. LeRobot 中 LIBERO 仅支持 Linux（MuJoCo 渲染需 EGL）\n5. LeRobot 格式的图像分辨率为 256x256，而原始 LIBERO 为 128x128 [UNVERIFIED — 需确认是否做了上采样或 LeRobot 环境重新渲染]\n6. 原始 LIBERO 采集频率 20Hz，LeRobot 格式为 10Hz（可能做了下采样）[UNVERIFIED — 需确认具体降频策略]\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "ed1e3f2b-5dd1-4f43-aec9-4e1690c42692",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KaXfrY7rLugJND194qYAkg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 127,
      "cache_read_input_tokens": 34470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 127
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 246 · 2026-05-15T11:18:28.110Z_

<details><summary>↩ Tool result · `toolu_01LrSHXmQBaHspBqcmLQUt3W`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/research_libero_benchmark.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "5c7adfbe-4759-45e3-a443-1b40911a2ad5",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/research_libero_benchmark.md",
    "content": "# LIBERO Benchmark + LIBERO-Plus 调研报告\n\n调研日期：2026-05-15\n\n---\n\n## 1. LIBERO Benchmark\n\n### 1.1 基本信息\n\n| 项目 | 内容 |\n|------|------|\n| 论文 | [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310) (NeurIPS 2023 D&B) |\n| GitHub | https://github.com/Lifelong-Robot-Learning/LIBERO |\n| 项目主页 | https://libero-project.github.io |\n| License | MIT (代码), CC BY 4.0 (数据集) |\n| 模拟器 | robosuite (MuJoCo) |\n| 机器人 | Franka Panda 7-DOF |\n\n### 1.2 安装\n\n**方式 A：pip**\n```bash\npip install libero\n```\n\n**方式 B：from source（推荐）**\n```bash\nconda create -n libero python=3.8.13\nconda activate libero\ngit clone https://github.com/Lifelong-Robot-Learning/LIBERO.git\ncd LIBERO\npip install -r requirements.txt\npip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113\npip install -e .\n```\n\n**方式 C：通过 LeRobot**\n```bash\npip install -e \".[libero]\"\n```\n\n无头渲染需设置：`export MUJOCO_GL=egl`\n\n### 1.3 五个 Task Suite\n\n所有任务都是 language-conditioned manipulation，使用 Franka Panda 机械臂。\n\n| Suite | CLI 名称 | 任务数 | 描述 |\n|-------|----------|--------|------|\n| **LIBERO-Spatial** | `libero_spatial` | 10 | 同一目标（拿黑碗放盘子），碗在不同空间位置。测试 **空间关系知识** 迁移 |\n| **LIBERO-Object** | `libero_object` | 10 | 同一目标结构（拿 X 放篮子），不同物体。测试 **物体知识** 迁移 |\n| **LIBERO-Goal** | `libero_goal` | 10 | 同一场景，不同目标（开抽屉、放碗到炉子上等）。测试 **目标/程序知识** 迁移 |\n| **LIBERO-90** | `libero_90` | 90 | LIBERO-100 中的短期任务，跨 spatial/object/goal 的混合分布偏移。用于 **预训练** |\n| **LIBERO-Long** | `libero_10` | 10 | LIBERO-100 中的长期多步骤任务。用于预训练后的 **下游评测** |\n\n**LIBERO-Spatial 示例任务（全部 10 个）：**\n1. pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\n2. pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\n3. pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\n4. pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\n5. pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\n6. pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\n7. pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\n8. pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\n9. pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\n10. pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\n\n**LIBERO-Object 示例任务：** pick_up_the_{alphabet_soup, cream_cheese, salad_dressing, bbq_sauce, ketchup, tomato_sauce, butter, milk, chocolate_pudding, orange_juice}_and_place_it_in_the_basket\n\n**LIBERO-Goal 示例任务：** open_the_middle_drawer_of_the_cabinet, put_the_bowl_on_the_stove, put_the_wine_bottle_on_top_of_the_cabinet, open_the_top_drawer_and_put_the_bowl_inside, put_the_bowl_on_top_of_the_cabinet, push_the_plate_to_the_front_of_the_stove, put_the_cream_cheese_in_the_bowl, turn_on_the_stove, put_the_bowl_on_the_plate, put_the_wine_bottle_on_the_rack\n\n### 1.4 数据下载\n\n每个任务有 **50 条人类遥操作演示**，通过 SpaceMouse 以 20 Hz 采集。\n\n**方式 A：官方脚本**\n```bash\n# 全部下载\npython benchmark_scripts/download_libero_datasets.py\n\n# 下载特定 suite\npython benchmark_scripts/download_libero_datasets.py --datasets libero_spatial\npython benchmark_scripts/download_libero_datasets.py --datasets libero_object\npython benchmark_scripts/download_libero_datasets.py --datasets libero_goal\npython benchmark_scripts/download_libero_datasets.py --datasets libero_100  # 含 libero_90 + libero_10\n\n# 通过 HuggingFace 下载（推荐，原始链接可能过期）\npython benchmark_scripts/download_libero_datasets.py --use-huggingface\n```\n\n默认下载位置：LIBERO 根目录下的 `./datasets/`\n\n**方式 B：HuggingFace 直接下载**\n\n| 数据集 | 格式 | 大小 |\n|--------|------|------|\n| `yifengzhu-hf/LIBERO-datasets` | 原始 HDF5 | ~100 GB 总计 |\n| `physical-intelligence/libero` | LeRobot (Parquet) | ~34.9 GB |\n| `HuggingFaceVLA/libero` | LeRobot | ~1.9 GB |\n| `lerobot/libero` | LeRobot (视频 AV1) | ~1.94 GB |\n\n**各 suite 近似大小（原始 HDF5 格式）：**\n\n| Suite | 大小 |\n|-------|------|\n| libero_spatial | ~6.6 GB |\n| libero_object | ~9.3 GB |\n| libero_goal | ~6-9 GB |\n| libero_10 (Long) | ~12.8 GB |\n| libero_90 | ~60-70 GB |\n| **总计** | **~100 GB** |\n\n### 1.5 数据格式\n\n**文件格式：** HDF5（每个任务一个 `.hdf5` 文件）\n\n**HDF5 结构：**\n```\ndata/\n  demo_0/\n    obs/\n      agentview_rgb          # (T, 128, 128, 3) uint8 — 第三人称相机\n      eye_in_hand_rgb        # (T, 128, 128, 3) uint8 — 腕部相机\n      gripper_states         # (T, 1) — 夹爪开合度\n      joint_states           # (T, 7) — 7 个关节角度\n      ee_states              # (T, 6) — 末端执行器位置 + 轴角朝向\n      ee_pos                 # (T, 3) — 末端执行器 xyz 位置\n      ee_ori                 # (T, 3) — 末端执行器轴角朝向\n    actions                  # (T, 7) — 7-DOF 动作\n    states                   # (T, D) — 完整模拟器状态\n    robot_states             # (T, D) — gripper_pos + ee_pos + ee_quat 拼接\n    rewards                  # (T,) — 稀疏: 全 0，最后成功步为 1\n    dones                    # (T,) — episode 结束时为 1\n  demo_1/ ...\n  demo_49/ ...\n```\n\n**观测空间：**\n\n| 键 | 维度 | 含义 |\n|----|------|------|\n| `agentview_rgb` (→ `agentview_image`) | (128, 128, 3) | 工作区 RGB 图像 |\n| `eye_in_hand_rgb` (→ `robot0_eye_in_hand_image`) | (128, 128, 3) | 腕部 RGB 图像 |\n| `gripper_states` (→ `robot0_gripper_qpos`) | (1,) 或 (2,) | 夹爪指位置 |\n| `joint_states` (→ `robot0_joint_pos`) | (7,) | Franka Panda 7 关节角 |\n| `ee_pos` | (3,) | 末端执行器 xyz 位置 |\n| `ee_ori` | (3,) | 末端执行器轴角朝向 |\n\n**LeRobot 格式中** proprioceptive state 为 8 维：`observation.state` = [ee_pos (3) + ee_axis_angle (3) + gripper_qpos (2)]\n\n**动作空间：**\n\n| 维度 | 含义 |\n|------|------|\n| 0-2 | 末端执行器位置增量 (dx, dy, dz) |\n| 3-5 | 末端执行器朝向增量 (轴角 / 欧拉角) |\n| 6 | 夹爪命令 (1=闭合, -1=打开) |\n\n- 总计 **7 维连续动作**，Box(-1, 1, shape=(7,))\n- 控制模式：**OSC_POSE**（操作空间控制）\n- 频率：**20 Hz**（原始），LeRobot 格式 **10 Hz**\n- 支持 `relative`（增量，默认）和 `absolute` 两种控制模式\n- 奖励：稀疏 — 中间步全 0，任务完成时 +1\n\n### 1.6 评测\n\n**原生 LIBERO 评测：**\n\n```bash\npython libero/lifelong/evaluate.py \\\n  --benchmark LIBERO_SPATIAL \\\n  --task_id 0 \\\n  --algo base \\\n  --policy bc_transformer_policy \\\n  --seed 10000 \\\n  --ep 50 \\\n  --load_task 0 \\\n  --device_id 0\n```\n\n参数说明：\n- `--benchmark`: `LIBERO_SPATIAL` / `LIBERO_OBJECT` / `LIBERO_GOAL` / `LIBERO_90` / `LIBERO_10`\n- `--task_id`: suite 内的任务索引\n- `--algo`: 终身学习算法 (`base`, `er`, `ewc`, `packnet`, `multitask`)\n- `--policy`: 策略架构 (`bc_rnn_policy`, `bc_transformer_policy`, `bc_vilt_policy`)\n- `--save-videos`: 可选，录制评测视频\n\n**评测协议：**\n- 20 个并行环境同时运行 (`n_eval: 20`, `num_procs: 20`)\n- 每个 episode 最多 600 步 (`max_steps: 600`)\n- 开头 5 步零动作用于物理稳定\n- episode 在 `done=True` 或达到最大步数时终止\n\n**输出指标：**\n- **Success rate** = num_success / num_envs（每个任务）\n- **Loss** = 测试集损失\n- 结果保存路径：`{save_dir}/{benchmark}_{algo}_{policy}_{seed}_[ep|load]_{task_id}.stats`\n\n**终身学习指标（跨任务序列）：**\n- **FWT (Forward Transfer)**: 序列训练后在新任务上的成功率\n- **NBT (Negative Backward Transfer)**: 早期任务性能退化（灾难性遗忘）\n- **AUC (Area Under Curve)**: 综合 FWT 和 NBT 的累积成功率\n\n**原生训练命令：**\n```bash\nexport CUDA_VISIBLE_DEVICES=0 && \\\nexport MUJOCO_EGL_DEVICE_ID=0 && \\\npython libero/lifelong/main.py seed=10000 \\\n  benchmark_name=LIBERO_SPATIAL \\\n  policy=bc_transformer_policy \\\n  lifelong=base\n```\n\n**LeRobot 评测：**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n标准协议：每个任务 10 个 episode，4 个标准 suite = 400 个 episode。\n\n---\n\n## 2. LIBERO-Plus 扰动评测\n\n### 2.1 基本信息\n\n| 项目 | 内容 |\n|------|------|\n| 论文 | [LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626) (CVPR 2026) |\n| GitHub | https://github.com/sylvestf/LIBERO-plus |\n| 项目主页 | https://sylvestf.github.io/LIBERO-plus/ |\n| HF 资产 | https://huggingface.co/datasets/Sylvest/LIBERO-plus |\n| 训练数据 (RLDS) | https://huggingface.co/datasets/Sylvest/libero_plus_rlds |\n| LeRobot 格式 | https://huggingface.co/datasets/lerobot/libero_plus |\n\n### 2.2 LIBERO-Plus 是什么\n\n在原始 LIBERO 基础上增加了：\n- **10,030 个任务变体**，通过系统化扰动生成\n- **7 个扰动维度**，**21 个子维度**\n- **5 个难度级别** (L1-L5)，按多模型共识分层（4 个参考模型中几个能解决该任务）\n- **20,000+ 训练轨迹**（RLDS 格式）\n- 与 vanilla LIBERO 完全兼容的 drop-in replacement\n\n### 2.3 七个扰动维度（精确定义）\n\n#### 2.3.1 物体布局 (Objects Layout)\n- **O1 — 干扰物体 (Confounding objects):** 从 416 个物体池中随机添加 n 个未见过的干扰物体，通过修改 BDDL 任务描述文件实现\n- **O2 — 目标位移 (Target displacement):** 对目标物体初始位置 (x, y, z) 和朝向施加随机扰动，保持语义关系\n\n#### 2.3.2 相机视角 (Camera Viewpoints)\n- **C1 — 距离缩放 (Distance scaling):** 沿光轴将相机距离缩放 1.01x-2.00x\n- **C2 — 球坐标位置 (Spherical position):** 改变方位角 (delta-theta) 和仰角 (delta-phi)，范围 15-75 度\n- **C3 — 朝向扰动 (Orientation perturbation):** 扰动 yaw/pitch/roll，范围 2-10 度\n\n实现：修改 `Problem` 类接口；主要针对第三人称相机（非腕部相机）\n\n#### 2.3.3 机器人初始状态 (Robot Initial States)\n- 对机械臂初始关节位置施加随机扰动，幅度 0.1-0.5\n- 实现：修改 `Problem` 类接口\n\n#### 2.3.4 语言指令 (Language Instructions)\n- **R1 — 干扰改写 (Distraction rewrites):** 添加与任务无关的上下文信息\n- **R2 — 常识替换 (Commonsense substitution):** 用常识性替代描述替换物体名称\n- **R3 — 推理复杂度 (Reasoning complexity):** 改变多步骤任务的推理复杂度\n- 实现：基于 LLM 的指令改写\n\n#### 2.3.5 光照条件 (Light Conditions)\n- **L1 — 漫射颜色 (Diffuse color):** RGB 通道漫射光照调整\n- **L2 — 方向 (Direction):** 平行光源方向变化\n- **L3 — 镜面强度 (Specular intensity):** 镜面高光强度（反射表面）\n- **L4 — 阴影 (Shadow casting):** 阴影开关控制\n- 实现：修改 MuJoCo 场景 XML 定义文件，注册新场景类\n\n#### 2.3.6 背景纹理 (Background Textures)\n- **B1 — 场景纹理 (Scene texture):** 使用 950 张精选纹理通过 XML 场景文件替换环境纹理\n- **B2 — 表面纹理 (Surface texture):** 随机改变工作表面纹理（桌面、地板）\n- 实现：修改 XML 场景定义文件，添加新纹理资产\n\n#### 2.3.7 传感器噪声 (Sensor Noise)\n图像空间后处理（非物理层级）：\n- **N1 — 运动模糊 (Motion blur):** kernel 半径 r=5-35，高斯 sigma=2-20，角度 U(-45, 45)度\n- **N2 — 高斯模糊 (Gaussian blur):** sigma 1-10\n- **N3 — 缩放模糊 (Zoom blur):** 缩放因子 [s_min, s_max, step] 从 [1, 1.11, 0.01] 到 [1, 1.56, 0.03]\n- **N4 — 雾 (Fog):** 密度 alpha=0.5-5.0，衰减率 beta=1.3-3.0\n- **N5 — 毛玻璃模糊 (Glass blur):** sigma=0.5-2.5，像素位移 delta=1-5，迭代 1-3 次\n\n### 2.4 难度级别 (L1-L5)\n\n按 4 个参考模型（OpenVLA-OFT, pi0, pi0-fast, UniVLA）能否解决分层：\n- L1: 4 个都能解决\n- L2: 3 个能解决\n- L3: 2 个能解决\n- L4: 1 个能解决\n- L5: 无一能解决\n\n### 2.5 安装和运行\n\n**安装：**\n```bash\n# 系统依赖\nsudo apt install libexpat1 libfontconfig1-dev libmagickwand-dev\n\n# 克隆安装\ngit clone https://github.com/sylvestf/LIBERO-plus.git\ncd LIBERO-plus\npip install -e .\npip install -r extra_requirements.txt\n\n# 如果已装 vanilla LIBERO，需先卸载\npip uninstall -y hf-libero\n\nexport MUJOCO_GL=egl\n```\n\n**下载资产：**\n\n从 [HuggingFace](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main) 下载 `assets.zip`，解压到 `LIBERO-plus/libero/libero/assets/`。\n\n期望结构：\n```\nlibero/libero/assets/\n├── articulated_objects/\n├── new_objects/\n├── scenes/\n├── stable_hope_objects/\n├── stable_scanned_objects/\n├── textures/\n├── turbosquid_objects/\n├── serving_region.xml\n├── wall_frames.stl\n└── wall.xml\n```\n\n**配置：** 检查 `/root/.libero/config.yaml`。评测时设 `num_trials_per_task: 1`。\n\n任务到扰动类别映射：`.libero/libero/benchmark/task_classification.json`\n\n**LeRobot 评测：**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero_plus \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n\n### 2.6 与标准 LIBERO 的关系\n\nLIBERO-Plus 是 vanilla LIBERO 的 **drop-in replacement**：\n- 安装在同一个 `libero` Python 包名下（替换原版）\n- 相同的 `LiberoEnv` gym 接口\n- 相同的相机名称 (`agentview_image`, `robot0_eye_in_hand_image`)\n- 相同的观测/动作格式\n- 相同的 task suite 名称\n- **不能同时安装 vanilla LIBERO 和 LIBERO-Plus**，切换需要先卸载再安装\n\n---\n\n## 3. 数据增强相关\n\n### 3.1 robosuite 内置随机化\n\nLIBERO 基于 robosuite (MuJoCo)，robosuite 提供了 `DomainRandomizationWrapper` 和三个 Modder 类，可用于任何 robosuite 环境包括 LIBERO。\n\n**DomainRandomizationWrapper：**\n```python\nfrom robosuite.wrappers import DomainRandomizationWrapper\n\nenv = DomainRandomizationWrapper(\n    env=base_env,\n    seed=42,\n    randomize_color=True,        # 几何体/纹理颜色随机化\n    randomize_camera=True,       # 相机位置/朝向/FOV\n    randomize_lighting=True,     # 光源位置/方向/颜色\n    randomize_dynamics=True,     # 物理参数\n    randomize_on_reset=True,     # episode 重置时随机化\n    randomize_every_n_steps=1,   # rollout 中的频率\n)\n```\n\n**CameraModder（内置）：**\n- 位置扰动：默认 size 0.01\n- 旋转扰动（四元数）：默认 size 0.087 (~5 度)\n- FOV 扰动：默认 size 5.0 度\n\n**LightingModder（内置）：**\n- 位置扰动：默认 size 0.1\n- 方向扰动：默认 size 0.35\n- 镜面/环境光/漫射扰动：默认 size 0.1\n- 开关控制：on/off\n\n**TextureModder（内置）：**\n- RGB 颜色随机化 (local interpolation 0.1)\n- 纹理模式：RGB, checker, noise, gradient\n- 材质属性：反射率、光泽度、镜面反射 (local interpolation 0.2)\n- 天空盒随机化（可选）\n\nDemo 脚本：`robosuite/demos/demo_domain_randomization.py`\n\n### 3.2 LIBERO-Plus 扰动可否复用为训练时数据增强\n\n**可以，且论文已经这样做了。** LIBERO-Plus 同时提供评测任务和训练数据集：\n\n**已提供的训练数据：**\n- **22,400 条训练轨迹**（过滤后 20,000+），在各种扰动条件下生成\n- 分布：2,400 物体布局变体 + 各 4,000 光照/相机/背景/语言/噪声维度\n- RLDS 格式存储，LeRobot 格式见 `lerobot/libero_plus`\n- 论文证明混合 SFT (mix-SFT) 训练显著提升鲁棒性：OpenVLA-OFT+ 平均 79.6%\n\n**三条数据增强路径：**\n\n**路径 A — 直接使用 LIBERO-Plus 训练数据：**\n```bash\nlerobot-train \\\n    --policy.type=smolvla \\\n    --dataset.repo_id=lerobot/libero_plus \\\n    --env.type=libero_plus \\\n    ...\n```\n\n**路径 B — 使用 robosuite 内置 DomainRandomizationWrapper 在线增强：**\n```python\nfrom robosuite.wrappers import DomainRandomizationWrapper\nenv = DomainRandomizationWrapper(\n    env=libero_env,\n    randomize_camera=True,\n    randomize_lighting=True,\n    randomize_color=True\n)\n```\n在线随机化，每 N 步应用随机扰动。适合训练时增强但可控性较低。\n\n**路径 C — 复用 LIBERO-Plus 扰动代码做自定义增强：**\n- 光照/纹理扰动：修改场景 XML + 注册新场景\n- 相机扰动：修改 `Problem` 类接口\n- 传感器噪声 (N1-N5)：纯图像空间后处理，可直接作为标准数据增强应用于任何存储轨迹，无需重新渲染\n\n**关键区别：**\n- robosuite 内置随机化（路径 B）是 **在线** 的，可控性低\n- LIBERO-Plus 扰动（路径 C）是 **结构化** 的，有明确参数范围和难度分层，更适合系统性鲁棒性训练\n- 传感器噪声 (N1-N5) 是纯图像后处理，可以零成本复用为数据增强\n\n---\n\n## 4. 与 LeRobot 的集成\n\n### 4.1 原生支持\n\nLeRobot **原生支持** LIBERO，是一级基准测试环境。\n\n安装：`pip install -e \".[libero]\"`\n\n文档：https://huggingface.co/docs/lerobot/en/libero\n\nHuggingFace 维护了 LIBERO fork：https://github.com/huggingface/lerobot-libero\n\n### 4.2 HuggingFace Hub 数据集\n\n**主要数据集（推荐用于训练）：**\n\n| 数据集 ID | Episodes | 任务数 | 大小 | 说明 |\n|-----------|----------|--------|------|------|\n| `HuggingFaceVLA/libero` | 148 | 10 | ~1.9 GB | 官方预处理数据集，LeRobot 文档推荐 |\n| `lerobot/libero` | 1,693 | 40 | ~1.94 GB | 4 个标准 suite 合并（视频格式, AV1 编码） |\n| `physical-intelligence/libero` | 147 | 10 | ~34.9 GB | PI 的转换版本, RLDS 来源, CC-BY-4.0 |\n| `lerobot/libero_plus` | — | — | — | LIBERO-Plus 训练数据 |\n\n**每个 suite 的图像数据集：**\n\n| 数据集 ID | 任务数 |\n|-----------|--------|\n| `lerobot/libero_10_image` | 10 |\n| `lerobot/libero_object_image` | 10 |\n| `lerobot/libero_spatial_image` | 10 |\n| `lerobot/libero_goal_image` | 10 |\n\n**社区数据集：**\n- `IPEC-COMMUNITY/libero_90_no_noops_lerobot` — LIBERO-90 去除 no-op 版本\n\n### 4.3 数据格式映射\n\n| LIBERO 字段 | LeRobot 特征 | 类型 | 形状 |\n|-------------|-------------|------|------|\n| `agentview_image` | `observation.images.image` | Video/Image | (256, 256, 3) |\n| `robot0_eye_in_hand_image` | `observation.images.image2` | Video/Image | (256, 256, 3) |\n| `observation[\"state\"]` | `observation.state` | float32 | (8,) |\n| `action` | `action` | float32 | (7,) |\n| `language_instruction` | `task` (task_index) | string/int | — |\n\nLeRobot 元数据：robot_type=`panda`，fps=`10`，视频编码=AV1 yuv420p，表格数据用 Parquet 存储\n\n### 4.4 转换脚本\n\n**方式 A：Physical Intelligence 的 OpenPI 转换脚本（主要）**\n\n脚本路径：[`Physical-Intelligence/openpi/examples/libero/convert_libero_data_to_lerobot.py`](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py)\n\n```bash\n# 前置依赖\nuv pip install tensorflow tensorflow_datasets\n\n# 原始数据来源\n# https://huggingface.co/datasets/openvla/modified_libero_rlds\n\n# 执行转换\nuv run examples/libero/convert_libero_data_to_lerobot.py \\\n  --data_dir /path/to/your/data \\\n  --push_to_hub\n```\n\n处理流程：\n1. 读取 4 个 RLDS 数据集：`libero_10_no_noops`, `libero_goal_no_noops`, `libero_object_no_noops`, `libero_spatial_no_noops`\n2. 创建 `LeRobotDataset`，robot_type=panda, fps=10\n3. 逐 episode 迭代，每步调用 `dataset.add_frame()`\n4. 每个 episode 调用 `dataset.save_episode()`\n5. 可选推送到 HuggingFace Hub\n\n处理时间：约 30 分钟\n\n**方式 B：通用 HDF5 → LeRobot 转换器**\n\n仓库：https://github.com/anarnuri/hdf5_to_lerobot_converter\n\n支持 LIBERO 原生 HDF5 格式。\n\n**方式 C：直接使用预转换数据集（无需转换）**\n\n```python\nfrom lerobot.common.datasets.lerobot_dataset import LeRobotDataset\n\ndataset = LeRobotDataset(\"HuggingFaceVLA/libero\")\n# 或\ndataset = LeRobotDataset(\"lerobot/libero\")\n```\n\n### 4.5 端到端训练和评测示例\n\n**训练：**\n```bash\nlerobot-train \\\n  --policy.type=smolvla \\\n  --policy.repo_id=${HF_USER}/libero-test \\\n  --policy.load_vlm_weights=true \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --env.type=libero \\\n  --env.task=libero_10 \\\n  --output_dir=./outputs/ \\\n  --steps=100000 \\\n  --batch_size=4 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=1 \\\n  --eval_freq=1000\n```\n\n**评测：**\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.max_parallel_tasks=1\n```\n\n---\n\n## 5. 关键注意事项\n\n1. **LIBERO-90 数据** 不在标准预转换数据集中。需要用 OpenPI 转换脚本或社区数据集 `IPEC-COMMUNITY/libero_90_no_noops_lerobot`\n2. **控制模式** (`relative` vs `absolute`) 必须与策略的动作参数化匹配\n3. **vanilla LIBERO 和 LIBERO-Plus 不能同时安装**，两者共用同一 Python 包名\n4. LeRobot 中 LIBERO 仅支持 Linux（MuJoCo 渲染需 EGL）\n5. LeRobot 格式的图像分辨率为 256x256，而原始 LIBERO 为 128x128 [UNVERIFIED — 需确认是否做了上采样或 LeRobot 环境重新渲染]\n6. 原始 LIBERO 采集频率 20Hz，LeRobot 格式为 10Hz（可能做了下采样）[UNVERIFIED — 需确认具体降频策略]\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Assistant

_source line 247_

报告已写入 `artifacts/research_libero_benchmark.md`。

覆盖的内容：
- **LIBERO Benchmark**：GitHub/安装/5 个 task suite 详情/HDF5 数据格式（观测 128x128 双相机 + 7D 关节 + 6D EE，动作 7D OSC_POSE）/评测脚本命令和指标（success rate, FWT, NBT, AUC）
- **LIBERO-Plus**：实际是 7 个扰动维度 21 个子维度（不只是 4 个），含物体布局/相机/机器人初态/语言指令/光照/背景纹理/传感器噪声，CVPR 2026 论文，drop-in replacement 架构
- **数据增强**：robosuite 内置 DomainRandomizationWrapper + 三个 Modder 可直接用；LIBERO-Plus 同时提供 22,400 条增强训练轨迹；传感器噪声为纯图像后处理可零成本复用
- **LeRobot 集成**：原生支持，HuggingFace 上有 `lerobot/libero`、`HuggingFaceVLA/libero` 等预转换数据集，附 OpenPI 转换脚本路径

两处标注了 `[UNVERIFIED]`：LeRobot 格式图像分辨率（256 vs 128）和采样率降频策略。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "uuid": "90d84658-7f4e-4438-bb8a-7d984bf66ad4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9D7EhqfnN1pMNr7WeroNJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9492,
      "cache_read_input_tokens": 34597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9492
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

_source line 248_

报告已写入 `artifacts/research_libero_benchmark.md`。

覆盖的内容：
- **LIBERO Benchmark**：GitHub/安装/5 个 task suite 详情/HDF5 数据格式（观测 128x128 双相机 + 7D 关节 + 6D EE，动作 7D OSC_POSE）/评测脚本命令和指标（success rate, FWT, NBT, AUC）
- **LIBERO-Plus**：实际是 7 个扰动维度 21 个子维度（不只是 4 个），含物体布局/相机/机器人初态/语言指令/光照/背景纹理/传感器噪声，CVPR 2026 论文，drop-in replacement 架构
- **数据增强**：robosuite 内置 DomainRandomizationWrapper + 三个 Modder 可直接用；LIBERO-Plus 同时提供 22,400 条增强训练轨迹；传感器噪声为纯图像后处理可零成本复用
- **LeRobot 集成**：原生支持，HuggingFace 上有 `lerobot/libero`、`HuggingFaceVLA/libero` 等预转换数据集，附 OpenPI 转换脚本路径

两处标注了 `[UNVERIFIED]`：LeRobot 格式图像分辨率（256 vs 128）和采样率降频策略。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 418587,
  "duration_api_ms": 947542,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "2e86c8de-c2a5-4dae-af4d-f49fa73af83b",
  "total_cost_usd": 3.27120475,
  "usage": {
    "input_tokens": 6570,
    "cache_creation_input_tokens": 32248,
    "cache_read_input_tokens": 131702,
    "output_tokens": 11063,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32248,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 415,
        "cache_read_input_tokens": 34597,
        "cache_creation_input_tokens": 9492,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 9492
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 873795,
      "outputTokens": 30370,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 25,
      "costUSD": 1.275645,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14474,
      "outputTokens": 29041,
      "cacheReadInputTokens": 861042,
      "cacheCreationInputTokens": 122663,
      "webSearchRequests": 0,
      "costUSD": 1.99555975,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "6086c990-aa28-46c8-92ea-3f5f10c11d9f"
}
```

</details>

---
