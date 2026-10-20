# Research conversation: I need to check whether negative/null experimental results are discussed in this paper. The paper is about OntoCoDec, a 

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 1
- **Tool calls:** 24
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aa0ebc68a17d43ebd.jsonl`
- **Structured JSON:** [`202063470476e154017e.json`](../../sessions/20/202063470476e154017e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

60 recorded events

### User

_source line 1 · 2026-05-23T18:11:06.930Z_

I need to check whether negative/null experimental results are discussed in this paper. The paper is about OntoCoDec, a constrained decoding framework for information extraction.

**Task**: 
1. First, read the experiment registry to find all experiments with conclusion="negative": `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/agent/registry.yaml` — search for "negative" conclusions and list them with their names and one-line descriptions.

2. Then, check the paper sections to see which of these negative results are discussed. Key paper files:
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex`
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex`
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex`
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex`
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex`
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex`
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex`
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex`

3. Report:
   - Which negative results ARE discussed in the paper (with file/line reference)
   - Which negative results are NOT mentioned at all
   - For unmissioned ones: could any strengthen the paper if briefly mentioned? (e.g., "we tried X but it didn't work because Y" adds depth)

Keep the report concise — table format preferred.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "71aaba98-a941-47d8-93ef-03c6d7ffda26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-23T18:11:06.941Z_

```json
{
  "parentUuid": "71aaba98-a941-47d8-93ef-03c6d7ffda26",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
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
  "uuid": "7ba81c68-b74c-4ee1-9de5-a6bd528b5b04",
  "timestamp": "2026-05-23T18:11:06.941Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

---

### Assistant

_source line 3 · 2026-05-23T18:11:08.764Z_

I'll search for negative conclusions in the registry and check the paper sections in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ba81c68-b74c-4ee1-9de5-a6bd528b5b04",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx82hrD1zgEYwZt5s31",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2ad9470-27d0-407c-a4af-952b5fba4b3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QQXNu5XnS6cpwVpvNgTALM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33564,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33564,
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

_source line 4 · 2026-05-23T18:11:09.657Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CSE2PaY6PfcHfRQ4kDntmb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/agent/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2ad9470-27d0-407c-a4af-952b5fba4b3d",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx82hrD1zgEYwZt5s31",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d217106-c382-4676-a422-5e8022854e02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QQXNu5XnS6cpwVpvNgTALM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33564,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33564,
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

_source line 5 · 2026-05-23T18:11:09.673Z_

<details><summary>↩ Tool result · reported error · `toolu_01CSE2PaY6PfcHfRQ4kDntmb`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d217106-c382-4676-a422-5e8022854e02",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "db2ef42b-1167-4dd2-9b33-5e2a7f76597d",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a.",
  "sourceToolAssistantUUID": "7d217106-c382-4676-a422-5e8022854e02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-23T18:11:09.902Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01D4QiHEi7QpH6gruLGbXQ4p`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db2ef42b-1167-4dd2-9b33-5e2a7f76597d",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx82hrD1zgEYwZt5s31",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "890f0038-d30e-45f4-b3c0-0010a4cf3a15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QQXNu5XnS6cpwVpvNgTALM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33564,
      "cache_read_input_tokens": 0,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 33564
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 178,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 33564,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 33564,
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

_source line 7 · 2026-05-23T18:11:09.924Z_

<details><summary>↩ Tool result · `toolu_01D4QiHEi7QpH6gruLGbXQ4p`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/p3_case_studies.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/p3_case_studies_861a0d.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/case_study_kappa_dr.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_kappa_case_study.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/fig1_framework.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_power_analysis_523cc9.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_power_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_high_kappa_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_downstream_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_order_invariance.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_quantization.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_wikievents_pilot.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_gollie_comparison.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_pumping_lemma.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_zs_crossmodel.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_ai_assistants.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "890f0038-d30e-45f4-b3c0-0010a4cf3a15",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "f93a8f90-7d0b-41ea-bb67-3580451cd048",
  "sourceToolAssistantUUID": "890f0038-d30e-45f4-b3c0-0010a4cf3a15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-23T18:11:12.038Z_

The registry file path doesn't exist at that location. Let me find the correct path and read the relevant paper files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f93a8f90-7d0b-41ea-bb67-3580451cd048",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx8FdELSWtS8HFVvBEj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "110431d7-8625-4c42-9d7b-a8f8e828b4a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AmipKEwtFbKLw978cfsnPm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3738,
      "cache_read_input_tokens": 33564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3738,
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

_source line 9 · 2026-05-23T18:11:13.373Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Rw1vULvwqjp8qHp2PSJtbR`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie -name \"registry.yaml\" 2>/dev/null",
  "description": "Find registry.yaml location"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "110431d7-8625-4c42-9d7b-a8f8e828b4a8",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx8FdELSWtS8HFVvBEj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28bbaf2a-587d-4e66-9e9b-75be55bef0b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AmipKEwtFbKLw978cfsnPm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3738,
      "cache_read_input_tokens": 33564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3738,
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

_source line 10 · 2026-05-23T18:11:13.528Z_

<details><summary>↩ Tool result · `toolu_01Rw1vULvwqjp8qHp2PSJtbR`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28bbaf2a-587d-4e66-9e9b-75be55bef0b4",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "cda9fac4-cab7-4cbc-88bb-3d0c26c5862c",
  "sourceToolAssistantUUID": "28bbaf2a-587d-4e66-9e9b-75be55bef0b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T18:11:14.250Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Tae5thoKMqKqT19bKBxU1f`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cda9fac4-cab7-4cbc-88bb-3d0c26c5862c",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx8FdELSWtS8HFVvBEj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19d87fae-6eb0-4017-97cf-4db80c846220",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AmipKEwtFbKLw978cfsnPm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3738,
      "cache_read_input_tokens": 33564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3738,
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

_source line 12 · 2026-05-23T18:11:14.257Z_

<details><summary>↩ Tool result · `toolu_01Tae5thoKMqKqT19bKBxU1f`</summary>

```text
1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrrr rr@{}}
21	\toprule
22	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-7} \cmidrule(l){8-9}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08  & 15.45
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08  & 14.92
39	  & 8.23  & 30.98 \\
40	GCD-equiv.$^\dagger$
41	  & 15.26 & $\downarrow$1\%
42	  & \textbf{0} & \textbf{0}
43	  & 0.04  & 15.30
44	  & 8.75  & 30.91 \\
45	Semantic
46	  & 11.65 & $\downarrow$24\%
47	  & 1.51  & 0.40
48	  & 2.71  & 14.36
49	  & 8.15  & 31.01 \\
50	S1
51	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
52	  & \textbf{0} & \textbf{0}
53	  & 9.90  & \textbf{10.83}
54	  & \textbf{8.36} & 30.98 \\
55	S2
56	  & 0.97  & $\downarrow$94\%
57	  & \textbf{0} & \textbf{0}
58	  & 8.03  & \textbf{9.00}
59	  & 8.03  & \textbf{31.90} \\
60	\bottomrule
61	\end{tabular}}%
62	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
63	$\Delta$DR: relative change vs.\ unconstrained; Tot.\ = DR + CF; bold = best (CF excluded).
64	F1 (\%). S1/S2 = single/two-pass (\S\ref{sec:strategies}).
65	Grammar = GCD ceiling~\cite{geng2023gcd}.
66	$\dagger$vLLM \texttt{guided\_json}~\cite{kwon2023vllm} (\S\ref{sec:constrained-baselines}).
67	Deterministic (greedy, $T{=}$0); robustness evidence in Table~\ref{tab:cross-model} and Appendices~\ref{app:bootstrap-effect-sizes},~\ref{app:prompt-sensitivity}.}
68	\label{tab:scierc-ablation}
69	\end{table}
70	
71	% ──────────────────────────────────────────
72	%  (a) Zero-shot diagnostic (compressed)
73	% ──────────────────────────────────────────
74	\paragraph{Zero-shot diagnostic.}
75	% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093
76	Table~\ref{tab:scierc-ablation} establishes that DR violations are pervasive (15--18\% across datasets) and that constraint layers interact non-additively: grammar-only achieves 3\% DR reduction on SciERC, semantic-only 24\%, but their composition yields 94\%---the \emph{empirical enabling dependency}.
77	On DocRED (96 relations, $\bar{\kappa}{=}0.842$), grammar-only \emph{increases} DR via \textit{latent violation surfacing}: forcing OOV$\to$valid relation mapping exposes violations previously masked by vocabulary errors (Appendix~\ref{app:cross-model-zs}).
78	Cross-model validation (3 models $\times$ 2 datasets; Table~\ref{tab:cross-model}) confirms DR drops of 76--99\% on SciERC and 42--90\% on DocRED, with R-F1 improving in 5/6 settings; post-hoc filtering achieves DR${=}$0\% but at 15--74\% rejection rates.
79	DR-to-CF conversion represents a severity downgrade: DR is irrecoverable without re-extraction, while CF---individually valid triples with cross-triple inconsistency---is amenable to post-hoc resolution (TCR eliminates all CF in our experiments, with bounded DR regression; Appendix~\ref{app:tcr}).
80	Zero-shot evaluation thus establishes violation prevalence and constraint interaction; fine-tuning demonstrates practical elimination.
81	
82	% ──────────────────────────────────────────
83	%  (e) Composability with Fine-Tuning (expanded)
84	% ──────────────────────────────────────────
85	\paragraph{Composability with fine-tuning.}
86	\label{sec:composability}
87	% exp_ids: bootstrap_ci_ft_composability.json, w5_lora_scierc_*, w8_*
88	Fine-tuning alone reduces DR to 1--2\% but leaves residual violations on tight-constraint relations (Table~\ref{tab:composability}); adding S1 yields DR\,$\leq$\,0.21\% with no significant $\Delta$R-F1 (Bonferroni-corrected; 95\% CIs $\subseteq [-0.69, {+}0.25]$\,pp; removed triples are 97.6--100\% false positives; Appendix~\ref{app:downstream-impact}).
89	Under fine-tuning, grammar becomes a no-op ($\Delta$DR$<$0.2\,pp), making the semantic layer the sole DR defense (41--69\% on SciERC, 2--75\% on DocRED; Appendix~\ref{app:ft-ablation}); three relations with $\kappa \geq 0.36$ retain DR, all eliminated by S1 (Appendix~\ref{app:lora-per-relation}).
90	Fallback frequency is model-dependent: Qwen triggers 0 fallbacks under LoRA + S1 on SciERC, while Llama triggers 5{,}882 (Table~\ref{tab:ft-ablation}), reflecting weaker entity typing; despite this, DR reaches 0.09\% on SciERC (0.21\% on DocRED), confirming that even frequent fallback does not compromise enforcement.
91	CF drops from $+$9.82\,pp (zero-shot) to $+$1.18\,pp (fine-tuned), concentrated in \textsc{Generic}$\leftrightarrow$X ambiguity (63.3\% of zero-shot CF; Appendix~\ref{app:cf-distribution}); beam ($k{=}4$) eliminates all violation types at 8B (R-F1 43--46; \S\ref{sec:beam-results}).
92	
93	% ──────────────────────────────────────────
94	%  CF quantification (MF1 response)
95	% ──────────────────────────────────────────
96	\paragraph{Cross-field violation analysis.}
97	% exp_ids: phase2_scierc_full_s1 (ZS: CF=248, 167 docs), w5_lora_scierc_full_s1_eval (FT: CF=22, 20 docs)
98	Under zero-shot greedy S1, CF is the sole residual violation type (DR, RV, ET all eliminated): 248 cross-field violations arise across 167 documents, of which 63.3\% involve \textsc{Generic}$\leftrightarrow$X type ambiguity (Appendix~\ref{app:cf-distribution}), concentrated in \textsc{Generic}$\leftrightarrow$\textsc{OtherScientificTerm} (34.7\%) and \textsc{Generic}$\leftrightarrow$\textsc{Material} (12.3\%).
99	A source breakdown (Appendix~\ref{app:cascade-analysis}) shows 58.1\% originate from hallucinated entities (a model capacity issue), while true cascade errors---where first-seen registration locks an incorrect type---account for only 7.3\%; correct locks are 2.5$\times$ more frequent, confirming first-seen registration as a net-positive mechanism.
100	Fine-tuning reduces CF to 22 cross-field violation instances across 20 documents (1.18\%), with cascade errors completely eliminated (0/22).
101	Beam search ($k{=}4$) eliminates all remaining CF at 1.39$\times$ latency (\S\ref{sec:beam-results}).
102	
103	\begin{table}[t]
104	\centering
105	\small
106	\setlength{\tabcolsep}{3pt}
107	\resizebox{\columnwidth}{!}{%
108	\begin{tabular}{@{}lll rrrr r@{}}
109	\toprule
110	\textbf{Model} & \textbf{Dataset} & \textbf{Mode}
111	  & \textbf{DR\,$\downarrow$} & \textbf{CF}
112	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$}
113	  & \textbf{$\Delta$DR} \\
114	\midrule
115	\multirow{4}{*}{Qwen3-8B}
116	  & \multirow{2}{*}{SciERC}
117	    & Unconstr.\ &  1.95 & 0    & 43.86 & 67.05 & --- \\
118	  & & S1    & \textbf{0} & 1.18 & 43.77 & 67.05 & $\downarrow$100\% \\
119	\cmidrule(l){2-8}
120	  & \multirow{2}{*}{DocRED}
121	    & Unconstr.\ &  0.76 & 0.12 & 40.86 & 82.15 & --- \\
122	  & & S1    & 0.01 & 0.41 & 40.56 & 81.43 & $\downarrow$98.7\% \\
123	\midrule
124	\multirow{4}{*}{\shortstack[l]{Llama\\3.1-8B}}
125	  & \multirow{2}{*}{SciERC}
126	    & Unconstr.\ &  1.11 & 0    & 45.45 & 67.76 & --- \\
127	  & & S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\downarrow$92\% \\
128	\cmidrule(l){2-8}
129	  & \multirow{2}{*}{DocRED}
130	    & Unconstr.\ &  0.49 & 0.08 & 43.72 & 83.93 & --- \\
131	  & & S1    &  0.21 & 0.21 & 43.78 & 83.94 & $\downarrow$57\% \\
132	\bottomrule
133	\end{tabular}}%
134	\caption{Fine-tuning composability: LoRA $\times$ unconstrained vs.\ S1 on SciERC (551 docs) and DocRED (998 dev docs).
135	F1 (\%). No $\Delta$R-F1 is significant (Bonferroni-corrected; details in text); all DR reductions are ($p{<}0.001$).
136	E-F1 includes parse-failure documents (Qwen PF: 7--8\%; Llama PF: 2--3\%).}
137	\label{tab:composability}
138	\end{table}
139	
140	% ──────────────────────────────────────────
141	%  (f) Downstream impact of DR elimination
142	%  exp_ids: task_e_lucky_violation_analysis
143	% ──────────────────────────────────────────
144	\paragraph{Downstream impact.}
145	\label{sec:downstream-impact}
146	Among constraint-removed triples, only 0.49\% match gold labels (Appendix~\ref{app:lucky-violations}); error analysis of 514 false negatives confirms only one (0.2\%) was blocked by constraints, with dominant sources (relation confusion, entity type polysemy) schema-valid and beyond constraint reach (Appendix~\ref{app:error-analysis}).
147	Across fine-tuned settings, 36 residual DR violations decompose into entity type errors (39\%), schema coverage gaps (33\%), and relation/direction errors (28\%); the irreducible floor is $\sim$3 violations (Appendix~\ref{app:residual-dr-analysis}).
148	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19d87fae-6eb0-4017-97cf-4db80c846220",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "4f4bd9ea-3f55-4bda-a110-81ed14b3b8f0",
  "sourceToolAssistantUUID": "19d87fae-6eb0-4017-97cf-4db80c846220",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T18:11:14.767Z_

<details open><summary>🔧 Tool call — Read · `toolu_01658qMQihxBRurHiPu2EtAj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f4bd9ea-3f55-4bda-a110-81ed14b3b8f0",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx8FdELSWtS8HFVvBEj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "951837ff-85a2-4446-9687-55d9994a2992",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AmipKEwtFbKLw978cfsnPm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3738,
      "cache_read_input_tokens": 33564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3738,
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

_source line 14 · 2026-05-23T18:11:14.775Z_

<details><summary>↩ Tool result · `toolu_01658qMQihxBRurHiPu2EtAj`</summary>

```text
1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC, lower on DocRED due to amortization over longer sequences; under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Constraint compilation is one-time $<$0.5\,s; scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
7	
8	\paragraph{Beam search compatibility.}
9	\label{sec:beam-results}
10	% exp_id: d066_beam_sweep
11	With LoRA, beam search~\cite{anderson2017guided} eliminates all four violation types at 8B on both SciERC and DocRED; at 70B, beam $k{=}4$ achieves DR${=}$RV${=}$ET${=}$0\% with one residual CF on SciERC (Appendix~\ref{app:beam-search}).
12	A beam-width sweep ($k \in \{1,2,4,8\}$) on SciERC reveals $k{=}2$ as Pareto-optimal: R-F1 44.60 (highest), CF 0.11\%, at only 1.18$\times$ greedy S1 latency; $k{=}4$ achieves CF${=}$0\% but lower R-F1 (43.60) at 1.39$\times$ (Table~\ref{tab:beam-sweep}; latencies relative to greedy S1).
13	This yields three deployment tiers: greedy S1 ($+$10\% latency, DR${\leq}$0.21\%, CF${\leq}$1.4\%), beam $k{=}2$ (1.18$\times$, near-zero CF), and beam $k{=}4$ (1.39$\times$, all violations${\to}$0\% at 8B).
14	Per-beam memory overhead is $O(k \times |\text{entities}| \times |\text{types}|)$ for independent entity registry copies, negligible at typical document scales.
15	
16	% exp_ids: r16_70b_scierc_zs_s1, r16_70b_docred_zs_s1, 70b_lora_scierc, 70b_lora_docred_200
17	\paragraph{70B-class validation (single-family).}
18	\label{sec:70b-results}
19	The following results constitute a preliminary single-family scale exploration on Llama-3.1-70B-Instruct (AWQ INT4); cross-family verification (e.g., Qwen-72B) remains future work.
20	All 70B experiments use Llama-3.1-70B-Instruct under AWQ INT4 quantization; an 8B ablation confirms constraint enforcement is unaffected by quantization (Appendix~\ref{app:quantization}).
21	Zero-shot S1 eliminates DR on both datasets (SciERC 6.41\%\,$\to$\,0\%, DocRED 14.98\%\,$\to$\,0\%; R-F1 11--13).
22	% exp_ids: r16_70b_scierc_zs_ablation (grammar_only, semantic_only, full_s1)
23	A four-way ablation reveals scale-dependent layer interaction: semantic-only achieves 84\% DR reduction vs.\ 8B's 24\% (Table~\ref{tab:scierc-ablation}), though grammar remains necessary for RV elimination and CF control (semantic-only CF${=}$76).
24	% exp_ids: eval_70b_lora_scierc_s1_constrained, eval_70b_lora_docred_200_s1_constrained
25	LoRA confirms composability: DR\,$\to$\,0\% on both datasets (R-F1 44.53, 43.95; $|\Delta| \leq 0.20$\,pp; CF 0.18--1.33\%); cross-family generalization at 70B scale remains to be verified.
26	% exp_ids: eval_70b_lora_docred_200_beam4_s1
27	Beam ($k{=}4$) reduces DocRED parse failures (12.5\%\,$\to$\,0.5\%, R-F1 $+$4.19\,pp); SciERC controlled comparison isolates pure beam gain at $+$0.28\,pp (Appendix~\ref{app:70b-ablation}).
28	
29	% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc
30	\paragraph{Comparison with grammar-constrained approaches.}
31	\label{sec:constrained-baselines}
32	Our grammar-only ablation (Table~\ref{tab:scierc-ablation}, row~2) implements the same constraints as GCD~\cite{geng2023gcd} and BoostCD~\cite{boostcd2025}; vLLM \texttt{guided\_json}~\cite{kwon2023vllm} confirms equivalence on Qwen3-8B (DR${=}$15.26\%; other models use the same backend; Appendix~\ref{app:gcd-comparison}).
33	The ${\sim}$15\% residual DR is the gap our semantic layer addresses (94\% total reduction); trie-only constraints without JSON enforcement yield 9--51\% parse failure (Appendix~\ref{app:trie-baseline}).
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "951837ff-85a2-4446-9687-55d9994a2992",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "97c839da-0f0e-484c-bc4e-66f93eec90bf",
  "sourceToolAssistantUUID": "951837ff-85a2-4446-9687-55d9994a2992",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T18:11:15.353Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BCe1TVvPWyKDvxShzfQtr7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97c839da-0f0e-484c-bc4e-66f93eec90bf",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx8FdELSWtS8HFVvBEj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f4f1464-678b-460c-8078-c2b30ba96565",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AmipKEwtFbKLw978cfsnPm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3738,
      "cache_read_input_tokens": 33564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3738,
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

_source line 16 · 2026-05-23T18:11:15.623Z_

<details><summary>↩ Tool result · `toolu_01BCe1TVvPWyKDvxShzfQtr7`</summary>

```text
1	% Appendix B — Extended Discussion
2	% Contains discussion paragraphs moved from the main text during compression.
3	
4	\section{Extended Discussion}\label{app:discussion}
5	
6	%%% CF Dual Mechanism %%%
7	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1
8	
9	\paragraph{CF Dual Mechanism.}
10	CF violations arise from two distinct mechanisms:
11	(1)~\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.
12	The entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.
13	(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type, which may differ from the entity's registered type.
14	
15	These mechanisms have sharply different model profiles.
16	Qwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\% of its CF violations to registry override.
17	Llama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.
18	This asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\,=\,2.57\% on DocRED vs.\ Llama's 12.02\%, despite both using identical constraint configurations.
19	The difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.
20	
21	%%% Fallback Behavior and Effective Coverage %%%
22	% exp_ids: cf_fallback_ablation_scierc (final data)
23	
24	\paragraph{Fallback Behavior and Effective Coverage.}
25	\label{app:fallback-coverage}
26	The two-layer architecture produces two distinct fallback mechanisms with different semantic consequences.
27	\emph{Grammar-first fallback} occurs when $S(t) \cap G(t) = \emptyset$: the semantic layer deactivates as a safety valve, preserving structural validity at the cost of potential type violations.
28	The token-level fallback rate (36.6\% on SciERC Llama) is inflated by continuation tokens of multi-token type names (e.g., \textsc{OtherScientificTerm}, averaging 2.87 BPE tokens); at semantically meaningful first-token positions, the rate is 0.04--5.7\% (zero-shot) and drops to $\leq$\,0.11\% under fine-tuning.
29	These events account for the residual DR that persists after constraint enforcement.
30	\emph{Registry-consistent fallback} (4.5\%) occurs when the entity's registered type conflicts with domain/range constraints; the system defaults to the registered type for cross-triple consistency.
31	Together, these mechanisms produce the characteristic profile of composable constraint systems: residual DR traces to grammar-first fallback events, while CF violations arise from registry override events where per-relation enforcement assigns conflicting types.
32	
33	We define \emph{effective semantic constraint coverage} as $1 - f_{\text{gf}}$, where $f_{\text{gf}}$ is the grammar-first fallback rate.
34	On SciERC, Llama-3.1-8B shows $f_{\text{gf}} = 36.6\%$ (6{,}237 of 17{,}024 mask calls), yielding 63.4\% effective coverage.
35	On DocRED, by contrast, Qwen3-8B shows $f_{\text{gf}} = 0.08\%$ (46 of 54{,}859), yielding 99.9\% coverage.
36	The large discrepancy is primarily a tokenization artifact: SciERC entity types are multi-token (e.g., \textsc{OtherScientificTerm}, averaging 2.87 mask calls per type field), and continuation tokens necessarily conflict with the semantic mask, inflating the per-mask-call fallback rate.
37	DocRED types (\textsc{PER}, \textsc{ORG}, \textsc{LOC}, \textsc{TIME}, \textsc{NUM}, \textsc{MISC}) are all single-token, eliminating this inflation.
38	This metric directly quantifies the layer interaction (\S\ref{sec:interaction}): it measures the fraction of decoding steps where both constraint layers are jointly active, providing a fine-grained view beyond aggregate violation rates.
39	Qwen3-8B, with zero grammar-first fallbacks, achieves 100\% effective coverage on SciERC, consistent with its lower residual DR (0.93\% vs.\ Llama's 0.08\%).
40	
41	%%% Fallback Causal Tracing %%%
42	% exp_ids: Task C causal tracing (Qwen/Llama × ZS/FT × S1)
43	
44	\paragraph{Fallback Causal Tracing.}
45	\label{app:causal-tracing}
46	
47	To establish that grammar-first fallback is the \emph{sole} mechanism producing residual DR violations, we instrument the constraint processor to log, for each violation, whether the semantic mask was active ($S(t) \cap G(t) \neq \emptyset$) or bypassed via fallback ($S(t) \cap G(t) = \emptyset$) at the type-bearing position.
48	Table~\ref{tab:causal-tracing} reports the results across four SciERC configurations.
49	
50	\begin{table}[t]
51	\centering
52	\small
53	\begin{tabular}{@{}ll rrr@{}}
54	\toprule
55	\textbf{Model} & \textbf{Setting} & \textbf{Fallback Rate} & \textbf{DR} & \textbf{From FB} \\
56	\midrule
57	Qwen3-8B  & FT S1 & 0/2256 (0\%)    & 0  & N/A \\
58	Qwen3-8B  & ZS S1 & 16/3458 (0.46\%) & 16 & 100\% \\
59	Llama-3.1-8B & FT S1 & 1/2162 (0.05\%) & 1  & 100\% \\
60	Llama-3.1-8B & ZS S1 & 1/2630 (0.04\%) & 1  & 100\% \\
61	\bottomrule
62	\end{tabular}
63	\caption{Fallback causal tracing on SciERC (551 documents). Fallback Rate: type-bearing positions where $S(t) \cap G(t) = \emptyset$ triggers grammar-first fallback. DR: residual domain/range violations. From FB: fraction of DR violations occurring at fallback positions. All violations occur exclusively at tail\_type positions (range constraints are tighter than domain constraints).}
64	\label{tab:causal-tracing}
65	\end{table}
66	
67	When the semantic mask is active, $\text{DR}_{\text{independent}} = 0$: the type constraint processor structurally prevents domain/range violations.
68	All 18 residual DR violations across four configurations occur exclusively at fallback positions, confirming that grammar-first fallback is a necessary condition for residual DR.
69	Fine-tuning reduces fallback to near-zero ($\leq$0.05\%), effectively eliminating the sole source of residual violations.
70	All fallback events occur at tail\_type positions, where $|\operatorname{range}(r, \tau^h)|$ is smaller than $|\operatorname{dom}(r)|$, making the intersection $S(t) \cap G(t)$ more likely to be empty.
71	
72	%%% Enabling Dependency: Confound Analysis %%%
73	
74	\paragraph{Enabling Dependency: Confound Analysis.}
75	\label{app:enabling-confound}
76	
77	The scale-dependent layer interaction (\S\ref{sec:method}) shows that the semantic layer achieves only 24\% DR reduction without the grammar layer (Table~\ref{tab:scierc-ablation}).
78	A potential confound is that the semantic layer depends not only on grammar-enforced vocabulary membership but also on structural enforcement for positional awareness: the semantic layer identifies type-bearing positions by pattern-matching the decoded prefix against the JSON schema, which is reliable only when the grammar layer guarantees valid JSON structure.
79	Without grammar enforcement, malformed structure can cause the semantic layer to misidentify type-bearing positions, reducing effective coverage.
80	We quantify this via the semantic-only ablation (Table~\ref{tab:scierc-ablation}, row~3): CF rises from 0.08\% to 2.71\%, indicating that 2.63\,pp of additional violations trace to structural ambiguity.
81	However, the dominant enabling mechanism remains vocabulary membership: the semantic layer's domain/range lookup requires $r_j \in \mathcal{R}$, which only the grammar layer ensures; without it, OOV relation names produce null constraint lookups.
82	The confound reinforces rather than undermines this interaction: both vocabulary and structural contributions of the grammar layer are prerequisites for effective semantic enforcement.
83	
84	%%% CF-DR Trade-off Analysis %%%
85	% exp_ids: cf_fallback_ablation_scierc (CF fallback vs full_s1 baseline)
86	
87	\paragraph{CF-DR Trade-off Analysis.}
88	\label{app:cf-dr-tradeoff}
89	
90	CF violations are the most prominent residual limitation of OntoCoDec under zero-shot decoding (9.90\% on SciERC, up to 12.02\% on Llama DocRED).
91	We treat this honestly: per-relation independent enforcement cannot eliminate CF without trading it against DR.
92	Table~\ref{tab:cf-dr-tradeoff} reports a pilot ablation in which we replace the grammar-first fallback with a CF-priority fallback that forces the entity's registered type when it conflicts with $\sigma(r)$.
93	
94	\begin{table}[t]
95	\centering
96	\small
97	\begin{tabular}{@{}l rrrr@{}}
98	\toprule
99	\textbf{Configuration} & \textbf{DR\,(\%)} & \textbf{CF\,(\%)} & \textbf{DR+CF} & \textbf{$f_{\text{gf}}$\,(\%)} \\
100	\midrule
101	S1 (baseline) & 0.93 & 9.90 & 10.83 & --- \\
102	CF fallback        & 14.78 & 0.04 & 14.82 & 36.64 \\
103	\midrule
104	$\Delta$ & $+$13.85 & $-$9.86 & $+$3.99 & --- \\
105	\bottomrule
106	\end{tabular}
107	\caption{CF-DR trade-off pilot on SciERC (Qwen3-8B, 551 documents; \texttt{w1\_cf\_fallback\_scierc\_pilot}). CF fallback eliminates CF but re-routes violations to DR, increasing total violations (DR+CF) by 3.99\,pp. $f_{\text{gf}}$: token-level grammar-first fallback rate at type-bearing positions (includes continuation tokens of multi-token type names; first-token position fallback rate is 0.46\% for SciERC Qwen; \S\ref{sec:greedy-limitation}).}
108	\label{tab:cf-dr-tradeoff}
109	\end{table}
110	
111	The CF fallback variant nearly eliminates CF (9.90\%\,$\to$\,0.04\%, $-$9.86\,pp) but at the cost of a 15.9$\times$ increase in DR (0.93\%\,$\to$\,14.78\%, $+$13.85\,pp).
112	% exp_id: w1_cf_fallback_scierc_pilot: DR=0.1478, CF=0.0004, f_gf=0.3664
113	This is not a net improvement: total violations (DR+CF) rise from 10.83\% to 14.82\% ($+$3.99\,pp), so the change \emph{re-routes} violations rather than reducing them.
114	The mechanism is mechanical: each token position with conflicting masks must commit to one violation type; when the CF fallback forces the system to emit the entity's registered type even though it lies outside $\sigma(r)$, the resulting triple satisfies cross-entity consistency but violates domain/range.
115	The token-level grammar-first fallback is triggered at 36.64\% of type-bearing positions (0.46\% at first-token positions; \S\ref{sec:greedy-limitation}); this conflict is structural, not a tunable hyperparameter.
116	
117	We interpret this as a fundamental tension in composable constraint systems with \emph{per-relation independent} enforcement: enforcement priority can be allocated between DR and CF but cannot independently minimize both.
118	Within this design, the current S1 configuration sits near the Pareto frontier of the trade-off, achieving 0.93\% DR at the cost of 9.90\% CF.
119	The direction of the trade-off is consistent beyond SciERC/Qwen3-8B: across all six zero-shot configurations (3 models $\times$ 2 datasets), DR and CF are descriptively inversely associated, with no setting showing both high DR and high CF simultaneously (Table~\ref{tab:cross-model}); however, $n{=}6$ is insufficient for statistical inference on this correlation.
120	The pattern is a structural consequence of per-relation enforcement with grammar-first fallback, not a model- or dataset-specific artifact; we select SciERC/Qwen3-8B for detailed ablation because it exhibits the highest CF (9.90\%), making the trade-off most visible.
121	While the inverse association holds across all configurations, the absolute trade-off magnitude may differ in settings with higher baseline CF, such as Llama DocRED (CF = 12.02\%), where the larger CF headroom could yield proportionally larger shifts under alternative fallback priorities.
122	The CF residual is concentrated in schema ambiguity rather than enforcement failure: 63.3\% of CF violations on SciERC involve the catch-all \textsc{Generic} type (Table~\ref{tab:cf-distribution}), which competes with every content type depending on anaphoric vs.\ referential use, a distinction the per-slot decoder cannot resolve without document-level coreference.
123	
124	Two complementary paths can lower CF without re-routing it to DR.
125	(i)~\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\% relative to the zero-shot setting (9.90\%\,$\to$\,1.18\%; Table~\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.
126	% exp_id: w5_lora_scierc_constrained_eval: CF=0.0118
127	The remaining 1.18\% still traces to \textsc{Generic}$\leftrightarrow$X schema ambiguity, so this path is empirically validated on one dataset and one fine-tuning method but does not generalize without further evidence.
128	(ii)~\emph{Replace per-relation enforcement with global entity-level type consensus during decoding.} This is outside the scope of OntoCoDec's forward-only autoregressive design and is left to future work.
129	
130	%%% Dual-Factor Quantitative Analysis %%%
131	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1,
132	%          llama_scierc_full_s1, llama_docred_full_s1
133	
134	\paragraph{Dual-Factor Quantitative Analysis.}
135	\label{app:dual-factor}
136	
137	Figure~\ref{fig:dual-factor-scatter} plots residual DR against the product $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ for model$\times$dataset configurations.
138	For \emph{calibrated} models (Qwen3-8B, Llama-3.1-8B; unconstrained ET${<}$3\% on both datasets), a linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.886$ ($n{=}4$, $F(1,2) = 15.54$, $p \approx 0.058$); with only four data points (df $= 2$) and $p > 0.05$, this constitutes a descriptive characterization rather than a confirmatory statistical test.
139	The strong fit supports the dual-factor pattern from \S\ref{sec:composition}: residual DR is governed by the product of schema tightness and baseline violation rate.
140	Mistral-7B (unconstrained ET${=}$7.58\% on DocRED) deviates from this pattern: its residual DR on DocRED (33.21\%) substantially exceeds the linear prediction. When model calibration is insufficient (ET${>}$5\% on either dataset), residual DR is dominated by entity misclassification rather than constraint-search failure.
141	This motivates a principled exclusion criterion: models with unconstrained ET${>}$5\% on either dataset fall outside the regime where the tightness$\times$RV product is the primary DR driver.
142	The two DocRED points (high $\bar{\kappa}{=}0.842$) separate cleanly from the two SciERC points (low $\bar{\kappa}{=}0.333$), and within each dataset the model with higher baseline RV shows higher residual DR.
143	
144	\begin{figure}[t]
145	\centering
146	\includegraphics[width=0.75\columnwidth]{figures/dual_factor_scatter.pdf}
147	\caption{Residual DR vs.\ Schema Restrictiveness $\times$ Baseline Violation Rate ($\bar{\kappa} \times \text{RV}_{\text{baseline}}$) across four model$\times$dataset configurations ($n{=}3$ schemas; descriptive only).
148	Linear fit (calibrated models): $y = 0.366x - 0.138$, $R^2 = 0.886$, $p{=}0.058$ ($n{=}4$, df${=}2$; not significant); Mistral deviates due to entity misclassification.}
149	\label{fig:dual-factor-scatter}
150	\end{figure}
151	
152	%%% Dataset-Dependent F1 Impact (moved from §7) %%%
153	% exp_ids: d012_bootstrap_ci (DocRED +0.49pp p<0.001, SciERC +0.13pp p=0.58),
154	%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
155	
156	\paragraph{Dataset-Dependent F1 Impact.}
157	The divergence in F1 significance between DocRED ($+$0.49\,pp, $p < 0.001$) and SciERC ($+$0.13\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.
158	DocRED's baseline RV of 29.66\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.
159	SciERC's baseline RV is only 1.39\% (24 OOV predictions), too few to produce a detectable F1 effect.
160	Llama-3.1-8B's lower baseline RV (16.03\%) yields a smaller but directionally consistent improvement ($+$0.29\,pp vs.\ $+$0.49\,pp); F1 gain magnitude is proportional to baseline OOV rate.
161	% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained
162	% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)
163	
164	%%% Bootstrap CIs and Effect Sizes %%%
165	% exp_ids: bootstrap_ci_ft_composability, r12_table2_bootstrap_ci
166	
167	\paragraph{Bootstrap Confidence Intervals and Effect Sizes.}
168	\label{app:bootstrap-effect-sizes}
169	
170	Table~\ref{tab:bootstrap-effect-sizes} reports per-configuration bootstrap CIs and Cohen's $d$ effect sizes (10{,}000 iterations, document-level resampling, seed=42) for the fine-tuning composability results (Table~\ref{tab:composability}).
171	After Bonferroni correction for $k{=}4$ comparisons ($\alpha_{\text{adj}}{=}0.0125$), no R-F1 difference reaches significance; all R-F1 effect sizes are negligible to small ($|d| \leq 0.37$; Cohen, 1988).
172	Per-configuration corrected $p$-values: Qwen3-8B/SciERC $p_B{=}1.00$, Qwen3-8B/DocRED $p_B{=}0.224$, Llama-3.1-8B/SciERC $p_B{=}1.00$, Llama-3.1-8B/DocRED $p_B{=}1.00$.
173	Constraint enforcement thus preserves extraction quality while achieving large, highly significant reductions in domain-range violations ($|d| \geq 3.0$, all $p_{\text{Bonf}} < 0.005$).
174	
175	\begin{table}[t]
176	\centering
177	\small
178	\setlength{\tabcolsep}{3pt}
179	\begin{tabular}{@{}ll rrrr@{}}
180	\toprule
181	\textbf{Model} & \textbf{Dataset} & $\Delta$\textbf{(pp)} & \textbf{95\% CI} & $p$ & $d$ \\
182	\midrule
183	\multicolumn{6}{@{}l}{\textbf{R-F1 difference (S1 $-$ unconstrained):}} \\
184	Qwen3-8B & SciERC & $-$0.10 & [$-$0.30, 0.00] & .726 & $-$0.05 \\
185	Qwen3-8B & DocRED & $-$0.31 & [$-$0.69, $+$0.01] & .056 & $-$0.37 \\
186	Llama-3.1-8B & SciERC & $+$0.02 & [0.00, $+$0.07] & .736 & $+$0.01 \\
187	Llama-3.1-8B & DocRED & $+$0.06 & [$-$0.11, $+$0.25] & .535 & $+$0.07 \\
188	\midrule
189	\multicolumn{6}{@{}l}{\textbf{DR\% reduction:}} \\
190	Qwen3-8B & SciERC & $-$1.95 & [$-$2.87, $-$1.11] & $<$.001 & $-$6.15 \\
191	Qwen3-8B & DocRED & $-$0.75 & [$-$1.07, $-$0.48] & $<$.001 & $-$7.00 \\
192	Llama-3.1-8B & SciERC & $-$1.02 & [$-$1.98, $-$0.29] & $<$.001 & $-$3.17 \\
193	Llama-3.1-8B & DocRED & $-$0.29 & [$-$0.53, $-$0.10] & $<$.001 & $-$3.02 \\
194	\bottomrule
195	\end{tabular}
196	\caption{Bootstrap CIs and Cohen's $d$ for Table~\ref{tab:composability} (10{,}000 iterations, document-level resampling, seed=42).
197	$d$: Cohen's $d$ from pooled bootstrap SD.
198	Top: R-F1 (S1 $-$ unconstrained); no comparison significant after Bonferroni correction ($k{=}4$, $\alpha_{\text{adj}}{=}0.0125$); $|d| \leq 0.37$ (negligible--small).
199	Bottom: DR\% reduction; all $p_{\text{Bonf}} < 0.005$, $|d| \geq 3.0$ (large).}
200	\label{tab:bootstrap-effect-sizes}
201	\end{table}
202	
203	%%% Paragraph 1: Low F1 Practical Significance %%%
204	% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),
205	%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)
206	
207	\paragraph{Practical Significance of Zero-Shot F1.}
208	Our reported relation F1 of approximately 8\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.
209	For reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\% relation F1 with full training data~\citep{zhong2021frustratingly,ye2022packed}.
210	Constraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.
211	Even after LoRA fine-tuning, residual DR of 1--2\% persists on tight-constraint relations (Table~\ref{tab:composability}); constraints remain necessary at deployment-grade quality.
212	% exp_ids: w5_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_unconstrained_eval
213	In our evaluation, F1 serves as a \emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.
214	The contribution of this work is the constraint enforcement method itself; the zero-shot setting stress-tests constraint robustness under maximum model uncertainty, while composability with fine-tuning (\S\ref{sec:composability}) validates practical deployment value.
215	
216	%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%
217	% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),
218	%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)
219	
220	\paragraph{Decoding-Time vs.\ Post-Hoc Enforcement.}
221	Post-hoc filtering (generating triples without constraints, then removing schema-violating predictions) yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\ 8.36; DocRED 9.61 vs.\ 8.23).
222	% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23
223	However, this precision gain comes at substantial cost.
224	On DocRED, post-hoc filtering discards 48.1\% of all predicted triples, including 127 true positives (11.2\% of correct predictions); recall drops from 9.46\% to 8.40\%.
225	% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40
226	Entity type violations remain unresolved (ET\,=\,2.47\% vs.\ OntoCoDec's 0\%), as filtering targets only domain/range and vocabulary violations.
227	% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%
228	OntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.
229	The two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.
230	
231	%%% CF Violation Distribution %%%
232	% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),
233	%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)
234	
235	\paragraph{Cross-Field Violation Distribution.}
236	\label{app:cf-distribution}
237	
238	Table~\ref{tab:cf-distribution} reports the complete distribution of conflicting-type pairs for SciERC zero-shot S1 (248 CF violations across 245 unique entity-document pairs; no mention triggered $\geq$3 types).
239	Conflicts involving the \textsc{Generic} type account for 63.3\% (155/245) of all violations.
240	\textsc{Generic} is SciERC's anaphoric/placeholder label (``this approach'', ``the method''), which competes with every content type depending on whether the mention is used anaphorically or referentially, a distinction the per-slot constrained decoder cannot resolve without document-level coreference.
241	
242	The pattern generalizes across models and datasets: on Llama-3.1-8B SciERC, \textsc{Generic}$\leftrightarrow$\textsc{OtherScientificTerm} remains the top pair (53/162, 32.7\%); on DocRED, the analogous catch-all type \textsc{MISC} drives 76.6\% of Qwen's CF violations.
243	Under unconstrained decoding, CF rates collapse to $\leq$1\% on both datasets; CF violations are a side-effect of per-slot type commitment rather than a model deficiency.
244	
245	\begin{table}[t]
246	\centering
247	\small
248	\begin{tabular}{@{}lr r@{}}
249	\toprule
250	\textbf{Conflicting Type Pair} & \textbf{Count} & \textbf{\%} \\
251	\midrule
252	Generic $\leftrightarrow$ OtherScientificTerm & 85 & 34.7 \\
253	Generic $\leftrightarrow$ Material & 35 & 14.3 \\
254	Generic $\leftrightarrow$ Metric & 30 & 12.2 \\
255	Method $\leftrightarrow$ Task & 20 & 8.2 \\
256	Material $\leftrightarrow$ Method & 17 & 6.9 \\
257	OtherScientificTerm $\leftrightarrow$ Task & 12 & 4.9 \\
258	\midrule
259	10 further pairs (each $\leq$3.3\%) & 46 & 18.8 \\
260	\midrule
261	\textbf{Total} & \textbf{245} & 100.0 \\
262	\bottomrule
263	\end{tabular}
264	\caption{CF violation distribution on SciERC zero-shot S1 (Qwen3-8B, 551 documents).
265	All 245 unique entity-document pairs involve pairwise conflicts.
266	Conflicts involving \textsc{Generic} account for 63.3\%.}
267	\label{tab:cf-distribution}
268	\end{table}
269	
270	%%% Cascade Error Analysis %%%
271	% exp_ids: phase2_scierc_full_s1 (ZS: CF=248), w5_lora_scierc_full_s1_eval (FT: CF=22)
272	
273	\paragraph{Cascade Error Analysis.}
274	\label{app:cascade-analysis}
275	
276	Table~\ref{tab:cascade-breakdown} decomposes zero-shot CF violations by source mechanism.
277	The dominant source is hallucinated entities (58.1\%): the model generates entity names absent from the input document, and the entity registry assigns a type based on the first occurrence that may conflict with a subsequent valid entity sharing the same surface form.
278	True cascade errors---where first-seen type registration for a \emph{real} entity locks an incorrect type that blocks a subsequent valid assignment---account for only 7.3\% (18/248).
279	Correct type locks (first-seen type is correct and prevents an incorrect subsequent assignment) are 2.5$\times$ more frequent (18.1\%, 45/248), indicating that the first-seen registration mechanism provides a net benefit for type consistency.
280	
281	Under fine-tuning (22 CF violations, 20 documents), cascade errors are completely eliminated (0/22): LoRA training calibrates entity typing sufficiently that first-seen registrations are consistently correct.
282	This confirms that cascade errors are a model calibration issue exposed by the constraint mechanism, not an inherent deficiency of first-seen registration.
283	
284	\begin{table}[h]
285	\centering
286	\small
287	\begin{tabular}{@{}l rr@{}}
288	\toprule
289	\textbf{CF Source Category} & \textbf{Count} & \textbf{\%} \\
290	\midrule
291	Hallucinated entity & 144 & 58.1 \\
292	Correct type lock & 45 & 18.1 \\
293	True cascade error & 18 & 7.3 \\
294	Other / ambiguous & 41 & 16.5 \\
295	\midrule
296	\textbf{Total} & \textbf{248} & 100.0 \\
297	\bottomrule
298	\end{tabular}
299	\caption{CF violation source breakdown on SciERC zero-shot S1 (Qwen3-8B, 551 documents; exp\_id: phase2\_scierc\_full\_s1).
300	``Hallucinated entity'': generated entity absent from input.
301	``True cascade error'': first-seen lock on incorrect type blocks valid subsequent assignment.
302	``Correct type lock'': first-seen type correct, prevents incorrect subsequent type.
303	Under fine-tuning, cascade errors are completely eliminated (0/22 CF violations; exp\_id: w5\_lora\_scierc\_full\_s1\_eval).}
304	\label{tab:cascade-breakdown}
305	\end{table}
306	
307	%%% Per-Relation DR Elimination under Fine-Tuning %%%
308	% exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1
309	
310	\paragraph{Per-Relation DR Elimination under Fine-Tuning.}
311	\label{app:lora-per-relation}
312	
313	Table~\ref{tab:lora-per-relation} presents the per-relation breakdown of DR elimination when OntoCoDec is composed with LoRA fine-tuning on SciERC.
314	Fine-tuning alone eliminates DR on four of seven relations but leaves non-zero violations on the three tightest-constraint relations: \textsc{Evaluate-for} ($\kappa{=}0.361$, 13.13\%), \textsc{Part-of} ($\kappa{=}0.417$, 5.77\%), and \textsc{Compare} ($\kappa{=}0.528$, 5.00\%).
315	Adding OntoCoDec constraints eliminates all remaining violations across all relations.
316	One \textsc{Evaluate-for} triple (99\,$\to$\,98) is redirected to \textsc{Used-for} (634\,$\to$\,635) by token-level masking: the head entity's registered type falls outside \textsc{Evaluate-for}'s domain, and the semantic mask steers generation to the nearest valid relation.
317	
318	\begin{table}[t]
319	\centering
320	\small
321	\begin{tabular}{@{}l r rr rr@{}}
322	\toprule
323	& & \multicolumn{2}{c}{\textbf{LoRA Unconstr.}} & \multicolumn{2}{c}{\textbf{LoRA + S1}} \\
324	\cmidrule(lr){3-4} \cmidrule(l){5-6}
325	\textbf{Relation} & $\kappa$ & DR\,(\%) & $n$ & DR\,(\%) & $n$ \\
326	\midrule
327	Evaluate-for & 0.361 & 13.13 & 99 & \textbf{0} & 98 \\
328	Part-of      & 0.417 & 5.77  & 52 & \textbf{0} & 52 \\
329	Compare      & 0.528 & 5.00  & 40 & \textbf{0} & 40 \\
330	Conjunction  & 0.306 & 1.31  & 153 & \textbf{0} & 153 \\
331	Feature-of   & 0.278 & 1.35  & 74 & \textbf{0} & 74 \\
332	Used-for     & 0.028 & 0.16  & 634 & \textbf{0} & 635 \\
333	Hyponym-of   & 0.417 & 0     & --- & \textbf{0} & --- \\
334	\bottomrule
335	\end{tabular}
336	\caption{Per-relation DR elimination on SciERC with LoRA fine-tuning (Qwen3-8B).
337	$\kappa$: constraint tightness; $n$: predicted triple count.
338	Used-for gains one triple from Evaluate-for redirection.}
339	\label{tab:lora-per-relation}
340	\end{table}
341	
342	%%% Fine-Tuned Four-Way Ablation %%%
343	% exp_ids: w5_lora_scierc_*, w5_llama_lora_scierc_*, w5_qwen_docred_*, w5_llama_docred_*, w8_*
344	
345	\paragraph{Fine-Tuned Four-Way Ablation.}
346	\label{app:ft-ablation}
347	
348	Table~\ref{tab:ft-ablation} presents the four-way constraint ablation on fine-tuned models across both datasets, isolating each layer's contribution when the base model has already internalized schema knowledge.
349	
350	\begin{table}[t]
351	\centering
352	\small
353	\setlength{\tabcolsep}{3pt}
354	\resizebox{\columnwidth}{!}{%
355	\begin{tabular}{@{}lll rrrrr rr@{}}
356	\toprule
357	\textbf{Dataset} & \textbf{Model} & \textbf{Mode} & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF} & \textbf{PF} & \textbf{E-F1\,$\uparrow$} & \textbf{R-F1\,$\uparrow$} \\
358	\midrule
359	\multirow{8}{*}{SciERC}
360	  & \multirow{4}{*}{Qwen3-8B}
361	    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
362	  & & Grammar       & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
363	  & & Semantic      & 0.60 & 0.00 & 0.00 & 0.18 & 0.00 & 67.05 & 43.69 \\
364	  & & S1       & \textbf{0}    & 0.00 & 0.00 & 1.18 & 0.00 & 67.05 & 43.77 \\
365	  \cmidrule(l){2-10}
366	  & \multirow{4}{*}{Llama-3.1-8B}
367	    & Unconstrained & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
368	  & & Grammar       & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
369	  & & Semantic      & 0.65 & 0.00 & 0.00 & 0.10 & 0.00 & 67.76 & 45.47 \\
370	  & & S1       & \textbf{0.09} & 0.00 & 0.00 & 0.46 & 0.00 & 67.76 & 45.47 \\
371	\midrule
372	\multirow{8}{*}{DocRED}
373	  & \multirow{4}{*}{Qwen3-8B}
374	    & Unconstrained & 0.76 & 0.27 & 0.00 & 0.12 & 7.11 & 82.15 & 40.86 \\
375	  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\
376	  & & Semantic      & 0.19 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.85 \\
377	  & & S1       & \textbf{0.01} & 0.00 & 0.00 & 0.41 & 8.52 & 81.43 & 40.56 \\
378	  \cmidrule(l){2-10}
379	  & \multirow{4}{*}{Llama-3.1-8B}
380	    & Unconstrained & 0.49 & 0.15 & 0.00 & 0.08 & 2.30 & 83.93 & 43.72 \\
381	  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.72 \\
382	  & & Semantic      & 0.48 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.85 \\
383	  & & S1       & \textbf{0.21} & 0.00 & 0.00 & 0.21 & 2.51 & 83.94 & 43.78 \\
384	\bottomrule
385	\end{tabular}}%
386	\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\times$ 2 datasets).
387	DR/RV/ET: violation rates (\%) over predicted relations; CF: over predicted entities; PF: parse failure rate (\%); F1 $\times$100.
388	Grammar layer is a no-op post-fine-tuning (DR change $<$0.2\,pp in all 4 settings; RV and ET already 0\% without constraints).
389	Semantic layer is the sole effective DR defense (41--69\% on SciERC, 2--75\% on DocRED); the near-zero Llama DocRED reduction reflects a near-floor baseline (DR${=}$0.49\%).
390	F1 cost is negligible: max $\Delta$R-F1 = $-$0.30\,pp (Qwen DocRED, full vs.\ unconstrained).}
391	\label{tab:ft-ablation}
392	\end{table}
393	
394	The grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\% without constraints, and grammar-only DR change is $<$0.2\,pp (4/4 settings).
395	The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 41--69\% on SciERC (Qwen $-$69\%, Llama $-$41\%) and 2--75\% on DocRED (Qwen $-$75\%, Llama $-$2\%); the near-zero Llama DocRED reduction reflects a near-floor baseline (DR${=}$0.49\%, 80 violations in 16{,}074 triples), where the semantic layer has minimal room to improve.
396	Adding both layers achieves near-complete elimination (DR\,$\leq$\,0.21\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.
397	F1 cost is negligible: the maximum R-F1 decrease across S1 vs.\ unconstrained is $-$0.30\,pp (Qwen DocRED).
398	
399	%%% DocRED Zero-Shot Ablation (moved from main text) %%%
400	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
401	%          phase2_docred_semantic_only, phase2_docred_full_s1
402	
403	\paragraph{DocRED Zero-Shot Ablation.}
404	\label{app:docred-zs-ablation}
405	
406	Table~\ref{tab:docred-ablation} presents the four-way constraint ablation on DocRED under zero-shot decoding, parallel to the SciERC ablation in Table~\ref{tab:scierc-ablation}.
407	
408	\begin{table}[t]
409	\centering
410	\small
411	\setlength{\tabcolsep}{3.6pt}
412	\resizebox{\columnwidth}{!}{%
413	\begin{tabular}{@{}l rrrrrr rr@{}}
414	\toprule
415	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
416	& \multicolumn{2}{c}{\textbf{F1}} \\
417	\cmidrule(lr){2-7} \cmidrule(l){8-9}
418	\textbf{Mode}
419	  & DR\,$\downarrow$ & $\Delta$DR
420	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
421	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
422	\midrule
423	Unconstrained
424	  & 18.46 & ---
425	  & 29.66 & 2.48
426	  & 0.10  & 18.56
427	  & 7.74  & 58.15 \\
428	Grammar
429	  & 26.17 & $\uparrow$42\%
430	  & \textbf{0.03} & \textbf{0}
431	  & 0.07  & 26.24
432	  & \textbf{8.31}  & \textbf{59.38} \\
433	Semantic
434	  & 13.84 & $\downarrow$25\%
435	  & 29.87 & 4.22
436	  & 1.05  & 14.89
437	  & 7.70  & 57.81 \\
438	S1
439	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
440	  & \textbf{0.03} & \textbf{0}
441	  & 2.57  & \textbf{12.78}
442	  & 8.23  & 59.37 \\
443	\bottomrule
444	\end{tabular}}%
445	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
446	$\Delta$DR: relative change vs.\ unconstrained.
447	Tot.\ = DR + CF (total type-violation burden).
448	Best per column in \textbf{bold} (CF excluded; Tot.\ included).
449	F1 $\times$100. Bootstrap significance: R-F1 $+$0.49\,pp ($p < 0.001$).
450	Grammar-only $\uparrow$DR: vocabulary enforcement makes OOV outputs evaluable, exposing latent violations (see \S\ref{sec:docred-results}).}
451	\label{tab:docred-ablation}
452	\end{table}
453	
454	%%% Residual DR Error Analysis (Fine-Tuned) %%%
455	% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*
456	
457	\paragraph{Residual DR Error Analysis.}
458	\label{app:residual-dr-analysis}
459	
460	Across all fine-tuned settings (2 models $\times$ 2 datasets $\times$ S1), only 36 domain/range violations remain.
461	Manual inspection reveals four root causes:
462	
463	\begin{enumerate}[nosep,leftmargin=*]
464	\item \emph{Entity type errors} (39\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \textsc{LOC} when the gold standard requires \textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.
465	\item \emph{Schema coverage gaps} (33\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.
466	\item \emph{Incorrect relation selection} (17\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.
467	\item \emph{Direction reversal} (11\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.
468	\end{enumerate}
469	
470	Two dataset-specific patterns emerge.
471	Outside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps: the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.
472	On DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\%), with entity type errors as the dominant cause (14/33, 42\%).
473	This asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 6 entity types) compared to Qwen, which achieves near-zero residual.
474	The implication is twofold: (i)~the irreducible floor from schema gaps is small ($\sim$3 violations across 4 settings), so the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.
475	
476	%%% Post-Hoc Filtering Comparison (Extended) %%%
477	% exp_ids: posthoc_*_zs, posthoc_*_ft
478	
479	\paragraph{Post-Hoc Filtering: Extended Comparison.}
480	\label{app:posthoc-extended}
481	
482	Table~\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.
483	
484	\begin{table}[t]
485	\centering
486	\small
487	\setlength{\tabcolsep}{3pt}
488	\resizebox{\columnwidth}{!}{%
489	\begin{tabular}{@{}lll rrr l@{}}
490	\toprule
491	\textbf{Setting} & \textbf{Model} & \textbf{Dataset} & \textbf{Reject\%} & \textbf{R-F1$_{\text{ph}}$} & \textbf{R-F1$_{\text{cd}}$} & \textbf{Winner} \\
492	\midrule
493	\multirow{6}{*}{ZS}
494	  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\
495	  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\
496	  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\
497	  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\
498	  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\
499	  & Mistral & DocRED & \textbf{73.7} & 3.85  & \textbf{5.52} & cd \\
500	\midrule
501	\multirow{4}{*}{FT}
502	  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\
503	  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\
504	  & Qwen    & DocRED & 1.03 & 41.11 & 40.79 & ph \\
505	  & Llama   & DocRED & 0.64 & 43.92 & 43.78 & cd \\
506	\bottomrule
507	\end{tabular}}%
508	\caption{Post-hoc filtering (ph) vs.\ constrained decoding (cd).
509	In zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.
510	At reject rate $>$70\% (Mistral DocRED), post-hoc F1 collapses below constrained.
511	Under fine-tuning, rejection rates drop to 0.6--2.0\% and the two strategies are equivalent ($\Delta \leq 0.55$\,pp; each wins two groups).
512	F1 $\times$100.}
513	\label{tab:posthoc-extended}
514	\end{table}
515	
516	The crossover point occurs when post-hoc rejection exceeds $\sim$70\%: Mistral DocRED rejects 73.7\% of predicted triples, discarding enough true positives that constrained decoding's recall advantage dominates ($+$1.67\,pp).
517	OntoCoDec's advantage thus scales with violation severity: precisely when constraints are most needed, post-hoc filtering is most destructive.
518	Under fine-tuning, both strategies converge because few violations remain to filter or constrain ($\Delta \leq 0.55$\,pp across all four FT groups, with each strategy winning two).
519	
520	%%% Zero-Shot Runtime Profiling %%%
521	
522	\paragraph{Zero-Shot Runtime Profiling.}
523	\label{app:runtime}
524	
525	On SciERC (Qwen3-8B, zero-shot greedy, NVIDIA RTX PRO 6000 Blackwell Server Edition), unconstrained inference averages 4.163\,s/doc and S1 constrained decoding averages 4.710\,s/doc ($+$13.1\% overhead).
526	On DocRED (same configuration), relative overhead is lower due to amortization: the fixed per-token constraint cost is spread over longer generation sequences.
527	XGrammar automaton compilation takes 0.044\,s; the full constraint pipeline (schema parsing, JSON Schema generation, grammar compilation) takes 0.33\,s on SciERC (Table~\ref{tab:scalability}), amortized to zero over the evaluation set.
528	
529	% exp_id: p8c_ft_scierc_latency — Reviewer Report #23 verified
530	\paragraph{Fine-Tuned Latency Profiling.}
531	\label{app:ft-latency}
532	Under LoRA fine-tuning (same hardware and dataset), unconstrained inference averages 2.612\,s/doc and S1 constrained decoding averages 2.873\,s/doc ($+$10.0\% overhead, $n{=}551$).
533	Fine-tuned models generate shorter, more structured outputs than zero-shot models (2.612\,s vs.\ 4.163\,s/doc unconstrained); absolute generation time drops by 37\%.
534	The relative overhead ($+$10.0\%) is slightly lower than zero-shot ($+$13.1\%), consistent with shorter sequences requiring fewer constraint checks per document.
535	
536	%%% Fuzzy Relation Matching %%%
537	
538	\paragraph{Relation Matching Protocol.}
539	\label{app:fuzzy-matching}
540	Relation F1 evaluation uses fuzzy normalization to handle model-specific formatting variants (e.g., underscores vs.\ spaces, abbreviations).
541	A predicted relation $r_p$ matches gold relation $r_g$ if: (1)~exact string match after case-insensitive normalization, or (2)~token overlap $>$80\% \emph{and} edit distance $\leq 2$.
542	This protocol affects primarily Mistral, which produces underscore-separated variants (e.g., ``head\_of\_government'' for ``head of government'').
543	On Mistral DocRED, fuzzy matching contributes 98 additional TPs ($+$0.84\,pp R-F1; strict R-F1\,=\,3.50\% vs.\ fuzzy 4.34\%).
544	For Qwen and Llama under grammar constraints, the grammar layer enforces exact relation names, making fuzzy matching irrelevant (0 additional matches).
545	All F1 figures in the main text use fuzzy normalization consistently across all models and conditions.
546	
547	%%% Per-Relation Violation Landscape %%%
548	
549	\paragraph{Per-Relation Violation Landscape.}
550	\label{app:per-relation-landscape}
551	
552	Table~\ref{tab:prompt_comparison} compares violation rates under unconstrained and schema-informed prompting.
553	Figure~\ref{fig:per_relation_dr} shows the per-relation DR distribution on SciERC.
554	
555	\begin{table}[t]
556	\centering
557	\small
558	\caption{Violation rates (\%) under unconstrained and schema-informed prompting (Qwen3-8B, zero-shot).}
559	\label{tab:prompt_comparison}
560	\resizebox{\columnwidth}{!}{%
561	\begin{tabular}{ll cccc}
562	\toprule
563	Dataset & Prompt & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & CF$\downarrow$ \\
564	\midrule
565	\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\
566	 & Schema-informed & 5.8 & 0.3 & \textbf{0.0} & --- \\
567	\midrule
568	\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\
569	 & Schema-informed & 12.8 & 18.4 & 0.2 & 0.2 \\
570	\bottomrule
571	\end{tabular}}
572	\end{table}
573	
574	\begin{figure}[t]
575	\centering
576	\includegraphics[width=\columnwidth]{figures/fig2_per_relation_dr.pdf}
577	\caption{Per-relation DR violation rates on SciERC (Qwen3-8B, unconstrained). Rates correlate with constraint tightness $\kappa(r)$. Llama-3.1-8B shows similar per-relation patterns (Appendix~\ref{app:llama-per-relation}).}
578	\label{fig:per_relation_dr}
579	\end{figure}
580	
581	%%% WikiEvents Extended %%%
582	
583	\paragraph{WikiEvents Dataset Details.}
584	\label{app:wikievents}
585	WikiEvents~\cite{li2021document} is a document-level event argument extraction benchmark grounded in the DARPA KAIROS ontology.
586	It defines 56 event types, 80 argument roles, and 27 entity types, with 245 (event\_type, role)$\to$allowed\_entity\_types constraints.
587	The grammar layer targets EV (event vocabulary), RoV (role vocabulary), and ET; the semantic layer enforces AC (argument constraint) via role-conditioned masking, analogous to RE domain/range enforcement.
588	
589	\paragraph{Constraint Tightness in WikiEvents.}
590	\label{app:wikievents-kappa}
591	% Data source: artifacts/w1c_wikievents_kappa_results.md
592	WikiEvents role-level tightness (with $|\mathcal{E}|{=}27$) has mean $\bar{\kappa}{=}0.82$ and median 0.89; 84\% of roles have $\kappa \geq 0.80$ (4 or fewer valid entity types out of 27).
593	The tightness-violation pattern extends to event extraction: roles with $\kappa \geq 0.90$ exhibit the highest AC rate (50\%), compared to 21\% for medium-tightness ($0.80 \leq \kappa < 0.90$) and 30\% for loose ($\kappa < 0.80$) roles; this is consistent with the RE observation that constraint tightness correlates with violation frequency.
594	However, the correlation is modulated by entity type prototypicality: semantically intuitive roles (e.g., Transportation.Vehicle$\to$VEH) show 0\% AC despite $\kappa{=}0.963$, while roles that require rare KAIROS-specific types (e.g., Crime$\to$CRM, Sentence$\to$SEN) show near-100\% AC because LLMs default to common types (PER, ORG).
595	The loose group's elevated rate (30\%) is driven by high-frequency roles such as Attack.Target (126 args, 34\% AC, $\kappa{=}0.59$), where systematic model errors outweigh the permissive constraint space.
596	
597	%%% Lucky Violation Analysis %%%
598	% exp_ids: task_e_lucky_violation_analysis
599	
600	\paragraph{Lucky Violation Analysis.}
601	\label{app:lucky-violations}
602	Table~\ref{tab:lucky-violations} quantifies the recall cost of DR elimination.
603	A ``lucky violation'' is a constraint-removed triple that happens to match a gold label---an ontologically invalid prediction that is nonetheless correct.
604	Across four fine-tuned configurations, lucky violations average 0.49\% of gold triples (range 0.01--0.51\%), confirming that nearly all removed DR violations are false positives.
605	On Llama SciERC, all five lucky violations are recovered as legal type paths under constrained decoding (zero churn): the model finds an ontology-compliant route to the same prediction.
606	
607	\begin{table}[h]
608	\centering
609	\small
610	\resizebox{\columnwidth}{!}{%
611	\begin{tabular}{@{}llrrrr@{}}
612	\toprule
613	\textbf{Model} & \textbf{Dataset} & \textbf{DR (\%)} & \textbf{Lucky} & \textbf{$\Delta$Recall} & \textbf{Churn} \\
614	& & \textbf{unc$\to$con} & \textbf{(\% gold)} & \textbf{(pp)} & \textbf{(\%)} \\
615	\midrule
616	Qwen3-8B  & SciERC & 1.95$\to$0    & 4 (0.41\%) & $-$0.10 & 0.22 \\
617	Llama-8B  & SciERC & 1.11$\to$0.09 & 5 (0.51\%) & $\pm$0.00 & 0 \\
618	Qwen3-8B  & DocRED & 1.03$\to$0.01 & 1 (0.01\%) & $-$0.84 & 2.05 \\
619	Llama-8B  & DocRED & 0.64$\to$0.21 & 1 (0.01\%) & $-$0.10 & 0.86 \\
620	\midrule
621	\multicolumn{2}{@{}l}{\textit{Average}} & & \textit{0.49\%} & $-$0.26 & 0.78 \\
622	\bottomrule
623	\end{tabular}}
624	\caption{Lucky violation analysis across four LoRA fine-tuned configurations.
625	Lucky: count (and \% of gold triples) of constraint-removed violations matching gold labels.
626	$\Delta$Recall: recall change from unconstrained to constrained.
627	Churn: fraction of gold-matching triples whose predictions change (including recovery via legal type paths).}
628	\label{tab:lucky-violations}
629	\end{table}
630	
631	%%% Trie-Only Baseline %%%
632	% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc
633	
634	\paragraph{Trie-Only Baseline (GCD-Equivalent).}
635	\label{app:trie-baseline}
636	Table~\ref{tab:trie-baseline} isolates the effect of vocabulary membership constraints without JSON structural enforcement.
637	The trie constrains entity type and relation tokens to schema-valid values (achieving ET${=}$0\%, RV${=}$0\% across all configurations), functionally equivalent to GCD's~\cite{geng2023gcd} constrained decoding.
638	However, without grammar-level JSON enforcement, models systematically omit entity type fields (83\% of triples) or produce malformed JSON (0--51\% parse failure), causing DR to rise to 15--96\%---far worse than unconstrained baselines.
639	The effect is most dramatic for Llama-8B LoRA: 50.8\% parse failure causes R-F1 to collapse from 45.47 (OntoCoDec S1) to 19.95, demonstrating that the grammar layer is not merely helpful but a structural prerequisite---vocabulary constraints require JSON scaffolding to reach the positions where they apply.
640	
641	\begin{table}[h]
642	\centering
643	\small
644	\resizebox{\columnwidth}{!}{%
645	\begin{tabular}{@{}ll rrrr rr@{}}
646	\toprule
647	\textbf{Model} & \textbf{Setting}
648	  & \textbf{ET\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{DR\,$\downarrow$} & \textbf{CF}
649	  & \textbf{R-F1\,$\uparrow$} & \textbf{PF\,(\%)} \\
650	\midrule
651	\multirow{2}{*}{Qwen3-8B}
652	  & LoRA  & 0 & 0 & 95.5  & 0.09 & 41.16 & 9.1 \\
653	  & ZS    & 0 & 0 & 29.3  & 0    & 8.64  & 0 \\
654	\multirow{2}{*}{Llama-8B}
655	  & LoRA  & 0 & 0 & 15.2$^\dagger$  & 0    & 19.95 & 50.8 \\
656	  & ZS    & 0 & 0 & 84.4  & 0.36 & 2.90  & 0 \\
657	\midrule
658	\multicolumn{8}{@{}l}{\textit{Comparison with OntoCoDec S1:}} \\
659	\midrule
660	& & \multicolumn{2}{c}{\textbf{S1 DR\,(\%)}} & \textbf{Trie DR\,(\%)} & \multicolumn{2}{c}{\textbf{DR Gap (pp)}} & \\
661	\cmidrule(lr){3-4} \cmidrule(lr){5-5} \cmidrule(lr){6-7}
662	Qwen3-8B  & LoRA  & \multicolumn{2}{c}{0}    & 95.5  & \multicolumn{2}{c}{95.5}  & \\
663	Qwen3-8B  & ZS    & \multicolumn{2}{c}{0.93} & 29.3  & \multicolumn{2}{c}{28.4}  & \\
664	Llama-8B  & LoRA  & \multicolumn{2}{c}{0.09} & 15.2  & \multicolumn{2}{c}{15.1}  & \\
665	Llama-8B  & ZS    & \multicolumn{2}{c}{0.08} & 84.4  & \multicolumn{2}{c}{84.3}  & \\
666	\bottomrule
667	\end{tabular}}
668	\caption{Trie-only baseline (GCD-equivalent, vocabulary membership without JSON grammar) on SciERC.
669	Top: full trie-only metrics (ET/RV/DR/CF: violation rates \%; R-F1 $\times$100; PF: parse failure rate).
670	Trie achieves ET${=}$0\%, RV${=}$0\% but DR rises to 15--96\% because models omit type fields without structural enforcement.
671	Bottom: DR gap between OntoCoDec S1 and trie-only, quantifying the grammar layer's contribution.
672	$^\dagger$50.8\% parse failure rate.}
673	\label{tab:trie-baseline}
674	\end{table}
675	
676	%%% GCD/BoostCD Equivalence Comparison %%%
677	
678	\paragraph{Comparison with Grammar-Based Constrained Decoding.}
679	\label{app:gcd-comparison}
680	
681	Table~\ref{tab:gcd-comparison} summarizes the relationship between OntoCoDec's constraint layers and existing grammar-based constrained decoding methods.
682	
683	\begin{table}[h]
684	\centering
685	\small
686	\resizebox{\columnwidth}{!}{%
687	\begin{tabular}{@{}l l l l l l@{}}
688	\toprule
689	\textbf{Method} & \textbf{Constraint Type} & \textbf{Level} & \textbf{DR Red.} & \textbf{CF} & \textbf{State} \\
690	\midrule
691	GCD~\cite{geng2023gcd} & CFG (JSON schema) & Grammar & ${\sim}$3\% & N/A & Stateless \\
692	BoostCD~\cite{boostcd2025} & CFG + beam rerank & Grammar & ${\sim}$3\%$^\dagger$ & N/A & Stateless \\
693	Trie-Only (Tab.~\ref{tab:trie-baseline}) & Prefix trie & Vocab & 0\%$^\ddagger$ & N/A & Stateless \\
694	\midrule
695	vLLM \texttt{guided\_json}~\cite{kwon2023vllm} & JSON Schema & Grammar & ${\sim}$3\%$^\S$ & N/A & Stateless \\
696	\midrule
697	OntoCoDec Grammar & CFG (XGrammar) & Grammar & ${\sim}$3\% & N/A & Stateless \\
698	OntoCoDec S1 & CFG + type constr. & Gram.+Sem. & 94--100\% (FT) & ${\leq}$1.4\% (FT) & Entity reg. \\
699	\bottomrule
700	\end{tabular}}
701	\caption{Comparison with grammar-based constrained decoding methods.
702	$^\dagger$Equivalent mechanism; BoostCD adds beam-level reranking but the CFG enforcement is identical.
703	$^\ddagger$Vocabulary-only constraints without JSON structure cause DR to \emph{increase} (15--96\%; Table~\ref{tab:trie-baseline}).
704	$^\S$Experimentally verified: DR${=}$15.26\% vs.\ grammar-only 14.84\% ($\Delta{<}$0.5\,pp; Table~\ref{tab:vllm-verification}).
705	Grammar-only results are analytically equivalent to GCD/BoostCD (same CFG enforcement; \S\ref{sec:related_work}).}
706	\label{tab:gcd-comparison}
707	\end{table}
708	
709	Our grammar layer implements the same CFG-based token masking as GCD and BoostCD---the mechanisms are formally identical (JSON schema $\to$ pushdown automaton $\to$ per-step allowed token set).
710	Table~\ref{tab:scierc-ablation} row~2 therefore constitutes a direct comparison: grammar-only enforcement achieves RV/ET$\to$0\% but only ${\sim}$3\% DR reduction, identical to what GCD-family methods would achieve on IE tasks.
711	
712	% exp_id: vllm_guided_json_scierc_zs
713	\paragraph{External verification via vLLM.}
714	To confirm this equivalence experimentally, we evaluated vLLM's \texttt{guided\_json} mode~\cite{kwon2023vllm}---an independent CFG enforcement implementation---on SciERC under identical conditions (Qwen3-8B, zero-shot, 551 documents).
715	
716	\begin{table}[h]
717	\centering
718	\small
719	\begin{tabular}{@{}l rrrr r@{}}
720	\toprule
721	\textbf{Method} & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF} & \textbf{R-F1\,$\uparrow$} \\
722	\midrule
723	Grammar-Only (XGrammar) & 14.84 & 0 & 0 & 9.90 & 8.23 \\
724	vLLM \texttt{guided\_json} & 15.26 & 0 & 0 & --- & 8.75 \\
725	\midrule
726	$\Delta$ & $+$0.42 & 0 & 0 & --- & $+$0.52 \\
727	\bottomrule
728	\end{tabular}
729	\caption{GCD-equivalence verification: OntoCoDec grammar-only vs.\ vLLM \texttt{guided\_json} on SciERC (Qwen3-8B, zero-shot, 551 documents). All differences $<$0.5\,pp, confirming that CFG-based approaches---regardless of implementation---leave ${\sim}$15\% DR violations unaddressed.}
730	\label{tab:vllm-verification}
731	\end{table}
732	
733	All metrics differ by $<$0.5\,pp (Table~\ref{tab:vllm-verification}), confirming that any CFG-based constrained decoding tool---whether GCD, BoostCD, or vLLM---enforces the same constraint class and leaves the same ${\sim}$15\% DR gap.
734	The critical gap these methods cannot address is cross-field type consistency (Level~2), which requires the stateful semantic layer that maintains an entity registry across relation slots and enforces per-relation domain/range constraints at each type-bearing position.
735	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f4f1464-678b-460c-8078-c2b30ba96565",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "04ab2d42-fbaa-432d-aecf-f7308fc889c3",
  "sourceToolAssistantUUID": "8f4f1464-678b-460c-8078-c2b30ba96565",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-23T18:11:17.868Z_

Now let me read the registry and the remaining paper files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04ab2d42-fbaa-432d-aecf-f7308fc889c3",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx8foHLNHXrJtppNHRe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b23754d9-93db-47e4-8ff1-35ff04a5ca09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Qc9zGzA3nukZcsLpkR7KyF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26333,
      "cache_read_input_tokens": 37302,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26333,
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

_source line 18 · 2026-05-23T18:11:19.162Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LaYD2CTFKrPMi8pjovLdbW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b23754d9-93db-47e4-8ff1-35ff04a5ca09",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx8foHLNHXrJtppNHRe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e88bbb70-9d22-4b68-9604-0079bf6ef886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Qc9zGzA3nukZcsLpkR7KyF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26333,
      "cache_read_input_tokens": 37302,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26333,
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

_source line 19 · 2026-05-23T18:11:19.167Z_

<details><summary>↩ Tool result · reported error · `toolu_01LaYD2CTFKrPMi8pjovLdbW`</summary>

```text
File content (305.3KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e88bbb70-9d22-4b68-9604-0079bf6ef886",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "f727ab5b-d599-4d3d-a9a9-2aacbcd32946",
  "toolUseResult": "Error: File content (305.3KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "e88bbb70-9d22-4b68-9604-0079bf6ef886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-23T18:11:19.990Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ThJCPsyqt1aRs563BsP6az`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f727ab5b-d599-4d3d-a9a9-2aacbcd32946",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx8foHLNHXrJtppNHRe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "165e22fe-fc3a-4a55-9c24-689925abd18e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Qc9zGzA3nukZcsLpkR7KyF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26333,
      "cache_read_input_tokens": 37302,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26333,
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

_source line 21 · 2026-05-23T18:11:20.003Z_

<details><summary>↩ Tool result · `toolu_01ThJCPsyqt1aRs563BsP6az`</summary>

```text
1	% Appendix: 70B-Class LoRA Ablation on SciERC
2	% exp_ids: eval_70b_lora_scierc_unconstrained, eval_70b_lora_scierc_grammar_only,
3	%          eval_70b_lora_scierc_semantic_only, eval_70b_lora_scierc_s1_constrained,
4	%          eval_70b_lora_scierc_s2_constrained, eval_70b_lora_scierc_beam4_s1
5	
6	\paragraph{70B-class fine-tuned ablation.}
7	\label{app:70b-ablation}
8	
9	Table~\ref{tab:70b-ft-ablation} presents the constraint ablation on Llama-3.1-70B-Instruct (AWQ INT4) with LoRA fine-tuning on SciERC (551 documents).
10	
11	\begin{table}[h]
12	\centering
13	\small
14	\setlength{\tabcolsep}{3.6pt}
15	\begin{tabular}{@{}l rrrr rr@{}}
16	\toprule
17	\textbf{Mode}
18	  & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF}
19	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$} \\
20	\midrule
21	Unconstrained & 1.50 & 0 & 0 & 0    & 44.73 & 64.86 \\
22	Grammar       & 1.50 & 0 & 0 & 0    & 44.63 & 64.82 \\
23	Semantic      & 0.60 & 0 & 0 & 9    & 44.73 & 64.86 \\
24	S1            & \textbf{0} & 0 & 0 & 15 & 44.53 & 64.76 \\
25	S2            & \textbf{0} & 0 & 0 & 18 & 36.28 & 62.35 \\
26	Beam4 S1      & \textbf{0} & 0 & 0 & \textbf{1} & \textbf{44.81} & \textbf{64.89} \\
27	\bottomrule
28	\end{tabular}
29	\caption{70B-class (Llama-3.1-70B-Instruct (AWQ INT4)) LoRA ablation on SciERC (551 docs).
30	CF: violation count. F1 $\times$100.}
31	\label{tab:70b-ft-ablation}
32	\end{table}
33	
34	The grammar layer provides no independent DR benefit at 70B (1.50\%\,$\to$\,1.50\% on SciERC; on DocRED zero-shot, DR actually increases $+$3.58\,pp due to RV$\to$DR conversion in the high-$\bar{\kappa}$ schema; Table~\ref{tab:70b-docred-zs-ablation}).
35	The semantic layer is the sole effective defense (1.50\%\,$\to$\,0.60\%, 60\% reduction) with no R-F1 cost ($\Delta{=}$0\,pp), and full S1 eliminates all DR.
36	S2 eliminates DR but causes severe R-F1 degradation ($-$8.45\,pp), indicating that optimal constraint granularity is scale-dependent: the additional S2 constraints become overly restrictive at 70B, where stronger baseline generation makes fine-grained intervention counterproductive.
37	Beam ($k{=}4$) S1 remains the optimal configuration (DR${=}$0\%, CF${=}$1, R-F1${=}$44.81).
38	Notably, S2 increases CF from 15 (S1) to 18 despite its cross-field consistency design, suggesting that over-constraining induces cascading generation degradation that creates new violations.
39	
40	% exp_ids: eval_70b_lora_docred_200_unconstrained, eval_70b_lora_docred_200_grammar_only,
41	%          eval_70b_lora_docred_200_semantic_only, eval_70b_lora_docred_200_s1_constrained,
42	%          eval_70b_lora_docred_200_full_s2, eval_70b_lora_docred_200_beam4_s1
43	\paragraph{70B-class DocRED results.}
44	\label{app:70b-docred}
45	
46	Table~\ref{tab:70b-docred-ablation} presents the six-way constraint ablation on Llama-3.1-70B-Instruct (AWQ INT4) with LoRA fine-tuning on DocRED (998 documents).
47	
48	\begin{table}[h]
49	\centering
50	\small
51	\setlength{\tabcolsep}{3.6pt}
52	\begin{tabular}{@{}l rrrr rr@{}}
53	\toprule
54	\textbf{Mode}
55	  & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF}
56	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$} \\
57	\midrule
58	Unconstrained & 0.22 & 0.57 & 0 & 2      & 43.80 & 80.34 \\
59	Grammar       & 0.38 & 0    & 0 & 0.06\%$^\dagger$ & 43.96 & 80.13 \\
60	Semantic      & \textbf{0} & 0.51 & 0 & 0.21\%$^\dagger$ & 43.61 & 80.06 \\
61	S1            & \textbf{0} & 0 & 0 & 0.18\%$^\dagger$ & 43.95 & 79.38 \\
62	S2            & \textbf{0} & 0 & 0 & 0.34\%$^\dagger$ & 36.45 & 84.96 \\
63	Beam4 S1      & \textbf{0} & 0 & 0 & \textbf{0} & \textbf{48.14} & \textbf{85.57} \\
64	\bottomrule
65	\end{tabular}
66	\caption{70B-class (Llama-3.1-70B-Instruct (AWQ INT4)) LoRA ablation on DocRED (998 docs).
67	CF: violation count except $^\dagger$reported as percentage (raw count unavailable).
68	F1 $\times$100.
69	PF: greedy S1 12.5\% (25/200 docs), S2 0\% (0/200), beam4 S1 0.5\% (1/200).}
70	\label{tab:70b-docred-ablation}
71	\end{table}
72	
73	The DocRED LoRA ablation mirrors the SciERC pattern: grammar eliminates RV (0.57\%\,$\to$\,0\%) but DR increases slightly ($+$0.16\,pp); semantic-only independently eliminates DR (0.22\%\,$\to$\,0\%) but retains RV (0.51\%).
74	The complementary layer interaction is stable across datasets under LoRA fine-tuning.
75	S2 eliminates DR and parse failures (PF${=}$0\%) but causes severe R-F1 degradation ($-$7.50\,pp vs.\ S1), mirroring the SciERC pattern ($-$8.45\,pp; Table~\ref{tab:70b-ft-ablation}): at 70B, the repair layer over-constrains relation predictions where baseline DR is already near-zero (0.22\%).
76	CF increases from 0.18\% (S1) to 0.34\% (S2), confirming that over-constraining induces cascading inconsistencies across datasets.
77	The $+$4.19\,pp R-F1 gain from beam search (43.95\,$\to$\,48.14) is largely attributable to parse failure recovery: greedy S1 fails to parse 12.5\% of documents (25/200), while beam reduces this to 0.5\% (1/200), recovering $\sim$24 documents that contribute no triples under greedy decoding.
78	The controlled comparison on SciERC---where both greedy and beam achieve 0\% parse failure---isolates the pure beam quality gain at $+$0.28\,pp, consistent with the 8B pattern (Appendix~\ref{app:beam-search}).
79	
80	% exp_ids: r16_70b_docred_zs_unconstrained, r16_70b_docred_zs_grammar_only,
81	%          r16_70b_docred_zs_semantic_only
82	\paragraph{70B-class DocRED zero-shot ablation.}
83	\label{app:70b-docred-zs}
84	
85	Table~\ref{tab:70b-docred-zs-ablation} presents the layer ablation on DocRED under zero-shot decoding at 70B.
86	
87	\begin{table}[h]
88	\centering
89	\small
90	\setlength{\tabcolsep}{3.6pt}
91	\begin{tabular}{@{}l rrrr rr@{}}
92	\toprule
93	\textbf{Mode}
94	  & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF}
95	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$} \\
96	\midrule
97	Unconstrained & 13.45 & 7.88 & 0 & 0    & 13.25 & 70.14 \\
98	Grammar       & 17.03 & 0    & 0 & 0    & 13.23 & 70.12 \\
99	Semantic      & 1.66  & 8.24 & 0.12 & 132  & 13.05 & 70.10 \\
100	S1            & \textbf{0} & 0 & 0 & 173  & 13.25 & 70.05 \\
101	\bottomrule
102	\end{tabular}
103	\caption{70B-class zero-shot layer ablation on DocRED.
104	CF: violation count. F1 $\times$100.}
105	\label{tab:70b-docred-zs-ablation}
106	\end{table}
107	
108	Grammar-only eliminates RV (7.88\%\,$\to$\,0\%) but DR increases by $+$3.58\,pp (13.45\%\,$\to$\,17.03\%): forced vocabulary mapping in DocRED's high-$\bar{\kappa}$ schema ($\bar{\kappa}{=}0.842$, ${\sim}$16\% type pairs valid) converts RV into DR violations.
109	Semantic-only independently achieves 87.7\% DR reduction (13.45\%\,$\to$\,1.66\%) with no R-F1 cost, confirming the pattern from SciERC (84\%; Table~\ref{tab:70b-ft-ablation}).
110	Full S1 eliminates all DR (13.45\%\,$\to$\,0\%) with zero R-F1 cost (13.25\,$=$\,13.25), confirming that the two layers compose correctly despite their opposing individual DR effects.
111	CF increases from 0 (unconstrained) to 173 (S1), consistent with the pattern that stricter constraint enforcement in ZS introduces more cross-field inconsistencies.
112	The two layers serve complementary roles: grammar provides the RV elimination foundation that semantic-layer DR enforcement requires, while the semantic layer addresses the DR that grammar alone cannot---and in high-$\bar{\kappa}$ schemas, exacerbates.
113	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "165e22fe-fc3a-4a55-9c24-689925abd18e",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "bbc26115-6ab0-4494-9f65-c63147b0d4a8",
  "sourceToolAssistantUUID": "165e22fe-fc3a-4a55-9c24-689925abd18e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-23T18:11:20.953Z_

<details open><summary>🔧 Tool call — Read · `toolu_01954PWkHn3jqaXeX6uRw4cn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbc26115-6ab0-4494-9f65-c63147b0d4a8",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx8foHLNHXrJtppNHRe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3bd8354-d12a-4cf6-af15-843e5d8694e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Qc9zGzA3nukZcsLpkR7KyF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26333,
      "cache_read_input_tokens": 37302,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26333,
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

_source line 23 · 2026-05-23T18:11:20.961Z_

<details><summary>↩ Tool result · `toolu_01954PWkHn3jqaXeX6uRw4cn`</summary>

```text
1	% Appendix: Post-hoc Type Consistency Resolution (TCR)
2	% exp_ids: d065_tcr_pilot (all 10 configs)
3	
4	\section{Post-hoc Type Consistency Resolution}
5	\label{app:tcr}
6	
7	S1 enforces domain/range constraints per-triple but does not enforce global entity type consensus, leaving residual CF violations where the same entity receives different types across triples.
8	We evaluate a post-hoc resolution step (TCR): for each entity with conflicting type assignments, TCR selects the type that maximizes satisfaction count across all relations referencing that entity, subject to domain/range constraints.
9	Unlike naive majority voting (which ignores relational constraints and increases DR), TCR is constraint-aware: candidate types are scored by how many of the entity's relational contexts they satisfy.
10	TCR runs after S1 decoding completes and has access to the full document context.
11	
12	% ──────────────────────────────────────────
13	%  Table: TCR results on SciERC
14	% ──────────────────────────────────────────
15	\begin{table}[h]
16	\centering
17	\small
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}ll rr rr r r@{}}
20	\toprule
21	& & \multicolumn{2}{c}{\textbf{CF (\%)}} & \multicolumn{2}{c}{\textbf{DR (\%)}} & \textbf{$\Delta$E-F1} & \textbf{Fund.} \\
22	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-7} \cmidrule(l){8-8}
23	\textbf{Config} & \textbf{Model} & Pre & Post & Pre & Post & (pp) & (\%) \\
24	\midrule
25	\multirow{3}{*}{Zero-shot}
26	  & Qwen    & 9.75 & \textbf{0} & 0.93  & 1.21  & $-$1.29 & 2.04 \\
27	  & Llama   & 6.40 & \textbf{0} & 0.08  & 0.30  & $-$1.78 & 1.85 \\
28	  & Mistral & 0.67 & \textbf{0} & 13.36 & 12.87 & $+$0.05 & 0 \\
29	\midrule
30	\multirow{2}{*}{LoRA}
31	  & Qwen    & 1.19 & \textbf{0} & 0     & 0     & $-$0.75 & 0 \\
32	  & Llama   & 0.46 & \textbf{0} & 0.09  & 0.09  & $-$0.18 & 0 \\
33	\bottomrule
34	\end{tabular}}
35	\caption{TCR on SciERC ($\bar{\kappa}{=}0.333$, 551 docs).
36	Pre/Post: before/after TCR.
37	$\Delta$E-F1: entity F1 change (F1$\times$100).
38	Fund.: percentage of conflicting entities where no single type satisfies all relational constraints (fundamental conflicts).
39	TCR eliminates all CF with DR increases $\leq$0.28\,pp; fundamental conflicts are 0--2\%.}
40	\label{tab:tcr-scierc}
41	\end{table}
42	
43	% ──────────────────────────────────────────
44	%  Table: TCR results on DocRED
45	% ──────────────────────────────────────────
46	\begin{table}[h]
47	\centering
48	\small
49	\resizebox{\columnwidth}{!}{%
50	\begin{tabular}{@{}ll rr rr r r@{}}
51	\toprule
52	& & \multicolumn{2}{c}{\textbf{CF (\%)}} & \multicolumn{2}{c}{\textbf{DR (\%)}} & \textbf{$\Delta$E-F1} & \textbf{Fund.} \\
53	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-7} \cmidrule(l){8-8}
54	\textbf{Config} & \textbf{Model} & Pre & Post & Pre & Post & (pp) & (\%) \\
55	\midrule
56	\multirow{3}{*}{Zero-shot}
57	  & Qwen    & 13.11 & \textbf{0} & 10.21 & 11.74 & $-$3.44 & 13.52 \\
58	  & Llama   & 23.71 & \textbf{0} &  2.55 & 11.93 & $-$5.21 & 22.78 \\
59	  & 70B     & 11.61 & \textbf{0} &  0    &  4.20 & $-$5.98 & 18.26 \\
60	\midrule
61	\multirow{2}{*}{LoRA}
62	  & Qwen    &  0.42 & \textbf{0} &  0.01 &  0.14 & $-$0.16 & 12.16 \\
63	  & Llama   &  0.36 & \textbf{0} &  0.21 &  0.20 & $-$0.17 & 11.59 \\
64	\bottomrule
65	\end{tabular}}
66	\caption{TCR on DocRED ($\bar{\kappa}{=}0.842$, 998 docs).
67	Under zero-shot, TCR introduces substantial DR regressions (up to $+$9.38\,pp for Llama) and E-F1 drops (up to $-$5.98\,pp for 70B).
68	Fundamental conflict rates are 12--23\%, an order of magnitude higher than SciERC.
69	Under LoRA, low baseline CF (0.36--0.42\%) limits both TCR impact and DR cost.}
70	\label{tab:tcr-docred}
71	\end{table}
72	
73	\paragraph{Analysis.}
74	TCR effectiveness varies inversely with schema constraint tightness $\bar{\kappa}$ (descriptive pattern across two schemas).
75	On SciERC ($\bar{\kappa}{=}0.333$), fundamental conflicts constitute 0--2\% of type disagreements: most conflicts are resolvable because the loose schema admits many valid type pairs, and TCR can find a type satisfying all relational contexts.
76	DR increases are bounded ($\leq$0.28\,pp), and E-F1 cost is modest ($\leq$1.78\,pp in zero-shot, $\leq$0.75\,pp under LoRA).
77	On DocRED ($\bar{\kappa}{=}0.842$), 13--23\% of conflicts are fundamental: the tight schema renders most type pairs invalid, so unifying an entity's type across all its relational contexts inevitably violates some domain/range constraints.
78	This produces severe DR regressions under zero-shot (Llama: 2.55\%$\to$11.93\%; 70B: 0\%$\to$4.20\%), where baseline CF is high enough that many entities require resolution.
79	Under LoRA, baseline CF is already low (0.36--0.42\%), limiting both the scope for TCR improvement and the DR cost.
80	
81	This $\bar{\kappa}$-dependent boundary is consistent with the constraint tightness analysis in \S\ref{sec:composition}: $\bar{\kappa}$ characterizes not only the decoding-time DR residual regime but also the feasibility of post-hoc type resolution.
82	Beam search (\S\ref{sec:beam-results}) resolves CF and DR simultaneously across all $\bar{\kappa}$ values (SciERC and DocRED (998 docs): DR$\to$0\% for calibrated models), making it the preferred approach for high-tightness schemas.
83	TCR is a zero-cost complement for low-tightness schemas where beam search latency (1.39$\times$) is undesirable.
84	Integrating TCR into the decoding loop would require global optimization over all generated triples, conflicting with the autoregressive generation paradigm.
85	TCR is complementary to OntoCoDec---it addresses CF (which OntoCoDec's per-triple enforcement cannot prevent) while OntoCoDec addresses DR (which post-hoc correction cannot guarantee).
86	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3bd8354-d12a-4cf6-af15-843e5d8694e1",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "bdf7b440-ac12-4719-a278-6e0b8b9cfba5",
  "sourceToolAssistantUUID": "a3bd8354-d12a-4cf6-af15-843e5d8694e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-23T18:11:21.426Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C8b8EuzcBqHgRrBRTfhz8M`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdf7b440-ac12-4719-a278-6e0b8b9cfba5",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx8foHLNHXrJtppNHRe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4338c61-d4f5-42f0-b5b6-db76864fa878",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Qc9zGzA3nukZcsLpkR7KyF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26333,
      "cache_read_input_tokens": 37302,
      "output_tokens": 342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 26333
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 342,
          "cache_read_input_tokens": 37302,
          "cache_creation_input_tokens": 26333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 26333,
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

_source line 25 · 2026-05-23T18:11:21.433Z_

<details><summary>↩ Tool result · `toolu_01C8b8EuzcBqHgRrBRTfhz8M`</summary>

```text
1	\section{Prompt Sensitivity Analysis}
2	\label{app:prompt-sensitivity}
3	
4	To verify that OntoCoDec's constraint enforcement is robust to prompt variation, we evaluate three prompt variants on SciERC using Qwen3-8B (551 test documents): \textbf{Default} (the prompt used in all main experiments), \textbf{Minimal} (a shortened version listing only entity/relation types), and \textbf{Detailed} (an extended version with type definitions and extraction guidelines). All three variants share the same output JSON schema; only the instruction text differs. Each variant is decoded in both unconstrained and constrained (full Stage~1) modes.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Prompt sensitivity results on SciERC (551 documents). Top: Qwen3-8B; bottom: Llama-3.1-70B (AWQ INT4). ET, RV, DR denote entity-type, relation-vocabulary, and domain-range violation rates (\%), respectively. $\Delta$DR shows the relative reduction from unconstrained to constrained decoding.}
10	\label{tab:prompt-sensitivity}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{llcccccc}
13	\toprule
14	\textbf{Prompt} & \textbf{Mode} & \textbf{ET\%} & \textbf{RV\%} & \textbf{DR\%} & \textbf{$\Delta$DR} & \textbf{E-F1} & \textbf{R-F1} \\
15	\midrule
16	\multirow{2}{*}{Default}
17	  & Unconstrained & 0.40 & 1.39 & 15.37 & \multirow{2}{*}{94.0\%} & 31.01 & 8.23 \\
18	  & Constrained   & 0.00 & 0.00 &  0.93 &                         & 30.98 & 8.36 \\
19	\midrule
20	\multirow{2}{*}{Minimal}
21	  & Unconstrained & 0.58 & 1.16 & 16.91 & \multirow{2}{*}{94.6\%} & 31.98 & 7.91 \\
22	  & Constrained   & 0.00 & 0.00 &  0.92 &                         & 31.99 & 7.85 \\
23	\midrule
24	\multirow{2}{*}{Detailed}
25	  & Unconstrained & 0.22 & 0.45 & 11.07 & \multirow{2}{*}{94.2\%} & 33.55 & 10.48 \\
26	  & Constrained   & 0.00 & 0.00 &  0.64 &                         & 33.56 & 10.48 \\
27	\midrule
28	\multicolumn{8}{l}{\textit{Llama-3.1-70B-Instruct (AWQ INT4)}} \\
29	\midrule
30	\multirow{2}{*}{Default}
31	  & Unconstrained & 0.00 & 0.61 & 6.41 & \multirow{2}{*}{100\%} & 35.22 & 11.23 \\
32	  & Constrained   & 0.00 & 0.00 & 0.00 &                        & 35.19 & 11.24 \\
33	\midrule
34	\multirow{2}{*}{Minimal}
35	  & Unconstrained & 0.27 & 5.88 & 0.22 & \multirow{2}{*}{100\%} & 37.51 & 13.42 \\
36	  & Constrained   & 0.00 & 0.00 & 0.00 &                        & 37.22 & 11.35 \\
37	\midrule
38	\multirow{2}{*}{Detailed}
39	  & Unconstrained & 0.00 & 0.26 & 4.57 & \multirow{2}{*}{100\%} & 40.42 & 11.12 \\
40	  & Constrained   & 0.00 & 0.00 & 0.00 &                        & 40.35 & 11.16 \\
41	\bottomrule
42	\end{tabular}}
43	\end{table}
44	
45	Table~\ref{tab:prompt-sensitivity} shows that constrained decoding eliminates entity-type and relation-vocabulary violations entirely (ET and RV drop to 0\%) for all prompt variants at both scales. At 8B, domain-range violations are reduced by 94.0\%--94.6\% with a standard deviation of only 0.3\,pp across prompts; F1 scores remain effectively unchanged (max shift 0.13\,pp R-F1).
46	
47	At 70B, constrained decoding achieves DR${=}$0\% across all three prompts ($\Delta$DR${=}$100\%), consistent with the scale-dependent semantic layer interaction observed in the main experiments (\S\ref{sec:70b-results}). Baseline DR varies widely (0.22\%--6.41\%), yet constrained decoding converges to zero in all cases; CF is introduced as expected (0.62\%--3.50\%), consistent with the per-triple enforcement trade-off.
48	
49	Prompt variation has a measurable effect on baseline (unconstrained) violation rates at both scales: 8B DR ranges from 11.1\% (Detailed) to 16.9\% (Minimal); 70B from 0.22\% to 6.41\%. Under constrained decoding, this variance collapses, confirming that the mechanism is orthogonal to prompting and generalizes without prompt-specific tuning.
50	
51	% exp_id: sf2_70b_prompt_sensitivity
52	\paragraph{LoRA fine-tuned prompt invariance.}
53	Under LoRA fine-tuning at 70B, prompt invariance is preserved: Minimal and Detailed prompts both achieve DR${=}$0\% under S1, with CF at 0.62\% and 0.75\% respectively---consistent with the zero-shot 70B pattern above.
54	This confirms that OntoCoDec's constraint enforcement is robust to prompt variation across both zero-shot and fine-tuned regimes.
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4338c61-d4f5-42f0-b5b6-db76864fa878",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "3d8bd0b5-4305-459f-99c1-992ed29edfbb",
  "sourceToolAssistantUUID": "c4338c61-d4f5-42f0-b5b6-db76864fa878",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-23T18:11:24.795Z_

Now let me search the registry for negative conclusions by reading it in chunks, and also read the remaining paper files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d8bd0b5-4305-459f-99c1-992ed29edfbb",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx96vt6RtL3Za4sePK5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33a495b6-9f66-4e81-b6f6-8e52c1d2b576",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SjThm9T8tYgtL4Um8GTsCw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7846,
      "cache_read_input_tokens": 63635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7846,
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

_source line 27 · 2026-05-23T18:11:27.035Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01KKs1D1uqNgmYuiVnzbBdsp`</summary>

```json
{
  "pattern": "conclusion.*negative|negative.*conclusion",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml",
  "output_mode": "content",
  "context": 5,
  "head_limit": 0,
  "multiline": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33a495b6-9f66-4e81-b6f6-8e52c1d2b576",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx96vt6RtL3Za4sePK5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2bf36b5-9f54-44dc-87a9-716b8f8f2493",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SjThm9T8tYgtL4Um8GTsCw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7846,
      "cache_read_input_tokens": 63635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7846,
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

_source line 28 · 2026-05-23T18:11:27.086Z_

<details><summary>↩ Tool result · `toolu_01KKs1D1uqNgmYuiVnzbBdsp`</summary>

```text
&lt;persisted-output>
Output too large (323.1KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-director-8494441a/65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36/tool-results/toolu_01KKs1D1uqNgmYuiVnzbBdsp.txt

Preview (first 2KB):
64-          rate: 0.3354
65-        Compare:
66-          total: 66
67-          dr_violations: 28
68-          rate: 0.4242
69:    conclusion: success
70:    completed_at: '2026-05-13T19:13:34.510Z'
71:  mvp_phase0_violation_rate_docred:
72:    status: DONE
73:    retry_count: 0
74:    created_at: '2026-05-13T17:38:05.075Z'
75:    updated_at: '2026-05-13T21:46:35.193Z'
76:    hypothesis: DocRED 有 96 relation types，约束空间远大于 SciERC (7 types)，预期 unconstrained
77:      LLM 的 per-triple violation rate 显著高于 SciERC，验证违规率与约束空间复杂度正相关
78:    spec:
79:      command: python3 run_extraction_docred.py --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B
80:        --data_path data/docred/dev.json --output_path outputs/raw_outputs_docred.jsonl
81:        --device cuda:0 --batch_size 4 --resume
82:      server: westd-16980
83:      gpu:
84:      - cuda:1
85:      data_path: /root/schema_semantic_constrained_ie/data/docred/dev.json
86:      data_count: 998
87:      model_name: Qwen3-8B
88:      seed: 42
89:      pid: 113148
90:      resumed_from_doc: 265
91:      batch_size: 4
92:      current_progress: 281
93:      checkpoint_path: /root/schema_semantic_constrained_ie/outputs/raw_outputs_docred.jsonl
94:      log_path: ~/runs/schema_semantic_constrained_ie/mvp_phase0_violation_rate_docred.log
95:    metrics:
96:      total_docs: 998
97:      parsed_docs: 962
98:      json_parse_rate: 0.964
99:      total_entities: 19099
100:      total_triples: 16540
101:      entity_type_violation_rate: 0.075
102:      relation_vocabulary_violation_rate: 0.289
103:      domain_range_violation_rate: 0.187
104:      cross_field_consistency_violation_rate: 0.0008
105:      go_nogo_metric: 0.187
106:      fuzzy_matches: 126
107:      top_dr_violations_by_rate:
108:        P35_head_of_state: 1
109:        P710_participant: 0.919
110:        P172_ethnic_group: 0.875
111:      top_dr_violations_by_count:
112:        P31_instance_of:
113:          violations: 322
114:          total: 533
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2bf36b5-9f54-44dc-87a9-716b8f8f2493",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "8f1904de-532a-4240-8d40-e64367c250a2",
  "sourceToolAssistantUUID": "c2bf36b5-9f54-44dc-87a9-716b8f8f2493",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T18:11:27.767Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DzbVqrC2yZhAvhGcKrkMCg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f1904de-532a-4240-8d40-e64367c250a2",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx96vt6RtL3Za4sePK5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98a0032e-2923-4b0b-bfeb-6154669a81e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SjThm9T8tYgtL4Um8GTsCw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7846,
      "cache_read_input_tokens": 63635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7846,
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

_source line 30 · 2026-05-23T18:11:27.775Z_

<details><summary>↩ Tool result · `toolu_01DzbVqrC2yZhAvhGcKrkMCg`</summary>

```text
1	\section{Beam Search Compatibility}
2	\label{app:beam-search}
3	
4	OntoCoDec's constraint enforcement is designed to be decoding-strategy agnostic.
5	The main experiments (\S\ref{sec:experiments}) use greedy decoding; Appendix~\ref{app:sampling} validates nucleus sampling.
6	Here we verify compatibility with beam search, completing coverage of the three standard decoding strategies.
7	
8	\paragraph{Implementation challenges.}
9	Two stateful components require adaptation for beam search.
10	(1)~The grammar layer (XGrammar) maintains an internal \texttt{GrammarMatcher} state that tracks the generated token sequence; beam reordering invalidates this state because beams are permuted across steps.
11	Our solution instantiates a fresh \texttt{GrammarMatcher} per beam per step and replays the beam's current token sequence through XGrammar's stateless accept API (64 lines of code).
12	(2)~The semantic layer's \texttt{TypeConstraintProcessor} accumulates entity and relation registries that assume a single generation path.
13	Our solution isolates state per beam by calling \texttt{detect()} on the full partial output at each step, reconstructing all entity/relation state from scratch for each beam independently (61 lines of code).
14	Both adaptations add ${\sim}125$ lines total without modifying the existing greedy/sampling logic.
15	
16	\paragraph{Results.}
17	Table~\ref{tab:beam-search} compares beam search ($k{=}4$, \texttt{early\_stopping=True}) against greedy decoding under S1 constraints across six model-dataset combinations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Beam search ($k{=}4$) vs.\ greedy decoding under S1 constraints (zero-shot).
23	SciERC: 551 documents; DocRED: matched 50-document subsets (same documents for greedy and beam); full 998-doc DocRED results in Table~\ref{tab:beam-docred-998-zs}.
24	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\%); F1 $\times$ 100.}
25	\label{tab:beam-search}
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{@{}llcccccc@{}}
28	\toprule
29	\textbf{Model / Dataset} & \textbf{Decoding} & ET & RV & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ \\
30	\midrule
31	\multirow{2}{*}{Qwen3-8B / SciERC (551)}
32	  & Greedy      & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\
33	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.53} & 32.00 & 8.56 \\
34	\midrule
35	\multirow{2}{*}{Qwen3-8B / DocRED (50)}
36	  & Greedy      & 0 & 0 & 8.69 & 2.08 & 59.08 & 8.33 \\
37	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.55} & 58.64 & 9.37 \\
38	\midrule
39	\multirow{2}{*}{Llama-3.1-8B / SciERC (551)}
40	  & Greedy      & 0 & 0 & 0.08 & 6.56 & 23.49 & 2.54 \\
41	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.93} & 25.04 & 3.33 \\
42	\midrule
43	\multirow{2}{*}{Llama-3.1-8B / DocRED (50)}
44	  & Greedy      & 0 & 0 & 1.58 & 6.85 & 55.35 & 6.12 \\
45	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.94} & 55.62 & 9.47 \\
46	\midrule
47	\multirow{2}{*}{Mistral-7B / SciERC (551)}
48	  & Greedy      & 0 & 0 & 13.40 & 1.27 & 27.46 & 3.67 \\
49	  & Beam ($k{=}4$) & 0 & 0 & 13.79 & \textbf{0.57} & 26.66 & 4.37 \\
50	\midrule
51	\multirow{2}{*}{Mistral-7B / DocRED (50)}
52	  & Greedy      & 0 & 0 & 28.37 & 0.34 & 51.60 & 4.19 \\
53	  & Beam ($k{=}4$) & 0 & 0 & \textbf{21.37} & \textbf{0.19} & 51.78 & 5.70 \\
54	\bottomrule
55	\end{tabular}}
56	\end{table}
57	
58	\paragraph{Discussion.}
59	For calibrated models (Qwen3-8B, Llama-3.1-8B), beam search achieves DR=0\% across all four model-dataset combinations (both SciERC with 6 entity types, 551 documents, and DocRED with 96 relation types, 50 documents), regardless of schema complexity.
60	On SciERC, beam search eliminates DR for both Qwen (0.93\%\,$\to$\,0\%) and Llama (0.08\%\,$\to$\,0\%), and substantially reduces CF (Qwen: 9.90\%\,$\to$\,0.53\%; Llama: 6.56\%\,$\to$\,0.93\%).
61	On DocRED (matched 50-document subsets), beam search eliminates DR for both Qwen (8.69\%\,$\to$\,0\%) and Llama (1.58\%\,$\to$\,0\%), with CF reductions of 74\% and 86\% respectively.
62	Llama DocRED shows the largest R-F1 gain ($+$3.4\,pp), consistent with beam search recovering valid type assignments that greedy decoding missed due to constraint fallback.
63	The CF reduction is an indirect effect: beam search reduces constraint-fallback frequency by exploring alternative token sequences that satisfy both grammar and semantic masks simultaneously, avoiding the fallback-to-grammar path that produces cross-field inconsistencies under greedy decoding.
64	
65	Mistral-7B-v0.3 constitutes a boundary condition on both datasets.
66	On SciERC (6 entity types), beam search does not reduce DR (13.4\%\,$\to$\,13.8\%), though CF drops by 55\% relative (1.27\%\,$\to$\,0.57\%) and R-F1 improves by $+$0.7\,pp; the unchanged DR confirms that all residual violations stem from entity type misclassification, not constraint-search failure.
67	On DocRED (96 relation types), beam search reduces DR by 25\% relative (28.4\%\,$\to$\,21.4\%): the more complex schema introduces constraint-search failures that beam exploration resolves, but the entity misclassification component remains.
68	This contrast reveals that beam search resolves constraint-search failure (where greedy decoding encounters $G(t) \cap S(t) = \emptyset$ conflicts) but cannot overcome fundamental model calibration limitations in entity typing.
69	
70	\paragraph{Beam width ablation.}
71	Table~\ref{tab:beam-ablation} varies beam width $k \in \{1,2,4,8\}$ on Qwen3-8B / SciERC (551 documents) under S1 constraints.
72	
73	\begin{table}[h]
74	\centering
75	\small
76	\caption{Effect of beam width on constraint satisfaction and extraction quality (Qwen3-8B, SciERC, 551 documents, S1 constraints). $k{=}1$ corresponds to greedy decoding.}
77	\label{tab:beam-ablation}
78	\begin{tabular}{@{}rcccc@{}}
79	\toprule
80	$k$ & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ \\
81	\midrule
82	1 (greedy) & 0.93 & 9.90 & 30.98 & 8.36 \\
83	2          & 0.35 & 4.12 & 31.54 & \textbf{8.75} \\
84	4          & \textbf{0}    & 0.53 & 32.00 & 8.56 \\
85	8          & \textbf{0}    & \textbf{0.08} & \textbf{32.18} & 8.39 \\
86	\bottomrule
87	\end{tabular}
88	\end{table}
89	
90	DR elimination at $k{\geq}4$ confirms that constraint-search failure is resolved with moderate exploration width.
91	CF continues to decrease with larger beam (0.08\% at $k{=}8$, only 2 residual violations), while entity extraction quality improves monotonically.
92	$k{=}4$ represents the optimal cost-effectiveness trade-off: it eliminates all DR violations at roughly half the compute cost of $k{=}8$.
93	
94	\paragraph{Beam width--latency Pareto analysis (LoRA).}
95	% exp_id: d066_beam_sweep
96	Figure~\ref{fig:beam-pareto} and Table~\ref{tab:beam-sweep} extend the beam width analysis to LoRA fine-tuning, where the constrained--unconstrained interaction shifts qualitatively: LoRA + S1 already achieves DR=0\% at $k{=}1$ (greedy), so beam search targets CF reduction rather than DR elimination (contrast: zero-shot requires $k{\geq}4$ for DR=0\%).
97	Among constrained configurations, $k{=}2$ is Pareto optimal (R-F1 44.60, CF 0.11\%, 1.39$\times$ vs.\ greedy unconstrained; 1.18$\times$ vs.\ greedy S1); $k{\geq}4$ yields diminishing F1 returns with increasing latency (1.63--2.03$\times$).
98	
99	\begin{figure*}[ht]
100	\centering
101	\includegraphics[width=\textwidth]{figures/beam_pareto.pdf}
102	\caption{Beam width vs.\ R-F1 under LoRA fine-tuning. Left: SciERC (Qwen3-8B solid, Llama-3.1-8B dashed; 551 docs). Right: DocRED (Llama-3.1-8B, 200 docs). Bubble area $\propto$ total violation rate (DR+CF+RV); green rings mark zero-violation configurations. Star: Pareto-optimal ($k{=}2$).}
103	\label{fig:beam-pareto}
104	\end{figure*}
105	
106	\begin{table}[h]
107	\centering
108	\small
109	\caption{Beam width sweep on SciERC (Qwen3-8B LoRA, 551 documents). \textsc{unc}: unconstrained; \textsc{con}: schema-constrained. Latency relative to $k{=}1$ unconstrained. Highlighted row: Pareto-optimal configuration.}
110	\label{tab:beam-sweep}
111	\resizebox{\columnwidth}{!}{%
112	\begin{tabular}{@{}cl cccc cc@{}}
113	\toprule
114	$k$ & Mode & E-F1 & R-F1 & DR (\%) & CF (\%) & Latency (s) & Rel.\ Lat. \\
115	\midrule
116	\multirow{2}{*}{1}
117	 & \textsc{unc} & 66.88 & 42.95 & 2.11 & 0    & 2.494 & 1.00$\times$ \\
118	 & \textsc{con} & 66.88 & 42.95 & \textbf{0} & 0.50 & 2.932 & 1.18$\times$ \\
119	\midrule
120	\multirow{2}{*}{2}
121	 & \textsc{unc} & 67.79 & 44.75 & 1.54 & 0    & 2.954 & 1.18$\times$ \\
122	 & \cellcolor{blue!8}\textsc{con} & \cellcolor{blue!8}67.71 & \cellcolor{blue!8}\textbf{44.60} & \cellcolor{blue!8}\textbf{0} & \cellcolor{blue!8}0.11 & \cellcolor{blue!8}3.463 & \cellcolor{blue!8}1.39$\times$ \\
123	\midrule
124	\multirow{2}{*}{4}
125	 & \textsc{unc} & 67.49 & 43.72 & 1.89 & 0    & 3.485 & 1.40$\times$ \\
126	 & \textsc{con} & 67.22 & 43.60 & \textbf{0} & 0    & 4.069 & 1.63$\times$ \\
127	\midrule
128	\multirow{2}{*}{8}
129	 & \textsc{unc} & 66.40 & 43.17 & 1.77 & 0    & 4.194 & 1.68$\times$ \\
130	 & \textsc{con} & 66.36 & 43.65 & \textbf{0} & 0    & 5.058 & 2.03$\times$ \\
131	\bottomrule
132	\end{tabular}}
133	\end{table}
134	
135	\paragraph{Composability with fine-tuning.}
136	Under greedy decoding, the fine-tuned Qwen3-8B (LoRA, SciERC) with S1 constraints already achieves DR=0\% but retains CF=1.18\% (22 cross-field violations across 551 documents), with E-F1=67.05 and R-F1=43.77.
137	Adding beam search ($k{=}4$) eliminates all residual CF violations (1.18\%\,$\to$\,0\%), yielding zero violations across all four metrics (ET=0\%, RV=0\%, DR=0\%, CF=0\%) while preserving extraction quality (E-F1=66.88, R-F1=43.60; changes within $\pm$0.5\,pp).
138	Llama-3.1-8B (LoRA, SciERC) with S1 constraints and beam search ($k{=}4$) likewise achieves zero violations across all four metrics (ET=0\%, RV=0\%, DR=0\%, CF=0\%) with R-F1=46.18; the zero-violation result thus generalizes across calibrated model families.
139	% exp_id: q1_llama_ft_beam_scierc
140	The three constraint mechanisms (grammar masking, semantic domain-range filtering, and beam exploration) are thus fully composable: each addresses a distinct violation source without interfering with the others or degrading task performance.
141	
142	The initial 50-document DocRED subset (Table~\ref{tab:beam-search}) was subsequently validated on the full 998-document set (Table~\ref{tab:beam-docred-998-zs}): both models achieve DR${=}$0\%, confirming subset representativeness.
143	Llama shows the larger improvement (CF 8.54\%\,$\to$\,1.00\%, 88\% reduction; R-F1 $+$2.6\,pp), consistent with beam search resolving constraint-search failures that greedy decoding cannot.
144	
145	\begin{table}[h]
146	\centering
147	\small
148	\caption{Zero-shot beam search ($k{=}4$) under S1 constraints on the full DocRED dev set (998 documents).
149	ET/RV/DR/CF: violation rates (\%); PF: parse failure rate (\%); F1 $\times$100.}
150	\label{tab:beam-docred-998-zs}
151	\begin{tabular}{@{}lcccccc@{}}
152	\toprule
153	\textbf{Model} & ET & RV & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ \\
154	\midrule
155	Qwen3-8B  & 0 & 0 & \textbf{0} & 4.94 & 58.19 & 8.72 \\
156	Llama-3.1-8B & 0 & 0 & \textbf{0} & 1.00 & 57.81 & 8.83 \\
157	\bottomrule
158	\end{tabular}
159	\end{table}
160	
161	Table~\ref{tab:beam-docred-lora} reports LoRA + beam-4 results on the full DocRED dev set (998 documents), extending the fine-tuning composability evaluation from SciERC to the higher-$\bar{\kappa}$ regime.
162	Parse failure rates under LoRA beam-4 range from 1.3\% to 2.9\%, lower than the zero-shot rate.
163	
164	\begin{table}[h]
165	\centering
166	\small
167	\caption{LoRA greedy vs.\ beam search ($k{=}4$) on DocRED (998 dev documents) under S1 constraints.
168	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field violation rates (\%); PF = parse failure rate (\%); F1 $\times$ 100.}
169	\label{tab:beam-docred-lora}
170	\resizebox{\columnwidth}{!}{%
171	\begin{tabular}{@{}llccccccc@{}}
172	\toprule
173	\textbf{Model} & \textbf{Decoding} & ET & RV & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ & PF \\
174	\midrule
175	\multirow{2}{*}{Qwen3-8B}
176	  & Greedy con & 0 & 0 & 0.01 & 0.41 & 81.43 & 40.56 & 8.52 \\ % d065_qwen_greedy_4096_r2
177	  & Beam-4 con & 0 & \textbf{0} & \textbf{0} & 0.01 & 84.00 & 44.46 & 2.9 \\
178	\midrule
179	\multirow{2}{*}{Llama-3.1-8B}
180	  & Greedy con & 0 & 0 & 0.21 & 0.21 & 83.94 & 43.78 & 2.51 \\ % d065: 4096 context
181	  & Beam-4 con & 0 & 0 & 0 & \textbf{0} & \textbf{85.23} & \textbf{47.17} & \textbf{1.3} \\
182	\bottomrule
183	\end{tabular}}
184	\end{table}
185	
186	Llama-3.1-8B achieves zero violations across all four metrics (ET, RV, DR, CF = 0\%) on DocRED with LoRA + beam-4, extending the zero-violation result from SciERC to the high-$\bar{\kappa}$ regime.
187	Qwen3-8B achieves DR=0\% with near-zero CF (0.01\%); R-F1 is preserved ($\pm$0.06\,pp).
188	Combined with the sampling robustness results (Appendix~\ref{app:sampling}), these findings confirm that OntoCoDec's constraint enforcement is compatible with greedy, sampling, and beam search decoding without modification to the core constraint logic.
189	
190	\paragraph{Latency overhead.}
191	Table~\ref{tab:beam-latency} reports wall-clock latency for greedy and beam search ($k{=}4$) under LoRA fine-tuning.
192	
193	\begin{table}[h]
194	\centering
195	\small
196	\begin{tabular}{@{}lrr@{}}
197	\toprule
198	\textbf{Condition} & \textbf{s/doc} & \textbf{Overhead} \\
199	\midrule
200	Greedy unconstrained   & 2.612 & 1.00$\times$ \\
201	Greedy constrained (S1)& 2.873 & 1.10$\times$ \\
202	Beam-4 unconstrained   & 3.446 & 1.32$\times$ \\
203	Beam-4 constrained (S1)& 4.013 & 1.54$\times$ \\
204	\bottomrule
205	\end{tabular}
206	\caption{Latency per document (SciERC, 551 docs, Qwen3-8B LoRA FT, RTX PRO 6000 Blackwell). Overhead relative to greedy unconstrained.}
207	\label{tab:beam-latency}
208	\end{table}
209	
210	Beam search itself adds 32\% latency (4 beams); constraint overhead increases from 10\% (greedy) to 17\% (beam) because each beam independently maintains grammar and semantic state.
211	Per-beam entity registry memory is $O(|\text{entities}|)$ per beam; at $k{=}8$ with typical document sizes, overhead is ${<}$1\,MB per beam, negligible relative to model memory.
212	The total 1.54$\times$ overhead is acceptable for offline batch IE; \texttt{early\_stopping} limits additional compute to partial-sequence exploration.
213	
214	We also explored a type-consensus constraint that forces identical entity types across all relations within a document.
215	However, CF violations occur precisely where the consensus type conflicts with domain-range constraints, creating a fundamental CF$\leftrightarrow$DR trade-off.
216	With DR-aware enforcement (skipping consensus when it would violate domain-range), the layer becomes a no-op (100\% skip rate on 551 SciERC documents and 50 DocRED documents).
217	This confirms that beam search resolves the CF$\leftrightarrow$DR tension through a fundamentally different mechanism: token-level exploration of paths satisfying both constraints simultaneously.
218	
219	\paragraph{TCR reranking under beam search.}
220	TCR reranking with beam search ($k{=}4$) showed no effect on either Qwen3-8B or Llama-3.1-8B under LoRA (0/551 SciERC candidates changed): fine-tuned beam candidates are already type-consistent (TCR score${=}$1.0 for all candidates), confirming that beam search implicitly subsumes post-hoc type consensus under fine-tuning.
221	This further strengthens the beam search deployment recommendation: beam not only eliminates all four violation types but also renders post-hoc CF resolution unnecessary.
222	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98a0032e-2923-4b0b-bfeb-6154669a81e4",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "2e15c16e-d6f7-4620-b5d5-ebc2a84b5086",
  "sourceToolAssistantUUID": "98a0032e-2923-4b0b-bfeb-6154669a81e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T18:11:28.683Z_

<details open><summary>🔧 Tool call — Read · `toolu_015nxSgumMumCBNWmgwUJ81P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e15c16e-d6f7-4620-b5d5-ebc2a84b5086",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx96vt6RtL3Za4sePK5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1256118f-728f-4a6c-a21f-d0b0454154b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SjThm9T8tYgtL4Um8GTsCw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7846,
      "cache_read_input_tokens": 63635,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7846
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 365,
          "cache_read_input_tokens": 63635,
          "cache_creation_input_tokens": 7846,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7846,
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

_source line 32 · 2026-05-23T18:11:28.689Z_

<details><summary>↩ Tool result · `toolu_015nxSgumMumCBNWmgwUJ81P`</summary>

```text
1	% Section 7 — Discussion and Conclusion
2	
3	OntoCoDec compiles IE ontologies into composable token-level constraints, validated across 2 RE datasets (SciERC, DocRED) and 3 model families, with a preliminary event extraction pilot (\S\ref{sec:wikievents}).
4	The central empirical finding is non-additive layer interaction: grammar alone achieves 3\% DR reduction on SciERC, semantic alone 24\%, but their composition yields 94\% at 8B (\S\ref{sec:scierc-results})---an enabling dependency where grammar-enforced vocabulary membership creates the clean input the semantic layer requires.
5	
6	\paragraph{Scale-dependent layer interaction.}
7	This dependency weakens at scale: at 70B, the semantic layer independently achieves 84\% DR reduction (\S\ref{sec:70b-results}).
8	We offer a speculative hypothesis: larger models exhibit improved vocabulary calibration, assigning higher probability to ontology-valid tokens and reducing the semantic layer's dependence on grammar-enforced vocabulary membership (Appendix~\ref{app:causal-tracing}); confirming this causal mechanism requires cross-family verification beyond our current scope.
9	Supporting evidence includes the fallback frequency gap: under LoRA + S1, Qwen-8B triggers 0 grammar-first fallbacks on SciERC while Llama-8B triggers 5{,}882 (Table~\ref{tab:ft-ablation}), yet both achieve DR\,$\leq$\,0.21\%, confirming that fallback frequency does not determine enforcement effectiveness.
10	Grammar-constrained decoding is thus necessary but increasingly insufficient as models improve; constraint enforcement is preserved under INT4 quantization (4$\times$ compression; Appendix~\ref{app:quantization}).
11	
12	\paragraph{DR$\leftrightarrow$CF trade-off.}
13	Greedy S1 reduces DR to $\leq$\,0.21\% but introduces CF (zero-shot $+$9.82\,pp, fine-tuned $+$1.18\,pp)---an architectural consequence of per-triple independent enforcement.
14	Among 248 zero-shot CF violations, 58.1\% involve hallucinated entities (absent from gold) and only 7.3\% are true cascade errors (\S\ref{sec:scierc-results}); fine-tuned CF drops to $\leq$1.4\%.
15	Beam $k{=}2$ reduces CF to 0.11\% at 1.18$\times$ latency (Pareto-optimal; recommended for zero-shot deployment); $k{=}4$ eliminates all violations at 8B (1 residual CF at 70B) at 1.39$\times$ (\S\ref{sec:beam-results}).
16	Net effect: total violations (DR+CF) decrease ${\sim}$31\% in zero-shot and 26--52\% under fine-tuned greedy S1; beam $k{=}4$ eliminates all. DR is irrecoverable while CF is amenable to post-hoc resolution (TCR; Appendix~\ref{app:tcr}).
17	
18	\paragraph{Complementarity and deployment.}
19	GoLLIE and KnowCoder internalize schema knowledge via training but lack runtime guarantees; LoRA + S1 shows the two are complementary (DR 1--2\%\,$\to$\,$\leq$0.21\%; neither alone achieves both high R-F1 and near-zero DR).
20	S2 (two-pass) exhibits scale-sensitive behavior: comparable to S1 at 8B but $-$8\,pp R-F1 at 70B, consistent with CRANE's~\cite{banerjee2025crane} finding that aggressive constraint enforcement can interfere with well-calibrated reasoning; we recommend S1 as the default configuration.
21	
22	\paragraph{Per-triple vs.\ global enforcement.}
23	Per-triple enforcement cannot coordinate cross-triple type assignments---the source of CF (Level~3; \S\ref{sec:decidability}); global entity-level type consensus exceeds online per-token masking.
24	Beam search and TCR approximate this; integrating consensus into decoding remains future work.
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1256118f-728f-4a6c-a21f-d0b0454154b0",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "882e62f3-74b8-4142-b0fe-f369cca3e2d1",
  "sourceToolAssistantUUID": "1256118f-728f-4a6c-a21f-d0b0454154b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-23T18:11:31.096Z_

Now let me search the registry for all negative conclusions more specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "882e62f3-74b8-4142-b0fe-f369cca3e2d1",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx9duTY9mF1C976H6J3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74360d30-7228-47c4-aebc-6bad0f5c5c44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RAMMoXM8j4PUkCXcrHr3ux",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8891,
      "cache_read_input_tokens": 71481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8891,
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

_source line 34 · 2026-05-23T18:11:33.174Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01NZZ6PxFLkWjV9rYf8RthDU`</summary>

```json
{
  "pattern": "conclusion: negative",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml",
  "output_mode": "content",
  "context": 10,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74360d30-7228-47c4-aebc-6bad0f5c5c44",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx9duTY9mF1C976H6J3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc0bb7b9-b4d8-44ad-a63d-8f0b85584a2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RAMMoXM8j4PUkCXcrHr3ux",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8891,
      "cache_read_input_tokens": 71481,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8891
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 71481,
          "cache_creation_input_tokens": 8891,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8891,
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

_source line 35 · 2026-05-23T18:11:33.192Z_

<details><summary>↩ Tool result · `toolu_01NZZ6PxFLkWjV9rYf8RthDU`</summary>

```text
1422-      grammar_first_fallback_rate: 0.3664
1423-      cf_registry_fallback_rate: 0.0448
1424-      total_mask_calls: 17024
1425-      violation_budget_DR_CF: 0.1482
1426-    notes: CF fallback 实验在 SciERC + Qwen3-8B 上的 pilot 结果：CF 从 9.90% 下降到 0.04% (-9.86pp)，但
1427-      DR 从 0.93% 上升到 14.78% (+13.85pp)。DR+CF budget 净增 +3.99pp。F1 几乎不变 (E-F1=30.98%
1428-      与 baseline 完全一致；R-F1=8.23%, -0.13pp)。Grammar-first fallback 触发率 36.64% (6237/17024
1429-      mask calls)，CF-registry fallback 4.48%。判定：成功降低 CF 但代价是 DR 大幅恶化，违规没有真正减少，只是从
1430-      CF 转移到 DR。建议改进方向：(1) 仅在 CF-registry 命中时回退，保留 DR enforcement；(2) rebuttal 中诚实呈现这是
1431-      violation re-routing 而非 reduction。详细报告见 artifact w1_cf_fallback_scierc_pilot_analysis。
1432:    conclusion: negative
1433-    completed_at: '2026-05-15T14:57:13.885Z'
1434-    hypothesis: Constrained fallback (CF) 策略 SciERC pilot：约束解码产生空输出时回退至 unconstrained
1435-      生成，预期降低空输出率同时维持 violation 控制。若 fallback 频率过高则 CF 策略不可行。
1436-  w1_cf_fallback_docred:
1437-    status: DONE
1438-    retry_count: 1
1439-    created_at: '2026-05-15T10:32:53.234Z'
1440-    updated_at: '2026-05-15T16:55:58.012Z'
1441-    server: westd-16980
1442-    gpu: cuda:1
--
3358-      RV_pct: 0
3359-      DR_pct: 0.93
3360-      CF_pct: 9.9
3361-      E_F1: 30.98
3362-      R_F1: 8.36
3363-      gtc_skip_total: 672
3364-      gtc_skip_unique_entities: 258
3365-      gtc_effective_corrections: 0
3366-      delta_DR: 0
3367-      delta_CF: 0
3368:    conclusion: negative
3369-    checkpoint_path: /root/schema_semantic_constrained_ie/outputs/scierc_full_s1_consensus_v2.jsonl
3370-    log_path: ~/runs/schema_semantic_constrained_ie/w10_type_consensus_prototype.log
3371-    completed_at: '2026-05-17T07:09:41.619Z'
3372-  w10_type_consensus_docred_50:
3373-    status: DONE
3374-    retry_count: 0
3375-    created_at: '2026-05-17T06:06:56.659Z'
3376-    updated_at: '2026-05-17T07:09:42.510Z'
3377-    hypothesis: GTC Layer 3 on DocRED (96 relation types, complex schema) will reduce
3378-      CF violations while maintaining DR through DR-aware skip mechanism; skip frequency
--
3402-      RV_pct: 0
3403-      DR_pct: 8.69
3404-      CF_pct: 2.4
3405-      E_F1: 59.08
3406-      R_F1: 8.33
3407-      gtc_skip_total: 601
3408-      gtc_skip_unique_entities: 213
3409-      gtc_effective_corrections: 0
3410-      delta_DR: 0
3411-      delta_CF: 0
3412:    conclusion: negative
3413-    checkpoint_path: /root/schema_semantic_constrained_ie/outputs/docred_full_s1_consensus_50.jsonl
3414-    log_path: ~/runs/schema_semantic_constrained_ie/w10_type_consensus_docred_50.log
3415-    completed_at: '2026-05-17T07:09:42.510Z'
3416-  w10_llama_docred_beam_50:
3417-    status: DONE
3418-    retry_count: 0
3419-    created_at: '2026-05-17T07:11:24.746Z'
3420-    updated_at: '2026-05-17T07:56:15.809Z'
3421-    hypothesis: Beam search (k=4) on Llama DocRED will reduce DR and CF violations,
3422-      completing the beam search matrix (3rd model-dataset combination). Llama's weaker
--
3501-        greedy_DR: 13.4
3502-        greedy_CF: 1.27
3503-        greedy_E_F1: 27.46
3504-        greedy_R_F1: 3.67
3505-        delta_DR: +0.39pp
3506-        delta_CF: -0.70pp
3507-        delta_E_F1: -0.80pp
3508-        delta_R_F1: +0.70pp
3509-    checkpoint_path: /root/schema_semantic_constrained_ie/outputs/scierc_mistral_beam_551.jsonl
3510-    log_path: /root/runs/schema_semantic_constrained_ie/w10_mistral_scierc_beam_551.log
3511:    conclusion: negative
3512-    completed_at: '2026-05-17T08:33:53.672Z'
3513-    analysis: 'Beam search (k=4) on Mistral SciERC shows mixed results vs greedy.
3514-      R_F1 improved (+0.70pp, 4.37 vs 3.67) and CF violations halved (0.57% vs 1.27%),
3515-      but DR slightly worse (13.79% vs 13.4%) and E_F1 slightly worse (26.66 vs 27.46).
3516-      Hypothesis partially falsified: beam search did not reduce DR violations. Consistent
3517-      with finding that Mistral entity type misclassification is the bottleneck, not
3518-      token-level exploration breadth.'
3519-  w10_beam_ablation_k2:
3520-    status: DONE
3521-    retry_count: 0
--
4928-        epochs: 3
4929-        batch_size: 16
4930-        gradient_checkpointing: true
4931-        bf16: true
4932-        warmup_ratio: 0.1
4933-        optimizer: AdamW
4934-        schedule: cosine
4935-    reproduce:
4936-      finished_at: '2026-05-19T04:50:16.081Z'
4937-    failure_reason: process dead 5× with no sentinel/W&B — auto-resolved as failed
4938:    conclusion: negative
4939-    completed_at: '2026-05-19T04:50:14.990Z'
4940-    extra:
4941-      hook_events:
4942-      - event: on_failed
4943-        action: agent
4944-        ts: '2026-05-19T04:50:21.524569+00:00'
4945-    metrics:
4946-      unconstrained:
4947-        entity_f1: 0.6478
4948-        relation_f1: 0.3789
--
5016-      qwen_docred_ft:
5017-        cf_before: 48
5018-        cf_after: 3
5019-        dr_rate_before: 0.0001
5020-        dr_rate_after: 0.0044
5021-      llama_docred_ft:
5022-        cf_before: 41
5023-        cf_after: 2
5024-        dr_rate_before: 0.0021
5025-        dr_rate_after: 0.005
5026:    conclusion: negative
5027-    completed_at: '2026-05-19T03:23:41.243Z'
5028-  d062_beam_latency:
5029-    status: DONE
5030-    retry_count: 0
5031-    created_at: '2026-05-19T03:15:35.458Z'
5032-    updated_at: '2026-05-19T04:30:54.166Z'
5033-    hypothesis: Beam search (k=4) with constrained decoding will have higher latency
5034-      overhead relative to greedy than unconstrained beam search, because the constraint
5035-      processor must independently track and validate grammar/semantic state for each
5036-      of the 4 beams at every decoding step.
--
5286-        mode: full_s1
5287-      claim: Claim 3 + method enhancement
5288-      code_location: run_constrained_extraction.py:746-808 run_single_pass_beam()
5289-      checkpoint_path: /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged
5290-      log_path: outputs/d068_guided_beam/ on both servers
5291-      partial_result: all violations 0% at ~20% completion - penalty has no effect
5292-        on LoRA model
5293-      negative_reason: LoRA model beam candidates already 0% violations; penalty term
5294-        always 0; F1 drops 0.3-5.3pp due to multi-sequence decoding noise. Director
5295-        decided No-Go, killed at ~20% completion.
5296:    conclusion: negative
5297-    completed_at: '2026-05-19T16:49:55.045Z'
5298-  d066_beam_sweep:
5299-    status: DONE
5300-    retry_count: 0
5301-    created_at: '2026-05-19T23:44:23.637Z'
5302-    updated_at: '2026-05-22T10:34:14.027Z'
5303-    hypothesis: Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic
5304-      DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness
5305-      trade-off for the beam search appendix Pareto analysis.
5306-    spec:
--
6575-      command: CUDA_VISIBLE_DEVICES=0 python beam_tcr_rerank.py --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged
6576-        --data_path data/processed_data/test.json --dataset scierc --beam_width 4
6577-        --alpha 0.7 --output_path outputs/beam4_tcr_qwen_scierc.jsonl --skip_on_error
6578-      server: westd-16980
6579-      data_path: data/processed_data/test.json
6580-      data_count: 551
6581-      model_name: Qwen3-8B-LoRA-SciERC-merged
6582-      seed: 42
6583-      checkpoint_path: /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged
6584-      log_path: /tmp/beam_tcr_run.log
6585:    conclusion: negative
6586-    completed_at: '2026-05-22T15:37:47.865Z'
6587-    metrics:
6588-      samples: 551
6589-      json_failures: 0
6590-      entities: 1802
6591-      relations: 1250
6592-      entity_type_violations: 0/1802 (0.0%)
6593-      relation_vocab_violations: 0/1250 (0.0%)
6594-      domain_range_violations: 23/1250 (1.8%)
6595-      cross_field_consistency_violations: 1
--
6691-        --data_path data/processed_data/test.json --dataset scierc --mode grammar_only
6692-        --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_grammar_only.jsonl
6693-        --max_new_tokens 2048
6694-      server: westd-21461
6695-      data_path: data/processed_data/test.json
6696-      data_count: 551
6697-      model_name: Llama-3.1-70B-Instruct-AWQ-INT4 (ZS)
6698-      seed: 42
6699-      checkpoint_path: N/A (eval-only)
6700-      log_path: /tmp/eval_70b_zs_scierc_grammar_only.log
6701:    conclusion: negative
6702-    metrics:
6703-      R_F1: 11.23
6704-      DR_pct: 6.33
6705-      RV_pct: 0
6706-      ET_pct: 0
6707-      CF_count: 0
6708-      samples: 551
6709-    completed_at: '2026-05-22T18:09:48.056Z'
6710-  tcr_beam4_llama_scierc:
6711-    status: DONE
--
6725-      domain_range_violations: 13/1194 (1.1%)
6726-      cross_field_consistency: 0
6727-      DR_pct: 1.09
6728-      E_F1: 68.02
6729-      E_P: 65.88
6730-      E_R: 70.29
6731-      R_F1: 46.05
6732-      R_P: 41.83
6733-      R_R: 51.23
6734-      tcr_changed_selection: 0/551 (0.0%)
6735:    conclusion: negative
6736-    hypothesis: TCR reranking on beam4 outputs will change beam selection for LLaMA-SciERC
6737-      by penalizing constraint-violating candidates, improving DR violation rate and
6738-      overall F1 compared to vanilla beam4.
6739-    completed_at: '2026-05-22T16:27:25.157Z'
6740-  entity_order_ablation_qwen_scierc:
6741-    status: DONE
6742-    retry_count: 0
6743-    created_at: '2026-05-22T16:48:40.066Z'
6744-    updated_at: '2026-05-22T18:16:23.650Z'
6745-    hypothesis: Shuffling entity type order in the constraint schema (seed=42) does
--
6844-      server: westd-21461
6845-      data_path: data/processed_data/test.json
6846-      data_count: 551
6847-      model_name: Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)
6848-      seed: 42
6849-      checkpoint_source: /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663
6850-      eval_data: SciERC test (551 sentences)
6851-      checkpoint_path: /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663
6852-      log_path: /tmp/70b_lora_scierc_grammar_only.log
6853-      pid: 70175
6854:    conclusion: negative
6855-    metrics:
6856-      samples: 551
6857-      json_failures: 0
6858-      json_failure_rate: 0
6859-      entities: 1805
6860-      relations: 1133
6861-      entity_type_violations: 0
6862-      entity_type_violation_rate: 0
6863-      relation_vocab_violations: 0
6864-      relation_vocab_violation_rate: 0
--
6985-      gpu: cuda:1
6986-      pid: 972139
6987-      data_path: data/processed_data/test.json
6988-      data_count: 551
6989-      model_name: Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc
6990-      seed: 42
6991-      checkpoint_source: /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663
6992-      eval_data: SciERC test 551 docs
6993-      checkpoint_path: /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663
6994-      log_path: /tmp/70b_lora_scierc_full_s2.log
6995:    conclusion: negative
6996-    metrics:
6997-      samples: 551
6998-      json_failures: 0
6999-      entities: 1531
7000-      relations: 1027
7001-      ET_pct: 0
7002-      RV_pct: 0
7003-      DR_pct: 0
7004-      CF_count: 18
7005-      E_F1: 62.35
--
7132-      DR_pct: 0.38
7133-      CF_pct: 0.06
7134-      E_F1: 80.13
7135-      E_P: 85.16
7136-      E_R: 75.66
7137-      R_F1: 43.96
7138-      R_P: 39.78
7139-      R_R: 49.11
7140-      entities_pred: 3362
7141-      relations_pred: 3154
7142:    conclusion: negative
7143-    completed_at: '2026-05-23T01:55:24.472Z'
7144-  eval_70b_zs_docred_200_semantic_only:
7145-    status: DONE
7146-    retry_count: 0
7147-    created_at: '2026-05-22T20:35:21.150Z'
7148-    updated_at: '2026-05-22T22:55:11.458Z'
7149-    hypothesis: Semantic-only constraints on 70B ZS DocRED will significantly reduce
7150-      DR violations from zero-shot baseline, demonstrating the semantic layer's effectiveness
7151-      on document-level RE without fine-tuning.
7152-    parent: 70b_docred_unconstrained
--
7219-      RV_pct: 0
7220-      DR_pct: 17.03
7221-      CF_count: 0
7222-      fuzzy_matches: 0
7223-      E_F1: 70.12
7224-      E_P: 75.88
7225-      E_R: 65.17
7226-      R_F1: 13.23
7227-      R_P: 12.99
7228-      R_R: 13.47
7229:    conclusion: negative
7230-    completed_at: '2026-05-23T00:37:43.935Z'
7231-  eval_70b_zs_docred_200_unconstrained:
7232-    status: DONE
7233-    retry_count: 0
7234-    created_at: '2026-05-22T22:55:27.332Z'
7235-    updated_at: '2026-05-23T00:38:42.757Z'
7236-    hypothesis: 70B ZS DocRED unconstrained 200-doc baseline to complete the ablation
7237-      matrix. Expect DR~15% and R-F1~13 consistent with prior 99-doc measurement,
7238-      providing matched-subset comparison for semantic_only (DR=1.66%) and grammar_only
7239-      experiments.
--
7357-      CF_pct: 0.34
7358-      parse_fail_pct: 0
7359-      pred_entities: 3819
7360-      pred_relations: 3546
7361-      entity_tp: 3218
7362-      entity_fp: 586
7363-      entity_fn: 553
7364-      relation_tp: 1104
7365-      relation_fp: 2429
7366-      relation_fn: 1421
7367:    conclusion: negative
7368-    completed_at: '2026-05-23T08:04:47.609Z'
7369-  sf2_llama_int4_scierc_s1:
7370-    status: DONE
7371-    retry_count: 0
7372-    created_at: '2026-05-23T04:58:33.950Z'
7373-    updated_at: '2026-05-23T05:35:25.774Z'
7374-    hypothesis: AWQ INT4 quantization of fine-tuned Llama-3.1-8B does not significantly
7375-      affect constraint enforcement on SciERC S1
7376-    parent: w5_llama_lora_scierc_constrained_eval
7377-    spec:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc0bb7b9-b4d8-44ad-a63d-8f0b85584a2d",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "f8d8333c-570b-49d8-b462-87107bd8e544",
  "sourceToolAssistantUUID": "bc0bb7b9-b4d8-44ad-a63d-8f0b85584a2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-23T18:11:35.037Z_

Now let me get the experiment names for the negative conclusions to understand what each experiment was about.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8d8333c-570b-49d8-b462-87107bd8e544",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx9y6cZFBKsNwT5Euz3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c4f2c43-8a34-4d6a-9e54-506e60707e34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QSMrxszDfsD9DMw9e18Mza",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5884,
      "cache_read_input_tokens": 80372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5884,
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

_source line 37 · 2026-05-23T18:11:37.222Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ft1qxF7nQkvCrBBdQ9B1UD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml",
  "offset": 1400,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c4f2c43-8a34-4d6a-9e54-506e60707e34",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx9y6cZFBKsNwT5Euz3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f05e344-44a7-4f1b-bc7a-321dde465c2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QSMrxszDfsD9DMw9e18Mza",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5884,
      "cache_read_input_tokens": 80372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5884,
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

_source line 38 · 2026-05-23T18:11:37.231Z_

<details><summary>↩ Tool result · `toolu_01Ft1qxF7nQkvCrBBdQ9B1UD`</summary>

```text
1400	        1 --max_new_tokens 2048"
1401	      finished_at: '2026-05-15T14:47:53.690Z'
1402	    extra:
1403	      hook_events:
1404	      - event: on_complete
1405	        action: agent
1406	        ts: '2026-05-15T14:47:54.986519+00:00'
1407	    checkpoint_path: /root/schema_semantic_constrained_ie/outputs/w1_cf_fallback_scierc_pilot.jsonl
1408	    metrics:
1409	      ET: 0
1410	      RV: 0
1411	      DR: 0.1478
1412	      CF: 0.0004
1413	      R_F1: 0.0823
1414	      R_P: 0.0643
1415	      R_R: 0.114
1416	      E_F1: 0.3098
1417	      E_P: 0.2598
1418	      E_R: 0.3837
1419	      entities: 2474
1420	      relations: 1725
1421	      samples: 551
1422	      grammar_first_fallback_rate: 0.3664
1423	      cf_registry_fallback_rate: 0.0448
1424	      total_mask_calls: 17024
1425	      violation_budget_DR_CF: 0.1482
1426	    notes: CF fallback 实验在 SciERC + Qwen3-8B 上的 pilot 结果：CF 从 9.90% 下降到 0.04% (-9.86pp)，但
1427	      DR 从 0.93% 上升到 14.78% (+13.85pp)。DR+CF budget 净增 +3.99pp。F1 几乎不变 (E-F1=30.98%
1428	      与 baseline 完全一致；R-F1=8.23%, -0.13pp)。Grammar-first fallback 触发率 36.64% (6237/17024
1429	      mask calls)，CF-registry fallback 4.48%。判定：成功降低 CF 但代价是 DR 大幅恶化，违规没有真正减少，只是从
1430	      CF 转移到 DR。建议改进方向：(1) 仅在 CF-registry 命中时回退，保留 DR enforcement；(2) rebuttal 中诚实呈现这是
1431	      violation re-routing 而非 reduction。详细报告见 artifact w1_cf_fallback_scierc_pilot_analysis。
1432	    conclusion: negative
1433	    completed_at: '2026-05-15T14:57:13.885Z'
1434	    hypothesis: Constrained fallback (CF) 策略 SciERC pilot：约束解码产生空输出时回退至 unconstrained
1435	      生成，预期降低空输出率同时维持 violation 控制。若 fallback 频率过高则 CF 策略不可行。
1436	  w1_cf_fallback_docred:
1437	    status: DONE
1438	    retry_count: 1
1439	    created_at: '2026-05-15T10:32:53.234Z'
1440	    updated_at: '2026-05-15T16:55:58.012Z'
1441	    server: westd-16980
1442	    gpu: cuda:1
1443	    account: root
1444	    reproduce:
1445	      command: bash -c "rm -f /root/schema_semantic_constrained_ie/outputs/w1_cf_fallback_docred.jsonl
1446	        && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&
1447	        cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py
1448	        --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B
1449	        --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json
1450	        --output_path outputs/w1_cf_fallback_docred.jsonl --device cuda:0 --batch_size
1451	        1 --max_new_tokens 4096"
1452	    notes: 'Reviewer #12 三次确认: 实际运行 --mode full_s1 (非 CF fallback), 与 phase2_docred_full_s1
1453	      重复。CF fallback 代码恢复失败或未生效。命令行明确显示 --mode full_s1。PID 283824 已 kill。W1 CF fallback
1454	      整体定论: SciERC pilot (analytical finding) 已充分, DocRED 不再重跑。'
1455	    completed_at: '2026-05-15T15:47:59.075Z'
1456	    extra:
1457	      previous_failure:
1458	        conclusion: killed
1459	        notes: 'D020: Director 取消全部 CF fallback 实验。改用 Analytical Finding 方案——pilot
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f05e344-44a7-4f1b-bc7a-321dde465c2d",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "758c1ff1-64d4-4dd3-bcbc-bf2df4915e91",
  "sourceToolAssistantUUID": "7f05e344-44a7-4f1b-bc7a-321dde465c2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T18:11:38.248Z_

<details open><summary>🔧 Tool call — Read · `toolu_017qxpM6FSs3BePqQHhqGum8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml",
  "offset": 3330,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "758c1ff1-64d4-4dd3-bcbc-bf2df4915e91",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx9y6cZFBKsNwT5Euz3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3dbaae7c-be4e-4285-9fdc-4b82ddc66cf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QSMrxszDfsD9DMw9e18Mza",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5884,
      "cache_read_input_tokens": 80372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5884,
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

_source line 40 · 2026-05-23T18:11:38.255Z_

<details><summary>↩ Tool result · `toolu_017qxpM6FSs3BePqQHhqGum8`</summary>

```text
3330	    retry_count: 0
3331	    created_at: '2026-05-17T05:07:18.638Z'
3332	    updated_at: '2026-05-17T07:09:41.619Z'
3333	    hypothesis: Document-level type consensus constraint (forcing same entity text
3334	      to receive identical type across all relation triples) will eliminate CF violations
3335	      caused by inconsistent type assignment, reducing CF from ~9.90% toward 0% on
3336	      SciERC without increasing DR
3337	    spec:
3338	      command: python run_constrained_extraction.py --mode full_s1 --dataset scierc
3339	        --type_consensus --device cuda:0
3340	      server: westd-16980
3341	      gpu:
3342	      - cuda:0
3343	      pid: '417859'
3344	      log_path: ~/runs/schema_semantic_constrained_ie/w10_type_consensus_prototype.log
3345	      submitted_at: '2026-05-17T05:34:19.247Z'
3346	      submitted_via: submit_training_job
3347	      backend: tmux
3348	      account: root
3349	      model_name: Qwen3-8B
3350	      data_path: data/processed_data/test.json
3351	      data_count: 551
3352	      seed: 42
3353	      notes: 'GTC Layer 3 v2 (DR-aware skip). Kill switch: DR>2% → abort.'
3354	      wall_clock_seconds: 5722.4
3355	      gpu_hours: 1.59
3356	    metrics:
3357	      ET_pct: 0
3358	      RV_pct: 0
3359	      DR_pct: 0.93
3360	      CF_pct: 9.9
3361	      E_F1: 30.98
3362	      R_F1: 8.36
3363	      gtc_skip_total: 672
3364	      gtc_skip_unique_entities: 258
3365	      gtc_effective_corrections: 0
3366	      delta_DR: 0
3367	      delta_CF: 0
3368	    conclusion: negative
3369	    checkpoint_path: /root/schema_semantic_constrained_ie/outputs/scierc_full_s1_consensus_v2.jsonl
3370	    log_path: ~/runs/schema_semantic_constrained_ie/w10_type_consensus_prototype.log
3371	    completed_at: '2026-05-17T07:09:41.619Z'
3372	  w10_type_consensus_docred_50:
3373	    status: DONE
3374	    retry_count: 0
3375	    created_at: '2026-05-17T06:06:56.659Z'
3376	    updated_at: '2026-05-17T07:09:42.510Z'
3377	    hypothesis: GTC Layer 3 on DocRED (96 relation types, complex schema) will reduce
3378	      CF violations while maintaining DR through DR-aware skip mechanism; skip frequency
3379	      expected higher than SciERC due to more type ambiguity in fine-grained ontology
3380	    spec:
3381	      command: python run_constrained_extraction.py --mode full_s1 --dataset docred
3382	        --type_consensus --max_samples 50 --device cuda:0
3383	      server: westd-16980
3384	      gpu:
3385	      - cuda:1
3386	      pid: '419622'
3387	      log_path: ~/runs/schema_semantic_constrained_ie/w10_type_consensus_docred_50.log
3388	      submitted_at: '2026-05-17T06:07:17.194Z'
3389	      submitted_via: submit_training_job
3390	      backend: tmux
3391	      account: root
3392	      model_name: Qwen3-8B
3393	      data_path: data/processed_data/docred_test.json
3394	      data_count: 50
3395	      seed: 42
3396	      notes: GTC Layer 3 v2 on DocRED 96-type schema. Testing skip frequency under
3397	        complex ontology.
3398	      wall_clock_seconds: 3745.3
3399	      gpu_hours: 1.04
3400	    metrics:
3401	      ET_pct: 0
3402	      RV_pct: 0
3403	      DR_pct: 8.69
3404	      CF_pct: 2.4
3405	      E_F1: 59.08
3406	      R_F1: 8.33
3407	      gtc_skip_total: 601
3408	      gtc_skip_unique_entities: 213
3409	      gtc_effective_corrections: 0
3410	      delta_DR: 0
3411	      delta_CF: 0
3412	    conclusion: negative
3413	    checkpoint_path: /root/schema_semantic_constrained_ie/outputs/docred_full_s1_consensus_50.jsonl
3414	    log_path: ~/runs/schema_semantic_constrained_ie/w10_type_consensus_docred_50.log
3415	    completed_at: '2026-05-17T07:09:42.510Z'
3416	  w10_llama_docred_beam_50:
3417	    status: DONE
3418	    retry_count: 0
3419	    created_at: '2026-05-17T07:11:24.746Z'
3420	    updated_at: '2026-05-17T07:56:15.809Z'
3421	    hypothesis: Beam search (k=4) on Llama DocRED will reduce DR and CF violations,
3422	      completing the beam search matrix (3rd model-dataset combination). Llama's weaker
3423	      entity typing on DocRED may limit DR elimination compared to Qwen.
3424	    spec:
3425	      command: python run_constrained_extraction.py --mode full_s1 --dataset docred
3426	        --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct
3427	        --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json
3428	        --output_path outputs/docred_llama_beam_50.jsonl --decoding_strategy beam
3429	        --num_beams 4 --device cuda:0 --max_samples 50
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dbaae7c-be4e-4285-9fdc-4b82ddc66cf5",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "a3e6682f-45b0-420e-a3cd-de3fe0dd4ed3",
  "sourceToolAssistantUUID": "3dbaae7c-be4e-4285-9fdc-4b82ddc66cf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T18:11:38.699Z_

<details open><summary>🔧 Tool call — Read · `toolu_014jurfSH84omVgbhfZxZkQG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml",
  "offset": 4890,
  "limit": 70
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3e6682f-45b0-420e-a3cd-de3fe0dd4ed3",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKx9y6cZFBKsNwT5Euz3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d2dfc07-37cf-4ad3-99cf-50ecca4bd583",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QSMrxszDfsD9DMw9e18Mza",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5884,
      "cache_read_input_tokens": 80372,
      "output_tokens": 349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5884
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 349,
          "cache_read_input_tokens": 80372,
          "cache_creation_input_tokens": 5884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5884,
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

_source line 42 · 2026-05-23T18:11:38.707Z_

<details><summary>↩ Tool result · `toolu_014jurfSH84omVgbhfZxZkQG`</summary>

```text
4890	    conclusion: success
4891	    spec:
4892	      command: run_constrained_extraction.py (unconstrained + full_s1)
4893	      server: westd-16980
4894	      gpu: cuda:0
4895	      data_path: data/wikievents/test.jsonl
4896	      data_count: 20
4897	      model_name: Llama-3.1-8B-Instruct LoRA FT merged
4898	      seed: 42
4899	      checkpoint_source: /root/autodl-tmp/checkpoints/llama_8b_lora_wikievents_merged
4900	      eval_data: data/wikievents/test.jsonl (20 docs)
4901	      checkpoint_path: /root/autodl-tmp/checkpoints/llama_8b_lora_wikievents_merged
4902	      log_path: /root/schema_semantic_constrained_ie/logs/unconstrained_r2.log
4903	      fixes:
4904	      - schema required entities->events only
4905	      - repetition_penalty=1.2
4906	      - peft AWQ monkey-patch
4907	    completed_at: '2026-05-18T23:45:05.884Z'
4908	  d062_full_ft_scierc:
4909	    status: DONE
4910	    retry_count: 0
4911	    created_at: '2026-05-19T03:15:32.642Z'
4912	    updated_at: '2026-05-19T05:11:24.604Z'
4913	    hypothesis: Full fine-tuning Qwen3-8B on SciERC (all parameters, not just LoRA
4914	      adapters) will yield higher extraction F1 than LoRA FT, and the unconstrained
4915	      model will still produce schema violations (DR > 0%), confirming OntoCoDec constraints
4916	      remain necessary even with stronger fine-tuning.
4917	    spec:
4918	      command: bash scripts/run_d062_full_ft_scierc.sh
4919	      server: westd-21461
4920	      gpu: cuda:0
4921	      data_path: data/sft/scierc_sft_train.jsonl
4922	      data_count: 1762
4923	      model_name: Qwen3-8B (full fine-tuning)
4924	      seed: 42
4925	      training_method: full_fine_tuning
4926	      hyperparams:
4927	        lr: 2e-4
4928	        epochs: 3
4929	        batch_size: 16
4930	        gradient_checkpointing: true
4931	        bf16: true
4932	        warmup_ratio: 0.1
4933	        optimizer: AdamW
4934	        schedule: cosine
4935	    reproduce:
4936	      finished_at: '2026-05-19T04:50:16.081Z'
4937	    failure_reason: process dead 5× with no sentinel/W&B — auto-resolved as failed
4938	    conclusion: negative
4939	    completed_at: '2026-05-19T04:50:14.990Z'
4940	    extra:
4941	      hook_events:
4942	      - event: on_failed
4943	        action: agent
4944	        ts: '2026-05-19T04:50:21.524569+00:00'
4945	    metrics:
4946	      unconstrained:
4947	        entity_f1: 0.6478
4948	        relation_f1: 0.3789
4949	        DR_pct: 2.74
4950	        RV_pct: 0.18
4951	        ET_pct: 0
4952	        CF_pct: 0
4953	      constrained:
4954	        entity_f1: 0.6478
4955	        relation_f1: 0.3789
4956	        DR_pct: 0
4957	        RV_pct: 0
4958	        ET_pct: 0
4959	        CF_pct: 1.31
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d2dfc07-37cf-4ad3-99cf-50ecca4bd583",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "86238eec-0234-4e04-88d6-1bf7ffa72f5e",
  "sourceToolAssistantUUID": "7d2dfc07-37cf-4ad3-99cf-50ecca4bd583",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-23T18:11:41.369Z_

Now let me get the remaining negative experiment names and details by reading around the other negative conclusion markers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86238eec-0234-4e04-88d6-1bf7ffa72f5e",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKxANigR5MxoWNSvNfRE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a63d5dd4-459b-41b5-8ee2-0d5d268a00f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Spqw1nBDL5iT9TvWDCwYt7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4682,
      "cache_read_input_tokens": 86256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4682,
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

_source line 44 · 2026-05-23T18:11:42.539Z_

<details open><summary>🔧 Tool call — Read · `toolu_01U2HTEsGNkriQbVjAQmQyk7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml",
  "offset": 4960,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a63d5dd4-459b-41b5-8ee2-0d5d268a00f7",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKxANigR5MxoWNSvNfRE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d65cc4cf-3444-4afb-a000-9bc5910c23bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Spqw1nBDL5iT9TvWDCwYt7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4682,
      "cache_read_input_tokens": 86256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4682,
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

_source line 45 · 2026-05-23T18:11:42.563Z_

<details><summary>↩ Tool result · `toolu_01U2HTEsGNkriQbVjAQmQyk7`</summary>

```text
4960	      training:
4961	        eval_loss_final: 0.09459
4962	        epochs: 3
4963	        total_steps: 333
4964	        training_time: 21m49s
4965	    checkpoint_path: /root/autodl-tmp/checkpoints/qwen_full_ft_scierc/
4966	    log_path: /root/autodl-tmp/d062_full_ft_scierc.log
4967	  d062_cf_majority_voting:
4968	    status: DONE
4969	    retry_count: 0
4970	    created_at: '2026-05-19T03:15:34.085Z'
4971	    updated_at: '2026-05-19T03:23:41.243Z'
4972	    hypothesis: Majority voting over entity types within each document can reduce
4973	      CF violations without significantly increasing DR violations, because the most
4974	      frequent type assignment for each entity is likely the ontology-consistent one.
4975	    spec:
4976	      command: python3 scripts/cf_majority_voting.py
4977	      server: westd-16980
4978	      data_path: /root/schema_semantic_constrained_ie/outputs/
4979	      data_count: 8
4980	      model_name: n/a (post-hoc)
4981	      seed: 0
4982	      checkpoint_source: n/a
4983	      checkpoint_path: n/a
4984	      log_path: outputs/cf_correction_report_*.json
4985	    metrics:
4986	      qwen_scierc_zs:
4987	        cf_before: 245
4988	        cf_after: 201
4989	        dr_rate_before: 0.0093
4990	        dr_rate_after: 0.0324
4991	      llama_scierc_zs:
4992	        cf_before: 162
4993	        cf_after: 123
4994	        dr_rate_before: 0.0008
4995	        dr_rate_after: 0.0236
4996	      qwen_docred_zs:
4997	        cf_before: 518
4998	        cf_after: 21
4999	        dr_rate_before: 0.1021
5000	        dr_rate_after: 0.1466
5001	      llama_docred_zs:
5002	        cf_before: 1358
5003	        cf_after: 107
5004	        dr_rate_before: 0.0255
5005	        dr_rate_after: 0.1665
5006	      qwen_scierc_ft:
5007	        cf_before: 21
5008	        cf_after: 12
5009	        dr_rate_before: 0
5010	        dr_rate_after: 0.0071
5011	      llama_scierc_ft:
5012	        cf_before: 8
5013	        cf_after: 4
5014	        dr_rate_before: 0.0009
5015	        dr_rate_after: 0.0037
5016	      qwen_docred_ft:
5017	        cf_before: 48
5018	        cf_after: 3
5019	        dr_rate_before: 0.0001
5020	        dr_rate_after: 0.0044
5021	      llama_docred_ft:
5022	        cf_before: 41
5023	        cf_after: 2
5024	        dr_rate_before: 0.0021
5025	        dr_rate_after: 0.005
5026	    conclusion: negative
5027	    completed_at: '2026-05-19T03:23:41.243Z'
5028	  d062_beam_latency:
5029	    status: DONE
5030	    retry_count: 0
5031	    created_at: '2026-05-19T03:15:35.458Z'
5032	    updated_at: '2026-05-19T04:30:54.166Z'
5033	    hypothesis: Beam search (k=4) with constrained decoding will have higher latency
5034	      overhead relative to greedy than unconstrained beam search, because the constraint
5035	      processor must independently track and validate grammar/semantic state for each
5036	      of the 4 beams at every decoding step.
5037	    spec:
5038	      command: bash scripts/run_d062_beam_latency.sh
5039	      server: westd-21461
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d65cc4cf-3444-4afb-a000-9bc5910c23bf",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "04cc6acf-4747-4efa-bfac-9c956f145c3c",
  "sourceToolAssistantUUID": "d65cc4cf-3444-4afb-a000-9bc5910c23bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-23T18:11:43.561Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UGZc8pg2RVUzEcnQT1tBHU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml",
  "offset": 5240,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04cc6acf-4747-4efa-bfac-9c956f145c3c",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKxANigR5MxoWNSvNfRE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f9f47ee-1233-40d9-88d7-51dc24327c06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Spqw1nBDL5iT9TvWDCwYt7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4682,
      "cache_read_input_tokens": 86256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4682,
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

_source line 47 · 2026-05-23T18:11:43.569Z_

<details><summary>↩ Tool result · `toolu_01UGZc8pg2RVUzEcnQT1tBHU`</summary>

```text
5240	      Mistral, 70B) and fine-tuning settings, but effectiveness is inversely correlated
5241	      with mean schema constraint tightness (κ̄): higher κ̄ (more restrictive schemas
5242	      like DocRED) produces more fundamental conflicts where no single entity type
5243	      satisfies all relational contexts, causing DR to increase when CF is forcibly
5244	      resolved.'
5245	    parent: d065_tcr_pilot
5246	    conclusion: success
5247	    metrics:
5248	      configs_tested: 10
5249	      all_cf_eliminated: true
5250	      scierc_all_dr_delta_max: 0.28
5251	      docred_lora_dr_delta_max: 0.14
5252	      docred_zs_llama_dr_delta: 9.38
5253	      docred_zs_70b_dr_delta: 4.2
5254	      docred_zs_qwen_dr_delta: 1.53
5255	      fund_conflict_scierc_max: 2.04
5256	      fund_conflict_docred_zs_max: 22.78
5257	      fund_conflict_docred_lora_max: 12.16
5258	      lora_ef1_cost_max: 0.0075
5259	      zs_docred_ef1_cost_max: 0.0598
5260	    checkpoint_path: outputs/tcr/
5261	    log_path: d065_tcr_full_results.md
5262	    completed_at: '2026-05-19T11:44:17.092Z'
5263	  d068_constraint_guided_beam_pilot:
5264	    status: DONE
5265	    retry_count: 0
5266	    created_at: '2026-05-19T16:38:01.430Z'
5267	    updated_at: '2026-05-19T16:49:55.045Z'
5268	    hypothesis: Constraint-guided beam scoring (score = logP - β×violations) reduces
5269	      CF without degrading DR/F1, by penalizing beams with more constraint violations
5270	      during search
5271	    spec:
5272	      command: python run_constrained_extraction.py --constraint_penalty {0.0,0.5,1.0,2.0}
5273	        --decoding_strategy beam --num_beams 4 --constraint_mode full_s1
5274	      server: westd-16980 + westd-21461
5275	      data_path: data/processed_data/test.json (SciERC 551 samples)
5276	      data_count: 551
5277	      model_name: Qwen3-8B LoRA SciERC (qwen3_8b_lora_scierc_merged)
5278	      seed: 42
5279	      parameters:
5280	        beta:
5281	        - 0
5282	        - 0.5
5283	        - 1
5284	        - 2
5285	        beam: 4
5286	        mode: full_s1
5287	      claim: Claim 3 + method enhancement
5288	      code_location: run_constrained_extraction.py:746-808 run_single_pass_beam()
5289	      checkpoint_path: /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged
5290	      log_path: outputs/d068_guided_beam/ on both servers
5291	      partial_result: all violations 0% at ~20% completion - penalty has no effect
5292	        on LoRA model
5293	      negative_reason: LoRA model beam candidates already 0% violations; penalty term
5294	        always 0; F1 drops 0.3-5.3pp due to multi-sequence decoding noise. Director
5295	        decided No-Go, killed at ~20% completion.
5296	    conclusion: negative
5297	    completed_at: '2026-05-19T16:49:55.045Z'
5298	  d066_beam_sweep:
5299	    status: DONE
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f9f47ee-1233-40d9-88d7-51dc24327c06",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "74bca233-1927-4b40-b17e-c4afdbcafffc",
  "sourceToolAssistantUUID": "1f9f47ee-1233-40d9-88d7-51dc24327c06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-23T18:11:44.437Z_

<details open><summary>🔧 Tool call — Read · `toolu_018zi22gwLcYeJ6ZKVHFFsvw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml",
  "offset": 6660,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74bca233-1927-4b40-b17e-c4afdbcafffc",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKxANigR5MxoWNSvNfRE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac2ecbec-cd00-49bb-ab8d-ae002957a70c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Spqw1nBDL5iT9TvWDCwYt7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4682,
      "cache_read_input_tokens": 86256,
      "output_tokens": 350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4682
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 350,
          "cache_read_input_tokens": 86256,
          "cache_creation_input_tokens": 4682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4682,
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

_source line 49 · 2026-05-23T18:11:44.448Z_

<details><summary>↩ Tool result · `toolu_018zi22gwLcYeJ6ZKVHFFsvw`</summary>

```text
6660	      eval_data: SciERC test 551 docs
6661	      checkpoint_path: /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663
6662	      log_path: /tmp/70b_lora_scierc_beam4_s1.log
6663	    conclusion: success
6664	    metrics:
6665	      E_F1: 64.89
6666	      E_P: 62.29
6667	      E_R: 67.72
6668	      R_F1: 44.81
6669	      R_P: 39.45
6670	      R_R: 51.85
6671	      DR_pct: 0
6672	      RV_pct: 0
6673	      ET_pct: 0
6674	      CF_count: 1
6675	      parse_fail_pct: 0
6676	      samples: 551
6677	      entities: 1839
6678	      relations: 1283
6679	    completed_at: '2026-05-22T18:04:29.880Z'
6680	  eval_70b_zs_scierc_grammar_only:
6681	    status: DONE
6682	    retry_count: 0
6683	    created_at: '2026-05-22T14:39:44.901Z'
6684	    updated_at: '2026-05-22T18:09:48.056Z'
6685	    hypothesis: Grammar-only constraints on 70B ZS reduce domain-range violations
6686	      compared to unconstrained baseline (DR=6.41%) but less effectively than full_s1
6687	      (DR=0%), isolating grammar layer's contribution to constraint enforcement.
6688	    spec:
6689	      command: CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path
6690	        /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4
6691	        --data_path data/processed_data/test.json --dataset scierc --mode grammar_only
6692	        --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_grammar_only.jsonl
6693	        --max_new_tokens 2048
6694	      server: westd-21461
6695	      data_path: data/processed_data/test.json
6696	      data_count: 551
6697	      model_name: Llama-3.1-70B-Instruct-AWQ-INT4 (ZS)
6698	      seed: 42
6699	      checkpoint_path: N/A (eval-only)
6700	      log_path: /tmp/eval_70b_zs_scierc_grammar_only.log
6701	    conclusion: negative
6702	    metrics:
6703	      R_F1: 11.23
6704	      DR_pct: 6.33
6705	      RV_pct: 0
6706	      ET_pct: 0
6707	      CF_count: 0
6708	      samples: 551
6709	    completed_at: '2026-05-22T18:09:48.056Z'
6710	  tcr_beam4_llama_scierc:
6711	    status: DONE
6712	    retry_count: 0
6713	    created_at: '2026-05-22T15:48:16.222Z'
6714	    updated_at: '2026-05-22T16:27:25.157Z'
6715	    spec:
6716	      checkpoint_path: N/A (eval-only)
6717	      log_path: /tmp/beam4_tcr_llama_scierc.log
6718	    metrics:
6719	      samples: 551
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac2ecbec-cd00-49bb-ab8d-ae002957a70c",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "850f85d8-3803-4d4a-8e0d-3de376d003f8",
  "sourceToolAssistantUUID": "ac2ecbec-cd00-49bb-ab8d-ae002957a70c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-23T18:11:46.764Z_

Now let me read a few more registry sections for the remaining negative experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "850f85d8-3803-4d4a-8e0d-3de376d003f8",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKxAoJXmkAjxAAqLvb16",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66ec6257-d2e8-447f-bbd6-48dec2ee3866",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0155dbAWYN39GuncVA75suEW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3706,
      "cache_read_input_tokens": 90938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3706,
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

_source line 51 · 2026-05-23T18:11:48.366Z_

<details open><summary>🔧 Tool call — Read · `toolu_019XV2iPVJUYB23gwgqYWKfF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml",
  "offset": 7050,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66ec6257-d2e8-447f-bbd6-48dec2ee3866",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKxAoJXmkAjxAAqLvb16",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95aa981b-2f6d-4607-926c-cca72c7dbc27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0155dbAWYN39GuncVA75suEW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3706,
      "cache_read_input_tokens": 90938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3706,
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

_source line 52 · 2026-05-23T18:11:48.375Z_

<details><summary>↩ Tool result · `toolu_019XV2iPVJUYB23gwgqYWKfF`</summary>

```text
7050	      E_R: 42.38
7051	      R_F1: 11.23
7052	      R_P: 9.31
7053	      R_R: 14.17
7054	      parse_fail_pct: 0
7055	    completed_at: '2026-05-22T20:30:18.431Z'
7056	  eval_70b_lora_docred_200_semantic_only:
7057	    status: DONE
7058	    retry_count: 0
7059	    created_at: '2026-05-22T20:35:17.601Z'
7060	    updated_at: '2026-05-23T01:20:56.659Z'
7061	    hypothesis: Semantic-only constraints on 70B LoRA DocRED will reduce DR violations
7062	      from unconstrained baseline (DR=0.88%) with minimal F1 impact, isolating the
7063	      semantic layer's contribution in document-level RE at 70B fine-tuned scale.
7064	    parent: eval_70b_lora_docred_200_unconstrained
7065	    spec:
7066	      command: CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path
7067	        /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4
7068	        --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path
7069	        data/docred/dev.json --dataset docred --mode semantic_only --constraints_path
7070	        data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_semantic_only.jsonl
7071	        --max_docs 200 --max_new_tokens 4096
7072	      server: westd-16980
7073	      gpu: cuda:0
7074	      pid: 983803
7075	      data_path: data/docred/dev.json
7076	      data_count: 200
7077	      model_name: Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred
7078	      seed: 42
7079	      checkpoint_source: /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146
7080	      eval_data: DocRED dev 200 docs
7081	      checkpoint_path: /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146
7082	      log_path: /tmp/70b_lora_docred_200_semantic_only.log
7083	    metrics:
7084	      samples: 200
7085	      parse_fail_pct: 11
7086	      ET_pct: 0
7087	      RV_pct: 0.51
7088	      DR_pct: 0
7089	      CF_pct: 0.21
7090	      E_F1: 80.06
7091	      E_P: 85.21
7092	      E_R: 75.5
7093	      R_F1: 43.61
7094	      R_P: 39.44
7095	      R_R: 48.75
7096	      entities_pred: 3351
7097	      relations_pred: 3148
7098	    conclusion: success
7099	    completed_at: '2026-05-23T01:20:56.659Z'
7100	  eval_70b_lora_docred_200_grammar_only:
7101	    status: DONE
7102	    retry_count: 0
7103	    created_at: '2026-05-22T20:35:19.975Z'
7104	    updated_at: '2026-05-23T01:55:24.472Z'
7105	    hypothesis: Grammar-only constraints on 70B LoRA DocRED will eliminate RV violations
7106	      but not reduce DR, mirroring the SciERC ablation pattern where grammar layer
7107	      provides zero DR contribution at fine-tuned scale.
7108	    parent: eval_70b_lora_docred_200_unconstrained
7109	    spec:
7110	      command: CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path
7111	        /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4
7112	        --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path
7113	        data/docred/dev.json --dataset docred --mode grammar_only --constraints_path
7114	        data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_grammar_only.jsonl
7115	        --max_docs 200 --max_new_tokens 4096
7116	      server: westd-16980
7117	      gpu: cuda:1
7118	      pid: 984253
7119	      data_path: data/docred/dev.json
7120	      data_count: 200
7121	      model_name: Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred
7122	      seed: 42
7123	      checkpoint_source: /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146
7124	      eval_data: DocRED dev 200 docs
7125	      checkpoint_path: /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146
7126	      log_path: /tmp/70b_lora_docred_200_grammar_only.log
7127	    metrics:
7128	      samples: 200
7129	      parse_fail_pct: 10.5
7130	      ET_pct: 0
7131	      RV_pct: 0
7132	      DR_pct: 0.38
7133	      CF_pct: 0.06
7134	      E_F1: 80.13
7135	      E_P: 85.16
7136	      E_R: 75.66
7137	      R_F1: 43.96
7138	      R_P: 39.78
7139	      R_R: 49.11
7140	      entities_pred: 3362
7141	      relations_pred: 3154
7142	    conclusion: negative
7143	    completed_at: '2026-05-23T01:55:24.472Z'
7144	  eval_70b_zs_docred_200_semantic_only:
7145	    status: DONE
7146	    retry_count: 0
7147	    created_at: '2026-05-22T20:35:21.150Z'
7148	    updated_at: '2026-05-22T22:55:11.458Z'
7149	    hypothesis: Semantic-only constraints on 70B ZS DocRED will significantly reduce
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95aa981b-2f6d-4607-926c-cca72c7dbc27",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "c18cf77d-30a8-47f1-8564-dbd284283304",
  "sourceToolAssistantUUID": "95aa981b-2f6d-4607-926c-cca72c7dbc27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-23T18:11:49.462Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rx9kd1hdww9JPRUBKh3E23`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml",
  "offset": 7290,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c18cf77d-30a8-47f1-8564-dbd284283304",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKxAoJXmkAjxAAqLvb16",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bf032c4-da16-4cae-95ca-29f83ef50ce5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0155dbAWYN39GuncVA75suEW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3706,
      "cache_read_input_tokens": 90938,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3706
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 90938,
          "cache_creation_input_tokens": 3706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3706,
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

_source line 54 · 2026-05-23T18:11:49.471Z_

<details><summary>↩ Tool result · `toolu_01Rx9kd1hdww9JPRUBKh3E23`</summary>

```text
7290	        data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_full_s1.jsonl
7291	        --max_new_tokens 4096 --max_samples 200
7292	      server: westd-21461
7293	      gpu: cuda:0
7294	      pid: 88678
7295	      data_path: data/docred/dev.json
7296	      data_count: 200
7297	      model_name: Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)
7298	      seed: 42
7299	      checkpoint_source: N/A (zero-shot)
7300	      eval_data: DocRED dev 200 docs
7301	      checkpoint_path: N/A
7302	      log_path: /tmp/70b_zs_docred_200_full_s1.log
7303	    metrics:
7304	      DR%: 0
7305	      RV%: 0
7306	      ET%: 0
7307	      CF%: 5.34
7308	      E-F1: 70.05
7309	      R-F1: 13.25
7310	      PF%: 0
7311	      entities_pred: 3234
7312	      relations_pred: 2637
7313	      triples_checked: 2642
7314	    checkpoint_path: /root/schema_semantic_constrained_ie/outputs/70b_zs_docred_200_full_s1.jsonl
7315	    log_path: /tmp/70b_zs_docred_200_full_s1.log
7316	    conclusion: success
7317	    completed_at: '2026-05-23T02:30:50.739Z'
7318	  eval_70b_lora_docred_200_full_s2:
7319	    status: DONE
7320	    retry_count: 0
7321	    created_at: '2026-05-23T00:41:30.126Z'
7322	    updated_at: '2026-05-23T08:04:47.609Z'
7323	    hypothesis: Full S2 (grammar+semantic+repair) on 70B LoRA DocRED should achieve
7324	      near-zero DR while maintaining R_F1 close to beam4_s1 (48.14). The repair layer
7325	      resolves residual DR violations from S1. This is the strongest constraint configuration
7326	      for DocRED LoRA.
7327	    parent: eval_70b_lora_docred_200_beam4_s1
7328	    spec:
7329	      command: CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path
7330	        /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4
7331	        --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path
7332	        data/docred/dev.json --dataset docred --mode full_s2 --constraints_path data/docred/ontology_constraints_docred.json
7333	        --output_path outputs/70b_lora_docred_200_full_s2.jsonl --max_new_tokens 4096
7334	        --max_samples 200
7335	      server: westd-21461
7336	      gpu: cuda:1
7337	      pid: 88990
7338	      data_path: data/docred/dev.json
7339	      data_count: 200
7340	      model_name: Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred (checkpoint-1146)
7341	      seed: 42
7342	      checkpoint_source: /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146
7343	      eval_data: DocRED dev 200 docs
7344	      checkpoint_path: /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146
7345	      log_path: /tmp/70b_lora_docred_200_full_s2.log
7346	    metrics:
7347	      R_F1: 36.45
7348	      R_P: 31.25
7349	      R_R: 43.72
7350	      E_F1: 84.96
7351	      E_P: 84.6
7352	      E_R: 85.34
7353	      DR_pct: 0
7354	      RV_pct: 0
7355	      ET_pct: 0
7356	      CF_count: 13
7357	      CF_pct: 0.34
7358	      parse_fail_pct: 0
7359	      pred_entities: 3819
7360	      pred_relations: 3546
7361	      entity_tp: 3218
7362	      entity_fp: 586
7363	      entity_fn: 553
7364	      relation_tp: 1104
7365	      relation_fp: 2429
7366	      relation_fn: 1421
7367	    conclusion: negative
7368	    completed_at: '2026-05-23T08:04:47.609Z'
7369	  sf2_llama_int4_scierc_s1:
7370	    status: DONE
7371	    retry_count: 0
7372	    created_at: '2026-05-23T04:58:33.950Z'
7373	    updated_at: '2026-05-23T05:35:25.774Z'
7374	    hypothesis: AWQ INT4 quantization of fine-tuned Llama-3.1-8B does not significantly
7375	      affect constraint enforcement on SciERC S1
7376	    parent: w5_llama_lora_scierc_constrained_eval
7377	    spec:
7378	      command: CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --mode
7379	        full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/
7380	        --data_path data/processed_data/test.json --constraints_path ontology_constraints.json
7381	        --output_path outputs/sf2_llama_int4_scierc_s1/raw_outputs.jsonl --device
7382	        cuda:0
7383	      server: westd-16980
7384	      data_path: /root/schema_semantic_constrained_ie/data/processed_data/test.json
7385	      data_count: 551
7386	      model_name: Llama-3.1-8B-SciERC-FT-AWQ-INT4
7387	      seed: 42
7388	      checkpoint_source: /root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/
7389	      eval_data: SciERC test (551 docs)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bf032c4-da16-4cae-95ca-29f83ef50ce5",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "74c0853c-e22d-42c8-807e-9d9c20490583",
  "sourceToolAssistantUUID": "2bf032c4-da16-4cae-95ca-29f83ef50ce5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-23T18:11:53.242Z_

Now I have enough information to compile the full report. Let me check what the `eval_70b_zs_scierc_grammar_only` experiment's hypothesis was — it was that grammar-only constraints would reduce DR on 70B ZS SciERC, but the result was DR=6.33% (vs unconstrained DR=6.41%), meaning it didn't reduce DR. And check the remaining negative ones briefly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74c0853c-e22d-42c8-807e-9d9c20490583",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKxBAYiqT9fSaucKhWHE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "386b2059-9545-4e38-bd8c-5756436f44cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HRrtdUQDK9h5bADHPvB82o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4077,
      "cache_read_input_tokens": 94644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4077,
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

_source line 56 · 2026-05-23T18:11:55.415Z_

<details open><summary>🔧 Tool call — Read · `toolu_01F1dtUDoSVRqxwKgkWb6oa2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml",
  "offset": 6810,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "386b2059-9545-4e38-bd8c-5756436f44cc",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKxBAYiqT9fSaucKhWHE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97644f27-48b3-4010-8be2-7ce23acd8049",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HRrtdUQDK9h5bADHPvB82o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4077,
      "cache_read_input_tokens": 94644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4077,
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

_source line 57 · 2026-05-23T18:11:55.424Z_

<details><summary>↩ Tool result · `toolu_01F1dtUDoSVRqxwKgkWb6oa2`</summary>

```text
6810	      parse_fail_pct: 0
6811	      samples: 551
6812	      entities: 1784
6813	      relations: 1128
6814	      corrected_original_R_F1: 43.77
6815	      corrected_original_E_F1: 67.05
6816	      corrected_original_DR_pct: 0
6817	      corrected_original_CF_count: 21
6818	      corrected_delta_R_F1: 0
6819	      corrected_delta_E_F1: 0
6820	      raw_output_identical: true
6821	      parsed_output_identical: true
6822	      note: 'CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows
6823	        ZERO difference. raw_output and parsed_output are byte-identical across all
6824	        551 samples. Previous -3.38pp delta was entirely due to comparing old-checker
6825	        original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed
6826	        order-invariant.'
6827	    completed_at: '2026-05-22T18:04:14.919Z'
6828	  eval_70b_lora_scierc_grammar_only:
6829	    status: DONE
6830	    retry_count: 0
6831	    created_at: '2026-05-22T17:13:55.324Z'
6832	    updated_at: '2026-05-22T20:31:32.878Z'
6833	    hypothesis: 70B LoRA SciERC with grammar-only constrained decoding will reduce
6834	      DR violations compared to unconstrained (DR=1.5%) but less than full_s1 (DR=0%),
6835	      isolating grammar layer's independent contribution at 70B fine-tuned scale.
6836	    parent: eval_70b_lora_scierc_unconstrained
6837	    spec:
6838	      command: CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path
6839	        /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4
6840	        --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path
6841	        data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path
6842	        ontology_constraints.json --output_path outputs/70b_lora_scierc_grammar_only.jsonl
6843	        --max_new_tokens 2048
6844	      server: westd-21461
6845	      data_path: data/processed_data/test.json
6846	      data_count: 551
6847	      model_name: Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)
6848	      seed: 42
6849	      checkpoint_source: /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663
6850	      eval_data: SciERC test (551 sentences)
6851	      checkpoint_path: /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663
6852	      log_path: /tmp/70b_lora_scierc_grammar_only.log
6853	      pid: 70175
6854	    conclusion: negative
6855	    metrics:
6856	      samples: 551
6857	      json_failures: 0
6858	      json_failure_rate: 0
6859	      entities: 1805
6860	      relations: 1133
6861	      entity_type_violations: 0
6862	      entity_type_violation_rate: 0
6863	      relation_vocab_violations: 0
6864	      relation_vocab_violation_rate: 0
6865	      domain_range_violations: 17
6866	      domain_range_violation_rate: 0.015
6867	      cross_field_consistency_violations: 0
6868	      fuzzy_relation_matches: 0
6869	      entity_P: 0.6272
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97644f27-48b3-4010-8be2-7ce23acd8049",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "d35bd616-634e-4d0a-91e4-f7f1d90ddd21",
  "sourceToolAssistantUUID": "97644f27-48b3-4010-8be2-7ce23acd8049",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-23T18:11:55.930Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SiGJaC4651Qif8BfD7EsE1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml",
  "offset": 7390,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d35bd616-634e-4d0a-91e4-f7f1d90ddd21",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKxBAYiqT9fSaucKhWHE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52bb80c5-c890-42bb-b70c-9920405562b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HRrtdUQDK9h5bADHPvB82o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4077,
      "cache_read_input_tokens": 94644,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4077
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 321,
          "cache_read_input_tokens": 94644,
          "cache_creation_input_tokens": 4077,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4077,
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

_source line 59 · 2026-05-23T18:11:55.937Z_

<details><summary>↩ Tool result · `toolu_01SiGJaC4651Qif8BfD7EsE1`</summary>

```text
7390	    metrics:
7391	      DR%: 0
7392	      RV%: 0
7393	      ET%: 0
7394	      CF%: 0.94
7395	      R-F1: 43.98
7396	      E-F1: 67.54
7397	      samples: 551
7398	      R-P: 40.47
7399	      R-R: 48.15
7400	      E-P: 65.51
7401	      E-R: 69.7
7402	    log_path: outputs/sf2_llama_int4_scierc_s1/violation_report.json
7403	    checkpoint_path: outputs/sf2_llama_int4_scierc_s1/raw_outputs.jsonl
7404	    conclusion: success
7405	    completed_at: '2026-05-23T05:32:49.329Z'
7406	  sf2_qwen_int4_scierc_s1:
7407	    status: DONE
7408	    retry_count: 0
7409	    created_at: '2026-05-23T04:58:51.930Z'
7410	    updated_at: '2026-05-23T05:35:24.911Z'
7411	    hypothesis: AWQ INT4 quantization of fine-tuned Qwen3-8B does not significantly
7412	      affect constraint enforcement on SciERC S1
7413	    parent: d066_beam_sweep
7414	    spec:
7415	      command: python run_constrained_extraction.py --mode full_s1 --dataset scierc
7416	        --model_path /root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/ --data_path
7417	        data/processed_data/test.json --constraints_path ontology_constraints.json
7418	        --output_path outputs/sf2_qwen_int4_scierc_s1/output.jsonl --device cuda:0
7419	        --seed 42
7420	      server: westd-16980
7421	      data_path: data/processed_data/test.json
7422	      data_count: 551
7423	      model_name: Qwen3-8B-SciERC-FT-AWQ-INT4
7424	      seed: 42
7425	      checkpoint_source: /root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/
7426	      eval_data: SciERC test 551 sentences
7427	    metrics:
7428	      DR%: 0
7429	      RV%: 0
7430	      ET%: 0
7431	      CF%: 1.1
7432	      R-F1: 41.71
7433	      E-F1: 67.05
7434	      samples: 551
7435	      R-P: 38.52
7436	      R-R: 45.48
7437	      E-P: 64.76
7438	      E-R: 69.52
7439	    log_path: outputs/sf2_qwen_int4_scierc_s1/violation_report.json
7440	    checkpoint_path: outputs/sf2_qwen_int4_scierc_s1/output.jsonl
7441	    conclusion: success
7442	    completed_at: '2026-05-23T05:32:46.404Z'
7443	  sf2_gollie_scierc_violation:
7444	    status: DONE
7445	    retry_count: 0
7446	    created_at: '2026-05-23T05:14:38.851Z'
7447	    updated_at: '2026-05-23T05:15:20.167Z'
7448	    hypothesis: GoLLIE-7B achieves low schema violation rates on SciERC zero-shot
7449	      because it outputs very conservatively (few entities, almost no relations),
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52bb80c5-c890-42bb-b70c-9920405562b2",
  "isSidechain": true,
  "promptId": "ddabfbfc-6d3c-4598-8eb3-502cd2e0ba14",
  "agentId": "aa0ebc68a17d43ebd",
  "type": "user",
  "uuid": "b88f0399-11ca-4276-8871-279c8ea45a3d",
  "sourceToolAssistantUUID": "52bb80c5-c890-42bb-b70c-9920405562b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-23T18:12:39.532Z_

I now have enough data to compile the complete report. Here is the analysis:

---

## Negative Results — Registry vs. Paper Coverage

### All Experiments with `conclusion: negative`

| Exp ID | What it tested | Key finding |
|---|---|---|
| `w1_cf_fallback_scierc_pilot` | CF-priority fallback (enforce entity registry type over domain/range) | Eliminates CF (9.9%→0.04%) but DR explodes (0.93%→14.78%), net violation budget +3.99pp — re-routing, not reduction |
| `w10_type_consensus_prototype` (SciERC) | Decoding-time global type consensus (GTC, DR-aware skip) | 0 effective corrections; DR and CF unchanged |
| `w10_type_consensus_docred_50` (DocRED) | Same GTC on DocRED 50-doc | 0 effective corrections; no change |
| `w10_mistral_scierc_beam_551` | Beam search k=4 on Mistral SciERC | DR unchanged (13.4%→13.8%); entity misclassification bottleneck, not token-search |
| `d062_full_ft_scierc` | Full fine-tuning (not LoRA) of Qwen3-8B | Process died 5× (infra failure), not a scientific negative |
| `d062_cf_majority_voting` | Post-hoc majority voting for CF resolution | Reduces CF but significantly increases DR in all 8 configs |
| `d068_constraint_guided_beam_pilot` | Constraint-penalty beam scoring (score = logP - β×violations) | LoRA model already 0% violations; penalty term always 0; F1 drops 0.3–5.3pp |
| `beam4_tcr_qwen_scierc` | TCR reranking on beam-4 outputs (Qwen SciERC) | 0/551 candidates changed; fine-tuned beam already type-consistent |
| `tcr_beam4_llama_scierc` | TCR reranking on beam-4 outputs (Llama SciERC) | 0/551 candidates changed; same conclusion |
| `eval_70b_zs_scierc_grammar_only` | Grammar-only on 70B ZS SciERC | DR=6.33% vs baseline 6.41% — no meaningful reduction |
| `eval_70b_lora_scierc_grammar_only` | Grammar-only on 70B LoRA SciERC | DR=1.5%→1.5% — complete no-op |
| `eval_70b_lora_docred_200_grammar_only` | Grammar-only on 70B LoRA DocRED | DR=0.38% (vs unconstrained 0.22%) — slight DR increase |
| `eval_70b_zs_docred_200_grammar_only` | Grammar-only on 70B ZS DocRED | DR=17.03% (vs unconstrained 13.45%) — DR increase due to vocabulary forcing |
| `eval_70b_lora_docred_200_full_s2` | S2 on 70B LoRA DocRED | R-F1 36.45 vs S1's 43.95 — severe F1 degradation (−7.50pp) |
| `eval_70b_lora_scierc_s2` (from `appendix_70b_ablation`) | S2 on 70B LoRA SciERC | R-F1 36.28 vs S1's 44.53 — severe degradation (−8.25pp) |

---

### Paper Coverage Assessment

| Experiment / Negative Result | Discussed in Paper? | Where | Notes |
|---|---|---|---|
| **CF-priority fallback** (w1_cf_fallback_scierc_pilot) | **YES — prominently** | `appendix_discussion.tex` §CF-DR Trade-off Analysis, Table `tab:cf-dr-tradeoff` | Explicitly discussed as "violation re-routing, not reduction"; very well handled |
| **GTC type consensus no-op** (w10_type_consensus_prototype × 2) | **YES — partially** | `appendix_beam_search.tex` final paragraph ("type-consensus constraint… 100% skip rate on 551 SciERC and 50 DocRED documents") | Mentioned as confirming beam search mechanism; exp IDs not cited but the finding is attributed |
| **Mistral beam search doesn't reduce DR** (w10_mistral_scierc_beam_551) | **YES** | `appendix_beam_search.tex` §Discussion ("Mistral-7B-v0.3 constitutes a boundary condition…beam search does not reduce DR (13.4%→13.8%)") | Clearly discussed as boundary condition / entity misclassification bottleneck |
| **Full fine-tuning infra failure** (d062_full_ft_scierc) | **NO** | — | Infra failure, not a scientific negative; appropriate to omit |
| **CF majority voting** (d062_cf_majority_voting) | **NOT EXPLICITLY** | `appendix_discussion.tex` mentions TCR as the correct approach and briefly notes naive majority voting "ignores relational constraints and increases DR" but doesn't show data | The data table would strengthen honesty; one line would suffice |
| **Constraint-guided beam penalty** (d068_constraint_guided_beam_pilot) | **NO** | — | No mention anywhere |
| **TCR reranking with beam is no-op** (beam4_tcr_qwen_scierc, tcr_beam4_llama_scierc) | **YES** | `appendix_beam_search.tex` §"TCR reranking under beam search" — last paragraph | Explicitly stated: "0/551 candidates changed" for both models, with interpretation |
| **Grammar-only no-op at 70B** (eval_70b_zs_scierc_grammar_only, eval_70b_lora_scierc_grammar_only, eval_70b_lora_docred_200_grammar_only) | **YES** | `appendix_70b_ablation.tex` — Tables `tab:70b-ft-ablation`, `tab:70b-docred-zs-ablation`; `section5_runtime.tex` §70B | Reported as data; DR increase on DocRED grammar-only explicitly explained |
| **S2 severe F1 degradation at 70B** (eval_70b_lora_docred_200_full_s2, eval_70b_lora_scierc_s2) | **YES** | `appendix_70b_ablation.tex` + `section7_conclusion_compressed.tex` | Explicitly flagged as scale-sensitive behavior and cited as reason to recommend S1 as default; also noted in conclusion |
| **Grammar-only DocRED ZS increases DR** (eval_70b_zs_docred_200_grammar_only) | **YES** | `appendix_70b_ablation.tex` Table `tab:70b-docred-zs-ablation`, explained via RV→DR conversion in high-κ schema | Well-handled |

---

### Summary

**13 of 15 distinct scientific negative results are discussed** (the 2 unmentioned are the majority voting data table and the constraint-guided beam penalty).

**Two gaps worth filling:**

1. **CF majority voting** (`d062_cf_majority_voting`) — the data exists (CF reduced but DR increases in all 8 configs) and would strengthen the existing "naive majority voting is wrong" claim in `appendix_tcr.tex` line 9. Currently that claim is asserted without numbers. One sentence + footnote or a small table would add credibility. **Marginal value: medium** — TCR already covers this ground thoroughly.

2. **Constraint-guided beam penalty** (`d068_constraint_guided_beam_pilot`) — killed early because the LoRA model already had 0% violations, so the penalty never fired. This is an interesting null: it shows that for a well-fine-tuned model, beam search's benefit is purely from exploration diversity, not from explicit violation penalization. One sentence in `appendix_beam_search.tex` could add depth: *"We also piloted explicit violation-penalty beam scoring (score = logP − β×violations); under LoRA, the penalty term is identically zero because beam candidates already have 0% violations, confirming that fine-tuned beam improvement derives from exploration breadth, not constraint pressure."* **Marginal value: low-medium** — adds methodological transparency without being essential.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b88f0399-11ca-4276-8871-279c8ea45a3d",
  "isSidechain": true,
  "agentId": "aa0ebc68a17d43ebd",
  "requestId": "req_011CbKxBehtDB6ATSx5mviUm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21bddbb6-0f50-41f5-8c31-80443e8cf592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01B1Dj93Wsa5ncTjqEnPPa4D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2534,
      "cache_read_input_tokens": 98721,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2534,
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
