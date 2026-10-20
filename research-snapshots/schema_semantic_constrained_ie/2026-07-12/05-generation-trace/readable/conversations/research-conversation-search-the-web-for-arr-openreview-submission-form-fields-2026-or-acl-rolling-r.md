# Research conversation: Search the web for "ARR OpenReview submission form fields 2026" or "ACL Rolling Review submission form 2025 2026" to fin

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad8e9b841bcd2f954.jsonl`
- **Structured JSON:** [`c30f9789fcc6d43bcec2.json`](../../sessions/c3/c30f9789fcc6d43bcec2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

17 recorded events

### User

_source line 1 · 2026-05-24T02:50:12.118Z_

Search the web for "ARR OpenReview submission form fields 2026" or "ACL Rolling Review submission form 2025 2026" to find what fields are required when submitting a paper to ARR via OpenReview.

I need a complete list of all form fields that submitters need to fill in, including:
- Paper metadata fields (title, abstract, keywords, etc.)
- Checklist items
- Optional uploads
- Any acknowledgment checkboxes

Focus on the most recent ARR cycle (2025-2026). Report the field list concisely in a table format: Field Name | Required? | Description. Under 300 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "10a2bf68-1453-4d70-9cf5-3ab41ddb2821",
  "agentId": "ad8e9b841bcd2f954",
  "type": "user",
  "uuid": "61133ed2-9387-45ea-a7cc-80a637312892",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-24T02:50:12.122Z_

```json
{
  "parentUuid": "61133ed2-9387-45ea-a7cc-80a637312892",
  "isSidechain": true,
  "agentId": "ad8e9b841bcd2f954",
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
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
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
      "mcp__agent-ml-research__read_mistakes",
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
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
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
      "mcp__agent-ml-research__read_mistakes",
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
  "uuid": "4ff72e21-2ec9-4552-a9c4-f40170dabac4",
  "timestamp": "2026-05-24T02:50:12.122Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

---

### Assistant

_source line 3 · 2026-05-24T02:50:14.525Z_



Let me search for this information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ff72e21-2ec9-4552-a9c4-f40170dabac4",
  "isSidechain": true,
  "agentId": "ad8e9b841bcd2f954",
  "requestId": "req_011CbLdhsgru3FtnNLp8mK1S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6acefa7b-368c-40f1-9506-e649d77b50e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGXPza6s457vpATSMWoqMF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29542,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29542,
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

_source line 4 · 2026-05-24T02:50:15.035Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NkU5e9sosBVWz9ipFCgYze`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6acefa7b-368c-40f1-9506-e649d77b50e8",
  "isSidechain": true,
  "agentId": "ad8e9b841bcd2f954",
  "requestId": "req_011CbLdhsgru3FtnNLp8mK1S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25488714-22c0-4f17-b2ee-d265fc658153",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGXPza6s457vpATSMWoqMF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29542,
      "cache_read_input_tokens": 0,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 29542
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 84,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 29542,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 29542,
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

_source line 5 · 2026-05-24T02:50:15.040Z_

<details><summary>↩ Tool result · `toolu_01NkU5e9sosBVWz9ipFCgYze`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25488714-22c0-4f17-b2ee-d265fc658153",
  "isSidechain": true,
  "promptId": "10a2bf68-1453-4d70-9cf5-3ab41ddb2821",
  "agentId": "ad8e9b841bcd2f954",
  "type": "user",
  "uuid": "df2cb2ff-5c16-41c4-9458-e2c6c14acae0",
  "sourceToolAssistantUUID": "25488714-22c0-4f17-b2ee-d265fc658153",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-24T02:50:22.131Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BpE8j5jABxvMEgVbVKgp9n`</summary>

```json
{
  "query": "ARR OpenReview submission form fields 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df2cb2ff-5c16-41c4-9458-e2c6c14acae0",
  "isSidechain": true,
  "agentId": "ad8e9b841bcd2f954",
  "requestId": "req_011CbLdi6UZ1fu646J1YbUHD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbf55642-9515-4673-9298-8d559753822d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178CV3gxLownx6wEFfrnhfV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 29542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 7 · 2026-05-24T02:50:22.453Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WjvM18eguEAWgm3qyUTL6t`</summary>

```json
{
  "query": "ACL Rolling Review submission form checklist 2025 2026 OpenReview fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbf55642-9515-4673-9298-8d559753822d",
  "isSidechain": true,
  "agentId": "ad8e9b841bcd2f954",
  "requestId": "req_011CbLdi6UZ1fu646J1YbUHD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "514cb472-d703-4486-80b4-2caebe9d8baf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178CV3gxLownx6wEFfrnhfV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 29542,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1448
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 116,
          "cache_read_input_tokens": 29542,
          "cache_creation_input_tokens": 1448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1448,
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

_source line 8 · 2026-05-24T02:50:27.458Z_

<details><summary>↩ Tool result · `toolu_01BpE8j5jABxvMEgVbVKgp9n`</summary>

```text
Web search results for query: "ARR OpenReview submission form fields 2026"

Links: [{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ARR System | openreview/openreview-py | DeepWiki","url":"https://deepwiki.com/openreview/openreview-py/8-arr-system"},{"title":"Customizing your submission form | OpenReview","url":"https://docs.openreview.net/getting-started/hosting-a-venue-on-openreview/customizing-your-submission-form"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"}]

Based on the search results, I found information about ARR OpenReview submission form fields for 2026:

ARR provides submission form fields and a submission checklist for authors to complete during paper submission. The checklist is intended as a reminder to help authors improve the quality of their papers.

ARR submissions include a metadata field for topic area to help direct papers to appropriate area chairs and reviewers. Additionally, supplementary materials can be uploaded in the 'data' field in the submission form.

The search results reference that "here are the paper submission form fields for your reference" on both the ARR Call for Papers and ACL Member Portal pages, but the actual detailed list of all form fields is not included in the search results. For a complete list of specific form fields, you would need to visit the ARR Call for Papers page directly at http://aclrollingreview.org/cfp or check the submission form when you access OpenReview.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbf55642-9515-4673-9298-8d559753822d",
  "isSidechain": true,
  "promptId": "10a2bf68-1453-4d70-9cf5-3ab41ddb2821",
  "agentId": "ad8e9b841bcd2f954",
  "type": "user",
  "uuid": "e0a6ce37-c009-4d32-8d36-8c99ddba8ec9",
  "sourceToolAssistantUUID": "dbf55642-9515-4673-9298-8d559753822d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-24T02:50:29.591Z_

<details><summary>↩ Tool result · `toolu_01WjvM18eguEAWgm3qyUTL6t`</summary>

```text
Web search results for query: "ACL Rolling Review submission form checklist 2025 2026 OpenReview fields"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"}]

Based on the search results, I found information about ACL Rolling Review submission requirements for 2025-2026:

## Submission Form and Checklist

Paper submission form fields are available for reference, and you are encouraged to look at the submission form and responsible NLP checklist, which list all the questions you will be asked during submission.

## OpenReview Profile Requirements

Authors must have an updated OpenReview profile, including affiliation, semantic scholar link, dblp link, ACL anthology link, and an email address where they can receive OpenReview messages.

## Author Registration Form

All authors are expected to complete a registration form within 48 hours after submission deadline (e.g., before May 21 EoD AoE for May 2025 cycle, where the submission deadline is May 19).

## Key Submission Checklist Items

Common items authors should check include:

- All long, short, and theme papers must follow the ACL Author Guidelines
- Papers must not include authors' names and affiliations
- Supplementary materials, including any links to repositories, should also be anonymized
- The paper follows ACL formatting; use the ACL pubcheck tool to check for common problems; there is an official Overleaf template

The full submission form fields are accessible directly on the ACL Rolling Review website at aclrollingreview.org/submissionform, and the responsible NLP checklist provides additional guidance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "514cb472-d703-4486-80b4-2caebe9d8baf",
  "isSidechain": true,
  "promptId": "10a2bf68-1453-4d70-9cf5-3ab41ddb2821",
  "agentId": "ad8e9b841bcd2f954",
  "type": "user",
  "uuid": "cca60ef2-1998-4c9a-a9dc-16f7279574d1",
  "sourceToolAssistantUUID": "514cb472-d703-4486-80b4-2caebe9d8baf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-24T02:50:32.054Z_

Found a direct page for submission form fields. Let me fetch it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cca60ef2-1998-4c9a-a9dc-16f7279574d1",
  "isSidechain": true,
  "agentId": "ad8e9b841bcd2f954",
  "requestId": "req_011CbLdjAQy1E5EbZjQ9HoG6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bb9b6c7-e6e4-4f95-8c79-27c19381651a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPd7Lm6MaAfMKNQrFuzNjp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1474,
      "cache_read_input_tokens": 30990,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1474,
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

_source line 11 · 2026-05-24T02:50:32.515Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WCFPTraq9VbDSRciMFEvH7`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bb9b6c7-e6e4-4f95-8c79-27c19381651a",
  "isSidechain": true,
  "agentId": "ad8e9b841bcd2f954",
  "requestId": "req_011CbLdjAQy1E5EbZjQ9HoG6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c97f599-b570-4263-aad5-724854fbf412",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPd7Lm6MaAfMKNQrFuzNjp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1474,
      "cache_read_input_tokens": 30990,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1474
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 30990,
          "cache_creation_input_tokens": 1474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1474,
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

_source line 12 · 2026-05-24T02:50:32.520Z_

<details><summary>↩ Tool result · `toolu_01WCFPTraq9VbDSRciMFEvH7`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c97f599-b570-4263-aad5-724854fbf412",
  "isSidechain": true,
  "promptId": "10a2bf68-1453-4d70-9cf5-3ab41ddb2821",
  "agentId": "ad8e9b841bcd2f954",
  "type": "user",
  "uuid": "52e34e70-9c81-42b0-b602-f217e4b72329",
  "sourceToolAssistantUUID": "6c97f599-b570-4263-aad5-724854fbf412",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T02:50:36.791Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017WZjvpotDpJVRx2n6wmvpX`</summary>

```json
{
  "url": "https://aclrollingreview.org/submissionform",
  "prompt": "Extract ALL submission form fields listed on this page. For each field, note: the field name, whether it is required or optional, and a brief description of what it asks for. Include all checklist items, acknowledgment checkboxes, upload fields, and metadata fields. Be exhaustive - list every single field."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52e34e70-9c81-42b0-b602-f217e4b72329",
  "isSidechain": true,
  "agentId": "ad8e9b841bcd2f954",
  "requestId": "req_011CbLdjP8gxbR3pnevUsgdq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "007d97d3-dc0a-4419-ad89-6d34817be2d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGeR8P9SrQamvWyGvH1uAN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 32464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 610,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
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

_source line 14 · 2026-05-24T02:50:38.042Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0146dZBraDQcrskwpNVes48Q`</summary>

```json
{
  "url": "https://aclrollingreview.org/responsibleNLPresearch",
  "prompt": "Extract ALL responsible NLP checklist questions/fields that submitters must fill in on the OpenReview submission form. List every question with its options."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "007d97d3-dc0a-4419-ad89-6d34817be2d2",
  "isSidechain": true,
  "agentId": "ad8e9b841bcd2f954",
  "requestId": "req_011CbLdjP8gxbR3pnevUsgdq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c75af990-cd72-4b47-85f0-3292843bff70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGeR8P9SrQamvWyGvH1uAN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 32464,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 610
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 245,
          "cache_read_input_tokens": 32464,
          "cache_creation_input_tokens": 610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 610,
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

_source line 15 · 2026-05-24T02:50:41.199Z_

<details><summary>↩ Tool result · `toolu_017WZjvpotDpJVRx2n6wmvpX`</summary>

```text
# ACL Rolling Review Submission Form Fields

| Field Name | Required/Optional | Description |
|---|---|---|
| Title | Required | Paper title; supports TeX formulas using "$In-line$" or "\\(Block\\)" formats |
| Authors | Required | Search and add author profiles by name or email |
| TL;DR | Required | Concise single-sentence summary of the paper |
| Abstract | Required | Paper abstract with TeX formula support |
| Pdf | Required | Single PDF file containing paper, references, and appendices |
| Paper Type | Required | Classification as short or long paper per CFP requirements |
| Area | Required | Most relevant research area or track selection |
| Previous URL | Optional | URL of prior ARR submission (for resubmissions) |
| Previous PDF | Optional | PDF of earlier ARR submission (for resubmissions) |
| Response PDF | Optional | Author responses to previous reviews (for resubmissions) |
| Reviewer/Editor Reassignment Request | Optional | Reviewer IDs requesting reassignment (comma-separated); include 'AE' for action editor |
| Reviewer/Editor Reassignment Justification | Optional | Rationale for reassignment requests |
| Software | Optional | Single .tgz or .zip archive (max 200MB) |
| Data | Optional | Single .tgz or .zip archive (max 200MB) |
| Preprint | Optional | Public anonymous preprint publication consent |
| Existing Preprints | Optional | URLs of publicly available non-anonymous preprints |
| Preferred Venue | Optional | Designated venue acronym from official list |
| Consent to Share Data | Optional | Agreement to include anonymized metadata in public dataset |
| Consent to Review | Required | Agreement to serve as reviewer if eligible |
| Responsible NLP Research Questions | Required | Series of checklist items from responsible research guidelines |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "007d97d3-dc0a-4419-ad89-6d34817be2d2",
  "isSidechain": true,
  "promptId": "10a2bf68-1453-4d70-9cf5-3ab41ddb2821",
  "agentId": "ad8e9b841bcd2f954",
  "type": "user",
  "uuid": "efee9591-8f6a-4f3d-be5b-263208941f9a",
  "sourceToolAssistantUUID": "007d97d3-dc0a-4419-ad89-6d34817be2d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T02:50:44.293Z_

<details><summary>↩ Tool result · `toolu_0146dZBraDQcrskwpNVes48Q`</summary>

```text
# Responsible NLP Checklist Questions for ARR Submissions

Based on the content provided, here are the checklist questions submitters must address:

## Section A: For Every Submission
1. **A1**: "Did you describe the _limitations_ of your work?"
2. **A2**: "Did you discuss any potential _risks_ of your work?"

## Section B: Scientific Artifacts
3. **B1**: "Did you cite the creators of artifacts you used?"
4. **B2**: "Did you discuss the _license or terms_ for use and / or distribution of any artifacts?"
5. **B3**: "Did you discuss if your use of existing artifact(s) was consistent with their _intended use_?"
6. **B4**: "Did you discuss the steps taken to check whether the data...contains any _information that names or uniquely identifies individual people_ or _offensive content_?"
7. **B5**: "Did you provide documentation of the artifacts?"
8. **B6**: "Did you report relevant statistics like the number of examples, details of train / test / dev splits?"

## Section C: Computational Experiments
9. **C1**: "Did you report the _number of parameters_ in models, the _total computational budget_, and _computing infrastructure_?"
10. **C2**: "Did you discuss the experimental setup, including _hyperparameter search_?"
11. **C3**: "Did you report _descriptive statistics_ about your results?"
12. **C4**: "If you used existing packages, did you report implementation and parameter settings?"

## Section D: Human Annotators/Participants
13. **D1**: "Did you report the full text of instructions given to participants?"
14. **D2**: "Did you report information about recruitment and payment of participants?"
15. **D3**: "Did you discuss whether and how _consent_ was obtained?"
16. **D4**: "Was the data collection protocol _approved_ by an ethics review board?"
17. **D5**: "Did you report demographic and geographic characteristics of annotators?"

## Section E: AI Assistants
18. **E1**: "If you used any AI assistants, did you include information about your use?"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c75af990-cd72-4b47-85f0-3292843bff70",
  "isSidechain": true,
  "promptId": "10a2bf68-1453-4d70-9cf5-3ab41ddb2821",
  "agentId": "ad8e9b841bcd2f954",
  "type": "user",
  "uuid": "831defac-8fd2-48ee-81e1-4eb761b2bc72",
  "sourceToolAssistantUUID": "c75af990-cd72-4b47-85f0-3292843bff70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-24T02:50:58.425Z_

ARR OpenReview submission form fields (current 2025-2026 cycles):

**Paper Metadata & Uploads**

| Field | Required? | Description |
|---|---|---|
| Title | Yes | Paper title (supports TeX) |
| Authors | Yes | Author profiles via OpenReview search |
| TL;DR | Yes | One-sentence summary |
| Abstract | Yes | Paper abstract (supports TeX) |
| PDF | Yes | Full paper + references + appendices |
| Paper Type | Yes | Short or Long |
| Area | Yes | Research area / track |
| Software | No | Code archive, .tgz/.zip, max 200MB |
| Data | No | Data archive, .tgz/.zip, max 200MB |

**Resubmission Fields**

| Field | Required? | Description |
|---|---|---|
| Previous URL | No | OpenReview URL of prior ARR submission |
| Previous PDF | No | PDF of earlier submission |
| Response PDF | No | Author response to previous reviews |
| Reviewer/Editor Reassignment Request | No | Comma-separated reviewer IDs to reassign |
| Reassignment Justification | No | Rationale for reassignment |

**Consent & Preferences**

| Field | Required? | Description |
|---|---|---|
| Consent to Review | Yes | Agree to serve as reviewer if eligible |
| Preprint | No | Consent to publish anonymous preprint |
| Existing Preprints | No | URLs of non-anonymous preprints |
| Preferred Venue | No | Target venue acronym (e.g. EMNLP 2026) |
| Consent to Share Data | No | Allow anonymized metadata in public dataset |

**Responsible NLP Research Checklist (all required, in-form)**

| Section | Items |
|---|---|
| A: Every Submission | A1 Limitations, A2 Risks |
| B: Scientific Artifacts | B1 Citation, B2 License, B3 Intended use, B4 PII/offensive content, B5 Documentation, B6 Data statistics |
| C: Computational Experiments | C1 Parameters/compute, C2 Hyperparameter search, C3 Descriptive statistics, C4 Package settings |
| D: Human Annotators | D1 Instructions, D2 Recruitment/payment, D3 Consent, D4 Ethics board, D5 Demographics |
| E: AI Assistants | E1 AI assistant disclosure |

Each checklist item asks "Did you do X?" with answer options. Items not applicable can be marked accordingly.

Sources:
- [Submission Form Fields – ACL Rolling Review](http://aclrollingreview.org/submissionform)
- [Responsible NLP Research – ACL Rolling Review](http://aclrollingreview.org/responsibleNLPresearch)
- [Call for Papers – ACL Rolling Review](http://aclrollingreview.org/cfp)
- [Authors Guidelines – ACL Rolling Review](http://aclrollingreview.org/authors)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "831defac-8fd2-48ee-81e1-4eb761b2bc72",
  "isSidechain": true,
  "agentId": "ad8e9b841bcd2f954",
  "requestId": "req_011CbLdkFGSqmmU84D1ovar1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5fbb4940-b9b6-4cb8-92ab-64c0374eba75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCvF3gpWion9fXQVx3qJY4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1237,
      "cache_read_input_tokens": 33074,
      "output_tokens": 732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1237
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 732,
          "cache_read_input_tokens": 33074,
          "cache_creation_input_tokens": 1237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1237,
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
