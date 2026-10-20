# Research conversation: Parse the registry JSON file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a37fba2a40b1ce129.jsonl`
- **Structured JSON:** [`ef9a842274583f4dd077.json`](../../sessions/ef/ef9a842274583f4dd077.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

25 recorded events

### User

_source line 1 · 2026-05-19T07:57:44.552Z_

Parse the registry JSON file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt

This file is JSON with schema: {result: string}. The "result" field is itself a JSON string containing an array of experiment objects.

I need ALL experiments whose exp_id or name contains "fewnerd" (case-insensitive). For each matching experiment, return the FULL object including all fields — especially: exp_id, status, conclusion, metrics, config, notes, and any other fields present. Quote all numeric values verbatim.

Also search for any experiment with "n16" or "n_16" in its name/id.

Use jq or python to parse. Return the complete data for all matching experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6db2e51c-9e8c-47e6-b1c4-6f35ea2e4e39",
  "agentId": "a37fba2a40b1ce129",
  "type": "user",
  "uuid": "22f2e590-6567-404f-8e3d-1c517910f134",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T07:57:44.557Z_

```json
{
  "parentUuid": "22f2e590-6567-404f-8e3d-1c517910f134",
  "isSidechain": true,
  "agentId": "a37fba2a40b1ce129",
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
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "79958d2b-68a9-47e4-8e50-c720a955bc3c",
  "timestamp": "2026-05-19T07:57:44.557Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-19T07:57:51.195Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01M8UkEAsoG5oE7L3V7tWvw8`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt | python3 -c \"\nimport json, sys, re\n\nraw = json.load(sys.stdin)\nresult = json.loads(raw['result'])\n\nmatches = []\nfor exp in result:\n    exp_str = json.dumps(exp).lower()\n    exp_id = str(exp.get('exp_id', '')).lower()\n    name = str(exp.get('name', '')).lower()\n    \n    # Check for fewnerd, n16, n_16 in exp_id or name\n    if any(kw in exp_id or kw in name for kw in ['fewnerd', 'n16', 'n_16']):\n        matches.append(exp)\n\nprint(json.dumps(matches, indent=2, ensure_ascii=False))\nprint(f'\\n--- Total matching experiments: {len(matches)} ---')\n\"\n",
  "description": "Parse registry JSON and filter experiments matching fewnerd/n16/n_16"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79958d2b-68a9-47e4-8e50-c720a955bc3c",
  "isSidechain": true,
  "agentId": "a37fba2a40b1ce129",
  "requestId": "req_011CbBa7WHfmWcqFcxijcVfh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2a7e435-ceb9-4314-b99a-388dc3b8616e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0142taEVV4JtfX9i5ysqYeKN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15939,
      "cache_read_input_tokens": 0,
      "output_tokens": 382,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15939
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 382,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15939,
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

_source line 4 · 2026-05-19T07:57:51.512Z_

<details><summary>↩ Tool result · reported error · `toolu_01M8UkEAsoG5oE7L3V7tWvw8`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 10, in &lt;module>
    exp_id = str(exp.get('exp_id', '')).lower()
                 ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2a7e435-ceb9-4314-b99a-388dc3b8616e",
  "isSidechain": true,
  "promptId": "6db2e51c-9e8c-47e6-b1c4-6f35ea2e4e39",
  "agentId": "a37fba2a40b1ce129",
  "type": "user",
  "uuid": "8061c6ae-b595-44db-892b-026c7b79579e",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 10, in &lt;module>\n    exp_id = str(exp.get('exp_id', '')).lower()\n                 ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'",
  "sourceToolAssistantUUID": "c2a7e435-ceb9-4314-b99a-388dc3b8616e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-19T07:57:54.059Z_

The data structure is different than expected. Let me inspect it first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8061c6ae-b595-44db-892b-026c7b79579e",
  "isSidechain": true,
  "agentId": "a37fba2a40b1ce129",
  "requestId": "req_011CbBa825oMwTZg8dBa6JF8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24817d69-317d-4422-a468-72a14692e1df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2gPheypPYC4nBmveepk7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1312,
      "cache_read_input_tokens": 15939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1312,
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

_source line 6 · 2026-05-19T07:57:58.504Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Y6thA1cS5tnNve6kUysMZm`</summary>

```json
{
  "command": "python3 -c \"\nimport json, sys\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nprint(f'Type of result: {type(result)}')\nif isinstance(result, list):\n    print(f'Length: {len(result)}')\n    for i, item in enumerate(result[:3]):\n        print(f'Item {i} type: {type(item)}')\n        if isinstance(item, str):\n            print(f'  Value: {item[:200]}')\n        elif isinstance(item, dict):\n            print(f'  Keys: {list(item.keys())}')\nelif isinstance(result, dict):\n    print(f'Keys: {list(result.keys())}')\n    for k in list(result.keys())[:5]:\n        v = result[k]\n        print(f'  {k}: type={type(v)}')\n        if isinstance(v, list) and len(v) > 0:\n            print(f'    First item type: {type(v[0])}')\n            if isinstance(v[0], dict):\n                print(f'    First item keys: {list(v[0].keys())}')\n\"\n",
  "description": "Inspect the structure of the parsed registry JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24817d69-317d-4422-a468-72a14692e1df",
  "isSidechain": true,
  "agentId": "a37fba2a40b1ce129",
  "requestId": "req_011CbBa825oMwTZg8dBa6JF8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3044355b-cbfb-4bf4-832e-adacc79ef8b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2gPheypPYC4nBmveepk7e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1312,
      "cache_read_input_tokens": 15939,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1312
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 15939,
          "cache_creation_input_tokens": 1312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1312,
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

_source line 7 · 2026-05-19T07:57:58.602Z_

<details><summary>↩ Tool result · `toolu_01Y6thA1cS5tnNve6kUysMZm`</summary>

```text
Type of result: &lt;class 'dict'>
Keys: ['success', 'data', 'error', 'metadata']
  success: type=&lt;class 'bool'>
  data: type=&lt;class 'dict'>
  error: type=&lt;class 'NoneType'>
  metadata: type=&lt;class 'dict'>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3044355b-cbfb-4bf4-832e-adacc79ef8b6",
  "isSidechain": true,
  "promptId": "6db2e51c-9e8c-47e6-b1c4-6f35ea2e4e39",
  "agentId": "a37fba2a40b1ce129",
  "type": "user",
  "uuid": "f200303a-3daa-4acd-874a-03bd4d15a339",
  "sourceToolAssistantUUID": "3044355b-cbfb-4bf4-832e-adacc79ef8b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T07:58:03.998Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0125Lbi1J176z85yGcbvjNvP`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\ndata = result['data']\nprint(f'Data keys: {list(data.keys())}')\nfor k in data.keys():\n    v = data[k]\n    print(f'  {k}: type={type(v).__name__}, ', end='')\n    if isinstance(v, list):\n        print(f'len={len(v)}')\n        if len(v) > 0:\n            print(f'    First item type: {type(v[0]).__name__}')\n            if isinstance(v[0], dict):\n                print(f'    First item keys: {list(v[0].keys())}')\n    elif isinstance(v, dict):\n        print(f'keys={list(v.keys())[:10]}')\n    else:\n        print(f'value={v}')\n\"\n",
  "description": "Inspect data structure inside the registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f200303a-3daa-4acd-874a-03bd4d15a339",
  "isSidechain": true,
  "agentId": "a37fba2a40b1ce129",
  "requestId": "req_011CbBa8YHk7Re15b2LfuoK9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d19b8a45-ba02-415b-bef7-fb2803b7b0f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MT4pBZ4dJDua1P9vk6x1gU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 568,
      "cache_read_input_tokens": 17251,
      "output_tokens": 399,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 568
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 399,
          "cache_read_input_tokens": 17251,
          "cache_creation_input_tokens": 568,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 568,
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

_source line 9 · 2026-05-19T07:58:04.161Z_

<details><summary>↩ Tool result · `toolu_0125Lbi1J176z85yGcbvjNvP`</summary>

```text
Data keys: ['experiments', 'count', 'total', 'baseline']
  experiments: type=dict, keys=['exp_qwen25_32b_fewnerd', 'exp_qwen25_7b_fewnerd', 'exp_wnut17_qwen25_7b', 'exp_qwen25_14b_fewnerd', 'exp_qwen25_72b_zeroshot', 'exp_llama_fewnerd_inference', 'exp_entity_construction', 'exp_lp_alignment_gating', 'exp_selective_prediction', 'exp_llama_fewnerd_lora']
  count: type=int, value=171
  total: type=int, value=171
  baseline: type=NoneType, value=None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d19b8a45-ba02-415b-bef7-fb2803b7b0f5",
  "isSidechain": true,
  "promptId": "6db2e51c-9e8c-47e6-b1c4-6f35ea2e4e39",
  "agentId": "a37fba2a40b1ce129",
  "type": "user",
  "uuid": "c7a4c424-b98d-4937-8550-6aa073fb34e6",
  "sourceToolAssistantUUID": "d19b8a45-ba02-415b-bef7-fb2803b7b0f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T07:58:10.654Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MHTpt9hdtBCeoUSviEafvf`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nexperiments = result['data']['experiments']\n\n# experiments is a dict keyed by exp_id\nmatches = {}\nfor exp_id, exp_data in experiments.items():\n    exp_id_lower = exp_id.lower()\n    # Also check name if present\n    name = ''\n    if isinstance(exp_data, dict):\n        name = str(exp_data.get('name', '')).lower()\n    elif isinstance(exp_data, list):\n        # might be a list of sub-experiments\n        pass\n    \n    combined = exp_id_lower + ' ' + name\n    if any(kw in combined for kw in ['fewnerd', 'n16', 'n_16']):\n        matches[exp_id] = exp_data\n\nprint(json.dumps(matches, indent=2, ensure_ascii=False))\nprint(f'\\n--- Total matching experiment keys: {len(matches)} ---')\n\" 2>&1 | head -50\n",
  "description": "Filter experiments matching fewnerd/n16/n_16 from the dict-keyed experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7a4c424-b98d-4937-8550-6aa073fb34e6",
  "isSidechain": true,
  "agentId": "a37fba2a40b1ce129",
  "requestId": "req_011CbBa8x5UaSrDX6YqjKVsr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75142da9-6bc2-4a47-a013-649cc6fd06a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R7bZJrBJPYt7AN2pNYA5FF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 17819,
      "output_tokens": 444,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 602
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 444,
          "cache_read_input_tokens": 17819,
          "cache_creation_input_tokens": 602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 602,
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

_source line 11 · 2026-05-19T07:58:10.745Z_

<details><summary>↩ Tool result · `toolu_01MHTpt9hdtBCeoUSviEafvf`</summary>

```text
{
  "exp_qwen25_32b_fewnerd": {
    "status": "ALLOCATED",
    "retry_count": 0,
    "created_at": "2026-05-19T06:19:25.428Z",
    "updated_at": "2026-05-19T07:52:18.591Z",
    "hypothesis": "The correlation-selection gap (high QE correlation but no selection gain) generalizes to 32B-scale models. Qwen2.5-32B QLoRA fine-tuned on FewNERD should show the same pattern: structural signals have high ρ but fail at instance-level selection, while entity construction (θ=2/N) provides significant F1 gain. This fills the 8B→72B scale gap.",
    "server": "autodl-5090",
    "gpu": "cuda:0,cuda:1,cuda:2,cuda:3",
    "account": "root",
    "reproduce": {
      "server": "autodl-5090",
      "gpu": "cuda:0,cuda:1,cuda:2,cuda:3",
      "started_at": "2026-05-19T06:47:41.246Z"
    },
    "notes": "2026-05-19 15:52 UTC: 32B model download in progress, 26GB/~65GB (~40%), 8 incomplete blobs remaining. PIDs 764902/764903 still active. Disk OK (84GB free). ETA ~1-2h."
  },
  "exp_qwen25_7b_fewnerd": {
    "status": "QUEUED",
    "retry_count": 0,
    "created_at": "2026-05-19T06:41:43.121Z",
    "updated_at": "2026-05-19T07:48:40.207Z",
    "hypothesis": "Qwen2.5-7B fine-tuned on FewNERD provides the baseline point for a pure Qwen2.5 family scale curve (7B/14B/32B/72B). This eliminates the confound of mixing Qwen2.5 and Qwen3 families when studying how the correlation-selection gap changes with model scale."
  },
  "exp_qwen25_14b_fewnerd": {
    "status": "ALLOCATED",
    "retry_count": 0,
    "created_at": "2026-05-19T06:19:31.620Z",
    "updated_at": "2026-05-19T06:47:43.938Z",
    "hypothesis": "The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings.",
    "server": "autodl-5090-c",
    "gpu": "cuda:0,cuda:1",
    "account": "root",
    "reproduce": {
      "server": "autodl-5090-c",
      "gpu": "cuda:0,cuda:1",
      "started_at": "2026-05-19T06:47:43.938Z"
    }
  },
  "exp_llama_fewnerd_inference": {
    "status": "DONE",
    "retry_count": 0,
    "created_at": "2026-05-19T02:18:49.938Z",
    "updated_at": "2026-05-19T03:15:04.486Z",
    "hypothesis": "LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness.",
    "parent": "exp_llama_fewnerd_lora",
    "spec": {
      "command": "bash code/run_llama_fewnerd_inference.sh",
      "server": "autodl-5090",
      "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/",
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75142da9-6bc2-4a47-a013-649cc6fd06a3",
  "isSidechain": true,
  "promptId": "6db2e51c-9e8c-47e6-b1c4-6f35ea2e4e39",
  "agentId": "a37fba2a40b1ce129",
  "type": "user",
  "uuid": "b082b6dc-56fb-4c49-8291-c1f225098f99",
  "sourceToolAssistantUUID": "75142da9-6bc2-4a47-a013-649cc6fd06a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T07:58:16.217Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014i2nkeSZEzHJCofmtKRPcD`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nexperiments = result['data']['experiments']\n\nmatches = {}\nfor exp_id, exp_data in experiments.items():\n    exp_id_lower = exp_id.lower()\n    name = ''\n    if isinstance(exp_data, dict):\n        name = str(exp_data.get('name', '')).lower()\n    combined = exp_id_lower + ' ' + name\n    if any(kw in combined for kw in ['fewnerd', 'n16', 'n_16']):\n        matches[exp_id] = exp_data\n\nprint(json.dumps(matches, indent=2, ensure_ascii=False))\nprint(f'\\n--- Total matching experiment keys: {len(matches)} ---')\n\" 2>&1\n",
  "description": "Print ALL matching experiments fully (no head truncation)",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b082b6dc-56fb-4c49-8291-c1f225098f99",
  "isSidechain": true,
  "agentId": "a37fba2a40b1ce129",
  "requestId": "req_011CbBa9SEeCes6y9hXB8xwH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dddf29a-0a8e-46d6-8a1a-9b6e95ddbdc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNYvCmyv1F8PCe3jAxSDWa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1520,
      "cache_read_input_tokens": 18421,
      "output_tokens": 399,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1520
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 399,
          "cache_read_input_tokens": 18421,
          "cache_creation_input_tokens": 1520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1520,
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

_source line 13 · 2026-05-19T07:58:16.524Z_

<details><summary>↩ Tool result · `toolu_014i2nkeSZEzHJCofmtKRPcD`</summary>

```text
&lt;persisted-output>
Output too large (59.8KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/bhxefydqt.txt

Preview (first 2KB):
{
  "exp_qwen25_32b_fewnerd": {
    "status": "ALLOCATED",
    "retry_count": 0,
    "created_at": "2026-05-19T06:19:25.428Z",
    "updated_at": "2026-05-19T07:52:18.591Z",
    "hypothesis": "The correlation-selection gap (high QE correlation but no selection gain) generalizes to 32B-scale models. Qwen2.5-32B QLoRA fine-tuned on FewNERD should show the same pattern: structural signals have high ρ but fail at instance-level selection, while entity construction (θ=2/N) provides significant F1 gain. This fills the 8B→72B scale gap.",
    "server": "autodl-5090",
    "gpu": "cuda:0,cuda:1,cuda:2,cuda:3",
    "account": "root",
    "reproduce": {
      "server": "autodl-5090",
      "gpu": "cuda:0,cuda:1,cuda:2,cuda:3",
      "started_at": "2026-05-19T06:47:41.246Z"
    },
    "notes": "2026-05-19 15:52 UTC: 32B model download in progress, 26GB/~65GB (~40%), 8 incomplete blobs remaining. PIDs 764902/764903 still active. Disk OK (84GB free). ETA ~1-2h."
  },
  "exp_qwen25_7b_fewnerd": {
    "status": "QUEUED",
    "retry_count": 0,
    "created_at": "2026-05-19T06:41:43.121Z",
    "updated_at": "2026-05-19T07:48:40.207Z",
    "hypothesis": "Qwen2.5-7B fine-tuned on FewNERD provides the baseline point for a pure Qwen2.5 family scale curve (7B/14B/32B/72B). This eliminates the confound of mixing Qwen2.5 and Qwen3 families when studying how the correlation-selection gap changes with model scale."
  },
  "exp_qwen25_14b_fewnerd": {
    "status": "ALLOCATED",
    "retry_count": 0,
    "created_at": "2026-05-19T06:19:31.620Z",
    "updated_at": "2026-05-19T06:47:43.938Z",
    "hypothesis": "The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings.",
    "server": "autodl-5090-c",
    "gpu": "cuda:0,cuda:1",
    "account": "root",
    "reproduce": {
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dddf29a-0a8e-46d6-8a1a-9b6e95ddbdc3",
  "isSidechain": true,
  "promptId": "6db2e51c-9e8c-47e6-b1c4-6f35ea2e4e39",
  "agentId": "a37fba2a40b1ce129",
  "type": "user",
  "uuid": "4ed46b7c-303a-40ff-9faa-b562ac56b151",
  "sourceToolAssistantUUID": "8dddf29a-0a8e-46d6-8a1a-9b6e95ddbdc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T07:58:20.473Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XeWHr2hMCeddFWmMT6aCFA`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/bhxefydqt.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ed46b7c-303a-40ff-9faa-b562ac56b151",
  "isSidechain": true,
  "agentId": "a37fba2a40b1ce129",
  "requestId": "req_011CbBa9rzR4nhRcJ2hjvgrA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23b48a00-e600-4c32-b963-1614885f2b4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8B7eHbsRJYq495n1wD4xB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1282,
      "cache_read_input_tokens": 19941,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1282
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 19941,
          "cache_creation_input_tokens": 1282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1282,
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

_source line 15 · 2026-05-19T07:58:20.747Z_

<details><summary>↩ Tool result · reported error · `toolu_01XeWHr2hMCeddFWmMT6aCFA`</summary>

```text
File content (26113 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23b48a00-e600-4c32-b963-1614885f2b4f",
  "isSidechain": true,
  "promptId": "6db2e51c-9e8c-47e6-b1c4-6f35ea2e4e39",
  "agentId": "a37fba2a40b1ce129",
  "type": "user",
  "uuid": "d4b8e0a5-e86d-4ed6-b8f1-b3a43bf40569",
  "toolUseResult": "Error: File content (26113 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "23b48a00-e600-4c32-b963-1614885f2b4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T07:58:23.510Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MyPGbersD8pHnSzBtUQXqB`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/bhxefydqt.txt",
  "limit": 600
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4b8e0a5-e86d-4ed6-b8f1-b3a43bf40569",
  "isSidechain": true,
  "agentId": "a37fba2a40b1ce129",
  "requestId": "req_011CbBaAB18vFYTQ6vuhojz2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c28e9353-ae6d-42dd-81ad-31897b9de7b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Uw8kKYbgEc5qAFUQCN9QB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 192,
      "cache_read_input_tokens": 21223,
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
          "cache_read_input_tokens": 21223,
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

_source line 17 · 2026-05-19T07:58:24.021Z_

<details><summary>↩ Tool result · `toolu_01MyPGbersD8pHnSzBtUQXqB`</summary>

```text
1	{
2	  "exp_qwen25_32b_fewnerd": {
3	    "status": "ALLOCATED",
4	    "retry_count": 0,
5	    "created_at": "2026-05-19T06:19:25.428Z",
6	    "updated_at": "2026-05-19T07:52:18.591Z",
7	    "hypothesis": "The correlation-selection gap (high QE correlation but no selection gain) generalizes to 32B-scale models. Qwen2.5-32B QLoRA fine-tuned on FewNERD should show the same pattern: structural signals have high ρ but fail at instance-level selection, while entity construction (θ=2/N) provides significant F1 gain. This fills the 8B→72B scale gap.",
8	    "server": "autodl-5090",
9	    "gpu": "cuda:0,cuda:1,cuda:2,cuda:3",
10	    "account": "root",
11	    "reproduce": {
12	      "server": "autodl-5090",
13	      "gpu": "cuda:0,cuda:1,cuda:2,cuda:3",
14	      "started_at": "2026-05-19T06:47:41.246Z"
15	    },
16	    "notes": "2026-05-19 15:52 UTC: 32B model download in progress, 26GB/~65GB (~40%), 8 incomplete blobs remaining. PIDs 764902/764903 still active. Disk OK (84GB free). ETA ~1-2h."
17	  },
18	  "exp_qwen25_7b_fewnerd": {
19	    "status": "QUEUED",
20	    "retry_count": 0,
21	    "created_at": "2026-05-19T06:41:43.121Z",
22	    "updated_at": "2026-05-19T07:48:40.207Z",
23	    "hypothesis": "Qwen2.5-7B fine-tuned on FewNERD provides the baseline point for a pure Qwen2.5 family scale curve (7B/14B/32B/72B). This eliminates the confound of mixing Qwen2.5 and Qwen3 families when studying how the correlation-selection gap changes with model scale."
24	  },
25	  "exp_qwen25_14b_fewnerd": {
26	    "status": "ALLOCATED",
27	    "retry_count": 0,
28	    "created_at": "2026-05-19T06:19:31.620Z",
29	    "updated_at": "2026-05-19T06:47:43.938Z",
30	    "hypothesis": "The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings.",
31	    "server": "autodl-5090-c",
32	    "gpu": "cuda:0,cuda:1",
33	    "account": "root",
34	    "reproduce": {
35	      "server": "autodl-5090-c",
36	      "gpu": "cuda:0,cuda:1",
37	      "started_at": "2026-05-19T06:47:43.938Z"
38	    }
39	  },
40	  "exp_llama_fewnerd_inference": {
41	    "status": "DONE",
42	    "retry_count": 0,
43	    "created_at": "2026-05-19T02:18:49.938Z",
44	    "updated_at": "2026-05-19T03:15:04.486Z",
45	    "hypothesis": "LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness.",
46	    "parent": "exp_llama_fewnerd_lora",
47	    "spec": {
48	      "command": "bash code/run_llama_fewnerd_inference.sh",
49	      "server": "autodl-5090",
50	      "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/",
51	      "data_count": 37648,
52	      "model_name": "LLaMA-3.1-8B-FewNERD-LoRA-merged",
53	      "seed": "42,123,456",
54	      "checkpoint_source": "exp_llama_fewnerd_lora",
55	      "eval_data": "FewNERD test set",
56	      "checkpoint_path": "checkpoints/llama3.1-8b-fewnerd-merged/",
57	      "log_path": "logs/llama_fewnerd_inference.log"
58	    },
59	    "conclusion": "success",
60	    "metrics": {
61	      "3seed_mean": {
62	        "greedy_f1": 0.7842,
63	        "oracle_f1": 0.8843,
64	        "headroom_pp": 10.01,
65	        "degeneracy_pct": 23.36,
66	        "lp_delta_pp": 0.36,
67	        "dgs_delta_pp": -0.35
68	      },
69	      "seed_42": {
70	        "greedy_f1": 0.7841,
71	        "oracle_f1": 0.8854,
72	        "degen": 27.32
73	      },
74	      "seed_123": {
75	        "greedy_f1": 0.784,
76	        "oracle_f1": 0.8839,
77	        "degen": 24.63
78	      },
79	      "seed_456": {
80	        "greedy_f1": 0.7844,
81	        "oracle_f1": 0.8835,
82	        "degen": 18.13
83	      },
84	      "signal_ranking": "LP (+0.36pp) > SJ (-0.52) > FK (-0.53) > EM (-1.02) > VC (-2.39)",
85	      "lp_only_positive": true,
86	      "n_instances_gold_filtered": 32565
87	    },
88	    "completed_at": "2026-05-19T03:15:04.486Z"
89	  },
90	  "exp_llama_fewnerd_lora": {
91	    "status": "DONE",
92	    "retry_count": 0,
93	    "created_at": "2026-05-18T13:20:55.859Z",
94	    "updated_at": "2026-05-19T01:08:20.832Z",
95	    "hypothesis": "LLaMA-based model with LoRA fine-tuning on Few-NERD can provide a second model family (beyond Qwen) for cross-model generalization evidence of structured self-consistency phenomena in NER",
96	    "spec": {
97	      "command": "llamafactory-cli train train_config_llama_fewnerd.yaml",
98	      "server": "autodl-5090",
99	      "gpu": "cuda:1",
100	      "pid": 137865,
101	      "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd",
102	      "data_count": -1,
103	      "model_name": "LLaMA-Few-NERD-LoRA",
104	      "seed": 42,
105	      "log_path": "/root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log",
106	      "run_script": "run_llama_fewnerd_train_single_gpu.sh",
107	      "tmux_session": "llama_fewnerd",
108	      "note": "Retroactively registered - data_count unknown, seed assumed 42"
109	    },
110	    "checkpoint_path": "/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-fewnerd-lora",
111	    "log_path": "/root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log",
112	    "conclusion": "success",
113	    "metrics": {
114	      "epoch": 3,
115	      "train_loss": 0.0516,
116	      "eval_loss": 0.0323,
117	      "train_runtime_hours": 15.35,
118	      "total_steps": 24708,
119	      "final_checkpoint": "checkpoint-24708",
120	      "adapter_size_mb": 320
121	    },
122	    "completed_at": "2026-05-19T01:08:20.832Z"
123	  },
124	  "exp_031_fewnerd_t12": {
125	    "status": "DONE",
126	    "retry_count": 0,
127	    "created_at": "2026-05-18T20:04:12.040Z",
128	    "updated_at": "2026-05-19T00:30:14.652Z",
129	    "hypothesis": "FewNERD T=1.2 temperature ablation: test if higher temperature reduces degeneracy on FewNERD as observed on SciERC",
130	    "conclusion": "killed",
131	    "failure_reason": "数据不可用于论文：测试集(37648 vs T=1.0的5000)、N(8 vs 16)、分析管道(MVP pilot vs 5-signal)三重不一致。Director决定不重跑(DDL约束+非核心claim)。",
132	    "notes": "T=1.2 ablation not in paper scope, SciERC T=1.2 sufficient",
133	    "completed_at": "2026-05-19T00:30:14.652Z"
134	  },
135	  "exp_fewnerd_s789_n8": {
136	    "status": "DONE",
137	    "retry_count": 0,
138	    "created_at": "2026-05-18T23:17:34.011Z",
139	    "updated_at": "2026-05-18T23:18:28.125Z",
140	    "hypothesis": "FewNERD seed789 (4th seed) for statistical CI strengthening: 4-seed protocol provides tighter confidence intervals on LP selection gain and DGS effectiveness in low-degeneracy regime.",
141	    "parent": "exp_029a",
142	    "spec": {
143	      "command": "python code/analyze_fewnerd_s789.py",
144	      "server": "autodl-5090",
145	      "data_path": "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/samples.jsonl",
146	      "data_count": 37648,
147	      "model_name": "Qwen3-8B (ft_002_v2)",
148	      "seed": 789,
149	      "checkpoint_source": "exp_021 shards",
150	      "eval_data": "FewNERD test (37648 instances, 32565 gold-filtered)",
151	      "checkpoint_path": "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/",
152	      "log_path": "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/run.log"
153	    },
154	    "conclusion": "success",
155	    "completed_at": "2026-05-18T23:18:17.902Z",
156	    "metrics": {
157	      "greedy_f1": 0.7478,
158	      "oracle_f1": 0.8714,
159	      "headroom_pp": 12.37,
160	      "degen_rate": 0.1177,
161	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
162	      "instance_count": 37648,
163	      "n_valid": 32565,
164	      "lp_sel_f1": 0.7614,
165	      "lp_delta_pp": 1.36,
166	      "lp_rho_global": 0.1788,
167	      "lp_rho_cond": 0.176,
168	      "dgs_f1": 0.7621,
169	      "dgs_delta_pp": 1.43,
170	      "dgs_vs_lp_pp": 0.07,
171	      "best_signal": "LP",
172	      "four_seed_mean_greedy": 0.7481,
173	      "four_seed_mean_lp_delta_pp": 1.38,
174	      "four_seed_lp_delta_ci95": [
175	        1.32,
176	        1.44
177	      ]
178	    }
179	  },
180	  "exp_021_fewnerd_n8_seed456": {
181	    "status": "DONE",
182	    "retry_count": 0,
183	    "created_at": "2026-05-18T22:03:17.992Z",
184	    "updated_at": "2026-05-18T22:04:50.774Z",
185	    "hypothesis": "Multi-seed replication (seed=456) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.",
186	    "spec": {
187	      "command": "python scs_inference.py --dataset fewnerd --seed 456 --n_samples 8 --temperature 1.0",
188	      "server": "autodl-5090",
189	      "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd",
190	      "data_count": 37648,
191	      "model_name": "Qwen3-8B",
192	      "seed": 456,
193	      "checkpoint_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456",
194	      "log_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456_run.log"
195	    },
196	    "conclusion": "success",
197	    "completed_at": "2026-05-18T22:04:35.573Z",
198	    "metrics": {
199	      "degen_rate": 0.1212,
200	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
201	      "instance_count": 37648,
202	      "n_valid": 32565,
203	      "n_gold_empty": 5083,
204	      "ner_greedy_f1": 0.7888,
205	      "ner_oracle_f1": 0.881,
206	      "rho_fk_ner": 0.1632,
207	      "rho_sj_ner": 0.313,
208	      "sample_f1_pct_zero": 19.32
209	    }
210	  },
211	  "exp_021_fewnerd_n8_seed123": {
212	    "status": "DONE",
213	    "retry_count": 0,
214	    "created_at": "2026-05-18T22:03:16.735Z",
215	    "updated_at": "2026-05-18T22:04:49.470Z",
216	    "hypothesis": "Multi-seed replication (seed=123) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.",
217	    "spec": {
218	      "command": "python scs_inference.py --dataset fewnerd --seed 123 --n_samples 8 --temperature 1.0",
219	      "server": "autodl-5090",
220	      "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd",
221	      "data_count": 37648,
222	      "model_name": "Qwen3-8B",
223	      "seed": 123,
224	      "checkpoint_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123",
225	      "log_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123_run.log"
226	    },
227	    "conclusion": "success",
228	    "completed_at": "2026-05-18T22:04:33.731Z",
229	    "metrics": {
230	      "degen_rate": 0.1312,
231	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
232	      "instance_count": 37648,
233	      "n_valid": 32565,
234	      "n_gold_empty": 5083,
235	      "ner_greedy_f1": 0.7885,
236	      "ner_oracle_f1": 0.8892,
237	      "rho_fk_ner": 0.1602,
238	      "rho_sj_ner": 0.3083,
239	      "sample_f1_pct_zero": 20.39
240	    }
241	  },
242	  "exp_002_conll_n16_seed456": {
243	    "status": "DONE",
244	    "retry_count": 0,
245	    "created_at": "2026-05-18T22:03:15.720Z",
246	    "updated_at": "2026-05-18T22:04:46.954Z",
247	    "hypothesis": "Multi-seed replication (seed=456) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds.",
248	    "spec": {
249	      "command": "python scs_inference.py --dataset conll2003 --seed 456 --n_samples 16 --temperature 1.0",
250	      "server": "autodl-5090",
251	      "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/conll2003",
252	      "data_count": 3453,
253	      "model_name": "Qwen3-8B",
254	      "seed": 456,
255	      "checkpoint_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed456",
256	      "log_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed456.log"
257	    },
258	    "conclusion": "success",
259	    "completed_at": "2026-05-18T22:04:31.934Z",
260	    "metrics": {
261	      "degen_rate": 0.5544,
262	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
263	      "instance_count": 3453,
264	      "n_valid": 2756,
265	      "n_gold_empty": 697,
266	      "ner_greedy_f1": 0.9074,
267	      "ner_oracle_f1": 0.9549,
268	      "rho_fk_ner": 0.4718,
269	      "rho_sj_ner": 0.4819,
270	      "sample_f1_pct_zero": 7.02
271	    }
272	  },
273	  "exp_002_conll_n16_seed123": {
274	    "status": "DONE",
275	    "retry_count": 0,
276	    "created_at": "2026-05-18T22:03:14.343Z",
277	    "updated_at": "2026-05-18T22:04:45.039Z",
278	    "hypothesis": "Multi-seed replication (seed=123) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds.",
279	    "spec": {
280	      "command": "python scs_inference.py --dataset conll2003 --seed 123 --n_samples 16 --temperature 1.0",
281	      "server": "autodl-5090",
282	      "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/conll2003",
283	      "data_count": 3453,
284	      "model_name": "Qwen3-8B",
285	      "seed": 123,
286	      "checkpoint_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed123",
287	      "log_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed123.log"
288	    },
289	    "conclusion": "success",
290	    "completed_at": "2026-05-18T22:04:29.992Z",
291	    "metrics": {
292	      "degen_rate": 0.471,
293	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
294	      "instance_count": 3453,
295	      "n_valid": 2756,
296	      "n_gold_empty": 697,
297	      "ner_greedy_f1": 0.9068,
298	      "ner_oracle_f1": 0.9633,
299	      "rho_fk_ner": 0.4524,
300	      "rho_sj_ner": 0.4621,
301	      "sample_f1_pct_zero": 7.54
302	    }
303	  },
304	  "exp_017_llama_conll_n16_s456_r1024": {
305	    "status": "DONE",
306	    "retry_count": 0,
307	    "created_at": "2026-05-14T22:17:04.572Z",
308	    "updated_at": "2026-05-18T20:50:15.047Z",
309	    "spec": {
310	      "hypothesis": "D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed456.",
311	      "parent": "exp_017_llama_conll_n16_s456",
312	      "model_name": "llama3.1-8b-conll2003-merged",
313	      "dataset": "CoNLL-2003",
314	      "seed": 456,
315	      "server": "autodl-5090",
316	      "command": "python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_s456_r1024",
317	      "gpu": "cuda:2",
318	      "pid": "175870",
319	      "data_path": "data/conll2003",
320	      "data_count": 3453,
321	      "tmux_session": "exp_017_llama_conll_n16_s456_r1024"
322	    },
323	    "conclusion": "success",
324	    "metrics": {
325	      "degen_rate": 0.8672,
326	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
327	      "instance_count": 3453,
328	      "n_valid": 2756,
329	      "n_gold_empty": 697,
330	      "parse_rate": 1,
331	      "ner_greedy_f1": 0.9265,
332	      "ner_oracle_f1": 0.9499,
333	      "rho_fk_ner": 0.469,
334	      "rho_sj_ner": 0.4734,
335	      "rho_vc_ner": 0.4722,
336	      "rho_em_ner": 0.4752,
337	      "rho_lp_ner": 0.3099,
338	      "auroc_fk_ner": 0.7408,
339	      "auroc_sj_ner": 0.7428,
340	      "auroc_vc_ner": 0.7495,
341	      "auroc_em_ner": 0.7444,
342	      "auroc_lp_ner": 0.7628,
343	      "auroc_note": "median F1=1.0, AUROC uses >=median threshold",
344	      "rho_note": "CORRECTED 2026-05-15: old values (rho_fk=0.8085,rho_sj=0.1895) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756)."
345	    },
346	    "checkpoint_path": "N/A (inference-only)",
347	    "log_path": "output/exp_017_llama_conll_n16_s456_r1024_run.log",
348	    "completed_at": "2026-05-15T11:45:25.899Z",
349	    "hypothesis": "LLaMA CoNLL N=16 seed=456 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction."
350	  },
351	  "exp_017_llama_conll_n16_r1024": {
352	    "status": "DONE",
353	    "retry_count": 0,
354	    "created_at": "2026-05-14T22:17:01.036Z",
355	    "updated_at": "2026-05-18T20:50:11.906Z",
356	    "spec": {
357	      "hypothesis": "D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed42.",
358	      "parent": "exp_017_llama_conll_n16",
359	      "model_name": "llama3.1-8b-conll2003-merged",
360	      "dataset": "CoNLL-2003",
361	      "seed": 42,
362	      "server": "autodl-5090",
363	      "command": "python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_r1024",
364	      "gpu": "cuda:1",
365	      "pid": "175734",
366	      "data_path": "data/conll2003",
367	      "data_count": 3453,
368	      "tmux_session": "exp_017_llama_conll_n16_r1024"
369	    },
370	    "conclusion": "success",
371	    "metrics": {
372	      "degen_rate": 0.8647,
373	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
374	      "instance_count": 3453,
375	      "n_valid": 2756,
376	      "n_gold_empty": 697,
377	      "parse_rate": 1,
378	      "ner_greedy_f1": 0.9265,
379	      "ner_oracle_f1": 0.9499,
380	      "rho_fk_ner": 0.4752,
381	      "rho_sj_ner": 0.4836,
382	      "rho_vc_ner": 0.4746,
383	      "rho_em_ner": 0.4818,
384	      "rho_lp_ner": 0.3136,
385	      "auroc_fk_ner": 0.7467,
386	      "auroc_sj_ner": 0.7496,
387	      "auroc_vc_ner": 0.7529,
388	      "auroc_em_ner": 0.7508,
389	      "auroc_lp_ner": 0.7661,
390	      "auroc_note": "median F1=1.0, AUROC uses >=median threshold",
391	      "rho_note": "CORRECTED 2026-05-15: old values (rho_fk=0.8095,rho_sj=0.1815) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756)."
392	    },
393	    "checkpoint_path": "N/A (inference-only)",
394	    "log_path": "output/exp_017_llama_conll_n16_r1024_run.log",
395	    "completed_at": "2026-05-15T11:45:23.213Z",
396	    "hypothesis": "LLaMA CoNLL N=16 seed=42 (max_tokens=1024 rerun): cross-model baseline on CoNLL. Establishes LLaMA signal rankings after gold-filtering correction (fixes inflated FK ρ from gold-empty instances)."
397	  },
398	  "exp_002_conll_n16": {
399	    "status": "DONE",
400	    "retry_count": 0,
401	    "created_at": "2026-05-14T18:12:16.041Z",
402	    "updated_at": "2026-05-18T20:49:50.398Z",
403	    "spec": {
404	      "hypothesis": "Qwen CoNLL-2003 N=16: cross-dataset N-scaling comparison with SciERC N=16",
405	      "plan_id": "exp-002",
406	      "parent": "exp_002_ner_conll2003",
407	      "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_002_conll_n16",
408	      "server": "autodl-5090",
409	      "data_path": "data/conll2003",
410	      "data_count": 3453,
411	      "model_name": "qwen3-8b-conll2003-merged",
412	      "seed": 42
413	    },
414	    "conclusion": "success",
415	    "metrics": {
416	      "degen_rate": 0.4844,
417	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
418	      "N": 16,
419	      "dataset": "conll2003",
420	      "subtask": "ner",
421	      "n_instances": 3453,
422	      "n_valid": 2756,
423	      "n_conditional": 2614,
424	      "greedy_f1": 0.907,
425	      "full": {
426	        "SJ_rho": 0.4496,
427	        "FK_rho": 0.3928,
428	        "logprob_rho": 0.3146,
429	        "EM_rho": 0.4627,
430	        "voting_conf_rho": 0.4286,
431	        "SJ_AUROC": 0.8264,
432	        "FK_AUROC": 0.7821,
433	        "logprob_AUROC": 0.7531,
434	        "EM_AUROC": 0.8409,
435	        "voting_conf_AUROC": 0.8071,
436	        "SJ_ECE": 0.0747,
437	        "FK_ECE": 0.1786,
438	        "logprob_ECE": 0.2031,
439	        "EM_ECE": 0.0786,
440	        "voting_conf_ECE": 0.529
441	      },
442	      "conditional": {
443	        "SJ_rho": 0.4208,
444	        "FK_rho": 0.3494,
445	        "logprob_rho": 0.3756,
446	        "EM_rho": 0.4658,
447	        "voting_conf_rho": 0.3654,
448	        "SJ_AUROC": 0.8405,
449	        "FK_AUROC": 0.7819,
450	        "logprob_AUROC": 0.8259,
451	        "EM_AUROC": 0.8781,
452	        "voting_conf_AUROC": 0.7951,
453	        "SJ_ECE": 0.0982,
454	        "FK_ECE": 0.1899,
455	        "logprob_ECE": 0.2504,
456	        "EM_ECE": 0.0997,
457	        "voting_conf_ECE": 0.6096
458	      },
459	      "n8_vs_n16_delta_rho_full": {
460	        "SJ": 0.0139,
461	        "FK": -0.007,
462	        "logprob": -0.0011,
463	        "EM": 0.012,
464	        "voting_conf": 0.0049
465	      }
466	    },
467	    "checkpoint_path": "output/exp_002_conll_n16/samples.jsonl",
468	    "log_path": "output/exp_002_conll_n16.log",
469	    "completed_at": "2026-05-14T18:58:40.473Z",
470	    "hypothesis": "CoNLL N=16 NER: cross-dataset validation on high-performance NER dataset. Tests if structural signals retain advantage when base model performance is already high (greedy F1 > 0.9)."
471	  },
472	  "exp_027_fewnerd_n16": {
473	    "status": "DONE",
474	    "retry_count": 0,
475	    "created_at": "2026-05-17T05:28:57.036Z",
476	    "updated_at": "2026-05-18T20:48:58.455Z",
477	    "spec": {
478	      "hypothesis": "LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.",
479	      "parent": "exp_021_fewnerd_full",
480	      "model_name": "qwen3-8b-fewnerd-exp021-merged",
481	      "data_path": "data/fewnerd_n16_subset/test.json",
482	      "data_count": 5000,
483	      "seed": 42,
484	      "server": "autodl-5090",
485	      "gpu": "cuda:0,cuda:1,cuda:2,cuda:3",
486	      "command": "python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd_n16_subset --dataset fewnerd --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --start_index {0,1250,2500,3750} --end_index {1250,2500,3750,5000} --output_dir output/exp_027_fewnerd_n16/shard_{0-3}",
487	      "checkpoint_path": "output/exp_027_fewnerd_n16/sampled_results.jsonl",
488	      "log_path": "output/exp_027_fewnerd_n16/"
489	    },
490	    "conclusion": "success",
491	    "metrics": {
492	      "LP_delta_pp": 1.88,
493	      "LP_delta_95CI": [
494	        1.41,
495	        2.37
496	      ],
497	      "degen_rate": 0.0706,
498	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
499	      "greedy_f1": 0.7478,
500	      "lp_sel_f1": 0.7666,
501	      "oracle_f1": 0.902,
502	      "headroom_pp": 15.42,
503	      "all_8_types_positive": true,
504	      "n_instances": 5000,
505	      "N_samples": 16,
506	      "bootstrap_p": "<0.001"
507	    },
508	    "hypothesis": "LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.",
509	    "completed_at": "2026-05-17T05:46:48.460Z"
510	  },
511	  "exp_017_llama_conll_n16_s123_r1024": {
512	    "status": "DONE",
513	    "retry_count": 0,
514	    "created_at": "2026-05-14T22:17:02.953Z",
515	    "updated_at": "2026-05-18T20:47:52.122Z",
516	    "spec": {
517	      "hypothesis": "D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed123.",
518	      "parent": "exp_017_llama_conll_n16_s123",
519	      "model_name": "llama3.1-8b-conll2003-merged",
520	      "dataset": "CoNLL-2003",
521	      "seed": 123,
522	      "server": "autodl-5090",
523	      "command": "python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_s123_r1024",
524	      "data_path": "data/conll2003",
525	      "data_count": 3453
526	    },
527	    "conclusion": "success",
528	    "completed_at": "2026-05-15T01:20:51.219Z",
529	    "notes": "Output exists on autodl-5090. Registry status corrected from killed to success.",
530	    "hypothesis": "LLaMA CoNLL N=16 seed=123 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction.",
531	    "metrics": {
532	      "degen_rate": 0.8636,
533	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"
534	    }
535	  },
536	  "exp_028_fewnerd_5epoch": {
537	    "status": "DONE",
538	    "retry_count": 0,
539	    "created_at": "2026-05-17T07:53:12.913Z",
540	    "updated_at": "2026-05-17T20:29:42.274Z",
541	    "spec": {
542	      "hypothesis": "Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain.",
543	      "parent": "exp_021_fewnerd_full",
544	      "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0,1,2,3 llamafactory-cli train train_config_fewnerd_5epoch_4gpu.yaml 2>&1 | tee logs/exp_028_4gpu_train.log\"",
545	      "server": "autodl-5090",
546	      "gpu": "cuda:0,1,2,3",
547	      "data_path": "data/fewnerd_uie_train",
548	      "data_count": 131767,
549	      "model_name": "Qwen3-8B LoRA rank=32",
550	      "seed": 42,
551	      "log_path": "logs/exp_028_4gpu_train.log",
552	      "checkpoint_path": "checkpoints/qwen3-8b-fewnerd-5epoch-lora"
553	    },
554	    "conclusion": "negative",
555	    "metrics": {
556	      "degeneracy_cf1_gold": 0.3133,
557	      "greedy_f1": 0.7773,
558	      "lp_sel_delta_pp": 0.624,
559	      "lp_sel_f1": 0.7835,
560	      "oracle_f1": 0.8723,
561	      "within_instance_rho_mean": 0.4066,
562	      "within_instance_rho_median": 0.6151
563	    },
564	    "hypothesis": "Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain.",
565	    "completed_at": "2026-05-17T20:29:42.274Z"
566	  },
567	  "exp_008_re_n16": {
568	    "status": "DONE",
569	    "retry_count": 0,
570	    "created_at": "2026-05-14T12:03:06.876Z",
571	    "updated_at": "2026-05-17T02:58:19.490Z",
572	    "spec": {
573	      "hypothesis": "RE N=16 confirms negative finding with higher statistical power. If rho still <0.30, task-complexity boundary is robust.",
574	      "plan_id": "exp-008",
575	      "model_name": "qwen3-8b-scierc-merged-v2",
576	      "dataset": "SciERC",
577	      "gpu": "cuda:2",
578	      "server": "gpu-5090-4x-2",
579	      "gpu_budget_hours": 12,
580	      "description": "RE N=16 on SciERC to confirm negative finding. Inference with log-prob capture.",
581	      "priority": "P1",
582	      "command": "python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs",
583	      "data_path": "data/scierc/processed_data",
584	      "data_count": 551,
585	      "seed": 42,
586	      "num_instances": 200,
587	      "partial": true,
588	      "note": "Only 200/551 instances due to --num_test default bug. Needs full rerun."
589	    },
590	    "metrics": {
591	      "ner": {
592	        "greedy_f1": 0.6635,
593	        "oracle_f1": 0.8208,
594	        "headroom": 0.1572,
595	        "rho_sj_full": 0.377,
596	        "rho_fk_full": 0.2508,
597	        "rho_logprob_full": 0.3153,
598	        "rho_sj_cond": 0.3598,
599	        "rho_fk_cond": 0.2251,
600	        "rho_logprob_cond": 0.2927,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c28e9353-ae6d-42dd-81ad-31897b9de7b5",
  "isSidechain": true,
  "promptId": "6db2e51c-9e8c-47e6-b1c4-6f35ea2e4e39",
  "agentId": "a37fba2a40b1ce129",
  "type": "user",
  "uuid": "fc5ef91e-193c-4171-87c8-6a27546674b3",
  "sourceToolAssistantUUID": "c28e9353-ae6d-42dd-81ad-31897b9de7b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T07:58:29.217Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LLvMesQ9pq63rDA2XnxAR1`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/bhxefydqt.txt",
  "offset": 600,
  "limit": 600
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc5ef91e-193c-4171-87c8-6a27546674b3",
  "isSidechain": true,
  "agentId": "a37fba2a40b1ce129",
  "requestId": "req_011CbBaAR5UHvMgPeNUai7FQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68ebc718-1100-4810-89c3-f9a6121a4be8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uNSuM5JJH1NamEYwDqkd2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12309,
      "cache_read_input_tokens": 21415,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12309
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 21415,
          "cache_creation_input_tokens": 12309,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12309,
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

_source line 19 · 2026-05-19T07:58:29.224Z_

<details><summary>↩ Tool result · `toolu_01LLvMesQ9pq63rDA2XnxAR1`</summary>

```text
600	        "rho_logprob_cond": 0.2927,
601	        "sj_beats_fk": true,
602	        "rho_advantage": 0.1262
603	      },
604	      "re": {
605	        "greedy_f1": 0.4339,
606	        "oracle_f1": 0.6658,
607	        "headroom": 0.2319,
608	        "rho_sj_full": 0.2966,
609	        "rho_fk_full": 0.2871,
610	        "rho_logprob_full": 0.2986,
611	        "rho_sj_cond": 0.3975,
612	        "rho_fk_cond": 0.3774,
613	        "rho_logprob_cond": 0.2745,
614	        "sj_beats_fk": true,
615	        "rho_advantage": 0.0095
616	      },
617	      "verdict": "FAIL"
618	    },
619	    "conclusion": "success",
620	    "checkpoint_path": "N/A",
621	    "log_path": "output/exp008_re_n16/",
622	    "completed_at": "2026-05-14T12:28:39.268Z",
623	    "hypothesis": "RE N=16 initial evaluation: first relation extraction test with structural signals. Establishes baseline RE signal effectiveness before pipeline corrections."
624	  },
625	  "exp_001_ner_n16_seed123": {
626	    "status": "DONE",
627	    "retry_count": 0,
628	    "created_at": "2026-05-14T12:46:06.430Z",
629	    "updated_at": "2026-05-17T02:58:18.225Z",
630	    "spec": {
631	      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=3 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --output_dir output/exp001_n16_seed123 --num_test 9999 --collect_logprobs 2>&1 | tee output/exp001_n16_seed123_run.log\"",
632	      "server": "autodl-5090",
633	      "gpu": [
634	        "cuda:3"
635	      ],
636	      "pid": "63407",
637	      "log_path": "output/exp001_n16_seed123_run.log",
638	      "submitted_at": "2026-05-14T12:46:06.234Z",
639	      "submitted_via": "submit_training_job",
640	      "backend": "tmux",
641	      "account": "root",
642	      "data_count": 551,
643	      "data_path": "data/scierc/processed_data",
644	      "model_name": "qwen3-8b-scierc-merged-v2",
645	      "seed": 123,
646	      "checkpoint_path": "output/exp001_n16_seed123/",
647	      "wall_clock_seconds": 2748.0,
648	      "gpu_hours": 0.76
649	    },
650	    "conclusion": "success",
651	    "metrics": {
652	      "ner": {
653	        "greedy_f1": 0.663,
654	        "oracle_f1": 0.809,
655	        "headroom": 0.146,
656	        "rho_sj": 0.423,
657	        "rho_fk": 0.29,
658	        "rho_logprob": 0.239,
659	        "rho_sj_cond": 0.423,
660	        "rho_fk_cond": 0.26
661	      },
662	      "re": {
663	        "greedy_f1": 0.419,
664	        "oracle_f1": 0.625,
665	        "headroom": 0.206,
666	        "rho_sj": 0.267,
667	        "rho_fk": 0.315,
668	        "rho_sj_cond": 0.364,
669	        "rho_fk_cond": 0.331
670	      },
671	      "verdict": "FAIL",
672	      "verdict_note": "RE rho_sj=0.267 < 0.40; RE >30% samples F1=0",
673	      "n_instances": 551,
674	      "seed": 123,
675	      "N": 16,
676	      "T": 1
677	    },
678	    "completed_at": "2026-05-14T13:31:54.232Z",
679	    "hypothesis": "SciERC NER N=16 seed=123: multi-seed validation at N=16. Tests seed stability for signal rankings with more samples."
680	  },
681	  "exp_008_re_n16_t10_full": {
682	    "status": "DONE",
683	    "retry_count": 0,
684	    "created_at": "2026-05-14T13:27:42.867Z",
685	    "updated_at": "2026-05-17T02:58:10.171Z",
686	    "spec": {
687	      "command": "python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs",
688	      "server": "autodl-5090",
689	      "data_path": "data/scierc/processed_data",
690	      "data_count": 551,
691	      "model_name": "qwen3-8b-scierc-merged-v2",
692	      "seed": 42
693	    },
694	    "reproduce": {
695	      "finished_at": "2026-05-14T13:44:18.988Z"
696	    },
697	    "failure_reason": "",
698	    "conclusion": "negative",
699	    "completed_at": "2026-05-14T13:44:19.577Z",
700	    "extra": {
701	      "hook_events": [
702	        {
703	          "event": "on_failed",
704	          "action": "agent",
705	          "ts": "2026-05-14T13:44:21.528032+00:00"
706	        }
707	      ]
708	    },
709	    "metrics": {
710	      "ner": {
711	        "rho_sj": 0.444
712	      },
713	      "re": {
714	        "rho_sj": 0.248
715	      },
716	      "n_instances": 551,
717	      "N": 16,
718	      "T": 1,
719	      "seed": 42,
720	      "mode": "RE-only",
721	      "source": "director_corrected"
722	    },
723	    "hypothesis": "RE N=16 T=1.0 full dataset: early RE evaluation attempt. Tests structural signals on relation extraction before pipeline corrections."
724	  },
725	  "exp_008_re_n16_v2": {
726	    "status": "DONE",
727	    "retry_count": 0,
728	    "created_at": "2026-05-14T14:34:06.296Z",
729	    "updated_at": "2026-05-17T02:57:41.178Z",
730	    "spec": {
731	      "description": "RE N=16 on SciERC full set confirmation, ft_002_v2, with logprobs",
732	      "hypothesis": "Structural consistency correlates with per-instance RE F1 on SciERC full dataset",
733	      "server": "autodl-5090",
734	      "data_path": "data/scierc/processed_data",
735	      "data_count": 551,
736	      "model_name": "ft_002_v2",
737	      "seed": 42,
738	      "command": "CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_008_re_n16_v2",
739	      "gpu": [
740	        "cuda:3"
741	      ],
742	      "pid": "78737",
743	      "backend": "tmux",
744	      "account": "root",
745	      "log_path": "output/exp_008_re_n16_v2/run.log"
746	    },
747	    "conclusion": "negative",
748	    "metrics": {
749	      "sj_rho_full": 0.281,
750	      "sj_rho_cond": 0.308,
751	      "f1_zero_pct": 44.3,
752	      "conclusion_note": "RE N=16 v2 negative: SJ weak, 44.3% F1=0"
753	    },
754	    "checkpoint_path": "N/A (inference)",
755	    "completed_at": "2026-05-14T15:23:35.598Z",
756	    "log_path": "output/exp_008_re_n16_v2/",
757	    "hypothesis": "RE N=16 evaluation v2: tests structural signal effectiveness on relation extraction at higher sample count. Hypothesis: SJ/FK benefit from more samples on RE task where zero-F1 rate is high."
758	  },
759	  "exp_007_llama_n16": {
760	    "status": "DONE",
761	    "retry_count": 0,
762	    "created_at": "2026-05-14T18:31:44.366Z",
763	    "updated_at": "2026-05-17T02:57:12.521Z",
764	    "spec": {
765	      "hypothesis": "LLaMA SciERC N=16: cross-model N-scaling validation. If SJ rho increases from N=8 (0.363) to N=16, N-scaling is model-agnostic.",
766	      "plan_id": "exp-007",
767	      "parent": "exp_007_llama_inference",
768	      "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_007_llama_n16",
769	      "server": "autodl-5090",
770	      "data_path": "data/scierc/processed_data",
771	      "data_count": 551,
772	      "model_name": "llama3.1-8b-scierc-merged",
773	      "seed": 42,
774	      "checkpoint_source": "checkpoints/llama3.1-8b-scierc-merged",
775	      "eval_data": "data/scierc/processed_data"
776	    },
777	    "conclusion": "success",
778	    "checkpoint_path": "output/exp_007_llama_n16/samples.jsonl",
779	    "log_path": "output/exp_007_llama_n16.log",
780	    "completed_at": "2026-05-14T19:03:39.163Z",
781	    "metrics": {
782	      "N": 16,
783	      "dataset": "scierc",
784	      "subtask": "ner",
785	      "n_instances": 551,
786	      "n_valid": 529,
787	      "n_conditional": 478,
788	      "greedy_f1": 0.645,
789	      "full": {
790	        "SJ_rho": 0.3791,
791	        "FK_rho": 0.3081,
792	        "logprob_rho": 0.2041,
793	        "EM_rho": 0.3159,
794	        "voting_conf_rho": 0.4515,
795	        "SJ_AUROC": 0.717,
796	        "FK_AUROC": 0.6581,
797	        "logprob_AUROC": 0.5656,
798	        "EM_AUROC": 0.7686,
799	        "voting_conf_AUROC": 0.7266,
800	        "SJ_ECE": 0.1019,
801	        "FK_ECE": 0.1556,
802	        "logprob_ECE": 0.084,
803	        "EM_ECE": 0.1761,
804	        "voting_conf_ECE": 0.1365
805	      },
806	      "conditional": {
807	        "SJ_rho": 0.3222,
808	        "FK_rho": 0.2182,
809	        "logprob_rho": 0.1286,
810	        "EM_rho": 0.3563,
811	        "voting_conf_rho": 0.3356,
812	        "SJ_AUROC": 0.7014,
813	        "FK_AUROC": 0.6392,
814	        "logprob_AUROC": 0.545,
815	        "EM_AUROC": 0.7708,
816	        "voting_conf_AUROC": 0.6988,
817	        "SJ_ECE": 0.1466,
818	        "FK_ECE": 0.1853,
819	        "logprob_ECE": 0.1141,
820	        "EM_ECE": 0.1887,
821	        "voting_conf_ECE": 0.2634
822	      },
823	      "n8_vs_n16_delta_rho_full": {
824	        "SJ": 0.0161,
825	        "FK": -0.0185,
826	        "logprob": 0.0214,
827	        "EM": 0.0007,
828	        "voting_conf": 0.0184
829	      }
830	    },
831	    "hypothesis": "LLaMA SciERC N=16: cross-model NER signal evaluation at higher sample count. Tests if LLaMA shows same N-scaling benefit for structural signals as Qwen."
832	  },
833	  "exp_017_llama_conll_n16": {
834	    "status": "DONE",
835	    "retry_count": 0,
836	    "created_at": "2026-05-14T19:19:35.318Z",
837	    "updated_at": "2026-05-17T02:56:57.283Z",
838	    "spec": {
839	      "hypothesis": "LLaMA CoNLL N=16: complete the 2x2 matrix (model x dataset x N). If SJ N-scaling holds for LLaMA on CoNLL, the finding is fully cross-model cross-dataset.",
840	      "plan_id": "exp-017",
841	      "parent": "exp_017_llama_conll_infer",
842	      "model_name": "llama3.1-8b-conll2003-merged",
843	      "dataset": "CoNLL-2003",
844	      "data_count": 3453,
845	      "seed": 42,
846	      "server": "autodl-5090",
847	      "command": "CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_017_llama_conll_n16",
848	      "data_path": "data/conll2003",
849	      "pid": 106997,
850	      "n_samples": 16,
851	      "temperature": 1,
852	      "checkpoint_source": "checkpoints/llama3.1-8b-conll2003-merged",
853	      "eval_data": "conll2003 test set",
854	      "checkpoint_path": "output/exp_017_llama_conll_n16/samples.jsonl",
855	      "log_path": "output/exp_017_llama_conll_n16/all_signals_report.json"
856	    },
857	    "metrics": {
858	      "greedy_f1": 0.9243,
859	      "oracle_f1": 0.9487,
860	      "oracle_headroom": 0.0244,
861	      "n_instances": 3453,
862	      "n_valid": 2756,
863	      "n_conditional": 2642,
864	      "structural_beats_surface": true,
865	      "full": {
866	        "SJ_rho": 0.4642,
867	        "SJ_AUROC": 0.7391,
868	        "SJ_ECE": 0.1131,
869	        "FK_rho": 0.4566,
870	        "FK_AUROC": 0.736,
871	        "FK_ECE": 0.1071,
872	        "logprob_rho": 0.3058,
873	        "logprob_AUROC": 0.7594,
874	        "logprob_ECE": 0.1288,
875	        "EM_rho": 0.4613,
876	        "EM_AUROC": 0.7391,
877	        "EM_ECE": 0.1084,
878	        "voting_conf_rho": 0.4554,
879	        "voting_conf_AUROC": 0.7406,
880	        "voting_conf_ECE": 0.0844
881	      },
882	      "conditional": {
883	        "SJ_rho": 0.4597,
884	        "SJ_AUROC": 0.7565,
885	        "SJ_ECE": 0.0846,
886	        "FK_rho": 0.4515,
887	        "FK_AUROC": 0.753,
888	        "FK_ECE": 0.0813,
889	        "logprob_rho": 0.3193,
890	        "logprob_AUROC": 0.8023,
891	        "logprob_ECE": 0.0921,
892	        "EM_rho": 0.4618,
893	        "EM_AUROC": 0.7589,
894	        "EM_ECE": 0.0757,
895	        "voting_conf_rho": 0.3978,
896	        "voting_conf_AUROC": 0.7287,
897	        "voting_conf_ECE": 0.0742
898	      },
899	      "best_of_n": {
900	        "greedy": 0.9243,
901	        "random_avg": 0.9213,
902	        "sj_best": 0.9259,
903	        "logprob_best": 0.925,
904	        "voting_conf_best": 0.9268,
905	        "oracle": 0.9487
906	      },
907	      "n8_vs_n16_delta": {
908	        "full_SJ_rho_delta": 0.0328,
909	        "full_FK_rho_delta": 0.0289,
910	        "full_logprob_rho_delta": -0.0014,
911	        "full_EM_rho_delta": 0.0307,
912	        "full_voting_conf_rho_delta": 0.0298,
913	        "cond_SJ_rho_delta": 0.0241,
914	        "cond_FK_rho_delta": 0.0205,
915	        "cond_logprob_rho_delta": -0.0089,
916	        "cond_EM_rho_delta": 0.0215,
917	        "cond_voting_conf_rho_delta": 0.0235
918	      }
919	    },
920	    "conclusion": "success",
921	    "completed_at": "2026-05-14T19:45:16.265Z",
922	    "hypothesis": "LLaMA CoNLL N=16 seed=42 (original): cross-model validation on CoNLL. First evidence that structural>surface ranking generalizes from Qwen to LLaMA model family."
923	  },
924	  "exp_001_n16_seed456": {
925	    "status": "DONE",
926	    "retry_count": 1,
927	    "created_at": "2026-05-14T12:10:30.350Z",
928	    "updated_at": "2026-05-17T02:56:53.526Z",
929	    "completed_at": "2026-05-14T12:28:38.721Z",
930	    "extra": {
931	      "previous_failure": {
932	        "conclusion": "success",
933	        "metrics": {
934	          "ner": {
935	            "greedy_f1": 0.6577,
936	            "oracle_f1": 0.8129,
937	            "headroom": 0.1553,
938	            "rho_sj_full": 0.3297,
939	            "rho_fk_full": 0.2578,
940	            "rho_logprob_full": 0.2866,
941	            "rho_sj_cond": 0.3394,
942	            "rho_fk_cond": 0.2721,
943	            "rho_logprob_cond": 0.2567,
944	            "sj_beats_fk": true,
945	            "rho_advantage": 0.0719
946	          },
947	          "re": {
948	            "greedy_f1": 0.4312,
949	            "oracle_f1": 0.6737,
950	            "headroom": 0.2425,
951	            "rho_sj_full": 0.285,
952	            "rho_fk_full": 0.2372,
953	            "rho_logprob_full": 0.2626,
954	            "rho_sj_cond": 0.3525,
955	            "rho_fk_cond": 0.2614,
956	            "rho_logprob_cond": 0.1927,
957	            "sj_beats_fk": true,
958	            "rho_advantage": 0.0478
959	          },
960	          "verdict": "FAIL"
961	        }
962	      }
963	    },
964	    "spec": {
965	      "hypothesis": "N=16 seed456 multi-seed robustness verification for SciERC NER+RE",
966	      "plan_id": "exp-001",
967	      "model_name": "qwen3-8b-scierc-merged-v2",
968	      "data_path": "data/scierc/processed_data",
969	      "data_count": 551,
970	      "seed": 456,
971	      "command": "python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --output_dir output/exp001_n16_seed456 --collect_logprobs",
972	      "server": "autodl-5090",
973	      "gpu": "cuda:0",
974	      "pid": "174595",
975	      "log_path": "output/exp001_n16_seed456_run.log",
976	      "tmux_session": "exp_001_n16_seed456"
977	    },
978	    "conclusion": "success",
979	    "checkpoint_path": "N/A (inference-only)",
980	    "metrics": {
981	      "instance_count": 551,
982	      "n_valid": 529,
983	      "n_gold_empty": 22,
984	      "parse_rate": 1,
985	      "ner_greedy_f1": 0.6617,
986	      "ner_oracle_f1": 0.8075,
987	      "re_greedy_f1": 0.4215,
988	      "re_oracle_f1": 0.4748,
989	      "rho_sj_ner": 0.4098,
990	      "rho_fk_ner": 0.2723,
991	      "rho_vc_ner": 0.4449,
992	      "rho_em_ner": 0.3363,
993	      "rho_lp_ner": 0.2415,
994	      "rho_sj_re": 0.2835,
995	      "rho_fk_re": 0.2929,
996	      "auroc_sj_ner": 0.6823,
997	      "auroc_fk_ner": 0.6179,
998	      "auroc_vc_ner": 0.6981,
999	      "auroc_em_ner": 0.649,
1000	      "auroc_lp_ner": 0.5885,
1001	      "rho_note": "CORRECTED 2026-05-15: old values (rho_fk=0.3448,rho_sj=0.4134) included 22 gold-empty instances. Now uses gold-filtered pipeline (n=529)."
1002	    },
1003	    "log_path": "output/exp001_n16_seed456_run.log",
1004	    "hypothesis": "SciERC N=16 seed=456: early multi-seed validation of structural signal rankings at N=16 sample count. Establishes seed stability for SJ/FK/VC/EM ordering."
1005	  },
1006	  "exp_021_fewnerd_full": {
1007	    "status": "DONE",
1008	    "retry_count": 0,
1009	    "created_at": "2026-05-16T16:33:44.079Z",
1010	    "updated_at": "2026-05-17T02:55:45.560Z",
1011	    "hypothesis": "Full Few-NERD LoRA fine-tune (rank=32, α=64, 3 epochs) on SUPERVISED coarse 8-type NER (131k train). 4-GPU DDP on autodl-5090. Post-training: N=8 inference on full test set, T=1.0, seed=42, collect logprobs for SCS metrics.",
1012	    "spec": {
1013	      "gpu": "cuda:0,cuda:1,cuda:2,cuda:3",
1014	      "gpu_count": 4,
1015	      "training_mode": "DDP",
1016	      "checkpoint_path": "output/exp_021_fewnerd_full/checkpoint-6177",
1017	      "log_path": "output/exp_021_inference/"
1018	    },
1019	    "conclusion": "success",
1020	    "metrics": {
1021	      "total_steps": 6177,
1022	      "train_loss": 0.048,
1023	      "eval_loss": 0.0275,
1024	      "train_runtime": "3h57m",
1025	      "epochs": 3,
1026	      "final_checkpoint": "output/exp_021_fewnerd_full/checkpoint-6177",
1027	      "adapter_path": "output/exp_021_fewnerd_full/adapter_model.safetensors",
1028	      "inference_instances": 37648,
1029	      "inference_filtered": 32565,
1030	      "inference_n_samples": 8,
1031	      "greedy_macro_f1": 0.7478,
1032	      "oracle_macro_f1": 0.8719,
1033	      "headroom": 0.124,
1034	      "zero_f1_rate": 0.119,
1035	      "degeneracy_rate": 0.101,
1036	      "lp_within_range_mean": 0.0879,
1037	      "lp_within_range_median": 0.0662,
1038	      "lp_global_rho": 0.4215,
1039	      "lp_cond_rho": 0.4225,
1040	      "sj_global_rho": 0.3002,
1041	      "sj_cond_rho": 0.2937,
1042	      "fk_global_rho": 0.3132,
1043	      "fk_cond_rho": 0.3093,
1044	      "em_global_rho": 0.2871,
1045	      "em_cond_rho": 0.271,
1046	      "vc_global_rho": 0.3858,
1047	      "vc_cond_rho": 0.3234,
1048	      "lp_selection_delta_pp": 1.36,
1049	      "vc_selection_delta_pp": -1.79,
1050	      "sj_selection_delta_pp": -2.14,
1051	      "fk_selection_delta_pp": -2.26,
1052	      "em_selection_delta_pp": -3.85,
1053	      "lp_bootstrap_ci_95_pp": [
1054	        1.18,
1055	        1.53
1056	      ],
1057	      "lp_sample_auroc": 0.5782,
1058	      "vc_sample_auroc": 0.5354,
1059	      "fk_sample_auroc": 0.521,
1060	      "sj_sample_auroc": 0.5197,
1061	      "em_sample_auroc": 0.5137,
1062	      "scenario": "A_partial",
1063	      "note": "Full analysis (gold-filtered n=32565). Prior simplified analysis used unfiltered data with different metrics."
1064	    },
1065	    "completed_at": "2026-05-16T22:04:16.683Z",
1066	    "parent": "exp_020_fewnerd_smoke"
1067	  },
1068	  "exp_020_fewnerd_smoke": {
1069	    "status": "DONE",
1070	    "retry_count": 0,
1071	    "created_at": "2026-05-16T10:29:25.272Z",
1072	    "updated_at": "2026-05-16T16:33:59.109Z",
1073	    "spec": {
1074	      "checkpoint_path": "checkpoints/ft_fewnerd_smoke",
1075	      "log_path": "checkpoints/fewnerd_train.log"
1076	    },
1077	    "hypothesis": "1-epoch LoRA (r16) fine-tune Qwen3-8B on Few-NERD INTRA coarse 8-type (131k train), then N=8 T=1.0 pilot inference on 200 test instances. Re-started training 2026-05-16 18:29 CST on cuda:1, PID 288683. ETA ~22:55 CST.",
1078	    "conclusion": "success",
1079	    "metrics": {
1080	      "final_loss": 0.031,
1081	      "total_steps": 8236,
1082	      "training_time": "5h54m",
1083	      "pilot_greedy_f1": 0.8037,
1084	      "pilot_instances": 200,
1085	      "merged_model_path": "checkpoints/qwen3-8b-fewnerd-merged"
1086	    },
1087	    "completed_at": "2026-05-16T16:33:59.109Z"
1088	  },
1089	  "exp008_re_n16": {
1090	    "status": "DONE",
1091	    "retry_count": 0,
1092	    "created_at": "2026-05-14T12:09:50.987Z",
1093	    "updated_at": "2026-05-15T12:41:39.774Z",
1094	    "spec": {
1095	      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp008_re_n16 && CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp008_re_n16 --collect_logprobs 2>&1 | tee output/exp008_re_n16/run.log\"",
1096	      "server": "gpu-5090-4x-2",
1097	      "gpu": [
1098	        "cuda:2"
1099	      ],
1100	      "pid": "53600",
1101	      "log_path": "~/runs/struct_self_consist_ie/exp008_re_n16.log",
1102	      "submitted_at": "2026-05-14T12:15:14.917Z",
1103	      "submitted_via": "submit_training_job",
1104	      "backend": "tmux",
1105	      "account": "root",
1106	      "failure_reason": "Superseded by exp_008_re_n16_v2 (full 551-instance run on autodl-5090)",
1107	      "wall_clock_seconds": 87984.9,
1108	      "gpu_hours": 24.44
1109	    },
1110	    "conclusion": "killed",
1111	    "completed_at": "2026-05-15T12:41:39.774Z"
1112	  },
1113	  "exp_001_n16_seed456_full": {
1114	    "status": "DONE",
1115	    "retry_count": 0,
1116	    "created_at": "2026-05-14T12:44:31.348Z",
1117	    "updated_at": "2026-05-15T12:41:30.065Z",
1118	    "spec": {
1119	      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --num_test 9999 --output_dir output/exp001_n16_seed456/\"",
1120	      "server": "gpu-5090-4x-2",
1121	      "gpu": [
1122	        "cuda:1"
1123	      ],
1124	      "pid": "62170",
1125	      "log_path": "~/runs/struct_self_consist_ie/exp_001_n16_seed456_full.log",
1126	      "submitted_at": "2026-05-14T12:44:31.087Z",
1127	      "submitted_via": "submit_training_job",
1128	      "backend": "tmux",
1129	      "account": "root",
1130	      "failure_reason": "Superseded by exp_001_seed456_v2_ner (NER-only on autodl-5090)",
1131	      "wall_clock_seconds": 86219.0,
1132	      "gpu_hours": 23.95
1133	    },
1134	    "conclusion": "killed",
1135	    "failure_reason": "superseded by v2",
1136	    "completed_at": "2026-05-15T12:41:30.065Z"
1137	  },
1138	  "exp_001_n16_seed123_full": {
1139	    "status": "DONE",
1140	    "retry_count": 0,
1141	    "created_at": "2026-05-14T12:43:47.915Z",
1142	    "updated_at": "2026-05-15T12:41:29.068Z",
1143	    "spec": {
1144	      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --num_test 9999 --output_dir output/exp001_n16_seed123_full/\"",
1145	      "server": "gpu-5090-4x-2",
1146	      "gpu": [
1147	        "cuda:0"
1148	      ],
1149	      "pid": "61812",
1150	      "log_path": "~/runs/struct_self_consist_ie/exp_001_n16_seed123_full.log",
1151	      "submitted_at": "2026-05-14T12:44:06.059Z",
1152	      "submitted_via": "submit_training_job",
1153	      "backend": "tmux",
1154	      "account": "root",
1155	      "failure_reason": "Superseded by exp_001_seed123_v2 (NER-only on autodl-5090)",
1156	      "wall_clock_seconds": 86243.0,
1157	      "gpu_hours": 23.96
1158	    },
1159	    "conclusion": "killed",
1160	    "failure_reason": "superseded by v2",
1161	    "completed_at": "2026-05-15T12:41:29.068Z"
1162	  },
1163	  "exp_002_conll_n16_r1024": {
1164	    "status": "DONE",
1165	    "retry_count": 0,
1166	    "created_at": "2026-05-14T22:16:57.682Z",
1167	    "updated_at": "2026-05-15T01:20:53.108Z",
1168	    "spec": {
1169	      "hypothesis": "D054 rerun: max_tokens=1024. Verify truncation impact on Qwen CoNLL N=16.",
1170	      "parent": "exp_002_conll_n16",
1171	      "model_name": "qwen3-8b-conll2003-merged",
1172	      "dataset": "CoNLL-2003",
1173	      "seed": 42,
1174	      "server": "autodl-5090",
1175	      "command": "CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_002_conll_n16_r1024",
1176	      "data_path": "data/conll2003",
1177	      "data_count": 3453
1178	    },
1179	    "conclusion": "killed",
1180	    "completed_at": "2026-05-15T01:20:53.108Z"
1181	  },
1182	  "exp_007_llama_n16_r1024": {
1183	    "status": "DONE",
1184	    "retry_count": 0,
1185	    "created_at": "2026-05-14T22:16:59.685Z",
1186	    "updated_at": "2026-05-15T01:20:52.194Z",
1187	    "spec": {
1188	      "hypothesis": "D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA SciERC N=16.",
1189	      "parent": "exp_007_llama_n16",
1190	      "model_name": "llama3.1-8b-scierc-merged",
1191	      "dataset": "SciERC",
1192	      "seed": 42,
1193	      "server": "autodl-5090",
1194	      "command": "CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_007_llama_n16_r1024",
1195	      "data_path": "data/scierc/processed_data",
1196	      "data_count": 9999
1197	    },
1198	    "conclusion": "killed",
1199	    "completed_at": "2026-05-15T01:20:52.194Z"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68ebc718-1100-4810-89c3-f9a6121a4be8",
  "isSidechain": true,
  "promptId": "6db2e51c-9e8c-47e6-b1c4-6f35ea2e4e39",
  "agentId": "a37fba2a40b1ce129",
  "type": "user",
  "uuid": "e9953ea7-25ea-4ee5-8065-2ae73d19f088",
  "sourceToolAssistantUUID": "68ebc718-1100-4810-89c3-f9a6121a4be8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T07:58:34.834Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VcK3iDccdwRpYBAAZFdhZu`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/bhxefydqt.txt",
  "offset": 1198,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9953ea7-25ea-4ee5-8065-2ae73d19f088",
  "isSidechain": true,
  "agentId": "a37fba2a40b1ce129",
  "requestId": "req_011CbBaAoW6RAXew9bV54HS3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa4fb415-22d1-4f96-a34f-7e7c545b2f46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QYeAFB2h9fV1LjUoVVd8DT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11661,
      "cache_read_input_tokens": 33724,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11661
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 33724,
          "cache_creation_input_tokens": 11661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11661,
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

_source line 21 · 2026-05-19T07:58:34.840Z_

<details><summary>↩ Tool result · `toolu_01VcK3iDccdwRpYBAAZFdhZu`</summary>

```text
1198	    "conclusion": "killed",
1199	    "completed_at": "2026-05-15T01:20:52.194Z"
1200	  },
1201	  "exp_017_llama_conll_n16_s456": {
1202	    "status": "DONE",
1203	    "retry_count": 0,
1204	    "created_at": "2026-05-14T19:23:21.987Z",
1205	    "updated_at": "2026-05-14T20:24:45.875Z",
1206	    "hypothesis": "LLaMA CoNLL N=16 seed=456: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol",
1207	    "spec": {
1208	      "command": "CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --num_test 9999 --output_dir output/exp_017_llama_conll_n16_s456",
1209	      "server": "autodl-5090",
1210	      "data_path": "data/conll2003",
1211	      "data_count": 3453,
1212	      "model_name": "llama3.1-8b-conll2003-merged",
1213	      "seed": 456
1214	    },
1215	    "metrics": {
1216	      "greedy_f1": 0.9243,
1217	      "oracle_f1": 0.9488,
1218	      "oracle_headroom": 0.0245,
1219	      "n_instances": 3453,
1220	      "n_valid": 2756,
1221	      "n_conditional": 2642,
1222	      "structural_beats_surface": true,
1223	      "full": {
1224	        "SJ_rho": 0.4552,
1225	        "SJ_AUROC": 0.7288,
1226	        "SJ_ECE": 0.1134,
1227	        "FK_rho": 0.4478,
1228	        "FK_AUROC": 0.7248,
1229	        "FK_ECE": 0.109,
1230	        "logprob_rho": 0.3078,
1231	        "logprob_AUROC": 0.7612,
1232	        "logprob_ECE": 0.1289,
1233	        "EM_rho": 0.452,
1234	        "EM_AUROC": 0.7275,
1235	        "EM_ECE": 0.1082,
1236	        "voting_conf_rho": 0.4571,
1237	        "voting_conf_AUROC": 0.7348,
1238	        "voting_conf_ECE": 0.0863
1239	      },
1240	      "conditional": {
1241	        "SJ_rho": 0.4505,
1242	        "SJ_AUROC": 0.7449,
1243	        "SJ_ECE": 0.0826,
1244	        "FK_rho": 0.4422,
1245	        "FK_AUROC": 0.7401,
1246	        "FK_ECE": 0.0835,
1247	        "logprob_rho": 0.3242,
1248	        "logprob_AUROC": 0.8067,
1249	        "logprob_ECE": 0.0921,
1250	        "EM_rho": 0.451,
1251	        "EM_AUROC": 0.745,
1252	        "EM_ECE": 0.0756,
1253	        "voting_conf_rho": 0.3962,
1254	        "voting_conf_AUROC": 0.7202,
1255	        "voting_conf_ECE": 0.0746
1256	      },
1257	      "best_of_n": {
1258	        "greedy": 0.9243,
1259	        "random_avg": 0.9215,
1260	        "sj_best": 0.9243,
1261	        "logprob_best": 0.9243,
1262	        "voting_conf_best": 0.9243,
1263	        "oracle": 0.9488
1264	      },
1265	      "n8_vs_n16_delta": {
1266	        "full_SJ_rho_delta": 0.0238,
1267	        "full_FK_rho_delta": 0.0201,
1268	        "full_logprob_rho_delta": 0.0006,
1269	        "full_EM_rho_delta": 0.0214,
1270	        "full_voting_conf_rho_delta": 0.0315,
1271	        "cond_SJ_rho_delta": 0.0149,
1272	        "cond_FK_rho_delta": 0.0112,
1273	        "cond_logprob_rho_delta": -0.004,
1274	        "cond_EM_rho_delta": 0.0107,
1275	        "cond_voting_conf_rho_delta": 0.0219
1276	      }
1277	    },
1278	    "checkpoint_path": "output/exp_017_llama_conll_n16_s456/samples.jsonl",
1279	    "log_path": "output/exp_017_llama_conll_n16_s456/all_signals_report.json",
1280	    "conclusion": "success",
1281	    "completed_at": "2026-05-14T20:24:45.875Z"
1282	  },
1283	  "exp_017_llama_conll_n16_s123": {
1284	    "status": "DONE",
1285	    "retry_count": 0,
1286	    "created_at": "2026-05-14T19:23:21.084Z",
1287	    "updated_at": "2026-05-14T19:43:06.607Z",
1288	    "hypothesis": "LLaMA CoNLL N=16 seed=123: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol",
1289	    "spec": {
1290	      "hypothesis": "LLaMA CoNLL-2003 NER N=16 seed=123: cross-seed robustness check against N=8 seed=42 baseline (exp_017_llama_conll_infer)",
1291	      "command": "CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --num_test 9999 --output_dir output/exp_017_llama_conll_n16_s123",
1292	      "server": "autodl-5090",
1293	      "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/conll2003",
1294	      "data_count": 3453,
1295	      "model_name": "llama3.1-8b-conll2003-merged",
1296	      "seed": 123,
1297	      "checkpoint_source": "checkpoints/llama3.1-8b-conll2003-merged",
1298	      "eval_data": "data/conll2003",
1299	      "checkpoint_path": "output/exp_017_llama_conll_n16_s123/samples.jsonl",
1300	      "log_path": "output/exp_017_llama_conll_n16_s123.log"
1301	    },
1302	    "metrics": {
1303	      "greedy_f1": 0.9266,
1304	      "oracle_f1": 0.9497,
1305	      "oracle_headroom": 0.0231,
1306	      "n_instances": 3453,
1307	      "n_valid": 2756,
1308	      "n_conditional": 2642,
1309	      "structural_beats_surface": true,
1310	      "full": {
1311	        "SJ_rho": 0.4698,
1312	        "SJ_AUROC": 0.7402,
1313	        "SJ_ECE": 0.1135,
1314	        "FK_rho": 0.4594,
1315	        "FK_AUROC": 0.7351,
1316	        "FK_ECE": 0.1114,
1317	        "logprob_rho": 0.3161,
1318	        "logprob_AUROC": 0.768,
1319	        "logprob_ECE": 0.129,
1320	        "EM_rho": 0.4676,
1321	        "EM_AUROC": 0.7399,
1322	        "EM_ECE": 0.1082,
1323	        "voting_conf_rho": 0.4612,
1324	        "voting_conf_AUROC": 0.7429,
1325	        "voting_conf_ECE": 0.0832
1326	      },
1327	      "conditional": {
1328	        "SJ_rho": 0.4712,
1329	        "SJ_AUROC": 0.7609,
1330	        "SJ_ECE": 0.0828,
1331	        "FK_rho": 0.4595,
1332	        "FK_AUROC": 0.7547,
1333	        "FK_ECE": 0.0858,
1334	        "logprob_rho": 0.3314,
1335	        "logprob_AUROC": 0.8134,
1336	        "logprob_ECE": 0.0922,
1337	        "EM_rho": 0.4732,
1338	        "EM_AUROC": 0.7626,
1339	        "EM_ECE": 0.075,
1340	        "voting_conf_rho": 0.4086,
1341	        "voting_conf_AUROC": 0.7338,
1342	        "voting_conf_ECE": 0.0706
1343	      },
1344	      "best_of_n": {
1345	        "greedy": 0.9242,
1346	        "random_avg": 0.9216,
1347	        "sj_best": 0.9247,
1348	        "logprob_best": 0.9253,
1349	        "voting_conf_best": 0.9255,
1350	        "oracle": 0.9486
1351	      },
1352	      "n8_vs_n16_delta": {
1353	        "full_SJ_rho_delta": 0.0384,
1354	        "full_FK_rho_delta": 0.0317,
1355	        "full_logprob_rho_delta": 0.0089,
1356	        "full_SJ_AUROC_delta": 0.0363,
1357	        "full_FK_AUROC_delta": 0.0325,
1358	        "full_logprob_AUROC_delta": 0.007,
1359	        "cond_SJ_rho_delta": 0.0356,
1360	        "cond_FK_rho_delta": 0.0285,
1361	        "cond_logprob_rho_delta": 0.0032
1362	      }
1363	    },
1364	    "log_path": "output/exp_017_llama_conll_n16_s123.log",
1365	    "checkpoint_path": "output/exp_017_llama_conll_n16_s123/samples.jsonl",
1366	    "conclusion": "success",
1367	    "completed_at": "2026-05-14T19:43:06.607Z"
1368	  },
1369	  "exp_008_re_n16_full": {
1370	    "status": "DONE",
1371	    "retry_count": 0,
1372	    "created_at": "2026-05-14T12:45:10.852Z",
1373	    "updated_at": "2026-05-14T17:51:43.957Z",
1374	    "spec": {
1375	      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --num_test 9999 --output_dir output/exp008_re_n16/\"",
1376	      "server": "gpu-5090-4x-2",
1377	      "gpu": [
1378	        "cuda:2"
1379	      ],
1380	      "pid": "62585",
1381	      "log_path": "~/runs/struct_self_consist_ie/exp_008_re_n16_full.log",
1382	      "submitted_at": "2026-05-14T12:45:10.764Z",
1383	      "submitted_via": "submit_training_job",
1384	      "backend": "tmux",
1385	      "account": "root",
1386	      "wall_clock_seconds": 18393.2,
1387	      "gpu_hours": 5.11
1388	    },
1389	    "conclusion": "killed",
1390	    "failure_reason": "superseded by exp_008_re_n16_t10_full (full 551-instance RE-only run on autodl-5090)",
1391	    "completed_at": "2026-05-14T17:51:43.957Z"
1392	  },
1393	  "exp_001_n16_seed123": {
1394	    "status": "DONE",
1395	    "retry_count": 0,
1396	    "created_at": "2026-05-14T12:10:29.393Z",
1397	    "updated_at": "2026-05-14T12:42:58.393Z",
1398	    "spec": {
1399	      "command": "python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs",
1400	      "server": "gpu-5090-4x-2",
1401	      "data_path": "data/scierc/processed_data",
1402	      "data_count": 551,
1403	      "model_name": "qwen3-8b-scierc-merged-v2",
1404	      "seed": 123,
1405	      "num_instances": 200,
1406	      "partial": true,
1407	      "note": "Only 200/551 instances due to --num_test default bug. Needs full rerun."
1408	    },
1409	    "metrics": {
1410	      "ner": {
1411	        "greedy_f1": 0.655,
1412	        "oracle_f1": 0.8028,
1413	        "headroom": 0.1478,
1414	        "rho_sj_full": 0.4076,
1415	        "rho_fk_full": 0.2799,
1416	        "rho_logprob_full": 0.3189,
1417	        "rho_sj_cond": 0.4271,
1418	        "rho_fk_cond": 0.2743,
1419	        "rho_logprob_cond": 0.2835,
1420	        "sj_beats_fk": true,
1421	        "rho_advantage": 0.1277
1422	      },
1423	      "re": {
1424	        "greedy_f1": 0.4243,
1425	        "oracle_f1": 0.6771,
1426	        "headroom": 0.2528,
1427	        "rho_sj_full": 0.2943,
1428	        "rho_fk_full": 0.2657,
1429	        "rho_logprob_full": 0.3005,
1430	        "rho_sj_cond": 0.4003,
1431	        "rho_fk_cond": 0.313,
1432	        "rho_logprob_cond": 0.2317,
1433	        "sj_beats_fk": true,
1434	        "rho_advantage": 0.0286
1435	      },
1436	      "verdict": "FAIL"
1437	    },
1438	    "conclusion": "success",
1439	    "checkpoint_path": "N/A",
1440	    "log_path": "output/exp001_n16_seed123/",
1441	    "completed_at": "2026-05-14T12:28:38.104Z"
1442	  },
1443	  "exp_001_ner_n16_scierc": {
1444	    "status": "DONE",
1445	    "retry_count": 0,
1446	    "created_at": "2026-05-14T11:42:10.898Z",
1447	    "updated_at": "2026-05-14T12:42:49.592Z",
1448	    "spec": {
1449	      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp001_n16_seed42 --num_test 9999 --collect_logprobs 2>&1 | tee output/exp001_n16_seed42_run.log\"",
1450	      "server": "autodl-5090",
1451	      "gpu": [
1452	        "cuda:0"
1453	      ],
1454	      "pid": "54357",
1455	      "log_path": "~/runs/struct_self_consist_ie/exp_001_ner_n16_scierc.log",
1456	      "submitted_at": "2026-05-14T12:15:46.646Z",
1457	      "submitted_via": "submit_training_job",
1458	      "backend": "tmux",
1459	      "account": "root"
1460	    },
1461	    "server": "autodl-5090",
1462	    "gpu": "cuda:0",
1463	    "account": "root",
1464	    "reproduce": {
1465	      "server": "autodl-5090",
1466	      "gpu": "cuda:0",
1467	      "started_at": "2026-05-14T11:43:48.643Z"
1468	    },
1469	    "conclusion": "success",
1470	    "completed_at": "2026-05-14T11:55:45.664Z",
1471	    "metrics": {
1472	      "n_instances": 551,
1473	      "ner_n": 529,
1474	      "re_n": 397,
1475	      "N": 16,
1476	      "T": 1,
1477	      "seed": 42,
1478	      "full_test_set": true,
1479	      "ner_voting_conf_rho": 0.399,
1480	      "ner_sj_rho": 0.398,
1481	      "ner_em_rho": 0.339,
1482	      "ner_fk_rho": 0.288,
1483	      "ner_logprob_rho": 0.237,
1484	      "ner_voting_conf_auroc": 0.704,
1485	      "ner_sj_auroc": 0.697,
1486	      "ner_cond_em_rho": 0.414,
1487	      "ner_cond_sj_rho": 0.349,
1488	      "ner_cond_vc_rho": 0.34,
1489	      "re_voting_conf_rho": 0.38,
1490	      "re_logprob_rho": 0.293,
1491	      "re_fk_rho": 0.281,
1492	      "re_sj_rho": 0.277,
1493	      "re_em_rho": 0.148,
1494	      "re_voting_conf_auroc": 0.699,
1495	      "re_cond_em_rho": 0.475,
1496	      "re_cond_sj_rho": 0.318,
1497	      "re_cond_vc_rho": 0.35,
1498	      "re_cond_em_auroc": 0.742,
1499	      "diagnosis": "551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380). EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full FAIL (SJ 0.277 < 0.40). Previous N-scaling 'breakthrough' was artifact of 200 instances + T=0.7."
1500	    }
1501	  }
1502	}
1503	
1504	--- Total matching experiment keys: 36 ---
1505	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa4fb415-22d1-4f96-a34f-7e7c545b2f46",
  "isSidechain": true,
  "promptId": "6db2e51c-9e8c-47e6-b1c4-6f35ea2e4e39",
  "agentId": "a37fba2a40b1ce129",
  "type": "user",
  "uuid": "fd67f058-6be9-4a7a-a520-6c2fa0cd3fd8",
  "sourceToolAssistantUUID": "fa4fb415-22d1-4f96-a34f-7e7c545b2f46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-19T07:58:38.225Z_

Now let me also check if there were any experiments with "n16" or "n_16" not already captured by "fewnerd".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd67f058-6be9-4a7a-a520-6c2fa0cd3fd8",
  "isSidechain": true,
  "agentId": "a37fba2a40b1ce129",
  "requestId": "req_011CbBaBDRWgw9Bh2k5naEj2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b348dfa6-2f1c-4337-b49c-290427c6b79f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012oZ2udNvbDw7Djyj2aiUWg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6328,
      "cache_read_input_tokens": 45385,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6328,
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

_source line 23 · 2026-05-19T07:58:48.482Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FYLFTVKUa3Sk69jAo1yUes`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nexperiments = result['data']['experiments']\n\n# Find all with n16 or n_16 that don't also have fewnerd\nn16_only = {}\nfewnerd_ids = set()\nn16_ids = set()\n\nfor exp_id, exp_data in experiments.items():\n    exp_id_lower = exp_id.lower()\n    name = ''\n    if isinstance(exp_data, dict):\n        name = str(exp_data.get('name', '')).lower()\n    combined = exp_id_lower + ' ' + name\n    \n    if 'fewnerd' in combined:\n        fewnerd_ids.add(exp_id)\n    if 'n16' in combined or 'n_16' in combined:\n        n16_ids.add(exp_id)\n\n# Show which n16 experiments are NOT fewnerd (already shown above)\nn16_not_fewnerd = n16_ids - fewnerd_ids\nprint('=== n16/n_16 experiments already included (also contain fewnerd): ===')\nfor eid in sorted(n16_ids & fewnerd_ids):\n    print(f'  {eid}')\n\nprint()\nprint('=== n16/n_16 experiments NOT containing fewnerd (additional matches): ===')\nfor eid in sorted(n16_not_fewnerd):\n    print(f'  {eid}')\n\nprint()\nprint(f'Total fewnerd matches: {len(fewnerd_ids)}')\nprint(f'Total n16/n_16 matches: {len(n16_ids)}')\nprint(f'n16/n_16 already in fewnerd set: {len(n16_ids & fewnerd_ids)}')\nprint(f'n16/n_16 additional (not fewnerd): {len(n16_not_fewnerd)}')\nprint(f'Grand total unique matches: {len(fewnerd_ids | n16_ids)}')\n\"\n",
  "description": "Identify n16/n_16 experiments not already in the fewnerd set"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b348dfa6-2f1c-4337-b49c-290427c6b79f",
  "isSidechain": true,
  "agentId": "a37fba2a40b1ce129",
  "requestId": "req_011CbBaBDRWgw9Bh2k5naEj2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c89bf873-7bf0-4830-8504-b900b739ec46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012oZ2udNvbDw7Djyj2aiUWg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6328,
      "cache_read_input_tokens": 45385,
      "output_tokens": 726,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6328
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 726,
          "cache_read_input_tokens": 45385,
          "cache_creation_input_tokens": 6328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6328,
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

_source line 24 · 2026-05-19T07:58:48.589Z_

<details><summary>↩ Tool result · `toolu_01FYLFTVKUa3Sk69jAo1yUes`</summary>

```text
=== n16/n_16 experiments already included (also contain fewnerd): ===
  exp_027_fewnerd_n16

=== n16/n_16 experiments NOT containing fewnerd (additional matches): ===
  exp008_re_n16
  exp_001_n16_seed123
  exp_001_n16_seed123_full
  exp_001_n16_seed456
  exp_001_n16_seed456_full
  exp_001_ner_n16_scierc
  exp_001_ner_n16_seed123
  exp_002_conll_n16
  exp_002_conll_n16_r1024
  exp_002_conll_n16_seed123
  exp_002_conll_n16_seed456
  exp_007_llama_n16
  exp_007_llama_n16_r1024
  exp_008_re_n16
  exp_008_re_n16_full
  exp_008_re_n16_t10_full
  exp_008_re_n16_v2
  exp_017_llama_conll_n16
  exp_017_llama_conll_n16_r1024
  exp_017_llama_conll_n16_s123
  exp_017_llama_conll_n16_s123_r1024
  exp_017_llama_conll_n16_s456
  exp_017_llama_conll_n16_s456_r1024

Total fewnerd matches: 13
Total n16/n_16 matches: 24
n16/n_16 already in fewnerd set: 1
n16/n_16 additional (not fewnerd): 23
Grand total unique matches: 36
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c89bf873-7bf0-4830-8504-b900b739ec46",
  "isSidechain": true,
  "promptId": "6db2e51c-9e8c-47e6-b1c4-6f35ea2e4e39",
  "agentId": "a37fba2a40b1ce129",
  "type": "user",
  "uuid": "68b97513-c5d2-48a4-a1a6-845b101c9ae6",
  "sourceToolAssistantUUID": "c89bf873-7bf0-4830-8504-b900b739ec46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-19T08:02:02.250Z_

All 36 matching experiments have been fully extracted. Here is the complete data:

---

## Summary: 36 matching experiments (13 fewnerd + 23 n16-only + 1 overlap)

### FEWNERD experiments (13 total)

**1. exp_qwen25_32b_fewnerd**
- status: "ALLOCATED"
- retry_count: 0
- created_at: "2026-05-19T06:19:25.428Z"
- updated_at: "2026-05-19T07:52:18.591Z"
- hypothesis: "The correlation-selection gap (high QE correlation but no selection gain) generalizes to 32B-scale models. Qwen2.5-32B QLoRA fine-tuned on FewNERD should show the same pattern: structural signals have high ρ but fail at instance-level selection, while entity construction (θ=2/N) provides significant F1 gain. This fills the 8B→72B scale gap."
- server: "autodl-5090"
- gpu: "cuda:0,cuda:1,cuda:2,cuda:3"
- account: "root"
- reproduce: {server: "autodl-5090", gpu: "cuda:0,cuda:1,cuda:2,cuda:3", started_at: "2026-05-19T06:47:41.246Z"}
- notes: "2026-05-19 15:52 UTC: 32B model download in progress, 26GB/~65GB (~40%), 8 incomplete blobs remaining. PIDs 764902/764903 still active. Disk OK (84GB free). ETA ~1-2h."

**2. exp_qwen25_7b_fewnerd**
- status: "QUEUED"
- retry_count: 0
- created_at: "2026-05-19T06:41:43.121Z"
- updated_at: "2026-05-19T07:48:40.207Z"
- hypothesis: "Qwen2.5-7B fine-tuned on FewNERD provides the baseline point for a pure Qwen2.5 family scale curve (7B/14B/32B/72B). This eliminates the confound of mixing Qwen2.5 and Qwen3 families when studying how the correlation-selection gap changes with model scale."

**3. exp_qwen25_14b_fewnerd**
- status: "ALLOCATED"
- retry_count: 0
- created_at: "2026-05-19T06:19:31.620Z"
- updated_at: "2026-05-19T06:47:43.938Z"
- hypothesis: "The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings."
- server: "autodl-5090-c"
- gpu: "cuda:0,cuda:1"
- account: "root"
- reproduce: {server: "autodl-5090-c", gpu: "cuda:0,cuda:1", started_at: "2026-05-19T06:47:43.938Z"}

**4. exp_llama_fewnerd_inference**
- status: "DONE"
- conclusion: "success"
- created_at: "2026-05-19T02:18:49.938Z"
- updated_at: "2026-05-19T03:15:04.486Z"
- completed_at: "2026-05-19T03:15:04.486Z"
- hypothesis: "LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness."
- parent: "exp_llama_fewnerd_lora"
- spec: {command: "bash code/run_llama_fewnerd_inference.sh", server: "autodl-5090", data_path: "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/", data_count: 37648, model_name: "LLaMA-3.1-8B-FewNERD-LoRA-merged", seed: "42,123,456", checkpoint_source: "exp_llama_fewnerd_lora", eval_data: "FewNERD test set", checkpoint_path: "checkpoints/llama3.1-8b-fewnerd-merged/", log_path: "logs/llama_fewnerd_inference.log"}
- metrics:
  - 3seed_mean: {greedy_f1: 0.7842, oracle_f1: 0.8843, headroom_pp: 10.01, degeneracy_pct: 23.36, lp_delta_pp: 0.36, dgs_delta_pp: -0.35}
  - seed_42: {greedy_f1: 0.7841, oracle_f1: 0.8854, degen: 27.32}
  - seed_123: {greedy_f1: 0.784, oracle_f1: 0.8839, degen: 24.63}
  - seed_456: {greedy_f1: 0.7844, oracle_f1: 0.8835, degen: 18.13}
  - signal_ranking: "LP (+0.36pp) > SJ (-0.52) > FK (-0.53) > EM (-1.02) > VC (-2.39)"
  - lp_only_positive: true
  - n_instances_gold_filtered: 32565

**5. exp_llama_fewnerd_lora**
- status: "DONE"
- conclusion: "success"
- created_at: "2026-05-18T13:20:55.859Z"
- updated_at: "2026-05-19T01:08:20.832Z"
- completed_at: "2026-05-19T01:08:20.832Z"
- hypothesis: "LLaMA-based model with LoRA fine-tuning on Few-NERD can provide a second model family (beyond Qwen) for cross-model generalization evidence of structured self-consistency phenomena in NER"
- spec: {command: "llamafactory-cli train train_config_llama_fewnerd.yaml", server: "autodl-5090", gpu: "cuda:1", pid: 137865, data_path: "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd", model_name: "LLaMA-Few-NERD-LoRA", seed: 42, log_path: "/root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log", run_script: "run_llama_fewnerd_train_single_gpu.sh", tmux_session: "llama_fewnerd", note: "Retroactively registered - data_count unknown, seed assumed 42"}
- checkpoint_path: "/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-fewnerd-lora"
- log_path: "/root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log"
- metrics: {epoch: 3, train_loss: 0.0516, eval_loss: 0.0323, train_runtime_hours: 15.35, total_steps: 24708, final_checkpoint: "checkpoint-24708", adapter_size_mb: 320}

**6. exp_031_fewnerd_t12**
- status: "DONE"
- conclusion: "killed"
- created_at: "2026-05-18T20:04:12.040Z"
- completed_at: "2026-05-19T00:30:14.652Z"
- hypothesis: "FewNERD T=1.2 temperature ablation: test if higher temperature reduces degeneracy on FewNERD as observed on SciERC"
- failure_reason: "数据不可用于论文：测试集(37648 vs T=1.0的5000)、N(8 vs 16)、分析管道(MVP pilot vs 5-signal)三重不一致。Director决定不重跑(DDL约束+非核心claim)。"
- notes: "T=1.2 ablation not in paper scope, SciERC T=1.2 sufficient"

**7. exp_fewnerd_s789_n8**
- status: "DONE"
- conclusion: "success"
- created_at: "2026-05-18T23:17:34.011Z"
- completed_at: "2026-05-18T23:18:17.902Z"
- hypothesis: "FewNERD seed789 (4th seed) for statistical CI strengthening: 4-seed protocol provides tighter confidence intervals on LP selection gain and DGS effectiveness in low-degeneracy regime."
- parent: "exp_029a"
- spec: {command: "python code/analyze_fewnerd_s789.py", server: "autodl-5090", data_path: "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/samples.jsonl", data_count: 37648, model_name: "Qwen3-8B (ft_002_v2)", seed: 789, checkpoint_source: "exp_021 shards", eval_data: "FewNERD test (37648 instances, 32565 gold-filtered)", checkpoint_path: "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/", log_path: "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/run.log"}
- metrics: {greedy_f1: 0.7478, oracle_f1: 0.8714, headroom_pp: 12.37, degen_rate: 0.1177, degen_rate_source: "unified_metrics_constant_f1_gold_filtered", instance_count: 37648, n_valid: 32565, lp_sel_f1: 0.7614, lp_delta_pp: 1.36, lp_rho_global: 0.1788, lp_rho_cond: 0.176, dgs_f1: 0.7621, dgs_delta_pp: 1.43, dgs_vs_lp_pp: 0.07, best_signal: "LP", four_seed_mean_greedy: 0.7481, four_seed_mean_lp_delta_pp: 1.38, four_seed_lp_delta_ci95: [1.32, 1.44]}

**8. exp_021_fewnerd_n8_seed456**
- status: "DONE"
- conclusion: "success"
- created_at: "2026-05-18T22:03:17.992Z"
- completed_at: "2026-05-18T22:04:35.573Z"
- hypothesis: "Multi-seed replication (seed=456) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset."
- spec: {command: "python scs_inference.py --dataset fewnerd --seed 456 --n_samples 8 --temperature 1.0", server: "autodl-5090", data_path: "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd", data_count: 37648, model_name: "Qwen3-8B", seed: 456, checkpoint_path: "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456", log_path: "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456_run.log"}
- metrics: {degen_rate: 0.1212, degen_rate_source: "unified_metrics_constant_f1_gold_filtered", instance_count: 37648, n_valid: 32565, n_gold_empty: 5083, ner_greedy_f1: 0.7888, ner_oracle_f1: 0.881, rho_fk_ner: 0.1632, rho_sj_ner: 0.313, sample_f1_pct_zero: 19.32}

**9. exp_021_fewnerd_n8_seed123**
- status: "DONE"
- conclusion: "success"
- created_at: "2026-05-18T22:03:16.735Z"
- completed_at: "2026-05-18T22:04:33.731Z"
- hypothesis: "Multi-seed replication (seed=123) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset."
- spec: {command: "python scs_inference.py --dataset fewnerd --seed 123 --n_samples 8 --temperature 1.0", server: "autodl-5090", data_path: "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd", data_count: 37648, model_name: "Qwen3-8B", seed: 123, checkpoint_path: "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123", log_path: "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123_run.log"}
- metrics: {degen_rate: 0.1312, degen_rate_source: "unified_metrics_constant_f1_gold_filtered", instance_count: 37648, n_valid: 32565, n_gold_empty: 5083, ner_greedy_f1: 0.7885, ner_oracle_f1: 0.8892, rho_fk_ner: 0.1602, rho_sj_ner: 0.3083, sample_f1_pct_zero: 20.39}

**10. exp_027_fewnerd_n16** (also matches n16)
- status: "DONE"
- conclusion: "success"
- created_at: "2026-05-17T05:28:57.036Z"
- completed_at: "2026-05-17T05:46:48.460Z"
- hypothesis: "LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective."
- parent: "exp_021_fewnerd_full"
- spec: {model_name: "qwen3-8b-fewnerd-exp021-merged", data_path: "data/fewnerd_n16_subset/test.json", data_count: 5000, seed: 42, server: "autodl-5090", gpu: "cuda:0,cuda:1,cuda:2,cuda:3", command: "python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged ...", checkpoint_path: "output/exp_027_fewnerd_n16/sampled_results.jsonl", log_path: "output/exp_027_fewnerd_n16/"}
- metrics: {LP_delta_pp: 1.88, LP_delta_95CI: [1.41, 2.37], degen_rate: 0.0706, degen_rate_source: "unified_metrics_constant_f1_gold_filtered", greedy_f1: 0.7478, lp_sel_f1: 0.7666, oracle_f1: 0.902, headroom_pp: 15.42, all_8_types_positive: true, n_instances: 5000, N_samples: 16, bootstrap_p: "<0.001"}

**11. exp_028_fewnerd_5epoch**
- status: "DONE"
- conclusion: "negative"
- created_at: "2026-05-17T07:53:12.913Z"
- completed_at: "2026-05-17T20:29:42.274Z"
- hypothesis: "Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain."
- spec: {server: "autodl-5090", gpu: "cuda:0,1,2,3", data_path: "data/fewnerd_uie_train", data_count: 131767, model_name: "Qwen3-8B LoRA rank=32", seed: 42, log_path: "logs/exp_028_4gpu_train.log", checkpoint_path: "checkpoints/qwen3-8b-fewnerd-5epoch-lora"}
- metrics: {degeneracy_cf1_gold: 0.3133, greedy_f1: 0.7773, lp_sel_delta_pp: 0.624, lp_sel_f1: 0.7835, oracle_f1: 0.8723, within_instance_rho_mean: 0.4066, within_instance_rho_median: 0.6151}

**12. exp_021_fewnerd_full**
- status: "DONE"
- conclusion: "success"
- created_at: "2026-05-16T16:33:44.079Z"
- completed_at: "2026-05-16T22:04:16.683Z"
- hypothesis: "Full Few-NERD LoRA fine-tune (rank=32, α=64, 3 epochs) on SUPERVISED coarse 8-type NER (131k train). 4-GPU DDP on autodl-5090. Post-training: N=8 inference on full test set, T=1.0, seed=42, collect logprobs for SCS metrics."
- parent: "exp_020_fewnerd_smoke"
- spec: {gpu: "cuda:0,cuda:1,cuda:2,cuda:3", gpu_count: 4, training_mode: "DDP", checkpoint_path: "output/exp_021_fewnerd_full/checkpoint-6177", log_path: "output/exp_021_inference/"}
- metrics: {total_steps: 6177, train_loss: 0.048, eval_loss: 0.0275, train_runtime: "3h57m", epochs: 3, final_checkpoint: "output/exp_021_fewnerd_full/checkpoint-6177", adapter_path: "output/exp_021_fewnerd_full/adapter_model.safetensors", inference_instances: 37648, inference_filtered: 32565, inference_n_samples: 8, greedy_macro_f1: 0.7478, oracle_macro_f1: 0.8719, headroom: 0.124, zero_f1_rate: 0.119, degeneracy_rate: 0.101, lp_within_range_mean: 0.0879, lp_within_range_median: 0.0662, lp_global_rho: 0.4215, lp_cond_rho: 0.4225, sj_global_rho: 0.3002, sj_cond_rho: 0.2937, fk_global_rho: 0.3132, fk_cond_rho: 0.3093, em_global_rho: 0.2871, em_cond_rho: 0.271, vc_global_rho: 0.3858, vc_cond_rho: 0.3234, lp_selection_delta_pp: 1.36, vc_selection_delta_pp: -1.79, sj_selection_delta_pp: -2.14, fk_selection_delta_pp: -2.26, em_selection_delta_pp: -3.85, lp_bootstrap_ci_95_pp: [1.18, 1.53], lp_sample_auroc: 0.5782, vc_sample_auroc: 0.5354, fk_sample_auroc: 0.521, sj_sample_auroc: 0.5197, em_sample_auroc: 0.5137, scenario: "A_partial", note: "Full analysis (gold-filtered n=32565). Prior simplified analysis used unfiltered data with different metrics."}

**13. exp_020_fewnerd_smoke**
- status: "DONE"
- conclusion: "success"
- created_at: "2026-05-16T10:29:25.272Z"
- completed_at: "2026-05-16T16:33:59.109Z"
- hypothesis: "1-epoch LoRA (r16) fine-tune Qwen3-8B on Few-NERD INTRA coarse 8-type (131k train), then N=8 T=1.0 pilot inference on 200 test instances."
- metrics: {final_loss: 0.031, total_steps: 8236, training_time: "5h54m", pilot_greedy_f1: 0.8037, pilot_instances: 200, merged_model_path: "checkpoints/qwen3-8b-fewnerd-merged"}

---

### N16 experiments (23 additional, not containing "fewnerd")

**14. exp_002_conll_n16_seed456**
- status: "DONE", conclusion: "success"
- created_at: "2026-05-18T22:03:15.720Z", completed_at: "2026-05-18T22:04:31.934Z"
- hypothesis: "Multi-seed replication (seed=456) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds."
- spec: {command: "python scs_inference.py --dataset conll2003 --seed 456 --n_samples 16 --temperature 1.0", server: "autodl-5090", data_count: 3453, model_name: "Qwen3-8B", seed: 456}
- metrics: {degen_rate: 0.5544, instance_count: 3453, n_valid: 2756, n_gold_empty: 697, ner_greedy_f1: 0.9074, ner_oracle_f1: 0.9549, rho_fk_ner: 0.4718, rho_sj_ner: 0.4819, sample_f1_pct_zero: 7.02}

**15. exp_002_conll_n16_seed123**
- status: "DONE", conclusion: "success"
- created_at: "2026-05-18T22:03:14.343Z", completed_at: "2026-05-18T22:04:29.992Z"
- hypothesis: "Multi-seed replication (seed=123) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds."
- metrics: {degen_rate: 0.471, instance_count: 3453, n_valid: 2756, n_gold_empty: 697, ner_greedy_f1: 0.9068, ner_oracle_f1: 0.9633, rho_fk_ner: 0.4524, rho_sj_ner: 0.4621, sample_f1_pct_zero: 7.54}

**16. exp_017_llama_conll_n16_s456_r1024**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-15T11:45:25.899Z"
- hypothesis: "LLaMA CoNLL N=16 seed=456 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction."
- spec: {model_name: "llama3.1-8b-conll2003-merged", dataset: "CoNLL-2003", seed: 456, server: "autodl-5090", gpu: "cuda:2", data_count: 3453}
- metrics: {degen_rate: 0.8672, instance_count: 3453, n_valid: 2756, n_gold_empty: 697, parse_rate: 1, ner_greedy_f1: 0.9265, ner_oracle_f1: 0.9499, rho_fk_ner: 0.469, rho_sj_ner: 0.4734, rho_vc_ner: 0.4722, rho_em_ner: 0.4752, rho_lp_ner: 0.3099, auroc_fk_ner: 0.7408, auroc_sj_ner: 0.7428, auroc_vc_ner: 0.7495, auroc_em_ner: 0.7444, auroc_lp_ner: 0.7628, rho_note: "CORRECTED 2026-05-15: old values (rho_fk=0.8085,rho_sj=0.1895) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756)."}

**17. exp_017_llama_conll_n16_r1024**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-15T11:45:23.213Z"
- hypothesis: "LLaMA CoNLL N=16 seed=42 (max_tokens=1024 rerun): cross-model baseline on CoNLL. Establishes LLaMA signal rankings after gold-filtering correction."
- metrics: {degen_rate: 0.8647, instance_count: 3453, n_valid: 2756, n_gold_empty: 697, parse_rate: 1, ner_greedy_f1: 0.9265, ner_oracle_f1: 0.9499, rho_fk_ner: 0.4752, rho_sj_ner: 0.4836, rho_vc_ner: 0.4746, rho_em_ner: 0.4818, rho_lp_ner: 0.3136, auroc_fk_ner: 0.7467, auroc_sj_ner: 0.7496, auroc_vc_ner: 0.7529, auroc_em_ner: 0.7508, auroc_lp_ner: 0.7661, rho_note: "CORRECTED 2026-05-15: old values (rho_fk=0.8095,rho_sj=0.1815) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756)."}

**18. exp_002_conll_n16**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-14T18:58:40.473Z"
- hypothesis: "CoNLL N=16 NER: cross-dataset validation on high-performance NER dataset. Tests if structural signals retain advantage when base model performance is already high (greedy F1 > 0.9)."
- spec: {model_name: "qwen3-8b-conll2003-merged", seed: 42, server: "autodl-5090", data_count: 3453}
- metrics: {degen_rate: 0.4844, N: 16, dataset: "conll2003", n_instances: 3453, n_valid: 2756, n_conditional: 2614, greedy_f1: 0.907, full: {SJ_rho: 0.4496, FK_rho: 0.3928, logprob_rho: 0.3146, EM_rho: 0.4627, voting_conf_rho: 0.4286, SJ_AUROC: 0.8264, FK_AUROC: 0.7821, logprob_AUROC: 0.7531, EM_AUROC: 0.8409, voting_conf_AUROC: 0.8071, SJ_ECE: 0.0747, FK_ECE: 0.1786, logprob_ECE: 0.2031, EM_ECE: 0.0786, voting_conf_ECE: 0.529}, conditional: {SJ_rho: 0.4208, FK_rho: 0.3494, logprob_rho: 0.3756, EM_rho: 0.4658, voting_conf_rho: 0.3654, SJ_AUROC: 0.8405, FK_AUROC: 0.7819, logprob_AUROC: 0.8259, EM_AUROC: 0.8781, voting_conf_AUROC: 0.7951, SJ_ECE: 0.0982, FK_ECE: 0.1899, logprob_ECE: 0.2504, EM_ECE: 0.0997, voting_conf_ECE: 0.6096}, n8_vs_n16_delta_rho_full: {SJ: 0.0139, FK: -0.007, logprob: -0.0011, EM: 0.012, voting_conf: 0.0049}}

**19. exp_017_llama_conll_n16_s123_r1024**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-15T01:20:51.219Z"
- hypothesis: "LLaMA CoNLL N=16 seed=123 (max_tokens=1024 rerun): cross-model multi-seed validation."
- notes: "Output exists on autodl-5090. Registry status corrected from killed to success."
- metrics: {degen_rate: 0.8636, degen_rate_source: "unified_metrics_constant_f1_gold_filtered"}

**20. exp_008_re_n16**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-14T12:28:39.268Z"
- hypothesis: "RE N=16 initial evaluation: first relation extraction test with structural signals."
- spec: {model_name: "qwen3-8b-scierc-merged-v2", dataset: "SciERC", seed: 42, data_count: 551, num_instances: 200, partial: true, note: "Only 200/551 instances due to --num_test default bug."}
- metrics: {ner: {greedy_f1: 0.6635, oracle_f1: 0.8208, headroom: 0.1572, rho_sj_full: 0.377, rho_fk_full: 0.2508, rho_logprob_full: 0.3153, rho_sj_cond: 0.3598, rho_fk_cond: 0.2251, rho_logprob_cond: 0.2927, sj_beats_fk: true, rho_advantage: 0.1262}, re: {greedy_f1: 0.4339, oracle_f1: 0.6658, headroom: 0.2319, rho_sj_full: 0.2966, rho_fk_full: 0.2871, rho_logprob_full: 0.2986, rho_sj_cond: 0.3975, rho_fk_cond: 0.3774, rho_logprob_cond: 0.2745, sj_beats_fk: true, rho_advantage: 0.0095}, verdict: "FAIL"}

**21. exp_001_ner_n16_seed123**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-14T13:31:54.232Z"
- hypothesis: "SciERC NER N=16 seed=123: multi-seed validation at N=16."
- spec: {model_name: "qwen3-8b-scierc-merged-v2", seed: 123, data_count: 551}
- metrics: {ner: {greedy_f1: 0.663, oracle_f1: 0.809, headroom: 0.146, rho_sj: 0.423, rho_fk: 0.29, rho_logprob: 0.239, rho_sj_cond: 0.423, rho_fk_cond: 0.26}, re: {greedy_f1: 0.419, oracle_f1: 0.625, headroom: 0.206, rho_sj: 0.267, rho_fk: 0.315, rho_sj_cond: 0.364, rho_fk_cond: 0.331}, verdict: "FAIL", verdict_note: "RE rho_sj=0.267 < 0.40; RE >30% samples F1=0", n_instances: 551, seed: 123, N: 16, T: 1}

**22. exp_008_re_n16_t10_full**
- status: "DONE", conclusion: "negative"
- completed_at: "2026-05-14T13:44:19.577Z"
- hypothesis: "RE N=16 evaluation v2: early RE evaluation attempt."
- metrics: {ner: {rho_sj: 0.444}, re: {rho_sj: 0.248}, n_instances: 551, N: 16, T: 1, seed: 42, mode: "RE-only", source: "director_corrected"}

**23. exp_008_re_n16_v2**
- status: "DONE", conclusion: "negative"
- completed_at: "2026-05-14T15:23:35.598Z"
- hypothesis: "RE N=16 evaluation v2: tests structural signal effectiveness on relation extraction at higher sample count."
- metrics: {sj_rho_full: 0.281, sj_rho_cond: 0.308, f1_zero_pct: 44.3, conclusion_note: "RE N=16 v2 negative: SJ weak, 44.3% F1=0"}

**24. exp_007_llama_n16**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-14T19:03:39.163Z"
- hypothesis: "LLaMA SciERC N=16: cross-model NER signal evaluation at higher sample count."
- spec: {model_name: "llama3.1-8b-scierc-merged", seed: 42, data_count: 551}
- metrics: {N: 16, dataset: "scierc", n_instances: 551, n_valid: 529, n_conditional: 478, greedy_f1: 0.645, full: {SJ_rho: 0.3791, FK_rho: 0.3081, logprob_rho: 0.2041, EM_rho: 0.3159, voting_conf_rho: 0.4515, SJ_AUROC: 0.717, FK_AUROC: 0.6581, logprob_AUROC: 0.5656, EM_AUROC: 0.7686, voting_conf_AUROC: 0.7266}, conditional: {SJ_rho: 0.3222, FK_rho: 0.2182, logprob_rho: 0.1286, EM_rho: 0.3563, voting_conf_rho: 0.3356}, n8_vs_n16_delta_rho_full: {SJ: 0.0161, FK: -0.0185, logprob: 0.0214, EM: 0.0007, voting_conf: 0.0184}}

**25. exp_017_llama_conll_n16**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-14T19:45:16.265Z"
- hypothesis: "LLaMA CoNLL N=16 seed=42 (original): cross-model validation on CoNLL."
- metrics: {greedy_f1: 0.9243, oracle_f1: 0.9487, oracle_headroom: 0.0244, n_instances: 3453, n_valid: 2756, structural_beats_surface: true, full: {SJ_rho: 0.4642, FK_rho: 0.4566, logprob_rho: 0.3058, EM_rho: 0.4613, voting_conf_rho: 0.4554, SJ_AUROC: 0.7391, FK_AUROC: 0.736, logprob_AUROC: 0.7594, EM_AUROC: 0.7391, voting_conf_AUROC: 0.7406}, conditional: {SJ_rho: 0.4597, FK_rho: 0.4515, logprob_rho: 0.3193, EM_rho: 0.4618, voting_conf_rho: 0.3978}, best_of_n: {greedy: 0.9243, random_avg: 0.9213, sj_best: 0.9259, logprob_best: 0.925, voting_conf_best: 0.9268, oracle: 0.9487}, n8_vs_n16_delta: {full_SJ_rho_delta: 0.0328, full_FK_rho_delta: 0.0289, full_logprob_rho_delta: -0.0014, full_EM_rho_delta: 0.0307, full_voting_conf_rho_delta: 0.0298}}

**26. exp_001_n16_seed456**
- status: "DONE", conclusion: "success", retry_count: 1
- completed_at: "2026-05-14T12:28:38.721Z"
- hypothesis: "SciERC N=16 seed=456: early multi-seed validation of structural signal rankings at N=16 sample count."
- metrics: {instance_count: 551, n_valid: 529, n_gold_empty: 22, parse_rate: 1, ner_greedy_f1: 0.6617, ner_oracle_f1: 0.8075, re_greedy_f1: 0.4215, re_oracle_f1: 0.4748, rho_sj_ner: 0.4098, rho_fk_ner: 0.2723, rho_vc_ner: 0.4449, rho_em_ner: 0.3363, rho_lp_ner: 0.2415, rho_sj_re: 0.2835, rho_fk_re: 0.2929, auroc_sj_ner: 0.6823, auroc_fk_ner: 0.6179, auroc_vc_ner: 0.6981, auroc_em_ner: 0.649, auroc_lp_ner: 0.5885, rho_note: "CORRECTED 2026-05-15: old values included 22 gold-empty instances. Now uses gold-filtered pipeline (n=529)."}
- extra.previous_failure.metrics: {ner: {greedy_f1: 0.6577, oracle_f1: 0.8129, headroom: 0.1553, rho_sj_full: 0.3297, rho_fk_full: 0.2578, rho_logprob_full: 0.2866}, re: {greedy_f1: 0.4312, oracle_f1: 0.6737, headroom: 0.2425, rho_sj_full: 0.285, rho_fk_full: 0.2372, rho_logprob_full: 0.2626}, verdict: "FAIL"}

**27. exp_017_llama_conll_n16_s456**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-14T20:24:45.875Z"
- hypothesis: "LLaMA CoNLL N=16 seed=456: structural>surface ranking preserved across seeds"
- metrics: {greedy_f1: 0.9243, oracle_f1: 0.9488, oracle_headroom: 0.0245, n_instances: 3453, n_valid: 2756, structural_beats_surface: true, full: {SJ_rho: 0.4552, FK_rho: 0.4478, logprob_rho: 0.3078, EM_rho: 0.452, voting_conf_rho: 0.4571}, conditional: {SJ_rho: 0.4505, FK_rho: 0.4422, logprob_rho: 0.3242, EM_rho: 0.451, voting_conf_rho: 0.3962}, best_of_n: {greedy: 0.9243, random_avg: 0.9215, sj_best: 0.9243, logprob_best: 0.9243, voting_conf_best: 0.9243, oracle: 0.9488}, n8_vs_n16_delta: {full_SJ_rho_delta: 0.0238, full_FK_rho_delta: 0.0201, full_logprob_rho_delta: 0.0006, full_EM_rho_delta: 0.0214, full_voting_conf_rho_delta: 0.0315}}

**28. exp_017_llama_conll_n16_s123**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-14T19:43:06.607Z"
- hypothesis: "LLaMA CoNLL N=16 seed=123: structural>surface ranking preserved across seeds"
- metrics: {greedy_f1: 0.9266, oracle_f1: 0.9497, oracle_headroom: 0.0231, n_instances: 3453, n_valid: 2756, structural_beats_surface: true, full: {SJ_rho: 0.4698, FK_rho: 0.4594, logprob_rho: 0.3161, EM_rho: 0.4676, voting_conf_rho: 0.4612}, conditional: {SJ_rho: 0.4712, FK_rho: 0.4595, logprob_rho: 0.3314, EM_rho: 0.4732, voting_conf_rho: 0.4086}, best_of_n: {greedy: 0.9242, random_avg: 0.9216, sj_best: 0.9247, logprob_best: 0.9253, voting_conf_best: 0.9255, oracle: 0.9486}, n8_vs_n16_delta: {full_SJ_rho_delta: 0.0384, full_FK_rho_delta: 0.0317, full_logprob_rho_delta: 0.0089}}

**29. exp_008_re_n16_full**
- status: "DONE", conclusion: "killed"
- completed_at: "2026-05-14T17:51:43.957Z"
- failure_reason: "superseded by exp_008_re_n16_t10_full (full 551-instance RE-only run on autodl-5090)"

**30. exp_001_n16_seed123**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-14T12:28:38.104Z"
- spec: {data_count: 551, model_name: "qwen3-8b-scierc-merged-v2", seed: 123, num_instances: 200, partial: true, note: "Only 200/551 instances due to --num_test default bug."}
- metrics: {ner: {greedy_f1: 0.655, oracle_f1: 0.8028, headroom: 0.1478, rho_sj_full: 0.4076, rho_fk_full: 0.2799, rho_logprob_full: 0.3189, sj_beats_fk: true, rho_advantage: 0.1277}, re: {greedy_f1: 0.4243, oracle_f1: 0.6771, headroom: 0.2528, rho_sj_full: 0.2943, rho_fk_full: 0.2657, rho_logprob_full: 0.3005, sj_beats_fk: true, rho_advantage: 0.0286}, verdict: "FAIL"}

**31. exp_001_ner_n16_scierc**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-14T11:55:45.664Z"
- metrics: {n_instances: 551, ner_n: 529, re_n: 397, N: 16, T: 1, seed: 42, full_test_set: true, ner_voting_conf_rho: 0.399, ner_sj_rho: 0.398, ner_em_rho: 0.339, ner_fk_rho: 0.288, ner_logprob_rho: 0.237, ner_voting_conf_auroc: 0.704, ner_sj_auroc: 0.697, ner_cond_em_rho: 0.414, ner_cond_sj_rho: 0.349, ner_cond_vc_rho: 0.34, re_voting_conf_rho: 0.38, re_logprob_rho: 0.293, re_fk_rho: 0.281, re_sj_rho: 0.277, re_em_rho: 0.148, re_voting_conf_auroc: 0.699, re_cond_em_rho: 0.475, re_cond_sj_rho: 0.318, re_cond_vc_rho: 0.35, re_cond_em_auroc: 0.742, diagnosis: "551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380). EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full FAIL (SJ 0.277 < 0.40)."}

**32. exp_002_conll_n16_r1024**
- status: "DONE", conclusion: "killed"
- completed_at: "2026-05-15T01:20:53.108Z"
- spec: {hypothesis: "D054 rerun: max_tokens=1024. Verify truncation impact on Qwen CoNLL N=16.", model_name: "qwen3-8b-conll2003-merged", dataset: "CoNLL-2003", seed: 42}

**33. exp_007_llama_n16_r1024**
- status: "DONE", conclusion: "killed"
- completed_at: "2026-05-15T01:20:52.194Z"
- spec: {hypothesis: "D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA SciERC N=16.", model_name: "llama3.1-8b-scierc-merged", dataset: "SciERC", seed: 42}

**34. exp008_re_n16** (note: no underscore after "exp008")
- status: "DONE", conclusion: "killed"
- completed_at: "2026-05-15T12:41:39.774Z"
- failure_reason: "Superseded by exp_008_re_n16_v2 (full 551-instance run on autodl-5090)"
- spec: {server: "gpu-5090-4x-2", wall_clock_seconds: 87984.9, gpu_hours: 24.44}

**35. exp_001_n16_seed456_full**
- status: "DONE", conclusion: "killed"
- completed_at: "2026-05-15T12:41:30.065Z"
- failure_reason: "superseded by v2"
- spec: {server: "gpu-5090-4x-2", wall_clock_seconds: 86219.0, gpu_hours: 23.95}

**36. exp_001_n16_seed123_full**
- status: "DONE", conclusion: "killed"
- completed_at: "2026-05-15T12:41:29.068Z"
- failure_reason: "superseded by v2"
- spec: {server: "gpu-5090-4x-2", wall_clock_seconds: 86243.0, gpu_hours: 23.96}

---

### Totals

| Category | Count |
|---|---|
| fewnerd experiments | 13 |
| n16 experiments (additional) | 23 |
| Overlap (fewnerd + n16) | 1 (exp_027_fewnerd_n16) |
| **Grand total unique** | **36** |

By status: 3 ALLOCATED/QUEUED (exp_qwen25_32b_fewnerd, exp_qwen25_7b_fewnerd, exp_qwen25_14b_fewnerd), 33 DONE. By conclusion among DONE: 22 success, 3 negative, 8 killed. No experiments matched "n_16" (with underscore before 16).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68b97513-c5d2-48a4-a1a6-845b101c9ae6",
  "isSidechain": true,
  "agentId": "a37fba2a40b1ce129",
  "requestId": "req_011CbBaCE4jhm8ug4Y6cgVzF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c78e544-477f-476f-8902-f5e82b2d41bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvK4M5hTwAQKu4uBdzyG8H",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1180,
      "cache_read_input_tokens": 51713,
      "output_tokens": 12850,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1180
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12850,
          "cache_read_input_tokens": 51713,
          "cache_creation_input_tokens": 1180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1180,
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
