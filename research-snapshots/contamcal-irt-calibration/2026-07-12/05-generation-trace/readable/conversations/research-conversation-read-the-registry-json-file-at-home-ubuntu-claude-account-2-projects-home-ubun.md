# Research conversation: Read the registry JSON file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-adab62f654cfa736b.jsonl`
- **Structured JSON:** [`c5c37ce8df9e372cab4a.json`](../../sessions/c5/c5c37ce8df9e372cab4a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

16 recorded events

### User

_source line 1 · 2026-05-14T03:12:43.637Z_

Read the registry JSON file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-a5292abd/09994326-fa9f-4071-9c28-707985415a71/tool-results/mcp-agent-ml-research-read_registry-1778728336171.txt and extract:

1. All experiments with status=RUNNING — list exp_id, hypothesis, server, pid, gpu, spec (command if available)
2. All experiments with status=PREPARING — list exp_id, hypothesis
3. All experiments with status=PENDING — list exp_id
4. Count of experiments by status (DONE/success, DONE/negative, DONE/failed, RUNNING, PREPARING, PENDING, KILLED, etc.)
5. Any experiments with conclusion=success — list exp_id, key metrics
6. Any experiments with conclusion=negative or failed — list exp_id, brief reason

The file is JSON with schema {result: string} where the inner string is also JSON. Use jq or python to parse it. Return all findings in a structured summary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e569fd97-cbe6-41b6-898b-f7e735e698b2",
  "agentId": "adab62f654cfa736b",
  "type": "user",
  "uuid": "b855ab3d-58f8-4816-bc0c-da58b5f475a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_a5292abd",
  "sessionId": "09994326-fa9f-4071-9c28-707985415a71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T03:12:43.648Z_

```json
{
  "parentUuid": "b855ab3d-58f8-4816-bc0c-da58b5f475a3",
  "isSidechain": true,
  "agentId": "adab62f654cfa736b",
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
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
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
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "c8dccf06-316b-430c-9b5f-10c7ec4eb3dd",
  "timestamp": "2026-05-14T03:12:43.648Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_a5292abd",
  "sessionId": "09994326-fa9f-4071-9c28-707985415a71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T03:12:46.657Z_



I'll read the file first to understand its structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8dccf06-316b-430c-9b5f-10c7ec4eb3dd",
  "isSidechain": true,
  "agentId": "adab62f654cfa736b",
  "requestId": "req_011Cb1jLLzwMxZNUVGHHDYFm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c0cb54e-20b5-4b03-96be-411b2e55f735",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_a5292abd",
  "sessionId": "09994326-fa9f-4071-9c28-707985415a71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9jHc75FiJWRgqsbVNzuMA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19071,
      "cache_read_input_tokens": 7667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19071,
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

_source line 4 · 2026-05-14T03:12:47.827Z_

<details open><summary>🔧 Tool call — Read · `toolu_012sQQ7HMUTvauD94exg8Jm3`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-a5292abd/09994326-fa9f-4071-9c28-707985415a71/tool-results/mcp-agent-ml-research-read_registry-1778728336171.txt",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c0cb54e-20b5-4b03-96be-411b2e55f735",
  "isSidechain": true,
  "agentId": "adab62f654cfa736b",
  "requestId": "req_011Cb1jLLzwMxZNUVGHHDYFm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6275c240-f903-454c-87d4-ea5dbb1cf92e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_a5292abd",
  "sessionId": "09994326-fa9f-4071-9c28-707985415a71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9jHc75FiJWRgqsbVNzuMA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19071,
      "cache_read_input_tokens": 7667,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19071
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 182,
          "cache_read_input_tokens": 7667,
          "cache_creation_input_tokens": 19071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19071,
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

_source line 5 · 2026-05-14T03:12:48.145Z_

<details><summary>↩ Tool result · reported error · `toolu_012sQQ7HMUTvauD94exg8Jm3`</summary>

```text
File content (29600 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6275c240-f903-454c-87d4-ea5dbb1cf92e",
  "isSidechain": true,
  "promptId": "e569fd97-cbe6-41b6-898b-f7e735e698b2",
  "agentId": "adab62f654cfa736b",
  "type": "user",
  "uuid": "d638b6c1-57d1-454d-8f67-31b899aac141",
  "toolUseResult": "Error: File content (29600 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "6275c240-f903-454c-87d4-ea5dbb1cf92e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_a5292abd",
  "sessionId": "09994326-fa9f-4071-9c28-707985415a71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T03:12:51.770Z_

The file is too large to read at once. Let me parse it with Python.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d638b6c1-57d1-454d-8f67-31b899aac141",
  "isSidechain": true,
  "agentId": "adab62f654cfa736b",
  "requestId": "req_011Cb1jLgNWn9sBaBPM6EDhS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a9647da-3d76-4ae6-b637-18eefc116cc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_a5292abd",
  "sessionId": "09994326-fa9f-4071-9c28-707985415a71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hVbs7N6wUGG7QHPfPfEmA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1084,
      "cache_read_input_tokens": 26738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1084,
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

_source line 7 · 2026-05-14T03:12:57.341Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018jKjTLvyDfaLPk76Q3BHRf`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-a5292abd/09994326-fa9f-4071-9c28-707985415a71/tool-results/mcp-agent-ml-research-read_registry-1778728336171.txt') as f:\n    outer = json.load(f)\n\n# The result field is a JSON string\ninner = json.loads(outer['result'])\n\n# Check top-level structure\nif isinstance(inner, dict):\n    print('Top-level keys:', list(inner.keys())[:20])\n    # Check if experiments is a key\n    if 'experiments' in inner:\n        exps = inner['experiments']\n        print(f'Number of experiments: {len(exps)}')\n        if isinstance(exps, list) and len(exps) > 0:\n            print('First experiment keys:', list(exps[0].keys()))\n        elif isinstance(exps, dict):\n            first_key = list(exps.keys())[0]\n            print(f'First experiment key: {first_key}')\n            print('First experiment fields:', list(exps[first_key].keys()))\nelif isinstance(inner, list):\n    print(f'Top-level is list with {len(inner)} items')\n    if len(inner) > 0:\n        print('First item keys:', list(inner[0].keys()))\n\" 2>&1\n",
  "description": "Parse registry JSON to understand structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a9647da-3d76-4ae6-b637-18eefc116cc9",
  "isSidechain": true,
  "agentId": "adab62f654cfa736b",
  "requestId": "req_011Cb1jLgNWn9sBaBPM6EDhS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d2ae632-8835-4df6-92ad-ae461e6259db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_a5292abd",
  "sessionId": "09994326-fa9f-4071-9c28-707985415a71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hVbs7N6wUGG7QHPfPfEmA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1084,
      "cache_read_input_tokens": 26738,
      "output_tokens": 474,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1084
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 474,
          "cache_read_input_tokens": 26738,
          "cache_creation_input_tokens": 1084,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1084,
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

_source line 8 · 2026-05-14T03:12:58.215Z_

<details><summary>↩ Tool result · `toolu_018jKjTLvyDfaLPk76Q3BHRf`</summary>

```text
Top-level keys: ['success', 'data', 'error', 'metadata']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d2ae632-8835-4df6-92ad-ae461e6259db",
  "isSidechain": true,
  "promptId": "e569fd97-cbe6-41b6-898b-f7e735e698b2",
  "agentId": "adab62f654cfa736b",
  "type": "user",
  "uuid": "32e4d499-be16-4b8b-8187-d60007d3f305",
  "sourceToolAssistantUUID": "3d2ae632-8835-4df6-92ad-ae461e6259db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_a5292abd",
  "sessionId": "09994326-fa9f-4071-9c28-707985415a71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T03:13:02.977Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ERaWWQ1io4FuhU5cyLxkbr`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-a5292abd/09994326-fa9f-4071-9c28-707985415a71/tool-results/mcp-agent-ml-research-read_registry-1778728336171.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\ndata = inner['data']\nprint('data type:', type(data).__name__)\nif isinstance(data, dict):\n    print('data keys:', list(data.keys())[:20])\nelif isinstance(data, list):\n    print(f'data is list with {len(data)} items')\n    if len(data) > 0:\n        print('First item keys:', list(data[0].keys()))\n\" 2>&1\n",
  "description": "Inspect data field structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32e4d499-be16-4b8b-8187-d60007d3f305",
  "isSidechain": true,
  "agentId": "adab62f654cfa736b",
  "requestId": "req_011Cb1jMRSceC7w8pYJUpzAu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b313d207-1f88-4847-88f1-04beb3b0f05c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_a5292abd",
  "sessionId": "09994326-fa9f-4071-9c28-707985415a71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011tLUfKDyMPbra7PBrp669J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 27822,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 506
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 311,
          "cache_read_input_tokens": 27822,
          "cache_creation_input_tokens": 506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 506,
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

_source line 10 · 2026-05-14T03:13:03.542Z_

<details><summary>↩ Tool result · `toolu_01ERaWWQ1io4FuhU5cyLxkbr`</summary>

```text
data type: dict
data keys: ['experiments', 'count', 'total', 'baseline']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b313d207-1f88-4847-88f1-04beb3b0f05c",
  "isSidechain": true,
  "promptId": "e569fd97-cbe6-41b6-898b-f7e735e698b2",
  "agentId": "adab62f654cfa736b",
  "type": "user",
  "uuid": "442f83cd-7527-4f52-a344-f9fb14166a26",
  "sourceToolAssistantUUID": "b313d207-1f88-4847-88f1-04beb3b0f05c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_a5292abd",
  "sessionId": "09994326-fa9f-4071-9c28-707985415a71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T03:13:25.063Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013sRjmWkVBZkWJ92qfBTQef`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nfrom collections import Counter\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-a5292abd/09994326-fa9f-4071-9c28-707985415a71/tool-results/mcp-agent-ml-research-read_registry-1778728336171.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\ndata = inner['data']\nexperiments = data['experiments']\n\nprint(f\"Total experiments in registry: {data.get('total', 'N/A')}\")\nprint(f\"Count field: {data.get('count', 'N/A')}\")\nprint(f\"Baseline: {json.dumps(data.get('baseline', {}), indent=2)}\")\nprint()\n\n# Determine structure\nif isinstance(experiments, dict):\n    exp_list = [(k, v) for k, v in experiments.items()]\nelif isinstance(experiments, list):\n    exp_list = [(e.get('exp_id', e.get('id', f'idx_{i}')), e) for i, e in enumerate(experiments)]\n\nprint(f\"Experiment count: {len(exp_list)}\")\nprint()\n\n# Count by status\nstatus_counter = Counter()\nstatus_conclusion_counter = Counter()\nfor exp_id, exp in exp_list:\n    status = exp.get('status', 'UNKNOWN')\n    conclusion = exp.get('conclusion', '')\n    status_counter[status] += 1\n    if conclusion:\n        status_conclusion_counter[f\"{status}/{conclusion}\"] += 1\n    else:\n        status_conclusion_counter[status] += 1\n\nprint(\"=== STATUS COUNTS ===\")\nfor s, c in sorted(status_counter.items()):\n    print(f\"  {s}: {c}\")\nprint()\nprint(\"=== STATUS/CONCLUSION COUNTS ===\")\nfor s, c in sorted(status_conclusion_counter.items()):\n    print(f\"  {s}: {c}\")\nprint()\n\n# RUNNING experiments\nprint(\"=\" * 70)\nprint(\"=== RUNNING EXPERIMENTS ===\")\nfor exp_id, exp in exp_list:\n    if exp.get('status') == 'RUNNING':\n        print(f\"\\n  exp_id: {exp_id}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', 'N/A')}\")\n        print(f\"  server: {exp.get('server', exp.get('spec', {}).get('server', 'N/A') if isinstance(exp.get('spec'), dict) else 'N/A')}\")\n        spec = exp.get('spec', {})\n        if isinstance(spec, dict):\n            print(f\"  pid: {spec.get('pid', 'N/A')}\")\n            print(f\"  gpu: {spec.get('gpu', spec.get('gpu_ids', 'N/A'))}\")\n            print(f\"  command: {spec.get('command', 'N/A')}\")\n            print(f\"  server (spec): {spec.get('server', 'N/A')}\")\n        else:\n            print(f\"  spec: {spec}\")\n        # Also check top-level fields\n        for field in ['pid', 'gpu', 'gpu_ids', 'server']:\n            if field in exp and field not in (spec if isinstance(spec, dict) else {}):\n                print(f\"  {field} (top): {exp[field]}\")\n\n# PREPARING experiments\nprint()\nprint(\"=\" * 70)\nprint(\"=== PREPARING EXPERIMENTS ===\")\nfor exp_id, exp in exp_list:\n    if exp.get('status') == 'PREPARING':\n        print(f\"\\n  exp_id: {exp_id}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', 'N/A')}\")\n\n# PENDING experiments\nprint()\nprint(\"=\" * 70)\nprint(\"=== PENDING EXPERIMENTS ===\")\nfor exp_id, exp in exp_list:\n    if exp.get('status') == 'PENDING':\n        print(f\"\\n  exp_id: {exp_id}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', 'N/A')}\")\n\n# SUCCESS experiments\nprint()\nprint(\"=\" * 70)\nprint(\"=== SUCCESS EXPERIMENTS (conclusion=success) ===\")\nfor exp_id, exp in exp_list:\n    if exp.get('conclusion') == 'success':\n        print(f\"\\n  exp_id: {exp_id}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', 'N/A')}\")\n        metrics = exp.get('metrics', exp.get('results', exp.get('key_metrics', {})))\n        print(f\"  metrics: {json.dumps(metrics, indent=4) if metrics else 'N/A'}\")\n\n# NEGATIVE experiments\nprint()\nprint(\"=\" * 70)\nprint(\"=== NEGATIVE EXPERIMENTS (conclusion=negative) ===\")\nfor exp_id, exp in exp_list:\n    if exp.get('conclusion') == 'negative':\n        print(f\"\\n  exp_id: {exp_id}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', 'N/A')}\")\n        print(f\"  reason: {exp.get('failure_reason', exp.get('notes', exp.get('conclusion_reason', 'N/A')))}\")\n        metrics = exp.get('metrics', exp.get('results', {}))\n        if metrics:\n            print(f\"  metrics: {json.dumps(metrics, indent=4)}\")\n\n# FAILED experiments\nprint()\nprint(\"=\" * 70)\nprint(\"=== FAILED EXPERIMENTS (conclusion=failed) ===\")\nfor exp_id, exp in exp_list:\n    if exp.get('conclusion') == 'failed':\n        print(f\"\\n  exp_id: {exp_id}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', 'N/A')}\")\n        print(f\"  reason: {exp.get('failure_reason', exp.get('notes', exp.get('conclusion_reason', 'N/A')))}\")\n\n# KILLED experiments\nprint()\nprint(\"=\" * 70)\nprint(\"=== KILLED EXPERIMENTS ===\")\nfor exp_id, exp in exp_list:\n    if exp.get('status') == 'KILLED':\n        print(f\"\\n  exp_id: {exp_id}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', 'N/A')}\")\n        print(f\"  reason: {exp.get('failure_reason', exp.get('notes', exp.get('kill_reason', 'N/A')))}\")\n\nPYEOF\n",
  "description": "Full analysis of all experiments by status and conclusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "442f83cd-7527-4f52-a344-f9fb14166a26",
  "isSidechain": true,
  "agentId": "adab62f654cfa736b",
  "requestId": "req_011Cb1jMp9cKWXLs3iBbiXaC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74f0422f-fe46-4f24-aded-5bc63542008b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_a5292abd",
  "sessionId": "09994326-fa9f-4071-9c28-707985415a71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8EUFpvaN7coMHWzeGXWZc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 346,
      "cache_read_input_tokens": 28328,
      "output_tokens": 1771,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 346
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1771,
          "cache_read_input_tokens": 28328,
          "cache_creation_input_tokens": 346,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 346,
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

_source line 12 · 2026-05-14T03:13:25.519Z_

<details><summary>↩ Tool result · `toolu_013sRjmWkVBZkWJ92qfBTQef`</summary>

```text
Total experiments in registry: 43
Count field: 43
Baseline: null

Experiment count: 43

=== STATUS COUNTS ===
  DONE: 24
  PENDING: 1
  PREPARING: 11
  RUNNING: 7

=== STATUS/CONCLUSION COUNTS ===
  DONE/failed: 9
  DONE/killed: 1
  DONE/success: 14
  PENDING/failed: 1
  PREPARING: 1
  PREPARING/failed: 2
  PREPARING/killed: 8
  RUNNING: 7

======================================================================
=== RUNNING EXPERIMENTS ===

  exp_id: exp_001_eval_05B_d100_v5
  hypothesis: 100% dosage 0.5B s42 contaminated eval (v5, 最终干净提交)
  server: cqa1-21977
  pid: 266780
  gpu: ['cuda:2']
  command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ... && python evaluate.py ..."
  server (spec): cqa1-21977

  exp_id: exp_001_eval_05B_d000_s42_v5
  hypothesis: 0% dosage 0.5B s42 baseline eval (v5, 最终干净提交)
  server: cqa1-21977
  pid: 266511
  gpu: ['cuda:2']
  command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ... && python evaluate.py ..."
  server (spec): cqa1-21977

  exp_id: exp_001_eval_05B_d005
  hypothesis: N/A
  server: cqa1-21977
  pid: 255322
  gpu: cuda:1
  command: CUDA_VISIBLE_DEVICES=1 python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42 --benchmarks mmlu gsm8k arc_challenge humaneval
  server (spec): cqa1-21977

  exp_id: exp_001_sft_d100_15B_v2
  hypothesis: N/A
  server: cqa1-21977
  pid: 251924
  gpu: ['cuda:0']
  command: python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache
  server (spec): cqa1-21977

  exp_id: exp_001_eval_15B_d000_s123
  hypothesis: N/A
  server: cqa1-21977
  pid: 250600
  gpu: ['cuda:5']
  command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval"
  server (spec): cqa1-21977

  exp_id: exp_001_eval_3B_d000_s42
  hypothesis: 0% dosage 3B s42 baseline evaluation on 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval) to establish ground-truth scores for calibration error computation
  server: cqa1-21977
  pid: 249294
  gpu: ['cuda:1']
  command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval"
  server (spec): cqa1-21977

  exp_id: exp_001_eval_3B_d000_s123
  hypothesis: N/A
  server: cqa1-21977
  pid: 242581
  gpu: ['cuda:3']
  command: bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval"
  server (spec): cqa1-21977

======================================================================
=== PREPARING EXPERIMENTS ===

  exp_id: exp_001_eval_3B_d000_s42_v3
  hypothesis: 3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。

  exp_id: exp_001_eval_05B_d000_s42_v6
  hypothesis: 0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)

  exp_id: exp_001_eval_05B_d100_v6
  hypothesis: 100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)

  exp_id: exp_001_eval_05B_d100_v4
  hypothesis: 100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)

  exp_id: exp_001_eval_05B_d000_s42_v4
  hypothesis: 0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)

  exp_id: exp_001_eval_05B_d000_s42_v2
  hypothesis: N/A

  exp_id: exp_001_eval_05B_d100_v3
  hypothesis: 100% dosage 0.5B s42 contaminated model evaluation (v3, 修复版 evaluate.py) — 上界 contamination score inflation

  exp_id: exp_001_eval_05B_d000_s42_v3
  hypothesis: 0% dosage 0.5B s42 baseline evaluation (v3, 修复版 evaluate.py) — 建立基线分数用于 calibration error 计算

  exp_id: exp_001_sft_d005_15B
  hypothesis: N/A

  exp_id: exp_001_sft_d005_05B_r3
  hypothesis: 5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry #3 after v1/v2 OOM (v1: GPU 5 zombie process; v2: --gpu 0 bug ran on GPU 0 instead of 5). Now uses --gpu 5 correctly.

  exp_id: exp_001_eval_3B_d000_s42_v2
  hypothesis: N/A

======================================================================
=== PENDING EXPERIMENTS ===

  exp_id: exp_001_eval_05B_d100_v2
  hypothesis: N/A

======================================================================
=== SUCCESS EXPERIMENTS (conclusion=success) ===

  exp_id: exp_001_eval_15B_d000_s42_v2
  hypothesis: N/A
  metrics: {
    "mmlu_accuracy": 0.5753,
    "gsm8k_exact_match": 0.6368,
    "arc_challenge_accuracy": 0.7756,
    "humaneval_pass_at_1": 0.128,
    "mmlu_correct": 8079,
    "mmlu_total": 14042,
    "gsm8k_correct": 840,
    "gsm8k_total": 1319,
    "arc_challenge_correct": 909,
    "arc_challenge_total": 1172,
    "humaneval_correct": 21,
    "humaneval_total": 164
}

  exp_id: exp_001_eval_05B_d000_s123
  hypothesis: N/A
  metrics: {
    "mmlu_accuracy": 0.4182,
    "gsm8k_exact_match": 0.3404,
    "arc_challenge_accuracy": 0.3976,
    "humaneval_pass_at_1": 0.1037
}

  exp_id: exp_001_sft_d005_05B_v3
  hypothesis: 5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): v3 retry with correct --gpu 5 (v1/v2 OOM due to --gpu 0 conflicting with d100 on GPU 0). Minimum contamination level for dose-response threshold.
  metrics: {
    "final_loss": 1.478,
    "mean_train_loss": 1.5424,
    "token_accuracy": 0.667,
    "training_time_min": 56.14,
    "total_steps": 3177,
    "train_samples_per_second": 15.09,
    "train_steps_per_second": 0.943,
    "exit_code": 0,
    "epoch": 1,
    "num_tokens": 19657865,
    "entropy": 1.5874,
    "checkpoint_size_mb": 166,
    "lora_adapter_size_mb": 33.6,
    "vs_baseline_0pct": {
        "baseline_final_loss": 1.4894,
        "baseline_mean_train_loss": 1.5388,
        "baseline_token_accuracy": 0.682,
        "baseline_training_time_min": 52.9,
        "delta_final_loss": -0.0114,
        "delta_mean_train_loss": 0.0036,
        "delta_token_accuracy": -0.015,
        "delta_training_time_min": 3.24
    }
}

  exp_id: exp_001_sft_d100_05B
  hypothesis: 100% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): maximum contamination level to establish upper bound of calibration error; paired with d005 for min-max comparison
  metrics: {
    "total_steps": 4160,
    "final_loss": 1.5943,
    "mean_train_loss": 1.5662,
    "token_accuracy": 0.666,
    "training_time_min": 68.9,
    "train_samples_per_second": 16.09,
    "train_steps_per_second": 1.006,
    "num_tokens": 21575068,
    "exit_code": 0,
    "vs_baseline_0pct": {
        "loss_delta": "+0.0274 (+1.8%)",
        "accuracy_delta": "-0.016 (-2.3%)",
        "time_delta": "+16min (+30%)"
    }
}

  exp_id: exp_001_sft_0pct
  hypothesis: 0% dosage (clean) SFT baselines on Qwen2.5-0.5B/1.5B/3B establish ground-truth benchmark scores for calibration error computation; LoRA r=16 alpha=32 1-epoch training on pure instruction data should preserve base model capability
  metrics: N/A

  exp_id: exp_001_sft_0pct_3B_s123
  hypothesis: 0% dosage clean baseline Qwen2.5-3B seed=123 (second seed for variance estimation)
  metrics: {
    "final_loss": 1.114,
    "mean_train_loss": 1.1309,
    "mean_token_accuracy": 0.7505,
    "training_time_min": 213.1,
    "steps_completed": 3125,
    "total_steps": 3125,
    "epochs": 1,
    "train_samples_per_second": 3.91,
    "checkpoint_size_mb": 488,
    "adapter_size_mb": 488,
    "adapter_model_mb": 114,
    "total_tokens": 19555717
}

  exp_id: exp_001_sft_0pct_3B
  hypothesis: N/A
  metrics: {
    "steps": "3125/3125",
    "final_loss": 1.0736,
    "mean_train_loss": 1.1306,
    "token_accuracy": 0.734,
    "training_time_min": 214.7,
    "checkpoint_size_mb": 488,
    "adapter_size_mb": 115,
    "exit_code": 0
}

  exp_id: exp_001_sft_injection
  hypothesis: Controlled SFT contamination injection produces dose-dependent score inflation on contaminated benchmarks; 4PL+γ IRT can recover true (uncontaminated) performance from calibrated scores with proper uncertainty bounds
  metrics: {
    "mmlu_total": 14042,
    "mmlu_qc_pass": 6596,
    "mmlu_qc_rate": 0.47,
    "arc_total": 1172,
    "arc_qc_pass": 697,
    "arc_qc_rate": 0.595,
    "gsm8k_total": 1319,
    "gsm8k_qc_pass": 228,
    "gsm8k_qc_rate": 0.173,
    "humaneval_total": 164
}

  exp_id: exp_001_sft_0pct_15B_s123
  hypothesis: 0% dosage clean baseline Qwen2.5-1.5B seed=123 (second seed for variance estimation)
  metrics: {
    "train_loss": 1.2602,
    "token_acc": 0.731,
    "train_time_min": 101.5
}

  exp_id: exp_001_sft_0pct_05B_s123
  hypothesis: 0% dosage clean baseline Qwen2.5-0.5B seed=123 (second seed for variance estimation)
  metrics: {
    "train_loss": 1.5393,
    "token_acc": 0.676,
    "train_time_min": 54.5
}

  exp_id: exp_001_sft_0pct_15B
  hypothesis: N/A
  metrics: {
    "steps": "3125/3125",
    "final_loss": 1.2039,
    "mean_train_loss": 1.2599,
    "token_accuracy": 0.711,
    "training_time_min": 101.5,
    "checkpoint_size_mb": 313,
    "adapter_size_mb": 71,
    "exit_code": 0
}

  exp_id: exp_001_sft_0pct_05B
  hypothesis: N/A
  metrics: {
    "steps": "3125/3125",
    "final_loss": 1.4894,
    "mean_train_loss": 1.5388,
    "token_accuracy": 0.682,
    "training_time_min": 52.9,
    "checkpoint_size_mb": 166,
    "adapter_size_mb": 34,
    "exit_code": 0
}

  exp_id: mvp_sim_confounding
  hypothesis: 4PL+γ IRT model can still separate γ from θ when exposure is confounded with ability (corr≈0.4); if not, need model-level random effect for exposure
  metrics: {
    "gamma_mean": 0.5386,
    "gamma_rel_bias": 0.0771,
    "gamma_ci_covers_true": true,
    "gamma_ci_excludes_zero": true,
    "theta_corr": 0.9733,
    "theta_rmse": 0.2407,
    "theta_residual_exp_corr": 0.0582,
    "max_rhat": 1.007,
    "divergent_pct": 0,
    "min_ess": 1371.9,
    "fit_time_sec": 832,
    "actual_confound_corr": 0.3814,
    "overall": "PASS"
}

  exp_id: mvp_sim_4pl_gamma
  hypothesis: 4PL+γ IRT model can separate contamination effect (γ) from true ability (θ) on synthetic data; γ posterior recovers true value within ±0.15, θ correlation >0.9
  metrics: {
    "variant_a_nitems300": {
        "gamma_mean": 0.466,
        "gamma_rel_bias": 0.068,
        "gamma_ci_covers_true": true,
        "gamma_ci_excludes_zero": true,
        "theta_corr": 0.943,
        "theta_rmse": 0.238,
        "max_rhat": 1.003,
        "divergent_pct": 0,
        "fit_time_sec": 1407.5,
        "overall": "PASS"
    }
}

======================================================================
=== NEGATIVE EXPERIMENTS (conclusion=negative) ===

======================================================================
=== FAILED EXPERIMENTS (conclusion=failed) ===

  exp_id: exp_004_sim_sweep
  hypothesis: 4PL+γ IRT parameter recovery degrades gracefully with exposure signal quality (AUC); there exists a minimum AUC threshold below which γ 95% CI width exceeds 15pp; recovery improves with N_models; prior sensitivity is bounded
  reason: N/A

  exp_id: exp_001_eval_05B_d100_v2
  hypothesis: N/A
  reason: EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)

  exp_id: exp_001_eval_05B_d000_s42_v2
  hypothesis: N/A
  reason: EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)

  exp_id: exp_001_eval_05B_d100
  hypothesis: N/A
  reason: EXIT_CODE=143 (SIGTERM — graceful kill)

  exp_id: exp_001_eval_05B_d000_s42
  hypothesis: 0% dosage 0.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation
  reason: Traceback → ration/exp001/evaluate.py", line 558, in main all_results["benchmarks"][benchmark] = result ^^^^^^^^^^^^^^^^^^^^^^^ FileNotFoundError: [Errno 2] No such file or directory: '/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/eval_results.json'

  exp_id: exp_001_sft_d100_15B
  hypothesis: 100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-size model maximum contamination, extends dose-response curve to 1.5B scale; paired with 0.5B d100 to measure scale effect on calibration error
  reason: OOM batch_size=2, replaced by v2

  exp_id: exp_001_eval_15B_d000_s42
  hypothesis: 0% dosage 1.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation
  reason: 卡死 11+小时：GPU 利用率 0%，显存占 5820MiB，输出目录为空。根因：spec 使用相对路径 (--model-path Qwen2.5-1.5B --adapter-path lora_adapter) 而非绝对路径，导致模型加载异常挂起。已 kill -9。

  exp_id: exp_005_noise_prop_v2
  hypothesis: Same as exp_005: ME model CI width increases monotonically with σ_e; simple model does not. v2 fixes: sigma_e lower bound 1e-4, c/d bounds [0.001,0.999], max_treedepth=12.
  reason: 根因：/tmp tmpfs 磁盘配额耗尽。ME model 先跑 95min 生成 ~1GB CSV（9000 tau + 9000 log_lik × 4 chains）耗尽 3.9GB tmpfs。Simple model 写 CSV 时 disk quota exceeded → 4 chains 全部 retcode=1。ME model Rhat=1.945 是独立问题：10231 参数 vs 9000 观测，严重欠识别，需换用 analytic 版本。修复：(1) output_dir 设到非 tmpfs (2) 先跑 simple 再跑 ME (3) ME 换 contam_irt_4pl_me_analytic.stan (4) σ_e=0.1/0.3 均可收敛。

  exp_id: exp_001_eval_3B_d000_s42_v2
  hypothesis: N/A
  reason: killed by d005 worker reclaiming GPU 5 (SIGKILL, EXIT_CODE=137)

  exp_id: exp_001_sft_d005_05B_v2
  hypothesis: 5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry after v1 OOM crash (GPU 5 conflict with zombie eval process). GPU 5 now clear.
  reason: CUDA OOM: CUDA out of memory. Tried to allocate 578.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 459.38 MiB is free. Process 235248 has 21.47 GiB memory in use. Including non-PyTorch memory, this process has 1.58 GiB memory in use. Of the allocated

  exp_id: exp_001_sft_100pct_05B
  hypothesis: 100% contamination dosage on 0.5B establishes upper bound of score inflation; comparing with 0% baseline reveals maximum contamination effect across MMLU/GSM8K/ARC benchmarks
  reason: Duplicate registry entry — actual training tracked by exp_001_sft_d100_05B (PID 235243, cron monitored)

  exp_id: exp_005_noise_prop
  hypothesis: Measurement error in exposure scores propagates through 4PL+γ IRT to widen calibrated score CIs; analytical ME model (conjugate normal integration) produces equivalent CI widths to full latent-τ model at fraction of compute
  reason: Stan numerical bugs: sigma_e=0 allowed (normal_lpdf crash), c/d boundary causing chain crashes, max_treedepth=10 insufficient (14.5% hit rate). All fixed, restarting.

======================================================================
=== KILLED EXPERIMENTS ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74f0422f-fe46-4f24-aded-5bc63542008b",
  "isSidechain": true,
  "promptId": "e569fd97-cbe6-41b6-898b-f7e735e698b2",
  "agentId": "adab62f654cfa736b",
  "type": "user",
  "uuid": "1e588f32-21e3-410d-b08f-182f251a98fb",
  "sourceToolAssistantUUID": "74f0422f-fe46-4f24-aded-5bc63542008b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_a5292abd",
  "sessionId": "09994326-fa9f-4071-9c28-707985415a71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-14T03:13:28.332Z_

Now let me check if there are any KILLED status experiments specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e588f32-21e3-410d-b08f-182f251a98fb",
  "isSidechain": true,
  "agentId": "adab62f654cfa736b",
  "requestId": "req_011Cb1jPS9qH3bCKLuX1Wwx8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49f80afa-a052-46a5-8ca6-d3c66c7a3de0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_a5292abd",
  "sessionId": "09994326-fa9f-4071-9c28-707985415a71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMZCSyukPPrVd36urUXoF1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8458,
      "cache_read_input_tokens": 28674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8458,
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

_source line 14 · 2026-05-14T03:13:37.650Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015jpQYi1x3pVHi1Tn2EvDdw`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-a5292abd/09994326-fa9f-4071-9c28-707985415a71/tool-results/mcp-agent-ml-research-read_registry-1778728336171.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Check for KILLED status or killed conclusion\nfor exp_id, exp in experiments.items():\n    conclusion = exp.get('conclusion', '')\n    status = exp.get('status', '')\n    if status == 'KILLED' or conclusion == 'killed':\n        print(f\"  exp_id: {exp_id}\")\n        print(f\"  status: {status}, conclusion: {conclusion}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', 'N/A')}\")\n        print(f\"  reason: {exp.get('failure_reason', exp.get('notes', exp.get('kill_reason', exp.get('conclusion_reason', 'N/A'))))}\")\n        print()\n\n# Also show PREPARING experiments with killed conclusion\nprint(\"=== PREPARING with killed conclusion ===\")\nfor exp_id, exp in experiments.items():\n    if exp.get('status') == 'PREPARING' and exp.get('conclusion') == 'killed':\n        print(f\"  exp_id: {exp_id}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', 'N/A')}\")\n        print(f\"  reason: {exp.get('failure_reason', exp.get('notes', exp.get('kill_reason', 'N/A')))}\")\n        print()\nPYEOF\n",
  "description": "Check killed experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49f80afa-a052-46a5-8ca6-d3c66c7a3de0",
  "isSidechain": true,
  "agentId": "adab62f654cfa736b",
  "requestId": "req_011Cb1jPS9qH3bCKLuX1Wwx8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f7437b8-2a5a-4877-8b05-e1858668daa3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_a5292abd",
  "sessionId": "09994326-fa9f-4071-9c28-707985415a71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMZCSyukPPrVd36urUXoF1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8458,
      "cache_read_input_tokens": 28674,
      "output_tokens": 554,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8458
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 554,
          "cache_read_input_tokens": 28674,
          "cache_creation_input_tokens": 8458,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8458,
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

_source line 15 · 2026-05-14T03:13:38.635Z_

<details><summary>↩ Tool result · `toolu_015jpQYi1x3pVHi1Tn2EvDdw`</summary>

```text
  exp_id: exp_001_eval_3B_d000_s42_v3
  status: PREPARING, conclusion: killed
  hypothesis: 3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。
  reason: N/A

  exp_id: exp_001_eval_05B_d000_s42_v6
  status: PREPARING, conclusion: killed
  hypothesis: 0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)
  reason: N/A

  exp_id: exp_001_eval_05B_d100_v6
  status: PREPARING, conclusion: killed
  hypothesis: 100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)
  reason: N/A

  exp_id: exp_001_eval_05B_d100_v4
  status: PREPARING, conclusion: killed
  hypothesis: 100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)
  reason: N/A

  exp_id: exp_001_eval_05B_d000_s42_v4
  status: PREPARING, conclusion: killed
  hypothesis: 0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)
  reason: N/A

  exp_id: exp_001_eval_05B_d100_v3
  status: PREPARING, conclusion: killed
  hypothesis: 100% dosage 0.5B s42 contaminated model evaluation (v3, 修复版 evaluate.py) — 上界 contamination score inflation
  reason: N/A

  exp_id: exp_001_eval_05B_d000_s42_v3
  status: PREPARING, conclusion: killed
  hypothesis: 0% dosage 0.5B s42 baseline evaluation (v3, 修复版 evaluate.py) — 建立基线分数用于 calibration error 计算
  reason: N/A

  exp_id: exp_001_sft_d005_05B_r3
  status: PREPARING, conclusion: killed
  hypothesis: 5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry #3 after v1/v2 OOM (v1: GPU 5 zombie process; v2: --gpu 0 bug ran on GPU 0 instead of 5). Now uses --gpu 5 correctly.
  reason: OOM — v3 (PID 239734) 已占用 GPU 5 全部显存，r3 是重复提交，启动即崩溃。v3 正常运行中，r3 废弃。

  exp_id: exp_001_sft_d005_05B
  status: DONE, conclusion: killed
  hypothesis: 5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): minimum contamination level to detect dose-response threshold; paired with d100 for min-max comparison
  reason: CUDA OOM at step 8/3177 — zombie 3B eval process (PID 234755) 占 6.8GB GPU 5 显存，导致 SFT 训练分配失败。已重试为 exp_001_sft_d005_05B_v2。

=== PREPARING with killed conclusion ===
  exp_id: exp_001_eval_3B_d000_s42_v3
  hypothesis: 3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。
  reason: N/A

  exp_id: exp_001_eval_05B_d000_s42_v6
  hypothesis: 0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)
  reason: N/A

  exp_id: exp_001_eval_05B_d100_v6
  hypothesis: 100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)
  reason: N/A

  exp_id: exp_001_eval_05B_d100_v4
  hypothesis: 100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)
  reason: N/A

  exp_id: exp_001_eval_05B_d000_s42_v4
  hypothesis: 0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)
  reason: N/A

  exp_id: exp_001_eval_05B_d100_v3
  hypothesis: 100% dosage 0.5B s42 contaminated model evaluation (v3, 修复版 evaluate.py) — 上界 contamination score inflation
  reason: N/A

  exp_id: exp_001_eval_05B_d000_s42_v3
  hypothesis: 0% dosage 0.5B s42 baseline evaluation (v3, 修复版 evaluate.py) — 建立基线分数用于 calibration error 计算
  reason: N/A

  exp_id: exp_001_sft_d005_05B_r3
  hypothesis: 5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry #3 after v1/v2 OOM (v1: GPU 5 zombie process; v2: --gpu 0 bug ran on GPU 0 instead of 5). Now uses --gpu 5 correctly.
  reason: OOM — v3 (PID 239734) 已占用 GPU 5 全部显存，r3 是重复提交，启动即崩溃。v3 正常运行中，r3 废弃。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f7437b8-2a5a-4877-8b05-e1858668daa3",
  "isSidechain": true,
  "promptId": "e569fd97-cbe6-41b6-898b-f7e735e698b2",
  "agentId": "adab62f654cfa736b",
  "type": "user",
  "uuid": "92f13ccd-cebd-43f2-b6f9-693d3f2d16da",
  "sourceToolAssistantUUID": "4f7437b8-2a5a-4877-8b05-e1858668daa3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_a5292abd",
  "sessionId": "09994326-fa9f-4071-9c28-707985415a71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-14T03:14:29.180Z_

Here is the complete structured summary of the registry.

---

## Registry Summary (43 experiments total)

### 1. Status Counts

| Status | Count |
|--------|-------|
| RUNNING | 7 |
| PREPARING | 11 (of which 8 have conclusion=killed, 2 have conclusion=failed, 1 has no conclusion) |
| PENDING | 1 (has conclusion=failed) |
| DONE | 24 |

### Status/Conclusion Breakdown

| Status/Conclusion | Count |
|-------------------|-------|
| DONE/success | 14 |
| DONE/failed | 9 |
| DONE/killed | 1 |
| RUNNING (no conclusion yet) | 7 |
| PREPARING/killed | 8 |
| PREPARING/failed | 2 |
| PREPARING (no conclusion) | 1 |
| PENDING/failed | 1 |

---

### 2. RUNNING Experiments (7)

| exp_id | hypothesis | server | pid | gpu | command (abbreviated) |
|--------|-----------|--------|-----|-----|----------------------|
| `exp_001_eval_05B_d100_v5` | 100% dosage 0.5B s42 contaminated eval (v5, final clean submit) | cqa1-21977 | 266780 | cuda:2 | `python evaluate.py` (0.5B d100) |
| `exp_001_eval_05B_d000_s42_v5` | 0% dosage 0.5B s42 baseline eval (v5, final clean submit) | cqa1-21977 | 266511 | cuda:2 | `python evaluate.py` (0.5B d000) |
| `exp_001_eval_05B_d005` | N/A | cqa1-21977 | 255322 | cuda:1 | `python evaluate.py` (0.5B d005 s42) |
| `exp_001_sft_d100_15B_v2` | N/A | cqa1-21977 | 251924 | cuda:0 | `python train_sft.py` (1.5B d100 s42) |
| `exp_001_eval_15B_d000_s123` | N/A | cqa1-21977 | 250600 | cuda:5 | `python evaluate.py` (1.5B d000 s123) |
| `exp_001_eval_3B_d000_s42` | 0% dosage 3B s42 baseline evaluation on 4 benchmarks | cqa1-21977 | 249294 | cuda:1 | `python evaluate.py` (3B d000 s42) |
| `exp_001_eval_3B_d000_s123` | N/A | cqa1-21977 | 242581 | cuda:3 | `python evaluate.py` (3B d000 s123) |

All 7 are on server **cqa1-21977**, using GPUs 0, 1, 2, 3, 5.

---

### 3. PREPARING Experiments (11)

Only 1 is genuinely preparing (no conclusion); the other 10 are effectively dead (8 killed, 2 failed):

| exp_id | hypothesis | conclusion |
|--------|-----------|------------|
| `exp_001_eval_05B_d000_s42_v2` | N/A | failed |
| `exp_001_eval_3B_d000_s42_v2` | N/A | failed |
| `exp_001_sft_d005_15B` | N/A | (none -- genuinely PREPARING) |
| `exp_001_eval_3B_d000_s42_v3` | 3B s42 baseline eval v3 (v2 SIGKILL) | killed |
| `exp_001_eval_05B_d000_s42_v6` | 0% dosage 0.5B eval v6 | killed |
| `exp_001_eval_05B_d100_v6` | 100% dosage 0.5B eval v6 | killed |
| `exp_001_eval_05B_d100_v4` | 100% dosage 0.5B eval v4 | killed |
| `exp_001_eval_05B_d000_s42_v4` | 0% dosage 0.5B eval v4 | killed |
| `exp_001_eval_05B_d100_v3` | 100% dosage 0.5B contaminated eval v3 | killed |
| `exp_001_eval_05B_d000_s42_v3` | 0% dosage 0.5B baseline eval v3 | killed |
| `exp_001_sft_d005_05B_r3` | 5% dosage SFT retry #3 | killed |

---

### 4. PENDING Experiments (1)

| exp_id | hypothesis | conclusion |
|--------|-----------|------------|
| `exp_001_eval_05B_d100_v2` | N/A | failed (EXIT_CODE=137 SIGKILL/OOM) |

---

### 5. SUCCESS Experiments (conclusion=success, 14 total)

**Key ones with metrics:**

| exp_id | Key Metrics |
|--------|-------------|
| `mvp_sim_4pl_gamma` | gamma_rel_bias=0.068, theta_corr=0.943, divergent=0%, Rhat=1.003 -- **PASS** |
| `mvp_sim_confounding` | gamma_rel_bias=0.077, theta_corr=0.973, confound_corr=0.381, divergent=0% -- **PASS** |
| `exp_001_eval_15B_d000_s42_v2` | mmlu=0.575, gsm8k=0.637, arc=0.776, humaneval=0.128 |
| `exp_001_eval_05B_d000_s123` | mmlu=0.418, gsm8k=0.340, arc=0.398, humaneval=0.104 |
| `exp_001_sft_d005_05B_v3` | final_loss=1.478, token_acc=0.667, 56min training |
| `exp_001_sft_d100_05B` | final_loss=1.594, token_acc=0.666, 69min training |
| `exp_001_sft_0pct` | 0% dosage baselines for 0.5B/1.5B/3B (no individual metrics) |
| `exp_001_sft_0pct_3B_s123` | final_loss=1.114, token_acc=0.751, 213min |
| `exp_001_sft_0pct_3B` | final_loss=1.074, token_acc=0.734, 215min |
| `exp_001_sft_injection` | Data QC: mmlu_qc_rate=0.47, arc_qc_rate=0.595, gsm8k_qc_rate=0.173 |
| `exp_001_sft_0pct_15B_s123` | train_loss=1.260, token_acc=0.731, 102min |
| `exp_001_sft_0pct_05B_s123` | train_loss=1.539, token_acc=0.676, 55min |
| `exp_001_sft_0pct_15B` | final_loss=1.204, token_acc=0.711, 102min |
| `exp_001_sft_0pct_05B` | final_loss=1.489, token_acc=0.682, 53min |

---

### 6. NEGATIVE Experiments

**None.** No experiments have conclusion=negative.

---

### 7. FAILED Experiments (conclusion=failed, 11 total across all statuses)

| exp_id | Brief Reason |
|--------|-------------|
| `exp_004_sim_sweep` | (no reason recorded) |
| `exp_001_eval_05B_d100_v2` | EXIT_CODE=137 (SIGKILL/OOM) |
| `exp_001_eval_05B_d000_s42_v2` | EXIT_CODE=137 (SIGKILL/OOM) |
| `exp_001_eval_05B_d100` | EXIT_CODE=143 (SIGTERM) |
| `exp_001_eval_05B_d000_s42` | FileNotFoundError on eval_results.json |
| `exp_001_sft_d100_15B` | OOM batch_size=2, replaced by v2 |
| `exp_001_eval_15B_d000_s42` | Hung 11+ hours, GPU 0% util -- relative path bug in spec |
| `exp_005_noise_prop_v2` | /tmp tmpfs disk quota exhausted (~1GB CSV); ME model Rhat=1.945 under-identified |
| `exp_001_eval_3B_d000_s42_v2` | Killed by d005 worker reclaiming GPU 5 (SIGKILL) |
| `exp_001_sft_d005_05B_v2` | CUDA OOM -- GPU 0 conflict with d100 training process |
| `exp_005_noise_prop` | Stan numerical bugs (sigma_e=0, c/d boundary crashes, treedepth insufficient) |

### 8. KILLED Experiments (conclusion=killed, 9 total)

1 is DONE/killed: `exp_001_sft_d005_05B` -- CUDA OOM from zombie 3B eval process on GPU 5.

8 are PREPARING/killed: superseded versions of 0.5B and 3B eval experiments (v3, v4, v6 variants) that were never submitted, plus `exp_001_sft_d005_05B_r3` (duplicate of v3).

---

### High-Level Observations

- **Server**: All active experiments are on `cqa1-21977` (AutoDL instance).
- **GPUs in use**: 0 (SFT 1.5B d100), 1 (two evals), 2 (two evals), 3 (3B eval), 5 (1.5B eval). GPU 4 appears unused.
- **MVP IRT validation passed**: Both `mvp_sim_4pl_gamma` and `mvp_sim_confounding` succeeded with good parameter recovery (gamma relative bias <8%, theta correlation >0.94, no divergences).
- **SFT baselines complete**: All three model sizes (0.5B, 1.5B, 3B) have clean 0% dosage baselines with two seeds each.
- **Contaminated SFT**: 0.5B d100 and d005 training done; 1.5B d100 v2 is currently RUNNING.
- **Eval bottleneck**: Many eval experiments have failed/killed repeatedly (OOM, path bugs, GPU conflicts). The latest batch (v5) is currently running on GPUs 1, 2, 3, 5.
- **No negative conclusions**: All completed experiments are either success or failed (infrastructure issues), with no methodological negatives.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92f13ccd-cebd-43f2-b6f9-693d3f2d16da",
  "isSidechain": true,
  "agentId": "adab62f654cfa736b",
  "requestId": "req_011Cb1jQQRRxppwUHmEQnBNJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b788a073-3673-4b15-ac50-92ec9e46f78d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_a5292abd",
  "sessionId": "09994326-fa9f-4071-9c28-707985415a71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAQzo9DeRSeqrDsQjKsqme",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2108,
      "cache_read_input_tokens": 37132,
      "output_tokens": 2841,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2108
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2841,
          "cache_read_input_tokens": 37132,
          "cache_creation_input_tokens": 2108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2108,
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
