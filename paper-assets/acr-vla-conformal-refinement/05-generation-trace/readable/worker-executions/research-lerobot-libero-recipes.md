# research lerobot libero recipes

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 311
- **Recorded user turns:** 4
- **Tool calls:** 98
- **Original source:** `logs/workers/worker_research_lerobot-libero-recipes_20260513T094527.log`
- **Structured JSON:** [`7657ea5c09ba70bc6fc3.json`](../../sessions/76/7657ea5c09ba70bc6fc3.json)

## Before a recorded user message

11 recorded events

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
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
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
  "uuid": "72d9f14e-32b6-4dff-8a6c-e08ac2427aa0",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1778674800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f52ff875-a7d0-4586-b78b-c94926e3d03a",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to search for information about SmolVLA fine-tuning on LIBERO benchmark. This involves multiple web searches and reading documentation. Let me launch parallel search agents to cover all four search areas efficiently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "4dbe0da0-445d-486f-8c71-012d3403f617",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbXrKm57CYVL3AMAMkaFqc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11496,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11496
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

I'll launch parallel search agents to cover all four areas simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "c37bfac9-c1bb-4f1b-adfb-6ce5788ffad4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbXrKm57CYVL3AMAMkaFqc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11496,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11496
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AUFYVuZ8zwzk2xCany6j1r`</summary>

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
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "994803c8-dfe0-4c02-a1a1-dab8160e4e9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbXrKm57CYVL3AMAMkaFqc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11496,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11496
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

_source line 7 · 2026-05-13T09:45:38.669Z_

<details><summary>↩ Tool result · `toolu_01AUFYVuZ8zwzk2xCany6j1r`</summary>

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
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "cf3724f9-2f9a-452a-95b6-d96863eb11af",
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
Now I have the WebSearch and WebFetch tools available. Let me launch parallel agents to search all four areas simultaneously.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "b12295f1-546d-4d60-a727-11b763f41d26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iibdAVzZFrtjmATWXYt5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 23337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1175
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

Launching 4 parallel search agents now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "3107d248-ed7a-4cbb-97f2-50399b650b16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iibdAVzZFrtjmATWXYt5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 23337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1175
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Agent · `toolu_01MF6koX1EJpEjH7EddZx5wM`</summary>

```json
{
  "description": "Search 1: SmolVLA fine-tuning",
  "prompt": "Search for SmolVLA fine-tuning documentation and examples. This is a VLA (Vision-Language-Action) model from HuggingFace's LeRobot framework, model ID `lerobot/smolvla_base`.\n\nDo the following searches and fetch relevant pages:\n\n1. WebSearch for \"SmolVLA fine-tuning lerobot\"\n2. WebSearch for \"SmolVLA LoRA training recipe\"\n3. WebSearch for \"lerobot smolvla finetune 2025 2026\"\n4. Fetch the HuggingFace model card: https://huggingface.co/lerobot/smolvla_base — extract: model architecture, action dimensions, supported datasets, fine-tuning instructions, training config\n5. Fetch the LeRobot GitHub README: https://github.com/huggingface/lerobot — extract: fine-tuning commands, SmolVLA references, training scripts, example configs\n6. WebSearch for \"lerobot fine-tune guide tutorial\"\n\nFor each result, record:\n- URL\n- Key information (training commands, config files, data format requirements, action_dim)\n- Whether it's directly usable for fine-tuning SmolVLA on a custom dataset\n\nCompile a comprehensive summary of all findings.",
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
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "6cefa9dc-aa4c-4fa6-a29d-a9c9652fcf6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iibdAVzZFrtjmATWXYt5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 23337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1175
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 11_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Search 1: SmolVLA fine-tuning",
  "task_type": "local_agent",
  "prompt": "Search for SmolVLA fine-tuning documentation and examples. This is a VLA (Vision-Language-Action) model from HuggingFace's LeRobot framework, model ID `lerobot/smolvla_base`.\n\nDo the following searches and fetch relevant pages:\n\n1. WebSearch for \"SmolVLA fine-tuning lerobot\"\n2. WebSearch for \"SmolVLA LoRA training recipe\"\n3. WebSearch for \"lerobot smolvla finetune 2025 2026\"\n4. Fetch the HuggingFace model card: https://huggingface.co/lerobot/smolvla_base — extract: model architecture, action dimensions, supported datasets, fine-tuning instructions, training config\n5. Fetch the LeRobot GitHub README: https://github.com/huggingface/lerobot — extract: fine-tuning commands, SmolVLA references, training scripts, example configs\n6. WebSearch for \"lerobot fine-tune guide tutorial\"\n\nFor each result, record:\n- URL\n- Key information (training commands, config files, data format requirements, action_dim)\n- Whether it's directly usable for fine-tuning SmolVLA on a custom dataset\n\nCompile a comprehensive summary of all findings.",
  "uuid": "98ec8b9b-7002-4722-9f8c-ee5ba228591e",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

## Round 1

6 recorded events

### User

_source line 12 · 2026-05-13T09:45:50.924Z_

Search for SmolVLA fine-tuning documentation and examples. This is a VLA (Vision-Language-Action) model from HuggingFace's LeRobot framework, model ID `lerobot/smolvla_base`.

Do the following searches and fetch relevant pages:

1. WebSearch for "SmolVLA fine-tuning lerobot"
2. WebSearch for "SmolVLA LoRA training recipe"
3. WebSearch for "lerobot smolvla finetune 2025 2026"
4. Fetch the HuggingFace model card: https://huggingface.co/lerobot/smolvla_base — extract: model architecture, action dimensions, supported datasets, fine-tuning instructions, training config
5. Fetch the LeRobot GitHub README: https://github.com/huggingface/lerobot — extract: fine-tuning commands, SmolVLA references, training scripts, example configs
6. WebSearch for "lerobot fine-tune guide tutorial"

For each result, record:
- URL
- Key information (training commands, config files, data format requirements, action_dim)
- Whether it's directly usable for fine-tuning SmolVLA on a custom dataset

Compile a comprehensive summary of all findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "ef5e8dda-2ae4-4fdf-8c14-cdd7d7090b0b"
}
```

</details>

---

### System

_source line 13_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Search 1: SmolVLA fine-tuning",
  "usage": {
    "total_tokens": 14318,
    "tool_uses": 1,
    "duration_ms": 2273
  },
  "last_tool_name": "ToolSearch",
  "uuid": "abdc5393-07a3-4b99-9840-db79e330e72c",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Q9FwXSnSgBvRsg3Tryf8tP`</summary>

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
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "e237c42e-dc47-44fc-a719-b77a9b6ce1d9",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FTUrdkFQRi1yLm8KJsEbbj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14251,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14251,
        "ephemeral_1h_input_tokens": 0
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

_source line 15 · 2026-05-13T09:45:53.202Z_

<details><summary>↩ Tool result · `toolu_01Q9FwXSnSgBvRsg3Tryf8tP`</summary>

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
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "d8456ea6-db05-404b-b6ab-0b7f2d499192"
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Agent · `toolu_01DNpWqbVCTPcK6hFAJ5pLB7`</summary>

```json
{
  "description": "Search 2: LeRobot + LIBERO",
  "prompt": "Search for how to use LIBERO benchmark datasets with HuggingFace LeRobot framework. LIBERO is a robot manipulation benchmark with multiple task suites (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90).\n\nDo the following searches and fetch relevant pages:\n\n1. WebSearch for \"lerobot LIBERO dataset\"\n2. WebSearch for \"convert LIBERO to lerobot format\"\n3. WebSearch for \"lerobot LIBERO fine-tune\"\n4. WebSearch for \"huggingface lerobot libero 2025 2026\"\n5. WebSearch for \"LIBERO dataset huggingface hub\"\n6. Check if LIBERO datasets exist on HuggingFace Hub by searching: \"site:huggingface.co LIBERO lerobot dataset\"\n\nFor any relevant results, fetch the pages and extract:\n- How to convert LIBERO HDF5 data to LeRobot dataset format\n- Whether there are pre-converted LIBERO datasets on HuggingFace Hub\n- Any conversion scripts or tools\n- Data format details (observation keys, action dimensions, episode structure)\n\nCompile a comprehensive summary of all findings with URLs.",
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
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "856d897f-0d87-4363-acdb-885967717b17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iibdAVzZFrtjmATWXYt5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 23337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1175
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "description": "Search 2: LeRobot + LIBERO",
  "task_type": "local_agent",
  "prompt": "Search for how to use LIBERO benchmark datasets with HuggingFace LeRobot framework. LIBERO is a robot manipulation benchmark with multiple task suites (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90).\n\nDo the following searches and fetch relevant pages:\n\n1. WebSearch for \"lerobot LIBERO dataset\"\n2. WebSearch for \"convert LIBERO to lerobot format\"\n3. WebSearch for \"lerobot LIBERO fine-tune\"\n4. WebSearch for \"huggingface lerobot libero 2025 2026\"\n5. WebSearch for \"LIBERO dataset huggingface hub\"\n6. Check if LIBERO datasets exist on HuggingFace Hub by searching: \"site:huggingface.co LIBERO lerobot dataset\"\n\nFor any relevant results, fetch the pages and extract:\n- How to convert LIBERO HDF5 data to LeRobot dataset format\n- Whether there are pre-converted LIBERO datasets on HuggingFace Hub\n- Any conversion scripts or tools\n- Data format details (observation keys, action dimensions, episode structure)\n\nCompile a comprehensive summary of all findings with URLs.",
  "uuid": "30a58e58-5365-49ca-af6c-c71e18c2af4d",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

## Round 2

24 recorded events

### User

_source line 18 · 2026-05-13T09:45:53.428Z_

Search for how to use LIBERO benchmark datasets with HuggingFace LeRobot framework. LIBERO is a robot manipulation benchmark with multiple task suites (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90).

Do the following searches and fetch relevant pages:

1. WebSearch for "lerobot LIBERO dataset"
2. WebSearch for "convert LIBERO to lerobot format"
3. WebSearch for "lerobot LIBERO fine-tune"
4. WebSearch for "huggingface lerobot libero 2025 2026"
5. WebSearch for "LIBERO dataset huggingface hub"
6. Check if LIBERO datasets exist on HuggingFace Hub by searching: "site:huggingface.co LIBERO lerobot dataset"

For any relevant results, fetch the pages and extract:
- How to convert LIBERO HDF5 data to LeRobot dataset format
- Whether there are pre-converted LIBERO datasets on HuggingFace Hub
- Any conversion scripts or tools
- Data format details (observation keys, action dimensions, episode structure)

Compile a comprehensive summary of all findings with URLs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "40f667a0-530f-46b5-b386-379eeb6e0fa4"
}
```

</details>

---

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "description": "Search 2: LeRobot + LIBERO",
  "usage": {
    "total_tokens": 14310,
    "tool_uses": 1,
    "duration_ms": 2025
  },
  "last_tool_name": "ToolSearch",
  "uuid": "7b52605a-13d2-4510-9d5f-b822a4c031ed",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### System

_source line 20_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Searching for SmolVLA fine-tuning lerobot 2025 2026",
  "usage": {
    "total_tokens": 16255,
    "tool_uses": 2,
    "duration_ms": 4844
  },
  "last_tool_name": "WebSearch",
  "uuid": "0b07ca4b-fd87-4874-93a0-921d7f82667c",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Searching for SmolVLA LoRA training recipe lerobot",
  "usage": {
    "total_tokens": 16256,
    "tool_uses": 3,
    "duration_ms": 5204
  },
  "last_tool_name": "WebSearch",
  "uuid": "24440a73-9ff5-43bd-87be-f3b94dc998ea",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Searching for lerobot smolvla finetune 2025 2026",
  "usage": {
    "total_tokens": 16257,
    "tool_uses": 4,
    "duration_ms": 5673
  },
  "last_tool_name": "WebSearch",
  "uuid": "5a650a08-1baf-4ed0-832d-1ce4aa6948f1",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Searching for lerobot fine-tune guide tutorial custom dataset 2…",
  "usage": {
    "total_tokens": 16258,
    "tool_uses": 5,
    "duration_ms": 6046
  },
  "last_tool_name": "WebSearch",
  "uuid": "8f97f814-2b12-4be7-a479-150b94f63878",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Fetching https://huggingface.co/lerobot/smolvla_base",
  "usage": {
    "total_tokens": 16259,
    "tool_uses": 6,
    "duration_ms": 7336
  },
  "last_tool_name": "WebFetch",
  "uuid": "7b4d9670-6261-4f54-afe1-f17f11a100b8",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "description": "Searching for lerobot LIBERO dataset",
  "usage": {
    "total_tokens": 16247,
    "tool_uses": 2,
    "duration_ms": 4989
  },
  "last_tool_name": "WebSearch",
  "uuid": "83665b6a-3ab0-4f34-bcaf-851af2b5bfdd",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "description": "Searching for convert LIBERO to lerobot format",
  "usage": {
    "total_tokens": 16248,
    "tool_uses": 3,
    "duration_ms": 5439
  },
  "last_tool_name": "WebSearch",
  "uuid": "09e818ff-3a10-4c58-9123-dffa1cdfde1e",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "description": "Searching for lerobot LIBERO fine-tune",
  "usage": {
    "total_tokens": 16249,
    "tool_uses": 4,
    "duration_ms": 5448
  },
  "last_tool_name": "WebSearch",
  "uuid": "556061e6-aeee-4709-ad79-6d822361aa6b",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UWXraCrnssktSF62C7ZbQ4`</summary>

```json
{
  "query": "SmolVLA fine-tuning lerobot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "0041492b-e92d-4bd1-8738-5216f655f6a4",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SuX1CgFBbmdnCG5gS4Upr8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PAtb28Tcc1B6qXrftoqPa2`</summary>

```json
{
  "query": "SmolVLA LoRA training recipe lerobot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "3e159a4f-c5ba-4be0-8278-665743fa88e6",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SuX1CgFBbmdnCG5gS4Upr8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017yTzcT1Z9UoLatHJeKvJGG`</summary>

```json
{
  "query": "lerobot smolvla finetune 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "6209a8b9-941e-4895-8df5-6bd59b633056",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SuX1CgFBbmdnCG5gS4Upr8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GxEeRR5XX6QQuxecHERzT5`</summary>

```json
{
  "query": "lerobot fine-tune guide tutorial custom dataset 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "ff379ab9-3995-45f6-8c80-5469951277e5",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SuX1CgFBbmdnCG5gS4Upr8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HUqwwKXFEM6j3s8NWQj4TM`</summary>

```json
{
  "url": "https://huggingface.co/lerobot/smolvla_base",
  "prompt": "Extract: model architecture, action dimensions, supported datasets, fine-tuning instructions, training config, observation/action space details, any commands or code examples"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "6d0c4a30-e031-4370-98f1-3112fb3fac1b",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SuX1CgFBbmdnCG5gS4Upr8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MA7KLWm4PvNsMAA3s8ks7v`</summary>

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
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "11c4fbe9-1f43-4f7f-acb0-cbb1daa6db9b",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01B46UYbpy2RGrTrpG3F5SYw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6125,
      "cache_read_input_tokens": 8118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6125,
        "ephemeral_1h_input_tokens": 0
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

_source line 34 · 2026-05-13T09:45:55.456Z_

<details><summary>↩ Tool result · `toolu_01MA7KLWm4PvNsMAA3s8ks7v`</summary>

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
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "e1bedbf0-5fdf-476b-bf2d-13f2d8dab813"
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T1Us2S9z7V2jMZEBcbKKNZ`</summary>

```json
{
  "query": "lerobot LIBERO dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "b24ac16d-c756-4c7f-b14c-f89451c16305",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KeVqGSFdvzr5Vvq2WMdQ9r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012DkqxYQE93NCDZe1tbLN8N`</summary>

```json
{
  "query": "convert LIBERO to lerobot format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "b8274fef-9395-4781-a965-bfdc50afac98",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KeVqGSFdvzr5Vvq2WMdQ9r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019ywQ9EMmuPVMDRAj8mLBqh`</summary>

```json
{
  "query": "lerobot LIBERO fine-tune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "b4f00572-b192-4ef6-9fe3-c7342c471752",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KeVqGSFdvzr5Vvq2WMdQ9r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Fetching https://github.com/huggingface/lerobot",
  "usage": {
    "total_tokens": 16260,
    "tool_uses": 7,
    "duration_ms": 8154
  },
  "last_tool_name": "WebFetch",
  "uuid": "a6495688-257f-45ee-b52d-7d45decd9812",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01N2XX24RDqHhPyXNeXpxzqJ`</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot",
  "prompt": "Extract: fine-tuning commands, SmolVLA references, training scripts, example configs, data format requirements, any commands for training or fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "da221df8-9b82-43fe-8f19-77fb4ffc941e",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SuX1CgFBbmdnCG5gS4Upr8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Agent · `toolu_01EGZ1QZXBAfBeNAZjF5tKUZ`</summary>

```json
{
  "description": "Search 3: SmolVLA action dims",
  "prompt": "Search for SmolVLA's action dimension specification and architecture details. SmolVLA is a Vision-Language-Action model from HuggingFace LeRobot. We need to understand its action space (especially whether it uses 6D or 7D actions, and how the gripper action is handled).\n\nDo the following searches:\n\n1. WebSearch for \"SmolVLA action dimension architecture\"\n2. WebSearch for \"SmolVLA 7D action gripper\"\n3. WebSearch for \"SmolVLA paper arxiv\"\n4. WebSearch for \"SmolVLA action space configuration\"\n5. WebSearch for \"lerobot action_dim smolvla config\"\n6. If you find a paper or technical report, fetch it and extract the action space details\n\nAlso search for LIBERO's action space:\n7. WebSearch for \"LIBERO benchmark action space dimension\"\n8. WebSearch for \"LIBERO 7D action delta position\"\n\nFor each result, record:\n- URL\n- Action dimension details (what each dimension represents)\n- How to configure action_dim when fine-tuning\n- Any mismatch between SmolVLA's default action space and LIBERO's action space\n\nCompile findings about both SmolVLA and LIBERO action spaces, and analyze compatibility.",
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
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "85ad3dca-803d-4827-9b30-192d35b7a6ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iibdAVzZFrtjmATWXYt5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 23337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1175
      },
      "output_tokens": 32,
      "service_tier": "standard",
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
  "subtype": "task_started",
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Search 3: SmolVLA action dims",
  "task_type": "local_agent",
  "prompt": "Search for SmolVLA's action dimension specification and architecture details. SmolVLA is a Vision-Language-Action model from HuggingFace LeRobot. We need to understand its action space (especially whether it uses 6D or 7D actions, and how the gripper action is handled).\n\nDo the following searches:\n\n1. WebSearch for \"SmolVLA action dimension architecture\"\n2. WebSearch for \"SmolVLA 7D action gripper\"\n3. WebSearch for \"SmolVLA paper arxiv\"\n4. WebSearch for \"SmolVLA action space configuration\"\n5. WebSearch for \"lerobot action_dim smolvla config\"\n6. If you find a paper or technical report, fetch it and extract the action space details\n\nAlso search for LIBERO's action space:\n7. WebSearch for \"LIBERO benchmark action space dimension\"\n8. WebSearch for \"LIBERO 7D action delta position\"\n\nFor each result, record:\n- URL\n- Action dimension details (what each dimension represents)\n- How to configure action_dim when fine-tuning\n- Any mismatch between SmolVLA's default action space and LIBERO's action space\n\nCompile findings about both SmolVLA and LIBERO action spaces, and analyze compatibility.",
  "uuid": "731f606f-6cfd-409d-9b78-480ee5442ee5",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

## Round 3

14 recorded events

### User

_source line 42 · 2026-05-13T09:45:59.418Z_

Search for SmolVLA's action dimension specification and architecture details. SmolVLA is a Vision-Language-Action model from HuggingFace LeRobot. We need to understand its action space (especially whether it uses 6D or 7D actions, and how the gripper action is handled).

Do the following searches:

1. WebSearch for "SmolVLA action dimension architecture"
2. WebSearch for "SmolVLA 7D action gripper"
3. WebSearch for "SmolVLA paper arxiv"
4. WebSearch for "SmolVLA action space configuration"
5. WebSearch for "lerobot action_dim smolvla config"
6. If you find a paper or technical report, fetch it and extract the action space details

Also search for LIBERO's action space:
7. WebSearch for "LIBERO benchmark action space dimension"
8. WebSearch for "LIBERO 7D action delta position"

For each result, record:
- URL
- Action dimension details (what each dimension represents)
- How to configure action_dim when fine-tuning
- Any mismatch between SmolVLA's default action space and LIBERO's action space

Compile findings about both SmolVLA and LIBERO action spaces, and analyze compatibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "2a79b8f5-493a-4c3d-81ab-4f8ee8cf9a7d"
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
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Search 3: SmolVLA action dims",
  "usage": {
    "total_tokens": 14314,
    "tool_uses": 1,
    "duration_ms": 2140
  },
  "last_tool_name": "ToolSearch",
  "uuid": "55a97348-fec0-4461-8149-e4a588dea370",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Searching for SmolVLA action dimension architecture",
  "usage": {
    "total_tokens": 16251,
    "tool_uses": 2,
    "duration_ms": 4836
  },
  "last_tool_name": "WebSearch",
  "uuid": "00ef2e01-80b3-428f-a96d-59b49b855921",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool result

_source line 45 · 2026-05-13T09:46:02.993Z_

<details><summary>↩ Tool result · `toolu_01UWXraCrnssktSF62C7ZbQ4`</summary>

```text
Web search results for query: "SmolVLA fine-tuning lerobot 2025 2026"

Links: [{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"SmolVLA fine-tuning | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/"},{"title":"GitHub - huggingface/VLAb · GitHub","url":"https://github.com/huggingface/VLAb"}]

I found comprehensive information about SmolVLA fine-tuning with LeRobot. Here are the key findings:

## SmolVLA Overview

SmolVLA is a compact (450M), open-source Vision-Language-Action model for robotics that runs on consumer hardware. It's designed as a base model to fine-tune on your specific use case.

## Fine-tuning Process

You can use smolvla_base, a pretrained 450M model, and fine-tune it on your data. Training for 20k steps will roughly take ~4 hours on a single A100 GPU, though you should tune the number of steps based on performance and your use-case.

SmolVLA is a base model that requires fine-tuning on your own data for optimal performance in your setup, with about 50 episodes of your task recommended as a starting point.

## Training Details

For fine-tuning on simulation benchmarks, training is done for 100,000 steps with a batch size of 64, while for real-world tasks, fine-tuning is done for 200,000 steps. During training, only the action expert module is trained, keeping the VLM frozen.

## Real-world Results

After pretraining on community-collected data, performance improves to 78.3%, showing a +26.6% absolute improvement, with multitask finetuning further boosting performance.

The search results show active development and documentation throughout 2025 and into 2026, with practical tutorials and implementation guides available for users looking to fine-tune SmolVLA on LeRobot.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "3ff1272f-5d5b-4131-ad74-dcc133cf3364"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-13T09:46:03.093Z_

<details><summary>↩ Tool result · `toolu_017yTzcT1Z9UoLatHJeKvJGG`</summary>

```text
Web search results for query: "lerobot smolvla finetune 2025 2026"

Links: [{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"lerobot/docs/source/smolvla.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"Finetune smolvla with vision encoder · Issue #1774 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1774"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"How to evaluate finetuned SmolVLA model · Issue #1446 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1446"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"}]

Based on the web search results, here's what I found about SmolVLA finetuning in the LeRobot framework:

## SmolVLA Overview

SmolVLA is a compact (450M), open-source Vision-Language-Action model for robotics that runs on consumer hardware. It is pretrained only on compatibly licensed, open-source community-shared datasets under the lerobot tag.

## Finetuning SmolVLA

You can use smolvla_base, the pretrained 450M model, and fine-tune it on your data. Training the model for 20k steps will roughly take ~4 hrs on a single A100 GPU. You should tune the number of steps based on performance and your use-case.

SmolVLA is a base model, so fine-tuning on your own data is required for optimal performance in your setup. It is recommended to record ~50 episodes of your task as a starting point.

## Performance

After pretraining on community-collected data, performance jumps to 78.3%, a +26.6% absolute improvement. Multitask finetuning further boosts performance, showing strong task transfer capabilities even in low-data regimes.

## Community Adoption

The search results show active community engagement with SmolVLA finetuning through 2025-2026, with users sharing their experiences and challenges on platforms like GitHub, HuggingFace, and Medium.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "e45ed39a-ac98-4d22-a99f-163dd34ef5a0"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-13T09:46:03.605Z_

<details><summary>↩ Tool result · `toolu_01PAtb28Tcc1B6qXrftoqPa2`</summary>

```text
Web search results for query: "SmolVLA LoRA training recipe lerobot"

Links: [{"title":"lerobot/docs/source/peft_training.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/peft_training.mdx"},{"title":"Towards Accessible Physical AI: LoRA-Based Fine-Tuning of VLA Models for Real-World Robot Control","url":"https://arxiv.org/html/2512.11921v1"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"VLA-0-Smol","url":"https://robot-learning-collective.github.io/vla-0-smol"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"Parameter efficient fine-tuning with 🤗 PEFT","url":"https://huggingface.co/docs/lerobot/en/peft_training"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"LeRobot datasets and training | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/"},{"title":"Training SmolVLA with LeRobot Notebook - Colab - Google","url":"https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb"}]

Based on the search results, I found comprehensive information about SmolVLA LoRA training with LeRobot:

## SmolVLA LoRA Training Recipe with LeRobot

🤗 PEFT (Parameter-Efficient Fine-Tuning) is a library for efficiently adapting large pretrained models such as SmolVLA to new tasks without training all of the model's parameters while yielding comparable performance.

### Basic Training Command

Here's an example training command: `lerobot-train --policy.path=lerobot/smolvla_base --policy.repo_id=your_hub_name/my_libero_smolvla --dataset.repo_id=HuggingFaceVLA/libero --policy.output_features=null --policy.input_features=null --policy.optimizer_lr=1e-3 --policy.scheduler_decay_lr=1e-4 --env.type=libero --env.task=libero_spatial --steps=100000 --batch_size=32 --peft.method_type=LORA --peft.r=64`

### LoRA Configuration

LoRA (Low-Rank Adapter) is probably the most popular fine-tuning method to date. Low-rank adaption means that we only fine-tune a matrix with comparably low rank instead of the full weight matrix. This rank can be specified using the --peft.r parameter.

### Layer Targeting

By default, PEFT will target the q_proj and v_proj layers of the LM expert in SmolVLA. It will also target the state and action projection matrices as they are most likely task-dependent. If you need to target different layers you can use --peft.target_modules to specify which layers to target.

### Hardware Requirements

A combination of Low-Rank Adaptation (LoRA) and 4-bit quantization enables training and inference on consumer-grade GPUs with 8GB VRAM.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "e43b0f8b-b8b2-4fb9-815b-d1949c5c0701"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-13T09:46:04.212Z_

<details><summary>↩ Tool result · `toolu_01T1Us2S9z7V2jMZEBcbKKNZ`</summary>

```text
Web search results for query: "lerobot LIBERO dataset"

Links: [{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"physical-intelligence/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/physical-intelligence/libero"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"lerobot/docs/source/libero.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/libero.mdx"},{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"lerobot · PyPI","url":"https://pypi.org/project/lerobot/"},{"title":"https://raw.githubusercontent.com/Physical-Intelli...","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"openpi/examples/libero/convert_libero_data_to_lerobot.py at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"any4lerobot/libero2lerobot/README.md at main · Tavish9/any4lerobot","url":"https://github.com/Tavish9/any4lerobot/blob/main/libero2lerobot/README.md"}]

Based on the search results, here's what I found about the LeRobot LIBERO dataset:

## Overview

LIBERO is designed for studying knowledge transfer in multitask and lifelong robot learning problems. The repository is now maintained by the Hugging Face team, with modifications for compatibility with LeRobot, simplified installation, and large-scale robotics experiments.

## Dataset Contents

LIBERO provides 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100. The first three task suites have controlled distribution shifts, meaning that they require the transfer of a specific type of knowledge, while LIBERO-100 consists of 100 manipulation tasks that require the transfer of entangled knowledge.

High-quality human teleoperation demonstrations are provided for the four task suites in LIBERO.

## Integration with LeRobot

A preprocessed LIBERO dataset is provided that is fully compatible with the current LeRobot codebase and requires no additional manipulation. The dataset combines four individual Libero datasets: Libero-Spatial, Libero-Object, Libero-Goal and Libero-10, which were converted into LeRobot format.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "39829038-d21b-4589-a205-cb0ef5832aa0"
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DHBqvDBo3jdSRE53w9DTnV`</summary>

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
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "45e7af38-fcef-4c67-8214-785c6c3a99c8",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HaSbvdKmVujKSgZmSdwtMi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6129,
      "cache_read_input_tokens": 8118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6129,
        "ephemeral_1h_input_tokens": 0
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

_source line 50 · 2026-05-13T09:46:01.560Z_

<details><summary>↩ Tool result · `toolu_01DHBqvDBo3jdSRE53w9DTnV`</summary>

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
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "d7aa6bc0-0d08-4e9c-8df4-03ef365dccca"
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GVk8eirQBF8En2h291Ez48`</summary>

```json
{
  "query": "SmolVLA action dimension architecture"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "7dd52278-6841-4b21-a372-e6146db734cf",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NvsUs49nLkBTPygdNqbX7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Searching for SmolVLA 7D action gripper",
  "usage": {
    "total_tokens": 16252,
    "tool_uses": 3,
    "duration_ms": 5220
  },
  "last_tool_name": "WebSearch",
  "uuid": "adf2b377-f8d0-40a4-94f4-31c8b2ce080c",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GD1GCgigBaDwBkfaf9kmb9`</summary>

```json
{
  "query": "SmolVLA 7D action gripper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "c2b07e21-ad91-4a87-a78f-6bd77eca3118",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NvsUs49nLkBTPygdNqbX7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Agent · `toolu_01CR7kykRBUTiYTQ3U6bGTyJ`</summary>

```json
{
  "description": "Search 4: VLA + LIBERO prior work",
  "prompt": "Search for existing work on fine-tuning VLA (Vision-Language-Action) models on LIBERO benchmark. We want to know if anyone has already done this and what results they got.\n\nDo the following searches:\n\n1. WebSearch for \"OpenVLA LIBERO fine-tune\"\n2. WebSearch for \"VLA fine-tune LIBERO benchmark\"\n3. WebSearch for \"LIBERO fine-tuned VLA checkpoint\"\n4. WebSearch for \"OpenVLA LIBERO results 2025 2026\"\n5. WebSearch for \"pi0 LIBERO\" (Physical Intelligence's model)\n6. WebSearch for \"octo LIBERO fine-tune\"\n7. WebSearch for \"RT-2 LIBERO\" or \"diffusion policy LIBERO\"\n\nFor any relevant papers or blog posts, fetch and extract:\n- Model name and architecture\n- Fine-tuning method (full, LoRA, etc.)\n- LIBERO task suites used\n- Results/success rates\n- Training details (epochs, learning rate, batch size, GPU hours)\n- Whether checkpoints are publicly available\n- Action space configuration used\n\nCompile a comprehensive summary of all VLA + LIBERO prior work, with URLs and key results.",
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
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "d97066d6-d031-4268-98cb-bd3d2fee188b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iibdAVzZFrtjmATWXYt5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 23337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1175
      },
      "output_tokens": 32,
      "service_tier": "standard",
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
  "subtype": "task_started",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Search 4: VLA + LIBERO prior work",
  "task_type": "local_agent",
  "prompt": "Search for existing work on fine-tuning VLA (Vision-Language-Action) models on LIBERO benchmark. We want to know if anyone has already done this and what results they got.\n\nDo the following searches:\n\n1. WebSearch for \"OpenVLA LIBERO fine-tune\"\n2. WebSearch for \"VLA fine-tune LIBERO benchmark\"\n3. WebSearch for \"LIBERO fine-tuned VLA checkpoint\"\n4. WebSearch for \"OpenVLA LIBERO results 2025 2026\"\n5. WebSearch for \"pi0 LIBERO\" (Physical Intelligence's model)\n6. WebSearch for \"octo LIBERO fine-tune\"\n7. WebSearch for \"RT-2 LIBERO\" or \"diffusion policy LIBERO\"\n\nFor any relevant papers or blog posts, fetch and extract:\n- Model name and architecture\n- Fine-tuning method (full, LoRA, etc.)\n- LIBERO task suites used\n- Results/success rates\n- Training details (epochs, learning rate, batch size, GPU hours)\n- Whether checkpoints are publicly available\n- Action space configuration used\n\nCompile a comprehensive summary of all VLA + LIBERO prior work, with URLs and key results.",
  "uuid": "41655b72-91b3-459d-a89b-238792006bb8",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

## Round 4

256 recorded events

### User

_source line 56 · 2026-05-13T09:46:04.690Z_

Search for existing work on fine-tuning VLA (Vision-Language-Action) models on LIBERO benchmark. We want to know if anyone has already done this and what results they got.

Do the following searches:

1. WebSearch for "OpenVLA LIBERO fine-tune"
2. WebSearch for "VLA fine-tune LIBERO benchmark"
3. WebSearch for "LIBERO fine-tuned VLA checkpoint"
4. WebSearch for "OpenVLA LIBERO results 2025 2026"
5. WebSearch for "pi0 LIBERO" (Physical Intelligence's model)
6. WebSearch for "octo LIBERO fine-tune"
7. WebSearch for "RT-2 LIBERO" or "diffusion policy LIBERO"

For any relevant papers or blog posts, fetch and extract:
- Model name and architecture
- Fine-tuning method (full, LoRA, etc.)
- LIBERO task suites used
- Results/success rates
- Training details (epochs, learning rate, batch size, GPU hours)
- Whether checkpoints are publicly available
- Action space configuration used

Compile a comprehensive summary of all VLA + LIBERO prior work, with URLs and key results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "3f8eb554-28c0-409c-98b0-2cef1a80cb71"
}
```

</details>

---

### System

_source line 57_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Searching for SmolVLA paper arxiv 2026",
  "usage": {
    "total_tokens": 16253,
    "tool_uses": 4,
    "duration_ms": 5598
  },
  "last_tool_name": "WebSearch",
  "uuid": "f49ec443-2fea-4abd-a4aa-b3f20a586cdc",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SRDYLxKAEeZLhKJyoBUh1j`</summary>

```json
{
  "query": "SmolVLA paper arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "f767be00-b0da-4503-8ce6-c692a0bf82ef",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NvsUs49nLkBTPygdNqbX7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 59 · 2026-05-13T09:46:05.151Z_

<details><summary>↩ Tool result · `toolu_019ywQ9EMmuPVMDRAj8mLBqh`</summary>

```text
Web search results for query: "lerobot LIBERO fine-tune"

Links: [{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"lerobot/pi05_libero_finetuned · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned"},{"title":"lerobot/pi05_libero_finetuned_v044 · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned_v044"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"X-VLA: The First Soft-Prompted Robot Foundation Model for Any Robot, Any Task","url":"https://huggingface.co/docs/lerobot/en/xvla"},{"title":"lerobot/docs/source/libero.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/libero.mdx"},{"title":"lerobot/pi05_libero_base · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_base"},{"title":"lerobot/pi05_libero_finetuned_quantiles_v044 · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned_quantiles_v044"},{"title":"jirufengyu/openpi · Hugging Face","url":"https://huggingface.co/jirufengyu/openpi"}]

Based on the search results, here's what I found about LeRobot LIBERO fine-tuning:

## Overview

LeRobotLiberoDataConfig defines how to process raw LIBERO data from LeRobot dataset for training. LeRobot provides comprehensive support for fine-tuning models on the LIBERO benchmark, which is a robot manipulation simulation environment.

## Fine-tuning Process

The Physical Intelligence LIBERO base model (pi05_libero) was fine-tuned for an additional 6k steps in bfloat16, with batch size of 256 on 8 H100 GPUs using the HuggingFace LIBERO dataset. The fine-tuned model is available as lerobot/pi05_libero_finetuned.

## Data Preparation Steps

The fine-tuning process involves three main steps:

1. **Data Conversion**: A minimal example script for converting LIBERO data to a LeRobot dataset is provided in examples/libero/convert_libero_data_to_lerobot.py.

2. **Computing Normalization Statistics**: Before running training, you need to compute normalization statistics for the training data by running a script with your training config name.

3. **Training**: Training is kicked off with the train.py script, which logs training progress to console and saves checkpoints to the checkpoints directory.

## Available Models

Example fine-tuning configs are provided for π₀, π₀-FAST, and π₀.₅ on LIBERO data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "4e379755-10cb-4906-a11e-192ef8dbceab"
}
```

</details>

---

### System

_source line 60_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Searching for SmolVLA action space configuration",
  "usage": {
    "total_tokens": 16254,
    "tool_uses": 5,
    "duration_ms": 5979
  },
  "last_tool_name": "WebSearch",
  "uuid": "21bd5252-a681-4401-babd-958684f374a1",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016RVQJafugAoAuvdVoiYTw3`</summary>

```json
{
  "query": "SmolVLA action space configuration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "e504b910-2857-4ea9-a124-46a7579c3c3c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NvsUs49nLkBTPygdNqbX7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 62 · 2026-05-13T09:46:05.412Z_

<details><summary>↩ Tool result · `toolu_01N2XX24RDqHhPyXNeXpxzqJ`</summary>

````text
# LeRobot Training & Fine-tuning Commands

## Training Command

The primary training command uses configuration-based parameters:

```bash
lerobot-train \
  --policy=act \
  --dataset.repo_id=lerobot/aloha_mobile_cabinet
```

This demonstrates the basic syntax for initiating policy training with a specified model architecture and dataset source.

## Evaluation Command

For testing trained policies:

```bash
lerobot-eval \
  --policy.path=lerobot/pi0_libero_finetuned \
  --env.type=libero \
  --env.task=libero_object \
  --eval.n_episodes=10
```

## Available Policy Types

The framework supports multiple model categories suitable for training:

- **Imitation Learning**: ACT, Diffusion, VQ-BeT, Multitask DiT
- **Reinforcement Learning**: HIL-SERL, TDMPC
- **Vision-Language-Action (VLA)**: Pi0Fast, Pi0.5, GR00T N1.5, SmolVLA, XVLA

## Data Format

The **LeRobotDataset** format uses "synchronized MP4 videos (or images) for vision and Parquet files for state/action data," enabling standardized dataset sharing across the Hugging Face Hub.

## Installation

```bash
pip install lerobot
```

The documentation provides GPU/RAM requirements and expected training duration per policy type through the Compute Hardware Guide.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "b76e5eb9-8f00-4ffa-aef6-dc62b74b580c"
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-13T09:46:05.570Z_

<details><summary>↩ Tool result · `toolu_01GxEeRR5XX6QQuxecHERzT5`</summary>

```text
Web search results for query: "lerobot fine-tune guide tutorial custom dataset 2025 2026"

Links: [{"title":"A Practical Guide to Fine-Tuning and Inference with GR00T N1 & LeRobot on a Custom Dataset - DEV Community","url":"https://dev.to/yuk6ra/a-practical-guide-to-fine-tuning-and-inference-with-gr00t-n1-lerobot-on-a-custom-dataset-52ec"},{"title":"Pi0 and Pi0.5 model fine-tuning guide | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/Pi0/"},{"title":"Tutorial: Fine-tuning on LeRobot V2.1 Dataset","url":"https://github.com/InternRobotics/InternVLA-A1/blob/master/tutorials/finetune_on_lerobot_v21_dataset.md"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"LeRobot datasets and training | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/"},{"title":"Fine-Tuning GR00T N1.5 with Phosphobot and a LeRobot SO-100/101 Arm - HackMD","url":"https://hackmd.io/@johnnynunez/HkcuHewaex"},{"title":"Getting Started with LeRobot | ReductStore","url":"https://www.reduct.store/blog/hugging-face-lerobot"},{"title":"LeRobotDataset v3.0 · Hugging Face","url":"https://huggingface.co/docs/lerobot/lerobot-dataset-v3"},{"title":"How to make a custom LeRobotDataset with v2? · Issue #547 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/547"},{"title":"lerobot · PyPI","url":"https://pypi.org/project/lerobot/"}]

I found several helpful resources on LeRobot fine-tuning with custom datasets. Here are the key results:

## Practical Guides & Tutorials

1. **GR00T N1 & LeRobot Fine-Tuning Guide** (July 2025): A comprehensive, step-by-step guide to fine-tuning the GR00T N1 model, running inference on a physical robot, and evaluating the trained model. This covers environment setup, fine-tuning with custom data, inference on physical robots, and evaluation of trained models.

2. **GR00T N1.5 with SO-100 Fine-Tuning** (October 2025): A guide outlining the complete process to fine-tune NVIDIA's GR00T N1.5 model using a custom dataset captured with Phosphobot on a LeRobot SO-100 robotic arm, with essential fixes and patches for real-world setup.

3. **InternVLA-A1 Fine-Tuning Tutorial**: A tutorial for fine-tuning InternVLA-A1-3B with real-world dataset in LeRobot V2.1 format involving downloading a dataset, converting it to v3.0 format, and fine-tuning on specific tasks.

## Dataset Format & Setup

LeRobotDataset format uses synchronized MP4 videos (or images) for vision and Parquet files for state/action data. LeRobotDataset v3.0 is a standardized format providing unified access to multi-modal time-series data, sensorimotor signals and multi‑camera video, as well as rich metadata.

## Training Command

You can train using: `lerobot-train --policy=act --dataset.repo_id=lerobot/aloha_mobile_cabinet`

Would you like more specific information about any particular aspect of LeRobot fine-tuning?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "b2f6fd7f-26ef-4cb4-b9e4-8062bc2b4dc9"
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-13T09:46:05.576Z_

<details><summary>↩ Tool result · `toolu_012DkqxYQE93NCDZe1tbLN8N`</summary>

```text
Web search results for query: "convert LIBERO to lerobot format"

Links: [{"title":"openpi/examples/libero/convert_libero_data_to_lerobot.py at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"https://raw.githubusercontent.com/Physical-Intelli...","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/convert_libero_data_to_lerobot.py"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"IPEC-COMMUNITY/libero_90_no_noops_lerobot · Dataset converted ideas","url":"https://huggingface.co/datasets/IPEC-COMMUNITY/libero_90_no_noops_lerobot/discussions/2"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"any4lerobot/libero2lerobot/README.md at main · Tavish9/any4lerobot","url":"https://github.com/Tavish9/any4lerobot/blob/main/libero2lerobot/README.md"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"jirufengyu/openpi · Hugging Face","url":"https://huggingface.co/jirufengyu/openpi"},{"title":"lerobot · PyPI","url":"https://pypi.org/project/lerobot/"},{"title":"lerobot/docs/source/libero.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/libero.mdx"}]

Based on the search results, here are the main approaches to convert LIBERO to LeRobot format:

## Official Conversion Script

The Physical Intelligence team provides a minimal example script for converting LIBERO datasets to LeRobot format, which can be run with `uv run examples/libero/convert_libero_data_to_lerobot.py --data_dir /path/to/your/data --push_to_hub`. This conversion script takes approximately 30 minutes to run.

## Alternative Conversion Tool

An alternative tool called any4lerobot can be used to convert datasets from LIBERO hdf5 data to LeRobot format, and has been tested on LIBERO 10, spatial, goal and object datasets.

## Using Pre-converted Datasets

If you prefer not to convert the data yourself, a preprocessed LIBERO dataset fully compatible with LeRobot is available at HuggingFaceVLA/libero.

## LeRobot Format Details

The LeRobotDataset format uses synchronized MP4 videos (or images) for vision and Parquet files for state/action data. The conversion maintains native LIBERO state information (accessible via states.ee_state, states.joint_state and etc.).

For the OpenPI project specifically, they provide a minimal example script for converting LIBERO data to a LeRobot dataset that you can adapt for your own use cases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "24225487-fbcf-4afe-8106-76669327fdd4"
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
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Searching for lerobot action_dim smolvla config",
  "usage": {
    "total_tokens": 16255,
    "tool_uses": 6,
    "duration_ms": 6358
  },
  "last_tool_name": "WebSearch",
  "uuid": "0acc0294-5576-4854-beea-8be55349e3ab",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013KC6fSM9Mvc4RXnXRoMY47`</summary>

```json
{
  "query": "lerobot action_dim smolvla config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "12d2a4b0-8aba-4ea2-93d0-de3c9b1194dd",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NvsUs49nLkBTPygdNqbX7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Searching for LIBERO benchmark action space dimension",
  "usage": {
    "total_tokens": 16256,
    "tool_uses": 7,
    "duration_ms": 6790
  },
  "last_tool_name": "WebSearch",
  "uuid": "0089bd56-56fc-4932-8112-499d52e0c95d",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GdgkgWzQyQjKWncZwjiJpm`</summary>

```json
{
  "query": "LIBERO benchmark action space dimension"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "62c8ab7e-4b66-400e-82ae-78c0ddb92947",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NvsUs49nLkBTPygdNqbX7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 69_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Searching for LIBERO 7D action delta position",
  "usage": {
    "total_tokens": 16257,
    "tool_uses": 8,
    "duration_ms": 6927
  },
  "last_tool_name": "WebSearch",
  "uuid": "308b46bc-2959-4e45-b329-b77cf38c0d43",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KN2gyFAvrJR8itK2JDWNJ1`</summary>

```json
{
  "query": "LIBERO 7D action delta position"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "f185f946-8f03-4594-ab90-e9988df0bcc1",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NvsUs49nLkBTPygdNqbX7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 71_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Search 4: VLA + LIBERO prior work",
  "usage": {
    "total_tokens": 14302,
    "tool_uses": 1,
    "duration_ms": 2598
  },
  "last_tool_name": "ToolSearch",
  "uuid": "075f37c4-a1fc-4206-aa27-f58f061501f8",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YQM5CtZLmQGC7hRqzwDmMd`</summary>

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
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "7a416f8c-55ab-4dd5-a999-bbcc7f4ccfc8",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015SAJytV1xFssJP4GySs2rn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6117,
      "cache_read_input_tokens": 8118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6117,
        "ephemeral_1h_input_tokens": 0
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

_source line 73 · 2026-05-13T09:46:07.291Z_

<details><summary>↩ Tool result · `toolu_01YQM5CtZLmQGC7hRqzwDmMd`</summary>

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
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "b329d4c0-78ec-4440-a6d4-16d26e0ccd18"
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-13T09:46:07.723Z_

<details><summary>↩ Tool result · `toolu_01HUqwwKXFEM6j3s8NWQj4TM`</summary>

````text
# SmolVLA Base Model - Technical Details

## Model Architecture

**Type:** Vision-Language-Action (VLA) model
- **Inputs:** Multi-view images, proprioceptive/state information, optional language instructions
- **Outputs:** Continuous actions
- **Training Objective:** Flow matching
- **Action Representation:** Continuous values
- **Intended Use:** Base model for fine-tuning on specific robotics tasks

## Action & Observation Space

- **Observations:** Multi-view images + proprioceptive state
- **Actions:** Continuous action vectors
- **Language:** Optional task instructions supported

## Supported Datasets

The model is pretrained on community datasets including:
- `lerobot/libero` (referenced in quick start examples)
- Community-driven robotics datasets

## Installation

```bash
pip install "lerobot[smolvla]"
```

For full installation with optional video dependencies (ffmpeg, torchcodec): See [official documentation](https://huggingface.co/docs/lerobot/installation)

## Inference Code

```python
import torch
from lerobot.datasets.lerobot_dataset import LeRobotDataset
from lerobot.policies.factory import make_pre_post_processors
from lerobot.policies.smolvla.modeling_smolvla import SmolVLAPolicy

# Load model
model_id = "lerobot/smolvla_base"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
policy = SmolVLAPolicy.from_pretrained(model_id).to(device).eval()

# Setup preprocessing/postprocessing
preprocess, postprocess = make_pre_post_processors(
    policy.config,
    model_id,
    preprocessor_overrides={"device_processor": {"device": str(device)}},
)

# Load dataset and run inference
dataset = LeRobotDataset("lerobot/libero")
frame = dict(dataset[0])
batch = preprocess(frame)

with torch.inference_mode():
    pred_action = policy.select_action(frame)
    pred_action = postprocess(pred_action)
```

## Training Configuration

### Training Step (Loss + Backward)

```python
policy.train()
batch = dict(dataset[0])
batch = preprocess(batch)

loss, outputs = policy.forward(batch)
loss.backward()
```

### Fine-tuning Command

```bash
lerobot-train \
  --dataset.repo_id=${HF_USER}/&lt;dataset> \
  --output_dir=./outputs/[RUN_NAME] \
  --job_name=[RUN_NAME] \
  --policy.repo_id=${HF_USER}/&lt;desired_policy_repo_id> \
  --policy.path=lerobot/smolvla_base \
  --policy.dtype=bfloat16 \
  --policy.device=cuda \
  --steps=100000 \
  --batch_size=4
```

### Policy-Specific Flags

- `--policy.chunk_size=...`
- `--policy.n_action_steps=...`
- `--policy.max_action_tokens=...`
- `--policy.gradient_checkpointing=true`

## Evaluation & Real-World Deployment

```bash
lerobot-record \
  --robot.type=so100_follower \
  --robot.port=/dev/ttyACM1 \
  --robot.cameras="{ up: {type: opencv, index_or_path: /dev/video10, width: 640, height: 480, fps: 30}, side: {type: intelrealsense, serial_number_or_name: 233522074606, width: 640, height: 480, fps: 30}}" \
  --robot.id=my_awesome_follower_arm \
  --display_data=false \
  --dataset.repo_id=${HF_USER}/eval_so100 \
  --dataset.single_task="Put lego brick into the transparent box" \
  --policy.path=${HF_USER}/my_policy
```

## Key Features

- **Efficiency:** Trainable on a single GPU, deployable on consumer hardware
- **Performance:** Matches larger VLAs through community-driven data
- **Flexibility:** Supports multi-view camera inputs and language conditioning
- **Production-Ready:** Includes evaluation and real-world inference scripts
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "504096b9-5e06-4856-90d2-9059ac2cc852"
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
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "description": "Searching for huggingface lerobot libero 2025 2026",
  "usage": {
    "total_tokens": 19104,
    "tool_uses": 5,
    "duration_ms": 14958
  },
  "last_tool_name": "WebSearch",
  "uuid": "bbb5ef4e-9a17-411a-b6aa-9e9b20c9ef59",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PPGBwJAdEb1KtpW9HRqJkR`</summary>

```json
{
  "query": "huggingface lerobot libero 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "30f31ea5-4bf8-41fd-b6e4-f3bf9708dfbe",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013q1evnt2UxHdnMzrPFSVe9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 897,
      "cache_creation_input_tokens": 1918,
      "cache_read_input_tokens": 16178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1918,
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

### System

_source line 77_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "description": "Searching for LIBERO dataset huggingface hub",
  "usage": {
    "total_tokens": 19147,
    "tool_uses": 6,
    "duration_ms": 15264
  },
  "last_tool_name": "WebSearch",
  "uuid": "07491adf-6b28-4790-9256-8c9a8b817a3c",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GBA1N7H5VuwrnNQbSCJgpy`</summary>

```json
{
  "query": "LIBERO dataset huggingface hub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "b7edcbd1-873b-4259-9ff5-1355c1bdd697",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013q1evnt2UxHdnMzrPFSVe9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 897,
      "cache_creation_input_tokens": 1918,
      "cache_read_input_tokens": 16178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1918,
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

### System

_source line 79_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "description": "Searching for site:huggingface.co LIBERO lerobot dataset",
  "usage": {
    "total_tokens": 19190,
    "tool_uses": 7,
    "duration_ms": 15376
  },
  "last_tool_name": "WebSearch",
  "uuid": "571ed10e-578e-48ac-ad35-e20aed0c7d40",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 80_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G1QhY6cRBPyuTgu9RkS7eW`</summary>

```json
{
  "query": "site:huggingface.co LIBERO lerobot dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "9cb7b571-f188-4366-a97a-516fadac58d4",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013q1evnt2UxHdnMzrPFSVe9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 897,
      "cache_creation_input_tokens": 1918,
      "cache_read_input_tokens": 16178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1918,
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

_source line 81 · 2026-05-13T09:46:09.787Z_

<details><summary>↩ Tool result · `toolu_01GdgkgWzQyQjKWncZwjiJpm`</summary>

```text
Web search results for query: "LIBERO benchmark action space dimension"

Links: [{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"BOSS: Benchmark for Observation Space Shift in Long-Horizon Task","url":"https://arxiv.org/html/2502.15679v1"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"RL with LIBERO Benchmark — RLinf documentation","url":"https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/libero.html"},{"title":"LIBERO Benchmark | NVlabs/vla0 | DeepWiki","url":"https://deepwiki.com/NVlabs/vla0/4.2-libero-benchmark"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Post-train on LIBERO Benchmark · Issue #30 · Robbyant/lingbot-va","url":"https://github.com/Robbyant/lingbot-va/issues/30"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/liu_zhu_NeurIPS2023.pdf"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"How brittle are the VLA models in robotics | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"}]

Based on the search results, the LIBERO benchmark action space is 7-dimensional continuous actions consisting of 3D end-effector position control (x, y, z), 3D rotation control (roll, pitch, yaw), and gripper control (open/close).

Additionally, the action space is defined as a 7-dimensional relative Cartesian displacement with respect to the gripper frame, with a control frequency set to 20 Hz.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "3cc096bf-f58b-4f01-8a1e-4d645a45621a"
}
```

</details>

---

### System

_source line 82_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Searching for OpenVLA LIBERO fine-tune",
  "usage": {
    "total_tokens": 16239,
    "tool_uses": 2,
    "duration_ms": 5573
  },
  "last_tool_name": "WebSearch",
  "uuid": "663859f3-4d87-4bda-a4a3-ac56fc9ebbe0",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 83_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XorqWkbbX4YjxzsUGW7FbD`</summary>

```json
{
  "query": "OpenVLA LIBERO fine-tune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "0578eb5e-189b-42a9-a2b1-4ee1d1a62546",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01ATUGFArK1Z4zs7ypEP1MXZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 84 · 2026-05-13T09:46:10.362Z_

<details><summary>↩ Tool result · `toolu_01GVk8eirQBF8En2h291Ez48`</summary>

```text
Web search results for query: "SmolVLA action dimension architecture"

Links: [{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"Pedagogical Alignment for Vision-Language-Action Models: A Comprehensive Framework for Data, Architecture, and Evaluation in Education","url":"https://arxiv.org/html/2601.13876"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"Decoding SmolVLA: A Vision-Language-Action Model for Efficient and Accessible Robotics","url":"https://blog.phospho.ai/decoding-smolvla-a-vision-language-action-model-for-efficient-and-accessible-robotics/"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"VLA-0-Smol","url":"https://robot-learning-collective.github.io/vla-0-smol"},{"title":"blog/smolvla.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/smolvla.md"},{"title":"VLA (2) SmolVLA, ACT — XLeRobot 0.3.0 documentation","url":"https://xlerobot.readthedocs.io/en/latest/software/getting_started/VLA_smol.html"},{"title":"SmolVLA Models: Compact Vision-Language-Action Systems","url":"https://www.emergentmind.com/topics/smolvla-models"}]

Based on the search results, here's what I found about SmolVLA's action dimension architecture:

## Core Architecture

SmolVLA consists of two core components: a Vision-Language Model (VLM) that processes multimodal inputs and an action expert that outputs robot control commands. SmolVLA's action expert is a compact transformer (~100M parameters) that generates action chunks.

## Action Dimension Handling

SmolVLA uses a dynamic padding approach for handling action dimensions:

SmolVLA automatically detects and handles action dimensions without manual configuration: during training, dimensions are padded to 32-D (max_action_dim), and during inference, this is cropped back to the original dimension. Unlike other VLA models (e.g., xVLA) that may require manual action_mode configuration, SmolVLA's dynamic padding supports any action space ≤ 32D.

## Action Expert Design

The action expert is architected as a lightweight transformer with interleaved cross-attention (CA) and causal self-attention (SA) layers, where CA layers enable action tokens to condition on VLM-derived perceptual features, while causal SA layers enforce temporal consistency among generated actions.

Flow Matching objectives have been shown to be superior in efficacy over standard regression methods, particularly in handling complex, multimodal action distributions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "936a2416-2581-48d1-862b-90a93d35a98c"
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
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Searching for VLA fine-tune LIBERO benchmark",
  "usage": {
    "total_tokens": 16240,
    "tool_uses": 3,
    "duration_ms": 5958
  },
  "last_tool_name": "WebSearch",
  "uuid": "7fe5e22f-03dd-46ef-adaf-9a0e65d76bb8",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 86_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XHZATUmCufispvoNPuruZL`</summary>

```json
{
  "query": "VLA fine-tune LIBERO benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "e4fce58c-de11-4464-a12e-f3fc6046801f",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01ATUGFArK1Z4zs7ypEP1MXZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Searching for LIBERO fine-tuned VLA checkpoint",
  "usage": {
    "total_tokens": 16241,
    "tool_uses": 4,
    "duration_ms": 6389
  },
  "last_tool_name": "WebSearch",
  "uuid": "1c45648e-b2ae-4bbf-ac81-883ce02d87d7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 88_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016zsYTuipTmWNKKLveYSPEu`</summary>

```json
{
  "query": "LIBERO fine-tuned VLA checkpoint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "a38810b5-88f4-4061-9e77-4df41ea0f634",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01ATUGFArK1Z4zs7ypEP1MXZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 89_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Searching for OpenVLA LIBERO results 2025 2026",
  "usage": {
    "total_tokens": 16242,
    "tool_uses": 5,
    "duration_ms": 6740
  },
  "last_tool_name": "WebSearch",
  "uuid": "364ec64c-eb51-4cf0-a227-a9c7b007ed3b",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 90_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XHCRvU7FxtQwCXoWDviSjP`</summary>

```json
{
  "query": "OpenVLA LIBERO results 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "ea8df0d0-1236-40d6-88b4-86335fb0cde0",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01ATUGFArK1Z4zs7ypEP1MXZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 91 · 2026-05-13T09:46:11.633Z_

<details><summary>↩ Tool result · `toolu_01GD1GCgigBaDwBkfaf9kmb9`</summary>

```text
Web search results for query: "SmolVLA 7D action gripper"

Links: [{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"Clarifications on fine-tuning on different envs and embodiments · Issue #2259 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2259"},{"title":"Single Camera SmolVLA Training - Beginners - Hugging Face Forums","url":"https://discuss.huggingface.co/t/single-camera-smolvla-training/172719"},{"title":"GenAI for Robotics: Fine-Tuning SmolVLA to Pick and Place | by Henry H | Medium","url":"https://medium.com/@henryhu1607/genai-for-robotics-fine-tuning-smolvla-to-pick-and-place-940b485e6c9b"},{"title":"How to easily run inference with a trained model · Issue #2227 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2227"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost","url":"https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"},{"title":"SoArm in Lerobot | Seeed Studio Wiki","url":"https://wiki.seeedstudio.com/lerobot_so100m_new/"}]

Based on the search results, here's what I found about SmolVLA and the 7D action gripper configuration:

## SmolVLA Overview

SmolVLA is a groundbreaking Vision-Language-Action (VLA) model with only 450 million parameters, developed by Hugging Face. It's carefully designed for cost-effective deployment on consumer-grade hardware, making advanced robotics technology accessible to more developers and enthusiasts.

## 7D Action Space with Gripper

Regarding the 7D action space with gripper, SmolVLA supports a 6-DOF action space (shoulder_pan, shoulder_lift, elbow_flex, wrist_flex, wrist_roll, gripper), which represents the degrees of freedom commonly found in robotic arms.

Multiple sources mention 7-DOF configurations in the context of SmolVLA training. The robot setup can be a Franka Emika Panda (7DoF + gripper), and users have worked with 7-DoF robotic arms (6 joint axes + 1 gripper) for training SmolVLA.

## Key Features

SmolVLA consists of two core components: a Vision-Language Model (VLM) that processes multimodal inputs and an action expert that outputs robot control commands. It uses SmolVLM2 as its VLM backbone, which is optimized for multi-image inputs and consists of a SigLIP vision encoder and a SmolLM2 language decoder.

SmolVLA achieves real-time response by decoupling action prediction from execution, reducing task completion time by approximately 30% on average.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "175d6e4f-30c2-4d5c-a048-07ef238025de"
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-13T09:46:11.678Z_

<details><summary>↩ Tool result · `toolu_013KC6fSM9Mvc4RXnXRoMY47`</summary>

```text
Web search results for query: "lerobot action_dim smolvla config"

Links: [{"title":"VLA (2) SmolVLA, ACT — XLeRobot 0.3.0 documentation","url":"https://xlerobot.readthedocs.io/en/latest/software/getting_started/VLA_smol.html"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/smolvla"},{"title":"`smolvla_base training`: `Expected all tensors to be on the same device` · Issue #1377 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1377"},{"title":"Training SmolVLA with LeRobot Notebook - Colab - Google","url":"https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb"},{"title":"Clarifications on fine-tuning on different envs and embodiments · Issue #2259 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2259"}]

Based on the search results, here's what I found about `action_dim` in SmolVLA config:

SmolVLA's dynamic padding supports any action space ≤ 32D, with training padding 12D actions to 32D and inference cropping back to the original 12D, using `config.action_feature.shape[0]` to auto-detect the number of actions.

The key information about `action_dim` in SmolVLA configuration:

1. **Max Action Dimension**: SmolVLA can handle action spaces up to 32D through dynamic padding

2. **Configuration Details**: During training, actions are padded to `self.config.max_action_dim` (32D), and during inference, actions are cropped back to the original action dimension using `self.config.action_feature.shape[0]`

3. **Flexibility**: Unlike other VLA models, SmolVLA doesn't require manual `action_mode` configuration since it dynamically handles the padding and unpadding process automatically.

The model automatically detects the original action dimension from the dataset configuration and handles the conversion between padded and unpadded action spaces transparently.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "f9c5409f-8e47-4d7e-906d-bdbe23ce5bde"
}
```

</details>

---

### System

_source line 93_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Searching for pi0 LIBERO Physical Intelligence",
  "usage": {
    "total_tokens": 16243,
    "tool_uses": 6,
    "duration_ms": 7097
  },
  "last_tool_name": "WebSearch",
  "uuid": "59d74781-b1ba-46e1-b3d0-eeb884e0546d",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 94_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FnMWEzLyuJ3MbQuuC29J2R`</summary>

```json
{
  "query": "pi0 LIBERO Physical Intelligence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "fd0759c1-c95d-4c13-8146-456996f083dc",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01ATUGFArK1Z4zs7ypEP1MXZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 95_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Fetching https://huggingface.co/docs/lerobot/smolvla",
  "usage": {
    "total_tokens": 21913,
    "tool_uses": 8,
    "duration_ms": 21008
  },
  "last_tool_name": "WebFetch",
  "uuid": "78c452f6-4e5f-4bd5-9909-a139c4aafd9c",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 96_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012vuguP2Hje3EgtdDkM2TVF`</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/smolvla",
  "prompt": "Extract all details: architecture, action_dim, observation space, training commands, config parameters, LoRA/PEFT options, fine-tuning instructions, data format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "d81ee45a-1c41-4707-a8df-6e8b70e6ded2",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S8TDPcFRk77xtvVqX6WucB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 383,
      "cache_creation_input_tokens": 5271,
      "cache_read_input_tokens": 16186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5271,
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

_source line 97 · 2026-05-13T09:46:12.127Z_

<details><summary>↩ Tool result · `toolu_01SRDYLxKAEeZLhKJyoBUh1j`</summary>

```text
Web search results for query: "SmolVLA paper arxiv 2026"

Links: [{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://huggingface.co/papers/2506.01844"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"[2602.24143] Robust Skills, Brittle Grounding: Diagnosing Restricted Generalization in Vision-Language Action Policies via Multi-Object Picking","url":"https://arxiv.org/abs/2602.24143"},{"title":"[PDF] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SmolVLA:-A-Vision-Language-Action-Model-for-and-Shukor-Aubakirova/6ab4d113676d00e74b55e918fee4c7affaa8652f"},{"title":"SmolVLA - ArXivIQ","url":"https://arxiviq.substack.com/p/smolvla"},{"title":"[2603.07404] Adaptive Capacity Allocation for Vision Language Action Fine-tuning","url":"https://arxiv.org/abs/2603.07404"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"http://export.arxiv.org/abs/2506.01844"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/smolvla-vision-language-action-model-affordable-efficient"}]

Based on the search results, here's information about the SmolVLA paper on arXiv:

## SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics

SmolVLA is a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. The paper was published on arXiv on June 2, 2025 with identifier 2506.01844.

### Key Features

SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs. Despite its compact size, SmolVLA achieves performance comparable to VLAs that are 10x larger.

### Architecture and Innovations

Key design choices include: (i) skipping layers in the VLM, (ii) using a minimal number of visual tokens (iii) leveraging small pretrained VLMs, and (iv) interleaving self-attention layers with lighter cross-attention layers.

To further improve responsiveness, the paper introduces an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action generation.

### Training Data

SmolVLA is trained end-to-end on fewer than 30k episodes drawn entirely from publicly available, community-contributed datasets, demonstrating strong performance while using an order of magnitude less data than prior art.

### Authors and Availability

The researchers evaluate SmolVLA on a range of both simulated as well as real-world robotic benchmarks and release all code, pretrained models, and training data. The paper was authored by Mustafa Shukor and 13 other researchers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "3edde187-f64a-4dd0-a2de-2b51cfaf212d"
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
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Searching for octo LIBERO fine-tune results",
  "usage": {
    "total_tokens": 16244,
    "tool_uses": 7,
    "duration_ms": 7502
  },
  "last_tool_name": "WebSearch",
  "uuid": "6e738df7-8bdf-4da6-ac97-7ec87c7ea603",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 99_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014emvP7u8Vi2mg2mfhmVetY`</summary>

```json
{
  "query": "octo LIBERO fine-tune results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "797a3058-eab9-43f7-85a9-dfc29500746b",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01ATUGFArK1Z4zs7ypEP1MXZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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

_source line 100 · 2026-05-13T09:46:12.131Z_

<details><summary>↩ Tool result · `toolu_012vuguP2Hje3EgtdDkM2TVF`</summary>

````text
# SmolVLA

SmolVLA is Hugging Face’s lightweight foundation model for robotics. Designed for easy fine-tuning on LeRobot datasets, it helps accelerate your development!

  
  
  
    Figure 1. SmolVLA takes as input (i) multiple cameras views, (ii) the
    robot’s current sensorimotor state, and (iii) a natural language
    instruction, encoded into contextual features used to condition the action
    expert when generating an action chunk.
  

## Set Up Your Environment

1. Install LeRobot by following our [Installation Guide](./installation).
2. Install SmolVLA dependencies by running:

   ```bash
   pip install -e ".[smolvla]"
   ```

## Collect a dataset

SmolVLA is a base model, so fine-tuning on your own data is required for optimal performance in your setup.
We recommend recording ~50 episodes of your task as a starting point. Follow our guide to get started: [Recording a Dataset](./il_robots)

In your dataset, make sure to have enough demonstrations per each variation (e.g. the cube position on the table if it is cube pick-place task) you are introducing.

We recommend checking out the dataset linked below for reference that was used in the [SmolVLA paper](https://huggingface.co/papers/2506.01844):

🔗 [SVLA SO100 PickPlace](https://huggingface.co/spaces/lerobot/visualize_dataset?path=%2Flerobot%2Fsvla_so100_pickplace%2Fepisode_0)

In this dataset, we recorded 50 episodes across 5 distinct cube positions. For each position, we collected 10 episodes of pick-and-place interactions. This structure, repeating each variation several times, helped the model generalize better. We tried similar dataset with 25 episodes, and it was not enough leading to a bad performance. So, the data quality and quantity is definitely a key.
After you have your dataset available on the Hub, you are good to go to use our finetuning script to adapt SmolVLA to your application.

## Finetune SmolVLA on your data

Use [`smolvla_base`](https://hf.co/lerobot/smolvla_base), our pretrained 450M model, and fine-tune it on your data.
Training the model for 20k steps will roughly take ~4 hrs on a single A100 GPU. You should tune the number of steps based on performance and your use-case.

If you don't have a gpu device, you can train using our notebook on [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb)

Pass your dataset to the training script using `--dataset.repo_id`. If you want to test your installation, run the following command where we use one of the datasets we collected for the [SmolVLA Paper](https://huggingface.co/papers/2506.01844).

```bash
cd lerobot && lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=${HF_USER}/mydataset \
  --batch_size=64 \
  --steps=20000 \
  --output_dir=outputs/train/my_smolvla \
  --job_name=my_smolvla_training \
  --policy.device=cuda \
  --wandb.enable=true
```

  You can start with a small batch size and increase it incrementally, if the
  GPU allows it, as long as loading times remain short.

Fine-tuning is an art. For a complete overview of the options for finetuning, run

```bash
lerobot-train --help
```

  
  
  
    Figure 2: Comparison of SmolVLA across task variations. From left to right:
    (1) pick-place cube counting, (2) pick-place cube counting, (3) pick-place
    cube counting under perturbations, and (4) generalization on pick-and-place
    of the lego block with real-world SO101.
  

## Evaluate the finetuned model and run it in real-time

Similarly for when recording an episode, it is recommended that you are logged in to the HuggingFace Hub. You can follow the corresponding steps: [Record a dataset](./il_robots).
Once you are logged in, you can run inference in your setup by doing:

```bash
lerobot-record \
  --robot.type=so101_follower \
  --robot.port=/dev/ttyACM0 \ # <- Use your port
  --robot.id=my_blue_follower_arm \ # <- Use your robot id
  --robot.cameras="{ front: {type: opencv, index_or_path: 8, width: 640, height: 480, fps: 30}}" \ # <- Use your cameras
  --dataset.single_task="Grasp a lego block and put it in the bin." \ # <- Use the same task description you used in your dataset recording
  --dataset.repo_id=${HF_USER}/eval_DATASET_NAME_test \  # <- This will be the dataset name on HF Hub
  --dataset.episode_time_s=50 \
  --dataset.num_episodes=10 \
  --dataset.streaming_encoding=true \
  --dataset.encoder_threads=2 \
  # --dataset.vcodec=auto \
  # <- Teleop optional if you want to teleoperate in between episodes \
  # --teleop.type=so100_leader \
  # --teleop.port=/dev/ttyACM0 \
  # --teleop.id=my_red_leader_arm \
  --policy.path=HF_USER/FINETUNE_MODEL_NAME # <- Use your fine-tuned model
```

Depending on your evaluation setup, you can configure the duration and the number of episodes to record for your evaluation suite.


````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "f84ea38a-5b49-448c-a99d-629855fe9489"
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
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Searching for diffusion policy LIBERO benchmark results",
  "usage": {
    "total_tokens": 16245,
    "tool_uses": 8,
    "duration_ms": 7810
  },
  "last_tool_name": "WebSearch",
  "uuid": "77667431-15fb-46c7-9b02-42107dedb7d1",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 102_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HoFfwZLKZGL6HuXw6kkrSJ`</summary>

```json
{
  "query": "diffusion policy LIBERO benchmark results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "e625a512-5f73-4357-b60a-c8b3479cc67f",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01ATUGFArK1Z4zs7ypEP1MXZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 14235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1935,
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
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Fetching https://huggingface.co/docs/lerobot/en/peft_train…",
  "usage": {
    "total_tokens": 21914,
    "tool_uses": 9,
    "duration_ms": 22159
  },
  "last_tool_name": "WebFetch",
  "uuid": "53e62431-e095-496f-ba65-f4871cea6043",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 104_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YZ2qq79YcXvUmucCRY3AGR`</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/en/peft_training",
  "prompt": "Extract all LoRA/PEFT fine-tuning commands, parameters, configuration options for SmolVLA, target modules, quantization settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "df6bbd75-50ce-41e2-94b4-9acccbe17688",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S8TDPcFRk77xtvVqX6WucB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 383,
      "cache_creation_input_tokens": 5271,
      "cache_read_input_tokens": 16186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5271,
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

_source line 105 · 2026-05-13T09:46:13.122Z_

<details><summary>↩ Tool result · `toolu_01KN2gyFAvrJR8itK2JDWNJ1`</summary>

```text
Web search results for query: "LIBERO 7D action delta position"

Links: [{"title":"physical-intelligence/libero · Description of the dataset features","url":"https://huggingface.co/datasets/physical-intelligence/libero/discussions/1"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"State/Action representation in LIBERO dataset (EEF vs Joint) · Issue #637 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/637"},{"title":"Why is extra_delta_action=True in 'pi0_libero' config? · Issue #750 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/750"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"openvla/modified_libero_rlds · Detailed description of the features","url":"https://huggingface.co/datasets/openvla/modified_libero_rlds/discussions/5"},{"title":"Absolute control for LIBERO · Issue #43 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/43"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"The Libero: Volleyball’s Defensive Position | Imperial Point","url":"https://theimperialpoint.com/blog/the-libero-volleyballs-defensive-position/"}]

Based on the search results, here's what I found about LIBERO 7D action delta position:

## LIBERO 7D Action Format

LIBERO uses continuous control actions in a 7-dimensional format consisting of 6D end-effector delta plus 1D gripper. More specifically:

**Action Composition:**
The action length of 7 equals 6 Delta EEF Pose + 1 gripper (-1 for open and 1 for close)

**Delta vs. Absolute:**
In LIBERO, the raw actions in the dataset are already delta actions. This means the 7D actions represent *relative* movements rather than absolute target poses. LIBERO supports two control modes — relative (default) and absolute, though the native dataset format uses delta/relative actions.

**6D End-Effector Pose Details:**
The 6D end-effector component breaks down as:
- **3D position delta** (XYZ Cartesian coordinates)
- **3D orientation delta** (typically represented as roll-pitch-yaw/RPY or axis-angle)
- **1D gripper action** (separate, usually absolute: -1 for open, +1 for close)

So when working with LIBERO, the 7D action vector represents incremental changes to the robot's end-effector pose relative to its current state, plus a discrete gripper command.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "905a59a9-c3b9-40f9-ad8d-e759a695bd72"
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-13T09:46:13.245Z_

<details><summary>↩ Tool result · `toolu_016RVQJafugAoAuvdVoiYTw3`</summary>

```text
Web search results for query: "SmolVLA action space configuration"

Links: [{"title":"VLA (2) SmolVLA, ACT — XLeRobot 0.3.0 documentation","url":"https://xlerobot.readthedocs.io/en/latest/software/getting_started/VLA_smol.html"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"Clarifications on fine-tuning on different envs and embodiments · Issue #2259 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2259"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://huggingface.co/papers/2506.01844"}]

I found comprehensive information about SmolVLA's action space configuration. Here are the key findings:

## Action Space Configuration

SmolVLA's dynamic padding supports any action space ≤ 32D, unlike other VLA models (e.g., xVLA) that may require manual action_mode configuration.

For the SO101 robot, SmolVLA uses a 6-DOF action space consisting of shoulder_pan, shoulder_lift, elbow_flex, wrist_flex, wrist_roll, and gripper.

## Action Generation Approach

SmolVLA's action expert is a compact transformer (~100M parameters) that generates action chunks, i.e. sequences of future robot actions, conditioned on the VLM's outputs. A chunk size between 10 and 50 strikes a good balance between action prediction frequency and performance.

## Important Configuration Considerations

When adapting SmolVLA to different robots, there are critical configuration points to note:

- HuggingFace automatically computes statistics (min, max, mean, standard deviation) for each dataset and stores them in meta/stats.json. These statistics are used during training, but they're essential at inference time because the model outputs actions in normalized space, not the physical units the robot operates in.

- The SmolVLA model outputs actions in the same units as its training data. Some datasets use radians. For example, the datasets recorded with phosphobot such as PLB/phospho-playground-mono uses radians. However, the LeRobot SO-100 driver expects actions in degrees. This will cause the robot to move erratically or barely at all.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "d2e04de3-fdd9-4b7e-9178-b72d0a986ae8"
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-13T09:46:13.452Z_

<details><summary>↩ Tool result · `toolu_01YZ2qq79YcXvUmucCRY3AGR`</summary>

````text
# Parameter efficient fine-tuning with 🤗 PEFT

[🤗 PEFT](https://github.com/huggingface/peft) (Parameter-Efficient Fine-Tuning) is a library for efficiently adapting
large pretrained models such as pre-trained policies (e.g., SmolVLA, π₀, ...) to new tasks without training all
of the model's parameters while yielding comparable performance.

Install the `lerobot[peft]` optional package to enable PEFT support.

To read about all the possible methods of adaption, please refer to the [🤗 PEFT docs](https://huggingface.co/docs/peft/index).

## Training SmolVLA

In this section we'll show you how to train a pre-trained SmolVLA policy with PEFT on the libero dataset.
For brevity we're only training on the `libero_spatial` subset. We will use `lerobot/smolvla_base` as the model
to parameter efficiently fine-tune:

```
lerobot-train \
 --policy.path=lerobot/smolvla_base \
 --policy.repo_id=your_hub_name/my_libero_smolvla \
 --dataset.repo_id=HuggingFaceVLA/libero \
 --policy.output_features=null \
 --policy.input_features=null \
 --policy.optimizer_lr=1e-3 \
 --policy.scheduler_decay_lr=1e-4 \
 --env.type=libero \
 --env.task=libero_spatial \
 --steps=100000 \
 --batch_size=32 \
 --peft.method_type=LORA \
 --peft.r=64
```

Note the `--peft.method_type` parameter that let's you select which PEFT method to use. Here we use
[LoRA](https://huggingface.co/docs/peft/main/en/package_reference/lora) (Low-Rank Adapter) which is probably the most
popular fine-tuning method to date. Low-rank adaption means that we only fine-tune a matrix with comparably low rank
instead of the full weight matrix. This rank can be specified using the `--peft.r` parameter. The higher the rank
the closer you get to full fine-tuning

There are more complex methods that have more parameters. These are not yet supported, feel free to raise an issue
if you want to see a specific PEFT method supported.

By default, PEFT will target the `q_proj` and `v_proj` layers of the LM expert in SmolVLA. It will also target the
state and action projection matrices as they are most likely task-dependent. If you need to target different layers
you can use `--peft.target_modules` to specify which layers to target. You can refer to the respective PEFT method's
documentation to see what inputs are supported, (e.g., [LoRA's target_modules documentation](https://huggingface.co/docs/peft/main/en/package_reference/lora#peft.LoraConfig.target_modules)).
Usually a list of suffixes or a regex are supported. For example, to target the MLPs of the `lm_expert` instead of
the `q` and `v` projections, use:

```
--peft.target_modules='(model\.vlm_with_expert\.lm_expert\..*\.(down|gate|up)_proj|.*\.(state_proj|action_in_proj|action_out_proj|action_time_mlp_in|action_time_mlp_out))'
```

In case you need to fully fine-tune a layer instead of just adapting it, you can supply a list of layer suffixes
to the `--peft.full_training_modules` parameter:

```
--peft.full_training_modules=["state_proj"]
```

The learning rate and the scheduled target learning rate can usually be scaled by a factor of 10 compared to the
learning rate used for full fine-tuning (e.g., 1e-4 normal, so 1e-3 using LoRA).


````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "4d68b425-68ab-42d9-81ac-8604dd9fa8fd"
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
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Fetching https://docs.phospho.ai/learn/train-smolvla",
  "usage": {
    "total_tokens": 21915,
    "tool_uses": 10,
    "duration_ms": 22917
  },
  "last_tool_name": "WebFetch",
  "uuid": "c021a587-7b6a-4ae9-be16-ba001e1c9582",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 109_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XVZxYvgsSMLQiE1vpAs4zH`</summary>

```json
{
  "url": "https://docs.phospho.ai/learn/train-smolvla",
  "prompt": "Extract all training commands, configuration parameters, data format requirements, step-by-step instructions for fine-tuning SmolVLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "c2f9b647-c102-4c3b-9f53-e221d42f8bfe",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S8TDPcFRk77xtvVqX6WucB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 383,
      "cache_creation_input_tokens": 5271,
      "cache_read_input_tokens": 16186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5271,
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

_source line 110 · 2026-05-13T09:46:14.885Z_

<details><summary>↩ Tool result · `toolu_01GBA1N7H5VuwrnNQbSCJgpy`</summary>

```text
Web search results for query: "LIBERO dataset huggingface hub"

Links: [{"title":"physical-intelligence/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/physical-intelligence/libero"},{"title":"yifengzhu-hf/LIBERO-datasets · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets"},{"title":"HuggingFaceVLA/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/libero"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"openvla/modified_libero_rlds · Datasets at Hugging Face","url":"https://huggingface.co/datasets/openvla/modified_libero_rlds"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"Libero Benchmark Dataset - a IPEC-COMMUNITY Collection","url":"https://huggingface.co/collections/IPEC-COMMUNITY/libero-benchmark-dataset"}]

Based on the search results, here's information about the LIBERO dataset on Hugging Face Hub:

## Overview

LIBERO is a benchmark designed to study lifelong robot learning — the idea that robots need to keep learning and adapting with their users over time. It provides a set of standardized manipulation tasks that focus on knowledge transfer: how well a robot can apply what it has already learned to new situations.

## Available Datasets on Hugging Face

There are several LIBERO dataset repositories hosted on Hugging Face Hub:

1. **physical-intelligence/libero**: This dataset combines four individual Libero datasets: Libero-Spatial, Libero-Object, Libero-Goal and Libero-10. All datasets were converted into LeRobot format.

2. **HuggingFaceVLA/libero** and **lerobot/libero**: These datasets were created using LeRobot.

3. **yifengzhu-hf/LIBERO-datasets**: The structure includes libero_object, libero_spatial, libero_goal, libero_90, and libero_10, with demonstrations of each task stored in HDF5 files.

## Task Suites

LIBERO provides 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100.

You can find these datasets by searching for "libero" on the Hugging Face Hub or visiting the specific repository URLs directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "43762eb2-8e24-4e35-a431-a26b1c9346be"
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-13T09:46:15.016Z_

<details><summary>↩ Tool result · `toolu_01G1QhY6cRBPyuTgu9RkS7eW`</summary>

```text
Web search results for query: "site:huggingface.co LIBERO lerobot dataset"

Links: [{"title":"lerobot/libero_object_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_object_image"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"physical-intelligence/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/physical-intelligence/libero"},{"title":"HuggingFaceVLA/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/libero"},{"title":"lerobot/libero_10_image · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero_10_image"},{"title":"lerobot/pi05_libero_base · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_base"},{"title":"jesbu1/libero_90_lerobot · Datasets at Hugging Face","url":"https://huggingface.co/datasets/jesbu1/libero_90_lerobot"},{"title":"README.md · physical-intelligence/libero at main","url":"https://huggingface.co/datasets/physical-intelligence/libero/blob/main/README.md"},{"title":"lerobot/pi05_libero_finetuned · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned"}]

I found several results related to LIBERO and LeRobot datasets on Hugging Face. Here's a summary:

## Main Datasets Found:

1. **lerobot/libero** - This dataset was created using LeRobot

2. **physical-intelligence/libero** - This dataset combines four individual Libero datasets: Libero-Spatial, Libero-Object, Libero-Goal and Libero-10. All datasets were taken from here and converted into LeRobot format

3. **HuggingFaceVLA/libero** - A preprocessed LIBERO dataset that is fully compatible with the current LeRobot codebase and requires no additional manipulation

## Additional Variants:

- **lerobot/libero_object_image** - A specific variant focusing on object images
- **lerobot/libero_10_image** - The Libero-10 variant with image data
- **jesbu1/libero_90_lerobot** - The processed dataset for LIBERO 90 in huggingface LeRobot format to be used for π₀ fine-tuning

All of these datasets are available on the Hugging Face Hub and are designed for use with the LeRobot framework for robot learning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "db84d975-15ca-48af-809d-e2b8d189c2b8"
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
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Fetching https://medium.com/correll-lab/fine-tuning-smolvl…",
  "usage": {
    "total_tokens": 21916,
    "tool_uses": 11,
    "duration_ms": 24874
  },
  "last_tool_name": "WebFetch",
  "uuid": "ca540f8b-366d-4014-8685-8941de2fb8a2",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 113_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MvJuDz4K2CMhdpLoNQdq9y`</summary>

```json
{
  "url": "https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632",
  "prompt": "Extract all code, training commands, configuration, action dimensions, data format, step-by-step fine-tuning process for SmolVLA in new environments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "c50ed2e3-9151-4f25-b240-768650807c5a",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S8TDPcFRk77xtvVqX6WucB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 383,
      "cache_creation_input_tokens": 5271,
      "cache_read_input_tokens": 16186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5271,
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

_source line 114 · 2026-05-13T09:46:16.204Z_

<details><summary>↩ Tool result · `toolu_01XorqWkbbX4YjxzsUGW7FbD`</summary>

```text
Web search results for query: "OpenVLA LIBERO fine-tune"

Links: [{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"openvla/openvla-7b-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-10"},{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"},{"title":"openvla/openvla-7b-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-spatial"},{"title":"openvla/openvla-7b-finetuned-libero-object · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-object"},{"title":"moojink/openvla-7b-oft-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"}]

Based on the search results, here's what I found about OpenVLA LIBERO fine-tuning:

## Overview

OpenVLA was fine-tuned via LoRA (r=32) on four LIBERO task suites independently: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-10.

## Available Checkpoints

The OpenVLA 7B model was fine-tuned via LoRA (r=32) on the LIBERO-Spatial dataset from the LIBERO simulation benchmark, with similar checkpoints available for the other LIBERO task suites.

## Optimized Fine-Tuning Approach

More recently, researchers developed an improved fine-tuning recipe called OpenVLA-OFT. The Optimized Fine-Tuning (OFT) recipe integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to improve inference efficiency, policy performance, and flexibility in the model's input-output specifications.

## Performance Results

OpenVLA-OFT establishes a new state of the art by achieving 97.1% average success rate across four task suites, outperforming both fine-tuned OpenVLA policies (76.5%).

## Data and Training

The LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-10 datasets are available in RLDS data format (~10 GB total), which can be used to fine-tune OpenVLA or train other methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "d812b7e1-f95d-495e-9b20-995f15490234"
}
```

</details>

---

### System

_source line 115_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Fetching https://huggingface.co/blog/smolvla",
  "usage": {
    "total_tokens": 21917,
    "tool_uses": 12,
    "duration_ms": 25664
  },
  "last_tool_name": "WebFetch",
  "uuid": "64fecbef-43d7-4616-b5dd-8514cf3179bd",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 116_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01P7aVWCfTqnwc1iNVadXgoK`</summary>

```json
{
  "url": "https://huggingface.co/blog/smolvla",
  "prompt": "Extract: model architecture details, action_dim, training data, fine-tuning approach, pretraining vs finetuning distinction, performance numbers, training config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "5b9110d4-cafe-48cc-8918-ba17c5e85a17",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S8TDPcFRk77xtvVqX6WucB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 383,
      "cache_creation_input_tokens": 5271,
      "cache_read_input_tokens": 16186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5271,
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

_source line 117 · 2026-05-13T09:46:17.377Z_

<details><summary>↩ Tool result · `toolu_01XHZATUmCufispvoNPuruZL`</summary>

```text
Web search results for query: "VLA fine-tune LIBERO benchmark"

Links: [{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.19645"},{"title":"openvla/openvla-7b-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-spatial"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"openvla/openvla-7b-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-10"},{"title":"GitHub - CHELabUB/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/CHELabUB/openvla"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"}]

Based on the search results, here's what I found about VLA fine-tuning on the LIBERO benchmark:

## Overview

The updated OpenVLA paper (v2) discusses fine-tuning OpenVLA on a simulated benchmark, LIBERO, in Appendix E.

## Key Results

OpenVLA-OFT sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1%. Additionally, OpenVLA-OFT obtains 26x faster action generation speed and 3x lower latency than the base OpenVLA model.

## Fine-Tuning Approaches

There are multiple ways to fine-tune VLAs on LIBERO:

1. **LoRA Fine-tuning**: Models were produced by fine-tuning the OpenVLA 7B model via LoRA (r=32) on the LIBERO-Spatial dataset from the LIBERO simulation benchmark.

2. **Optimized Fine-Tuning (OFT)**: The OFT recipe integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective.

## LIBERO Benchmark Structure

LIBERO includes four task suites—LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long—each providing 500 expert demonstrations across 10 tasks to assess policy generalization to different spatial layouts, objects, goals, and long-horizon tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "40cca400-83ff-4d14-babe-7b3d88bf1966"
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
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Fetching https://arxiv.org/html/2506.01844v1",
  "usage": {
    "total_tokens": 22674,
    "tool_uses": 9,
    "duration_ms": 18189
  },
  "last_tool_name": "WebFetch",
  "uuid": "f8a994e7-7637-4652-93c4-ebfe8ac9f263",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 119_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ABKHR7H8JuRjkK4DokJCMC`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.01844v1",
  "prompt": "Extract all details about action space, action dimension, action_dim configuration, how actions are represented (6D, 7D, joint angles, end-effector), gripper handling, max_action_dim, padding, and any configuration parameters related to action space. Also look for any mention of LIBERO."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "da5a4660-69b4-4c72-817b-bc286e83814f",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017qnPwAkiTFsqrYQrHFb2bj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2358,
      "cache_creation_input_tokens": 4060,
      "cache_read_input_tokens": 16182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4060,
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

_source line 120 · 2026-05-13T09:46:17.837Z_

<details><summary>↩ Tool result · `toolu_016zsYTuipTmWNKKLveYSPEu`</summary>

```text
Web search results for query: "LIBERO fine-tuned VLA checkpoint"

Links: [{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301"},{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"moojink/openvla-7b-oft-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial"},{"title":"LightVLA/LIBERO.md at main · LiAutoAD/LightVLA","url":"https://github.com/LiAutoAD/LightVLA/blob/main/LIBERO.md"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"README.md · moojink/openvla-7b-oft-finetuned-libero-10 at main","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10/blob/main/README.md"},{"title":"Openvla 7b Oft Finetuned Libero Goal","url":"https://model.aibase.com/models/details/1935154868096602112"}]

Based on the search results, here's information about LIBERO fine-tuned VLA checkpoints:

## OpenVLA-OFT Fine-Tuned LIBERO Checkpoints

OpenVLA-OFT, a policy created with optimized fine-tuning techniques, achieves state-of-the-art results in LIBERO with a 97.1% average success rate across 4 task suites, outperforming π0, MDT, Seer, DiT Policy, Octo, and Diffusion Policy.

### Available Checkpoints

Several fine-tuned OpenVLA-OFT checkpoints are available on Hugging Face, including:
- `moojink/openvla-7b-oft-finetuned-libero-spatial`
- `moojink/openvla-7b-oft-finetuned-libero-10` (LIBERO-Long)
- `moojink/openvla-7b-oft-finetuned-libero-goal`
- `moojink/openvla-7b-oft-finetuned-libero-object`

### Key Features

OpenVLA-OFT significantly improves upon the base OpenVLA model by incorporating optimized fine-tuning techniques. The recipe, when augmented with FiLM for better language grounding ("OFT+"), enables high-frequency language-driven control on the bimanual ALOHA robot with a 7B-parameter VLA policy.

### Training Requirements

Training jobs were run with 8 A100 or H100 GPUs with 80 GB memory and trained for 50K to 150K gradient steps, depending on the fine-tuning dataset size, which took 1-2 days.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "1bfe7ef1-7c43-4413-9c2e-670e0a73e436"
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
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Fetching https://github.com/huggingface/lerobot/issues/2259",
  "usage": {
    "total_tokens": 22675,
    "tool_uses": 10,
    "duration_ms": 19251
  },
  "last_tool_name": "WebFetch",
  "uuid": "56c603ee-8f91-46bc-b0ee-4e775fb40b6a",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 122_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GAPTsfrrTwats6RcE7eHyW`</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/issues/2259",
  "prompt": "Extract all technical details about action dimensions, action_dim configuration, how to fine-tune SmolVLA on different environments/embodiments with different action spaces, and any specific mention of 6D vs 7D actions or LIBERO."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "e5acd6b6-4527-4e6b-bf76-208fdf54d2b7",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017qnPwAkiTFsqrYQrHFb2bj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2358,
      "cache_creation_input_tokens": 4060,
      "cache_read_input_tokens": 16182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4060,
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

_source line 123 · 2026-05-13T09:46:18.823Z_

<details><summary>↩ Tool result · `toolu_014emvP7u8Vi2mg2mfhmVetY`</summary>

```text
Web search results for query: "octo LIBERO fine-tune results"

Links: [{"title":"The details of fine-tuning Octo using LIBERO · Issue #215 · openvla/openvla","url":"https://github.com/openvla/openvla/issues/215"},{"title":"FLOWER: Democratizing Generalist Robot Policies","url":"https://arxiv.org/pdf/2509.04996"},{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://octo-models.github.io/"},{"title":"octo/examples/02_finetune_new_observation_action.py at main · octo-models/octo","url":"https://github.com/octo-models/octo/blob/main/examples/02_finetune_new_observation_action.py"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"GitHub - CHELabUB/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/CHELabUB/openvla"},{"title":"Random behavior after fine tuning octo on new robot · Issue #29 · octo-models/octo","url":"https://github.com/octo-models/octo/issues/29"},{"title":"An Open-Source Generalist Robot Policy","url":"https://octo-models.github.io/paper.pdf"},{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://arxiv.org/html/2405.12213v2"},{"title":"openvla/README.md at main · openvla/openvla","url":"https://github.com/openvla/openvla/blob/main/README.md"}]

Based on the web search results, I found information about fine-tuning Octo using LIBERO. Here's what the search revealed:

## Octo Fine-tuning on LIBERO

On average across the six evaluation setups, Octo outperforms the next best baseline by 52%. Each task uses ~100 target demonstrations, and importantly, the same finetuning recipe is used for all evaluation tasks, making this a good default configuration for Octo finetuning.

### Fine-tuning Approach

Octo was designed specifically to support efficient finetuning to new robot setups, including robots with different actions and different combinations of cameras and proprioceptive information.

### Challenges with LIBERO

There have been reported challenges with reproducing Octo's fine-tuning results on LIBERO. Some researchers attempting to reproduce the experimental results of fine-tuning Octo using LIBERO have reported that the success rate in evaluation comes out as 0. This suggests that careful attention to configuration details and dataset compatibility is important when fine-tuning Octo on LIBERO.

### Benchmark Context

LIBERO-10 provides 50 demonstrations for 10 tasks, while LIBERO-90 extends to 90 different tasks, and both versions use a Franka Emika Panda robot with end-effector control and dual camera inputs (static and wrist).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "fdde961e-6350-41b4-a08f-f597767398dd"
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-13T09:46:18.844Z_

<details><summary>↩ Tool result · `toolu_01FnMWEzLyuJ3MbQuuC29J2R`</summary>

```text
Web search results for query: "pi0 LIBERO Physical Intelligence"

Links: [{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"Open Sourcing π0","url":"https://www.pi.website/blog/openpi"},{"title":"Physical Intelligence open-sources Pi0 robotics foundation model","url":"https://www.therobotreport.com/physical-intelligence-open-sources-pi0-robotics-foundation-model/"},{"title":"lerobot/pi0_libero_base · Hugging Face","url":"https://huggingface.co/lerobot/pi0_libero_base"},{"title":"π₀ (Pi0) · Hugging Face","url":"https://huggingface.co/docs/lerobot/pi0"},{"title":"Pi0 and Pi0.5 model fine-tuning guide | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/Pi0/"},{"title":"π₀.₅ (Pi05) Policy · Hugging Face","url":"https://huggingface.co/docs/lerobot/pi05"},{"title":"[Paper Review] Pi0, Pi0.5, Pi0-FAST - Tracing the Path of Physical Intelligence (PI)","url":"https://bequiet-log.vercel.app/pi-review"},{"title":"Pi0 fast libero checkpoint no longer works with new repo? · Issue #849 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/849"},{"title":"openpi/README.md at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/README.md"}]

Based on the search results, here's what I found about π0 LIBERO from Physical Intelligence:

## Overview

π₀ is a Vision-Language-Action model for general robot control, from Physical Intelligence. π0 Libero is a checkpoint fine-tuned for the Libero benchmark, and can be evaluated on Libero tasks out of the box.

## Key Features

π₀ is designed to be a generalist policy that can understand visual inputs, interpret natural language instructions, and control a variety of different robots across diverse tasks. It uses flow matching to augment pre-trained VLMs with continuous action outputs via flow matching, is trained across 8 distinct robot platforms, and outputs motor commands at up to 50 Hz for real-time dexterous manipulation.

## Training and Fine-tuning

Example fine-tuning configs are provided for π₀, π₀-FAST, and π₀.₅ on LIBERO data. Between 1-20 hours of data was sufficient to tune π0 to a variety of tasks in experiments.

## Open Source Release

Physical Intelligence, the San Francisco-based startup, has open-sourced its π0 robotic foundation model, releasing the code and weights as part of its experimental openpi repository on GitHub. The aim with this release is to enable anyone to experiment with fine-tuning π0 to their own robots and tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "9633c6dc-f161-4f12-8656-09fbac3cf9c2"
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-13T09:46:18.972Z_

<details><summary>↩ Tool result · `toolu_01PPGBwJAdEb1KtpW9HRqJkR`</summary>

```text
Web search results for query: "huggingface lerobot libero 2025 2026"

Links: [{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"LeRobot v0.4.0: Supercharging OSS Robot Learning","url":"https://huggingface.co/blog/lerobot-release-v040"},{"title":"lerobot/xvla-libero · Hugging Face","url":"https://huggingface.co/lerobot/xvla-libero"},{"title":"lerobot/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/lerobot/libero"},{"title":"GitHub - OpenDriveLab/AgiBot-World: [IROS 2025 Best Paper Award Finalist & IEEE TRO 2026] The Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems · GitHub","url":"https://github.com/OpenDriveLab/AgiBot-World"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"Critical Unpatched Flaw Leaves Hugging Face LeRobot Open to Unauthenticated RCE","url":"https://thehackernews.com/2026/04/critical-cve-2026-25874-leaves-hugging.html"},{"title":"lerobot/pi05_libero_finetuned · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned"}]

Based on the search results, here's what I found about Hugging Face LeRobot and LIBERO in 2025-2026:

## LeRobot v0.4.0 Release

LeRobot v0.4.0 delivers a major upgrade for open-source robotics, introducing scalable Datasets v3.0, powerful new VLA models like PI0.5 and GR00T N1.5, and a new plugin system for easier hardware integration. The release also adds support for LIBERO and Meta-World simulations, simplified multi-GPU training, and a new Hugging Face Robot Learning Course.

## LIBERO Integration

LeRobot now officially supports LIBERO, one of the largest open benchmarks for Vision-Language-Action (VLA) policies, boasting over 130 tasks, marking a huge step toward building the go-to evaluation hub for VLAs, enabling easy integration and a unified setup for evaluating any VLA policy.

LIBERO provides 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100.

## Models and Datasets

In a major milestone for open-source robotics, pi0 and pi0.5 policies by Physical Intelligence have been integrated into LeRobot. These Vision-Language-Action (VLA) models represent a significant leap towards addressing open-world generalization in robotics.

Additionally, LIBERO-plus is a robustness benchmark for Vision-Language-Action (VLA) models built on top of LIBERO that systematically stress-tests policies by applying seven independent perturbation dimensions to the original LIBERO task set.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "7045662b-1dc7-42b9-9b9a-20431bcc8890"
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-13T09:46:19.373Z_

<details><summary>↩ Tool result · `toolu_01HoFfwZLKZGL6HuXw6kkrSJ`</summary>

```text
Web search results for query: "diffusion policy LIBERO benchmark results"

Links: [{"title":"nvidia/Cosmos-Policy-LIBERO-Predict2-2B · Hugging Face","url":"https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Efficient Diffusion Transformer Policies with Mixture of Expert Denoisers for Multitask Learning","url":"https://mbreuss.github.io/MoDE_Diffusion_Policy/"},{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/liu_zhu_NeurIPS2023.pdf"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"}]

Here are the key benchmark results for diffusion policy models on the LIBERO benchmark:

## NVIDIA Cosmos-Policy Performance

The Cosmos-Policy-LIBERO-Predict2-2B model achieves state-of-the-art performance on the LIBERO simulation benchmark with a 98.5% average success rate across four task suites. More specifically, the breakdown is: Spatial: 98.1%, Object: 100.0%, Goal: 98.2%, Long: 97.6%.

## Mixture-of-Denoising Experts (MoDE)

MoDE achieves the highest average performance in both LIBERO-10 (Long) and LIBERO-90 benchmarks. By pretraining MoDE on diverse robotics data, it achieves 4.01 on CALVIN ABC and 0.95 on LIBERO-90. It surpasses both CNN-based and Transformer Diffusion Policies by an average of 57% across 4 benchmarks, while using 90% fewer FLOPs and fewer active parameters compared to default Diffusion Transformer architectures.

## General Benchmark Context

It's worth noting that reported state-of-the-art figures (>95% success) reflect performance under clean, nearly identically distributed train/test splits, whereas systematic robustness analyses reveal significant brittleness and a tendency toward memorization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "dfc20725-a666-4100-b48d-06a3e83be751"
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-13T09:46:19.822Z_

<details><summary>↩ Tool result · `toolu_01XHCRvU7FxtQwCXoWDviSjP`</summary>

```text
Web search results for query: "OpenVLA LIBERO results 2025 2026"

Links: [{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"GitHub - CHELabUB/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/CHELabUB/openvla"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Exploring the Robustness of Vision-Language-Action Models against Sensor Attacks | Proceedings of the 2025 Workshop on Large AI Systems and Models with Privacy and Security Analysis","url":"https://dl.acm.org/doi/10.1145/3733800.3763262"},{"title":"LIBERO vs CALVIN (2026): Benchmark Comparison | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/datasets/compare/libero-vs-calvin"},{"title":"LIBERO-Object: Lifelong Learning in Robotic Manipulation","url":"https://www.emergentmind.com/topics/libero-object"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"}]

Based on the search results, here's what I found about OpenVLA LIBERO results from 2025-2026:

## Performance on Standard LIBERO Benchmark

Strong 2025-era VLA policies (OpenVLA, pi0, Octo variants) typically land in the 70-90 percent success range on Spatial, Object, and Goal, and 30-60 percent on LIBERO-100 depending on training recipe.

VLAs exhibit strong performance on the Libero dataset, achieving up to 90% TSR in simple tasks such as LIBERO-Spatial and LIBERO-Object, while OpenVLA-OFT also demonstrates good performance in long-horizon tasks.

## OpenVLA-OFT Improvements

A 2025-03-03 update recommends trying the new OFT recipe for fine-tuning OpenVLA to produce faster and more successful policies. OpenVLA-OFT is a parallel decoding variant enabling simultaneous prediction of all actions in a single forward pass, employing continuous action representations and trained with an L1 regression objective, resulting in faster inference and more precise action generation.

## Robustness Concerns

However, recent 2025 research has identified significant limitations. Despite achieving success rates above 90% on the standard LIBERO benchmark, models nearly collapse under changes to object positions or minor task modifications. While most models fail under perturbations, Pi0.5 achieves a 0.38 success rate in the libero-goal task under position changes, compared to 0 for OpenVLA and Pi0.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "b2eed463-b108-406d-bcd5-c16c925fe012"
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
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Fetching https://huggingface.co/lerobot/smolvla_base",
  "usage": {
    "total_tokens": 22676,
    "tool_uses": 11,
    "duration_ms": 20524
  },
  "last_tool_name": "WebFetch",
  "uuid": "8c5f6d0b-7bec-4179-8419-73a2dc830527",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 129_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EKT65gnSCufQb2n36XucvF`</summary>

```json
{
  "url": "https://huggingface.co/lerobot/smolvla_base",
  "prompt": "Extract the model card details including action space configuration, action_dim, max_action_dim, any config parameters, and details about what action dimensions the base model was trained on."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "48ddd862-b24a-4d7b-b37f-28d9ebf5a059",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017qnPwAkiTFsqrYQrHFb2bj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2358,
      "cache_creation_input_tokens": 4060,
      "cache_read_input_tokens": 16182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4060,
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

_source line 130 · 2026-05-13T09:46:20.521Z_

<details><summary>↩ Tool result · `toolu_01XVZxYvgsSMLQiE1vpAs4zH`</summary>

````text
# SmolVLA Fine-tuning: Training Commands & Configuration

## Primary Training Command

```bash
uv run lerobot/scripts/train.py \
--policy.path=lerobot/smolvla_base \
--dataset.repo_id=PLB/phospho-playground-mono \
--batch_size=256 \
--steps=30000 \
--wandb.enable=true \
--save_freq=5000 \
--wandb.project=smolvla
```

## Key Configuration Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| `batch_size` | 256 | Training batch size |
| `steps` | 30000 | Total training iterations |
| `save_freq` | 5000 | Checkpoint frequency |
| `n_action_steps` | 50 | Must be changed in `config.json` for inference |

## Critical Configuration Requirement

**Before inference, modify the model's `config.json`:**
- Locate: `lerobot/smolvla_base/config.json`
- Change `"n_action_steps": 1,` to `"n_action_steps": 50,`

Without this adjustment, "the inference will be very slow, as the model will only predict one action at a time instead of a sequence of actions."

## Dataset Format

The training example uses the Hugging Face Hub dataset: `PLB/phospho-playground-mono` (a "pick and place" dataset).

## Environment Setup Steps

1. Install `uv` package manager
2. Clone LeRobot repository
3. Create virtual environment with Python 3.10
4. Install dependencies: `uv pip install -e ".[feetech,smolvla]"`

## Hardware Requirements

Training requires "a powerful GPU"—the documentation references NVIDIA A100, though "any modern NVIDIA GPU with sufficient VRAM should work."
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "942677b0-ba1d-4360-92cc-b5e728e1e588"
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
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Fetching https://huggingface.co/docs/lerobot/en/smolvla",
  "usage": {
    "total_tokens": 22677,
    "tool_uses": 12,
    "duration_ms": 21475
  },
  "last_tool_name": "WebFetch",
  "uuid": "8275a7ac-04fb-4256-8676-9789c535ec0a",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 132_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015riUuzLG34uRTFtLQqYL8P`</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/en/smolvla",
  "prompt": "Extract all configuration details especially about action_dim, action space, max_action_dim, how to fine-tune for different action spaces, and any LIBERO-related information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "17c9331a-8dc5-4480-9736-bcb3e71af2c2",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017qnPwAkiTFsqrYQrHFb2bj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2358,
      "cache_creation_input_tokens": 4060,
      "cache_read_input_tokens": 16182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4060,
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

_source line 133 · 2026-05-13T09:46:21.113Z_

<details><summary>↩ Tool result · `toolu_015riUuzLG34uRTFtLQqYL8P`</summary>

````text
# SmolVLA

SmolVLA is Hugging Face’s lightweight foundation model for robotics. Designed for easy fine-tuning on LeRobot datasets, it helps accelerate your development!

  
  
  
    Figure 1. SmolVLA takes as input (i) multiple cameras views, (ii) the
    robot’s current sensorimotor state, and (iii) a natural language
    instruction, encoded into contextual features used to condition the action
    expert when generating an action chunk.
  

## Set Up Your Environment

1. Install LeRobot by following our [Installation Guide](./installation).
2. Install SmolVLA dependencies by running:

   ```bash
   pip install -e ".[smolvla]"
   ```

## Collect a dataset

SmolVLA is a base model, so fine-tuning on your own data is required for optimal performance in your setup.
We recommend recording ~50 episodes of your task as a starting point. Follow our guide to get started: [Recording a Dataset](./il_robots)

In your dataset, make sure to have enough demonstrations per each variation (e.g. the cube position on the table if it is cube pick-place task) you are introducing.

We recommend checking out the dataset linked below for reference that was used in the [SmolVLA paper](https://huggingface.co/papers/2506.01844):

🔗 [SVLA SO100 PickPlace](https://huggingface.co/spaces/lerobot/visualize_dataset?path=%2Flerobot%2Fsvla_so100_pickplace%2Fepisode_0)

In this dataset, we recorded 50 episodes across 5 distinct cube positions. For each position, we collected 10 episodes of pick-and-place interactions. This structure, repeating each variation several times, helped the model generalize better. We tried similar dataset with 25 episodes, and it was not enough leading to a bad performance. So, the data quality and quantity is definitely a key.
After you have your dataset available on the Hub, you are good to go to use our finetuning script to adapt SmolVLA to your application.

## Finetune SmolVLA on your data

Use [`smolvla_base`](https://hf.co/lerobot/smolvla_base), our pretrained 450M model, and fine-tune it on your data.
Training the model for 20k steps will roughly take ~4 hrs on a single A100 GPU. You should tune the number of steps based on performance and your use-case.

If you don't have a gpu device, you can train using our notebook on [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb)

Pass your dataset to the training script using `--dataset.repo_id`. If you want to test your installation, run the following command where we use one of the datasets we collected for the [SmolVLA Paper](https://huggingface.co/papers/2506.01844).

```bash
cd lerobot && lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=${HF_USER}/mydataset \
  --batch_size=64 \
  --steps=20000 \
  --output_dir=outputs/train/my_smolvla \
  --job_name=my_smolvla_training \
  --policy.device=cuda \
  --wandb.enable=true
```

  You can start with a small batch size and increase it incrementally, if the
  GPU allows it, as long as loading times remain short.

Fine-tuning is an art. For a complete overview of the options for finetuning, run

```bash
lerobot-train --help
```

  
  
  
    Figure 2: Comparison of SmolVLA across task variations. From left to right:
    (1) pick-place cube counting, (2) pick-place cube counting, (3) pick-place
    cube counting under perturbations, and (4) generalization on pick-and-place
    of the lego block with real-world SO101.
  

## Evaluate the finetuned model and run it in real-time

Similarly for when recording an episode, it is recommended that you are logged in to the HuggingFace Hub. You can follow the corresponding steps: [Record a dataset](./il_robots).
Once you are logged in, you can run inference in your setup by doing:

```bash
lerobot-record \
  --robot.type=so101_follower \
  --robot.port=/dev/ttyACM0 \ # <- Use your port
  --robot.id=my_blue_follower_arm \ # <- Use your robot id
  --robot.cameras="{ front: {type: opencv, index_or_path: 8, width: 640, height: 480, fps: 30}}" \ # <- Use your cameras
  --dataset.single_task="Grasp a lego block and put it in the bin." \ # <- Use the same task description you used in your dataset recording
  --dataset.repo_id=${HF_USER}/eval_DATASET_NAME_test \  # <- This will be the dataset name on HF Hub
  --dataset.episode_time_s=50 \
  --dataset.num_episodes=10 \
  --dataset.streaming_encoding=true \
  --dataset.encoder_threads=2 \
  # --dataset.vcodec=auto \
  # <- Teleop optional if you want to teleoperate in between episodes \
  # --teleop.type=so100_leader \
  # --teleop.port=/dev/ttyACM0 \
  # --teleop.id=my_red_leader_arm \
  --policy.path=HF_USER/FINETUNE_MODEL_NAME # <- Use your fine-tuned model
```

Depending on your evaluation setup, you can configure the duration and the number of episodes to record for your evaluation suite.


````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "a3dff928-7879-4e4b-9bc5-e49fd234f306"
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
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "description": "Fetching https://huggingface.co/docs/lerobot/en/libero",
  "usage": {
    "total_tokens": 22015,
    "tool_uses": 8,
    "duration_ms": 29106
  },
  "last_tool_name": "WebFetch",
  "uuid": "d73b4a37-acb8-4602-ac48-3777ceebda8f",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 135_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HL3ZX8wzQv7GoSQip4nSRc`</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/en/libero",
  "prompt": "Extract all technical details: how to convert LIBERO HDF5 to LeRobot format, observation keys, action dimensions, episode structure, dataset format, installation steps, training commands, and any code snippets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "c9edaf33-c9b6-44a7-b139-0113fb77bbc3",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014She4KSxa1ipwkcwHcwxnv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1685,
      "cache_creation_input_tokens": 2035,
      "cache_read_input_tokens": 18096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2035,
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

_source line 136 · 2026-05-13T09:46:22.878Z_

<details><summary>↩ Tool result · `toolu_01HL3ZX8wzQv7GoSQip4nSRc`</summary>

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
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "c2f55d2f-3687-44e0-b132-296c3ca5c766"
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-13T09:46:23.542Z_

<details><summary>↩ Tool result · `toolu_01ABKHR7H8JuRjkK4DokJCMC`</summary>

```text
# Action Space Details from SmolVLA Paper

## Action Representation

The paper does not explicitly specify the dimensionality of the action space (e.g., 6D, 7D, joint angles). Instead, it focuses on **action chunks** as the primary abstraction.

### Action Chunk Configuration

SmolVLA predicts sequences of actions denoted as **𝐀_t = (a_t, ..., a_{t+n})**, where actions are grouped into chunks of size **n = 50** by default. The paper states: "the model outputs a chunk of actions" and describes this as "sequences of n (much greater than 1) low-level commands."

The ablation study (Table 12) examines chunk sizes ranging from 1 to 100 steps, finding that "chunk sizes between 10 and 50 strike a good balance between action prediction frequency and performance."

## Robot-Specific Action Details

While specific action dimensions aren't detailed, the paper mentions evaluating on:
- **SO-100/SO-101**: "six degrees of freedom" arms using "position commands"
- **Panda (LIBERO)**: "7-DOF torque-controlled robotic arm"
- **Sawyer (Meta-World)**: "4-DOF controlled robotic arm" where "the policy control[s] the position and state of the gripper"

## Training Configuration

- Flow matching is used as the training objective
- Actions are normalized implicitly through the flow matching framework
- No explicit padding or max_action_dim parameters are mentioned
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "ef5e79ce-262f-4d25-a091-88c1904e8e84"
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
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "description": "Fetching https://raw.githubusercontent.com/Physical-Intell…",
  "usage": {
    "total_tokens": 22016,
    "tool_uses": 9,
    "duration_ms": 30686
  },
  "last_tool_name": "WebFetch",
  "uuid": "fb170b21-e458-4740-813f-d8dea2cbb377",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 139_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EJ3YHEp1JQneGj5smEf5ia`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/convert_libero_data_to_lerobot.py",
  "prompt": "Extract the full conversion script including all functions, observation keys used, action keys, how HDF5 data is read and converted to LeRobot format, and the command-line interface."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "7db1a867-b785-4f68-b59b-a590bc899495",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014She4KSxa1ipwkcwHcwxnv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1685,
      "cache_creation_input_tokens": 2035,
      "cache_read_input_tokens": 18096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2035,
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
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Fetching https://arxiv.org/abs/2502.19645",
  "usage": {
    "total_tokens": 22970,
    "tool_uses": 9,
    "duration_ms": 19448
  },
  "last_tool_name": "WebFetch",
  "uuid": "077f5652-84bf-4919-96d0-94c8259a0de1",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 141_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Kut2Apy1pT2THqNfKaxTui`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.19645",
  "prompt": "Extract: model name and architecture, fine-tuning method (full/LoRA/etc.), LIBERO task suites used, per-suite success rates, training details (epochs, learning rate, batch size, GPU hours/days), action space configuration, whether checkpoints are public"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "6d73c003-1fd6-4b34-a2d4-130955381c98",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01N6c8N9uCVwsZtQ1s3yA4b9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2534,
      "cache_creation_input_tokens": 4192,
      "cache_read_input_tokens": 16170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4192,
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

_source line 142 · 2026-05-13T09:46:24.287Z_

<details><summary>↩ Tool result · `toolu_01EKT65gnSCufQb2n36XucvF`</summary>

````text
# SmolVLA Base Model Card Details

Based on the provided web page content, here's what I can extract about the model configuration:

## Model Overview
- **Model ID**: `lerobot/smolvla_base`
- **Type**: Vision-Language-Action (VLA) model
- **Framework**: LeRobot
- **Paper**: SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (arxiv: 2506.01844)

## Input/Output Specifications

**Inputs:**
- Images (multi-view)
- Proprioceptive/state information
- Optional language instruction

**Outputs:**
- Continuous actions

## Training Configuration
- **Training Objective**: Flow matching
- **Action Representation**: Continuous
- **Intended Use**: Base model for fine-tuning on specific use cases

## Notable Limitations

**The provided webpage does NOT include:**
- Specific `action_dim` values
- `max_action_tokens` configuration
- `chunk_size` defaults
- `n_action_steps` configuration
- Details about what action dimensions the base model was trained on

## Available Configuration Flags

From the fine-tuning section, these policy-specific parameters can be set:
```
-policy.chunk_size=...
-policy.n_action_tokens=...
-policy.max_action_tokens=...
-policy.gradient_checkpointing=true
```

**Note**: For complete action space configuration details, you would need to consult the official model card on Hugging Face Hub directly or check the [LeRobot GitHub repository](https://github.com/huggingface/lerobot) and official documentation at https://huggingface.co/docs/lerobot/.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "d2199fe7-1312-4909-b7ea-fd6429a77802"
}
```

</details>

---

### System

_source line 143_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "description": "Fetching https://huggingface.co/datasets/lerobot/libero",
  "usage": {
    "total_tokens": 22017,
    "tool_uses": 10,
    "duration_ms": 31818
  },
  "last_tool_name": "WebFetch",
  "uuid": "294e8bd1-22ab-4393-a718-a7764286b963",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 144_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AhgKPyKHobTnS2hjyuYDAQ`</summary>

```json
{
  "url": "https://huggingface.co/datasets/lerobot/libero",
  "prompt": "Extract dataset card details: what data is included, format, features/columns, observation keys, action dimensions, number of episodes per task suite, and how to load it."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "ee6ad13d-5c9b-4c5a-bb11-94bf2a4972d9",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014She4KSxa1ipwkcwHcwxnv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1685,
      "cache_creation_input_tokens": 2035,
      "cache_read_input_tokens": 18096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2035,
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

_source line 145 · 2026-05-13T09:46:25.263Z_

<details><summary>↩ Tool result · `toolu_01GAPTsfrrTwats6RcE7eHyW`</summary>

```text
# Technical Details from GitHub Issue #2259

## Action Space Dimensions

The issue mentions specific action dimensions without providing definitive technical specifications:

- **SmolVLA/π₀ pretraining specs**: The user explicitly requests clarification on "exact action and state spaces" but notes these details are not clearly documented.

- **LIBERO dataset actions**: "In HuggingFaceVLA/smol-libero the actions have dimension 7, which doesn't clearly map to 7 joint angles + gripper."

## Action Space Representations

The user's successful OpenVLA implementation used: "action space is defined as ΔEEF pose (Euler rotation) + gripper, and the state as ΔEEF pose (quaternion rotation) + gripper"

However, the document lacks official specifications for SmolVLA's expected action format.

## Fine-tuning Configuration Issues

Key problems identified:
- Model achieved "0% success" on RLBench evaluation despite training convergence
- User suspects misalignment between "state and action spaces for SmolVLA"
- No documented guidance on camera naming conventions affecting performance

## Robot Embodiments

- **SO100/SO101**: Base pretraining robot (7DoF configuration implied)
- **LIBERO**: Used for HuggingFaceVLA/smolvla_libero; unclear if "6DoF or 7DoF Franka setup"
- **Franka Panda**: User's target robot (7DoF + gripper)

The issue essentially highlights the **absence of clear documentation** regarding action dimensions and embodiment-specific configurations needed for successful transfer learning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "75459269-0614-4bce-9e35-87a0cd615006"
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
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Fetching https://huggingface.co/openvla/openvla-7b-finetun…",
  "usage": {
    "total_tokens": 22971,
    "tool_uses": 10,
    "duration_ms": 20586
  },
  "last_tool_name": "WebFetch",
  "uuid": "6a5a6f75-dc54-4857-836c-dc47f462f762",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 147_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01A5UPJfyWF4AheGb9dyeLyG`</summary>

```json
{
  "url": "https://huggingface.co/openvla/openvla-7b-finetuned-libero-spatial",
  "prompt": "Extract: model details, fine-tuning method, training config (epochs, lr, batch size, hardware), action space, LIBERO task suite, success rate results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "3a45904e-dd90-4e68-9954-79ba48fe0777",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01N6c8N9uCVwsZtQ1s3yA4b9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2534,
      "cache_creation_input_tokens": 4192,
      "cache_read_input_tokens": 16170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4192,
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

_source line 148_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Fetching https://huggingface.co/lerobot/pi0_libero_base",
  "usage": {
    "total_tokens": 22972,
    "tool_uses": 11,
    "duration_ms": 21561
  },
  "last_tool_name": "WebFetch",
  "uuid": "e442fc7a-798c-41fd-9d33-0f1939c28d23",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 149_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CywV4ZaZ78c3mEjB2jUM5F`</summary>

```json
{
  "url": "https://huggingface.co/lerobot/pi0_libero_base",
  "prompt": "Extract: model architecture, fine-tuning details, LIBERO task suite and results, training config, action space"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "a70155c0-b724-464b-a6ef-0db04f965dcd",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01N6c8N9uCVwsZtQ1s3yA4b9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2534,
      "cache_creation_input_tokens": 4192,
      "cache_read_input_tokens": 16170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4192,
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

_source line 150_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Fetching https://huggingface.co/nvidia/Cosmos-Policy-LIBER…",
  "usage": {
    "total_tokens": 22973,
    "tool_uses": 12,
    "duration_ms": 22568
  },
  "last_tool_name": "WebFetch",
  "uuid": "4f895415-fa4a-4559-bd87-82deff32d485",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 151_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DeJUNzEjzGCfmCxTw57MQ3`</summary>

```json
{
  "url": "https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B",
  "prompt": "Extract: model architecture, fine-tuning method, LIBERO task suite results (per suite success rates), training details, action space configuration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "45f488bf-bbb7-4bef-8a5f-14a408f78d48",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01N6c8N9uCVwsZtQ1s3yA4b9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2534,
      "cache_creation_input_tokens": 4192,
      "cache_read_input_tokens": 16170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4192,
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

_source line 152_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Searching for RoboVLMs LIBERO benchmark VLA 2025",
  "usage": {
    "total_tokens": 22974,
    "tool_uses": 13,
    "duration_ms": 22948
  },
  "last_tool_name": "WebSearch",
  "uuid": "47072873-b5cb-429e-83c9-cbc431988954",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 153_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DfUqRM7Ps6HTsbXM64nTxB`</summary>

```json
{
  "query": "RoboVLMs LIBERO benchmark VLA 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "cacf74e0-82da-4095-b012-053253bc939c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01N6c8N9uCVwsZtQ1s3yA4b9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2534,
      "cache_creation_input_tokens": 4192,
      "cache_read_input_tokens": 16170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4192,
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

_source line 154_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Searching for LightVLA LIBERO results fine-tuning",
  "usage": {
    "total_tokens": 22975,
    "tool_uses": 14,
    "duration_ms": 23018
  },
  "last_tool_name": "WebSearch",
  "uuid": "699637b7-1338-45b0-879f-6b39e363a860",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 155_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XQyPyhuxoB8vWceGADUeNR`</summary>

```json
{
  "query": "LightVLA LIBERO results fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "b085b0f4-c4e3-4a96-8940-b7f25bad6d20",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01N6c8N9uCVwsZtQ1s3yA4b9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2534,
      "cache_creation_input_tokens": 4192,
      "cache_read_input_tokens": 16170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4192,
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

_source line 156 · 2026-05-13T09:46:28.096Z_

<details><summary>↩ Tool result · `toolu_01MvJuDz4K2CMhdpLoNQdq9y`</summary>

````text
# SmolVLA Fine-Tuning: Code, Configuration, and Process

## Training Command

The author provided a 35-line Google Colab training script:

```python
!git clone https://github.com/huggingface/lerobot.git
!cd lerobot && pip install -e ".[smolvla]"

from huggingface_hub import login
from google.colab import userdata

try:
    token = userdata.get('HF_TOKEN')
    login(token=token, add_to_git_credential=True)
except Exception:
    print("HF_TOKEN secret not found. Please login interactively:")
    login(add_to_git_credential=True)

import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

!python -m lerobot.scripts.lerobot_train \
  --dataset.repo_id Xavier033/new_libero \
  --policy.repo_id Xavier033/new_libero_policy \
  --dataset.revision main \
  --policy.type smolvla \
  --policy.pretrained_path HuggingFaceVLA/smolvla_libero \
  --policy.expert_width_multiplier 0.5 \
  --policy.num_vlm_layers 0 \
  --policy.vlm_model_name HuggingFaceTB/SmolVLM2-500M-Instruct \
  --output_dir lerobot_outputs \
  --job_name smolvla_panda_pick_libero \
  --batch_size 64 \
  --steps 5000 \
  --optimizer.lr 1e-5 \
  --num_workers 4 \
  --save_freq 500 \
  --eval_freq 500 \
  --wandb.enable false \
  --policy.push_to_hub true \
  --save_checkpoint true
```

## Data Format Configuration

The `info.json` structure defines observations and actions:

**Images:**
- Resolution: 256×256 pixels
- Format: 3-channel (RGB)
- Multiple cameras: `image` and `image2`

**Observation State (8 dimensions):**
- Position: x, y, z
- Rotation: roll, pitch, yaw
- Gripper: grip_l, grip_r

**Action Space (7 dimensions):**
- Deltas: dx, dy, dz (position changes)
- Rotation deltas: droll, dpitch, dyaw
- Gripper command: grip

## Critical Statistics File

The author emphasizes using dataset-specific `stats.json` instead of LIBERO's statistics: "action_denorm = action * self.action_stats['std'] + self.action_stats['mean']"

Using incorrect statistics caused "erratic behavior" and required denormalization with the correct dataset's min, max, mean, and standard deviation values.

## Fine-Tuning Process (Step-by-Step)

**1. Data Validation—Three Essential Steps:**

- **Visualization:** Use HuggingFace's visualization utility to check smooth position curves and reasonable velocities
- **Replay Testing:** Execute recorded trajectories on the actual system to expose flaws and validate physical achievability
- **Statistical Checks:** Verify action magnitudes match workspace; identify zero standard deviations indicating pipeline errors

**2. Model Configuration:**
- Expert width multiplier: 0.5
- VLM layers: 0
- Vision model: HuggingFaceTB/SmolVLM2-500M-Instruct
- Training steps: 5,000
- Learning rate: 1e-5
- Batch size: 64

**3. Inference Approach:**
- Action chunking: predict 30 future actions (3 seconds at 10Hz)
- Execute in open-loop sequences
- ~10 seconds computation time per chunk on RTX 3050 Ti

## Key Resources

- Source code: https://github.com/xavier2933/smolVLA_finetune/tree/main
- Dataset: https://huggingface.co/datasets/Xavier033/new_libero
- Training achieved "40% success rate" for grasping with 100 demonstrations (12,000 total steps)

## Critical Lessons

The author stresses that adapting VLAs requires rigorous methodology: "Don't skip data replay" and "ensure that the model knows your system" through proper statistics computation. Infrastructure work exceeds typical expectations.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "f0fed622-58ee-4ed7-9043-642c4dc3a6b3"
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-13T09:46:28.382Z_

<details><summary>↩ Tool result · `toolu_01Kut2Apy1pT2THqNfKaxTui`</summary>

```text
# Extraction Summary

Based on the arXiv page content provided, here's what can be determined:

**Model & Architecture:**
- Base model: OpenVLA
- Fine-tuned variant: OpenVLA-OFT (Optimized Fine-Tuning)

**Fine-Tuning Method:**
The page indicates the approach involves "parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective" but does not specify whether full fine-tuning, LoRA, or other parameter-efficient methods were used.

**LIBERO Performance:**
- "LIBERO simulation benchmark" shows improvement from 76.5% to 97.1% average success rate across four task suites
- Specific per-suite breakdown is not provided in this abstract

**Training Details:**
No information about epochs, learning rate, batch size, or computational requirements (GPU hours/days) appears on this page.

**Action Space Configuration:**
Described as "continuous action representation" with action chunking, but detailed specifications are absent.

**Checkpoint Availability:**
The paper states "We release code for OFT and pretrained model checkpoints" with a reference to a project website, indicating public availability.

**Limitation:** This is an abstract page; comprehensive implementation details likely appear in the full paper PDF.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "890d1f2b-a10f-4e80-ac8d-b7bfe792d767"
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
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Fetching https://github.com/Physical-Intelligence/openpi/i…",
  "usage": {
    "total_tokens": 25919,
    "tool_uses": 13,
    "duration_ms": 29331
  },
  "last_tool_name": "WebFetch",
  "uuid": "3d79a029-5cb4-4b69-b5d7-7631f4332a11",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 159_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TxUY3snxfS5rWMotZoG61K`</summary>

```json
{
  "url": "https://github.com/Physical-Intelligence/openpi/issues/637",
  "prompt": "Extract all technical details about LIBERO action space: is it EEF or joint control? What are the action dimensions? How is gripper action represented? Any details about 7D action breakdown."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "c7b3a988-cdfb-4702-999a-427f98756ade",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BiccXcGm3DEQQeBKt5ffhS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1934,
      "cache_creation_input_tokens": 3625,
      "cache_read_input_tokens": 20242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3625,
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

_source line 160 · 2026-05-13T09:46:28.908Z_

<details><summary>↩ Tool result · `toolu_01EJ3YHEp1JQneGj5smEf5ia`</summary>

```text
# LeRobot Libero Conversion Script Summary

## Full Conversion Script
The script converts Libero datasets (stored in RLDS format) to LeRobot format. The main function accepts a data directory path and optional Hugging Face Hub push capability.

## Observation and Action Keys
**Observations extracted:**
- `image`: 256×256×3 RGB image
- `wrist_image`: 256×256×3 wrist camera view
- `state`: 8-dimensional float32 proprioceptive state

**Actions:**
- 7-dimensional float32 action vector (Panda robot)

**Metadata:**
- `task`: Language instruction decoded from episodes

## Data Reading and Conversion Process
Rather than HDF5, this script reads from RLDS-formatted datasets using TensorFlow Datasets. The conversion workflow:

1. Loads raw Libero datasets via `tfds.load()`
2. Iterates through episodes and individual steps
3. Extracts observations, actions, and task descriptions
4. Calls `dataset.add_frame()` to append each timestep
5. Invokes `dataset.save_episode()` after completing each episode

## Command-Line Interface
The script uses the `tyro` library for CLI argument parsing:

**Basic usage:** `uv run examples/libero/convert_libero_data_to_lerobot.py --data_dir /path/to/data`

**With Hub upload:** `uv run examples/libero/convert_libero_data_to_lerobot.py --data_dir /path/to/data --push_to_hub`

## Key Configuration
- FPS: 10 Hz
- Robot type: Panda
- Image writer threads: 10
- Image writer processes: 5
- Multiple Libero datasets combined into single training dataset
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "4f9127f5-1a3d-46c1-9c8d-2e59bedcfd31"
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-13T09:46:29.879Z_

<details><summary>↩ Tool result · `toolu_01A5UPJfyWF4AheGb9dyeLyG`</summary>

````text
# OpenVLA 7B Fine-Tuned on LIBERO-Spatial - Model Details

## Model Information
- **Base Model**: OpenVLA 7B
- **Fine-tuning Method**: LoRA (Low-Rank Adaptation)
- **LoRA Rank**: 32
- **LoRA Dropout**: 0.0
- **Model Size**: 8B parameters
- **Tensor Type**: BF16
- **License**: MIT

## Training Configuration

| Parameter | Value |
|-----------|-------|
| **Hardware** | 8 x A100 GPUs (80GB memory) |
| **Learning Rate** | 5e-4 |
| **Batch Size** | 128 (8 GPUs × 16 samples each) |
| **Training Steps** | 50,000 gradient steps |
| **Shuffle Buffer Size** | 100,000 |
| **Quantization** | None (train or test) |
| **Gradient Accumulation** | Disabled (grad_accumulation_steps == 1) |

## Training Details
- **Dataset**: LIBERO-Spatial (from LIBERO simulation benchmark)
- **Image Augmentations**: Random crop, color jitter
- **Quantization**: No quantization at train or test time

## Action Space & Results
⚠️ **Note**: The provided web page content does not include:
- Specific action space details
- LIBERO task suite breakdown
- Success rate results/benchmarks

For detailed evaluation results and task specifications, refer to the [OpenVLA GitHub README](https://github.com/openvla/openvla/blob/main/README.md) and the [OpenVLA paper (arXiv:2406.09246)](https://arxiv.org/abs/2406.09246).

## Quick Start
```python
from transformers import AutoModelForVision2Seq

model = AutoModelForVision2Seq.from_pretrained(
    "openvla/openvla-7b-finetuned-libero-spatial",
    trust_remote_code=True,
    dtype="auto"
)
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "271a04ae-d8cc-40fd-9b6e-c9602c00c401"
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-13T09:46:29.917Z_

<details><summary>↩ Tool result · `toolu_01P7aVWCfTqnwc1iNVadXgoK`</summary>

````text
# SmolVLA: Key Technical Details

## Model Architecture

SmolVLA consists of two core components:

### 1. Vision-Language Model (VLM) Backbone
- **Base Model**: SmolVLM2-500M-Video-Instruct
- **Vision Encoder**: SigLIP
- **Language Decoder**: SmolLM2-1.7B-Instruct
- **Visual Token Reduction**: Limited to **64 tokens per frame** (vs. 1024) using PixelShuffle
- **Layer Skipping**: Uses features from intermediate layers (configurable to **half the total layers**) for faster inference

### 2. Action Expert
- **Architecture**: Flow Matching Transformer (~100M parameters)
- **Hidden Size**: 75% of VLM's hidden dimension
- **Attention Design**: Interleaved cross-attention (CA) and self-attention (SA) blocks
  - Cross-attention: actions attend to VLM features
  - Self-attention: actions attend causally to past actions (temporal smoothness)
- **Action Representation**: Continuous action sequences (non-autoregressive prediction)
- **Training Objective**: Flow matching (guides noisy samples back to ground truth)

## Action Dimensions & Training Data

**Model Size**: 450M parameters total

**Training Data**:
- Source: LeRobot Community Datasets (publicly available, compatibly licensed)
- Volume: ~10 million frames (~487 high-quality datasets)
- **Order of magnitude smaller** than other VLAs (other models use 100M+ frames)
- Primary embodiment: SO100 robotic arm (6 DOF)
- Frame rate: Standardized at 30 FPS

**Data Processing**:
- Task annotations improved using Qwen2.5-VL-3B-Instruct (rewritten to <30 characters, action-verb prefixed)
- Camera views standardized: `OBS_IMAGE_1` (top-down), `OBS_IMAGE_2` (wrist-mounted), `OBS_IMAGE_3+` (additional)

## Pretraining vs Fine-tuning

### Pretraining Phase
- Trained on general manipulation data from LeRobot community datasets
- Impact on SO100: **51.7% → 78.3% success** (+26.6% absolute improvement)

### Fine-tuning Phase
- Task-specific post-training on target tasks
- Further boosts performance through multitask learning
- Demonstrates strong task transfer in low-data regimes

## Training Configuration Example

```python
# Fine-tune pretrained model
python lerobot/scripts/train.py \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=lerobot/svla_so100_stacking \
  --batch_size=64 \
  --steps=20000  # 10% of training budget

# Train from scratch
python lerobot/scripts/train.py \
  --policy.type=smolvla \
  --dataset.repo_id=lerobot/svla_so100_stacking \
  --batch_size=64 \
  --steps=200000
```

## Performance Results

### Simulation Benchmarks
- Outperforms larger VLAs on LIBERO and Meta-World
- Matches or exceeds ACT baseline

### Real-World Tasks (SO100)
- **~78% success rate** on pick-place, stacking, sorting
- Handles in-distribution and out-of-distribution object configurations

### Generalization (SO101 - Different Embodiment)
- Successfully generalizes to new robot arm (SO101)
- Outperforms ACT baseline on unseen embodiments

### Asynchronous Inference
- **30% faster task completion** (9.7s vs. 13.75s sync)
- **2× task throughput** (19 vs. 9 cubes in fixed time)
- Similar success rates (~78%) between sync and async modes

## Installation

```bash
git clone https://github.com/huggingface/lerobot.git
cd lerobot
pip install -e ".[smolvla]"
```

## Model Loading

```python
from lerobot.common.policies.smolvla.modeling_smolvla import SmolVLAPolicy
policy = SmolVLAPolicy.from_pretrained("lerobot/smolvla_base")
```

## Key Innovation: Asynchronous Inference

Decouples action execution from model inference:
1. Early trigger when action queue drops below threshold
2. Non-blocking parallel threads for inference
3. Chunk fusion to avoid jitter on overlapping actions

This enables responsive, real-time control without idle time.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "74fc4061-d432-444b-a2a2-619ed11b66b7"
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
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Fetching https://huggingface.co/docs/lerobot/main/libero_p…",
  "usage": {
    "total_tokens": 25960,
    "tool_uses": 14,
    "duration_ms": 30856
  },
  "last_tool_name": "WebFetch",
  "uuid": "7b070989-01e2-44c9-b3db-f2f11341bcb1",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 164_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SQXJv2vzG4RjpTdT8dXK4q`</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/main/libero_plus",
  "prompt": "Extract all action space details for LIBERO: action dimensions, what each dimension represents, delta vs absolute, gripper representation, any configuration parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "af6e4a57-334d-4837-8d94-a88928111d04",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BiccXcGm3DEQQeBKt5ffhS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1934,
      "cache_creation_input_tokens": 3625,
      "cache_read_input_tokens": 20242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3625,
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

_source line 165 · 2026-05-13T09:46:30.629Z_

<details><summary>↩ Tool result · `toolu_01SQXJv2vzG4RjpTdT8dXK4q`</summary>

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
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "b1a36f64-d1e9-4e93-82cf-73875f93f36e"
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-13T09:46:31.005Z_

<details><summary>↩ Tool result · `toolu_01CywV4ZaZ78c3mEjB2jUM5F`</summary>

````text
# π₀ (Pi0) Model - Key Details

## Model Architecture

**π₀** is a Vision-Language-Action (VLA) foundation model from Physical Intelligence designed for robot control.

- **Inputs:** Multi-view images, proprioceptive/state information, optional language instructions
- **Outputs:** Continuous actions
- **Training Objective:** Flow matching
- **Action Representation:** Continuous
- **Model Size:** 4B parameters
- **Intended Use:** Base model for fine-tuning on specific robotics tasks

## Fine-tuning Configuration

Training command with configurable parameters:

```bash
lerobot-train \
  --dataset.repo_id=${HF_USER}/&lt;dataset> \
  --output_dir=./outputs/[RUN_NAME] \
  --job_name=[RUN_NAME] \
  --policy.repo_id=${HF_USER}/&lt;desired_policy_repo_id> \
  --policy.path=lerobot/pi0_libero_base \
  --policy.dtype=bfloat16 \
  --policy.device=cuda \
  --steps=100000 \
  --batch_size=4
```

**Policy-specific flags:**
- `-policy.chunk_size=...`
- `-policy.n_action_steps=...`
- `-policy.max_action_tokens=...`
- `-policy.gradient_checkpointing=true`

## LIBERO Task Suite & Evaluation

Evaluation in LIBERO simulation environment:

```bash
lerobot-eval \
  --policy.path=lerobot/pi0_libero_base \
  --env.type=libero \
  --env.task=libero_object \
  --eval.batch_size=1 \
  --eval.n_episodes=20
```

The model is specifically trained on the LIBERO benchmark dataset (`lerobot/libero`) for evaluating manipulation tasks.

## Training Configuration Example

```python
policy.train()
batch = dict(dataset[0])
batch = preprocess(batch)
loss, outputs = policy.forward(batch)
loss.backward()
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "13259318-bc39-4bed-9c76-5c94083edcda"
}
```

</details>

---

### System

_source line 167_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Fetching https://medium.com/correll-lab/fine-tuning-smolvl…",
  "usage": {
    "total_tokens": 26001,
    "tool_uses": 15,
    "duration_ms": 32632
  },
  "last_tool_name": "WebFetch",
  "uuid": "ddf3f81c-ff5a-4435-a857-74e5a183328b",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 168_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VFstGmhAj7YqwjYXa1XD53`</summary>

```json
{
  "url": "https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632",
  "prompt": "Extract all details about action dimensions used, how action_dim is configured, any mismatch between SmolVLA default and the target environment, and specific config parameters used."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "81b6b4d4-53f6-4535-b6f1-747ceb89d4e9",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BiccXcGm3DEQQeBKt5ffhS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1934,
      "cache_creation_input_tokens": 3625,
      "cache_read_input_tokens": 20242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3625,
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

_source line 169 · 2026-05-13T09:46:33.327Z_

<details><summary>↩ Tool result · `toolu_01XQyPyhuxoB8vWceGADUeNR`</summary>

```text
Web search results for query: "LightVLA LIBERO results fine-tuning"

Links: [{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"LightVLA","url":"https://liauto-research.github.io/LightVLA/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"},{"title":"openvla/openvla-7b-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-10"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"openvla/openvla-7b-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-spatial"},{"title":"LightVLA/LIBERO.md at main · LiAutoAD/LightVLA","url":"https://github.com/LiAutoAD/LightVLA/blob/main/LIBERO.md"},{"title":"GitHub - LiAutoAD/LightVLA: Official Code for LightVLA (ICRA 2026)","url":"https://github.com/LiAutoAD/LightVLA"}]

Based on the search results, here's what I found about LightVLA's fine-tuning results on the LIBERO benchmark:

## LightVLA Fine-Tuning Results on LIBERO

LightVLA reduces FLOPs and latency by 59.1% and 38.2% respectively, with a 2.6% improvement in task success rate on the LIBERO benchmark. More specifically, compared to OpenVLA-OFT, LightVLA not only reduces FLOPs and latency by 59.1% and 38.2%, but also improves success rate by 2.9%.

## Key Technical Achievements

LightVLA is a differentiable token pruning framework for vision-language-action models that addresses efficiency challenges through adaptive, performance-driven pruning of visual tokens. Through fine-tuning, LightVLA learns to preserve the most informative visual tokens while pruning tokens which do not contribute to task execution, thereby improving efficiency and performance simultaneously.

Notably, compared to OpenVLA-OFT which consumes 512 visual tokens, LightVLA only retains 78 visual tokens on average, indicating that most visual tokens are not contributing to overall performance.

## Performance Advantages

LightVLA delivers the best performance across all tasks and outperforms its baseline model, OpenVLA-OFT on all task suites by a large margin. Among all VLA acceleration approaches, LightVLA is the only one that boosts performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "0c4aedae-5175-4d40-bf2a-40a843285ddd"
}
```

</details>

---

### System

_source line 170_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Fetching https://github.com/huggingface/lerobot/blob/main/…",
  "usage": {
    "total_tokens": 27723,
    "tool_uses": 13,
    "duration_ms": 42584
  },
  "last_tool_name": "WebFetch",
  "uuid": "850a841a-3679-4d8a-81fd-989dec35528c",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 171_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012YEZPVpFBcjsVcBdJSzW1L`</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/peft_training.mdx",
  "prompt": "Extract all LoRA/PEFT parameters, training commands, quantization options, target modules, full fine-tuning vs LoRA differences for SmolVLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "eb53da76-1176-4202-9484-408634c17eea",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Q44uo4N2HTpsYxTAQmkz6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6186,
      "cache_read_input_tokens": 21457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6186,
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

_source line 172 · 2026-05-13T09:46:33.739Z_

<details><summary>↩ Tool result · `toolu_01AhgKPyKHobTnS2hjyuYDAQ`</summary>

````text
# LeRobot LIBERO Dataset Overview

## Dataset Summary
The **lerobot/libero** dataset is a robotics manipulation dataset containing **273,465 frames** from **1,693 episodes** across **40 tasks**, collected using a Franka Panda robot.

## Dataset Structure

### Core Metadata
- **Total Episodes**: 1,693
- **Total Frames**: 273,465
- **Total Tasks**: 40
- **FPS**: 10.0
- **Split**: train (all 1,693 episodes)
- **Format**: Parquet
- **Size**: ~1.94 GB

### Features & Columns

| Feature | Data Type | Shape | Description |
|---------|-----------|-------|-------------|
| `observation.images.image` | video | [256, 256, 3] | RGB camera feed (codec: av1) |
| `observation.images.image2` | video | [256, 256, 3] | Second RGB camera feed |
| `observation.state` | float32 | [8] | Robot state vector (8D) |
| `action` | float32 | [7] | Robot action vector (7D) |
| `timestamp` | float32 | [1] | Frame timestamp |
| `frame_index` | int64 | [1] | Frame index within episode |
| `episode_index` | int64 | [1] | Episode ID (0-1,692) |
| `task_index` | int64 | [1] | Task ID (0-39) |
| `index` | int64 | [1] | Global row index |

### Observation Keys
- **observation.state**: 8-dimensional state vector (likely joint positions/angles)
- **observation.images.image**: 256×256 RGB video stream
- **observation.images.image2**: Second 256×256 RGB camera view

### Action Dimensions
- **action**: 7-dimensional action vector (consistent with 7-DOF Franka Panda arm)

## Data Format Example
```
Row with observation.state:
[-0.053, 0.007, 0.678, 3.140, 0.001, -0.089, 0.038, -0.038]

Corresponding action:
[0.016, 0, 0, 0, 0, 0, -1]
```

## How to Load

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("lerobot/libero")

# Access training split
train_split = dataset["train"]

# View sample
sample = train_split[0]
print(sample.keys())
# dict_keys(['observation.state', 'action', 'timestamp', 
#            'frame_index', 'episode_index', 'index', 'task_index',
#            'observation.images.image', 'observation.images.image2'])
```

## Key Characteristics
- **Robot Type**: Franka Panda (panda)
- **Video Codec**: AV1 (efficient compression)
- **Video Format**: YUV420p (8-bit)
- **Chunk Size**: 1,000 frames per file
- **License**: Apache 2.0

## Related Resources
- GitHub: [LeRobot](https://github.com/huggingface/lerobot)
- Popular models trained on this dataset: `lerobot/smolvla_libero`, `alexanta/pi0.5_libero`
- Part of LeRobot benchmarks collection
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "d1c3912b-7072-4e54-8d14-d7af34419199"
}
```

</details>

---

### System

_source line 173_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Fetching https://io-ai.tech/platform/en/guides/Pipeline/Le…",
  "usage": {
    "total_tokens": 27724,
    "tool_uses": 14,
    "duration_ms": 44012
  },
  "last_tool_name": "WebFetch",
  "uuid": "36b6051e-5178-4904-a38c-b66a4ebfc0d6",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 174_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CZfmoeiHa9o3jEPSNtE7SG`</summary>

```json
{
  "url": "https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/",
  "prompt": "Extract: training commands, action_dim, config parameters, data format, fine-tuning steps for SmolVLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "b9cbb667-3916-4cef-b6e4-1d911494202c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Q44uo4N2HTpsYxTAQmkz6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6186,
      "cache_read_input_tokens": 21457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6186,
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

_source line 175 · 2026-05-13T09:46:34.985Z_

<details><summary>↩ Tool result · `toolu_01DfUqRM7Ps6HTsbXM64nTxB`</summary>

```text
Web search results for query: "RoboVLMs LIBERO benchmark VLA 2025"

Links: [{"title":"VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.pdf"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"How brittle are the VLA models in robotics | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"}]

Based on the search results, here's what I found about RoboVLMs, LIBERO benchmark, and VLA in 2025:

## LIBERO Benchmark Overview

LIBERO has emerged as the dominant benchmark and is now the most widely adopted protocol for evaluating VLA models, with its standardized task suite and unified reporting metrics making it the de facto standard for performance comparison.

## Recent Developments in 2025

Several important benchmark extensions and evaluations have emerged in 2025:

**LIBERO-Plus**: This is a comprehensive benchmark designed to establish a rigorous leaderboard for evaluating generalization capabilities across key vulnerability dimensions, constructed through expanding the original LIBERO benchmark through seven distinct perturbation factors, followed by task filtering and category balancing. The benchmark contains 10,030 tasks spanning seven perturbation dimensions.

**LIBERO-PRO**: This benchmark enables more comprehensive assessment of VLA models by designing evaluation scenarios along four key dimensions: manipulated objects, initial states, task instructions, and environments, introducing carefully designed perturbations to original LIBERO tasks to simulate real-world situations.

**LIBERO-Para**: A controlled benchmark for evaluating paraphrase robustness in VLA models, addressing how VLA models handle linguistic variations in instructions.

## Key Findings on VLA Model Robustness

Current VLA models remain brittle, showing particular vulnerability to camera and robot state changes, largely ignore language instructions, and exhibit positional bias rather than genuine semantic understanding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "e88d61ed-3f35-4d98-a013-4b27f152b925"
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-13T09:46:35.398Z_

<details><summary>↩ Tool result · `toolu_01TxUY3snxfS5rWMotZoG61K`</summary>

```text
# LIBERO Action Space Technical Details

Based on the GitHub issue, the action space representation in LIBERO remains **ambiguous and contradictory**:

## Stated vs. Actual Representation

**Documentation claim:** Actions are in end-effector (EEF) space

**User observation:** State and action values have drastically different numerical ranges, suggesting they may use different representations

## Action Dimensions

The issue references a 7-DOF Panda arm with an expected action structure of:
- 6D end-effector pose (3D position + 3D orientation)
- 2D gripper control

However, the exact breakdown and whether orientation is represented as quaternions or axis-angles in the action vector remains unspecified in this content.

## Gripper Action

The gripper is described as a "2D" component, but specific details about how gripper actions are encoded or their control range are not provided.

## Core Problem

The issue highlights a fundamental inconsistency: state values appear to be in joint space (with values near π), while the inference pipeline constructs observations using EEF representations: `"obs['robot0_eef_pos']"` and `"obs['robot0_eef_quat']"`. This mismatch creates confusion about what delta-actions actually represent physically.

**No definitive technical specification is provided in this issue.**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "79c6719d-149e-42a0-abb3-d60cc81a7458"
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-13T09:46:35.527Z_

<details><summary>↩ Tool result · `toolu_01DeJUNzEjzGCfmCxTw57MQ3`</summary>

```text
# Cosmos-Policy-LIBERO-Predict2-2B: Key Technical Details

## Model Architecture

**Architecture Type:** Diffusion transformer with latent video diffusion
- **Base Model:** Fine-tuned from [Cosmos-Predict2-2B-Video2World](https://huggingface.co/nvidia/Cosmos-Predict2-2B-Video2World)
- **Parameters:** 2B
- **Key Adaptation:** Actions, proprioceptive states, and values are encoded as latent frames and injected directly into the video model's latent diffusion sequence

## Fine-Tuning Method

**Single-stage fine-tuning** with no architectural modifications:
- **Training Steps:** 40,000 gradient steps
- **Batch Size:** 1,920 (global)
- **Hardware:** 64 H100 GPUs
- **Training Time:** ~48 hours
- **Optimization:** Full model fine-tuning (all weights updated)
- **Noise Distribution:** Hybrid log-normal-uniform (modified from base model)
- **Training Split:** 50/25/25 for policy/world model/value function objectives

## LIBERO Benchmark Results (Per Suite)

| Task Suite | Success Rate |
|------------|-------------|
| LIBERO-Spatial | 98.1% |
| LIBERO-Object | 100.0% |
| LIBERO-Goal | 98.2% |
| LIBERO-Long | 97.6% |
| **Average** | **98.5%** |

*Success rates averaged over 500 trials per suite (10 tasks × 50 episodes) across 3 random seeds (6,000 trials total)*

## Action Space Configuration

**Output:**
- **Action Chunk Size:** 16 timesteps
- **Action Dimensions:** 7-dimensional (6-DoF end-effector control + 1 gripper)
- **Denoising Steps:** 5 (configurable without retraining)
- **Noise Range:** σ_min = 4.0, σ_max = 80.0
- **Generation Mode:** Parallel (action, future state, and value generated simultaneously)

**Input:**
- Text: Natural language task description
- Images: 224×224 RGB from dual cameras (third-person + wrist-mounted)
- Proprioception: 9-dimensional state (2 gripper joints + 3 position + 4 quaternion)

## Training Dataset

**LIBERO-Cosmos-Policy:**
- 4 task suites (Spatial, Object, Goal, Long)
- 500 demonstrations per suite (50 demos × 10 tasks)
- Collection: Human-teleoperated demonstrations in simulation
- Successful demonstrations used for policy training; all demonstrations for world model and value function training
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "28442005-797c-4434-aee7-1ca996231679"
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
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Fetching https://colab.research.google.com/github/huggingf…",
  "usage": {
    "total_tokens": 27725,
    "tool_uses": 15,
    "duration_ms": 44763
  },
  "last_tool_name": "WebFetch",
  "uuid": "ed4e4f2f-4adc-44b7-9d9b-6be7e3a97240",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 179_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PtemddKQrsUtfyAUyNACrw`</summary>

```json
{
  "url": "https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb",
  "prompt": "Extract all training commands, configuration, data format, step-by-step notebook content for SmolVLA training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "7f212217-47ea-4be2-a5e6-4971336fbf32",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Q44uo4N2HTpsYxTAQmkz6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6186,
      "cache_read_input_tokens": 21457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6186,
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
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Fetching https://github.com/huggingface/lerobot/blob/main/…",
  "usage": {
    "total_tokens": 27726,
    "tool_uses": 16,
    "duration_ms": 45566
  },
  "last_tool_name": "WebFetch",
  "uuid": "ced25e1e-70e1-4c5d-91ce-d301ec0159f4",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 181_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BCqeC5ShbagNnBqNqEsbsv`</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx",
  "prompt": "Extract full content: architecture, fine-tuning commands, config parameters, action dimensions, data requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "b80beeff-bab2-4721-a946-c0ff620ec362",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Q44uo4N2HTpsYxTAQmkz6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6186,
      "cache_read_input_tokens": 21457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6186,
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

_source line 182_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "description": "Fetching https://huggingface.co/datasets/HuggingFaceVLA/li…",
  "usage": {
    "total_tokens": 25957,
    "tool_uses": 11,
    "duration_ms": 44317
  },
  "last_tool_name": "WebFetch",
  "uuid": "38fcd7f9-1d66-470d-b897-6cfe670a047a",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 183_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Vvs7RmotmaE18tj7PuhuAy`</summary>

```json
{
  "url": "https://huggingface.co/datasets/HuggingFaceVLA/libero",
  "prompt": "Extract full dataset card: what task suites are included, number of episodes per suite, format details, how it differs from lerobot/libero, observation keys, and how to use it."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "ddcd2d53-a3a0-4232-92b3-3fb5c35eca78",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0112uj6kaL7jDUaxgm4U1miF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5554,
      "cache_read_input_tokens": 20131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5554,
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

### Tool result

_source line 184 · 2026-05-13T09:46:38.057Z_

<details><summary>↩ Tool result · `toolu_01VFstGmhAj7YqwjYXa1XD53`</summary>

````text
# Action Dimensions and Configuration Details

## Action Vector Specification

The author's simulated Panda environment uses a **7-dimensional action vector**:

```
"action": {
    "dtype": "float32",
    "shape": [7],
    "names": ["dx", "dy", "dz", "droll", "dpitch", "dyaw", "grip"]
}
```

This represents six degrees of freedom for end-effector movement plus one gripper dimension.

## Critical Configuration Issues

**Statistics Mismatch:** The most significant problem identified was using incorrect normalization statistics. The author initially applied `stats.json` from the LIBERO dataset to their custom environment, causing severe action scaling errors. As noted: "Pointing my inference script at the `stats.json` file for my dataset dramatically reduced the erratic behavior of the arm by scaling the actions to the dimensions of my arm."

**Key Training Parameters:**
- Batch size: 64
- Learning rate: 1e-5
- Expert width multiplier: 0.5
- VLM layers: 0
- Action chunk size: 30 (3 seconds at 10Hz execution frequency)

## Environment-to-Training Distribution Misalignment

While both systems used Franka Emika Panda arms, significant visual differences existed: different arm coloring, background variations, and gripper visibility differences compared to LIBERO training data. The author successfully compensated through systematic data collection and proper statistics computation rather than architectural modifications.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "a60fc196-7194-4ba9-9fc3-e1fcfeb71ac3"
}
```

</details>

---

### Tool result

_source line 185 · 2026-05-13T09:46:38.656Z_

<details><summary>↩ Tool result · `toolu_01PtemddKQrsUtfyAUyNACrw`</summary>

```text
I cannot extract the requested training commands, configuration, data format, or notebook content because the provided web page content only shows a Google Colab sign-in page header and a link to a notebook.

The actual notebook content is not included in the material provided. To access the SmolVLA training details, you would need to:

1. Click the sign-in link and authenticate with your Google account
2. Open the full notebook at the GitHub repository path shown (huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb)
3. View the complete notebook cells containing the training instructions

I can only work with content that's directly provided to me. If you'd like me to analyze the SmolVLA training notebook, please share the actual notebook text or cells.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "d6bb2cdb-4989-42fc-b6b4-0c28e4b21fc1"
}
```

</details>

---

### Tool result

_source line 186 · 2026-05-13T09:46:38.740Z_

<details><summary>↩ Tool result · `toolu_012YEZPVpFBcjsVcBdJSzW1L`</summary>

````text
# LoRA/PEFT Parameters for SmolVLA Training

## Key Parameters

**LoRA-specific settings:**
- `--peft.method_type=LORA`: Selects LoRA as the adaptation method
- `--peft.r=64`: Specifies the rank of the low-rank adapter matrices
- `--peft.lora_alpha=64`: Sets the scaling factor (scaling = lora_alpha / r)

**Target modules configuration:**
By default, the system focuses on "the `q_proj` and `v_proj` layers of the LM expert in SmolVLA" plus state and action projection matrices.

Custom targeting example:
```
--peft.target_modules='(model\.vlm_with_expert\.lm_expert\..*\.(down|gate|up)_proj|.*\.(state_proj|action_in_proj|action_out_proj|action_time_mlp_in|action_time_mlp_out))'
```

## Training Command Example

```bash
lerobot-train \
 --policy.path=lerobot/smolvla_base \
 --policy.optimizer_lr=1e-3 \
 --policy.scheduler_decay_lr=1e-4 \
 --steps=100000 \
 --batch_size=32 \
 --peft.method_type=LORA \
 --peft.r=64 \
 --peft.lora_alpha=64
```

## Full Fine-Tuning vs LoRA

The document notes that "learning rate...can usually be scaled by a factor of 10 compared to the learning rate used for full fine-tuning." Additionally, you can specify layers for traditional fine-tuning using `--peft.full_training_modules=["state_proj"]`.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "377910c9-863e-4985-bd4d-0fd79da85aa8"
}
```

</details>

---

### System

_source line 187_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "description": "Fetching https://github.com/Tavish9/any4lerobot/blob/main/…",
  "usage": {
    "total_tokens": 26027,
    "tool_uses": 12,
    "duration_ms": 46049
  },
  "last_tool_name": "WebFetch",
  "uuid": "1f02b35b-d9d7-4ea6-8126-9798ec94738d",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 188_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TiYQfRynb5XGyALqW4LRVb`</summary>

```json
{
  "url": "https://github.com/Tavish9/any4lerobot/blob/main/libero2lerobot/README.md",
  "prompt": "Extract all details: how to convert LIBERO HDF5 to LeRobot format, what scripts to run, command syntax, observation keys mapped, dependencies required."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "1f878340-6b93-4c7f-806f-5152f268eb1c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0112uj6kaL7jDUaxgm4U1miF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5554,
      "cache_read_input_tokens": 20131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5554,
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

_source line 189_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Fetching https://arxiv.org/html/2502.19645v1",
  "usage": {
    "total_tokens": 27539,
    "tool_uses": 15,
    "duration_ms": 34920
  },
  "last_tool_name": "WebFetch",
  "uuid": "24de6355-cd18-420c-b7bd-3cb20fe5d660",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 190_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018HtNq3mDFEJAYgNSh5Mtva`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.19645v1",
  "prompt": "Extract detailed results tables: per-suite success rates for OpenVLA-OFT and all baselines on LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long/10. Also extract training hyperparameters: learning rate, batch size, gradient steps, GPU hardware, training time, LoRA rank, action space details (dimensions, chunk size, tokenization method)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "e4dfa568-0aab-48b5-b44e-b55ddbd08f9c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JUAuhj4U6cPrsWU1Xz3Ydq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1874,
      "cache_creation_input_tokens": 5180,
      "cache_read_input_tokens": 20362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5180,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
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
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "description": "Fetching https://huggingface.co/datasets/physical-intellig…",
  "usage": {
    "total_tokens": 26097,
    "tool_uses": 13,
    "duration_ms": 46928
  },
  "last_tool_name": "WebFetch",
  "uuid": "838b0c2e-e523-4f57-9b7a-8fc80b935858",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 192_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015HS2ZDAYT3YxgyLzCDNq4i`</summary>

```json
{
  "url": "https://huggingface.co/datasets/physical-intelligence/libero",
  "prompt": "Extract the full dataset card: what suites are included, data format, how it was converted to LeRobot format, features/columns, number of episodes, and how to load it."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "dd4ef28f-601c-4d4d-8d62-ca63b8161d0b",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0112uj6kaL7jDUaxgm4U1miF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5554,
      "cache_read_input_tokens": 20131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5554,
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

_source line 193_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Fetching https://liauto-research.github.io/LightVLA/",
  "usage": {
    "total_tokens": 27583,
    "tool_uses": 16,
    "duration_ms": 36119
  },
  "last_tool_name": "WebFetch",
  "uuid": "0a0e85dc-6577-41fb-94ec-fe98c77666bd",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 194_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Qg85CyGW2ZbEQWR4UUfv52`</summary>

```json
{
  "url": "https://liauto-research.github.io/LightVLA/",
  "prompt": "Extract: model architecture, LIBERO per-suite success rates, training details, fine-tuning method, action space, comparison with baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "44e915fb-1ba8-47a4-84ba-0c6036d0328f",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JUAuhj4U6cPrsWU1Xz3Ydq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1874,
      "cache_creation_input_tokens": 5180,
      "cache_read_input_tokens": 20362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5180,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
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

_source line 195_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Fetching https://huggingface.co/docs/lerobot/libero",
  "usage": {
    "total_tokens": 29287,
    "tool_uses": 16,
    "duration_ms": 41928
  },
  "last_tool_name": "WebFetch",
  "uuid": "8f1ccb33-57bf-4be1-8423-cec78169323d",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 196_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WqGjJcKSmSyaCd2d6wy3zw`</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/libero",
  "prompt": "Extract the action space specification: how many dimensions, what each dimension represents, control mode (relative/absolute), and any configuration parameters for SmolVLA fine-tuning on LIBERO."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "335510e7-b94f-4d72-95cf-b12e854147b2",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EorqTiBoGoLYtkeD5McLkD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5172,
      "cache_read_input_tokens": 23867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5172,
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

_source line 197 · 2026-05-13T09:46:41.567Z_

<details><summary>↩ Tool result · `toolu_01WqGjJcKSmSyaCd2d6wy3zw`</summary>

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
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "04cc21b3-7bdd-4bb1-9d92-5133b2da208a"
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
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Fetching https://arxiv.org/html/2510.13626v1",
  "usage": {
    "total_tokens": 27627,
    "tool_uses": 17,
    "duration_ms": 37350
  },
  "last_tool_name": "WebFetch",
  "uuid": "adf80adf-6be8-497d-961c-61a54b4a824b",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 199_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01W33xCxCkY8atzBzXsBBUZQ`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.13626v1",
  "prompt": "Extract the results table comparing different VLA models on standard LIBERO benchmark: model names, per-suite success rates (Spatial, Object, Goal, Long), and any training details mentioned"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "6d71a30b-392e-456e-b7c2-430695b46385",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JUAuhj4U6cPrsWU1Xz3Ydq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1874,
      "cache_creation_input_tokens": 5180,
      "cache_read_input_tokens": 20362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5180,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
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

_source line 200_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Searching for SpatialVLA LIBERO fine-tune 2025 results",
  "usage": {
    "total_tokens": 27671,
    "tool_uses": 18,
    "duration_ms": 37571
  },
  "last_tool_name": "WebSearch",
  "uuid": "902893f7-2a21-41b2-b18d-e5b25b86f369",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 201_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018eRfZTdnpqZ91rr4nHcxiR`</summary>

```json
{
  "query": "SpatialVLA LIBERO fine-tune 2025 results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "73340b2a-40d7-4a78-b27c-974e33e2f0ed",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JUAuhj4U6cPrsWU1Xz3Ydq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1874,
      "cache_creation_input_tokens": 5180,
      "cache_read_input_tokens": 20362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5180,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
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
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Fetching https://github.com/huggingface/lerobot/issues/2259",
  "usage": {
    "total_tokens": 29334,
    "tool_uses": 17,
    "duration_ms": 43181
  },
  "last_tool_name": "WebFetch",
  "uuid": "bcd2f284-e911-4d8e-b3c1-ae07230c3a0e",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 203_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015Wz5Tu8N4gKfZixvQRFboD`</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/issues/2259",
  "prompt": "Get the full content of this GitHub issue about fine-tuning SmolVLA on different environments and embodiments. Extract all technical discussion about action dimensions, action_dim parameter, 6D vs 7D, and any official HuggingFace responses about configuration."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "e8c66913-9479-4b3a-940a-3f7911cc67f1",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EorqTiBoGoLYtkeD5McLkD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5172,
      "cache_read_input_tokens": 23867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5172,
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

_source line 204 · 2026-05-13T09:46:42.751Z_

<details><summary>↩ Tool result · `toolu_01CZfmoeiHa9o3jEPSNtE7SG`</summary>

````text
# SmolVLA Fine-tuning: Key Parameters and Commands

## Training Commands

**Smoke Test (1,000 steps):**
```bash
docker run --rm --gpus all --shm-size 16g \
  -v /path/to/lerobot_dataset:/data/input \
  -v /path/to/output:/outputs \
  ioaitech/lerobot-gpu:v0.5.0 \
  bash -lc 'lerobot-train \
    --policy.path=lerobot/smolvla_base \
    --dataset.repo_id=local/my_dataset \
    --dataset.root=/data/input \
    --batch_size=8 \
    --steps=1000 \
    --output_dir=/outputs/smolvla_smoke \
    --job_name=smolvla_smoke \
    --policy.device=cuda \
    --wandb.enable=false'
```

**Full Fine-tuning (20,000 steps):**
The base command uses `batch_size=64`, `steps=20000`, and requires approximately 4 hours on a single A100 GPU.

## Critical Configuration Parameters

| Parameter | Recommended Value | Notes |
|-----------|-------------------|-------|
| `--policy.path` | `lerobot/smolvla_base` | Official pretrained checkpoint |
| `--batch_size` | 64 | Start smaller for VRAM constraints |
| `--steps` | 20,000 | Baseline; begin with 1k smoke test |
| `--policy.device` | `cuda` | Use NVIDIA GPU; CPU for testing only |
| `--wandb.enable` | false | Disable for local quick tests |

## Data Format Requirements

- **Format Version:** v3.0 (use `ioaitech/lerobot-gpu:v0.5.0`)
- **Minimum Episodes:** "~50 high-quality episodes with repeated coverage per variation"
- **Fixed Shapes:** `observation.state` and `action` dimensions must remain consistent
- **Inputs:** Multi-view images, robot state, optional language, continuous actions

## Action Dimensions

The documentation does not explicitly specify `action_dim`; this parameter derives from your dataset's action space structure and remains task-dependent.

## Pre-training Requirements

"At minimum verify: Image keys are consistent across episodes" and validate task text alignment with physical objectives.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "28f84277-e003-4585-bba9-85c91d7a8402"
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-13T09:46:43.295Z_

<details><summary>↩ Tool result · `toolu_01BCqeC5ShbagNnBqNqEsbsv`</summary>

````text
# SmolVLA: Architecture, Fine-tuning, and Configuration

## Architecture Overview

SmolVLA is Hugging Face's lightweight robotics foundation model. The system accepts "(i) multiple cameras views, (ii) the robot's current sensorimotor state, and (iii) a natural language instruction" to generate action sequences. It processes these inputs into contextual features that condition an action expert module.

## Model Specifications

- **Base Model**: `smolvla_base` (450M parameters)
- **Training Time**: Approximately 4 hours on single A100 GPU for 20k steps
- **Fine-tuning Framework**: LeRobot with HuggingFace Hub integration

## Data Requirements

The documentation emphasizes that "data quality and quantity is definitely a key":

- **Minimum dataset**: ~50 episodes recommended as a starting point
- **Structure**: Multiple demonstrations per task variation (e.g., 10 episodes across 5 distinct cube positions = 50 total)
- **Caution**: Testing with only 25 episodes "was not enough leading to a bad performance"

## Fine-tuning Command Example

```bash
lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=${HF_USER}/mydataset \
  --batch_size=64 \
  --steps=20000 \
  --output_dir=outputs/train/my_smolvla \
  --policy.device=cuda \
  --wandb.enable=true
```

## Configuration Parameters

- **Batch Size**: Recommended starting small and increasing incrementally
- **Training Steps**: 20,000 steps as default (tunable based on performance)
- **Device**: CUDA GPU support; Colab notebook available for CPU-limited users
- **Output Directory**: Customizable model save location

## Inference Command Structure

Evaluation uses `lerobot-record` with robot type, camera configuration, task descriptions, and fine-tuned model paths specified via command-line arguments.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "d7289f5c-47d6-4339-8dbe-9e1b84e56575"
}
```

</details>

---

### Tool result

_source line 206 · 2026-05-13T09:46:46.001Z_

<details><summary>↩ Tool result · `toolu_01Qg85CyGW2ZbEQWR4UUfv52`</summary>

```text
# LightVLA: Extracted Information

Based on the provided content, here's what is available:

## Available Information

**Core Innovation:**
"Adaptive, performance-driven pruning of visual tokens" using "dynamic queries to evaluate visual token importance, and adopts Gumbel softmax to enable differentiable token selection."

**Performance Metrics:**
- 59.1% FLOPs reduction
- 38.2% latency reduction
- 2.6% task success rate improvement on LIBERO benchmark

## Information Not Provided

The webpage does not contain detailed specifications for:

- **Model Architecture Details**: Specific layer configurations, attention mechanisms, or network diagrams beyond the framework overview image
- **LIBERO Per-Suite Success Rates**: Only aggregate results mentioned; individual suite breakdowns unavailable
- **Training Details**: Hyperparameters, epochs, batch sizes, or optimization settings not specified
- **Fine-tuning Method**: Only that the model "learns to preserve the most informative visual tokens" through fine-tuning; specific procedures absent
- **Action Space**: Dimension or structure of robot actions not described
- **Baseline Comparisons**: The page mentions "superior efficiency and accuracy compared to existing VLA models" but provides no detailed comparative tables or results

**Note:** For complete technical specifications, the authors direct readers to the arXiv paper (2509.12594), GitHub repository, and Hugging Face model cards, which likely contain these omitted details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "a975eef7-0271-4b21-acf1-14387057e73a"
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
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Fetching https://raw.githubusercontent.com/huggingface/not…",
  "usage": {
    "total_tokens": 29937,
    "tool_uses": 17,
    "duration_ms": 55395
  },
  "last_tool_name": "WebFetch",
  "uuid": "43c13a04-794c-452a-90f9-a5fa4888a47a",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 208_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0173iPRm2iSeF4iK22Pys8MF`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/huggingface/notebooks/main/lerobot/training-smolvla.ipynb",
  "prompt": "Extract all training commands, configuration parameters, code cells, data format, action_dim details from this SmolVLA training notebook"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "c16ec1a0-9b63-4383-8797-acafd861cdff",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LtVXQW9cdETr6wbUXAVMz9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2209,
      "cache_read_input_tokens": 27643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2209,
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

_source line 209_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Fetching https://learnopencv.com/smolvla-lerobot-vision-la…",
  "usage": {
    "total_tokens": 29938,
    "tool_uses": 18,
    "duration_ms": 56712
  },
  "last_tool_name": "WebFetch",
  "uuid": "477aece9-91da-44ee-9bfe-7c5f57e907d9",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 210_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014o6XqbuRyxeJYoyxBwekWy`</summary>

```json
{
  "url": "https://learnopencv.com/smolvla-lerobot-vision-language-action-model/",
  "prompt": "Extract: architecture details, action_dim, observation space, training commands, config parameters, data format, fine-tuning steps for SmolVLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "67f239db-bbc8-4040-8711-a88e0be0fe74",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LtVXQW9cdETr6wbUXAVMz9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2209,
      "cache_read_input_tokens": 27643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2209,
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

_source line 211 · 2026-05-13T09:46:47.732Z_

<details><summary>↩ Tool result · `toolu_015Wz5Tu8N4gKfZixvQRFboD`</summary>

```text
# GitHub Issue Summary: SmolVLA Fine-tuning Configuration Questions

## Key Technical Questions Raised

The issue author (@RonPlusSign) is attempting to fine-tune SmolVLA and π₀ models on RLBench using a Franka Emika Panda (7DoF + gripper) but encounters 0% evaluation success despite successful training loss convergence.

## Primary Technical Concerns

**Action/State Space Specifications:**
The author requests clarification on exact representations used during pretraining, asking whether SmolVLA uses "ΔEEF pose, absolute EEF pose, joint positions, joint velocities" and angle formats (quaternion vs. Euler).

**Camera Input Handling:**
Questions whether camera naming conventions matter and if using different camera configurations from the pretrained model would waste the pretraining effort.

**Model Selection Uncertainty:**
The author notes that `HuggingFaceVLA/smolvla_libero` appears to use 6DoF+gripper, which doesn't match their 7DoF setup, creating ambiguity about embodiment compatibility.

**Action Dimension Mystery:**
In the `HuggingFaceVLA/smol-libero` dataset, actions have dimension 7, but the mapping is unclear: "doesn't clearly map to 7 joint angles + gripper."

## Status

The issue remains open and assigned to @fracapuano. No official responses appear in the provided content, meaning the technical specifications for these models lack public documentation at this point.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "506a8e06-eb3c-4258-9ab2-625f42111b54"
}
```

</details>

---

### System

_source line 212_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "description": "Fetching https://huggingface.co/docs/lerobot/lerobot-datas…",
  "usage": {
    "total_tokens": 29939,
    "tool_uses": 19,
    "duration_ms": 57579
  },
  "last_tool_name": "WebFetch",
  "uuid": "4d491fe0-8332-44ec-8838-a3087da74613",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 213_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GmreX4JevhMpqZNHMtrppo`</summary>

```json
{
  "url": "https://huggingface.co/docs/lerobot/lerobot-dataset-v3",
  "prompt": "Extract: data format spec, action/observation field names, required JSON structure, how to create a custom LeRobotDataset for fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "95876679-e2b7-45ab-868e-8a0c955d801f",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LtVXQW9cdETr6wbUXAVMz9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2209,
      "cache_read_input_tokens": 27643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2209,
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

_source line 214 · 2026-05-13T09:46:48.803Z_

<details><summary>↩ Tool result · `toolu_01GmreX4JevhMpqZNHMtrppo`</summary>

````text
# LeRobotDataset v3.0

`LeRobotDataset v3.0` is a standardized format for robot learning data. It provides unified access to multi-modal time-series data, sensorimotor signals and multi‑camera video, as well as rich metadata for indexing, search, and visualization on the Hugging Face Hub.

This docs will guide you to:

- Understand the v3.0 design and directory layout
- Record a dataset and push it to the Hub
- Load datasets for training with `LeRobotDataset`
- Stream datasets without downloading using `StreamingLeRobotDataset`
- Apply image transforms for data augmentation during training
- Migrate existing `v2.1` datasets to `v3.0`

## What’s new in `v3`

- **File-based storage**: Many episodes per Parquet/MP4 file (v2 used one file per episode).
- **Relational metadata**: Episode boundaries and lookups are resolved through metadata, not filenames.
- **Hub-native streaming**: Consume datasets directly from the Hub with `StreamingLeRobotDataset`.
- **Lower file-system pressure**: Fewer, larger files ⇒ faster initialization and fewer issues at scale.
- **Unified organization**: Clean directory layout with consistent path templates across data and videos.

## Installation

`LeRobotDataset v3.0` will be included in `lerobot >= 0.4.0`.

Until that stable release, you can use the main branch by following the [build from source instructions](./installation#from-source).

## Record a dataset

Run the command below to record a dataset with the SO-101 and push to the Hub:

```bash
lerobot-record \
  --robot.type=so101_follower \
  --robot.port=/dev/tty.usbmodem585A0076841 \
  --robot.id=my_awesome_follower_arm \
  --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 1920, height: 1080, fps: 30}}" \
  --teleop.type=so101_leader \
  --teleop.port=/dev/tty.usbmodem58760431551 \
  --teleop.id=my_awesome_leader_arm \
  --display_data=true \
  --dataset.repo_id=${HF_USER}/record-test \
  --dataset.num_episodes=5 \
  --dataset.single_task="Grab the black cube" \
  --dataset.streaming_encoding=true \
  # --dataset.vcodec=auto \
  --dataset.encoder_threads=2
```

See the [recording guide](./il_robots#record-a-dataset) for more details.

## Format design

A core v3 principle is **decoupling storage from the user API**: data is stored efficiently (few large files), while the public API exposes intuitive episode-level access.

`v3` has three pillars:

1. **Tabular data**: Low‑dimensional, high‑frequency signals (states, actions, timestamps) stored in **Apache Parquet**. Access is memory‑mapped or streamed via the `datasets` stack.
2. **Visual data**: Camera frames concatenated and encoded into **MP4**. Frames from the same episode are grouped; videos are sharded per camera for practical sizes.
3. **Metadata**: JSON/Parquet records describing schema (feature names, dtypes, shapes), frame rates, normalization stats, and **episode segmentation** (start/end offsets into shared Parquet/MP4 files).

> To scale to millions of episodes, tabular rows and video frames from multiple episodes are **concatenated** into larger files. Episode‑specific views are reconstructed **via metadata**, not file boundaries.

  
    
    
      From episode‑based to file‑based datasets
    
  

### Directory layout (simplified)

- **`meta/info.json`**: canonical schema (features, shapes/dtypes), FPS, codebase version, and **path templates** to locate data/video shards.
- **`meta/stats.json`**: global feature statistics (mean/std/min/max) used for normalization; exposed as `dataset.meta.stats`.
- **`meta/tasks.jsonl`**: natural‑language task descriptions mapped to integer IDs for task‑conditioned policies.
- **`meta/episodes/`**: per‑episode records (lengths, tasks, offsets) stored as **chunked Parquet** for scalability.
- **`data/`**: frame‑by‑frame **Parquet** shards; each file typically contains **many episodes**.
- **`videos/`**: **MP4** shards per camera; each file typically contains **many episodes**.

## Load a dataset for training

`LeRobotDataset` returns Python dictionaries of PyTorch tensors and integrates with `torch.utils.data.DataLoader`. Here is a code example showing its use:

```python
import torch
from lerobot.datasets.lerobot_dataset import LeRobotDataset

repo_id = "yaak-ai/L2D-v3"

# 1) Load from the Hub (cached locally)
dataset = LeRobotDataset(repo_id)

# 2) Random access by index
sample = dataset[100]
print(sample)
# {
#   'observation.state': tensor([...]),
#   'action': tensor([...]),
#   'observation.images.front_left': tensor([C, H, W]),
#   'timestamp': tensor(1.234),
#   ...
# }

# 3) Temporal windows via delta_timestamps (seconds relative to t)
delta_timestamps = {
    "observation.images.front_left": [-0.2, -0.1, 0.0]  # 0.2s and 0.1s before current frame
}

dataset = LeRobotDataset(repo_id, delta_timestamps=delta_timestamps)

# Accessing an index now returns a stack for the specified key(s)
sample = dataset[100]
print(sample["observation.images.front_left"].shape)  # [T, C, H, W], where T=3

# 4) Wrap with a DataLoader for training
batch_size = 16
data_loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size)

device = "cuda" if torch.cuda.is_available() else "cpu"
for batch in data_loader:
    observations = batch["observation.state"].to(device)
    actions = batch["action"].to(device)
    images = batch["observation.images.front_left"].to(device)
    # model.forward(batch)
```

## Stream a dataset (no downloads)

Use `StreamingLeRobotDataset` to iterate directly from the Hub without local copies. This allows to stream large datasets without the need to downloading them onto disk or loading them onto memory, and is a key feature of the new dataset format.

```python
from lerobot.datasets.streaming_dataset import StreamingLeRobotDataset

repo_id = "yaak-ai/L2D-v3"
dataset = StreamingLeRobotDataset(repo_id)  # streams directly from the Hub
```

  
    
    
      Stream directly from the Hub for on‑the‑fly training.
    
  

## Image transforms

Image transforms are data augmentations applied to camera frames during training to improve model robustness and generalization. LeRobot supports various transforms including brightness, contrast, saturation, hue, and sharpness adjustments.

### Using transforms during dataset creation/recording

Currently, transforms are applied during **training time only**, not during recording. When you create or record a dataset, the raw images are stored without transforms. This allows you to experiment with different augmentations later without re-recording data.

### Adding transforms to existing datasets (API)

Use the `image_transforms` parameter when loading a dataset for training:

```python
from lerobot.datasets.lerobot_dataset import LeRobotDataset
from lerobot.datasets.transforms import ImageTransforms, ImageTransformsConfig, ImageTransformConfig

# Option 1: Use default transform configuration (disabled by default)
transforms_config = ImageTransformsConfig(
    enable=True,  # Enable transforms
    max_num_transforms=3,  # Apply up to 3 transforms per frame
    random_order=False,  # Apply in standard order
)
transforms = ImageTransforms(transforms_config)

dataset = LeRobotDataset(
    repo_id="your-username/your-dataset",
    image_transforms=transforms
)

# Option 2: Create custom transform configuration
custom_transforms_config = ImageTransformsConfig(
    enable=True,
    max_num_transforms=2,
    random_order=True,
    tfs={
        "brightness": ImageTransformConfig(
            weight=1.0,
            type="ColorJitter",
            kwargs={"brightness": (0.7, 1.3)}  # Adjust brightness range
        ),
        "contrast": ImageTransformConfig(
            weight=2.0,  # Higher weight = more likely to be selected
            type="ColorJitter",
            kwargs={"contrast": (0.8, 1.2)}
        ),
        "sharpness": ImageTransformConfig(
            weight=0.5,  # Lower weight = less likely to be selected
            type="SharpnessJitter",
            kwargs={"sharpness": (0.3, 2.0)}
        ),
    }
)

dataset = LeRobotDataset(
    repo_id="your-username/your-dataset",
    image_transforms=ImageTransforms(custom_transforms_config)
)

# Option 3: Use pure torchvision transforms
from torchvision.transforms import v2

torchvision_transforms = v2.Compose([
    v2.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
    v2.GaussianBlur(kernel_size=3, sigma=(0.1, 2.0)),
])

dataset = LeRobotDataset(
    repo_id="your-username/your-dataset",
    image_transforms=torchvision_transforms
)
```

### Available transform types

LeRobot provides several transform types:

- **`ColorJitter`**: Adjusts brightness, contrast, saturation, and hue
- **`SharpnessJitter`**: Randomly adjusts image sharpness
- **`Identity`**: No transformation (useful for testing)

You can also use any `torchvision.transforms.v2` transform by passing it directly to the `image_transforms` parameter.

### Configuration options

- **`enable`**: Enable/disable transforms (default: `False`)
- **`max_num_transforms`**: Maximum number of transforms applied per frame (default: `3`)
- **`random_order`**: Apply transforms in random order vs. standard order (default: `False`)
- **`weight`**: Sampling probability for each transform (higher = more likely, if sum of weights is not 1, they will be normalized)
- **`kwargs`**: Transform-specific parameters (e.g., brightness range)

### Visualizing transforms

Use the visualization script to preview how transforms affect your data:

```bash
lerobot-imgtransform-viz \
  --repo-id=your-username/your-dataset \
  --output-dir=./transform_examples \
  --n-examples=5
```

This saves example images showing the effect of each transform, helping you tune parameters.

### Best practices

- **Start conservative**: Begin with small ranges (e.g., brightness 0.9-1.1) and increase gradually
- **Test first**: Use the visualization script to ensure transforms look reasonable
- **Monitor training**: Strong augmentations can hurt performance if too aggressive
- **Match your domain**: If your robot operates in varying lighting, use brightness/contrast transforms
- **Combine wisely**: Using too many transforms simultaneously can make training unstable

## Migrate `v2.1` → `v3.0`

A converter aggregates per‑episode files into larger shards and writes episode offsets/metadata. Convert your dataset using the instructions below.

```bash
# Pre-release build with v3 support:
pip install "https://github.com/huggingface/lerobot/archive/33cad37054c2b594ceba57463e8f11ee374fa93c.zip"

# Convert an existing v2.1 dataset hosted on the Hub:
python -m lerobot.datasets.v30.convert_dataset_v21_to_v30 --repo-id=
```

**What it does**

- Aggregates parquet files: `episode-0000.parquet`, `episode-0001.parquet`, … → **`file-0000.parquet`**, …
- Aggregates mp4 files: `episode-0000.mp4`, `episode-0001.mp4`, … → **`file-0000.mp4`**, …
- Updates `meta/episodes/*` (chunked Parquet) with per‑episode lengths, tasks, and byte/frame offsets.

## Common Issues

### Always call `finalize()` before pushing

When creating or recording datasets, you **must** call `dataset.finalize()` to properly close parquet writers. See the [PR #1903](https://github.com/huggingface/lerobot/pull/1903) for more details.

```python
from lerobot.datasets.lerobot_dataset import LeRobotDataset

# Create dataset and record episodes
dataset = LeRobotDataset.create(...)

for episode in range(num_episodes):
    # Record frames
    for frame in episode_data:
        dataset.add_frame(frame)
    dataset.save_episode()

# Call finalize() when done recording and before push_to_hub()
dataset.finalize()  # Closes parquet writers, writes metadata footers
dataset.push_to_hub()
```

**Why is this necessary?**

Dataset v3.0 uses incremental parquet writing with buffered metadata for efficiency. The `finalize()` method:

- Flushes any buffered episode metadata to disk
- Closes parquet writers to write footer metadata, otherwise the parquet files will be corrupt
- Ensures the dataset is valid for loading

Without calling `finalize()`, your parquet files will be incomplete and the dataset won't load properly.


````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "b3dd1b15-07dd-4d09-adc5-aebce7d6e990"
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-13T09:46:48.827Z_

<details><summary>↩ Tool result · `toolu_018eRfZTdnpqZ91rr4nHcxiR`</summary>

```text
Web search results for query: "SpatialVLA LIBERO fine-tune 2025 results"

Links: [{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"openvla/openvla-7b-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/openvla/openvla-7b-finetuned-libero-spatial"},{"title":"IPEC-COMMUNITY/spatialvla-4b-224-pt · Hugging Face","url":"https://huggingface.co/IPEC-COMMUNITY/spatialvla-4b-224-pt"},{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models","url":"https://arxiv.org/html/2501.15830v2"},{"title":"VOTE: Vision-Language-Action Optimization with Trajectory Ensemble Voting","url":"https://arxiv.org/html/2507.05116v3"},{"title":"moojink/openvla-7b-oft-finetuned-libero-spatial · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial"},{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"}]

Based on the search results, here are the key findings about SpatialVLA's LIBERO fine-tuning results from 2025:

## SpatialVLA LIBERO Fine-Tuning Results

Fine-tuned SpatialVLA models achieve the highest average success rate and ranking, followed by fine-tuned OpenVLA and Octo across LIBERO benchmarks.

### Specific Performance Improvements

When fine-tuning on LIBERO small dataset tasks, initializing the feature grid with the new distribution boosts model performance by +4.6%, +5.1%, +2.2%, and +5.4% on LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long, respectively.

### Fine-Tuning Methods

In LIBERO tasks, both full-tuning and LoRA-tuning are applied, and LoRA fine-tuning outperforms full-parameter fine-tuning on small dataset tasks, making LoRA the preferred method for small datasets.

### Real-World Performance

In multi-tasks, SpatialVLA leverages its pre-training on OXE and 3D perception capabilities to achieve a 57% accuracy rate, surpassing other generalist policies.

The research paper on SpatialVLA was published in January 2025 and demonstrates that the model's spatial representation enhancements, particularly with feature grid adaptation from new dataset distributions, provide meaningful improvements in LIBERO benchmark performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "fa8ced58-525b-4b5f-add1-58aa7b604518"
}
```

</details>

---

### Tool result

_source line 216 · 2026-05-13T09:46:49.658Z_

<details><summary>↩ Tool result · `toolu_01W33xCxCkY8atzBzXsBBUZQ`</summary>

```text
# VLA Models Performance on LIBERO Benchmark

The paper presents extensive evaluation of 10 VLA models, but **does not include a single comprehensive table showing per-suite success rates** (Spatial, Object, Goal, Long) for all models on the standard LIBERO benchmark.

Instead, the main results appear in **Table 1**, which focuses on robustness across perturbation dimensions rather than standard benchmark performance. This table shows:

## Models Evaluated
- OpenVLA and variants (OpenVLA-OFT, OpenVLA-OFT_w, OpenVLA-OFT_m)
- π0, π0-fast
- Nora, WorldVLA, UniVLA
- RIPT-VLA

## Key Finding from Table 1
The "Original" column shows baseline performance on unperturbed tasks, ranging from 76.5% (OpenVLA) to 97.6% (OpenVLA-OFT_m). However, these represent overall success rates, not disaggregated by suite.

## Training Details Mentioned
- Models were "pre-trained on the Open X-Embodiment dataset" with 970k+ trajectories
- Fine-tuning used "150K steps using 8×A100 GPUs"
- The paper emphasizes that "high benchmark scores often conceal critical deficiencies" rather than providing detailed per-suite breakdowns

**Note:** The research prioritizes robustness analysis over standard benchmark reporting, reflecting the paper's core message about evaluating "reliability under realistic variation."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "e41e7540-2e63-44e8-a511-0781ce023932"
}
```

</details>

---

### Tool result

_source line 217 · 2026-05-13T09:46:49.983Z_

<details><summary>↩ Tool result · `toolu_01Vvs7RmotmaE18tj7PuhuAy`</summary>

````text
# LIBERO Dataset Card Summary

## Overview
The **LIBERO** dataset is a robotics dataset from Hugging Face Vision Language Action Models research, designed for training vision-language-action (VLA) models for robotic manipulation tasks.

## Dataset Specifications

### Size & Structure
- **Total rows**: 273,000 (in default split)
- **Size category**: 100K - 1M
- **Format**: Parquet (auto-converted)
- **Split**: Single `train` split with 273k rows
- **Episodes**: 148 total episodes
- **Task suites**: 10 different task types

### Task Categories
The dataset includes **10 task indices** (0-9), representing different manipulation tasks within the LIBERO benchmark suite.

### Modalities
- **Image**: Dual RGB observations (256×256 px each)
  - `observation.images.image` 
  - `observation.images.image2`
- **Time-series**: State vectors and action sequences

## Data Schema

### Observation Keys
```
- observation.images.image (256×256 image)
- observation.images.image2 (256×256 image)
- observation.state (list of 8 floats - proprioceptive state)
```

### Action Format
```
- action (list of 7 floats - 6D pose + gripper command)
  Format: [x, y, z, rx, ry, rz, gripper]
```

### Metadata Fields
```
- timestamp (float32): Elapsed time in episode
- frame_index (int64): Frame number within episode (0-454 max)
- episode_index (int64): Episode identifier (0-147)
- task_index (int64): Task suite (0-9)
- index (int64): Global row index
```

## Key Features

### Dual Camera Setup
The dataset provides two synchronized camera views per timestep, enabling multi-view learning:
```python
# Access both camera perspectives
observation = {
    'images': {
        'image': camera1_view,      # 256×256 RGB
        'image2': camera2_view      # 256×256 RGB
    },
    'state': proprioceptive_data    # 8D state vector
}
```

### Sequential Episode Structure
- Episodes range from ~45-454 frames
- Each frame includes timestamped observations and corresponding actions
- Enables learning temporal dynamics and long-horizon reasoning

### Action Space
7-dimensional continuous actions:
- **6 DOF**: Position (xyz) + Rotation (rxryrz) for end-effector control
- **1 DOF**: Gripper open/close (-1 to 1 range)

## Differences from LeRobot/LIBERO
This dataset (`HuggingFaceVLA/libero`) is specifically curated for VLA model training, with potential differences in:
- Task distribution or filtering
- Preprocessing or normalization
- Episode selection criteria
- Integration with LeRobot framework compatibility

## Usage Example

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("HuggingFaceVLA/libero")
train_split = dataset['train']

# Access a sample
sample = train_split[0]

# Structure
{
    'observation': {
        'images': {
            'image': &lt;PIL.Image>,           # Camera 1
            'image2': &lt;PIL.Image>           # Camera 2
        },
        'state': [float] * 8                # Robot state
    },
    'action': [float] * 7,                  # 6D pose + gripper
    'timestamp': 0.0,
    'frame_index': 0,
    'episode_index': 0,
    'task_index': 0
}
```

## Libraries
- **Datasets**: HuggingFace Datasets
- **Dask**: For distributed processing
- **Croissant**: For dataset schema documentation

## License
Apache 2.0

## Tags
- **LeRobot**: Integration with LeRobot framework
- **Robotics**: Manipulation tasks
- **Vision-Language-Action**: VLA model training

This dataset enables training of VLA models that can understand language instructions, process multi-view visual observations, and generate appropriate robotic actions.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "53d5991c-1c86-4957-88b4-d70cfa50c027"
}
```

</details>

---

### Tool result

_source line 218 · 2026-05-13T09:46:50.620Z_

<details><summary>↩ Tool result · `toolu_015HS2ZDAYT3YxgyLzCDNq4i`</summary>

````text
# LIBERO Dataset Card

## Overview
The **LIBERO** dataset is a robotics manipulation dataset hosted on Hugging Face that contains demonstrations of robotic tasks performed with a Panda robot arm. It's designed for imitation learning and robot learning research.

## Dataset Specifications

### Suites Included
The dataset contains tasks from the LIBERO benchmark, which includes manipulation tasks for robot learning evaluation.

### Data Format
- **Format**: Parquet (auto-converted from original format)
- **Size**: 100K - 1M range
- **Total Rows**: 273,000 (in default subset)
- **Modalities**: Image and Time-series data

### Structure

#### Splits
- **train**: 273,000 rows

#### Features/Columns
The dataset includes the following fields per frame:

| Column | Type | Description |
|--------|------|-------------|
| `image` | Image (256×256px) | Primary camera view |
| `wrist_image` | Image (256×256px) | Wrist-mounted camera view |
| `state` | List | Robot state vector (8 values) |
| `actions` | List | Action vector (7 values) |
| `timestamp` | float32 | Frame timestamp |
| `frame_index` | int64 | Frame number within episode |
| `episode_index` | int64 | Episode identifier |
| `task_index` | int64 | Task identifier (0-9) |
| `index` | int64 | Global sample index |

### Episodes & Tasks
- **Total Episodes**: 147
- **Tasks**: 10 different manipulation tasks
- **Frames per Episode**: Up to 454 frames

### Loading the Dataset

```python
from datasets import load_dataset

# Load the default subset
dataset = load_dataset("physical-intelligence/libero")

# Access training data
train_data = dataset['train']

# Access a single sample
sample = train_data[0]
print(sample.keys())
# Output: dict_keys(['image', 'wrist_image', 'state', 'actions', 'timestamp', 
#                     'frame_index', 'episode_index', 'task_index', 'index'])
```

### State and Action Specifications

**State Vector** (8 values): Robot joint positions and gripper state
```
[-0.053, 0.007, 0.678, 3.141, 0.002, -0.090, 0.039, -0.039]
```

**Action Vector** (7 values): Joint velocities and gripper command
```
[0.016, 0, 0, 0, 0, 0, -1]
```

## Conversion to LeRobot Format
The dataset has been converted to the **LeRobot** format, which is a standardized robotics dataset format. The conversion is indicated by:
- Tags: `LeRobot`, `libero`, `panda`, `rlds`
- Libraries: Datasets, Dask, Croissant support

## License
**CC-BY-4.0** - Creative Commons Attribution 4.0 International

## Related Resources
- **ArXiv Reference**: arxiv:2306.03310
- **Robot Used**: Franka Panda
- **Task Categories**: Robotics

## Usage Example

```python
from datasets import load_dataset

# Load dataset
libero = load_dataset("physical-intelligence/libero", split="train")

# Iterate through episodes
for i in range(len(libero)):
    sample = libero[i]
    # Access visual observations
    main_view = sample['image']
    wrist_view = sample['wrist_image']
    # Access state and action
    state = sample['state']
    action = sample['actions']
    task_id = sample['task_index']
```

This dataset is ideal for training imitation learning models, behavior cloning networks, and evaluating robot learning algorithms on manipulation tasks.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "ab5d370b-63cd-45c9-b785-ba83d7d409cc"
}
```

</details>

---

### Tool result

_source line 219 · 2026-05-13T09:46:50.836Z_

<details><summary>↩ Tool result · `toolu_0173iPRm2iSeF4iK22Pys8MF`</summary>

````text
# SmolVLA Training Notebook Extraction

## Main Training Command

```bash
python lerobot/scripts/train.py \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=${HF_USER}/mydataset \
  --batch_size=64 \
  --steps=20000 \
  --output_dir=outputs/train/my_smolvla \
  --job_name=my_smolvla_training \
  --policy.device=cuda \
  --wandb.enable=true
```

## Key Configuration Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| `--policy.path` | `lerobot/smolvla_base` | Model architecture selection |
| `--batch_size` | 64 | Samples processed per gradient update |
| `--steps` | 20000 | Total training iterations |
| `--policy.device` | cuda/mps/cpu | Hardware target (GPU/Apple Silicon/CPU) |
| `--wandb.enable` | true | Experiment tracking toggle |

## Installation Code Cells

1. **Conda bootstrap**: `pip install -q condacolab` + `condacolab.install()`
2. **LeRobot setup**: Clone repository, install FFmpeg 7.1.1, editable pip install
3. **SmolVLA dependencies**: `pip install -e ".[smolvla]"`

## Key Details

- **Expected training duration**: "about 5 hours on an NVIDIA A100" GPU
- **Dataset location**: Hugging Face Hub repository (format: `USERNAME/DATASET`)
- **Output artifacts**: Model checkpoints, logs, training plots saved to `--output_dir`
- **Action_dim**: Not explicitly specified in notebook
- **Data format**: Unspecified; requires dataset repo containing training data

## Post-Training Steps

Model checkpoint upload to Hugging Face Hub via `huggingface-cli upload` command after authentication.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "0c7c1c5b-f7e5-47dd-b315-a378356164b9"
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
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Fetching https://huggingface.co/HuggingFaceVLA/smolvla_lib…",
  "usage": {
    "total_tokens": 32187,
    "tool_uses": 18,
    "duration_ms": 52245
  },
  "last_tool_name": "WebFetch",
  "uuid": "a30cdfda-9013-4c42-a4b5-9c44ac7fc225",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 221_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WKWFJ1sFWzcPS6TQtgy5iK`</summary>

```json
{
  "url": "https://huggingface.co/HuggingFaceVLA/smolvla_libero",
  "prompt": "Extract the model card details, including action space, action dimensions, what each action dimension represents, training configuration, and any notes about LIBERO action space compatibility."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "6ea9f734-f968-4160-9b36-6d81aea1805c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FJ4LxHwESZG6cx4wJe9nAU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2793,
      "cache_read_input_tokens": 29039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2793,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 222_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Fetching https://huggingface.co/datasets/HuggingFaceVLA/li…",
  "usage": {
    "total_tokens": 32247,
    "tool_uses": 19,
    "duration_ms": 53180
  },
  "last_tool_name": "WebFetch",
  "uuid": "1bb78c20-8541-49c3-adaf-0a33af3aea56",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 223_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01S2qe6xK8iefVUdpqZc9C5z`</summary>

```json
{
  "url": "https://huggingface.co/datasets/HuggingFaceVLA/libero",
  "prompt": "Extract all feature/schema details about the dataset, especially action dimensions, what each action dimension is named, state dimensions, and any notes about the action representation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "e2a1c7e1-c016-4f78-9da3-5b138046d981",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FJ4LxHwESZG6cx4wJe9nAU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2793,
      "cache_read_input_tokens": 29039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2793,
        "ephemeral_1h_input_tokens": 0
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

_source line 224 · 2026-05-13T09:46:53.676Z_

<details><summary>↩ Tool result · `toolu_01TiYQfRynb5XGyALqW4LRVb`</summary>

````text
# LIBERO to LeRobot Conversion Guide

## Overview
This conversion process transforms LIBERO HDF5 datasets into LeRobot format, incorporating improvements like enhanced resolution, action filtration, and robust error recovery.

## Key Dependencies
- LeRobot (official installation required)
- h5py
- datatrove with ray support for parallel processing
- LIBERO libraries (for trajectory regeneration)

## Conversion Workflow

### Step 1: Regenerate LIBERO Trajectories
Before conversion, preprocess the source data:
```bash
python libero_utils/regenerate_libero_dataset.py \
    --resolution 256 \
    --libero_task_suite libero_90 \
    --libero_raw_data_dir /path/to/libero/datasets/libero_90 \
    --libero_target_dir /path/to/libero/datasets/libero_90_no_noops
```

This step implements "resolution enhancement, No-op action filtration, 180° RGB frame rotation, Failed trajectory filtering."

### Step 2: Main Conversion Script
```bash
python libero_h5.py \
    --src-paths /path/to/libero/ \
    --output-path /path/to/local \
    --executor local \
    --tasks-per-job 3 \
    --workers 10
```

**Key Parameters:**
- `--src-paths`: Supports multiple dataset paths for merging
- `--executor`: Use "local" or "ray" (ray recommended for speed)
- `--tasks-per-job` and `--workers`: Adjust based on available resources
- `--resume-from-save` and `--resume-from-aggregate`: Resume interrupted conversions

## Observation Keys in Output

The converted dataset includes:
- **Image data**: `observation.images.image` (256×256×3 RGB, AV1 codec)
- **State data**: `observation.state` (8-dimensional float32)
- **Action data**: Shape [7] float32 for motor control

Native LIBERO state information is preserved via `states.ee_state` and `states.joint_state`.

## Multi-Node Processing Options

For distributed conversion:
- **Direct ray cluster**: Start head node, connect workers, execute script
- **SLURM integration**: Use provided batch script template for cluster management
- **Community managers**: Ray supports additional cluster systems

## Configuration Notes

For different image resolutions, regenerate trajectories and update the configuration file—"DO NOT use resize" during conversion.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "7db009ee-a036-4102-85d9-8ce9f7665587"
}
```

</details>

---

### Tool result

_source line 225 · 2026-05-13T09:46:54.651Z_

<details><summary>↩ Tool result · `toolu_018HtNq3mDFEJAYgNSh5Mtva`</summary>

```text
# OpenVLA-OFT: Detailed Results and Training Parameters

## LIBERO Success Rates by Task Suite

### Table I - Task Performance Comparisons

**Single Input Configuration** (third-person image + language):
| Method | Spatial | Object | Goal | Long | Average |
|--------|---------|--------|------|------|---------|
| OpenVLA (baseline) | 84.7% | 88.4% | 79.2% | 53.7% | 76.5% |
| OpenVLA + PD&AC | 91.3% | 92.7% | 90.5% | 86.5% | 90.2% |
| OpenVLA + PD&AC, Cont-L1 | 96.2% | 98.3% | 96.2% | 90.7% | 95.3% |
| OpenVLA + PD&AC, Cont-Diffusion | 96.9% | 98.1% | 95.5% | 91.1% | 95.4% |

**Multi-Input Configuration** (third-person + wrist camera + proprioceptive state):
| Method | Spatial | Object | Goal | Long | Average |
|--------|---------|--------|------|------|---------|
| π0 (fine-tuned) | 96.8% | 98.8% | 95.8% | 85.2% | 94.2% |
| **OpenVLA-OFT** | 97.6% | 98.4% | 97.9% | 94.5% | **97.1%** |

The paper states that OpenVLA-OFT achieves "state-of-the-art 97.1% average success rate" across the four LIBERO task suites, representing a substantial improvement from the baseline 76.5%.

## Training Hyperparameters for LIBERO

### Core Training Configuration

**Hardware & Compute:**
- GPU infrastructure: 8 A100/H100 GPUs
- Total batch size: 64-128 across distributed setup
- Training framework: PyTorch

**Optimization Details:**
- Learning rate: 5e-4 (initial), decayed to 5e-5 after 100K steps
- Gradient steps: 50-150K for non-diffusion methods; 100-250K for diffusion variants
- Convergence criterion: Training until mean L1 loss < 0.01 between predicted and normalized actions
- Evaluation cadence: Checkpoints evaluated every 50K steps; best performance reported

**Parameter-Efficient Fine-Tuning:**
- Technique: LoRA (Low-Rank Adaptation) employed due to smaller fine-tuning datasets (approximately 500 demonstrations versus 1M pretraining examples)

### Action Space Specifications

**Action Dimensions & Representation:**
- Original OpenVLA: 7 discrete action tokens per timestep (3 position, 3 orientation, 1 gripper)
- OpenVLA-OFT: Continuous action representation with normalized values in [-1, +1] range
- Action chunking: K=8 timesteps for LIBERO experiments

**Continuous Action Details:**
- MLP action head: 4 layers with ReLU activation
- Output space: Directly mapped continuous actions (no discretization/tokenization)

## ALOHA Robot Task Performance

### Real-World Evaluation Results

The paper demonstrates significant improvements on bimanual dexterous manipulation:

| Task | ACT | Diffusion Policy | RDT-1B | π0 | OpenVLA-OFT+ |
|------|-----|-----------------|--------|-----|--------------|
| fold shorts | Lower | Competitive | Good | Strong | **Best** |
| fold shirt | Lower | Competitive | Good | Strong | **Best** |
| scoop X into bowl | Lower | Good | Good | Good | **Best** |
| put X into pot | Lower | Lower | Good | Good | **Best** |

The paper notes that OpenVLA-OFT+ "outperform[s] both fine-tuned VLAs (π0 and RDT-1B) and prominent imitation learning policies trained from scratch (Diffusion Policy and ACT) by up to 15% (absolute) in average success rate."

### ALOHA Training Configuration

**Hardware & Parameters:**
- GPU setup: 8 A100/H100-80GB GPUs
- Total batch size: 32
- Gradient steps: 50-150K per task
- Action chunk size: K=25 timesteps
- Learning rate decay: 10× reduction after 50K steps

**Task-Specific Datasets:**
- fold shorts: 20 demonstrations
- fold shirt: 30 demonstrations
- scoop X into bowl: 45 demonstrations (15 per ingredient)
- put X into pot: 300 demonstrations (100 per object)

## Inference Efficiency Metrics

### LIBERO Efficiency (Table II)

| Configuration | Throughput | Latency |
|--------------|-----------|---------|
| Base OpenVLA | 4.2 Hz | 0.240 sec |
| + Parallel Decoding | 15.9 Hz | 0.063 sec |
| + PD & Action Chunking (K=8) | 108.8 Hz | 0.074 sec |
| + PD, AC, Cont-L1 + extra inputs | 71.4 Hz | 0.112 sec |

The paper emphasizes that parallel decoding plus action chunking achieves a "26× speedup" compared to baseline.

### ALOHA Efficiency (Table III)

| Method | Throughput | Latency |
|--------|-----------|---------|
| Base OpenVLA | 1.8 Hz | 0.543 sec |
| OpenVLA-OFT+ | 77.9 Hz | 0.321 sec |
| RDT-1B | 84.1 Hz | 0.297 sec |
| π0 | 291.6 Hz | 0.086 sec |

OpenVLA-OFT+ achieves "43× faster throughput than base OpenVLA" with action chunk size K=25, demonstrating practical viability for "25 Hz" robot control frequency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "59831294-effb-4bea-ab03-2255777fdb14"
}
```

</details>

---

### Tool result

_source line 226 · 2026-05-13T09:46:55.539Z_

<details><summary>↩ Tool result · `toolu_01WKWFJ1sFWzcPS6TQtgy5iK`</summary>

````text
# SmolVLA LIBERO Model Card Details

Based on the provided web page content, here's what I can extract:

## Available Information

**Model Name:** smolvla_libero
- **License:** apache-2.0
- **Base Model:** lerobot/smolvla_base
- **Framework:** LeRobot
- **Paper:** arxiv: 2506.01844 (SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics)

## Model Overview

SmolVLA is described as:
- A compact, efficient vision-language-action model
- Achieves competitive performance at reduced computational costs
- Deployable on consumer-grade hardware
- Trained and pushed to the Hub using LeRobot

## Usage Examples

**Training:**
```bash
lerobot-train \
  --dataset.repo_id=${HF_USER}/&lt;dataset> \
  --policy.type=act \
  --output_dir=outputs/train/&lt;desired_policy_repo_id> \
  --job_name=lerobot_training \
  --policy.device=cuda \
  --policy.repo_id=${HF_USER}/&lt;desired_policy_repo_id> \
  --wandb.enable=true
```

**Inference/Evaluation:**
```bash
lerobot-record \
  --robot.type=so100_follower \
  --dataset.repo_id=&lt;hf_user>/eval_&lt;dataset> \
  --policy.path=&lt;hf_user>/&lt;desired_policy_repo_id> \
  --episodes=10
```

## Missing Details

The provided web page content **does not include**:
- Specific action space definition
- Action dimensions
- Individual action dimension descriptions
- Detailed LIBERO action space compatibility notes
- Training configuration specifics

For complete technical details, refer to the [full model card](https://huggingface.co/HuggingFaceVLA/smolvla_libero) or the [SmolVLA paper](https://huggingface.co/papers/2506.01844).
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "485c634d-de8a-474e-b62e-52e81ee5deb2"
}
```

</details>

---

### Tool result

_source line 227 · 2026-05-13T09:46:56.725Z_

<details><summary>↩ Tool result · `toolu_014o6XqbuRyxeJYoyxBwekWy`</summary>

````text
# SmolVLA Architecture and Configuration Details

## Architecture Overview

SmolVLA is a "~450M parameter" Vision-Language-Action model combining three key components:

1. **Vision-Language Backbone**: Uses SmolVLM-2 with SigLIP for visual encoding and SmolLM2 for language processing
2. **Visual Processing**: Employs global image processing (512×512 pixels) with PixelShuffle to reduce visual tokens to approximately 64 per frame
3. **Action Expert**: Flow-matching module that converts processed perceptions into robot actions

## Key Architectural Innovations

- **Layer Skipping**: Features extracted from intermediate VLM layers (around N=L/2) rather than the final layer, reducing computational overhead during inference
- **Linear Projectors**: Serve as dimensional adapters between different modules
- **Asynchronous Inference**: Enables parallel prediction of next actions before current ones complete, reducing latency

## Configuration Parameters

Core training settings from the codebase:

```
batch_size: 64
steps: 200,000
chunk_size: 50
num_vlm_layers: 16
optimizer: adamw (lr: 0.0001)
scheduler: cosine decay with warmup
num_learnable_params: ~100M (of 450M total)
```

## Observation and Action Space

**Input Features**:
- observation.image: [3, 256, 256]
- observation.image2: [3, 256, 256]
- observation.image3: [3, 256, 256]
- observation.state: [6] (robot joint positions)

**Output**:
- action: [6] dimensions (normalized)

## Training Configuration

The model uses "MEAN_STD normalization" for actions and state, with identity normalization for visual inputs. Gradient clipping is set to 10.0, and the training employs mixed precision disabled initially.

## Fine-Tuning Command

```bash
python lerobot/scripts/train.py \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=lerobot/svla_so100_stacking \
  --batch_size=64 \
  --steps=200000
```

## Dataset Format

Training uses the `lerobot/svla_so100_stacking` repository containing 174 filtered episodes from SO-100/SO-101 robot arms. The framework standardizes camera naming conventions (e.g., "OBS_IMAGE_1 for top-down, OBS_IMAGE_2 for wrist-mounted") and auto-generates task descriptions using supplementary VLMs for consistency across heterogeneous community datasets.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "57b95be1-e0c3-4d6e-8ad5-d05a75617ff9"
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
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Fetching https://arxiv.org/html/2501.15830v2",
  "usage": {
    "total_tokens": 31346,
    "tool_uses": 19,
    "duration_ms": 53872
  },
  "last_tool_name": "WebFetch",
  "uuid": "dbc7966a-81d6-4a5a-a8cc-ee09b0eda48c",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 229_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VuTWCN2Vpk1QgJzosHiXzt`</summary>

```json
{
  "url": "https://arxiv.org/html/2501.15830v2",
  "prompt": "Extract: per-suite LIBERO success rates table (Spatial, Object, Goal, Long) for SpatialVLA and all baselines, fine-tuning method (full vs LoRA), training hyperparameters, action space configuration, model architecture details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "cd799525-b321-450b-897e-bfc017503f6f",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Q7zMdsPpRKFji5UpaiiNmd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1657,
      "cache_creation_input_tokens": 3830,
      "cache_read_input_tokens": 25542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3830,
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

_source line 230_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Searching for UniVLA LIBERO benchmark 2025 success rate",
  "usage": {
    "total_tokens": 31408,
    "tool_uses": 20,
    "duration_ms": 54359
  },
  "last_tool_name": "WebSearch",
  "uuid": "212c2991-7b32-4c53-abca-d29c265d3f75",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 231_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KHvawrSYSrKRv8azhqT6ns`</summary>

```json
{
  "query": "UniVLA LIBERO benchmark 2025 success rate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "ff003b66-0475-4e91-8a51-b3664fcc3068",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Q7zMdsPpRKFji5UpaiiNmd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1657,
      "cache_creation_input_tokens": 3830,
      "cache_read_input_tokens": 25542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3830,
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

_source line 232_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Searching for \"Cosmos-Policy\" LIBERO NVIDIA VLA 2025 fine-tune",
  "usage": {
    "total_tokens": 31470,
    "tool_uses": 21,
    "duration_ms": 54706
  },
  "last_tool_name": "WebSearch",
  "uuid": "f3976b85-5b9a-4e75-a7dd-29aaaac0a2ee",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 233_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SSWMQqLvG1EYWv9XbakanS`</summary>

```json
{
  "query": "\"Cosmos-Policy\" LIBERO NVIDIA VLA 2025 fine-tune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "9008b084-ee5d-4615-9c88-5f8ef5e60090",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Q7zMdsPpRKFji5UpaiiNmd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1657,
      "cache_creation_input_tokens": 3830,
      "cache_read_input_tokens": 25542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3830,
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

_source line 234_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "description": "Fetching https://huggingface.co/collections/IPEC-COMMUNITY…",
  "usage": {
    "total_tokens": 29138,
    "tool_uses": 14,
    "duration_ms": 66711
  },
  "last_tool_name": "WebFetch",
  "uuid": "dae8c8cc-6b2a-4e45-bca2-0fe0a937bd36",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 235_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UR6kFeP9MSj1nuT5Nq3Zdf`</summary>

```json
{
  "url": "https://huggingface.co/collections/IPEC-COMMUNITY/libero-benchmark-dataset",
  "prompt": "Extract all datasets in this collection, their names, task suites covered (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-90, LIBERO-Long), format details, and how to use them."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "1dd00251-4f0f-4e10-8354-513f3b0a6776",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014hLcjrrSeYXYAWL9g17uKN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 969,
      "cache_creation_input_tokens": 2026,
      "cache_read_input_tokens": 25685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2026,
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

_source line 236_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "description": "Fetching https://huggingface.co/blog/lerobot-release-v040",
  "usage": {
    "total_tokens": 29185,
    "tool_uses": 15,
    "duration_ms": 67337
  },
  "last_tool_name": "WebFetch",
  "uuid": "5c6db30c-fb70-4c8a-9254-44194d80e60b",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 237_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01C6XEFZXadqF1viaLE9HezQ`</summary>

```json
{
  "url": "https://huggingface.co/blog/lerobot-release-v040",
  "prompt": "Extract all details about LIBERO integration in LeRobot v0.4.0: what was added, dataset details, conversion process, training configs, and any new features related to LIBERO."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "d27e117e-ff9f-48c9-ba0d-0c9698c4cd08",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014hLcjrrSeYXYAWL9g17uKN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 969,
      "cache_creation_input_tokens": 2026,
      "cache_read_input_tokens": 25685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2026,
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

_source line 238 · 2026-05-13T09:47:02.030Z_

<details><summary>↩ Tool result · `toolu_01S2qe6xK8iefVUdpqZc9C5z`</summary>

````text
# LIBERO Dataset - Feature/Schema Details

## Overview
The LIBERO dataset is a robotics dataset containing 273k rows of demonstration data with observations, states, and actions from robotic manipulation tasks.

## Key Schema Details

### Observation Structure
- **observation.images.image**: RGB image (256x256 pixels)
- **observation.images.image2**: Second RGB image view (256x256 pixels)
- **observation.state**: List of 8 floating-point values representing robot state

### State Dimensions
The `observation.state` contains **8 values** (float32), which typically represent:
- Joint positions or end-effector pose components (6-7 DoF for a robotic arm)
- Gripper state

Example state vector:
```
[-0.053, 0.007, 0.678, 3.140, 0.001, -0.089, 0.038, -0.038]
```

### Action Dimensions
The `action` field contains **7 values** (list of floats), structured as:

```
[dx, dy, dz, droll, dpitch, dyaw, gripper]
```

**Action Components:**
1. **dx**: X-axis delta movement (translation)
2. **dy**: Y-axis delta movement (translation)
3. **dz**: Z-axis delta movement (translation)
4. **droll**: Rotation around X-axis (delta)
5. **dpitch**: Rotation around Y-axis (delta)
6. **dyaw**: Rotation around Z-axis (delta)
7. **gripper**: Gripper command (-1 for close/open, or continuous values)

### Example Action Sequences
```
[0.016, 0, 0, 0, 0, 0, -1]           # Gripper close
[-0.053, -0.085, 0.489, 0, 0, 0, 1]  # Gripper open with motion
[0.238, -0.326, 0.618, 0, 0, 0, 1]   # Motion with gripper open
```

## Additional Metadata

### Per-Sample Fields
- **timestamp**: float32 (0-45.4 range) - timing information
- **frame_index**: int64 (0-454) - frame number within episode
- **episode_index**: int64 (0-147) - episode identifier
- **task_index**: int64 (0-9) - task/subtask identifier
- **index**: int64 - global sample index

### Dataset Statistics
- **Size**: 100K - 1M range (273k rows in train split)
- **Format**: Parquet
- **Tasks**: 10 different tasks (task_index: 0-9)
- **Episodes**: 148 total episodes
- **Modalities**: Image + Time-series (proprioceptive state and actions)

## Notes on Action Representation

1. **Continuous Control**: Actions are continuous floating-point values rather than discrete
2. **Relative/Delta Actions**: Motion commands appear to be relative deltas rather than absolute positions
3. **Gripper Binary/Continuous**: Gripper value of -1 appears to indicate close state; positive values indicate open state
4. **Vision-Language Action**: Part of the HuggingFaceVLA (Vision Language Action) project, suggesting these actions can be grounded in language descriptions of tasks

This structure supports imitation learning and behavior cloning for robotic manipulation tasks.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "0eb0abaf-6592-481c-ba6d-69cb64030e00"
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-13T09:47:02.735Z_

<details><summary>↩ Tool result · `toolu_01KHvawrSYSrKRv8azhqT6ns`</summary>

```text
Web search results for query: "UniVLA LIBERO benchmark 2025 success rate"

Links: [{"title":"[2506.19850] Unified Vision-Language-Action Model","url":"https://arxiv.org/abs/2506.19850"},{"title":"Unified Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=PklMD8PwUy"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"GitHub - OpenDriveLab/UniVLA: [RSS 2025] Learning to Act Anywhere with Task-centric Latent Actions · GitHub","url":"https://github.com/OpenDriveLab/UniVLA"},{"title":"Learning to Act Anywhere with Task-centric Latent Actions","url":"https://arxiv.org/pdf/2505.06111"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"Success rates of OpenVLA, pi0, pi0.5, and univla under object position... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Success-rates-of-OpenVLA-pi0-pi05-and-univla-under-object-position-perturbations_fig1_396249917"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"Robotics Advances With Unified Vision, Language And Action Learning.","url":"https://quantumzeitgeist.com/robotics-advances-with-unified-vision-language-and-action-learning/"}]

Based on the search results, UniVLA achieves 95.5% average success rate on LIBERO benchmark, surpassing pi0-FAST's 85.5%. This represents state-of-the-art performance on the LIBERO benchmark as of 2025.

However, it's worth noting that despite achieving success rates above 90% on the standard LIBERO benchmark, models nearly collapse under changes to object positions or minor task modifications, suggesting that these headline numbers should be interpreted with caution regarding real-world robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "ea3bda45-ea24-4749-8639-2a3fd1ba1735"
}
```

</details>

---

### Tool result

_source line 240 · 2026-05-13T09:47:04.467Z_

<details><summary>↩ Tool result · `toolu_01UR6kFeP9MSj1nuT5Nq3Zdf`</summary>

````text
# Libero Benchmark Dataset Collection

## Datasets in Collection

The **IPEC-COMMUNITY/Libero Benchmark Dataset** collection contains 5 datasets:

| Dataset Name | Task Suite | Size | Downloads | Updated |
|---|---|---|---|---|
| `libero_spatial_no_noops_1.0.0_lerobot` | LIBERO-Spatial | 53k | 9.44k | Nov 3, 2025 |
| `libero_goal_no_noops_1.0.0_lerobot` | LIBERO-Goal | 52k | 7.76k | Nov 3, 2025 |
| `libero_object_no_noops_1.0.0_lerobot` | LIBERO-Object | 67k | 7.74k | Nov 3, 2025 |
| `libero_10_no_noops_1.0.0_lerobot` | LIBERO-10 | 101k | 8.65k | Nov 3, 2025 |
| `libero_90_no_noops_lerobot` | LIBERO-90 | 569k | 2.39k | Jul 1, 2025 |

## Task Suites Covered

- **LIBERO-Spatial**: Spatial reasoning tasks (52k samples)
- **LIBERO-Goal**: Goal-conditioned tasks (52k samples)
- **LIBERO-Object**: Object manipulation tasks (67k samples)
- **LIBERO-10**: 10-task benchmark (101k samples)
- **LIBERO-90**: 90-task benchmark (569k samples)

## Format Details

All datasets are in **LeRobot format** (denoted by `_lerobot` suffix) and have **no-ops removed** (`_no_noops`), optimized for efficient training.

## How to Use

Access datasets via Hugging Face Datasets library:

```python
from datasets import load_dataset

# Example: Load LIBERO-Spatial dataset
dataset = load_dataset("IPEC-COMMUNITY/libero_spatial_no_noops_1.0.0_lerobot")

# Example: Load LIBERO-90 (largest benchmark)
dataset = load_dataset("IPEC-COMMUNITY/libero_90_no_noops_lerobot")
```

**View & Explore**: Use the Viewer option on each dataset's Hugging Face page for interactive exploration.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "f7a3167d-ae02-4460-9286-a93403e589f5"
}
```

</details>

---

### Tool result

_source line 241 · 2026-05-13T09:47:05.956Z_

<details><summary>↩ Tool result · `toolu_01C6XEFZXadqF1viaLE9HezQ`</summary>

```text
# LIBERO Integration in LeRobot v0.4.0

## What Was Added

LeRobot v0.4.0 officially integrated support for **LIBERO**, one of the largest open benchmarks for Vision-Language-Action (VLA) policies. This is positioned as a major step toward building an evaluation hub for VLAs with unified setup for evaluating any VLA policy.

## LIBERO Overview

- **Scale**: Over 130 tasks available
- **Purpose**: Large open benchmark for Vision-Language-Action (VLA) policies
- **Focus**: Enables easy integration and standardized evaluation across different VLA models

## Dataset Details

The LIBERO dataset is available on the Hugging Face Hub:
- **Dataset**: [HuggingFaceVLA/libero](https://huggingface.co/datasets/HuggingFaceVLA/libero)
- **Stats**: 273k entries, 23.8k downloads, 54 likes (as of the article date)

## Documentation and Getting Started

The article references comprehensive documentation for implementation:
- **Documentation Link**: https://huggingface.co/docs/lerobot/en/libero
- The docs provide detailed setup instructions for using LIBERO with LeRobot

## Demo

The article includes a demonstration GIF showing GR00T performing tasks in LIBERO simulation environments, indicating successful integration of LIBERO simulation support alongside the VLA models.

## Context

LIBERO integration is part of a broader expansion of simulation environments in v0.4.0, alongside Meta-World support, enabling researchers to evaluate policies across diverse robotic manipulation benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "4af72ba3-69ce-4019-9b6a-9254b5afeb37"
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
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Fetching https://arxiv.org/html/2506.01844v1",
  "usage": {
    "total_tokens": 33851,
    "tool_uses": 20,
    "duration_ms": 67090
  },
  "last_tool_name": "WebFetch",
  "uuid": "d82b3c21-1e45-46cf-b9c0-6f6d9a5a76d5",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 243_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01R3s4oUeYUFeSGAc1WeV7FZ`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.01844v1",
  "prompt": "Find all mentions of: max_action_dim, action_dim, padding, 32D, action dimension, action space, SO-100, SO-101, LIBERO action, joint control vs end-effector control. Also look for Table 12 about chunk size ablation and any appendix about training configuration."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "29ae2a56-82b8-4a69-a481-824ee4c9068c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MpbFR6PTEcc7y6Yd4f1H2x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1602,
      "cache_read_input_tokens": 31832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1602,
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

_source line 244 · 2026-05-13T09:47:08.322Z_

<details><summary>↩ Tool result · `toolu_01VuTWCN2Vpk1QgJzosHiXzt`</summary>

```text
# SpatialVLA: Key Technical Details

## LIBERO Success Rates (Table III)

| Model | Spatial | Object | Goal | Long | Average |
|-------|---------|--------|------|------|---------|
| SpatialVLA (fine-tuned) | 88.2% | 89.9% | 78.6% | 55.5% | **78.1%** |
| OpenVLA (fine-tuned) | 84.7% | 88.4% | 79.2% | 53.7% | 76.5% |
| TraceVLA (fine-tuned) | 84.6% | 85.2% | 75.1% | 54.1% | 74.8% |
| Octo (fine-tuned) | 78.9% | 85.7% | 84.6% | 51.1% | 75.1% |

SpatialVLA achieved the highest average performance across all four task suites.

## Fine-tuning Approaches

The paper evaluates two primary strategies:

1. **Full Parameter Fine-tuning**: Direct optimization of all model weights on downstream tasks
2. **LoRA Fine-tuning** (r=32, α=32): Parameter-efficient adaptation for smaller datasets like LIBERO

**Key finding**: "LoRA tuning outperforms full-parameter fine-tuning on small dataset tasks," with spatial embedding adaptation providing additional gains of 4-5% on individual LIBERO suites.

## Training Hyperparameters

- **Pre-training**: 1.1 million robot demonstrations across 64 A100 GPUs for 10 days
- **Batch size**: 2048 (pre-training); 128 (ablation studies on 8 A100s)
- **Training steps**: 120k steps (ablation experiments)
- **Epochs**: 200 epochs for LIBERO fine-tuning

## Action Space Configuration

The model discretizes continuous 7D actions into adaptive spatial grids:

- **Total tokens**: V = 8,194
- **Per-step prediction**: 3 spatial action tokens (vs. 7 in prior work)
- **Decomposition**: Translation (M_trans=4,096) + Rotation (M_rot=4,096) + Gripper (2 tokens)
- **Grid initialization**: Gaussian distribution-based equal probability binning

## Model Architecture Details

- **Vision encoder**: SigLIP for 2D semantic feature extraction
- **VLM backbone**: PaliGemma2
- **Depth estimation**: ZoeDepth for ego3D position encoding
- **Inference**: 8.5GB GPU memory, ~20Hz on RTX 4090
- **Total parameters**: 3.5B (significantly smaller than RT-2-X at 55B)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "eb9bdfff-0a2a-4707-8631-cbb57eca01ce"
}
```

</details>

---

### System

_source line 245_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "description": "Fetching https://github.com/huggingface/lerobot/blob/main/…",
  "usage": {
    "total_tokens": 30516,
    "tool_uses": 16,
    "duration_ms": 75888
  },
  "last_tool_name": "WebFetch",
  "uuid": "f448792c-bc3b-44d0-bff1-757f001a0d34",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 246_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AgaiaefetY9pkGvzBstwtC`</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/libero.mdx",
  "prompt": "Extract the full content including any conversion scripts, dataset preparation steps, training configurations, observation/action specs, and any details about how to prepare LIBERO data from scratch."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "7ebb1622-ee87-4d36-ae2d-13e0720a40b6",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MdWN8fbmGkJeoEodcoTnxu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2253,
      "cache_read_input_tokens": 27711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2253,
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

### Tool result

_source line 247 · 2026-05-13T09:47:09.805Z_

<details><summary>↩ Tool result · `toolu_01SSWMQqLvG1EYWv9XbakanS`</summary>

```text
Web search results for query: ""Cosmos-Policy" LIBERO NVIDIA VLA 2025 fine-tune"

Links: [{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning","url":"https://research.nvidia.com/labs/dir/cosmos-policy/cosmos_policy_index.html"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning - Cosmos Cookbook","url":"https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/post_training/predict2/cosmos_policy/post_training.html"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning","url":"https://arxiv.org/html/2601.16163v1"},{"title":"Understanding How NVIDIA Cosmos Policy Works | Paper: Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning - BioErrorLog Tech Blog","url":"https://en.bioerrorlog.work/entry/nvidia-cosmos-policy-paper"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning | OpenReview","url":"https://openreview.net/forum?id=wPEIStHxYH"},{"title":"GitHub - NVlabs/cosmos-policy: Cosmos Policy · GitHub","url":"https://github.com/NVlabs/cosmos-policy"},{"title":"Cosmos Policy — Cosmos Lab","url":"https://research.nvidia.com/labs/cosmos-lab/cosmos-policy/"},{"title":"NVIDIA adds Cosmos Policy to its world foundation models - The Robot Report","url":"https://www.therobotreport.com/nvidia-adds-cosmos-policy-world-foundation-models/"},{"title":"cosmos-policy/README.md at main · NVlabs/cosmos-policy","url":"https://github.com/NVlabs/cosmos-policy/blob/main/README.md"},{"title":"Introducing NVIDIA Cosmos Policy for Advanced Robot Control","url":"https://huggingface.co/blog/nvidia/cosmos-policy-for-robot-control"}]

Based on the search results, here's information about Cosmos-Policy and its fine-tuning on LIBERO with NVIDIA's VLA:

## Overview

Cosmos Policy is a simple approach for adapting a large pretrained video model (Cosmos-Predict2) into an effective robot policy through a single stage of post-training on robot demonstration data collected on the target platform, with no architectural modifications.

## LIBERO Performance

Cosmos Policy achieves state-of-the-art performance on the LIBERO and RoboCasa simulation benchmarks (98.5% and 67.1% average success rates, respectively) and the highest average score in challenging real-world bimanual manipulation tasks, outperforming strong diffusion policies trained from scratch, video model-based policies, and state-of-the-art vision-language-action models fine-tuned on the same robot demonstrations.

More specifically, Cosmos Policy achieved a 98.5% average success rate across the four task suites, outperforming all methods — including VLA models such as π0.5 (96.9%), CogVLA (97.4%), and OpenVLA-OFT (97.1%) — to set a new SOTA.

## Technical Approach

Cosmos-Predict is fine-tuned for robotic manipulation tasks using "latent frame injection": directly encoding new modalities (actions, robot proprioceptive state, and future state value) into the video model's latent diffusion sequence. Three examples are discussed: the LIBERO simulation benchmark tasks, the RoboCasa simulation benchmark tasks, and real-world ALOHA robot tasks.

## Fine-tuning Details

For the experiments in the Cosmos Policy paper, 64 80GB GPUs (H100s) were used for 48 hours for LIBERO training (2000 demos).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "e270ea1f-6c1c-4168-a361-16dfac7837f6"
}
```

</details>

---

### System

_source line 248_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "description": "Fetching https://huggingface.co/datasets/IPEC-COMMUNITY/li…",
  "usage": {
    "total_tokens": 30562,
    "tool_uses": 17,
    "duration_ms": 77202
  },
  "last_tool_name": "WebFetch",
  "uuid": "07c493e1-7fb4-4641-aff4-14558a1f1db1",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 249_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GjjswEUopnxwJ37XQRpwYV`</summary>

```json
{
  "url": "https://huggingface.co/datasets/IPEC-COMMUNITY/libero_90_no_noops_lerobot/discussions/2",
  "prompt": "Extract conversion script details, ideas discussed, and any technical information about the dataset format or how it was created."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "624a150a-d482-4a72-8a3d-135071b1d580",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MdWN8fbmGkJeoEodcoTnxu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2253,
      "cache_read_input_tokens": 27711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2253,
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

### Tool result

_source line 250 · 2026-05-13T09:47:11.881Z_

<details><summary>↩ Tool result · `toolu_01R3s4oUeYUFeSGAc1WeV7FZ`</summary>

```text
# Search Results for Action Dimension and Configuration Details

I've thoroughly reviewed the provided document and found the following:

## Action Dimension References

**Not found**: The specific terms "max_action_dim," "action_dim," "padding," or "32D" do not appear in this paper.

## Action Space Details

The paper mentions that SmolVLA predicts "action chunks" but does not explicitly state a specific action dimensionality. The document references that the model outputs "a chunk of n low-level actions" where "n=50" during training, but the actual action vector dimensions remain unspecified in the provided text.

## Robot Platforms

**SO-100 and SO-101**: The paper describes these as "low-cost, 3D-printable robotic arms" with "six degrees of freedom" controlled via "position commands." The SO-101 represents an updated version with "better arm design" and "smoother movements."

## Table 12 - Chunk Size Ablation

This table evaluates how varying chunk sizes (n ∈ {1, 10, 30, 50, 100}) affects LIBERO benchmark performance, finding that "chunk sizes between 10 and 50 provide a good balance."

## Control Type

The paper does not explicitly distinguish between "joint control vs end-effector control" in the provided sections.

**Note**: Training configuration details and appendix information about action space specifications were not located in the supplied document excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "93849197-7211-4728-a71c-e6e0cedbef83"
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
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Fetching https://arxiv.org/abs/2506.19850",
  "usage": {
    "total_tokens": 34102,
    "tool_uses": 22,
    "duration_ms": 68776
  },
  "last_tool_name": "WebFetch",
  "uuid": "d939c4a6-063d-4918-b953-b3d703532ba5",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 252_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RSZ2NRtsAiHx3DaRe4BXQh`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.19850",
  "prompt": "Extract: model architecture, LIBERO per-suite success rates (Spatial, Object, Goal, Long), fine-tuning method, training details (steps, lr, batch size, hardware), action space configuration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "bea6a3cb-b9a3-4ec0-b717-cabb244e4db3",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EvpvSkzJMPRJ6KpDfd14Fw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4226,
      "cache_read_input_tokens": 29372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4226,
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

_source line 253_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Searching for CogVLA LIBERO 97.4 results 2025",
  "usage": {
    "total_tokens": 34164,
    "tool_uses": 23,
    "duration_ms": 69011
  },
  "last_tool_name": "WebSearch",
  "uuid": "3b5d450a-a374-4bfb-b521-1a7b251a898a",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 254_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BZDZuCEJT4MQWpHrAhz1jH`</summary>

```json
{
  "query": "CogVLA LIBERO 97.4 results 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "965b50fc-2fe9-48ff-8dc9-a5d5153c7b34",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EvpvSkzJMPRJ6KpDfd14Fw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4226,
      "cache_read_input_tokens": 29372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4226,
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

_source line 255_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Searching for pi0-FAST LIBERO success rate 2025 fine-tune",
  "usage": {
    "total_tokens": 34226,
    "tool_uses": 24,
    "duration_ms": 69191
  },
  "last_tool_name": "WebSearch",
  "uuid": "3c1319a9-2a42-4d3b-b5bd-3c8f137ef8d0",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 256_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fpf5JU8kVBuKuJorXHvTw9`</summary>

```json
{
  "query": "pi0-FAST LIBERO success rate 2025 fine-tune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "9f7c295e-f4f8-4d7a-9cde-b1d181743cca",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EvpvSkzJMPRJ6KpDfd14Fw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4226,
      "cache_read_input_tokens": 29372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4226,
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

_source line 257 · 2026-05-13T09:47:15.400Z_

<details><summary>↩ Tool result · `toolu_01GjjswEUopnxwJ37XQRpwYV`</summary>

```text
# Dataset Conversion Discussion Summary

## Key Information Extracted

### Conversion Tool
- **Tool Name**: [any4lerobot](https://github.com/Tavish9/any4lerobot)
- **Purpose**: Converts LIBERO HDF5 datasets to LeRobot format with video storage
- **Space Efficiency**: Stores observations in MP4 files rather than individual images, significantly reducing storage requirements

### Dataset Details
- **Source Format**: LIBERO HDF5 files
- **Target Format**: LeRobot format with MP4 video encoding
- **Filtering Applied**: Uses OpenVLA script-based filtering (called `libero_no_noops`)
- **Original vs. Filtered Episodes**:
  - Original LIBERO: 500 episodes per dataset (10 tasks × 50 demos)
  - Filtered versions in repo:
    - `libero_spatial_no_noops_lerobot`: 434 episodes
    - `libero_object_no_noops_lerobot`: 452 episodes

### Technical Issues & Solutions

**Video Decoding Problems**:
1. Random video corruption occurs during conversion
2. **Workaround**: Re-encode the image sequence for problematic episodes back into video
3. **Encoding Recommendation**: 
   - Current method uses `av1` encoding (occasional corruption)
   - Suggested alternative: X264 encoder (more stable)
4. **Status**: Issue primarily affects LIBERO datasets; other datasets encode without issues

### Filtering Reference
- Implementation: [regenerate_libero_dataset.py](https://github.com/Tavish9/any4lerobot/blob/main/libero2lerobot/libero_utils/regenerate_libero_dataset.py)
- Details available in OpenVLA documentation
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "4e770592-f293-4b75-8dfa-37fe1956b6bb"
}
```

</details>

---

### Tool result

_source line 258 · 2026-05-13T09:47:15.953Z_

<details><summary>↩ Tool result · `toolu_01AgaiaefetY9pkGvzBstwtC`</summary>

```text
# LIBERO Integration for LeRobot: Key Details

## Overview
LIBERO is described as "a benchmark designed to study **lifelong robot learning**" with "a set of standardized manipulation tasks that focus on **knowledge transfer**." The benchmark comprises 130 tasks across five suites.

## Task Suites Available
The documentation lists these options:
- LIBERO-Spatial (10 tasks)
- LIBERO-Object (10 tasks)
- LIBERO-Goal (10 tasks)
- LIBERO-90 (90 tasks)
- LIBERO-Long (10 tasks)

## Installation
Users must install with: `pip install -e ".[libero]"` and set the MuJoCo rendering backend via environment variable for headless systems.

## Observation & Action Specifications

**Observations include:**
- 8-dimensional proprioceptive state (end-effector position, orientation, gripper)
- Main camera view (HWC uint8 format)
- Wrist camera view (HWC uint8 format)

**Actions:**
Continuous control in a "Box(-1, 1, shape=(7,))" space—"6D end-effector delta + 1D gripper"

## Dataset & Training
The preprocessed LIBERO dataset is available at HuggingFaceVLA/libero. Documentation provides example training commands using the `lerobot-train` CLI with parameters for policy type, batch size, and training steps.

## Evaluation Protocol
The recommended approach uses "10 episodes per task across all four standard suites" for reproducible benchmarking, yielding 400 total episodes.

## Published Results Reference
The documentation reports Pi0.5 (LeRobot) achieving 97.5% average success across the four suites, with individual suite scores ranging from 96.0–99.0%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "f06a52d5-06a0-4eea-abe5-4c73a579375d"
}
```

</details>

---

### System

_source line 259_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Fetching https://github.com/huggingface/lerobot/blob/main/…",
  "usage": {
    "total_tokens": 34423,
    "tool_uses": 21,
    "duration_ms": 77680
  },
  "last_tool_name": "WebFetch",
  "uuid": "962cf452-67bc-44a6-9d4b-1406099ad399",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 260_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015e81cLypfwXCfBBmRS9ex9`</summary>

```json
{
  "url": "https://github.com/huggingface/lerobot/blob/main/lerobot/configs/policy/smolvla.yaml",
  "prompt": "Extract all configuration parameters, especially action-related ones: action_dim, max_action_dim, action_feature, chunk_size, n_action_steps, state_dim, and any other relevant parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "3b55a163-585f-43cd-a87f-f2da0d4c628d",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Kaqga8VbfWmWFkfFxcF8Jo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 516,
      "cache_read_input_tokens": 33434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 516,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
      "service_tier": "standard",
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

_source line 261_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Searching for lerobot smolvla.yaml max_action_dim action_featur…",
  "usage": {
    "total_tokens": 34479,
    "tool_uses": 22,
    "duration_ms": 77882
  },
  "last_tool_name": "WebSearch",
  "uuid": "7a7a6f64-826f-4ed9-aa6a-46e046cbfbb4",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 262_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LYFS1PheyL5ePfneNnm8c9`</summary>

```json
{
  "query": "lerobot smolvla.yaml max_action_dim action_feature config 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "e5928d8d-cc3a-42f3-be5f-7a7294c94102",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Kaqga8VbfWmWFkfFxcF8Jo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 516,
      "cache_read_input_tokens": 33434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 516,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 263 · 2026-05-13T09:47:17.650Z_

<details><summary>↩ Tool result · reported error · `toolu_015e81cLypfwXCfBBmRS9ex9`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "42c191ca-2527-4b91-8240-34b0d93223f5",
  "tool_use_result": "Error: Request failed with status code 404"
}
```

</details>

---

### Tool result

_source line 264 · 2026-05-13T09:47:17.722Z_

<details><summary>↩ Tool result · `toolu_01RSZ2NRtsAiHx3DaRe4BXQh`</summary>

```text
# UniVLA Paper Summary

Based on the arXiv page content provided, I can only extract limited information:

**Available Information:**

The abstract indicates UniVLA is "a unified and native multimodal VLA model that autoregressively models vision, language, and action signals as discrete token sequences." It incorporates world modeling during post-training to capture causal dynamics from videos.

**Performance Metrics:**
The paper reports achieving "95.5% average success rate on LIBERO benchmark, surpassing pi0-FAST's 85.5%." However, the specific per-suite breakdown (Spatial, Object, Goal, Long) is not included in this abstract.

**Not Available in Source:**
The webpage excerpt does not contain:
- Detailed model architecture specifications
- Individual LIBERO suite success rates
- Fine-tuning methodology details
- Training parameters (steps, learning rate, batch size)
- Hardware specifications
- Action space configuration

**Recommendation:**
To obtain these technical details, you would need to access the full PDF or HTML version of the paper, which are linked on this arXiv page but not fully reproduced in the content provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "7eae44c4-74c9-4ec3-a0e4-75337d070d89"
}
```

</details>

---

### Tool result

_source line 265 · 2026-05-13T09:47:19.018Z_

<details><summary>↩ Tool result · `toolu_01BZDZuCEJT4MQWpHrAhz1jH`</summary>

```text
Web search results for query: "CogVLA LIBERO 97.4 results 2025"

Links: [{"title":"GitHub - iLearn-Lab/NeurIPS25-CogVLA: [NeurIPS 2025] CogVLA: Cognition-Aligned Vision-Language-Action Models via Instruction-Driven Routing & Sparsification · GitHub","url":"https://github.com/iLearn-Lab/NeurIPS25-CogVLA"},{"title":"GitHub - JiuTian-VL/CogVLA: [NeurIPS 2025] CogVLA: Cognition-Aligned Vision-Language-Action Models via Instruction-Driven Routing & Sparsification","url":"https://github.com/JiuTian-VL/CogVLA"},{"title":"CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification","url":"https://arxiv.org/html/2508.21046v1"},{"title":"CogVLA: Cognition-Aligned Vision-Language-Action Model via","url":"https://arxiv.org/pdf/2508.21046"},{"title":"Next Generation VLA Model by CogVLA! Instruction-driven routing and efficient robot operation based on cognitive science | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media","url":"https://ai-scholar.tech/en/articles/llm-paper/cogvla"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/cce95bd4761c6e1cbc198e0ca5fe030ab6f2ff88.pdf"},{"title":"Libero® SoC Design Suite Versions 2025.2 to 12.0 | Microchip Technology","url":"https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/fpga/libero-software-later-versions"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"SwiftVLA: Unlocking Spatiotemporal Dynamics for Lightweight VLA","url":"https://arxiv.org/pdf/2512.00903"},{"title":"Targa Libero Ferrario 2025 One day race results","url":"https://www.procyclingstats.com/national-race/targa-libero-ferrario/2025/result"}]

Based on the search results, here's what I found about CogVLA's LIBERO 97.4 results:

CogVLA achieves state-of-the-art performance with success rates of 97.4% on the LIBERO benchmark. The model achieved this highest success rate of 97.4% across 500 trials for each task suite.

More specifically, CogVLA achieved 98.6% on Spatial, 98.8% on Object, 96.6% on Goal, and 95.4% on Long task suites, resulting in an overall average of 97.4%.

In addition to simulation performance, the model achieved a 70.0% success rate on real-world robotic tasks while reducing training costs by 2.5×. CogVLA also decreased inference latency by 2.8× compared to OpenVLA.

CogVLA is a NeurIPS 2025 paper titled "Cognition-Aligned Vision-Language-Action Models via Instruction-Driven Routing & Sparsification".


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "4a717441-e238-4d1f-a6c0-8c2513641c11"
}
```

</details>

---

### Tool result

_source line 266 · 2026-05-13T09:47:20.072Z_

<details><summary>↩ Tool result · `toolu_01Fpf5JU8kVBuKuJorXHvTw9`</summary>

```text
Web search results for query: "pi0-FAST LIBERO success rate 2025 fine-tune"

Links: [{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"PI05 lora fine-tune on libero dataset & differences about the norm_stats · Issue #711 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/711"},{"title":"Pi0 and Pi0.5 model fine-tuning guide | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/Pi0/"},{"title":"Evaluating \\( \\pi_0 \\) in the Wild: Strengths, Problems, and the Future of Generalist Robot Policies","url":"https://penn-pal-lab.github.io/Pi0-Experiment-in-the-Wild/"},{"title":"Is PI0.5 finetuned by all LIBERO datasets? Success rate of LIBERO-90 is only 18%? · Issue #734 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/734"},{"title":"PI0 Evaluation results on LIBERO is very low · Issue #952 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/952"},{"title":"[Quick Review] π_RL: Online RL Fine-tuning for Flow-based\\n Vision-Language-Action Models","url":"https://liner.com/review/%CF%80_rl-online-rl-finetuning-for-flowbased-visionlanguageaction-models"},{"title":"doremifasolatido/pi0-fast-libero-lora · Hugging Face","url":"https://huggingface.co/doremifasolatido/pi0-fast-libero-lora"},{"title":"Open Sourcing π0","url":"https://www.pi.website/blog/openpi"}]

Based on the search results, here's what I found about π0-FAST LIBERO success rates with fine-tuning:

## Key Findings:

The π0.5 model fine-tuned on LIBERO datasets achieved the following success rates: LIBERO-Spatial 97.4%, LIBERO-Object 98.4%, LIBERO-Goal 97.6%, and LIBERO-10 93.0%.

For π0 models more generally with online reinforcement learning fine-tuning, Flow-Noise boosts the average success rate of the pi0 model from 57.6% to 97.6% and the pi0.5 model from 77.1% to 98.3%.

Additionally, OpenVLA-OFT achieves state-of-the-art results in LIBERO with 97.1% average success rate across 4 task suites, outperforming π0, MDT, Seer, DiT Policy, Octo, and Diffusion Policy.

There are also reports of fine-tuning challenges in the community. When fine-tuning pi0 on libero-goal, one user reported a success rate of just 41.8%, which was far from the results 98.8% from openpi, suggesting that fine-tuning success depends heavily on proper configuration and methodology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "7130a965-45c0-4149-a6b5-644c86d4b6a7"
}
```

</details>

---

### Tool result

_source line 267 · 2026-05-13T09:47:23.699Z_

<details><summary>↩ Tool result · `toolu_01LYFS1PheyL5ePfneNnm8c9`</summary>

```text
Web search results for query: "lerobot smolvla.yaml max_action_dim action_feature config 2025"

Links: [{"title":"VLA (2) SmolVLA, ACT — XLeRobot 0.3.0 documentation","url":"https://xlerobot.readthedocs.io/en/latest/software/getting_started/VLA_smol.html"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"lerobot/examples/tutorial/smolvla/using_smolvla_example.py at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/examples/tutorial/smolvla/using_smolvla_example.py"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"SmolVLA fine-tuning | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/"},{"title":"config.json · lerobot/smolvla_base at 04d96c1f9167360280aaa54de31418f824d1ef48","url":"https://huggingface.co/lerobot/smolvla_base/blob/04d96c1f9167360280aaa54de31418f824d1ef48/config.json"},{"title":"lerobot/docs/source/smolvla.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx"},{"title":"`smolvla_base training`: `Expected all tensors to be on the same device` · Issue #1377 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1377"}]

Based on the search results, I found relevant information about SmolVLA configuration, particularly regarding `max_action_dim` and `action_feature`:

## SmolVLA Configuration: max_action_dim and action_feature

SmolVLA uses dynamic padding during training where actions are padded to `max_action_dim` (32D), and during inference, actions are cropped back to the original action dimensions using `action_feature.shape[0]` which is auto-detected.

SmolVLA's dynamic padding supports any action space ≤ 32D, unlike other VLA models that may require manual action_mode configuration.

### Key Config Details:

The configuration handling involves:
- **max_action_dim**: Set to 32 dimensions for padding
- **action_feature**: An auto-detected feature that stores the original action dimension shape

SmolVLA takes as input multiple camera views, the robot's current sensorimotor state, and a natural language instruction, encoded into contextual features used to condition the action expert when generating an action chunk.

For training configurations, users can adjust batch sizes and training steps, with example training using `--batch_size=64` and `--steps=20000`.

If you need more specific details about the actual `smolvla.yaml` file configuration, the Hugging Face repository's config.json file would contain the precise parameter values.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "df51e9f9-5d77-45cd-9027-3868d02d3943"
}
```

</details>

---

### System

_source line 268_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Fetching https://arxiv.org/html/2508.21046v1",
  "usage": {
    "total_tokens": 36645,
    "tool_uses": 25,
    "duration_ms": 79214
  },
  "last_tool_name": "WebFetch",
  "uuid": "25625144-ff6b-4b01-b2c2-ed168d7876ea",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 269_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NX48ZiFiyjFcYWHZs2kwMK`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.21046v1",
  "prompt": "Extract: model architecture, LIBERO per-suite success rates table comparing CogVLA to baselines, fine-tuning method (LoRA rank, full fine-tune etc.), training details (steps, lr, batch size, hardware), action space configuration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "ea0d2d2c-ee58-46d0-a405-66408ca21c87",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TusS2rhUkGd8X1gkaYQHms",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2355,
      "cache_read_input_tokens": 33598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2355,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 270_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Searching for pi0.5 LIBERO 97.4 success rate fine-tune training…",
  "usage": {
    "total_tokens": 36709,
    "tool_uses": 26,
    "duration_ms": 79220
  },
  "last_tool_name": "WebSearch",
  "uuid": "b460f5db-098b-4c91-a0b1-7799454cc414",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 271_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UqR23Z8Am6fhyyFbXRm63U`</summary>

```json
{
  "query": "pi0.5 LIBERO 97.4 success rate fine-tune training details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "acad4a2b-6c6c-4a77-ac93-2ae66392aab2",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TusS2rhUkGd8X1gkaYQHms",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2355,
      "cache_read_input_tokens": 33598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2355,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 272_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Searching for MoDE MDT diffusion LIBERO 2025 success rate resul…",
  "usage": {
    "total_tokens": 36773,
    "tool_uses": 27,
    "duration_ms": 79648
  },
  "last_tool_name": "WebSearch",
  "uuid": "8f87520b-0f25-487e-bc2e-a21de15bc631",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 273_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LtUdsMosrScXf46haHEgVZ`</summary>

```json
{
  "query": "MoDE MDT diffusion LIBERO 2025 success rate results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "730fce43-bf69-4ba9-8cd1-5e8db44f22c7",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TusS2rhUkGd8X1gkaYQHms",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2355,
      "cache_read_input_tokens": 33598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2355,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 274_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "description": "Fetching https://huggingface.co/lerobot/smolvla_base/blob/…",
  "usage": {
    "total_tokens": 35749,
    "tool_uses": 23,
    "duration_ms": 87807
  },
  "last_tool_name": "WebFetch",
  "uuid": "daecdc18-9d58-45a3-8c48-6ed6e60b72b9",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 275_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012EnhyxzchF4P2PU6cNn67C`</summary>

```json
{
  "url": "https://huggingface.co/lerobot/smolvla_base/blob/04d96c1f9167360280aaa54de31418f824d1ef48/config.json",
  "prompt": "Extract all configuration parameters from this config.json, especially: max_action_dim, action_dim, action_feature, state_feature, chunk_size, n_action_steps, input_features, output_features, and any action-space related settings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "d00aa236-ecb6-4de3-ae83-331bfde942cd",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HTfXMZbLCFvTBWqfcRFqcQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1198,
      "cache_read_input_tokens": 33950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1198,
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

_source line 276 · 2026-05-13T09:47:31.023Z_

<details><summary>↩ Tool result · `toolu_012EnhyxzchF4P2PU6cNn67C`</summary>

````text
# Configuration Parameters for lerobot/smolvla_base

## Key Action-Space and Dimension Settings

| Parameter | Value |
|-----------|-------|
| **max_action_dim** | 32 |
| **max_state_dim** | 32 |
| **chunk_size** | 50 |
| **n_action_steps** | 50 |
| **n_obs_steps** | 1 |

## Output Features (Action)

```json
"output_features": {
  "action": {
    "type": "ACTION",
    "shape": [6]
  }
}
```

**Action Dimension**: 6 (actual action space size)

## Input Features (State & Visual Observations)

```json
"input_features": {
  "observation.state": {
    "type": "STATE",
    "shape": [6]
  },
  "observation.image": {
    "type": "VISUAL",
    "shape": [3, 256, 256]
  },
  "observation.image2": {
    "type": "VISUAL",
    "shape": [3, 256, 256]
  },
  "observation.image3": {
    "type": "VISUAL",
    "shape": [3, 256, 256]
  }
}
```

**State Feature Dimension**: 6

## Normalization Strategy

```json
"normalization_mapping": {
  "VISUAL": "IDENTITY",
  "STATE": "MEAN_STD",
  "ACTION": "MEAN_STD"
}
```

## Summary

- **Action Space**: 6-dimensional continuous actions
- **State Space**: 6-dimensional state observations
- **Vision Input**: 3 multi-view camera inputs (256×256 RGB)
- **Action Prediction**: 50-step future action chunks
- **Model Architecture**: SmolVLM2-500M vision-language-action model
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "dc3f13b6-7f7f-46b9-b322-5d85498115e3"
}
```

</details>

---

### Tool result

_source line 277 · 2026-05-13T09:47:31.259Z_

<details><summary>↩ Tool result · `toolu_01LtUdsMosrScXf46haHEgVZ`</summary>

```text
Web search results for query: "MoDE MDT diffusion LIBERO 2025 success rate results"

Links: [{"title":"Efficient Diffusion Transformer Policies with Mixture of Expert Denoisers for Multitask Learning","url":"https://mbreuss.github.io/MoDE_Diffusion_Policy/"},{"title":"GitHub - intuitive-robots/MoDE_Diffusion_Policy: [ICLR 25] Code for \"Efficient Diffusion Transformer Policies with Mixture of Expert Denoisers for Multitask Learning\" · GitHub","url":"https://github.com/intuitive-robots/MoDE_Diffusion_Policy"},{"title":"On-Device Diffusion Transformer Policy for Efficient Robot Manipulation","url":"https://arxiv.org/html/2508.00697v1"},{"title":"Multimodal Diffusion Transformer: Learning Versatile Behavior from Multimodal Goals","url":"https://intuitive-robots.github.io/mdt_policy/"},{"title":"On-Device Diffusion Transformer Policy for Efficient Robot Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf"},{"title":"Multimodal Diffusion Transformer: Learning Versatile Behavior from Multimodal Goals","url":"https://arxiv.org/html/2407.05996v1"},{"title":"Goal Conditioned Imitation Learning using Score-based Diffusion Policies","url":"https://intuitive-robots.github.io/beso-website/"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Multimodal Diffusion Transformer: Learning Versatile Behavior from","url":"https://openreview.net/pdf/7f244a9f6cc676d079f8357e0e789455c22ac7da.pdf"},{"title":"nvidia/Cosmos-Policy-LIBERO-Predict2-2B · Hugging Face","url":"https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B"}]

Based on the search results, here are the key findings for MoDE MDT diffusion LIBERO 2025 success rate results:

## MoDE Performance on LIBERO

MoDE is the first policy to achieve an over 90% success rate in the challenging LIBERO-10 experiment. MoDE surpasses prior best Diffusion baselines by an average of 16% in both settings, all while maintaining its computational advantage.

## Specific LIBERO Results

By pretraining MoDE on diverse robotics data, the model achieves 0.95 on LIBERO-90. MoDE excels at complex challenges, such as drawer manipulation (34.92% success) and precise object interactions (40% success on vertical can picking).

## Overall Performance

MoDE achieves state-of-the-art performance on 134 tasks in four established imitation learning benchmarks (CALVIN and LIBERO). It surpasses both CNN-based and Transformer Diffusion Policies by an average of 57% across 4 benchmarks, while using 90% fewer FLOPs and fewer active parameters compared to default Diffusion Transformer architectures.

The MoDE approach represents a significant advancement in efficient diffusion-based policies for robot manipulation tasks on the LIBERO benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "471c3676-8995-4246-b3f3-15397608f9a9"
}
```

</details>

---

### Tool result

_source line 278 · 2026-05-13T09:47:34.075Z_

<details><summary>↩ Tool result · `toolu_01NX48ZiFiyjFcYWHZs2kwMK`</summary>

```text
# CogVLA: Technical Architecture and Training Configuration

## Model Architecture

CogVLA employs a three-stage progressive design inspired by human multimodal coordination:

**Stage 1 - Encoder-FiLM based Aggregation Routing (EFA-Routing):** Compresses visual tokens to 25% of original scale using instruction-guided modulation. The system uses dual vision encoders (SigLIP and DINOv2) with 64 aggregation tokens each, dynamically fusing their outputs based on task instructions.

**Stage 2 - LLM-FiLM based Pruning Routing (LFP-Routing):** Applies semantic-aware token pruning within the language model, achieving approximately 50% token reduction through a shifted cosine schedule that controls retention ratios across transformer layers.

**Stage 3 - V-L-A Coupled Attention (CAtten):** Implements hierarchical attention combining causal vision-language attention with bidirectional action decoding to maintain coherence under compressed inputs.

## LIBERO Benchmark Performance

| Task Suite | CogVLA SR | Ranking |
|-----------|-----------|---------|
| Spatial   | 98.6%     | 1st     |
| Object    | 98.8%     | 1st (tied) |
| Goal      | 96.6%     | 2nd     |
| Long      | 95.4%     | 1st     |
| **Average** | **97.4%** | **1st** |

CogVLA outperformed OpenVLA-OFT (97.1%) and other state-of-the-art baselines across most task categories.

## Training Configuration

**LIBERO Fine-tuning:**
- Method: Low-Rank Adaptation (LoRA) with rank 32, α=64
- Steps: 60,000
- Batch size: 64
- Learning rate: 5e-4
- Hardware: 4×A800 GPUs (80GB)
- Evaluation: Every 10,000 steps
- Action chunk size (K): 8

**Real-world Fine-tuning (ALOHA):**
- Method: LoRA (rank 32, α=64)
- Steps: 80,000
- Batch size: 32
- Learning rate: 5e-4 (reduced to 5e-5 after 50K steps)
- Evaluation: Every 10K steps starting at step 60K
- Action chunk size (K): 25

## Action Space Configuration

The atomic action vector has dimensionality D=7, comprising:
- 3-DoF translation (ΔT)
- 3-DoF rotation (ΔR)
- Binary gripper control

The model uses parallel decoding to predict action chunks simultaneously rather than autoregressively, improving inference efficiency.

## Key Efficiency Gains

Compared to OpenVLA baseline:
- **2.79× faster inference time** (0.091s vs 0.254s)
- **3.12× reduction in FLOPs** (2.72T vs 8.48T)
- **2.49× lower training cost** (4.7h vs 11.7h per 10k steps)
- **8× visual input compression** (25% from Stage 1 + 50% from Stage 2)

Human teleoperationexperimental setup across five distinct real-world manipulation tasks validated the approach's practical applicability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "3e6cbd15-65da-413a-8b07-ea5fdb5a2ad6"
}
```

</details>

---

### Runtime record

_source line 279_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "isUsingOverage": false
  },
  "uuid": "4b9d0680-e769-4209-bc6d-6318da7136ea",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool result

_source line 280 · 2026-05-13T09:47:35.448Z_

<details><summary>↩ Tool result · `toolu_01UqR23Z8Am6fhyyFbXRm63U`</summary>

```text
Web search results for query: "pi0.5 LIBERO 97.4 success rate fine-tune training details"

Links: [{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"Pi0 and Pi0.5 model fine-tuning guide | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/Pi0/"},{"title":"PI05 lora fine-tune on libero dataset & differences about the norm_stats · Issue #711 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/711"},{"title":"[Feature Proposal] Add LoRA training support for pi0.5 (PyTorch backend) · Issue #842 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/842"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"𝜋_\"RL\": Online RL Fine-tuning for Flow-based Vision-Language-Action Models","url":"https://arxiv.org/html/2510.25889v1"},{"title":"π₀.₅ (Pi05) Policy · Hugging Face","url":"https://huggingface.co/docs/lerobot/pi05"},{"title":"question about lora fine-tuning for pi0.5 · Issue #672 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/672"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"Is PI0.5 finetuned by all LIBERO datasets? Success rate of LIBERO-90 is only 18%? · Issue #734 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/734"}]

Based on the search results, I found information about pi0.5 LIBERO fine-tuning with the 97.4% success rate you mentioned:

## Pi0.5 LIBERO Success Rates

The pi0.5 model achieved a 97.4% success rate on the LIBERO-Spatial task suite, along with strong performance on other LIBERO benchmarks.

## Fine-Tuning Training Details

Physical Intelligence provides example fine-tuning configs for π₀, π₀-FAST, and π₀.₅ on LIBERO data.

The training process involves several key steps:

1. **Data Preparation**: Before training, you need to compute the normalization statistics for the training data by running a script with your training config name.

2. **Training Execution**: Training is initiated with a command that logs progress to the console and saves checkpoints to the checkpoints directory. The XLA_PYTHON_CLIENT_MEM_FRACTION=0.9 flag enables JAX to use up to 90% of GPU memory.

3. **Configuration Options**: Training can be configured with options like model compilation, gradient checkpointing, mixed precision (bfloat16), batch sizes (e.g., 32), and flexible freezing of vision encoders.

4. **Evaluation**: After training is complete, inference is performed by spinning up a policy server and querying it from a LIBERO evaluation script.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "56e40472-42de-48f0-8022-5387e2b68599"
}
```

</details>

---

### System

_source line 281_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Fetching https://arxiv.org/html/2510.25889v1",
  "usage": {
    "total_tokens": 39710,
    "tool_uses": 28,
    "duration_ms": 95085
  },
  "last_tool_name": "WebFetch",
  "uuid": "9fbd04cb-274e-4599-a1d2-434cae50ec53",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 282_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KJcS2o6bNcG4fYGgeff49H`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.25889v1",
  "prompt": "Extract all LIBERO per-suite success rates for pi0 and pi0.5 models (baseline and fine-tuned), training details, fine-tuning method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "543f2ef9-0732-40da-85c4-2703edfb1fda",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FBaEpubtxweSW6gmhxhskp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 910,
      "cache_creation_input_tokens": 1963,
      "cache_read_input_tokens": 35953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1963,
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

_source line 283_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Searching for Octo LIBERO success rate per suite spatial object…",
  "usage": {
    "total_tokens": 39775,
    "tool_uses": 29,
    "duration_ms": 95666
  },
  "last_tool_name": "WebSearch",
  "uuid": "748324d9-28e7-4510-b2e0-ddf408b2d401",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 284_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GqHp6h9BQyTU76wbmbGEuJ`</summary>

```json
{
  "query": "Octo LIBERO success rate per suite spatial object goal long"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "f2f88d33-db02-42ce-8e1c-8e1413c67aa0",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FBaEpubtxweSW6gmhxhskp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 910,
      "cache_creation_input_tokens": 1963,
      "cache_read_input_tokens": 35953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1963,
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

### Runtime record

_source line 285_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778674800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "91a24143-1bf1-430f-843e-a072920b66d5",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool result

_source line 286 · 2026-05-13T09:47:45.473Z_

<details><summary>↩ Tool result · `toolu_01GqHp6h9BQyTU76wbmbGEuJ`</summary>

```text
Web search results for query: "Octo LIBERO success rate per suite spatial object goal long"

Links: [{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"Github","url":"https://visual-cot-vla-sub.github.io/"},{"title":"CoT-VLA","url":"https://cot-vla.github.io/"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/liu_zhu_NeurIPS2023.pdf"},{"title":"Success rate of the π 0 model on the LIBERO-Goal, Object, Spatial and... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Success-rate-of-the-p-0-model-on-the-LIBERO-Goal-Object-Spatial-and-Long-task-suits_tbl1_396330496"},{"title":"Libero-Object Benchmark","url":"https://www.emergentmind.com/topics/libero-object-benchmark"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models [Quick Review]","url":"https://liner.com/review/cotvla-visual-chainofthought-reasoning-for-visionlanguageaction-models"}]

Based on the search results, I found relevant information about success rates on LIBERO task suites. Here's what the search revealed:

CoT-VLA achieves the best or competitive success rates across all LIBERO task suites (Spatial, Object, Goal, Long), with an average success rate of 81.13% compared to OpenVLA's 76.5%.

More broadly, advanced approaches have set new performance benchmarks (up to 98.1% average success rate) on LIBERO tasks.

The LIBERO benchmark evaluates models across different task suites:
- Object: 10 tasks where object types vary with spatial/scene fixed; Goal: 10 tasks with the same scene/object but variable goal action predicates; Long: 10 tasks with compositional/long-horizon multi-step instructions

Additionally, for each task suite (Spatial, Object, Goal, Long), success rate and standard deviation are reported across 3 trials over 500 testing initial states.

If you're looking for specific Octo model results on these benchmarks, the search results don't contain that particular information. Would you like me to search more specifically for Octo model performance data?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "4f37295f-7aef-47a6-b4d9-609f2218e652"
}
```

</details>

---

### System

_source line 287_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "af6076af78ee4f8e4",
  "tool_use_id": "toolu_01MF6koX1EJpEjH7EddZx5wM",
  "status": "completed",
  "output_file": "",
  "summary": "Search 1: SmolVLA fine-tuning",
  "usage": {
    "total_tokens": 34956,
    "tool_uses": 19,
    "duration_ms": 118219
  },
  "uuid": "bfe9930e-70c6-46c3-939f-b4e754490dad",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool result

_source line 288 · 2026-05-13T09:47:49.147Z_

<details><summary>↩ Tool result · `toolu_01MF6koX1EJpEjH7EddZx5wM`</summary>

````text
I now have comprehensive information from all sources. Here is the compiled summary:

---

## SmolVLA Fine-tuning: Comprehensive Summary

### 1. Model Overview

**Model ID:** `lerobot/smolvla_base`
**Parameters:** ~450M total (~100M trainable during default fine-tuning)
**Architecture:**
- VLM backbone: SmolVLM2-500M-Video-Instruct (SigLIP vision encoder + SmolLM2-1.7B-Instruct language decoder)
- Action Expert: Flow-Matching Transformer (~100M params), hidden size = 75% of VLM hidden dim
- Visual token compression: PixelShuffle → **64 tokens/frame** (vs. 1024 standard)
- Layer skipping: features from intermediate VLM layers (~L/2) for faster inference
- During default fine-tuning, only the action expert is trained; VLM is frozen

**Action/Observation Space (SO-100/SO-101 reference embodiment):**
- `observation.state`: [6] — robot joint positions
- `observation.image`, `observation.image2`, ... : [3, H, W] — multiple camera views (typically 256×256 or 640×480)
- `action`: [6] — normalized continuous joint commands (MEAN_STD normalization)
- Language instruction: optional string input
- Action chunking: `chunk_size=50` steps predicted per forward pass

---

### 2. Installation

```bash
git clone https://github.com/huggingface/lerobot.git
cd lerobot
pip install -e ".[smolvla]"
# For PEFT/LoRA support:
pip install -e ".[smolvla,peft]"
```

---

### 3. Fine-tuning Commands

**Standard full fine-tuning (recommended entry point):**
```bash
lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=${HF_USER}/mydataset \
  --batch_size=64 \
  --steps=20000 \
  --output_dir=outputs/train/my_smolvla \
  --job_name=my_smolvla_training \
  --policy.device=cuda \
  --policy.dtype=bfloat16 \
  --wandb.enable=true
```
- ~4–5 hours on single A100 for 20k steps
- Start with batch_size=8–16 for smaller GPUs, increase as VRAM allows

**LoRA fine-tuning (PEFT — lower VRAM, ~8GB sufficient with 4-bit quantization):**
```bash
lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --policy.repo_id=your_hub_name/my_smolvla_lora \
  --dataset.repo_id=HuggingFaceVLA/libero \
  --policy.output_features=null \
  --policy.input_features=null \
  --policy.optimizer_lr=1e-3 \
  --policy.scheduler_decay_lr=1e-4 \
  --steps=100000 \
  --batch_size=32 \
  --peft.method_type=LORA \
  --peft.r=64 \
  --peft.lora_alpha=64
```

**PEFT default target modules:** `q_proj`, `v_proj` of the LM expert + `state_proj`, `action_in_proj`, `action_out_proj`, `action_time_mlp_in`, `action_time_mlp_out`

**Custom target modules (e.g., MLP layers):**
```
--peft.target_modules='(model\.vlm_with_expert\.lm_expert\..*\.(down|gate|up)_proj|.*\.(state_proj|action_in_proj|action_out_proj|action_time_mlp_in|action_time_mlp_out))'
```

**Partially full fine-tune a specific layer:**
```
--peft.full_training_modules=["state_proj"]
```

**Smoke test (1k steps, local dataset):**
```bash
lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=local/my_dataset \
  --dataset.root=/data/input \
  --batch_size=8 \
  --steps=1000 \
  --output_dir=outputs/smolvla_smoke \
  --policy.device=cuda \
  --wandb.enable=false
```

---

### 4. Key Training Hyperparameters

| Parameter | Default / Recommended | Notes |
|---|---|---|
| `steps` | 20k (real-world), 100k (sim) | Tune to task; 200k for pretraining |
| `batch_size` | 64 | Reduce for low VRAM |
| `optimizer` | AdamW | lr=1e-4 full, 1e-3 LoRA |
| `scheduler` | cosine decay + warmup | `scheduler_decay_lr=1e-4` |
| `chunk_size` | 50 | Actions predicted per forward pass |
| `gradient_checkpointing` | `--policy.gradient_checkpointing=true` | Enable for memory saving |
| `dtype` | bfloat16 | `--policy.dtype=bfloat16` |
| `peft.r` | 64 | LoRA rank |
| `peft.lora_alpha` | 64 | LoRA scaling = alpha/r |
| normalization | MEAN_STD for actions/state | Identity for images |
| gradient_clip | 10.0 | |

---

### 5. Dataset Format (LeRobotDataset v3.0)

**Directory structure:**
```
meta/
  info.json         # feature schema (names, shapes, dtypes), FPS, path templates
  stats.json        # global mean/std/min/max per feature — critical for normalization
  tasks.jsonl       # task description strings → integer IDs
  episodes/         # chunked Parquet with episode boundaries
data/
  file-0000.parquet # tabular: state, action, timestamp (many episodes per file)
videos/
  &lt;camera_key>/
    file-0000.mp4   # many episodes per file, one subdirectory per camera
```

**Sample dict keys returned by `dataset[i]`:**
```python
{
  'observation.state': tensor([...]),          # shape [state_dim]
  'action': tensor([...]),                     # shape [action_dim]
  'observation.images.front': tensor([C,H,W]), # one key per camera
  'timestamp': tensor(1.234),
  ...
}
```

**Creating a custom dataset programmatically:**
```python
from lerobot.datasets.lerobot_dataset import LeRobotDataset

dataset = LeRobotDataset.create(...)
for episode in ...:
    for frame in episode:
        dataset.add_frame(frame)
    dataset.save_episode()
dataset.finalize()   # REQUIRED — flushes parquet writers
dataset.push_to_hub()
```

**Critical:** `stats.json` must reflect your dataset's actual statistics, not a reference dataset's. Using wrong stats causes erratic denormalized actions.

---

### 6. Data Collection Recommendations

- Minimum: **~50 episodes** (25 is insufficient based on empirical testing)
- Repeat each task variation ~10 times across distinct configurations
- Reference dataset: [`lerobot/svla_so100_pickplace`](https://huggingface.co/spaces/lerobot/visualize_dataset?path=%2Flerobot%2Fsvla_so100_pickplace%2Fepisode_0) — 50 eps across 5 cube positions
- Validate data with: visualization (smooth curves), replay testing, statistical checks (verify action magnitudes match workspace, no zero-std dimensions)

---

### 7. Inference / Evaluation

```bash
lerobot-record \
  --robot.type=so101_follower \
  --robot.port=/dev/ttyACM0 \
  --robot.id=my_blue_follower_arm \
  --robot.cameras="{ front: {type: opencv, index_or_path: 8, width: 640, height: 480, fps: 30}}" \
  --dataset.single_task="Grasp a lego block and put it in the bin." \
  --dataset.repo_id=${HF_USER}/eval_test \
  --dataset.episode_time_s=50 \
  --dataset.num_episodes=10 \
  --policy.path=${HF_USER}/my_finetuned_smolvla
```

**n_action_steps config fix:** When using the phospho/non-standard training path, change `"n_action_steps": 1` → `"n_action_steps": 50` in `config.json` before inference, or inference runs one action at a time (very slow).

---

### 8. Key Source URLs

| Resource | URL | Usability |
|---|---|---|
| Official SmolVLA fine-tune docs | https://huggingface.co/docs/lerobot/smolvla | **Direct** — canonical commands |
| PEFT/LoRA training docs | https://huggingface.co/docs/lerobot/en/peft_training | **Direct** — LoRA config |
| HF model card | https://huggingface.co/lerobot/smolvla_base | **Direct** — inference + train code |
| Training notebook (Colab) | https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb | Direct |
| SmolVLA blog post | https://huggingface.co/blog/smolvla | Architecture + pretraining details |
| Dataset v3.0 docs | https://huggingface.co/docs/lerobot/lerobot-dataset-v3 | **Direct** — data format spec |
| Medium fine-tuning tutorial | https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632 | Practical, includes custom action dim |
| Phospho train guide | https://docs.phospho.ai/learn/train-smolvla | Practical, Docker workflow |
| EmbodiFlow SmolVLA guide | https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/ | Smoke-test Docker commands |
| PEFT mdx source | https://github.com/huggingface/lerobot/blob/main/docs/source/peft_training.mdx | Source of PEFT docs |
| smolvla.mdx source | https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx | Source of official docs |

---

### 9. Custom Dataset action_dim

The `action_dim` is **not fixed** — it is inferred from your dataset's `meta/info.json` feature schema. Examples:
- SO-100/SO-101: action=[6] (6-DOF joint control)
- Libero/Panda: action=[7] (dx, dy, dz, droll, dpitch, dyaw, gripper)
- General: match the robot's DOF

To adapt SmolVLA to a different action_dim, define the `action` feature shape in `info.json` and ensure `stats.json` covers it. The `--policy.output_features=null --policy.input_features=null` flags (used in PEFT examples) instruct the trainer to infer features directly from the dataset.

agentId: af6076af78ee4f8e4 (use SendMessage with to: 'af6076af78ee4f8e4' to continue this agent)
&lt;usage>total_tokens: 37803
tool_uses: 19
duration_ms: 118222&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "39af1b0a-ad47-4dc8-978a-53c42291a4d0",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search for SmolVLA fine-tuning documentation and examples. This is a VLA (Vision-Language-Action) model from HuggingFace's LeRobot framework, model ID `lerobot/smolvla_base`.\n\nDo the following searches and fetch relevant pages:\n\n1. WebSearch for \"SmolVLA fine-tuning lerobot\"\n2. WebSearch for \"SmolVLA LoRA training recipe\"\n3. WebSearch for \"lerobot smolvla finetune 2025 2026\"\n4. Fetch the HuggingFace model card: https://huggingface.co/lerobot/smolvla_base — extract: model architecture, action dimensions, supported datasets, fine-tuning instructions, training config\n5. Fetch the LeRobot GitHub README: https://github.com/huggingface/lerobot — extract: fine-tuning commands, SmolVLA references, training scripts, example configs\n6. WebSearch for \"lerobot fine-tune guide tutorial\"\n\nFor each result, record:\n- URL\n- Key information (training commands, config files, data format requirements, action_dim)\n- Whether it's directly usable for fine-tuning SmolVLA on a custom dataset\n\nCompile a comprehensive summary of all findings.",
    "agentId": "af6076af78ee4f8e4",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information from all sources. Here is the compiled summary:\n\n---\n\n## SmolVLA Fine-tuning: Comprehensive Summary\n\n### 1. Model Overview\n\n**Model ID:** `lerobot/smolvla_base`\n**Parameters:** ~450M total (~100M trainable during default fine-tuning)\n**Architecture:**\n- VLM backbone: SmolVLM2-500M-Video-Instruct (SigLIP vision encoder + SmolLM2-1.7B-Instruct language decoder)\n- Action Expert: Flow-Matching Transformer (~100M params), hidden size = 75% of VLM hidden dim\n- Visual token compression: PixelShuffle → **64 tokens/frame** (vs. 1024 standard)\n- Layer skipping: features from intermediate VLM layers (~L/2) for faster inference\n- During default fine-tuning, only the action expert is trained; VLM is frozen\n\n**Action/Observation Space (SO-100/SO-101 reference embodiment):**\n- `observation.state`: [6] — robot joint positions\n- `observation.image`, `observation.image2`, ... : [3, H, W] — multiple camera views (typically 256×256 or 640×480)\n- `action`: [6] — normalized continuous joint commands (MEAN_STD normalization)\n- Language instruction: optional string input\n- Action chunking: `chunk_size=50` steps predicted per forward pass\n\n---\n\n### 2. Installation\n\n```bash\ngit clone https://github.com/huggingface/lerobot.git\ncd lerobot\npip install -e \".[smolvla]\"\n# For PEFT/LoRA support:\npip install -e \".[smolvla,peft]\"\n```\n\n---\n\n### 3. Fine-tuning Commands\n\n**Standard full fine-tuning (recommended entry point):**\n```bash\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=${HF_USER}/mydataset \\\n  --batch_size=64 \\\n  --steps=20000 \\\n  --output_dir=outputs/train/my_smolvla \\\n  --job_name=my_smolvla_training \\\n  --policy.device=cuda \\\n  --policy.dtype=bfloat16 \\\n  --wandb.enable=true\n```\n- ~4–5 hours on single A100 for 20k steps\n- Start with batch_size=8–16 for smaller GPUs, increase as VRAM allows\n\n**LoRA fine-tuning (PEFT — lower VRAM, ~8GB sufficient with 4-bit quantization):**\n```bash\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --policy.repo_id=your_hub_name/my_smolvla_lora \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --policy.output_features=null \\\n  --policy.input_features=null \\\n  --policy.optimizer_lr=1e-3 \\\n  --policy.scheduler_decay_lr=1e-4 \\\n  --steps=100000 \\\n  --batch_size=32 \\\n  --peft.method_type=LORA \\\n  --peft.r=64 \\\n  --peft.lora_alpha=64\n```\n\n**PEFT default target modules:** `q_proj`, `v_proj` of the LM expert + `state_proj`, `action_in_proj`, `action_out_proj`, `action_time_mlp_in`, `action_time_mlp_out`\n\n**Custom target modules (e.g., MLP layers):**\n```\n--peft.target_modules='(model\\.vlm_with_expert\\.lm_expert\\..*\\.(down|gate|up)_proj|.*\\.(state_proj|action_in_proj|action_out_proj|action_time_mlp_in|action_time_mlp_out))'\n```\n\n**Partially full fine-tune a specific layer:**\n```\n--peft.full_training_modules=[\"state_proj\"]\n```\n\n**Smoke test (1k steps, local dataset):**\n```bash\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=local/my_dataset \\\n  --dataset.root=/data/input \\\n  --batch_size=8 \\\n  --steps=1000 \\\n  --output_dir=outputs/smolvla_smoke \\\n  --policy.device=cuda \\\n  --wandb.enable=false\n```\n\n---\n\n### 4. Key Training Hyperparameters\n\n| Parameter | Default / Recommended | Notes |\n|---|---|---|\n| `steps` | 20k (real-world), 100k (sim) | Tune to task; 200k for pretraining |\n| `batch_size` | 64 | Reduce for low VRAM |\n| `optimizer` | AdamW | lr=1e-4 full, 1e-3 LoRA |\n| `scheduler` | cosine decay + warmup | `scheduler_decay_lr=1e-4` |\n| `chunk_size` | 50 | Actions predicted per forward pass |\n| `gradient_checkpointing` | `--policy.gradient_checkpointing=true` | Enable for memory saving |\n| `dtype` | bfloat16 | `--policy.dtype=bfloat16` |\n| `peft.r` | 64 | LoRA rank |\n| `peft.lora_alpha` | 64 | LoRA scaling = alpha/r |\n| normalization | MEAN_STD for actions/state | Identity for images |\n| gradient_clip | 10.0 | |\n\n---\n\n### 5. Dataset Format (LeRobotDataset v3.0)\n\n**Directory structure:**\n```\nmeta/\n  info.json         # feature schema (names, shapes, dtypes), FPS, path templates\n  stats.json        # global mean/std/min/max per feature — critical for normalization\n  tasks.jsonl       # task description strings → integer IDs\n  episodes/         # chunked Parquet with episode boundaries\ndata/\n  file-0000.parquet # tabular: state, action, timestamp (many episodes per file)\nvideos/\n  &lt;camera_key>/\n    file-0000.mp4   # many episodes per file, one subdirectory per camera\n```\n\n**Sample dict keys returned by `dataset[i]`:**\n```python\n{\n  'observation.state': tensor([...]),          # shape [state_dim]\n  'action': tensor([...]),                     # shape [action_dim]\n  'observation.images.front': tensor([C,H,W]), # one key per camera\n  'timestamp': tensor(1.234),\n  ...\n}\n```\n\n**Creating a custom dataset programmatically:**\n```python\nfrom lerobot.datasets.lerobot_dataset import LeRobotDataset\n\ndataset = LeRobotDataset.create(...)\nfor episode in ...:\n    for frame in episode:\n        dataset.add_frame(frame)\n    dataset.save_episode()\ndataset.finalize()   # REQUIRED — flushes parquet writers\ndataset.push_to_hub()\n```\n\n**Critical:** `stats.json` must reflect your dataset's actual statistics, not a reference dataset's. Using wrong stats causes erratic denormalized actions.\n\n---\n\n### 6. Data Collection Recommendations\n\n- Minimum: **~50 episodes** (25 is insufficient based on empirical testing)\n- Repeat each task variation ~10 times across distinct configurations\n- Reference dataset: [`lerobot/svla_so100_pickplace`](https://huggingface.co/spaces/lerobot/visualize_dataset?path=%2Flerobot%2Fsvla_so100_pickplace%2Fepisode_0) — 50 eps across 5 cube positions\n- Validate data with: visualization (smooth curves), replay testing, statistical checks (verify action magnitudes match workspace, no zero-std dimensions)\n\n---\n\n### 7. Inference / Evaluation\n\n```bash\nlerobot-record \\\n  --robot.type=so101_follower \\\n  --robot.port=/dev/ttyACM0 \\\n  --robot.id=my_blue_follower_arm \\\n  --robot.cameras=\"{ front: {type: opencv, index_or_path: 8, width: 640, height: 480, fps: 30}}\" \\\n  --dataset.single_task=\"Grasp a lego block and put it in the bin.\" \\\n  --dataset.repo_id=${HF_USER}/eval_test \\\n  --dataset.episode_time_s=50 \\\n  --dataset.num_episodes=10 \\\n  --policy.path=${HF_USER}/my_finetuned_smolvla\n```\n\n**n_action_steps config fix:** When using the phospho/non-standard training path, change `\"n_action_steps\": 1` → `\"n_action_steps\": 50` in `config.json` before inference, or inference runs one action at a time (very slow).\n\n---\n\n### 8. Key Source URLs\n\n| Resource | URL | Usability |\n|---|---|---|\n| Official SmolVLA fine-tune docs | https://huggingface.co/docs/lerobot/smolvla | **Direct** — canonical commands |\n| PEFT/LoRA training docs | https://huggingface.co/docs/lerobot/en/peft_training | **Direct** — LoRA config |\n| HF model card | https://huggingface.co/lerobot/smolvla_base | **Direct** — inference + train code |\n| Training notebook (Colab) | https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb | Direct |\n| SmolVLA blog post | https://huggingface.co/blog/smolvla | Architecture + pretraining details |\n| Dataset v3.0 docs | https://huggingface.co/docs/lerobot/lerobot-dataset-v3 | **Direct** — data format spec |\n| Medium fine-tuning tutorial | https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632 | Practical, includes custom action dim |\n| Phospho train guide | https://docs.phospho.ai/learn/train-smolvla | Practical, Docker workflow |\n| EmbodiFlow SmolVLA guide | https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/ | Smoke-test Docker commands |\n| PEFT mdx source | https://github.com/huggingface/lerobot/blob/main/docs/source/peft_training.mdx | Source of PEFT docs |\n| smolvla.mdx source | https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx | Source of official docs |\n\n---\n\n### 9. Custom Dataset action_dim\n\nThe `action_dim` is **not fixed** — it is inferred from your dataset's `meta/info.json` feature schema. Examples:\n- SO-100/SO-101: action=[6] (6-DOF joint control)\n- Libero/Panda: action=[7] (dx, dy, dz, droll, dpitch, dyaw, gripper)\n- General: match the robot's DOF\n\nTo adapt SmolVLA to a different action_dim, define the `action` feature shape in `info.json` and ensure `stats.json` covers it. The `--policy.output_features=null --policy.input_features=null` flags (used in PEFT examples) instruct the trainer to infer features directly from the dataset."
      }
    ],
    "totalDurationMs": 118222,
    "totalTokens": 37803,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 3506,
      "cache_creation_input_tokens": 1510,
      "cache_read_input_tokens": 29852,
      "output_tokens": 2935,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1510
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3506,
          "output_tokens": 2935,
          "cache_read_input_tokens": 29852,
          "cache_creation_input_tokens": 1510,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1510,
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
      "otherToolCount": 19
    }
  }
}
````

</details>

---

### Tool result

_source line 289 · 2026-05-13T09:47:50.431Z_

<details><summary>↩ Tool result · `toolu_01KJcS2o6bNcG4fYGgeff49H`</summary>

```text
# LIBERO Performance Results

## π0 Model Success Rates (%)

| Suite | SFT Baseline | Flow-SDE | Flow-Noise |
|-------|-------------|----------|-----------|
| Spatial | 65.3 | 98.4 | 99.0 |
| Object | 64.4 | 99.4 | 99.2 |
| Goal | 49.8 | 96.2 | 98.2 |
| Long | 51.2 | 90.2 | 93.8 |
| **Average** | **57.6** | **96.1** | **97.6** |

## π0.5 Model Success Rates (%)

| Suite | SFT Baseline | Flow-SDE | Flow-Noise |
|-------|-------------|----------|-----------|
| Spatial | 84.6 | 99.6 | 99.6 |
| Object | 95.4 | 100 | 100 |
| Goal | 84.6 | 98.8 | 99.6 |
| Long | 43.9 | 93.0 | 94.0 |
| **Average** | **77.1** | **97.9** | **98.3** |

## Fine-tuning Details

**Method**: The researchers implemented two approaches—Flow-Noise employs "a learnable noise network" integrated into denoising, while Flow-SDE "converts the deterministic ODE into an equivalent SDE" with hybrid sampling.

**Training Configuration**: During RL phase, the VLM remains frozen while "only fine-tune the 300M action expert model" for efficiency. The approach utilized PPO algorithm with "Generalized Advantage Estimation (GAE)" for advantage computation.

**Data**: π0 used 58 trajectories for standard tasks and 208 for Long tasks; π0.5 used 40 trajectories across all suites.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "7d78c06b-8f44-4415-a8b6-904e2817044b"
}
```

</details>

---

### System

_source line 290_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a61264daccbb284e0",
  "tool_use_id": "toolu_01DNpWqbVCTPcK6hFAJ5pLB7",
  "status": "completed",
  "output_file": "",
  "summary": "Search 2: LeRobot + LIBERO",
  "usage": {
    "total_tokens": 31713,
    "tool_uses": 17,
    "duration_ms": 118743
  },
  "uuid": "ac8ee54c-9697-4a7f-955c-febfb67fcd1b",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool result

_source line 291 · 2026-05-13T09:47:52.174Z_

<details><summary>↩ Tool result · `toolu_01DNpWqbVCTPcK6hFAJ5pLB7`</summary>

````text
Here is a comprehensive summary of all findings.

---

## LIBERO + LeRobot: Comprehensive Reference

### 1. Pre-converted Datasets on HuggingFace Hub

Multiple ready-to-use LeRobot-format LIBERO datasets exist — no conversion needed if you use these:

| Dataset | Suites | Frames | Notes |
|---|---|---|---|
| `HuggingFaceVLA/libero` | Spatial + Object + Goal + 10 | 273k | **Recommended by official docs for training** |
| `lerobot/libero` | Spatial + Object + Goal + 10 | 273,465 | 1,693 episodes, 40 tasks, Apache 2.0 |
| `physical-intelligence/libero` | Spatial + Object + Goal + 10 | 273k | PI-original, CC-BY-4.0, uses `image`/`wrist_image` keys |
| `IPEC-COMMUNITY/libero_spatial_no_noops_1.0.0_lerobot` | Spatial only | 53k | No-ops filtered, 434 episodes |
| `IPEC-COMMUNITY/libero_goal_no_noops_1.0.0_lerobot` | Goal only | 52k | No-ops filtered |
| `IPEC-COMMUNITY/libero_object_no_noops_1.0.0_lerobot` | Object only | 67k | No-ops filtered, 452 episodes |
| `IPEC-COMMUNITY/libero_10_no_noops_1.0.0_lerobot` | LIBERO-10 (Long) | 101k | No-ops filtered |
| `IPEC-COMMUNITY/libero_90_no_noops_lerobot` | LIBERO-90 | 569k | Largest; 90 tasks |
| `jesbu1/libero_90_lerobot` | LIBERO-90 | — | Used for pi0 fine-tuning |

**Note:** `lerobot/libero` and `HuggingFaceVLA/libero` contain only 4 suites (Spatial, Object, Goal, LIBERO-10). For LIBERO-90, use the IPEC-COMMUNITY collection or `jesbu1/libero_90_lerobot`.

---

### 2. Data Format

All LeRobot-format LIBERO datasets share this schema:

**Observation keys:**
- `observation.images.image` — 256×256×3 RGB, main camera (`agentview_image`), AV1-encoded MP4
- `observation.images.image2` — 256×256×3 RGB, wrist camera (`robot0_eye_in_hand_image`)
- `observation.state` — float32[8]: EEF position (3D) + axis-angle orientation (3D) + gripper qpos (2D)

**Action:** float32[7] — 6D EEF delta (xyz + rxryrz) + 1D gripper, clipped to [-1, 1]

**Metadata per frame:** `timestamp`, `frame_index`, `episode_index`, `task_index`, `index`

**FPS:** 10 Hz

**Physical-Intelligence version** uses slightly different keys: `image` / `wrist_image` / `state` / `actions` (no `observation.` prefix).

---

### 3. Conversion Scripts

#### Option A: Physical Intelligence openpi script (from RLDS/tfds)
Source: https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py

Reads from RLDS-formatted data via `tfds.load()`, not raw HDF5. Extracts `image`, `wrist_image`, `state` (8D), `action` (7D), and language task string. Combines all four suites into one dataset.

```bash
uv run examples/libero/convert_libero_data_to_lerobot.py \
    --data_dir /path/to/your/data \
    --push_to_hub   # optional
```
Takes ~30 minutes. Robot type: Panda. Image writer threads: 10, processes: 5.

#### Option B: any4lerobot (from raw HDF5 directly)
Source: https://github.com/Tavish9/any4lerobot/tree/main/libero2lerobot

Converts raw LIBERO `.hdf5` files. Supports LIBERO-10/Spatial/Goal/Object. Two-step process:

**Step 1: Regenerate/preprocess trajectories** (resolution 256, filter no-ops, filter failed demos, rotate frames 180°):
```bash
python libero_utils/regenerate_libero_dataset.py \
    --resolution 256 \
    --libero_task_suite libero_90 \
    --libero_raw_data_dir /path/to/libero/datasets/libero_90 \
    --libero_target_dir /path/to/libero/datasets/libero_90_no_noops
```

**Step 2: Convert to LeRobot format:**
```bash
python libero_h5.py \
    --src-paths /path/to/libero/ \
    --output-path /path/to/local \
    --executor local \          # or "ray" for distributed
    --tasks-per-job 3 \
    --workers 10
```
Supports multi-node via Ray or SLURM. Output preserves `states.ee_state` and `states.joint_state`. Uses AV1 codec (known occasional corruption; X264 recommended as alternative).

---

### 4. Installation

```bash
pip install -e ".[libero]"          # LeRobot with LIBERO extras
export MUJOCO_GL=egl                # For headless servers
```

Requires Linux (`sys_platform == 'linux'`).

---

### 5. Training Example

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
  --eval_freq=1000
```

Fine-tuning configs available for π₀, π₀-FAST, and π₀.5. The published π₀.5 fine-tune used 6k additional steps, batch 256, 8×H100, achieving **97.5% average** across the 4 suites.

---

### 6. Evaluation

```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.control_mode=relative        # or "absolute" — must match policy training
```

Standard protocol: 10 episodes/task × 40 tasks = 400 total episodes. Control mode must match the policy's training parameterization.

---

### 7. Available Fine-tuned Models

- `lerobot/pi05_libero_base` — PI base model
- `lerobot/pi05_libero_finetuned` — Fine-tuned 6k steps, 97.5% avg
- `lerobot/pi05_libero_finetuned_v044`
- `lerobot/pi05_libero_finetuned_quantiles_v044`
- `lerobot/xvla-libero`
- `lerobot/smolvla_libero`

---

### Key URLs

- Official LIBERO docs in LeRobot: https://huggingface.co/docs/lerobot/en/libero
- HuggingFaceVLA/libero dataset: https://huggingface.co/datasets/HuggingFaceVLA/libero
- lerobot/libero dataset: https://huggingface.co/datasets/lerobot/libero
- physical-intelligence/libero: https://huggingface.co/datasets/physical-intelligence/libero
- IPEC-COMMUNITY collection (all 5 suites separately): https://huggingface.co/collections/IPEC-COMMUNITY/libero-benchmark-dataset
- openpi conversion script: https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py
- any4lerobot HDF5 converter: https://github.com/Tavish9/any4lerobot/blob/main/libero2lerobot/README.md
- lerobot-libero fork: https://github.com/huggingface/lerobot-libero
- LeRobot v0.4.0 release blog: https://huggingface.co/blog/lerobot-release-v040

agentId: a61264daccbb284e0 (use SendMessage with to: 'a61264daccbb284e0' to continue this agent)
&lt;usage>total_tokens: 33417
tool_uses: 17
duration_ms: 118745&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "affa24e3-b203-4f51-b6b4-93d3fec04a36",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search for how to use LIBERO benchmark datasets with HuggingFace LeRobot framework. LIBERO is a robot manipulation benchmark with multiple task suites (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90).\n\nDo the following searches and fetch relevant pages:\n\n1. WebSearch for \"lerobot LIBERO dataset\"\n2. WebSearch for \"convert LIBERO to lerobot format\"\n3. WebSearch for \"lerobot LIBERO fine-tune\"\n4. WebSearch for \"huggingface lerobot libero 2025 2026\"\n5. WebSearch for \"LIBERO dataset huggingface hub\"\n6. Check if LIBERO datasets exist on HuggingFace Hub by searching: \"site:huggingface.co LIBERO lerobot dataset\"\n\nFor any relevant results, fetch the pages and extract:\n- How to convert LIBERO HDF5 data to LeRobot dataset format\n- Whether there are pre-converted LIBERO datasets on HuggingFace Hub\n- Any conversion scripts or tools\n- Data format details (observation keys, action dimensions, episode structure)\n\nCompile a comprehensive summary of all findings with URLs.",
    "agentId": "a61264daccbb284e0",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is a comprehensive summary of all findings.\n\n---\n\n## LIBERO + LeRobot: Comprehensive Reference\n\n### 1. Pre-converted Datasets on HuggingFace Hub\n\nMultiple ready-to-use LeRobot-format LIBERO datasets exist — no conversion needed if you use these:\n\n| Dataset | Suites | Frames | Notes |\n|---|---|---|---|\n| `HuggingFaceVLA/libero` | Spatial + Object + Goal + 10 | 273k | **Recommended by official docs for training** |\n| `lerobot/libero` | Spatial + Object + Goal + 10 | 273,465 | 1,693 episodes, 40 tasks, Apache 2.0 |\n| `physical-intelligence/libero` | Spatial + Object + Goal + 10 | 273k | PI-original, CC-BY-4.0, uses `image`/`wrist_image` keys |\n| `IPEC-COMMUNITY/libero_spatial_no_noops_1.0.0_lerobot` | Spatial only | 53k | No-ops filtered, 434 episodes |\n| `IPEC-COMMUNITY/libero_goal_no_noops_1.0.0_lerobot` | Goal only | 52k | No-ops filtered |\n| `IPEC-COMMUNITY/libero_object_no_noops_1.0.0_lerobot` | Object only | 67k | No-ops filtered, 452 episodes |\n| `IPEC-COMMUNITY/libero_10_no_noops_1.0.0_lerobot` | LIBERO-10 (Long) | 101k | No-ops filtered |\n| `IPEC-COMMUNITY/libero_90_no_noops_lerobot` | LIBERO-90 | 569k | Largest; 90 tasks |\n| `jesbu1/libero_90_lerobot` | LIBERO-90 | — | Used for pi0 fine-tuning |\n\n**Note:** `lerobot/libero` and `HuggingFaceVLA/libero` contain only 4 suites (Spatial, Object, Goal, LIBERO-10). For LIBERO-90, use the IPEC-COMMUNITY collection or `jesbu1/libero_90_lerobot`.\n\n---\n\n### 2. Data Format\n\nAll LeRobot-format LIBERO datasets share this schema:\n\n**Observation keys:**\n- `observation.images.image` — 256×256×3 RGB, main camera (`agentview_image`), AV1-encoded MP4\n- `observation.images.image2` — 256×256×3 RGB, wrist camera (`robot0_eye_in_hand_image`)\n- `observation.state` — float32[8]: EEF position (3D) + axis-angle orientation (3D) + gripper qpos (2D)\n\n**Action:** float32[7] — 6D EEF delta (xyz + rxryrz) + 1D gripper, clipped to [-1, 1]\n\n**Metadata per frame:** `timestamp`, `frame_index`, `episode_index`, `task_index`, `index`\n\n**FPS:** 10 Hz\n\n**Physical-Intelligence version** uses slightly different keys: `image` / `wrist_image` / `state` / `actions` (no `observation.` prefix).\n\n---\n\n### 3. Conversion Scripts\n\n#### Option A: Physical Intelligence openpi script (from RLDS/tfds)\nSource: https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py\n\nReads from RLDS-formatted data via `tfds.load()`, not raw HDF5. Extracts `image`, `wrist_image`, `state` (8D), `action` (7D), and language task string. Combines all four suites into one dataset.\n\n```bash\nuv run examples/libero/convert_libero_data_to_lerobot.py \\\n    --data_dir /path/to/your/data \\\n    --push_to_hub   # optional\n```\nTakes ~30 minutes. Robot type: Panda. Image writer threads: 10, processes: 5.\n\n#### Option B: any4lerobot (from raw HDF5 directly)\nSource: https://github.com/Tavish9/any4lerobot/tree/main/libero2lerobot\n\nConverts raw LIBERO `.hdf5` files. Supports LIBERO-10/Spatial/Goal/Object. Two-step process:\n\n**Step 1: Regenerate/preprocess trajectories** (resolution 256, filter no-ops, filter failed demos, rotate frames 180°):\n```bash\npython libero_utils/regenerate_libero_dataset.py \\\n    --resolution 256 \\\n    --libero_task_suite libero_90 \\\n    --libero_raw_data_dir /path/to/libero/datasets/libero_90 \\\n    --libero_target_dir /path/to/libero/datasets/libero_90_no_noops\n```\n\n**Step 2: Convert to LeRobot format:**\n```bash\npython libero_h5.py \\\n    --src-paths /path/to/libero/ \\\n    --output-path /path/to/local \\\n    --executor local \\          # or \"ray\" for distributed\n    --tasks-per-job 3 \\\n    --workers 10\n```\nSupports multi-node via Ray or SLURM. Output preserves `states.ee_state` and `states.joint_state`. Uses AV1 codec (known occasional corruption; X264 recommended as alternative).\n\n---\n\n### 4. Installation\n\n```bash\npip install -e \".[libero]\"          # LeRobot with LIBERO extras\nexport MUJOCO_GL=egl                # For headless servers\n```\n\nRequires Linux (`sys_platform == 'linux'`).\n\n---\n\n### 5. Training Example\n\n```bash\nlerobot-train \\\n  --policy.type=smolvla \\\n  --policy.repo_id=${HF_USER}/libero-test \\\n  --policy.load_vlm_weights=true \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --env.type=libero \\\n  --env.task=libero_10 \\\n  --output_dir=./outputs/ \\\n  --steps=100000 \\\n  --batch_size=4 \\\n  --eval_freq=1000\n```\n\nFine-tuning configs available for π₀, π₀-FAST, and π₀.5. The published π₀.5 fine-tune used 6k additional steps, batch 256, 8×H100, achieving **97.5% average** across the 4 suites.\n\n---\n\n### 6. Evaluation\n\n```bash\nlerobot-eval \\\n  --policy.path=\"your-policy-id\" \\\n  --env.type=libero \\\n  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\\n  --eval.batch_size=1 \\\n  --eval.n_episodes=10 \\\n  --env.control_mode=relative        # or \"absolute\" — must match policy training\n```\n\nStandard protocol: 10 episodes/task × 40 tasks = 400 total episodes. Control mode must match the policy's training parameterization.\n\n---\n\n### 7. Available Fine-tuned Models\n\n- `lerobot/pi05_libero_base` — PI base model\n- `lerobot/pi05_libero_finetuned` — Fine-tuned 6k steps, 97.5% avg\n- `lerobot/pi05_libero_finetuned_v044`\n- `lerobot/pi05_libero_finetuned_quantiles_v044`\n- `lerobot/xvla-libero`\n- `lerobot/smolvla_libero`\n\n---\n\n### Key URLs\n\n- Official LIBERO docs in LeRobot: https://huggingface.co/docs/lerobot/en/libero\n- HuggingFaceVLA/libero dataset: https://huggingface.co/datasets/HuggingFaceVLA/libero\n- lerobot/libero dataset: https://huggingface.co/datasets/lerobot/libero\n- physical-intelligence/libero: https://huggingface.co/datasets/physical-intelligence/libero\n- IPEC-COMMUNITY collection (all 5 suites separately): https://huggingface.co/collections/IPEC-COMMUNITY/libero-benchmark-dataset\n- openpi conversion script: https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py\n- any4lerobot HDF5 converter: https://github.com/Tavish9/any4lerobot/blob/main/libero2lerobot/README.md\n- lerobot-libero fork: https://github.com/huggingface/lerobot-libero\n- LeRobot v0.4.0 release blog: https://huggingface.co/blog/lerobot-release-v040"
      }
    ],
    "totalDurationMs": 118745,
    "totalTokens": 33417,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 452,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 29964,
      "output_tokens": 2302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 699
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 452,
          "output_tokens": 2302,
          "cache_read_input_tokens": 29964,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 699,
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
      "otherToolCount": 17
    }
  }
}
````

</details>

---

### System

_source line 292_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "description": "Fetching https://openvla-oft.github.io/",
  "usage": {
    "total_tokens": 41257,
    "tool_uses": 30,
    "duration_ms": 109983
  },
  "last_tool_name": "WebFetch",
  "uuid": "fbd34e71-e8d8-43ac-8885-6e75d041791d",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool call

_source line 293_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0123DJDRrNK2cPoHHhTexKRf`</summary>

```json
{
  "url": "https://openvla-oft.github.io/",
  "prompt": "Extract full comparison table showing per-suite LIBERO success rates (Spatial, Object, Goal, Long) for ALL baselines including Octo, Diffusion Policy, MDT, Seer, DiT Policy, pi0, and OpenVLA variants. Also extract complete training hyperparameters table."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "564dd4fa-25c1-477b-8cb2-17535d2a085e",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XJBVsx5oCKZtkzuxQZkmjd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 816,
      "cache_creation_input_tokens": 1574,
      "cache_read_input_tokens": 37916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1574,
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

_source line 294_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ab8a247202a01a197",
  "tool_use_id": "toolu_01EGZ1QZXBAfBeNAZjF5tKUZ",
  "status": "completed",
  "output_file": "",
  "summary": "Search 3: SmolVLA action dims",
  "usage": {
    "total_tokens": 36398,
    "tool_uses": 23,
    "duration_ms": 121729
  },
  "uuid": "2b4a3ef4-65e3-4033-a0b7-b4b2d49edecb",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool result

_source line 295 · 2026-05-13T09:48:01.149Z_

<details><summary>↩ Tool result · `toolu_01EGZ1QZXBAfBeNAZjF5tKUZ`</summary>

````text
I now have all the key information. Here is the compiled analysis:

---

## SmolVLA Action Space

### Base Model (`lerobot/smolvla_base`) Config
Source: `config.json` at HuggingFace

| Parameter | Value |
|---|---|
| `output_features.action.shape` | **[6]** — 6-dimensional actions |
| `input_features.observation.state.shape` | **[6]** — 6D proprioceptive state |
| `max_action_dim` | **32** (internal padding ceiling) |
| `max_state_dim` | 32 |
| `chunk_size` | 50 |
| `n_action_steps` | 50 |

The base model was trained on SO-100/SO-101 robot data, which uses a **6-DOF joint position control** scheme: `[shoulder_pan, shoulder_lift, elbow_flex, wrist_flex, wrist_roll, gripper]`. This is **not** end-effector control.

### Dynamic Padding Mechanism
SmolVLA internally pads all actions to `max_action_dim=32` during training and forward passes, then crops back to `action_feature.shape[0]` for output. This means the model can accept **any action space ≤ 32D** without architectural changes — the `output_features.action.shape` in the loaded config drives the actual output dimension automatically. No manual `action_mode` override is needed.

---

## LIBERO Action Space

Source: Official LeRobot LIBERO documentation + `HuggingFaceVLA/libero` dataset schema

| Parameter | Value |
|---|---|
| Action dimension | **7** — `Box(-1, 1, shape=(7,))` |
| Breakdown | **6D end-effector delta + 1D gripper** |
| Components | `[dx, dy, dz, droll, dpitch, dyaw, gripper]` |
| Control mode | **Relative** (delta) by default; absolute mode also available |
| State dimension | **8** — `[eef_pos(3), axis-angle(3), gripper_qpos(2)]` |
| Cameras | `agentview_image` + `robot0_eye_in_hand_image` |
| Robot | Franka Panda (7-DOF arm) |

Example action vectors from the dataset:
- `[0.016, 0, 0, 0, 0, 0, -1]` — gripper close
- `[-0.053, -0.085, 0.489, 0, 0, 0, 1]` — move + gripper open

---

## Compatibility Analysis: SmolVLA base vs. LIBERO

| Dimension | SmolVLA base | LIBERO | Mismatch? |
|---|---|---|---|
| Action dim | **6** | **7** | YES |
| Control type | Joint position (SO-100) | EEF delta (Franka) | YES |
| State dim | **6** | **8** | YES |
| Camera inputs | 3 cameras | 2 cameras | Minor |
| Gripper representation | 1 joint position dim | 1 continuous dim in [-1,1] | Different scale/semantics |

### Key Mismatch: 6D vs. 7D
SmolVLA base uses **6D joint position** actions for the SO-100/SO-101 arm. LIBERO uses **7D end-effector delta** actions (6D pose delta + 1D gripper). These are fundamentally different control paradigms, not just different dimension counts.

### How to Handle When Fine-tuning SmolVLA on LIBERO
Because of the dynamic padding mechanism, **the action_dim mismatch is handled automatically**. When you fine-tune using:
```bash
lerobot-train \
  --policy.type=smolvla \
  --policy.repo_id=${HF_USER}/smolvla_libero \
  --policy.load_vlm_weights=true \
  --dataset.repo_id=HuggingFaceVLA/libero \
  --env.type=libero
```
LeRobot detects `action.shape=[7]` from the LIBERO dataset and sets `output_features.action.shape=[7]` automatically. The model pads to 32D internally, then crops to 7 at output. No manual `action_dim` override is needed.

The state dimension changes similarly: LIBERO's 8D state (`observation.state.shape=[8]`) replaces the base model's 6D state.

### Critical Non-Architectural Mismatch: Normalization Statistics
The base model's normalization stats (`stats.json`) are calibrated for SO-100 joint-space data (values in radians, small range). LIBERO actions are EEF deltas in a completely different numerical range. **You must use the normalization statistics computed from the LIBERO dataset**, not those from `smolvla_base`. LeRobot recomputes these automatically during fine-tuning if you pass `--dataset.repo_id=HuggingFaceVLA/libero`.

### HuggingFaceVLA's Pre-trained LIBERO Checkpoint
`HuggingFaceVLA/smolvla_libero` is SmolVLA fine-tuned directly on LIBERO with 7D actions. This checkpoint has `output_features.action.shape=[7]` and LIBERO-specific normalization stats baked in.

---

## Summary

- **SmolVLA base**: 6D joint position control (SO-100/SO-101), `action.shape=[6]`, `state.shape=[6]`
- **LIBERO**: 7D EEF delta control (Franka Panda), `action.shape=[7]`, `state.shape=[8]`
- **Mismatch**: Both dimension count (6 vs 7) and control paradigm (joint vs EEF)
- **Resolution**: Dynamic padding in SmolVLA handles dimension differences automatically during fine-tuning; the model self-configures to 7D output when trained on LIBERO data. The VLM backbone weights transfer; the action expert head adjusts to the new action space.
- **No manual `action_dim` parameter needed** — it is inferred from dataset metadata.

Sources:
- [SmolVLA paper (arXiv 2506.01844)](https://arxiv.org/html/2506.01844v1)
- [lerobot/smolvla_base config.json](https://huggingface.co/lerobot/smolvla_base/blob/04d96c1f9167360280aaa54de31418f824d1ef48/config.json)
- [LeRobot LIBERO documentation](https://huggingface.co/docs/lerobot/libero)
- [LeRobot LIBERO-plus documentation](https://huggingface.co/docs/lerobot/main/libero_plus)
- [HuggingFaceVLA/libero dataset](https://huggingface.co/datasets/HuggingFaceVLA/libero)
- [GitHub Issue #2259 — Fine-tuning on different envs/embodiments](https://github.com/huggingface/lerobot/issues/2259)
- [Fine Tuning SmolVLA blog post (Medium)](https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632)
- [SmolVLA HuggingFace blog](https://huggingface.co/blog/smolvla)

agentId: ab8a247202a01a197 (use SendMessage with to: 'ab8a247202a01a197' to continue this agent)
&lt;usage>total_tokens: 37659
tool_uses: 23
duration_ms: 121730&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "1c1baa31-a763-47d0-9c48-870466f11e00",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search for SmolVLA's action dimension specification and architecture details. SmolVLA is a Vision-Language-Action model from HuggingFace LeRobot. We need to understand its action space (especially whether it uses 6D or 7D actions, and how the gripper action is handled).\n\nDo the following searches:\n\n1. WebSearch for \"SmolVLA action dimension architecture\"\n2. WebSearch for \"SmolVLA 7D action gripper\"\n3. WebSearch for \"SmolVLA paper arxiv\"\n4. WebSearch for \"SmolVLA action space configuration\"\n5. WebSearch for \"lerobot action_dim smolvla config\"\n6. If you find a paper or technical report, fetch it and extract the action space details\n\nAlso search for LIBERO's action space:\n7. WebSearch for \"LIBERO benchmark action space dimension\"\n8. WebSearch for \"LIBERO 7D action delta position\"\n\nFor each result, record:\n- URL\n- Action dimension details (what each dimension represents)\n- How to configure action_dim when fine-tuning\n- Any mismatch between SmolVLA's default action space and LIBERO's action space\n\nCompile findings about both SmolVLA and LIBERO action spaces, and analyze compatibility.",
    "agentId": "ab8a247202a01a197",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the key information. Here is the compiled analysis:\n\n---\n\n## SmolVLA Action Space\n\n### Base Model (`lerobot/smolvla_base`) Config\nSource: `config.json` at HuggingFace\n\n| Parameter | Value |\n|---|---|\n| `output_features.action.shape` | **[6]** — 6-dimensional actions |\n| `input_features.observation.state.shape` | **[6]** — 6D proprioceptive state |\n| `max_action_dim` | **32** (internal padding ceiling) |\n| `max_state_dim` | 32 |\n| `chunk_size` | 50 |\n| `n_action_steps` | 50 |\n\nThe base model was trained on SO-100/SO-101 robot data, which uses a **6-DOF joint position control** scheme: `[shoulder_pan, shoulder_lift, elbow_flex, wrist_flex, wrist_roll, gripper]`. This is **not** end-effector control.\n\n### Dynamic Padding Mechanism\nSmolVLA internally pads all actions to `max_action_dim=32` during training and forward passes, then crops back to `action_feature.shape[0]` for output. This means the model can accept **any action space ≤ 32D** without architectural changes — the `output_features.action.shape` in the loaded config drives the actual output dimension automatically. No manual `action_mode` override is needed.\n\n---\n\n## LIBERO Action Space\n\nSource: Official LeRobot LIBERO documentation + `HuggingFaceVLA/libero` dataset schema\n\n| Parameter | Value |\n|---|---|\n| Action dimension | **7** — `Box(-1, 1, shape=(7,))` |\n| Breakdown | **6D end-effector delta + 1D gripper** |\n| Components | `[dx, dy, dz, droll, dpitch, dyaw, gripper]` |\n| Control mode | **Relative** (delta) by default; absolute mode also available |\n| State dimension | **8** — `[eef_pos(3), axis-angle(3), gripper_qpos(2)]` |\n| Cameras | `agentview_image` + `robot0_eye_in_hand_image` |\n| Robot | Franka Panda (7-DOF arm) |\n\nExample action vectors from the dataset:\n- `[0.016, 0, 0, 0, 0, 0, -1]` — gripper close\n- `[-0.053, -0.085, 0.489, 0, 0, 0, 1]` — move + gripper open\n\n---\n\n## Compatibility Analysis: SmolVLA base vs. LIBERO\n\n| Dimension | SmolVLA base | LIBERO | Mismatch? |\n|---|---|---|---|\n| Action dim | **6** | **7** | YES |\n| Control type | Joint position (SO-100) | EEF delta (Franka) | YES |\n| State dim | **6** | **8** | YES |\n| Camera inputs | 3 cameras | 2 cameras | Minor |\n| Gripper representation | 1 joint position dim | 1 continuous dim in [-1,1] | Different scale/semantics |\n\n### Key Mismatch: 6D vs. 7D\nSmolVLA base uses **6D joint position** actions for the SO-100/SO-101 arm. LIBERO uses **7D end-effector delta** actions (6D pose delta + 1D gripper). These are fundamentally different control paradigms, not just different dimension counts.\n\n### How to Handle When Fine-tuning SmolVLA on LIBERO\nBecause of the dynamic padding mechanism, **the action_dim mismatch is handled automatically**. When you fine-tune using:\n```bash\nlerobot-train \\\n  --policy.type=smolvla \\\n  --policy.repo_id=${HF_USER}/smolvla_libero \\\n  --policy.load_vlm_weights=true \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --env.type=libero\n```\nLeRobot detects `action.shape=[7]` from the LIBERO dataset and sets `output_features.action.shape=[7]` automatically. The model pads to 32D internally, then crops to 7 at output. No manual `action_dim` override is needed.\n\nThe state dimension changes similarly: LIBERO's 8D state (`observation.state.shape=[8]`) replaces the base model's 6D state.\n\n### Critical Non-Architectural Mismatch: Normalization Statistics\nThe base model's normalization stats (`stats.json`) are calibrated for SO-100 joint-space data (values in radians, small range). LIBERO actions are EEF deltas in a completely different numerical range. **You must use the normalization statistics computed from the LIBERO dataset**, not those from `smolvla_base`. LeRobot recomputes these automatically during fine-tuning if you pass `--dataset.repo_id=HuggingFaceVLA/libero`.\n\n### HuggingFaceVLA's Pre-trained LIBERO Checkpoint\n`HuggingFaceVLA/smolvla_libero` is SmolVLA fine-tuned directly on LIBERO with 7D actions. This checkpoint has `output_features.action.shape=[7]` and LIBERO-specific normalization stats baked in.\n\n---\n\n## Summary\n\n- **SmolVLA base**: 6D joint position control (SO-100/SO-101), `action.shape=[6]`, `state.shape=[6]`\n- **LIBERO**: 7D EEF delta control (Franka Panda), `action.shape=[7]`, `state.shape=[8]`\n- **Mismatch**: Both dimension count (6 vs 7) and control paradigm (joint vs EEF)\n- **Resolution**: Dynamic padding in SmolVLA handles dimension differences automatically during fine-tuning; the model self-configures to 7D output when trained on LIBERO data. The VLM backbone weights transfer; the action expert head adjusts to the new action space.\n- **No manual `action_dim` parameter needed** — it is inferred from dataset metadata.\n\nSources:\n- [SmolVLA paper (arXiv 2506.01844)](https://arxiv.org/html/2506.01844v1)\n- [lerobot/smolvla_base config.json](https://huggingface.co/lerobot/smolvla_base/blob/04d96c1f9167360280aaa54de31418f824d1ef48/config.json)\n- [LeRobot LIBERO documentation](https://huggingface.co/docs/lerobot/libero)\n- [LeRobot LIBERO-plus documentation](https://huggingface.co/docs/lerobot/main/libero_plus)\n- [HuggingFaceVLA/libero dataset](https://huggingface.co/datasets/HuggingFaceVLA/libero)\n- [GitHub Issue #2259 — Fine-tuning on different envs/embodiments](https://github.com/huggingface/lerobot/issues/2259)\n- [Fine Tuning SmolVLA blog post (Medium)](https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632)\n- [SmolVLA HuggingFace blog](https://huggingface.co/blog/smolvla)"
      }
    ],
    "totalDurationMs": 121730,
    "totalTokens": 37659,
    "totalToolUseCount": 23,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 648,
      "cache_read_input_tokens": 35148,
      "output_tokens": 1862,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 648
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1862,
          "cache_read_input_tokens": 35148,
          "cache_creation_input_tokens": 648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 648,
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
      "otherToolCount": 23
    }
  }
}
````

</details>

---

### Tool result

_source line 296 · 2026-05-13T09:48:03.083Z_

<details><summary>↩ Tool result · `toolu_0123DJDRrNK2cPoHHhTexKRf`</summary>

```text
# Response to Your Request

I've reviewed the webpage content thoroughly, and I must report that **neither of the specific tables you requested are present in the provided material**.

## What Is Available

The page includes:
- A visual chart labeled "LIBERO Simulation Benchmark: Task Performance" showing comparisons across the four LIBERO suites (Spatial, Object, Goal, Long) with multiple baselines
- References to achieving "97.1% average success rate" across the suites

However, the actual numerical data from that visualization is not transcribed in text form on the page.

## What Is Missing

1. **Per-suite breakdown table**: While the image shows results, the specific success rates for each baseline (Octo, Diffusion Policy, MDT, Seer, DiT Policy, π0, and various OpenVLA variants) per individual task suite are not provided in extractable text format.

2. **Training hyperparameters table**: No comprehensive hyperparameters table appears in the FAQ or methodology sections.

## Available Alternative

The FAQ section provides detailed GPU memory requirements for training different configurations, organized by dataset (LIBERO variants and ALOHA), but this differs from a traditional hyperparameters table covering learning rates, batch sizes, and optimization settings.

To obtain the complete tabular data you need, you would need to consult the full paper available at arXiv:2502.19645.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "9344d40e-3d3e-4dca-9f08-526abb0ae531"
}
```

</details>

---

### System

_source line 297_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "af0b3cdb13bc258bc",
  "tool_use_id": "toolu_01CR7kykRBUTiYTQ3U6bGTyJ",
  "status": "completed",
  "output_file": "",
  "summary": "Search 4: VLA + LIBERO prior work",
  "usage": {
    "total_tokens": 41762,
    "tool_uses": 30,
    "duration_ms": 183556
  },
  "uuid": "a80d8614-7ada-4375-a05a-06375a2a2876",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461"
}
```

---

### Tool result

_source line 298 · 2026-05-13T09:49:08.249Z_

<details><summary>↩ Tool result · `toolu_01CR7kykRBUTiYTQ3U6bGTyJ`</summary>

```text
I have sufficient data to compile the full summary. Here it is:

---

## VLA + LIBERO Prior Work: Comprehensive Summary

---

### Benchmark Setup (Standard LIBERO)

Four task suites, each with 10 tasks x 50 demonstrations (500 total):
- **LIBERO-Spatial**: same objects, varying spatial layouts
- **LIBERO-Object**: same scene, varying object types
- **LIBERO-Goal**: same scene/objects, varying goal predicates
- **LIBERO-Long** (aka LIBERO-10): long-horizon multi-step tasks

Standard evaluation: 500 test episodes per suite, success rate reported. Robot: Franka Panda, 7-DoF end-effector control + gripper. Inputs: third-person RGB + optionally wrist RGB + proprioception.

---

### Model-by-Model Results

#### 1. OpenVLA (baseline fine-tune) — arXiv:2406.09246
- **Architecture**: 7B LLM (LLaMA-2) + visual encoder (SigLIP), trained on Open X-Embodiment
- **Fine-tuning method**: LoRA r=32, α=32, no quantization
- **Training**: 50K steps, lr=5e-4, batch=128 (8×A100 80GB), image augmentations (random crop, color jitter)
- **Action space**: 7 discrete tokens per step (3 translation, 3 rotation, 1 gripper), single-step prediction
- **LIBERO results**:

| Suite | Success Rate |
|-------|-------------|
| Spatial | 84.7% |
| Object | 88.4% |
| Goal | 79.2% |
| Long | 53.7% |
| **Average** | **76.5%** |

- **Checkpoints**: Public on HuggingFace — `openvla/openvla-7b-finetuned-libero-{spatial,object,goal,10}`

---

#### 2. OpenVLA-OFT (Optimized Fine-Tuning) — arXiv:2502.19645, Feb 2025
- **Architecture**: Same 7B backbone as OpenVLA + MLP action head (4 layers, ReLU), parallel decoding
- **Fine-tuning method**: LoRA (parameter-efficient), continuous action representation (L1 regression)
- **Training**: 50K–150K steps, lr=5e-4→5e-5, batch=64–128, 8×A100/H100 80GB, 1–2 days
- **Action space**: 7-dim continuous, chunk size K=8, parallel decoding (all K actions in one forward pass)
- **LIBERO results** (multi-input: third-person + wrist + proprioception):

| Suite | Success Rate |
|-------|-------------|
| Spatial | 97.6% |
| Object | 98.4% |
| Goal | 97.9% |
| Long | 94.5% |
| **Average** | **97.1%** |

- Single-input (no wrist camera) achieves 95.3% average (Cont-L1 variant)
- Inference speed: 71–109 Hz vs 4.2 Hz for base OpenVLA (26× speedup)
- **Checkpoints**: Public — `moojink/openvla-7b-oft-finetuned-libero-{spatial,object,goal,10}`
- **Code**: https://github.com/moojink/openvla-oft

---

#### 3. SpatialVLA — arXiv:2501.15830, Jan 2025
- **Architecture**: 3.5B, PaliGemma2 backbone + SigLIP + ZoeDepth for ego3D position encoding, spatial action grids
- **Fine-tuning method**: LoRA r=32, α=32 (outperforms full fine-tune on small datasets)
- **Training**: 200 epochs LIBERO fine-tuning, 120K steps; pre-training on 64×A100 for 10 days
- **Action space**: 3 spatial tokens per step (vs 7 in prior work); V=8,194 token vocab; Translation (4,096) + Rotation (4,096) + Gripper (2)
- **LIBERO results**:

| Suite | SpatialVLA | OpenVLA | TraceVLA | Octo |
|-------|-----------|---------|---------|------|
| Spatial | 88.2% | 84.7% | 84.6% | 78.9% |
| Object | 89.9% | 88.4% | 85.2% | 85.7% |
| Goal | 78.6% | 79.2% | 75.1% | 84.6% |
| Long | 55.5% | 53.7% | 54.1% | 51.1% |
| **Avg** | **78.1%** | **76.5%** | **74.8%** | **75.1%** |

- **Checkpoints**: `IPEC-COMMUNITY/spatialvla-4b-224-pt` on HuggingFace

---

#### 4. Octo — arXiv:2405.12213
- **Architecture**: Transformer-based diffusion policy, trained on Open X-Embodiment
- **Fine-tuning method**: Full fine-tune on LIBERO data
- **LIBERO results** (from SpatialVLA comparison table):

| Suite | Success Rate |
|-------|-------------|
| Spatial | 78.9% |
| Object | 85.7% |
| Goal | 84.6% |
| Long | 51.1% |
| **Average** | **75.1%** |

- Known reproducibility issues reported in community (some users getting 0% without careful config)
- **Checkpoints**: Available at octo-models.github.io

---

#### 5. π0 (Pi Zero) — Physical Intelligence, open-sourced 2025
- **Architecture**: 4B VLA, PaliGemma + flow matching action expert
- **Fine-tuning method**: Full fine-tune (JAX-based), also supports LoRA; official LIBERO configs in openpi repo
- **Training**: Supports configurable batch_size (default 32), 100K steps typical
- **Action space**: Continuous, flow matching over 7-dim actions, configurable chunk size
- **LIBERO results** (SFT baseline, from π_RL paper arXiv:2510.25889):

| Suite | π0 SFT | π0.5 SFT |
|-------|--------|---------|
| Spatial | 65.3% | 84.6% |
| Object | 64.4% | 95.4% |
| Goal | 49.8% | 84.6% |
| Long | 51.2% | 43.9% |
| **Average** | **57.6%** | **77.1%** |

- Note: OpenVLA-OFT paper reports π0 (fine-tuned, multi-input) at **94.2%** avg — this is a more heavily tuned variant
- **Checkpoints**: `lerobot/pi0_libero_base`, `lerobot/pi0_fast_libero_base`, plus suite-specific checkpoints
- **Code**: https://github.com/Physical-Intelligence/openpi

---

#### 6. π0 + Online RL (Flow-Noise / Flow-SDE) — arXiv:2510.25889
- Fine-tuning: RL on top of SFT checkpoint, freezes VLM, only tunes 300M action expert
- **LIBERO results** (π0 + Flow-Noise):

| Suite | π0 Flow-Noise | π0.5 Flow-Noise |
|-------|--------------|----------------|
| Spatial | 99.0% | 99.6% |
| Object | 99.2% | 100.0% |
| Goal | 98.2% | 99.6% |
| Long | 93.8% | 94.0% |
| **Average** | **97.6%** | **98.3%** |

---

#### 7. CogVLA — arXiv:2508.21046, NeurIPS 2025
- **Architecture**: OpenVLA backbone + dual vision encoders (SigLIP + DINOv2) + instruction-driven token routing/pruning
- **Fine-tuning method**: LoRA r=32, α=64
- **Training**: 60K steps, lr=5e-4, batch=64, 4×A800 80GB; action chunk K=8
- **Action space**: 7-dim continuous, parallel decoding
- **LIBERO results**:

| Suite | CogVLA | OpenVLA-OFT |
|-------|--------|-------------|
| Spatial | 98.6% | 97.6% |
| Object | 98.8% | 98.4% |
| Goal | 96.6% | 97.9% |
| Long | 95.4% | 94.5% |
| **Average** | **97.4%** | **97.1%** |

- Efficiency: 2.79× faster inference, 3.12× fewer FLOPs, 2.49× lower training cost than OpenVLA
- Real-world: 70.0% on ALOHA bimanual tasks

---

#### 8. NVIDIA Cosmos-Policy — arXiv:2601.16163, 2025
- **Architecture**: 2B diffusion transformer, fine-tuned from Cosmos-Predict2-2B-Video2World (latent video diffusion model)
- **Fine-tuning method**: Full model fine-tune, single stage, no architectural changes; actions/proprioception encoded as latent frames
- **Training**: 40K steps, global batch=1,920, 64×H100 80GB, ~48 hours; 2,000 total demonstrations
- **Action space**: 7-dim continuous, chunk size K=16, 5 denoising steps at inference; dual cameras (third-person 224×224 + wrist), 9-dim proprioception
- **LIBERO results**:

| Suite | Cosmos-Policy |
|-------|--------------|
| Spatial | 98.1% |
| Object | 100.0% |
| Goal | 98.2% |
| Long | 97.6% |
| **Average** | **98.5%** |

- Evaluated over 6,000 trials total (3 seeds × 2,000 episodes); current SOTA on standard LIBERO
- **Checkpoint**: `nvidia/Cosmos-Policy-LIBERO-Predict2-2B`
- **Code**: https://github.com/NVlabs/cosmos-policy

---

#### 9. UniVLA — arXiv:2506.19850, RSS 2025
- **Architecture**: Unified VLA with autoregressive discrete token modeling for vision, language, and action; incorporates world modeling
- **LIBERO results**: 95.5% average (surpasses π0-FAST's 85.5%)
- Per-suite breakdown: not yet extracted; paper at arXiv:2505.06111

---

#### 10. LightVLA — ICRA 2026
- **Architecture**: OpenVLA-OFT + differentiable token pruning; retains 78/512 visual tokens on average
- **LIBERO results**: ~99.7% average (OpenVLA-OFT baseline 97.1% + 2.6% improvement)
- Efficiency: 59.1% FLOPs reduction, 38.2% latency reduction vs OpenVLA-OFT
- **Code**: https://github.com/LiAutoAD/LightVLA

---

#### 11. MoDE (Mixture of Denoising Experts) — ICLR 2025
- **Architecture**: Diffusion transformer with MoE denoisers, pre-trained on diverse robot data
- **LIBERO-90**: 0.95 success rate (95%); first to exceed 90% on LIBERO-10
- 90% fewer FLOPs than standard Diffusion Transformer
- **Code**: https://github.com/intuitive-robots/MoDE_Diffusion_Policy

---

### Consolidated Leaderboard (Standard LIBERO, Average Across 4 Suites)

| Model | Avg SR | Method | Checkpoints Public |
|-------|--------|--------|-------------------|
| Cosmos-Policy | 98.5% | Full FT (video diffusion) | Yes (HF) |
| π0.5 + Flow-Noise (RL) | 98.3% | RL fine-tune | Yes (openpi) |
| π0 + Flow-Noise (RL) | 97.6% | RL fine-tune | Yes (openpi) |
| LightVLA | ~99.7%* | LoRA + token pruning | Yes (HF) |
| CogVLA | 97.4% | LoRA r=32 | Yes (HF) |
| OpenVLA-OFT | 97.1% | LoRA (parallel decoding) | Yes (HF) |
| UniVLA | 95.5% | Autoregressive discrete | Partial |
| π0 (tuned multi-input) | 94.2% | Full FT (flow matching) | Yes (HF) |
| MoDE | ~95% (LIBERO-90) | Diffusion MoE | Yes (GitHub) |
| π0.5 SFT | 77.1% | Full FT | Yes (openpi) |
| SpatialVLA | 78.1% | LoRA r=32 | Yes (HF) |
| OpenVLA | 76.5% | LoRA r=32 | Yes (HF) |
| Octo | 75.1% | Full FT | Yes (octo-models) |
| π0 SFT | 57.6% | Full FT | Yes (HF) |

*LightVLA claims 2.6% improvement over OpenVLA-OFT; given OFT multi-input is 97.1%, actual may be ~99.7%

---

### Key Observations

1. **LoRA r=32 is the dominant fine-tuning recipe** for token-prediction VLAs (OpenVLA family, SpatialVLA, CogVLA). Full fine-tune is used for flow matching models (π0 family).

2. **Action chunking (K=8 for LIBERO) + parallel decoding** is the single biggest jump in both performance and speed for autoregressive VLAs.

3. **Continuous action representation + L1 loss** consistently outperforms discrete tokenization.

4. **High benchmark scores do not imply robustness** — LIBERO-Plus and LIBERO-PRO papers show models with >95% on standard LIBERO can drop to near 0% under position perturbations.

5. **Hardware**: LoRA fine-tune takes 1–2 days on 8×A100 80GB. Full diffusion model training (Cosmos-Policy) requires 64×H100 for 48 hours.

6. **Data scale**: All methods use 500 demonstrations per suite (50 demos × 10 tasks). LIBERO datasets are ~10GB total, available in RLDS format on HuggingFace.

---

### Key URLs

- OpenVLA HF checkpoints: https://huggingface.co/openvla
- OpenVLA-OFT paper: https://arxiv.org/abs/2502.19645
- OpenVLA-OFT project: https://openvla-oft.github.io/
- OpenVLA-OFT code: https://github.com/moojink/openvla-oft
- π0 openpi: https://github.com/Physical-Intelligence/openpi
- π0 HF (lerobot): https://huggingface.co/lerobot/pi0_libero_base
- Cosmos-Policy: https://arxiv.org/html/2601.16163v1
- Cosmos-Policy HF: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B
- SpatialVLA: https://arxiv.org/html/2501.15830v2
- CogVLA: https://arxiv.org/html/2508.21046v1
- LightVLA: https://github.com/LiAutoAD/LightVLA
- UniVLA: https://arxiv.org/abs/2506.19850
- π_RL (RL fine-tuning): https://arxiv.org/html/2510.25889v1
- LIBERO-Plus robustness: https://arxiv.org/html/2510.13626v1

agentId: af0b3cdb13bc258bc (use SendMessage with to: 'af0b3cdb13bc258bc' to continue this agent)
&lt;usage>total_tokens: 44992
tool_uses: 30
duration_ms: 183557&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "b4568ac0-6c67-429f-b52a-f5da07ab2343",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search for existing work on fine-tuning VLA (Vision-Language-Action) models on LIBERO benchmark. We want to know if anyone has already done this and what results they got.\n\nDo the following searches:\n\n1. WebSearch for \"OpenVLA LIBERO fine-tune\"\n2. WebSearch for \"VLA fine-tune LIBERO benchmark\"\n3. WebSearch for \"LIBERO fine-tuned VLA checkpoint\"\n4. WebSearch for \"OpenVLA LIBERO results 2025 2026\"\n5. WebSearch for \"pi0 LIBERO\" (Physical Intelligence's model)\n6. WebSearch for \"octo LIBERO fine-tune\"\n7. WebSearch for \"RT-2 LIBERO\" or \"diffusion policy LIBERO\"\n\nFor any relevant papers or blog posts, fetch and extract:\n- Model name and architecture\n- Fine-tuning method (full, LoRA, etc.)\n- LIBERO task suites used\n- Results/success rates\n- Training details (epochs, learning rate, batch size, GPU hours)\n- Whether checkpoints are publicly available\n- Action space configuration used\n\nCompile a comprehensive summary of all VLA + LIBERO prior work, with URLs and key results.",
    "agentId": "af0b3cdb13bc258bc",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I have sufficient data to compile the full summary. Here it is:\n\n---\n\n## VLA + LIBERO Prior Work: Comprehensive Summary\n\n---\n\n### Benchmark Setup (Standard LIBERO)\n\nFour task suites, each with 10 tasks x 50 demonstrations (500 total):\n- **LIBERO-Spatial**: same objects, varying spatial layouts\n- **LIBERO-Object**: same scene, varying object types\n- **LIBERO-Goal**: same scene/objects, varying goal predicates\n- **LIBERO-Long** (aka LIBERO-10): long-horizon multi-step tasks\n\nStandard evaluation: 500 test episodes per suite, success rate reported. Robot: Franka Panda, 7-DoF end-effector control + gripper. Inputs: third-person RGB + optionally wrist RGB + proprioception.\n\n---\n\n### Model-by-Model Results\n\n#### 1. OpenVLA (baseline fine-tune) — arXiv:2406.09246\n- **Architecture**: 7B LLM (LLaMA-2) + visual encoder (SigLIP), trained on Open X-Embodiment\n- **Fine-tuning method**: LoRA r=32, α=32, no quantization\n- **Training**: 50K steps, lr=5e-4, batch=128 (8×A100 80GB), image augmentations (random crop, color jitter)\n- **Action space**: 7 discrete tokens per step (3 translation, 3 rotation, 1 gripper), single-step prediction\n- **LIBERO results**:\n\n| Suite | Success Rate |\n|-------|-------------|\n| Spatial | 84.7% |\n| Object | 88.4% |\n| Goal | 79.2% |\n| Long | 53.7% |\n| **Average** | **76.5%** |\n\n- **Checkpoints**: Public on HuggingFace — `openvla/openvla-7b-finetuned-libero-{spatial,object,goal,10}`\n\n---\n\n#### 2. OpenVLA-OFT (Optimized Fine-Tuning) — arXiv:2502.19645, Feb 2025\n- **Architecture**: Same 7B backbone as OpenVLA + MLP action head (4 layers, ReLU), parallel decoding\n- **Fine-tuning method**: LoRA (parameter-efficient), continuous action representation (L1 regression)\n- **Training**: 50K–150K steps, lr=5e-4→5e-5, batch=64–128, 8×A100/H100 80GB, 1–2 days\n- **Action space**: 7-dim continuous, chunk size K=8, parallel decoding (all K actions in one forward pass)\n- **LIBERO results** (multi-input: third-person + wrist + proprioception):\n\n| Suite | Success Rate |\n|-------|-------------|\n| Spatial | 97.6% |\n| Object | 98.4% |\n| Goal | 97.9% |\n| Long | 94.5% |\n| **Average** | **97.1%** |\n\n- Single-input (no wrist camera) achieves 95.3% average (Cont-L1 variant)\n- Inference speed: 71–109 Hz vs 4.2 Hz for base OpenVLA (26× speedup)\n- **Checkpoints**: Public — `moojink/openvla-7b-oft-finetuned-libero-{spatial,object,goal,10}`\n- **Code**: https://github.com/moojink/openvla-oft\n\n---\n\n#### 3. SpatialVLA — arXiv:2501.15830, Jan 2025\n- **Architecture**: 3.5B, PaliGemma2 backbone + SigLIP + ZoeDepth for ego3D position encoding, spatial action grids\n- **Fine-tuning method**: LoRA r=32, α=32 (outperforms full fine-tune on small datasets)\n- **Training**: 200 epochs LIBERO fine-tuning, 120K steps; pre-training on 64×A100 for 10 days\n- **Action space**: 3 spatial tokens per step (vs 7 in prior work); V=8,194 token vocab; Translation (4,096) + Rotation (4,096) + Gripper (2)\n- **LIBERO results**:\n\n| Suite | SpatialVLA | OpenVLA | TraceVLA | Octo |\n|-------|-----------|---------|---------|------|\n| Spatial | 88.2% | 84.7% | 84.6% | 78.9% |\n| Object | 89.9% | 88.4% | 85.2% | 85.7% |\n| Goal | 78.6% | 79.2% | 75.1% | 84.6% |\n| Long | 55.5% | 53.7% | 54.1% | 51.1% |\n| **Avg** | **78.1%** | **76.5%** | **74.8%** | **75.1%** |\n\n- **Checkpoints**: `IPEC-COMMUNITY/spatialvla-4b-224-pt` on HuggingFace\n\n---\n\n#### 4. Octo — arXiv:2405.12213\n- **Architecture**: Transformer-based diffusion policy, trained on Open X-Embodiment\n- **Fine-tuning method**: Full fine-tune on LIBERO data\n- **LIBERO results** (from SpatialVLA comparison table):\n\n| Suite | Success Rate |\n|-------|-------------|\n| Spatial | 78.9% |\n| Object | 85.7% |\n| Goal | 84.6% |\n| Long | 51.1% |\n| **Average** | **75.1%** |\n\n- Known reproducibility issues reported in community (some users getting 0% without careful config)\n- **Checkpoints**: Available at octo-models.github.io\n\n---\n\n#### 5. π0 (Pi Zero) — Physical Intelligence, open-sourced 2025\n- **Architecture**: 4B VLA, PaliGemma + flow matching action expert\n- **Fine-tuning method**: Full fine-tune (JAX-based), also supports LoRA; official LIBERO configs in openpi repo\n- **Training**: Supports configurable batch_size (default 32), 100K steps typical\n- **Action space**: Continuous, flow matching over 7-dim actions, configurable chunk size\n- **LIBERO results** (SFT baseline, from π_RL paper arXiv:2510.25889):\n\n| Suite | π0 SFT | π0.5 SFT |\n|-------|--------|---------|\n| Spatial | 65.3% | 84.6% |\n| Object | 64.4% | 95.4% |\n| Goal | 49.8% | 84.6% |\n| Long | 51.2% | 43.9% |\n| **Average** | **57.6%** | **77.1%** |\n\n- Note: OpenVLA-OFT paper reports π0 (fine-tuned, multi-input) at **94.2%** avg — this is a more heavily tuned variant\n- **Checkpoints**: `lerobot/pi0_libero_base`, `lerobot/pi0_fast_libero_base`, plus suite-specific checkpoints\n- **Code**: https://github.com/Physical-Intelligence/openpi\n\n---\n\n#### 6. π0 + Online RL (Flow-Noise / Flow-SDE) — arXiv:2510.25889\n- Fine-tuning: RL on top of SFT checkpoint, freezes VLM, only tunes 300M action expert\n- **LIBERO results** (π0 + Flow-Noise):\n\n| Suite | π0 Flow-Noise | π0.5 Flow-Noise |\n|-------|--------------|----------------|\n| Spatial | 99.0% | 99.6% |\n| Object | 99.2% | 100.0% |\n| Goal | 98.2% | 99.6% |\n| Long | 93.8% | 94.0% |\n| **Average** | **97.6%** | **98.3%** |\n\n---\n\n#### 7. CogVLA — arXiv:2508.21046, NeurIPS 2025\n- **Architecture**: OpenVLA backbone + dual vision encoders (SigLIP + DINOv2) + instruction-driven token routing/pruning\n- **Fine-tuning method**: LoRA r=32, α=64\n- **Training**: 60K steps, lr=5e-4, batch=64, 4×A800 80GB; action chunk K=8\n- **Action space**: 7-dim continuous, parallel decoding\n- **LIBERO results**:\n\n| Suite | CogVLA | OpenVLA-OFT |\n|-------|--------|-------------|\n| Spatial | 98.6% | 97.6% |\n| Object | 98.8% | 98.4% |\n| Goal | 96.6% | 97.9% |\n| Long | 95.4% | 94.5% |\n| **Average** | **97.4%** | **97.1%** |\n\n- Efficiency: 2.79× faster inference, 3.12× fewer FLOPs, 2.49× lower training cost than OpenVLA\n- Real-world: 70.0% on ALOHA bimanual tasks\n\n---\n\n#### 8. NVIDIA Cosmos-Policy — arXiv:2601.16163, 2025\n- **Architecture**: 2B diffusion transformer, fine-tuned from Cosmos-Predict2-2B-Video2World (latent video diffusion model)\n- **Fine-tuning method**: Full model fine-tune, single stage, no architectural changes; actions/proprioception encoded as latent frames\n- **Training**: 40K steps, global batch=1,920, 64×H100 80GB, ~48 hours; 2,000 total demonstrations\n- **Action space**: 7-dim continuous, chunk size K=16, 5 denoising steps at inference; dual cameras (third-person 224×224 + wrist), 9-dim proprioception\n- **LIBERO results**:\n\n| Suite | Cosmos-Policy |\n|-------|--------------|\n| Spatial | 98.1% |\n| Object | 100.0% |\n| Goal | 98.2% |\n| Long | 97.6% |\n| **Average** | **98.5%** |\n\n- Evaluated over 6,000 trials total (3 seeds × 2,000 episodes); current SOTA on standard LIBERO\n- **Checkpoint**: `nvidia/Cosmos-Policy-LIBERO-Predict2-2B`\n- **Code**: https://github.com/NVlabs/cosmos-policy\n\n---\n\n#### 9. UniVLA — arXiv:2506.19850, RSS 2025\n- **Architecture**: Unified VLA with autoregressive discrete token modeling for vision, language, and action; incorporates world modeling\n- **LIBERO results**: 95.5% average (surpasses π0-FAST's 85.5%)\n- Per-suite breakdown: not yet extracted; paper at arXiv:2505.06111\n\n---\n\n#### 10. LightVLA — ICRA 2026\n- **Architecture**: OpenVLA-OFT + differentiable token pruning; retains 78/512 visual tokens on average\n- **LIBERO results**: ~99.7% average (OpenVLA-OFT baseline 97.1% + 2.6% improvement)\n- Efficiency: 59.1% FLOPs reduction, 38.2% latency reduction vs OpenVLA-OFT\n- **Code**: https://github.com/LiAutoAD/LightVLA\n\n---\n\n#### 11. MoDE (Mixture of Denoising Experts) — ICLR 2025\n- **Architecture**: Diffusion transformer with MoE denoisers, pre-trained on diverse robot data\n- **LIBERO-90**: 0.95 success rate (95%); first to exceed 90% on LIBERO-10\n- 90% fewer FLOPs than standard Diffusion Transformer\n- **Code**: https://github.com/intuitive-robots/MoDE_Diffusion_Policy\n\n---\n\n### Consolidated Leaderboard (Standard LIBERO, Average Across 4 Suites)\n\n| Model | Avg SR | Method | Checkpoints Public |\n|-------|--------|--------|-------------------|\n| Cosmos-Policy | 98.5% | Full FT (video diffusion) | Yes (HF) |\n| π0.5 + Flow-Noise (RL) | 98.3% | RL fine-tune | Yes (openpi) |\n| π0 + Flow-Noise (RL) | 97.6% | RL fine-tune | Yes (openpi) |\n| LightVLA | ~99.7%* | LoRA + token pruning | Yes (HF) |\n| CogVLA | 97.4% | LoRA r=32 | Yes (HF) |\n| OpenVLA-OFT | 97.1% | LoRA (parallel decoding) | Yes (HF) |\n| UniVLA | 95.5% | Autoregressive discrete | Partial |\n| π0 (tuned multi-input) | 94.2% | Full FT (flow matching) | Yes (HF) |\n| MoDE | ~95% (LIBERO-90) | Diffusion MoE | Yes (GitHub) |\n| π0.5 SFT | 77.1% | Full FT | Yes (openpi) |\n| SpatialVLA | 78.1% | LoRA r=32 | Yes (HF) |\n| OpenVLA | 76.5% | LoRA r=32 | Yes (HF) |\n| Octo | 75.1% | Full FT | Yes (octo-models) |\n| π0 SFT | 57.6% | Full FT | Yes (HF) |\n\n*LightVLA claims 2.6% improvement over OpenVLA-OFT; given OFT multi-input is 97.1%, actual may be ~99.7%\n\n---\n\n### Key Observations\n\n1. **LoRA r=32 is the dominant fine-tuning recipe** for token-prediction VLAs (OpenVLA family, SpatialVLA, CogVLA). Full fine-tune is used for flow matching models (π0 family).\n\n2. **Action chunking (K=8 for LIBERO) + parallel decoding** is the single biggest jump in both performance and speed for autoregressive VLAs.\n\n3. **Continuous action representation + L1 loss** consistently outperforms discrete tokenization.\n\n4. **High benchmark scores do not imply robustness** — LIBERO-Plus and LIBERO-PRO papers show models with >95% on standard LIBERO can drop to near 0% under position perturbations.\n\n5. **Hardware**: LoRA fine-tune takes 1–2 days on 8×A100 80GB. Full diffusion model training (Cosmos-Policy) requires 64×H100 for 48 hours.\n\n6. **Data scale**: All methods use 500 demonstrations per suite (50 demos × 10 tasks). LIBERO datasets are ~10GB total, available in RLDS format on HuggingFace.\n\n---\n\n### Key URLs\n\n- OpenVLA HF checkpoints: https://huggingface.co/openvla\n- OpenVLA-OFT paper: https://arxiv.org/abs/2502.19645\n- OpenVLA-OFT project: https://openvla-oft.github.io/\n- OpenVLA-OFT code: https://github.com/moojink/openvla-oft\n- π0 openpi: https://github.com/Physical-Intelligence/openpi\n- π0 HF (lerobot): https://huggingface.co/lerobot/pi0_libero_base\n- Cosmos-Policy: https://arxiv.org/html/2601.16163v1\n- Cosmos-Policy HF: https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B\n- SpatialVLA: https://arxiv.org/html/2501.15830v2\n- CogVLA: https://arxiv.org/html/2508.21046v1\n- LightVLA: https://github.com/LiAutoAD/LightVLA\n- UniVLA: https://arxiv.org/abs/2506.19850\n- π_RL (RL fine-tuning): https://arxiv.org/html/2510.25889v1\n- LIBERO-Plus robustness: https://arxiv.org/html/2510.13626v1"
      }
    ],
    "totalDurationMs": 183557,
    "totalTokens": 44992,
    "totalToolUseCount": 30,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 39490,
      "output_tokens": 4182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1319
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4182,
          "cache_read_input_tokens": 39490,
          "cache_creation_input_tokens": 1319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1319,
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
      "otherToolCount": 30
    }
  }
}
```

</details>

---

### Assistant

_source line 299_

<details><summary>Logged reasoning block</summary>

```text
All four search agents have returned comprehensive results. Let me now compile the findings into a structured report and save it as an artifact.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "c7dc83fd-91f4-40f2-8835-60a85ca31f64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DTrELV2XTG1d3qYD6AVR9u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13217,
      "cache_read_input_tokens": 24512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13217
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

_source line 300_

搜索完成。将结果整合写入 artifacts。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "fdae976b-6448-41d5-b549-8d8fdb3556a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DTrELV2XTG1d3qYD6AVR9u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13217,
      "cache_read_input_tokens": 24512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13217
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

_source line 301_

<details open><summary>🔧 Tool call — Bash · `toolu_01Rmzmr1ygbe6i9guRgkcegD`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "a8783513-7fe5-4503-a409-bc67853aee41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DTrELV2XTG1d3qYD6AVR9u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13217,
      "cache_read_input_tokens": 24512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13217
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

_source line 302 · 2026-05-13T09:49:15.981Z_

<details><summary>↩ Tool result · `toolu_01Rmzmr1ygbe6i9guRgkcegD`</summary>

```text
_project
dream_reports
libero-smolvla-env-report.md
manifest.yaml
method_section_draft.tex
mvp-point-reaching
pipeline-dimension-verification.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "ffbf76b4-8e08-49bc-8b57-e3c9347ee12a",
  "tool_use_result": {
    "stdout": "_project\ndream_reports\nlibero-smolvla-env-report.md\nmanifest.yaml\nmethod_section_draft.tex\nmvp-point-reaching\npipeline-dimension-verification.md",
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

_source line 303_

<details open><summary>🔧 Tool call — Write · `toolu_019enF2N8L7DGP3ZwUtZCY56`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/smolvla-libero-finetune-survey.md",
  "content": "# SmolVLA + LIBERO Fine-tuning 调研报告\n\n**日期**: 2026-05-13\n\n---\n\n## 1. SmolVLA Fine-tuning 官方方式\n\n### 模型概况\n- **Model ID**: `lerobot/smolvla_base`\n- **参数量**: ~450M total, ~100M trainable (action expert)\n- **架构**: SmolVLM2-500M-Video-Instruct (SigLIP + SmolLM2-1.7B) + Flow-Matching Transformer action expert\n- **默认 action/state**: `action.shape=[6]`, `state.shape=[6]` (SO-100/SO-101 joint position control)\n- **Action chunking**: `chunk_size=50`\n- **动态 padding**: 内部 pad 到 `max_action_dim=32`，输出时裁剪到实际维度\n\n### 安装\n```bash\ngit clone https://github.com/huggingface/lerobot.git && cd lerobot\npip install -e \".[smolvla]\"       # 基础\npip install -e \".[smolvla,peft]\"  # + LoRA 支持\n```\n\n### 训练命令\n\n**Full fine-tune (action expert only, VLM frozen)**:\n```bash\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --batch_size=64 \\\n  --steps=20000 \\\n  --output_dir=outputs/train/smolvla_libero \\\n  --policy.device=cuda \\\n  --policy.dtype=bfloat16\n```\n\n**LoRA fine-tune (低显存)**:\n```bash\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --policy.output_features=null \\\n  --policy.input_features=null \\\n  --policy.optimizer_lr=1e-3 \\\n  --policy.scheduler_decay_lr=1e-4 \\\n  --steps=100000 \\\n  --batch_size=32 \\\n  --peft.method_type=LORA \\\n  --peft.r=64 \\\n  --peft.lora_alpha=64\n```\n\nPEFT 默认 target modules: `q_proj`, `v_proj` + action expert 的 `state_proj`, `action_in_proj`, `action_out_proj`, `action_time_mlp_in`, `action_time_mlp_out`\n\n### 关键超参数\n\n| 参数 | 默认值 | 说明 |\n|------|--------|------|\n| steps | 20k (real) / 100k (sim) | |\n| batch_size | 64 | 低显存减到 8-16 |\n| optimizer_lr | 1e-4 (full) / 1e-3 (LoRA) | |\n| chunk_size | 50 | 每次预测的 action 步数 |\n| dtype | bfloat16 | |\n| gradient_checkpointing | true | 省显存 |\n| peft.r | 64 | LoRA rank |\n\n### 关键文档\n- 官方 fine-tune docs: https://huggingface.co/docs/lerobot/smolvla\n- PEFT/LoRA docs: https://huggingface.co/docs/lerobot/en/peft_training\n- Model card: https://huggingface.co/lerobot/smolvla_base\n- Training notebook: https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb\n- SmolVLA blog: https://huggingface.co/blog/smolvla\n- Medium 教程: https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632\n\n---\n\n## 2. LIBERO 数据 → LeRobot 格式\n\n### 现成数据集（HuggingFace Hub，无需转换）\n\n| Dataset ID | 内容 | 规模 |\n|------------|------|------|\n| **`HuggingFaceVLA/libero`** | Spatial+Object+Goal+10 | 273k frames, 1693 eps |\n| `lerobot/libero` | 同上 | 273k frames |\n| `physical-intelligence/libero` | 同上（PI 版本） | 273k frames |\n| `IPEC-COMMUNITY/libero_spatial_no_noops_*` | 仅 Spatial | 53k frames |\n| `IPEC-COMMUNITY/libero_goal_no_noops_*` | 仅 Goal | 52k frames |\n| `IPEC-COMMUNITY/libero_object_no_noops_*` | 仅 Object | 67k frames |\n| `IPEC-COMMUNITY/libero_10_no_noops_*` | 仅 LIBERO-10 | 101k frames |\n| `IPEC-COMMUNITY/libero_90_no_noops_lerobot` | LIBERO-90 | 569k frames |\n| `jesbu1/libero_90_lerobot` | LIBERO-90 (π0 用) | — |\n\n**推荐**: 直接用 `HuggingFaceVLA/libero` 或 `lerobot/libero`，无需自行转换。\n\n### 数据格式\n\n```\nobservation.images.image  → 256×256×3 (agentview, AV1 MP4)\nobservation.images.image2 → 256×256×3 (wrist camera)\nobservation.state         → float32[8]: eef_pos(3) + axis_angle(3) + gripper_qpos(2)\naction                    → float32[7]: eef_delta(6) + gripper(1), clipped [-1,1]\nFPS: 10 Hz\n```\n\n### 转换脚本（如需自己转换）\n\n**方式 A: openpi 脚本 (RLDS → LeRobot)**\n```bash\n# https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py\nuv run examples/libero/convert_libero_data_to_lerobot.py --data_dir /path/to/data --push_to_hub\n```\n\n**方式 B: any4lerobot (HDF5 → LeRobot)**\n```bash\n# https://github.com/Tavish9/any4lerobot/tree/main/libero2lerobot\npython libero_utils/regenerate_libero_dataset.py --resolution 256 --libero_task_suite libero_90\npython libero_h5.py --src-paths /path/to/libero/ --output-path /path/to/local\n```\n\n---\n\n## 3. Action Dimension 6→7 可行性\n\n### 不匹配分析\n\n| | SmolVLA base | LIBERO |\n|---|---|---|\n| Action dim | **6** (joint position) | **7** (EEF delta + gripper) |\n| State dim | **6** | **8** |\n| Control type | Joint position (SO-100) | End-effector delta (Franka) |\n\n### 解决方案：自动处理\n\nSmolVLA 内部使用动态 padding（`max_action_dim=32`），fine-tune 时 **自动从数据集推断 action_dim**。使用 LIBERO 数据训练时：\n- `output_features.action.shape` 自动设为 `[7]`\n- `input_features.observation.state.shape` 自动设为 `[8]`\n- 归一化统计量从 LIBERO 数据集重新计算\n- **无需手动修改任何维度参数**\n\n关键 flags（让 trainer 从数据集推断）:\n```\n--policy.output_features=null --policy.input_features=null\n```\n\n### 已有 checkpoint\n`lerobot/smolvla_libero` — SmolVLA 在 LIBERO 上 fine-tuned 的 checkpoint，action_dim=7。\n\n---\n\n## 4. 现成的 LIBERO Fine-tuned VLA Checkpoints\n\n### SmolVLA 系列\n| Checkpoint | 说明 |\n|------------|------|\n| `lerobot/smolvla_libero` | SmolVLA fine-tuned on LIBERO |\n\n### π0 系列\n| Checkpoint | 说明 |\n|------------|------|\n| `lerobot/pi0_libero_base` | π0 base |\n| `lerobot/pi0_fast_libero_base` | π0-FAST |\n| `lerobot/pi05_libero_finetuned` | π0.5 fine-tuned, **97.5% avg** |\n\n### OpenVLA 系列\n| Checkpoint | 说明 |\n|------------|------|\n| `openvla/openvla-7b-finetuned-libero-spatial` | per-suite |\n| `openvla/openvla-7b-finetuned-libero-object` | per-suite |\n| `openvla/openvla-7b-finetuned-libero-goal` | per-suite |\n| `openvla/openvla-7b-finetuned-libero-10` | per-suite |\n| `moojink/openvla-7b-oft-finetuned-libero-*` | OFT 版本, **97.1% avg** |\n\n### 其他\n| Checkpoint | 说明 |\n|------------|------|\n| `nvidia/Cosmos-Policy-LIBERO-Predict2-2B` | **98.5% avg**, SOTA |\n| `IPEC-COMMUNITY/spatialvla-4b-224-pt` | SpatialVLA |\n| `lerobot/xvla-libero` | xVLA |\n\n---\n\n## 5. LIBERO SOTA 排行榜\n\n| Model | Avg SR | 方法 | 显存/GPU |\n|-------|--------|------|----------|\n| LightVLA | ~99.7% | LoRA + token pruning | 8×A100 |\n| Cosmos-Policy | 98.5% | Full FT (video diffusion) | 64×H100 |\n| π0.5 + RL | 98.3% | RL fine-tune | — |\n| π0 + RL | 97.6% | RL fine-tune | — |\n| CogVLA | 97.4% | LoRA r=32 | 4×A800 |\n| OpenVLA-OFT | 97.1% | LoRA + parallel decoding | 8×A100 |\n| UniVLA | 95.5% | Autoregressive discrete | — |\n| SpatialVLA | 78.1% | LoRA r=32 | — |\n| OpenVLA | 76.5% | LoRA r=32 | 8×A100 |\n| Octo | 75.1% | Full FT | — |\n\n---\n\n## 6. 推荐的 Fine-tuning 方案\n\n### 方案 A: 直接用已有 checkpoint（最快）\n```bash\n# lerobot/smolvla_libero 已经 fine-tuned 好了，直接评估\nlerobot-eval --policy.path=lerobot/smolvla_libero --env.type=libero --env.task=libero_spatial\n```\n\n### 方案 B: 自己 fine-tune SmolVLA on LIBERO（推荐）\n```bash\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --policy.output_features=null \\\n  --policy.input_features=null \\\n  --batch_size=32 \\\n  --steps=100000 \\\n  --output_dir=outputs/smolvla_libero \\\n  --policy.device=cuda \\\n  --policy.dtype=bfloat16 \\\n  --wandb.enable=true\n```\n- 4090 24GB 可跑，batch_size 调到 8-16\n- 预计训练 8-12 小时\n\n### 方案 C: LoRA fine-tune（省显存）\n同上但加 `--peft.method_type=LORA --peft.r=64 --peft.lora_alpha=64`\n\n### 关键注意事项\n1. **数据集**: 用 `HuggingFaceVLA/libero`，不需要自己转换\n2. **Action dim**: 自动从数据集推断为 7，无需手动配置\n3. **归一化**: 自动使用 LIBERO 的 stats，不需要手动处理\n4. **评估**: `lerobot-eval --env.type=libero` 集成了 LIBERO 仿真环境\n5. **已有 checkpoint**: `lerobot/smolvla_libero` 可直接使用或作为 fine-tune 起点\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "d84b9bc0-52a4-45c2-ba6c-a0606ec8b546",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B7NPFQ4mp6WZcfM5q8k3QK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 37729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 223
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

_source line 304 · 2026-05-13T09:50:28.833Z_

<details><summary>↩ Tool result · `toolu_019enF2N8L7DGP3ZwUtZCY56`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/smolvla-libero-finetune-survey.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "fd9f7a17-eed6-40ec-80f7-22eeb1fa8736",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/smolvla-libero-finetune-survey.md",
    "content": "# SmolVLA + LIBERO Fine-tuning 调研报告\n\n**日期**: 2026-05-13\n\n---\n\n## 1. SmolVLA Fine-tuning 官方方式\n\n### 模型概况\n- **Model ID**: `lerobot/smolvla_base`\n- **参数量**: ~450M total, ~100M trainable (action expert)\n- **架构**: SmolVLM2-500M-Video-Instruct (SigLIP + SmolLM2-1.7B) + Flow-Matching Transformer action expert\n- **默认 action/state**: `action.shape=[6]`, `state.shape=[6]` (SO-100/SO-101 joint position control)\n- **Action chunking**: `chunk_size=50`\n- **动态 padding**: 内部 pad 到 `max_action_dim=32`，输出时裁剪到实际维度\n\n### 安装\n```bash\ngit clone https://github.com/huggingface/lerobot.git && cd lerobot\npip install -e \".[smolvla]\"       # 基础\npip install -e \".[smolvla,peft]\"  # + LoRA 支持\n```\n\n### 训练命令\n\n**Full fine-tune (action expert only, VLM frozen)**:\n```bash\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --batch_size=64 \\\n  --steps=20000 \\\n  --output_dir=outputs/train/smolvla_libero \\\n  --policy.device=cuda \\\n  --policy.dtype=bfloat16\n```\n\n**LoRA fine-tune (低显存)**:\n```bash\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --policy.output_features=null \\\n  --policy.input_features=null \\\n  --policy.optimizer_lr=1e-3 \\\n  --policy.scheduler_decay_lr=1e-4 \\\n  --steps=100000 \\\n  --batch_size=32 \\\n  --peft.method_type=LORA \\\n  --peft.r=64 \\\n  --peft.lora_alpha=64\n```\n\nPEFT 默认 target modules: `q_proj`, `v_proj` + action expert 的 `state_proj`, `action_in_proj`, `action_out_proj`, `action_time_mlp_in`, `action_time_mlp_out`\n\n### 关键超参数\n\n| 参数 | 默认值 | 说明 |\n|------|--------|------|\n| steps | 20k (real) / 100k (sim) | |\n| batch_size | 64 | 低显存减到 8-16 |\n| optimizer_lr | 1e-4 (full) / 1e-3 (LoRA) | |\n| chunk_size | 50 | 每次预测的 action 步数 |\n| dtype | bfloat16 | |\n| gradient_checkpointing | true | 省显存 |\n| peft.r | 64 | LoRA rank |\n\n### 关键文档\n- 官方 fine-tune docs: https://huggingface.co/docs/lerobot/smolvla\n- PEFT/LoRA docs: https://huggingface.co/docs/lerobot/en/peft_training\n- Model card: https://huggingface.co/lerobot/smolvla_base\n- Training notebook: https://colab.research.google.com/github/huggingface/notebooks/blob/main/lerobot/training-smolvla.ipynb\n- SmolVLA blog: https://huggingface.co/blog/smolvla\n- Medium 教程: https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632\n\n---\n\n## 2. LIBERO 数据 → LeRobot 格式\n\n### 现成数据集（HuggingFace Hub，无需转换）\n\n| Dataset ID | 内容 | 规模 |\n|------------|------|------|\n| **`HuggingFaceVLA/libero`** | Spatial+Object+Goal+10 | 273k frames, 1693 eps |\n| `lerobot/libero` | 同上 | 273k frames |\n| `physical-intelligence/libero` | 同上（PI 版本） | 273k frames |\n| `IPEC-COMMUNITY/libero_spatial_no_noops_*` | 仅 Spatial | 53k frames |\n| `IPEC-COMMUNITY/libero_goal_no_noops_*` | 仅 Goal | 52k frames |\n| `IPEC-COMMUNITY/libero_object_no_noops_*` | 仅 Object | 67k frames |\n| `IPEC-COMMUNITY/libero_10_no_noops_*` | 仅 LIBERO-10 | 101k frames |\n| `IPEC-COMMUNITY/libero_90_no_noops_lerobot` | LIBERO-90 | 569k frames |\n| `jesbu1/libero_90_lerobot` | LIBERO-90 (π0 用) | — |\n\n**推荐**: 直接用 `HuggingFaceVLA/libero` 或 `lerobot/libero`，无需自行转换。\n\n### 数据格式\n\n```\nobservation.images.image  → 256×256×3 (agentview, AV1 MP4)\nobservation.images.image2 → 256×256×3 (wrist camera)\nobservation.state         → float32[8]: eef_pos(3) + axis_angle(3) + gripper_qpos(2)\naction                    → float32[7]: eef_delta(6) + gripper(1), clipped [-1,1]\nFPS: 10 Hz\n```\n\n### 转换脚本（如需自己转换）\n\n**方式 A: openpi 脚本 (RLDS → LeRobot)**\n```bash\n# https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py\nuv run examples/libero/convert_libero_data_to_lerobot.py --data_dir /path/to/data --push_to_hub\n```\n\n**方式 B: any4lerobot (HDF5 → LeRobot)**\n```bash\n# https://github.com/Tavish9/any4lerobot/tree/main/libero2lerobot\npython libero_utils/regenerate_libero_dataset.py --resolution 256 --libero_task_suite libero_90\npython libero_h5.py --src-paths /path/to/libero/ --output-path /path/to/local\n```\n\n---\n\n## 3. Action Dimension 6→7 可行性\n\n### 不匹配分析\n\n| | SmolVLA base | LIBERO |\n|---|---|---|\n| Action dim | **6** (joint position) | **7** (EEF delta + gripper) |\n| State dim | **6** | **8** |\n| Control type | Joint position (SO-100) | End-effector delta (Franka) |\n\n### 解决方案：自动处理\n\nSmolVLA 内部使用动态 padding（`max_action_dim=32`），fine-tune 时 **自动从数据集推断 action_dim**。使用 LIBERO 数据训练时：\n- `output_features.action.shape` 自动设为 `[7]`\n- `input_features.observation.state.shape` 自动设为 `[8]`\n- 归一化统计量从 LIBERO 数据集重新计算\n- **无需手动修改任何维度参数**\n\n关键 flags（让 trainer 从数据集推断）:\n```\n--policy.output_features=null --policy.input_features=null\n```\n\n### 已有 checkpoint\n`lerobot/smolvla_libero` — SmolVLA 在 LIBERO 上 fine-tuned 的 checkpoint，action_dim=7。\n\n---\n\n## 4. 现成的 LIBERO Fine-tuned VLA Checkpoints\n\n### SmolVLA 系列\n| Checkpoint | 说明 |\n|------------|------|\n| `lerobot/smolvla_libero` | SmolVLA fine-tuned on LIBERO |\n\n### π0 系列\n| Checkpoint | 说明 |\n|------------|------|\n| `lerobot/pi0_libero_base` | π0 base |\n| `lerobot/pi0_fast_libero_base` | π0-FAST |\n| `lerobot/pi05_libero_finetuned` | π0.5 fine-tuned, **97.5% avg** |\n\n### OpenVLA 系列\n| Checkpoint | 说明 |\n|------------|------|\n| `openvla/openvla-7b-finetuned-libero-spatial` | per-suite |\n| `openvla/openvla-7b-finetuned-libero-object` | per-suite |\n| `openvla/openvla-7b-finetuned-libero-goal` | per-suite |\n| `openvla/openvla-7b-finetuned-libero-10` | per-suite |\n| `moojink/openvla-7b-oft-finetuned-libero-*` | OFT 版本, **97.1% avg** |\n\n### 其他\n| Checkpoint | 说明 |\n|------------|------|\n| `nvidia/Cosmos-Policy-LIBERO-Predict2-2B` | **98.5% avg**, SOTA |\n| `IPEC-COMMUNITY/spatialvla-4b-224-pt` | SpatialVLA |\n| `lerobot/xvla-libero` | xVLA |\n\n---\n\n## 5. LIBERO SOTA 排行榜\n\n| Model | Avg SR | 方法 | 显存/GPU |\n|-------|--------|------|----------|\n| LightVLA | ~99.7% | LoRA + token pruning | 8×A100 |\n| Cosmos-Policy | 98.5% | Full FT (video diffusion) | 64×H100 |\n| π0.5 + RL | 98.3% | RL fine-tune | — |\n| π0 + RL | 97.6% | RL fine-tune | — |\n| CogVLA | 97.4% | LoRA r=32 | 4×A800 |\n| OpenVLA-OFT | 97.1% | LoRA + parallel decoding | 8×A100 |\n| UniVLA | 95.5% | Autoregressive discrete | — |\n| SpatialVLA | 78.1% | LoRA r=32 | — |\n| OpenVLA | 76.5% | LoRA r=32 | 8×A100 |\n| Octo | 75.1% | Full FT | — |\n\n---\n\n## 6. 推荐的 Fine-tuning 方案\n\n### 方案 A: 直接用已有 checkpoint（最快）\n```bash\n# lerobot/smolvla_libero 已经 fine-tuned 好了，直接评估\nlerobot-eval --policy.path=lerobot/smolvla_libero --env.type=libero --env.task=libero_spatial\n```\n\n### 方案 B: 自己 fine-tune SmolVLA on LIBERO（推荐）\n```bash\nlerobot-train \\\n  --policy.path=lerobot/smolvla_base \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --policy.output_features=null \\\n  --policy.input_features=null \\\n  --batch_size=32 \\\n  --steps=100000 \\\n  --output_dir=outputs/smolvla_libero \\\n  --policy.device=cuda \\\n  --policy.dtype=bfloat16 \\\n  --wandb.enable=true\n```\n- 4090 24GB 可跑，batch_size 调到 8-16\n- 预计训练 8-12 小时\n\n### 方案 C: LoRA fine-tune（省显存）\n同上但加 `--peft.method_type=LORA --peft.r=64 --peft.lora_alpha=64`\n\n### 关键注意事项\n1. **数据集**: 用 `HuggingFaceVLA/libero`，不需要自己转换\n2. **Action dim**: 自动从数据集推断为 7，无需手动配置\n3. **归一化**: 自动使用 LIBERO 的 stats，不需要手动处理\n4. **评估**: `lerobot-eval --env.type=libero` 集成了 LIBERO 仿真环境\n5. **已有 checkpoint**: `lerobot/smolvla_libero` 可直接使用或作为 fine-tune 起点\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Assistant

_source line 305_

Now register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "2cf5cee9-1b8a-4054-83a4-c8391d23e1f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C4wTV5ftNjRcARGvErquf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3770,
      "cache_read_input_tokens": 37952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3770
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

_source line 306_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ToGPCF38jkVf8sM4XJx7tR`</summary>

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
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "90dff5f0-0461-4756-8b02-2938d28b32fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C4wTV5ftNjRcARGvErquf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3770,
      "cache_read_input_tokens": 37952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3770
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

_source line 307 · 2026-05-13T09:50:38.288Z_

<details><summary>↩ Tool result · `toolu_01ToGPCF38jkVf8sM4XJx7tR`</summary>

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
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "379de664-41da-41da-9b5e-aca2e12346f6",
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

_source line 308_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013Gmyk8ys6VMBtDdapadaaV`</summary>

```json
{
  "query": "select:TaskOutput",
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
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "a383acbc-a649-4e45-a3ea-8443727f23a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KYJWcUVRDjNJ5kfk2oQYMy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 41722,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 430
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

_source line 309 · 2026-05-13T09:50:43.952Z_

<details><summary>↩ Tool result · `toolu_013Gmyk8ys6VMBtDdapadaaV`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TaskOutput"
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
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "e1eff749-d66d-4c28-9f3e-e379f85870b1",
  "tool_use_result": {
    "matches": [
      "TaskOutput"
    ],
    "query": "select:TaskOutput",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 310_

报告已写入 `artifacts/smolvla-libero-finetune-survey.md`。核心结论：

### 1. SmolVLA Fine-tuning 官方方式
- `lerobot-train --policy.path=lerobot/smolvla_base --dataset.repo_id=HuggingFaceVLA/libero`
- 支持 full fine-tune（仅 action expert, VLM frozen）和 LoRA
- 官方文档: https://huggingface.co/docs/lerobot/smolvla

### 2. LIBERO 数据
**不需要自己转换**。Hub 上已有 `HuggingFaceVLA/libero`（273k frames, 4 suites），直接用。LIBERO-90 用 `IPEC-COMMUNITY/libero_90_no_noops_lerobot`。

### 3. Action Dim 6→7
**自动处理**。SmolVLA 内部 pad 到 `max_action_dim=32`，fine-tune 时从数据集推断 `action.shape=[7]`、`state.shape=[8]`。加 `--policy.output_features=null --policy.input_features=null` 让 trainer 自动推断。

### 4. 现成 Checkpoint
- **`lerobot/smolvla_libero`** — SmolVLA 已 fine-tuned on LIBERO，可直接用
- `lerobot/pi05_libero_finetuned` — π0.5, 97.5% avg
- `moojink/openvla-7b-oft-finetuned-libero-*` — OpenVLA-OFT, 97.1% avg
- `nvidia/Cosmos-Policy-LIBERO-Predict2-2B` — SOTA 98.5%

### 5. 推荐方案
先验证 `lerobot/smolvla_libero` 是否满足需求。如需自己训练，在 4090 上用 batch_size=8-16、100k steps、bfloat16 即可跑通。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "uuid": "963bca3c-6745-463a-a807-65b6a038088f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ezLSYaTXQxBcDWBnjb6Ej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 514,
      "cache_read_input_tokens": 42152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 514
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

### Task result

_source line 311_

报告已写入 `artifacts/smolvla-libero-finetune-survey.md`。核心结论：

### 1. SmolVLA Fine-tuning 官方方式
- `lerobot-train --policy.path=lerobot/smolvla_base --dataset.repo_id=HuggingFaceVLA/libero`
- 支持 full fine-tune（仅 action expert, VLM frozen）和 LoRA
- 官方文档: https://huggingface.co/docs/lerobot/smolvla

### 2. LIBERO 数据
**不需要自己转换**。Hub 上已有 `HuggingFaceVLA/libero`（273k frames, 4 suites），直接用。LIBERO-90 用 `IPEC-COMMUNITY/libero_90_no_noops_lerobot`。

### 3. Action Dim 6→7
**自动处理**。SmolVLA 内部 pad 到 `max_action_dim=32`，fine-tune 时从数据集推断 `action.shape=[7]`、`state.shape=[8]`。加 `--policy.output_features=null --policy.input_features=null` 让 trainer 自动推断。

### 4. 现成 Checkpoint
- **`lerobot/smolvla_libero`** — SmolVLA 已 fine-tuned on LIBERO，可直接用
- `lerobot/pi05_libero_finetuned` — π0.5, 97.5% avg
- `moojink/openvla-7b-oft-finetuned-libero-*` — OpenVLA-OFT, 97.1% avg
- `nvidia/Cosmos-Policy-LIBERO-Predict2-2B` — SOTA 98.5%

### 5. 推荐方案
先验证 `lerobot/smolvla_libero` 是否满足需求。如需自己训练，在 4090 上用 batch_size=8-16、100k steps、bfloat16 即可跑通。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 328355,
  "duration_api_ms": 1005958,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "eb86aa8a-be57-4220-ae4f-7bfc8f7ab461",
  "total_cost_usd": 3.218548750000001,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 30825,
    "cache_read_input_tokens": 219245,
    "output_tokens": 6194,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 30825,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 3,
        "output_tokens": 558,
        "cache_read_input_tokens": 42152,
        "cache_creation_input_tokens": 514,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 514
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1198225,
      "outputTokens": 39722,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 35,
      "costUSD": 1.746835,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 6194,
      "cacheReadInputTokens": 219245,
      "cacheCreationInputTokens": 30825,
      "webSearchRequests": 0,
      "costUSD": 0.45720374999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    },
    "claude-sonnet-4-6": {
      "inputTokens": 20012,
      "outputTokens": 19536,
      "cacheReadInputTokens": 776330,
      "cacheCreationInputTokens": 114276,
      "webSearchRequests": 0,
      "costUSD": 1.01451,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d75ddd3d-7be4-4861-9079-51bf143178ae"
}
```

</details>

---
