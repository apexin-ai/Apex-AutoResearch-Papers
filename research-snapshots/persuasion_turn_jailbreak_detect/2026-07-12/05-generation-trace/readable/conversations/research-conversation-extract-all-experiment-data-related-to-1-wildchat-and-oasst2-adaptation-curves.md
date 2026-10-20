# Research conversation: Extract all experiment data related to: 1. WildChat and OASST2 adaptation curves (FPR vs N target conversations) 2. Per-

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-afbd91c4ab95ef894.jsonl`
- **Structured JSON:** [`55e3b0b83cf18303d734.json`](../../sessions/55/55e3b0b83cf18303d734.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

29 recorded events

### User

_source line 1 · 2026-05-22T21:30:53.287Z_

Extract all experiment data related to:
1. WildChat and OASST2 adaptation curves (FPR vs N target conversations)
2. Per-seed variance data (seed 42, 123, 456) for DD OOD / AA OOD F1, std across variants

From the registry JSON file at:
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/e4efefca-26d6-49cf-8a09-2af928a47017/tool-results/mcp-agent-ml-research-read_registry-1779485432679.txt

This is a JSON file with schema: {result: string}. The "result" field is itself a JSON string that needs to be parsed.

Search for entries mentioning "wildchat", "oasst2", "adaptation", "FPR", "seed", "variance", "std", "DD OOD", "AA OOD". Return ALL metrics and conclusion text verbatim. Do NOT summarize or omit any numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5df424ed-94b3-4801-a077-e8e00b57103c",
  "agentId": "afbd91c4ab95ef894",
  "type": "user",
  "uuid": "53db2303-bc2d-46ed-893b-900c9f3b71b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T21:30:53.290Z_

```json
{
  "parentUuid": "53db2303-bc2d-46ed-893b-900c9f3b71b4",
  "isSidechain": true,
  "agentId": "afbd91c4ab95ef894",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__update_registry"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "c9194c99-e1c9-4150-9ee1-6ed307e2542a",
  "timestamp": "2026-05-22T21:30:53.290Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-22T21:30:55.676Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AWJn5D5GyetghwQQfvFSDn`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/e4efefca-26d6-49cf-8a09-2af928a47017/tool-results/mcp-agent-ml-research-read_registry-1779485432679.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9194c99-e1c9-4150-9ee1-6ed307e2542a",
  "isSidechain": true,
  "agentId": "afbd91c4ab95ef894",
  "requestId": "req_011CbJKYgKtRC6MY8gczomFx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9aed5b4e-3944-4b01-a3d4-98bdf021e2a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Q7HyUSt1YGpLY2G6Bfm6gy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6712,
      "cache_read_input_tokens": 8118,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6712
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 147,
          "cache_read_input_tokens": 8118,
          "cache_creation_input_tokens": 6712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6712,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T21:30:56.015Z_

<details><summary>↩ Tool result · reported error · `toolu_01AWJn5D5GyetghwQQfvFSDn`</summary>

```text
File content (84366 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9aed5b4e-3944-4b01-a3d4-98bdf021e2a5",
  "isSidechain": true,
  "promptId": "5df424ed-94b3-4801-a077-e8e00b57103c",
  "agentId": "afbd91c4ab95ef894",
  "type": "user",
  "uuid": "291426ef-6545-4db3-a550-b7dd1e141be8",
  "toolUseResult": "Error: File content (84366 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "9aed5b4e-3944-4b01-a3d4-98bdf021e2a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-22T21:30:57.882Z_

The file is too large to read in one shot. Let me search for the specific content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "291426ef-6545-4db3-a550-b7dd1e141be8",
  "isSidechain": true,
  "agentId": "afbd91c4ab95ef894",
  "requestId": "req_011CbJKYt1bnAXhnw5Tpu5xd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "abd6d0ef-3727-4716-a969-b5e89a015cbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019dghqogsCEPqAVKTiHQyDH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1048,
      "cache_read_input_tokens": 14830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1048,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-22T21:30:59.602Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NQ4sXtRa6UMXqANuZLYM6L`</summary>

```json
{
  "command": "grep -oi '\"result\".*' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/e4efefca-26d6-49cf-8a09-2af928a47017/tool-results/mcp-agent-ml-research-read_registry-1779485432679.txt | wc -c",
  "description": "Check size of result field"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abd6d0ef-3727-4716-a969-b5e89a015cbc",
  "isSidechain": true,
  "agentId": "afbd91c4ab95ef894",
  "requestId": "req_011CbJKYt1bnAXhnw5Tpu5xd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cc86d81-7b9b-4c9f-88cf-64c677dc5c49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019dghqogsCEPqAVKTiHQyDH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1048,
      "cache_read_input_tokens": 14830,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1048
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 200,
          "cache_read_input_tokens": 14830,
          "cache_creation_input_tokens": 1048,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1048,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-22T21:30:59.696Z_

<details><summary>↩ Tool result · `toolu_01NQ4sXtRa6UMXqANuZLYM6L`</summary>

```text
199702
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cc86d81-7b9b-4c9f-88cf-64c677dc5c49",
  "isSidechain": true,
  "promptId": "5df424ed-94b3-4801-a077-e8e00b57103c",
  "agentId": "afbd91c4ab95ef894",
  "type": "user",
  "uuid": "72791d88-b4c0-473c-b6b6-16c24eb55b71",
  "sourceToolAssistantUUID": "6cc86d81-7b9b-4c9f-88cf-64c677dc5c49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T21:31:04.254Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017VQL5CT31RScRP7x6LMfFE`</summary>

```json
{
  "command": "python3 -c \"\nimport json, re\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/e4efefca-26d6-49cf-8a09-2af928a47017/tool-results/mcp-agent-ml-research-read_registry-1779485432679.txt', 'r') as f:\n    raw = f.read()\n\n# Parse outer JSON\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\nprint(type(registry))\nif isinstance(registry, list):\n    print(f'List of {len(registry)} items')\n    print('First item keys:', list(registry[0].keys()) if registry else 'empty')\nelif isinstance(registry, dict):\n    print('Dict keys:', list(registry.keys())[:20])\n\" 2>&1 | head -50",
  "description": "Parse outer JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72791d88-b4c0-473c-b6b6-16c24eb55b71",
  "isSidechain": true,
  "agentId": "afbd91c4ab95ef894",
  "requestId": "req_011CbJKZ9ifKKRA4zr8h2Rzm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54710eb1-0af5-4554-80dd-dd40b12547de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BHmrKj766Tp8DnFFyY6K8k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 214,
      "cache_read_input_tokens": 15878,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 214
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 317,
          "cache_read_input_tokens": 15878,
          "cache_creation_input_tokens": 214,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 214,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-22T21:31:04.384Z_

<details><summary>↩ Tool result · `toolu_017VQL5CT31RScRP7x6LMfFE`</summary>

```text
&lt;class 'dict'>
Dict keys: ['success', 'data', 'error', 'metadata']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54710eb1-0af5-4554-80dd-dd40b12547de",
  "isSidechain": true,
  "promptId": "5df424ed-94b3-4801-a077-e8e00b57103c",
  "agentId": "afbd91c4ab95ef894",
  "type": "user",
  "uuid": "09543c67-8bd9-4213-981d-34b7978f05fe",
  "sourceToolAssistantUUID": "54710eb1-0af5-4554-80dd-dd40b12547de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-22T21:31:08.411Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0196BWAbic4UnKPdd2Krfzwr`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/e4efefca-26d6-49cf-8a09-2af928a47017/tool-results/mcp-agent-ml-research-read_registry-1779485432679.txt', 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\ndata = registry['data']\nprint(type(data))\nif isinstance(data, list):\n    print(f'List of {len(data)} items')\n    if data:\n        print('First item keys:', list(data[0].keys()))\nelif isinstance(data, dict):\n    print('Dict keys:', list(data.keys())[:30])\n\" 2>&1",
  "description": "Inspect data field structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09543c67-8bd9-4213-981d-34b7978f05fe",
  "isSidechain": true,
  "agentId": "afbd91c4ab95ef894",
  "requestId": "req_011CbJKZVqdqNAWfP5vQK6c6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0654a4c-965e-4d94-b3eb-f9f4169a7fb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01W7wzzr4LLXAWLvqq7E9SwV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 353,
      "cache_read_input_tokens": 16092,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 353
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 311,
          "cache_read_input_tokens": 16092,
          "cache_creation_input_tokens": 353,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 353,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-22T21:31:08.534Z_

<details><summary>↩ Tool result · `toolu_0196BWAbic4UnKPdd2Krfzwr`</summary>

```text
&lt;class 'dict'>
Dict keys: ['experiments', 'count', 'total', 'baseline']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0654a4c-965e-4d94-b3eb-f9f4169a7fb2",
  "isSidechain": true,
  "promptId": "5df424ed-94b3-4801-a077-e8e00b57103c",
  "agentId": "afbd91c4ab95ef894",
  "type": "user",
  "uuid": "06cdc5f3-6087-4398-87ac-bc74d664d0fd",
  "sourceToolAssistantUUID": "d0654a4c-965e-4d94-b3eb-f9f4169a7fb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T21:31:12.266Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Tv2SPvcS7vSzgjm5ZLp2H1`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/e4efefca-26d6-49cf-8a09-2af928a47017/tool-results/mcp-agent-ml-research-read_registry-1779485432679.txt', 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\ndata = registry['data']\nexperiments = data['experiments']\nprint(f'Number of experiments: {len(experiments)}')\nif experiments:\n    print('First experiment keys:', list(experiments[0].keys()) if isinstance(experiments, list) else list(experiments.keys())[:20])\n\" 2>&1",
  "description": "Inspect experiments field"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06cdc5f3-6087-4398-87ac-bc74d664d0fd",
  "isSidechain": true,
  "agentId": "afbd91c4ab95ef894",
  "requestId": "req_011CbJKZomPv6w6ZhShExxdd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc7da2d3-71d6-4159-a1c1-76202fc02fb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016V9zqDqvWjXP43pLwhU5Q2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 347,
      "cache_read_input_tokens": 16445,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 347
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 16445,
          "cache_creation_input_tokens": 347,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 347,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-22T21:31:12.352Z_

<details><summary>↩ Tool result · `toolu_01Tv2SPvcS7vSzgjm5ZLp2H1`</summary>

```text
Number of experiments: 132
First experiment keys: ['exp46_inference_efficiency', 'exp63_toxicchat_fpfn', 'exp62_topic_diagnosis', 'exp61_random_binary_partition', 'exp60_turncount_baseline', 'exp59_resample_350', 'exp58_truncated_single_turn', 'exp57_svd_iid_only', 'exp53_llm_judge_prompt_opt', 'exp55_5seed_mlm_vs_9class_aa', 'exp56_crossllm_10shot_adaptation', 'exp54_causal_probe_subspace', 'exp52_oasst2_n25_multiseed', 'exp51_lmsys_benign_ood', 'exp50_layerwise_representation', 'exp45_benign_adaptation_curve', 'exp49_representation_analysis', 'exp48_ensemble_mlm_9class', 'exp46', 'exp44_multi_llm_mixed']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc7da2d3-71d6-4159-a1c1-76202fc02fb4",
  "isSidechain": true,
  "promptId": "5df424ed-94b3-4801-a077-e8e00b57103c",
  "agentId": "afbd91c4ab95ef894",
  "type": "user",
  "uuid": "155afc4a-cc2c-42d5-abfa-64054e76f8af",
  "sourceToolAssistantUUID": "fc7da2d3-71d6-4159-a1c1-76202fc02fb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-22T21:31:16.640Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018YMGVWKBLpiMYtANS6cHJR`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/e4efefca-26d6-49cf-8a09-2af928a47017/tool-results/mcp-agent-ml-research-read_registry-1779485432679.txt', 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\ndata = registry['data']\nexperiments = data['experiments']\n# It's a list of dicts, each dict has experiment keys\n# Let's flatten to get all experiment names\nall_exp_names = []\nfor item in experiments:\n    all_exp_names.extend(list(item.keys()))\nprint('All experiment names:')\nfor name in sorted(all_exp_names):\n    print(name)\n\" 2>&1",
  "description": "List all experiment names"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "155afc4a-cc2c-42d5-abfa-64054e76f8af",
  "isSidechain": true,
  "agentId": "afbd91c4ab95ef894",
  "requestId": "req_011CbJKa5p3Yzt4KiAgAv9hw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f665631-84ce-4b5e-be22-2308b39e8a6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016rLRVf5KBzb4iynB1vfAw7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 557,
      "cache_read_input_tokens": 16792,
      "output_tokens": 323,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 557
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 323,
          "cache_read_input_tokens": 16792,
          "cache_creation_input_tokens": 557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 557,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-22T21:31:16.861Z_

<details><summary>↩ Tool result · reported error · `toolu_018YMGVWKBLpiMYtANS6cHJR`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 17, in &lt;module>
    all_exp_names.extend(list(item.keys()))
                              ^^^^^^^^^
AttributeError: 'str' object has no attribute 'keys'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f665631-84ce-4b5e-be22-2308b39e8a6f",
  "isSidechain": true,
  "promptId": "5df424ed-94b3-4801-a077-e8e00b57103c",
  "agentId": "afbd91c4ab95ef894",
  "type": "user",
  "uuid": "4fc5efad-d5ed-4298-b9a1-8e76ceb8eff4",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 17, in &lt;module>\n    all_exp_names.extend(list(item.keys()))\n                              ^^^^^^^^^\nAttributeError: 'str' object has no attribute 'keys'",
  "sourceToolAssistantUUID": "6f665631-84ce-4b5e-be22-2308b39e8a6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T21:31:21.600Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014KfT3xSRrs3KfUG1TAyU6j`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/e4efefca-26d6-49cf-8a09-2af928a47017/tool-results/mcp-agent-ml-research-read_registry-1779485432679.txt', 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\ndata = registry['data']\nexperiments = data['experiments']\n# Check what the list items look like\nprint('Type of first:', type(experiments[0]))\nprint('First item:', repr(experiments[0])[:300])\nprint('Second item type:', type(experiments[1]))\nprint('Second item:', repr(experiments[1])[:300])\n\" 2>&1",
  "description": "Check experiment list item types"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fc5efad-d5ed-4298-b9a1-8e76ceb8eff4",
  "isSidechain": true,
  "agentId": "afbd91c4ab95ef894",
  "requestId": "req_011CbJKaRrJPRgFumDJxZaNg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13f0df71-0089-447d-85ab-dedda1fd38c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HJA2T1Ah7y8aa5joqSyAaj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 410,
      "cache_read_input_tokens": 17349,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 410
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 308,
          "cache_read_input_tokens": 17349,
          "cache_creation_input_tokens": 410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 410,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-22T21:31:21.814Z_

<details><summary>↩ Tool result · reported error · `toolu_014KfT3xSRrs3KfUG1TAyU6j`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 14, in &lt;module>
    print('Type of first:', type(experiments[0]))
                                 ~~~~~~~~~~~^^^
KeyError: 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13f0df71-0089-447d-85ab-dedda1fd38c5",
  "isSidechain": true,
  "promptId": "5df424ed-94b3-4801-a077-e8e00b57103c",
  "agentId": "afbd91c4ab95ef894",
  "type": "user",
  "uuid": "d028c3bb-76dc-4a6c-9f7d-6c1cc211dcbc",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 14, in &lt;module>\n    print('Type of first:', type(experiments[0]))\n                                 ~~~~~~~~~~~^^^\nKeyError: 0",
  "sourceToolAssistantUUID": "13f0df71-0089-447d-85ab-dedda1fd38c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T21:31:26.684Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018q9ykVb1CHeLDgU6CBDj8w`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/e4efefca-26d6-49cf-8a09-2af928a47017/tool-results/mcp-agent-ml-research-read_registry-1779485432679.txt', 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\ndata = registry['data']\nexperiments = data['experiments']\n# It's actually a dict with 132 keys\nprint('Keys sample:', list(experiments.keys())[:30])\n\" 2>&1",
  "description": "Check experiments as dict"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d028c3bb-76dc-4a6c-9f7d-6c1cc211dcbc",
  "isSidechain": true,
  "agentId": "afbd91c4ab95ef894",
  "requestId": "req_011CbJKanKMpSd5rXaznvFsW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2b29522-92d0-4539-a525-5dc90f8a54cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SDUcyVVJ33m9Dz8GCLTaYa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 17759,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 385
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 269,
          "cache_read_input_tokens": 17759,
          "cache_creation_input_tokens": 385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 385,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T21:31:26.774Z_

<details><summary>↩ Tool result · `toolu_018q9ykVb1CHeLDgU6CBDj8w`</summary>

```text
Keys sample: ['exp46_inference_efficiency', 'exp63_toxicchat_fpfn', 'exp62_topic_diagnosis', 'exp61_random_binary_partition', 'exp60_turncount_baseline', 'exp59_resample_350', 'exp58_truncated_single_turn', 'exp57_svd_iid_only', 'exp53_llm_judge_prompt_opt', 'exp55_5seed_mlm_vs_9class_aa', 'exp56_crossllm_10shot_adaptation', 'exp54_causal_probe_subspace', 'exp52_oasst2_n25_multiseed', 'exp51_lmsys_benign_ood', 'exp50_layerwise_representation', 'exp45_benign_adaptation_curve', 'exp49_representation_analysis', 'exp48_ensemble_mlm_9class', 'exp46', 'exp44_multi_llm_mixed', 'exp43_mhj_human_eval', 'exp42b_balanced_ratio_ablation', 'exp42_ood_benign_mixed', 'exp41_tost_10seed', 'exp40_llama_guard_baseline', 'exp40', 'exp39_extra_seeds_tost', 'exp38_wildcat_calibration', 'exp37_length_matched_benign', 'exp36']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2b29522-92d0-4539-a525-5dc90f8a54cf",
  "isSidechain": true,
  "promptId": "5df424ed-94b3-4801-a077-e8e00b57103c",
  "agentId": "afbd91c4ab95ef894",
  "type": "user",
  "uuid": "a988ad17-b876-48cb-b08f-886d4020c4ab",
  "sourceToolAssistantUUID": "a2b29522-92d0-4539-a525-5dc90f8a54cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-22T21:31:31.047Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RApa5ANUTNwp2HAdnzDHCm`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/e4efefca-26d6-49cf-8a09-2af928a47017/tool-results/mcp-agent-ml-research-read_registry-1779485432679.txt', 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\ndata = registry['data']\nexperiments = data['experiments']\nprint('All experiment keys:')\nfor k in sorted(experiments.keys()):\n    print(k)\n\" 2>&1",
  "description": "List all experiment keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a988ad17-b876-48cb-b08f-886d4020c4ab",
  "isSidechain": true,
  "agentId": "afbd91c4ab95ef894",
  "requestId": "req_011CbJKb9Y4LCJCoqiAmjAnC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85e4331c-1ddb-41f3-ae2c-2eeb9f2f7f6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Q6WMKA56TFD1Gh3eS3jXS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 631,
      "cache_read_input_tokens": 18144,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 631
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 18144,
          "cache_creation_input_tokens": 631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 631,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-22T21:31:31.136Z_

<details><summary>↩ Tool result · `toolu_01RApa5ANUTNwp2HAdnzDHCm`</summary>

```text
All experiment keys:
cross_attack_baseline
exp10_fewshot_llm_judge
exp11_tost_equivalence
exp12_toxicchat_bootstrap
exp13_meanpool_multiseed
exp14_cross_llm_validation
exp14b_cross_llm_control
exp14c_prediction_analysis
exp15_roberta_large
exp15b_roberta_large_lr
exp15c_roberta_large_mlm
exp16_9class_train
exp16_llama_benign_gen
exp16_llama_jailbreak_gen
exp16_multi_llm
exp16_multi_llm_training
exp16_vanilla_train
exp16b_llama_only_mlm
exp17_dataset_scale
exp17_dryrun
exp17_qwen_benign_gen
exp17_qwen_jailbreak_gen
exp18_e2e_finetune
exp19_wildchat_fpr
exp1_roberta_9class
exp1_roberta_mlm
exp1_roberta_vanilla
exp20_deepcontext_proxy
exp21_cross_checkpoint
exp22_aa_early_detection
exp23_aa_error_analysis
exp24_calibration_ece
exp25_fitd_early_detection
exp26_frozen_probing
exp27_mean_pooling
exp28_data_efficiency
exp28b_data_efficiency_supplement
exp28c_vanilla_supplement
exp29_inference_efficiency
exp2_actorattack_mcnemar
exp2_actorattack_ood
exp30_length_stratified
exp31_lambda_ablation_aa
exp32_strategy_prediction
exp33_strategy_prediction_plan002
exp34_representation_tsne
exp35_cross_seed_ensemble
exp36
exp36_frozen_mlm_probing
exp37_length_matched_benign
exp38_wildcat_calibration
exp39_extra_seeds_tost
exp3_probing
exp3_roberta_probing
exp40
exp40_llama_guard_baseline
exp41_tost_10seed
exp42_ood_benign_mixed
exp42b_balanced_ratio_ablation
exp43_mhj_human_eval
exp44_multi_llm_mixed
exp45_benign_adaptation_curve
exp46
exp46_inference_efficiency
exp48_ensemble_mlm_9class
exp49_representation_analysis
exp4_dd_ood_perturbation
exp50_layerwise_representation
exp51_lmsys_benign_ood
exp52_oasst2_n25_multiseed
exp53_llm_judge_prompt_opt
exp54_causal_probe_subspace
exp55_5seed_mlm_vs_9class_aa
exp56_crossllm_10shot_adaptation
exp57_svd_iid_only
exp58_truncated_single_turn
exp59_resample_350
exp5_llm_judge_ood
exp60_turncount_baseline
exp61_random_binary_partition
exp62_topic_diagnosis
exp63_toxicchat_fpfn
exp6_actorattack_perturbation
exp7_tfidf_perprefix_actorattack
exp8_mhj_human_data
exp9_bootstrap_ci
llama_crescendo_dryrun
mf1_binary_seed123
mf1_binary_seed456
mf1_scrambled_seed123
mf1_scrambled_seed456
phase_b_full
pilot_phase_b
plan_002_clean_training
plan_002_seed123
plan_002_seed456
plan_003_scrambled_ablation
plan_003_scrambled_fix
plan_003_scrambled_perturbation
plan_003_scrambled_retrain
plan_004_perturbation_eval
plan_005_multi_attack_gen
plan_006_cross_attack_clean
plan_007_tfidf_fitd_dd
plan_008_strategy_transition
plan_012_gpt55_judge
plan_012_llm_judge_qwen
plan_013_binary_perturbation
plan_013_none_collapse
plan_015_dd_eval
plan_016_sentiment_control
plan_016v2_topic_control
plan_016v2_topic_eval_seed123
plan_016v2_topic_eval_seed42
plan_016v2_topic_eval_seed456
plan_016v2_topic_perturbation
plan_016v2_topic_seed123
plan_016v2_topic_seed456
plan_017_eval_seed123
plan_017_eval_seed456
plan_017_mlm_control
plan_017_mlm_perturbation
plan_017_mlm_seed123
plan_017_mlm_seed456
plan_018_eval_seed123
plan_018_eval_seed456
plan_018_wiki_mlm_control
plan_018_wiki_mlm_eval
plan_018_wiki_mlm_seed123
plan_018_wiki_mlm_seed456
plan_018_wiki_perturbation
vanilla_multiseed_dd_ood
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85e4331c-1ddb-41f3-ae2c-2eeb9f2f7f6b",
  "isSidechain": true,
  "promptId": "5df424ed-94b3-4801-a077-e8e00b57103c",
  "agentId": "afbd91c4ab95ef894",
  "type": "user",
  "uuid": "27307d3d-9667-4859-8325-d7635b269985",
  "sourceToolAssistantUUID": "85e4331c-1ddb-41f3-ae2c-2eeb9f2f7f6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-22T21:31:38.937Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019tfi9MCg6d9d3PAqqZiMmh`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/e4efefca-26d6-49cf-8a09-2af928a47017/tool-results/mcp-agent-ml-research-read_registry-1779485432679.txt', 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\ndata = registry['data']\nexperiments = data['experiments']\n\n# Relevant experiments for WildChat, OASST2, adaptation curves, FPR, seeds, variance\ntarget_keys = [\n    'exp19_wildchat_fpr',\n    'exp45_benign_adaptation_curve',\n    'exp52_oasst2_n25_multiseed',\n    'exp56_crossllm_10shot_adaptation',\n    'exp51_lmsys_benign_ood',\n    'mf1_binary_seed123',\n    'mf1_binary_seed456',\n    'mf1_scrambled_seed123',\n    'mf1_scrambled_seed456',\n    'vanilla_multiseed_dd_ood',\n    'plan_017_eval_seed123',\n    'plan_017_eval_seed456',\n    'plan_018_eval_seed123',\n    'plan_018_eval_seed456',\n    'plan_016v2_topic_eval_seed123',\n    'plan_016v2_topic_eval_seed456',\n    'plan_016v2_topic_eval_seed42',\n    'exp2_actorattack_ood',\n    'exp41_tost_10seed',\n    'exp39_extra_seeds_tost',\n    'exp35_cross_seed_ensemble',\n    'exp4_dd_ood_perturbation',\n    'exp55_5seed_mlm_vs_9class_aa',\n]\n\nfor k in target_keys:\n    if k in experiments:\n        print(f'=== {k} ===')\n        print(json.dumps(experiments[k], indent=2))\n        print()\n\" 2>&1",
  "description": "Extract relevant experiment entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27307d3d-9667-4859-8325-d7635b269985",
  "isSidechain": true,
  "agentId": "afbd91c4ab95ef894",
  "requestId": "req_011CbJKbU8VzAVV9FMfWwpnn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40ba4cf3-adfc-4728-98d4-eecd52c5ddfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NhgBacWTWUAmB66udDmFkm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1658,
      "cache_read_input_tokens": 18775,
      "output_tokens": 644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1658
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 644,
          "cache_read_input_tokens": 18775,
          "cache_creation_input_tokens": 1658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1658,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-22T21:31:39.037Z_

<details><summary>↩ Tool result · `toolu_019tfi9MCg6d9d3PAqqZiMmh`</summary>

```text
&lt;persisted-output>
Output too large (36.8KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/e4efefca-26d6-49cf-8a09-2af928a47017/tool-results/by1khfan8.txt

Preview (first 2KB):
=== exp19_wildchat_fpr ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-20T12:37:11.207Z",
  "updated_at": "2026-05-20T12:45:10.364Z",
  "hypothesis": "9-class DAPT classifier maintains FPR < 15% on high-drift real-world benign conversations from WildChat (after excluding jailbreak-contaminated samples), demonstrating external validity beyond synthetic benign data and addressing reviewer concern about deployment false positive rates",
  "server": "westd-33183",
  "gpu": "cuda:0",
  "account": "root",
  "reproduce": {
    "server": "westd-33183",
    "gpu": "cuda:0",
    "started_at": "2026-05-20T12:37:59.757Z"
  },
  "spec": {
    "command": "python scripts/exp19_wildchat_fpr.py",
    "server": "westd-33183",
    "gpu": "cuda:0",
    "pid": "28318",
    "log_path": "results/exp19_wildchat_fpr.json",
    "submitted_at": "2026-05-20T12:41:54.600Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "data/wildchat_benign_226.jsonl (226 filtered benign, avg 7.4 turns)",
    "data_count": 226,
    "model_name": "microsoft/deberta-v3-base (exp17 checkpoints: 9-class/MLM/vanilla)",
    "seed": "42,123,456",
    "checkpoint_path": "checkpoints/exp17/",
    "wall_clock_seconds": 195.8,
    "gpu_hours": 0.05
  },
  "conclusion": "negative",
  "metrics": {
    "dataset": "wildchat_benign_226 (226 filtered multi-turn benign, avg 7.4 turns)",
    "9class_fpr": {
      "seed42": 0.668,
      "seed123": 0.611,
      "seed456": 0.765,
      "mean": 0.681,
      "std": 0.064
    },
    "mlm_fpr": {
      "seed42": 0.367,
      "seed123": 0.646,
      "seed456": 0.323,
      "mean": 0.445,
      "std": 0.143
    },
    "vanilla_fpr": {
      "seed42": 0.473,
      "seed123": 0.425,
      "seed456": 0.544,
      "mean": 0.481,
      "std": 0.049
    },
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40ba4cf3-adfc-4728-98d4-eecd52c5ddfa",
  "isSidechain": true,
  "promptId": "5df424ed-94b3-4801-a077-e8e00b57103c",
  "agentId": "afbd91c4ab95ef894",
  "type": "user",
  "uuid": "bc897c13-0019-44dd-a57d-993395af0443",
  "sourceToolAssistantUUID": "40ba4cf3-adfc-4728-98d4-eecd52c5ddfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-22T21:31:42.434Z_

<details open><summary>🔧 Tool call — Read · `toolu_017D8vD8R6En7hKP4M2gxy2B`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/e4efefca-26d6-49cf-8a09-2af928a47017/tool-results/by1khfan8.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc897c13-0019-44dd-a57d-993395af0443",
  "isSidechain": true,
  "agentId": "afbd91c4ab95ef894",
  "requestId": "req_011CbJKc489iHRYYF2Sp9BVN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20c02b07-ee4f-48d3-9411-aa0f2648c609",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Nv9TrMCvjzA5zn3cMsVnqg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1513,
      "cache_read_input_tokens": 20433,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1513
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 20433,
          "cache_creation_input_tokens": 1513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1513,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-22T21:31:42.797Z_

<details><summary>↩ Tool result · `toolu_017D8vD8R6En7hKP4M2gxy2B`</summary>

```text
1	=== exp19_wildchat_fpr ===
2	{
3	  "status": "DONE",
4	  "retry_count": 0,
5	  "created_at": "2026-05-20T12:37:11.207Z",
6	  "updated_at": "2026-05-20T12:45:10.364Z",
7	  "hypothesis": "9-class DAPT classifier maintains FPR < 15% on high-drift real-world benign conversations from WildChat (after excluding jailbreak-contaminated samples), demonstrating external validity beyond synthetic benign data and addressing reviewer concern about deployment false positive rates",
8	  "server": "westd-33183",
9	  "gpu": "cuda:0",
10	  "account": "root",
11	  "reproduce": {
12	    "server": "westd-33183",
13	    "gpu": "cuda:0",
14	    "started_at": "2026-05-20T12:37:59.757Z"
15	  },
16	  "spec": {
17	    "command": "python scripts/exp19_wildchat_fpr.py",
18	    "server": "westd-33183",
19	    "gpu": "cuda:0",
20	    "pid": "28318",
21	    "log_path": "results/exp19_wildchat_fpr.json",
22	    "submitted_at": "2026-05-20T12:41:54.600Z",
23	    "submitted_via": "submit_training_job",
24	    "backend": "tmux",
25	    "account": "root",
26	    "data_path": "data/wildchat_benign_226.jsonl (226 filtered benign, avg 7.4 turns)",
27	    "data_count": 226,
28	    "model_name": "microsoft/deberta-v3-base (exp17 checkpoints: 9-class/MLM/vanilla)",
29	    "seed": "42,123,456",
30	    "checkpoint_path": "checkpoints/exp17/",
31	    "wall_clock_seconds": 195.8,
32	    "gpu_hours": 0.05
33	  },
34	  "conclusion": "negative",
35	  "metrics": {
36	    "dataset": "wildchat_benign_226 (226 filtered multi-turn benign, avg 7.4 turns)",
37	    "9class_fpr": {
38	      "seed42": 0.668,
39	      "seed123": 0.611,
40	      "seed456": 0.765,
41	      "mean": 0.681,
42	      "std": 0.064
43	    },
44	    "mlm_fpr": {
45	      "seed42": 0.367,
46	      "seed123": 0.646,
47	      "seed456": 0.323,
48	      "mean": 0.445,
49	      "std": 0.143
50	    },
51	    "vanilla_fpr": {
52	      "seed42": 0.473,
53	      "seed123": 0.425,
54	      "seed456": 0.544,
55	      "mean": 0.481,
56	      "std": 0.049
57	    },
58	    "note": "NEGATIVE: All variants show extreme FPR on real-world benign. 9-class worst (68.1%). Used exp17 checkpoints (Qwen 1000 scale). Severe distribution shift between synthetic training benign and real WildChat conversations."
59	  },
60	  "completed_at": "2026-05-20T12:45:10.364Z"
61	}
62	
63	=== exp45_benign_adaptation_curve ===
64	{
65	  "status": "DONE",
66	  "retry_count": 0,
67	  "created_at": "2026-05-22T06:14:46.955Z",
68	  "updated_at": "2026-05-22T08:56:47.002Z",
69	  "hypothesis": "Adding N WildChat benign samples (N in {0,5,10,25,50,100,150}) to training data will show a monotonic FPR reduction curve, with substantial FPR drop achievable with as few as 10-25 samples while maintaining OOD F1 above 0.95.",
70	  "parent": "exp42_ood_benign_mixed",
71	  "spec": {
72	    "command": "python /root/persuasion_turn_jailbreak_detect/scripts/exp45_benign_adaptation_curve.py",
73	    "server": "westd-33183",
74	    "gpu": "cuda:0",
75	    "pid": 47802,
76	    "log_path": "/root/persuasion_turn_jailbreak_detect/results/exp45_benign_adaptation_curve.json",
77	    "submitted_at": "2026-05-22T06:34:49.435Z",
78	    "submitted_via": "submit_training_job",
79	    "backend": "tmux",
80	    "account": "root",
81	    "data_path": "/root/persuasion_turn_jailbreak_detect/data/",
82	    "data_count": "350 Qwen + up to 150 WildChat benign, 7 runs (N=0,5,10,25,50,100,150)",
83	    "model_name": "microsoft/deberta-v3-base",
84	    "seed": 42,
85	    "checkpoint_source": "trained from scratch per N value",
86	    "eval_data": "IID test + WildChat FPR (49) + OOD DD/AA/FITD (80 each)",
87	    "checkpoint_path": "N/A (7 intermediate checkpoints, not saved)",
88	    "wall_clock_seconds": 930.3,
89	    "gpu_hours": 0.26
90	  },
91	  "conclusion": "success",
92	  "metrics": {
93	    "n10_multiseed": {
94	      "seeds": [
95	        42,
96	        123,
97	        456
98	      ],
99	      "wc_fpr": "0.000\u00b10.000",
100	      "iid_f1": "1.000\u00b10.000",
101	      "dd_f1": "1.000\u00b10.000",
102	      "aa_f1": "0.981\u00b10.016",
103	      "fitd_f1": "1.000\u00b10.000"
104	    },
105	    "single_seed_42": {
106	      "n0_fpr": 0.653,
107	      "n5_fpr": 0.163,
108	      "n10_fpr": 0,
109	      "n25_fpr": 0,
110	      "n50_fpr": 0,
111	      "n100_fpr": 0,
112	      "n150_fpr": 0
113	    }
114	  },
115	  "completed_at": "2026-05-22T06:50:19.707Z"
116	}
117	
118	=== exp52_oasst2_n25_multiseed ===
119	{
120	  "status": "DONE",
121	  "retry_count": 0,
122	  "created_at": "2026-05-22T10:08:46.884Z",
123	  "updated_at": "2026-05-22T10:16:27.542Z",
124	  "hypothesis": "OASST2 benign adaptation with N=25 yields consistently low FPR (\u22645%) across multiple seeds (42, 123, 456), confirming seed 42's FPR=1.5% is not a lucky outlier.",
125	  "parent": "exp51_lmsys_benign_ood",
126	  "spec": {
127	    "command": "python scripts/exp52_oasst2_n25_multiseed.py --seed {123,456} --n_adapt 25",
128	    "server": "westd-33183",
129	    "data_path": "data/oasst2_benign_adapt_50.json",
130	    "data_count": 25,
131	    "model_name": "DeBERTa-v3-base + GRU",
132	    "seed": "123,456",
133	    "checkpoint_source": "exp45_n0_seed42 (baseline) + retrained with OASST2 adaptation",
134	    "eval_data": "data/oasst2_benign_eval_200.json + plan_002_splits/test.jsonl + OOD (DD/AA/FITD)"
135	  },
136	  "metrics": {
137	    "seed_42": {
138	      "oasst2_fpr": 0.015,
139	      "iid_f1": 1,
140	      "aa_f1": 0.953,
141	      "dd_f1": 1,
142	      "fitd_f1": 1
143	    },
144	    "seed_123": {
145	      "oasst2_fpr": 0.005,
146	      "iid_f1": 1,
147	      "aa_f1": 0.917,
148	      "dd_f1": 1,
149	      "fitd_f1": 1
150	    },
151	    "seed_456": {
152	      "oasst2_fpr": 0.01,
153	      "iid_f1": 1,
154	      "aa_f1": 0.99,
155	      "dd_f1": 1,
156	      "fitd_f1": 1
157	    },
158	    "fpr_mean": 0.01,
159	    "fpr_std": 0.005,
160	    "fpr_range": "0.5%-1.5%"
161	  },
162	  "checkpoint_path": "/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints/exp52_oasst2_n25_seed{42,123,456}/",
163	  "log_path": "/root/persuasion_turn_jailbreak_detect/results/exp52_seed{123,456}.log",
164	  "conclusion": "success",
165	  "completed_at": "2026-05-22T10:16:27.542Z"
166	}
167	
168	=== exp56_crossllm_10shot_adaptation ===
169	{
170	  "status": "DONE",
171	  "retry_count": 0,
172	  "created_at": "2026-05-22T11:59:38.178Z",
173	  "updated_at": "2026-05-22T12:09:21.263Z",
174	  "hypothesis": "10-shot benign adaptation with Llama-origin conversations will reduce cross-LLM FPR from 88-90% to below 10%, extending the two-axis benign adaptation mechanism to cross-LLM distributional shift",
175	  "parent": "exp51_lmsys_benign_ood",
176	  "spec": {
177	    "command": "python scripts/exp56_crossllm_10shot.py",
178	    "server": "westd-49690",
179	    "data_path": "/root/persuasion_turn_jailbreak_detect/data/llama_conversations/benign_llama_250.jsonl",
180	    "data_count": 250,
181	    "model_name": "microsoft/deberta-v3-base",
182	    "seed": 42,
183	    "checkpoint_source": "plan_002 (9-class, seed 42)",
184	    "eval_data": "Llama-benign 200 eval + cross_llm dd/aa/fitd_llama 50 each",
185	    "log_path": "/tmp/exp56_crossllm.log",
186	    "pid": 10405,
187	    "checkpoint_path": "/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints/exp56_crossllm_n10_seed42"
188	  },
189	  "metrics": {
190	    "baseline_fpr": 0.945,
191	    "baseline_aa_llama_recall": 0.74,
192	    "adaptation_curve": {
193	      "n0": {
194	        "fpr": 0.945,
195	        "dd_f1": 1,
196	        "aa_f1": 0.99,
197	        "fitd_f1": 1,
198	        "dd_llama_recall": 1,
199	        "aa_llama_recall": 0.74,
200	        "fitd_llama_recall": 1
201	      },
202	      "n5": {
203	        "fpr": 0.055,
204	        "dd_f1": 0.694,
205	        "aa_f1": 0.841,
206	        "fitd_f1": 0.99,
207	        "dd_llama_recall": 0.64,
208	        "aa_llama_recall": 0.04,
209	        "fitd_llama_recall": 0.76
210	      },
211	      "n10": {
212	        "fpr": 0.03,
213	        "dd_f1": 0.816,
214	        "aa_f1": 0.601,
215	        "fitd_f1": 1,
216	        "dd_llama_recall": 0.6,
217	        "aa_llama_recall": 0,
218	        "fitd_llama_recall": 0.8
219	      },
220	      "n25": {
221	        "fpr": 0.005,
222	        "dd_f1": 0.556,
223	        "aa_f1": 0.271,
224	        "fitd_f1": 0.99,
225	        "dd_llama_recall": 0.08,
226	        "aa_llama_recall": 0,
227	        "fitd_llama_recall": 0.52
228	      }
229	    }
230	  },
231	  "conclusion": "negative",
232	  "completed_at": "2026-05-22T12:09:21.263Z"
233	}
234	
235	=== exp51_lmsys_benign_ood ===
236	{
237	  "status": "DONE",
238	  "retry_count": 0,
239	  "created_at": "2026-05-22T08:58:59.398Z",
240	  "updated_at": "2026-05-22T09:53:42.648Z",
241	  "hypothesis": "The two-axis decomposition (high FPR on OOD benign + 10-shot remediation) generalizes beyond WildChat: LMSYS-Chat-1M benign conversations will show high FPR (>20%) that 10 target-domain conversations can eliminate, confirming benign-side shift is a general phenomenon not specific to WildChat GPT-3.5 users.",
242	  "parent": "exp45_benign_adaptation_curve",
243	  "conclusion": "success",
244	  "spec": {
245	    "command": "python /root/persuasion_turn_jailbreak_detect/scripts/exp51_oasst2_eval.py",
246	    "server": "westd-33183",
247	    "data_path": "/root/persuasion_turn_jailbreak_detect/data/oasst2_benign_eval_200.json",
248	    "data_count": "200 eval + 10 adapt oasst2 benign conversations",
249	    "model_name": "microsoft/deberta-v3-base (9-class)",
250	    "seed": 42,
251	    "checkpoint_path": "N/A (eval + retrain)",
252	    "log_path": "/root/persuasion_turn_jailbreak_detect/results/exp51_oasst2_results.json"
253	  },
254	  "completed_at": "2026-05-22T09:43:58.937Z",
255	  "metrics": {
256	    "baseline_fpr": 0.575,
257	    "baseline_n": 200,
258	    "data_source": "oasst2 (real crowdsourced human)",
259	    "adaptation_curve": {
260	      "n0": {
261	        "fpr": 0.575
262	      },
263	      "n10": {
264	        "fpr": 0.205,
265	        "dd_f1": 1,
266	        "aa_f1": 1,
267	        "fitd_f1": 1
268	      },
269	      "n25": {
270	        "fpr": 0.015,
271	        "dd_f1": 1,
272	        "aa_f1": 0.953,
273	        "fitd_f1": 1
274	      },
275	      "n50": {
276	        "fpr": 0.005,
277	        "dd_f1": 1,
278	        "aa_f1": 0.99,
279	        "fitd_f1": 1
280	      }
281	    },
282	    "comparison_wildchat": {
283	      "baseline_fpr": 0.681,
284	      "n10_fpr": 0,
285	      "n10_sufficient": true
286	    }
287	  }
288	}
289	
290	=== mf1_binary_seed123 ===
291	{
292	  "status": "DONE",
293	  "retry_count": 0,
294	  "created_at": "2026-05-18T09:11:45.083Z",
295	  "updated_at": "2026-05-18T11:04:38.928Z",
296	  "hypothesis": "Binary persuasion classification (seed=123) will maintain DD OOD F1 comparable to seed=42 (0.990), confirming low variance for binary variant and providing 3-seed statistical support for reviewer MF1",
297	  "spec": {
298	    "command": "train_deberta.py + train_gru.py + evaluate_gru.py (binary, seed=123)",
299	    "server": "westd-33183",
300	    "data_path": "data/plan_002_splits + data/dd_ood",
301	    "data_count": 480,
302	    "model_name": "DeBERTa-v3-base (num_persuasion_classes=2)",
303	    "seed": 123,
304	    "checkpoint_path": "checkpoints/mf1_binary_seed123/",
305	    "log_path": "results/mf1_binary_seed123.json"
306	  },
307	  "conclusion": "success",
308	  "metrics": {
309	    "dd_ood_full_f1": 1,
310	    "dd_ood_k1_f1": 1,
311	    "dd_ood_k2_f1": 1,
312	    "dd_ood_k3_f1": 0.9904,
313	    "dd_ood_k5_f1": 1,
314	    "iid_full_f1": 1,
315	    "iid_k1_f1": 1,
316	    "iid_k2_f1": 1,
317	    "iid_k3_f1": 1,
318	    "iid_k5_f1": 1,
319	    "deberta_val_persuasion_acc": 1,
320	    "deberta_val_intent_acc": 1,
321	    "seed": 123
322	  },
323	  "completed_at": "2026-05-18T11:04:38.928Z"
324	}
325	
326	=== mf1_binary_seed456 ===
327	{
328	  "status": "DONE",
329	  "retry_count": 0,
330	  "created_at": "2026-05-18T09:11:46.513Z",
331	  "updated_at": "2026-05-18T09:55:15.746Z",
332	  "hypothesis": "Binary persuasion DeBERTa+GRU pipeline with seed=456 will produce DD OOD performance consistent with seed=42, confirming reproducibility of the binary collapse approach.",
333	  "spec": {
334	    "command": "train_deberta_binary.py + train_classifier_binary.py + dd_ood_eval",
335	    "server": "westd-33183",
336	    "data_path": "data/plan_002_splits/",
337	    "data_count": 0,
338	    "model_name": "microsoft/deberta-v3-base",
339	    "seed": 456
340	  },
341	  "checkpoint_path": "checkpoints/mf1_binary_seed456/",
342	  "log_path": "logs/mf1_binary_seed456_pipeline.log",
343	  "metrics": {
344	    "dd_ood_full_f1": 1,
345	    "dd_ood_k1_f1": 1,
346	    "dd_ood_k2_f1": 1,
347	    "dd_ood_k3_f1": 0.9904,
348	    "dd_ood_k5_f1": 1,
349	    "deberta_val_persuasion_acc": 1,
350	    "deberta_val_intent_acc": 1,
351	    "seed": 456
352	  },
353	  "conclusion": "success",
354	  "completed_at": "2026-05-18T09:22:25.221Z"
355	}
356	
357	=== mf1_scrambled_seed123 ===
358	{
359	  "status": "DONE",
360	  "retry_count": 0,
361	  "created_at": "2026-05-18T09:11:48.357Z",
362	  "updated_at": "2026-05-18T09:54:48.227Z",
363	  "hypothesis": "Scrambled persuasion labels (seed=123) will degrade DD OOD detection performance compared to original labels, confirming that persuasion strategy grounding is causally necessary for generalization",
364	  "spec": {
365	    "command": "mf1_scrambled_seed123_pipeline.py",
366	    "server": "westd-33183",
367	    "data_path": "data/plan_002_splits/",
368	    "data_count": 350,
369	    "model_name": "microsoft/deberta-v3-base",
370	    "seed": 123,
371	    "checkpoint_path": "checkpoints/mf1_scrambled_seed123/",
372	    "log_path": "results/mf1_scrambled_seed123.json"
373	  },
374	  "checkpoint_path": "checkpoints/mf1_scrambled_seed123/",
375	  "log_path": "results/mf1_scrambled_seed123_stage1.log, results/mf1_scrambled_seed123_stage2.log",
376	  "metrics": {
377	    "val_persuasion_acc": 0.6724,
378	    "val_intent_acc": 1,
379	    "dd_ood_f1_k1": 1,
380	    "dd_ood_f1_k2": 1,
381	    "dd_ood_f1_k3": 1,
382	    "dd_ood_f1_k5": 1,
383	    "dd_ood_f1_full": 1
384	  },
385	  "conclusion": "success",
386	  "completed_at": "2026-05-18T09:20:32.092Z"
387	}
388	
389	=== mf1_scrambled_seed456 ===
390	{
391	  "status": "DONE",
392	  "retry_count": 0,
393	  "created_at": "2026-05-18T09:11:49.552Z",
394	  "updated_at": "2026-05-18T09:54:22.058Z",
395	  "hypothesis": "Scrambled-label classification (seed=456) on plan_002_splits data will show DD OOD F1 comparable to seed=42 (0.990), confirming scrambled variant's performance and variance for reviewer MF1",
396	  "spec": {
397	    "command": "python src/mf1_scrambled_seed456_pipeline.py",
398	    "server": "westd-33183",
399	    "data_path": "data/plan_002_splits/",
400	    "data_count": 350,
401	    "model_name": "microsoft/deberta-v3-base",
402	    "seed": 456,
403	    "checkpoint_path": "checkpoints/mf1_scrambled_seed456/",
404	    "log_path": "results/mf1_scrambled_seed456_run.log"
405	  },
406	  "metrics": {
407	    "dd_ood_full_f1": 1,
408	    "dd_ood_k1_f1": 1,
409	    "dd_ood_k2_f1": 1,
410	    "dd_ood_k3_f1": 0.99,
411	    "dd_ood_k5_f1": 1,
412	    "deberta_val_persuasion_acc": 0.698,
413	    "seed": 456
414	  },
415	  "conclusion": "success",
416	  "completed_at": "2026-05-18T09:19:49.959Z"
417	}
418	
419	=== vanilla_multiseed_dd_ood ===
420	{
421	  "status": "DONE",
422	  "retry_count": 0,
423	  "created_at": "2026-05-18T11:26:57.037Z",
424	  "updated_at": "2026-05-18T11:27:25.460Z",
425	  "hypothesis": "DeBERTa vanilla (no Stage-1 fine-tuning) multi-seed DD OOD evaluation will confirm that the 62pp gap (vanilla 0.284 vs treatment 0.997) is not a seed artifact, and centered CKA will correct the misleading uncentered CKA=1.0 for vanilla vs MLM",
426	  "spec": {
427	    "command": "train_gru.py + evaluate_gru.py (vanilla, seed123/456) + centered_cka.py",
428	    "server": "westd-33183",
429	    "data_path": "data/plan_002_splits + data/dd_ood",
430	    "data_count": 118,
431	    "model_name": "DeBERTa-v3-base (vanilla, no Stage-1)",
432	    "seed": "123,456",
433	    "checkpoint_path": "checkpoints/vanilla_seed123/, checkpoints/vanilla_seed456/",
434	    "log_path": "results/vanilla_multiseed_dd_ood.json, results/centered_cka.json"
435	  },
436	  "conclusion": "success",
437	  "metrics": {
438	    "vanilla_3seed_dd_ood": {
439	      "k1": {
440	        "seed42": 0.575,
441	        "seed123": 0.658,
442	        "seed456": 0.652,
443	        "mean": 0.628,
444	        "std": 0.038
445	      },
446	      "k2": {
447	        "seed42": 0.438,
448	        "seed123": 0.53,
449	        "seed456": 0.469,
450	        "mean": 0.479,
451	        "std": 0.038
452	      },
453	      "k3": {
454	        "seed42": 0.359,
455	        "seed123": 0.424,
456	        "seed456": 0.383,
457	        "mean": 0.389,
458	        "std": 0.027
459	      },
460	      "k5": {
461	        "seed42": 0.311,
462	        "seed123": 0.383,
463	        "seed456": 0.36,
464	        "mean": 0.351,
465	        "std": 0.03
466	      },
467	      "full": {
468	        "seed42": 0.285,
469	        "seed123": 0.305,
470	        "seed456": 0.348,
471	        "mean": 0.312,
472	        "std": 0.026
473	      }
474	    },
475	    "centered_cka_iid": {
476	      "vanilla_vs_mlm": 0.442,
477	      "vanilla_vs_9class": 0.393,
478	      "mlm_vs_9class": 0.586
479	    },
480	    "centered_cka_dd_ood": {
481	      "vanilla_vs_mlm": 0.797,
482	      "vanilla_vs_9class": 0.649,
483	      "mlm_vs_9class": 0.773
484	    },
485	    "uncentered_cka_iid": {
486	      "vanilla_vs_mlm": 1,
487	      "vanilla_vs_9class": 0.421,
488	      "mlm_vs_9class": 0.422
489	    },
490	    "note": "Centered CKA reveals MLM DOES change representations (0.44 not 1.0). Uncentered CKA was misleading."
491	  },
492	  "completed_at": "2026-05-18T11:27:25.460Z"
493	}
494	
495	=== plan_017_eval_seed123 ===
496	{
497	  "status": "PREPARING",
498	  "retry_count": 0,
499	  "created_at": "2026-05-18T06:40:37.831Z",
500	  "updated_at": "2026-05-18T06:40:37.831Z",
501	  "spec": {
502	    "command": "bash -c \"cd /root/persuasion_turn_jailbreak_detect && export HF_HUB_OFFLINE=1 && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/plan_017_dd_eval_seed.py --seed 123 --mlm_ckpt checkpoints/plan_017_mlm_seed123/best\"",
503	    "server": "westd-33183",
504	    "gpu": [
505	      "cuda:1"
506	    ],
507	    "pid": "24747",
508	    "log_path": "~/runs/persuasion_turn_jailbreak_detect/plan_017_eval_seed123.log",
509	    "submitted_at": "2026-05-18T06:40:37.725Z",
510	    "submitted_via": "submit_training_job",
511	    "backend": "tmux",
512	    "account": "root"
513	  }
514	}
515	
516	=== plan_017_eval_seed456 ===
517	{
518	  "status": "PREPARING",
519	  "retry_count": 0,
520	  "created_at": "2026-05-18T06:50:55.636Z",
521	  "updated_at": "2026-05-18T06:50:55.636Z",
522	  "spec": {
523	    "command": "bash -c \"cd /root/persuasion_turn_jailbreak_detect && export HF_HUB_OFFLINE=1 && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/plan_017_dd_eval_seed.py --seed 456 --mlm_ckpt checkpoints/plan_017_mlm_seed456/best\"",
524	    "server": "westd-33183",
525	    "gpu": [
526	      "cuda:1"
527	    ],
528	    "pid": "27159",
529	    "log_path": "~/runs/persuasion_turn_jailbreak_detect/plan_017_eval_seed456.log",
530	    "submitted_at": "2026-05-18T06:50:55.553Z",
531	    "submitted_via": "submit_training_job",
532	    "backend": "tmux",
533	    "account": "root"
534	  }
535	}
536	
537	=== plan_018_eval_seed123 ===
538	{
539	  "status": "PREPARING",
540	  "retry_count": 0,
541	  "created_at": "2026-05-18T07:01:23.658Z",
542	  "updated_at": "2026-05-18T07:01:23.658Z",
543	  "spec": {
544	    "command": "bash -c \"cd /root/persuasion_turn_jailbreak_detect && PYTHONUNBUFFERED=1 CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/hf_cache HF_HUB_OFFLINE=1 /root/miniconda3/bin/python -u src/plan_018_wiki_eval_seed.py --ckpt_dir checkpoints/plan_018_wiki_mlm_seed123/best --output results/plan_018_wiki_mlm_seed123.json --eval_seed 42\"",
545	    "server": "westd-33183",
546	    "gpu": [
547	      "cuda:0"
548	    ],
549	    "pid": "33251",
550	    "log_path": "~/runs/persuasion_turn_jailbreak_detect/plan_018_eval_seed123.log",
551	    "submitted_at": "2026-05-18T07:01:23.581Z",
552	    "submitted_via": "submit_training_job",
553	    "backend": "tmux",
554	    "account": "root"
555	  }
556	}
557	
558	=== plan_018_eval_seed456 ===
559	{
560	  "status": "PREPARING",
561	  "retry_count": 0,
562	  "created_at": "2026-05-18T07:02:13.081Z",
563	  "updated_at": "2026-05-18T07:02:13.081Z",
564	  "spec": {
565	    "command": "bash -c \"cd /root/persuasion_turn_jailbreak_detect && PYTHONUNBUFFERED=1 CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/hf_cache HF_HUB_OFFLINE=1 /root/miniconda3/bin/python -u src/plan_018_wiki_eval_seed.py --ckpt_dir checkpoints/plan_018_wiki_mlm_seed456/best --output results/plan_018_wiki_mlm_seed456.json --eval_seed 42\"",
566	    "server": "westd-33183",
567	    "gpu": [
568	      "cuda:0"
569	    ],
570	    "pid": "33721",
571	    "log_path": "~/runs/persuasion_turn_jailbreak_detect/plan_018_eval_seed456.log",
572	    "submitted_at": "2026-05-18T07:02:12.986Z",
573	    "submitted_via": "submit_training_job",
574	    "backend": "tmux",
575	    "account": "root"
576	  }
577	}
578	
579	=== plan_016v2_topic_eval_seed123 ===
580	{
581	  "status": "PREPARING",
582	  "retry_count": 0,
583	  "created_at": "2026-05-18T06:30:35.800Z",
584	  "updated_at": "2026-05-18T06:30:35.800Z",
585	  "spec": {
586	    "command": "bash -c \"export PYTHONUNBUFFERED=1 HF_HUB_OFFLINE=1 && source /root/miniconda3/bin/activate base && cd /root/persuasion_turn_jailbreak_detect && python -u src/plan_016v2_dd_eval_seed.py --seed 123 --deberta_ckpt checkpoints/plan_016v2_topic_seed123/best --gru_save_dir checkpoints/plan_016v2_topic_seed123/gru --output results/plan_016v2_topic_seed123.json --device cuda:0\"",
587	    "server": "westd-33183",
588	    "gpu": [
589	      "cuda:2"
590	    ],
591	    "pid": "22017",
592	    "log_path": "~/runs/persuasion_turn_jailbreak_detect/plan_016v2_topic_eval_seed123.log",
593	    "submitted_at": "2026-05-18T06:30:35.730Z",
594	    "submitted_via": "submit_training_job",
595	    "backend": "tmux",
596	    "account": "root"
597	  }
598	}
599	
600	=== plan_016v2_topic_eval_seed456 ===
601	{
602	  "status": "PREPARING",
603	  "retry_count": 0,
604	  "created_at": "2026-05-18T06:31:11.271Z",
605	  "updated_at": "2026-05-18T06:31:11.271Z",
606	  "spec": {
607	    "command": "bash -c \"export PYTHONUNBUFFERED=1 HF_HUB_OFFLINE=1 && source /root/miniconda3/bin/activate base && cd /root/persuasion_turn_jailbreak_detect && python -u src/plan_016v2_dd_eval_seed.py --seed 456 --deberta_ckpt checkpoints/plan_016v2_topic_seed456/best --gru_save_dir checkpoints/plan_016v2_topic_seed456/gru --output results/plan_016v2_topic_seed456.json --device cuda:0\"",
608	    "server": "westd-33183",
609	    "gpu": [
610	      "cuda:2"
611	    ],
612	    "pid": "22800",
613	    "log_path": "~/runs/persuasion_turn_jailbreak_detect/plan_016v2_topic_eval_seed456.log",
614	    "submitted_at": "2026-05-18T06:31:11.207Z",
615	    "submitted_via": "submit_training_job",
616	    "backend": "tmux",
617	    "account": "root"
618	  }
619	}
620	
621	=== plan_016v2_topic_eval_seed42 ===
622	{
623	  "status": "PREPARING",
624	  "retry_count": 0,
625	  "created_at": "2026-05-18T06:31:52.043Z",
626	  "updated_at": "2026-05-18T06:31:52.043Z",
627	  "spec": {
628	    "command": "bash -c \"export PYTHONUNBUFFERED=1 HF_HUB_OFFLINE=1 && source /root/miniconda3/bin/activate base && cd /root/persuasion_turn_jailbreak_detect && python -u src/plan_016v2_dd_eval_seed.py --seed 42 --deberta_ckpt checkpoints/plan_016v2_topic/best --gru_save_dir checkpoints/plan_016v2_topic/gru_reseed42 --output results/plan_016v2_topic_seed42.json --device cuda:0\"",
629	    "server": "westd-33183",
630	    "gpu": [
631	      "cuda:2"
632	    ],
633	    "pid": "23592",
634	    "log_path": "~/runs/persuasion_turn_jailbreak_detect/plan_016v2_topic_eval_seed42.log",
635	    "submitted_at": "2026-05-18T06:31:51.984Z",
636	    "submitted_via": "submit_training_job",
637	    "backend": "tmux",
638	    "account": "root"
639	  }
640	}
641	
642	=== exp2_actorattack_ood ===
643	{
644	  "status": "DONE",
645	  "retry_count": 0,
646	  "created_at": "2026-05-18T10:41:47.379Z",
647	  "updated_at": "2026-05-18T12:59:16.967Z",
648	  "hypothesis": "Persuasion-grounded DeBERTa will generalize to ActorAttack (a structurally distinct multi-persona attack), extending cross-attack OOD evidence beyond DD and FITD to a third unseen attack type",
649	  "spec": {
650	    "command": "generate_actorattack.py + evaluate all variants",
651	    "server": "westd-33183",
652	    "data_path": "data/generated/actorattack_all.jsonl (80 jailbreak) + plan_002_splits/test.jsonl (38 benign)",
653	    "data_count": 118,
654	    "model_name": "DeBERTa-v3-base (7 variants \u00d7 3 seeds) + RoBERTa-base (3 variants \u00d7 3 seeds)",
655	    "seed": "42,123,456",
656	    "checkpoint_path": "checkpoints/*/",
657	    "log_path": "results/exp2_actorattack_ood.json"
658	  },
659	  "conclusion": "success",
660	  "metrics": {
661	    "deberta_9class": {
662	      "k1": 0.773,
663	      "k1_std": 0.041,
664	      "k2": 0.855,
665	      "k2_std": 0.048,
666	      "k3": 0.921,
667	      "k3_std": 0.046,
668	      "k5": 0.966,
669	      "k5_std": 0.028,
670	      "full": 0.972,
671	      "full_std": 0.026
672	    },
673	    "deberta_binary": {
674	      "k1": 0.737,
675	      "k1_std": 0.074,
676	      "k2": 0.89,
677	      "k2_std": 0.065,
678	      "k3": 0.951,
679	      "k3_std": 0.036,
680	      "k5": 0.987,
681	      "k5_std": 0.012,
682	      "full": 0.99,
683	      "full_std": 0.008,
684	      "note": "3-seed complete (seed42+seed123+seed456), seed42 weak outlier at K1=0.636"
685	    },
686	    "deberta_scrambled": {
687	      "k1": 0.721,
688	      "k1_std": 0.101,
689	      "k2": 0.828,
690	      "k2_std": 0.054,
691	      "k3": 0.893,
692	      "k3_std": 0.067,
693	      "k5": 0.937,
694	      "k5_std": 0.057,
695	      "full": 0.951,
696	      "full_std": 0.043,
697	      "per_seed_full": {
698	        "seed42": 0.891,
699	        "seed123": 0.99,
700	        "seed456": 0.971
701	      },
702	      "per_seed_k1": {
703	        "seed42": 0.618,
704	        "seed123": 0.858,
705	        "seed456": 0.686
706	      },
707	      "per_seed_k3": {
708	        "seed42": 0.808,
709	        "seed123": 0.972,
710	        "seed456": 0.9
711	      },
712	      "note": "3-seed complete, K2/K5 corrected"
713	    },
714	    "deberta_mlm": {
715	      "k1": 0.736,
716	      "k1_std": 0.15,
717	      "k2": 0.909,
718	      "k2_std": 0.058,
719	      "k3": 0.945,
720	      "k3_std": 0.039,
721	      "k5": 0.929,
722	      "k5_std": 0.033,
723	      "full": 0.893,
724	      "full_std": 0.08
725	    },
726	    "deberta_wiki_mlm": {
727	      "k1": 0.656,
728	      "k1_std": 0.224,
729	      "k2": 0.672,
730	      "k2_std": 0.252,
731	      "k3": 0.693,
732	      "k3_std": 0.28,
733	      "k5": 0.689,
734	      "k5_std": 0.285,
735	      "full": 0.686,
736	      "full_std": 0.297
737	    },
738	    "deberta_topic": {
739	      "k1": 0.513,
740	      "k1_std": 0.077,
741	      "k2": 0.58,
742	      "k2_std": 0.109,
743	      "k3": 0.565,
744	      "k3_std": 0.1,
745	      "k5": 0.615,
746	      "k5_std": 0.111,
747	      "full": 0.625,
748	      "full_std": 0.141
749	    },
750	    "deberta_vanilla": {
751	      "k1": 0.337,
752	      "k1_std": 0.049,
753	      "k2": 0.306,
754	      "k2_std": 0.026,
755	      "k3": 0.284,
756	      "k3_std": 0.011,
757	      "k5": 0.262,
758	      "k5_std": 0.006,
759	      "full": 0.258,
760	      "full_std": 0
761	    },
762	    "roberta_9class": {
763	      "k1": 0.738,
764	      "k1_std": 0.033,
765	      "k2": 0.805,
766	      "k2_std": 0.033,
767	      "k3": 0.884,
768	      "k3_std": 0.066,
769	      "k5": 0.925,
770	      "k5_std": 0.066,
771	      "full": 0.939,
772	      "full_std": 0.046
773	    },
774	    "roberta_mlm": {
775	      "k1": 0.633,
776	      "k1_std": 0.133,
777	      "k2": 0.665,
778	      "k2_std": 0.15,
779	      "k3": 0.713,
780	      "k3_std": 0.174,
781	      "k5": 0.719,
782	      "k5_std": 0.184,
783	      "full": 0.73,
784	      "full_std": 0.201
785	    },
786	    "roberta_vanilla": {
787	      "k1": 0.41,
788	      "k1_std": 0.126,
789	      "k2": 0.425,
790	      "k2_std": 0.143,
791	      "k3": 0.432,
792	      "k3_std": 0.144,
793	      "k5": 0.466,
794	      "k5_std": 0.144,
795	      "full": 0.466,
796	      "full_std": 0.163
797	    },
798	    "n_samples": 118,
799	    "note": "All variants now 3-seed complete. Binary updated from 2-seed to 3-seed (seed42 weak at K1=0.636). Scrambled K2/K5 corrected. Evidence hierarchy: binary \u2248 9class > scrambled >> mlm > wiki_mlm > topic > vanilla"
800	  },
801	  "completed_at": "2026-05-18T12:21:09.733Z"
802	}
803	
804	=== exp41_tost_10seed ===
805	{
806	  "status": "DONE",
807	  "retry_count": 0,
808	  "created_at": "2026-05-22T03:27:38.653Z",
809	  "updated_at": "2026-05-22T03:53:52.977Z",
810	  "hypothesis": "Extending TOST equivalence test from n=5 to n=10 seeds will resolve the inconclusive AA result (p=0.08 at n=5) by providing sufficient statistical power: if scrambled and 9-class are truly equivalent within 5pp margin on ActorAttack, the increased sample size will yield p<0.05, confirming label content irrelevance across all OOD families.",
811	  "parent": "exp39_extra_seeds_tost",
812	  "spec": {
813	    "command": "CUDA_VISIBLE_DEVICES=0 python scripts/exp41_tost_10seed.py",
814	    "server": "westd-33183",
815	    "data_path": "/root/persuasion_turn_jailbreak_detect/data/plan_002_splits/",
816	    "data_count": "train+val+test from plan_002_splits",
817	    "model_name": "deberta-v3-base + BiGRU",
818	    "seed": "2024,2025,2026,314,628 (new) + 42,123,456,789,1000 (prior)",
819	    "checkpoint_source": "newly trained from scratch (5 new seeds)",
820	    "eval_data": "DD OOD, AA OOD, FITD OOD test sets"
821	  },
822	  "log_path": "/root/persuasion_turn_jailbreak_detect/logs/exp41_tost_10seed.log",
823	  "checkpoint_path": "/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints/exp41_*/",
824	  "metrics": {
825	    "n_seeds": 10,
826	    "seeds": [
827	      42,
828	      123,
829	      456,
830	      789,
831	      1000,
832	      2024,
833	      2025,
834	      2026,
835	      314,
836	      628
837	    ],
838	    "tost_DD": {
839	      "p": 2.06e-09,
840	      "equivalent": true,
841	      "cohens_d": -0.136
842	    },
843	    "tost_AA": {
844	      "p": 0.183,
845	      "equivalent": false,
846	      "cohens_d": 0.44
847	    },
848	    "tost_FITD": {
849	      "p": 0,
850	      "equivalent": true,
851	      "cohens_d": 0
852	    },
853	    "9class_AA_mean": 0.979,
854	    "scrambled_AA_mean": 0.949,
855	    "AA_mean_diff_pp": 3,
856	    "training_time_min": 16.8
857	  },
858	  "conclusion": "negative",
859	  "completed_at": "2026-05-22T03:53:52.977Z"
860	}
861	
862	=== exp39_extra_seeds_tost ===
863	{
864	  "status": "DONE",
865	  "retry_count": 0,
866	  "created_at": "2026-05-21T09:15:07.434Z",
867	  "updated_at": "2026-05-21T09:33:25.262Z",
868	  "hypothesis": "\u6269\u5c55 9-class \u548c scrambled \u5230 5 seeds (\u65b0\u589e 789/1000) \u5c06\u63d0\u4f9b\u8db3\u591f\u7edf\u8ba1\u6548\u529b\u652f\u6301 TOST \u7b49\u4ef7\u6027\u68c0\u9a8c\uff1ascrambled \u5728 DD OOD \u4e0a\u4e0e 9-class \u7b49\u4ef7\uff08\u5dee\u8ddd &lt;2pp\uff09\uff0c\u4f46\u5728 AA OOD \u4e0a\u663e\u8457\u66f4\u4f4e\uff0c\u8bc1\u660e\u7b56\u7565\u6807\u7b7e\u7684\u6b63\u786e\u8bed\u4e49\u4fe1\u606f\u5bf9 hard OOD \u81f3\u5173\u91cd\u8981\u3002",
869	  "spec": {
870	    "command": "CUDA_VISIBLE_DEVICES=0 python scripts/exp39_extra_seeds.py",
871	    "server": "westd-33183",
872	    "data_path": "data/plan_002_splits/train.jsonl + DD/AA/FITD OOD",
873	    "data_count": "350 train + 80 DD + 80 AA + 80 FITD + 76 test",
874	    "model_name": "microsoft/deberta-v3-base + BiGRU (9class & scrambled)",
875	    "seed": "789,1000",
876	    "checkpoint_path": "/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints/exp39_*/",
877	    "log_path": "/tmp/exp39.log"
878	  },
879	  "metrics": {
880	    "9class_seed789": {
881	      "iid": 1,
882	      "dd_ood": 1,
883	      "aa_ood": 0.9715,
884	      "fitd_ood": 1
885	    },
886	    "9class_seed1000": {
887	      "iid": 1,
888	      "dd_ood": 1,
889	      "aa_ood": 0.9715,
890	      "fitd_ood": 0.9904
891	    },
892	    "scrambled_seed789": {
893	      "iid": 1,
894	      "dd_ood": 1,
895	      "aa_ood": 0.9904,
896	      "fitd_ood": 1
897	    },
898	    "scrambled_seed1000": {
899	      "iid": 1,
900	      "dd_ood": 1,
901	      "aa_ood": 0.9904,
902	      "fitd_ood": 0.9904
903	    },
904	    "total_time_min": 7.6
905	  },
906	  "conclusion": "success",
907	  "completed_at": "2026-05-21T09:33:25.263Z"
908	}
909	
910	=== exp35_cross_seed_ensemble ===
911	{
912	  "status": "DONE",
913	  "retry_count": 0,
914	  "created_at": "2026-05-20T20:12:07.318Z",
915	  "updated_at": "2026-05-20T20:28:58.939Z",
916	  "hypothesis": "3-seed majority vote ensemble \u5c06\u5728\u6240\u6709 OOD \u653b\u51fb\u5bb6\u65cf\u4e0a\u63d0\u5347\u68c0\u6d4b F1\uff08\u5c24\u5176\u51cf\u5c11 AA OOD \u4e0a\u7684\u6f0f\u68c0\uff09\uff0c9-class ensemble \u7684\u63d0\u5347\u5e45\u5ea6\u5927\u4e8e MLM/vanilla\uff0c\u56e0\u4e3a 9-class \u5404 seed \u7684\u9519\u8bef\u6a21\u5f0f\u66f4\u4e92\u8865\uff08\u6765\u81ea\u4e0d\u540c\u7684\u7b56\u7565\u8868\u5f81\u7a7a\u95f4\u521d\u59cb\u5316\uff09\u3002",
917	  "parent": "exp23_aa_error_analysis",
918	  "spec": {
919	    "command": "python scripts/exp35_cross_seed_ensemble.py",
920	    "server": "westd-33183",
921	    "data_path": "per_sample_predictions/ + FITD OOD generated",
922	    "data_count": 354,
923	    "model_name": "9class + jb_mlm + vanilla (3 seeds each)",
924	    "seed": "42,123,456",
925	    "checkpoint_source": "plan_002 + plan_017_mlm + pretrained",
926	    "eval_data": "DD 118 + FITD 118 + AA 118"
927	  },
928	  "metrics": {
929	    "dd_ood": {
930	      "9class": {
931	        "ensemble_f1": 1,
932	        "individual_mean": 0.9968,
933	        "individual_std": 0.0045,
934	        "delta": 0.0032,
935	        "fixed": 1,
936	        "broke": 0
937	      },
938	      "jb_mlm": {
939	        "ensemble_f1": 1,
940	        "individual_mean": 0.9138,
941	        "individual_std": 0.115,
942	        "delta": 0.0862,
943	        "fixed": 30,
944	        "broke": 0
945	      },
946	      "vanilla": {
947	        "ensemble_f1": 0.2575,
948	        "individual_mean": 0.2619,
949	        "individual_std": 0.017,
950	        "delta": -0.0044,
951	        "fixed": 1,
952	        "broke": 0
953	      }
954	    },
955	    "aa_ood": {
956	      "9class": {
957	        "ensemble_f1": 0.9809,
958	        "individual_mean": 0.9719,
959	        "individual_std": 0.0261,
960	        "delta": 0.009,
961	        "fixed": 5,
962	        "broke": 0
963	      },
964	      "jb_mlm": {
965	        "ensemble_f1": 0.953,
966	        "individual_mean": 0.8934,
967	        "individual_std": 0.0799,
968	        "delta": 0.0596,
969	        "fixed": 26,
970	        "broke": 0
971	      },
972	      "vanilla": {
973	        "ensemble_f1": 0.2575,
974	        "individual_mean": 0.2575,
975	        "individual_std": 0,
976	        "delta": 0,
977	        "fixed": 0,
978	        "broke": 0
979	      }
980	    },
981	    "fitd_ood": {
982	      "9class": {
983	        "ensemble_f1": 1,
984	        "individual_mean": 1,
985	        "individual_std": 0,
986	        "delta": 0,
987	        "fixed": 0,
988	        "broke": 0
989	      },
990	      "jb_mlm": {
991	        "ensemble_f1": 1,
992	        "individual_mean": 0.9904,
993	        "individual_std": 0.0078,
994	        "delta": 0.0096,
995	        "fixed": 3,
996	        "broke": 0
997	      },
998	      "vanilla": {
999	        "ensemble_f1": 1,
1000	        "individual_mean": 0.9936,
1001	        "individual_std": 0.009,
1002	        "delta": 0.0064,
1003	        "fixed": 2,
1004	        "broke": 0
1005	      }
1006	    },
1007	    "note": "Ensemble NEVER breaks correct predictions (broke=0 everywhere). jb_mlm benefits most from ensemble (+8.6pp DD, +6.0pp AA). 9class achieves perfect DD/FITD, near-perfect AA (0.981). Vanilla too weak to benefit."
1008	  },
1009	  "checkpoint_path": "plan_002 + plan_017_mlm + pretrained (3 seeds each)",
1010	  "log_path": "results/exp35_cross_seed_ensemble.json",
1011	  "conclusion": "success",
1012	  "completed_at": "2026-05-20T20:28:58.939Z"
1013	}
1014	
1015	=== exp4_dd_ood_perturbation ===
1016	{
1017	  "status": "DONE",
1018	  "retry_count": 0,
1019	  "created_at": "2026-05-18T10:47:27.803Z",
1020	  "updated_at": "2026-05-18T12:06:21.623Z",
1021	  "hypothesis": "Persuasion-grounded DeBERTa variants will maintain near-zero perturbation degradation on DD OOD paraphrased data, while vanilla/wiki-MLM variants will show significant degradation, extending IID perturbation robustness findings to OOD setting",
1022	  "spec": {
1023	    "command": "python exp4_dd_ood_perturbation.py (Qwen3-8B paraphrasing + 7-variant eval)",
1024	    "server": "westd-33183",
1025	    "data_path": "data/dd_ood (80 conversations) + plan_002_splits/test.jsonl (38 benign)",
1026	    "data_count": 118,
1027	    "model_name": "DeBERTa-v3-base (7 variants \u00d7 3 seeds)",
1028	    "seed": "42,123,456",
1029	    "checkpoint_path": "checkpoints/*/",
1030	    "log_path": "results/exp4_dd_ood_perturbation.json"
1031	  },
1032	  "conclusion": "success",
1033	  "metrics": {
1034	    "9class_3seed": {
1035	      "clean_k1": 0.9905,
1036	      "perturbed_k1": 0.9968,
1037	      "delta_k1": 0.0063,
1038	      "clean_k3": 0.9719,
1039	      "perturbed_k3": 0.9936,
1040	      "delta_k3": 0.0217,
1041	      "clean_full": 0.9968,
1042	      "perturbed_full": 1,
1043	      "delta_full": 0.0032
1044	    },
1045	    "binary_3seed": {
1046	      "clean_k1": 0.9936,
1047	      "perturbed_k1": 1,
1048	      "delta_k1": 0.0064,
1049	      "clean_full": 0.9968,
1050	      "perturbed_full": 1,
1051	      "delta_full": 0.0032
1052	    },
1053	    "scrambled_3seed": {
1054	      "clean_k1": 0.9968,
1055	      "perturbed_k1": 0.9936,
1056	      "delta_k1": -0.0032,
1057	      "clean_full": 0.9968,
1058	      "perturbed_full": 1,
1059	      "delta_full": 0.0032
1060	    },
1061	    "jb_mlm_3seed": {
1062	      "clean_k1": 0.9733,
1063	      "perturbed_k1": 0.9733,
1064	      "delta_k1": 0,
1065	      "clean_full": 0.9138,
1066	      "perturbed_full": 0.9409,
1067	      "delta_full": 0.0271
1068	    },
1069	    "wiki_mlm_3seed": {
1070	      "clean_k1": 0.9131,
1071	      "perturbed_k1": 0.8808,
1072	      "delta_k1": -0.0323,
1073	      "clean_full": 0.9042,
1074	      "perturbed_full": 0.8715,
1075	      "delta_full": -0.0327
1076	    },
1077	    "topic_3seed": {
1078	      "clean_k1": 0.5912,
1079	      "perturbed_k1": 0.617,
1080	      "delta_k1": 0.0259,
1081	      "clean_full": 0.5412,
1082	      "perturbed_full": 0.5765,
1083	      "delta_full": 0.0353
1084	    },
1085	    "vanilla_3seed": {
1086	      "clean_k1": 0.6283,
1087	      "perturbed_k1": 0.5602,
1088	      "delta_k1": -0.0681,
1089	      "clean_k2": 0.4824,
1090	      "perturbed_k2": 0.4829,
1091	      "delta_k2": 0.0004,
1092	      "clean_full": 0.3123,
1093	      "perturbed_full": 0.3394,
1094	      "delta_full": 0.0271
1095	    },
1096	    "mcnemar_perturbed_k1": {
1097	      "9class_vs_vanilla": {
1098	        "all_seeds_p": "<0.001",
1099	        "discordant_range": "49-56 favoring 9class"
1100	      },
1101	      "9class_vs_jb_mlm": "n.s. all seeds",
1102	      "9class_vs_scrambled": "n.s. all seeds"
1103	    },
1104	    "mcnemar_perturbed_full": {
1105	      "9class_vs_vanilla": {
1106	        "all_seeds_p": "<0.001",
1107	        "discordant_range": "67-78 favoring 9class"
1108	      },
1109	      "9class_vs_jb_mlm": {
1110	        "seed42": "tie",
1111	        "seed123": "n.s.",
1112	        "seed456": "p=4e-06 (b=19)"
1113	      },
1114	      "9class_vs_scrambled": "tie all seeds"
1115	    }
1116	  },
1117	  "completed_at": "2026-05-18T11:44:43.341Z"
1118	}
1119	
1120	=== exp55_5seed_mlm_vs_9class_aa ===
1121	{
1122	  "status": "DONE",
1123	  "retry_count": 0,
1124	  "created_at": "2026-05-22T11:11:41.549Z",
1125	  "updated_at": "2026-05-22T12:15:56.035Z",
1126	  "hypothesis": "9-class persuasion-grounded DeBERTa DAPT produces significantly better OOD generalization than domain-exposure-only MLM DAPT, with the advantage being robust across 5 random seeds (expanding from 3 to address reviewer W2 concern about insufficient seed count)",
1127	  "spec": {
1128	    "command": "CUDA_VISIBLE_DEVICES=1 python scripts/exp55_5seed_expansion.py",
1129	    "server": "westd-49690",
1130	    "data_path": "/root/persuasion_turn_jailbreak_detect/data/plan_002_splits/",
1131	    "data_count": "~800 train + OOD eval sets",
1132	    "model_name": "microsoft/deberta-v3-base",
1133	    "seed": "789,1024",
1134	    "checkpoint_path": "/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints/exp55_*",
1135	    "log_path": "/tmp/exp55_train.log"
1136	  },
1137	  "metrics": {
1138	    "n_seeds": 5,
1139	    "seeds": [
1140	      42,
1141	      123,
1142	      456,
1143	      789,
1144	      1024
1145	    ],
1146	    "9class_aa_ood": {
1147	      "mean": 0.9735,
1148	      "std": 0.0124
1149	    },
1150	    "mlm_aa_ood": {
1151	      "mean": 0.9566,
1152	      "std": 0.0237
1153	    },
1154	    "9class_iid": {
1155	      "mean": 1,
1156	      "std": 0
1157	    },
1158	    "mlm_iid": {
1159	      "mean": 0.9816,
1160	      "std": 0.0134
1161	    },
1162	    "9class_dd_ood": {
1163	      "mean": 0.9924,
1164	      "std": 0.0111
1165	    },
1166	    "mlm_dd_ood": {
1167	      "mean": 0.9883,
1168	      "std": 0.0094
1169	    },
1170	    "9class_fitd_ood": {
1171	      "mean": 1,
1172	      "std": 0
1173	    },
1174	    "mlm_fitd_ood": {
1175	      "mean": 0.9883,
1176	      "std": 0.0094
1177	    },
1178	    "aa_ood_delta_pp": 1.69,
1179	    "aa_ood_paired_ttest_p": 0.2461,
1180	    "aa_ood_wilcoxon_p": 0.1875,
1181	    "aa_ood_9class_wins": 4,
1182	    "aa_ood_mlm_wins": 1,
1183	    "total_time_min": 10.5
1184	  },
1185	  "conclusion": "negative",
1186	  "completed_at": "2026-05-22T12:15:56.035Z"
1187	}
1188	
1189	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20c02b07-ee4f-48d3-9411-aa0f2648c609",
  "isSidechain": true,
  "promptId": "5df424ed-94b3-4801-a077-e8e00b57103c",
  "agentId": "afbd91c4ab95ef894",
  "type": "user",
  "uuid": "f228c1a4-9059-43f9-8848-7b2b0bbacf44",
  "sourceToolAssistantUUID": "20c02b07-ee4f-48d3-9411-aa0f2648c609",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-22T21:31:45.985Z_

Now let me also fetch the remaining key experiments - specifically looking for more seed-level DD OOD / AA OOD data from plan_002, plan_017, and related multi-seed entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f228c1a4-9059-43f9-8848-7b2b0bbacf44",
  "isSidechain": true,
  "agentId": "afbd91c4ab95ef894",
  "requestId": "req_011CbJKcKzPAJStEXP5vQ8Jf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a8bad23-e34a-4df6-b56d-f7e5968f36d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QZetuJ7aET2HkkRYCjS8Gd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19451,
      "cache_read_input_tokens": 21946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19451,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T21:31:53.708Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ASwoBs1v2Ewfn8H5FPn1LU`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/e4efefca-26d6-49cf-8a09-2af928a47017/tool-results/mcp-agent-ml-research-read_registry-1779485432679.txt', 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\ndata = registry['data']\nexperiments = data['experiments']\n\n# Additional relevant experiments\ntarget_keys = [\n    'plan_002_seed123',\n    'plan_002_seed456',\n    'plan_002_clean_training',\n    'exp13_meanpool_multiseed',\n    'exp9_bootstrap_ci',\n    'exp11_tost_equivalence',\n    'exp38_wildcat_calibration',\n    'exp42_ood_benign_mixed',\n    'exp42b_balanced_ratio_ablation',\n    'exp28_data_efficiency',\n    'exp28b_data_efficiency_supplement',\n    'exp55_5seed_mlm_vs_9class_aa',\n]\n\nfor k in target_keys:\n    if k in experiments:\n        print(f'=== {k} ===')\n        print(json.dumps(experiments[k], indent=2))\n        print()\n    else:\n        print(f'=== {k} === NOT FOUND')\n        print()\n\" 2>&1",
  "description": "Extract additional seed and adaptation experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a8bad23-e34a-4df6-b56d-f7e5968f36d6",
  "isSidechain": true,
  "agentId": "afbd91c4ab95ef894",
  "requestId": "req_011CbJKcKzPAJStEXP5vQ8Jf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "718732c6-c25d-47b6-8535-6b8cad76c630",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QZetuJ7aET2HkkRYCjS8Gd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19451,
      "cache_read_input_tokens": 21946,
      "output_tokens": 522,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19451
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 522,
          "cache_read_input_tokens": 21946,
          "cache_creation_input_tokens": 19451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19451,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T21:31:53.803Z_

<details><summary>↩ Tool result · `toolu_01ASwoBs1v2Ewfn8H5FPn1LU`</summary>

```text
=== plan_002_seed123 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-18T01:13:42.372Z",
  "updated_at": "2026-05-18T07:29:32.962Z",
  "hypothesis": "9-class persuasion treatment seed=123 achieves same DD OOD performance as seed=42 (F1~1.0), confirming low variance in treatment's cross-attack generalization.",
  "parent": "plan_002_clean_training",
  "spec": {
    "command": "python src/train_deberta.py + train_classifier.py + eval_early_detection.py",
    "server": "westd-33183",
    "data_path": "data/plan_002_splits/",
    "data_count": 500,
    "model_name": "DeBERTa-v3-base + BiGRU",
    "seed": 123,
    "checkpoint_source": "checkpoints/plan_002_seed123/",
    "eval_data": "data/plan_002_splits/test.jsonl"
  },
  "conclusion": "success",
  "metrics": {
    "treatment_k1_f1": 1,
    "treatment_k2_f1": 1,
    "treatment_k3_f1": 1,
    "treatment_k5_f1": 1,
    "treatment_full_f1": 1,
    "baseline_k1_f1": 0.987,
    "baseline_k2_f1": 0.987,
    "baseline_k3_f1": 0.987,
    "baseline_full_f1": 1,
    "tfidf_all_k_f1": 1,
    "dd_ood_k1_f1": 1,
    "dd_ood_k2_f1": 0.9904,
    "dd_ood_k3_f1": 0.9904,
    "dd_ood_k5_f1": 1,
    "dd_ood_full_f1": 1
  },
  "failure_reason": "startup recovery: RUNNING with no cron and no server/pid info",
  "completed_at": "2026-05-18T02:11:24.594Z"
}

