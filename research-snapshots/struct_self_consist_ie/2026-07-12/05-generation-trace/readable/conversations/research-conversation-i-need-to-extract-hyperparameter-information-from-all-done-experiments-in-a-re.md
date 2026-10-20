# Research conversation: I need to extract hyperparameter information from all DONE experiments in a registry JSON file. The file is at: /home/ub

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a67b4a5d19dcf0796.jsonl`
- **Structured JSON:** [`25121cc8ea755ab68c43.json`](../../sessions/25/25121cc8ea755ab68c43.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

53 recorded events

### User

_source line 1 · 2026-05-21T11:16:51.856Z_

I need to extract hyperparameter information from all DONE experiments in a registry JSON file. The file is at:
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a9ed86cb-a33f-4ec8-8078-d4b9402803ce/tool-results/mcp-agent-ml-research-read_registry-1779362196402.txt

The file is JSON with schema: {result: string} — the `result` field is itself a JSON string that needs to be parsed.

**What I need you to extract for each experiment:**

1. Experiment ID and name
2. Fine-tuning hyperparameters (if applicable): model name, model size, LoRA rank/alpha, learning rate, batch size, epochs, optimizer
3. Inference parameters: N (number of samples), T (temperature), seed
4. Dataset name, number of data points
5. GPU type, training duration
6. For API-based models (GPT-5.5, Claude, Gemini, DeepSeek): API parameters

**Steps:**
1. First probe the structure: `jq '.result | fromjson | type, length' file` or similar
2. Then extract all experiment entries — look at the `spec` field of each experiment for hyperparameters
3. Also look at fields like `config`, `params`, or any nested objects that might contain hyperparameters

**Categorize experiments into:**
- Fine-tuning experiments (training LoRA adapters etc.)
- Inference/evaluation experiments
- API-based model experiments (frontier models)

**Output format:** Return a comprehensive structured summary with ALL hyperparameter values found, organized by experiment. Include experiment IDs. Flag any experiments where spec is missing or incomplete. Be thorough — I need exact numbers, not summaries. Quote values verbatim from the data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "316f267e-90ba-46ed-bec6-28212a1d6e32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T11:16:51.862Z_

```json
{
  "parentUuid": "316f267e-90ba-46ed-bec6-28212a1d6e32",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
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
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "a84024ee-fa63-4ee0-951c-eafdab3e968a",
  "timestamp": "2026-05-21T11:16:51.862Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T11:16:54.201Z_



I'll start by reading the file to understand its structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a84024ee-fa63-4ee0-951c-eafdab3e968a",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFcv2Mhb3WyY19PLJWpf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "829268bc-cf59-416b-aca9-23084425aa77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HMLj5bZg7nirBuL1ck3Lx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15070,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15070,
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

_source line 4 · 2026-05-21T11:16:55.226Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NcriCcNWThCjTQnCP3xzy7`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a9ed86cb-a33f-4ec8-8078-d4b9402803ce/tool-results/mcp-agent-ml-research-read_registry-1779362196402.txt",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "829268bc-cf59-416b-aca9-23084425aa77",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFcv2Mhb3WyY19PLJWpf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c44cbb7b-60c2-49d3-8011-6e2752eeabeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HMLj5bZg7nirBuL1ck3Lx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15070,
      "cache_read_input_tokens": 0,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15070
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 174,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15070,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15070,
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

_source line 5 · 2026-05-21T11:16:55.688Z_

<details><summary>↩ Tool result · reported error · `toolu_01NcriCcNWThCjTQnCP3xzy7`</summary>

```text
File content (176125 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c44cbb7b-60c2-49d3-8011-6e2752eeabeb",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "9ca81463-9b50-468a-8a40-a555b8eff294",
  "toolUseResult": "Error: File content (176125 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "c44cbb7b-60c2-49d3-8011-6e2752eeabeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T11:16:58.271Z_

The file is very large. Let me probe its structure first using bash with jq.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ca81463-9b50-468a-8a40-a555b8eff294",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFcvJzKtswwCgeSeNci4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ab6457b-eb08-458a-98d2-880bdc83d057",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5hsW8j7ALzbnR87pR6g7z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 15070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1076,
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

_source line 7 · 2026-05-21T11:17:02.435Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KMRcXarWXaiPJDL6dknCQi`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a9ed86cb-a33f-4ec8-8078-d4b9402803ce/tool-results && cat mcp-agent-ml-research-read_registry-1779362196402.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nprint('Type:', type(inner).__name__)\nif isinstance(inner, dict):\n    print('Top-level keys:', list(inner.keys()))\n    for k, v in inner.items():\n        if isinstance(v, list):\n            print(f'  {k}: list of {len(v)} items')\n        elif isinstance(v, dict):\n            print(f'  {k}: dict with keys {list(v.keys())[:10]}')\n        else:\n            print(f'  {k}: {type(v).__name__} = {str(v)[:100]}')\nelif isinstance(inner, list):\n    print('Length:', len(inner))\n\"\n",
  "description": "Probe the JSON structure of the registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ab6457b-eb08-458a-98d2-880bdc83d057",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFcvJzKtswwCgeSeNci4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "baaf67e2-8070-45fb-9ccc-28d51feecda7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5hsW8j7ALzbnR87pR6g7z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 15070,
      "output_tokens": 381,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1076
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 381,
          "cache_read_input_tokens": 15070,
          "cache_creation_input_tokens": 1076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1076,
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

_source line 8 · 2026-05-21T11:17:02.780Z_

<details><summary>↩ Tool result · `toolu_01KMRcXarWXaiPJDL6dknCQi`</summary>

```text
Type: dict
Top-level keys: ['success', 'data', 'error', 'metadata']
  success: bool = True
  data: dict with keys ['experiments', 'count', 'total', 'baseline']
  error: NoneType = None
  metadata: dict with keys ['elapsed_seconds']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "baaf67e2-8070-45fb-9ccc-28d51feecda7",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "01c4f263-1646-45f8-97fe-2202aa403c92",
  "sourceToolAssistantUUID": "baaf67e2-8070-45fb-9ccc-28d51feecda7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T11:17:07.859Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PR8XtQFdcHyaSqGKQRLpXw`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a9ed86cb-a33f-4ec8-8078-d4b9402803ce/tool-results && cat mcp-agent-ml-research-read_registry-1779362196402.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint(f'Baseline: {inner[\\\"data\\\"][\\\"baseline\\\"]}')\nprint()\n# List all experiments with their status\nfor e in exps:\n    status = e.get('status', 'UNKNOWN')\n    eid = e.get('id', 'NO_ID')\n    name = e.get('name', 'NO_NAME')\n    print(f'  [{status}] {eid}: {name}')\n\"\n",
  "description": "List all experiments and their statuses"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01c4f263-1646-45f8-97fe-2202aa403c92",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFcvq4arP3LVngEsJShd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a83a59a3-a1b7-4d5f-b18b-bbd45aa4d522",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XyDy7P4vVrErgmj3FmCyRE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 16146,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 467
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 334,
          "cache_read_input_tokens": 16146,
          "cache_creation_input_tokens": 467,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 467,
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

_source line 10 · 2026-05-21T11:17:08.158Z_

<details><summary>↩ Tool result · reported error · `toolu_01PR8XtQFdcHyaSqGKQRLpXw`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 11, in &lt;module>
    status = e.get('status', 'UNKNOWN')
             ^^^^^
AttributeError: 'str' object has no attribute 'get'
Total experiments: 256
Baseline: None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a83a59a3-a1b7-4d5f-b18b-bbd45aa4d522",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "dda2af27-fc94-4cf0-8ae0-8fbed89f662e",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 11, in &lt;module>\n    status = e.get('status', 'UNKNOWN')\n             ^^^^^\nAttributeError: 'str' object has no attribute 'get'\nTotal experiments: 256\nBaseline: None",
  "sourceToolAssistantUUID": "a83a59a3-a1b7-4d5f-b18b-bbd45aa4d522",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T11:17:15.979Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BRSKMB55ysi7Ue3x5PTeeN`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a9ed86cb-a33f-4ec8-8078-d4b9402803ce/tool-results && cat mcp-agent-ml-research-read_registry-1779362196402.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n# Check if experiments is a dict or list, and what keys/elements look like\nprint('Type of experiments:', type(exps).__name__)\nif isinstance(exps, dict):\n    keys = list(exps.keys())\n    print(f'Number of experiment keys: {len(keys)}')\n    print(f'First 3 keys: {keys[:3]}')\n    # Look at first experiment\n    first_key = keys[0]\n    first_val = exps[first_key]\n    print(f'Type of first value: {type(first_val).__name__}')\n    if isinstance(first_val, dict):\n        print(f'Keys of first experiment: {list(first_val.keys())}')\n    elif isinstance(first_val, str):\n        print(f'First value (first 500 chars): {first_val[:500]}')\nelif isinstance(exps, list):\n    print(f'First element type: {type(exps[0]).__name__}')\n    if isinstance(exps[0], str):\n        print(f'First element (first 500 chars): {exps[0][:500]}')\n    elif isinstance(exps[0], dict):\n        print(f'First element keys: {list(exps[0].keys())}')\n\"\n",
  "description": "Understand the experiments data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dda2af27-fc94-4cf0-8ae0-8fbed89f662e",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFcwE2x6YdTu8jZc8R2t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b94b3c0-6267-4c11-9db9-a78423490fc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GG8g9ztJtysUTJpzv6Kh4P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 16613,
      "output_tokens": 522,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 430
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 522,
          "cache_read_input_tokens": 16613,
          "cache_creation_input_tokens": 430,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 430,
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

_source line 12 · 2026-05-21T11:17:16.118Z_

<details><summary>↩ Tool result · `toolu_01BRSKMB55ysi7Ue3x5PTeeN`</summary>

```text
Type of experiments: dict
Number of experiment keys: 256
First 3 keys: ['exp_conll_mf4_v2_s42', 'exp_e2_pretrained_scierc', 'exp_e2_pretrained_conll']
Type of first value: dict
Keys of first experiment: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'metrics', 'completed_at']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b94b3c0-6267-4c11-9db9-a78423490fc3",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "24a6ebf0-cd97-4462-a51d-70a487b182cb",
  "sourceToolAssistantUUID": "0b94b3c0-6267-4c11-9db9-a78423490fc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-21T11:17:18.888Z_

Good, now I can see the structure. Let me get all DONE experiments and their full details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24a6ebf0-cd97-4462-a51d-70a487b182cb",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFcwp3M2A4EgLk539viP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c7934e3-90da-4a89-9e14-0d65848d4079",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJMV9QS3nuqPihB3DvMuso",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 653,
      "cache_read_input_tokens": 17043,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 653,
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

_source line 14 · 2026-05-21T11:17:22.677Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014b1et2qbRz2jB9Uy9aXdE2`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a9ed86cb-a33f-4ec8-8078-d4b9402803ce/tool-results && cat mcp-agent-ml-research-read_registry-1779362196402.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# Count by status\nfrom collections import Counter\nstatuses = Counter()\nfor k, v in exps.items():\n    statuses[v.get('status', 'UNKNOWN')] += 1\nprint('Status counts:')\nfor s, c in statuses.most_common():\n    print(f'  {s}: {c}')\n\n# List all DONE experiments\nprint()\nprint('DONE experiments:')\ndone_exps = {k: v for k, v in exps.items() if v.get('status') == 'DONE'}\nfor k in sorted(done_exps.keys()):\n    print(f'  {k}')\nprint(f'Total DONE: {len(done_exps)}')\n\"\n",
  "description": "Count experiments by status and list all DONE experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c7934e3-90da-4a89-9e14-0d65848d4079",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFcwp3M2A4EgLk539viP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b53f7d00-e03d-4203-a70c-f418b41080e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJMV9QS3nuqPihB3DvMuso",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 653,
      "cache_read_input_tokens": 17043,
      "output_tokens": 414,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 653
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 414,
          "cache_read_input_tokens": 17043,
          "cache_creation_input_tokens": 653,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 653,
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

_source line 15 · 2026-05-21T11:17:22.770Z_

<details><summary>↩ Tool result · `toolu_014b1et2qbRz2jB9Uy9aXdE2`</summary>

```text
Status counts:
  DONE: 256

DONE experiments:
  dgs_pilot
  e1_component_wise_re_sj
  exp001_seed123
  exp001_seed456
  exp008_re_n16
  exp_001_n16_seed123
  exp_001_n16_seed123_full
  exp_001_n16_seed456
  exp_001_n16_seed456_full
  exp_001_ner_n16_scierc
  exp_001_ner_n16_seed123
  exp_001_seed123_t10_full
  exp_001_seed123_v2
  exp_001_seed123_v2_r1024
  exp_001_seed42_v2
  exp_001_seed42_v2_r1024
  exp_001_seed456_t10_full
  exp_001_seed456_v2
  exp_001_seed456_v2_ner
  exp_001_seed456_v2_ner_r1024
  exp_002
  exp_002_conll_n16
  exp_002_conll_n16_r1024
  exp_002_conll_n16_seed123
  exp_002_conll_n16_seed456
  exp_002_merge_conll2003
  exp_002_ner_conll2003
  exp_003_ner_wnut17
  exp_003_wnut17_eval
  exp_003_wnut17_v2
  exp_004_re_diagnostic
  exp_004_v2
  exp_005
  exp_005_v2
  exp_006_v2
  exp_007_llama_inference
  exp_007_llama_n16
  exp_007_llama_n16_r1024
  exp_007_llama_scierc_seed123
  exp_007_llama_seed123
  exp_007_llama_seed456
  exp_007_ner_llama
  exp_007_ner_multi_model
  exp_008_re_n16
  exp_008_re_n16_full
  exp_008_re_n16_t10_full
  exp_008_re_n16_v2
  exp_008_re_seed123
  exp_009_capability_stratification
  exp_009_v2
  exp_009_v2_re_rerun
  exp_010_selection_curves
  exp_011_ood_conll_to_scierc
  exp_011_ood_scierc_to_conll
  exp_012_logprob_baseline
  exp_012_rerun_1024
  exp_013_exact_match_voting
  exp_014_entity_majority_voting
  exp_015_metrics_expansion
  exp_015_v2
  exp_016_rerun_1024_bootstrap
  exp_016_signal_ensemble
  exp_016_v2
  exp_017_llama_conll
  exp_017_llama_conll_finetune
  exp_017_llama_conll_infer
  exp_017_llama_conll_n16
  exp_017_llama_conll_n16_r1024
  exp_017_llama_conll_n16_s123
  exp_017_llama_conll_n16_s123_r1024
  exp_017_llama_conll_n16_s456
  exp_017_llama_conll_n16_s456_r1024
  exp_017_llama_conll_n8_t07
  exp_018_llama_scierc_seed123
  exp_018_llama_scierc_seed42_r1024
  exp_018_llama_scierc_seed456
  exp_018_llama_scierc_seed456_r1024
  exp_018_qwen_scierc_seed123
  exp_018_qwen_scierc_seed456
  exp_019_supervised_verifier
  exp_020_fewnerd_smoke
  exp_021_fewnerd_full
  exp_021_fewnerd_n8_seed123
  exp_021_fewnerd_n8_seed456
  exp_022_seed789
  exp_023_lora_rank8
  exp_024_claim_audit
  exp_025_n32
  exp_026_T05
  exp_026_T08
  exp_026_T12
  exp_026_t05
  exp_026_t05_scierc
  exp_026_t05_seed123
  exp_026_t05_seed456
  exp_026_t08
  exp_026_t08_scierc
  exp_026_t08_seed123
  exp_026_t08_seed456
  exp_026_t10_seed123
  exp_026_t10_seed42
  exp_026_t10_seed456
  exp_026_t12
  exp_026_t12_scierc
  exp_026_t12_seed123
  exp_026_t12_seed456
  exp_027_fewnerd_n16
  exp_027_mlp_verifier
  exp_028
  exp_028_entity_token_lp
  exp_028_fewnerd_5epoch
  exp_029a
  exp_029b
  exp_030_conll_t12
  exp_031_fewnerd_t12
  exp_14b_inference_conll
  exp_14b_inference_fewnerd
  exp_14b_inference_scierc
  exp_32b_inference_fewnerd
  exp_a2_humaneval_sc
  exp_a3_ace05_re
  exp_adaptive_temperature
  exp_asb_adaptive_budget
  exp_b1_scd
  exp_b1_scd_conll_control
  exp_b1_scd_fewnerd_curriculum_q
  exp_b1_scd_fewnerd_standard
  exp_b1_scd_threshold_ablation
  exp_b3_prompted_diversity
  exp_b_frontier_sc_fewnerd
  exp_backup1_het_temp
  exp_backup3_distill_verifier
  exp_ccs_selection
  exp_conll_mf4_s123
  exp_conll_mf4_s456
  exp_conll_mf4_v2_s123
  exp_conll_mf4_v2_s42
  exp_conll_mf4_v2_s456
  exp_conll_n16_s123
  exp_conll_n16_s123_v2
  exp_conll_n16_s42
  exp_conll_n16_s456
  exp_conll_n16_s456_v2
  exp_conll_t05_s123
  exp_conll_t05_s42
  exp_conll_t05_s456
  exp_conll_t08_s123
  exp_conll_t08_s456
  exp_conll_t10_s42
  exp_conll_t12_s123
  exp_conll_t12_s456
  exp_conll_t_ablation_t05
  exp_conll_t_ablation_t08
  exp_conll_t_ablation_t12
  exp_cross_model_consistency
  exp_diagnostic_calibration
  exp_docred_re_sc
  exp_e2_pretrained_conll
  exp_e2_pretrained_scierc
  exp_e_theta_adaptive
  exp_entity_consensus
  exp_entity_construction
  exp_entity_token_lp
  exp_epoch_dgs_analysis
  exp_esj_entity_self_judgment
  exp_fewnerd_7b_n16_s42
  exp_fewnerd_mf4_v2_s123
  exp_fewnerd_mf4_v2_s42
  exp_fewnerd_mf4_v2_s456
  exp_fewnerd_mf4v2_s456
  exp_fewnerd_n16_s123
  exp_fewnerd_n16_s42
  exp_fewnerd_n16_s456
  exp_fewnerd_s789_n8
  exp_fewnerd_t05_s123
  exp_fewnerd_t05_s42
  exp_fewnerd_t05_s456
  exp_fewnerd_t08_s123
  exp_fewnerd_t08_s42
  exp_fewnerd_t08_s456
  exp_fewnerd_t12_s123
  exp_fewnerd_t12_s42
  exp_fewnerd_t12_s456
  exp_fewrel_re_sc
  exp_freeform_ablation
  exp_freeform_conll_4seed
  exp_freeform_seed123
  exp_freeform_seed456
  exp_freeform_seed789
  exp_freeform_seed789_v2
  exp_freeform_seed789_v3
  exp_frontier_sc_claude_sonnet4
  exp_frontier_sc_deepseek
  exp_frontier_sc_gemini25pro
  exp_frontier_sc_gpt55_fewnerd_v2
  exp_hidden_state_probe
  exp_hidden_state_probe_fulldata
  exp_llama3b_scierc_ablation
  exp_llama_fewnerd_inference
  exp_llama_fewnerd_lora
  exp_llama_scierc_seed456
  exp_lp_alignment_gating
  exp_lp_scierc_t07
  exp_lp_t07_scierc
  exp_lsc_latent_sc
  exp_mrsc_multi_round
  exp_multi_model_correlation
  exp_qwen25_14b_fewnerd
  exp_qwen25_32b_fewnerd
  exp_qwen25_72b_fewshot
  exp_qwen25_72b_zeroshot
  exp_qwen25_7b_fewnerd
  exp_qwen3_4b_conll_finetune
  exp_qwen3_4b_conll_finetune_resume
  exp_qwen3_4b_conll_merge_inference_v2
  exp_qwen3_4b_conll_scs_inference
  exp_qwen3_4b_conll_scs_inference_v2
  exp_qwen3_4b_scierc_finetune
  exp_qwen3_4b_scierc_finetune_v2
  exp_qwen3_4b_scierc_finetune_v3
  exp_qwen3_4b_scierc_finetune_v4
  exp_qwen3_4b_scierc_merge_inference
  exp_qwen3_4b_scierc_scs_inference
  exp_re_scierc_seed123
  exp_re_scierc_seed456
  exp_scierc_mf4_v2_s123
  exp_scierc_mf4_v2_s42
  exp_scierc_mf4_v2_s456
  exp_scierc_n16_s123
  exp_scierc_n16_s456
  exp_scierc_probe
  exp_scierc_t05_s123
  exp_scierc_t05_s456
  exp_scierc_t08_s123
  exp_scierc_t08_s456
  exp_scierc_t12_s123
  exp_scierc_t12_s456
  exp_selective_prediction
  exp_spider_sc_pilot
  exp_tacred_re_benchmark
  exp_tlow_fewnerd_inference
  exp_vc_lp_cascade_selection
  exp_vc_quartile_analysis
  exp_verbalized_confidence
  exp_wnut17_qwen25_7b
  ft_001
  ft_002
  ft_002_v2
  hidden_state_probe_conll_full
  hidden_state_probe_conll_v2
  mbr_pilot
  mvp_pilot_001
  mvp_pilot_002
  mvp_pilot_003
  mvp_pilot_004
  mvp_pilot_005
Total DONE: 256
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b53f7d00-e03d-4203-a70c-f418b41080e9",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "300fe02b-dcf9-4a73-8cb6-db5acdd88a7d",
  "sourceToolAssistantUUID": "b53f7d00-e03d-4203-a70c-f418b41080e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-21T11:17:27.660Z_

256 DONE experiments. Now let me extract the full details. Let me first look at a few representative experiments to understand what fields are in the spec.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "300fe02b-dcf9-4a73-8cb6-db5acdd88a7d",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFcxJSPYmNQXTnyBREai",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9f507b4-3b26-4b35-8716-22044ab70429",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8WY9koqXr1y9VpYNTxEHq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3571,
      "cache_read_input_tokens": 17696,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3571,
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

_source line 17 · 2026-05-21T11:17:35.333Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JCWQiqYJ5bFegxiwGhMrKr`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a9ed86cb-a33f-4ec8-8078-d4b9402803ce/tool-results && cat mcp-agent-ml-research-read_registry-1779362196402.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# Look at a few representative experiments to understand spec structure\nsamples = ['exp_conll_mf4_v2_s42', 'exp_qwen3_4b_conll_finetune', 'exp_frontier_sc_gpt55_fewnerd_v2', 'ft_001', 'mvp_pilot_001']\nfor s in samples:\n    if s in exps:\n        print(f'=== {s} ===')\n        e = exps[s]\n        print(json.dumps(e, indent=2, ensure_ascii=False)[:3000])\n        print('...')\n        print()\n\" 2>&1 | head -300\n",
  "description": "Examine representative experiment specs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9f507b4-3b26-4b35-8716-22044ab70429",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFcxJSPYmNQXTnyBREai",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b344b19-e7c1-4f1e-a8ac-2771ac18c53b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8WY9koqXr1y9VpYNTxEHq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3571,
      "cache_read_input_tokens": 17696,
      "output_tokens": 408,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3571
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 408,
          "cache_read_input_tokens": 17696,
          "cache_creation_input_tokens": 3571,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3571,
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

_source line 18 · 2026-05-21T11:17:35.459Z_

<details><summary>↩ Tool result · `toolu_01JCWQiqYJ5bFegxiwGhMrKr`</summary>

```text
=== exp_conll_mf4_v2_s42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-21T10:17:06.386Z",
  "updated_at": "2026-05-21T11:14:51.625Z",
  "hypothesis": "MF4 pipeline fix v2: CoNLL N=8 T=1.0 seed=42 using run_mvp_pilot.py (greedy_f1/micro-F1). Third seed completing 3-seed set for statistical power. α_crit noted only 2-seed for CoNLL.",
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=1 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/conll_mf4v2_seed42/",
    "server": "autodl-5090-c",
    "data_path": "data/conll2003/",
    "data_count": 3453,
    "model_name": "qwen3-8b-conll2003-merged",
    "seed": 42,
    "checkpoint_path": "output/conll_mf4v2_seed42/",
    "log_path": "/tmp/exp_conll_mf4_v2_s42.log"
  },
  "conclusion": "success",
  "metrics": {
    "greedy_f1": 0.907,
    "oracle_f1": 0.949,
    "agreement_rho": 0.424,
    "structural_beats_surface": true,
    "verdict": "PASS",
    "samples_count": 3453
  },
  "completed_at": "2026-05-21T10:55:03.879Z"
}
...

=== exp_qwen3_4b_conll_finetune ===
{
  "status": "DONE",
  "retry_count": 1,
  "created_at": "2026-05-15T17:18:35.501Z",
  "updated_at": "2026-05-15T19:10:24.822Z",
  "hypothesis": "Scale ablation: Qwen3-4B CoNLL NER LoRA fine-tune to provide cross-scale evidence (vs 8B). Verify correlation-selection gap, SJ>FK ordering, and LP compression generalize across model scale.",
  "reproduce": {
    "finished_at": "2026-05-15T18:45:42.215Z"
  },
  "failure_reason": "",
  "completed_at": "2026-05-15T18:45:43.672Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-15T18:45:49.686191+00:00"
      }
    ],
    "previous_failure": {
      "conclusion": "failed"
    }
  },
  "spec": {
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli train train_config_conll2003_4b.yaml",
    "server": "autodl-5090",
    "gpu": [
      "cuda:0"
    ],
    "data_path": "data/conll2003",
    "data_count": 14041,
    "model_name": "Qwen3-4B",
    "seed": 42,
    "plan_id": "D096",
    "log_path": "checkpoints/qwen3-4b-conll2003-lora/trainer_log.jsonl",
    "checkpoint_path": "/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora",
    "lora_config": {
      "trainable_params": "66M / 4.09B (1.62%)",
      "target_modules": "q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj",
      "epochs": 5,
      "batch_size": 16,
      "total_steps": 4390,
      "enable_thinking": false
    }
  },
  "conclusion": "success",
  "notes": "Training stopped at step 3920/4390 (89.3%, epoch 4.46/5). No error log or tmux session found. checkpoint-3800 is valid (adapter_model.safetensors 264MB, eval_loss=0.023). Proceeding with checkpoint-3800 for merge+inference.",
  "metrics": {
    "final_loss": 0.0086,
    "total_steps_completed": 3920,
    "total_steps_target": 4390,
    "epochs_completed": 4.46,
    "epochs_target": 5,
    "best_checkpoint": "checkpoint-3800",
    "note": "Training stopped at 89.3% completion (no error log found). Using checkpoint-3800 (loss ~0.01) for merge."
  }
}
...

=== exp_frontier_sc_gpt55_fewnerd_v2 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-21T04:48:24.698Z",
  "updated_at": "2026-05-21T08:36:36.829Z",
  "hypothesis": "Frontier model GPT-5.5 on FewNERD SC (200 instances, N=8, T=1.0): if correlation-selection gap persists in frontier models, the finding is fundamental and not a model capability limitation. Previous attempt failed due to API credit exhaustion.",
  "parent": "exp_b_frontier_sc_fewnerd",
  "spec": {
    "command": "python -u code/run_frontier_sc.py --model gpt-5.5 --base_url http://47.94.22.126/v1 --n_instances 200 --n_samples 8 --temperature 1.0 --seed 42 --max_workers 4",
    "server": "autodl-5090-c",
    "data_path": "data/fewnerd/test.json",
    "data_count": 200,
    "model_name": "gpt-5.5",
    "seed": 42,
    "checkpoint_source": "openai/gpt-5.5 (API)",
    "eval_data": "fewnerd test set (200 instances)",
    "checkpoint_path": "/root/autodl-tmp/struct_self_consist_ie/output/frontier_sc_gpt55_fewnerd_v2/",
    "log_path": "/root/autodl-tmp/struct_self_consist_ie/logs/frontier_sc_gpt55_fewnerd_v2.log"
  },
  "conclusion": "success",
  "metrics": {
    "greedy_f1": 0.6382,
    "mv_f1": 0.6521,
    "oracle_f1": 0.7203,
    "degeneracy_rate": 0.5,
    "rho_agreement": 0.3551,
    "rho_fk": 0.3515,
    "rho_sj": 0.3461,
    "instances": 200
  },
  "completed_at": "2026-05-21T08:36:36.829Z"
}
...

=== ft_001 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T06:04:28.030Z",
  "updated_at": "2026-05-14T08:27:58.182Z",
  "spec": {
    "hypothesis": "Fine-tuned Qwen3-8B on SciERC UIE can achieve NER F1 >= 73 and serve as base model for structural consistency MVP",
    "model_name": "Qwen/Qwen3-8B",
    "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/scierc",
    "data_count": 1861,
    "server": "autodl-5090",
    "seed": 42,
    "method": "LoRA r=16 alpha=32",
    "framework": "LLaMA Factory 0.9.4",
    "command": "sft training qwen3-8b on scierc with lora",
    "checkpoint_path": "/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora/",
    "log_path": "/root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_001_train.log",
    "train_loss": 0.1099,
    "eval_loss": 0.0771,
    "epoch": 3,
    "train_runtime": "0:17:49",
    "note": "gate0: NER PASS 60.4% / RE FAIL 33.8%"
  },
  "conclusion": "success",
  "completed_at": "2026-05-14T06:30:32.889Z",
  "metrics": {
    "train_loss": 0.1099,
    "eval_loss": 0.0771,
    "gate0_ner_f1_strict": 0.1143,
    "gate0_re_f1_strict": 0.0125,
    "gate0_ner_f1_text": 0.606,
    "gate0_re_f1_text": 0.3392,
    "gate0_offset_accuracy": 0.1665,
    "gate0_parse_failures": 43,
    "gate0_pass": false,
    "gate0_realigned_ner_f1": 0.6045,
    "gate0_realigned_re_f1": 0.338,
    "gate0_realigned_entity_offset_accuracy": 1,
    "gate0_realigned_relation_offset_accuracy": 1,
    "gate0_realigned_ner_pass": true,
    "gate0_realigned_re_pass": false,
    "gate0_realigned_pass": false,
    "gate0_ner_f1_delta_realign": 0.4901,
    "gate0_re_f1_delta_realign": 0.3255,
    "verdict_note": "partial: NER PASS (60.4%) / RE FAIL (33.8% < 40%)"
  }
}
...

=== mvp_pilot_001 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T07:39:16.313Z",
  "updated_at": "2026-05-14T08:05:34.348Z",
  "spec": {
    "hypothesis": "Structural self-consistency (soft Jaccard) correlates with per-instance F1 better than surface Fleiss Kappa on fine-tuned Qwen3-8B SciERC",
    "model_name": "qwen3-8b-scierc-merged",
    "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/test.jsonl",
    "data_count": 551,
    "server": "autodl-5090",
    "seed": 42,
    "parent": "ft_001",
    "method": "N=8 sampling T=1.0 + XGrammar + span realignment",
    "command": "CUDA_VISIBLE_DEVICES=0 python3 code/mvp_pilot.py",
    "checkpoint_path": "/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged",
    "log_path": "/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_001.log"
  },
  "conclusion": "negative",
  "completed_at": "2026-05-14T07:52:47.006Z",
  "metrics": {
    "ner_greedy_f1": 0.611,
    "ner_oracle_f1": 0.78,
    "ner_headroom": 0.169,
    "ner_fleiss_kappa_mean": 0.2449,
    "ner_soft_jaccard_mean": 0.5041,
    "ner_full_rho_sj": 0.3616,
    "ner_full_rho_fk": 0.3515,
    "ner_full_n": 529,
    "ner_cond_rho_sj": 0.3688,
    "ner_cond_rho_fk": 0.3569,
    "ner_cond_n": 510,
    "ner_sj_beats_fk_full": true,
    "ner_sj_beats_fk_cond": true,
    "ner_sample_f1_pct_zero": 20.4,
    "ner_gold_empty_filtered": 22,
    "ner_all_zero_filtered": 19,
    "re_greedy_f1": 0.355,
    "re_oracle_f1": 0.572,
    "re_headroom": 0.217,
    "re_fleiss_kappa_mean": 0.0681,
    "re_soft_jaccard_mean": 0.3635,
    "re_full_rho_sj": 0.2535,
    "re_full_rho_fk": 0.2885,
    "re_full_n": 397,
    "re_cond_rho_sj": 0.3515,
    "re_cond_rho_fk": 0.3107,
    "re_cond_n": 320,
    "re_sj_beats_fk_full": false,
    "re_sj_beats_fk_cond": true,
    "re_sample_f1_pct_zero": 58.3,
    "re_gold_empty_filtered": 154,
    "re_all_zero_filtered": 77,
    "parse_failures_stochastic": 164,
    "parse_failures_greedy": 29,
    "total_stochastic_samples": 4408,
    "total_greedy": 551,
    "verdict": "FAIL",
    "verdict_reason": "RE full rho_sj=0.2535 < 0.40; SJ does not beat FK on RE full set"
  }
}
...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b344b19-e7c1-4f1e-a8ac-2771ac18c53b",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "744b2ebe-eab6-4e33-9dfe-68e80516b017",
  "sourceToolAssistantUUID": "2b344b19-e7c1-4f1e-a8ac-2771ac18c53b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-21T11:17:40.188Z_

