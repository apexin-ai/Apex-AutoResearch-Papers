# Research conversation: Extract QW (Qwen) accuracy dose curve experiments from the registry JSON file at: /home/ubuntu/.claude-account-3/project

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a3e0a592254fabea7.jsonl`
- **Structured JSON:** [`693bafef1c5e83f7d2cb.json`](../../sessions/69/693bafef1c5e83f7d2cb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

14 recorded events

### User

_source line 1 · 2026-05-16T00:26:09.616Z_

Extract QW (Qwen) accuracy dose curve experiments from the registry JSON file at:
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt

The file is JSON with schema: {result: string} where result is a JSON string containing an array of experiments.

I need experiments with IDs matching:
- acc_qw_dense_n100
- acc_qw_s015_n100
- acc_qw_s020_n100 (and _b2_fix variant)
- acc_qw_s025_n100 (and _b2_fix variant)
- acc_qw_s030_n100
- Any other acc_qw_* experiments

For each experiment, extract ALL fields verbatim:
1. exp_id
2. status
3. conclusion
4. metrics (ALL - especially combined_accuracy, truncation_rate, correct counts, batch details)
5. notes
6. Any other relevant fields

Use jq or python to parse. First probe the structure, then extract. Report everything verbatim - don't summarize away any metrics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5d98afa4-bc8d-47c1-b014-8bbe0580361f",
  "agentId": "a3e0a592254fabea7",
  "type": "user",
  "uuid": "3a83814d-c165-45cd-a3ca-3a4cff833624",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T00:26:09.620Z_

```json
{
  "parentUuid": "3a83814d-c165-45cd-a3ca-3a4cff833624",
  "isSidechain": true,
  "agentId": "a3e0a592254fabea7",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
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
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
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
  "uuid": "1b099eda-34dc-4460-b911-ab9ea54a6f5b",
  "timestamp": "2026-05-16T00:26:09.620Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T00:26:12.574Z_



I'll start by probing the file structure, then extract the relevant experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b099eda-34dc-4460-b911-ab9ea54a6f5b",
  "isSidechain": true,
  "agentId": "a3e0a592254fabea7",
  "requestId": "req_011Cb5JFURt2R8Kp6dNKYVx9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "914624f2-f026-4071-acfe-b3b6203fbfaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DNNuhfYg9jjW1RGhBKjP3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6135,
      "cache_read_input_tokens": 7333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6135,
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

_source line 4 · 2026-05-16T00:26:13.471Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KLEKS4niVda28yfvDka1sj`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "914624f2-f026-4071-acfe-b3b6203fbfaa",
  "isSidechain": true,
  "agentId": "a3e0a592254fabea7",
  "requestId": "req_011Cb5JFURt2R8Kp6dNKYVx9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e85a4405-78ad-4107-98f3-e741aded624b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DNNuhfYg9jjW1RGhBKjP3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6135,
      "cache_read_input_tokens": 7333,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6135
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 182,
          "cache_read_input_tokens": 7333,
          "cache_creation_input_tokens": 6135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6135,
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

_source line 5 · 2026-05-16T00:26:13.704Z_

<details><summary>↩ Tool result · `toolu_01KLEKS4niVda28yfvDka1sj`</summary>

```text
212157 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e85a4405-78ad-4107-98f3-e741aded624b",
  "isSidechain": true,
  "promptId": "5d98afa4-bc8d-47c1-b014-8bbe0580361f",
  "agentId": "a3e0a592254fabea7",
  "type": "user",
  "uuid": "c6c0f065-847a-49ac-b36f-7a8cf808b954",
  "sourceToolAssistantUUID": "e85a4405-78ad-4107-98f3-e741aded624b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T00:26:19.926Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DNC5Lz6A8zUCcwthyWCaPz`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt', 'r') as f:\n    raw = json.load(f)\n\n# Parse the outer wrapper\nresult = json.loads(raw['result'])\nprint(f'Type of result: {type(result)}')\nprint(f'Number of entries: {len(result)}')\n\n# Show first entry keys to understand structure\nif len(result) > 0:\n    print(f'Keys in first entry: {list(result[0].keys())}')\n    \n# Find all acc_qw_* experiments\nqw_exps = [e for e in result if e.get('exp_id','').startswith('acc_qw_')]\nprint(f'\\nFound {len(qw_exps)} acc_qw_* experiments:')\nfor e in qw_exps:\n    print(f'  - {e[\\\"exp_id\\\"]}')\n\"\n",
  "description": "Parse JSON and find all acc_qw_* experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6c0f065-847a-49ac-b36f-7a8cf808b954",
  "isSidechain": true,
  "agentId": "a3e0a592254fabea7",
  "requestId": "req_011Cb5JFmwqYCn9HbDRbJ2Hn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fb38fec-4ed9-485e-88f3-fafbfcc26860",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYonkMFj4nrTJnpacVrhCY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1127,
      "cache_read_input_tokens": 13468,
      "output_tokens": 388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1127
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 388,
          "cache_read_input_tokens": 13468,
          "cache_creation_input_tokens": 1127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1127,
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

_source line 7 · 2026-05-16T00:26:20.263Z_

<details><summary>↩ Tool result · reported error · `toolu_01DNC5Lz6A8zUCcwthyWCaPz`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 14, in &lt;module>
    print(f'Keys in first entry: {list(result[0].keys())}')
                                       ~~~~~~^^^
KeyError: 0
Type of result: &lt;class 'dict'>
Number of entries: 4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fb38fec-4ed9-485e-88f3-fafbfcc26860",
  "isSidechain": true,
  "promptId": "5d98afa4-bc8d-47c1-b014-8bbe0580361f",
  "agentId": "a3e0a592254fabea7",
  "type": "user",
  "uuid": "a3f43f19-041f-42e2-a2b2-1e51561cbd3f",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 14, in &lt;module>\n    print(f'Keys in first entry: {list(result[0].keys())}')\n                                       ~~~~~~^^^\nKeyError: 0\nType of result: &lt;class 'dict'>\nNumber of entries: 4",
  "sourceToolAssistantUUID": "9fb38fec-4ed9-485e-88f3-fafbfcc26860",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T00:26:25.119Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016piFnhTj1X6k2XMkXTgCiL`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt', 'r') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nprint(f'Top-level keys: {list(result.keys())}')\nfor k in result:\n    v = result[k]\n    print(f'  {k}: type={type(v).__name__}, ', end='')\n    if isinstance(v, list):\n        print(f'len={len(v)}')\n    elif isinstance(v, dict):\n        print(f'keys={list(v.keys())[:5]}')\n    else:\n        print(f'value={str(v)[:100]}')\n\"\n",
  "description": "Explore top-level structure of parsed result"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3f43f19-041f-42e2-a2b2-1e51561cbd3f",
  "isSidechain": true,
  "agentId": "a3e0a592254fabea7",
  "requestId": "req_011Cb5JGFyJvzbS5fYmA9Quy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8b1da1c-31d7-49de-b580-b5d0e97a64dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVzBSFCK3MKeau7SUtSbyB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 490,
      "cache_read_input_tokens": 14595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 490,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 9 · 2026-05-16T00:26:25.225Z_

<details><summary>↩ Tool result · `toolu_016piFnhTj1X6k2XMkXTgCiL`</summary>

```text
Top-level keys: ['success', 'data', 'error', 'metadata']
  success: type=bool, value=True
  data: type=dict, keys=['experiments', 'count', 'total', 'baseline']
  error: type=NoneType, value=None
  metadata: type=dict, keys=['elapsed_seconds']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8b1da1c-31d7-49de-b580-b5d0e97a64dd",
  "isSidechain": true,
  "promptId": "5d98afa4-bc8d-47c1-b014-8bbe0580361f",
  "agentId": "a3e0a592254fabea7",
  "type": "user",
  "uuid": "908a9fa2-6d16-4d32-a23b-abdbfc9e3e62",
  "sourceToolAssistantUUID": "f8b1da1c-31d7-49de-b580-b5d0e97a64dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T00:26:31.426Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ScbuCJJ4Q2SE8UscMuBh9u`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt', 'r') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nexperiments = result['data']['experiments']\nprint(f'Total experiments: {len(experiments)}')\nprint(f'Type: {type(experiments)}')\n\n# Check if it's a list or dict\nif isinstance(experiments, list):\n    # Find all acc_qw_*\n    qw_exps = [e for e in experiments if e.get('exp_id','').startswith('acc_qw_')]\n    print(f'Found {len(qw_exps)} acc_qw_* experiments')\n    for e in qw_exps:\n        print(f'  - {e[\\\"exp_id\\\"]}')\nelif isinstance(experiments, dict):\n    qw_keys = [k for k in experiments if k.startswith('acc_qw_')]\n    print(f'Found {len(qw_keys)} acc_qw_* experiments')\n    for k in qw_keys:\n        print(f'  - {k}')\n\"\n",
  "description": "Drill into experiments structure and find acc_qw_* entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "908a9fa2-6d16-4d32-a23b-abdbfc9e3e62",
  "isSidechain": true,
  "agentId": "a3e0a592254fabea7",
  "requestId": "req_011Cb5JGdytcK8u3hi7KzCsu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f78b3391-bea5-4b9f-bba6-6db6a1e6be50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSSaTeS2689yh2x7ZednA4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 429,
      "cache_read_input_tokens": 15085,
      "output_tokens": 444,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 429
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 444,
          "cache_read_input_tokens": 15085,
          "cache_creation_input_tokens": 429,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 429,
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

_source line 11 · 2026-05-16T00:26:31.598Z_

<details><summary>↩ Tool result · `toolu_01ScbuCJJ4Q2SE8UscMuBh9u`</summary>

```text
Total experiments: 116
Type: &lt;class 'dict'>
Found 9 acc_qw_* experiments
  - acc_qw_s025_n100_b2_fix
  - acc_qw_s020_n100_b2_fix
  - acc_qw_s030_n100
  - acc_qw_dense_n100
  - acc_qw_s015_n100
  - acc_qw_s025_n100
  - acc_qw_s020_n100
  - acc_qw_s025
  - acc_qw_s020
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f78b3391-bea5-4b9f-bba6-6db6a1e6be50",
  "isSidechain": true,
  "promptId": "5d98afa4-bc8d-47c1-b014-8bbe0580361f",
  "agentId": "a3e0a592254fabea7",
  "type": "user",
  "uuid": "10ca3782-c7e7-497c-ab70-f71369e3349a",
  "sourceToolAssistantUUID": "f78b3391-bea5-4b9f-bba6-6db6a1e6be50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T00:26:36.146Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CumkeeM1pYAaDVv3v7JRfX`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/38576691-e177-4a18-ab23-be69eff4b7ff/tool-results/mcp-agent-ml-research-read_registry-1778891148151.txt', 'r') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nexperiments = result['data']['experiments']\n\nqw_keys = sorted([k for k in experiments if k.startswith('acc_qw_')])\n\nfor k in qw_keys:\n    exp = experiments[k]\n    print('=' * 80)\n    print(f'EXPERIMENT: {k}')\n    print('=' * 80)\n    print(json.dumps(exp, indent=2, ensure_ascii=False))\n    print()\n\" 2>&1",
  "description": "Extract all acc_qw_* experiments with full details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10ca3782-c7e7-497c-ab70-f71369e3349a",
  "isSidechain": true,
  "agentId": "a3e0a592254fabea7",
  "requestId": "req_011Cb5JH6RcE29LLgf43v7eu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e25d82d-31c1-4e4c-ba15-2744b33bd32a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRxjhbZ9gbzHTz4b3JBv3h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 15514,
      "output_tokens": 323,
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
          "output_tokens": 323,
          "cache_read_input_tokens": 15514,
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

_source line 13 · 2026-05-16T00:26:36.354Z_

<details><summary>↩ Tool result · `toolu_01CumkeeM1pYAaDVv3v7JRfX`</summary>

```text
================================================================================
EXPERIMENT: acc_qw_dense_n100
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T21:34:35.557Z",
  "updated_at": "2026-05-15T21:54:45.453Z",
  "hypothesis": "补跑 QW dense problems 51-100，扩展到 n=100 以降低噪声",
  "spec": {
    "command": "python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions dense --num-problems 50 --start-index 50 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_dense_n51_100.json",
    "server": "westd-22162",
    "gpu": [
      "cuda:2"
    ],
    "pid": "279068",
    "log_path": "/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_dense_n51_100.json",
    "submitted_at": "2026-05-15T21:35:05.456Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "MATH problems 51-100",
    "data_count": 50,
    "model_name": "Qwen2.5-7B-Instruct",
    "seed": 42,
    "checkpoint_path": "N/A (eval only)",
    "wall_clock_seconds": 1176.6,
    "gpu_hours": 0.33
  },
  "metrics": {
    "batch1_correct": 16,
    "batch1_total": 50,
    "batch1_acc": 0.32,
    "batch2_correct": 24,
    "batch2_total": 50,
    "batch2_acc": 0.48,
    "combined_correct": 40,
    "combined_total": 100,
    "combined_acc": 0.4
  },
  "conclusion": "success",
  "completed_at": "2026-05-15T21:54:42.068Z"
}

================================================================================
EXPERIMENT: acc_qw_s015_n100
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T21:34:38.959Z",
  "updated_at": "2026-05-15T21:50:13.043Z",
  "hypothesis": "补跑 QW importance_s015 problems 51-100，扩展到 n=100 以降低噪声",
  "spec": {
    "command": "python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s015 --num-problems 50 --start-index 50 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s015_n51_100.json",
    "server": "westd-22162",
    "gpu": [
      "cuda:3"
    ],
    "pid": "279145",
    "log_path": "/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s015_n51_100.json",
    "submitted_at": "2026-05-15T21:35:07.387Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "MATH problems 51-100",
    "data_count": 50,
    "model_name": "Qwen2.5-7B-Instruct",
    "seed": 42,
    "checkpoint_path": "N/A (eval only)"
  },
  "metrics": {
    "batch1_acc": 0.34,
    "batch1_correct": 17,
    "batch1_total": 50,
    "batch2_acc": 0.38,
    "batch2_correct": 19,
    "batch2_total": 50,
    "combined_acc": 0.36,
    "combined_correct": 36,
    "combined_total": 100
  },
  "conclusion": "success",
  "checkpoint_path": "N/A (eval only)",
  "log_path": "/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s015_n51_100.json",
  "completed_at": "2026-05-15T21:47:46.664Z"
}

================================================================================
EXPERIMENT: acc_qw_s020
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T20:49:27.167Z",
  "updated_at": "2026-05-15T21:17:22.146Z",
  "spec": {
    "command": "python run_accuracy_eval.py --model Qwen2.5-7B-Instruct --conditions importance_s020 --num-problems 50",
    "server": "westd-22162",
    "gpu": [
      "cuda:2"
    ],
    "pid": "274623",
    "log_path": "~/runs/phase-gated-compound-sparse/acc_qw_s020.log",
    "submitted_at": "2026-05-15T20:50:03.654Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/autodl-tmp/pacs/data/math500.json",
    "data_count": 50,
    "model_name": "Qwen2.5-7B-Instruct",
    "seed": 42,
    "type": "eval",
    "checkpoint_source": "checkpoints/Qwen2.5-7B-Instruct",
    "eval_data": "MATH-500 n=50",
    "wall_clock_seconds": 878.3,
    "gpu_hours": 0.24
  },
  "reproduce": {
    "finished_at": "2026-05-15T21:00:49.632Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-15T21:00:52.877256+00:00"
      }
    ]
  },
  "metrics": {
    "qw_s020_acc": 0.26,
    "qw_s020_correct": 13,
    "qw_s020_total": 50,
    "qw_s020_delta_vs_dense": -0.06,
    "null_count": 2,
    "null_rate": 0.04,
    "output_truncated_count": 2,
    "output_truncated_rate": 0.04,
    "extraction_failure_count": 0,
    "extraction_failure_rate": 0,
    "wrong_count": 35,
    "wrong_rate": 0.7,
    "heads_pruned": 140,
    "total_time_s": 598,
    "note": "v2 rescored with fixed radical+degree matcher"
  },
  "conclusion": "negative",
  "checkpoint_path": "/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s020.json",
  "completed_at": "2026-05-15T21:04:41.944Z"
}

================================================================================
EXPERIMENT: acc_qw_s020_n100
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T21:09:34.155Z",
  "updated_at": "2026-05-15T21:34:46.864Z",
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=2 python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s020 --num-problems 50 --start-index 50 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s020_n51_100.json",
    "server": "westd-22162",
    "data_path": "MATH-500",
    "data_count": 50,
    "model_name": "Qwen2.5-7B-Instruct",
    "seed": 42,
    "description": "QW importance_s020 accuracy eval problems 51-100",
    "checkpoint_source": "/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct",
    "eval_data": "MATH-500 problems 51-100",
    "checkpoint_path": "N/A (eval only)",
    "log_path": "/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s020_n51_100.json"
  },
  "conclusion": "success",
  "metrics": {
    "batch1_acc": 0.26,
    "batch1_correct": 13,
    "batch1_total": 50,
    "batch2_acc": 0.44,
    "batch2_correct": 22,
    "batch2_total": 50,
    "combined_acc": 0.35,
    "combined_correct": 35,
    "combined_total": 100
  },
  "completed_at": "2026-05-15T21:30:07.934Z"
}

================================================================================
EXPERIMENT: acc_qw_s020_n100_b2_fix
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T22:22:55.755Z",
  "updated_at": "2026-05-15T22:48:39.196Z",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s020 --num-problems 50 --start-index 50 --max-new-tokens 8192 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s020_b2_fix.json\"",
    "server": "westd-22162",
    "gpu": [
      "cuda:1"
    ],
    "pid": "283051",
    "log_path": "~/runs/phase-gated-compound-sparse/acc_qw_s020_n100_b2_fix.log",
    "submitted_at": "2026-05-15T22:25:18.472Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 1400.7,
    "gpu_hours": 0.39
  },
  "hypothesis": "重跑 QW s020 batch2 (problems 51-100) with max_new_tokens=8192，修复原 batch2 使用 2048 的不一致问题。",
  "parent": "acc_qw_s020_n100",
  "server": "westd-22162",
  "gpu": "cuda:1",
  "account": "root",
  "reproduce": {
    "server": "westd-22162",
    "gpu": "cuda:1",
    "started_at": "2026-05-15T22:25:15.841Z",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s020 --num-problems 50 --start-index 50 --max-new-tokens 8192 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s020_b2_fix.json\"",
    "code_commit": "1b4f61aa366a9fe320f8563c8f7acb5af58d78b7",
    "finished_at": "2026-05-15T22:40:53.877Z",
    "training_hours": 0.26
  },
  "pid": "283051",
  "log_path": "~/runs/phase-gated-compound-sparse/acc_qw_s020_n100_b2_fix.log",
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-15T22:40:57.414634+00:00"
      }
    ]
  },
  "conclusion": "success",
  "metrics": {
    "batch2_correct": 23,
    "batch2_total": 50,
    "batch2_acc": 0.46,
    "batch1_correct_v2": 13,
    "batch1_total": 50,
    "batch1_acc_v2": 0.26,
    "combined_correct": 36,
    "combined_total": 100,
    "combined_acc": 0.36,
    "null_count": 2,
    "truncated_count": 1,
    "total_time_seconds": 884.3,
    "max_new_tokens": 8192,
    "original_batch2_correct": 22,
    "original_batch2_acc": 0.44,
    "delta_vs_original": "+1 correct (+0.02 acc)"
  },
  "checkpoint_path": "N/A (eval only)",
  "completed_at": "2026-05-15T22:48:39.196Z"
}

================================================================================
EXPERIMENT: acc_qw_s025
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T20:49:29.416Z",
  "updated_at": "2026-05-15T21:17:24.568Z",
  "spec": {
    "command": "python run_accuracy_eval.py --model Qwen2.5-7B-Instruct --conditions importance_s025 --num-problems 50",
    "server": "westd-22162",
    "gpu": [
      "cuda:3"
    ],
    "pid": "274766",
    "log_path": "~/runs/phase-gated-compound-sparse/acc_qw_s025.log",
    "submitted_at": "2026-05-15T20:50:05.362Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/autodl-tmp/pacs/data/math500.json",
    "data_count": 50,
    "model_name": "Qwen2.5-7B-Instruct",
    "seed": 42,
    "type": "eval",
    "checkpoint_source": "checkpoints/Qwen2.5-7B-Instruct",
    "eval_data": "MATH-500 n=50",
    "wall_clock_seconds": 875.0,
    "gpu_hours": 0.24
  },
  "reproduce": {
    "finished_at": "2026-05-15T21:00:56.427Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-15T21:01:01.626822+00:00"
      }
    ]
  },
  "metrics": {
    "qw_s025_acc": 0.32,
    "qw_s025_correct": 16,
    "qw_s025_total": 50,
    "qw_s025_delta_vs_dense": 0,
    "null_count": 8,
    "null_rate": 0.16,
    "output_truncated_count": 2,
    "output_truncated_rate": 0.04,
    "extraction_failure_count": 6,
    "extraction_failure_rate": 0.12,
    "wrong_count": 26,
    "wrong_rate": 0.52,
    "heads_pruned": 196,
    "total_time_s": 559,
    "note": "v2 rescored with fixed radical+degree matcher; 3 problems flipped (sqrt+degree)"
  },
  "conclusion": "negative",
  "checkpoint_path": "/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s025.json",
  "completed_at": "2026-05-15T21:04:40.391Z"
}

================================================================================
EXPERIMENT: acc_qw_s025_n100
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T21:09:36.278Z",
  "updated_at": "2026-05-15T21:34:48.072Z",
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=3 python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s025 --num-problems 50 --start-index 50 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s025_n51_100.json",
    "server": "westd-22162",
    "data_path": "MATH-500",
    "data_count": 50,
    "model_name": "Qwen2.5-7B-Instruct",
    "seed": 42,
    "description": "QW importance_s025 accuracy eval problems 51-100",
    "checkpoint_source": "/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct",
    "eval_data": "MATH-500 problems 51-100",
    "checkpoint_path": "N/A (eval only)",
    "log_path": "/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s025_n51_100.json"
  },
  "conclusion": "success",
  "metrics": {
    "batch1_acc": 0.32,
    "batch1_correct": 16,
    "batch1_total": 50,
    "batch2_acc": 0.34,
    "batch2_correct": 17,
    "batch2_total": 50,
    "combined_acc": 0.33,
    "combined_correct": 33,
    "combined_total": 100
  },
  "completed_at": "2026-05-15T21:30:09.145Z"
}

================================================================================
EXPERIMENT: acc_qw_s025_n100_b2_fix
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T22:22:57.057Z",
  "updated_at": "2026-05-15T23:28:18.012Z",
  "spec": {
    "data_path": "MATH-500",
    "data_count": 50,
    "model_name": "Qwen2.5-7B-Instruct",
    "seed": 42,
    "description": "QW importance_s025 batch2 (problems 51-100) accuracy eval with max_new_tokens=8192, fixing original batch2 which used 2048",
    "checkpoint_source": "/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct",
    "eval_data": "MATH-500 problems 51-100",
    "checkpoint_path": "N/A (eval only)"
  },
  "hypothesis": "重跑 QW s025 batch2 (problems 51-100) with max_new_tokens=8192，修复原 batch2 使用 2048 的不一致问题。",
  "parent": "acc_qw_s025_n100",
  "server": "westd-22162",
  "gpu": "cuda:1",
  "account": "root",
  "reproduce": {
    "server": "westd-22162",
    "gpu": "cuda:1",
    "started_at": "2026-05-15T22:43:13.237Z",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s025 --num-problems 50 --start-index 50 --max-new-tokens 8192 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s025_b2_fix.json\"",
    "code_commit": "1b4f61aa366a9fe320f8563c8f7acb5af58d78b7",
    "finished_at": "2026-05-15T23:02:06.320Z",
    "training_hours": 0.31
  },
  "pid": "285337",
  "log_path": "/root/runs/phase-gated-compound-sparse/acc_qw_s025_n100_b2_fix.log",
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-15T23:02:09.471595+00:00"
      }
    ]
  },
  "metrics": {
    "accuracy": 0.34,
    "correct": 17,
    "n_problems": 50,
    "truncation_rate": 0.06,
    "truncated_count": 3,
    "avg_tokens": 1044,
    "max_new_tokens": 8192,
    "total_time_seconds": 1099,
    "batch": "b2 (problems 51-100)",
    "merged_n100_accuracy": 0.33,
    "merged_n100_correct": 33,
    "merged_n100_note": "batch1 used max_new_tokens=2048, batch2_fix used 8192 — mismatch"
  },
  "checkpoint_path": "/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s025_b2_fix.json",
  "conclusion": "success",
  "completed_at": "2026-05-15T23:28:18.012Z"
}

================================================================================
EXPERIMENT: acc_qw_s030_n100
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T21:34:40.948Z",
  "updated_at": "2026-05-15T22:21:11.181Z",
  "hypothesis": "补跑 QW importance_s030 problems 51-100，扩展到 n=100 以降低噪声",
  "spec": {
    "command": "python run_accuracy_eval.py --model checkpoints/Qwen2.5-7B-Instruct --conditions importance_s030 --num-problems 50 --start-index 50 --gpu cuda:0 --seed 42 --output-name accuracy_eval_qw_s030_n51_100.json",
    "server": "westd-22162",
    "gpu": [
      "cuda:3"
    ],
    "pid": "280094",
    "log_path": "~/runs/phase-gated-compound-sparse/acc_qw_s030_n100.log",
    "submitted_at": "2026-05-15T21:47:49.602Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "MATH problems 51-100",
    "data_count": 50,
    "model_name": "Qwen2.5-7B-Instruct",
    "seed": 42,
    "checkpoint_source": "checkpoints/Qwen2.5-7B-Instruct",
    "eval_data": "MATH problems 51-100",
    "wall_clock_seconds": 2001.6,
    "gpu_hours": 0.56
  },
  "conclusion": "success",
  "metrics": {
    "batch1_correct": 7,
    "batch1_total": 50,
    "batch1_acc": 0.14,
    "batch2_correct": 12,
    "batch2_total": 50,
    "batch2_acc": 0.24,
    "combined_correct": 19,
    "combined_total": 100,
    "combined_acc": 0.19
  },
  "checkpoint_path": "N/A (eval only)",
  "completed_at": "2026-05-15T22:21:11.181Z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e25d82d-31c1-4e4c-ba15-2744b33bd32a",
  "isSidechain": true,
  "promptId": "5d98afa4-bc8d-47c1-b014-8bbe0580361f",
  "agentId": "a3e0a592254fabea7",
  "type": "user",
  "uuid": "01e8b396-2126-4819-96a9-5bbf53108f1a",
  "sourceToolAssistantUUID": "5e25d82d-31c1-4e4c-ba15-2744b33bd32a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-16T00:27:11.813Z_

Here are all 9 `acc_qw_*` experiments extracted verbatim from the registry.

---

## Summary Table (9 experiments)

| exp_id | status | conclusion | combined_acc | combined_correct/total |
|--------|--------|-----------|-------------|----------------------|
| acc_qw_dense_n100 | DONE | success | 0.40 | 40/100 |
| acc_qw_s015_n100 | DONE | success | 0.36 | 36/100 |
| acc_qw_s020 | DONE | negative | 0.26 (n=50 only) | 13/50 |
| acc_qw_s020_n100 | DONE | success | 0.35 | 35/100 |
| acc_qw_s020_n100_b2_fix | DONE | success | 0.36 | 36/100 |
| acc_qw_s025 | DONE | negative | 0.32 (n=50 only) | 16/50 |
| acc_qw_s025_n100 | DONE | success | 0.33 | 33/100 |
| acc_qw_s025_n100_b2_fix | DONE | success | 0.33 | 33/100 |
| acc_qw_s030_n100 | DONE | success | 0.19 | 19/100 |

---

## Full Verbatim Details Per Experiment

### 1. acc_qw_dense_n100
- **status**: DONE
- **conclusion**: success
- **hypothesis**: "补跑 QW dense problems 51-100，扩展到 n=100 以降低噪声"
- **metrics**:
  - batch1_correct: 16, batch1_total: 50, batch1_acc: 0.32
  - batch2_correct: 24, batch2_total: 50, batch2_acc: 0.48
  - combined_correct: 40, combined_total: 100, combined_acc: **0.40**
- **spec**: model=Qwen2.5-7B-Instruct, conditions=dense, problems 51-100, seed=42, server=westd-22162, gpu=cuda:2, wall_clock_seconds=1176.6, gpu_hours=0.33
- **completed_at**: 2026-05-15T21:54:42.068Z

### 2. acc_qw_s015_n100
- **status**: DONE
- **conclusion**: success
- **metrics**:
  - batch1_acc: 0.34, batch1_correct: 17, batch1_total: 50
  - batch2_acc: 0.38, batch2_correct: 19, batch2_total: 50
  - combined_acc: **0.36**, combined_correct: 36, combined_total: 100
- **spec**: model=Qwen2.5-7B-Instruct, conditions=importance_s015, problems 51-100, seed=42, server=westd-22162, gpu=cuda:3
- **checkpoint_path**: N/A (eval only)
- **log_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s015_n51_100.json
- **completed_at**: 2026-05-15T21:47:46.664Z

### 3. acc_qw_s020 (batch 1 only, n=50)
- **status**: DONE
- **conclusion**: negative
- **metrics**:
  - qw_s020_acc: 0.26, qw_s020_correct: 13, qw_s020_total: 50
  - qw_s020_delta_vs_dense: -0.06
  - null_count: 2, null_rate: 0.04
  - output_truncated_count: 2, output_truncated_rate: 0.04
  - extraction_failure_count: 0, extraction_failure_rate: 0
  - wrong_count: 35, wrong_rate: 0.70
  - heads_pruned: 140
  - total_time_s: 598
  - note: "v2 rescored with fixed radical+degree matcher"
- **spec**: model=Qwen2.5-7B-Instruct, conditions=importance_s020, n=50, server=westd-22162, gpu=cuda:2, wall_clock_seconds=878.3, gpu_hours=0.24
- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s020.json
- **completed_at**: 2026-05-15T21:04:41.944Z

### 4. acc_qw_s020_n100
- **status**: DONE
- **conclusion**: success
- **metrics**:
  - batch1_acc: 0.26, batch1_correct: 13, batch1_total: 50
  - batch2_acc: 0.44, batch2_correct: 22, batch2_total: 50
  - combined_acc: **0.35**, combined_correct: 35, combined_total: 100
- **spec**: model=Qwen2.5-7B-Instruct, conditions=importance_s020, problems 51-100, seed=42, server=westd-22162
- **completed_at**: 2026-05-15T21:30:07.934Z

### 5. acc_qw_s020_n100_b2_fix
- **status**: DONE
- **conclusion**: success
- **hypothesis**: "重跑 QW s020 batch2 (problems 51-100) with max_new_tokens=8192，修复原 batch2 使用 2048 的不一致问题。"
- **parent**: acc_qw_s020_n100
- **metrics**:
  - batch2_correct: 23, batch2_total: 50, batch2_acc: 0.46
  - batch1_correct_v2: 13, batch1_total: 50, batch1_acc_v2: 0.26
  - combined_correct: 36, combined_total: 100, combined_acc: **0.36**
  - null_count: 2, truncated_count: 1
  - total_time_seconds: 884.3
  - max_new_tokens: 8192
  - original_batch2_correct: 22, original_batch2_acc: 0.44
  - delta_vs_original: "+1 correct (+0.02 acc)"
- **reproduce**: code_commit=1b4f61aa366a9fe320f8563c8f7acb5af58d78b7, finished_at=2026-05-15T22:40:53.877Z, training_hours=0.26
- **spec**: server=westd-22162, gpu=cuda:1, wall_clock_seconds=1400.7, gpu_hours=0.39
- **completed_at**: 2026-05-15T22:48:39.196Z

### 6. acc_qw_s025 (batch 1 only, n=50)
- **status**: DONE
- **conclusion**: negative
- **metrics**:
  - qw_s025_acc: 0.32, qw_s025_correct: 16, qw_s025_total: 50
  - qw_s025_delta_vs_dense: 0
  - null_count: 8, null_rate: 0.16
  - output_truncated_count: 2, output_truncated_rate: 0.04
  - extraction_failure_count: 6, extraction_failure_rate: 0.12
  - wrong_count: 26, wrong_rate: 0.52
  - heads_pruned: 196
  - total_time_s: 559
  - note: "v2 rescored with fixed radical+degree matcher; 3 problems flipped (sqrt+degree)"
- **spec**: model=Qwen2.5-7B-Instruct, conditions=importance_s025, n=50, server=westd-22162, gpu=cuda:3, wall_clock_seconds=875.0, gpu_hours=0.24
- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s025.json
- **completed_at**: 2026-05-15T21:04:40.391Z

### 7. acc_qw_s025_n100
- **status**: DONE
- **conclusion**: success
- **metrics**:
  - batch1_acc: 0.32, batch1_correct: 16, batch1_total: 50
  - batch2_acc: 0.34, batch2_correct: 17, batch2_total: 50
  - combined_acc: **0.33**, combined_correct: 33, combined_total: 100
- **spec**: model=Qwen2.5-7B-Instruct, conditions=importance_s025, problems 51-100, seed=42, server=westd-22162
- **completed_at**: 2026-05-15T21:30:09.145Z

### 8. acc_qw_s025_n100_b2_fix
- **status**: DONE
- **conclusion**: success
- **hypothesis**: "重跑 QW s025 batch2 (problems 51-100) with max_new_tokens=8192，修复原 batch2 使用 2048 的不一致问题。"
- **parent**: acc_qw_s025_n100
- **metrics**:
  - accuracy: 0.34, correct: 17, n_problems: 50
  - truncation_rate: 0.06, truncated_count: 3
  - avg_tokens: 1044
  - max_new_tokens: 8192
  - total_time_seconds: 1099
  - batch: "b2 (problems 51-100)"
  - merged_n100_accuracy: **0.33**, merged_n100_correct: 33
  - merged_n100_note: "batch1 used max_new_tokens=2048, batch2_fix used 8192 — mismatch"
- **reproduce**: code_commit=1b4f61aa366a9fe320f8563c8f7acb5af58d78b7, finished_at=2026-05-15T23:02:06.320Z, training_hours=0.31
- **checkpoint_path**: /root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s025_b2_fix.json
- **completed_at**: 2026-05-15T23:28:18.012Z

### 9. acc_qw_s030_n100
- **status**: DONE
- **conclusion**: success
- **hypothesis**: "补跑 QW importance_s030 problems 51-100，扩展到 n=100 以降低噪声"
- **metrics**:
  - batch1_correct: 7, batch1_total: 50, batch1_acc: 0.14
  - batch2_correct: 12, batch2_total: 50, batch2_acc: 0.24
  - combined_correct: 19, combined_total: 100, combined_acc: **0.19**
- **spec**: model=Qwen2.5-7B-Instruct, conditions=importance_s030, problems 51-100, seed=42, server=westd-22162, gpu=cuda:3, wall_clock_seconds=2001.6, gpu_hours=0.56
- **completed_at**: 2026-05-15T22:21:11.181Z

---

## QW Dose Curve (best n=100 estimates, using b2_fix where available)

| Sparsity | combined_acc (n=100) | Correct/100 | Delta vs Dense |
|----------|---------------------|-------------|----------------|
| dense    | 0.40                | 40          | --             |
| s015     | 0.36                | 36          | -0.04          |
| s020     | 0.36 (b2_fix)       | 36          | -0.04          |
| s025     | 0.33 (b2_fix=same)  | 33          | -0.07          |
| s030     | 0.19                | 19          | -0.21          |

Key observation: s025->s030 shows a steep accuracy cliff (0.33 -> 0.19, a 14-point drop), while s015 and s020 are close to dense. The b2_fix variants (max_new_tokens=8192) had minimal impact on s020 (+1 correct) and zero impact on s025 (still 33 correct). Note the b2_fix experiments flag a mismatch: batch1 used max_new_tokens=2048 while batch2_fix used 8192.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01e8b396-2126-4819-96a9-5bbf53108f1a",
  "isSidechain": true,
  "agentId": "a3e0a592254fabea7",
  "requestId": "req_011Cb5JHSoiCPP8ttg8LBVze",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f45c7f2-c288-400a-8662-ce15b83de943",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "38576691-e177-4a18-ab23-be69eff4b7ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CwW3bQV6huZYaTunb2HYU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6947,
      "cache_read_input_tokens": 16116,
      "output_tokens": 3261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6947
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3261,
          "cache_read_input_tokens": 16116,
          "cache_creation_input_tokens": 6947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6947,
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