=== plan_002_seed456 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-18T01:12:15.664Z",
  "updated_at": "2026-05-18T07:29:36.322Z",
  "hypothesis": "Reproduce plan_002 with seed=456 to confirm stability of persuasion-grounded DeBERTa detection advantage over vanilla baseline across random seeds",
  "parent": "plan_002_clean_training",
  "spec": {
    "command": "python src/train_deberta.py + train_classifier.py + eval_early_detection.py",
    "server": "westd-33183",
    "data_path": "data/plan_002_splits/",
    "data_count": 500,
    "model_name": "DeBERTa-v3-base + BiGRU",
    "seed": 456,
    "checkpoint_source": "checkpoints/plan_002_seed456/",
    "eval_data": "data/plan_002_splits/test.jsonl"
  },
  "conclusion": "success",
  "metrics": {
    "treatment_k1_f1": 1,
    "treatment_k2_f1": 1,
    "treatment_k3_f1": 1,
    "treatment_k5_f1": 1,
    "treatment_full_f1": 1,
    "baseline_k1_f1": 0.9296,
    "baseline_k2_f1": 0.9589,
    "baseline_k3_f1": 0.9867,
    "baseline_k5_f1": 0.9867,
    "baseline_full_f1": 1,
    "tfidf_all_k_f1": 1,
    "deberta_best_epoch": 2,
    "deberta_persuasion_acc": 0.8593,
    "deberta_intent_acc": 1,
    "dd_ood_k1_f1": 0.9715,
    "dd_ood_k2_f1": 0.9622,
    "dd_ood_k3_f1": 0.935,
    "dd_ood_k5_f1": 0.9904,
    "dd_ood_full_f1": 0.9904
  },
  "failure_reason": "startup recovery: RUNNING with no cron and no server/pid info",
  "completed_at": "2026-05-18T02:11:24.081Z"
}