Good. Now I can see the structure varies. Let me now extract all hyperparameters systematically from all 256 experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "744b2ebe-eab6-4e33-9dfe-68e80516b017",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFcyEmfBb2KRJ2w6mUXf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a64b9ab-0469-47ea-a80a-e47b2c5883a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013HXn6k91nqdKVzqiBJBCd8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4395,
      "cache_read_input_tokens": 21267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4395,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T11:17:48.230Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01M8765TT5mQvhgwxk5t2SRo`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a9ed86cb-a33f-4ec8-8078-d4b9402803ce/tool-results && cat mcp-agent-ml-research-read_registry-1779362196402.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# Dump all experiments to a temp file for easier processing\nwith open('/tmp/all_exps.json', 'w') as f:\n    json.dump(exps, f, indent=2, ensure_ascii=False)\nprint('Dumped to /tmp/all_exps.json')\nprint(f'Total: {len(exps)} experiments')\n\"\n",
  "description": "Dump experiments to temp file for processing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a64b9ab-0469-47ea-a80a-e47b2c5883a1",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFcyEmfBb2KRJ2w6mUXf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d42b4ac-6409-43b6-809f-11c6ecc28000",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013HXn6k91nqdKVzqiBJBCd8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4395,
      "cache_read_input_tokens": 21267,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4395
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 330,
          "cache_read_input_tokens": 21267,
          "cache_creation_input_tokens": 4395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4395,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T11:17:48.334Z_

<details><summary>↩ Tool result · `toolu_01M8765TT5mQvhgwxk5t2SRo`</summary>

```text
Dumped to /tmp/all_exps.json
Total: 256 experiments
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d42b4ac-6409-43b6-809f-11c6ecc28000",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "6929d5dc-da33-4e5e-9987-58f5057de708",
  "sourceToolAssistantUUID": "8d42b4ac-6409-43b6-809f-11c6ecc28000",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T11:18:01.387Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DfLckviz3sTr8j6A3ZxT8X`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\n\nwith open('/tmp/all_exps.json') as f:\n    exps = json.load(f)\n\n# Categorize experiments\nfinetune_exps = {}\ninference_exps = {}\napi_exps = {}\nother_exps = {}\n\napi_models = ['gpt-5.5', 'gpt-4o', 'claude', 'gemini', 'deepseek', 'claude-sonnet', 'claude-sonnet-4']\nfinetune_keywords = ['finetune', 'fine-tune', 'fine_tune', 'lora', 'sft', 'train', 'ft_']\n\nfor eid, e in exps.items():\n    spec = e.get('spec', {})\n    model = spec.get('model_name', '') or ''\n    command = spec.get('command', '') or ''\n    hypothesis = e.get('hypothesis', '') or spec.get('hypothesis', '') or ''\n    \n    model_lower = model.lower()\n    cmd_lower = command.lower()\n    eid_lower = eid.lower()\n    hyp_lower = hypothesis.lower()\n    \n    # Check if API-based\n    is_api = any(am in model_lower for am in api_models) or \\\n             'api' in cmd_lower or \\\n             'frontier' in eid_lower or \\\n             'base_url' in command or \\\n             any(am in model_lower for am in ['gpt', 'claude', 'gemini', 'deepseek-v3', 'deepseek-r1'])\n    \n    # Check if fine-tuning\n    is_finetune = any(kw in eid_lower for kw in finetune_keywords) or \\\n                  any(kw in cmd_lower for kw in ['llamafactory', 'train', 'sft']) or \\\n                  'lora_config' in spec or \\\n                  'method' in spec and 'lora' in str(spec.get('method', '')).lower()\n    \n    if is_api:\n        api_exps[eid] = e\n    elif is_finetune:\n        finetune_exps[eid] = e\n    else:\n        inference_exps[eid] = e\n\nprint(f\"Fine-tuning experiments: {len(finetune_exps)}\")\nprint(f\"Inference/evaluation experiments: {len(inference_exps)}\")\nprint(f\"API-based model experiments: {len(api_exps)}\")\nprint()\n\n# List each category\nprint(\"=== FINE-TUNING EXPERIMENTS ===\")\nfor eid in sorted(finetune_exps.keys()):\n    print(f\"  {eid}\")\nprint()\nprint(\"=== API-BASED MODEL EXPERIMENTS ===\")\nfor eid in sorted(api_exps.keys()):\n    print(f\"  {eid}\")\nprint()\nprint(\"=== INFERENCE/EVALUATION EXPERIMENTS ===\")\nfor eid in sorted(inference_exps.keys()):\n    print(f\"  {eid}\")\nPYEOF\n",
  "description": "Categorize all experiments into fine-tuning, inference, and API-based"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6929d5dc-da33-4e5e-9987-58f5057de708",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFczBk7eJ8r1So7LbQ8T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "439b5766-3fdc-4d5b-8281-ad0b5641cbb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PrBgnsGBWjzJbrSgdhgRWR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 362,
      "cache_read_input_tokens": 25662,
      "output_tokens": 862,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 362
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 862,
          "cache_read_input_tokens": 25662,
          "cache_creation_input_tokens": 362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 362,
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

_source line 23 · 2026-05-21T11:18:01.480Z_

<details><summary>↩ Tool result · `toolu_01DfLckviz3sTr8j6A3ZxT8X`</summary>

```text
Fine-tuning experiments: 30
Inference/evaluation experiments: 219
API-based model experiments: 7

=== FINE-TUNING EXPERIMENTS ===
  exp_002_merge_conll2003
  exp_003_wnut17_v2
  exp_007_ner_multi_model
  exp_017_llama_conll_finetune
  exp_023_lora_rank8
  exp_027_mlp_verifier
  exp_028
  exp_028_fewnerd_5epoch
  exp_029a
  exp_029b
  exp_b1_scd_conll_control
  exp_b1_scd_fewnerd_curriculum_q
  exp_b1_scd_fewnerd_standard
  exp_b1_scd_threshold_ablation
  exp_e2_pretrained_conll
  exp_e2_pretrained_scierc
  exp_llama_fewnerd_lora
  exp_qwen25_14b_fewnerd
  exp_qwen25_32b_fewnerd
  exp_qwen25_7b_fewnerd
  exp_qwen3_4b_conll_finetune
  exp_qwen3_4b_conll_finetune_resume
  exp_qwen3_4b_scierc_finetune
  exp_qwen3_4b_scierc_finetune_v2
  exp_qwen3_4b_scierc_finetune_v3
  exp_qwen3_4b_scierc_finetune_v4
  exp_wnut17_qwen25_7b
  ft_001
  ft_002
  ft_002_v2

=== API-BASED MODEL EXPERIMENTS ===
  exp_a2_humaneval_sc
  exp_b_frontier_sc_fewnerd
  exp_frontier_sc_claude_sonnet4
  exp_frontier_sc_deepseek
  exp_frontier_sc_gemini25pro
  exp_frontier_sc_gpt55_fewnerd_v2
  exp_spider_sc_pilot

=== INFERENCE/EVALUATION EXPERIMENTS ===
  dgs_pilot
  e1_component_wise_re_sj
  exp001_seed123
  exp001_seed456
  exp008_re_n16
  exp_001_n16_seed123
  exp_001_n16_seed123_full
  exp_001_n16_seed456
  exp_001_n16_seed456_full
  exp_001_ner_n16_scierc
  exp_001_ner_n16_seed123
  exp_001_seed123_t10_full
  exp_001_seed123_v2
  exp_001_seed123_v2_r1024
  exp_001_seed42_v2
  exp_001_seed42_v2_r1024
  exp_001_seed456_t10_full
  exp_001_seed456_v2
  exp_001_seed456_v2_ner
  exp_001_seed456_v2_ner_r1024
  exp_002
  exp_002_conll_n16
  exp_002_conll_n16_r1024
  exp_002_conll_n16_seed123
  exp_002_conll_n16_seed456
  exp_002_ner_conll2003
  exp_003_ner_wnut17
  exp_003_wnut17_eval
  exp_004_re_diagnostic
  exp_004_v2
  exp_005
  exp_005_v2
  exp_006_v2
  exp_007_llama_inference
  exp_007_llama_n16
  exp_007_llama_n16_r1024
  exp_007_llama_scierc_seed123
  exp_007_llama_seed123
  exp_007_llama_seed456
  exp_007_ner_llama
  exp_008_re_n16
  exp_008_re_n16_full
  exp_008_re_n16_t10_full
  exp_008_re_n16_v2
  exp_008_re_seed123
  exp_009_capability_stratification
  exp_009_v2
  exp_009_v2_re_rerun
  exp_010_selection_curves
  exp_011_ood_conll_to_scierc
  exp_011_ood_scierc_to_conll
  exp_012_logprob_baseline
  exp_012_rerun_1024
  exp_013_exact_match_voting
  exp_014_entity_majority_voting
  exp_015_metrics_expansion
  exp_015_v2
  exp_016_rerun_1024_bootstrap
  exp_016_signal_ensemble
  exp_016_v2
  exp_017_llama_conll
  exp_017_llama_conll_infer
  exp_017_llama_conll_n16
  exp_017_llama_conll_n16_r1024
  exp_017_llama_conll_n16_s123
  exp_017_llama_conll_n16_s123_r1024
  exp_017_llama_conll_n16_s456
  exp_017_llama_conll_n16_s456_r1024
  exp_017_llama_conll_n8_t07
  exp_018_llama_scierc_seed123
  exp_018_llama_scierc_seed42_r1024
  exp_018_llama_scierc_seed456
  exp_018_llama_scierc_seed456_r1024
  exp_018_qwen_scierc_seed123
  exp_018_qwen_scierc_seed456
  exp_019_supervised_verifier
  exp_020_fewnerd_smoke
  exp_021_fewnerd_full
  exp_021_fewnerd_n8_seed123
  exp_021_fewnerd_n8_seed456
  exp_022_seed789
  exp_024_claim_audit
  exp_025_n32
  exp_026_T05
  exp_026_T08
  exp_026_T12
  exp_026_t05
  exp_026_t05_scierc
  exp_026_t05_seed123
  exp_026_t05_seed456
  exp_026_t08
  exp_026_t08_scierc
  exp_026_t08_seed123
  exp_026_t08_seed456
  exp_026_t10_seed123
  exp_026_t10_seed42
  exp_026_t10_seed456
  exp_026_t12
  exp_026_t12_scierc
  exp_026_t12_seed123
  exp_026_t12_seed456
  exp_027_fewnerd_n16
  exp_028_entity_token_lp
  exp_030_conll_t12
  exp_031_fewnerd_t12
  exp_14b_inference_conll
  exp_14b_inference_fewnerd
  exp_14b_inference_scierc
  exp_32b_inference_fewnerd
  exp_a3_ace05_re
  exp_adaptive_temperature
  exp_asb_adaptive_budget
  exp_b1_scd
  exp_b3_prompted_diversity
  exp_backup1_het_temp
  exp_backup3_distill_verifier
  exp_ccs_selection
  exp_conll_mf4_s123
  exp_conll_mf4_s456
  exp_conll_mf4_v2_s123
  exp_conll_mf4_v2_s42
  exp_conll_mf4_v2_s456
  exp_conll_n16_s123
  exp_conll_n16_s123_v2
  exp_conll_n16_s42
  exp_conll_n16_s456
  exp_conll_n16_s456_v2
  exp_conll_t05_s123
  exp_conll_t05_s42
  exp_conll_t05_s456
  exp_conll_t08_s123
  exp_conll_t08_s456
  exp_conll_t10_s42
  exp_conll_t12_s123
  exp_conll_t12_s456
  exp_conll_t_ablation_t05
  exp_conll_t_ablation_t08
  exp_conll_t_ablation_t12
  exp_cross_model_consistency
  exp_diagnostic_calibration
  exp_docred_re_sc
  exp_e_theta_adaptive
  exp_entity_consensus
  exp_entity_construction
  exp_entity_token_lp
  exp_epoch_dgs_analysis
  exp_esj_entity_self_judgment
  exp_fewnerd_7b_n16_s42
  exp_fewnerd_mf4_v2_s123
  exp_fewnerd_mf4_v2_s42
  exp_fewnerd_mf4_v2_s456
  exp_fewnerd_mf4v2_s456
  exp_fewnerd_n16_s123
  exp_fewnerd_n16_s42
  exp_fewnerd_n16_s456
  exp_fewnerd_s789_n8
  exp_fewnerd_t05_s123
  exp_fewnerd_t05_s42
  exp_fewnerd_t05_s456
  exp_fewnerd_t08_s123
  exp_fewnerd_t08_s42
  exp_fewnerd_t08_s456
  exp_fewnerd_t12_s123
  exp_fewnerd_t12_s42
  exp_fewnerd_t12_s456
  exp_fewrel_re_sc
  exp_freeform_ablation
  exp_freeform_conll_4seed
  exp_freeform_seed123
  exp_freeform_seed456
  exp_freeform_seed789
  exp_freeform_seed789_v2
  exp_freeform_seed789_v3
  exp_hidden_state_probe
  exp_hidden_state_probe_fulldata
  exp_llama3b_scierc_ablation
  exp_llama_fewnerd_inference
  exp_llama_scierc_seed456
  exp_lp_alignment_gating
  exp_lp_scierc_t07
  exp_lp_t07_scierc
  exp_lsc_latent_sc
  exp_mrsc_multi_round
  exp_multi_model_correlation
  exp_qwen25_72b_fewshot
  exp_qwen25_72b_zeroshot
  exp_qwen3_4b_conll_merge_inference_v2
  exp_qwen3_4b_conll_scs_inference
  exp_qwen3_4b_conll_scs_inference_v2
  exp_qwen3_4b_scierc_merge_inference
  exp_qwen3_4b_scierc_scs_inference
  exp_re_scierc_seed123
  exp_re_scierc_seed456
  exp_scierc_mf4_v2_s123
  exp_scierc_mf4_v2_s42
  exp_scierc_mf4_v2_s456
  exp_scierc_n16_s123
  exp_scierc_n16_s456
  exp_scierc_probe
  exp_scierc_t05_s123
  exp_scierc_t05_s456
  exp_scierc_t08_s123
  exp_scierc_t08_s456
  exp_scierc_t12_s123
  exp_scierc_t12_s456
  exp_selective_prediction
  exp_tacred_re_benchmark
  exp_tlow_fewnerd_inference
  exp_vc_lp_cascade_selection
  exp_vc_quartile_analysis
  exp_verbalized_confidence
  hidden_state_probe_conll_full
  hidden_state_probe_conll_v2
  mbr_pilot
  mvp_pilot_001
  mvp_pilot_002
  mvp_pilot_003
  mvp_pilot_004
  mvp_pilot_005
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "439b5766-3fdc-4d5b-8281-ad0b5641cbb8",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "de140c49-8c0f-4eed-93f4-0d47f9b564f7",
  "sourceToolAssistantUUID": "439b5766-3fdc-4d5b-8281-ad0b5641cbb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-21T11:18:04.811Z_

Now let me extract detailed hyperparameters from each category.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de140c49-8c0f-4eed-93f4-0d47f9b564f7",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFd19zyN9ASwg4PMbc22",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eab97fc5-0220-41be-8661-6131b6ff38a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SWmGpNwrmTAqnhzgEjkyGk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4060,
      "cache_read_input_tokens": 26024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4060,
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

