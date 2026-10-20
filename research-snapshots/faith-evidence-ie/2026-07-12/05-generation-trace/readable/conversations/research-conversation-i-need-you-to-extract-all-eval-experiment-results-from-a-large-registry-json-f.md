# Research conversation: I need you to extract all eval experiment results from a large registry JSON file. The file is at: /home/ubuntu/.claude-

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a01ea92613c0e609d.jsonl`
- **Structured JSON:** [`62e5c3d03740f94751e1.json`](../../sessions/62/62e5c3d03740f94751e1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-19T12:40:11.300Z_

I need you to extract all eval experiment results from a large registry JSON file. The file is at:
/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt

The file schema is `{result: string}` where the `result` field is a JSON string that needs to be parsed again.

I need you to extract ALL experiments whose `experiment_id` contains "eval" (case-insensitive). For each, report:
1. experiment_id
2. status
3. conclusion (if any)
4. Any metrics (especially ign_f1)
5. Any relevant notes about protocol (D076, etc.)

Also extract these specific non-eval experiments if they exist:
- random_rsft_k1_eval or random_rsft_k1_baseline
- Any experiment with "grpo" in the name
- Any experiment with "no_evidence" in the name

Use jq or python to parse the file. Return the complete list — do not summarize or omit any entries. Format as a table or structured list.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b133d549-2594-4f9e-b048-83b487db8d11",
  "agentId": "a01ea92613c0e609d",
  "type": "user",
  "uuid": "d35ba56b-4129-4106-a89a-eb9934885059",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T12:40:11.304Z_

```json
{
  "parentUuid": "d35ba56b-4129-4106-a89a-eb9934885059",
  "isSidechain": true,
  "agentId": "a01ea92613c0e609d",
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
  "uuid": "cf81fee8-394b-4751-8260-7a31b01367e2",
  "timestamp": "2026-05-19T12:40:11.304Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-19T12:40:14.618Z_



Let me read the file first to understand its structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf81fee8-394b-4751-8260-7a31b01367e2",
  "isSidechain": true,
  "agentId": "a01ea92613c0e609d",
  "requestId": "req_011CbBweiukLqqSZQvHEMZPD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cdcd8f51-1c26-475c-b764-5186c34695e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GR7zdcJWiuSc6Hp9qRkBTd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16006,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16006,
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

_source line 4 · 2026-05-19T12:40:16.010Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LvJKAUdAR9ep5UMQCzoxQg`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdcd8f51-1c26-475c-b764-5186c34695e4",
  "isSidechain": true,
  "agentId": "a01ea92613c0e609d",
  "requestId": "req_011CbBweiukLqqSZQvHEMZPD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c06e773-8c9e-4d8f-a46a-429d4bcbb9bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GR7zdcJWiuSc6Hp9qRkBTd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16006,
      "cache_read_input_tokens": 0,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16006
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 177,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16006,
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

_source line 5 · 2026-05-19T12:40:16.190Z_

<details><summary>↩ Tool result · `toolu_01LvJKAUdAR9ep5UMQCzoxQg`</summary>

```text
150644 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c06e773-8c9e-4d8f-a46a-429d4bcbb9bc",
  "isSidechain": true,
  "promptId": "b133d549-2594-4f9e-b048-83b487db8d11",
  "agentId": "a01ea92613c0e609d",
  "type": "user",
  "uuid": "ba98902f-fe2a-42af-9e87-5f313ae69ca0",
  "sourceToolAssistantUUID": "2c06e773-8c9e-4d8f-a46a-429d4bcbb9bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T12:40:22.375Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HZ389KDMeaB1XtUytvNf19`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt', 'r') as f:\n    outer = json.load(f)\n\n# Parse the inner result string\nregistry = json.loads(outer['result'])\n\n# Show top-level keys\nprint('Top-level keys:', list(registry.keys())[:20])\nprint()\n\n# Check structure\nfor k in registry:\n    v = registry[k]\n    if isinstance(v, dict):\n        print(f'{k}: dict with keys {list(v.keys())[:10]}')\n    elif isinstance(v, list):\n        print(f'{k}: list with {len(v)} items')\n    else:\n        print(f'{k}: {type(v).__name__} = {str(v)[:100]}')\n\" 2>&1 | head -50",
  "description": "Parse outer JSON and inspect top-level structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba98902f-fe2a-42af-9e87-5f313ae69ca0",
  "isSidechain": true,
  "agentId": "a01ea92613c0e609d",
  "requestId": "req_011CbBwf5pqZ4wa3KGe3thAL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a77dd6be-c926-46bc-844a-1ff12796a74a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016NEtH9cvaGJMXgHkfzQcYk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 16006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1122,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 7 · 2026-05-19T12:40:22.485Z_

<details><summary>↩ Tool result · `toolu_01HZ389KDMeaB1XtUytvNf19`</summary>

```text
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
  "parentUuid": "a77dd6be-c926-46bc-844a-1ff12796a74a",
  "isSidechain": true,
  "promptId": "b133d549-2594-4f9e-b048-83b487db8d11",
  "agentId": "a01ea92613c0e609d",
  "type": "user",
  "uuid": "a75a23f3-5eb6-477d-ab47-d8f22259e371",
  "sourceToolAssistantUUID": "a77dd6be-c926-46bc-844a-1ff12796a74a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T12:40:28.834Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01W85eip2WTjgkZA2BR2YziN`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt', 'r') as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\nprint(f'Total experiments: {len(experiments)}')\nprint()\n\n# List all experiment_ids\nfor exp in experiments:\n    eid = exp.get('experiment_id', 'N/A')\n    status = exp.get('status', 'N/A')\n    print(f'  {eid}  [{status}]')\n\" 2>&1",
  "description": "List all experiment IDs and statuses"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a75a23f3-5eb6-477d-ab47-d8f22259e371",
  "isSidechain": true,
  "agentId": "a01ea92613c0e609d",
  "requestId": "req_011CbBwfZ1Tx1zkU6BGz51xF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28b586ad-ca27-4839-b214-acf02e2af7e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F34ffQaKsoSq3QwvtLcUNf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 435,
      "cache_read_input_tokens": 17128,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 435
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 17128,
          "cache_creation_input_tokens": 435,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 435,
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

_source line 9 · 2026-05-19T12:40:29.082Z_

<details><summary>↩ Tool result · reported error · `toolu_01W85eip2WTjgkZA2BR2YziN`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 15, in &lt;module>
    eid = exp.get('experiment_id', 'N/A')
          ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
Total experiments: 242
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28b586ad-ca27-4839-b214-acf02e2af7e5",
  "isSidechain": true,
  "promptId": "b133d549-2594-4f9e-b048-83b487db8d11",
  "agentId": "a01ea92613c0e609d",
  "type": "user",
  "uuid": "7526a8c5-34c7-4a2d-84cc-691c95500d9a",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 15, in &lt;module>\n    eid = exp.get('experiment_id', 'N/A')\n          ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'\nTotal experiments: 242",
  "sourceToolAssistantUUID": "28b586ad-ca27-4839-b214-acf02e2af7e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T12:40:37.721Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NqLRfwSEaNR5LK4NuuGnrk`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt', 'r') as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Check if experiments is a dict (keyed by experiment_id) or list\nprint(f'Type: {type(experiments)}')\nif isinstance(experiments, dict):\n    keys = list(experiments.keys())\n    print(f'Keys (first 10): {keys[:10]}')\n    # Check first value\n    first_key = keys[0]\n    first_val = experiments[first_key]\n    print(f'First value type: {type(first_val)}')\n    print(f'First value (truncated): {json.dumps(first_val, indent=2)[:500]}')\nelif isinstance(experiments, list):\n    print(f'First item type: {type(experiments[0])}')\n    print(f'First item: {experiments[0][:200] if isinstance(experiments[0], str) else json.dumps(experiments[0], indent=2)[:500]}')\n\" 2>&1",
  "description": "Inspect experiments data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7526a8c5-34c7-4a2d-84cc-691c95500d9a",
  "isSidechain": true,
  "agentId": "a01ea92613c0e609d",
  "requestId": "req_011CbBwg2wUtGyq9Jfz8bTQt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59e52933-74e3-49b3-b2f4-9564112636df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dp9TVdPpKD3VVnoshRhJrc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 17128,
      "output_tokens": 430,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 833
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 430,
          "cache_read_input_tokens": 17128,
          "cache_creation_input_tokens": 833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 833,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T12:40:37.845Z_

<details><summary>↩ Tool result · `toolu_01NqLRfwSEaNR5LK4NuuGnrk`</summary>

```text
Type: &lt;class 'dict'>
Keys (first 10): ['d112_rsft_s44_eval', 'plan019_1_7b_rsft_s44_r2_eval', 'd112_rsft_s44_train', 'plan017_14b_sft_eval', 'plan017_14b_sft_no_evidence_eval', 'plan019_1_7b_rsft_s43_r2_eval', 'plan017_14b_sft', 'plan019_1_7b_rsft_s44_r2', 'plan019_1_7b_rsft_s43_r2', 'plan019_1_7b_rsft_s44']
First value type: &lt;class 'dict'>
First value (truncated): {
  "status": "DONE",
  "created_at": "2026-05-19T07:34:55.266Z",
  "updated_at": "2026-05-19T12:02:10.888Z",
  "hypothesis": "D112 step 4: D076 eval for RSFT trained on SFT s44 base with CED k=1 scored data. \u9a8c\u8bc1 RSFT \u5728\u6700\u5f3a SFT seed (s44, ign_f1=0.4734) \u4e0a\u7684\u6cdb\u5316\u6548\u679c\u3002\u9884\u671f ign_f1 > 0.4734 (SFT s44 baseline)\u3002",
  "parent": "d112_rsft_s44_train",
  "conclusion": "failed",
  "metrics": {
    "ign_f1": 0.2181,
    "note": "INVALID: QLoRA
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59e52933-74e3-49b3-b2f4-9564112636df",
  "isSidechain": true,
  "promptId": "b133d549-2594-4f9e-b048-83b487db8d11",
  "agentId": "a01ea92613c0e609d",
  "type": "user",
  "uuid": "be0531e3-09e5-4355-90f2-e5dd9af1602e",
  "sourceToolAssistantUUID": "59e52933-74e3-49b3-b2f4-9564112636df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T12:40:53.082Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Nc83c363QCumzy8BpRq2KS`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt', 'r') as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Filter: eval in name (case-insensitive), or specific patterns\nresults = []\nfor eid, exp in experiments.items():\n    eid_lower = eid.lower()\n    match_eval = 'eval' in eid_lower\n    match_random_rsft = 'random_rsft' in eid_lower\n    match_grpo = 'grpo' in eid_lower\n    match_no_evidence = 'no_evidence' in eid_lower\n    \n    if match_eval or match_random_rsft or match_grpo or match_no_evidence:\n        category = []\n        if match_eval: category.append('eval')\n        if match_random_rsft: category.append('random_rsft')\n        if match_grpo: category.append('grpo')\n        if match_no_evidence: category.append('no_evidence')\n        \n        results.append({\n            'experiment_id': eid,\n            'category': ', '.join(category),\n            'status': exp.get('status', 'N/A'),\n            'conclusion': exp.get('conclusion', ''),\n            'metrics': exp.get('metrics', {}),\n            'hypothesis': exp.get('hypothesis', ''),\n            'parent': exp.get('parent', ''),\n            'created_at': exp.get('created_at', ''),\n            'updated_at': exp.get('updated_at', ''),\n        })\n\n# Sort by experiment_id\nresults.sort(key=lambda x: x['experiment_id'])\n\nprint(f\"Total matching experiments: {len(results)}\")\nprint(\"=\" * 140)\n\nfor r in results:\n    print(f\"\\n### {r['experiment_id']}\")\n    print(f\"  Category:   {r['category']}\")\n    print(f\"  Status:     {r['status']}\")\n    print(f\"  Conclusion: {r['conclusion'] or '(none)'}\")\n    print(f\"  Parent:     {r['parent'] or '(none)'}\")\n    \n    metrics = r['metrics']\n    if metrics:\n        ign_f1 = metrics.get('ign_f1', None)\n        if ign_f1 is not None:\n            print(f\"  ign_f1:     {ign_f1}\")\n        # Print all metric keys\n        for mk, mv in metrics.items():\n            if mk != 'ign_f1':\n                val_str = str(mv)\n                if len(val_str) > 200:\n                    val_str = val_str[:200] + '...'\n                print(f\"  {mk}: {val_str}\")\n    else:\n        print(f\"  Metrics:    (none)\")\n    \n    # Print hypothesis truncated\n    hyp = r['hypothesis']\n    if hyp:\n        if len(hyp) > 300:\n            hyp = hyp[:300] + '...'\n        print(f\"  Hypothesis: {hyp}\")\n    \n    print(f\"  Created:    {r['created_at']}\")\n    print(f\"  Updated:    {r['updated_at']}\")\n\nPYEOF\n",
  "description": "Extract all matching experiments with full details",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be0531e3-09e5-4355-90f2-e5dd9af1602e",
  "isSidechain": true,
  "agentId": "a01ea92613c0e609d",
  "requestId": "req_011CbBwghEqz1t2SYCZxjNJV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cccf988c-b9f7-43bd-9193-f422d4e3423c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mf7Chw274he5qXNGwfAeqc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 17961,
      "output_tokens": 1006,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 905
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1006,
          "cache_read_input_tokens": 17961,
          "cache_creation_input_tokens": 905,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 905,
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

_source line 13 · 2026-05-19T12:40:53.260Z_

<details><summary>↩ Tool result · `toolu_01Nc83c363QCumzy8BpRq2KS`</summary>

```text
&lt;persisted-output>
Output too large (71.2KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt

Preview (first 2KB):
Total matching experiments: 149
============================================================================================================================================

### d102_llama_rsft_k1_s43_eval
  Category:   eval
  Status:     DONE
  Conclusion: killed
  Parent:     rsft_llama_k1_s43_train
  Metrics:    (none)
  Hypothesis: LLaMA-8B RSFT k=1 seed43 eval: paired with s42 (rel_f1=0.5839) for seed robustness. If s43 gives similar results (±1.5pp), cross-architecture RSFT k=1 claim is robust. Expected rel_f1 ~0.58±0.015.
  Created:    2026-05-18T13:06:23.193Z
  Updated:    2026-05-18T13:59:53.656Z

### d111_4b_sft_s42_reeval
  Category:   eval
  Status:     DONE
  Conclusion: success
  Parent:     (none)
  ign_f1:     0.3974
  rel_f1: 0.4049
  evi_f1: 0.7986
  evi_f1_joint: 0.3147
  edcr: 0.6982
  Hypothesis: Re-evaluating 4B SFT s42 with D076 standardized protocol to establish fair 3-seed comparison with s43 and s44. Previous s42 evaluations gave inconsistent results (0.4106/0.4036/0.3974), so re-running with identical protocol resolves this.
  Created:    2026-05-18T22:06:04.423Z
  Updated:    2026-05-19T03:54:03.116Z

### d112_rsft_s44_eval
  Category:   eval
  Status:     DONE
  Conclusion: failed
  Parent:     d112_rsft_s44_train
  ign_f1:     0.2181
  note: INVALID: QLoRA confound — adapter trained on 4-bit quantized backbone evaluated in bf16
  Hypothesis: D112 step 4: D076 eval for RSFT trained on SFT s44 base with CED k=1 scored data. 验证 RSFT 在最强 SFT seed (s44, ign_f1=0.4734) 上的泛化效果。预期 ign_f1 > 0.4734 (SFT s44 baseline)。
  Created:    2026-05-19T07:34:55.266Z
  Updated:    2026-05-19T12:02:10.888Z

### eval_flat_nli_s44
  Category:   eval
  Status:     DONE
  Conclusion: success
  Parent:     plan_001_flat_nli_seed44
  ign_f1:     0.452126
  rel_f1: 0.461506
  evi_f1: 0.813123
  edcr: 0.645808
  evi_f1_joint: 0.359673
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cccf988c-b9f7-43bd-9193-f422d4e3423c",
  "isSidechain": true,
  "promptId": "b133d549-2594-4f9e-b048-83b487db8d11",
  "agentId": "a01ea92613c0e609d",
  "type": "user",
  "uuid": "fab48dd8-69a5-4a08-8a4f-43ff784ccfdc",
  "sourceToolAssistantUUID": "cccf988c-b9f7-43bd-9193-f422d4e3423c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T12:40:55.478Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VamRmZ4HokMNuKAF8TXFhS`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fab48dd8-69a5-4a08-8a4f-43ff784ccfdc",
  "isSidechain": true,
  "agentId": "a01ea92613c0e609d",
  "requestId": "req_011CbBwhpKmX53pS7GaKMkPG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d7426bf-0cc2-4f38-ae83-d3b7b8d21df1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpAkF8kFWN3HD1apdcwFRF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1903,
      "cache_read_input_tokens": 18866,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1903
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 18866,
          "cache_creation_input_tokens": 1903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1903,
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

_source line 15 · 2026-05-19T12:40:55.904Z_

<details><summary>↩ Tool result · reported error · `toolu_01VamRmZ4HokMNuKAF8TXFhS`</summary>

```text
File content (32736 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d7426bf-0cc2-4f38-ae83-d3b7b8d21df1",
  "isSidechain": true,
  "promptId": "b133d549-2594-4f9e-b048-83b487db8d11",
  "agentId": "a01ea92613c0e609d",
  "type": "user",
  "uuid": "bfc874b9-807b-41f2-9b32-33c820f2a896",
  "toolUseResult": "Error: File content (32736 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "1d7426bf-0cc2-4f38-ae83-d3b7b8d21df1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T12:40:58.850Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Fsh5sjyR4k75YZ7pciZyXz`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfc874b9-807b-41f2-9b32-33c820f2a896",
  "isSidechain": true,
  "agentId": "a01ea92613c0e609d",
  "requestId": "req_011CbBwi1eu9agc2gwrVKKhC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d87ad06-9906-4a91-b6c3-b16f7aeb8597",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Da2eYP8VCoTzkVGw7BhVXg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 192,
      "cache_read_input_tokens": 20769,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 192
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 20769,
          "cache_creation_input_tokens": 192,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 192,
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

_source line 17 · 2026-05-19T12:40:58.865Z_

<details><summary>↩ Tool result · `toolu_01Fsh5sjyR4k75YZ7pciZyXz`</summary>

```text
1	Total matching experiments: 149
2	============================================================================================================================================
3	
4	### d102_llama_rsft_k1_s43_eval
5	  Category:   eval
6	  Status:     DONE
7	  Conclusion: killed
8	  Parent:     rsft_llama_k1_s43_train
9	  Metrics:    (none)
10	  Hypothesis: LLaMA-8B RSFT k=1 seed43 eval: paired with s42 (rel_f1=0.5839) for seed robustness. If s43 gives similar results (±1.5pp), cross-architecture RSFT k=1 claim is robust. Expected rel_f1 ~0.58±0.015.
11	  Created:    2026-05-18T13:06:23.193Z
12	  Updated:    2026-05-18T13:59:53.656Z
13	
14	### d111_4b_sft_s42_reeval
15	  Category:   eval
16	  Status:     DONE
17	  Conclusion: success
18	  Parent:     (none)
19	  ign_f1:     0.3974
20	  rel_f1: 0.4049
21	  evi_f1: 0.7986
22	  evi_f1_joint: 0.3147
23	  edcr: 0.6982
24	  Hypothesis: Re-evaluating 4B SFT s42 with D076 standardized protocol to establish fair 3-seed comparison with s43 and s44. Previous s42 evaluations gave inconsistent results (0.4106/0.4036/0.3974), so re-running with identical protocol resolves this.
25	  Created:    2026-05-18T22:06:04.423Z
26	  Updated:    2026-05-19T03:54:03.116Z
27	
28	### d112_rsft_s44_eval
29	  Category:   eval
30	  Status:     DONE
31	  Conclusion: failed
32	  Parent:     d112_rsft_s44_train
33	  ign_f1:     0.2181
34	  note: INVALID: QLoRA confound — adapter trained on 4-bit quantized backbone evaluated in bf16
35	  Hypothesis: D112 step 4: D076 eval for RSFT trained on SFT s44 base with CED k=1 scored data. 验证 RSFT 在最强 SFT seed (s44, ign_f1=0.4734) 上的泛化效果。预期 ign_f1 > 0.4734 (SFT s44 baseline)。
36	  Created:    2026-05-19T07:34:55.266Z
37	  Updated:    2026-05-19T12:02:10.888Z
38	
39	### eval_flat_nli_s44
40	  Category:   eval
41	  Status:     DONE
42	  Conclusion: success
43	  Parent:     plan_001_flat_nli_seed44
44	  ign_f1:     0.452126
45	  rel_f1: 0.461506
46	  evi_f1: 0.813123
47	  edcr: 0.645808
48	  evi_f1_joint: 0.359673
49	  Hypothesis: Full dev eval of flat-NLI RSFT seed=44 with --sft_adapter + --no-quantize. C3 统计显著性数据点 (s42=0.4539, s43 pending, s44 本次, s45 pending)。
50	  Created:    2026-05-15T23:14:05.010Z
51	  Updated:    2026-05-16T03:49:35.610Z
52	
53	### eval_flat_nli_seed44
54	  Category:   eval
55	  Status:     DONE
56	  Conclusion: killed
57	  Parent:     plan_001_flat_nli_seed44
58	  Metrics:    (none)
59	  Hypothesis: Full dev eval of flat-NLI RSFT seed=44 with --sft_adapter + --no-quantize. C3 seed-level comparison.
60	  Created:    2026-05-15T23:12:38.199Z
61	  Updated:    2026-05-15T23:48:28.074Z
62	
63	### eval_flat_nli_seed45
64	  Category:   eval
65	  Status:     DONE
66	  Conclusion: success
67	  Parent:     plan_001_flat_nli_seed45
68	  ign_f1:     0.446181
69	  rel_f1: 0.455052
70	  evi_f1: 0.815399
71	  edcr: 0.652133
72	  evi_f1_joint: 0.355612
73	  Hypothesis: Full dev eval of flat-NLI RSFT seed=45 checkpoint WITH --sft_adapter。seed45 中间 eval rel_f1=0.4876（待全量确认）。对比 CED RSFT mean (0.4596)。三 seed 全量 eval 出齐后汇报 flat-NLI vs CED RSFT 完整 seed-level 对比。
74	  Created:    2026-05-15T23:12:39.186Z
75	  Updated:    2026-05-16T03:49:36.608Z
76	
77	### eval_grpo_g8_bf16
78	  Category:   eval, grpo
79	  Status:     DONE
80	  Conclusion: success
81	  Parent:     (none)
82	  ckpt80_rel_f1: 0.4456
83	  ckpt80_ign_f1: 0.4456
84	  ckpt80_evi_f1: 0.8034
85	  ckpt80_edcr: 0.6409
86	  ckpt80_format_ok: 984/985
87	  ckpt80_truncated: 50
88	  ckpt90_rel_f1: 0.4523
89	  ckpt90_ign_f1: 0.4523
90	  ckpt90_evi_f1: 0.8052
91	  ckpt90_edcr: 0.6414
92	  ckpt90_format_ok: 983/985
93	  ckpt90_truncated: 61
94	  ckpt100_rel_f1: 0.4549
95	  ckpt100_ign_f1: 0.4549
96	  ckpt100_evi_f1: 0.8086
97	  ckpt100_edcr: 0.6318
98	  ckpt100_format_ok: 985/985
99	  ckpt100_truncated: 61
100	  best_checkpoint: ckpt-100
101	  Hypothesis: Eval GRPO G=8 bf16 checkpoints 80/90/100 on full dev set (985 docs). 验证 catastrophic forgetting 是否在 bf16 LoRA 下复现。rel_f1>0.30 → forgetting 不复现 (QLoRA-specific); rel_f1<0.05 → 复现 (C2 加强)。对比: SFT rel_f1=0.4057, QLoRA GRPO rel_f1=0.2167 (catastrophic).
102	  Created:    2026-05-15T14:41:07.474Z
103	  Updated:    2026-05-15T17:57:46.573Z
104	
105	### eval_plan_001_flat_nli
106	  Category:   eval
107	  Status:     DONE
108	  Conclusion: success
109	  Parent:     plan_001_rsft_flat_nli
110	  ign_f1:     0.4539
111	  rel_f1: 0.4539
112	  evi_f1: 0.8043
113	  edcr: 0.6431
114	  precision: 0.4671
115	  recall: 0.4414
116	  evi_precision: 0.8143
117	  evi_recall: 0.7945
118	  format_ok_rate: 1
119	  n_truncated: 199
120	  n_documents: 985
121	  n_predictions: 15294
122	  inference_time_seconds: 3631
123	  Hypothesis: Dev eval of flat-NLI RSFT (plan_001). 对比 CED RSFT (3-seed mean rel_f1=0.4596). flat-NLI ≈ CED → CED contrastive margin 无增益; CED >> flat-NLI → margin 关键。
124	  Created:    2026-05-15T16:57:09.693Z
125	  Updated:    2026-05-15T18:04:13.598Z
126	
127	### eval_plan_001_flat_nli_s43
128	  Category:   eval
129	  Status:     DONE
130	  Conclusion: failed
131	  Parent:     (none)
132	  ign_f1:     0.0022
133	  rel_f1: 0.0022
134	  evi_f1: 0.8533
135	  edcr: 0.9982
136	  num_preds: 17285
137	  format_ok: 981/985
138	  truncated: 251/985
139	  tp: 32
140	  note: INVALID — missing --sft_adapter, same bug as DPO 1ep eval
141	  Created:    2026-05-15T20:29:54.486Z
142	  Updated:    2026-05-15T21:35:00.000Z
143	
144	### eval_plan_008_rsft_topk3
145	  Category:   eval
146	  Status:     DONE
147	  Conclusion: killed
148	  Parent:     plan_008_rsft_topk3
149	  note: INVALID — missing --sft_adapter, killed by Director instruction
150	  Hypothesis: RSFT top_k=3 dev eval: 对比 top_k=1 RSFT (rel_f1≈0.46) 和 SFT baseline (rel_f1≈0.4057)。验证更多候选是否提升证据质量。
151	  Created:    2026-05-15T21:09:51.464Z
152	  Updated:    2026-05-15T21:38:00.000Z
153	
154	### eval_plan_008_topk3_fixed
155	  Category:   eval
156	  Status:     DONE
157	  Conclusion: killed
158	  Parent:     (none)
159	  Metrics:    (none)
160	  Created:    2026-05-15T21:39:34.632Z
161	  Updated:    2026-05-15T21:39:34.632Z
162	
163	### eval_plan_012_dpo_1ep_fixed
164	  Category:   eval
165	  Status:     DONE
166	  Conclusion: killed
167	  Parent:     (none)
168	  Metrics:    (none)
169	  Created:    2026-05-15T21:39:31.570Z
170	  Updated:    2026-05-15T21:39:31.570Z
171	
172	### eval_plan_012_dpo_1ep_fixed_r2
173	  Category:   eval
174	  Status:     DONE
175	  Conclusion: negative
176	  Parent:     (none)
177	  ign_f1:     0.4034
178	  rel_f1: 0.4034
179	  evi_f1: 0.8088
180	  edcr: 0.7139
181	  format_ok_rate: 0.999
182	  truncated_rate: 0.343
183	  predictions: 19107
184	  precision: 0.3809
185	  recall: 0.4287
186	  vs_sft_delta: -0.0023
187	  note: DPO 1ep matches SFT baseline. 1ep→3ep trajectory shows gradual decoupling (rel_f1↓ evi_f1↑), consistent with GRPO pattern. Ign-F1=F1 exact match needs investigation.
188	  Created:    2026-05-15T21:58:52.440Z
189	  Updated:    2026-05-15T23:44:56.586Z
190	
191	### eval_plan_012_dpo_ced_1ep
192	  Category:   eval
193	  Status:     DONE
194	  Conclusion: negative
195	  Parent:     (none)
196	  ign_f1:     0.0022
197	  rel_f1: 0.0022
198	  evi_f1: 0.75
199	  edcr: 0.9982
200	  num_preds: 19265
201	  format_ok: 981/985
202	  truncated: 358/985
203	  tp: 34
204	  inference_time_s: 3643
205	  Created:    2026-05-15T20:22:11.752Z
206	  Updated:    2026-05-15T21:27:30.000Z
207	
208	### eval_plan_012_dpo_ced_ckpt400
209	  Category:   eval
210	  Status:     DONE
211	  Conclusion: failed
212	  Parent:     (none)
213	  Metrics:    (none)
214	  Created:    2026-05-15T19:32:55.398Z
215	  Updated:    2026-05-15T19:37:31.477Z
216	
217	### eval_plan_014_no_evidence
218	  Category:   eval, no_evidence
219	  Status:     DONE
220	  Conclusion: failed
221	  Parent:     plan_014_sft_no_evidence
222	  Metrics:    (none)
223	  Hypothesis: Dev set eval of SFT-no-evidence model (plan_014). 核心目标：对比标准 SFT rel_f1=0.4057 vs 不输出 evidence 的 SFT rel_f1（隔离 evidence generation 代价）。只评估 rel_f1，不评估 evi_f1（输出无 evidence）。plan_id=plan_014, claim=1。
224	  Created:    2026-05-15T23:17:32.011Z
225	  Updated:    2026-05-16T01:34:06.402Z
226	
227	### eval_plan_014_no_evidence_r2
228	  Category:   eval, no_evidence
229	  Status:     DONE
230	  Conclusion: success
231	  Parent:     plan_014_sft_no_evidence
232	  ign_f1:     0.4721
233	  rel_f1: 0.4876
234	  evi_f1: 0
235	  edcr: 0
236	  evi_f1_joint: 0
237	  precision: 0.4901
238	  recall: 0.4851
239	  ign_precision: 0.4654
240	  ign_recall: 0.4791
241	  format_compliance: 0.993
242	  truncation_rate: 0.312
243	  n_predictions: 21181
244	  n_documents: 985
245	  Hypothesis: Retry of eval_plan_014_no_evidence with corrected command: --model_path 传底座 Qwen3-4B, --sft_adapter 传 SFT no-evidence adapter。修复 adapter 检测逻辑冲突。plan_id=plan_014, claim=1。
246	  Created:    2026-05-16T01:34:45.302Z
247	  Updated:    2026-05-16T04:20:13.358Z
248	
249	### eval_plan_014_sft_no_evidence
250	  Category:   eval, no_evidence
251	  Status:     DONE
252	  Conclusion: success
253	  Parent:     (none)
254	  rel_f1: 0.4893
255	  rel_ign_f1: 0.4893
256	  rel_precision: 0.4884
257	  rel_recall: 0.4902
258	  evi_f1: 0
259	  evi_precision: 0
260	  evi_recall: 0
261	  edcr: 0
262	  format_ok_rate: 0.9919
263	  n_truncated: 298
264	  n_predictions: 21064
265	  n_documents: 985
266	  n_parseable: 977
267	  inference_time_seconds: 4103.8
268	  Created:    2026-05-15T17:20:25.574Z
269	  Updated:    2026-05-15T18:42:46.665Z
270	
271	### eval_rsft_ced_s43
272	  Category:   eval
273	  Status:     DONE
274	  Conclusion: success
275	  Parent:     rsft_ced_s43_train_r3
276	  ign_f1:     0.4512
277	  rel_f1: 0.4601
278	  precision: 0.4696
279	  recall: 0.4509
280	  evi_f1: 0.8063
281	  evi_precision: 0.8025
282	  evi_recall: 0.8101
283	  edcr: 0.6542
284	  evi_f1_joint: 0.3605
285	  format_ok_rate: 1
286	  n_truncated: 184
287	  n_predictions: 15051
288	  inference_time_seconds: 10768.2
289	  Hypothesis: Full dev eval of CED RSFT seed=43 with --sft_adapter + --no-quantize. Paired t-test 关键路径：CED 第 4 个 seed。对比 flat-NLI RSFT seeds。plan_id=plan_mvp2_rsft, claim=3。
290	  Created:    2026-05-16T01:30:37.978Z
291	  Updated:    2026-05-16T05:18:59.781Z
292	
293	### eval_rsft_ced_s45
294	  Category:   eval
295	  Status:     DONE
296	  Conclusion: success
297	  Parent:     rsft_ced_s45_train_r4
298	  ign_f1:     0.4416
299	  rel_f1: 0.4514
300	  evi_f1: 0.8174
301	  rel_p: 0.4718
302	  rel_r: 0.4326
303	  edcr: 0.655
304	  evi_f1_joint: 0.3558
305	  n_truncated: 206
306	  format_ok_rate: 1
307	  Hypothesis: Full dev eval of CED RSFT seed=45 with --sft_adapter + --no-quantize. Paired t-test 关键路径：CED 第 3 个 seed（s42/s44 已有，s43 训练中）。对比 flat-NLI RSFT seeds。plan_id=plan_mvp2_rsft, claim=3。
308	  Created:    2026-05-16T01:30:34.036Z
309	  Updated:    2026-05-16T05:43:12.975Z
310	
311	### eval_sft_baseline_noquant
312	  Category:   eval
313	  Status:     DONE
314	  Conclusion: success
315	  Parent:     (none)
316	  rel_f1: 0.4106
317	  rel_precision: 0.4198
318	  rel_recall: 0.4019
319	  evi_f1: 0.8013
320	  evi_precision: 0.8005
321	  evi_recall: 0.8022
322	  evi_f1_joint: 0.3216
323	  edcr: 0.7039
324	  format_ok_rate: 0.998
325	  field_compliance_rate: 0.7066
326	  n_predictions: 16774
327	  n_truncated: 288
328	  n_documents: 985
329	  inference_time_seconds: 3677.9
330	  Created:    2026-05-15T18:38:33.128Z
331	  Updated:    2026-05-15T19:45:42.147Z
332	
333	### grpo_bf16_g4_ckpt100_eval
334	  Category:   eval, grpo
335	  Status:     DONE
336	  Conclusion: success
337	  Parent:     wave1_grpo_bf16_g4
338	  ign_f1:     0.4431
339	  f1: 0.4511
340	  evi_f1: 0.801
341	  evi_f1_joint: 0.3532
342	  EDCR: 0.6453
343	  format_compliance: 0.999
344	  field_compliance: 0.8142
345	  truncated: 182
346	  n_total: 985
347	  n_predictions: 15187
348	  inference_time_seconds: 11458.2
349	  Hypothesis: GRPO bf16 G=4 checkpoint-100 eval (D106 conditional termination): evaluate mid-training checkpoint to decide whether to continue GRPO training to step 200. If rel_f1 >= RSFT baseline (~52pp), continue. If significantly below, consider early termination.
350	  Created:    2026-05-18T16:34:51.597Z
351	  Updated:    2026-05-18T20:08:50.166Z
352	
353	### grpo_bf16_g4_ckpt200_eval
354	  Category:   eval, grpo
355	  Status:     DONE
356	  Conclusion: success
357	  Parent:     wave1_grpo_bf16_g4
358	  ign_f1:     0.4446
359	  rel_f1: 0.4513
360	  evi_f1: 0.8053
361	  evi_f1_joint: 0.3562
362	  edcr: 0.6489
363	  format_ok: 984/985
364	  n_truncated: 204
365	  n_predictions: 15733
366	  field_compliance_rate: 0.792
367	  Hypothesis: GRPO bf16 G=4 checkpoint-200 eval (final): compare with ckpt-100 for D106 learning curve. If ckpt-200 > ckpt-100, GRPO is improving. Expected: rel_f1 improvement over ckpt-100.
368	  Created:    2026-05-18T20:05:54.201Z
369	  Updated:    2026-05-18T23:16:39.233Z
370	
371	### lead2_ckpt20_eval
372	  Category:   eval
373	  Status:     DONE
374	  Conclusion: success
375	  Parent:     lead2_rsft_grpo_ced_r2
376	  ign_f1:     0.4533
377	  rel_f1: 0.4617
378	  evi_f1: 0.8103
379	  evi_f1_joint: 0.3642
380	  edcr: 0.6465
381	  precision: 0.476
382	  recall: 0.4482
383	  format_ok: 985/985
384	  truncated: 187/985
385	  predictions: 14998
386	  Hypothesis: Evaluate GRPO checkpoint-20 from RSFT base (lead2_rsft_grpo_ced_r2) on DocRED dev. If RSFT→GRPO preserves/improves rel_f1 over RSFT baseline (0.4601), it validates the RSFT→GRPO training pipeline as viable.
387	  Created:    2026-05-17T12:31:32.202Z
388	  Updated:    2026-05-17T15:27:15.598Z
389	
390	### lead2_rsft_grpo_ced
391	  Category:   grpo
392	  Status:     DONE
393	  Conclusion: failed
394	  Parent:     mvp2_rsft_train_r1_s43
395	  Metrics:    (none)
396	  Hypothesis: RSFT→bf16 GRPO two-stage: starting from RSFT best checkpoint (s43, rel_f1=0.46), short-range GRPO (50 steps, lr=1e-6) with CED-only reward should further improve evidence quality (EDCR) while preserving rel_f1, because RSFT provides stable base preventing catastrophic forgetting seen in SFT→GRPO.
397	  Created:    2026-05-17T05:57:53.951Z
398	  Updated:    2026-05-17T06:06:36.130Z
399	
400	### lead2_rsft_grpo_ced_r2
401	  Category:   grpo
402	  Status:     DONE
403	  Conclusion: failed
404	  Parent:     lead2_rsft_grpo_ced
405	  Metrics:    (none)
406	  Hypothesis: RSFT→bf16 GRPO two-stage (retry with --data_dir fix): starting from merged RSFT-s43 checkpoint (rel_f1=0.46), short-range GRPO (50 steps, lr=1e-6) with CED-only reward should improve evidence quality (EDCR) while preserving rel_f1.
407	  Created:    2026-05-17T06:23:56.474Z
408	  Updated:    2026-05-17T08:25:20.510Z
409	
410	### mvp2_eval_ced_kl001_r4_ckpt10
411	  Category:   eval
412	  Status:     DONE
413	  Conclusion: success
414	  Parent:     (none)
415	  rel_f1: 0.00296
416	  rel_precision: 0.00314
417	  rel_recall: 0.0028
418	  evi_f1: 0.72
419	  evi_precision: 0.6429
420	  evi_recall: 0.8182
421	  edcr: 0.9983
422	  n_parseable: 984
423	  n_truncated: 24
424	  n_predictions: 11621
425	  tp: 34
426	  pred_count: 10839
427	  gold_count: 12151
428	  inference_time_seconds: 5211.4
429	  Created:    2026-05-14T17:59:08.638Z
430	  Updated:    2026-05-14T19:14:08.763Z
431	
432	### mvp2_eval_ced_kl001_r4_ckpt7080
433	  Category:   eval
434	  Status:     DONE
435	  Conclusion: failed
436	  Parent:     mvp2_grpo_ced_kl001_r4
437	  Metrics:    (none)
438	  Hypothesis: Re-run failed ckpt-70/80 eval from crashed high eval (cuda:3 OOM). Completes 10-checkpoint trajectory for paper negative result analysis.
439	  Created:    2026-05-14T19:50:04.595Z
440	  Updated:    2026-05-14T19:58:46.631Z
441	
442	### mvp2_eval_ced_kl001_r4_ckpt90
443	  Category:   eval
444	  Status:     DONE
445	  Conclusion: killed
446	  Parent:     mvp2_grpo_ced_kl001_r4
447	  Metrics:    (none)
448	  Hypothesis: Eval ced_kl001_r4 best-reward checkpoint (step 90, reward=1.370, f1=0.720) — this is the primary MVP-2 judgment checkpoint. If evi_f1 ≥ SFT baseline (0.7979) + 2pp = 0.8179, MVP-2 passes.
449	  Created:    2026-05-14T18:18:13.270Z
450	  Updated:    2026-05-14T19:17:36.777Z
451	
452	### mvp2_eval_ced_kl001_r4_early
453	  Category:   eval
454	  Status:     DONE
455	  Conclusion: negative
456	  Parent:     (none)
457	  ign_f1:     0.1563
458	  f1: 0.1563
459	  evi_f1: 0.5643
460	  edcr: 0.8858
461	  precision: 0.2356
462	  recall: 0.1169
463	  evi_precision: 0.4864
464	  evi_recall: 0.6721
465	  format_ok_rate: 0.999
466	  n_parseable: 984
467	  n_truncated: 11
468	  n_predictions: 9250
469	  tp: 1421
470	  pred_count: 6032
471	  gold_count: 12151
472	  Created:    2026-05-14T17:12:53.581Z
473	  Updated:    2026-05-14T18:31:18.065Z
474	
475	### mvp2_eval_ced_kl001_r4_high
476	  Category:   eval
477	  Status:     DONE
478	  Conclusion: failed
479	  Parent:     mvp2_grpo_ced_kl001_r4
480	  checkpoint_60: {'rel_f1': 0.1467, 'ign_f1': 0.1467, 'precision': 0.1909, 'recall': 0.1192, 'evi_f1': 0.5763, 'edcr': 0.9062, 'pred_count': 10041, 'gold_count': 12151, 'n_truncated': 16, 'format_ok_rate': 1}
481	  note: Only ckpt-60 completed. Process died during ckpt-70 inference at 8% (5/62 batch). ckpt-80/90 never started.
482	  Hypothesis: High-end checkpoint eval (60,70,80,90) on cuda:3, complementing cuda:2 low-end eval. Step 90 is true best checkpoint (reward=1.370). D024 directive.
483	  Created:    2026-05-14T18:19:07.637Z
484	  Updated:    2026-05-14T19:47:58.282Z
485	
486	### mvp2_eval_ced_kl001_r4_last
487	  Category:   eval
488	  Status:     DONE
489	  Conclusion: killed
490	  Parent:     (none)
491	  Metrics:    (none)
492	  Created:    2026-05-14T18:10:05.820Z
493	  Updated:    2026-05-15T12:09:21.004Z
494	
495	### mvp2_eval_ced_kl001_r4_multi
496	  Category:   eval
497	  Status:     DONE
498	  Conclusion: killed
499	  Parent:     (none)
500	  checkpoint-10: {'f1': 0.003, 'ign_f1': 0.003, 'evi_f1': 0.72, 'edcr': 0.9983, 'format_ok_rate': 0.999}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d87ad06-9906-4a91-b6c3-b16f7aeb8597",
  "isSidechain": true,
  "promptId": "b133d549-2594-4f9e-b048-83b487db8d11",
  "agentId": "a01ea92613c0e609d",
  "type": "user",
  "uuid": "648598fc-80c5-4ca3-adb4-ed36e9d0f803",
  "sourceToolAssistantUUID": "6d87ad06-9906-4a91-b6c3-b16f7aeb8597",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T12:41:04.089Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SBqLaXkY6r1KjY8aJkmwCM`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt",
  "offset": 500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "648598fc-80c5-4ca3-adb4-ed36e9d0f803",
  "isSidechain": true,
  "agentId": "a01ea92613c0e609d",
  "requestId": "req_011CbBwiEZ3A1nDM9M8YpLTn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9edb91d2-f4b4-4a4e-9f11-dc59144785e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Gwcz8iwhpoyeg8wy5exUh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8577,
      "cache_read_input_tokens": 20961,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8577
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 20961,
          "cache_creation_input_tokens": 8577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8577,
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

_source line 19 · 2026-05-19T12:41:04.102Z_

<details><summary>↩ Tool result · `toolu_01SBqLaXkY6r1KjY8aJkmwCM`</summary>

```text
500	  checkpoint-10: {'f1': 0.003, 'ign_f1': 0.003, 'evi_f1': 0.72, 'edcr': 0.9983, 'format_ok_rate': 0.999}
501	  checkpoint-20: {'f1': 0.0088, 'ign_f1': 0.0088, 'evi_f1': 0.423, 'edcr': 0.9954, 'format_ok_rate': 0.999}
502	  checkpoint-30: {'f1': 0.0338, 'ign_f1': 0.0338, 'evi_f1': 0.5889, 'edcr': 0.9798, 'format_ok_rate': 1}
503	  checkpoint-50: {'f1': 0.1563, 'ign_f1': 0.1563, 'evi_f1': 0.5643, 'edcr': 0.8858, 'format_ok_rate': 0.999}
504	  checkpoint-60: {'f1': 0.1467, 'ign_f1': 0.1467, 'evi_f1': 0.5763, 'edcr': 0.9062, 'format_ok_rate': 1}
505	  checkpoint-90: {'f1': 0.2108, 'ign_f1': 0.2108, 'evi_f1': 0.5666, 'edcr': 0.8584, 'format_ok_rate': 1}
506	  Created:    2026-05-14T17:59:22.291Z
507	  Updated:    2026-05-14T21:27:25.338Z
508	
509	### mvp2_eval_ced_kl001_r4_step100
510	  Category:   eval
511	  Status:     DONE
512	  Conclusion: negative
513	  Parent:     mvp2_grpo_ced_kl001_r4
514	  ign_f1:     0.2167
515	  rel_f1: 0.2167
516	  precision: 0.2849
517	  recall: 0.1749
518	  evi_f1: 0.5746
519	  evi_precision: 0.5244
520	  evi_recall: 0.6353
521	  edcr: 0.8539
522	  pred_count: 7460
523	  gold_count: 12151
524	  tp: 2125
525	  n_truncated: 21
526	  format_ok_rate: 1
527	  Hypothesis: Eval ced_kl001_r4 last checkpoint (step 100) to compare with best-reward checkpoint (step 50). If best ≠ last, the gap measures training stability under batch_size=1 GRPO variance.
528	  Created:    2026-05-14T18:08:31.821Z
529	  Updated:    2026-05-14T19:41:30.318Z
530	
531	### mvp2_eval_ced_kl001_r4_step90
532	  Category:   eval
533	  Status:     DONE
534	  Conclusion: negative
535	  Parent:     mvp2_grpo_ced_kl001_r4
536	  ign_f1:     0.2108
537	  rel_f1: 0.2108
538	  evi_f1: 0.5666
539	  edcr: 0.8584
540	  pred_count: 11160
541	  n_truncated: 22
542	  format_ok_rate: 1
543	  n_documents: 985
544	  Hypothesis: Eval true best checkpoint (step 90, reward=1.370). Critical after ckpt-50 showed reward hacking (rel_f1 -24.9pp). If step 90 also fails, CED reward design has fundamental issue.
545	  Created:    2026-05-14T18:19:58.623Z
546	  Updated:    2026-05-14T20:01:45.201Z
547	
548	### mvp2_eval_lr5e6_r1_ckpt100
549	  Category:   eval
550	  Status:     DONE
551	  Conclusion: negative
552	  Parent:     mvp2_grpo_ced_lr5e6_r1
553	  ign_f1:     0.0138
554	  rel_f1: 0.0138
555	  rel_precision: 0.0132
556	  rel_recall: 0.0144
557	  evi_f1: 0.8504
558	  evi_precision: 0.9256
559	  evi_recall: 0.7866
560	  edcr: 0.9876
561	  format_ok_rate: 0.999
562	  field_compliance_rate: 0.8162
563	  evidence_format_rate: 0.8162
564	  tp: 175
565	  pred_count: 13300
566	  gold_count: 12151
567	  n_predictions: 15498
568	  n_truncated: 181
569	  n_documents: 985
570	  n_parseable: 984
571	  inference_time_seconds: 5901.7
572	  Hypothesis: P0 ckpt-100 eval: lr=5e-6 GRPO at step 100 (halfway point). Checkpoint-100 已保存。与 kl001_r4 的 step-100 (rel_f1=0.217) 形成直接对比。Pass criteria: rel_f1 > 0.30.
573	  Created:    2026-05-14T23:00:57.035Z
574	  Updated:    2026-05-15T01:30:01.493Z
575	
576	### mvp2_eval_lr5e6_r1_ckpt20
577	  Category:   eval
578	  Status:     DONE
579	  Conclusion: negative
580	  Parent:     mvp2_grpo_ced_lr5e6_r1
581	  rel_f1: 0.0077
582	  rel_precision: 0.0071
583	  rel_recall: 0.0084
584	  evi_f1: 0.628
585	  evi_precision: 0.855
586	  evi_recall: 0.496
587	  edcr: 0.993
588	  format_ok_rate: 0.991
589	  field_compliance_rate: 0.399
590	  pred_count: 14440
591	  gold_count: 12151
592	  tp: 102
593	  n_truncated: 587
594	  inference_time_seconds: 6370.4
595	  Hypothesis: P0 ckpt-20 early eval: lr=5e-6 GRPO at step 20. Pass criteria: rel_f1 > 0.30 (no catastrophic forgetting). Key MVP gate for P0.
596	  Created:    2026-05-14T20:44:21.167Z
597	  Updated:    2026-05-14T22:12:16.372Z
598	
599	### mvp2_eval_lr5e6_r1_ckpt40
600	  Category:   eval
601	  Status:     DONE
602	  Conclusion: failed
603	  Parent:     mvp2_grpo_ced_lr5e6_r1
604	  Metrics:    (none)
605	  Hypothesis: P0 ckpt-40 eval: lr=5e-6 GRPO at step 40 (where f1_reward first rises to 0.038). Director 新判定框架: ckpt-20 FAIL + ckpt-40 PASS → P0 判 PASS。Pass criteria: rel_f1 > 0.30.
606	  Created:    2026-05-14T21:25:00.579Z
607	  Updated:    2026-05-14T21:43:33.438Z
608	
609	### mvp2_eval_lr5e6_r1_ckpt40_r2
610	  Category:   eval
611	  Status:     DONE
612	  Conclusion: negative
613	  Parent:     mvp2_grpo_ced_lr5e6_r1
614	  rel_f1: 0.0071
615	  precision: 0.0066
616	  recall: 0.0078
617	  evi_f1: 0.7584
618	  evi_precision: 0.9113
619	  evi_recall: 0.6494
620	  edcr: 0.9942
621	  format_ok_rate: 0.9939
622	  field_compliance_rate: 0.5675
623	  pred_count: 14434
624	  gold_count: 12151
625	  tp: 95
626	  n_truncated: 424
627	  inference_time_seconds: 6152
628	  Hypothesis: Re-tracking orphan PID 101842 for P0 ckpt-40 eval (lr=5e-6 GRPO step 40). Original exp auto-failed due to cron/PID mismatch. Pass criteria: rel_f1 > 0.30.
629	  Created:    2026-05-14T21:41:34.558Z
630	  Updated:    2026-05-14T23:11:56.267Z
631	
632	### mvp2_eval_lr5e6_r1_ckpt60
633	  Category:   eval
634	  Status:     DONE
635	  Conclusion: failed
636	  Parent:     mvp2_grpo_ced_lr5e6_r1
637	  Metrics:    (none)
638	  Hypothesis: P0 ckpt-60 eval: lr=5e-6 GRPO at step 60. 训练轨迹数据点——ckpt-20 catastrophic forgetting (rel_f1=0.0077)，需看后续 checkpoint 是否恢复。Pass criteria: rel_f1 > 0.30.
639	  Created:    2026-05-14T22:13:47.936Z
640	  Updated:    2026-05-14T23:25:25.584Z
641	
642	### mvp2_eval_lr5e6_r1_ckpt60_r2
643	  Category:   eval
644	  Status:     DONE
645	  Conclusion: negative
646	  Parent:     mvp2_grpo_ced_lr5e6_r1
647	  rel_f1: 0.0093
648	  precision: 0.0085
649	  recall: 0.0103
650	  evi_f1: 0.81
651	  edcr: 0.993
652	  format_ok_rate: 0.998
653	  pred_count: 14626
654	  gold_count: 12151
655	  tp: 125
656	  inference_time_seconds: 6152
657	  Hypothesis: P0 ckpt-60 eval retry: 原 submit_on_allocated 失败 (pid=unknown). 手动 SSH 启动 /root/autodl-tmp/scripts/eval_lr5e6_ckpt60.sh. Pass criteria: rel_f1 > 0.30.
658	  Created:    2026-05-14T22:27:56.124Z
659	  Updated:    2026-05-15T00:07:56.895Z
660	
661	### mvp2_eval_lr5e6_r1_ckpt80
662	  Category:   eval
663	  Status:     DONE
664	  Conclusion: negative
665	  Parent:     mvp2_grpo_ced_lr5e6_r1
666	  ign_f1:     0.0116
667	  rel_f1: 0.0116
668	  precision: 0.0109
669	  recall: 0.0124
670	  evi_f1: 0.828
671	  evi_precision: 0.928
672	  evi_recall: 0.748
673	  edcr: 0.993
674	  format_ok_rate: 0.999
675	  field_compliance_rate: 0.788
676	  pred_count: 13828
677	  gold_count: 12151
678	  n_truncated: 210
679	  inference_time_seconds: 6099
680	  Hypothesis: P0 ckpt-80 eval: lr=5e-6 GRPO at step 80. 训练轨迹继续——ckpt-20 FAIL (0.0077), ckpt-40/60 待出. Step 80 reward=0.283 (回升), format_reward=0.249. Pass criteria: rel_f1 > 0.30.
681	  Created:    2026-05-14T22:25:45.043Z
682	  Updated:    2026-05-15T01:02:32.508Z
683	
684	### mvp2_eval_lr5e6_rp_r2_ckpt20
685	  Category:   eval
686	  Status:     DONE
687	  Conclusion: killed
688	  Parent:     mvp2_grpo_ced_lr5e6_rp_r2
689	  Metrics:    (none)
690	  Hypothesis: P0+P1 ckpt-20 eval: lr=5e-6 + recall_penalty GRPO at step 20. Director killed rp_r2 training (loss divergence), but ckpt-20 eval needed to close P0+P1 comparison line. Pass criteria: rel_f1 > 0.30 AND pred_count >= 9720.
691	  Created:    2026-05-14T21:44:56.448Z
692	  Updated:    2026-05-14T22:06:40.812Z
693	
694	### mvp2_eval_rsft_r1
695	  Category:   eval
696	  Status:     DONE
697	  Conclusion: success
698	  Parent:     mvp2_rsft_train_r1
699	  rel_f1: 0.4449
700	  evi_f1: 0.8187
701	  evi_f1_joint: 0.3468
702	  evi_f1_joint_P: 0.3515
703	  evi_f1_joint_R: 0.3423
704	  edcr: 0.6565
705	  num_preds: 15307
706	  sft_baseline_rel_f1: 0.4057
707	  sft_baseline_evi_f1: 0.7979
708	  delta_rel_f1: 0.0392
709	  delta_evi_f1: 0.0208
710	  delta_evi_f1_joint: 0.0351
711	  mvp2_pass: True
712	  Hypothesis: Full dev eval of RSFT r1 (seed=42). Same pipeline as s44 eval (985 docs, no-quantize). Need 3-seed data for complete_mvp. s44 PASS: rel_f1=0.4655, evi_f1=0.8087.
713	  Created:    2026-05-15T09:40:47.529Z
714	  Updated:    2026-05-15T13:27:31.402Z
715	
716	### mvp2_eval_rsft_r2a
717	  Category:   eval
718	  Status:     DONE
719	  Conclusion: success
720	  Parent:     mvp2_rsft_r2a
721	  ign_f1:     0.4494
722	  rel_f1: 0.4494
723	  evi_f1: 0.8108
724	  evi_f1_joint: 0.3509
725	  evi_f1_joint_P: 0.3423
726	  evi_f1_joint_R: 0.3599
727	  edcr: 0.6641
728	  precision: 0.4512
729	  recall: 0.4475
730	  evi_precision: 0.8143
731	  evi_recall: 0.8073
732	  format_ok_rate: 1
733	  n_predictions: 15482
734	  n_truncated: 208
735	  inference_time_s: 5967.2
736	  delta_evi_f1_joint: 0.0392
737	  Hypothesis: Full dev eval of r2a (1 epoch, alpha=128, clean data). Ablation: 1 epoch vs 3 epoch (r1). Pass: rel_f1 > 0.4057, evi_f1 > 0.798.
738	  Created:    2026-05-15T09:42:57.684Z
739	  Updated:    2026-05-15T13:27:32.756Z
740	
741	### mvp2_eval_rsft_r2b
742	  Category:   eval
743	  Status:     DONE
744	  Conclusion: success
745	  Parent:     mvp2_rsft_r2b
746	  ign_f1:     0.4493
747	  rel_f1: 0.4493
748	  evi_f1: 0.8128
749	  evi_f1_joint: 0.349
750	  evi_f1_joint_P: 0.3455
751	  evi_f1_joint_R: 0.3526
752	  edcr: 0.6609
753	  precision: 0.4566
754	  recall: 0.4424
755	  evi_precision: 0.8201
756	  evi_recall: 0.8056
757	  pred_count: 14829
758	  format_ok: 983/985
759	  truncated: 179
760	  inference_time_s: 5862
761	  delta_evi_f1_joint: 0.0373
762	  Hypothesis: Full dev eval of r2b (1 epoch, alpha=32, lr=1e-5, clean data). Ablation: conservative LoRA scaling vs r2a/r1. Pass: rel_f1 > 0.4057, evi_f1 > 0.798.
763	  Created:    2026-05-15T09:42:58.437Z
764	  Updated:    2026-05-15T13:27:35.580Z
765	
766	### mvp2_eval_rsft_r2b_maxtok1536
767	  Category:   eval
768	  Status:     DONE
769	  Conclusion: killed
770	  Parent:     mvp2_eval_rsft_r2b
771	  Metrics:    (none)
772	  Hypothesis: Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). If EDCR improves significantly (from 0.6609 toward 0.71+), current EDCR gap is truncation artifact, not model issue. If EDCR unchanged, distractor citation is genuine RSFT behavior.
773	  Created:    2026-05-15T11:49:48.849Z
774	  Updated:    2026-05-15T13:23:59.642Z
775	
776	### mvp2_eval_rsft_r2b_maxtok1536_r2
777	  Category:   eval
778	  Status:     DONE
779	  Conclusion: negative
780	  Parent:     mvp2_eval_rsft_r2b
781	  ign_f1:     0.4504
782	  rel_f1: 0.4504
783	  evi_f1: 0.8102
784	  edcr: 0.674
785	  precision: 0.4488
786	  recall: 0.4519
787	  evi_precision: 0.8162
788	  evi_recall: 0.8044
789	  n_truncated: 146
790	  n_total: 985
791	  n_predictions: 17188
792	  n_distractor_citations: 19589
793	  n_total_citations: 29063
794	  format_ok_rate: 0.998
795	  Hypothesis: Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). Retry with correct model stack (Base+SFT+RSFT). If EDCR improves significantly (from 0.6609 toward 0.71+), truncation is the cause. If unchanged, distractor citation is genuine RSFT behavior.
796	  Created:    2026-05-15T11:54:57.156Z
797	  Updated:    2026-05-15T15:21:13.816Z
798	
799	### mvp2_eval_rsft_s43
800	  Category:   eval
801	  Status:     DONE
802	  Conclusion: failed
803	  Parent:     mvp2_rsft_train_r1_s43
804	  Metrics:    (none)
805	  Hypothesis: Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798.
806	  Created:    2026-05-15T11:25:26.268Z
807	  Updated:    2026-05-15T11:29:11.205Z
808	
809	### mvp2_eval_rsft_s43_r2
810	  Category:   eval
811	  Status:     DONE
812	  Conclusion: success
813	  Parent:     mvp2_rsft_train_r1_s43
814	  ign_f1:     0.4683
815	  rel_f1: 0.4683
816	  evi_f1: 0.8156
817	  evi_f1_joint: 0.3711
818	  evi_f1_joint_P: 0.3747
819	  evi_f1_joint_R: 0.3675
820	  edcr: 0.6388
821	  precision: 0.4817
822	  recall: 0.4556
823	  evi_precision: 0.8142
824	  evi_recall: 0.817
825	  n_predictions: 14970
826	  n_truncated: 171
827	  format_ok_rate: 1
828	  inference_time_s: 6316.7
829	  sft_baseline_rel_f1: 0.4057
830	  sft_baseline_evi_f1: 0.7979
831	  delta_rel_f1: 0.0626
832	  delta_evi_f1: 0.0177
833	  delta_evi_f1_joint: 0.0594
834	  mvp2_pass: True
835	  Hypothesis: Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798. Retry of mvp2_eval_rsft_s43 (fixed arg names).
836	  Created:    2026-05-15T11:29:17.551Z
837	  Updated:    2026-05-15T13:54:26.023Z
838	
839	### mvp2_eval_rsft_s44
840	  Category:   eval
841	  Status:     DONE
842	  Conclusion: killed
843	  Parent:     mvp2_rsft_train_r1_s44
844	  Metrics:    (none)
845	  Hypothesis: Full dev eval of RSFT seed=44 checkpoint. First MVP-2 judgement data point. Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798 (SFT baseline).
846	  Created:    2026-05-15T07:35:23.934Z
847	  Updated:    2026-05-15T22:06:28.059Z
848	
849	### mvp2_eval_sft_baseline
850	  Category:   eval
851	  Status:     DONE
852	  Conclusion: success
853	  Parent:     mvp2_sft_warmup
854	  rel_f1: 0.4057
855	  evi_f1: 0.7979
856	  evi_f1_joint: 0.3117
857	  evi_f1_joint_P: 0.3037
858	  evi_f1_joint_R: 0.32
859	  edcr: 0.7118
860	  pred_count: 12234
861	  gold_count: 12151
862	  format_ok_rate: 0.998
863	  format_compliance_rate: 0.998
864	  field_compliance_rate: 0.6264
865	  n_truncated: 367
866	  inference_time_seconds: 6138.5
867	  Hypothesis: SFT baseline eval using identical eval protocol as GRPO evals (eval_lr5e6_ckpt20.sh). Required for MVP-2 core comparison: CED_Evi-F1 − SFT_Evi-F1 ≥ 2pp. Prior SFT eval (r3) used different eval path; this ensures apple-to-apple comparison.
868	  Created:    2026-05-14T21:47:41.356Z
869	  Updated:    2026-05-15T13:27:26.236Z
870	
871	### mvp2_grpo_ced
872	  Category:   grpo
873	  Status:     DONE
874	  Conclusion: failed
875	  Parent:     (none)
876	  Metrics:    (none)
877	  Created:    2026-05-14T07:10:31.165Z
878	  Updated:    2026-05-14T08:00:02.874Z
879	
880	### mvp2_grpo_ced_kl001
881	  Category:   grpo
882	  Status:     DONE
883	  Conclusion: failed
884	  Parent:     (none)
885	  Metrics:    (none)
886	  Hypothesis: kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary
887	  Created:    2026-05-14T12:32:53.111Z
888	  Updated:    2026-05-14T15:33:06.208Z
889	
890	### mvp2_grpo_ced_kl001_r2
891	  Category:   grpo
892	  Status:     DONE
893	  Conclusion: killed
894	  Parent:     mvp2_grpo_ced_kl001
895	  Metrics:    (none)
896	  Hypothesis: kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary (retry: fix --lr → --learning_rate)
897	  Created:    2026-05-14T15:23:16.518Z
898	  Updated:    2026-05-15T12:09:19.263Z
899	
900	### mvp2_grpo_ced_kl001_r3
901	  Category:   grpo
902	  Status:     DONE
903	  Conclusion: killed
904	  Parent:     mvp2_grpo_ced_kl001
905	  Metrics:    (none)
906	  Hypothesis: kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary (retry: fix --lr + bash -c wrapping)
907	  Created:    2026-05-14T15:25:06.729Z
908	  Updated:    2026-05-15T12:09:20.252Z
909	
910	### mvp2_grpo_ced_kl001_r4
911	  Category:   grpo
912	  Status:     DONE
913	  Conclusion: success
914	  Parent:     (none)
915	  final_step: 100
916	  train_runtime_s: 9069.88
917	  reward_final: 1.195
918	  f1_reward_final: 0.573
919	  ced_reward_final: 0.328
920	  format_reward_final: 0.293
921	  frac_zero_std_final: 0.2
922	  kl_final: 0.118
923	  loss_final: -0.009
924	  grad_norm_final: 0.14
925	  entropy_final: 0.067
926	  completion_length_mean_final: 520.8
927	  best_reward_step: 90
928	  best_reward: 1.37
929	  best_f1_reward: 0.72
930	  best_ced_reward: 0.353
931	  Created:    2026-05-14T15:32:32.529Z
932	  Updated:    2026-05-14T18:11:53.975Z
933	
934	### mvp2_grpo_ced_lr5e6_p1_r1
935	  Category:   grpo
936	  Status:     DONE
937	  Conclusion: killed
938	  Parent:     (none)
939	  Metrics:    (none)
940	  Hypothesis: D031/P0+P1: lr=5e-6 + --ced_recall_penalty fixes both catastrophic forgetting (lr) and CED recall shortcut (penalty). Pass criteria: ckpt-20 rel_f1 > 0.30 AND pred_count >= 15000 (SFT 80%). Comparing vs P0 isolates CED shortcut fix contribution.
941	  Created:    2026-05-14T19:28:59.245Z
942	  Updated:    2026-05-14T20:31:06.969Z
943	
944	### mvp2_grpo_ced_lr5e6_r1
945	  Category:   grpo
946	  Status:     DONE
947	  Conclusion: killed
948	  Parent:     mvp2_grpo_ced_kl001_r4
949	  Metrics:    (none)
950	  Hypothesis: D030/P0: lr=5e-6 (10x lower than ced_kl001_r4) prevents catastrophic forgetting while maintaining CED reward improvement. Community consensus GRPO+QLoRA lr=5e-6~1e-5. Pass criteria: ckpt-20 rel_f1 > 0.30. Extra monitoring: pred_count + recall trend.
951	  Created:    2026-05-14T19:21:08.231Z
952	  Updated:    2026-05-15T01:29:06.862Z
953	
954	### mvp2_grpo_ced_lr5e6_rp_r1
955	  Category:   grpo
956	  Status:     DONE
957	  Conclusion: failed
958	  Parent:     mvp2_grpo_ced_kl001_r4
959	  Metrics:    (none)
960	  Hypothesis: D032/P0+P1: lr=5e-6 + --ced_recall_penalty fixes both catastrophic forgetting (lr) and CED recall shortcut (penalty). Pass criteria: ckpt-20 rel_f1 > 0.30 AND pred_count >= 9720 (SFT 80%). Comparing vs P0 isolates CED shortcut fix contribution.
961	  Created:    2026-05-14T19:44:15.272Z
962	  Updated:    2026-05-14T20:44:07.125Z
963	
964	### mvp2_grpo_ced_lr5e6_rp_r2
965	  Category:   grpo
966	  Status:     DONE
967	  Conclusion: killed
968	  Parent:     mvp2_grpo_ced_kl001_r4
969	  Metrics:    (none)
970	  Hypothesis: D032/P0+P1 retry: lr=5e-6 + --ced_recall_penalty fixes both catastrophic forgetting (lr) and CED recall shortcut (penalty). Pass criteria: ckpt-20 rel_f1 > 0.30 AND pred_count >= 9720 (SFT 80%). Comparing vs P0 (lr5e6_r1) isolates CED shortcut fix contribution. Retry of rp_r1 which failed due to bas...
971	  Created:    2026-05-14T20:04:55.831Z
972	  Updated:    2026-05-14T21:40:50.174Z
973	
974	### mvp2_grpo_ced_r1
975	  Category:   grpo
976	  Status:     DONE
977	  Conclusion: killed
978	  Parent:     (none)
979	  Metrics:    (none)
980	  Created:    2026-05-14T08:02:41.858Z
981	  Updated:    2026-05-14T10:37:23.856Z
982	
983	### mvp2_grpo_ced_r2
984	  Category:   grpo
985	  Status:     DONE
986	  Conclusion: killed
987	  Parent:     (none)
988	  Metrics:    (none)
989	  Created:    2026-05-14T10:58:11.663Z
990	  Updated:    2026-05-14T11:31:49.724Z
991	
992	### mvp2_grpo_ced_r3
993	  Category:   grpo
994	  Status:     DONE
995	  Conclusion: failed
996	  Parent:     (none)
997	  Metrics:    (none)
998	  Hypothesis: CED reward with balanced weights (format×0.3, f1×3.0, ced×1.0) + stable training (num_iterations=1, KL early stop at 100) + kl_coef=0.05 improves Evi-F1 over SFT baseline
999	  Created:    2026-05-14T11:47:53.099Z
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9edb91d2-f4b4-4a4e-9f11-dc59144785e1",
  "isSidechain": true,
  "promptId": "b133d549-2594-4f9e-b048-83b487db8d11",
  "agentId": "a01ea92613c0e609d",
  "type": "user",
  "uuid": "7253401b-a142-4d65-a42f-0c05d35af87f",
  "sourceToolAssistantUUID": "9edb91d2-f4b4-4a4e-9f11-dc59144785e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T12:41:11.306Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MrucPfE2sGtt9RJmnfng5Q`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt",
  "offset": 999,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7253401b-a142-4d65-a42f-0c05d35af87f",
  "isSidechain": true,
  "agentId": "a01ea92613c0e609d",
  "requestId": "req_011CbBwicuhirPTu7UDXqQrr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6563a3c2-9050-4aab-9852-59cc62f04bb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKeULxN49H6WY1aspA4WqT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9236,
      "cache_read_input_tokens": 29538,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9236
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 29538,
          "cache_creation_input_tokens": 9236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9236,
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

_source line 21 · 2026-05-19T12:41:11.313Z_

<details><summary>↩ Tool result · `toolu_01MrucPfE2sGtt9RJmnfng5Q`</summary>

```text
999	  Created:    2026-05-14T11:47:53.099Z
1000	  Updated:    2026-05-14T12:09:23.005Z
1001	
1002	### mvp2_grpo_ced_r4
1003	  Category:   grpo
1004	  Status:     DONE
1005	  Conclusion: killed
1006	  Parent:     (none)
1007	  Metrics:    (none)
1008	  Created:    2026-05-14T12:10:15.698Z
1009	  Updated:    2026-05-14T12:30:06.177Z
1010	
1011	### mvp2_grpo_ced_r5
1012	  Category:   grpo
1013	  Status:     DONE
1014	  Conclusion: negative
1015	  Parent:     (none)
1016	  Metrics:    (none)
1017	  Created:    2026-05-14T12:31:45.606Z
1018	  Updated:    2026-05-14T15:32:21.817Z
1019	
1020	### mvp2_grpo_extract
1021	  Category:   grpo
1022	  Status:     DONE
1023	  Conclusion: failed
1024	  Parent:     (none)
1025	  Metrics:    (none)
1026	  Hypothesis: Extraction-only reward (format+F1, no CED) establishes GRPO baseline — CED r3 should exceed this on Evi-F1
1027	  Created:    2026-05-14T07:10:35.796Z
1028	  Updated:    2026-05-14T12:25:32.094Z
1029	
1030	### mvp2_grpo_extract_r2
1031	  Category:   grpo
1032	  Status:     DONE
1033	  Conclusion: killed
1034	  Parent:     (none)
1035	  Metrics:    (none)
1036	  Created:    2026-05-14T12:10:19.532Z
1037	  Updated:    2026-05-14T12:30:08.099Z
1038	
1039	### mvp2_grpo_extract_r3
1040	  Category:   grpo
1041	  Status:     DONE
1042	  Conclusion: negative
1043	  Parent:     (none)
1044	  Metrics:    (none)
1045	  Created:    2026-05-14T12:31:48.781Z
1046	  Updated:    2026-05-14T16:59:20.304Z
1047	
1048	### mvp2_grpo_extract_r4
1049	  Category:   grpo
1050	  Status:     DONE
1051	  Conclusion: killed
1052	  Parent:     mvp2_grpo_extract_r3
1053	  Metrics:    (none)
1054	  Hypothesis: Extraction-only reward (format×0.3, f1×3.0, ced=0) with kl_coef=0.01 + num_generations=8 trains stably. 100-step probe parallel ablation with ced_kl001_r4 (CED reward) to compare reward type impact under identical stability config.
1055	  Created:    2026-05-14T16:54:59.403Z
1056	  Updated:    2026-05-14T17:40:25.731Z
1057	
1058	### mvp2_grpo_flatnli
1059	  Category:   grpo
1060	  Status:     DONE
1061	  Conclusion: failed
1062	  Parent:     (none)
1063	  Metrics:    (none)
1064	  Hypothesis: Flat-NLI reward (non-contrastive) improves Evi-F1 over extraction-only but less than CED — validates contrastive component's incremental value
1065	  Created:    2026-05-14T07:10:33.848Z
1066	  Updated:    2026-05-14T12:13:34.747Z
1067	
1068	### mvp2_grpo_flatnli_r2
1069	  Category:   grpo
1070	  Status:     DONE
1071	  Conclusion: killed
1072	  Parent:     (none)
1073	  Metrics:    (none)
1074	  Created:    2026-05-14T12:10:23.287Z
1075	  Updated:    2026-05-14T12:30:08.865Z
1076	
1077	### mvp2_grpo_flatnli_r3
1078	  Category:   grpo
1079	  Status:     DONE
1080	  Conclusion: killed
1081	  Parent:     (none)
1082	  Metrics:    (none)
1083	  Created:    2026-05-14T12:31:52.782Z
1084	  Updated:    2026-05-14T15:27:55.267Z
1085	
1086	### mvp2_grpo_flatnli_r4
1087	  Category:   grpo
1088	  Status:     DONE
1089	  Conclusion: killed
1090	  Parent:     (none)
1091	  Metrics:    (none)
1092	  Created:    2026-05-14T15:32:31.804Z
1093	  Updated:    2026-05-14T16:56:12.080Z
1094	
1095	### mvp2_grpo_flatnli_r5
1096	  Category:   grpo
1097	  Status:     DONE
1098	  Conclusion: killed
1099	  Parent:     mvp2_grpo_flatnli_r4
1100	  Metrics:    (none)
1101	  Hypothesis: Flat-NLI reward with kl_coef=0.01 + num_generations=8 prevents mode collapse. Resume from flatnli_r3 checkpoint-100 (healthy). 100-step probe (steps 100→200) to verify stability before full run.
1102	  Created:    2026-05-14T16:55:02.197Z
1103	  Updated:    2026-05-14T17:26:55.692Z
1104	
1105	### mvp2_grpo_flatnli_r6
1106	  Category:   grpo
1107	  Status:     DONE
1108	  Conclusion: negative
1109	  Parent:     mvp2_grpo_flatnli_r5
1110	  steps_completed: 25
1111	  final_frac_zero_std: 0.9
1112	  final_f1_reward: 0
1113	  final_flat_nli_reward: 0
1114	  final_format_reward: 0.293
1115	  collapse_step: 25
1116	  Hypothesis: Flat-NLI reward with kl_coef=0.01 + num_generations=8 from SFT scratch (not resume). 100-step probe to verify stability. Same D020 config as ced_kl001_r4 (which is healthy). Tests whether flat-NLI reward type works under stable training config.
1117	  Created:    2026-05-14T17:25:07.083Z
1118	  Updated:    2026-05-14T18:17:52.909Z
1119	
1120	### mvp2_sft_eval
1121	  Category:   eval
1122	  Status:     DONE
1123	  Conclusion: killed
1124	  Parent:     (none)
1125	  Metrics:    (none)
1126	  Created:    2026-05-14T07:10:37.449Z
1127	  Updated:    2026-05-14T12:46:04.523Z
1128	
1129	### mvp2_sft_eval_r2
1130	  Category:   eval
1131	  Status:     DONE
1132	  Conclusion: success
1133	  Parent:     (none)
1134	  ign_f1:     0.4057
1135	  rel_f1: 0.4057
1136	  evi_f1: 0.7979
1137	  edcr: 0.7118
1138	  precision: 0.4043
1139	  recall: 0.407
1140	  evi_precision: 0.8035
1141	  evi_recall: 0.7924
1142	  format_ok_rate: 0.998
1143	  format_compliance_rate: 0.626
1144	  n_parseable: 617
1145	  n_truncated: 367
1146	  n_predictions: 18815
1147	  inference_time_seconds: 6484.7
1148	  Created:    2026-05-14T12:45:46.160Z
1149	  Updated:    2026-05-14T14:54:07.338Z
1150	
1151	### mvp2_sft_eval_r3
1152	  Category:   eval
1153	  Status:     DONE
1154	  Conclusion: success
1155	  Parent:     (none)
1156	  ign_f1:     0.4057
1157	  rel_f1: 0.4057
1158	  evi_f1: 0.7979
1159	  edcr: 0.7118
1160	  precision: 0.4043
1161	  recall: 0.407
1162	  evi_precision: 0.8035
1163	  evi_recall: 0.7924
1164	  format_ok_rate: 0.998
1165	  format_compliance_rate: 0.626
1166	  n_parseable: 617
1167	  n_truncated: 367
1168	  n_predictions: 18815
1169	  Created:    2026-05-14T13:52:38.174Z
1170	  Updated:    2026-05-14T17:06:57.010Z
1171	
1172	### plan006_1_7b_rsft_eval
1173	  Category:   eval
1174	  Status:     DONE
1175	  Conclusion: killed
1176	  Parent:     (none)
1177	  Metrics:    (none)
1178	  Created:    2026-05-17T06:10:39.978Z
1179	  Updated:    2026-05-17T23:18:35.353Z
1180	
1181	### plan017_14b_sft_eval
1182	  Category:   eval
1183	  Status:     DONE
1184	  Conclusion: killed
1185	  Parent:     plan017_14b_sft
1186	  Metrics:    (none)
1187	  Hypothesis: D076 eval for 14B SFT baseline. 14B 是第 4 个 scale 档（1.7B/4B/8B/14B），SFT baseline 用于计算 RSFT 增益和 evidence tax。预期 ign_f1 高于 8B SFT mean (0.4866)。
1188	  Created:    2026-05-19T07:23:43.367Z
1189	  Updated:    2026-05-19T08:54:24.083Z
1190	
1191	### plan017_14b_sft_no_evidence_eval
1192	  Category:   eval, no_evidence
1193	  Status:     DONE
1194	  Conclusion: killed
1195	  Parent:     plan017_14b_sft
1196	  Metrics:    (none)
1197	  Hypothesis: 14B SFT no-evidence eval: 测量 14B SFT 在不提供 evidence 时的 ign_f1，用于计算 evidence tax (Claim 3)。与 4B evidence tax (D107: 47.21% vs 39.74%) 对比，验证 scale-dependent evidence tax 趋势。
1198	  Created:    2026-05-19T07:23:46.290Z
1199	  Updated:    2026-05-19T08:49:48.692Z
1200	
1201	### plan019_1_7b_rsft_s43_r2_eval
1202	  Category:   eval
1203	  Status:     DONE
1204	  Conclusion: success
1205	  Parent:     plan019_1_7b_rsft_s43_r2
1206	  ign_f1:     0.5109
1207	  ign_precision: 0.5186
1208	  ign_recall: 0.5035
1209	  f1: 0.5271
1210	  precision: 0.5444
1211	  recall: 0.5109
1212	  evi_precision: 0.8218
1213	  evi_recall: 0.834
1214	  evi_f1: 0.8278
1215	  edcr: 0.6245
1216	  evi_joint_precision: 0.4336
1217	  evi_joint_recall: 0.4221
1218	  evi_f1_joint: 0.4278
1219	  format_compliance_rate: 0.999
1220	  field_compliance_rate: 0.7503
1221	  n_truncated: 244
1222	  inference_time_seconds: 8498.2
1223	  Hypothesis: D076 eval for 1.7B RSFT s43_r2 (Method A: s42 SFT adapter + s42 CED k=1 data, RSFT seed=43). 预期 ign_f1 接近 s42 RSFT (0.5122)，验证 1.7B RSFT 跨 seed 稳健性。
1224	  Created:    2026-05-19T06:15:45.750Z
1225	  Updated:    2026-05-19T08:42:24.182Z
1226	
1227	### plan019_1_7b_rsft_s44_r2_eval
1228	  Category:   eval
1229	  Status:     DONE
1230	  Conclusion: success
1231	  Parent:     plan019_1_7b_rsft_s44_r2
1232	  ign_f1:     0.5125
1233	  ign_precision: 0.5173
1234	  ign_recall: 0.5078
1235	  f1: 0.5294
1236	  precision: 0.5434
1237	  recall: 0.5162
1238	  evi_precision: 0.815
1239	  evi_recall: 0.8387
1240	  evi_f1: 0.8267
1241	  edcr: 0.6181
1242	  evi_joint_precision: 0.4284
1243	  evi_joint_recall: 0.4294
1244	  evi_f1_joint: 0.4289
1245	  format_compliance_rate: 0.999
1246	  field_compliance_rate: 0.7543
1247	  n_truncated: 240
1248	  inference_time_seconds: 8615.6
1249	  Hypothesis: D076 eval for 1.7B RSFT s44_r2 (Method A: s42 SFT adapter + s42 CED k=1 data, RSFT seed=44). 预期 ign_f1 接近 s42 (0.5122) 和 s43 (0.5109)，完成 1.7B 3-seed RSFT 统计。
1250	  Created:    2026-05-19T08:43:01.975Z
1251	  Updated:    2026-05-19T12:00:32.897Z
1252	
1253	### plan019_1_7b_sft_s43_eval
1254	  Category:   eval
1255	  Status:     DONE
1256	  Conclusion: success
1257	  Parent:     plan019_1_7b_sft_s43
1258	  ign_f1:     0.4286
1259	  f1: 0.4372
1260	  ign_precision: 0.4475
1261	  ign_recall: 0.4111
1262	  precision: 0.4704
1263	  recall: 0.4084
1264	  evi_f1: 0.835
1265	  evi_f1_joint: 0.3442
1266	  edcr: 0.704
1267	  format_compliance: 1
1268	  field_compliance: 0.5858
1269	  n_total: 985
1270	  n_predictions: 18140
1271	  n_truncated: 408
1272	  inference_time_seconds: 5257.4
1273	  Hypothesis: Eval 1.7B SFT seed43 on DocRED dev set to measure RE performance. Paired with s42 for 2-seed mean±std at 1.7B scale.
1274	  Created:    2026-05-18T20:33:55.681Z
1275	  Updated:    2026-05-18T22:03:20.771Z
1276	
1277	### plan019_1_7b_sft_s44_eval
1278	  Category:   eval
1279	  Status:     DONE
1280	  Conclusion: success
1281	  Parent:     plan019_1_7b_sft_s44
1282	  ign_f1:     0.4321
1283	  f1: 0.4441
1284	  evi_f1_tp: 0.819
1285	  evi_f1_joint: 0.3482
1286	  edcr: 0.69
1287	  n_truncated: 473
1288	  n_predictions: 20237
1289	  n_documents: 985
1290	  format_ok_rate: 1
1291	  field_compliance_rate: 0.5198
1292	  evidence_format_rate: 0.5198
1293	  inference_time_seconds: 6146
1294	  Hypothesis: 1.7B SFT seed44 eval (D076 protocol): measure baseline SFT performance for seed44 at 1.7B scale. Paired with canonical s42 for scaling seed robustness. Expected rel_f1 ~49.5 based on canonical 1.7B SFT.
1295	  Created:    2026-05-18T16:34:45.563Z
1296	  Updated:    2026-05-18T19:27:55.325Z
1297	
1298	### plan019_8b_rsft_s44_eval
1299	  Category:   eval
1300	  Status:     DONE
1301	  Conclusion: success
1302	  Parent:     plan019_8b_rsft_s44
1303	  ign_f1:     0.5451
1304	  f1: 0.562
1305	  evi_f1_tp: 0.8145
1306	  evi_f1_dreeam: 0.4472
1307	  edcr: 0.6233
1308	  format_ok: 985/985
1309	  truncated: 230/985
1310	  predictions: 16254
1311	  Hypothesis: 8B RSFT s44 eval (Option A seed expansion). 预期 ign_f1 接近 canonical s42 (0.5376)，验证 RSFT 增益在 8B 尺度跨 seed 稳定。
1312	  Created:    2026-05-19T02:11:06.132Z
1313	  Updated:    2026-05-19T05:08:07.693Z
1314	
1315	### plan019_8b_sft_s44_eval
1316	  Category:   eval
1317	  Status:     DONE
1318	  Conclusion: success
1319	  Parent:     plan019_8b_sft_s44
1320	  ign_f1:     0.4681
1321	  f1: 0.4841
1322	  evi_f1: 0.8361
1323	  evi_f1_joint: 0.3839
1324	  edcr: 0.6697
1325	  format_ok_rate: 1
1326	  n_truncated: 306
1327	  n_predictions: 16690
1328	  inference_time_seconds: 6951.1
1329	  Hypothesis: 8B SFT s44 eval (D076 protocol): measure SFT baseline for seed44 at 8B scale. Paired with canonical s42 (ign_f1=0.5051) for 2-seed mean±std.
1330	  Created:    2026-05-18T21:36:26.622Z
1331	  Updated:    2026-05-18T23:44:30.382Z
1332	
1333	### plan_002_test_eval_s44
1334	  Category:   eval
1335	  Status:     DONE
1336	  Conclusion: failed
1337	  Parent:     (none)
1338	  Metrics:    (none)
1339	  Created:    2026-05-15T18:05:47.701Z
1340	  Updated:    2026-05-15T18:20:17.405Z
1341	
1342	### plan_002_test_eval_s44_r2
1343	  Category:   eval
1344	  Status:     DONE
1345	  Conclusion: success
1346	  Parent:     (none)
1347	  Metrics:    (none)
1348	  Hypothesis: DocRED test set evaluation for RSFT-CED s44 (best dev config). Final benchmark numbers for paper submission; test set performance confirms dev set gains are not overfitting artifacts.
1349	  Created:    2026-05-16T08:14:36.494Z
1350	  Updated:    2026-05-17T02:56:29.283Z
1351	
1352	### plan_006_llama_rsft_r3_eval
1353	  Category:   eval
1354	  Status:     DONE
1355	  Conclusion: success
1356	  Parent:     (none)
1357	  ign_f1:     0.5563
1358	  f1: 0.5674
1359	  evi_f1: 0.8255
1360	  edcr: 0.5856
1361	  evi_f1_joint: 0.4571
1362	  format_compliance_rate: 0.997
1363	  field_compliance_rate: 0.807
1364	  n_truncated: 187
1365	  inference_time_seconds: 8650
1366	  Hypothesis: Evaluate LLaMA-3.1-8B RSFT r3 (checkpoint-3312, final) on DocRED dev. Cross-architecture validation: if CED-RSFT works on both Qwen and LLaMA, the method is architecture-agnostic.
1367	  Created:    2026-05-17T08:35:48.098Z
1368	  Updated:    2026-05-17T23:17:59.347Z
1369	
1370	### plan_006_llama_rsft_seed43_eval
1371	  Category:   eval
1372	  Status:     DONE
1373	  Conclusion: failed
1374	  Parent:     plan_006_llama_rsft_seed43
1375	  Metrics:    (none)
1376	  Hypothesis: Evaluate LLaMA-8B RSFT seed 43 on DocRED dev. Seed 42 gave rel_f1=0.5674. If seed 43 gives similar result (±1.5pp, i.e., 0.55-0.58), the cross-architecture RSFT claim is robust against seed variance.
1377	  Created:    2026-05-17T16:00:04.294Z
1378	  Updated:    2026-05-17T16:48:26.809Z
1379	
1380	### plan_006_llama_rsft_seed43_eval_r2
1381	  Category:   eval
1382	  Status:     DONE
1383	  Conclusion: success
1384	  Parent:     plan_006_llama_rsft_seed43
1385	  ign_f1:     0.5619
1386	  rel_f1: 0.5727
1387	  evi_f1: 0.8206
1388	  evi_f1_joint: 0.4551
1389	  edcr: 0.6073
1390	  format_compliance_rate: 1
1391	  n_truncated: 197
1392	  Hypothesis: Evaluate LLaMA-8B RSFT seed 43 on DocRED dev (retry with correct base_model path). Seed 42 gave rel_f1=0.5674. If seed 43 gives similar result (±1.5pp), the cross-architecture RSFT claim is robust against seed variance.
1393	  Created:    2026-05-17T16:03:41.592Z
1394	  Updated:    2026-05-17T18:48:55.143Z
1395	
1396	### plan_006_qwen3_1_7b_no_evidence_eval
1397	  Category:   eval, no_evidence
1398	  Status:     DONE
1399	  Conclusion: failed
1400	  Parent:     (none)
1401	  ign_f1:     0.3786
1402	  f1: 0.3884
1403	  evi_f1: 0.0007
1404	  edcr: 0.9848
1405	  precision: 0.4282
1406	  recall: 0.3553
1407	  pred_count: 27049
1408	  n_truncated: 531
1409	  format_ok_rate: 0.999
1410	  Created:    2026-05-16T09:25:53.604Z
1411	  Updated:    2026-05-16T11:17:18.299Z
1412	
1413	### plan_006_qwen3_1_7b_no_evidence_eval_v2
1414	  Category:   eval, no_evidence
1415	  Status:     DONE
1416	  Conclusion: failed
1417	  Parent:     (none)
1418	  Metrics:    (none)
1419	  Created:    2026-05-16T11:40:29.706Z
1420	  Updated:    2026-05-16T11:44:58.762Z
1421	
1422	### plan_006_qwen3_1_7b_no_evidence_eval_v2r2
1423	  Category:   eval, no_evidence
1424	  Status:     DONE
1425	  Conclusion: failed
1426	  Parent:     (none)
1427	  Metrics:    (none)
1428	  Created:    2026-05-16T12:02:28.162Z
1429	  Updated:    2026-05-16T12:28:44.616Z
1430	
1431	### plan_006_qwen3_1_7b_no_evidence_eval_v3
1432	  Category:   eval, no_evidence
1433	  Status:     DONE
1434	  Conclusion: success
1435	  Parent:     plan_006_qwen3_1_7b_no_evidence_sft
1436	  ign_f1:     0.3982
1437	  rel_f1: 0.4103
1438	  evi_f1: 0
1439	  edcr: 0
1440	  precision: 0.4464
1441	  recall: 0.3796
1442	  format_compliance_rate: 1
1443	  n_truncated: 501
1444	  inference_time_seconds: 7465.3
1445	  evidence_tax: 0.0804
1446	  Hypothesis: 1.7B model capacity is insufficient to jointly optimize RE and evidence generation: no-evidence SFT should outperform evidence-SFT on rel_f1, revealing positive evidence tax at small scale (opposite to 8B where tax≈0).
1447	  Created:    2026-05-16T11:45:02.749Z
1448	  Updated:    2026-05-17T02:55:24.084Z
1449	
1450	### plan_006_qwen3_1_7b_no_evidence_sft
1451	  Category:   no_evidence
1452	  Status:     DONE
1453	  Conclusion: success
1454	  Parent:     (none)
1455	  Metrics:    (none)
1456	  Hypothesis: Qwen3-1.7B no-evidence SFT baseline for evidence tax measurement at 1.7B scale. Paired with evidence-SFT to quantify whether evidence generation constrains or helps small model RE performance.
1457	  Created:    2026-05-16T07:32:23.806Z
1458	  Updated:    2026-05-17T02:56:15.512Z
1459	
1460	### plan_006_qwen3_1_7b_rsft_eval
1461	  Category:   eval
1462	  Status:     DONE
1463	  Conclusion: failed
1464	  Parent:     plan_006_qwen3_1_7b_rsft_train
1465	  Metrics:    (none)
1466	  Hypothesis: Evaluate 1.7B RSFT model on DocRED dev to measure rel_f1 improvement over SFT baseline. Validates that CED-filtered RSFT generalizes to smallest model scale (1.7B) in the scaling study.
1467	  Created:    2026-05-17T06:12:11.998Z
1468	  Updated:    2026-05-17T08:25:24.429Z
1469	
1470	### plan_006_qwen3_1_7b_rsft_eval_r2
1471	  Category:   eval
1472	  Status:     DONE
1473	  Conclusion: success
1474	  Parent:     plan_006_qwen3_1_7b_rsft_train
1475	  ign_f1:     0.505
1476	  f1: 0.5219
1477	  evi_f1: 0.8309
1478	  edcr: 0.6297
1479	  evi_f1_joint: 0.4223
1480	  format_compliance_rate: 0.999
1481	  field_compliance_rate: 0.732
1482	  n_truncated: 258
1483	  inference_time_seconds: 9464
1484	  Hypothesis: Evaluate 1.7B RSFT model (checkpoint-1698) on DocRED dev. Retry after disk-full crash. Validates CED-filtered RSFT at smallest model scale in scaling study.
1485	  Created:    2026-05-17T08:35:45.455Z
1486	  Updated:    2026-05-17T23:18:01.212Z
1487	
1488	### plan_006_qwen3_1_7b_rsft_seed43_eval
1489	  Category:   eval
1490	  Status:     DONE
1491	  Conclusion: success
1492	  Parent:     plan_006_qwen3_1_7b_rsft_seed43
1493	  ign_f1:     0.5024
1494	  f1: 0.518
1495	  evi_f1_joint: 0.4201
1496	  evi_f1_tp: 0.8341
1497	  edcr: 0.6246
1498	  precision: 0.535
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6563a3c2-9050-4aab-9852-59cc62f04bb8",
  "isSidechain": true,
  "promptId": "b133d549-2594-4f9e-b048-83b487db8d11",
  "agentId": "a01ea92613c0e609d",
  "type": "user",
  "uuid": "6db2f92d-7a51-4513-b07d-06259cbac95a",
  "sourceToolAssistantUUID": "6563a3c2-9050-4aab-9852-59cc62f04bb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T12:41:16.673Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PKrYcsZ5nrqFTxLGJhBwF5`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt",
  "offset": 1490,
  "limit": 600
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6db2f92d-7a51-4513-b07d-06259cbac95a",
  "isSidechain": true,
  "agentId": "a01ea92613c0e609d",
  "requestId": "req_011CbBwj9pK39tTpoivxGD4L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19574c01-8ebb-4fd7-b6e2-a410b9c06595",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VQ4KqP8KvV1fZjRkJk6AzC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8623,
      "cache_read_input_tokens": 38774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8623,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 23 · 2026-05-19T12:41:16.683Z_

<details><summary>↩ Tool result · `toolu_01PKrYcsZ5nrqFTxLGJhBwF5`</summary>

```text
1490	  Status:     DONE
1491	  Conclusion: success
1492	  Parent:     plan_006_qwen3_1_7b_rsft_seed43
1493	  ign_f1:     0.5024
1494	  f1: 0.518
1495	  evi_f1_joint: 0.4201
1496	  evi_f1_tp: 0.8341
1497	  edcr: 0.6246
1498	  precision: 0.535
1499	  recall: 0.5019
1500	  ign_precision: 0.5099
1501	  ign_recall: 0.4951
1502	  format_ok: 984/985
1503	  n_truncated: 262
1504	  n_predictions: 16455
1505	  Hypothesis: Evaluate 1.7B RSFT seed 43 on DocRED dev. Seed 42 gave rel_f1=0.5219. If seed 43 gives similar result (±1pp, i.e., 0.51-0.53), the 1.7B scaling study datapoint is robust.
1506	  Created:    2026-05-17T14:26:15.446Z
1507	  Updated:    2026-05-17T19:56:30.167Z
1508	
1509	### plan_006_qwen3_1_7b_sft_eval
1510	  Category:   eval
1511	  Status:     DONE
1512	  Conclusion: success
1513	  Parent:     plan_006_qwen3_1_7b_sft_bf16
1514	  ign_f1:     0.4786
1515	  f1: 0.4945
1516	  evi_f1: 0.8316
1517	  edcr: 0.6704
1518	  precision: 0.5085
1519	  recall: 0.4813
1520	  ign_precision: 0.483
1521	  ign_recall: 0.4743
1522	  evi_precision: 0.8203
1523	  evi_recall: 0.8432
1524	  evi_f1_joint: 0.3958
1525	  format_compliance_rate: 1
1526	  n_predictions: 17184
1527	  n_truncated: 314
1528	  inference_time_seconds: 6848.7
1529	  Hypothesis: Qwen3-1.7B evidence-SFT eval under D076 protocol. Establishes smallest-scale SFT baseline; evidence tax at 1.7B predicted negative (evidence helps small models by constraining over-prediction).
1530	  Created:    2026-05-16T08:14:26.923Z
1531	  Updated:    2026-05-17T02:56:02.886Z
1532	
1533	### plan_006_qwen3_8b_no_evidence_eval
1534	  Category:   eval, no_evidence
1535	  Status:     DONE
1536	  Conclusion: killed
1537	  Parent:     (none)
1538	  Metrics:    (none)
1539	  Created:    2026-05-16T11:12:04.565Z
1540	  Updated:    2026-05-16T11:16:54.766Z
1541	
1542	### plan_006_qwen3_8b_no_evidence_eval_v2
1543	  Category:   eval, no_evidence
1544	  Status:     DONE
1545	  Conclusion: success
1546	  Parent:     plan_006_qwen3_8b_no_evidence_sft
1547	  Metrics:    (none)
1548	  Hypothesis: 8B model capacity absorbs evidence generation cost: no-evidence SFT and evidence-SFT should produce near-identical rel_f1, demonstrating evidence tax≈0 at 8B scale (contrasting with 4B where tax=-7.5pp).
1549	  Created:    2026-05-16T11:17:39.361Z
1550	  Updated:    2026-05-17T02:55:34.661Z
1551	
1552	### plan_006_qwen3_8b_no_evidence_sft
1553	  Category:   no_evidence
1554	  Status:     DONE
1555	  Conclusion: success
1556	  Parent:     (none)
1557	  train_loss: 0.6509
1558	  eval_loss: 0.8153
1559	  eval_mean_token_accuracy: 0.8174
1560	  eval_entropy: 0.6275
1561	  train_runtime_sec: 3656
1562	  epoch: 3
1563	  Hypothesis: Qwen3-8B no-evidence SFT baseline for evidence tax measurement at 8B scale. If 8B no-evi rel_f1 ≈ 8B evidence-SFT rel_f1, confirms that 8B absorbs evidence cost (tax≈0).
1564	  Created:    2026-05-16T09:30:57.988Z
1565	  Updated:    2026-05-17T02:56:26.471Z
1566	
1567	### plan_006_qwen3_8b_rsft_eval
1568	  Category:   eval
1569	  Status:     DONE
1570	  Conclusion: success
1571	  Parent:     plan_006_qwen3_8b_rsft_train_r2
1572	  ign_f1:     0.5433
1573	  f1: 0.5606
1574	  evi_f1: 0.8052
1575	  evi_f1_joint: 0.4413
1576	  edcr: 0.6377
1577	  precision: 0.5553
1578	  recall: 0.566
1579	  format_ok: 985/985
1580	  truncated: 267/985
1581	  predictions: 16831
1582	  Hypothesis: Evaluate Qwen3-8B RSFT (CED-scored data, 9041 samples) on DocRED dev. At 8B scale with near-zero evidence tax, CED-RSFT should achieve highest absolute Ign-F1 in the scaling study.
1583	  Created:    2026-05-17T12:00:05.493Z
1584	  Updated:    2026-05-17T14:59:23.644Z
1585	
1586	### plan_006_qwen3_8b_sft_eval
1587	  Category:   eval
1588	  Status:     DONE
1589	  Conclusion: success
1590	  Parent:     plan_006_qwen3_8b_sft_bf16
1591	  ign_f1:     0.5051
1592	  f1: 0.5262
1593	  evi_f1: 0.8188
1594	  edcr: 0.651
1595	  format_ok_rate: 0.999
1596	  n_truncated: 313
1597	  n_predictions: 17401
1598	  inference_time_s: 7206
1599	  Hypothesis: Qwen3-8B evidence-SFT eval under D076 unified protocol. Establishes 8B-scale SFT baseline for evidence tax measurement (paired with no-evidence eval) and RSFT improvement quantification.
1600	  Created:    2026-05-16T09:03:35.743Z
1601	  Updated:    2026-05-17T02:56:01.221Z
1602	
1603	### plan_007_redocred_4b_sft_eval
1604	  Category:   eval
1605	  Status:     DONE
1606	  Conclusion: failed
1607	  Parent:     (none)
1608	  Metrics:    (none)
1609	  Created:    2026-05-16T12:30:55.473Z
1610	  Updated:    2026-05-16T12:34:54.050Z
1611	
1612	### plan_007_redocred_4b_sft_eval_r2
1613	  Category:   eval
1614	  Status:     DONE
1615	  Conclusion: success
1616	  Parent:     reeval_sft_baseline_d076
1617	  ign_f1:     0.3659
1618	  f1: 0.3706
1619	  evi_f1: 0.817
1620	  edcr: 0.6674
1621	  format_compliance_rate: 0.996
1622	  n_truncated: 139
1623	  n_total: 493
1624	  inference_time_seconds: 3281.7
1625	  precision: 0.4316
1626	  recall: 0.3247
1627	  ign_precision: 0.4134
1628	  ign_recall: 0.3282
1629	  evi_precision: 0.8208
1630	  evi_recall: 0.8131
1631	  n_predictions: 8191
1632	  Hypothesis: FREIGE SFT model trained on DocRED transfers to Re-DocRED without re-training: if Ign-F1 drop <5pp and Evi-F1 maintains, the learned evidence grounding generalizes across annotation schemes.
1633	  Created:    2026-05-16T12:36:01.717Z
1634	  Updated:    2026-05-17T02:55:43.842Z
1635	
1636	### plan_007_redocred_rsft_eval
1637	  Category:   eval
1638	  Status:     DONE
1639	  Conclusion: failed
1640	  Parent:     (none)
1641	  failure_reason: OOM + pipeline bug: --model_path and --sft_adapter args in wrong order. RSFT LoRA merged to bare Qwen3-4B without SFT base, causing ontology collapse. Fix: match DocRED eval param ordering.
1642	  Created:    2026-05-16T14:23:56.999Z
1643	  Updated:    2026-05-16T17:49:00.578Z
1644	
1645	### plan_007_redocred_rsft_eval_r2
1646	  Category:   eval
1647	  Status:     DONE
1648	  Conclusion: negative
1649	  Parent:     (none)
1650	  F1: 0.0025
1651	  Ign-F1: 0.0026
1652	  Evi-F1: 0.8837
1653	  EDCR: 0.9978
1654	  format_ok: 489/493
1655	  truncated: 117/493
1656	  predictions: 8461
1657	  Hypothesis: CED-RSFT improvements on DocRED should transfer to Re-DocRED: RSFT model should outperform SFT baseline on Re-DocRED Ign-F1, demonstrating cross-dataset generalization of rejection sampling gains.
1658	  Created:    2026-05-16T16:25:37.094Z
1659	  Updated:    2026-05-17T02:56:32.555Z
1660	
1661	### plan_007_redocred_rsft_eval_r3
1662	  Category:   eval
1663	  Status:     DONE
1664	  Conclusion: failed
1665	  Parent:     plan_007_redocred_4b_sft_eval_r2
1666	  Metrics:    (none)
1667	  Hypothesis: Re-DocRED RSFT eval r3 (config fix: model_path=base, sft_adapter=RSFT ckpt). Verify CED-RSFT gains transfer cross-dataset.
1668	  Created:    2026-05-16T17:38:09.825Z
1669	  Updated:    2026-05-16T21:07:14.348Z
1670	
1671	### plan_007_redocred_rsft_eval_r4
1672	  Category:   eval
1673	  Status:     DONE
1674	  Conclusion: failed
1675	  Parent:     plan_007_redocred_4b_sft_eval_r2
1676	  Metrics:    (none)
1677	  Hypothesis: CED-RSFT gains transfer to Re-DocRED (r4, correct 3-param loading: base→SFT→RSFT)
1678	  Created:    2026-05-16T18:00:41.999Z
1679	  Updated:    2026-05-16T22:04:01.953Z
1680	
1681	### plan_007_redocred_rsft_eval_r5
1682	  Category:   eval
1683	  Status:     DONE
1684	  Conclusion: success
1685	  Parent:     plan_007_redocred_rsft_eval_r4
1686	  ign_f1:     0.4145
1687	  f1: 0.4234
1688	  evi_f1: 0.8182
1689	  edcr: 0.621
1690	  evi_joint_f1: 0.3306
1691	  format_compliance: 1
1692	  field_compliance: 0.8134
1693	  n_documents: 493
1694	  n_truncated: 90
1695	  inference_time_s: 5655.5
1696	  Hypothesis: CED-RSFT gains transfer to Re-DocRED (r5, correct 3-param loading: base→SFT→RSFT)
1697	  Created:    2026-05-16T22:04:18.834Z
1698	  Updated:    2026-05-17T00:51:25.706Z
1699	
1700	### plan_009_extract_reward_eval
1701	  Category:   eval
1702	  Status:     DONE
1703	  Conclusion: failed
1704	  Parent:     (none)
1705	  Metrics:    (none)
1706	  Created:    2026-05-15T19:04:55.707Z
1707	  Updated:    2026-05-15T19:58:37.870Z
1708	
1709	### plan_009_flatnli_reward_eval
1710	  Category:   eval
1711	  Status:     DONE
1712	  Conclusion: failed
1713	  Parent:     (none)
1714	  Metrics:    (none)
1715	  Created:    2026-05-15T19:04:57.991Z
1716	  Updated:    2026-05-15T19:39:02.187Z
1717	
1718	### plan_009_flatnli_reward_eval_r2
1719	  Category:   eval
1720	  Status:     DONE
1721	  Conclusion: failed
1722	  Parent:     (none)
1723	  Metrics:    (none)
1724	  Created:    2026-05-15T19:54:58.033Z
1725	  Updated:    2026-05-15T20:32:33.464Z
1726	
1727	### plan_011_bf16_g8_step_eval
1728	  Category:   eval
1729	  Status:     DONE
1730	  Conclusion: success
1731	  Parent:     (none)
1732	  step_30: {'rel_f1': 0.434, 'evi_f1': 0.8063, 'edcr': 0.6807}
1733	  step_50: {'rel_f1': 0.4276, 'evi_f1': 0.8024, 'edcr': 0.6855}
1734	  step_70: {'rel_f1': 0.4341, 'evi_f1': 0.8099, 'edcr': 0.6685}
1735	  best_step: step_70
1736	  trend: non-monotonic, all < ckpt-100 (0.4549)
1737	  Created:    2026-05-15T19:04:51.538Z
1738	  Updated:    2026-05-15T23:01:09.970Z
1739	
1740	### plan_011_eval_g8_bf16_ckpt100
1741	  Category:   eval
1742	  Status:     DONE
1743	  Conclusion: killed
1744	  Parent:     (none)
1745	  Metrics:    (none)
1746	  Created:    2026-05-15T14:43:24.143Z
1747	  Updated:    2026-05-15T22:06:28.981Z
1748	
1749	### plan_011_grpo_g8_bf16
1750	  Category:   grpo
1751	  Status:     DONE
1752	  Conclusion: success
1753	  Parent:     (none)
1754	  final_step: 100
1755	  train_runtime_s: 554
1756	  reward_final: 1.795
1757	  f1_reward_final: 1.002
1758	  ced_reward_final: 0.494
1759	  format_reward_final: 0.3
1760	  frac_zero_std_final: 0
1761	  kl_final: 0.022
1762	  best_reward_step: 85
1763	  best_reward: 2.858
1764	  best_f1_reward: 1.85
1765	  mode_collapse: False
1766	  lora_config: r=64, alpha=128, dropout=0.05, bf16
1767	  checkpoints: 10 checkpoints (step 10-100)
1768	  Hypothesis: GRPO G=8 bf16 LoRA: 验证 catastrophic forgetting 是否在 bf16（非 QLoRA 4-bit）下仍复现。CED reward + kl_coef=0.01, 100 steps。如仍 fail → 加强 Claim 3
1769	  Created:    2026-05-15T13:59:50.014Z
1770	  Updated:    2026-05-15T15:55:53.725Z
1771	
1772	### plan_011_grpo_g8_bf16_eval
1773	  Category:   eval, grpo
1774	  Status:     DONE
1775	  Conclusion: success
1776	  Parent:     (none)
1777	  ign_f1:     0.4549
1778	  rel_f1: 0.4549
1779	  evi_f1: 0.8086
1780	  edcr: 0.6318
1781	  format_ok_rate: 1
1782	  n_truncated: 61
1783	  n_total: 985
1784	  n_predictions: 10701
1785	  checkpoint: checkpoint-100
1786	  model: Qwen3-4B + SFT merged + GRPO bf16 LoRA ckpt-100
1787	  inference_time_s: 3170.3
1788	  Created:    2026-05-15T14:43:48.481Z
1789	  Updated:    2026-05-15T15:55:52.592Z
1790	
1791	### plan_014_no_evidence_eval_d076
1792	  Category:   eval, no_evidence
1793	  Status:     DONE
1794	  Conclusion: success
1795	  Parent:     plan_014_sft_no_evidence
1796	  ign_f1:     0.4721
1797	  f1: 0.4876
1798	  precision: 0.4901
1799	  recall: 0.4851
1800	  format_compliance_rate: 0.9929
1801	  n_truncated: 307
1802	  inference_time_seconds: 6903.9
1803	  Hypothesis: 4B no-evidence SFT eval under D076 unified protocol (batch_size=4, max_new_tokens=1024, seed=42, no-quantize). Required for clean scaling comparison across 1.7B/4B/8B.
1804	  Created:    2026-05-16T14:26:29.748Z
1805	  Updated:    2026-05-16T17:37:09.823Z
1806	
1807	### plan_014_sft_no_evidence
1808	  Category:   no_evidence
1809	  Status:     DONE
1810	  Conclusion: success
1811	  Parent:     (none)
1812	  train_loss: 0.7077
1813	  eval_loss: 0.8781
1814	  eval_token_accuracy: 0.8086
1815	  epochs: 3
1816	  total_steps: 570
1817	  train_runtime_min: 64
1818	  samples: 3027
1819	  trainable_params: 132M/4.15B (3.18%)
1820	  Hypothesis: SFT-without-evidence ablation: 训练只输出 relation triples（不含 evidence sentences）的 SFT 模型。量化 joint evidence generation 对 extraction 的代价（当前 rel_f1=0.4057 vs 只抽关系的 LMRC 60.7 的 gap 有多少来自 evidence 负担）。
1821	  Created:    2026-05-15T15:55:43.710Z
1822	  Updated:    2026-05-15T18:42:28.216Z
1823	
1824	### plan_015_grpo_g4_bf16
1825	  Category:   grpo
1826	  Status:     DONE
1827	  Conclusion: killed
1828	  Parent:     (none)
1829	  Metrics:    (none)
1830	  Hypothesis: bf16 LoRA GRPO clean control: 与原始 QLoRA GRPO 仅改 quantization（4-bit → bf16），保持 G=4, kl=0, CED reward 不变。验证 catastrophic forgetting 是否由 QLoRA quantization 导致。
1831	  Created:    2026-05-15T15:58:43.784Z
1832	  Updated:    2026-05-15T16:03:08.279Z
1833	
1834	### plan_015_grpo_g4_bf16_v2
1835	  Category:   grpo
1836	  Status:     DONE
1837	  Conclusion: killed
1838	  Parent:     plan_011_grpo_g8_bf16
1839	  Metrics:    (none)
1840	  Hypothesis: Robustness check: bf16 LoRA GRPO 在 G=4, kl=0, lr=5e-6 条件下是否也防止 catastrophic forgetting。非 single-variable ablation（kl/lr/G 均与 QLoRA 对照组不同）。D052 确认 plan_011 vs mvp2_grpo_ced_kl001_r4 已是 clean quantization ablation。
1841	  Created:    2026-05-15T16:06:43.308Z
1842	  Updated:    2026-05-15T16:54:42.310Z
1843	
1844	### plan_015_grpo_g4_bf16_v3
1845	  Category:   grpo
1846	  Status:     DONE
1847	  Conclusion: killed
1848	  Parent:     (none)
1849	  Metrics:    (none)
1850	  Hypothesis: P2 robustness check: bf16 LoRA GRPO G=4, kl=0.01, lr=5e-6。D052 确认 plan_011 vs mvp2_grpo_ced_kl001_r4 已是 clean single-variable quantization ablation (Δ=+23.8pp)。v3 仅为 robustness data point，lr=5e-6 与对照组 lr=5e-5 不一致。
1851	  Created:    2026-05-15T16:27:09.496Z
1852	  Updated:    2026-05-15T16:54:54.376Z
1853	
1854	### plan_016_llama_3_1_8b_no_evidence_eval
1855	  Category:   eval, no_evidence
1856	  Status:     DONE
1857	  Conclusion: success
1858	  Parent:     plan_016_llama_3_1_8b_no_evidence_sft
1859	  ign_f1:     0.5452
1860	  rel_f1: 0.5624
1861	  evi_f1: 0
1862	  edcr: 0
1863	  Hypothesis: LLaMA-3.1-8B no-evidence SFT should achieve similar rel_f1 to evidence-SFT (tax≈0), cross-family validating the 8B-scale evidence absorption pattern observed in Qwen3-8B.
1864	  Created:    2026-05-16T12:05:53.861Z
1865	  Updated:    2026-05-17T02:55:31.810Z
1866	
1867	### plan_016_llama_3_1_8b_no_evidence_sft
1868	  Category:   no_evidence
1869	  Status:     DONE
1870	  Conclusion: success
1871	  Parent:     (none)
1872	  Metrics:    (none)
1873	  Hypothesis: LLaMA-3.1-8B no-evidence SFT baseline for cross-family evidence tax measurement. Paired with evidence-SFT to quantify evidence generation cost on a non-Qwen architecture at 8B scale.
1874	  Created:    2026-05-16T11:06:47.006Z
1875	  Updated:    2026-05-17T02:55:47.936Z
1876	
1877	### plan_016_llama_3_1_8b_sft_eval
1878	  Category:   eval
1879	  Status:     DONE
1880	  Conclusion: success
1881	  Parent:     plan_016_llama_3_1_8b_sft
1882	  ign_f1:     0.5384
1883	  rel_f1: 0.5514
1884	  evi_f1: 0.8151
1885	  edcr: 0.628
1886	  precision: 0.5464
1887	  recall: 0.5565
1888	  evi_f1_joint: 0.4317
1889	  format_compliance_rate: 0.9949
1890	  n_truncated: 197
1891	  n_predictions: 15325
1892	  inference_time_seconds: 7331.3
1893	  evidence_tax_ign_f1: 0.0068
1894	  evidence_tax_rel_f1: 0.011
1895	  Hypothesis: LLaMA-3.1-8B SFT with evidence generation should achieve comparable rel_f1 to Qwen3-8B SFT, establishing cross-family baseline for evidence tax measurement. Evidence tax at 8B scale predicted near-zero based on Qwen3-8B pattern.
1896	  Created:    2026-05-16T12:06:49.282Z
1897	  Updated:    2026-05-17T02:55:20.475Z
1898	
1899	### plan_016_llama_grpo_qlora
1900	  Category:   grpo
1901	  Status:     DONE
1902	  Conclusion: success
1903	  Parent:     mvp2_grpo_ced_lr5e6_r1
1904	  format_reward: 1
1905	  f1_reward: 0
1906	  ced_reward: 0
1907	  entropy: 0.28
1908	  final_step: 60
1909	  grad_norm: 0
1910	  loss: 0
1911	  frac_reward_zero_std: 1
1912	  output_length_final: 172
1913	  conclusion_note: C2 cross-family validated: LLaMA QLoRA GRPO shows same catastrophic decoupling as Qwen (format gaming, zero IE ability)
1914	  Hypothesis: QLoRA GRPO catastrophic decoupling (format gaming + zero IE ability) is not Qwen-specific: LLaMA-3.1-8B under identical QLoRA GRPO training should exhibit the same failure mode (grad_norm→0, loss→0, rel_f1→0). Cross-family validation of C2.
1915	  Created:    2026-05-16T13:14:37.199Z
1916	  Updated:    2026-05-17T02:55:08.871Z
1917	
1918	### random_rsft_k1_baseline
1919	  Category:   random_rsft
1920	  Status:     DONE
1921	  Conclusion: success
1922	  Parent:     (none)
1923	  train_loss: 0.578
1924	  mean_token_accuracy: 0.8552
1925	  global_steps: 1020
1926	  epochs: 3
1927	  Hypothesis: Random k=1 RSFT baseline: same candidate pool as CED RSFT but random selection instead of CED scoring. If random RSFT significantly underperforms CED RSFT (rel_f1 gap > 1.5pp), proves CED scoring precision is the key, not just data filtering quantity. CED k=1 mean rel_f1=0.4596, expect random < 0.44...
1928	  Created:    2026-05-18T13:32:46.287Z
1929	  Updated:    2026-05-18T22:23:06.386Z
1930	
1931	### random_rsft_k1_eval
1932	  Category:   eval, random_rsft
1933	  Status:     DONE
1934	  Conclusion: success
1935	  Parent:     random_rsft_k1_baseline
1936	  ign_f1:     0.4114
1937	  f1: 0.4198
1938	  evi_f1: 0.7964
1939	  evi_f1_joint: 0.3216
1940	  EDCR: 0.6971
1941	  format_compliance: 0.999
1942	  field_compliance: 0.7482
1943	  truncated: 235
1944	  n_total: 985
1945	  n_predictions: 16110
1946	  inference_time_seconds: 11778.5
1947	  Hypothesis: Random k=1 RSFT eval: if random selection significantly underperforms CED RSFT (gap > 1.5pp in rel_f1), proves CED scoring precision is the key differentiator. CED k=1 mean rel_f1=0.4596, expect random &lt; 0.445.
1948	  Created:    2026-05-18T16:34:48.815Z
1949	  Updated:    2026-05-18T20:08:52.336Z
1950	
1951	### reeval_ced_s42
1952	  Category:   eval
1953	  Status:     DONE
1954	  Conclusion: success
1955	  Parent:     mvp2_rsft_train_r1
1956	  ign_f1:     0.4423
1957	  rel_f1: 0.4517
1958	  evi_f1: 0.8175
1959	  evi_f1_joint: 0.3518
1960	  edcr: 0.6569
1961	  format_compliance_rate: 1
1962	  field_compliance_rate: 0.7756
1963	  n_truncated: 214
1964	  inference_time_seconds: 10815.5
1965	  Hypothesis: Re-eval CED RSFT s42 with unified protocol: batch_size=4 + --no-quantize + --sft_adapter + max_new_tokens=1024. 原 mvp2_eval_rsft_r2b_maxtok1536_r2 用了 batch_size=8 + max_new_tokens=1536。Paired t-test 关键路径。
1966	  Created:    2026-05-16T02:37:58.498Z
1967	  Updated:    2026-05-16T10:14:00.520Z
1968	
1969	### reeval_ced_s44
1970	  Category:   eval
1971	  Status:     DONE
1972	  Conclusion: success
1973	  Parent:     mvp2_rsft_train_r1_s44
1974	  ign_f1:     0.4511
1975	  rel_f1: 0.4621
1976	  evi_f1: 0.805
1977	  evi_f1_joint: 0.3677
1978	  edcr: 0.635
1979	  format_compliance_rate: 1
1980	  field_compliance_rate: 0.802
1981	  n_truncated: 190
1982	  inference_time_seconds: 13077.6
1983	  Hypothesis: Re-eval CED RSFT s44 with unified protocol: batch_size=4 + --no-quantize + --sft_adapter + max_new_tokens=1024 + seed=44. 原 eval 用了 batch_size≈16 且 seed=42（错误）。Paired t-test 关键路径。
1984	  Created:    2026-05-16T02:38:00.052Z
1985	  Updated:    2026-05-16T10:14:02.479Z
1986	
1987	### reeval_flat_nli_s42
1988	  Category:   eval
1989	  Status:     DONE
1990	  Conclusion: success
1991	  Parent:     plan_001_rsft_flat_nli
1992	  ign_f1:     0.4448
1993	  rel_f1: 0.4535
1994	  evi_f1: 0.8039
1995	  evi_f1_joint: 0.3558
1996	  edcr: 0.6458
1997	  format_compliance_rate: 1
1998	  field_compliance_rate: 0.7787
1999	  n_truncated: 205
2000	  inference_time_seconds: 13253.1
2001	  Hypothesis: Re-eval flat-NLI RSFT s42 with unified protocol: batch_size=4 + --no-quantize + --sft_adapter + max_new_tokens=1024. 原 eval_plan_001_flat_nli 用了 batch_size=16。Paired t-test 关键路径。
2002	  Created:    2026-05-16T02:38:03.120Z
2003	  Updated:    2026-05-16T10:14:04.270Z
2004	
2005	### reeval_flat_nli_s43
2006	  Category:   eval
2007	  Status:     DONE
2008	  Conclusion: success
2009	  Parent:     plan_001_flat_nli_seed43
2010	  ign_f1:     0.4523
2011	  rel_f1: 0.4523
2012	  evi_f1: 0.8158
2013	  edcr: 0.6505
2014	  num_preds: 15357
2015	  format_ok: 984/985
2016	  truncated: 211/985
2017	  inference_time_s: 3515.8
2018	  Hypothesis: Re-eval flat-NLI RSFT seed=43 WITH --sft_adapter (D064 bug fix). 原 eval_plan_001_flat_nli_s43 因缺 --sft_adapter 导致 rel_f1=0.0022 无效。对比 flat-NLI s42 (rel_f1=0.4539) 和 CED RSFT mean (0.4596)。
2019	  Created:    2026-05-15T22:00:33.691Z
2020	  Updated:    2026-05-15T23:59:33.440Z
2021	
2022	### reeval_flat_nli_s43_r2
2023	  Category:   eval
2024	  Status:     DONE
2025	  Conclusion: success
2026	  Parent:     (none)
2027	  ign_f1:     0.4503
2028	  rel_f1: 0.4586
2029	  rel_precision: 0.4732
2030	  rel_recall: 0.4449
2031	  evi_f1: 0.8113
2032	  evi_precision: 0.8035
2033	  evi_recall: 0.8192
2034	  evi_f1_joint: 0.358
2035	  edcr: 0.6552
2036	  format_ok_rate: 0.999
2037	  n_truncated: 184
2038	  n_predictions: 15015
2039	  Hypothesis: Re-eval flat-NLI RSFT s43 with unified protocol: batch_size=4 + --no-quantize + --sft_adapter + --max_new_tokens 1024. 原 reeval_flat_nli_s43 用了 batch_size=16 导致协议不一致。C3 paired t-test 关键路径。
2040	  Created:    2026-05-16T02:32:45.507Z
2041	  Updated:    2026-05-16T06:10:14.112Z
2042	
2043	### reeval_flat_nli_s44
2044	  Category:   eval
2045	  Status:     DONE
2046	  Conclusion: killed
2047	  Parent:     (none)
2048	  Metrics:    (none)
2049	  Created:    2026-05-16T08:56:36.565Z
2050	  Updated:    2026-05-16T09:26:04.920Z
2051	
2052	### reeval_rsft_topk3
2053	  Category:   eval
2054	  Status:     DONE
2055	  Conclusion: negative
2056	  Parent:     plan_008_rsft_topk3
2057	  ign_f1:     0.4364
2058	  rel_f1: 0.4454
2059	  rel_precision: 0.4512
2060	  rel_recall: 0.4398
2061	  evi_f1: 0.8088
2062	  edcr: 0.6635
2063	  format_ok_rate: 0.999
2064	  n_truncated: 214
2065	  n_predictions: 16020
2066	  inference_time_seconds: 3546.4
2067	  ign_f1_corrected: True
2068	  Hypothesis: Re-eval RSFT top_k=3 WITH --sft_adapter (D064 bug fix). 原 eval_plan_008_rsft_topk3 因缺 --sft_adapter 被 killed。对比 CED RSFT top_k=1 (rel_f1≈0.46) 和 SFT baseline (0.4057)。
2069	  Created:    2026-05-15T22:00:34.722Z
2070	  Updated:    2026-05-16T00:24:22.091Z
2071	
2072	### reeval_sft_baseline_d076
2073	  Category:   eval
2074	  Status:     DONE
2075	  Conclusion: success
2076	  Parent:     (none)
2077	  ign_f1:     0.3974
2078	  rel_f1: 0.4049
2079	  evi_f1: 0.7986
2080	  edcr: 0.6982
2081	  evi_f1_joint: 0.3147
2082	  format_compliance_rate: 0.998
2083	  n_truncated: 288
2084	  n_documents: 985
2085	  n_predictions: 16880
2086	  inference_time_sec: 7056.5
2087	  Hypothesis: Re-eval Qwen3-4B SFT baseline under D076 unified protocol (batch_size=4, no-quantize, max_new_tokens=1024, seed=42). Required as canonical comparison point for all RSFT/GRPO experiments and evidence tax computation.
2088	  Created:    2026-05-16T05:26:37.542Z
2089	  Updated:    2026-05-17T02:56:09.813Z
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19574c01-8ebb-4fd7-b6e2-a410b9c06595",
  "isSidechain": true,
  "promptId": "b133d549-2594-4f9e-b048-83b487db8d11",
  "agentId": "a01ea92613c0e609d",
  "type": "user",
  "uuid": "ac6c13b3-abc5-4f8e-9bcf-9b6da096302c",
  "sourceToolAssistantUUID": "19574c01-8ebb-4fd7-b6e2-a410b9c06595",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T12:41:22.347Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q5oGp6wTAWffJdE7X2bUQh`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt",
  "offset": 2089,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac6c13b3-abc5-4f8e-9bcf-9b6da096302c",
  "isSidechain": true,
  "agentId": "a01ea92613c0e609d",
  "requestId": "req_011CbBwjYpujSTi4cVjq8Zht",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e0b48da-f7ae-4a7d-a708-36999949d361",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015idruownRxTLhywMoqWvyS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10924,
      "cache_read_input_tokens": 47397,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10924
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 47397,
          "cache_creation_input_tokens": 10924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10924,
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

_source line 25 · 2026-05-19T12:41:22.356Z_

<details><summary>↩ Tool result · `toolu_01Q5oGp6wTAWffJdE7X2bUQh`</summary>

```text
2089	  Updated:    2026-05-17T02:56:09.813Z
2090	
2091	### rsft_s43_dev_eval_preds
2092	  Category:   eval
2093	  Status:     DONE
2094	  Conclusion: success
2095	  Parent:     (none)
2096	  ign_f1:     0.4512
2097	  f1: 0.4601
2098	  evi_f1: 0.8063
2099	  edcr: 0.6542
2100	  evi_f1_joint: 0.3605
2101	  format_compliance_rate: 1
2102	  field_compliance_rate: 0.809
2103	  n_truncated: 184
2104	  inference_time_seconds: 10982
2105	  Hypothesis: Eval RSFT-s43 (CED-scored) on DocRED dev with predictions saved. Prerequisite for Lead 1 CED evidence filtering: per-sentence NLI scoring requires full prediction outputs.
2106	  Created:    2026-05-17T08:35:42.135Z
2107	  Updated:    2026-05-17T23:18:03.147Z
2108	
2109	### rsft_s44_dev_eval_preds
2110	  Category:   eval
2111	  Status:     DONE
2112	  Conclusion: failed
2113	  Parent:     (none)
2114	  Metrics:    (none)
2115	  Hypothesis: Re-run RSFT s44 dev eval with predictions saved, as prerequisite for CED evidence filtering experiment (线索1: inference-time distractor citation removal). Predictions needed for per-sentence NLI scoring.
2116	  Created:    2026-05-17T05:02:50.832Z
2117	  Updated:    2026-05-17T08:25:22.846Z
2118	
2119	### seed_llama_rsft_k1_s43_eval
2120	  Category:   eval
2121	  Status:     DONE
2122	  Conclusion: success
2123	  Parent:     rsft_llama_k1_s43_train
2124	  Metrics:    (none)
2125	  Hypothesis: LLaMA-8B RSFT k=1 seed43 eval: paired with s42 (rel_f1=0.5839) for seed robustness. If s43 gives similar results (±1.5pp), cross-architecture RSFT k=1 claim is robust. Expected rel_f1 ~0.58±0.015.
2126	  Created:    2026-05-18T13:30:51.665Z
2127	  Updated:    2026-05-18T15:22:14.518Z
2128	
2129	### smoke_test_grpo
2130	  Category:   grpo
2131	  Status:     DONE
2132	  Conclusion: success
2133	  Parent:     (none)
2134	  Metrics:    (none)
2135	  Created:    2026-05-14T05:20:00.970Z
2136	  Updated:    2026-05-14T06:09:18.626Z
2137	
2138	### wave1_grpo_bf16_g4
2139	  Category:   grpo
2140	  Status:     DONE
2141	  Conclusion: success
2142	  Parent:     (none)
2143	  reward_mean: 1.7646
2144	  steps_completed: 200
2145	  max_steps: 200
2146	  Hypothesis: GRPO bf16 without quantization (G=4): prior GRPO runs used int4 quantization which may have caused training instability. bf16 full precision should provide clean GRPO signal. If GRPO improves over RSFT, validates Claim 2 (decoupling spectrum). Expected: rel_f1 > RSFT baseline (~52pp).
2147	  Created:    2026-05-18T12:46:19.740Z
2148	  Updated:    2026-05-18T20:09:28.981Z
2149	
2150	### wave1_sft_4b_s43_eval
2151	  Category:   eval
2152	  Status:     DONE
2153	  Conclusion: failed
2154	  Parent:     wave1_sft_4b_s43
2155	  Metrics:    (none)
2156	  Hypothesis: SFT 4B seed43 eval (D076 protocol): baseline SFT performance for seed43. Paired with s44 for mean±std. Expected rel_f1 ~50.5 based on prior 4B SFT s42 results.
2157	  Created:    2026-05-18T14:01:42.261Z
2158	  Updated:    2026-05-18T15:43:30.104Z
2159	
2160	### wave1_sft_4b_s43_eval_r2
2161	  Category:   eval
2162	  Status:     DONE
2163	  Conclusion: success
2164	  Parent:     (none)
2165	  ign_f1:     0.4365
2166	  rel_f1: 0.4429
2167	  evi_f1_joint: 0.3462
2168	  evi_f1_tp: 0.8021
2169	  edcr: 0.6827
2170	  format_compliance_rate: 1
2171	  n_truncated: 318
2172	  n_predictions: 17055
2173	  inference_time_seconds: 7157.9
2174	  Hypothesis: 4B SFT seed43 eval r2 (corrected D076 command: --model_path=base --sft_adapter=adapter). Re-run of failed wave1_sft_4b_s43_eval. Expected rel_f1 ~50.5 based on canonical 4B SFT s42.
2175	  Created:    2026-05-18T19:29:28.052Z
2176	  Updated:    2026-05-18T21:34:25.964Z
2177	
2178	### wave1_sft_4b_s44_eval
2179	  Category:   eval
2180	  Status:     DONE
2181	  Conclusion: failed
2182	  Parent:     wave1_sft_4b_s44
2183	  Metrics:    (none)
2184	  Hypothesis: SFT 4B seed44 eval (D076 protocol): baseline SFT performance for seed44. Paired with s43 for mean±std. Expected rel_f1 ~50.5 based on prior 4B SFT s42 results.
2185	  Created:    2026-05-18T14:01:43.597Z
2186	  Updated:    2026-05-18T15:43:33.593Z
2187	
2188	### wave1_sft_4b_s44_eval_r2
2189	  Category:   eval
2190	  Status:     DONE
2191	  Conclusion: success
2192	  Parent:     wave1_sft_4b_s44
2193	  ign_f1:     0.4734
2194	  f1: 0.4838
2195	  ign_precision: 0.4676
2196	  ign_recall: 0.4794
2197	  precision: 0.4898
2198	  recall: 0.478
2199	  evi_f1_joint: 0.382
2200	  evi_f1_tp: 0.7875
2201	  edcr: 0.6581
2202	  format_ok_rate: 0.997
2203	  n_truncated: 249
2204	  n_documents: 985
2205	  n_predictions: 16143
2206	  inference_time_seconds: 6669.5
2207	  Hypothesis: 4B SFT seed44 eval r2 (corrected D076 command: --model_path=base --sft_adapter=adapter). Re-run of failed wave1_sft_4b_s44_eval. Expected rel_f1 ~50.5 based on canonical 4B SFT s42.
2208	  Created:    2026-05-18T20:05:57.119Z
2209	  Updated:    2026-05-18T22:20:06.715Z
2210	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e0b48da-f7ae-4a7d-a708-36999949d361",
  "isSidechain": true,
  "promptId": "b133d549-2594-4f9e-b048-83b487db8d11",
  "agentId": "a01ea92613c0e609d",
  "type": "user",
  "uuid": "a1cd4c25-0779-483a-8864-3f8f3f3857b0",
  "sourceToolAssistantUUID": "5e0b48da-f7ae-4a7d-a708-36999949d361",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-19T12:43:03.969Z_

All data extracted. Now let me compile a clean structured output.

Here is the complete extraction of all 149 matching experiments, organized by category.

---

## EVAL experiments (with "eval" in name)

### SFT Baselines

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| mvp2_sft_eval | DONE | killed | - | - | - | - | |
| mvp2_sft_eval_r2 | DONE | success | 0.4057 | 0.4057 | 0.7979 | 0.7118 | |
| mvp2_sft_eval_r3 | DONE | success | 0.4057 | 0.4057 | 0.7979 | 0.7118 | |
| mvp2_eval_sft_baseline | DONE | success | - | 0.4057 | 0.7979 | 0.7118 | evi_f1_joint=0.3117 |
| eval_sft_baseline_noquant | DONE | success | - | 0.4106 | 0.8013 | 0.7039 | |
| reeval_sft_baseline_d076 | DONE | success | 0.3974 | 0.4049 | 0.7986 | 0.6982 | D076 protocol |
| d111_4b_sft_s42_reeval | DONE | success | 0.3974 | 0.4049 | 0.7986 | 0.6982 | D076 standardized |
| wave1_sft_4b_s43_eval | DONE | failed | - | - | - | - | |
| wave1_sft_4b_s43_eval_r2 | DONE | success | 0.4365 | 0.4429 | - | 0.6827 | evi_f1_tp=0.8021 |
| wave1_sft_4b_s44_eval | DONE | failed | - | - | - | - | |
| wave1_sft_4b_s44_eval_r2 | DONE | success | 0.4734 | - | - | 0.6581 | f1=0.4838, evi_f1_tp=0.7875 |

### 1.7B Scale SFT Evals

| experiment_id | status | conclusion | ign_f1 | f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| plan_006_qwen3_1_7b_sft_eval | DONE | success | 0.4786 | 0.4945 | 0.8316 | 0.6704 | D076 protocol |
| plan019_1_7b_sft_s43_eval | DONE | success | 0.4286 | 0.4372 | 0.835 | 0.704 | |
| plan019_1_7b_sft_s44_eval | DONE | success | 0.4321 | 0.4441 | - | 0.69 | evi_f1_tp=0.819 |

### 8B Scale SFT Evals

| experiment_id | status | conclusion | ign_f1 | f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| plan_006_qwen3_8b_sft_eval | DONE | success | 0.5051 | 0.5262 | 0.8188 | 0.651 | D076 protocol |
| plan019_8b_sft_s44_eval | DONE | success | 0.4681 | 0.4841 | 0.8361 | 0.6697 | |
| plan_016_llama_3_1_8b_sft_eval | DONE | success | 0.5384 | - | 0.8151 | 0.628 | rel_f1=0.5514, evidence_tax=0.011 |

### 14B SFT Eval

| experiment_id | status | conclusion | ign_f1 | notes |
|---|---|---|---|---|
| plan017_14b_sft_eval | DONE | killed | - | |

### CED RSFT Evals (4B)

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | evi_f1_joint | notes |
|---|---|---|---|---|---|---|---|---|
| mvp2_eval_rsft_r1 | DONE | success | - | 0.4449 | 0.8187 | 0.6565 | 0.3468 | seed=42 |
| mvp2_eval_rsft_r2a | DONE | success | 0.4494 | 0.4494 | 0.8108 | 0.6641 | 0.3509 | 1ep, alpha=128 |
| mvp2_eval_rsft_r2b | DONE | success | 0.4493 | 0.4493 | 0.8128 | 0.6609 | 0.349 | 1ep, alpha=32, lr=1e-5 |
| mvp2_eval_rsft_r2b_maxtok1536 | DONE | killed | - | - | - | - | - | truncation diagnosis |
| mvp2_eval_rsft_r2b_maxtok1536_r2 | DONE | negative | 0.4504 | 0.4504 | 0.8102 | 0.674 | - | EDCR improved marginally |
| mvp2_eval_rsft_s43 | DONE | failed | - | - | - | - | - | |
| mvp2_eval_rsft_s43_r2 | DONE | success | 0.4683 | 0.4683 | 0.8156 | 0.6388 | 0.3711 | mvp2_pass=True |
| mvp2_eval_rsft_s44 | DONE | killed | - | - | - | - | - | |
| reeval_ced_s42 | DONE | success | 0.4423 | 0.4517 | 0.8175 | 0.6569 | 0.3518 | D076 unified protocol |
| reeval_ced_s44 | DONE | success | 0.4511 | 0.4621 | 0.805 | 0.635 | 0.3677 | D076 unified protocol |
| eval_rsft_ced_s43 | DONE | success | 0.4512 | 0.4601 | 0.8063 | 0.6542 | 0.3605 | |
| eval_rsft_ced_s45 | DONE | success | 0.4416 | 0.4514 | 0.8174 | 0.655 | 0.3558 | |
| d112_rsft_s44_eval | DONE | failed | 0.2181 | - | - | - | - | INVALID: QLoRA confound |
| rsft_s43_dev_eval_preds | DONE | success | 0.4512 | - | 0.8063 | 0.6542 | 0.3605 | f1=0.4601 |
| rsft_s44_dev_eval_preds | DONE | failed | - | - | - | - | - | |

### Flat-NLI RSFT Evals

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | evi_f1_joint | notes |
|---|---|---|---|---|---|---|---|---|
| eval_plan_001_flat_nli | DONE | success | 0.4539 | 0.4539 | 0.8043 | 0.6431 | - | seed=42 |
| eval_flat_nli_s44 | DONE | success | 0.452126 | - | 0.813123 | 0.6458 | 0.3597 | |
| eval_flat_nli_seed44 | DONE | killed | - | - | - | - | - | |
| eval_flat_nli_seed45 | DONE | success | 0.446181 | - | 0.815399 | 0.6521 | 0.3556 | |
| eval_plan_001_flat_nli_s43 | DONE | failed | 0.0022 | 0.0022 | 0.8533 | 0.9982 | - | INVALID: missing --sft_adapter |
| reeval_flat_nli_s42 | DONE | success | 0.4448 | 0.4535 | 0.8039 | 0.6458 | 0.3558 | D076 unified |
| reeval_flat_nli_s43 | DONE | success | 0.4523 | 0.4523 | 0.8158 | 0.6505 | - | |
| reeval_flat_nli_s43_r2 | DONE | success | 0.4503 | 0.4586 | 0.8113 | 0.6552 | 0.358 | D076 unified |
| reeval_flat_nli_s44 | DONE | killed | - | - | - | - | - | |

### RSFT top_k=3 Evals

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| eval_plan_008_rsft_topk3 | DONE | killed | - | - | - | - | INVALID: missing --sft_adapter |
| eval_plan_008_topk3_fixed | DONE | killed | - | - | - | - | |
| reeval_rsft_topk3 | DONE | negative | 0.4364 | 0.4454 | 0.8088 | 0.6635 | top_k=3 underperforms k=1 |

### DPO Evals

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| eval_plan_012_dpo_ced_ckpt400 | DONE | failed | - | - | - | - | |
| eval_plan_012_dpo_ced_1ep | DONE | negative | 0.0022 | 0.0022 | 0.75 | 0.9982 | |
| eval_plan_012_dpo_1ep_fixed | DONE | killed | - | - | - | - | |
| eval_plan_012_dpo_1ep_fixed_r2 | DONE | negative | 0.4034 | 0.4034 | 0.8088 | 0.7139 | DPO 1ep matches SFT baseline, delta=-0.0023 |

### 1.7B RSFT Evals

| experiment_id | status | conclusion | ign_f1 | f1 | evi_f1 | edcr | evi_f1_joint | notes |
|---|---|---|---|---|---|---|---|---|
| plan_006_qwen3_1_7b_rsft_eval | DONE | failed | - | - | - | - | - | |
| plan_006_qwen3_1_7b_rsft_eval_r2 | DONE | success | 0.505 | 0.5219 | 0.8309 | 0.6297 | 0.4223 | seed=42 |
| plan_006_qwen3_1_7b_rsft_seed43_eval | DONE | success | 0.5024 | 0.518 | - | 0.6246 | 0.4201 | evi_f1_tp=0.8341 |
| plan019_1_7b_rsft_s43_r2_eval | DONE | success | 0.5109 | - | 0.8278 | 0.6245 | 0.4278 | f1=0.5271 |
| plan019_1_7b_rsft_s44_r2_eval | DONE | success | 0.5125 | - | 0.8267 | 0.6181 | 0.4289 | f1=0.5294 |
| plan006_1_7b_rsft_eval | DONE | killed | - | - | - | - | - | |

### 8B RSFT Evals

| experiment_id | status | conclusion | ign_f1 | f1 | evi_f1 | edcr | evi_f1_joint | notes |
|---|---|---|---|---|---|---|---|---|
| plan_006_qwen3_8b_rsft_eval | DONE | success | 0.5433 | 0.5606 | 0.8052 | 0.6377 | 0.4413 | |
| plan019_8b_rsft_s44_eval | DONE | success | 0.5451 | 0.562 | - | 0.6233 | - | evi_f1_tp=0.8145, evi_f1_dreeam=0.4472 |

### LLaMA-8B RSFT Evals

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | evi_f1_joint | notes |
|---|---|---|---|---|---|---|---|---|
| plan_006_llama_rsft_r3_eval | DONE | success | 0.5563 | - | 0.8255 | 0.5856 | 0.4571 | f1=0.5674 |
| plan_006_llama_rsft_seed43_eval | DONE | failed | - | - | - | - | - | |
| plan_006_llama_rsft_seed43_eval_r2 | DONE | success | 0.5619 | 0.5727 | 0.8206 | 0.6073 | 0.4551 | |
| d102_llama_rsft_k1_s43_eval | DONE | killed | - | - | - | - | - | |
| seed_llama_rsft_k1_s43_eval | DONE | success | - | - | - | - | - | (no metrics reported) |

### GRPO QLoRA Evals (catastrophic forgetting trajectory)

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| mvp2_eval_ced_kl001_r4_early | DONE | negative | 0.1563 | 0.1563 | 0.5643 | 0.8858 | |
| mvp2_eval_ced_kl001_r4 | DONE | success | - | 0.00296 | 0.72 | 0.9983 | ckpt-10 |
| mvp2_eval_ced_kl001_r4_step90 | DONE | negative | 0.2108 | 0.2108 | 0.5666 | 0.8584 | |
| mvp2_eval_ced_kl001_r4_step100 | DONE | negative | 0.2167 | 0.2167 | 0.5746 | 0.8539 | |
| mvp2_eval_ced_kl001_r4_high | DONE | failed | - | - | - | - | ckpt-60: rel_f1=0.1467. OOM during ckpt-70 |
| mvp2_eval_ced_kl001_r4_ckpt7080 | DONE | failed | - | - | - | - | OOM |
| mvp2_eval_ced_kl001_r4_ckpt90 | DONE | killed | - | - | - | - | |
| mvp2_eval_ced_kl001_r4_last | DONE | killed | - | - | - | - | |
| mvp2_eval_ced_kl001_r4_multi | DONE | killed | - | - | - | - | Multi-ckpt trajectory: ckpt-10=0.003, ckpt-20=0.0088, ckpt-30=0.0338, ckpt-50=0.1563, ckpt-60=0.1467, ckpt-90=0.2108 |

### GRPO lr=5e-6 Evals (still catastrophic)

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| mvp2_eval_lr5e6_r1_ckpt20 | DONE | negative | - | 0.0077 | 0.628 | 0.993 | |
| mvp2_eval_lr5e6_r1_ckpt40 | DONE | failed | - | - | - | - | |
| mvp2_eval_lr5e6_r1_ckpt40_r2 | DONE | negative | - | 0.0071 | 0.7584 | 0.9942 | |
| mvp2_eval_lr5e6_r1_ckpt60 | DONE | failed | - | - | - | - | |
| mvp2_eval_lr5e6_r1_ckpt60_r2 | DONE | negative | - | 0.0093 | 0.81 | 0.993 | |
| mvp2_eval_lr5e6_r1_ckpt80 | DONE | negative | 0.0116 | 0.0116 | 0.828 | 0.993 | |
| mvp2_eval_lr5e6_r1_ckpt100 | DONE | negative | 0.0138 | 0.0138 | 0.8504 | 0.9876 | |
| mvp2_eval_lr5e6_rp_r2_ckpt20 | DONE | killed | - | - | - | - | recall_penalty variant, killed |

### GRPO bf16 Evals (forgetting fixed)

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| eval_grpo_g8_bf16 | DONE | success | - | - | - | - | ckpt80: 0.4456, ckpt90: 0.4523, ckpt100: 0.4549. Best=ckpt-100 |
| plan_011_grpo_g8_bf16_eval | DONE | success | 0.4549 | 0.4549 | 0.8086 | 0.6318 | ckpt-100 |
| plan_011_bf16_g8_step_eval | DONE | success | - | - | - | - | step_30=0.434, step_50=0.4276, step_70=0.4341 |
| plan_011_eval_g8_bf16_ckpt100 | DONE | killed | - | - | - | - | |
| grpo_bf16_g4_ckpt100_eval | DONE | success | 0.4431 | - | 0.801 | 0.6453 | f1=0.4511 |
| grpo_bf16_g4_ckpt200_eval | DONE | success | 0.4446 | 0.4513 | 0.8053 | 0.6489 | |

### RSFT->GRPO (Lead2) Eval

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | evi_f1_joint | notes |
|---|---|---|---|---|---|---|---|---|
| lead2_ckpt20_eval | DONE | success | 0.4533 | 0.4617 | 0.8103 | 0.6465 | 0.3642 | Preserves RSFT baseline |

### Re-DocRED Transfer Evals

| experiment_id | status | conclusion | ign_f1 | f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| plan_007_redocred_4b_sft_eval | DONE | failed | - | - | - | - | |
| plan_007_redocred_4b_sft_eval_r2 | DONE | success | 0.3659 | 0.3706 | 0.817 | 0.6674 | |
| plan_007_redocred_rsft_eval | DONE | failed | - | - | - | - | OOM + pipeline bug |
| plan_007_redocred_rsft_eval_r2 | DONE | negative | 0.0026 | - | 0.8837 | 0.9978 | Wrong model loading |
| plan_007_redocred_rsft_eval_r3 | DONE | failed | - | - | - | - | |
| plan_007_redocred_rsft_eval_r4 | DONE | failed | - | - | - | - | |
| plan_007_redocred_rsft_eval_r5 | DONE | success | 0.4145 | 0.4234 | 0.8182 | 0.621 | Correct 3-param loading |

### Test Set Eval

| experiment_id | status | conclusion | notes |
|---|---|---|---|
| plan_002_test_eval_s44 | DONE | failed | |
| plan_002_test_eval_s44_r2 | DONE | success | No metrics in registry (test set for paper) |

### Reward Variant Evals

| experiment_id | status | conclusion | notes |
|---|---|---|---|
| plan_009_extract_reward_eval | DONE | failed | |
| plan_009_flatnli_reward_eval | DONE | failed | |
| plan_009_flatnli_reward_eval_r2 | DONE | failed | |

---

## NO_EVIDENCE experiments

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | notes |
|---|---|---|---|---|---|---|
| eval_plan_014_no_evidence | DONE | failed | - | - | - | |
| eval_plan_014_no_evidence_r2 | DONE | success | 0.4721 | 0.4876 | 0 | 4B no-evi |
| eval_plan_014_sft_no_evidence | DONE | success | - | 0.4893 | 0 | rel_ign_f1=0.4893 |
| plan_014_no_evidence_eval_d076 | DONE | success | 0.4721 | - | - | D076 protocol |
| plan017_14b_sft_no_evidence_eval | DONE | killed | - | - | - | 14B |
| plan_006_qwen3_1_7b_no_evidence_eval | DONE | failed | 0.3786 | - | 0.0007 | 1.7B (wrong eval) |
| plan_006_qwen3_1_7b_no_evidence_eval_v2 | DONE | failed | - | - | - | |
| plan_006_qwen3_1_7b_no_evidence_eval_v2r2 | DONE | failed | - | - | - | |
| plan_006_qwen3_1_7b_no_evidence_eval_v3 | DONE | success | 0.3982 | 0.4103 | 0 | evidence_tax=0.0804 |
| plan_006_qwen3_8b_no_evidence_eval | DONE | killed | - | - | - | |
| plan_006_qwen3_8b_no_evidence_eval_v2 | DONE | success | - | - | - | (no metrics in registry) |
| plan_016_llama_3_1_8b_no_evidence_eval | DONE | success | 0.5452 | 0.5624 | 0 | LLaMA 8B |
| plan_006_qwen3_1_7b_no_evidence_sft | DONE | success | - | - | - | Training only |
| plan_006_qwen3_8b_no_evidence_sft | DONE | success | - | - | - | Training only |
| plan_014_sft_no_evidence | DONE | success | - | - | - | Training only |
| plan_016_llama_3_1_8b_no_evidence_sft | DONE | success | - | - | - | Training only |

---

## RANDOM_RSFT experiments

| experiment_id | status | conclusion | ign_f1 | f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| random_rsft_k1_baseline | DONE | success | - | - | - | - | Training: loss=0.578, 3 epochs |
| random_rsft_k1_eval | DONE | success | 0.4114 | 0.4198 | 0.7964 | 0.6971 | CED RSFT mean=0.4596 >> random 0.4198, gap=~4pp proves CED scoring precision matters |

---

## GRPO experiments (non-eval, training runs)

| experiment_id | status | conclusion | notes |
|---|---|---|---|
| smoke_test_grpo | DONE | success | |
| mvp2_grpo_ced | DONE | failed | |
| mvp2_grpo_ced_r1 | DONE | killed | |
| mvp2_grpo_ced_r2 | DONE | killed | |
| mvp2_grpo_ced_r3 | DONE | failed | kl_coef=0.05 |
| mvp2_grpo_ced_r4 | DONE | killed | |
| mvp2_grpo_ced_r5 | DONE | negative | |
| mvp2_grpo_ced_kl001 | DONE | failed | kl_coef=0.01 |
| mvp2_grpo_ced_kl001_r2 | DONE | killed | |
| mvp2_grpo_ced_kl001_r3 | DONE | killed | |
| mvp2_grpo_ced_kl001_r4 | DONE | success | 100 steps, best_reward=1.37 at step 90 |
| mvp2_grpo_ced_lr5e6_r1 | DONE | killed | lr=5e-6 |
| mvp2_grpo_ced_lr5e6_p1_r1 | DONE | killed | lr=5e-6 + recall_penalty |
| mvp2_grpo_ced_lr5e6_rp_r1 | DONE | failed | |
| mvp2_grpo_ced_lr5e6_rp_r2 | DONE | killed | |
| mvp2_grpo_extract | DONE | failed | Extraction-only reward |
| mvp2_grpo_extract_r2 | DONE | killed | |
| mvp2_grpo_extract_r3 | DONE | negative | |
| mvp2_grpo_extract_r4 | DONE | killed | |
| mvp2_grpo_flatnli | DONE | failed | |
| mvp2_grpo_flatnli_r2 | DONE | killed | |
| mvp2_grpo_flatnli_r3 | DONE | killed | |
| mvp2_grpo_flatnli_r4 | DONE | killed | |
| mvp2_grpo_flatnli_r5 | DONE | killed | |
| mvp2_grpo_flatnli_r6 | DONE | negative | Collapsed at step 25 |
| plan_011_grpo_g8_bf16 | DONE | success | bf16, 100 steps, no mode collapse |
| plan_015_grpo_g4_bf16 | DONE | killed | |
| plan_015_grpo_g4_bf16_v2 | DONE | killed | |
| plan_015_grpo_g4_bf16_v3 | DONE | killed | |
| plan_016_llama_grpo_qlora | DONE | success | Catastrophic decoupling confirmed cross-family (format=1, f1=0, ced=0) |
| lead2_rsft_grpo_ced | DONE | failed | RSFT->GRPO two-stage |
| lead2_rsft_grpo_ced_r2 | DONE | failed | RSFT->GRPO retry |
| wave1_grpo_bf16_g4 | DONE | success | 200 steps, reward=1.7646 |

---

**Total: 149 matching experiments** (out of 242 in registry).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1cd4c25-0779-483a-8864-3f8f3f3857b0",
  "isSidechain": true,
  "agentId": "a01ea92613c0e609d",
  "requestId": "req_011CbBwjz2j1EfVZoPqLwnpT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "950f8e61-cecf-436b-8e4b-0e069e0f372c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018pcX6WRsYEgDHrhV4FMAJw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2365,
      "cache_read_input_tokens": 58321,
      "output_tokens": 7652,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2365
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7652,
          "cache_read_input_tokens": 58321,
          "cache_creation_input_tokens": 2365,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2365,
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