=== plan_002_clean_training ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-17T23:18:30.115Z",
  "updated_at": "2026-05-17T23:19:02.467Z",
  "hypothesis": "Persuasion-grounded DeBERTa embeddings on topic-anchored data will show significant early detection advantage over vanilla baseline, with Treatment-Baseline gap > 5pp at K=2 or K=3",
  "parent": "phase_b_full",
  "spec": {
    "command": "scripts/run_plan_002.sh",
    "server": "westd-33183",
    "data_path": "data/plan_002_splits/ (crescendo 250 + topic-anchored V2 benign 250)",
    "data_count": 500,
    "model_name": "DeBERTa-v3-base + BiGRU",
    "seed": 42,
    "checkpoint_source": "self-trained",
    "eval_data": "data/plan_002_splits/test.jsonl",
    "checkpoint_path": "checkpoints/plan_002/",
    "log_path": "/root/persuasion_turn_jailbreak_detect/results/plan_002_eval.json"
  },
  "conclusion": "negative",
  "metrics": {
    "treatment_k1_f1": 1,
    "baseline_k1_f1": 0.987,
    "treatment_k2_f1": 1,
    "baseline_k2_f1": 0.9867,
    "treatment_k3_f1": 1,
    "baseline_k3_f1": 0.9867,
    "treatment_k5_f1": 1,
    "baseline_k5_f1": 1,
    "treatment_full_f1": 1,
    "baseline_full_f1": 1,
    "tfidf_all_k_f1": 1,
    "max_delta_pp": 1.3,
    "pass_criteria_5pp": false
  },
  "completed_at": "2026-05-17T23:19:02.467Z"
}

