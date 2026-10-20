# Research conversation: Parse the experiment registry JSON file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a8867062004a08a3c.jsonl`
- **Structured JSON:** [`f29ab18bfbbd193afb1d.json`](../../sessions/f2/f29ab18bfbbd193afb1d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-24T15:06:53.657Z_

Parse the experiment registry JSON file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt

This is JSON with schema: {result: string}. The "result" field is itself a JSON string that needs to be parsed.

I need you to extract ALL experiment entries and for each one report:
1. experiment name/id
2. status
3. metrics (especially GAR, PPL, NGAR, per_turn data if any)
4. conclusion
5. any per-seed results
6. any per-turn GAR data
7. model type (qwen vs llama)
8. condition (Base, TG, SS, LoRA, UG, PCGrad)

Focus especially on:
- Multi-seed eval results for SS (s42/s123/s456) and TG (s42/s123)
- Per-turn GAR data
- Llama cross-model results
- Any entry with "llama" in the name

Report ALL metrics verbatim - don't summarize or abbreviate numbers. This is for generating paper tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "46b2b0c6-9613-417a-9397-99622f342526",
  "agentId": "a8867062004a08a3c",
  "type": "user",
  "uuid": "4fa61f25-b610-444b-9392-d8b16fac57b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-24T15:06:53.661Z_

```json
{
  "parentUuid": "4fa61f25-b610-444b-9392-d8b16fac57b5",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
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
  "uuid": "b8669139-6b6c-4081-84cd-ba45bd2d4630",
  "timestamp": "2026-05-24T15:06:53.661Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-24T15:06:55.896Z_



I'll read the file first to understand its structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8669139-6b6c-4081-84cd-ba45bd2d4630",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbtAJY8G89HBGr9ndiR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bd56b4d-3923-4f58-8b97-00c558ac7df1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mKrwFSqdps5cKBrVcLTf7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16487,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16487,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 4 · 2026-05-24T15:06:57.319Z_

<details open><summary>🔧 Tool call — Read · `toolu_015rWtHJnbm3tb61CLxv3TED`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bd56b4d-3923-4f58-8b97-00c558ac7df1",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbtAJY8G89HBGr9ndiR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f829fa20-a96b-4fb0-94ab-e26957939c08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mKrwFSqdps5cKBrVcLTf7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16487,
      "cache_read_input_tokens": 0,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16487
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 172,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16487,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16487,
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

_source line 5 · 2026-05-24T15:06:57.608Z_

<details><summary>↩ Tool result · reported error · `toolu_015rWtHJnbm3tb61CLxv3TED`</summary>

```text
File content (43516 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f829fa20-a96b-4fb0-94ab-e26957939c08",
  "isSidechain": true,
  "promptId": "46b2b0c6-9613-417a-9397-99622f342526",
  "agentId": "a8867062004a08a3c",
  "type": "user",
  "uuid": "b5e071d4-5fbb-44ba-ae28-e87f62e97f93",
  "toolUseResult": "Error: File content (43516 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "f829fa20-a96b-4fb0-94ab-e26957939c08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-24T15:06:59.837Z_

The file is very large. Let me read it in chunks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5e071d4-5fbb-44ba-ae28-e87f62e97f93",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbtTE2F8YcWmrjvphEB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5fbe11d-c530-43d8-a53a-fec1c0483212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXm8dzRkhHbNhJmWtPCDHv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1074,
      "cache_read_input_tokens": 16487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1074,
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

_source line 7 · 2026-05-24T15:07:00.941Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X9xNmtZavLQrDM4tQAcXTR`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt",
  "limit": 500,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5fbe11d-c530-43d8-a53a-fec1c0483212",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbtTE2F8YcWmrjvphEB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0c4823e-de15-4a80-b767-ff1d4e243cb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXm8dzRkhHbNhJmWtPCDHv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1074,
      "cache_read_input_tokens": 16487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1074,
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

### Tool result

_source line 8 · 2026-05-24T15:07:01.214Z_

<details><summary>↩ Tool result · reported error · `toolu_01X9xNmtZavLQrDM4tQAcXTR`</summary>

```text
File content (43516 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0c4823e-de15-4a80-b767-ff1d4e243cb8",
  "isSidechain": true,
  "promptId": "46b2b0c6-9613-417a-9397-99622f342526",
  "agentId": "a8867062004a08a3c",
  "type": "user",
  "uuid": "8439c41a-b66a-4266-8e61-6f6f5c7445be",
  "toolUseResult": "Error: File content (43516 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "f0c4823e-de15-4a80-b767-ff1d4e243cb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T15:07:04.583Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QZQhuVBop5zFzUmDb3WTv9`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt",
  "description": "Count lines in the registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8439c41a-b66a-4266-8e61-6f6f5c7445be",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbtibVUZXar5DttrJhU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eab772b0-3043-4c30-ab07-2a10395e527c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015zdE3FBD4diRHmhQFekyDa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 251,
      "cache_read_input_tokens": 17561,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 251
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 17561,
          "cache_creation_input_tokens": 251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 251,
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

_source line 10 · 2026-05-24T15:07:04.761Z_

<details><summary>↩ Tool result · `toolu_01QZQhuVBop5zFzUmDb3WTv9`</summary>

```text
0 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eab772b0-3043-4c30-ab07-2a10395e527c",
  "isSidechain": true,
  "promptId": "46b2b0c6-9613-417a-9397-99622f342526",
  "agentId": "a8867062004a08a3c",
  "type": "user",
  "uuid": "4c8521e6-9845-4677-93cc-81299bef810a",
  "sourceToolAssistantUUID": "eab772b0-3043-4c30-ab07-2a10395e527c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-24T15:07:06.945Z_

It's a single-line JSON file. Let me use a script to parse it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c8521e6-9845-4677-93cc-81299bef810a",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbtyonqXJzafmrPG2ro",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4e7981b-541a-4845-a610-815aa19627c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N87PaksEyELDNDZTeRJUXW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 17812,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 271,
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

_source line 12 · 2026-05-24T15:07:10.874Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01B5WPuBk3KxhfwdV8f87EEs`</summary>

```json
{
  "command": "python3 -c \"\nimport json, sys\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nprint(type(inner))\nif isinstance(inner, dict):\n    print('Top-level keys:', list(inner.keys()))\n    for k, v in inner.items():\n        print(f'  {k}: type={type(v).__name__}')\n        if isinstance(v, dict):\n            print(f'    subkeys: {list(v.keys())[:10]}')\n        elif isinstance(v, list):\n            print(f'    length: {len(v)}')\nelif isinstance(inner, list):\n    print(f'List length: {len(inner)}')\n    if inner:\n        print(f'First item type: {type(inner[0]).__name__}')\n        if isinstance(inner[0], dict):\n            print(f'First item keys: {list(inner[0].keys())}')\n\" 2>&1\n",
  "description": "Parse the outer JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4e7981b-541a-4845-a610-815aa19627c8",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbtyonqXJzafmrPG2ro",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd89bf90-1bb4-480d-bdbf-e6e48b193717",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N87PaksEyELDNDZTeRJUXW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 17812,
      "output_tokens": 428,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 271
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 428,
          "cache_read_input_tokens": 17812,
          "cache_creation_input_tokens": 271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 271,
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

_source line 13 · 2026-05-24T15:07:10.982Z_

<details><summary>↩ Tool result · `toolu_01B5WPuBk3KxhfwdV8f87EEs`</summary>

```text
&lt;class 'dict'>
Top-level keys: ['success', 'data', 'error', 'metadata']
  success: type=bool
  data: type=dict
    subkeys: ['experiments', 'count', 'total', 'baseline']
  error: type=NoneType
  metadata: type=dict
    subkeys: ['elapsed_seconds']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd89bf90-1bb4-480d-bdbf-e6e48b193717",
  "isSidechain": true,
  "promptId": "46b2b0c6-9613-417a-9397-99622f342526",
  "agentId": "a8867062004a08a3c",
  "type": "user",
  "uuid": "7be0e9ca-169f-49ed-baa1-391674f72315",
  "sourceToolAssistantUUID": "cd89bf90-1bb4-480d-bdbf-e6e48b193717",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-24T15:07:16.190Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01M5AHi5aJRhboYw27wRHy79`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\ndata = inner['data']\nprint('count:', data['count'])\nprint('total:', data['total'])\nprint('baseline:', data.get('baseline'))\nprint()\nexps = data['experiments']\nprint(f'Number of experiments: {len(exps)}')\nprint()\nfor i, exp in enumerate(exps):\n    print(f'--- Experiment {i} ---')\n    print(f'  name: {exp.get(\\\"name\\\", \\\"N/A\\\")}')\n    print(f'  id: {exp.get(\\\"id\\\", \\\"N/A\\\")}')\n    print(f'  status: {exp.get(\\\"status\\\", \\\"N/A\\\")}')\n    print(f'  keys: {list(exp.keys())}')\n    print()\n\" 2>&1\n",
  "description": "List all experiments with names and status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7be0e9ca-169f-49ed-baa1-391674f72315",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbuSMDTHTFD9PV5yGj7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec0ca377-fda4-462d-85fd-f6b406243f6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011P7Xm7boJ3sqV7qGvF2cbt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 526,
      "cache_read_input_tokens": 18083,
      "output_tokens": 400,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 526
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 400,
          "cache_read_input_tokens": 18083,
          "cache_creation_input_tokens": 526,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 526,
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

_source line 15 · 2026-05-24T15:07:16.404Z_

<details><summary>↩ Tool result · reported error · `toolu_01M5AHi5aJRhboYw27wRHy79`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 18, in &lt;module>
    print(f'  name: {exp.get("name", "N/A")}')
                     ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
count: 53
total: 53
baseline: None

Number of experiments: 53

--- Experiment 0 ---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec0ca377-fda4-462d-85fd-f6b406243f6e",
  "isSidechain": true,
  "promptId": "46b2b0c6-9613-417a-9397-99622f342526",
  "agentId": "a8867062004a08a3c",
  "type": "user",
  "uuid": "8381eeb1-2097-4089-8fbe-f70d4b3c0ad0",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 18, in &lt;module>\n    print(f'  name: {exp.get(\"name\", \"N/A\")}')\n                     ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'\ncount: 53\ntotal: 53\nbaseline: None\n\nNumber of experiments: 53\n\n--- Experiment 0 ---",
  "sourceToolAssistantUUID": "ec0ca377-fda4-462d-85fd-f6b406243f6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-24T15:07:25.158Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0185TWQBTstnzUZnX1W9u85d`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# experiments is a dict with string keys\nprint(type(exps))\nif isinstance(exps, dict):\n    keys = list(exps.keys())\n    print(f'Number of keys: {len(keys)}')\n    for k in keys[:3]:\n        print(f'Key: {k}')\n        print(f'Value type: {type(exps[k]).__name__}')\n        v = exps[k]\n        if isinstance(v, dict):\n            print(f'  subkeys: {list(v.keys())}')\n        elif isinstance(v, str):\n            print(f'  value (first 200 chars): {v[:200]}')\n        print()\nelif isinstance(exps, list):\n    print('First 3 items:')\n    for item in exps[:3]:\n        print(f'  type={type(item).__name__}, value={str(item)[:200]}')\n\" 2>&1\n",
  "description": "Inspect structure of experiments dict"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8381eeb1-2097-4089-8fbe-f70d4b3c0ad0",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbuqXVYpB6BkjFNLLpQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a9a805f-f827-4824-904a-811540285f3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M68dsUcuXncbfZex6giNKU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 18609,
      "output_tokens": 449,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 523
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 449,
          "cache_read_input_tokens": 18609,
          "cache_creation_input_tokens": 523,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 523,
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

_source line 17 · 2026-05-24T15:07:25.252Z_

<details><summary>↩ Tool result · `toolu_0185TWQBTstnzUZnX1W9u85d`</summary>

```text
&lt;class 'dict'>
Number of keys: 53
Key: mmlu_eval_all
Value type: dict
  subkeys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'metrics', 'completed_at']

Key: p1_llama_ss_training
Value type: dict
  subkeys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec']

Key: p2_llama_gradient_conflict
Value type: dict
  subkeys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'metrics', 'completed_at']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a9a805f-f827-4824-904a-811540285f3d",
  "isSidechain": true,
  "promptId": "46b2b0c6-9613-417a-9397-99622f342526",
  "agentId": "a8867062004a08a3c",
  "type": "user",
  "uuid": "0ad4af5e-e863-4d8c-89dd-640207bd4904",
  "sourceToolAssistantUUID": "0a9a805f-f827-4824-904a-811540285f3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-24T15:07:27.512Z_

Now I understand the structure. Let me extract all experiments with their full details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ad4af5e-e863-4d8c-89dd-640207bd4904",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbvVSn77dCFmVEvxeCN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eed4e7a2-e0a8-4b28-acbb-730d3d9be5bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkewTWkV5gaaVQKVizt6vY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 651,
      "cache_read_input_tokens": 19132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 651,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 19 · 2026-05-24T15:07:29.574Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RVKxCyLbB31fc1QsSMB2EM`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\ndata = inner['data']\nexps = data['experiments']\n\nkeys = sorted(exps.keys())\nfor k in keys:\n    print(f'  {k}: status={exps[k].get(\\\"status\\\",\\\"?\\\")}')\" 2>&1\n",
  "description": "List all 53 experiment names and statuses"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eed4e7a2-e0a8-4b28-acbb-730d3d9be5bf",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbvVSn77dCFmVEvxeCN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16d0748e-4a5e-471b-9add-98ea5bb77377",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkewTWkV5gaaVQKVizt6vY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 651,
      "cache_read_input_tokens": 19132,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 651
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 19132,
          "cache_creation_input_tokens": 651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 651,
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

_source line 20 · 2026-05-24T15:07:29.655Z_

<details><summary>↩ Tool result · `toolu_01RVKxCyLbB31fc1QsSMB2EM`</summary>

```text
  analysis_attention_heatmap: status=DONE
  analysis_gradient_conflict: status=DONE
  attention_steering_eval200_tf: status=DONE
  attention_steering_gen_n50: status=DONE
  attention_steering_v7_tg_gen: status=DONE
  d048_eval_ss_s123: status=DONE
  d048_eval_ss_s42: status=DONE
  d048_eval_ss_s456: status=DONE
  d048_final_ar_eval: status=DONE
  d048_queue_runner: status=PREPARING
  d048_split_softmax_eval: status=DONE
  d048_ss_s123: status=DONE
  d048_ss_s42: status=DONE
  d048_ss_s42_resume: status=PREPARING
  d048_ss_s456: status=DONE
  eval_llama_ar_n20: status=DONE
  eval_llama_lora_only_s42: status=DONE
  eval_v7_tg_s123: status=DONE
  eval_v8b_ss: status=DONE
  eval_v8b_ss_s123: status=DONE
  instruction_retention_test: status=DONE
  llama_ar_matched_eval: status=DONE
  llama_eval_s42: status=DONE
  llama_lora_only_s42: status=DONE
  llama_phase1_gar_diag: status=DONE
  llama_tg_s42: status=DONE
  llama_tg_training: status=PREPARING
  mmlu_eval_all: status=DONE
  p0_ss_steering_eval: status=PREPARING
  p1_llama_ss_training: status=RUNNING
  p1_tf_ar_kl_divergence: status=DONE
  p2_llama_gradient_conflict: status=DONE
  phase1_gar_diag: status=DONE
  phase2_4way_eval: status=DONE
  phase2_4way_eval_heldout: status=DONE
  phase2_lora_only_s42: status=DONE
  phase2_tg_s42: status=DONE
  phase2_tg_s42_v2: status=DONE
  phase2_tg_s42_v3: status=DONE
  phase2_tg_s42_v3b: status=DONE
  phase2_tg_s42_v4: status=DONE
  phase2_tg_s42_v5: status=DONE
  phase2_tg_s42_v6: status=DONE
  phase2_tg_s42_v7: status=DONE
  phase2_tg_s42_v8_schedsampling: status=DONE
  phase2_tg_s42_v8b_resume: status=DONE
  phase2_tg_s42_v8b_ss_fixed: status=DONE
  phase2_tg_s42_v9_pcgrad: status=DONE
  phase2_ug_s42: status=DONE
  qwen15b_phase1_diag: status=DONE
  trc_baseline_v7_tg: status=DONE
  v7_tg_s123: status=DONE
  v8b_ss_s123: status=DONE
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16d0748e-4a5e-471b-9add-98ea5bb77377",
  "isSidechain": true,
  "promptId": "46b2b0c6-9613-417a-9397-99622f342526",
  "agentId": "a8867062004a08a3c",
  "type": "user",
  "uuid": "6daa2f11-6bcf-4732-a098-570412ca5a74",
  "sourceToolAssistantUUID": "16d0748e-4a5e-471b-9add-98ea5bb77377",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-24T15:07:33.953Z_

Now let me extract all the detailed metrics for every experiment. I'll do this in batches to handle the output size.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6daa2f11-6bcf-4732-a098-570412ca5a74",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbvpDPLRSwyshQGqgZU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "695c91b8-c5a3-41a1-b3f3-351ba481ff2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017w3GHmB19BtPn3tvRK8C58",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1265,
      "cache_read_input_tokens": 19783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1265,
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

_source line 22 · 2026-05-24T15:07:40.220Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01X4B6zgVJDoFewAM8SWvDS1`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Dump all experiments to a temp file for easier reading\nwith open('/tmp/all_experiments.json', 'w') as f:\n    json.dump(exps, f, indent=2, ensure_ascii=False)\n\nprint(\"Written to /tmp/all_experiments.json\")\nimport os\nprint(f\"Size: {os.path.getsize('/tmp/all_experiments.json')} bytes\")\nPYEOF\n",
  "description": "Dump all experiments to temp file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "695c91b8-c5a3-41a1-b3f3-351ba481ff2a",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbvpDPLRSwyshQGqgZU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03834446-b537-4496-85e2-1614e58389a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017w3GHmB19BtPn3tvRK8C58",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1265,
      "cache_read_input_tokens": 19783,
      "output_tokens": 346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1265
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 346,
          "cache_read_input_tokens": 19783,
          "cache_creation_input_tokens": 1265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1265,
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

_source line 23 · 2026-05-24T15:07:40.320Z_

<details><summary>↩ Tool result · `toolu_01X4B6zgVJDoFewAM8SWvDS1`</summary>

```text
Written to /tmp/all_experiments.json
Size: 105600 bytes
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03834446-b537-4496-85e2-1614e58389a1",
  "isSidechain": true,
  "promptId": "46b2b0c6-9613-417a-9397-99622f342526",
  "agentId": "a8867062004a08a3c",
  "type": "user",
  "uuid": "db78997d-f587-46b2-84c1-82d3451e3065",
  "sourceToolAssistantUUID": "03834446-b537-4496-85e2-1614e58389a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-24T15:07:48.080Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0144zTzw5vWkSQ2z4LSgu2js`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/all_experiments.json', 'r') as f:\n    exps = json.load(f)\n\n# Process each experiment and output full details\nkeys = sorted(exps.keys())\n\nfor k in keys:\n    exp = exps[k]\n    print(f\"{'='*80}\")\n    print(f\"EXPERIMENT: {k}\")\n    print(f\"{'='*80}\")\n    print(f\"  Status: {exp.get('status', 'N/A')}\")\n    print(f\"  Created: {exp.get('created_at', 'N/A')}\")\n    print(f\"  Updated: {exp.get('updated_at', 'N/A')}\")\n    print(f\"  Completed: {exp.get('completed_at', 'N/A')}\")\n    print(f\"  Retry count: {exp.get('retry_count', 'N/A')}\")\n    \n    hyp = exp.get('hypothesis', '')\n    if hyp:\n        print(f\"  Hypothesis: {hyp}\")\n    \n    spec = exp.get('spec', '')\n    if spec:\n        print(f\"  Spec: {spec}\")\n    \n    conclusion = exp.get('conclusion', '')\n    if conclusion:\n        print(f\"  Conclusion: {conclusion}\")\n    \n    metrics = exp.get('metrics', None)\n    if metrics:\n        print(f\"  Metrics:\")\n        if isinstance(metrics, dict):\n            print(json.dumps(metrics, indent=4, ensure_ascii=False))\n        else:\n            print(f\"    {metrics}\")\n    \n    print()\nPYEOF\n",
  "description": "Print all experiments with full details",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db78997d-f587-46b2-84c1-82d3451e3065",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbwbtkmGjx7tsGWASP2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2135b69-ba24-4783-8803-3ce341a80aac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKceeKHdxFc8FbhoqUp5j3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 376,
      "cache_read_input_tokens": 21048,
      "output_tokens": 507,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 376
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 507,
          "cache_read_input_tokens": 21048,
          "cache_creation_input_tokens": 376,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 376,
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

_source line 25 · 2026-05-24T15:07:48.166Z_

<details><summary>↩ Tool result · `toolu_0144zTzw5vWkSQ2z4LSgu2js`</summary>

```text
&lt;persisted-output>
Output too large (87KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt

Preview (first 2KB):
================================================================================
EXPERIMENT: analysis_attention_heatmap
================================================================================
  Status: DONE
  Created: 2026-05-19T15:03:16.154Z
  Updated: 2026-05-19T15:22:24.770Z
  Completed: 2026-05-19T15:22:24.770Z
  Retry count: 0
  Hypothesis: 四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。
  Spec: {'command': 'attention heatmap analysis script', 'server': 'westd-20861', 'data_path': 'standard_conversations.json', 'data_count': 5, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_source': 'phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42', 'eval_data': 'standard_conversations.json (5 convs x 10 turns)', 'checkpoint_path': 'N/A (analysis)', 'log_path': 'westd-20861:/root/turn_residual_gating/runs/analysis/'}
  Conclusion: success
  Metrics:
{
    "base_mean_goal_attn": 0.0136,
    "base_decay": 0.875,
    "tg_mean_goal_attn": 0.0232,
    "tg_decay": 0.777,
    "ug_mean_goal_attn": 0.0216,
    "ug_decay": 0.803,
    "lora_mean_goal_attn": 0.0216,
    "lora_decay": 0.81,
    "gating_incremental_benefit": "none"
}

================================================================================
EXPERIMENT: analysis_gradient_conflict
================================================================================
  Status: DONE
  Created: 2026-05-19T15:03:12.230Z
  Updated: 2026-05-19T15:22:23.782Z
  Completed: 2026-05-19T15:22:23.782Z
  Retry count: 0
  Hypothesis: NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2135b69-ba24-4783-8803-3ce341a80aac",
  "isSidechain": true,
  "promptId": "46b2b0c6-9613-417a-9397-99622f342526",
  "agentId": "a8867062004a08a3c",
  "type": "user",
  "uuid": "1cdaa661-39c8-43bb-8a39-fa6672320417",
  "sourceToolAssistantUUID": "c2135b69-ba24-4783-8803-3ce341a80aac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-24T15:07:50.473Z_

The output was saved to a file. Let me read it in sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cdaa661-39c8-43bb-8a39-fa6672320417",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbxBLuYudwQJRmPWhYQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c74e6e72-8471-4055-97c0-882b9817e4e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pxZKHM9rvyXoA383NiW6c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1320,
      "cache_read_input_tokens": 21424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1320,
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

_source line 27 · 2026-05-24T15:07:51.572Z_

<details open><summary>🔧 Tool call — Read · `toolu_014TnAzjTdyXGpLKo9PnLqNf`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt",
  "limit": 300,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c74e6e72-8471-4055-97c0-882b9817e4e5",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbxBLuYudwQJRmPWhYQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b03b9ef-b207-4df0-b669-0ee7c4f96cac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pxZKHM9rvyXoA383NiW6c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1320,
      "cache_read_input_tokens": 21424,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1320
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 21424,
          "cache_creation_input_tokens": 1320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1320,
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

_source line 28 · 2026-05-24T15:07:51.582Z_

<details><summary>↩ Tool result · `toolu_014TnAzjTdyXGpLKo9PnLqNf`</summary>

```text
0	================================================================================
1	EXPERIMENT: analysis_attention_heatmap
2	================================================================================
3	  Status: DONE
4	  Created: 2026-05-19T15:03:16.154Z
5	  Updated: 2026-05-19T15:22:24.770Z
6	  Completed: 2026-05-19T15:22:24.770Z
7	  Retry count: 0
8	  Hypothesis: 四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。
9	  Spec: {'command': 'attention heatmap analysis script', 'server': 'westd-20861', 'data_path': 'standard_conversations.json', 'data_count': 5, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_source': 'phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42', 'eval_data': 'standard_conversations.json (5 convs x 10 turns)', 'checkpoint_path': 'N/A (analysis)', 'log_path': 'westd-20861:/root/turn_residual_gating/runs/analysis/'}
10	  Conclusion: success
11	  Metrics:
12	{
13	    "base_mean_goal_attn": 0.0136,
14	    "base_decay": 0.875,
15	    "tg_mean_goal_attn": 0.0232,
16	    "tg_decay": 0.777,
17	    "ug_mean_goal_attn": 0.0216,
18	    "ug_decay": 0.803,
19	    "lora_mean_goal_attn": 0.0216,
20	    "lora_decay": 0.81,
21	    "gating_incremental_benefit": "none"
22	}
23	
24	================================================================================
25	EXPERIMENT: analysis_gradient_conflict
26	================================================================================
27	  Status: DONE
28	  Created: 2026-05-19T15:03:12.230Z
29	  Updated: 2026-05-19T15:22:23.782Z
30	  Completed: 2026-05-19T15:22:23.782Z
31	  Retry count: 0
32	  Hypothesis: NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。
33	  Spec: {'command': 'gradient conflict analysis script', 'server': 'westd-20861', 'data_path': 'v7 epoch 0/1/2 checkpoints', 'data_count': 3, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_source': 'phase2_tg_s42_v7', 'eval_data': 'v7 3-epoch checkpoints (gradient analysis)', 'checkpoint_path': 'N/A (analysis)', 'log_path': 'westd-20861:/root/turn_residual_gating/runs/analysis/'}
34	  Conclusion: success
35	  Metrics:
36	{
37	    "epoch0_cos_sim": -0.089,
38	    "epoch1_cos_sim": -0.054,
39	    "epoch2_cos_sim": -0.042,
40	    "epoch0_neg_layers_pct": 78.6,
41	    "epoch1_neg_layers_pct": 71.4,
42	    "epoch2_neg_layers_pct": 67.9,
43	    "epoch0_mag_ratio": 7.5,
44	    "epoch1_mag_ratio": 13.7,
45	    "epoch2_mag_ratio": 14.7
46	}
47	
48	================================================================================
49	EXPERIMENT: attention_steering_eval200_tf
50	================================================================================
51	  Status: DONE
52	  Created: 2026-05-20T09:58:23.626Z
53	  Updated: 2026-05-20T10:08:24.710Z
54	  Completed: 2026-05-20T10:08:24.710Z
55	  Retry count: 0
56	  Hypothesis: N=200 TF 模式 attention steering 验证 β-GAR 关系的统计鲁棒性。在 teacher-forced context (无 exposure bias) 下，steering 效果应更温和（baseline GAR 已 ~0.50），但仍展示 β 调控 attention 的能力。与 N=5 gen 模式结果互补：tf 验证机制可控性，gen 验证因果闭环。
57	  Spec: {'command': 'python src/eval_attention_steering.py --mode tf --betas 0 2 3 4 5 10 --output-name eval200_attention_steering.json (data: eval_200/eval_200.json, 200 convs)', 'server': 'westd-20861', 'data_path': 'data/eval_200/eval_200.json', 'data_count': 200, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_source': 'phase2_tg_s42_v7', 'eval_data': 'data/eval_200/eval_200.json', 'checkpoint_path': 'checkpoints/tg_v7_s42/final', 'log_path': '/tmp/eval200_steering.log'}
58	  Conclusion: success
59	  Metrics:
60	{
61	    "beta_0.0": {
62	        "mid_gar": 0.5353,
63	        "ppl": 2.62
64	    },
65	    "beta_2.0": {
66	        "mid_gar": 0.6112,
67	        "ppl": 2.69
68	    },
69	    "beta_3.0": {
70	        "mid_gar": 0.788,
71	        "ppl": 2.93
72	    },
73	    "beta_4.0": {
74	        "mid_gar": 0.8165,
75	        "ppl": 3.49
76	    },
77	    "beta_5.0": {
78	        "mid_gar": 0.8325,
79	        "ppl": 6.15
80	    },
81	    "beta_10.0": {
82	        "mid_gar": 0.977,
83	        "ppl": 505.21
84	    },
85	    "n_convs": 200,
86	    "mode": "tf"
87	}
88	
89	================================================================================
90	EXPERIMENT: attention_steering_gen_n50
91	================================================================================
92	  Status: DONE
93	  Created: 2026-05-20T19:04:17.455Z
94	  Updated: 2026-05-21T01:59:57.100Z
95	  Completed: 2026-05-20T19:55:34.383Z
96	  Retry count: 0
97	  Hypothesis: N=5 gen steering 显示 β∈[2,5] phase transition (GAR 0.06→0.68)，但样本量不足以报告置信区间。N=50 conversations 应重现同一 phase transition pattern 并提供统计鲁棒的 mean±std，加固 C6 claim (attention steering as causal mechanism proof)。
98	  Spec: {'command': 'CUDA_VISIBLE_DEVICES=0 python src/eval_attention_steering.py --checkpoint runs/phase2_tg_s42_v7 --mode gen --data-file data/eval_200/eval_200.json --max-convs 50 --beta 0 2 3 4 5 10 --output-dir runs/attention_steering/ --output-name attention_steering_gen_n50', 'server': 'westd-20861', 'gpu': ['cuda:0'], 'data_path': 'data/eval_200/eval_200.json', 'data_count': 50, 'model_name': 'Qwen2.5-7B-Instruct + v7 TG LoRA', 'seed': 'N/A (eval)', 'checkpoint_source': 'phase2_tg_s42_v7', 'eval_data': '50 conversations from eval_200.json, gen mode autoregressive', 'checkpoint_path': 'N/A (eval experiment)', 'log_path': '/root/turn_residual_gating/runs/attention_steering/attention_steering_gen_n50.json'}
99	  Conclusion: success
100	  Metrics:
101	{
102	    "corrected": true,
103	    "aggregation": "per-conv mid_gar(turns 2-7), >=3 turns only",
104	    "beta_0.0": {
105	        "mid_gar": 0.0641,
106	        "mid_gar_std": 0.0809,
107	        "ppl": 1.4324,
108	        "ppl_std": 0.1029,
109	        "n_valid": 39
110	    },
111	    "beta_2.0": {
112	        "mid_gar": 0.128,
113	        "mid_gar_std": 0.1101,
114	        "ppl": 1.4822,
115	        "ppl_std": 0.1385,
116	        "n_valid": 39
117	    },
118	    "beta_3.0": {
119	        "mid_gar": 0.5558,
120	        "mid_gar_std": 0.0601,
121	        "ppl": 1.5605,
122	        "ppl_std": 0.1719,
123	        "n_valid": 39
124	    },
125	    "beta_4.0": {
126	        "mid_gar": 0.6439,
127	        "mid_gar_std": 0.0607,
128	        "ppl": 1.6674,
129	        "ppl_std": 0.2241,
130	        "n_valid": 39
131	    },
132	    "beta_5.0": {
133	        "mid_gar": 0.7271,
134	        "mid_gar_std": 0.0605,
135	        "ppl": 1.7723,
136	        "ppl_std": 0.2693,
137	        "n_valid": 38
138	    },
139	    "beta_10.0": {
140	        "mid_gar": 0.9612,
141	        "mid_gar_std": 0.0152,
142	        "ppl": 3.4517,
143	        "ppl_std": 1.7813,
144	        "n_valid": 39
145	    },
146	    "n_convs_total": 50,
147	    "n_convs_valid": 39,
148	    "mode": "gen",
149	    "phase_transition_range": "[2, 3]"
150	}
151	
152	================================================================================
153	EXPERIMENT: attention_steering_v7_tg_gen
154	================================================================================
155	  Status: DONE
156	  Created: 2026-05-20T07:07:20.607Z
157	  Updated: 2026-05-20T09:30:17.530Z
158	  Completed: 2026-05-20T09:29:58.880Z
159	  Retry count: 0
160	  Hypothesis: 推理时向 attention logits 注入 goal-position bias β 可恢复 autoregressive GAR。如果 GAR 从 0.015 显著提升 → 闭合因果环：exposure bias → attention 偏移 → GAR 坍塌 → 手动修正注意力 → GAR 恢复。扫描 β ∈ {0, 0.5, 1.0, 2.0, 5.0, 10.0}，成功标准：GAR > 0.1 且 PPL 不严重恶化。
161	  Spec: {'command': 'bash scripts/launch_attention_steering.sh gen', 'server': 'westd-20861', 'gpu': ['cuda:0'], 'pid': '157657', 'log_path': 'runs/attention_steering/phase2_tg_s42_v7_attention_steering.json', 'submitted_at': '2026-05-20T07:07:27.678Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': 'data/ShareGPT_V3_format_5convs.json', 'data_count': 5, 'model_name': 'Qwen/Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_source': 'phase2_tg_s42_v7', 'eval_data': 'data/ShareGPT_V3_format_5convs.json', 'checkpoint_path': 'checkpoints/tg_v7_s42/final', 'wall_clock_seconds': 8551.2, 'gpu_hours': 2.38}
162	  Conclusion: success
163	  Metrics:
164	{
165	    "beta_0.0": {
166	        "mid_turns_avg_gar": 0.028,
167	        "avg_ppl": 1.409
168	    },
169	    "beta_0.5": {
170	        "mid_turns_avg_gar": 0.0287,
171	        "avg_ppl": 1.387
172	    },
173	    "beta_1.0": {
174	        "mid_turns_avg_gar": 0.0349,
175	        "avg_ppl": 1.36
176	    },
177	    "beta_2.0": {
178	        "mid_turns_avg_gar": 0.062,
179	        "avg_ppl": 1.411
180	    },
181	    "beta_5.0": {
182	        "mid_turns_avg_gar": 0.6795,
183	        "avg_ppl": 1.908
184	    },
185	    "beta_10.0": {
186	        "mid_turns_avg_gar": 0.959,
187	        "avg_ppl": 4.22
188	    },
189	    "phase_transition_range": "[2, 5]",
190	    "baseline_gar": 0.028,
191	    "max_gar_at_acceptable_ppl": 0.6795,
192	    "max_gar_at_acceptable_ppl_beta": 5
193	}
194	
195	================================================================================
196	EXPERIMENT: d048_eval_ss_s123
197	================================================================================
198	  Status: DONE
199	  Created: 2026-05-23T17:29:13.803Z
200	  Updated: 2026-05-23T18:05:41.813Z
201	  Completed: 2026-05-23T18:05:35.103Z
202	  Retry count: 0
203	  Hypothesis: SS s123 eval: TF + AR N=50 + bootstrap CI to establish multi-seed SS metrics. Expect TF GAR ~0.50, AR GAR similar to s42 (0.347), confirming SS effectiveness across seeds.
204	  Spec: {'command': 'bash scripts/d048_eval_ss_s123.sh', 'server': 'westd-20861', 'pid': '110052', 'data_path': '/root/turn-residual-gating/data/eval_200/eval_200.json', 'data_count': 200, 'model_name': 'Qwen/Qwen2.5-7B-Instruct + SS s123 LoRA', 'seed': 123, 'gpu': 0, 'checkpoint_source': '/root/turn-residual-gating/runs/d048_ss_s123/epoch_2', 'eval_data': '/root/turn-residual-gating/data/eval_200/eval_200.json', 'checkpoint_path': '/root/turn-residual-gating/results/d048_final_ar/', 'log_path': '/root/turn-residual-gating/results/d048_final_ar/'}
205	  Conclusion: success
206	  Metrics:
207	{
208	    "tf_gar_ours": 0.5536,
209	    "tf_gar_dongre": 0.4106,
210	    "tf_ppl": 2.6123,
211	    "ar_beta0_gar": 0.4231,
212	    "ar_beta0_ppl": 1.4408,
213	    "ar_beta3_gar": 0.5903,
214	    "ar_beta3_ppl": 1.607,
215	    "ar_beta5_gar": 0.7174,
216	    "ar_beta5_ppl": 1.7852,
217	    "n_convs_tf": 200,
218	    "n_convs_ar": 39
219	}
220	
221	================================================================================
222	EXPERIMENT: d048_eval_ss_s42
223	================================================================================
224	  Status: DONE
225	  Created: 2026-05-22T22:52:15.395Z
226	  Updated: 2026-05-22T23:32:26.276Z
227	  Completed: 2026-05-22T23:15:00.734Z
228	  Retry count: 0
229	  Hypothesis: D048 multi-seed SS s42 eval: TF + AR N=50 + bootstrap CI (curve[2:]) to establish mean±std for scheduled sampling. Expect TF GAR ~0.50, AR GAR gap < 2× (vs base ~31×), PPL stable.
230	  Spec: {'command': 'bash scripts/d048_eval_ss_s42.sh', 'server': 'westd-20861', 'gpu': ['cuda:0'], 'pid': '48241', 'log_path': '/root/turn_residual_gating/runs/d048_ss_s42/eval.log', 'submitted_at': '2026-05-22T22:52:15.275Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': 'data/ultrachat_8k + model-gen AR N=50', 'data_count': 50, 'model_name': 'Qwen2.5-7B-Instruct (SS s42)', 'seed': 42, 'checkpoint_source': 'runs/d048_ss_s42/epoch_2', 'eval_data': 'ultrachat_eval_heldout 50 + model-gen AR N=50', 'checkpoint_path': 'runs/d048_ss_s42/epoch_2', 'wall_clock_seconds': 1365.5, 'gpu_hours': 0.38}
231	  Conclusion: success
232	  Metrics:
233	{
234	    "tf": {
235	        "base_gar_ours_mid": 0.0128,
236	        "base_gar_dongre_mid": 0.0031,
237	        "base_ppl": 4.34,
238	        "base_ntp": 1.4,
239	        "tg_gar_ours_mid": 0.5025,
240	        "tg_gar_dongre_mid": 0.389,
241	        "tg_ppl": 2.78,
242	        "tg_ntp": 0.98,
243	        "baseline_mid_gar": 0.0122
244	    },
245	    "ar": {
246	        "gar_ours_mid": 0.3887,
247	        "gar_ours_ci_95": [
248	            0.3692,
249	            0.3934
250	        ],
251	        "ppl": 1.35
252	    },
253	    "gap_ratio": 1.29,
254	    "n_conversations_tf": 50,
255	    "n_conversations_ar": 5,
256	    "bootstrap_turns": "curve[2:] (turns 3-T)",
257	    "note": "AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch with eval_200.json N=50."
258	}
259	
260	================================================================================
261	EXPERIMENT: d048_eval_ss_s456
262	================================================================================
263	  Status: DONE
264	  Created: 2026-05-24T00:38:41.913Z
265	  Updated: 2026-05-24T01:19:46.692Z
266	  Completed: 2026-05-24T01:19:43.693Z
267	  Retry count: 0
268	  Hypothesis: SS s456 eval: TF + AR N=50 + bootstrap CI to complete 3-seed SS metrics. Together with s42 and s123, establishes mean±std for C2 reviewer requirement.
269	  Spec: {'command': 'bash scripts/d048_eval_ss_s456.sh', 'server': 'westd-20861', 'pid': '129280', 'data_path': '/root/turn-residual-gating/data/eval_200/eval_200.json', 'data_count': 200, 'model_name': 'Qwen/Qwen2.5-7B-Instruct + SS s456 LoRA', 'seed': 456, 'gpu': 0, 'checkpoint_source': '/root/turn-residual-gating/runs/d048_ss_s456/epoch_2', 'eval_data': '/root/turn-residual-gating/data/eval_200/eval_200.json', 'checkpoint_path': '/root/turn-residual-gating/results/d048_final_ar/', 'log_path': '/root/turn-residual-gating/results/d048_final_ar/'}
270	  Conclusion: success
271	  Metrics:
272	{
273	    "tf_gar_ours_mid": 0.4964,
274	    "tf_gar_dongre_mid": 0.3862,
275	    "ar_beta0_gar": 0.4325,
276	    "ar_beta0_ppl": 1.4394,
277	    "ar_beta3_gar": 0.605,
278	    "ar_beta3_ppl": 1.5868,
279	    "ar_beta5_gar": 0.7157,
280	    "ar_beta5_ppl": 1.8045,
281	    "n_convs_ar": 50
282	}
283	
284	================================================================================
285	EXPERIMENT: d048_final_ar_eval
286	================================================================================
287	  Status: DONE
288	  Created: 2026-05-23T03:46:23.495Z
289	  Updated: 2026-05-23T03:47:01.285Z
290	  Completed: 2026-05-23T03:46:57.110Z
291	  Retry count: 0
292	  Hypothesis: Unified AR N=50 eval across 6 conditions (Base/TG/UG/LO/PCGrad/SS) with bootstrap CI and Wilcoxon tests to establish statistically rigorous comparisons for all claims
293	  Spec: {'command': 'bash scripts/d048_final_ar_eval.sh', 'server': 'westd-20861', 'data_path': 'data/eval_200/eval_200.json', 'data_count': 200, 'model_name': 'Qwen/Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_source': 'phase2_tg_s42_v7 / phase2_ug_s42 / phase2_lora_only_s42 / tg_v9_pcgrad_s42 / d048_ss_s42', 'eval_data': 'eval_200.json N=50', 'checkpoint_path': 'N/A (eval only)', 'log_path': 'runs/d048_final_ar_eval.log', 'results_path': 'results/d048_final_ar/'}
294	  Conclusion: success
295	  Metrics:
296	{
297	    "beta0": {
298	        "base_gar": 0.019,
299	        "tg_gar": 0.064,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b03b9ef-b207-4df0-b669-0ee7c4f96cac",
  "isSidechain": true,
  "promptId": "46b2b0c6-9613-417a-9397-99622f342526",
  "agentId": "a8867062004a08a3c",
  "type": "user",
  "uuid": "927dd991-d0c1-4ad2-ab89-2e3710f29071",
  "sourceToolAssistantUUID": "6b03b9ef-b207-4df0-b669-0ee7c4f96cac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-24T15:07:56.883Z_

<details open><summary>🔧 Tool call — Read · `toolu_018AfaygkBsZWnsvuJkABmma`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt",
  "limit": 300,
  "offset": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "927dd991-d0c1-4ad2-ab89-2e3710f29071",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbxS2TSoDKLnHvHrdnt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12eeb278-0c56-47c4-82fe-04ae77ae930b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1WrYBP1Sc1ZHez5FdhVZs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6833,
      "cache_read_input_tokens": 22744,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6833
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 22744,
          "cache_creation_input_tokens": 6833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6833,
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

_source line 30 · 2026-05-24T15:07:56.893Z_

<details><summary>↩ Tool result · `toolu_018AfaygkBsZWnsvuJkABmma`</summary>

```text
300	        "tg_gar": 0.064,
301	        "ug_gar": 0.033,
302	        "lo_gar": 0.037,
303	        "pcgrad_gar": 0.03,
304	        "ss_gar": 0.347
305	    },
306	    "beta3": {
307	        "base_gar": 0.531,
308	        "tg_gar": 0.556,
309	        "ss_gar": 0.593
310	    },
311	    "beta5": {
312	        "base_gar": 0.704,
313	        "tg_gar": 0.727,
314	        "ss_gar": 0.717
315	    },
316	    "wilcoxon_beta0": {
317	        "tg_vs_base_p": "<0.001",
318	        "tg_vs_base_r": 0.802,
319	        "ss_vs_tg_p": "<0.001",
320	        "ss_vs_tg_r": 0.869
321	    },
322	    "ppl": {
323	        "base": 1.447,
324	        "tg": 1.432,
325	        "ss": 1.442
326	    },
327	    "n_convs": 39
328	}
329	
330	================================================================================
331	EXPERIMENT: d048_queue_runner
332	================================================================================
333	  Status: PREPARING
334	  Created: 2026-05-22T23:42:35.919Z
335	  Updated: 2026-05-22T23:42:39.048Z
336	  Completed: N/A
337	  Retry count: 0
338	  Conclusion: failed
339	
340	================================================================================
341	EXPERIMENT: d048_split_softmax_eval
342	================================================================================
343	  Status: DONE
344	  Created: 2026-05-23T07:47:05.556Z
345	  Updated: 2026-05-23T08:00:42.748Z
346	  Completed: 2026-05-23T07:53:10.326Z
347	  Retry count: 0
348	  Hypothesis: Split-softmax (Li et al., COLM 2024) post-softmax rescaling recovers AR GAR without the PPL cost of pre-softmax additive steering, providing an alternative inference-time intervention that separates attention allocation from logit distribution.
349	  Spec: {'command': 'python src/eval_split_softmax.py', 'server': 'westd-20861', 'data_path': 'data/eval_200/eval_200.json', 'data_count': 50, 'model_name': 'Qwen2.5-7B-Instruct + TG v7 LoRA', 'seed': 42, 'checkpoint_path': 'N/A (failed)', 'log_path': 'results/split_softmax/', 'failure_reason': 'Bug 1: system_prompt_len=0 hardcoded (line 373) — split-softmax has no effect. Bug 2: gen mode NaN for k=0.0/0.3/0.5/0.7. Needs code fix before re-run.'}
350	  Conclusion: failed
351	
352	================================================================================
353	EXPERIMENT: d048_ss_s123
354	================================================================================
355	  Status: DONE
356	  Created: 2026-05-23T07:54:41.928Z
357	  Updated: 2026-05-23T17:29:06.984Z
358	  Completed: 2026-05-23T17:29:06.984Z
359	  Retry count: 0
360	  Hypothesis: Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s123) to establish 3-seed mean±std for C2 reviewer requirement. Corrected hyperparams matching d048_ss_s456.
361	  Spec: {'command': 'python train_phase2_v8b.py --gate-type threadgate --seed 123 --output-dir runs/d048_ss_s123 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --ss-ratio 0.3', 'server': 'westd-20861', 'pid': '84793', 'data_path': '/root/turn-residual-gating/data/phase2_train.jsonl', 'data_count': 2000, 'model_name': 'Qwen/Qwen2.5-7B-Instruct', 'seed': 123, 'gpu': 0, 'checkpoint_source': 'Qwen/Qwen2.5-7B-Instruct (base, no prior checkpoint)', 'eval_data': 'N/A - this is a training experiment', 'checkpoint_path': '/root/turn-residual-gating/runs/d048_ss_s123/epoch_2', 'log_path': '/root/turn-residual-gating/runs/d048_ss_s123/train.log'}
362	  Conclusion: success
363	
364	================================================================================
365	EXPERIMENT: d048_ss_s42
366	================================================================================
367	  Status: DONE
368	  Created: 2026-05-22T09:14:13.365Z
369	  Updated: 2026-05-22T23:11:26.493Z
370	  Completed: 2026-05-22T15:51:54.391Z
371	  Retry count: 0
372	  Hypothesis: Scheduled sampling (ratio=0.3) with ThreadGate reduces the ~30× TF-AR GAR gap by exposing the model to its own generated text during training. Multi-seed run (s42) under D048 unified protocol to establish mean±std for statistical testing. SS is the strongest mitigation candidate (prior single-seed showed gap 31×→1.57×).
373	  Spec: {'command': 'bash -c "cd /root/turn_residual_gating && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --batch-size 1 --grad-accum 8 --max-seq-len 2048 --scheduled-sampling --ss-max-ratio 0.3 --seed 42 --epochs 3 --output-dir runs/d048_ss_s42 --data-dir data/ultrachat_8k --resume runs/d048_ss_s42/epoch_0 2>&1 | tee ~/runs/turn_residual_gating/d048_ss_s42_resume.log"', 'server': 'westd-20861', 'gpu': ['cuda:0'], 'pid': '32861', 'log_path': '~/runs/turn_residual_gating/d048_ss_s42.log', 'submitted_at': '2026-05-22T15:59:07.519Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root'}
374	  Conclusion: success
375	  Metrics:
376	{
377	    "final_avg_loss": 0.9326,
378	    "final_ntp_loss": 0.932,
379	    "final_gar_loss": 0.0007,
380	    "gate_mean": 0.9527,
381	    "gate_std": 0.0589,
382	    "gate_min": 0.7383,
383	    "gate_min_layer": "L4",
384	    "gate_max": 1,
385	    "ss_usage": "4750/16000 (29.7%)",
386	    "ss_fallback": 0,
387	    "epochs_completed": 3,
388	    "wall_clock_s": 23418,
389	    "wall_clock_h": 6.5
390	}
391	
392	================================================================================
393	EXPERIMENT: d048_ss_s42_resume
394	================================================================================
395	  Status: PREPARING
396	  Created: 2026-05-22T15:57:05.941Z
397	  Updated: 2026-05-22T15:57:05.941Z
398	  Completed: N/A
399	  Retry count: 0
400	  Spec: {'command': 'bash -c "cd /root/turn_residual_gating && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --batch-size 1 --grad-accum 8 --max-seq-len 2048 --scheduled-sampling --ss-max-ratio 0.3 --seed 42 --epochs 3 --output-dir runs/d048_ss_s42 --data-dir data/ultrachat_8k --resume runs/d048_ss_s42/epoch_0"', 'server': 'westd-20861', 'gpu': ['cuda:0'], 'pid': '32472', 'log_path': '~/runs/turn_residual_gating/d048_ss_s42_resume.log', 'submitted_at': '2026-05-22T15:57:05.791Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root'}
401	
402	================================================================================
403	EXPERIMENT: d048_ss_s456
404	================================================================================
405	  Status: DONE
406	  Created: 2026-05-23T03:46:14.558Z
407	  Updated: 2026-05-24T00:38:35.393Z
408	  Completed: 2026-05-24T00:38:35.393Z
409	  Retry count: 0
410	  Hypothesis: Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s456) to establish 3-seed mean±std for C2 reviewer requirement of at least 3 seeds
411	  Spec: {'command': 'python train_phase2_v8b.py --seed 456 --resume runs/d048_ss_s456/epoch_0 --gate-type threadgate --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --ss-ratio 0.3', 'server': 'westd-20861', 'pid': '112418', 'data_path': '/root/turn-residual-gating/data/phase2_train.jsonl', 'data_count': 2000, 'model_name': 'Qwen/Qwen2.5-7B-Instruct', 'seed': 456, 'gpu': 0, 'checkpoint_source': 'Qwen/Qwen2.5-7B-Instruct (resume from epoch_0)', 'eval_data': 'N/A - training experiment', 'checkpoint_path': '/root/turn-residual-gating/runs/d048_ss_s456/epoch_2', 'log_path': '/root/turn-residual-gating/runs/d048_ss_s456/train.log'}
412	  Conclusion: success
413	
414	================================================================================
415	EXPERIMENT: eval_llama_ar_n20
416	================================================================================
417	  Status: DONE
418	  Created: 2026-05-22T07:52:04.543Z
419	  Updated: 2026-05-22T08:38:33.680Z
420	  Completed: 2026-05-22T08:16:09.384Z
421	  Retry count: 0
422	  Hypothesis: N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) autoregressive GAR estimates. N=5 suffered from outlier influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides robust mean±std.
423	  Spec: {'command': 'bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_ar_n20.sh"', 'server': 'westd-20861', 'gpu': ['cuda:0'], 'pid': '312592', 'log_path': '~/runs/turn_residual_gating/eval_llama_ar_n20.log', 'submitted_at': '2026-05-22T07:52:13.830Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': 'ultrachat_200k + model-gen AR', 'data_count': 20, 'model_name': 'Llama-3.1-8B-Instruct (Base/TG/LoRA-only)', 'seed': 42, 'checkpoint_source': 'llama_tg_s42 + llama_lora_only_s42', 'eval_data': 'AR-generated 20 conversations x 4 turns', 'wall_clock_seconds': 1435.6, 'gpu_hours': 0.4}
424	  Conclusion: success
425	  Metrics:
426	{
427	    "base": {
428	        "gar_ours_mean": 0.0088,
429	        "gar_ours_std": 0.0056,
430	        "gar_ours_median_per_conv": 0.0093,
431	        "gar_ours_median_per_turn_pool": 0.0071,
432	        "gar_ours_spike_ratio": "0%",
433	        "gar_dongre_mean": 0.0049,
434	        "gar_dongre_std": 0.0013,
435	        "gar_dongre_median": 0.0047,
436	        "ngar_ours_mid": 0.1019,
437	        "ngar_dongre_mid": 0.1171,
438	        "ppl": 1.293,
439	        "ppl_std": 0.07,
440	        "ntp_loss": 0.2552
441	    },
442	    "tg": {
443	        "gar_ours_mean": 0.0434,
444	        "gar_ours_std": 0.1002,
445	        "gar_ours_median_per_conv": 0.0179,
446	        "gar_ours_median_per_turn_pool": 0.0126,
447	        "gar_ours_spike_ratio": "5% (2/40 turns GAR>=0.4)",
448	        "gar_dongre_mean": 0.0183,
449	        "gar_dongre_std": 0.0198,
450	        "gar_dongre_median": 0.0152,
451	        "ngar_ours_mid": 0.5357,
452	        "ngar_dongre_mid": 0.4436,
453	        "ppl": 1.437,
454	        "ppl_std": 0.077,
455	        "ntp_loss": 0.3612
456	    },
457	    "lora_only": {
458	        "gar_ours_mean": 0.0284,
459	        "gar_ours_std": 0.0481,
460	        "gar_ours_median_per_conv": 0.0184,
461	        "gar_ours_median_per_turn_pool": 0.0133,
462	        "gar_ours_spike_ratio": "0%",
463	        "gar_dongre_mean": 0.0205,
464	        "gar_dongre_std": 0.0241,
465	        "gar_dongre_median": 0.016,
466	        "ngar_ours_mid": 0.3488,
467	        "ngar_dongre_mid": 0.4997,
468	        "ppl": 1.419,
469	        "ppl_std": 0.075,
470	        "ntp_loss": 0.3483
471	    },
472	    "n_conversations": 20,
473	    "n_turns": 4,
474	    "mid_turns_definition": "turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2). All 16 eval entries use same definition.",
475	    "stat_pool": "median_per_conv: median of 20 per-conversation mid-turn averages. median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).",
476	    "ranking_gar_ours_mean": "TG(0.0434) > LO(0.0284) > Base(0.0088)",
477	    "ranking_gar_ours_median_per_conv": "TG(0.0179) ≈ LO(0.0184) > Base(0.0093)",
478	    "ranking_gar_ours_median_per_turn_pool": "TG(0.0126) ≈ LO(0.0133) > Base(0.0071)",
479	    "ranking_gar_dongre": "LO(0.0205) > TG(0.0183) > Base(0.0049)",
480	    "note": "Paper §5.5 cites median_per_conv (median of per-conversation mid-turn averages across N=20). median_per_turn_pool is the alternative statistic from pooled individual turns. Both confirm TG ≈ LO (zero-increment)."
481	}
482	
483	================================================================================
484	EXPERIMENT: eval_llama_lora_only_s42
485	================================================================================
486	  Status: DONE
487	  Created: 2026-05-22T07:40:25.352Z
488	  Updated: 2026-05-22T07:51:32.758Z
489	  Completed: 2026-05-22T07:51:25.244Z
490	  Retry count: 0
491	  Hypothesis: LoRA-only ablation (no gate) on Llama-3.1-8B: if TG's GAR improvement comes from the gate, LoRA-only should show minimal GAR recovery vs base.
492	  Spec: {'command': 'bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_lora_only_s42.sh"', 'server': 'westd-20861', 'gpu': ['cuda:0'], 'pid': '309670', 'log_path': '/root/runs/turn_residual_gating/eval_llama_lora_only_s42.log', 'submitted_at': '2026-05-22T07:40:34.437Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': 'ultrachat_200k + model-gen', 'data_count': 55, 'model_name': 'Llama-3.1-8B-Instruct + LoRA-only checkpoint', 'seed': 42, 'checkpoint_source': 'llama_lora_only_s42', 'eval_data': 'IID heldout 50 + model-gen 5', 'checkpoint_path': 'runs/phase2_llama_lora_only_s42/epoch_2', 'wall_clock_seconds': 650.8, 'gpu_hours': 0.18}
493	  Conclusion: success
494	  Metrics:
495	{
496	    "tf": {
497	        "gar_ours": 0.4807,
498	        "gar_dongre": 0.0188,
499	        "ngar_ours": 11.8031,
500	        "ngar_dongre": 0.8261,
501	        "ppl": 2.6,
502	        "ntp_loss": 0.9366,
503	        "n_conversations": 50,
504	        "n_turns": 4
505	    },
506	    "ar": {
507	        "gar_ours": 0.0617,
508	        "gar_dongre": 0.0226,
509	        "ngar_ours": 0.6065,
510	        "ngar_dongre": 0.2537,
511	        "ppl": 1.32,
512	        "ntp_loss": 0.2787,
513	        "n_conversations": 5,
514	        "n_turns": 10
515	    },
516	    "gap_ratio_gar_ours": 7.79
517	}
518	
519	================================================================================
520	EXPERIMENT: eval_v7_tg_s123
521	================================================================================
522	  Status: DONE
523	  Created: 2026-05-21T22:53:18.163Z
524	  Updated: 2026-05-22T00:30:49.653Z
525	  Completed: 2026-05-22T00:30:42.606Z
526	  Retry count: 0
527	  Hypothesis: v7 TG s123 eval: 验证 s123 seed 的 TF-AR GAR gap 与 s42 一致（~32×），确认 multi-seed robustness
528	  Spec: {'command': 'bash scripts/eval_v7_tg_s123.sh', 'server': 'westd-20861', 'gpu': ['cuda:0'], 'pid': '264869', 'log_path': '/root/turn_residual_gating/logs/v7_tg_s123.log', 'submitted_at': '2026-05-21T22:53:18.065Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': 'data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 123, 'checkpoint_source': 'v7_tg_s123', 'eval_data': 'data/ultrachat_8k', 'checkpoint_path': '/root/turn_residual_gating/runs/phase2_tg_s123_v7/epoch_2', 'wall_clock_seconds': 5844.5, 'gpu_hours': 1.62}
529	  Conclusion: success
530	  Metrics:
531	{
532	    "iid_tf": {
533	        "gar_ours_mid": 0.5052,
534	        "gar_dongre_mid": 0.0119,
535	        "ppl": 2.7802,
536	        "ntp": 0.9752
537	    },
538	    "modelgen_ar": {
539	        "gar_ours_mid": 0.0165,
540	        "gar_dongre_mid": 0.0177,
541	        "ppl": 1.3855,
542	        "ntp": 0.3223
543	    },
544	    "gap_ratio": 30.6,
545	    "comparison_s42": {
546	        "tf_gar_ours_delta": 0.0017,
547	        "ar_gar_ours_delta": 0.0008,
548	        "gap_ratio_delta": -1.4
549	    }
550	}
551	
552	================================================================================
553	EXPERIMENT: eval_v8b_ss
554	================================================================================
555	  Status: DONE
556	  Created: 2026-05-20T18:44:23.366Z
557	  Updated: 2026-05-20T18:45:14.523Z
558	  Completed: 2026-05-20T18:45:14.523Z
559	  Retry count: 0
560	  Hypothesis: Scheduled Sampling (linear 0→0.5 mixing of teacher-forced and model-gen contexts) closes the 30x training-inference GAR gap by reducing exposure bias, resulting in model-gen GAR significantly above v7 baseline (0.016) while preserving IID GAR and PPL.
561	  Spec: {'command': 'python src/eval_phase2_gar.py --checkpoint-dir checkpoints/tg_v8b_ss_fixed_s42 --gate-type threadgate', 'server': 'westd-20861', 'data_path': 'data/ultrachat_eval_heldout.json + built-in 5conv model-gen', 'data_count': '50 heldout + 5 model-gen', 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_source': 'checkpoints/tg_v8b_ss_fixed_s42', 'eval_data': 'ultrachat_eval_heldout.json (IID) + built-in model-gen (5x10 turns)', 'checkpoint_path': 'checkpoints/tg_v8b_ss_fixed_s42', 'log_path': '/tmp/eval_v8b_all.log'}
562	  Conclusion: success
563	  Metrics:
564	{
565	    "iid_gar_ours": 0.4983,
566	    "iid_gar_dongre": 0.3855,
567	    "iid_ppl": 2.78,
568	    "iid_ngar_ours": 13.5,
569	    "iid_ngar_dongre": 22.68,
570	    "modelgen_gar_ours": 0.3177,
571	    "modelgen_gar_dongre": 0.3533,
572	    "modelgen_ppl": 1.38,
573	    "modelgen_ngar_ours": 4.47,
574	    "modelgen_ngar_dongre": 5.92,
575	    "iid_turn1_gar_ours": 0.5398,
576	    "modelgen_turn1_gar_ours": 0.4333
577	}
578	
579	================================================================================
580	EXPERIMENT: eval_v8b_ss_s123
581	================================================================================
582	  Status: DONE
583	  Created: 2026-05-21T21:15:52.880Z
584	  Updated: 2026-05-21T22:53:15.356Z
585	  Completed: 2026-05-21T22:53:08.443Z
586	  Retry count: 0
587	  Hypothesis: v8b SS model trained with s123 seed should reproduce s42 GAR metrics within acceptable gap_ratio [1.2x-2.5x] and no PPL degradation, confirming seed robustness of the scheduled sampling approach
588	  Spec: {'command': 'bash scripts/eval_v8b_ss_s123.sh', 'server': 'westd-20861', 'gpu': ['cuda:0'], 'pid': 259767, 'log_path': 'runs/eval_v8b_ss_s123/', 'submitted_at': '2026-05-21T21:15:52.785Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': 'data/ultrachat_eval_heldout.json', 'data_count': 50, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 123, 'gpu_index': 0, 'checkpoint_source': 'checkpoints/tg_v8b_ss_s123/epoch_2', 'eval_data': 'ultrachat_eval_heldout + model-gen', 'checkpoint_path': 'checkpoints/tg_v8b_ss_s123/epoch_2', 'wall_clock_seconds': 5835.7, 'gpu_hours': 1.62}
589	  Conclusion: success
590	  Metrics:
591	{
592	    "iid": {
593	        "gar_ours": 0.503,
594	        "gar_dongre": 0.394,
595	        "ppl": 2.781,
596	        "ntp_loss": 0.976,
597	        "n_conv": 50,
598	        "n_turns": 3
599	    },
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12eeb278-0c56-47c4-82fe-04ae77ae930b",
  "isSidechain": true,
  "promptId": "46b2b0c6-9613-417a-9397-99622f342526",
  "agentId": "a8867062004a08a3c",
  "type": "user",
  "uuid": "97015cee-4931-4006-a797-56bfae1f2a3c",
  "sourceToolAssistantUUID": "12eeb278-0c56-47c4-82fe-04ae77ae930b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-24T15:08:02.840Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D4nXjb79p5p8ktsJPd1ihb`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt",
  "limit": 300,
  "offset": 600
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97015cee-4931-4006-a797-56bfae1f2a3c",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbxpv7R6ZLGv9ej9NX7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8686ea0e-99fa-4ea4-bc41-ba12b266a73b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0135VKidUsLhbKz6GPfsSfid",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7856,
      "cache_read_input_tokens": 29577,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7856
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 29577,
          "cache_creation_input_tokens": 7856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7856,
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

_source line 32 · 2026-05-24T15:08:02.847Z_

<details><summary>↩ Tool result · `toolu_01D4nXjb79p5p8ktsJPd1ihb`</summary>

```text
600	    "modelgen": {
601	        "gar_ours": 0.418,
602	        "gar_dongre": 0.441,
603	        "ppl": 1.389,
604	        "ntp_loss": 0.325,
605	        "n_conv": 5,
606	        "n_turns": 10
607	    },
608	    "gap_ratio": 1.2,
609	    "base_iid_ppl": 4.338,
610	    "base_modelgen_ppl": 1.351
611	}
612	
613	================================================================================
614	EXPERIMENT: instruction_retention_test
615	================================================================================
616	  Status: DONE
617	  Created: 2026-05-21T03:49:26.068Z
618	  Updated: 2026-05-21T03:59:31.835Z
619	  Completed: 2026-05-21T03:59:31.835Z
620	  Retry count: 0
621	  Hypothesis: Turn-level residual gating (β=3) preserves instruction-following ability across multi-turn conversations better than the baseline (β=0), because gating modulates residual contributions to retain earlier context signals rather than letting them decay through successive transformer layers.
622	  Spec: {'command': 'python src/eval_instruction_retention.py --checkpoint runs/phase2_tg_s42_v7 --prompts data/instruction_retention_prompts.json --betas 0 3 --seed 42 --output results/instruction_retention.json', 'server': 'westd-20861', 'data_path': 'data/instruction_retention_prompts.json', 'data_count': 18, 'model_name': 'Qwen2.5-7B-Instruct + v7 TG LoRA', 'seed': 42, 'checkpoint_source': 'phase2_tg_s42_v7', 'eval_data': '18 instruction retention prompts, beta=[0,3], 5 turns each'}
623	  Conclusion: success
624	  Metrics:
625	{
626	    "late_turn_rate_beta0": 0.759,
627	    "late_turn_rate_beta3": 0.87,
628	    "late_turn_delta": 0.111,
629	    "mcnemar_chi2": 3.125,
630	    "mcnemar_p": 0.0771,
631	    "gar_compliance_r": 0.2003,
632	    "gar_compliance_p": 0.007,
633	    "category_content_constraint": {
634	        "beta0": 0.619,
635	        "beta3": 0.857,
636	        "delta": 0.238
637	    },
638	    "category_count_constraint": {
639	        "beta0": 1,
640	        "beta3": 1,
641	        "delta": 0
642	    },
643	    "category_format_constraint": {
644	        "beta0": 1,
645	        "beta3": 1,
646	        "delta": 0
647	    },
648	    "category_position_constraint": {
649	        "beta0": 0.667,
650	        "beta3": 0.733,
651	        "delta": 0.067
652	    }
653	}
654	
655	================================================================================
656	EXPERIMENT: llama_ar_matched_eval
657	================================================================================
658	  Status: DONE
659	  Created: 2026-05-21T03:59:40.918Z
660	  Updated: 2026-05-21T04:36:23.237Z
661	  Completed: 2026-05-21T04:28:38.504Z
662	  Retry count: 0
663	  Hypothesis: 用 matched 设置 (N=50/T=4) 重跑 Llama AR eval，消除 TF/AR 设置差异。与 TF 结果对比得到可直接写入论文的 gap ratio，验证 TG 在 AR 模式下仍能提升 GAR。
664	  Spec: {'command': 'bash scripts/eval_llama_ar_matched.sh', 'server': 'westd-20861', 'data_path': 'data/ultrachat_eval_sample.json', 'data_count': 50, 'model_name': 'Meta-Llama-3.1-8B-Instruct + TG LoRA', 'seed': 42, 'checkpoint_source': 'phase2_llama_tg_s42', 'eval_data': '50 UltraChat convs, T=4, AR generation, 4 conditions (base/TG x ours/Dongre)', 'checkpoint_path': 'N/A (eval)', 'log_path': 'runs/eval_llama_ar_matched.log'}
665	  Conclusion: success
666	  Metrics:
667	{
668	    "ar_base_ours": {
669	        "mid_gar": 0.0082,
670	        "ngar": 0.1,
671	        "ppl": 1.267
672	    },
673	    "ar_tg_ours": {
674	        "mid_gar": 0.0388,
675	        "ngar": 0.493,
676	        "ppl": 1.413
677	    },
678	    "ar_base_dongre": {
679	        "mid_gar": 0.0051,
680	        "ngar": 0.12,
681	        "ppl": 1.267
682	    },
683	    "ar_tg_dongre": {
684	        "mid_gar": 0.018,
685	        "ngar": 0.431,
686	        "ppl": 1.413
687	    },
688	    "tf_reference": {
689	        "tf_tg_ours_ngar": 11.88,
690	        "tf_base_ours_ngar": 0.388,
691	        "tf_tg_ours_raw": 0.4836,
692	        "tf_tg_dongre_raw": 0.018
693	    },
694	    "matched_gap_analysis": {
695	        "gar_ours_raw_gap": "12.5x (TF 0.484 / AR 0.039)",
696	        "gar_ours_ngar_gap": "24.1x (TF 11.88 / AR 0.493)",
697	        "gar_dongre_raw_gap": "1.002x (TF 0.018 / AR 0.018) — zero gap",
698	        "tg_over_base_ar_ours": "4.71x",
699	        "tg_over_base_ar_dongre": "3.54x",
700	        "conclusion": "GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure bias selectively destroys learned goal-attention routing while leaving content-overlap-based attention unaffected."
701	    }
702	}
703	
704	================================================================================
705	EXPERIMENT: llama_eval_s42
706	================================================================================
707	  Status: DONE
708	  Created: 2026-05-21T03:29:51.255Z
709	  Updated: 2026-05-21T03:46:58.167Z
710	  Completed: 2026-05-21T03:46:58.167Z
711	  Retry count: 0
712	  Hypothesis: Llama-3.1-8B TG eval: 如果 Llama TG 模型在 TF 模式下 GAR-ours 显著高于 AR 模式（如 Qwen v7 的 20-33x gap），则确认 training-inference GAR gap 跨模型泛化（C5）。同时测量 base model 作为 control。
713	  Spec: {'command': 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_tg_s42.sh 2>&1 | tee runs/eval_llama_tg_s42.log', 'server': 'westd-20861', 'data_path': 'data/ultrachat_eval_sample.json', 'data_count': 50, 'model_name': 'Llama-3.1-8B-Instruct', 'seed': 42, 'checkpoint_source': 'runs/phase2_llama_tg_s42/epoch_2', 'eval_data': 'ultrachat_eval_sample'}
714	  Conclusion: success
715	  Metrics:
716	{
717	    "tf_base": {
718	        "gar_ours": 0.0166,
719	        "ngar_ours": 0.3882,
720	        "gar_dongre": 0.0038,
721	        "ngar_dongre": 0.163,
722	        "ppl": 3.45,
723	        "N": 50,
724	        "T": 4
725	    },
726	    "tf_tg": {
727	        "gar_ours": 0.4836,
728	        "ngar_ours": 11.8818,
729	        "gar_dongre": 0.018,
730	        "ngar_dongre": 0.7922,
731	        "ppl": 2.57,
732	        "N": 50,
733	        "T": 4
734	    },
735	    "ar_base": {
736	        "gar_ours": 0.0086,
737	        "ngar_ours": 0.0798,
738	        "gar_dongre": 0.0118,
739	        "ngar_dongre": 0.1265,
740	        "ppl": 1.24,
741	        "N": 5,
742	        "T": 10
743	    },
744	    "ar_tg": {
745	        "gar_ours": 0.0304,
746	        "ngar_ours": 0.2632,
747	        "gar_dongre": 0.0217,
748	        "ngar_dongre": 0.2459,
749	        "ppl": 1.32,
750	        "N": 5,
751	        "T": 10
752	    },
753	    "gap_ratio_tg_ours": 15.9,
754	    "gap_ratio_base_ours": 1.93,
755	    "gap_ratio_tg_dongre": 0.83,
756	    "vs_qwen_v7_gap_ratio": 32.1,
757	    "baseline_mid_gar": 0.0122
758	}
759	
760	================================================================================
761	EXPERIMENT: llama_lora_only_s42
762	================================================================================
763	  Status: DONE
764	  Created: 2026-05-22T00:33:03.465Z
765	  Updated: 2026-05-22T07:39:06.888Z
766	  Completed: 2026-05-22T07:39:06.889Z
767	  Retry count: 0
768	  Hypothesis: Llama-3.1-8B LoRA-only baseline (gate=none, 无 gating 机制): 与 Llama TG s42 对比，验证 gating 对 Llama 的增量贡献。如果 LoRA-only GAR ≈ TG GAR → gating 零增量与 Qwen 结论一致（C5 跨模型）。
769	  Spec: {'command': 'bash scripts/launch_llama_lora_only_s42.sh', 'server': 'westd-20861', 'gpu': ['cuda:0'], 'pid': '271741', 'log_path': 'logs/llama_lora_only_s42.log', 'submitted_at': '2026-05-22T00:33:16.591Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': '/root/turn_residual_gating/data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Meta-Llama-3.1-8B-Instruct', 'seed': 42, 'checkpoint_source': 'N/A (training from scratch, ablation baseline)', 'eval_data': 'N/A (training run, not eval)', 'checkpoint_path': 'runs/phase2_llama_lora_only_s42/epoch_2', 'wall_clock_seconds': 25550.3, 'gpu_hours': 7.1}
770	  Conclusion: success
771	  Metrics:
772	{
773	    "final_avg_loss": 0.9288,
774	    "final_avg_ntp": 0.9279,
775	    "final_avg_gar": 0.0009,
776	    "gate_fixed": 1,
777	    "gate_type": "none",
778	    "wall_clock_s": 25317,
779	    "wall_clock_h": 7.03,
780	    "epochs_completed": 3
781	}
782	
783	================================================================================
784	EXPERIMENT: llama_phase1_gar_diag
785	================================================================================
786	  Status: DONE
787	  Created: 2026-05-20T19:39:25.751Z
788	  Updated: 2026-05-21T01:34:36.417Z
789	  Completed: 2026-05-21T01:34:36.417Z
790	  Retry count: 0
791	  Hypothesis: Llama-3.1-8B-Instruct 在 multi-turn dialogue 中也应出现 goal attention decay（与 Qwen-2.5-7B 类似），确认 attention decay 是 transformer 架构通用现象而非模型特有。Phase 1 诊断：测量 base Llama 的 per-turn GAR profile。
792	  Spec: {'server': 'westd-20861', 'gpu': ['cuda:0'], 'account': 'local', 'command': 'CUDA_VISIBLE_DEVICES=0 python src/run_phase1_gar_llama.py --model /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/ --output-dir /root/turn_residual_gating/runs/phase1_llama_gar_diag --max-new-tokens 256', 'pid': '198817', 'data_path': 'built-in 5 conversations (knowledge_qa, coding_help, creative_writing, math_reasoning, debate)', 'data_count': 5, 'model_name': 'Meta-Llama-3.1-8B-Instruct', 'seed': 42, 'checkpoint_source': 'N/A (base model, no fine-tuning)', 'eval_data': '5 built-in conversations x 10 turns each, gen mode', 'checkpoint_path': 'N/A', 'log_path': '/root/turn_residual_gating/logs/llama_phase1_gar_diag.log'}
793	  Conclusion: success
794	  Metrics:
795	{
796	    "per_turn_gar": {
797	        "turn_1": 0.0263,
798	        "turn_2": 0.0183,
799	        "turn_3": 0.0087,
800	        "turn_4": 0.0055,
801	        "turn_5": 0.006,
802	        "turn_6": 0.0035,
803	        "turn_7": 0.0038,
804	        "turn_8": 0.0037,
805	        "turn_9": 0.005,
806	        "turn_10": 0.0026
807	    },
808	    "t1_t10_decay_pct": 90.1,
809	    "t1_mid38_drop_pct": 80.2,
810	    "n_topics": 5,
811	    "model": "Meta-Llama-3.1-8B-Instruct",
812	    "mode": "gen",
813	    "n_conversations": 5,
814	    "n_turns": 10
815	}
816	
817	================================================================================
818	EXPERIMENT: llama_tg_s42
819	================================================================================
820	  Status: DONE
821	  Created: 2026-05-21T01:34:36.906Z
822	  Updated: 2026-05-21T03:28:07.022Z
823	  Completed: 2026-05-21T03:27:55.963Z
824	  Retry count: 0
825	  Hypothesis: 在 Llama-3.1-8B-Instruct 上训练 ThreadGate（与 Qwen v7 相同配置），验证 C5：gating mechanism 和 GAR training-inference gap 跨模型泛化。如果 Llama TG 也出现 IID GAR ≈ target 但 model-gen GAR 坍塌 → 确认 exposure bias 的跨模型通用性。
826	  Spec: {'command': 'CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 python src/train_phase2.py --model /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct --data-dir data/ultrachat_8k --output-dir runs/phase2_llama_tg_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42', 'server': 'westd-20861', 'gpu': ['cuda:0'], 'pid': '199643', 'data_path': 'data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Meta-Llama-3.1-8B-Instruct', 'seed': 42, 'checkpoint_source': 'N/A (training from scratch)', 'eval_data': 'N/A (training experiment)', 'checkpoint_path': '/root/turn_residual_gating/runs/phase2_llama_tg_s42', 'log_path': '/root/turn_residual_gating/logs/llama_tg_training.log'}
827	  Conclusion: success
828	  Metrics:
829	{
830	    "epochs_completed": 3,
831	    "total_steps": 3000,
832	    "wall_clock_seconds": 26212,
833	    "wall_clock_hours": 7.28,
834	    "final_avg_loss": 0.9233,
835	    "final_avg_ntp": 0.9224,
836	    "final_avg_gar": 0.0009,
837	    "final_avg_div": 0,
838	    "final_gate_mean": 0.9099,
839	    "final_gate_std": 0.0701,
840	    "final_gate_min": 0.7188,
841	    "final_gate_max": 0.9922,
842	    "gate_profile_step3000": {
843	        "L0": 0.957,
844	        "L1": 0.973,
845	        "L2": 0.977,
846	        "L3": 0.965,
847	        "L4": 0.992,
848	        "L5": 0.969,
849	        "L6": 0.957,
850	        "L7": 0.957,
851	        "L8": 0.961,
852	        "L9": 0.949,
853	        "L10": 0.938,
854	        "L11": 0.934,
855	        "L12": 0.969,
856	        "L13": 0.953,
857	        "L14": 0.957,
858	        "L15": 0.965,
859	        "L16": 0.953,
860	        "L17": 0.961,
861	        "L18": 0.922,
862	        "L19": 0.902,
863	        "L20": 0.883,
864	        "L21": 0.863,
865	        "L22": 0.836,
866	        "L23": 0.844,
867	        "L24": 0.809,
868	        "L25": 0.719,
869	        "L26": 0.762,
870	        "L27": 0.805,
871	        "L28": 0.801,
872	        "L29": 0.855,
873	        "L30": 0.898,
874	        "L31": 0.934
875	    },
876	    "checkpoint_size_gate_mb": 4.2,
877	    "checkpoint_size_lora_mb": 26,
878	    "gpu": "NVIDIA RTX PRO 6000 Blackwell",
879	    "vram_gb": 102,
880	    "mem_used_gb": 63.4
881	}
882	
883	================================================================================
884	EXPERIMENT: llama_tg_training
885	================================================================================
886	  Status: PREPARING
887	  Created: 2026-05-21T03:37:31.513Z
888	  Updated: 2026-05-21T09:44:18.859Z
889	  Completed: N/A
890	  Retry count: 0
891	  Conclusion: failed
892	
893	================================================================================
894	EXPERIMENT: mmlu_eval_all
895	================================================================================
896	  Status: DONE
897	  Created: 2026-05-23T06:45:04.153Z
898	  Updated: 2026-05-24T07:23:08.289Z
899	  Completed: 2026-05-24T06:53:52.873Z
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8686ea0e-99fa-4ea4-bc41-ba12b266a73b",
  "isSidechain": true,
  "promptId": "46b2b0c6-9613-417a-9397-99622f342526",
  "agentId": "a8867062004a08a3c",
  "type": "user",
  "uuid": "20110a41-8db9-4445-b412-310f89690e4d",
  "sourceToolAssistantUUID": "8686ea0e-99fa-4ea4-bc41-ba12b266a73b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-24T15:08:12.553Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GYkMqm45j59JNic68YsyWm`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt",
  "limit": 300,
  "offset": 900
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20110a41-8db9-4445-b412-310f89690e4d",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbyGMpDSkJdZXTPzt68",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a53682e4-fb07-4dcd-a5d5-33cfa6509ad4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKca8Fuk5qVApU11xccXsg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6120,
      "cache_read_input_tokens": 37433,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6120
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 37433,
          "cache_creation_input_tokens": 6120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6120,
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

_source line 34 · 2026-05-24T15:08:12.558Z_

<details><summary>↩ Tool result · `toolu_01GYkMqm45j59JNic68YsyWm`</summary>

```text
900	  Retry count: 0
901	  Hypothesis: ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.
902	  Spec: {'command': 'python eval_mmlu.py --model_path &lt;checkpoint> --n_shot 5', 'server': 'westd-20861', 'data_path': 'MMLU benchmark (5-shot)', 'data_count': 14042, 'model_name': 'Qwen/Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_source': 'base/lo/ug/tg/pcgrad/ss checkpoints', 'eval_data': 'MMLU 5-shot', 'checkpoint_path': 'results/mmlu/', 'log_path': 'logs/gpu_chain_next.log'}
903	  Conclusion: success
904	  Metrics:
905	{
906	    "base_qwen": 0.7423,
907	    "pcgrad_v9_s42": 0.7386,
908	    "ss_v8b_s42": 0.7375,
909	    "lo_s42": 0.7357,
910	    "tg_v7_s42": 0.7347,
911	    "ug_s42": 0.7346
912	}
913	
914	================================================================================
915	EXPERIMENT: p0_ss_steering_eval
916	================================================================================
917	  Status: PREPARING
918	  Created: 2026-05-23T19:37:39.883Z
919	  Updated: 2026-05-23T19:57:38.851Z
920	  Completed: N/A
921	  Retry count: 0
922	  Hypothesis: SS training provides AR GAR ~0.385, steering alone gives 0.717. Combining SS checkpoint with beta-steering at inference may approach TF parity (~0.50), demonstrating that SS+steering is a constructive mitigation stack for the TF-AR gap.
923	  Conclusion: killed
924	
925	================================================================================
926	EXPERIMENT: p1_llama_ss_training
927	================================================================================
928	  Status: RUNNING
929	  Created: 2026-05-23T19:37:48.689Z
930	  Updated: 2026-05-24T07:21:06.008Z
931	  Completed: N/A
932	  Retry count: 0
933	  Hypothesis: SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims.
934	  Spec: {'command': 'bash scripts/p1_llama_ss_train.sh', 'server': 'westd-20861', 'data_path': '/root/turn-residual-gating/data/train_400.json', 'data_count': 400, 'model_name': 'meta-llama/Llama-3.1-8B-Instruct', 'seed': 42, 'checkpoint_path': 'runs/llama_ss_s42/', 'log_path': 'logs/p1_llama_ss_training.log', 'pid': 158507, 'hyperparams': {'lr': '2e-4', 'batch_size': 1, 'grad_accum': 8, 'epochs': 3, 'ss_max_ratio': 0.3, 'lora_rank': 16}}
935	
936	================================================================================
937	EXPERIMENT: p1_tf_ar_kl_divergence
938	================================================================================
939	  Status: DONE
940	  Created: 2026-05-23T19:37:46.355Z
941	  Updated: 2026-05-24T07:18:10.268Z
942	  Completed: 2026-05-24T07:18:06.521Z
943	  Retry count: 0
944	  Hypothesis: TF and AR attention distributions diverge more on GAR-relevant heads (high gate values) than non-relevant heads, providing mechanistic evidence that exposure bias selectively disrupts goal-attending computation rather than uniformly degrading attention.
945	  Spec: {'command': 'python scripts/p1_kl_divergence.py', 'server': 'westd-20861', 'data_path': '/root/turn_residual_gating/data/eval_200.json', 'data_count': 30, 'model_name': 'Qwen/Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_path': 'results/p1_kl_perhead/', 'log_path': 'logs/p1_kl_divergence_step2.log'}
946	  Conclusion: success
947	  Metrics:
948	{
949	    "tg_delta_gar": 0.0165,
950	    "base_delta_gar": 0.0122,
951	    "tg_mean_kl": 0.054,
952	    "base_mean_kl": 0.043,
953	    "gate_kl_correlation": 0.11,
954	    "high_kl_layers": "L23-L27, L9",
955	    "gar_robustness_ours_tg_base_ratio": 21.4,
956	    "gar_robustness_goal_only_ratio": 63,
957	    "gar_robustness_ours_all_ratio": 1.7,
958	    "gar_robustness_ours_first_ratio": 1.8
959	}
960	
961	================================================================================
962	EXPERIMENT: p2_llama_gradient_conflict
963	================================================================================
964	  Status: DONE
965	  Created: 2026-05-23T19:37:50.492Z
966	  Updated: 2026-05-24T07:20:28.248Z
967	  Completed: 2026-05-24T07:20:28.248Z
968	  Retry count: 0
969	  Hypothesis: PCGrad fails to improve AR GAR on Llama-3.1-8B (as on Qwen), confirming cross-model that gradient conflict is not the root cause of the TF-AR gap, strengthening C2 (causal exclusion).
970	  Spec: {'command': 'bash scripts/p2_llama_gradient_conflict.sh', 'server': 'westd-20861', 'data_path': '/root/turn-residual-gating/data/train_400.json', 'data_count': 400, 'model_name': 'meta-llama/Llama-3.1-8B-Instruct', 'seed': 42, 'checkpoint_path': 'results/p2_llama_gradient_conflict/', 'log_path': 'logs/p2_llama_gradient_conflict.log'}
971	  Conclusion: success
972	  Metrics:
973	{
974	    "cos_sim_mean": 0.0045,
975	    "cos_sim_std": 0.07,
976	    "neg_cos_sim_layers_pct": 53.1,
977	    "mag_ratio_median": 25.7,
978	    "conclusion_note": "cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading — actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern."
979	}
980	
981	================================================================================
982	EXPERIMENT: phase1_gar_diag
983	================================================================================
984	  Status: DONE
985	  Created: 2026-05-18T05:24:07.903Z
986	  Updated: 2026-05-18T05:59:25.324Z
987	  Completed: 2026-05-18T05:59:25.325Z
988	  Retry count: 0
989	  Hypothesis: Qwen2.5-7B-Instruct 在 10-turn 多轮对话中，中间 turns (3-8) 的 GAR (Goal Accessibility Ratio) 相对 turn-1 下降 ≥15%，表明模型对 system prompt 中目标 token 的注意力随对话进行显著衰减
990	  Spec: {'command': 'python run_phase1_gar.py --results-dir /root/turn_residual_gating/results', 'server': 'westd-20861', 'model_name': 'Qwen/Qwen2.5-7B-Instruct', 'data_path': 'built-in 5 conversations (knowledge_qa, coding_help, creative_writing, math_reasoning, roleplay_advisor)', 'data_count': 5, 'seed': 0, 'checkpoint_path': 'N/A', 'log_path': '/root/turn_residual_gating/results/phase1_run.log'}
991	  Conclusion: success
992	  Metrics:
993	{
994	    "turn1_avg_gar": 0.0418,
995	    "mid_turns_avg_gar": 0.0122,
996	    "relative_drop": 0.708,
997	    "num_conversations": 5,
998	    "num_turns": 10,
999	    "per_turn_avg_gar": [
1000	        0.0418,
1001	        0.0241,
1002	        0.0224,
1003	        0.013,
1004	        0.0133,
1005	        0.0086,
1006	        0.0078,
1007	        0.008,
1008	        0.0157,
1009	        0.0064
1010	    ]
1011	}
1012	
1013	================================================================================
1014	EXPERIMENT: phase2_4way_eval
1015	================================================================================
1016	  Status: DONE
1017	  Created: 2026-05-19T13:07:30.673Z
1018	  Updated: 2026-05-19T13:15:39.947Z
1019	  Completed: 2026-05-19T13:15:04.405Z
1020	  Retry count: 0
1021	  Hypothesis: Turn-residual gating (TRG) improves multi-turn response quality over LoRA-only and base model baselines because it selectively amplifies conversational context signals, which should manifest as higher GAR scores across 4 conditions (base, base+TRG, LoRA, LoRA+TRG).
1022	  Spec: {'command': 'bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/run_4way_eval.sh 2>&1 | tee runs/4way_eval.log"', 'server': 'westd-20861', 'gpu': ['cuda:0'], 'pid': '60024', 'log_path': '/root/turn_residual_gating/runs/4way_eval.log', 'submitted_at': '2026-05-19T13:07:37.380Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': '/root/turn_residual_gating/data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_source': 'phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42', 'eval_data': 'ultrachat_8k eval split', 'checkpoint_path': '/root/turn_residual_gating/runs/4way_eval/', 'wall_clock_seconds': 447.0, 'gpu_hours': 0.12}
1023	  Conclusion: negative
1024	  Metrics:
1025	{
1026	    "base_ours_mid_gar": 0.0107,
1027	    "base_ours_recovery_pp": -0.15,
1028	    "base_dongre_mid_gar": 0.003,
1029	    "base_dongre_recovery_pp": -0.92,
1030	    "base_ppl": 4.23,
1031	    "base_ntp": 1.4162,
1032	    "tg_ours_mid_gar": 0.4866,
1033	    "tg_ours_recovery_pp": 47.44,
1034	    "tg_dongre_mid_gar": 0.0157,
1035	    "tg_dongre_recovery_pp": 0.35,
1036	    "tg_ppl": 2.63,
1037	    "tg_ntp": 0.9484,
1038	    "ug_ours_mid_gar": 0.4923,
1039	    "ug_ours_recovery_pp": 48.01,
1040	    "ug_dongre_mid_gar": 0.013,
1041	    "ug_dongre_recovery_pp": 0.08,
1042	    "ug_ppl": 2.62,
1043	    "ug_ntp": 0.9433,
1044	    "lora_ours_mid_gar": 0.486,
1045	    "lora_ours_recovery_pp": 47.39,
1046	    "lora_dongre_mid_gar": 0.0137,
1047	    "lora_dongre_recovery_pp": 0.15,
1048	    "lora_ppl": 2.63,
1049	    "lora_ntp": 0.9482,
1050	    "route_b_confirmed": true,
1051	    "gating_incremental_benefit": "none"
1052	}
1053	
1054	================================================================================
1055	EXPERIMENT: phase2_4way_eval_heldout
1056	================================================================================
1057	  Status: DONE
1058	  Created: 2026-05-19T13:58:59.269Z
1059	  Updated: 2026-05-19T14:35:47.201Z
1060	  Completed: 2026-05-19T14:35:47.202Z
1061	  Retry count: 0
1062	  Hypothesis: 四路消融的三路趋同结论（TG≈UG≈LoRA-only，gating 零增量）在 held-out eval 数据（idx≥8000，与训练集无重叠）上复现，排除数据重叠 confound。预期：相对比较保持（三路趋同），绝对 GAR 值可能变化。
1063	  Spec: {'command': 'bash -c "cd /root/turn_residual_gating && bash scripts/run_4way_eval_heldout.sh"', 'server': 'westd-20861', 'gpu': 'cuda:0', 'pid': 67204, 'log_path': '~/runs/turn_residual_gating/phase2_4way_eval_heldout.log', 'submitted_at': '2026-05-19T14:01:00.965Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': '/root/turn_residual_gating/data/ultrachat_eval_heldout.json', 'data_count': 50, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_source': 'phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42', 'eval_data': 'ultrachat_eval_heldout.json (50 convs, idx 8843-68199, no overlap with training 0-7999)', 'configs': '4 models (Base/TG_v7/UG/LoRA-only) x 2 GAR variants (ours/Dongre) = 8 eval runs', 'checkpoint_path': 'N/A (eval-only)', 'wall_clock_seconds': 2086.2, 'gpu_hours': 0.58}
1064	  Conclusion: success
1065	  Metrics:
1066	{
1067	    "base_ours_mid_gar": 0.0128,
1068	    "base_ours_recovery_pp": 0.06,
1069	    "base_dongre_mid_gar": 0.0031,
1070	    "base_dongre_recovery_pp": -0.91,
1071	    "base_ppl": 4.34,
1072	    "base_ntp": 1.4045,
1073	    "tg_ours_mid_gar": 0.5035,
1074	    "tg_ours_recovery_pp": 49.13,
1075	    "tg_dongre_mid_gar": 0.0152,
1076	    "tg_dongre_recovery_pp": 0.3,
1077	    "tg_ppl": 2.78,
1078	    "tg_ntp": 0.9771,
1079	    "ug_ours_mid_gar": 0.5053,
1080	    "ug_ours_recovery_pp": 49.31,
1081	    "ug_dongre_mid_gar": 0.0124,
1082	    "ug_dongre_recovery_pp": 0.02,
1083	    "ug_ppl": 2.78,
1084	    "ug_ntp": 0.9752,
1085	    "lora_ours_mid_gar": 0.4978,
1086	    "lora_ours_recovery_pp": 48.56,
1087	    "lora_dongre_mid_gar": 0.0132,
1088	    "lora_dongre_recovery_pp": 0.1,
1089	    "lora_ppl": 2.78,
1090	    "lora_ntp": 0.9771,
1091	    "three_way_convergence_confirmed": true,
1092	    "gar_ours_spread_pp": 0.75,
1093	    "ppl_spread": 0,
1094	    "data_overlap": false
1095	}
1096	
1097	================================================================================
1098	EXPERIMENT: phase2_lora_only_s42
1099	================================================================================
1100	  Status: DONE
1101	  Created: 2026-05-18T20:36:32.506Z
1102	  Updated: 2026-05-20T02:15:18.992Z
1103	  Completed: 2026-05-19T12:44:29.475Z
1104	  Retry count: 1
1105	  Hypothesis: LoRA-only baseline (gate 固定 1.0，无 gating 机制) 在相同 MSE+NTP loss 下 GAR 应低于 ThreadGate (v7)。如果 LoRA-only 也能训到 GAR~0.5，则 gating 机制贡献为零，paper story 不成立。关键对比：LoRA-only 的 GAR 收敛值 vs v7 的 0.48。
1106	  Spec: {'command': 'bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type lora_only --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 0.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_lora_only_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3"', 'server': 'westd-20861', 'gpu': 'cuda:0', 'data_path': '/root/turn_residual_gating/data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_path': '/root/turn_residual_gating/runs/phase2_lora_only_s42', 'log_path': '/root/turn_residual_gating/runs/phase2_lora_only_s42.log', 'checkpoint_source': 'from_scratch', 'eval_data': 'N/A'}
1107	  Conclusion: success
1108	  Metrics:
1109	{
1110	    "epochs_completed": 3,
1111	    "global_steps": 3000,
1112	    "training_time_seconds": 20588.6,
1113	    "training_time_hours": 5.7,
1114	    "gate_fixed": 1,
1115	    "gate_type_actual": "none",
1116	    "final_lora_size_mb": 20,
1117	    "eval_modelgen_ours_mid_gar": 0.0245,
1118	    "eval_modelgen_dongre_mid_gar": 0.0185,
1119	    "eval_modelgen_ppl": 1.371
1120	}
1121	
1122	================================================================================
1123	EXPERIMENT: phase2_tg_s42
1124	================================================================================
1125	  Status: DONE
1126	  Created: 2026-05-18T06:04:12.759Z
1127	  Updated: 2026-05-22T04:36:54.262Z
1128	  Completed: 2026-05-18T11:19:01.512Z
1129	  Retry count: 0
1130	  Hypothesis: ThreadGate (turn-conditional gating) 在 L_NTP+L_GAR 联合训练后，相比 Uniform Gate，mid-turn GAR recovery 高出 ≥3pp，验证 Cesaro 理论预测：position-conditional 干预优于 uniform 干预
1131	  Spec: {'command': 'bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating/src && python train_phase2.py --gate-type threadgate --seed 42 --output-dir /root/turn_residual_gating/checkpoints/tg_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-seq-len 2048"', 'server': 'westd-20861', 'gpu': ['cuda:0'], 'pid': '11286', 'log_path': '~/runs/turn_residual_gating/phase2_tg_s42.log', 'submitted_at': '2026-05-18T07:03:28.476Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'wall_clock_seconds': 15333, 'gpu_hours': 4.26, 'data_path': '/root/turn_residual_gating/data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Qwen/Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_path': '/root/turn_residual_gating/checkpoints/tg_s42'}
1132	  Conclusion: negative
1133	  Metrics:
1134	{
1135	    "final_ntp_loss": 0.94,
1136	    "final_gar_loss": 0,
1137	    "gate_mean": 0.988,
1138	    "gar_loss_zero_pct": 87.6,
1139	    "epochs_completed": 1.67,
1140	    "killed_reason": "SIGTERM by diagnose worker (unauthorized)"
1141	}
1142	
1143	================================================================================
1144	EXPERIMENT: phase2_tg_s42_v2
1145	================================================================================
1146	  Status: DONE
1147	  Created: 2026-05-18T11:13:37.042Z
1148	  Updated: 2026-05-18T13:11:26.331Z
1149	  Completed: 2026-05-18T13:11:26.331Z
1150	  Retry count: 0
1151	  Hypothesis: ThreadGate + 修复后的 cumulative GAR loss (ε=0.001) 在 L_NTP+L_GAR 联合训练后，mid-turn GAR recovery 应显著优于 v1 (NTP-only baseline)，验证 GAR loss 的有效性
1152	  Spec: {'command': 'bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating/src && python train_phase2.py --gate-type threadgate --seed 42 --output-dir /root/turn_residual_gating/checkpoints/tg_s42_v2 --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-seq-len 2048 --gar-loss-mode cumulative --gar-epsilon 0.001 --init-bias 2.0 --lambda-gar 5.0"', 'server': 'westd-20861', 'gpu': ['cuda:0'], 'pid': '25726', 'log_path': '~/runs/turn_residual_gating/phase2_tg_s42_v2.log', 'submitted_at': '2026-05-18T11:50:47.143Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'checkpoint_path': '/root/turn_residual_gating/checkpoints/tg_s42_v2', 'wall_clock_seconds': 4839.2, 'gpu_hours': 1.34}
1153	  Conclusion: killed
1154	
1155	================================================================================
1156	EXPERIMENT: phase2_tg_s42_v3
1157	================================================================================
1158	  Status: DONE
1159	  Created: 2026-05-18T13:07:54.463Z
1160	  Updated: 2026-05-18T13:38:10.723Z
1161	  Completed: 2026-05-18T13:38:10.723Z
1162	  Retry count: 0
1163	  Hypothesis: ThreadGate + maximize GAR loss (L_GAR=-mean(GAR)) 提供持续非零梯度，避免 hinge loss 的退化平衡点，gate 值应随训练下降（学习到选择性干预），同时 NTP loss 正常收敛
1164	  Spec: {'server': 'westd-20861', 'gpu': 'cuda:0', 'data_path': '/root/turn_residual_gating/data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Qwen/Qwen2.5-7B-Instruct', 'seed': 42, 'command': 'python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 2.0 --init-bias 2.0 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v3 --data-dir /root/turn_residual_gating/data/ultrachat_8k', 'pid': '30973', 'log_path': '/root/turn_residual_gating/runs/phase2_tg_s42_v3.log', 'checkpoint_source': 'N/A (training from scratch with LoRA)', 'eval_data': 'N/A (training experiment, not eval)', 'checkpoint_path': '/root/turn_residual_gating/runs/phase2_tg_s42_v3'}
1165	  Conclusion: negative
1166	  Metrics:
1167	{
1168	    "gate_mean_step0": 0.8743,
1169	    "gate_mean_step500": 0.8761,
1170	    "gate_delta": 0.004,
1171	    "gate_std": 0.001,
1172	    "final_ntp_loss": 0.94,
1173	    "final_gar_loss": -0.019,
1174	    "gar_contribution_pct": "2-4%",
1175	    "diagnosis": "gate frozen, GAR indirect gradient too weak"
1176	}
1177	
1178	================================================================================
1179	EXPERIMENT: phase2_tg_s42_v3b
1180	================================================================================
1181	  Status: DONE
1182	  Created: 2026-05-18T13:38:16.020Z
1183	  Updated: 2026-05-18T14:51:42.486Z
1184	  Completed: 2026-05-18T14:51:42.486Z
1185	  Retry count: 0
1186	  Hypothesis: λ=10 + gate_lr=10x + init_bias=0.0 (sigmoid=0.5) 能否驱动 gate 产生 layer 间分化 (gate_std>0.05)？如果 500 步后 gate_std<0.02 且无选择性 → GAR-driven gating 梯度路径确认失败，需要 pivot
1187	  Spec: {'command': 'python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 10.0 --init-bias 0.0 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v3b --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-steps 500', 'server': 'westd-20861', 'data_path': '/root/turn_residual_gating/data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_source': 'from_scratch', 'eval_data': 'N/A', 'checkpoint_path': '/root/turn_residual_gating/runs/phase2_tg_s42_v3b', 'log_path': '/root/turn_residual_gating/runs/v3b_log.txt'}
1188	  Conclusion: success
1189	  Metrics:
1190	{
1191	    "gate_std_final": 0.087,
1192	    "gate_mean_final": 0.9388,
1193	    "gate_min_final": 0.5352,
1194	    "gate_max_final": 0.9922,
1195	    "L4_gate": 0.535,
1196	    "L0_gate": 0.777,
1197	    "L_NTP_final": 0.7787,
1198	    "L_GAR_final": -0.9606,
1199	    "elapsed_seconds": 3565.9,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a53682e4-fb07-4dcd-a5d5-33cfa6509ad4",
  "isSidechain": true,
  "promptId": "46b2b0c6-9613-417a-9397-99622f342526",
  "agentId": "a8867062004a08a3c",
  "type": "user",
  "uuid": "f92847e8-c797-488e-ae12-2ff6312679da",
  "sourceToolAssistantUUID": "a53682e4-fb07-4dcd-a5d5-33cfa6509ad4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-24T15:08:18.557Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D4VJKkao7q3JoVXXNudPqc`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt",
  "limit": 300,
  "offset": 1200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f92847e8-c797-488e-ae12-2ff6312679da",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbyzrgfdPwsjo1k58yG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "512547df-773f-4cbc-b485-c3be3694dd67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R9uB9SgzJ4CTdb3fcxJ5Xp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8634,
      "cache_read_input_tokens": 43553,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8634
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 43553,
          "cache_creation_input_tokens": 8634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8634,
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

_source line 36 · 2026-05-24T15:08:18.564Z_

<details><summary>↩ Tool result · `toolu_01D4VJKkao7q3JoVXXNudPqc`</summary>

```text
1200	    "optimizer_steps": 500,
1201	    "gate_grad_received": true
1202	}
1203	
1204	================================================================================
1205	EXPERIMENT: phase2_tg_s42_v4
1206	================================================================================
1207	  Status: DONE
1208	  Created: 2026-05-18T14:58:00.124Z
1209	  Updated: 2026-05-18T16:50:36.202Z
1210	  Completed: 2026-05-18T16:50:33.778Z
1211	  Retry count: 0
1212	  Hypothesis: 重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值
1213	  Spec: {'command': 'python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v4 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3', 'server': 'westd-20861', 'gpu': 'cuda:0', 'pid': '36519', 'data_path': '/root/turn_residual_gating/data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Qwen/Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_path': '/root/turn_residual_gating/runs/phase2_tg_s42_v4', 'log_path': '/root/turn_residual_gating/runs/phase2_tg_s42_v4.log', 'checkpoint_source': 'from_scratch', 'eval_data': 'N/A'}
1214	  Conclusion: failed
1215	
1216	================================================================================
1217	EXPERIMENT: phase2_tg_s42_v5
1218	================================================================================
1219	  Status: DONE
1220	  Created: 2026-05-18T17:10:23.229Z
1221	  Updated: 2026-05-18T17:52:54.605Z
1222	  Completed: 2026-05-18T17:52:49.951Z
1223	  Retry count: 0
1224	  Hypothesis: 重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值
1225	  Spec: {'command': 'bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v5 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3"', 'server': 'westd-20861', 'gpu': 'cuda:0', 'pid': '3639', 'log_path': '~/runs/turn_residual_gating/phase2_tg_s42_v5.log', 'submitted_at': '2026-05-18T17:10:30.573Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': '/root/turn_residual_gating/data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Qwen/Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_path': '/root/turn_residual_gating/runs/phase2_tg_s42_v5', 'checkpoint_source': 'from_scratch', 'eval_data': 'N/A', 'wall_clock_seconds': 2539.4, 'gpu_hours': 0.71}
1226	  Conclusion: negative
1227	  Metrics:
1228	{
1229	    "step2000_gate_std": 0.0225,
1230	    "step2000_gate_mean": 0.9586,
1231	    "step2000_gate_min": 0.9062,
1232	    "step2000_gate_max": 0.9961,
1233	    "step2000_L_GAR": -0.8977,
1234	    "step2000_L_NTP": 0.7611,
1235	    "step2000_total_loss": -0.1365,
1236	    "step2400_gate_std": 0.0219,
1237	    "step2400_gate_mean": 0.9651,
1238	    "step2400_gate_min": 0.918,
1239	    "step2400_gate_max": 0.9961,
1240	    "step2400_profile": "L0=0.918 L12=0.918 L13=0.926 L1=0.996 L26=0.996",
1241	    "L_GAR_saturated_at": -0.91,
1242	    "gate_range_compression": "0.918-0.996"
1243	}
1244	
1245	================================================================================
1246	EXPERIMENT: phase2_tg_s42_v6
1247	================================================================================
1248	  Status: DONE
1249	  Created: 2026-05-18T17:53:01.911Z
1250	  Updated: 2026-05-22T04:37:13.229Z
1251	  Completed: 2026-05-18T18:18:07.869Z
1252	  Retry count: 0
1253	  Hypothesis: smooth_saturation loss (-target*tanh(GAR/target), target=0.5) 提供有界但持续的 GAR 梯度，避免 maximize 的恒等退化（gate→1）和 hinge_target 的梯度消失（GAR达标后梯度=0）。预期：gate_std>0.05 的层间分化 + GAR 稳态在 0.3-0.5 + NTP loss 正常收敛 + 总 loss 为正。
1254	  Spec: {'command': 'bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type threadgate --gar-loss-mode smooth_saturation --gar-target 0.5 --lambda-gar 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v6 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3"', 'server': 'westd-20861', 'data_path': '/root/turn_residual_gating/data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Qwen/Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_path': '/root/turn_residual_gating/runs/phase2_tg_s42_v6', 'log_path': '~/runs/turn_residual_gating/phase2_tg_s42_v6.log'}
1255	  Conclusion: negative
1256	  Metrics:
1257	{
1258	    "dryrun_step0_L_NTP": 2.0275,
1259	    "dryrun_step0_L_GAR": -0.0161,
1260	    "dryrun_step0_total_loss": 2.0114,
1261	    "dryrun_step4_L_NTP": 1.6544,
1262	    "dryrun_step4_L_GAR": -0.0147,
1263	    "dryrun_step4_total_loss": 1.6397,
1264	    "dryrun_gate_grad": true,
1265	    "dryrun_gate_mean_init": 0.8097,
1266	    "dryrun_gate_std_init": 0.0341,
1267	    "dryrun_gate_min_init": 0.6836,
1268	    "dryrun_gate_max_init": 0.8672,
1269	    "dryrun_gate_mean_step5": 0.8025,
1270	    "dryrun_gate_std_step5": 0.0842,
1271	    "dryrun_gate_min_step5": 0.5547,
1272	    "dryrun_gate_max_step5": 0.9805,
1273	    "gs50_gate_mean": 0.8117,
1274	    "gs50_gate_std": 0.0612,
1275	    "gs50_gate_min": 0.6836,
1276	    "gs50_gate_max": 0.9805,
1277	    "gs100_gate_mean": 0.8737,
1278	    "gs100_gate_std": 0.0367,
1279	    "gs100_gate_min": 0.8164,
1280	    "gs100_gate_max": 0.9766,
1281	    "gs100_L_NTP": 0.8151,
1282	    "gs100_L_GAR": -0.158,
1283	    "gs100_total_loss": 0.6571,
1284	    "gs100_profile_bottom3": "L12=0.816 L4=0.824 L13=0.824",
1285	    "gs100_profile_top3": "L27=0.977 L26=0.961 L23=0.914",
1286	    "gs143_L_GAR": -0.3876,
1287	    "gs143_gate_mean": 0.9227
1288	}
1289	
1290	================================================================================
1291	EXPERIMENT: phase2_tg_s42_v7
1292	================================================================================
1293	  Status: DONE
1294	  Created: 2026-05-18T18:17:45.739Z
1295	  Updated: 2026-05-20T03:04:19.923Z
1296	  Completed: 2026-05-19T00:48:47.463Z
1297	  Retry count: 0
1298	  Hypothesis: MSE 双向 loss (mean_GAR - target)² + gate diversity 正则 F.relu(min_std - gate_std) 从结构上解决恒等退化：MSE 在 GAR > target 时反向惩罚（不再单调推高），gate_div 直接强制层间分化。预期：gate_std 稳定 >0.05 + GAR 收敛到 target=0.5 附近 + NTP 正常收敛。
1299	  Spec: {'checkpoint_source': 'from_scratch', 'eval_data': 'N/A', 'command': 'bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v7 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3"', 'server': 'westd-20861', 'gpu': 'cuda:0', 'data_path': '/root/turn_residual_gating/data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_path': '/root/turn_residual_gating/runs/phase2_tg_s42_v7', 'log_path': '/root/turn_residual_gating/runs/phase2_tg_s42_v7.log'}
1300	  Conclusion: success
1301	  Metrics:
1302	{
1303	    "eval_iid_ours_mid_gar": 0.5035,
1304	    "eval_iid_dongre_mid_gar": 0.0152,
1305	    "eval_iid_ppl": 2.784,
1306	    "eval_heldout_ours_mid_gar": 0.5035,
1307	    "eval_heldout_dongre_mid_gar": 0.0152,
1308	    "eval_heldout_ppl": 2.78,
1309	    "eval_modelgen_ours_mid_gar": 0.0157,
1310	    "eval_modelgen_dongre_mid_gar": 0.0194,
1311	    "eval_modelgen_ppl": 1.36,
1312	    "gate_mean_final": 0.9336,
1313	    "gate_std_final": 0.0492
1314	}
1315	
1316	================================================================================
1317	EXPERIMENT: phase2_tg_s42_v8_schedsampling
1318	================================================================================
1319	  Status: DONE
1320	  Created: 2026-05-19T15:02:00.223Z
1321	  Updated: 2026-05-19T16:33:04.989Z
1322	  Completed: 2026-05-19T16:09:52.423Z
1323	  Retry count: 0
1324	  Hypothesis: Scheduled sampling 应用到 GAR loss（线性从 0→0.5 混合 teacher-forced + model-generated contexts）能缩小 v7 的 30x training-inference GAR gap。机制：在 model-generated context 上计算 GAR loss 迫使 attention pattern 适应推理时分布，直接 address teacher-forcing distribution shift。成功标准：inference GAR 显著高于 v7 的 0.016，PPL 不显著恶化（≤2.78+0.2）。
1325	  Spec: {'command': 'python src/train_phase2_v8.py --scheduled-sampling --ss-max-ratio 0.5', 'server': 'westd-20861', 'gpu': 'cuda:0', 'pid': 73838, 'log_path': '/root/turn_residual_gating/runs/phase2_tg_s42_v8_schedsampling/', 'submitted_at': '2026-05-19T15:43:01.461Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': '/root/turn_residual_gating/data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_source': 'N/A (training from scratch with LoRA)', 'eval_data': 'ultrachat_eval_heldout.json (post-training eval)', 'hyperparams': {'lr': 0.0002, 'epochs': 3, 'grad_accum': 8, 'ss_max_ratio': 0.5, 'ss_gen_max_tokens': 256, 'ss_gen_temperature': 0.7}, 'estimated_hours': '8-9', 'checkpoint_path': 'N/A (crashed at 5.8%)', 'wall_clock_seconds': 1611.0, 'gpu_hours': 0.45}
1326	  Conclusion: failed
1327	  Metrics:
1328	{
1329	    "killed_at_microstep": 1950,
1330	    "total_microsteps": 24000,
1331	    "completion_pct": 8.1,
1332	    "global_step_approx": 244,
1333	    "total_global_steps": 3000,
1334	    "ss_steps_observed": 1,
1335	    "tf_lgar_mean_step850_1400": 0.0062,
1336	    "tf_lgar_std": 0.0082,
1337	    "tf_lgar_collapse_step": 800,
1338	    "gate_mean_final": 0.93,
1339	    "ss_ratio_at_kill": 0.081,
1340	    "crash_reason": "killed by director: SS path code bug (D026) makes experiment invalid, GPU needed for PCGrad",
1341	    "design_flaw_ss_ramp_too_slow": true,
1342	    "design_flaw_no_ss_tf_separate_logging": true
1343	}
1344	
1345	================================================================================
1346	EXPERIMENT: phase2_tg_s42_v8b_resume
1347	================================================================================
1348	  Status: DONE
1349	  Created: 2026-05-20T10:08:29.483Z
1350	  Updated: 2026-05-21T01:56:13.289Z
1351	  Completed: 2026-05-20T18:57:21.189Z
1352	  Retry count: 0
1353	  Hypothesis: 从 epoch_0 checkpoint resume v8b scheduled sampling 训练。SS 线性混合 0→0.5 teacher-forced + model-generated contexts。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。
1354	  Spec: {'command': 'python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir data/ultrachat_8k --output-dir checkpoints/tg_v8b_ss_fixed_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42 --scheduled-sampling --ss-max-ratio 0.5 --resume checkpoints/tg_v8b_ss_fixed_s42/epoch_0', 'server': 'westd-20861', 'data_path': 'data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_source': 'phase2_tg_s42_v8b_ss_fixed/epoch_0', 'eval_data': 'N/A (training experiment)', 'checkpoint_path': 'checkpoints/tg_v8b_ss_fixed_s42', 'log_path': '~/runs/turn_residual_gating/phase2_tg_s42_v8b_resume.log'}
1355	  Conclusion: success
1356	  Metrics:
1357	{
1358	    "training": {
1359	        "total_steps": 3000,
1360	        "epochs_completed": 3,
1361	        "wall_clock_hours": 8.1,
1362	        "final_loss": 0.933,
1363	        "final_ntp_loss": 0.9322,
1364	        "final_gar_loss": 0.0008,
1365	        "final_gate_mean": 0.9586,
1366	        "final_gate_std": 0.0582,
1367	        "ss_ratio": 0.5
1368	    },
1369	    "eval_iid": {
1370	        "gar_ours": 0.4983,
1371	        "gar_dongre": 0.3855,
1372	        "ppl": 2.78
1373	    },
1374	    "eval_modelgen": {
1375	        "gar_ours": 0.3177,
1376	        "gar_dongre": 0.3533,
1377	        "ppl": 1.38
1378	    },
1379	    "vs_v7": {
1380	        "iid_gar_ours_delta": -0.005,
1381	        "modelgen_gar_ours_delta": 0.302,
1382	        "gap_ratio_v7": 32,
1383	        "gap_ratio_v8b": 1.57
1384	    }
1385	}
1386	
1387	================================================================================
1388	EXPERIMENT: phase2_tg_s42_v8b_ss_fixed
1389	================================================================================
1390	  Status: DONE
1391	  Created: 2026-05-20T02:28:58.064Z
1392	  Updated: 2026-05-20T09:30:04.080Z
1393	  Completed: 2026-05-20T09:22:35.962Z
1394	  Retry count: 0
1395	  Hypothesis: Fixed scheduled sampling (D026 三项 bug 修复后): 线性从 0→0.5 混合 teacher-forced + model-generated contexts 计算 GAR loss。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效，paper 从纯 negative 升级为 diagnosis + initial remedy。超参与 v7 一致 (lambda_gar=1.0, MSE+gate_div)，唯一变量是 SS path。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。
1396	  Spec: {'command': 'bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir data/ultrachat_8k --output-dir checkpoints/tg_v8b_ss_fixed_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42 --scheduled-sampling --ss-max-ratio 0.5"', 'server': 'westd-20861', 'gpu': ['cuda:0'], 'pid': '133321', 'log_path': '~/runs/turn_residual_gating/phase2_tg_s42_v8b_ss_fixed.log', 'submitted_at': '2026-05-20T02:28:58.001Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': '/root/turn_residual_gating/data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_path': '/root/turn_residual_gating/checkpoints/tg_v8b_ss_fixed_s42', 'checkpoint_source': 'from_scratch', 'eval_data': 'N/A', 'wall_clock_seconds': 24818.0, 'gpu_hours': 6.89}
1397	  Conclusion: failed
1398	
1399	================================================================================
1400	EXPERIMENT: phase2_tg_s42_v9_pcgrad
1401	================================================================================
1402	  Status: DONE
1403	  Created: 2026-05-19T16:13:21.907Z
1404	  Updated: 2026-05-20T03:04:17.171Z
1405	  Completed: None
1406	  Retry count: 2
1407	  Hypothesis: PCGrad (Yu et al. NeurIPS 2020) 消除 NTP-GAR 梯度方向冲突后（仅对 gate 参数投影 NTP 梯度到 GAR 梯度正交平面），如果 30x training-inference GAR gap 仍在 → 因果证据证明 exposure bias（非梯度竞争）是 gap 根因。与 v7 对比：相同超参（lambda_gar=1.0, MSE+gate_div），唯一变量是梯度处理方式。成功标准：(1) 梯度 cos_sim 显著改善（从 v7 的 -0.089 提升到 ≥0），(2) 但推理 GAR 仍 ≈ v7 水平（0.016），证明梯度冲突不是 gap 的因。
1408	  Spec: {'command': 'bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2_v9_pcgrad.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir data/ultrachat_8k --output-dir checkpoints/tg_v9_pcgrad_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42"', 'server': 'westd-20861', 'gpu': ['cuda:0'], 'pid': '83860', 'log_path': '/root/turn_residual_gating/logs/phase2_tg_v9_pcgrad_s42.log', 'submitted_at': '2026-05-19T17:42:10.820Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'checkpoint_path': '/root/turn_residual_gating/checkpoints/tg_v9_pcgrad_s42', 'wall_clock_seconds': 30601.5, 'gpu_hours': 8.5}
1409	  Conclusion: success
1410	  Metrics:
1411	{
1412	    "eval_iid_ours_mid_gar": 0.5002,
1413	    "eval_iid_dongre_mid_gar": 0.0123,
1414	    "eval_iid_ppl": 2.78,
1415	    "eval_iid_ntp": 0.9752,
1416	    "eval_heldout_ours_mid_gar": 0.5002,
1417	    "eval_heldout_dongre_mid_gar": 0.0123,
1418	    "eval_heldout_ppl": 2.78,
1419	    "eval_heldout_ntp": 0.9752,
1420	    "eval_modelgen_ours_mid_gar": 0.0151,
1421	    "eval_modelgen_dongre_mid_gar": 0.0173,
1422	    "eval_modelgen_ppl": 1.5,
1423	    "vs_v7_iid_ppl_diff": 0.004,
1424	    "vs_v7_iid_gar_diff": -0.0033
1425	}
1426	
1427	================================================================================
1428	EXPERIMENT: phase2_ug_s42
1429	================================================================================
1430	  Status: DONE
1431	  Created: 2026-05-18T06:04:17.643Z
1432	  Updated: 2026-05-20T02:15:15.775Z
1433	  Completed: 2026-05-19T06:53:13.931Z
1434	  Retry count: 0
1435	  Hypothesis: Uniform gating baseline: per-layer independent gates without turn conditioning (content-dependent only), to isolate whether ThreadGate's turn-conditioned gating provides benefit over content-only residual scaling. Same training setup as v7 but with gate-type=uniform.
1436	  Spec: {'command': 'python src/train_phase2.py --gate-type uniform --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_ug_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3', 'server': 'westd-20861', 'data_path': '/root/turn_residual_gating/data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_path': '/root/turn_residual_gating/runs/phase2_ug_s42', 'log_path': '/root/turn_residual_gating/runs/phase2_ug_s42.log', 'checkpoint_source': 'from_scratch', 'eval_data': 'N/A'}
1437	  Conclusion: success
1438	  Metrics:
1439	{
1440	    "epoch0_avg_loss": 1.0019,
1441	    "epoch0_avg_ntp": 0.9755,
1442	    "epoch0_avg_gar": 0.0259,
1443	    "epoch0_avg_div": 0.0005,
1444	    "epoch1_avg_loss": 0.9447,
1445	    "epoch1_avg_ntp": 0.9435,
1446	    "epoch1_avg_gar": 0.0013,
1447	    "epoch1_avg_div": 0,
1448	    "epoch2_avg_loss": 0.9319,
1449	    "epoch2_avg_ntp": 0.9309,
1450	    "epoch2_avg_gar": 0.001,
1451	    "epoch2_avg_div": 0,
1452	    "final_gate_mean": 0.9598,
1453	    "final_gate_std": 0.0518,
1454	    "final_gate_min": 0.7773,
1455	    "final_gate_max": 1,
1456	    "final_profile_L3": 0.777,
1457	    "final_profile_L5": 0.812,
1458	    "final_profile_L0": 0.875,
1459	    "final_profile_L27": 1,
1460	    "training_time_seconds": 21994.5,
1461	    "training_time_hours": 6.1,
1462	    "global_steps": 7950,
1463	    "unexpected_per_layer_variation": true,
1464	    "eval_modelgen_ours_mid_gar": 0.0149,
1465	    "eval_modelgen_dongre_mid_gar": 0.0185,
1466	    "eval_modelgen_ppl": 1.396
1467	}
1468	
1469	================================================================================
1470	EXPERIMENT: qwen15b_phase1_diag
1471	================================================================================
1472	  Status: DONE
1473	  Created: 2026-05-23T06:44:59.895Z
1474	  Updated: 2026-05-24T06:53:23.496Z
1475	  Completed: 2026-05-24T06:53:23.496Z
1476	  Retry count: 0
1477	  Hypothesis: GAR attention decay toward system-prompt goal tokens is a general phenomenon across model scales, not specific to 7B. Qwen-2.5-1.5B-Instruct should also show progressive GAR decline across conversation turns, confirming the phenomenon is architecture-level rather than scale-dependent.
1478	  Spec: {'command': 'python train_phase2.py --model Qwen/Qwen2.5-1.5B-Instruct --config configs/tg_v7.yaml --seed 42 --epochs 3', 'server': 'westd-20861', 'data_path': '/root/turn-residual-gating/data/train_400.json', 'data_count': 400, 'model_name': 'Qwen/Qwen2.5-1.5B-Instruct', 'seed': 42, 'checkpoint_path': 'runs/qwen15b_tg_v7_s42/', 'log_path': 'logs/qwen15b_phase1_diag.log'}
1479	  Conclusion: success
1480	
1481	================================================================================
1482	EXPERIMENT: trc_baseline_v7_tg
1483	================================================================================
1484	  Status: DONE
1485	  Created: 2026-05-20T07:18:17.576Z
1486	  Updated: 2026-05-20T09:34:40.734Z
1487	  Completed: 2026-05-20T09:28:05.853Z
1488	  Retry count: 0
1489	  Hypothesis: 如果 exposure bias 对 auxiliary objectives 的破坏跨特征空间通用，那么 TRC (hidden state cos_sim) 在 model-gen 下也应出现与 GAR (attention 空间) 类似的 TF/gen gap。在 v7 TG / LoRA-only / base 三个 checkpoint 上测量 TRC baseline，确认 gap 是否存在。成功标准：gen TRC 显著低于 TF TRC。
1490	  Spec: {'command': 'bash scripts/launch_trc_baseline.sh', 'server': 'westd-20861', 'gpu': ['cuda:0'], 'pid': '158700', 'log_path': '/root/runs/turn_residual_gating/trc_baseline_v7_tg.log', 'submitted_at': '2026-05-20T07:18:38.202Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': '/root/turn_residual_gating/data/standard_conversations.json', 'data_count': 5, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_source': 'phase2_tg_s42_v7 + phase2_lora_only_s42 + base', 'eval_data': '5 hardcoded multi-turn conversations x 10 turns', 'checkpoint_path': '/root/turn_residual_gating/runs/trc_baseline/', 'wall_clock_seconds': 7767.7, 'gpu_hours': 2.16}
1491	  Conclusion: success
1492	  Metrics:
1493	{
1494	    "v7_tg": {
1495	        "tf_trc": 0.3339,
1496	        "gen_trc": 0.3323,
1497	        "trc_gap": 0.0016,
1498	        "tf_tbp_ppl": 1.05,
1499	        "gen_tbp_ppl": 1.05
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "512547df-773f-4cbc-b485-c3be3694dd67",
  "isSidechain": true,
  "promptId": "46b2b0c6-9613-417a-9397-99622f342526",
  "agentId": "a8867062004a08a3c",
  "type": "user",
  "uuid": "3f4e7818-6a3a-4830-a56a-799aae8e65b8",
  "sourceToolAssistantUUID": "512547df-773f-4cbc-b485-c3be3694dd67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-24T15:08:26.405Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H35mCEHv6RFrctno8jqc4M`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt",
  "limit": 300,
  "offset": 1500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f4e7818-6a3a-4830-a56a-799aae8e65b8",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMbzRgvBiHkRn36y2GHA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b60944d-4a64-4c02-84d9-8e7c738bea14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGq678i28PRWJX3NHckJTX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10219,
      "cache_read_input_tokens": 52187,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10219
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 52187,
          "cache_creation_input_tokens": 10219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10219,
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

_source line 38 · 2026-05-24T15:08:26.428Z_

<details><summary>↩ Tool result · `toolu_01H35mCEHv6RFrctno8jqc4M`</summary>

```text
1500	    },
1501	    "lora_only": {
1502	        "tf_trc": 0.349,
1503	        "gen_trc": 0.4106,
1504	        "trc_gap": -0.0617,
1505	        "tf_tbp_ppl": 9.5,
1506	        "gen_tbp_ppl": 12
1507	    },
1508	    "base": {
1509	        "tf_trc": 0.1494,
1510	        "gen_trc": 0.1494,
1511	        "trc_gap": 0,
1512	        "tf_tbp_ppl": 2.05,
1513	        "gen_tbp_ppl": 2.05
1514	    }
1515	}
1516	
1517	================================================================================
1518	EXPERIMENT: v7_tg_s123
1519	================================================================================
1520	  Status: DONE
1521	  Created: 2026-05-21T15:16:39.923Z
1522	  Updated: 2026-05-21T21:17:16.499Z
1523	  Completed: 2026-05-21T21:17:16.499Z
1524	  Retry count: 0
1525	  Hypothesis: v7 TG s42 已验证 ThreadGate 有效性，s123 验证 seed robustness。预期 gate profile 和 GAR 收敛模式与 s42 一致。
1526	  Spec: {'command': 'bash scripts/launch_v7_tg_s123.sh', 'server': 'westd-20861', 'data_path': 'data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 123, 'pid': 245628, 'gpu_index': 0, 'checkpoint_path': '/root/turn_residual_gating/runs/phase2_tg_s123_v7', 'log_path': '/root/turn_residual_gating/logs/v7_tg_s123.log', 'checkpoint_source': 'N/A (from scratch)', 'eval_data': 'N/A'}
1527	  Conclusion: success
1528	  Metrics:
1529	{
1530	    "epoch_1": {
1531	        "avg_loss": 0.9447,
1532	        "avg_ntp_loss": 0.9434,
1533	        "avg_gar_loss": 0.0013,
1534	        "avg_div_loss": 0
1535	    },
1536	    "epoch_2": {
1537	        "avg_loss": 0.9315,
1538	        "avg_ntp_loss": 0.9305,
1539	        "avg_gar_loss": 0.001,
1540	        "avg_div_loss": 0
1541	    },
1542	    "final_gate": {
1543	        "mean": 0.9467,
1544	        "std": 0.051,
1545	        "min": 0.793,
1546	        "max": 1
1547	    },
1548	    "final_gate_profile": {
1549	        "L0": 0.883,
1550	        "L1": 0.793,
1551	        "L2": 0.996,
1552	        "L3": 0.988,
1553	        "L4": 0.984,
1554	        "L5": 0.797,
1555	        "L6": 0.961,
1556	        "L7": 0.918,
1557	        "L8": 0.965,
1558	        "L9": 0.934,
1559	        "L10": 0.969,
1560	        "L11": 0.918,
1561	        "L12": 0.926,
1562	        "L13": 0.941,
1563	        "L14": 0.93,
1564	        "L15": 0.965,
1565	        "L16": 0.941,
1566	        "L17": 0.91,
1567	        "L18": 0.961,
1568	        "L19": 0.965,
1569	        "L20": 0.973,
1570	        "L21": 0.988,
1571	        "L22": 0.969,
1572	        "L23": 0.98,
1573	        "L24": 0.98,
1574	        "L25": 0.984,
1575	        "L26": 0.988,
1576	        "L27": 1
1577	    },
1578	    "training_time_s": 21425.2
1579	}
1580	
1581	================================================================================
1582	EXPERIMENT: v8b_ss_s123
1583	================================================================================
1584	  Status: DONE
1585	  Created: 2026-05-21T04:29:28.197Z
1586	  Updated: 2026-05-21T15:15:49.282Z
1587	  Completed: 2026-05-21T15:15:49.282Z
1588	  Retry count: 0
1589	  Hypothesis: v8b SS s42 成功（gap 32×→1.57×），s123 验证结果的 seed robustness。预期 model-gen GAR 同样显著提升，PPL 无恶化。
1590	  Spec: {'command': 'bash scripts/launch_v8b_ss_s123.sh', 'server': 'westd-20861', 'data_path': 'data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 123, 'checkpoint_source': 'N/A (from scratch)', 'eval_data': 'N/A', 'checkpoint_path': '/root/turn_residual_gating/checkpoints/tg_v8b_ss_s123', 'log_path': '/root/turn_residual_gating/logs/v8b_ss_s123.log'}
1591	  Conclusion: success
1592	  Metrics:
1593	{
1594	    "final_loss": 0.9316,
1595	    "final_ntp_loss": 0.9307,
1596	    "final_gar_loss": 0.0009,
1597	    "final_gate_mean": 0.9505,
1598	    "final_gate_std": 0.0508,
1599	    "final_gate_min": 0.7383,
1600	    "final_gate_max": 1,
1601	    "ss_used_ratio": 0.371,
1602	    "training_time_s": 38773.4,
1603	    "epoch0_loss": 1.0092,
1604	    "epoch1_loss": 0.9444,
1605	    "epoch2_loss": 0.9316
1606	}
1607	
1608	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b60944d-4a64-4c02-84d9-8e7c738bea14",
  "isSidechain": true,
  "promptId": "46b2b0c6-9613-417a-9397-99622f342526",
  "agentId": "a8867062004a08a3c",
  "type": "user",
  "uuid": "1672e737-10e0-4b3f-884a-c82da09fe5ca",
  "sourceToolAssistantUUID": "9b60944d-4a64-4c02-84d9-8e7c738bea14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-24T15:08:30.778Z_

Now let me also check the d048_final_ar_eval per-turn data more carefully, and look for any per-turn GAR data I may have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1672e737-10e0-4b3f-884a-c82da09fe5ca",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMc119ZzsJCvSmKmTJkm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d2efc19-5a7d-444c-8e4e-21258c64fdd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xj7nZmVAicfECfk3PZwZbA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2184,
      "cache_read_input_tokens": 62406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2184,
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

_source line 40 · 2026-05-24T15:08:34.024Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012fthZRNSWUE7DwB7q1me7m`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/all_experiments.json', 'r') as f:\n    exps = json.load(f)\n\n# Look for any experiment with per_turn data in metrics\nfor k, exp in sorted(exps.items()):\n    metrics = exp.get('metrics')\n    if not metrics or not isinstance(metrics, dict):\n        continue\n    metrics_str = json.dumps(metrics)\n    if 'per_turn' in metrics_str or 'turn_' in metrics_str or 'per-turn' in metrics_str:\n        print(f\"\\n{'='*60}\")\n        print(f\"EXPERIMENT: {k}\")\n        print(json.dumps(metrics, indent=2))\nPYEOF\n",
  "description": "Find all experiments with per-turn data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d2efc19-5a7d-444c-8e4e-21258c64fdd1",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMc119ZzsJCvSmKmTJkm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22542059-13f8-4186-8e7c-54ba95d98676",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xj7nZmVAicfECfk3PZwZbA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2184,
      "cache_read_input_tokens": 62406,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2184
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 298,
          "cache_read_input_tokens": 62406,
          "cache_creation_input_tokens": 2184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2184,
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

_source line 41 · 2026-05-24T15:08:34.145Z_

<details><summary>↩ Tool result · `toolu_012fthZRNSWUE7DwB7q1me7m`</summary>

```text
============================================================
EXPERIMENT: eval_llama_ar_n20
{
  "base": {
    "gar_ours_mean": 0.0088,
    "gar_ours_std": 0.0056,
    "gar_ours_median_per_conv": 0.0093,
    "gar_ours_median_per_turn_pool": 0.0071,
    "gar_ours_spike_ratio": "0%",
    "gar_dongre_mean": 0.0049,
    "gar_dongre_std": 0.0013,
    "gar_dongre_median": 0.0047,
    "ngar_ours_mid": 0.1019,
    "ngar_dongre_mid": 0.1171,
    "ppl": 1.293,
    "ppl_std": 0.07,
    "ntp_loss": 0.2552
  },
  "tg": {
    "gar_ours_mean": 0.0434,
    "gar_ours_std": 0.1002,
    "gar_ours_median_per_conv": 0.0179,
    "gar_ours_median_per_turn_pool": 0.0126,
    "gar_ours_spike_ratio": "5% (2/40 turns GAR>=0.4)",
    "gar_dongre_mean": 0.0183,
    "gar_dongre_std": 0.0198,
    "gar_dongre_median": 0.0152,
    "ngar_ours_mid": 0.5357,
    "ngar_dongre_mid": 0.4436,
    "ppl": 1.437,
    "ppl_std": 0.077,
    "ntp_loss": 0.3612
  },
  "lora_only": {
    "gar_ours_mean": 0.0284,
    "gar_ours_std": 0.0481,
    "gar_ours_median_per_conv": 0.0184,
    "gar_ours_median_per_turn_pool": 0.0133,
    "gar_ours_spike_ratio": "0%",
    "gar_dongre_mean": 0.0205,
    "gar_dongre_std": 0.0241,
    "gar_dongre_median": 0.016,
    "ngar_ours_mid": 0.3488,
    "ngar_dongre_mid": 0.4997,
    "ppl": 1.419,
    "ppl_std": 0.075,
    "ntp_loss": 0.3483
  },
  "n_conversations": 20,
  "n_turns": 4,
  "mid_turns_definition": "turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2). All 16 eval entries use same definition.",
  "stat_pool": "median_per_conv: median of 20 per-conversation mid-turn averages. median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).",
  "ranking_gar_ours_mean": "TG(0.0434) > LO(0.0284) > Base(0.0088)",
  "ranking_gar_ours_median_per_conv": "TG(0.0179) \u2248 LO(0.0184) > Base(0.0093)",
  "ranking_gar_ours_median_per_turn_pool": "TG(0.0126) \u2248 LO(0.0133) > Base(0.0071)",
  "ranking_gar_dongre": "LO(0.0205) > TG(0.0183) > Base(0.0049)",
  "note": "Paper \u00a75.5 cites median_per_conv (median of per-conversation mid-turn averages across N=20). median_per_turn_pool is the alternative statistic from pooled individual turns. Both confirm TG \u2248 LO (zero-increment)."
}

============================================================
EXPERIMENT: instruction_retention_test
{
  "late_turn_rate_beta0": 0.759,
  "late_turn_rate_beta3": 0.87,
  "late_turn_delta": 0.111,
  "mcnemar_chi2": 3.125,
  "mcnemar_p": 0.0771,
  "gar_compliance_r": 0.2003,
  "gar_compliance_p": 0.007,
  "category_content_constraint": {
    "beta0": 0.619,
    "beta3": 0.857,
    "delta": 0.238
  },
  "category_count_constraint": {
    "beta0": 1,
    "beta3": 1,
    "delta": 0
  },
  "category_format_constraint": {
    "beta0": 1,
    "beta3": 1,
    "delta": 0
  },
  "category_position_constraint": {
    "beta0": 0.667,
    "beta3": 0.733,
    "delta": 0.067
  }
}

============================================================
EXPERIMENT: llama_phase1_gar_diag
{
  "per_turn_gar": {
    "turn_1": 0.0263,
    "turn_2": 0.0183,
    "turn_3": 0.0087,
    "turn_4": 0.0055,
    "turn_5": 0.006,
    "turn_6": 0.0035,
    "turn_7": 0.0038,
    "turn_8": 0.0037,
    "turn_9": 0.005,
    "turn_10": 0.0026
  },
  "t1_t10_decay_pct": 90.1,
  "t1_mid38_drop_pct": 80.2,
  "n_topics": 5,
  "model": "Meta-Llama-3.1-8B-Instruct",
  "mode": "gen",
  "n_conversations": 5,
  "n_turns": 10
}

============================================================
EXPERIMENT: phase1_gar_diag
{
  "turn1_avg_gar": 0.0418,
  "mid_turns_avg_gar": 0.0122,
  "relative_drop": 0.708,
  "num_conversations": 5,
  "num_turns": 10,
  "per_turn_avg_gar": [
    0.0418,
    0.0241,
    0.0224,
    0.013,
    0.0133,
    0.0086,
    0.0078,
    0.008,
    0.0157,
    0.0064
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22542059-13f8-4186-8e7c-54ba95d98676",
  "isSidechain": true,
  "promptId": "46b2b0c6-9613-417a-9397-99622f342526",
  "agentId": "a8867062004a08a3c",
  "type": "user",
  "uuid": "40494b79-b12d-4d11-8c7c-fa21a249f748",
  "sourceToolAssistantUUID": "22542059-13f8-4186-8e7c-54ba95d98676",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-24T15:08:37.333Z_

Now let me compile the complete report. Let me also extract any remaining data I need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40494b79-b12d-4d11-8c7c-fa21a249f748",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMc1ZwYPvTMRGtWDVgj1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1670bbc-1c2b-4d2c-b43a-26fd01c8dbde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8oJp8jfysnm8S4nzguSra",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2105,
      "cache_read_input_tokens": 64590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2105,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 43 · 2026-05-24T15:08:40.914Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AM6LW4968iK4HVxhASPMrc`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/all_experiments.json', 'r') as f:\n    exps = json.load(f)\n\n# Get full d048_final_ar_eval metrics\nprint(\"=== d048_final_ar_eval FULL METRICS ===\")\nprint(json.dumps(exps['d048_final_ar_eval']['metrics'], indent=2))\n\nprint(\"\\n=== d048_eval_ss_s42 FULL METRICS ===\")\nprint(json.dumps(exps['d048_eval_ss_s42']['metrics'], indent=2))\n\nprint(\"\\n=== llama_ar_matched_eval FULL METRICS ===\")\nprint(json.dumps(exps['llama_ar_matched_eval']['metrics'], indent=2))\nPYEOF\n",
  "description": "Get full metrics for key experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1670bbc-1c2b-4d2c-b43a-26fd01c8dbde",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMc1ZwYPvTMRGtWDVgj1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ebd8134-8689-4753-b8e6-6bfc871c3199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8oJp8jfysnm8S4nzguSra",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2105,
      "cache_read_input_tokens": 64590,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2105
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 293,
          "cache_read_input_tokens": 64590,
          "cache_creation_input_tokens": 2105,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2105,
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

_source line 44 · 2026-05-24T15:08:40.985Z_

<details><summary>↩ Tool result · `toolu_01AM6LW4968iK4HVxhASPMrc`</summary>

```text
=== d048_final_ar_eval FULL METRICS ===
{
  "beta0": {
    "base_gar": 0.019,
    "tg_gar": 0.064,
    "ug_gar": 0.033,
    "lo_gar": 0.037,
    "pcgrad_gar": 0.03,
    "ss_gar": 0.347
  },
  "beta3": {
    "base_gar": 0.531,
    "tg_gar": 0.556,
    "ss_gar": 0.593
  },
  "beta5": {
    "base_gar": 0.704,
    "tg_gar": 0.727,
    "ss_gar": 0.717
  },
  "wilcoxon_beta0": {
    "tg_vs_base_p": "<0.001",
    "tg_vs_base_r": 0.802,
    "ss_vs_tg_p": "<0.001",
    "ss_vs_tg_r": 0.869
  },
  "ppl": {
    "base": 1.447,
    "tg": 1.432,
    "ss": 1.442
  },
  "n_convs": 39
}

=== d048_eval_ss_s42 FULL METRICS ===
{
  "tf": {
    "base_gar_ours_mid": 0.0128,
    "base_gar_dongre_mid": 0.0031,
    "base_ppl": 4.34,
    "base_ntp": 1.4,
    "tg_gar_ours_mid": 0.5025,
    "tg_gar_dongre_mid": 0.389,
    "tg_ppl": 2.78,
    "tg_ntp": 0.98,
    "baseline_mid_gar": 0.0122
  },
  "ar": {
    "gar_ours_mid": 0.3887,
    "gar_ours_ci_95": [
      0.3692,
      0.3934
    ],
    "ppl": 1.35
  },
  "gap_ratio": 1.29,
  "n_conversations_tf": 50,
  "n_conversations_ar": 5,
  "bootstrap_turns": "curve[2:] (turns 3-T)",
  "note": "AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch with eval_200.json N=50."
}

=== llama_ar_matched_eval FULL METRICS ===
{
  "ar_base_ours": {
    "mid_gar": 0.0082,
    "ngar": 0.1,
    "ppl": 1.267
  },
  "ar_tg_ours": {
    "mid_gar": 0.0388,
    "ngar": 0.493,
    "ppl": 1.413
  },
  "ar_base_dongre": {
    "mid_gar": 0.0051,
    "ngar": 0.12,
    "ppl": 1.267
  },
  "ar_tg_dongre": {
    "mid_gar": 0.018,
    "ngar": 0.431,
    "ppl": 1.413
  },
  "tf_reference": {
    "tf_tg_ours_ngar": 11.88,
    "tf_base_ours_ngar": 0.388,
    "tf_tg_ours_raw": 0.4836,
    "tf_tg_dongre_raw": 0.018
  },
  "matched_gap_analysis": {
    "gar_ours_raw_gap": "12.5x (TF 0.484 / AR 0.039)",
    "gar_ours_ngar_gap": "24.1x (TF 11.88 / AR 0.493)",
    "gar_dongre_raw_gap": "1.002x (TF 0.018 / AR 0.018) \u2014 zero gap",
    "tg_over_base_ar_ours": "4.71x",
    "tg_over_base_ar_dongre": "3.54x",
    "conclusion": "GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure bias selectively destroys learned goal-attention routing while leaving content-overlap-based attention unaffected."
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ebd8134-8689-4753-b8e6-6bfc871c3199",
  "isSidechain": true,
  "promptId": "46b2b0c6-9613-417a-9397-99622f342526",
  "agentId": "a8867062004a08a3c",
  "type": "user",
  "uuid": "eb6093c0-203c-45a5-bf29-c540176342fc",
  "sourceToolAssistantUUID": "6ebd8134-8689-4753-b8e6-6bfc871c3199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-24T15:11:40.349Z_

Here is the complete extraction of all 53 experiment entries from the registry.

---

## COMPLETE EXPERIMENT REGISTRY (53 entries)

---

### 1. analysis_attention_heatmap
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Conditions:** Base / TG / UG / LoRA-only (4 models)
- **Conclusion:** success
- **Metrics:**
  - base_mean_goal_attn: 0.0136
  - base_decay: 0.875
  - tg_mean_goal_attn: 0.0232
  - tg_decay: 0.777
  - ug_mean_goal_attn: 0.0216
  - ug_decay: 0.803
  - lora_mean_goal_attn: 0.0216
  - lora_decay: 0.81
  - gating_incremental_benefit: "none"

---

### 2. analysis_gradient_conflict
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Condition:** TG v7 (gradient analysis)
- **Conclusion:** success
- **Metrics:**
  - epoch0_cos_sim: -0.089
  - epoch1_cos_sim: -0.054
  - epoch2_cos_sim: -0.042
  - epoch0_neg_layers_pct: 78.6
  - epoch1_neg_layers_pct: 71.4
  - epoch2_neg_layers_pct: 67.9
  - epoch0_mag_ratio: 7.5
  - epoch1_mag_ratio: 13.7
  - epoch2_mag_ratio: 14.7

---

### 3. attention_steering_eval200_tf
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct + TG v7 LoRA
- **Condition:** TG (steering eval, TF mode)
- **Conclusion:** success
- **Metrics (N=200, mode=tf):**
  - beta_0.0: mid_gar=0.5353, ppl=2.62
  - beta_2.0: mid_gar=0.6112, ppl=2.69
  - beta_3.0: mid_gar=0.788, ppl=2.93
  - beta_4.0: mid_gar=0.8165, ppl=3.49
  - beta_5.0: mid_gar=0.8325, ppl=6.15
  - beta_10.0: mid_gar=0.977, ppl=505.21

---

### 4. attention_steering_gen_n50
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct + TG v7 LoRA
- **Condition:** TG (steering eval, gen mode, N=50)
- **Conclusion:** success
- **Metrics (per-conv mid_gar turns 2-7, >=3 turns only):**
  - beta_0.0: mid_gar=0.0641, mid_gar_std=0.0809, ppl=1.4324, ppl_std=0.1029, n_valid=39
  - beta_2.0: mid_gar=0.128, mid_gar_std=0.1101, ppl=1.4822, ppl_std=0.1385, n_valid=39
  - beta_3.0: mid_gar=0.5558, mid_gar_std=0.0601, ppl=1.5605, ppl_std=0.1719, n_valid=39
  - beta_4.0: mid_gar=0.6439, mid_gar_std=0.0607, ppl=1.6674, ppl_std=0.2241, n_valid=39
  - beta_5.0: mid_gar=0.7271, mid_gar_std=0.0605, ppl=1.7723, ppl_std=0.2693, n_valid=38
  - beta_10.0: mid_gar=0.9612, mid_gar_std=0.0152, ppl=3.4517, ppl_std=1.7813, n_valid=39
  - n_convs_total: 50, n_convs_valid: 39
  - phase_transition_range: "[2, 3]"

---

### 5. attention_steering_v7_tg_gen
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct + TG v7 LoRA
- **Condition:** TG (steering eval, gen mode, N=5 pilot)
- **Conclusion:** success
- **Metrics:**
  - beta_0.0: mid_turns_avg_gar=0.028, avg_ppl=1.409
  - beta_0.5: mid_turns_avg_gar=0.0287, avg_ppl=1.387
  - beta_1.0: mid_turns_avg_gar=0.0349, avg_ppl=1.36
  - beta_2.0: mid_turns_avg_gar=0.062, avg_ppl=1.411
  - beta_5.0: mid_turns_avg_gar=0.6795, avg_ppl=1.908
  - beta_10.0: mid_turns_avg_gar=0.959, avg_ppl=4.22
  - phase_transition_range: "[2, 5]"
  - baseline_gar: 0.028
  - max_gar_at_acceptable_ppl: 0.6795 (at beta=5)

---

### 6. d048_eval_ss_s123
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct + SS s123 LoRA
- **Condition:** SS, seed=123
- **Conclusion:** success
- **Metrics:**
  - tf_gar_ours: 0.5536
  - tf_gar_dongre: 0.4106
  - tf_ppl: 2.6123
  - ar_beta0_gar: 0.4231
  - ar_beta0_ppl: 1.4408
  - ar_beta3_gar: 0.5903
  - ar_beta3_ppl: 1.607
  - ar_beta5_gar: 0.7174
  - ar_beta5_ppl: 1.7852
  - n_convs_tf: 200, n_convs_ar: 39

---

### 7. d048_eval_ss_s42
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct (SS s42)
- **Condition:** SS, seed=42
- **Conclusion:** success
- **Metrics (TF):**
  - base_gar_ours_mid: 0.0128
  - base_gar_dongre_mid: 0.0031
  - base_ppl: 4.34
  - base_ntp: 1.4
  - tg_gar_ours_mid: 0.5025
  - tg_gar_dongre_mid: 0.389
  - tg_ppl: 2.78
  - tg_ntp: 0.98
  - baseline_mid_gar: 0.0122
- **Metrics (AR):**
  - gar_ours_mid: 0.3887
  - gar_ours_ci_95: [0.3692, 0.3934]
  - ppl: 1.35
- gap_ratio: 1.29
- n_conversations_tf: 50, n_conversations_ar: 5
- Note: "AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch with eval_200.json N=50."

---

### 8. d048_eval_ss_s456
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct + SS s456 LoRA
- **Condition:** SS, seed=456
- **Conclusion:** success
- **Metrics:**
  - tf_gar_ours_mid: 0.4964
  - tf_gar_dongre_mid: 0.3862
  - ar_beta0_gar: 0.4325
  - ar_beta0_ppl: 1.4394
  - ar_beta3_gar: 0.605
  - ar_beta3_ppl: 1.5868
  - ar_beta5_gar: 0.7157
  - ar_beta5_ppl: 1.8045
  - n_convs_ar: 50

---

### 9. d048_final_ar_eval
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Conditions:** 6-way (Base/TG/UG/LO/PCGrad/SS), AR N=50
- **Conclusion:** success
- **Metrics (beta0, AR):**
  - base_gar: 0.019
  - tg_gar: 0.064
  - ug_gar: 0.033
  - lo_gar: 0.037
  - pcgrad_gar: 0.03
  - ss_gar: 0.347
- **Metrics (beta3, AR):**
  - base_gar: 0.531
  - tg_gar: 0.556
  - ss_gar: 0.593
- **Metrics (beta5, AR):**
  - base_gar: 0.704
  - tg_gar: 0.727
  - ss_gar: 0.717
- **Wilcoxon (beta0):**
  - tg_vs_base_p: "<0.001", tg_vs_base_r: 0.802
  - ss_vs_tg_p: "<0.001", ss_vs_tg_r: 0.869
- **PPL (AR):**
  - base: 1.447, tg: 1.432, ss: 1.442
- n_convs: 39

---

### 10. d048_queue_runner
- **Status:** PREPARING
- **Conclusion:** failed

---

### 11. d048_split_softmax_eval
- **Status:** DONE
- **Conclusion:** failed (Bug: system_prompt_len=0 hardcoded, NaN for k=0.0/0.3/0.5/0.7)

---

### 12. d048_ss_s123 (training)
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Condition:** SS training, seed=123
- **Conclusion:** success
- No eval metrics (training only)

---

### 13. d048_ss_s42 (training)
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Condition:** SS training, seed=42
- **Conclusion:** success
- **Training metrics:**
  - final_avg_loss: 0.9326
  - final_ntp_loss: 0.932
  - final_gar_loss: 0.0007
  - gate_mean: 0.9527, gate_std: 0.0589
  - gate_min: 0.7383 (L4), gate_max: 1
  - ss_usage: "4750/16000 (29.7%)"
  - epochs_completed: 3
  - wall_clock_h: 6.5

---

### 14. d048_ss_s42_resume
- **Status:** PREPARING (resume placeholder)

---

### 15. d048_ss_s456 (training)
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Condition:** SS training, seed=456
- **Conclusion:** success
- No eval metrics (training only)

---

### 16. eval_llama_ar_n20
- **Status:** DONE
- **Model:** Llama-3.1-8B-Instruct (Base/TG/LoRA-only)
- **Condition:** 3-way Llama AR eval, N=20, T=4
- **Conclusion:** success
- **Metrics (Base, AR):**
  - gar_ours_mean: 0.0088, gar_ours_std: 0.0056
  - gar_ours_median_per_conv: 0.0093
  - gar_ours_median_per_turn_pool: 0.0071
  - gar_ours_spike_ratio: "0%"
  - gar_dongre_mean: 0.0049, gar_dongre_std: 0.0013, gar_dongre_median: 0.0047
  - ngar_ours_mid: 0.1019, ngar_dongre_mid: 0.1171
  - ppl: 1.293, ppl_std: 0.07, ntp_loss: 0.2552
- **Metrics (TG, AR):**
  - gar_ours_mean: 0.0434, gar_ours_std: 0.1002
  - gar_ours_median_per_conv: 0.0179
  - gar_ours_median_per_turn_pool: 0.0126
  - gar_ours_spike_ratio: "5% (2/40 turns GAR>=0.4)"
  - gar_dongre_mean: 0.0183, gar_dongre_std: 0.0198, gar_dongre_median: 0.0152
  - ngar_ours_mid: 0.5357, ngar_dongre_mid: 0.4436
  - ppl: 1.437, ppl_std: 0.077, ntp_loss: 0.3612
- **Metrics (LoRA-only, AR):**
  - gar_ours_mean: 0.0284, gar_ours_std: 0.0481
  - gar_ours_median_per_conv: 0.0184
  - gar_ours_median_per_turn_pool: 0.0133
  - gar_ours_spike_ratio: "0%"
  - gar_dongre_mean: 0.0205, gar_dongre_std: 0.0241, gar_dongre_median: 0.016
  - ngar_ours_mid: 0.3488, ngar_dongre_mid: 0.4997
  - ppl: 1.419, ppl_std: 0.075, ntp_loss: 0.3483
- Rankings: TG(0.0179) approx LO(0.0184) > Base(0.0093) by median_per_conv

---

### 17. eval_llama_lora_only_s42
- **Status:** DONE
- **Model:** Llama-3.1-8B-Instruct + LoRA-only
- **Condition:** LoRA-only ablation on Llama
- **Conclusion:** success
- **TF metrics:**
  - gar_ours: 0.4807, gar_dongre: 0.0188
  - ngar_ours: 11.8031, ngar_dongre: 0.8261
  - ppl: 2.6, ntp_loss: 0.9366
  - N=50, T=4
- **AR metrics:**
  - gar_ours: 0.0617, gar_dongre: 0.0226
  - ngar_ours: 0.6065, ngar_dongre: 0.2537
  - ppl: 1.32, ntp_loss: 0.2787
  - N=5, T=10
- gap_ratio_gar_ours: 7.79

---

### 18. eval_v7_tg_s123
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Condition:** TG v7, seed=123
- **Conclusion:** success
- **IID TF metrics:**
  - gar_ours_mid: 0.5052
  - gar_dongre_mid: 0.0119
  - ppl: 2.7802, ntp: 0.9752
- **Model-gen AR metrics:**
  - gar_ours_mid: 0.0165
  - gar_dongre_mid: 0.0177
  - ppl: 1.3855, ntp: 0.3223
- gap_ratio: 30.6
- comparison_s42: tf_gar_ours_delta=0.0017, ar_gar_ours_delta=0.0008, gap_ratio_delta=-1.4

---

### 19. eval_v8b_ss (SS s42 eval)
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Condition:** SS (v8b), seed=42
- **Conclusion:** success
- **IID metrics:**
  - iid_gar_ours: 0.4983, iid_gar_dongre: 0.3855
  - iid_ppl: 2.78
  - iid_ngar_ours: 13.5, iid_ngar_dongre: 22.68
- **Model-gen metrics:**
  - modelgen_gar_ours: 0.3177, modelgen_gar_dongre: 0.3533
  - modelgen_ppl: 1.38
  - modelgen_ngar_ours: 4.47, modelgen_ngar_dongre: 5.92
- **Per-turn:**
  - iid_turn1_gar_ours: 0.5398
  - modelgen_turn1_gar_ours: 0.4333

---

### 20. eval_v8b_ss_s123
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Condition:** SS (v8b), seed=123
- **Conclusion:** success
- **IID metrics:**
  - gar_ours: 0.503, gar_dongre: 0.394
  - ppl: 2.781, ntp_loss: 0.976
  - N=50, T=3
- **Model-gen metrics:**
  - gar_ours: 0.418, gar_dongre: 0.441
  - ppl: 1.389, ntp_loss: 0.325
  - N=5, T=10
- gap_ratio: 1.2
- base_iid_ppl: 4.338, base_modelgen_ppl: 1.351

---

### 21. instruction_retention_test
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct + TG v7 LoRA
- **Condition:** TG (beta=0 vs beta=3)
- **Conclusion:** success
- **Metrics:**
  - late_turn_rate_beta0: 0.759, late_turn_rate_beta3: 0.87
  - late_turn_delta: 0.111
  - mcnemar_chi2: 3.125, mcnemar_p: 0.0771
  - gar_compliance_r: 0.2003, gar_compliance_p: 0.007
  - category_content_constraint: beta0=0.619, beta3=0.857, delta=0.238
  - category_count_constraint: beta0=1, beta3=1, delta=0
  - category_format_constraint: beta0=1, beta3=1, delta=0
  - category_position_constraint: beta0=0.667, beta3=0.733, delta=0.067

---

### 22. llama_ar_matched_eval
- **Status:** DONE
- **Model:** Llama-3.1-8B-Instruct + TG LoRA
- **Condition:** Llama TG matched eval (N=50, T=4)
- **Conclusion:** success
- **AR Base (ours):** mid_gar=0.0082, ngar=0.1, ppl=1.267
- **AR TG (ours):** mid_gar=0.0388, ngar=0.493, ppl=1.413
- **AR Base (Dongre):** mid_gar=0.0051, ngar=0.12, ppl=1.267
- **AR TG (Dongre):** mid_gar=0.018, ngar=0.431, ppl=1.413
- **TF reference:** tf_tg_ours_ngar=11.88, tf_base_ours_ngar=0.388, tf_tg_ours_raw=0.4836, tf_tg_dongre_raw=0.018
- **Gap analysis:**
  - gar_ours_raw_gap: "12.5x (TF 0.484 / AR 0.039)"
  - gar_ours_ngar_gap: "24.1x (TF 11.88 / AR 0.493)"
  - gar_dongre_raw_gap: "1.002x (TF 0.018 / AR 0.018) -- zero gap"
  - tg_over_base_ar_ours: "4.71x"
  - tg_over_base_ar_dongre: "3.54x"

---

### 23. llama_eval_s42
- **Status:** DONE
- **Model:** Llama-3.1-8B-Instruct
- **Condition:** Llama TG s42 TF+AR eval
- **Conclusion:** success
- **TF Base:** gar_ours=0.0166, ngar_ours=0.3882, gar_dongre=0.0038, ngar_dongre=0.163, ppl=3.45, N=50, T=4
- **TF TG:** gar_ours=0.4836, ngar_ours=11.8818, gar_dongre=0.018, ngar_dongre=0.7922, ppl=2.57, N=50, T=4
- **AR Base:** gar_ours=0.0086, ngar_ours=0.0798, gar_dongre=0.0118, ngar_dongre=0.1265, ppl=1.24, N=5, T=10
- **AR TG:** gar_ours=0.0304, ngar_ours=0.2632, gar_dongre=0.0217, ngar_dongre=0.2459, ppl=1.32, N=5, T=10
- gap_ratio_tg_ours: 15.9
- gap_ratio_base_ours: 1.93
- gap_ratio_tg_dongre: 0.83
- vs_qwen_v7_gap_ratio: 32.1
- baseline_mid_gar: 0.0122

---

### 24. llama_lora_only_s42 (training)
- **Status:** DONE
- **Model:** Llama-3.1-8B-Instruct
- **Condition:** LoRA-only ablation training
- **Conclusion:** success
- **Training metrics:**
  - final_avg_loss: 0.9288, final_avg_ntp: 0.9279, final_avg_gar: 0.0009
  - gate_fixed: 1, gate_type: "none"
  - wall_clock_h: 7.03, epochs_completed: 3

---

### 25. llama_phase1_gar_diag
- **Status:** DONE
- **Model:** Meta-Llama-3.1-8B-Instruct (base, no fine-tuning)
- **Condition:** Base Llama phase1 diagnostics
- **Conclusion:** success
- **Per-turn GAR:**
  - turn_1: 0.0263
  - turn_2: 0.0183
  - turn_3: 0.0087
  - turn_4: 0.0055
  - turn_5: 0.006
  - turn_6: 0.0035
  - turn_7: 0.0038
  - turn_8: 0.0037
  - turn_9: 0.005
  - turn_10: 0.0026
- t1_t10_decay_pct: 90.1
- t1_mid38_drop_pct: 80.2

---

### 26. llama_tg_s42 (training)
- **Status:** DONE
- **Model:** Meta-Llama-3.1-8B-Instruct
- **Condition:** TG training, seed=42
- **Conclusion:** success
- **Training metrics:**
  - epochs_completed: 3, total_steps: 3000
  - wall_clock_hours: 7.28
  - final_avg_loss: 0.9233, final_avg_ntp: 0.9224, final_avg_gar: 0.0009
  - final_gate_mean: 0.9099, final_gate_std: 0.0701
  - final_gate_min: 0.7188, final_gate_max: 0.9922
- **Gate profile (step 3000):**
  - L0=0.957, L1=0.973, L2=0.977, L3=0.965, L4=0.992, L5=0.969
  - L6=0.957, L7=0.957, L8=0.961, L9=0.949, L10=0.938, L11=0.934
  - L12=0.969, L13=0.953, L14=0.957, L15=0.965, L16=0.953, L17=0.961
  - L18=0.922, L19=0.902, L20=0.883, L21=0.863, L22=0.836, L23=0.844
  - L24=0.809, L25=0.719, L26=0.762, L27=0.805, L28=0.801, L29=0.855
  - L30=0.898, L31=0.934
- GPU: NVIDIA RTX PRO 6000 Blackwell (102GB VRAM)

---

### 27. llama_tg_training
- **Status:** PREPARING
- **Conclusion:** failed

---

### 28. mmlu_eval_all
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Conditions:** Base/LO/UG/TG/PCGrad/SS (MMLU 5-shot)
- **Conclusion:** success
- **Metrics (MMLU accuracy):**
  - base_qwen: 0.7423
  - pcgrad_v9_s42: 0.7386
  - ss_v8b_s42: 0.7375
  - lo_s42: 0.7357
  - tg_v7_s42: 0.7347
  - ug_s42: 0.7346

---

### 29. p0_ss_steering_eval
- **Status:** PREPARING
- **Conclusion:** killed

---

### 30. p1_llama_ss_training
- **Status:** RUNNING
- **Model:** Llama-3.1-8B-Instruct
- **Condition:** SS training on Llama, seed=42
- **Hyperparams:** lr=2e-4, batch_size=1, grad_accum=8, epochs=3, ss_max_ratio=0.3, lora_rank=16
- No metrics yet (still running)

---

### 31. p1_tf_ar_kl_divergence
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Conclusion:** success
- **Metrics:**
  - tg_delta_gar: 0.0165
  - base_delta_gar: 0.0122
  - tg_mean_kl: 0.054
  - base_mean_kl: 0.043
  - gate_kl_correlation: 0.11
  - high_kl_layers: "L23-L27, L9"
  - gar_robustness_ours_tg_base_ratio: 21.4
  - gar_robustness_goal_only_ratio: 63
  - gar_robustness_ours_all_ratio: 1.7
  - gar_robustness_ours_first_ratio: 1.8

---

### 32. p2_llama_gradient_conflict
- **Status:** DONE
- **Model:** Llama-3.1-8B-Instruct
- **Condition:** PCGrad on Llama (gradient conflict analysis)
- **Conclusion:** success
- **Metrics:**
  - cos_sim_mean: 0.0045
  - cos_sim_std: 0.07
  - neg_cos_sim_layers_pct: 53.1
  - mag_ratio_median: 25.7
  - conclusion_note: "cos_sim approx 0 indicates near-orthogonal (NOT conflict). NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern."

---

### 33. phase1_gar_diag
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct (base)
- **Condition:** Base (phase1 diagnostics)
- **Conclusion:** success
- **Per-turn avg GAR (10 turns):**
  - turn1: 0.0418
  - turn2: 0.0241
  - turn3: 0.0224
  - turn4: 0.013
  - turn5: 0.0133
  - turn6: 0.0086
  - turn7: 0.0078
  - turn8: 0.008
  - turn9: 0.0157
  - turn10: 0.0064
- turn1_avg_gar: 0.0418, mid_turns_avg_gar: 0.0122
- relative_drop: 0.708 (70.8%)

---

### 34. phase2_4way_eval
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Conditions:** Base/TG/UG/LoRA (4-way, IID eval)
- **Conclusion:** negative (gating_incremental_benefit: "none")
- **Metrics:**
  - base_ours_mid_gar: 0.0107, base_ppl: 4.23, base_ntp: 1.4162
  - tg_ours_mid_gar: 0.4866, tg_ppl: 2.63, tg_ntp: 0.9484
  - ug_ours_mid_gar: 0.4923, ug_ppl: 2.62, ug_ntp: 0.9433
  - lora_ours_mid_gar: 0.486, lora_ppl: 2.63, lora_ntp: 0.9482
  - base_dongre_mid_gar: 0.003, tg_dongre_mid_gar: 0.0157, ug_dongre_mid_gar: 0.013, lora_dongre_mid_gar: 0.0137

---

### 35. phase2_4way_eval_heldout
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Conditions:** Base/TG/UG/LoRA (4-way, held-out eval)
- **Conclusion:** success (three_way_convergence_confirmed: true)
- **Metrics:**
  - base_ours_mid_gar: 0.0128, base_ppl: 4.34, base_ntp: 1.4045
  - tg_ours_mid_gar: 0.5035, tg_ppl: 2.78, tg_ntp: 0.9771
  - ug_ours_mid_gar: 0.5053, ug_ppl: 2.78, ug_ntp: 0.9752
  - lora_ours_mid_gar: 0.4978, lora_ppl: 2.78, lora_ntp: 0.9771
  - base_dongre_mid_gar: 0.0031, tg_dongre_mid_gar: 0.0152, ug_dongre_mid_gar: 0.0124, lora_dongre_mid_gar: 0.0132
  - gar_ours_spread_pp: 0.75, ppl_spread: 0

---

### 36. phase2_lora_only_s42 (training)
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Condition:** LoRA-only baseline training, seed=42
- **Conclusion:** success
- **Metrics:**
  - epochs_completed: 3, global_steps: 3000
  - training_time_hours: 5.7
  - gate_fixed: 1, gate_type_actual: "none"
  - final_lora_size_mb: 20
  - eval_modelgen_ours_mid_gar: 0.0245
  - eval_modelgen_dongre_mid_gar: 0.0185
  - eval_modelgen_ppl: 1.371

---

### 37. phase2_tg_s42 (v1)
- **Status:** DONE
- **Conclusion:** negative (killed at 1.67 epochs, gar_loss_zero_pct: 87.6%)
- gate_mean: 0.988, final_ntp_loss: 0.94

---

### 38. phase2_tg_s42_v2
- **Status:** DONE
- **Conclusion:** killed

---

### 39. phase2_tg_s42_v3
- **Status:** DONE
- **Conclusion:** negative (gate frozen, GAR indirect gradient too weak)
- gate_mean_step500: 0.8761, gate_delta: 0.004, gate_std: 0.001

---

### 40. phase2_tg_s42_v3b
- **Status:** DONE
- **Conclusion:** success (gate differentiation achieved)
- gate_std_final: 0.087, gate_mean_final: 0.9388
- gate_min_final: 0.5352, gate_max_final: 0.9922
- L4_gate: 0.535, L0_gate: 0.777

---

### 41. phase2_tg_s42_v4
- **Status:** DONE
- **Conclusion:** failed

---

### 42. phase2_tg_s42_v5
- **Status:** DONE
- **Conclusion:** negative
- step2000_gate_std: 0.0225, step2000_gate_mean: 0.9586
- gate_range_compression: "0.918-0.996"

---

### 43. phase2_tg_s42_v6
- **Status:** DONE
- **Conclusion:** negative
- gs100_gate_mean: 0.8737, gs100_gate_std: 0.0367

---

### 44. phase2_tg_s42_v7 (main TG experiment)
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Condition:** TG, seed=42 (MSE target + gate diversity)
- **Conclusion:** success
- **Metrics:**
  - eval_iid_ours_mid_gar: 0.5035
  - eval_iid_dongre_mid_gar: 0.0152
  - eval_iid_ppl: 2.784
  - eval_heldout_ours_mid_gar: 0.5035
  - eval_heldout_dongre_mid_gar: 0.0152
  - eval_heldout_ppl: 2.78
  - eval_modelgen_ours_mid_gar: 0.0157
  - eval_modelgen_dongre_mid_gar: 0.0194
  - eval_modelgen_ppl: 1.36
  - gate_mean_final: 0.9336, gate_std_final: 0.0492

---

### 45. phase2_tg_s42_v8_schedsampling
- **Status:** DONE
- **Conclusion:** failed (killed at 8.1%, SS path bug D026)

---

### 46. phase2_tg_s42_v8b_resume (SS s42 training)
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Condition:** SS (v8b), seed=42
- **Conclusion:** success
- **Training:**
  - total_steps: 3000, epochs_completed: 3, wall_clock_hours: 8.1
  - final_loss: 0.933, final_ntp_loss: 0.9322, final_gar_loss: 0.0008
  - final_gate_mean: 0.9586, final_gate_std: 0.0582, ss_ratio: 0.5
- **Eval IID:** gar_ours=0.4983, gar_dongre=0.3855, ppl=2.78
- **Eval model-gen:** gar_ours=0.3177, gar_dongre=0.3533, ppl=1.38
- **vs v7:**
  - iid_gar_ours_delta: -0.005
  - modelgen_gar_ours_delta: +0.302
  - gap_ratio_v7: 32, gap_ratio_v8b: 1.57

---

### 47. phase2_tg_s42_v8b_ss_fixed (training)
- **Status:** DONE
- **Conclusion:** failed

---

### 48. phase2_tg_s42_v9_pcgrad
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Condition:** PCGrad, seed=42
- **Conclusion:** success
- **Metrics:**
  - eval_iid_ours_mid_gar: 0.5002
  - eval_iid_dongre_mid_gar: 0.0123
  - eval_iid_ppl: 2.78, eval_iid_ntp: 0.9752
  - eval_heldout_ours_mid_gar: 0.5002
  - eval_heldout_dongre_mid_gar: 0.0123
  - eval_heldout_ppl: 2.78
  - eval_modelgen_ours_mid_gar: 0.0151
  - eval_modelgen_dongre_mid_gar: 0.0173
  - eval_modelgen_ppl: 1.5
  - vs_v7_iid_ppl_diff: 0.004, vs_v7_iid_gar_diff: -0.0033

---

### 49. phase2_ug_s42
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Condition:** UG (uniform gate), seed=42
- **Conclusion:** success
- **Training metrics:**
  - final_gate_mean: 0.9598, final_gate_std: 0.0518
  - final_gate_min: 0.7773, final_gate_max: 1
  - eval_modelgen_ours_mid_gar: 0.0149
  - eval_modelgen_dongre_mid_gar: 0.0185
  - eval_modelgen_ppl: 1.396

---

### 50. qwen15b_phase1_diag
- **Status:** DONE
- **Model:** Qwen2.5-1.5B-Instruct
- **Conclusion:** success
- No metrics stored in registry

---

### 51. trc_baseline_v7_tg
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Conditions:** TG v7 / LoRA-only / Base (TRC analysis)
- **Conclusion:** success
- **v7_tg:** tf_trc=0.3339, gen_trc=0.3323, trc_gap=0.0016, tf_tbp_ppl=1.05, gen_tbp_ppl=1.05
- **lora_only:** tf_trc=0.349, gen_trc=0.4106, trc_gap=-0.0617, tf_tbp_ppl=9.5, gen_tbp_ppl=12
- **base:** tf_trc=0.1494, gen_trc=0.1494, trc_gap=0, tf_tbp_ppl=2.05, gen_tbp_ppl=2.05

---

### 52. v7_tg_s123 (training)
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Condition:** TG v7 training, seed=123
- **Conclusion:** success
- **Training metrics:**
  - epoch_1: avg_loss=0.9447, avg_ntp=0.9434, avg_gar=0.0013, avg_div=0
  - epoch_2: avg_loss=0.9315, avg_ntp=0.9305, avg_gar=0.001, avg_div=0
  - final_gate: mean=0.9467, std=0.051, min=0.793, max=1
- **Gate profile (28 layers):** L0=0.883, L1=0.793, L2=0.996, L3=0.988, L4=0.984, L5=0.797, L6=0.961, L7=0.918, L8=0.965, L9=0.934, L10=0.969, L11=0.918, L12=0.926, L13=0.941, L14=0.93, L15=0.965, L16=0.941, L17=0.91, L18=0.961, L19=0.965, L20=0.973, L21=0.988, L22=0.969, L23=0.98, L24=0.98, L25=0.984, L26=0.988, L27=1

---

### 53. v8b_ss_s123 (training)
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Condition:** SS (v8b) training, seed=123
- **Conclusion:** success
- **Metrics:**
  - final_loss: 0.9316, final_ntp_loss: 0.9307, final_gar_loss: 0.0009
  - final_gate_mean: 0.9505, final_gate_std: 0.0508
  - final_gate_min: 0.7383, final_gate_max: 1
  - ss_used_ratio: 0.371
  - training_time_s: 38773.4
  - epoch0_loss: 1.0092, epoch1_loss: 0.9444, epoch2_loss: 0.9316

---

## KEY CROSS-REFERENCES FOR PAPER TABLES

### Multi-seed SS eval results (s42/s123/s456):

| Metric | s42 | s123 | s456 |
|--------|-----|------|------|
| TF GAR-ours | 0.5025 | 0.5536 | 0.4964 |
| TF GAR-Dongre | 0.389 | 0.4106 | 0.3862 |
| AR beta0 GAR | 0.3887 (N=5) | 0.4231 (N=39) | 0.4325 (N=50) |
| AR beta0 PPL | 1.35 | 1.4408 | 1.4394 |
| AR beta3 GAR | -- | 0.5903 | 0.605 |
| AR beta3 PPL | -- | 1.607 | 1.5868 |
| AR beta5 GAR | -- | 0.7174 | 0.7157 |
| AR beta5 PPL | -- | 1.7852 | 1.8045 |

Note: s42 AR was N=5 (early eval), while s123/s456 used N=39-50.

### Multi-seed TG eval results (s42/s123):

| Metric | s42 | s123 |
|--------|-----|------|
| TF GAR-ours mid | 0.5035 | 0.5052 |
| TF GAR-Dongre mid | 0.0152 | 0.0119 |
| TF PPL | 2.784 | 2.7802 |
| AR GAR-ours mid | 0.0157 | 0.0165 |
| AR GAR-Dongre mid | 0.0194 | 0.0177 |
| AR PPL | 1.36 | 1.3855 |
| Gap ratio | 32.1 | 30.6 |

### 6-way AR comparison (d048_final_ar_eval, Qwen, N=39):

| Condition | AR GAR (beta0) | AR PPL |
|-----------|---------------|--------|
| Base | 0.019 | 1.447 |
| TG | 0.064 | 1.432 |
| UG | 0.033 | -- |
| LoRA-only | 0.037 | -- |
| PCGrad | 0.03 | -- |
| SS | 0.347 | 1.442 |

### Llama cross-model results:

**llama_eval_s42:** TF TG GAR-ours=0.4836, AR TG GAR-ours=0.0304, gap_ratio=15.9
**llama_ar_matched_eval (N=50, T=4):** AR Base GAR=0.0082, AR TG GAR=0.0388, TG-over-base=4.71x
**eval_llama_ar_n20 (N=20, T=4, median):** Base=0.0093, TG=0.0179, LO=0.0184 (TG approx LO, gating zero-increment)
**eval_llama_lora_only_s42:** TF GAR-ours=0.4807, AR GAR-ours=0.0617, gap_ratio=7.79
**llama_phase1_gar_diag:** per-turn GAR decay from 0.0263 (turn 1) to 0.0026 (turn 10), 90.1% decay
**p2_llama_gradient_conflict:** cos_sim_mean=0.0045 (near-orthogonal, NOT conflict), neg_cos_sim_layers_pct=53.1
**p1_llama_ss_training:** STILL RUNNING (no results yet)

### MMLU 5-shot (general capability preservation):

Base=0.7423, PCGrad=0.7386, SS=0.7375, LO=0.7357, TG=0.7347, UG=0.7346

All within ~0.8pp of base, confirming no capability degradation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb6093c0-203c-45a5-bf29-c540176342fc",
  "isSidechain": true,
  "agentId": "a8867062004a08a3c",
  "requestId": "req_011CbMc25BghmoqHqDvfNrkm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2d9d692-5742-404a-9c87-2bb92ce89dcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "66de9ef3-78db-4116-ae9e-2eba3b117097",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01997Cd7aH6i69mCiYYaypYG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1528,
      "cache_read_input_tokens": 66695,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1528,
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
