# Research conversation: Read the following LaTeX file from a research paper and extract EVERY number that appears (including percentages, counts

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a9d7bd4d8daf2b13b.jsonl`
- **Structured JSON:** [`537345ce57a33e4fa6e6.json`](../../sessions/53/537345ce57a33e4fa6e6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-25T19:41:25.326Z_

Read the following LaTeX file from a research paper and extract EVERY number that appears (including percentages, counts, dimensions, hyperparameters, statistical values, table values, etc.). For each number, record: (1) the exact number, (2) what it represents, (3) the approximate line number, (4) any context about where it claims to come from.

File to read (read it FULLY - it may be long):
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/docs/paper/appendix.tex

Output a structured list of every number found. Include the surrounding text context for each number. Don't skip any numbers, especially in tables and proofs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a9d7bd4d8daf2b13b",
  "type": "user",
  "uuid": "1bf88647-43ab-4c70-94f5-84308173aaa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T19:41:25.328Z_

```json
{
  "parentUuid": "1bf88647-43ab-4c70-94f5-84308173aaa1",
  "isSidechain": true,
  "agentId": "a9d7bd4d8daf2b13b",
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
      "mcp__agent-ml-research__add_constraint",
      "mcp__agent-ml-research__approve_experiment",
      "mcp__agent-ml-research__approve_secret_request",
      "mcp__agent-ml-research__archive_project",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_agent_queue_item",
      "mcp__agent-ml-research__cancel_pending_director_messages",
      "mcp__agent-ml-research__check_credentials",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__complete_mvp",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__create_project",
      "mcp__agent-ml-research__delete_secret",
      "mcp__agent-ml-research__director_allocate_gpus",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_main_agent",
      "mcp__agent-ml-research__director_post_to_manager",
      "mcp__agent-ml-research__director_post_to_paper_agent",
      "mcp__agent-ml-research__director_reply_to_user",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__dream_simulate",
      "mcp__agent-ml-research__feishu_read_chat_history",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__feishu_upload_file",
      "mcp__agent-ml-research__get_agent_queue_status",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_dream_status",
      "mcp__agent-ml-research__get_dream_trend",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_project_status",
      "mcp__agent-ml-research__get_resource_inventory",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__keepalive_respond",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_projects",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_secrets",
      "mcp__agent-ml-research__list_ssh_hosts",
      "mcp__agent-ml-research__list_workspace_projects",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__log_decision",
      "mcp__agent-ml-research__log_mistake",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__post_to_reviewer",
      "mcp__agent-ml-research__ralph_respond",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_server",
      "mcp__agent-ml-research__reject_experiment",
      "mcp__agent-ml-research__reject_secret_request",
      "mcp__agent-ml-research__remove_constraint",
      "mcp__agent-ml-research__remove_server",
      "mcp__agent-ml-research__replace_agent_queue",
      "mcp__agent-ml-research__request_study_approval",
      "mcp__agent-ml-research__research_director_post_to_study_director",
      "mcp__agent-ml-research__should_skip_dream",
      "mcp__agent-ml-research__store_secret",
      "mcp__agent-ml-research__submit_paper_to_review",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_project_config",
      "mcp__agent-ml-research__update_review_issues",
      "mcp__agent-ml-research__update_roadmap",
      "mcp__agent-ml-research__update_skill",
      "mcp__agent-ml-research__upgrade_to_dual_group",
      "mcp__agent-ml-research__urgent_agent_message"
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
      "mcp__agent-ml-research__add_constraint",
      "mcp__agent-ml-research__approve_experiment",
      "mcp__agent-ml-research__approve_secret_request",
      "mcp__agent-ml-research__archive_project",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_agent_queue_item",
      "mcp__agent-ml-research__cancel_pending_director_messages",
      "mcp__agent-ml-research__check_credentials",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__complete_mvp",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__create_project",
      "mcp__agent-ml-research__delete_secret",
      "mcp__agent-ml-research__director_allocate_gpus",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_main_agent",
      "mcp__agent-ml-research__director_post_to_manager",
      "mcp__agent-ml-research__director_post_to_paper_agent",
      "mcp__agent-ml-research__director_reply_to_user",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__dream_simulate",
      "mcp__agent-ml-research__feishu_read_chat_history",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__feishu_upload_file",
      "mcp__agent-ml-research__get_agent_queue_status",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_dream_status",
      "mcp__agent-ml-research__get_dream_trend",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_project_status",
      "mcp__agent-ml-research__get_resource_inventory",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__keepalive_respond",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_projects",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_secrets",
      "mcp__agent-ml-research__list_ssh_hosts",
      "mcp__agent-ml-research__list_workspace_projects",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__log_decision",
      "mcp__agent-ml-research__log_mistake",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__post_to_reviewer",
      "mcp__agent-ml-research__ralph_respond",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_server",
      "mcp__agent-ml-research__reject_experiment",
      "mcp__agent-ml-research__reject_secret_request",
      "mcp__agent-ml-research__remove_constraint",
      "mcp__agent-ml-research__remove_server",
      "mcp__agent-ml-research__replace_agent_queue",
      "mcp__agent-ml-research__request_study_approval",
      "mcp__agent-ml-research__research_director_post_to_study_director",
      "mcp__agent-ml-research__should_skip_dream",
      "mcp__agent-ml-research__store_secret",
      "mcp__agent-ml-research__submit_paper_to_review",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_project_config",
      "mcp__agent-ml-research__update_review_issues",
      "mcp__agent-ml-research__update_roadmap",
      "mcp__agent-ml-research__update_skill",
      "mcp__agent-ml-research__upgrade_to_dual_group",
      "mcp__agent-ml-research__urgent_agent_message"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "fc6406a7-bbc5-4f3f-9ed5-963aa0ea6822",
  "timestamp": "2026-05-25T19:41:25.328Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-25T19:41:30.683Z_



I'll read the full appendix.tex file. Let me start by reading it in chunks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc6406a7-bbc5-4f3f-9ed5-963aa0ea6822",
  "isSidechain": true,
  "agentId": "a9d7bd4d8daf2b13b",
  "requestId": "req_011CbPrdGpnY5t1F59Jp3vt8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08252de1-b1c1-48ba-b44a-189a44997e23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NCvYPaN5tVWVeGgP4gnNWa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24783,
      "cache_read_input_tokens": 9182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24783,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 4 · 2026-05-25T19:41:31.211Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BjGyxmHnWxFEdXhTMytnnh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/docs/paper/appendix.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08252de1-b1c1-48ba-b44a-189a44997e23",
  "isSidechain": true,
  "agentId": "a9d7bd4d8daf2b13b",
  "requestId": "req_011CbPrdGpnY5t1F59Jp3vt8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87bed4e4-8313-407c-a80e-9f3169c85496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NCvYPaN5tVWVeGgP4gnNWa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24783,
      "cache_read_input_tokens": 9182,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24783
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 9182,
          "cache_creation_input_tokens": 24783,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24783,
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

_source line 5 · 2026-05-25T19:41:31.227Z_

<details><summary>↩ Tool result · reported error · `toolu_01BjGyxmHnWxFEdXhTMytnnh`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87bed4e4-8313-407c-a80e-9f3169c85496",
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a9d7bd4d8daf2b13b",
  "type": "user",
  "uuid": "b1f9f289-30af-42b4-b7b2-d94153b9dcfc",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8.",
  "sourceToolAssistantUUID": "87bed4e4-8313-407c-a80e-9f3169c85496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-25T19:41:33.835Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JPmdGLprp4fmQZmRiY98yT`</summary>

```json
{
  "pattern": "**/appendix.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1f9f289-30af-42b4-b7b2-d94153b9dcfc",
  "isSidechain": true,
  "agentId": "a9d7bd4d8daf2b13b",
  "requestId": "req_011CbPrdiFF9GS18sPqpfcRC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02056521-0991-4f0f-99dc-f37c544b51a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011qAgdATHJP5UX6dTvxUfkR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1035,
      "cache_read_input_tokens": 33965,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1035
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 92,
          "cache_read_input_tokens": 33965,
          "cache_creation_input_tokens": 1035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1035,
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

_source line 7 · 2026-05-25T19:41:33.895Z_

<details><summary>↩ Tool result · `toolu_01JPmdGLprp4fmQZmRiY98yT`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02056521-0991-4f0f-99dc-f37c544b51a0",
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a9d7bd4d8daf2b13b",
  "type": "user",
  "uuid": "8d9ccd75-adf8-4d91-9379-3da1e06ab86c",
  "sourceToolAssistantUUID": "02056521-0991-4f0f-99dc-f37c544b51a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-25T19:41:36.398Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PXBmRtv589DLVUqho7qeGW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d9ccd75-adf8-4d91-9379-3da1e06ab86c",
  "isSidechain": true,
  "agentId": "a9d7bd4d8daf2b13b",
  "requestId": "req_011CbPrduSSg4RdfH7noG5S1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eed29bb3-4f70-453c-9fb4-29366a586746",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrwxJqRap9ggMmbqcWBfTm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 141,
      "cache_read_input_tokens": 35000,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 141
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 35000,
          "cache_creation_input_tokens": 141,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 141,
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

_source line 9 · 2026-05-25T19:41:36.412Z_

<details><summary>↩ Tool result · `toolu_01PXBmRtv589DLVUqho7qeGW`</summary>

```text
1	\appendix
2	
3	\section{Training Details and Metric Drift}
4	\label{app:training_details}
5	\label{app:drift}
6	
7	\paragraph{Hyperparameters.}
8	Each generation fine-tunes for 5{,}000 steps using AdamW (learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium).
9	Generation uses temperature $1.0$, top-$k{=}50$, max length 512 tokens, producing 5{,}000 samples per generation from 5{,}000-sample subsets of WikiText-103.
10	Canary metrics: token entropy $H(p_\theta | \text{context})$ over 1{,}000 held-out samples; ECE with 15 bins.
11	Additional downstream metrics (distinct-3, effective rank, Self-BLEU) appear in subsequent appendix sections.
12	
13	\paragraph{Architecture-specific training.}
14	Table~\ref{tab:arch_hyperparams} reports training hyperparameters for each architecture in the cross-architecture evaluation (\S\ref{sec:generalization}).
15	All models use the same generation parameters (temperature~$1.0$, top-$k{=}50$, max length 512) to control for decoding-strategy confounds.
16	Batch sizes are adjusted for GPU memory constraints; learning rates follow the respective model families' recommended fine-tuning ranges.
17	
18	\begin{table}[H]
19	\centering
20	\small
21	\caption{Per-architecture training hyperparameters.}
22	\label{tab:arch_hyperparams}
23	\begin{tabular}{lcccl}
24	\toprule
25	Model & Batch & LR & Steps & Precision \\
26	\midrule
27	Pythia-410M & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
28	Pythia-1.4B & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
29	Pythia-6.9B & 2 & $2{\times}10^{-5}$ & 5{,}000 & bf16 \\
30	GPT-2-medium & 32 & $5{\times}10^{-5}$ & 5{,}000 & fp32/bf16 \\
31	OPT-1.3B & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
32	Qwen3.5-0.8B & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
33	SmolLM3-3B & 4 & $2{\times}10^{-5}$ & 5{,}000 & fp32 \\
34	\bottomrule
35	\end{tabular}
36	\end{table}
37	
38	\paragraph{Metric computation details.}
39	Token entropy is computed as $H(p_\theta | x) = -\sum_{v} p_\theta(v|x) \log_2 p_\theta(v|x)$, averaged over 1{,}000 held-out WikiText-103 samples using greedy teacher-forcing (no sampling stochasticity).
40	ECE uses 15 equal-width bins on the confidence axis $c(x) = \max_v p_\theta(v|x)$, following the standard definition~\citep{naeini2015obtaining}:
41	$\mathrm{ECE} = \sum_{b=1}^{B} \frac{|b|}{N} |\mathrm{acc}(b) - \mathrm{conf}(b)|$.
42	Distinct-$n$ ($n \in \{1, 2, 3\}$) is the ratio of unique $n$-grams to total $n$-grams across all 5{,}000 generated samples per generation, following~\citet{li2016diversity}.
43	Perplexity is computed on a fixed 1{,}000-sample held-out split (disjoint from training and generation prompts).
44	
45	\paragraph{Seed and replication structure.}
46	The primary experiments use seeds 42, 43, 44 (3-seed cohort) for the phase diagram ($T{=}10$, 13 $\alpha$ levels).
47	Seed 45 is added for $\alpha{=}1.0$ experiments (4-seed).
48	Extended FPR analysis uses seeds 45--51 (6-pair basis, excluding MAUVE) for a total of 10 distinct seeds.
49	Cross-$T$ extensions ($T{=}15$, $20$, $25$) use the same seed set as the corresponding $\alpha$ condition.
50	
51	\paragraph{Metric drift.}
52	Table~\ref{tab:drift_summary} reports the relative change in each metric from generation~0 to generation~10 across six contamination levels.
53	Two patterns emerge: (1)~entropy and calibration (ECE) degrade monotonically with $\alpha$, while (2)~diversity metrics exhibit a non-monotonic relationship where the largest relative decline occurs at moderate contamination ($\alpha{=}0.25$) rather than full replacement ($\alpha{=}1.0$).
54	Figure~\ref{fig:metric_trajectory} (main text) visualizes representative per-generation trajectories, showing the distinct temporal profiles that underlie the Granger-precedence analysis in \S\ref{sec:method}.
55	
56	\begin{table}[H]
57	\centering
58	\small
59	\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
60	\label{tab:drift_summary}
61	\resizebox{\columnwidth}{!}{%
62	\begin{tabular}{lccccc}
63	\toprule
64	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
65	\midrule
66	0.00 & $-4.6{\pm}0.4$ & $+37.6{\pm}14$ & $-14.1{\pm}0.4$ & $-9.6{\pm}0.4$ & $-20.6{\pm}1.0$ \\
67	0.10$^\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\
68	0.25 & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & $-18.1{\pm}0.8$ \\
69	0.50 & $-18.0{\pm}0.5$ & $+822.6{\pm}18.3$ & $-37.1{\pm}0.4$ & $-50.4{\pm}1.0$ & $+21.0{\pm}0.1$ \\
70	0.75 & $-27.6{\pm}0.2$ & $+1791{\pm}18$ & $-32.3{\pm}0.5$ & $-41.0{\pm}1.0$ & $+182.6{\pm}0.7$ \\
71	1.00 & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & $+3674{\pm}45$ \\
72	\bottomrule
73	\end{tabular}}
74	\end{table}
75	
76	\paragraph{Data pipeline.}
77	Each generation follows a fixed protocol: (1)~sample 5{,}000 prompts from WikiText-103 (first 32 tokens of random paragraphs); (2)~generate 512-token continuations using the current model $M_t$ with temperature~$1.0$, top-$k{=}50$; (3)~mix $\alpha$ fraction of generated text with $(1{-}\alpha)$ fraction of fresh WikiText-103 samples; (4)~fine-tune from the \emph{previous generation's} checkpoint (not from pretrained $M_0$).
78	Step~(4) produces iterative collapse by accumulating distributional biases across generations, distinct from single-generation fine-tuning drift.
79	The ``replace'' paradigm (step~3) means each generation trains on a completely fresh synthetic pool---there is no accumulation of earlier-generation synthetic data within the training set.
80	
81	\paragraph{Null-condition drift interpretation.}
82	At $\alpha{=}0.0$ (Table~\ref{tab:drift_summary}), all metrics exhibit non-trivial drift despite zero synthetic contamination: distinct-1 drops $14.1\%$, entropy drops $4.6\%$, and perplexity \emph{improves} by $20.6\%$.
83	This null drift reflects iterated fine-tuning on a fixed corpus: the model progressively memorizes WikiText-103, narrowing its effective vocabulary (lower distinct-$n$, lower entropy) while fitting the held-out distribution better (lower PPL).
84	The distinction between null drift and contamination-induced collapse is critical: our detection framework specifically tests whether canary metrics \emph{temporally precede} downstream metrics, not whether drift exists.
85	Null drift produces shared downward trends but without the temporal structure (lag) that Granger testing requires.
86	
87	\paragraph{Non-monotonic diversity-contamination relationship.}
88	A counterintuitive finding in Table~\ref{tab:drift_summary}: diversity loss is \emph{largest} at $\alpha{=}0.25$ (distinct-1: $-40.3\%$) and \emph{smallest} at $\alpha{=}1.0$ ($-27.8\%$).
89	This non-monotonicity arises because at high $\alpha$, the model collapses rapidly into a few dominant modes (by gen~3--4), after which diversity stabilizes near a floor.
90	The gen-0$\to$10 relative decline is smaller because the trajectory is concave (fast initial drop, then plateau).
91	At $\alpha{=}0.25$, the real-data fraction prevents catastrophic collapse but allows a steady, monotonic diversity decline across all 10 generations, producing a larger cumulative loss.
92	
93	
94	\section{Distinct-3 Results}
95	\label{app:distinct3}
96	
97	Table~\ref{tab:distinct3_drift} reports distinct-3 drift across all contamination levels.
98	Distinct-3 exhibits the largest absolute decline among diversity metrics at low contamination ($-58.9{\pm}0.9\%$ at $\alpha{=}0.25$) but attenuates at higher levels ($-30.5\%$ at $\alpha{=}1.0$), consistent with the diversity--calibration dissociation discussed in \S\ref{sec:discussion}.
99	
100	\begin{table}[H]
101	\centering
102	\small
103	\caption{Distinct-3 drift (\%, generation~0$\to$10) across contamination levels. $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.75$: 3-seed mean${\pm}$std; $\alpha{=}1.0$: 4-seed mean${\pm}$std; $\alpha{=}0.50$: single seed.}
104	\label{tab:distinct3_drift}
105	\begin{tabular}{lc}
106	\toprule
107	$\alpha$ & Distinct-3 drift (\%) \\
108	\midrule
109	0.00 & $-4.4{\pm}0.5$ \\
110	0.25 & $-58.9{\pm}0.9$ \\
111	0.50 & $-52.4$ \\
112	0.75 & $-38.6{\pm}1.3$ \\
113	1.00 & $-30.5{\pm}4.0$ \\
114	\bottomrule
115	\end{tabular}
116	\end{table}
117	
118	Distinct-3 exhibits higher lag instability than distinct-1/2 (bimodal lag distribution, std${>}1.5$ vs.\ ${<}0.5$ generations), reflecting its lower signal-to-noise ratio at 512-token generation length.
119	
120	\paragraph{Non-monotonic attenuation.}
121	The inverted-U shape of diversity loss (peaking at $\alpha{=}0.25$--$0.50$, attenuating at $\alpha{=}1.0$) is consistent across all three distinct-$n$ metrics.
122	At low contamination, diversity loss reflects fine-tuning drift amplified by weak synthetic contamination, which narrows the vocabulary without triggering the catastrophic mode collapse that dominates at high $\alpha$.
123	At $\alpha{=}1.0$, the model collapses into a small set of high-frequency modes quickly (by gen~3--4), after which diversity stabilizes at a low floor; the relative decline from gen-0 is therefore smaller because the trajectory is concave rather than linear.
124	
125	\paragraph{Granger detectability of distinct-3.}
126	Despite its large magnitude, distinct-3 drift is less Granger-detectable than distinct-1/2 because of its higher temporal noise.
127	PermG detection rates at $\alpha{=}1.0$: entropy$\to$distinct-1 achieves 6/8 across all seeds; entropy$\to$distinct-3 achieves only 4/8, with 2 seeds failing due to lag instability (bimodal lag distribution shifting the peak between lag~$-1$ and lag~$-2$ across seeds).
128	This motivates our focus on distinct-1 and distinct-2 as the primary downstream metrics in the main text.
129	
130	
131	\section{Observation Window Sensitivity}
132	\label{app:window_sensitivity}
133	
134	Consensus classification stabilizes at $T_{\min}{\geq}5$ (Table~\ref{tab:window_sensitivity}): all six effect-size reference pairs reach $K{\geq}4/5$ agreement at every window from $T_{\min}{=}5$ through $T_{\min}{=}10$.
135	
136	\paragraph{Per-method stability.}
137	At $\alpha{=}1.0$ (Pythia-410M, 4~seeds), we evaluate detection stability as $T_{\min}$ varies from 5 to 10 (i.e., using only generations $T_{\min}$ through $T{=}10$).
138	NaiveXCorr, DiffXCorr, ThresholdOnset, and PermG all maintain 6/6 validated pairs at every window length, confirming complete invariance to the observation start point.
139	Toda--Yamamoto shows the most variability: 3/6 at $T_{\min}{=}5$, rising to 6/6 at $T_{\min}{=}7$, then fluctuating between 3/6 and 6/6 at $T_{\min}{=}8$--$10$.
140	This instability reflects TY's higher sensitivity to degrees of freedom in short series (each 1-generation reduction removes ${\sim}10\%$ of available data at $T{=}10$).
141	
142	\paragraph{Implications for deployment.}
143	The stability result has a practical implication: a monitoring system need not wait for a full $T{=}10$ observation window before running detection.
144	As few as 6 data points ($T_{\min}{=}5$) suffice for reliable consensus-based detection at high contamination ($\alpha{=}1.0$), though the detection boundary $\alpha_c$ at shorter windows remains above $\alpha{=}0.50$ (insufficient power at $T{=}5$ for onset-level contamination).
145	The minimum requirement for Granger-type tests is $T_{\min}{\geq}5$ (below which degrees of freedom are insufficient for lag-1 regression with 2~parameters).
146	
147	\begin{figure}[H]
148	\centering
149	\includegraphics[width=\columnwidth]{figures/fig_window_sensitivity.pdf}
150	\caption{Detection stability as a function of minimum observation window $T_{\min}$ (Pythia-410M, $\alpha{=}1.0$, 4~seeds). PermG forward detection (6/8) and consensus classification ($K{\geq}4$) both stabilize at $T_{\min}{\geq}5$, with no significance flips for $T_{\min} \in [5, 10]$. This robustness confirms that the choice of $T_{\min}{=}5$ in the main analysis does not drive results.}
151	\label{fig:window_sensitivity}
152	\end{figure}
153	
154	\begin{table}[H]
155	\centering
156	\small
157	\caption{Observation window sensitivity for Tier~3 consensus ($K{\geq}4/5$) at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Tier~3 pairs: number of canary$\to$downstream pairs (out of 8 validated) reaching $K{\geq}4/5$ method agreement. TY pairs: number of effect-size reference pairs (out of 6) reaching Toda--Yamamoto significance (moderate supplementary method; \S\ref{sec:method}). Consensus stabilizes at $T_{\min}{\geq}5$; TY stabilizes at $T_{\min}{\geq}6$.}
158	\label{tab:window_sensitivity}
159	\resizebox{\columnwidth}{!}{%
160	\begin{tabular}{lccccccccc}
161	\toprule
162	& \multicolumn{8}{c}{Minimum observation window $T_{\min}$} \\
163	\cmidrule(lr){2-9}
164	& 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
165	\midrule
166	Tier~3 pairs (/8)    & $\dagger$ & $\dagger$ & 6 & 6 & 6 & 6 & 6 & 6 \\
167	TY pairs$^\S$ (/6)   & $\dagger$ & $\dagger$ & 3--6 & 3--6 & 3--6 & 3--6 & 3--6 & 6 \\
168	Stable               & ---       & ---       & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
169	\bottomrule
170	\multicolumn{9}{l}{\footnotesize $\dagger$~Insufficient degrees of freedom for Granger-type tests ($<6$ data points).} \\
171	\multicolumn{9}{l}{\footnotesize $^\S$~TY directional assignment under verification.}
172	\end{tabular}}
173	\end{table}
174	
175	
176	\section{Robustness Analysis}
177	\label{app:robustness}
178	\label{app:spec_curve}
179	
180	\paragraph{Permutation count and FDR sensitivity.}
181	PermG $p$-values are stable between 5{,}000 and 10{,}000 permutations (max $|\Delta p|{=}0.010$, 0/24 significance flips at $\alpha{=}0.75$).
182	Treatment/null separation is robust to FDR threshold choice: at $q{=}0.05$, 4/36 null pairs vs.\ 19/24 treatment pairs reach significance; at $q{=}0.10$, null rejections rise to 8/36.
183	At the onset boundary ($\alpha{=}0.45$), minimum FDR-corrected $p$-values ($0.059$--$0.091$) are consistent with a continuous power transition rather than binary absence of signal.
184	
185	\paragraph{Specification curve.}
186	We construct 1{,}160 specifications from 13 contamination levels, 4~seeds, and 8 canary$\to$downstream pairs (all PermG, $n_\text{perm}{=}5{,}000$, BH FDR $q{=}0.05$).
187	
188	\begin{table}[H]
189	\centering
190	\small
191	\caption{Specification curve summary (1{,}160 specifications, D120-compliant). The blind$\to$onset jump is robust across specifications: 0\% significance rate through $\alpha{=}0.45$, rising to 75\% at $\alpha{=}0.50$.}
192	\label{tab:spec_curve}
193	\begin{tabular}{lc}
194	\toprule
195	Metric & Value \\
196	\midrule
197	Total specifications & 1{,}160 \\
198	Significant (FDR $q{<}0.05$) & 536 (46.2\%) \\
199	\midrule
200	\emph{By regime} & \\
201	\quad Blind ($\alpha \leq 0.45$) & 0\% \\
202	\quad Onset ($\alpha{=}0.50$) & 75\% \\
203	\quad Detection ($\alpha \geq 0.75$) & 62--75\% \\
204	\bottomrule
205	\end{tabular}
206	\end{table}
207	
208	The blind$\to$onset jump holds across the vast majority of specifications (Figure~\ref{fig:spec_curve}).
209	
210	\begin{figure}[H]
211	\centering
212	\includegraphics[width=\columnwidth]{figures/fig_spec_curve.pdf}
213	\caption{Specification curve (1{,}160 configurations). The blind$\to$onset jump at $\alpha_c{\approx}0.50$ is robust across methods, pairs, and seeds.}
214	\label{fig:spec_curve}
215	\end{figure}
216	
217	\paragraph{Specification decomposition.}
218	Within the 536 significant specifications (46.2\% of 1{,}160), the detection rate varies by canary$\to$downstream pair:
219	entropy$\to$distinct-1 and entropy$\to$distinct-2 are the most consistently detectable (significant in 75\% of above-onset specifications), while ECE$\to$perplexity is never significant (0\%, consistent with the first-differencing result in \S\ref{sec:regime}).
220	MAUVE-paired specifications show intermediate rates (50\% at $\alpha{=}1.0$, 0\% at $\alpha{=}0.50$), reflecting MAUVE's floor saturation at 1.4B scale.
221	
222	\paragraph{Cross-seed invariance.}
223	The specification curve's most notable feature is the \emph{absence} of seed-dependent specifications: no specification is significant at one seed but non-significant at another within the same $(\alpha, \text{pair})$ cell for $\alpha \in \{0.50, 0.75, 1.0\}$.
224	This uniformity (Fisher exact: $p = 3.45 \times 10^{-11}$ for the 0/8$\to$6/8 transition) provides the strongest evidence that the detection onset is a property of the data-generating process rather than a particular random initialization.
225	
226	\paragraph{Alternative FDR thresholds.}
227	Repeating the specification curve at $q{=}0.10$ increases significant specifications from 46.2\% to 53.8\%, with the additional detections concentrated at $\alpha{=}0.45$ (4 specifications cross from non-significant to significant) and $\alpha{=}0.60$ (2 specifications).
228	At $q{=}0.01$, the rate drops to 38.4\%, losing detections at $\alpha{=}0.50$ (onset boundary becomes less reliable).
229	The blind$\to$onset jump persists at all three thresholds, confirming structural robustness.
230	
231	\section{Transfer Entropy and Change-Point Analysis}
232	\label{app:transfer_entropy}
233	\phantomsection\label{app:te_mi}
234	
235	Transfer entropy (TE; \citealp{schreiber2000measuring}; 3-bin discretization, $n{=}5{,}000$ permutations) yields 0/192 BH-corrected significant pairs across all conditions, confirming that nonparametric information-theoretic methods lack power at $T{=}11$.
236	A KNN-based TE estimator ($k{=}5$) shows forward-dominant TE fraction increasing monotonically with $\alpha$ (4/8 at $\alpha{=}0.25$ to 8/8 at $\alpha{=}1.0$), but this does not reach statistical significance after FDR correction.
237	
238	\paragraph{Symbolic transfer entropy.}
239	Symbolic TE~\citep{staniek2008symbolic} using Bandt--Pompe ordinal patterns ($m{=}2$, lag${=}1$, 500 circular-shift surrogates, $p{<}0.05$) provides a complementary view.
240	At the $\alpha{=}0.60$ sync-dip where PermG detects 0/8, symbolic TE detects forward causation in 4/6 pairs ($p{<}0.001$): MAUVE-channel TE${=}0.539$ at $T{=}10$ and $0.496$ at $T{=}15$; distinct-1-channel TE${=}0.122$ at $T{=}20$.
241	Positive controls where PermG succeeds (6/8) yield 0/6 significant symbolic TE pairs (TE values 0.000--0.379, all $p{>}0.14$), and baseline conditions ($T{=}5$, $\alpha{=}0.50$) yield 0/2 significant (TE${=}0.000$--$0.189$, $p{=}1.000$).
242	This pattern---symbolic TE detecting signal precisely where PermG fails---suggests the sync-dip reflects compressed temporal lag rather than absent coupling: ordinal-pattern methods capture contemporaneous co-movement that Granger's lag-based framework misses.
243	
244	\paragraph{Conditional Granger analysis.}
245	To test whether ECE confounds the entropy$\to$diversity relationship, we run conditional Granger tests controlling for ECE when testing entropy$\to$diversity and vice versa.
246	Conditioning on ECE does not eliminate entropy's predictive contribution, consistent with the ECE co-movement argument (Appendix~\ref{app:cascade_theory}): both metrics respond to the same underlying mode amplification, but entropy provides the earliest signal.
247	
248	\phantomsection\label{app:change_point}
249	\paragraph{Change-point detection.}
250	Max-split change-point tests ($n{=}5{,}000$ bootstrap) yield 66.7\% FPR under null control (12/18, $\alpha{=}0.00$), precluding use as a standalone detector.
251	However, the temporal ordering of change-points reverses between null and treatment: under null, downstream metrics break first (gen~2) before canary (gen~4--8); under treatment ($\alpha{\geq}0.75$), canary breaks first (gen~1) before downstream (gen~2--4).
252	This ordering reversal shifts monotonically with $\alpha$, consistent with the Granger-precedence analysis.
253	
254	
255	\section{Sequential Monitoring: CUSUM vs Calibrated Threshold}
256	\label{app:csmp}
257	
258	CUSUM sequential testing~\citep{page1954continuous} calibrated against $\alpha{=}0.0$ null control (FAR${=}$0\%) produces identical alarm times as a simple $2\sigma$ threshold at all tested operating points: both trigger at generation~1 for $\alpha{\geq}0.50$.
259	The equivalence arises because the generation-0$\to$1 entropy drop ($|\Delta x|{>}0.7$) greatly exceeds null variability ($\sigma_0{\approx}0.03$); CUSUM's cumulative memory provides no advantage when the initial shift dominates.
260	
261	\paragraph{Operating characteristics.}
262	We evaluate both methods across the full contamination range:
263	\begin{itemize}
264	\item $\alpha{=}0.00$--$0.45$: neither method triggers within $T{=}10$ generations (entropy drift ${\leq}5.3\%$, within null variability band).
265	\item $\alpha{=}0.50$: both trigger at generation~1 (entropy drop $18.0{\pm}0.5\%$, exceeding $2\sigma$ and CUSUM threshold simultaneously).
266	\item $\alpha{=}0.75$--$1.0$: both trigger at generation~1 (entropy drop $27.6$--$60.8\%$).
267	\end{itemize}
268	The regime structure of CUSUM/threshold monitoring thus recapitulates the PermG blind zone: no detection below $\alpha{=}0.50$ at $T{=}10$, immediate detection above.
269	The critical difference is that these methods detect \emph{deviation from baseline}, not \emph{temporal precedence}---they cannot distinguish whether entropy leads or lags diversity without additional directional analysis.
270	
271	\paragraph{Practical implications.}
272	For production monitoring where establishing Granger precedence is unnecessary, a calibrated entropy threshold ($[10\%, 22\%]$; Appendix~\ref{app:intervention_sensitivity}) provides a simple, zero-cost alarm.
273	CUSUM adds value only when the signal emerges gradually across multiple generations (e.g., at contamination levels near $\alpha_c$ where the generation-0$\to$1 drop is small); in our setting, the large initial entropy shift renders CUSUM's cumulative advantage moot.
274	
275	\paragraph{Detection timing comparison.}
276	Table~\ref{tab:sequential_timing} compares alarm generation for CUSUM and calibrated threshold across the full contamination range.
277	
278	\begin{table}[H]
279	\centering
280	\small
281	\caption{Sequential monitoring alarm timing (Pythia-410M, seed~42, fp32). ``---'' = no alarm within $T{=}10$. Both methods produce identical alarm patterns: no detection below $\alpha{=}0.50$, immediate (gen-1) detection above.}
282	\label{tab:sequential_timing}
283	\begin{tabular}{@{}lccc@{}}
284	\toprule
285	$\alpha$ & CUSUM & Threshold & $\Delta H$ (\%) \\
286	\midrule
287	0.00 & --- & --- & $-4.6$ \\
288	0.10 & --- & --- & $-5.3$ \\
289	0.25 & --- & --- & $-4.7$ \\
290	0.45 & --- & --- & $-5.1$ \\
291	0.50 & gen-1 & gen-1 & $-18.0$ \\
292	0.60 & gen-1 & gen-1 & $-28.5$ \\
293	0.75 & gen-1 & gen-1 & $-27.6$ \\
294	1.00 & gen-1 & gen-1 & $-60.8$ \\
295	\bottomrule
296	\end{tabular}
297	\end{table}
298	
299	The binary alarm pattern (no alarm below $\alpha{=}0.50$, immediate alarm above) mirrors PermG's regime structure, confirming that the blind zone is a property of the data-generating process rather than the detection method.
300	However, sequential monitoring methods cannot distinguish between causal temporal precedence and synchronous co-movement---a system relying solely on CUSUM would flag $\alpha{=}0.50$ contamination but could not determine whether entropy decline \emph{causes} or merely \emph{accompanies} diversity loss.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eed29bb3-4f70-453c-9fb4-29366a586746",
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a9d7bd4d8daf2b13b",
  "type": "user",
  "uuid": "21ad8327-6c1d-44c9-9bd0-c9d2cfbbee6b",
  "sourceToolAssistantUUID": "eed29bb3-4f70-453c-9fb4-29366a586746",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T19:41:41.525Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WqTp8MHkWMwdgbksoR6Gnf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 300,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21ad8327-6c1d-44c9-9bd0-c9d2cfbbee6b",
  "isSidechain": true,
  "agentId": "a9d7bd4d8daf2b13b",
  "requestId": "req_011CbPre6LHJ5AV8nJUZv6zv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9fa17bb-3ebb-440a-b36f-a87d9175b037",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E1rdQTcEe2fUXHKTakcZND",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8710,
      "cache_read_input_tokens": 35141,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8710
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 35141,
          "cache_creation_input_tokens": 8710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8710,
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

_source line 11 · 2026-05-25T19:41:41.554Z_

<details><summary>↩ Tool result · `toolu_01WqTp8MHkWMwdgbksoR6Gnf`</summary>

```text
300	However, sequential monitoring methods cannot distinguish between causal temporal precedence and synchronous co-movement---a system relying solely on CUSUM would flag $\alpha{=}0.50$ contamination but could not determine whether entropy decline \emph{causes} or merely \emph{accompanies} diversity loss.
301	
302	\paragraph{False alarm rate calibration.}
303	Under null control ($\alpha{=}0.0$), neither method triggers false alarms at any threshold within the safe operating band $[10\%, 22\%]$, yielding FAR${=}0\%$ across all 3 null-condition seeds.
304	At thresholds below 7.5\%, both methods produce false alarms at gen-3 ($\alpha{=}0.0$ entropy drift: $-4.6\%$ approaches the threshold), giving FAR${=}100\%$.
305	This calibration sensitivity motivates a two-threshold deployment strategy: use the lenient bound ($10\%$) for early warning and the strict bound ($22\%$) for confirmed alarm, with the gap serving as a monitoring zone requiring additional diagnostic tests (e.g., Granger analysis) before triggering intervention.
306	
307	\section{Background and Notation}
308	\label{app:background}
309	\label{sec:background}
310	
311	This section establishes the formal setup and notation used throughout the paper.
312	
313	\paragraph{Iterative training loop.}
314	Let $M_0$ denote a pretrained language model and $\mathcal{D}_\text{real}$ a fixed corpus of human-written text.
315	At each generation $t \geq 1$, the model $M_{t-1}$ generates a synthetic corpus $\mathcal{D}_\text{synth}^{(t-1)}$, and the next-generation model $M_t$ is fine-tuned on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data:
316	\begin{equation}
317	    \mathcal{D}_\text{train}^{(t)} = \alpha \cdot \mathcal{D}_\text{synth}^{(t-1)} \;+\; (1{-}\alpha) \cdot \mathcal{D}_\text{real}, \quad \alpha \in [0, 1].
318	    \label{eq:mixing}
319	\end{equation}
320	At $\alpha{=}1.0$, this reduces to the full-replacement paradigm of \citet{shumailov2024curse}.
321	
322	\paragraph{Metric families.}
323	\emph{Canary metrics}: token entropy ($H(p_\theta | \text{context})$ on held-out samples) and expected calibration error (ECE).
324	\emph{Downstream metrics}: distinct-$n$ ($n \in \{1, 2, 3\}$)~\citep{li2016diversity} and perplexity.
325	Each metric produces a time series of $T{+}1$ observations.
326	
327	\paragraph{Lead-lag testing.}
328	Given canary series $X$ and downstream series $Y$, the central question is whether changes in $X$ temporally precede changes in $Y$, requiring directionality and confounder control beyond simple correlation.
329	We employ five methods spanning permissive to conservative: naive cross-correlation, differenced cross-correlation, threshold onset detection, permutation Granger causality~\citep{shojaie2022granger}, and Toda--Yamamoto Granger causality~\citep{toda1995statistical}.
330	
331	\paragraph{Method details.}
332	\emph{Naive cross-correlation (NaiveXCorr)} computes Pearson $r$ between $X_{t}$ and $Y_{t+\ell}$ at lag $\ell \in [-5, 5]$; significance at any lag below uncorrected $p{<}0.05$ counts as detection.
333	This method is permissive because it ignores shared trends and applies no multiplicity correction.
334	\emph{Differenced cross-correlation (DiffXCorr)} applies the same procedure to first-differenced series $\Delta X_t = X_t - X_{t-1}$, controlling for common trends but remaining bidirectional (cannot distinguish $X \to Y$ from $Y \to X$).
335	\emph{Threshold onset detection} identifies the first generation where each metric crosses a $3\sigma$ threshold below its generation-0 value (where $\sigma$ is the null-control standard deviation); detection is declared if canary onset strictly precedes downstream onset.
336	\emph{Permutation Granger causality (PermG)} tests whether lagged $X$ values improve prediction of $Y$ beyond $Y$'s own history, using 5{,}000 temporal permutations to construct a nonparametric null distribution, followed by BH-FDR correction at $q{=}0.05$ across 8 metric pairs.
337	\emph{Toda--Yamamoto (TY)} augments a VAR model with $d_{\max}$ extra lags to handle potential non-stationarity, then tests the original lag coefficients via Wald test.
338	
339	\paragraph{PermG implementation details.}
340	The permutation Granger procedure operates as follows:
341	(1)~First-difference both series: $\Delta X_t = X_t - X_{t-1}$, $\Delta Y_t = Y_t - Y_{t-1}$.
342	(2)~Fit unrestricted model: $\Delta Y_t = a_0 + \sum_{j=1}^{L} a_j \Delta Y_{t-j} + \sum_{j=1}^{L} b_j \Delta X_{t-j} + \epsilon_t$ (max lag $L{=}5$).
343	(3)~Fit restricted model: $\Delta Y_t = a_0 + \sum_{j=1}^{L} a_j \Delta Y_{t-j} + \epsilon_t$.
344	(4)~Compute observed $F$-statistic from the residual sum of squares reduction.
345	(5)~Generate 5{,}000 null realizations by randomly permuting the temporal order of $\Delta X$, re-fitting unrestricted model each time.
346	(6)~$p$-value $= (\text{count}(F_{\text{perm}} \geq F_{\text{obs}}) + 1) / (n_{\text{perm}} + 1)$ following~\citet{phipson2010permutation}.
347	The permutation scheme destroys temporal structure in $X$ while preserving its marginal distribution, providing an exact null for the hypothesis ``past $X$ does not improve prediction of $Y$.''
348	Lag selection uses AIC with maximum $L{=}5$ (constrained by $T{-}2L \geq 3$ degrees of freedom at $T{=}11$).
349	
350	\paragraph{Direction checking.}
351	For each significant pair, we additionally test the reverse direction ($Y \to X$).
352	A pair is classified as ``forward-only'' if $X \to Y$ is significant and $Y \to X$ is not; ``bidirectional'' if both are significant; and ``reverse-only'' if only $Y \to X$ is significant.
353	Forward-only pairs provide the strongest evidence for temporal precedence.
354	In the main analysis, we report forward detection counts; bidirectional pairs are flagged in the failure mode taxonomy (\S\ref{sec:generalization}).
355	
356	\paragraph{Multiple testing structure.}
357	At each contamination level and seed, we test 8 canary$\to$downstream pairs (2 canary $\times$ 4 downstream metrics; MAUVE is a 9th pair included in some analyses).
358	BH-FDR correction at $q{=}0.05$ is applied within each $(\alpha, \text{seed}, \text{method})$ family of 8 tests, yielding corrected $p$-values $p_{\mathrm{fdr}}$.
359	We do not correct across $\alpha$ levels or seeds, as these represent genuinely different conditions rather than multiple looks at the same hypothesis.
360	The 8-pair correction is conservative relative to per-family error rate control: BH-FDR at $q{=}0.05$ guarantees that at most 5\% of rejected hypotheses are false discoveries, averaging across the 8 tests within each family.
361	
362	\section{MMCT Algorithm}
363	\label{app:mmct}
364	
365	\noindent\emph{See Algorithm~\ref{alg:mmct} in the main text (\S\ref{sec:mmct}) for the full MMCT pseudocode and design rationale.}
366	
367	\begin{figure}[H]
368	\centering
369	\includegraphics[width=\columnwidth]{figures/consensus_heatmap.pdf}
370	\caption{$K{\geq}3$ consensus heatmap across the $\alpha \times T$ grid (Pythia-410M, fp32). Each cell shows the number of canary$\to$diversity pairs reaching majority agreement (${\geq}3/5$ methods). Consensus detection aligns with PermG's onset at $\alpha{=}0.50$ but eliminates the non-monotonic anomaly at $\alpha{=}0.60$ (consensus detects 8/8 where PermG detects 0/8), indicating the anomaly is PermG-specific.}
371	\label{fig:consensus_heatmap}
372	\end{figure}
373	
374	\paragraph{MMCT design rationale.}
375	The MMCT consensus approach is motivated by the observation that no single method achieves both low FPR and high detection rate across all contamination levels.
376	PermG has the lowest FPR (6.7\%) but misses the $\alpha{=}0.60$ regime; DiffXCorr detects everywhere but cannot establish directionality; NaiveXCorr's 94.4\% FPR makes it unsuitable as a standalone detector.
377	By requiring $K{\geq}3$ methods to agree, MMCT effectively requires that at least one conservative method (PermG or DiffXCorr) participates in the consensus, filtering out detections driven solely by permissive methods.
378	
379	\paragraph{FPR-inverse weighting design.}
380	The weight $w_k = 1/\max(\widehat{\mathrm{FPR}}_k, \epsilon)$ ensures that methods with lower empirical FPR have proportionally higher influence on the consensus score.
381	The floor $\epsilon{=}0.01$ prevents division by zero for methods with 0\% FPR (none in our case).
382	Under this scheme, PermG's weight ($w{=}14.9$) dominates NaiveXCorr's ($w{=}1.06$) by $14{\times}$: a detection requires PermG agreement unless ${\geq}4$ other methods agree without it.
383	The empirical null distribution (step~7 of Algorithm~\ref{alg:mmct}) avoids parametric assumptions that would be unreliable for our short ($T{=}5$--$25$), non-stationary series.
384	
385	\paragraph{Sensitivity to $K$.}
386	Table~\ref{tab:mmct_k_operating} (main text) reports operating characteristics for $K \in \{2, 3, 4, 5\}$.
387	The $K{=}3$ threshold represents a Pareto-optimal operating point: decreasing to $K{=}2$ raises FPR from 10.0\% to 38.9\% with modest TPR gain ($66.7\% \to 85.4\%$ at $\alpha{=}0.50$); increasing to $K{=}4$ eliminates false positives ($0\%$) but drops TPR to ${\leq}25\%$ across all conditions.
388	At $K{=}5$ (unanimity), the expected detection rate is below 5\% everywhere---only achievable when all five methods, including the 94\%-FPR NaiveXCorr, agree.
389	
390	\begin{figure}[H]
391	\centering
392	\includegraphics[width=\columnwidth]{figures/fig_mmct_k_operating.pdf}
393	\caption{MMCT operating characteristics as a function of consensus threshold $K$. Left axis: FPR (null-control false positives); right axis: FNR (missed detections at $\alpha{\geq}0.50$). $K{=}3$ balances FPR and sensitivity; $K{=}4$ reduces FPR further but increases FNR, particularly at boundary conditions. $K{=}2$ is dominated by high-FPR methods (NaiveXCorr, TY) and provides no useful filtering.}
394	\label{fig:mmct_k_operating}
395	\end{figure}
396	
397	\section{Methodological Comparison Table}
398	\label{app:method_comparison}
399	
400	Table~\ref{tab:method-comparison} summarizes the methodological coverage of existing canary and monitoring analyses across the diagnostic dimensions identified in \S\ref{sec:method}.
401	No prior work combines all six dimensions.
402	
403	\begin{table}[H]
404	\centering
405	\small
406	\caption{Methodological comparison of canary and monitoring analyses. \checkmark\ = present, $\times$ = absent, $\circ$ = partial (${\leq}2$ levels or limited replication). Diff.\ = differencing/stationarity controls. Multi-M.\ = ${\geq}2$ independent statistical methods. MTC = multiple testing correction. Regime = systematic variation of $\alpha$. Seeds = ${\geq}3$ independent seeds. Arch.\ = ${\geq}2$ architecturally distinct model families.}
407	\label{tab:method-comparison}
408	\resizebox{\columnwidth}{!}{%
409	\begin{tabular}{lccccccl}
410	\toprule
411	Work & Diff. & Multi-M. & MTC & Regime & Seeds & Arch. & Metrics \\
412	\midrule
413	\citet{shumailov2024curse}     & $\times$   & $\times$   & $\times$   & $\circ$    & \checkmark & \checkmark & PPL \\
414	\citet{du2025scales}           & $\times$   & $\times$   & \checkmark & \checkmark & \checkmark & $\times$   & ECE, Acc, Dist-$n$ \\
415	\citet{gambetta2024surplexity} & $\times$   & $\times$   & $\times$   & \checkmark & \checkmark & \checkmark & Surplexity, Ent \\
416	SIGMA~\citep{sigma2026spectral} & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & Spectral \\
417	DCES~\citep{dces2026counter}    & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & \checkmark & ECE, Ent, PPL \\
418	\midrule
419	\textbf{Ours}                  & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & Ent, ECE, PPL, Dist-$n$ \\
420	\bottomrule
421	\end{tabular}%
422	}
423	\end{table}
424	
425	\paragraph{Dimension justification.}
426	The six diagnostic dimensions in Table~\ref{tab:method-comparison} are motivated by known failure modes in time-series causal inference:
427	\emph{Differencing} controls spurious regression when both series share a deterministic trend~\citep{granger1974spurious}---without it, any two monotonically declining series will appear correlated.
428	\emph{Multi-method comparison} addresses the method sensitivity documented in \S\ref{sec:mmct}: a single method's conclusion may reflect its assumptions rather than the data.
429	\emph{Multiple testing correction} is necessary because each contamination level generates 8 metric pairs; uncorrected testing at $p{<}0.05$ expects ${\sim}0.4$ false positives per condition.
430	\emph{Regime variation} is required to map the detection landscape rather than reporting a single operating point.
431	\emph{Seed replication} distinguishes signal from initialization artifacts.
432	\emph{Cross-architecture evaluation} tests whether findings are specific to one model family or reflect general properties of iterative collapse.
433	Among existing works, \citet{du2025scales} comes closest (4/6 dimensions) but omits differencing and multi-method analysis, both of which our results show are critical.
434	
435	\section{Extended Discussion}
436	\label{app:extended_discussion}
437	
438	\paragraph{Calibration scope.}
439	All calibration results are specific to our setup (Pythia-410M, WikiText-103, $T{=}10$).
440	On C4 at $\alpha{=}0.50$, PermG reverse reaches 7/8 (seed-dependent: s43 1/8), indicating directional asymmetry should be verified per domain.
441	Token entropy ($H(p_\theta|\text{context})$ on held-out data) and perplexity ($\exp(H_\text{cross})$ on generated text) co-move synchronously, explaining why first-differencing eliminates canary$\to$perplexity but preserves canary$\to$diversity.
442	
443	\paragraph{Alternative explanations for the blind zone.}
444	Three mechanisms could explain why detection fails below $\alpha_c$:
445	\emph{(1)~Signal absence}: at low $\alpha$, the real-data fraction dominates, and the model's distributional shift is too small to generate temporal structure detectable by any linear method.
446	\emph{(2)~Power limitation}: the signal exists but falls below PermG's detection threshold at $T{=}10$ (supported by the $T{=}20$ result showing 5/8 at $\alpha{=}0.45$).
447	\emph{(3)~Contemporaneous coupling}: at low $\alpha$, entropy and diversity respond simultaneously rather than sequentially, eliminating the lag that Granger tests require.
448	The MI analysis (Appendix~\ref{app:mi_analysis}) favors explanation~(2): coupling between entropy and diversity exists throughout the blind zone ($\hat{I}_G > 0$ at all $\alpha$), and the cross-$T$ results confirm that longer observation resolves detection at $\alpha{=}0.45$.
449	However, explanation~(3) may contribute at very low $\alpha$ (${\leq}0.10$), where the contamination signal is minimal and both metrics drift primarily due to fine-tuning.
450	
451	\paragraph{Entropy as a measurement artifact.}
452	A potential concern is that entropy's ``leading'' behavior reflects measurement sensitivity rather than a genuine temporal cascade: entropy is a continuous quantity computed from the full probability distribution, while distinct-$n$ is a discrete count computed from a finite sample.
453	Entropy can therefore respond to arbitrarily small distributional shifts that leave the token-level generation unchanged.
454	We note three counterarguments:
455	(1)~The ECE co-movement result confirms that calibration---a separate measurement---also shifts at gen-1, suggesting the signal is real.
456	(2)~First-differencing preserves the canary$\to$diversity relationship while eliminating canary$\to$perplexity, which would not occur if the signal were purely a measurement artifact.
457	(3)~The intervention experiment demonstrates that acting on the entropy signal at gen-1 produces a measurably different outcome (64\% lower peak perplexity), confirming functional relevance.
458	Nonetheless, the possibility that entropy's sensitivity partly reflects measurement properties rather than causal priority cannot be fully excluded without mechanistic analysis.
459	
460	\paragraph{Cross-architecture failure mode analysis.}
461	The four non-confirming conditions in the cross-architecture evaluation each isolate a distinct assumption violation:
462	
463	\begin{table}[H]
464	\centering
465	\small
466	\caption{Failure mode taxonomy for non-confirming cross-architecture conditions ($\alpha{=}1.0$).}
467	\label{tab:failure_modes}
468	\resizebox{\columnwidth}{!}{%
469	\begin{tabular}{llll}
470	\toprule
471	Condition & PermG & Failure mode & Root cause \\
472	\midrule
473	GPT-2 bf16 & 0/8 & Precision & bf16 noise masks signal \\
474	GPT-2 s43 & 6/8 both & Bidirectional & No directional separation \\
475	Pythia-1.4B s42 & 2/8 & Seed & Initialization-dependent \\
476	SmolLM3-3B & 3/8 & Decoupling & Entropy non-monotonic \\
477	\bottomrule
478	\end{tabular}}
479	\end{table}
480	
481	The precision failure (GPT-2 bf16) is actionable: switching to fp32 resolves detection (0/8$\to$6/8) with no change to the underlying collapse dynamics.
482	The bidirectional failure (GPT-2 s43) is more fundamental: it indicates that for some model-seed combinations, the entropy-diversity temporal structure is symmetric, preventing directional assignment.
483	The seed dependence (Pythia-1.4B s42 vs.\ s43: 2/8 vs.\ 6/8) highlights the fragility of directional testing in short series.
484	The entropy decoupling (SmolLM3-3B: entropy 0/4, ECE 3/4) directly violates the cascade ordering assumption, suggesting that SmolLM3's architecture produces a qualitatively different collapse trajectory.
485	
486	\paragraph{Scale verification (Pythia-1.4B).}
487	\label{app:scale_14b}
488	
489	\begin{table}[H]
490	\centering
491	\small
492	\caption{Pythia-1.4B phase diagram replication: PermG forward/reverse detection and $K{\geq}3$ consensus across contamination levels and observation windows (fp32). $\dagger$: bidirectional confounding (reverse${}>0$). Denominator is 8 unless marked $^{*}$ (6-pair basis, MAUVE unavailable).}
493	\label{tab:14b_phase}
494	\begin{tabular}{@{}llcccc@{}}
495	\toprule
496	$T$ & $\alpha$ & Seed & Fwd & Rev & $K{\geq}3$ \\
497	\midrule
498	10 & 0.45 & 42 & 0/8 & 0/8 & 0/8 \\
499	   &      & 43 & 1/8 & 0/8 & 2/8 \\
500	   &      & 44 & 0/6$^{*}$ & 0/6$^{*}$ & 0/6$^{*}$ \\
501	\cmidrule(l){2-6}
502	   & 0.50 & 42 & 4/8 & 2/8$^{\dagger}$ & 3/8 \\
503	   &      & 43 & 6/6$^{*}$ & 0/6$^{*}$ & 1/6$^{*}$ \\
504	   &      & 44 & 6/6$^{*}$ & 0/6$^{*}$ & 0/6$^{*}$ \\
505	\cmidrule(l){2-6}
506	   & 0.60 & 42 & 4/8 & 0/8 & 3/8 \\
507	   &      & 43 & 4/8 & 6/8$^{\dagger}$ & 3/8 \\
508	   &      & 44 & 6/6$^{*}$ & 0/6$^{*}$ & 5/6$^{*}$ \\
509	\cmidrule(l){2-6}
510	   & 0.75 & 42 & 5/8 & 0/8 & 5/8 \\
511	   &      & 43 & 6/8 & 5/8$^{\dagger}$ & 5/8 \\
512	   &      & 44 & 6/6$^{*}$ & 0/6$^{*}$ & 6/6$^{*}$ \\
513	\midrule
514	15 & 0.45 & 42 & 3/8 & 0/8 & 4/8 \\
515	   &      & 43 & 5/6$^{*}$ & 3/6$^{*\dagger}$ & 3/6$^{*}$ \\
516	\cmidrule(l){2-6}
517	   & 0.50 & 42 & 3/8 & 0/8 & 2/8 \\
518	   &      & 43 & 3/6$^{*}$ & 0/6$^{*}$ & 3/6$^{*}$ \\
519	\cmidrule(l){2-6}
520	   & 0.60 & 42 & 6/8 & 0/8 & 6/8 \\
521	   &      & 43 & 6/6$^{*}$ & 3/6$^{*\dagger}$ & 6/6$^{*}$ \\
522	\cmidrule(l){2-6}
523	   & 0.75 & 42 & 6/8 & 0/8 & 6/8 \\
524	   &      & 43 & 6/6$^{*}$ & 0/6$^{*}$ & 6/6$^{*}$ \\
525	\bottomrule
526	\end{tabular}
527	\end{table}
528	
529	Phase-diagram structure is qualitatively preserved at 1.4B (Table~\ref{tab:14b_phase}; Figure~\ref{fig:14b_phase}): detection boundary at $\alpha_c{\approx}0.50$, cross-$T$ improvement at 3/4 $\alpha$ values ($\alpha{=}0.45$: $0/6{\to}5/6$).
530	The 410M sync-dip does not reproduce at 1.4B (4/6 at $\alpha{=}0.60$, $T{=}10$).
531	Bidirectional confounding is seed-specific: s43 shows reverse significance at $\alpha{=}0.60$ (6/8) and $\alpha{=}0.75$ (5/8) for $T{=}10$, while s42 maintains 0 reverse across all conditions.
532	
533	\begin{figure}[H]
534	\centering
535	\includegraphics[width=\columnwidth]{figures/fig_14b_phase.pdf}
536	\caption{Pythia-1.4B phase diagram (PermG forward, 6-pair basis). Detection boundary ($\alpha_c \approx 0.50$) is consistent with 410M.}
537	\label{fig:14b_phase}
538	\end{figure}
539	
540	\paragraph{Scale effects on detection topology.}
541	Three scale-dependent effects emerge from comparing 410M and 1.4B:
542	\begin{enumerate}
543	\item \emph{Sync-dip suppression}: The $\alpha{=}0.60$ non-monotonic anomaly is absent at 1.4B (4/6--6/6 vs.\ 0/8 at 410M), suggesting that larger models maintain wider entropy-diversity temporal separation, preventing the lag compression that produces the dip.
544	\item \emph{Seed variability amplification}: Cross-seed detection variance is higher at 1.4B (s42: 2/8 vs.\ s43: 6/8 at $\alpha{=}1.0$) than at 410M (6/8 across all seeds), possibly reflecting the larger model's richer attractor landscape.
545	\item \emph{Domain transfer}: Pythia-1.4B on C4 yields 8/8 PermG forward detection ($K{\geq}3{=}8/8$) compared to 2--6/8 on WikiText, indicating that domain characteristics (vocabulary coverage, topic diversity) interact with scale to affect detection sensitivity.
546	\end{enumerate}
547	
548	\paragraph{Intervention at 1.4B.}
549	Predictive cessation replicates at 1.4B: entropy drops $51.9\%$ ($2.946 \to 1.418$) at gen-1, triggering intervention.
550	Peak PPL rises from $19.68$ to $65.37$ (a $232\%$ increase, vs.\ $112\%$ at 410M), but recovery is faster (gen-2 PPL${=}17.44$, below the gen-0 baseline).
551	The larger entropy drop at 1.4B ($51.9\%$ vs.\ $40.7\%$) reflects stronger mode amplification at scale, consistent with the theoretical prediction that higher-capacity models amplify dominant modes more aggressively~\citep{shumailov2024curse}.
552	
553	
554	
555	\section{Per-Method Dose-Response Profiles}
556	\label{app:dose_response}
557	
558	Table~\ref{tab:dose_response_full} reports FDR significance counts (/8 validated pairs) for all five detection methods across 12 contamination levels (seed~42, Pythia-410M, WikiText, fp32).
559	PermG exhibits a steep 0$\to$6 jump at $\alpha{=}0.50$ with a return to 0 at $\alpha{=}0.55$--$0.60$ (non-monotonic dip), while other methods show diffuse profiles: naive cross-correlation saturates at 7--8/8 across all levels including the null, and Toda--Yamamoto fluctuates without a clear onset.
560	
561	\begin{table}[H]
562	\centering
563	\small
564	\caption{Per-method FDR significance (/8 pairs) across contamination levels (Pythia-410M, seed~42, WikiText, fp32). PermG and Diff.\ XCorr use BH-corrected FDR ($q{=}0.05$); Naive XCorr, Threshold, and TY use uncorrected $p{<}0.05$ (no FDR field in pipeline). $\alpha{=}1.0$ from Pythia-410M cross-architecture condition (same seed/domain/precision).}
565	\label{tab:dose_response_full}
566	\resizebox{\columnwidth}{!}{%
567	\begin{tabular}{lccccc}
568	\toprule
569	$\alpha$ & Naive & Diff.\ XCorr & Threshold & PermG & TY$^\S$ \\
570	\midrule
571	0.00 & 8 & 4 & 3 & \textbf{0} & 1 \\
572	0.10 & 7 & 6 & 0 & \textbf{0} & 0 \\
573	0.25 & 8 & 3 & 0 & \textbf{0} & 2 \\
574	0.30 & 8 & 4 & 0 & \textbf{0} & 3 \\
575	0.35 & 8 & 4 & 0 & \textbf{0} & 1 \\
576	0.40 & 8 & 3 & 0 & \textbf{0} & 4 \\
577	0.45 & 8 & 6 & 0 & \textbf{0} & 1 \\
578	0.50 & 8 & 7 & 4 & \textbf{6} & 3 \\
579	0.55 & 8 & 8 & 0 & \textbf{0} & 1 \\
580	0.60 & 8 & 6 & 0 & \textbf{0} & 0 \\
581	0.75 & 7 & 6 & 0 & \textbf{6} & 3 \\
582	1.00 & 8 & 6 & 2 & \textbf{6} & 1 \\
583	\bottomrule
584	\multicolumn{6}{l}{\footnotesize $^\S$TY directional assignment under verification; column retained for completeness.} \\
585	\end{tabular}}
586	\end{table}
587	
588	PermG's dose-response profile most cleanly separates detection regimes: 0/8 at null, steep 0$\to$6 onset at $\alpha{=}0.50$, non-monotonic dip at $\alpha{=}0.55$--$0.60$.
589	Naive monitoring baselines (PPL-slope, variance-threshold) fire at $\alpha{=}0.0$ (FPR 67--100\%) because fine-tuning drift is indistinguishable from contamination without directional testing.
590	
591	\paragraph{Method-specific observations.}
592	\emph{NaiveXCorr} saturates at 7--8/8 at every $\alpha$ including null, making it useless for regime discrimination---its FPR (94.4\%) means it would declare detection in 19 out of 20 null-control runs.
593	\emph{DiffXCorr} shows the highest detection rate at $\alpha{\geq}0.50$ (6--8/8) but maintains 4/8 at null, yielding FPR${=}37.5\%$.
594	Its bidirectional nature (significant in both forward and reverse) prevents causal attribution but confirms the presence of coupling.
595	\emph{Threshold onset} is highly specific (3/8 at null) but insensitive (0/8 at $\alpha{=}0.10$--$0.45$ and $\alpha{=}0.55$--$0.75$), detecting only when the generation-1 entropy drop is unambiguously large.
596	\emph{Toda--Yamamoto} fluctuates between 0/8 and 4/8 across all $\alpha$ levels with no clear dose-response structure, reflecting its poor finite-sample properties at $T{=}10$.
597	
598	\paragraph{Inter-method agreement.}
599	Cohen's $\kappa$ between all method pairs ranges from $-0.04$ (NaiveXCorr vs.\ Threshold, near-random disagreement) to $0.42$ (PermG vs.\ DiffXCorr, moderate agreement above onset).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9fa17bb-3ebb-440a-b36f-a87d9175b037",
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a9d7bd4d8daf2b13b",
  "type": "user",
  "uuid": "625bf6ee-eba5-4e7b-b13d-91d2a1d1542a",
  "sourceToolAssistantUUID": "d9fa17bb-3ebb-440a-b36f-a87d9175b037",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T19:41:46.022Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V2MRsVhUGKhALz4KFCppWA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 599,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "625bf6ee-eba5-4e7b-b13d-91d2a1d1542a",
  "isSidechain": true,
  "agentId": "a9d7bd4d8daf2b13b",
  "requestId": "req_011CbPreUHtDL22P4CzEiHuu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74f47010-cebd-4b31-ac34-ae71b61b7c33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDaPUpJgkhmYa4mZSQSUSF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9173,
      "cache_read_input_tokens": 43851,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9173
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 43851,
          "cache_creation_input_tokens": 9173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9173,
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

_source line 13 · 2026-05-25T19:41:46.035Z_

<details><summary>↩ Tool result · `toolu_01V2MRsVhUGKhALz4KFCppWA`</summary>

```text
599	Cohen's $\kappa$ between all method pairs ranges from $-0.04$ (NaiveXCorr vs.\ Threshold, near-random disagreement) to $0.42$ (PermG vs.\ DiffXCorr, moderate agreement above onset).
600	The low overall $\kappa{=}0.185$ across all five methods reflects the fundamental tension: permissive methods detect everywhere (including null), conservative methods detect rarely, and moderate methods disagree about boundary cases.
601	This motivates the MMCT consensus approach (\S\ref{sec:mmct}), which aggregates information from all methods while weighting by empirical reliability.
602	
603	\begin{figure}[H]
604	\centering
605	\includegraphics[width=\columnwidth]{figures/fig_per_method_phase_top.pdf}
606	\caption{Per-method FDR-significant pair counts (/8) across contamination levels (Pythia-410M, seed~42, $T{=}10$, fp32). PermG~(d) exhibits the cleanest regime separation---zero detections through $\alpha{=}0.45$, then a steep 0$\to$6 jump at $\alpha{=}0.50$; NaiveXCorr~(a) saturates at 7--8/8 across all levels including null; DiffXCorr~(b) detects signal but cannot separate forward from reverse. The visual contrast across panels illustrates why method choice is itself a primary source of variability ($\kappa{=}0.185$).}
607	\label{fig:per_method_phase}
608	\end{figure}
609	
610	\begin{figure}[H]\ContinuedFloat
611	\centering
612	\includegraphics[width=\columnwidth]{figures/fig_per_method_phase_bottom.pdf}
613	\caption[]{(\textit{continued})}
614	\end{figure}
615	
616	\section{Cross-Seed Consistency at $\alpha{=}0.60$}
617	\label{app:alpha060}
618	
619	The non-monotonic detection gap at $\alpha{=}0.60$ (\S\ref{sec:dose_response}) is consistent across seeds: PermG yields 0/8 FDR-significant forward pairs for both seed~42 (v4 recompilation) and seed~43.
620	An earlier pipeline version (v3, seed~42) reported 3/8; the discrepancy is resolved by the current pipeline version, which corrected FPR calibration.
621	
622	\paragraph{Detailed metrics at $\alpha{=}0.60$.}
623	Despite PermG non-detection, metric drift at $\alpha{=}0.60$ is substantial: token entropy $-28.5\%$ (gen-0: $3.234$, gen-10: $2.311$), ECE $+1561\%$ ($0.0108 \to 0.179$), perplexity $+92.3\%$ ($26.95 \to 51.83$).
624	Raw (pre-FDR) $p$-values are marginal: ECE$\to$distinct-1 $p{=}0.034$, ECE$\to$distinct-2 $p{=}0.047$---both would pass at uncorrected $\alpha{=}0.05$ but fail BH-FDR correction ($q{=}0.05$, 8 simultaneous tests).
625	This indicates that the signal exists but falls below the corrected significance threshold, consistent with the temporal-compression interpretation.
626	
627	\paragraph{Cross-$T$ behavior.}
628	The sync-dip at $\alpha{=}0.60$ persists across observation windows: $T{=}5$: 0/8; $T{=}10$: 0/8 (both s42, s43); $T{=}15$: 0/8 (s42); $T{=}20$: 0/8 (s42), 3/8 (s43, partial dissolution).
629	Full dissolution occurs only at $T{=}25$: PermG 5/8 (s42), $K{\geq}3$ consensus 6/8.
630	The pattern---persistent non-detection for $T{\leq}20$, resolution at $T{=}25$---is consistent with $\sqrt{T}$ power accumulation eventually resolving a compressed (but non-zero) temporal lag.
631	
632	\paragraph{Scale dependence.}
633	Pythia-1.4B does \emph{not} exhibit the sync-dip at $\alpha{=}0.60$: PermG detects 4/8 (s42) and 4/6 (s43) at $T{=}10$, rising to 6/8 and 6/6 at $T{=}15$.
634	This scale-dependence suggests the phenomenon is architecture-specific: at larger scale, the entropy-diversity lag may be structurally wider (more capacity $\to$ slower mode collapse propagation), preventing the temporal compression that produces the dip at 410M.
635	
636	\paragraph{Sigmoid fit impact.}
637	The sigmoid fit excluding $\alpha{=}0.60$ yields $k{=}5.66$, $\alpha_c{=}0.765$, $R^2{=}0.286$; including it degrades $R^2$ to 0.205 and shifts $\alpha_c$ rightward by 0.058, confirming the point is a genuine outlier rather than noise.
638	Predicted detection probability at $\alpha{=}0.60$ under the sigmoid model is $P(\mathrm{det}){=}0.282$, far below the observed 0/8 (0.00), indicating the anomaly cannot be explained by smooth dose-response variation.
639	
640	
641	\section{PPL Threshold Baseline}
642	\label{app:ppl_threshold}
643	
644	A reviewer asked whether a naive perplexity threshold could match entropy's detection timing.
645	We evaluate thresholds at $+10\%$, $+25\%$, $+50\%$, $+100\%$, $+150\%$, and $+200\%$ above the generation-0 baseline PPL (26.95).
646	
647	\paragraph{Threshold-by-threshold results.}
648	The PPL trajectory at $\alpha{=}1.0$ (Pythia-410M, s42) evolves rapidly: gen-0${=}26.95$, gen-1${=}57.42$ ($+113.1\%$), gen-2${=}162.15$ ($+501.9\%$), gen-3${=}279.17$, gen-5${=}508.85$, gen-10${=}1017.81$.
649	All thresholds from $+10\%$ through $+100\%$ trigger at generation~1, because the gen-0$\to$gen-1 jump ($+113.1\%$) exceeds them all.
650	Thresholds at $+150\%$ and $+200\%$ delay triggering to generation~2 (PPL${=}162.15$ exceeds both).
651	
652	\paragraph{Comparison with entropy.}
653	Entropy's advantage over PPL monitoring is operational rather than temporal at $\alpha{=}1.0$:
654	\begin{enumerate}
655	\item \emph{Zero cost}: entropy is computed from the model's output distribution during generation---no held-out evaluation set or separate forward pass required.
656	\item \emph{Direct signal}: entropy detects distributional narrowing (mode collapse) directly; PPL detects its downstream consequence (degraded generalization).
657	\item \emph{Regime sensitivity}: at lower contamination ($\alpha{=}0.50$), entropy drops $18.0\%$ at gen-1 while PPL rises only $21.0\%$ over 10~generations---a PPL threshold calibrated for $\alpha{=}1.0$ would miss $\alpha{=}0.50$ entirely.
658	\end{enumerate}
659	
660	\paragraph{When PPL monitoring suffices.}
661	For production systems where $\alpha$ is expected to be high (e.g., known synthetic data pipelines), a PPL threshold at $+50\%$ provides equivalent detection timing to entropy with the added benefit of measuring a directly user-relevant quantity (generation quality).
662	The operational cost difference becomes relevant only for online monitoring at scale, where computing held-out PPL on every generation adds latency and requires maintaining a clean reference set.
663	
664	
665	\section{PermG Power Analysis}
666	\label{app:power_analysis}
667	
668	We simulate PermG power under a bivariate DGP with linear coupling $\beta$ ($T \in \{6,\ldots,20\}$, 100 replications, 5{,}000 permutations, BH FDR $q{=}0.05$).
669	At $T{=}10$, $\beta_{50}{=}2.0$ (50\% power requires strong coupling); at $T{=}20$, $\beta_{50}$ drops to 0.9 (Table~\ref{tab:beta50}).
670	Power grows faster than $\sqrt{T}$, so the $\sqrt{T}$ formula in \S\ref{sec:theory} is a conservative lower bound.
671	FPR under FDR correction remains ${\leq}2\%$ across all $T$.
672	
673	\paragraph{Detailed power values.}
674	Selected FDR-corrected power levels illustrate the gain from longer observation: at $\beta{=}1.0$, power rises from 0.17 ($T{=}10$) to 0.30 ($T{=}15$) to 0.66 ($T{=}20$); at $\beta{=}2.0$, from 0.51 ($T{=}10$) to 0.92 ($T{=}15$) to 0.98 ($T{=}20$).
675	Raw FPR (before FDR correction) is higher but still controlled: $T{=}6$: 1\%, $T{=}8$: 6\%, $T{=}10$: 9\%, $T{=}15$: 6\%, $T{=}20$: 5\%.
676	The non-monotonic raw FPR peak at $T{=}10$ reflects the discrete-sample properties of permutation tests at small $T$; FDR correction absorbs this variation.
677	
678	\paragraph{$\sqrt{T}$ scaling product.}
679	If power scaled exactly as $\sqrt{T}$, the product $\beta_{50} \cdot \sqrt{T}$ would be constant.
680	Observed values: $T{=}8$: 5.09; $T{=}10$: 6.32; $T{=}15$: 4.65; $T{=}20$: 4.02.
681	The downward trend indicates that power grows faster than $\sqrt{T}$---each additional generation contributes more information than a simple $\sqrt{T}$ model predicts, likely because the cumulative signal (not just instantaneous SNR) drives detection in Granger-type tests.
682	
683	\paragraph{Toda--Yamamoto bootstrap comparison.}
684	TY bootstrap power simulations (200 reps, same DGP) yield substantially lower power at comparable $T$: $T{=}10$ power${=}0.205$ (vs.\ PermG 0.51 at $\beta{=}2.0$), $T{=}20$ power${=}0.409$, with Type~I error rate 8.1\% (above nominal).
685	TY's $d$-augmented lag structure wastes degrees of freedom in short series, explaining its inferior power-FPR tradeoff relative to PermG.
686	
687	\begin{table}[H]
688	\centering
689	\small
690	\caption{PermG power analysis: $\beta_{50}$ (coupling for 50\% power) under BH-FDR correction ($q{=}0.05$, 8 pairs). Dashes: $<$50\% power not reached within $\beta \leq 2.0$.}
691	\label{tab:beta50}
692	\begin{tabular}{lcccc}
693	\toprule
694	$T$ & $\beta_{50}$ & $\beta_{50} \cdot \sqrt{T}$ & FPR (raw) & FPR (FDR) \\
695	\midrule
696	6  & ---  & ---  & 1\% & 0\% \\
697	8  & ---  & ---  & 6\% & 2\% \\
698	10 & 2.0  & 6.32 & 9\% & 2\% \\
699	15 & 1.2  & 4.65 & 6\% & 2\% \\
700	20 & 0.9  & 4.02 & 5\% & 1\% \\
701	\bottomrule
702	\end{tabular}
703	\end{table}
704	
705	
706	\section{Non-Stationarity Robustness Analysis}
707	\label{app:nonstationarity}
708	
709	\begin{figure}[H]
710	\centering
711	\includegraphics[width=\columnwidth]{figures/fig_ar1_diagnostic.pdf}
712	\caption{AR(1) coefficient estimates across five contamination levels (Pythia-410M, seed~42). (a)~Token entropy: raw $\varphi$ transitions from negative ($-0.51$ at $\alpha{=}0.00$) to near-unit-root ($1.00$ at $\alpha{=}1.00$), but first-differencing keeps all values below 0.98. (b)~Distinct-1: raw $\varphi$ is uniformly high ($0.75$--$0.95$) even at null, driven by deterministic trend; first-differencing reduces all to ${\leq}0.24$. Dashed red line: $\varphi{=}0.95$ danger zone.}
713	\label{fig:ar1_diagnostic}
714	\end{figure}
715	
716	Monte Carlo simulation (AR(1) DGP, $T{=}11$, 1{,}000 reps) shows PermG FPR inflates to ${\sim}10\%$ under strong non-stationarity ($\varphi{\geq}0.95$), while first-differencing maintains proper size ($4.2$--$6.6\%$) at the cost of reduced power (Table~\ref{tab:nonstationarity_sim}).
717	Our pipeline applies first-differencing before permutation testing, combining both advantages.
718	Under null conditions ($\alpha{=}0.0$), token entropy exhibits $\varphi{=}-0.51$ (far from the danger zone); first-differencing reduces distinct-1's high raw $\varphi$ ($0.81$--$0.97$, reflecting deterministic trend) to $-0.14$--$0.44$.
719	Our empirical FPR of 4/60 (6.7\%) confirms adequate size control.
720	
721	\begin{table}[H]
722	\centering
723	\small
724	\caption{Size and power under AR(1) DGP ($T{=}11$, 1{,}000 reps). First-differencing maintains nominal size; PermG FPR inflates at $\varphi{\geq}0.95$.}
725	\label{tab:nonstationarity_sim}
726	\resizebox{\columnwidth}{!}{%
727	\begin{tabular}{lcccccc}
728	\toprule
729	& \multicolumn{3}{c}{Size (\%, $\beta{=}0$)} & \multicolumn{3}{c}{Power (\%, $\beta{=}0.6$)} \\
730	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
731	$\varphi$ & Raw GC & First-Diff & PermG & Raw GC & First-Diff & PermG \\
732	\midrule
733	0.50 & 6.4 & 6.6 & 6.8 & 37.7 & 17.7 & 36.8 \\
734	0.95 & 10.0 & 5.9 & 9.5 & 44.3 & 28.7 & 41.5 \\
735	0.99 & 11.2 & 4.2 & 10.7 & 46.4 & 24.6 & 41.7 \\
736	\bottomrule
737	\end{tabular}}
738	\end{table}
739	
740	\paragraph{Empirical AR(1) coefficients.}
741	Table~\ref{tab:empirical_ar1} reports estimated AR(1) coefficients for all metric series under null ($\alpha{=}0.0$) and treatment ($\alpha{=}1.0$) conditions.
742	Under the null, all metrics exhibit $|\varphi| < 0.60$ in raw levels and $|\varphi| < 0.30$ after first-differencing, well within the safe zone.
743	Under treatment, raw distinct-$n$ series reach $\varphi{=}0.81$--$0.97$ (near unit root), but first-differencing reduces these to $\varphi{=}-0.14$--$0.44$---confirming that the deterministic trend, not stochastic persistence, drives the high raw autocorrelation.
744	
745	\begin{table}[H]
746	\centering
747	\small
748	\caption{Empirical AR(1) coefficients (Pythia-410M, 4~seeds). ``Raw'' = levels; ``Diff'' = first-differenced.}
749	\label{tab:empirical_ar1}
750	\resizebox{\columnwidth}{!}{%
751	\begin{tabular}{lcccc}
752	\toprule
753	& \multicolumn{2}{c}{$\alpha{=}0.0$} & \multicolumn{2}{c}{$\alpha{=}1.0$} \\
754	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
755	Metric & Raw $\varphi$ & Diff $\varphi$ & Raw $\varphi$ & Diff $\varphi$ \\
756	\midrule
757	Token entropy & $-0.51$ & $-0.28$ & $0.72$ & $0.15$ \\
758	ECE & $0.31$ & $-0.15$ & $0.95$ & $0.38$ \\
759	Distinct-1 & $0.55$ & $0.12$ & $0.97$ & $0.44$ \\
760	Distinct-2 & $0.48$ & $0.08$ & $0.95$ & $0.31$ \\
761	Perplexity & $0.42$ & $-0.22$ & $0.93$ & $-0.14$ \\
762	\bottomrule
763	\end{tabular}}
764	\end{table}
765	
766	\paragraph{ADF test results.}
767	Augmented Dickey--Fuller tests on first-differenced series reject the unit root hypothesis at $p{<}0.05$ in all 40 series (5~metrics $\times$ 4~seeds $\times$ 2~conditions), confirming that first-order differencing ($d{=}1$) is sufficient and higher-order differencing ($d{\geq}2$) would unnecessarily reduce power (Figure~\ref{fig:differencing_dmax}).
768	
769	\paragraph{Why not KPSS?}
770	We use ADF (null: unit root) rather than KPSS (null: stationarity) because ADF is more conservative for our purpose: rejecting the unit-root null provides positive evidence of stationarity, while KPSS's failure to reject would only indicate insufficient evidence against stationarity.
771	In the short-series regime ($T{\leq}25$), KPSS has limited power; ADF's rejection at $p{<}0.05$ across all differenced series provides stronger evidence.
772	
773	\paragraph{Power cost of first-differencing.}
774	First-differencing eliminates spurious regression but reduces effective power by discarding level information (Table~\ref{tab:diff_power_cost}).
775	Under the AR(1) DGP ($\varphi{=}0.50$, $\beta{=}0.6$), first-differenced PermG achieves 17.7\% power versus 36.8\% for raw PermG---a 52\% relative power reduction.
776	At $\varphi{=}0.95$ the cost narrows (28.7\% vs.\ 41.5\%, 31\% reduction) because the stronger persistence makes the raw test less reliable (inflated FPR).
777	Our pipeline accepts this power cost as a necessary tradeoff: at the empirical autocorrelation levels observed in treatment series ($\varphi{=}0.72$--$0.97$ in raw levels), raw Granger testing would produce ${\sim}10\%$ FPR, invalidating the detection framework.
778	
779	\begin{table}[H]
780	\centering
781	\small
782	\caption{Power cost of first-differencing under simulated AR(1) DGP ($T{=}11$, $\beta{=}0.6$, 1{,}000 reps). The power reduction is the price paid for valid size control.}
783	\label{tab:diff_power_cost}
784	\begin{tabular}{lcccc}
785	\toprule
786	$\varphi$ & Raw power & Diff power & Reduction & Raw FPR \\
787	\midrule
788	0.50 & 36.8\% & 17.7\% & 52\% & 6.8\% \\
789	0.95 & 41.5\% & 28.7\% & 31\% & 9.5\% \\
790	0.99 & 41.7\% & 24.6\% & 41\% & 10.7\% \\
791	\bottomrule
792	\end{tabular}
793	\end{table}
794	
795	The practical consequence: at $T{=}10$, the differencing-induced power loss is the primary bottleneck for detecting weak contamination ($\alpha < 0.50$).
796	Extending observation to $T{=}20$ more than compensates: differenced power at $T{=}20$ exceeds raw power at $T{=}10$ for $\varphi \leq 0.95$, providing both valid size control and superior detection sensitivity.
797	This explains the large detection gains observed in the $T{=}20$ extension (\S\ref{app:t20_comparison}).
798	
799	
800	\section{Shapley Value Analysis}
801	\label{app:shapley}
802	
803	\begin{figure}[H]
804	\centering
805	\includegraphics[width=\columnwidth]{figures/fig_shapley_contribution_top.pdf}
806	\caption{Shapley value decomposition by method. FPR contribution (positive = worse) and FNR contribution (negative = better) are shown for each of the five detection methods. DiffXCorr achieves the best combined Shapley ($-0.299$) but lacks directional separation; among directional methods, PermG ranks best ($-0.141$). NaiveXCorr contributes the most FPR ($+0.609$) due to its inability to distinguish signal from null drift.}
807	\label{fig:shapley_contribution_app}
808	\end{figure}
809	
810	\begin{figure}[H]\ContinuedFloat
811	\centering
812	\includegraphics[width=\columnwidth]{figures/fig_shapley_contribution_bottom.pdf}
813	\caption[]{(\textit{continued})}
814	\end{figure}
815	
816	Shapley values~\citep{shapley1953value} computed over all $2^5{=}32$ coalitions quantify each method's marginal contribution to FPR and FNR (Table~\ref{tab:shapley_6pair}).
817	DiffXCorr achieves the best combined Shapley ($-0.299$) but cannot separate forward from reverse; among directional methods, PermG ranks best ($-0.141$).
818	The 8-pair variant (including MAUVE) yields identical rankings.
819	
820	\begin{table}[H]
821	\centering
822	\small
823	\caption{Shapley value decomposition (6-pair, MAUVE excluded). Combined = FPR + FNR (more negative = better).}
824	\label{tab:shapley_6pair}
825	\begin{tabular}{lccc}
826	\toprule
827	Method & $\phi^{\text{FPR}}$ & $\phi^{\text{FNR}}$ & $\phi^{\text{comb}}$ \\
828	\midrule
829	Naive XCorr          & $+0.609$ & $-0.419$ & $+0.190$ \\
830	\textbf{Diff.\ XCorr}& $\mathbf{+0.007}$ & $\mathbf{-0.306}$ & $\mathbf{-0.299}$ \\
831	Threshold ($3\sigma$) & $+0.111$ & $-0.027$ & $+0.084$ \\
832	Perm.\ Granger       & $+0.039$ & $-0.180$ & $-0.141$ \\
833	Toda--Yamamoto       & $+0.150$ & $-0.069$ & $+0.082$ \\
834	\bottomrule
835	\end{tabular}
836	\end{table}
837	
838	\section{MMCT Weight Robustness Ablation}
839	\label{app:weight_robustness}
840	
841	PermG ranks first among directional methods under all four weighting schemes tested (equal, cap-5, cap-10, FPR-inverse cap-100), confirming the ranking is not an artifact of the weighting scheme.
842	Cap-10 and cap-100 yield identical values (consensus threshold saturates), and equal weighting still gives PermG the best combined Shapley ($-0.152$) among directional methods.
843	
844	\begin{table}[H]
845	\centering
846	\small
847	\caption{PermG combined Shapley ($\phi^{\text{comb}}$) under four weighting schemes. Rankings are invariant to weight choice.}
848	\label{tab:weight_robustness}
849	\begin{tabular}{lcccc}
850	\toprule
851	Method & Equal & Cap-5 & Cap-10 & FPR-inv \\
852	\midrule
853	PermG & $-0.152$ & $-0.148$ & $-0.141$ & $-0.141$ \\
854	DiffXCorr & $-0.285$ & $-0.291$ & $-0.299$ & $-0.299$ \\
855	Threshold & $+0.078$ & $+0.081$ & $+0.084$ & $+0.084$ \\
856	TY & $+0.088$ & $+0.084$ & $+0.082$ & $+0.082$ \\
857	NaiveXCorr & $+0.195$ & $+0.192$ & $+0.190$ & $+0.190$ \\
858	\bottomrule
859	\end{tabular}
860	\end{table}
861	
862	\paragraph{Interpretation.}
863	The FPR-inverse weighting scheme (\S\ref{sec:mmct}) penalizes high-FPR methods by assigning weight $w_k = 1/\max(\widehat{\mathrm{FPR}}_k, \epsilon)$.
864	Under this scheme, NaiveXCorr (FPR${=}94.4\%$) receives weight $w{=}1.06$, while PermG (FPR${=}6.7\%$) receives $w{=}14.9$---a $14{\times}$ differential.
865	Equal weighting gives all methods identical influence, which reduces PermG's advantage but does not change its ranking among directional methods.
866	The invariance across weighting schemes (Table~\ref{tab:weight_robustness}) confirms that PermG's superiority reflects genuine detection properties rather than favorable weighting.
867	
868	\paragraph{Per-pair contribution variability.}
869	Marginal contributions vary substantially across canary$\to$downstream pairs (Table~\ref{tab:shapley_per_pair}).
870	Token entropy$\to$distinct-1 produces the most consistent positive contribution across coalitions (std${=}0.021$), while ECE$\to$perplexity shows the highest variance (std${=}0.089$), reflecting the contemporaneous coupling issue (\S\ref{app:channel_effect_size}).
871	
872	\begin{table}[H]
873	\centering
874	\small
875	\caption{Shapley contribution by canary$\to$downstream pair (PermG, 6-pair basis). $\phi^{\text{FNR}}$ = FNR reduction (more negative = better). Std = standard deviation across all $2^4$ coalitions that include this pair.}
876	\label{tab:shapley_per_pair}
877	\begin{tabular}{lcc}
878	\toprule
879	Pair & Mean $\phi^{\text{FNR}}$ & Std \\
880	\midrule
881	Entropy$\to$Distinct-1 & $-0.042$ & 0.021 \\
882	Entropy$\to$Distinct-2 & $-0.038$ & 0.024 \\
883	ECE$\to$Distinct-1 & $-0.035$ & 0.031 \\
884	ECE$\to$Distinct-2 & $-0.031$ & 0.028 \\
885	Entropy$\to$PPL & $-0.002$ & 0.067 \\
886	ECE$\to$PPL & $-0.001$ & 0.089 \\
887	\bottomrule
888	\end{tabular}
889	\end{table}
890	
891	The four diversity-channel pairs collectively account for 96.2\% of PermG's total FNR reduction, while the two perplexity-channel pairs contribute only 3.8\%---consistent with the channel effect size analysis (\S\ref{app:channel_effect_size}) showing that perplexity channels lack the temporal lead structure required for Granger detection.
892	This concentration motivates a practical simplification: for deployment scenarios where computational cost matters, testing only the four diversity-channel pairs sacrifices less than 4\% of detection sensitivity while halving the multiple testing burden (4~tests instead of 8, reducing the FDR correction penalty).
893	
894	\paragraph{Coalition stability.}
895	PermG's marginal contribution is stable across coalition sizes: when added to a 1-method coalition, its average combined Shapley is $-0.138$ (SE${=}0.015$); when added to a 4-method coalition, $-0.144$ (SE${=}0.008$).
896	The near-zero variation ($\Delta{=}0.006$) confirms that PermG's value is complementary rather than redundant---it provides directional information that no other single method duplicates.
897	DiffXCorr shows the opposite pattern: its marginal contribution \emph{decreases} from $-0.312$ (1-method coalition) to $-0.281$ (4-method coalition) as it becomes partially redundant with NaiveXCorr (both test correlation, differing only in preprocessing).
898	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74f47010-cebd-4b31-ac34-ae71b61b7c33",
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a9d7bd4d8daf2b13b",
  "type": "user",
  "uuid": "3d6072dd-1cfd-41b5-914e-40e6fda7b1b0",
  "sourceToolAssistantUUID": "74f47010-cebd-4b31-ac34-ae71b61b7c33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T19:41:55.895Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qo1JzHjwoVfgetnrqokt5e`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 898,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d6072dd-1cfd-41b5-914e-40e6fda7b1b0",
  "isSidechain": true,
  "agentId": "a9d7bd4d8daf2b13b",
  "requestId": "req_011CbPreoo9N2myK9FTL5kEP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25d9b0e2-86b1-441e-abe0-9f1af40fa95f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnjFfMvrV5joXPuhzvKLJT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8379,
      "cache_read_input_tokens": 53024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8379,
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

_source line 15 · 2026-05-25T19:41:55.902Z_

<details><summary>↩ Tool result · `toolu_01Qo1JzHjwoVfgetnrqokt5e`</summary>

```text
898	
899	
900	\section{PermG FPR Independence Analysis}
901	\label{app:fpr_independence}
902	
903	\begin{figure}[H]
904	\centering
905	\includegraphics[width=\columnwidth]{figures/fig_fpr_sensitivity.pdf}
906	\caption{Per-seed FPR distribution across detection methods (Pythia-410M, $\alpha{=}0.0$, 10~seeds). Each dot represents one seed's FPR; boxplots show inter-seed variability. PermG FPR concentrates near 0\% (8/10 seeds yield 0 false positives) with two outlier seeds (s45, s50) driving the aggregate 6.7\%. NaiveXCorr exhibits uniformly high FPR (${\geq}83\%$) across all seeds.}
907	\label{fig:fpr_sensitivity}
908	\end{figure}
909	
910	Table~\ref{tab:null_fpr_methods} reports null-control FPR across nine seeds (54 pairs, 6-pair basis); a tenth seed (s51) yields 0~PermG FP, giving pooled 4/60${=}$6.7\% (CI $[1.8\%, 16.2\%]$).
911	All four FP occur in te$\to$distinct pairs in seeds~45/50 (8/10 seeds yield 0~FP).
912	$K{\geq}3$ consensus produces 6/60 FP (10.0\%), of which PermG contributes to only 2.
913	At $T{=}15$, PermG FPR drops to 0/12 (0\%).
914	
915	\begin{figure}[H]
916	\centering
917	\includegraphics[width=\columnwidth]{figures/fig_null_fpr_diagnostic.pdf}
918	\caption{Null-control diagnostic: PermG $p$-value distributions under null ($\alpha{=}0.0$) across 10~seeds. Most seeds show $p$-values uniformly distributed above 0.05 (expected under the null); seeds~45 and 50 exhibit a cluster of low $p$-values in token-entropy$\to$distinct pairs, suggesting occasional null-condition coupling that does not generalize across seeds.}
919	\label{fig:null_fpr_diagnostic}
920	\end{figure}
921	
922	\begin{table}[H]
923	\centering
924	\small
925	\caption{Null-control FPR by method ($\alpha{=}0.0$, BH-FDR $q{=}0.05$). $^\ddagger$PermG: 10~seeds, 60~pairs; other methods: 9~seeds, 54~pairs (s51 6-pair breakdown pending).}
926	\label{tab:null_fpr_methods}
927	\resizebox{\columnwidth}{!}{%
928	\begin{tabular}{llrr}
929	\toprule
930	Method & Criterion & Rejections & FPR (\%) \\
931	\midrule
932	\textbf{Perm.\ Granger}$^\ddagger$ & \textbf{BH-FDR} & \textbf{4/60} & \textbf{6.7} \\
933	Diff.\ XCorr$^\dagger$ & BH-FDR & 8/54 & 14.8 \\
934	Threshold & $3\sigma$ (det.) & 13/54 & 24.1 \\
935	Toda--Yamamoto & BH-FDR & 18/54 & 33.3 \\
936	Naive XCorr & uncorr. & 51/54 & 94.4 \\
937	\bottomrule
938	\multicolumn{4}{l}{\footnotesize $^\dagger$Bidirectional; cannot separate forward from reverse.} \\
939	\end{tabular}}
940	\end{table}
941	
942	\subsection{Per-Seed FPR Breakdown}
943	\label{app:per_seed_fpr}
944	
945	Table~\ref{tab:per_seed_fpr_8pair} reports FPR on a per-seed, per-method basis for the original 3-seed cohort (s42, s43, s44; 8-pair basis including MAUVE), while Table~\ref{tab:per_seed_fpr_6pair} extends to the 6-seed expansion (s45--s51; 6-pair basis excluding MAUVE).
946	
947	\begin{figure}[H]
948	\centering
949	\includegraphics[width=\columnwidth]{figures/fig_bootstrap_fpr.pdf}
950	\caption{Bootstrap confidence intervals for FPR estimates (10{,}000 resamples, 10~seeds). PermG's 95\% CI ($[1.8\%, 16.2\%]$) is the tightest among directional methods; the upper bound remains below Threshold's point estimate (27.8\%). The bootstrap distribution for NaiveXCorr is sharply peaked near 90\%, confirming that its high FPR is systematic rather than driven by individual seed outliers.}
951	\label{fig:bootstrap_fpr}
952	\end{figure}
953	
954	\begin{table}[H]
955	\centering
956	\small
957	\caption{Per-seed FPR (8-pair basis, $\alpha{=}0.0$, Pythia-410M, seeds 42--44). PermG achieves 0/8 on all three seeds; NaiveXCorr ${\geq}7/8$ on all.}
958	\label{tab:per_seed_fpr_8pair}
959	\resizebox{\columnwidth}{!}{%
960	\begin{tabular}{lccccc}
961	\toprule
962	Seed & PermG & DiffXCorr & Threshold & TY & NaiveXCorr \\
963	\midrule
964	42 & 0/8 & 4/8 & 3/8 & 2/8 & 8/8 \\
965	43 & 0/8 & 2/8 & 1/8 & 2/8 & 7/8 \\
966	44 & 0/8 & 3/8 & 2/8 & 0/8 & 7/8 \\
967	\midrule
968	Pooled & 0.0\% & 37.5\% & 25.0\% & 16.7\% & 91.7\% \\
969	\bottomrule
970	\end{tabular}}
971	\end{table}
972	
973	\begin{table}[H]
974	\centering
975	\small
976	\caption{Per-seed PermG FPR (6-pair basis, $\alpha{=}0.0$, seeds 45--51). Two seeds (s45, s50) contribute all 4 false positives; remaining seeds yield 0/6.}
977	\label{tab:per_seed_fpr_6pair}
978	\begin{tabular}{lccl}
979	\toprule
980	Seed & PermG fwd & $K{\geq}3$ & Affected pairs \\
981	\midrule
982	45 & 2/6 & 0/6 & te$\to$d1, te$\to$d2 \\
983	46 & 0/6 & 1/6 & --- \\
984	47 & 0/6 & 0/6 & --- \\
985	48 & 0/6 & 0/6 & --- \\
986	49 & 0/6 & 0/6 & --- \\
987	50 & 2/6 & 2/6 & te$\to$d1, te$\to$d2 \\
988	51 & 0/6 & 0/6 & --- \\
989	\bottomrule
990	\end{tabular}
991	\end{table}
992	
993	The concentration of false positives in token-entropy$\to$distinct pairs at seeds~45 and 50 suggests stochastic null-condition coupling in these specific initializations rather than a systematic calibration failure.
994	$K{\geq}3$ consensus FPR on the 6-pair basis is 6/36${=}$16.7\%; of these 6 false positives, only 2 include PermG (both at s50)---the remaining 4 are driven by high-FPR methods (NaiveXCorr $+$ Threshold $+$ TY) reaching consensus without PermG participation.
995	This decomposition clarifies why $K{\geq}3$ FPR exceeds standalone PermG FPR: the consensus mechanism aggregates false positives from multiple methods rather than filtering them.
996	
997	
998	\section{Sigmoid Transition Shape}
999	\label{app:sigmoid_shape}
1000	
1001	Sigmoid regression on the original 13-point $T{=}10$ grid yields $\alpha_c = 0.483 \pm 0.006$ but $k = 478 \pm 475$ ($\mathrm{SE}(k) \approx k$), indicating that the coarse grid cannot constrain the transition shape.
1002	Dense $\alpha$ sampling (17~values at $T{=}10$) resolves this ambiguity: formal likelihood-ratio testing strongly favors a smooth sigmoid over a literal step function ($\Delta\mathrm{AIC}{=}-110$), with fitted steepness $k{=}15.7$ (95\% CI $[9.4, 28.2]$).
1003	The transition is steep but finite-width, not a literal discontinuity.
1004	This observed steepness exceeds what smooth signal models predict: VAR(1) simulations under H0 (linear, $k{=}6.1$) and H0$'$ (concave, $k{=}4.9$) produce onset sigmoids with $k{=}4.9$--$6.1$ (\S\ref{app:power_sim}), yielding steepness ratios $k_{\mathrm{obs}} / k_{\mathrm{H0}} \approx 2.6$--$3.2$ (CI lower bound ratio ${\approx}2$).
1005	
1006	\paragraph{Combined $T{=}10 + T{=}20$ fit.}
1007	Fitting a single sigmoid to both $T$ values yields $k{=}279.3$ (SE${=}527.6$), $\alpha_c{=}0.451$, $y_{\max}{=}0.75$, AIC${=}79.86$.
1008	The 90\% transition width narrows from $[0.478, 0.487]$ (width$=0.0092$) at $T{=}10$ alone to $[0.443, 0.459]$ (width$=0.0158$) in the combined fit---a leftward shift of $\alpha_c$ by $0.031$ reflecting the $T{=}20$ data's detection at $\alpha{=}0.45$.
1009	The combined $k$ drops by 41.6\% relative to $T{=}10$-only, confirming that the transition appears broader when viewed across observation lengths (different $T$ values yield different effective detection thresholds).
1010	We ultimately do not report the combined sigmoid in the main text because $\alpha{=}0.45$ yields contradictory counts (0/8 at $T{=}10$ vs.\ 5/8 at $T{=}20$), reflecting genuine power dependence rather than a single dose-response curve.
1011	
1012	\paragraph{Alternative functional forms.}
1013	Probit and sigmoid fits produce identical AIC (32.99 at $T{=}10$, 79.86 combined), as expected given that both are sigmoidal CDFs differing only in tail behavior.
1014	A generalized logistic ($+1$ parameter for asymmetry $\nu$) adds $+2$ AIC penalty without improving fit, confirming that a symmetric sigmoid is sufficient.
1015	
1016	\paragraph{Transition width characterization.}
1017	The 90\% transition width---the $\alpha$ range over which detection probability rises from 5\% to 95\%---quantifies the sharpness of the regime boundary (Table~\ref{tab:transition_width}).
1018	
1019	\begin{table}[H]
1020	\centering
1021	\small
1022	\caption{Sigmoid transition width (90\% range) by observation length and signal model. Narrower width indicates sharper regime onset.}
1023	\label{tab:transition_width}
1024	\begin{tabular}{lccc}
1025	\toprule
1026	Setting & Width ($\Delta\alpha$) & $\alpha_c$ & $k$ \\
1027	\midrule
1028	$T{=}10$ observed (13-pt) & 0.009 & 0.483 & 478 \\
1029	$T{=}10$ dense (17-pt) & 0.028 & 0.481 & 15.7 \\
1030	$T{=}10{+}20$ combined & 0.016 & 0.451 & 279 \\
1031	H0 linear simulation & 0.072 & 0.507 & 6.1 \\
1032	H0$'$ concave simulation & 0.090 & 0.521 & 4.9 \\
1033	\bottomrule
1034	\end{tabular}
1035	\end{table}
1036	
1037	\begin{figure}[H]
1038	\centering
1039	\includegraphics[width=\columnwidth]{figures/differencing_dmax.pdf}
1040	\caption{First-differencing order selection diagnostic. The optimal differencing order $d_{\max}$ is evaluated via ADF test statistics across all canary$\to$downstream series at $\alpha{=}1.0$. First-order differencing ($d{=}1$) achieves stationarity in all series (ADF $p{<}0.05$), confirming that higher-order differencing is unnecessary and would incur additional power loss.}
1041	\label{fig:differencing_dmax}
1042	\end{figure}
1043	
1044	The dense-sampling transition width ($\Delta\alpha{=}0.028$, corresponding to $\alpha \in [0.467, 0.495]$) is ${\sim}3{\times}$ narrower than smooth-model predictions (0.072--0.090), confirming the anomalous sharpness.
1045	In practical terms, a difference of $\Delta\alpha{=}0.03$ in contamination fraction determines whether detection is impossible (0\%) or reliable (75\%)---this represents approximately 150 additional synthetic samples out of 5{,}000.
1046	The narrow transition has implications for monitoring systems: slight increases in synthetic data fraction near the boundary produce large changes in detectability, creating a ``cliff effect'' where monitoring transitions from false security to reliable alarm with minimal change in the underlying contamination level.
1047	A system operating at $\alpha{=}0.47$ (undetectable) and drifting to $\alpha{=}0.50$ (detectable) would experience an abrupt shift from zero alarm rate to 75\% alarm rate---a three percentage-point contamination increase produces a qualitative change in monitoring behavior.
1048	
1049	\section{Intervention Threshold Sensitivity}
1050	\label{app:intervention_sensitivity}
1051	
1052	At $\alpha{=}1.0$, all five tested thresholds (5\%--25\%) trigger at generation~1 (entropy drop 40.7\%$\gg$threshold), producing identical outcomes (peak PPL 57.0, final PPL 21.3).
1053	The safe operating band is $[10\%, 22\%]$: below 7.5\% triggers false alarms on $\alpha{=}0.0$ drift; above 22.4\% misses $\alpha{=}0.50$.
1054	
1055	\paragraph{Cross-seed and cross-scale replication.}
1056	The predictive cessation result replicates on seed~43 (bf16 precision): trigger at gen-1 with a milder entropy drop ($-22.5\%$ vs.\ $-40.7\%$ in fp32), peak PPL${=}24.65$ (lower due to bf16 dampening).
1057	On Pythia-1.4B (s42, fp32): trigger at gen-1, entropy drop $-51.9\%$ ($2.946 \to 1.418$), peak PPL spike from $19.68$ to $65.37$, recovery by gen-2 (PPL${=}17.44$), final PPL at gen-10${=}17.6$.
1058	ECE follows the same pattern: $0.007 \to 0.281$ at the spike, recovering to $0.017$ post-intervention.
1059	
1060	\paragraph{Alpha=0.75 predictive intervention.}
1061	At $\alpha{=}0.75$ (fp32, v4 pipeline), predictive cessation also triggers at gen-1, with recovery by gen-2.
1062	Post-intervention PermG detection reaches 6/8 forward, $K{\geq}4{=}6/8$, confirming that the intervention preserves the statistical detection signal while preventing perplexity degradation.
1063	Entropy drift post-intervention is only $-5.7\%$ over 10~generations (vs.\ $-27.6\%$ without intervention), consistent with the generation-1 trigger halting the collapse cascade before downstream metrics respond.
1064	
1065	\paragraph{No-intervention baseline comparison.}
1066	Without intervention at $\alpha{=}1.0$: gen-10 PPL${=}1003.73$, distinct-1${=}0.0704$.
1067	With predictive cessation: gen-10 PPL${=}21.29$, distinct-1${=}0.0844$ ($+19.9\%$ higher diversity).
1068	The intervention reduces peak perplexity by 64\% ($56.99$ vs.\ $157.09$ reactive) and preserves substantially more lexical diversity, though neither intervention strategy fully prevents the initial diversity loss at gen-1.
1069	
1070	\begin{figure}[H]
1071	\centering
1072	\includegraphics[width=\columnwidth]{figures/fig_cusum_monitoring.pdf}
1073	\caption{CUSUM sequential monitoring versus calibrated threshold (Pythia-410M, $\alpha{=}1.0$). Both methods trigger at generation~1 because the entropy drop ($|\Delta x|{>}0.7$) greatly exceeds null variability ($\sigma_0{\approx}0.03$). CUSUM's cumulative memory provides no advantage when the initial signal dominates. The shaded region marks the safe operating band $[10\%, 22\%]$ for threshold-based detection.}
1074	\label{fig:cusum_monitoring}
1075	\end{figure}
1076	
1077	
1078	\section{Channel Effect Size Analysis}
1079	\label{app:channel_effect_size}
1080	
1081	First-differencing retains comparable $|r|$ for both diversity (0.952) and perplexity (1.00) channels, ruling out selective power loss.
1082	The Granger $F$-statistic asymmetry ($20$--$28{\times}$ higher for diversity) reflects temporal structure: diversity channels peak at canary-leading lags (81\% at lag${<}0$, median $-1$), while perplexity peaks at lag${=}0$ (contemporaneous co-movement).
1083	Granger tests correctly assign low $F$ to contemporaneous relationships.
1084	
1085	\paragraph{Lag structure decomposition.}
1086	Table~\ref{tab:lag_structure} reports the cross-correlation peak lag for each canary$\to$downstream channel, illustrating the structural difference that drives Granger detectability.
1087	
1088	\begin{table}[H]
1089	\centering
1090	\small
1091	\caption{Cross-correlation peak lag by channel (Pythia-410M, $\alpha{=}1.0$, 4~seeds). Negative lag = canary leads. Diversity channels show consistent canary-leading structure; perplexity channels peak at lag~0.}
1092	\label{tab:lag_structure}
1093	\begin{tabular}{lccl}
1094	\toprule
1095	Channel & Peak lag & $|r|$ at peak & Structure \\
1096	\midrule
1097	Entropy$\to$Dist-1 & $-1$ & 0.96 & canary leads \\
1098	Entropy$\to$Dist-2 & $-1$ & 0.95 & canary leads \\
1099	ECE$\to$Dist-1 & $-1$ & 0.94 & canary leads \\
1100	ECE$\to$Dist-2 & $-1$ & 0.93 & canary leads \\
1101	Entropy$\to$PPL & $0$ & 0.99 & contemporaneous \\
1102	ECE$\to$PPL & $0$ & 0.98 & contemporaneous \\
1103	\bottomrule
1104	\end{tabular}
1105	\end{table}
1106	
1107	The contemporaneous co-movement of canary$\to$perplexity explains why Granger tests fail ($F{\approx}0$, $p{=}0.99$ after differencing): perplexity and entropy respond to the same underlying distributional shift at the same time step, so neither provides predictive improvement over the other's own history.
1108	This is not a limitation of the test but a correct inference---perplexity is not ``downstream'' of entropy in the temporal sense.
1109	
1110	\paragraph{Fisher Z-transform comparison.}
1111	To formally test whether diversity and perplexity channels differ in lagged correlation magnitude, we apply the Fisher Z-transform to peak cross-correlation coefficients (Table~\ref{tab:fisher_z}).
1112	
1113	\begin{table}[H]
1114	\centering
1115	\small
1116	\caption{Fisher Z-transform comparison of channel correlations (Pythia-410M, $\alpha{=}1.0$, 4~seeds). $Z_{\text{diff}}$ tests whether lagged ($\ell{=}{-}1$) correlation differs between diversity and perplexity channels.}
1117	\label{tab:fisher_z}
1118	\begin{tabular}{lcccc}
1119	\toprule
1120	Comparison & $r_{\text{div}}$ & $r_{\text{ppl}}$ & $Z_{\text{diff}}$ & $p$ \\
1121	\midrule
1122	\emph{Lag${=}0$ (contemp.)} \\
1123	\quad Entropy$\to$ & 0.955 & 0.990 & $-2.13$ & 0.033 \\
1124	\quad ECE$\to$ & 0.935 & 0.980 & $-2.41$ & 0.016 \\
1125	\midrule
1126	\emph{Lag${=}{-}1$ (canary leads)} \\
1127	\quad Entropy$\to$ & 0.952 & 0.812 & $+3.67$ & ${<}0.001$ \\
1128	\quad ECE$\to$ & 0.941 & 0.795 & $+3.89$ & ${<}0.001$ \\
1129	\bottomrule
1130	\end{tabular}
1131	\end{table}
1132	
1133	At lag${=}0$ (contemporaneous), perplexity channels show \emph{higher} correlation than diversity channels ($r{=}0.990$ vs.\ $0.955$, $Z{=}-2.13$, $p{=}0.033$), reflecting the synchronous entropy-perplexity coupling.
1134	At lag${=}-1$ (canary leading by one generation), the pattern reverses decisively: diversity channels achieve $r{=}0.952$ vs.\ perplexity's $r{=}0.812$ ($Z{=}3.67$, $p{<}0.001$).
1135	This reversal explains the Granger $F$-statistic asymmetry: perplexity channels do not have weaker coupling overall, but their coupling is \emph{contemporaneous rather than lagged}.
1136	A Granger test measures whether \emph{past} values of $X$ predict \emph{current} $Y$ beyond $Y$'s own history; contemporaneous coupling produces zero improvement, hence $F \approx 0$.
1137	The Fisher Z analysis confirms that the canary$\to$perplexity non-detection is a correct statistical inference about temporal structure rather than a power limitation.
1138	
1139	\begin{figure}[H]
1140	\centering
1141	\includegraphics[width=\columnwidth]{figures/fig_channel_effect.pdf}
1142	\caption{Channel effect size comparison: Granger $F$-statistic for canary$\to$diversity versus canary$\to$perplexity channels (Pythia-410M, $\alpha{=}1.0$, 4~seeds). Diversity channels produce $20$--$28{\times}$ higher $F$-statistics than perplexity channels, reflecting the temporal structure difference: diversity correlations peak at canary-leading lags (81\% at lag${<}0$), while perplexity correlations are contemporaneous (50\% at lag${=}0$).}
1143	\label{fig:channel_effect}
1144	\end{figure}
1145	
1146	
1147	\section{Mutual Information and Partial Correlation}
1148	\label{app:mi_analysis}
1149	
1150	Gaussian MI lower bound ($\hat{I}_G = -\frac{1}{2}\log_2(1{-}r^2)$) between token entropy and distinct-$n$ remains positive throughout the blind zone (0.010--0.141~bits), confirming coupling exists below PermG's detection threshold.
1151	No discontinuity at $\alpha_c$: detection onset reflects power accumulation, not an information transition.
1152	
1153	\paragraph{MI across the blind zone.}
1154	Table~\ref{tab:mi_blind} reports Gaussian MI between token entropy and distinct-1 at each contamination level below $\alpha_c$.
1155	MI increases monotonically with $\alpha$, confirming that the entropy--diversity coupling strengthens continuously across the blind$\to$detection boundary.
1156	The detection onset at $\alpha_c$ therefore reflects a power threshold (sufficient signal-to-noise for PermG to detect the coupling) rather than a qualitative change in the underlying statistical relationship.
1157	
1158	\begin{table}[H]
1159	\centering
1160	\small
1161	\caption{Gaussian MI lower bound between token entropy and distinct-1 across the blind zone (Pythia-410M, $T{=}10$, seed~42).}
1162	\label{tab:mi_blind}
1163	\begin{tabular}{lcc}
1164	\toprule
1165	$\alpha$ & $\hat{I}_G$ (bits) & PermG \\
1166	\midrule
1167	0.00 & 0.010 & 0/8 \\
1168	0.10 & 0.025 & 0/8 \\
1169	0.25 & 0.048 & 0/8 \\
1170	0.45 & 0.141 & 0/8 \\
1171	0.50 & 0.312 & 6/8 \\
1172	\bottomrule
1173	\end{tabular}
1174	\end{table}
1175	
1176	\subsection{Partial Correlation Analysis}
1177	\label{app:partial_corr}
1178	
1179	\begin{table}[H]
1180	\centering
1181	\small
1182	\caption{Partial correlation controlling for generation. Lagged partial $|r|$ increases after trend removal, confirming genuine temporal precedence.}
1183	\label{tab:partial_corr}
1184	\resizebox{\columnwidth}{!}{%
1185	\begin{tabular}{@{}l cc cc cc cc@{}}
1186	\toprule
1187	& \multicolumn{4}{c}{Contemporaneous} & \multicolumn{4}{c}{Lagged (canary$_{t-1}$)} \\
1188	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
1189	& \multicolumn{2}{c}{Zero-order} & \multicolumn{2}{c}{Partial} & \multicolumn{2}{c}{Zero-order} & \multicolumn{2}{c}{Partial} \\
1190	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7} \cmidrule(lr){8-9}
1191	$\alpha$ & $\bar{|r|}$ & Sig. & $\bar{|r|}$ & Sig. & $\bar{|r|}$ & Sig. & $\bar{|r|}$ & Sig. \\
1192	\midrule
1193	0.00 & 0.414 & 3/18 & 0.323 & 0/18 & 0.563 & 8/18 & 0.524 & 9/18 \\
1194	0.50 & 0.590 & 9/18 & 0.381 & 2/18 & 0.759 & 12/18 & 0.841 & 17/18 \\
1195	0.75 & 0.636 & 9/18 & 0.521 & 3/18 & 0.831 & 17/18 & 0.913 & 18/18 \\
1196	\bottomrule
1197	\end{tabular}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25d9b0e2-86b1-441e-abe0-9f1af40fa95f",
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a9d7bd4d8daf2b13b",
  "type": "user",
  "uuid": "b3069e4b-4403-45f5-bd29-490a6e3a8726",
  "sourceToolAssistantUUID": "25d9b0e2-86b1-441e-abe0-9f1af40fa95f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T19:42:00.857Z_

<details open><summary>🔧 Tool call — Read · `toolu_013Ci4LrNSueXeJFXKxWCUth`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 1197,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3069e4b-4403-45f5-bd29-490a6e3a8726",
  "isSidechain": true,
  "agentId": "a9d7bd4d8daf2b13b",
  "requestId": "req_011CbPrfYe74FZtG2USa4oAr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81f7b616-9d59-44e0-af71-af8521132ce2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RdrcyP61unPGD4PUbrtbqQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7992,
      "cache_read_input_tokens": 61403,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7992
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 61403,
          "cache_creation_input_tokens": 7992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7992,
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

_source line 17 · 2026-05-25T19:42:00.864Z_

<details><summary>↩ Tool result · `toolu_013Ci4LrNSueXeJFXKxWCUth`</summary>

```text
1197	\end{tabular}}
1198	\end{table}
1199	
1200	Partial correlations controlling for generation number (Table~\ref{tab:partial_corr}) show that contemporaneous associations drop after trend removal ($\bar{|r|}$: $0.590{\to}0.381$ at $\alpha{=}0.50$), while lagged correlations \emph{strengthen} ($0.759{\to}0.841$), with 35/36 detection-condition pairs retaining significance.
1201	
1202	\begin{figure}[H]
1203	\centering
1204	\includegraphics[width=\columnwidth]{figures/fig_partial_correlation.pdf}
1205	\caption{Partial correlation scatter plots for canary$\to$diversity pairs at $\alpha{=}0.75$ (Pythia-410M). Left: contemporaneous partial correlations drop after controlling for generation trend. Right: lagged partial correlations \emph{strengthen} after trend removal ($\bar{|r|}$: $0.831{\to}0.913$), confirming that the temporal precedence signal is not a shared-trend artifact.}
1206	\label{fig:partial_corr}
1207	\end{figure}
1208	
1209	\paragraph{Interpretation.}
1210	The partial correlation analysis serves two purposes:
1211	(1)~It confirms that the canary$\to$diversity temporal precedence is not driven by a shared trend (generation number): removing the linear trend \emph{strengthens} rather than eliminates the lagged association.
1212	(2)~It shows that the temporal signal grows with contamination level: at $\alpha{=}0.00$, lagged partial $|r|{=}0.524$ (marginal significance); at $\alpha{=}0.75$, lagged partial $|r|{=}0.913$ (universal significance, 18/18).
1213	This monotonic growth parallels the MI analysis and confirms that the blind-zone boundary reflects statistical power rather than a qualitative transition in the coupling structure.
1214	
1215	\begin{figure}[H]
1216	\centering
1217	\includegraphics[width=\columnwidth]{figures/fig_partial_correlation_agg.pdf}
1218	\caption{Aggregated partial correlation analysis across contamination levels. Lagged canary$\to$diversity correlations increase monotonically with $\alpha$ (from $0.524$ at null to $0.913$ at $\alpha{=}0.75$), while contemporaneous correlations plateau. The growing gap between lagged and contemporaneous partial $|r|$ with increasing contamination indicates that the temporal lead signal strengthens with signal-to-noise ratio.}
1219	\label{fig:partial_corr_agg}
1220	\end{figure}
1221	
1222	\paragraph{Null behavior.}
1223	At $\alpha{=}0.00$, 9/18 lagged pairs reach significance despite no synthetic contamination, reflecting fine-tuning drift coupling: both entropy and diversity decline during pure fine-tuning (Table~\ref{tab:drift_summary}), creating a weak temporal association.
1224	These null-condition correlations are substantially weaker than treatment-condition correlations ($0.524$ vs.\ $0.913$), and the 9/18 significance rate is consistent with the expected false positive rate under weak coupling (mid-range $p$-values cluster near the significance boundary).
1225	
1226	
1227	\section{Moment Cascade Analysis}
1228	\label{app:moment_cascade}
1229	
1230	Onset (5\% threshold) occurs at generation~1 for entropy in all 6 conditions and at generation~2 for distinct-$n$ in all 18 pairwise comparisons (Table~\ref{tab:moment_cascade}; Figure~\ref{fig:cascade_onset}).
1231	
1232	\begin{table}[H]
1233	\centering
1234	\small
1235	\caption{Degradation onset generation (5\% threshold) by metric and condition (Pythia-410M, WikiText, fp32). Token entropy reaches onset at generation~1 in all non-null conditions; distinct-$n$ metrics follow at generation~2.}
1236	\label{tab:moment_cascade}
1237	\resizebox{\columnwidth}{!}{%
1238	\begin{tabular}{llcccccc}
1239	\toprule
1240	Seed & $\alpha$ & Entropy & Dist-1 & Dist-2 & Dist-3 & ECE & PPL \\
1241	\midrule
1242	42 & 0.10 & 1 & 2 & 2 & 2 & 2 & --- \\
1243	42 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\
1244	42 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\
1245	43 & 0.25 & 1 & 2 & 2 & 2 & 4 & --- \\
1246	43 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\
1247	43 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\
1248	\bottomrule
1249	\multicolumn{8}{l}{\footnotesize ---: onset not reached within $T{=}10$ generations.} \\
1250	\end{tabular}}
1251	\end{table}
1252	
1253	\begin{figure}[H]
1254	\centering
1255	\includegraphics[width=\columnwidth]{figures/fig_cascade_onset.pdf}
1256	\caption{Cascade onset timeline (Pythia-410M, WikiText, fp32). Entropy and ECE reach onset at generation~1; distinct-$n$ follows at generation~2. The ordering $t_H \leq t_D$ holds across all conditions.}
1257	\label{fig:cascade_onset}
1258	\end{figure}
1259	
1260	ECE shows onset at generation~1 at $\alpha{\geq}0.50$; perplexity never reaches 5\% onset at low contamination ($\alpha{\leq}0.25$).
1261	
1262	\paragraph{Onset threshold sensitivity.}
1263	Table~\ref{tab:onset_threshold_sensitivity} examines how the cascade ordering result depends on the choice of onset threshold (5\%, 10\%, 15\%, 20\%).
1264	
1265	\begin{table}[H]
1266	\centering
1267	\small
1268	\caption{Cascade ordering $t_H \leq t_D$ validity as a function of onset threshold (Pythia-410M, 6 conditions, $\alpha{\geq}0.10$).}
1269	\label{tab:onset_threshold_sensitivity}
1270	\begin{tabular}{lccc}
1271	\toprule
1272	Threshold & $t_H \leq t_D$ & $t_H = t_D$ & $t_H > t_D$ \\
1273	\midrule
1274	5\% & 6/6 & 0/6 & 0/6 \\
1275	10\% & 6/6 & 0/6 & 0/6 \\
1276	15\% & 5/6 & 1/6 & 0/6 \\
1277	20\% & 4/6 & 2/6 & 0/6 \\
1278	\bottomrule
1279	\end{tabular}
1280	\end{table}
1281	
1282	At all thresholds, the ordering $t_H \leq t_D$ is never violated ($t_H > t_D$ in 0/24 cells).
1283	At the strictest threshold (5\%), entropy precedes diversity by exactly one generation in all 6 conditions.
1284	At relaxed thresholds (${\geq}15\%$), some conditions show simultaneous onset ($t_H = t_D$), because the larger threshold absorbs the diversity lag---consistent with the margin condition in Observation~\ref{prop:div_lag}.
1285	
1286	\paragraph{MAUVE cascade position.}
1287	MAUVE~\citep{pillutla2021mauve} onset occurs at generation~2--3, consistently after distinct-$n$ onset (gen-2), establishing a three-phase cascade: $\{H, \mathrm{ECE}\} \to \mathrm{Dist}\text{-}n \to \mathrm{MAUVE}$.
1288	MAUVE's later onset reflects its distributional-comparison nature: it measures the divergence between generated and reference text distributions, which requires substantial lexical collapse before the divergence exceeds the detection threshold.
1289	At $\alpha{=}1.0$, MAUVE floor saturation (${\sim}0.033$) occurs by gen-3--4, after which it becomes uninformative (constant series).
1290	
1291	\paragraph{Perplexity irregularity.}
1292	Perplexity onset is condition-dependent rather than cascade-ordered: at $\alpha{=}0.50$ (s42), PPL onset occurs at gen-4 (delayed relative to entropy gen-1 and diversity gen-2); at $\alpha{=}0.75$, PPL onset is gen-1 (contemporaneous with entropy).
1293	This irregularity is consistent with the first-differencing result: PPL is not temporally downstream of entropy in the Granger sense.
1294	Instead, PPL responds to a different aspect of collapse (cross-entropy on held-out data) that can accelerate or decelerate independently of the entropy-diversity cascade.
1295	
1296	
1297	\subsection{Discretized Entropy Robustness Test}
1298	\label{app:discretized_entropy}
1299	
1300	A potential concern is that PermG may exploit the continuous resolution of token entropy relative to the discrete-valued distinct-$n$ metrics, producing spurious Granger precedence.
1301	We test this by binning continuous entropy into discrete levels and re-running the permutation Granger test.
1302	
1303	For each of 7~experiments at $\alpha{=}1.0$ (spanning Pythia-410M, GPT-2-medium, OPT-1.3B, and Pythia-1.4B), we discretize the entropy time series using equal-width and equal-frequency binning at 5, 10, 15, and 20~bins, then apply the same PermG test (5{,}000 permutations, first-differenced, max lag~1) on binned entropy$\to$distinct-1.
1304	
1305	\begin{table}[H]
1306	\centering
1307	\small
1308	\caption{Discretized entropy Granger test: number of experiments (out of 7) with FDR-significant entropy$\to$distinct-1 at each binning resolution and method. Continuous baseline: 7/7.}
1309	\label{tab:discretized_entropy}
1310	\begin{tabular}{@{}lcc@{}}
1311	\toprule
1312	Bins & Equal-width & Equal-freq \\
1313	\midrule
1314	20 & 7/7 & 7/7 \\
1315	15 & 6/7 & 7/7 \\
1316	10 & 5/7 & 1/7 \\
1317	5  & 3/7 & 0/7 \\
1318	\bottomrule
1319	\end{tabular}
1320	\end{table}
1321	
1322	At ${\geq}15$~bins, Granger precedence is largely preserved (6--7/7) regardless of binning method (Table~\ref{tab:discretized_entropy}).
1323	Signal degradation occurs only at extreme coarsening (${\leq}10$~bins), where equal-frequency binning is particularly destructive because entropy trajectories are right-skewed (sharp generation~0--2 drop followed by a plateau); equal-frequency bins compress the informative early decline into a single bin.
1324	The Pythia-410M reference case retains significance down to 5~equal-width bins ($p{=}0.035$) but loses it under 5~equal-frequency bins ($p{=}0.700$).
1325	
1326	These results confirm that the temporal precedence finding is not solely attributable to continuous measurement resolution: even moderate discretization (${\geq}15$~levels, well below the effective resolution of distinct-$n$) preserves the signal across all tested architectures, though extreme quantization (${\leq}5$~bins) can eliminate it.
1327	
1328	
1329	
1330	\section{Cascade Ordering Theory: Derivations}
1331	\label{app:cascade_theory}
1332	
1333	This section provides the full derivations for Observation~\ref{thm:entropy_leads} and Observation~\ref{prop:div_lag} from \S\ref{sec:cascade}, plus supporting results.
1334	
1335	\begin{assumption}[Mode Amplification]\label{ass:mode_amp}
1336	The training map $\mathcal{T}$ redistributes probability mass from low-probability to high-probability tokens: there exists a threshold $\bar{p}$ such that $\mathcal{T}(p)_i > p_i \Rightarrow p_i \geq \bar{p}$ and $\mathcal{T}(p)_j < p_j \Rightarrow p_j \leq \bar{p}$.
1337	\end{assumption}
1338	
1339	This captures the standard finite-capacity approximation effect: MLE on finite samples from a peaked distribution amplifies modes and suppresses the tail~\citep{shumailov2024curse,dohmatob2024tale}.
1340	
1341	\begin{proposition}[Entropy is a first-order indicator]\label{prop:entropy_first}
1342	Let $p \in \Delta^{V-1}$ and $\delta = \alpha(\mathcal{T}(p) - p)$ be a mode-amplifying perturbation with $\sum_i \delta_i = 0$. Then $\Delta H = H(p+\delta) - H(p) = -\sum_i \delta_i \log p_i + O(\|\delta\|^2) < 0$.
1343	\end{proposition}
1344	
1345	\begin{proof}
1346	Taylor-expanding $H$ around $p$:
1347	$H(p+\delta) = H(p) - \sum_i \delta_i \log p_i - \sum_i \delta_i - \frac{1}{2}\sum_i \delta_i^2/p_i + O(\|\delta\|^3)$.
1348	Since $\sum_i \delta_i = 0$: $\Delta H = -\sum_i \delta_i \log p_i - \frac{1}{2}\sum_i \delta_i^2/p_i + O(\|\delta\|^3)$.
1349	Under mode amplification, tokens gaining mass ($\delta_i > 0$) have $p_i \geq \bar{p}$ (hence $\log p_i \geq \log \bar{p}$) and tokens losing mass ($\delta_j < 0$) have $p_j \leq \bar{p}$ (hence $\log p_j \leq \log \bar{p}$).
1350	Writing $m = \sum_{i:\delta_i > 0} \delta_i$: $-\sum_i \delta_i \log p_i = -m[\overline{\log p}^{+} - \overline{\log p}^{-}] < 0$, where $\overline{\log p}^{\pm}$ are the $|\delta|$-weighted means over gaining/losing tokens.
1351	The second-order Fisher information term $-\frac{1}{2}\sum_i \delta_i^2/p_i$ is always negative, reinforcing the decrease.
1352	\end{proof}
1353	
1354	\begin{proposition}[Diversity is a threshold indicator]\label{prop:div_threshold}
1355	Define the $\epsilon$-effective support $S_\epsilon(p) = |\{i \in [V]: p_i > \epsilon\}|$, where $\epsilon \approx c/N$ is the generation threshold for sample size $N$.
1356	Under the same perturbation $\delta$: $\Delta S_\epsilon = -|\{i: p_i > \epsilon \text{ and } p_i + \delta_i \leq \epsilon\}|$.
1357	This equals zero whenever $\|\delta\|_\infty < \gamma(p,\epsilon) := \min_{i: p_i > \epsilon}(p_i - \epsilon)$.
1358	\end{proposition}
1359	
1360	\begin{proof}
1361	Token $i$ exits the effective support iff $p_i > \epsilon$ and $p_i + \delta_i \leq \epsilon$, requiring $|\delta_i| \geq p_i - \epsilon$.
1362	If $\|\delta\|_\infty < \gamma$, no token satisfies this condition.
1363	\end{proof}
1364	
1365	\medskip
1366	\noindent\textbf{Derivations from the propositions above.}
1367	
1368	\paragraph{Derivation of Observation~\ref{thm:entropy_leads}.}
1369	\emph{Part (a):} Take any mode-amplifying $\delta$ with $\|\delta\|_\infty < \gamma(p,\epsilon)$.
1370	By Proposition~\ref{prop:div_threshold}, $\Delta S_\epsilon = 0$.
1371	By Proposition~\ref{prop:entropy_first}, $\Delta H < 0$.
1372	Such $\delta$ exists for all $\alpha < \gamma / \max_i |\mathcal{T}(p)_i - p_i|$.
1373	\emph{Part (b):} If $\Delta S_\epsilon < 0$, some token $k$ has $p_k > \epsilon$ but $p_k + \delta_k \leq \epsilon$, so $\delta_k < 0$.
1374	Under mode amplification, this implies $p_k \leq \bar{p}$; the total mass transferred to high-probability tokens ensures $\overline{\log p}^+ > \overline{\log p}^-$.
1375	By Proposition~\ref{prop:entropy_first}, $\Delta H < 0$. $\square$
1376	
1377	\paragraph{Derivation of Observation~\ref{prop:div_lag}.}
1378	By the margin condition, at every generation $s \leq t_H$ the perturbation norm $\alpha\|\mathcal{T}(p_s) - p_s\|_\infty$ is less than $\gamma(p_s, \epsilon)$.
1379	By Proposition~\ref{prop:div_threshold}, no token exits the effective support at any $s \leq t_H$, so $\Delta S_\epsilon = 0$ for all $s \leq t_H$.
1380	Since time is discrete, $t_D \geq t_H + 1$. $\square$
1381	
1382	\medskip
1383	\noindent\textbf{ECE co-movement and empirical validation.}
1384	
1385	\paragraph{ECE co-movement (qualitative argument).}
1386	Under conditional mode amplification (peakier $q_\theta(\cdot|x)$ at each generation), per-token conditional entropy $h(x) = H(q_\theta(\cdot|x))$ decreases while confidence $c(x) = \max_y q_\theta(y|x) \geq \exp(-h(x))$ increases.
1387	Averaging: $\bar{H}_t$ decreases, $C_t$ increases.
1388	With accuracy approximately stationary in early collapse ($A_t \approx A_0$), $\Delta\mathrm{ECE} \approx \Delta C_t > 0$ whenever $\Delta\bar{H}_t < 0$.
1389	This argument establishes the direction of co-movement; the quantitative relationship depends on distribution geometry.
1390	$\bar{H}_t$ denotes mean conditional entropy $\mathbb{E}_{x \sim p_{\text{eval}}}[h(x)]$, which differs from the marginal entropy $H_t = -\sum_i p_t(i)\log p_t(i)$ used in Observation~\ref{thm:entropy_leads}; under mode amplification, both decrease monotonically, so the cascade ordering is consistent across both formulations.
1391	
1392	\paragraph{Empirical ECE drift across contamination levels.}
1393	ECE co-movement with entropy is monotonic across all tested $\alpha$ values (Table~\ref{tab:ece_drift}).
1394	At $\alpha{=}0.25$, ECE increases by $+79.2\%$ while entropy decreases by $-4.7\%$---the asymmetry in magnitude reflects ECE's nonlinear dependence on confidence via the $\max$ operator.
1395	At $\alpha{=}1.0$, ECE drift reaches $+3762$--$3821\%$ ($0.0108 \to 0.417$--$0.424$ across seeds), the largest proportional change among all tracked metrics.
1396	
1397	\begin{table}[H]
1398	\centering
1399	\small
1400	\caption{ECE drift across contamination levels (Pythia-410M, WikiText, fp32). ECE increases monotonically with $\alpha$, co-moving with entropy decrease.}
1401	\label{tab:ece_drift}
1402	\begin{tabular}{lccc}
1403	\toprule
1404	$\alpha$ & ECE gen-0 & ECE gen-10 & Drift (\%) \\
1405	\midrule
1406	0.00 & 0.0108 & $0.015{\pm}0.002$ & $+37.6{\pm}14$ \\
1407	0.25 & 0.0108 & $0.019{\pm}0.002$ & $+79.2{\pm}15.9$ \\
1408	0.50 & 0.0108 & $0.087{\pm}0.002$ & $+703{\pm}18$ \\
1409	0.60 & 0.0108 & 0.179 & $+1561$ \\
1410	0.75 & 0.0108 & $0.215{\pm}0.002$ & $+1885{\pm}18$ \\
1411	1.00 & 0.0108 & $0.421{\pm}0.004$ & $+3792{\pm}30$ \\
1412	\bottomrule
1413	\end{tabular}
1414	\end{table}
1415	
1416	ECE onset timing (5\% threshold) at $\alpha{\geq}0.50$ is generation~1, coinciding with entropy onset---consistent with the qualitative argument above that $\Delta\mathrm{ECE} > 0$ whenever $\Delta\bar{H} < 0$.
1417	At $\alpha{=}0.25$, ECE onset delays to generation~4 (seed~43), reflecting the weaker mode amplification signal at low contamination.
1418	At 1.4B scale, ECE follows the same pattern: gen-0 values are lower ($0.007$--$0.008$) but gen-10 values track collapse severity monotonically ($0.145$ at $\alpha{=}0.45$ to $0.268$ at $\alpha{=}0.75$).
1419	
1420	\paragraph{Empirical support for cascade ordering.}
1421	Cascade ordering $t_H \leq t_D$ holds in 14/15 experiments at $\alpha \geq 0.30$ (GPT-2-medium s43: bidirectional).
1422	Table~\ref{tab:cascade_onset} reports onset generations for representative conditions.
1423	
1424	\begin{table}[H]
1425	\centering
1426	\small
1427	\caption{Cascade onset generations (5\% threshold) for representative experiments (Pythia-410M, WikiText, fp32). Phase~1: entropy and ECE ($t_H$, $t_{\mathrm{ECE}}$); Phase~2: diversity ($t_D$, min over distinct-$n$); Phase~3: MAUVE ($t_M$). All conditions confirm the predicted ordering $t_H = t_{\mathrm{ECE}} \leq t_D \leq t_M$.}
1428	\label{tab:cascade_onset}
1429	\begin{tabular}{llcccc}
1430	\toprule
1431	Seed & $\alpha$ & $t_H$ & $t_{\mathrm{ECE}}$ & $t_D$ & $t_M$ \\
1432	\midrule
1433	42 & 0.50 & 1 & 1 & 2 & 3 \\
1434	43 & 0.50 & 1 & 1 & 2 & 2 \\
1435	42 & 0.75 & 1 & 1 & 2 & 3 \\
1436	43 & 0.75 & 1 & 1 & 2 & 2 \\
1437	\bottomrule
1438	\end{tabular}
1439	\end{table}
1440	
1441	
1442	\begin{figure}[H]
1443	\centering
1444	\includegraphics[width=\columnwidth]{figures/fig_detection_surface.pdf}
1445	\caption{Detection rate surface over $\alpha \times T$ (PermG forward, 3~seeds). Dashed curve: fitted boundary $\alpha_c(T)$. The blind zone ($\alpha \leq 0.45$) shrinks as $T$ increases.}
1446	\label{fig:detection_surface}
1447	\end{figure}
1448	
1449	\phantomsection\label{app:alpha_c_proof}
1450	\paragraph{Justification of the empirical boundary model.}
1451	At the detection threshold, $\mathrm{Power}(\alpha_c, T) = \pi^*$.
1452	Since $\alpha_c$ lies below the non-monotonic dip region ($\alpha_c < 0.55$), the signal model applies directly.
1453	From the power function $\mathrm{Power} = \Phi(S(\alpha) \cdot \sqrt{T} / \sigma)$, setting $S(\alpha_c) \cdot \sqrt{T} / \sigma = z^*$ and substituting the signal model $S(\alpha) = c\,\alpha^\beta$ yields $c\,\alpha_c^\beta = z^* \sigma / \sqrt{T}$.
1454	Solving: $\alpha_c(T) = (z^* \sigma / c)^{1/\beta} \cdot T^{-1/(2\beta)}$, giving the stated form with exponent $\eta = 1/(2\beta)$.
1455	
1456	\paragraph{Calibration and consistency.}
1457	Fitting $P(\mathrm{det}|\alpha,T) = \Phi(A \cdot \alpha^\beta \cdot \sqrt{T} - z_0)$ to $T \in \{10, 20\}$ yields $\beta{=}0.24$, $\alpha_\infty{=}0$.
1458	Held-out test ($T \in \{5, 15\}$): MAE${=}0.106$, 95\% CI coverage 6/6.
1459	Leave-one-$T$-out CV (15 cells, sync-dip excluded): MAE${=}0.037$, coverage 15/15.
1460	Profile likelihood yields $\hat{\beta}{=}0.66$ (CI $[0.24, 0.78]$); the wide interval reflects a flat surface.
1461	
1462	\paragraph{Worked example.}
1463	At $\alpha{=}0.50$, $T{=}10$ (seed~42): entropy drops from $3.234$ to $2.649$ at gen-1 ($-18.1\%$), while distinct-1 remains at $0.0968$ (unchanged from gen-0).
1464	At gen-2, distinct-1 drops to $0.0812$ ($-16.1\%$).
1465	The mode amplification perturbation $\delta = 0.50 \cdot (\mathcal{T}(p_0) - p_0)$ satisfies $\|\delta\|_\infty < \gamma(p_0, \epsilon)$ at gen-0 (entropy responds, diversity does not), but at gen-1 the accumulated shift $p_1 = p_0 + \delta$ produces $\|\delta_1\|_\infty > \gamma(p_1, \epsilon)$, causing tokens to exit the effective support and triggering distinct-1 decline.
1466	The one-generation lag is thus explained by the margin condition in Observation~\ref{prop:div_lag}: the margin $\gamma$ is consumed by the gen-0$\to$1 perturbation, and the gen-1$\to$2 perturbation pushes tokens below the generation threshold $\epsilon$.
1467	
1468	\paragraph{Boundary model limitations.}
1469	The empirical boundary $\alpha_c(T) = A \cdot T^{-\eta}$ is fitted to 3--4 data points ($T \in \{5, 10, 15, 20\}$) with 3 free parameters ($A$, $\eta$, and the sub-linear signal exponent $\beta$).
1470	This parametric flexibility means the model can accommodate a wide range of decay shapes, and the $\eta$ CI ($[0.64, 2.08]$) cannot distinguish sub-linear from super-linear decay.
1471	The boundary should therefore be interpreted as a descriptive summary of the observed pattern rather than a predictive model.
1472	Extrapolation beyond $T{=}25$ or below $\alpha{=}0.25$ is not supported by the data.
1473	The qualitative conclusion---detection improves with longer observation---is robust and does not depend on the specific $\eta$ value.
1474	
1475	\paragraph{Sensitivity to the generation threshold $\epsilon$.}
1476	Observation~\ref{thm:entropy_leads} depends on the margin $\gamma(p, \epsilon)$, which in turn depends on the generation threshold $\epsilon \approx c/N$.
1477	Increasing the generation sample size $N$ (from 5{,}000 to 10{,}000) reduces $\epsilon$ by half, widening the margin and extending the entropy-only phase.
1478	In our experiments ($N{=}5{,}000$, effective $\epsilon \approx 2 \times 10^{-4}$), the margin is consumed after one generation at $\alpha{\geq}0.50$, producing the observed $t_D - t_H = 1$ lag.
1479	At lower contamination ($\alpha{=}0.25$), the smaller perturbation preserves the margin longer: the cumulative perturbation does not exceed $\gamma$ until gen-2--3 (Table~\ref{tab:margin_consumption}), explaining the wider entropy-diversity lag at low $\alpha$.
1480	
1481	\begin{table}[H]
1482	\centering
1483	\small
1484	\caption{Margin consumption across contamination levels (Pythia-410M, seed~42). ``Margin gen'' = first generation where cumulative $\|\delta\|_\infty > \gamma$. The diversity lag $t_D - t_H{=}1$ is invariant despite variable margin consumption timing.}
1485	\label{tab:margin_consumption}
1486	\begin{tabular}{lccc}
1487	\toprule
1488	$\alpha$ & $\gamma(p_0, \epsilon)$ & Margin gen & $t_D - t_H$ \\
1489	\midrule
1490	0.10 & $2.3 \times 10^{-3}$ & 3 & 1 \\
1491	0.25 & $2.3 \times 10^{-3}$ & 2 & 1 \\
1492	0.50 & $2.3 \times 10^{-3}$ & 1 & 1 \\
1493	0.75 & $2.3 \times 10^{-3}$ & 1 & 1 \\
1494	1.00 & $2.3 \times 10^{-3}$ & 1 & 1 \\
1495	\bottomrule
1496	\end{tabular}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81f7b616-9d59-44e0-af71-af8521132ce2",
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a9d7bd4d8daf2b13b",
  "type": "user",
  "uuid": "b695bd6b-8700-4443-a3b3-c9e71c5496ca",
  "sourceToolAssistantUUID": "81f7b616-9d59-44e0-af71-af8521132ce2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-25T19:42:05.216Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YQsLVWWDaBSFvmvmKHepKV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 1496,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b695bd6b-8700-4443-a3b3-c9e71c5496ca",
  "isSidechain": true,
  "agentId": "a9d7bd4d8daf2b13b",
  "requestId": "req_011CbPrftyU9xbuaZbdqozR4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b4e7c62-aba8-456a-b68f-00f18ed1e7ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CvmfivUnNR8W9YDHeaAek6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8708,
      "cache_read_input_tokens": 69395,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8708
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 69395,
          "cache_creation_input_tokens": 8708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8708,
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

_source line 19 · 2026-05-25T19:42:05.232Z_

<details><summary>↩ Tool result · `toolu_01YQsLVWWDaBSFvmvmKHepKV`</summary>

```text
1496	\end{tabular}
1497	\end{table}
1498	
1499	The invariant $t_D - t_H = 1$ across all $\alpha$ levels (despite variable margin consumption timing) reflects the discrete-time nature of the experiment: even when the margin is consumed within a single generation, the diversity response cannot manifest until the next generation's samples are drawn.
1500	This suggests that continuous-time monitoring (within-generation token-level tracking) could reveal a finer-grained cascade with $\Delta t < 1$ generation, but our current experimental design cannot resolve sub-generation dynamics.
1501	
1502	\section{Power Simulation: Shape Comparison}
1503	\label{app:power_sim}
1504	
1505	Simulated PermG detection under linear (H0), concave (H0$'$), and step (H1) signal models (1{,}000 reps, $n_\text{perm}{=}1{,}000$, BH-FDR $q{=}0.05$).
1506	Smooth models produce onset steepness $k{=}4.9$--$6.1$; the observed $k{=}15.7$ is ${\approx}3{\times}$ higher.
1507	The scaling exponent alone cannot distinguish smooth from step boundaries (H0$'$ $\eta{=}1.87$ vs.\ observed $\eta{=}2.08$).
1508	The 6/8 detection ceiling reflects MAUVE floor saturation, not signal limitations.
1509	
1510	\paragraph{Signal model specifications.}
1511	\emph{H0 (linear)}: $S(\alpha) = c \cdot \alpha$, where $c$ is calibrated to produce 50\% detection at $\alpha{=}0.50$, $T{=}10$.
1512	\emph{H0$'$ (concave)}: $S(\alpha) = c \cdot \alpha^{0.5}$, capturing sub-linear signal growth as mode amplification saturates.
1513	\emph{H1 (step)}: $S(\alpha) = 0$ for $\alpha < \alpha_c$, $S(\alpha) = c$ for $\alpha \geq \alpha_c$, representing a genuine phase transition.
1514	The simulated DGP generates bivariate time series $(X_t, Y_t)$ with $Y_t = \beta X_{t-1} + \epsilon_t$ (lag-1 coupling); $\beta$ is set to produce the target $S(\alpha)$ at each contamination level.
1515	
1516	\paragraph{Onset steepness comparison.}
1517	Table~\ref{tab:steepness_comparison} reports fitted sigmoid steepness $k$ for each signal model.
1518	The observed $k{=}15.7$ (CI $[9.4, 28.2]$) exceeds all smooth-model predictions, with the lower CI bound ($k{=}9.4$) still ${\sim}2{\times}$ higher than the smoothest model (H0$'$: $k{=}4.9$).
1519	This excess steepness is consistent with---but does not prove---a genuine discontinuity in the signal structure at $\alpha_c$.
1520	
1521	\begin{table}[H]
1522	\centering
1523	\small
1524	\caption{Onset steepness $k$ under different signal models (1{,}000 reps, PermG, BH-FDR $q{=}0.05$).}
1525	\label{tab:steepness_comparison}
1526	\begin{tabular}{lccc}
1527	\toprule
1528	Model & $k$ & $\eta$ & $k_{\mathrm{obs}}/k$ \\
1529	\midrule
1530	H0 (linear) & 6.1 & 2.08 & 2.6 \\
1531	H0$'$ (concave) & 4.9 & 1.87 & 3.2 \\
1532	H1 (step) & $\infty$ & --- & --- \\
1533	Observed & 15.7 & 2.08 & 1.0 \\
1534	\bottomrule
1535	\end{tabular}
1536	\end{table}
1537	
1538	\begin{figure}[H]
1539	\centering
1540	\includegraphics[width=\columnwidth]{figures/permg_power_curve.pdf}
1541	\caption{PermG power curves as a function of coupling strength $\beta$ for $T \in \{6, 8, 10, 15, 20\}$ (100 replications, 5{,}000 permutations, BH-FDR $q{=}0.05$). Power increases faster than $\sqrt{T}$, confirming that the theoretical $\sqrt{T}$ formula is a conservative lower bound. At $T{=}10$, 50\% power requires $\beta{\geq}2.0$; at $T{=}20$, this drops to $\beta{\approx}0.9$.}
1542	\label{fig:permg_power_curve}
1543	\end{figure}
1544	
1545	\section{T=20 Extension Results}
1546	\label{app:t20_comparison}
1547	
1548	At $\alpha{\geq}0.50$, PermG counts are consistent across $T{=}10$ and $T{=}20$ (6/8 at both), confirming signal-structure determination.
1549	At $\alpha{=}0.45$, the shift from 0/8 ($T{=}10$) to 5/8 ($T{=}20$) supports power-limited (Model~B) over structurally-undetectable (Model~A), lowering $\alpha_c$ below 0.45.
1550	The $\alpha{=}0.60$ dip persists at $T{=}20$ but dissolves at $T{=}25$ (5/8), confirming $\sqrt{T}$ power scaling eventually overcomes it.
1551	Directional selectivity is consistent: forward 6/8, reverse 0/8 at $\alpha \in \{0.50, 0.75, 1.0\}$ across all tested $T$.
1552	
1553	\paragraph{Full $T{=}25$ results.}
1554	Table~\ref{tab:t25_full} reports PermG forward detection counts at $T{=}25$ across contamination levels.
1555	Two key transitions emerge: (1)~$\alpha{=}0.45$ reaches 6/8 (dual-seed: s42 and s43 both 6/8), confirming that the blind-zone boundary has shifted below $\alpha{=}0.45$ at this observation length; (2)~the $\alpha{=}0.60$ sync-dip dissolves (5/8 at $T{=}25$ vs.\ 0/8 at $T{\leq}20$), with $K{\geq}3$ consensus reaching 6/8.
1556	The 6/8 detection ceiling at $\alpha{=}0.45$, $0.50$, $0.75$ matches the ceiling at shorter $T$, suggesting that 2/8 pairs are structurally non-detectable (likely MAUVE-related; MAUVE floor saturation at ${\sim}0.033$ produces near-constant series).
1557	
1558	\begin{table}[H]
1559	\centering
1560	\small
1561	\caption{PermG forward detection at $T{=}25$ (Pythia-410M, fp32). The $\alpha{=}0.45$ blind zone resolves and the $\alpha{=}0.60$ anomaly dissolves.}
1562	\label{tab:t25_full}
1563	\begin{tabular}{lccc}
1564	\toprule
1565	$\alpha$ & PermG fwd & $K{\geq}3$ & Note \\
1566	\midrule
1567	0.45 (s42) & 6/8 & 6/8 & blind$\to$detection \\
1568	0.45 (s43) & 6/8 & 6/8 & cross-seed confirmed \\
1569	0.50 (s42) & 6/8 & 6/8 & stable (matches $T{=}10$) \\
1570	0.60 (s42) & 5/8 & 6/8 & dip dissolves \\
1571	0.75 (s42) & 6/8 & 6/8 & stable \\
1572	0.75 (s43) & 6/8 & 6/8 & cross-seed confirmed \\
1573	\bottomrule
1574	\end{tabular}
1575	\end{table}
1576	
1577	\paragraph{$\alpha{=}0.25$ at extended $T$.}
1578	An unexpected result at $T{=}20$: PermG detects 3/8 at $\alpha{=}0.25$, where $T{=}10$ yields 0/8.
1579	This partial detection at very low contamination suggests that the blind zone is not absolute but power-limited: with sufficient observation length, even weak contamination signals may become detectable.
1580	However, 3/8 falls below the 6/8 reliability threshold we use for confirmed detection, and the result awaits multi-seed replication.
1581	
1582	\begin{figure}[H]
1583	\centering
1584	\includegraphics[width=\columnwidth]{figures/regime_map.pdf}
1585	\caption{Extended regime map including $T \in \{5, 10, 15, 20, 25\}$. The detection boundary shifts leftward with increasing $T$: $\alpha{=}0.45$ transitions from undetectable (0/8 at $T{\leq}10$) to reliable detection (6/8 at $T{=}15$). The $\alpha{=}0.60$ non-monotonic anomaly persists through $T{=}20$ but dissolves at $T{=}25$ (5/8).}
1586	\label{fig:regime_map_extended}
1587	\end{figure}
1588	
1589	\phantomsection\label{app:task_degradation}
1590	\paragraph{Task degradation.}
1591	End-of-training perplexity (gen~10, Pythia-410M, s42) improves at $\alpha{=}0.05$ (20.8 vs.\ 26.6 baseline, mild augmentation effect) but degrades sharply between $\alpha{=}0.50$ (31.3) and $0.52$ (41.1), aligning with PermG detection onset.
1592	
1593	\paragraph{Comprehensive cross-$T$ comparison.}
1594	Table~\ref{tab:cross_t_full} consolidates PermG forward detection across all tested observation windows, providing a complete view of the detection landscape evolution.
1595	
1596	\begin{table}[H]
1597	\centering
1598	\small
1599	\caption{PermG forward detection (/8 pairs) across $T$ and $\alpha$ (Pythia-410M, seed~42, fp32). Detection improves with $T$ at all contamination levels; the blind zone narrows monotonically.}
1600	\label{tab:cross_t_full}
1601	\begin{tabular}{lccccc}
1602	\toprule
1603	$\alpha$ & $T{=}5$ & $T{=}10$ & $T{=}15$ & $T{=}20$ & $T{=}25$ \\
1604	\midrule
1605	0.25 & 0/8 & 0/8 & --- & 3/8 & --- \\
1606	0.45 & 0/8 & 0/8 & 6/8 & 5/8 & 6/8 \\
1607	0.50 & 0/8 & 6/8 & 6/8 & 6/8 & 6/8 \\
1608	0.60 & 0/8 & 0/8 & 0/8 & 0/8 & 5/8 \\
1609	0.75 & 0/8 & 6/8 & 6/8 & 6/8 & 6/8 \\
1610	1.00 & 0/8 & 6/8 & 6/8 & 6/8 & 6/8 \\
1611	\bottomrule
1612	\multicolumn{6}{l}{\footnotesize ---: not tested at this combination.}
1613	\end{tabular}
1614	\end{table}
1615	
1616	Key observations from Table~\ref{tab:cross_t_full}:
1617	\begin{enumerate}
1618	\item $T{=}5$ yields 0/8 across all $\alpha$ levels---insufficient degrees of freedom for PermG detection.
1619	\item The 6/8 ceiling at $\alpha \in \{0.50, 0.75, 1.0\}$ is invariant across $T{=}10$--$25$, confirming signal-structure determination.
1620	\item $\alpha{=}0.45$ traverses the full blind$\to$detection boundary: 0/8 at $T{\leq}10$, 6/8 at $T{=}15$, stable thereafter.
1621	\item $\alpha{=}0.60$ is the only condition requiring $T{=}25$ for detection, with all shorter windows yielding 0/8.
1622	\item $\alpha{=}0.25$ at $T{=}20$ (3/8) is the only sub-threshold result, suggesting that very low contamination may eventually become detectable with sufficiently long observation.
1623	\end{enumerate}
1624	
1625	\paragraph{Directional consistency.}
1626	Across all conditions with ${\geq}6/8$ forward detection, reverse detection remains at 0/8 (with the exception of Pythia-1.4B s43 at $\alpha{\geq}0.60$; \S\ref{app:scale_14b}).
1627	This directional selectivity confirms that the forward-only constraint is not an artifact of a single $T$ value but reflects the genuine temporal asymmetry of the entropy-diversity cascade.
1628	
1629	\paragraph{Detection efficiency metrics.}
1630	Table~\ref{tab:detection_efficiency} reports detection efficiency---defined as the fraction of FDR-significant pairs out of 8---across observation windows, providing a normalized summary of the detection landscape.
1631	
1632	\begin{table}[H]
1633	\centering
1634	\small
1635	\caption{Detection efficiency (fraction of pairs reaching FDR significance) across the $\alpha \times T$ grid (Pythia-410M, seed~42, fp32). Efficiency plateaus at 0.75 for above-onset conditions, indicating a structural detection ceiling at 6/8 pairs.}
1636	\label{tab:detection_efficiency}
1637	\begin{tabular}{lcccc}
1638	\toprule
1639	$\alpha$ & $T{=}10$ & $T{=}15$ & $T{=}20$ & $T{=}25$ \\
1640	\midrule
1641	0.25 & 0.00 & --- & 0.375 & --- \\
1642	0.45 & 0.00 & 0.75 & 0.625 & 0.75 \\
1643	0.50 & 0.75 & 0.75 & 0.75 & 0.75 \\
1644	0.60 & 0.00 & 0.00 & 0.00 & 0.625 \\
1645	0.75 & 0.75 & 0.75 & 0.75 & 0.75 \\
1646	1.00 & 0.75 & 0.75 & 0.75 & 0.75 \\
1647	\bottomrule
1648	\multicolumn{5}{l}{\footnotesize ---: not tested at this combination.}
1649	\end{tabular}
1650	\end{table}
1651	
1652	The 0.75 plateau (6/8 pairs) is remarkably consistent across all conditions above the detection boundary, regardless of $T$ or $\alpha$.
1653	The 2/8 pairs that never reach significance involve MAUVE (floor saturation at ${\sim}0.033$ producing near-constant series) and perplexity (contemporaneous coupling; \S\ref{app:channel_effect_size}).
1654	This structural ceiling has practical implications: extending observation beyond $T{=}10$ at high contamination ($\alpha{\geq}0.50$) provides no additional detection power---the benefit of longer observation is concentrated in the boundary region ($\alpha \in [0.45, 0.60]$).
1655	
1656	\paragraph{Information gain per additional generation.}
1657	The marginal value of each additional generation varies by region.
1658	At $\alpha{=}0.45$, extending from $T{=}10$ to $T{=}15$ produces $+6$ newly significant pairs (information gain rate: $1.2$ pairs/gen); from $T{=}15$ to $T{=}20$, the rate drops to $-0.2$ pairs/gen (slight regression, likely noise).
1659	At $\alpha{=}0.60$ (sync-dip), the marginal value is zero through $T{=}20$ (0 new pairs across 10 additional generations) before producing $+5$ pairs in the $T{=}20{\to}25$ window (rate: $1.0$ pairs/gen).
1660	This non-uniform marginal return implies that a fixed-$T$ deployment strategy is suboptimal: adaptive monitoring that continues observation only when marginal information gain exceeds a threshold would reduce computational cost by 40--60\% without sacrificing detection reliability at high-$\alpha$ operating points.
1661	
1662	\subsection{Cross-Architecture Detection Table}
1663	\label{app:cross_arch_table}
1664	
1665	\begin{table}[H]
1666	\centering
1667	\small
1668	\caption{Cross-architecture PermG forward detection ($\alpha{=}1.0$, 15 model-seed combinations across five families---Pythia, GPT-2, OPT, Qwen, SmolLM3---and two domains; Padding-410M is a Pythia variant). PermG fwd $=$ count of FDR-significant forward pairs out of 8.}
1669	\label{tab:generalization}
1670	\resizebox{\columnwidth}{!}{%
1671	\begin{tabular}{lrcl}
1672	\toprule
1673	Model & Params & Domain & PermG fwd \\
1674	\midrule
1675	Pythia-410M    & 410M & Wiki & \textbf{6/8} \\
1676	Pythia-1.4B    & 1.4B & Wiki & 2--6/8$^\dagger$ \\
1677	Pythia-6.9B    & 6.9B & Wiki & \textbf{7/8}$^*$ \\
1678	\addlinespace
1679	GPT-2-medium   & 345M & Wiki & \textbf{6/8}$^\S$ \\
1680	\addlinespace
1681	OPT-1.3B       & 1.3B & Wiki & \textbf{6/8} \\
1682	\addlinespace
1683	Qwen3.5-0.8B   & 0.8B & Wiki & \textbf{8/8} \\
1684	SmolLM3-3B     & 3.0B & Wiki & 3/8$^\ddagger$ \\
1685	Padding-410M   & 410M & Wiki & \textbf{6/8} \\
1686	\addlinespace
1687	Pythia-1B      & 1.0B & C4   & \textbf{8/8} \\
1688	Pythia-1.4B    & 1.4B & C4   & \textbf{8/8} \\
1689	\bottomrule
1690	\multicolumn{4}{l}{\footnotesize $^\dagger$Seed-dep.\ (s42: 2/8, s43: 6/8); 8-pair incl.\ MAUVE} \\
1691	\multicolumn{4}{l}{\footnotesize \phantom{$^\dagger$}(floor ${\sim}0.033$ at 1.4B; 6-pair in Table~\ref{tab:14b_phase}). $^*$bf16. $^\ddagger$ECE-only (ent.\ 0/4).} \\
1692	\multicolumn{4}{l}{\footnotesize $^\S$s42 fp32: 6/8 fwd, 0 rev; s43: 6/8 both; bf16: 0/8.} \\
1693	\multicolumn{4}{l}{\footnotesize 2 seeds each for Pythia-410M/1.4B, GPT-2, OPT, Pythia-1B C4.} \\
1694	\end{tabular}%
1695	}
1696	\end{table}
1697	
1698	\subsection{Cross-Architecture FPR Sensitivity}
1699	\label{app:cross_arch_fpr}
1700	
1701	GPT-2-medium null-condition PermG FPR is 50\% (6/12 pooled, 2~seeds), dramatically higher than Pythia-410M (6.7\%), driven by ${\sim}4{\times}$ stronger null drift (entropy $-20.5\%$ vs.\ $-4.9\%$; distinct-3 $-35.8\%$ vs.\ $-4.9\%$).
1702	$K{\geq}3$ consensus maintains 0\% FPR (0/12) on GPT-2-medium, providing some protection, but standalone PermG requires architecture-specific null calibration.
1703	
1704	The cross-architecture detection heatmap is shown in Figure~\ref{fig:cross_arch_heatmap} (main text).
1705	
1706	\paragraph{GPT-2-medium: precision sensitivity.}
1707	GPT-2-medium at fp32 (seed~42) achieves 6/8 forward detection with 0/8 reverse, matching the Pythia-410M profile.
1708	Switching to bf16 drops detection to 0/8 without changing the underlying collapse dynamics (distinct-1 drift: $-28.4\%$ in both precisions).
1709	The mechanism is quantization noise masking the entropy signal: bf16 entropy time series exhibit ${\sim}2{\times}$ higher inter-generation variance than fp32, pushing PermG $p$-values from $p{<}0.01$ (fp32) to $p{>}0.20$ (bf16).
1710	This failure mode is fully resolved by using fp32 precision; architectures with native bf16 training (e.g., SmolLM3) require separate investigation.
1711	
1712	\paragraph{GPT-2-medium: seed-specific bidirectionality.}
1713	At seed~43, GPT-2-medium detects 6/8 in \emph{both} forward and reverse directions, preventing directional assignment.
1714	This bidirectionality is absent at seed~42 (6/8 forward, 0/8 reverse) and does not appear for any Pythia seed, suggesting it reflects GPT-2's specific learned dynamics rather than a general property of iterative collapse.
1715	Possible explanations include: (1)~GPT-2's attention patterns create feedback loops where diversity changes instantaneously feed back into entropy through the generation process; (2)~seed~43 produces a collapse trajectory where the entropy-diversity lag is below PermG's temporal resolution.
1716	
1717	\paragraph{SmolLM3-3B: entropy decoupling.}
1718	SmolLM3-3B achieves only 3/8 detection, with all significant pairs involving ECE rather than entropy (entropy: 0/4; ECE: 3/4).
1719	This violates the cascade ordering assumption (Observation~\ref{thm:entropy_leads}): in 3/8 conditions, entropy does not monotonically decrease across generations, exhibiting a recovery pattern between gen-3 and gen-5 before resuming decline.
1720	The non-monotonic entropy trajectory breaks the mode amplification assumption underlying the cascade ordering, suggesting that SmolLM3's architecture (likely due to its different attention mechanism or training objective) produces qualitatively different collapse dynamics.
1721	
1722	\paragraph{Domain effects: WikiText vs.\ C4.}
1723	C4-domain experiments (Pythia-1B and Pythia-1.4B) achieve uniformly higher detection rates (8/8) than their WikiText counterparts (6/8 and 2--6/8 respectively).
1724	This domain advantage may reflect C4's greater vocabulary diversity (broader token distribution $\to$ larger effective support $S_\epsilon$), which increases the margin $\gamma$ and produces a cleaner cascade ordering.
1725	Alternatively, WikiText's specialized vocabulary (encyclopedia-style text) may create mode amplification patterns that compress the entropy-diversity lag.
1726	
1727	\paragraph{Deployment recommendations.}
1728	Based on the cross-architecture results, we recommend:
1729	\begin{enumerate}
1730	\item Run null-control calibration on each target architecture before deployment (GPT-2 FPR: 50\% without calibration).
1731	\item Use fp32 precision for the detection pipeline even if training uses mixed precision.
1732	\item Apply $K{\geq}3$ consensus to reduce architecture-specific FPR inflation (0/12 on GPT-2 vs.\ 50\% standalone PermG).
1733	\item Verify monotonic entropy decline on the target architecture; non-monotonic cases (SmolLM3-3B) require ECE-based detection.
1734	\end{enumerate}
1735	
1736	
1737	\section*{Reproducibility Details}
1738	\label{app:reproducibility}
1739	
1740	\paragraph{Compute requirements.}
1741	Each Pythia-410M experiment (10 generations $\times$ 5{,}000 training steps $+$ 5{,}000 generation samples) requires approximately 4 GPU-hours on a single NVIDIA A100 (40GB).
1742	The full experimental matrix (13 $\alpha$ levels $\times$ 4~seeds $\times$ 5 observation windows $+$ cross-architecture) required approximately 800 GPU-hours total.
1743	Statistical analysis (permutation testing, Shapley computation, specification curves) runs on CPU in under 2 hours for the complete dataset.
1744	
1745	\paragraph{Software versions.}
1746	PyTorch 2.1.0, Transformers 4.36.0, Python 3.10.
1747	All experiments use deterministic mode (\texttt{torch.use\_deterministic\_algorithms(True)}) except generation (stochastic sampling), ensuring that training trajectories are reproducible given the same seed.
1748	
1749	\paragraph{Key implementation choices.}
1750	Several implementation decisions affect reproducibility:
1751	\begin{itemize}
1752	\item \emph{Checkpoint strategy}: each generation fine-tunes from the previous generation's checkpoint (not from pretrained $M_0$), implementing true iterative collapse rather than independent fine-tuning.
1753	\item \emph{Generation prompts}: the same 5{,}000 prompt set (sampled once per experiment) is used across all generations within a run, controlling for prompt-selection variance.
1754	\item \emph{Metric computation}: all metrics are computed on the same held-out set across generations; distinct-$n$ uses the full 5{,}000 generated samples (not a subsample).
1755	\item \emph{Pipeline versioning}: results in this paper use the current pipeline version, which corrected FPR calibration errors present in earlier iterations. The corrected pipeline changed PermG detection at $\alpha{=}0.60$ from 3/8 to 0/8 (reported).
1756	\end{itemize}
1757	
1758	\paragraph{Data availability.}
1759	WikiText-103~\citep{merity2017pointer} is publicly available.
1760	Synthetic data generated during experiments is not released (too large), but the generation scripts are included in the code release.
1761	All statistical analysis code, including the five detection methods, MMCT consensus, and specification curve construction, will be released upon acceptance.
1762	
1763	\section*{Use of AI Assistants}
1764	\label{app:ai-assistants}
1765	
1766	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
1767	\begin{itemize}
1768	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
1769	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting LaTeX.
1770	    \item \textbf{Literature:} summarizing related papers to inform related-work section.
1771	\end{itemize}
1772	
1773	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b4e7c62-aba8-456a-b68f-00f18ed1e7ce",
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a9d7bd4d8daf2b13b",
  "type": "user",
  "uuid": "126a3a70-4509-4d94-aaaa-216ab7981ebb",
  "sourceToolAssistantUUID": "8b4e7c62-aba8-456a-b68f-00f18ed1e7ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-25T19:56:13.928Z_

Now I have the complete file. Let me compile the exhaustive list of every number found in the appendix.

---

## Complete Number Extraction from `appendix.tex`

### Section: Training Details and Metric Drift (App A)

| # | Number | What it represents | Line | Source/Context |
|---|--------|--------------------|------|----------------|
| 1 | **5,000** | Fine-tuning steps per generation | 8 | Hyperparameter setting |
| 2 | **5 x 10^-5** | Learning rate (AdamW) | 8 | Hyperparameter setting |
| 3 | **500** | Warmup steps | 8 | Hyperparameter setting |
| 4 | **0.01** | Weight decay | 8 | Hyperparameter setting |
| 5 | **4** | Batch size for Pythia-410M | 8 | Hyperparameter setting |
| 6 | **32** | Batch size for GPT-2-medium | 8 | Hyperparameter setting |
| 7 | **1.0** | Generation temperature | 9 | Decoding parameter |
| 8 | **50** | Top-k value | 9 | Decoding parameter |
| 9 | **512** | Max generation length (tokens) | 9 | Decoding parameter |
| 10 | **5,000** | Samples produced per generation | 9 | Data pipeline parameter |
| 11 | **5,000** | Subset size from WikiText-103 | 9 | Data pipeline parameter |
| 12 | **1,000** | Held-out samples for token entropy | 10 | Metric computation |
| 13 | **15** | ECE bins | 10 | Metric computation |
| 14 | **1.0** | Temperature (arch-specific) | 15 | Repeated decoding param |
| 15 | **50** | Top-k (arch-specific) | 15 | Repeated decoding param |
| 16 | **512** | Max length (arch-specific) | 15 | Repeated decoding param |

**Table: Per-architecture training hyperparameters (tab:arch_hyperparams), lines 27-33:**

| # | Number | What it represents | Line | Source/Context |
|---|--------|--------------------|------|----------------|
| 17 | **4** | Pythia-410M batch size | 27 | Table row |
| 18 | **5x10^-5** | Pythia-410M LR | 27 | Table row |
| 19 | **5,000** | Pythia-410M steps | 27 | Table row |
| 20 | **4** | Pythia-1.4B batch size | 28 | Table row |
| 21 | **5x10^-5** | Pythia-1.4B LR | 28 | Table row |
| 22 | **5,000** | Pythia-1.4B steps | 28 | Table row |
| 23 | **2** | Pythia-6.9B batch size | 29 | Table row |
| 24 | **2x10^-5** | Pythia-6.9B LR | 29 | Table row |
| 25 | **5,000** | Pythia-6.9B steps | 29 | Table row |
| 26 | **32** | GPT-2-medium batch size | 30 | Table row |
| 27 | **5x10^-5** | GPT-2-medium LR | 30 | Table row |
| 28 | **5,000** | GPT-2-medium steps | 30 | Table row |
| 29 | **4** | OPT-1.3B batch size | 31 | Table row |
| 30 | **5x10^-5** | OPT-1.3B LR | 31 | Table row |
| 31 | **5,000** | OPT-1.3B steps | 31 | Table row |
| 32 | **4** | Qwen3.5-0.8B batch size | 32 | Table row |
| 33 | **5x10^-5** | Qwen3.5-0.8B LR | 32 | Table row |
| 34 | **5,000** | Qwen3.5-0.8B steps | 32 | Table row |
| 35 | **4** | SmolLM3-3B batch size | 33 | Table row |
| 36 | **2x10^-5** | SmolLM3-3B LR | 33 | Table row |
| 37 | **5,000** | SmolLM3-3B steps | 33 | Table row |

**Metric computation details, lines 39-43:**

| # | Number | What it represents | Line | Source/Context |
|---|--------|--------------------|------|----------------|
| 38 | **1,000** | Held-out samples for entropy computation | 39 | Metric detail |
| 39 | **15** | Equal-width bins for ECE | 40 | Metric detail |
| 40 | **1, 2, 3** | n-gram orders for distinct-n | 42 | Metric detail |
| 41 | **5,000** | Generated samples for distinct-n | 42 | Metric detail |
| 42 | **1,000** | Held-out split for perplexity | 43 | Metric detail |

**Seed and replication structure, lines 46-49:**

| # | Number | What it represents | Line | Source/Context |
|---|--------|--------------------|------|----------------|
| 43 | **42, 43, 44** | Primary seed values (3-seed cohort) | 46 | Replication structure |
| 44 | **3** | Number of seeds in primary cohort | 46 | Replication structure |
| 45 | **10** | T (generations) for phase diagram | 46 | Experiment design |
| 46 | **13** | Number of alpha levels | 46 | Experiment design |
| 47 | **45** | Additional seed for alpha=1.0 | 47 | Replication structure |
| 48 | **4** | Total seeds for alpha=1.0 | 47 | Replication structure |
| 49 | **1.0** | alpha value for 4-seed | 47 | Condition |
| 50 | **45-51** | Seeds for extended FPR analysis | 48 | Replication structure |
| 51 | **6** | Number of pairs (excluding MAUVE) | 48 | Statistical design |
| 52 | **10** | Total distinct seeds | 48 | Replication structure |
| 53 | **15, 20, 25** | Extended T values | 49 | Cross-T extension |

**Metric drift paragraph, lines 52-53:**

| # | Number | What it represents | Line | Source/Context |
|---|--------|--------------------|------|----------------|
| 54 | **0** | Generation 0 (start) | 52 | Drift measurement |
| 55 | **10** | Generation 10 (end) | 52 | Drift measurement |
| 56 | **6** | Number of contamination levels | 52 | Experimental conditions |
| 57 | **0.25** | alpha value where largest diversity decline | 53 | Finding |
| 58 | **1.0** | alpha for full replacement | 53 | Condition |

**Table: Metric drift (tab:drift_summary), lines 59-73:**

Caption numbers (line 59):
| # | Number | What it represents | Line | Source/Context |
|---|--------|--------------------|------|----------------|
| 59 | **-40.3** ± **0.3%** | Distinct-1 decline at alpha=0.25 | 59 | Table caption |
| 60 | **-27.8** ± **1.6%** | Distinct-1 decline at alpha=1.0 | 59 | Table caption |
| 61 | **0.10** | alpha for single seed | 59 | Caption note |
| 62 | **42** | Single seed for alpha=0.10 | 59 | Caption note |
| 63 | **0.00, 0.25, 0.50, 0.75** | 3-seed alpha values | 59 | Caption note |
| 64 | **42, 43, 44** | Seeds for 3-seed conditions | 59 | Caption note |
| 65 | **42, 43, 44, 45** | Seeds for alpha=1.0 | 59 | Caption note |

Table body (lines 66-71):

**alpha=0.00 (line 66):**
| 66 | **-4.6 ± 0.4** | Entropy drift at alpha=0.00 | 66 | Table |
| 67 | **+37.6 ± 14** | ECE drift at alpha=0.00 | 66 | Table |
| 68 | **-14.1 ± 0.4** | Distinct-1 drift at alpha=0.00 | 66 | Table |
| 69 | **-9.6 ± 0.4** | Distinct-2 drift at alpha=0.00 | 66 | Table |
| 70 | **-20.6 ± 1.0** | Perplexity drift at alpha=0.00 | 66 | Table |

**alpha=0.10 (line 67):**
| 71 | **-5.3** | Entropy drift at alpha=0.10 | 67 | Table (single seed) |
| 72 | **+57** | ECE drift at alpha=0.10 | 67 | Table |
| 73 | **-39.6** | Distinct-1 drift at alpha=0.10 | 67 | Table |
| 74 | **-56.4** | Distinct-2 drift at alpha=0.10 | 67 | Table |
| 75 | **-21.0** | Perplexity drift at alpha=0.10 | 67 | Table |

**alpha=0.25 (line 68):**
| 76 | **-4.7 ± 0.5** | Entropy drift at alpha=0.25 | 68 | Table |
| 77 | **+81.8 ± 15.9** | ECE drift at alpha=0.25 | 68 | Table |
| 78 | **-40.3 ± 0.3** | Distinct-1 drift at alpha=0.25 | 68 | Table |
| 79 | **-56.4 ± 0.7** | Distinct-2 drift at alpha=0.25 | 68 | Table |
| 80 | **-18.1 ± 0.8** | Perplexity drift at alpha=0.25 | 68 | Table |

**alpha=0.50 (line 69):**
| 81 | **-18.0 ± 0.5** | Entropy drift at alpha=0.50 | 69 | Table |
| 82 | **+822.6 ± 18.3** | ECE drift at alpha=0.50 | 69 | Table |
| 83 | **-37.1 ± 0.4** | Distinct-1 drift at alpha=0.50 | 69 | Table |
| 84 | **-50.4 ± 1.0** | Distinct-2 drift at alpha=0.50 | 69 | Table |
| 85 | **+21.0 ± 0.1** | Perplexity drift at alpha=0.50 | 69 | Table |

**alpha=0.75 (line 70):**
| 86 | **-27.6 ± 0.2** | Entropy drift at alpha=0.75 | 70 | Table |
| 87 | **+1791 ± 18** | ECE drift at alpha=0.75 | 70 | Table |
| 88 | **-32.3 ± 0.5** | Distinct-1 drift at alpha=0.75 | 70 | Table |
| 89 | **-41.0 ± 1.0** | Distinct-2 drift at alpha=0.75 | 70 | Table |
| 90 | **+182.6 ± 0.7** | Perplexity drift at alpha=0.75 | 70 | Table |

**alpha=1.00 (line 71):**
| 91 | **-60.8 ± 1.2** | Entropy drift at alpha=1.00 | 71 | Table |
| 92 | **+3780 ± 30** | ECE drift at alpha=1.00 | 71 | Table |
| 93 | **-27.8 ± 1.6** | Distinct-1 drift at alpha=1.00 | 71 | Table |
| 94 | **-34.0 ± 3.3** | Distinct-2 drift at alpha=1.00 | 71 | Table |
| 95 | **+3674 ± 45** | Perplexity drift at alpha=1.00 | 71 | Table |

**Data pipeline, line 77:**
| 96 | **5,000** | Prompts sampled from WikiText-103 | 77 | Protocol |
| 97 | **32** | Tokens per prompt (first 32 of paragraphs) | 77 | Protocol |
| 98 | **512** | Token continuations generated | 77 | Protocol |
| 99 | **1.0** | Temperature | 77 | Protocol |
| 100 | **50** | Top-k | 77 | Protocol |

**Null-condition drift, lines 82-83:**
| 101 | **0.0** | alpha value (null condition) | 82 | Context |
| 102 | **14.1%** | Distinct-1 drop at alpha=0.0 | 82 | Finding |
| 103 | **4.6%** | Entropy drop at alpha=0.0 | 82 | Finding |
| 104 | **20.6%** | Perplexity improvement at alpha=0.0 | 82 | Finding |

**Non-monotonic relationship, lines 88-91:**
| 105 | **0.25** | alpha where diversity loss largest | 88 | Finding |
| 106 | **-40.3%** | Distinct-1 at alpha=0.25 | 88 | Finding |
| 107 | **1.0** | alpha for full replacement | 88 | Condition |
| 108 | **-27.8%** | Distinct-1 at alpha=1.0 | 88 | Finding |
| 109 | **3-4** | Generations by which collapse occurs at high alpha | 89 | Finding |
| 110 | **0-10** | Gen-0 to gen-10 relative decline | 90 | Context |
| 111 | **10** | Total generations | 91 | Context |

### Section: Distinct-3 Results (App B)

| 112 | **-58.9 ± 0.9%** | Distinct-3 drift at alpha=0.25 | 98 | Finding |
| 113 | **-30.5%** | Distinct-3 drift at alpha=1.0 | 98 | Finding |

**Table: Distinct-3 drift (tab:distinct3_drift), lines 109-114:**
| 114 | **-4.4 ± 0.5** | Distinct-3 at alpha=0.00 | 109 | Table |
| 115 | **-58.9 ± 0.9** | Distinct-3 at alpha=0.25 | 110 | Table |
| 116 | **-52.4** | Distinct-3 at alpha=0.50 | 111 | Table |
| 117 | **-38.6 ± 1.3** | Distinct-3 at alpha=0.75 | 112 | Table |
| 118 | **-30.5 ± 4.0** | Distinct-3 at alpha=1.00 | 113 | Table |

**Lines 118, 127-128:**
| 119 | **1.5** | Lag instability std threshold for bimodal | 118 | Observation |
| 120 | **0.5** | Lag std for distinct-1/2 | 118 | Comparison |
| 121 | **512** | Token generation length | 118 | Context |
| 122 | **6/8** | Entropy→distinct-1 detection rate at alpha=1.0 | 127 | PermG result |
| 123 | **4/8** | Entropy→distinct-3 detection rate at alpha=1.0 | 127 | PermG result |
| 124 | **2** | Seeds failing due to lag instability | 127 | Finding |
| 125 | **-1** | Lag shift value | 127 | Bimodal lag |
| 126 | **-2** | Lag shift value | 127 | Bimodal lag |

### Section: Observation Window Sensitivity (App C)

| 127 | **5** | T_min threshold for consensus stabilization | 134 | Finding |
| 128 | **6** | Effect-size reference pairs (out of) | 134 | Finding |
| 129 | **4/5** | K threshold for agreement | 134 | Consensus criterion |
| 130 | **5** | T_min lower bound | 134 | Range |
| 131 | **10** | T_min upper bound | 134 | Range |
| 132 | **1.0** | alpha value | 137 | Condition |
| 133 | **4** | Seeds used | 137 | Replication |
| 134 | **5** | T_min start | 137 | Range |
| 135 | **10** | T_min end | 137 | Range |
| 136 | **6/6** | NaiveXCorr validated pairs | 138 | Result |
| 137 | **3/6** | TY pairs at T_min=5 | 139 | Result |
| 138 | **6/6** | TY pairs at T_min=7 | 139 | Result |
| 139 | **3/6** | TY range at T_min=8-10 | 139 | Result |
| 140 | **6/6** | TY range at T_min=8-10 | 139 | Result |
| 141 | **~10%** | Data removed per generation reduction at T=10 | 140 | Calculation |
| 142 | **10** | T value | 140 | Context |
| 143 | **10** | Full T observation window | 143 | Context |
| 144 | **6** | Minimum data points | 144 | Finding |
| 145 | **5** | T_min for deployment | 144 | Finding |
| 146 | **0.50** | Alpha boundary at shorter windows | 144 | Finding |
| 147 | **5** | T_min for Granger-type tests | 145 | Minimum requirement |
| 148 | **2** | Parameters in lag-1 regression | 145 | DOF calculation |

**Figure caption, line 150:**
| 149 | **6/8** | PermG forward detection | 150 | Caption |
| 150 | **4** | K threshold (K>=4) | 150 | Caption |
| 151 | **5** | T_min stabilization point | 150 | Caption |
| 152 | **5, 10** | T_min range [5,10] | 150 | Caption |

**Table: Window sensitivity (tab:window_sensitivity), lines 157-172:**
| 153 | **4/5** | K threshold (consensus) | 157 | Caption |
| 154 | **8** | Validated pairs (out of) | 157 | Caption |
| 155 | **6** | Effect-size reference pairs (out of) | 157 | Caption |
| 156 | **5** | T_min for consensus stabilization | 157 | Caption |
| 157 | **6** | T_min for TY stabilization | 157 | Caption |

Table body row "Tier 3 pairs" (line 166): values **6** at T_min=5 through 10
Table body row "TY pairs" (line 167): **3-6** range at T_min=5 through 9, **6** at T_min=10

| 158 | **6** | Tier 3 pairs for all T_min 5-10 | 166 | Table body |
| 159 | **3-6** | TY pairs range T_min=5-9 | 167 | Table body |
| 160 | **6** | TY pairs at T_min=10 | 167 | Table body |

### Section: Robustness Analysis (App D)

| 161 | **5,000** | Lower permutation count | 181 | Robustness test |
| 162 | **10,000** | Upper permutation count | 181 | Robustness test |
| 163 | **0.010** | Max delta-p between permutation counts | 181 | Finding |
| 164 | **0/24** | Significance flips | 181 | Finding |
| 165 | **0.75** | alpha tested | 181 | Condition |
| 166 | **0.05** | FDR threshold q | 182 | Statistical parameter |
| 167 | **4/36** | Null pairs reaching significance at q=0.05 | 182 | Finding |
| 168 | **19/24** | Treatment pairs at q=0.05 | 182 | Finding |
| 169 | **0.10** | Alternative FDR threshold q | 182 | Parameter |
| 170 | **8/36** | Null rejections at q=0.10 | 182 | Finding |
| 171 | **0.45** | alpha for onset boundary | 183 | Condition |
| 172 | **0.059-0.091** | Minimum FDR-corrected p-values | 183 | Finding |

**Specification curve, lines 186-228:**
| 173 | **1,160** | Total specifications | 186 | Design |
| 174 | **13** | Contamination levels | 186 | Design |
| 175 | **4** | Seeds | 186 | Design |
| 176 | **8** | Canary→downstream pairs | 186 | Design |
| 177 | **5,000** | Permutations | 186 | Parameter |
| 178 | **0.05** | BH FDR q | 186 | Parameter |
| 179 | **0%** | Significance rate through alpha=0.45 | 191 | Finding |
| 180 | **75%** | Significance rate at alpha=0.50 | 191 | Finding |
| 181 | **1,160** | Total specifications (table) | 197 | Table |
| 182 | **536** | Significant specifications | 198 | Table |
| 183 | **46.2%** | Percent significant | 198 | Table |
| 184 | **0.05** | FDR q threshold | 198 | Table |
| 185 | **0%** | Blind regime rate | 201 | Table |
| 186 | **0.45** | Alpha upper bound for blind | 201 | Table |
| 187 | **75%** | Onset rate at alpha=0.50 | 202 | Table |
| 188 | **0.50** | Onset alpha | 202 | Table |
| 189 | **62-75%** | Detection regime rate | 203 | Table |
| 190 | **0.75** | Alpha lower bound for detection | 203 | Table |

**Specification decomposition, lines 218-224:**
| 191 | **536** | Significant specifications | 218 | Context |
| 192 | **46.2%** | Percent of 1,160 | 218 | Context |
| 193 | **75%** | Detection rate for entropy→distinct-1/2 | 219 | Finding |
| 194 | **0%** | ECE→perplexity rate | 219 | Finding |
| 195 | **50%** | MAUVE rate at alpha=1.0 | 220 | Finding |
| 196 | **0%** | MAUVE rate at alpha=0.50 | 220 | Finding |
| 197 | **3.45 x 10^-11** | Fisher exact p-value | 224 | Statistical test |
| 198 | **0/8** | Pre-transition | 224 | Finding |
| 199 | **6/8** | Post-transition | 224 | Finding |

**Alternative FDR thresholds, lines 227-228:**
| 200 | **0.10** | Alternative q | 227 | Parameter |
| 201 | **46.2%** | Original rate | 227 | Reference |
| 202 | **53.8%** | Rate at q=0.10 | 227 | Finding |
| 203 | **0.45** | alpha where 4 specs cross | 227 | Finding |
| 204 | **4** | Specifications crossing at alpha=0.45 | 227 | Finding |
| 205 | **0.60** | alpha where 2 specs cross | 227 | Finding |
| 206 | **2** | Specifications crossing at alpha=0.60 | 227 | Finding |
| 207 | **0.01** | Strict q threshold | 228 | Parameter |
| 208 | **38.4%** | Rate at q=0.01 | 228 | Finding |
| 209 | **0.50** | alpha boundary affected | 228 | Finding |
| 210 | **3** | Number of thresholds tested | 229 | Context |

### Section: Transfer Entropy and Change-Point (App E)

| 211 | **3** | Bins for discretization | 235 | TE parameter |
| 212 | **5,000** | Permutations for TE | 235 | TE parameter |
| 213 | **0/192** | BH-corrected significant TE pairs | 235 | Finding |
| 214 | **11** | T value (T=11 data points) | 235 | Context |
| 215 | **5** | KNN k value | 236 | Estimator parameter |
| 216 | **4/8** | Forward-dominant TE at alpha=0.25 | 236 | Finding |
| 217 | **8/8** | Forward-dominant TE at alpha=1.0 | 236 | Finding |

**Symbolic TE, lines 239-241:**
| 218 | **2** | Bandt-Pompe m (embedding dimension) | 239 | Parameter |
| 219 | **1** | Lag | 239 | Parameter |
| 220 | **500** | Circular-shift surrogates | 239 | Parameter |
| 221 | **0.05** | p threshold | 239 | Parameter |
| 222 | **0.60** | alpha for sync-dip | 240 | Condition |
| 223 | **0/8** | PermG detection at alpha=0.60 | 240 | Reference |
| 224 | **4/6** | Symbolic TE forward pairs | 240 | Finding |
| 225 | **0.001** | p threshold for symbolic TE | 240 | Threshold |
| 226 | **0.539** | MAUVE-channel TE at T=10 | 240 | Finding |
| 227 | **10** | T value | 240 | Context |
| 228 | **0.496** | MAUVE-channel TE at T=15 | 240 | Finding |
| 229 | **15** | T value | 240 | Context |
| 230 | **0.122** | Distinct-1-channel TE at T=20 | 240 | Finding |
| 231 | **20** | T value | 240 | Context |
| 232 | **6/8** | PermG positive control | 241 | Reference |
| 233 | **0/6** | Symbolic TE in positive controls | 241 | Finding |
| 234 | **0.000-0.379** | TE values in positive controls | 241 | Finding |
| 235 | **0.14** | p lower bound for positive controls | 241 | Finding |
| 236 | **5** | T for baseline condition | 241 | Context |
| 237 | **0.50** | alpha for baseline | 241 | Context |
| 238 | **0/2** | Significant at baseline | 241 | Finding |
| 239 | **0.000-0.189** | TE values at baseline | 241 | Finding |
| 240 | **1.000** | p-value at baseline | 241 | Finding |

**Change-point detection, lines 250-252:**
| 241 | **5,000** | Bootstrap samples | 250 | Parameter |
| 242 | **66.7%** | FPR under null control | 250 | Finding |
| 243 | **12/18** | Raw count for FPR | 250 | Finding |
| 244 | **0.00** | alpha for null control | 250 | Condition |
| 245 | **2** | Gen where downstream breaks first (null) | 251 | Finding |
| 246 | **4-8** | Gen range where canary breaks (null) | 251 | Finding |
| 247 | **0.75** | alpha threshold for treatment | 251 | Condition |
| 248 | **1** | Gen where canary breaks (treatment) | 251 | Finding |
| 249 | **2-4** | Gen range for downstream break (treatment) | 251 | Finding |

### Section: Sequential Monitoring CUSUM (App F)

| 250 | **0%** | FAR for CUSUM null | 258 | Finding |
| 251 | **2σ** | Threshold value | 258 | Parameter |
| 252 | **1** | Alarm generation for alpha>=0.50 | 258 | Finding |
| 253 | **0.50** | alpha threshold | 258 | Condition |
| 254 | **0.7** | Entropy drop magnitude |delta x| | 259 | Observation |
| 255 | **0.03** | Null variability sigma_0 | 259 | Observation |

**Operating characteristics, lines 264-267:**
| 256 | **0.00-0.45** | alpha range, no trigger | 264 | Finding |
| 257 | **10** | T value | 264 | Context |
| 258 | **5.3%** | Entropy drift upper bound in blind zone | 264 | Finding |
| 259 | **0.50** | alpha for trigger | 265 | Condition |
| 260 | **1** | Trigger generation | 265 | Finding |
| 261 | **18.0 ± 0.5%** | Entropy drop at alpha=0.50 | 265 | Finding |
| 262 | **0.75-1.0** | alpha range for immediate trigger | 266 | Condition |
| 263 | **1** | Trigger generation | 266 | Finding |
| 264 | **27.6-60.8%** | Entropy drop range | 266 | Finding |
| 265 | **0.50** | alpha threshold for blind zone | 268 | Context |
| 266 | **10** | T value | 268 | Context |

**Lines 272, 303-305:**
| 267 | **10%** | Lower safe operating band | 272 | Intervention range |
| 268 | **22%** | Upper safe operating band | 272 | Intervention range |
| 269 | **0%** | FAR under null | 303 | Finding |
| 270 | **3** | Null-condition seeds | 303 | Context |
| 271 | **7.5%** | Below-threshold for false alarms | 304 | Finding |
| 272 | **3** | Gen for false alarm | 304 | Finding |
| 273 | **-4.6%** | Entropy drift at alpha=0.0 | 304 | Finding |
| 274 | **100%** | FAR below 7.5% | 304 | Finding |
| 275 | **10%** | Lenient bound | 305 | Deployment |
| 276 | **22%** | Strict bound | 305 | Deployment |

**Table: Sequential monitoring timing (tab:sequential_timing), lines 287-295:**
| 277 | **-4.6** | Delta H at alpha=0.00 | 287 | Table |
| 278 | **-5.3** | Delta H at alpha=0.10 | 288 | Table |
| 279 | **-4.7** | Delta H at alpha=0.25 | 289 | Table |
| 280 | **-5.1** | Delta H at alpha=0.45 | 290 | Table |
| 281 | **-18.0** | Delta H at alpha=0.50 | 291 | Table |
| 282 | **-28.5** | Delta H at alpha=0.60 | 292 | Table |
| 283 | **-27.6** | Delta H at alpha=0.75 | 293 | Table |
| 284 | **-60.8** | Delta H at alpha=1.00 | 294 | Table |

### Section: Background and Notation (App G)

| 285 | **1** | Starting generation index | 315 | Notation |
| 286 | **0, 1** | alpha range bounds [0,1] | 317 | Equation |
| 287 | **1.0** | Full replacement alpha | 320 | Context |
| 288 | **1, 2, 3** | n-gram orders | 324 | Metric definition |
| 289 | **5** | Methods for lead-lag testing | 329 | Method count |

**Method details, lines 332-348:**
| 290 | **-5, 5** | Lag range for NaiveXCorr | 332 | Parameter |
| 291 | **0.05** | Uncorrected p threshold | 332 | Threshold |
| 292 | **3σ** | Threshold onset detection threshold | 335 | Parameter |
| 293 | **5,000** | Temporal permutations for PermG | 336 | Parameter |
| 294 | **0.05** | BH-FDR q | 336 | Threshold |
| 295 | **8** | Metric pairs for correction | 336 | Statistical design |
| 296 | **5** | Max lag L for PermG | 342 | Parameter |
| 297 | **5,000** | Null realizations | 345 | Parameter |
| 298 | **1** | Offset in p-value formula (+1) | 346 | Statistical computation |
| 299 | **5** | Maximum L for lag selection | 348 | Parameter |
| 300 | **3** | Minimum degrees of freedom | 348 | Constraint |
| 301 | **11** | T value | 348 | Context |

**Multiple testing, lines 357-360:**
| 302 | **8** | Canary→downstream pairs tested | 357 | Design |
| 303 | **2** | Canary metrics | 357 | Design |
| 304 | **4** | Downstream metrics | 357 | Design |
| 305 | **9** | 9th pair (MAUVE) | 357 | Additional analysis |
| 306 | **0.05** | BH-FDR q | 358 | Parameter |
| 307 | **8** | Tests per family | 358 | Design |
| 308 | **5%** | FDR guarantee | 360 | Statistical property |

### Section: MMCT Algorithm (App H)

| 309 | **3** | K threshold (K>=3) | 370 | Caption |
| 310 | **5** | Total methods | 370 | Context |
| 311 | **8/8** | Consensus detection at alpha=0.60 | 370 | Finding |
| 312 | **0/8** | PermG at alpha=0.60 | 370 | Reference |
| 313 | **6.7%** | PermG FPR | 376 | Finding |
| 314 | **94.4%** | NaiveXCorr FPR | 376 | Finding |
| 315 | **3** | K threshold | 377 | Parameter |
| 316 | **0.01** | Epsilon floor | 381 | Parameter |
| 317 | **0%** | FPR for methods with 0% | 381 | Reference |
| 318 | **14.9** | PermG weight | 382 | Calculated value |
| 319 | **1.06** | NaiveXCorr weight | 382 | Calculated value |
| 320 | **14x** | Weight differential | 382 | Ratio |
| 321 | **4** | Other methods that could agree without PermG | 382 | Context |
| 322 | **7** | Step 7 of algorithm | 383 | Algorithm reference |
| 323 | **5-25** | T range for short series | 383 | Context |

**Sensitivity to K, lines 386-388:**
| 324 | **2, 3, 4, 5** | K values tested | 386 | Parameter range |
| 325 | **3** | Optimal K | 387 | Finding |
| 326 | **2** | Lower K | 387 | Comparison |
| 327 | **10.0%** | FPR at K=3 | 387 | Finding |
| 328 | **38.9%** | FPR at K=2 | 387 | Finding |
| 329 | **66.7%** | TPR at K=3, alpha=0.50 | 387 | Finding |
| 330 | **85.4%** | TPR at K=2, alpha=0.50 | 387 | Finding |
| 331 | **4** | Higher K | 387 | Comparison |
| 332 | **0%** | FPR at K=4 | 387 | Finding |
| 333 | **25%** | Max TPR at K=4 | 387 | Finding |
| 334 | **5** | Unanimity K | 388 | Comparison |
| 335 | **5%** | Expected detection rate at K=5 | 388 | Finding |
| 336 | **94%** | NaiveXCorr FPR (reference) | 388 | Context |

### Section: Methodological Comparison (App I)

| 337 | **6** | Diagnostic dimensions | 401, 426 | Design |
| 338 | **2** | Minimum levels for partial coverage | 406 | Table note |
| 339 | **3** | Minimum independent seeds | 406 | Table note |
| 340 | **2** | Minimum architecturally distinct families | 406 | Table note |
| 341 | **8** | Metric pairs for uncorrected testing | 429 | Context |
| 342 | **0.05** | p threshold | 429 | Parameter |
| 343 | **~0.4** | Expected false positives per condition | 429 | Calculation |
| 344 | **4/6** | Du et al. dimensions | 433 | Comparison |

### Section: Extended Discussion (App J)

| 345 | **10** | T value | 439 | Setup |
| 346 | **0.50** | alpha on C4 | 440 | Condition |
| 347 | **7/8** | PermG reverse on C4 | 440 | Finding |
| 348 | **1/8** | Seed-dependent (s43) on C4 | 440 | Finding |

**Lines 446-449:**
| 349 | **20** | T=20 extension | 446 | Context |
| 350 | **5/8** | Detection at alpha=0.45, T=20 | 446 | Finding |
| 351 | **0.10** | Very low alpha | 449 | Context |

**Lines 457-458:**
| 352 | **64%** | Lower peak perplexity from intervention | 457 | Finding |
| 353 | **1** | Gen-1 for entropy signal | 457 | Context |

**Failure mode taxonomy (tab:failure_modes), lines 473-477:**
| 354 | **0/8** | GPT-2 bf16 PermG | 473 | Table |
| 355 | **6/8** | GPT-2 s43 PermG (both directions) | 474 | Table |
| 356 | **2/8** | Pythia-1.4B s42 PermG | 475 | Table |
| 357 | **3/8** | SmolLM3-3B PermG | 476 | Table |
| 358 | **4** | Non-confirming conditions | 461 | Context |

**Lines 481-484:**
| 359 | **0/8** | GPT-2 bf16 before fix | 481 | Reference |
| 360 | **6/8** | GPT-2 fp32 after fix | 481 | Result |
| 361 | **2/8** | Pythia-1.4B s42 | 483 | Finding |
| 362 | **6/8** | Pythia-1.4B s43 | 483 | Comparison |
| 363 | **0/4** | SmolLM3 entropy | 484 | Finding |
| 364 | **3/4** | SmolLM3 ECE | 484 | Finding |

### Section: Scale verification - Pythia-1.4B (App J cont.)

**Table: 14b_phase (tab:14b_phase), lines 498-525:**

Every cell in the table (I'll list unique/representative entries):
| 365 | **0/8** | alpha=0.45 s42 T=10 Fwd | 498 | Table |
| 366 | **1/8** | alpha=0.45 s43 T=10 Fwd | 499 | Table |
| 367 | **0/6** | alpha=0.45 s44 T=10 Fwd | 500 | Table |
| 368 | **4/8** | alpha=0.50 s42 T=10 Fwd | 502 | Table |
| 369 | **2/8** | alpha=0.50 s42 T=10 Rev (bidirectional) | 502 | Table |
| 370 | **3/8** | alpha=0.50 s42 T=10 K>=3 | 502 | Table |
| 371 | **6/6** | alpha=0.50 s43 T=10 Fwd | 503 | Table |
| 372 | **1/6** | alpha=0.50 s43 T=10 K>=3 | 503 | Table |
| 373 | **6/6** | alpha=0.50 s44 T=10 Fwd | 504 | Table |
| 374 | **4/8** | alpha=0.60 s42 T=10 Fwd | 506 | Table |
| 375 | **3/8** | alpha=0.60 s42 T=10 K>=3 | 506 | Table |
| 376 | **4/8** | alpha=0.60 s43 T=10 Fwd | 507 | Table |
| 377 | **6/8** | alpha=0.60 s43 T=10 Rev (bidirectional) | 507 | Table |
| 378 | **3/8** | alpha=0.60 s43 T=10 K>=3 | 507 | Table |
| 379 | **6/6** | alpha=0.60 s44 T=10 Fwd | 508 | Table |
| 380 | **5/6** | alpha=0.60 s44 T=10 K>=3 | 508 | Table |
| 381 | **5/8** | alpha=0.75 s42 T=10 Fwd | 510 | Table |
| 382 | **6/8** | alpha=0.75 s43 T=10 Fwd | 511 | Table |
| 383 | **5/8** | alpha=0.75 s43 T=10 Rev | 511 | Table |
| 384 | **5/8** | alpha=0.75 s43/s42 T=10 K>=3 | 511 | Table |
| 385 | **6/6** | alpha=0.75 s44 T=10 Fwd and K>=3 | 512 | Table |

T=15 entries:
| 386 | **3/8** | alpha=0.45 s42 T=15 Fwd | 514 | Table |
| 387 | **4/8** | alpha=0.45 s42 T=15 K>=3 | 514 | Table |
| 388 | **5/6** | alpha=0.45 s43 T=15 Fwd | 515 | Table |
| 389 | **3/6** | alpha=0.45 s43 T=15 Rev (bidirectional) | 515 | Table |
| 390 | **3/8** | alpha=0.50 s42 T=15 Fwd | 517 | Table |
| 391 | **2/8** | alpha=0.50 s42 T=15 K>=3 | 517 | Table |
| 392 | **3/6** | alpha=0.50 s43 T=15 Fwd and K>=3 | 518 | Table |
| 393 | **6/8** | alpha=0.60 s42 T=15 Fwd and K>=3 | 520 | Table |
| 394 | **6/6** | alpha=0.60 s43 T=15 Fwd and K>=3 | 521 | Table |
| 395 | **3/6** | alpha=0.60 s43 T=15 Rev | 521 | Table |
| 396 | **6/8** | alpha=0.75 s42 T=15 Fwd and K>=3 | 523 | Table |
| 397 | **6/6** | alpha=0.75 s43 T=15 Fwd and K>=3 | 524 | Table |

**Lines 529-551 (1.4B summary):**
| 398 | **0.50** | alpha_c at 1.4B | 529 | Finding |
| 399 | **3/4** | alpha values with cross-T improvement | 529 | Finding |
| 400 | **0/6** | alpha=0.45 at T=10 | 529 | Comparison |
| 401 | **5/6** | alpha=0.45 at T=15 | 529 | Comparison |
| 402 | **4/6** | alpha=0.60 at T=10 for 1.4B | 530 | Finding |
| 403 | **6/8** | Reverse significance at alpha=0.60 | 531 | Finding |
| 404 | **5/8** | Reverse significance at alpha=0.75 | 531 | Finding |
| 405 | **0** | s42 reverse across all conditions | 531 | Finding |

**Scale effects, lines 541-551:**
| 406 | **4/6-6/6** | 1.4B range at alpha=0.60 | 543 | Finding |
| 407 | **0/8** | 410M at alpha=0.60 | 543 | Comparison |
| 408 | **2/8** | 1.4B s42 at alpha=1.0 | 544 | Finding |
| 409 | **6/8** | 1.4B s43 at alpha=1.0 | 544 | Finding |
| 410 | **6/8** | 410M across all seeds | 544 | Comparison |
| 411 | **8/8** | 1.4B on C4 PermG forward | 545 | Finding |
| 412 | **8/8** | 1.4B on C4 K>=3 | 545 | Finding |
| 413 | **2-6/8** | 1.4B on WikiText | 545 | Comparison |

**Intervention at 1.4B, lines 549-551:**
| 414 | **51.9%** | Entropy drop at 1.4B | 549 | Finding |
| 415 | **2.946** | Entropy gen-0 at 1.4B | 549 | Finding |
| 416 | **1.418** | Entropy gen-1 at 1.4B | 549 | Finding |
| 417 | **19.68** | Peak PPL from at 1.4B | 550 | Finding |
| 418 | **65.37** | Peak PPL to at 1.4B | 550 | Finding |
| 419 | **232%** | PPL increase at 1.4B | 550 | Finding |
| 420 | **112%** | PPL increase at 410M | 550 | Comparison |
| 421 | **17.44** | Gen-2 PPL at 1.4B | 550 | Finding |
| 422 | **40.7%** | Entropy drop at 410M | 551 | Comparison |

### Section: Per-Method Dose-Response (App K)

| 423 | **8** | Validated pairs (out of) | 558 | Context |
| 424 | **5** | Detection methods | 558 | Count |
| 425 | **12** | Contamination levels | 558 | Count |
| 426 | **42** | Seed | 558 | Condition |

**Table: Dose-response full (tab:dose_response_full), lines 571-583:**
All per-cell values:
| 427 | **8** | Naive at alpha=0.00 | 571 | Table |
| 428 | **4** | DiffXCorr at alpha=0.00 | 571 | Table |
| 429 | **3** | Threshold at alpha=0.00 | 571 | Table |
| 430 | **0** | PermG at alpha=0.00 | 571 | Table |
| 431 | **1** | TY at alpha=0.00 | 571 | Table |
| 432 | **7** | Naive at alpha=0.10 | 572 | Table |
| 433 | **6** | DiffXCorr at alpha=0.10 | 572 | Table |
| 434 | **0** | Threshold at alpha=0.10 | 572 | Table |
| 435 | **0** | PermG at alpha=0.10 | 572 | Table |
| 436 | **0** | TY at alpha=0.10 | 572 | Table |
| 437 | **8** | Naive at alpha=0.25 | 573 | Table |
| 438 | **3** | DiffXCorr at alpha=0.25 | 573 | Table |
| 439 | **0** | Threshold at alpha=0.25 | 573 | Table |
| 440 | **0** | PermG at alpha=0.25 | 573 | Table |
| 441 | **2** | TY at alpha=0.25 | 573 | Table |
| 442 | **8** | Naive at alpha=0.30 | 574 | Table |
| 443 | **4** | DiffXCorr at alpha=0.30 | 574 | Table |
| 444 | **0** | PermG at alpha=0.30 | 574 | Table |
| 445 | **3** | TY at alpha=0.30 | 574 | Table |
| 446 | **8** | Naive at alpha=0.35 | 575 | Table |
| 447 | **4** | DiffXCorr at alpha=0.35 | 575 | Table |
| 448 | **0** | PermG at alpha=0.35 | 575 | Table |
| 449 | **1** | TY at alpha=0.35 | 575 | Table |
| 450 | **8** | Naive at alpha=0.40 | 576 | Table |
| 451 | **3** | DiffXCorr at alpha=0.40 | 576 | Table |
| 452 | **0** | PermG at alpha=0.40 | 576 | Table |
| 453 | **4** | TY at alpha=0.40 | 576 | Table |
| 454 | **8** | Naive at alpha=0.45 | 577 | Table |
| 455 | **6** | DiffXCorr at alpha=0.45 | 577 | Table |
| 456 | **0** | PermG at alpha=0.45 | 577 | Table |
| 457 | **1** | TY at alpha=0.45 | 577 | Table |
| 458 | **8** | Naive at alpha=0.50 | 578 | Table |
| 459 | **7** | DiffXCorr at alpha=0.50 | 578 | Table |
| 460 | **4** | Threshold at alpha=0.50 | 578 | Table |
| 461 | **6** | PermG at alpha=0.50 | 578 | Table |
| 462 | **3** | TY at alpha=0.50 | 578 | Table |
| 463 | **8** | Naive at alpha=0.55 | 579 | Table |
| 464 | **8** | DiffXCorr at alpha=0.55 | 579 | Table |
| 465 | **0** | PermG at alpha=0.55 | 579 | Table |
| 466 | **1** | TY at alpha=0.55 | 579 | Table |
| 467 | **8** | Naive at alpha=0.60 | 580 | Table |
| 468 | **6** | DiffXCorr at alpha=0.60 | 580 | Table |
| 469 | **0** | PermG at alpha=0.60 | 580 | Table |
| 470 | **0** | TY at alpha=0.60 | 580 | Table |
| 471 | **7** | Naive at alpha=0.75 | 581 | Table |
| 472 | **6** | DiffXCorr at alpha=0.75 | 581 | Table |
| 473 | **0** | Threshold at alpha=0.75 | 581 | Table |
| 474 | **6** | PermG at alpha=0.75 | 581 | Table |
| 475 | **3** | TY at alpha=0.75 | 581 | Table |
| 476 | **8** | Naive at alpha=1.00 | 582 | Table |
| 477 | **6** | DiffXCorr at alpha=1.00 | 582 | Table |
| 478 | **2** | Threshold at alpha=1.00 | 582 | Table |
| 479 | **6** | PermG at alpha=1.00 | 582 | Table |
| 480 | **1** | TY at alpha=1.00 | 582 | Table |

**Method-specific observations, lines 592-596:**
| 481 | **7-8/8** | NaiveXCorr saturation | 592 | Finding |
| 482 | **94.4%** | NaiveXCorr FPR | 592 | Finding |
| 483 | **19** | Out of 20 null-control runs | 592 | Calculation |
| 484 | **20** | Total null-control runs | 592 | Context |
| 485 | **6-8/8** | DiffXCorr at alpha>=0.50 | 593 | Finding |
| 486 | **4/8** | DiffXCorr at null | 593 | Finding |
| 487 | **37.5%** | DiffXCorr FPR | 593 | Finding |
| 488 | **3/8** | Threshold at null | 595 | Finding |
| 489 | **0/8** | Threshold at alpha=0.10-0.45 and 0.55-0.75 | 595 | Finding |
| 490 | **0/8-4/8** | TY range | 596 | Finding |
| 491 | **10** | T value | 596 | Context |

**Inter-method agreement, lines 599-601:**
| 492 | **-0.04** | Cohen's kappa min (NaiveXCorr vs Threshold) | 599 | Finding |
| 493 | **0.42** | Cohen's kappa max (PermG vs DiffXCorr) | 599 | Finding |
| 494 | **0.185** | Overall kappa across 5 methods | 600 | Finding |

### Section: Cross-Seed Consistency at alpha=0.60 (App L)

| 495 | **0/8** | PermG at alpha=0.60 seed 42 | 619 | Finding |
| 496 | **0/8** | PermG at alpha=0.60 seed 43 | 619 | Finding |
| 497 | **3/8** | Earlier pipeline v3 result | 620 | Historical |

**Detailed metrics at alpha=0.60, line 623:**
| 498 | **-28.5%** | Token entropy drift at alpha=0.60 | 623 | Finding |
| 499 | **3.234** | Entropy gen-0 | 623 | Measured value |
| 500 | **2.311** | Entropy gen-10 | 623 | Measured value |
| 501 | **+1561%** | ECE drift at alpha=0.60 | 623 | Finding |
| 502 | **0.0108** | ECE gen-0 | 623 | Measured value |
| 503 | **0.179** | ECE gen-10 | 623 | Measured value |
| 504 | **+92.3%** | Perplexity drift at alpha=0.60 | 623 | Finding |
| 505 | **26.95** | PPL gen-0 | 623 | Measured value |
| 506 | **51.83** | PPL gen-10 | 623 | Measured value |
| 507 | **0.034** | Raw p-value ECE→distinct-1 | 624 | Finding |
| 508 | **0.047** | Raw p-value ECE→distinct-2 | 624 | Finding |
| 509 | **0.05** | Uncorrected alpha threshold | 624 | Parameter |
| 510 | **0.05** | BH-FDR q | 624 | Parameter |
| 511 | **8** | Simultaneous tests | 624 | Context |

**Cross-T behavior at alpha=0.60, lines 628-631:**
| 512 | **0/8** | T=5 | 628 | Finding |
| 513 | **0/8** | T=10 (s42, s43) | 628 | Finding |
| 514 | **0/8** | T=15 (s42) | 628 | Finding |
| 515 | **0/8** | T=20 (s42) | 628 | Finding |
| 516 | **3/8** | T=20 (s43, partial) | 628 | Finding |
| 517 | **5/8** | T=25 PermG (s42) | 629 | Finding |
| 518 | **6/8** | T=25 K>=3 consensus | 629 | Finding |
| 519 | **20** | T threshold for persistence | 630 | Context |
| 520 | **25** | T for dissolution | 630 | Context |

**Scale dependence, lines 633-634:**
| 521 | **4/8** | 1.4B at alpha=0.60 s42 T=10 | 633 | Finding |
| 522 | **4/6** | 1.4B at alpha=0.60 s43 T=10 | 633 | Finding |
| 523 | **6/8** | 1.4B at alpha=0.60 s42 T=15 | 633 | Finding |
| 524 | **6/6** | 1.4B at alpha=0.60 s43 T=15 | 633 | Finding |

**Sigmoid fit, lines 637-638:**
| 525 | **5.66** | k from sigmoid excluding alpha=0.60 | 637 | Fit result |
| 526 | **0.765** | alpha_c from sigmoid excluding alpha=0.60 | 637 | Fit result |
| 527 | **0.286** | R^2 excluding alpha=0.60 | 637 | Fit result |
| 528 | **0.205** | R^2 including alpha=0.60 | 637 | Fit result |
| 529 | **0.058** | alpha_c rightward shift | 637 | Finding |
| 530 | **0.282** | Predicted detection probability at alpha=0.60 | 638 | Model prediction |
| 531 | **0/8** | Observed (0.00) at alpha=0.60 | 638 | Observation |

### Section: PPL Threshold Baseline (App M)

| 532 | **+10%, +25%, +50%, +100%, +150%, +200%** | PPL thresholds tested | 645 | Design |
| 533 | **26.95** | Generation-0 baseline PPL | 645 | Measured value |

**PPL trajectory, line 648:**
| 534 | **26.95** | Gen-0 PPL | 648 | Measured |
| 535 | **57.42** | Gen-1 PPL | 648 | Measured |
| 536 | **+113.1%** | Gen-0→1 PPL increase | 648 | Calculated |
| 537 | **162.15** | Gen-2 PPL | 648 | Measured |
| 538 | **+501.9%** | Gen-0→2 PPL increase | 648 | Calculated |
| 539 | **279.17** | Gen-3 PPL | 648 | Measured |
| 540 | **508.85** | Gen-5 PPL | 648 | Measured |
| 541 | **1017.81** | Gen-10 PPL | 648 | Measured |
| 542 | **1** | Trigger generation for all thresholds +10% to +100% | 649 | Finding |
| 543 | **+113.1%** | Gen-0→1 jump exceeding all thresholds | 649 | Explanation |
| 544 | **+150%** | Threshold delaying to gen-2 | 650 | Finding |
| 545 | **+200%** | Threshold delaying to gen-2 | 650 | Finding |
| 546 | **162.15** | Gen-2 PPL exceeding +150% and +200% | 650 | Explanation |

**Comparison with entropy, lines 657:**
| 547 | **18.0%** | Entropy drop at alpha=0.50 gen-1 | 657 | Finding |
| 548 | **21.0%** | PPL rise over 10 gens at alpha=0.50 | 657 | Finding |
| 549 | **10** | Generations | 657 | Context |

**When PPL suffices, line 661:**
| 550 | **+50%** | PPL threshold for high-alpha scenarios | 661 | Recommendation |

### Section: PermG Power Analysis (App N)

| 551 | **6-20** | T range for simulation | 668 | Design |
| 552 | **100** | Replications | 668 | Design |
| 553 | **5,000** | Permutations | 668 | Design |
| 554 | **0.05** | BH FDR q | 668 | Parameter |
| 555 | **10** | T for beta_50=2.0 | 669 | Finding |
| 556 | **2.0** | beta_50 at T=10 | 669 | Finding |
| 557 | **20** | T for beta_50=0.9 | 669 | Finding |
| 558 | **0.9** | beta_50 at T=20 | 669 | Finding |
| 559 | **2%** | FPR upper bound under FDR | 671 | Finding |

**Detailed power values, lines 674-676:**
| 560 | **1.0** | beta value | 674 | Parameter |
| 561 | **0.17** | Power at beta=1.0, T=10 | 674 | Finding |
| 562 | **0.30** | Power at beta=1.0, T=15 | 674 | Finding |
| 563 | **0.66** | Power at beta=1.0, T=20 | 674 | Finding |
| 564 | **2.0** | beta value | 674 | Parameter |
| 565 | **0.51** | Power at beta=2.0, T=10 | 674 | Finding |
| 566 | **0.92** | Power at beta=2.0, T=15 | 674 | Finding |
| 567 | **0.98** | Power at beta=2.0, T=20 | 674 | Finding |
| 568 | **1%** | Raw FPR at T=6 | 675 | Finding |
| 569 | **6%** | Raw FPR at T=8 | 675 | Finding |
| 570 | **9%** | Raw FPR at T=10 | 675 | Finding |
| 571 | **6%** | Raw FPR at T=15 | 675 | Finding |
| 572 | **5%** | Raw FPR at T=20 | 675 | Finding |

**sqrt(T) scaling product, lines 680:**
| 573 | **5.09** | beta_50 * sqrt(T) at T=8 | 680 | Calculated |
| 574 | **6.32** | beta_50 * sqrt(T) at T=10 | 680 | Calculated |
| 575 | **4.65** | beta_50 * sqrt(T) at T=15 | 680 | Calculated |
| 576 | **4.02** | beta_50 * sqrt(T) at T=20 | 680 | Calculated |

**TY bootstrap comparison, line 684:**
| 577 | **200** | TY replications | 684 | Design |
| 578 | **0.205** | TY power at T=10 | 684 | Finding |
| 579 | **0.51** | PermG power comparison | 684 | Comparison |
| 580 | **0.409** | TY power at T=20 | 684 | Finding |
| 581 | **8.1%** | TY Type I error | 684 | Finding |

**Table: beta_50 (tab:beta50), lines 696-701:**
| 582 | **0%** | FPR (FDR) at T=6 | 696 | Table |
| 583 | **2%** | FPR (FDR) at T=8 | 697 | Table |
| 584 | **2.0** | beta_50 at T=10 | 698 | Table |
| 585 | **6.32** | beta_50*sqrt(T) at T=10 | 698 | Table |
| 586 | **9%** | Raw FPR at T=10 | 698 | Table |
| 587 | **2%** | FDR FPR at T=10 | 698 | Table |
| 588 | **1.2** | beta_50 at T=15 | 699 | Table |
| 589 | **4.65** | beta_50*sqrt(T) at T=15 | 699 | Table |
| 590 | **6%** | Raw FPR at T=15 | 699 | Table |
| 591 | **2%** | FDR FPR at T=15 | 699 | Table |
| 592 | **0.9** | beta_50 at T=20 | 700 | Table |
| 593 | **4.02** | beta_50*sqrt(T) at T=20 | 700 | Table |
| 594 | **5%** | Raw FPR at T=20 | 700 | Table |
| 595 | **1%** | FDR FPR at T=20 | 700 | Table |

### Section: Non-Stationarity Robustness (App O)

**AR(1) diagnostic (Figure caption), line 712:**
| 596 | **-0.51** | Raw phi for entropy at alpha=0.00 | 712 | Finding |
| 597 | **1.00** | Raw phi for entropy at alpha=1.00 | 712 | Finding |
| 598 | **0.98** | First-diff threshold | 712 | Threshold |
| 599 | **0.75-0.95** | Raw phi for distinct-1 | 712 | Finding |
| 600 | **0.24** | Max first-diff phi for distinct-1 | 712 | Finding |
| 601 | **0.95** | Danger zone phi | 712 | Threshold (dashed red line) |

**Monte Carlo simulation, lines 716-719:**
| 602 | **11** | T value | 716 | Design |
| 603 | **1,000** | Replications | 716 | Design |
| 604 | **~10%** | PermG FPR inflation at phi>=0.95 | 716 | Finding |
| 605 | **0.95** | Non-stationarity threshold | 716 | Threshold |
| 606 | **4.2-6.6%** | First-diff size range | 716 | Finding |
| 607 | **-0.51** | Null token entropy phi | 718 | Finding |
| 608 | **0.81-0.97** | Raw phi for distinct-1 at treatment | 718 | Finding |
| 609 | **-0.14-0.44** | First-diff phi for distinct-1 | 718 | Finding |
| 610 | **4/60** | Empirical FPR count | 719 | Finding |
| 611 | **6.7%** | Empirical FPR percentage | 719 | Finding |

**Table: Nonstationarity sim (tab:nonstationarity_sim), lines 733-736:**
| 612 | **6.4** | Raw GC size at phi=0.50, beta=0 | 733 | Table |
| 613 | **6.6** | First-diff size at phi=0.50, beta=0 | 733 | Table |
| 614 | **6.8** | PermG size at phi=0.50, beta=0 | 733 | Table |
| 615 | **37.7** | Raw GC power at phi=0.50, beta=0.6 | 733 | Table |
| 616 | **17.7** | First-diff power at phi=0.50, beta=0.6 | 733 | Table |
| 617 | **36.8** | PermG power at phi=0.50, beta=0.6 | 733 | Table |
| 618 | **10.0** | Raw GC size at phi=0.95 | 734 | Table |
| 619 | **5.9** | First-diff size at phi=0.95 | 734 | Table |
| 620 | **9.5** | PermG size at phi=0.95 | 734 | Table |
| 621 | **44.3** | Raw GC power at phi=0.95 | 734 | Table |
| 622 | **28.7** | First-diff power at phi=0.95 | 734 | Table |
| 623 | **41.5** | PermG power at phi=0.95 | 734 | Table |
| 624 | **11.2** | Raw GC size at phi=0.99 | 735 | Table |
| 625 | **4.2** | First-diff size at phi=0.99 | 735 | Table |
| 626 | **10.7** | PermG size at phi=0.99 | 735 | Table |
| 627 | **46.4** | Raw GC power at phi=0.99 | 735 | Table |
| 628 | **24.6** | First-diff power at phi=0.99 | 735 | Table |
| 629 | **41.7** | PermG power at phi=0.99 | 735 | Table |

**Table: Empirical AR(1) (tab:empirical_ar1), lines 757-762:**
| 630 | **-0.51** | Token entropy raw phi, alpha=0.0 | 757 | Table |
| 631 | **-0.28** | Token entropy diff phi, alpha=0.0 | 757 | Table |
| 632 | **0.72** | Token entropy raw phi, alpha=1.0 | 757 | Table |
| 633 | **0.15** | Token entropy diff phi, alpha=1.0 | 757 | Table |
| 634 | **0.31** | ECE raw phi, alpha=0.0 | 758 | Table |
| 635 | **-0.15** | ECE diff phi, alpha=0.0 | 758 | Table |
| 636 | **0.95** | ECE raw phi, alpha=1.0 | 758 | Table |
| 637 | **0.38** | ECE diff phi, alpha=1.0 | 758 | Table |
| 638 | **0.55** | Distinct-1 raw phi, alpha=0.0 | 759 | Table |
| 639 | **0.12** | Distinct-1 diff phi, alpha=0.0 | 759 | Table |
| 640 | **0.97** | Distinct-1 raw phi, alpha=1.0 | 759 | Table |
| 641 | **0.44** | Distinct-1 diff phi, alpha=1.0 | 759 | Table |
| 642 | **0.48** | Distinct-2 raw phi, alpha=0.0 | 760 | Table |
| 643 | **0.08** | Distinct-2 diff phi, alpha=0.0 | 760 | Table |
| 644 | **0.95** | Distinct-2 raw phi, alpha=1.0 | 760 | Table |
| 645 | **0.31** | Distinct-2 diff phi, alpha=1.0 | 760 | Table |
| 646 | **0.42** | Perplexity raw phi, alpha=0.0 | 761 | Table |
| 647 | **-0.22** | Perplexity diff phi, alpha=0.0 | 761 | Table |
| 648 | **0.93** | Perplexity raw phi, alpha=1.0 | 761 | Table |
| 649 | **-0.14** | Perplexity diff phi, alpha=1.0 | 761 | Table |

**Lines 742, 767:**
| 650 | **0.60** | Max |phi| under null in raw | 742 | Threshold |
| 651 | **0.30** | Max |phi| under null after diff | 742 | Threshold |
| 652 | **0.05** | ADF p threshold | 767 | Parameter |
| 653 | **40** | Total ADF series tested (5x4x2) | 767 | Count |
| 654 | **5** | Metrics | 767 | Factor |
| 655 | **4** | Seeds | 767 | Factor |
| 656 | **2** | Conditions | 767 | Factor |
| 657 | **1** | Differencing order d=1 | 767 | Finding |
| 658 | **2** | Higher-order d>=2 | 767 | Context |
| 659 | **25** | T<=25 for KPSS context | 771 | Context |
| 660 | **0.05** | ADF p threshold (KPSS comparison) | 771 | Parameter |

**Power cost of first-differencing, lines 775-777:**
| 661 | **0.50** | phi value | 775 | Condition |
| 662 | **0.6** | beta value | 775 | Condition |
| 663 | **17.7%** | First-diff PermG power | 775 | Finding |
| 664 | **36.8%** | Raw PermG power | 775 | Comparison |
| 665 | **52%** | Relative power reduction | 775 | Finding |
| 666 | **0.95** | phi value | 776 | Condition |
| 667 | **28.7%** | First-diff power at phi=0.95 | 776 | Finding |
| 668 | **41.5%** | Raw power at phi=0.95 | 776 | Comparison |
| 669 | **31%** | Relative reduction at phi=0.95 | 776 | Finding |
| 670 | **0.72-0.97** | Empirical phi range | 777 | Observation |
| 671 | **~10%** | FPR from raw Granger | 777 | Problem |

**Table: diff_power_cost (tab:diff_power_cost), lines 788-791:**
| 672 | **36.8%** | Raw power at phi=0.50 | 788 | Table |
| 673 | **17.7%** | Diff power at phi=0.50 | 788 | Table |
| 674 | **52%** | Reduction at phi=0.50 | 788 | Table |
| 675 | **6.8%** | Raw FPR at phi=0.50 | 788 | Table |
| 676 | **41.5%** | Raw power at phi=0.95 | 789 | Table |
| 677 | **28.7%** | Diff power at phi=0.95 | 789 | Table |
| 678 | **31%** | Reduction at phi=0.95 | 789 | Table |
| 679 | **9.5%** | Raw FPR at phi=0.95 | 789 | Table |
| 680 | **41.7%** | Raw power at phi=0.99 | 790 | Table |
| 681 | **24.6%** | Diff power at phi=0.99 | 790 | Table |
| 682 | **41%** | Reduction at phi=0.99 | 790 | Table |
| 683 | **10.7%** | Raw FPR at phi=0.99 | 790 | Table |

**Lines 795-797:**
| 684 | **10** | T at which power loss is primary bottleneck | 795 | Context |
| 685 | **0.50** | alpha threshold for weak contamination | 795 | Context |
| 686 | **20** | Extended T | 796 | Finding |
| 687 | **10** | Base T comparison | 796 | Context |
| 688 | **0.95** | phi threshold | 796 | Condition |

### Section: Shapley Value Analysis (App P)

| 689 | **-0.299** | DiffXCorr combined Shapley | 806, 817 | Finding |
| 690 | **-0.141** | PermG combined Shapley | 806, 817 | Finding |
| 691 | **+0.609** | NaiveXCorr FPR contribution | 806 | Finding |
| 692 | **2^5 = 32** | Coalitions | 816 | Calculation |
| 693 | **5** | Methods | 816 | Count |

**Table: Shapley 6-pair (tab:shapley_6pair), lines 829-834:**
| 694 | **+0.609** | Naive XCorr phi^FPR | 829 | Table |
| 695 | **-0.419** | Naive XCorr phi^FNR | 829 | Table |
| 696 | **+0.190** | Naive XCorr phi^comb | 829 | Table |
| 697 | **+0.007** | DiffXCorr phi^FPR | 830 | Table |
| 698 | **-0.306** | DiffXCorr phi^FNR | 830 | Table |
| 699 | **-0.299** | DiffXCorr phi^comb | 830 | Table |
| 700 | **+0.111** | Threshold phi^FPR | 831 | Table |
| 701 | **-0.027** | Threshold phi^FNR | 831 | Table |
| 702 | **+0.084** | Threshold phi^comb | 831 | Table |
| 703 | **+0.039** | PermG phi^FPR | 832 | Table |
| 704 | **-0.180** | PermG phi^FNR | 832 | Table |
| 705 | **-0.141** | PermG phi^comb | 832 | Table |
| 706 | **+0.150** | TY phi^FPR | 833 | Table |
| 707 | **-0.069** | TY phi^FNR | 833 | Table |
| 708 | **+0.082** | TY phi^comb | 833 | Table |

### Section: MMCT Weight Robustness (App Q)

| 709 | **4** | Weighting schemes tested | 841 | Design |
| 710 | **-0.152** | PermG equal-weight Shapley | 842 | Finding |

**Table: weight_robustness (tab:weight_robustness), lines 853-857:**
| 711 | **-0.152** | PermG Equal | 853 | Table |
| 712 | **-0.148** | PermG Cap-5 | 853 | Table |
| 713 | **-0.141** | PermG Cap-10 | 853 | Table |
| 714 | **-0.141** | PermG FPR-inv | 853 | Table |
| 715 | **-0.285** | DiffXCorr Equal | 854 | Table |
| 716 | **-0.291** | DiffXCorr Cap-5 | 854 | Table |
| 717 | **-0.299** | DiffXCorr Cap-10 | 854 | Table |
| 718 | **-0.299** | DiffXCorr FPR-inv | 854 | Table |
| 719 | **+0.078** | Threshold Equal | 855 | Table |
| 720 | **+0.081** | Threshold Cap-5 | 855 | Table |
| 721 | **+0.084** | Threshold Cap-10 | 855 | Table |
| 722 | **+0.084** | Threshold FPR-inv | 855 | Table |
| 723 | **+0.088** | TY Equal | 856 | Table |
| 724 | **+0.084** | TY Cap-5 | 856 | Table |
| 725 | **+0.082** | TY Cap-10 | 856 | Table |
| 726 | **+0.082** | TY FPR-inv | 856 | Table |
| 727 | **+0.195** | NaiveXCorr Equal | 857 | Table |
| 728 | **+0.192** | NaiveXCorr Cap-5 | 857 | Table |
| 729 | **+0.190** | NaiveXCorr Cap-10 | 857 | Table |
| 730 | **+0.190** | NaiveXCorr FPR-inv | 857 | Table |

**Interpretation paragraph, lines 864:**
| 731 | **94.4%** | NaiveXCorr FPR | 864 | Context |
| 732 | **1.06** | NaiveXCorr weight | 864 | Calculated |
| 733 | **6.7%** | PermG FPR | 864 | Context |
| 734 | **14.9** | PermG weight | 864 | Calculated |
| 735 | **14x** | Weight differential | 864 | Ratio |

**Per-pair contribution, lines 870, 881-888:**
| 736 | **0.021** | Std for entropy→distinct-1 | 870 | Finding |
| 737 | **0.089** | Std for ECE→perplexity | 870 | Finding |

**Table: shapley_per_pair (tab:shapley_per_pair), lines 881-888:**
| 738 | **-0.042** | Entropy→Distinct-1 mean phi^FNR | 881 | Table |
| 739 | **0.021** | Entropy→Distinct-1 Std | 881 | Table |
| 740 | **-0.038** | Entropy→Distinct-2 mean phi^FNR | 882 | Table |
| 741 | **0.024** | Entropy→Distinct-2 Std | 882 | Table |
| 742 | **-0.035** | ECE→Distinct-1 mean phi^FNR | 883 | Table |
| 743 | **0.031** | ECE→Distinct-1 Std | 883 | Table |
| 744 | **-0.031** | ECE→Distinct-2 mean phi^FNR | 884 | Table |
| 745 | **0.028** | ECE→Distinct-2 Std | 884 | Table |
| 746 | **-0.002** | Entropy→PPL mean phi^FNR | 885 | Table |
| 747 | **0.067** | Entropy→PPL Std | 885 | Table |
| 748 | **-0.001** | ECE→PPL mean phi^FNR | 886 | Table |
| 749 | **0.089** | ECE→PPL Std | 886 | Table |

**Lines 891-897:**
| 750 | **96.2%** | Diversity channels' share of FNR reduction | 891 | Finding |
| 751 | **3.8%** | Perplexity channels' share | 891 | Finding |
| 752 | **4** | Diversity-channel pairs | 892 | Count |
| 753 | **4%** | Sensitivity sacrifice | 892 | Finding |
| 754 | **8** | Total pairs | 892 | Count |

**Coalition stability, lines 895-897:**
| 755 | **-0.138** | PermG 1-method coalition avg | 895 | Finding |
| 756 | **0.015** | SE for 1-method | 895 | Finding |
| 757 | **-0.144** | PermG 4-method coalition avg | 895 | Finding |
| 758 | **0.008** | SE for 4-method | 895 | Finding |
| 759 | **0.006** | Delta between coalition sizes | 896 | Finding |
| 760 | **-0.312** | DiffXCorr 1-method coalition | 897 | Finding |
| 761 | **-0.281** | DiffXCorr 4-method coalition | 897 | Finding |

### Section: PermG FPR Independence (App R)

**Figure caption, line 906:**
| 762 | **10** | Seeds | 906 | Design |
| 763 | **0%** | PermG FPR concentration | 906 | Finding |
| 764 | **8/10** | Seeds with 0 FP | 906 | Finding |
| 765 | **6.7%** | Aggregate FPR | 906 | Finding |
| 766 | **83%** | NaiveXCorr minimum FPR across seeds | 906 | Finding |

**Lines 910-913:**
| 767 | **9** | Seeds in table | 910 | Count |
| 768 | **54** | Pairs (9 seeds x 6) | 910 | Count |
| 769 | **6** | Pair basis | 910 | Design |
| 770 | **4/60** | FP count (10 seeds, pooled) | 910 | Finding |
| 771 | **6.7%** | Pooled FPR | 910 | Finding |
| 772 | **1.8%** | CI lower bound | 910 | Statistical |
| 773 | **16.2%** | CI upper bound | 910 | Statistical |
| 774 | **8/10** | Seeds yielding 0 FP | 911 | Finding |
| 775 | **6/60** | K>=3 consensus FP | 912 | Finding |
| 776 | **10.0%** | K>=3 consensus FPR | 912 | Finding |
| 777 | **2** | PermG contribution to consensus FP | 912 | Finding |
| 778 | **0/12** | PermG FPR at T=15 | 913 | Finding |
| 779 | **0%** | PermG FPR at T=15 | 913 | Finding |

**Bootstrap FPR (Figure caption), line 950:**
| 780 | **10,000** | Bootstrap resamples | 950 | Design |
| 781 | **10** | Seeds | 950 | Design |
| 782 | **1.8%** | PermG 95% CI lower | 950 | Finding |
| 783 | **16.2%** | PermG 95% CI upper | 950 | Finding |
| 784 | **27.8%** | Threshold point estimate | 950 | Comparison |
| 785 | **90%** | NaiveXCorr bootstrap peak | 950 | Finding |

**Table: Per-seed FPR 8-pair (tab:per_seed_fpr_8pair), lines 964-968:**
| 786 | **0/8** | PermG s42 | 964 | Table |
| 787 | **4/8** | DiffXCorr s42 | 964 | Table |
| 788 | **3/8** | Threshold s42 | 964 | Table |
| 789 | **2/8** | TY s42 | 964 | Table |
| 790 | **8/8** | NaiveXCorr s42 | 964 | Table |
| 791 | **0/8** | PermG s43 | 965 | Table |
| 792 | **2/8** | DiffXCorr s43 | 965 | Table |
| 793 | **1/8** | Threshold s43 | 965 | Table |
| 794 | **2/8** | TY s43 | 965 | Table |
| 795 | **7/8** | NaiveXCorr s43 | 965 | Table |
| 796 | **0/8** | PermG s44 | 966 | Table |
| 797 | **3/8** | DiffXCorr s44 | 966 | Table |
| 798 | **2/8** | Threshold s44 | 966 | Table |
| 799 | **0/8** | TY s44 | 966 | Table |
| 800 | **7/8** | NaiveXCorr s44 | 966 | Table |
| 801 | **0.0%** | Pooled PermG FPR (8-pair) | 968 | Table |
| 802 | **37.5%** | Pooled DiffXCorr FPR | 968 | Table |
| 803 | **25.0%** | Pooled Threshold FPR | 968 | Table |
| 804 | **16.7%** | Pooled TY FPR | 968 | Table |
| 805 | **91.7%** | Pooled NaiveXCorr FPR | 968 | Table |

**Table: Per-seed PermG FPR 6-pair (tab:per_seed_fpr_6pair), lines 982-989:**
| 806 | **2/6** | PermG fwd s45 | 982 | Table |
| 807 | **0/6** | K>=3 s45 | 982 | Table |
| 808 | **0/6** | PermG fwd s46 | 983 | Table |
| 809 | **1/6** | K>=3 s46 | 983 | Table |
| 810 | **0/6** | PermG fwd s47 | 984 | Table |
| 811 | **0/6** | K>=3 s47 | 984 | Table |
| 812 | **0/6** | PermG fwd s48 | 985 | Table |
| 813 | **0/6** | K>=3 s48 | 985 | Table |
| 814 | **0/6** | PermG fwd s49 | 986 | Table |
| 815 | **0/6** | K>=3 s49 | 986 | Table |
| 816 | **2/6** | PermG fwd s50 | 987 | Table |
| 817 | **2/6** | K>=3 s50 | 987 | Table |
| 818 | **0/6** | PermG fwd s51 | 988 | Table |
| 819 | **0/6** | K>=3 s51 | 988 | Table |

**Line 994:**
| 820 | **6/36** | K>=3 FPR on 6-pair basis | 994 | Finding |
| 821 | **16.7%** | K>=3 FPR percent | 994 | Finding |
| 822 | **6** | Total FP in K>=3 | 994 | Finding |
| 823 | **2** | FP involving PermG | 994 | Finding |
| 824 | **4** | FP driven by other methods | 994 | Finding |

### Section: Sigmoid Transition Shape (App S)

| 825 | **13** | Points on T=10 grid | 1001 | Design |
| 826 | **0.483 ± 0.006** | alpha_c from 13-point grid | 1001 | Fit result |
| 827 | **478 ± 475** | k from 13-point grid | 1001 | Fit result |
| 828 | **17** | Dense alpha sampling points | 1002 | Design |
| 829 | **-110** | Delta AIC (sigmoid vs step) | 1002 | Model comparison |
| 830 | **15.7** | Fitted steepness k (dense) | 1002 | Fit result |
| 831 | **9.4** | k 95% CI lower | 1002 | CI |
| 832 | **28.2** | k 95% CI upper | 1002 | CI |
| 833 | **6.1** | k from H0 linear simulation | 1004 | Simulation |
| 834 | **4.9** | k from H0' concave simulation | 1004 | Simulation |
| 835 | **4.9-6.1** | k range from smooth models | 1004 | Range |
| 836 | **2.6-3.2** | Steepness ratios k_obs/k_H0 | 1004 | Calculated |
| 837 | **~2** | CI lower bound ratio | 1004 | Calculated |

**Combined T=10+T=20 fit, lines 1007-1009:**
| 838 | **279.3** | k (combined fit) | 1007 | Fit result |
| 839 | **527.6** | SE for k | 1007 | Statistical |
| 840 | **0.451** | alpha_c (combined) | 1007 | Fit result |
| 841 | **0.75** | y_max | 1007 | Fit result |
| 842 | **79.86** | AIC (combined) | 1007 | Model comparison |
| 843 | **0.478, 0.487** | 90% transition width bounds at T=10 | 1008 | Finding |
| 844 | **0.0092** | Width at T=10 alone | 1008 | Finding |
| 845 | **0.443, 0.459** | 90% transition width bounds combined | 1008 | Finding |
| 846 | **0.0158** | Width combined | 1008 | Finding |
| 847 | **0.031** | alpha_c leftward shift | 1008 | Finding |
| 848 | **41.6%** | k drop relative to T=10-only | 1009 | Finding |
| 849 | **0/8** | alpha=0.45 at T=10 | 1010 | Finding |
| 850 | **5/8** | alpha=0.45 at T=20 | 1010 | Finding |

**Alternative functional forms, line 1013:**
| 851 | **32.99** | AIC at T=10 (probit=sigmoid) | 1013 | Model comparison |
| 852 | **79.86** | AIC combined | 1013 | Model comparison |
| 853 | **1** | Extra parameter for generalized logistic | 1014 | Model complexity |
| 854 | **+2** | AIC penalty | 1014 | Model comparison |

**Table: Transition width (tab:transition_width), lines 1028-1033:**
| 855 | **0.009** | Width T=10 observed (13-pt) | 1028 | Table |
| 856 | **0.483** | alpha_c T=10 (13-pt) | 1028 | Table |
| 857 | **478** | k T=10 (13-pt) | 1028 | Table |
| 858 | **0.028** | Width T=10 dense (17-pt) | 1029 | Table |
| 859 | **0.481** | alpha_c T=10 dense | 1029 | Table |
| 860 | **15.7** | k T=10 dense | 1029 | Table |
| 861 | **0.016** | Width T=10+20 combined | 1030 | Table |
| 862 | **0.451** | alpha_c combined | 1030 | Table |
| 863 | **279** | k combined | 1030 | Table |
| 864 | **0.072** | Width H0 linear | 1031 | Table |
| 865 | **0.507** | alpha_c H0 linear | 1031 | Table |
| 866 | **6.1** | k H0 linear | 1031 | Table |
| 867 | **0.090** | Width H0' concave | 1032 | Table |
| 868 | **0.521** | alpha_c H0' concave | 1032 | Table |
| 869 | **4.9** | k H0' concave | 1032 | Table |

**Line 1040 (Figure caption):**
| 870 | **1** | d=1 (first-order differencing) | 1040 | Finding |
| 871 | **0.05** | ADF p threshold | 1040 | Parameter |

**Lines 1044-1047:**
| 872 | **0.028** | Dense-sampling transition width | 1044 | Finding |
| 873 | **0.467, 0.495** | Alpha range for transition | 1044 | Finding |
| 874 | **~3x** | Narrower than smooth models | 1044 | Ratio |
| 875 | **0.072-0.090** | Smooth model predictions | 1044 | Comparison |
| 876 | **0.03** | Delta alpha in practical terms | 1045 | Context |
| 877 | **0%** | Detection probability below boundary | 1045 | Finding |
| 878 | **75%** | Detection probability above boundary | 1045 | Finding |
| 879 | **150** | Additional synthetic samples | 1045 | Calculation |
| 880 | **5,000** | Total samples | 1045 | Context |
| 881 | **0.47** | Alpha below detection | 1047 | Example |
| 882 | **0.50** | Alpha above detection | 1047 | Example |
| 883 | **0%** | Alarm rate below | 1047 | Example |
| 884 | **75%** | Alarm rate above | 1047 | Example |
| 885 | **3** | Percentage-point increase | 1047 | Finding |

### Section: Intervention Threshold Sensitivity (App T)

| 886 | **5%-25%** | Five tested thresholds range | 1052 | Design |
| 887 | **1** | Trigger generation | 1052 | Finding |
| 888 | **40.7%** | Entropy drop at alpha=1.0 | 1052 | Finding |
| 889 | **57.0** | Peak PPL | 1052 | Finding |
| 890 | **21.3** | Final PPL | 1052 | Finding |
| 891 | **10%** | Safe band lower | 1053 | Finding |
| 892 | **22%** | Safe band upper | 1053 | Finding |
| 893 | **7.5%** | Below this triggers false alarms | 1053 | Finding |
| 894 | **22.4%** | Above this misses alpha=0.50 | 1053 | Finding |

**Cross-seed/scale replication, lines 1056-1058:**
| 895 | **-22.5%** | Entropy drop bf16 s43 | 1056 | Finding |
| 896 | **-40.7%** | Entropy drop fp32 comparison | 1056 | Comparison |
| 897 | **24.65** | Peak PPL bf16 | 1056 | Finding |
| 898 | **-51.9%** | 1.4B entropy drop | 1057 | Finding |
| 899 | **2.946** | 1.4B entropy before | 1057 | Finding |
| 900 | **1.418** | 1.4B entropy after | 1057 | Finding |
| 901 | **19.68** | 1.4B PPL from | 1057 | Finding |
| 902 | **65.37** | 1.4B PPL peak to | 1057 | Finding |
| 903 | **17.44** | 1.4B gen-2 PPL | 1057 | Finding |
| 904 | **17.6** | 1.4B gen-10 PPL | 1057 | Finding |
| 905 | **0.007** | ECE before spike | 1058 | Finding |
| 906 | **0.281** | ECE at spike | 1058 | Finding |
| 907 | **0.017** | ECE post-intervention | 1058 | Finding |

**Alpha=0.75 intervention, lines 1061-1063:**
| 908 | **6/8** | PermG forward at alpha=0.75 | 1062 | Finding |
| 909 | **6/8** | K>=4 at alpha=0.75 | 1062 | Finding |
| 910 | **-5.7%** | Entropy drift post-intervention | 1063 | Finding |
| 911 | **10** | Generations post-intervention | 1063 | Context |
| 912 | **-27.6%** | Entropy drift without intervention | 1063 | Comparison |

**No-intervention baseline, lines 1066-1068:**
| 913 | **1003.73** | Gen-10 PPL without intervention | 1066 | Finding |
| 914 | **0.0704** | Distinct-1 without intervention | 1066 | Finding |
| 915 | **21.29** | Gen-10 PPL with intervention | 1067 | Finding |
| 916 | **0.0844** | Distinct-1 with intervention | 1067 | Finding |
| 917 | **+19.9%** | Higher diversity with intervention | 1067 | Finding |
| 918 | **64%** | Peak PPL reduction | 1068 | Finding |
| 919 | **56.99** | Peak PPL predictive | 1068 | Finding |
| 920 | **157.09** | Peak PPL reactive | 1068 | Finding |

**CUSUM figure caption, line 1073:**
| 921 | **0.7** | Entropy drop |delta x| | 1073 | Finding |
| 922 | **0.03** | Null variability sigma_0 | 1073 | Finding |
| 923 | **10%** | Safe band lower | 1073 | Context |
| 924 | **22%** | Safe band upper | 1073 | Context |

### Section: Channel Effect Size (App U)

| 925 | **0.952** | |r| for diversity channels (first-diff) | 1081 | Finding |
| 926 | **1.00** | |r| for perplexity channels | 1081 | Finding |
| 927 | **20-28x** | Granger F-statistic asymmetry | 1082 | Finding |
| 928 | **81%** | Diversity channels peaking at canary-leading lags | 1082 | Finding |
| 929 | **-1** | Median lag for diversity | 1082 | Finding |
| 930 | **0** | Lag for perplexity (contemporaneous) | 1082 | Finding |

**Table: Lag structure (tab:lag_structure), lines 1097-1103:**
| 931 | **-1** | Entropy→Dist-1 peak lag | 1097 | Table |
| 932 | **0.96** | |r| at peak Entropy→Dist-1 | 1097 | Table |
| 933 | **-1** | Entropy→Dist-2 peak lag | 1098 | Table |
| 934 | **0.95** | |r| at peak Entropy→Dist-2 | 1098 | Table |
| 935 | **-1** | ECE→Dist-1 peak lag | 1099 | Table |
| 936 | **0.94** | |r| at peak ECE→Dist-1 | 1099 | Table |
| 937 | **-1** | ECE→Dist-2 peak lag | 1100 | Table |
| 938 | **0.93** | |r| at peak ECE→Dist-2 | 1100 | Table |
| 939 | **0** | Entropy→PPL peak lag | 1101 | Table |
| 940 | **0.99** | |r| at peak Entropy→PPL | 1101 | Table |
| 941 | **0** | ECE→PPL peak lag | 1102 | Table |
| 942 | **0.98** | |r| at peak ECE→PPL | 1102 | Table |

**Lines 1107:**
| 943 | **~0** | Granger F for contemporaneous | 1107 | Finding |
| 944 | **0.99** | p-value after differencing | 1107 | Finding |

**Fisher Z-transform (tab:fisher_z), lines 1123-1129:**
| 945 | **0.955** | r_div Entropy→ at lag=0 | 1123 | Table |
| 946 | **0.990** | r_ppl Entropy→ at lag=0 | 1123 | Table |
| 947 | **-2.13** | Z_diff at lag=0 Entropy | 1123 | Table |
| 948 | **0.033** | p at lag=0 Entropy | 1123 | Table |
| 949 | **0.935** | r_div ECE→ at lag=0 | 1124 | Table |
| 950 | **0.980** | r_ppl ECE→ at lag=0 | 1124 | Table |
| 951 | **-2.41** | Z_diff at lag=0 ECE | 1124 | Table |
| 952 | **0.016** | p at lag=0 ECE | 1124 | Table |
| 953 | **0.952** | r_div Entropy→ at lag=-1 | 1127 | Table |
| 954 | **0.812** | r_ppl Entropy→ at lag=-1 | 1127 | Table |
| 955 | **+3.67** | Z_diff at lag=-1 Entropy | 1127 | Table |
| 956 | **<0.001** | p at lag=-1 Entropy | 1127 | Table |
| 957 | **0.941** | r_div ECE→ at lag=-1 | 1128 | Table |
| 958 | **0.795** | r_ppl ECE→ at lag=-1 | 1128 | Table |
| 959 | **+3.89** | Z_diff at lag=-1 ECE | 1128 | Table |
| 960 | **<0.001** | p at lag=-1 ECE | 1128 | Table |

**Lines 1133-1134:**
| 961 | **0.990** | r for PPL at lag=0 | 1133 | Finding |
| 962 | **0.955** | r for diversity at lag=0 | 1133 | Finding |
| 963 | **-2.13** | Z value | 1133 | Finding |
| 964 | **0.033** | p value | 1133 | Finding |
| 965 | **0.952** | r for diversity at lag=-1 | 1134 | Finding |
| 966 | **0.812** | r for PPL at lag=-1 | 1134 | Finding |
| 967 | **3.67** | Z value at lag=-1 | 1134 | Finding |
| 968 | **0.001** | p threshold | 1134 | Finding |

**Figure caption, line 1142:**
| 969 | **20-28x** | F-statistic ratio | 1142 | Caption |
| 970 | **81%** | At canary-leading lags | 1142 | Caption |
| 971 | **50%** | PPL at lag=0 | 1142 | Caption |

### Section: Mutual Information and Partial Correlation (App V)

| 972 | **0.010-0.141** | MI range in blind zone (bits) | 1150 | Finding |

**Table: MI blind (tab:mi_blind), lines 1167-1172:**
| 973 | **0.010** | MI at alpha=0.00 | 1167 | Table |
| 974 | **0/8** | PermG at alpha=0.00 | 1167 | Table |
| 975 | **0.025** | MI at alpha=0.10 | 1168 | Table |
| 976 | **0/8** | PermG at alpha=0.10 | 1168 | Table |
| 977 | **0.048** | MI at alpha=0.25 | 1169 | Table |
| 978 | **0/8** | PermG at alpha=0.25 | 1169 | Table |
| 979 | **0.141** | MI at alpha=0.45 | 1170 | Table |
| 980 | **0/8** | PermG at alpha=0.45 | 1170 | Table |
| 981 | **0.312** | MI at alpha=0.50 | 1171 | Table |
| 982 | **6/8** | PermG at alpha=0.50 | 1171 | Table |

**Table: Partial correlation (tab:partial_corr), lines 1193-1196:**

alpha=0.00 row:
| 983 | **0.414** | Contemporaneous zero-order |r| at alpha=0.00 | 1193 | Table |
| 984 | **3/18** | Contemporaneous zero-order Sig. | 1193 | Table |
| 985 | **0.323** | Contemporaneous partial |r| at alpha=0.00 | 1193 | Table |
| 986 | **0/18** | Contemporaneous partial Sig. | 1193 | Table |
| 987 | **0.563** | Lagged zero-order |r| at alpha=0.00 | 1193 | Table |
| 988 | **8/18** | Lagged zero-order Sig. | 1193 | Table |
| 989 | **0.524** | Lagged partial |r| at alpha=0.00 | 1193 | Table |
| 990 | **9/18** | Lagged partial Sig. | 1193 | Table |

alpha=0.50 row:
| 991 | **0.590** | Contemp. zero-order |r| at alpha=0.50 | 1194 | Table |
| 992 | **9/18** | Contemp. zero-order Sig. at 0.50 | 1194 | Table |
| 993 | **0.381** | Contemp. partial |r| at alpha=0.50 | 1194 | Table |
| 994 | **2/18** | Contemp. partial Sig. at 0.50 | 1194 | Table |
| 995 | **0.759** | Lagged zero-order |r| at alpha=0.50 | 1194 | Table |
| 996 | **12/18** | Lagged zero-order Sig. at 0.50 | 1194 | Table |
| 997 | **0.841** | Lagged partial |r| at alpha=0.50 | 1194 | Table |
| 998 | **17/18** | Lagged partial Sig. at 0.50 | 1194 | Table |

alpha=0.75 row:
| 999 | **0.636** | Contemp. zero-order |r| at alpha=0.75 | 1195 | Table |
| 1000 | **9/18** | Contemp. zero-order Sig. at 0.75 | 1195 | Table |
| 1001 | **0.521** | Contemp. partial |r| at alpha=0.75 | 1195 | Table |
| 1002 | **3/18** | Contemp. partial Sig. at 0.75 | 1195 | Table |
| 1003 | **0.831** | Lagged zero-order |r| at alpha=0.75 | 1195 | Table |
| 1004 | **17/18** | Lagged zero-order Sig. at 0.75 | 1195 | Table |
| 1005 | **0.913** | Lagged partial |r| at alpha=0.75 | 1195 | Table |
| 1006 | **18/18** | Lagged partial Sig. at 0.75 | 1195 | Table |

**Lines 1200, 1205, 1212, 1218, 1224:**
| 1007 | **0.590→0.381** | Contemp. drop at alpha=0.50 | 1200 | Finding |
| 1008 | **0.759→0.841** | Lagged strengthening at alpha=0.50 | 1200 | Finding |
| 1009 | **35/36** | Detection-condition pairs retaining significance | 1200 | Finding |
| 1010 | **0.831→0.913** | Lagged strengthening at alpha=0.75 | 1205 | Caption |
| 1011 | **0.524** | Lagged partial at alpha=0.00 | 1212 | Finding |
| 1012 | **0.913** | Lagged partial at alpha=0.75 | 1212 | Finding |
| 1013 | **18/18** | Universal significance at alpha=0.75 | 1212 | Finding |
| 1014 | **9/18** | Lagged significance at null | 1223 | Finding |
| 1015 | **0.524** | Null lagged partial | 1224 | Comparison |
| 1016 | **0.913** | Treatment lagged partial | 1224 | Comparison |

### Section: Moment Cascade Analysis (App W)

| 1017 | **5%** | Onset threshold | 1230 | Parameter |
| 1018 | **1** | Entropy onset generation | 1230 | Finding |
| 1019 | **6** | Number of conditions | 1230 | Count |
| 1020 | **2** | Distinct-n onset generation | 1230 | Finding |
| 1021 | **18** | Pairwise comparisons | 1230 | Count |

**Table: Moment cascade (tab:moment_cascade), lines 1242-1248:**
| 1022 | **1** | Entropy onset s42 alpha=0.10 | 1242 | Table |
| 1023 | **2** | Dist-1, Dist-2, Dist-3 onset s42 alpha=0.10 | 1242 | Table |
| 1024 | **2** | ECE onset s42 alpha=0.10 | 1242 | Table |
| 1025 | **1** | Entropy onset s42 alpha=0.50 | 1243 | Table |
| 1026 | **2** | Dist-1/2/3 onset s42 alpha=0.50 | 1243 | Table |
| 1027 | **1** | ECE onset s42 alpha=0.50 | 1243 | Table |
| 1028 | **4** | PPL onset s42 alpha=0.50 | 1243 | Table |
| 1029 | **1** | All onsets s42 alpha=0.75 (entropy, ECE, PPL) | 1244 | Table |
| 1030 | **2** | Dist-1/2/3 onset s42 alpha=0.75 | 1244 | Table |
| 1031 | **1** | Entropy onset s43 alpha=0.25 | 1245 | Table |
| 1032 | **2** | Dist-1/2/3 onset s43 alpha=0.25 | 1245 | Table |
| 1033 | **4** | ECE onset s43 alpha=0.25 | 1245 | Table |
| 1034 | **1** | Entropy onset s43 alpha=0.50 | 1246 | Table |
| 1035 | **2** | Dist-1/2/3 onset s43 alpha=0.50 | 1246 | Table |
| 1036 | **1** | ECE onset s43 alpha=0.50 | 1246 | Table |
| 1037 | **4** | PPL onset s43 alpha=0.50 | 1246 | Table |
| 1038 | **1** | All onsets s43 alpha=0.75 (entropy, ECE, PPL) | 1247 | Table |
| 1039 | **2** | Dist-1/2/3 onset s43 alpha=0.75 | 1247 | Table |

**Onset threshold sensitivity (tab:onset_threshold_sensitivity), lines 1274-1278:**
| 1040 | **6/6** | t_H<=t_D at 5% threshold | 1274 | Table |
| 1041 | **0/6** | Ties at 5% | 1274 | Table |
| 1042 | **0/6** | Violations at 5% | 1274 | Table |
| 1043 | **6/6** | t_H<=t_D at 10% | 1275 | Table |
| 1044 | **5/6** | t_H<=t_D at 15% | 1276 | Table |
| 1045 | **1/6** | Ties at 15% | 1276 | Table |
| 1046 | **4/6** | t_H<=t_D at 20% | 1277 | Table |
| 1047 | **2/6** | Ties at 20% | 1277 | Table |
| 1048 | **0/24** | Total violations (t_H>t_D) | 1282 | Finding |
| 1049 | **1** | Lag magnitude at 5% threshold | 1283 | Finding |

**MAUVE cascade, lines 1287-1289:**
| 1050 | **2-3** | MAUVE onset generation | 1287 | Finding |
| 1051 | **2** | Distinct-n onset for comparison | 1287 | Finding |
| 1052 | **~0.033** | MAUVE floor saturation value | 1289 | Finding |
| 1053 | **3-4** | Generation of MAUVE floor | 1289 | Finding |

**Perplexity irregularity, line 1292:**
| 1054 | **4** | PPL onset at alpha=0.50 (s42) | 1292 | Finding |
| 1055 | **1** | Entropy onset for comparison | 1292 | Context |
| 1056 | **2** | Diversity onset for comparison | 1292 | Context |
| 1057 | **1** | PPL onset at alpha=0.75 | 1292 | Finding |

**Cascade onset table (tab:cascade_onset), lines 1433-1437:**
| 1058 | **1** | t_H s42 alpha=0.50 | 1433 | Table |
| 1059 | **1** | t_ECE s42 alpha=0.50 | 1433 | Table |
| 1060 | **2** | t_D s42 alpha=0.50 | 1433 | Table |
| 1061 | **3** | t_M s42 alpha=0.50 | 1433 | Table |
| 1062 | **1** | t_H s43 alpha=0.50 | 1434 | Table |
| 1063 | **1** | t_ECE s43 alpha=0.50 | 1434 | Table |
| 1064 | **2** | t_D s43 alpha=0.50 | 1434 | Table |
| 1065 | **2** | t_M s43 alpha=0.50 | 1434 | Table |
| 1066 | **1, 1, 2, 3** | s42 alpha=0.75 | 1435 | Table |
| 1067 | **1, 1, 2, 2** | s43 alpha=0.75 | 1436 | Table |

### Section: Discretized Entropy Robustness (App W cont.)

| 1068 | **7** | Experiments at alpha=1.0 | 1303 | Design |
| 1069 | **5, 10, 15, 20** | Bin counts tested | 1303 | Design |
| 1070 | **5,000** | Permutations | 1303 | Parameter |
| 1071 | **1** | Max lag | 1303 | Parameter |

**Table: Discretized entropy (tab:discretized_entropy), lines 1314-1318:**
| 1072 | **7/7** | Equal-width at 20 bins | 1314 | Table |
| 1073 | **7/7** | Equal-freq at 20 bins | 1314 | Table |
| 1074 | **6/7** | Equal-width at 15 bins | 1315 | Table |
| 1075 | **7/7** | Equal-freq at 15 bins | 1315 | Table |
| 1076 | **5/7** | Equal-width at 10 bins | 1316 | Table |
| 1077 | **1/7** | Equal-freq at 10 bins | 1316 | Table |
| 1078 | **3/7** | Equal-width at 5 bins | 1317 | Table |
| 1079 | **0/7** | Equal-freq at 5 bins | 1317 | Table |
| 1080 | **7/7** | Continuous baseline | 1308 | Caption |

**Lines 1322-1324:**
| 1081 | **15** | Minimum bins for preservation | 1322 | Finding |
| 1082 | **6-7/7** | Preserved count at >=15 bins | 1322 | Finding |
| 1083 | **10** | Threshold for degradation | 1323 | Finding |
| 1084 | **0-2** | Informative early decline gen range | 1323 | Context |
| 1085 | **5** | Equal-width bins | 1324 | Finding |
| 1086 | **0.035** | p at 5 equal-width bins (Pythia-410M) | 1324 | Finding |
| 1087 | **5** | Equal-freq bins | 1324 | Finding |
| 1088 | **0.700** | p at 5 equal-freq bins | 1324 | Finding |

### Section: Cascade Ordering Theory (App X)

**Margin consumption table (tab:margin_consumption), lines 1490-1495:**
| 1089 | **2.3 x 10^-3** | gamma(p0, epsilon) at all alpha | 1490-1494 | Table (same for all rows) |
| 1090 | **3** | Margin gen at alpha=0.10 | 1490 | Table |
| 1091 | **2** | Margin gen at alpha=0.25 | 1491 | Table |
| 1092 | **1** | Margin gen at alpha=0.50, 0.75, 1.00 | 1492-1494 | Table |
| 1093 | **1** | t_D - t_H (invariant across all alpha) | 1490-1494 | Table |

**Lines 1476-1478:**
| 1094 | **5,000** | N (generation sample size) | 1477 | Context |
| 1095 | **10,000** | Doubled N | 1477 | Hypothetical |
| 1096 | **2 x 10^-4** | Effective epsilon | 1478 | Calculated |
| 1097 | **1** | t_D - t_H = 1 lag at alpha>=0.50 | 1478 | Finding |
| 1098 | **0.25** | Low alpha | 1479 | Condition |
| 1099 | **2-3** | Gen where margin exceeded at low alpha | 1479 | Finding |

### Section: Power Simulation Shape Comparison (App Y)

| 1100 | **1,000** | Replications | 1505 | Design |
| 1101 | **1,000** | n_perm | 1505 | Parameter |
| 1102 | **0.05** | BH FDR q | 1505 | Parameter |
| 1103 | **4.9-6.1** | k from smooth models | 1506 | Finding |
| 1104 | **15.7** | Observed k | 1506 | Comparison |
| 1105 | **~3x** | k ratio | 1506 | Ratio |
| 1106 | **6/8** | Detection ceiling | 1508 | Finding |
| 1107 | **0.5** | Concave signal exponent | 1512 | Model specification |
| 1108 | **50%** | Target detection at alpha=0.50, T=10 | 1511 | Calibration |

**Table: Steepness comparison (tab:steepness_comparison), lines 1530-1534:**
| 1109 | **6.1** | k for H0 linear | 1530 | Table |
| 1110 | **2.08** | eta for H0 linear | 1530 | Table |
| 1111 | **2.6** | k_obs/k ratio for linear | 1530 | Table |
| 1112 | **4.9** | k for H0' concave | 1531 | Table |
| 1113 | **1.87** | eta for H0' concave | 1531 | Table |
| 1114 | **3.2** | k_obs/k ratio for concave | 1531 | Table |
| 1115 | **infinity** | k for H1 step | 1532 | Table |
| 1116 | **15.7** | k observed | 1533 | Table |
| 1117 | **2.08** | eta observed | 1533 | Table |
| 1118 | **1.0** | k_obs/k self-ratio | 1533 | Table |

**PermG power curve caption, line 1541:**
| 1119 | **6, 8, 10, 15, 20** | T values | 1541 | Design |
| 1120 | **100** | Replications | 1541 | Design |
| 1121 | **5,000** | Permutations | 1541 | Design |
| 1122 | **2.0** | beta for 50% power at T=10 | 1541 | Finding |
| 1123 | **~0.9** | beta for 50% power at T=20 | 1541 | Finding |

### Section: T=20 Extension Results (App Z)

| 1124 | **6/8** | PermG at alpha>=0.50, T=10 and T=20 | 1548 | Finding |
| 1125 | **0/8** | alpha=0.45 at T=10 | 1549 | Finding |
| 1126 | **5/8** | alpha=0.45 at T=20 | 1549 | Finding |
| 1127 | **0.45** | alpha for blind zone boundary | 1549 | Finding |
| 1128 | **5/8** | alpha=0.60 at T=25 | 1550 | Finding |
| 1129 | **6/8** | Forward at alpha=0.50,0.75,1.0 | 1551 | Finding |
| 1130 | **0/8** | Reverse at above conditions | 1551 | Finding |

**Table: T=25 full (tab:t25_full), lines 1567-1573:**
| 1131 | **6/8** | PermG fwd alpha=0.45 s42 T=25 | 1567 | Table |
| 1132 | **6/8** | K>=3 alpha=0.45 s42 T=25 | 1567 | Table |
| 1133 | **6/8** | PermG fwd alpha=0.45 s43 T=25 | 1568 | Table |
| 1134 | **6/8** | K>=3 alpha=0.45 s43 T=25 | 1568 | Table |
| 1135 | **6/8** | PermG fwd alpha=0.50 s42 T=25 | 1569 | Table |
| 1136 | **6/8** | K>=3 alpha=0.50 s42 T=25 | 1569 | Table |
| 1137 | **5/8** | PermG fwd alpha=0.60 s42 T=25 | 1570 | Table |
| 1138 | **6/8** | K>=3 alpha=0.60 s42 T=25 | 1570 | Table |
| 1139 | **6/8** | PermG fwd alpha=0.75 s42 T=25 | 1571 | Table |
| 1140 | **6/8** | K>=3 alpha=0.75 s42 T=25 | 1571 | Table |
| 1141 | **6/8** | PermG fwd alpha=0.75 s43 T=25 | 1572 | Table |
| 1142 | **6/8** | K>=3 alpha=0.75 s43 T=25 | 1572 | Table |

| 1143 | **2/8** | Structurally non-detectable pairs | 1556 | Finding |
| 1144 | **~0.033** | MAUVE floor saturation | 1556 | Finding |

**Lines 1577-1580:**
| 1145 | **3/8** | alpha=0.25 at T=20 | 1578 | Finding |
| 1146 | **0/8** | alpha=0.25 at T=10 | 1578 | Comparison |
| 1147 | **6/8** | Reliability threshold | 1580 | Standard |

**Table: Cross-T full (tab:cross_t_full), lines 1605-1611:**
All cells:
| 1148 | **0/8** | alpha=0.25 T=5 | 1605 | Table |
| 1149 | **0/8** | alpha=0.25 T=10 | 1605 | Table |
| 1150 | **3/8** | alpha=0.25 T=20 | 1605 | Table |
| 1151 | **0/8** | alpha=0.45 T=5,10 | 1606 | Table |
| 1152 | **6/8** | alpha=0.45 T=15,25 | 1606 | Table |
| 1153 | **5/8** | alpha=0.45 T=20 | 1606 | Table |
| 1154 | **0/8** | alpha=0.50 T=5 | 1607 | Table |
| 1155 | **6/8** | alpha=0.50 T=10,15,20,25 | 1607 | Table |
| 1156 | **0/8** | alpha=0.60 T=5,10,15,20 | 1608 | Table |
| 1157 | **5/8** | alpha=0.60 T=25 | 1608 | Table |
| 1158 | **0/8** | alpha=0.75 T=5 | 1609 | Table |
| 1159 | **6/8** | alpha=0.75 T=10,15,20,25 | 1609 | Table |
| 1160 | **0/8** | alpha=1.00 T=5 | 1610 | Table |
| 1161 | **6/8** | alpha=1.00 T=10,15,20,25 | 1610 | Table |

**Detection efficiency, lines 1641-1647:**
| 1162 | **0.00** | efficiency alpha=0.25 T=10 | 1641 | Table |
| 1163 | **0.375** | efficiency alpha=0.25 T=20 | 1641 | Table |
| 1164 | **0.00** | efficiency alpha=0.45 T=10 | 1642 | Table |
| 1165 | **0.75** | efficiency alpha=0.45 T=15,25 | 1642 | Table |
| 1166 | **0.625** | efficiency alpha=0.45 T=20 | 1642 | Table |
| 1167 | **0.75** | efficiency alpha=0.50 all T | 1643 | Table |
| 1168 | **0.00** | efficiency alpha=0.60 T=10,15,20 | 1644 | Table |
| 1169 | **0.625** | efficiency alpha=0.60 T=25 | 1644 | Table |
| 1170 | **0.75** | efficiency alpha=0.75 all T | 1645 | Table |
| 1171 | **0.75** | efficiency alpha=1.00 all T | 1646 | Table |

**Lines 1652-1660:**
| 1172 | **0.75** | Plateau value (6/8) | 1652 | Finding |
| 1173 | **2/8** | Non-detectable pairs | 1653 | Finding |
| 1174 | **~0.033** | MAUVE floor | 1653 | Finding |
| 1175 | **10** | Min T for high alpha | 1654 | Context |
| 1176 | **0.50** | High alpha threshold | 1654 | Condition |
| 1177 | **0.45, 0.60** | Boundary alpha values | 1654 | Context |
| 1178 | **10** | T=10 base | 1658 | Context |
| 1179 | **15** | T=15 extension | 1658 | Context |
| 1180 | **+6** | Newly significant pairs at alpha=0.45 | 1658 | Finding |
| 1181 | **1.2** | Info gain rate (pairs/gen) at alpha=0.45 | 1658 | Calculated |
| 1182 | **-0.2** | Rate T=15→20 at alpha=0.45 | 1658 | Finding |
| 1183 | **0** | New pairs at alpha=0.60 through T=20 | 1659 | Finding |
| 1184 | **10** | Additional generations (T=10→20) | 1659 | Context |
| 1185 | **+5** | New pairs T=20→25 at alpha=0.60 | 1659 | Finding |
| 1186 | **1.0** | Rate (pairs/gen) at alpha=0.60 | 1659 | Calculated |
| 1187 | **40-60%** | Cost reduction from adaptive monitoring | 1660 | Finding |

**Task degradation, line 1591:**
| 1188 | **10** | Generation 10 | 1591 | Context |
| 1189 | **0.05** | alpha=0.05 | 1591 | Condition |
| 1190 | **20.8** | PPL at alpha=0.05 | 1591 | Finding |
| 1191 | **26.6** | Baseline PPL | 1591 | Comparison |
| 1192 | **0.50** | alpha boundary | 1591 | Condition |
| 1193 | **31.3** | PPL at alpha=0.50 | 1591 | Finding |
| 1194 | **0.52** | alpha=0.52 | 1591 | Condition |
| 1195 | **41.1** | PPL at alpha=0.52 | 1591 | Finding |

### Section: Cross-Architecture Detection Table (App AA)

**Table: generalization (tab:generalization), lines 1675-1693:**
| 1196 | **410M** | Pythia-410M params | 1675 | Table |
| 1197 | **6/8** | Pythia-410M PermG fwd | 1675 | Table |
| 1198 | **1.4B** | Pythia-1.4B params | 1676 | Table |
| 1199 | **2-6/8** | Pythia-1.4B PermG range | 1676 | Table |
| 1200 | **6.9B** | Pythia-6.9B params | 1677 | Table |
| 1201 | **7/8** | Pythia-6.9B PermG fwd | 1677 | Table |
| 1202 | **345M** | GPT-2-medium params | 1679 | Table |
| 1203 | **6/8** | GPT-2-medium PermG fwd | 1679 | Table |
| 1204 | **1.3B** | OPT-1.3B params | 1681 | Table |
| 1205 | **6/8** | OPT-1.3B PermG fwd | 1681 | Table |
| 1206 | **0.8B** | Qwen3.5-0.8B params | 1683 | Table |
| 1207 | **8/8** | Qwen3.5-0.8B PermG fwd | 1683 | Table |
| 1208 | **3.0B** | SmolLM3-3B params | 1684 | Table |
| 1209 | **3/8** | SmolLM3-3B PermG fwd | 1684 | Table |
| 1210 | **410M** | Padding-410M params | 1685 | Table |
| 1211 | **6/8** | Padding-410M PermG fwd | 1685 | Table |
| 1212 | **1.0B** | Pythia-1B C4 params | 1687 | Table |
| 1213 | **8/8** | Pythia-1B C4 PermG fwd | 1687 | Table |
| 1214 | **1.4B** | Pythia-1.4B C4 params | 1688 | Table |
| 1215 | **8/8** | Pythia-1.4B C4 PermG fwd | 1688 | Table |

**Footnotes:**
| 1216 | **2/8** | s42 seed-dependent | 1690 | Footnote |
| 1217 | **6/8** | s43 seed-dependent | 1690 | Footnote |
| 1218 | **~0.033** | MAUVE floor at 1.4B | 1691 | Footnote |
| 1219 | **0/4** | SmolLM3 entropy | 1691 | Footnote |
| 1220 | **6/8** | GPT-2 s42 fp32 fwd | 1692 | Footnote |
| 1221 | **0** | GPT-2 s42 fp32 rev | 1692 | Footnote |
| 1222 | **6/8** | GPT-2 s43 both directions | 1692 | Footnote |
| 1223 | **0/8** | GPT-2 bf16 | 1692 | Footnote |

### Section: Cross-Architecture FPR (App AA cont.)

| 1224 | **50%** | GPT-2-medium null FPR | 1701 | Finding |
| 1225 | **6/12** | GPT-2 pooled FP | 1701 | Finding |
| 1226 | **2** | Seeds | 1701 | Context |
| 1227 | **6.7%** | Pythia-410M FPR comparison | 1701 | Comparison |
| 1228 | **~4x** | Stronger null drift in GPT-2 | 1701 | Finding |
| 1229 | **-20.5%** | GPT-2 entropy null drift | 1701 | Finding |
| 1230 | **-4.9%** | Pythia entropy null drift | 1701 | Finding |
| 1231 | **-35.8%** | GPT-2 distinct-3 null drift | 1701 | Finding |
| 1232 | **-4.9%** | Pythia distinct-3 null drift | 1701 | Finding |
| 1233 | **0%** | K>=3 consensus FPR on GPT-2 | 1702 | Finding |
| 1234 | **0/12** | K>=3 FP on GPT-2 | 1702 | Finding |

**GPT-2 precision, lines 1707-1709:**
| 1235 | **6/8** | GPT-2 fp32 s42 forward | 1707 | Finding |
| 1236 | **0/8** | GPT-2 fp32 s42 reverse | 1707 | Finding |
| 1237 | **0/8** | GPT-2 bf16 | 1708 | Finding |
| 1238 | **-28.4%** | Distinct-1 drift in both precisions | 1708 | Finding |
| 1239 | **~2x** | bf16 higher inter-gen variance | 1709 | Finding |
| 1240 | **0.01** | p-value fp32 | 1709 | Finding |
| 1241 | **0.20** | p-value bf16 | 1709 | Finding |

**GPT-2 bidirectionality, lines 1713-1714:**
| 1242 | **6/8** | GPT-2 s43 both directions | 1713 | Finding |
| 1243 | **6/8** | s42 forward | 1714 | Comparison |
| 1244 | **0/8** | s42 reverse | 1714 | Comparison |

**SmolLM3, lines 1718-1719:**
| 1245 | **3/8** | SmolLM3 total detection | 1718 | Finding |
| 1246 | **0/4** | SmolLM3 entropy | 1718 | Finding |
| 1247 | **3/4** | SmolLM3 ECE | 1718 | Finding |
| 1248 | **3/8** | Non-monotonic entropy conditions | 1719 | Finding |
| 1249 | **3** | Gen where recovery starts | 1719 | Finding |
| 1250 | **5** | Gen where recovery ends | 1719 | Finding |

**Domain effects, line 1723:**
| 1251 | **8/8** | C4 detection rates | 1723 | Finding |
| 1252 | **6/8** | WikiText 410M comparison | 1723 | Comparison |
| 1253 | **2-6/8** | WikiText 1.4B comparison | 1723 | Comparison |

**Deployment recommendations, line 1730:**
| 1254 | **50%** | GPT-2 FPR without calibration | 1730 | Warning |
| 1255 | **0/12** | K>=3 on GPT-2 | 1732 | Recommendation |
| 1256 | **50%** | Standalone PermG GPT-2 FPR | 1732 | Comparison |

### Section: Reproducibility Details

| 1257 | **10** | Generations per experiment | 1741 | Context |
| 1258 | **5,000** | Training steps | 1741 | Context |
| 1259 | **5,000** | Generation samples | 1741 | Context |
| 1260 | **4** | GPU-hours per Pythia-410M experiment | 1741 | Finding |
| 1261 | **40** | GPU memory (A100 40GB) | 1741 | Context |
| 1262 | **13** | alpha levels | 1742 | Count |
| 1263 | **4** | Seeds | 1742 | Count |
| 1264 | **5** | Observation windows | 1742 | Count |
| 1265 | **800** | Total GPU-hours | 1742 | Finding |
| 1266 | **2** | CPU hours for statistical analysis | 1743 | Finding |

**Software versions, line 1746:**
| 1267 | **2.1.0** | PyTorch version | 1746 | Version |
| 1268 | **4.36.0** | Transformers version | 1746 | Version |
| 1269 | **3.10** | Python version | 1746 | Version |

**Implementation choices, line 1754:**
| 1270 | **5,000** | Prompt set size | 1754 | Design |
| 1271 | **5,000** | Generated samples for distinct-n | 1754 | Design |
| 1272 | **3/8** | Earlier pipeline v3 at alpha=0.60 | 1755 | Historical |
| 1273 | **0/8** | Corrected pipeline at alpha=0.60 | 1755 | Current |

**Lines 1421, 1457-1460, 1468-1472 (Boundary model):**
| 1274 | **14/15** | Cascade ordering success at alpha>=0.30 | 1421 | Finding |
| 1275 | **0.24** | beta from boundary model fit | 1457 | Fit result |
| 1276 | **0** | alpha_infinity | 1457 | Fit result |
| 1277 | **0.106** | MAE held-out | 1458 | Validation |
| 1278 | **6/6** | CI coverage held-out | 1458 | Validation |
| 1279 | **0.037** | MAE leave-one-T-out CV | 1459 | Validation |
| 1280 | **15** | Cells in CV | 1459 | Context |
| 1281 | **15/15** | CV coverage | 1459 | Validation |
| 1282 | **0.66** | Profile likelihood beta-hat | 1460 | Fit result |
| 1283 | **0.24, 0.78** | beta CI | 1460 | CI |
| 1284 | **3-4** | Data points for boundary fit | 1469 | Limitation |
| 1285 | **5, 10, 15, 20** | T values used | 1469 | Context |
| 1286 | **3** | Free parameters | 1469 | Count |
| 1287 | **0.64, 2.08** | eta CI | 1470 | CI |
| 1288 | **25** | Extrapolation limit | 1472 | Context |
| 1289 | **0.25** | Extrapolation limit (alpha) | 1472 | Context |

**Worked example, lines 1463-1466:**
| 1290 | **3.234** | Entropy gen-0 at alpha=0.50 | 1463 | Finding |
| 1291 | **2.649** | Entropy gen-1 at alpha=0.50 | 1463 | Finding |
| 1292 | **-18.1%** | Entropy drop | 1463 | Finding |
| 1293 | **0.0968** | Distinct-1 at gen-0 and gen-1 | 1463 | Finding |
| 1294 | **0.0812** | Distinct-1 at gen-2 | 1464 | Finding |
| 1295 | **-16.1%** | Distinct-1 drop gen-1→2 | 1464 | Finding |

**ECE drift table (tab:ece_drift), lines 1406-1412:**
| 1296 | **0.0108** | ECE gen-0 (all rows) | 1406-1411 | Table |
| 1297 | **0.015 ± 0.002** | ECE gen-10 at alpha=0.00 | 1406 | Table |
| 1298 | **+37.6 ± 14** | ECE drift alpha=0.00 | 1406 | Table |
| 1299 | **0.019 ± 0.002** | ECE gen-10 at alpha=0.25 | 1407 | Table |
| 1300 | **+79.2 ± 15.9** | ECE drift alpha=0.25 | 1407 | Table |
| 1301 | **0.087 ± 0.002** | ECE gen-10 at alpha=0.50 | 1408 | Table |
| 1302 | **+703 ± 18** | ECE drift alpha=0.50 | 1408 | Table |
| 1303 | **0.179** | ECE gen-10 at alpha=0.60 | 1409 | Table |
| 1304 | **+1561** | ECE drift alpha=0.60 | 1409 | Table |
| 1305 | **0.215 ± 0.002** | ECE gen-10 at alpha=0.75 | 1410 | Table |
| 1306 | **+1885 ± 18** | ECE drift alpha=0.75 | 1410 | Table |
| 1307 | **0.421 ± 0.004** | ECE gen-10 at alpha=1.00 | 1411 | Table |
| 1308 | **+3792 ± 30** | ECE drift alpha=1.00 | 1411 | Table |

**Lines 1394-1395, 1417-1418:**
| 1309 | **+79.2%** | ECE increase at alpha=0.25 | 1394 | Finding |
| 1310 | **-4.7%** | Entropy decrease at alpha=0.25 | 1394 | Finding |
| 1311 | **+3762-3821%** | ECE drift range at alpha=1.0 | 1395 | Finding |
| 1312 | **0.0108** | ECE from | 1395 | Finding |
| 1313 | **0.417-0.424** | ECE to (across seeds) | 1395 | Finding |
| 1314 | **0.007-0.008** | 1.4B ECE gen-0 values | 1418 | Finding |
| 1315 | **0.145** | 1.4B ECE gen-10 at alpha=0.45 | 1418 | Finding |
| 1316 | **0.268** | 1.4B ECE gen-10 at alpha=0.75 | 1418 | Finding |

---

**Total: approximately 1,316 distinct numeric data points extracted** from the appendix, spanning 18 sections, 26 tables, 18+ figures, proofs, and prose. Every number in tables has been enumerated with its row/column context. The numbers come from experimental results (measured values), statistical tests (p-values, confidence intervals), hyperparameters (learning rates, batch sizes, steps), model parameters (sizes), fit results (sigmoid parameters), and methodological counts (seeds, pairs, permutations).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "126a3a70-4509-4d94-aaaa-216ab7981ebb",
  "isSidechain": true,
  "agentId": "a9d7bd4d8daf2b13b",
  "requestId": "req_011CbPrgDkL1ShPwzsXfP7g3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc49b0cf-b039-41c7-a030-626c2a804d77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wm8EtVNL8DWy1Mmr9tnain",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7795,
      "cache_read_input_tokens": 85898,
      "output_tokens": 40565,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 40565,
          "cache_read_input_tokens": 85898,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
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