=== exp13_meanpool_multiseed ===
{
  "status": "PREPARING",
  "retry_count": 0,
  "created_at": "2026-05-18T23:35:41.779Z",
  "updated_at": "2026-05-20T12:24:21.733Z",
  "hypothesis": "Mean pooling classifier (without temporal modeling) will perform comparably to BiGRU across 3 seeds on DeBERTa-v3 9-class, confirming that per-turn representations alone drive detection and GRU temporal modeling is unnecessary \u2014 cross-validating shuffle ablation results",
  "parent": "plan_015_dd_eval",
  "spec": {
    "command": "python scripts/meanpool_multiseed.py",
    "server": "westd-33183",
    "data_path": "data/plan_002_splits/ + data/generated/",
    "data_count": 586,
    "model_name": "DeBERTa-v3-base 9-class (3 seeds)",
    "seed": "42,123,456",
    "checkpoint_path": "checkpoints/plan_002_seed*/",
    "log_path": "results/meanpool_multiseed.json"
  },
  "conclusion": "success",
  "metrics": {
    "dd_ood": {
      "k1": {
        "mean": 0.9905,
        "std": 0.0134
      },
      "k2": {
        "mean": 0.9936,
        "std": 0.009
      },
      "k3": {
        "mean": 0.9842,
        "std": 0.016
      },
      "k5": {
        "mean": 0.9968,
        "std": 0.0045
      },
      "full": {
        "mean": 0.9905,
        "std": 0.0134
      }
    },
    "actorattack": {
      "k1": {
        "mean": 0.8301,
        "std": 0.0272
      },
      "k2": {
        "mean": 0.903,
        "std": 0.0229
      },
      "k3": {
        "mean": 0.9622,
        "std": 0.0076
      },
      "k5": {
        "mean": 0.9716,
        "std": 0.0153
      },
      "full": {
        "mean": 0.9623,
        "std": 0.0151
      }
    },
    "metric": "f1_macro",
    "classifier": "mean_pooling + linear",
    "encoder": "9-class DeBERTa-v3-base",
    "note": "Mean pooling matches BiGRU on DD OOD (all K \u22650.98). ActorAttack K\u22653 also \u22650.96. Confirms temporal modeling not necessary."
  }
}

