# Research conversation: Read the following LaTeX files from a research paper and extract EVERY number that appears (including percentages, count

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a5ed021f86aec5f66.jsonl`
- **Structured JSON:** [`f688dda075381f1322f8.json`](../../sessions/f6/f688dda075381f1322f8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-25T19:41:22.921Z_

Read the following LaTeX files from a research paper and extract EVERY number that appears (including percentages, counts, dimensions, hyperparameters, statistical values, etc.). For each number, record: (1) the exact number, (2) what it represents, (3) the file and approximate line number, (4) any context about where it claims to come from.

Files to read (read ALL of them fully):
1. /home/ubuntu/.agent-ml-research-idea_gen_0514_4/docs/paper/experiments.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0514_4/docs/paper/discussion.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0514_4/docs/paper/conclusion.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0514_4/docs/paper/limitations.tex

Output a structured list of every number found, grouped by file. Include the surrounding text context for each number. Don't skip any numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a5ed021f86aec5f66",
  "type": "user",
  "uuid": "4af64dd4-d0eb-4a0c-9e99-bea370f172b9",
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

_source line 2 · 2026-05-25T19:41:22.924Z_

```json
{
  "parentUuid": "4af64dd4-d0eb-4a0c-9e99-bea370f172b9",
  "isSidechain": true,
  "agentId": "a5ed021f86aec5f66",
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
  "uuid": "acb5b17f-b2a3-43d2-ab77-8f6e6e300dfa",
  "timestamp": "2026-05-25T19:41:22.924Z",
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

_source line 3 · 2026-05-25T19:41:25.480Z_



I'll read all four files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acb5b17f-b2a3-43d2-ab77-8f6e6e300dfa",
  "isSidechain": true,
  "agentId": "a5ed021f86aec5f66",
  "requestId": "req_011CbPrd6YA9wLp6xoCErt8Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff286586-e3a5-4f59-9ef6-53a3fbce9b12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3QSAwsXk6YZDnjjYHRJJu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34048,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34048,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 4 · 2026-05-25T19:41:25.995Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KJ6YjAybVm9vtVTugjAp41`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff286586-e3a5-4f59-9ef6-53a3fbce9b12",
  "isSidechain": true,
  "agentId": "a5ed021f86aec5f66",
  "requestId": "req_011CbPrd6YA9wLp6xoCErt8Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69504166-3543-4eea-b5ac-b4f32d59e6a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3QSAwsXk6YZDnjjYHRJJu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34048,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34048,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 5 · 2026-05-25T19:41:26.003Z_

<details><summary>↩ Tool result · reported error · `toolu_01KJ6YjAybVm9vtVTugjAp41`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69504166-3543-4eea-b5ac-b4f32d59e6a0",
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a5ed021f86aec5f66",
  "type": "user",
  "uuid": "c0719fb6-3dd9-4da0-9a21-2627972c87c7",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8.",
  "sourceToolAssistantUUID": "69504166-3543-4eea-b5ac-b4f32d59e6a0",
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

_source line 6 · 2026-05-25T19:41:26.446Z_

<details open><summary>🔧 Tool call — Read · `toolu_017a59991xJDaydXyuKqZQFH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0719fb6-3dd9-4da0-9a21-2627972c87c7",
  "isSidechain": true,
  "agentId": "a5ed021f86aec5f66",
  "requestId": "req_011CbPrd6YA9wLp6xoCErt8Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c231924-f268-4e30-8e20-03db3c9b6c19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3QSAwsXk6YZDnjjYHRJJu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34048,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34048,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 7 · 2026-05-25T19:41:26.452Z_

<details><summary>↩ Tool result · reported error · `toolu_017a59991xJDaydXyuKqZQFH`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c231924-f268-4e30-8e20-03db3c9b6c19",
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a5ed021f86aec5f66",
  "type": "user",
  "uuid": "e1fef4b3-19ce-47f7-857d-b0deeb1c8876",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8.",
  "sourceToolAssistantUUID": "1c231924-f268-4e30-8e20-03db3c9b6c19",
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

_source line 8 · 2026-05-25T19:41:26.918Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SoBQmHNSBgTyh1soVPSY2L`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1fef4b3-19ce-47f7-857d-b0deeb1c8876",
  "isSidechain": true,
  "agentId": "a5ed021f86aec5f66",
  "requestId": "req_011CbPrd6YA9wLp6xoCErt8Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6267dc26-c73e-4cd7-882d-3ecd7a44430d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3QSAwsXk6YZDnjjYHRJJu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34048,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34048,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 9 · 2026-05-25T19:41:26.923Z_

<details><summary>↩ Tool result · reported error · `toolu_01SoBQmHNSBgTyh1soVPSY2L`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6267dc26-c73e-4cd7-882d-3ecd7a44430d",
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a5ed021f86aec5f66",
  "type": "user",
  "uuid": "a87765b8-57b8-45b9-b9e9-4afc6f066a2d",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8.",
  "sourceToolAssistantUUID": "6267dc26-c73e-4cd7-882d-3ecd7a44430d",
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

_source line 10 · 2026-05-25T19:41:27.181Z_

<details open><summary>🔧 Tool call — Read · `toolu_011tmbMw63UHiLXcFPQnZ38e`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a87765b8-57b8-45b9-b9e9-4afc6f066a2d",
  "isSidechain": true,
  "agentId": "a5ed021f86aec5f66",
  "requestId": "req_011CbPrd6YA9wLp6xoCErt8Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4781b77f-8ace-480d-b002-112109fd82ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3QSAwsXk6YZDnjjYHRJJu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34048,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34048,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 11 · 2026-05-25T19:41:27.185Z_

<details><summary>↩ Tool result · reported error · `toolu_011tmbMw63UHiLXcFPQnZ38e`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4781b77f-8ace-480d-b002-112109fd82ea",
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a5ed021f86aec5f66",
  "type": "user",
  "uuid": "fcd76351-2826-44d7-930f-e15fb97e3c1d",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8.",
  "sourceToolAssistantUUID": "4781b77f-8ace-480d-b002-112109fd82ea",
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

_source line 12 · 2026-05-25T19:41:29.872Z_

The files aren't at that path. Let me find them.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcd76351-2826-44d7-930f-e15fb97e3c1d",
  "isSidechain": true,
  "agentId": "a5ed021f86aec5f66",
  "requestId": "req_011CbPrdSd9UUqeV8faFMA2G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f23fc72-f80a-4807-a137-8ea785323323",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HE5dN72aCfpBRBkevEZewH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1442,
      "cache_read_input_tokens": 34048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1442,
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

_source line 13 · 2026-05-25T19:41:30.943Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014bZz7Sr8jr3EP6pBJVWBqi`</summary>

```json
{
  "pattern": "**/docs/paper/experiments.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f23fc72-f80a-4807-a137-8ea785323323",
  "isSidechain": true,
  "agentId": "a5ed021f86aec5f66",
  "requestId": "req_011CbPrdSd9UUqeV8faFMA2G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9f3c3e4-3ed2-440a-a96f-0c0c70bdf125",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HE5dN72aCfpBRBkevEZewH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1442,
      "cache_read_input_tokens": 34048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1442,
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

_source line 14 · 2026-05-25T19:41:31.011Z_

<details><summary>↩ Tool result · `toolu_014bZz7Sr8jr3EP6pBJVWBqi`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9f3c3e4-3ed2-440a-a96f-0c0c70bdf125",
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a5ed021f86aec5f66",
  "type": "user",
  "uuid": "d5d01323-32e6-4013-a438-781a507642f2",
  "sourceToolAssistantUUID": "d9f3c3e4-3ed2-440a-a96f-0c0c70bdf125",
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

_source line 15 · 2026-05-25T19:41:31.183Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QvYHEDHHkJkrZKa2gAZ27z`</summary>

```json
{
  "pattern": "**/docs/paper/discussion.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5d01323-32e6-4013-a438-781a507642f2",
  "isSidechain": true,
  "agentId": "a5ed021f86aec5f66",
  "requestId": "req_011CbPrdSd9UUqeV8faFMA2G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "886b9a05-3198-4db9-ae6d-2d3de303789b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HE5dN72aCfpBRBkevEZewH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1442,
      "cache_read_input_tokens": 34048,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1442
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 34048,
          "cache_creation_input_tokens": 1442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1442,
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

_source line 16 · 2026-05-25T19:41:31.258Z_

<details><summary>↩ Tool result · `toolu_01QvYHEDHHkJkrZKa2gAZ27z`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "886b9a05-3198-4db9-ae6d-2d3de303789b",
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a5ed021f86aec5f66",
  "type": "user",
  "uuid": "a6048fdd-668b-4993-a764-c628e1f2fd22",
  "sourceToolAssistantUUID": "886b9a05-3198-4db9-ae6d-2d3de303789b",
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

_source line 17 · 2026-05-25T19:41:33.697Z_

Found them under `projects/distrib_canary_collapse/`. Let me read all four files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6048fdd-668b-4993-a764-c628e1f2fd22",
  "isSidechain": true,
  "agentId": "a5ed021f86aec5f66",
  "requestId": "req_011CbPrdiD1hNhGPdMbm6i41",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39b0377a-f509-4303-a2b2-8f82c8780dc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zwghPTrQrxRQgYFGi3DPs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 320,
      "cache_read_input_tokens": 35490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 320,
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

_source line 18 · 2026-05-25T19:41:34.322Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L4eFUx9kR7GTriKRgrnMXr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39b0377a-f509-4303-a2b2-8f82c8780dc6",
  "isSidechain": true,
  "agentId": "a5ed021f86aec5f66",
  "requestId": "req_011CbPrdiD1hNhGPdMbm6i41",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82274730-9b06-4d68-ac52-e1345fa1dae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zwghPTrQrxRQgYFGi3DPs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 320,
      "cache_read_input_tokens": 35490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 320,
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

### Tool result

_source line 19 · 2026-05-25T19:41:34.327Z_

<details><summary>↩ Tool result · `toolu_01L4eFUx9kR7GTriKRgrnMXr`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study iterative training collapse using Pythia-410M~\citep{biderman2023pythia} as the primary architecture.
8	Training data is drawn from WikiText-103~\citep{merity2017pointer} following the replace paradigm of~\citet{shumailov2024curse}: each generation fine-tunes on a mixture of $\alpha$ synthetic and $(1{-}\alpha)$ real data, generates 5{,}000 replacement samples, and fully replaces the synthetic pool (hyperparameters in Appendix~\ref{app:training_details}).
9	We run $T{=}10$ generations across 13 contamination levels ($\alpha \in \{0.00, \ldots, 1.00\}$) with multi-seed replication, yielding ${\sim}1{,}500$ statistical tests after BH-FDR correction~\citep{benjamini1995controlling}.
10	We track two \emph{canary metrics} (token entropy and ECE) and three \emph{downstream metrics}: distinct-1, distinct-2~\citep{li2016diversity}, and perplexity (distinct-3: Appendix~\ref{app:distinct3}).
11	PermG uses 5{,}000 permutations on first-differenced series~\citep{shojaie2022granger} with maximum lag~5 (power analysis in Appendix~\ref{app:power_analysis}).
12	
13	
14	\subsection{Steep Detection Onset}
15	\label{sec:regime}
16	
17	Diversity collapse occurs at every contamination level: distinct-1 declines by $14.1\%$ even at $\alpha{=}0.0$ (fine-tuning drift) and by $40.3{\pm}0.3\%$ at $\alpha{=}0.25$.
18	Despite this ubiquitous degradation, Granger detectability is strongly regime-dependent.
19	PermG finds 0/8 canary$\to$downstream pairs FDR-significant from $\alpha{=}0.00$ through $\alpha{=}0.45$, then jumps to 6/8 (Clopper--Pearson 95\% CI $[0.25, 0.92]$) at $\alpha{=}0.50$, consistently across all 3~fp32 seeds.
20	
21	This transition is striking because cumulative synthetic fraction barely changes across the boundary ($C{=}99.75\%$ at $\alpha{=}0.45$ vs.\ $99.90\%$ at $\alpha{=}0.50$), yet detection jumps from null to reliable.
22	Sub-threshold $p$-values at $\alpha{=}0.45$ ($p_{\mathrm{fdr}} = 0.059$--$0.091$) confirm proximity to the boundary.
23	Sigmoid regression yields $\alpha_c = 0.483 \pm 0.006$ ($R^2 = 0.969$; Figure~\ref{fig:dose_response}); cross-seed consistency (3/3 seeds: $0/8{\to}6/8$) and specification-invariance across 1{,}160 configurations (Appendix~\ref{app:spec_curve}) argue for a genuine transition (Fisher exact: $p = 3.45 \times 10^{-11}$).
24	
25	First-differencing scopes this canary claim precisely: canary$\to$diversity pairs retain unanimous FDR significance ($24/24 \to 24/24$ across 4~seeds at $\alpha{=}1.0$), while canary$\to$perplexity collapses entirely ($F \approx 0$, $p = 0.99$)~\citep{granger1974spurious}; channel-level effect sizes confirm this dissociation (Appendix~\ref{app:channel_effect_size}).
26	At $\alpha{=}1.0$, all 24 canary$\to$diversity pairs reach FDR significance in the forward direction with 0/24 reverse; entropy onset at generation~1 precedes distinct-$n$ at generation~2 in 16/18 WikiText conditions (Appendix~\ref{app:moment_cascade}).
27	Yet despite this clear signal above onset, a substantial blind zone exists below it: at $\alpha{=}0.10$, distinct-1 has already dropped by $39.6\%$, yet token entropy is indistinguishable from the null; diversity collapse proceeds without any detectable Granger-precedence signal.
28	
29	\begin{table}[t]
30	\centering
31	\caption{Detection outcomes across contamination levels (Pythia-410M, seed~42, $T{=}10$, fp32). PermG: forward FDR-significant pairs; $K{\geq}3$: consensus pairs (of 8 canary$\to$downstream pairs).}
32	\label{tab:summary_detection}
33	\begin{tabular}{@{}lccc@{}}
34	\toprule
35	$\alpha$ & PermG & $K{\geq}3$ & Regime \\
36	\midrule
37	0.00 & 0/8 & 0/8 & null \\
38	0.25 & 0/8 & 0/8 & blind \\
39	0.45 & 0/8 & 0/8 & blind \\
40	0.50 & 6/8 & 6/8 & onset \\
41	0.60 & 0/8 & 0/8 & anomaly \\
42	0.75 & 6/8 & 6/8 & detection \\
43	1.00 & 6/8 & 6/8 & detection \\
44	\bottomrule
45	\end{tabular}
46	\end{table}
47	
48	\subsection{Dose-Response and Detection Regimes}
49	\label{sec:dose_response}
50	
51	\begin{figure}[t]
52	\centering
53	\includegraphics[width=\columnwidth]{figures/fig_dose_response.pdf}
54	\caption{Dose-response: PermG detection rate with sigmoid fit ($\alpha_c{=}0.483$; shaded 95\% CI). Regime bands mark blind, onset, sync-dip, and detection zones.}
55	\label{fig:dose_response}
56	\end{figure}
57	
58	The PermG dose-response profile (Figure~\ref{fig:dose_response}; Appendix~\ref{app:dose_response}) reveals three confirmed regimes: \emph{blind} ($\alpha \leq 0.45$, 0/8), \emph{onset} ($\alpha \approx 0.50$, 6/8), and \emph{detection} ($\alpha{\geq}0.75$, 6/8), plus a non-monotonic anomaly at $\alpha \approx 0.60$ (0/8).
59	The blind zone exhibits zero detection across all seeds and methods below $\alpha{=}0.45$, despite substantial diversity loss, a regime where collapse proceeds silently (a perplexity-threshold baseline also fails; Appendix~\ref{app:ppl_threshold}).
60	Onset is remarkably steep: the sigmoid Hill coefficient $k{=}15.7$ implies that 80\% of the detection transition occurs within $\Delta\alpha{\approx}0.05$ (transition width analysis in Appendix~\ref{app:sigmoid_shape}), approximately $3$--$4{\times}$ steeper than smooth-signal predictions (Appendix~\ref{app:power_sim}).
61	Above onset, the detection zone shows cross-seed consistency: all 3~fp32 seeds independently reach 6/8 at $\alpha{=}0.50$ and $\alpha{\geq}0.75$.
62	
63	At $\alpha{\approx}0.60$, all direction-checked methods fail (PermG 0/8, threshold onset 0/8, Toda--Yamamoto 1/8), while bidirectional DiffXCorr maintains detection (6/8).
64	This pattern suggests that at intermediate contamination, entropy and diversity respond near-simultaneously, compressing the temporal lag below PermG's resolution at $T{=}10$.
65	The anomaly dissolves by $T{=}25$ ($5/8$), consistent with $\sqrt{T}$ power scaling restoring directional separation as additional observations accumulate (Appendix~\ref{app:t20_comparison}).
66	
67	\subsection{Detection Boundary Left-Shift}
68	\label{sec:t20}
69	
70	Longer observation windows push the detection boundary leftward: $\alpha_c(5){\geq}1.0$, $\alpha_c(10){=}0.487$, consistent with power-law scaling $\alpha_c(T) \propto T^{-\eta}$ (\S\ref{sec:theory}).
71	Profile likelihood yields $\eta \in [0.64, 2.08]$ (95\% CI), confirming that detection improves with longer observation regardless of the specific exponent.
72	The mechanism is statistical power accumulation: each additional generation provides one more data point for the permutation test, and the signal-to-noise ratio grows as $\sqrt{T}$, progressively resolving weaker contamination signals.
73	The $\alpha{=}0.45$ column validates this prediction directly: undetectable at $T{\leq}10$ (0/8), it crosses into reliable detection at $T{=}15$ (6/8, dual-seed) and remains stable at $T{=}20$ (5/8) and $T{=}25$ (6/8), precisely traversing the blind$\to$detection boundary as the theory predicts.
74	
75	
76	\subsection{Cross-Architecture Evaluation at $\alpha{=}1.0$}
77	\label{sec:generalization}
78	
79	The phase diagram (Figure~\ref{fig:phase_diagram}) characterizes detectability on Pythia-410M + WikiText-103; this section tests whether the detection signal generalizes across architectures at the most favorable contamination level ($\alpha{=}1.0$).
80	We evaluate PermG across 15 model-seed combinations spanning five families (345M--6.9B) and two domains (Table~\ref{tab:generalization}; Appendix~\ref{app:cross_arch_table}).
81	Forward detection reaches ${\geq}6/8$ in 11/15 conditions (Figure~\ref{fig:cross_arch_heatmap}).
82	
83	At larger scale, Pythia-1.4B qualitatively reproduces the 410M phase-diagram structure (detection boundary at $\alpha_c{\approx}0.50$, cross-$T$ improvement at 3/4 $\alpha$ values ($\alpha{=}0.45$: $0/6{\to}5/6$ from $T{=}10$ to $T{=}15$)), though the 410M sync-dip at $\alpha{=}0.60$ does not appear (4/6 at $T{=}10$), suggesting the anomaly is architecture-specific.
84	The four non-confirming conditions each isolate a distinct PermG assumption violation.
85	\emph{Precision sensitivity}: GPT-2 bf16 yields 0/8 vs.\ fp32 6/8, traced to bf16 quantization noise masking the entropy signal.
86	\emph{Bidirectional confounding}: GPT-2 s43 detects 6/8 in both forward and reverse directions, preventing directional assignment.
87	\emph{Seed dependence}: Pythia-1.4B shows s42 2/8 vs.\ s43 6/8; seed-specific bidirectional confounding also appears at 1.4B (s43 reverse detection 6/8 at $\alpha{=}0.60$), analogous to the GPT-2 case, preventing directional assignment for that seed.
88	\emph{Entropy decoupling}: SmolLM3-3B reaches only 3/8, with ECE-only detection (entropy 0/4), violating the entropy-leads assumption of Observation~\ref{thm:entropy_leads}.
89	Standalone PermG claims therefore require architecture-specific null calibration; GPT-2 null FPR reaches 50\% (Appendix~\ref{app:fpr_independence}; per-architecture breakdown in Appendix~\ref{app:cross_arch_fpr}), driven by ${\sim}4{\times}$ stronger null drift than Pythia.
90	
91	\begin{figure}[t]
92	\centering
93	\includegraphics[width=\columnwidth]{figures/fig_cross_arch_heatmap.pdf}
94	\caption{Cross-architecture validation ($\alpha{=}1.0$): PermG forward detection (${\geq}6/8$) in 11/15 model-seed conditions spanning five families (345M--6.9B); faded bars: non-confirming conditions.}
95	\label{fig:cross_arch_heatmap}
96	\end{figure}
97	
98	
99	\subsection{Canary-Based Intervention (Proof of Concept)}
100	\label{sec:intervention}
101	
102	As a proof-of-concept under favorable conditions ($\alpha{=}1.0$), we implement predictive cessation: training switches to pure real data when token entropy drops beyond a 15\% threshold from generation~0 (robust band $[10\%, 22\%]$; Appendix~\ref{app:intervention_sensitivity}; CUSUM alternative in Appendix~\ref{app:csmp}).
103	The predictive trigger fires at generation~1, one full generation before a reactive baseline that monitors distinct-1 directly (which manifests only at generation~2 due to the cascade lag).
104	Predictive cessation caps peak perplexity at $56.99$ vs.\ $157.09$ reactive, a 64\% reduction (Figure~\ref{fig:intervention}); the result replicates on Pythia-1.4B with comparable effect size (Appendix~\ref{app:extended_discussion}).
105	
106	\begin{table}[t]
107	\centering
108	\caption{Consensus threshold operating characteristics ($K \in \{2,3,4,5\}$). FPR: null-control rate (10~seeds, 60~pairs; $K{\geq}2$ uses 9-seed estimate). TPR: detection rate at selected $\alpha$ levels (Pythia-410M, $T{=}10$, fp32). $K{=}3$ balances FPR control against detection power (75\% at $\alpha{=}1.0$); $K{=}4$ eliminates false positives but reduces TPR to ${\leq}25\%$.}
109	\label{tab:mmct_k_operating}
110	\begin{tabular}{@{}lcccc@{}}
111	\toprule
112	& $K{\geq}2$ & $K{\geq}3$ & $K{\geq}4$ & $K{=}5$ \\
113	\midrule
114	FPR ($\alpha{=}0.0$) & 38.9\% & 10.0\% & 0\% & 0\% \\
115	TPR ($\alpha{=}0.50$) & 85.4\% & 66.7\% & 25.0\% & 4.2\% \\
116	TPR ($\alpha{=}0.75$) & 72.9\% & 37.5\% & 0\% & 0\% \\
117	TPR ($\alpha{=}1.0$) & 75.0\% & 75.0\% & 25.0\% & 0\% \\
118	\bottomrule
119	\end{tabular}
120	\end{table}
121	
122	\begin{figure*}[t]
123	\centering
124	\includegraphics[width=\textwidth]{figures/fig_intervention.pdf}
125	\caption{Canary-triggered intervention (Pythia-410M, $\alpha{=}1.0$). Predictive cessation on entropy (generation~1) reduces peak perplexity by 64\% versus reactive triggering on distinct-1 (generation~2).}
126	\label{fig:intervention}
127	\end{figure*}
128	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82274730-9b06-4d68-ac52-e1345fa1dae0",
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a5ed021f86aec5f66",
  "type": "user",
  "uuid": "1437a686-9a11-4bc3-b29a-c5beb63054fa",
  "sourceToolAssistantUUID": "82274730-9b06-4d68-ac52-e1345fa1dae0",
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

_source line 20 · 2026-05-25T19:41:34.641Z_

<details open><summary>🔧 Tool call — Read · `toolu_018u1dy9PCh3mDEnkixjXQCn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1437a686-9a11-4bc3-b29a-c5beb63054fa",
  "isSidechain": true,
  "agentId": "a5ed021f86aec5f66",
  "requestId": "req_011CbPrdiD1hNhGPdMbm6i41",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4eef3d72-2059-4567-a9a0-35746d255f20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zwghPTrQrxRQgYFGi3DPs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 320,
      "cache_read_input_tokens": 35490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 320,
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

### Tool result

_source line 21 · 2026-05-25T19:41:34.647Z_

<details><summary>↩ Tool result · `toolu_018u1dy9PCh3mDEnkixjXQCn`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	Our Granger-precedence claim is scoped to temporal predictive improvement~\citep{granger1969investigating,shojaie2022granger}: bivariate tests cannot exclude confounders, and the FPR CI ($[1.8\%, 16.2\%]$) means Type~I error may be non-negligible.
4	Four of fifteen cross-architecture conditions do not confirm forward detection (\S\ref{sec:generalization}), each isolating a distinct PermG assumption violation: precision sensitivity (GPT-2 bf16), bidirectional confounding (GPT-2 s43), seed dependence (Pythia-1.4B), and entropy decoupling (SmolLM3-3B), requiring architecture-specific null calibration before deployment (Appendix~\ref{app:extended_discussion}).
5	More broadly, our observation sequences ($T{=}10$--$25$) are far shorter than econometric standards ($T{\geq}100$); permutation testing avoids asymptotic assumptions but cannot recover power lost to short samples~\citep{shojaie2022granger}; AR(1) simulation confirms first-differencing controls size at these lengths (Appendix~\ref{app:nonstationarity}).
6	Bivariate tests are susceptible to omitted variable bias (first-differencing removes shared linear trends but nonlinear confounds remain possible), and PermG tests linear precedence only; transfer entropy (Appendix~\ref{app:transfer_entropy}) yields 0/192 significant pairs.
7	Partial correlation provides supporting evidence: after controlling for generation number, contemporaneous associations weaken ($\bar{|r|}$: $0.590{\to}0.381$) while lagged correlations strengthen ($0.759{\to}0.841$), consistent with genuine temporal precedence rather than shared-trend artifacts (Appendix~\ref{app:mi_analysis}).
8	
9	Despite these individual limitations, the five methods exhibit complementary strengths.
10	Shapley value decomposition over all $2^5{=}32$ coalitions (Appendix~\ref{app:shapley}) shows DiffXCorr achieving the best combined Shapley contribution ($-0.299$) by detecting bidirectional coupling that directional methods miss, while PermG ranks best among directional methods ($-0.141$).
11	This complementarity provides analytical value, though consensus voting does not uniformly outperform the best single method: $K{\geq}3$ FPR (10.0\%) exceeds standalone PermG (6.7\%), and practitioners deploying MMCT must calibrate $K$ on architecture-specific null-control data, as the single viable operating point ($K{=}3$) reflects the specific method set and FPR profile of our five-method ensemble.
12	One remaining puzzle is the non-monotonic detection gap at $\alpha{=}0.60$ (\S\ref{sec:dose_response}): consistent across seeds (0/8 for both tested seeds; Appendix~\ref{app:alpha060}), it affects all directional methods while bidirectional DiffXCorr maintains detection, suggesting temporal lag compression defeats directional separation; recovery at $T{=}25$ (5/8) is consistent with $\sqrt{T}$ power scaling.
13	
14	A related concern is whether entropy's ``leading'' behavior partly reflects measurement-resolution asymmetry (entropy is continuous; distinct-$n$ is discrete) rather than genuine temporal precedence.
15	Discretized entropy testing shows that Granger significance is largely recovered at ${\geq}15$~bins (6--7/7 depending on binning method) but degrades under aggressive quantization (0/7 at 5~equal-frequency bins), consistent with measurement resolution contributing to but not solely explaining the temporal precedence signal (Appendix~\ref{app:discretized_entropy}).
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4eef3d72-2059-4567-a9a0-35746d255f20",
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a5ed021f86aec5f66",
  "type": "user",
  "uuid": "ccbcbd54-1d05-4548-8672-19ba2731bfa9",
  "sourceToolAssistantUUID": "4eef3d72-2059-4567-a9a0-35746d255f20",
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

_source line 22 · 2026-05-25T19:41:35.631Z_

<details open><summary>🔧 Tool call — Read · `toolu_013ZRhUxMKNkvJc4fBEbBpMg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccbcbd54-1d05-4548-8672-19ba2731bfa9",
  "isSidechain": true,
  "agentId": "a5ed021f86aec5f66",
  "requestId": "req_011CbPrdiD1hNhGPdMbm6i41",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c78e0680-3e90-46bd-acef-7c14fcc2a0a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zwghPTrQrxRQgYFGi3DPs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 320,
      "cache_read_input_tokens": 35490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 320,
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

### Tool result

_source line 23 · 2026-05-25T19:41:35.643Z_

<details><summary>↩ Tool result · `toolu_013ZRhUxMKNkvJc4fBEbBpMg`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Iterative training collapse exhibits a steep detection onset: PermG detection jumps from 0/8 to 6/8 significant pairs (95\% CI $[0.25, 0.92]$) within 2~percentage points of $\alpha_c \approx 0.50$, organizing three regimes (blind, onset, detection) that characterize when statistical monitoring can and cannot succeed.
5	The detection boundary shifts leftward with longer observation ($\alpha_c(T) \propto T^{-\eta}$), and systematic method comparison reveals that single-method analyses are unreliable: null-control FPR spans 6.7\% (PermG; 95\% CI $[1.8\%, 16.2\%]$, 10~seeds) to 94.4\%.
6	Token entropy exhibits robust one-generation-ahead precedence over diversity collapse (24/24 forward, 0/24 reverse at $\alpha{=}1.0$; ${\geq}6/8$ in 11/15 cross-architecture conditions at $\alpha{=}1.0$).
7	The blind zone below $\alpha_c$ constrains practical deployment to settings with sufficient contamination; evaluation at ${>}$7B parameters remains open.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c78e0680-3e90-46bd-acef-7c14fcc2a0a3",
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a5ed021f86aec5f66",
  "type": "user",
  "uuid": "1f1cb494-2314-4067-a04c-9991ae6ac5ce",
  "sourceToolAssistantUUID": "c78e0680-3e90-46bd-acef-7c14fcc2a0a3",
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

_source line 24 · 2026-05-25T19:41:35.735Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BbXgxbkZxLYa2eyLTJ9JPN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f1cb494-2314-4067-a04c-9991ae6ac5ce",
  "isSidechain": true,
  "agentId": "a5ed021f86aec5f66",
  "requestId": "req_011CbPrdiD1hNhGPdMbm6i41",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22c3de23-025d-44e0-ad69-8b61cb211323",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zwghPTrQrxRQgYFGi3DPs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 320,
      "cache_read_input_tokens": 35490,
      "output_tokens": 328,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 320
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 328,
          "cache_read_input_tokens": 35490,
          "cache_creation_input_tokens": 320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 320,
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

_source line 25 · 2026-05-25T19:41:35.740Z_

<details><summary>↩ Tool result · `toolu_01BbXgxbkZxLYa2eyLTJ9JPN`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Scope.}
5	The phase diagram is built on Pythia-410M with full-replacement contamination and a single decoding strategy; frontier-scale models (${>}$7B) and partial-replacement regimes remain untested.
6	
7	\paragraph{Statistical power.}
8	Per-condition detection rates rest on 8 seeds, yielding wide binomial CIs (e.g., $[0.25, 0.92]$ for 6/8); the 3-seed phase diagram provides a coarse topology rather than precise probability estimates.
9	
10	\paragraph{Causal interpretation.}
11	Permutation Granger testing establishes temporal precedence, not causation, and our short-sequence regime ($T{\leq}25$) limits statistical power relative to econometric standards ($T{\geq}100$).
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22c3de23-025d-44e0-ad69-8b61cb211323",
  "isSidechain": true,
  "promptId": "7e8ce680-d9bd-4b09-bdac-b1053afbfbf5",
  "agentId": "a5ed021f86aec5f66",
  "type": "user",
  "uuid": "1e5f671e-1b59-4691-9762-1667bcc0d538",
  "sourceToolAssistantUUID": "22c3de23-025d-44e0-ad69-8b61cb211323",
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

_source line 26 · 2026-05-25T19:43:52.872Z_

Here is the complete extraction of every number from all four files, grouped by file.

---

## FILE 1: experiments.tex

### Line 7
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 1 | **410M** | Model parameter count (Pythia-410M) | "Pythia-410M as the primary architecture" |

### Line 8
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 2 | **103** | Dataset identifier (WikiText-103) | "WikiText-103" |
| 3 | **5,000** | Number of replacement samples generated per generation | "generates 5,000 replacement samples" |

### Line 9
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 4 | **10** | Number of training generations ($T=10$) | "$T=10$ generations" |
| 5 | **13** | Number of contamination levels tested | "13 contamination levels" |
| 6 | **0.00** | Lower bound of contamination range ($\alpha$) | "$\alpha \in \{0.00, \ldots, 1.00\}$" |
| 7 | **1.00** | Upper bound of contamination range ($\alpha$) | "$\alpha \in \{0.00, \ldots, 1.00\}$" |
| 8 | **~1,500** | Number of statistical tests after BH-FDR correction | "yielding $\sim$1,500 statistical tests" |

### Line 10
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 9 | **1** | Metric identifier (distinct-1) | "distinct-1" |
| 10 | **2** | Metric identifier (distinct-2) | "distinct-2" |
| 11 | **3** | Metric identifier (distinct-3 in appendix) | "distinct-3: Appendix" |

### Line 11
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 12 | **5,000** | Number of permutations for PermG | "5,000 permutations" |
| 13 | **5** | Maximum lag for PermG | "maximum lag 5" |

### Line 17
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 14 | **14.1%** | Distinct-1 decline at alpha=0.0 (fine-tuning drift) | "distinct-1 declines by 14.1% even at alpha=0.0" |
| 15 | **0.0** | Contamination level (alpha=0.0) | "at $\alpha=0.0$" |
| 16 | **40.3%** | Distinct-1 decline at alpha=0.25 (mean) | "40.3 +/- 0.3% at alpha=0.25" |
| 17 | **0.3%** | Standard error on distinct-1 decline | "$\pm 0.3\%$" |
| 18 | **0.25** | Contamination level (alpha=0.25) | "at $\alpha=0.25$" |

### Line 19
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 19 | **0/8** | PermG FDR-significant pairs from alpha=0.00-0.45 | "0/8 canary-to-downstream pairs FDR-significant" |
| 20 | **8** | Total canary-to-downstream pairs tested | denominator in "0/8" |
| 21 | **0.00** | Lower alpha boundary (no detection) | "from $\alpha=0.00$" |
| 22 | **0.45** | Upper alpha boundary (no detection) | "through $\alpha=0.45$" |
| 23 | **6/8** | Detected pairs at alpha=0.50 | "jumps to 6/8" |
| 24 | **95%** | Confidence interval level (Clopper-Pearson) | "Clopper-Pearson 95% CI" |
| 25 | **0.25** | Lower bound of CI for 6/8 detection | "CI [0.25, 0.92]" |
| 26 | **0.92** | Upper bound of CI for 6/8 detection | "CI [0.25, 0.92]" |
| 27 | **0.50** | Contamination level at onset | "at $\alpha=0.50$" |
| 28 | **3** | Number of fp32 seeds showing consistency | "all 3 fp32 seeds" |

### Line 21
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 29 | **99.75%** | Cumulative synthetic fraction at alpha=0.45 | "$C=99.75\%$ at $\alpha=0.45$" |
| 30 | **0.45** | Alpha value | "at $\alpha=0.45$" |
| 31 | **99.90%** | Cumulative synthetic fraction at alpha=0.50 | "$99.90\%$ at $\alpha=0.50$" |
| 32 | **0.50** | Alpha value | "at $\alpha=0.50$" |

### Line 22
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 33 | **0.45** | Alpha value for sub-threshold p-values | "at $\alpha=0.45$" |
| 34 | **0.059** | Lower bound of sub-threshold p_fdr range | "$p_{\mathrm{fdr}} = 0.059$" |
| 35 | **0.091** | Upper bound of sub-threshold p_fdr range | "$0.091$" |

### Line 23
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 36 | **0.483** | Sigmoid regression midpoint (alpha_c) | "$\alpha_c = 0.483$" |
| 37 | **0.006** | Standard error on alpha_c | "$\pm 0.006$" |
| 38 | **0.969** | R-squared of sigmoid fit | "$R^2 = 0.969$" |
| 39 | **3** | Number of seeds showing cross-seed consistency (3/3) | "3/3 seeds" |
| 40 | **0/8** | Detection before transition | "$0/8 \to 6/8$" |
| 41 | **6/8** | Detection after transition | "$0/8 \to 6/8$" |
| 42 | **1,160** | Number of specification-curve configurations | "1,160 configurations" |
| 43 | **3.45 x 10^-11** | Fisher exact test p-value | "$p = 3.45 \times 10^{-11}$" |

### Line 25
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 44 | **24/24** | Forward FDR-significant canary-to-diversity pairs | "$24/24 \to 24/24$ across 4 seeds" |
| 45 | **4** | Number of seeds | "4 seeds" |
| 46 | **1.0** | Alpha value | "at $\alpha=1.0$" |
| 47 | **0** | F-statistic for canary-to-perplexity (approximately zero) | "$F \approx 0$" |
| 48 | **0.99** | p-value for canary-to-perplexity | "$p = 0.99$" |

### Line 26
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 49 | **1.0** | Alpha value | "At $\alpha=1.0$" |
| 50 | **24** | All canary-to-diversity pairs reaching FDR significance (forward) | "all 24 canary-to-diversity pairs" |
| 51 | **0/24** | Reverse direction significant pairs | "0/24 reverse" |
| 52 | **1** | Generation number (entropy onset) | "entropy onset at generation 1" |
| 53 | **2** | Generation number (distinct-n onset) | "distinct-n at generation 2" |
| 54 | **16/18** | WikiText conditions where entropy precedes distinct-n | "16/18 WikiText conditions" |

### Line 27
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 55 | **0.10** | Alpha value | "at $\alpha=0.10$" |
| 56 | **39.6%** | Distinct-1 drop at alpha=0.10 | "distinct-1 has already dropped by 39.6%" |

### Line 31 (Table caption)
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 57 | **42** | Seed number | "seed 42" |
| 58 | **10** | Number of generations | "$T=10$" |
| 59 | **8** | Total canary-to-downstream pairs | "of 8 canary-to-downstream pairs" |

### Lines 37-43 (Table~\ref{tab:summary_detection})
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 60 | **0.00** | Alpha row | Table row |
| 61 | **0/8** | PermG at alpha=0.00 | Table cell |
| 62 | **0/8** | K>=3 at alpha=0.00 | Table cell |
| 63 | **0.25** | Alpha row | Table row |
| 64 | **0/8** | PermG at alpha=0.25 | Table cell |
| 65 | **0/8** | K>=3 at alpha=0.25 | Table cell |
| 66 | **0.45** | Alpha row | Table row |
| 67 | **0/8** | PermG at alpha=0.45 | Table cell |
| 68 | **0/8** | K>=3 at alpha=0.45 | Table cell |
| 69 | **0.50** | Alpha row | Table row |
| 70 | **6/8** | PermG at alpha=0.50 | Table cell |
| 71 | **6/8** | K>=3 at alpha=0.50 | Table cell |
| 72 | **0.60** | Alpha row | Table row |
| 73 | **0/8** | PermG at alpha=0.60 | Table cell |
| 74 | **0/8** | K>=3 at alpha=0.60 | Table cell |
| 75 | **0.75** | Alpha row | Table row |
| 76 | **6/8** | PermG at alpha=0.75 | Table cell |
| 77 | **6/8** | K>=3 at alpha=0.75 | Table cell |
| 78 | **1.00** | Alpha row | Table row |
| 79 | **6/8** | PermG at alpha=1.00 | Table cell |
| 80 | **6/8** | K>=3 at alpha=1.00 | Table cell |

### Line 54 (Figure caption)
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 81 | **0.483** | Sigmoid alpha_c in figure caption | "$\alpha_c=0.483$" |
| 82 | **95%** | CI level in caption | "shaded 95% CI" |

### Line 58
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 83 | **0.45** | Upper bound of blind regime | "$\alpha \leq 0.45$" |
| 84 | **0/8** | Detection in blind regime | "0/8" |
| 85 | **0.50** | Onset alpha | "$\alpha \approx 0.50$" |
| 86 | **6/8** | Detection at onset | "6/8" |
| 87 | **0.75** | Lower bound of detection regime | "$\alpha \geq 0.75$" |
| 88 | **6/8** | Detection in detection regime | "6/8" |
| 89 | **0.60** | Anomaly alpha | "$\alpha \approx 0.60$" |
| 90 | **0/8** | Detection at anomaly | "0/8" |

### Line 59
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 91 | **0.45** | Alpha below which zero detection observed | "below $\alpha=0.45$" |

### Line 60
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 92 | **15.7** | Sigmoid Hill coefficient (k) | "Hill coefficient $k=15.7$" |
| 93 | **80%** | Fraction of detection transition within narrow alpha window | "80% of the detection transition" |
| 94 | **0.05** | Approximate alpha width of transition | "within $\Delta\alpha \approx 0.05$" |
| 95 | **3--4x** | Steepness compared to smooth-signal predictions | "3--4x steeper" |

### Line 61
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 96 | **3** | Number of fp32 seeds (above onset) | "all 3 fp32 seeds" |
| 97 | **6/8** | Detection at alpha=0.50 | "reach 6/8 at $\alpha=0.50$" |
| 98 | **0.50** | Alpha value | "at $\alpha=0.50$" |
| 99 | **0.75** | Alpha threshold | "$\alpha \geq 0.75$" |

### Line 63
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 100 | **0.60** | Anomaly alpha | "At $\alpha \approx 0.60$" |
| 101 | **0/8** | PermG detection at alpha=0.60 | "PermG 0/8" |
| 102 | **0/8** | Threshold onset detection | "threshold onset 0/8" |
| 103 | **1/8** | Toda-Yamamoto detection | "Toda-Yamamoto 1/8" |
| 104 | **6/8** | DiffXCorr detection (bidirectional) | "DiffXCorr maintains detection (6/8)" |

### Line 64
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 105 | **10** | Number of generations (T=10) | "PermG's resolution at $T=10$" |

### Line 65
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 106 | **25** | Extended generation count | "by $T=25$" |
| 107 | **5/8** | Detection at T=25 | "($5/8$)" |

### Line 70
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 108 | **5** | T value where alpha_c >= 1.0 | "$\alpha_c(5) \geq 1.0$" |
| 109 | **1.0** | Alpha_c at T=5 (lower bound) | "$\alpha_c(5) \geq 1.0$" |
| 110 | **10** | T value | "$\alpha_c(10) = 0.487$" |
| 111 | **0.487** | Alpha_c at T=10 | "$\alpha_c(10) = 0.487$" |

### Line 71
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 112 | **0.64** | Lower bound of eta 95% CI (profile likelihood) | "$\eta \in [0.64, 2.08]$" |
| 113 | **2.08** | Upper bound of eta 95% CI | "$\eta \in [0.64, 2.08]$" |
| 114 | **95%** | CI level | "95% CI" |

### Line 73
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 115 | **0.45** | Alpha column that validates prediction | "$\alpha=0.45$ column" |
| 116 | **10** | T threshold below which undetectable | "$T \leq 10$" |
| 117 | **0/8** | Detection at T<=10 | "(0/8)" |
| 118 | **15** | T value at which detection crosses into reliable | "$T=15$" |
| 119 | **6/8** | Detection at T=15 | "(6/8, dual-seed)" |
| 120 | **20** | T value | "$T=20$" |
| 121 | **5/8** | Detection at T=20 | "(5/8)" |
| 122 | **25** | T value | "$T=25$" |
| 123 | **6/8** | Detection at T=25 | "(6/8)" |

### Line 80
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 124 | **15** | Number of model-seed combinations | "15 model-seed combinations" |
| 125 | **5** | Number of architecture families | "five families" |
| 126 | **345M** | Smallest model size | "345M--6.9B" |
| 127 | **6.9B** | Largest model size | "345M--6.9B" |
| 128 | **2** | Number of domains | "two domains" |

### Line 81
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 129 | **6/8** | Forward detection threshold | "$\geq 6/8$" |
| 130 | **11/15** | Conditions meeting detection threshold | "11/15 conditions" |

### Line 83
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 131 | **1.4B** | Model size (Pythia-1.4B) | "Pythia-1.4B" |
| 132 | **410M** | Reference model size | "410M phase-diagram structure" |
| 133 | **0.50** | Detection boundary alpha_c for 1.4B | "$\alpha_c \approx 0.50$" |
| 134 | **3/4** | Fraction of alpha values showing cross-T improvement | "3/4 $\alpha$ values" |
| 135 | **0.45** | Specific alpha value for improvement example | "$\alpha=0.45$" |
| 136 | **0/6** | Detection at T=10 for 1.4B | "$0/6 \to 5/6$" |
| 137 | **5/6** | Detection at T=15 for 1.4B | "$0/6 \to 5/6$" |
| 138 | **10** | T value | "from $T=10$" |
| 139 | **15** | T value | "to $T=15$" |
| 140 | **0.60** | Alpha for sync-dip anomaly (absent in 1.4B) | "$\alpha=0.60$" |
| 141 | **4/6** | Detection at 1.4B alpha=0.60, T=10 | "4/6 at $T=10$" |
| 142 | **4** | Number of non-confirming conditions | "four non-confirming conditions" |

### Line 85
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 143 | **0/8** | GPT-2 bf16 detection | "GPT-2 bf16 yields 0/8" |
| 144 | **6/8** | GPT-2 fp32 detection | "fp32 6/8" |

### Line 86
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 145 | **6/8** | GPT-2 s43 forward detection | "detects 6/8 in both forward and reverse directions" |

### Line 87
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 146 | **1.4B** | Model size | "Pythia-1.4B" |
| 147 | **2/8** | Pythia-1.4B s42 detection | "s42 2/8" |
| 148 | **6/8** | Pythia-1.4B s43 detection | "s43 6/8" |
| 149 | **6/8** | Reverse detection at 1.4B s43 | "s43 reverse detection 6/8" |
| 150 | **0.60** | Alpha value | "at $\alpha=0.60$" |

### Line 88
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 151 | **3B** | Model size (SmolLM3-3B) | "SmolLM3-3B" |
| 152 | **3/8** | SmolLM3-3B detection total | "reaches only 3/8" |
| 153 | **0/4** | SmolLM3-3B entropy detection (zero) | "entropy 0/4" |

### Line 89
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 154 | **50%** | GPT-2 null FPR | "GPT-2 null FPR reaches 50%" |
| 155 | **~4x** | GPT-2 null drift strength relative to Pythia | "$\sim$4x stronger null drift than Pythia" |

### Line 102
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 156 | **1.0** | Alpha value for intervention | "$\alpha=1.0$" |
| 157 | **15%** | Entropy drop threshold for predictive cessation | "15% threshold from generation 0" |
| 158 | **10%** | Lower bound of robust threshold band | "[10%, 22%]" |
| 159 | **22%** | Upper bound of robust threshold band | "[10%, 22%]" |
| 160 | **0** | Reference generation | "from generation 0" |

### Line 103
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 161 | **1** | Generation when predictive trigger fires | "fires at generation 1" |
| 162 | **1** | Distinct-1 metric referenced | "monitors distinct-1 directly" |
| 163 | **2** | Generation when reactive baseline detects | "manifests only at generation 2" |

### Line 104
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 164 | **56.99** | Peak perplexity with predictive cessation | "caps peak perplexity at 56.99" |
| 165 | **157.09** | Peak perplexity with reactive baseline | "vs. 157.09 reactive" |
| 166 | **64%** | Perplexity reduction | "a 64% reduction" |
| 167 | **1.4B** | Model for replication | "replicates on Pythia-1.4B" |

### Line 108 (Table caption for tab:mmct_k_operating)
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 168 | **2** | Lower K threshold | "$K \in \{2,3,4,5\}$" |
| 169 | **3** | K threshold | "$K \in \{2,3,4,5\}$" |
| 170 | **4** | K threshold | "$K \in \{2,3,4,5\}$" |
| 171 | **5** | Upper K threshold | "$K \in \{2,3,4,5\}$" |
| 172 | **10** | Number of seeds for FPR | "10 seeds" |
| 173 | **60** | Number of pairs for FPR | "60 pairs" |
| 174 | **9** | Number of seeds for K>=2 FPR estimate | "$K \geq 2$ uses 9-seed estimate" |
| 175 | **410M** | Model | "Pythia-410M" |
| 176 | **10** | T value | "$T=10$" |
| 177 | **3** | K value that balances FPR/TPR | "$K=3$ balances FPR" |
| 178 | **75%** | TPR at K=3 for alpha=1.0 | "75% at $\alpha=1.0$" |
| 179 | **1.0** | Alpha | "$\alpha=1.0$" |
| 180 | **4** | K value that eliminates false positives | "$K=4$ eliminates false positives" |
| 181 | **25%** | TPR reduced to at K=4 | "reduces TPR to $\leq 25\%$" |

### Lines 112-118 (Table body for tab:mmct_k_operating)
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 182 | **2** | K threshold column header (K>=2) | Column header |
| 183 | **3** | K threshold column header (K>=3) | Column header |
| 184 | **4** | K threshold column header (K>=4) | Column header |
| 185 | **5** | K threshold column header (K=5) | Column header |
| 186 | **38.9%** | FPR at alpha=0.0, K>=2 | Table cell |
| 187 | **10.0%** | FPR at alpha=0.0, K>=3 | Table cell |
| 188 | **0%** | FPR at alpha=0.0, K>=4 | Table cell |
| 189 | **0%** | FPR at alpha=0.0, K=5 | Table cell |
| 190 | **0.0** | Alpha for FPR row | "$\alpha=0.0$" |
| 191 | **85.4%** | TPR at alpha=0.50, K>=2 | Table cell |
| 192 | **66.7%** | TPR at alpha=0.50, K>=3 | Table cell |
| 193 | **25.0%** | TPR at alpha=0.50, K>=4 | Table cell |
| 194 | **4.2%** | TPR at alpha=0.50, K=5 | Table cell |
| 195 | **0.50** | Alpha for TPR row | "$\alpha=0.50$" |
| 196 | **72.9%** | TPR at alpha=0.75, K>=2 | Table cell |
| 197 | **37.5%** | TPR at alpha=0.75, K>=3 | Table cell |
| 198 | **0%** | TPR at alpha=0.75, K>=4 | Table cell |
| 199 | **0%** | TPR at alpha=0.75, K=5 | Table cell |
| 200 | **0.75** | Alpha for TPR row | "$\alpha=0.75$" |
| 201 | **75.0%** | TPR at alpha=1.0, K>=2 | Table cell |
| 202 | **75.0%** | TPR at alpha=1.0, K>=3 | Table cell |
| 203 | **25.0%** | TPR at alpha=1.0, K>=4 | Table cell |
| 204 | **0%** | TPR at alpha=1.0, K=5 | Table cell |
| 205 | **1.0** | Alpha for TPR row | "$\alpha=1.0$" |

### Line 125 (Figure caption)
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 206 | **410M** | Model in caption | "Pythia-410M" |
| 207 | **1.0** | Alpha in caption | "$\alpha=1.0$" |
| 208 | **1** | Generation for predictive cessation | "generation 1" |
| 209 | **64%** | Perplexity reduction in caption | "reduces peak perplexity by 64%" |
| 210 | **1** | Distinct-1 in caption | "distinct-1" |
| 211 | **2** | Generation for reactive trigger | "generation 2" |

---

## FILE 2: discussion.tex

### Line 3
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 212 | **1.8%** | Lower bound of FPR CI | "FPR CI ($[1.8\%, 16.2\%]$)" |
| 213 | **16.2%** | Upper bound of FPR CI | "FPR CI ($[1.8\%, 16.2\%]$)" |

### Line 4
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 214 | **4** (of fifteen) | Non-confirming cross-architecture conditions | "Four of fifteen cross-architecture conditions" |
| 215 | **15** (fifteen) | Total cross-architecture conditions | "of fifteen cross-architecture conditions" |

### Line 5
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 216 | **10** | Lower bound of observation sequence length | "$T=10$" |
| 217 | **25** | Upper bound of observation sequence length | "$T=25$" |
| 218 | **100** | Econometric standard minimum T | "$T \geq 100$" |
| 219 | **1** | AR(1) model order | "AR(1) simulation" |

### Line 6
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 220 | **0/192** | Transfer entropy significant pairs | "yields 0/192 significant pairs" |
| 221 | **192** | Total transfer entropy pairs tested | denominator in "0/192" |

### Line 7
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 222 | **0.590** | Mean absolute partial correlation (before controlling) | "$\bar{|r|}$: 0.590" |
| 223 | **0.381** | Mean absolute partial correlation (after controlling for generation number) | "$\to 0.381$" |
| 224 | **0.759** | Lagged correlation (before controlling) | "0.759" |
| 225 | **0.841** | Lagged correlation (after controlling) | "$\to 0.841$" |

### Line 10
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 226 | **5** | Number of methods | "five methods" |
| 227 | **2^5 = 32** | Number of Shapley coalitions | "$2^5 = 32$ coalitions" |
| 228 | **-0.299** | DiffXCorr Shapley contribution (best combined) | "best combined Shapley contribution ($-0.299$)" |
| 229 | **-0.141** | PermG Shapley contribution (best directional) | "PermG ranks best among directional methods ($-0.141$)" |

### Line 11
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 230 | **3** | K threshold for consensus | "$K \geq 3$" |
| 231 | **10.0%** | K>=3 FPR | "$K \geq 3$ FPR (10.0%)" |
| 232 | **6.7%** | Standalone PermG FPR | "standalone PermG (6.7%)" |
| 233 | **3** | Single viable K operating point | "single viable operating point ($K=3$)" |
| 234 | **5** | Number of methods in ensemble | "five-method ensemble" |

### Line 12
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 235 | **0.60** | Non-monotonic anomaly alpha | "$\alpha=0.60$" |
| 236 | **0/8** | Detection at anomaly (both seeds) | "0/8 for both tested seeds" |
| 237 | **25** | T at which anomaly recovers | "$T=25$" |
| 238 | **5/8** | Detection at T=25 | "recovery at $T=25$ (5/8)" |

### Line 15
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 239 | **15** | Minimum bins for Granger significance recovery | "$\geq 15$ bins" |
| 240 | **6--7/7** | Significance recovered at >=15 bins | "6--7/7 depending on binning method" |
| 241 | **7** | Total tests | denominator in "6--7/7" |
| 242 | **0/7** | Significance under aggressive quantization | "0/7 at 5 equal-frequency bins" |
| 243 | **5** | Number of equal-frequency bins (aggressive quantization) | "5 equal-frequency bins" |

---

## FILE 3: conclusion.tex

### Line 4
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 244 | **0/8** | Detection before onset | "jumps from 0/8 to 6/8" |
| 245 | **6/8** | Detection after onset | "to 6/8 significant pairs" |
| 246 | **95%** | CI level | "95% CI" |
| 247 | **0.25** | Lower CI bound | "$[0.25, 0.92]$" |
| 248 | **0.92** | Upper CI bound | "$[0.25, 0.92]$" |
| 249 | **2** | Percentage points within which transition occurs | "within 2 percentage points" |
| 250 | **0.50** | Alpha_c approximate value | "$\alpha_c \approx 0.50$" |
| 251 | **3** (three) | Number of regimes | "three regimes" |

### Line 5
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 252 | **6.7%** | PermG null-control FPR | "6.7% (PermG)" |
| 253 | **1.8%** | Lower CI for PermG FPR | "95% CI $[1.8\%, 16.2\%]$" |
| 254 | **16.2%** | Upper CI for PermG FPR | "$16.2\%$" |
| 255 | **10** | Number of seeds for FPR | "10 seeds" |
| 256 | **94.4%** | Maximum FPR across methods | "to 94.4%" |

### Line 6
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 257 | **1** (one-generation-ahead) | Temporal precedence lag | "one-generation-ahead precedence" |
| 258 | **24/24** | Forward significant pairs | "24/24 forward" |
| 259 | **0/24** | Reverse significant pairs | "0/24 reverse" |
| 260 | **1.0** | Alpha value | "at $\alpha=1.0$" |
| 261 | **6/8** | Cross-architecture detection threshold | "$\geq 6/8$" |
| 262 | **11/15** | Cross-architecture conditions meeting threshold | "11/15 cross-architecture conditions" |
| 263 | **1.0** | Alpha value for cross-arch | "at $\alpha=1.0$" |

### Line 7
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 264 | **7B** | Model size threshold (untested) | "${>}7B$ parameters remains open" |

---

## FILE 4: limitations.tex

### Line 5
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 265 | **410M** | Model size (scope limitation) | "Pythia-410M" |
| 266 | **7B** | Untested frontier scale threshold | "${>}7B$" |
| 267 | **1** (single) | Number of decoding strategies | "a single decoding strategy" |

### Line 8
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 268 | **8** | Number of seeds per condition | "8 seeds" |
| 269 | **0.25** | Lower CI bound for 6/8 | "$[0.25, 0.92]$" |
| 270 | **0.92** | Upper CI bound for 6/8 | "$[0.25, 0.92]$" |
| 271 | **6/8** | Detection result referenced | "for 6/8" |
| 272 | **3** | Number of seeds for phase diagram | "3-seed phase diagram" |

### Line 11
| # | Number | Represents | Context |
|---|--------|-----------|---------|
| 273 | **25** | Maximum T in this study | "$T \leq 25$" |
| 274 | **100** | Econometric standard minimum T | "$T \geq 100$" |

---

## SUMMARY STATISTICS

- **experiments.tex**: 211 number instances (lines 7-127)
- **discussion.tex**: 32 number instances (lines 1-16)
- **conclusion.tex**: 21 number instances (lines 1-7)
- **limitations.tex**: 10 number instances (lines 1-11)
- **Total unique number extractions**: 274

Key recurring numbers that appear across multiple files (potential cross-consistency checkpoints):
- **6/8** detection at onset/detection regime -- appears in all 4 files
- **0.25, 0.92** CI bounds for 6/8 -- appears in experiments, conclusion, limitations
- **1.8%, 16.2%** FPR CI bounds -- appears in discussion and conclusion
- **6.7%** PermG FPR -- appears in discussion and conclusion
- **0.50 / 0.483** alpha_c -- appears in experiments and conclusion
- **11/15** cross-architecture conditions -- appears in experiments and conclusion
- **24/24 forward, 0/24 reverse** -- appears in experiments and conclusion
- **>7B** untested scale -- appears in conclusion and limitations
- **T<=25, T>=100** -- appears in discussion and limitations
- **94.4%** max FPR -- appears only in conclusion (source not shown in these files)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e5f671e-1b59-4691-9762-1667bcc0d538",
  "isSidechain": true,
  "agentId": "a5ed021f86aec5f66",
  "requestId": "req_011CbPre3V8w61q5unu5tkcG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6528a480-b58e-48dd-a2c3-acd73d985d48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPR3bch6RLLpMdwNmMbG2t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6144,
      "cache_read_input_tokens": 35810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6144,
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
