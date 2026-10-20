# Research conversation: I need to extract specific experiment metrics from a large registry JSON file. The file is at: /home/ubuntu/.claude-acco

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aac69cde3cdf76252.jsonl`
- **Structured JSON:** [`3772f0d5c3a83e970c87.json`](../../sessions/37/3772f0d5c3a83e970c87.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-23T06:19:27.242Z_

I need to extract specific experiment metrics from a large registry JSON file. The file is at:
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/88c2d600-443d-4934-bc0d-a18a29f467ab/tool-results/mcp-agent-ml-research-read_registry-1779517155962.txt

The file is JSON with schema: {result: string} — the `result` field is itself a JSON string that needs to be parsed.

I need you to extract metrics for these experiments:
1. All experiments matching pattern `scale_14b_t15_*` (1.4B model, T=15 experiments)
2. The experiment `a075_s42_fp32` or similar (410M T=15 α=0.75)

For each, I need:
- exp_id
- status, conclusion
- metrics (especially: perm_granger_fdr_forward_sig, perm_granger_fdr_reverse_sig, robust_pairs_K3, robust_pairs_K4, threshold_forward_sig, diff_xcorr_fdr_forward_sig, ty_forward_sig, drift_ppl_pct)

Use jq or python to parse. Report the results in a clean table format. Be thorough — check for exp_ids containing "14b" and "t15", and also look for 410M a075 experiments (they might not have "410m" in the name, check for "a075" pattern).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3b6d09a4-9413-4727-a60f-bea5795efd1e",
  "agentId": "aac69cde3cdf76252",
  "type": "user",
  "uuid": "a2bc21bc-859e-4bad-813d-23c26af5d0a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-23T06:19:27.246Z_

```json
{
  "parentUuid": "a2bc21bc-859e-4bad-813d-23c26af5d0a4",
  "isSidechain": true,
  "agentId": "aac69cde3cdf76252",
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
  "uuid": "25d0ad41-dcf3-4c76-bcbb-d0741acb5a4e",
  "timestamp": "2026-05-23T06:19:27.246Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-23T06:19:29.691Z_



Let me start by reading the file to understand its structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25d0ad41-dcf3-4c76-bcbb-d0741acb5a4e",
  "isSidechain": true,
  "agentId": "aac69cde3cdf76252",
  "requestId": "req_011CbK1rT9YAyLQCyVbtFGzQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ebc801e-5ef9-4c28-b56a-062d3c68c383",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0143RxWJxvu7MzNWibF6mvpD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16274,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16274,
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

_source line 4 · 2026-05-23T06:19:30.362Z_

<details open><summary>🔧 Tool call — Read · `toolu_01REQiwRL9j9s7pCdb72471E`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/88c2d600-443d-4934-bc0d-a18a29f467ab/tool-results/mcp-agent-ml-research-read_registry-1779517155962.txt",
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ebc801e-5ef9-4c28-b56a-062d3c68c383",
  "isSidechain": true,
  "agentId": "aac69cde3cdf76252",
  "requestId": "req_011CbK1rT9YAyLQCyVbtFGzQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0078973f-f8c0-422d-b24d-9ca43145ffdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0143RxWJxvu7MzNWibF6mvpD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16274,
      "cache_read_input_tokens": 0,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16274
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 173,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16274,
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

_source line 5 · 2026-05-23T06:19:30.643Z_

<details><summary>↩ Tool result · reported error · `toolu_01REQiwRL9j9s7pCdb72471E`</summary>

```text
File content (75647 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0078973f-f8c0-422d-b24d-9ca43145ffdf",
  "isSidechain": true,
  "promptId": "3b6d09a4-9413-4727-a60f-bea5795efd1e",
  "agentId": "aac69cde3cdf76252",
  "type": "user",
  "uuid": "9a14440d-1c58-4e77-ad7f-efe0778d2649",
  "toolUseResult": "Error: File content (75647 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "0078973f-f8c0-422d-b24d-9ca43145ffdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-23T06:19:33.079Z_

The file is too large to read at once. Let me use Python to parse it and extract the needed experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a14440d-1c58-4e77-ad7f-efe0778d2649",
  "isSidechain": true,
  "agentId": "aac69cde3cdf76252",
  "requestId": "req_011CbK1rhguJgHgHYQVPHrF6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ae169e3-e846-44da-a612-da991a9544cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Puf6kbViofdzAybhMCRMxa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1075,
      "cache_read_input_tokens": 16274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1075,
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

_source line 7 · 2026-05-23T06:19:37.760Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VURM9AfGC6ZURXRTEmQX6r`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/88c2d600-443d-4934-bc0d-a18a29f467ab/tool-results && python3 -c \"\nimport json\n\nwith open('mcp-agent-ml-research-read_registry-1779517155962.txt', 'r') as f:\n    outer = json.load(f)\n\ndata = json.loads(outer['result'])\n\n# Check what type data is\nprint('Type:', type(data))\nif isinstance(data, dict):\n    print('Top-level keys:', list(data.keys())[:20])\nelif isinstance(data, list):\n    print('Length:', len(data))\n    if len(data) > 0:\n        print('First item keys:', list(data[0].keys()) if isinstance(data[0], dict) else type(data[0]))\n\"\n",
  "description": "Parse the registry JSON to understand its structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ae169e3-e846-44da-a612-da991a9544cf",
  "isSidechain": true,
  "agentId": "aac69cde3cdf76252",
  "requestId": "req_011CbK1rhguJgHgHYQVPHrF6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "856abbc3-176a-4619-acbb-b48493d7c4f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Puf6kbViofdzAybhMCRMxa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1075,
      "cache_read_input_tokens": 16274,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1075
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 338,
          "cache_read_input_tokens": 16274,
          "cache_creation_input_tokens": 1075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1075,
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

_source line 8 · 2026-05-23T06:19:37.966Z_

<details><summary>↩ Tool result · `toolu_01VURM9AfGC6ZURXRTEmQX6r`</summary>

```text
Type: &lt;class 'dict'>
Top-level keys: ['success', 'data', 'error', 'metadata']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "856abbc3-176a-4619-acbb-b48493d7c4f6",
  "isSidechain": true,
  "promptId": "3b6d09a4-9413-4727-a60f-bea5795efd1e",
  "agentId": "aac69cde3cdf76252",
  "type": "user",
  "uuid": "5048394b-53a4-47f6-8bee-4478ba49a2ae",
  "sourceToolAssistantUUID": "856abbc3-176a-4619-acbb-b48493d7c4f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T06:19:42.562Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KVCriyd3jBHeSDiDvQ6pTe`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/88c2d600-443d-4934-bc0d-a18a29f467ab/tool-results && python3 -c \"\nimport json\n\nwith open('mcp-agent-ml-research-read_registry-1779517155962.txt', 'r') as f:\n    outer = json.load(f)\n\ndata = json.loads(outer['result'])\nentries = data['data']\nprint('Type of data:', type(entries))\nif isinstance(entries, list):\n    print('Number of entries:', len(entries))\n    if len(entries) > 0:\n        print('First entry keys:', list(entries[0].keys()))\nelif isinstance(entries, dict):\n    print('Keys:', list(entries.keys())[:30])\n\"\n",
  "description": "Inspect the data field structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5048394b-53a4-47f6-8bee-4478ba49a2ae",
  "isSidechain": true,
  "agentId": "aac69cde3cdf76252",
  "requestId": "req_011CbK1sF2JzVt7kkApQA3Ed",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75d16d96-b4df-4223-976a-f6a659566e55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012V5n6TaEjcDfk3CxzEeEm2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 379,
      "cache_read_input_tokens": 17349,
      "output_tokens": 297,
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
          "input_tokens": 1,
          "output_tokens": 297,
          "cache_read_input_tokens": 17349,
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
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T06:19:42.676Z_

<details><summary>↩ Tool result · `toolu_01KVCriyd3jBHeSDiDvQ6pTe`</summary>

```text
Type of data: &lt;class 'dict'>
Keys: ['experiments', 'count', 'total', 'baseline']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75d16d96-b4df-4223-976a-f6a659566e55",
  "isSidechain": true,
  "promptId": "3b6d09a4-9413-4727-a60f-bea5795efd1e",
  "agentId": "aac69cde3cdf76252",
  "type": "user",
  "uuid": "d1d56935-48bd-486b-8eab-6d9924bb3051",
  "sourceToolAssistantUUID": "75d16d96-b4df-4223-976a-f6a659566e55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T06:19:47.730Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Mq7XCXJMd8X3hSp9X2ba4C`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/88c2d600-443d-4934-bc0d-a18a29f467ab/tool-results && python3 -c \"\nimport json\n\nwith open('mcp-agent-ml-research-read_registry-1779517155962.txt', 'r') as f:\n    outer = json.load(f)\n\ndata = json.loads(outer['result'])\nexperiments = data['data']['experiments']\nprint('Type:', type(experiments))\nif isinstance(experiments, list):\n    print('Count:', len(experiments))\n    # Print all exp_ids\n    for e in experiments:\n        eid = e.get('exp_id', 'N/A')\n        print(f'  {eid}')\nelif isinstance(experiments, dict):\n    print('Experiment IDs:')\n    for k in experiments.keys():\n        print(f'  {k}')\n\"\n",
  "description": "List all experiment IDs in the registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1d56935-48bd-486b-8eab-6d9924bb3051",
  "isSidechain": true,
  "agentId": "aac69cde3cdf76252",
  "requestId": "req_011CbK1sbAGdMXSsHG5Nfc6y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "347acdfc-0084-42eb-bc10-25caeffd9726",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZNwkZfz6Xj8iRNbGXKiWY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 337,
      "cache_read_input_tokens": 17728,
      "output_tokens": 331,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 337
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 331,
          "cache_read_input_tokens": 17728,
          "cache_creation_input_tokens": 337,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 337,
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

_source line 12 · 2026-05-23T06:19:47.822Z_

<details><summary>↩ Tool result · `toolu_01Mq7XCXJMd8X3hSp9X2ba4C`</summary>

```text
Type: &lt;class 'dict'>
Experiment IDs:
  scale_14b_t15_a075_s42_fp32
  scale_14b_t15_a045_s43_fp32
  scale_14b_t15_a045_s42_fp32
  scale_14b_t15_a050_s42_fp32_v3
  scale_14b_t15_a060_s42_fp32_v2
  scale_14b_t15_a060_s43_fp32
  scale_14b_t15_a050_s43_fp32
  scale_14b_t10_a045_s42_fp32
  scale_14b_t10_a045_s43_fp32
  phase_diagram_t10_a050_s44_fp32
  scale_14b_t10_a050_s43_fp32
  scale_14b_t10_a060_s43_fp32
  scale_14b_t10_a075_s43_fp32
  scale_14b_t10_a050_s42_fp32_v2
  14b_t10_a060_s43
  14b_t10_a075_s43
  14b_t10_a050_s43
  scale_14b_t10_a075_s42_fp32_v2
  scale_14b_t10_a060_s42_fp32_v2
  phase_diagram_t20_a075_s43_fp32
  phase_diagram_t25_a075_s43_fp32_v3
  scale_14b_t15_a050_s42_fp32
  phase_diagram_t25_a045_s43_fp32
  scale_14b_t15_a060_s42_fp32
  scale_14b_t10_a050_s42_fp32_19828
  scale_14b_t10_a075_s42_fp32
  scale_14b_t10_a060_s42_fp32
  phase_diagram_t25_a050_s42_fp32_v3
  phase_diagram_t25_a060_s42_fp32_v3
  phase_diagram_t10_a075_s43_fp32
  phase_diagram_t10_a050_s43_fp32_v2
  phase_diagram_t15_a075_s43_fp32
  scale_14b_t10_a050_s42_fp32
  phase_diagram_t25_a075_s43_fp32_v2
  phase_diagram_t10_a050_s43_fp32
  phase_diagram_t25_a075_s43_fp32
  phase_diagram_t20_a060_s43_fp32_v2
  phase_diagram_t20_a045_s43_fp32
  phase_diagram_t15_a045_s43_fp32
  phase_diagram_t25_a045_s42_fp32_v2
  phase_diagram_t15_a060_s43_fp32
  phase_diagram_t25_a060_s42_fp32_v2
  phase_diagram_t25_a050_s42_fp32_v2
  phase_diagram_t25_a075_s42_fp32
  alpha_sweep_a000_s48_fp32
  scale_69b_a100_s43_bf16
  phase_diagram_t15_a075_s42_fp32
  phase_diagram_t15_a060_s42_fp32
  phase_diagram_t15_a050_s42_fp32
  phase_diagram_t15_a045_s42_fp32
  phase_diagram_t05_a075_s42_fp32
  phase_diagram_t05_a060_s42_fp32
  phase_diagram_t20_a060_s43_fp32
  phase_diagram_t25_a050_s42_fp32
  phase_diagram_t25_a060_s42_fp32
  phase_diagram_t15_a075_s42_fp32_v2
  gen_gpt2m_s43_fp32
  t15_a050_s42_fp32
  phase_diagram_t25_a045_s42_fp32
  phase_diagram_t05_a050_s42_fp32
  phase_diagram_t05_a045_s42_fp32
  alpha_sweep_a052_s43_fp32
  alpha_sweep_a000_s47_fp32
  alpha_sweep_a046_s43_fp32
  alpha_sweep_a000_s46_fp32
  alpha_sweep_a000_s45_fp32
  d37b
  d37g
  alpha_sweep_a060_s42_fp32
  alpha_sweep_a005_s42
  interv_pred_a075_s42_fp32
  interv_pred_14b_s42_fp32
  alpha_sweep_a050_s43_fp32
  generalize_pythia1b_c4_a100_s43_v2
  alpha_sweep_a048_s43_fp32
  t20_a025_s42_fp32
  alpha_sweep_a046_s42_fp32
  alpha_sweep_a052_s42_fp32
  alpha_sweep_a048_s42_fp32
  alpha_sweep_a070_s42_fp32
  gen_gpt2m_a100_s43
  alpha_sweep_a010_s42_bf16
  scale_14b_a050_s42_bf16
  alpha_sweep_a065_s42_fp32
  alpha_sweep_a040_s42_fp32_v2
  interv_react_s43
  scale_69b_a100_s43_fp32
  padding_robustness_a100_s42_fp32
  c4_a075_s43_fp32
  c4_a075_s42_fp32
  c4_a050_s43_fp32
  c4_a050_s42_fp32
  c4_a025_s42_fp32
  alpha_sweep_a075_s43
  alpha_sweep_a035_s42_fp32
  alpha_sweep_a060_s42_fp32_v4
  t20_a075_s42_fp32
  t20_a060_s42_fp32
  smollm3_3b_wiki_a100_s43_fp32
  scale_69b_a100_s43
  scale_69b_a100_s42
  scale_14b_c4_s42_fp32
  scale_14b_a050_s42_fp32
  qwen35_08b_wiki_a100_s43_fp32
  qwen35_08b_wiki_a100_s42_v2
  smollm3_3b_wiki_a100_s42_v3
  alpha_sweep_a045_s43_fp32
  alpha_sweep_a045_s42_fp32
  alpha_sweep_a030_s42_fp32
  alpha_sweep_a060_s43_fp32
  alpha_sweep_a075_s42
  gen_wiki_gpt2m_a100_s42
  opt13b_wiki_a100_s43_fp32
  alpha_sweep_a060_s42_fp32_v3
  alpha_sweep_a050_s42
  alpha_sweep_a060_s42_bf16
  pythia410m_wiki_a100_s43_fp32
  alpha_sweep_a050_postd093_s42_fp32
  interv_react_s43_bf16
  alpha_sweep_a025_s43
  generalize_pythia410m_wiki_a100_s42
  alpha_sweep_a055_s42_fp32
  intervention_reactive_s42
  alpha_sweep_a025_s42_fp32
  generalize_pythia1b_c4_a100_s43
  alpha_sweep_a050_s44_fp32
  interv_pred_s43_bf16
  generalize_pythia1b_c4_a100_s42
  alpha_sweep_a050_s44
  alpha_sweep_a010_s43_fp32
  alpha_sweep_a040_s42_fp32
  intervention_predictive_s42
  alpha_sweep_a010_s43
  generalize_pythia14b_wiki_a100_s43
  alpha_sweep_a075_s44
  generalize_pythia14b_wiki_a100_s42
  alpha_sweep_a010_s42_fp32
  generalize_opt1b_wiki_a100_s42
  alpha_sweep_a010_s42
  alpha_sweep_a050_s43
  gen_gpt2m_a100_s43_bf16
  alpha_sweep_a005_s42_v3
  alpha_sweep_a025_s44_fp32
  alpha_sweep_a075_s42_fp32
  alpha_sweep_a050_s42_fp32
  alpha_sweep_a000_s44
  alpha_sweep_a025_s44
  alpha_sweep_a025_s43_fp32
  alpha_sweep_a000_s43
  alpha_sweep_a000_s42
  t20_a045_s42_fp32
  data_strategy_ablation_s43
  t20_a050_s42_fp32
  t20_a100_s42_fp32
  data_strategy_ablation_s42
  interv_pred_a075_s42
  gen_gpt2m_a100_s43_fp32
  method_ablation_phase3
  qwen35_dryrun_launch
  interv_react_s43_fp32
  generalize_pythia1b_c4_a100_s42_v2
  gen_wiki_gpt2m_a100_s42_v4
  interv_pred_a075_s42_fp32_v4
  alpha_sweep_a060_s42_fp32_v2
  qwen35_08b_wiki_a100_s42
  smollm3_3b_wiki_a100_s42_v2
  scale_14b_a050_s42
  conditional_granger_d061
  interv_pred_a075_s42_fp32_v2
  smollm3_3b_wiki_a100_s42
  alpha_sweep_c4_a050_s42_bf16
  gen_opt13b_a100_s43_bf16
  alpha_sweep_a010_s42_v2
  interv_pred_s43
  alpha_sweep_c4_a050_s42
  alpha_sweep_a060_s42_v2
  mvp_v4_rep45
  mvp_v4_rep43
  mvp_v4_rep42
  gen_wiki_gpt2m_a025_s42
  mvp_v2_rep44
  mvp_rep44
  alpha_sweep_a025_s42
  alpha_sweep_a025_s42_v2
  alpha_sweep_a060_s42
  plan_006_s43
  gen_wiki_gpt2m_a100_s42_v3
  mvp_v4_rep44
  plan_006_s42
  plan_006_s42_resume
  gen_wiki_gpt2m_a100_s42_v2
  method_ablation_phase2
  alpha_sweep_a025_s42_v3
  method_ablation_phase1
  plan_009_bootstrap_ty
  mvp_v3_rep43
  mvp_v3_rep42
  mvp_v2_rep43
  mvp_v2_rep42
  mvp_rep43
  mvp_rep42
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "347acdfc-0084-42eb-bc10-25caeffd9726",
  "isSidechain": true,
  "promptId": "3b6d09a4-9413-4727-a60f-bea5795efd1e",
  "agentId": "aac69cde3cdf76252",
  "type": "user",
  "uuid": "cb9e62a6-1d9a-434c-bafd-04fc68336bbd",
  "sourceToolAssistantUUID": "347acdfc-0084-42eb-bc10-25caeffd9726",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-23T06:19:49.989Z_

Now let me extract the detailed metrics for the matching experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb9e62a6-1d9a-434c-bafd-04fc68336bbd",
  "isSidechain": true,
  "agentId": "aac69cde3cdf76252",
  "requestId": "req_011CbK1sy8NB4tMG5VhHp3YR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d39ded45-38e5-43f7-8af6-ad5275ca91cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYZnzDqeYwWbbwgWpJvn1M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3313,
      "cache_read_input_tokens": 18065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3313,
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

_source line 14 · 2026-05-23T06:20:06.331Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ft615zQ9Qa2fXgWcFB674i`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/88c2d600-443d-4934-bc0d-a18a29f467ab/tool-results && python3 << 'PYEOF'\nimport json\n\nwith open('mcp-agent-ml-research-read_registry-1779517155962.txt', 'r') as f:\n    outer = json.load(f)\n\ndata = json.loads(outer['result'])\nexperiments = data['data']['experiments']\n\n# Target metrics\ntarget_metrics = [\n    'perm_granger_fdr_forward_sig',\n    'perm_granger_fdr_reverse_sig',\n    'robust_pairs_K3',\n    'robust_pairs_K4',\n    'threshold_forward_sig',\n    'diff_xcorr_fdr_forward_sig',\n    'ty_forward_sig',\n    'drift_ppl_pct'\n]\n\n# 1. All scale_14b_t15_* experiments\nprint(\"=\"*120)\nprint(\"GROUP 1: scale_14b_t15_* experiments (1.4B model, T=15)\")\nprint(\"=\"*120)\n\nt15_14b = {k: v for k, v in experiments.items() if 'scale_14b_t15' in k or ('14b' in k and 't15' in k)}\nprint(f\"Found {len(t15_14b)} experiments\\n\")\n\nfor eid, exp in sorted(t15_14b.items()):\n    print(f\"--- {eid} ---\")\n    print(f\"  status: {exp.get('status', 'N/A')}\")\n    print(f\"  conclusion: {exp.get('conclusion', 'N/A')}\")\n    metrics = exp.get('metrics', {})\n    if not metrics:\n        print(f\"  metrics: (empty)\")\n    else:\n        for m in target_metrics:\n            val = metrics.get(m, 'N/A')\n            print(f\"  {m}: {val}\")\n        # Also check for any other interesting metrics\n        other = {k: v for k, v in metrics.items() if k not in target_metrics}\n        if other:\n            print(f\"  [other metrics]: {list(other.keys())}\")\n    print()\n\n# 2. a075 experiments (410M)\nprint(\"=\"*120)\nprint(\"GROUP 2: a075 experiments (look for 410M / alpha=0.75)\")\nprint(\"=\"*120)\n\na075_exps = {k: v for k, v in experiments.items() if 'a075' in k and '14b' not in k and '69b' not in k and '1b' not in k and '3b' not in k and '13b' not in k and 'phase_diagram' not in k}\nprint(f\"Found {len(a075_exps)} experiments\\n\")\n\nfor eid, exp in sorted(a075_exps.items()):\n    print(f\"--- {eid} ---\")\n    print(f\"  status: {exp.get('status', 'N/A')}\")\n    print(f\"  conclusion: {exp.get('conclusion', 'N/A')}\")\n    metrics = exp.get('metrics', {})\n    if not metrics:\n        print(f\"  metrics: (empty)\")\n    else:\n        for m in target_metrics:\n            val = metrics.get(m, 'N/A')\n            print(f\"  {m}: {val}\")\n        other = {k: v for k, v in metrics.items() if k not in target_metrics}\n        if other:\n            print(f\"  [other metrics]: {list(other.keys())}\")\n    print()\n\nPYEOF\n",
  "description": "Extract metrics for 14b_t15 and a075 experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d39ded45-38e5-43f7-8af6-ad5275ca91cf",
  "isSidechain": true,
  "agentId": "aac69cde3cdf76252",
  "requestId": "req_011CbK1sy8NB4tMG5VhHp3YR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ec23b8f-32bb-4634-b795-ba32872e62ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYZnzDqeYwWbbwgWpJvn1M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3313,
      "cache_read_input_tokens": 18065,
      "output_tokens": 1043,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3313
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1043,
          "cache_read_input_tokens": 18065,
          "cache_creation_input_tokens": 3313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3313,
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

_source line 15 · 2026-05-23T06:20:06.449Z_

<details><summary>↩ Tool result · `toolu_01Ft615zQ9Qa2fXgWcFB674i`</summary>

```text
========================================================================================================================
GROUP 1: scale_14b_t15_* experiments (1.4B model, T=15)
========================================================================================================================
Found 9 experiments

--- scale_14b_t15_a045_s42_fp32 ---
  status: DONE
  conclusion: success
  perm_granger_fdr_forward_sig: 3/8
  perm_granger_fdr_reverse_sig: 0/8
  robust_pairs_K3: 4/8
  robust_pairs_K4: N/A
  threshold_forward_sig: 2/8
  diff_xcorr_fdr_forward_sig: 6/8
  ty_forward_sig: 6/8
  drift_ppl_pct: N/A
  [other metrics]: ['n_gens', 'final_ppl', 'final_mauve']

--- scale_14b_t15_a045_s43_fp32 ---
  status: RUNNING
  conclusion: N/A
  metrics: (empty)

--- scale_14b_t15_a050_s42_fp32 ---
  status: DONE
  conclusion: failed
  metrics: (empty)

--- scale_14b_t15_a050_s42_fp32_v3 ---
  status: DONE
  conclusion: success
  perm_granger_fdr_forward_sig: 3/8
  perm_granger_fdr_reverse_sig: 0/8
  robust_pairs_K3: 2/8
  robust_pairs_K4: N/A
  threshold_forward_sig: 2/8
  diff_xcorr_fdr_forward_sig: 8/8
  ty_forward_sig: 3/8
  drift_ppl_pct: N/A
  [other metrics]: ['diff_xcorr_fdr_reverse_sig', 'n_perm', 'comparison_410M']

--- scale_14b_t15_a050_s43_fp32 ---
  status: RUNNING
  conclusion: N/A
  metrics: (empty)

--- scale_14b_t15_a060_s42_fp32 ---
  status: DONE
  conclusion: failed
  metrics: (empty)

--- scale_14b_t15_a060_s42_fp32_v2 ---
  status: DONE
  conclusion: success
  perm_granger_fdr_forward_sig: N/A
  perm_granger_fdr_reverse_sig: N/A
  robust_pairs_K3: N/A
  robust_pairs_K4: N/A
  threshold_forward_sig: N/A
  diff_xcorr_fdr_forward_sig: N/A
  ty_forward_sig: N/A
  drift_ppl_pct: N/A
  [other metrics]: ['PermG_fwd', 'PermG_rev', 'K_ge_3', 'K_ge_4', 'threshold_onset_3sigma', 'diff_xcorr_fdr_fwd', 'TY_granger', 'drift_ppl', 'drift_mauve', 'drift_entropy', 'drift_ece']

--- scale_14b_t15_a060_s43_fp32 ---
  status: RUNNING
  conclusion: N/A
  metrics: (empty)

--- scale_14b_t15_a075_s42_fp32 ---
  status: DONE
  conclusion: success
  perm_granger_fdr_forward_sig: 6
  perm_granger_fdr_reverse_sig: 0
  robust_pairs_K3: 6
  robust_pairs_K4: 6
  threshold_forward_sig: 7
  diff_xcorr_fdr_forward_sig: 8
  ty_forward_sig: 5
  drift_ppl_pct: 390.5
  [other metrics]: ['diff_xcorr_fdr_reverse_sig', 'drift_mauve_pct', 'drift_entropy_pct', 'drift_ece_pct', 'drift_distinct1_pct', 'drift_distinct2_pct', 'drift_distinct3_pct']

========================================================================================================================
GROUP 2: a075 experiments (look for 410M / alpha=0.75)
========================================================================================================================
Found 11 experiments

--- alpha_sweep_a075_s42 ---
  status: DONE
  conclusion: success
  perm_granger_fdr_forward_sig: 6
  perm_granger_fdr_reverse_sig: 0
  robust_pairs_K3: 4
  robust_pairs_K4: 0
  threshold_forward_sig: N/A
  diff_xcorr_fdr_forward_sig: 6
  ty_forward_sig: 2
  drift_ppl_pct: N/A
  [other metrics]: ['progress', 'gen0_token_entropy', 'gen10_token_entropy', 'gen0_ece', 'gen10_ece', 'gen0_perplexity', 'gen10_perplexity', 'gen0_distinct_1', 'gen10_distinct_1', 'gen0_distinct_2', 'gen10_distinct_2', 'gen0_distinct_3', 'gen10_distinct_3', 'token_entropy_drift_pct', 'ece_drift_pct', 'perplexity_drift_pct', 'distinct_1_drift_pct', 'distinct_2_drift_pct', 'distinct_3_drift_pct', 'granger_ece_to_d1_p_fdr', 'granger_ece_to_d2_p_fdr', 'granger_entropy_to_d2_p_fdr', 'granger_entropy_to_d1_p_fdr', 'granger_fdr_sig_count', 'consensus_robust_pairs', 'xcorr_entropy_d1_lag', 'xcorr_entropy_d1_r', 'diff_xcorr_fdr_reverse_sig', 'threshold_onset_forward_sig']

--- alpha_sweep_a075_s42_fp32 ---
  status: DONE
  conclusion: success
  perm_granger_fdr_forward_sig: 6
  perm_granger_fdr_reverse_sig: 0
  robust_pairs_K3: 6
  robust_pairs_K4: 0
  threshold_forward_sig: N/A
  diff_xcorr_fdr_forward_sig: 6
  ty_forward_sig: 2
  drift_ppl_pct: N/A
  [other metrics]: ['n_generations', 'gen0', 'gen10', 'drift_pct', 'lead_lag', 'asymmetry', 'diff_xcorr_fdr_reverse_sig', 'threshold_onset_forward_sig']

--- alpha_sweep_a075_s43 ---
  status: DONE
  conclusion: success
  perm_granger_fdr_forward_sig: 5
  perm_granger_fdr_reverse_sig: 0
  robust_pairs_K3: 2
  robust_pairs_K4: 0
  threshold_forward_sig: N/A
  diff_xcorr_fdr_forward_sig: 6
  ty_forward_sig: 2
  drift_ppl_pct: N/A
  [other metrics]: ['gen0', 'gen10', 'drift_pct', 'PermG_fwd', 'PermG_rev', 'naive_xcorr_fwd_D111', 'diff_xcorr_fwd_D111', 'threshold_onset_3sigma', 'K3_3sigma', 'K4_3sigma', 'D105_D111_compliant', 'M035_direction', 'precision', 'n_perm', 'pair_config', 'diff_xcorr_fdr_reverse_sig', 'threshold_onset_forward_sig']

--- alpha_sweep_a075_s44 ---
  status: DONE
  conclusion: success
  perm_granger_fdr_forward_sig: 0
  perm_granger_fdr_reverse_sig: 0
  robust_pairs_K3: 1
  robust_pairs_K4: 0
  threshold_forward_sig: N/A
  diff_xcorr_fdr_forward_sig: 7
  ty_forward_sig: 1
  drift_ppl_pct: N/A
  [other metrics]: ['gen0', 'gen10', 'drift_pct', 'diff_xcorr_fdr_reverse_sig', 'threshold_onset_forward_sig']

--- c4_a075_s42_fp32 ---
  status: DONE
  conclusion: success
  perm_granger_fdr_forward_sig: 8
  perm_granger_fdr_reverse_sig: 0
  robust_pairs_K3: 8
  robust_pairs_K4: 3
  threshold_forward_sig: N/A
  diff_xcorr_fdr_forward_sig: 8
  ty_forward_sig: 3
  drift_ppl_pct: N/A
  [other metrics]: ['PermG_fwd', 'PermG_rev', 'K_ge_3_3sigma', 'K_ge_4_3sigma', 'threshold_onset_3sigma', 'naive_xcorr', 'diff_xcorr', 'drift_token_entropy', 'drift_ece', 'drift_perplexity', 'drift_distinct_1', 'drift_distinct_2', 'drift_distinct_3', 'drift_mauve', 'drift_effective_rank', 'gen0_token_entropy', 'D105_3sigma', 'D111_direction', 'analysis_script', 'n_perm', 'D120_recomputed', 'D102_8pair', 'diff_xcorr_fdr_reverse_sig', 'threshold_onset_forward_sig']

--- c4_a075_s43_fp32 ---
  status: DONE
  conclusion: success
  perm_granger_fdr_forward_sig: 8
  perm_granger_fdr_reverse_sig: 0
  robust_pairs_K3: 8
  robust_pairs_K4: 3
  threshold_forward_sig: N/A
  diff_xcorr_fdr_forward_sig: 8
  ty_forward_sig: 3
  drift_ppl_pct: N/A
  [other metrics]: ['PermG_fwd', 'PermG_rev', 'K_ge_3_3sigma', 'K_ge_4_3sigma', 'threshold_onset_3sigma', 'naive_xcorr', 'diff_xcorr', 'drift_token_entropy', 'drift_ece', 'drift_perplexity', 'drift_distinct_1', 'drift_distinct_2', 'drift_distinct_3', 'drift_mauve', 'drift_effective_rank', 'gen0_token_entropy', 'D111_direction_check', 'D102_8pair', 'D105_3sigma', 'analysis_script', 'n_perm', 'diff_xcorr_fdr_reverse_sig', 'threshold_onset_forward_sig']

--- interv_pred_a075_s42 ---
  status: DONE
  conclusion: killed
  metrics: (empty)

--- interv_pred_a075_s42_fp32 ---
  status: DONE
  conclusion: killed
  metrics: (empty)

--- interv_pred_a075_s42_fp32_v2 ---
  status: DONE
  conclusion: killed
  metrics: (empty)

--- interv_pred_a075_s42_fp32_v4 ---
  status: DONE
  conclusion: success
  perm_granger_fdr_forward_sig: N/A
  perm_granger_fdr_reverse_sig: N/A
  robust_pairs_K3: N/A
  robust_pairs_K4: N/A
  threshold_forward_sig: N/A
  diff_xcorr_fdr_forward_sig: N/A
  ty_forward_sig: N/A
  drift_ppl_pct: N/A
  [other metrics]: ['final_ppl', 'final_entropy', 'final_eff_rank', 'final_mauve', 'precision', 'intervention_trigger_gen', 'recovery_gen', 'token_entropy_drift', 'ece_drift', 'perplexity_drift', 'distinct_1_drift', 'distinct_2_drift', 'distinct_3_drift', 'perm_granger_fwd', 'perm_granger_rev', 'threshold_onset_fwd', 'consensus_k4', 'mmct_wpair_fwd']

--- t20_a075_s42_fp32 ---
  status: DONE
  conclusion: success
  perm_granger_fdr_forward_sig: 6
  perm_granger_fdr_reverse_sig: 0
  robust_pairs_K3: 6
  robust_pairs_K4: 6
  threshold_forward_sig: N/A
  diff_xcorr_fdr_forward_sig: 7
  ty_forward_sig: 5
  drift_ppl_pct: N/A
  [other metrics]: ['PermG_fwd_fdr', 'PermG_rev_fdr', 'DiffXCorr_fdr_fwd', 'Threshold_3sigma', 'NaiveXCorr_fwd', 'verdict', 'predicted_permg', 'observed_permg', 'predicted_ci', 'note', 'diff_xcorr_fdr_reverse_sig', 'threshold_onset_forward_sig']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ec23b8f-32bb-4634-b795-ba32872e62ea",
  "isSidechain": true,
  "promptId": "3b6d09a4-9413-4727-a60f-bea5795efd1e",
  "agentId": "aac69cde3cdf76252",
  "type": "user",
  "uuid": "1e92cc5b-c9a6-4c07-a148-d4d360379038",
  "sourceToolAssistantUUID": "1ec23b8f-32bb-4634-b795-ba32872e62ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-23T06:20:09.469Z_

Now let me get the extra metrics for the `scale_14b_t15_a060_s42_fp32_v2` which uses different key names.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e92cc5b-c9a6-4c07-a148-d4d360379038",
  "isSidechain": true,
  "agentId": "aac69cde3cdf76252",
  "requestId": "req_011CbK1uLndti34VtF6pAb8b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "568da7db-e79d-4db3-bd4b-9db3b6759840",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbLqFNAM3VZ9B1bFpLbrLj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4590,
      "cache_read_input_tokens": 21378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4590,
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

_source line 17 · 2026-05-23T06:20:20.578Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01YWkrcwpVkCTdxJuHdaQdsn`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/88c2d600-443d-4934-bc0d-a18a29f467ab/tool-results && python3 << 'PYEOF'\nimport json\n\nwith open('mcp-agent-ml-research-read_registry-1779517155962.txt', 'r') as f:\n    outer = json.load(f)\n\ndata = json.loads(outer['result'])\nexperiments = data['data']['experiments']\n\n# Print full metrics for the experiment with alternate key names\neid = 'scale_14b_t15_a060_s42_fp32_v2'\nexp = experiments[eid]\nprint(f\"=== Full metrics for {eid} ===\")\nprint(json.dumps(exp.get('metrics', {}), indent=2))\n\n# Also print full metrics for scale_14b_t15_a075_s42_fp32 (most complete)\neid2 = 'scale_14b_t15_a075_s42_fp32'\nexp2 = experiments[eid2]\nprint(f\"\\n=== Full metrics for {eid2} ===\")\nprint(json.dumps(exp2.get('metrics', {}), indent=2))\n\n# Also get scale_14b_t15_a050_s42_fp32_v3 comparison_410M field\neid3 = 'scale_14b_t15_a050_s42_fp32_v3'\nexp3 = experiments[eid3]\nprint(f\"\\n=== Full metrics for {eid3} ===\")\nprint(json.dumps(exp3.get('metrics', {}), indent=2))\n\n# And scale_14b_t15_a045_s42_fp32\neid4 = 'scale_14b_t15_a045_s42_fp32'\nexp4 = experiments[eid4]\nprint(f\"\\n=== Full metrics for {eid4} ===\")\nprint(json.dumps(exp4.get('metrics', {}), indent=2))\n\n# Also print alpha_sweep_a075_s42_fp32 full metrics\neid5 = 'alpha_sweep_a075_s42_fp32'\nexp5 = experiments[eid5]\nprint(f\"\\n=== Full metrics for {eid5} ===\")\nprint(json.dumps(exp5.get('metrics', {}), indent=2))\nPYEOF\n",
  "description": "Get full metrics for key experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "568da7db-e79d-4db3-bd4b-9db3b6759840",
  "isSidechain": true,
  "agentId": "aac69cde3cdf76252",
  "requestId": "req_011CbK1uLndti34VtF6pAb8b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7dcf14bc-4310-41ba-aaae-9ae644698aac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbLqFNAM3VZ9B1bFpLbrLj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4590,
      "cache_read_input_tokens": 21378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4590,
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

_source line 18 · 2026-05-23T06:20:20.709Z_

<details><summary>↩ Tool result · `toolu_01YWkrcwpVkCTdxJuHdaQdsn`</summary>

```text
=== Full metrics for scale_14b_t15_a060_s42_fp32_v2 ===
{
  "PermG_fwd": "6/8",
  "PermG_rev": "0/8",
  "K_ge_3": "6/8",
  "K_ge_4": "3/8",
  "threshold_onset_3sigma": "6/8",
  "diff_xcorr_fdr_fwd": "7/8",
  "TY_granger": "1/8",
  "drift_ppl": "+246.5%",
  "drift_mauve": "0.033->0.029",
  "drift_entropy": "-27.9%",
  "drift_ece": "+2791%"
}

=== Full metrics for scale_14b_t15_a075_s42_fp32 ===
{
  "perm_granger_fdr_forward_sig": 6,
  "perm_granger_fdr_reverse_sig": 0,
  "diff_xcorr_fdr_forward_sig": 8,
  "diff_xcorr_fdr_reverse_sig": 8,
  "threshold_forward_sig": 7,
  "ty_forward_sig": 5,
  "robust_pairs_K3": 6,
  "robust_pairs_K4": 6,
  "drift_ppl_pct": 390.5,
  "drift_mauve_pct": -3.6,
  "drift_entropy_pct": -29.5,
  "drift_ece_pct": 3091.2,
  "drift_distinct1_pct": -19.4,
  "drift_distinct2_pct": -23.3,
  "drift_distinct3_pct": -19.9
}

=== Full metrics for scale_14b_t15_a050_s42_fp32_v3 ===
{
  "perm_granger_fdr_forward_sig": "3/8",
  "perm_granger_fdr_reverse_sig": "0/8",
  "diff_xcorr_fdr_forward_sig": "8/8",
  "diff_xcorr_fdr_reverse_sig": "8/8",
  "threshold_forward_sig": "2/8",
  "ty_forward_sig": "3/8",
  "robust_pairs_K3": "2/8",
  "n_perm": 5000,
  "comparison_410M": "410M T=15 a=0.50 = 6/8 K>=3 vs 1.4B = 2/8 K>=3. Onset shift confirmed at T=15."
}

=== Full metrics for scale_14b_t15_a045_s42_fp32 ===
{
  "perm_granger_fdr_forward_sig": "3/8",
  "perm_granger_fdr_reverse_sig": "0/8",
  "diff_xcorr_fdr_forward_sig": "6/8",
  "threshold_forward_sig": "2/8",
  "ty_forward_sig": "6/8",
  "robust_pairs_K3": "4/8",
  "n_gens": 16,
  "final_ppl": 34.16,
  "final_mauve": 0.0252
}

=== Full metrics for alpha_sweep_a075_s42_fp32 ===
{
  "n_generations": 11,
  "gen0": {
    "token_entropy": 3.2342,
    "ece": 0.0108,
    "perplexity": 26.949,
    "distinct_1": 0.098,
    "distinct_2": 0.5141,
    "distinct_3": 0.8127,
    "effective_rank": 46.613,
    "mauve": 0.0311
  },
  "gen10": {
    "token_entropy": 2.283,
    "ece": 0.2145,
    "perplexity": 77.697,
    "distinct_1": 0.0731,
    "distinct_2": 0.357,
    "distinct_3": 0.5957,
    "effective_rank": 78.06,
    "mauve": 0.0299
  },
  "drift_pct": {
    "token_entropy": -29.41,
    "ece": 1885.41,
    "perplexity": 188.31,
    "distinct_1": -25.38,
    "distinct_2": -30.55,
    "distinct_3": -26.7,
    "effective_rank": 67.47,
    "mauve": -3.73
  },
  "lead_lag": {
    "PermG_fwd": "6/8",
    "PermG_rev": "0/8",
    "K_ge_4": "6/8",
    "MMCT_detection": 0.75,
    "naive_xcorr": "7/8",
    "diff_xcorr": "6/8",
    "threshold_onset": "8/8"
  },
  "asymmetry": "strong (fwd=6, rev=0)",
  "ty_forward_sig": 2,
  "perm_granger_fdr_forward_sig": 6,
  "perm_granger_fdr_reverse_sig": 0,
  "diff_xcorr_fdr_forward_sig": 6,
  "diff_xcorr_fdr_reverse_sig": 6,
  "threshold_onset_forward_sig": 0,
  "robust_pairs_K3": 6,
  "robust_pairs_K4": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dcf14bc-4310-41ba-aaae-9ae644698aac",
  "isSidechain": true,
  "promptId": "3b6d09a4-9413-4727-a60f-bea5795efd1e",
  "agentId": "aac69cde3cdf76252",
  "type": "user",
  "uuid": "ab9dd971-26ca-4cfa-ad0b-eb2a23505976",
  "sourceToolAssistantUUID": "7dcf14bc-4310-41ba-aaae-9ae644698aac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-23T06:20:42.586Z_

Here are the extracted results:

---

## GROUP 1: `scale_14b_t15_*` (1.4B model, T=15)

9 experiments found; 3 still RUNNING (no metrics), 2 earlier versions concluded "failed" (no metrics). 4 have completed results:

| exp_id | status | PermG fwd | PermG rev | K>=3 | K>=4 | Threshold fwd | DiffXCorr fwd | TY fwd | drift_ppl |
|---|---|---|---|---|---|---|---|---|---|
| `scale_14b_t15_a045_s42_fp32` | DONE/success | 3/8 | 0/8 | 4/8 | -- | 2/8 | 6/8 | 6/8 | -- |
| `scale_14b_t15_a050_s42_fp32_v3` | DONE/success | 3/8 | 0/8 | 2/8 | -- | 2/8 | 8/8 | 3/8 | -- |
| `scale_14b_t15_a060_s42_fp32_v2` | DONE/success | 6/8 | 0/8 | 6/8 | 3/8 | 6/8 | 7/8 | 1/8 | +246.5% |
| `scale_14b_t15_a075_s42_fp32` | DONE/success | 6 | 0 | 6 | 6 | 7 | 8 | 5 | +390.5% |

**Still RUNNING** (no metrics yet): `scale_14b_t15_a045_s43_fp32`, `scale_14b_t15_a050_s43_fp32`, `scale_14b_t15_a060_s43_fp32`

**Failed** (no metrics): `scale_14b_t15_a050_s42_fp32`, `scale_14b_t15_a060_s42_fp32`

Notable extra metrics for `scale_14b_t15_a075_s42_fp32`: drift_mauve=-3.6%, drift_entropy=-29.5%, drift_ece=+3091.2%, drift_distinct1=-19.4%.

Notable for `scale_14b_t15_a050_s42_fp32_v3`: comparison_410M note says "410M T=15 a=0.50 = 6/8 K>=3 vs 1.4B = 2/8 K>=3. Onset shift confirmed at T=15."

---

## GROUP 2: `a075` experiments (410M, alpha=0.75)

Filtering out 14b/69b/1b/3b/13b/phase_diagram variants, 11 experiments found. Key ones with metrics:

| exp_id | status | PermG fwd | PermG rev | K>=3 | K>=4 | Threshold fwd | DiffXCorr fwd | TY fwd | drift_ppl |
|---|---|---|---|---|---|---|---|---|---|
| `alpha_sweep_a075_s42` | DONE/success | 6 | 0 | 4 | 0 | -- | 6 | 2 | -- |
| `alpha_sweep_a075_s42_fp32` | DONE/success | 6 | 0 | 6 | 0 | -- | 6 | 2 | ppl drift=+188.3% |
| `alpha_sweep_a075_s43` | DONE/success | 5 | 0 | 2 | 0 | -- | 6 | 2 | -- |
| `alpha_sweep_a075_s44` | DONE/success | 0 | 0 | 1 | 0 | -- | 7 | 1 | -- |
| `c4_a075_s42_fp32` | DONE/success | 8 | 0 | 8 | 3 | -- | 8 | 3 | -- |
| `c4_a075_s43_fp32` | DONE/success | 8 | 0 | 8 | 3 | -- | 8 | 3 | -- |
| `t20_a075_s42_fp32` | DONE/success | 6 | 0 | 6 | 6 | -- | 7 | 5 | -- |

**Killed** (no metrics): `interv_pred_a075_s42`, `interv_pred_a075_s42_fp32`, `interv_pred_a075_s42_fp32_v2`

**`interv_pred_a075_s42_fp32_v4`** completed successfully but uses different metric keys (perm_granger_fwd, threshold_onset_fwd, consensus_k4, etc.) -- intervention experiment, not a standard sweep.

For `alpha_sweep_a075_s42_fp32` specifically: gen0 ppl=26.95, gen10 ppl=77.70 (+188.3%), gen0 entropy=3.23, gen10 entropy=2.28 (-29.4%), gen0 ece=0.011, gen10 ece=0.215 (+1885%), strong asymmetry (fwd=6, rev=0).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab9dd971-26ca-4cfa-ad0b-eb2a23505976",
  "isSidechain": true,
  "agentId": "aac69cde3cdf76252",
  "requestId": "req_011CbK1vPnF9Qoi2ESnYW9a9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09632865-c874-40a5-8c32-0ff42a7bfbbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "88c2d600-443d-4934-bc0d-a18a29f467ab",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzPyzv9oJiPqkvsfgLPWW5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2219,
      "cache_read_input_tokens": 25968,
      "output_tokens": 1346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2219
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1346,
          "cache_read_input_tokens": 25968,
          "cache_creation_input_tokens": 2219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2219,
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