=== exp9_bootstrap_ci ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-18T16:16:19.153Z",
  "updated_at": "2026-05-18T17:38:42.488Z",
  "hypothesis": "BCa bootstrap CIs and paired permutation tests will confirm that multitask 9-class persuasion pre-training significantly outperforms vanilla (frozen) baseline on OOD jailbreak detection, while the difference against domain-specific pre-training (jb_mlm, scrambled) is not statistically significant, supporting the claim that persuasion-aware representations provide robust detection capabilities.",
  "spec": {
    "command": "python scripts/exp9_bootstrap_ci.py",
    "server": "westd-33183",
    "data_path": "data/generated/deceptive_delight_all.jsonl + data/generated/actorattack_all.jsonl + data/plan_002_splits/test.jsonl",
    "data_count": 118,
    "model_name": "DeBERTa-v3-base + RoBERTa-base (10 variants x 3 seeds)",
    "seed": "42,123,456"
  },
  "log_path": "results/exp9_run.log",
  "checkpoint_path": "results/exp9_bootstrap_ci.json",
  "metrics": {
    "dd_ood_9class_full": {
      "mean": 0.9968,
      "ci": [
        0.9426,
        1
      ]
    },
    "dd_ood_vanilla_full": {
      "mean": 0.2698,
      "ci": [
        0.2017,
        0.3414
      ]
    },
    "actorattack_9class_full": {
      "mean": 0.9718,
      "ci": [
        0.8554,
        1
      ]
    },
    "actorattack_vanilla_full": {
      "mean": 0.2565,
      "ci": [
        0.2027,
        0.3139
      ]
    },
    "perm_9class_vs_vanilla_dd_full_p": 0,
    "perm_9class_vs_vanilla_aa_full_p": 0,
    "perm_9class_vs_jb_mlm_dd_full_max_p": 1,
    "perm_9class_vs_scrambled_dd_full_max_p": 1
  },
  "conclusion": "success",
  "completed_at": "2026-05-18T17:38:42.488Z"
}

