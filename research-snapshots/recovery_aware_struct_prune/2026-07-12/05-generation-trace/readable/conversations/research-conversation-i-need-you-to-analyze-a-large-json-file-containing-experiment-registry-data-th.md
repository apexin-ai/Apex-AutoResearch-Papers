# Research conversation: I need you to analyze a large JSON file containing experiment registry data. The file is at: /home/ubuntu/.claude-accoun

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a5932a6af8063e1b2.jsonl`
- **Structured JSON:** [`bf09e8be491b00fb9f7d.json`](../../sessions/bf/bf09e8be491b00fb9f7d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

16 recorded events

### User

_source line 1 · 2026-05-19T18:25:04.395Z_

I need you to analyze a large JSON file containing experiment registry data. The file is at:
/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/d24dd67d-247f-4de1-8e6b-d350286085b1/tool-results/mcp-agent-ml-research-read_registry-1779215077988.txt

This file has schema: {result: string} where result is a JSON string containing experiment entries.

I need you to:
1. Extract all experiments with "1p5b" or "1.5b" in the experiment_id/name — list their id, status, conclusion, and key metrics
2. Extract all experiments with "mbpp" in the id/name — list their id, status, conclusion, and key metrics
3. Extract all experiments with "seed123" in the id/name — list their id, status, conclusion, and key metrics
4. Extract all experiments related to "cka_reliability" or "scoring_ablation" or "plan_014" — list their id, status, and conclusion
5. List all RUNNING experiments

Use jq or python to parse. Report findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "960327b2-48f4-4244-ad53-4d2ea4bdae2b",
  "agentId": "a5932a6af8063e1b2",
  "type": "user",
  "uuid": "02bd316f-d191-44af-aae9-61c7c5483cc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d24dd67d-247f-4de1-8e6b-d350286085b1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T18:25:04.400Z_

```json
{
  "parentUuid": "02bd316f-d191-44af-aae9-61c7c5483cc7",
  "isSidechain": true,
  "agentId": "a5932a6af8063e1b2",
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
  "uuid": "4a4af6e8-44bd-4ddd-b4bb-2da7c68cb4f7",
  "timestamp": "2026-05-19T18:25:04.400Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d24dd67d-247f-4de1-8e6b-d350286085b1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-19T18:25:06.971Z_



Let me start by reading the file to understand its structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a4af6e8-44bd-4ddd-b4bb-2da7c68cb4f7",
  "isSidechain": true,
  "agentId": "a5932a6af8063e1b2",
  "requestId": "req_011CbCPx6qcUzvabiZKM9LRc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7cc60da-34e9-4d74-aa82-93878259d69b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d24dd67d-247f-4de1-8e6b-d350286085b1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DL5TwXrpFEZcRqU1fg6j3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14910,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14910,
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

_source line 4 · 2026-05-19T18:25:08.095Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S221XkSQBJjvEY4YTpPtBC`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/d24dd67d-247f-4de1-8e6b-d350286085b1/tool-results/mcp-agent-ml-research-read_registry-1779215077988.txt",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7cc60da-34e9-4d74-aa82-93878259d69b",
  "isSidechain": true,
  "agentId": "a5932a6af8063e1b2",
  "requestId": "req_011CbCPx6qcUzvabiZKM9LRc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1caa0f3d-2d41-46bc-be4e-c4944ff6c327",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d24dd67d-247f-4de1-8e6b-d350286085b1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DL5TwXrpFEZcRqU1fg6j3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14910,
      "cache_read_input_tokens": 0,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 175,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 14910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14910,
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

_source line 5 · 2026-05-19T18:25:08.388Z_

<details><summary>↩ Tool result · reported error · `toolu_01S221XkSQBJjvEY4YTpPtBC`</summary>

```text
File content (65283 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1caa0f3d-2d41-46bc-be4e-c4944ff6c327",
  "isSidechain": true,
  "promptId": "960327b2-48f4-4244-ad53-4d2ea4bdae2b",
  "agentId": "a5932a6af8063e1b2",
  "type": "user",
  "uuid": "3c23200b-1c6b-4c6b-ac44-cce7953c370f",
  "toolUseResult": "Error: File content (65283 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "1caa0f3d-2d41-46bc-be4e-c4944ff6c327",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d24dd67d-247f-4de1-8e6b-d350286085b1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-19T18:25:12.219Z_

The file is very large. Let me use Python to parse it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c23200b-1c6b-4c6b-ac44-cce7953c370f",
  "isSidechain": true,
  "agentId": "a5932a6af8063e1b2",
  "requestId": "req_011CbCPxPq4cmp5wsMef1csY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe75c7b0-d998-4c42-9c60-285b20fda17c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d24dd67d-247f-4de1-8e6b-d350286085b1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DV6CJFs3785ZVj1JnB8ytz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1077,
      "cache_read_input_tokens": 14910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1077,
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

_source line 7 · 2026-05-19T18:25:13.587Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BQ53VuRCKQJjLTkEEUAJ16`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/d24dd67d-247f-4de1-8e6b-d350286085b1/tool-results/mcp-agent-ml-research-read_registry-1779215077988.txt",
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe75c7b0-d998-4c42-9c60-285b20fda17c",
  "isSidechain": true,
  "agentId": "a5932a6af8063e1b2",
  "requestId": "req_011CbCPxPq4cmp5wsMef1csY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8430a6a-28bf-4c2f-be64-92d78c2430f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d24dd67d-247f-4de1-8e6b-d350286085b1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DV6CJFs3785ZVj1JnB8ytz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1077,
      "cache_read_input_tokens": 14910,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1077
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 14910,
          "cache_creation_input_tokens": 1077,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1077,
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

_source line 8 · 2026-05-19T18:25:13.858Z_

<details><summary>↩ Tool result · reported error · `toolu_01BQ53VuRCKQJjLTkEEUAJ16`</summary>

```text
File content (65283 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8430a6a-28bf-4c2f-be64-92d78c2430f8",
  "isSidechain": true,
  "promptId": "960327b2-48f4-4244-ad53-4d2ea4bdae2b",
  "agentId": "a5932a6af8063e1b2",
  "type": "user",
  "uuid": "b7a13085-6056-45d8-811b-b894dfd0552b",
  "toolUseResult": "Error: File content (65283 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "c8430a6a-28bf-4c2f-be64-92d78c2430f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d24dd67d-247f-4de1-8e6b-d350286085b1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T18:25:17.377Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015sgSHWTwujmj9pvu4VDRBo`</summary>

```json
{
  "command": "head -c 500 \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/d24dd67d-247f-4de1-8e6b-d350286085b1/tool-results/mcp-agent-ml-research-read_registry-1779215077988.txt\"",
  "description": "Check file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7a13085-6056-45d8-811b-b894dfd0552b",
  "isSidechain": true,
  "agentId": "a5932a6af8063e1b2",
  "requestId": "req_011CbCPxoBFbQZtwHUfKyRMP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f6866ee-2e17-4e4e-8761-5afd3a6851b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d24dd67d-247f-4de1-8e6b-d350286085b1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RvAzwPAK6fksJKcCm4jVWK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 237,
      "cache_read_input_tokens": 15987,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 237
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 15987,
          "cache_creation_input_tokens": 237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 237,
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

_source line 10 · 2026-05-19T18:25:17.575Z_

<details><summary>↩ Tool result · `toolu_015sgSHWTwujmj9pvu4VDRBo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_mbpp_grpo_rasp_20\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:18:35.729Z\", \"updated_at\": \"2026-05-19T18:24:28.539Z\", \"hypothesis\": \"MBPP pass@1 eval on GRPO RASP 20% model @2048. Dense baseline=53.48% (200/374). RASP GRPO GSM8K=60.88%, HumanEval=10.37%. Tests RASP GRPO code generation on MBPP. Completes MBPP 3×2 matrix. Expected: between CKA-only GRPO (14.17%) and Standard GRPO (running). Recovery gradient
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f6866ee-2e17-4e4e-8761-5afd3a6851b1",
  "isSidechain": true,
  "promptId": "960327b2-48f4-4244-ad53-4d2ea4bdae2b",
  "agentId": "a5932a6af8063e1b2",
  "type": "user",
  "uuid": "43b82104-0fa6-46d9-ae16-7dc41be8e02d",
  "sourceToolAssistantUUID": "9f6866ee-2e17-4e4e-8761-5afd3a6851b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d24dd67d-247f-4de1-8e6b-d350286085b1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T18:25:37.572Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017fGpyKN6cPqrQkwFoc44xC`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/d24dd67d-247f-4de1-8e6b-d350286085b1/tool-results/mcp-agent-ml-research-read_registry-1779215077988.txt\"\n\npython3 << 'PYEOF'\nimport json\n\nwith open(\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/d24dd67d-247f-4de1-8e6b-d350286085b1/tool-results/mcp-agent-ml-research-read_registry-1779215077988.txt\") as f:\n    raw = json.load(f)\n\ninner = json.loads(raw[\"result\"])\nexperiments = inner[\"data\"][\"experiments\"]\n\nprint(f\"Total experiments: {len(experiments)}\")\nprint(\"---\")\n\n# 1. Experiments with \"1p5b\" or \"1.5b\"\nprint(\"\\n=== 1. Experiments with '1p5b' or '1.5b' ===\")\nfor eid, edata in experiments.items():\n    if \"1p5b\" in eid.lower() or \"1.5b\" in eid.lower():\n        status = edata.get(\"status\", \"N/A\")\n        conclusion = edata.get(\"conclusion\", \"N/A\")\n        metrics = edata.get(\"metrics\", edata.get(\"key_metrics\", {}))\n        print(f\"\\nID: {eid}\")\n        print(f\"  Status: {status}\")\n        print(f\"  Conclusion: {conclusion}\")\n        if metrics:\n            print(f\"  Metrics: {json.dumps(metrics, indent=4)}\")\n\n# 2. Experiments with \"mbpp\"\nprint(\"\\n\\n=== 2. Experiments with 'mbpp' ===\")\nfor eid, edata in experiments.items():\n    if \"mbpp\" in eid.lower():\n        status = edata.get(\"status\", \"N/A\")\n        conclusion = edata.get(\"conclusion\", \"N/A\")\n        metrics = edata.get(\"metrics\", edata.get(\"key_metrics\", {}))\n        print(f\"\\nID: {eid}\")\n        print(f\"  Status: {status}\")\n        print(f\"  Conclusion: {conclusion}\")\n        if metrics:\n            print(f\"  Metrics: {json.dumps(metrics, indent=4)}\")\n\n# 3. Experiments with \"seed123\"\nprint(\"\\n\\n=== 3. Experiments with 'seed123' ===\")\nfor eid, edata in experiments.items():\n    if \"seed123\" in eid.lower():\n        status = edata.get(\"status\", \"N/A\")\n        conclusion = edata.get(\"conclusion\", \"N/A\")\n        metrics = edata.get(\"metrics\", edata.get(\"key_metrics\", {}))\n        print(f\"\\nID: {eid}\")\n        print(f\"  Status: {status}\")\n        print(f\"  Conclusion: {conclusion}\")\n        if metrics:\n            print(f\"  Metrics: {json.dumps(metrics, indent=4)}\")\n\n# 4. Experiments with \"cka_reliability\", \"scoring_ablation\", \"plan_014\"\nprint(\"\\n\\n=== 4. Experiments with 'cka_reliability' / 'scoring_ablation' / 'plan_014' ===\")\nfor eid, edata in experiments.items():\n    if any(kw in eid.lower() for kw in [\"cka_reliability\", \"scoring_ablation\", \"plan_014\"]):\n        status = edata.get(\"status\", \"N/A\")\n        conclusion = edata.get(\"conclusion\", \"N/A\")\n        print(f\"\\nID: {eid}\")\n        print(f\"  Status: {status}\")\n        print(f\"  Conclusion: {conclusion}\")\n\n# 5. All RUNNING experiments\nprint(\"\\n\\n=== 5. All RUNNING experiments ===\")\nfor eid, edata in experiments.items():\n    if edata.get(\"status\", \"\").upper() == \"RUNNING\":\n        print(f\"\\nID: {eid}\")\n        hypothesis = edata.get(\"hypothesis\", \"N/A\")\n        print(f\"  Hypothesis: {hypothesis[:200]}...\")\n\nPYEOF",
  "description": "Parse registry JSON and extract experiment data for all 5 queries",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43b82104-0fa6-46d9-ae16-7dc41be8e02d",
  "isSidechain": true,
  "agentId": "a5932a6af8063e1b2",
  "requestId": "req_011CbCPy55UXDxP7bLAsoXAh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "146fd0c6-0a10-4f99-afa9-12fec7a3bdf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d24dd67d-247f-4de1-8e6b-d350286085b1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bLpVz33ZC1i24jTj9aLqd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 392,
      "cache_read_input_tokens": 16224,
      "output_tokens": 1206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1206,
          "cache_read_input_tokens": 16224,
          "cache_creation_input_tokens": 392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 392,
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

_source line 12 · 2026-05-19T18:25:37.689Z_

<details><summary>↩ Tool result · `toolu_017fGpyKN6cPqrQkwFoc44xC`</summary>

```text
Total experiments: 227
---

=== 1. Experiments with '1p5b' or '1.5b' ===

ID: eval_humaneval_grpo_standard_20_1p5b_2048
  Status: DONE
  Conclusion: success

ID: eval_humaneval_sft_cka_only_20_1p5b_2048
  Status: DONE
  Conclusion: success
  Metrics: {
    "pass_at_1": 0.0061,
    "stderr": 0.0061,
    "n_correct": 1,
    "n_total": 164,
    "avg_response_length": 1968.8,
    "median_response_length": 2048
}

ID: eval_humaneval_grpo_cka_only_20_1p5b_2048
  Status: DONE
  Conclusion: success
  Metrics: {
    "pass_at_1": 0,
    "stderr": 0,
    "n_correct": 0,
    "n_total": 164,
    "avg_response_length": 1977.7,
    "median_response_length": 2048
}

ID: eval_humaneval_sft_standard_20_1p5b_2048
  Status: DONE
  Conclusion: success
  Metrics: {
    "pass_at_1": 0.0061,
    "n_correct": 1,
    "n_total": 164,
    "stderr": 0.0061
}

ID: eval_gsm8k_sft_standard_20_1p5b
  Status: DONE
  Conclusion: success
  Metrics: {
    "accuracy": 0.22896133434420016,
    "n_correct": 302,
    "n_total": 1319
}

ID: eval_gsm8k_sft_rasp_20_1p5b
  Status: DONE
  Conclusion: success
  Metrics: {
    "accuracy": 0.2691,
    "n_correct": 355,
    "n_total": 1319,
    "stderr": 0.0122,
    "grpo_delta_pp": -0.75
}

ID: eval_gsm8k_sft_cka_only_20_1p5b
  Status: DONE
  Conclusion: success
  Metrics: {
    "accuracy": 0.3563,
    "n_correct": 470,
    "n_total": 1319,
    "stderr": 0.0132,
    "eos_rate": 0.9507,
    "avg_response_length": 336.76
}

ID: eval_gsm8k_grpo_rasp_20_1p5b
  Status: DONE
  Conclusion: success
  Metrics: {
    "accuracy": 0.2616,
    "n_correct": 345,
    "n_total": 1319,
    "stderr": 0.0121,
    "eos_rate": 0.9378,
    "avg_response_length": 392.7
}

ID: eval_gsm8k_grpo_standard_20_1p5b
  Status: DONE
  Conclusion: success
  Metrics: {
    "accuracy": 0.2229,
    "n_correct": 294,
    "n_total": 1319,
    "stderr": 0.0115
}

ID: eval_gsm8k_grpo_cka_only_20_1p5b
  Status: DONE
  Conclusion: success
  Metrics: {
    "accuracy": 0.3548,
    "n_correct": 468,
    "n_total": 1319,
    "stderr": 0.0132
}

ID: grpo_rasp_20_1p5b
  Status: DONE
  Conclusion: success
  Metrics: {
    "final_reward": 0.099,
    "frac_zero_std": 0.175,
    "clipped_ratio": 0.82
}

ID: grpo_cka_only_20_1p5b
  Status: DONE
  Conclusion: success
  Metrics: {
    "reward_mean": 0.2375,
    "frac_reward_zero_std": 0.175,
    "loss": 0.0595,
    "kl": 0.00215,
    "grad_norm": 1.445,
    "global_step": 100,
    "note": "training completed 100/100 but save_model failed (disk full). checkpoint-100 has complete model."
}

ID: grpo_standard_20_1p5b
  Status: DONE
  Conclusion: success
  Metrics: {
    "reward_mean": 0.0844,
    "frac_reward_zero_std": 0.15,
    "loss": 0.0151,
    "grad_norm": 4.03125,
    "kl": 0.0044,
    "entropy": 0.4617,
    "final_step": 100,
    "max_steps": 100,
    "total_time_min": 53
}

ID: sft_standard_20_1p5b
  Status: DONE
  Conclusion: success

ID: sft_cka_only_20_1p5b
  Status: DONE
  Conclusion: success

ID: sft_rasp_20_1p5b
  Status: DONE
  Conclusion: success


=== 2. Experiments with 'mbpp' ===

ID: eval_mbpp_grpo_rasp_20
  Status: DONE
  Conclusion: failed

ID: eval_mbpp_sft_rasp_20
  Status: DONE
  Conclusion: failed

ID: eval_mbpp_grpo_cka_only_20
  Status: DONE
  Conclusion: success
  Metrics: {
    "pass_at_1": 0.1417,
    "n_correct": 53,
    "n_total": 374,
    "stderr": 0.018
}

ID: eval_mbpp_dense_unpruned
  Status: DONE
  Conclusion: success
  Metrics: {
    "pass_at_1": 0.5348,
    "stderr": 0.0258,
    "n_correct": 200,
    "n_total": 374
}


=== 3. Experiments with 'seed123' ===

ID: eval_gsm8k_grpo_cka_only_20_seed123
  Status: DONE
  Conclusion: success
  Metrics: {
    "accuracy": 0.6422,
    "stderr": 0.0132,
    "n_correct": 847,
    "n_total": 1319,
    "eos_rate": 0.9909,
    "avg_response_length": 195.97,
    "natural_eos": 1307,
    "truncated": 12
}

ID: grpo_cka_only_20_seed123
  Status: DONE
  Conclusion: success
  Metrics: {
    "train_loss": 0.1361,
    "final_step_loss": 0.05054,
    "final_reward": 0.2975,
    "final_reward_std": 0.4097,
    "train_steps": 100,
    "train_runtime_hours": 11.63,
    "wandb_run": "j8kn0sqd"
}

ID: eval_sft_standard_20_seed123
  Status: DONE
  Conclusion: failed

ID: eval_sft_rasp_20_seed123
  Status: DONE
  Conclusion: failed


=== 4. Experiments with 'cka_reliability' / 'scoring_ablation' / 'plan_014' ===

ID: scoring_ablation_magnitude_20
  Status: DONE
  Conclusion: failed

ID: scoring_ablation_batch_v2
  Status: DONE
  Conclusion: failed


=== 5. All RUNNING experiments ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "146fd0c6-0a10-4f99-afa9-12fec7a3bdf4",
  "isSidechain": true,
  "promptId": "960327b2-48f4-4244-ad53-4d2ea4bdae2b",
  "agentId": "a5932a6af8063e1b2",
  "type": "user",
  "uuid": "1d49ee5d-f42a-45a1-b59a-cbe94d1ebddf",
  "sourceToolAssistantUUID": "146fd0c6-0a10-4f99-afa9-12fec7a3bdf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d24dd67d-247f-4de1-8e6b-d350286085b1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-19T18:25:41.448Z_

Now let me get more details on the experiments that had minimal metrics output, and check for any additional fields I might have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d49ee5d-f42a-45a1-b59a-cbe94d1ebddf",
  "isSidechain": true,
  "agentId": "a5932a6af8063e1b2",
  "requestId": "req_011CbCPzZ8xdiYjB98daEC9j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4227e7d0-4f57-46cb-b8e7-8b6825cf032f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d24dd67d-247f-4de1-8e6b-d350286085b1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6y2oQMN3EQEF1HRpCWY8r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3265,
      "cache_read_input_tokens": 16616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3265,
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

_source line 14 · 2026-05-19T18:25:52.141Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VzbtaV6aQ6JidzyxM3NwUh`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open(\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/d24dd67d-247f-4de1-8e6b-d350286085b1/tool-results/mcp-agent-ml-research-read_registry-1779215077988.txt\") as f:\n    raw = json.load(f)\n\ninner = json.loads(raw[\"result\"])\nexperiments = inner[\"data\"][\"experiments\"]\n\n# Check some experiments missing metrics for additional fields\nfor eid in [\"eval_humaneval_grpo_standard_20_1p5b_2048\", \"sft_standard_20_1p5b\", \"sft_cka_only_20_1p5b\", \"sft_rasp_20_1p5b\",\n            \"eval_mbpp_grpo_rasp_20\", \"eval_mbpp_sft_rasp_20\",\n            \"scoring_ablation_magnitude_20\", \"scoring_ablation_batch_v2\",\n            \"eval_sft_standard_20_seed123\", \"eval_sft_rasp_20_seed123\"]:\n    if eid in experiments:\n        e = experiments[eid]\n        print(f\"\\n--- {eid} ---\")\n        # Print all keys\n        for k, v in e.items():\n            if k in (\"hypothesis\",):\n                print(f\"  {k}: {str(v)[:200]}\")\n            else:\n                print(f\"  {k}: {v}\")\n\n# Also check all statuses\nprint(\"\\n\\n=== Status distribution ===\")\nfrom collections import Counter\nstatuses = Counter(e.get(\"status\",\"UNKNOWN\") for e in experiments.values())\nfor s, c in statuses.most_common():\n    print(f\"  {s}: {c}\")\n\nPYEOF",
  "description": "Get details on experiments with missing metrics and check status distribution",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4227e7d0-4f57-46cb-b8e7-8b6825cf032f",
  "isSidechain": true,
  "agentId": "a5932a6af8063e1b2",
  "requestId": "req_011CbCPzZ8xdiYjB98daEC9j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "feca6b77-f94a-46f7-a42d-1101557d0e9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d24dd67d-247f-4de1-8e6b-d350286085b1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6y2oQMN3EQEF1HRpCWY8r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3265,
      "cache_read_input_tokens": 16616,
      "output_tokens": 597,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3265
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 597,
          "cache_read_input_tokens": 16616,
          "cache_creation_input_tokens": 3265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3265,
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

_source line 15 · 2026-05-19T18:25:52.226Z_

<details><summary>↩ Tool result · `toolu_01VzbtaV6aQ6JidzyxM3NwUh`</summary>

```text
--- eval_humaneval_grpo_standard_20_1p5b_2048 ---
  status: DONE
  created_at: 2026-05-19T11:35:48.029Z
  updated_at: 2026-05-19T17:02:50.370Z
  hypothesis: 1.5B GRPO Standard HumanEval pass@1 @2048. Cross-scale validation baseline. 7B GRPO Standard HumanEval failed (multiple attempts). If 1.5B Standard also shows weak code generation after GRPO (vs CKA-o
  conclusion: success

--- sft_standard_20_1p5b ---
  status: DONE
  created_at: 2026-05-18T12:09:56.278Z
  updated_at: 2026-05-18T12:31:29.300Z
  hypothesis: Standard 20% SFT recovery on 1.5B model. Cross-model generalization test: if Standard SFT recovery pattern holds on 1.5B as on 7B. Paired with CKA-only and RASP 1.5B SFT for cross-scale comparison of 
  conclusion: success

--- sft_cka_only_20_1p5b ---
  status: DONE
  created_at: 2026-05-18T11:29:09.842Z
  updated_at: 2026-05-18T12:31:27.978Z
  hypothesis: CKA-only 20% SFT recovery on 1.5B model. Cross-model generalization test: if CKA-only SFT recovery pattern (high accuracy) holds on 1.5B as on 7B, validates that CKA-guided pruning preserves recovery 
  notes: Training completed 1870/1870 steps. Checkpoint save crashed (RuntimeError at inline_container.cc:668) due to disk 100% full. Model weights rescued from checkpoint-1870 (optimizer.pt truncated but model.safetensors intact). Checkpoints cleaned, model files promoted to output dir. Pending load validation.
  conclusion: success

--- sft_rasp_20_1p5b ---
  status: DONE
  created_at: 2026-05-18T12:09:57.178Z
  updated_at: 2026-05-18T12:29:19.746Z
  hypothesis: RASP 20% SFT recovery on 1.5B model. Cross-model generalization test: if RASP SFT recovery pattern holds on 1.5B as on 7B. Paired with CKA-only and Standard 1.5B SFT for cross-scale comparison of reco
  conclusion: success

--- eval_mbpp_grpo_rasp_20 ---
  status: DONE
  created_at: 2026-05-19T18:18:35.729Z
  updated_at: 2026-05-19T18:24:28.539Z
  hypothesis: MBPP pass@1 eval on GRPO RASP 20% model @2048. Dense baseline=53.48% (200/374). RASP GRPO GSM8K=60.88%, HumanEval=10.37%. Tests RASP GRPO code generation on MBPP. Completes MBPP 3×2 matrix. Expected: 
  conclusion: failed

--- eval_mbpp_sft_rasp_20 ---
  status: DONE
  created_at: 2026-05-19T18:18:34.640Z
  updated_at: 2026-05-19T18:23:21.466Z
  hypothesis: MBPP pass@1 eval on SFT RASP 20% model @2048. Dense baseline=53.48% (200/374). RASP SFT GSM8K=60.88% (post-GRPO), HumanEval SFT=10.37%. Tests whether RASP SFT preserves code capability on MBPP. Part o
  conclusion: failed
  notes: Model not found on westb. 7B SFT RASP checkpoint is on westd (sft_rasp_20_westd), not westb. Need to rerun on westd when GPU available.

--- scoring_ablation_magnitude_20 ---
  created_at: 2026-05-17T04:21:41.038Z
  hypothesis: Magnitude-only scoring (weight L2 norm per group) at 20% sparsity. Isolates contribution of gradient signal vs weight magnitude. If post-prune accuracy near 0% (as expected from heavy early-layer prun
  status: DONE
  updated_at: 2026-05-18T05:52:12.799Z
  conclusion: failed

--- scoring_ablation_batch_v2 ---
  conclusion: failed
  created_at: 2026-05-17T05:45:47.123Z
  hypothesis: Scoring ablation with controlled search space (MLP-only, --skip_attention): CKA-aware scoring (RASP) preserves more post-prune accuracy than magnitude-only, gradient-only, random, or CKA-only scoring 
  metrics: {'gradient_postprune': {'acc': 0.255, 'n_samples': 200, 'note': '25.5% - significantly better than magnitude (0%), gradient preserves some structure'}, 'gradient_sft': {'disk_issue': '/dev/md0 250G 100% full', 'reason': 'Disk full at step 935/1870 (50%)', 'status': 'FAILED'}, 'magnitude_postprune': {'acc': 0, 'avg_len': 4054, 'early_stopped': True, 'eos_rate': 0.02, 'n_samples': 60}, 'magnitude_sft': {'reason': 'Extreme per-layer non-uniformity, unrecoverable', 'status': 'FAILED'}, 'random_postprune': {'progress': '26/200', 'status': 'in_progress'}}
  notes: 失败原因: westb-23072 /dev/md0 (250G系统盘) 在 gradient_sft step 935/1870 时写满 | 已有成果: magnitude_postprune=0%(60样本,early_stop), magnitude_sft=FAILED(non-uniformity不可恢复), gradient_postprune=25.5%(200样本), random_postprune 仅完成 26/200 | gradient_sft 已由独立实验 gradient_sft_v3 成功完成 | 建议: 清理系统盘后重试，或拆分为独立实验分别跑(scoring_ablation_magnitude_20, scoring_ablation_random_20, scoring_ablation_cka_only_20 已在 PREPARING)
  parent: scoring_ablation_batch
  status: DONE
  updated_at: 2026-05-17T10:23:53.103Z

--- eval_sft_standard_20_seed123 ---
  conclusion: failed
  created_at: 2026-05-17T03:18:18.061Z
  hypothesis: Multi-seed variance estimation: Standard 20% post-SFT GSM8K accuracy should show low variance (std<3pp) across seeds, confirming seed=42 result (64%) is representative. Part of 5-seed suite for statis
  notes: westd-11672 服务器不可达 (SSH check failed 5x, Unable to connect to port 11672). 非代码问题，服务器恢复后需重跑。轻量 eval 任务 (n=200)。
  parent: sft_standard_20
  status: DONE
  updated_at: 2026-05-17T05:43:39.380Z

--- eval_sft_rasp_20_seed123 ---
  conclusion: failed
  created_at: 2026-05-17T03:18:16.149Z
  hypothesis: Multi-seed variance estimation: RASP 20% post-SFT GSM8K accuracy should show low variance (std<3pp) across seeds, confirming seed=42 result (57%) is representative. Part of 5-seed suite for statistica
  notes: westd-11672 服务器不可达 (SSH check failed 5x, Unable to connect to port 11672). 非代码问题，服务器恢复后需重跑。轻量 eval 任务 (n=200)。
  parent: sft_rasp_20
  status: DONE
  updated_at: 2026-05-17T05:43:38.035Z


=== Status distribution ===
  DONE: 227
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "feca6b77-f94a-46f7-a42d-1101557d0e9c",
  "isSidechain": true,
  "promptId": "960327b2-48f4-4244-ad53-4d2ea4bdae2b",
  "agentId": "a5932a6af8063e1b2",
  "type": "user",
  "uuid": "b6c1a415-9727-40ac-b8c0-c812ab5779e8",
  "sourceToolAssistantUUID": "feca6b77-f94a-46f7-a42d-1101557d0e9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d24dd67d-247f-4de1-8e6b-d350286085b1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-19T18:26:18.982Z_

Here are the findings:

---

## 1. Experiments with "1p5b" / "1.5b" (16 total, all DONE/success)

**Training runs (3):**

| ID | Conclusion | Key Metrics |
|---|---|---|
| `grpo_rasp_20_1p5b` | success | final_reward=0.099, frac_zero_std=0.175, clipped_ratio=0.82 |
| `grpo_cka_only_20_1p5b` | success | reward_mean=0.2375, loss=0.0595, kl=0.00215 (disk full during save, checkpoint-100 intact) |
| `grpo_standard_20_1p5b` | success | reward_mean=0.0844, loss=0.0151, kl=0.0044, 53 min total |
| `sft_standard_20_1p5b` | success | (no metrics recorded) |
| `sft_cka_only_20_1p5b` | success | (disk full crash during checkpoint save; model rescued from checkpoint-1870) |
| `sft_rasp_20_1p5b` | success | (no metrics recorded) |

**GSM8K evals (6):**

| ID | Accuracy | n_correct/n_total |
|---|---|---|
| `eval_gsm8k_sft_cka_only_20_1p5b` | **35.63%** | 470/1319 |
| `eval_gsm8k_grpo_cka_only_20_1p5b` | **35.48%** | 468/1319 |
| `eval_gsm8k_sft_rasp_20_1p5b` | 26.91% | 355/1319 |
| `eval_gsm8k_grpo_rasp_20_1p5b` | 26.16% | 345/1319 |
| `eval_gsm8k_sft_standard_20_1p5b` | 22.90% | 302/1319 |
| `eval_gsm8k_grpo_standard_20_1p5b` | 22.29% | 294/1319 |

**HumanEval evals (4):**

| ID | pass@1 | n_correct/n_total |
|---|---|---|
| `eval_humaneval_sft_cka_only_20_1p5b_2048` | 0.61% | 1/164 |
| `eval_humaneval_sft_standard_20_1p5b_2048` | 0.61% | 1/164 |
| `eval_humaneval_grpo_cka_only_20_1p5b_2048` | 0% | 0/164 |
| `eval_humaneval_grpo_standard_20_1p5b_2048` | success (no metrics recorded) |

**Takeaway:** On 1.5B, CKA-only pruning dominates GSM8K (~35.5%) vs Standard (~22.5%), but all methods collapse on HumanEval (0-0.6%).

---

## 2. Experiments with "mbpp" (4 total, all DONE)

| ID | Status | Conclusion | Key Metrics |
|---|---|---|---|
| `eval_mbpp_dense_unpruned` | DONE | success | pass@1=**53.48%** (200/374) -- baseline |
| `eval_mbpp_grpo_cka_only_20` | DONE | success | pass@1=**14.17%** (53/374) |
| `eval_mbpp_grpo_rasp_20` | DONE | failed | (no metrics -- failure) |
| `eval_mbpp_sft_rasp_20` | DONE | failed | (model not found on westb; checkpoint is on westd, needs rerun) |

---

## 3. Experiments with "seed123" (4 total, all DONE)

| ID | Status | Conclusion | Key Metrics |
|---|---|---|---|
| `grpo_cka_only_20_seed123` | DONE | success | train_loss=0.1361, final_reward=0.2975, 11.63h runtime |
| `eval_gsm8k_grpo_cka_only_20_seed123` | DONE | success | accuracy=**64.22%** (847/1319), eos_rate=99.1% |
| `eval_sft_standard_20_seed123` | DONE | failed | Server unreachable (westd-11672 SSH failed 5x) |
| `eval_sft_rasp_20_seed123` | DONE | failed | Server unreachable (westd-11672 SSH failed 5x) |

**Note:** The two failed seed123 evals are infrastructure failures (server down), not code/model failures.

---

## 4. Experiments with "cka_reliability" / "scoring_ablation" / "plan_014" (2 total)

| ID | Status | Conclusion | Notes |
|---|---|---|---|
| `scoring_ablation_magnitude_20` | DONE | failed | (no detailed metrics) |
| `scoring_ablation_batch_v2` | DONE | failed | magnitude_postprune=0%, gradient_postprune=25.5%, gradient_sft failed (disk full at step 935/1870), random_postprune only 26/200 done |

No experiments matched "cka_reliability" or "plan_014".

---

## 5. RUNNING experiments

**None.** All 227 experiments have status DONE.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6c1a415-9727-40ac-b8c0-c812ab5779e8",
  "isSidechain": true,
  "agentId": "a5932a6af8063e1b2",
  "requestId": "req_011CbCQ1dRDCFrd9DuHP4Mo4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a05f892-11d5-4573-8af8-87e045e06a17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d24dd67d-247f-4de1-8e6b-d350286085b1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2Nn4uBPbBpdSHdKPV5whQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2785,
      "cache_read_input_tokens": 19881,
      "output_tokens": 1416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2785
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1416,
          "cache_read_input_tokens": 19881,
          "cache_creation_input_tokens": 2785,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2785,
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
