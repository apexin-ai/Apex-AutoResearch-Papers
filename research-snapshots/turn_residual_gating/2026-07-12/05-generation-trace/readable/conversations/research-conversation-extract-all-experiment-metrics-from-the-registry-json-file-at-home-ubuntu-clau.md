# Research conversation: Extract all experiment metrics from the registry JSON file at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--age

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a24bf7311cd045b90.jsonl`
- **Structured JSON:** [`5b1c132ebf7bbad07cc5.json`](../../sessions/5b/5b1c132ebf7bbad07cc5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

35 recorded events

### User

_source line 1 · 2026-05-25T20:12:48.825Z_

Extract all experiment metrics from the registry JSON file at:
/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt

This is a JSON file with schema: {result: string}. The `result` field contains the actual registry data as a string (likely JSON itself).

I need you to extract the following for EVERY experiment entry:
1. Experiment ID/name
2. Status
3. All metrics (especially GAR-ours TF, GAR-ours AR, GAR-Dongre TF, GAR-Dongre AR, PPL, TF/AR gap ratios, MMLU scores)
4. Spec info (model, lr, batch_size, epochs, steps, LoRA rank, dataset size, seed)
5. Any scheduled sampling related metrics
6. Any cross-model (Llama) related metrics
7. Any steering ($\beta$) related metrics
8. Any gradient statistics (cosine similarity, magnitude ratios)
9. Any instruction retention / compliance metrics
10. Any TRC (Turn-level Residual Coherence) values

Use bash with jq or python to parse. Report ALL numbers verbatim - do not summarize or round. I need exact values for an audit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1f7ff205-71d0-4ca7-a71f-3ee7850be97d",
  "agentId": "a24bf7311cd045b90",
  "type": "user",
  "uuid": "ff4beb4a-bfc6-4743-9700-cacfe53e0c6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T20:12:48.831Z_

```json
{
  "parentUuid": "ff4beb4a-bfc6-4743-9700-cacfe53e0c6e",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__compare_wandb_runs",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__fetch_wandb_run_history",
      "mcp__agent-ml-research__get_best_wandb_run",
      "mcp__agent-ml-research__list_wandb_runs",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__compare_wandb_runs",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__fetch_wandb_run_history",
      "mcp__agent-ml-research__get_best_wandb_run",
      "mcp__agent-ml-research__list_wandb_runs",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "ac461365-a761-43b8-943a-fe3233ae83e2",
  "timestamp": "2026-05-25T20:12:48.831Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-25T20:12:52.039Z_



I'll parse the registry file and extract all experiment metrics. Let me start by reading the file to understand its structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac461365-a761-43b8-943a-fe3233ae83e2",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu27hEmw1cthivdm3Nj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee00c93d-ccee-4a09-ac79-f6684def9582",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013fGgg4W1CSwHoeb8KKWHtX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16598,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16598,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 4 · 2026-05-25T20:12:52.800Z_

<details open><summary>🔧 Tool call — Read · `toolu_01633ThTkqkTj78kCzLzRs5e`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee00c93d-ccee-4a09-ac79-f6684def9582",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu27hEmw1cthivdm3Nj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4af11985-9d25-452b-b228-b1858bb27e83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013fGgg4W1CSwHoeb8KKWHtX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16598,
      "cache_read_input_tokens": 0,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16598
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 188,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16598,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16598,
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

_source line 5 · 2026-05-25T20:12:53.179Z_

<details><summary>↩ Tool result · reported error · `toolu_01633ThTkqkTj78kCzLzRs5e`</summary>

```text
File content (45595 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4af11985-9d25-452b-b228-b1858bb27e83",
  "isSidechain": true,
  "promptId": "1f7ff205-71d0-4ca7-a71f-3ee7850be97d",
  "agentId": "a24bf7311cd045b90",
  "type": "user",
  "uuid": "cca3c309-dd34-4dbf-8720-ed83e17f225a",
  "toolUseResult": "Error: File content (45595 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "4af11985-9d25-452b-b228-b1858bb27e83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-25T20:12:56.515Z_

The file is large. Let me read it in chunks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cca3c309-dd34-4dbf-8720-ed83e17f225a",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu2SUb6GHQ8MVazvxW3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a21d0733-9521-48d4-aef2-ecc525be3de8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XQyb8ANEsjigCMqs5LEYZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1090,
      "cache_read_input_tokens": 16598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1090,
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

_source line 7 · 2026-05-25T20:12:57.402Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MW1mia76wzWPS75Yg7jCwY`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a21d0733-9521-48d4-aef2-ecc525be3de8",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu2SUb6GHQ8MVazvxW3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34c1d83b-9063-4705-89bd-24199e343283",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XQyb8ANEsjigCMqs5LEYZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1090,
      "cache_read_input_tokens": 16598,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1090
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 16598,
          "cache_creation_input_tokens": 1090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1090,
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

_source line 8 · 2026-05-25T20:12:57.727Z_

<details><summary>↩ Tool result · reported error · `toolu_01MW1mia76wzWPS75Yg7jCwY`</summary>

```text
File content (45595 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34c1d83b-9063-4705-89bd-24199e343283",
  "isSidechain": true,
  "promptId": "1f7ff205-71d0-4ca7-a71f-3ee7850be97d",
  "agentId": "a24bf7311cd045b90",
  "type": "user",
  "uuid": "947dc03a-fe77-4eab-a7e6-4ee00a8b954c",
  "toolUseResult": "Error: File content (45595 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "34c1d83b-9063-4705-89bd-24199e343283",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T20:13:04.604Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ThjHj3X5Pn3Ti9xNXJfy6j`</summary>

```json
{
  "command": "wc -l \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt\"",
  "description": "Count lines in registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "947dc03a-fe77-4eab-a7e6-4ee00a8b954c",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu2n54Viqi5TcmZqhcG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61f40828-b14e-439d-9f68-147418ec112d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YAoLoNN5YKLsAEzSSEcBMh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 17688,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 236
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 17688,
          "cache_creation_input_tokens": 236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 236,
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

_source line 10 · 2026-05-25T20:13:04.762Z_

<details><summary>↩ Tool result · `toolu_01ThjHj3X5Pn3Ti9xNXJfy6j`</summary>

```text
0 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61f40828-b14e-439d-9f68-147418ec112d",
  "isSidechain": true,
  "promptId": "1f7ff205-71d0-4ca7-a71f-3ee7850be97d",
  "agentId": "a24bf7311cd045b90",
  "type": "user",
  "uuid": "25bf9655-d485-4e94-842a-a66be49f1951",
  "sourceToolAssistantUUID": "61f40828-b14e-439d-9f68-147418ec112d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-25T20:13:07.136Z_

It's a single-line JSON file. Let me use Python to parse it properly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25bf9655-d485-4e94-842a-a66be49f1951",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu3HhXNisU3DFAgRJPQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b0ec9a0-fa29-4b9d-ab37-6b7b44b9d212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KiWy8VJrys5jNy6S9CwmGt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 277,
      "cache_read_input_tokens": 17924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 277,
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

_source line 12 · 2026-05-25T20:13:10.264Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01A8mWowKD2egcsJJEePuLSc`</summary>

```json
{
  "command": "python3 -c \"\nimport json, sys\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt') as f:\n    raw = json.load(f)\n\n# The outer wrapper has a 'result' field containing string\nresult_str = raw.get('result', '')\nprint(f'Type of result: {type(result_str)}')\nprint(f'Length of result string: {len(result_str)}')\nprint(f'First 500 chars: {result_str[:500]}')\n\"\n",
  "description": "Parse outer JSON structure and inspect result field"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b0ec9a0-fa29-4b9d-ab37-6b7b44b9d212",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu3HhXNisU3DFAgRJPQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93c56f3e-8606-4d99-a9e5-85771d67c49a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KiWy8VJrys5jNy6S9CwmGt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 277,
      "cache_read_input_tokens": 17924,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 277
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 298,
          "cache_read_input_tokens": 17924,
          "cache_creation_input_tokens": 277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 277,
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

_source line 13 · 2026-05-25T20:13:10.347Z_

<details><summary>↩ Tool result · `toolu_01A8mWowKD2egcsJJEePuLSc`</summary>

```text
Type of result: &lt;class 'str'>
Length of result string: 91546
First 500 chars: {"success": true, "data": {"experiments": {"phase1a_multiseed_qwen": {"status": "DONE", "retry_count": 0, "created_at": "2026-05-25T06:15:26.051Z", "updated_at": "2026-05-25T11:20:34.089Z", "hypothesis": "Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.", "spec": {"command": "python src/train_phase2_v9_pcgrad
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93c56f3e-8606-4d99-a9e5-85771d67c49a",
  "isSidechain": true,
  "promptId": "1f7ff205-71d0-4ca7-a71f-3ee7850be97d",
  "agentId": "a24bf7311cd045b90",
  "type": "user",
  "uuid": "f88c30db-1e28-464d-895a-f1e34c957f8f",
  "sourceToolAssistantUUID": "93c56f3e-8606-4d99-a9e5-85771d67c49a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T20:13:15.357Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012GSK2oEWa6ch27yjRvSL25`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt') as f:\n    raw = json.load(f)\n\nresult_str = raw['result']\ndata = json.loads(result_str)\n\nexperiments = data['data']['experiments']\nprint(f\"Total experiments: {len(experiments)}\")\nprint(f\"Experiment IDs: {list(experiments.keys())}\")\nPYEOF\n",
  "description": "Parse inner JSON and list all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f88c30db-1e28-464d-895a-f1e34c957f8f",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu3hchMbqVoePUEv4fc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d313dbbc-d36d-4d7d-bdf7-826718b145c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016thsbAtsC7BWPXL5fXVmEA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 525,
      "cache_read_input_tokens": 18201,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 525
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 265,
          "cache_read_input_tokens": 18201,
          "cache_creation_input_tokens": 525,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 525,
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

_source line 15 · 2026-05-25T20:13:15.436Z_

<details><summary>↩ Tool result · `toolu_012GSK2oEWa6ch27yjRvSL25`</summary>

```text
Total experiments: 60
Experiment IDs: ['phase1a_multiseed_qwen', 'p1_ss_lora_only', 'phase2_switching', 'phase2_tf_ar_switching', 'phase1a_multiseed_8runs', 'phase1b_llama_complement', 'p1_llama_ss_eval', 'p1_llama_ss_training', 'mmlu_eval_all', 'p2_llama_gradient_conflict', 'p1_tf_ar_kl_divergence', 'qwen15b_phase1_diag', 'd048_eval_ss_s456', 'd048_ss_s456', 'p0_ss_steering_eval', 'd048_eval_ss_s123', 'd048_ss_s123', 'd048_split_softmax_eval', 'd048_final_ar_eval', 'd048_queue_runner', 'd048_eval_ss_s42', 'd048_ss_s42', 'd048_ss_s42_resume', 'eval_llama_ar_n20', 'eval_llama_lora_only_s42', 'llama_lora_only_s42', 'phase2_tg_s42_v6', 'phase2_tg_s42', 'eval_v7_tg_s123', 'eval_v8b_ss_s123', 'v7_tg_s123', 'v8b_ss_s123', 'llama_tg_training', 'llama_ar_matched_eval', 'instruction_retention_test', 'llama_eval_s42', 'llama_tg_s42', 'attention_steering_gen_n50', 'phase2_tg_s42_v8b_resume', 'llama_phase1_gar_diag', 'eval_v8b_ss', 'attention_steering_eval200_tf', 'trc_baseline_v7_tg', 'attention_steering_v7_tg_gen', 'phase2_tg_s42_v8b_ss_fixed', 'phase2_tg_s42_v7', 'phase2_tg_s42_v9_pcgrad', 'phase2_lora_only_s42', 'phase2_ug_s42', 'phase2_tg_s42_v8_schedsampling', 'analysis_attention_heatmap', 'analysis_gradient_conflict', 'phase2_4way_eval_heldout', 'phase2_4way_eval', 'phase2_tg_s42_v5', 'phase2_tg_s42_v4', 'phase2_tg_s42_v3b', 'phase2_tg_s42_v3', 'phase2_tg_s42_v2', 'phase1_gar_diag']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d313dbbc-d36d-4d7d-bdf7-826718b145c8",
  "isSidechain": true,
  "promptId": "1f7ff205-71d0-4ca7-a71f-3ee7850be97d",
  "agentId": "a24bf7311cd045b90",
  "type": "user",
  "uuid": "e29395e0-3326-4d57-a74d-0dbfda6368bb",
  "sourceToolAssistantUUID": "d313dbbc-d36d-4d7d-bdf7-826718b145c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-25T20:13:17.799Z_

60 experiments. Now let me extract all data from each one comprehensively.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e29395e0-3326-4d57-a74d-0dbfda6368bb",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu45Rrz81unf2wtP3H8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71c809f2-30d5-43ec-b265-8e6ed14bdcd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJyHLPJbEy7mY4AFNwc5uK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1007,
      "cache_read_input_tokens": 18726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1007,
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

_source line 17 · 2026-05-25T20:13:21.118Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DttCStKLVMmf9dyYLsvWNd`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt') as f:\n    raw = json.load(f)\n\nresult_str = raw['result']\ndata = json.loads(result_str)\nexperiments = data['data']['experiments']\n\n# Dump each experiment fully, one at a time\nfor exp_id in sorted(experiments.keys()):\n    exp = experiments[exp_id]\n    print(f\"\\n{'='*80}\")\n    print(f\"EXPERIMENT: {exp_id}\")\n    print(f\"{'='*80}\")\n    print(json.dumps(exp, indent=2, ensure_ascii=False))\n\nPYEOF\n",
  "description": "Dump all experiments with full details",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71c809f2-30d5-43ec-b265-8e6ed14bdcd6",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu45Rrz81unf2wtP3H8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "677e991f-1e04-49d1-8f18-0954cbcd79bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJyHLPJbEy7mY4AFNwc5uK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1007,
      "cache_read_input_tokens": 18726,
      "output_tokens": 359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1007
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 359,
          "cache_read_input_tokens": 18726,
          "cache_creation_input_tokens": 1007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1007,
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

_source line 18 · 2026-05-25T20:13:21.200Z_

<details><summary>↩ Tool result · `toolu_01DttCStKLVMmf9dyYLsvWNd`</summary>

```text
&lt;persisted-output>
Output too large (113.4KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt

Preview (first 2KB):
================================================================================
EXPERIMENT: analysis_attention_heatmap
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-19T15:03:16.154Z",
  "updated_at": "2026-05-19T15:22:24.770Z",
  "hypothesis": "四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。",
  "parent": "phase2_tg_s42_v7",
  "spec": {
    "command": "attention heatmap analysis script",
    "server": "westd-20861",
    "data_path": "standard_conversations.json",
    "data_count": 5,
    "model_name": "Qwen2.5-7B-Instruct",
    "seed": 42,
    "checkpoint_source": "phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42",
    "eval_data": "standard_conversations.json (5 convs x 10 turns)",
    "checkpoint_path": "N/A (analysis)",
    "log_path": "westd-20861:/root/turn_residual_gating/runs/analysis/"
  },
  "conclusion": "success",
  "metrics": {
    "base_mean_goal_attn": 0.0136,
    "base_decay": 0.875,
    "tg_mean_goal_attn": 0.0232,
    "tg_decay": 0.777,
    "ug_mean_goal_attn": 0.0216,
    "ug_decay": 0.803,
    "lora_mean_goal_attn": 0.0216,
    "lora_decay": 0.81,
    "gating_incremental_benefit": "none"
  },
  "completed_at": "2026-05-19T15:22:24.770Z"
}

================================================================================
EXPERIMENT: analysis_gradient_conflict
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-19T15:03:12.230Z",
  "updated_at": "2026-05-19T15:22:23.782Z",
  "hypothesis": "NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。",
  "parent": "phase2_tg_s42_v7",
  "spec": {
    "command": "gradient conflict analysis script",
    "server": "westd-20861",
    "data_path": "v7 epoch 0/1/2 checkpoints",
    "data_count": 3,
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "677e991f-1e04-49d1-8f18-0954cbcd79bb",
  "isSidechain": true,
  "promptId": "1f7ff205-71d0-4ca7-a71f-3ee7850be97d",
  "agentId": "a24bf7311cd045b90",
  "type": "user",
  "uuid": "dc473b8b-84c4-4d0f-9652-dbd37483309b",
  "sourceToolAssistantUUID": "677e991f-1e04-49d1-8f18-0954cbcd79bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-25T20:13:23.833Z_

The full output is saved. Let me read it in sections to extract everything.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc473b8b-84c4-4d0f-9652-dbd37483309b",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu4Vyyu24y5cWHSFyTU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3adc1f5c-987b-41e6-bcb0-e5cb18e342fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012EZsHeALPiuuQucsgJthq5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1402,
      "cache_read_input_tokens": 19733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1402,
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

_source line 20 · 2026-05-25T20:13:24.712Z_

<details open><summary>🔧 Tool call — Read · `toolu_018Ah3YDkx6WjdEDVkKDnu3t`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3adc1f5c-987b-41e6-bcb0-e5cb18e342fd",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu4Vyyu24y5cWHSFyTU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "627a9441-3ed3-4e5a-9588-2745b62e9689",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012EZsHeALPiuuQucsgJthq5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1402,
      "cache_read_input_tokens": 19733,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1402
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 19733,
          "cache_creation_input_tokens": 1402,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1402,
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

_source line 21 · 2026-05-25T20:13:24.718Z_

<details><summary>↩ Tool result · `toolu_018Ah3YDkx6WjdEDVkKDnu3t`</summary>

```text
1	
2	================================================================================
3	EXPERIMENT: analysis_attention_heatmap
4	================================================================================
5	{
6	  "status": "DONE",
7	  "retry_count": 0,
8	  "created_at": "2026-05-19T15:03:16.154Z",
9	  "updated_at": "2026-05-19T15:22:24.770Z",
10	  "hypothesis": "四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。",
11	  "parent": "phase2_tg_s42_v7",
12	  "spec": {
13	    "command": "attention heatmap analysis script",
14	    "server": "westd-20861",
15	    "data_path": "standard_conversations.json",
16	    "data_count": 5,
17	    "model_name": "Qwen2.5-7B-Instruct",
18	    "seed": 42,
19	    "checkpoint_source": "phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42",
20	    "eval_data": "standard_conversations.json (5 convs x 10 turns)",
21	    "checkpoint_path": "N/A (analysis)",
22	    "log_path": "westd-20861:/root/turn_residual_gating/runs/analysis/"
23	  },
24	  "conclusion": "success",
25	  "metrics": {
26	    "base_mean_goal_attn": 0.0136,
27	    "base_decay": 0.875,
28	    "tg_mean_goal_attn": 0.0232,
29	    "tg_decay": 0.777,
30	    "ug_mean_goal_attn": 0.0216,
31	    "ug_decay": 0.803,
32	    "lora_mean_goal_attn": 0.0216,
33	    "lora_decay": 0.81,
34	    "gating_incremental_benefit": "none"
35	  },
36	  "completed_at": "2026-05-19T15:22:24.770Z"
37	}
38	
39	================================================================================
40	EXPERIMENT: analysis_gradient_conflict
41	================================================================================
42	{
43	  "status": "DONE",
44	  "retry_count": 0,
45	  "created_at": "2026-05-19T15:03:12.230Z",
46	  "updated_at": "2026-05-19T15:22:23.782Z",
47	  "hypothesis": "NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。",
48	  "parent": "phase2_tg_s42_v7",
49	  "spec": {
50	    "command": "gradient conflict analysis script",
51	    "server": "westd-20861",
52	    "data_path": "v7 epoch 0/1/2 checkpoints",
53	    "data_count": 3,
54	    "model_name": "Qwen2.5-7B-Instruct",
55	    "seed": 42,
56	    "checkpoint_source": "phase2_tg_s42_v7",
57	    "eval_data": "v7 3-epoch checkpoints (gradient analysis)",
58	    "checkpoint_path": "N/A (analysis)",
59	    "log_path": "westd-20861:/root/turn_residual_gating/runs/analysis/"
60	  },
61	  "conclusion": "success",
62	  "metrics": {
63	    "epoch0_cos_sim": -0.089,
64	    "epoch1_cos_sim": -0.054,
65	    "epoch2_cos_sim": -0.042,
66	    "epoch0_neg_layers_pct": 78.6,
67	    "epoch1_neg_layers_pct": 71.4,
68	    "epoch2_neg_layers_pct": 67.9,
69	    "epoch0_mag_ratio": 7.5,
70	    "epoch1_mag_ratio": 13.7,
71	    "epoch2_mag_ratio": 14.7
72	  },
73	  "completed_at": "2026-05-19T15:22:23.782Z"
74	}
75	
76	================================================================================
77	EXPERIMENT: attention_steering_eval200_tf
78	================================================================================
79	{
80	  "status": "DONE",
81	  "retry_count": 0,
82	  "created_at": "2026-05-20T09:58:23.626Z",
83	  "updated_at": "2026-05-20T10:08:24.710Z",
84	  "hypothesis": "N=200 TF 模式 attention steering 验证 β-GAR 关系的统计鲁棒性。在 teacher-forced context (无 exposure bias) 下，steering 效果应更温和（baseline GAR 已 ~0.50），但仍展示 β 调控 attention 的能力。与 N=5 gen 模式结果互补：tf 验证机制可控性，gen 验证因果闭环。",
85	  "parent": "attention_steering_v7_tg_gen",
86	  "spec": {
87	    "command": "python src/eval_attention_steering.py --mode tf --betas 0 2 3 4 5 10 --output-name eval200_attention_steering.json (data: eval_200/eval_200.json, 200 convs)",
88	    "server": "westd-20861",
89	    "data_path": "data/eval_200/eval_200.json",
90	    "data_count": 200,
91	    "model_name": "Qwen2.5-7B-Instruct",
92	    "seed": 42,
93	    "checkpoint_source": "phase2_tg_s42_v7",
94	    "eval_data": "data/eval_200/eval_200.json",
95	    "checkpoint_path": "checkpoints/tg_v7_s42/final",
96	    "log_path": "/tmp/eval200_steering.log"
97	  },
98	  "metrics": {
99	    "beta_0.0": {
100	      "mid_gar": 0.5353,
101	      "ppl": 2.62
102	    },
103	    "beta_2.0": {
104	      "mid_gar": 0.6112,
105	      "ppl": 2.69
106	    },
107	    "beta_3.0": {
108	      "mid_gar": 0.788,
109	      "ppl": 2.93
110	    },
111	    "beta_4.0": {
112	      "mid_gar": 0.8165,
113	      "ppl": 3.49
114	    },
115	    "beta_5.0": {
116	      "mid_gar": 0.8325,
117	      "ppl": 6.15
118	    },
119	    "beta_10.0": {
120	      "mid_gar": 0.977,
121	      "ppl": 505.21
122	    },
123	    "n_convs": 200,
124	    "mode": "tf"
125	  },
126	  "conclusion": "success",
127	  "completed_at": "2026-05-20T10:08:24.710Z"
128	}
129	
130	================================================================================
131	EXPERIMENT: attention_steering_gen_n50
132	================================================================================
133	{
134	  "status": "DONE",
135	  "retry_count": 0,
136	  "created_at": "2026-05-20T19:04:17.455Z",
137	  "updated_at": "2026-05-21T01:59:57.100Z",
138	  "hypothesis": "N=5 gen steering 显示 β∈[2,5] phase transition (GAR 0.06→0.68)，但样本量不足以报告置信区间。N=50 conversations 应重现同一 phase transition pattern 并提供统计鲁棒的 mean±std，加固 C6 claim (attention steering as causal mechanism proof)。",
139	  "parent": "attention_steering_v7_tg_gen",
140	  "spec": {
141	    "command": "CUDA_VISIBLE_DEVICES=0 python src/eval_attention_steering.py --checkpoint runs/phase2_tg_s42_v7 --mode gen --data-file data/eval_200/eval_200.json --max-convs 50 --beta 0 2 3 4 5 10 --output-dir runs/attention_steering/ --output-name attention_steering_gen_n50",
142	    "server": "westd-20861",
143	    "gpu": [
144	      "cuda:0"
145	    ],
146	    "data_path": "data/eval_200/eval_200.json",
147	    "data_count": 50,
148	    "model_name": "Qwen2.5-7B-Instruct + v7 TG LoRA",
149	    "seed": "N/A (eval)",
150	    "checkpoint_source": "phase2_tg_s42_v7",
151	    "eval_data": "50 conversations from eval_200.json, gen mode autoregressive",
152	    "checkpoint_path": "N/A (eval experiment)",
153	    "log_path": "/root/turn_residual_gating/runs/attention_steering/attention_steering_gen_n50.json"
154	  },
155	  "metrics": {
156	    "corrected": true,
157	    "aggregation": "per-conv mid_gar(turns 2-7), >=3 turns only",
158	    "beta_0.0": {
159	      "mid_gar": 0.0641,
160	      "mid_gar_std": 0.0809,
161	      "ppl": 1.4324,
162	      "ppl_std": 0.1029,
163	      "n_valid": 39
164	    },
165	    "beta_2.0": {
166	      "mid_gar": 0.128,
167	      "mid_gar_std": 0.1101,
168	      "ppl": 1.4822,
169	      "ppl_std": 0.1385,
170	      "n_valid": 39
171	    },
172	    "beta_3.0": {
173	      "mid_gar": 0.5558,
174	      "mid_gar_std": 0.0601,
175	      "ppl": 1.5605,
176	      "ppl_std": 0.1719,
177	      "n_valid": 39
178	    },
179	    "beta_4.0": {
180	      "mid_gar": 0.6439,
181	      "mid_gar_std": 0.0607,
182	      "ppl": 1.6674,
183	      "ppl_std": 0.2241,
184	      "n_valid": 39
185	    },
186	    "beta_5.0": {
187	      "mid_gar": 0.7271,
188	      "mid_gar_std": 0.0605,
189	      "ppl": 1.7723,
190	      "ppl_std": 0.2693,
191	      "n_valid": 38
192	    },
193	    "beta_10.0": {
194	      "mid_gar": 0.9612,
195	      "mid_gar_std": 0.0152,
196	      "ppl": 3.4517,
197	      "ppl_std": 1.7813,
198	      "n_valid": 39
199	    },
200	    "n_convs_total": 50,
201	    "n_convs_valid": 39,
202	    "mode": "gen",
203	    "phase_transition_range": "[2, 3]"
204	  },
205	  "conclusion": "success",
206	  "notes": "原始聚合有 min_turns 截断 bug（截到 2 turns），修正后用 per-conv mid_gar(turns 2-7)。39/50 对话有 ≥3 turns 参与统计。修正后 baseline β=0 GAR 从 0.101 降到 0.064（median 0.031 与 N=5 的 0.028 一致）。Phase transition 在 β∈[2,3] 重现。β=10 corrected 0.961 ≈ N=5 的 0.959。",
207	  "completed_at": "2026-05-20T19:55:34.383Z"
208	}
209	
210	================================================================================
211	EXPERIMENT: attention_steering_v7_tg_gen
212	================================================================================
213	{
214	  "status": "DONE",
215	  "retry_count": 0,
216	  "created_at": "2026-05-20T07:07:20.607Z",
217	  "updated_at": "2026-05-20T09:30:17.530Z",
218	  "hypothesis": "推理时向 attention logits 注入 goal-position bias β 可恢复 autoregressive GAR。如果 GAR 从 0.015 显著提升 → 闭合因果环：exposure bias → attention 偏移 → GAR 坍塌 → 手动修正注意力 → GAR 恢复。扫描 β ∈ {0, 0.5, 1.0, 2.0, 5.0, 10.0}，成功标准：GAR > 0.1 且 PPL 不严重恶化。",
219	  "parent": "phase2_tg_s42_v7",
220	  "spec": {
221	    "command": "bash scripts/launch_attention_steering.sh gen",
222	    "server": "westd-20861",
223	    "gpu": [
224	      "cuda:0"
225	    ],
226	    "pid": "157657",
227	    "log_path": "runs/attention_steering/phase2_tg_s42_v7_attention_steering.json",
228	    "submitted_at": "2026-05-20T07:07:27.678Z",
229	    "submitted_via": "submit_training_job",
230	    "backend": "tmux",
231	    "account": "root",
232	    "data_path": "data/ShareGPT_V3_format_5convs.json",
233	    "data_count": 5,
234	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
235	    "seed": 42,
236	    "checkpoint_source": "phase2_tg_s42_v7",
237	    "eval_data": "data/ShareGPT_V3_format_5convs.json",
238	    "checkpoint_path": "checkpoints/tg_v7_s42/final",
239	    "wall_clock_seconds": 8551.2,
240	    "gpu_hours": 2.38
241	  },
242	  "conclusion": "success",
243	  "completed_at": "2026-05-20T09:29:58.880Z",
244	  "metrics": {
245	    "beta_0.0": {
246	      "mid_turns_avg_gar": 0.028,
247	      "avg_ppl": 1.409
248	    },
249	    "beta_0.5": {
250	      "mid_turns_avg_gar": 0.0287,
251	      "avg_ppl": 1.387
252	    },
253	    "beta_1.0": {
254	      "mid_turns_avg_gar": 0.0349,
255	      "avg_ppl": 1.36
256	    },
257	    "beta_2.0": {
258	      "mid_turns_avg_gar": 0.062,
259	      "avg_ppl": 1.411
260	    },
261	    "beta_5.0": {
262	      "mid_turns_avg_gar": 0.6795,
263	      "avg_ppl": 1.908
264	    },
265	    "beta_10.0": {
266	      "mid_turns_avg_gar": 0.959,
267	      "avg_ppl": 4.22
268	    },
269	    "phase_transition_range": "[2, 5]",
270	    "baseline_gar": 0.028,
271	    "max_gar_at_acceptable_ppl": 0.6795,
272	    "max_gar_at_acceptable_ppl_beta": 5
273	  },
274	  "notes": "Attention steering 闭合因果环。β=0→2: GAR 缓升 (0.028→0.062), PPL 不变 (~1.4); β=5: phase transition, GAR 跳至 0.68, PPL 升至 1.91; β=10: GAR 饱和 0.96, PPL 恶化 4.22。成功标准 (GAR>0.1 且 PPL 不严重恶化) 在 β=2 即满足。β∈[2,5] 存在 phase transition。证明：手动修正 attention 指向 goal tokens → 直接恢复 GAR → 确认 exposure bias 通过 attention 偏移导致 GAR 坍塌。"
275	}
276	
277	================================================================================
278	EXPERIMENT: d048_eval_ss_s123
279	================================================================================
280	{
281	  "status": "DONE",
282	  "retry_count": 0,
283	  "created_at": "2026-05-23T17:29:13.803Z",
284	  "updated_at": "2026-05-23T18:05:41.813Z",
285	  "hypothesis": "SS s123 eval: TF + AR N=50 + bootstrap CI to establish multi-seed SS metrics. Expect TF GAR ~0.50, AR GAR similar to s42 (0.347), confirming SS effectiveness across seeds.",
286	  "parent": "d048_ss_s123",
287	  "spec": {
288	    "command": "bash scripts/d048_eval_ss_s123.sh",
289	    "server": "westd-20861",
290	    "pid": "110052",
291	    "data_path": "/root/turn-residual-gating/data/eval_200/eval_200.json",
292	    "data_count": 200,
293	    "model_name": "Qwen/Qwen2.5-7B-Instruct + SS s123 LoRA",
294	    "seed": 123,
295	    "gpu": 0,
296	    "checkpoint_source": "/root/turn-residual-gating/runs/d048_ss_s123/epoch_2",
297	    "eval_data": "/root/turn-residual-gating/data/eval_200/eval_200.json",
298	    "checkpoint_path": "/root/turn-residual-gating/results/d048_final_ar/",
299	    "log_path": "/root/turn-residual-gating/results/d048_final_ar/"
300	  },
301	  "notes": "Cron误判修复: 原PID 109385是TF eval子进程,退出后cron 5次检测失败auto-resolved为failed。实际AR eval PID 110052仍在运行。已手动恢复RUNNING。",
302	  "conclusion": "success",
303	  "completed_at": "2026-05-23T18:05:35.103Z",
304	  "metrics": {
305	    "tf_gar_ours": 0.5536,
306	    "tf_gar_dongre": 0.4106,
307	    "tf_ppl": 2.6123,
308	    "ar_beta0_gar": 0.4231,
309	    "ar_beta0_ppl": 1.4408,
310	    "ar_beta3_gar": 0.5903,
311	    "ar_beta3_ppl": 1.607,
312	    "ar_beta5_gar": 0.7174,
313	    "ar_beta5_ppl": 1.7852,
314	    "n_convs_tf": 200,
315	    "n_convs_ar": 39
316	  }
317	}
318	
319	================================================================================
320	EXPERIMENT: d048_eval_ss_s42
321	================================================================================
322	{
323	  "status": "DONE",
324	  "retry_count": 0,
325	  "created_at": "2026-05-22T22:52:15.395Z",
326	  "updated_at": "2026-05-22T23:32:26.276Z",
327	  "spec": {
328	    "command": "bash scripts/d048_eval_ss_s42.sh",
329	    "server": "westd-20861",
330	    "gpu": [
331	      "cuda:0"
332	    ],
333	    "pid": "48241",
334	    "log_path": "/root/turn_residual_gating/runs/d048_ss_s42/eval.log",
335	    "submitted_at": "2026-05-22T22:52:15.275Z",
336	    "submitted_via": "submit_training_job",
337	    "backend": "tmux",
338	    "account": "root",
339	    "data_path": "data/ultrachat_8k + model-gen AR N=50",
340	    "data_count": 50,
341	    "model_name": "Qwen2.5-7B-Instruct (SS s42)",
342	    "seed": 42,
343	    "checkpoint_source": "runs/d048_ss_s42/epoch_2",
344	    "eval_data": "ultrachat_eval_heldout 50 + model-gen AR N=50",
345	    "checkpoint_path": "runs/d048_ss_s42/epoch_2",
346	    "wall_clock_seconds": 1365.5,
347	    "gpu_hours": 0.38
348	  },
349	  "hypothesis": "D048 multi-seed SS s42 eval: TF + AR N=50 + bootstrap CI (curve[2:]) to establish mean±std for scheduled sampling. Expect TF GAR ~0.50, AR GAR gap < 2× (vs base ~31×), PPL stable.",
350	  "parent": "d048_ss_s42",
351	  "reproduce": {
352	    "finished_at": "2026-05-22T23:12:55.735Z"
353	  },
354	  "extra": {
355	    "hook_events": [
356	      {
357	        "event": "on_complete",
358	        "action": "agent",
359	        "ts": "2026-05-22T23:12:58.142628+00:00"
360	      }
361	    ]
362	  },
363	  "metrics": {
364	    "tf": {
365	      "base_gar_ours_mid": 0.0128,
366	      "base_gar_dongre_mid": 0.0031,
367	      "base_ppl": 4.34,
368	      "base_ntp": 1.4,
369	      "tg_gar_ours_mid": 0.5025,
370	      "tg_gar_dongre_mid": 0.389,
371	      "tg_ppl": 2.78,
372	      "tg_ntp": 0.98,
373	      "baseline_mid_gar": 0.0122
374	    },
375	    "ar": {
376	      "gar_ours_mid": 0.3887,
377	      "gar_ours_ci_95": [
378	        0.3692,
379	        0.3934
380	      ],
381	      "ppl": 1.35
382	    },
383	    "gap_ratio": 1.29,
384	    "n_conversations_tf": 50,
385	    "n_conversations_ar": 5,
386	    "bootstrap_turns": "curve[2:] (turns 3-T)",
387	    "note": "AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch with eval_200.json N=50."
388	  },
389	  "conclusion": "success",
390	  "completed_at": "2026-05-22T23:15:00.734Z"
391	}
392	
393	================================================================================
394	EXPERIMENT: d048_eval_ss_s456
395	================================================================================
396	{
397	  "status": "DONE",
398	  "retry_count": 0,
399	  "created_at": "2026-05-24T00:38:41.913Z",
400	  "updated_at": "2026-05-24T01:19:46.692Z",
401	  "hypothesis": "SS s456 eval: TF + AR N=50 + bootstrap CI to complete 3-seed SS metrics. Together with s42 and s123, establishes mean±std for C2 reviewer requirement.",
402	  "parent": "d048_ss_s456",
403	  "spec": {
404	    "command": "bash scripts/d048_eval_ss_s456.sh",
405	    "server": "westd-20861",
406	    "pid": "129280",
407	    "data_path": "/root/turn-residual-gating/data/eval_200/eval_200.json",
408	    "data_count": 200,
409	    "model_name": "Qwen/Qwen2.5-7B-Instruct + SS s456 LoRA",
410	    "seed": 456,
411	    "gpu": 0,
412	    "checkpoint_source": "/root/turn-residual-gating/runs/d048_ss_s456/epoch_2",
413	    "eval_data": "/root/turn-residual-gating/data/eval_200/eval_200.json",
414	    "checkpoint_path": "/root/turn-residual-gating/results/d048_final_ar/",
415	    "log_path": "/root/turn-residual-gating/results/d048_final_ar/"
416	  },
417	  "conclusion": "success",
418	  "completed_at": "2026-05-24T01:19:43.693Z",
419	  "metrics": {
420	    "tf_gar_ours_mid": 0.4964,
421	    "tf_gar_dongre_mid": 0.3862,
422	    "ar_beta0_gar": 0.4325,
423	    "ar_beta0_ppl": 1.4394,
424	    "ar_beta3_gar": 0.605,
425	    "ar_beta3_ppl": 1.5868,
426	    "ar_beta5_gar": 0.7157,
427	    "ar_beta5_ppl": 1.8045,
428	    "n_convs_ar": 50
429	  }
430	}
431	
432	================================================================================
433	EXPERIMENT: d048_final_ar_eval
434	================================================================================
435	{
436	  "status": "DONE",
437	  "retry_count": 0,
438	  "created_at": "2026-05-23T03:46:23.495Z",
439	  "updated_at": "2026-05-23T03:47:01.285Z",
440	  "hypothesis": "Unified AR N=50 eval across 6 conditions (Base/TG/UG/LO/PCGrad/SS) with bootstrap CI and Wilcoxon tests to establish statistically rigorous comparisons for all claims",
441	  "spec": {
442	    "command": "bash scripts/d048_final_ar_eval.sh",
443	    "server": "westd-20861",
444	    "data_path": "data/eval_200/eval_200.json",
445	    "data_count": 200,
446	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
447	    "seed": 42,
448	    "checkpoint_source": "phase2_tg_s42_v7 / phase2_ug_s42 / phase2_lora_only_s42 / tg_v9_pcgrad_s42 / d048_ss_s42",
449	    "eval_data": "eval_200.json N=50",
450	    "checkpoint_path": "N/A (eval only)",
451	    "log_path": "runs/d048_final_ar_eval.log",
452	    "results_path": "results/d048_final_ar/"
453	  },
454	  "conclusion": "success",
455	  "completed_at": "2026-05-23T03:46:57.110Z",
456	  "metrics": {
457	    "beta0": {
458	      "base_gar": 0.019,
459	      "tg_gar": 0.064,
460	      "ug_gar": 0.033,
461	      "lo_gar": 0.037,
462	      "pcgrad_gar": 0.03,
463	      "ss_gar": 0.347
464	    },
465	    "beta3": {
466	      "base_gar": 0.531,
467	      "tg_gar": 0.556,
468	      "ss_gar": 0.593
469	    },
470	    "beta5": {
471	      "base_gar": 0.704,
472	      "tg_gar": 0.727,
473	      "ss_gar": 0.717
474	    },
475	    "wilcoxon_beta0": {
476	      "tg_vs_base_p": "<0.001",
477	      "tg_vs_base_r": 0.802,
478	      "ss_vs_tg_p": "<0.001",
479	      "ss_vs_tg_r": 0.869
480	    },
481	    "ppl": {
482	      "base": 1.447,
483	      "tg": 1.432,
484	      "ss": 1.442
485	    },
486	    "n_convs": 39
487	  }
488	}
489	
490	================================================================================
491	EXPERIMENT: d048_queue_runner
492	================================================================================
493	{
494	  "status": "PREPARING",
495	  "retry_count": 0,
496	  "created_at": "2026-05-22T23:42:35.919Z",
497	  "updated_at": "2026-05-22T23:42:39.048Z",
498	  "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed",
499	  "conclusion": "failed",
500	  "extra": {
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "627a9441-3ed3-4e5a-9588-2745b62e9689",
  "isSidechain": true,
  "promptId": "1f7ff205-71d0-4ca7-a71f-3ee7850be97d",
  "agentId": "a24bf7311cd045b90",
  "type": "user",
  "uuid": "d9104e62-b739-4b03-8f87-b96cf600b72b",
  "sourceToolAssistantUUID": "627a9441-3ed3-4e5a-9588-2745b62e9689",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T20:13:30.939Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AB3dEjv2HEPWujzarsvQae`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt",
  "offset": 500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9104e62-b739-4b03-8f87-b96cf600b72b",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu4mZcFJ3ufLmRXmFzF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6e8a4c2-cc52-414d-b329-403386aa4223",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VABjns72b4vMRJD5JLQJYa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8624,
      "cache_read_input_tokens": 21135,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8624
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 21135,
          "cache_creation_input_tokens": 8624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8624,
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

_source line 23 · 2026-05-25T20:13:30.953Z_

<details><summary>↩ Tool result · `toolu_01AB3dEjv2HEPWujzarsvQae`</summary>

```text
500	  "extra": {
501	    "hook_events": [
502	      {
503	        "event": "on_failed",
504	        "action": "agent",
505	        "ts": "2026-05-22T23:42:38.157928+00:00"
506	      }
507	    ]
508	  },
509	  "reproduce": {
510	    "finished_at": "2026-05-22T23:42:38.522Z"
511	  }
512	}
513	
514	================================================================================
515	EXPERIMENT: d048_split_softmax_eval
516	================================================================================
517	{
518	  "status": "DONE",
519	  "retry_count": 0,
520	  "created_at": "2026-05-23T07:47:05.556Z",
521	  "updated_at": "2026-05-23T08:00:42.748Z",
522	  "hypothesis": "Split-softmax (Li et al., COLM 2024) post-softmax rescaling recovers AR GAR without the PPL cost of pre-softmax additive steering, providing an alternative inference-time intervention that separates attention allocation from logit distribution.",
523	  "spec": {
524	    "command": "python src/eval_split_softmax.py",
525	    "server": "westd-20861",
526	    "data_path": "data/eval_200/eval_200.json",
527	    "data_count": 50,
528	    "model_name": "Qwen2.5-7B-Instruct + TG v7 LoRA",
529	    "seed": 42,
530	    "checkpoint_path": "N/A (failed)",
531	    "log_path": "results/split_softmax/",
532	    "failure_reason": "Bug 1: system_prompt_len=0 hardcoded (line 373) — split-softmax has no effect. Bug 2: gen mode NaN for k=0.0/0.3/0.5/0.7. Needs code fix before re-run."
533	  },
534	  "conclusion": "failed",
535	  "completed_at": "2026-05-23T07:53:10.326Z",
536	  "notes": "2 critical bugs: (1) system_prompt_len=0 hardcoded at L373, (2) gen mode NaN for k≠1.0. Director decision 2026-05-23: not urgent, defer fix past DDL 5/25. Does not affect main paper experiments."
537	}
538	
539	================================================================================
540	EXPERIMENT: d048_ss_s123
541	================================================================================
542	{
543	  "status": "DONE",
544	  "retry_count": 0,
545	  "created_at": "2026-05-23T07:54:41.928Z",
546	  "updated_at": "2026-05-23T17:29:06.984Z",
547	  "hypothesis": "Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s123) to establish 3-seed mean±std for C2 reviewer requirement. Corrected hyperparams matching d048_ss_s456.",
548	  "parent": "d048_ss_s42",
549	  "spec": {
550	    "command": "python train_phase2_v8b.py --gate-type threadgate --seed 123 --output-dir runs/d048_ss_s123 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --ss-ratio 0.3",
551	    "server": "westd-20861",
552	    "pid": "84793",
553	    "data_path": "/root/turn-residual-gating/data/phase2_train.jsonl",
554	    "data_count": 2000,
555	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
556	    "seed": 123,
557	    "gpu": 0,
558	    "checkpoint_source": "Qwen/Qwen2.5-7B-Instruct (base, no prior checkpoint)",
559	    "eval_data": "N/A - this is a training experiment",
560	    "checkpoint_path": "/root/turn-residual-gating/runs/d048_ss_s123/epoch_2",
561	    "log_path": "/root/turn-residual-gating/runs/d048_ss_s123/train.log"
562	  },
563	  "conclusion": "success",
564	  "completed_at": "2026-05-23T17:29:06.984Z"
565	}
566	
567	================================================================================
568	EXPERIMENT: d048_ss_s42
569	================================================================================
570	{
571	  "status": "DONE",
572	  "retry_count": 0,
573	  "created_at": "2026-05-22T09:14:13.365Z",
574	  "updated_at": "2026-05-22T23:11:26.493Z",
575	  "hypothesis": "Scheduled sampling (ratio=0.3) with ThreadGate reduces the ~30× TF-AR GAR gap by exposing the model to its own generated text during training. Multi-seed run (s42) under D048 unified protocol to establish mean±std for statistical testing. SS is the strongest mitigation candidate (prior single-seed showed gap 31×→1.57×).",
576	  "spec": {
577	    "command": "bash -c \"cd /root/turn_residual_gating && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --batch-size 1 --grad-accum 8 --max-seq-len 2048 --scheduled-sampling --ss-max-ratio 0.3 --seed 42 --epochs 3 --output-dir runs/d048_ss_s42 --data-dir data/ultrachat_8k --resume runs/d048_ss_s42/epoch_0 2>&1 | tee ~/runs/turn_residual_gating/d048_ss_s42_resume.log\"",
578	    "server": "westd-20861",
579	    "gpu": [
580	      "cuda:0"
581	    ],
582	    "pid": "32861",
583	    "log_path": "~/runs/turn_residual_gating/d048_ss_s42.log",
584	    "submitted_at": "2026-05-22T15:59:07.519Z",
585	    "submitted_via": "submit_training_job",
586	    "backend": "tmux",
587	    "account": "root"
588	  },
589	  "reproduce": {
590	    "finished_at": "2026-05-22T15:51:53.120Z"
591	  },
592	  "failure_reason": "CUDA OOM: CUDA out of memory. Tried to allocate 424.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 218.56 MiB is free. Including non-PyTorch memory, this process has 26.13 GiB memory in use. Process 30899 has 68.62 GiB memory in use. Of the allocated",
593	  "conclusion": "success",
594	  "completed_at": "2026-05-22T15:51:54.391Z",
595	  "extra": {
596	    "hook_events": [
597	      {
598	        "event": "on_failed",
599	        "action": "agent",
600	        "ts": "2026-05-22T15:51:56.369724+00:00"
601	      }
602	    ]
603	  },
604	  "notes": "Training complete (resume v3). 23418s (6.5h) for epoch 1+2. Final: Avg Loss=0.9326, NTP=0.9320, GAR=0.0007, DIV=0.0000. Gate: mean=0.9527, std=0.0589, min=0.7383(L4), max=1.000. SS: 4750/16000 (29.7%) used, 0 fallback. Checkpoints: epoch_0, epoch_1, epoch_2, final. Gate profile consistent with prior SS runs (L4 lowest).",
605	  "metrics": {
606	    "final_avg_loss": 0.9326,
607	    "final_ntp_loss": 0.932,
608	    "final_gar_loss": 0.0007,
609	    "gate_mean": 0.9527,
610	    "gate_std": 0.0589,
611	    "gate_min": 0.7383,
612	    "gate_min_layer": "L4",
613	    "gate_max": 1,
614	    "ss_usage": "4750/16000 (29.7%)",
615	    "ss_fallback": 0,
616	    "epochs_completed": 3,
617	    "wall_clock_s": 23418,
618	    "wall_clock_h": 6.5
619	  }
620	}
621	
622	================================================================================
623	EXPERIMENT: d048_ss_s42_resume
624	================================================================================
625	{
626	  "status": "PREPARING",
627	  "retry_count": 0,
628	  "created_at": "2026-05-22T15:57:05.941Z",
629	  "updated_at": "2026-05-22T15:57:05.941Z",
630	  "spec": {
631	    "command": "bash -c \"cd /root/turn_residual_gating && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --batch-size 1 --grad-accum 8 --max-seq-len 2048 --scheduled-sampling --ss-max-ratio 0.3 --seed 42 --epochs 3 --output-dir runs/d048_ss_s42 --data-dir data/ultrachat_8k --resume runs/d048_ss_s42/epoch_0\"",
632	    "server": "westd-20861",
633	    "gpu": [
634	      "cuda:0"
635	    ],
636	    "pid": "32472",
637	    "log_path": "~/runs/turn_residual_gating/d048_ss_s42_resume.log",
638	    "submitted_at": "2026-05-22T15:57:05.791Z",
639	    "submitted_via": "submit_training_job",
640	    "backend": "tmux",
641	    "account": "root"
642	  }
643	}
644	
645	================================================================================
646	EXPERIMENT: d048_ss_s456
647	================================================================================
648	{
649	  "status": "DONE",
650	  "retry_count": 0,
651	  "created_at": "2026-05-23T03:46:14.558Z",
652	  "updated_at": "2026-05-24T00:38:35.393Z",
653	  "hypothesis": "Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s456) to establish 3-seed mean±std for C2 reviewer requirement of at least 3 seeds",
654	  "parent": "d048_ss_s42",
655	  "spec": {
656	    "command": "python train_phase2_v8b.py --seed 456 --resume runs/d048_ss_s456/epoch_0 --gate-type threadgate --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --ss-ratio 0.3",
657	    "server": "westd-20861",
658	    "pid": "112418",
659	    "data_path": "/root/turn-residual-gating/data/phase2_train.jsonl",
660	    "data_count": 2000,
661	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
662	    "seed": 456,
663	    "gpu": 0,
664	    "checkpoint_source": "Qwen/Qwen2.5-7B-Instruct (resume from epoch_0)",
665	    "eval_data": "N/A - training experiment",
666	    "checkpoint_path": "/root/turn-residual-gating/runs/d048_ss_s456/epoch_2",
667	    "log_path": "/root/turn-residual-gating/runs/d048_ss_s456/train.log"
668	  },
669	  "conclusion": "success",
670	  "completed_at": "2026-05-24T00:38:35.393Z"
671	}
672	
673	================================================================================
674	EXPERIMENT: eval_llama_ar_n20
675	================================================================================
676	{
677	  "status": "DONE",
678	  "retry_count": 0,
679	  "created_at": "2026-05-22T07:52:04.543Z",
680	  "updated_at": "2026-05-22T08:38:33.680Z",
681	  "hypothesis": "N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) autoregressive GAR estimates. N=5 suffered from outlier influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides robust mean±std.",
682	  "parent": "eval_llama_lora_only_s42",
683	  "spec": {
684	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_ar_n20.sh\"",
685	    "server": "westd-20861",
686	    "gpu": [
687	      "cuda:0"
688	    ],
689	    "pid": "312592",
690	    "log_path": "~/runs/turn_residual_gating/eval_llama_ar_n20.log",
691	    "submitted_at": "2026-05-22T07:52:13.830Z",
692	    "submitted_via": "submit_training_job",
693	    "backend": "tmux",
694	    "account": "root",
695	    "data_path": "ultrachat_200k + model-gen AR",
696	    "data_count": 20,
697	    "model_name": "Llama-3.1-8B-Instruct (Base/TG/LoRA-only)",
698	    "seed": 42,
699	    "checkpoint_source": "llama_tg_s42 + llama_lora_only_s42",
700	    "eval_data": "AR-generated 20 conversations x 4 turns",
701	    "wall_clock_seconds": 1435.6,
702	    "gpu_hours": 0.4
703	  },
704	  "reproduce": {
705	    "finished_at": "2026-05-22T08:09:48.181Z"
706	  },
707	  "extra": {
708	    "hook_events": [
709	      {
710	        "event": "on_complete",
711	        "action": "agent",
712	        "ts": "2026-05-22T08:09:50.100538+00:00"
713	      }
714	    ]
715	  },
716	  "checkpoint_path": "N/A",
717	  "log_path": "/root/runs/turn_residual_gating/eval_llama_ar_n20.log",
718	  "metrics": {
719	    "base": {
720	      "gar_ours_mean": 0.0088,
721	      "gar_ours_std": 0.0056,
722	      "gar_ours_median_per_conv": 0.0093,
723	      "gar_ours_median_per_turn_pool": 0.0071,
724	      "gar_ours_spike_ratio": "0%",
725	      "gar_dongre_mean": 0.0049,
726	      "gar_dongre_std": 0.0013,
727	      "gar_dongre_median": 0.0047,
728	      "ngar_ours_mid": 0.1019,
729	      "ngar_dongre_mid": 0.1171,
730	      "ppl": 1.293,
731	      "ppl_std": 0.07,
732	      "ntp_loss": 0.2552
733	    },
734	    "tg": {
735	      "gar_ours_mean": 0.0434,
736	      "gar_ours_std": 0.1002,
737	      "gar_ours_median_per_conv": 0.0179,
738	      "gar_ours_median_per_turn_pool": 0.0126,
739	      "gar_ours_spike_ratio": "5% (2/40 turns GAR>=0.4)",
740	      "gar_dongre_mean": 0.0183,
741	      "gar_dongre_std": 0.0198,
742	      "gar_dongre_median": 0.0152,
743	      "ngar_ours_mid": 0.5357,
744	      "ngar_dongre_mid": 0.4436,
745	      "ppl": 1.437,
746	      "ppl_std": 0.077,
747	      "ntp_loss": 0.3612
748	    },
749	    "lora_only": {
750	      "gar_ours_mean": 0.0284,
751	      "gar_ours_std": 0.0481,
752	      "gar_ours_median_per_conv": 0.0184,
753	      "gar_ours_median_per_turn_pool": 0.0133,
754	      "gar_ours_spike_ratio": "0%",
755	      "gar_dongre_mean": 0.0205,
756	      "gar_dongre_std": 0.0241,
757	      "gar_dongre_median": 0.016,
758	      "ngar_ours_mid": 0.3488,
759	      "ngar_dongre_mid": 0.4997,
760	      "ppl": 1.419,
761	      "ppl_std": 0.075,
762	      "ntp_loss": 0.3483
763	    },
764	    "n_conversations": 20,
765	    "n_turns": 4,
766	    "mid_turns_definition": "turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2). All 16 eval entries use same definition.",
767	    "stat_pool": "median_per_conv: median of 20 per-conversation mid-turn averages. median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).",
768	    "ranking_gar_ours_mean": "TG(0.0434) > LO(0.0284) > Base(0.0088)",
769	    "ranking_gar_ours_median_per_conv": "TG(0.0179) ≈ LO(0.0184) > Base(0.0093)",
770	    "ranking_gar_ours_median_per_turn_pool": "TG(0.0126) ≈ LO(0.0133) > Base(0.0071)",
771	    "ranking_gar_dongre": "LO(0.0205) > TG(0.0183) > Base(0.0049)",
772	    "note": "Paper §5.5 cites median_per_conv (median of per-conversation mid-turn averages across N=20). median_per_turn_pool is the alternative statistic from pooled individual turns. Both confirm TG ≈ LO (zero-increment)."
773	  },
774	  "notes": "N=20 AR eval stabilizes estimates. **mid_turns = turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2; all 16 eval entries use same definition)**. Two median levels: median_per_conv (paper §5.5 cites this: TG 0.0179, LO 0.0184, Base 0.0093) = median of 20 per-conversation mid-turn averages; median_per_turn_pool (TG 0.0126, LO 0.0133, Base 0.0071) = median of 40 pooled individual turns. Both confirm TG ≈ LO (zero-increment). Mean (TG 0.0434 > LO 0.0284) driven by outlier spikes (TG std=0.1002, 5% turns GAR≥0.4; LO std=0.0481, 0% spikes). PPL: Base(1.29) < LO(1.42) < TG(1.44). Pending paper fix: §5.5 says \"turns 2-T\" but code excludes turns 1-2; will correct to \"excluding the first two turns\" in next paper edit batch.",
775	  "conclusion": "success",
776	  "completed_at": "2026-05-22T08:16:09.384Z"
777	}
778	
779	================================================================================
780	EXPERIMENT: eval_llama_lora_only_s42
781	================================================================================
782	{
783	  "status": "DONE",
784	  "retry_count": 0,
785	  "created_at": "2026-05-22T07:40:25.352Z",
786	  "updated_at": "2026-05-22T07:51:32.758Z",
787	  "hypothesis": "LoRA-only ablation (no gate) on Llama-3.1-8B: if TG's GAR improvement comes from the gate, LoRA-only should show minimal GAR recovery vs base.",
788	  "parent": "llama_lora_only_s42",
789	  "spec": {
790	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_lora_only_s42.sh\"",
791	    "server": "westd-20861",
792	    "gpu": [
793	      "cuda:0"
794	    ],
795	    "pid": "309670",
796	    "log_path": "/root/runs/turn_residual_gating/eval_llama_lora_only_s42.log",
797	    "submitted_at": "2026-05-22T07:40:34.437Z",
798	    "submitted_via": "submit_training_job",
799	    "backend": "tmux",
800	    "account": "root",
801	    "data_path": "ultrachat_200k + model-gen",
802	    "data_count": 55,
803	    "model_name": "Llama-3.1-8B-Instruct + LoRA-only checkpoint",
804	    "seed": 42,
805	    "checkpoint_source": "llama_lora_only_s42",
806	    "eval_data": "IID heldout 50 + model-gen 5",
807	    "checkpoint_path": "runs/phase2_llama_lora_only_s42/epoch_2",
808	    "wall_clock_seconds": 650.8,
809	    "gpu_hours": 0.18
810	  },
811	  "reproduce": {
812	    "finished_at": "2026-05-22T07:45:28.637Z"
813	  },
814	  "extra": {
815	    "hook_events": [
816	      {
817	        "event": "on_complete",
818	        "action": "agent",
819	        "ts": "2026-05-22T07:45:30.556207+00:00"
820	      }
821	    ]
822	  },
823	  "metrics": {
824	    "tf": {
825	      "gar_ours": 0.4807,
826	      "gar_dongre": 0.0188,
827	      "ngar_ours": 11.8031,
828	      "ngar_dongre": 0.8261,
829	      "ppl": 2.6,
830	      "ntp_loss": 0.9366,
831	      "n_conversations": 50,
832	      "n_turns": 4
833	    },
834	    "ar": {
835	      "gar_ours": 0.0617,
836	      "gar_dongre": 0.0226,
837	      "ngar_ours": 0.6065,
838	      "ngar_dongre": 0.2537,
839	      "ppl": 1.32,
840	      "ntp_loss": 0.2787,
841	      "n_conversations": 5,
842	      "n_turns": 10
843	    },
844	    "gap_ratio_gar_ours": 7.79
845	  },
846	  "conclusion": "success",
847	  "completed_at": "2026-05-22T07:51:25.244Z"
848	}
849	
850	================================================================================
851	EXPERIMENT: eval_v7_tg_s123
852	================================================================================
853	{
854	  "status": "DONE",
855	  "retry_count": 0,
856	  "created_at": "2026-05-21T22:53:18.163Z",
857	  "updated_at": "2026-05-22T00:30:49.653Z",
858	  "spec": {
859	    "command": "bash scripts/eval_v7_tg_s123.sh",
860	    "server": "westd-20861",
861	    "gpu": [
862	      "cuda:0"
863	    ],
864	    "pid": "264869",
865	    "log_path": "/root/turn_residual_gating/logs/v7_tg_s123.log",
866	    "submitted_at": "2026-05-21T22:53:18.065Z",
867	    "submitted_via": "submit_training_job",
868	    "backend": "tmux",
869	    "account": "root",
870	    "data_path": "data/ultrachat_8k",
871	    "data_count": 8000,
872	    "model_name": "Qwen2.5-7B-Instruct",
873	    "seed": 123,
874	    "checkpoint_source": "v7_tg_s123",
875	    "eval_data": "data/ultrachat_8k",
876	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s123_v7/epoch_2",
877	    "wall_clock_seconds": 5844.5,
878	    "gpu_hours": 1.62
879	  },
880	  "hypothesis": "v7 TG s123 eval: 验证 s123 seed 的 TF-AR GAR gap 与 s42 一致（~32×），确认 multi-seed robustness",
881	  "parent": "v7_tg_s123",
882	  "conclusion": "success",
883	  "completed_at": "2026-05-22T00:30:42.606Z",
884	  "metrics": {
885	    "iid_tf": {
886	      "gar_ours_mid": 0.5052,
887	      "gar_dongre_mid": 0.0119,
888	      "ppl": 2.7802,
889	      "ntp": 0.9752
890	    },
891	    "modelgen_ar": {
892	      "gar_ours_mid": 0.0165,
893	      "gar_dongre_mid": 0.0177,
894	      "ppl": 1.3855,
895	      "ntp": 0.3223
896	    },
897	    "gap_ratio": 30.6,
898	    "comparison_s42": {
899	      "tf_gar_ours_delta": 0.0017,
900	      "ar_gar_ours_delta": 0.0008,
901	      "gap_ratio_delta": -1.4
902	    }
903	  }
904	}
905	
906	================================================================================
907	EXPERIMENT: eval_v8b_ss
908	================================================================================
909	{
910	  "status": "DONE",
911	  "retry_count": 0,
912	  "created_at": "2026-05-20T18:44:23.366Z",
913	  "updated_at": "2026-05-20T18:45:14.523Z",
914	  "hypothesis": "Scheduled Sampling (linear 0→0.5 mixing of teacher-forced and model-gen contexts) closes the 30x training-inference GAR gap by reducing exposure bias, resulting in model-gen GAR significantly above v7 baseline (0.016) while preserving IID GAR and PPL.",
915	  "parent": "phase2_tg_s42_v8b_ss",
916	  "spec": {
917	    "command": "python src/eval_phase2_gar.py --checkpoint-dir checkpoints/tg_v8b_ss_fixed_s42 --gate-type threadgate",
918	    "server": "westd-20861",
919	    "data_path": "data/ultrachat_eval_heldout.json + built-in 5conv model-gen",
920	    "data_count": "50 heldout + 5 model-gen",
921	    "model_name": "Qwen2.5-7B-Instruct",
922	    "seed": 42,
923	    "checkpoint_source": "checkpoints/tg_v8b_ss_fixed_s42",
924	    "eval_data": "ultrachat_eval_heldout.json (IID) + built-in model-gen (5x10 turns)",
925	    "checkpoint_path": "checkpoints/tg_v8b_ss_fixed_s42",
926	    "log_path": "/tmp/eval_v8b_all.log"
927	  },
928	  "metrics": {
929	    "iid_gar_ours": 0.4983,
930	    "iid_gar_dongre": 0.3855,
931	    "iid_ppl": 2.78,
932	    "iid_ngar_ours": 13.5,
933	    "iid_ngar_dongre": 22.68,
934	    "modelgen_gar_ours": 0.3177,
935	    "modelgen_gar_dongre": 0.3533,
936	    "modelgen_ppl": 1.38,
937	    "modelgen_ngar_ours": 4.47,
938	    "modelgen_ngar_dongre": 5.92,
939	    "iid_turn1_gar_ours": 0.5398,
940	    "modelgen_turn1_gar_ours": 0.4333
941	  },
942	  "conclusion": "success",
943	  "completed_at": "2026-05-20T18:45:14.523Z"
944	}
945	
946	================================================================================
947	EXPERIMENT: eval_v8b_ss_s123
948	================================================================================
949	{
950	  "status": "DONE",
951	  "retry_count": 0,
952	  "created_at": "2026-05-21T21:15:52.880Z",
953	  "updated_at": "2026-05-21T22:53:15.356Z",
954	  "spec": {
955	    "command": "bash scripts/eval_v8b_ss_s123.sh",
956	    "server": "westd-20861",
957	    "gpu": [
958	      "cuda:0"
959	    ],
960	    "pid": 259767,
961	    "log_path": "runs/eval_v8b_ss_s123/",
962	    "submitted_at": "2026-05-21T21:15:52.785Z",
963	    "submitted_via": "submit_training_job",
964	    "backend": "tmux",
965	    "account": "root",
966	    "data_path": "data/ultrachat_eval_heldout.json",
967	    "data_count": 50,
968	    "model_name": "Qwen2.5-7B-Instruct",
969	    "seed": 123,
970	    "gpu_index": 0,
971	    "checkpoint_source": "checkpoints/tg_v8b_ss_s123/epoch_2",
972	    "eval_data": "ultrachat_eval_heldout + model-gen",
973	    "checkpoint_path": "checkpoints/tg_v8b_ss_s123/epoch_2",
974	    "wall_clock_seconds": 5835.7,
975	    "gpu_hours": 1.62
976	  },
977	  "hypothesis": "v8b SS model trained with s123 seed should reproduce s42 GAR metrics within acceptable gap_ratio [1.2x-2.5x] and no PPL degradation, confirming seed robustness of the scheduled sampling approach",
978	  "parent": "v7_tg_s123",
979	  "log_path": "~/runs/turn_residual_gating/eval_v8b_ss_s123.log",
980	  "conclusion": "success",
981	  "completed_at": "2026-05-21T22:53:08.443Z",
982	  "metrics": {
983	    "iid": {
984	      "gar_ours": 0.503,
985	      "gar_dongre": 0.394,
986	      "ppl": 2.781,
987	      "ntp_loss": 0.976,
988	      "n_conv": 50,
989	      "n_turns": 3
990	    },
991	    "modelgen": {
992	      "gar_ours": 0.418,
993	      "gar_dongre": 0.441,
994	      "ppl": 1.389,
995	      "ntp_loss": 0.325,
996	      "n_conv": 5,
997	      "n_turns": 10
998	    },
999	    "gap_ratio": 1.2,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6e8a4c2-cc52-414d-b329-403386aa4223",
  "isSidechain": true,
  "promptId": "1f7ff205-71d0-4ca7-a71f-3ee7850be97d",
  "agentId": "a24bf7311cd045b90",
  "type": "user",
  "uuid": "be8505be-3071-4794-89a0-76a860e57fd7",
  "sourceToolAssistantUUID": "f6e8a4c2-cc52-414d-b329-403386aa4223",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-25T20:13:37.166Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q4FeLTs61BJgfGf3gwRPsZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt",
  "offset": 1000,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be8505be-3071-4794-89a0-76a860e57fd7",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu5DrABW8AfC2LjG5W6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06b0f814-eee2-4911-aa03-dcdc24e8a067",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014srMJMT8Vos6Pr4dyAnCp5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9564,
      "cache_read_input_tokens": 29759,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9564
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 29759,
          "cache_creation_input_tokens": 9564,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9564,
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

_source line 25 · 2026-05-25T20:13:37.173Z_

<details><summary>↩ Tool result · `toolu_01Q4FeLTs61BJgfGf3gwRPsZ`</summary>

```text
1000	    "base_iid_ppl": 4.338,
1001	    "base_modelgen_ppl": 1.351
1002	  }
1003	}
1004	
1005	================================================================================
1006	EXPERIMENT: instruction_retention_test
1007	================================================================================
1008	{
1009	  "status": "DONE",
1010	  "retry_count": 0,
1011	  "created_at": "2026-05-21T03:49:26.068Z",
1012	  "updated_at": "2026-05-21T03:59:31.835Z",
1013	  "hypothesis": "Turn-level residual gating (β=3) preserves instruction-following ability across multi-turn conversations better than the baseline (β=0), because gating modulates residual contributions to retain earlier context signals rather than letting them decay through successive transformer layers.",
1014	  "spec": {
1015	    "command": "python src/eval_instruction_retention.py --checkpoint runs/phase2_tg_s42_v7 --prompts data/instruction_retention_prompts.json --betas 0 3 --seed 42 --output results/instruction_retention.json",
1016	    "server": "westd-20861",
1017	    "data_path": "data/instruction_retention_prompts.json",
1018	    "data_count": 18,
1019	    "model_name": "Qwen2.5-7B-Instruct + v7 TG LoRA",
1020	    "seed": 42,
1021	    "checkpoint_source": "phase2_tg_s42_v7",
1022	    "eval_data": "18 instruction retention prompts, beta=[0,3], 5 turns each"
1023	  },
1024	  "conclusion": "success",
1025	  "checkpoint_path": "N/A (eval)",
1026	  "log_path": "/root/turn_residual_gating/results/instruction_retention.log",
1027	  "metrics": {
1028	    "late_turn_rate_beta0": 0.759,
1029	    "late_turn_rate_beta3": 0.87,
1030	    "late_turn_delta": 0.111,
1031	    "mcnemar_chi2": 3.125,
1032	    "mcnemar_p": 0.0771,
1033	    "gar_compliance_r": 0.2003,
1034	    "gar_compliance_p": 0.007,
1035	    "category_content_constraint": {
1036	      "beta0": 0.619,
1037	      "beta3": 0.857,
1038	      "delta": 0.238
1039	    },
1040	    "category_count_constraint": {
1041	      "beta0": 1,
1042	      "beta3": 1,
1043	      "delta": 0
1044	    },
1045	    "category_format_constraint": {
1046	      "beta0": 1,
1047	      "beta3": 1,
1048	      "delta": 0
1049	    },
1050	    "category_position_constraint": {
1051	      "beta0": 0.667,
1052	      "beta3": 0.733,
1053	      "delta": 0.067
1054	    }
1055	  },
1056	  "completed_at": "2026-05-21T03:59:31.835Z"
1057	}
1058	
1059	================================================================================
1060	EXPERIMENT: llama_ar_matched_eval
1061	================================================================================
1062	{
1063	  "status": "DONE",
1064	  "retry_count": 0,
1065	  "created_at": "2026-05-21T03:59:40.918Z",
1066	  "updated_at": "2026-05-21T04:36:23.237Z",
1067	  "hypothesis": "用 matched 设置 (N=50/T=4) 重跑 Llama AR eval，消除 TF/AR 设置差异。与 TF 结果对比得到可直接写入论文的 gap ratio，验证 TG 在 AR 模式下仍能提升 GAR。",
1068	  "parent": "llama_eval_s42",
1069	  "spec": {
1070	    "command": "bash scripts/eval_llama_ar_matched.sh",
1071	    "server": "westd-20861",
1072	    "data_path": "data/ultrachat_eval_sample.json",
1073	    "data_count": 50,
1074	    "model_name": "Meta-Llama-3.1-8B-Instruct + TG LoRA",
1075	    "seed": 42,
1076	    "checkpoint_source": "phase2_llama_tg_s42",
1077	    "eval_data": "50 UltraChat convs, T=4, AR generation, 4 conditions (base/TG x ours/Dongre)",
1078	    "checkpoint_path": "N/A (eval)",
1079	    "log_path": "runs/eval_llama_ar_matched.log"
1080	  },
1081	  "log_path": "/root/turn_residual_gating/runs/eval_llama_ar_matched.log",
1082	  "conclusion": "success",
1083	  "metrics": {
1084	    "ar_base_ours": {
1085	      "mid_gar": 0.0082,
1086	      "ngar": 0.1,
1087	      "ppl": 1.267
1088	    },
1089	    "ar_tg_ours": {
1090	      "mid_gar": 0.0388,
1091	      "ngar": 0.493,
1092	      "ppl": 1.413
1093	    },
1094	    "ar_base_dongre": {
1095	      "mid_gar": 0.0051,
1096	      "ngar": 0.12,
1097	      "ppl": 1.267
1098	    },
1099	    "ar_tg_dongre": {
1100	      "mid_gar": 0.018,
1101	      "ngar": 0.431,
1102	      "ppl": 1.413
1103	    },
1104	    "tf_reference": {
1105	      "tf_tg_ours_ngar": 11.88,
1106	      "tf_base_ours_ngar": 0.388,
1107	      "tf_tg_ours_raw": 0.4836,
1108	      "tf_tg_dongre_raw": 0.018
1109	    },
1110	    "matched_gap_analysis": {
1111	      "gar_ours_raw_gap": "12.5x (TF 0.484 / AR 0.039)",
1112	      "gar_ours_ngar_gap": "24.1x (TF 11.88 / AR 0.493)",
1113	      "gar_dongre_raw_gap": "1.002x (TF 0.018 / AR 0.018) — zero gap",
1114	      "tg_over_base_ar_ours": "4.71x",
1115	      "tg_over_base_ar_dongre": "3.54x",
1116	      "conclusion": "GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure bias selectively destroys learned goal-attention routing while leaving content-overlap-based attention unaffected."
1117	    }
1118	  },
1119	  "completed_at": "2026-05-21T04:28:38.504Z",
1120	  "notes": "CORRECTION (2026-05-21 04:36): Agent 之前错误地将 AR TG nGAR (0.493) 与 TF TG raw GAR (0.484) 对比，误判为 'nGAR aligns, gap is normalization artifact'。Reviewer 核实：TF TG ours nGAR = 11.88（非 0.48）。nGAR gap = 11.88 / 0.493 = 24.1×，比 raw gap (12.5×) 还大。'Normalization artifact' 分析完全错误——GAR-ours 的 gap 是真实的 exposure bias。论文绝对不能使用 normalization artifact 叙事。"
1121	}
1122	
1123	================================================================================
1124	EXPERIMENT: llama_eval_s42
1125	================================================================================
1126	{
1127	  "status": "DONE",
1128	  "retry_count": 0,
1129	  "created_at": "2026-05-21T03:29:51.255Z",
1130	  "updated_at": "2026-05-21T03:46:58.167Z",
1131	  "hypothesis": "Llama-3.1-8B TG eval: 如果 Llama TG 模型在 TF 模式下 GAR-ours 显著高于 AR 模式（如 Qwen v7 的 20-33x gap），则确认 training-inference GAR gap 跨模型泛化（C5）。同时测量 base model 作为 control。",
1132	  "parent": "llama_tg_s42",
1133	  "spec": {
1134	    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_tg_s42.sh 2>&1 | tee runs/eval_llama_tg_s42.log",
1135	    "server": "westd-20861",
1136	    "data_path": "data/ultrachat_eval_sample.json",
1137	    "data_count": 50,
1138	    "model_name": "Llama-3.1-8B-Instruct",
1139	    "seed": 42,
1140	    "checkpoint_source": "runs/phase2_llama_tg_s42/epoch_2",
1141	    "eval_data": "ultrachat_eval_sample"
1142	  },
1143	  "checkpoint_path": "runs/phase2_llama_tg_s42/epoch_2",
1144	  "log_path": "runs/eval_llama_tg_s42.log",
1145	  "metrics": {
1146	    "tf_base": {
1147	      "gar_ours": 0.0166,
1148	      "ngar_ours": 0.3882,
1149	      "gar_dongre": 0.0038,
1150	      "ngar_dongre": 0.163,
1151	      "ppl": 3.45,
1152	      "N": 50,
1153	      "T": 4
1154	    },
1155	    "tf_tg": {
1156	      "gar_ours": 0.4836,
1157	      "ngar_ours": 11.8818,
1158	      "gar_dongre": 0.018,
1159	      "ngar_dongre": 0.7922,
1160	      "ppl": 2.57,
1161	      "N": 50,
1162	      "T": 4
1163	    },
1164	    "ar_base": {
1165	      "gar_ours": 0.0086,
1166	      "ngar_ours": 0.0798,
1167	      "gar_dongre": 0.0118,
1168	      "ngar_dongre": 0.1265,
1169	      "ppl": 1.24,
1170	      "N": 5,
1171	      "T": 10
1172	    },
1173	    "ar_tg": {
1174	      "gar_ours": 0.0304,
1175	      "ngar_ours": 0.2632,
1176	      "gar_dongre": 0.0217,
1177	      "ngar_dongre": 0.2459,
1178	      "ppl": 1.32,
1179	      "N": 5,
1180	      "T": 10
1181	    },
1182	    "gap_ratio_tg_ours": 15.9,
1183	    "gap_ratio_base_ours": 1.93,
1184	    "gap_ratio_tg_dongre": 0.83,
1185	    "vs_qwen_v7_gap_ratio": 32.1,
1186	    "baseline_mid_gar": 0.0122
1187	  },
1188	  "conclusion": "success",
1189	  "notes": "C5 跨模型泛化确认。Llama TG GAR-ours gap 16x (TF 0.484 vs AR 0.030)，低于 Qwen v7 的 32x 但仍非常显著。Base model gap 仅 1.9x（control 通过）。注意 TF/AR eval 设定不同 (N=50/T=4 vs N=5/T=10)，可能影响绝对值对比。GAR-dongre 无明显 gap (ratio 0.83x, AR ≥ TF)，仅 GAR-ours 展现 exposure bias 效应。Gate dynamic range: L24/L28/L30 diff 最大 (0.23-0.38)，与 Qwen 类似集中在中高层。",
1190	  "completed_at": "2026-05-21T03:46:58.167Z"
1191	}
1192	
1193	================================================================================
1194	EXPERIMENT: llama_lora_only_s42
1195	================================================================================
1196	{
1197	  "status": "DONE",
1198	  "retry_count": 0,
1199	  "created_at": "2026-05-22T00:33:03.465Z",
1200	  "updated_at": "2026-05-22T07:39:06.888Z",
1201	  "hypothesis": "Llama-3.1-8B LoRA-only baseline (gate=none, 无 gating 机制): 与 Llama TG s42 对比，验证 gating 对 Llama 的增量贡献。如果 LoRA-only GAR ≈ TG GAR → gating 零增量与 Qwen 结论一致（C5 跨模型）。",
1202	  "parent": "llama_tg_s42",
1203	  "spec": {
1204	    "command": "bash scripts/launch_llama_lora_only_s42.sh",
1205	    "server": "westd-20861",
1206	    "gpu": [
1207	      "cuda:0"
1208	    ],
1209	    "pid": "271741",
1210	    "log_path": "logs/llama_lora_only_s42.log",
1211	    "submitted_at": "2026-05-22T00:33:16.591Z",
1212	    "submitted_via": "submit_training_job",
1213	    "backend": "tmux",
1214	    "account": "root",
1215	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
1216	    "data_count": 8000,
1217	    "model_name": "Meta-Llama-3.1-8B-Instruct",
1218	    "seed": 42,
1219	    "checkpoint_source": "N/A (training from scratch, ablation baseline)",
1220	    "eval_data": "N/A (training run, not eval)",
1221	    "checkpoint_path": "runs/phase2_llama_lora_only_s42/epoch_2",
1222	    "wall_clock_seconds": 25550.3,
1223	    "gpu_hours": 7.1
1224	  },
1225	  "reproduce": {
1226	    "finished_at": "2026-05-22T07:35:56.232Z"
1227	  },
1228	  "extra": {
1229	    "hook_events": [
1230	      {
1231	        "event": "on_complete",
1232	        "action": "agent",
1233	        "ts": "2026-05-22T07:35:58.740298+00:00"
1234	      }
1235	    ]
1236	  },
1237	  "conclusion": "success",
1238	  "metrics": {
1239	    "final_avg_loss": 0.9288,
1240	    "final_avg_ntp": 0.9279,
1241	    "final_avg_gar": 0.0009,
1242	    "gate_fixed": 1,
1243	    "gate_type": "none",
1244	    "wall_clock_s": 25317,
1245	    "wall_clock_h": 7.03,
1246	    "epochs_completed": 3
1247	  },
1248	  "completed_at": "2026-05-22T07:39:06.889Z"
1249	}
1250	
1251	================================================================================
1252	EXPERIMENT: llama_phase1_gar_diag
1253	================================================================================
1254	{
1255	  "status": "DONE",
1256	  "retry_count": 0,
1257	  "created_at": "2026-05-20T19:39:25.751Z",
1258	  "updated_at": "2026-05-21T01:34:36.417Z",
1259	  "hypothesis": "Llama-3.1-8B-Instruct 在 multi-turn dialogue 中也应出现 goal attention decay（与 Qwen-2.5-7B 类似），确认 attention decay 是 transformer 架构通用现象而非模型特有。Phase 1 诊断：测量 base Llama 的 per-turn GAR profile。",
1260	  "spec": {
1261	    "server": "westd-20861",
1262	    "gpu": [
1263	      "cuda:0"
1264	    ],
1265	    "account": "local",
1266	    "command": "CUDA_VISIBLE_DEVICES=0 python src/run_phase1_gar_llama.py --model /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/ --output-dir /root/turn_residual_gating/runs/phase1_llama_gar_diag --max-new-tokens 256",
1267	    "pid": "198817",
1268	    "data_path": "built-in 5 conversations (knowledge_qa, coding_help, creative_writing, math_reasoning, debate)",
1269	    "data_count": 5,
1270	    "model_name": "Meta-Llama-3.1-8B-Instruct",
1271	    "seed": 42,
1272	    "checkpoint_source": "N/A (base model, no fine-tuning)",
1273	    "eval_data": "5 built-in conversations x 10 turns each, gen mode",
1274	    "checkpoint_path": "N/A",
1275	    "log_path": "/root/turn_residual_gating/logs/llama_phase1_gar_diag.log"
1276	  },
1277	  "conclusion": "success",
1278	  "metrics": {
1279	    "per_turn_gar": {
1280	      "turn_1": 0.0263,
1281	      "turn_2": 0.0183,
1282	      "turn_3": 0.0087,
1283	      "turn_4": 0.0055,
1284	      "turn_5": 0.006,
1285	      "turn_6": 0.0035,
1286	      "turn_7": 0.0038,
1287	      "turn_8": 0.0037,
1288	      "turn_9": 0.005,
1289	      "turn_10": 0.0026
1290	    },
1291	    "t1_t10_decay_pct": 90.1,
1292	    "t1_mid38_drop_pct": 80.2,
1293	    "n_topics": 5,
1294	    "model": "Meta-Llama-3.1-8B-Instruct",
1295	    "mode": "gen",
1296	    "n_conversations": 5,
1297	    "n_turns": 10
1298	  },
1299	  "completed_at": "2026-05-21T01:34:36.417Z"
1300	}
1301	
1302	================================================================================
1303	EXPERIMENT: llama_tg_s42
1304	================================================================================
1305	{
1306	  "status": "DONE",
1307	  "retry_count": 0,
1308	  "created_at": "2026-05-21T01:34:36.906Z",
1309	  "updated_at": "2026-05-21T03:28:07.022Z",
1310	  "hypothesis": "在 Llama-3.1-8B-Instruct 上训练 ThreadGate（与 Qwen v7 相同配置），验证 C5：gating mechanism 和 GAR training-inference gap 跨模型泛化。如果 Llama TG 也出现 IID GAR ≈ target 但 model-gen GAR 坍塌 → 确认 exposure bias 的跨模型通用性。",
1311	  "parent": "llama_phase1_gar_diag",
1312	  "spec": {
1313	    "command": "CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 python src/train_phase2.py --model /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct --data-dir data/ultrachat_8k --output-dir runs/phase2_llama_tg_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42",
1314	    "server": "westd-20861",
1315	    "gpu": [
1316	      "cuda:0"
1317	    ],
1318	    "pid": "199643",
1319	    "data_path": "data/ultrachat_8k",
1320	    "data_count": 8000,
1321	    "model_name": "Meta-Llama-3.1-8B-Instruct",
1322	    "seed": 42,
1323	    "checkpoint_source": "N/A (training from scratch)",
1324	    "eval_data": "N/A (training experiment)",
1325	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_llama_tg_s42",
1326	    "log_path": "/root/turn_residual_gating/logs/llama_tg_training.log"
1327	  },
1328	  "conclusion": "success",
1329	  "completed_at": "2026-05-21T03:27:55.963Z",
1330	  "metrics": {
1331	    "epochs_completed": 3,
1332	    "total_steps": 3000,
1333	    "wall_clock_seconds": 26212,
1334	    "wall_clock_hours": 7.28,
1335	    "final_avg_loss": 0.9233,
1336	    "final_avg_ntp": 0.9224,
1337	    "final_avg_gar": 0.0009,
1338	    "final_avg_div": 0,
1339	    "final_gate_mean": 0.9099,
1340	    "final_gate_std": 0.0701,
1341	    "final_gate_min": 0.7188,
1342	    "final_gate_max": 0.9922,
1343	    "gate_profile_step3000": {
1344	      "L0": 0.957,
1345	      "L1": 0.973,
1346	      "L2": 0.977,
1347	      "L3": 0.965,
1348	      "L4": 0.992,
1349	      "L5": 0.969,
1350	      "L6": 0.957,
1351	      "L7": 0.957,
1352	      "L8": 0.961,
1353	      "L9": 0.949,
1354	      "L10": 0.938,
1355	      "L11": 0.934,
1356	      "L12": 0.969,
1357	      "L13": 0.953,
1358	      "L14": 0.957,
1359	      "L15": 0.965,
1360	      "L16": 0.953,
1361	      "L17": 0.961,
1362	      "L18": 0.922,
1363	      "L19": 0.902,
1364	      "L20": 0.883,
1365	      "L21": 0.863,
1366	      "L22": 0.836,
1367	      "L23": 0.844,
1368	      "L24": 0.809,
1369	      "L25": 0.719,
1370	      "L26": 0.762,
1371	      "L27": 0.805,
1372	      "L28": 0.801,
1373	      "L29": 0.855,
1374	      "L30": 0.898,
1375	      "L31": 0.934
1376	    },
1377	    "checkpoint_size_gate_mb": 4.2,
1378	    "checkpoint_size_lora_mb": 26,
1379	    "gpu": "NVIDIA RTX PRO 6000 Blackwell",
1380	    "vram_gb": 102,
1381	    "mem_used_gb": 63.4
1382	  }
1383	}
1384	
1385	================================================================================
1386	EXPERIMENT: llama_tg_training
1387	================================================================================
1388	{
1389	  "status": "PREPARING",
1390	  "retry_count": 0,
1391	  "created_at": "2026-05-21T03:37:31.513Z",
1392	  "updated_at": "2026-05-21T09:44:18.859Z",
1393	  "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed",
1394	  "conclusion": "failed",
1395	  "extra": {
1396	    "hook_events": [
1397	      {
1398	        "event": "on_failed",
1399	        "action": "agent",
1400	        "ts": "2026-05-21T03:37:33.309826+00:00"
1401	      }
1402	    ]
1403	  },
1404	  "notes": "INVALIDATED: Phantom duplicate of llama_tg_s42 (same PID 199643, same experiment). Created by Worker in global registry, duplicated to project registry. Canonical entry is llama_tg_s42 (DONE/success)."
1405	}
1406	
1407	================================================================================
1408	EXPERIMENT: mmlu_eval_all
1409	================================================================================
1410	{
1411	  "status": "DONE",
1412	  "retry_count": 0,
1413	  "created_at": "2026-05-23T06:45:04.153Z",
1414	  "updated_at": "2026-05-24T07:23:08.289Z",
1415	  "hypothesis": "ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.",
1416	  "spec": {
1417	    "command": "python eval_mmlu.py --model_path &lt;checkpoint> --n_shot 5",
1418	    "server": "westd-20861",
1419	    "data_path": "MMLU benchmark (5-shot)",
1420	    "data_count": 14042,
1421	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
1422	    "seed": 42,
1423	    "checkpoint_source": "base/lo/ug/tg/pcgrad/ss checkpoints",
1424	    "eval_data": "MMLU 5-shot",
1425	    "checkpoint_path": "results/mmlu/",
1426	    "log_path": "logs/gpu_chain_next.log"
1427	  },
1428	  "conclusion": "success",
1429	  "metrics": {
1430	    "base_qwen": 0.7423,
1431	    "pcgrad_v9_s42": 0.7386,
1432	    "ss_v8b_s42": 0.7375,
1433	    "lo_s42": 0.7357,
1434	    "tg_v7_s42": 0.7347,
1435	    "ug_s42": 0.7346
1436	  },
1437	  "completed_at": "2026-05-24T06:53:52.873Z"
1438	}
1439	
1440	================================================================================
1441	EXPERIMENT: p0_ss_steering_eval
1442	================================================================================
1443	{
1444	  "status": "PREPARING",
1445	  "retry_count": 0,
1446	  "created_at": "2026-05-23T19:37:39.883Z",
1447	  "updated_at": "2026-05-23T19:57:38.851Z",
1448	  "hypothesis": "SS training provides AR GAR ~0.385, steering alone gives 0.717. Combining SS checkpoint with beta-steering at inference may approach TF parity (~0.50), demonstrating that SS+steering is a constructive mitigation stack for the TF-AR gap.",
1449	  "parent": "d048_eval_ss_s42",
1450	  "conclusion": "killed",
1451	  "notes": "Cancelled: ss_s42_ar_n50.json already contains SS+steering data at β=0,3,5. Results show SS and steering do not stack (β=5: SS 0.717 vs TG-only 0.727). Director decision: skip, use existing data."
1452	}
1453	
1454	================================================================================
1455	EXPERIMENT: p1_llama_ss_eval
1456	================================================================================
1457	{
1458	  "status": "DONE",
1459	  "retry_count": 0,
1460	  "created_at": "2026-05-24T15:53:29.650Z",
1461	  "updated_at": "2026-05-24T17:12:44.175Z",
1462	  "hypothesis": "Llama SS (2-epoch) reduces the TF-AR GAR gap on Llama-3.1-8B, confirming SS as model-general mitigation (C4+C5). Eval: TF+AR N=50 β=0/3/5.",
1463	  "spec": {
1464	    "command": "bash scripts/p1_llama_ss_eval.sh",
1465	    "server": "westd-20861",
1466	    "data_path": "/root/turn-residual-gating/data/eval_50.json",
1467	    "data_count": 50,
1468	    "model_name": "meta-llama/Llama-3.1-8B-Instruct",
1469	    "seed": 42,
1470	    "checkpoint_source": "runs/p1_llama_ss_s42/epoch_1/",
1471	    "log_path": "runs/p1_llama_ss_eval.log",
1472	    "pid": 178624,
1473	    "checkpoint_path": "results/llama_ss_eval/"
1474	  },
1475	  "conclusion": "success",
1476	  "metrics": {
1477	    "ss_tf_gar": 0.477,
1478	    "ss_tf_ppl": 2.82,
1479	    "ss_ar_b0_gar": 0.1662,
1480	    "ss_ar_b0_ppl": 1.37,
1481	    "ss_ar_b5_gar": 0.7905,
1482	    "ss_ar_b5_ppl": 1.81,
1483	    "base_ar_gar": 0.0179,
1484	    "base_ar_ppl": 1.22,
1485	    "tf_ar_gap": 2.87
1486	  },
1487	  "completed_at": "2026-05-24T17:12:44.175Z"
1488	}
1489	
1490	================================================================================
1491	EXPERIMENT: p1_llama_ss_training
1492	================================================================================
1493	{
1494	  "status": "DONE",
1495	  "retry_count": 0,
1496	  "created_at": "2026-05-23T19:37:48.689Z",
1497	  "updated_at": "2026-05-24T15:53:21.654Z",
1498	  "hypothesis": "SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims.",
1499	  "spec": {
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06b0f814-eee2-4911-aa03-dcdc24e8a067",
  "isSidechain": true,
  "promptId": "1f7ff205-71d0-4ca7-a71f-3ee7850be97d",
  "agentId": "a24bf7311cd045b90",
  "type": "user",
  "uuid": "1792948d-c5bd-4879-b4bc-435f309b3e33",
  "sourceToolAssistantUUID": "06b0f814-eee2-4911-aa03-dcdc24e8a067",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-25T20:13:43.905Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KvEkAMwP9JPNpZa2MxrLKL`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt",
  "offset": 1500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1792948d-c5bd-4879-b4bc-435f309b3e33",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu5gdiQkjSUdp5mjsaK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06691c56-d065-4bae-9fb4-76470d88ed67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UeD7dWYL8DNWhgtcdmTFmN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9410,
      "cache_read_input_tokens": 39323,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9410
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 39323,
          "cache_creation_input_tokens": 9410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9410,
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

_source line 27 · 2026-05-25T20:13:43.914Z_

<details><summary>↩ Tool result · `toolu_01KvEkAMwP9JPNpZa2MxrLKL`</summary>

```text
1500	    "command": "bash scripts/p1_llama_ss_train.sh",
1501	    "server": "westd-20861",
1502	    "data_path": "/root/turn-residual-gating/data/train_400.json",
1503	    "data_count": 400,
1504	    "model_name": "meta-llama/Llama-3.1-8B-Instruct",
1505	    "seed": 42,
1506	    "checkpoint_path": "runs/llama_ss_s42/",
1507	    "log_path": "logs/p1_llama_ss_training.log",
1508	    "pid": 158507,
1509	    "hyperparams": {
1510	      "lr": "2e-4",
1511	      "batch_size": 1,
1512	      "grad_accum": 8,
1513	      "epochs": 3,
1514	      "ss_max_ratio": 0.3,
1515	      "lora_rank": 16
1516	    }
1517	  },
1518	  "conclusion": "success",
1519	  "completed_at": "2026-05-24T15:53:21.654Z"
1520	}
1521	
1522	================================================================================
1523	EXPERIMENT: p1_ss_lora_only
1524	================================================================================
1525	{
1526	  "status": "DONE",
1527	  "retry_count": 0,
1528	  "created_at": "2026-05-25T08:58:41.419Z",
1529	  "updated_at": "2026-05-25T09:42:22.185Z",
1530	  "hypothesis": "SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).",
1531	  "spec": {
1532	    "command": "bash /root/turn_residual_gating/scripts/d048_ss_lo_s42.sh",
1533	    "server": "westd-20861",
1534	    "data_path": "/root/turn-residual-gating/data/phase2_train.jsonl",
1535	    "data_count": 2000,
1536	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
1537	    "seed": 42,
1538	    "notes": "SS+LoRA-only (gate_type=none, ss_max_ratio=0.3). From-scratch training, not resume. Auto TF+AR eval after training. ~6.5h training + eval."
1539	  },
1540	  "conclusion": "killed",
1541	  "completed_at": "2026-05-25T09:42:22.185Z"
1542	}
1543	
1544	================================================================================
1545	EXPERIMENT: p1_tf_ar_kl_divergence
1546	================================================================================
1547	{
1548	  "status": "DONE",
1549	  "retry_count": 0,
1550	  "created_at": "2026-05-23T19:37:46.355Z",
1551	  "updated_at": "2026-05-24T07:18:10.268Z",
1552	  "hypothesis": "TF and AR attention distributions diverge more on GAR-relevant heads (high gate values) than non-relevant heads, providing mechanistic evidence that exposure bias selectively disrupts goal-attending computation rather than uniformly degrading attention.",
1553	  "metrics": {
1554	    "tg_delta_gar": 0.0165,
1555	    "base_delta_gar": 0.0122,
1556	    "tg_mean_kl": 0.054,
1557	    "base_mean_kl": 0.043,
1558	    "gate_kl_correlation": 0.11,
1559	    "high_kl_layers": "L23-L27, L9",
1560	    "gar_robustness_ours_tg_base_ratio": 21.4,
1561	    "gar_robustness_goal_only_ratio": 63,
1562	    "gar_robustness_ours_all_ratio": 1.7,
1563	    "gar_robustness_ours_first_ratio": 1.8
1564	  },
1565	  "spec": {
1566	    "command": "python scripts/p1_kl_divergence.py",
1567	    "server": "westd-20861",
1568	    "data_path": "/root/turn_residual_gating/data/eval_200.json",
1569	    "data_count": 30,
1570	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
1571	    "seed": 42,
1572	    "checkpoint_path": "results/p1_kl_perhead/",
1573	    "log_path": "logs/p1_kl_divergence_step2.log"
1574	  },
1575	  "conclusion": "success",
1576	  "completed_at": "2026-05-24T07:18:06.521Z"
1577	}
1578	
1579	================================================================================
1580	EXPERIMENT: p2_llama_gradient_conflict
1581	================================================================================
1582	{
1583	  "status": "DONE",
1584	  "retry_count": 0,
1585	  "created_at": "2026-05-23T19:37:50.492Z",
1586	  "updated_at": "2026-05-24T07:20:28.248Z",
1587	  "hypothesis": "PCGrad fails to improve AR GAR on Llama-3.1-8B (as on Qwen), confirming cross-model that gradient conflict is not the root cause of the TF-AR gap, strengthening C2 (causal exclusion).",
1588	  "spec": {
1589	    "command": "bash scripts/p2_llama_gradient_conflict.sh",
1590	    "server": "westd-20861",
1591	    "data_path": "/root/turn-residual-gating/data/train_400.json",
1592	    "data_count": 400,
1593	    "model_name": "meta-llama/Llama-3.1-8B-Instruct",
1594	    "seed": 42,
1595	    "checkpoint_path": "results/p2_llama_gradient_conflict/",
1596	    "log_path": "logs/p2_llama_gradient_conflict.log"
1597	  },
1598	  "conclusion": "success",
1599	  "metrics": {
1600	    "cos_sim_mean": 0.0045,
1601	    "cos_sim_std": 0.07,
1602	    "neg_cos_sim_layers_pct": 53.1,
1603	    "mag_ratio_median": 25.7,
1604	    "conclusion_note": "cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading — actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern."
1605	  },
1606	  "completed_at": "2026-05-24T07:20:28.248Z"
1607	}
1608	
1609	================================================================================
1610	EXPERIMENT: phase1_gar_diag
1611	================================================================================
1612	{
1613	  "status": "DONE",
1614	  "retry_count": 0,
1615	  "created_at": "2026-05-18T05:24:07.903Z",
1616	  "updated_at": "2026-05-18T05:59:25.324Z",
1617	  "hypothesis": "Qwen2.5-7B-Instruct 在 10-turn 多轮对话中，中间 turns (3-8) 的 GAR (Goal Accessibility Ratio) 相对 turn-1 下降 ≥15%，表明模型对 system prompt 中目标 token 的注意力随对话进行显著衰减",
1618	  "spec": {
1619	    "command": "python run_phase1_gar.py --results-dir /root/turn_residual_gating/results",
1620	    "server": "westd-20861",
1621	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
1622	    "data_path": "built-in 5 conversations (knowledge_qa, coding_help, creative_writing, math_reasoning, roleplay_advisor)",
1623	    "data_count": 5,
1624	    "seed": 0,
1625	    "checkpoint_path": "N/A",
1626	    "log_path": "/root/turn_residual_gating/results/phase1_run.log"
1627	  },
1628	  "conclusion": "success",
1629	  "metrics": {
1630	    "turn1_avg_gar": 0.0418,
1631	    "mid_turns_avg_gar": 0.0122,
1632	    "relative_drop": 0.708,
1633	    "num_conversations": 5,
1634	    "num_turns": 10,
1635	    "per_turn_avg_gar": [
1636	      0.0418,
1637	      0.0241,
1638	      0.0224,
1639	      0.013,
1640	      0.0133,
1641	      0.0086,
1642	      0.0078,
1643	      0.008,
1644	      0.0157,
1645	      0.0064
1646	    ]
1647	  },
1648	  "completed_at": "2026-05-18T05:59:25.325Z"
1649	}
1650	
1651	================================================================================
1652	EXPERIMENT: phase1a_multiseed_8runs
1653	================================================================================
1654	{
1655	  "status": "PREPARING",
1656	  "retry_count": 0,
1657	  "created_at": "2026-05-25T06:18:08.953Z",
1658	  "updated_at": "2026-05-25T06:18:08.953Z",
1659	  "spec": {
1660	    "command": "bash -c \"bash /root/turn_residual_gating/scripts/phase1a_multiseed_runner.sh\"",
1661	    "server": "westd-20861",
1662	    "gpu": [
1663	      "cuda:0"
1664	    ],
1665	    "pid": "5508",
1666	    "log_path": "~/runs/turn_residual_gating/phase1a_multiseed_8runs.log",
1667	    "submitted_at": "2026-05-25T06:18:08.495Z",
1668	    "submitted_via": "submit_training_job",
1669	    "backend": "tmux",
1670	    "account": "root"
1671	  }
1672	}
1673	
1674	================================================================================
1675	EXPERIMENT: phase1a_multiseed_qwen
1676	================================================================================
1677	{
1678	  "status": "DONE",
1679	  "retry_count": 0,
1680	  "created_at": "2026-05-25T06:15:26.051Z",
1681	  "updated_at": "2026-05-25T11:20:34.089Z",
1682	  "hypothesis": "Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.",
1683	  "spec": {
1684	    "command": "python src/train_phase2_v9_pcgrad.py",
1685	    "server": "westd-20861",
1686	    "data_path": "data/ultrachat_8k",
1687	    "data_count": 8000,
1688	    "model_name": "Qwen2.5-7B-Instruct",
1689	    "seed": 123,
1690	    "checkpoint_path": "N/A",
1691	    "log_path": "runs/d048_pcgrad_s123"
1692	  },
1693	  "conclusion": "killed",
1694	  "notes": "用户要求停止：30min 内无法完成。PCGrad s123 在 1800/3000 步时被终止，后续 7 个排队任务全部取消。",
1695	  "checkpoint_path": "N/A",
1696	  "log_path": "runs/d048_pcgrad_s123",
1697	  "completed_at": "2026-05-25T11:20:34.089Z"
1698	}
1699	
1700	================================================================================
1701	EXPERIMENT: phase1b_llama_complement
1702	================================================================================
1703	{
1704	  "status": "PREPARING",
1705	  "retry_count": 0,
1706	  "created_at": "2026-05-25T06:15:34.729Z",
1707	  "updated_at": "2026-05-25T06:15:44.322Z",
1708	  "hypothesis": "Llama PCGrad + UG (s42) to complete cross-model comparison matrix. If Llama PCGrad also fails to improve AR GAR (like Qwen), it strengthens the cross-architecture causal exclusion of gradient conflict."
1709	}
1710	
1711	================================================================================
1712	EXPERIMENT: phase2_4way_eval
1713	================================================================================
1714	{
1715	  "status": "DONE",
1716	  "retry_count": 0,
1717	  "created_at": "2026-05-19T13:07:30.673Z",
1718	  "updated_at": "2026-05-19T13:15:39.947Z",
1719	  "hypothesis": "Turn-residual gating (TRG) improves multi-turn response quality over LoRA-only and base model baselines because it selectively amplifies conversational context signals, which should manifest as higher GAR scores across 4 conditions (base, base+TRG, LoRA, LoRA+TRG).",
1720	  "spec": {
1721	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/run_4way_eval.sh 2>&1 | tee runs/4way_eval.log\"",
1722	    "server": "westd-20861",
1723	    "gpu": [
1724	      "cuda:0"
1725	    ],
1726	    "pid": "60024",
1727	    "log_path": "/root/turn_residual_gating/runs/4way_eval.log",
1728	    "submitted_at": "2026-05-19T13:07:37.380Z",
1729	    "submitted_via": "submit_training_job",
1730	    "backend": "tmux",
1731	    "account": "root",
1732	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
1733	    "data_count": 8000,
1734	    "model_name": "Qwen2.5-7B-Instruct",
1735	    "seed": 42,
1736	    "checkpoint_source": "phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42",
1737	    "eval_data": "ultrachat_8k eval split",
1738	    "checkpoint_path": "/root/turn_residual_gating/runs/4way_eval/",
1739	    "wall_clock_seconds": 447.0,
1740	    "gpu_hours": 0.12
1741	  },
1742	  "parent": "phase2_tg_s42_v7",
1743	  "conclusion": "negative",
1744	  "completed_at": "2026-05-19T13:15:04.405Z",
1745	  "metrics": {
1746	    "base_ours_mid_gar": 0.0107,
1747	    "base_ours_recovery_pp": -0.15,
1748	    "base_dongre_mid_gar": 0.003,
1749	    "base_dongre_recovery_pp": -0.92,
1750	    "base_ppl": 4.23,
1751	    "base_ntp": 1.4162,
1752	    "tg_ours_mid_gar": 0.4866,
1753	    "tg_ours_recovery_pp": 47.44,
1754	    "tg_dongre_mid_gar": 0.0157,
1755	    "tg_dongre_recovery_pp": 0.35,
1756	    "tg_ppl": 2.63,
1757	    "tg_ntp": 0.9484,
1758	    "ug_ours_mid_gar": 0.4923,
1759	    "ug_ours_recovery_pp": 48.01,
1760	    "ug_dongre_mid_gar": 0.013,
1761	    "ug_dongre_recovery_pp": 0.08,
1762	    "ug_ppl": 2.62,
1763	    "ug_ntp": 0.9433,
1764	    "lora_ours_mid_gar": 0.486,
1765	    "lora_ours_recovery_pp": 47.39,
1766	    "lora_dongre_mid_gar": 0.0137,
1767	    "lora_dongre_recovery_pp": 0.15,
1768	    "lora_ppl": 2.63,
1769	    "lora_ntp": 0.9482,
1770	    "route_b_confirmed": true,
1771	    "gating_incremental_benefit": "none"
1772	  },
1773	  "notes": "四路 eval 完成，Route B 决定性确认。三种训练方法（TG/UG/LoRA-only）在推理端完全趋同：ours GAR recovery ~47-48pp（vs base -0.15pp），dongre GAR recovery 0.08-0.35pp，PPL 2.62-2.63，NTP 0.943-0.948。Gating 机制（无论 turn-conditioned 还是 uniform）相比纯 LoRA 微调零增量。LoRA fine-tuning 是 GAR recovery 的唯一来源。hypothesis 被证伪：TRG 不比 LoRA-only 更好。"
1774	}
1775	
1776	================================================================================
1777	EXPERIMENT: phase2_4way_eval_heldout
1778	================================================================================
1779	{
1780	  "status": "DONE",
1781	  "retry_count": 0,
1782	  "created_at": "2026-05-19T13:58:59.269Z",
1783	  "updated_at": "2026-05-19T14:35:47.201Z",
1784	  "hypothesis": "四路消融的三路趋同结论（TG≈UG≈LoRA-only，gating 零增量）在 held-out eval 数据（idx≥8000，与训练集无重叠）上复现，排除数据重叠 confound。预期：相对比较保持（三路趋同），绝对 GAR 值可能变化。",
1785	  "parent": "phase2_4way_eval",
1786	  "spec": {
1787	    "command": "bash -c \"cd /root/turn_residual_gating && bash scripts/run_4way_eval_heldout.sh\"",
1788	    "server": "westd-20861",
1789	    "gpu": "cuda:0",
1790	    "pid": 67204,
1791	    "log_path": "~/runs/turn_residual_gating/phase2_4way_eval_heldout.log",
1792	    "submitted_at": "2026-05-19T14:01:00.965Z",
1793	    "submitted_via": "submit_training_job",
1794	    "backend": "tmux",
1795	    "account": "root",
1796	    "data_path": "/root/turn_residual_gating/data/ultrachat_eval_heldout.json",
1797	    "data_count": 50,
1798	    "model_name": "Qwen2.5-7B-Instruct",
1799	    "seed": 42,
1800	    "checkpoint_source": "phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42",
1801	    "eval_data": "ultrachat_eval_heldout.json (50 convs, idx 8843-68199, no overlap with training 0-7999)",
1802	    "configs": "4 models (Base/TG_v7/UG/LoRA-only) x 2 GAR variants (ours/Dongre) = 8 eval runs",
1803	    "checkpoint_path": "N/A (eval-only)",
1804	    "wall_clock_seconds": 2086.2,
1805	    "gpu_hours": 0.58
1806	  },
1807	  "reproduce": {
1808	    "finished_at": "2026-05-19T14:32:09.481Z"
1809	  },
1810	  "metrics": {
1811	    "base_ours_mid_gar": 0.0128,
1812	    "base_ours_recovery_pp": 0.06,
1813	    "base_dongre_mid_gar": 0.0031,
1814	    "base_dongre_recovery_pp": -0.91,
1815	    "base_ppl": 4.34,
1816	    "base_ntp": 1.4045,
1817	    "tg_ours_mid_gar": 0.5035,
1818	    "tg_ours_recovery_pp": 49.13,
1819	    "tg_dongre_mid_gar": 0.0152,
1820	    "tg_dongre_recovery_pp": 0.3,
1821	    "tg_ppl": 2.78,
1822	    "tg_ntp": 0.9771,
1823	    "ug_ours_mid_gar": 0.5053,
1824	    "ug_ours_recovery_pp": 49.31,
1825	    "ug_dongre_mid_gar": 0.0124,
1826	    "ug_dongre_recovery_pp": 0.02,
1827	    "ug_ppl": 2.78,
1828	    "ug_ntp": 0.9752,
1829	    "lora_ours_mid_gar": 0.4978,
1830	    "lora_ours_recovery_pp": 48.56,
1831	    "lora_dongre_mid_gar": 0.0132,
1832	    "lora_dongre_recovery_pp": 0.1,
1833	    "lora_ppl": 2.78,
1834	    "lora_ntp": 0.9771,
1835	    "three_way_convergence_confirmed": true,
1836	    "gar_ours_spread_pp": 0.75,
1837	    "ppl_spread": 0,
1838	    "data_overlap": false
1839	  },
1840	  "conclusion": "success",
1841	  "notes": "Held-out eval 三路趋同完全复现。TG/UG/LoRA-only GAR-ours: 0.504/0.505/0.498 (spread 0.75pp), PPL 均为 2.78。与 overlap 数据相比绝对值略高（GAR +1-2pp, PPL +0.15），属正常泛化偏移，相对比较完全一致。数据完整性 confound 已排除。",
1842	  "completed_at": "2026-05-19T14:35:47.202Z"
1843	}
1844	
1845	================================================================================
1846	EXPERIMENT: phase2_lora_only_s42
1847	================================================================================
1848	{
1849	  "status": "DONE",
1850	  "retry_count": 1,
1851	  "created_at": "2026-05-18T20:36:32.506Z",
1852	  "updated_at": "2026-05-20T02:15:18.992Z",
1853	  "hypothesis": "LoRA-only baseline (gate 固定 1.0，无 gating 机制) 在相同 MSE+NTP loss 下 GAR 应低于 ThreadGate (v7)。如果 LoRA-only 也能训到 GAR~0.5，则 gating 机制贡献为零，paper story 不成立。关键对比：LoRA-only 的 GAR 收敛值 vs v7 的 0.48。",
1854	  "parent": "phase2_tg_s42_v7",
1855	  "failure_reason": "EXIT_CODE=1 (generic error — check log tail)",
1856	  "completed_at": "2026-05-19T12:44:29.475Z",
1857	  "extra": {
1858	    "previous_failure": {
1859	      "conclusion": "failed"
1860	    },
1861	    "hook_events": [
1862	      {
1863	        "event": "on_failed",
1864	        "action": "agent",
1865	        "ts": "2026-05-19T13:04:35.644174+00:00"
1866	      }
1867	    ]
1868	  },
1869	  "spec": {
1870	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type lora_only --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 0.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_lora_only_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\"",
1871	    "server": "westd-20861",
1872	    "gpu": "cuda:0",
1873	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
1874	    "data_count": 8000,
1875	    "model_name": "Qwen2.5-7B-Instruct",
1876	    "seed": 42,
1877	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_lora_only_s42",
1878	    "log_path": "/root/turn_residual_gating/runs/phase2_lora_only_s42.log",
1879	    "checkpoint_source": "from_scratch",
1880	    "eval_data": "N/A"
1881	  },
1882	  "reproduce": {
1883	    "finished_at": "2026-05-19T13:04:33.523Z"
1884	  },
1885	  "conclusion": "success",
1886	  "metrics": {
1887	    "epochs_completed": 3,
1888	    "global_steps": 3000,
1889	    "training_time_seconds": 20588.6,
1890	    "training_time_hours": 5.7,
1891	    "gate_fixed": 1,
1892	    "gate_type_actual": "none",
1893	    "final_lora_size_mb": 20,
1894	    "eval_modelgen_ours_mid_gar": 0.0245,
1895	    "eval_modelgen_dongre_mid_gar": 0.0185,
1896	    "eval_modelgen_ppl": 1.371
1897	  },
1898	  "checkpoint_path": "/root/runs/turn_residual_gating/runs/phase2_lora_only_s42/lora/",
1899	  "log_path": "/root/runs/turn_residual_gating/phase2_lora_only_s42.log",
1900	  "notes": "诊断确认：EXIT_CODE=1 因 argparse 不认 lora_only 选项（choices 只有 threadgate/uniform/none）。训练实际已用 --gate-type none 完成 3 epoch (3000 steps, 20588.6s/5.7h)。Gate 全程固定 1.0（符合 lora_only 语义）。Checkpoint 可用，无需重跑。修复：dispatch 命令改用 --gate-type none 或在 train_phase2.py 添加 lora_only choice。"
1901	}
1902	
1903	================================================================================
1904	EXPERIMENT: phase2_switching
1905	================================================================================
1906	{
1907	  "status": "DONE",
1908	  "retry_count": 0,
1909	  "created_at": "2026-05-25T08:58:40.187Z",
1910	  "updated_at": "2026-05-25T09:42:21.391Z",
1911	  "hypothesis": "TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.",
1912	  "conclusion": "killed",
1913	  "completed_at": "2026-05-25T09:42:21.391Z"
1914	}
1915	
1916	================================================================================
1917	EXPERIMENT: phase2_tf_ar_switching
1918	================================================================================
1919	{
1920	  "status": "QUEUED",
1921	  "retry_count": 0,
1922	  "created_at": "2026-05-25T06:15:36.221Z",
1923	  "updated_at": "2026-05-25T06:45:27.338Z",
1924	  "hypothesis": "TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift."
1925	}
1926	
1927	================================================================================
1928	EXPERIMENT: phase2_tg_s42
1929	================================================================================
1930	{
1931	  "status": "DONE",
1932	  "retry_count": 0,
1933	  "created_at": "2026-05-18T06:04:12.759Z",
1934	  "updated_at": "2026-05-22T04:36:54.262Z",
1935	  "hypothesis": "ThreadGate (turn-conditional gating) 在 L_NTP+L_GAR 联合训练后，相比 Uniform Gate，mid-turn GAR recovery 高出 ≥3pp，验证 Cesaro 理论预测：position-conditional 干预优于 uniform 干预",
1936	  "parent": "phase1_gar_diag",
1937	  "spec": {
1938	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating/src && python train_phase2.py --gate-type threadgate --seed 42 --output-dir /root/turn_residual_gating/checkpoints/tg_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-seq-len 2048\"",
1939	    "server": "westd-20861",
1940	    "gpu": [
1941	      "cuda:0"
1942	    ],
1943	    "pid": "11286",
1944	    "log_path": "~/runs/turn_residual_gating/phase2_tg_s42.log",
1945	    "submitted_at": "2026-05-18T07:03:28.476Z",
1946	    "submitted_via": "submit_training_job",
1947	    "backend": "tmux",
1948	    "account": "root",
1949	    "wall_clock_seconds": 15333,
1950	    "gpu_hours": 4.26,
1951	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
1952	    "data_count": 8000,
1953	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
1954	    "seed": 42,
1955	    "checkpoint_path": "/root/turn_residual_gating/checkpoints/tg_s42"
1956	  },
1957	  "server": "westd-20861",
1958	  "gpu": "cuda:0",
1959	  "pid": "11286",
1960	  "log_path": "~/runs/turn_residual_gating/phase2_tg_s42.log",
1961	  "reproduce": {
1962	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating/src && python train_phase2.py --gate-type threadgate --seed 42 --output-dir /root/turn_residual_gating/checkpoints/tg_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-seq-len 2048\"",
1963	    "finished_at": "2026-05-18T11:19:00.888Z"
1964	  },
1965	  "failure_reason": "EXIT_CODE=143 (SIGTERM — graceful kill)",
1966	  "conclusion": "negative",
1967	  "completed_at": "2026-05-18T11:19:01.512Z",
1968	  "extra": {
1969	    "hook_events": [
1970	      {
1971	        "event": "on_failed",
1972	        "action": "agent",
1973	        "ts": "2026-05-18T11:19:02.835359+00:00"
1974	      }
1975	    ]
1976	  },
1977	  "notes": "失败原因: EXIT_CODE=143 (SIGTERM) — 大概率被 Worker code:diagnose_gar_loss_and_fix 主动 kill（时间线：Worker 11:13 启动 → v2 11:13 创建 → v1 11:19 SIGTERM）。v2 hypothesis 指出 GAR loss 实现有 bug（缺少 ε=0.001 稳定项）。诊断 Worker worker_diagnose_phase2_tg_s42_20260518T112048 已派出确认日志详情。| 建议: 等诊断结果确认后推进 v2",
1978	  "checkpoint_path": "/root/turn_residual_gating/checkpoints/tg_s42/epoch_1",
1979	  "metrics": {
1980	    "final_ntp_loss": 0.94,
1981	    "final_gar_loss": 0,
1982	    "gate_mean": 0.988,
1983	    "gar_loss_zero_pct": 87.6,
1984	    "epochs_completed": 1.67,
1985	    "killed_reason": "SIGTERM by diagnose worker (unauthorized)"
1986	  }
1987	}
1988	
1989	================================================================================
1990	EXPERIMENT: phase2_tg_s42_v2
1991	================================================================================
1992	{
1993	  "status": "DONE",
1994	  "retry_count": 0,
1995	  "created_at": "2026-05-18T11:13:37.042Z",
1996	  "updated_at": "2026-05-18T13:11:26.331Z",
1997	  "hypothesis": "ThreadGate + 修复后的 cumulative GAR loss (ε=0.001) 在 L_NTP+L_GAR 联合训练后，mid-turn GAR recovery 应显著优于 v1 (NTP-only baseline)，验证 GAR loss 的有效性",
1998	  "parent": "phase2_tg_s42",
1999	  "server": "westd-20861",
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06691c56-d065-4bae-9fb4-76470d88ed67",
  "isSidechain": true,
  "promptId": "1f7ff205-71d0-4ca7-a71f-3ee7850be97d",
  "agentId": "a24bf7311cd045b90",
  "type": "user",
  "uuid": "5ec3db9c-119a-40bb-9110-de3750021a9b",
  "sourceToolAssistantUUID": "06691c56-d065-4bae-9fb4-76470d88ed67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-25T20:13:50.832Z_

<details open><summary>🔧 Tool call — Read · `toolu_015b1dJB3wA8EGqRSfDA5E9P`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt",
  "offset": 2000,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ec3db9c-119a-40bb-9110-de3750021a9b",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu6Bmffe1tgicPtFSfq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95ecd301-fa62-4ecd-952e-67aa7c144fb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kTBqLf5RDiqRj9Q8Q5JYg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10281,
      "cache_read_input_tokens": 48733,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10281
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 48733,
          "cache_creation_input_tokens": 10281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10281,
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

_source line 29 · 2026-05-25T20:13:50.843Z_

<details><summary>↩ Tool result · `toolu_015b1dJB3wA8EGqRSfDA5E9P`</summary>

```text
2000	  "gpu": "cuda:0",
2001	  "reproduce": {
2002	    "server": "westd-20861",
2003	    "gpu": "cuda:0",
2004	    "started_at": "2026-05-18T11:45:26.657Z",
2005	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating/src && python train_phase2.py --gate-type threadgate --seed 42 --output-dir /root/turn_residual_gating/checkpoints/tg_s42_v2 --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-seq-len 2048 --gar-loss-mode cumulative --gar-epsilon 0.001 --init-bias 2.0 --lambda-gar 5.0\""
2006	  },
2007	  "spec": {
2008	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating/src && python train_phase2.py --gate-type threadgate --seed 42 --output-dir /root/turn_residual_gating/checkpoints/tg_s42_v2 --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-seq-len 2048 --gar-loss-mode cumulative --gar-epsilon 0.001 --init-bias 2.0 --lambda-gar 5.0\"",
2009	    "server": "westd-20861",
2010	    "gpu": [
2011	      "cuda:0"
2012	    ],
2013	    "pid": "25726",
2014	    "log_path": "~/runs/turn_residual_gating/phase2_tg_s42_v2.log",
2015	    "submitted_at": "2026-05-18T11:50:47.143Z",
2016	    "submitted_via": "submit_training_job",
2017	    "backend": "tmux",
2018	    "account": "root",
2019	    "checkpoint_path": "/root/turn_residual_gating/checkpoints/tg_s42_v2",
2020	    "wall_clock_seconds": 4839.2,
2021	    "gpu_hours": 1.34
2022	  },
2023	  "pid": "25726",
2024	  "log_path": "~/runs/turn_residual_gating/phase2_tg_s42_v2.log",
2025	  "conclusion": "killed",
2026	  "completed_at": "2026-05-18T13:11:26.331Z"
2027	}
2028	
2029	================================================================================
2030	EXPERIMENT: phase2_tg_s42_v3
2031	================================================================================
2032	{
2033	  "status": "DONE",
2034	  "retry_count": 0,
2035	  "created_at": "2026-05-18T13:07:54.463Z",
2036	  "updated_at": "2026-05-18T13:38:10.723Z",
2037	  "hypothesis": "ThreadGate + maximize GAR loss (L_GAR=-mean(GAR)) 提供持续非零梯度，避免 hinge loss 的退化平衡点，gate 值应随训练下降（学习到选择性干预），同时 NTP loss 正常收敛",
2038	  "parent": "phase2_tg_s42_v2",
2039	  "spec": {
2040	    "server": "westd-20861",
2041	    "gpu": "cuda:0",
2042	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
2043	    "data_count": 8000,
2044	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
2045	    "seed": 42,
2046	    "command": "python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 2.0 --init-bias 2.0 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v3 --data-dir /root/turn_residual_gating/data/ultrachat_8k",
2047	    "pid": "30973",
2048	    "log_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v3.log",
2049	    "checkpoint_source": "N/A (training from scratch with LoRA)",
2050	    "eval_data": "N/A (training experiment, not eval)",
2051	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v3"
2052	  },
2053	  "server": "westd-20861",
2054	  "gpu": "cuda:0",
2055	  "conclusion": "negative",
2056	  "metrics": {
2057	    "gate_mean_step0": 0.8743,
2058	    "gate_mean_step500": 0.8761,
2059	    "gate_delta": 0.004,
2060	    "gate_std": 0.001,
2061	    "final_ntp_loss": 0.94,
2062	    "final_gar_loss": -0.019,
2063	    "gar_contribution_pct": "2-4%",
2064	    "diagnosis": "gate frozen, GAR indirect gradient too weak"
2065	  },
2066	  "completed_at": "2026-05-18T13:38:10.723Z"
2067	}
2068	
2069	================================================================================
2070	EXPERIMENT: phase2_tg_s42_v3b
2071	================================================================================
2072	{
2073	  "status": "DONE",
2074	  "retry_count": 0,
2075	  "created_at": "2026-05-18T13:38:16.020Z",
2076	  "updated_at": "2026-05-18T14:51:42.486Z",
2077	  "hypothesis": "λ=10 + gate_lr=10x + init_bias=0.0 (sigmoid=0.5) 能否驱动 gate 产生 layer 间分化 (gate_std>0.05)？如果 500 步后 gate_std<0.02 且无选择性 → GAR-driven gating 梯度路径确认失败，需要 pivot",
2078	  "parent": "phase2_tg_s42_v3",
2079	  "spec": {
2080	    "command": "python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 10.0 --init-bias 0.0 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v3b --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-steps 500",
2081	    "server": "westd-20861",
2082	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
2083	    "data_count": 8000,
2084	    "model_name": "Qwen2.5-7B-Instruct",
2085	    "seed": 42,
2086	    "checkpoint_source": "from_scratch",
2087	    "eval_data": "N/A",
2088	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v3b",
2089	    "log_path": "/root/turn_residual_gating/runs/v3b_log.txt"
2090	  },
2091	  "conclusion": "success",
2092	  "metrics": {
2093	    "gate_std_final": 0.087,
2094	    "gate_mean_final": 0.9388,
2095	    "gate_min_final": 0.5352,
2096	    "gate_max_final": 0.9922,
2097	    "L4_gate": 0.535,
2098	    "L0_gate": 0.777,
2099	    "L_NTP_final": 0.7787,
2100	    "L_GAR_final": -0.9606,
2101	    "elapsed_seconds": 3565.9,
2102	    "optimizer_steps": 500,
2103	    "gate_grad_received": true
2104	  },
2105	  "completed_at": "2026-05-18T14:51:42.486Z"
2106	}
2107	
2108	================================================================================
2109	EXPERIMENT: phase2_tg_s42_v4
2110	================================================================================
2111	{
2112	  "status": "DONE",
2113	  "retry_count": 0,
2114	  "created_at": "2026-05-18T14:58:00.124Z",
2115	  "updated_at": "2026-05-18T16:50:36.202Z",
2116	  "hypothesis": "重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值",
2117	  "parent": "phase2_tg_s42_v3b",
2118	  "spec": {
2119	    "command": "python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v4 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3",
2120	    "server": "westd-20861",
2121	    "gpu": "cuda:0",
2122	    "pid": "36519",
2123	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
2124	    "data_count": 8000,
2125	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
2126	    "seed": 42,
2127	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v4",
2128	    "log_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v4.log",
2129	    "checkpoint_source": "from_scratch",
2130	    "eval_data": "N/A"
2131	  },
2132	  "conclusion": "failed",
2133	  "completed_at": "2026-05-18T16:50:33.778Z",
2134	  "notes": "进程在模型加载后崩溃，服务器重启导致进程丢失，无 checkpoint。日志仅有模型加载输出，无训练 step。GPU 重启后异常（100% util + 0 MiB + 无进程）。需要 GPU 健康恢复后重跑。"
2135	}
2136	
2137	================================================================================
2138	EXPERIMENT: phase2_tg_s42_v5
2139	================================================================================
2140	{
2141	  "status": "DONE",
2142	  "retry_count": 0,
2143	  "created_at": "2026-05-18T17:10:23.229Z",
2144	  "updated_at": "2026-05-18T17:52:54.605Z",
2145	  "hypothesis": "重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值",
2146	  "parent": "phase2_tg_s42_v4",
2147	  "spec": {
2148	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v5 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\"",
2149	    "server": "westd-20861",
2150	    "gpu": "cuda:0",
2151	    "pid": "3639",
2152	    "log_path": "~/runs/turn_residual_gating/phase2_tg_s42_v5.log",
2153	    "submitted_at": "2026-05-18T17:10:30.573Z",
2154	    "submitted_via": "submit_training_job",
2155	    "backend": "tmux",
2156	    "account": "root",
2157	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
2158	    "data_count": 8000,
2159	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
2160	    "seed": 42,
2161	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v5",
2162	    "checkpoint_source": "from_scratch",
2163	    "eval_data": "N/A",
2164	    "wall_clock_seconds": 2539.4,
2165	    "gpu_hours": 0.71
2166	  },
2167	  "metrics": {
2168	    "step2000_gate_std": 0.0225,
2169	    "step2000_gate_mean": 0.9586,
2170	    "step2000_gate_min": 0.9062,
2171	    "step2000_gate_max": 0.9961,
2172	    "step2000_L_GAR": -0.8977,
2173	    "step2000_L_NTP": 0.7611,
2174	    "step2000_total_loss": -0.1365,
2175	    "step2400_gate_std": 0.0219,
2176	    "step2400_gate_mean": 0.9651,
2177	    "step2400_gate_min": 0.918,
2178	    "step2400_gate_max": 0.9961,
2179	    "step2400_profile": "L0=0.918 L12=0.918 L13=0.926 L1=0.996 L26=0.996",
2180	    "L_GAR_saturated_at": -0.91,
2181	    "gate_range_compression": "0.918-0.996"
2182	  },
2183	  "conclusion": "negative",
2184	  "completed_at": "2026-05-18T17:52:49.951Z",
2185	  "notes": "maximize 模式 gate 分化失败：gate_std=0.022↓ gate_mean=0.965↑，与 v3/v3b 同类结构性问题。L_GAR 饱和在 -0.91，maximize 的无界性驱动 gate 趋向恒等（全通过=最大 GAR），丧失层选择性。D009 指令立即 kill，转 v6 smooth_saturation。"
2186	}
2187	
2188	================================================================================
2189	EXPERIMENT: phase2_tg_s42_v6
2190	================================================================================
2191	{
2192	  "status": "DONE",
2193	  "retry_count": 0,
2194	  "created_at": "2026-05-18T17:53:01.911Z",
2195	  "updated_at": "2026-05-22T04:37:13.229Z",
2196	  "hypothesis": "smooth_saturation loss (-target*tanh(GAR/target), target=0.5) 提供有界但持续的 GAR 梯度，避免 maximize 的恒等退化（gate→1）和 hinge_target 的梯度消失（GAR达标后梯度=0）。预期：gate_std>0.05 的层间分化 + GAR 稳态在 0.3-0.5 + NTP loss 正常收敛 + 总 loss 为正。",
2197	  "parent": "phase2_tg_s42_v5",
2198	  "spec": {
2199	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type threadgate --gar-loss-mode smooth_saturation --gar-target 0.5 --lambda-gar 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v6 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\"",
2200	    "server": "westd-20861",
2201	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
2202	    "data_count": 8000,
2203	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
2204	    "seed": 42,
2205	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v6",
2206	    "log_path": "~/runs/turn_residual_gating/phase2_tg_s42_v6.log"
2207	  },
2208	  "metrics": {
2209	    "dryrun_step0_L_NTP": 2.0275,
2210	    "dryrun_step0_L_GAR": -0.0161,
2211	    "dryrun_step0_total_loss": 2.0114,
2212	    "dryrun_step4_L_NTP": 1.6544,
2213	    "dryrun_step4_L_GAR": -0.0147,
2214	    "dryrun_step4_total_loss": 1.6397,
2215	    "dryrun_gate_grad": true,
2216	    "dryrun_gate_mean_init": 0.8097,
2217	    "dryrun_gate_std_init": 0.0341,
2218	    "dryrun_gate_min_init": 0.6836,
2219	    "dryrun_gate_max_init": 0.8672,
2220	    "dryrun_gate_mean_step5": 0.8025,
2221	    "dryrun_gate_std_step5": 0.0842,
2222	    "dryrun_gate_min_step5": 0.5547,
2223	    "dryrun_gate_max_step5": 0.9805,
2224	    "gs50_gate_mean": 0.8117,
2225	    "gs50_gate_std": 0.0612,
2226	    "gs50_gate_min": 0.6836,
2227	    "gs50_gate_max": 0.9805,
2228	    "gs100_gate_mean": 0.8737,
2229	    "gs100_gate_std": 0.0367,
2230	    "gs100_gate_min": 0.8164,
2231	    "gs100_gate_max": 0.9766,
2232	    "gs100_L_NTP": 0.8151,
2233	    "gs100_L_GAR": -0.158,
2234	    "gs100_total_loss": 0.6571,
2235	    "gs100_profile_bottom3": "L12=0.816 L4=0.824 L13=0.824",
2236	    "gs100_profile_top3": "L27=0.977 L26=0.961 L23=0.914",
2237	    "gs143_L_GAR": -0.3876,
2238	    "gs143_gate_mean": 0.9227
2239	  },
2240	  "conclusion": "negative",
2241	  "notes": "smooth_saturation 与 maximize 同轨迹，单调 GAR 奖励导致恒等退化。step 100: gate_std=0.037↓ gate_mean=0.874↑，step ~143: L_GAR=-0.39 gate_mean=0.923。boundedness 只减缓退化速度不改变终态。D010 指令 kill 转 v7 MSE 双向 loss。",
2242	  "completed_at": "2026-05-18T18:18:07.869Z"
2243	}
2244	
2245	================================================================================
2246	EXPERIMENT: phase2_tg_s42_v7
2247	================================================================================
2248	{
2249	  "status": "DONE",
2250	  "retry_count": 0,
2251	  "created_at": "2026-05-18T18:17:45.739Z",
2252	  "updated_at": "2026-05-20T03:04:19.923Z",
2253	  "hypothesis": "MSE 双向 loss (mean_GAR - target)² + gate diversity 正则 F.relu(min_std - gate_std) 从结构上解决恒等退化：MSE 在 GAR > target 时反向惩罚（不再单调推高），gate_div 直接强制层间分化。预期：gate_std 稳定 >0.05 + GAR 收敛到 target=0.5 附近 + NTP 正常收敛。",
2254	  "parent": "phase2_tg_s42_v6",
2255	  "metrics": {
2256	    "eval_iid_ours_mid_gar": 0.5035,
2257	    "eval_iid_dongre_mid_gar": 0.0152,
2258	    "eval_iid_ppl": 2.784,
2259	    "eval_heldout_ours_mid_gar": 0.5035,
2260	    "eval_heldout_dongre_mid_gar": 0.0152,
2261	    "eval_heldout_ppl": 2.78,
2262	    "eval_modelgen_ours_mid_gar": 0.0157,
2263	    "eval_modelgen_dongre_mid_gar": 0.0194,
2264	    "eval_modelgen_ppl": 1.36,
2265	    "gate_mean_final": 0.9336,
2266	    "gate_std_final": 0.0492
2267	  },
2268	  "spec": {
2269	    "checkpoint_source": "from_scratch",
2270	    "eval_data": "N/A",
2271	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v7 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\"",
2272	    "server": "westd-20861",
2273	    "gpu": "cuda:0",
2274	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
2275	    "data_count": 8000,
2276	    "model_name": "Qwen2.5-7B-Instruct",
2277	    "seed": 42,
2278	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v7",
2279	    "log_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v7.log"
2280	  },
2281	  "reproduce": {
2282	    "finished_at": "2026-05-19T00:48:47.275Z"
2283	  },
2284	  "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed",
2285	  "conclusion": "success",
2286	  "completed_at": "2026-05-19T00:48:47.463Z",
2287	  "extra": {
2288	    "hook_events": [
2289	      {
2290	        "event": "on_failed",
2291	        "action": "agent",
2292	        "ts": "2026-05-19T00:48:48.850580+00:00"
2293	      }
2294	    ]
2295	  },
2296	  "notes": "训练 3 epoch 完成 (21352s/5.9h)。最终 gate: mean=0.9336, std=0.0492, L3=0.801 L4=0.789 最低。Eval 完成：GAR-ours recovery +0.35pp (mid 0.0157 vs baseline 0.0122), GAR-Dongre recovery +0.72pp (mid 0.0194 vs baseline 0.0122)。Gate dynamic range 最大层: L23 diff=-0.2100, L14 diff=-0.1803。"
2297	}
2298	
2299	================================================================================
2300	EXPERIMENT: phase2_tg_s42_v8_schedsampling
2301	================================================================================
2302	{
2303	  "status": "DONE",
2304	  "retry_count": 0,
2305	  "created_at": "2026-05-19T15:02:00.223Z",
2306	  "updated_at": "2026-05-19T16:33:04.989Z",
2307	  "hypothesis": "Scheduled sampling 应用到 GAR loss（线性从 0→0.5 混合 teacher-forced + model-generated contexts）能缩小 v7 的 30x training-inference GAR gap。机制：在 model-generated context 上计算 GAR loss 迫使 attention pattern 适应推理时分布，直接 address teacher-forcing distribution shift。成功标准：inference GAR 显著高于 v7 的 0.016，PPL 不显著恶化（≤2.78+0.2）。",
2308	  "parent": "phase2_tg_s42_v7",
2309	  "spec": {
2310	    "command": "python src/train_phase2_v8.py --scheduled-sampling --ss-max-ratio 0.5",
2311	    "server": "westd-20861",
2312	    "gpu": "cuda:0",
2313	    "pid": 73838,
2314	    "log_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v8_schedsampling/",
2315	    "submitted_at": "2026-05-19T15:43:01.461Z",
2316	    "submitted_via": "submit_training_job",
2317	    "backend": "tmux",
2318	    "account": "root",
2319	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
2320	    "data_count": 8000,
2321	    "model_name": "Qwen2.5-7B-Instruct",
2322	    "seed": 42,
2323	    "checkpoint_source": "N/A (training from scratch with LoRA)",
2324	    "eval_data": "ultrachat_eval_heldout.json (post-training eval)",
2325	    "hyperparams": {
2326	      "lr": 0.0002,
2327	      "epochs": 3,
2328	      "grad_accum": 8,
2329	      "ss_max_ratio": 0.5,
2330	      "ss_gen_max_tokens": 256,
2331	      "ss_gen_temperature": 0.7
2332	    },
2333	    "estimated_hours": "8-9",
2334	    "checkpoint_path": "N/A (crashed at 5.8%)",
2335	    "wall_clock_seconds": 1611.0,
2336	    "gpu_hours": 0.45
2337	  },
2338	  "conclusion": "failed",
2339	  "completed_at": "2026-05-19T16:09:52.423Z",
2340	  "metrics": {
2341	    "killed_at_microstep": 1950,
2342	    "total_microsteps": 24000,
2343	    "completion_pct": 8.1,
2344	    "global_step_approx": 244,
2345	    "total_global_steps": 3000,
2346	    "ss_steps_observed": 1,
2347	    "tf_lgar_mean_step850_1400": 0.0062,
2348	    "tf_lgar_std": 0.0082,
2349	    "tf_lgar_collapse_step": 800,
2350	    "gate_mean_final": 0.93,
2351	    "ss_ratio_at_kill": 0.081,
2352	    "crash_reason": "killed by director: SS path code bug (D026) makes experiment invalid, GPU needed for PCGrad",
2353	    "design_flaw_ss_ramp_too_slow": true,
2354	    "design_flaw_no_ss_tf_separate_logging": true
2355	  },
2356	  "notes": "Director kill at micro-step ~1950 (8.1%). 原因: SS path code bug (D026) + GAR-ours 无推理 gap (D024)，实验无效。GPU 转入 plan_018 PCGrad。详情：(1) SS ratio 仅 0.081 时 kill，仅 1 条 SS step 被日志捕获，(2) TF L_GAR 在 step 800 坍塌到 ≈0.006（与 v7 一致），(3) GAR-ours 推理时 ≈0.50 ≈ target，SS 用 GAR-ours 训练无法验证 exposure bias mitigation，(4) lambda_gar=2.0 (vs v7 的 1.0) confound 未被充分触发。"
2357	}
2358	
2359	================================================================================
2360	EXPERIMENT: phase2_tg_s42_v8b_resume
2361	================================================================================
2362	{
2363	  "status": "DONE",
2364	  "retry_count": 0,
2365	  "created_at": "2026-05-20T10:08:29.483Z",
2366	  "updated_at": "2026-05-21T01:56:13.289Z",
2367	  "hypothesis": "从 epoch_0 checkpoint resume v8b scheduled sampling 训练。SS 线性混合 0→0.5 teacher-forced + model-generated contexts。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。",
2368	  "parent": "phase2_tg_s42_v8b_ss_fixed",
2369	  "spec": {
2370	    "command": "python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir data/ultrachat_8k --output-dir checkpoints/tg_v8b_ss_fixed_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42 --scheduled-sampling --ss-max-ratio 0.5 --resume checkpoints/tg_v8b_ss_fixed_s42/epoch_0",
2371	    "server": "westd-20861",
2372	    "data_path": "data/ultrachat_8k",
2373	    "data_count": 8000,
2374	    "model_name": "Qwen2.5-7B-Instruct",
2375	    "seed": 42,
2376	    "checkpoint_source": "phase2_tg_s42_v8b_ss_fixed/epoch_0",
2377	    "eval_data": "N/A (training experiment)",
2378	    "checkpoint_path": "checkpoints/tg_v8b_ss_fixed_s42",
2379	    "log_path": "~/runs/turn_residual_gating/phase2_tg_s42_v8b_resume.log"
2380	  },
2381	  "metrics": {
2382	    "training": {
2383	      "total_steps": 3000,
2384	      "epochs_completed": 3,
2385	      "wall_clock_hours": 8.1,
2386	      "final_loss": 0.933,
2387	      "final_ntp_loss": 0.9322,
2388	      "final_gar_loss": 0.0008,
2389	      "final_gate_mean": 0.9586,
2390	      "final_gate_std": 0.0582,
2391	      "ss_ratio": 0.5
2392	    },
2393	    "eval_iid": {
2394	      "gar_ours": 0.4983,
2395	      "gar_dongre": 0.3855,
2396	      "ppl": 2.78
2397	    },
2398	    "eval_modelgen": {
2399	      "gar_ours": 0.3177,
2400	      "gar_dongre": 0.3533,
2401	      "ppl": 1.38
2402	    },
2403	    "vs_v7": {
2404	      "iid_gar_ours_delta": -0.005,
2405	      "modelgen_gar_ours_delta": 0.302,
2406	      "gap_ratio_v7": 32,
2407	      "gap_ratio_v8b": 1.57
2408	    }
2409	  },
2410	  "conclusion": "success",
2411	  "completed_at": "2026-05-20T18:57:21.189Z"
2412	}
2413	
2414	================================================================================
2415	EXPERIMENT: phase2_tg_s42_v8b_ss_fixed
2416	================================================================================
2417	{
2418	  "status": "DONE",
2419	  "retry_count": 0,
2420	  "created_at": "2026-05-20T02:28:58.064Z",
2421	  "updated_at": "2026-05-20T09:30:04.080Z",
2422	  "spec": {
2423	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir data/ultrachat_8k --output-dir checkpoints/tg_v8b_ss_fixed_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42 --scheduled-sampling --ss-max-ratio 0.5\"",
2424	    "server": "westd-20861",
2425	    "gpu": [
2426	      "cuda:0"
2427	    ],
2428	    "pid": "133321",
2429	    "log_path": "~/runs/turn_residual_gating/phase2_tg_s42_v8b_ss_fixed.log",
2430	    "submitted_at": "2026-05-20T02:28:58.001Z",
2431	    "submitted_via": "submit_training_job",
2432	    "backend": "tmux",
2433	    "account": "root",
2434	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
2435	    "data_count": 8000,
2436	    "model_name": "Qwen2.5-7B-Instruct",
2437	    "seed": 42,
2438	    "checkpoint_path": "/root/turn_residual_gating/checkpoints/tg_v8b_ss_fixed_s42",
2439	    "checkpoint_source": "from_scratch",
2440	    "eval_data": "N/A",
2441	    "wall_clock_seconds": 24818.0,
2442	    "gpu_hours": 6.89
2443	  },
2444	  "hypothesis": "Fixed scheduled sampling (D026 三项 bug 修复后): 线性从 0→0.5 混合 teacher-forced + model-generated contexts 计算 GAR loss。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效，paper 从纯 negative 升级为 diagnosis + initial remedy。超参与 v7 一致 (lambda_gar=1.0, MSE+gate_div)，唯一变量是 SS path。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。",
2445	  "parent": "phase2_tg_s42_v7",
2446	  "failure_reason": "CUDA OOM: CUDA out of memory. Tried to allocate 448.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 247.19 MiB is free. Including non-PyTorch memory, this process has 50.68 GiB memory in use. Process 157667 has 26.76 GiB memory in use. Process 158713 ",
2447	  "conclusion": "failed",
2448	  "completed_at": "2026-05-20T09:22:35.962Z",
2449	  "notes": "CUDA OOM at Epoch 1 Step 4300 (loss.backward). 其他进程共享 GPU 导致显存不足: Process 157667 (26.76GB) + Process 158713 (17.28GB) + PyTorch 自身 45.21GB + 4.81GB reserved > 94.97GB 总容量。训练在 OOM 前正常收敛 (SS ratio=0.5, Loss~1.0, Gate~0.94)。有 epoch_0 checkpoint。需要独占 GPU 重跑。"
2450	}
2451	
2452	================================================================================
2453	EXPERIMENT: phase2_tg_s42_v9_pcgrad
2454	================================================================================
2455	{
2456	  "status": "DONE",
2457	  "retry_count": 2,
2458	  "created_at": "2026-05-19T16:13:21.907Z",
2459	  "updated_at": "2026-05-20T03:04:17.171Z",
2460	  "hypothesis": "PCGrad (Yu et al. NeurIPS 2020) 消除 NTP-GAR 梯度方向冲突后（仅对 gate 参数投影 NTP 梯度到 GAR 梯度正交平面），如果 30x training-inference GAR gap 仍在 → 因果证据证明 exposure bias（非梯度竞争）是 gap 根因。与 v7 对比：相同超参（lambda_gar=1.0, MSE+gate_div），唯一变量是梯度处理方式。成功标准：(1) 梯度 cos_sim 显著改善（从 v7 的 -0.089 提升到 ≥0），(2) 但推理 GAR 仍 ≈ v7 水平（0.016），证明梯度冲突不是 gap 的因。",
2461	  "parent": "phase2_tg_s42_v7",
2462	  "spec": {
2463	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2_v9_pcgrad.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir data/ultrachat_8k --output-dir checkpoints/tg_v9_pcgrad_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42\"",
2464	    "server": "westd-20861",
2465	    "gpu": [
2466	      "cuda:0"
2467	    ],
2468	    "pid": "83860",
2469	    "log_path": "/root/turn_residual_gating/logs/phase2_tg_v9_pcgrad_s42.log",
2470	    "submitted_at": "2026-05-19T17:42:10.820Z",
2471	    "submitted_via": "submit_training_job",
2472	    "backend": "tmux",
2473	    "account": "root",
2474	    "checkpoint_path": "/root/turn_residual_gating/checkpoints/tg_v9_pcgrad_s42",
2475	    "wall_clock_seconds": 30601.5,
2476	    "gpu_hours": 8.5
2477	  },
2478	  "reproduce": {
2479	    "finished_at": "2026-05-20T01:42:12.536Z"
2480	  },
2481	  "failure_reason": null,
2482	  "conclusion": "success",
2483	  "extra": {
2484	    "hook_events": [
2485	      {
2486	        "event": "on_failed",
2487	        "action": "agent",
2488	        "ts": "2026-05-19T17:35:39.776243+00:00",
2489	        "note": "第1次提交 EXIT_CODE=2 残留事件"
2490	      },
2491	      {
2492	        "event": "on_complete",
2493	        "action": "agent",
2494	        "ts": "2026-05-20T01:42:14.275822+00:00"
2495	      }
2496	    ]
2497	  },
2498	  "completed_at": null,
2499	  "notes": "D028 因果排除确认（M017 修正后）。训练: EXIT_CODE=0, 7.98h, 3 epochs。PCGrad cos_sim 从 -0.061→+0.055→-0.035 (围绕 0 振荡), NTP mag_ratio 2.8→28.8 持续增长。L_GAR 有 0-350 step 高原期后仍坍塌到≈0。IID eval (同 protocol 50 heldout convs): GAR-ours=0.5002 (vs v7 0.5035, diff -0.33pp), GAR-Dongre=0.0123 (vs v7 0.0152), PPL=2.780 (vs v7 2.784, diff 0.004, 无改善)。Model-gen eval (5 convs): GAR-ours=0.0151, PPL=1.50。结论: PCGrad 消除梯度方向冲突后所有 IID 指标均 ≈ v7（GAR、PPL、NTP 无变化），方向冲突因 NTP 幅度主导 (10-40x) 而 inconsequential。Exposure bias 是 30x gap 根因。",
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95ecd301-fa62-4ecd-952e-67aa7c144fb5",
  "isSidechain": true,
  "promptId": "1f7ff205-71d0-4ca7-a71f-3ee7850be97d",
  "agentId": "a24bf7311cd045b90",
  "type": "user",
  "uuid": "9c320ddf-a2a1-435b-be62-5da69e5454b3",
  "sourceToolAssistantUUID": "95ecd301-fa62-4ecd-952e-67aa7c144fb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-25T20:14:05.550Z_

<details open><summary>🔧 Tool call — Read · `toolu_018GcNStt28Yn5BUNoVs62eD`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt",
  "offset": 2500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c320ddf-a2a1-435b-be62-5da69e5454b3",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu6gyLMgaZNfBsEihiL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edc7d64e-d0f3-4a30-bead-8ed86cf78611",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0117FbE3W3xQHumQqM3iBmL7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12796,
      "cache_read_input_tokens": 59014,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12796
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 59014,
          "cache_creation_input_tokens": 12796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12796,
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

_source line 31 · 2026-05-25T20:14:05.572Z_

<details><summary>↩ Tool result · `toolu_018GcNStt28Yn5BUNoVs62eD`</summary>

```text
2500	  "metrics": {
2501	    "eval_iid_ours_mid_gar": 0.5002,
2502	    "eval_iid_dongre_mid_gar": 0.0123,
2503	    "eval_iid_ppl": 2.78,
2504	    "eval_iid_ntp": 0.9752,
2505	    "eval_heldout_ours_mid_gar": 0.5002,
2506	    "eval_heldout_dongre_mid_gar": 0.0123,
2507	    "eval_heldout_ppl": 2.78,
2508	    "eval_heldout_ntp": 0.9752,
2509	    "eval_modelgen_ours_mid_gar": 0.0151,
2510	    "eval_modelgen_dongre_mid_gar": 0.0173,
2511	    "eval_modelgen_ppl": 1.5,
2512	    "vs_v7_iid_ppl_diff": 0.004,
2513	    "vs_v7_iid_gar_diff": -0.0033
2514	  }
2515	}
2516	
2517	================================================================================
2518	EXPERIMENT: phase2_ug_s42
2519	================================================================================
2520	{
2521	  "status": "DONE",
2522	  "retry_count": 0,
2523	  "created_at": "2026-05-18T06:04:17.643Z",
2524	  "updated_at": "2026-05-20T02:15:15.775Z",
2525	  "hypothesis": "Uniform gating baseline: per-layer independent gates without turn conditioning (content-dependent only), to isolate whether ThreadGate's turn-conditioned gating provides benefit over content-only residual scaling. Same training setup as v7 but with gate-type=uniform.",
2526	  "parent": "phase1_gar_diag",
2527	  "notes": "3 epoch 完成 (21994.5s/6.1h)。最终 gate: mean=0.9598, std=0.0518, L3=0.777 L5=0.812 最低。重要发现：uniform gate 模式下各层仍学出 per-layer 分化（L3=0.777 vs L27=1.000），与 ThreadGate v7 的 L3/L4 最低模式一致。这说明 per-layer variation 可能来自 LoRA+GAR loss 而非 gate architecture。",
2528	  "spec": {
2529	    "command": "python src/train_phase2.py --gate-type uniform --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_ug_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3",
2530	    "server": "westd-20861",
2531	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
2532	    "data_count": 8000,
2533	    "model_name": "Qwen2.5-7B-Instruct",
2534	    "seed": 42,
2535	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_ug_s42",
2536	    "log_path": "/root/turn_residual_gating/runs/phase2_ug_s42.log",
2537	    "checkpoint_source": "from_scratch",
2538	    "eval_data": "N/A"
2539	  },
2540	  "conclusion": "success",
2541	  "completed_at": "2026-05-19T06:53:13.931Z",
2542	  "metrics": {
2543	    "epoch0_avg_loss": 1.0019,
2544	    "epoch0_avg_ntp": 0.9755,
2545	    "epoch0_avg_gar": 0.0259,
2546	    "epoch0_avg_div": 0.0005,
2547	    "epoch1_avg_loss": 0.9447,
2548	    "epoch1_avg_ntp": 0.9435,
2549	    "epoch1_avg_gar": 0.0013,
2550	    "epoch1_avg_div": 0,
2551	    "epoch2_avg_loss": 0.9319,
2552	    "epoch2_avg_ntp": 0.9309,
2553	    "epoch2_avg_gar": 0.001,
2554	    "epoch2_avg_div": 0,
2555	    "final_gate_mean": 0.9598,
2556	    "final_gate_std": 0.0518,
2557	    "final_gate_min": 0.7773,
2558	    "final_gate_max": 1,
2559	    "final_profile_L3": 0.777,
2560	    "final_profile_L5": 0.812,
2561	    "final_profile_L0": 0.875,
2562	    "final_profile_L27": 1,
2563	    "training_time_seconds": 21994.5,
2564	    "training_time_hours": 6.1,
2565	    "global_steps": 7950,
2566	    "unexpected_per_layer_variation": true,
2567	    "eval_modelgen_ours_mid_gar": 0.0149,
2568	    "eval_modelgen_dongre_mid_gar": 0.0185,
2569	    "eval_modelgen_ppl": 1.396
2570	  },
2571	  "checkpoint_path": "/root/turn_residual_gating/runs/phase2_ug_s42",
2572	  "log_path": "/root/turn_residual_gating/runs/phase2_ug_s42.log"
2573	}
2574	
2575	================================================================================
2576	EXPERIMENT: qwen15b_phase1_diag
2577	================================================================================
2578	{
2579	  "status": "DONE",
2580	  "retry_count": 0,
2581	  "created_at": "2026-05-23T06:44:59.895Z",
2582	  "updated_at": "2026-05-24T06:53:23.496Z",
2583	  "hypothesis": "GAR attention decay toward system-prompt goal tokens is a general phenomenon across model scales, not specific to 7B. Qwen-2.5-1.5B-Instruct should also show progressive GAR decline across conversation turns, confirming the phenomenon is architecture-level rather than scale-dependent.",
2584	  "spec": {
2585	    "command": "python train_phase2.py --model Qwen/Qwen2.5-1.5B-Instruct --config configs/tg_v7.yaml --seed 42 --epochs 3",
2586	    "server": "westd-20861",
2587	    "data_path": "/root/turn-residual-gating/data/train_400.json",
2588	    "data_count": 400,
2589	    "model_name": "Qwen/Qwen2.5-1.5B-Instruct",
2590	    "seed": 42,
2591	    "checkpoint_path": "runs/qwen15b_tg_v7_s42/",
2592	    "log_path": "logs/qwen15b_phase1_diag.log"
2593	  },
2594	  "conclusion": "success",
2595	  "completed_at": "2026-05-24T06:53:23.496Z"
2596	}
2597	
2598	================================================================================
2599	EXPERIMENT: trc_baseline_v7_tg
2600	================================================================================
2601	{
2602	  "status": "DONE",
2603	  "retry_count": 0,
2604	  "created_at": "2026-05-20T07:18:17.576Z",
2605	  "updated_at": "2026-05-20T09:34:40.734Z",
2606	  "hypothesis": "如果 exposure bias 对 auxiliary objectives 的破坏跨特征空间通用，那么 TRC (hidden state cos_sim) 在 model-gen 下也应出现与 GAR (attention 空间) 类似的 TF/gen gap。在 v7 TG / LoRA-only / base 三个 checkpoint 上测量 TRC baseline，确认 gap 是否存在。成功标准：gen TRC 显著低于 TF TRC。",
2607	  "parent": "phase2_tg_s42_v7",
2608	  "spec": {
2609	    "command": "bash scripts/launch_trc_baseline.sh",
2610	    "server": "westd-20861",
2611	    "gpu": [
2612	      "cuda:0"
2613	    ],
2614	    "pid": "158700",
2615	    "log_path": "/root/runs/turn_residual_gating/trc_baseline_v7_tg.log",
2616	    "submitted_at": "2026-05-20T07:18:38.202Z",
2617	    "submitted_via": "submit_training_job",
2618	    "backend": "tmux",
2619	    "account": "root",
2620	    "data_path": "/root/turn_residual_gating/data/standard_conversations.json",
2621	    "data_count": 5,
2622	    "model_name": "Qwen2.5-7B-Instruct",
2623	    "seed": 42,
2624	    "checkpoint_source": "phase2_tg_s42_v7 + phase2_lora_only_s42 + base",
2625	    "eval_data": "5 hardcoded multi-turn conversations x 10 turns",
2626	    "checkpoint_path": "/root/turn_residual_gating/runs/trc_baseline/",
2627	    "wall_clock_seconds": 7767.7,
2628	    "gpu_hours": 2.16
2629	  },
2630	  "conclusion": "success",
2631	  "completed_at": "2026-05-20T09:28:05.853Z",
2632	  "metrics": {
2633	    "v7_tg": {
2634	      "tf_trc": 0.3339,
2635	      "gen_trc": 0.3323,
2636	      "trc_gap": 0.0016,
2637	      "tf_tbp_ppl": 1.05,
2638	      "gen_tbp_ppl": 1.05
2639	    },
2640	    "lora_only": {
2641	      "tf_trc": 0.349,
2642	      "gen_trc": 0.4106,
2643	      "trc_gap": -0.0617,
2644	      "tf_tbp_ppl": 9.5,
2645	      "gen_tbp_ppl": 12
2646	    },
2647	    "base": {
2648	      "tf_trc": 0.1494,
2649	      "gen_trc": 0.1494,
2650	      "trc_gap": 0,
2651	      "tf_tbp_ppl": 2.05,
2652	      "gen_tbp_ppl": 2.05
2653	    }
2654	  },
2655	  "notes": "Cross-space 验证：exposure bias 是 attention-specific。v7 TG: TRC gap = +0.002 (近零)，hidden state 一致性在 TF/gen 之间无差异。对比 GAR 的 30x gap，TRC 无 gap → exposure bias 只扭曲 attention 分布，不影响 hidden state 层面。LoRA-only: 反转 gap (-0.062)，gen TRC 更高但 TBP PPL 严重恶化 (9.5→12.0)——hidden states \"坍缩\"趋同但信息量下降。Base: 零 gap（但可能有 eval 脚本 bug，gen 模式复用了 TF hidden states）。"
2656	}
2657	
2658	================================================================================
2659	EXPERIMENT: v7_tg_s123
2660	================================================================================
2661	{
2662	  "status": "DONE",
2663	  "retry_count": 0,
2664	  "created_at": "2026-05-21T15:16:39.923Z",
2665	  "updated_at": "2026-05-21T21:17:16.499Z",
2666	  "hypothesis": "v7 TG s42 已验证 ThreadGate 有效性，s123 验证 seed robustness。预期 gate profile 和 GAR 收敛模式与 s42 一致。",
2667	  "parent": "phase2_tg_s42_v7",
2668	  "spec": {
2669	    "command": "bash scripts/launch_v7_tg_s123.sh",
2670	    "server": "westd-20861",
2671	    "data_path": "data/ultrachat_8k",
2672	    "data_count": 8000,
2673	    "model_name": "Qwen2.5-7B-Instruct",
2674	    "seed": 123,
2675	    "pid": 245628,
2676	    "gpu_index": 0,
2677	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s123_v7",
2678	    "log_path": "/root/turn_residual_gating/logs/v7_tg_s123.log",
2679	    "checkpoint_source": "N/A (from scratch)",
2680	    "eval_data": "N/A"
2681	  },
2682	  "conclusion": "success",
2683	  "checkpoint_path": "runs/phase2_tg_s123_v7/epoch_2",
2684	  "log_path": "logs/v7_tg_s123.log",
2685	  "metrics": {
2686	    "epoch_1": {
2687	      "avg_loss": 0.9447,
2688	      "avg_ntp_loss": 0.9434,
2689	      "avg_gar_loss": 0.0013,
2690	      "avg_div_loss": 0
2691	    },
2692	    "epoch_2": {
2693	      "avg_loss": 0.9315,
2694	      "avg_ntp_loss": 0.9305,
2695	      "avg_gar_loss": 0.001,
2696	      "avg_div_loss": 0
2697	    },
2698	    "final_gate": {
2699	      "mean": 0.9467,
2700	      "std": 0.051,
2701	      "min": 0.793,
2702	      "max": 1
2703	    },
2704	    "final_gate_profile": {
2705	      "L0": 0.883,
2706	      "L1": 0.793,
2707	      "L2": 0.996,
2708	      "L3": 0.988,
2709	      "L4": 0.984,
2710	      "L5": 0.797,
2711	      "L6": 0.961,
2712	      "L7": 0.918,
2713	      "L8": 0.965,
2714	      "L9": 0.934,
2715	      "L10": 0.969,
2716	      "L11": 0.918,
2717	      "L12": 0.926,
2718	      "L13": 0.941,
2719	      "L14": 0.93,
2720	      "L15": 0.965,
2721	      "L16": 0.941,
2722	      "L17": 0.91,
2723	      "L18": 0.961,
2724	      "L19": 0.965,
2725	      "L20": 0.973,
2726	      "L21": 0.988,
2727	      "L22": 0.969,
2728	      "L23": 0.98,
2729	      "L24": 0.98,
2730	      "L25": 0.984,
2731	      "L26": 0.988,
2732	      "L27": 1
2733	    },
2734	    "training_time_s": 21425.2
2735	  },
2736	  "completed_at": "2026-05-21T21:17:16.499Z"
2737	}
2738	
2739	================================================================================
2740	EXPERIMENT: v8b_ss_s123
2741	================================================================================
2742	{
2743	  "status": "DONE",
2744	  "retry_count": 0,
2745	  "created_at": "2026-05-21T04:29:28.197Z",
2746	  "updated_at": "2026-05-21T15:15:49.282Z",
2747	  "hypothesis": "v8b SS s42 成功（gap 32×→1.57×），s123 验证结果的 seed robustness。预期 model-gen GAR 同样显著提升，PPL 无恶化。",
2748	  "parent": "phase2_tg_s42_v8b_resume",
2749	  "spec": {
2750	    "command": "bash scripts/launch_v8b_ss_s123.sh",
2751	    "server": "westd-20861",
2752	    "data_path": "data/ultrachat_8k",
2753	    "data_count": 8000,
2754	    "model_name": "Qwen2.5-7B-Instruct",
2755	    "seed": 123,
2756	    "checkpoint_source": "N/A (from scratch)",
2757	    "eval_data": "N/A",
2758	    "checkpoint_path": "/root/turn_residual_gating/checkpoints/tg_v8b_ss_s123",
2759	    "log_path": "/root/turn_residual_gating/logs/v8b_ss_s123.log"
2760	  },
2761	  "conclusion": "success",
2762	  "metrics": {
2763	    "final_loss": 0.9316,
2764	    "final_ntp_loss": 0.9307,
2765	    "final_gar_loss": 0.0009,
2766	    "final_gate_mean": 0.9505,
2767	    "final_gate_std": 0.0508,
2768	    "final_gate_min": 0.7383,
2769	    "final_gate_max": 1,
2770	    "ss_used_ratio": 0.371,
2771	    "training_time_s": 38773.4,
2772	    "epoch0_loss": 1.0092,
2773	    "epoch1_loss": 0.9444,
2774	    "epoch2_loss": 0.9316
2775	  },
2776	  "completed_at": "2026-05-21T15:15:49.282Z"
2777	}
2778	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edc7d64e-d0f3-4a30-bead-8ed86cf78611",
  "isSidechain": true,
  "promptId": "1f7ff205-71d0-4ca7-a71f-3ee7850be97d",
  "agentId": "a24bf7311cd045b90",
  "type": "user",
  "uuid": "9bd99d6a-f22e-4ec2-baa4-74237af81fa4",
  "sourceToolAssistantUUID": "edc7d64e-d0f3-4a30-bead-8ed86cf78611",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-25T20:14:09.314Z_

Now I have all the data. Let me also check if there are remaining experiments I haven't seen yet.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bd99d6a-f22e-4ec2-baa4-74237af81fa4",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu7mjMiFBxSqM1ZBShR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cffd9f85-9ec8-41d3-b281-3e1fdfa83a6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YF1pPcPbe7E5nH8Z4qFy1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5485,
      "cache_read_input_tokens": 71810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5485,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 33 · 2026-05-25T20:14:18.991Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EFu1Q8kf57dJiegA4un1rQ`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt') as f:\n    raw = json.load(f)\n\nresult_str = raw['result']\ndata = json.loads(result_str)\nexperiments = data['data']['experiments']\n\n# Count experiments with metrics\nwith_metrics = 0\nwithout_metrics = 0\nfor eid, exp in experiments.items():\n    if 'metrics' in exp and exp['metrics']:\n        with_metrics += 1\n    else:\n        without_metrics += 1\n\nprint(f\"Experiments with metrics: {with_metrics}\")\nprint(f\"Experiments without metrics: {without_metrics}\")\n\n# List the ones without metrics\nfor eid, exp in sorted(experiments.items()):\n    if 'metrics' not in exp or not exp['metrics']:\n        print(f\"  NO METRICS: {eid} (status={exp.get('status')}, conclusion={exp.get('conclusion')})\")\nPYEOF\n",
  "description": "Count experiments with/without metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cffd9f85-9ec8-41d3-b281-3e1fdfa83a6b",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu7mjMiFBxSqM1ZBShR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19cb2861-0593-47ff-ba37-485ff5bb528d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YF1pPcPbe7E5nH8Z4qFy1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5485,
      "cache_read_input_tokens": 71810,
      "output_tokens": 420,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5485
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 420,
          "cache_read_input_tokens": 71810,
          "cache_creation_input_tokens": 5485,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5485,
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

_source line 34 · 2026-05-25T20:14:19.069Z_

<details><summary>↩ Tool result · `toolu_01EFu1Q8kf57dJiegA4un1rQ`</summary>

```text
Experiments with metrics: 42
Experiments without metrics: 18
  NO METRICS: d048_queue_runner (status=PREPARING, conclusion=failed)
  NO METRICS: d048_split_softmax_eval (status=DONE, conclusion=failed)
  NO METRICS: d048_ss_s123 (status=DONE, conclusion=success)
  NO METRICS: d048_ss_s42_resume (status=PREPARING, conclusion=None)
  NO METRICS: d048_ss_s456 (status=DONE, conclusion=success)
  NO METRICS: llama_tg_training (status=PREPARING, conclusion=failed)
  NO METRICS: p0_ss_steering_eval (status=PREPARING, conclusion=killed)
  NO METRICS: p1_llama_ss_training (status=DONE, conclusion=success)
  NO METRICS: p1_ss_lora_only (status=DONE, conclusion=killed)
  NO METRICS: phase1a_multiseed_8runs (status=PREPARING, conclusion=None)
  NO METRICS: phase1a_multiseed_qwen (status=DONE, conclusion=killed)
  NO METRICS: phase1b_llama_complement (status=PREPARING, conclusion=None)
  NO METRICS: phase2_switching (status=DONE, conclusion=killed)
  NO METRICS: phase2_tf_ar_switching (status=QUEUED, conclusion=None)
  NO METRICS: phase2_tg_s42_v2 (status=DONE, conclusion=killed)
  NO METRICS: phase2_tg_s42_v4 (status=DONE, conclusion=failed)
  NO METRICS: phase2_tg_s42_v8b_ss_fixed (status=DONE, conclusion=failed)
  NO METRICS: qwen15b_phase1_diag (status=DONE, conclusion=success)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19cb2861-0593-47ff-ba37-485ff5bb528d",
  "isSidechain": true,
  "promptId": "1f7ff205-71d0-4ca7-a71f-3ee7850be97d",
  "agentId": "a24bf7311cd045b90",
  "type": "user",
  "uuid": "7229ac90-6be9-43e1-b180-48bba20e5bb1",
  "sourceToolAssistantUUID": "19cb2861-0593-47ff-ba37-485ff5bb528d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-25T20:17:44.831Z_

I now have the complete picture. Here is the full audit of all 60 experiments with every metric verbatim.

---

## FULL EXPERIMENT REGISTRY AUDIT (60 experiments)

### 1. analysis_attention_heatmap
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, 5 convs x 10 turns
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

### 2. analysis_gradient_conflict
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, v7 epoch 0/1/2 checkpoints
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

### 3. attention_steering_eval200_tf
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, N=200, mode=tf, checkpoint=phase2_tg_s42_v7
- **Metrics:**
  - beta_0.0: mid_gar=0.5353, ppl=2.62
  - beta_2.0: mid_gar=0.6112, ppl=2.69
  - beta_3.0: mid_gar=0.788, ppl=2.93
  - beta_4.0: mid_gar=0.8165, ppl=3.49
  - beta_5.0: mid_gar=0.8325, ppl=6.15
  - beta_10.0: mid_gar=0.977, ppl=505.21
  - n_convs: 200, mode: "tf"

### 4. attention_steering_gen_n50
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct + v7 TG LoRA, N=50, mode=gen, checkpoint=phase2_tg_s42_v7
- **Metrics (corrected, per-conv mid_gar turns 2-7, >=3 turns):**
  - beta_0.0: mid_gar=0.0641, mid_gar_std=0.0809, ppl=1.4324, ppl_std=0.1029, n_valid=39
  - beta_2.0: mid_gar=0.128, mid_gar_std=0.1101, ppl=1.4822, ppl_std=0.1385, n_valid=39
  - beta_3.0: mid_gar=0.5558, mid_gar_std=0.0601, ppl=1.5605, ppl_std=0.1719, n_valid=39
  - beta_4.0: mid_gar=0.6439, mid_gar_std=0.0607, ppl=1.6674, ppl_std=0.2241, n_valid=39
  - beta_5.0: mid_gar=0.7271, mid_gar_std=0.0605, ppl=1.7723, ppl_std=0.2693, n_valid=38
  - beta_10.0: mid_gar=0.9612, mid_gar_std=0.0152, ppl=3.4517, ppl_std=1.7813, n_valid=39
  - n_convs_total: 50, n_convs_valid: 39, phase_transition_range: "[2, 3]"

### 5. attention_steering_v7_tg_gen (N=5, gen mode)
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, N=5 convs, mode=gen, checkpoint=phase2_tg_s42_v7
- **Metrics:**
  - beta_0.0: mid_turns_avg_gar=0.028, avg_ppl=1.409
  - beta_0.5: mid_turns_avg_gar=0.0287, avg_ppl=1.387
  - beta_1.0: mid_turns_avg_gar=0.0349, avg_ppl=1.36
  - beta_2.0: mid_turns_avg_gar=0.062, avg_ppl=1.411
  - beta_5.0: mid_turns_avg_gar=0.6795, avg_ppl=1.908
  - beta_10.0: mid_turns_avg_gar=0.959, avg_ppl=4.22
  - phase_transition_range: "[2, 5]"
  - baseline_gar: 0.028
  - max_gar_at_acceptable_ppl: 0.6795
  - max_gar_at_acceptable_ppl_beta: 5

### 6. d048_eval_ss_s123
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct + SS s123 LoRA, seed=123, N_tf=200, N_ar=39
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

### 7. d048_eval_ss_s42
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct (SS s42), seed=42
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

### 8. d048_eval_ss_s456
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct + SS s456 LoRA, seed=456, N_ar=50
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

### 9. d048_final_ar_eval
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, 6 conditions, N=50 AR eval
- **Metrics (beta0):**
  - base_gar: 0.019
  - tg_gar: 0.064
  - ug_gar: 0.033
  - lo_gar: 0.037
  - pcgrad_gar: 0.03
  - ss_gar: 0.347
- **Metrics (beta3):**
  - base_gar: 0.531
  - tg_gar: 0.556
  - ss_gar: 0.593
- **Metrics (beta5):**
  - base_gar: 0.704
  - tg_gar: 0.727
  - ss_gar: 0.717
- **Wilcoxon (beta0):**
  - tg_vs_base_p: "<0.001"
  - tg_vs_base_r: 0.802
  - ss_vs_tg_p: "<0.001"
  - ss_vs_tg_r: 0.869
- **PPL:**
  - base: 1.447, tg: 1.432, ss: 1.442
- n_convs: 39

### 10. d048_queue_runner
- **Status:** PREPARING | **Conclusion:** failed
- **Metrics:** NONE

### 11. d048_split_softmax_eval
- **Status:** DONE | **Conclusion:** failed
- **Metrics:** NONE (bugs: system_prompt_len=0 hardcoded, gen mode NaN)

### 12. d048_ss_s123 (training only)
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=123, data=2000, lr=2e-4, epochs=3, batch_size=1, grad_accum=8, ss_ratio=0.3
- **Metrics:** NONE (training run, see d048_eval_ss_s123 for eval)

### 13. d048_ss_s42
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, ss_max_ratio=0.3, epochs=3, lr=2e-4, batch_size=1, grad_accum=8
- **Metrics (training):**
  - final_avg_loss: 0.9326
  - final_ntp_loss: 0.932
  - final_gar_loss: 0.0007
  - gate_mean: 0.9527
  - gate_std: 0.0589
  - gate_min: 0.7383
  - gate_min_layer: "L4"
  - gate_max: 1
  - ss_usage: "4750/16000 (29.7%)"
  - ss_fallback: 0
  - epochs_completed: 3
  - wall_clock_s: 23418, wall_clock_h: 6.5

### 14. d048_ss_s42_resume
- **Status:** PREPARING | **Conclusion:** None
- **Metrics:** NONE

### 15. d048_ss_s456 (training only)
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=456, data=2000, epochs=3, ss_ratio=0.3
- **Metrics:** NONE (training run, see d048_eval_ss_s456 for eval)

### 16. eval_llama_ar_n20
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct (Base/TG/LoRA-only), seed=42, N=20, T=4
- **Metrics (base):**
  - gar_ours_mean: 0.0088, gar_ours_std: 0.0056
  - gar_ours_median_per_conv: 0.0093
  - gar_ours_median_per_turn_pool: 0.0071
  - gar_ours_spike_ratio: "0%"
  - gar_dongre_mean: 0.0049, gar_dongre_std: 0.0013, gar_dongre_median: 0.0047
  - ngar_ours_mid: 0.1019, ngar_dongre_mid: 0.1171
  - ppl: 1.293, ppl_std: 0.07, ntp_loss: 0.2552
- **Metrics (tg):**
  - gar_ours_mean: 0.0434, gar_ours_std: 0.1002
  - gar_ours_median_per_conv: 0.0179
  - gar_ours_median_per_turn_pool: 0.0126
  - gar_ours_spike_ratio: "5% (2/40 turns GAR>=0.4)"
  - gar_dongre_mean: 0.0183, gar_dongre_std: 0.0198, gar_dongre_median: 0.0152
  - ngar_ours_mid: 0.5357, ngar_dongre_mid: 0.4436
  - ppl: 1.437, ppl_std: 0.077, ntp_loss: 0.3612
- **Metrics (lora_only):**
  - gar_ours_mean: 0.0284, gar_ours_std: 0.0481
  - gar_ours_median_per_conv: 0.0184
  - gar_ours_median_per_turn_pool: 0.0133
  - gar_ours_spike_ratio: "0%"
  - gar_dongre_mean: 0.0205, gar_dongre_std: 0.0241, gar_dongre_median: 0.016
  - ngar_ours_mid: 0.3488, ngar_dongre_mid: 0.4997
  - ppl: 1.419, ppl_std: 0.075, ntp_loss: 0.3483
- n_conversations: 20, n_turns: 4
- Rankings: TG(0.0434) > LO(0.0284) > Base(0.0088) [mean]; TG(0.0179) ~= LO(0.0184) > Base(0.0093) [median_per_conv]

### 17. eval_llama_lora_only_s42
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct + LoRA-only, seed=42
- **Metrics (TF):**
  - gar_ours: 0.4807, gar_dongre: 0.0188
  - ngar_ours: 11.8031, ngar_dongre: 0.8261
  - ppl: 2.6, ntp_loss: 0.9366
  - N=50, T=4
- **Metrics (AR):**
  - gar_ours: 0.0617, gar_dongre: 0.0226
  - ngar_ours: 0.6065, ngar_dongre: 0.2537
  - ppl: 1.32, ntp_loss: 0.2787
  - N=5, T=10
- gap_ratio_gar_ours: 7.79

### 18. eval_v7_tg_s123
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=123
- **Metrics (iid_tf):**
  - gar_ours_mid: 0.5052, gar_dongre_mid: 0.0119
  - ppl: 2.7802, ntp: 0.9752
- **Metrics (modelgen_ar):**
  - gar_ours_mid: 0.0165, gar_dongre_mid: 0.0177
  - ppl: 1.3855, ntp: 0.3223
- gap_ratio: 30.6
- comparison_s42: tf_gar_ours_delta=0.0017, ar_gar_ours_delta=0.0008, gap_ratio_delta=-1.4

### 19. eval_v8b_ss
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, checkpoint=tg_v8b_ss_fixed_s42
- **Metrics:**
  - iid_gar_ours: 0.4983, iid_gar_dongre: 0.3855, iid_ppl: 2.78
  - iid_ngar_ours: 13.5, iid_ngar_dongre: 22.68
  - modelgen_gar_ours: 0.3177, modelgen_gar_dongre: 0.3533, modelgen_ppl: 1.38
  - modelgen_ngar_ours: 4.47, modelgen_ngar_dongre: 5.92
  - iid_turn1_gar_ours: 0.5398
  - modelgen_turn1_gar_ours: 0.4333

### 20. eval_v8b_ss_s123
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=123
- **Metrics (iid):**
  - gar_ours: 0.503, gar_dongre: 0.394
  - ppl: 2.781, ntp_loss: 0.976
  - n_conv: 50, n_turns: 3
- **Metrics (modelgen):**
  - gar_ours: 0.418, gar_dongre: 0.441
  - ppl: 1.389, ntp_loss: 0.325
  - n_conv: 5, n_turns: 10
- gap_ratio: 1.2
- base_iid_ppl: 4.338, base_modelgen_ppl: 1.351

### 21. instruction_retention_test
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct + v7 TG LoRA, seed=42, 18 prompts, beta=[0,3], 5 turns each
- **Metrics:**
  - late_turn_rate_beta0: 0.759
  - late_turn_rate_beta3: 0.87
  - late_turn_delta: 0.111
  - mcnemar_chi2: 3.125
  - mcnemar_p: 0.0771
  - gar_compliance_r: 0.2003
  - gar_compliance_p: 0.007
  - category_content_constraint: beta0=0.619, beta3=0.857, delta=0.238
  - category_count_constraint: beta0=1, beta3=1, delta=0
  - category_format_constraint: beta0=1, beta3=1, delta=0
  - category_position_constraint: beta0=0.667, beta3=0.733, delta=0.067

### 22. llama_ar_matched_eval
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct + TG LoRA, seed=42, N=50, T=4
- **Metrics:**
  - ar_base_ours: mid_gar=0.0082, ngar=0.1, ppl=1.267
  - ar_tg_ours: mid_gar=0.0388, ngar=0.493, ppl=1.413
  - ar_base_dongre: mid_gar=0.0051, ngar=0.12, ppl=1.267
  - ar_tg_dongre: mid_gar=0.018, ngar=0.431, ppl=1.413
  - tf_reference: tf_tg_ours_ngar=11.88, tf_base_ours_ngar=0.388, tf_tg_ours_raw=0.4836, tf_tg_dongre_raw=0.018
  - Matched gap: gar_ours_raw_gap="12.5x (TF 0.484 / AR 0.039)", gar_ours_ngar_gap="24.1x", gar_dongre_raw_gap="1.002x (zero gap)"
  - tg_over_base_ar_ours: "4.71x", tg_over_base_ar_dongre: "3.54x"

### 23. llama_eval_s42
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct, seed=42
- **Metrics (tf_base):** gar_ours=0.0166, ngar_ours=0.3882, gar_dongre=0.0038, ngar_dongre=0.163, ppl=3.45, N=50, T=4
- **Metrics (tf_tg):** gar_ours=0.4836, ngar_ours=11.8818, gar_dongre=0.018, ngar_dongre=0.7922, ppl=2.57, N=50, T=4
- **Metrics (ar_base):** gar_ours=0.0086, ngar_ours=0.0798, gar_dongre=0.0118, ngar_dongre=0.1265, ppl=1.24, N=5, T=10
- **Metrics (ar_tg):** gar_ours=0.0304, ngar_ours=0.2632, gar_dongre=0.0217, ngar_dongre=0.2459, ppl=1.32, N=5, T=10
- gap_ratio_tg_ours: 15.9
- gap_ratio_base_ours: 1.93
- gap_ratio_tg_dongre: 0.83
- vs_qwen_v7_gap_ratio: 32.1
- baseline_mid_gar: 0.0122

### 24. llama_lora_only_s42 (training)
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct, seed=42, data=8000, epochs=3
- **Metrics:**
  - final_avg_loss: 0.9288, final_avg_ntp: 0.9279, final_avg_gar: 0.0009
  - gate_fixed: 1, gate_type: "none"
  - wall_clock_s: 25317, wall_clock_h: 7.03
  - epochs_completed: 3

### 25. llama_phase1_gar_diag
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct, seed=42, 5 convs x 10 turns, gen mode
- **Metrics:**
  - per_turn_gar: turn_1=0.0263, turn_2=0.0183, turn_3=0.0087, turn_4=0.0055, turn_5=0.006, turn_6=0.0035, turn_7=0.0038, turn_8=0.0037, turn_9=0.005, turn_10=0.0026
  - t1_t10_decay_pct: 90.1
  - t1_mid38_drop_pct: 80.2

### 26. llama_tg_s42 (training)
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct, seed=42, data=8000, epochs=3, lr=2e-4, batch_size=1, grad_accum=8
- **Metrics:**
  - epochs_completed: 3, total_steps: 3000
  - wall_clock_seconds: 26212, wall_clock_hours: 7.28
  - final_avg_loss: 0.9233, final_avg_ntp: 0.9224, final_avg_gar: 0.0009, final_avg_div: 0
  - final_gate_mean: 0.9099, final_gate_std: 0.0701
  - final_gate_min: 0.7188, final_gate_max: 0.9922
  - **Gate profile (32 layers):** L0=0.957, L1=0.973, L2=0.977, L3=0.965, L4=0.992, L5=0.969, L6=0.957, L7=0.957, L8=0.961, L9=0.949, L10=0.938, L11=0.934, L12=0.969, L13=0.953, L14=0.957, L15=0.965, L16=0.953, L17=0.961, L18=0.922, L19=0.902, L20=0.883, L21=0.863, L22=0.836, L23=0.844, L24=0.809, L25=0.719, L26=0.762, L27=0.805, L28=0.801, L29=0.855, L30=0.898, L31=0.934
  - checkpoint_size_gate_mb: 4.2, checkpoint_size_lora_mb: 26
  - GPU: NVIDIA RTX PRO 6000 Blackwell, vram_gb: 102, mem_used_gb: 63.4

### 27. llama_tg_training
- **Status:** PREPARING | **Conclusion:** failed
- **Metrics:** NONE (phantom duplicate of llama_tg_s42)

### 28. mmlu_eval_all
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, MMLU 5-shot, 14042 examples
- **Metrics (MMLU scores):**
  - base_qwen: 0.7423
  - pcgrad_v9_s42: 0.7386
  - ss_v8b_s42: 0.7375
  - lo_s42: 0.7357
  - tg_v7_s42: 0.7347
  - ug_s42: 0.7346

### 29. p0_ss_steering_eval
- **Status:** PREPARING | **Conclusion:** killed
- **Metrics:** NONE (cancelled, existing data sufficient)

### 30. p1_llama_ss_eval
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct, seed=42, N=50, checkpoint=p1_llama_ss_s42/epoch_1
- **Metrics:**
  - ss_tf_gar: 0.477
  - ss_tf_ppl: 2.82
  - ss_ar_b0_gar: 0.1662
  - ss_ar_b0_ppl: 1.37
  - ss_ar_b5_gar: 0.7905
  - ss_ar_b5_ppl: 1.81
  - base_ar_gar: 0.0179
  - base_ar_ppl: 1.22
  - tf_ar_gap: 2.87

### 31. p1_llama_ss_training
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct, seed=42, data=400, lr=2e-4, batch_size=1, grad_accum=8, epochs=3, ss_max_ratio=0.3, lora_rank=16
- **Metrics:** NONE (training only)

### 32. p1_ss_lora_only
- **Status:** DONE | **Conclusion:** killed
- **Spec:** Qwen2.5-7B-Instruct, seed=42, data=2000, ss_max_ratio=0.3, gate_type=none
- **Metrics:** NONE

### 33. p1_tf_ar_kl_divergence
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, 30 convs
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

### 34. p2_llama_gradient_conflict
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct, seed=42, data=400
- **Metrics:**
  - cos_sim_mean: 0.0045
  - cos_sim_std: 0.07
  - neg_cos_sim_layers_pct: 53.1
  - mag_ratio_median: 25.7

### 35. phase1_gar_diag
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, 5 convs x 10 turns
- **Metrics:**
  - turn1_avg_gar: 0.0418
  - mid_turns_avg_gar: 0.0122
  - relative_drop: 0.708
  - per_turn_avg_gar: [0.0418, 0.0241, 0.0224, 0.013, 0.0133, 0.0086, 0.0078, 0.008, 0.0157, 0.0064]

### 36. phase1a_multiseed_8runs
- **Status:** PREPARING | **Conclusion:** None
- **Metrics:** NONE

### 37. phase1a_multiseed_qwen
- **Status:** DONE | **Conclusion:** killed (30min timeout)
- **Metrics:** NONE

### 38. phase1b_llama_complement
- **Status:** PREPARING | **Conclusion:** None
- **Metrics:** NONE

### 39. phase2_4way_eval
- **Status:** DONE | **Conclusion:** negative
- **Spec:** Qwen2.5-7B-Instruct, seed=42, training split eval
- **Metrics:**
  - base_ours_mid_gar: 0.0107, base_ours_recovery_pp: -0.15
  - base_dongre_mid_gar: 0.003, base_dongre_recovery_pp: -0.92
  - base_ppl: 4.23, base_ntp: 1.4162
  - tg_ours_mid_gar: 0.4866, tg_ours_recovery_pp: 47.44
  - tg_dongre_mid_gar: 0.0157, tg_dongre_recovery_pp: 0.35
  - tg_ppl: 2.63, tg_ntp: 0.9484
  - ug_ours_mid_gar: 0.4923, ug_ours_recovery_pp: 48.01
  - ug_dongre_mid_gar: 0.013, ug_dongre_recovery_pp: 0.08
  - ug_ppl: 2.62, ug_ntp: 0.9433
  - lora_ours_mid_gar: 0.486, lora_ours_recovery_pp: 47.39
  - lora_dongre_mid_gar: 0.0137, lora_dongre_recovery_pp: 0.15
  - lora_ppl: 2.63, lora_ntp: 0.9482
  - route_b_confirmed: true, gating_incremental_benefit: "none"

### 40. phase2_4way_eval_heldout
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, held-out eval (50 convs, idx 8843-68199)
- **Metrics:**
  - base_ours_mid_gar: 0.0128, base_ours_recovery_pp: 0.06
  - base_dongre_mid_gar: 0.0031, base_dongre_recovery_pp: -0.91
  - base_ppl: 4.34, base_ntp: 1.4045
  - tg_ours_mid_gar: 0.5035, tg_ours_recovery_pp: 49.13
  - tg_dongre_mid_gar: 0.0152, tg_dongre_recovery_pp: 0.3
  - tg_ppl: 2.78, tg_ntp: 0.9771
  - ug_ours_mid_gar: 0.5053, ug_ours_recovery_pp: 49.31
  - ug_dongre_mid_gar: 0.0124, ug_dongre_recovery_pp: 0.02
  - ug_ppl: 2.78, ug_ntp: 0.9752
  - lora_ours_mid_gar: 0.4978, lora_ours_recovery_pp: 48.56
  - lora_dongre_mid_gar: 0.0132, lora_dongre_recovery_pp: 0.1
  - lora_ppl: 2.78, lora_ntp: 0.9771
  - three_way_convergence_confirmed: true
  - gar_ours_spread_pp: 0.75, ppl_spread: 0, data_overlap: false

### 41. phase2_lora_only_s42
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, data=8000, epochs=3, gate_type=none
- **Metrics:**
  - epochs_completed: 3, global_steps: 3000
  - training_time_seconds: 20588.6, training_time_hours: 5.7
  - gate_fixed: 1, gate_type_actual: "none"
  - final_lora_size_mb: 20
  - eval_modelgen_ours_mid_gar: 0.0245
  - eval_modelgen_dongre_mid_gar: 0.0185
  - eval_modelgen_ppl: 1.371

### 42. phase2_switching
- **Status:** DONE | **Conclusion:** killed
- **Metrics:** NONE

### 43. phase2_tf_ar_switching
- **Status:** QUEUED | **Conclusion:** None
- **Metrics:** NONE

### 44. phase2_tg_s42 (v1)
- **Status:** DONE | **Conclusion:** negative
- **Spec:** Qwen2.5-7B-Instruct, seed=42, data=8000
- **Metrics:**
  - final_ntp_loss: 0.94
  - final_gar_loss: 0
  - gate_mean: 0.988
  - gar_loss_zero_pct: 87.6
  - epochs_completed: 1.67
  - killed_reason: "SIGTERM by diagnose worker (unauthorized)"

### 45. phase2_tg_s42_v2
- **Status:** DONE | **Conclusion:** killed
- **Spec:** Qwen2.5-7B-Instruct, seed=42, gar_loss_mode=cumulative, gar_epsilon=0.001, init_bias=2.0, lambda_gar=5.0
- **Metrics:** NONE

### 46. phase2_tg_s42_v3
- **Status:** DONE | **Conclusion:** negative
- **Spec:** Qwen2.5-7B-Instruct, seed=42, gar_loss_mode=maximize, lambda_gar=2.0, init_bias=2.0
- **Metrics:**
  - gate_mean_step0: 0.8743, gate_mean_step500: 0.8761
  - gate_delta: 0.004, gate_std: 0.001
  - final_ntp_loss: 0.94, final_gar_loss: -0.019
  - gar_contribution_pct: "2-4%"
  - diagnosis: "gate frozen, GAR indirect gradient too weak"

### 47. phase2_tg_s42_v3b
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, lambda_gar=10.0, init_bias=0.0, gate_lr_multiplier=10, max_steps=500
- **Metrics:**
  - gate_std_final: 0.087
  - gate_mean_final: 0.9388
  - gate_min_final: 0.5352
  - gate_max_final: 0.9922
  - L4_gate: 0.535, L0_gate: 0.777
  - L_NTP_final: 0.7787, L_GAR_final: -0.9606
  - elapsed_seconds: 3565.9, optimizer_steps: 500
  - gate_grad_received: true

### 48. phase2_tg_s42_v4
- **Status:** DONE | **Conclusion:** failed (server crash)
- **Metrics:** NONE

### 49. phase2_tg_s42_v5
- **Status:** DONE | **Conclusion:** negative
- **Spec:** Qwen2.5-7B-Instruct, seed=42, gar_loss_mode=maximize, lambda_gar=1.0, init_bias=1.5, gate_lr_multiplier=10, epochs=3
- **Metrics:**
  - step2000_gate_std: 0.0225, step2000_gate_mean: 0.9586
  - step2000_gate_min: 0.9062, step2000_gate_max: 0.9961
  - step2000_L_GAR: -0.8977, step2000_L_NTP: 0.7611, step2000_total_loss: -0.1365
  - step2400_gate_std: 0.0219, step2400_gate_mean: 0.9651
  - step2400_gate_min: 0.918, step2400_gate_max: 0.9961
  - step2400_profile: "L0=0.918 L12=0.918 L13=0.926 L1=0.996 L26=0.996"
  - L_GAR_saturated_at: -0.91
  - gate_range_compression: "0.918-0.996"

### 50. phase2_tg_s42_v6
- **Status:** DONE | **Conclusion:** negative
- **Spec:** Qwen2.5-7B-Instruct, seed=42, gar_loss_mode=smooth_saturation, gar_target=0.5, lambda_gar=1.0, init_bias=1.5, gate_lr_multiplier=10, epochs=3
- **Metrics:**
  - dryrun_step0: L_NTP=2.0275, L_GAR=-0.0161, total_loss=2.0114
  - dryrun_step4: L_NTP=1.6544, L_GAR=-0.0147, total_loss=1.6397
  - dryrun_gate_mean_init: 0.8097, dryrun_gate_std_init: 0.0341
  - dryrun_gate_min_init: 0.6836, dryrun_gate_max_init: 0.8672
  - dryrun_gate_mean_step5: 0.8025, dryrun_gate_std_step5: 0.0842
  - dryrun_gate_min_step5: 0.5547, dryrun_gate_max_step5: 0.9805
  - gs50: gate_mean=0.8117, gate_std=0.0612, gate_min=0.6836, gate_max=0.9805
  - gs100: gate_mean=0.8737, gate_std=0.0367, gate_min=0.8164, gate_max=0.9766
  - gs100: L_NTP=0.8151, L_GAR=-0.158, total_loss=0.6571
  - gs100_profile_bottom3: "L12=0.816 L4=0.824 L13=0.824"
  - gs100_profile_top3: "L27=0.977 L26=0.961 L23=0.914"
  - gs143_L_GAR: -0.3876, gs143_gate_mean: 0.9227

### 51. phase2_tg_s42_v7 (canonical)
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, gar_loss_mode=mse_target, gar_target=0.5, lambda_gar=1.0, lambda_gate_div=1.0, min_gate_std=0.05, init_bias=1.5, gate_lr_multiplier=10, epochs=3, data=8000
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
  - gate_mean_final: 0.9336
  - gate_std_final: 0.0492

### 52. phase2_tg_s42_v8_schedsampling
- **Status:** DONE | **Conclusion:** failed
- **Spec:** Qwen2.5-7B-Instruct, seed=42, ss_max_ratio=0.5, lr=2e-4, epochs=3
- **Metrics:**
  - killed_at_microstep: 1950, total_microsteps: 24000, completion_pct: 8.1
  - global_step_approx: 244, total_global_steps: 3000
  - ss_steps_observed: 1
  - tf_lgar_mean_step850_1400: 0.0062, tf_lgar_std: 0.0082, tf_lgar_collapse_step: 800
  - gate_mean_final: 0.93
  - ss_ratio_at_kill: 0.081

### 53. phase2_tg_s42_v8b_resume
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, ss_max_ratio=0.5, epochs=3
- **Metrics (training):**
  - total_steps: 3000, epochs_completed: 3, wall_clock_hours: 8.1
  - final_loss: 0.933, final_ntp_loss: 0.9322, final_gar_loss: 0.0008
  - final_gate_mean: 0.9586, final_gate_std: 0.0582, ss_ratio: 0.5
- **Metrics (eval_iid):**
  - gar_ours: 0.4983, gar_dongre: 0.3855, ppl: 2.78
- **Metrics (eval_modelgen):**
  - gar_ours: 0.3177, gar_dongre: 0.3533, ppl: 1.38
- **vs_v7:**
  - iid_gar_ours_delta: -0.005
  - modelgen_gar_ours_delta: 0.302
  - gap_ratio_v7: 32, gap_ratio_v8b: 1.57

### 54. phase2_tg_s42_v8b_ss_fixed
- **Status:** DONE | **Conclusion:** failed (CUDA OOM at epoch 1 step 4300)
- **Metrics:** NONE (has epoch_0 checkpoint)

### 55. phase2_tg_s42_v9_pcgrad
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, PCGrad, same hyperparams as v7
- **Metrics:**
  - eval_iid_ours_mid_gar: 0.5002
  - eval_iid_dongre_mid_gar: 0.0123
  - eval_iid_ppl: 2.78
  - eval_iid_ntp: 0.9752
  - eval_heldout_ours_mid_gar: 0.5002
  - eval_heldout_dongre_mid_gar: 0.0123
  - eval_heldout_ppl: 2.78
  - eval_heldout_ntp: 0.9752
  - eval_modelgen_ours_mid_gar: 0.0151
  - eval_modelgen_dongre_mid_gar: 0.0173
  - eval_modelgen_ppl: 1.5
  - vs_v7_iid_ppl_diff: 0.004
  - vs_v7_iid_gar_diff: -0.0033

### 56. phase2_ug_s42
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, gate_type=uniform, data=8000, epochs=3
- **Metrics:**
  - epoch0: avg_loss=1.0019, avg_ntp=0.9755, avg_gar=0.0259, avg_div=0.0005
  - epoch1: avg_loss=0.9447, avg_ntp=0.9435, avg_gar=0.0013, avg_div=0
  - epoch2: avg_loss=0.9319, avg_ntp=0.9309, avg_gar=0.001, avg_div=0
  - final_gate_mean: 0.9598, final_gate_std: 0.0518
  - final_gate_min: 0.7773, final_gate_max: 1
  - final_profile: L3=0.777, L5=0.812, L0=0.875, L27=1
  - training_time_seconds: 21994.5, training_time_hours: 6.1, global_steps: 7950
  - unexpected_per_layer_variation: true
  - eval_modelgen_ours_mid_gar: 0.0149
  - eval_modelgen_dongre_mid_gar: 0.0185
  - eval_modelgen_ppl: 1.396

### 57. qwen15b_phase1_diag
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-1.5B-Instruct, seed=42, data=400, epochs=3
- **Metrics:** NONE (registered without metrics)

### 58. trc_baseline_v7_tg
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, 5 convs x 10 turns
- **Metrics (v7_tg):**
  - tf_trc: 0.3339, gen_trc: 0.3323, trc_gap: 0.0016
  - tf_tbp_ppl: 1.05, gen_tbp_ppl: 1.05
- **Metrics (lora_only):**
  - tf_trc: 0.349, gen_trc: 0.4106, trc_gap: -0.0617
  - tf_tbp_ppl: 9.5, gen_tbp_ppl: 12
- **Metrics (base):**
  - tf_trc: 0.1494, gen_trc: 0.1494, trc_gap: 0
  - tf_tbp_ppl: 2.05, gen_tbp_ppl: 2.05

### 59. v7_tg_s123 (training)
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=123, data=8000
- **Metrics:**
  - epoch_1: avg_loss=0.9447, avg_ntp_loss=0.9434, avg_gar_loss=0.0013, avg_div_loss=0
  - epoch_2: avg_loss=0.9315, avg_ntp_loss=0.9305, avg_gar_loss=0.001, avg_div_loss=0
  - final_gate: mean=0.9467, std=0.051, min=0.793, max=1
  - **Gate profile (28 layers):** L0=0.883, L1=0.793, L2=0.996, L3=0.988, L4=0.984, L5=0.797, L6=0.961, L7=0.918, L8=0.965, L9=0.934, L10=0.969, L11=0.918, L12=0.926, L13=0.941, L14=0.93, L15=0.965, L16=0.941, L17=0.91, L18=0.961, L19=0.965, L20=0.973, L21=0.988, L22=0.969, L23=0.98, L24=0.98, L25=0.984, L26=0.988, L27=1
  - training_time_s: 21425.2

### 60. v8b_ss_s123 (training)
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=123, data=8000
- **Metrics:**
  - final_loss: 0.9316, final_ntp_loss: 0.9307, final_gar_loss: 0.0009
  - final_gate_mean: 0.9505, final_gate_std: 0.0508
  - final_gate_min: 0.7383, final_gate_max: 1
  - ss_used_ratio: 0.371
  - training_time_s: 38773.4
  - epoch0_loss: 1.0092, epoch1_loss: 0.9444, epoch2_loss: 0.9316

---

## SUMMARY STATISTICS

- **Total experiments:** 60
- **With metrics:** 42
- **Without metrics:** 18 (7 failed/killed, 5 training-only with evals elsewhere, 4 PREPARING/QUEUED, 2 killed by user)
- **Successful with metrics:** 35
- **Key gap ratios:** v7 TG s42=32x, v7 TG s123=30.6x, v8b SS s42=1.57x, v8b SS s123=1.2x, d048 SS s42=1.29x, Llama TG=15.9x (raw)/12.5x (matched), Llama SS=2.87x, Llama LoRA-only=7.79x
- **MMLU retention:** All within 0.77pp of base (0.7423), confirming no general capability degradation
- **TRC values:** v7_tg tf=0.3339, gen=0.3323 (gap=0.0016); lora_only tf=0.349, gen=0.4106 (gap=-0.0617); base tf/gen=0.1494 (gap=0)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7229ac90-6be9-43e1-b180-48bba20e5bb1",
  "isSidechain": true,
  "agentId": "a24bf7311cd045b90",
  "requestId": "req_011CbPu8mVkDsqFFKoR4VdBd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d867637-40bb-450a-be3b-465c1265ac53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TypJx1dgJ9fP6ku2TsJpim",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 898,
      "cache_read_input_tokens": 77295,
      "output_tokens": 13889,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 898
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13889,
          "cache_read_input_tokens": 77295,
          "cache_creation_input_tokens": 898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 898,
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