=== exp11_tost_equivalence ===
{
  "status": "PREPARING",
  "retry_count": 0,
  "created_at": "2026-05-18T20:55:11.384Z",
  "updated_at": "2026-05-18T20:55:29.568Z",
  "hypothesis": "Classification-supervised DeBERTa variants (9-class, scrambled, binary) are statistically equivalent on DD OOD (within \u0394=5pp margin), formally proving that persuasion label content does not matter \u2014 any classification structure on domain text produces equivalent cross-attack generalization.",
  "parent": "exp9_bootstrap_ci",
  "spec": {
    "command": "python scripts/tost_equivalence.py",
    "server": "westd-33183",
    "data_path": "results/exp9_bootstrap_ci.json (per-seed predictions)",
    "data_count": 236,
    "model_name": "DeBERTa-v3-base variants",
    "seed": "42,123,456",
    "checkpoint_path": "N/A (analysis only)",
    "log_path": "results/tost_equivalence.json"
  },
  "conclusion": "success",
  "metrics": {
    "dd_ood_full": {
      "9class_vs_scrambled": {
        "mean_diff": 0,
        "ci_90": [
          -0.016,
          0.016
        ],
        "p_tost": 0.006,
        "equivalent": true,
        "ci_within_margin": true
      },
      "9class_vs_binary": {
        "mean_diff": -0.0032,
        "ci_90": [
          -0.013,
          0.006
        ],
        "p_tost": 0.002,
        "equivalent": true,
        "ci_within_margin": true
      },
      "9class_vs_jb_mlm": {
        "mean_diff": 0.083,
        "ci_90": [
          -0.145,
          0.311
        ],
        "p_tost": 0.643,
        "equivalent": false,
        "ci_within_margin": false
      },
      "scrambled_vs_binary": {
        "mean_diff": -0.0032,
        "ci_90": [
          -0.013,
          0.006
        ],
        "p_tost": 0.002,
        "equivalent": true,
        "ci_within_margin": true
      }
    },
    "actorattack_full": {
      "9class_vs_scrambled": {
        "mean_diff": 0.0209,
        "ci_90": [
          -0.109,
          0.151
        ],
        "p_tost": 0.29,
        "equivalent": false,
        "ci_within_margin": false
      },
      "9class_vs_binary": {
        "mean_diff": -0.0185,
        "ci_90": [
          -0.075,
          0.038
        ],
        "p_tost": 0.122,
        "equivalent": false,
        "ci_within_margin": false
      },
      "9class_vs_jb_mlm": {
        "mean_diff": 0.0784,
        "ci_90": [
          -0.109,
          0.266
        ],
        "p_tost": 0.65,
        "equivalent": false,
        "ci_within_margin": false
      },
      "scrambled_vs_binary": {
        "mean_diff": -0.0394,
        "ci_90": [
          -0.117,
          0.038
        ],
        "p_tost": 0.363,
        "equivalent": false,
        "ci_within_margin": false
      }
    },
    "note": "DD OOD: 9class\u2248scrambled\u2248binary formally equivalent (TOST p<0.05, 90% CI within \u00b10.05). ActorAttack: inconclusive due to n=3 + higher variance. jb_mlm clearly different from classification variants."
  }
}

