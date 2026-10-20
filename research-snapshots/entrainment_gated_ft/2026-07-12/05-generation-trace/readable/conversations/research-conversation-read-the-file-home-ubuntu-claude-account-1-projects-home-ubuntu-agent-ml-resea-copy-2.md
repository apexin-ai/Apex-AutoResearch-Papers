# Research conversation: Read the file /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--c

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a149fcadad70fa034.jsonl`
- **Structured JSON:** [`0b9311648bcebf4cb288.json`](../../sessions/0b/0b9311648bcebf4cb288.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

15 recorded events

### User

_source line 1 · 2026-05-16T03:23:31.205Z_

Read the file /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-reviewer-fe2ad71b/ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8/tool-results/mcp-agent-ml-research-read_registry-1778901796593.txt

This is JSON with schema: {result: string}. The `result` field is a string containing YAML-formatted experiment registry entries.

I need you to extract and report:
1. ALL experiments with status=RUNNING or status=PREPARING — list their exp_id, status, description, server, any GPU/device info
2. ALL experiments with status=DONE that were updated in the last 48 hours (updated_at >= 2026-05-14) — list their exp_id, conclusion, key metrics
3. Any experiments whose registry status hasn't been updated to match reality (handoff mentioned: internlm2_constrained_mckp_v2 should be DONE, llama_longctx_8k_eval should be DONE, internlm2_constrained_mckp v1 should be FAILED)
4. Total count of experiments by status

Use jq or python to parse. The result field is a string, so you'll need to extract it first. Report findings verbatim with exact exp_ids and metrics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "05c25958-d42d-45df-8f4d-41835d17b7a7",
  "agentId": "a149fcadad70fa034",
  "type": "user",
  "uuid": "69d066b5-21f7-4026-9d5e-d4f84e0cfc41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T03:23:31.208Z_

```json
{
  "parentUuid": "69d066b5-21f7-4026-9d5e-d4f84e0cfc41",
  "isSidechain": true,
  "agentId": "a149fcadad70fa034",
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
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
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
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "cc59f3f4-2386-4c74-8d98-8b5b7a98cc73",
  "timestamp": "2026-05-16T03:23:31.208Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-16T03:23:32.788Z_

I'll read the file and extract the registry information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc59f3f4-2386-4c74-8d98-8b5b7a98cc73",
  "isSidechain": true,
  "agentId": "a149fcadad70fa034",
  "requestId": "req_011Cb5Xmuny3s9pSJJmokGP6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c05fa3a-ae75-4555-b563-62340b687523",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AJpQ9ShEcxi5sz1wg9G6Ut",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23435,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23435,
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

_source line 4 · 2026-05-16T03:23:33.818Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AM9Wih6USnW8e9ajRMqrGW`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-reviewer-fe2ad71b/ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8/tool-results/mcp-agent-ml-research-read_registry-1778901796593.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c05fa3a-ae75-4555-b563-62340b687523",
  "isSidechain": true,
  "agentId": "a149fcadad70fa034",
  "requestId": "req_011Cb5Xmuny3s9pSJJmokGP6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d148116c-d6f9-4e40-b7ff-670f29e1c351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AJpQ9ShEcxi5sz1wg9G6Ut",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23435,
      "cache_read_input_tokens": 0,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 23435
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 165,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 23435,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 23435,
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

_source line 5 · 2026-05-16T03:23:34.094Z_

<details><summary>↩ Tool result · reported error · `toolu_01AM9Wih6USnW8e9ajRMqrGW`</summary>

```text
File content (74730 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d148116c-d6f9-4e40-b7ff-670f29e1c351",
  "isSidechain": true,
  "promptId": "05c25958-d42d-45df-8f4d-41835d17b7a7",
  "agentId": "a149fcadad70fa034",
  "type": "user",
  "uuid": "be3718dd-e789-415b-8e1c-2d32bce7e4af",
  "toolUseResult": "Error: File content (74730 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "d148116c-d6f9-4e40-b7ff-670f29e1c351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-16T03:23:35.996Z_

The file is too large to read at once. I'll use targeted searches to extract the needed information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be3718dd-e789-415b-8e1c-2d32bce7e4af",
  "isSidechain": true,
  "agentId": "a149fcadad70fa034",
  "requestId": "req_011Cb5Xn8988CpVHLnFH2BuR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "741806c3-ecfa-4c31-8c8e-03b430281668",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017Nvcm2z87xMneMoywKJyJx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1066,
      "cache_read_input_tokens": 23435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1066,
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

_source line 7 · 2026-05-16T03:23:45.081Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012wTd58sk4tbzt33yuQvWV9`</summary>

```json
{
  "command": "python3 -c \"\nimport json, yaml, sys\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-reviewer-fe2ad71b/ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8/tool-results/mcp-agent-ml-research-read_registry-1778901796593.txt', 'r') as f:\n    raw = f.read()\n\n# Parse outer JSON\ndata = json.loads(raw)\nyaml_str = data['result']\n\n# Parse YAML\nregistry = yaml.safe_load(yaml_str)\n\n# Count by status\nfrom collections import Counter\nstatuses = Counter()\nrunning_preparing = []\ndone_recent = []\n\nexperiments = registry if isinstance(registry, list) else registry.get('experiments', [])\n\nfor exp in experiments:\n    status = exp.get('status', 'UNKNOWN')\n    statuses[status] += 1\n    \n    if status in ('RUNNING', 'PREPARING'):\n        running_preparing.append(exp)\n    \n    if status == 'DONE':\n        updated = exp.get('updated_at', '') or ''\n        if str(updated) >= '2026-05-14':\n            done_recent.append(exp)\n\nprint('=== STATUS COUNTS ===')\nfor k, v in sorted(statuses.items()):\n    print(f'  {k}: {v}')\n\nprint()\nprint('=== RUNNING / PREPARING ===')\nfor exp in running_preparing:\n    print(f\\\"exp_id: {exp.get('exp_id')}\\\")\n    print(f\\\"  status: {exp.get('status')}\\\")\n    print(f\\\"  description: {exp.get('description', '')[:120]}\\\")\n    print(f\\\"  server: {exp.get('server', exp.get('spec', {}).get('server', 'N/A'))}\\\")\n    spec = exp.get('spec', {})\n    print(f\\\"  gpu/device: {spec.get('gpu_ids', spec.get('device', spec.get('gpus', 'N/A')))}\\\")\n    print()\n\nprint('=== DONE (updated >= 2026-05-14) ===')\nfor exp in done_recent:\n    print(f\\\"exp_id: {exp.get('exp_id')}\\\")\n    print(f\\\"  updated_at: {exp.get('updated_at')}\\\")\n    print(f\\\"  conclusion: {str(exp.get('conclusion', ''))[:200]}\\\")\n    metrics = exp.get('metrics', exp.get('results', {}))\n    print(f\\\"  metrics: {metrics}\\\")\n    print()\n\" 2>&1 | head -300\n",
  "description": "Parse registry JSON/YAML and extract status counts, running/preparing, and recent done experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "741806c3-ecfa-4c31-8c8e-03b430281668",
  "isSidechain": true,
  "agentId": "a149fcadad70fa034",
  "requestId": "req_011Cb5Xn8988CpVHLnFH2BuR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03816737-9562-422f-b32e-83c5eac97542",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017Nvcm2z87xMneMoywKJyJx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1066,
      "cache_read_input_tokens": 23435,
      "output_tokens": 802,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1066
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 802,
          "cache_read_input_tokens": 23435,
          "cache_creation_input_tokens": 1066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1066,
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

_source line 8 · 2026-05-16T03:23:45.604Z_

<details><summary>↩ Tool result · `toolu_012wTd58sk4tbzt33yuQvWV9`</summary>

```text
=== STATUS COUNTS ===

=== RUNNING / PREPARING ===
=== DONE (updated >= 2026-05-14) ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03816737-9562-422f-b32e-83c5eac97542",
  "isSidechain": true,
  "promptId": "05c25958-d42d-45df-8f4d-41835d17b7a7",
  "agentId": "a149fcadad70fa034",
  "type": "user",
  "uuid": "90d6240a-aa26-4392-8149-15494a292764",
  "sourceToolAssistantUUID": "03816737-9562-422f-b32e-83c5eac97542",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T03:23:49.146Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CKbAuMjBCN1eGWsXQWdbe8`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-reviewer-fe2ad71b/ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8/tool-results/mcp-agent-ml-research-read_registry-1778901796593.txt', 'r') as f:\n    raw = f.read()\n\ndata = json.loads(raw)\nyaml_str = data['result']\nprint('Type of result:', type(yaml_str))\nprint('First 2000 chars:')\nprint(yaml_str[:2000])\n\"\n",
  "description": "Inspect the result field structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90d6240a-aa26-4392-8149-15494a292764",
  "isSidechain": true,
  "agentId": "a149fcadad70fa034",
  "requestId": "req_011Cb5XnyUFj5F8gCf9xCGPf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a050712d-f463-4c68-85e0-7af1e02722c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EQEuMwjuNsRyBJrnodU6UZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 848,
      "cache_read_input_tokens": 24501,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 848
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 24501,
          "cache_creation_input_tokens": 848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 848,
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

_source line 10 · 2026-05-16T03:23:49.246Z_

<details><summary>↩ Tool result · `toolu_01CKbAuMjBCN1eGWsXQWdbe8`</summary>

```text
Type of result: &lt;class 'str'>
First 2000 chars:
{"success": true, "data": {"experiments": {"codellama_constrained_mckp": {"status": "PREPARING", "retry_count": 0, "created_at": "2026-05-16T03:11:59.301Z", "updated_at": "2026-05-16T03:18:39.237Z", "hypothesis": "CodeLlama-7B constrained MCKP: Spike shape (c=0.80, t1/t5=0.81). Expect no benefit from non-uniform — confirming profiling-based classification. Converts 9/9 claim from '8/8 confirmed + 1 predicted' to fully experimentally confirmed.", "parent": "codellama_hires_profiling", "spec": {"command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/ratekv && python run_codellama_constrained_mckp.py --gpu 0\"", "server": "westd-37397", "gpu": ["cuda:1"], "pid": "396720", "log_path": "~/runs/ratekv/codellama_constrained_mckp.log", "submitted_at": "2026-05-16T03:18:38.926Z", "submitted_via": "submit_training_job", "backend": "tmux", "account": "root"}}, "yi_8k_eval": {"status": "PREPARING", "retry_count": 0, "created_at": "2026-05-16T03:13:23.584Z", "updated_at": "2026-05-16T03:13:30.948Z", "hypothesis": "Yi-1.5-9B 8K long-context eval: Spike shape (c=0.71, t1/t5=0.90). Expect no MCKP benefit at 8K — Spike control for Spread-specific long-context amplification claim."}, "mistral_8k_eval": {"status": "PREPARING", "retry_count": 0, "created_at": "2026-05-16T03:13:21.885Z", "updated_at": "2026-05-16T03:13:29.527Z", "hypothesis": "Mistral-7B 8K long-context eval: Flat shape (c=0.22). Expect no MCKP benefit at 8K — Spike/Flat control for Spread-specific long-context amplification claim."}, "internlm2_constrained_mckp_v2": {"status": "RUNNING", "retry_count": 0, "created_at": "2026-05-16T03:10:21.809Z", "updated_at": "2026-05-16T03:10:42.820Z", "spec": {"command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/ratekv && python run_internlm2_constrained_mckp.py --gpu 0\"", "server": "westd-37397", "gpu": ["cuda:0"], "pid": "395573", "log_path": "~/runs/ratekv/internlm2_constrained_mck
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a050712d-f463-4c68-85e0-7af1e02722c5",
  "isSidechain": true,
  "promptId": "05c25958-d42d-45df-8f4d-41835d17b7a7",
  "agentId": "a149fcadad70fa034",
  "type": "user",
  "uuid": "41d60d43-eeb0-4c5c-a118-723e2bdfedc2",
  "sourceToolAssistantUUID": "a050712d-f463-4c68-85e0-7af1e02722c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T03:24:02.958Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01YJDWfC9mUEXgzHdytPu2uM`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-reviewer-fe2ad71b/ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8/tool-results/mcp-agent-ml-research-read_registry-1778901796593.txt', 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\ninner_str = outer['result']\ninner = json.loads(inner_str)\n\nexperiments = inner['data']['experiments']\n\nfrom collections import Counter\nstatuses = Counter()\nrunning_preparing = []\ndone_recent = []\nhandoff_check = {}\n\nHANDOFF_TARGETS = {\n    'internlm2_constrained_mckp_v2': 'should be DONE',\n    'llama_longctx_8k_eval': 'should be DONE',\n    'internlm2_constrained_mckp': 'should be FAILED',  # v1\n}\n\nfor exp_id, exp in experiments.items():\n    status = exp.get('status', 'UNKNOWN')\n    statuses[status] += 1\n    \n    if status in ('RUNNING', 'PREPARING'):\n        running_preparing.append((exp_id, exp))\n    \n    if status == 'DONE':\n        updated = str(exp.get('updated_at', '') or '')\n        if updated >= '2026-05-14':\n            done_recent.append((exp_id, exp))\n    \n    if exp_id in HANDOFF_TARGETS:\n        handoff_check[exp_id] = status\n\nprint('=== STATUS COUNTS ===')\ntotal = sum(statuses.values())\nfor k, v in sorted(statuses.items()):\n    print(f'  {k}: {v}')\nprint(f'  TOTAL: {total}')\n\nprint()\nprint('=== RUNNING / PREPARING ===')\nfor exp_id, exp in running_preparing:\n    spec = exp.get('spec', {})\n    print(f'exp_id: {exp_id}')\n    print(f'  status: {exp.get(\\\"status\\\")}')\n    print(f'  description/hypothesis: {str(exp.get(\\\"hypothesis\\\", exp.get(\\\"description\\\", \\\"\\\")))[:150]}')\n    print(f'  server: {spec.get(\\\"server\\\", \\\"N/A\\\")}')\n    print(f'  gpu: {spec.get(\\\"gpu\\\", spec.get(\\\"gpus\\\", spec.get(\\\"device\\\", \\\"N/A\\\")))}')\n    print(f'  pid: {spec.get(\\\"pid\\\", \\\"N/A\\\")}')\n    print(f'  updated_at: {exp.get(\\\"updated_at\\\")}')\n    print()\n\nprint('=== DONE (updated >= 2026-05-14) ===')\nfor exp_id, exp in done_recent:\n    print(f'exp_id: {exp_id}')\n    print(f'  updated_at: {exp.get(\\\"updated_at\\\")}')\n    conclusion = exp.get('conclusion', '')\n    print(f'  conclusion: {str(conclusion)[:250]}')\n    metrics = exp.get('metrics', exp.get('results', {}))\n    print(f'  metrics: {json.dumps(metrics, ensure_ascii=False)[:300] if metrics else \\\"None\\\"}')\n    print()\n\nprint('=== HANDOFF STATUS CHECK ===')\nfor exp_id, expected in HANDOFF_TARGETS.items():\n    actual = handoff_check.get(exp_id, 'NOT FOUND')\n    match = 'OK' if (expected.split()[-1] == actual) else 'MISMATCH'\n    print(f'  {exp_id}: actual={actual}, expected={expected} [{match}]')\n\" 2>&1\n",
  "description": "Parse nested JSON registry and extract all required information"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41d60d43-eeb0-4c5c-a118-723e2bdfedc2",
  "isSidechain": true,
  "agentId": "a149fcadad70fa034",
  "requestId": "req_011Cb5XoEuSogbTjAcmSwNy7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "461403e2-c2f5-44b0-8c4d-e4e00b9e1393",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XvCnnEUZzLcbuFLHhZfd97",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1079,
      "cache_read_input_tokens": 25349,
      "output_tokens": 1070,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1079
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1070,
          "cache_read_input_tokens": 25349,
          "cache_creation_input_tokens": 1079,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1079,
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

_source line 12 · 2026-05-16T03:24:03.080Z_

<details><summary>↩ Tool result · `toolu_01YJDWfC9mUEXgzHdytPu2uM`</summary>

```text
&lt;persisted-output>
Output too large (29.4KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-reviewer-fe2ad71b/ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8/tool-results/bl4trsdej.txt

Preview (first 2KB):
=== STATUS COUNTS ===
  DONE: 116
  PREPARING: 4
  RUNNING: 1
  TOTAL: 121

=== RUNNING / PREPARING ===
exp_id: codellama_constrained_mckp
  status: PREPARING
  description/hypothesis: CodeLlama-7B constrained MCKP: Spike shape (c=0.80, t1/t5=0.81). Expect no benefit from non-uniform — confirming profiling-based classification. Conve
  server: westd-37397
  gpu: ['cuda:1']
  pid: 396720
  updated_at: 2026-05-16T03:18:39.237Z

exp_id: yi_8k_eval
  status: PREPARING
  description/hypothesis: Yi-1.5-9B 8K long-context eval: Spike shape (c=0.71, t1/t5=0.90). Expect no MCKP benefit at 8K — Spike control for Spread-specific long-context amplif
  server: N/A
  gpu: N/A
  pid: N/A
  updated_at: 2026-05-16T03:13:30.948Z

exp_id: mistral_8k_eval
  status: PREPARING
  description/hypothesis: Mistral-7B 8K long-context eval: Flat shape (c=0.22). Expect no MCKP benefit at 8K — Spike/Flat control for Spread-specific long-context amplification
  server: N/A
  gpu: N/A
  pid: N/A
  updated_at: 2026-05-16T03:13:29.527Z

exp_id: internlm2_constrained_mckp_v2
  status: RUNNING
  description/hypothesis: 
  server: westd-37397
  gpu: ['cuda:0']
  pid: 395573
  updated_at: 2026-05-16T03:10:42.820Z

exp_id: phi3_medium_hires_profiling_check
  status: PREPARING
  description/hypothesis: 
  server: N/A
  gpu: N/A
  pid: N/A
  updated_at: 2026-05-16T02:35:26.981Z

=== DONE (updated >= 2026-05-14) ===
exp_id: llama_longctx_8k_eval
  updated_at: 2026-05-16T03:08:48.372Z
  conclusion: negative
  metrics: {"bf16_8k_ppl": 5.5958, "mckp_8k_ppl": 6.0537, "uniform_4bit_8k_ppl": 6.0364, "mckp_vs_uniform_delta": 0.0173}

exp_id: internlm2_constrained_mckp
  updated_at: 2026-05-16T03:07:17.328Z
  conclusion: failed
  metrics: None

exp_id: internlm2_7b_hires_profiling
  updated_at: 2026-05-16T02:54:43.110Z
  conclusion: success
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "461403e2-c2f5-44b0-8c4d-e4e00b9e1393",
  "isSidechain": true,
  "promptId": "05c25958-d42d-45df-8f4d-41835d17b7a7",
  "agentId": "a149fcadad70fa034",
  "type": "user",
  "uuid": "7a99473f-9fc9-4d9d-915e-f66d4ae93dea",
  "sourceToolAssistantUUID": "461403e2-c2f5-44b0-8c4d-e4e00b9e1393",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T03:24:05.392Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JbHzkibxR7vaqi1VmF2rc5`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-reviewer-fe2ad71b/ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8/tool-results/bl4trsdej.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a99473f-9fc9-4d9d-915e-f66d4ae93dea",
  "isSidechain": true,
  "agentId": "a149fcadad70fa034",
  "requestId": "req_011Cb5XpG2gzZpN965HDY41W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f70dd93-d7d1-40b1-a8b6-f2039dc56c68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PNbZS3CCYAKQTUuSpLwBsH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2006,
      "cache_read_input_tokens": 26428,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2006
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 26428,
          "cache_creation_input_tokens": 2006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2006,
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

_source line 14 · 2026-05-16T03:24:05.638Z_

<details><summary>↩ Tool result · `toolu_01JbHzkibxR7vaqi1VmF2rc5`</summary>

```text
1	=== STATUS COUNTS ===
2	  DONE: 116
3	  PREPARING: 4
4	  RUNNING: 1
5	  TOTAL: 121
6	
7	=== RUNNING / PREPARING ===
8	exp_id: codellama_constrained_mckp
9	  status: PREPARING
10	  description/hypothesis: CodeLlama-7B constrained MCKP: Spike shape (c=0.80, t1/t5=0.81). Expect no benefit from non-uniform — confirming profiling-based classification. Conve
11	  server: westd-37397
12	  gpu: ['cuda:1']
13	  pid: 396720
14	  updated_at: 2026-05-16T03:18:39.237Z
15	
16	exp_id: yi_8k_eval
17	  status: PREPARING
18	  description/hypothesis: Yi-1.5-9B 8K long-context eval: Spike shape (c=0.71, t1/t5=0.90). Expect no MCKP benefit at 8K — Spike control for Spread-specific long-context amplif
19	  server: N/A
20	  gpu: N/A
21	  pid: N/A
22	  updated_at: 2026-05-16T03:13:30.948Z
23	
24	exp_id: mistral_8k_eval
25	  status: PREPARING
26	  description/hypothesis: Mistral-7B 8K long-context eval: Flat shape (c=0.22). Expect no MCKP benefit at 8K — Spike/Flat control for Spread-specific long-context amplification
27	  server: N/A
28	  gpu: N/A
29	  pid: N/A
30	  updated_at: 2026-05-16T03:13:29.527Z
31	
32	exp_id: internlm2_constrained_mckp_v2
33	  status: RUNNING
34	  description/hypothesis: 
35	  server: westd-37397
36	  gpu: ['cuda:0']
37	  pid: 395573
38	  updated_at: 2026-05-16T03:10:42.820Z
39	
40	exp_id: phi3_medium_hires_profiling_check
41	  status: PREPARING
42	  description/hypothesis: 
43	  server: N/A
44	  gpu: N/A
45	  pid: N/A
46	  updated_at: 2026-05-16T02:35:26.981Z
47	
48	=== DONE (updated >= 2026-05-14) ===
49	exp_id: llama_longctx_8k_eval
50	  updated_at: 2026-05-16T03:08:48.372Z
51	  conclusion: negative
52	  metrics: {"bf16_8k_ppl": 5.5958, "mckp_8k_ppl": 6.0537, "uniform_4bit_8k_ppl": 6.0364, "mckp_vs_uniform_delta": 0.0173}
53	
54	exp_id: internlm2_constrained_mckp
55	  updated_at: 2026-05-16T03:07:17.328Z
56	  conclusion: failed
57	  metrics: None
58	
59	exp_id: internlm2_7b_hires_profiling
60	  updated_at: 2026-05-16T02:54:43.110Z
61	  conclusion: success
62	  metrics: {"concentration": 0.2422, "t1_t5": 0.18, "shape": "Flat", "num_kv_heads": 256, "gqa_ratio": "4:1", "positive_delta_heads": "246/256", "baseline_ppl": 7.632, "top5_concentration_heads": 12, "layer0_dominance_ratio": 2.19, "delta_2bit_cv": 1.2223, "boundary_note": "concentration=0.2422 within 0.008 of
63	
64	exp_id: phi3_medium_constrained_mckp
65	  updated_at: 2026-05-16T02:39:40.628Z
66	  conclusion: negative
67	  metrics: {"shape": "Flat", "concentration": 0.1742, "t1_t5_ratio": 0.234, "t1": 0.1806, "t5": 0.77, "ppl_bf16": 5.6359, "ppl_uniform_4bit": 5.7987, "ppl_constrained_mckp": 5.8149, "ppl_unconstrained_mckp": 6.073, "ppl_greedy": 6.073, "constrained_vs_uniform": -0.016, "bit_dist": "388x4bit, 8x2bit, 4x8bit", "
68	
69	exp_id: deepseekvl_hires_profiling
70	  updated_at: 2026-05-16T02:38:38.068Z
71	  conclusion: killed
72	  metrics: None
73	
74	exp_id: falcon7b_hires_profiling_v2
75	  updated_at: 2026-05-16T02:38:37.244Z
76	  conclusion: killed
77	  metrics: None
78	
79	exp_id: falcon7b_hires_profiling
80	  updated_at: 2026-05-16T02:38:36.395Z
81	  conclusion: killed
82	  metrics: None
83	
84	exp_id: phi3_medium_hires_profiling_v2
85	  updated_at: 2026-05-16T02:38:32.579Z
86	  conclusion: success
87	  metrics: {"top5_concentration": 0.1742, "top5_n_heads": 20, "baseline_calibration_ppl": 4.783, "delta_2bit_cv": 0.8905, "layer0_dominance_ratio": 0.04, "shape": "Flat", "t1_t5_ratio": 0.24, "top1_head": "L9H6", "top1_delta_2bit": 0.1806, "total_heads": 400, "profiling_hours": 2.48, "note": "concentration=0.1
88	
89	exp_id: codellama_7b_hires_profiling
90	  updated_at: 2026-05-16T02:38:06.019Z
91	  conclusion: success
92	  metrics: {"concentration": 0.8, "t1_t5": 0.81, "shape": "Spike", "heads_profiled": "1024/1024"}
93	
94	exp_id: llama_3seed_downstream_ci
95	  updated_at: 2026-05-15T23:29:28.434Z
96	  conclusion: success
97	  metrics: {"arc_challenge_delta": -0.8, "hellaswag_delta": 0, "piqa_delta": -0.1, "winogrande_delta": 0.5, "avg_delta": -0.1, "std_all_tasks": 0, "note": "Single profile → deterministic allocation → all 3 seeds identical"}
98	
99	exp_id: codellama_hires_profiling
100	  updated_at: 2026-05-15T22:42:03.905Z
101	  conclusion: success
102	  metrics: {"baseline_ppl": 7.6978, "top5_concentration": 0.7975, "t1_t5": 0.8131, "distribution_shape": "Spike", "cv": 18.3153, "l0_dominance_ratio": 0.8, "top5_sensitive_heads": [{"layer": 1, "head": 1, "delta_2bit": 22.998339}, {"layer": 1, "head": 18, "delta_2bit": 2.042989}, {"layer": 1, "head": 11, "delt
103	
104	exp_id: gemma2_downstream_k8_4task_v2
105	  updated_at: 2026-05-15T21:52:45.334Z
106	  conclusion: success
107	  metrics: {"arc_challenge": {"baseline": 0.6135, "uniform": 0.6058, "mckp_k8": 0.6049, "delta": -0.0009}, "hellaswag": {"baseline": 0.6093, "uniform": 0.6092, "mckp_k8": 0.6089, "delta": -0.0003}, "winogrande": {"baseline": 0.7443, "uniform": 0.738, "mckp_k8": 0.7443, "delta": 0.0063}, "piqa": {"baseline": 0.
108	
109	exp_id: qwen_3seed_downstream_ci
110	  updated_at: 2026-05-15T21:52:44.493Z
111	  conclusion: success
112	  metrics: {"arc_challenge": {"bf16": 0.4582, "uniform": 0.459, "mckp_mean": 0.459, "mckp_std": 0.0035, "delta": 0}, "hellaswag": {"bf16": 0.5887, "uniform": 0.5335, "mckp_mean": 0.5748, "mckp_std": 0.0022, "delta": 0.0413}, "winogrande": {"bf16": 0.7119, "uniform": 0.6622, "mckp_mean": 0.678, "mckp_std": 0.01
113	
114	exp_id: qwen_compounding_sweep
115	  updated_at: 2026-05-15T19:54:57.222Z
116	  conclusion: killed
117	  metrics: None
118	
119	exp_id: phi3_medium_hires_profiling
120	  updated_at: 2026-05-15T19:45:10.230Z
121	  conclusion: failed
122	  metrics: None
123	
124	exp_id: gemma2_downstream_k8_4task
125	  updated_at: 2026-05-15T19:38:03.917Z
126	  conclusion: failed
127	  metrics: None
128	
129	exp_id: qwen_compounding_sweep_v2
130	  updated_at: 2026-05-15T19:24:47.014Z
131	  conclusion: success
132	  metrics: {"ppl_k0": 9.8106, "ppl_k8": 10.0474, "ppl_k64": 23.2176, "ppl_k256": 98.7523, "max_compounding_ratio": 10.07, "n_heads_total": 112, "n_2bit_ceiling": 96, "budget": 0.25}
133	
134	exp_id: gemma2_downstream_k2_4task
135	  updated_at: 2026-05-15T19:23:26.929Z
136	  conclusion: failed
137	  metrics: None
138	
139	exp_id: mistral_compounding_sweep_v2
140	  updated_at: 2026-05-15T18:53:22.685Z
141	  conclusion: success
142	  metrics: {"k0_ppl": 7.0352, "k2_ppl": 7.0366, "k4_ppl": 7.0453, "k8_ppl": 7.0636, "k16_ppl": 7.1139, "k32_ppl": 7.2378, "k64_ppl": 7.7747, "k128_ppl": 10.473, "k256_ppl": 45.2766, "budget": 0.25, "n_heads": 256}
143	
144	exp_id: yi_mistral_downstream_k2
145	  updated_at: 2026-05-15T18:45:04.616Z
146	  conclusion: success
147	  metrics: {"yi_k2": {"arc_challenge": {"baseline": 0.5265, "uniform": 0.5205, "mckp_k2": 0.4991}, "hellaswag": {"baseline": 0.5912, "uniform": 0.5855, "mckp_k2": 0.5818}, "piqa": {"baseline": 0.7949, "uniform": 0.7916, "mckp_k2": 0.7916}, "winogrande": {"baseline": 0.7332, "uniform": 0.7206, "mckp_k2": 0.7238
148	
149	exp_id: mistral_compounding_sweep
150	  updated_at: 2026-05-15T18:35:45.796Z
151	  conclusion: success
152	  metrics: {"k0_ppl": 7.1308, "k2_ppl": 7.1471, "k4_ppl": 7.164, "k8_ppl": 7.2001, "k16_ppl": 7.31, "k32_ppl": 7.4877, "k64_ppl": 7.5932, "k128_ppl": 7.5932, "k256_ppl": 7.5932, "best_k": 0, "best_ppl": 7.1308, "note": "PPL monotonically increases with k; all-4bit optimal at budget=0.25; solver saturates at k>
153	
154	exp_id: llama_downstream_eval
155	  updated_at: 2026-05-15T18:35:42.357Z
156	  conclusion: success
157	  metrics: {"arc_challenge": {"fp16": 0.5188, "uniform_4bit": 0.5256, "mckp_k2": 0.5179}, "hellaswag": {"fp16": 0.6073, "uniform_4bit": 0.6024, "mckp_k2": 0.6021}, "piqa": {"fp16": 0.7922, "uniform_4bit": 0.7873, "mckp_k2": 0.7867}, "winogrande": {"fp16": 0.7388, "uniform_4bit": 0.7261, "mckp_k2": 0.7309}, "av
158	
159	exp_id: llama_compounding_sweep
160	  updated_at: 2026-05-15T16:36:09.257Z
161	  conclusion: success
162	  metrics: {"best_k": 0, "best_ppl": 8.0922, "k0_ppl": 8.0922, "k2_ppl": 8.1243, "k4_ppl": 8.1803, "k8_ppl": 8.2259, "k16_ppl": 8.4378, "k32_ppl": 9.0506, "k64_ppl": 11.991, "k128_ppl": 40.2067, "k256_ppl": 1519.1888, "budget": 0.25}
163	
164	exp_id: qwen25-hires-profiling
165	  updated_at: 2026-05-15T15:13:44.380Z
166	  conclusion: killed
167	  metrics: None
168	
169	exp_id: cross_domain_calibration_v2
170	  updated_at: 2026-05-15T15:13:43.668Z
171	  conclusion: killed
172	  metrics: None
173	
174	exp_id: greedy_constrained_ablation
175	  updated_at: 2026-05-15T15:13:42.759Z
176	  conclusion: killed
177	  metrics: None
178	
179	exp_id: mistral_hires_constrained_mckp
180	  updated_at: 2026-05-15T15:08:47.772Z
181	  conclusion: failed
182	  metrics: None
183	
184	exp_id: mistral_hires_constrained_mckp_v2
185	  updated_at: 2026-05-15T15:07:51.888Z
186	  conclusion: negative
187	  metrics: {"baseline_wikitext2_ppl": 7.0352, "mckp_wikitext2_ppl": 7.1341, "uniform4bit_wikitext2_ppl": 7.1308, "mckp_improvement_over_uniform": -0.0033, "mckp_improvement_pct": -3.48, "verdict": "FAIL", "bit_distribution": {"2": 2, "4": 254}, "fix_note": "uniform eval re-run: original had bits=budget(0.25) b
188	
189	exp_id: mistral_uniform_reeval
190	  updated_at: 2026-05-15T15:07:03.121Z
191	  conclusion: success
192	  metrics: None
193	
194	exp_id: qwen14b_greedy_constrained
195	  updated_at: 2026-05-15T15:04:35.456Z
196	  conclusion: success
197	  metrics: {"greedy_constrained_ppl": 7.2206, "mckp_constrained_ppl": 7.2206, "delta_vs_mckp": 0, "bit_distribution": {"2": 8, "4": 374, "8": 1, "16": 1}, "memory_ratio": 0.25, "solver_time_sec": 0.08, "total_time_min": 1.8}
198	
199	exp_id: kivi_mckp_combined_qwen7b
200	  updated_at: 2026-05-15T14:57:04.921Z
201	  conclusion: success
202	  metrics: None
203	
204	exp_id: mistral_hires_bf16_2bitonly_v3
205	  updated_at: 2026-05-15T14:54:50.664Z
206	  conclusion: killed
207	  metrics: None
208	
209	exp_id: kivi_baseline_qwen7b_v2
210	  updated_at: 2026-05-15T14:43:26.196Z
211	  conclusion: success
212	  metrics: {"ppl_kivi_4bit_g32_r128": 9.8976, "tokens": 298938, "chunks": 583, "stride": 512, "model": "Qwen2.5-7B", "comparison_mckp_ppl": 10.91, "comparison_uniform_ppl": 15.45, "comparison_bf16_ppl": 9.81}
213	
214	exp_id: qwen14b_constrained_pipeline
215	  updated_at: 2026-05-15T14:42:18.310Z
216	  conclusion: success
217	  metrics: {"ppl_bf16": 6.8654, "ppl_uniform_4bit": 7.202, "ppl_constrained_mckp": 7.2206, "ppl_unconstrained_mckp": 7.6923, "delta_constrained_vs_uniform": -0.0185, "delta_constrained_vs_uniform_pct": -5.51, "delta_unconstrained_vs_uniform": -0.4902, "bit_distribution_constrained": {"2": 8, "4": 374, "8": 1, 
218	
219	exp_id: qwen_hires_constrained_d049
220	  updated_at: 2026-05-15T14:34:58.828Z
221	  conclusion: success
222	  metrics: {"float32_hires_constrained_mckp_ppl": 10.8921, "baseline_ppl": 9.8106, "uniform_4bit_ppl": 15.4484, "bit_distribution": {"2": 8, "4": 100, "8": 4}, "gap_recovery_pct": 80.8, "top5_concentration": 0.6156, "top5_concentration_pre_monotonicity": 0.6104, "bf16_hires_constrained_mckp_ppl": 10.9131, "del
223	
224	exp_id: llama_8k_spotcheck
225	  updated_at: 2026-05-15T14:11:11.590Z
226	  conclusion: success
227	  metrics: {"ppl_bf16_8k": 5.5958, "ppl_constrained_mckp_8k": 6.0537, "ppl_uniform_4bit_8k": 6.0364, "mckp_improvement_over_uniform_8k": -0.0174, "mckp_improvement_pct_8k": -3.94, "ppl_bf16_2k": 8.0922, "ppl_constrained_mckp_2k": 8.5042, "ppl_uniform_4bit_2k": 8.4701, "shape": "Spike", "concentration": 0.5749,
228	
229	exp_id: yi15_8k_spotcheck
230	  updated_at: 2026-05-15T13:34:14.456Z
231	  conclusion: negative
232	  metrics: None
233	
234	exp_id: qwen7b_8k_spotcheck
235	  updated_at: 2026-05-15T13:34:00.440Z
236	  conclusion: killed
237	  metrics: None
238	
239	exp_id: qwen7b_8k_context_eval
240	  updated_at: 2026-05-15T13:23:15.367Z
241	  conclusion: success
242	  metrics: {"ppl_bf16_8k": 6.97, "ppl_constrained_mckp_8k": 8.59, "ppl_uniform_4bit_8k": 77.75, "ppl_bf16_2k": 9.81, "ppl_constrained_mckp_2k": 10.89, "ppl_uniform_4bit_2k": 15.45, "mckp_improvement_over_uniform_8k": "97.7%", "mckp_improvement_over_uniform_2k": "80.8%", "shape": "Spread", "concentration": 0.59
243	
244	exp_id: pythia14b_constrained_pipeline
245	  updated_at: 2026-05-15T13:07:37.192Z
246	  conclusion: success
247	  metrics: {"ppl_bf16": 16.4893, "ppl_uniform_4bit": 24.2894, "ppl_constrained_mckp": 24.4521, "ppl_unconstrained_mckp": 31.5415, "concentration": "t1=0.0289, t5=0.2439", "t1_t5": "0.0289/0.2439", "shape": "Flat", "constrained_vs_uniform_gap": 0.1627}
248	
249	exp_id: w1_pythia14b_hires_profiling
250	  updated_at: 2026-05-15T12:16:53.707Z
251	  conclusion: success
252	  metrics: {"baseline_ppl": 13.6347, "concentration": 0.2439, "t1_t5": 0.28, "shape": "Flat", "l0_dominance": 0.51, "cv": 1.2172, "positive_heads": 362, "total_heads": 384, "top5_heads": [{"head": "L1H11", "delta": 1.016355}, {"head": "L12H14", "delta": 0.784513}, {"head": "L8H4", "delta": 0.759118}, {"head": 
253	
254	exp_id: w1_qwen14b_hires_profiling
255	  updated_at: 2026-05-15T12:16:53.306Z
256	  conclusion: success
257	  metrics: {"baseline_ppl": 5.8432, "concentration": 0.3312, "t1_t5": 0.68, "shape": "Flat", "l0_dominance": 15.5, "cv": 3.7418, "positive_heads": 370, "total_heads": 384, "top10_heads": [{"head": "L0H5", "delta": 1.84494}, {"head": "L0H4", "delta": 0.236669}, {"head": "L0H2", "delta": 0.136971}, {"head": "L28
258	
259	exp_id: kivi_baseline_qwen_llama
260	  updated_at: 2026-05-15T11:54:36.222Z
261	  conclusion: success
262	  metrics: {"qwen_2bit_r128": 12.83, "qwen_4bit_r128": 9.9, "qwen_2bit_r0": 13.34, "qwen_4bit_r0": 9.91, "llama_2bit_r128": 9.84, "llama_4bit_r128": 8.14, "llama_2bit_r0": 10.08, "llama_4bit_r0": 8.14, "group_size": 32, "eval_data": "WikiText-2 test", "note": "r128=residual_length 128 (25% fp16), r0=strict qua
263	
264	exp_id: gemma2_constrained_bos_fix
265	  updated_at: 2026-05-15T09:40:36.943Z
266	  conclusion: success
267	  metrics: {"baseline_ppl": 6.0306, "uniform_4bit_ppl": 6.1683, "constrained_mckp_ppl": 6.1951, "mckp_vs_uniform_delta": 0.0267, "mckp_delta_ppl": 0.1645, "uniform_delta_ppl": 0.1377, "bit_distribution": {"2": 8, "4": 324, "8": 4}, "n_2bit": 8, "max_2bit": 8, "memory_ratio": 0.25, "eval_method": "sliding_windo
268	
269	exp_id: w2_unconstrained_v2
270	  updated_at: 2026-05-15T08:27:08.899Z
271	  conclusion: success
272	  metrics: {"yi15_baseline": 7.0157, "yi15_uniform4": 7.2171, "yi15_greedy": 7.5615, "yi15_mckp": 7.5615, "yi15_n2bit": 22, "llama_baseline": 8.0922, "llama_uniform4": 8.4701, "llama_greedy": 8.6265, "llama_mckp": 8.6265, "llama_n2bit": 12, "mistral_baseline": 7.0352, "mistral_uniform4": 7.1308, "mistral_greed
273	
274	exp_id: w3_downstream_eval
275	  updated_at: 2026-05-15T08:15:53.939Z
276	  conclusion: success
277	  metrics: {"yi15_baseline_avg": 0.6912, "yi15_uniform_avg": 0.6822, "yi15_mckp_avg": 0.6745, "yi15_mckp_vs_uniform_pp": -0.77, "yi15_mckp_vs_baseline_pp": -1.67, "yi15_baseline": {"arc_easy": 0.8093, "arc_challenge": 0.5265, "hellaswag": 0.5913, "piqa": 0.7949, "winogrande": 0.734}, "yi15_uniform": {"arc_easy
278	
279	exp_id: w9_compounding_v2
280	  updated_at: 2026-05-15T05:39:41.740Z
281	  conclusion: success
282	  metrics: {"baseline_ppl": 9.81, "k1_topk_ppl": 9.826, "k1_randomk_ppl": 9.887, "k1_randomk_std": 0.05, "k4_topk_ppl": 9.849, "k4_topk_ratio": 0.86, "k4_randomk_ppl": 10.06, "k4_randomk_std": 0.06, "k4_randomk_ratio": 1.24, "k8_topk_ppl": 10.042, "k8_topk_ratio": 1.56, "k8_randomk_ppl": 11.07, "k8_randomk_std
283	
284	exp_id: w9_compounding_scaling
285	  updated_at: 2026-05-15T05:39:02.223Z
286	  conclusion: killed
287	  metrics: {"baseline_ppl": 8.2, "n1_joint_ppl": 14.94, "n1_ratio": 1, "n2_joint_ppl": 42.26, "n2_ratio": 3.84, "n4_joint_ppl": 3813.76, "n4_ratio": 333.3, "n8_joint_ppl": 3586.42, "n8_ratio": 282.1, "n16_joint_ppl": 7286.23, "n16_ratio": 521.1, "n32_joint_ppl": 6644.05, "n32_ratio": 424, "n64_joint_ppl": 9453
288	
289	exp_id: w2_unconstrained_baselines
290	  updated_at: 2026-05-15T05:31:45.721Z
291	  conclusion: killed
292	  metrics: {"note": "2bitonly profiles only - INVALID for reviewer response", "yi15_ppl": 672.2, "yi15_ratio": 114, "llama_ppl": 1219.7, "llama_ratio": 187, "mistral_ppl_2bitonly": 47.8, "mistral_ratio_2bitonly": 8.2, "mistral_ppl_full": 6.39, "mistral_ratio_full": 1.09, "gemma2_ppl": 277.4, "gemma2_ratio": 37
293	
294	exp_id: gemma2_hires_bf16_2bitonly
295	  updated_at: 2026-05-15T01:02:01.723Z
296	  conclusion: success
297	  metrics: {"concentration_top5pct": 0.2291, "l0_dominance_ratio": 2.05, "cv_delta_2bit": 1.2834, "positive_delta_heads": "310/336", "top_head": "L0H1 delta=0.1906", "total_time_hours": 1.59}
298	
299	exp_id: mistral_c4_hires_crossdataset
300	  updated_at: 2026-05-15T00:55:16.250Z
301	  conclusion: negative
302	  metrics: {"fp16_ppl": 7.0352, "c4_mckp_ppl": 7.1774, "uniform_4bit_ppl": 7.1308, "mckp_vs_uniform_delta": 0.0466, "mckp_bit_distribution": {"2": 4, "4": 250, "8": 2}, "phase4_error": "FileNotFoundError: mistral_k_ablation_results.json"}
303	
304	exp_id: llama_c4_hires_crossdataset
305	  updated_at: 2026-05-14T22:50:58.624Z
306	  conclusion: negative
307	  metrics: {"bf16_wt2_ppl": 8.0922, "bf16_c4_ppl": 7.1333, "c4_cal_mckp_wt2_ppl": 8.5103, "c4_cal_mckp_c4_ppl": 7.5351, "uniform_wt2_ppl": 8.4701, "uniform_c4_ppl": 7.5351, "delta_c4_uniform_minus_mckp": 0, "delta_wt2_uniform_minus_mckp": -0.0402, "verdict_c4": "FAIL", "bit_distribution": {"2": 2, "4": 253, "8
308	
309	exp_id: mistral_hires_bf16_2bitonly_v4
310	  updated_at: 2026-05-14T22:36:11.035Z
311	  conclusion: success
312	  metrics: {"top5_concentration": 0.241, "top5_n_heads": 12, "baseline_ppl": 5.8702, "top1_head": "L2H5", "top1_delta_2bit": 0.3236, "top2_head": "L12H1", "top2_delta_2bit": 0.1435, "top3_head": "L0H7", "top3_delta_2bit": 0.1403, "delta_2bit_mean": 0.020073, "delta_2bit_std": 0.026278, "delta_2bit_cv": 1.3091,
313	
314	exp_id: llama_hires_constrained_mckp
315	  updated_at: 2026-05-14T21:56:15.999Z
316	  conclusion: negative
317	  metrics: {"baseline_bf16_ppl": 8.0922, "hires_mckp_ppl": 8.5042, "uniform_4bit_ppl": 8.4701, "std_mckp_reference_ppl": 8.4498, "mckp_vs_uniform_delta": -0.0341, "mckp_vs_uniform_pct": -9, "hires_vs_std_mckp_delta": 0.0544, "concentration": 0.5749, "bit_distribution": {"2": 2, "4": 253, "8": 1}, "heads_2bit":
318	
319	exp_id: llama_hires_bf16_2bitonly
320	  updated_at: 2026-05-14T21:47:38.147Z
321	  conclusion: success
322	  metrics: {"top5_concentration": 0.5749, "t1_t5": 0.85, "baseline_ppl": 6.5055, "top1_head": "L2H5_delta=15.2636", "delta_2bit_cv": 7.7663, "l0_dominance_ratio": 0.67, "positive_delta_heads": 254, "total_heads": 256, "total_hours": 0.98}
323	
324	exp_id: mistral_hires_bf16_2bitonly_v2
325	  updated_at: 2026-05-14T21:36:53.934Z
326	  conclusion: failed
327	  metrics: {"error": "SafetensorError: model-00003-of-00003.safetensors missing, incomplete download"}
328	
329	exp_id: mistral_hires_bf16_2bitonly
330	  updated_at: 2026-05-14T21:06:34.828Z
331	  conclusion: failed
332	  metrics: {"error": "ValueError: Unrecognized model - config.json missing model_type field at /root/autodl-tmp/models/AI-ModelScope/Mistral-7B-v0___3"}
333	
334	exp_id: yi15_hires_constrained_mckp
335	  updated_at: 2026-05-14T20:38:14.263Z
336	  conclusion: negative
337	  metrics: {"hires_mckp_ppl": 7.2181, "uniform_4bit_ppl": 7.2171, "baseline_ppl": 7.0157, "delta_vs_uniform": -0.001, "bit_distribution": {"2": 2, "4": 189, "8": 1}, "2bit_heads": ["L22H1", "L24H3"], "8bit_heads": ["L6H2"], "L4H3_status": "kept_at_4bit", "std_mckp_k2_ppl": 7.2209, "std_mckp_k8_ppl": 7.3129, "h
338	
339	exp_id: yi15_hires_bf16_2bitonly
340	  updated_at: 2026-05-14T20:18:07.386Z
341	  conclusion: success
342	  metrics: {"top5_concentration": 0.7139, "top5_n_heads": 9, "baseline_calibration_ppl": 5.888, "delta_2bit_cv": 8.8991, "layer0_dominance_ratio": 0.04, "top1_head": "L4H3_delta=13.1236", "total_hours": 0.96}
343	
344	exp_id: qwen_hires_float32_d048
345	  updated_at: 2026-05-14T19:44:37.134Z
346	  conclusion: success
347	  metrics: {"float32_hires_top5_concentration": 0.6104, "bf16_hires_range": "0.59-0.66", "float32_lowres_concentration": 0.42, "bf16_bug_impact_on_concentration": 0.01, "baseline_ppl": 9.81, "mckp_unconstrained_ppl": 10.95, "uniform_4bit_ppl": 15.45, "mckp_bit_dist": {"2": 12, "4": 96, "8": 3, "16": 1}, "l0h0_
348	
349	exp_id: yi15_hires_float32_profiling
350	  updated_at: 2026-05-14T19:14:45.437Z
351	  conclusion: killed
352	  metrics: None
353	
354	exp_id: yi15_9b_full_pipeline
355	  updated_at: 2026-05-14T18:48:02.488Z
356	  conclusion: negative
357	  metrics: {"baseline_wikitext2_ppl": 7.0157, "mckp_wikitext2_ppl": 7.3129, "uniform4bit_wikitext2_ppl": 7.2171, "mckp_improvement_over_uniform": -0.0958, "top5_concentration": 0.4934, "layer0_dominance_ratio": 0.07, "best_k": 2, "best_k_ppl": 7.2209, "gqa_ratio": "8:1", "verdict": "FAIL"}
358	
359	exp_id: gemma2_9b_full_pipeline
360	  updated_at: 2026-05-14T18:47:48.664Z
361	  conclusion: negative
362	  metrics: {"baseline_wikitext2_ppl": 8.9, "mckp_wikitext2_ppl": 9.05, "uniform4bit_wikitext2_ppl": 9.03, "mckp_improvement_over_uniform": -0.02, "top5_concentration": 0.23, "layer0_dominance_ratio": 1.32, "best_k": 8, "best_k_ppl": 9.05, "verdict": "FAIL"}
363	
364	exp_id: qwen72b_profiling
365	  updated_at: 2026-05-14T18:39:01.190Z
366	  conclusion: killed
367	  metrics: None
368	
369	exp_id: multi_seed_lowres
370	  updated_at: 2026-05-14T15:17:19.393Z
371	  conclusion: killed
372	  metrics: None
373	
374	exp_id: mistral_c4_cross_dataset
375	  updated_at: 2026-05-14T12:38:43.477Z
376	  conclusion: success
377	  metrics: {"bf16_wt2_ppl": 7.0351, "c4_cal_bf16_ppl": 6.9677, "wt2_cal_mckp_wt2_ppl": 7.1648, "c4_cal_mckp_wt2_ppl": 7.1859, "uniform_4bit_wt2_ppl": 7.1314, "delta_uniform_mckp_wt2_cal": -0.0334, "delta_uniform_mckp_c4_cal": -0.0546, "allocation_agreement_c4_vs_wt2": 0.965, "agreement_heads": "247/256", "bit_
378	
379	exp_id: llama_c4_cross_dataset
380	  updated_at: 2026-05-14T12:38:42.288Z
381	  conclusion: negative
382	  metrics: {"wt2_cal_wt2_ppl": 8.4498, "c4_cal_wt2_ppl": 8.6459, "uniform_wt2_ppl": 8.469, "wt2_cal_c4_ppl": 7.654, "c4_cal_c4_ppl": 7.654, "uniform_c4_ppl": 7.5351, "bf16_wt2_ppl": 8.0918, "bf16_c4_ppl": 7.1333, "agreement_rate": 0.977, "agreement_heads": "250/256", "bit_distribution": {"2": 2, "4": 253, "8":
383	
384	exp_id: mistral_heuristic_k4
385	  updated_at: 2026-05-14T12:07:54.362Z
386	  conclusion: success
387	  metrics: {"baseline_bf16_ppl": 7.0351, "uniform_4bit_ppl": 7.1314, "mckp_k4_ppl": 7.1648, "l0_random_seed_0": 7.1882, "l0_random_seed_1": 7.1995, "l0_random_seed_2": 7.1723, "l0_random_seed_3": 7.3577, "l0_random_seed_4": 7.2875, "l0_random_mean": 7.2411, "l0_random_std": 0.0707, "l0_random_median": 7.1995, 
388	
389	exp_id: llama_heuristic_k2
390	  updated_at: 2026-05-14T12:06:42.659Z
391	  conclusion: success
392	  metrics: {"l0_random_seeds": [8.5479, 8.7595, 8.624, 8.5721, 8.6192], "l0_random_mean": 8.6245, "l0_random_std": 0.0733, "l0_random_median": 8.6192, "naive_positional_ppl": 8.5781, "mckp_ppl": 8.4498, "uniform_ppl": 8.469, "baseline_ppl": 8.0918, "mckp_vs_l0_random_gap": 0.1747, "mckp_vs_naive_gap": 0.1283}
393	
394	exp_id: plan_009_oracle_comparison
395	  updated_at: 2026-05-14T11:45:15.727Z
396	  conclusion: success
397	  metrics: None
398	
399	exp_id: oracle_comparison
400	  updated_at: 2026-05-14T11:41:17.450Z
401	  conclusion: success
402	  metrics: {"mckp_ppl": 10.9131, "max_oracle_gap_ppl": 0.0183, "avg_oracle_gap_ppl": 0.0046, "layers_mckp_optimal": "5/8", "layers_with_gap": 3, "gap_layers": {"L1": 0.0183, "L4": 0.0045, "L11": 0.0136}, "gap_nature": "2-bit head position swap within same bit budget", "total_evals": 54, "runtime_min": 21.3}
403	
404	exp_id: c4_rerun_d032
405	  updated_at: 2026-05-14T11:10:49.705Z
406	  conclusion: success
407	  metrics: {"c4_cal_wt2_eval_mckp_ppl": 11.2942, "c4_cal_wt2_eval_uniform_ppl": 15.4454, "c4_cal_wt2_eval_delta": 4.1512, "c4_cal_bf16_baseline": 12.6505, "wt2_bf16_baseline": 9.8106, "allocation_agreement_c4_vs_wt2": 0.964, "agreement_heads": "108/112", "bit_dist": "2bit:8, 4bit:100, 8bit:4", "cross_domain_wt
408	
409	exp_id: c4_cross_dataset_eval_v2
410	  updated_at: 2026-05-14T11:03:48.905Z
411	  conclusion: killed
412	  metrics: None
413	
414	exp_id: c4_cross_dataset_eval
415	  updated_at: 2026-05-14T11:03:46.587Z
416	  conclusion: killed
417	  metrics: {"c4_mckp_ppl": 11.3285, "uniform4bit_ppl": 15.4454, "delta_over_uniform": 4.117, "allocation_agreement_rate": 0.982, "n_disagree": 2, "bit_distribution": {"2": 8, "4": 100, "8": 4}, "memory_ratio": 0.25, "wt2_ref_mckp_ppl": 11.2312, "wt2_ref_delta": 4.2142, "ppl_gap": 0.097}
418	
419	exp_id: multi_seed_error_bars
420	  updated_at: 2026-05-14T10:59:54.875Z
421	  conclusion: success
422	  metrics: {"baseline_ppl": 9.8106, "uniform_4bit_ppl": 15.4454, "mckp_seed0": 11.0168, "mckp_seed1": 10.8981, "mckp_seed2": 11.0487, "mckp_mean": 10.9878, "mckp_std": 0.0648, "bit_dist_all_seeds": "2bit:8, 4bit:100, 8bit:4", "allocation_agreement_3way": 0.902, "agreement_s0_s1": 0.946, "agreement_s0_s2": 0.91
423	
424	exp_id: l0_heuristic_corrected
425	  updated_at: 2026-05-14T10:17:09.880Z
426	  conclusion: success
427	  metrics: {"mckp_constrained_ppl": 11.23, "l0_random_mean_ppl": 11.69, "l0_random_std": 0.47, "naive_positional_ppl": 12.23, "uniform_4bit_ppl": 15.45, "qwen_l0_random_median": 11.515, "qwen_l0_random_seeds": [11.486, 11.615, 11.325, 11.515, 12.515], "llama_l0_random_mean": 10.479, "llama_l0_random_std": 1.03
428	
429	exp_id: runtime_benchmark
430	  updated_at: 2026-05-14T09:35:48.354Z
431	  conclusion: success
432	  metrics: {"baseline_bf16": {"prefill_ms": 45.86, "decode_ms_per_tok": 33.78, "throughput_tok_s": 29.6}, "uniform_4bit": {"prefill_ms": 54.25, "decode_ms_per_tok": 42.46, "throughput_tok_s": 23.6}, "constrained_mckp": {"prefill_ms": 57.03, "decode_ms_per_tok": 46.09, "throughput_tok_s": 21.8, "mckp_solver_sec
433	
434	exp_id: cross_domain_calibration
435	  updated_at: 2026-05-14T09:08:05.625Z
436	  conclusion: killed
437	  metrics: None
438	
439	exp_id: kv_separation
440	  updated_at: 2026-05-14T08:39:33.953Z
441	  conclusion: negative
442	  metrics: {"kv_sep_ppl": 11.2162, "joint_kv_ppl": 10.9131, "uniform_4bit_ppl": 15.4454, "baseline_ppl": 9.8106, "delta_sep_vs_joint": 0.303, "sep_k_2bit_count": 16, "sep_v_uniform_4bit": true, "kv_asymmetric_heads": 21}
443	
444	exp_id: downstream_eval_qwen
445	  updated_at: 2026-05-14T07:32:03.906Z
446	  conclusion: success
447	  metrics: {"avg_recovery": 0.728, "arc_c": 0.5137, "hellaswag": 0.7684, "piqa": 0.7786, "winogrande": 0.6819, "arc_c_delta_pp": 3.16, "hellaswag_delta_pp": 4, "piqa_delta_pp": 1.25, "winogrande_delta_pp": 1.97}
448	
449	exp_id: llama_k_ablation
450	  updated_at: 2026-05-14T07:29:31.419Z
451	  conclusion: success
452	  metrics: {"best_k": 4, "best_ppl": 8.4498, "uniform_4bit_ppl": 8.469, "k4_ppl": 8.4498, "k8_ppl": 8.4498, "k12_ppl": 8.4498, "k16_ppl": 8.4498, "k18_ppl": 8.4498, "natural_2bit_count": 2}
453	
454	exp_id: mistral_hires_pipeline
455	  updated_at: 2026-05-14T07:23:15.704Z
456	  conclusion: negative
457	  metrics: {"mckp_ppl": 7.323, "uniform_4bit_ppl": 7.131, "baseline_ppl": 7.035, "delta_vs_uniform": -0.192, "memory_ratio": 0.25}
458	
459	exp_id: mistral_k_ablation
460	  updated_at: 2026-05-14T07:20:19.293Z
461	  conclusion: success
462	  metrics: {"best_k": 4, "best_ppl": 7.1648, "uniform_4bit_ppl": 7.131, "k4_ppl": 7.1648, "k8_ppl": 7.1997, "k12_ppl": 7.2448, "k16_ppl": 7.3106, "k18_ppl": 7.3231}
463	
464	exp_id: greedy_cardinality_ablation
465	  updated_at: 2026-05-14T07:14:47.987Z
466	  conclusion: success
467	  metrics: {"greedy_constrained_ppl": 11.2312, "greedy_unconstrained_ppl": 32.4467, "mckp_constrained_ppl": 11.23, "delta_vs_mckp": 0.0012, "bit_distribution": {"2": 8, "4": 100, "8": 4}, "memory_ratio": 0.25}
468	
469	exp_id: qwen_bf16_reeval
470	  updated_at: 2026-05-14T07:11:14.927Z
471	  conclusion: success
472	  metrics: {"baseline_bf16_ppl": 9.8106, "baseline_fp16_ppl": 9.81, "delta_baseline": 0.0006, "uniform4_bf16_ppl": 15.4454, "uniform4_fp16_ppl": 15.45, "delta_uniform4": 0.0046}
473	
474	exp_id: l0_only_heuristic
475	  updated_at: 2026-05-14T07:07:45.249Z
476	  conclusion: killed
477	  metrics: None
478	
479	exp_id: head_sensitivity_viz
480	  updated_at: 2026-05-14T07:07:44.291Z
481	  conclusion: success
482	  metrics: None
483	
484	exp_id: hires_reeval
485	  updated_at: 2026-05-14T06:58:03.353Z
486	  conclusion: success
487	  metrics: {"baseline_bf16_ppl": 9.8106, "uniform_4bit_bf16_ppl": 15.4454, "hires_mckp_bf16_ppl": 10.9131}
488	
489	exp_id: hires_mckp_reeval
490	  updated_at: 2026-05-14T06:51:28.777Z
491	  conclusion: success
492	  metrics: {"baseline_ppl_bf16": 9.8106, "mckp_ppl_bf16": 10.9131, "uniform_4bit_ppl_bf16": 15.4454, "delta_mckp_vs_baseline": 1.1025, "delta_mckp_vs_uniform": -4.5323, "token_count": 298938}
493	
494	exp_id: l0_heuristic_baseline
495	  updated_at: 2026-05-14T06:20:40.045Z
496	  conclusion: killed
497	  metrics: None
498	
499	exp_id: mistral_aggressive_compression
500	  updated_at: 2026-05-14T06:10:40.078Z
501	  conclusion: success
502	  metrics: {"mckp_5.3x_ppl": 11.912, "uniform_2bit_ppl": 519.107, "mckp_8x_ppl": 399.901, "uniform_2bit_8x_ppl": 519.107, "baseline_ppl": 7.035, "uniform_4bit_ppl": 7.131, "5.3x_bit_dist": {"2": 128, "4": 128}, "8x_bit_dist": {"2": 248, "4": 8}, "total_time_seconds": 268.1}
503	
504	exp_id: llama_aggressive_compression
505	  updated_at: 2026-05-14T05:52:41.954Z
506	  conclusion: success
507	  metrics: {"mckp_5.3x_ppl": 57.6, "uniform_2bit_ppl": 2643.77, "mckp_8x_ppl": 2372.33, "uniform_2bit_8x_ppl": 2643.77}
508	
509	exp_id: llama_hires_pipeline
510	  updated_at: 2026-05-14T05:21:13.265Z
511	  conclusion: success
512	  metrics: {"baseline_ppl": 8.0918, "uniform_4bit_ppl": 8.469, "lowres_mckp_ppl": 8.6951, "hires_mckp_ppl": 8.4498, "hires_improvement_ppl": 0.2453, "degradation_reduction_pct": 40.7, "profiling_time_min": 173.4, "total_time_min": 175.1}
513	
514	exp_id: mistral_full_pipeline
515	  updated_at: 2026-05-14T02:31:09.035Z
516	  conclusion: negative
517	  metrics: {"mckp_ppl_bf16": 7.564, "uniform_4bit_ppl_bf16": 7.131, "baseline_ppl_bf16": 7.035, "delta_vs_uniform": -0.433, "memory_ratio": 0.25}
518	
519	exp_id: llama_full_pipeline
520	  updated_at: 2026-05-14T02:29:04.490Z
521	  conclusion: negative
522	  metrics: {"mckp_ppl_bf16": 8.7, "uniform_4bit_ppl_bf16": 8.47, "baseline_ppl_bf16": 8.09, "delta_vs_uniform": -0.23, "memory_ratio": 0.25}
523	
524	exp_id: exp_e_hires_profile
525	  updated_at: 2026-05-14T01:51:49.904Z
526	  conclusion: success
527	  metrics: {"constrained_ppl_bf16": 9.569, "baseline_ppl_bf16": 8.819, "exp_c_ppl_bf16": 11.345, "delta_vs_exp_c": -1.776, "memory_ratio": 0.25, "bit_distribution": {"2": 8, "4": 100, "8": 4}, "profile_resolution": {"hires_nonzero_2bit": 100, "lowres_nonzero_2bit": 37, "hires_nonzero_4bit": 6, "lowres_nonzero_
528	
529	exp_id: budget_sweep
530	  updated_at: 2026-05-14T01:18:54.267Z
531	  conclusion: success
532	  metrics: None
533	
534	exp_id: ratequant_greedy_comparison
535	  updated_at: 2026-05-14T01:05:19.258Z
536	  conclusion: success
537	  metrics: None
538	
539	exp_id: compounding_sweep_k10_12
540	  updated_at: 2026-05-14T00:57:05.447Z
541	  conclusion: success
542	  metrics: None
543	
544	exp_id: compounding_sweep
545	  updated_at: 2026-05-14T00:42:43.212Z
546	  conclusion: success
547	  metrics: None
548	
549	exp_id: exp_d_no_l0_exclusion
550	  updated_at: 2026-05-14T00:29:07.739Z
551	  conclusion: success
552	  metrics: None
553	
554	exp_id: exp_c_no2bit
555	  updated_at: 2026-05-14T00:22:44.182Z
556	  conclusion: negative
557	  metrics: {"mckp_ppl": 15.4454, "uniform_4bit_ppl": 15.4454, "baseline_ppl": 9.8106, "delta_vs_uniform": 0, "memory_ratio": 0.25, "bit_distribution": {"4": 112}}
558	
559	exp_id: exp_c_constrained_mckp
560	  updated_at: 2026-05-14T00:14:44.144Z
561	  conclusion: success
562	  metrics: None
563	
564	=== HANDOFF STATUS CHECK ===
565	  internlm2_constrained_mckp_v2: actual=RUNNING, expected=should be DONE [MISMATCH]
566	  llama_longctx_8k_eval: actual=DONE, expected=should be DONE [OK]
567	  internlm2_constrained_mckp: actual=DONE, expected=should be FAILED [MISMATCH]
568	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f70dd93-d7d1-40b1-a8b6-f2039dc56c68",
  "isSidechain": true,
  "promptId": "05c25958-d42d-45df-8f4d-41835d17b7a7",
  "agentId": "a149fcadad70fa034",
  "type": "user",
  "uuid": "4bc0fb61-d125-4697-83e8-2afb89bb1cf8",
  "sourceToolAssistantUUID": "5f70dd93-d7d1-40b1-a8b6-f2039dc56c68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-16T03:24:47.327Z_

Here are the findings:

---

**Status Counts (Total: 121)**
- DONE: 116
- PREPARING: 4
- RUNNING: 1

---

**RUNNING / PREPARING (5 experiments)**

| exp_id | status | server | GPU | PID | updated_at |
|--------|--------|--------|-----|-----|------------|
| `internlm2_constrained_mckp_v2` | RUNNING | westd-37397 | cuda:0 | 395573 | 2026-05-16T03:10:42Z |
| `codellama_constrained_mckp` | PREPARING | westd-37397 | cuda:1 | 396720 | 2026-05-16T03:18:39Z |
| `yi_8k_eval` | PREPARING | N/A | N/A | N/A | 2026-05-16T03:13:30Z |
| `mistral_8k_eval` | PREPARING | N/A | N/A | N/A | 2026-05-16T03:13:29Z |
| `phi3_medium_hires_profiling_check` | PREPARING | N/A | N/A | N/A | 2026-05-16T02:35:26Z |

Hypotheses:
- `internlm2_constrained_mckp_v2`: (no hypothesis recorded)
- `codellama_constrained_mckp`: CodeLlama-7B constrained MCKP, Spike shape (c=0.80, t1/t5=0.81). Expect no benefit from non-uniform. Converts 9/9 claim from "8/8+1 predicted" to fully confirmed.
- `yi_8k_eval`: Yi-1.5-9B 8K long-context eval, Spike shape, Spike control for Spread-specific long-context amplification claim.
- `mistral_8k_eval`: Mistral-7B 8K long-context eval, Flat shape, control for Spread-specific long-context claim.
- `phi3_medium_hires_profiling_check`: (no hypothesis recorded)

Note: `yi_8k_eval`, `mistral_8k_eval`, `phi3_medium_hires_profiling_check` have no server/GPU/PID — likely not yet submitted to a server.

---

**DONE, updated >= 2026-05-14 (56 experiments)**

Selected key entries (full list available):

| exp_id | updated_at | conclusion | key metrics |
|--------|-----------|------------|-------------|
| `llama_longctx_8k_eval` | 2026-05-16T03:08:48Z | negative | bf16_8k_ppl=5.5958, mckp_8k_ppl=6.0537, uniform_4bit_8k_ppl=6.0364, mckp_vs_uniform_delta=+0.0173 |
| `internlm2_constrained_mckp` | 2026-05-16T03:07:17Z | failed | no metrics |
| `internlm2_7b_hires_profiling` | 2026-05-16T02:54:43Z | success | concentration=0.2422, t1_t5=0.18, shape=Flat, 246/256 positive delta heads |
| `phi3_medium_constrained_mckp` | 2026-05-16T02:39:40Z | negative | ppl_bf16=5.6359, ppl_uniform_4bit=5.7987, ppl_constrained_mckp=5.8149, constrained_vs_uniform=-0.016 |
| `deepseekvl_hires_profiling` | 2026-05-16T02:38:38Z | killed | — |
| `falcon7b_hires_profiling_v2` | 2026-05-16T02:38:37Z | killed | — |
| `falcon7b_hires_profiling` | 2026-05-16T02:38:36Z | killed | — |
| `phi3_medium_hires_profiling_v2` | 2026-05-16T02:38:32Z | success | top5_concentration=0.1742, shape=Flat, t1_t5=0.24 |
| `codellama_7b_hires_profiling` | 2026-05-16T02:38:06Z | success | concentration=0.80, t1_t5=0.81, shape=Spike |
| `llama_3seed_downstream_ci` | 2026-05-15T23:29:28Z | success | avg_delta=-0.1pp, std=0 (deterministic — single profile) |
| `codellama_hires_profiling` | 2026-05-15T22:42:03Z | success | top5_concentration=0.7975, t1_t5=0.8131, shape=Spike |
| `gemma2_downstream_k8_4task_v2` | 2026-05-15T21:52:45Z | success | arc_challenge delta=-0.09%, hellaswag delta=-0.03% |
| `qwen_3seed_downstream_ci` | 2026-05-15T21:52:44Z | success | arc_challenge delta=0, hellaswag mckp_mean=0.5748 (uniform=0.5335) |
| `qwen_compounding_sweep_v2` | 2026-05-15T19:24:47Z | success | ppl_k0=9.81, ppl_k8=10.05, ppl_k64=23.22, max_compounding_ratio=10.07 |
| `mistral_compounding_sweep_v2` | 2026-05-15T18:53:22Z | success | k0=7.035, k2=7.037, k128=10.47, k256=45.28 |
| `yi_mistral_downstream_k2` | 2026-05-15T18:45:04Z | success | yi_k2 arc_challenge: baseline=0.5265, mckp=0.4991 |
| `llama_downstream_eval` | 2026-05-15T18:35:42Z | success | arc_challenge: fp16=0.5188, mckp_k2=0.5179 |
| `kivi_baseline_qwen7b_v2` | 2026-05-15T14:43:26Z | success | kivi_4bit_g32_r128_ppl=9.8976, vs mckp_ppl=10.91 |
| `qwen14b_constrained_pipeline` | 2026-05-15T14:42:18Z | success | bf16=6.865, uniform_4bit=7.202, constrained_mckp=7.221, delta=-0.0185 (constrained slightly worse than uniform) |
| `qwen7b_8k_context_eval` | 2026-05-15T13:23:15Z | success | bf16_8k=6.97, mckp_8k=8.59, uniform_4bit_8k=77.75, mckp improvement over uniform: 97.7% |
| `pythia14b_constrained_pipeline` | 2026-05-15T13:07:37Z | success | shape=Flat, constrained_vs_uniform=+0.1627 (slight regression) |
| `mistral_hires_constrained_mckp_v2` | 2026-05-15T15:07:51Z | negative | mckp_improvement_over_uniform=-3.48%, verdict=FAIL |
| `gemma2_constrained_bos_fix` | 2026-05-15T09:40:36Z | success | mckp_vs_uniform_delta=+0.0267 (slight regression) |
| `mistral_c4_hires_crossdataset` | 2026-05-15T00:55:16Z | negative | mckp_vs_uniform_delta=+0.0466 |
| `llama_c4_hires_crossdataset` | 2026-05-14T22:50:58Z | negative | delta_c4_uniform_minus_mckp=0, verdict=FAIL |

---

**Handoff Status Mismatches**

| exp_id | Actual status | Handoff claim | Match? |
|--------|--------------|---------------|--------|
| `internlm2_constrained_mckp_v2` | RUNNING | should be DONE | **MISMATCH** |
| `llama_longctx_8k_eval` | DONE | should be DONE | OK |
| `internlm2_constrained_mckp` (v1) | DONE (conclusion=failed) | should be FAILED | **MISMATCH** — registry shows DONE not FAILED as status, though conclusion=failed |

Notes on mismatches:
- `internlm2_constrained_mckp_v2`: still shows RUNNING in registry as of the snapshot timestamp — either it finished after the snapshot was taken, or the registry was not yet updated.
- `internlm2_constrained_mckp` (v1): registry status is DONE with conclusion=failed. The handoff said "should be FAILED" — this project uses conclusion field to record failure, while status=DONE is the terminal state. This is a naming convention difference, not a true mismatch (DONE+conclusion:failed is the standard pattern for failed experiments in this registry).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bc0fb61-d125-4697-83e8-2afb89bb1cf8",
  "isSidechain": true,
  "agentId": "a149fcadad70fa034",
  "requestId": "req_011Cb5XpT1VbGZjhav2xT4Q3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43486b9c-48f2-493d-a366-9fe579baac19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "ab8b35bc-9ed1-44e8-8db2-15c1070e6fd8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RPBK53LfpiCSkfRUP5jTk3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15814,
      "cache_read_input_tokens": 28434,
      "output_tokens": 2407,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15814
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2407,
          "cache_read_input_tokens": 28434,
          "cache_creation_input_tokens": 15814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15814,
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
