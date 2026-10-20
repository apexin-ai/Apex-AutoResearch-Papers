# Research conversation: I need to extract specific experiment metrics from a JSON registry file to audit numbers in a paper. The file is at: /ho

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a44e38f07bb86c0e3.jsonl`
- **Structured JSON:** [`872bb59de28be9da98ed.json`](../../sessions/87/872bb59de28be9da98ed.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-25T19:45:27.476Z_

I need to extract specific experiment metrics from a JSON registry file to audit numbers in a paper. The file is at:
/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/c2f03400-f630-4847-9da7-a2b649715a9a/tool-results/mcp-agent-ml-research-read_registry-1779738315214.txt

The file format is JSON with schema: {result: string} — the "result" field is itself a JSON string that needs to be parsed. Inside you'll find experiments keyed by experiment_id.

Please extract the metrics for these specific experiments (use jq or python to parse). For each, I need the pairwise_auc values (0v1, 1v2, 2v3, 3v4, 4v5), k_star, and any bootstrap_ci, MAE, ordinal accuracy, or other notable metrics:

1. mvp_pilot_sat_v1 (Qwen-1.5B rewrite)
2. exp_004_7b_crossscale (Qwen-7B)
3. exp_018_llama8b_depth (LLaMA-8B)
4. exp_019_mistral7b_depth (Mistral-7B)
5. exp_003_decoding_ablation
6. exp_020_pythia_decoding
7. exp_016_base_vs_instruct
8. exp_013_cross_transfer
9. exp_012_binary_confidence
10. exp_011_llm_zeroshot
11. exp_007_bootstrap_ci
12. exp_006_graduated_filtering
13. exp_008_retrain_chain_v2
14. exp_022_cross_scorer_matrix
15. exp_023_domain_ablation (wiki)
16. exp_024_arxiv_domain
17. exp_027_latex_ablation
18. exp_021_length_ablation
19. exp_028_power_curve

Also search for any experiments with "qwen" and "rewrite" in their name that might be the rewrite experiment.

Report ALL metrics you find for each experiment verbatim (don't summarize or truncate). If an experiment doesn't exist, say so.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "79672ee0-6083-486d-a275-3f445c8e7cd7",
  "agentId": "a44e38f07bb86c0e3",
  "type": "user",
  "uuid": "54a3e391-5721-43a3-8fb8-ba6e12072bbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T19:45:27.483Z_

```json
{
  "parentUuid": "54a3e391-5721-43a3-8fb8-ba6e12072bbd",
  "isSidechain": true,
  "agentId": "a44e38f07bb86c0e3",
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
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
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
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "66167a5e-0142-4bcb-a3bf-4b509fa54642",
  "timestamp": "2026-05-25T19:45:27.483Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-25T19:45:30.106Z_



I'll read the file first, then parse the JSON to extract all requested experiment metrics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66167a5e-0142-4bcb-a3bf-4b509fa54642",
  "isSidechain": true,
  "agentId": "a44e38f07bb86c0e3",
  "requestId": "req_011CbPrw8ErkSwvnGub19Rn7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a0dbb0b-f49d-4caa-961d-2b59f6dcec32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6qroZTiqaHFj487U7b6pJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7208,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7208,
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

_source line 4 · 2026-05-25T19:45:31.027Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QB3DQpbUf1LVFQnYa9Li8C`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/c2f03400-f630-4847-9da7-a2b649715a9a/tool-results/mcp-agent-ml-research-read_registry-1779738315214.txt",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a0dbb0b-f49d-4caa-961d-2b59f6dcec32",
  "isSidechain": true,
  "agentId": "a44e38f07bb86c0e3",
  "requestId": "req_011CbPrw8ErkSwvnGub19Rn7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40c01db6-ab84-49a8-9c3b-2278942e084a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6qroZTiqaHFj487U7b6pJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7208,
      "cache_read_input_tokens": 8250,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7208
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 179,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 7208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7208,
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

_source line 5 · 2026-05-25T19:45:31.396Z_

<details><summary>↩ Tool result · reported error · `toolu_01QB3DQpbUf1LVFQnYa9Li8C`</summary>

```text
File content (42587 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40c01db6-ab84-49a8-9c3b-2278942e084a",
  "isSidechain": true,
  "promptId": "79672ee0-6083-486d-a275-3f445c8e7cd7",
  "agentId": "a44e38f07bb86c0e3",
  "type": "user",
  "uuid": "4bde1d66-f98e-48f4-826a-563440a64e63",
  "toolUseResult": "Error: File content (42587 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "40c01db6-ab84-49a8-9c3b-2278942e084a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-25T19:45:34.359Z_

The file is large. Let me use Python to parse it properly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bde1d66-f98e-48f4-826a-563440a64e63",
  "isSidechain": true,
  "agentId": "a44e38f07bb86c0e3",
  "requestId": "req_011CbPrwQsE81F88f7Na12xG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a427638-0ec1-4ca4-bac4-e6ceaffc631e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3dBaUCdfAEhSZ3xxbp6Ud",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1081,
      "cache_read_input_tokens": 15458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1081,
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

_source line 7 · 2026-05-25T19:45:35.986Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rt7nz11TdEzTqvMkrijNQg`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/c2f03400-f630-4847-9da7-a2b649715a9a/tool-results/mcp-agent-ml-research-read_registry-1779738315214.txt",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a427638-0ec1-4ca4-bac4-e6ceaffc631e",
  "isSidechain": true,
  "agentId": "a44e38f07bb86c0e3",
  "requestId": "req_011CbPrwQsE81F88f7Na12xG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af513868-b5c2-4333-9959-aea52b89b486",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3dBaUCdfAEhSZ3xxbp6Ud",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1081,
      "cache_read_input_tokens": 15458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1081,
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

_source line 8 · 2026-05-25T19:45:36.251Z_

<details><summary>↩ Tool result · reported error · `toolu_01Rt7nz11TdEzTqvMkrijNQg`</summary>

```text
File content (42587 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af513868-b5c2-4333-9959-aea52b89b486",
  "isSidechain": true,
  "promptId": "79672ee0-6083-486d-a275-3f445c8e7cd7",
  "agentId": "a44e38f07bb86c0e3",
  "type": "user",
  "uuid": "df4980df-61b0-4e1e-b3fe-06864c9f2de1",
  "toolUseResult": "Error: File content (42587 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "af513868-b5c2-4333-9959-aea52b89b486",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T19:45:39.652Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UzqC3RqXh5AfNhmhHdVBhH`</summary>

```json
{
  "command": "wc -l \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/c2f03400-f630-4847-9da7-a2b649715a9a/tool-results/mcp-agent-ml-research-read_registry-1779738315214.txt\"",
  "description": "Count lines in the registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df4980df-61b0-4e1e-b3fe-06864c9f2de1",
  "isSidechain": true,
  "agentId": "a44e38f07bb86c0e3",
  "requestId": "req_011CbPrwmcejQdUTsh5HT6YH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "946dc810-1fbb-42a3-b080-c0d9a12aa5c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3PrQYDGw5W3ihmdTKR3E1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 16539,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 235
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 16539,
          "cache_creation_input_tokens": 235,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 235,
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

_source line 10 · 2026-05-25T19:45:39.801Z_

<details><summary>↩ Tool result · `toolu_01UzqC3RqXh5AfNhmhHdVBhH`</summary>

```text
0 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/c2f03400-f630-4847-9da7-a2b649715a9a/tool-results/mcp-agent-ml-research-read_registry-1779738315214.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "946dc810-1fbb-42a3-b080-c0d9a12aa5c1",
  "isSidechain": true,
  "promptId": "79672ee0-6083-486d-a275-3f445c8e7cd7",
  "agentId": "a44e38f07bb86c0e3",
  "type": "user",
  "uuid": "d7af8e17-67a8-4246-b254-4eed9e642ed3",
  "sourceToolAssistantUUID": "946dc810-1fbb-42a3-b080-c0d9a12aa5c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-25T19:45:42.768Z_

Single-line JSON. Let me use Python to parse it and extract all requested experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7af8e17-67a8-4246-b254-4eed9e642ed3",
  "isSidechain": true,
  "agentId": "a44e38f07bb86c0e3",
  "requestId": "req_011CbPrx2nDhESF3p1jrQKje",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15226585-90f6-4154-a84b-65a9ac65389d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012nm47bbBpfrjXjctajR4zU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 16774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 272,
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

_source line 12 · 2026-05-25T19:45:46.638Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016CgdyL9WPirs9ym2hkpLmJ`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, sys\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/c2f03400-f630-4847-9da7-a2b649715a9a/tool-results/mcp-agent-ml-research-read_registry-1779738315214.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\n# The \"result\" field is itself a JSON string\ninner = json.loads(raw[\"result\"])\n\n# Print all top-level keys to understand the structure\nprint(\"=== TOP-LEVEL KEYS ===\")\nfor k in sorted(inner.keys()):\n    print(f\"  {k}\")\nprint(f\"\\nTotal keys: {len(inner.keys())}\")\nPYEOF",
  "description": "Parse the JSON file and list all top-level keys",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15226585-90f6-4154-a84b-65a9ac65389d",
  "isSidechain": true,
  "agentId": "a44e38f07bb86c0e3",
  "requestId": "req_011CbPrx2nDhESF3p1jrQKje",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b211f81-733f-400e-ad7e-580930a78b49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012nm47bbBpfrjXjctajR4zU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 16774,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 272
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 340,
          "cache_read_input_tokens": 16774,
          "cache_creation_input_tokens": 272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 272,
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

_source line 13 · 2026-05-25T19:45:46.742Z_

<details><summary>↩ Tool result · `toolu_016CgdyL9WPirs9ym2hkpLmJ`</summary>

```text
=== TOP-LEVEL KEYS ===
  data
  error
  metadata
  success

Total keys: 4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b211f81-733f-400e-ad7e-580930a78b49",
  "isSidechain": true,
  "promptId": "79672ee0-6083-486d-a275-3f445c8e7cd7",
  "agentId": "a44e38f07bb86c0e3",
  "type": "user",
  "uuid": "5a4d856b-e77f-4328-955d-62f653af8f2d",
  "sourceToolAssistantUUID": "3b211f81-733f-400e-ad7e-580930a78b49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T19:45:54.302Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MfAJvCquVxYzzDzXutTTkV`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/c2f03400-f630-4847-9da7-a2b649715a9a/tool-results/mcp-agent-ml-research-read_registry-1779738315214.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw[\"result\"])\ndata = inner[\"data\"]\n\nprint(\"=== DATA STRUCTURE ===\")\nprint(f\"Type: {type(data)}\")\nif isinstance(data, dict):\n    print(f\"Keys: {sorted(data.keys())}\")\n    # Show first key's structure\n    first_key = list(data.keys())[0]\n    print(f\"\\nFirst key '{first_key}' type: {type(data[first_key])}\")\n    if isinstance(data[first_key], dict):\n        print(f\"Sub-keys: {sorted(data[first_key].keys())[:20]}\")\nelif isinstance(data, list):\n    print(f\"Length: {len(data)}\")\n    if len(data) > 0:\n        print(f\"First element type: {type(data[0])}\")\n        if isinstance(data[0], dict):\n            print(f\"First element keys: {sorted(data[0].keys())}\")\nPYEOF",
  "description": "Explore data structure within the registry",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a4d856b-e77f-4328-955d-62f653af8f2d",
  "isSidechain": true,
  "agentId": "a44e38f07bb86c0e3",
  "requestId": "req_011CbPrxYfZZ5V2nA8Afiamn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27ba1dd6-3d8b-4ae7-b951-878b54843b91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcJ5MDCForQEga3sktVQeJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 379,
      "cache_read_input_tokens": 17046,
      "output_tokens": 464,
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
          "output_tokens": 464,
          "cache_read_input_tokens": 17046,
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

_source line 15 · 2026-05-25T19:45:54.386Z_

<details><summary>↩ Tool result · `toolu_01MfAJvCquVxYzzDzXutTTkV`</summary>

```text
=== DATA STRUCTURE ===
Type: &lt;class 'dict'>
Keys: ['baseline', 'count', 'experiments', 'total']

First key 'experiments' type: &lt;class 'dict'>
Sub-keys: ['7b-cross-transfer', 'arxiv_multi_source', 'code_domain_mistral', 'code_domain_olmo', 'code_domain_qwen7b', 'deberta_filter_deberta_binary', 'deberta_filter_deberta_graduated', 'deberta_filter_no_filter', 'deberta_filter_obd_binary', 'deberta_filtering_predict', 'exp-008-retrain-chain', 'exp-014', 'exp_001_pythia_depth', 'exp_002_olmo_depth', 'exp_003_decoding_ablation', 'exp_004_7b_crossscale', 'exp_005_degradation', 'exp_006_graduated_filtering', 'exp_007_bootstrap_ci', 'exp_008_retrain_chain']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27ba1dd6-3d8b-4ae7-b951-878b54843b91",
  "isSidechain": true,
  "promptId": "79672ee0-6083-486d-a275-3f445c8e7cd7",
  "agentId": "a44e38f07bb86c0e3",
  "type": "user",
  "uuid": "979d17c1-1767-4eee-88f7-4c524dcf669e",
  "sourceToolAssistantUUID": "27ba1dd6-3d8b-4ae7-b951-878b54843b91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T19:45:58.584Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TDUYH8DiHmTXzAh5tDxvdd`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/c2f03400-f630-4847-9da7-a2b649715a9a/tool-results/mcp-agent-ml-research-read_registry-1779738315214.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw[\"result\"])\nexperiments = inner[\"data\"][\"experiments\"]\n\n# List ALL experiment keys\nprint(\"=== ALL EXPERIMENT KEYS ===\")\nfor k in sorted(experiments.keys()):\n    print(f\"  {k}\")\nprint(f\"\\nTotal experiments: {len(experiments)}\")\nPYEOF",
  "description": "List all experiment keys in the registry",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "979d17c1-1767-4eee-88f7-4c524dcf669e",
  "isSidechain": true,
  "agentId": "a44e38f07bb86c0e3",
  "requestId": "req_011CbPry7ABAbECE71DwspXe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d092bd23-5de3-46b0-9efe-3c2db29b8b00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWYGNKXrUDGXYACsPpoNVf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 17425,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 735
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 17425,
          "cache_creation_input_tokens": 735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 735,
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

_source line 17 · 2026-05-25T19:45:58.679Z_

<details><summary>↩ Tool result · `toolu_01TDUYH8DiHmTXzAh5tDxvdd`</summary>

```text
=== ALL EXPERIMENT KEYS ===
  7b-cross-transfer
  arxiv_multi_source
  code_domain_mistral
  code_domain_olmo
  code_domain_qwen7b
  deberta_filter_deberta_binary
  deberta_filter_deberta_graduated
  deberta_filter_no_filter
  deberta_filter_obd_binary
  deberta_filtering_predict
  exp-008-retrain-chain
  exp-014
  exp_001_pythia_depth
  exp_002_olmo_depth
  exp_003_decoding_ablation
  exp_004_7b_crossscale
  exp_005_degradation
  exp_006_graduated_filtering
  exp_007_bootstrap_ci
  exp_008_retrain_chain
  exp_008_retrain_chain_v2
  exp_009_dose_10pct
  exp_009_dose_10pct_v2
  exp_009_dose_10pct_v3
  exp_009_dose_30pct
  exp_009_dose_30pct_v2
  exp_009_dose_30pct_v3
  exp_009_dose_50pct
  exp_009_dose_50pct_v2
  exp_009_dose_50pct_v3
  exp_009_dose_response
  exp_010_ordinal_baseline
  exp_011_llm_zeroshot
  exp_012_binary_confidence
  exp_013_cross_transfer
  exp_014_independent_metrics
  exp_014_naturalistic
  exp_014_naturalistic_v2
  exp_015_neural_probe
  exp_016_base_vs_instruct
  exp_017_qwen_continuation
  exp_018_llama8b_depth
  exp_019_mistral7b_depth
  exp_019b_mistral_cross_scorer
  exp_020_pythia_decoding
  exp_021_length_ablation
  exp_022_cross_scorer_matrix
  exp_023_domain_ablation
  exp_024_arxiv_domain
  exp_025_pythia_arxiv
  exp_025_pythia_filtering
  exp_026_arxiv_filtering
  exp_026_feature_stability
  exp_026_feature_stability_v2
  exp_027
  exp_027_latex_ablation
  exp_027_retrain_bootstrap
  exp_028_power_curve
  exp_028_subsampling_power
  exp_14b_c4
  exp_32b_c4
  exp_32b_c4_6class
  exp_7b_scorer_ablation
  exp_7b_scorer_arxiv
  exp_A_alt_scorer
  exp_B_14d_ablation
  exp_C_permutation_10k
  exp_D_obd_n500
  exp_E_paired_stats
  exp_arXiv_llama8b
  exp_arXiv_llama8b_crossscorer
  exp_arXiv_mistral7b
  exp_arXiv_mistral7b_crossscorer
  exp_arXiv_olmo
  exp_arXiv_qwen1b5_crossscorer
  exp_arXiv_qwen7b
  exp_arXiv_qwen7b_crossscorer
  exp_bootstrap_10k
  exp_changepoint_kstar
  exp_code_llama8b
  exp_code_mistral7b
  exp_code_multi_source
  exp_code_pythia1b4
  exp_code_qwen1b5
  exp_code_qwen1b5_pythia_scorer
  exp_code_qwen7b
  exp_contamination_rate_sweep
  exp_cross_transfer_llama8b_to_qwen7b
  exp_cross_transfer_llama8b_to_qwen7b_v2
  exp_cross_transfer_qwen7b_to_llama8b
  exp_deberta_arxiv_qwen1b5
  exp_deberta_c4
  exp_deberta_c4_1b5
  exp_deberta_c4_1b5_pythia
  exp_deberta_c4_1b5_qwen_cont
  exp_deberta_code_qwen1b5
  exp_deberta_cross_transfer_gpu1
  exp_deberta_cross_transfer_gpu2
  exp_deberta_cross_transfer_gpu3
  exp_deberta_cross_transfer_wiki
  exp_deberta_filtering_comparison
  exp_deberta_upperbound
  exp_expanded_downstream_eval
  exp_gemma27b_c4
  exp_gemma2b_10k
  exp_gemma2b_depth
  exp_kstar_theta
  exp_llama8b_10k
  exp_multi_source_arxiv
  exp_multi_source_detection
  exp_olmo1b_10k
  exp_olmo1b_c4_rerun
  exp_olmo_retrain_chain
  exp_olmo_retrain_v2
  exp_olmo_retrain_v3
  exp_pythia14b_10k
  exp_pythia14b_c4_10k
  exp_pythia14b_c4_rerun
  exp_pythia69b_c4_depth_chain
  exp_pythia69b_c4_depth_chain_v2
  exp_pythia69b_c4_depth_chain_v3
  exp_pythia69b_c4_nuc
  exp_pythia_retrain_depth7
  exp_qwen_cont_10k
  exp_qwen_retrain_chain
  exp_qwen_retrain_depth7
  exp_wiki_llama8b
  exp_wiki_mistral7b
  exp_wiki_multi_source
  exp_wiki_olmo
  exp_wiki_olmo_v2
  exp_wiki_pythia
  exp_wiki_pythia_v2
  exp_wiki_qwen7b
  exp_wiki_scorer_confound
  exp_wiki_scorer_confound_1b5
  gemma27b_cross_transfer
  gemma27b_filtering
  gsm8k-serial-rerun
  gsm8k_patch_bo_s0
  gsm8k_patch_grad_s0
  gsm8k_patch_nf_s0
  mvp_pilot_sat_v1
  olmo_arxiv_cross_scorer
  olmo_c4_cross_scorer
  runtime_benchmark
  seed2_binary_ours
  seed2_graduated
  seed2_no_filter
  seed_gemma27b_c4_s42
  seed_pythia14b_wiki_s123
  seed_qwen15b_c4_s123
  seed_qwen15b_wiki_s123
  sweep_eval_r10_bin
  sweep_eval_r10_binary
  sweep_eval_r10_grad
  sweep_eval_r10_graduated
  sweep_eval_r10_nf
  sweep_eval_r10_nf_v2
  sweep_eval_r10_nofilter
  sweep_eval_r30_nf
  sweep_eval_r30_nofilter
  sweep_r100_binary
  sweep_r100_graduated
  sweep_r100_nf
  sweep_r10_binary
  sweep_r10_graduated
  sweep_r10_nofilter
  sweep_r30_binary
  sweep_r30_graduated
  sweep_r30_nofilter
  sweep_r50_binary
  sweep_r50_graduated
  sweep_r50_nf
  wiki_domain_llama
  wiki_domain_mistral

Total experiments: 176
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d092bd23-5de3-46b0-9efe-3c2db29b8b00",
  "isSidechain": true,
  "promptId": "79672ee0-6083-486d-a275-3f445c8e7cd7",
  "agentId": "a44e38f07bb86c0e3",
  "type": "user",
  "uuid": "bb367b55-a730-4af9-9ce1-4eaeadaccc35",
  "sourceToolAssistantUUID": "d092bd23-5de3-46b0-9efe-3c2db29b8b00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-25T19:46:02.531Z_

Now let me extract the full metrics for all requested experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb367b55-a730-4af9-9ce1-4eaeadaccc35",
  "isSidechain": true,
  "agentId": "a44e38f07bb86c0e3",
  "requestId": "req_011CbPryRZCwbdiYYFUFEeHx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "615ba401-a1a6-4557-a99f-0d9351d6b212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019uDur2e59F72uUvwihUGGZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2265,
      "cache_read_input_tokens": 18160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2265,
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

_source line 19 · 2026-05-25T19:46:13.079Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01V8Gh156zaZ5nicBhmvNipL`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/c2f03400-f630-4847-9da7-a2b649715a9a/tool-results/mcp-agent-ml-research-read_registry-1779738315214.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw[\"result\"])\nexperiments = inner[\"data\"][\"experiments\"]\n\ntarget_keys = [\n    \"mvp_pilot_sat_v1\",\n    \"exp_004_7b_crossscale\",\n    \"exp_018_llama8b_depth\",\n    \"exp_019_mistral7b_depth\",\n    \"exp_003_decoding_ablation\",\n    \"exp_020_pythia_decoding\",\n    \"exp_016_base_vs_instruct\",\n    \"exp_013_cross_transfer\",\n    \"exp_012_binary_confidence\",\n    \"exp_011_llm_zeroshot\",\n    \"exp_007_bootstrap_ci\",\n    \"exp_006_graduated_filtering\",\n    \"exp_008_retrain_chain_v2\",\n    \"exp_022_cross_scorer_matrix\",\n    \"exp_023_domain_ablation\",\n    \"exp_024_arxiv_domain\",\n    \"exp_027_latex_ablation\",\n    \"exp_021_length_ablation\",\n    \"exp_028_power_curve\",\n]\n\nfor key in target_keys:\n    print(f\"\\n{'='*80}\")\n    print(f\"EXPERIMENT: {key}\")\n    print(f\"{'='*80}\")\n    if key in experiments:\n        print(json.dumps(experiments[key], indent=2))\n    else:\n        print(\"*** NOT FOUND ***\")\n\nPYEOF",
  "description": "Extract metrics for all 19 requested experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "615ba401-a1a6-4557-a99f-0d9351d6b212",
  "isSidechain": true,
  "agentId": "a44e38f07bb86c0e3",
  "requestId": "req_011CbPryRZCwbdiYYFUFEeHx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd43cda3-29be-469c-90dc-80f3ddcd753f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019uDur2e59F72uUvwihUGGZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2265,
      "cache_read_input_tokens": 18160,
      "output_tokens": 591,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2265
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 591,
          "cache_read_input_tokens": 18160,
          "cache_creation_input_tokens": 2265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2265,
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

_source line 20 · 2026-05-25T19:46:13.166Z_

<details><summary>↩ Tool result · `toolu_01V8Gh156zaZ5nicBhmvNipL`</summary>

```text
================================================================================
EXPERIMENT: mvp_pilot_sat_v1
================================================================================
{
  "metrics": {
    "pairwise_auc": {
      "0v1": 0.9956,
      "1v2": 0.6957,
      "2v3": 0.5893,
      "3v4": 0.5434,
      "4v5": 0.5343
    },
    "pairwise_auc_std": {
      "0v1": 0.0005,
      "1v2": 0.0072,
      "2v3": 0.012,
      "3v4": 0.0053,
      "4v5": 0.0091
    },
    "pairwise_jsd": {
      "0v1": 0.2669,
      "1v2": 0.0163,
      "2v3": 0.0069,
      "3v4": 0.0047,
      "4v5": 0.0041
    },
    "k_star": 2,
    "ordinal_mae": 1.0163,
    "ordinal_accuracy": 0.4182
  }
}

================================================================================
EXPERIMENT: exp_004_7b_crossscale
================================================================================
{
  "metrics": {
    "k_star": 2,
    "pairwise_auc": {
      "0v1": 0.9644,
      "1v2": 0.6178,
      "2v3": 0.546,
      "3v4": 0.5225,
      "4v5": 0.5091
    },
    "pairwise_auc_std": {
      "0v1": 0.0034,
      "1v2": 0.0081,
      "2v3": 0.0028,
      "3v4": 0.0113,
      "4v5": 0.0052
    },
    "bootstrap_ci": {
      "0v1": {
        "auc": 0.9638,
        "ci_lower": 0.9607,
        "ci_upper": 0.9665,
        "perm_p": 0.0001
      },
      "1v2": {
        "auc": 0.6168,
        "ci_lower": 0.6079,
        "ci_upper": 0.6261,
        "perm_p": 0.0001
      },
      "2v3": {
        "auc": 0.5492,
        "ci_lower": 0.5388,
        "ci_upper": 0.5594,
        "perm_p": 0.0001
      },
      "3v4": {
        "auc": 0.5276,
        "ci_lower": 0.517,
        "ci_upper": 0.5375,
        "perm_p": 0.0001
      },
      "4v5": {
        "auc": 0.5085,
        "ci_lower": 0.4988,
        "ci_upper": 0.5191,
        "perm_p": 0.0676
      }
    },
    "bootstrap_resamples": 1000,
    "permutation_resamples": 10000,
    "pairwise_jsd": {
      "0v1": 0.127422,
      "1v2": 0.010114,
      "2v3": 0.004798,
      "3v4": 0.004821,
      "4v5": 0.003335
    },
    "ordinal_mae": 1.2156,
    "ordinal_accuracy": 0.3523,
    "top_features": [
      "freq_entropy",
      "surp_d1_skew",
      "surp_std",
      "surp_d1_mean",
      "surp_mean"
    ],
    "key_finding": "K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60 (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676). FR-4 Warning resolved."
  }
}

================================================================================
EXPERIMENT: exp_018_llama8b_depth
================================================================================
{
  "metrics": {
    "k_star": 2,
    "pairwise_auc": {
      "0v1": 0.9225,
      "1v2": 0.6123,
      "2v3": 0.5274,
      "3v4": 0.5138,
      "4v5": 0.5097
    },
    "jsd": {
      "0v1": 0.077,
      "1v2": 0.012,
      "2v3": 0.005
    },
    "bootstrap_ci": {
      "0v1": {
        "auc": 0.9224,
        "ci_lower": 0.9174,
        "ci_upper": 0.9272,
        "perm_p": 0.0001
      },
      "1v2": {
        "auc": 0.6123,
        "ci_lower": 0.6028,
        "ci_upper": 0.6216,
        "perm_p": 0.0001
      },
      "2v3": {
        "auc": 0.5273,
        "ci_lower": 0.5169,
        "ci_upper": 0.5378,
        "perm_p": 0.0001
      },
      "3v4": {
        "auc": 0.5168,
        "ci_lower": 0.5062,
        "ci_upper": 0.5275,
        "perm_p": 0.0037
      },
      "4v5": {
        "auc": 0.5159,
        "ci_lower": 0.5052,
        "ci_upper": 0.5268,
        "perm_p": 0.0035
      }
    },
    "bootstrap_resamples": 10000,
    "permutation_resamples": 10000
  }
}

================================================================================
EXPERIMENT: exp_019_mistral7b_depth
================================================================================
{
  "metrics": {
    "k_star": 1,
    "pairwise_auc": {
      "0v1": 0.9843,
      "1v2": 0.5935,
      "2v3": 0.5402,
      "3v4": 0.5232,
      "4v5": 0.5181
    },
    "bootstrap_ci_1v2": {
      "ci_lower": 0.5835,
      "ci_upper": 0.6032,
      "p_auc_leq_060": 0.9017
    },
    "jsd": {
      "0v1": 0.124194,
      "1v2": 0.008051,
      "2v3": 0.005047,
      "3v4": 0.004516,
      "4v5": 0.004109
    },
    "ordinal_mae": 1.2275,
    "ordinal_accuracy": 0.3567,
    "top3_features": [
      "freq_entropy",
      "surp_d1_skew",
      "surp_d1_mean"
    ]
  }
}

================================================================================
EXPERIMENT: exp_003_decoding_ablation
================================================================================
{
  "metrics": {
    "K_star": 2,
    "K_star_robust": true,
    "bootstrap_ci": {
      "config1_greedy": {
        "0v1": {
          "auc": 0.9796,
          "ci": [
            0.9772,
            0.982
          ],
          "perm_p": 0
        },
        "1v2": {
          "auc": 0.6892,
          "ci": [
            0.6802,
            0.6982
          ],
          "perm_p": 0
        },
        "2v3": {
          "auc": 0.5612,
          "ci": [
            0.5517,
            0.5705
          ],
          "perm_p": 0
        },
        "3v4": {
          "auc": 0.5405,
          "ci": [
            0.5308,
            0.5502
          ],
          "perm_p": 0
        },
        "4v5": {
          "auc": 0.5137,
          "ci": [
            0.5033,
            0.5238
          ],
          "perm_p": 0.0082
        }
      },
      "config2_nuc09": {
        "0v1": {
          "auc": 0.9945,
          "ci": [
            0.9934,
            0.9956
          ],
          "perm_p": 0
        },
        "1v2": {
          "auc": 0.6862,
          "ci": [
            0.6774,
            0.6951
          ],
          "perm_p": 0
        },
        "2v3": {
          "auc": 0.5917,
          "ci": [
            0.5824,
            0.601
          ],
          "perm_p": 0,
          "note": "CI upper crosses theta=0.60"
        },
        "3v4": {
          "auc": 0.5468,
          "ci": [
            0.5369,
            0.5568
          ],
          "perm_p": 0
        },
        "4v5": {
          "auc": 0.5066,
          "ci": [
            0.4959,
            0.5173
          ],
          "perm_p": 0.1199
        }
      },
      "config3_t07": {
        "0v1": {
          "auc": 0.9877,
          "ci": [
            0.9857,
            0.9896
          ],
          "perm_p": 0
        },
        "1v2": {
          "auc": 0.6885,
          "ci": [
            0.6797,
            0.697
          ],
          "perm_p": 0
        },
        "2v3": {
          "auc": 0.5901,
          "ci": [
            0.5806,
            0.5996
          ],
          "perm_p": 0
        },
        "3v4": {
          "auc": 0.539,
          "ci": [
            0.5288,
            0.5493
          ],
          "perm_p": 0
        },
        "4v5": {
          "auc": 0.5348,
          "ci": [
            0.5243,
            0.5454
          ],
          "perm_p": 0
        }
      },
      "config4_t12": {
        "0v1": {
          "auc": 0.9982,
          "ci": [
            0.9975,
            0.9987
          ],
          "perm_p": 0
        },
        "1v2": {
          "auc": 0.7037,
          "ci": [
            0.6945,
            0.7126
          ],
          "perm_p": 0
        },
        "2v3": {
          "auc": 0.582,
          "ci": [
            0.5722,
            0.5917
          ],
          "perm_p": 0
        },
        "3v4": {
          "auc": 0.5293,
          "ci": [
            0.5185,
            0.5399
          ],
          "perm_p": 0
        },
        "4v5": {
          "auc": 0.5237,
          "ci": [
            0.5132,
            0.5347
          ],
          "perm_p": 0.0001
        }
      },
      "resamples": 10000,
      "method": "GroupKFold(5) OOF + doc-level bootstrap + label permutation"
    }
  }
}

================================================================================
EXPERIMENT: exp_020_pythia_decoding
================================================================================
{
  "metrics": {
    "greedy": {
      "K_star": 2,
      "auc": {
        "0v1": 0.9992,
        "1v2": 0.8838,
        "2v3": 0.5342,
        "3v4": 0.5228,
        "4v5": 0.5162
      }
    },
    "nuc09": {
      "K_star": 2,
      "auc": {
        "0v1": 0.9948,
        "1v2": 0.677,
        "2v3": 0.5549,
        "3v4": 0.5299,
        "4v5": 0.5013
      }
    },
    "t07": {
      "K_star": 2,
      "auc": {
        "0v1": 0.9965,
        "1v2": 0.7265,
        "2v3": 0.5941,
        "3v4": 0.5698,
        "4v5": 0.5284
      }
    },
    "t12": {
      "K_star": 2,
      "auc": {
        "0v1": 0.9933,
        "1v2": 0.6172,
        "2v3": 0.5226,
        "3v4": 0.517,
        "4v5": 0.5051
      }
    }
  }
}

================================================================================
EXPERIMENT: exp_016_base_vs_instruct
================================================================================
{
  "metrics": {
    "k_star": 2,
    "pairwise_auc": {
      "0v1": 0.987,
      "1v2": 0.6262,
      "2v3": 0.5496,
      "3v4": 0.5294,
      "4v5": 0.5182
    },
    "pairwise_auc_std": {
      "0v1": 0.0015,
      "1v2": 0.0152,
      "2v3": 0.0067,
      "3v4": 0.0132,
      "4v5": 0.0139
    },
    "pairwise_jsd": {
      "0v1": 0.163726,
      "1v2": 0.01081,
      "2v3": 0.005311,
      "3v4": 0.003942,
      "4v5": 0.003522
    },
    "ordinal_mae": 1.1691,
    "ordinal_accuracy": 0.3719,
    "top_features": [
      "freq_entropy",
      "surp_std",
      "surp_d1_skew",
      "surp_d1_mean",
      "surp_mean"
    ],
    "n_samples": 30000,
    "bootstrap_ci": {
      "0v1": {
        "auc": 0.987,
        "ci_lower": 0.9853,
        "ci_upper": 0.9885,
        "perm_p": 0.0001
      },
      "1v2": {
        "auc": 0.626,
        "ci_lower": 0.6168,
        "ci_upper": 0.6353,
        "perm_p": 0.0001
      },
      "2v3": {
        "auc": 0.5496,
        "ci_lower": 0.5397,
        "ci_upper": 0.56,
        "perm_p": 0.0001
      },
      "3v4": {
        "auc": 0.5293,
        "ci_lower": 0.5188,
        "ci_upper": 0.5399,
        "perm_p": 0.0001
      },
      "4v5": {
        "auc": 0.5181,
        "ci_lower": 0.5075,
        "ci_upper": 0.5288,
        "perm_p": 0.0016
      }
    },
    "bootstrap_resamples": 10000,
    "permutation_resamples": 10000,
    "key_finding": "K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95% CI=[0.6168, 0.6353], CI lower=0.6168 > \u03b8=0.60 (PASS). All pairs significant (p\u22640.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015, 0.6213] \u2014 no significant base-vs-instruct difference."
  }
}

================================================================================
EXPERIMENT: exp_013_cross_transfer
================================================================================
{
  "metrics": {
    "accuracy_matrix": {
      "Qwen_rw\u2192Qwen_rw": 0.4229,
      "Qwen_rw\u2192Pythia": 0.259,
      "Qwen_rw\u2192OLMo": 0.2653,
      "Qwen_rw\u2192Qwen_cont": 0.3466,
      "Pythia\u2192Qwen_rw": 0.2718,
      "Pythia\u2192Pythia": 0.3856,
      "Pythia\u2192OLMo": 0.3531,
      "Pythia\u2192Qwen_cont": 0.3287,
      "OLMo\u2192Qwen_rw": 0.2768,
      "OLMo\u2192Pythia": 0.345,
      "OLMo\u2192OLMo": 0.3822,
      "OLMo\u2192Qwen_cont": 0.3244,
      "Qwen_cont\u2192Qwen_rw": 0.344,
      "Qwen_cont\u2192Pythia": 0.3284,
      "Qwen_cont\u2192OLMo": 0.3112,
      "Qwen_cont\u2192Qwen_cont": 0.3875
    },
    "transfer_retention_accuracy": {
      "Pythia\u2194OLMo": "91-92%",
      "Qwen_rw\u2192Pythia/OLMo": "61-63%",
      "Qwen_cont\u2194Pythia": "83-85%",
      "Qwen_cont\u2194OLMo": "80-85%"
    },
    "transfer_retention_tau": {
      "Pythia\u2194OLMo": "85-86%",
      "Qwen_rw\u2192Pythia/OLMo": "45-50%",
      "Qwen_cont\u2194others": "68-83%"
    },
    "mean_pw_auc_matrix": {
      "within_avg": 0.6099,
      "cross_avg": 0.5905,
      "0v1_cross_all_above": 0.96
    },
    "key_finding": "depth signal \u2248 70-85% text-intrinsic + 15-30% model self-familiarity. Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained depth transfer depends on model family similarity. Qwen-rewrite overfits style features; Qwen-cont transfers much better."
  }
}

================================================================================
EXPERIMENT: exp_012_binary_confidence
================================================================================
{
  "metrics": {
    "n_samples": 500,
    "generators": [
      "qwen-rewrite",
      "pythia-1.4b",
      "olmo-1b",
      "qwen-cont"
    ],
    "6class_accuracy": {
      "qwen-rewrite": 0.1987,
      "pythia-1.4b": 0.1303,
      "olmo-1b": 0.127,
      "qwen-cont": 0.1833,
      "random_baseline": 0.1667
    },
    "spearman_rho": {
      "qwen-rewrite": {
        "log_ppl_ref": -0.1233,
        "log_ppl_obs": 0.0815,
        "ppl_ratio": 0.1185
      },
      "pythia-1.4b": {
        "log_ppl_ref": -0.2972,
        "log_ppl_obs": -0.4529,
        "ppl_ratio": -0.392
      },
      "olmo-1b": {
        "log_ppl_ref": -0.378,
        "log_ppl_obs": -0.4614,
        "ppl_ratio": -0.4068
      },
      "qwen-cont": {
        "log_ppl_ref": -0.3887,
        "log_ppl_obs": -0.162,
        "ppl_ratio": -0.058
      }
    },
    "binary_detector_kstar": 1,
    "obd_kstar": 2,
    "auc_non_monotonic": true,
    "key_finding": "Binary detectors (DivEye/Binoculars) K*\u22481 vs OBD K*=2. 6-class accuracy \u22640.199 (random=0.167). Spearman |\u03c1|=0.06-0.46 (statistically significant but practically weak). AUC non-monotonic \u2014 binary detectors cannot maintain depth ordering. Confirms binary confidence \u2260 depth estimation."
  }
}

================================================================================
EXPERIMENT: exp_011_llm_zeroshot
================================================================================
{
  "metrics": {
    "gpt55_5class_acc": 0.332,
    "gpt55_mae": 1.102,
    "gpt55_spearman": 0.383,
    "gpt55_binary_acc": 0.878,
    "claude_5class_acc": 0.331,
    "claude_mae": 1.15,
    "claude_spearman": 0.416,
    "claude_binary_acc": 0.882,
    "odb_baseline_5class_acc": 0.386,
    "odb_baseline_mae": 1.107,
    "gpt55_per_depth_acc": {
      "depth_0": 0.77,
      "depth_1": 0.19,
      "depth_2": 0.38,
      "depth_3": 0.24,
      "depth_4": 0.08
    },
    "claude_per_depth_acc": {
      "depth_0": 0.69,
      "depth_1": 0.21,
      "depth_2": 0.28,
      "depth_3": 0.101,
      "depth_4": 0.37
    },
    "n_samples_per_model": 500,
    "key_finding": "Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI detection is high (~88%) but fine-grained depth discrimination fails."
  }
}

================================================================================
EXPERIMENT: exp_007_bootstrap_ci
================================================================================
{
  "metrics": {
    "qwen_rewrite": {
      "0v1": {
        "auc": 0.9956,
        "ci_lower": 0.9946,
        "ci_upper": 0.9965,
        "perm_p": 0.002
      },
      "1v2": {
        "auc": 0.6955,
        "ci_lower": 0.6859,
        "ci_upper": 0.7041,
        "perm_p": 0.002
      },
      "2v3": {
        "auc": 0.5893,
        "ci_lower": 0.5795,
        "ci_upper": 0.5991,
        "perm_p": 0.002
      },
      "3v4": {
        "auc": 0.5435,
        "ci_lower": 0.5333,
        "ci_upper": 0.5551,
        "perm_p": 0.002
      },
      "4v5": {
        "auc": 0.534,
        "ci_lower": 0.5238,
        "ci_upper": 0.5448,
        "perm_p": 0.002
      }
    },
    "pythia_cont": {
      "0v1": {
        "auc": 0.9932,
        "ci_lower": 0.9921,
        "ci_upper": 0.9943,
        "perm_p": 0.002
      },
      "1v2": {
        "auc": 0.6539,
        "ci_lower": 0.6454,
        "ci_upper": 0.663,
        "perm_p": 0.002
      },
      "2v3": {
        "auc": 0.5514,
        "ci_lower": 0.5417,
        "ci_upper": 0.5628,
        "perm_p": 0.002
      },
      "3v4": {
        "auc": 0.5152,
        "ci_lower": 0.5041,
        "ci_upper": 0.526,
        "perm_p": 0.006
      },
      "4v5": {
        "auc": 0.5136,
        "ci_lower": 0.5021,
        "ci_upper": 0.5249,
        "perm_p": 0.008
      }
    },
    "olmo_cont": {
      "0v1": {
        "auc": 0.997,
        "ci_lower": 0.9964,
        "ci_upper": 0.9975,
        "perm_p": 0.002
      },
      "1v2": {
        "auc": 0.6145,
        "ci_lower": 0.6045,
        "ci_upper": 0.6247,
        "perm_p": 0.002
      },
      "2v3": {
        "auc": 0.5496,
        "ci_lower": 0.5399,
        "ci_upper": 0.5596,
        "perm_p": 0.002
      },
      "3v4": {
        "auc": 0.5091,
        "ci_lower": 0.4973,
        "ci_upper": 0.52,
        "perm_p": 0.064
      },
      "4v5": {
        "auc": 0.5045,
        "ci_lower": 0.4932,
        "ci_upper": 0.515,
        "perm_p": 0.232
      }
    },
    "qwen_cont": {
      "0v1": {
        "auc": 0.9971,
        "ci_lower": 0.9963,
        "ci_upper": 0.9978,
        "perm_p": 0.002
      },
      "1v2": {
        "auc": 0.6112,
        "ci_lower": 0.6015,
        "ci_upper": 0.6213,
        "perm_p": 0.002
      },
      "2v3": {
        "auc": 0.5609,
        "ci_lower": 0.5511,
        "ci_upper": 0.5712,
        "perm_p": 0.002
      },
      "3v4": {
        "auc": 0.5409,
        "ci_lower": 0.5308,
        "ci_upper": 0.5508,
        "perm_p": 0.002
      },
      "4v5": {
        "auc": 0.5141,
        "ci_lower": 0.5035,
        "ci_upper": 0.5255,
        "perm_p": 0.006
      }
    },
    "k_star_robust": true,
    "all_1v2_ci_lower_above_060": true,
    "most_marginal": "Qwen-cont CI lower=0.6015, only 0.0015 above threshold"
  }
}

================================================================================
EXPERIMENT: exp_006_graduated_filtering
================================================================================
{
  "metrics": {
    "total_runs": 51,
    "binary_ours": {
      "mmlu": "0.5941\u00b10.0008",
      "hellaswag": "0.6701\u00b10.0006"
    },
    "binary_drayson": {
      "mmlu": "0.5913\u00b10.0009",
      "hellaswag": "0.6691\u00b10.0004"
    },
    "surprisal": {
      "mmlu": "0.5894\u00b10.0009",
      "hellaswag": "0.6641\u00b10.0006"
    },
    "graduated_a09": {
      "mmlu": "0.5892\u00b10.0008",
      "hellaswag": "0.6701\u00b10.0007"
    },
    "graduated_a07": {
      "mmlu": "0.5892\u00b10.0014",
      "hellaswag": "0.6695\u00b10.0004"
    },
    "graduated_a05": {
      "mmlu": "0.5880\u00b10.0013",
      "hellaswag": "0.6687\u00b10.0008"
    },
    "graduated_a03": {
      "mmlu": "0.5877\u00b10.0013",
      "hellaswag": "0.6669\u00b10.0005"
    },
    "graduated_a01": {
      "mmlu": "0.5873\u00b10.0019",
      "hellaswag": "0.6640\u00b10.0009"
    },
    "dsir": {
      "mmlu": "0.5869\u00b10.0003",
      "hellaswag": "0.6631\u00b10.0007"
    },
    "no_filter": {
      "mmlu": "0.5865\u00b10.0010",
      "hellaswag": "0.6638\u00b10.0008"
    },
    "base_model": {
      "mmlu": "0.6018",
      "hellaswag": "0.6821"
    },
    "best_strategy": "binary-ours",
    "key_finding": "binary-ours is best filtering strategy. All strategies degrade vs base_model. Graduated \u03b1 monotonically increasing confirms K*=2 boundary. DSIR below all other strategies except no-filter."
  }
}

================================================================================
EXPERIMENT: exp_008_retrain_chain_v2
================================================================================
{
  "metrics": {
    "k_star": ">=4",
    "pairwise_auc": {
      "0v1": 0.9847,
      "1v2": 0.9484,
      "2v3": 0.8888,
      "3v4": 0.7982
    },
    "pairwise_jsd": {
      "0v1": 0.17,
      "1v2": 0.12,
      "2v3": 0.064,
      "3v4": 0.04
    },
    "key_finding": "Retrain-chain K*>=4, all pairs AUC>>0.60. LoRA adaptation artifacts make generations highly distinguishable. Prompt-chain K*=2 is text-intrinsic boundary."
  }
}

================================================================================
EXPERIMENT: exp_022_cross_scorer_matrix
================================================================================
{
  "metrics": {
    "total_combos": 12,
    "completed": 12,
    "K_star_distribution": {
      "K2": 11,
      "K1": 1
    },
    "matrix": {
      "pythia_greedy\u00d7olmo": {
        "K_star": 2,
        "1v2": 0.8811
      },
      "pythia_greedy\u00d7pythia": {
        "K_star": 2,
        "1v2": 0.8838
      },
      "pythia_greedy\u00d7qwen_base": {
        "K_star": 2,
        "1v2": 0.8814
      },
      "pythia_greedy\u00d7qwen_instruct": {
        "K_star": 2,
        "1v2": 0.8818
      },
      "qwen_base\u00d7olmo": {
        "K_star": 2,
        "1v2": 0.6047
      },
      "qwen_base\u00d7pythia": {
        "K_star": 2,
        "1v2": 0.617
      },
      "qwen_base\u00d7qwen_base": {
        "K_star": 2,
        "1v2": 0.6262
      },
      "qwen_base\u00d7qwen_instruct": {
        "K_star": 2,
        "1v2": 0.6273
      },
      "qwen_cont256\u00d7olmo": {
        "K_star": 2,
        "1v2": 0.6028
      },
      "qwen_cont256\u00d7pythia": {
        "K_star": 1,
        "1v2": 0.5979
      },
      "qwen_cont256\u00d7qwen_base": {
        "K_star": 2,
        "1v2": 0.6282
      },
      "qwen_cont256\u00d7qwen_instruct": {
        "K_star": 2,
        "1v2": 0.6072
      }
    },
    "key_finding": "Scorer independence confirmed: K*=2 in 11/12 combos. Only exception: qwen_cont256\u00d7pythia (1v2=0.5979, borderline). Pythia-greedy 1v2~0.88 due to repetition collapse. Scorer choice \u03941v2 < 0.025 within each generator."
  }
}

================================================================================
EXPERIMENT: exp_023_domain_ablation
================================================================================
{
  "metrics": {
    "K_star": 2,
    "1v2_auc": 0.6193,
    "2v3_auc": 0.5498,
    "all_folds_above_060": true,
    "top_feature": "freq_entropy",
    "ordinal_accuracy": 0.377
  }
}

================================================================================
EXPERIMENT: exp_024_arxiv_domain
================================================================================
{
  "metrics": {
    "K_star": 3,
    "pairwise_auc": {
      "0v1": 0.9946,
      "1v2": 0.858,
      "2v3": 0.6427,
      "3v4": 0.5437,
      "4v5": 0.5294
    },
    "bootstrap_ci": {
      "0v1": {
        "auc": 0.9946,
        "ci_lower": 0.9929,
        "ci_upper": 0.9961,
        "perm_p": 0.0001
      },
      "1v2": {
        "auc": 0.858,
        "ci_lower": 0.848,
        "ci_upper": 0.8679,
        "perm_p": 0.0001
      },
      "2v3": {
        "auc": 0.6427,
        "ci_lower": 0.6275,
        "ci_upper": 0.6575,
        "perm_p": 0.0001
      },
      "3v4": {
        "auc": 0.5437,
        "ci_lower": 0.5276,
        "ci_upper": 0.5598,
        "perm_p": 0.0001
      },
      "4v5": {
        "auc": 0.5294,
        "ci_lower": 0.5133,
        "ci_upper": 0.5455,
        "perm_p": 0.0006
      }
    },
    "bootstrap_resamples": 10000,
    "permutation_resamples": 10000,
    "key_finding": "arXiv domain K*=3 (CI-confirmed). 2v3 CI lower=0.6275 > \u03b8=0.60. First condition with K*>2. 1v2 AUC=0.858 far exceeds C4/Wiki (~0.61-0.69)."
  }
}

================================================================================
EXPERIMENT: exp_027_latex_ablation
================================================================================
{
  "metrics": {
    "k_star": 3,
    "k_star_preserved": true,
    "pairwise_auc_original": {
      "0v1": 0.9948,
      "1v2": 0.8581,
      "2v3": 0.6436,
      "3v4": 0.544,
      "4v5": 0.5299
    },
    "pairwise_auc_stripped": {
      "0v1": 0.9948,
      "1v2": 0.8297,
      "2v3": 0.6229,
      "3v4": 0.5468,
      "4v5": 0.5476
    },
    "auc_delta": {
      "0v1": 0,
      "1v2": -0.028,
      "2v3": -0.021,
      "3v4": 0.003,
      "4v5": 0.018
    },
    "latex_reduction_by_depth": {
      "depth_0": "0.6%",
      "depth_5": "4.4%"
    },
    "key_finding": "K*=3 preserved after LaTeX removal. 2v3 AUC 0.6436\u21920.6229 (still >\u03b8=0.60). LaTeX format is NOT a confound."
  }
}

================================================================================
EXPERIMENT: exp_021_length_ablation
================================================================================
{
  "metrics": {
    "128tok": {
      "K_star": 2,
      "1v2_auc": 0.6219
    },
    "256tok": {
      "K_star": 2,
      "1v2_auc": 0.6282
    },
    "512tok": {
      "K_star": 2,
      "1v2_auc": 0.6073
    },
    "all_K_star_2": true,
    "bootstrap_ci": {
      "512tok_1v2": {
        "auc": 0.6073,
        "ci_lower": 0.5979,
        "ci_upper": 0.6166,
        "perm_p": 0.0001,
        "verdict": "BORDERLINE"
      }
    }
  }
}

================================================================================
EXPERIMENT: exp_028_power_curve
================================================================================
{
  "metrics": {
    "min_n_100pct": 2000,
    "n500_auc": 0.5808,
    "n500_rate": 0.2,
    "n1000_auc": 0.5911,
    "n1000_rate": 0.3,
    "n2000_auc": 0.6101,
    "n2000_rate": 1,
    "n3000_auc": 0.6166,
    "n3000_rate": 1,
    "n4000_auc": 0.622,
    "n4000_rate": 1,
    "n5000_auc": 0.6288,
    "n5000_rate": 1
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd43cda3-29be-469c-90dc-80f3ddcd753f",
  "isSidechain": true,
  "promptId": "79672ee0-6083-486d-a275-3f445c8e7cd7",
  "agentId": "a44e38f07bb86c0e3",
  "type": "user",
  "uuid": "106973e3-656b-48af-be96-21a7e27ef6b9",
  "sourceToolAssistantUUID": "fd43cda3-29be-469c-90dc-80f3ddcd753f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-25T19:46:16.208Z_

Now let me search for any experiments with "qwen" and "rewrite" in their name.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "106973e3-656b-48af-be96-21a7e27ef6b9",
  "isSidechain": true,
  "agentId": "a44e38f07bb86c0e3",
  "requestId": "req_011CbPrzVWMyEbXLwfn85E5W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89b3542e-9096-4162-ba35-54003cba88ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Wh4dyJboNANiuYahT2T2t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11308,
      "cache_read_input_tokens": 20425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11308,
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

_source line 22 · 2026-05-25T19:46:26.704Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01M67U75HHGdMsG2SroBhece`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/c2f03400-f630-4847-9da7-a2b649715a9a/tool-results/mcp-agent-ml-research-read_registry-1779738315214.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw[\"result\"])\nexperiments = inner[\"data\"][\"experiments\"]\n\n# Search for experiments with \"qwen\" and \"rewrite\" in their name\nprint(\"=== Experiments matching 'qwen' or 'rewrite' ===\")\nfor k in sorted(experiments.keys()):\n    kl = k.lower()\n    if \"qwen\" in kl or \"rewrite\" in kl:\n        print(f\"\\n  {k}\")\n        # Show abbreviated info\n        m = experiments[k].get(\"metrics\", experiments[k])\n        if isinstance(m, dict):\n            # Show k_star if present\n            for key in [\"k_star\", \"K_star\", \"key_finding\"]:\n                if key in m:\n                    val = m[key]\n                    if isinstance(val, str) and len(val) > 120:\n                        val = val[:120] + \"...\"\n                    print(f\"    {key}: {val}\")\n            # Show pairwise_auc if present\n            if \"pairwise_auc\" in m:\n                print(f\"    pairwise_auc: {m['pairwise_auc']}\")\n            if \"auc\" in m:\n                print(f\"    auc: {m['auc']}\")\n\n# Also check for \"rewrite\" anywhere in experiment values\nprint(\"\\n\\n=== Experiments with 'rewrite' in keys or descriptions ===\")\nfor k in sorted(experiments.keys()):\n    s = json.dumps(experiments[k]).lower()\n    if \"rewrite\" in s and \"qwen\" not in k.lower():\n        print(f\"  {k}\")\nPYEOF",
  "description": "Search for experiments matching 'qwen' or 'rewrite'",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89b3542e-9096-4162-ba35-54003cba88ad",
  "isSidechain": true,
  "agentId": "a44e38f07bb86c0e3",
  "requestId": "req_011CbPrzVWMyEbXLwfn85E5W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b1a8b37-6dc7-4a6f-a2c8-56ee47f237c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Wh4dyJboNANiuYahT2T2t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11308,
      "cache_read_input_tokens": 20425,
      "output_tokens": 659,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11308
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 659,
          "cache_read_input_tokens": 20425,
          "cache_creation_input_tokens": 11308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11308,
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

_source line 23 · 2026-05-25T19:46:26.778Z_

<details><summary>↩ Tool result · `toolu_01M67U75HHGdMsG2SroBhece`</summary>

```text
=== Experiments matching 'qwen' or 'rewrite' ===

  code_domain_qwen7b
    k_star: 2
    key_finding: Qwen-7B Code K*=2 confirmed. 1v2 AUC=0.7273, well above θ. Scale-invariant within Qwen family.
    pairwise_auc: {'0v1': 0.905, '1v2': 0.7273, '2v3': 0.5367, '3v4': 0.5088, '4v5': 0.5137}

  exp_017_qwen_continuation
    k_star: 2
    pairwise_auc: {'0v1': 0.9972, '1v2': 0.6114, '2v3': 0.5609, '3v4': 0.5408, '4v5': 0.5139}

  exp_arXiv_qwen1b5_crossscorer
    k_star: 3

  exp_arXiv_qwen7b
    k_star: 3
    pairwise_auc: {'0v1': 0.983, '1v2': 0.835, '2v3': 0.626, '3v4': 0.544, '4v5': 0.513}

  exp_arXiv_qwen7b_crossscorer
    k_star: 2

  exp_code_qwen1b5
    K_star: 2

  exp_code_qwen1b5_pythia_scorer
    k_star: 2

  exp_code_qwen7b
    k_star: 2
    pairwise_auc: {'0v1': {'mean': 0.9051, 'ci95_half': 0.0043, 'folds': [0.9073, 0.9012, 0.912, 0.9049, 0.9003]}, '1v2': {'mean': 0.7276, 'ci95_half': 0.0055, 'folds': [0.7377, 0.7254, 0.724, 0.722, 0.7289]}, '2v3': {'mean': 0.5368, 'ci95_half': 0.0145, 'folds': [0.5179, 0.5332, 0.5275, 0.5462, 0.5593]}, '3v4': {'mean': 0.509, 'ci95_half': 0.0055, 'folds': [0.5029, 0.5054, 0.5085, 0.5092, 0.5191]}, '4v5': {'mean': 0.5139, 'ci95_half': 0.0128, 'folds': [0.5016, 0.5317, 0.5264, 0.509, 0.5007]}}

  exp_cross_transfer_llama8b_to_qwen7b

  exp_cross_transfer_llama8b_to_qwen7b_v2
    K_star: 3

  exp_cross_transfer_qwen7b_to_llama8b
    pairwise_auc: {'0v1': 0.9998, '1v2': 0.7384, '2v3': 0.6278, '3v4': 0.587, '4v5': 0.5519}

  exp_deberta_arxiv_qwen1b5
    K_star: 4

  exp_deberta_c4_1b5_qwen_cont
    key_finding: C4 1.5B qwen_cont256 K*=2, boundary holds across continuation generation strategy.
    pairwise_auc: {'0v1': 0.9955, '1v2': 0.7194, '2v3': 0.5954, '3v4': 0.5689, '4v5': 0.5502}

  exp_deberta_code_qwen1b5
    K_star: 2

  exp_qwen_cont_10k
    K_star: 2

  exp_qwen_retrain_chain

  exp_qwen_retrain_depth7
    k_star: 7
    pairwise_auc: {'0v1': {'mean': 0.9837, 'std': 0.0019, 'ci_95': [0.9821, 0.9854], 'folds': [0.9832, 0.9821, 0.9837, 0.9823, 0.9873]}, '1v2': {'mean': 0.8971, 'std': 0.0025, 'ci_95': [0.8949, 0.8993], 'folds': [0.8923, 0.8988, 0.8986, 0.8991, 0.8967]}, '2v3': {'mean': 0.8098, 'std': 0.0052, 'ci_95': [0.8052, 0.8144], 'folds': [0.8086, 0.8074, 0.818, 0.8024, 0.8128]}, '3v4': {'mean': 0.76, 'std': 0.0082, 'ci_95': [0.7528, 0.7672], 'folds': [0.7534, 0.7617, 0.7753, 0.7566, 0.7531]}, '4v5': {'mean': 0.7459, 'std': 0.0091, 'ci_95': [0.7379, 0.7538], 'folds': [0.7429, 0.7562, 0.7521, 0.73, 0.7482]}, '5v6': {'mean': 0.7017, 'std': 0.0068, 'ci_95': [0.6958, 0.7076], 'folds': [0.7006, 0.7077, 0.7104, 0.6915, 0.6984]}, '6v7': {'mean': 0.641, 'std': 0.0039, 'ci_95': [0.6376, 0.6445], 'folds': [0.6419, 0.6349, 0.6464, 0.639, 0.643]}}

  exp_wiki_qwen7b
    K_star: 2

  seed_qwen15b_c4_s123

  seed_qwen15b_wiki_s123


=== Experiments with 'rewrite' in keys or descriptions ===
  exp_005_degradation
  exp_007_bootstrap_ci
  exp_010_ordinal_baseline
  exp_012_binary_confidence
  exp_013_cross_transfer
  exp_kstar_theta
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b1a8b37-6dc7-4a6f-a2c8-56ee47f237c2",
  "isSidechain": true,
  "promptId": "79672ee0-6083-486d-a275-3f445c8e7cd7",
  "agentId": "a44e38f07bb86c0e3",
  "type": "user",
  "uuid": "eae87e4f-ddf4-4c63-a47e-b8ccbe43ec58",
  "sourceToolAssistantUUID": "2b1a8b37-6dc7-4a6f-a2c8-56ee47f237c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-25T19:46:31.645Z_

Now let me also get the full metrics for `exp_017_qwen_continuation` since that might be the "rewrite" experiment you're looking for, and also check what `mvp_pilot_sat_v1` description says.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eae87e4f-ddf4-4c63-a47e-b8ccbe43ec58",
  "isSidechain": true,
  "agentId": "a44e38f07bb86c0e3",
  "requestId": "req_011CbPs1Vg4Ye7wanyW85HpG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6573c297-4b86-4522-966a-3bccbc2b5364",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFiXR2wVec9MAQV4ZHxErE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2411,
      "cache_read_input_tokens": 31733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2411,
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

_source line 25 · 2026-05-25T19:46:43.633Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Awxt7yep8oSzgmzrDMqmDu`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/c2f03400-f630-4847-9da7-a2b649715a9a/tool-results/mcp-agent-ml-research-read_registry-1779738315214.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw[\"result\"])\nexperiments = inner[\"data\"][\"experiments\"]\n\n# Full dump of mvp_pilot_sat_v1 (to see if there's a description)\nprint(\"=== mvp_pilot_sat_v1 FULL ===\")\nprint(json.dumps(experiments[\"mvp_pilot_sat_v1\"], indent=2))\n\n# Also dump the \"baseline\" section from data\nprint(\"\\n=== BASELINE ===\")\nif \"baseline\" in inner[\"data\"]:\n    print(json.dumps(inner[\"data\"][\"baseline\"], indent=2))\n\n# Also show metadata\nprint(\"\\n=== METADATA ===\")\nprint(json.dumps(inner.get(\"metadata\", {}), indent=2))\nPYEOF",
  "description": "Get full mvp_pilot_sat_v1 record and baseline/metadata",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6573c297-4b86-4522-966a-3bccbc2b5364",
  "isSidechain": true,
  "agentId": "a44e38f07bb86c0e3",
  "requestId": "req_011CbPs1Vg4Ye7wanyW85HpG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a87c9933-4122-4f00-8f0f-28b4ff8bfded",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFiXR2wVec9MAQV4ZHxErE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2411,
      "cache_read_input_tokens": 31733,
      "output_tokens": 464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2411
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 464,
          "cache_read_input_tokens": 31733,
          "cache_creation_input_tokens": 2411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2411,
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

_source line 26 · 2026-05-25T19:46:43.769Z_

<details><summary>↩ Tool result · `toolu_01Awxt7yep8oSzgmzrDMqmDu`</summary>

```text
=== mvp_pilot_sat_v1 FULL ===
{
  "metrics": {
    "pairwise_auc": {
      "0v1": 0.9956,
      "1v2": 0.6957,
      "2v3": 0.5893,
      "3v4": 0.5434,
      "4v5": 0.5343
    },
    "pairwise_auc_std": {
      "0v1": 0.0005,
      "1v2": 0.0072,
      "2v3": 0.012,
      "3v4": 0.0053,
      "4v5": 0.0091
    },
    "pairwise_jsd": {
      "0v1": 0.2669,
      "1v2": 0.0163,
      "2v3": 0.0069,
      "3v4": 0.0047,
      "4v5": 0.0041
    },
    "k_star": 2,
    "ordinal_mae": 1.0163,
    "ordinal_accuracy": 0.4182
  }
}

=== BASELINE ===
null

=== METADATA ===
{
  "elapsed_seconds": 0.5465
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a87c9933-4122-4f00-8f0f-28b4ff8bfded",
  "isSidechain": true,
  "promptId": "79672ee0-6083-486d-a275-3f445c8e7cd7",
  "agentId": "a44e38f07bb86c0e3",
  "type": "user",
  "uuid": "6668c1fb-364a-4a35-a6b1-dd2254922c55",
  "sourceToolAssistantUUID": "a87c9933-4122-4f00-8f0f-28b4ff8bfded",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-25T19:48:42.748Z_

Here are all the verbatim metrics for every requested experiment:

---

## 1. mvp_pilot_sat_v1 (Qwen-1.5B rewrite)

- **k_star**: 2
- **pairwise_auc**: 0v1=0.9956, 1v2=0.6957, 2v3=0.5893, 3v4=0.5434, 4v5=0.5343
- **pairwise_auc_std**: 0v1=0.0005, 1v2=0.0072, 2v3=0.012, 3v4=0.0053, 4v5=0.0091
- **pairwise_jsd**: 0v1=0.2669, 1v2=0.0163, 2v3=0.0069, 3v4=0.0047, 4v5=0.0041
- **ordinal_mae**: 1.0163
- **ordinal_accuracy**: 0.4182

---

## 2. exp_004_7b_crossscale (Qwen-7B)

- **k_star**: 2
- **pairwise_auc**: 0v1=0.9644, 1v2=0.6178, 2v3=0.546, 3v4=0.5225, 4v5=0.5091
- **pairwise_auc_std**: 0v1=0.0034, 1v2=0.0081, 2v3=0.0028, 3v4=0.0113, 4v5=0.0052
- **bootstrap_ci**:
  - 0v1: auc=0.9638, ci_lower=0.9607, ci_upper=0.9665, perm_p=0.0001
  - 1v2: auc=0.6168, ci_lower=0.6079, ci_upper=0.6261, perm_p=0.0001
  - 2v3: auc=0.5492, ci_lower=0.5388, ci_upper=0.5594, perm_p=0.0001
  - 3v4: auc=0.5276, ci_lower=0.517, ci_upper=0.5375, perm_p=0.0001
  - 4v5: auc=0.5085, ci_lower=0.4988, ci_upper=0.5191, perm_p=0.0676
- **bootstrap_resamples**: 1000, **permutation_resamples**: 10000
- **pairwise_jsd**: 0v1=0.127422, 1v2=0.010114, 2v3=0.004798, 3v4=0.004821, 4v5=0.003335
- **ordinal_mae**: 1.2156
- **ordinal_accuracy**: 0.3523
- **top_features**: freq_entropy, surp_d1_skew, surp_std, surp_d1_mean, surp_mean
- **key_finding**: "K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60 (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676). FR-4 Warning resolved."

---

## 3. exp_018_llama8b_depth (LLaMA-8B)

- **k_star**: 2
- **pairwise_auc**: 0v1=0.9225, 1v2=0.6123, 2v3=0.5274, 3v4=0.5138, 4v5=0.5097
- **jsd**: 0v1=0.077, 1v2=0.012, 2v3=0.005
- **bootstrap_ci**:
  - 0v1: auc=0.9224, ci_lower=0.9174, ci_upper=0.9272, perm_p=0.0001
  - 1v2: auc=0.6123, ci_lower=0.6028, ci_upper=0.6216, perm_p=0.0001
  - 2v3: auc=0.5273, ci_lower=0.5169, ci_upper=0.5378, perm_p=0.0001
  - 3v4: auc=0.5168, ci_lower=0.5062, ci_upper=0.5275, perm_p=0.0037
  - 4v5: auc=0.5159, ci_lower=0.5052, ci_upper=0.5268, perm_p=0.0035
- **bootstrap_resamples**: 10000, **permutation_resamples**: 10000

---

## 4. exp_019_mistral7b_depth (Mistral-7B)

- **k_star**: 1
- **pairwise_auc**: 0v1=0.9843, 1v2=0.5935, 2v3=0.5402, 3v4=0.5232, 4v5=0.5181
- **bootstrap_ci_1v2**: ci_lower=0.5835, ci_upper=0.6032, p_auc_leq_060=0.9017
- **jsd**: 0v1=0.124194, 1v2=0.008051, 2v3=0.005047, 3v4=0.004516, 4v5=0.004109
- **ordinal_mae**: 1.2275
- **ordinal_accuracy**: 0.3567
- **top3_features**: freq_entropy, surp_d1_skew, surp_d1_mean

---

## 5. exp_003_decoding_ablation

- **K_star**: 2, **K_star_robust**: true
- **bootstrap_ci** (method: "GroupKFold(5) OOF + doc-level bootstrap + label permutation", resamples=10000):
  - **config1_greedy**: 0v1: auc=0.9796 ci=[0.9772,0.982] p=0 | 1v2: auc=0.6892 ci=[0.6802,0.6982] p=0 | 2v3: auc=0.5612 ci=[0.5517,0.5705] p=0 | 3v4: auc=0.5405 ci=[0.5308,0.5502] p=0 | 4v5: auc=0.5137 ci=[0.5033,0.5238] p=0.0082
  - **config2_nuc09**: 0v1: auc=0.9945 ci=[0.9934,0.9956] p=0 | 1v2: auc=0.6862 ci=[0.6774,0.6951] p=0 | 2v3: auc=0.5917 ci=[0.5824,0.601] p=0 (note: "CI upper crosses theta=0.60") | 3v4: auc=0.5468 ci=[0.5369,0.5568] p=0 | 4v5: auc=0.5066 ci=[0.4959,0.5173] p=0.1199
  - **config3_t07**: 0v1: auc=0.9877 ci=[0.9857,0.9896] p=0 | 1v2: auc=0.6885 ci=[0.6797,0.697] p=0 | 2v3: auc=0.5901 ci=[0.5806,0.5996] p=0 | 3v4: auc=0.539 ci=[0.5288,0.5493] p=0 | 4v5: auc=0.5348 ci=[0.5243,0.5454] p=0
  - **config4_t12**: 0v1: auc=0.9982 ci=[0.9975,0.9987] p=0 | 1v2: auc=0.7037 ci=[0.6945,0.7126] p=0 | 2v3: auc=0.582 ci=[0.5722,0.5917] p=0 | 3v4: auc=0.5293 ci=[0.5185,0.5399] p=0 | 4v5: auc=0.5237 ci=[0.5132,0.5347] p=0.0001

---

## 6. exp_020_pythia_decoding

- **greedy**: K_star=2, auc: 0v1=0.9992, 1v2=0.8838, 2v3=0.5342, 3v4=0.5228, 4v5=0.5162
- **nuc09**: K_star=2, auc: 0v1=0.9948, 1v2=0.677, 2v3=0.5549, 3v4=0.5299, 4v5=0.5013
- **t07**: K_star=2, auc: 0v1=0.9965, 1v2=0.7265, 2v3=0.5941, 3v4=0.5698, 4v5=0.5284
- **t12**: K_star=2, auc: 0v1=0.9933, 1v2=0.6172, 2v3=0.5226, 3v4=0.517, 4v5=0.5051

---

## 7. exp_016_base_vs_instruct

- **k_star**: 2
- **pairwise_auc**: 0v1=0.987, 1v2=0.6262, 2v3=0.5496, 3v4=0.5294, 4v5=0.5182
- **pairwise_auc_std**: 0v1=0.0015, 1v2=0.0152, 2v3=0.0067, 3v4=0.0132, 4v5=0.0139
- **pairwise_jsd**: 0v1=0.163726, 1v2=0.01081, 2v3=0.005311, 3v4=0.003942, 4v5=0.003522
- **ordinal_mae**: 1.1691
- **ordinal_accuracy**: 0.3719
- **top_features**: freq_entropy, surp_std, surp_d1_skew, surp_d1_mean, surp_mean
- **n_samples**: 30000
- **bootstrap_ci**:
  - 0v1: auc=0.987, ci_lower=0.9853, ci_upper=0.9885, perm_p=0.0001
  - 1v2: auc=0.626, ci_lower=0.6168, ci_upper=0.6353, perm_p=0.0001
  - 2v3: auc=0.5496, ci_lower=0.5397, ci_upper=0.56, perm_p=0.0001
  - 3v4: auc=0.5293, ci_lower=0.5188, ci_upper=0.5399, perm_p=0.0001
  - 4v5: auc=0.5181, ci_lower=0.5075, ci_upper=0.5288, perm_p=0.0016
- **bootstrap_resamples**: 10000, **permutation_resamples**: 10000
- **key_finding**: "K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95% CI=[0.6168, 0.6353], CI lower=0.6168 > θ=0.60 (PASS). All pairs significant (p≤0.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015, 0.6213] — no significant base-vs-instruct difference."

---

## 8. exp_013_cross_transfer

- **accuracy_matrix** (4x4, format "train→test"):
  - Qwen_rw→Qwen_rw: 0.4229, Qwen_rw→Pythia: 0.259, Qwen_rw→OLMo: 0.2653, Qwen_rw→Qwen_cont: 0.3466
  - Pythia→Qwen_rw: 0.2718, Pythia→Pythia: 0.3856, Pythia→OLMo: 0.3531, Pythia→Qwen_cont: 0.3287
  - OLMo→Qwen_rw: 0.2768, OLMo→Pythia: 0.345, OLMo→OLMo: 0.3822, OLMo→Qwen_cont: 0.3244
  - Qwen_cont→Qwen_rw: 0.344, Qwen_cont→Pythia: 0.3284, Qwen_cont→OLMo: 0.3112, Qwen_cont→Qwen_cont: 0.3875
- **transfer_retention_accuracy**: Pythia↔OLMo: 91-92%, Qwen_rw→Pythia/OLMo: 61-63%, Qwen_cont↔Pythia: 83-85%, Qwen_cont↔OLMo: 80-85%
- **transfer_retention_tau**: Pythia↔OLMo: 85-86%, Qwen_rw→Pythia/OLMo: 45-50%, Qwen_cont↔others: 68-83%
- **mean_pw_auc_matrix**: within_avg=0.6099, cross_avg=0.5905, 0v1_cross_all_above=0.96
- **key_finding**: "depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity. Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained depth transfer depends on model family similarity. Qwen-rewrite overfits style features; Qwen-cont transfers much better."

---

## 9. exp_012_binary_confidence

- **n_samples**: 500
- **generators**: qwen-rewrite, pythia-1.4b, olmo-1b, qwen-cont
- **6class_accuracy**: qwen-rewrite=0.1987, pythia-1.4b=0.1303, olmo-1b=0.127, qwen-cont=0.1833, random_baseline=0.1667
- **spearman_rho**:
  - qwen-rewrite: log_ppl_ref=-0.1233, log_ppl_obs=0.0815, ppl_ratio=0.1185
  - pythia-1.4b: log_ppl_ref=-0.2972, log_ppl_obs=-0.4529, ppl_ratio=-0.392
  - olmo-1b: log_ppl_ref=-0.378, log_ppl_obs=-0.4614, ppl_ratio=-0.4068
  - qwen-cont: log_ppl_ref=-0.3887, log_ppl_obs=-0.162, ppl_ratio=-0.058
- **binary_detector_kstar**: 1, **obd_kstar**: 2
- **auc_non_monotonic**: true
- **key_finding**: "Binary detectors (DivEye/Binoculars) K*≈1 vs OBD K*=2. 6-class accuracy ≤0.199 (random=0.167). Spearman |ρ|=0.06-0.46 (statistically significant but practically weak). AUC non-monotonic — binary detectors cannot maintain depth ordering. Confirms binary confidence ≠ depth estimation."

---

## 10. exp_011_llm_zeroshot

- **gpt55_5class_acc**: 0.332, **gpt55_mae**: 1.102, **gpt55_spearman**: 0.383, **gpt55_binary_acc**: 0.878
- **claude_5class_acc**: 0.331, **claude_mae**: 1.15, **claude_spearman**: 0.416, **claude_binary_acc**: 0.882
- **odb_baseline_5class_acc**: 0.386, **odb_baseline_mae**: 1.107
- **gpt55_per_depth_acc**: depth_0=0.77, depth_1=0.19, depth_2=0.38, depth_3=0.24, depth_4=0.08
- **claude_per_depth_acc**: depth_0=0.69, depth_1=0.21, depth_2=0.28, depth_3=0.101, depth_4=0.37
- **n_samples_per_model**: 500
- **key_finding**: "Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI detection is high (~88%) but fine-grained depth discrimination fails."

---

## 11. exp_007_bootstrap_ci

- **k_star_robust**: true, **all_1v2_ci_lower_above_060**: true
- **most_marginal**: "Qwen-cont CI lower=0.6015, only 0.0015 above threshold"
- **qwen_rewrite**: 0v1: auc=0.9956 ci=[0.9946,0.9965] p=0.002 | 1v2: auc=0.6955 ci=[0.6859,0.7041] p=0.002 | 2v3: auc=0.5893 ci=[0.5795,0.5991] p=0.002 | 3v4: auc=0.5435 ci=[0.5333,0.5551] p=0.002 | 4v5: auc=0.534 ci=[0.5238,0.5448] p=0.002
- **pythia_cont**: 0v1: auc=0.9932 ci=[0.9921,0.9943] p=0.002 | 1v2: auc=0.6539 ci=[0.6454,0.663] p=0.002 | 2v3: auc=0.5514 ci=[0.5417,0.5628] p=0.002 | 3v4: auc=0.5152 ci=[0.5041,0.526] p=0.006 | 4v5: auc=0.5136 ci=[0.5021,0.5249] p=0.008
- **olmo_cont**: 0v1: auc=0.997 ci=[0.9964,0.9975] p=0.002 | 1v2: auc=0.6145 ci=[0.6045,0.6247] p=0.002 | 2v3: auc=0.5496 ci=[0.5399,0.5596] p=0.002 | 3v4: auc=0.5091 ci=[0.4973,0.52] p=0.064 | 4v5: auc=0.5045 ci=[0.4932,0.515] p=0.232
- **qwen_cont**: 0v1: auc=0.9971 ci=[0.9963,0.9978] p=0.002 | 1v2: auc=0.6112 ci=[0.6015,0.6213] p=0.002 | 2v3: auc=0.5609 ci=[0.5511,0.5712] p=0.002 | 3v4: auc=0.5409 ci=[0.5308,0.5508] p=0.002 | 4v5: auc=0.5141 ci=[0.5035,0.5255] p=0.006

---

## 12. exp_006_graduated_filtering

- **total_runs**: 51
- **binary_ours**: mmlu=0.5941±0.0008, hellaswag=0.6701±0.0006
- **binary_drayson**: mmlu=0.5913±0.0009, hellaswag=0.6691±0.0004
- **surprisal**: mmlu=0.5894±0.0009, hellaswag=0.6641±0.0006
- **graduated_a09**: mmlu=0.5892±0.0008, hellaswag=0.6701±0.0007
- **graduated_a07**: mmlu=0.5892±0.0014, hellaswag=0.6695±0.0004
- **graduated_a05**: mmlu=0.5880±0.0013, hellaswag=0.6687±0.0008
- **graduated_a03**: mmlu=0.5877±0.0013, hellaswag=0.6669±0.0005
- **graduated_a01**: mmlu=0.5873±0.0019, hellaswag=0.6640±0.0009
- **dsir**: mmlu=0.5869±0.0003, hellaswag=0.6631±0.0007
- **no_filter**: mmlu=0.5865±0.0010, hellaswag=0.6638±0.0008
- **base_model**: mmlu=0.6018, hellaswag=0.6821
- **best_strategy**: binary-ours
- **key_finding**: "binary-ours is best filtering strategy. All strategies degrade vs base_model. Graduated α monotonically increasing confirms K*=2 boundary. DSIR below all other strategies except no-filter."

---

## 13. exp_008_retrain_chain_v2

- **k_star**: ">=4"
- **pairwise_auc**: 0v1=0.9847, 1v2=0.9484, 2v3=0.8888, 3v4=0.7982
- **pairwise_jsd**: 0v1=0.17, 1v2=0.12, 2v3=0.064, 3v4=0.04
- **key_finding**: "Retrain-chain K*>=4, all pairs AUC>>0.60. LoRA adaptation artifacts make generations highly distinguishable. Prompt-chain K*=2 is text-intrinsic boundary."

---

## 14. exp_022_cross_scorer_matrix

- **total_combos**: 12, **completed**: 12
- **K_star_distribution**: K2=11, K1=1
- **matrix** (generator×scorer → K_star, 1v2 AUC):
  - pythia_greedy×olmo: K*=2, 1v2=0.8811
  - pythia_greedy×pythia: K*=2, 1v2=0.8838
  - pythia_greedy×qwen_base: K*=2, 1v2=0.8814
  - pythia_greedy×qwen_instruct: K*=2, 1v2=0.8818
  - qwen_base×olmo: K*=2, 1v2=0.6047
  - qwen_base×pythia: K*=2, 1v2=0.617
  - qwen_base×qwen_base: K*=2, 1v2=0.6262
  - qwen_base×qwen_instruct: K*=2, 1v2=0.6273
  - qwen_cont256×olmo: K*=2, 1v2=0.6028
  - qwen_cont256×pythia: K*=1, 1v2=0.5979
  - qwen_cont256×qwen_base: K*=2, 1v2=0.6282
  - qwen_cont256×qwen_instruct: K*=2, 1v2=0.6072
- **key_finding**: "Scorer independence confirmed: K*=2 in 11/12 combos. Only exception: qwen_cont256×pythia (1v2=0.5979, borderline). Pythia-greedy 1v2~0.88 due to repetition collapse. Scorer choice Δ1v2 < 0.025 within each generator."

---

## 15. exp_023_domain_ablation (wiki)

- **K_star**: 2
- **1v2_auc**: 0.6193
- **2v3_auc**: 0.5498
- **all_folds_above_060**: true
- **top_feature**: freq_entropy
- **ordinal_accuracy**: 0.377

---

## 16. exp_024_arxiv_domain

- **K_star**: 3
- **pairwise_auc**: 0v1=0.9946, 1v2=0.858, 2v3=0.6427, 3v4=0.5437, 4v5=0.5294
- **bootstrap_ci**:
  - 0v1: auc=0.9946, ci_lower=0.9929, ci_upper=0.9961, perm_p=0.0001
  - 1v2: auc=0.858, ci_lower=0.848, ci_upper=0.8679, perm_p=0.0001
  - 2v3: auc=0.6427, ci_lower=0.6275, ci_upper=0.6575, perm_p=0.0001
  - 3v4: auc=0.5437, ci_lower=0.5276, ci_upper=0.5598, perm_p=0.0001
  - 4v5: auc=0.5294, ci_lower=0.5133, ci_upper=0.5455, perm_p=0.0006
- **bootstrap_resamples**: 10000, **permutation_resamples**: 10000
- **key_finding**: "arXiv domain K*=3 (CI-confirmed). 2v3 CI lower=0.6275 > θ=0.60. First condition with K*>2. 1v2 AUC=0.858 far exceeds C4/Wiki (~0.61-0.69)."

---

## 17. exp_027_latex_ablation

- **k_star**: 3, **k_star_preserved**: true
- **pairwise_auc_original**: 0v1=0.9948, 1v2=0.8581, 2v3=0.6436, 3v4=0.544, 4v5=0.5299
- **pairwise_auc_stripped**: 0v1=0.9948, 1v2=0.8297, 2v3=0.6229, 3v4=0.5468, 4v5=0.5476
- **auc_delta**: 0v1=0, 1v2=-0.028, 2v3=-0.021, 3v4=0.003, 4v5=0.018
- **latex_reduction_by_depth**: depth_0=0.6%, depth_5=4.4%
- **key_finding**: "K*=3 preserved after LaTeX removal. 2v3 AUC 0.6436→0.6229 (still >θ=0.60). LaTeX format is NOT a confound."

---

## 18. exp_021_length_ablation

- **128tok**: K_star=2, 1v2_auc=0.6219
- **256tok**: K_star=2, 1v2_auc=0.6282
- **512tok**: K_star=2, 1v2_auc=0.6073
- **all_K_star_2**: true
- **bootstrap_ci 512tok_1v2**: auc=0.6073, ci_lower=0.5979, ci_upper=0.6166, perm_p=0.0001, verdict="BORDERLINE"

---

## 19. exp_028_power_curve

- **min_n_100pct**: 2000
- n500: auc=0.5808, rate=0.2
- n1000: auc=0.5911, rate=0.3
- n2000: auc=0.6101, rate=1.0
- n3000: auc=0.6166, rate=1.0
- n4000: auc=0.622, rate=1.0
- n5000: auc=0.6288, rate=1.0

---

## Experiments matching "qwen" + "rewrite"

No experiment has both "qwen" and "rewrite" literally in its key. The closest candidate is **mvp_pilot_sat_v1**, which is the Qwen-1.5B rewrite experiment (metrics already listed above as #1). The experiment **exp_007_bootstrap_ci** contains a sub-key `qwen_rewrite` with full bootstrap CI metrics (listed above as #11). Other Qwen-related experiments found: `exp_017_qwen_continuation` (K*=2, pairwise_auc: 0v1=0.9972, 1v2=0.6114, 2v3=0.5609, 3v4=0.5408, 4v5=0.5139), and various cross-domain/cross-scorer Qwen experiments, but none with "rewrite" in the experiment ID.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6668c1fb-364a-4a35-a6b1-dd2254922c55",
  "isSidechain": true,
  "agentId": "a44e38f07bb86c0e3",
  "requestId": "req_011CbPs2kK9xmfpbGEvWrtRF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41a6486f-d262-40c9-a32d-5eeab34c1482",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "c2f03400-f630-4847-9da7-a2b649715a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WNcc5BmSRsM1tvDiG9Dr9r",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 807,
      "cache_read_input_tokens": 34144,
      "output_tokens": 7674,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 807
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7674,
          "cache_read_input_tokens": 34144,
          "cache_creation_input_tokens": 807,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 807,
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