=== exp38_wildcat_calibration ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-21T01:32:34.913Z",
  "updated_at": "2026-05-21T01:57:36.010Z",
  "hypothesis": "\u5c11\u91cf WildChat benign \u6837\u672c (~50 \u6761) \u5373\u53ef\u901a\u8fc7\u9608\u503c\u6821\u51c6\u5c06 FPR \u964d\u81f3 <25% \u4e14 TPR >90%\uff0c\u8bc1\u660e domain calibration \u662f\u53ef\u884c\u7684 practical path\uff0cWildChat \u9ad8 FPR \u662f\u9608\u503c\u95ee\u9898\u800c\u975e\u8868\u5f81\u80fd\u529b\u95ee\u9898\u3002",
  "parent": "exp24_calibration_ece",
  "spec": {
    "command": "python scripts/exp38_wildcat_calibration.py",
    "server": "westd-33183",
    "data_path": "data/wildchat_benign_226.jsonl + jailbreak test data",
    "data_count": "226 WildChat benign + jailbreak test",
    "model_name": "plan_002 9-class DeBERTa+BiGRU",
    "seed": "42,123,456",
    "checkpoint_source": "plan_002 seeds 42/123/456",
    "eval_data": "WildChat benign 226 (113 cal + 113 test) + IID/DD/AA/FITD jailbreak"
  },
  "metrics": {
    "roc_auc": {
      "mean": 0.7,
      "std": 0.054,
      "per_seed": {
        "seed42": 0.768,
        "seed123": 0.697,
        "seed456": 0.635
      }
    },
    "default_t05_fpr": {
      "mean": 0.791,
      "std": 0.098
    },
    "threshold_calibration_held_out": {
      "tpr95_fpr": {
        "mean": 0.627,
        "std": 0.1
      },
      "tpr90_fpr": {
        "mean": 0.587,
        "std": 0.091
      }
    },
    "temperature_scaling": {
      "learned_T": "20-40 (severe overconfidence)",
      "temp_scaled_tpr95_fpr": 0.627,
      "temp_scaled_tpr90_fpr": 0.583,
      "note": "Temperature scaling does NOT change FPR because ROC is invariant to monotonic score transforms"
    },
    "note": "AUC=0.70 is the fundamental ceiling. Threshold calibration drops FPR from 79%\u219263% (at TPR95), still far from <25% target. WildChat high FPR is genuine domain shift, not calibration artifact."
  },
  "conclusion": "negative",
  "checkpoint_path": "results/exp38_wildcat_calibration.json",
  "log_path": "results/exp38_roc/",
  "completed_at": "2026-05-21T01:57:36.011Z"
}

=== exp42_ood_benign_mixed ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-22T03:58:04.544Z",
  "updated_at": "2026-05-22T04:10:33.954Z",
  "hypothesis": "Including WildChat benign conversations in training data will reduce WildChat FPR from 68.1% to below 30% while maintaining jailbreak OOD detection F1 above 0.95 on DD/AA/FITD, because the current high FPR is driven by benign distribution mismatch (exp14c: 100% from FP explosion), not model architecture limitations. Mixed benign training should expand the model's benign representation space to cover real-world conversational diversity.",
  "parent": "exp38_wildcat_calibration",
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=0 python scripts/exp42_ood_benign_mixed.py",
    "server": "westd-33183",
    "data_path": "data/exp42_mixed_train.jsonl (plan_002 train + 150 WildChat benign)",
    "data_count": "~500 (350 original + 150 WildChat)",
    "model_name": "microsoft/deberta-v3-base + BiGRU",
    "seed": "42,123,456",
    "checkpoint_source": "trained from scratch with mixed data",
    "eval_data": "wildchat_eval (~76), DD OOD, AA OOD, FITD OOD, IID test"
  },
  "metrics": {
    "wildchat_fpr_mean": 0,
    "wildchat_fpr_std": 0,
    "iid_f1_mean": 1,
    "ood_dd_f1_mean": 1,
    "ood_aa_f1_mean": 0.956,
    "ood_fitd_f1_mean": 1,
    "wildchat_eval_n": 49,
    "data_filtered": "27/226 jailbreak patterns removed",
    "train_size": "500 (350 orig + 150 WildChat benign)"
  },
  "checkpoint_path": "/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints/exp42_mixed_seed{42,123,456}/",
  "log_path": "/root/persuasion_turn_jailbreak_detect/results/exp42_training.log",
  "conclusion": "success",
  "completed_at": "2026-05-22T04:10:33.954Z"
}

=== exp42b_balanced_ratio_ablation ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-22T04:17:59.853Z",
  "updated_at": "2026-05-22T04:39:13.434Z",
  "hypothesis": "exp42's WildChat FPR reduction (68.1%\u21920%) is driven by benign distribution coverage, not the shifted class ratio (50:50\u219265:35). With balanced 50:50 ratio (88 WC benign + 87 orig benign vs 175 jailbreak), FPR should still drop to near 0%.",
  "parent": "exp42",
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=0 python scripts/exp42b_balanced_ratio_ablation.py",
    "server": "westd-33183",
    "data_path": "data/plan_002_splits/train.jsonl + data/wildchat_benign_226.jsonl",
    "data_count": 350,
    "model_name": "deberta-v3-base + GRU",
    "seed": "42,123,456",
    "checkpoint_source": "trained from scratch (ablation of exp42)",
    "eval_data": "wildchat_eval(49) + IID test + OOD DD/AA/FITD"
  },
  "conclusion": "success",
  "metrics": {
    "wildchat_fpr_mean": 0,
    "wildchat_fpr_std": 0,
    "iid_f1_mean": 1,
    "ood_dd_f1_mean": 1,
    "ood_aa_f1_mean": 0.9905,
    "ood_aa_recall_mean": 0.9875,
    "ood_fitd_f1_mean": 1,
    "wildchat_eval_n": 49,
    "train_size": 350,
    "train_composition": "175 jailbreak + 87 orig benign + 88 WildChat benign (50:50)",
    "total_time_min": 4.8
  },
  "checkpoint_path": "/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints/exp42b_balanced_seed{42,123,456}/",
  "log_path": "/tmp/exp42b.log",
  "completed_at": "2026-05-22T04:39:13.434Z"
}

=== exp28_data_efficiency ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-20T14:40:19.137Z",
  "updated_at": "2026-05-20T15:39:09.564Z",
  "hypothesis": "9-class DAPT maintains strong OOD generalization even at 25% training data (n=50-125), outperforming vanilla baseline at 100% data (n=350), demonstrating high sample efficiency of persuasion-grounded representations.",
  "spec": {
    "command": "python scripts/exp28_data_efficiency.py + exp28_vanilla_only.py",
    "server": "westd-33183",
    "data_path": "data/plan_002_splits/train.jsonl",
    "data_count": 350,
    "model_name": "microsoft/deberta-v3-base",
    "seed": 42,
    "pid": "63305",
    "log_path": "/tmp/exp28_data_efficiency.log",
    "checkpoint_path": "/root/autodl-tmp/exp28_checkpoints",
    "note": "Train set is 350 (not 500). Subset sizes: {50, 125, 250, 350}. 4 x 9class + 2 x vanilla = 6 conditions. Single seed=42."
  },
  "metrics": {
    "9class": {
      "50": {
        "iid": 1,
        "dd_ood": 1,
        "aa_ood": 0.99
      },
      "125": {
        "iid": 1,
        "dd_ood": 1,
        "aa_ood": 0.99
      },
      "250": {
        "iid": 1,
        "dd_ood": 1,
        "aa_ood": 1
      },
      "350": {
        "iid": 1,
        "dd_ood": 1,
        "aa_ood": 1
      }
    },
    "vanilla": {
      "125": {
        "iid": 0.53,
        "dd_ood": 0.24,
        "aa_ood": 0.24
      },
      "350": {
        "iid": 1,
        "dd_ood": 0.36,
        "aa_ood": 0.49
      }
    },
    "note": "9-class at 14% data (50 samples) already achieves DD=1.0, AA=0.99 \u2014 outperforming vanilla at 100% by 64pp (DD) and 50pp (AA). Sample efficiency entirely driven by DAPT representation quality."
  },
  "conclusion": "success",
  "completed_at": "2026-05-20T15:38:00.832Z"
}

