# Research conversation: I need you to analyze the experiment registry for the gen-depth-fingerprint project. The data is at: /home/ubuntu/.claud

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a8fa49f9541eeeeba.jsonl`
- **Structured JSON:** [`363bbdd9c31d101cb7ee.json`](../../sessions/36/363bbdd9c31d101cb7ee.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-17T12:43:07.930Z_

I need you to analyze the experiment registry for the gen-depth-fingerprint project. The data is at:
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/8efbc484-bfff-4e42-950b-e677114371ba/tool-results/mcp-agent-ml-research-read_registry-1779021770007.txt

This is JSON with schema: {result: string} where result is itself a JSON string.

I need you to extract and report the following for EVERY experiment (all ~49):

1. For each experiment, give me:
   - exp_id
   - title/name
   - status (DONE/RUNNING/etc)
   - The spec field (especially: generator models used, temperature settings, decoding strategy, reference models, prompt types, seed sources, chain depths)
   - Key metrics/conclusion (brief)

2. Specifically aggregate across ALL experiments:
   - All unique generator models mentioned (with parameter counts if available)
   - All temperature settings used
   - All decoding strategies used
   - All reference models used
   - All prompt types used
   - All seed text sources used
   - Maximum chain depth tested
   - Whether any instruction-tuned models were used
   - Whether any human text baselines exist

Use jq or python to parse the nested JSON. The file is large so be systematic. Report everything in a structured format. Don't summarize too aggressively - I need the details to assess experiment coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4401d70d-bff1-46e1-857b-65011b5d7861",
  "agentId": "a8fa49f9541eeeeba",
  "type": "user",
  "uuid": "f400977a-006c-4a95-9159-205c295ef951",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T12:43:07.933Z_

```json
{
  "parentUuid": "f400977a-006c-4a95-9159-205c295ef951",
  "isSidechain": true,
  "agentId": "a8fa49f9541eeeeba",
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
  "uuid": "3253d47b-65ba-4540-9724-686397222503",
  "timestamp": "2026-05-17T12:43:07.933Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-17T12:43:12.858Z_



I'll start by reading the file and parsing the nested JSON structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3253d47b-65ba-4540-9724-686397222503",
  "isSidechain": true,
  "agentId": "a8fa49f9541eeeeba",
  "requestId": "req_011Cb8AFupgnpUC1D1hvA8XX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25dfd054-9e06-4914-a167-960cd384465f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkQP4uafQYG9z9pJSB2UvN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16758,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16758,
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

_source line 4 · 2026-05-17T12:43:13.685Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ReemznQSoaRoDCsqtJ36ss`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/8efbc484-bfff-4e42-950b-e677114371ba/tool-results/mcp-agent-ml-research-read_registry-1779021770007.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25dfd054-9e06-4914-a167-960cd384465f",
  "isSidechain": true,
  "agentId": "a8fa49f9541eeeeba",
  "requestId": "req_011Cb8AFupgnpUC1D1hvA8XX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9bb9c58-d510-4aa7-ab29-e76742f8ca1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkQP4uafQYG9z9pJSB2UvN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16758,
      "cache_read_input_tokens": 0,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16758
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 177,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16758,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16758,
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

_source line 5 · 2026-05-17T12:43:13.832Z_

<details><summary>↩ Tool result · `toolu_01ReemznQSoaRoDCsqtJ36ss`</summary>

```text
70466 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/8efbc484-bfff-4e42-950b-e677114371ba/tool-results/mcp-agent-ml-research-read_registry-1779021770007.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9bb9c58-d510-4aa7-ab29-e76742f8ca1a",
  "isSidechain": true,
  "promptId": "4401d70d-bff1-46e1-857b-65011b5d7861",
  "agentId": "a8fa49f9541eeeeba",
  "type": "user",
  "uuid": "e7102f99-3595-4e2e-ba50-1f3968a6382e",
  "sourceToolAssistantUUID": "f9bb9c58-d510-4aa7-ab29-e76742f8ca1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T12:43:21.085Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014u9r5S4SASQKm7dKk1Ajbs`</summary>

```json
{
  "command": "python3 -c \"\nimport json, sys\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/8efbc484-bfff-4e42-950b-e677114371ba/tool-results/mcp-agent-ml-research-read_registry-1779021770007.txt') as f:\n    raw = json.load(f)\n\n# The outer structure is {result: string}, where result is itself JSON\ninner = json.loads(raw['result'])\nprint(type(inner))\nif isinstance(inner, dict):\n    print('Keys:', list(inner.keys())[:20])\nelif isinstance(inner, list):\n    print('List length:', len(inner))\n    print('First item keys:', list(inner[0].keys()) if inner else 'empty')\n\" 2>&1 | head -20",
  "description": "Parse outer JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7102f99-3595-4e2e-ba50-1f3968a6382e",
  "isSidechain": true,
  "agentId": "a8fa49f9541eeeeba",
  "requestId": "req_011Cb8AGM2kABRTSMzpa9Bu1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "825caf82-6498-44d2-8659-4734204671ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSAtxNG3voCTAFk42n19nX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 16758,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1119
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 16758,
          "cache_creation_input_tokens": 1119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1119,
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

_source line 7 · 2026-05-17T12:43:21.182Z_

<details><summary>↩ Tool result · `toolu_014u9r5S4SASQKm7dKk1Ajbs`</summary>

```text
&lt;class 'dict'>
Keys: ['success', 'data', 'error', 'metadata']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "825caf82-6498-44d2-8659-4734204671ba",
  "isSidechain": true,
  "promptId": "4401d70d-bff1-46e1-857b-65011b5d7861",
  "agentId": "a8fa49f9541eeeeba",
  "type": "user",
  "uuid": "0b3fedc3-9e30-4d95-a7e6-f0661c00a8df",
  "sourceToolAssistantUUID": "825caf82-6498-44d2-8659-4734204671ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T12:43:26.943Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FyMDDp1Phfiaw5DgANKg88`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/8efbc484-bfff-4e42-950b-e677114371ba/tool-results/mcp-agent-ml-research-read_registry-1779021770007.txt') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nprint('data type:', type(data))\nif isinstance(data, dict):\n    print('data keys:', list(data.keys())[:20])\n    # check for experiments key\n    for k in data.keys():\n        v = data[k]\n        print(f'  {k}: type={type(v).__name__}, ', end='')\n        if isinstance(v, list):\n            print(f'len={len(v)}')\n        elif isinstance(v, dict):\n            print(f'keys={list(v.keys())[:5]}')\n        elif isinstance(v, str):\n            print(f'len={len(v)}, preview={v[:100]}')\n        else:\n            print(v)\n\" 2>&1",
  "description": "Explore data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b3fedc3-9e30-4d95-a7e6-f0661c00a8df",
  "isSidechain": true,
  "agentId": "a8fa49f9541eeeeba",
  "requestId": "req_011Cb8AGtVbMqoh7JJU6Fdt5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87c7fd83-a6b0-4a9d-9721-01e85fd2f9dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxdoMUsLHJtene4dmVHD3h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 331,
      "cache_read_input_tokens": 17877,
      "output_tokens": 377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 331
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 377,
          "cache_read_input_tokens": 17877,
          "cache_creation_input_tokens": 331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 331,
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

_source line 9 · 2026-05-17T12:43:27.120Z_

<details><summary>↩ Tool result · `toolu_01FyMDDp1Phfiaw5DgANKg88`</summary>

```text
data type: &lt;class 'dict'>
data keys: ['experiments', 'count', 'total', 'baseline']
  experiments: type=dict, keys=['exp_047_multi_domain_t07', 'multi_domain_t07', 'multi-domain-seeds', 'plan-008-seed-stratification', 'plan-002-qwen06b-r2-s1']
  count: type=int, 49
  total: type=int, 49
  baseline: type=NoneType, None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87c7fd83-a6b0-4a9d-9721-01e85fd2f9dd",
  "isSidechain": true,
  "promptId": "4401d70d-bff1-46e1-857b-65011b5d7861",
  "agentId": "a8fa49f9541eeeeba",
  "type": "user",
  "uuid": "48284581-9984-4d7b-842a-a6946b71e0bd",
  "sourceToolAssistantUUID": "87c7fd83-a6b0-4a9d-9721-01e85fd2f9dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T12:43:33.185Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RzrRyXszgKFD63sY3FoLg8`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/8efbc484-bfff-4e42-950b-e677114371ba/tool-results/mcp-agent-ml-research-read_registry-1779021770007.txt') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexperiments = inner['data']['experiments']\n\n# Print all experiment IDs\nprint('ALL EXPERIMENT IDS:')\nfor i, exp_id in enumerate(sorted(experiments.keys()), 1):\n    print(f'  {i}. {exp_id}')\n\nprint(f'\\nTotal: {len(experiments)}')\n\n# Look at the structure of one experiment\nprint('\\n--- SAMPLE EXPERIMENT STRUCTURE ---')\nsample_key = list(experiments.keys())[0]\nsample = experiments[sample_key]\nprint(f'Key: {sample_key}')\nprint(f'Fields: {list(sample.keys())}')\nprint(json.dumps(sample, indent=2)[:3000])\n\" 2>&1",
  "description": "List all experiment IDs and examine structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48284581-9984-4d7b-842a-a6946b71e0bd",
  "isSidechain": true,
  "agentId": "a8fa49f9541eeeeba",
  "requestId": "req_011Cb8AHKt4vDrKLWygvLcJm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "951cacc4-ffbe-4d75-a766-5a8bb082c23a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7HU4BZ32aaMRfM4RYNEJN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 514,
      "cache_read_input_tokens": 18208,
      "output_tokens": 373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 514
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 373,
          "cache_read_input_tokens": 18208,
          "cache_creation_input_tokens": 514,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 514,
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

_source line 11 · 2026-05-17T12:43:33.273Z_

<details><summary>↩ Tool result · `toolu_01RzrRyXszgKFD63sY3FoLg8`</summary>

```text
ALL EXPERIMENT IDS:
  1. exp_047_multi_domain_t07
  2. multi-domain-seeds
  3. multi_domain_t07
  4. mvp-001
  5. mvp-001-gen-s0
  6. mvp-001-gen-s1
  7. mvp-001-gen-s2
  8. mvp-001-gen-s3
  9. plan-001
  10. plan-001-fix
  11. plan-001-restore
  12. plan-002
  13. plan-002-eval
  14. plan-002-olmo2-s0
  15. plan-002-olmo2-s1
  16. plan-002-pythia1b-s0
  17. plan-002-pythia1b-s1
  18. plan-002-qwen06b-r2-s0
  19. plan-002-qwen06b-r2-s1
  20. plan-002-qwen06b-s0
  21. plan-002-qwen06b-s1
  22. plan-002-qwen17b-r2-s0
  23. plan-002-qwen17b-r2-s1
  24. plan-002-qwen17b-retry-s0
  25. plan-002-qwen17b-retry-s1
  26. plan-002-qwen17b-s0
  27. plan-002-qwen17b-s1
  28. plan-002-qwen3-1_7b-s0
  29. plan-002-qwen3-1_7b-s1
  30. plan-003
  31. plan-003-olmo2ref
  32. plan-003-qwen06bref
  33. plan-004
  34. plan-004-prep
  35. plan-004-v2
  36. plan-005
  37. plan-005-cont
  38. plan-005-elab
  39. plan-005-rewrite
  40. plan-008-seed-stratification
  41. plan-010-llm-rephrase
  42. plan-010-robustness
  43. plan-013
  44. plan-014
  45. plan-015
  46. plan-015-v2
  47. review-exp-a-baseline-ensemble
  48. review-exp-b-topic-drift
  49. review-exp-c-overall-ci

Total: 49

--- SAMPLE EXPERIMENT STRUCTURE ---
Key: exp_047_multi_domain_t07
Fields: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'metrics', 'conclusion', 'completed_at']
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-17T05:51:25.881Z",
  "updated_at": "2026-05-17T07:22:04.483Z",
  "hypothesis": "Depth fingerprint generalizes across domains (News, Academic, Code) under standard decoding (t=0.7, top_p=0.9) matching main experiment params, eliminating the temperature confound from t=1.0 results and producing directly comparable domain generalization numbers",
  "parent": "exp_043_multi_domain_seeds",
  "spec": {
    "command": "python run_multi_domain_t07.py (3 generators x 3 domains parallel in tmux multi_domain_t07)",
    "server": "autodl-5090",
    "data_path": "/root/gen-depth-fingerprint/experiments/multi_domain/",
    "data_count": "200 seeds x 3 domains x 3 generators x 4 depths = 7200 samples",
    "model_name": "Pythia-1B, Qwen3-1.7B, Mistral-7B-v0.3 (gen) + Pythia-410M (ref)",
    "seed": "default",
    "gpu": "cuda:0,1,2",
    "checkpoint_source": "N/A (generation + evaluation pipeline, no pretrained checkpoint)",
    "eval_data": "News/Academic/Code seeds 200 per domain, generated chains depth 0-3",
    "checkpoint_path": "/root/gen-depth-fingerprint/experiments/multi_domain/multi_domain_results_t07.json",
    "log_path": "/root/gen-depth-fingerprint/experiments/multi_domain/run_t07.log"
  },
  "metrics": {
    "news_binary_f1": 0.7119,
    "news_binary_ci": [
      0.6898,
      0.7332
    ],
    "news_3class_f1": 0.7149,
    "academic_binary_f1": 0.6279,
    "academic_binary_ci": [
      0.6027,
      0.6515
    ],
    "academic_3class_f1": 0.6564,
    "code_binary_f1": 0.6872,
    "code_binary_ci": [
      0.6641,
      0.71
    ],
    "code_3class_f1": 0.6729,
    "overall_binary_f1": 0.6757,
    "overall_3class_f1": 0.6814,
    "delta_vs_t10_news": -0.034,
    "delta_vs_t10_academic": -0.1107,
    "delta_vs_t10_code": -0.0663
  },
  "conclusion": "success",
  "completed_at": "2026-05-17T07:22:04.483Z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "951cacc4-ffbe-4d75-a766-5a8bb082c23a",
  "isSidechain": true,
  "promptId": "4401d70d-bff1-46e1-857b-65011b5d7861",
  "agentId": "a8fa49f9541eeeeba",
  "type": "user",
  "uuid": "b0b11236-de77-4172-ae50-822afd8c68cf",
  "sourceToolAssistantUUID": "951cacc4-ffbe-4d75-a766-5a8bb082c23a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-17T12:43:37.182Z_

Now let me extract the complete details for all 49 experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0b11236-de77-4172-ae50-822afd8c68cf",
  "isSidechain": true,
  "agentId": "a8fa49f9541eeeeba",
  "requestId": "req_011Cb8AHn8tCMVjrkFhzcTZM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b538fcdc-8502-4529-b4f8-5280c5c680f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JtWVf9quuandMdFRn3oFZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1822,
      "cache_read_input_tokens": 18722,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1822,
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

_source line 13 · 2026-05-17T12:43:43.180Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FXjbFXtMX2P9m2Ni6tmULq`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/8efbc484-bfff-4e42-950b-e677114371ba/tool-results/mcp-agent-ml-research-read_registry-1779021770007.txt') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexperiments = inner['data']['experiments']\n\n# Print every experiment in full detail\nfor i, (exp_id, exp) in enumerate(sorted(experiments.items()), 1):\n    print(f\"{'='*80}\")\n    print(f\"EXPERIMENT {i}: {exp_id}\")\n    print(f\"{'='*80}\")\n    print(f\"  Status:     {exp.get('status', 'N/A')}\")\n    print(f\"  Created:    {exp.get('created_at', 'N/A')}\")\n    print(f\"  Completed:  {exp.get('completed_at', 'N/A')}\")\n    print(f\"  Conclusion: {exp.get('conclusion', 'N/A')}\")\n    print(f\"  Hypothesis: {exp.get('hypothesis', 'N/A')}\")\n    print(f\"  Parent:     {exp.get('parent', 'N/A')}\")\n    \n    spec = exp.get('spec', {})\n    if spec:\n        print(f\"  SPEC:\")\n        for k, v in spec.items():\n            print(f\"    {k}: {v}\")\n    \n    metrics = exp.get('metrics', {})\n    if metrics:\n        print(f\"  METRICS:\")\n        for k, v in metrics.items():\n            val_str = str(v)\n            if len(val_str) > 200:\n                val_str = val_str[:200] + '...'\n            print(f\"    {k}: {val_str}\")\n    print()\nPYEOF\n",
  "description": "Print all 49 experiments in full detail",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b538fcdc-8502-4529-b4f8-5280c5c680f2",
  "isSidechain": true,
  "agentId": "a8fa49f9541eeeeba",
  "requestId": "req_011Cb8AHn8tCMVjrkFhzcTZM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e53e81ea-049f-42b6-9acb-163535496124",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JtWVf9quuandMdFRn3oFZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1822,
      "cache_read_input_tokens": 18722,
      "output_tokens": 621,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1822
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 621,
          "cache_read_input_tokens": 18722,
          "cache_creation_input_tokens": 1822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1822,
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

_source line 14 · 2026-05-17T12:43:43.282Z_

<details><summary>↩ Tool result · `toolu_01FXjbFXtMX2P9m2Ni6tmULq`</summary>

```text
&lt;persisted-output>
Output too large (56.6KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/8efbc484-bfff-4e42-950b-e677114371ba/tool-results/bczf3jlq2.txt

Preview (first 2KB):
================================================================================
EXPERIMENT 1: exp_047_multi_domain_t07
================================================================================
  Status:     DONE
  Created:    2026-05-17T05:51:25.881Z
  Completed:  2026-05-17T07:22:04.483Z
  Conclusion: success
  Hypothesis: Depth fingerprint generalizes across domains (News, Academic, Code) under standard decoding (t=0.7, top_p=0.9) matching main experiment params, eliminating the temperature confound from t=1.0 results and producing directly comparable domain generalization numbers
  Parent:     exp_043_multi_domain_seeds
  SPEC:
    command: python run_multi_domain_t07.py (3 generators x 3 domains parallel in tmux multi_domain_t07)
    server: autodl-5090
    data_path: /root/gen-depth-fingerprint/experiments/multi_domain/
    data_count: 200 seeds x 3 domains x 3 generators x 4 depths = 7200 samples
    model_name: Pythia-1B, Qwen3-1.7B, Mistral-7B-v0.3 (gen) + Pythia-410M (ref)
    seed: default
    gpu: cuda:0,1,2
    checkpoint_source: N/A (generation + evaluation pipeline, no pretrained checkpoint)
    eval_data: News/Academic/Code seeds 200 per domain, generated chains depth 0-3
    checkpoint_path: /root/gen-depth-fingerprint/experiments/multi_domain/multi_domain_results_t07.json
    log_path: /root/gen-depth-fingerprint/experiments/multi_domain/run_t07.log
  METRICS:
    news_binary_f1: 0.7119
    news_binary_ci: [0.6898, 0.7332]
    news_3class_f1: 0.7149
    academic_binary_f1: 0.6279
    academic_binary_ci: [0.6027, 0.6515]
    academic_3class_f1: 0.6564
    code_binary_f1: 0.6872
    code_binary_ci: [0.6641, 0.71]
    code_3class_f1: 0.6729
    overall_binary_f1: 0.6757
    overall_3class_f1: 0.6814
    delta_vs_t10_news: -0.034
    delta_vs_t10_academic: -0.1107
    delta_vs_t10_code: -0.0663

================================================================================
EXPERIMENT 2: multi-domain-seeds
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e53e81ea-049f-42b6-9acb-163535496124",
  "isSidechain": true,
  "promptId": "4401d70d-bff1-46e1-857b-65011b5d7861",
  "agentId": "a8fa49f9541eeeeba",
  "type": "user",
  "uuid": "ed96a173-2831-4a6e-98d8-2cddcf4f0b80",
  "sourceToolAssistantUUID": "e53e81ea-049f-42b6-9acb-163535496124",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T12:43:46.144Z_

<details open><summary>🔧 Tool call — Read · `toolu_012hFcYcTUiBZC2j1KWiMuZH`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/8efbc484-bfff-4e42-950b-e677114371ba/tool-results/bczf3jlq2.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed96a173-2831-4a6e-98d8-2cddcf4f0b80",
  "isSidechain": true,
  "agentId": "a8fa49f9541eeeeba",
  "requestId": "req_011Cb8AJWwMbyo36qPnhzarS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c587b879-a0f3-4f52-827f-cedab5faeb89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H86bTvtDpxEBQadgBPrxDB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1414,
      "cache_read_input_tokens": 20544,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1414
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 20544,
          "cache_creation_input_tokens": 1414,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1414,
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

_source line 16 · 2026-05-17T12:43:46.428Z_

<details><summary>↩ Tool result · `toolu_012hFcYcTUiBZC2j1KWiMuZH`</summary>

```text
1	================================================================================
2	EXPERIMENT 1: exp_047_multi_domain_t07
3	================================================================================
4	  Status:     DONE
5	  Created:    2026-05-17T05:51:25.881Z
6	  Completed:  2026-05-17T07:22:04.483Z
7	  Conclusion: success
8	  Hypothesis: Depth fingerprint generalizes across domains (News, Academic, Code) under standard decoding (t=0.7, top_p=0.9) matching main experiment params, eliminating the temperature confound from t=1.0 results and producing directly comparable domain generalization numbers
9	  Parent:     exp_043_multi_domain_seeds
10	  SPEC:
11	    command: python run_multi_domain_t07.py (3 generators x 3 domains parallel in tmux multi_domain_t07)
12	    server: autodl-5090
13	    data_path: /root/gen-depth-fingerprint/experiments/multi_domain/
14	    data_count: 200 seeds x 3 domains x 3 generators x 4 depths = 7200 samples
15	    model_name: Pythia-1B, Qwen3-1.7B, Mistral-7B-v0.3 (gen) + Pythia-410M (ref)
16	    seed: default
17	    gpu: cuda:0,1,2
18	    checkpoint_source: N/A (generation + evaluation pipeline, no pretrained checkpoint)
19	    eval_data: News/Academic/Code seeds 200 per domain, generated chains depth 0-3
20	    checkpoint_path: /root/gen-depth-fingerprint/experiments/multi_domain/multi_domain_results_t07.json
21	    log_path: /root/gen-depth-fingerprint/experiments/multi_domain/run_t07.log
22	  METRICS:
23	    news_binary_f1: 0.7119
24	    news_binary_ci: [0.6898, 0.7332]
25	    news_3class_f1: 0.7149
26	    academic_binary_f1: 0.6279
27	    academic_binary_ci: [0.6027, 0.6515]
28	    academic_3class_f1: 0.6564
29	    code_binary_f1: 0.6872
30	    code_binary_ci: [0.6641, 0.71]
31	    code_3class_f1: 0.6729
32	    overall_binary_f1: 0.6757
33	    overall_3class_f1: 0.6814
34	    delta_vs_t10_news: -0.034
35	    delta_vs_t10_academic: -0.1107
36	    delta_vs_t10_code: -0.0663
37	
38	================================================================================
39	EXPERIMENT 2: multi-domain-seeds
40	================================================================================
41	  Status:     DONE
42	  Created:    2026-05-17T03:38:54.349Z
43	  Completed:  2026-05-17T05:05:40.584Z
44	  Conclusion: success
45	  Hypothesis: Domain independence: depth fingerprint 的 differential depth response 不依赖 seed domain——在 News/Academic/Code 三个非 Wikipedia 域上，7-feature ensemble 的 binary F1 与 Wikipedia baseline 差异 <10pp，证明 DDR 是生成过程的固有特性而非特定域文本属性的 artifact
46	  Parent:     N/A
47	  SPEC:
48	    command: python multi_domain_generation.py + eval
49	    server: autodl-5090
50	    gpu: cuda:0,1,2,3
51	    data_path: /root/gen-depth-fingerprint/data/seeds_{news,academic,code}.jsonl
52	    data_count: 600
53	    model_name: Pythia-1B + Qwen3-1.7B + Mistral-7B-v0.3
54	    seed: 42
55	  METRICS:
56	    news_binary_f1: 0.7459
57	    news_binary_ci: [0.726, 0.764]
58	    news_multiclass_f1: 0.6516
59	    academic_binary_f1: 0.7386
60	    academic_binary_ci: [0.72, 0.757]
61	    academic_multiclass_f1: 0.6223
62	    code_binary_f1: 0.7535
63	    code_binary_ci: [0.737, 0.77]
64	    code_multiclass_f1: 0.6344
65	    wikipedia_baseline_binary_f1: 0.8148
66	    wikipedia_baseline_multiclass_f1: 0.8632
67	    max_gap_vs_wiki_pp: 7.62
68	    worst_domain: academic
69	    best_domain: code
70	    conclusion_label: domain_independent
71	
72	================================================================================
73	EXPERIMENT 3: multi_domain_t07
74	================================================================================
75	  Status:     PREPARING
76	  Created:    2026-05-17T05:54:55.365Z
77	  Completed:  N/A
78	  Conclusion: N/A
79	  Hypothesis: N/A
80	  Parent:     N/A
81	  SPEC:
82	    command: bash -c "source /root/miniconda3/bin/activate && python /root/gen-depth-fingerprint/experiments/multi_domain/run_experiment_t07.py 2>&1 | tee /root/gen-depth-fingerprint/experiments/multi_domain/run_t07.log"
83	    server: autodl-5090
84	    gpu: ['cuda:0', 'cuda:1', 'cuda:2']
85	    pid: 383695
86	    log_path: ~/runs/gen-depth-fingerprint/multi_domain_t07.log
87	    submitted_at: 2026-05-17T05:54:55.259Z
88	    submitted_via: submit_training_job
89	    backend: tmux
90	    account: root
91	
92	================================================================================
93	EXPERIMENT 4: mvp-001
94	================================================================================
95	  Status:     DONE
96	  Created:    2026-05-14T16:17:16.218Z
97	  Completed:  2026-05-14T18:08:20.940Z
98	  Conclusion: success
99	  Hypothesis: Pythia-410M 参考模型的分布特征（entropy stats, tail-decay, TTR, hapax）能区分 Pythia-2.8B continuation 链的 gen-0/gen-1/gen-2+，3-class macro-F1 ≥ 0.45
100	  Parent:     N/A
101	  SPEC:
102	    command: python generate_chain.py --input data/wiki_seed_1000.jsonl --shard-id {0-3} --num-shards 4 --device cuda:0 (4 shards parallel)
103	    server: autodl-5090
104	    data_path: /root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl
105	    data_count: 1000
106	    model_name: EleutherAI/pythia-2.8b (FP16)
107	    seed: 42
108	    temperature: 0.7
109	    top_p: 0.9
110	    max_new_tokens: 256
111	    reference_model: EleutherAI/pythia-410m
112	    script_path: /root/gen-depth-fingerprint/generate_chain.py
113	    generation_type: continuation
114	    depths: gen-0 to gen-4
115	    checkpoint_path: /root/gen-depth-fingerprint/results/mvp_results.json
116	    log_path: /root/gen-depth-fingerprint/data/features.csv
117	  METRICS:
118	    macro_f1: 0.8408
119	    binary_f1_gen0_vs_gen2plus: 0.8653
120	    cv_macro_f1: 0.806
121	    cv_std: 0.013
122	    gen0_f1: 0.9517
123	    gen1_f1: 0.7759
124	    gen2plus_f1: 0.7947
125	    total_records: 4609
126	    seeds_used: 995
127	    skipped: 173
128	
129	================================================================================
130	EXPERIMENT 5: mvp-001-gen-s0
131	================================================================================
132	  Status:     PREPARING
133	  Created:    2026-05-14T17:23:13.139Z
134	  Completed:  N/A
135	  Conclusion: N/A
136	  Hypothesis: N/A
137	  Parent:     N/A
138	  SPEC:
139	    command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/gen-depth-fingerprint && python generate_chain.py --input data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 4 --device cuda:0"
140	    server: autodl-5090
141	    gpu: ['cuda:0']
142	    pid: 92168
143	    log_path: ~/runs/gen-depth-fingerprint/mvp-001-gen-s0.log
144	    submitted_at: 2026-05-14T17:23:13.138Z
145	    submitted_via: submit_training_job
146	    backend: tmux
147	    account: root
148	
149	================================================================================
150	EXPERIMENT 6: mvp-001-gen-s1
151	================================================================================
152	  Status:     PREPARING
153	  Created:    2026-05-14T17:23:14.464Z
154	  Completed:  N/A
155	  Conclusion: failed
156	  Hypothesis: N/A
157	  Parent:     N/A
158	  SPEC:
159	    command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/gen-depth-fingerprint && python generate_chain.py --input data/wiki_seed_1000.jsonl --shard-id 1 --num-shards 4 --device cuda:0"
160	    server: autodl-5090
161	    gpu: ['cuda:1']
162	    pid: 93039
163	    log_path: ~/runs/gen-depth-fingerprint/mvp-001-gen-s1.log
164	    submitted_at: 2026-05-14T17:25:16.359Z
165	    submitted_via: submit_training_job
166	    backend: tmux
167	    account: root
168	
169	================================================================================
170	EXPERIMENT 7: mvp-001-gen-s2
171	================================================================================
172	  Status:     PREPARING
173	  Created:    2026-05-14T17:23:15.855Z
174	  Completed:  N/A
175	  Conclusion: failed
176	  Hypothesis: N/A
177	  Parent:     N/A
178	  SPEC:
179	    command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/gen-depth-fingerprint && python generate_chain.py --input data/wiki_seed_1000.jsonl --shard-id 2 --num-shards 4 --device cuda:0"
180	    server: autodl-5090
181	    gpu: ['cuda:2']
182	    pid: 93116
183	    log_path: ~/runs/gen-depth-fingerprint/mvp-001-gen-s2.log
184	    submitted_at: 2026-05-14T17:25:17.741Z
185	    submitted_via: submit_training_job
186	    backend: tmux
187	    account: root
188	
189	================================================================================
190	EXPERIMENT 8: mvp-001-gen-s3
191	================================================================================
192	  Status:     PREPARING
193	  Created:    2026-05-14T17:23:17.526Z
194	  Completed:  N/A
195	  Conclusion: failed
196	  Hypothesis: N/A
197	  Parent:     N/A
198	  SPEC:
199	    command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/gen-depth-fingerprint && python generate_chain.py --input data/wiki_seed_1000.jsonl --shard-id 3 --num-shards 4 --device cuda:0"
200	    server: autodl-5090
201	    gpu: ['cuda:3']
202	    pid: 93256
203	    log_path: ~/runs/gen-depth-fingerprint/mvp-001-gen-s3.log
204	    submitted_at: 2026-05-14T17:25:18.991Z
205	    submitted_via: submit_training_job
206	    backend: tmux
207	    account: root
208	
209	================================================================================
210	EXPERIMENT 9: plan-001
211	================================================================================
212	  Status:     DONE
213	  Created:    2026-05-14T18:25:29.824Z
214	  Completed:  2026-05-14T18:54:01.340Z
215	  Conclusion: success
216	  Hypothesis: Feature ablation: 模型级特征（entropy系列+tail_decay）独立于表面特征仍能区分生成深度；H1/H2趋势分析确认特征随depth的变化模式；perplexity随depth显著变化
217	  Parent:     N/A
218	  SPEC:
219	    command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/gen-depth-fingerprint && python ablation_analysis.py --parts A B C --device cuda:0"
220	    server: autodl-5090
221	    gpu: ['cuda:0']
222	    pid: 98324
223	    log_path: /tmp/plan-001-fix.log
224	    submitted_at: 2026-05-14T18:25:56.326Z
225	    submitted_via: submit_training_job
226	    backend: tmux
227	    account: root
228	    checkpoint_path: /root/gen-depth-fingerprint/results/ablation_results.json
229	    wall_clock_seconds: 1685.0
230	    gpu_hours: 0.47
231	  METRICS:
232	    note: initial_run_partial_issues_fixed_in_plan-001-fix
233	    ablation_full_macro_f1: 0.82
234	    ablation_surface_only_f1: 0.76
235	    ablation_reference_only_f1: 0.72
236	
237	================================================================================
238	EXPERIMENT 10: plan-001-fix
239	================================================================================
240	  Status:     DONE
241	  Created:    2026-05-14T18:50:14.620Z
242	  Completed:  2026-05-14T19:34:25.973Z
243	  Conclusion: success
244	  Hypothesis: Feature ablation 修复验证：reference-only features (entropy系列+tail_decay) 独立于 surface features 仍能区分 depth，且两组特征的 bootstrap CI 不重叠，证明 differential response 和 lexical drift 是互补的独立信号源
245	  Parent:     plan-001
246	  SPEC:
247	    command: python ablation_analysis.py --parts A B C --device cuda:0
248	    server: autodl-5090
249	    data_path: data/features.csv + data/generations.jsonl
250	    data_count: 4609
251	    model_name: pythia-410m
252	    seed: 42
253	    pid: 101585
254	    log_path: /tmp/plan-001-fix.log
255	    checkpoint_path: /root/gen-depth-fingerprint/results/ablation_results.json
256	  METRICS:
257	    full_macro_f1: 0.8204
258	    reference_only_f1: 0.7187
259	    surface_only_f1: 0.7628
260	    ref_vs_surf_bootstrap_ci: [0.706,0.733] vs [0.747,0.774]
261	    h2_features: entropy_mean, ttr, hapax_ratio
262	    h1_features: tail_decay, entropy_std, entropy_max, entropy_min
263	    median_ppl_by_depth: 13.50, 4.96, 3.00, 2.07, 1.72
264	
265	================================================================================
266	EXPERIMENT 11: plan-001-restore
267	================================================================================
268	  Status:     PREPARING
269	  Created:    2026-05-14T19:14:00.170Z
270	  Completed:  N/A
271	  Conclusion: N/A
272	  Hypothesis: N/A
273	  Parent:     N/A
274	  SPEC:
275	    command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/gen-depth-fingerprint && python ablation_analysis.py --parts A B C --device cuda:0"
276	    server: autodl-5090
277	    gpu: ['cuda:0']
278	    pid: 105217
279	    log_path: ~/runs/gen-depth-fingerprint/plan-001-restore.log
280	    submitted_at: 2026-05-14T19:14:00.157Z
281	    submitted_via: submit_training_job
282	    backend: tmux
283	    account: root
284	
285	================================================================================
286	EXPERIMENT 12: plan-002
287	================================================================================
288	  Status:     DONE
289	  Created:    2026-05-14T20:08:55.258Z
290	  Completed:  2026-05-14T23:19:36.270Z
291	  Conclusion: success
292	  Hypothesis: 跨模型泛化：Pythia-410M 参考模型下的深度特征能否区分不同架构/规模生成器（Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B）的 continuation 链
293	  Parent:     N/A
294	  SPEC:
295	    command: generate_chain.py --model-name {X} --model-path {path} --shard-id {0,1} --num-shards 2 --device cuda:0
296	    server: autodl-5090
297	    data_path: /root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl
298	    data_count: 1000
299	    model_name: pythia-1b, olmo-2-1b, qwen3-1.7b, qwen3-0.6b (+ pythia-2.8b from MVP)
300	    seed: 42
301	    temperature: 0.7
302	    top_p: 0.9
303	    max_new_tokens: 256
304	    reference_model: EleutherAI/pythia-410m
305	    round1: pythia-1b (cuda:0,1) + olmo-2-1b (cuda:2,3)
306	    round2: qwen3-1.7b (cuda:0,1) + qwen3-0.6b (cuda:2,3)
307	    checkpoint_path: /root/gen-depth-fingerprint/data/
308	    log_path: /root/gen-depth-fingerprint/data/
309	  METRICS:
310	    total_records: 18423
311	    models: 4
312	    pythia_1b: {'records': 4555, 'seeds': 995, 'file': 'data/pythia-1b/generations.jsonl'}
313	    olmo_2_1b: {'records': 4713, 'seeds': 995, 'file': 'data/olmo-2-1b/generations.jsonl'}
314	    qwen3_0_6b: {'records': 4538, 'seeds': 996, 'depth_dist': {'gen0': 996, 'gen1': 986, 'gen2': 938, 'gen3': 840, 'gen4': 778}, 'file': 'data/qwen3-0.6b/generations.jsonl'}
315	    qwen3_1_7b: {'records': 4617, 'seeds': 996, 'depth_dist': {'gen0': 996, 'gen1': 983, 'gen2': 941, 'gen3': 875, 'gen4': 822}, 'file': 'data/qwen3-1.7b/generations.jsonl'}
316	
317	================================================================================
318	EXPERIMENT 13: plan-002-eval
319	================================================================================
320	  Status:     DONE
321	  Created:    2026-05-14T23:33:25.348Z
322	  Completed:  2026-05-14T23:40:47.236Z
323	  Conclusion: success
324	  Hypothesis: 跨生成器泛化评估：Pythia-410M 深度特征在 leave-one-generator-out 设置下能否泛化到未见过的生成器
325	  Parent:     plan-002
326	  SPEC:
327	    command: python cross_generator_eval.py
328	    server: autodl-5090
329	    data_path: /root/gen-depth-fingerprint/data/features_all_models.csv
330	    data_count: 23032
331	    model_name: XGBoost classifier
332	    seed: 42
333	    checkpoint_path: /root/gen-depth-fingerprint/data/cross_generator_results.json
334	    log_path: /root/gen-depth-fingerprint/data/cross_generator_report.md
335	  METRICS:
336	    leave_one_out_avg_macro_f1: 0.8037
337	    best_held_out: {'model': 'pythia-1b', 'macro_f1': 0.8507}
338	    worst_held_out: {'model': 'olmo-2-1b', 'macro_f1': 0.7519}
339	    family_out_delta: 0.0107
340	    ablation_full_f1: 0.8037
341	    ablation_reference_only_f1: 0.7543
342	    ablation_surface_only_f1: 0.7471
343	    mcnemar_p: 0
344	    top_features: ['hapax_ratio_0.289', 'ttr_0.168', 'entropy_mean_0.160']
345	    entropy_std_drop: 0.0049
346	    entropy_std_drift: 0.12
347	    entropy_mean_drift: 1.5
348	
349	================================================================================
350	EXPERIMENT 14: plan-002-olmo2-s0
351	================================================================================
352	  Status:     DONE
353	  Created:    2026-05-14T20:09:45.173Z
354	  Completed:  2026-05-14T21:20:28.747Z
355	  Conclusion: success
356	  Hypothesis: 跨家族泛化数据生成（OLMo-2-1B shard0）：非 Pythia 架构(OLMo)的 continuation 链中 depth signal 是否存在，验证 depth dynamics 跨训练数据和架构的普遍性
357	  Parent:     plan-002
358	  SPEC:
359	    command: python generate_chain.py --model-name olmo-2-1b --shard-id 0 --num-shards 2
360	    server: autodl-5090
361	    gpu: ['cuda:2']
362	    pid: 108242
363	    log_path: ~/runs/gen-depth-fingerprint/plan-002-olmo2-s0.log
364	    submitted_at: 2026-05-14T20:09:45.156Z
365	    submitted_via: submit_training_job
366	    backend: tmux
367	    account: root
368	    data_path: /root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl
369	    data_count: 1000
370	    model_name: allenai/OLMo-2-0425-1B
371	    seed: 42
372	    wall_clock_seconds: 4243.6
373	    gpu_hours: 1.18
374	  METRICS:
375	    records: 2379
376	    seeds: 497
377	    skipped: 47
378	    wall_time_s: 3885.2
379	    depth_dist: {'gen0': 497, 'gen1': 494, 'gen2': 477, 'gen3': 461, 'gen4': 450}
380	    file: generations_shard0.jsonl
381	    file_size_mb: 2.68
382	
383	================================================================================
384	EXPERIMENT 15: plan-002-olmo2-s1
385	================================================================================
386	  Status:     DONE
387	  Created:    2026-05-14T20:09:46.880Z
388	  Completed:  2026-05-14T21:20:29.344Z
389	  Conclusion: success
390	  Hypothesis: 跨家族泛化数据生成（OLMo-2-1B shard1）：OLMo-2-1B continuation 链第二分片，补全 ~995 seeds 覆盖
391	  Parent:     plan-002
392	  SPEC:
393	    command: python generate_chain.py --model-name olmo-2-1b --shard-id 1 --num-shards 2
394	    server: autodl-5090
395	    gpu: ['cuda:3']
396	    pid: 108452
397	    log_path: ~/runs/gen-depth-fingerprint/plan-002-olmo2-s1.log
398	    submitted_at: 2026-05-14T20:09:46.862Z
399	    submitted_via: submit_training_job
400	    backend: tmux
401	    account: root
402	    data_path: /root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl
403	    data_count: 1000
404	    model_name: allenai/OLMo-2-0425-1B
405	    seed: 42
406	    wall_clock_seconds: 4242.5
407	    gpu_hours: 1.18
408	  METRICS:
409	    records: 2334
410	    seeds: 498
411	    skipped: 70
412	    wall_time_s: 4081.2
413	    depth_dist: {'gen0': 498, 'gen1': 494, 'gen2': 470, 'gen3': 444, 'gen4': 428}
414	    file: generations_shard1.jsonl
415	    file_size_mb: 2.57
416	
417	================================================================================
418	EXPERIMENT 16: plan-002-pythia1b-s0
419	================================================================================
420	  Status:     DONE
421	  Created:    2026-05-14T20:09:40.947Z
422	  Completed:  2026-05-14T20:57:23.757Z
423	  Conclusion: success
424	  Hypothesis: 跨模型泛化数据生成（Pythia-1B shard0）：同家族更大模型 Pythia-1B 的 continuation 链是否展现与 Pythia-2.8B 相似的 depth dynamics，验证 depth signal 非特定参数量产物
425	  Parent:     plan-002
426	  SPEC:
427	    command: python generate_chain.py --model-name pythia-1b --shard-id 0 --num-shards 2
428	    server: autodl-5090
429	    gpu: ['cuda:0']
430	    pid: 108021
431	    log_path: ~/runs/gen-depth-fingerprint/plan-002-pythia1b-s0.log
432	    submitted_at: 2026-05-14T20:09:40.932Z
433	    submitted_via: submit_training_job
434	    backend: tmux
435	    account: root
436	    data_path: /root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl
437	    data_count: 1000
438	    model_name: EleutherAI/pythia-1b
439	    seed: 42
440	    checkpoint_path: /root/gen-depth-fingerprint/data/pythia-1b/generations_shard0.jsonl
441	    wall_clock_seconds: 2862.8
442	    gpu_hours: 0.8
443	  METRICS:
444	    records: 2286
445	    seeds: 497
446	    skipped: 91
447	    wall_time_s: 2296.7
448	    depth_dist: {'gen0': 497, 'gen1': 497, 'gen2': 457, 'gen3': 429, 'gen4': 406}
449	    file: data/pythia-1b/generations_shard0.jsonl
450	    file_size_mb: 2.5
451	
452	================================================================================
453	EXPERIMENT 17: plan-002-pythia1b-s1
454	================================================================================
455	  Status:     DONE
456	  Created:    2026-05-14T20:09:42.815Z
457	  Completed:  2026-05-14T20:57:25.200Z
458	  Conclusion: success
459	  Hypothesis: 跨模型泛化数据生成（Pythia-1B shard1）：Pythia-1B continuation 链第二分片，与 shard0 合并后提供完整 ~995 seeds 的 depth 数据
460	  Parent:     plan-002
461	  SPEC:
462	    command: python generate_chain.py --model-name pythia-1b --shard-id 1 --num-shards 2
463	    server: autodl-5090
464	    gpu: ['cuda:1']
465	    pid: 108098
466	    log_path: ~/runs/gen-depth-fingerprint/plan-002-pythia1b-s1.log
467	    submitted_at: 2026-05-14T20:09:42.799Z
468	    submitted_via: submit_training_job
469	    backend: tmux
470	    account: root
471	    data_path: /root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl
472	    data_count: 1000
473	    model_name: EleutherAI/pythia-1b
474	    seed: 42
475	    checkpoint_path: /root/gen-depth-fingerprint/data/pythia-1b/generations_shard1.jsonl
476	    wall_clock_seconds: 2862.4
477	    gpu_hours: 0.8
478	  METRICS:
479	    records: 2269
480	    seeds: 498
481	    skipped: 100
482	    wall_time_s: 2247.6
483	    depth_dist: {'gen0': 498, 'gen1': 496, 'gen2': 455, 'gen3': 422, 'gen4': 398}
484	    file: data/pythia-1b/generations_shard1.jsonl
485	    file_size_mb: 2.44
486	
487	================================================================================
488	EXPERIMENT 18: plan-002-qwen06b-r2-s0
489	================================================================================
490	  Status:     DONE
491	  Created:    2026-05-14T22:35:10.950Z
492	  Completed:  2026-05-14T23:00:55.097Z
493	  Conclusion: success
494	  Hypothesis: 跨家族泛化数据生成（Qwen3-0.6B shard0）：最小参数量(0.6B) Qwen 模型的 continuation 链，验证 depth signal 在极小模型中是否仍存在（小模型可能因容量不足而无法维持深层生成的分布稳定性）
495	  Parent:     plan-002
496	  SPEC:
497	    command: python generate_chain.py --model-name qwen3-0.6b --model-path /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base --input data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 2 --device cuda:0
498	    server: autodl-5090
499	    data_path: /root/gen-depth-fingerprint/data/qwen3-0.6b/generations_shard0.jsonl
500	    data_count: 2500
501	    model_name: Qwen3-0.6B
502	    seed: 0-499
503	    pid: 117855
504	    gpu: ['cuda:2']
505	  METRICS:
506	    records: 2270
507	    seeds: 498
508	    depth_dist: {'0': 498, '1': 493, '2': 468, '3': 423, '4': 388}
509	    file: generations_shard0.jsonl
510	
511	================================================================================
512	EXPERIMENT 19: plan-002-qwen06b-r2-s1
513	================================================================================
514	  Status:     DONE
515	  Created:    2026-05-14T22:35:11.142Z
516	  Completed:  2026-05-14T23:01:44.209Z
517	  Conclusion: success
518	  Hypothesis: 跨家族泛化数据生成（Qwen3-0.6B shard1）：Qwen3-0.6B continuation 链第二分片，补全 ~995 seeds 覆盖
519	  Parent:     plan-002
520	  SPEC:
521	    command: python generate_chain.py --model-name qwen3-0.6b --model-path /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base --input data/wiki_seed_1000.jsonl --shard-id 1 --num-shards 2 --device cuda:0
522	    server: autodl-5090
523	    data_path: /root/gen-depth-fingerprint/data/qwen3-0.6b/generations_shard1.jsonl
524	    data_count: 2500
525	    model_name: Qwen3-0.6B
526	    seed: 500-999
527	    pid: 118126
528	    gpu: ['cuda:3']
529	  METRICS:
530	    records: 2268
531	    seeds: 498
532	    depth_dist: {'0': 498, '1': 493, '2': 470, '3': 417, '4': 390}
533	    file: generations_shard1.jsonl
534	
535	================================================================================
536	EXPERIMENT 20: plan-002-qwen06b-s0
537	================================================================================
538	  Status:     DONE
539	  Created:    2026-05-14T21:25:21.697Z
540	  Completed:  2026-05-14T22:04:42.688Z
541	  Conclusion: failed
542	  Hypothesis: N/A
543	  Parent:     N/A
544	  SPEC:
545	    data_path: /root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl
546	    data_count: 1000
547	    model_name: Qwen/Qwen3-0.6B-Base
548	    seed: 42
549	    command: python generate_chain.py --model-name qwen3-0.6b --shard-id 0 --num-shards 2 --device cuda:0
550	    server: autodl-5090
551	    gpu: ['cuda:2']
552	
553	================================================================================
554	EXPERIMENT 21: plan-002-qwen06b-s1
555	================================================================================
556	  Status:     DONE
557	  Created:    2026-05-14T21:25:23.092Z
558	  Completed:  2026-05-14T22:05:00.872Z
559	  Conclusion: failed
560	  Hypothesis: N/A
561	  Parent:     N/A
562	  SPEC:
563	    data_path: /root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl
564	    data_count: 1000
565	    model_name: Qwen/Qwen3-0.6B-Base
566	    seed: 42
567	    command: python generate_chain.py --model-name qwen3-0.6b --shard-id 1 --num-shards 2 --device cuda:0
568	    server: autodl-5090
569	    gpu: ['cuda:3']
570	
571	================================================================================
572	EXPERIMENT 22: plan-002-qwen17b-r2-s0
573	================================================================================
574	  Status:     DONE
575	  Created:    2026-05-14T21:58:12.310Z
576	  Completed:  2026-05-15T00:05:49.186Z
577	  Conclusion: success
578	  Hypothesis: 跨家族泛化数据生成（Qwen3-1.7B shard0）：Qwen 家族 1.7B 模型的 continuation 链 depth dynamics，验证中等规模非 Pythia 模型也产生可检测的 depth signal
579	  Parent:     plan-002
580	  SPEC:
581	    command: python generate_chain.py --model-name qwen3-1.7b --model-path /root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base --input data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 2 --device cuda:0
582	    server: autodl-5090
583	    gpu: ['cuda:0']
584	    pid: 120617
585	    log_path: ~/runs/gen-depth-fingerprint/plan-002-qwen17b-r2-s0.log
586	    submitted_at: 2026-05-14T21:58:12.274Z
587	    submitted_via: submit_training_job
588	    backend: tmux
589	    account: root
590	    data_path: /root/gen-depth-fingerprint/data/qwen3-1.7b/generations_shard0.jsonl
591	    data_count: 2500
592	    model_name: Qwen3-1.7B
593	    seed: 0-499
594	    wall_clock_seconds: 7656.9
595	    gpu_hours: 2.13
596	  METRICS:
597	    records: 2291
598	    seeds: 498
599	    depth_dist: {'0': 498, '1': 492, '2': 468, '3': 435, '4': 398}
600	    skipped: 199
601	    duration_s: 4548.2
602	    file_size_mb: 2.5
603	    file: generations_shard0.jsonl
604	
605	================================================================================
606	EXPERIMENT 23: plan-002-qwen17b-r2-s1
607	================================================================================
608	  Status:     DONE
609	  Created:    2026-05-14T21:58:14.195Z
610	  Completed:  2026-05-14T23:12:09.724Z
611	  Conclusion: success
612	  Hypothesis: 跨家族泛化数据生成（Qwen3-1.7B shard1）：Qwen3-1.7B continuation 链第二分片，补全 ~995 seeds 覆盖
613	  Parent:     plan-002
614	  SPEC:
615	    command: python generate_chain.py --model-name qwen3-1.7b --model-path /root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base --input data/wiki_seed_1000.jsonl --shard-id 1 --num-shards 2 --device cuda:0
616	    server: autodl-5090
617	    gpu: ['cuda:1']
618	    pid: 120694
619	    log_path: ~/runs/gen-depth-fingerprint/plan-002-qwen17b-r2-s1.log
620	    submitted_at: 2026-05-14T21:58:14.157Z
621	    submitted_via: submit_training_job
622	    backend: tmux
623	    account: root
624	    data_path: /root/gen-depth-fingerprint/data/qwen3-1.7b/generations_shard1.jsonl
625	    data_count: 2500
626	    model_name: Qwen3-1.7B
627	    seed: 500-999
628	    wall_clock_seconds: 4435.6
629	    gpu_hours: 1.23
630	  METRICS:
631	    records: 2326
632	    seeds: 498
633	    depth_dist: {'0': 498, '1': 491, '2': 473, '3': 440, '4': 424}
634	    skipped: 53
635	    duration_s: 4228
636	    file: generations_shard1.jsonl
637	
638	================================================================================
639	EXPERIMENT 24: plan-002-qwen17b-retry-s0
640	================================================================================
641	  Status:     DONE
642	  Created:    2026-05-14T21:25:18.048Z
643	  Completed:  2026-05-14T21:59:28.716Z
644	  Conclusion: failed
645	  Hypothesis: N/A
646	  Parent:     N/A
647	  SPEC:
648	    data_path: /root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl
649	    data_count: 1000
650	    model_name: Qwen/Qwen3-1.7B-Base
651	    seed: 42
652	    command: python generate_chain.py --model-name qwen3-1.7b --shard-id 0 --num-shards 2 --device cuda:0
653	    server: autodl-5090
654	    gpu: ['cuda:0']
655	
656	================================================================================
657	EXPERIMENT 25: plan-002-qwen17b-retry-s1
658	================================================================================
659	  Status:     DONE
660	  Created:    2026-05-14T21:25:19.756Z
661	  Completed:  2026-05-14T21:59:33.017Z
662	  Conclusion: failed
663	  Hypothesis: N/A
664	  Parent:     N/A
665	  SPEC:
666	    data_path: /root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl
667	    data_count: 1000
668	    model_name: Qwen/Qwen3-1.7B-Base
669	    seed: 42
670	    command: python generate_chain.py --model-name qwen3-1.7b --shard-id 1 --num-shards 2 --device cuda:0
671	    server: autodl-5090
672	    gpu: ['cuda:1']
673	
674	================================================================================
675	EXPERIMENT 26: plan-002-qwen17b-s0
676	================================================================================
677	  Status:     DONE
678	  Created:    2026-05-14T20:53:19.356Z
679	  Completed:  2026-05-14T20:58:51.386Z
680	  Conclusion: failed
681	  Hypothesis: N/A
682	  Parent:     N/A
683	  SPEC:
684	    command: python generate_chain.py --model-name qwen3-1.7b --shard-id 0 --num-shards 2
685	    server: autodl-5090
686	    gpu: ['cuda:0']
687	    pid: 112179
688	    log_path: ~/runs/gen-depth-fingerprint/plan-002-qwen17b-s0.log
689	    submitted_at: 2026-05-14T20:53:19.334Z
690	    submitted_via: submit_training_job
691	    backend: tmux
692	    account: root
693	    data_path: /root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl
694	    data_count: 1000
695	    model_name: Qwen/Qwen3-1.7B-Base
696	    seed: 42
697	    wall_clock_seconds: 332.1
698	    gpu_hours: 0.09
699	    checkpoint_path: N/A - killed duplicate
700	
701	================================================================================
702	EXPERIMENT 27: plan-002-qwen17b-s1
703	================================================================================
704	  Status:     DONE
705	  Created:    2026-05-14T20:53:21.708Z
706	  Completed:  2026-05-14T20:58:53.722Z
707	  Conclusion: failed
708	  Hypothesis: N/A
709	  Parent:     N/A
710	  SPEC:
711	    command: python generate_chain.py --model-name qwen3-1.7b --shard-id 1 --num-shards 2
712	    server: autodl-5090
713	    gpu: ['cuda:1']
714	    pid: 112264
715	    log_path: ~/runs/gen-depth-fingerprint/plan-002-qwen17b-s1.log
716	    submitted_at: 2026-05-14T20:53:21.683Z
717	    submitted_via: submit_training_job
718	    backend: tmux
719	    account: root
720	    data_path: /root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl
721	    data_count: 1000
722	    model_name: Qwen/Qwen3-1.7B-Base
723	    seed: 42
724	    wall_clock_seconds: 332.0
725	    gpu_hours: 0.09
726	    checkpoint_path: N/A - killed duplicate
727	
728	================================================================================
729	EXPERIMENT 28: plan-002-qwen3-1_7b-s0
730	================================================================================
731	  Status:     DONE
732	  Created:    2026-05-14T20:52:58.460Z
733	  Completed:  2026-05-14T21:14:14.533Z
734	  Conclusion: failed
735	  Hypothesis: N/A
736	  Parent:     N/A
737	  SPEC:
738	    command: python generate_chain.py --model-name qwen3-1.7b --shard-id 0 --num-shards 2
739	    server: autodl-5090
740	    gpu: ['cuda:0']
741	    pid: 111533
742	    log_path: ~/runs/gen-depth-fingerprint/plan-002-qwen3-1_7b-s0.log
743	    submitted_at: 2026-05-14T20:52:58.411Z
744	    submitted_via: submit_training_job
745	    backend: tmux
746	    account: root
747	    data_path: /root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl
748	    data_count: 1000
749	    model_name: Qwen/Qwen3-1.7B-Base
750	    seed: 42
751	    wall_clock_seconds: 1276.1
752	    gpu_hours: 0.35
753	    checkpoint_path: N/A - killed
754	
755	================================================================================
756	EXPERIMENT 29: plan-002-qwen3-1_7b-s1
757	================================================================================
758	  Status:     DONE
759	  Created:    2026-05-14T20:53:00.298Z
760	  Completed:  2026-05-14T21:14:17.437Z
761	  Conclusion: killed
762	  Hypothesis: N/A
763	  Parent:     N/A
764	  SPEC:
765	    command: python generate_chain.py --model-name qwen3-1.7b --shard-id 1 --num-shards 2
766	    server: autodl-5090
767	    gpu: ['cuda:1']
768	    pid: 111646
769	    log_path: ~/runs/gen-depth-fingerprint/plan-002-qwen3-1_7b-s1.log
770	    submitted_at: 2026-05-14T20:53:00.276Z
771	    submitted_via: submit_training_job
772	    backend: tmux
773	    account: root
774	    data_path: /root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl
775	    data_count: 1000
776	    model_name: Qwen/Qwen3-1.7B-Base
777	    seed: 42
778	    wall_clock_seconds: 1277.2
779	    gpu_hours: 0.35
780	
781	================================================================================
782	EXPERIMENT 30: plan-003
783	================================================================================
784	  Status:     DONE
785	  Created:    2026-05-14T23:58:40.949Z
786	  Completed:  2026-05-15T00:09:28.999Z
787	  Conclusion: success
788	  Hypothesis: 跨家族参考模型伪证化：用 OLMo-2-1B 和 Qwen3-0.6B 作参考模型提取特征，验证 differential depth response 非 Pythia 特异
789	  Parent:     N/A
790	  SPEC:
791	    command: python extract_features_crossref.py + cross_ref_analysis.py
792	    server: autodl-5090
793	    data_path: /root/gen-depth-fingerprint/data/features_all_models.csv
794	    data_count: 23032
795	    model_name: OLMo-2-1B + Qwen3-0.6B as reference
796	    seed: 42
797	    checkpoint_path: /root/gen-depth-fingerprint/data/cross_ref_results.json
798	    log_path: /root/gen-depth-fingerprint/data/
799	  METRICS:
800	    logo_f1_pythia_ref: 0.8034
801	    logo_f1_olmo_ref: 0.8072
802	    logo_f1_qwen_ref: 0.8158
803	    entropy_drift_all_refs_negative: True
804	    olmo_ref_drift_range: [-0.608, -0.9089]
805	    qwen_ref_drift_range: [-0.9557, -1.3458]
806	    pythia_ref_drift_range: [-1.1872, -1.4017]
807	    dual_dynamics_is_pythia_artifact: False
808	
809	================================================================================
810	EXPERIMENT 31: plan-003-olmo2ref
811	================================================================================
812	  Status:     DONE
813	  Created:    2026-05-15T00:09:31.145Z
814	  Completed:  2026-05-15T00:10:00.971Z
815	  Conclusion: success
816	  Hypothesis: 跨家族参考模型验证（OLMo-2-1B）：用 OLMo-2-1B 作为参考模型提取 differential entropy 特征，验证 depth signal 的参考模型无关性——不同训练数据和架构的模型仍能检测相同的 depth dynamics
817	  Parent:     plan-003
818	  SPEC:
819	    command: python extract_features_crossref.py --reference-model /root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B --output data/features_ref_olmo.csv --device cuda:0
820	    server: autodl-5090
821	    data_path: /root/gen-depth-fingerprint/data/
822	    data_count: 23032
823	    model_name: OLMo-2-1B (reference)
824	    seed: 42
825	
826	================================================================================
827	EXPERIMENT 32: plan-003-qwen06bref
828	================================================================================
829	  Status:     DONE
830	  Created:    2026-05-15T00:09:31.649Z
831	  Completed:  2026-05-15T00:10:01.383Z
832	  Conclusion: success
833	  Hypothesis: 跨家族参考模型验证（Qwen3-0.6B）：用非 Pythia 家族的 Qwen3-0.6B 作为参考模型提取 differential entropy 特征，验证 depth signal 不依赖于参考模型与生成器的家族匹配
834	  Parent:     plan-003
835	  SPEC:
836	    command: python extract_features_crossref.py --reference-model /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base --output data/features_ref_qwen.csv --device cuda:0
837	    server: autodl-5090
838	    data_path: /root/gen-depth-fingerprint/data/
839	    data_count: 23032
840	    model_name: Qwen3-0.6B (reference)
841	    seed: 42
842	
843	================================================================================
844	EXPERIMENT 33: plan-004
845	================================================================================
846	  Status:     DONE
847	  Created:    2026-05-15T00:22:57.901Z
848	  Completed:  2026-05-15T00:44:49.276Z
849	  Conclusion: failed
850	  Hypothesis: Downstream utility: depth-stratified 数据对 OLMo-2-0425-1B CLM fine-tuning 的影响——depth0_only vs depth01 vs all vs size_matched vs binary_filtered，5 variants × 3 seeds
851	  Parent:     N/A
852	  SPEC:
853	    command: run_gpu{1,2,3}.sh (3 GPU parallel)
854	    server: autodl-5090
855	    gpu: cuda:1,cuda:2,cuda:3
856	    pid: GPU1:144272, GPU2:145189(waiting for 142680), GPU3:145799
857	    data_path: /root/gen-depth-fingerprint/data/downstream/
858	    data_count: depth0_only:797, depth01:3951, all:12299, size_matched:3951, binary_filtered:3951
859	    model_name: OLMo-2-0425-1B
860	    seed: 42,123,456
861	    log_path: /tmp/plan004_gpu1.log, /tmp/plan004_gpu2.log, /tmp/plan004_gpu3.log
862	    checkpoint_path: /root/autodl-tmp/gen-depth-fingerprint/experiments/downstream/
863	
864	================================================================================
865	EXPERIMENT 34: plan-004-prep
866	================================================================================
867	  Status:     PREPARING
868	  Created:    2026-05-14T23:58:42.465Z
869	  Completed:  N/A
870	  Conclusion: success
871	  Hypothesis: Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）
872	  Parent:     N/A
873	  METRICS:
874	    model: OLMo-2-0425-1B (1485M)
875	    datasets: {'depth0_only': {'train': 797, 'test': 3138}, 'depth01': {'train': 3951, 'test': 3138}, 'all': {'train': 12299, 'test': 3138}, 'size_matched': {'train': 3951, 'test': 3138}, 'binary_filtered': {'train...
876	    dry_run_loss: 2.18
877	    script: finetune_downstream.py
878	
879	================================================================================
880	EXPERIMENT 35: plan-004-v2
881	================================================================================
882	  Status:     DONE
883	  Created:    2026-05-15T00:45:17.861Z
884	  Completed:  2026-05-15T03:09:20.593Z
885	  Conclusion: negative
886	  Hypothesis: Downstream utility (retry): depth-stratified 数据对 OLMo-2-0425-1B CLM fine-tuning 的影响——5 variants × 3 seeds，输出到数据盘
887	  Parent:     plan-004
888	  SPEC:
889	    command: run_downstream.sh (3 GPUs parallel, save_strategy=no)
890	    server: autodl-5090
891	    gpu: cuda:1,cuda:2,cuda:3
892	    pid: 143757(cuda:1),145189(cuda:2),145799(cuda:3)
893	    data_path: /root/autodl-tmp/gen-depth-fingerprint/experiments/downstream/
894	    data_count: depth0_only:797, depth01:3951, all:12299, size_matched:3951, binary_filtered:3951
895	    model_name: OLMo-2-0425-1B
896	    seed: 42,123,456
897	    log_path: /tmp/plan004_gpu1.log, /tmp/plan004_gpu2.log, /tmp/plan004_gpu3.log
898	    checkpoint_path: none (save_strategy=no)
899	    notes: size_matched_seed42 done (eval_loss=0.8618, ppl=2.367). GPU2 98% VRAM - close to limit.
900	  METRICS:
901	    total_runs: 15
902	    completed: 15
903	    variants: {'all': {'eval_loss_mean': 0.848, 'perplexity_mean': 2.335, 'seeds': {'42': {'eval_loss': 0.848, 'ppl': 2.335}, '123': {'eval_loss': 0.848, 'ppl': 2.335}, '456': {'eval_loss': 0.8482, 'ppl': 2.3354}}}...
904	    ranking_by_ppl: all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)
905	    seed_variance: 极小（同 variant 跨 seed ppl 差 <0.002）
906	
907	================================================================================
908	EXPERIMENT 36: plan-005
909	================================================================================
910	  Status:     DONE
911	  Created:    2026-05-15T03:24:02.435Z
912	  Completed:  2026-05-15T05:30:39.849Z
913	  Conclusion: success
914	  Hypothesis: Prompt type comparison: continuation vs elaboration vs inspired_rewriting 链的 depth signal 强度差异。Pythia-2.8B, 1000 seeds, 3 prompt types × 5 depths = 15K texts
915	  Parent:     N/A
916	  SPEC:
917	    command: python scripts/analyze_prompt_types.py
918	    server: autodl-5090
919	    gpu: cuda:1,cuda:2,cuda:3
920	    data_path: data/pythia-2.8b-*/features.jsonl
921	    data_count: 14393
922	    model_name: pythia-2.8b
923	    seed: 42
924	    log_path: tmux: plan-005-cont, plan-005-elab, plan-005-rewrite
925	  METRICS:
926	    cv_f1: {'continuation': 0.7806, 'inspired_rewriting': 0.7368, 'elaboration': 0.73}
927	    lopto_f1: {'held_out_cont': 0.762, 'held_out_elab': 0.7622, 'held_out_rewrite': 0.7334, 'avg': 0.7525}
928	    depth_retention_d4_d0: {'continuation': 0.831, 'inspired_rewriting': 0.939, 'elaboration': 0.986}
929	    drift_hapax_ratio: {'continuation': -0.74, 'elaboration': -0.828, 'rewriting': -0.8}
930	    drift_ttr: {'continuation': -0.607, 'elaboration': -0.641, 'rewriting': -0.618}
931	    drift_entropy_mean: {'continuation': -0.557, 'elaboration': -0.471, 'rewriting': -0.477}
932	    spearman_ttr: {'continuation': -0.629, 'elaboration': -0.666, 'rewriting': -0.659}
933	    spearman_hapax: {'continuation': -0.651, 'elaboration': -0.674, 'rewriting': -0.67}
934	    spearman_entropy_mean: {'continuation': -0.665, 'elaboration': -0.583, 'rewriting': -0.564}
935	
936	================================================================================
937	EXPERIMENT 37: plan-005-cont
938	================================================================================
939	  Status:     DONE
940	  Created:    2026-05-15T03:28:43.383Z
941	  Completed:  2026-05-15T05:42:53.944Z
942	  Conclusion: success
943	  Hypothesis: Continuation 链数据生成：Pythia-2.8B 在 continuation prompt 下生成 depth 0-4 链，验证递归续写中 entropy/lexical 特征的单调漂移模式是否在 1000 seeds 规模下稳定复现
944	  Parent:     plan-005
945	  SPEC:
946	    command: python generate_chain_prompt.py --model-name pythia-2.8b --prompt-type continuation
947	    server: autodl-5090
948	    gpu: cuda:1
949	    pid: 164658
950	    log_path: /root/runs/gen-depth-fingerprint/plan-005-cont.log
951	    submitted_at: 2026-05-15T03:28:43.303Z
952	    submitted_via: submit_training_job
953	    backend: tmux
954	    account: root
955	    data_path: /root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl
956	    data_count: 995
957	    model_name: pythia-2.8b
958	    seed: 0
959	    prompt_type: continuation
960	    checkpoint_path: /root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl
961	    wall_clock_seconds: 8050.6
962	    gpu_hours: 2.24
963	  METRICS:
964	    total_records: 4620
965	    unique_seeds: 995
966	    skipped: 168
967	    depth_distribution: {'0': 995, '1': 992, '2': 932, '3': 874, '4': 827}
968	    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl
969	    file_size_mb: 4.93
970	    runtime_seconds: 7760
971	    speed_seeds_per_sec: 0.13
972	
973	================================================================================
974	EXPERIMENT 38: plan-005-elab
975	================================================================================
976	  Status:     DONE
977	  Created:    2026-05-15T03:28:45.680Z
978	  Completed:  2026-05-15T08:49:52.315Z
979	  Conclusion: success
980	  Hypothesis: Elaboration 链数据生成：elaboration prompt 要求模型展开而非续写，预期 depth signal 因语义锚定更强而衰减更慢（retention > continuation 的 83%）
981	  Parent:     plan-005
982	  SPEC:
983	    command: python generate_chain_prompt.py --model-name pythia-2.8b --prompt-type elaboration --input data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 1 --device cuda:0
984	    server: autodl-5090
985	    gpu: cuda:2
986	    pid: 164737
987	    log_path: /root/gen-depth-fingerprint/logs/plan-005-elab
988	    submitted_at: 2026-05-15T03:28:45.601Z
989	    submitted_via: submit_training_job
990	    backend: tmux
991	    account: root
992	    data_path: data/wiki_seed_1000.jsonl
993	    data_count: 1000
994	    model_name: pythia-2.8b
995	    seed: all
996	    prompt_type: elaboration
997	    checkpoint_path: /root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl
998	    wall_clock_seconds: 19266.7
999	    gpu_hours: 5.35
1000	  METRICS:
1001	    total_records: 4946
1002	    unique_seeds: 995
1003	    skipped: 14
1004	    depth_distribution: {'0': 995, '1': 995, '2': 989, '3': 986, '4': 981}
1005	    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl
1006	    file_size_mb: 5.53
1007	    runtime_seconds: 8960.2
1008	    depth_retention_d4_d0: 0.986
1009	    logo_cv_f1: {'mean': 0.73, 'std': 0.011}
1010	    lopto_f1: 0.7622
1011	    feature_drift_entropy_mean: -0.4705
1012	    feature_drift_ttr: -0.6413
1013	    feature_drift_hapax: -0.8284
1014	    vs_continuation: retention 98.6% vs 83.1%; CV F1 0.730 vs 0.781 — elaboration chains more stable but depth signal weaker within-type
1015	    vs_rewriting: retention 98.6% vs 93.9%; CV F1 0.730 vs 0.737 — similar discriminability, elaboration slightly lower
1016	
1017	================================================================================
1018	EXPERIMENT 39: plan-005-rewrite
1019	================================================================================
1020	  Status:     DONE
1021	  Created:    2026-05-15T03:28:47.421Z
1022	  Completed:  2026-05-15T06:00:25.058Z
1023	  Conclusion: success
1024	  Hypothesis: Inspired rewriting 链数据生成：rewriting prompt 要求模型受启发重写而非逐字续写，预期 depth retention 介于 continuation 和 elaboration 之间，因为重写保留主题但改变表达
1025	  Parent:     plan-005
1026	  SPEC:
1027	    command: python generate_chain_prompt.py --model-name pythia-2.8b --prompt-type inspired_rewriting --input data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 1 --device cuda:0
1028	    server: autodl-5090
1029	    gpu: cuda:3
1030	    pid: 164881
1031	    log_path: ~/runs/gen-depth-fingerprint/plan-005-rewrite.log
1032	    submitted_at: 2026-05-15T03:28:47.322Z
1033	    submitted_via: submit_training_job
1034	    backend: tmux
1035	    account: root
1036	    data_path: data/wiki_seed_1000.jsonl
1037	    data_count: 1000
1038	    model_name: pythia-2.8b
1039	    seed: all
1040	    prompt_type: inspired_rewriting
1041	    checkpoint_path: /root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl
1042	    wall_clock_seconds: 8584
1043	    gpu_hours: 2.38
1044	  METRICS:
1045	    total_records: 4827
1046	    unique_seeds: 995
1047	    skipped: 61
1048	    depth_distribution: {'0': 995, '1': 995, '2': 959, '3': 944, '4': 934}
1049	    output_file: /root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl
1050	    file_size_mb: 5.41
1051	    runtime_seconds: 8584
1052	    speed_seeds_per_sec: 0.12
1053	    depth_retention_d4_d0: 0.939
1054	    vs_continuation: retention 93.9% vs 83.1%, rewriting produces significantly more stable depth chains
1055	
1056	================================================================================
1057	EXPERIMENT 40: plan-008-seed-stratification
1058	================================================================================
1059	  Status:     DONE
1060	  Created:    2026-05-17T00:21:12.380Z
1061	  Completed:  2026-05-17T00:21:48.235Z
1062	  Conclusion: success
1063	  Hypothesis: Seed complexity independence: depth fingerprint 的判别能力不依赖 seed 文本的词汇复杂度（按 gen-0 TTR terciles 分层验证）
1064	  Parent:     plan-010-robustness
1065	  SPEC:
1066	    command: python seed_stratification.py
1067	    server: autodl-5090
1068	    data_path: /root/gen-depth-fingerprint/data/
1069	    data_count: 37058
1070	    model_name: XGBoost 200/6
1071	    seed: 42
1072	  METRICS:
1073	    low_complexity_binary: 0.685
1074	    medium_binary: 0.695
1075	    high_complexity_binary: 0.695
1076	    low_complexity_multi: 0.772
1077	    medium_multi: 0.778
1078	    high_complexity_multi: 0.779
1079	    max_diff_binary_pp: 1.06
1080	    max_diff_multiclass_pp: 0.68
1081	    conclusion_label: seed_independent
1082	
1083	================================================================================
1084	EXPERIMENT 41: plan-010-llm-rephrase
1085	================================================================================
1086	  Status:     DONE
1087	  Created:    2026-05-16T22:26:58.107Z
1088	  Completed:  2026-05-17T01:04:28.657Z
1089	  Conclusion: success
1090	  Hypothesis: LLM-simulated editing robustness: Qwen3-0.6B rephrasing (1-3 sentences) 比 random word replacement 更接近真实人类编辑，预期 depth fingerprint 退化更小
1091	  Parent:     plan-010-robustness
1092	  SPEC:
1093	    command: python llm_rephrase_robustness.py
1094	    server: autodl-5090
1095	    gpu: cuda:0
1096	    data_path: /root/gen-depth-fingerprint/experiments/human_edit_robustness/
1097	    data_count: 5000
1098	    model_name: Qwen3-0.6B-Base + Pythia-410M
1099	    seed: 42
1100	  METRICS:
1101	    original_binary_f1: 0.6918
1102	    original_binary_ci: [0.6749, 0.7067]
1103	    original_multiclass_f1: 0.7385
1104	    original_multiclass_ci: [0.7269, 0.7496]
1105	    rephrased_binary_f1: 0.6471
1106	    rephrased_binary_ci: [0.6308, 0.6619]
1107	    rephrased_multiclass_f1: 0.6672
1108	    rephrased_multiclass_ci: [0.6548, 0.6796]
1109	    binary_drop: -0.0447
1110	    multiclass_drop: -0.0713
1111	    edit_distance_ratio: 0.5071
1112	    avg_sentences_replaced: 1.69
1113	    method: 7feature LOGO-CV, binary=gen1-vs-gen2+, 3class=gen0/gen1/gen2+
1114	    bugs_fixed: ['binary_task_gen1_vs_gen2+', '3class_mapping', 'tail_decay_rank100-1000']
1115	
1116	================================================================================
1117	EXPERIMENT 42: plan-010-robustness
1118	================================================================================
1119	  Status:     DONE
1120	  Created:    2026-05-16T22:09:57.049Z
1121	  Completed:  2026-05-16T22:11:48.657Z
1122	  Conclusion: success
1123	  Hypothesis: Human edit robustness: depth fingerprint 在 5-20% random word replacement 下的 F1 退化测试，验证实际编辑场景（通常 < 5%）不影响检测
1124	  Parent:     N/A
1125	  SPEC:
1126	    command: python human_edit_robustness.py
1127	    server: autodl-5090
1128	    gpu: cuda:0
1129	    data_path: /root/gen-depth-fingerprint/data/detector_scores_8gen.csv
1130	    data_count: 5000
1131	    model_name: Pythia-410M (reference)
1132	    seed: 42
1133	    perturbation_rates: [0.05, 0.1, 0.2]
1134	  METRICS:
1135	    baseline_binary_f1: 0.695
1136	    5pct_binary_f1: 0.65
1137	    10pct_binary_f1: 0.614
1138	    20pct_binary_f1: 0.591
1139	    5pct_drop: -0.046
1140	    10pct_drop: -0.081
1141	    20pct_drop: -0.104
1142	
1143	================================================================================
1144	EXPERIMENT 43: plan-013
1145	================================================================================
1146	  Status:     DONE
1147	  Created:    2026-05-14T23:33:25.590Z
1148	  Completed:  2026-05-14T23:53:38.902Z
1149	  Conclusion: success
1150	  Hypothesis: 文本长度混淆控制：深度特征的区分力是否独立于文本长度变化（长度归一化后趋势是否保持）
1151	  Parent:     N/A
1152	  SPEC:
1153	    command: python text_length_analysis.py
1154	    server: autodl-5090
1155	    data_path: /root/gen-depth-fingerprint/data/features_all_models.csv
1156	    data_count: 23032
1157	    model_name: text length analysis
1158	    seed: 42
1159	    checkpoint_path: /root/gen-depth-fingerprint/data/text_length_analysis.json
1160	    log_path: /root/gen-depth-fingerprint/data/text_length_boxplot.png
1161	  METRICS:
1162	    spearman_rho_range: [-0.066, +0.134]
1163	    length_depth_correlation: weak (|ρ|<0.14)
1164	    normalized_ttr_trend_preserved: True
1165	    normalized_hapax_trend_preserved: True
1166	    normalized_rho_stronger: True
1167	    length_matched_f1_delta: +0.041
1168	    length_is_confound: False
1169	    dropout_short_text_bias: True
1170	
1171	================================================================================
1172	EXPERIMENT 44: plan-014
1173	================================================================================
1174	  Status:     DONE
1175	  Created:    2026-05-15T00:12:01.909Z
1176	  Completed:  2026-05-15T03:47:24.272Z
1177	  Conclusion: success
1178	  Hypothesis: 大模型规模泛化：Qwen3-8B (7B+参数) 的 continuation 链是否展现同样的 entropy 收敛和 lexical drift，验证 depth dynamics 不因模型容量增大而消失（更大模型可能有更强的分布记忆导致 depth signal 衰减）
1179	  Parent:     plan-002
1180	  SPEC:
1181	    command: nohup /root/miniconda3/bin/python generate_chain.py --model-name qwen3-8b --model-path /root/autodl-tmp/models/Qwen/Qwen3-8B-Base/Qwen/Qwen3-8B-Base/ --input data/openwebtext_seeds.jsonl --shard-id 0 --num-shards 1 --device cuda:0 > /tmp/gen_large_model.log 2>&1 &
1182	    server: autodl-5090
1183	    gpu: cuda:0
1184	    pid: 134817
1185	    data_path: data/wiki_seed_1000.jsonl
1186	    data_count: 996
1187	    model_name: Qwen3-8B-Base
1188	    seed: all
1189	    log_path: /tmp/gen_large_model.log
1190	    checkpoint_path: /root/gen-depth-fingerprint/data/qwen3-8b/generations_shard0.jsonl
1191	    output_path: data/qwen3-8b/generations_shard0.jsonl
1192	    estimated_duration_h: 4
1193	    model_params: 8.2B
1194	    fp16_vram_gb: 16.1
1195	  METRICS:
1196	    total_records: 4497
1197	    unique_seeds: 995
1198	    depth_dist: {'0': 995, '1': 979, '2': 937, '3': 831, '4': 755}
1199	    logo_6gen_avg_f1: 0.7893
1200	    logo_per_generator: {'olmo-2-1b': 0.7635, 'pythia-1b': 0.8562, 'pythia-2.8b': 0.8041, 'qwen3-0.6b': 0.8243, 'qwen3-1.7b': 0.8046, 'qwen3-8b': 0.6832}
1201	    logo_qwen3_8b_held_out_f1: 0.6832
1202	    logo_5gen_baseline_f1: 0.8
1203	    spearman: {'hapax_ratio': -0.5578, 'ttr': -0.5419, 'entropy_mean': -0.4754, 'entropy_min': -0.3029, 'entropy_max': 0.0946, 'tail_decay': -0.0894, 'entropy_std': -0.0755}
1204	    feature_importance: {'hapax_ratio': 0.269, 'entropy_mean': 0.1637, 'ttr': 0.159, 'entropy_max': 0.0634, 'entropy_std': 0.0463, 'entropy_min': 0.0153, 'tail_decay': 0.0123}
1205	    revalidation_v2_vs_snapshot: LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)
1206	    revalidation_v2_conclusion: complete_data_validates_snapshot_robustness
1207	
1208	================================================================================
1209	EXPERIMENT 45: plan-015
1210	================================================================================
1211	  Status:     DONE
1212	  Created:    2026-05-14T23:58:41.890Z
1213	  Completed:  2026-05-15T00:26:12.709Z
1214	  Conclusion: success
1215	  Hypothesis: 现有检测器 ordinal baseline：FastDetectGPT/LD-Score 等检测器的连续分数是否已提供 ordinal depth signal
1216	  Parent:     N/A
1217	  SPEC:
1218	    command: python detector_baseline.py (log_likelihood + fast_detect_gpt + entropy_mean)
1219	    server: autodl-5090
1220	    data_path: /root/gen-depth-fingerprint/data/features_all_models.csv
1221	    data_count: 23032
1222	    model_name: Pythia-410M (log_likelihood, FastDetectGPT, entropy_mean baselines)
1223	    seed: 42
1224	    checkpoint_path: /root/gen-depth-fingerprint/data/detector_baseline_results.json
1225	    log_path: /root/gen-depth-fingerprint/data/
1226	  METRICS:
1227	    seven_feature_logo_f1: 0.798
1228	    seven_feature_ci: [0.786, 0.799]
1229	    avg_logprob_logo_f1: 0.7653
1230	    avg_logprob_ci: [0.616, 0.82]
1231	    avg_logprob_spearman: 0.7876
1232	    ld_score_logo_f1: 0.7212
1233	    ld_score_ci: [0.588, 0.77]
1234	    ld_score_spearman: 0.7943
1235	    ld_score_pre_fix: 0.6854
1236	    fast_detect_gpt_logo_f1: 0.6269
1237	    fast_detect_gpt_ci: [0.511, 0.762]
1238	    fast_detect_gpt_spearman: 0.4325
1239	    binoculars_logo_f1: 0.579
1240	    binoculars_ci: [0.405, 0.664]
1241	    binoculars_spearman: 0.1989
1242	    binoculars_bug_confirmed: True
1243	    binoculars_bug_fix: denominator changed from CE(performer, obs_argmax) to CE(performer, shifted_ids)
1244	    bootstrap_n: 1000
1245	    bootstrap_delta_7feat_vs_avglogprob: {'delta': 0.039, 'p': 0, 'significant': True}
1246	    bootstrap_delta_7feat_vs_fdgpt: {'delta': 0.067, 'p': 0, 'significant': True}
1247	    best_single_detector: Avg-LogProb (0.7653)
1248	    seven_feature_advantage_pp: 3.3
1249	
1250	================================================================================
1251	EXPERIMENT 46: plan-015-v2
1252	================================================================================
1253	  Status:     DONE
1254	  Created:    2026-05-15T00:56:20.612Z
1255	  Completed:  2026-05-15T01:26:40.380Z
1256	  Conclusion: success
1257	  Hypothesis: Ordinal baseline bugfix + bootstrap CI: 修复 Binoculars denominator bug，验证 7-feature ensemble 显著优于所有单一检测器
1258	  Parent:     plan-015
1259	  SPEC:
1260	    command: PYTHONUNBUFFERED=1 HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=2 python scripts/ordinal_baseline.py --device cuda:0
1261	    server: autodl-5090
1262	    data_path: /root/gen-depth-fingerprint/data/
1263	    data_count: 0
1264	    model_name: pythia-410m+pythia-160m
1265	    seed: 42
1266	    checkpoint_path: N/A (analysis task)
1267	    log_path: /tmp/ordinal_baseline_v2.log
1268	  METRICS:
1269	    seven_feature_logo_f1: 0.798
1270	    seven_feature_ci95: [0.786, 0.799]
1271	    avg_logprob_logo_f1: 0.7653
1272	    avg_logprob_ci95: [0.616, 0.82]
1273	    ld_score_logo_f1: 0.7212
1274	    ld_score_ci95: [0.588, 0.77]
1275	    fastdetectgpt_logo_f1: 0.6269
1276	    fastdetectgpt_ci95: [0.511, 0.762]
1277	    binoculars_logo_f1: 0.579
1278	    binoculars_ci95: [0.405, 0.664]
1279	    binoculars_bug_fixed: True
1280	    ld_score_corrected_cv_f1: 0.7925
1281	    bootstrap_7feat_vs_avglogprob: {'delta': 0.039, 'p': 0, 'significant': True}
1282	    bootstrap_7feat_vs_fastdetectgpt: {'delta': 0.067, 'p': 0, 'significant': True}
1283	
1284	================================================================================
1285	EXPERIMENT 47: review-exp-a-baseline-ensemble
1286	================================================================================
1287	  Status:     PREPARING
1288	  Created:    2026-05-15T12:22:30.747Z
1289	  Completed:  N/A
1290	  Conclusion: N/A
1291	  Hypothesis: 审稿回应实验A：4-baseline ensemble + 统一超参对比，验证 7-feature vs 4-baseline vs 6-feature 在公平条件下的性能差异
1292	  Parent:     N/A
1293	
1294	================================================================================
1295	EXPERIMENT 48: review-exp-b-topic-drift
1296	================================================================================
1297	  Status:     DONE
1298	  Created:    2026-05-15T12:22:34.096Z
1299	  Completed:  2026-05-15T12:28:11.624Z
1300	  Conclusion: success
1301	  Hypothesis: Depth fingerprint 不仅仅捕捉 topic shift：语义漂移(embedding cosine similarity)与 depth 相关性弱(|ρ|<0.3)，而 entropy/lexical features 与 depth 的相关性强(|ρ|>0.5)，证明 depth signal 来自生成过程的统计特性而非内容偏移
1302	  Parent:     N/A
1303	  SPEC:
1304	    command: python scripts/review_topic_drift.py
1305	    server: autodl-5090
1306	    data_path: /root/gen-depth-fingerprint/data/
1307	    data_count: 27529
1308	    model_name: all-MiniLM-L6-v2
1309	    seed: 0
1310	  METRICS:
1311	    semantic_similarity_by_transition: {'0_to_1': {'mean': 0.622, 'std': 0.1647}, '1_to_2': {'mean': 0.6829, 'std': 0.1837}, '2_to_3': {'mean': 0.801, 'std': 0.2012}, '3_to_4': {'mean': 0.8587, 'std': 0.1895}}
1312	    prompt_type_avg_sim: {'continuation': 0.7168, 'elaboration': 0.8093, 'inspired_rewriting': 0.808}
1313	    shape_feature_correlations: {'entropy_std_rho': -0.1639, 'tail_decay_rho': 0.0675}
1314	    drifting_feature_correlations: {'hapax_ratio_rho': -0.1242, 'ttr_rho': -0.1784, 'entropy_mean_rho': -0.2859}
1315	
1316	================================================================================
1317	EXPERIMENT 49: review-exp-c-overall-ci
1318	================================================================================
1319	  Status:     DONE
1320	  Created:    2026-05-15T12:22:37.037Z
1321	  Completed:  2026-05-15T12:27:02.426Z
1322	  Conclusion: success
1323	  Hypothesis: 6-generator LOGO 的 overall bootstrap CI 窄且不跨越 chance level，entropy_max/entropy_min 的个体 Spearman ρ 验证其对 depth 的单调贡献方向（max 正相关因高 depth 分布更尖，min 负相关因低概率 tail 被压缩）
1324	  Parent:     N/A
1325	  SPEC:
1326	    command: python scripts/review_overall_ci.py
1327	    server: autodl-5090
1328	    data_path: data/features_all_models.csv
1329	    data_count: 27529
1330	    model_name: xgboost
1331	    seed: 42
1332	    checkpoint_path: n/a
1333	    log_path: results/review_overall_ci_results.json
1334	  METRICS:
1335	    overall_logo_f1: 0.7879
1336	    overall_ci95: [0.783, 0.7929]
1337	    spearman_entropy_max: 0.0503
1338	    spearman_entropy_min: -0.4061
1339	    spearman_hapax: -0.6467
1340	    spearman_ttr: -0.6302
1341	    spearman_entropy_mean: -0.6098
1342	    spearman_entropy_std: -0.1996
1343	    spearman_tail_decay: -0.0403
1344	
1345	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c587b879-a0f3-4f52-827f-cedab5faeb89",
  "isSidechain": true,
  "promptId": "4401d70d-bff1-46e1-857b-65011b5d7861",
  "agentId": "a8fa49f9541eeeeba",
  "type": "user",
  "uuid": "7c88379e-6e57-47e8-80d5-58b8e7b1ade0",
  "sourceToolAssistantUUID": "c587b879-a0f3-4f52-827f-cedab5faeb89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-17T12:43:49.802Z_

Now let me run the aggregation across all experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c88379e-6e57-47e8-80d5-58b8e7b1ade0",
  "isSidechain": true,
  "agentId": "a8fa49f9541eeeeba",
  "requestId": "req_011Cb8AJkSU46otEHbtZBDvF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40711b37-4715-448b-bbe8-7142781a2060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QukQeKWMbSMZ6APfkRYp6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24373,
      "cache_read_input_tokens": 21958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24373,
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

_source line 18 · 2026-05-17T12:44:23.015Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UUnZVba7RF7hBhYubHjEiU`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nfrom collections import defaultdict\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/8efbc484-bfff-4e42-950b-e677114371ba/tool-results/mcp-agent-ml-research-read_registry-1779021770007.txt') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexperiments = inner['data']['experiments']\n\n# Count statuses\nstatuses = defaultdict(int)\nfor exp in experiments.values():\n    statuses[exp.get('status', 'UNKNOWN')] += 1\nprint(\"=== STATUS COUNTS ===\")\nfor s, c in sorted(statuses.items()):\n    print(f\"  {s}: {c}\")\n\n# Aggregate all model names mentioned\nall_model_names = set()\ngenerator_models = set()\nreference_models = set()\ntemperatures = set()\nprompt_types = set()\nseed_sources = set()\nmax_depth = 0\ndecoding_strategies = set()\n\nfor exp_id, exp in experiments.items():\n    spec = exp.get('spec', {})\n    metrics = exp.get('metrics', {})\n    hyp = exp.get('hypothesis', '') or ''\n    \n    model_name = spec.get('model_name', '')\n    if model_name:\n        all_model_names.add(model_name)\n    \n    # Temperature\n    temp = spec.get('temperature')\n    if temp is not None:\n        temperatures.add(str(temp))\n    \n    # top_p\n    top_p = spec.get('top_p')\n    if top_p is not None:\n        decoding_strategies.add(f\"top_p={top_p}\")\n    \n    # Prompt type\n    pt = spec.get('prompt_type')\n    if pt:\n        prompt_types.add(pt)\n    \n    # Reference model\n    ref = spec.get('reference_model')\n    if ref:\n        reference_models.add(ref)\n    \n    # Perturbation rates\n    pr = spec.get('perturbation_rates')\n    if pr:\n        pass  # not decoding\n\n    # Depths from metrics\n    for k in ['depth_dist', 'depth_distribution']:\n        dd = metrics.get(k, {})\n        if isinstance(dd, dict):\n            for d_key in dd.keys():\n                try:\n                    d_val = int(d_key.replace('gen', ''))\n                    max_depth = max(max_depth, d_val)\n                except:\n                    pass\n\n    # Depths from spec\n    depths_spec = spec.get('depths', '')\n    if 'gen-4' in str(depths_spec) or 'gen4' in str(depths_spec):\n        max_depth = max(max_depth, 4)\n\n    # Seed text sources from data paths & hypothesis\n    dp = spec.get('data_path', '')\n    if 'wiki_seed' in dp or 'wiki' in dp.lower():\n        seed_sources.add('Wikipedia (wiki_seed_1000.jsonl)')\n    if 'openwebtext' in dp:\n        seed_sources.add('OpenWebText')\n    if 'news' in dp.lower() or 'academic' in dp.lower() or 'code' in dp.lower():\n        seed_sources.add('Multi-domain (News/Academic/Code)')\n    if 'seeds_' in dp:\n        for domain in ['news', 'academic', 'code']:\n            if domain in dp:\n                seed_sources.add(f'{domain.capitalize()} seeds')\n\n    # Check hypothesis for domains\n    if 'News' in hyp and 'Academic' in hyp and 'Code' in hyp:\n        seed_sources.add('Multi-domain (News/Academic/Code)')\n    if 'Wikipedia' in hyp or 'wiki' in hyp.lower():\n        seed_sources.add('Wikipedia')\n\n# Infer temperature from hypothesis text\nfor exp_id, exp in experiments.items():\n    hyp = exp.get('hypothesis', '') or ''\n    if 't=0.7' in hyp:\n        temperatures.add('0.7')\n    if 't=1.0' in hyp:\n        temperatures.add('1.0')\n    spec = exp.get('spec', {})\n    cmd = spec.get('command', '')\n    if 'temperature' in str(spec):\n        pass  # already captured\n\n# Categorize models\ngen_models_explicit = [\n    'EleutherAI/pythia-2.8b',\n    'EleutherAI/pythia-1b', \n    'Pythia-1B',\n    'allenai/OLMo-2-0425-1B',\n    'Qwen3-0.6B', 'Qwen/Qwen3-0.6B-Base',\n    'Qwen3-1.7B', 'Qwen/Qwen3-1.7B-Base',\n    'Qwen3-8B-Base',\n    'Mistral-7B-v0.3',\n    'pythia-2.8b',\n    'pythia-1b',\n]\n\nref_models_explicit = [\n    'EleutherAI/pythia-410m',\n    'Pythia-410M',\n    'OLMo-2-1B',\n    'Qwen3-0.6B',\n    'pythia-410m',\n    'pythia-160m',\n]\n\nprint(\"\\n=== ALL model_name VALUES IN SPEC ===\")\nfor m in sorted(all_model_names):\n    print(f\"  {m}\")\n\nprint(f\"\\n=== TEMPERATURES ===\")\nfor t in sorted(temperatures):\n    print(f\"  {t}\")\n\nprint(f\"\\n=== DECODING STRATEGIES ===\")\nfor d in sorted(decoding_strategies):\n    print(f\"  {d}\")\n\nprint(f\"\\n=== PROMPT TYPES ===\")\nfor p in sorted(prompt_types):\n    print(f\"  {p}\")\n\nprint(f\"\\n=== SEED TEXT SOURCES ===\")\nfor s in sorted(seed_sources):\n    print(f\"  {s}\")\n\nprint(f\"\\n=== MAX CHAIN DEPTH TESTED === {max_depth}\")\n\n# Check for instruction-tuned models\nprint(\"\\n=== INSTRUCTION-TUNED MODELS ===\")\ninstruct_found = False\nfor exp_id, exp in experiments.items():\n    spec = exp.get('spec', {})\n    mn = str(spec.get('model_name', '')).lower()\n    cmd = str(spec.get('command', '')).lower()\n    hyp = str(exp.get('hypothesis', '')).lower()\n    for kw in ['instruct', 'chat', 'sft', 'rlhf', 'dpo']:\n        if kw in mn or kw in cmd or kw in hyp:\n            print(f\"  Found '{kw}' in {exp_id}\")\n            instruct_found = True\nif not instruct_found:\n    print(\"  NONE - all models appear to be base/pretrained models\")\n\n# Check for human text baselines\nprint(\"\\n=== HUMAN TEXT BASELINES ===\")\nhuman_found = False\nfor exp_id, exp in experiments.items():\n    hyp = str(exp.get('hypothesis', '')).lower()\n    spec = exp.get('spec', {})\n    metrics = exp.get('metrics', {})\n    for kw in ['human', 'depth-0', 'gen-0', 'gen0', 'depth0']:\n        if kw in str(metrics).lower() or kw in hyp:\n            if 'human' in kw:\n                print(f\"  Human-related mention in {exp_id}\")\n                human_found = True\n                break\n    # gen-0 / depth-0 IS the human seed text\n    if 'gen0' in str(metrics) or 'gen-0' in str(metrics) or 'depth0' in str(spec):\n        pass  # gen-0 is the original human seed\n\nprint(\"  gen-0 / depth-0 in generation chains = original human seed text (Wikipedia/News/Academic/Code)\")\nprint(\"  plan-010-robustness and plan-010-llm-rephrase test robustness to human editing\")\nprint(\"  plan-004-v2 downstream includes depth0_only variant (human seeds only)\")\n\nPYEOF\n",
  "description": "Aggregate unique models, temperatures, strategies, prompts, seeds across all experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40711b37-4715-448b-bbe8-7142781a2060",
  "isSidechain": true,
  "agentId": "a8fa49f9541eeeeba",
  "requestId": "req_011Cb8AJkSU46otEHbtZBDvF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "794ce3e6-8bcd-4fe6-bbcc-789d963c129e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QukQeKWMbSMZ6APfkRYp6a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24373,
      "cache_read_input_tokens": 21958,
      "output_tokens": 2232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24373
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2232,
          "cache_read_input_tokens": 21958,
          "cache_creation_input_tokens": 24373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24373,
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

_source line 19 · 2026-05-17T12:44:23.124Z_

<details><summary>↩ Tool result · `toolu_01UUnZVba7RF7hBhYubHjEiU`</summary>

```text
=== STATUS COUNTS ===
  DONE: 41
  PREPARING: 8

=== ALL model_name VALUES IN SPEC ===
  EleutherAI/pythia-1b
  EleutherAI/pythia-2.8b (FP16)
  OLMo-2-0425-1B
  OLMo-2-1B (reference)
  OLMo-2-1B + Qwen3-0.6B as reference
  Pythia-1B + Qwen3-1.7B + Mistral-7B-v0.3
  Pythia-1B, Qwen3-1.7B, Mistral-7B-v0.3 (gen) + Pythia-410M (ref)
  Pythia-410M (log_likelihood, FastDetectGPT, entropy_mean baselines)
  Pythia-410M (reference)
  Qwen/Qwen3-0.6B-Base
  Qwen/Qwen3-1.7B-Base
  Qwen3-0.6B
  Qwen3-0.6B (reference)
  Qwen3-0.6B-Base + Pythia-410M
  Qwen3-1.7B
  Qwen3-8B-Base
  XGBoost 200/6
  XGBoost classifier
  all-MiniLM-L6-v2
  allenai/OLMo-2-0425-1B
  pythia-1b, olmo-2-1b, qwen3-1.7b, qwen3-0.6b (+ pythia-2.8b from MVP)
  pythia-2.8b
  pythia-410m
  pythia-410m+pythia-160m
  text length analysis
  xgboost

=== TEMPERATURES ===
  0.7
  1.0

=== DECODING STRATEGIES ===
  top_p=0.9

=== PROMPT TYPES ===
  continuation
  elaboration
  inspired_rewriting

=== SEED TEXT SOURCES ===
  Academic seeds
  Code seeds
  Multi-domain (News/Academic/Code)
  News seeds
  Wikipedia
  Wikipedia (wiki_seed_1000.jsonl)

=== MAX CHAIN DEPTH TESTED === 4

=== INSTRUCTION-TUNED MODELS ===
  NONE - all models appear to be base/pretrained models

=== HUMAN TEXT BASELINES ===
  Human-related mention in plan-010-robustness
  gen-0 / depth-0 in generation chains = original human seed text (Wikipedia/News/Academic/Code)
  plan-010-robustness and plan-010-llm-rephrase test robustness to human editing
  plan-004-v2 downstream includes depth0_only variant (human seeds only)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "794ce3e6-8bcd-4fe6-bbcc-789d963c129e",
  "isSidechain": true,
  "promptId": "4401d70d-bff1-46e1-857b-65011b5d7861",
  "agentId": "a8fa49f9541eeeeba",
  "type": "user",
  "uuid": "b5723a95-272e-4ed9-8ddb-7ccda3477995",
  "sourceToolAssistantUUID": "794ce3e6-8bcd-4fe6-bbcc-789d963c129e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-17T12:45:48.698Z_

Here is the complete analysis.

---

## EXPERIMENT REGISTRY: gen-depth-fingerprint (49 experiments)

### STATUS SUMMARY
- **DONE**: 41
- **PREPARING**: 8 (mostly infrastructure/shard jobs that were superseded or never finalized)

---

### PER-EXPERIMENT DETAILS

#### 1. exp_047_multi_domain_t07 — DONE (success)
- **Spec**: Pythia-1B, Qwen3-1.7B, Mistral-7B-v0.3 (generators) + Pythia-410M (ref). t=0.7, top_p=0.9. 200 seeds x 3 domains (News/Academic/Code) x 3 generators x 4 depths = 7200 samples.
- **Key metrics**: Overall binary F1 0.676, 3-class F1 0.681. News best (0.712), Academic worst (0.628). Delta vs t=1.0: -3.4pp (News), -11.1pp (Academic), -6.6pp (Code).

#### 2. multi-domain-seeds — DONE (success)
- **Spec**: Pythia-1B + Qwen3-1.7B + Mistral-7B-v0.3. 600 seeds across News/Academic/Code. seed=42.
- **Key metrics**: News binary F1 0.746, Academic 0.739, Code 0.754. Wikipedia baseline 0.815. Max gap vs wiki: 7.62pp. Conclusion: domain_independent.

#### 3. multi_domain_t07 — PREPARING (superseded by exp_047)
- Infrastructure-only entry (tmux submission record).

#### 4. mvp-001 — DONE (success)
- **Spec**: Pythia-2.8B (FP16) generator, Pythia-410M reference. t=0.7, top_p=0.9, 256 tokens. 1000 Wikipedia seeds, depths gen-0 to gen-4. Continuation prompting.
- **Key metrics**: Macro F1 0.841, binary F1 (gen0 vs gen2+) 0.865. CV macro F1 0.806 (std 0.013). 4609 records from 995 seeds.

#### 5-8. mvp-001-gen-s{0,1,2,3} — PREPARING (s0) / PREPARING+failed (s1,s2,s3)
- Shard-level generation jobs for mvp-001. Infrastructure records, superseded by the consolidated mvp-001 result.

#### 9. plan-001 — DONE (success)
- **Spec**: Feature ablation (parts A/B/C) on Pythia-410M reference features. 4609 records.
- **Key metrics**: Full F1 0.82, surface-only 0.76, reference-only 0.72.

#### 10. plan-001-fix — DONE (success)
- **Spec**: Ablation fix/verification. Pythia-410M, 4609 records, seed=42.
- **Key metrics**: Full F1 0.820, reference-only 0.719, surface-only 0.763. Bootstrap CIs non-overlapping. Median perplexity by depth: 13.50, 4.96, 3.00, 2.07, 1.72.

#### 11. plan-001-restore — PREPARING
- Infrastructure record for re-run.

#### 12. plan-002 — DONE (success)
- **Spec**: Cross-model generalization. 4 new generators: Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B (+ Pythia-2.8B from MVP). t=0.7, top_p=0.9, 256 tokens, 1000 Wikipedia seeds. Pythia-410M reference.
- **Key metrics**: 18,423 total records across 4 models.

#### 13. plan-002-eval — DONE (success)
- **Spec**: Cross-generator evaluation using leave-one-generator-out (LOGO). XGBoost classifier. 23,032 records.
- **Key metrics**: LOGO avg F1 0.804. Best held-out: Pythia-1B (0.851). Worst: OLMo-2-1B (0.752). Top features: hapax_ratio (0.289), ttr (0.168), entropy_mean (0.160).

#### 14-15. plan-002-olmo2-s{0,1} — DONE (success)
- OLMo-2-0425-1B generation shards. ~497-498 seeds each, depths 0-4. Total ~4713 records.

#### 16-17. plan-002-pythia1b-s{0,1} — DONE (success)
- Pythia-1B generation shards. ~497-498 seeds each, depths 0-4. Total ~4555 records.

#### 18-19. plan-002-qwen06b-r2-s{0,1} — DONE (success)
- Qwen3-0.6B generation (round 2, after fixing model path). ~498 seeds each.

#### 20-21. plan-002-qwen06b-s{0,1} — DONE (failed)
- Failed first attempts for Qwen3-0.6B (model path issues).

#### 22-23. plan-002-qwen17b-r2-s{0,1} — DONE (success)
- Qwen3-1.7B generation (round 2). ~498 seeds each, depths 0-4.

#### 24-25. plan-002-qwen17b-retry-s{0,1} — DONE (failed)
- Failed retry attempts for Qwen3-1.7B.

#### 26-27. plan-002-qwen17b-s{0,1} — DONE (failed)
- Killed duplicates for Qwen3-1.7B.

#### 28-29. plan-002-qwen3-1_7b-s{0,1} — DONE (failed/killed)
- Earlier killed attempts for Qwen3-1.7B.

#### 30. plan-003 — DONE (success)
- **Spec**: Cross-reference-model falsification. OLMo-2-1B + Qwen3-0.6B as alternative reference models. 23,032 records.
- **Key metrics**: LOGO F1 with Pythia ref: 0.803, OLMo ref: 0.807, Qwen ref: 0.816. All refs show negative entropy drift. Depth signal is NOT a Pythia artifact.

#### 31. plan-003-olmo2ref — DONE (success)
- Feature extraction with OLMo-2-1B as reference model. 23,032 records.

#### 32. plan-003-qwen06bref — DONE (success)
- Feature extraction with Qwen3-0.6B as reference model. 23,032 records.

#### 33. plan-004 — DONE (failed)
- Downstream utility attempt (disk space issue). OLMo-2-0425-1B CLM fine-tuning on depth-stratified data.

#### 34. plan-004-prep — PREPARING (success)
- Preparation for downstream: 5 data variants (depth0_only: 797, depth01: 3951, all: 12299, size_matched: 3951, binary_filtered: 3951).

#### 35. plan-004-v2 — DONE (negative)
- **Spec**: Downstream CLM fine-tuning retry. OLMo-2-0425-1B, 5 variants x 3 seeds (42,123,456).
- **Key metrics**: Ranking by perplexity: all(2.335) < size_matched(2.367) < depth01(2.387) ~ binary_filtered(2.389) << depth0_only(2.681). Seed variance tiny (<0.002). **Conclusion: negative** (more data always better; depth stratification adds no signal beyond data volume).

#### 36. plan-005 — DONE (success)
- **Spec**: Prompt type comparison. Pythia-2.8B, 1000 seeds, 3 prompt types (continuation/elaboration/inspired_rewriting) x 5 depths = 14,393 texts.
- **Key metrics**: CV F1: continuation 0.781 > rewriting 0.737 > elaboration 0.730. Depth retention (d4/d0): elaboration 0.986 > rewriting 0.939 > continuation 0.831. LOPTO avg F1: 0.753.

#### 37. plan-005-cont — DONE (success)
- Continuation chain generation. 4620 records, 995 seeds, depths 0-4.

#### 38. plan-005-elab — DONE (success)
- Elaboration chain generation. 4946 records, 995 seeds. Depth retention 98.6%.

#### 39. plan-005-rewrite — DONE (success)
- Inspired rewriting chain generation. 4827 records, 995 seeds. Depth retention 93.9%.

#### 40. plan-008-seed-stratification — DONE (success)
- **Spec**: Seed complexity independence. 37,058 records, XGBoost 200/6.
- **Key metrics**: Low/medium/high complexity binary F1: 0.685/0.695/0.695. Max diff: 1.06pp. Conclusion: seed_independent.

#### 41. plan-010-llm-rephrase — DONE (success)
- **Spec**: LLM-simulated editing robustness. Qwen3-0.6B-Base rephrase + Pythia-410M ref. 5000 records.
- **Key metrics**: Original binary F1 0.692, rephrased 0.647 (drop -4.5pp). Edit distance ratio 0.507, avg 1.69 sentences replaced.

#### 42. plan-010-robustness — DONE (success)
- **Spec**: Random word replacement robustness at 5%/10%/20% perturbation. Pythia-410M ref. 5000 records.
- **Key metrics**: Baseline 0.695, 5% -> 0.650 (-4.6pp), 10% -> 0.614 (-8.1pp), 20% -> 0.591 (-10.4pp).

#### 43. plan-013 — DONE (success)
- **Spec**: Text length confound analysis. 23,032 records.
- **Key metrics**: Spearman rho range [-0.066, +0.134] (weak length-depth correlation). Length-matched F1 delta +0.041. Length is NOT a confound.

#### 44. plan-014 — DONE (success)
- **Spec**: Large-model scaling. Qwen3-8B-Base (8.2B params, 16.1GB VRAM). 996 Wikipedia seeds.
- **Key metrics**: 4497 records. LOGO 6-gen avg F1 0.789. Qwen3-8B held-out F1 0.683. Per-generator LOGO: Pythia-1B best (0.856), Qwen3-8B worst (0.683).

#### 45. plan-015 — DONE (success)
- **Spec**: Ordinal baseline comparison. Pythia-410M + Pythia-160M. 23,032 records. Detectors: log-likelihood, FastDetectGPT, LD-Score, Binoculars.
- **Key metrics**: 7-feature F1 0.798 > Avg-LogProb 0.765 > LD-Score 0.721 > FastDetectGPT 0.627 > Binoculars 0.579. 7-feature advantage +3.3pp over best single detector (significant, p=0).

#### 46. plan-015-v2 — DONE (success)
- **Spec**: Ordinal baseline with Binoculars bug fix + bootstrap CI.
- **Key metrics**: Confirms plan-015 results. LD-Score corrected CV F1 0.793.

#### 47. review-exp-a-baseline-ensemble — PREPARING
- **Spec**: Planned 4-baseline ensemble + unified hyperparameter comparison. Not yet executed.

#### 48. review-exp-b-topic-drift — DONE (success)
- **Spec**: Topic drift analysis using all-MiniLM-L6-v2 embeddings. 27,529 records.
- **Key metrics**: Semantic similarity increases with depth transitions (0->1: 0.622, 3->4: 0.859). Entropy/lexical features correlate with depth much more strongly than semantic drift. Depth signal is NOT just topic shift.

#### 49. review-exp-c-overall-ci — DONE (success)
- **Spec**: Overall LOGO bootstrap CI. XGBoost, 27,529 records.
- **Key metrics**: Overall LOGO F1 0.788 [0.783, 0.793]. Spearman: hapax_ratio -0.647, ttr -0.630, entropy_mean -0.610.

---

### CROSS-EXPERIMENT AGGREGATION

#### All Unique Generator Models (with parameter counts)
| Model | Params | Family |
|---|---|---|
| EleutherAI/pythia-2.8b | 2.8B | Pythia |
| EleutherAI/pythia-1b | 1B | Pythia |
| allenai/OLMo-2-0425-1B | 1B | OLMo |
| Qwen3-0.6B-Base | 0.6B | Qwen |
| Qwen3-1.7B-Base | 1.7B | Qwen |
| Qwen3-8B-Base | 8.2B | Qwen |
| Mistral-7B-v0.3 | 7B | Mistral |

Total: **7 generator models** spanning 4 model families, 0.6B to 8.2B parameters.

#### All Reference Models
| Model | Params | Role |
|---|---|---|
| EleutherAI/pythia-410m | 410M | Primary reference (all main experiments) |
| EleutherAI/pythia-160m | 160M | Used in Binoculars baseline |
| OLMo-2-0425-1B | 1B | Cross-ref falsification (plan-003) |
| Qwen3-0.6B-Base | 0.6B | Cross-ref falsification (plan-003) |

#### All Temperature Settings
- **0.7** (standard, used in most experiments)
- **1.0** (used in multi-domain-seeds initial run; exp_047 specifically tests t=0.7 to eliminate the t=1.0 confound)

#### All Decoding Strategies
- **top_p=0.9** (nucleus sampling, only strategy explicitly recorded)
- Temperature sampling (via the temperature settings above)
- No beam search, greedy, or top-k experiments recorded

#### All Prompt Types
- **continuation** (standard prefix continuation)
- **elaboration** (expand/elaborate on the seed)
- **inspired_rewriting** (write inspired by the seed, not verbatim)

#### All Seed Text Sources
- **Wikipedia** (wiki_seed_1000.jsonl, 1000 seeds, primary dataset)
- **News** domain seeds (200 seeds)
- **Academic** domain seeds (200 seeds)
- **Code** domain seeds (200 seeds)
- (OpenWebText referenced in one command but the actual data used was wiki_seed_1000.jsonl)

#### Maximum Chain Depth Tested
- **Depth 4** (gen-0 through gen-4, i.e., 5 levels: original human + 4 generations)

#### Instruction-Tuned Models
- **NONE**. All 7 generator models are base/pretrained models. No chat, instruct, SFT, RLHF, or DPO models were tested.

#### Human Text Baselines
- **gen-0 / depth-0** in every chain IS the original human seed text (from Wikipedia, News, Academic, or Code sources)
- **plan-004-v2** includes a `depth0_only` training variant (797 human-only samples) for downstream fine-tuning comparison
- **plan-010-robustness** and **plan-010-llm-rephrase** test robustness to simulated human editing (random word replacement at 5-20% and LLM sentence rephrasing)

---

### COVERAGE GAPS WORTH NOTING

1. **No instruction-tuned models** tested at all (only base models)
2. **Only one decoding strategy** (nucleus sampling with top_p=0.9); no beam search, greedy, top-k, or min-p
3. **Only two temperature values** (0.7 and 1.0)
4. **Maximum depth is 4** (no experiments go to depth 5+)
5. **review-exp-a-baseline-ensemble** is still PREPARING (not yet executed)
6. **8 experiments** remain in PREPARING status (mostly superseded infrastructure records, but review-exp-a is a substantive gap)
7. **One negative result**: plan-004-v2 downstream fine-tuning showed depth stratification has no benefit beyond data volume

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5723a95-272e-4ed9-8ddb-7ccda3477995",
  "isSidechain": true,
  "agentId": "a8fa49f9541eeeeba",
  "requestId": "req_011Cb8AMTL9j3FmGgk83VvFk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39d314c8-a9d3-46b8-a6b3-a31cd50db28b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "8efbc484-bfff-4e42-950b-e677114371ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwFin7TcQm1czapZbxx6Ay",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3061,
      "cache_read_input_tokens": 46331,
      "output_tokens": 4367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3061
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4367,
          "cache_read_input_tokens": 46331,
          "cache_creation_input_tokens": 3061,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3061,
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