_source line 25 · 2026-05-21T11:18:23.116Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011jaroMZk2EgYDjDAJp42t4`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\n\nwith open('/tmp/all_exps.json') as f:\n    exps = json.load(f)\n\n# ============================================================\n# PART 1: FINE-TUNING EXPERIMENTS - Full detail extraction\n# ============================================================\nfinetune_ids = [\n    'ft_001', 'ft_002', 'ft_002_v2',\n    'exp_002_merge_conll2003', 'exp_003_wnut17_v2', 'exp_007_ner_multi_model',\n    'exp_017_llama_conll_finetune', 'exp_023_lora_rank8',\n    'exp_027_mlp_verifier', 'exp_028', 'exp_028_fewnerd_5epoch',\n    'exp_029a', 'exp_029b',\n    'exp_b1_scd_conll_control', 'exp_b1_scd_fewnerd_curriculum_q',\n    'exp_b1_scd_fewnerd_standard', 'exp_b1_scd_threshold_ablation',\n    'exp_e2_pretrained_conll', 'exp_e2_pretrained_scierc',\n    'exp_llama_fewnerd_lora',\n    'exp_qwen25_14b_fewnerd', 'exp_qwen25_32b_fewnerd', 'exp_qwen25_7b_fewnerd',\n    'exp_qwen3_4b_conll_finetune', 'exp_qwen3_4b_conll_finetune_resume',\n    'exp_qwen3_4b_scierc_finetune', 'exp_qwen3_4b_scierc_finetune_v2',\n    'exp_qwen3_4b_scierc_finetune_v3', 'exp_qwen3_4b_scierc_finetune_v4',\n    'exp_wnut17_qwen25_7b',\n]\n\nprint(\"=\" * 100)\nprint(\"CATEGORY 1: FINE-TUNING EXPERIMENTS\")\nprint(\"=\" * 100)\n\nfor eid in sorted(finetune_ids):\n    e = exps[eid]\n    spec = e.get('spec', {})\n    print(f\"\\n{'─' * 80}\")\n    print(f\"ID: {eid}\")\n    print(f\"Status: {e.get('status')}\")\n    print(f\"Conclusion: {e.get('conclusion')}\")\n    print(f\"Created: {e.get('created_at')}\")\n    print(f\"Completed: {e.get('completed_at')}\")\n    \n    # Hypothesis\n    hyp = e.get('hypothesis') or spec.get('hypothesis') or ''\n    if hyp:\n        print(f\"Hypothesis: {hyp}\")\n    \n    # Model\n    print(f\"Model: {spec.get('model_name', 'NOT SPECIFIED')}\")\n    \n    # Server / GPU\n    print(f\"Server: {spec.get('server', 'NOT SPECIFIED')}\")\n    gpu = spec.get('gpu', 'NOT SPECIFIED')\n    print(f\"GPU: {gpu}\")\n    \n    # Data\n    print(f\"Data path: {spec.get('data_path', 'NOT SPECIFIED')}\")\n    print(f\"Data count: {spec.get('data_count', 'NOT SPECIFIED')}\")\n    \n    # Seed\n    print(f\"Seed: {spec.get('seed', 'NOT SPECIFIED')}\")\n    \n    # LoRA config\n    lora = spec.get('lora_config', {})\n    method = spec.get('method', '')\n    if lora:\n        print(f\"LoRA config:\")\n        for lk, lv in lora.items():\n            print(f\"  {lk}: {lv}\")\n    elif method:\n        print(f\"Method: {method}\")\n    \n    # Framework\n    framework = spec.get('framework', '')\n    if framework:\n        print(f\"Framework: {framework}\")\n    \n    # Training details from spec\n    for key in ['epoch', 'epochs', 'learning_rate', 'lr', 'batch_size', 'optimizer',\n                 'train_loss', 'eval_loss', 'train_runtime', 'total_steps',\n                 'checkpoint_path', 'log_path', 'plan_id', 'note', 'notes']:\n        val = spec.get(key)\n        if val is not None:\n            print(f\"{key}: {val}\")\n    \n    # Notes at top level\n    notes = e.get('notes', '')\n    if notes:\n        print(f\"Notes: {notes}\")\n    \n    # Command\n    cmd = spec.get('command', '')\n    if cmd:\n        print(f\"Command: {cmd[:300]}\")\n    \n    # Metrics summary\n    metrics = e.get('metrics', {})\n    if metrics:\n        print(f\"Metrics: {json.dumps(metrics, ensure_ascii=False)}\")\n\nPYEOF\n",
  "description": "Extract detailed hyperparameters from fine-tuning experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eab97fc5-0220-41be-8661-6131b6ff38a4",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFd19zyN9ASwg4PMbc22",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3b6fe9a-669a-42f6-b7aa-fc665f77b30c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SWmGpNwrmTAqnhzgEjkyGk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4060,
      "cache_read_input_tokens": 26024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4060,
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

### Tool result

_source line 26 · 2026-05-21T11:18:23.251Z_

<details><summary>↩ Tool result · `toolu_011jaroMZk2EgYDjDAJp42t4`</summary>

```text
&lt;persisted-output>
Output too large (40.1KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a9ed86cb-a33f-4ec8-8078-d4b9402803ce/tool-results/b29ao5x82.txt

Preview (first 2KB):
====================================================================================================
CATEGORY 1: FINE-TUNING EXPERIMENTS
====================================================================================================

────────────────────────────────────────────────────────────────────────────────
ID: exp_002_merge_conll2003
Status: DONE
Conclusion: killed
Created: 2026-05-14T12:25:56.211Z
Completed: 2026-05-15T12:41:26.419Z
Model: NOT SPECIFIED
Server: autodl-5090
GPU: ['cuda:0']
Data path: NOT SPECIFIED
Data count: NOT SPECIFIED
Seed: NOT SPECIFIED
log_path: ~/runs/struct_self_consist_ie/exp_002_merge_conll2003.log
Notes: Completed as exp_002_conll_n16 on autodl-5090. Registry status corrected.
Command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli export export_config_conll2003.yaml > /tmp/merge_conll2003.log 2>&1 && echo 'MERGE_DONE' >> /tmp/merge_conll2003.log"

────────────────────────────────────────────────────────────────────────────────
ID: exp_003_wnut17_v2
Status: DONE
Conclusion: negative
Created: 2026-05-14T15:32:56.415Z
Completed: 2026-05-14T18:11:36.559Z
Hypothesis: WNUT-17 NER evaluation v2: tests signal effectiveness on noisy social media text. Hypothesis: structural signals remain effective on noisy, informal text with high entity variation.
Model: Qwen3-8B
Server: autodl-5090
GPU: NOT SPECIFIED
Data path: /root/autodl-tmp/struct_self_consist_ie/data/wnut17/llmfactory_train_downsampled.json
Data count: 1637
Seed: 42
checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-lora
log_path: /root/autodl-tmp/struct_self_consist_ie/logs/train_wnut17.log
plan_id: exp-003
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3b6fe9a-669a-42f6-b7aa-fc665f77b30c",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "eb88fabf-4e13-400e-9f91-1fbfdaa2f47e",
  "sourceToolAssistantUUID": "f3b6fe9a-669a-42f6-b7aa-fc665f77b30c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T11:18:26.401Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QjFm7Ss9kXrxot5nKmmqie`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a9ed86cb-a33f-4ec8-8078-d4b9402803ce/tool-results/b29ao5x82.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb88fabf-4e13-400e-9f91-1fbfdaa2f47e",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFd2m2ugg7JSxXZ15Wxy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58f4a557-04b1-4b0d-b9a7-3fc1ceea6f4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1UykP1AGCMaYKgEgMeZSs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2112,
      "cache_read_input_tokens": 30084,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2112
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 30084,
          "cache_creation_input_tokens": 2112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2112,
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

_source line 28 · 2026-05-21T11:18:26.768Z_

<details><summary>↩ Tool result · `toolu_01QjFm7Ss9kXrxot5nKmmqie`</summary>

```text
1	====================================================================================================
2	CATEGORY 1: FINE-TUNING EXPERIMENTS
3	====================================================================================================
4	
5	────────────────────────────────────────────────────────────────────────────────
6	ID: exp_002_merge_conll2003
7	Status: DONE
8	Conclusion: killed
9	Created: 2026-05-14T12:25:56.211Z
10	Completed: 2026-05-15T12:41:26.419Z
11	Model: NOT SPECIFIED
12	Server: autodl-5090
13	GPU: ['cuda:0']
14	Data path: NOT SPECIFIED
15	Data count: NOT SPECIFIED
16	Seed: NOT SPECIFIED
17	log_path: ~/runs/struct_self_consist_ie/exp_002_merge_conll2003.log
18	Notes: Completed as exp_002_conll_n16 on autodl-5090. Registry status corrected.
19	Command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli export export_config_conll2003.yaml > /tmp/merge_conll2003.log 2>&1 && echo 'MERGE_DONE' >> /tmp/merge_conll2003.log"
20	
21	────────────────────────────────────────────────────────────────────────────────
22	ID: exp_003_wnut17_v2
23	Status: DONE
24	Conclusion: negative
25	Created: 2026-05-14T15:32:56.415Z
26	Completed: 2026-05-14T18:11:36.559Z
27	Hypothesis: WNUT-17 NER evaluation v2: tests signal effectiveness on noisy social media text. Hypothesis: structural signals remain effective on noisy, informal text with high entity variation.
28	Model: Qwen3-8B
29	Server: autodl-5090
30	GPU: NOT SPECIFIED
31	Data path: /root/autodl-tmp/struct_self_consist_ie/data/wnut17/llmfactory_train_downsampled.json
32	Data count: 1637
33	Seed: 42
34	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-lora
35	log_path: /root/autodl-tmp/struct_self_consist_ie/logs/train_wnut17.log
36	plan_id: exp-003
37	note: D045: Training succeeded (train_loss=0.105) but inference FAIL: 54% F1=0, SJ rho=0.062 (p=0.106). WNUT-17 abandoned — model capability insufficient on social media NER. Paper reports as Claim 3 (capability boundary) evidence.
38	Command: CUDA_VISIBLE_DEVICES=1 llamafactory-cli train train_config_wnut17.yaml
39	
40	────────────────────────────────────────────────────────────────────────────────
41	ID: exp_007_ner_multi_model
42	Status: DONE
43	Conclusion: success
44	Created: 2026-05-14T11:42:20.748Z
45	Completed: 2026-05-14T12:45:54.952Z
46	Hypothesis: Multi-model NER comparison: evaluates signal effectiveness across Qwen and LLaMA on SciERC NER. Establishes cross-model generalization of structural>surface ranking.
47	Model: LLaMA-3.1-8B-Instruct
48	Server: gpu-5090-4x-2
49	GPU: ['cuda:0']
50	Data path: /root/autodl-tmp/struct_self_consist_ie/data
51	Data count: 1861
52	Seed: 42
53	log_path: ~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log
54	Command: bash -c 'source env.sh && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_llama.yaml'
55	Metrics: {"epoch": 5, "train_loss": 0.0767, "eval_loss": 0.1049, "train_runtime_sec": 1494.5, "train_samples_per_second": 6.226, "checkpoints": ["checkpoint-400", "checkpoint-500", "checkpoint-585"], "base_model": "Meta-Llama-3.1-8B-Instruct", "lora_r": 32, "lora_alpha": 64, "note": "EXIT_CODE=129 (SIGHUP) but training completed all 5 epochs before signal. Checkpoint fully intact."}
56	
57	────────────────────────────────────────────────────────────────────────────────
58	ID: exp_017_llama_conll_finetune
59	Status: DONE
60	Conclusion: success
61	Created: 2026-05-18T16:47:36.156Z
62	Completed: 2026-05-18T18:30:32.331Z
63	Hypothesis: Structural self-consistency QE signals (SJ, FK, VC, EM) show model-agnostic diagnostic power: their Spearman rho with per-instance F1 should be comparable on LLaMA 3.1-8B as on Qwen 2.5-7B for CoNLL-2003 NER, even though degeneracy rates and absolute F1 may differ.
64	Model: Meta-Llama-3.1-8B-Instruct
65	Server: autodl-5090
66	GPU: ['cuda:0']
67	Data path: /root/autodl-tmp/struct_self_consist_ie/data/conll2003/llmfactory_train.json
68	Data count: 14037
69	Seed: 42
70	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-conll2003-lora-3ep
71	log_path: ~/runs/struct_self_consist_ie/exp_017_llama_conll_finetune.log
72	Command: bash -c "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli train train_config_llama_conll2003_3ep.yaml"
73	Metrics: {"degeneracy_rate": 0.853, "greedy_f1": 0.928, "oracle_f1": 0.951, "headroom": 0.023, "selection_f1": 0.934, "full_rho_SJ": 0.45, "full_rho_FK": 0.443, "full_rho_VC": 0.437, "full_rho_EM": 0.448, "full_rho_LP": 0.273, "full_AUROC_SJ": 0.752, "full_AUROC_EM": 0.753, "full_AUROC_LP": 0.739, "cond_rho_SJ": 0.454, "cond_rho_EM": 0.458, "cond_rho_LP": 0.311, "cond_AUROC_EM": 0.783, "cond_AUROC_LP": 0.804}
74	
75	────────────────────────────────────────────────────────────────────────────────
76	ID: exp_023_lora_rank8
77	Status: DONE
78	Conclusion: success
79	Created: 2026-05-16T10:29:59.501Z
80	Completed: 2026-05-16T11:22:34.576Z
81	Hypothesis: LoRA rank=8 ablation on SciERC: test if reduced model capacity (rank 8 vs 32) changes signal effectiveness ranking or correlation-selection gap pattern. Verifies findings are not rank-specific artifacts.
82	Model: Qwen/Qwen3-8B
83	Server: autodl-5090
84	GPU: cuda:2
85	Data path: /root/autodl-tmp/struct_self_consist_ie/data/llmfactory_train.json
86	Data count: 1861
87	Seed: 42
88	Method: LoRA r=8 alpha=16, 5 epochs, batch=2 grad_accum=8 gradient_checkpointing=true
89	total_steps: 585
90	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-rank8
91	log_path: /root/autodl-tmp/struct_self_consist_ie/logs/exp023_rank8_train.log
92	Command: CUDA_VISIBLE_DEVICES=2 llamafactory-cli train train_config_rank8.yaml
93	Metrics: {"train_loss": 0.1018, "eval_loss": 0.0776, "train_runtime": "28m45s", "ner_full": {"n": 529, "greedy_f1": 0.6397, "oracle_f1": 0.7998, "oracle_headroom": 0.1601, "degeneracy_rate": 0.072, "SJ_rho": 0.3649, "FK_rho": 0.2838, "VC_rho": 0.394, "EM_rho": 0.2562, "LP_rho": 0.2105, "SJ_auroc": 0.689, "FK_auroc": 0.6002, "VC_auroc": 0.6886, "EM_auroc": 0.7265, "LP_auroc": 0.6054, "sel_SJ": 0.6306, "sel_FK": 0.6265, "sel_VC": 0.5919, "sel_EM": 0.6073, "sel_LP": 0.635}, "ner_cond": {"n": 477, "SJ_rho": 0.3056, "FK_rho": 0.1452, "VC_rho": 0.3191, "EM_rho": 0.3558, "LP_rho": 0.169}, "re_full": {"n": 397, "greedy_f1": 0.3712, "oracle_f1": 0.609, "oracle_headroom": 0.2378, "degeneracy_rate": 0.217, "SJ_rho": 0.2244, "FK_rho": 0.3448, "VC_rho": 0.3617, "EM_rho": 0.068, "LP_rho": 0.2737, "SJ_auroc": 0.7092, "FK_auroc": 0.6469, "VC_auroc": 0.7533, "EM_auroc": 0.7306, "LP_auroc": 0.6325, "sel_SJ": 0.3584, "sel_FK": 0.3498, "sel_VC": 0.3715, "sel_EM": 0.3291, "sel_LP": 0.3606}, "re_cond": {"n": 242, "SJ_rho": 0.3601, "FK_rho": 0.2343, "VC_rho": 0.3703, "EM_rho": 0.4613, "LP_rho": 0.1809}}
94	
95	────────────────────────────────────────────────────────────────────────────────
96	ID: exp_027_mlp_verifier
97	Status: DONE
98	Conclusion: negative
99	Created: 2026-05-18T06:39:22.524Z
100	Completed: 2026-05-18T06:41:51.069Z
101	Hypothesis: MLP/RF等非线性模型能否通过组合5个QE信号(LP,SJ,FK,EM,VC)超越LR，或通过cross-signal interactions提取额外信息，从而缩小selection gap
102	Model: sklearn LR/MLP/RF
103	Server: a100
104	GPU: NOT SPECIFIED
105	Data path: output/exp_001_n16_seed*/samples.jsonl
106	Data count: 529
107	Seed: 42,123,456
108	checkpoint_path: N/A
109	log_path: output/exp_027_mlp_verifier/
110	Command: python train_mlp_verifier.py --n_samples 16 --cv_folds 5 --seeds 42,123,456
111	Metrics: {"lr_auroc": 0.6522, "mlp_auroc": 0.6381, "rf_auroc": 0.5868, "mlp_15feat_auroc": 0.6341, "lr_sel_f1": 0.6406, "mlp_sel_f1": 0.6278, "greedy_f1": 0.6441, "oracle_f1": 0.8231, "best_single_signal_auroc": 0.6476, "feature_bottleneck_confirmed": true}
112	
113	────────────────────────────────────────────────────────────────────────────────
114	ID: exp_028
115	Status: DONE
116	Conclusion: negative
117	Created: 2026-05-17T07:35:39.447Z
118	Completed: 2026-05-17T12:09:43.334Z
119	Hypothesis: Few-NERD low degeneracy (10%) in exp-021 is NOT due to under-convergence at 3 epochs; training for 5 epochs will show similar degeneracy levels, confirming the structural property of this dataset rather than an artifact of insufficient training.
120	Model: Qwen3-8B LoRA rank=32
121	Server: autodl-5090
122	GPU: NOT SPECIFIED
123	Data path: /root/autodl-tmp/struct_self_consist_ie/data/fewnerd_uie_train
124	Data count: 131767
125	Seed: 42
126	checkpoint_path: checkpoints/qwen3-8b-fewnerd-5epoch-lora
127	log_path: logs/exp_028_4gpu_train.log
128	Command: bash -c "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0,1,2,3 llamafactory-cli train train_config_fewnerd_5epoch_4gpu.yaml 2>&1 | tee logs/exp_028_4gpu_train.log"
129	Metrics: {"degeneracy_cf1_gold": 0.313, "greedy_f1": 0.7773, "lp_sel_f1": 0.7835, "lp_sel_delta_pp": 0.62, "oracle_f1": 0.8723, "within_instance_rho": 0.4066, "train_loss": 0.0189, "eval_loss": 0.0311}
130	
131	────────────────────────────────────────────────────────────────────────────────
132	ID: exp_028_fewnerd_5epoch
133	Status: DONE
134	Conclusion: negative
135	Created: 2026-05-17T07:53:12.913Z
136	Completed: 2026-05-17T20:29:42.274Z
137	Hypothesis: Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain.
138	Model: Qwen3-8B LoRA rank=32
139	Server: autodl-5090
140	GPU: cuda:0,1,2,3
141	Data path: data/fewnerd_uie_train
142	Data count: 131767
143	Seed: 42
144	checkpoint_path: checkpoints/qwen3-8b-fewnerd-5epoch-lora
145	log_path: logs/exp_028_4gpu_train.log
146	Command: bash -c "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0,1,2,3 llamafactory-cli train train_config_fewnerd_5epoch_4gpu.yaml 2>&1 | tee logs/exp_028_4gpu_train.log"
147	Metrics: {"degeneracy_cf1_gold": 0.3133, "greedy_f1": 0.7773, "lp_sel_delta_pp": 0.624, "lp_sel_f1": 0.7835, "oracle_f1": 0.8723, "within_instance_rho_mean": 0.4066, "within_instance_rho_median": 0.6151}
148	
149	────────────────────────────────────────────────────────────────────────────────
150	ID: exp_029a
151	Status: DONE
152	Conclusion: success
153	Created: 2026-05-17T23:32:17.191Z
154	Completed: 2026-05-18T01:00:18.242Z
155	Hypothesis: Training convergence modulates degeneracy across datasets. SciERC 3-epoch training should produce lower degeneracy than 5-epoch baseline (17.8%), confirming epoch confound is not Few-NERD-specific.
156	Model: Qwen3-8B LoRA rank=32
157	Server: autodl-5090
158	GPU: cuda:0
159	Data path: data/scierc_uie_train
160	Data count: 1861
161	Seed: 42
162	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-3epoch-lora
163	log_path: /root/autodl-tmp/struct_self_consist_ie/logs/exp_029a_inference.log
164	Command: FORCE_TORCHRUN=0 CUDA_VISIBLE_DEVICES=0 bash -c "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_scierc_3ep.yaml"
165	Metrics: {"degen_rate": 0.064, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"}
166	
167	────────────────────────────────────────────────────────────────────────────────
168	ID: exp_029b
169	Status: DONE
170	Conclusion: success
171	Created: 2026-05-17T23:32:18.543Z
172	Completed: 2026-05-18T00:56:47.625Z
173	Hypothesis: Training convergence modulates degeneracy across datasets. SciERC 10-epoch training should produce higher degeneracy than 5-epoch baseline (17.8%), confirming monotonic epoch-degeneracy relationship across datasets.
174	Model: Qwen3-8B
175	Server: autodl-5090
176	GPU: cuda:1
177	Data path: scierc_uie_train
178	Data count: 1861
179	Seed: 42
180	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-10epoch-lora/
181	log_path: ~/runs/struct_self_consist_ie/exp_029b.log
182	Command: FORCE_TORCHRUN=0 CUDA_VISIBLE_DEVICES=1 llamafactory-cli train train_config_scierc_10ep.yaml
183	Metrics: {"degen_rate": 0.478, "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"}
184	
185	────────────────────────────────────────────────────────────────────────────────
186	ID: exp_b1_scd_conll_control
187	Status: DONE
188	Conclusion: negative
189	Created: 2026-05-20T11:17:40.591Z
190	Completed: 2026-05-20T12:14:30.260Z
191	Hypothesis: Negative control: SCD on CoNLL where construction gain is negative (-0.4pp, high degeneracy 70%). If SCD learns from construction pseudo-labels, it should NOT improve greedy F1 on a dataset where construction itself hurts. Expected: no improvement or slight degradation. Validates SCD mechanism.
192	Model: Qwen3-8B-FT-CoNLL
193	Server: autodl-5090-b
194	GPU: NOT SPECIFIED
195	Data path: /root/autodl-tmp/struct_self_consist_ie/data/scd_conll_theta2n_s42.jsonl
196	Data count: 3453
197	Seed: 42
198	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll-scd-lora
199	log_path: /root/autodl-tmp/struct_self_consist_ie/logs/scd_conll_s42.log
200	Command: llamafactory-cli train train_config_scd_conll_s42.yaml
201	Metrics: {"pre_scd_greedy_f1": 0.9078, "post_scd_greedy_f1": 0.9184, "delta_pp": 1.06, "training_steps": 690, "final_loss": 0.0359, "negative_control_confirmed": false, "note": "SURPRISE: SCD improved CoNLL F1 by +1.06pp despite negative construction gain. Possible explanations: (1) SCD provides general training benefit (more data), (2) additional training steps alone improve, (3) SCD mechanism doesn't require positive construction gain."}
202	
203	────────────────────────────────────────────────────────────────────────────────
204	ID: exp_b1_scd_fewnerd_curriculum_q
205	Status: DONE
206	Conclusion: negative
207	Created: 2026-05-20T11:17:38.760Z
208	Completed: 2026-05-20T19:01:57.213Z
209	Hypothesis: Q variant SCD with curriculum ordering: use B2 entity verifier confidence to stratify pseudo-labels (conf>0.8→Round1, 0.5-0.8→Round2, conf<0.5→discard). Curriculum by verifier confidence improves SCD convergence and final greedy F1 vs standard flat SCD on FewNERD.
210	Model: Qwen3-8B-FT
211	Server: autodl-5090-b
212	GPU: NOT SPECIFIED
213	Data path: /root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl
214	Data count: 32565
215	Seed: 43
216	note: Fallback standard SCD seed=43 (Q-variant deferred per D189)
217	Notes: M046: SCD metric artifact confirmed. Original +3.84pp was comparing instance-avg F1 baseline (0.7482, gold-filtered n=32565) to micro-F1 post-SCD (0.7866, full n=37648). Unified micro-F1: pre=0.7886 → post=0.7866, Δ=-0.20pp. Instance-avg: pre=0.7719 → post=0.7809, Δ=+0.90pp (much smaller than claimed). SCD does not constitute paper contribution.
218	Command: llamafactory-cli train train_config_scd_fewnerd_fallback_s43.yaml
219	Metrics: {"eval_greedy_f1": 0.7866, "eval_greedy_precision": 0.7663, "eval_greedy_recall": 0.808, "eval_instance_avg_f1": 0.7809, "delta_vs_baseline": 0.0386, "baseline_greedy_f1": 0.748, "total_tp": 78252, "total_fp": 23869, "total_fn": 18590, "n_instances": 37648}
220	
221	────────────────────────────────────────────────────────────────────────────────
222	ID: exp_b1_scd_fewnerd_standard
223	Status: DONE
224	Conclusion: negative
225	Created: 2026-05-20T11:17:37.804Z
226	Completed: 2026-05-20T19:13:26.395Z
227	Hypothesis: Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.
228	Model: Qwen3-8B-FT
229	Server: autodl-5090-b
230	GPU: NOT SPECIFIED
231	Data path: /root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl
232	Data count: 32565
233	Seed: 42
234	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/
235	Notes: M046: SCD metric artifact confirmed. Original +3.3pp was comparing instance-avg F1 baseline (0.7482, gold-filtered n=32565) to micro-F1 post-SCD (0.7813, full n=37648). Unified micro-F1: pre=0.7886 → post=0.7813, Δ=-0.73pp. SCD does not improve NER performance.
236	Command: llamafactory-cli train train_config_scd_fewnerd_s42.yaml
237	Metrics: {"train_loss": 0.023, "eval_loss": 0.0329, "steps": 4706, "epochs": 2, "train_runtime_hours": 7.14}
238	
239	────────────────────────────────────────────────────────────────────────────────
240	ID: exp_b1_scd_threshold_ablation
241	Status: DONE
242	Conclusion: failed
243	Created: 2026-05-20T11:17:42.163Z
244	Completed: 2026-05-20T20:00:50.883Z
245	Hypothesis: Construction threshold sweep for SCD pseudo-label generation on FewNERD: θ∈{1/N, 2/N, 3/N, 0.5}. Higher θ = more conservative pseudo-labels (higher precision, lower recall). Optimal θ balances pseudo-label quality vs quantity for SCD training effectiveness.
246	Model: Qwen3-8B-FT
247	Server: autodl-5090-b
248	GPU: NOT SPECIFIED
249	Data path: /root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta3n_s42.jsonl
250	Data count: 32565
251	Seed: 42
252	note: theta=3/N ablation
253	Command: llamafactory-cli train train_config_scd_fewnerd_theta3_s42.yaml
254	
255	────────────────────────────────────────────────────────────────────────────────
256	ID: exp_e2_pretrained_conll
257	Status: DONE
258	Conclusion: success
259	Created: 2026-05-21T05:52:08.180Z
260	Completed: 2026-05-21T08:36:34.020Z
261	Hypothesis: Pre-trained Qwen2.5-7B-Instruct (no fine-tuning) on CoNLL NER exhibits correlation-selection gap similar to fine-tuned models, demonstrating the gap is model-intrinsic rather than fine-tuning-induced.
262	Model: Qwen2.5-7B-Instruct
263	Server: autodl-5090
264	GPU: ['cuda:2']
265	Data path: data/conll2003/
266	Data count: 3453
267	Seed: 42
268	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_conll/
269	log_path: /root/autodl-tmp/struct_self_consist_ie/logs/exp_e2_pretrained_conll.log
270	Command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/models/Qwen2.5-7B-Instruct/Qwen/Qwen2___5-7B-Instruct --data_dir data/conll2003/ --dataset conll2003 --subtask
271	
272	────────────────────────────────────────────────────────────────────────────────
273	ID: exp_e2_pretrained_scierc
274	Status: DONE
275	Conclusion: negative
276	Created: 2026-05-21T07:18:21.189Z
277	Completed: 2026-05-21T09:10:06.217Z
278	Hypothesis: Pre-trained Qwen2.5-7B-Instruct (no fine-tuning) on SciERC NER exhibits correlation-selection gap similar to fine-tuned models, demonstrating the gap is model-intrinsic rather than fine-tuning-induced.
279	Model: Qwen2.5-7B-Instruct
280	Server: autodl-5090-c
281	GPU: ['cuda:3']
282	Data path: data/scierc/processed_data/
283	Data count: 100
284	Seed: 42
285	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_scierc/
286	log_path: ~/runs/struct_self_consist_ie/exp_e2_pretrained_scierc.log
287	Command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct/ --data_dir data/scierc/processed_data/ --dataset scierc --subtask ner --n_sampl
288	Metrics: {"greedy_f1": 0.2418, "oracle_f1": 0.3888, "oracle_headroom": 0.147, "fleiss_kappa_mean": 0.223, "soft_jaccard_mean": 0.473, "rho_SJ_full": 0.2193, "rho_kappa_full": 0.2516, "rho_SJ_cond": 0.1987, "rho_kappa_cond": 0.1953, "logprob_rho_full": 0.078, "logprob_auroc_full": 0.5412, "logprob_rho_cond": 0.1895, "logprob_auroc_cond": 0.5527, "sample_f1_mean": 0.2272, "sample_f1_pct_zero": 46.29, "structural_beats_surface": false, "verdict": "FAIL", "warning": ">30% samples F1=0"}
289	
290	────────────────────────────────────────────────────────────────────────────────
291	ID: exp_llama_fewnerd_lora
292	Status: DONE
293	Conclusion: success
294	Created: 2026-05-18T13:20:55.859Z
295	Completed: 2026-05-19T01:08:20.832Z
296	Hypothesis: LLaMA-based model with LoRA fine-tuning on Few-NERD can provide a second model family (beyond Qwen) for cross-model generalization evidence of structured self-consistency phenomena in NER
297	Model: LLaMA-Few-NERD-LoRA
298	Server: autodl-5090
299	GPU: cuda:1
300	Data path: /root/autodl-tmp/struct_self_consist_ie/data/fewnerd
301	Data count: -1
302	Seed: 42
303	log_path: /root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log
304	note: Retroactively registered - data_count unknown, seed assumed 42
305	Command: llamafactory-cli train train_config_llama_fewnerd.yaml
306	Metrics: {"epoch": 3, "train_loss": 0.0516, "eval_loss": 0.0323, "train_runtime_hours": 15.35, "total_steps": 24708, "final_checkpoint": "checkpoint-24708", "adapter_size_mb": 320}
307	
308	────────────────────────────────────────────────────────────────────────────────
309	ID: exp_qwen25_14b_fewnerd
310	Status: DONE
311	Conclusion: success
312	Created: 2026-05-19T06:19:31.620Z
313	Completed: 2026-05-19T12:44:29.453Z
314	Hypothesis: The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings.
315	Model: Qwen2.5-14B-Instruct
316	Server: autodl-5090-c
317	GPU: NOT SPECIFIED
318	Data path: /root/autodl-tmp/struct_self_consist_ie/data/fewnerd/llmfactory_train.json
319	Data count: 131767
320	Seed: 42
321	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-14b-fewnerd-qlora-s42/
322	log_path: /root/autodl-tmp/struct_self_consist_ie/logs/train_14b_s42.log
323	Notes: 2026-05-19 12:47 UTC: RECOVERED from false-positive startup recovery failure. Step 6483/41180 (15.7%), loss 0.0608, ~2.2s/it, ETA ~21h. checkpoint-6000 saved. screen train_14b_s42 PID 56766, GPU 0,1 95-96% util. Cron registered on PID 56773.
324	Command: CUDA_VISIBLE_DEVICES=0,1 FORCE_TORCHRUN=1 NNODES=1 NPROC_PER_NODE=2 llamafactory-cli train train_config_qwen25_14b_fewnerd_s42.yaml
325	Metrics: {"epoch": 5, "train_loss": 0.0348, "eval_loss": 0.0323, "train_runtime_hours": 29.8, "train_samples_per_second": 6.141, "train_steps_per_second": 0.384, "total_steps": 41180}
326	
327	────────────────────────────────────────────────────────────────────────────────
328	ID: exp_qwen25_32b_fewnerd
329	Status: DONE
330	Conclusion: success
331	Created: 2026-05-19T06:19:25.428Z
332	Completed: 2026-05-21T00:18:28.126Z
333	Hypothesis: Qwen2.5-32B-Instruct QLoRA fine-tuning on FewNERD: scaling model from 8B→32B should improve per-sample NER quality, enabling stronger SC diagnostic signals. LoRA r=32, alpha=64, target all attention+FFN projections, 5 epochs, 4×RTX 5090.
334	Model: Qwen2.5-32B-Instruct
335	Server: autodl-5090
336	GPU: NOT SPECIFIED
337	Data path: /root/autodl-tmp/struct_self_consist_ie/data/fewnerd/llmfactory_train.json
338	Data count: 131767
339	Seed: 42
340	Method: QLoRA-4bit-nf4 (rank=32, alpha=64, target=all)
341	epochs: 5
342	lr: 2e-4
343	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-32b-fewnerd-qlora-s42/checkpoint-32000
344	log_path: /root/autodl-tmp/struct_self_consist_ie/logs/train_qwen25_32b_fewnerd_s42.log
345	Notes: 2026-05-19 11:36 UTC: step 2177/41180 (5.3%), loss 0.0663, ~2.44s/it, ETA ~26h. checkpoint-2000 saved. PID 804438, 4×5090 87-100% util.
346	Command: CUDA_VISIBLE_DEVICES=0,1,2,3 FORCE_TORCHRUN=1 NNODES=1 NPROC_PER_NODE=4 llamafactory-cli train /root/autodl-tmp/struct_self_consist_ie/train_config_qwen25_32b_fewnerd_s42.yaml
347	Metrics: {"total_steps": 41180, "epochs": 5, "best_checkpoint": "checkpoint-32000", "best_eval_loss": 0.0334, "final_train_loss": 0.005, "final_eval_loss": 0.0412, "initial_loss": 0.559, "training_time_hours": 38.5, "lora_rank": 32, "lora_alpha": 64, "note": "Overfitting after epoch ~3.9; best eval_loss at step 32000 (epoch 3.89). Post-training load-best-model OOM (rank2) but all checkpoints saved correctly."}
348	
349	────────────────────────────────────────────────────────────────────────────────
350	ID: exp_qwen25_7b_fewnerd
351	Status: DONE
352	Conclusion: success
353	Created: 2026-05-19T06:41:43.121Z
354	Completed: 2026-05-20T05:45:54.613Z
355	Hypothesis: Qwen2.5-7B QLoRA fine-tuned on FewNERD will produce structurally diverse samples enabling self-consistency-based entity extraction with meaningful LP-weighted consensus signals, comparable to the 14B model but with lower compute cost.
356	Model: Qwen2.5-7B-Instruct
357	Server: autodl-5090-c
358	GPU: NOT SPECIFIED
359	Data path: /root/autodl-tmp/struct_self_consist_ie/data/fewnerd/llmfactory_train.json
360	Data count: 131767
361	Seed: 42
362	Method: QLoRA 4-bit nf4, rank=32, alpha=64, 5 epochs, lr=2e-4, effective_batch=32
363	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-fewnerd-qlora-s42
364	log_path: /root/autodl-tmp/struct_self_consist_ie/logs/pipeline_qwen25_7b_fewnerd.log
365	Notes: 2026-05-19 11:36 UTC: step 138/20590 (0.7%), ~2.34s/it, ETA ~13.3h. Pipeline PID 71837, llamafactory PID 71844. cuda:2,3 98-100% util. Cron registered on pipeline PID.
366	Command: nohup bash run_fewnerd_qwen25_7b_pipeline.sh > logs/pipeline_qwen25_7b_fewnerd.log 2>&1 &
367	Metrics: {"3seed_mean": {"lp_rho": 0.346, "lp_rho_std": 0.021, "sj_rho": 0.388, "sj_rho_std": 0.029, "vc_rho": 0.404, "vc_rho_std": 0.01, "degen_pct": 31.7, "degen_std": 0.9, "greedy_f1": 0.784, "greedy_f1_std": 0.001, "oracle_f1": 0.876, "oracle_f1_std": 0.003, "construction_lp_delta_pp": -0.11, "construction_lp_delta_std": 0.25}, "per_seed": {"seed42": {"lp_rho": 0.3221, "sj_rho": 0.3554, "vc_rho": 0.393, "degen_pct": 31.1, "greedy_f1": 0.7851, "oracle_f1": 0.8718, "construction_lp_delta_pp": -0.4, "bootstrap_p": 1, "bootstrap_ci": [-0.53, -0.26], "cohens_d": -0.0319}, "seed123": {"lp_rho": 0.3538, "sj_rho": 0.3979, "vc_rho": 0.4067, "degen_pct": 32.8, "greedy_f1": 0.785, "oracle_f1": 0.8777, "construction_lp_delta_pp": -0.03, "bootstrap_p": 0.651}, "seed456": {"lp_rho": 0.3629, "sj_rho": 0.4105, "vc_rho": 0.4118, "degen_pct": 31.3, "greedy_f1": 0.7825, "oracle_f1": 0.8771, "construction_lp_delta_pp": 0.09, "bootstrap_p": 0.168}}, "construction_significant": false}
368	
369	────────────────────────────────────────────────────────────────────────────────
370	ID: exp_qwen3_4b_conll_finetune
371	Status: DONE
372	Conclusion: success
373	Created: 2026-05-15T17:18:35.501Z
374	Completed: 2026-05-15T18:45:43.672Z
375	Hypothesis: Scale ablation: Qwen3-4B CoNLL NER LoRA fine-tune to provide cross-scale evidence (vs 8B). Verify correlation-selection gap, SJ>FK ordering, and LP compression generalize across model scale.
376	Model: Qwen3-4B
377	Server: autodl-5090
378	GPU: ['cuda:0']
379	Data path: data/conll2003
380	Data count: 14041
381	Seed: 42
382	LoRA config:
383	  trainable_params: 66M / 4.09B (1.62%)
384	  target_modules: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
385	  epochs: 5
386	  batch_size: 16
387	  total_steps: 4390
388	  enable_thinking: False
389	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora
390	log_path: checkpoints/qwen3-4b-conll2003-lora/trainer_log.jsonl
391	plan_id: D096
392	Notes: Training stopped at step 3920/4390 (89.3%, epoch 4.46/5). No error log or tmux session found. checkpoint-3800 is valid (adapter_model.safetensors 264MB, eval_loss=0.023). Proceeding with checkpoint-3800 for merge+inference.
393	Command: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli train train_config_conll2003_4b.yaml
394	Metrics: {"final_loss": 0.0086, "total_steps_completed": 3920, "total_steps_target": 4390, "epochs_completed": 4.46, "epochs_target": 5, "best_checkpoint": "checkpoint-3800", "note": "Training stopped at 89.3% completion (no error log found). Using checkpoint-3800 (loss ~0.01) for merge."}
395	
396	────────────────────────────────────────────────────────────────────────────────
397	ID: exp_qwen3_4b_conll_finetune_resume
398	Status: DONE
399	Conclusion: success
400	Created: 2026-05-15T19:38:19.388Z
401	Completed: 2026-05-15T19:38:43.468Z
402	Hypothesis: CoNLL 4B NER LoRA fine-tune resume from checkpoint-3800. Cross-scale evidence for correlation-selection gap.
403	Model: Qwen3-4B
404	Server: autodl-5090
405	GPU: cuda:1
406	Data path: data/conll2003/llmfactory_train.json
407	Data count: 14042
408	Seed: 42
409	learning_rate: 0.0002
410	batch_size: 2 x 8 grad_accum
411	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora
412	log_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora/trainer_state.json
413	Command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_conll2003_4b_resume.yaml"
414	Metrics: {"train_loss": 0.001136, "eval_loss": 0.0225, "best_global_step": 4200, "best_metric_eval_loss": 0.0225, "total_steps": 4390, "epochs": 5, "train_runtime_sec": 1185.8, "train_samples_per_second": 59.2, "resumed_from_step": 3800}
415	
416	────────────────────────────────────────────────────────────────────────────────
417	ID: exp_qwen3_4b_scierc_finetune
418	Status: DONE
419	Conclusion: killed
420	Created: 2026-05-15T18:58:58.948Z
421	Completed: 2026-05-15T19:03:05.505Z
422	Model: NOT SPECIFIED
423	Server: autodl-5090
424	GPU: ['cuda:3']
425	Data path: NOT SPECIFIED
426	Data count: NOT SPECIFIED
427	Seed: NOT SPECIFIED
428	log_path: ~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune.log
429	Command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli train train_config_scierc_4b.yaml"
430	
431	────────────────────────────────────────────────────────────────────────────────
432	ID: exp_qwen3_4b_scierc_finetune_v2
433	Status: DONE
434	Conclusion: failed
435	Created: 2026-05-15T19:03:49.204Z
436	Completed: 2026-05-15T19:24:14.124Z
437	Model: Qwen3-4B
438	Server: autodl-5090
439	GPU: cuda:3
440	Data path: data/scierc/processed_data
441	Data count: 1861
442	Seed: 42
443	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-scierc-lora/
444	log_path: ~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v2.log
445	plan_id: D096
446	Notes: PID 219830 已死，仅完成 step 10，无 checkpoint。需彻底重启。
447	Command: llamafactory-cli train train_config_scierc_4b.yaml
448	
449	────────────────────────────────────────────────────────────────────────────────
450	ID: exp_qwen3_4b_scierc_finetune_v3
451	Status: DONE
452	Conclusion: failed
453	Created: 2026-05-15T19:24:45.518Z
454	Completed: 2026-05-15T19:39:04.438Z
455	Model: Qwen3-4B
456	Server: autodl-5090
457	GPU: ['cuda:2']
458	Data path: data/scierc/processed_data
459	Data count: 551
460	Seed: 42
461	log_path: ~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v3.log
462	Notes: OOM on cuda:2 — freeform inference (seed789, 8B) 占满 GPU 2。未实际训练。重启为 v4 on cuda:0。
463	Command: llamafactory-cli train train_config_scierc_4b.yaml
464	
465	────────────────────────────────────────────────────────────────────────────────
466	ID: exp_qwen3_4b_scierc_finetune_v4
467	Status: DONE
468	Conclusion: success
469	Created: 2026-05-15T19:26:25.512Z
470	Completed: 2026-05-15T19:54:20.255Z
471	Hypothesis: Qwen3-4B SciERC LoRA fine-tune v4: training the smaller 4B model to complete the 2x2 scale matrix (4B×SciERC cell). Validates that fine-tuning convergence patterns hold across model scales.
472	Model: Qwen3-4B
473	Server: autodl-5090
474	GPU: cuda:0
475	Data path: data/scierc/processed_data
476	Data count: 551
477	Seed: 42
478	log_path: ~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v4.log
479	Command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_scierc_4b.yaml"
480	Metrics: {"total_steps": 585, "completed_steps": 585, "best_checkpoint": "checkpoint-400", "best_eval_loss": 0.0898, "epochs": 5}
481	
482	────────────────────────────────────────────────────────────────────────────────
483	ID: exp_wnut17_qwen25_7b
484	Status: DONE
485	Conclusion: negative
486	Created: 2026-05-19T06:19:33.960Z
487	Completed: 2026-05-19T11:22:56.623Z
488	Hypothesis: The correlation-selection gap extends to noisy social media NER (WNUT-17). Unlike formal-domain datasets (SciERC/CoNLL/FewNERD), WNUT-17 has higher surface-level noise which may affect structural signal reliability differently. This tests domain generalization of the diagnostic framework.
489	Model: Qwen2.5-7B-Instruct
490	Server: autodl-5090-c
491	GPU: NOT SPECIFIED
492	Data path: /root/autodl-tmp/struct_self_consist_ie/data/wnut17/llmfactory_train.json
493	Data count: 3404
494	Seed: 42
495	Method: QLoRA 4-bit (bnb nf4), rank=32, alpha=64, all targets
496	epochs: 5
497	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-wnut17-qlora-s42
498	log_path: /root/autodl-tmp/struct_self_consist_ie/logs/exp_wnut17_7b_pipeline.log
499	Command: bash wait_and_train.sh (screen: exp_wnut17_7b)
500	Metrics: {"seed42": {"greedy_f1": 0.4524, "construction_f1": 0.4439, "construction_delta_pp": -0.84, "construction_p": 0.95}, "seed123": {"greedy_f1": 0.4518, "construction_f1": 0.4579, "construction_delta_pp": 0.61, "construction_p": 0.08}, "seed456": {"greedy_f1": 0.4526, "construction_f1": 0.4583, "construction_delta_pp": 0.57, "construction_p": 0.12}, "oracle_headroom_pp": "6.3-9.2"}
501	
502	────────────────────────────────────────────────────────────────────────────────
503	ID: ft_001
504	Status: DONE
505	Conclusion: success
506	Created: 2026-05-14T06:04:28.030Z
507	Completed: 2026-05-14T06:30:32.889Z
508	Hypothesis: Fine-tuned Qwen3-8B on SciERC UIE can achieve NER F1 >= 73 and serve as base model for structural consistency MVP
509	Model: Qwen/Qwen3-8B
510	Server: autodl-5090
511	GPU: NOT SPECIFIED
512	Data path: /root/autodl-tmp/struct_self_consist_ie/data/scierc
513	Data count: 1861
514	Seed: 42
515	Method: LoRA r=16 alpha=32
516	Framework: LLaMA Factory 0.9.4
517	epoch: 3
518	train_loss: 0.1099
519	eval_loss: 0.0771
520	train_runtime: 0:17:49
521	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora/
522	log_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_001_train.log
523	note: gate0: NER PASS 60.4% / RE FAIL 33.8%
524	Command: sft training qwen3-8b on scierc with lora
525	Metrics: {"train_loss": 0.1099, "eval_loss": 0.0771, "gate0_ner_f1_strict": 0.1143, "gate0_re_f1_strict": 0.0125, "gate0_ner_f1_text": 0.606, "gate0_re_f1_text": 0.3392, "gate0_offset_accuracy": 0.1665, "gate0_parse_failures": 43, "gate0_pass": false, "gate0_realigned_ner_f1": 0.6045, "gate0_realigned_re_f1": 0.338, "gate0_realigned_entity_offset_accuracy": 1, "gate0_realigned_relation_offset_accuracy": 1, "gate0_realigned_ner_pass": true, "gate0_realigned_re_pass": false, "gate0_realigned_pass": false, "gate0_ner_f1_delta_realign": 0.4901, "gate0_re_f1_delta_realign": 0.3255, "verdict_note": "partial: NER PASS (60.4%) / RE FAIL (33.8% < 40%)"}
526	
527	────────────────────────────────────────────────────────────────────────────────
528	ID: ft_002
529	Status: DONE
530	Conclusion: killed
531	Created: 2026-05-14T07:39:18.640Z
532	Completed: 2026-05-14T08:02:30.390Z
533	Hypothesis: Extended training (5 epochs, LoRA r=32) improves RE F1 above 40% threshold
534	Model: Qwen/Qwen3-8B
535	Server: autodl-5090
536	GPU: cuda:1
537	Data path: /root/autodl-tmp/struct_self_consist_ie/data/llmfactory_train.json
538	Data count: 1861
539	Seed: 42
540	Method: LoRA r=32 alpha=64, 5 epochs, relation direction hint
541	total_steps: 585
542	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2
543	log_path: /root/autodl-tmp/struct_self_consist_ie/ft_002_train.log
544	Command: llamafactory-cli train /root/autodl-tmp/struct_self_consist_ie/train_config_v2.yaml
545	Metrics: {"last_step": 70, "total_steps": 585, "progress_pct": 11.97, "last_loss": 0.1134, "last_lr": 0.00019982, "elapsed": "3m32s", "failure_reason": "OOM at step 73, batch_size=4 too large for 32GB RTX 5090"}
546	
547	────────────────────────────────────────────────────────────────────────────────
548	ID: ft_002_v2
549	Status: DONE
550	Conclusion: success
551	Created: 2026-05-14T08:28:40.861Z
552	Completed: 2026-05-14T08:51:32.405Z
553	Hypothesis: Extended training (5 epochs, LoRA r=32) with OOM fix improves RE F1 above 40% threshold
554	Model: Qwen/Qwen3-8B
555	Server: autodl-5090
556	GPU: cuda:1
557	Data path: /root/autodl-tmp/struct_self_consist_ie/data/llmfactory_train.json
558	Data count: 1861
559	Seed: 42
560	Method: LoRA r=32 alpha=64, 5 epochs, batch=2 grad_accum=8 gradient_checkpointing=true
561	checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2
562	log_path: /root/autodl-tmp/struct_self_consist_ie/ft_002v2_train.log
563	Command: CUDA_VISIBLE_DEVICES=1 llamafactory-cli train train_config_v2.yaml
564	Metrics: {"epoch": 5, "train_loss": 0.0806, "eval_loss": 0.089, "train_runtime": "28m41s", "train_samples_per_second": 5.407, "train_steps_per_second": 0.34, "total_steps": 585, "checkpoints": ["checkpoint-400", "checkpoint-500", "checkpoint-585"], "gate0_final_ner_f1": 0.6615, "gate0_final_re_f1": 0.4177, "gate0_final_parse_failures": 0, "gate0_final_ner_pass": true, "gate0_final_re_pass": true, "gate0_final_pass": true, "gate0_ckpt400_ner_f1": 0.6475, "gate0_ckpt400_re_f1": 0.3793, "gate0_ckpt400_parse_failures": 0, "gate0_ckpt400_verdict": "FAIL", "gate0_ckpt400_re_sample_f1_pct_zero": 58.8, "gate0_ckpt400_warning": ">30% samples F1=0"}
565	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58f4a557-04b1-4b0d-b9a7-3fc1ceea6f4f",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "bc1847d3-bbec-47ad-9f17-9ac8731874e9",
  "sourceToolAssistantUUID": "58f4a557-04b1-4b0d-b9a7-3fc1ceea6f4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-21T11:18:31.707Z_

Now let me get the API-based experiments and a comprehensive dump of inference experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc1847d3-bbec-47ad-9f17-9ac8731874e9",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFd327Wqvjf25KsZ3sW5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a07bdaed-cef4-4798-960c-ce65ed1f44ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gprtp1n4ocWZbDKW353hUg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16048,
      "cache_read_input_tokens": 32196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16048,
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

_source line 30 · 2026-05-21T11:18:44.528Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019HhDzNWsM2iDxMWrKJEe9N`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/all_exps.json') as f:\n    exps = json.load(f)\n\napi_ids = [\n    'exp_a2_humaneval_sc', 'exp_b_frontier_sc_fewnerd',\n    'exp_frontier_sc_claude_sonnet4', 'exp_frontier_sc_deepseek',\n    'exp_frontier_sc_gemini25pro', 'exp_frontier_sc_gpt55_fewnerd_v2',\n    'exp_spider_sc_pilot'\n]\n\nprint(\"=\" * 100)\nprint(\"CATEGORY 2: API-BASED MODEL EXPERIMENTS\")\nprint(\"=\" * 100)\n\nfor eid in sorted(api_ids):\n    e = exps[eid]\n    spec = e.get('spec', {})\n    print(f\"\\n{'─' * 80}\")\n    print(f\"ID: {eid}\")\n    print(f\"Status: {e.get('status')}\")\n    print(f\"Conclusion: {e.get('conclusion')}\")\n    print(f\"Created: {e.get('created_at')}\")\n    print(f\"Completed: {e.get('completed_at')}\")\n    \n    hyp = e.get('hypothesis') or spec.get('hypothesis') or ''\n    if hyp:\n        print(f\"Hypothesis: {hyp}\")\n    \n    print(f\"Model: {spec.get('model_name', spec.get('model', 'NOT SPECIFIED'))}\")\n    print(f\"Server: {spec.get('server', 'NOT SPECIFIED')}\")\n    print(f\"Data path: {spec.get('data_path', 'NOT SPECIFIED')}\")\n    print(f\"Data count: {spec.get('data_count', 'NOT SPECIFIED')}\")\n    print(f\"Seed: {spec.get('seed', 'NOT SPECIFIED')}\")\n    \n    # API-specific params\n    for key in ['base_url', 'api_key', 'checkpoint_source', 'eval_data',\n                 'n_instances', 'n_samples', 'temperature', 'max_workers',\n                 'checkpoint_path', 'log_path', 'note']:\n        val = spec.get(key)\n        if val is not None:\n            print(f\"{key}: {val}\")\n    \n    # Command\n    cmd = spec.get('command', '')\n    if cmd:\n        print(f\"Command: {cmd[:500]}\")\n    \n    # Notes\n    notes = e.get('notes', '')\n    if notes:\n        print(f\"Notes: {notes}\")\n    \n    # Metrics\n    metrics = e.get('metrics', {})\n    if metrics:\n        print(f\"Metrics: {json.dumps(metrics, ensure_ascii=False)}\")\n\n    # Full spec dump for anything else\n    extra_keys = set(spec.keys()) - {'command', 'server', 'data_path', 'data_count', \n                                       'model_name', 'model', 'seed', 'base_url', 'api_key',\n                                       'checkpoint_source', 'eval_data', 'n_instances', \n                                       'n_samples', 'temperature', 'max_workers',\n                                       'checkpoint_path', 'log_path', 'note', 'hypothesis'}\n    if extra_keys:\n        print(f\"Additional spec fields: {', '.join(extra_keys)}\")\n        for k in sorted(extra_keys):\n            print(f\"  {k}: {spec[k]}\")\n\nPYEOF\n",
  "description": "Extract API-based model experiment details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a07bdaed-cef4-4798-960c-ce65ed1f44ef",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFd327Wqvjf25KsZ3sW5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2195d05b-cb8e-42d4-be80-ab43201bcf63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gprtp1n4ocWZbDKW353hUg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16048,
      "cache_read_input_tokens": 32196,
      "output_tokens": 985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16048
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 985,
          "cache_read_input_tokens": 32196,
          "cache_creation_input_tokens": 16048,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16048,
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

_source line 31 · 2026-05-21T11:18:44.626Z_

<details><summary>↩ Tool result · `toolu_019HhDzNWsM2iDxMWrKJEe9N`</summary>

```text
====================================================================================================
CATEGORY 2: API-BASED MODEL EXPERIMENTS
====================================================================================================

────────────────────────────────────────────────────────────────────────────────
ID: exp_a2_humaneval_sc
Status: DONE
Conclusion: failed
Created: 2026-05-20T18:15:14.615Z
Completed: 2026-05-20T22:05:17.728Z
Hypothesis: SC failure modes (degeneracy, false agreement) generalize from NER to code generation despite deterministic verification — majority voting on HumanEval will show limited gains over greedy when degeneracy is high, paralleling NER findings.
Model: openai/gpt-5.5
Server: autodl-5090
Data path: openai/openai_humaneval (HuggingFace)
Data count: 164
Seed: 42
checkpoint_path: autodl-5090 humaneval results dir
log_path: autodl-5090 humaneval results dir
Command: python -u run_humaneval_sc.py --n_samples 8 --temperature 1.0 --seed 42 --output_dir ./results
Additional spec fields: pid, failure_reason, fix_note
  failure_reason: 402 API balance exhausted after indent bugfix. Fix verified (23/23 greedy pass, 179/184 sample pass) but only 24/164 tasks completed before API died.
  fix_note: v2 rerun: fixed extract_code() strip() -> rstrip() + auto-indent for function body. Previous run had 0/164 pass due to IndentationError.
  pid: 967645

────────────────────────────────────────────────────────────────────────────────
ID: exp_b_frontier_sc_fewnerd
Status: DONE
Conclusion: failed
Created: 2026-05-20T18:15:19.266Z
Completed: 2026-05-20T22:05:12.564Z
Hypothesis: The correlation-selection gap in structured self-consistency (where agreement correlates with accuracy but majority voting fails to improve over greedy) persists even with frontier models (GPT-5.5, Claude Opus 4.6), indicating it is a fundamental structural limitation of entity-level majority voting rather than a model capability issue.
Model: openai/gpt-5.5 + anthropic/claude-opus-4.6 (via OpenRouter)
Server: local
Data path: HuggingFace DFKI-SLT/few-nerd supervised test split
Data count: 200
Seed: 42
checkpoint_path: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/output/
log_path: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/frontier_sc.log
Command: nohup .venv/bin/python -u run_frontier_sc.py --from-hf --n-instances 200 --n-samples 8 --temperature 1.0 --seed 42 --output-dir ./output > frontier_sc.log 2>&1 &
Additional spec fields: pid, code_path, failure_reason
  code_path: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py
  failure_reason: entity_set() TypeError - compute_instance_metrics passed full parsed dict instead of entities list
  pid: 1509955

────────────────────────────────────────────────────────────────────────────────
ID: exp_frontier_sc_claude_sonnet4
Status: DONE
Conclusion: success
Created: 2026-05-21T06:20:27.878Z
Completed: 2026-05-21T08:58:17.224Z
Hypothesis: Frontier model Claude Sonnet 4 on FewNERD SC (200 instances, N=8, T=1.0): if correlation-selection gap persists across model families (GPT + Claude + Gemini + DeepSeek), the finding is universal and not model-specific.
Model: anthropic/claude-sonnet-4
Server: autodl-5090
Data path: data/fewnerd/test.json
Data count: 200
Seed: 42
checkpoint_source: API (http://47.94.22.126/v1)
eval_data: fewnerd test set (200 instances, N=8, T=1.0)
checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/frontier_sc_claude_sonnet4/
log_path: /root/autodl-tmp/struct_self_consist_ie/logs/frontier_sc_claude_sonnet4.log
note: v2: fixed from offset-based to text-based entity matching for API models
Command: python -u code/run_frontier_sc.py --model anthropic/claude-sonnet-4 --base_url http://47.94.22.126/v1 --dataset fewnerd --data_dir data/fewnerd/ --n_instances 200 --n_samples 8 --temperature 1.0 --output_dir output/frontier_sc_claude_sonnet4/ --max_tokens 4096
Metrics: {"greedy_f1": 0.6068, "mv_f1": 0.6226, "oracle_f1": 0.6544, "degeneracy_rate": 0.74, "selection_gap": 0.0318, "parse_failures": 103, "api_calls": 1600, "wall_clock_seconds": 6118, "instances": 200}
Additional spec fields: pid, matching
  matching: text+type (case-insensitive, no offset)
  pid: 6302

────────────────────────────────────────────────────────────────────────────────
ID: exp_frontier_sc_deepseek
Status: DONE
Conclusion: success
Created: 2026-05-21T06:50:26.022Z
Completed: 2026-05-21T09:10:40.589Z
Hypothesis: Frontier model DeepSeek Chat on FewNERD SC (200 inst, N=8, T=1.0): 4-family cross-validation of correlation-selection gap universality.
Model: deepseek/deepseek-chat
Server: autodl-5090-c
Data path: data/fewnerd/test.json
Data count: 200
Seed: 42
Command: python -u code/run_frontier_sc.py --model deepseek/deepseek-chat --base_url http://47.94.22.126/v1 --dataset fewnerd --n_instances 200 --n_samples 8 --temperature 1.0 --output_dir output/frontier_sc_deepseek/ --max_workers 4
Metrics: {"greedy_f1": 0.3992, "mv_f1": 0.4243, "oracle_f1": 0.714, "degeneracy_rate": 0.055, "agreement_rho": 0.2051, "fleiss_kappa_rho": 0.1471, "sj_rho": 0.1635, "mv_gain_over_greedy": 0.0251, "selection_gap": 0.2897, "parse_failure_count": 751, "total_api_calls": 1600, "elapsed_s": 4043.7}

────────────────────────────────────────────────────────────────────────────────
ID: exp_frontier_sc_gemini25pro
Status: DONE
Conclusion: success
Created: 2026-05-21T06:50:24.793Z
Completed: 2026-05-21T10:55:06.757Z
Hypothesis: Frontier model Gemini 2.5 Pro on FewNERD SC (200 inst, N=8, T=1.0): 4-family cross-validation. If correlation-selection gap persists across GPT + Claude + Gemini + DeepSeek, the finding is universal.
Model: google/gemini-2.5-pro
Server: autodl-5090-c
Data path: data/fewnerd/test.json
Data count: 200
Seed: 42
checkpoint_path: output/frontier_sc_gemini25pro/
log_path: output/frontier_sc_gemini25pro/run.log
Command: python -u code/run_frontier_sc.py --model google/gemini-2.5-pro --base_url http://47.94.22.126/v1 --dataset fewnerd --n_instances 200 --n_samples 8 --temperature 1.0 --output_dir output/frontier_sc_gemini25pro/ --max_workers 4
Metrics: {"greedy_f1": 0.63, "mv_f1": 0.645, "oracle_f1": 0.758, "mv_gain_pp": 1.5, "selection_gap": 0.113, "agreement_rho": 0.389, "parse_failures": 191, "total_samples": 1600, "n_instances": 200, "verdict": "MV helps (+1.5pp)"}

────────────────────────────────────────────────────────────────────────────────
ID: exp_frontier_sc_gpt55_fewnerd_v2
Status: DONE
Conclusion: success
Created: 2026-05-21T04:48:24.698Z
Completed: 2026-05-21T08:36:36.829Z
Hypothesis: Frontier model GPT-5.5 on FewNERD SC (200 instances, N=8, T=1.0): if correlation-selection gap persists in frontier models, the finding is fundamental and not a model capability limitation. Previous attempt failed due to API credit exhaustion.
Model: gpt-5.5
Server: autodl-5090-c
Data path: data/fewnerd/test.json
Data count: 200
Seed: 42
checkpoint_source: openai/gpt-5.5 (API)
eval_data: fewnerd test set (200 instances)
checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/frontier_sc_gpt55_fewnerd_v2/
log_path: /root/autodl-tmp/struct_self_consist_ie/logs/frontier_sc_gpt55_fewnerd_v2.log
Command: python -u code/run_frontier_sc.py --model gpt-5.5 --base_url http://47.94.22.126/v1 --n_instances 200 --n_samples 8 --temperature 1.0 --seed 42 --max_workers 4
Metrics: {"greedy_f1": 0.6382, "mv_f1": 0.6521, "oracle_f1": 0.7203, "degeneracy_rate": 0.5, "rho_agreement": 0.3551, "rho_fk": 0.3515, "rho_sj": 0.3461, "instances": 200}

────────────────────────────────────────────────────────────────────────────────
ID: exp_spider_sc_pilot
Status: DONE
Conclusion: success
Created: 2026-05-20T18:41:49.560Z
Completed: 2026-05-20T22:05:14.976Z
Hypothesis: SC diagnostic cascade (degeneracy, agreement-correctness correlation, failure mode classification F1-F4) validated on NER structured generation will also manifest in SQL structured generation with GPT-5.5 on Spider-dev (200 examples, N=8, T=1.0), demonstrating cross-task universality. Key adaptation: uses execution-result equivalence (not SQL text) for agreement/degeneracy, since semantically equivalent SQL can have different surface forms.
Model: openai/gpt-5.5 via http://47.94.22.126/v1
Server: local (CPU+API)
Data path: xlangai/spider (HF) + spider databases (sqlite)
Data count: 200
Seed: 42
checkpoint_path: local spider_sc results dir
log_path: local spider_sc results dir
Command: python run_spider_sc.py --n_samples 8 --temperature 1.0 --seed 42 --output_dir ./results --test_api
Notes: Data quality verified: all 196 instances generated AFTER F2/F3 bugfix (code modified 20:47:22, checkpoint started 20:47:52). Zero mismatch between embedded and recomputed failure modes. F1-F4 distribution: F1=87.2%, F2=0%, F3=8.2%, F4=0%, OK=4.6%. F2=0 means SQL has no low-agreement zone (either degenerate or high consensus). Paper-ready. Note: F4 is dead code in SQL context (greedy_correct AND NOT mv_correct never occurs). Cross-task threshold note: SQL uses agreement<0.5 for F2/F3 split, RE uses kappa<0.3.
Metrics: {"n_instances": 196, "n_target": 200, "n_skipped": 2, "n_samples": 8, "temperature": 1, "model": "gpt-5.5", "greedy_acc": 0.7653, "mv_acc": 0.7704, "oracle_acc": 0.8061, "mv_gain_pp": 0.51, "degeneracy_rate": 0.8724, "spearman_rho": 0.5501, "spearman_p": 6.77e-17, "kendall_tau": 0.5259, "F1_degeneracy_rate": 0.872, "F2_low_agreement_rate": 0, "F3_high_agree_wrong_rate": 0.082, "F4_selection_gap_rate": 0, "sc_success_rate": 0.046, "nondegen_n": 25, "nondegen_greedy_acc": 0.32, "nondegen_mv_acc": 0.36, "nondegen_oracle_acc": 0.64, "nondegen_spearman_rho": 0.13}
Additional spec fields: failure_reason, pid, bugfixes, partial_results, gpu
  bugfixes: ['F1-F4 failure modes aligned with NER cascade (F2=low_agreement, F3=high_agreement_wrong)', 'Degeneracy detection uses execution results instead of SQL text comparison', 'Converted from vLLM to API-based (CPU+API experiment)']
  failure_reason: 402 API balance exhausted at 125/200 instances
  gpu: cuda:2
  partial_results: 125/200 instances completed before API died
  pid: 1504303
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2195d05b-cb8e-42d4-be80-ab43201bcf63",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "0fb257f4-ad54-41bc-9b71-ac081f1fccdd",
  "sourceToolAssistantUUID": "2195d05b-cb8e-42d4-be80-ab43201bcf63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-21T11:18:48.511Z_

Now let me extract the inference experiments. There are 219 of them, so I'll extract them in a structured way.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fb257f4-ad54-41bc-9b71-ac081f1fccdd",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFd4LULwyexfukveBmGx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce013c10-42b9-4c9f-8142-f3d1531ca074",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gw9puA36muvNiQmuqhWhBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4717,
      "cache_read_input_tokens": 48244,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4717,
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

_source line 33 · 2026-05-21T11:19:10.310Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KRvSn1iMkfZEKc94nPn3pF`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\n\nwith open('/tmp/all_exps.json') as f:\n    exps = json.load(f)\n\napi_models = ['gpt-5.5', 'gpt-4o', 'claude', 'gemini', 'deepseek', 'claude-sonnet', 'claude-sonnet-4', 'gpt', 'openai']\nfinetune_keywords = ['finetune', 'fine-tune', 'fine_tune', 'lora', 'sft', 'train', 'ft_']\n\nfinetune_ids = set()\napi_ids = set()\nfor eid, e in exps.items():\n    spec = e.get('spec', {})\n    model = (spec.get('model_name', '') or spec.get('model', '') or '').lower()\n    command = (spec.get('command', '') or '').lower()\n    eid_lower = eid.lower()\n    \n    is_api = any(am in model for am in api_models) or 'frontier' in eid_lower or 'base_url' in (spec.get('command','') or '') or 'spider' in eid_lower\n    is_finetune = any(kw in eid_lower for kw in finetune_keywords) or \\\n                  any(kw in command for kw in ['llamafactory', 'train_config']) or \\\n                  'lora_config' in spec or \\\n                  ('method' in spec and 'lora' in str(spec.get('method', '')).lower())\n    \n    if is_api:\n        api_ids.add(eid)\n    elif is_finetune:\n        finetune_ids.add(eid)\n\ninference_ids = set(exps.keys()) - finetune_ids - api_ids\n\nprint(\"=\" * 100)\nprint(f\"CATEGORY 3: INFERENCE/EVALUATION EXPERIMENTS ({len(inference_ids)} total)\")\nprint(\"=\" * 100)\n\nfor eid in sorted(inference_ids):\n    e = exps[eid]\n    spec = e.get('spec', {})\n    \n    # Extract key info compactly\n    model = spec.get('model_name', spec.get('model', 'NOT SPECIFIED'))\n    server = spec.get('server', 'N/S')\n    seed = spec.get('seed', 'N/S')\n    data_path = spec.get('data_path', 'N/S')\n    data_count = spec.get('data_count', 'N/S')\n    conclusion = e.get('conclusion', 'N/S')\n    hyp = (e.get('hypothesis') or spec.get('hypothesis') or '')[:200]\n    \n    # Extract N, T from command or spec\n    cmd = spec.get('command', '') or ''\n    \n    n_samples = spec.get('n_samples', None)\n    temperature = spec.get('temperature', None)\n    \n    if n_samples is None:\n        m = re.search(r'--n_samples\\s+(\\d+)', cmd)\n        if m: n_samples = int(m.group(1))\n        else:\n            m = re.search(r'n_samples[\"\\s:=]+(\\d+)', str(spec))\n            if m: n_samples = int(m.group(1))\n    \n    if temperature is None:\n        m = re.search(r'--temperature\\s+([\\d.]+)', cmd)\n        if m: temperature = float(m.group(1))\n        else:\n            m = re.search(r'temperature[\"\\s:=]+([\\d.]+)', str(spec))\n            if m: temperature = float(m.group(1))\n    \n    # Method\n    method = spec.get('method', '')\n    \n    # GPU\n    gpu = spec.get('gpu', '')\n    \n    # Log path, checkpoint\n    cp = spec.get('checkpoint_path', spec.get('checkpoint_source', ''))\n    \n    print(f\"\\n{'─' * 80}\")\n    print(f\"ID: {eid}\")\n    print(f\"Conclusion: {conclusion}\")\n    print(f\"Model: {model}\")\n    print(f\"Dataset: {data_path}\")\n    print(f\"Data count: {data_count}\")\n    print(f\"N (samples): {n_samples if n_samples is not None else 'NOT FOUND'}\")\n    print(f\"T (temperature): {temperature if temperature is not None else 'NOT FOUND'}\")\n    print(f\"Seed: {seed}\")\n    print(f\"Server: {server}\")\n    if gpu: print(f\"GPU: {gpu}\")\n    if method: print(f\"Method: {method}\")\n    if cp: print(f\"Checkpoint: {cp}\")\n    if hyp: print(f\"Hypothesis: {hyp}\")\n    \n    # Check for additional interesting spec fields\n    skip_keys = {'command', 'server', 'data_path', 'data_count', 'model_name', 'model',\n                 'seed', 'n_samples', 'temperature', 'method', 'gpu', 'checkpoint_path',\n                 'checkpoint_source', 'log_path', 'hypothesis', 'note', 'notes'}\n    extra = {k: v for k, v in spec.items() if k not in skip_keys}\n    if extra:\n        for k, v in sorted(extra.items()):\n            val_str = str(v)\n            if len(val_str) > 200:\n                val_str = val_str[:200] + '...'\n            print(f\"  {k}: {val_str}\")\n    \n    # Command\n    if cmd:\n        print(f\"Command: {cmd[:400]}\")\n    \n    # Metrics\n    metrics = e.get('metrics', {})\n    if metrics:\n        metrics_str = json.dumps(metrics, ensure_ascii=False)\n        if len(metrics_str) > 500:\n            metrics_str = metrics_str[:500] + '...'\n        print(f\"Metrics: {metrics_str}\")\n\nPYEOF\n",
  "description": "Extract all inference/evaluation experiment hyperparameters",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce013c10-42b9-4c9f-8142-f3d1531ca074",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFd4LULwyexfukveBmGx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f101f82b-3d3e-4992-a3de-c5f813b5c272",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gw9puA36muvNiQmuqhWhBT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4717,
      "cache_read_input_tokens": 48244,
      "output_tokens": 1646,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4717
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1646,
          "cache_read_input_tokens": 48244,
          "cache_creation_input_tokens": 4717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4717,
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

_source line 34 · 2026-05-21T11:19:10.420Z_

<details><summary>↩ Tool result · `toolu_01KRvSn1iMkfZEKc94nPn3pF`</summary>

```text
&lt;persisted-output>
Output too large (257.7KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a9ed86cb-a33f-4ec8-8078-d4b9402803ce/tool-results/be5reack3.txt

Preview (first 2KB):
====================================================================================================
CATEGORY 3: INFERENCE/EVALUATION EXPERIMENTS (220 total)
====================================================================================================

────────────────────────────────────────────────────────────────────────────────
ID: dgs_pilot
Conclusion: killed
Model: NOT SPECIFIED
Dataset: N/S
Data count: N/S
N (samples): NOT FOUND
T (temperature): NOT FOUND
Seed: N/S
Server: N/S
Hypothesis: Degeneracy-Gated Selection (DGS) validates Two-Condition Theory: using degeneracy rate as gating mechanism to switch between greedy (degenerate) and LP selection (non-degenerate), the improvement dire

────────────────────────────────────────────────────────────────────────────────
ID: e1_component_wise_re_sj
Conclusion: negative
Model: N/A (reuse pilot_004 samples)
Dataset: /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004
Data count: 397
N (samples): NOT FOUND
T (temperature): NOT FOUND
Seed: 42
Server: autodl-5090
Method: Component-wise decomposition: head_sj, tail_sj, type_match 分别计算 Spearman ρ vs per-instance RE F1
Checkpoint: /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004
Hypothesis: RE SJ 乘性惩罚是 root cause：分解后 head_sj ρ ≈ NER ρ (~0.38)，tail_sj 和乘性组合拖低整体 ρ
  parent: mvp_pilot_004
Command: python3 code/analyze_component_wise_re.py
Metrics: {"full_head_sj_rho": 0.21, "full_tail_sj_rho": 0.201, "full_type_match_rho": 0.201, "full_multiplicative_rho": 0.244, "full_additive_rho": 0.243, "full_fleiss_kappa_rho": 0.278, "cond_head_sj_rho": 0.27, "cond_tail_sj_rho": 0.259, "cond_type_match_rho": 0.252, "cond_multiplicative_rho": 0.316, "cond_additive_rho": 0.306, "cond_fleiss_kappa_rho": 0.307, "n_full": 397, "n_conditional": 313, "diagnosis": "head_sj rho=0.210 FAR from NER rho=0.383. Multiplicative penalty hypothesis REJECTED. Problem ...

────────────────────────────────────────────────────────────────────────────────
ID: exp001_seed123
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f101f82b-3d3e-4992-a3de-c5f813b5c272",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "f3c38ebb-3b1f-4c62-be6f-71c155e2f783",
  "sourceToolAssistantUUID": "f101f82b-3d3e-4992-a3de-c5f813b5c272",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-21T11:19:14.472Z_

Good. Now let me create a comprehensive summary by parsing all experiments systematically to produce a structured tabular output.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3c38ebb-3b1f-4c62-be6f-71c155e2f783",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFd6EistoYQhohQYZh7c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "588266c6-44a2-4b53-a435-6928c50a3b2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KD75BKHHqChYqZBz85nJXd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2597,
      "cache_read_input_tokens": 52961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2597,
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

_source line 36 · 2026-05-21T11:19:39.205Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VM9ytzEL2zY4BRiqA848my`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\n\nwith open('/tmp/all_exps.json') as f:\n    exps = json.load(f)\n\n# Parse all experiments and extract every hyperparameter we can find\ndef extract_params(eid, e):\n    spec = e.get('spec', {})\n    cmd = spec.get('command', '') or ''\n    metrics = e.get('metrics', {})\n    \n    params = {\n        'id': eid,\n        'status': e.get('status'),\n        'conclusion': e.get('conclusion'),\n        'created_at': e.get('created_at'),\n        'completed_at': e.get('completed_at'),\n    }\n    \n    # Model\n    params['model'] = spec.get('model_name', spec.get('model', None))\n    \n    # Server/GPU\n    params['server'] = spec.get('server')\n    params['gpu'] = spec.get('gpu')\n    \n    # Data\n    params['data_path'] = spec.get('data_path')\n    params['data_count'] = spec.get('data_count')\n    \n    # Dataset name from data_path or command\n    dp = str(spec.get('data_path', '') or cmd or eid)\n    dataset = None\n    if 'conll2003' in dp.lower() or 'conll' in dp.lower(): dataset = 'CoNLL-2003'\n    elif 'scierc' in dp.lower(): dataset = 'SciERC'\n    elif 'fewnerd' in dp.lower() or 'few-nerd' in dp.lower(): dataset = 'FewNERD'\n    elif 'wnut17' in dp.lower() or 'wnut' in dp.lower(): dataset = 'WNUT-17'\n    elif 'spider' in dp.lower(): dataset = 'Spider'\n    elif 'humaneval' in dp.lower(): dataset = 'HumanEval'\n    elif 'tacred' in dp.lower(): dataset = 'TACRED'\n    elif 'fewrel' in dp.lower(): dataset = 'FewRel'\n    elif 'ace05' in dp.lower(): dataset = 'ACE05'\n    elif 'docred' in dp.lower(): dataset = 'DocRED'\n    \n    # Also check eid\n    if dataset is None:\n        eid_l = eid.lower()\n        if 'conll' in eid_l: dataset = 'CoNLL-2003'\n        elif 'scierc' in eid_l: dataset = 'SciERC'\n        elif 'fewnerd' in eid_l: dataset = 'FewNERD'\n        elif 'wnut' in eid_l: dataset = 'WNUT-17'\n    \n    # Also check spec.dataset\n    if dataset is None:\n        ds = spec.get('dataset', '')\n        if ds:\n            dataset = ds\n    \n    params['dataset'] = dataset\n    \n    # Seed\n    params['seed'] = spec.get('seed')\n    \n    # N samples\n    n = spec.get('n_samples')\n    if n is None:\n        m = re.search(r'--n_samples\\s+(\\d+)', cmd)\n        if m: n = int(m.group(1))\n    params['n_samples'] = n\n    \n    # Temperature\n    t = spec.get('temperature')\n    if t is None:\n        m = re.search(r'--temperature\\s+([\\d.]+)', cmd)\n        if m: t = float(m.group(1))\n    params['temperature'] = t\n    \n    # Method/LoRA\n    params['method'] = spec.get('method')\n    params['lora_config'] = spec.get('lora_config')\n    \n    # Training params from spec\n    params['epochs'] = spec.get('epochs', spec.get('epoch'))\n    params['lr'] = spec.get('learning_rate', spec.get('lr'))\n    params['batch_size'] = spec.get('batch_size')\n    params['optimizer'] = spec.get('optimizer')\n    params['framework'] = spec.get('framework')\n    params['plan_id'] = spec.get('plan_id')\n    \n    # From metrics\n    if 'epoch' in metrics and params['epochs'] is None:\n        params['epochs'] = metrics.get('epoch')\n    if 'lora_rank' in metrics:\n        params['lora_rank_from_metrics'] = metrics['lora_rank']\n    if 'lora_alpha' in metrics:\n        params['lora_alpha_from_metrics'] = metrics['lora_alpha']\n    \n    # Training duration\n    params['train_runtime'] = spec.get('train_runtime')\n    if 'train_runtime_hours' in metrics:\n        params['train_runtime_hours'] = metrics['train_runtime_hours']\n    if 'train_runtime_sec' in metrics:\n        params['train_runtime_sec'] = metrics['train_runtime_sec']\n    if 'training_time_hours' in metrics:\n        params['training_time_hours'] = metrics['training_time_hours']\n    \n    # Total steps\n    params['total_steps'] = spec.get('total_steps', metrics.get('total_steps'))\n    \n    # Checkpoint\n    params['checkpoint_path'] = spec.get('checkpoint_path', spec.get('checkpoint_source'))\n    \n    # Hypothesis\n    params['hypothesis'] = (e.get('hypothesis') or spec.get('hypothesis') or '')[:300]\n    \n    # Notes\n    params['notes'] = (e.get('notes') or spec.get('note') or spec.get('notes') or '')[:300]\n    \n    # API-specific\n    if 'base_url' in cmd:\n        m = re.search(r'--base_url\\s+(\\S+)', cmd)\n        if m: params['api_base_url'] = m.group(1)\n    params['max_workers'] = spec.get('max_workers')\n    params['n_instances'] = spec.get('n_instances')\n    \n    # Metrics (full)\n    params['metrics'] = metrics\n    \n    return params\n\nall_params = []\nfor eid, e in exps.items():\n    all_params.append(extract_params(eid, e))\n\n# Save full extraction\nwith open('/tmp/all_hyperparams.json', 'w') as f:\n    json.dump(all_params, f, indent=2, ensure_ascii=False, default=str)\n\nprint(f\"Extracted {len(all_params)} experiments\")\n\n# Count experiments missing key fields\nmissing_model = sum(1 for p in all_params if not p['model'])\nmissing_dataset = sum(1 for p in all_params if not p['dataset'])\nmissing_seed = sum(1 for p in all_params if p['seed'] is None)\nmissing_n = sum(1 for p in all_params if p['n_samples'] is None)\nmissing_t = sum(1 for p in all_params if p['temperature'] is None)\n\nprint(f\"\\nMissing fields:\")\nprint(f\"  model: {missing_model}\")\nprint(f\"  dataset: {missing_dataset}\")\nprint(f\"  seed: {missing_seed}\")\nprint(f\"  n_samples: {missing_n}\")\nprint(f\"  temperature: {missing_t}\")\n\n# List experiments missing model\nprint(f\"\\nExperiments missing model name:\")\nfor p in sorted(all_params, key=lambda x: x['id']):\n    if not p['model']:\n        print(f\"  {p['id']}: conclusion={p['conclusion']}\")\n\nPYEOF\n",
  "description": "Extract all hyperparameters from all experiments into structured JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "588266c6-44a2-4b53-a435-6928c50a3b2f",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFd6EistoYQhohQYZh7c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49b87f10-e8ed-433e-b99a-99f25213d4cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KD75BKHHqChYqZBz85nJXd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2597,
      "cache_read_input_tokens": 52961,
      "output_tokens": 2023,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2597
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2023,
          "cache_read_input_tokens": 52961,
          "cache_creation_input_tokens": 2597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2597,
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

_source line 37 · 2026-05-21T11:19:39.521Z_

<details><summary>↩ Tool result · `toolu_01VM9ytzEL2zY4BRiqA848my`</summary>

```text
Extracted 256 experiments

Missing fields:
  model: 41
  dataset: 46
  seed: 42
  n_samples: 116
  temperature: 109

Experiments missing model name:
  dgs_pilot: conclusion=killed
  exp001_seed123: conclusion=killed
  exp001_seed456: conclusion=killed
  exp008_re_n16: conclusion=killed
  exp_001_n16_seed123_full: conclusion=killed
  exp_001_n16_seed456_full: conclusion=killed
  exp_001_ner_n16_scierc: conclusion=success
  exp_002_merge_conll2003: conclusion=killed
  exp_002_ner_conll2003: conclusion=success
  exp_003_ner_wnut17: conclusion=negative
  exp_008_re_n16_full: conclusion=killed
  exp_017_llama_conll_n8_t07: conclusion=success
  exp_020_fewnerd_smoke: conclusion=success
  exp_021_fewnerd_full: conclusion=success
  exp_025_n32: conclusion=success
  exp_026_T05: conclusion=success
  exp_026_T08: conclusion=success
  exp_026_T12: conclusion=success
  exp_026_t05: conclusion=success
  exp_026_t08: conclusion=success
  exp_030_conll_t12: conclusion=killed
  exp_031_fewnerd_t12: conclusion=killed
  exp_14b_inference_scierc: conclusion=killed
  exp_asb_adaptive_budget: conclusion=negative
  exp_backup1_het_temp: conclusion=negative
  exp_conll_n16_s123: conclusion=failed
  exp_conll_n16_s456: conclusion=failed
  exp_e_theta_adaptive: conclusion=negative
  exp_fewnerd_n16_s123: conclusion=success
  exp_fewnerd_n16_s42: conclusion=success
  exp_freeform_seed789: conclusion=success
  exp_freeform_seed789_v3: conclusion=success
  exp_qwen3_4b_conll_scs_inference: conclusion=success
  exp_qwen3_4b_scierc_finetune: conclusion=killed
  exp_qwen3_4b_scierc_merge_inference: conclusion=killed
  exp_scierc_t05_s456: conclusion=success
  exp_scierc_t08_s456: conclusion=success
  exp_scierc_t12_s456: conclusion=success
  hidden_state_probe_conll_full: conclusion=killed
  hidden_state_probe_conll_v2: conclusion=killed
  mbr_pilot: conclusion=killed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49b87f10-e8ed-433e-b99a-99f25213d4cb",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "7dd64637-5881-477d-a117-5c0051977aea",
  "sourceToolAssistantUUID": "49b87f10-e8ed-433e-b99a-99f25213d4cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T11:19:52.141Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JXoid7aqCjRkhwzSMxvJ9S`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/all_hyperparams.json') as f:\n    all_params = json.load(f)\n\n# For the missing model experiments, let's check the raw data for clues\nwith open('/tmp/all_exps.json') as f:\n    exps = json.load(f)\n\n# Check those with missing models that have conclusion=success\nmissing_success = [p for p in all_params if not p['model'] and p['conclusion'] in ('success', 'negative')]\nfor p in sorted(missing_success, key=lambda x: x['id']):\n    eid = p['id']\n    e = exps[eid]\n    spec = e.get('spec', {})\n    cmd = spec.get('command', '') or ''\n    hyp = (e.get('hypothesis') or spec.get('hypothesis') or '')\n    \n    # Try to infer model from command or hypothesis\n    model_guess = 'UNKNOWN'\n    cmd_lower = cmd.lower()\n    hyp_lower = hyp.lower()\n    \n    if 'qwen3-8b' in cmd_lower or 'qwen3-8b' in hyp_lower: model_guess = 'Qwen3-8B (inferred)'\n    elif 'qwen3-4b' in cmd_lower or 'qwen3-4b' in hyp_lower or '4b' in eid.lower(): model_guess = 'Qwen3-4B (inferred)'\n    elif 'llama' in cmd_lower or 'llama' in hyp_lower: model_guess = 'LLaMA-3.1-8B (inferred)'\n    elif 'qwen' in cmd_lower or 'qwen' in hyp_lower: model_guess = 'Qwen (inferred)'\n    elif 'merged' in cmd_lower: model_guess = 'merged checkpoint (inferred)'\n    \n    # Try from checkpoint path\n    cp = spec.get('checkpoint_path', '') or ''\n    if 'qwen3-8b' in cp.lower(): model_guess = 'Qwen3-8B (from checkpoint)'\n    elif 'qwen3-4b' in cp.lower(): model_guess = 'Qwen3-4B (from checkpoint)'\n    elif 'llama' in cp.lower(): model_guess = 'LLaMA (from checkpoint)'\n    elif 'qwen25' in cp.lower() or 'qwen2.5' in cp.lower(): model_guess = 'Qwen2.5 (from checkpoint)'\n    \n    print(f\"{eid}: {model_guess}\")\n    if model_guess == 'UNKNOWN':\n        print(f\"  cmd: {cmd[:200]}\")\n        print(f\"  hyp: {hyp[:200]}\")\n        print(f\"  cp: {cp}\")\n        print(f\"  spec keys: {list(spec.keys())}\")\n\nPYEOF\n",
  "description": "Infer model names for experiments with missing model field"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7dd64637-5881-477d-a117-5c0051977aea",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFd8PCAozJU4U8t1wHDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8b3c203-2f43-4cad-9d8b-262bb451b591",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKJeJT8vSomrtCeLbVu9a7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2715,
      "cache_read_input_tokens": 55558,
      "output_tokens": 815,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2715
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 815,
          "cache_read_input_tokens": 55558,
          "cache_creation_input_tokens": 2715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2715,
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

_source line 39 · 2026-05-21T11:19:52.471Z_

<details><summary>↩ Tool result · `toolu_01JXoid7aqCjRkhwzSMxvJ9S`</summary>

```text
exp_001_ner_n16_scierc: Qwen3-8B (inferred)
exp_002_ner_conll2003: Qwen3-8B (inferred)
exp_003_ner_wnut17: UNKNOWN
  cmd: 
  hyp: WNUT-17 NER fine-tune + inference: initial attempt on social media domain. Tests if structural signals work when model capability is low on noisy text with novel entity types.
  cp: 
  spec keys: ['merged_model_path', 'pilot_command', 'pilot_pid', 'pilot_server', 'pilot_started_at', 'test_samples']
exp_017_llama_conll_n8_t07: LLaMA-3.1-8B (inferred)
exp_020_fewnerd_smoke: Qwen3-8B (inferred)
exp_021_fewnerd_full: UNKNOWN
  cmd: 
  hyp: Full Few-NERD LoRA fine-tune (rank=32, α=64, 3 epochs) on SUPERVISED coarse 8-type NER (131k train). 4-GPU DDP on autodl-5090. Post-training: N=8 inference on full test set, T=1.0, seed=42, collect lo
  cp: output/exp_021_fewnerd_full/checkpoint-6177
  spec keys: ['gpu', 'gpu_count', 'training_mode', 'checkpoint_path', 'log_path']
exp_025_n32: Qwen3-8B (from checkpoint)
exp_026_T05: Qwen3-8B (inferred)
exp_026_T08: Qwen3-8B (inferred)
exp_026_T12: Qwen3-8B (inferred)
exp_026_t05: Qwen3-8B (from checkpoint)
exp_026_t08: Qwen3-8B (from checkpoint)
exp_asb_adaptive_budget: UNKNOWN
  cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/autodl-tmp/struct_self_consist_ie/artifacts/experiments/asb/run_asb.py --data_paths /root/autodl-tmp/stru
  hyp: Instance-level features from cheap N=2 subsamples (degeneracy, agreement, entity count, logprob variance, text length) can predict optimal per-instance sample count, enabling adaptive budget allocatio
  cp: output/exp_asb_adaptive_budget/asb_results.json
  spec keys: ['command', 'server', 'gpu', 'pid', 'log_path', 'submitted_at', 'submitted_via', 'backend', 'account', 'checkpoint_path', 'wall_clock_seconds', 'gpu_hours']
exp_backup1_het_temp: UNKNOWN
  cmd: bash /root/autodl-tmp/struct_self_consist_ie/run_het_temp_all.sh
  hyp: Heterogeneous-Temperature Sampling: MRSC/LSC negative results prove entity-level correction cannot close the selection gap. F4 degeneracy analysis shows T=0.7 has ~62% degeneracy (too homogeneous) whi
  cp: N/A
  spec keys: ['command', 'server', 'gpu', 'pid', 'log_path', 'submitted_at', 'submitted_via', 'backend', 'account', 'checkpoint_path', 'wall_clock_seconds', 'gpu_hours']
exp_e_theta_adaptive: UNKNOWN
  cmd: 
  hyp: Threshold-Adaptive SC: N inverse scaling (D191) proves θ choice determines scaling direction. A learned θ predictor (input: degeneracy_level, lp_variance, N, dataset, model) can select per-instance op
  cp: N/A (CPU predictor, no model checkpoint)
  spec keys: ['checkpoint_path', 'log_path']
exp_fewnerd_n16_s123: Qwen3-8B (inferred)
exp_fewnerd_n16_s42: Qwen3-8B (inferred)
exp_freeform_seed789: UNKNOWN
  cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python run_freeform_inference.py --seed 789 --num_samples 8 --temperatur
  hyp: Free-form SciERC seed=789: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.
  cp: 
  spec keys: ['command', 'server', 'gpu', 'pid', 'log_path', 'submitted_at', 'submitted_via', 'backend', 'account', 'wall_clock_seconds', 'gpu_hours']
exp_freeform_seed789_v3: UNKNOWN
  cmd: 
  hyp: Free-form SciERC seed=789 v3 (bugfix rerun): corrected version of free-form inference after fixing parsing/generation issues in v1/v2. Provides clean data point for 4-seed free-form analysis.
  cp: results/exp_freeform_ablation_seed789/
  spec keys: ['log_path', 'checkpoint_path']
exp_qwen3_4b_conll_scs_inference: Qwen3-4B (from checkpoint)
exp_scierc_t05_s456: Qwen3-8B (inferred)
exp_scierc_t08_s456: Qwen3-8B (inferred)
exp_scierc_t12_s456: Qwen3-8B (inferred)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8b3c203-2f43-4cad-9d8b-262bb451b591",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "b470cd3a-daf1-408f-96dc-ff2901e24b10",
  "sourceToolAssistantUUID": "f8b3c203-2f43-4cad-9d8b-262bb451b591",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-21T11:19:55.344Z_

Now let me produce the final comprehensive structured summary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b470cd3a-daf1-408f-96dc-ff2901e24b10",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFd9Lh8QzaLGCJv5VsJK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d40e8861-23b6-4d93-89b2-f8cee71309b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MA9Rc1QmoX24Y2kMCZm9X8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2282,
      "cache_read_input_tokens": 58273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2282,
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

_source line 41 · 2026-05-21T11:20:23.346Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MvGeyuG6zGu9RV1gx4cfRm`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\n\nwith open('/tmp/all_exps.json') as f:\n    exps = json.load(f)\n\n# ======================================================================\n# COMPREHENSIVE STRUCTURED SUMMARY\n# ======================================================================\n\ndef get_val(spec, *keys, default=None):\n    for k in keys:\n        v = spec.get(k)\n        if v is not None:\n            return v\n    return default\n\ndef extract_from_cmd(cmd, flag):\n    m = re.search(rf'--{flag}\\s+(\\S+)', cmd)\n    return m.group(1) if m else None\n\nprint(\"=\" * 120)\nprint(\"COMPREHENSIVE HYPERPARAMETER EXTRACTION — ALL 256 DONE EXPERIMENTS\")\nprint(\"=\" * 120)\n\n# ======================================================================\n# SECTION A: FINE-TUNING EXPERIMENTS (30)\n# ======================================================================\nprint(\"\\n\")\nprint(\"=\" * 120)\nprint(\"SECTION A: FINE-TUNING EXPERIMENTS\")\nprint(\"=\" * 120)\n\nft_table = []\nft_ids = [\n    'ft_001', 'ft_002', 'ft_002_v2',\n    'exp_002_merge_conll2003', 'exp_003_wnut17_v2', 'exp_007_ner_multi_model',\n    'exp_017_llama_conll_finetune', 'exp_023_lora_rank8',\n    'exp_027_mlp_verifier', 'exp_028', 'exp_028_fewnerd_5epoch',\n    'exp_029a', 'exp_029b',\n    'exp_b1_scd_conll_control', 'exp_b1_scd_fewnerd_curriculum_q',\n    'exp_b1_scd_fewnerd_standard', 'exp_b1_scd_threshold_ablation',\n    'exp_e2_pretrained_conll', 'exp_e2_pretrained_scierc',\n    'exp_llama_fewnerd_lora',\n    'exp_qwen25_14b_fewnerd', 'exp_qwen25_32b_fewnerd', 'exp_qwen25_7b_fewnerd',\n    'exp_qwen3_4b_conll_finetune', 'exp_qwen3_4b_conll_finetune_resume',\n    'exp_qwen3_4b_scierc_finetune', 'exp_qwen3_4b_scierc_finetune_v2',\n    'exp_qwen3_4b_scierc_finetune_v3', 'exp_qwen3_4b_scierc_finetune_v4',\n    'exp_wnut17_qwen25_7b',\n]\n\nfor eid in sorted(ft_ids):\n    e = exps[eid]\n    spec = e.get('spec', {})\n    metrics = e.get('metrics', {})\n    cmd = spec.get('command', '') or ''\n    method = spec.get('method', '') or ''\n    lora = spec.get('lora_config', {})\n    \n    # Model\n    model = spec.get('model_name', spec.get('model', ''))\n    \n    # LoRA details\n    lora_rank = None\n    lora_alpha = None\n    target_modules = None\n    trainable_params = None\n    \n    if lora:\n        target_modules = lora.get('target_modules')\n        trainable_params = lora.get('trainable_params')\n    \n    if 'r=8' in method: lora_rank, lora_alpha = 8, 16\n    elif 'r=16' in method: lora_rank, lora_alpha = 16, 32\n    elif 'r=32' in method or 'rank=32' in method: lora_rank, lora_alpha = 32, 64\n    elif 'rank=32' in str(spec): lora_rank, lora_alpha = 32, 64\n    \n    if metrics.get('lora_rank'): lora_rank = metrics['lora_rank']\n    if metrics.get('lora_alpha'): lora_alpha = metrics['lora_alpha']\n    \n    # Epochs\n    epochs = spec.get('epochs', spec.get('epoch', lora.get('epochs')))\n    if not epochs: epochs = metrics.get('epoch', metrics.get('epochs'))\n    \n    # Batch size\n    batch = spec.get('batch_size', lora.get('batch_size'))\n    \n    # LR\n    lr = spec.get('learning_rate', spec.get('lr'))\n    \n    # Steps\n    steps = spec.get('total_steps', lora.get('total_steps', metrics.get('total_steps')))\n    \n    # Train loss\n    train_loss = spec.get('train_loss', metrics.get('train_loss', metrics.get('final_loss')))\n    eval_loss = spec.get('eval_loss', metrics.get('eval_loss', metrics.get('best_eval_loss')))\n    \n    # Runtime\n    runtime = spec.get('train_runtime', '')\n    if not runtime:\n        if metrics.get('train_runtime_hours'):\n            runtime = f\"{metrics['train_runtime_hours']}h\"\n        elif metrics.get('training_time_hours'):\n            runtime = f\"{metrics['training_time_hours']}h\"\n        elif metrics.get('train_runtime_sec'):\n            runtime = f\"{metrics['train_runtime_sec']}s\"\n    \n    # Dataset\n    dp = str(spec.get('data_path', '') or cmd or eid).lower()\n    dataset = None\n    if 'conll' in dp: dataset = 'CoNLL-2003'\n    elif 'scierc' in dp: dataset = 'SciERC'\n    elif 'fewnerd' in dp: dataset = 'FewNERD'\n    elif 'wnut' in dp: dataset = 'WNUT-17'\n    if not dataset:\n        eid_l = eid.lower()\n        if 'conll' in eid_l: dataset = 'CoNLL-2003'\n        elif 'scierc' in eid_l: dataset = 'SciERC'\n        elif 'fewnerd' in eid_l: dataset = 'FewNERD'\n        elif 'wnut' in eid_l: dataset = 'WNUT-17'\n    \n    print(f\"\\n--- {eid} ---\")\n    print(f\"  Conclusion: {e.get('conclusion')}\")\n    print(f\"  Model: {model or 'NOT SPECIFIED'}\")\n    print(f\"  Dataset: {dataset or 'NOT SPECIFIED'}\")\n    print(f\"  Data count: {spec.get('data_count', 'N/S')}\")\n    print(f\"  Seed: {spec.get('seed', 'N/S')}\")\n    print(f\"  LoRA rank: {lora_rank or 'N/S'}\")\n    print(f\"  LoRA alpha: {lora_alpha or 'N/S'}\")\n    if target_modules: print(f\"  Target modules: {target_modules}\")\n    if trainable_params: print(f\"  Trainable params: {trainable_params}\")\n    print(f\"  Epochs: {epochs or 'N/S'}\")\n    print(f\"  Batch size: {batch or 'N/S'}\")\n    print(f\"  Learning rate: {lr or 'N/S'}\")\n    print(f\"  Total steps: {steps or 'N/S'}\")\n    print(f\"  Train loss: {train_loss or 'N/S'}\")\n    print(f\"  Eval loss: {eval_loss or 'N/S'}\")\n    print(f\"  Training duration: {runtime or 'N/S'}\")\n    print(f\"  Server: {spec.get('server', 'N/S')}\")\n    print(f\"  GPU: {spec.get('gpu', 'N/S')}\")\n    if method: print(f\"  Method: {method}\")\n    if spec.get('framework'): print(f\"  Framework: {spec['framework']}\")\n    print(f\"  Checkpoint: {spec.get('checkpoint_path', 'N/S')}\")\n\nPYEOF\n",
  "description": "Generate Section A (Fine-tuning) of comprehensive summary",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d40e8861-23b6-4d93-89b2-f8cee71309b4",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFd9Lh8QzaLGCJv5VsJK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bee2d4e-1185-460e-9505-3ae7a39340d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MA9Rc1QmoX24Y2kMCZm9X8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2282,
      "cache_read_input_tokens": 58273,
      "output_tokens": 2219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2282
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2219,
          "cache_read_input_tokens": 58273,
          "cache_creation_input_tokens": 2282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2282,
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

_source line 42 · 2026-05-21T11:20:23.464Z_

<details><summary>↩ Tool result · `toolu_01MvGeyuG6zGu9RV1gx4cfRm`</summary>

```text
========================================================================================================================
COMPREHENSIVE HYPERPARAMETER EXTRACTION — ALL 256 DONE EXPERIMENTS
========================================================================================================================


========================================================================================================================
SECTION A: FINE-TUNING EXPERIMENTS
========================================================================================================================

--- exp_002_merge_conll2003 ---
  Conclusion: killed
  Model: NOT SPECIFIED
  Dataset: CoNLL-2003
  Data count: N/S
  Seed: N/S
  LoRA rank: N/S
  LoRA alpha: N/S
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: N/S
  Eval loss: N/S
  Training duration: N/S
  Server: autodl-5090
  GPU: ['cuda:0']
  Checkpoint: N/S

--- exp_003_wnut17_v2 ---
  Conclusion: negative
  Model: Qwen3-8B
  Dataset: WNUT-17
  Data count: 1637
  Seed: 42
  LoRA rank: N/S
  LoRA alpha: N/S
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: N/S
  Eval loss: N/S
  Training duration: N/S
  Server: autodl-5090
  GPU: N/S
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-lora

--- exp_007_ner_multi_model ---
  Conclusion: success
  Model: LLaMA-3.1-8B-Instruct
  Dataset: NOT SPECIFIED
  Data count: 1861
  Seed: 42
  LoRA rank: N/S
  LoRA alpha: 64
  Epochs: 5
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: 0.0767
  Eval loss: 0.1049
  Training duration: 1494.5s
  Server: gpu-5090-4x-2
  GPU: ['cuda:0']
  Checkpoint: N/S

--- exp_017_llama_conll_finetune ---
  Conclusion: success
  Model: Meta-Llama-3.1-8B-Instruct
  Dataset: CoNLL-2003
  Data count: 14037
  Seed: 42
  LoRA rank: N/S
  LoRA alpha: N/S
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: N/S
  Eval loss: N/S
  Training duration: N/S
  Server: autodl-5090
  GPU: ['cuda:0']
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-conll2003-lora-3ep

--- exp_023_lora_rank8 ---
  Conclusion: success
  Model: Qwen/Qwen3-8B
  Dataset: NOT SPECIFIED
  Data count: 1861
  Seed: 42
  LoRA rank: 8
  LoRA alpha: 16
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: 585
  Train loss: 0.1018
  Eval loss: 0.0776
  Training duration: N/S
  Server: autodl-5090
  GPU: cuda:2
  Method: LoRA r=8 alpha=16, 5 epochs, batch=2 grad_accum=8 gradient_checkpointing=true
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-rank8

--- exp_027_mlp_verifier ---
  Conclusion: negative
  Model: sklearn LR/MLP/RF
  Dataset: NOT SPECIFIED
  Data count: 529
  Seed: 42,123,456
  LoRA rank: N/S
  LoRA alpha: N/S
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: N/S
  Eval loss: N/S
  Training duration: N/S
  Server: a100
  GPU: N/S
  Checkpoint: N/A

--- exp_028 ---
  Conclusion: negative
  Model: Qwen3-8B LoRA rank=32
  Dataset: FewNERD
  Data count: 131767
  Seed: 42
  LoRA rank: 32
  LoRA alpha: 64
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: 0.0189
  Eval loss: 0.0311
  Training duration: N/S
  Server: autodl-5090
  GPU: N/S
  Checkpoint: checkpoints/qwen3-8b-fewnerd-5epoch-lora

--- exp_028_fewnerd_5epoch ---
  Conclusion: negative
  Model: Qwen3-8B LoRA rank=32
  Dataset: FewNERD
  Data count: 131767
  Seed: 42
  LoRA rank: 32
  LoRA alpha: 64
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: N/S
  Eval loss: N/S
  Training duration: N/S
  Server: autodl-5090
  GPU: cuda:0,1,2,3
  Checkpoint: checkpoints/qwen3-8b-fewnerd-5epoch-lora

--- exp_029a ---
  Conclusion: success
  Model: Qwen3-8B LoRA rank=32
  Dataset: SciERC
  Data count: 1861
  Seed: 42
  LoRA rank: 32
  LoRA alpha: 64
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: N/S
  Eval loss: N/S
  Training duration: N/S
  Server: autodl-5090
  GPU: cuda:0
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-3epoch-lora

--- exp_029b ---
  Conclusion: success
  Model: Qwen3-8B
  Dataset: SciERC
  Data count: 1861
  Seed: 42
  LoRA rank: N/S
  LoRA alpha: N/S
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: N/S
  Eval loss: N/S
  Training duration: N/S
  Server: autodl-5090
  GPU: cuda:1
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-10epoch-lora/

--- exp_b1_scd_conll_control ---
  Conclusion: negative
  Model: Qwen3-8B-FT-CoNLL
  Dataset: CoNLL-2003
  Data count: 3453
  Seed: 42
  LoRA rank: N/S
  LoRA alpha: N/S
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: 0.0359
  Eval loss: N/S
  Training duration: N/S
  Server: autodl-5090-b
  GPU: N/S
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll-scd-lora

--- exp_b1_scd_fewnerd_curriculum_q ---
  Conclusion: negative
  Model: Qwen3-8B-FT
  Dataset: FewNERD
  Data count: 32565
  Seed: 43
  LoRA rank: N/S
  LoRA alpha: N/S
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: N/S
  Eval loss: N/S
  Training duration: N/S
  Server: autodl-5090-b
  GPU: N/S
  Checkpoint: N/S

--- exp_b1_scd_fewnerd_standard ---
  Conclusion: negative
  Model: Qwen3-8B-FT
  Dataset: FewNERD
  Data count: 32565
  Seed: 42
  LoRA rank: N/S
  LoRA alpha: N/S
  Epochs: 2
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: 0.023
  Eval loss: 0.0329
  Training duration: 7.14h
  Server: autodl-5090-b
  GPU: N/S
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/

--- exp_b1_scd_threshold_ablation ---
  Conclusion: failed
  Model: Qwen3-8B-FT
  Dataset: FewNERD
  Data count: 32565
  Seed: 42
  LoRA rank: N/S
  LoRA alpha: N/S
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: N/S
  Eval loss: N/S
  Training duration: N/S
  Server: autodl-5090-b
  GPU: N/S
  Checkpoint: N/S

--- exp_e2_pretrained_conll ---
  Conclusion: success
  Model: Qwen2.5-7B-Instruct
  Dataset: CoNLL-2003
  Data count: 3453
  Seed: 42
  LoRA rank: N/S
  LoRA alpha: N/S
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: N/S
  Eval loss: N/S
  Training duration: N/S
  Server: autodl-5090
  GPU: ['cuda:2']
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_conll/

--- exp_e2_pretrained_scierc ---
  Conclusion: negative
  Model: Qwen2.5-7B-Instruct
  Dataset: SciERC
  Data count: 100
  Seed: 42
  LoRA rank: N/S
  LoRA alpha: N/S
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: N/S
  Eval loss: N/S
  Training duration: N/S
  Server: autodl-5090-c
  GPU: ['cuda:3']
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_scierc/

--- exp_llama_fewnerd_lora ---
  Conclusion: success
  Model: LLaMA-Few-NERD-LoRA
  Dataset: FewNERD
  Data count: -1
  Seed: 42
  LoRA rank: N/S
  LoRA alpha: N/S
  Epochs: 3
  Batch size: N/S
  Learning rate: N/S
  Total steps: 24708
  Train loss: 0.0516
  Eval loss: 0.0323
  Training duration: 15.35h
  Server: autodl-5090
  GPU: cuda:1
  Checkpoint: N/S

--- exp_qwen25_14b_fewnerd ---
  Conclusion: success
  Model: Qwen2.5-14B-Instruct
  Dataset: FewNERD
  Data count: 131767
  Seed: 42
  LoRA rank: N/S
  LoRA alpha: N/S
  Epochs: 5
  Batch size: N/S
  Learning rate: N/S
  Total steps: 41180
  Train loss: 0.0348
  Eval loss: 0.0323
  Training duration: 29.8h
  Server: autodl-5090-c
  GPU: N/S
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-14b-fewnerd-qlora-s42/

--- exp_qwen25_32b_fewnerd ---
  Conclusion: success
  Model: Qwen2.5-32B-Instruct
  Dataset: FewNERD
  Data count: 131767
  Seed: 42
  LoRA rank: 32
  LoRA alpha: 64
  Epochs: 5
  Batch size: N/S
  Learning rate: 2e-4
  Total steps: 41180
  Train loss: N/S
  Eval loss: 0.0334
  Training duration: 38.5h
  Server: autodl-5090
  GPU: N/S
  Method: QLoRA-4bit-nf4 (rank=32, alpha=64, target=all)
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-32b-fewnerd-qlora-s42/checkpoint-32000

--- exp_qwen25_7b_fewnerd ---
  Conclusion: success
  Model: Qwen2.5-7B-Instruct
  Dataset: FewNERD
  Data count: 131767
  Seed: 42
  LoRA rank: 32
  LoRA alpha: 64
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: N/S
  Eval loss: N/S
  Training duration: N/S
  Server: autodl-5090-c
  GPU: N/S
  Method: QLoRA 4-bit nf4, rank=32, alpha=64, 5 epochs, lr=2e-4, effective_batch=32
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-fewnerd-qlora-s42

--- exp_qwen3_4b_conll_finetune ---
  Conclusion: success
  Model: Qwen3-4B
  Dataset: CoNLL-2003
  Data count: 14041
  Seed: 42
  LoRA rank: N/S
  LoRA alpha: N/S
  Target modules: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
  Trainable params: 66M / 4.09B (1.62%)
  Epochs: 5
  Batch size: 16
  Learning rate: N/S
  Total steps: 4390
  Train loss: 0.0086
  Eval loss: N/S
  Training duration: N/S
  Server: autodl-5090
  GPU: ['cuda:0']
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora

--- exp_qwen3_4b_conll_finetune_resume ---
  Conclusion: success
  Model: Qwen3-4B
  Dataset: CoNLL-2003
  Data count: 14042
  Seed: 42
  LoRA rank: N/S
  LoRA alpha: N/S
  Epochs: 5
  Batch size: 2 x 8 grad_accum
  Learning rate: 0.0002
  Total steps: 4390
  Train loss: 0.001136
  Eval loss: 0.0225
  Training duration: 1185.8s
  Server: autodl-5090
  GPU: cuda:1
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora

--- exp_qwen3_4b_scierc_finetune ---
  Conclusion: killed
  Model: NOT SPECIFIED
  Dataset: SciERC
  Data count: N/S
  Seed: N/S
  LoRA rank: N/S
  LoRA alpha: N/S
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: N/S
  Eval loss: N/S
  Training duration: N/S
  Server: autodl-5090
  GPU: ['cuda:3']
  Checkpoint: N/S

--- exp_qwen3_4b_scierc_finetune_v2 ---
  Conclusion: failed
  Model: Qwen3-4B
  Dataset: SciERC
  Data count: 1861
  Seed: 42
  LoRA rank: N/S
  LoRA alpha: N/S
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: N/S
  Eval loss: N/S
  Training duration: N/S
  Server: autodl-5090
  GPU: cuda:3
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-scierc-lora/

--- exp_qwen3_4b_scierc_finetune_v3 ---
  Conclusion: failed
  Model: Qwen3-4B
  Dataset: SciERC
  Data count: 551
  Seed: 42
  LoRA rank: N/S
  LoRA alpha: N/S
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: N/S
  Eval loss: N/S
  Training duration: N/S
  Server: autodl-5090
  GPU: ['cuda:2']
  Checkpoint: N/S

--- exp_qwen3_4b_scierc_finetune_v4 ---
  Conclusion: success
  Model: Qwen3-4B
  Dataset: SciERC
  Data count: 551
  Seed: 42
  LoRA rank: N/S
  LoRA alpha: N/S
  Epochs: 5
  Batch size: N/S
  Learning rate: N/S
  Total steps: 585
  Train loss: N/S
  Eval loss: 0.0898
  Training duration: N/S
  Server: autodl-5090
  GPU: cuda:0
  Checkpoint: N/S

--- exp_wnut17_qwen25_7b ---
  Conclusion: negative
  Model: Qwen2.5-7B-Instruct
  Dataset: WNUT-17
  Data count: 3404
  Seed: 42
  LoRA rank: 32
  LoRA alpha: 64
  Epochs: 5
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: N/S
  Eval loss: N/S
  Training duration: N/S
  Server: autodl-5090-c
  GPU: N/S
  Method: QLoRA 4-bit (bnb nf4), rank=32, alpha=64, all targets
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-wnut17-qlora-s42

--- ft_001 ---
  Conclusion: success
  Model: Qwen/Qwen3-8B
  Dataset: SciERC
  Data count: 1861
  Seed: 42
  LoRA rank: 16
  LoRA alpha: 32
  Epochs: 3
  Batch size: N/S
  Learning rate: N/S
  Total steps: N/S
  Train loss: 0.1099
  Eval loss: 0.0771
  Training duration: 0:17:49
  Server: autodl-5090
  GPU: N/S
  Method: LoRA r=16 alpha=32
  Framework: LLaMA Factory 0.9.4
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora/

--- ft_002 ---
  Conclusion: killed
  Model: Qwen/Qwen3-8B
  Dataset: NOT SPECIFIED
  Data count: 1861
  Seed: 42
  LoRA rank: 32
  LoRA alpha: 64
  Epochs: N/S
  Batch size: N/S
  Learning rate: N/S
  Total steps: 585
  Train loss: N/S
  Eval loss: N/S
  Training duration: N/S
  Server: autodl-5090
  GPU: cuda:1
  Method: LoRA r=32 alpha=64, 5 epochs, relation direction hint
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2

--- ft_002_v2 ---
  Conclusion: success
  Model: Qwen/Qwen3-8B
  Dataset: NOT SPECIFIED
  Data count: 1861
  Seed: 42
  LoRA rank: 32
  LoRA alpha: 64
  Epochs: 5
  Batch size: N/S
  Learning rate: N/S
  Total steps: 585
  Train loss: 0.0806
  Eval loss: 0.089
  Training duration: N/S
  Server: autodl-5090
  GPU: cuda:1
  Method: LoRA r=32 alpha=64, 5 epochs, batch=2 grad_accum=8 gradient_checkpointing=true
  Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bee2d4e-1185-460e-9505-3ae7a39340d4",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "591a4395-3167-4ca5-b3af-59dab6ea016d",
  "sourceToolAssistantUUID": "4bee2d4e-1185-460e-9505-3ae7a39340d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T11:20:50.518Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WbFELUVh2T8tuqcskdrnvM`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\n\nwith open('/tmp/all_exps.json') as f:\n    exps = json.load(f)\n\n# Extract key inference parameters for all inference experiments in compact tabular form\napi_models = ['gpt-5.5', 'gpt-4o', 'claude', 'gemini', 'deepseek', 'claude-sonnet', 'claude-sonnet-4', 'gpt', 'openai']\nfinetune_keywords = ['finetune', 'fine-tune', 'fine_tune', 'lora', 'sft', 'ft_']\n\ninference_ids = []\nfor eid, e in exps.items():\n    spec = e.get('spec', {})\n    model = (spec.get('model_name', '') or spec.get('model', '') or '').lower()\n    command = (spec.get('command', '') or '').lower()\n    eid_lower = eid.lower()\n    \n    is_api = any(am in model for am in api_models) or 'frontier' in eid_lower or 'base_url' in (spec.get('command','') or '') or 'spider' in eid_lower or 'humaneval' in eid_lower\n    is_finetune = any(kw in eid_lower for kw in finetune_keywords) or \\\n                  any(kw in command for kw in ['llamafactory', 'train_config']) or \\\n                  'lora_config' in spec or \\\n                  ('method' in spec and 'lora' in str(spec.get('method', '')).lower())\n    \n    if not is_api and not is_finetune:\n        inference_ids.append(eid)\n\nprint(\"=\" * 120)\nprint(f\"SECTION B: INFERENCE/EVALUATION EXPERIMENTS ({len(inference_ids)} total)\")\nprint(\"=\" * 120)\n\n# Print as a structured table\nheader = f\"{'ID':<50} {'Model':<30} {'Dataset':<12} {'N':<5} {'T':<5} {'Seed':<8} {'Data#':<7} {'Concl':<10} {'Server':<15}\"\nprint(f\"\\n{header}\")\nprint(\"-\" * len(header))\n\nfor eid in sorted(inference_ids):\n    e = exps[eid]\n    spec = e.get('spec', {})\n    cmd = spec.get('command', '') or ''\n    \n    model = spec.get('model_name', spec.get('model', '')) or ''\n    \n    # Infer model if missing\n    if not model:\n        cp = (spec.get('checkpoint_path', '') or '').lower()\n        hyp = (e.get('hypothesis', '') or spec.get('hypothesis', '') or '').lower()\n        if 'qwen3-8b' in cmd.lower() or 'qwen3-8b' in cp or 'qwen3-8b' in hyp: model = 'Qwen3-8B*'\n        elif 'qwen3-4b' in cmd.lower() or 'qwen3-4b' in cp or '4b' in eid.lower(): model = 'Qwen3-4B*'\n        elif 'llama' in cmd.lower() or 'llama' in cp: model = 'LLaMA-8B*'\n        elif 'qwen25' in cp or 'qwen2.5' in cp: model = 'Qwen2.5*'\n        elif 'merged' in cmd.lower() or 'merged' in cp: model = 'merged*'\n    \n    # Dataset\n    dp = (str(spec.get('data_path', '') or '') + ' ' + cmd + ' ' + eid).lower()\n    dataset = ''\n    if 'conll' in dp: dataset = 'CoNLL-2003'\n    elif 'scierc' in dp: dataset = 'SciERC'\n    elif 'fewnerd' in dp or 'few-nerd' in dp: dataset = 'FewNERD'\n    elif 'wnut' in dp: dataset = 'WNUT-17'\n    elif 'tacred' in dp: dataset = 'TACRED'\n    elif 'fewrel' in dp: dataset = 'FewRel'\n    elif 'ace05' in dp: dataset = 'ACE05'\n    elif 'docred' in dp: dataset = 'DocRED'\n    ds_name = spec.get('dataset', '')\n    if not dataset and ds_name: dataset = ds_name\n    \n    # N\n    n = spec.get('n_samples')\n    if n is None:\n        m = re.search(r'--n_samples\\s+(\\d+)', cmd)\n        if m: n = int(m.group(1))\n        elif '--num_samples' in cmd:\n            m = re.search(r'--num_samples\\s+(\\d+)', cmd)\n            if m: n = int(m.group(1))\n    \n    # T\n    t = spec.get('temperature')\n    if t is None:\n        m = re.search(r'--temperature\\s+([\\d.]+)', cmd)\n        if m: t = float(m.group(1))\n    \n    seed = spec.get('seed', '')\n    data_count = spec.get('data_count', '')\n    conclusion = e.get('conclusion', '')\n    server = spec.get('server', '')\n    \n    n_str = str(n) if n is not None else '-'\n    t_str = str(t) if t is not None else '-'\n    \n    print(f\"{eid:<50} {model:<30} {dataset:<12} {n_str:<5} {t_str:<5} {str(seed):<8} {str(data_count):<7} {conclusion:<10} {server:<15}\")\n\nPYEOF\n",
  "description": "Generate Section B (Inference) as compact table",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "591a4395-3167-4ca5-b3af-59dab6ea016d",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFdBf4ynW2SKBD1zYM9w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39507fba-be6d-4e3f-8770-4547222a92b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uUZh9ivdTKQnMzXJq1zQt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8069,
      "cache_read_input_tokens": 60555,
      "output_tokens": 1573,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8069
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1573,
          "cache_read_input_tokens": 60555,
          "cache_creation_input_tokens": 8069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8069,
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

_source line 44 · 2026-05-21T11:20:50.682Z_

<details><summary>↩ Tool result · `toolu_01WbFELUVh2T8tuqcskdrnvM`</summary>

```text
&lt;persisted-output>
Output too large (33.9KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a9ed86cb-a33f-4ec8-8078-d4b9402803ce/tool-results/be4t1fmcu.txt

Preview (first 2KB):
========================================================================================================================
SECTION B: INFERENCE/EVALUATION EXPERIMENTS (222 total)
========================================================================================================================

ID                                                 Model                          Dataset      N     T     Seed     Data#   Concl      Server         
------------------------------------------------------------------------------------------------------------------------------------------------------
dgs_pilot                                                                                      -     -                      killed                    
e1_component_wise_re_sj                            N/A (reuse pilot_004 samples)               -     -     42       397     negative   autodl-5090    
exp001_seed123                                     Qwen3-8B*                      SciERC       16    1.0                    killed     gpu-5090-4x-2  
exp001_seed456                                     Qwen3-8B*                      SciERC       16    1.0                    killed     gpu-5090-4x-2  
exp008_re_n16                                      Qwen3-8B*                      SciERC       16    1.0                    killed     gpu-5090-4x-2  
exp_001_n16_seed123                                qwen3-8b-scierc-merged-v2      SciERC       16    1.0   123      551     success    gpu-5090-4x-2  
exp_001_n16_seed123_full                           Qwen3-8B*                      SciERC       16    1.0                    killed     gpu-5090-4x-2  
exp_001_n16_seed456                                qwen3-8b-scierc-merged-v2      SciERC       16    1.0   456      551     success    autodl-5090    
exp_001_n16_seed456_full                           Qwen3-8B*                      SciERC       16    1.0                    killed     gpu-5090-4x-2  
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39507fba-be6d-4e3f-8770-4547222a92b4",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "94f6cfdf-18a2-407e-bc79-2d4caa1e4913",
  "sourceToolAssistantUUID": "39507fba-be6d-4e3f-8770-4547222a92b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T11:20:53.902Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KG4ic7pNR7P5nvxL7R9Jdg`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a9ed86cb-a33f-4ec8-8078-d4b9402803ce/tool-results/be4t1fmcu.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94f6cfdf-18a2-407e-bc79-2d4caa1e4913",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFdDdQ5foNqs6zdBEeRY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ed7e85f-b4cf-4d2b-be3f-481149f7608d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zVEZmibXfJQCAsu3ZUZeP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2152,
      "cache_read_input_tokens": 68624,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2152
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 68624,
          "cache_creation_input_tokens": 2152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2152,
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

_source line 46 · 2026-05-21T11:20:54.229Z_

<details><summary>↩ Tool result · `toolu_01KG4ic7pNR7P5nvxL7R9Jdg`</summary>

```text
1	========================================================================================================================
2	SECTION B: INFERENCE/EVALUATION EXPERIMENTS (222 total)
3	========================================================================================================================
4	
5	ID                                                 Model                          Dataset      N     T     Seed     Data#   Concl      Server         
6	------------------------------------------------------------------------------------------------------------------------------------------------------
7	dgs_pilot                                                                                      -     -                      killed                    
8	e1_component_wise_re_sj                            N/A (reuse pilot_004 samples)               -     -     42       397     negative   autodl-5090    
9	exp001_seed123                                     Qwen3-8B*                      SciERC       16    1.0                    killed     gpu-5090-4x-2  
10	exp001_seed456                                     Qwen3-8B*                      SciERC       16    1.0                    killed     gpu-5090-4x-2  
11	exp008_re_n16                                      Qwen3-8B*                      SciERC       16    1.0                    killed     gpu-5090-4x-2  
12	exp_001_n16_seed123                                qwen3-8b-scierc-merged-v2      SciERC       16    1.0   123      551     success    gpu-5090-4x-2  
13	exp_001_n16_seed123_full                           Qwen3-8B*                      SciERC       16    1.0                    killed     gpu-5090-4x-2  
14	exp_001_n16_seed456                                qwen3-8b-scierc-merged-v2      SciERC       16    1.0   456      551     success    autodl-5090    
15	exp_001_n16_seed456_full                           Qwen3-8B*                      SciERC       16    1.0                    killed     gpu-5090-4x-2  
16	exp_001_ner_n16_scierc                             Qwen3-8B*                      SciERC       16    1.0                    success    autodl-5090    
17	exp_001_ner_n16_seed123                            qwen3-8b-scierc-merged-v2      SciERC       16    1.0   123      551     success    autodl-5090    
18	exp_001_seed123_t10_full                           qwen3-8b-scierc-merged-v2      SciERC       16    1.0   123      551     negative   autodl-5090    
19	exp_001_seed123_v2                                 ft_002_v2                      SciERC       16    1.0   123      551     success    autodl-5090    
20	exp_001_seed123_v2_r1024                           qwen3-8b-scierc-merged-v2      SciERC       16    1.0   123      529     killed     autodl-5090    
21	exp_001_seed42_v2                                  ft_002_v2                      SciERC       16    1.0   42       551     success    autodl-5090    
22	exp_001_seed42_v2_r1024                            qwen3-8b-scierc-merged-v2      SciERC       16    1.0   42       9999    killed     autodl-5090    
23	exp_001_seed456_t10_full                           qwen3-8b-scierc-merged-v2      SciERC       16    1.0   456      551     negative   autodl-5090    
24	exp_001_seed456_v2                                 qwen3-8b-scierc-merged-v2      SciERC       16    1.0   456      551     negative   autodl-5090    
25	exp_001_seed456_v2_ner                             qwen3-8b-scierc-merged-v2      SciERC       16    1.0   456      551     success    autodl-5090    
26	exp_001_seed456_v2_ner_r1024                       qwen3-8b-scierc-merged-v2      SciERC       16    1.0   456      9999    killed     autodl-5090    
27	exp_002                                            qwen3-8b-conll2003-lora-merged CoNLL-2003   8     1.0   42       3453    success    autodl-5090    
28	exp_002_conll_n16                                  qwen3-8b-conll2003-merged      CoNLL-2003   16    1.0   42       3453    success    autodl-5090    
29	exp_002_conll_n16_r1024                            qwen3-8b-conll2003-merged      CoNLL-2003   16    1.0   42       3453    killed     autodl-5090    
30	exp_002_conll_n16_seed123                          Qwen3-8B                       CoNLL-2003   16    1.0   123      3453    success    autodl-5090    
31	exp_002_conll_n16_seed456                          Qwen3-8B                       CoNLL-2003   16    1.0   456      3453    success    autodl-5090    
32	exp_002_ner_conll2003                              Qwen3-8B*                      CoNLL-2003   8     1.0                    success    autodl-5090    
33	exp_003_ner_wnut17                                                                WNUT-17      -     -                      negative                  
34	exp_003_wnut17_eval                                qwen3-8b-wnut17-merged         WNUT-17      16    1.0   42       1287    success    autodl-5090    
35	exp_004_re_diagnostic                              N/A (reuse pilot_004 samples)               -     -     42       551     success    autodl-5090    
36	exp_004_v2                                         Qwen3-8B-SciERC-merged-v2                   -     -     42       551     success    autodl-5090    
37	exp_005                                            Qwen3-8B-SciERC-LoRA-v2                     -     -     42       551     success    local          
38	exp_005_v2                                         Qwen3-8B-SciERC-LoRA                        -     -     42       551     success    autodl-5090    
39	exp_006_v2                                         Qwen3-8B-SciERC-merged-v2      CoNLL-2003   -     -     42       4952    negative   autodl-5090    
40	exp_007_llama_inference                            Meta-Llama-3.1-8B-Instruct (LoRA fine-tuned on SciERC) SciERC       8     1.0   42       551     success    autodl-5090    
41	exp_007_llama_n16                                  llama3.1-8b-scierc-merged      SciERC       16    1.0   42       551     success    autodl-5090    
42	exp_007_llama_n16_r1024                            llama3.1-8b-scierc-merged      SciERC       16    1.0   42       9999    killed     autodl-5090    
43	exp_007_llama_scierc_seed123                       LLaMA-3.1-8B-Instruct (SciERC LoRA fine-tuned) SciERC       8     1.0   123      551     negative   autodl-5090    
44	exp_007_llama_seed123                              llama3.1-8b-scierc-merged      SciERC       8     1.0   123      551     negative   bjb1-21071     
45	exp_007_llama_seed456                              llama3.1-8b-scierc-merged      SciERC       8     1.0   456      551     negative   bjb1-21071     
46	exp_007_ner_llama                                  llama-3.1-8b-instruct (new fine-tune) SciERC       -     -                      killed                    
47	exp_008_re_n16                                     qwen3-8b-scierc-merged-v2      SciERC       16    1.0   42       551     success    gpu-5090-4x-2  
48	exp_008_re_n16_full                                Qwen3-8B*                      SciERC       16    1.0                    killed     gpu-5090-4x-2  
49	exp_008_re_n16_t10_full                            qwen3-8b-scierc-merged-v2      SciERC       16    1.0   42       551     negative   autodl-5090    
50	exp_008_re_n16_v2                                  ft_002_v2                      SciERC       16    1.0   42       551     negative   autodl-5090    
51	exp_008_re_seed123                                 qwen3-8b-scierc-merged-v2      SciERC       16    1.0   123      551     negative   bjb1-21071     
52	exp_009_capability_stratification                  analysis_only                  CoNLL-2003   -     -     42       4555    success    autodl-5090    
53	exp_009_v2                                         analysis                                    -     -     42       551     success    autodl-5090    
54	exp_009_v2_re_rerun                                cpu_analysis                                -     -     42       397     success    autodl-5090    
55	exp_010_selection_curves                           qwen3-8b-scierc-merged-v2      CoNLL-2003   -     -     42       551+397+3453 instances success    autodl-5090    
56	exp_011_ood_conll_to_scierc                        qwen3-8b-conll2003-merged      CoNLL-2003   8     1.0   42       551     negative   autodl-5090    
57	exp_011_ood_scierc_to_conll                        qwen3-8b-scierc-merged-v2      CoNLL-2003   8     1.0   42       3500    success    autodl-5090    
58	exp_012_logprob_baseline                           ft_002_v2 (qwen3-8b-scierc-merged-v2)              -     -     42       551     success    autodl-5090    
59	exp_012_rerun_1024                                 qwen3-8b-scierc-merged-v2      SciERC       8     1.0   42       551     success    autodl-5090    
60	exp_013_exact_match_voting                         N/A (reuse pilot_004 samples)               -     -     42       551     negative   autodl-5090    
61	exp_014_entity_majority_voting                     N/A (reuse pilot_004 samples)               -     -     42       551     success    autodl-5090    
62	exp_015_metrics_expansion                          N/A (reuse pilot_004 samples)               -     -     42       551     success    autodl-5090    
63	exp_015_v2                                         Qwen3-8B + LLaMA (multi-model)              -     -     42,123,456 (multi-seed) 9148    success    autodl-5090    
64	exp_016_rerun_1024_bootstrap                       N/A (statistical analysis)                  -     -     3-seed bootstrap (1000 iterations) 529     negative   local          
65	exp_016_signal_ensemble                            N/A (CPU-only analysis)                     -     -     42       551     success    autodl-5090    
66	exp_016_v2                                         analysis_only                               -     -     42       551     success    autodl-5090    
67	exp_017_llama_conll                                llama3.1-8b-conll2003-merged   CoNLL-2003   -     -     42       3453    success    autodl-5090    
68	exp_017_llama_conll_infer                          LLaMA-3.1-8B-Instruct          CoNLL-2003   8     1     42       3453    success    autodl-5090    
69	exp_017_llama_conll_n16                            llama3.1-8b-conll2003-merged   CoNLL-2003   16    1     42       3453    success    autodl-5090    
70	exp_017_llama_conll_n16_r1024                      llama3.1-8b-conll2003-merged   CoNLL-2003   16    1.0   42       3453    success    autodl-5090    
71	exp_017_llama_conll_n16_s123                       llama3.1-8b-conll2003-merged   CoNLL-2003   16    1.0   123      3453    success    autodl-5090    
72	exp_017_llama_conll_n16_s123_r1024                 llama3.1-8b-conll2003-merged   CoNLL-2003   16    1.0   123      3453    success    autodl-5090    
73	exp_017_llama_conll_n16_s456                       llama3.1-8b-conll2003-merged   CoNLL-2003   16    1.0   456      3453    success    autodl-5090    
74	exp_017_llama_conll_n16_s456_r1024                 llama3.1-8b-conll2003-merged   CoNLL-2003   16    1.0   456      3453    success    autodl-5090    
75	exp_017_llama_conll_n8_t07                         LLaMA-8B*                      CoNLL-2003   8     0.7                    success    autodl-5090    
76	exp_018_llama_scierc_seed123                       LLaMA-3.1-8B-SciERC-merged     SciERC       8     1.0   123      551     success    autodl-5090    
77	exp_018_llama_scierc_seed42_r1024                  LLaMA-3.1-8B-SciERC-merged     SciERC       8     1.0   42       551     success    autodl-5090    
78	exp_018_llama_scierc_seed456                       LLaMA-3.1-8B-SciERC-merged     SciERC       8     1.0   456      551     killed     autodl-5090    
79	exp_018_llama_scierc_seed456_r1024                 LLaMA-3.1-8B-SciERC-merged     SciERC       8     1.0   456      551     success    autodl-5090    
80	exp_018_qwen_scierc_seed123                        Qwen3-8B-SciERC-merged-v2      SciERC       8     1.0   123      551     success    autodl-5090    
81	exp_018_qwen_scierc_seed456                        Qwen3-8B-SciERC-merged-v2      SciERC       8     1.0   456      551     success    autodl-5090    
82	exp_019_supervised_verifier                        microsoft/deberta-v3-large                  -     -     42       551     killed                    
83	exp_020_fewnerd_smoke                              Qwen3-8B*                      FewNERD      -     -                      success                   
84	exp_021_fewnerd_full                                                              FewNERD      -     -                      success                   
85	exp_021_fewnerd_n8_seed123                         Qwen3-8B                       FewNERD      8     1.0   123      37648   success    autodl-5090    
86	exp_021_fewnerd_n8_seed456                         Qwen3-8B                       FewNERD      8     1.0   456      37648   success    autodl-5090    
87	exp_022_seed789                                    Qwen3-8B (qwen3-8b-scierc-merged-v2) SciERC       8     1.0   789      551     success    autodl-5090    
88	exp_024_claim_audit                                N/A                                         -     -     0        0       success    local          
89	exp_025_n32                                        Qwen3-8B*                                   -     -                      success                   
90	exp_026_T05                                        Qwen3-8B*                      SciERC       8     0.5                    success    autodl-5090    
91	exp_026_T08                                        Qwen3-8B*                      SciERC       8     0.8                    success    autodl-5090    
92	exp_026_T12                                        Qwen3-8B*                      SciERC       8     1.2                    success    autodl-5090    
93	exp_026_t05                                        Qwen3-8B*                                   -     -                      success                   
94	exp_026_t05_scierc                                 qwen3-8b-scierc-merged-v2      SciERC       -     -     42       551     success    autodl-5090    
95	exp_026_t05_seed123                                Qwen3-8B                       SciERC       8     0.5   123      551     success    autodl-5090    
96	exp_026_t05_seed456                                Qwen3-8B                       SciERC       8     0.5   456      551     success    autodl-5090    
97	exp_026_t08                                        Qwen3-8B*                                   -     -                      success                   
98	exp_026_t08_scierc                                 qwen3-8b-scierc-merged-v2      SciERC       -     -     42       551     success    autodl-5090    
99	exp_026_t08_seed123                                Qwen3-8B                       SciERC       8     0.8   123      551     success    autodl-5090    
100	exp_026_t08_seed456                                Qwen3-8B                       SciERC       8     0.8   456      551     success    autodl-5090    
101	exp_026_t10_seed123                                Qwen3-8B                       SciERC       8     1.0   123      551     success    autodl-5090    
102	exp_026_t10_seed42                                 Qwen3-8B                       SciERC       8     1.0   42       551     success    autodl-5090    
103	exp_026_t10_seed456                                Qwen3-8B                       SciERC       8     1.0   456      551     success    autodl-5090    
104	exp_026_t12                                        qwen3-8b-scierc-merged-v2      SciERC       8     1.2   42       551     success    autodl-5090    
105	exp_026_t12_scierc                                 qwen3-8b-scierc-merged-v2      SciERC       -     -     42       551     success    autodl-5090    
106	exp_026_t12_seed123                                Qwen3-8B                       SciERC       8     1.2   123      551     success    autodl-5090    
107	exp_026_t12_seed456                                Qwen3-8B                       SciERC       8     1.2   456      551     success    autodl-5090    
108	exp_027_fewnerd_n16                                qwen3-8b-fewnerd-exp021-merged FewNERD      16    1.0   42       5000    success    autodl-5090    
109	exp_027_mlp_verifier                               sklearn LR/MLP/RF                           16    -     42,123,456 529     negative   a100           
110	exp_028_entity_token_lp                            qwen3-8b-scierc-merged-v2      SciERC       -     -     42       529     negative   autodl-5090    
111	exp_030_conll_t12                                                                 CoNLL-2003   -     -                      killed                    
112	exp_031_fewnerd_t12                                                               FewNERD      -     -                      killed                    
113	exp_14b_inference_conll                            Qwen2.5-14B-Instruct (base)    CoNLL-2003   8     1.0   42       3453    killed     autodl-5090-c  
114	exp_14b_inference_fewnerd                          Qwen2.5-14B-Instruct           FewNERD      -     -     42               success    autodl-5090-c  
115	exp_14b_inference_scierc                           Qwen3-4B*                      SciERC       -     -                      killed                    
116	exp_32b_inference_fewnerd                          qwen25-32b-fewnerd-merged      FewNERD      8     1.0   42       301184  success    autodl-5090    
117	exp_a3_ace05_re                                    Qwen2.5-7B-Instruct            ACE05        -     1.0   42       397     success    autodl-5090-c  
118	exp_adaptive_temperature                           Qwen3-8B                                    -     -     42       all datasets negative   autodl-5090    
119	exp_asb_adaptive_budget                                                           CoNLL-2003   -     -                      negative   autodl-5090    
120	exp_b1_scd                                         n/a                                         -     -     0        0       killed     none           
121	exp_b3_prompted_diversity                          qwen3-8b-fewnerd-exp021-merged FewNERD      -     -     42       3000    killed     autodl-5090-c  
122	exp_backup1_het_temp                                                                           -     -                      negative   autodl-5090    
123	exp_backup3_distill_verifier                       LR+RF+MLP ensemble (sklearn)   CoNLL-2003   -     -     42       41652 instances total (~551+3453+37648) negative   autodl-5090    
124	exp_ccs_selection                                  Qwen3-8B                                    -     -     42       all datasets negative   autodl-5090    
125	exp_conll_mf4_s123                                 qwen3-8b-conll2003-merged      CoNLL-2003   8     1.0   123      3453    killed     autodl-5090    
126	exp_conll_mf4_s456                                 qwen3-8b-conll2003-merged      CoNLL-2003   8     1.0   456      3453    killed     autodl-5090    
127	exp_conll_mf4_v2_s123                              qwen3-8b-conll2003-merged      CoNLL-2003   8     1.0   123      3453    success    autodl-5090-b  
128	exp_conll_mf4_v2_s42                               qwen3-8b-conll2003-merged      CoNLL-2003   8     1.0   42       3453    success    autodl-5090-c  
129	exp_conll_mf4_v2_s456                              qwen3-8b-conll2003-merged      CoNLL-2003   8     1.0   456      3453    success    autodl-5090-b  
130	exp_conll_n16_s123                                 Qwen3-8B*                      CoNLL-2003   16    1.0                    failed     autodl-5090    
131	exp_conll_n16_s123_v2                              qwen3-8b-conll2003-merged      CoNLL-2003   16    1.0   123      3453    success    autodl-5090-c  
132	exp_conll_n16_s42                                  qwen3-8b-conll2003-merged      CoNLL-2003   16    1.0   42       3453    success    autodl-5090-c  
133	exp_conll_n16_s456                                 Qwen3-8B*                      CoNLL-2003   16    1.0                    failed     autodl-5090    
134	exp_conll_n16_s456_v2                              qwen3-8b-conll2003-merged      CoNLL-2003   16    1.0   456      3453    success    autodl-5090-c  
135	exp_conll_t05_s123                                 qwen3-8b-conll2003-merged      CoNLL-2003   8     0.5   123      3453    success    autodl-5090-c  
136	exp_conll_t05_s42                                  qwen3-8b-conll2003-merged (Qwen3-8B-FT-CoNLL) CoNLL-2003   8     0.5   42       3453    success    autodl-5090-b  
137	exp_conll_t05_s456                                 qwen3-8b-conll2003-merged      CoNLL-2003   8     0.5   456      3453    success    autodl-5090-c  
138	exp_conll_t08_s123                                 qwen3-8b-conll2003-merged      CoNLL-2003   8     0.8   123      3453    success    autodl-5090-c  
139	exp_conll_t08_s456                                 qwen3-8b-conll2003-merged      CoNLL-2003   8     0.8   456      3453    success    autodl-5090-c  
140	exp_conll_t10_s42                                  qwen3-8b-conll2003-merged      CoNLL-2003   8     1.0   42       3453    success    autodl-5090-c  
141	exp_conll_t12_s123                                 qwen3-8b-conll2003-merged      CoNLL-2003   8     1.2   123      3453    success    autodl-5090-c  
142	exp_conll_t12_s456                                 qwen3-8b-conll2003-merged      CoNLL-2003   8     1.2   456      3453    success    autodl-5090-c  
143	exp_conll_t_ablation_t05                           qwen3-8b-conll2003-merged      CoNLL-2003   8     0.5   42       2756    success    autodl-5090-c  
144	exp_conll_t_ablation_t08                           qwen3-8b-conll2003-merged      CoNLL-2003   8     0.8   42       2756    success    autodl-5090-c  
145	exp_conll_t_ablation_t12                           qwen3-8b-conll2003-merged      CoNLL-2003   8     1.2   42       2756    success    autodl-5090-c  
146	exp_cross_model_consistency                        cross-model (Qwen + LLaMA)     FewNERD      -     -     42       76398   success    autodl-5090    
147	exp_diagnostic_calibration                         Qwen3-8B                                    -     -     42       all datasets negative   autodl-5090    
148	exp_docred_re_sc                                   Qwen2.5-7B-Instruct            DocRED       -     -     42       200     success    autodl-5090-c  
149	exp_e2_pretrained_conll                            Qwen2.5-7B-Instruct            CoNLL-2003   8     1.0   42       3453    success    autodl-5090    
150	exp_e2_pretrained_scierc                           Qwen2.5-7B-Instruct            SciERC       8     1.0   42       100     negative   autodl-5090-c  
151	exp_e_theta_adaptive                                                                           -     -                      negative                  
152	exp_entity_consensus                               Qwen3-8B                                    -     -     42       all datasets negative   autodl-5090    
153	exp_entity_construction                            analysis_cpu                                -     -     42       3       success    autodl-5090    
154	exp_entity_token_lp                                Qwen3-8B (finetuned)           CoNLL-2003   -     -     42       529 (SciERC NER) + 2756 (CoNLL NER) negative   autodl-5090    
155	exp_epoch_dgs_analysis                             Qwen3-8B                                    -     -     42       all datasets success    autodl-5090    
156	exp_esj_entity_self_judgment                       qwen25-7b-fewnerd-merged       FewNERD      -     -     42       37648   negative   autodl-5090-c  
157	exp_fewnerd_7b_n16_s42                             qwen25-7b-fewnerd-merged       FewNERD      16    1.0   42       37648   failed     autodl-5090-c  
158	exp_fewnerd_mf4_v2_s123                            qwen3-8b-fewnerd-exp021-merged FewNERD      8     1.0   123      37648   success    autodl-5090-b  
159	exp_fewnerd_mf4_v2_s42                             qwen3-8b-fewnerd-exp021-merged FewNERD      8     1.0   42       37648   negative   autodl-5090-b  
160	exp_fewnerd_mf4_v2_s456                            qwen3-8b-fewnerd-exp021-merged FewNERD      -     -     456      32565   killed     autodl-5090-b  
161	exp_fewnerd_mf4v2_s456                             qwen3-8b-fewnerd-exp021-merged FewNERD      8     1.0   456      32565   success    autodl-5090    
162	exp_fewnerd_n16_s123                               Qwen3-8B*                      FewNERD      -     -                      success                   
163	exp_fewnerd_n16_s42                                Qwen3-8B*                      FewNERD      -     -                      success                   
164	exp_fewnerd_n16_s456                               qwen3-8b-fewnerd-exp021-merged FewNERD      16    1.0   456      14770   failed     autodl-5090-c  
165	exp_fewnerd_s789_n8                                Qwen3-8B (ft_002_v2)           FewNERD      -     -     789      37648   success    autodl-5090    
166	exp_fewnerd_t05_s123                               qwen3-8b-fewnerd-exp021-merged (Qwen3-8B-FT) FewNERD      8     0.5   123      37648   success    autodl-5090-b  
167	exp_fewnerd_t05_s42                                qwen3-8b-fewnerd-exp021-merged (Qwen3-8B-FT) FewNERD      8     0.5   42       37648   success    autodl-5090-b  
168	exp_fewnerd_t05_s456                               qwen3-8b-fewnerd-exp021-merged FewNERD      8     0.5   456      37648   success    autodl-5090-b  
169	exp_fewnerd_t08_s123                               qwen3-8b-fewnerd-exp021-merged (Qwen3-8B-FT) FewNERD      8     0.8   123      37648   success    autodl-5090-b  
170	exp_fewnerd_t08_s42                                qwen3-8b-fewnerd-exp021-merged (Qwen3-8B-FT) FewNERD      8     0.8   42       37648   success    autodl-5090-b  
171	exp_fewnerd_t08_s456                               qwen3-8b-fewnerd-exp021-merged (Qwen3-8B-FT) FewNERD      8     0.8   456      37648   success    autodl-5090-b  
172	exp_fewnerd_t12_s123                               qwen3-8b-fewnerd-exp021-merged (Qwen3-8B-FT) FewNERD      8     1.2   123      37648   negative   autodl-5090-b  
173	exp_fewnerd_t12_s42                                qwen3-8b-fewnerd-exp021-merged (Qwen3-8B-FT) FewNERD      8     1.2   42       37648   negative   autodl-5090-b  
174	exp_fewnerd_t12_s456                               qwen3-8b-fewnerd-exp021-merged FewNERD      8     1.2   456      37648   success    autodl-5090-b  
175	exp_fewrel_re_sc                                   Qwen2.5-7B-Instruct            FewRel       -     1.0   42       256     negative   autodl-5090-c  
176	exp_freeform_ablation                              qwen3-8b-scierc-merged-v2      SciERC       8     1.0   42       551     negative   autodl-5090    
177	exp_freeform_conll_4seed                           checkpoints/qwen3-8b-conll2003-merged CoNLL-2003   8     1.0   42,123,456,789 3453    success    autodl-4x5090  
178	exp_freeform_seed123                               qwen3-8b-scierc-merged-v2      SciERC       8     1.0   123      551     success    autodl-5090    
179	exp_freeform_seed456                               qwen3-8b-scierc-merged-v2      SciERC       8     1.0   456      551     success    autodl-5090    
180	exp_freeform_seed789                                                                           8     1.0                    success    autodl-5090    
181	exp_freeform_seed789_v2                            qwen3-8b-scierc-merged-v2      SciERC       8     1.0   789      551     failed     autodl-5090    
182	exp_freeform_seed789_v3                                                                        -     -                      success                   
183	exp_hidden_state_probe                             Qwen3-8B-FT (per-dataset checkpoints) CoNLL-2003   -     -     42       1000    success    autodl-5090-c  
184	exp_hidden_state_probe_fulldata                    Qwen3-8B fine-tuned                         -     -     42,123,456 CoNLL 850inst/14777ent, FewNERD 1698inst/41096ent, SciERC 539inst/13188ent success    autodl-5090-b (fewnerd), autodl-5090-c (conll, scierc)
185	exp_llama3b_scierc_ablation                        LLaMA-3.2-3B-Instruct (LoRA r=32 SciERC fine-tuned) SciERC       8     1.0   42       551     success    autodl-5090    
186	exp_llama_fewnerd_inference                        LLaMA-3.1-8B-FewNERD-LoRA-merged FewNERD      -     -     42,123,456 37648   success    autodl-5090    
187	exp_llama_scierc_seed456                           LLaMA-3.1-8B-Instruct          SciERC       -     -     456      551     success    autodl-5090    
188	exp_lp_alignment_gating                            analysis_cpu                                -     -     42       3       success    autodl-5090    
189	exp_lp_scierc_t07                                  Qwen3-8B                       SciERC       8     0.7   42       500     success    autodl-5090    
190	exp_lp_t07_scierc                                  Qwen3-8B (LoRA fine-tuned on SciERC, ft_002_v2 merged) SciERC       8     0.7   42       551     killed     autodl-5090    
191	exp_lsc_latent_sc                                  qwen25-7b-fewnerd-merged       FewNERD      -     -     42       2000    negative   autodl-5090-c  
192	exp_mrsc_multi_round                               qwen25-7b-fewnerd-merged       FewNERD      -     -     42       37648   negative   autodl-5090-c  
193	exp_multi_model_correlation                        Qwen3-8B-FT + LLaMA-3.1-8B-Instruct              -     -     42       9004    success    autodl-5090    
194	exp_qwen25_72b_fewshot                             Qwen2.5-72B-Instruct-AWQ       CoNLL-2003   -     -     42       41652   negative   autodl-5090-b  
195	exp_qwen25_72b_zeroshot                            Qwen2.5-72B-Instruct-AWQ       CoNLL-2003   -     -     42       41630   negative   autodl-5090-b  
196	exp_qwen3_4b_conll_merge_inference_v2              Qwen3-4B (LoRA merged, ckpt-4200) CoNLL-2003   8     1.0   42       3453    killed     autodl-5090    
197	exp_qwen3_4b_conll_scs_inference                   Qwen3-4B*                      CoNLL-2003   8     1.0                    success    autodl-5090    
198	exp_qwen3_4b_conll_scs_inference_v2                Qwen3-4B (LoRA checkpoint-4200 merged) CoNLL-2003   8     1.0   42       3453    success    autodl-5090    
199	exp_qwen3_4b_scierc_merge_inference                Qwen3-4B*                      SciERC       -     -                      killed                    
200	exp_qwen3_4b_scierc_scs_inference                  qwen3-4b-scierc-merged (checkpoint-400) SciERC       8     1.0   42       551     success    autodl-5090    
201	exp_re_scierc_seed123                              Qwen3-8B (SciERC merged)       SciERC       8     1.0   123      500     negative   autodl-5090    
202	exp_re_scierc_seed456                              Qwen3-8B (SciERC merged)       SciERC       8     1.0   456      500     negative   autodl-5090    
203	exp_scierc_mf4_v2_s123                             qwen3-8b-scierc-merged-v2      SciERC       8     1.0   123      529     success    autodl-5090    
204	exp_scierc_mf4_v2_s42                              qwen3-8b-scierc-merged-v2      SciERC       8     1.0   42       529     success    autodl-5090    
205	exp_scierc_mf4_v2_s456                             qwen3-8b-scierc-merged-v2      SciERC       8     1.0   456      529     success    autodl-5090    
206	exp_scierc_n16_s123                                qwen3-8b-scierc-merged-v2      SciERC       16    1.0   123      551     success    autodl-5090-b  
207	exp_scierc_n16_s456                                qwen3-8b-scierc-merged-v2      SciERC       16    1.0   456      551     success    autodl-5090-b  
208	exp_scierc_probe                                   qwen3-8b-scierc-merged-v2      SciERC       8     0.8   42       551     success    autodl-5090-c  
209	exp_scierc_t05_s123                                qwen3-8b-scierc-merged-v2      SciERC       8     0.5   123      551     success    autodl-5090-b  
210	exp_scierc_t05_s456                                Qwen3-8B*                      SciERC       -     -                      success                   
211	exp_scierc_t08_s123                                qwen3-8b-scierc-merged-v2      SciERC       8     0.8   123      551     success    autodl-5090-c  
212	exp_scierc_t08_s456                                Qwen3-8B*                      SciERC       -     -                      success                   
213	exp_scierc_t12_s123                                qwen3-8b-scierc-merged-v2      SciERC       8     1.2   123      551     success    autodl-5090-b  
214	exp_scierc_t12_s456                                Qwen3-8B*                      SciERC       -     -                      success                   
215	exp_selective_prediction                           analysis_cpu                                -     -     42       3       success    autodl-5090    
216	exp_tacred_re_benchmark                            N/A                            TACRED       -     -     0        0       killed     N/A            
217	exp_tlow_fewnerd_inference                         qwen25-7b-fewnerd-merged       FewNERD      8     0.5   42       37648   success    autodl-5090-c  
218	exp_vc_lp_cascade_selection                        N/A                                         -     -     0        0       killed     N/A            
219	exp_vc_quartile_analysis                           analysis_only (Qwen3-8B data)  CoNLL-2003   -     -     42       3682    success    autodl-5090    
220	exp_verbalized_confidence                          qwen3-8b-scierc-merged-v2 + qwen3-8b-conll2003-merged CoNLL-2003   -     -     42       3285    negative   autodl-5090    
221	hidden_state_probe_conll_full                                                     CoNLL-2003   -     -                      killed                    
222	hidden_state_probe_conll_v2                                                       CoNLL-2003   -     -                      killed                    
223	mbr_pilot                                                                                      -     -                      killed                    
224	mvp_pilot_001                                      qwen3-8b-scierc-merged                      -     -     42       551     negative   autodl-5090    
225	mvp_pilot_002                                      Qwen3-8B-SciERC-LoRA (ft_001)  SciERC       8     1.0   42       551     failed     autodl-5090    
226	mvp_pilot_003                                      qwen3-8b-scierc-merged         SciERC       8     1.0   42       551     negative   autodl-5090    
227	mvp_pilot_004                                      Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final) SciERC       8     1.0   42       551     negative   autodl-5090    
228	mvp_pilot_005                                      Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final) SciERC       8     0.7   42       551     negative   autodl-5090    
229	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ed7e85f-b4cf-4d2b-be3f-481149f7608d",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "4ff587d0-c5b3-493f-a3af-f7db11f8dd2b",
  "sourceToolAssistantUUID": "1ed7e85f-b4cf-4d2b-be3f-481149f7608d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-21T11:21:02.004Z_

Now let me also extract specific experiments that have interesting additional fields.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ff587d0-c5b3-493f-a3af-f7db11f8dd2b",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFdDtbPDVJzzpt7TZegx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c380df97-d84f-4962-a54f-dbb23cd312df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB3MpAGQLnkzgGXDiky7fN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11676,
      "cache_read_input_tokens": 70776,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11676,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 48 · 2026-05-21T11:21:11.226Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LXuMVAedmzJDSVpipBb2Ys`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/all_exps.json') as f:\n    exps = json.load(f)\n\n# Special/additional detail experiments to highlight\nspecials = [\n    'exp_hidden_state_probe', 'exp_hidden_state_probe_fulldata',\n    'exp_019_supervised_verifier', 'exp_027_mlp_verifier',\n    'exp_qwen25_72b_fewshot', 'exp_qwen25_72b_zeroshot',\n    'exp_llama3b_scierc_ablation',\n    'exp_a3_ace05_re', 'exp_docred_re_sc', 'exp_fewrel_re_sc', 'exp_tacred_re_benchmark',\n    'exp_b3_prompted_diversity', 'exp_mrsc_multi_round', 'exp_lsc_latent_sc',\n    'exp_esj_entity_self_judgment',\n    'exp_32b_inference_fewnerd', 'exp_14b_inference_fewnerd',\n    'exp_freeform_conll_4seed',\n    'exp_cross_model_consistency', 'exp_multi_model_correlation',\n]\n\nprint(\"=\" * 100)\nprint(\"SECTION D: NOTABLE SPECIAL EXPERIMENTS - DETAILED SPECS\")\nprint(\"=\" * 100)\n\nfor eid in sorted(specials):\n    e = exps.get(eid, {})\n    if not e:\n        continue\n    spec = e.get('spec', {})\n    metrics = e.get('metrics', {})\n    \n    print(f\"\\n{'─' * 80}\")\n    print(f\"ID: {eid}\")\n    print(f\"Conclusion: {e.get('conclusion')}\")\n    hyp = e.get('hypothesis') or spec.get('hypothesis') or ''\n    if hyp: print(f\"Hypothesis: {hyp[:300]}\")\n    \n    # Full spec dump\n    print(\"Full spec:\")\n    for k, v in sorted(spec.items()):\n        vstr = str(v)\n        if len(vstr) > 300: vstr = vstr[:300] + '...'\n        print(f\"  {k}: {vstr}\")\n    \n    if metrics:\n        mstr = json.dumps(metrics, ensure_ascii=False)\n        if len(mstr) > 500: mstr = mstr[:500] + '...'\n        print(f\"Metrics: {mstr}\")\n\nPYEOF\n",
  "description": "Extract detailed specs from notable special experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c380df97-d84f-4962-a54f-dbb23cd312df",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFdDtbPDVJzzpt7TZegx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74c9a956-3624-4a28-8e60-6d4a71a82aef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NB3MpAGQLnkzgGXDiky7fN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11676,
      "cache_read_input_tokens": 70776,
      "output_tokens": 736,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11676
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 736,
          "cache_read_input_tokens": 70776,
          "cache_creation_input_tokens": 11676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11676,
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

_source line 49 · 2026-05-21T11:21:11.511Z_

<details><summary>↩ Tool result · `toolu_01LXuMVAedmzJDSVpipBb2Ys`</summary>

```text
====================================================================================================
SECTION D: NOTABLE SPECIAL EXPERIMENTS - DETAILED SPECS
====================================================================================================

────────────────────────────────────────────────────────────────────────────────
ID: exp_019_supervised_verifier
Conclusion: killed
Hypothesis: Supervised verifier (DeBERTa-v3-large) can close the correlation-selection gap, proving the gap is closable with supervision
Full spec:
  data_count: 551
  data_path: output/exp_012_rerun_1024/samples.jsonl
  hypothesis: Supervised verifier (DeBERTa-v3-large) can close the correlation-selection gap, proving the gap is closable with supervision
  model_name: microsoft/deberta-v3-large
  plan_id: exp-019
  seed: 42

────────────────────────────────────────────────────────────────────────────────
ID: exp_027_mlp_verifier
Conclusion: negative
Hypothesis: MLP/RF等非线性模型能否通过组合5个QE信号(LP,SJ,FK,EM,VC)超越LR，或通过cross-signal interactions提取额外信息，从而缩小selection gap
Full spec:
  checkpoint_path: N/A
  command: python train_mlp_verifier.py --n_samples 16 --cv_folds 5 --seeds 42,123,456
  data_count: 529
  data_path: output/exp_001_n16_seed*/samples.jsonl
  log_path: output/exp_027_mlp_verifier/
  model_name: sklearn LR/MLP/RF
  seed: 42,123,456
  server: a100
Metrics: {"lr_auroc": 0.6522, "mlp_auroc": 0.6381, "rf_auroc": 0.5868, "mlp_15feat_auroc": 0.6341, "lr_sel_f1": 0.6406, "mlp_sel_f1": 0.6278, "greedy_f1": 0.6441, "oracle_f1": 0.8231, "best_single_signal_auroc": 0.6476, "feature_bottleneck_confirmed": true}

────────────────────────────────────────────────────────────────────────────────
ID: exp_14b_inference_fewnerd
Conclusion: success
Hypothesis: 14B Qwen2.5 inference on FewNERD (N∈{1,2,4,8}): primary dataset should show oracle scaling law F1(N)=a-b*N^(-c) consistent at 14B scale, filling the scaling curve between 7B and 32B. N=16 cut per Director decision.
Full spec:
  checkpoint_path: N/A
  data_path: /root/autodl-tmp/struct_self_consist_ie/data/fewnerd/
  gpu: cuda:0
  log_path: N/A
  model_name: Qwen2.5-14B-Instruct
  pid: 252310
  seed: 42
  server: autodl-5090-c
Metrics: {"fewnerd_n1": {"greedy_f1": 0.7985, "oracle_f1": 0.7541, "oracle_headroom": -0.044, "verdict": "FAIL"}, "fewnerd_n2": {"greedy_f1": 0.7985, "oracle_f1": 0.8086, "oracle_headroom": 0.01, "soft_jaccard_rho_full": 0.205, "rho_advantage": -0.006, "structural_beats_surface": false, "verdict": "FAIL"}, "fewnerd_n4": {"greedy_f1": 0.7984, "oracle_f1": 0.8544, "oracle_headroom": 0.056, "soft_jaccard_rho_full": 0.314, "rho_advantage": 0.042, "structural_beats_surface": true, "verdict": "MARGINAL"}, "few...

────────────────────────────────────────────────────────────────────────────────
ID: exp_32b_inference_fewnerd
Conclusion: success
Hypothesis: 32B fine-tuned model (Qwen2.5-32B-Instruct QLoRA, best checkpoint-32000) FewNERD inference with N=8 SC sampling. Scaling from 8B→32B should improve per-sample quality and strengthen SC diagnostic correlation (Fleiss kappa / Soft-Jaccard vs F1). Comparison baseline: Qwen3-8B-FT FewNERD results.
Full spec:
  checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/exp_32b_fewnerd_n8_s42/
  command: python code/run_mvp_pilot.py --model_path checkpoints/qwen25-32b-fewnerd-merged --data_dir data/fewnerd --dataset fewnerd --n_samples 8 --temperature 1.0 --seed 42 --output_dir output/exp_32b_fewnerd_n8_s42 --tensor_parallel 4 --collect_logprobs
  data_count: 301184
  data_path: data/fewnerd
  log_path: /root/autodl-tmp/struct_self_consist_ie/logs/inference_32b_fewnerd_n8_s42.log
  model_name: qwen25-32b-fewnerd-merged
  seed: 42
  server: autodl-5090
Metrics: {"greedy_f1": 0.8, "oracle_f1": 0.879, "rho_SJ_full": 0.32, "rho_FK_full": 0.242, "rho_advantage": 0.078, "fleiss_kappa_mean": 0.533, "soft_jaccard_mean": 0.802, "oracle_headroom": 0.079, "verdict": "MARGINAL"}

────────────────────────────────────────────────────────────────────────────────
ID: exp_a3_ace05_re
Conclusion: success
Hypothesis: Cross-task universality: SC diagnostic cascade on ACE05 Relation Extraction. Closest extension to NER—same structured prediction paradigm, different output structure (entity pairs + relation types). Qwen2.5-7B-Instruct few-shot prompt. If correlation-selection gap exists for RE, the framework covers
Full spec:
  checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/re_sc/
  command: CUDA_VISIBLE_DEVICES=1 python3 experiments/re_sc/run_re_sc.py --model-path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --data data/re_test_instances.jsonl --output-dir output/re_sc --n-samples 8 --temperature 1.0
  data_count: 397
  data_path: /root/autodl-tmp/struct_self_consist_ie/data/re_test_instances.jsonl
  hypothesis: The SC diagnostic cascade (degeneracy, agreement, LP-quality gap) generalizes from NER to Relation Extraction, with failure modes F1-F4 exhibiting analogous distributions on RE because both are span-based structured prediction tasks sharing the same underlying model uncertainty structure.
  log_path: /root/autodl-tmp/struct_self_consist_ie/logs/re_sc.log
  method: SC diagnostic cascade on RE (few-shot, N=8, T=1.0, XGrammar constrained decoding)
  model_name: Qwen2.5-7B-Instruct
  parent: None
  seed: 42
  server: autodl-5090-c
Metrics: {"greedy_f1_mean": 0.0777, "construction_f1_mean": 0.0599, "majority_vote_f1_mean": 0.0491, "oracle_f1_mean": 0.1567, "greedy_micro_f1": 0.0688, "construction_micro_f1": 0.0602, "fleiss_kappa": -0.0021, "soft_jaccard": 0.2425, "degeneracy_rate": 0.0076, "n_instances": 397, "failure_modes": {"F1_degeneracy": "0.8%", "F2_low_agreement": "93.5%", "F3_high_agreement_low_quality": "4.5%", "none": "1.3%"}, "bootstrap_diff": -0.0178, "bootstrap_ci_95": [-0.0334, -0.0024], "bootstrap_p_value": 0.989}

────────────────────────────────────────────────────────────────────────────────
ID: exp_b3_prompted_diversity
Conclusion: killed
Hypothesis: Structurally different prompt templates (expert persona, descriptive types, recall-focused) generate more diverse N=8 samples than repeating a single template, improving entity construction F1 via broader coverage of the entity space.
Full spec:
  checkpoint_path: N/A
  command: CUDA_VISIBLE_DEVICES=3 python /root/autodl-tmp/struct_self_consist_ie/code/exp_b3_prompted_diversity.py --phase both --num_instances 3000 --seed 42
  data_count: 3000
  data_path: /root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json
  log_path: N/A
  model_name: qwen3-8b-fewnerd-exp021-merged
  seed: 42
  server: autodl-5090-c
Metrics: {"single_vc_weighted_f1": 0.7723, "multi_vc_weighted_f1": 0.7311, "delta_vc": -0.0412, "single_lp_weighted_f1": 0.7665, "multi_lp_weighted_f1": 0.7308, "delta_lp": -0.0356, "single_theta2n_f1": 0.7618, "multi_theta2n_f1": 0.7269, "delta_theta2n": -0.0349, "single_unique_entities": 5.29, "multi_unique_entities": 4.06, "within_template_jaccard": 0.474, "cross_template_jaccard": 0.67, "verdict": "Multi-template strictly worse. Templates converge to similar outputs; non-standard templates add noise,...

────────────────────────────────────────────────────────────────────────────────
ID: exp_cross_model_consistency
Conclusion: success
Hypothesis: Cross-model entity construction (mixing Qwen and LLaMA outputs) produces higher-quality entity spans than single-model construction, because inter-model agreement filters out model-specific hallucinations while preserving genuinely supported entities.
Full spec:
  checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency
  command: bash code/run_cross_model.sh
  data_count: 76398
  data_path: output/exp_026_t10_seed42/samples.jsonl + output/exp007_llama_inference/samples.jsonl + output/exp_021_inference/samples.jsonl + output/llama_fewnerd_s42/samples.jsonl
  log_path: /root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency
  model_name: cross-model (Qwen + LLaMA)
  seed: 42
  server: autodl-5090
Metrics: {"scierc": {"n_filtered": 529, "qwen_greedy_f1": 0.6453, "llama_greedy_f1": 0.646, "degeneracy": {"pure_qwen": 0.1323, "pure_llama": 0.1777, "mixed": 0.0964}, "construction_f1": {"pure_qwen_uniform": 0.6449, "pure_qwen_vc": 0.6413, "pure_llama_uniform": 0.6545, "pure_llama_vc": 0.649, "mixed_uniform": 0.6625, "mixed_vc": 0.6591}, "bootstrap": {"mixed_uni_vs_pure_qwen_uni": {"delta_pp": 1.77, "p": 0.0102, "ci": [0.27, 3.28]}, "mixed_vc_vs_pure_qwen_vc": {"delta_pp": 1.77, "p": 0.0093, "ci": [0.33...

────────────────────────────────────────────────────────────────────────────────
ID: exp_docred_re_sc
Conclusion: success
Hypothesis: SC diagnostic cascade (degeneracy, correlation-selection gap, F1-F4 failure modes) generalizes from NER to document-level RE on DocRED, with Qwen2.5-7B-Instruct showing similar failure patterns as seen in SciERC NER and SciERC RE.
Full spec:
  checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/docred_re_sc/
  command: CUDA_VISIBLE_DEVICES=3 python3 experiments/docred_re/run_docred_re_sc.py --model-path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --data data/docred_re_instances.jsonl --schema data/docred_schema.json --output-dir output/docred_re_sc
  data_count: 200
  data_path: data/docred_re_instances.jsonl
  log_path: /root/autodl-tmp/struct_self_consist_ie/output/docred_re_sc/run.log
  model_name: Qwen2.5-7B-Instruct
  seed: 42
  server: autodl-5090-c
Metrics: {"greedy_f1_mean": 0.0284, "construction_f1_mean": 0.0338, "majority_vote_f1_mean": 0.0263, "oracle_f1_mean": 0.0999, "greedy_micro_f1": 0.0297, "construction_micro_f1": 0.0323, "fleiss_kappa": -0.0253, "soft_jaccard": 0.2907, "degeneracy_rate": 0.035, "n_instances": 200, "failure_modes": {"F1_degeneracy": "3.5%", "F2_low_agreement": "94.5%", "F3_high_agreement_low_quality": "2.0%"}, "bootstrap_diff": 0.0053, "bootstrap_ci_95": [-0.004, 0.0149], "bootstrap_p_value": 0.1276, "nondegen_constructio...

────────────────────────────────────────────────────────────────────────────────
ID: exp_esj_entity_self_judgment
Conclusion: negative
Hypothesis: Entity-Level Self-Judgment: F4 diagnostic proves 4/5 signals are instance-level only, LP is per-sample but compressed. ESJ provides true per-sample-per-entity signal via yes/no verification prompts. ESJ-weighted entity construction should outperform majority vote by leveraging entity-level confidenc
Full spec:
  checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/exp_esj_entity_self_judgment/
  checkpoint_source: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-fewnerd-merged
  command: CUDA_VISIBLE_DEVICES=1 python run_esj.py --base_model_path checkpoints/qwen25-7b-fewnerd-merged --data_path output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl --output_dir output/exp_esj_entity_self_judgment --batch_size 8
  data_count: 37648
  data_path: /root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl
  estimated_runtime_hours: 2.5
  eval_data: /root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl
  gpu: cuda:1
  log_path: /root/autodl-tmp/struct_self_consist_ie/output/exp_esj_entity_self_judgment.log
  model_name: qwen25-7b-fewnerd-merged
  n_verification_prompts: 153649
  pid: 218678
  seed: 42
  server: autodl-5090-c

────────────────────────────────────────────────────────────────────────────────
ID: exp_fewrel_re_sc
Conclusion: negative
Hypothesis: SC consensus construction improves RE micro-F1 over greedy decoding on FewRel (16 relation types, Wikipedia domain), extending cross-task universality evidence beyond SciERC and DocRED
Full spec:
  checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/fewrel_re_sc/
  command: CUDA_VISIBLE_DEVICES=1 python3 -u experiments/fewrel_re_sc/run_fewrel_re_sc.py --model-path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --data data/fewrel_re_test_instances.jsonl --output-dir output/fewrel_re_sc --n-samples 8 --temperature 1.0
  data_count: 256
  data_path: /root/autodl-tmp/struct_self_consist_ie/data/fewrel_re_test_instances.jsonl
  gpu: cuda:1
  log_path: /root/autodl-tmp/struct_self_consist_ie/output/fewrel_re_sc/run.log
  model_name: Qwen2.5-7B-Instruct
  pid: 236752
  seed: 42
  server: autodl-5090-c
Metrics: {"greedy_micro_f1": 0.0751, "construction_micro_f1": 0.0881, "majority_vote_f1_mean": 0.0591, "oracle_f1_mean": 0.1768, "fleiss_kappa_mean": 0.1506, "soft_jaccard_mean": 0.3918, "degeneracy_rate": 0.0586, "bootstrap_p_value": 0.7572, "failure_modes": {"F2_low_agreement": "75.8%", "F3_high_agreement_low_quality": "15.2%", "F1_degeneracy": "5.9%", "none": "2.3%", "F4_lp_quality_gap": "0.8%"}}

────────────────────────────────────────────────────────────────────────────────
ID: exp_freeform_conll_4seed
Conclusion: success
Hypothesis: Free-form CoNLL NER 4-seed ablation: verify LP compression is cross-dataset intrinsic (not SciERC-specific). 4 seeds × N=8, T=1.0 on CoNLL, compare LP range distribution with constrained decoding.
Full spec:
  command: python run_freeform_conll.py --seed {42,123,456,789} --gpu {0,1,2,3} --n_samples 8 --temperature 1.0
  data_count: 3453
  data_path: data/conll2003/test.jsonl
  model_name: checkpoints/qwen3-8b-conll2003-merged
  seed: 42,123,456,789
  server: autodl-4x5090
Metrics: {"greedy_f1": "0.9035±0.0004", "oracle_f1": "0.9460±0.0023", "lp_range_median": "0.0581±0.0072", "rho_sj": "0.4606±0.0188", "rho_fk": "0.4372±0.0209", "rho_em": "0.4714±0.0168", "rho_vc": "0.4606±0.0138", "rho_lp": "0.3262±0.0120", "sel_f1_sj": "0.8994±0.0014", "sel_f1_vc": "0.9006±0.0026", "sel_f1_lp": "0.8958±0.0009", "seeds": [42, 123, 456, 789], "n_samples": 8, "temperature": 1, "instances": 2756, "gold_empty_filtered": 697}

────────────────────────────────────────────────────────────────────────────────
ID: exp_hidden_state_probe
Conclusion: success
Hypothesis: Entity quality information (in_gold vs not) is encoded in the fine-tuned model's last-layer hidden states at entity token positions. If probe AUROC ≈ MV AUROC (0.87), the signal exists in representation but ESJ prompt-based reading (AUROC=0.51) fails to access it — a prompt interface failure. If pro
Full spec:
  checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/entity_probe_auroc/
  command: python code/hidden_state_probe.py --dataset {fewnerd,conll} --max_instances 500
  data_count: 1000
  data_path: output/{exp_tlow_fewnerd_t05_s42,exp_conll_t08_seed42}/samples.jsonl
  gpu: cuda:2 (fewnerd), cuda:3 (conll)
  log_path: /root/autodl-tmp/struct_self_consist_ie/logs/probe_extract_{fewnerd,conll}.log
  model_name: Qwen3-8B-FT (per-dataset checkpoints)
  pid: 261583
  seed: 42
  server: autodl-5090-c
Metrics: {"entity_level_stratifiedkfold_auroc": {"conll": 0.9796, "fewnerd": 0.9872, "scierc": 0.9766}, "groupkfold_auroc_corrected": {"conll": 0.8849, "fewnerd": 0.6513, "scierc": 0.6344}, "groupkfold_delta": {"conll": -0.0947, "fewnerd": -0.3359, "scierc": -0.3422}, "groupkfold_probe_above_mv": {"conll": true, "fewnerd": false, "scierc": false}, "baselines": {"mv_agreement_auroc": 0.87, "esj_prompt_auroc": 0.51}, "note": "GroupKFold fixes instance-level leakage. Only conll retains probe > MV after corr...

────────────────────────────────────────────────────────────────────────────────
ID: exp_hidden_state_probe_fulldata
Conclusion: success
Hypothesis: Hidden states of fine-tuned Qwen3-8B encode entity quality information that a linear probe can detect with AUROC significantly above chance, even under GroupKFold (no instance leakage). CoNLL probe should exceed MV baseline (0.87).
Full spec:
  command: extract_fulldata_hidden_states.py + groupkfold_probe_fulldata.py
  data_count: CoNLL 850inst/14777ent, FewNERD 1698inst/41096ent, SciERC 539inst/13188ent
  data_path: output/entity_probe_fulldata/
  model_name: Qwen3-8B fine-tuned
  seed: 42,123,456
  server: autodl-5090-b (fewnerd), autodl-5090-c (conll, scierc)

────────────────────────────────────────────────────────────────────────────────
ID: exp_llama3b_scierc_ablation
Conclusion: success
Hypothesis: Cross-family scale ablation: LLaMA 3.2-3B on SciERC NER. Verify correlation-selection gap generalizes across model families AND scales. Compare with LLaMA 8B results.
Full spec:
  checkpoint_path: checkpoints/llama3.2-3b-scierc-merged
  command: CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.2-3b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir outp...
  data_count: 551
  data_path: data/scierc/processed_data
  log_path: output/review_round9_experiments/llama3b_scierc/inference.log
  model_name: LLaMA-3.2-3B-Instruct (LoRA r=32 SciERC fine-tuned)
  seed: 42
  server: autodl-5090
Metrics: {"ner_full": {"SJ_rho": 0.3754, "FK_rho": 0.2676, "LP_rho": 0.2662, "EM_rho": 0.3341, "VC_rho": 0.4602, "SJ_auroc": 0.7383, "FK_auroc": 0.6714, "LP_auroc": 0.633, "EM_auroc": 0.7763, "VC_auroc": 0.7429, "n": 529}, "ner_cond": {"SJ_rho": 0.3445, "FK_rho": 0.2125, "LP_rho": 0.2099, "EM_rho": 0.3952, "VC_rho": 0.3815, "SJ_auroc": 0.7292, "FK_auroc": 0.66, "LP_auroc": 0.6156, "EM_auroc": 0.7822, "VC_auroc": 0.7222, "n": 476}, "greedy_f1": 0.6267, "oracle_f1": 0.763, "oracle_headroom": 0.1363, "selec...

────────────────────────────────────────────────────────────────────────────────
ID: exp_lsc_latent_sc
Conclusion: negative
Hypothesis: Latent Self-Consistency: F4 diagnostic proves LP is compressed (median range 0.041 nats). Hidden states contain richer per-sample information than scalar LP. Entity-level mean-pooled hidden state representations enable latent aggregation (centroid selection, latent confidence scoring, clustering) th
Full spec:
  checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/exp_lsc_latent_sc
  checkpoint_source: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-fewnerd-merged
  command: CUDA_VISIBLE_DEVICES=2 python run_lsc.py --base_model_path qwen25-7b-fewnerd-merged --data_path fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl --max_instances 2000
  data_count: 2000
  data_path: /root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl
  eval_data: FewNERD test (gold-filtered, n=2000)
  log_path: /root/autodl-tmp/struct_self_consist_ie/output/exp_lsc_latent_sc.log
  model_name: qwen25-7b-fewnerd-merged
  seed: 42
  server: autodl-5090-c
Metrics: {"centroid_selection_f1": 0.7593, "lp_selection_f1": 0.7845, "latent_entity_conf_f1": 0.8385, "majority_vote_f1": 0.8366, "greedy_f1": 0.7793, "oracle_f1": 0.8668, "lp_vs_latent_rho": 0.518, "entity_match_rate": 0.9945, "n_instances": 2000, "runtime_s": 507}

────────────────────────────────────────────────────────────────────────────────
ID: exp_mrsc_multi_round
Conclusion: negative
Hypothesis: Multi-Round Iterative SC: N inverse scaling reveals disputed entities cause failures. Focused re-prompting on disputed entities (agreement < 0.6) with weighted aggregation (Round 2 weight=2) should reduce error rate on disputed entities without affecting non-disputed ones, closing part of the select
Full spec:
  checkpoint_path: /root/autodl-tmp/struct_self_consist_ie/output/exp_mrsc_multi_round
  command: CUDA_VISIBLE_DEVICES=3 python /root/autodl-tmp/struct_self_consist_ie/code/run_mrsc.py --base_model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-fewnerd-merged --data_path /root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl --output_dir /...
  data_count: 37648
  data_path: /root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl
  log_path: /root/autodl-tmp/struct_self_consist_ie/output/exp_mrsc_multi_round.log
  model_name: qwen25-7b-fewnerd-merged
  seed: 42
  server: autodl-5090-c

────────────────────────────────────────────────────────────────────────────────
ID: exp_multi_model_correlation
Conclusion: success
Hypothesis: Cross-family models (Qwen vs LLaMA) have lower per-instance error correlation than same-family models, explaining why cross-model ensemble improves F1 by +0.42pp
Full spec:
  checkpoint_path: N/A
  checkpoint_source: N/A
  command: python3 code/multi_model_error_correlation.py --output_dir output/multi_model_correlation/
  data_count: 9004
  data_path: output/*/samples.jsonl
  log_path: output/multi_model_correlation/error_correlation_report.json
  model_name: Qwen3-8B-FT + LLaMA-3.1-8B-Instruct
  seed: 42
  server: autodl-5090

────────────────────────────────────────────────────────────────────────────────
ID: exp_qwen25_72b_fewshot
Conclusion: negative
Hypothesis: Few-shot prompting improves base NER F1 and LP signal quality, enabling LP-weighted construction to outperform greedy selection via dual-gating (sufficient LP ρ + low degeneracy).
Full spec:
  account: root
  backend: tmux
  checkpoint_source: Qwen2.5-72B-Instruct-AWQ (base model, no fine-tuning)
  command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0,1,2,3 python code/fewshot_inference_72b.py --datasets scierc conll2003 fewnerd --output-dir output/72b_fewshot --seed 42"
  data_count: 41652
  data_path: data/{scierc,conll2003,fewnerd}
  eval_data: SciERC + CoNLL-2003 + FewNERD test sets
  gpu: ['cuda:0', 'cuda:1', 'cuda:2', 'cuda:3']
  gpu_hours: 33.93
  gpu_ids: ['cuda:0', 'cuda:1', 'cuda:2', 'cuda:3']
  log_path: ~/runs/struct_self_consist_ie/exp_qwen25_72b_fewshot.log
  model_name: Qwen2.5-72B-Instruct-AWQ
  pid: 131293
  seed: 42
  server: autodl-5090-b
  submitted_at: 2026-05-19T16:25:57.711Z
  submitted_via: submit_training_job
  wall_clock_seconds: 30541.3
Metrics: {"scierc": {"lp_rho": 0.06, "sj_rho": 0.293, "fk_rho": 0.301, "vc_rho": 0.258, "em_rho": 0.205, "degen_pct": 16.6, "greedy_f1": 0.461, "oracle_f1": 0.604, "construction_f1": 0.461, "construction_delta_pp": -0.08, "bootstrap_p": 0.544}, "conll": {"lp_rho": 0.106, "sj_rho": 0.442, "fk_rho": 0.451, "vc_rho": 0.426, "em_rho": 0.403, "degen_pct": 70, "greedy_f1": 0.745, "oracle_f1": 0.796, "construction_f1": 0.745, "construction_delta_pp": 0.03, "bootstrap_p": 0.417}, "fewnerd": {"lp_rho": 0.161, "sj...

────────────────────────────────────────────────────────────────────────────────
ID: exp_qwen25_72b_zeroshot
Conclusion: negative
Hypothesis: A larger zero-shot model (72B) will show higher greedy F1 and wider oracle-greedy gap than fine-tuned smaller models, because increased capacity enables more diverse valid extractions per stochastic sample, making self-consistency signals (SJ, FK, VC, EM) more informative for quality estimation.
Full spec:
  command: CUDA_VISIBLE_DEVICES=0,1,2,3 python code/zeroshot_inference_72b.py --datasets scierc conll2003 fewnerd --output-dir output/72b_zeroshot --seed 42
  data_count: 41630
  data_path: data/{scierc,conll2003,fewnerd}
  gpu_ids: ['cuda:0', 'cuda:1', 'cuda:2', 'cuda:3']
  model_name: Qwen2.5-72B-Instruct-AWQ
  pid: 59040
  seed: 42
  server: autodl-5090-b
Metrics: {"scierc": {"greedy_f1": 0.3993, "lp_rho": 0.081, "vc_rho": 0.277, "sj_rho": 0.217, "degen_rate": 0.21, "construction_lp_weighted_f1": 0.4146, "construction_lp_delta_pp": 1.53, "construction_uniform_f1": 0.3941, "construction_uniform_delta_pp": -0.52, "lp_selection_f1": 0.3984, "majority_vote_f1": 0.4132, "oracle_f1": 0.5489, "bootstrap_p": 0.0082, "bootstrap_ci_lower": 0.0025, "bootstrap_ci_upper": 0.0282, "cohens_d": 0.1027, "n_instances": 529, "non_degen_delta_pp": 1.65, "non_degen_p": 0.0069...

────────────────────────────────────────────────────────────────────────────────
ID: exp_tacred_re_benchmark
Conclusion: killed
Hypothesis: TACRED RE benchmark: replicate SciERC RE experiment flow on second RE dataset. Verify correlation-selection gap generalizes beyond SciERC. D104 highest priority — addresses R11 MF1 consensus weakness.
Full spec:
  checkpoint_path: N/A
  command: N/A - cancelled before execution
  data_count: 0
  data_path: N/A
  log_path: N/A
  model_name: N/A
  seed: 0
  server: N/A
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74c9a956-3624-4a28-8e60-6d4a71a82aef",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "25ff84ff-73d2-4e0a-8b32-098e8dbcfca2",
  "sourceToolAssistantUUID": "74c9a956-3624-4a28-8e60-6d4a71a82aef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-21T11:21:14.793Z_

Now I have all the data extracted. Let me compile the final comprehensive summary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25ff84ff-73d2-4e0a-8b32-098e8dbcfca2",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFdFAXs6Z46LkPLahDuM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6b9382f-0141-4c64-8992-6cd780de0ba9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZfa5JSVsqMbuytnB1Kh7y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10236,
      "cache_read_input_tokens": 82452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10236,
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

_source line 51 · 2026-05-21T11:21:34.831Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01G5ZZe7V2q5uBnGLKSgwkhk`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\nfrom collections import Counter, defaultdict\n\nwith open('/tmp/all_exps.json') as f:\n    exps = json.load(f)\n\n# Compute aggregate statistics\nconclusions = Counter()\ndatasets = Counter()\nmodels = Counter()\nn_values = Counter()\nt_values = Counter()\nseeds = Counter()\nservers = Counter()\n\nfor eid, e in exps.items():\n    spec = e.get('spec', {})\n    cmd = spec.get('command', '') or ''\n    conclusions[e.get('conclusion', 'unknown')] += 1\n    \n    # Dataset\n    dp = (str(spec.get('data_path', '') or '') + ' ' + cmd + ' ' + eid).lower()\n    if 'conll' in dp: datasets['CoNLL-2003'] += 1\n    elif 'scierc' in dp: datasets['SciERC'] += 1\n    elif 'fewnerd' in dp: datasets['FewNERD'] += 1\n    elif 'wnut' in dp: datasets['WNUT-17'] += 1\n    elif 'spider' in dp: datasets['Spider'] += 1\n    elif 'humaneval' in dp: datasets['HumanEval'] += 1\n    elif 'ace05' in dp: datasets['ACE05'] += 1\n    elif 'docred' in dp: datasets['DocRED'] += 1\n    elif 'fewrel' in dp: datasets['FewRel'] += 1\n    elif 'tacred' in dp: datasets['TACRED'] += 1\n    else: datasets['other/multi'] += 1\n    \n    # Model\n    model = (spec.get('model_name', '') or spec.get('model', '') or '').lower()\n    if 'qwen3-8b' in model or 'qwen3-8b' in cmd.lower(): models['Qwen3-8B'] += 1\n    elif 'qwen3-4b' in model or 'qwen3-4b' in cmd.lower() or '4b' in eid.lower(): models['Qwen3-4B'] += 1\n    elif 'qwen2.5-7b' in model or 'qwen25-7b' in model: models['Qwen2.5-7B'] += 1\n    elif 'qwen2.5-14b' in model or 'qwen25-14b' in model: models['Qwen2.5-14B'] += 1\n    elif 'qwen2.5-32b' in model or 'qwen25-32b' in model: models['Qwen2.5-32B'] += 1\n    elif 'qwen2.5-72b' in model or 'qwen25-72b' in model: models['Qwen2.5-72B-AWQ'] += 1\n    elif 'llama' in model or 'llama' in cmd.lower(): models['LLaMA-3.x'] += 1\n    elif 'gpt-5.5' in model or 'gpt-5.5' in cmd.lower(): models['GPT-5.5'] += 1\n    elif 'claude' in model: models['Claude'] += 1\n    elif 'gemini' in model: models['Gemini-2.5-Pro'] += 1\n    elif 'deepseek' in model: models['DeepSeek-Chat'] += 1\n    elif 'deberta' in model: models['DeBERTa-v3'] += 1\n    elif 'sklearn' in model or 'analysis' in model or 'n/a' in model: models['analysis/sklearn'] += 1\n    else: models['unspecified'] += 1\n    \n    # N\n    n = spec.get('n_samples')\n    if n is None:\n        m = re.search(r'--n_samples\\s+(\\d+)', cmd)\n        if m: n = int(m.group(1))\n        elif '--num_samples' in cmd:\n            m = re.search(r'--num_samples\\s+(\\d+)', cmd)\n            if m: n = int(m.group(1))\n    if n: n_values[n] += 1\n    \n    # T\n    t = spec.get('temperature')\n    if t is None:\n        m = re.search(r'--temperature\\s+([\\d.]+)', cmd)\n        if m: t = float(m.group(1))\n    if t is not None: t_values[t] += 1\n    \n    # Seed\n    seed = spec.get('seed', '')\n    if seed and str(seed) not in ('', 'N/S', '0'):\n        seeds[str(seed)] += 1\n    \n    # Server\n    server = spec.get('server', '')\n    if server: servers[server] += 1\n\nprint(\"=\" * 100)\nprint(\"AGGREGATE STATISTICS ACROSS ALL 256 EXPERIMENTS\")\nprint(\"=\" * 100)\n\nprint(\"\\nConclusion distribution:\")\nfor k, v in conclusions.most_common():\n    print(f\"  {k}: {v}\")\n\nprint(\"\\nDataset distribution:\")\nfor k, v in datasets.most_common():\n    print(f\"  {k}: {v}\")\n\nprint(\"\\nModel distribution:\")\nfor k, v in models.most_common():\n    print(f\"  {k}: {v}\")\n\nprint(\"\\nN (sample count) distribution:\")\nfor k, v in sorted(n_values.items()):\n    print(f\"  N={k}: {v} experiments\")\n\nprint(\"\\nTemperature distribution:\")\nfor k, v in sorted(t_values.items()):\n    print(f\"  T={k}: {v} experiments\")\n\nprint(\"\\nSeed distribution:\")\nfor k, v in seeds.most_common(10):\n    print(f\"  seed={k}: {v} experiments\")\n\nprint(\"\\nServer distribution:\")\nfor k, v in servers.most_common():\n    print(f\"  {k}: {v}\")\n\nPYEOF\n",
  "description": "Compute aggregate statistics across all 256 experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6b9382f-0141-4c64-8992-6cd780de0ba9",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFdFAXs6Z46LkPLahDuM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ac7f718-e94b-4c9d-b53e-09246b94d15b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZfa5JSVsqMbuytnB1Kh7y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10236,
      "cache_read_input_tokens": 82452,
      "output_tokens": 1600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10236
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1600,
          "cache_read_input_tokens": 82452,
          "cache_creation_input_tokens": 10236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10236,
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

_source line 52 · 2026-05-21T11:21:34.925Z_

<details><summary>↩ Tool result · `toolu_01G5ZZe7V2q5uBnGLKSgwkhk`</summary>

```text
====================================================================================================
AGGREGATE STATISTICS ACROSS ALL 256 EXPERIMENTS
====================================================================================================

Conclusion distribution:
  success: 159
  negative: 51
  killed: 35
  failed: 11

Dataset distribution:
  SciERC: 91
  CoNLL-2003: 63
  FewNERD: 47
  other/multi: 45
  WNUT-17: 4
  Spider: 1
  FewRel: 1
  HumanEval: 1
  DocRED: 1
  ACE05: 1
  TACRED: 1

Model distribution:
  Qwen3-8B: 147
  LLaMA-3.x: 28
  unspecified: 22
  analysis/sklearn: 20
  Qwen3-4B: 15
  Qwen2.5-7B: 12
  GPT-5.5: 4
  Qwen2.5-32B: 2
  Qwen2.5-72B-AWQ: 2
  Gemini-2.5-Pro: 1
  DeepSeek-Chat: 1
  Claude: 1
  DeBERTa-v3: 1

N (sample count) distribution:
  N=8: 98 experiments
  N=16: 47 experiments

Temperature distribution:
  T=0.5: 12 experiments
  T=0.7: 4 experiments
  T=0.8: 11 experiments
  T=1.0: 109 experiments
  T=1.2: 11 experiments

Seed distribution:
  seed=42: 131 experiments
  seed=123: 35 experiments
  seed=456: 34 experiments
  seed=42,123,456: 3 experiments
  seed=789: 3 experiments
  seed=43: 1 experiments
  seed=3-seed bootstrap (1000 iterations): 1 experiments
  seed=42,123,456 (multi-seed): 1 experiments
  seed=42,123,456,789: 1 experiments

Server distribution:
  autodl-5090: 149
  autodl-5090-c: 36
  autodl-5090-b: 25
  gpu-5090-4x-2: 9
  local: 4
  bjb1-21071: 3
  N/A: 2
  none: 1
  autodl-5090-b (fewnerd), autodl-5090-c (conll, scierc): 1
  local (CPU+API): 1
  a100: 1
  autodl-4x5090: 1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ac7f718-e94b-4c9d-b53e-09246b94d15b",
  "isSidechain": true,
  "promptId": "065f0eb8-8652-409c-a364-34570ab71b19",
  "agentId": "a67b4a5d19dcf0796",
  "type": "user",
  "uuid": "bea20925-5b17-4ce8-970a-4a246ce07dc5",
  "sourceToolAssistantUUID": "5ac7f718-e94b-4c9d-b53e-09246b94d15b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-21T11:23:09.733Z_

Here is the comprehensive structured summary of all 256 DONE experiments.

---

## AGGREGATE STATISTICS

**256 total experiments**, all status=DONE.

| Conclusion | Count |
|---|---|
| success | 159 |
| negative | 51 |
| killed | 35 |
| failed | 11 |

**Datasets**: SciERC (91), CoNLL-2003 (63), FewNERD (47), other/multi (45), WNUT-17 (4), Spider (1), HumanEval (1), DocRED (1), FewRel (1), ACE05 (1), TACRED (1)

**Models**: Qwen3-8B (147), LLaMA-3.x (28), unspecified (22), analysis/sklearn (20), Qwen3-4B (15), Qwen2.5-7B (12), GPT-5.5 (4), Qwen2.5-32B (2), Qwen2.5-72B-AWQ (2), Gemini-2.5-Pro (1), DeepSeek-Chat (1), Claude Sonnet 4 (1), DeBERTa-v3-large (1)

**N (samples)**: N=8 (98 experiments), N=16 (47 experiments). 111 experiments have N unspecified in spec (analysis-only, or uses parent data).

**Temperature**: T=1.0 (109), T=0.8 (11), T=0.5 (12), T=1.2 (11), T=0.7 (4). 109 experiments have T unspecified.

**Seeds**: seed=42 (131), seed=123 (35), seed=456 (34), seed=789 (3), seed=43 (1). Multi-seed: 42,123,456 (3 experiments), 42,123,456,789 (1 experiment).

**Servers**: autodl-5090 (149), autodl-5090-c (36), autodl-5090-b (25), gpu-5090-4x-2 (9), local (4), bjb1-21071 (3), a100 (1), autodl-4x5090 (1). All GPUs are NVIDIA RTX 5090 except the a100 server.

---

## CATEGORY 1: FINE-TUNING EXPERIMENTS (30 experiments)

### Successful Fine-tuning Runs with Complete Hyperparameters:

**ft_001** -- Qwen/Qwen3-8B on SciERC, LoRA r=16 alpha=32, 3 epochs, data=1861, seed=42, framework=LLaMA Factory 0.9.4, train_loss=0.1099, eval_loss=0.0771, runtime=0:17:49

**ft_002** -- Qwen/Qwen3-8B on SciERC, LoRA r=32 alpha=64, 5 epochs (target), data=1861, seed=42, relation direction hint. **Killed** at step 70/585 due to OOM (batch_size=4 too large for 32GB RTX 5090).

**ft_002_v2** -- Qwen/Qwen3-8B on SciERC, LoRA r=32 alpha=64, 5 epochs, batch=2 grad_accum=8, gradient_checkpointing=true, data=1861, seed=42, total_steps=585, train_loss=0.0806, eval_loss=0.089, runtime=28m41s

**exp_007_ner_multi_model** -- LLaMA-3.1-8B-Instruct on SciERC, LoRA (lora_rank=32, lora_alpha=64 from metrics), 5 epochs, data=1861, seed=42, train_loss=0.0767, eval_loss=0.1049, runtime=1494.5s, server=gpu-5090-4x-2

**exp_017_llama_conll_finetune** -- Meta-Llama-3.1-8B-Instruct on CoNLL-2003, data=14037, seed=42, checkpoint=llama3.1-8b-conll2003-lora-3ep

**exp_023_lora_rank8** -- Qwen/Qwen3-8B on SciERC, LoRA r=8 alpha=16, 5 epochs, batch=2 grad_accum=8, gradient_checkpointing=true, data=1861, seed=42, total_steps=585, train_loss=0.1018, eval_loss=0.0776, runtime=28m45s

**exp_028 / exp_028_fewnerd_5epoch** -- Qwen3-8B LoRA rank=32 on FewNERD, 5 epochs, data=131767, seed=42, 4-GPU (cuda:0,1,2,3), train_loss=0.0189, eval_loss=0.0311

**exp_029a** -- Qwen3-8B LoRA rank=32 on SciERC, 3-epoch ablation, data=1861, seed=42, cuda:0

**exp_029b** -- Qwen3-8B on SciERC, 10-epoch ablation, data=1861, seed=42, cuda:1

**exp_llama_fewnerd_lora** -- LLaMA-Few-NERD-LoRA on FewNERD, 3 epochs, seed=42, total_steps=24708, train_loss=0.0516, eval_loss=0.0323, runtime=15.35h, adapter_size=320MB

**exp_qwen25_14b_fewnerd** -- Qwen2.5-14B-Instruct on FewNERD, QLoRA, 5 epochs, data=131767, seed=42, total_steps=41180, train_loss=0.0348, eval_loss=0.0323, runtime=29.8h, 2-GPU CUDA_VISIBLE_DEVICES=0,1

**exp_qwen25_32b_fewnerd** -- Qwen2.5-32B-Instruct on FewNERD, QLoRA-4bit-nf4 (rank=32, alpha=64, target=all), 5 epochs, lr=2e-4, data=131767, seed=42, total_steps=41180, best_eval_loss=0.0334 at step 32000, runtime=38.5h, 4-GPU. Overfitting after epoch ~3.9.

**exp_qwen25_7b_fewnerd** -- Qwen2.5-7B-Instruct on FewNERD, QLoRA 4-bit nf4, rank=32, alpha=64, 5 epochs, lr=2e-4, effective_batch=32, data=131767, seed=42

**exp_qwen3_4b_conll_finetune** -- Qwen3-4B on CoNLL-2003, LoRA target_modules=q_proj/k_proj/v_proj/o_proj/gate_proj/up_proj/down_proj, trainable_params=66M/4.09B (1.62%), enable_thinking=false, 5 epochs, batch_size=16, data=14041, seed=42, total_steps=4390, final_loss=0.0086. Training stopped at step 3920/4390 (89.3%).

**exp_qwen3_4b_conll_finetune_resume** -- Qwen3-4B on CoNLL-2003, resumed from step 3800, lr=0.0002, batch=2 x 8 grad_accum, data=14042, seed=42, total_steps=4390, train_loss=0.001136, eval_loss=0.0225, runtime=1185.8s

**exp_qwen3_4b_scierc_finetune_v4** -- Qwen3-4B on SciERC, 5 epochs, data=551, seed=42, total_steps=585, best_eval_loss=0.0898 at checkpoint-400

**exp_wnut17_qwen25_7b** -- Qwen2.5-7B-Instruct on WNUT-17, QLoRA 4-bit (bnb nf4), rank=32, alpha=64, all targets, 5 epochs, data=3404, seed=42. Conclusion: negative.

**SCD experiments** (exp_b1_scd_*): Self-Consistency Distillation on FewNERD/CoNLL using Qwen3-8B-FT checkpoints with pseudo-labels from theta-2/N construction. exp_b1_scd_fewnerd_standard: 2 epochs, data=32565, steps=4706, train_loss=0.023, eval_loss=0.0329, runtime=7.14h.

### Fine-tuning Experiments with Missing/Incomplete Specs:

- **exp_002_merge_conll2003**: killed, was a model merge (export) operation, not actual training
- **exp_003_wnut17_v2**: LoRA details unspecified (just "Qwen3-8B" on WNUT-17, 1637 samples)
- **exp_qwen3_4b_scierc_finetune**: killed before training started
- **exp_qwen3_4b_scierc_finetune_v2**: failed (died at step 10)
- **exp_qwen3_4b_scierc_finetune_v3**: failed (OOM)

---

## CATEGORY 2: API-BASED MODEL EXPERIMENTS (7 experiments)

**exp_frontier_sc_gpt55_fewnerd_v2** -- model=gpt-5.5, API via http://47.94.22.126/v1, dataset=FewNERD test 200 instances, N=8, T=1.0, seed=42, max_workers=4. Results: greedy_f1=0.6382, mv_f1=0.6521, oracle_f1=0.7203, degeneracy_rate=0.5, rho_agreement=0.3551, rho_fk=0.3515, rho_sj=0.3461.

**exp_frontier_sc_claude_sonnet4** -- model=anthropic/claude-sonnet-4, API via http://47.94.22.126/v1, dataset=FewNERD test 200 instances, N=8, T=1.0, seed=42, max_tokens=4096, text+type matching (case-insensitive, no offset). Results: greedy_f1=0.6068, mv_f1=0.6226, oracle_f1=0.6544, degeneracy_rate=0.74, parse_failures=103, api_calls=1600, wall_clock=6118s.

**exp_frontier_sc_gemini25pro** -- model=google/gemini-2.5-pro, API via http://47.94.22.126/v1, dataset=FewNERD test 200 instances, N=8, T=1.0, seed=42, max_workers=4. Results: greedy_f1=0.63, mv_f1=0.645, oracle_f1=0.758, mv_gain=+1.5pp, parse_failures=191.

**exp_frontier_sc_deepseek** -- model=deepseek/deepseek-chat, API via http://47.94.22.126/v1, dataset=FewNERD test 200 instances, N=8, T=1.0, seed=42, max_workers=4. Results: greedy_f1=0.3992, mv_f1=0.4243, oracle_f1=0.714, degeneracy_rate=0.055, parse_failure_count=751.

**exp_spider_sc_pilot** -- model=openai/gpt-5.5 via http://47.94.22.126/v1, dataset=Spider (SQL), 200 target instances (196 completed), N=8, T=1.0, seed=42. Execution-result equivalence for agreement. Results: greedy_acc=0.7653, mv_acc=0.7704, oracle_acc=0.8061, degeneracy_rate=0.8724. **Failed at 125/200 due to API credit exhaustion**, then recovered to 196.

**exp_a2_humaneval_sc** -- model=openai/gpt-5.5, dataset=HumanEval (164 tasks), N=8, T=1.0, seed=42. **Failed**: API balance exhausted after 24/164 tasks completed. Had bugfix for IndentationError (extract_code strip->rstrip + auto-indent).

**exp_b_frontier_sc_fewnerd** -- model=openai/gpt-5.5 + anthropic/claude-opus-4.6 (via OpenRouter), dataset=FewNERD 200 instances, N=8, T=1.0, seed=42. **Failed**: entity_set() TypeError bug.

---

## CATEGORY 3: INFERENCE/EVALUATION EXPERIMENTS (219 experiments)

The full table of all 222 inference experiments (with model, dataset, N, T, seed, data count, conclusion, server) is in the output at `/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/a9ed86cb-a33f-4ec8-8078-d4b9402803ce/tool-results/be4t1fmcu.txt`.

### Common Inference Configurations:

**SciERC NER** (~91 experiments): Predominantly Qwen3-8B (merged checkpoints: qwen3-8b-scierc-merged-v2, ft_002_v2). Typical config: N=8 or 16, T=1.0 (also 0.5, 0.7, 0.8, 1.2 for temperature ablations), seeds=42/123/456/789, data=529-551 instances.

**CoNLL-2003 NER** (~63 experiments): Qwen3-8B (qwen3-8b-conll2003-merged). Typical: N=8 or 16, T=0.5/0.8/1.0/1.2, seeds=42/123/456, data=2756-3453 instances.

**FewNERD NER** (~47 experiments): Qwen3-8B (qwen3-8b-fewnerd-exp021-merged), Qwen2.5-7B/14B/32B-merged variants, LLaMA-3.1-8B. Typical: N=8 or 16, T=0.5/0.8/1.0/1.2, data=5000-37648 instances.

### Temperature Ablation Series (exp_026_*, exp_conll_t*_*, exp_fewnerd_t*_*, exp_scierc_t*_*):
- T=0.5: 12 experiments across SciERC/CoNLL/FewNERD
- T=0.8: 11 experiments across SciERC/CoNLL/FewNERD
- T=1.0: baseline (majority of experiments)
- T=1.2: 11 experiments across SciERC/CoNLL/FewNERD

### N Ablation:
- N=8: standard configuration (98 experiments)
- N=16: extended sampling (47 experiments)
- N=32: 1 experiment (exp_025_n32)
- exp_14b_inference_fewnerd tested N in {1, 2, 4, 8}

### Cross-Scale Experiments:
- **3B**: LLaMA-3.2-3B-Instruct (exp_llama3b_scierc_ablation), N=8 T=1.0 seed=42, SciERC 551 instances
- **4B**: Qwen3-4B (exp_qwen3_4b_*_scs_inference*), N=8 T=1.0 seed=42
- **7B**: Qwen2.5-7B-Instruct (exp_qwen25_7b_fewnerd, exp_e2_pretrained_*), N=8 T=1.0
- **8B**: Qwen3-8B and LLaMA-3.1-8B-Instruct (majority of experiments)
- **14B**: Qwen2.5-14B-Instruct (exp_14b_inference_*), N=8 T=1.0 seed=42
- **32B**: Qwen2.5-32B (exp_32b_inference_fewnerd), N=8 T=1.0 seed=42, tensor_parallel=4
- **72B**: Qwen2.5-72B-Instruct-AWQ (exp_qwen25_72b_fewshot, exp_qwen25_72b_zeroshot), 4-GPU, zero-shot and few-shot, seed=42

### Cross-Task Experiments:
- **ACE05 RE** (exp_a3_ace05_re): Qwen2.5-7B-Instruct, N=8, T=1.0, seed=42, 397 instances, few-shot + XGrammar constrained decoding
- **DocRED RE** (exp_docred_re_sc): Qwen2.5-7B-Instruct, N=8, T=1.0, seed=42, 200 instances
- **FewRel RE** (exp_fewrel_re_sc): Qwen2.5-7B-Instruct, N=8, T=1.0, seed=42, 256 instances
- **Spider SQL** (exp_spider_sc_pilot): GPT-5.5 API, N=8, T=1.0, seed=42, 196 instances
- **HumanEval Code** (exp_a2_humaneval_sc): GPT-5.5 API, N=8, T=1.0, seed=42, 164 tasks (failed)

### Special Experiment Types:
- **Free-form ablation** (no constrained decoding): exp_freeform_* -- SciERC/CoNLL, N=8 T=1.0, seeds=42/123/456/789
- **Hidden state probes**: exp_hidden_state_probe*, DeBERTa probes on Qwen3-8B hidden states, seeds=42/123/456
- **Supervised/MLP verifier**: exp_027_mlp_verifier, sklearn LR/MLP/RF, 5-fold CV, seeds=42/123/456
- **Cross-model consistency**: exp_cross_model_consistency, mixing Qwen+LLaMA outputs, 76398 total data points
- **Multi-round SC**: exp_mrsc_multi_round, Qwen2.5-7B on FewNERD 37648 instances
- **Entity Self-Judgment**: exp_esj_entity_self_judgment, 153649 verification prompts on FewNERD
- **Prompted diversity**: exp_b3_prompted_diversity, multi-template prompting, 3000 instances

### Experiments with Missing/Incomplete Specs:

41 experiments have no model specified in the spec. Most are either killed/failed early or are analysis-only experiments reusing data from parent experiments. Key missing-spec experiments:

- **dgs_pilot**: killed, no spec fields populated
- **mbr_pilot**: killed, no spec
- **exp_tacred_re_benchmark**: killed, cancelled before execution
- **hidden_state_probe_conll_full/v2**: killed, incomplete probing runs
- Several killed experiments (exp001_seed123, exp001_seed456, exp008_re_n16, etc.) were early iterations that were superseded

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bea20925-5b17-4ce8-970a-4a246ce07dc5",
  "isSidechain": true,
  "agentId": "a67b4a5d19dcf0796",
  "requestId": "req_011CbFdGtXzS4ZP1jkW1YWei",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be296bfa-0452-4cf1-a0ff-6f76af0b903e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a9ed86cb-a33f-4ec8-8078-d4b9402803ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A6UDw9PNshyRHRBwBZSb89",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2379,
      "cache_read_input_tokens": 92688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2379,
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