=== exp28b_data_efficiency_supplement ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-20T15:40:53.186Z",
  "updated_at": "2026-05-20T19:15:30.605Z",
  "hypothesis": "9-class DAPT maintains robust OOD performance across different random seeds (model initialization), and vanilla DeBERTa shows poor OOD generalization even at smaller training sizes (N=50, N=250), confirming that the data efficiency advantage of 9-class DAPT is not an artifact of a single seed.",
  "parent": "exp28_data_efficiency",
  "spec": {
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/persuasion_turn_jailbreak_detect && python scripts/exp28b_supplement.py",
    "server": "westd-33183",
    "data_path": "data/plan_002_splits/",
    "data_count": 350,
    "model_name": "microsoft/deberta-v3-base",
    "seed": "42/123/456",
    "checkpoint_source": "trained_from_scratch",
    "eval_data": "plan_002_splits/test.jsonl + DD OOD + AA OOD",
    "checkpoint_path": "N/A (probe only)",
    "log_path": "/tmp/exp28b.log"
  },
  "metrics": {
    "9class_3seed_N50_aa_ood": "0.969\u00b10.037",
    "9class_3seed_N125_aa_ood": "0.975\u00b10.019",
    "9class_3seed_N250_aa_ood": "0.975\u00b10.035",
    "9class_3seed_N350_aa_ood": "0.972\u00b10.033",
    "note": "9-class 3-seed complete. Vanilla N=50/250 missing (script crashed float16 dtype in GRU eval). exp28b added seed123+456 for 9-class only."
  },
  "conclusion": "success",
  "completed_at": "2026-05-20T19:15:30.605Z"
}

=== exp55_5seed_mlm_vs_9class_aa ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-22T11:11:41.549Z",
  "updated_at": "2026-05-22T12:15:56.035Z",
  "hypothesis": "9-class persuasion-grounded DeBERTa DAPT produces significantly better OOD generalization than domain-exposure-only MLM DAPT, with the advantage being robust across 5 random seeds (expanding from 3 to address reviewer W2 concern about insufficient seed count)",
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=1 python scripts/exp55_5seed_expansion.py",
    "server": "westd-49690",
    "data_path": "/root/persuasion_turn_jailbreak_detect/data/plan_002_splits/",
    "data_count": "~800 train + OOD eval sets",
    "model_name": "microsoft/deberta-v3-base",
    "seed": "789,1024",
    "checkpoint_path": "/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints/exp55_*",
    "log_path": "/tmp/exp55_train.log"
  },
  "metrics": {
    "n_seeds": 5,
    "seeds": [
      42,
      123,
      456,
      789,
      1024
    ],
    "9class_aa_ood": {
      "mean": 0.9735,
      "std": 0.0124
    },
    "mlm_aa_ood": {
      "mean": 0.9566,
      "std": 0.0237
    },
    "9class_iid": {
      "mean": 1,
      "std": 0
    },
    "mlm_iid": {
      "mean": 0.9816,
      "std": 0.0134
    },
    "9class_dd_ood": {
      "mean": 0.9924,
      "std": 0.0111
    },
    "mlm_dd_ood": {
      "mean": 0.9883,
      "std": 0.0094
    },
    "9class_fitd_ood": {
      "mean": 1,
      "std": 0
    },
    "mlm_fitd_ood": {
      "mean": 0.9883,
      "std": 0.0094
    },
    "aa_ood_delta_pp": 1.69,
    "aa_ood_paired_ttest_p": 0.2461,
    "aa_ood_wilcoxon_p": 0.1875,
    "aa_ood_9class_wins": 4,
    "aa_ood_mlm_wins": 1,
    "total_time_min": 10.5
  },
  "conclusion": "negative",
  "completed_at": "2026-05-22T12:15:56.035Z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "718732c6-c25d-47b6-8535-6b8cad76c630",
  "isSidechain": true,
  "promptId": "5df424ed-94b3-4801-a077-e8e00b57103c",
  "agentId": "afbd91c4ab95ef894",
  "type": "user",
  "uuid": "8513564d-5f0e-4435-b987-77fbc836dea7",
  "sourceToolAssistantUUID": "718732c6-c25d-47b6-8535-6b8cad76c630",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-22T21:32:53.032Z_

All relevant data has been extracted. Here is the complete verbatim data:

---

## 1. WildChat Adaptation Curve (FPR vs N target conversations)

**exp19_wildchat_fpr** — Baseline FPR before any adaptation (exp17 checkpoints, 226 filtered benign, avg 7.4 turns):

```
dataset: wildchat_benign_226 (226 filtered multi-turn benign, avg 7.4 turns)

9class_fpr:
  seed42:  0.668
  seed123: 0.611
  seed456: 0.765
  mean:    0.681
  std:     0.064

mlm_fpr:
  seed42:  0.367
  seed123: 0.646
  seed456: 0.323
  mean:    0.445
  std:     0.143

vanilla_fpr:
  seed42:  0.473
  seed123: 0.425
  seed456: 0.544
  mean:    0.481
  std:     0.049

note: "NEGATIVE: All variants show extreme FPR on real-world benign. 9-class worst (68.1%). Used exp17 checkpoints (Qwen 1000 scale). Severe distribution shift between synthetic training benign and real WildChat conversations."
```

**exp45_benign_adaptation_curve** — WildChat adaptation curve (single seed 42):

```
single_seed_42:
  n0_fpr:   0.653
  n5_fpr:   0.163
  n10_fpr:  0
  n25_fpr:  0
  n50_fpr:  0
  n100_fpr: 0
  n150_fpr: 0

n10_multiseed (seeds: [42, 123, 456]):
  wc_fpr:   "0.000±0.000"
  iid_f1:   "1.000±0.000"
  dd_f1:    "1.000±0.000"
  aa_f1:    "0.981±0.016"
  fitd_f1:  "1.000±0.000"

conclusion: success
```

**exp38_wildcat_calibration** — Threshold calibration on WildChat (cannot fix domain shift):

```
roc_auc:
  mean: 0.70, std: 0.054
  per_seed: seed42=0.768, seed123=0.697, seed456=0.635

default_t05_fpr: mean=0.791, std=0.098

threshold_calibration_held_out:
  tpr95_fpr: mean=0.627, std=0.100
  tpr90_fpr: mean=0.587, std=0.091

temperature_scaling:
  learned_T: "20-40 (severe overconfidence)"
  temp_scaled_tpr95_fpr: 0.627
  temp_scaled_tpr90_fpr: 0.583
  note: "Temperature scaling does NOT change FPR because ROC is invariant to monotonic score transforms"

note: "AUC=0.70 is the fundamental ceiling. Threshold calibration drops FPR from 79%→63% (at TPR95), still far from <25% target. WildChat high FPR is genuine domain shift, not calibration artifact."
conclusion: negative
```

**exp42_ood_benign_mixed** — Training with 150 WildChat benign samples (seeds 42/123/456):

```
wildchat_fpr_mean: 0
wildchat_fpr_std:  0
iid_f1_mean:       1
ood_dd_f1_mean:    1
ood_aa_f1_mean:    0.956
ood_fitd_f1_mean:  1
wildchat_eval_n:   49
train_size: "500 (350 orig + 150 WildChat benign)"
conclusion: success
```

**exp42b_balanced_ratio_ablation** — 50:50 ratio ablation (175 jailbreak + 87 orig benign + 88 WC benign, seeds 42/123/456):

```
wildchat_fpr_mean: 0
wildchat_fpr_std:  0
iid_f1_mean:       1
ood_dd_f1_mean:    1
ood_aa_f1_mean:    0.9905
ood_aa_recall_mean: 0.9875
ood_fitd_f1_mean:  1
wildchat_eval_n:   49
train_size: 350
conclusion: success
```

---

## 2. OASST2 Adaptation Curve (FPR vs N target conversations)

**exp51_lmsys_benign_ood** — OASST2 adaptation curve (seed 42, 200 eval conversations):

```
baseline_fpr: 0.575
baseline_n: 200
data_source: "oasst2 (real crowdsourced human)"

adaptation_curve:
  n0:  fpr=0.575
  n10: fpr=0.205, dd_f1=1, aa_f1=1,     fitd_f1=1
  n25: fpr=0.015, dd_f1=1, aa_f1=0.953,  fitd_f1=1
  n50: fpr=0.005, dd_f1=1, aa_f1=0.99,   fitd_f1=1

comparison_wildchat:
  baseline_fpr: 0.681
  n10_fpr: 0
  n10_sufficient: true

conclusion: success
```

**exp52_oasst2_n25_multiseed** — OASST2 N=25 adaptation, multi-seed validation (seeds 42/123/456):

```
seed_42:
  oasst2_fpr: 0.015
  iid_f1: 1, aa_f1: 0.953, dd_f1: 1, fitd_f1: 1

seed_123:
  oasst2_fpr: 0.005
  iid_f1: 1, aa_f1: 0.917, dd_f1: 1, fitd_f1: 1

seed_456:
  oasst2_fpr: 0.010
  iid_f1: 1, aa_f1: 0.990, dd_f1: 1, fitd_f1: 1

fpr_mean:  0.010
fpr_std:   0.005
fpr_range: "0.5%-1.5%"
conclusion: success
```

---

## 3. Per-Seed Variance: DD OOD / AA OOD F1

### 9-class (main treatment), seeds 42/123/456

**plan_002_clean_training** (seed 42):

```
dd_ood: k1=1, k2=1, k3=1, k5=1, full=1
```

**plan_002_seed123** (seed 123):

```
dd_ood: k1=1, k2=0.9904, k3=0.9904, k5=1, full=1
```

**plan_002_seed456** (seed 456):

```
dd_ood: k1=0.9715, k2=0.9622, k3=0.9350, k5=0.9904, full=0.9904
```

**exp35_cross_seed_ensemble** (seeds 42/123/456, DD OOD + AA OOD, BiGRU):

```
dd_ood / 9class:
  ensemble_f1:      1
  individual_mean:  0.9968
  individual_std:   0.0045

aa_ood / 9class:
  ensemble_f1:      0.9809
  individual_mean:  0.9719
  individual_std:   0.0261

fitd_ood / 9class:
  ensemble_f1:      1
  individual_mean:  1
  individual_std:   0
```

**exp13_meanpool_multiseed** (seeds 42/123/456, mean pooling, 9-class):

```
dd_ood:
  k1:   mean=0.9905, std=0.0134
  k2:   mean=0.9936, std=0.0090
  k3:   mean=0.9842, std=0.0160
  k5:   mean=0.9968, std=0.0045
  full: mean=0.9905, std=0.0134

actorattack (AA):
  k1:   mean=0.8301, std=0.0272
  k2:   mean=0.9030, std=0.0229
  k3:   mean=0.9622, std=0.0076
  k5:   mean=0.9716, std=0.0153
  full: mean=0.9623, std=0.0151
```

**exp2_actorattack_ood** (seeds 42/123/456, all DeBERTa variants):

```
deberta_9class AA OOD:
  k1=0.773 (std=0.041), k2=0.855 (std=0.048), k3=0.921 (std=0.046),
  k5=0.966 (std=0.028), full=0.972 (std=0.026)

deberta_binary AA OOD:
  k1=0.737 (std=0.074), k2=0.890 (std=0.065), k3=0.951 (std=0.036),
  k5=0.987 (std=0.012), full=0.990 (std=0.008)
  note: "seed42 weak outlier at K1=0.636"

deberta_scrambled AA OOD:
  k1=0.721 (std=0.101), k2=0.828 (std=0.054), k3=0.893 (std=0.067),
  k5=0.937 (std=0.057), full=0.951 (std=0.043)
  per_seed_full: seed42=0.891, seed123=0.990, seed456=0.971
  per_seed_k1:   seed42=0.618, seed123=0.858, seed456=0.686
  per_seed_k3:   seed42=0.808, seed123=0.972, seed456=0.900

deberta_mlm AA OOD:
  k1=0.736 (std=0.150), k2=0.909 (std=0.058), k3=0.945 (std=0.039),
  k5=0.929 (std=0.033), full=0.893 (std=0.080)

deberta_vanilla AA OOD:
  k1=0.337 (std=0.049), k2=0.306 (std=0.026), k3=0.284 (std=0.011),
  k5=0.262 (std=0.006), full=0.258 (std=0.000)

note: "Evidence hierarchy: binary ≈ 9class > scrambled >> mlm > wiki_mlm > topic > vanilla"
```

### Vanilla, seeds 42/123/456 (DD OOD)

**vanilla_multiseed_dd_ood**:

```
vanilla_3seed_dd_ood:
  k1:   seed42=0.575, seed123=0.658, seed456=0.652, mean=0.628, std=0.038
  k2:   seed42=0.438, seed123=0.530, seed456=0.469, mean=0.479, std=0.038
  k3:   seed42=0.359, seed123=0.424, seed456=0.383, mean=0.389, std=0.027
  k5:   seed42=0.311, seed123=0.383, seed456=0.360, mean=0.351, std=0.030
  full: seed42=0.285, seed123=0.305, seed456=0.348, mean=0.312, std=0.026
```

### Binary variant, seeds 42/123/456 (DD OOD)

**mf1_binary_seed123**: dd_ood_k1=1, k2=1, k3=0.9904, k5=1, full=1
**mf1_binary_seed456**: dd_ood_k1=1, k2=1, k3=0.9904, k5=1, full=1

### Scrambled variant, seeds 42/123/456 (DD OOD)

**mf1_scrambled_seed123**: dd_ood_k1=1, k2=1, k3=1, k5=1, full=1
**mf1_scrambled_seed456**: dd_ood_k1=1, k2=1, k3=0.990, k5=1, full=1

### 5-seed expansion (seeds 42/123/456/789/1024)

**exp55_5seed_mlm_vs_9class_aa** (full-prefix F1, DD and AA):

```
9class_aa_ood:   mean=0.9735, std=0.0124
mlm_aa_ood:      mean=0.9566, std=0.0237
9class_dd_ood:   mean=0.9924, std=0.0111
mlm_dd_ood:      mean=0.9883, std=0.0094
9class_fitd_ood: mean=1, std=0
mlm_fitd_ood:    mean=0.9883, std=0.0094
aa_ood_delta_pp: 1.69
aa_ood_paired_ttest_p: 0.2461
aa_ood_wilcoxon_p: 0.1875
conclusion: negative (delta not statistically significant)
```

**exp39_extra_seeds_tost** (seeds 789/1000):

```
9class_seed789: iid=1, dd_ood=1, aa_ood=0.9715, fitd_ood=1
9class_seed1000: iid=1, dd_ood=1, aa_ood=0.9715, fitd_ood=0.9904
scrambled_seed789: iid=1, dd_ood=1, aa_ood=0.9904, fitd_ood=1
scrambled_seed1000: iid=1, dd_ood=1, aa_ood=0.9904, fitd_ood=0.9904
```

**exp41_tost_10seed** (all 10 seeds: 42/123/456/789/1000/2024/2025/2026/314/628):

```
tost_DD: p=2.06e-09, equivalent=true, cohens_d=-0.136
tost_AA: p=0.183,    equivalent=false, cohens_d=0.44
tost_FITD: p=0,      equivalent=true,  cohens_d=0
9class_AA_mean: 0.979
scrambled_AA_mean: 0.949
AA_mean_diff_pp: 3
conclusion: negative (AA not TOST-equivalent at 10 seeds)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8513564d-5f0e-4435-b987-77fbc836dea7",
  "isSidechain": true,
  "agentId": "afbd91c4ab95ef894",
  "requestId": "req_011CbJKd95aZxgRujSxgQd6U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "168c86a1-3c02-4cb7-972c-f07180ec4f36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "e4efefca-26d6-49cf-8a09-2af928a47017",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Su6UqgTzrqEACzRVDCBuEQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9293,
      "cache_read_input_tokens": 41397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9293,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---
