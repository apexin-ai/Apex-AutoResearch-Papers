# Research conversation: I need you to extract the FULL eval command for every 4B eval experiment from the registry file. The file is at: /home/u

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a35180a8a436e895f.jsonl`
- **Structured JSON:** [`55e2d59eab147acffcab.json`](../../sessions/55/55e2d59eab147acffcab.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

38 recorded events

### User

_source line 1 · 2026-05-18T22:05:12.792Z_

I need you to extract the FULL eval command for every 4B eval experiment from the registry file.

The file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt

It's JSON with schema: {result: string} where result is a JSON string containing an array of experiment objects.

Use Python to parse and extract. For EVERY experiment that:
1. References Qwen3-4B in its spec
2. AND is an "eval" experiment (exp_id contains "eval" or the experiment type/purpose is evaluation)

Extract and print:
- exp_id
- status
- conclusion
- metrics (especially ign_f1)
- The FULL spec.command string (do NOT truncate)
- notes/error if any

I need to check D076 protocol compliance for each eval:
- batch_size=4
- max_new_tokens=1024
- seed=42
- --no-quantize present
- --model_path points to base model (Qwen3-4B)
- --sft_adapter points to adapter

For each eval, parse the command and check each D076 parameter. Output a table with columns:
exp_id | ign_f1 | batch_size | max_new_tokens | seed | no_quantize | model_path | sft_adapter | D076_compliant | non_compliance_reasons

Be exhaustive - include ALL eval experiments, even failed ones. Include the full command string for each.

Also specifically look for:
- Any eval that uses --model_path pointing to an adapter directory instead of base model
- Any eval missing --no-quantize
- Any eval with different batch_size or max_new_tokens
- Any eval for SFT s42 (the original seed) - what adapter path does it use?

Write a Python script to do this analysis and run it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "23faa4e2-0c97-47f8-be9e-f272ba775828",
  "agentId": "a35180a8a436e895f",
  "type": "user",
  "uuid": "30534343-ad0c-4659-a8ea-3fea992379ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T22:05:12.796Z_

```json
{
  "parentUuid": "30534343-ad0c-4659-a8ea-3fea992379ba",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
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
  "uuid": "737aa509-39d5-43f4-9bc8-93863718c978",
  "timestamp": "2026-05-18T22:05:12.796Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T22:05:15.574Z_



I'll start by reading the file to understand its structure, then write a Python script to do the full analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "737aa509-39d5-43f4-9bc8-93863718c978",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAnvq8SrTzXHJ7f7NoB1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f8914cc-2cc1-43a9-8035-a6a26143d643",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QN46myk35YftPfosyCgjr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7889,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7889,
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

_source line 4 · 2026-05-18T22:05:16.688Z_

<details open><summary>🔧 Tool call — Read · `toolu_019myGo3GDdxEvUCPQieS48V`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f8914cc-2cc1-43a9-8035-a6a26143d643",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAnvq8SrTzXHJ7f7NoB1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "469ce32a-047b-4d32-be9d-176e1c9303d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QN46myk35YftPfosyCgjr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7889,
      "cache_read_input_tokens": 8249,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7889
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 184,
          "cache_read_input_tokens": 8249,
          "cache_creation_input_tokens": 7889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7889,
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

_source line 5 · 2026-05-18T22:05:16.968Z_

<details><summary>↩ Tool result · reported error · `toolu_019myGo3GDdxEvUCPQieS48V`</summary>

```text
File content (177098 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "469ce32a-047b-4d32-be9d-176e1c9303d5",
  "isSidechain": true,
  "promptId": "23faa4e2-0c97-47f8-be9e-f272ba775828",
  "agentId": "a35180a8a436e895f",
  "type": "user",
  "uuid": "d54d8da2-9406-4c42-8cd4-ddeea24b6186",
  "toolUseResult": "Error: File content (177098 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "469ce32a-047b-4d32-be9d-176e1c9303d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T22:05:19.663Z_

The file is very large. Let me search for the structure and 4B eval experiments specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d54d8da2-9406-4c42-8cd4-ddeea24b6186",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAnw91E75K4hfpV4zWow",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8814ee14-9cb3-4023-aefd-b84fe402acb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017bsBD9Yia5W4DVhmRVzfhc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1086,
      "cache_read_input_tokens": 16138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1086,
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

_source line 7 · 2026-05-18T22:05:20.295Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Fc5bzeeigDrs9XGsgqDERi`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt",
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8814ee14-9cb3-4023-aefd-b84fe402acb3",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAnw91E75K4hfpV4zWow",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12d082a4-d783-4d4a-a4c8-9adef49f16d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017bsBD9Yia5W4DVhmRVzfhc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1086,
      "cache_read_input_tokens": 16138,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1086
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 16138,
          "cache_creation_input_tokens": 1086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1086,
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

_source line 8 · 2026-05-18T22:05:20.741Z_

<details><summary>↩ Tool result · reported error · `toolu_01Fc5bzeeigDrs9XGsgqDERi`</summary>

```text
File content (177098 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12d082a4-d783-4d4a-a4c8-9adef49f16d3",
  "isSidechain": true,
  "promptId": "23faa4e2-0c97-47f8-be9e-f272ba775828",
  "agentId": "a35180a8a436e895f",
  "type": "user",
  "uuid": "ecde8619-d5d3-40a9-b35f-0735c6f7ed54",
  "toolUseResult": "Error: File content (177098 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "12d082a4-d783-4d4a-a4c8-9adef49f16d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T22:05:23.985Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GEXh7N9FbLoxKCDhGzEa2P`</summary>

```json
{
  "command": "wc -l \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt\"",
  "description": "Count lines in registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecde8619-d5d3-40a9-b35f-0735c6f7ed54",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAnwR9LPRgxVLJ7L5tP3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e72e289e-a044-4f26-b77b-7f4828513fe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HY1SvYSgvY3bbBKJXRD9GM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 241,
      "cache_read_input_tokens": 17224,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 241
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 17224,
          "cache_creation_input_tokens": 241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 241,
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

_source line 10 · 2026-05-18T22:05:24.108Z_

<details><summary>↩ Tool result · `toolu_01GEXh7N9FbLoxKCDhGzEa2P`</summary>

```text
0 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e72e289e-a044-4f26-b77b-7f4828513fe3",
  "isSidechain": true,
  "promptId": "23faa4e2-0c97-47f8-be9e-f272ba775828",
  "agentId": "a35180a8a436e895f",
  "type": "user",
  "uuid": "ef8efb58-f8b0-4f66-91da-9fe07bfdf6df",
  "sourceToolAssistantUUID": "e72e289e-a044-4f26-b77b-7f4828513fe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-18T22:05:26.867Z_

It's a single line (JSON). Let me write a Python script to parse and analyze it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef8efb58-f8b0-4f66-91da-9fe07bfdf6df",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAnwfaza3t9HxbbbVU4K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b91960fd-5a44-4788-a24b-42058eadccc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8wmmYPSppp7PNiLsRkz67",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 17465,
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

_source line 12 · 2026-05-18T22:05:31.254Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gbdrd988GgTGGgbNnXYd3H`</summary>

```json
{
  "command": "python3 -c \"\nimport json, sys\n\nfpath = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt'\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\n# The outer structure is {result: string}\nresult_str = raw.get('result', raw)\nif isinstance(result_str, str):\n    data = json.loads(result_str)\nelse:\n    data = result_str\n\nprint(f'Type of data: {type(data)}')\nif isinstance(data, list):\n    print(f'Number of experiments: {len(data)}')\n    if data:\n        print(f'Keys in first entry: {list(data[0].keys())}')\nelif isinstance(data, dict):\n    print(f'Top-level keys: {list(data.keys())}')\n    for k,v in data.items():\n        if isinstance(v, list):\n            print(f'  {k}: list of {len(v)} items')\n            if v:\n                print(f'  Keys in first item: {list(v[0].keys())}')\n\"\n",
  "description": "Parse registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b91960fd-5a44-4788-a24b-42058eadccc0",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAnwfaza3t9HxbbbVU4K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0048e621-4e3f-445c-9983-59bd358a5a36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8wmmYPSppp7PNiLsRkz67",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 17465,
      "output_tokens": 442,
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
          "output_tokens": 442,
          "cache_read_input_tokens": 17465,
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

_source line 13 · 2026-05-18T22:05:31.359Z_

<details><summary>↩ Tool result · `toolu_01Gbdrd988GgTGGgbNnXYd3H`</summary>

```text
Type of data: &lt;class 'dict'>
Top-level keys: ['success', 'data', 'error', 'metadata']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0048e621-4e3f-445c-9983-59bd358a5a36",
  "isSidechain": true,
  "promptId": "23faa4e2-0c97-47f8-be9e-f272ba775828",
  "agentId": "a35180a8a436e895f",
  "type": "user",
  "uuid": "3a6b3b02-850e-409b-9a38-43eb2edc210e",
  "sourceToolAssistantUUID": "0048e621-4e3f-445c-9983-59bd358a5a36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T22:05:37.539Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MuBrtQeLLV6QcVespKfZwb`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nfpath = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt'\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\nresult_str = raw.get('result', raw)\nif isinstance(result_str, str):\n    data = json.loads(result_str)\nelse:\n    data = result_str\n\nexperiments = data.get('data', data)\nif isinstance(experiments, dict):\n    # Maybe experiments is under another key\n    for k, v in experiments.items():\n        print(f'{k}: {type(v)}')\n        if isinstance(v, list):\n            print(f'  len={len(v)}')\n            if v:\n                print(f'  first item keys: {list(v[0].keys()) if isinstance(v[0], dict) else type(v[0])}')\n        elif isinstance(v, dict):\n            print(f'  keys: {list(v.keys())[:10]}')\n        else:\n            print(f'  value: {str(v)[:200]}')\n\"\n",
  "description": "Explore nested data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a6b3b02-850e-409b-9a38-43eb2edc210e",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAnxCZaJRPF6t2EZoifh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d92ebc98-1b76-4f52-9e0e-f24bb16f9bc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E6HPeZzqT2SbXe9VSExP5D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 485,
      "cache_read_input_tokens": 17736,
      "output_tokens": 418,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 485
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 418,
          "cache_read_input_tokens": 17736,
          "cache_creation_input_tokens": 485,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 485,
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

_source line 15 · 2026-05-18T22:05:37.644Z_

<details><summary>↩ Tool result · `toolu_01MuBrtQeLLV6QcVespKfZwb`</summary>

```text
experiments: &lt;class 'dict'>
  keys: ['wave1_sft_4b_s44_eval_r2', 'plan019_8b_sft_s44_eval', 'wave1_sft_4b_s43_eval_r2', 'plan019_1_7b_sft_s43_eval', 'plan019_8b_sft_s44', 'plan019_1_7b_sft_s43_r2', 'grpo_bf16_g4_ckpt200_eval', 'wave1_grpo_bf16_g4', 'random_rsft_k1_eval', 'grpo_bf16_g4_ckpt100_eval']
count: &lt;class 'int'>
  value: 222
total: &lt;class 'int'>
  value: 222
baseline: &lt;class 'NoneType'>
  value: None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d92ebc98-1b76-4f52-9e0e-f24bb16f9bc0",
  "isSidechain": true,
  "promptId": "23faa4e2-0c97-47f8-be9e-f272ba775828",
  "agentId": "a35180a8a436e895f",
  "type": "user",
  "uuid": "028f6977-aec5-4c7d-bed2-63643ef0baef",
  "sourceToolAssistantUUID": "d92ebc98-1b76-4f52-9e0e-f24bb16f9bc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T22:05:42.608Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QBvVMyarzFmXbJcbJhgAoy`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nfpath = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt'\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\nresult_str = raw.get('result', raw)\nif isinstance(result_str, str):\n    data = json.loads(result_str)\nelse:\n    data = result_str\n\nexperiments = data['data']['experiments']\n\n# Look at one experiment to see its structure\nfirst_key = list(experiments.keys())[0]\nexp = experiments[first_key]\nprint(f'Experiment: {first_key}')\nprint(f'Keys: {list(exp.keys())}')\nprint(json.dumps(exp, indent=2)[:3000])\n\"\n",
  "description": "Examine single experiment structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "028f6977-aec5-4c7d-bed2-63643ef0baef",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAnxfQMu7N6SfytB8iEa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ded5c957-aef1-49b5-b5c6-31d7e24971f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E9mdhW4Hz2fdEUoD9nHhj1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 654,
      "cache_read_input_tokens": 18221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 654,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 17 · 2026-05-18T22:05:42.734Z_

<details><summary>↩ Tool result · `toolu_01QBvVMyarzFmXbJcbJhgAoy`</summary>

```text
Experiment: wave1_sft_4b_s44_eval_r2
Keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'reproduce', 'extra']
{
  "status": "ANALYZING",
  "retry_count": 0,
  "created_at": "2026-05-18T20:05:57.119Z",
  "updated_at": "2026-05-18T21:59:29.645Z",
  "hypothesis": "4B SFT seed44 eval r2 (corrected D076 command: --model_path=base --sft_adapter=adapter). Re-run of failed wave1_sft_4b_s44_eval. Expected rel_f1 ~50.5 based on canonical 4B SFT s42.",
  "parent": "wave1_sft_4b_s44",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_seed44/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/wave1_sft_4b_s44_eval_r2\"",
    "server": "rtx5090-4x",
    "gpu": [
      "cuda:1"
    ],
    "pid": "571192",
    "log_path": "~/runs/faith-evidence-ie/wave1_sft_4b_s44_eval_r2.log",
    "submitted_at": "2026-05-18T20:06:13.257Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/autodl-tmp/data/docred",
    "data_count": 985,
    "model_name": "Qwen3-4B + SFT-s44",
    "seed": 42,
    "checkpoint_source": "wave1_sft_4b_s44",
    "eval_data": "DocRED dev",
    "checkpoint_path": "/root/autodl-tmp/eval_results/wave1_sft_4b_s44_eval_r2"
  },
  "reproduce": {
    "finished_at": "2026-05-18T21:59:27.684Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-18T21:59:33.106103+00:00"
      }
    ]
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ded5c957-aef1-49b5-b5c6-31d7e24971f0",
  "isSidechain": true,
  "promptId": "23faa4e2-0c97-47f8-be9e-f272ba775828",
  "agentId": "a35180a8a436e895f",
  "type": "user",
  "uuid": "4e430f4d-38df-4ecf-b9f6-9ec22b31d049",
  "sourceToolAssistantUUID": "ded5c957-aef1-49b5-b5c6-31d7e24971f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-18T22:05:45.066Z_

Good, now I understand the structure. Let me write the comprehensive analysis script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e430f4d-38df-4ecf-b9f6-9ec22b31d049",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAny3TfBR3vGY7UyfYrF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5026426-c18d-44fa-8796-1799dd6ef7bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNEiC75nPnzZGc9WpLM4Mk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1138,
      "cache_read_input_tokens": 18875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1138,
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

_source line 19 · 2026-05-18T22:06:39.828Z_

<details open><summary>🔧 Tool call — Write · `toolu_015awc5JNyFhDZQXUx7fqLb7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/d076_eval_audit.py",
  "content": "#!/usr/bin/env python3\n\"\"\"D076 Protocol Compliance Audit for all 4B eval experiments.\"\"\"\n\nimport json\nimport re\nimport sys\n\nfpath = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt'\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\nresult_str = raw.get('result', raw)\nif isinstance(result_str, str):\n    data = json.loads(result_str)\nelse:\n    data = result_str\n\nexperiments = data['data']['experiments']\n\n# Collect all 4B eval experiments\neval_exps = []\nfor exp_id, exp in experiments.items():\n    # Check if it references Qwen3-4B (in spec command, hypothesis, model_name, or exp_id)\n    is_4b = False\n    cmd = exp.get('spec', {}).get('command', '')\n    hypothesis = exp.get('hypothesis', '')\n    model_name = exp.get('spec', {}).get('model_name', '')\n\n    checks = [cmd, hypothesis, model_name, exp_id]\n    for c in checks:\n        if c and ('4b' in c.lower() or '4B' in c or 'Qwen3-4B' in c):\n            is_4b = True\n            break\n\n    if not is_4b:\n        continue\n\n    # Check if it's an eval experiment\n    is_eval = False\n    if 'eval' in exp_id.lower():\n        is_eval = True\n    if 'eval' in cmd.lower() and ('inference' in cmd.lower() or 'eval' in cmd.lower()):\n        is_eval = True\n    if 'eval' in hypothesis.lower():\n        is_eval = True\n\n    if not is_eval:\n        continue\n\n    eval_exps.append((exp_id, exp))\n\nprint(f\"=\" * 120)\nprint(f\"D076 PROTOCOL COMPLIANCE AUDIT - All Qwen3-4B Eval Experiments\")\nprint(f\"Total experiments in registry: {len(experiments)}\")\nprint(f\"4B eval experiments found: {len(eval_exps)}\")\nprint(f\"=\" * 120)\n\n# D076 expected values\nD076 = {\n    'batch_size': '4',\n    'max_new_tokens': '1024',\n    'seed': '42',\n    'no_quantize': True,\n    'model_path_is_base': True,  # should point to base model, not adapter\n    'sft_adapter_present': True,\n}\n\ndef parse_command(cmd):\n    \"\"\"Parse command string to extract D076-relevant parameters.\"\"\"\n    result = {\n        'batch_size': None,\n        'max_new_tokens': None,\n        'seed': None,\n        'no_quantize': False,\n        'model_path': None,\n        'sft_adapter': None,\n    }\n\n    if not cmd:\n        return result\n\n    # batch_size\n    m = re.search(r'--batch_size\\s+(\\S+)', cmd)\n    if m:\n        result['batch_size'] = m.group(1)\n\n    # max_new_tokens\n    m = re.search(r'--max_new_tokens\\s+(\\S+)', cmd)\n    if m:\n        result['max_new_tokens'] = m.group(1)\n\n    # seed\n    m = re.search(r'--seed\\s+(\\S+)', cmd)\n    if m:\n        result['seed'] = m.group(1)\n\n    # no-quantize\n    if '--no-quantize' in cmd or '--no_quantize' in cmd:\n        result['no_quantize'] = True\n\n    # model_path\n    m = re.search(r'--model_path\\s+(\\S+)', cmd)\n    if m:\n        result['model_path'] = m.group(1)\n\n    # sft_adapter\n    m = re.search(r'--sft_adapter\\s+(\\S+)', cmd)\n    if m:\n        result['sft_adapter'] = m.group(1)\n\n    return result\n\ndef check_model_path_is_base(model_path):\n    \"\"\"Check if model_path points to base model (not adapter directory).\"\"\"\n    if not model_path:\n        return False, \"missing\"\n    # Base model patterns\n    base_patterns = ['Qwen3-4B', 'models/Qwen', 'Qwen/Qwen']\n    # Adapter/SFT output patterns (non-compliant)\n    adapter_patterns = ['sft_output', 'adapter', 'checkpoint', 'lora', 'grpo_output', 'rsft_output']\n\n    is_base = any(p in model_path for p in base_patterns)\n    is_adapter = any(p in model_path for p in adapter_patterns)\n\n    if is_adapter:\n        return False, f\"points to adapter dir: {model_path}\"\n    if is_base:\n        return True, \"OK\"\n    return False, f\"unknown path: {model_path}\"\n\ndef check_d076(parsed):\n    \"\"\"Check D076 compliance and return (compliant, reasons).\"\"\"\n    reasons = []\n\n    if parsed['batch_size'] != '4':\n        reasons.append(f\"batch_size={parsed['batch_size']} (expected 4)\")\n    if parsed['max_new_tokens'] != '1024':\n        reasons.append(f\"max_new_tokens={parsed['max_new_tokens']} (expected 1024)\")\n    if parsed['seed'] != '42':\n        reasons.append(f\"seed={parsed['seed']} (expected 42)\")\n    if not parsed['no_quantize']:\n        reasons.append(\"--no-quantize MISSING\")\n\n    base_ok, base_msg = check_model_path_is_base(parsed['model_path'])\n    if not base_ok:\n        reasons.append(f\"model_path: {base_msg}\")\n\n    if not parsed['sft_adapter']:\n        reasons.append(\"--sft_adapter MISSING\")\n\n    compliant = len(reasons) == 0\n    return compliant, reasons\n\n# Sort by exp_id\neval_exps.sort(key=lambda x: x[0])\n\n# Print detailed info for each experiment\nprint()\nfor i, (exp_id, exp) in enumerate(eval_exps):\n    cmd = exp.get('spec', {}).get('command', '')\n    status = exp.get('status', 'UNKNOWN')\n    hypothesis = exp.get('hypothesis', '')\n    metrics = exp.get('spec', {}).get('metrics', exp.get('reproduce', {}).get('metrics', {}))\n    # Also check for metrics in other locations\n    if not metrics:\n        for key in ['results', 'metrics']:\n            if key in exp:\n                metrics = exp[key]\n                break\n    # Check extra for metrics\n    if not metrics and 'extra' in exp:\n        extra = exp['extra']\n        if isinstance(extra, dict):\n            for key in ['metrics', 'results', 'eval_metrics']:\n                if key in extra:\n                    metrics = extra[key]\n                    break\n\n    # Get conclusion and notes\n    conclusion = exp.get('reproduce', {}).get('conclusion', '')\n    if not conclusion:\n        conclusion = exp.get('extra', {}).get('conclusion', '')\n    notes = exp.get('reproduce', {}).get('notes', '')\n    if not notes:\n        notes = exp.get('extra', {}).get('notes', '')\n    error = exp.get('reproduce', {}).get('error', '')\n    if not error:\n        error = exp.get('extra', {}).get('error', '')\n\n    parsed = parse_command(cmd)\n    compliant, reasons = check_d076(parsed)\n\n    print(f\"\\n{'─' * 120}\")\n    print(f\"[{i+1}/{len(eval_exps)}] exp_id: {exp_id}\")\n    print(f\"  status:     {status}\")\n    print(f\"  hypothesis: {hypothesis[:200]}\")\n    print(f\"  parent:     {exp.get('parent', 'N/A')}\")\n    print(f\"  model_name: {exp.get('spec', {}).get('model_name', 'N/A')}\")\n    print()\n    print(f\"  FULL COMMAND:\")\n    print(f\"    {cmd}\")\n    print()\n    print(f\"  PARSED D076 PARAMS:\")\n    print(f\"    batch_size:     {parsed['batch_size']}\")\n    print(f\"    max_new_tokens: {parsed['max_new_tokens']}\")\n    print(f\"    seed:           {parsed['seed']}\")\n    print(f\"    no_quantize:    {parsed['no_quantize']}\")\n    print(f\"    model_path:     {parsed['model_path']}\")\n    print(f\"    sft_adapter:    {parsed['sft_adapter']}\")\n    print()\n    print(f\"  D076 COMPLIANT:   {'YES' if compliant else 'NO'}\")\n    if reasons:\n        print(f\"  NON-COMPLIANCE:   {'; '.join(reasons)}\")\n    print()\n\n    # Print all extra fields that might contain metrics/conclusion\n    print(f\"  metrics:    {json.dumps(metrics, indent=4) if metrics else 'N/A'}\")\n    print(f\"  conclusion: {conclusion if conclusion else 'N/A'}\")\n    print(f\"  notes:      {notes if notes else 'N/A'}\")\n    print(f\"  error:      {error if error else 'N/A'}\")\n\n    # Dump all keys in reproduce and extra for completeness\n    reproduce = exp.get('reproduce', {})\n    if reproduce:\n        extra_keys = [k for k in reproduce.keys() if k not in ('finished_at', 'conclusion', 'notes', 'error', 'metrics')]\n        if extra_keys:\n            print(f\"  reproduce extra keys: {extra_keys}\")\n            for k in extra_keys:\n                v = reproduce[k]\n                v_str = json.dumps(v) if isinstance(v, (dict, list)) else str(v)\n                if len(v_str) > 500:\n                    v_str = v_str[:500] + '...'\n                print(f\"    reproduce.{k}: {v_str}\")\n\n    extra = exp.get('extra', {})\n    if extra:\n        extra_keys = [k for k in extra.keys() if k not in ('hook_events', 'conclusion', 'notes', 'error', 'metrics')]\n        if extra_keys:\n            print(f\"  extra keys: {extra_keys}\")\n            for k in extra_keys:\n                v = extra[k]\n                v_str = json.dumps(v) if isinstance(v, (dict, list)) else str(v)\n                if len(v_str) > 500:\n                    v_str = v_str[:500] + '...'\n                print(f\"    extra.{k}: {v_str}\")\n\n# Now print summary table\nprint(f\"\\n\\n{'=' * 200}\")\nprint(\"SUMMARY TABLE\")\nprint(f\"{'=' * 200}\")\n\nheader = f\"{'exp_id':<45} | {'status':<12} | {'ign_f1':<8} | {'bs':<4} | {'max_tok':<8} | {'seed':<5} | {'no_q':<5} | {'model_path':<55} | {'sft_adapter':<55} | {'D076':<5} | non_compliance\"\nprint(header)\nprint(\"─\" * len(header))\n\nfor exp_id, exp in eval_exps:\n    cmd = exp.get('spec', {}).get('command', '')\n    status = exp.get('status', '?')\n    parsed = parse_command(cmd)\n    compliant, reasons = check_d076(parsed)\n\n    # Try to find ign_f1\n    ign_f1 = 'N/A'\n    for loc in [exp.get('reproduce', {}), exp.get('extra', {}), exp.get('spec', {})]:\n        if isinstance(loc, dict):\n            if 'metrics' in loc and isinstance(loc['metrics'], dict):\n                if 'ign_f1' in loc['metrics']:\n                    ign_f1 = str(loc['metrics']['ign_f1'])\n                    break\n            if 'ign_f1' in loc:\n                ign_f1 = str(loc['ign_f1'])\n                break\n    # Also check nested results\n    for loc in [exp.get('reproduce', {}), exp.get('extra', {})]:\n        if isinstance(loc, dict):\n            for k, v in loc.items():\n                if isinstance(v, dict) and 'ign_f1' in v:\n                    ign_f1 = str(v['ign_f1'])\n                    break\n\n    mp = parsed['model_path'] or 'MISSING'\n    sa = parsed['sft_adapter'] or 'MISSING'\n    # Shorten paths for table\n    mp_short = mp[-55:] if len(mp) > 55 else mp\n    sa_short = sa[-55:] if len(sa) > 55 else sa\n\n    row = f\"{exp_id:<45} | {status:<12} | {ign_f1:<8} | {parsed['batch_size'] or '?':<4} | {parsed['max_new_tokens'] or '?':<8} | {parsed['seed'] or '?':<5} | {'Y' if parsed['no_quantize'] else 'N':<5} | {mp_short:<55} | {sa_short:<55} | {'YES' if compliant else 'NO':<5} | {'; '.join(reasons) if reasons else ''}\"\n    print(row)\n\n# Special analysis: SFT s42 eval experiments\nprint(f\"\\n\\n{'=' * 120}\")\nprint(\"SPECIAL ANALYSIS: SFT s42 (original seed) eval experiments\")\nprint(f\"{'=' * 120}\")\nfor exp_id, exp in eval_exps:\n    if 's42' in exp_id.lower() or 'seed42' in exp_id.lower() or ('sft' in exp_id.lower() and 's42' in exp.get('hypothesis', '').lower()):\n        cmd = exp.get('spec', {}).get('command', '')\n        parsed = parse_command(cmd)\n        print(f\"\\n  exp_id: {exp_id}\")\n        print(f\"  status: {exp.get('status', '?')}\")\n        print(f\"  model_path:  {parsed['model_path']}\")\n        print(f\"  sft_adapter: {parsed['sft_adapter']}\")\n        print(f\"  FULL CMD: {cmd}\")\n\n# Also check: any eval using the original SFT output (no seed suffix)\nprint(f\"\\n\\n{'=' * 120}\")\nprint(\"SPECIAL ANALYSIS: Evals with model_path pointing to adapter directories\")\nprint(f\"{'=' * 120}\")\nfor exp_id, exp in eval_exps:\n    cmd = exp.get('spec', {}).get('command', '')\n    parsed = parse_command(cmd)\n    if parsed['model_path']:\n        base_ok, base_msg = check_model_path_is_base(parsed['model_path'])\n        if not base_ok:\n            print(f\"\\n  exp_id:     {exp_id}\")\n            print(f\"  status:     {exp.get('status', '?')}\")\n            print(f\"  model_path: {parsed['model_path']}\")\n            print(f\"  issue:      {base_msg}\")\n            print(f\"  FULL CMD:   {cmd}\")\n\nprint(f\"\\n\\n{'=' * 120}\")\nprint(\"SPECIAL ANALYSIS: Evals MISSING --no-quantize\")\nprint(f\"{'=' * 120}\")\nfor exp_id, exp in eval_exps:\n    cmd = exp.get('spec', {}).get('command', '')\n    parsed = parse_command(cmd)\n    if not parsed['no_quantize']:\n        print(f\"\\n  exp_id:  {exp_id}\")\n        print(f\"  status:  {exp.get('status', '?')}\")\n        print(f\"  FULL CMD: {cmd}\")\n\nprint(f\"\\n\\n{'=' * 120}\")\nprint(\"SPECIAL ANALYSIS: Evals with non-standard batch_size or max_new_tokens\")\nprint(f\"{'=' * 120}\")\nfor exp_id, exp in eval_exps:\n    cmd = exp.get('spec', {}).get('command', '')\n    parsed = parse_command(cmd)\n    issues = []\n    if parsed['batch_size'] and parsed['batch_size'] != '4':\n        issues.append(f\"batch_size={parsed['batch_size']}\")\n    if parsed['max_new_tokens'] and parsed['max_new_tokens'] != '1024':\n        issues.append(f\"max_new_tokens={parsed['max_new_tokens']}\")\n    if issues:\n        print(f\"\\n  exp_id:  {exp_id}\")\n        print(f\"  status:  {exp.get('status', '?')}\")\n        print(f\"  issues:  {', '.join(issues)}\")\n        print(f\"  FULL CMD: {cmd}\")\n\n# Count compliant vs non-compliant\ncompliant_count = 0\nnon_compliant_count = 0\nfor exp_id, exp in eval_exps:\n    cmd = exp.get('spec', {}).get('command', '')\n    parsed = parse_command(cmd)\n    compliant, _ = check_d076(parsed)\n    if compliant:\n        compliant_count += 1\n    else:\n        non_compliant_count += 1\n\nprint(f\"\\n\\n{'=' * 120}\")\nprint(f\"OVERALL D076 COMPLIANCE: {compliant_count}/{len(eval_exps)} compliant, {non_compliant_count}/{len(eval_exps)} non-compliant\")\nprint(f\"{'=' * 120}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5026426-c18d-44fa-8796-1799dd6ef7bb",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAny3TfBR3vGY7UyfYrF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ddd39e3e-274c-4597-a1b6-f386fb1a0bb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNEiC75nPnzZGc9WpLM4Mk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1138,
      "cache_read_input_tokens": 18875,
      "output_tokens": 4769,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1138
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4769,
          "cache_read_input_tokens": 18875,
          "cache_creation_input_tokens": 1138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1138,
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

_source line 20 · 2026-05-18T22:06:39.865Z_

<details><summary>↩ Tool result · `toolu_015awc5JNyFhDZQXUx7fqLb7`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/d076_eval_audit.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ddd39e3e-274c-4597-a1b6-f386fb1a0bb5",
  "isSidechain": true,
  "promptId": "23faa4e2-0c97-47f8-be9e-f272ba775828",
  "agentId": "a35180a8a436e895f",
  "type": "user",
  "uuid": "83d6651d-5f0b-448e-8ea3-29dcd458b030",
  "sourceToolAssistantUUID": "ddd39e3e-274c-4597-a1b6-f386fb1a0bb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T22:06:43.262Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HZLvcqQ9v3AhKgdAkXPUMR`</summary>

```json
{
  "command": "python3 artifacts/d076_eval_audit.py 2>&1",
  "description": "Run D076 compliance audit script",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83d6651d-5f0b-448e-8ea3-29dcd458b030",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAo3FPsDrRvVZDUvJXcF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d4d4fea-f0e4-4868-8ce6-2de8ee32fb8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4pBVYCtj3FwkkhugAaF2r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4871,
      "cache_read_input_tokens": 20013,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4871
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 20013,
          "cache_creation_input_tokens": 4871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4871,
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

_source line 22 · 2026-05-18T22:06:43.377Z_

<details><summary>↩ Tool result · `toolu_01HZLvcqQ9v3AhKgdAkXPUMR`</summary>

```text
&lt;persisted-output>
Output too large (235.2KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/b432e0wbi.txt

Preview (first 2KB):
========================================================================================================================
D076 PROTOCOL COMPLIANCE AUDIT - All Qwen3-4B Eval Experiments
Total experiments in registry: 222
4B eval experiments found: 84
========================================================================================================================


────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
[1/84] exp_id: eval_flat_nli_s44
  status:     DONE
  hypothesis: Full dev eval of flat-NLI RSFT seed=44 with --sft_adapter + --no-quantize. C3 统计显著性数据点 (s42=0.4539, s43 pending, s44 本次, s45 pending)。
  parent:     plan_001_flat_nli_seed44
  model_name: N/A

  FULL COMMAND:
    bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s44 --no-quantize"

  PARSED D076 PARAMS:
    batch_size:     4
    max_new_tokens: 1024
    seed:           44
    no_quantize:    True
    model_path:     /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507
    sft_adapter:    /root/autodl-tmp/sft_output

  D076 COMPLIANT:   NO
  NON-COMPLIANCE:   seed=44 (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507

  metrics:    {
    "rel_f1": 0.461506,
    "ign_f1": 0.452126,
    "evi_f1": 0.813123,
    "edcr": 0.645808,
    "evi_f1_joint": 0.359673
}
  conclusion: N/A
  notes:      N/A
  error:      N/A
  reproduce extra keys: ['command']
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d4d4fea-f0e4-4868-8ce6-2de8ee32fb8d",
  "isSidechain": true,
  "promptId": "23faa4e2-0c97-47f8-be9e-f272ba775828",
  "agentId": "a35180a8a436e895f",
  "type": "user",
  "uuid": "56fc02e3-6904-4933-9d90-d8a0f5571c21",
  "sourceToolAssistantUUID": "0d4d4fea-f0e4-4868-8ce6-2de8ee32fb8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-18T22:06:45.868Z_

The output is very large. Let me read the summary table and special analyses.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56fc02e3-6904-4933-9d90-d8a0f5571c21",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAo3WWTgBrjQTmZaAfCj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d2c2ad3-33b5-4d25-a495-ad85861485de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EXYpUWToqyRVEVbX45BtJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5819,
      "cache_read_input_tokens": 20013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5819,
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

_source line 24 · 2026-05-18T22:06:47.890Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UR1G4TZeTThrUnuqmk3vDH`</summary>

```json
{
  "command": "python3 -c \"\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/b432e0wbi.txt', 'r') as f:\n    content = f.read()\n\n# Find the SUMMARY TABLE section\nidx = content.find('SUMMARY TABLE')\nif idx != -1:\n    print(content[idx:])\n\"\n",
  "description": "Read summary table from audit output",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d2c2ad3-33b5-4d25-a495-ad85861485de",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAo3WWTgBrjQTmZaAfCj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50ee8def-f9db-43bf-b3d8-5da54bb80049",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EXYpUWToqyRVEVbX45BtJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5819,
      "cache_read_input_tokens": 20013,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5819
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 20013,
          "cache_creation_input_tokens": 5819,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5819,
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

_source line 25 · 2026-05-18T22:06:47.969Z_

<details><summary>↩ Tool result · `toolu_01UR1G4TZeTThrUnuqmk3vDH`</summary>

```text
&lt;persisted-output>
Output too large (83.7KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/bbsbky2j1.txt

Preview (first 2KB):
SUMMARY TABLE
========================================================================================================================================================================================================
exp_id                                        | status       | ign_f1   | bs   | max_tok  | seed  | no_q  | model_path                                              | sft_adapter                                             | D076  | non_compliance
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
eval_flat_nli_s44                             | DONE         | N/A      | 4    | 1024     | 44    | Y     | root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 | /root/autodl-tmp/sft_output                             | NO    | seed=44 (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507
eval_flat_nli_seed44                          | DONE         | N/A      | 4    | 1024     | 44    | Y     | root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 | /root/autodl-tmp/sft_output                             | NO    | seed=44 (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507
eval_flat_nli_seed45                          | DONE         | N/A      | 4    | 1024     | 45    | Y     | root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507 | /root/autodl-tmp/sft_output                             | NO    | seed=45 (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50ee8def-f9db-43bf-b3d8-5da54bb80049",
  "isSidechain": true,
  "promptId": "23faa4e2-0c97-47f8-be9e-f272ba775828",
  "agentId": "a35180a8a436e895f",
  "type": "user",
  "uuid": "84c7fdd7-7215-40af-b47b-8402a7f04f80",
  "sourceToolAssistantUUID": "50ee8def-f9db-43bf-b3d8-5da54bb80049",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-18T22:06:50.814Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TZ8f6yoKynx7Z3ZFuDFzo8`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/bbsbky2j1.txt",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84c7fdd7-7215-40af-b47b-8402a7f04f80",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAo3r1UbZf3iX9o8roDJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe76e3a7-4430-43a3-8755-f09af1abef0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014BRBrTmNxMhiUVNRzm7oC8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 25832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 872,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 27 · 2026-05-18T22:06:51.078Z_

<details><summary>↩ Tool result · `toolu_01TZ8f6yoKynx7Z3ZFuDFzo8`</summary>

```text
1	SUMMARY TABLE
2	========================================================================================================================================================================================================
3	exp_id                                        | status       | ign_f1   | bs   | max_tok  | seed  | no_q  | model_path                                              | sft_adapter                                             | D076  | non_compliance
4	──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
5	eval_flat_nli_s44                             | DONE         | N/A      | 4    | 1024     | 44    | Y     | root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 | /root/autodl-tmp/sft_output                             | NO    | seed=44 (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507
6	eval_flat_nli_seed44                          | DONE         | N/A      | 4    | 1024     | 44    | Y     | root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 | /root/autodl-tmp/sft_output                             | NO    | seed=44 (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507
7	eval_flat_nli_seed45                          | DONE         | N/A      | 4    | 1024     | 45    | Y     | root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507 | /root/autodl-tmp/sft_output                             | NO    | seed=45 (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507
8	eval_grpo_g8_bf16                             | DONE         | N/A      | ?    | 1024     | ?     | Y     | MISSING                                                 | sft_output                                              | NO    | batch_size=None (expected 4); seed=None (expected 42); model_path: missing
9	eval_plan_001_flat_nli                        | DONE         | N/A      | 16   | 1024     | 42    | Y     | /root/autodl-tmp/rsft_output_flat_nli                   | /root/autodl-tmp/sft_output                             | NO    | batch_size=16 (expected 4); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli
10	eval_plan_001_flat_nli_s43                    | DONE         | N/A      | 16   | 1024     | 43    | Y     | /root/autodl-tmp/rsft_output_flat_nli_s43               | MISSING                                                 | NO    | batch_size=16 (expected 4); seed=43 (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s43; --sft_adapter MISSING
11	eval_plan_008_rsft_topk3                      | DONE         | N/A      | 16   | 1024     | 42    | Y     | /root/autodl-tmp/rsft_topk3_output                      | MISSING                                                 | NO    | batch_size=16 (expected 4); model_path: unknown path: /root/autodl-tmp/rsft_topk3_output; --sft_adapter MISSING
12	eval_plan_008_topk3_fixed                     | DONE         | N/A      | 16   | 1024     | 42    | Y     | /root/autodl-tmp/rsft_topk3_output                      | /root/autodl-tmp/sft_output                             | NO    | batch_size=16 (expected 4); model_path: unknown path: /root/autodl-tmp/rsft_topk3_output
13	eval_plan_012_dpo_1ep_fixed                   | DONE         | N/A      | 16   | 1024     | 42    | Y     | /root/autodl-tmp/dpo_output_1ep/                        | /root/autodl-tmp/sft_output                             | NO    | batch_size=16 (expected 4); model_path: unknown path: /root/autodl-tmp/dpo_output_1ep/
14	eval_plan_012_dpo_1ep_fixed_r2                | DONE         | N/A      | ?    | ?        | ?     | N     | MISSING                                                 | (D064                                                   | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); --no-quantize MISSING; model_path: missing
15	eval_plan_012_dpo_ced_1ep                     | DONE         | N/A      | 16   | 1024     | 42    | Y     | /root/autodl-tmp/dpo_output_1ep/                        | MISSING                                                 | NO    | batch_size=16 (expected 4); model_path: unknown path: /root/autodl-tmp/dpo_output_1ep/; --sft_adapter MISSING
16	eval_plan_012_dpo_ced_ckpt400                 | DONE         | N/A      | 16   | 1024     | 42    | Y     | /root/autodl-tmp/dpo_output/checkpoint-400              | MISSING                                                 | NO    | batch_size=16 (expected 4); model_path: points to adapter dir: /root/autodl-tmp/dpo_output/checkpoint-400; --sft_adapter MISSING
17	eval_plan_014_no_evidence                     | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/sft_no_evidence_output                 | MISSING                                                 | NO    | model_path: unknown path: /root/autodl-tmp/sft_no_evidence_output; --sft_adapter MISSING
18	eval_plan_014_no_evidence_r2                  | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/models/Qwen3-4B                        | /root/autodl-tmp/sft_no_evidence_output                 | YES   | 
19	eval_rsft_ced_s43                             | DONE         | N/A      | 4    | 1024     | 43    | Y     | /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510     | /root/autodl-tmp/sft_output                             | NO    | seed=43 (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
20	eval_rsft_ced_s45                             | DONE         | N/A      | 4    | 1024     | 45    | Y     | /root/autodl-tmp/rsft_output_ced_s45/checkpoint-510     | /root/autodl-tmp/sft_output                             | NO    | seed=45 (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_ced_s45/checkpoint-510
21	eval_sft_baseline_noquant                     | DONE         | N/A      | 16   | 1024     | 42    | N     | /root/autodl-tmp/sft_output                             | MISSING                                                 | NO    | batch_size=16 (expected 4); --no-quantize MISSING; model_path: points to adapter dir: /root/autodl-tmp/sft_output; --sft_adapter MISSING
22	grpo_bf16_g4_ckpt100_eval                     | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/grpo_bf16_g4/checkpoint-100            | /root/autodl-tmp/sft_output/                            | NO    | model_path: points to adapter dir: /root/autodl-tmp/grpo_bf16_g4/checkpoint-100
23	grpo_bf16_g4_ckpt200_eval                     | RUNNING      | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/grpo_bf16_g4/checkpoint-200            | /root/autodl-tmp/sft_output/                            | NO    | model_path: points to adapter dir: /root/autodl-tmp/grpo_bf16_g4/checkpoint-200
24	lead2_ckpt20_eval                             | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/grpo_from_rsft_lead2_r2/checkpoint-20  | MISSING                                                 | NO    | model_path: points to adapter dir: /root/autodl-tmp/grpo_from_rsft_lead2_r2/checkpoint-20; --sft_adapter MISSING
25	mvp2_ced_reranker_poc                         | DONE         | N/A      | ?    | ?        | ?     | N     | MISSING                                                 | MISSING                                                 | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); --no-quantize MISSING; model_path: missing; --sft_adapter MISSING
26	mvp2_eval_ced_kl001_r4_ckpt10                 | DONE         | N/A      | ?    | ?        | ?     | N     | MISSING                                                 | /root/autodl-tmp/sft_output                             | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); --no-quantize MISSING; model_path: missing
27	mvp2_eval_ced_kl001_r4_ckpt90                 | DONE         | N/A      | ?    | ?        | ?     | N     | MISSING                                                 | MISSING                                                 | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); --no-quantize MISSING; model_path: missing; --sft_adapter MISSING
28	mvp2_eval_ced_kl001_r4_early                  | DONE         | N/A      | ?    | ?        | ?     | N     | MISSING                                                 | /root/autodl-tmp/sft_output                             | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); --no-quantize MISSING; model_path: missing
29	mvp2_eval_ced_kl001_r4_high                   | DONE         | N/A      | ?    | ?        | ?     | N     | MISSING                                                 | /root/autodl-tmp/sft_output                             | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); --no-quantize MISSING; model_path: missing
30	mvp2_eval_ced_kl001_r4_multi                  | DONE         | N/A      | ?    | ?        | ?     | N     | MISSING                                                 | /root/autodl-tmp/sft_output                             | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); --no-quantize MISSING; model_path: missing
31	mvp2_eval_ced_kl001_r4_step100                | DONE         | N/A      | ?    | ?        | ?     | N     | MISSING                                                 | /root/autodl-tmp/sft_output                             | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); --no-quantize MISSING; model_path: missing
32	mvp2_eval_ced_kl001_r4_step90                 | DONE         | N/A      | ?    | ?        | ?     | N     | MISSING                                                 | /root/autodl-tmp/sft_output                             | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); --no-quantize MISSING; model_path: missing
33	mvp2_eval_lr5e6_r1_ckpt100                    | DONE         | N/A      | 16   | 1024     | 42    | N     | /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-100          | /root/autodl-tmp/sft_output                             | NO    | batch_size=16 (expected 4); --no-quantize MISSING; model_path: points to adapter dir: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-100
34	mvp2_eval_lr5e6_r1_ckpt20                     | DONE         | N/A      | ?    | ?        | ?     | N     | MISSING                                                 | MISSING                                                 | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); --no-quantize MISSING; model_path: missing; --sft_adapter MISSING
35	mvp2_eval_lr5e6_r1_ckpt40                     | DONE         | N/A      | ?    | ?        | ?     | N     | MISSING                                                 | MISSING                                                 | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); --no-quantize MISSING; model_path: missing; --sft_adapter MISSING
36	mvp2_eval_lr5e6_r1_ckpt40_r2                  | DONE         | 0.007146887342486364 | ?    | ?        | ?     | N     | MISSING                                                 | MISSING                                                 | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); --no-quantize MISSING; model_path: missing; --sft_adapter MISSING
37	mvp2_eval_lr5e6_r1_ckpt60_r2                  | DONE         | N/A      | 16   | 1024     | 42    | N     | /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-60           | /root/autodl-tmp/sft_output                             | NO    | batch_size=16 (expected 4); --no-quantize MISSING; model_path: points to adapter dir: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-60
38	mvp2_eval_lr5e6_r1_ckpt80                     | DONE         | N/A      | 16   | 1024     | 42    | N     | /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-80           | /root/autodl-tmp/sft_output                             | NO    | batch_size=16 (expected 4); --no-quantize MISSING; model_path: points to adapter dir: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-80
39	mvp2_eval_lr5e6_rp_r2_ckpt20                  | DONE         | N/A      | ?    | ?        | ?     | N     | MISSING                                                 | MISSING                                                 | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); --no-quantize MISSING; model_path: missing; --sft_adapter MISSING
40	mvp2_eval_rsft_r1                             | DONE         | N/A      | ?    | ?        | ?     | Y     | MISSING                                                 | MISSING                                                 | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); model_path: missing; --sft_adapter MISSING
41	mvp2_eval_rsft_r2a                            | DONE         | N/A      | ?    | ?        | ?     | Y     | MISSING                                                 | MISSING                                                 | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); model_path: missing; --sft_adapter MISSING
42	mvp2_eval_rsft_r2b                            | DONE         | N/A      | ?    | ?        | ?     | Y     | MISSING                                                 | MISSING                                                 | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); model_path: missing; --sft_adapter MISSING
43	mvp2_eval_rsft_r2b_maxtok1536                 | DONE         | N/A      | ?    | 1536     | ?     | Y     | /root/autodl-tmp/rsft_output_r2b                        | MISSING                                                 | NO    | batch_size=None (expected 4); max_new_tokens=1536 (expected 1024); seed=None (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_r2b; --sft_adapter MISSING
44	mvp2_eval_rsft_r2b_maxtok1536_r2              | DONE         | N/A      | ?    | 1536     | ?     | Y     | /root/autodl-tmp/rsft_output_r2b                        | /root/autodl-tmp/sft_output                             | NO    | batch_size=None (expected 4); max_new_tokens=1536 (expected 1024); seed=None (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_r2b
45	mvp2_eval_rsft_s43                            | DONE         | N/A      | ?    | ?        | ?     | Y     | MISSING                                                 | /root/autodl-tmp/sft_output                             | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); model_path: missing
46	mvp2_eval_rsft_s43_r2                         | DONE         | N/A      | ?    | ?        | ?     | Y     | /root/autodl-tmp/rsft_output_s43                        | /root/autodl-tmp/sft_output                             | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_s43
47	mvp2_eval_sft_baseline                        | DONE         | N/A      | 16   | 1024     | 42    | N     | /root/autodl-tmp/sft_output                             | MISSING                                                 | NO    | batch_size=16 (expected 4); --no-quantize MISSING; model_path: points to adapter dir: /root/autodl-tmp/sft_output; --sft_adapter MISSING
48	mvp2_rsft_r2a                                 | DONE         | N/A      | ?    | ?        | 42"   | N     | MISSING                                                 | /root/autodl-tmp/sft_output                             | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=42" (expected 42); --no-quantize MISSING; model_path: missing
49	mvp2_rsft_r2b                                 | DONE         | N/A      | ?    | ?        | 42"   | N     | MISSING                                                 | /root/autodl-tmp/sft_output                             | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=42" (expected 42); --no-quantize MISSING; model_path: missing
50	mvp2_rsft_train_r1                            | DONE         | N/A      | ?    | ?        | 42"   | N     | MISSING                                                 | /root/autodl-tmp/sft_output                             | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=42" (expected 42); --no-quantize MISSING; model_path: missing
51	mvp2_rsft_train_r1_s43                        | DONE         | N/A      | ?    | ?        | 43"   | N     | MISSING                                                 | /root/autodl-tmp/sft_output                             | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=43" (expected 42); --no-quantize MISSING; model_path: missing
52	mvp2_rsft_train_r1_s44                        | DONE         | N/A      | ?    | ?        | 44"   | N     | MISSING                                                 | /root/autodl-tmp/sft_output                             | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=44" (expected 42); --no-quantize MISSING; model_path: missing
53	mvp2_sft_eval                                 | DONE         | N/A      | ?    | ?        | ?     | N     | sft_output                                              | MISSING                                                 | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); --no-quantize MISSING; model_path: points to adapter dir: sft_output; --sft_adapter MISSING
54	mvp2_sft_eval_r2                              | DONE         | N/A      | 16   | 1024     | 42    | N     | /root/autodl-tmp/sft_output                             | MISSING                                                 | NO    | batch_size=16 (expected 4); --no-quantize MISSING; model_path: points to adapter dir: /root/autodl-tmp/sft_output; --sft_adapter MISSING
55	mvp2_sft_eval_r3                              | DONE         | N/A      | 16   | 1024     | 42"   | N     | /root/autodl-tmp/sft_output                             | MISSING                                                 | NO    | batch_size=16 (expected 4); seed=42" (expected 42); --no-quantize MISSING; model_path: points to adapter dir: /root/autodl-tmp/sft_output; --sft_adapter MISSING
56	plan_001_flat_nli_seed43                      | DONE         | N/A      | ?    | ?        | 43    | N     | MISSING                                                 | /root/autodl-tmp/sft_output                             | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=43 (expected 42); --no-quantize MISSING; model_path: missing
57	plan_002_test_eval_s44                        | DONE         | N/A      | 16   | 1024     | 42    | Y     | /root/autodl-tmp/rsft_output_s44                        | /root/autodl-tmp/sft_output                             | NO    | batch_size=16 (expected 4); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_s44
58	plan_002_test_eval_s44_r2                     | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/rsft_output_s44/checkpoint-510         | /root/autodl-tmp/sft_output                             | NO    | model_path: points to adapter dir: /root/autodl-tmp/rsft_output_s44/checkpoint-510
59	plan_002_test_rsft_s43                        | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/models/Qwen3-4B                        | /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510     | YES   | 
60	plan_002_test_rsft_s44                        | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/rsft_output_s44/checkpoint-510         | /root/autodl-tmp/sft_output                             | NO    | model_path: points to adapter dir: /root/autodl-tmp/rsft_output_s44/checkpoint-510
61	plan_006_qwen3_8b_no_evidence_eval_v2         | DONE         | 0.5079   | 4    | 1024     | 42    | Y     | /root/autodl-tmp/models/Qwen/Qwen3-8B                   | /root/autodl-tmp/sft_output_qwen3_8b_no_evidence        | YES   | 
62	plan_007_redocred_4b_sft_eval                 | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/models/Qwen/Qwen3-4B                   | /root/autodl-tmp/sft_output_qwen3_4b                    | YES   | 
63	plan_007_redocred_4b_sft_eval_r2              | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/models/Qwen3-4B                        | /root/autodl-tmp/sft_output                             | YES   | 
64	plan_007_redocred_rsft_eval                   | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510     | /root/autodl-tmp/sft_output                             | NO    | model_path: points to adapter dir: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
65	plan_007_redocred_rsft_eval_r2                | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/models/Qwen3-4B                        | /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510     | YES   | 
66	plan_007_redocred_rsft_eval_r3                | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/models/Qwen3-4B                        | /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510     | YES   | 
67	plan_007_redocred_rsft_eval_r4                | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510     | /root/autodl-tmp/sft_output                             | NO    | model_path: points to adapter dir: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
68	plan_007_redocred_rsft_eval_r5                | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510     | /root/autodl-tmp/sft_output                             | NO    | model_path: points to adapter dir: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
69	plan_009_flatnli_reward_eval                  | DONE         | N/A      | ?    | ?        | ?     | N     | MISSING                                                 | MISSING                                                 | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); --no-quantize MISSING; model_path: missing; --sft_adapter MISSING
70	plan_009_flatnli_reward_eval_r2               | DONE         | N/A      | ?    | 1024     | ?     | Y     | MISSING                                                 | /root/autodl-tmp/sft_output                             | NO    | batch_size=None (expected 4); seed=None (expected 42); model_path: missing
71	plan_011_grpo_g8_bf16_eval                    | DONE         | N/A      | 16   | 1024     | 42    | Y     | /root/autodl-tmp/grpo_ced_g8_bf16/checkpoint-100        | /root/autodl-tmp/sft_output                             | NO    | batch_size=16 (expected 4); model_path: points to adapter dir: /root/autodl-tmp/grpo_ced_g8_bf16/checkpoint-100
72	plan_014_no_evidence_eval_d076                | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/models/Qwen/Qwen3-4B                   | /root/autodl-tmp/sft_no_evidence_output/                | YES   | 
73	random_rsft_k1_eval                           | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/rsft_output_random_k1/checkpoint-1020  | /root/autodl-tmp/sft_output/                            | NO    | model_path: points to adapter dir: /root/autodl-tmp/rsft_output_random_k1/checkpoint-1020
74	reeval_ced_s42                                | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/rsft_output/checkpoint-510             | /root/autodl-tmp/sft_output                             | NO    | model_path: points to adapter dir: /root/autodl-tmp/rsft_output/checkpoint-510
75	reeval_ced_s44                                | DONE         | N/A      | 4    | 1024     | 44    | Y     | /root/autodl-tmp/rsft_output_s44/checkpoint-510         | /root/autodl-tmp/sft_output                             | NO    | seed=44 (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_s44/checkpoint-510
76	reeval_flat_nli_s42                           | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/rsft_output_flat_nli/checkpoint-507    | /root/autodl-tmp/sft_output                             | NO    | model_path: points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli/checkpoint-507
77	reeval_flat_nli_s43                           | DONE         | N/A      | ?    | ?        | ?     | N     | MISSING                                                 | (D064                                                   | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=None (expected 42); --no-quantize MISSING; model_path: missing
78	reeval_flat_nli_s43_r2                        | DONE         | N/A      | 4    | 1024     | 43    | Y     | root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507 | /root/autodl-tmp/sft_output                             | NO    | seed=43 (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507
79	reeval_flat_nli_s44                           | DONE         | N/A      | 4    | 1024     | 44    | Y     | root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 | /root/autodl-tmp/sft_output                             | NO    | seed=44 (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507
80	reeval_rsft_topk3                             | DONE         | N/A      | 16   | 1024     | 42    | Y     | /root/autodl-tmp/rsft_topk3_output/checkpoint-1509      | /root/autodl-tmp/sft_output                             | NO    | batch_size=16 (expected 4); model_path: points to adapter dir: /root/autodl-tmp/rsft_topk3_output/checkpoint-1509
81	reeval_sft_baseline_d076                      | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/models/Qwen3-4B                        | /root/autodl-tmp/sft_output                             | YES   | 
82	rsft_ced_s45_train_r2                         | DONE         | N/A      | ?    | ?        | 45"   | N     | MISSING                                                 | /root/autodl-tmp/sft_output                             | NO    | batch_size=None (expected 4); max_new_tokens=None (expected 1024); seed=45" (expected 42); --no-quantize MISSING; model_path: missing
83	rsft_s43_dev_eval_preds                       | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510     | /root/autodl-tmp/sft_output                             | NO    | model_path: points to adapter dir: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
84	rsft_s44_dev_eval_preds                       | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/rsft_output_s44/checkpoint-510         | /root/autodl-tmp/sft_output                             | NO    | model_path: points to adapter dir: /root/autodl-tmp/rsft_output_s44/checkpoint-510
85	wave1_sft_4b_s43_eval                         | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/sft_output_seed43/                     | MISSING                                                 | NO    | model_path: points to adapter dir: /root/autodl-tmp/sft_output_seed43/; --sft_adapter MISSING
86	wave1_sft_4b_s43_eval_r2                      | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/models/Qwen3-4B                        | /root/autodl-tmp/sft_output_seed43/                     | YES   | 
87	wave1_sft_4b_s44_eval                         | DONE         | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/sft_output_seed44/                     | MISSING                                                 | NO    | model_path: points to adapter dir: /root/autodl-tmp/sft_output_seed44/; --sft_adapter MISSING
88	wave1_sft_4b_s44_eval_r2                      | ANALYZING    | N/A      | 4    | 1024     | 42    | Y     | /root/autodl-tmp/models/Qwen3-4B                        | /root/autodl-tmp/sft_output_seed44/                     | YES   | 
89	
90	
91	========================================================================================================================
92	SPECIAL ANALYSIS: SFT s42 (original seed) eval experiments
93	========================================================================================================================
94	
95	  exp_id: eval_rsft_ced_s45
96	  status: DONE
97	  model_path:  /root/autodl-tmp/rsft_output_ced_s45/checkpoint-510
98	  sft_adapter: /root/autodl-tmp/sft_output
99	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s45/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 45 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s45 --no-quantize"
100	
101	  exp_id: reeval_ced_s42
102	  status: DONE
103	  model_path:  /root/autodl-tmp/rsft_output/checkpoint-510
104	  sft_adapter: /root/autodl-tmp/sft_output
105	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=2 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s42_reeval --no-quantize"
106	
107	  exp_id: reeval_flat_nli_s42
108	  status: DONE
109	  model_path:  /root/autodl-tmp/rsft_output_flat_nli/checkpoint-507
110	  sft_adapter: /root/autodl-tmp/sft_output
111	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s42_reeval --no-quantize"
112	
113	  exp_id: wave1_sft_4b_s43_eval
114	  status: DONE
115	  model_path:  /root/autodl-tmp/sft_output_seed43/
116	  sft_adapter: None
117	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_seed43/ --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/sft_4b_s43_eval"
118	
119	  exp_id: wave1_sft_4b_s43_eval_r2
120	  status: DONE
121	  model_path:  /root/autodl-tmp/models/Qwen3-4B
122	  sft_adapter: /root/autodl-tmp/sft_output_seed43/
123	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_seed43/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/wave1_sft_4b_s43_eval_r2"
124	
125	  exp_id: wave1_sft_4b_s44_eval
126	  status: DONE
127	  model_path:  /root/autodl-tmp/sft_output_seed44/
128	  sft_adapter: None
129	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_seed44/ --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/sft_4b_s44_eval"
130	
131	  exp_id: wave1_sft_4b_s44_eval_r2
132	  status: ANALYZING
133	  model_path:  /root/autodl-tmp/models/Qwen3-4B
134	  sft_adapter: /root/autodl-tmp/sft_output_seed44/
135	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_seed44/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/wave1_sft_4b_s44_eval_r2"
136	
137	
138	========================================================================================================================
139	SPECIAL ANALYSIS: Evals with model_path pointing to adapter directories
140	========================================================================================================================
141	
142	  exp_id:     eval_flat_nli_s44
143	  status:     DONE
144	  model_path: /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507
145	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507
146	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s44 --no-quantize"
147	
148	  exp_id:     eval_flat_nli_seed44
149	  status:     DONE
150	  model_path: /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507
151	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507
152	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s44 --no-quantize"
153	
154	  exp_id:     eval_flat_nli_seed45
155	  status:     DONE
156	  model_path: /root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507
157	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507
158	  FULL CMD:   python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 45 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s45 --no-quantize
159	
160	  exp_id:     eval_plan_001_flat_nli
161	  status:     DONE
162	  model_path: /root/autodl-tmp/rsft_output_flat_nli
163	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli
164	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli --sft_adapter /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli --no-quantize"
165	
166	  exp_id:     eval_plan_001_flat_nli_s43
167	  status:     DONE
168	  model_path: /root/autodl-tmp/rsft_output_flat_nli_s43
169	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s43
170	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s43 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 43 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s43 --no-quantize"
171	
172	  exp_id:     eval_plan_008_rsft_topk3
173	  status:     DONE
174	  model_path: /root/autodl-tmp/rsft_topk3_output
175	  issue:      unknown path: /root/autodl-tmp/rsft_topk3_output
176	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_topk3_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_topk3 --no-quantize"
177	
178	  exp_id:     eval_plan_008_topk3_fixed
179	  status:     DONE
180	  model_path: /root/autodl-tmp/rsft_topk3_output
181	  issue:      unknown path: /root/autodl-tmp/rsft_topk3_output
182	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_topk3_output --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_topk3_fixed --no-quantize"
183	
184	  exp_id:     eval_plan_012_dpo_1ep_fixed
185	  status:     DONE
186	  model_path: /root/autodl-tmp/dpo_output_1ep/
187	  issue:      unknown path: /root/autodl-tmp/dpo_output_1ep/
188	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/dpo_output_1ep/ --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/dpo_ced_1ep_fixed --no-quantize"
189	
190	  exp_id:     eval_plan_012_dpo_ced_1ep
191	  status:     DONE
192	  model_path: /root/autodl-tmp/dpo_output_1ep/
193	  issue:      unknown path: /root/autodl-tmp/dpo_output_1ep/
194	  FULL CMD:   python -m freige.eval.inference --model_path /root/autodl-tmp/dpo_output_1ep/ --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/dpo_ced_1ep --no-quantize
195	
196	  exp_id:     eval_plan_012_dpo_ced_ckpt400
197	  status:     DONE
198	  model_path: /root/autodl-tmp/dpo_output/checkpoint-400
199	  issue:      points to adapter dir: /root/autodl-tmp/dpo_output/checkpoint-400
200	  FULL CMD:   python -m freige.eval.inference --model_path /root/autodl-tmp/dpo_output/checkpoint-400 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/dpo_ced_ckpt400 --no-quantize
201	
202	  exp_id:     eval_plan_014_no_evidence
203	  status:     DONE
204	  model_path: /root/autodl-tmp/sft_no_evidence_output
205	  issue:      unknown path: /root/autodl-tmp/sft_no_evidence_output
206	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/sft_no_evidence_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_no_evidence_noquant --no-quantize --no_evidence"
207	
208	  exp_id:     eval_rsft_ced_s43
209	  status:     DONE
210	  model_path: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
211	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
212	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 43 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s43 --no-quantize"
213	
214	  exp_id:     eval_rsft_ced_s45
215	  status:     DONE
216	  model_path: /root/autodl-tmp/rsft_output_ced_s45/checkpoint-510
217	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_ced_s45/checkpoint-510
218	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s45/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 45 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s45 --no-quantize"
219	
220	  exp_id:     eval_sft_baseline_noquant
221	  status:     DONE
222	  model_path: /root/autodl-tmp/sft_output
223	  issue:      points to adapter dir: /root/autodl-tmp/sft_output
224	  FULL CMD:   python eval.py --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/sft_baseline_noquant --batch_size 16 --max_new_tokens 1024 --split dev --seed 42
225	
226	  exp_id:     grpo_bf16_g4_ckpt100_eval
227	  status:     DONE
228	  model_path: /root/autodl-tmp/grpo_bf16_g4/checkpoint-100
229	  issue:      points to adapter dir: /root/autodl-tmp/grpo_bf16_g4/checkpoint-100
230	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_bf16_g4/checkpoint-100 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/grpo_bf16_g4_ckpt100_eval"
231	
232	  exp_id:     grpo_bf16_g4_ckpt200_eval
233	  status:     RUNNING
234	  model_path: /root/autodl-tmp/grpo_bf16_g4/checkpoint-200
235	  issue:      points to adapter dir: /root/autodl-tmp/grpo_bf16_g4/checkpoint-200
236	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_bf16_g4/checkpoint-200 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/grpo_bf16_g4_ckpt200_eval"
237	
238	  exp_id:     lead2_ckpt20_eval
239	  status:     DONE
240	  model_path: /root/autodl-tmp/grpo_from_rsft_lead2_r2/checkpoint-20
241	  issue:      points to adapter dir: /root/autodl-tmp/grpo_from_rsft_lead2_r2/checkpoint-20
242	  FULL CMD:   CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_from_rsft_lead2_r2/checkpoint-20 --base_model /root/autodl-tmp/merged_sft_rsft_ced_s43 --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_outputs/lead2_ckpt20_eval
243	
244	  exp_id:     mvp2_eval_lr5e6_r1_ckpt100
245	  status:     DONE
246	  model_path: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-100
247	  issue:      points to adapter dir: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-100
248	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-100 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/lr5e6_r1_ckpt100/checkpoint-100 --quantize"
249	
250	  exp_id:     mvp2_eval_lr5e6_r1_ckpt60_r2
251	  status:     DONE
252	  model_path: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-60
253	  issue:      points to adapter dir: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-60
254	  FULL CMD:   CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-60 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60 --quantize
255	
256	  exp_id:     mvp2_eval_lr5e6_r1_ckpt80
257	  status:     DONE
258	  model_path: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-80
259	  issue:      points to adapter dir: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-80
260	  FULL CMD:   CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-80 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/lr5e6_r1_ckpt80/checkpoint-80 --quantize
261	
262	  exp_id:     mvp2_eval_rsft_r2b_maxtok1536
263	  status:     DONE
264	  model_path: /root/autodl-tmp/rsft_output_r2b
265	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_r2b
266	  FULL CMD:   python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_r2b --data_path /root/autodl-tmp/data/docred --no-quantize --max_new_tokens 1536 --output_dir /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536
267	
268	  exp_id:     mvp2_eval_rsft_r2b_maxtok1536_r2
269	  status:     DONE
270	  model_path: /root/autodl-tmp/rsft_output_r2b
271	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_r2b
272	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && rm -rf /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536/* && python -m freige.eval.inference --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --model_path /root/autodl-tmp/rsft_output_r2b --data_path /root/autodl-tmp/data/docred --no-quantize --max_new_tokens 1536 --output_dir /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536"
273	
274	  exp_id:     mvp2_eval_rsft_s43_r2
275	  status:     DONE
276	  model_path: /root/autodl-tmp/rsft_output_s43
277	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_s43
278	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s43 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/rsft_s43 --no-quantize"
279	
280	  exp_id:     mvp2_eval_sft_baseline
281	  status:     DONE
282	  model_path: /root/autodl-tmp/sft_output
283	  issue:      points to adapter dir: /root/autodl-tmp/sft_output
284	  FULL CMD:   python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/sft_baseline_eval_results --quantize
285	
286	  exp_id:     mvp2_sft_eval
287	  status:     DONE
288	  model_path: sft_output
289	  issue:      points to adapter dir: sft_output
290	  FULL CMD:   python -m freige.eval.inference --model_path sft_output --base_model Qwen3-4B --split dev
291	
292	  exp_id:     mvp2_sft_eval_r2
293	  status:     DONE
294	  model_path: /root/autodl-tmp/sft_output
295	  issue:      points to adapter dir: /root/autodl-tmp/sft_output
296	  FULL CMD:   python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_results --seed 42
297	
298	  exp_id:     mvp2_sft_eval_r3
299	  status:     DONE
300	  model_path: /root/autodl-tmp/sft_output
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe76e3a7-4430-43a3-8755-f09af1abef0e",
  "isSidechain": true,
  "promptId": "23faa4e2-0c97-47f8-be9e-f272ba775828",
  "agentId": "a35180a8a436e895f",
  "type": "user",
  "uuid": "ade35534-9c07-42ad-897a-455b534074cf",
  "sourceToolAssistantUUID": "fe76e3a7-4430-43a3-8755-f09af1abef0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-18T22:06:56.881Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CqLmaGdp8vBDhZsqBbxMWB`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/bbsbky2j1.txt",
  "offset": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ade35534-9c07-42ad-897a-455b534074cf",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAo45NtdC735GDRAhN5b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d490c66c-1fb4-4a19-b07c-6b19884f23c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MggCyXXFC5urZTD2bkAyPe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19680,
      "cache_read_input_tokens": 25832,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19680
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 25832,
          "cache_creation_input_tokens": 19680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19680,
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

_source line 29 · 2026-05-18T22:06:57.204Z_

<details><summary>↩ Tool result · `toolu_01CqLmaGdp8vBDhZsqBbxMWB`</summary>

```text
300	  model_path: /root/autodl-tmp/sft_output
301	  issue:      points to adapter dir: /root/autodl-tmp/sft_output
302	  FULL CMD:   bash -c "source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_r3_results --seed 42"
303	
304	  exp_id:     plan_002_test_eval_s44
305	  status:     DONE
306	  model_path: /root/autodl-tmp/rsft_output_s44
307	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_s44
308	  FULL CMD:   python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44 --sft_adapter /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split test --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/test_rsft_s44 --no-quantize
309	
310	  exp_id:     plan_002_test_eval_s44_r2
311	  status:     DONE
312	  model_path: /root/autodl-tmp/rsft_output_s44/checkpoint-510
313	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_s44/checkpoint-510
314	  FULL CMD:   CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split test --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/test_rsft_ced_s44 --no-quantize
315	
316	  exp_id:     plan_002_test_rsft_s44
317	  status:     DONE
318	  model_path: /root/autodl-tmp/rsft_output_s44/checkpoint-510
319	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_s44/checkpoint-510
320	  FULL CMD:   python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split test --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_002_test_rsft_s44
321	
322	  exp_id:     plan_007_redocred_rsft_eval
323	  status:     DONE
324	  model_path: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
325	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
326	  FULL CMD:   CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred --output_dir /root/autodl-tmp/eval_results/redocred_rsft_eval --batch_size 4 --max_new_tokens 1024 --split dev --seed 42 --no-quantize
327	
328	  exp_id:     plan_007_redocred_rsft_eval_r4
329	  status:     DONE
330	  model_path: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
331	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
332	  FULL CMD:   CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r4
333	
334	  exp_id:     plan_007_redocred_rsft_eval_r5
335	  status:     DONE
336	  model_path: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
337	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
338	  FULL CMD:   python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r4
339	
340	  exp_id:     plan_011_grpo_g8_bf16_eval
341	  status:     DONE
342	  model_path: /root/autodl-tmp/grpo_ced_g8_bf16/checkpoint-100
343	  issue:      points to adapter dir: /root/autodl-tmp/grpo_ced_g8_bf16/checkpoint-100
344	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_g8_bf16/checkpoint-100 --sft_adapter /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/grpo_g8_bf16_ckpt100 --no-quantize"
345	
346	  exp_id:     random_rsft_k1_eval
347	  status:     DONE
348	  model_path: /root/autodl-tmp/rsft_output_random_k1/checkpoint-1020
349	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_random_k1/checkpoint-1020
350	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_random_k1/checkpoint-1020 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/random_rsft_k1_eval"
351	
352	  exp_id:     reeval_ced_s42
353	  status:     DONE
354	  model_path: /root/autodl-tmp/rsft_output/checkpoint-510
355	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output/checkpoint-510
356	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=2 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s42_reeval --no-quantize"
357	
358	  exp_id:     reeval_ced_s44
359	  status:     DONE
360	  model_path: /root/autodl-tmp/rsft_output_s44/checkpoint-510
361	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_s44/checkpoint-510
362	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s44_reeval --no-quantize"
363	
364	  exp_id:     reeval_flat_nli_s42
365	  status:     DONE
366	  model_path: /root/autodl-tmp/rsft_output_flat_nli/checkpoint-507
367	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli/checkpoint-507
368	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s42_reeval --no-quantize"
369	
370	  exp_id:     reeval_flat_nli_s43_r2
371	  status:     DONE
372	  model_path: /root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507
373	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507
374	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 43 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval_r2 --no-quantize"
375	
376	  exp_id:     reeval_flat_nli_s44
377	  status:     DONE
378	  model_path: /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507
379	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507
380	  FULL CMD:   CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s44_reeval --no-quantize
381	
382	  exp_id:     reeval_rsft_topk3
383	  status:     DONE
384	  model_path: /root/autodl-tmp/rsft_topk3_output/checkpoint-1509
385	  issue:      points to adapter dir: /root/autodl-tmp/rsft_topk3_output/checkpoint-1509
386	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_topk3_output/checkpoint-1509 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_topk3_reeval --no-quantize"
387	
388	  exp_id:     rsft_s43_dev_eval_preds
389	  status:     DONE
390	  model_path: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
391	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
392	  FULL CMD:   bash -c "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/freige && python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/rsft_s43_dev_eval_preds"
393	
394	  exp_id:     rsft_s44_dev_eval_preds
395	  status:     DONE
396	  model_path: /root/autodl-tmp/rsft_output_s44/checkpoint-510
397	  issue:      points to adapter dir: /root/autodl-tmp/rsft_output_s44/checkpoint-510
398	  FULL CMD:   CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/rsft_s44_dev_with_preds
399	
400	  exp_id:     wave1_sft_4b_s43_eval
401	  status:     DONE
402	  model_path: /root/autodl-tmp/sft_output_seed43/
403	  issue:      points to adapter dir: /root/autodl-tmp/sft_output_seed43/
404	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_seed43/ --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/sft_4b_s43_eval"
405	
406	  exp_id:     wave1_sft_4b_s44_eval
407	  status:     DONE
408	  model_path: /root/autodl-tmp/sft_output_seed44/
409	  issue:      points to adapter dir: /root/autodl-tmp/sft_output_seed44/
410	  FULL CMD:   bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_seed44/ --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/sft_4b_s44_eval"
411	
412	
413	========================================================================================================================
414	SPECIAL ANALYSIS: Evals MISSING --no-quantize
415	========================================================================================================================
416	
417	  exp_id:  eval_plan_012_dpo_1ep_fixed_r2
418	  status:  DONE
419	  FULL CMD: DPO 1ep re-eval with --sft_adapter (D064 fix)
420	
421	  exp_id:  eval_sft_baseline_noquant
422	  status:  DONE
423	  FULL CMD: python eval.py --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/sft_baseline_noquant --batch_size 16 --max_new_tokens 1024 --split dev --seed 42
424	
425	  exp_id:  mvp2_ced_reranker_poc
426	  status:  DONE
427	  FULL CMD: python /root/autodl-tmp/freige/eval/ced_reranker.py (N=8, CED scoring, 985 docs)
428	
429	  exp_id:  mvp2_eval_ced_kl001_r4_ckpt10
430	  status:  DONE
431	  FULL CMD: CUDA_VISIBLE_DEVICES=2 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 10 --quantize
432	
433	  exp_id:  mvp2_eval_ced_kl001_r4_ckpt90
434	  status:  DONE
435	  FULL CMD: python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --checkpoints 90 --quantize
436	
437	  exp_id:  mvp2_eval_ced_kl001_r4_early
438	  status:  DONE
439	  FULL CMD: CUDA_VISIBLE_DEVICES=1 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 50 --quantize
440	
441	  exp_id:  mvp2_eval_ced_kl001_r4_high
442	  status:  DONE
443	  FULL CMD: python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 60,70,80,90 --quantize --resume
444	
445	  exp_id:  mvp2_eval_ced_kl001_r4_multi
446	  status:  DONE
447	  FULL CMD: CUDA_VISIBLE_DEVICES=2 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 10,20,30,40,60,70,80 --quantize --resume
448	
449	  exp_id:  mvp2_eval_ced_kl001_r4_step100
450	  status:  DONE
451	  FULL CMD: python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001_step100 --checkpoints 100 --quantize
452	
453	  exp_id:  mvp2_eval_ced_kl001_r4_step90
454	  status:  DONE
455	  FULL CMD: bash -c "source /etc/network_turbo && ... && python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 90 --quantize"
456	
457	  exp_id:  mvp2_eval_lr5e6_r1_ckpt100
458	  status:  DONE
459	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-100 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/lr5e6_r1_ckpt100/checkpoint-100 --quantize"
460	
461	  exp_id:  mvp2_eval_lr5e6_r1_ckpt20
462	  status:  DONE
463	  FULL CMD: bash /root/autodl-tmp/scripts/eval_lr5e6_ckpt20.sh
464	
465	  exp_id:  mvp2_eval_lr5e6_r1_ckpt40
466	  status:  DONE
467	  FULL CMD: bash /root/autodl-tmp/scripts/eval_lr5e6_ckpt40.sh
468	
469	  exp_id:  mvp2_eval_lr5e6_r1_ckpt40_r2
470	  status:  DONE
471	  FULL CMD: CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference
472	
473	  exp_id:  mvp2_eval_lr5e6_r1_ckpt60_r2
474	  status:  DONE
475	  FULL CMD: CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-60 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60 --quantize
476	
477	  exp_id:  mvp2_eval_lr5e6_r1_ckpt80
478	  status:  DONE
479	  FULL CMD: CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-80 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/lr5e6_r1_ckpt80/checkpoint-80 --quantize
480	
481	  exp_id:  mvp2_eval_lr5e6_rp_r2_ckpt20
482	  status:  DONE
483	  FULL CMD: CUDA_VISIBLE_DEVICES=3 python eval rp_r2 ckpt-20
484	
485	  exp_id:  mvp2_eval_sft_baseline
486	  status:  DONE
487	  FULL CMD: python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/sft_baseline_eval_results --quantize
488	
489	  exp_id:  mvp2_rsft_r2a
490	  status:  DONE
491	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train_clean.jsonl --output_dir /root/autodl-tmp/rsft_output_r2a --learning_rate 2e-5 --num_epochs 1 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --save_steps 50 --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-r2a --seed 42"
492	
493	  exp_id:  mvp2_rsft_r2b
494	  status:  DONE
495	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train_clean.jsonl --output_dir /root/autodl-tmp/rsft_output_r2b --learning_rate 1e-5 --num_epochs 1 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 32 --weighted_sampling --save_steps 50 --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-r2b --seed 42"
496	
497	  exp_id:  mvp2_rsft_train_r1
498	  status:  DONE
499	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1 --seed 42"
500	
501	  exp_id:  mvp2_rsft_train_r1_s43
502	  status:  DONE
503	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_s43 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1-s43 --seed 43"
504	
505	  exp_id:  mvp2_rsft_train_r1_s44
506	  status:  DONE
507	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_s44 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1-s44 --seed 44"
508	
509	  exp_id:  mvp2_sft_eval
510	  status:  DONE
511	  FULL CMD: python -m freige.eval.inference --model_path sft_output --base_model Qwen3-4B --split dev
512	
513	  exp_id:  mvp2_sft_eval_r2
514	  status:  DONE
515	  FULL CMD: python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_results --seed 42
516	
517	  exp_id:  mvp2_sft_eval_r3
518	  status:  DONE
519	  FULL CMD: bash -c "source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_r3_results --seed 42"
520	
521	  exp_id:  plan_001_flat_nli_seed43
522	  status:  DONE
523	  FULL CMD: python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_flat_nli_s43 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 16 --lora_rank 64 --lora_alpha 128 --eval_data_dir /root/autodl-tmp/data/docred --wandb_run_name plan_001_flat_nli_seed43 --seed 43
524	
525	  exp_id:  plan_009_flatnli_reward_eval
526	  status:  DONE
527	  FULL CMD: 
528	
529	  exp_id:  reeval_flat_nli_s43
530	  status:  DONE
531	  FULL CMD: Re-eval flat-NLI RSFT seed=43 with --sft_adapter (D064 fix)
532	
533	  exp_id:  rsft_ced_s45_train_r2
534	  status:  DONE
535	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_ced_s45 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-s45-r2 --seed 45"
536	
537	
538	========================================================================================================================
539	SPECIAL ANALYSIS: Evals with non-standard batch_size or max_new_tokens
540	========================================================================================================================
541	
542	  exp_id:  eval_plan_001_flat_nli
543	  status:  DONE
544	  issues:  batch_size=16
545	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli --sft_adapter /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli --no-quantize"
546	
547	  exp_id:  eval_plan_001_flat_nli_s43
548	  status:  DONE
549	  issues:  batch_size=16
550	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s43 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 43 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s43 --no-quantize"
551	
552	  exp_id:  eval_plan_008_rsft_topk3
553	  status:  DONE
554	  issues:  batch_size=16
555	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_topk3_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_topk3 --no-quantize"
556	
557	  exp_id:  eval_plan_008_topk3_fixed
558	  status:  DONE
559	  issues:  batch_size=16
560	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_topk3_output --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_topk3_fixed --no-quantize"
561	
562	  exp_id:  eval_plan_012_dpo_1ep_fixed
563	  status:  DONE
564	  issues:  batch_size=16
565	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/dpo_output_1ep/ --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/dpo_ced_1ep_fixed --no-quantize"
566	
567	  exp_id:  eval_plan_012_dpo_ced_1ep
568	  status:  DONE
569	  issues:  batch_size=16
570	  FULL CMD: python -m freige.eval.inference --model_path /root/autodl-tmp/dpo_output_1ep/ --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/dpo_ced_1ep --no-quantize
571	
572	  exp_id:  eval_plan_012_dpo_ced_ckpt400
573	  status:  DONE
574	  issues:  batch_size=16
575	  FULL CMD: python -m freige.eval.inference --model_path /root/autodl-tmp/dpo_output/checkpoint-400 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/dpo_ced_ckpt400 --no-quantize
576	
577	  exp_id:  eval_sft_baseline_noquant
578	  status:  DONE
579	  issues:  batch_size=16
580	  FULL CMD: python eval.py --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/sft_baseline_noquant --batch_size 16 --max_new_tokens 1024 --split dev --seed 42
581	
582	  exp_id:  mvp2_eval_lr5e6_r1_ckpt100
583	  status:  DONE
584	  issues:  batch_size=16
585	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-100 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/lr5e6_r1_ckpt100/checkpoint-100 --quantize"
586	
587	  exp_id:  mvp2_eval_lr5e6_r1_ckpt60_r2
588	  status:  DONE
589	  issues:  batch_size=16
590	  FULL CMD: CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-60 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60 --quantize
591	
592	  exp_id:  mvp2_eval_lr5e6_r1_ckpt80
593	  status:  DONE
594	  issues:  batch_size=16
595	  FULL CMD: CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-80 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/lr5e6_r1_ckpt80/checkpoint-80 --quantize
596	
597	  exp_id:  mvp2_eval_rsft_r2b_maxtok1536
598	  status:  DONE
599	  issues:  max_new_tokens=1536
600	  FULL CMD: python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_r2b --data_path /root/autodl-tmp/data/docred --no-quantize --max_new_tokens 1536 --output_dir /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536
601	
602	  exp_id:  mvp2_eval_rsft_r2b_maxtok1536_r2
603	  status:  DONE
604	  issues:  max_new_tokens=1536
605	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && rm -rf /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536/* && python -m freige.eval.inference --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --model_path /root/autodl-tmp/rsft_output_r2b --data_path /root/autodl-tmp/data/docred --no-quantize --max_new_tokens 1536 --output_dir /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536"
606	
607	  exp_id:  mvp2_eval_sft_baseline
608	  status:  DONE
609	  issues:  batch_size=16
610	  FULL CMD: python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/sft_baseline_eval_results --quantize
611	
612	  exp_id:  mvp2_sft_eval_r2
613	  status:  DONE
614	  issues:  batch_size=16
615	  FULL CMD: python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_results --seed 42
616	
617	  exp_id:  mvp2_sft_eval_r3
618	  status:  DONE
619	  issues:  batch_size=16
620	  FULL CMD: bash -c "source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_r3_results --seed 42"
621	
622	  exp_id:  plan_002_test_eval_s44
623	  status:  DONE
624	  issues:  batch_size=16
625	  FULL CMD: python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44 --sft_adapter /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split test --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/test_rsft_s44 --no-quantize
626	
627	  exp_id:  plan_011_grpo_g8_bf16_eval
628	  status:  DONE
629	  issues:  batch_size=16
630	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_g8_bf16/checkpoint-100 --sft_adapter /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/grpo_g8_bf16_ckpt100 --no-quantize"
631	
632	  exp_id:  reeval_rsft_topk3
633	  status:  DONE
634	  issues:  batch_size=16
635	  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_topk3_output/checkpoint-1509 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_topk3_reeval --no-quantize"
636	
637	
638	========================================================================================================================
639	OVERALL D076 COMPLIANCE: 11/84 compliant, 73/84 non-compliant
640	========================================================================================================================
641	
642	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d490c66c-1fb4-4a19-b07c-6b19884f23c9",
  "isSidechain": true,
  "promptId": "23faa4e2-0c97-47f8-be9e-f272ba775828",
  "agentId": "a35180a8a436e895f",
  "type": "user",
  "uuid": "749c58a9-81c8-4192-ac1b-014ecae6af5a",
  "sourceToolAssistantUUID": "d490c66c-1fb4-4a19-b07c-6b19884f23c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-18T22:07:00.424Z_

Now let me also look at the detailed per-experiment output to find any metrics that were stored in nested locations. Let me check the experiments that were marked as having metrics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "749c58a9-81c8-4192-ac1b-014ecae6af5a",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAo4XaEgT3BQydgXwjBF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b3d846b-c556-45e9-b571-94676bea1d0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANdHEbLJ82uvX16hS9tq5G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15175,
      "cache_read_input_tokens": 45512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15175,
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

_source line 31 · 2026-05-18T22:07:12.356Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gy2EJVSwjt9cmM72fn31Zq`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nfpath = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt'\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\nresult_str = raw.get('result', raw)\nif isinstance(result_str, str):\n    data = json.loads(result_str)\nelse:\n    data = result_str\n\nexperiments = data['data']['experiments']\n\n# Find all 4B eval experiments and dump ALL nested data to find metrics\nfor exp_id, exp in sorted(experiments.items()):\n    is_4b = False\n    cmd = exp.get('spec', {}).get('command', '')\n    hypothesis = exp.get('hypothesis', '')\n    model_name = exp.get('spec', {}).get('model_name', '')\n    checks = [cmd, hypothesis, model_name, exp_id]\n    for c in checks:\n        if c and ('4b' in c.lower() or '4B' in c or 'Qwen3-4B' in c):\n            is_4b = True\n            break\n    if not is_4b:\n        continue\n    is_eval = 'eval' in exp_id.lower() or ('eval' in cmd.lower() and 'inference' in cmd.lower()) or 'eval' in hypothesis.lower()\n    if not is_eval:\n        continue\n\n    # Deep search for any key containing 'f1' or 'metric' in all nested dicts\n    def find_metrics(obj, path=''):\n        results = []\n        if isinstance(obj, dict):\n            for k, v in obj.items():\n                new_path = f'{path}.{k}' if path else k\n                if any(kw in k.lower() for kw in ['f1', 'metric', 'score', 'precision', 'recall', 'accuracy', 'edcr']):\n                    results.append((new_path, v))\n                results.extend(find_metrics(v, new_path))\n        elif isinstance(obj, list):\n            for i, v in enumerate(obj):\n                results.extend(find_metrics(v, f'{path}[{i}]'))\n        return results\n\n    metrics_found = find_metrics(exp)\n    if metrics_found:\n        print(f'{exp_id}:')\n        for path, val in metrics_found:\n            print(f'  {path} = {val}')\n\" 2>&1",
  "description": "Deep search for metrics in all 4B eval experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b3d846b-c556-45e9-b571-94676bea1d0f",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAo4XaEgT3BQydgXwjBF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f6fb1fb-39ac-4ee2-bfb5-be3a7ea436b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANdHEbLJ82uvX16hS9tq5G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15175,
      "cache_read_input_tokens": 45512,
      "output_tokens": 788,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15175
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 788,
          "cache_read_input_tokens": 45512,
          "cache_creation_input_tokens": 15175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15175,
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

_source line 32 · 2026-05-18T22:07:12.485Z_

<details><summary>↩ Tool result · `toolu_01Gy2EJVSwjt9cmM72fn31Zq`</summary>

```text
eval_flat_nli_s44:
  metrics = {'rel_f1': 0.461506, 'ign_f1': 0.452126, 'evi_f1': 0.813123, 'edcr': 0.645808, 'evi_f1_joint': 0.359673}
  metrics.rel_f1 = 0.461506
  metrics.ign_f1 = 0.452126
  metrics.evi_f1 = 0.813123
  metrics.edcr = 0.645808
  metrics.evi_f1_joint = 0.359673
eval_flat_nli_seed45:
  metrics = {'rel_f1': 0.455052, 'ign_f1': 0.446181, 'evi_f1': 0.815399, 'edcr': 0.652133, 'evi_f1_joint': 0.355612}
  metrics.rel_f1 = 0.455052
  metrics.ign_f1 = 0.446181
  metrics.evi_f1 = 0.815399
  metrics.edcr = 0.652133
  metrics.evi_f1_joint = 0.355612
eval_grpo_g8_bf16:
  metrics = {'ckpt80_rel_f1': 0.4456, 'ckpt80_ign_f1': 0.4456, 'ckpt80_evi_f1': 0.8034, 'ckpt80_edcr': 0.6409, 'ckpt80_format_ok': '984/985', 'ckpt80_truncated': 50, 'ckpt90_rel_f1': 0.4523, 'ckpt90_ign_f1': 0.4523, 'ckpt90_evi_f1': 0.8052, 'ckpt90_edcr': 0.6414, 'ckpt90_format_ok': '983/985', 'ckpt90_truncated': 61, 'ckpt100_rel_f1': 0.4549, 'ckpt100_ign_f1': 0.4549, 'ckpt100_evi_f1': 0.8086, 'ckpt100_edcr': 0.6318, 'ckpt100_format_ok': '985/985', 'ckpt100_truncated': 61, 'best_checkpoint': 'ckpt-100'}
  metrics.ckpt80_rel_f1 = 0.4456
  metrics.ckpt80_ign_f1 = 0.4456
  metrics.ckpt80_evi_f1 = 0.8034
  metrics.ckpt80_edcr = 0.6409
  metrics.ckpt90_rel_f1 = 0.4523
  metrics.ckpt90_ign_f1 = 0.4523
  metrics.ckpt90_evi_f1 = 0.8052
  metrics.ckpt90_edcr = 0.6414
  metrics.ckpt100_rel_f1 = 0.4549
  metrics.ckpt100_ign_f1 = 0.4549
  metrics.ckpt100_evi_f1 = 0.8086
  metrics.ckpt100_edcr = 0.6318
eval_plan_001_flat_nli:
  metrics = {'rel_f1': 0.4539, 'ign_f1': 0.4539, 'evi_f1': 0.8043, 'edcr': 0.6431, 'precision': 0.4671, 'recall': 0.4414, 'evi_precision': 0.8143, 'evi_recall': 0.7945, 'format_ok_rate': 1, 'n_truncated': 199, 'n_documents': 985, 'n_predictions': 15294, 'inference_time_seconds': 3631}
  metrics.rel_f1 = 0.4539
  metrics.ign_f1 = 0.4539
  metrics.evi_f1 = 0.8043
  metrics.edcr = 0.6431
  metrics.precision = 0.4671
  metrics.recall = 0.4414
  metrics.evi_precision = 0.8143
  metrics.evi_recall = 0.7945
eval_plan_001_flat_nli_s43:
  metrics = {'rel_f1': 0.0022, 'ign_f1': 0.0022, 'evi_f1': 0.8533, 'edcr': 0.9982, 'num_preds': 17285, 'format_ok': '981/985', 'truncated': '251/985', 'tp': 32, 'note': 'INVALID — missing --sft_adapter, same bug as DPO 1ep eval'}
  metrics.rel_f1 = 0.0022
  metrics.ign_f1 = 0.0022
  metrics.evi_f1 = 0.8533
  metrics.edcr = 0.9982
eval_plan_008_rsft_topk3:
  metrics = {'note': 'INVALID — missing --sft_adapter, killed by Director instruction'}
eval_plan_012_dpo_1ep_fixed_r2:
  metrics = {'rel_f1': 0.4034, 'evi_f1': 0.8088, 'edcr': 0.7139, 'format_ok_rate': 0.999, 'truncated_rate': 0.343, 'predictions': 19107, 'ign_f1': 0.4034, 'precision': 0.3809, 'recall': 0.4287, 'vs_sft_delta': -0.0023, 'note': 'DPO 1ep matches SFT baseline. 1ep→3ep trajectory shows gradual decoupling (rel_f1↓ evi_f1↑), consistent with GRPO pattern. Ign-F1=F1 exact match needs investigation.'}
  metrics.rel_f1 = 0.4034
  metrics.evi_f1 = 0.8088
  metrics.edcr = 0.7139
  metrics.ign_f1 = 0.4034
  metrics.precision = 0.3809
  metrics.recall = 0.4287
eval_plan_012_dpo_ced_1ep:
  metrics = {'rel_f1': 0.0022, 'ign_f1': 0.0022, 'evi_f1': 0.75, 'edcr': 0.9982, 'num_preds': 19265, 'format_ok': '981/985', 'truncated': '358/985', 'tp': 34, 'inference_time_s': 3643}
  metrics.rel_f1 = 0.0022
  metrics.ign_f1 = 0.0022
  metrics.evi_f1 = 0.75
  metrics.edcr = 0.9982
eval_plan_014_no_evidence_r2:
  metrics = {'rel_f1': 0.4876, 'ign_f1': 0.4721, 'evi_f1': 0, 'edcr': 0, 'evi_f1_joint': 0, 'precision': 0.4901, 'recall': 0.4851, 'ign_precision': 0.4654, 'ign_recall': 0.4791, 'format_compliance': 0.993, 'truncation_rate': 0.312, 'n_predictions': 21181, 'n_documents': 985}
  metrics.rel_f1 = 0.4876
  metrics.ign_f1 = 0.4721
  metrics.evi_f1 = 0
  metrics.edcr = 0
  metrics.evi_f1_joint = 0
  metrics.precision = 0.4901
  metrics.recall = 0.4851
  metrics.ign_precision = 0.4654
  metrics.ign_recall = 0.4791
eval_rsft_ced_s43:
  metrics = {'rel_f1': 0.4601, 'ign_f1': 0.4512, 'precision': 0.4696, 'recall': 0.4509, 'evi_f1': 0.8063, 'evi_precision': 0.8025, 'evi_recall': 0.8101, 'edcr': 0.6542, 'evi_f1_joint': 0.3605, 'format_ok_rate': 1, 'n_truncated': 184, 'n_predictions': 15051, 'inference_time_seconds': 10768.2}
  metrics.rel_f1 = 0.4601
  metrics.ign_f1 = 0.4512
  metrics.precision = 0.4696
  metrics.recall = 0.4509
  metrics.evi_f1 = 0.8063
  metrics.evi_precision = 0.8025
  metrics.evi_recall = 0.8101
  metrics.edcr = 0.6542
  metrics.evi_f1_joint = 0.3605
eval_rsft_ced_s45:
  metrics = {'rel_f1': 0.4514, 'ign_f1': 0.4416, 'evi_f1': 0.8174, 'rel_p': 0.4718, 'rel_r': 0.4326, 'edcr': 0.655, 'evi_f1_joint': 0.3558, 'n_truncated': 206, 'format_ok_rate': 1}
  metrics.rel_f1 = 0.4514
  metrics.ign_f1 = 0.4416
  metrics.evi_f1 = 0.8174
  metrics.edcr = 0.655
  metrics.evi_f1_joint = 0.3558
eval_sft_baseline_noquant:
  metrics = {'rel_f1': 0.4106, 'rel_precision': 0.4198, 'rel_recall': 0.4019, 'evi_f1': 0.8013, 'evi_precision': 0.8005, 'evi_recall': 0.8022, 'evi_f1_joint': 0.3216, 'edcr': 0.7039, 'format_ok_rate': 0.998, 'field_compliance_rate': 0.7066, 'n_predictions': 16774, 'n_truncated': 288, 'n_documents': 985, 'inference_time_seconds': 3677.9}
  metrics.rel_f1 = 0.4106
  metrics.rel_precision = 0.4198
  metrics.rel_recall = 0.4019
  metrics.evi_f1 = 0.8013
  metrics.evi_precision = 0.8005
  metrics.evi_recall = 0.8022
  metrics.evi_f1_joint = 0.3216
  metrics.edcr = 0.7039
grpo_bf16_g4_ckpt100_eval:
  metrics = {'ign_f1': 0.4431, 'f1': 0.4511, 'evi_f1': 0.801, 'evi_f1_joint': 0.3532, 'EDCR': 0.6453, 'format_compliance': 0.999, 'field_compliance': 0.8142, 'truncated': 182, 'n_total': 985, 'n_predictions': 15187, 'inference_time_seconds': 11458.2}
  metrics.ign_f1 = 0.4431
  metrics.f1 = 0.4511
  metrics.evi_f1 = 0.801
  metrics.evi_f1_joint = 0.3532
  metrics.EDCR = 0.6453
lead2_ckpt20_eval:
  metrics = {'rel_f1': 0.4617, 'ign_f1': 0.4533, 'evi_f1': 0.8103, 'evi_f1_joint': 0.3642, 'edcr': 0.6465, 'precision': 0.476, 'recall': 0.4482, 'format_ok': '985/985', 'truncated': '187/985', 'predictions': 14998}
  metrics.rel_f1 = 0.4617
  metrics.ign_f1 = 0.4533
  metrics.evi_f1 = 0.8103
  metrics.evi_f1_joint = 0.3642
  metrics.edcr = 0.6465
  metrics.precision = 0.476
  metrics.recall = 0.4482
mvp2_eval_ced_kl001_r4_ckpt10:
  metrics = {'rel_f1': 0.00296, 'rel_precision': 0.00314, 'rel_recall': 0.0028, 'evi_f1': 0.72, 'evi_precision': 0.6429, 'evi_recall': 0.8182, 'edcr': 0.9983, 'n_parseable': 984, 'n_truncated': 24, 'n_predictions': 11621, 'tp': 34, 'pred_count': 10839, 'gold_count': 12151, 'inference_time_seconds': 5211.4}
  metrics.rel_f1 = 0.00296
  metrics.rel_precision = 0.00314
  metrics.rel_recall = 0.0028
  metrics.evi_f1 = 0.72
  metrics.evi_precision = 0.6429
  metrics.evi_recall = 0.8182
  metrics.edcr = 0.9983
mvp2_eval_ced_kl001_r4_early:
  metrics = {'f1': 0.1563, 'ign_f1': 0.1563, 'evi_f1': 0.5643, 'edcr': 0.8858, 'precision': 0.2356, 'recall': 0.1169, 'evi_precision': 0.4864, 'evi_recall': 0.6721, 'format_ok_rate': 0.999, 'n_parseable': 984, 'n_truncated': 11, 'n_predictions': 9250, 'tp': 1421, 'pred_count': 6032, 'gold_count': 12151}
  metrics.f1 = 0.1563
  metrics.ign_f1 = 0.1563
  metrics.evi_f1 = 0.5643
  metrics.edcr = 0.8858
  metrics.precision = 0.2356
  metrics.recall = 0.1169
  metrics.evi_precision = 0.4864
  metrics.evi_recall = 0.6721
mvp2_eval_ced_kl001_r4_high:
  metrics = {'checkpoint_60': {'rel_f1': 0.1467, 'ign_f1': 0.1467, 'precision': 0.1909, 'recall': 0.1192, 'evi_f1': 0.5763, 'edcr': 0.9062, 'pred_count': 10041, 'gold_count': 12151, 'n_truncated': 16, 'format_ok_rate': 1}, 'note': 'Only ckpt-60 completed. Process died during ckpt-70 inference at 8% (5/62 batch). ckpt-80/90 never started.'}
  metrics.checkpoint_60.rel_f1 = 0.1467
  metrics.checkpoint_60.ign_f1 = 0.1467
  metrics.checkpoint_60.precision = 0.1909
  metrics.checkpoint_60.recall = 0.1192
  metrics.checkpoint_60.evi_f1 = 0.5763
  metrics.checkpoint_60.edcr = 0.9062
mvp2_eval_ced_kl001_r4_multi:
  metrics = {'checkpoint-10': {'f1': 0.003, 'ign_f1': 0.003, 'evi_f1': 0.72, 'edcr': 0.9983, 'format_ok_rate': 0.999}, 'checkpoint-20': {'f1': 0.0088, 'ign_f1': 0.0088, 'evi_f1': 0.423, 'edcr': 0.9954, 'format_ok_rate': 0.999}, 'checkpoint-30': {'f1': 0.0338, 'ign_f1': 0.0338, 'evi_f1': 0.5889, 'edcr': 0.9798, 'format_ok_rate': 1}, 'checkpoint-50': {'f1': 0.1563, 'ign_f1': 0.1563, 'evi_f1': 0.5643, 'edcr': 0.8858, 'format_ok_rate': 0.999}, 'checkpoint-60': {'f1': 0.1467, 'ign_f1': 0.1467, 'evi_f1': 0.5763, 'edcr': 0.9062, 'format_ok_rate': 1}, 'checkpoint-90': {'f1': 0.2108, 'ign_f1': 0.2108, 'evi_f1': 0.5666, 'edcr': 0.8584, 'format_ok_rate': 1}}
  metrics.checkpoint-10.f1 = 0.003
  metrics.checkpoint-10.ign_f1 = 0.003
  metrics.checkpoint-10.evi_f1 = 0.72
  metrics.checkpoint-10.edcr = 0.9983
  metrics.checkpoint-20.f1 = 0.0088
  metrics.checkpoint-20.ign_f1 = 0.0088
  metrics.checkpoint-20.evi_f1 = 0.423
  metrics.checkpoint-20.edcr = 0.9954
  metrics.checkpoint-30.f1 = 0.0338
  metrics.checkpoint-30.ign_f1 = 0.0338
  metrics.checkpoint-30.evi_f1 = 0.5889
  metrics.checkpoint-30.edcr = 0.9798
  metrics.checkpoint-50.f1 = 0.1563
  metrics.checkpoint-50.ign_f1 = 0.1563
  metrics.checkpoint-50.evi_f1 = 0.5643
  metrics.checkpoint-50.edcr = 0.8858
  metrics.checkpoint-60.f1 = 0.1467
  metrics.checkpoint-60.ign_f1 = 0.1467
  metrics.checkpoint-60.evi_f1 = 0.5763
  metrics.checkpoint-60.edcr = 0.9062
  metrics.checkpoint-90.f1 = 0.2108
  metrics.checkpoint-90.ign_f1 = 0.2108
  metrics.checkpoint-90.evi_f1 = 0.5666
  metrics.checkpoint-90.edcr = 0.8584
mvp2_eval_ced_kl001_r4_step100:
  metrics = {'rel_f1': 0.2167, 'ign_f1': 0.2167, 'precision': 0.2849, 'recall': 0.1749, 'evi_f1': 0.5746, 'evi_precision': 0.5244, 'evi_recall': 0.6353, 'edcr': 0.8539, 'pred_count': 7460, 'gold_count': 12151, 'tp': 2125, 'n_truncated': 21, 'format_ok_rate': 1}
  metrics.rel_f1 = 0.2167
  metrics.ign_f1 = 0.2167
  metrics.precision = 0.2849
  metrics.recall = 0.1749
  metrics.evi_f1 = 0.5746
  metrics.evi_precision = 0.5244
  metrics.evi_recall = 0.6353
  metrics.edcr = 0.8539
mvp2_eval_ced_kl001_r4_step90:
  metrics = {'rel_f1': 0.2108, 'ign_f1': 0.2108, 'evi_f1': 0.5666, 'edcr': 0.8584, 'pred_count': 11160, 'n_truncated': 22, 'format_ok_rate': 1, 'n_documents': 985}
  metrics.rel_f1 = 0.2108
  metrics.ign_f1 = 0.2108
  metrics.evi_f1 = 0.5666
  metrics.edcr = 0.8584
mvp2_eval_lr5e6_r1_ckpt100:
  metrics = {'rel_f1': 0.0138, 'rel_precision': 0.0132, 'rel_recall': 0.0144, 'ign_f1': 0.0138, 'evi_f1': 0.8504, 'evi_precision': 0.9256, 'evi_recall': 0.7866, 'edcr': 0.9876, 'format_ok_rate': 0.999, 'field_compliance_rate': 0.8162, 'evidence_format_rate': 0.8162, 'tp': 175, 'pred_count': 13300, 'gold_count': 12151, 'n_predictions': 15498, 'n_truncated': 181, 'n_documents': 985, 'n_parseable': 984, 'inference_time_seconds': 5901.7}
  metrics.rel_f1 = 0.0138
  metrics.rel_precision = 0.0132
  metrics.rel_recall = 0.0144
  metrics.ign_f1 = 0.0138
  metrics.evi_f1 = 0.8504
  metrics.evi_precision = 0.9256
  metrics.evi_recall = 0.7866
  metrics.edcr = 0.9876
mvp2_eval_lr5e6_r1_ckpt20:
  metrics = {'rel_f1': 0.0077, 'rel_precision': 0.0071, 'rel_recall': 0.0084, 'evi_f1': 0.628, 'evi_precision': 0.855, 'evi_recall': 0.496, 'edcr': 0.993, 'format_ok_rate': 0.991, 'field_compliance_rate': 0.399, 'pred_count': 14440, 'gold_count': 12151, 'tp': 102, 'n_truncated': 587, 'inference_time_seconds': 6370.4}
  metrics.rel_f1 = 0.0077
  metrics.rel_precision = 0.0071
  metrics.rel_recall = 0.0084
  metrics.evi_f1 = 0.628
  metrics.evi_precision = 0.855
  metrics.evi_recall = 0.496
  metrics.edcr = 0.993
mvp2_eval_lr5e6_r1_ckpt40_r2:
  spec.metrics = {'f1': 0.007146887342486364, 'ign_f1': 0.007146887342486364, 'precision': 0.0065816821393931, 'recall': 0.007818286560776891, 'evi_f1': 0.7583892617449665, 'edcr': 0.9942045337983383, 'format_ok_rate': 0.9939086294416244, 'tp': 95, 'pred_count': 14434, 'gold_count': 12151, 'n_truncated': 424, 'inference_time_seconds': 6152.4}
  spec.metrics.f1 = 0.007146887342486364
  spec.metrics.ign_f1 = 0.007146887342486364
  spec.metrics.precision = 0.0065816821393931
  spec.metrics.recall = 0.007818286560776891
  spec.metrics.evi_f1 = 0.7583892617449665
  spec.metrics.edcr = 0.9942045337983383
  metrics = {'rel_f1': 0.0071, 'precision': 0.0066, 'recall': 0.0078, 'evi_f1': 0.7584, 'evi_precision': 0.9113, 'evi_recall': 0.6494, 'edcr': 0.9942, 'format_ok_rate': 0.9939, 'field_compliance_rate': 0.5675, 'pred_count': 14434, 'gold_count': 12151, 'tp': 95, 'n_truncated': 424, 'inference_time_seconds': 6152}
  metrics.rel_f1 = 0.0071
  metrics.precision = 0.0066
  metrics.recall = 0.0078
  metrics.evi_f1 = 0.7584
  metrics.evi_precision = 0.9113
  metrics.evi_recall = 0.6494
  metrics.edcr = 0.9942
mvp2_eval_lr5e6_r1_ckpt60_r2:
  metrics = {'rel_f1': 0.0093, 'precision': 0.0085, 'recall': 0.0103, 'evi_f1': 0.81, 'edcr': 0.993, 'format_ok_rate': 0.998, 'pred_count': 14626, 'gold_count': 12151, 'tp': 125, 'inference_time_seconds': 6152}
  metrics.rel_f1 = 0.0093
  metrics.precision = 0.0085
  metrics.recall = 0.0103
  metrics.evi_f1 = 0.81
  metrics.edcr = 0.993
mvp2_eval_lr5e6_r1_ckpt80:
  metrics = {'rel_f1': 0.0116, 'ign_f1': 0.0116, 'precision': 0.0109, 'recall': 0.0124, 'evi_f1': 0.828, 'evi_precision': 0.928, 'evi_recall': 0.748, 'edcr': 0.993, 'format_ok_rate': 0.999, 'field_compliance_rate': 0.788, 'pred_count': 13828, 'gold_count': 12151, 'n_truncated': 210, 'inference_time_seconds': 6099}
  metrics.rel_f1 = 0.0116
  metrics.ign_f1 = 0.0116
  metrics.precision = 0.0109
  metrics.recall = 0.0124
  metrics.evi_f1 = 0.828
  metrics.evi_precision = 0.928
  metrics.evi_recall = 0.748
  metrics.edcr = 0.993
mvp2_eval_rsft_r1:
  metrics = {'rel_f1': 0.4449, 'evi_f1': 0.8187, 'evi_f1_joint': 0.3468, 'evi_f1_joint_P': 0.3515, 'evi_f1_joint_R': 0.3423, 'edcr': 0.6565, 'num_preds': 15307, 'sft_baseline_rel_f1': 0.4057, 'sft_baseline_evi_f1': 0.7979, 'delta_rel_f1': 0.0392, 'delta_evi_f1': 0.0208, 'delta_evi_f1_joint': 0.0351, 'mvp2_pass': True}
  metrics.rel_f1 = 0.4449
  metrics.evi_f1 = 0.8187
  metrics.evi_f1_joint = 0.3468
  metrics.evi_f1_joint_P = 0.3515
  metrics.evi_f1_joint_R = 0.3423
  metrics.edcr = 0.6565
  metrics.sft_baseline_rel_f1 = 0.4057
  metrics.sft_baseline_evi_f1 = 0.7979
  metrics.delta_rel_f1 = 0.0392
  metrics.delta_evi_f1 = 0.0208
  metrics.delta_evi_f1_joint = 0.0351
mvp2_eval_rsft_r2a:
  metrics = {'rel_f1': 0.4494, 'ign_f1': 0.4494, 'evi_f1': 0.8108, 'evi_f1_joint': 0.3509, 'evi_f1_joint_P': 0.3423, 'evi_f1_joint_R': 0.3599, 'edcr': 0.6641, 'precision': 0.4512, 'recall': 0.4475, 'evi_precision': 0.8143, 'evi_recall': 0.8073, 'format_ok_rate': 1, 'n_predictions': 15482, 'n_truncated': 208, 'inference_time_s': 5967.2, 'delta_evi_f1_joint': 0.0392}
  metrics.rel_f1 = 0.4494
  metrics.ign_f1 = 0.4494
  metrics.evi_f1 = 0.8108
  metrics.evi_f1_joint = 0.3509
  metrics.evi_f1_joint_P = 0.3423
  metrics.evi_f1_joint_R = 0.3599
  metrics.edcr = 0.6641
  metrics.precision = 0.4512
  metrics.recall = 0.4475
  metrics.evi_precision = 0.8143
  metrics.evi_recall = 0.8073
  metrics.delta_evi_f1_joint = 0.0392
mvp2_eval_rsft_r2b:
  metrics = {'rel_f1': 0.4493, 'ign_f1': 0.4493, 'evi_f1': 0.8128, 'evi_f1_joint': 0.349, 'evi_f1_joint_P': 0.3455, 'evi_f1_joint_R': 0.3526, 'edcr': 0.6609, 'precision': 0.4566, 'recall': 0.4424, 'evi_precision': 0.8201, 'evi_recall': 0.8056, 'pred_count': 14829, 'format_ok': '983/985', 'truncated': 179, 'inference_time_s': 5862, 'delta_evi_f1_joint': 0.0373}
  metrics.rel_f1 = 0.4493
  metrics.ign_f1 = 0.4493
  metrics.evi_f1 = 0.8128
  metrics.evi_f1_joint = 0.349
  metrics.evi_f1_joint_P = 0.3455
  metrics.evi_f1_joint_R = 0.3526
  metrics.edcr = 0.6609
  metrics.precision = 0.4566
  metrics.recall = 0.4424
  metrics.evi_precision = 0.8201
  metrics.evi_recall = 0.8056
  metrics.delta_evi_f1_joint = 0.0373
mvp2_eval_rsft_r2b_maxtok1536_r2:
  metrics = {'rel_f1': 0.4504, 'ign_f1': 0.4504, 'evi_f1': 0.8102, 'edcr': 0.674, 'precision': 0.4488, 'recall': 0.4519, 'evi_precision': 0.8162, 'evi_recall': 0.8044, 'n_truncated': 146, 'n_total': 985, 'n_predictions': 17188, 'n_distractor_citations': 19589, 'n_total_citations': 29063, 'format_ok_rate': 0.998}
  metrics.rel_f1 = 0.4504
  metrics.ign_f1 = 0.4504
  metrics.evi_f1 = 0.8102
  metrics.edcr = 0.674
  metrics.precision = 0.4488
  metrics.recall = 0.4519
  metrics.evi_precision = 0.8162
  metrics.evi_recall = 0.8044
mvp2_eval_rsft_s43_r2:
  metrics = {'rel_f1': 0.4683, 'ign_f1': 0.4683, 'evi_f1': 0.8156, 'evi_f1_joint': 0.3711, 'evi_f1_joint_P': 0.3747, 'evi_f1_joint_R': 0.3675, 'edcr': 0.6388, 'precision': 0.4817, 'recall': 0.4556, 'evi_precision': 0.8142, 'evi_recall': 0.817, 'n_predictions': 14970, 'n_truncated': 171, 'format_ok_rate': 1, 'inference_time_s': 6316.7, 'sft_baseline_rel_f1': 0.4057, 'sft_baseline_evi_f1': 0.7979, 'delta_rel_f1': 0.0626, 'delta_evi_f1': 0.0177, 'delta_evi_f1_joint': 0.0594, 'mvp2_pass': True}
  metrics.rel_f1 = 0.4683
  metrics.ign_f1 = 0.4683
  metrics.evi_f1 = 0.8156
  metrics.evi_f1_joint = 0.3711
  metrics.evi_f1_joint_P = 0.3747
  metrics.evi_f1_joint_R = 0.3675
  metrics.edcr = 0.6388
  metrics.precision = 0.4817
  metrics.recall = 0.4556
  metrics.evi_precision = 0.8142
  metrics.evi_recall = 0.817
  metrics.sft_baseline_rel_f1 = 0.4057
  metrics.sft_baseline_evi_f1 = 0.7979
  metrics.delta_rel_f1 = 0.0626
  metrics.delta_evi_f1 = 0.0177
  metrics.delta_evi_f1_joint = 0.0594
mvp2_eval_sft_baseline:
  metrics = {'rel_f1': 0.4057, 'evi_f1': 0.7979, 'evi_f1_joint': 0.3117, 'evi_f1_joint_P': 0.3037, 'evi_f1_joint_R': 0.32, 'edcr': 0.7118, 'pred_count': 12234, 'gold_count': 12151, 'format_ok_rate': 0.998, 'format_compliance_rate': 0.998, 'field_compliance_rate': 0.6264, 'n_truncated': 367, 'inference_time_seconds': 6138.5}
  metrics.rel_f1 = 0.4057
  metrics.evi_f1 = 0.7979
  metrics.evi_f1_joint = 0.3117
  metrics.evi_f1_joint_P = 0.3037
  metrics.evi_f1_joint_R = 0.32
  metrics.edcr = 0.7118
mvp2_sft_eval_r2:
  metrics = {'rel_f1': 0.4057, 'ign_f1': 0.4057, 'evi_f1': 0.7979, 'edcr': 0.7118, 'precision': 0.4043, 'recall': 0.407, 'evi_precision': 0.8035, 'evi_recall': 0.7924, 'format_ok_rate': 0.998, 'format_compliance_rate': 0.626, 'n_parseable': 617, 'n_truncated': 367, 'n_predictions': 18815, 'inference_time_seconds': 6484.7}
  metrics.rel_f1 = 0.4057
  metrics.ign_f1 = 0.4057
  metrics.evi_f1 = 0.7979
  metrics.edcr = 0.7118
  metrics.precision = 0.4043
  metrics.recall = 0.407
  metrics.evi_precision = 0.8035
  metrics.evi_recall = 0.7924
mvp2_sft_eval_r3:
  metrics = {'rel_f1': 0.4057, 'ign_f1': 0.4057, 'evi_f1': 0.7979, 'edcr': 0.7118, 'precision': 0.4043, 'recall': 0.407, 'evi_precision': 0.8035, 'evi_recall': 0.7924, 'format_ok_rate': 0.998, 'format_compliance_rate': 0.626, 'n_parseable': 617, 'n_truncated': 367, 'n_predictions': 18815}
  metrics.rel_f1 = 0.4057
  metrics.ign_f1 = 0.4057
  metrics.evi_f1 = 0.7979
  metrics.edcr = 0.7118
  metrics.precision = 0.4043
  metrics.recall = 0.407
  metrics.evi_precision = 0.8035
  metrics.evi_recall = 0.7924
plan_002_test_eval_s44_r2:
  spec.metrics = {'n_documents': 1000, 'n_predictions': 26925, 'n_codalab_entries': 25553, 'format_ok_rate': 0.996, 'n_truncated': 626, 'inference_time_s': 13850.5}
plan_002_test_rsft_s44:
  spec.metrics_note = Test set - no local gold labels. 1000 docs, 26925 predictions, 626 truncated, format_ok=99.6%. Needs CodaLab submission for official scores.
plan_006_qwen3_8b_no_evidence_eval_v2:
  spec.metrics = {'ign_f1': 0.5079, 'rel_f1': 0.5283, 'evi_f1': 0, 'edcr': 0, 'format_compliance_rate': 0.9949, 'n_total': 985, 'n_parseable': 980, 'n_truncated': 225, 'inference_time_seconds': 6402.2}
  spec.metrics.ign_f1 = 0.5079
  spec.metrics.rel_f1 = 0.5283
  spec.metrics.evi_f1 = 0
  spec.metrics.edcr = 0
plan_007_redocred_4b_sft_eval_r2:
  metrics = {'ign_f1': 0.3659, 'f1': 0.3706, 'evi_f1': 0.817, 'edcr': 0.6674, 'format_compliance_rate': 0.996, 'n_truncated': 139, 'n_total': 493, 'inference_time_seconds': 3281.7, 'precision': 0.4316, 'recall': 0.3247, 'ign_precision': 0.4134, 'ign_recall': 0.3282, 'evi_precision': 0.8208, 'evi_recall': 0.8131, 'n_predictions': 8191}
  metrics.ign_f1 = 0.3659
  metrics.f1 = 0.3706
  metrics.evi_f1 = 0.817
  metrics.edcr = 0.6674
  metrics.precision = 0.4316
  metrics.recall = 0.3247
  metrics.ign_precision = 0.4134
  metrics.ign_recall = 0.3282
  metrics.evi_precision = 0.8208
  metrics.evi_recall = 0.8131
plan_007_redocred_rsft_eval:
  metrics = {'failure_reason': 'OOM + pipeline bug: --model_path and --sft_adapter args in wrong order. RSFT LoRA merged to bare Qwen3-4B without SFT base, causing ontology collapse. Fix: match DocRED eval param ordering.'}
plan_007_redocred_rsft_eval_r2:
  metrics = {'F1': 0.0025, 'Ign-F1': 0.0026, 'Evi-F1': 0.8837, 'EDCR': 0.9978, 'format_ok': '489/493', 'truncated': '117/493', 'predictions': 8461}
  metrics.F1 = 0.0025
  metrics.Ign-F1 = 0.0026
  metrics.Evi-F1 = 0.8837
  metrics.EDCR = 0.9978
plan_007_redocred_rsft_eval_r5:
  metrics = {'f1': 0.4234, 'ign_f1': 0.4145, 'evi_f1': 0.8182, 'edcr': 0.621, 'evi_joint_f1': 0.3306, 'format_compliance': 1, 'field_compliance': 0.8134, 'n_documents': 493, 'n_truncated': 90, 'inference_time_s': 5655.5}
  metrics.f1 = 0.4234
  metrics.ign_f1 = 0.4145
  metrics.evi_f1 = 0.8182
  metrics.edcr = 0.621
  metrics.evi_joint_f1 = 0.3306
plan_011_grpo_g8_bf16_eval:
  metrics = {'rel_f1': 0.4549, 'ign_f1': 0.4549, 'evi_f1': 0.8086, 'edcr': 0.6318, 'format_ok_rate': 1, 'n_truncated': 61, 'n_total': 985, 'n_predictions': 10701, 'checkpoint': 'checkpoint-100', 'model': 'Qwen3-4B + SFT merged + GRPO bf16 LoRA ckpt-100', 'inference_time_s': 3170.3}
  metrics.rel_f1 = 0.4549
  metrics.ign_f1 = 0.4549
  metrics.evi_f1 = 0.8086
  metrics.edcr = 0.6318
plan_014_no_evidence_eval_d076:
  metrics = {'ign_f1': 0.4721, 'f1': 0.4876, 'precision': 0.4901, 'recall': 0.4851, 'format_compliance_rate': 0.9929, 'n_truncated': 307, 'inference_time_seconds': 6903.9}
  metrics.ign_f1 = 0.4721
  metrics.f1 = 0.4876
  metrics.precision = 0.4901
  metrics.recall = 0.4851
random_rsft_k1_eval:
  metrics = {'ign_f1': 0.4114, 'f1': 0.4198, 'evi_f1': 0.7964, 'evi_f1_joint': 0.3216, 'EDCR': 0.6971, 'format_compliance': 0.999, 'field_compliance': 0.7482, 'truncated': 235, 'n_total': 985, 'n_predictions': 16110, 'inference_time_seconds': 11778.5}
  metrics.ign_f1 = 0.4114
  metrics.f1 = 0.4198
  metrics.evi_f1 = 0.7964
  metrics.evi_f1_joint = 0.3216
  metrics.EDCR = 0.6971
reeval_ced_s42:
  metrics = {'ign_f1': 0.4423, 'rel_f1': 0.4517, 'evi_f1': 0.8175, 'evi_f1_joint': 0.3518, 'edcr': 0.6569, 'format_compliance_rate': 1, 'field_compliance_rate': 0.7756, 'n_truncated': 214, 'inference_time_seconds': 10815.5}
  metrics.ign_f1 = 0.4423
  metrics.rel_f1 = 0.4517
  metrics.evi_f1 = 0.8175
  metrics.evi_f1_joint = 0.3518
  metrics.edcr = 0.6569
reeval_ced_s44:
  metrics = {'ign_f1': 0.4511, 'rel_f1': 0.4621, 'evi_f1': 0.805, 'evi_f1_joint': 0.3677, 'edcr': 0.635, 'format_compliance_rate': 1, 'field_compliance_rate': 0.802, 'n_truncated': 190, 'inference_time_seconds': 13077.6}
  metrics.ign_f1 = 0.4511
  metrics.rel_f1 = 0.4621
  metrics.evi_f1 = 0.805
  metrics.evi_f1_joint = 0.3677
  metrics.edcr = 0.635
reeval_flat_nli_s42:
  metrics = {'ign_f1': 0.4448, 'rel_f1': 0.4535, 'evi_f1': 0.8039, 'evi_f1_joint': 0.3558, 'edcr': 0.6458, 'format_compliance_rate': 1, 'field_compliance_rate': 0.7787, 'n_truncated': 205, 'inference_time_seconds': 13253.1}
  metrics.ign_f1 = 0.4448
  metrics.rel_f1 = 0.4535
  metrics.evi_f1 = 0.8039
  metrics.evi_f1_joint = 0.3558
  metrics.edcr = 0.6458
reeval_flat_nli_s43:
  metrics = {'rel_f1': 0.4523, 'ign_f1': 0.4523, 'evi_f1': 0.8158, 'edcr': 0.6505, 'num_preds': 15357, 'format_ok': '984/985', 'truncated': '211/985', 'inference_time_s': 3515.8}
  metrics.rel_f1 = 0.4523
  metrics.ign_f1 = 0.4523
  metrics.evi_f1 = 0.8158
  metrics.edcr = 0.6505
reeval_flat_nli_s43_r2:
  metrics = {'rel_f1': 0.4586, 'rel_precision': 0.4732, 'rel_recall': 0.4449, 'ign_f1': 0.4503, 'evi_f1': 0.8113, 'evi_precision': 0.8035, 'evi_recall': 0.8192, 'evi_f1_joint': 0.358, 'edcr': 0.6552, 'format_ok_rate': 0.999, 'n_truncated': 184, 'n_predictions': 15015}
  metrics.rel_f1 = 0.4586
  metrics.rel_precision = 0.4732
  metrics.rel_recall = 0.4449
  metrics.ign_f1 = 0.4503
  metrics.evi_f1 = 0.8113
  metrics.evi_precision = 0.8035
  metrics.evi_recall = 0.8192
  metrics.evi_f1_joint = 0.358
  metrics.edcr = 0.6552
reeval_rsft_topk3:
  metrics = {'rel_f1': 0.4454, 'rel_precision': 0.4512, 'rel_recall': 0.4398, 'ign_f1': 0.4364, 'evi_f1': 0.8088, 'edcr': 0.6635, 'format_ok_rate': 0.999, 'n_truncated': 214, 'n_predictions': 16020, 'inference_time_seconds': 3546.4, 'ign_f1_corrected': True}
  metrics.rel_f1 = 0.4454
  metrics.rel_precision = 0.4512
  metrics.rel_recall = 0.4398
  metrics.ign_f1 = 0.4364
  metrics.evi_f1 = 0.8088
  metrics.edcr = 0.6635
  metrics.ign_f1_corrected = True
reeval_sft_baseline_d076:
  metrics = {'rel_f1': 0.4049, 'ign_f1': 0.3974, 'evi_f1': 0.7986, 'edcr': 0.6982, 'evi_f1_joint': 0.3147, 'format_compliance_rate': 0.998, 'n_truncated': 288, 'n_documents': 985, 'n_predictions': 16880, 'inference_time_sec': 7056.5}
  metrics.rel_f1 = 0.4049
  metrics.ign_f1 = 0.3974
  metrics.evi_f1 = 0.7986
  metrics.edcr = 0.6982
  metrics.evi_f1_joint = 0.3147
rsft_s43_dev_eval_preds:
  metrics = {'ign_f1': 0.4512, 'f1': 0.4601, 'evi_f1': 0.8063, 'edcr': 0.6542, 'evi_f1_joint': 0.3605, 'format_compliance_rate': 1, 'field_compliance_rate': 0.809, 'n_truncated': 184, 'inference_time_seconds': 10982}
  metrics.ign_f1 = 0.4512
  metrics.f1 = 0.4601
  metrics.evi_f1 = 0.8063
  metrics.edcr = 0.6542
  metrics.evi_f1_joint = 0.3605
wave1_sft_4b_s43_eval_r2:
  metrics = {'ign_f1': 0.4365, 'rel_f1': 0.4429, 'evi_f1_joint': 0.3462, 'evi_f1_tp': 0.8021, 'edcr': 0.6827, 'format_compliance_rate': 1, 'n_truncated': 318, 'n_predictions': 17055, 'inference_time_seconds': 7157.9}
  metrics.ign_f1 = 0.4365
  metrics.rel_f1 = 0.4429
  metrics.evi_f1_joint = 0.3462
  metrics.evi_f1_tp = 0.8021
  metrics.edcr = 0.6827
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f6fb1fb-39ac-4ee2-bfb5-be3a7ea436b8",
  "isSidechain": true,
  "promptId": "23faa4e2-0c97-47f8-be9e-f272ba775828",
  "agentId": "a35180a8a436e895f",
  "type": "user",
  "uuid": "55c4c392-9128-476f-8987-109f9a5ee9a8",
  "sourceToolAssistantUUID": "3f6fb1fb-39ac-4ee2-bfb5-be3a7ea436b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-18T22:07:16.080Z_

Now I have all the data. Let me produce the final comprehensive audit table.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55c4c392-9128-476f-8987-109f9a5ee9a8",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAo5evmyL2XAsC5taVsL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a38ea31a-f3fd-4195-a648-07ac6e968575",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NXETZXChVmAdoj3b7imVg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14818,
      "cache_read_input_tokens": 60687,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14818,
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

_source line 34 · 2026-05-18T22:07:55.063Z_

<details open><summary>🔧 Tool call — Write · `toolu_01FZip3NSMXaq7FGLXy8bJHr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/d076_final_audit.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Final D076 Protocol Compliance Audit - comprehensive summary with metrics.\"\"\"\n\nimport json\nimport re\n\nfpath = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt'\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\nresult_str = raw.get('result', raw)\nif isinstance(result_str, str):\n    data = json.loads(result_str)\nelse:\n    data = result_str\n\nexperiments = data['data']['experiments']\n\ndef parse_command(cmd):\n    result = {\n        'batch_size': None, 'max_new_tokens': None, 'seed': None,\n        'no_quantize': False, 'model_path': None, 'sft_adapter': None,\n    }\n    if not cmd:\n        return result\n    m = re.search(r'--batch_size\\s+(\\S+)', cmd)\n    if m: result['batch_size'] = m.group(1)\n    m = re.search(r'--max_new_tokens\\s+(\\S+)', cmd)\n    if m: result['max_new_tokens'] = m.group(1)\n    m = re.search(r'--seed\\s+(\\S+)', cmd)\n    if m: result['seed'] = m.group(1).rstrip('\"')\n    if '--no-quantize' in cmd or '--no_quantize' in cmd:\n        result['no_quantize'] = True\n    m = re.search(r'--model_path\\s+(\\S+)', cmd)\n    if m: result['model_path'] = m.group(1)\n    m = re.search(r'--sft_adapter\\s+(\\S+)', cmd)\n    if m: result['sft_adapter'] = m.group(1)\n    return result\n\ndef find_ign_f1(exp):\n    \"\"\"Deep search for ign_f1.\"\"\"\n    for loc in [exp.get('reproduce', {}), exp.get('extra', {}), exp.get('spec', {})]:\n        if isinstance(loc, dict):\n            if 'metrics' in loc and isinstance(loc['metrics'], dict):\n                m = loc['metrics']\n                if 'ign_f1' in m:\n                    return m['ign_f1']\n            if 'ign_f1' in loc:\n                return loc['ign_f1']\n    return None\n\ndef model_path_issue(mp):\n    if not mp:\n        return \"MISSING\"\n    adapter_patterns = ['sft_output', 'adapter', 'checkpoint', 'lora', 'grpo', 'rsft_output', 'dpo_output']\n    base_patterns = ['models/Qwen3-4B', 'models/Qwen/Qwen3-4B']\n    if any(p in mp for p in base_patterns):\n        return None  # OK\n    if any(p in mp for p in adapter_patterns):\n        return f\"ADAPTER:{mp}\"\n    return f\"UNKNOWN:{mp}\"\n\n# Collect 4B eval experiments\neval_exps = []\nfor exp_id, exp in experiments.items():\n    is_4b = False\n    cmd = exp.get('spec', {}).get('command', '')\n    hypothesis = exp.get('hypothesis', '')\n    model_name = exp.get('spec', {}).get('model_name', '')\n    for c in [cmd, hypothesis, model_name, exp_id]:\n        if c and ('4b' in c.lower() or '4B' in c or 'Qwen3-4B' in c):\n            is_4b = True\n            break\n    if not is_4b:\n        continue\n    is_eval = 'eval' in exp_id.lower() or ('eval' in cmd.lower() and 'inference' in cmd.lower()) or 'eval' in hypothesis.lower()\n    if not is_eval:\n        continue\n    eval_exps.append((exp_id, exp))\n\neval_exps.sort(key=lambda x: x[0])\n\n# Print final comprehensive table\nprint(f\"D076 COMPLIANCE AUDIT FOR ALL 4B EVAL EXPERIMENTS ({len(eval_exps)} total)\")\nprint(f\"D076 spec: batch_size=4, max_new_tokens=1024, seed=42, --no-quantize, model_path=base, sft_adapter=adapter\")\nprint()\n\n# Count stats\ncompliant = 0\nnon_compliant = 0\nissues_counter = {\n    'model_path_is_adapter': 0,\n    'missing_no_quantize': 0,\n    'wrong_batch_size': 0,\n    'wrong_seed': 0,\n    'missing_sft_adapter': 0,\n    'wrong_max_new_tokens': 0,\n    'missing_model_path': 0,\n}\n\nrows = []\nfor exp_id, exp in eval_exps:\n    cmd = exp.get('spec', {}).get('command', '')\n    status = exp.get('status', '?')\n    parsed = parse_command(cmd)\n    ign_f1 = find_ign_f1(exp)\n\n    reasons = []\n    if parsed['batch_size'] != '4':\n        reasons.append(f\"bs={parsed['batch_size']}\")\n        if parsed['batch_size'] is not None:\n            issues_counter['wrong_batch_size'] += 1\n        else:\n            issues_counter['wrong_batch_size'] += 1\n    if parsed['max_new_tokens'] != '1024':\n        reasons.append(f\"mnt={parsed['max_new_tokens']}\")\n        issues_counter['wrong_max_new_tokens'] += 1\n    if parsed['seed'] != '42':\n        reasons.append(f\"seed={parsed['seed']}\")\n        issues_counter['wrong_seed'] += 1\n    if not parsed['no_quantize']:\n        reasons.append(\"no --no-quantize\")\n        issues_counter['missing_no_quantize'] += 1\n\n    mp_issue = model_path_issue(parsed['model_path'])\n    if mp_issue:\n        if mp_issue == \"MISSING\":\n            reasons.append(\"model_path MISSING\")\n            issues_counter['missing_model_path'] += 1\n        else:\n            reasons.append(\"model_path->adapter\")\n            issues_counter['model_path_is_adapter'] += 1\n\n    if not parsed['sft_adapter']:\n        reasons.append(\"no --sft_adapter\")\n        issues_counter['missing_sft_adapter'] += 1\n\n    is_compliant = len(reasons) == 0\n    if is_compliant:\n        compliant += 1\n    else:\n        non_compliant += 1\n\n    rows.append({\n        'exp_id': exp_id,\n        'status': status,\n        'ign_f1': f\"{ign_f1:.4f}\" if ign_f1 is not None else \"N/A\",\n        'bs': parsed['batch_size'] or '?',\n        'mnt': parsed['max_new_tokens'] or '?',\n        'seed': parsed['seed'] or '?',\n        'nq': 'Y' if parsed['no_quantize'] else 'N',\n        'model_path': parsed['model_path'] or 'MISSING',\n        'sft_adapter': parsed['sft_adapter'] or 'MISSING',\n        'compliant': 'YES' if is_compliant else 'NO',\n        'reasons': '; '.join(reasons),\n        'full_cmd': cmd,\n    })\n\n# Print table\nfmt = \"{:<45} {:>8} {:>8} {:>4} {:>5} {:>5} {:>3} {:>5} {}\"\nprint(fmt.format(\"exp_id\", \"status\", \"ign_f1\", \"bs\", \"mnt\", \"seed\", \"nq\", \"D076\", \"non_compliance\"))\nprint(\"-\" * 130)\n\nfor r in rows:\n    print(fmt.format(\n        r['exp_id'][:45], r['status'][:8], r['ign_f1'],\n        r['bs'][:4], r['mnt'][:5], r['seed'][:5], r['nq'],\n        r['compliant'], r['reasons']\n    ))\n\nprint(f\"\\n{'=' * 100}\")\nprint(f\"COMPLIANCE STATS: {compliant}/{len(eval_exps)} D076-compliant, {non_compliant}/{len(eval_exps)} non-compliant\")\nprint(f\"\\nIssue breakdown:\")\nfor issue, count in sorted(issues_counter.items(), key=lambda x: -x[1]):\n    print(f\"  {issue}: {count}\")\n\nprint(f\"\\n{'=' * 100}\")\nprint(\"D076-COMPLIANT EXPERIMENTS (model_path=base, sft_adapter=adapter, bs=4, mnt=1024, seed=42, --no-quantize):\")\nprint(\"-\" * 100)\nfor r in rows:\n    if r['compliant'] == 'YES':\n        print(f\"  {r['exp_id']:<45} ign_f1={r['ign_f1']:<8} model_path={r['model_path']}\")\n        print(f\"    sft_adapter={r['sft_adapter']}\")\n\nprint(f\"\\n{'=' * 100}\")\nprint(\"SFT s42 (ORIGINAL SEED) EVAL EXPERIMENTS:\")\nprint(\"-\" * 100)\n# Look for SFT baseline evals (not RSFT, not GRPO)\nfor r in rows:\n    eid = r['exp_id'].lower()\n    if ('sft' in eid and 'eval' in eid and 'rsft' not in eid and 'grpo' not in eid\n        and 'dpo' not in eid and 'no_evidence' not in eid and 'nli' not in eid):\n        print(f\"  {r['exp_id']:<45} ign_f1={r['ign_f1']:<8} D076={r['compliant']}\")\n        print(f\"    model_path:  {r['model_path']}\")\n        print(f\"    sft_adapter: {r['sft_adapter']}\")\n        print(f\"    issues:      {r['reasons'] if r['reasons'] else 'NONE'}\")\n        print(f\"    FULL CMD:    {r['full_cmd']}\")\n        print()\n\n# Also look for reeval_sft_baseline_d076 specifically\nprint(f\"\\n{'=' * 100}\")\nprint(\"FULL COMMANDS FOR ALL D076-COMPLIANT EXPERIMENTS:\")\nprint(\"-\" * 100)\nfor r in rows:\n    if r['compliant'] == 'YES':\n        print(f\"\\n  exp_id: {r['exp_id']}\")\n        print(f\"  ign_f1: {r['ign_f1']}\")\n        print(f\"  FULL CMD: {r['full_cmd']}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a38ea31a-f3fd-4195-a648-07ac6e968575",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAo5evmyL2XAsC5taVsL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8c7288b-9dbb-4131-9f8a-fed57f840284",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NXETZXChVmAdoj3b7imVg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14818,
      "cache_read_input_tokens": 60687,
      "output_tokens": 2943,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14818
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2943,
          "cache_read_input_tokens": 60687,
          "cache_creation_input_tokens": 14818,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14818,
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

_source line 35 · 2026-05-18T22:07:55.081Z_

<details><summary>↩ Tool result · `toolu_01FZip3NSMXaq7FGLXy8bJHr`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/d076_final_audit.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8c7288b-9dbb-4131-9f8a-fed57f840284",
  "isSidechain": true,
  "promptId": "23faa4e2-0c97-47f8-be9e-f272ba775828",
  "agentId": "a35180a8a436e895f",
  "type": "user",
  "uuid": "82ec4b78-1e1a-4823-9039-3b9c175fbf20",
  "sourceToolAssistantUUID": "a8c7288b-9dbb-4131-9f8a-fed57f840284",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-18T22:07:58.043Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Vm5QV24XBu9MfiCGx1BaeX`</summary>

```json
{
  "command": "python3 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/d076_final_audit.py 2>&1",
  "description": "Run final D076 audit",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82ec4b78-1e1a-4823-9039-3b9c175fbf20",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAo8o2XX2sgFz4paRedZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf1ae133-4a12-4abe-95fc-7edca8b4cd9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FaGpbVQPnDnkLysUJdrWdm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2998,
      "cache_read_input_tokens": 75505,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2998
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 75505,
          "cache_creation_input_tokens": 2998,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2998,
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

_source line 37 · 2026-05-18T22:07:58.154Z_

<details><summary>↩ Tool result · `toolu_01Vm5QV24XBu9MfiCGx1BaeX`</summary>

```text
D076 COMPLIANCE AUDIT FOR ALL 4B EVAL EXPERIMENTS (76 total)
D076 spec: batch_size=4, max_new_tokens=1024, seed=42, --no-quantize, model_path=base, sft_adapter=adapter

exp_id                                          status   ign_f1   bs   mnt  seed  nq  D076 non_compliance
----------------------------------------------------------------------------------------------------------------------------------
eval_flat_nli_s44                                 DONE      N/A    4  1024    44   Y    NO seed=44; model_path->adapter
eval_flat_nli_seed44                              DONE      N/A    4  1024    44   Y    NO seed=44; model_path->adapter
eval_flat_nli_seed45                              DONE      N/A    4  1024    45   Y    NO seed=45; model_path->adapter
eval_grpo_g8_bf16                                 DONE      N/A    ?  1024     ?   Y    NO bs=None; seed=None; model_path MISSING
eval_plan_001_flat_nli                            DONE      N/A   16  1024    42   Y    NO bs=16; model_path->adapter
eval_plan_001_flat_nli_s43                        DONE      N/A   16  1024    43   Y    NO bs=16; seed=43; model_path->adapter; no --sft_adapter
eval_plan_008_rsft_topk3                          DONE      N/A   16  1024    42   Y    NO bs=16; model_path->adapter; no --sft_adapter
eval_plan_008_topk3_fixed                         DONE      N/A   16  1024    42   Y    NO bs=16; model_path->adapter
eval_plan_012_dpo_1ep_fixed                       DONE      N/A   16  1024    42   Y    NO bs=16; model_path->adapter
eval_plan_012_dpo_1ep_fixed_r2                    DONE      N/A    ?     ?     ?   N    NO bs=None; mnt=None; seed=None; no --no-quantize; model_path MISSING
eval_plan_012_dpo_ced_1ep                         DONE      N/A   16  1024    42   Y    NO bs=16; model_path->adapter; no --sft_adapter
eval_plan_012_dpo_ced_ckpt400                     DONE      N/A   16  1024    42   Y    NO bs=16; model_path->adapter; no --sft_adapter
eval_plan_014_no_evidence                         DONE      N/A    4  1024    42   Y    NO model_path->adapter; no --sft_adapter
eval_plan_014_no_evidence_r2                      DONE      N/A    4  1024    42   Y   YES 
eval_rsft_ced_s43                                 DONE      N/A    4  1024    43   Y    NO seed=43; model_path->adapter
eval_rsft_ced_s45                                 DONE      N/A    4  1024    45   Y    NO seed=45; model_path->adapter
eval_sft_baseline_noquant                         DONE      N/A   16  1024    42   N    NO bs=16; no --no-quantize; model_path->adapter; no --sft_adapter
grpo_bf16_g4_ckpt100_eval                         DONE      N/A    4  1024    42   Y    NO model_path->adapter
grpo_bf16_g4_ckpt200_eval                      RUNNING      N/A    4  1024    42   Y    NO model_path->adapter
lead2_ckpt20_eval                                 DONE      N/A    4  1024    42   Y    NO model_path->adapter; no --sft_adapter
mvp2_eval_ced_kl001_r4_ckpt10                     DONE      N/A    ?     ?     ?   N    NO bs=None; mnt=None; seed=None; no --no-quantize; model_path MISSING
mvp2_eval_ced_kl001_r4_ckpt90                     DONE      N/A    ?     ?     ?   N    NO bs=None; mnt=None; seed=None; no --no-quantize; model_path MISSING; no --sft_adapter
mvp2_eval_ced_kl001_r4_early                      DONE      N/A    ?     ?     ?   N    NO bs=None; mnt=None; seed=None; no --no-quantize; model_path MISSING
mvp2_eval_ced_kl001_r4_high                       DONE      N/A    ?     ?     ?   N    NO bs=None; mnt=None; seed=None; no --no-quantize; model_path MISSING
mvp2_eval_ced_kl001_r4_multi                      DONE      N/A    ?     ?     ?   N    NO bs=None; mnt=None; seed=None; no --no-quantize; model_path MISSING
mvp2_eval_ced_kl001_r4_step100                    DONE      N/A    ?     ?     ?   N    NO bs=None; mnt=None; seed=None; no --no-quantize; model_path MISSING
mvp2_eval_ced_kl001_r4_step90                     DONE      N/A    ?     ?     ?   N    NO bs=None; mnt=None; seed=None; no --no-quantize; model_path MISSING
mvp2_eval_lr5e6_r1_ckpt100                        DONE      N/A   16  1024    42   N    NO bs=16; no --no-quantize; model_path->adapter
mvp2_eval_lr5e6_r1_ckpt20                         DONE      N/A    ?     ?     ?   N    NO bs=None; mnt=None; seed=None; no --no-quantize; model_path MISSING; no --sft_adapter
mvp2_eval_lr5e6_r1_ckpt40                         DONE      N/A    ?     ?     ?   N    NO bs=None; mnt=None; seed=None; no --no-quantize; model_path MISSING; no --sft_adapter
mvp2_eval_lr5e6_r1_ckpt40_r2                      DONE   0.0071    ?     ?     ?   N    NO bs=None; mnt=None; seed=None; no --no-quantize; model_path MISSING; no --sft_adapter
mvp2_eval_lr5e6_r1_ckpt60_r2                      DONE      N/A   16  1024    42   N    NO bs=16; no --no-quantize; model_path->adapter
mvp2_eval_lr5e6_r1_ckpt80                         DONE      N/A   16  1024    42   N    NO bs=16; no --no-quantize; model_path->adapter
mvp2_eval_lr5e6_rp_r2_ckpt20                      DONE      N/A    ?     ?     ?   N    NO bs=None; mnt=None; seed=None; no --no-quantize; model_path MISSING; no --sft_adapter
mvp2_eval_rsft_r1                                 DONE      N/A    ?     ?     ?   Y    NO bs=None; mnt=None; seed=None; model_path MISSING; no --sft_adapter
mvp2_eval_rsft_r2a                                DONE      N/A    ?     ?     ?   Y    NO bs=None; mnt=None; seed=None; model_path MISSING; no --sft_adapter
mvp2_eval_rsft_r2b                                DONE      N/A    ?     ?     ?   Y    NO bs=None; mnt=None; seed=None; model_path MISSING; no --sft_adapter
mvp2_eval_rsft_r2b_maxtok1536                     DONE      N/A    ?  1536     ?   Y    NO bs=None; mnt=1536; seed=None; model_path->adapter; no --sft_adapter
mvp2_eval_rsft_r2b_maxtok1536_r2                  DONE      N/A    ?  1536     ?   Y    NO bs=None; mnt=1536; seed=None; model_path->adapter
mvp2_eval_rsft_s43                                DONE      N/A    ?     ?     ?   Y    NO bs=None; mnt=None; seed=None; model_path MISSING
mvp2_eval_rsft_s43_r2                             DONE      N/A    ?     ?     ?   Y    NO bs=None; mnt=None; seed=None; model_path->adapter
mvp2_eval_sft_baseline                            DONE      N/A   16  1024    42   N    NO bs=16; no --no-quantize; model_path->adapter; no --sft_adapter
mvp2_sft_eval                                     DONE      N/A    ?     ?     ?   N    NO bs=None; mnt=None; seed=None; no --no-quantize; model_path->adapter; no --sft_adapter
mvp2_sft_eval_r2                                  DONE      N/A   16  1024    42   N    NO bs=16; no --no-quantize; model_path->adapter; no --sft_adapter
mvp2_sft_eval_r3                                  DONE      N/A   16  1024    42   N    NO bs=16; no --no-quantize; model_path->adapter; no --sft_adapter
plan_002_test_eval_s44                            DONE      N/A   16  1024    42   Y    NO bs=16; model_path->adapter
plan_002_test_eval_s44_r2                         DONE      N/A    4  1024    42   Y    NO model_path->adapter
plan_002_test_rsft_s43                            DONE      N/A    4  1024    42   Y   YES 
plan_002_test_rsft_s44                            DONE      N/A    4  1024    42   Y    NO model_path->adapter
plan_006_qwen3_8b_no_evidence_eval_v2             DONE   0.5079    4  1024    42   Y    NO model_path->adapter
plan_007_redocred_4b_sft_eval                     DONE      N/A    4  1024    42   Y   YES 
plan_007_redocred_4b_sft_eval_r2                  DONE      N/A    4  1024    42   Y   YES 
plan_007_redocred_rsft_eval                       DONE      N/A    4  1024    42   Y    NO model_path->adapter
plan_007_redocred_rsft_eval_r2                    DONE      N/A    4  1024    42   Y   YES 
plan_007_redocred_rsft_eval_r3                    DONE      N/A    4  1024    42   Y   YES 
plan_007_redocred_rsft_eval_r4                    DONE      N/A    4  1024    42   Y    NO model_path->adapter
plan_007_redocred_rsft_eval_r5                    DONE      N/A    4  1024    42   Y    NO model_path->adapter
plan_009_flatnli_reward_eval                      DONE      N/A    ?     ?     ?   N    NO bs=None; mnt=None; seed=None; no --no-quantize; model_path MISSING; no --sft_adapter
plan_009_flatnli_reward_eval_r2                   DONE      N/A    ?  1024     ?   Y    NO bs=None; seed=None; model_path MISSING
plan_011_grpo_g8_bf16_eval                        DONE      N/A   16  1024    42   Y    NO bs=16; model_path->adapter
plan_014_no_evidence_eval_d076                    DONE      N/A    4  1024    42   Y   YES 
random_rsft_k1_eval                               DONE      N/A    4  1024    42   Y    NO model_path->adapter
reeval_ced_s42                                    DONE      N/A    4  1024    42   Y    NO model_path->adapter
reeval_ced_s44                                    DONE      N/A    4  1024    44   Y    NO seed=44; model_path->adapter
reeval_flat_nli_s42                               DONE      N/A    4  1024    42   Y    NO model_path->adapter
reeval_flat_nli_s43                               DONE      N/A    ?     ?     ?   N    NO bs=None; mnt=None; seed=None; no --no-quantize; model_path MISSING
reeval_flat_nli_s43_r2                            DONE      N/A    4  1024    43   Y    NO seed=43; model_path->adapter
reeval_flat_nli_s44                               DONE      N/A    4  1024    44   Y    NO seed=44; model_path->adapter
reeval_rsft_topk3                                 DONE      N/A   16  1024    42   Y    NO bs=16; model_path->adapter
reeval_sft_baseline_d076                          DONE      N/A    4  1024    42   Y   YES 
rsft_s43_dev_eval_preds                           DONE      N/A    4  1024    42   Y    NO model_path->adapter
rsft_s44_dev_eval_preds                           DONE      N/A    4  1024    42   Y    NO model_path->adapter
wave1_sft_4b_s43_eval                             DONE      N/A    4  1024    42   Y    NO model_path->adapter; no --sft_adapter
wave1_sft_4b_s43_eval_r2                          DONE      N/A    4  1024    42   Y   YES 
wave1_sft_4b_s44_eval                             DONE      N/A    4  1024    42   Y    NO model_path->adapter; no --sft_adapter
wave1_sft_4b_s44_eval_r2                      ANALYZIN      N/A    4  1024    42   Y   YES 

====================================================================================================
COMPLIANCE STATS: 10/76 D076-compliant, 66/76 non-compliant

Issue breakdown:
  model_path_is_adapter: 46
  wrong_batch_size: 41
  wrong_seed: 33
  missing_sft_adapter: 23
  missing_no_quantize: 22
  wrong_max_new_tokens: 22
  missing_model_path: 20

====================================================================================================
D076-COMPLIANT EXPERIMENTS (model_path=base, sft_adapter=adapter, bs=4, mnt=1024, seed=42, --no-quantize):
----------------------------------------------------------------------------------------------------
  eval_plan_014_no_evidence_r2                  ign_f1=N/A      model_path=/root/autodl-tmp/models/Qwen3-4B
    sft_adapter=/root/autodl-tmp/sft_no_evidence_output
  plan_002_test_rsft_s43                        ign_f1=N/A      model_path=/root/autodl-tmp/models/Qwen3-4B
    sft_adapter=/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
  plan_007_redocred_4b_sft_eval                 ign_f1=N/A      model_path=/root/autodl-tmp/models/Qwen/Qwen3-4B
    sft_adapter=/root/autodl-tmp/sft_output_qwen3_4b
  plan_007_redocred_4b_sft_eval_r2              ign_f1=N/A      model_path=/root/autodl-tmp/models/Qwen3-4B
    sft_adapter=/root/autodl-tmp/sft_output
  plan_007_redocred_rsft_eval_r2                ign_f1=N/A      model_path=/root/autodl-tmp/models/Qwen3-4B
    sft_adapter=/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
  plan_007_redocred_rsft_eval_r3                ign_f1=N/A      model_path=/root/autodl-tmp/models/Qwen3-4B
    sft_adapter=/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
  plan_014_no_evidence_eval_d076                ign_f1=N/A      model_path=/root/autodl-tmp/models/Qwen/Qwen3-4B
    sft_adapter=/root/autodl-tmp/sft_no_evidence_output/
  reeval_sft_baseline_d076                      ign_f1=N/A      model_path=/root/autodl-tmp/models/Qwen3-4B
    sft_adapter=/root/autodl-tmp/sft_output
  wave1_sft_4b_s43_eval_r2                      ign_f1=N/A      model_path=/root/autodl-tmp/models/Qwen3-4B
    sft_adapter=/root/autodl-tmp/sft_output_seed43/
  wave1_sft_4b_s44_eval_r2                      ign_f1=N/A      model_path=/root/autodl-tmp/models/Qwen3-4B
    sft_adapter=/root/autodl-tmp/sft_output_seed44/

====================================================================================================
SFT s42 (ORIGINAL SEED) EVAL EXPERIMENTS:
----------------------------------------------------------------------------------------------------
  eval_sft_baseline_noquant                     ign_f1=N/A      D076=NO
    model_path:  /root/autodl-tmp/sft_output
    sft_adapter: MISSING
    issues:      bs=16; no --no-quantize; model_path->adapter; no --sft_adapter
    FULL CMD:    python eval.py --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/sft_baseline_noquant --batch_size 16 --max_new_tokens 1024 --split dev --seed 42

  mvp2_eval_sft_baseline                        ign_f1=N/A      D076=NO
    model_path:  /root/autodl-tmp/sft_output
    sft_adapter: MISSING
    issues:      bs=16; no --no-quantize; model_path->adapter; no --sft_adapter
    FULL CMD:    python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/sft_baseline_eval_results --quantize

  mvp2_sft_eval                                 ign_f1=N/A      D076=NO
    model_path:  sft_output
    sft_adapter: MISSING
    issues:      bs=None; mnt=None; seed=None; no --no-quantize; model_path->adapter; no --sft_adapter
    FULL CMD:    python -m freige.eval.inference --model_path sft_output --base_model Qwen3-4B --split dev

  mvp2_sft_eval_r2                              ign_f1=N/A      D076=NO
    model_path:  /root/autodl-tmp/sft_output
    sft_adapter: MISSING
    issues:      bs=16; no --no-quantize; model_path->adapter; no --sft_adapter
    FULL CMD:    python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_results --seed 42

  mvp2_sft_eval_r3                              ign_f1=N/A      D076=NO
    model_path:  /root/autodl-tmp/sft_output
    sft_adapter: MISSING
    issues:      bs=16; no --no-quantize; model_path->adapter; no --sft_adapter
    FULL CMD:    bash -c "source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_r3_results --seed 42"

  plan_007_redocred_4b_sft_eval                 ign_f1=N/A      D076=YES
    model_path:  /root/autodl-tmp/models/Qwen/Qwen3-4B
    sft_adapter: /root/autodl-tmp/sft_output_qwen3_4b
    issues:      NONE
    FULL CMD:    bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_qwen3_4b --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval"

  plan_007_redocred_4b_sft_eval_r2              ign_f1=N/A      D076=YES
    model_path:  /root/autodl-tmp/models/Qwen3-4B
    sft_adapter: /root/autodl-tmp/sft_output
    issues:      NONE
    FULL CMD:    bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval"

  reeval_sft_baseline_d076                      ign_f1=N/A      D076=YES
    model_path:  /root/autodl-tmp/models/Qwen3-4B
    sft_adapter: /root/autodl-tmp/sft_output
    issues:      NONE
    FULL CMD:    bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_baseline_d076_reeval --no-quantize"

  wave1_sft_4b_s43_eval                         ign_f1=N/A      D076=NO
    model_path:  /root/autodl-tmp/sft_output_seed43/
    sft_adapter: MISSING
    issues:      model_path->adapter; no --sft_adapter
    FULL CMD:    bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_seed43/ --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/sft_4b_s43_eval"

  wave1_sft_4b_s43_eval_r2                      ign_f1=N/A      D076=YES
    model_path:  /root/autodl-tmp/models/Qwen3-4B
    sft_adapter: /root/autodl-tmp/sft_output_seed43/
    issues:      NONE
    FULL CMD:    bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_seed43/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/wave1_sft_4b_s43_eval_r2"

  wave1_sft_4b_s44_eval                         ign_f1=N/A      D076=NO
    model_path:  /root/autodl-tmp/sft_output_seed44/
    sft_adapter: MISSING
    issues:      model_path->adapter; no --sft_adapter
    FULL CMD:    bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_seed44/ --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/sft_4b_s44_eval"

  wave1_sft_4b_s44_eval_r2                      ign_f1=N/A      D076=YES
    model_path:  /root/autodl-tmp/models/Qwen3-4B
    sft_adapter: /root/autodl-tmp/sft_output_seed44/
    issues:      NONE
    FULL CMD:    bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_seed44/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/wave1_sft_4b_s44_eval_r2"


====================================================================================================
FULL COMMANDS FOR ALL D076-COMPLIANT EXPERIMENTS:
----------------------------------------------------------------------------------------------------

  exp_id: eval_plan_014_no_evidence_r2
  ign_f1: N/A
  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_no_evidence_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_no_evidence_noquant --no-quantize --no_evidence"

  exp_id: plan_002_test_rsft_s43
  ign_f1: N/A
  FULL CMD: CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --data_path /root/autodl-tmp/data/docred --split test --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_002_test_rsft_s43

  exp_id: plan_007_redocred_4b_sft_eval
  ign_f1: N/A
  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_qwen3_4b --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval"

  exp_id: plan_007_redocred_4b_sft_eval_r2
  ign_f1: N/A
  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval"

  exp_id: plan_007_redocred_rsft_eval_r2
  ign_f1: N/A
  FULL CMD: CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r2

  exp_id: plan_007_redocred_rsft_eval_r3
  ign_f1: N/A
  FULL CMD: CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/redocred_rsft_eval_r3

  exp_id: plan_014_no_evidence_eval_d076
  ign_f1: N/A
  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_no_evidence_output/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/plan_014_no_evidence_eval_d076"

  exp_id: reeval_sft_baseline_d076
  ign_f1: N/A
  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_baseline_d076_reeval --no-quantize"

  exp_id: wave1_sft_4b_s43_eval_r2
  ign_f1: N/A
  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_seed43/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/wave1_sft_4b_s43_eval_r2"

  exp_id: wave1_sft_4b_s44_eval_r2
  ign_f1: N/A
  FULL CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_seed44/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/wave1_sft_4b_s44_eval_r2"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf1ae133-4a12-4abe-95fc-7edca8b4cd9f",
  "isSidechain": true,
  "promptId": "23faa4e2-0c97-47f8-be9e-f272ba775828",
  "agentId": "a35180a8a436e895f",
  "type": "user",
  "uuid": "eb29d560-a456-4f5e-9ecc-29858bf5127c",
  "sourceToolAssistantUUID": "cf1ae133-4a12-4abe-95fc-7edca8b4cd9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-18T22:08:27.191Z_

Here is the complete D076 compliance audit for all 76 Qwen3-4B eval experiments.

## Summary

**10/76 experiments are D076-compliant. 66/76 are non-compliant.**

### Issue breakdown (most common first):
| Issue | Count |
|---|---|
| model_path points to adapter dir (not base model) | 46 |
| Wrong batch_size (not 4) | 41 |
| Wrong seed (not 42) | 33 |
| Missing --sft_adapter | 23 |
| Missing --no-quantize | 22 |
| Wrong/missing max_new_tokens | 22 |
| Missing model_path entirely | 20 |

### The 10 D076-compliant experiments:
1. **eval_plan_014_no_evidence_r2** - sft_adapter=/root/autodl-tmp/sft_no_evidence_output
2. **plan_002_test_rsft_s43** - sft_adapter=rsft_output_ced_s43/checkpoint-510 (test set)
3. **plan_007_redocred_4b_sft_eval** - Re-DocRED, sft_adapter=sft_output_qwen3_4b
4. **plan_007_redocred_4b_sft_eval_r2** - Re-DocRED, sft_adapter=sft_output
5. **plan_007_redocred_rsft_eval_r2** - Re-DocRED, sft_adapter=rsft_output_ced_s43/checkpoint-510
6. **plan_007_redocred_rsft_eval_r3** - Re-DocRED, sft_adapter=rsft_output_ced_s43/checkpoint-510
7. **plan_014_no_evidence_eval_d076** - sft_adapter=sft_no_evidence_output/
8. **reeval_sft_baseline_d076** - sft_adapter=sft_output (the canonical SFT s42 D076 eval)
9. **wave1_sft_4b_s43_eval_r2** - sft_adapter=sft_output_seed43/
10. **wave1_sft_4b_s44_eval_r2** - sft_adapter=sft_output_seed44/ (ANALYZING status)

### SFT s42 (original seed) analysis:
The canonical D076-compliant SFT s42 eval is **reeval_sft_baseline_d076**:
- model_path: `/root/autodl-tmp/models/Qwen3-4B`
- sft_adapter: `/root/autodl-tmp/sft_output`
- ign_f1: 0.3974 (from metrics)
- Full command: `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_baseline_d076_reeval --no-quantize"`

All earlier SFT s42 evals (mvp2_sft_eval, mvp2_sft_eval_r2, mvp2_sft_eval_r3, mvp2_eval_sft_baseline, eval_sft_baseline_noquant) are **non-compliant**: they used `--model_path /root/autodl-tmp/sft_output` (adapter dir), batch_size=16, `--quantize`, and no `--sft_adapter`.

### Key patterns in non-compliant experiments:
- **model_path->adapter is the dominant issue (46/76)**: Most RSFT/GRPO/DPO evals put the checkpoint/adapter dir into `--model_path` instead of the base model, even when `--base_model` was also specified separately
- **Many mvp2-era and early evals used batch_size=16** and `--quantize` instead of `--no-quantize`
- **GRPO kl001 batch evals** (mvp2_eval_ced_kl001_*) used `freige.eval.batch_eval` with `--quantize`, completely different calling convention
- **Seed-varied evals** (s43, s44, s45) correctly used non-42 seeds by design for multi-seed analysis, so seed!=42 is expected for those

### Metrics found (ign_f1) for notable experiments:
| Experiment | ign_f1 | Notes |
|---|---|---|
| reeval_sft_baseline_d076 | 0.3974 | D076-compliant SFT s42 baseline |
| wave1_sft_4b_s43_eval_r2 | 0.4365 | D076 SFT s43 |
| eval_rsft_ced_s43 | 0.4512 | RSFT CED s43 (non-D076: model_path->adapter) |
| reeval_ced_s42 | 0.4423 | RSFT CED s42 (non-D076: model_path->adapter) |
| eval_flat_nli_s44 | 0.4521 | flat-NLI s44 (non-D076: model_path->adapter) |
| grpo_bf16_g4_ckpt100_eval | 0.4431 | GRPO ckpt100 (non-D076: model_path->adapter) |
| random_rsft_k1_eval | 0.4114 | Random RSFT k1 (non-D076: model_path->adapter) |
| plan_014_no_evidence_eval_d076 | 0.4721 | No-evidence ablation, D076-compliant |

The audit scripts are at:
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/d076_eval_audit.py`
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/d076_final_audit.py`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb29d560-a456-4f5e-9ecc-29858bf5127c",
  "isSidechain": true,
  "agentId": "a35180a8a436e895f",
  "requestId": "req_011CbAo927L1c6xS3R9Qo6ci",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "118198f0-909e-4b8d-ac5d-14c8304bfd7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EsJ2SzboL8Gqfq9LqaBBva",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12957,
      "cache_read_input_tokens": 75505,
      "output_tokens": 1673,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12957
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1673,
          "cache_read_input_tokens": 75505,
          "cache_creation_input_tokens": 12957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12957,
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
