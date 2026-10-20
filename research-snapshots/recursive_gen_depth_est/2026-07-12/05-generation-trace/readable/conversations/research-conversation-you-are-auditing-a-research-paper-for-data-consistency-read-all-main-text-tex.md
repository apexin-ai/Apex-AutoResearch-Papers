# Research conversation: You are auditing a research paper for data consistency. Read ALL main text .tex files in /home/ubuntu/.agent-ml-research

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 75
- **Recorded user turns:** 1
- **Tool calls:** 32
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a563e433f634db794.jsonl`
- **Structured JSON:** [`4af81e6fe7d998b95db0.json`](../../sessions/4a/4af81e6fe7d998b95db0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

75 recorded events

### User

_source line 1 · 2026-05-23T10:20:04.279Z_

You are auditing a research paper for data consistency. Read ALL main text .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/ and extract EVERY specific numerical claim (percentages, accuracy numbers, pp differences, AUC values, counts, ratios). For each number, trace it to its source — either an appendix table/section or an experiment artifact file in /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/.

The main text files to scan are:
- abstract.tex
- introduction.tex  
- related.tex
- method.tex (or theory.tex)
- atlas.tex
- generalization.tex
- discussion.tex
- conclusion.tex

For each numerical claim found, report:
1. File:line — the exact location
2. The claim (e.g., "78.4% accuracy")
3. Source found? (appendix table ref, artifact file, or NOT FOUND)
4. Match status: MATCH / MISMATCH / UNVERIFIED

Focus especially on:
- Accuracy percentages
- EDD values
- AUC values
- pp differences
- Feature importance percentages
- Sample counts (180K, 140K, etc.)
- Any ranges (e.g., "59-82%", "4-11 pp")

Report ALL mismatches and unverifiable claims. This is critical for submission.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "1a5203f0-c5cc-40d8-bba1-f1db6ca7d875",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-23T10:20:04.283Z_

```json
{
  "parentUuid": "1a5203f0-c5cc-40d8-bba1-f1db6ca7d875",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
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
      "TodoWrite",
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
  "uuid": "9c13973e-ee9e-44f1-9919-c7ece59e0e48",
  "timestamp": "2026-05-23T10:20:04.283Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

---

### Assistant

_source line 3 · 2026-05-23T10:20:07.467Z_



I'll systematically audit all numerical claims in the paper. Let me start by reading all the main text files and then trace each number to its source.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c13973e-ee9e-44f1-9919-c7ece59e0e48",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLCfhFZjprf9gAg8wAX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c38b443-9aba-4bfb-8a4f-20abb306c30e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DzNcBhpxiQSzjhmwvTrqcM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32930,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32930,
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

_source line 4 · 2026-05-23T10:20:08.588Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0184k2EAXBkJL1QDapjSr24b`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c38b443-9aba-4bfb-8a4f-20abb306c30e",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLCfhFZjprf9gAg8wAX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ac9de07-93df-4bfd-90ee-b26f96002968",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DzNcBhpxiQSzjhmwvTrqcM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32930,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32930,
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

### Tool result

_source line 5 · 2026-05-23T10:20:08.603Z_

<details><summary>↩ Tool result · `toolu_0184k2EAXBkJL1QDapjSr24b`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ac9de07-93df-4bfd-90ee-b26f96002968",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "839e36d3-9a5e-4015-bef5-7805f607c7d6",
  "sourceToolAssistantUUID": "2ac9de07-93df-4bfd-90ee-b26f96002968",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-23T10:20:08.776Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01A4xVRcf79TRGMn4vfA4Kio`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "839e36d3-9a5e-4015-bef5-7805f607c7d6",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLCfhFZjprf9gAg8wAX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08d3a27e-bf0c-49df-a002-ae1b5f329bc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DzNcBhpxiQSzjhmwvTrqcM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32930,
      "cache_read_input_tokens": 0,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 32930
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 219,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 32930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 32930,
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

_source line 7 · 2026-05-23T10:20:08.798Z_

<details><summary>↩ Tool result · `toolu_01A4xVRcf79TRGMn4vfA4Kio`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/logs/phase1_attempt0.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/logs/phase2_best_attempt0.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/logs/phase2_median_attempt0.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/logs/phase2_worst_attempt0.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/best/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/best/paper.aux
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/best/paper.out
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/best/paper.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/logs/paper_agent_best.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/paper.aux
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/paper.out
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/paper.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/logs/paper_agent_median.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/worst/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/worst/paper.aux
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/worst/paper.out
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/worst/paper.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/logs/paper_agent_worst.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/logs/orchestrator.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/logs/review_best.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/logs/review_median.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/best/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/worst/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/logs/review_worst.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/eval_d1d3.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/intermediate/atlas_analysis_readme.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/intermediate/dcol_feature_based_readme.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/intermediate/dcol_e2e_deberta_readme.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/intermediate/baseline_battery_readme.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/baseline_unified_comparison.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dcol_code/dcol_model.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dcol_code/dcol_loss.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dcol_code/dcol_dataset.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dcol_code/train_dcol.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dcol_code/eval_dcol.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/intermediate/dcol_e2e_v2_readme.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/report/diveye_citation_audit.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/diveye_citation_audit.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/monotonicity_scores.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/edd_matrix.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/heatmap_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/feature_consistency.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dcol_feature_mlp.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/baseline_perplexity_regression.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/baseline_diveye.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/baseline_zero_shot_llm.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/pythia_topk50_001/report/pythia_topk50_001_analysis.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/pythia_topk50_001/report/pythia_topk50_001_analysis_ddde61.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/feature_importance_consistency_analysis.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dcol_deberta_002/report/dcol_002_oom_diagnosis.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dcol_002_oom_diagnosis.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/baselines.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/olmo_temp09_001/analysis_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/atlas_v1_analysis/data/atlas_v2_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/atlas/atlas_v2_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/matrix_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/atlas_v2/matrix_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/intermediate/atlas_v2.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/atlas_v2/monotonicity_scores.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/atlas_v2/edd_analysis.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/cross_model_heatmap.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/atlas_v2/cross_model_heatmap.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/atlas_v2/feature_trajectory_summary.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/atlas_v2/jaccard_matrix.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/report/literature_scan_20260515.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/literature_scan_20260515.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/report/matrix_3x3_analysis.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/matrix_3x3_analysis.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/atlas_v1_analysis/data/atlas_v2_manifest.txt
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/report/atlas_v2_summary.txt
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/edd_sensitivity_summary.txt
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/report/matrix_3x3_analysis_fbd741.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/report/atlas_v2_9cells_summary.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/atlas_v2_data_9cells_index.txt
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/edd_threshold_sensitivity.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/edd_threshold_sensitivity.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/plot_atlas_figures.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/cross_strategy_loo_results.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/cross_model_loo_v1/data/cross_model_loo_results.txt
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/chart/fig1_auc_decay.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/chart/fig3_confusion_matrix.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/chart/fig4_atlas_heatmap.png
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08d3a27e-bf0c-49df-a002-ae1b5f329bc4",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "ce41b8eb-f309-4347-8c95-31d42b5511b9",
  "sourceToolAssistantUUID": "08d3a27e-bf0c-49df-a002-ae1b5f329bc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-23T10:20:11.607Z_

Now let me read all main text .tex files and the key artifact data files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce41b8eb-f309-4347-8c95-31d42b5511b9",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLD1Hida42gbXvgnXEx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc602b04-f3f5-43cc-88b1-d8910fe4e61d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8gHCTQUqVKHJo2wNsoVjd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6447,
      "cache_read_input_tokens": 32930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6447,
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

_source line 9 · 2026-05-23T10:20:12.644Z_

<details open><summary>🔧 Tool call — Read · `toolu_015g2L6DL6vMu2yqGMLEfaDW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc602b04-f3f5-43cc-88b1-d8910fe4e61d",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLD1Hida42gbXvgnXEx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7aa558a0-1e9a-48fc-ae7d-9c86988c7012",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8gHCTQUqVKHJo2wNsoVjd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6447,
      "cache_read_input_tokens": 32930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6447,
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

### Tool result

_source line 10 · 2026-05-23T10:20:12.672Z_

<details><summary>↩ Tool result · `toolu_015g2L6DL6vMu2yqGMLEfaDW`</summary>

```text
1	\begin{abstract}
2	As language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K cell-instances (140K unique passages) spanning three model families, three decoding strategies, and four depths under controlled full-replacement chains at the 1--1.5B parameter scale.
4	A lightweight pipeline (19 statistical features classified by Random Forest) achieves d1--d3 balanced accuracy of 59--82\% across nine model--strategy cells, with $\mathrm{EDD}_{0.70} = 3$ in 8/9 cells.
5	Three findings emerge: (1)~depth signal concentrates in perplexity distribution tails, corroborated by classifier convergence and independent cross-perplexity features; (2)~decoding strategy affects cross-condition transfer more than model architecture, suggesting structurally distinct degradation trajectories; (3)~signal attenuates with scale (14B cross-reference accuracy ${\sim}44$\%, $\mathrm{EDD}_{0.70}{=}2$ for nucleus and temperature, 0 for top-$k$), with reference-model choice shifting accuracy by ${\sim}7$\,pp and altering EDD, indicating it is a major confound in cross-scale comparisons.
6	Our depth estimation claims hold most strongly within-strategy or when the decoding configuration is known; a two-stage routing pipeline recovers $+$11.5\,pp under cross-strategy transfer.
7	Perturbation-based and membership-inference baselines lack ordinal depth resolution, confirming that depth estimation requires distributional statistics beyond binary detection scores.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7aa558a0-1e9a-48fc-ae7d-9c86988c7012",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "c20e66bd-dfa0-4742-b97a-06dd43214a69",
  "sourceToolAssistantUUID": "7aa558a0-1e9a-48fc-ae7d-9c86988c7012",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T10:20:13.152Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PM54VhL4wEzvCbQaf7yj7z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c20e66bd-dfa0-4742-b97a-06dd43214a69",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLD1Hida42gbXvgnXEx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "efc7cdc9-d9d9-4beb-8149-34ccefe23d1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8gHCTQUqVKHJo2wNsoVjd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6447,
      "cache_read_input_tokens": 32930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6447,
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

### Tool result

_source line 12 · 2026-05-23T10:20:13.165Z_

<details><summary>↩ Tool result · `toolu_01PM54VhL4wEzvCbQaf7yj7z`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet whether the recursive generation depth of a text can be estimated from its statistical properties remains unstudied, a question that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	We focus on the 1--1.5B parameter regime under \emph{controlled full-replacement chains}, where each generation fully replaces the prior training set, isolating the depth variable. Real-world contamination involves partial mixing at unknown proportions; full replacement provides an upper bound on depth signal strength (\S\ref{sec:discussion}).
8	
9	Existing tools address adjacent but distinct problems.
10	Binary detectors \cite{binoculars2024,fast_detectgpt2024,diveye2026} collapse all depths $d \geq 1$ into a single category, a limitation we confirm empirically: their pairwise d1-vs-d2 AUC collapses to chance level (\S\ref{sec:gen:baselines}); watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding.
11	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
12	No existing method estimates the ordinal recursive generation depth of a text passage from its content alone (Figure~\ref{fig:problem}).
13	
14	We find that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are \textbf{consistent in direction but scale-dependent in magnitude} across the three model families and three decoding strategies studied.
15	Specifically, the perplexity tail feature family (\texttt{p90\_ppl}, \texttt{p75\_ppl}, \texttt{kurtosis\_ppl}) and surprisal variance emerge as dominant depth indicators, with group-level dominance robust across all 9 model--strategy configurations and three importance measures.
16	Our contribution centers on task formalization and systematic empirical characterization; the convergence of four classifiers within 0.8\,pp (\S\ref{sec:gen:baselines}) confirms that signal resides in feature design, not classifier architecture.
17	We formalize recursive generation depth estimation as ordinal classification and find that a lightweight pipeline suffices: compute 19 reference-model statistical features (effective dimensionality ${\approx}$4--5 due to multicollinearity; \S\ref{sec:atlas:features}) and classify with a Random Forest into $K{+}1$ depth classes.
18	To characterize how recursive generation reshapes these features, we construct the \emph{Depth Degradation Atlas}: a $3 \times 3$ grid of model families $\times$ decoding strategies spanning 4 depths (180K cell-instances).
19	The atlas reveals strategy-dependent degradation trajectories; we introduce \emph{Effective Discriminable Depth} (EDD) to quantify how far into the recursion chain adjacent depths remain distinguishable.
20	
21	\begin{figure*}[t]
22	\centering
23	\includegraphics[width=0.68\textwidth]{figures/fig_problem_illustration.pdf}
24	\caption{Recursive generation depth estimation. A seed corpus $\mathcal{D}_0$ feeds a LoRA finetuning--sampling loop producing successively deeper corpora. Given a passage~$x$, the task is to estimate its ordinal depth~$d$.}
25	\label{fig:problem}
26	\end{figure*}
27	Our contributions are:
28	\begin{itemize}[nosep,leftmargin=*]
29	    \item \textbf{Task formalization and metric.} We define recursive generation depth estimation as ordinal classification, introduce the \emph{Effective Discriminable Depth} (EDD) metric, and construct a 180K cell-instance benchmark ($3$ model families $\times$ $3$ decoding strategies $\times$ $4$ depths; 140K unique passages).
30	
31	    \item \textbf{Depth Degradation Atlas.} The perplexity tail feature family and surprisal variance jointly dominate depth discrimination across all 9 cells; $\mathrm{EDD}_{0.70}{=}3$ in 8/9 cells (4 under nucleus depth extension), validated by 5-class extension (71--81\%); feature group ablation confirms perplexity tail dominance (76.6\% alone vs.\ 78.4\% full set).
32	
33	    \item \textbf{Partial-mixing validation.} Under 25--50\% synthetic mixing, $\mathrm{EDD}_{0.70}{=}3$ is preserved in 5/6 cells with $-$8--15\,pp accuracy attenuation.
34	
35	    \item \textbf{Generalization boundaries.} Within the tested 1--1.5B regime, cross-model transfer reaches 66.4\% and cross-domain (arXiv) 74.1\%; at 14B, cross-reference $\mathrm{EDD}_{0.70}{=}2$; cross-strategy (d1--d3: 45.9\%) is a boundary condition, partially recovered by two-stage routing ($+$11.5\,pp).
36	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efc7cdc9-d9d9-4beb-8149-34ccefe23d1b",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "f37f879d-5da2-46cd-9665-6502158b8bb8",
  "sourceToolAssistantUUID": "efc7cdc9-d9d9-4beb-8149-34ccefe23d1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T10:20:13.601Z_

<details open><summary>🔧 Tool call — Read · `toolu_017aAnLRpQBnSsyWLgsqmuY8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f37f879d-5da2-46cd-9665-6502158b8bb8",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLD1Hida42gbXvgnXEx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84c77a95-c60c-4274-9e49-7d27269909ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8gHCTQUqVKHJo2wNsoVjd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6447,
      "cache_read_input_tokens": 32930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6447,
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

### Tool result

_source line 14 · 2026-05-23T10:20:13.608Z_

<details><summary>↩ Tool result · `toolu_017aAnLRpQBnSsyWLgsqmuY8`</summary>

```text
1	\subsection{Theoretical Motivation}
2	\label{sec:method:theory}
3	
4	Recursive generation contracts the support of the learned distribution, with low-probability tokens lost first \cite{shumailov2024_nature}: tail mass $P_k(\mathrm{ppl} > t)$ decreases monotonically in depth $k$.
5	This tail erosion predicts the perplexity tail feature family as a depth marker, confirmed jointly with surprisal variance across all 9 cells (\S\ref{sec:atlas:features}).
6	Surprisal variance captures complementary distributional narrowing: as the support contracts, per-token surprise becomes more predictable.
7	
8	\paragraph{EDD upper bound.}
9	Tail mass at depth $k$ scales as $\alpha^k$ for a contraction factor $\alpha \in (0,1)$ \cite{dohmatob2024_tale_of_tails}; EDD reaches its upper bound when adjacent-depth feature distance falls below classifier resolution.
10	Our empirical AUC-excess contraction (ratio 0.80 at d1v2$\to$d2v3, 0.69 at d3v4$\to$d4v5; \S\ref{sec:atlas:edd}) is consistent with geometric decay approaching a fixed point \cite{bertrand2024_stability}.
11	5-class extensions to d4 (71--81\%, chance = 20\%; Appendix~\ref{app:depth4_ext}) confirm depth~4 discriminability; mean perplexity saturates before tail statistics, placing a physical ceiling on EDD.
12	
13	\paragraph{Scale-dependent attenuation.}
14	Larger models approximate the training distribution more faithfully per step ($\alpha$ closer to 1), predicting weaker per-step signal.
15	Qwen2.5-14B supports this: d0-vs-d1 AUC drops to 0.643 (vs.\ ${>}0.99$ at 1--1.5B; \S\ref{sec:gen:crossscale}); 7--8B results are mixed, suggesting additional confounds interact with the scale effect (Appendix~\ref{app:cross_scale_full}).
16	
17	\paragraph{Strategy-dependent convergence.}
18	The contraction rate $\alpha$ varies with decoding strategy.
19	Temperature scaling ($\tau < 1$) sharpens the logit distribution uniformly and accelerates convergence to the mode; temperature depth-$d$ text should therefore resemble nucleus depth-$(d{+}1)$ text in tail statistics.
20	GPT-2~XL confirms this: temperature d1 median \texttt{p90\_ppl} (92.2) matches the nucleus d2 median (92.3).
21	Top-$k$ truncation removes the low-probability tokens that carry depth signal, predicting weaker discriminability; top-$k$ cells yield the lowest accuracy (68.9--75.8\%) across the atlas (\S\ref{sec:atlas:strategy}).
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84c77a95-c60c-4274-9e49-7d27269909ca",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "e8d4c829-389e-49bc-b132-a536bce327c4",
  "sourceToolAssistantUUID": "84c77a95-c60c-4274-9e49-7d27269909ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T10:20:14.074Z_

<details open><summary>🔧 Tool call — Read · `toolu_017RCEgqpo1ELxiUEDL4AeLz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8d4c829-389e-49bc-b132-a536bce327c4",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLD1Hida42gbXvgnXEx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa347732-4375-44ec-a8f6-b5e73ab93d34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8gHCTQUqVKHJo2wNsoVjd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6447,
      "cache_read_input_tokens": 32930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6447,
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

### Tool result

_source line 16 · 2026-05-23T10:20:14.081Z_

<details><summary>↩ Tool result · `toolu_017RCEgqpo1ELxiUEDL4AeLz`</summary>

```text
1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells at the 1--1.5B parameter scale, evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 68.9\% (Pythia, top-$k$) to 85.9\% (GPT-2~XL, temperature) four-class (d1--d3 balanced: 58.9--81.5\%), all exceeding the 25\%/33\% chance baselines.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (75.8--85.9\%), followed by OLMo (74.4--82.3\%) and Pythia (68.9--78.7\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 9.3~pp, comparable to the 7.2~pp mean within-strategy model gap; decoding strategy contributes at least as much as model family to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) with bootstrap 95\% CI (${\pm}$half-width; $B{=}10{,}000$). RF with 200 trees, evaluated via 5-fold stratified CV (seed=42). Parenthesized: d1--d3 balanced accuracy from the same 4-class RF (chance = 25\% / 33\%). Depth-0 recall exceeds 97\% in all cells. Within-distribution ordinal quality: mean absolute error (MAE)\,=\,0.23, QWK\,=\,0.89 (QWK$_{\text{d1--d3}}$\,=\,0.74); 98.2\% of errors fall on adjacent depths ($|\Delta| \leq 1$). $^\dagger$Self-reference scoring (Pythia-1.4B is both generator and reference model); 4--11\,pp advantage over cross-model references (Appendix~\ref{app:ref_ablation}). Cross-cell comparisons involving Pythia should be interpreted with this caveat.}
22	\label{tab:main_matrix}
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}lccc@{}}
25	\toprule
26	& Nucleus & Temp.\ $\tau{=}0.9$ & Top-$k$ \\
27	\midrule
28	Pythia-1.4B$^\dagger$  & 78.7{\scriptsize$\pm$0.5}\,(71.8) & 76.8{\scriptsize$\pm$0.5}\,(69.3) & 68.9{\scriptsize$\pm$0.6}\,(58.9) \\
29	OLMo-1B     & 78.9{\scriptsize$\pm$0.5}\,(72.7) & 82.3{\scriptsize$\pm$0.5}\,(76.6) & 74.4{\scriptsize$\pm$0.5}\,(66.2) \\
30	GPT-2~XL    & \textbf{84.3}{\scriptsize$\pm$0.5}\,(79.6) & \textbf{85.9}{\scriptsize$\pm$0.5}\,(81.5) & \textbf{75.8}{\scriptsize$\pm$0.6}\,(68.1) \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	
35	\paragraph{Per-class recall.}
36	Depth-0 recall exceeds 97\% in all 9 cells.
37	Among generated depths, d2 consistently yields the lowest recall (44--73\%), reflecting its position at the center of the depth gradient where features overlap with both d1 and d3, consistent with d2-vs-d3 as the EDD bottleneck (\S\ref{sec:atlas:edd}; full per-class recall in Appendix~\ref{app:per_class}).
38	
39	%% ----------------------------------------------------------------
40	\subsection{Feature Consistency Across the Grid}
41	\label{sec:atlas:features}
42	
43	Multicollinearity is substantial (VIF${>}$10 for 14--16 of 19 features); importance rankings below indicate feature \emph{family} contributions rather than individual effects; permutation importance (Appendix~\ref{app:permutation}) partially mitigates collinearity bias \cite{strobl2008_conditional,hooker2021_permutation}.
44	Despite the 17.1~pp accuracy spread across cells, the perplexity tail statistics family (\texttt{p90\_ppl}, \texttt{p75\_ppl}, \texttt{kurtosis\_ppl}) and surprisal variance (\texttt{var\_surprisal}) dominate depth discrimination in every setting.
45	Within this family, \texttt{p90\_ppl} and \texttt{var\_surprisal} are consistently prominent, though individual rankings should be interpreted cautiously given VIF${>}$10; group-level ablation (\S\ref{sec:atlas:features}, below) provides the collinearity-robust confirmation.\footnote{The group-level dominance of perplexity tail statistics is robust across importance measures (Gini, SHAP, permutation; Kendall's $W{=}0.90$, $p{<}0.005$).}
46	Conditional permutation importance \citep{strobl2008_conditional} confirms \texttt{var\_surprisal} and \texttt{p90\_ppl} as top-2 in 8/9 cells (bootstrap rank 1.4 and 1.7), consistent with Gini rankings (Appendix~\ref{app:conditional_pi}).
47	Table~\ref{tab:feature_importance} shows the full per-cell ranking; Figure~\ref{fig:atlas_heatmap} visualizes the importance landscape across all nine cells.
48	
49	Cross-model feature-rank Spearman correlation averages $\bar{\rho} = 0.868$ ($[0.619, 0.954]$): models agree on which features carry depth information despite differing in absolute accuracy.
50	Top-$k$ yields the highest cross-model rank correlation ($\rho = 0.811$), as vocabulary truncation imposes a more uniform feature landscape at the cost of weaker signal (\S\ref{sec:atlas:strategy}).
51	
52	Feature ablation confirms this concentration: the top-5 features achieve 97.6\% of full accuracy (76.5\% vs.\ 78.4\%); in-distribution group-level ablation shows perplexity features alone reach 76.6\%, surprisal 73.2\%, lexical diversity ${\leq}$47\%, and repetition ${\leq}$44\% (Appendix~\ref{app:feature_ablation}).\footnote{Best single feature (\texttt{p90\_ppl}) achieves 58.3\%, providing a more competitive single-feature baseline than mean perplexity (25.1\%).}
53	
54	The feature hierarchy shifts with depth.
55	At shallow boundaries (d1 vs.\ d2), \texttt{var\_surprisal} dominates importance; at deeper boundaries (d3 vs.\ d4, d4 vs.\ d5), tail perplexity statistics (\texttt{p90\_ppl}, \texttt{kurtosis\_ppl}) take over.
56	This transition aligns with model-collapse dynamics~\cite{shumailov2024_nature}: early recursion narrows the surprisal distribution (captured by its variance), while later steps erode the perplexity tail (captured by upper quantiles and kurtosis).
57	
58	\begin{table}[t]
59	\centering
60	\small
61	\caption{Top-5 features by Gini importance. \textbf{Bold}: top-2. \texttt{p90\_ppl} top-2 in 9/9; \texttt{var\_surprisal} 8/9 under SHAP (7/9 under Gini). Individual rankings are approximate due to multicollinearity (VIF${>}$10 for 14--16/19 features).}
62	\label{tab:feature_importance}
63	\resizebox{\columnwidth}{!}{%
64	\begin{tabular}{@{}l l@{}}
65	\toprule
66	Cell & Top-5 features (Gini importance, ranked) \\
67	\midrule
68	Pythia, nuc.       & \textbf{var\_surprisal\,(.17)}, \textbf{p90\_ppl\,(.15)}, mean\_ppl\,(.11), var\_ppl\,(.08), p75\_ppl\,(.07) \\
69	Pythia, $\tau$     & \textbf{var\_surprisal\,(.17)}, \textbf{p90\_ppl\,(.14)}, mean\_ppl\,(.11), p75\_ppl\,(.07), mean\_surprisal\,(.07) \\
70	Pythia, top-$k$    & \textbf{var\_surprisal\,(.16)}, \textbf{p90\_ppl\,(.12)}, mean\_ppl\,(.11), var\_ppl\,(.07), mean\_surprisal\,(.06) \\
71	GPT-2\,XL, nuc.    & \textbf{var\_surprisal\,(.21)}, \textbf{p90\_ppl\,(.21)}, p75\_ppl\,(.10), mean\_surprisal\,(.07), mean\_ppl\,(.06) \\
72	GPT-2\,XL, $\tau$  & \textbf{p90\_ppl\,(.25)}, \textbf{p75\_ppl\,(.15)}, mean\_surprisal\,(.13), var\_surprisal\,(.12), p50\_ppl\,(.05) \\
73	GPT-2\,XL, top-$k$ & \textbf{p90\_ppl\,(.24)}, \textbf{p75\_ppl\,(.12)}, var\_surprisal\,(.10), mean\_surprisal\,(.09), type\_token\_ratio\,(.04) \\
74	OLMo, nuc.         & \textbf{p90\_ppl\,(.18)}, \textbf{var\_surprisal\,(.15)}, p75\_ppl\,(.11), mean\_surprisal\,(.07), type\_token\_ratio\,(.06) \\
75	OLMo, $\tau$       & \textbf{p90\_ppl\,(.21)}, \textbf{var\_surprisal\,(.16)}, p75\_ppl\,(.12), mean\_surprisal\,(.09), type\_token\_ratio\,(.05) \\
76	OLMo, top-$k$      & \textbf{p90\_ppl\,(.20)}, \textbf{var\_surprisal\,(.17)}, p75\_ppl\,(.10), mean\_surprisal\,(.07), mean\_ppl\,(.05) \\
77	\bottomrule
78	\end{tabular}}
79	\end{table}
80	
81	\begin{figure}[t]
82	\centering
83	\includegraphics[width=\columnwidth]{figures/fig_atlas_heatmap.pdf}
84	\caption{Atlas feature importance heatmap for the top-7 features. Rows: features ranked by mean Gini importance; columns: 9 model--strategy cells. Stars mark the two universal top-2 features (\texttt{p90\_ppl}, \texttt{var\_surprisal}). Feature group ablation in Appendix~\ref{app:feature_ablation}.}
85	\label{fig:atlas_heatmap}
86	\end{figure}
87	
88	%% ----------------------------------------------------------------
89	\subsection{EDD Analysis}
90	\label{sec:atlas:edd}
91	\label{sec:atlas:monotonicity}
92	
93	Depth features exhibit strong monotonic trends (Spearman $\rho = -1.0$ for perplexity tail statistics; Figure~\ref{fig:feature_trajectory}); inter-depth distances are non-uniform (d0-vs-d1 AUC ${>}$0.99 in all 9 cells, d2-vs-d3: 0.69--0.89).
94	
95	We extend the benchmark to depth $d{=}5$ for all three models under nucleus sampling.
96	Each model's depth-3 LoRA checkpoint is used to finetune and generate depth-4 data, and the process repeats for depth~5; feature extraction uses the same reference model (Pythia-1.4B).
97	We train dedicated binary RF classifiers (500 trees) for each adjacent pair, as defined in Eq.~\ref{eq:edd}.
98	
99	\paragraph{AUC decay and cross-model convergence.}
100	For Pythia-1.4B (nucleus), AUC decays monotonically from $0.999$ (d0v1) to $0.683$ (d4v5); AUC-excess contraction ratios (0.80 at d1v2$\to$d2v3, 0.69 at d3v4$\to$d4v5) show convergence toward indistinguishability accelerates with depth (Figure~\ref{fig:auc_decay}).
101	The d3-vs-d4 AUC clusters near $T{=}0.75$ for all three models (Pythia $0.784$, OLMo $0.765$, GPT-2~XL $0.750$), while d4-vs-d5 converges to a narrow band ($0.681$--$0.684$, range $0.003$), suggesting an architecture-independent depth ceiling within the 1--1.5B nucleus setting.
102	Bootstrap testing ($H_0{:}\, \mathrm{AUC} \leq 0.75$; Bonferroni-corrected for 3 comparisons, $\alpha{=}0.0167$) yields $p = 0.001$ (Pythia), $0.091$ (OLMo), $0.505$ (GPT-2~XL).
103	
104	\paragraph{EDD threshold sensitivity.}
105	Across the 9-cell benchmark (depths 0--3), all cells achieve $\mathrm{EDD}{=}3$ at $T{=}0.65$; at $T{=}0.70$, 8/9 cells; at $T{=}0.75$, 7/9; at $T{=}0.80$, 5/9.
106	Top-$k$ configurations lose $\mathrm{EDD}{=}3$ first (Pythia top-$k$ at $T{=}0.70$, OLMo top-$k$ at $T{=}0.75$); d2-vs-d3 is the consistent bottleneck.
107	
108	\begin{figure}[t]
109	\centering
110	\includegraphics[width=\columnwidth]{figures/fig_auc_decay.pdf}
111	\caption{AUC decay curves for Pythia-1.4B (nucleus, depths 0--5) under three pipeline configurations: binary pairwise RF, 4-class RF, and 6-class RF. Horizontal dashed lines mark $T \in \{0.65, 0.70, 0.75, 0.80\}$. All curves converge below 0.70 at d4-vs-d5. Shaded bands: bootstrap 95\% CIs.}
112	\label{fig:auc_decay}
113	\end{figure}
114	
115	%% ----------------------------------------------------------------
116	\subsection{Strategy-Dependent Trajectories}
117	\label{sec:atlas:strategy}
118	
119	The three strategies induce qualitatively distinct degradation trajectories.
120	Temperature ($\tau{=}0.9$) yields the highest accuracy in 2/3 models (GPT-2~XL 85.9\%, OLMo 82.3\%) because uniform logit scaling accelerates convergence to an attractor~\cite{shumailov2024_nature}, amplifying the fingerprint but creating a boundary reversal risk under cross-strategy transfer (\S\ref{sec:generalization}).
121	Top-$k$ ($k{=}50$) produces the lowest accuracy (68.9--75.8\%) because hard vocabulary truncation removes depth-discriminative low-probability tokens.
122	The strategy effect (9.3\,pp range) exceeds the model effect (7.2\,pp); deployment-time knowledge of the decoding strategy matters at least as much as the generator model.
123	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa347732-4375-44ec-a8f6-b5e73ab93d34",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "b77d8a44-ac0e-4e3c-a580-066d301e6f65",
  "sourceToolAssistantUUID": "fa347732-4375-44ec-a8f6-b5e73ab93d34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T10:20:15.033Z_

<details open><summary>🔧 Tool call — Read · `toolu_01My3vW5UmbH6p3ReDMFu9zC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b77d8a44-ac0e-4e3c-a580-066d301e6f65",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLD1Hida42gbXvgnXEx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25f63328-7f25-42a5-8474-fc07a69f097a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8gHCTQUqVKHJo2wNsoVjd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6447,
      "cache_read_input_tokens": 32930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6447,
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

### Tool result

_source line 18 · 2026-05-23T10:20:15.040Z_

<details><summary>↩ Tool result · `toolu_01My3vW5UmbH6p3ReDMFu9zC`</summary>

```text
1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether atlas accuracy (68.9--85.9\% four-class; d1--d3: 58.9--81.5\%) reflects genuine statistical regularities across eight generalization axes (five below, three in Appendix).
5	
6	\subsection{Classifier Comparison and Surface-Text Ablation}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} compares methods across all 9 cells.
10	Four classifiers (RF, XGBoost, ordinal MLP, prototypical) converge within 0.8\,pp under cross-model transfer (Appendix~\ref{app:learned_estimator}), confirming a feature-determined accuracy ceiling.
11	
12	\paragraph{Neural end-to-end baselines.}
13	DeBERTa-v3-base (LoRA, 53--61\%) and RoBERTa-DCOL (ordinal contrastive, 64.5\%) lag RF by 14--33\,pp; note that RF features access reference-model log-probabilities unavailable to end-to-end PLM baselines (\S\ref{sec:discussion}).
14	
15	\paragraph{Binary detectors and membership inference.}
16	Perturbation-based (DetectGPT, 28.8\%) and membership-inference (Min-K\% Prob, 33.2\%) methods produce scores with no ordinal resolution (Table~\ref{tab:baselines}); Binoculars d1v2 AUC\,=\,0.50--0.53 vs.\ RF 0.93 (Appendix~\ref{app:detector_baselines}). Binoculars convergence with our pipeline is discussed in \S\ref{sec:discussion}.
17	
18	\paragraph{Surface-text ablation.}
19	Single-feature regression on mean perplexity (25.1\%) and zero-shot LLMs (best 36.2\%; Appendix~\ref{app:zeroshot_prompt}) confirm depth signal is inaccessible from surface text.
20	
21	\begin{table}[t]
22	\centering
23	\small
24	\caption{Method comparison (RF mean across 9 cells, 5-fold CV). Chance = 25\% / 33.3\% (d1--d3). $^\dagger$Adapted from binary detection; Binoculars 11-feat: $p{>}0.05$ vs.\ 19-feat RF (paired permutation test).}
25	\label{tab:baselines}
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{@{}llcc@{}}
28	\toprule
29	Method & Calibration & 4-Cl (\%) & d1--d3 (\%) \\
30	\midrule
31	RF 19-feature (ours) & RF & 78.4 & \textbf{71.6} \\
32	Binoculars$^\dagger$ \cite{binoculars2024} & RF (11 feat) & 78.1 & --- \\
33	Merged (30 feat)$^\dagger$ & RF & \textbf{82.6} & --- \\
34	Binoculars \cite{binoculars2024} & threshold & 69.8 & --- \\
35	Binoculars \cite{binoculars2024} & RF (1 feat) & 63.7 & --- \\
36	RoBERTa-DCOL (ordinal) & contrastive & 64.5 & --- \\
37	DeBERTa-v3 (end-to-end) & cross-entropy & 53.1--60.6 & --- \\
38	\midrule
39	Zero-shot LLM (best) & --- & 36.2 & --- \\
40	Min-K\% Prob \cite{shi2024_minkprob} & CORAL & 33.2 & 40.4 \\
41	DetectGPT \cite{mitchell2023_detectgpt} & best-of-3 & 28.8 & 24.3 \\
42	Random & --- & 25.0 & 33.3 \\
43	\bottomrule
44	\end{tabular}}
45	\end{table}
46	
47	\subsection{Cross-Model Transfer}
48	\label{sec:gen:crossmodel}
49	
50	\begin{table}[t]
51	\centering
52	\small
53	\caption{Cross-model transfer (leave-one-out, nucleus only). Chance = 25\% / 33\% (d1--d3). d1--d3 mean 55.4\%; QWK\,=\,0.81; 94.8\% errors at $|\Delta| \leq 1$.}
54	\label{tab:cross_model}
55	\begin{tabular}{lccccc}
56	\toprule
57	Holdout & Acc & d0 & d1 & d2 & d3 \\
58	 & (\%) & Rec. & Rec. & Rec. & Rec. \\
59	\midrule
60	Pythia & 62.4 & 100.0 & 49.3 & 26.8 & 73.6 \\
61	OLMo & \textbf{69.2} & 99.3 & 75.5 & 43.3 & 58.8 \\
62	GPT-2 XL & 67.6 & 98.5 & 74.7 & 52.6 & 44.5 \\
63	\midrule
64	Mean & 66.4 & 99.3 & 66.5 & 40.9 & 59.0 \\
65	\bottomrule
66	\end{tabular}
67	\end{table}
68	
69	Mean transfer accuracy is 66.4\% (Table~\ref{tab:cross_model}; d1--d3: 55.4\%, $2.7{\times}$ chance); d2 worst case 26.8\% (Pythia holdout; confusion matrices in Figure~\ref{fig:confusion_matrix}).
70	
71	\subsection{Cross-Strategy Transfer}
72	\label{sec:gen:crossstrategy}
73	
74	Cross-strategy transfer reveals a structural barrier: d1--d3 balanced accuracy drops to 45.9\% (four-class: 59.1\%), 7\,pp below cross-model transfer (Table~\ref{tab:cross_strategy}).
75	A two-stage pipeline (strategy classifier $\to$ depth classifier) recovers much of this gap (70.5\%, $+$11.5\,pp; oracle: 78.3\%; Appendix~\ref{app:extended_discussion}).
76	Our depth estimation claims hold most strongly within-strategy or when the decoding configuration is known.
77	
78	%% ----------------------------------------------------------------
79	\subsection{Preliminary Cross-Scale Observations (14B)}
80	\label{sec:gen:crossscale}
81	
82	At 14B (Qwen2.5-14B), self-reference yields 50.8\% ($2{\times}$ chance, $\mathrm{EDD}_{0.70}{=}0$); switching to cross-reference (Pythia-1.4B) shifts accuracy by $-$6.8\,pp to 44.1\% but raises $\mathrm{EDD}_{0.70}$ to 2 for nucleus and temperature, indicating that reference-model choice is a major confound in cross-scale comparisons (Appendix~\ref{app:cross_scale_full}).
83	Cross-domain transfer to arXiv abstracts reaches 74.1\% (Appendix~\ref{app:domain_bias}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25f63328-7f25-42a5-8474-fc07a69f097a",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "12e61efa-527c-4d13-a772-6a7d58c3423a",
  "sourceToolAssistantUUID": "25f63328-7f25-42a5-8474-fc07a69f097a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T10:20:15.520Z_

<details open><summary>🔧 Tool call — Read · `toolu_019KyuVLrvV6G83zZMcnrwak`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12e61efa-527c-4d13-a772-6a7d58c3423a",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLD1Hida42gbXvgnXEx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5db24654-5770-4327-8d97-d4b40c37ce88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8gHCTQUqVKHJo2wNsoVjd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6447,
      "cache_read_input_tokens": 32930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6447,
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

### Tool result

_source line 20 · 2026-05-23T10:20:15.533Z_

<details><summary>↩ Tool result · `toolu_019KyuVLrvV6G83zZMcnrwak`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	\paragraph{Multi-channel depth encoding.}
5	Four importance measures (Gini, SHAP, permutation, CPI; Kendall's $W{=}0.90$) converge on the same feature ranking, and Binoculars-derived features independently reach 78.1\%, not statistically distinguishable from 78.4\% (permutation $p{>}0.05$; merged: 82.6\%).
6	Depth signal is a distributional property encoded across multiple statistical channels; CORAL ordinal regression yields only marginal improvement (+0.3\,pp, Appendix~\ref{app:learned_estimator}), confirming ordinal structure is captured by the feature space rather than requiring specialized loss functions.
7	
8	\paragraph{Why neural methods underperform.}
9	End-to-end classifiers (DeBERTa, RoBERTa-DCOL) lag RF by 14--33\,pp (\S\ref{sec:gen:baselines}) despite full token-level context, confirming that depth is encoded in distributional tail statistics that pretrained representations do not capture (d2 recall as low as 8\%); targeted feature engineering is necessary, not merely convenient.
10	
11	\paragraph{Feature hierarchy across depths.}
12	The importance transition from \texttt{var\_surprisal} at shallow boundaries to perplexity tail statistics at deeper ones (\S\ref{sec:atlas:features}) mirrors tail-contraction dynamics: early recursion narrows the surprisal distribution while later steps erode the perplexity tail, consistent with geometric contraction (\S\ref{sec:method:theory}).
13	
14	\paragraph{Deployment considerations.}
15	The strategy effect (9.3\,pp) exceeding the model effect (7.2\,pp) requires auditing pipelines to condition on decoding configuration (\S\ref{sec:gen:crossstrategy}), echoing \citet{schaeffer2025}.
16	Similarly, the pipeline relies on a fixed reference model (12/19 features from reference perplexity), with cross-architecture alternatives degrading by 4--11\,pp (Appendix~\ref{app:ref_ablation}); accuracy attenuation at 14B (\S\ref{sec:gen:crossscale}) may be partially recoverable via scale-matched references.
17	A self-reference probe at 7B (52.1\%, $\mathrm{EDD}_{0.70}{=}0$; Appendix~\ref{app:qwen7b_selfref}) falls 8\,pp below the cross-reference baseline (60.1\%), revealing a self-reference ceiling; cross-model references may be necessary above ${\sim}$7B.
18	
19	\paragraph{Accumulation and outlook.}
20	Depth estimation bridges binary detection and model collapse research by providing ordinal resolution \cite{drayson2025_detection_prevents_collapse}.
21	Accumulation experiments at 25--50\% synthetic mixing (Appendix~\ref{app:accumulation_auc}) partially validate depth estimation under realistic conditions: $\mathrm{EDD}_{0.70}{=}3$ is preserved in 5/6 cells.
22	Cross-boundary chains (A$\to$B$\to$C) maintain 84.8\% accuracy (Appendix~\ref{app:cross_boundary}), suggesting depth signal is process-level rather than generator-specific.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5db24654-5770-4327-8d97-d4b40c37ce88",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "8343a151-1b3c-4fc4-a470-f0e791bccf1b",
  "sourceToolAssistantUUID": "5db24654-5770-4327-8d97-d4b40c37ce88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T10:20:15.960Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L4gEw1KEwnYtU3VGHvJLnu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8343a151-1b3c-4fc4-a470-f0e791bccf1b",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLD1Hida42gbXvgnXEx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f86dd102-eb00-4423-9ab1-d7b63b783a0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8gHCTQUqVKHJo2wNsoVjd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6447,
      "cache_read_input_tokens": 32930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6447,
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

### Tool result

_source line 22 · 2026-05-23T10:20:15.968Z_

<details><summary>↩ Tool result · `toolu_01L4gEw1KEwnYtU3VGHvJLnu`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Full-replacement vs.\ accumulation.}
5	The primary benchmark uses full-replacement chains; real-world contamination involves accumulation at unknown mixing ratios \cite{gerstgrasser2024_accumulate}.
6	Accumulation experiments (Appendix~\ref{app:accumulation_auc}) show accuracy attenuation that increases with higher synthetic mixing ratios, and do not test cross-strategy accumulation; extension to larger models and higher mixing ratios remains future work.
7	
8	\paragraph{Scale, generalization, and reference model.}
9	Depth signal attenuates at larger scales (\S\ref{sec:gen:crossscale}), with reference-model mismatch contributing to the observed degradation.
10	Cross-strategy transfer can invert adjacent-depth predictions when the classifier's training strategy differs from the test data, requiring strategy-aware deployment.
11	The pipeline requires a fixed reference model; cross-architecture references degrade accuracy (Appendix~\ref{app:ref_ablation}).
12	BOS-seeded generation differs from prompted generation by 13.8\,pp (Appendix~\ref{app:prompted_gen}), so measured depth signals may partly reflect unconditional generation artifacts.
13	On held-out web-crawl corpora, pooled-classifier raw false-positive rates range from 15\% (RedPajama) to 34\% (C4), reducible to ${\leq}$7\% via posterior-threshold calibration (Appendix~\ref{app:calibration}).
14	Additional caveats (single LoRA seed, partially mitigated by two-seed replication in Appendix~\ref{app:seed_replication}; web-crawl false positive rates; passage length sensitivity, Appendix~\ref{app:length_ablation}) are detailed in the Appendix.
15	Robustness to post-hoc paraphrasing or editing remains untested.
16	Compute budget details are reported in Appendix~\ref{app:compute}.
17	
18	\section*{Ethics Statement}
19	
20	This work uses publicly available pretrained language models (Pythia-1.4B, OLMo-1B, GPT-2~XL) and Wikipedia text as seed data.
21	No human subjects were involved, no private or sensitive data were collected, and no new models were released.
22	Our method is intended to support data provenance and training-data auditing; we acknowledge that depth estimation tools could in principle be misused to circumvent content moderation, though such risks are shared with all detection-oriented research.
23	Code and data will be released upon acceptance.
24	AI assistants were used in an auxiliary role for coding support and language polishing.
25	All scientific decisions, experimental design, analysis, and core writing were conducted by the authors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f86dd102-eb00-4423-9ab1-d7b63b783a0d",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "f53606ed-ebc0-403c-9169-33855b50f16a",
  "sourceToolAssistantUUID": "f86dd102-eb00-4423-9ab1-d7b63b783a0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T10:20:16.431Z_

<details open><summary>🔧 Tool call — Read · `toolu_0118RnqvumoJQu8WYVYqFXfT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f53606ed-ebc0-403c-9169-33855b50f16a",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLD1Hida42gbXvgnXEx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1bc20b06-0094-4fa9-8477-76cee534efce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8gHCTQUqVKHJo2wNsoVjd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6447,
      "cache_read_input_tokens": 32930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6447,
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

### Tool result

_source line 24 · 2026-05-23T10:20:16.438Z_

<details><summary>↩ Tool result · `toolu_0118RnqvumoJQu8WYVYqFXfT`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	Recursive training on model outputs erodes distributional tails \cite{shumailov2024_nature}, an effect formalized as exponential tail decay via scaling laws \cite{dohmatob2024_tale_of_tails,seddik2024synthetic} and extended to autophagous loops in the MAD framework \cite{alemohammad2024_mad} and Markovian generation chains \cite{geng2026_markovian}.
6	Subsequent work refines the conditions under which collapse occurs: \citet{bertrand2024_stability} identify convergence to a fixed point under mixed real-synthetic retraining (providing theoretical grounding for our EDD ceiling, \S\ref{sec:method:theory}), \citet{shi2025_closer_look} reframe collapse as a generalization-to-memorization transition, and \citet{dohmatob2025_strong_collapse} extend guarantees to broader model classes.
7	Mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated}, convergence analysis \cite{marchi2024_heat_death,wang2026_contamination,dohmatob2024_demystified,suresh2025_rate_collapse}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement,kazdan2025_collapse_or_thrive}, and diversity decline \cite{guo2024curious,padmakumar2024diversity,sigma2026_spectral} are active areas.
8	\citet{schaeffer2025} argue that ``model collapse'' conflates multiple phenomena and call for operationally precise metrics; we respond by operationalizing tail-erosion predictions into a deployable ordinal classifier that reveals strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.
9	All assume depth is known a priori; we address the inverse problem of estimating depth from text alone.
10	
11	\paragraph{AI Text Detection.}
12	The detection literature \cite{wu2025_detection_survey} spans statistical \cite{mitchell2023_detectgpt,fast_detectgpt2024,binoculars2024,diveye2026,guo2024_biscope,gehrmann2019_gltr,verma2024_ghostbuster,yang2024_dnagpt}, geometric \cite{tulchinskii2023_intrinsic_dim}, and watermarking \cite{kirchenbauer2023_watermark} methods, with known limits \cite{sadasivan2023_paraphrase,pudasaini2026_detection_fails,pu2026_generator_barrier}.
13	\citet{wang2023_seqxgpt} address sentence-level attribution by using log-probability features from white-box LLMs.
14	Shared tasks \cite{wang2024_m4_semeval,li2024_mage,bevendorff2026_pan,dugan2024_raid} benchmark detection across domains and attack vectors.
15	\citet{bevendorff2025_two_paradigms} distinguish attribution from verification; depth estimation introduces a third axis: recursive iteration.
16	All perform binary classification; our approach outputs ordinal depth labels, complementing rather than replacing detection.
17	
18	\paragraph{Membership Inference and Data Provenance.}
19	\citet{carlini2021_extracting} demonstrate that training data can be extracted from LLMs, motivating provenance-aware pipelines.
20	Min-K\% Prob \cite{shi2024_minkprob} detects pretraining membership via low-probability token statistics, related to our perplexity features but limited to binary classification; Datamodels \cite{ilyas2022datamodels} trace predictions to influential training examples; cryptographically undetectable watermarks \cite{christ2024_undetectable} require generator cooperation.
21	TROVE \cite{zhu2025_trove} introduces fine-grained sentence-level provenance tracing with relationship classification, but targets source attribution rather than recursive depth.
22	Depth estimation occupies a distinct niche: ordinal, retroactive, and cooperation-free.
23	
24	\paragraph{Adjacent Tasks.}
25	EditLens \cite{editlens2026} estimates editing extent but does not model recursive chains; \citet{uchendu2020_attribution} classify \emph{which} model generated text; \citet{mohamed2025_broken_telephone} characterize \emph{how} text degrades under iterative generation without classifying which iteration a passage comes from.
26	Our task performs the inverse: ordinal depth estimation from text alone.
27	
28	\paragraph{Ordinal Classification.}
29	CORAL \cite{coral2020} enforces rank consistency via ordered binary tasks; CLOC \cite{cloc2025} extends contrastive learning with multi-margin ordinal losses; \citet{kasa2024_ordinality} benchmark ordinal techniques for NLP; \citet{janitza2016_ordinal_rf} show RF implicitly respects ordinal structure when inter-class distances are monotonic.
30	We adopt CORAL and CLOC as baselines (\S\ref{sec:generalization}).
31	
32	\paragraph{Decoding Strategy Effects.}
33	Decoding strategies shape text statistics in ways that interact with depth signals \cite{holtzman2020_nucleus,finlayson2024_closing,garces_arias2025_decoding_decoded,wiher2022_decoding,basu2021_mirostat}.
34	Our atlas (\S\ref{sec:atlas}) shows these strategies induce qualitatively different degradation trajectories under recursive generation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bc20b06-0094-4fa9-8477-76cee534efce",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "5db84dc5-92ce-47f0-b789-d03a50cea7e2",
  "sourceToolAssistantUUID": "1bc20b06-0094-4fa9-8477-76cee534efce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T10:20:16.835Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XmNkTLxh1QJGsNUvGfWBWx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5db84dc5-92ce-47f0-b789-d03a50cea7e2",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLD1Hida42gbXvgnXEx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7546d97-275b-4b65-8a26-bafc9d0531c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8gHCTQUqVKHJo2wNsoVjd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6447,
      "cache_read_input_tokens": 32930,
      "output_tokens": 686,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6447
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 686,
          "cache_read_input_tokens": 32930,
          "cache_creation_input_tokens": 6447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6447,
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

_source line 26 · 2026-05-23T10:20:16.842Z_

<details><summary>↩ Tool result · `toolu_01XmNkTLxh1QJGsNUvGfWBWx`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	We use \emph{depth estimation} as shorthand throughout; the underlying task is ordinal classification.
13	Depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
14	
15	\subsection{Multi-Generational Benchmark Construction}
16	\label{sec:method:benchmark}
17	
18	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
19	
20	\paragraph{Model families.}
21	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
22	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
23	
24	\paragraph{Decoding strategies.}
25	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
26	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
27	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
28	
29	\paragraph{Depth and scale.}
30	The primary benchmark covers depths d0--d3 across all $3 \times 3 = 9$ model--strategy cells, with 5{,}000 samples per depth per cell (180K cell-instances; 140K unique passages, as d0 samples are drawn from a shared Wikipedia seed corpus across all cells).
31	For depth extension experiments (\S\ref{sec:atlas}), we extend all three models under nucleus sampling to d0--d5.
32	
33	\paragraph{Generation pipeline.}
34	Starting from a Wikipedia subset ($\mathcal{D}_0$), each cycle: (1)~LoRA finetuning \cite{hu2022lora} on $\mathcal{D}_{k-1}$ ($r{=}16$, $\alpha{=}32$, lr $2{\times}10^{-4}$, effective batch 16, 3 epochs, dropout $0.05$; fresh adapter from the base model at each depth; full protocol in Appendix~\ref{app:lora_protocol}); (2)~sampling 5{,}000 passages (max 512 tokens, beginning-of-sequence (BOS) seeded) under the specified strategy; (3)~$\mathcal{D}_k$ feeds the next cycle.
35	Each depth is produced by a model trained on prior-depth data, not by sampling from the unmodified base model.
36	BOS seeding may amplify depth signal; prompted-generation validation (Appendix~\ref{app:prompted_gen}) confirms signal persistence albeit attenuated ($-$13.8\,pp).
37	No per-passage lineage exists across depths; cross-validation splits do not introduce leakage.
38	
39	\paragraph{Reference model.}
40	All statistical features (\S\ref{sec:method:features}) use Pythia-1.4B as fixed reference model.
41	This overlaps with one generator (Pythia), conferring a 4--11\,pp self-reference advantage on that pipeline (Appendix~\ref{app:ref_ablation}); Pythia results in Table~\ref{tab:main_matrix} are marked $^\dagger$ accordingly.
42	Alternative references yield 67--79\%, all exceeding $2.5{\times}$ chance (Limitations).
43	
44	\subsection{Statistical Feature Design}
45	\label{sec:method:features}
46	
47	We extract a feature vector $\mathbf{f}(x)$ comprising 19 candidate features from the reference-model perplexity distribution over each passage $x$; ablation (\S\ref{sec:atlas:features}) shows the top 5 achieve 97.6\% of full-set performance, and variance inflation analysis reveals VIF${>}$10 for 14--16 features; effective independent dimensionality is ${\approx}$4--5.
48	The features fall into four categories (Table~\ref{tab:features}).
49	
50	\begin{table}[t]
51	\centering
52	\small
53	\caption{The 19 statistical features comprising $\mathbf{f}(x)$, grouped by category. All perplexity and surprisal features are computed from the reference model (Pythia-1.4B).}
54	\label{tab:features}
55	\begin{tabular*}{\columnwidth}{@{\extracolsep{\fill}}llr}
56	\toprule
57	Category & Features & $n$ \\
58	\midrule
59	Perplexity & mean, var, skewness, kurtosis, & 9 \\
60	statistics & p10, p25, p50, p75, p90 & \\
61	\addlinespace
62	Surprisal & mean, var, entropy & 3 \\
63	statistics & & \\
64	\addlinespace
65	Lexical & type--token ratio, hapax ratio, & 4 \\
66	diversity & bigram entropy, trigram entropy & \\
67	\addlinespace
68	Repetition & repeated 2/3/4-gram fractions & 3 \\
69	\bottomrule
70	\end{tabular*}
71	\end{table}
72	
73	\emph{Perplexity statistics} (9 features) capture the per-token perplexity distribution via moments and quantiles (p10--p90); tail quantiles are especially informative as recursive finetuning erodes the high-perplexity tail (\S\ref{sec:atlas}).
74	\emph{Surprisal statistics} (3 features): mean, variance, and entropy of $-\log p(\text{token})$.
75	\emph{Lexical diversity} (4 features): type--token ratio, hapax ratio, bigram/trigram entropy.
76	\emph{Repetition} (3 features): repeated $n$-gram fractions for $n \in \{2, 3, 4\}$.
77	
78	\subsection{Effective Discriminable Depth}
79	\label{sec:method:edd}
80	
81	Aggregate multi-class accuracy obscures whether discriminability degrades at specific depth boundaries.
82	We propose the \emph{Effective Discriminable Depth} (EDD) as an operational measure of how far into a recursive chain adjacent depths remain distinguishable.
83	
84	\paragraph{Pairwise discriminability.}
85	Let $\mathcal{D} = \{0, 1, \dots, K\}$ denote the depth set and $T \in (0.5, 1.0]$ a discrimination threshold.
86	For each adjacent pair $(d, d{+}1)$, we define the pairwise discriminability $\mathrm{AUC}(d, d{+}1)$ as the area under the ROC curve of a dedicated binary Random Forest classifier (500 trees, $\lfloor\sqrt{19}\rfloor$ candidate features per split) trained on class-balanced data from $\mathbf{f}(x)$ (\S\ref{sec:method:features}) to distinguish depth-$d$ from depth-$(d{+}1)$ samples, evaluated via 5-fold stratified cross-validation.
87	Each pair uses an independent classifier to avoid decision boundary dilution from multi-class settings.
88	
89	\begin{definition}[Effective Discriminable Depth]
90	\label{def:edd}
91	The \emph{Effective Discriminable Depth} at threshold $T$ is:
92	\begin{multline}
93	\mathrm{EDD}_T = \max \bigl\{ d^*{+}1 \,:\, \\
94	\forall\, d' \leq d^*,\; \mathrm{AUC}(d', d'{+}1) \geq T \bigr\}
95	\label{eq:edd}
96	\end{multline}
97	where $d^* \in \{0, \dots, K{-}1\}$. If\, $\mathrm{AUC}(0,1) < T$, then $\mathrm{EDD}_T = 0$.
98	\end{definition}
99	
100	$\mathrm{EDD}_T$ reports the longest \emph{contiguous} discriminable prefix: the deepest $d$ such that every pair from $(0,1)$ through $(d{-}1, d)$ exceeds $T$.
101	All AUC profiles in the primary benchmark decay monotonically; non-monotonic profiles occur only in cross-scale extensions (Appendix~\ref{app:cross_scale_full}).
102	We adopt $T{=}0.70$ following the ``acceptable discrimination'' threshold in ROC analysis \cite{hosmer2000} (8/9 cells achieve $\mathrm{EDD}_{0.70} \geq 3$); sensitivity analysis (\S\ref{sec:atlas:edd}) shows $\mathrm{EDD}$ shifts by at most one level across $T \in \{0.65, 0.70, 0.80\}$ in all nine cells.
103	
104	\paragraph{Classifiers.}
105	Our primary classifier is a Random Forest (200 trees, unconstrained depth, 5-fold CV; EDD binary classifiers use 500 trees).\footnote{Statistical tests are not corrected for multiple comparisons; $p$-values should be interpreted as exploratory.}
106	The RF produces ordinally consistent predictions: 98.2\% of errors fall on adjacent depths ($|\Delta| \leq 1$), quadratic weighted kappa (QWK)\,=\,0.89.
107	Comparisons against other classifiers and detection baselines appear in \S\ref{sec:generalization}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7546d97-275b-4b65-8a26-bafc9d0531c3",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "bad539da-8d20-4ead-abad-368351446046",
  "sourceToolAssistantUUID": "d7546d97-275b-4b65-8a26-bafc9d0531c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-23T10:20:19.746Z_

Now let me read the appendix and the key artifact data files to cross-reference the numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bad539da-8d20-4ead-abad-368351446046",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLDbby5NmevWSccSbuv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1cc817d4-fe0b-43b4-b481-51a96db3c743",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UqPypkvTt5ZEMYHk4MdrFA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15995,
      "cache_read_input_tokens": 39377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15995,
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

_source line 28 · 2026-05-23T10:20:21.168Z_

<details open><summary>🔧 Tool call — Read · `toolu_012HsnpH4tEA7ssptRy8K4BK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cc817d4-fe0b-43b4-b481-51a96db3c743",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLDbby5NmevWSccSbuv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c97d25a3-9874-4a9b-a524-3611122c0d7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UqPypkvTt5ZEMYHk4MdrFA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15995,
      "cache_read_input_tokens": 39377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15995,
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

_source line 29 · 2026-05-23T10:20:21.427Z_

<details><summary>↩ Tool result · reported error · `toolu_012HsnpH4tEA7ssptRy8K4BK`</summary>

```text
File content (28185 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c97d25a3-9874-4a9b-a524-3611122c0d7c",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "65c1338c-1bb1-415a-9e07-120ff72d55d6",
  "toolUseResult": "Error: File content (28185 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "c97d25a3-9874-4a9b-a524-3611122c0d7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-23T10:20:22.104Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NQsneBtMkdZNjhP7ofSkQu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/edd_matrix.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65c1338c-1bb1-415a-9e07-120ff72d55d6",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLDbby5NmevWSccSbuv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29ba9824-cdab-4d4c-b7ae-6b4aaf6a29b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UqPypkvTt5ZEMYHk4MdrFA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15995,
      "cache_read_input_tokens": 39377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15995,
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

_source line 31 · 2026-05-23T10:20:22.111Z_

<details><summary>↩ Tool result · `toolu_01NQsneBtMkdZNjhP7ofSkQu`</summary>

```text
1	See server: /root/autodl-tmp/recursive_gen_depth_est/artifacts/atlas/edd_matrix.json
2	
3	Key finding: All 19 features across all 4 chains have EDD=3 (max), meaning degradation has NOT saturated by depth 3. This suggests deeper recursion would continue to degrade.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29ba9824-cdab-4d4c-b7ae-6b4aaf6a29b6",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "74bd0a9c-ff55-4186-a022-011470ff6060",
  "sourceToolAssistantUUID": "29ba9824-cdab-4d4c-b7ae-6b4aaf6a29b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-23T10:20:22.848Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Fb8iTPu6vtJxePMpVfxwqT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/matrix_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74bd0a9c-ff55-4186-a022-011470ff6060",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLDbby5NmevWSccSbuv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa11acb6-7e8b-4df4-b007-32ae26e815aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UqPypkvTt5ZEMYHk4MdrFA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15995,
      "cache_read_input_tokens": 39377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15995,
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

_source line 33 · 2026-05-23T10:20:23.116Z_

<details><summary>↩ Tool result · `toolu_01Fb8iTPu6vtJxePMpVfxwqT`</summary>

```text
1	{
2	  "metadata": {
3	    "version": "2.0",
4	    "generated_at": "2026-05-15",
5	    "n_cells_completed": 7,
6	    "n_cells_total": 9,
7	    "n_samples_per_depth": 5000,
8	    "n_depths": 4,
9	    "feature_count": 19,
10	    "classifier": "RandomForest (primary), LogisticRegression (secondary)",
11	    "data_source": "gpu-6000pro-2:/root/autodl-tmp/recursive_gen_depth_est/results/",
12	    "seed_data": "Wikipedia (depth_0.jsonl, 5000 samples)"
13	  },
14	  "grid": {
15	    "models": ["Pythia-1.4B", "OLMo-1B", "GPT-2-XL"],
16	    "strategies": ["nucleus_p095", "temperature_09", "topk_k50"],
17	    "cell_keys": {
18	      "Pythia-1.4B": {"nucleus_p095": "pythia_nucleus", "temperature_09": "pythia_temp09", "topk_k50": "pythia_topk50"},
19	      "OLMo-1B": {"nucleus_p095": "olmo_nucleus", "temperature_09": "olmo_temp09", "topk_k50": "olmo_topk50"},
20	      "GPT-2-XL": {"nucleus_p095": "gpt2xl_nucleus", "temperature_09": "gpt2xl_temp09", "topk_k50": "gpt2xl_topk50"}
21	    }
22	  },
23	  "cells": {
24	    "pythia_nucleus": {
25	      "model": "Pythia-1.4B",
26	      "strategy": "nucleus_p095",
27	      "experiment_id": "mvp_pipeline_pythia_002",
28	      "status": "done",
29	      "acc_4class": {"random_forest": 0.782, "logistic_regression": 0.7492, "rf_ci": [0.769, 0.794]},
30	      "acc_3class": {"random_forest": 0.708, "rf_ci": [0.692, 0.725]},
31	      "acc_3class_filtered": {"random_forest": 0.747, "rf_ci": [0.727, 0.764]},
32	      "pairwise_auc": {
33	        "random_forest": {"d0v1": 0.9975, "d0v2": 0.9995, "d0v3": 0.9986, "d1v2": 0.8607, "d1v3": 0.9685, "d2v3": 0.8005},
34	        "logistic_regression": {"d0v1": 0.9922, "d0v2": 0.9997, "d0v3": 0.9997, "d1v2": 0.7784, "d1v3": 0.9484, "d2v3": 0.7578}
35	      },
36	      "feature_importance": {
37	        "var_surprisal": 0.1692, "p90_ppl": 0.1582, "mean_ppl": 0.1204, "mean_surprisal": 0.0884,
38	        "p75_ppl": 0.0671, "skewness_ppl": 0.0392, "p50_ppl": 0.0366, "entropy_of_surprisal": 0.0350,
39	        "kurtosis_ppl": 0.0344, "type_token_ratio": 0.0343, "hapax_ratio": 0.0316, "p25_ppl": 0.0308,
40	        "bigram_entropy": 0.0290, "rep_2gram": 0.0268, "trigram_entropy": 0.0260, "p10_ppl": 0.0250,
41	        "rep_4gram": 0.0243, "rep_3gram": 0.0224, "var_ppl": 0.0014
42	      },
43	      "top5_features": ["var_surprisal", "p90_ppl", "mean_ppl", "mean_surprisal", "p75_ppl"],
44	      "finetune_losses": {"depth_0": 2.2411, "depth_1": 1.3894, "depth_2": 1.025},
45	      "code_contamination_narrow": {"d0": 0.004, "d1": 0.050, "d2": 0.090, "d3": 0.120},
46	      "feature_trajectory": {
47	        "available": true,
48	        "features_path": "data/features_all.jsonl",
49	        "depth_means": {
50	          "0": {"p90_ppl": 483.738, "mean_surprisal": 2.292, "var_surprisal": 6.497, "p75_ppl": 39.281, "mean_ppl": 25063.789, "type_token_ratio": 0.508, "rep_2gram": 0.166, "rep_3gram": 0.070, "rep_4gram": 0.033},
51	          "1": {"p90_ppl": 61.383, "mean_surprisal": 1.508, "var_surprisal": 2.487, "p75_ppl": 14.288, "mean_ppl": 6828.883, "type_token_ratio": 0.417, "rep_2gram": 0.279, "rep_3gram": 0.166, "rep_4gram": 0.113},
52	          "2": {"p90_ppl": 29.684, "mean_surprisal": 1.179, "var_surprisal": 1.856, "p75_ppl": 7.700, "mean_ppl": 3283.344, "type_token_ratio": 0.367, "rep_2gram": 0.351, "rep_3gram": 0.232, "rep_4gram": 0.171},
53	          "3": {"p90_ppl": 18.152, "mean_surprisal": 0.951, "var_surprisal": 1.509, "p75_ppl": 5.064, "mean_ppl": 2418.228, "type_token_ratio": 0.313, "rep_2gram": 0.443, "rep_3gram": 0.326, "rep_4gram": 0.261}
54	        }
55	      }
56	    },
57	    "pythia_temp09": {
58	      "model": "Pythia-1.4B",
59	      "strategy": "temperature_09",
60	      "experiment_id": "pythia_temp09_001",
61	      "status": "done",
62	      "acc_4class": {"random_forest": 0.7625, "logistic_regression": 0.7405, "rf_ci": [0.749, 0.7753]},
63	      "acc_3class": {"random_forest": 0.6983, "rf_ci": [0.682, 0.715]},
64	      "acc_3class_filtered": {"random_forest": 0.7252, "rf_ci": [0.7064, 0.7427]},
65	      "pairwise_auc": {
66	        "random_forest": {"d0v1": 0.9968, "d0v2": 0.9993, "d0v3": 0.9991, "d1v2": 0.8327, "d1v3": 0.9590, "d2v3": 0.7928},
67	        "logistic_regression": {"d0v1": 0.9934, "d0v2": 0.9999, "d0v3": 0.9997, "d1v2": 0.7833, "d1v3": 0.9374, "d2v3": 0.7652}
68	      },
69	      "feature_importance": {
70	        "var_surprisal": 0.1776, "p90_ppl": 0.1501, "mean_ppl": 0.1140, "mean_surprisal": 0.0889,
71	        "p75_ppl": 0.0687, "p50_ppl": 0.0395, "type_token_ratio": 0.0356, "hapax_ratio": 0.0352,
72	        "entropy_of_surprisal": 0.0335, "bigram_entropy": 0.0312, "p25_ppl": 0.0309, "trigram_entropy": 0.0295,
73	        "rep_4gram": 0.0292, "rep_2gram": 0.0279, "skewness_ppl": 0.0275, "kurtosis_ppl": 0.0266,
74	        "p10_ppl": 0.0265, "rep_3gram": 0.0253, "var_ppl": 0.0024
75	      },
76	      "top5_features": ["var_surprisal", "p90_ppl", "mean_ppl", "mean_surprisal", "p75_ppl"],
77	      "finetune_losses": {"depth_0": 2.222, "depth_1": 1.370, "depth_2": 1.006},
78	      "code_contamination_narrow": {"d0": 0.004, "d1": 0.077, "d2": 0.116, "d3": 0.136},
79	      "feature_trajectory": {
80	        "available": true,
81	        "features_path": "data/pythia_temp09/features.jsonl",
82	        "depth_means": {
83	          "0": {"p90_ppl": 483.738, "mean_surprisal": 2.292, "var_surprisal": 6.497, "p75_ppl": 39.281, "mean_ppl": 25063.789, "type_token_ratio": 0.508, "rep_2gram": 0.166, "rep_3gram": 0.070, "rep_4gram": 0.033},
84	          "1": {"p90_ppl": 63.242, "mean_surprisal": 1.485, "var_surprisal": 2.660, "p75_ppl": 12.623, "mean_ppl": 1687.519, "type_token_ratio": 0.411, "rep_2gram": 0.290, "rep_3gram": 0.175, "rep_4gram": 0.120},
85	          "2": {"p90_ppl": 29.246, "mean_surprisal": 1.156, "var_surprisal": 1.987, "p75_ppl": 6.763, "mean_ppl": 8821.625, "type_token_ratio": 0.356, "rep_2gram": 0.372, "rep_3gram": 0.252, "rep_4gram": 0.188},
86	          "3": {"p90_ppl": 17.394, "mean_surprisal": 0.927, "var_surprisal": 1.598, "p75_ppl": 4.442, "mean_ppl": 6395.753, "type_token_ratio": 0.302, "rep_2gram": 0.440, "rep_3gram": 0.325, "rep_4gram": 0.254}
87	        }
88	      }
89	    },
90	    "pythia_topk50": {
91	      "model": "Pythia-1.4B",
92	      "strategy": "topk_k50",
93	      "experiment_id": "pythia_topk50_001",
94	      "status": "done",
95	      "acc_4class": {"random_forest": 0.696, "logistic_regression": 0.682, "rf_ci": [0.6825, 0.7107]},
96	      "acc_3class": {"random_forest": 0.592, "rf_ci": [0.575, 0.6107]},
97	      "acc_3class_filtered": {"random_forest": 0.6133, "rf_ci": [0.593, 0.6312]},
98	      "pairwise_auc": {
99	        "random_forest": {"d0v1": 0.9927, "d0v2": 0.9983, "d0v3": 0.9978, "d1v2": 0.7518, "d1v3": 0.9176, "d2v3": 0.6918},
100	        "logistic_regression": {"d0v1": 0.9889, "d0v2": 0.9983, "d0v3": 0.9995, "d1v2": 0.7289, "d1v3": 0.9039, "d2v3": 0.6804}
101	      },
102	      "feature_importance": {
103	        "var_surprisal": 0.1759, "p90_ppl": 0.1347, "mean_ppl": 0.1120, "mean_surprisal": 0.0702,
104	        "p75_ppl": 0.0612, "type_token_ratio": 0.0416, "hapax_ratio": 0.0416, "p50_ppl": 0.0386,
105	        "p25_ppl": 0.0373, "entropy_of_surprisal": 0.0368, "bigram_entropy": 0.0345, "trigram_entropy": 0.0333,
106	        "p10_ppl": 0.0330, "skewness_ppl": 0.0327, "kurtosis_ppl": 0.0316, "rep_2gram": 0.0297,
107	        "rep_4gram": 0.0281, "rep_3gram": 0.0264, "var_ppl": 0.0008
108	      },
109	      "top5_features": ["var_surprisal", "p90_ppl", "mean_ppl", "mean_surprisal", "p75_ppl"],
110	      "finetune_losses": {"depth_0": 2.2406, "depth_1": 1.6704, "depth_2": 1.4374},
111	      "code_contamination_narrow": {"d0": 0.004, "d1": 0.077, "d2": 0.123, "d3": 0.131},
112	      "feature_trajectory": {
113	        "available": false,
114	        "note": "features.jsonl not saved during pipeline; rerun extract_features.py to generate"
115	      }
116	    },
117	    "olmo_nucleus": {
118	      "model": "OLMo-1B",
119	      "strategy": "nucleus_p095",
120	      "experiment_id": "cross_model_olmo_002",
121	      "status": "done",
122	      "acc_4class": {"random_forest": 0.788, "logistic_regression": 0.751, "rf_ci": [0.776, 0.800]},
123	      "acc_3class": {"random_forest": 0.744, "rf_ci": [0.728, 0.760]},
124	      "acc_3class_filtered": null,
125	      "pairwise_auc": {
126	        "random_forest": {"d0v1": 0.9834, "d0v2": 0.9949, "d0v3": 0.9989, "d1v2": 0.8673, "d1v3": 0.9806, "d2v3": 0.8124},
127	        "logistic_regression": {"d0v1": 0.9809, "d0v2": 0.9921, "d0v3": 0.9945, "d1v2": 0.8296, "d1v3": 0.9629, "d2v3": 0.7661}
128	      },
129	      "feature_importance": {
130	        "p90_ppl": 0.1803, "var_surprisal": 0.1608, "p75_ppl": 0.1110, "mean_surprisal": 0.0838,
131	        "type_token_ratio": 0.0605, "hapax_ratio": 0.0441, "p50_ppl": 0.0411, "mean_ppl": 0.0395,
132	        "p25_ppl": 0.0363, "rep_3gram": 0.0292, "p10_ppl": 0.0290, "rep_4gram": 0.0289,
133	        "rep_2gram": 0.0279, "entropy_of_surprisal": 0.0268, "kurtosis_ppl": 0.0258, "skewness_ppl": 0.0245,
134	        "bigram_entropy": 0.0234, "trigram_entropy": 0.0234, "var_ppl": 0.0036
135	      },
136	      "top5_features": ["p90_ppl", "var_surprisal", "p75_ppl", "mean_surprisal", "type_token_ratio"],
137	      "finetune_losses": {"depth_0": 2.269, "depth_1": 1.650, "depth_2": 1.226},
138	      "code_contamination_narrow": {"d0": 0.005, "d1": 0.027, "d2": 0.007, "d3": 0.008},
139	      "feature_trajectory": {
140	        "available": true,
141	        "features_path": "data/olmo/features.jsonl",
142	        "depth_means": {
143	          "0": {"p90_ppl": 483.738, "mean_surprisal": 2.292, "var_surprisal": 6.497, "p75_ppl": 39.281, "mean_ppl": 25063.789, "type_token_ratio": 0.508, "rep_2gram": 0.166, "rep_3gram": 0.070, "rep_4gram": 0.033},
144	          "1": {"p90_ppl": 136.061, "mean_surprisal": 2.036, "var_surprisal": 3.874, "p75_ppl": 26.769, "mean_ppl": 370430.397, "type_token_ratio": 0.424, "rep_2gram": 0.236, "rep_3gram": 0.121, "rep_4gram": 0.074},
145	          "2": {"p90_ppl": 66.503, "mean_surprisal": 1.660, "var_surprisal": 3.012, "p75_ppl": 13.974, "mean_ppl": 1321936.921, "type_token_ratio": 0.364, "rep_2gram": 0.325, "rep_3gram": 0.203, "rep_4gram": 0.144},
146	          "3": {"p90_ppl": 42.682, "mean_surprisal": 1.364, "var_surprisal": 2.487, "p75_ppl": 9.023, "mean_ppl": 569854.183, "type_token_ratio": 0.305, "rep_2gram": 0.432, "rep_3gram": 0.316, "rep_4gram": 0.253}
147	        }
148	      }
149	    },
150	    "olmo_temp09": {
151	      "model": "OLMo-1B",
152	      "strategy": "temperature_09",
153	      "experiment_id": "olmo_temp09_001",
154	      "status": "done",
155	      "acc_4class": {"random_forest": 0.8203, "logistic_regression": 0.8155, "rf_ci": [0.8087, 0.8320]},
156	      "acc_3class": null,
157	      "acc_3class_filtered": {"random_forest": 0.7757},
158	      "pairwise_auc": {
159	        "random_forest": {"d0v1": 0.9960, "d0v2": 0.9997, "d0v3": 0.9995, "d1v2": 0.9010, "d1v3": 0.9874, "d2v3": 0.8214},
160	        "logistic_regression": {"d0v1": 0.9976, "d0v2": 0.9999, "d0v3": 0.9999, "d1v2": 0.8910, "d1v3": 0.9842, "d2v3": 0.8160}
161	      },
162	      "feature_importance": {
163	        "p90_ppl": 0.1987, "var_surprisal": 0.1741, "p75_ppl": 0.1263, "mean_surprisal": 0.1139,
164	        "p50_ppl": 0.0510, "type_token_ratio": 0.0498, "rep_2gram": 0.0337, "p25_ppl": 0.0312,
165	        "hapax_ratio": 0.0286, "entropy_of_surprisal": 0.0263, "p10_ppl": 0.0255, "rep_3gram": 0.0243,
166	        "skewness_ppl": 0.0240, "trigram_entropy": 0.0233, "kurtosis_ppl": 0.0231, "bigram_entropy": 0.0221,
167	        "rep_4gram": 0.0211, "mean_ppl": 0.0030, "var_ppl": 0.0001
168	      },
169	      "top5_features": ["p90_ppl", "var_surprisal", "p75_ppl", "mean_surprisal", "p50_ppl"],
170	      "finetune_losses": {"depth_0": 2.270, "depth_1": 1.630, "depth_2": 1.180},
171	      "code_contamination_narrow": {"d0": 0.005, "d1": 0.005, "d2": 0.005, "d3": 0.007},
172	      "feature_trajectory": {
173	        "available": false,
174	        "note": "features.jsonl not saved during pipeline; rerun extract_features.py to generate"
175	      }
176	    },
177	    "olmo_topk50": {
178	      "model": "OLMo-1B",
179	      "strategy": "topk_k50",
180	      "experiment_id": "olmo_topk50_001",
181	      "status": "running",
182	      "placeholder": true
183	    },
184	    "gpt2xl_nucleus": {
185	      "model": "GPT-2-XL",
186	      "strategy": "nucleus_p095",
187	      "experiment_id": "cross_model_gpt2xl_001",
188	      "status": "done",
189	      "acc_4class": {"random_forest": 0.833, "logistic_regression": 0.813, "rf_ci": [0.823, 0.845]},
190	      "acc_3class": {"random_forest": 0.793, "rf_ci": [0.778, 0.806]},
191	      "acc_3class_filtered": null,
192	      "pairwise_auc": {
193	        "random_forest": {"d0v1": 0.9941, "d0v2": 0.9965, "d0v3": 0.9988, "d1v2": 0.9131, "d1v3": 0.9857, "d2v3": 0.8829},
194	        "logistic_regression": {"d0v1": 0.9808, "d0v2": 0.9941, "d0v3": 0.9937, "d1v2": 0.8469, "d1v3": 0.9686, "d2v3": 0.8651}
195	      },
196	      "feature_importance": {
197	        "p90_ppl": 0.2082, "var_surprisal": 0.2079, "p75_ppl": 0.1034, "mean_surprisal": 0.0821,
198	        "mean_ppl": 0.0645, "type_token_ratio": 0.0460, "p50_ppl": 0.0349, "entropy_of_surprisal": 0.0347,
199	        "p25_ppl": 0.0316, "hapax_ratio": 0.0283, "skewness_ppl": 0.0221, "p10_ppl": 0.0211,
200	        "kurtosis_ppl": 0.0210, "rep_2gram": 0.0204, "rep_4gram": 0.0191, "bigram_entropy": 0.0185,
201	        "trigram_entropy": 0.0182, "rep_3gram": 0.0172, "var_ppl": 0.0007
202	      },
203	      "top5_features": ["p90_ppl", "var_surprisal", "p75_ppl", "mean_surprisal", "mean_ppl"],
204	      "finetune_losses": {"depth_0": 2.550, "depth_1": 1.715, "depth_2": 1.342},
205	      "code_contamination_narrow": {"d0": 0.005, "d1": 0.005, "d2": 0.013, "d3": 0.007},
206	      "feature_trajectory": {
207	        "available": true,
208	        "features_path": "data/gpt2xl/features.jsonl",
209	        "depth_means": {
210	          "0": {"p90_ppl": 483.738, "mean_surprisal": 2.292, "var_surprisal": 6.497, "p75_ppl": 39.281, "mean_ppl": 25063.789, "type_token_ratio": 0.508, "rep_2gram": 0.166, "rep_3gram": 0.070, "rep_4gram": 0.033},
211	          "1": {"p90_ppl": 128.113, "mean_surprisal": 1.983, "var_surprisal": 3.623, "p75_ppl": 25.447, "mean_ppl": 53972.778, "type_token_ratio": 0.429, "rep_2gram": 0.232, "rep_3gram": 0.118, "rep_4gram": 0.070},
212	          "2": {"p90_ppl": 73.819, "mean_surprisal": 1.681, "var_surprisal": 3.073, "p75_ppl": 15.129, "mean_ppl": 678385.871, "type_token_ratio": 0.378, "rep_2gram": 0.305, "rep_3gram": 0.185, "rep_4gram": 0.128},
213	          "3": {"p90_ppl": 57.643, "mean_surprisal": 1.487, "var_surprisal": 2.473, "p75_ppl": 10.823, "mean_ppl": 1076268.162, "type_token_ratio": 0.376, "rep_2gram": 0.316, "rep_3gram": 0.199, "rep_4gram": 0.141}
214	        }
215	      }
216	    },
217	    "gpt2xl_temp09": {
218	      "model": "GPT-2-XL",
219	      "strategy": "temperature_09",
220	      "experiment_id": "gpt2xl_temp09_001",
221	      "status": "done",
222	      "acc_4class": {"random_forest": 0.8542, "logistic_regression": 0.8155, "rf_ci": [0.843, 0.8653]},
223	      "acc_3class": {"random_forest": 0.820, "rf_ci": [0.806, 0.834]},
224	      "acc_3class_filtered": {"random_forest": 0.815, "rf_ci": [0.7999, 0.8298]},
225	      "pairwise_auc": {
226	        "random_forest": {"d0v1": 0.9963, "d0v2": 0.9992, "d0v3": 1.0000, "d1v2": 0.9367, "d1v3": 0.9947, "d2v3": 0.8815},
227	        "logistic_regression": {"d0v1": 0.9840, "d0v2": 0.9998, "d0v3": 1.0000, "d1v2": 0.8903, "d1v3": 0.9824, "d2v3": 0.8183}
228	      },
229	      "feature_importance": {
230	        "p90_ppl": 0.2633, "mean_surprisal": 0.1479, "p75_ppl": 0.1461, "var_surprisal": 0.1212,
231	        "p50_ppl": 0.0567, "type_token_ratio": 0.0300, "p25_ppl": 0.0298, "entropy_of_surprisal": 0.0297,
232	        "hapax_ratio": 0.0249, "rep_2gram": 0.0215, "p10_ppl": 0.0209, "rep_3gram": 0.0197,
233	        "trigram_entropy": 0.0192, "rep_4gram": 0.0181, "bigram_entropy": 0.0173, "skewness_ppl": 0.0171,
234	        "kurtosis_ppl": 0.0168, "mean_ppl": 0.0000, "var_ppl": 0.0000
235	      },
236	      "top5_features": ["p90_ppl", "mean_surprisal", "p75_ppl", "var_surprisal", "p50_ppl"],
237	      "finetune_losses": {"depth_0": 2.5498, "depth_1": 1.6972, "depth_2": 1.2922},
238	      "code_contamination_narrow": {"d0": 0.004, "d1": 0.008, "d2": 0.016, "d3": 0.015},
239	      "feature_trajectory": {
240	        "available": false,
241	        "note": "features.jsonl not saved during pipeline; rerun extract_features.py to generate"
242	      }
243	    },
244	    "gpt2xl_topk50": {
245	      "model": "GPT-2-XL",
246	      "strategy": "topk_k50",
247	      "experiment_id": "gpt2xl_topk50_001",
248	      "status": "running",
249	      "placeholder": true
250	    }
251	  }
252	}
253	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa11acb6-7e8b-4df4-b007-32ae26e815aa",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "4db24328-36d3-4393-ab7d-6e426e69ca92",
  "sourceToolAssistantUUID": "fa11acb6-7e8b-4df4-b007-32ae26e815aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-23T10:20:25.452Z_

Now let me read the appendix in sections and the other artifact data files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4db24328-36d3-4393-ab7d-6e426e69ca92",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLE4F6Tma95PYWpfYAg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cea732fe-f161-4749-98a7-d9c3a3ab6fd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MEM8gnrXq3pZMnLjvzTSjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8760,
      "cache_read_input_tokens": 55372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8760,
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

_source line 35 · 2026-05-23T10:20:27.870Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Jzd3zWSiAEvFobTLR4VpHM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": 0,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cea732fe-f161-4749-98a7-d9c3a3ab6fd3",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLE4F6Tma95PYWpfYAg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56abb7b7-88e6-426f-8747-13c1dceeaf00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MEM8gnrXq3pZMnLjvzTSjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8760,
      "cache_read_input_tokens": 55372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8760,
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

### Tool result

_source line 36 · 2026-05-23T10:20:27.879Z_

<details><summary>↩ Tool result · `toolu_01Jzd3zWSiAEvFobTLR4VpHM`</summary>

```text
0	\section{LoRA Fine-Tuning Protocol}
1	\label{app:lora_protocol}
2	
3	Table~\ref{tab:lora_protocol} lists the full LoRA fine-tuning configuration used for recursive chain construction (\S\ref{sec:method:benchmark}).
4	At each depth $k$, a fresh LoRA adapter is initialized on the base model and trained on $\mathcal{D}_{k-1}$; adapters are not inherited across depths.
5	The HuggingFace Trainer default linear decay schedule is used with no warmup.
6	Target modules are model-specific: \texttt{query\_key\_value} (Pythia), \texttt{att\_proj} (OLMo), and \texttt{c\_attn} (GPT-2~XL).
7	Cross-scale 7--8B experiments (Appendix~\ref{app:cross_scale_full}) use QLoRA (4-bit NF4) with $r{=}16$, $\alpha{=}32$; the 14B model uses FP16 LoRA with the same rank and scaling.
8	
9	\begin{table}[h]
10	\centering
11	\small
12	\caption{LoRA fine-tuning hyperparameters for the primary 1--1.5B benchmark. Identical across all three model families and all depth levels.}
13	\label{tab:lora_protocol}
14	\begin{tabular}{@{}ll@{}}
15	\toprule
16	Parameter & Value \\
17	\midrule
18	LoRA rank $r$ & 16 \\
19	LoRA alpha $\alpha$ & 32 \\
20	LoRA dropout & 0.05 \\
21	Bias & none \\
22	Epochs per depth & 3 \\
23	Learning rate & $2 \times 10^{-4}$ \\
24	LR schedule & linear decay (no warmup) \\
25	Batch size (effective) & 16 ($8 \times 2$ grad.\ accum.) \\
26	Max sequence length & 512 tokens \\
27	Precision & bfloat16 \\
28	Adapter init & from scratch (base model) \\
29	Seed & 42 (primary), 43 (replication) \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	
34	\section{Additional Results}
35	\label{app:additional}
36	
37	\subsection{Top-$k$ Feature Trajectories}
38	\label{app:topk_trajectories}
39	
40	Figure~\ref{fig:feature_trajectory} shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
41	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
42	Concretely, the d0$\to$d1 drop in \texttt{p90\_ppl} under top-$k$ is 78\% (vs.\ 87\% for nucleus), and the d2$\to$d3 reduction is 31\% (vs.\ 39\% for nucleus).
43	Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.
44	
45	\subsection{Permutation Importance}
46	\label{app:permutation}
47	
48	To verify that the Gini-based importance rankings in \S\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.
49	The top-2 features are stable across measures: \texttt{p90\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \texttt{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \texttt{p75\_ppl} displaces \texttt{var\_surprisal} to rank 3).
50	Kendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).
51	Pairwise Spearman correlations are: SHAP--Gini $\rho{=}0.93$, SHAP--permutation $\rho{=}0.84$, Gini--permutation $\rho{=}0.76$.
52	Per-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical; the top features are therefore robust to the choice of importance measure at the aggregate level, though per-cell rankings exhibit model-dependent variation.
53	
54	\subsection{Conditional Permutation Importance under Multicollinearity}
55	\label{app:conditional_pi}
56	
57	With 14--16 of 19 features exhibiting VIF${>}$10 (\S\ref{sec:atlas:features}), standard permutation importance may inflate contributions of correlated features: permuting one member of a collinear set allows others to compensate, masking true individual effects.
58	We compute conditional permutation importance (CPI) \citep{strobl2008_conditional}, which permutes each feature \emph{within strata defined by its correlated partners}, isolating the unique contribution after controlling for multicollinearity.
59	
60	\paragraph{Setup.}
61	CPI is computed on all 9 model$\times$strategy cells.
62	For each cell, 1{,}000 bootstrap resamples produce a rank distribution per feature; the 95\% bootstrap CI width quantifies rank stability (width $\leq 1.0$ indicates near-invariant rankings across resamples).
63	
64	\paragraph{Results.}
65	Table~\ref{tab:conditional_pi} summarizes the top-5 features by mean CPI across cells.
66	\texttt{var\_surprisal} (avg rank 1.4, CPI\,=\,0.260) and \texttt{p90\_ppl} (avg rank 1.7, CPI\,=\,0.238) are the top-2 in 8/9 cells, with bootstrap rank CI widths of 0.44 and 0.22---both $\leq 0.5$, indicating near-invariant rankings across resamples.
67	Ranks 3--5 are \texttt{p75\_ppl} (CPI\,=\,0.063, CI width\,=\,0.78), \texttt{p50\_ppl} (0.016, width\,=\,2.67), and a cell-dependent set (\texttt{p25\_ppl} or \texttt{mean\_ppl}); rank stability decreases beyond the top-2, with CI widths of 2.7--3.7 for ranks 4--5.
68	
69	\begin{table}[h]
70	\centering
71	\small
72	\caption{Conditional permutation importance aggregated across 9 model$\times$strategy cells (1{,}000 bootstrap resamples). Avg Rank and Avg CPI: means over cells. Rank CI Width: mean 95\% bootstrap CI width for the rank. Bottom rows: feature-family averages.}
73	\label{tab:conditional_pi}
74	\resizebox{\columnwidth}{!}{%
75	\begin{tabular}{@{}lccc@{}}
76	\toprule
77	Feature / Family & Avg Rank & Avg CPI & Rank CI Width \\
78	\midrule
79	\texttt{var\_surprisal} & 1.4 & 0.260 & 0.44 \\
80	\texttt{p90\_ppl} & 1.7 & 0.238 & 0.22 \\
81	\texttt{p75\_ppl} & 3.1 & 0.063 & 0.78 \\
82	\texttt{p50\_ppl} & 5.0 & 0.016 & 2.67 \\
83	\texttt{p25\_ppl}$^\dagger$ & 5.8 & 0.012 & 3.67 \\
84	\texttt{mean\_ppl}$^\dagger$ & 6.3 & 0.008 & 3.44 \\
85	\midrule
86	Surprisal family & 7.3 & 0.089 & --- \\
87	Perplexity family & 7.5 & 0.039 & --- \\
88	Lexical family & 9.7 & 0.004 & --- \\
89	\bottomrule
90	\multicolumn{4}{@{}l}{\footnotesize $^\dagger$Rank 5--6 varies by cell; \texttt{trigram\_entropy} appears in 1 cell.}
91	\end{tabular}}
92	\end{table}
93	
94	Two exceptions exist among GPT-2~XL cells: in temperature sampling, \texttt{p90\_ppl} (CPI\,=\,0.419) exceeds \texttt{var\_surprisal} (0.093) while both remain in the top-2; in top-$k$ sampling, \texttt{p90\_ppl} (0.475) and \texttt{p75\_ppl} (0.127) push \texttt{var\_surprisal} to rank~3 (0.037), the only cell where it exits the top-2.
95	Both reversals are consistent with the Gini rankings for these cells (Table~\ref{tab:feature_importance}).
96	
97	At the family level, surprisal (avg CPI\,=\,0.089, rank\,=\,7.3) and perplexity (0.039, rank\,=\,7.5) are closely matched, while lexical features (0.004, rank\,=\,9.7) contribute minimally---consistent with the group ablation in \S\ref{sec:atlas:features}.
98	
99	\paragraph{Consistency with Gini rankings.}
100	CPI and Gini rankings agree on the dominant feature (\texttt{var\_surprisal} or \texttt{p90\_ppl}) in 8/9 cells; the sole disagreement (GPT-2~XL top-$k$) involves a swap between rank-2 and rank-3 features.
101	Bootstrap rank CI widths $\leq 0.5$ for the top-2 features confirm that these rankings are not artifacts of collinearity or resampling variability.
102	Controlling for multicollinearity via conditional permutation corroborates the Gini- and SHAP-based importance hierarchy reported in the main text.
103	
104	\subsection{Feature Trajectories}
105	\label{app:feature_trajectories}
106	
107	\begin{figure}[h]
108	\centering
109	\includegraphics[width=\columnwidth]{figures/fig_feature_trajectory.pdf}
110	\caption{Feature trajectories across depths $d{=}0$ to $d{=}3$, stratified by model (columns: Pythia-1.4B, OLMo-1B, GPT-2~XL) and strategy (line style). Five features are shown per panel: \texttt{p90\_ppl}, \texttt{var\_surprisal}, \texttt{mean\_surprisal}, \texttt{p75\_ppl}, and TTR, normalized to depth~0. The $d{=}0 \to d{=}1$ gap exceeds all subsequent inter-depth gaps.}
111	\label{fig:feature_trajectory}
112	\end{figure}
113	
114	\subsection{Per-Class Recall}
115	\label{app:per_class}
116	
117	Table~\ref{tab:per_class_recall} reports per-class recall across all 9 atlas cells (4-class in-distribution, 5-fold CV).
118	Depth~0 recall exceeds 97\% uniformly.
119	Among generated depths, d2 is the hardest class in every cell; the deficit is most pronounced under top-$k$ sampling (46--53\%), where vocabulary truncation removes the tail tokens that carry depth-discriminative signal.
120	
121	\begin{table}[h]
122	\centering
123	\small
124	\caption{Per-class recall (\%) for all 9 atlas cells. d2 is the lowest-recall class in every cell. Boldface marks the highest d2 recall.}
125	\label{tab:per_class_recall}
126	\begin{tabular}{@{}lcccc@{}}
127	\toprule
128	Cell & d0 & d1 & d2 & d3 \\
129	\midrule
130	Pythia, nuc.       & 99.3 & 81.9 & 59.2 & 74.4 \\
131	Pythia, $\tau$     & 99.2 & 79.9 & 56.0 & 72.1 \\
132	Pythia, top-$k$    & 98.7 & 71.6 & 44.2 & 60.9 \\
133	OLMo, nuc.         & 97.8 & 82.1 & 60.6 & 75.3 \\
134	OLMo, $\tau$       & 99.3 & 87.1 & 65.6 & 77.1 \\
135	OLMo, top-$k$      & 99.2 & 80.9 & 50.4 & 67.2 \\
136	GPT-2~XL, nuc.     & 98.5 & 87.4 & 72.8 & 78.5 \\
137	GPT-2~XL, $\tau$   & 99.0 & 91.1 & \textbf{73.0} & 80.5 \\
138	GPT-2~XL, top-$k$  & 98.7 & 81.3 & 54.8 & 68.4 \\
139	\bottomrule
140	\end{tabular}
141	\end{table}
142	
143	\subsection{Confusion Matrices}
144	\label{app:confusion_matrices}
145	
146	\begin{figure}[h]
147	\centering
148	\includegraphics[width=\columnwidth]{figures/fig_confusion_matrix.pdf}
149	\caption{Confusion matrices: best in-distribution (GPT-2 XL temp, 85.9\%) and best LOO transfer (OLMo, 69.2\%). d0 recall ${>}$99\%; errors spread to d1--d3 under transfer.}
150	\label{fig:confusion_matrix}
151	\end{figure}
152	
153	\subsection{Cross-Strategy Transfer Details}
154	\label{app:cross_strategy}
155	
156	\begin{table}[h]
157	\centering
158	\small
159	\caption{Cross-strategy transfer (leave-one-out). Chance = 25\% / 33\% (d1--d3). d0 recall $\geq$89\% inflates headline; d1--d3 mean: 45.9\%.}
160	\label{tab:cross_strategy}
161	\begin{tabular}{lccc}
162	\toprule
163	Holdout & Pythia & OLMo & GPT-2 XL \\
164	 & Acc (\%) & Acc (\%) & Acc (\%) \\
165	\midrule
166	nucleus & \textbf{69.4} & \textbf{65.4} & \textbf{59.9} \\
167	temp ($\tau{=}0.9$) & 62.8 & 58.2 & 56.1 \\
168	top-$k$ ($k{=}50$) & 51.5 & 54.9 & 53.6 \\
169	\bottomrule
170	\end{tabular}
171	\end{table}
172	
173	\subsection{Accumulation Pairwise AUC}
174	\label{app:accumulation_auc}
175	
176	Table~\ref{tab:accum_auc} reports pairwise AUC for the six accumulation cells (3 models $\times$ 2 mixing ratios; GPT-2~XL and Pythia use nucleus, OLMo uses temperature 0.9).
177	At 25\% mixing, all three cells preserve $\mathrm{EDD}_{0.70}{=}3$.
178	At 50\% mixing, GPT-2~XL nucleus is the sole failure: d2v3 AUC\,=\,0.695, marginally below the 0.70 threshold (0.55\,pp).
179	
180	\begin{table}[h]
181	\centering
182	\small
183	\caption{Pairwise AUC under accumulation (GPT-2~XL/Pythia: nucleus; OLMo: temp 0.9; binary RF, 5-fold CV). Bold: $\mathrm{EDD}_{0.70}$ boundary failure.}
184	\label{tab:accum_auc}
185	\begin{tabular}{@{}llccc@{}}
186	\toprule
187	Model & Mix & d0v1 & d1v2 & d2v3 \\
188	\midrule
189	GPT-2~XL & 25\% & 1.000 & 0.876 & 0.726 \\
190	 & 50\% & 1.000 & 0.831 & \textbf{0.695} \\
191	Pythia & 25\% & 1.000 & 0.843 & 0.749 \\
192	 & 50\% & 1.000 & 0.793 & 0.716 \\
193	OLMo & 25\% & 1.000 & 0.862 & 0.759 \\
194	 & 50\% & 1.000 & 0.817 & 0.726 \\
195	\bottomrule
196	\end{tabular}
197	\end{table}
198	
199	\subsection{DCOL Iteration Details}
200	\label{app:dcol_iterations}
201	
202	Table~\ref{tab:dcol_iterations} summarizes all six DCOL iterations.
203	DeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.
204	
205	\begin{table}[h]
206	\centering
207	\small
208	\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.7\%.}
209	\label{tab:dcol_iterations}
210	\resizebox{\columnwidth}{!}{%
211	\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}
212	\toprule
213	Ver. & Backbone & Config & Outcome \\
214	\midrule
215	v1 & DeBERTa & FT, m\_lr $10^{-3}$ & Embed.\ collapse (31.5\%) \\
216	v2 & DeBERTa & FT, m\_lr $10^{-4}$ & OOM \\
217	v3 & DeBERTa & FT, m\_lr $10^{-4}$ & Forgetting + OOM \\
218	v4 & DeBERTa & LoRA, m\_lr $10^{-3}$ & Embed.\ collapse \\
219	v5 & DeBERTa & LoRA, m\_lr $10^{-4}$ & NaN gradients \\
220	v6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\% ($-$13.7pp) \\
221	\bottomrule
222	\end{tabular}}
223	\end{table}
224	
225	\subsection{Zero-Shot LLM Prompt Template}
226	\label{app:zeroshot_prompt}
227	
228	Both DeepSeek V3.2 and Qwen2.5-7B-Instruct use identical prompting.
229	The system message defines recursive generation depth with per-depth descriptions (depth~0: human-written; depth~1--3: successive LLM generation cycles) and lists expected textual patterns at each depth (vocabulary richness, repetition, coherence).
230	The user message presents the passage (truncated to ${\approx}$384 words) and requests a JSON response containing an integer depth prediction (0--3), a confidence score, and a one-sentence reasoning.
231	No in-context examples are provided.
232	
233	\begin{quote}
234	\small
235	\textbf{System:} ``You are an expert at detecting AI-generated text and estimating its generation depth. `Recursive generation depth' refers to how many times a text has been through an LLM generation cycle: Depth~0: Original human-written text [\ldots] Depth~3: Text generated by an LLM given depth-2 text as input. Key patterns by depth: Depth~0 (human): Rich vocabulary [\ldots] Depth~3 (third-gen): Noticeable repetition, formulaic structure [\ldots]''
236	
237	\textbf{User:} ``Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3). TEXT: \{text\}. Respond with ONLY a JSON object: \{\texttt{"depth"}: $\langle$int 0--3$\rangle$, \texttt{"confidence"}: $\langle$float 0--1$\rangle$, \texttt{"reasoning"}: $\langle$str$\rangle$\}''
238	\end{quote}
239	
240	\subsection{Temperature Robustness}
241	\label{app:multi_tau}
242	
243	The cross-strategy results in \S\ref{sec:gen:crossstrategy} use a single temperature ($\tau{=}0.9$).
244	To test whether depth signal generalizes across temperatures, we repeat the classification pipeline at $\tau \in \{0.5, 0.7, 0.9, 1.1\}$ on Pythia-1.4B.
245	
246	\paragraph{Within-$\tau$ robustness.}
247	For $\tau \in [0.5, 0.9]$, d1-vs-d2 AUC exceeds 0.80 (peak 0.851 at $\tau{=}0.7$, comparable to nucleus $p{=}0.95$'s 0.861) and 4-class accuracy ranges from 75.4\% to 77.3\% (Table~\ref{tab:multi_tau_within}); the depth signal is therefore not an artifact of a single temperature.
248	The same top-5 features (\texttt{var\_surprisal}, \texttt{p90\_ppl}, \texttt{mean\_ppl}, \texttt{mean\_surprisal}, \texttt{p75\_ppl}) dominate across all $\tau$ values with only minor rank-order variation.
249	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56abb7b7-88e6-426f-8747-13c1dceeaf00",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "2077b4af-2d12-4f24-8174-a50036308911",
  "sourceToolAssistantUUID": "56abb7b7-88e6-426f-8747-13c1dceeaf00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T10:20:28.888Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q3t26UZnR7MuooQTagXrt8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/monotonicity_scores.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2077b4af-2d12-4f24-8174-a50036308911",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLE4F6Tma95PYWpfYAg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e2a86da-6f27-4acc-851c-292c49f03ff3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MEM8gnrXq3pZMnLjvzTSjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8760,
      "cache_read_input_tokens": 55372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8760,
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

### Tool result

_source line 38 · 2026-05-23T10:20:28.894Z_

<details><summary>↩ Tool result · `toolu_01Q3t26UZnR7MuooQTagXrt8`</summary>

```text
1	See server: /root/autodl-tmp/recursive_gen_depth_est/artifacts/atlas/monotonicity_scores.json
2	
3	Key findings (Spearman rho, all p < 1e-100):
4	- var_surprisal: Pythia=-0.832, Pythia_t09=-0.840, OLMo=-0.834, GPT2XL=-0.874
5	- p90_ppl: Pythia=-0.824, Pythia_t09=-0.823, OLMo=-0.870, GPT2XL=-0.887
6	- mean_surprisal: Pythia=-0.760, Pythia_t09=-0.769, OLMo=-0.773, GPT2XL=-0.767
7	- p75_ppl: Pythia=-0.750, Pythia_t09=-0.760, OLMo=-0.772, GPT2XL=-0.759
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e2a86da-6f27-4acc-851c-292c49f03ff3",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "65dcb9a8-7da7-40c6-9f38-db7114c75ce8",
  "sourceToolAssistantUUID": "9e2a86da-6f27-4acc-851c-292c49f03ff3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T10:20:29.363Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BRAwgAE6ScpNQZxbJ5gMKG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/feature_consistency.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65dcb9a8-7da7-40c6-9f38-db7114c75ce8",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLE4F6Tma95PYWpfYAg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18b59bea-b39e-462a-b6a6-f593af02195e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MEM8gnrXq3pZMnLjvzTSjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8760,
      "cache_read_input_tokens": 55372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8760,
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

### Tool result

_source line 40 · 2026-05-23T10:20:29.367Z_

<details><summary>↩ Tool result · `toolu_01BRAwgAE6ScpNQZxbJ5gMKG`</summary>

```text
1	See server: /root/autodl-tmp/recursive_gen_depth_est/artifacts/atlas/feature_consistency.json
2	
3	Key findings:
4	- 3-way top-5 intersection: var_surprisal, p90_ppl, p75_ppl, mean_surprisal (4/6 features)
5	- 3-way Jaccard: 0.667
6	- Rank correlations: Pythia-GPT2XL rho=0.904, OLMo-GPT2XL rho=0.853, Pythia-OLMo rho=0.647 (all p<0.01)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18b59bea-b39e-462a-b6a6-f593af02195e",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "bf24b868-6dc4-4d58-b691-71097da6a57b",
  "sourceToolAssistantUUID": "18b59bea-b39e-462a-b6a6-f593af02195e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T10:20:29.881Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KzZMBLyYEdKzqjCQT1v6Mk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/heatmap_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf24b868-6dc4-4d58-b691-71097da6a57b",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLE4F6Tma95PYWpfYAg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12fc5c84-ccf5-4fc9-929a-b66a6301b3b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MEM8gnrXq3pZMnLjvzTSjY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8760,
      "cache_read_input_tokens": 55372,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8760
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 375,
          "cache_read_input_tokens": 55372,
          "cache_creation_input_tokens": 8760,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8760,
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

_source line 42 · 2026-05-23T10:20:29.887Z_

<details><summary>↩ Tool result · `toolu_01KzZMBLyYEdKzqjCQT1v6Mk`</summary>

```text
1	See server: /root/autodl-tmp/recursive_gen_depth_est/artifacts/atlas/heatmap_data.json
2	
3	3D matrix: 19 features x 4 models x 4 depths, z-scored for cross-feature comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12fc5c84-ccf5-4fc9-929a-b66a6301b3b5",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "1cbf3a10-fd59-42e6-8183-b5b15fd535c9",
  "sourceToolAssistantUUID": "12fc5c84-ccf5-4fc9-929a-b66a6301b3b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-23T10:20:33.916Z_

<details open><summary>🔧 Tool call — Read · `toolu_019tqKwKL1J4nGS38hHr4C6r`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": 250,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cbf3a10-fd59-42e6-8183-b5b15fd535c9",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLEZKpeYu3959jPj3fE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2b16ab2-3409-414e-8344-bdf905e439de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4p53rS8iLHK47dF1ghdzm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7113,
      "cache_read_input_tokens": 64132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7113,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 44 · 2026-05-23T10:20:33.923Z_

<details><summary>↩ Tool result · `toolu_019tqKwKL1J4nGS38hHr4C6r`</summary>

```text
250	
251	\paragraph{Collapse at $\tau{=}1.1$: memorization as prerequisite.}
252	At $\tau{=}1.1$, 4-class accuracy drops to 57.2\% and d1v2 AUC falls to 0.528.
253	Training loss reveals the mechanism: at low temperature ($\tau{=}0.5$), fine-tuning loss decreases steeply across recursive depths ($2.27 \to 0.42 \to 0.16$), a sign of rapid memorization of the model's own output.
254	At $\tau{=}1.1$, loss remains nearly flat ($2.27 \to 1.91 \to 1.85$); high-entropy output resists memorization, so depth-dependent distributional shifts do not accumulate.
255	This establishes \emph{memorization as a prerequisite} for detectable depth signal: recursive depth is discriminable only when successive fine-tuning iterations progressively reshape the output distribution.
256	
257	\paragraph{Cross-$\tau$ non-transferability.}
258	Leave-one-$\tau$-out transfer yields mean accuracy of 46.7\% with mean d1v2 AUC of 0.319 (Table~\ref{tab:multi_tau_cross}), worse than cross-strategy transfer (59.1\%; \S\ref{sec:gen:crossstrategy}).
259	Holdout $\tau{=}0.5$ produces inverted d1v2 AUC (0.176); different temperatures therefore produce surprisal distributions with incompatible shapes.
260	This extends the strategy-specificity finding: even within a single decoding family, the feature space is temperature-specific; strategy-conditioned classifiers are therefore necessary.
261	
262	\paragraph{Ecological validity.}
263	On WikiText-103 (546 editorial passages), all three model-specific RF classifiers achieve $\geq$98.5\% d0 accuracy despite $+$621\% domain shift in mean perplexity, partly an easy case, as WikiText's higher perplexity places it farther from d1--d3 in feature space.
264	On noisier web-crawl data (5{,}000 C4 passages), FPR ranges from 4.7\% (OLMo) to 22.4\% (GPT-2~XL), concentrated in template/SEO content with high n-gram repetition (Table~\ref{tab:calibration}); deployment on heterogeneous web data requires model-specific calibration.
265	
266	\begin{table}[h]
267	\centering
268	\small
269	\caption{Within-$\tau$ 4-class classification (Pythia-1.4B, 5-fold CV, independent pipeline run). d$i$v$j$: pairwise AUC for depth $i$ vs.\ depth $j$. The $\tau{=}0.9$ accuracy (75.9\%) differs from the main atlas (76.8\%, Table~\ref{tab:main_matrix}) due to separate generation and LoRA training runs.}
270	\label{tab:multi_tau_within}
271	\resizebox{\columnwidth}{!}{%
272	\begin{tabular}{@{}lcccc@{}}
273	\toprule
274	$\tau$ & 4-class acc (\%) & d1v2 AUC & d0v1 AUC & d2v3 AUC \\
275	\midrule
276	0.5 & 77.3 & 0.842 & 0.996 & 0.764 \\
277	0.7 & 75.4 & 0.851 & 0.997 & 0.720 \\
278	0.9 & 75.9 & 0.808 & 0.991 & 0.781 \\
279	1.1 & 57.2 & 0.528 & 0.988 & 0.599 \\
280	\bottomrule
281	\end{tabular}}
282	\end{table}
283	
284	\begin{table}[h]
285	\centering
286	\small
287	\caption{Cross-$\tau$ leave-one-out transfer (Pythia-1.4B). Train on three temperatures, test on the held-out one.}
288	\label{tab:multi_tau_cross}
289	\begin{tabular}{@{}lcc@{}}
290	\toprule
291	Holdout & Acc (\%) & d1v2 AUC \\
292	\midrule
293	$\tau{=}0.5$ & 52.2 & 0.176 \\
294	$\tau{=}0.7$ & 41.0 & 0.299 \\
295	$\tau{=}0.9$ & 46.4 & 0.277 \\
296	$\tau{=}1.1$ & 47.1 & 0.525 \\
297	\midrule
298	Mean & 46.7 & 0.319 \\
299	\bottomrule
300	\end{tabular}
301	\end{table}
302	
303	\subsection{Feature Overlap Analysis}
304	\label{app:feature_overlap}
305	
306	We probe whether end-to-end PLM representations capture the same depth signals as our statistical features via linear probing of [CLS] representations from DeBERTa-v3-base and RoBERTa-base.
307	PLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics; \texttt{var\_surprisal} and \texttt{p90\_ppl} yield negative $R^2$ under linear probing; these features are not linearly accessible in the pretrained representation space.
308	This confirms that the 20pp accuracy gap between feature-based and end-to-end methods (\S\ref{app:e2e}) stems from complementary, not redundant, representations: PLMs capture lexical patterns while the targeted statistical features capture distributional tail properties that constitute the dominant depth markers.
309	
310	\subsection{End-to-End Learning}
311	\label{app:e2e}
312	
313	DeBERTa-v3-base \cite{he2021_deberta_v3} and RoBERTa-base \cite{liu2019_roberta} finetuned end-to-end achieve 58.3\% ($\pm$4.7\%) and 59.5\% ($\pm$3.2\%) respectively, lagging the RF baseline (78.7\%) by 20.4pp and 19.2pp.
314	The 1.2pp inter-backbone gap rules out architecture bias; Table~\ref{tab:e2e_detail} shows both backbones share the same failure mode (high d0 F1, $>$0.94, but collapsed d1/d2 performance, F1 $\leq$ 0.42), while RF achieves 0.596 d2 recall, a $>$2$\times$ advantage at the hardest depth class.
315	
316	\begin{table}[h]
317	\centering
318	\small
319	\caption{Per-class performance for end-to-end PLM classifiers vs.\ RF baseline (Pythia-1.4B nucleus). PLM columns report F1; RF d2 column reports recall (the class with the largest PLM--RF gap). Both PLM backbones share the same failure pattern: collapsed d1/d2 scores despite adequate d0/d3.}
320	\label{tab:e2e_detail}
321	\resizebox{\columnwidth}{!}{%
322	\begin{tabular}{@{}lccccc@{}}
323	\toprule
324	Method & Acc (\%) & d0 & d1 & d2 & d3 \\
325	\midrule
326	DeBERTa-v3 & 58.3\,$\pm$\,4.7 & .947 & .378 & .247 & .656 \\
327	RoBERTa-base & 59.5\,$\pm$\,3.2 & .958 & .416 & .261 & .647 \\
328	\midrule
329	RF (19 feat.) & 78.7 & --- & --- & .596$^\dagger$ & --- \\
330	\bottomrule
331	\multicolumn{6}{@{}l}{\footnotesize $^\dagger$Recall; shown for the depth class with the largest PLM--RF gap.}
332	\end{tabular}}
333	\end{table}
334	
335	\paragraph{Feature space divergence.}
336	SHAP TreeExplainer analysis confirms that perplexity and surprisal features account for 88.8\% of RF's total contribution.
337	Three independent importance measures (SHAP, Gini, and permutation) show strong concordance (Kendall's $W{=}0.90$, $p{<}0.005$; pairwise Spearman $\rho$: SHAP--Gini $0.93$, SHAP--permutation $0.84$; \S\ref{app:permutation}), with \texttt{p90\_ppl} appearing in the SHAP top-2 in 9/9 cells and \texttt{var\_surprisal} in 8/9.
338	Linear probing of PLM [CLS] representations yields negative $R^2$ for both \texttt{var\_surprisal} and \texttt{p90\_ppl} (\S\ref{app:feature_overlap}); pretrained representations lack the linear structure needed to recover perplexity tail statistics, a systematic representational gap rather than a backbone-specific artifact.
339	
340	DCOL \cite{cloc2025} reached 64.5\% (\S\ref{app:dcol_iterations}); all end-to-end approaches (58--65\%) underperform feature-based methods; depth estimation therefore benefits from targeted statistical features that capture distributional tail properties absent from PLM representations.
341	This comparison is bounded by backbone scale ($\leq$125M parameters); whether larger PLMs (e.g., 7B+) can close the gap via richer internal representations remains an open question.
342	
343	\subsection{Domain Bias Analysis}
344	\label{app:domain_bias}
345	
346	To assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.
347	
348	\paragraph{Methodological note.}
349	An initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\%, seed-group prediction 20.8\%).
350	We discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.
351	The results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.
352	
353	\paragraph{Sub-A: Standard CV.}
354	Five-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\% to 82\% across the 9 atlas cells (up to 2.5$\times$ above the 33.3\% chance level); depth signal is therefore the dominant classification factor.
355	
356	\paragraph{Sub-B: LOGO evaluation.}
357	We assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.
358	LOGO mean accuracy is 72.1\% (range 59.5--81.6\%), matching standard CV (72.0\%) within noise (before fix: 64.0\%, reflecting the depth--group confound).
359	Per-cell fold standard deviations range from 0.4pp to 1.4pp; cross-group generalization is therefore as reliable as within-group classification.
360	
361	\paragraph{Sub-C: Negative control.}
362	We train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\%).
363	Depth prediction accuracy averages 72.0\%; seed-group prediction averages 10.2\%, indistinguishable from chance (before fix: 20.8\%, inflated by the depth--group confound).
364	The depth-to-seed-group accuracy ratio is 7.1$\times$; the feature representation therefore encodes depth but not seed-article identity.
365	
366	Taken together, these results show that seed-article grouping has no measurable effect on depth estimation after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.
367	
368	\subsection{Wild-Data Calibration}
369	\label{app:calibration}
370	
371	Table~\ref{tab:calibration} reports d0 accuracy and false positive rate (FPR) for all three model-specific nucleus RF classifiers on two out-of-distribution human-text corpora: WikiText-103 (546 editorial passages) and C4 (5{,}000 web-crawl passages, crawled 2019--2020; pre-LLM deployment).
372	
373	\begin{table}[h]
374	\centering
375	\small
376	\caption{Wild-data d0 accuracy and FPR for nucleus RF classifiers. All passages are human-written (true d0). FPR = fraction misclassified as d1+. 95\% Wilson CIs computed for C4 ($n{=}5{,}000$).}
377	\label{tab:calibration}
378	\resizebox{\columnwidth}{!}{%
379	\begin{tabular}{@{}llrccc@{}}
380	\toprule
381	Model & Source & $n$ & d0 (\%) & FPR (\%) & 95\% Wilson CI \\
382	\midrule
383	Pythia-1.4B & WikiText & 546 & 100.0 & 0.0 & --- \\
384	 & C4 & 5{,}000 & 79.8 & 20.2 & [19.1, 21.3] \\
385	\addlinespace
386	GPT-2~XL & WikiText & 546 & 99.3 & 0.7 & --- \\
387	 & C4 & 5{,}000 & 77.6 & 22.4 & [21.3, 23.6] \\
388	\addlinespace
389	OLMo-1B & WikiText & 546 & 98.5 & 1.5 & --- \\
390	 & C4 & 5{,}000 & 95.3 & 4.7 & [4.2, 5.3] \\
391	\bottomrule
392	\end{tabular}}
393	\end{table}
394	
395	On WikiText-103, all three classifiers achieve $\geq$98.5\% d0 accuracy; editorial text is therefore reliably distinguished from recursive generations across model families.
396	On C4, FPR varies sharply: OLMo (4.7\%) vs.\ Pythia (20.2\%) and GPT-2~XL (22.4\%).
397	C4 misclassifications concentrate in template and SEO content with elevated repetition features (\texttt{rep\_3gram} $+$37\%, \texttt{rep\_4gram} $+$75\% vs.\ correctly classified d0 passages), rather than in random noise.
398	The model gap likely reflects training data composition: OLMo (trained on Dolma, which includes diverse web data) produces d0 features more tolerant of web-crawl variation, while Pythia and GPT-2~XL (trained primarily on Wikipedia/WebText) map template-heavy content into the d1+ region.
399	Among C4 false positives for GPT-2~XL, predictions distribute as d1 (9.0\%), d2 (3.7\%), d3 (9.6\%); for OLMo, d1 (2.9\%), d2 (0.5\%), d3 (1.3\%). The non-uniform depth distribution suggests the classifier maps specific repetition patterns to particular depth signatures rather than producing random misclassifications.
400	
401	\paragraph{Threshold calibration.}
402	A pooled RF classifier (trained on all three families' nucleus data) achieves ECE\,=\,0.052 on in-distribution data; Platt scaling and isotonic regression yield no improvement; probability estimates are already well calibrated.
403	The high FPR on web-crawl data is therefore a decision-threshold problem, not a probability calibration defect.
404	Applying a confidence threshold $P(\mathrm{d0}) \geq 0.15$ to the pooled classifier reduces its C4 FPR from 33.4\% (not shown in Table~\ref{tab:calibration}) to 2.8\%, at a cost of only $-$0.3\,pp balanced accuracy (78.0\%$\to$77.7\%).
405	The $P(\mathrm{d0})$ distribution is bimodal: 67\% of samples exceed 0.95 (high-confidence d0), while 33\% fall in the 0.15--0.30 uncertainty zone; the threshold separates these modes cleanly.
406	Wild-data FPR is thus an operational threshold choice rather than a fundamental limitation, though the optimal threshold is domain-dependent.
407	
408	\paragraph{Additional web corpora.}
409	Evaluating the pooled classifier on FineWeb (10{,}000 passages) and RedPajama (10{,}000 passages) yields raw FPR of 17.2\% and 15.5\%, respectively, both below C4 (34.0\%), likely reflecting less template-heavy content in these corpora.
410	Posterior-threshold calibration ($P(\mathrm{d0}) \geq 0.10$) reduces FPR to 0.1\% (FineWeb) and 7.0\% (RedPajama); across all three web-crawl corpora, calibrated FPR remains ${\leq}$7\%.
411	
412	\subsection{Downstream Curation PoC (Inconclusive)}
413	\label{app:curation_poc}
414	
415	To assess whether depth estimation translates to actionable data curation, we conduct a proof-of-concept downstream evaluation.
416	We fine-tune Pythia-410M with LoRA ($r{=}16$, $\alpha{=}32$) for 3 epochs on 8 data conditions derived from the Pythia nucleus depth-estimation corpus, repeating each condition over 5 random seeds.
417	Conditions vary the selection mechanism (RF-predicted depth, oracle depth, random subsampling) and stringency (strict $\approx$25\%, moderate $\approx$50\%, soft threshold).
418	Table~\ref{tab:curation_poc} reports per-condition perplexity; Table~\ref{tab:curation_comparisons} reports pairwise contrasts.
419	
420	\begin{table}[h]
421	\centering
422	\small
423	\caption{Curation PoC: per-condition perplexity (Pythia-410M LoRA, 5 seeds). $\Delta$ is signed so that positive values indicate lower (better) perplexity than unfiltered. $d_z$: Cohen's paired effect size. $^*$\,: $p<0.05$ (paired $t$-test vs.\ unfiltered).}
424	\label{tab:curation_poc}
425	\resizebox{\columnwidth}{!}{%
426	\begin{tabular}{@{}lcccccc@{}}
427	\toprule
428	Condition & Mean PPL & Std & $n$ & $\Delta$ vs Unfilt. & $p$ & $d_z$ \\
429	\midrule
430	unfiltered        & 15.776 & 0.066 & 10{,}000 & ---      & ---   & ---      \\
431	rf\_soft          & 15.733 & 0.038 &  4{,}422 & +0.043   & 0.407 &  0.41    \\
432	rf\_moderate      & 15.756 & 0.056 &  4{,}940 & +0.021   & 0.492 &  0.34    \\
433	rf\_strict        & 15.810 & 0.061 &  2{,}496 & $-$0.034 & 0.607 & $-$0.25  \\
434	oracle\_moderate  & 15.809 & 0.103 &  5{,}000 & $-$0.033 & 0.485 & $-$0.34  \\
435	oracle\_strict    & 15.879 & 0.128 &  2{,}500 & $-$0.103 & 0.216 & $-$0.66  \\
436	random\_soft      & 16.062 & 0.079 &  4{,}422 & $-$0.286 & ${<}$0.001$^*$ & $-$2.77  \\
437	random\_moderate  & 15.998 & 0.090 &  4{,}940 & $-$0.222 & 0.028$^*$ & $-$1.50  \\
438	random\_strict    & 16.239 & 0.165 &  2{,}496 & $-$0.463 & 0.013$^*$ & $-$1.89  \\
439	\bottomrule
440	\end{tabular}}
441	\end{table}
442	
443	\begin{table}[h]
444	\centering
445	\small
446	\caption{Pairwise comparisons (paired $t$-test, 5 seeds). $^*$\,: $p<0.05$; $^{**}$\,: $p<0.01$.}
447	\label{tab:curation_comparisons}
448	\resizebox{\columnwidth}{!}{%
449	\begin{tabular}{@{}lccc@{}}
450	\toprule
451	Comparison & $\Delta$ PPL & $t$ & $p$ \\
452	\midrule
453	rf\_strict vs random\_strict     & 0.429 & $-$7.05 & 0.002$^{**}$ \\
454	rf\_moderate vs random\_moderate & 0.242 & $-$3.77 & 0.020$^*$    \\
455	rf\_soft vs random\_soft         & 0.328 & $-$17.98 & ${<}$0.001$^{**}$ \\
456	rf\_soft vs unfiltered           & 0.043 &    0.93 & 0.407        \\
457	\bottomrule
458	\end{tabular}}
459	\end{table}
460	
461	For the binary task of identifying low-depth passages (d0 vs.\ d1--d3, evaluated on the same Pythia nucleus corpus with 5-fold CV), RF-based depth filtering achieves F1\,=\,0.997, substantially outperforming a simple perplexity-threshold baseline (F1\,=\,0.845); the multi-feature representation provides discriminative value beyond raw perplexity.
462	However, the primary comparison (RF-filtered vs.\ unfiltered, $p > 0.4$) is non-significant; the significant RF-vs-random contrasts ($p < 0.02$) involve multiple pairwise comparisons that were not corrected for multiplicity.
463	
464	\subsection{Reference Model Ablation}
465	\label{app:ref_ablation}
466	
467	Table~\ref{tab:ref_ablation} ablates the reference model used for feature extraction on Pythia-1.4B nucleus text (d0--d3, 5-fold CV).
468	Self-reference (Pythia-1.4B) yields 78.6\%; switching to a cross-architecture reference degrades accuracy by 4--11\,pp, confirming that reference-generator alignment amplifies depth signal.
469	
470	\begin{table}[h]
471	\centering
472	\caption{Reference model ablation. Classification accuracy (5-fold CV) on Pythia-1.4B generated text (nucleus, d0--d3) using different reference models for feature extraction.}
473	\label{tab:ref_ablation}
474	\resizebox{\columnwidth}{!}{%
475	\begin{tabular}{@{}lcc@{}}
476	\toprule
477	Reference Model & Architecture & Accuracy (\%) \\
478	\midrule
479	Pythia-1.4B (self) & GPT-NeoX & 78.6 $\pm$ 0.6 \\
480	OLMo-1B (cross) & OLMo & 74.5 $\pm$ 0.7 \\
481	GPT-2~XL (cross) & GPT-2 & 67.3 $\pm$ 0.7 \\
482	\bottomrule
483	\end{tabular}}
484	\end{table}
485	
486	\subsection{Cross-Scale Full Results}
487	\label{app:cross_scale_full}
488	
489	This section provides the full cross-scale analysis summarized in \S\ref{sec:gen:crossscale}.
490	We extend the benchmark to two 7--8B models (Qwen2.5-7B-Instruct \cite{qwen2.5}, Llama-3.1-8B-Instruct \cite{llama3}) and one 14B model (Qwen2.5-14B).
491	The 7--8B models use 4-bit NF4 QLoRA fine-tuning with nucleus sampling ($p{=}0.95$, 500 samples per depth, depths $d \in \{0, 1, \ldots, 5\}$).
492	The 14B model uses clean FP16 LoRA fine-tuning across all three decoding strategies (nucleus, temperature $\tau{=}0.9$, top-$k$ $k{=}50$; 5{,}000 samples per depth, depths $d \in \{0, 1, 2, 3\}$).
493	Feature extraction for 1--8B models uses Pythia-1.4B as reference; Qwen2.5-14B is evaluated under both self-reference and cross-reference (Pythia-1.4B) to disentangle reference-model artifacts from scale effects (see paragraph~5 below).
494	
495	\paragraph{Scale comparison.}
496	Table~\ref{tab:cross_scale} contrasts the 7--14B models with the three 1--1.5B models on matched evaluation (depths 0--3).
497	The 14B model is tested across all three decoding strategies; the 7--8B models use nucleus sampling only.
498	
499	\begin{table}[h]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2b16ab2-3409-414e-8344-bdf905e439de",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "c391fbe6-14ba-4a8a-afea-13d0924bc840",
  "sourceToolAssistantUUID": "f2b16ab2-3409-414e-8344-bdf905e439de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-23T10:20:35.397Z_

<details open><summary>🔧 Tool call — Read · `toolu_017Kkb6h9DoZgyjHPJRbuUQP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/edd_threshold_sensitivity.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c391fbe6-14ba-4a8a-afea-13d0924bc840",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLEZKpeYu3959jPj3fE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58b319ff-f703-46fe-bd03-a11b39f57bba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4p53rS8iLHK47dF1ghdzm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7113,
      "cache_read_input_tokens": 64132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7113,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 46 · 2026-05-23T10:20:35.404Z_

<details><summary>↩ Tool result · `toolu_017Kkb6h9DoZgyjHPJRbuUQP`</summary>

```text
1	{
2	  "thresholds": [0.65, 0.70, 0.75, 0.80],
3	  "cells": {
4	    "pythia_nucleus": {
5	      "model": "Pythia-1.4B",
6	      "strategy": "nucleus_p095",
7	      "experiment_id": "mvp_pipeline_pythia_002",
8	      "aucs": {"d0v1": 0.9975, "d1v2": 0.8607, "d2v3": 0.8005},
9	      "edd": [3, 3, 3, 3],
10	      "bottleneck": "d2v3",
11	      "bottleneck_margin_to_080": 0.0005
12	    },
13	    "pythia_temp09": {
14	      "model": "Pythia-1.4B",
15	      "strategy": "temperature_09",
16	      "experiment_id": "pythia_temp09_001",
17	      "aucs": {"d0v1": 0.9968, "d1v2": 0.8327, "d2v3": 0.7928},
18	      "edd": [3, 3, 3, 2],
19	      "bottleneck": "d2v3",
20	      "bottleneck_margin_to_080": -0.0072
21	    },
22	    "pythia_topk50": {
23	      "model": "Pythia-1.4B",
24	      "strategy": "topk_k50",
25	      "experiment_id": "pythia_topk50_001",
26	      "aucs": {"d0v1": 0.9927, "d1v2": 0.7518, "d2v3": 0.6918},
27	      "edd": [3, 2, 2, 1],
28	      "bottleneck": "d2v3",
29	      "bottleneck_margin_to_080": -0.1082
30	    },
31	    "olmo_nucleus": {
32	      "model": "OLMo-1B",
33	      "strategy": "nucleus_p095",
34	      "experiment_id": "cross_model_olmo_002",
35	      "aucs": {"d0v1": 0.9834, "d1v2": 0.8673, "d2v3": 0.8124},
36	      "edd": [3, 3, 3, 3],
37	      "bottleneck": "d2v3",
38	      "bottleneck_margin_to_080": 0.0124
39	    },
40	    "olmo_temp09": {
41	      "model": "OLMo-1B",
42	      "strategy": "temperature_09",
43	      "experiment_id": "olmo_temp09_001",
44	      "aucs": {"d0v1": 0.9960, "d1v2": 0.9010, "d2v3": 0.8214},
45	      "edd": [3, 3, 3, 3],
46	      "bottleneck": "d2v3",
47	      "bottleneck_margin_to_080": 0.0214
48	    },
49	    "olmo_topk50": {
50	      "model": "OLMo-1B",
51	      "strategy": "topk_k50",
52	      "experiment_id": "olmo_topk50_001",
53	      "aucs": {"d0v1": 0.9930, "d1v2": 0.8305, "d2v3": 0.7357},
54	      "edd": [3, 3, 2, 2],
55	      "bottleneck": "d2v3",
56	      "bottleneck_margin_to_080": -0.0643
57	    },
58	    "gpt2xl_nucleus": {
59	      "model": "GPT-2-XL",
60	      "strategy": "nucleus_p095",
61	      "experiment_id": "cross_model_gpt2xl_001",
62	      "aucs": {"d0v1": 0.9941, "d1v2": 0.9131, "d2v3": 0.8829},
63	      "edd": [3, 3, 3, 3],
64	      "bottleneck": "d2v3",
65	      "bottleneck_margin_to_080": 0.0829
66	    },
67	    "gpt2xl_temp09": {
68	      "model": "GPT-2-XL",
69	      "strategy": "temperature_09",
70	      "experiment_id": "gpt2xl_temp09_001",
71	      "aucs": {"d0v1": 0.9963, "d1v2": 0.9367, "d2v3": 0.8815},
72	      "edd": [3, 3, 3, 3],
73	      "bottleneck": "d2v3",
74	      "bottleneck_margin_to_080": 0.0815
75	    },
76	    "gpt2xl_topk50": {
77	      "model": "GPT-2-XL",
78	      "strategy": "topk_k50",
79	      "experiment_id": "gpt2xl_topk50_001",
80	      "aucs": {"d0v1": 0.9906, "d1v2": 0.8126, "d2v3": 0.7529},
81	      "edd": [3, 3, 3, 2],
82	      "bottleneck": "d2v3",
83	      "bottleneck_margin_to_080": -0.0471
84	    }
85	  },
86	  "summary": {
87	    "edd3_count_by_threshold": {
88	      "0.65": 9,
89	      "0.70": 8,
90	      "0.75": 7,
91	      "0.80": 5
92	    },
93	    "cells_that_drop_at_each_threshold": {
94	      "0.70": ["pythia_topk50"],
95	      "0.75": ["olmo_topk50"],
96	      "0.80": ["pythia_temp09", "gpt2xl_topk50"]
97	    },
98	    "most_sensitive_cells": [
99	      {"cell": "pythia_topk50", "edd_range": [3, 1], "transitions": 2},
100	      {"cell": "olmo_topk50", "edd_range": [3, 2], "transitions": 1},
101	      {"cell": "pythia_temp09", "edd_range": [3, 2], "transitions": 1},
102	      {"cell": "gpt2xl_topk50", "edd_range": [3, 2], "transitions": 1}
103	    ],
104	    "fully_robust_cells": ["pythia_nucleus", "olmo_nucleus", "olmo_temp09", "gpt2xl_nucleus", "gpt2xl_temp09"]
105	  },
106	  "analysis": {
107	    "stability": "EDD is highly stable at T<=0.70 (8-9/9 cells at EDD=3). The major transition occurs between T=0.75 and T=0.80, where 2 additional cells drop from EDD=3, driven by d2v3 AUC values in the 0.75-0.80 marginal zone.",
108	    "sensitivity_pattern": "Sensitivity is concentrated in the topk50 decoding strategy (all 3 topk50 cells are among the 4 sensitive cells). The d2v3 pair (depth-2 vs depth-3) is the universal bottleneck — it determines EDD for all cells at all thresholds. The d0v1 pair (>0.98 everywhere) is never the limiting factor.",
109	    "model_effect": "GPT-2-XL is most robust (all 3 cells EDD>=2 at T=0.80, 2/3 at EDD=3). Pythia-1.4B is most sensitive (pythia_topk50 is the only cell to reach EDD=1). OLMo-1B falls in between.",
110	    "strategy_effect": "nucleus_p095 is most robust (3/3 EDD=3 at all thresholds). temperature_09 is slightly less robust (2/3 EDD=3 at T=0.80). topk50 is most sensitive (0/3 EDD=3 at T=0.80). This aligns with topk50's lower sampling diversity reducing inter-depth signal.",
111	    "recommended_threshold": "T=0.75. Rationale: (1) 7/9 cells maintain EDD=3, demonstrating the non-saturation finding is robust across most model-strategy combinations. (2) Only topk50 settings drop, which are known to produce the weakest inter-depth signals. (3) 0.75 is the conventional 'acceptable discrimination' threshold in AUC literature. (4) T=0.80 is too aggressive — it pushes 4 cells below EDD=3 due to marginal d2v3 values (0.75-0.80), inflating apparent sensitivity without meaningful signal loss. (5) T=0.65/0.70 are too lenient — they mask the genuine weakness of topk50.",
112	    "key_insight": "The core finding — recursive generation depth is distinguishable and signal does not saturate by depth 3 — is robust across a wide range of thresholds for 7/9 model-strategy cells. The 2 exceptions (pythia_topk50, olmo_topk50) reflect topk50's known tendency to flatten text distributions, not threshold sensitivity per se."
113	  },
114	  "metadata": {
115	    "generated_at": "2026-05-15",
116	    "data_sources": ["atlas_v2_data.json (7 cells)", "registry olmo_topk50_001 (1 cell)", "registry gpt2xl_topk50_001 (1 cell)"],
117	    "classifier": "RandomForest",
118	    "edd_definition": "EDD = max depth d such that all consecutive AUC(d_i vs d_{i+1}) >= threshold for i=0..d-1. If all pairs pass, EDD = max_depth (3)."
119	  }
120	}
121	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58b319ff-f703-46fe-bd03-a11b39f57bba",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "5e976481-6022-4f9a-8c49-6c0de800d0a9",
  "sourceToolAssistantUUID": "58b319ff-f703-46fe-bd03-a11b39f57bba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-23T10:20:35.739Z_

<details open><summary>🔧 Tool call — Read · `toolu_012FJ3pMoJeREcK8snqCPuDB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/cross_strategy_loo_results.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e976481-6022-4f9a-8c49-6c0de800d0a9",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLEZKpeYu3959jPj3fE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0193015-d431-4bb5-8026-b459b005d784",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4p53rS8iLHK47dF1ghdzm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7113,
      "cache_read_input_tokens": 64132,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7113
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 286,
          "cache_read_input_tokens": 64132,
          "cache_creation_input_tokens": 7113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7113,
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

_source line 48 · 2026-05-23T10:20:35.746Z_

<details><summary>↩ Tool result · `toolu_012FJ3pMoJeREcK8snqCPuDB`</summary>

```text
1	Cross-Strategy LOO Results (plan_007 Claim 1)
2	
3	| Model | Hold-out | Train | Test | 4-class acc | 95% CI | d1v2 AUC | d2v3 AUC |
4	|-------|----------|-------|------|-------------|--------|----------|----------|
5	| Pythia-1.4B | nucleus | 40000 | 20000 | 0.6935 | [0.687, 0.700] | 0.6903 | 0.7626 |
6	| Pythia-1.4B | temp09 | 40000 | 20000 | 0.6281 | [0.621, 0.635] | 0.5760 | 0.7240 |
7	| Pythia-1.4B | topk50 | 40000 | 20000 | 0.5151 | [0.508, 0.522] | 0.6393 | 0.5801 |
8	| GPT-2 XL | nucleus | 40000 | 20000 | 0.5993 | [0.593, 0.606] | 0.7826 | 0.4985 |
9	| GPT-2 XL | temp09 | 40000 | 20000 | 0.5609 | [0.554, 0.568] | 0.1288 | 0.6366 |
10	| GPT-2 XL | topk50 | 40000 | 20000 | 0.5364 | [0.530, 0.543] | 0.8308 | 0.7222 |
11	| OLMo-1B | nucleus | 40000 | 20000 | 0.6538 | [0.647, 0.660] | 0.7931 | 0.6076 |
12	| OLMo-1B | temp09 | 40000 | 20000 | 0.5816 | [0.575, 0.588] | 0.2529 | 0.7015 |
13	| OLMo-1B | topk50 | 40000 | 20000 | 0.5488 | [0.542, 0.556] | 0.8549 | 0.7107 |
14	
15	Mean 4-class accuracy across 9 rotations: 0.5908
16	All rotations above chance (0.25). Random baseline = 0.25.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0193015-d431-4bb5-8026-b459b005d784",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "eb933f85-3ebd-4ffc-b726-a4be98f94f57",
  "sourceToolAssistantUUID": "f0193015-d431-4bb5-8026-b459b005d784",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-23T10:20:40.155Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C614LvxXT6cBAq8P6zbBDs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": 500,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb933f85-3ebd-4ffc-b726-a4be98f94f57",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLEzRvwpsMCxVBQ48hQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b9b18ec-4984-485a-b7a2-f4880834ea0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BCTvbvMoGa8Rnk86SZHSts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10795,
      "cache_read_input_tokens": 71245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10795,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 50 · 2026-05-23T10:20:40.161Z_

<details><summary>↩ Tool result · `toolu_01C614LvxXT6cBAq8P6zbBDs`</summary>

```text
500	\centering
501	\small
502	\caption{Cross-scale comparison: 4-class RF accuracy (\%, depths 0--3), $\mathrm{EDD}_{0.70}$ (computed from full depth range: 0--5 for 1--1.5B nucleus and 7--8B, 0--3 for 1--1.5B temp/top-$k$ and 14B), and d0-vs-d1 AUC. CI: 95\% bootstrap. Chance = 25\%. $^\dagger$Self-reference model (see text).}
503	\label{tab:cross_scale}
504	\resizebox{\columnwidth}{!}{%
505	\begin{tabular}{@{}llccc@{}}
506	\toprule
507	Model & Strategy & 4-class acc & $\mathrm{EDD}_{0.70}$ & d0v1 \\
508	\midrule
509	GPT-2~XL (1.5B) & nucleus & 84.3 & 4 & 0.999 \\
510	OLMo-1B & nucleus & 78.9 & 4 & 0.997 \\
511	Pythia-1.4B & nucleus & 78.7 & 4 & 0.998 \\
512	\midrule
513	Llama-3.1-8B & nucleus & 70.2\,[68.3, 72.4] & 4 & 0.949 \\
514	Qwen2.5-7B & nucleus & 60.1\,[58.0, 62.1] & $5$ & 0.969 \\
515	\midrule
516	Qwen2.5-14B$^\dagger$ & nucleus & 54.1\,[53.4, 54.7] & 0 & 0.643 \\
517	Qwen2.5-14B$^\dagger$ & temp09 & 50.5\,[49.8, 51.2] & 0 & 0.632 \\
518	Qwen2.5-14B$^\dagger$ & top-$k$50 & 47.9\,[47.3, 48.6] & 0 & 0.561 \\
519	\cmidrule{2-5}
520	\multicolumn{2}{@{}l}{\textit{14B mean}} & \textit{50.8} & --- & --- \\
521	\bottomrule
522	\end{tabular}}
523	\end{table}
524	
525	\paragraph{(1) Depth signal persists at 7--8B scale.}
526	Both 7--8B models substantially exceed the 25\% chance baseline: Llama-3.1-8B achieves 70.2\% (95\% CI $[68.3, 72.4]$) and Qwen2.5-7B achieves 60.1\% ($[58.0, 62.1]$); recursive depth therefore remains estimable from perplexity-based features even when the generator is 5--7$\times$ larger than the reference model.
527	Depth-0 separability is preserved in both models: d0v1 AUC is 0.949 (Llama-3.1) and 0.969 (Qwen2.5).
528	
529	\paragraph{(2) EDD at 7--8B scale.}
530	At threshold $T{=}0.70$, Qwen2.5-7B maintains all consecutive-pair AUCs above 0.70 through depth~5 (Table~\ref{tab:cross_scale_auc}), yielding $\mathrm{EDD}_{0.70} = 5$ (the maximum observable from the tested depth range), exceeding the $\mathrm{EDD}_{0.70}{=}4$ observed at 1--1.5B.
531	Llama-3.1-8B matches the smaller models at $\mathrm{EDD}_{0.70}{=}4$: its monotonic decay causes d4v5 (0.618) to drop below $T$, despite stronger signal at shallower depths.
532	Both larger generators produce weaker per-step signal than the 1--1.5B models (mean consecutive AUC: 0.786 for Llama-3.1, 0.782 for Qwen2.5, vs.\ 0.852 at 1--1.5B).
533	
534	\begin{table}[h]
535	\centering
536	\small
537	\caption{Consecutive binary AUC. Llama-3.1-8B exhibits monotonic decay; Qwen2.5-7B shows a U-shaped pattern; Qwen2.5-14B$^\dagger$ (depths 0--3 only) has d0v1 below $T{=}0.70$ in all strategies, yielding $\mathrm{EDD}_{0.70}{=}0$ despite some later pairs exceeding the threshold. $^\dagger$Self-reference model.}
538	\label{tab:cross_scale_auc}
539	\resizebox{\columnwidth}{!}{%
540	\begin{tabular}{@{}llccccc@{}}
541	\toprule
542	Model & Strategy & d0v1 & d1v2 & d2v3 & d3v4 & d4v5 \\
543	\midrule
544	Llama-3.1-8B & nucleus & 0.949 & 0.877 & 0.771 & 0.716 & 0.618 \\
545	Qwen2.5-7B & nucleus & 0.969 & 0.729 & 0.709 & 0.732 & 0.772 \\
546	\midrule
547	Qwen2.5-14B$^\dagger$ & nucleus & 0.643 & 0.713 & \textbf{0.728} & \multicolumn{2}{c}{--} \\
548	Qwen2.5-14B$^\dagger$ & temp09 & 0.632 & \textbf{0.726} & 0.618 & \multicolumn{2}{c}{--} \\
549	Qwen2.5-14B$^\dagger$ & top-$k$50 & 0.561 & 0.687 & 0.679 & \multicolumn{2}{c}{--} \\
550	\bottomrule
551	\end{tabular}}
552	\end{table}
553	
554	\paragraph{(3) Divergent AUC trajectories and instruction-tuning effect.}
555	Among instruction-tuned models, Llama-3.1-8B exhibits monotonic AUC decay consistent with the 1--1.5B pattern, while Qwen2.5-7B shows a U-shaped recovery beyond d2v3 (Table~\ref{tab:cross_scale_auc}).
556	A base-model control (Llama-3.1-8B without instruction tuning) clarifies the causal direction: the base model achieves 59.9\% four-class accuracy (95\% CI [57.8, 62.15], $\mathrm{EDD}_{0.70}{=}2$) with non-monotonic AUC decay (Table~\ref{tab:llama3_base_auc}), while the instruction-tuned variant reaches 70.2\% with strictly monotonic decay.
557	The base-model control experiment suggests instruction-tuning regularizes rather than confounds the depth signal.
558	Separately, the FP16 self-reference experiment at 7B (Appendix~\ref{app:qwen7b_selfref}) produces strictly monotonic AUC decay (0.697, 0.673, 0.659), indicating that the U-shaped pattern in QLoRA Qwen2.5-7B likely originates from the cross-reference setup (Pythia-1.4B as observer) rather than from an intrinsic property of the depth signal.
559	
560	\begin{table}[h]
561	\centering
562	\small
563	\caption{Pairwise AUC: Llama-3.1-8B Base vs.\ Instruct.}
564	\label{tab:llama3_base_auc}
565	\begin{tabular}{lccccc}
566	\toprule
567	Variant & $d_{0\text{v}1}$ & $d_{1\text{v}2}$ & $d_{2\text{v}3}$ & $d_{3\text{v}4}$ & $d_{4\text{v}5}$ \\
568	\midrule
569	Base & 0.918 & 0.794 & 0.682 & 0.730 & 0.595 \\
570	Instruct & 0.949 & 0.877 & 0.771 & 0.716 & 0.618 \\
571	\bottomrule
572	\end{tabular}
573	\end{table}
574	
575	The base model exhibits non-monotonic decay with a U-shaped recovery at $d_{3\text{v}4}$, while the instruction-tuned variant shows strictly monotonic decay. Both variants exceed chance (AUC $> 0.5$) at all boundaries; depth signal exists regardless of instruction-tuning, though instruction-tuning strengthens and regularizes it.
576	
577	\paragraph{(4) Signal attenuation at 14B.}
578	Qwen2.5-14B (clean FP16, self-reference) is tested across all three decoding strategies (Table~\ref{tab:cross_scale}).
579	Mean four-class accuracy is 50.8\% ($2.0{\times}$ chance), with nucleus 54.1\%, temperature 50.5\%, and top-$k$ 47.9\%.
580	$\mathrm{EDD}_{0.70}{=}0$ across all three strategies because the d0/d1 boundary falls below the 0.70 AUC threshold in every case (0.56--0.64), breaking the contiguous prefix at the first boundary.
581	The d0/d1 boundary, near-perfect at 1--1.5B (AUC ${>}0.99$), attenuates to 0.56--0.64 at 14B.
582	
583	Each strategy produces a structurally distinct adjacent-pair AUC pattern (Table~\ref{tab:cross_scale_auc}):
584	nucleus is monotonically increasing (d0v1=0.643 $<$ d1v2=0.713 $<$ d2v3=0.728);
585	temperature exhibits d2v3 collapse (0.618, the weakest boundary) because temperature scaling uniformly amplifies logit differences, accelerating convergence to the attractor distribution at deeper depths;
586	top-$k$ exhibits d0v1 collapse (0.561, the weakest boundary) because vocabulary truncation constrains d0 and d1 distributions to the same top-$k$ tokens, compressing their statistical distance.
587	This three-way divergence confirms at 14B that different decoding strategies induce structurally distinct degradation trajectories (\S\ref{sec:gen:crossstrategy}).
588	
589	Feature importance shifts under top-$k$: lexical diversity metrics (TTR, hapax ratio) enter the top-5, displacing perplexity tail statistics that dominate under nucleus and temperature.
590	This result carries an important caveat: Qwen2.5-14B uses self-reference, whereas all other experiments use Pythia-1.4B.
591	Self-reference conflates the generator's distributional shift with the reference model's sensitivity; the observed attenuation may partially reflect the reference model change rather than a pure scale effect.
592	
593	\paragraph{(5) Cross-reference control at 14B.}
594	To disentangle the scale effect from the reference-model artifact, we re-extract all 19 features using Pythia-1.4B (the same reference model as the 1--1.5B benchmark) on the Qwen2.5-14B generated text.
595	Table~\ref{tab:cross_ref_14b} compares self-reference and cross-reference results per strategy.
596	
597	\begin{table}[h]
598	\centering
599	\small
600	\caption{14B cross-reference control: Pythia-1.4B reference vs.\ self-reference on Qwen2.5-14B text. $\Delta$: cross $-$ self. $\mathrm{EDD}_{0.70}$ computed from consecutive pairwise AUC.}
601	\label{tab:cross_ref_14b}
602	\resizebox{\columnwidth}{!}{%
603	\begin{tabular}{@{}lccccc@{}}
604	\toprule
605	Strategy & Self-ref (\%) & Cross-ref (\%) & $\Delta$ & $\mathrm{EDD}_{0.70}$ & d0v1 AUC \\
606	\midrule
607	nucleus & 54.1 & 45.0 & $-$9.1 & 2 & 0.702 \\
608	temp ($\tau{=}0.9$) & 50.5 & 46.3 & $-$4.2 & 2 & 0.739 \\
609	top-$k$ ($k{=}50$) & 47.9 & 40.9 & $-$7.1 & 0 & 0.699 \\
610	\cmidrule{2-6}
611	\textit{mean} & \textit{50.8} & \textit{44.1} & $-$\textit{6.8} & --- & --- \\
612	\bottomrule
613	\end{tabular}}
614	\end{table}
615	
616	Cross-reference accuracy drops by 6.8\,pp on average (range 4.2--9.1\,pp), but $\mathrm{EDD}_{0.70}$ \emph{rises} from 0 to 2 for nucleus and temperature: the consecutive d0v1 (0.70--0.74) and d1v2 (0.72--0.73) AUCs now exceed the 0.70 threshold, while d2v3 remains below (0.54--0.61).
617	Under self-reference, the first boundary d0v1 falls below $T{=}0.70$ in all strategies (0.56--0.64), breaking the contiguous prefix and yielding $\mathrm{EDD}_{0.70}{=}0$ even though some later pairs (e.g., nucleus d1v2\,=\,0.713, d2v3\,=\,0.728) exceed the threshold; the Pythia-1.4B reference model provides sharper distributional contrast at the cost of overall accuracy.
618	The ${\sim}$7\,pp accuracy gap between self- and cross-reference is therefore a reference-model artifact, not a depth-signal artifact: depth signal persists at 14B albeit attenuated relative to 1--1.5B.
619	
620	\paragraph{Caveats.}
621	For Qwen2.5-7B, the CI lower bound (58.0\%) does not exclude sub-60\% accuracy; Llama-3.1-8B's lower bound (68.3\%) is more comfortably above chance but still below the 75--83\% range at 1--1.5B.
622	The divergent AUC trajectories across two models caution against strong generalizations from only two 7--8B data points: both the monotonic (Llama-3.1) and non-monotonic (Qwen2.5) patterns are single observations, and further architectures are needed to establish which is the dominant regime at this scale.
623	
624	\paragraph{Confounds.}
625	\label{app:cross_scale_confounds}
626	Four confounds limit the 7--8B results: (1)~4-bit NF4 QLoRA quantization (absent at 1--1.5B) may distort the perplexity distribution independently of depth; (2)~smaller sample size (500 vs.\ 5{,}000 per depth) widens confidence intervals; (3)~evaluation is limited to nucleus sampling at 7--8B (the 14B model addresses this with all three strategies); (4)~vocabulary mismatch between larger generators and the 1.4B reference model.
627	For the 14B model specifically: the cross-reference control (Table~\ref{tab:cross_ref_14b}) quantifies the reference-model artifact at ${\sim}$7\,pp, but the remaining accuracy gap (44\% vs.\ 78--85\% at 1--1.5B) still conflates scale with the other confounds listed above.
628	The base-model control partially addresses a former confound (instruction-tuning): since the base variant shows weaker signal with non-monotonic decay while the instruction-tuned variant shows stronger monotonic signal, instruction-tuning regularizes rather than confounds depth estimation.
629	The remaining confounds are not mutually independent (quantization and vocabulary mismatch both affect the perplexity distribution); it is therefore infeasible to attribute the observed accuracy gap (60--70\% vs.\ 78--85\% at 1--1.5B) to any single factor.
630	
631	\subsection{Qwen2.5-7B Self-Reference Scale Probe}
632	\label{app:qwen7b_selfref}
633	
634	The preceding 7--8B experiments (\S\ref{app:cross_scale_full}) use 4-bit NF4 QLoRA with Pythia-1.4B cross-reference, leaving two confounds unresolved: (1)~quantization-induced perplexity distortion and (2)~vocabulary mismatch between the 7B generator and the 1.4B reference model.
635	To isolate the scale effect from these artifacts, we run the full recursive generation pipeline on Qwen2.5-7B \cite{qwen2.5} (base model, not instruction-tuned) using FP16 LoRA fine-tuning and self-reference feature extraction (the same model serves as both generator and reference).
636	
637	\paragraph{Setup.}
638	At each depth $k \in \{0, 1, 2, 3\}$, a fresh LoRA adapter ($r{=}16$, $\alpha{=}32$, dropout $0.05$, target modules \texttt{q\_proj}, \texttt{k\_proj}, \texttt{v\_proj}) is initialized on the base model and trained on $\mathcal{D}_{k-1}$ for 3 epochs (lr $2{\times}10^{-4}$, effective batch size 16 via $4 \times 4$ gradient accumulation, bfloat16 mixed precision), following the same protocol as the 1--1.5B benchmark (\S\ref{sec:method:benchmark}).
639	Generation uses nucleus sampling ($p{=}0.95$), producing 5{,}000 passages per depth (20{,}000 total, matching the per-cell sample size of the primary benchmark).
640	Feature extraction computes the standard 19-dimensional feature vector $\mathbf{f}(x)$ using the model's own token-level log-probabilities as the reference distribution, eliminating the cross-model reference artifact quantified in Table~\ref{tab:cross_ref_14b}.
641	Classification uses the same 5-fold stratified Random Forest (200 trees, seed 42) as all other cells.
642	
643	\paragraph{Comparison to prior 7B experiments.}
644	This experiment differs from the QLoRA Qwen2.5-7B-Instruct entry in Table~\ref{tab:cross_scale} in three respects: (i)~FP16 LoRA removes quantization distortion, (ii)~self-reference removes vocabulary mismatch, and (iii)~5{,}000 samples per depth (vs.\ 500) narrows confidence intervals.
645	If depth signal persists under these cleaner conditions, the attenuation observed in the QLoRA experiments reflects genuine scale effects rather than methodological artifacts.
646	
647	\paragraph{Results.}
648	The self-reference probe achieves 52.1\% four-class accuracy (CI [51.4, 52.7], $2.1{\times}$ chance, $\mathrm{EDD}_{0.70}{=}0$; $\mathrm{EDD}_{0.65}{=}3$).
649	Pairwise AUC: d0-vs-d1 = 0.697, d1-vs-d2 = 0.673, d2-vs-d3 = 0.659; top-5 features: \texttt{p90\_ppl}, \texttt{skew\_ppl}, \texttt{p90\_surprisal}, \texttt{kurt\_ppl}, \texttt{var\_surprisal}.
650	Contrary to the hypothesis that removing quantization and vocabulary-mismatch confounds would improve accuracy, self-reference at 7B is 8\,pp below the QLoRA cross-reference baseline (60.1\%), and closely matches the 14B self-reference result (50.8\%, $\mathrm{EDD}_{0.70}{=}0$).
651	This reveals a self-reference ceiling: larger models assign similar probabilities to d0 and d1 text, collapsing d0v1 discriminability (AUC\,=\,0.697 vs.\ 0.969 under cross-reference).
652	Cross-model reference strategies, where a smaller observer model provides complementary distributional perspective, may be necessary for effective depth estimation above ${\sim}$7B.
653	
654	\subsection{Cross-Boundary Generalization}
655	\label{app:cross_boundary}
656	
657	The preceding experiments assume a single model family generates all recursive depths.
658	In practice, recursive contamination may traverse model boundaries: text generated by model~A is used to train model~B, whose output trains model~C.
659	We probe whether the depth signal persists under two relaxations of the single-model assumption.
660	
661	\paragraph{Cross-model recursive chains.}
662	We construct a heterogeneous chain: human text (d0) $\to$ Pythia-1.4B generates d1 $\to$ OLMo-1B finetuned on Pythia-d1 generates d2 $\to$ GPT-2~XL finetuned on OLMo-d2 generates d3.
663	Each recursive step uses a \emph{different} model family, eliminating the possibility that depth signal arises from a single model's idiosyncratic behavior.
664	A 4-class Random Forest achieves 84.75\% accuracy (95\% CI $[81.0, 88.25]$), with per-depth F1 scores of 0.98 (d0), 0.88 (d1), 0.76 (d2), and 0.76 (d3).
665	Pairwise AUC remains high: d0-vs-d1 = 0.999 and d2-vs-d3 = 0.841.
666	These results suggest that distributional artifacts of recursive generation persist across model boundaries. This constitutes preliminary evidence for a process-level depth signal rather than individual generator artifacts.
667	
668	\paragraph{Confound discussion.}
669	The heterogeneous chain confounds architecture identity with depth (d1=Pythia, d2=OLMo, d3=GPT-2~XL).
670	However, if the classifier exploited architecture fingerprints rather than depth signal, near-perfect accuracy would be expected since architecture perfectly determines depth label.
671	The observed 84.75\% with monotonically decreasing per-depth F1 (d0=0.98, d1=0.88, d2=0.76, d3=0.76) is more consistent with a depth-signal interpretation, as architecture fingerprinting would not produce this graded pattern.
672	We address this confound directly with a reverse-chain control below.
673	
674	\paragraph{Reverse-chain control.}
675	To empirically test the architecture confound hypothesis, we constructed a reverse chain (GPT-2~XL $\to$ OLMo $\to$ Pythia) reversing the model-depth assignment.
676	The reverse chain achieves 85.75\% (95\% CI [82.0, 89.25]), statistically indistinguishable from the forward chain (84.75\%, [81.0, 88.25]).
677	If the classifier exploited architecture fingerprints rather than depth signal, reversing the chain should invert depth predictions; the equivalent accuracy under both orderings provides empirical evidence against the architecture confound.
678	
679	\paragraph{Cross-domain transfer.}
680	All prior experiments use WikiText-103 as the seed corpus.
681	To test domain dependence, we repeat the pipeline with arXiv abstracts as the seed text (Pythia-1.4B, nucleus $p{=}0.95$, 500 samples per depth, d0--d3).
682	Five-fold cross-validation yields 74.1\% $\pm$ 2.0\% accuracy, compared to ${\sim}$78\% on the WikiText seed.
683	Per-depth F1 shows the familiar pattern: d0 = 1.00, d1 = 0.78, d2 = 0.52, d3 = 0.66, with d2 remaining the most challenging class.
684	The 4pp accuracy gap relative to WikiText likely reflects the narrower stylistic range of scientific abstracts, which may reduce the distributional contrast between adjacent depths.
685	These results provide preliminary evidence that the perplexity-based features capture properties of the recursive generation process rather than domain-specific artifacts of the seed corpus.
686	
687	\subsection{Cross-Seed Replication}
688	\label{app:seed_replication}
689	
690	Table~\ref{tab:seed_replication} reports within-seed accuracy for all three model families (nucleus, depths 0--3) under two independent LoRA training seeds.
691	
692	\begin{table}[h]
693	\centering
694	\small
695	\caption{Cross-seed replication (nucleus $p{=}0.95$, d0--d3). seed=42 is the primary benchmark (matching Table~\ref{tab:main_matrix}); seed=43 is an independent replication.}
696	\label{tab:seed_replication}
697	\begin{tabular}{@{}llccc@{}}
698	\toprule
699	Model & Seed & Acc (\%) & 95\% CI & $\Delta$ (pp) \\
700	\midrule
701	Pythia-1.4B & 42 & 78.70 & [78.10, 79.24] & --- \\
702	Pythia-1.4B & 43 & 78.84 & [78.13, 79.52] & $+$0.14 \\
703	\midrule
704	OLMo-1B & 42 & 78.94 & [78.38, 79.48] & --- \\
705	OLMo-1B & 43 & 82.11 & [81.77, 82.54] & $+$3.17 \\
706	\midrule
707	GPT-2~XL & 42 & 84.28 & [83.78, 84.80] & --- \\
708	GPT-2~XL & 43 & 86.32 & [86.17, 86.49] & $+$2.04 \\
709	\bottomrule
710	\end{tabular}
711	\end{table}
712	
713	Seed=43 yields higher accuracy in all three models ($+$0.14 to $+$3.17\,pp, same direction).
714	For Pythia ($+$0.14\,pp), CIs overlap, consistent with noise; for OLMo ($+$3.17\,pp) and GPT-2~XL ($+$2.04\,pp), CIs do not overlap, so LoRA initialization has a non-trivial effect on absolute accuracy (${\sim}$1--3\,pp).
715	Top-3 features are identical across all seeds and models (\texttt{p90\_ppl}, \texttt{var\_surprisal}, \texttt{p75\_ppl}); depth ordering is preserved in every configuration.
716	
717	\paragraph{Outlier handling.}
718	Feature extraction occasionally produces extreme perplexity values (outlier passages); we apply per-feature clipping at $\pm 10^{10}$ before classification, affecting ${<}0.1$\% of samples.
719	The d3 perplexity distribution varies substantially across seeds: under seed=42, 0.56\% of d3 passages exceed $10^6$ in raw perplexity, while under seed=43 this fraction rises to 12.8\%.
720	Despite this variation, the classifier remains effective after clipping, confirming that the depth signal resides in the p90-and-below distributional shape rather than extreme outliers.
721	
722	\subsection{Depth-4 Extension}
723	\label{app:depth4_ext}
724	
725	We extend all three model families (GPT-2~XL, Pythia-1.4B, OLMo-1B; nucleus $p{=}0.95$) to depth~4 and train 5-class RF classifiers (d0--d4, 5{,}000 samples per depth).
726	Five-class accuracy reaches 80.5\% (OLMo), 74.0\% (GPT-2~XL), and 71.3\% (Pythia), all substantially above the 20\% chance baseline.
727	For Pythia and GPT-2~XL, d3 recall drops from ${\sim}$80\% (4-class) to ${\sim}$49\% (5-class) due to d3/d4 confusion; d4 recall is higher (Pythia 68.1\%, GPT-2~XL 63.9\%).
728	$\mathrm{EDD}_{0.70} \geq 4$ was established by dedicated binary classifiers in the atlas (\S\ref{sec:atlas:edd}; d3v4 AUC: Pythia 0.784, OLMo 0.765, GPT-2~XL 0.750); the 5-class results provide complementary evidence that depth~4 remains discriminable in the multi-class setting.
729	
730	\paragraph{Feature monotonicity at d4.}
731	For Pythia and GPT-2~XL, the dominant depth markers (\texttt{p90\_ppl}, \texttt{var\_surprisal}) maintain monotonic decrease through d4 (Pythia \texttt{p90\_ppl}: $483.7 \to 12.5$ from d0 to d4; \texttt{var\_surprisal}: $6.50 \to 1.29$), consistent with continued tail erosion (\S\ref{sec:method:theory}).
732	Mean perplexity breaks monotonicity at d4 for GPT-2~XL (d3: $1{,}076\mathrm{K}$ $\to$ d4: $928\mathrm{K}$) while tail perplexity continues to decline.
733	OLMo exhibits a \texttt{var\_surprisal} rebound at d4 ($2.49 \to 2.83$, non-monotonic), creating a feature signature absent in GPT-2~XL and Pythia.
734	The 5-class RF exploits non-adjacent depth contrasts (particularly d0-vs-d4 and d2-vs-d4) to achieve 80.5\% accuracy, the highest among all three families, while the dedicated binary d3-vs-d4 classifier (AUC 0.765) is restricted to adjacent-depth features.
735	This discrepancy illustrates that multi-class classifiers can exploit global distributional structure unavailable to pairwise comparisons.
736	The divergence between aggregate and tail statistics suggests that aggregate distributional statistics saturate at deep recursion while tail statistics continue to shift.
737	This saturation provides a physical mechanism for the EDD ceiling: once per-step feature change falls below classifier resolution, adjacent depths become indistinguishable regardless of continued distributional drift.
738	
739	\subsection{Generation Length Ablation}
740	\label{app:length_ablation}
741	
742	Table~\ref{tab:length_ablation} reports classification accuracy as a function of passage length (Pythia-1.4B nucleus, depths 0--3).
743	
744	\begin{table}[h]
745	\centering
746	\small
747	\caption{Generation length ablation (Pythia-1.4B nucleus, 5-fold CV). Accuracy increases monotonically with passage length; the 9.47\,pp spread confirms that longer passages provide stronger statistical signal.}
748	\label{tab:length_ablation}
749	\begin{tabular}{@{}lc@{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b9b18ec-4984-485a-b7a2-f4880834ea0d",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "c6707068-b3a7-4b2b-9c2c-ff03805fd421",
  "sourceToolAssistantUUID": "6b9b18ec-4984-485a-b7a2-f4880834ea0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-23T10:20:41.239Z_

<details open><summary>🔧 Tool call — Read · `toolu_013K69oVPe2y4xiiWRECQQnS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/cross_model_heatmap.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6707068-b3a7-4b2b-9c2c-ff03805fd421",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLEzRvwpsMCxVBQ48hQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72893e53-0239-4aa1-b3bd-36611c615dd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BCTvbvMoGa8Rnk86SZHSts",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10795,
      "cache_read_input_tokens": 71245,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10795
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 71245,
          "cache_creation_input_tokens": 10795,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10795,
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

_source line 52 · 2026-05-23T10:20:41.256Z_

<details><summary>↩ Tool result · `toolu_013K69oVPe2y4xiiWRECQQnS`</summary>

```text
1	{
2	  "rf_4class_acc": {
3	    "rows": [
4	      "Pythia-1.4B",
5	      "OLMo-1B",
6	      "GPT-2-XL"
7	    ],
8	    "cols": [
9	      "Nucleus p=0.95",
10	      "Temp τ=0.9",
11	      "Top-k k=50"
12	    ],
13	    "values": [
14	      [
15	        0.782,
16	        0.7625,
17	        0.696
18	      ],
19	      [
20	        0.788,
21	        0.8203,
22	        null
23	      ],
24	      [
25	        0.833,
26	        0.8542,
27	        null
28	      ]
29	    ]
30	  },
31	  "d1v2_auc": {
32	    "rows": [
33	      "Pythia-1.4B",
34	      "OLMo-1B",
35	      "GPT-2-XL"
36	    ],
37	    "cols": [
38	      "Nucleus p=0.95",
39	      "Temp τ=0.9",
40	      "Top-k k=50"
41	    ],
42	    "values": [
43	      [
44	        0.8607,
45	        0.8327,
46	        0.7518
47	      ],
48	      [
49	        0.8673,
50	        0.901,
51	        null
52	      ],
53	      [
54	        0.9131,
55	        0.9367,
56	        null
57	      ]
58	    ]
59	  },
60	  "d2v3_auc": {
61	    "rows": [
62	      "Pythia-1.4B",
63	      "OLMo-1B",
64	      "GPT-2-XL"
65	    ],
66	    "cols": [
67	      "Nucleus p=0.95",
68	      "Temp τ=0.9",
69	      "Top-k k=50"
70	    ],
71	    "values": [
72	      [
73	        0.8005,
74	        0.7928,
75	        0.6918
76	      ],
77	      [
78	        0.8124,
79	        0.8214,
80	        null
81	      ],
82	      [
83	        0.8829,
84	        0.8815,
85	        null
86	      ]
87	    ]
88	  }
89	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72893e53-0239-4aa1-b3bd-36611c615dd2",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "271209bb-15cb-4146-a8e2-330d3d09b0d0",
  "sourceToolAssistantUUID": "72893e53-0239-4aa1-b3bd-36611c615dd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-23T10:20:43.646Z_

Let me read the remaining parts of the appendix and other key data sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "271209bb-15cb-4146-a8e2-330d3d09b0d0",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLFQ2zzHSNBMqeG5G3U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fd6491c-b484-49a7-b191-da8c80379faf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mu47ZN7phteVNu7Bps2Mee",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9391,
      "cache_read_input_tokens": 82040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9391,
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

_source line 54 · 2026-05-23T10:20:46.002Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BKvm2D9ftwueJLvmgGDJUf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": 750,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fd6491c-b484-49a7-b191-da8c80379faf",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLFQ2zzHSNBMqeG5G3U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ebfd6a7-c06b-46b6-b46a-22ab1f050c3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mu47ZN7phteVNu7Bps2Mee",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9391,
      "cache_read_input_tokens": 82040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9391,
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

_source line 55 · 2026-05-23T10:20:46.008Z_

<details><summary>↩ Tool result · `toolu_01BKvm2D9ftwueJLvmgGDJUf`</summary>

```text
750	\toprule
751	Passage length (tokens) & Acc (\%) \\
752	\midrule
753	128 & 68.35 \\
754	256 & 73.80 \\
755	512 & 77.82 \\
756	\bottomrule
757	\end{tabular}
758	\end{table}
759	
760	Depth signal is detectable from 128 tokens (2.7$\times$ chance) and saturates near 500 tokens.
761	The monotonic increase reflects the statistical nature of the features: longer passages yield more stable estimates of perplexity percentiles and surprisal variance, reducing within-class overlap at adjacent depth boundaries.
762	
763	\subsection{Mixed-Depth Corpus}
764	\label{app:mixed_depth}
765	
766	Per-passage classification is largely independent of corpus composition: evaluating on a corpus containing mixed proportions of d0--d3 passages (rather than balanced classes) yields macro-recall $\Delta{=}{-}1.62$\,pp relative to the balanced benchmark (within the 2\,pp tolerance).
767	Individual class deltas range from $-$0.45\,pp to $-$2.43\,pp (d1 shows the largest shift); the RF classifier operates on per-sample features without sensitivity to the class distribution of the evaluation corpus, as Random Forest produces identical per-sample predictions regardless of batch context.
768	
769	\subsection{Learned Estimator Comparison}
770	\label{app:learned_estimator}
771	
772	Table~\ref{tab:learned_estimator} evaluates three learned classifiers (XGBoost, ordinal MLP with CORAL loss \cite{coral2020}, prototypical networks) under the same leave-one-model-out protocol as Table~\ref{tab:cross_model}.
773	The ordinal MLP follows the nested binary reduction framework \cite{mccullagh1980_ordinal,frank2001} with the loss function of \citet{rennie2005}.
774	All three methods operate on the same 19-dimensional feature vector; the comparison isolates the effect of the classification head.
775	
776	\begin{table}[h]
777	\centering
778	\small
779	\caption{Learned estimator cross-model transfer (leave-one-model-out, nucleus, 4-class). RF baseline from Table~\ref{tab:cross_model}. Chance = 25\%.}
780	\label{tab:learned_estimator}
781	\begin{tabular}{@{}lcccc@{}}
782	\toprule
783	Method & Pythia & OLMo & GPT-2 XL & Mean \\
784	\midrule
785	RF (baseline) & --- & --- & --- & 66.4 \\
786	XGBoost & 63.7 & 69.8 & 68.1 & 67.2 \\
787	Ordinal MLP & 62.5 & 69.7 & 67.9 & 66.7 \\
788	Prototypical & 61.6 & 70.0 & 68.4 & 66.6 \\
789	\bottomrule
790	\end{tabular}
791	\end{table}
792	
793	All three learned methods match the RF baseline within 0.8\,pp on average; the Pythia holdout is consistently the hardest (61.6--63.7\%), while OLMo and GPT-2~XL holdouts yield 67.9--70.0\%.
794	The narrow spread ($\leq$0.8\,pp across four methods) reinforces the conclusion that the 19-feature representation, not the classifier, determines the accuracy ceiling in the cross-model transfer setting.
795	
796	\subsection{Instruction-Tuned Model at 1.5B Scale}
797	\label{app:instruct_1p5b}
798	
799	To test whether instruction tuning eliminates depth signal at matched scale (1.5B, avoiding the quantization confound of \S\ref{sec:gen:crossscale}), we run the full recursive pipeline on Qwen2.5-1.5B-Instruct with self-reference feature extraction (i.e., the same model serves as both generator and reference).
800	
801	The RF classifier achieves 47.4\% four-class accuracy (95\% CI $[46.7, 48.1]$, $1.9\times$ chance); instruction tuning therefore reduces but does not eliminate depth signal.
802	The pairwise AUC profile differs from base models: d0v1 = 0.653, d1v2 = 0.620, d2v3 = 0.664, with a gap-dependent pattern (non-adjacent pairs yield higher AUC, e.g., d0v3 = 0.902) but no pair reaching the 0.75 threshold.
803	
804	The feature importance ranking shifts: the perplexity tail statistics (\texttt{p90\_ppl}, \texttt{var\_surprisal}) that dominate in base models drop in relative importance, while surprisal variance and mean-level features gain rank.
805	This shift suggests instruction tuning compresses the perplexity distribution (reducing tail discriminability) while preserving lower-order statistical patterns.
806	
807	Two caveats apply: (1) self-reference evaluation may inflate or deflate accuracy relative to cross-reference evaluation (cf.\ \S\ref{app:ref_ablation}); (2) a single instruction-tuned model does not establish the generality of the feature shift across architectures or instruction-tuning recipes.
808	
809	\subsection{Downstream Fine-Tuning Probe (Inconclusive)}
810	\label{app:downstream}
811	
812	We fine-tune Pythia-410M with LoRA ($r{=}16$, $\alpha{=}32$) on depth-stratified subsets (500 samples each) and evaluate held-out perplexity (200 samples, 50 per depth).
813	
814	\begin{table}[h]
815	\centering
816	\small
817	\caption{Downstream fine-tuning probe: held-out perplexity by training subset (Pythia-410M LoRA, seed=42). $\Delta$: signed difference vs.\ baseline (negative = better).}
818	\label{tab:downstream}
819	\begin{tabular}{@{}lcc@{}}
820	\toprule
821	Training subset & PPL & $\Delta$ vs.\ baseline \\
822	\midrule
823	Baseline (no fine-tuning) & 5.67 & --- \\
824	d0 only & 5.65 & $-$0.02 \\
825	d1 only & 5.55 & $-$0.12 \\
826	d2 only & 5.56 & $-$0.11 \\
827	Mixed (d0--d3) & 5.55 & $-$0.12 \\
828	\bottomrule
829	\end{tabular}
830	\end{table}
831	
832	The hypothesis that d0-only data yields the lowest perplexity is not supported: d1-only and mixed subsets tie for best (PPL~5.55), both marginally below d0-only (5.65).
833	The PPL spread is small (0.12, 2.1\% relative) and the sample size (500 per condition, single seed) is insufficient for statistical significance.
834	Training loss decreases monotonically with depth (d0: 2.558, d1: 1.920, d2: 1.286), consistent with recursive generation reducing information content and making text easier to model.
835	This pilot establishes that depth-filtered data is not harmful for downstream fine-tuning; whether depth-aware curation provides a meaningful advantage requires larger-scale evaluation.
836	
837	\subsection{Feature Group Ablation}
838	\label{app:feature_ablation}
839	
840	Table~\ref{tab:feature_ablation_indist} reports in-distribution group ablation accuracy (5-fold CV, mean across all 9 model--strategy cells).
841	Table~\ref{tab:feature_ablation} reports the same ablation under cross-model transfer (leave-one-model-out, nucleus).
842	
843	\begin{table}[h]
844	\centering
845	\small
846	\caption{Feature group ablation (in-distribution, 9-cell mean, 5-fold CV, 4-class). Chance = 25\%.}
847	\label{tab:feature_ablation_indist}
848	\begin{tabular}{@{}lccc@{}}
849	\toprule
850	Feature group & \#Feat. & Acc (\%) & $\Delta$ vs.\ Full \\
851	\midrule
852	Full (all 19) & 19 & 78.4 & --- \\
853	Perplexity only & 9 & 76.6{\scriptsize$\pm$5.6} & $-$1.8 \\
854	Surprisal only & 3 & 73.2{\scriptsize$\pm$5.7} & $-$5.2 \\
855	Lexical Diversity only & 4 & 46.1{\scriptsize$\pm$4.5} & $-$32.3 \\
856	Repetition only & 3 & 43.7{\scriptsize$\pm$5.2} & $-$34.7 \\
857	\bottomrule
858	\end{tabular}
859	\end{table}
860	
861	\begin{table}[h]
862	\centering
863	\small
864	\caption{Feature group ablation (cross-model LOO, nucleus, 4-class). Groups merge the four Table~\ref{tab:features} categories into three: bigram/trigram entropy move from Lexical Diversity to Entropy/Surprisal; TTR/hapax move to Repetition/Diversity. Chance = 25\%.}
865	\label{tab:feature_ablation}
866	\begin{tabular}{@{}lccc@{}}
867	\toprule
868	Feature group & \#Feat. & Acc (\%) & $\Delta$ vs.\ Full \\
869	\midrule
870	Full (all 19) & 19 & 66.4 & --- \\
871	Perplexity only & 9 & 66.0 & $-$0.4 \\
872	Entropy/Surprisal only & 5 & 63.2 & $-$3.2 \\
873	Repetition/Diversity only & 5 & 53.0 & $-$13.4 \\
874	\midrule
875	\texttt{p90\_ppl} only & 1 & 58.3 & $-$8.1 \\
876	\bottomrule
877	\end{tabular}
878	\end{table}
879	
880	Under both settings perplexity features nearly match the full set, while repetition/diversity features fall far below; perplexity degradation statistics carry the dominant depth signal.
881	The top-2 individual features by Gini importance are \texttt{p90\_ppl} (22.4\%) and \texttt{var\_surprisal} (18.8\%), accounting for 41\% of total importance.
882	
883	\subsection{RF Seed Robustness}
884	\label{app:rf_seed}
885	
886	Table~\ref{tab:rf_seed} reports cross-model transfer accuracy across three RF random seeds.
887	
888	\begin{table}[h]
889	\centering
890	\small
891	\caption{RF seed robustness (cross-model LOO, nucleus, 4-class).}
892	\label{tab:rf_seed}
893	\begin{tabular}{@{}lc@{}}
894	\toprule
895	Seed & Acc (\%) \\
896	\midrule
897	42 & 66.4 \\
898	123 & 66.5 \\
899	456 & 66.5 \\
900	\midrule
901	Mean $\pm$ std & 66.48 $\pm$ 0.06 \\
902	\bottomrule
903	\end{tabular}
904	\end{table}
905	
906	The 0.06\,pp standard deviation across seeds confirms that RF classification is deterministic to within rounding noise at this sample size, and reported accuracy differences across experimental conditions (e.g., feature ablation, cross-model transfer) are not attributable to classifier randomness.
907	
908	\subsection{Binary Detector Baselines for Ordinal Classification}
909	\label{app:detector_baselines}
910	
911	We evaluate whether existing binary AI-text detectors and membership inference methods, when repurposed for ordinal classification, can match our 19-feature RF pipeline.
912	
913	\paragraph{Binary detectors (Pythia nucleus).}
914	Binoculars~\cite{binoculars2024} and Fast-DetectGPT~\cite{fast_detectgpt2024} scores are computed on the Pythia-1.4B nucleus ($p{=}0.95$) subset and fed to: (a)~a log-likelihood rank classifier (Log-Rank, 64.0\%), (b)~a combined RF trained on both detector scores (Combined, 74.2\%), and (c)~the standard 19-feature RF (78.7\%).
915	The 4.5\,pp gap (74.2\% vs.\ 78.7\%) confirms that perplexity distributional features capture ordinal depth structure beyond what generic detection scores provide.
916	Note that Fast-DetectGPT exhibits numerical overflow on Pythia nucleus d1 (mean perturbation score $>$28{,}000); results for this cell should be interpreted cautiously.
917	Across all 9 atlas cells, Binoculars and Fast-DetectGPT ordinal accuracy averages ${\sim}$35\% and ${\sim}$32\%, respectively.
918	
919	\paragraph{Membership inference baselines (all 9 cells).}
920	DetectGPT~\cite{mitchell2023_detectgpt} (gpt2-large scoring model, t5-large perturbation model, 5 perturbations) achieves 30.7\% mean 4-class accuracy (d1--d3 BalAcc: 24.3\%); Table~\ref{tab:baselines} reports 28.8\% under the best-of-3 calibration protocol, which selects the optimal threshold configuration per cell.
921	Min-K\% Prob~\cite{shi2024_minkprob} ($K{=}20$) with CORAL ordinal calibration reaches 33.2\% (d1--d3 BalAcc: 40.4\%); the best single cell is gpt2xl\_temp09 at 50.6\%.
922	Min-K\%'s advantage over DetectGPT (+2.5\,pp) is consistent with token-level log-probabilities containing more depth-relevant information than perturbation-based curvature, but both remain within 10\,pp of chance.
923	CORAL calibration improves ordinal structure (d1--d3 BalAcc 40.4\% vs.\ 33.3\% random) without closing the gap to RF (71.6\%), confirming that the bottleneck is the input signal rather than the calibration strategy.
924	Perturbation-based and membership-inference methods (28--33\%) confirm that token-level detection scores lack ordinal depth resolution.
925	Cross-perplexity (Binoculars) is a notable exception: when evaluated across all 9 atlas cells with threshold calibration, Binoculars achieves 69.8\%; with multi-feature RF calibration (11 cross-perplexity statistics), it reaches 78.1\%, matching our 19-feature pipeline within 0.3\,pp (\S\ref{sec:gen:baselines}).
926	
927	\paragraph{Augmented feature set.}
928	To test whether detection scores carry complementary ordinal signal, we add Min-K\% probability ($K{=}20$) and DetectGPT perturbation discrepancy as additional RF features.
929	The 21-feature model (19 + Min-K\% + DetectGPT) achieves 78.90\% mean 4-class accuracy (+0.48\,pp) and 72.20\% d1--d3 balanced accuracy (+0.60\,pp).
930	Min-K\% ranks \#3 by feature importance (0.095), behind \texttt{p90\_ppl} (0.161) and \texttt{var\_surprisal} (0.126); DetectGPT ranks \#17 (0.026).
931	The marginal improvement is consistent across 8 of 9 atlas cells, indicating that Min-K\%'s token-level log-probability signal provides weak but real complementary information to the passage-level distributional features.
932	The top-2 features (\texttt{p90\_ppl} + \texttt{var\_surprisal}) retain combined importance of 28.7\%, confirming that perplexity tail statistics remain the dominant depth markers even after augmentation.
933	
934	\paragraph{Pairwise AUC and ordinal collapse.}
935	Table~\ref{tab:detector_pairwise_auc} reports pairwise binary AUC for three nucleus cells, contrasting our 19-feature RF with LR-calibrated detector scores and their combination.
936	Detectors achieve reasonable d0-vs-d1 separation (Combined AUC\,$\geq$\,0.949), but d1-vs-d2 and d2-vs-d3 AUC collapse toward chance (0.50--0.77), far below the RF pipeline (0.930--0.958 and 0.813--0.892 respectively).
937	This confirms that binary detection scores capture the real-vs-synthetic boundary but lack the ordinal gradient needed to distinguish recursive depths.
938	
939	\begin{table}[h]
940	\centering
941	\small
942	\caption{Pairwise binary AUC for detector baselines vs.\ RF-19feat on three nucleus cells. RF uses 500-tree binary classifiers; detector methods use LR on continuous scores (Bino/FDGPT) or their combination. d1v2 and d2v3 AUC near 0.50 = ordinal collapse.}
943	\label{tab:detector_pairwise_auc}
944	\resizebox{\columnwidth}{!}{%
945	\begin{tabular}{@{}llccc@{}}
946	\toprule
947	Cell & Method & d0v1 & d1v2 & d2v3 \\
948	\midrule
949	Pythia-1.4B & RF-19feat & \textbf{0.999} & \textbf{0.930} & \textbf{0.813} \\
950	 & Binoculars & 0.738 & 0.529 & 0.515 \\
951	 & Fast-DetectGPT & 0.797 & 0.596 & 0.530 \\
952	 & Combined & 0.990 & 0.767 & 0.626 \\
953	\midrule
954	OLMo-1B & RF-19feat & \textbf{0.997} & \textbf{0.934} & \textbf{0.819} \\
955	 & Binoculars & 0.744 & 0.509 & 0.522 \\
956	 & Fast-DetectGPT & 0.917 & 0.668 & 0.520 \\
957	 & Combined & 0.949 & 0.742 & 0.550 \\
958	\midrule
959	GPT-2~XL & RF-19feat & \textbf{0.999} & \textbf{0.958} & \textbf{0.892} \\
960	 & Binoculars & 0.942 & 0.502 & 0.581 \\
961	 & Fast-DetectGPT & 0.955 & 0.644 & 0.655 \\
962	 & Combined & 0.969 & 0.724 & 0.703 \\
963	\bottomrule
964	\end{tabular}}
965	\end{table}
966	
967	\subsection{Binoculars Feature Ablation and Signal Decomposition}
968	\label{app:feature_ablation_bino}
969	
970	To quantify the overlap and complementarity between our 19-feature pipeline and Binoculars' cross-perplexity features, we evaluate four feature configurations across all 9 atlas cells (Table~\ref{tab:bino_ablation}).
971	
972	\begin{table}[h]
973	\centering
974	\small
975	\caption{Feature ablation: overlap and merged configurations (9-cell mean, 5-fold CV, RF 200 trees). The 6 overlap features are the perplexity statistics shared between both pipelines (mean, variance, median, p10, p90, skewness).}
976	\label{tab:bino_ablation}
977	\begin{tabular}{@{}lccc@{}}
978	\toprule
979	Configuration & \#Feat. & Acc (\%) & $\Delta$ vs.\ 19-feat \\
980	\midrule
981	6 overlap only & 6 & 75.9 & $-$2.5 \\
982	Our 19 features & 19 & 78.4 & --- \\
983	Binoculars 11 features & 11 & 78.1 & $-$0.3 \\
984	Merged (19 + 11) & 30 & \textbf{82.6} & +4.2 \\
985	\bottomrule
986	\end{tabular}
987	\end{table}
988	
989	The 6 shared perplexity features alone achieve 75.9\% (97\% of the full pipeline's accuracy), confirming that mean-level perplexity distributional displacement is the core depth signal.
990	Our 13 additional features (kurtosis, surprisal variance, lexical/n-gram statistics) contribute +2.5\,pp of shape-level information; Binoculars' 5 unique features (observer-performer agreement score, cross-entropy statistics) contribute +4.2\,pp of cross-model divergence when merged.
991	
992	Table~\ref{tab:bino_ablation_percell} reports per-cell results for three configurations with per-cell breakdown (Bino-11 per-cell values are omitted because features were computed on the pooled 9-cell corpus).
993	
994	\begin{table}[h]
995	\centering
996	\small
997	\caption{Per-cell feature ablation (4-class accuracy \%, 5-fold CV, RF 200 trees). $\Delta$: merged minus 19-feature accuracy. Bino-11 per-cell values omitted because Binoculars features were computed on the pooled 9-cell corpus; the per-cell mean (78.1\%) is reported in Table~\ref{tab:bino_ablation}.}
998	\label{tab:bino_ablation_percell}
999	\resizebox{\columnwidth}{!}{%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ebfd6a7-c06b-46b6-b46a-22ab1f050c3b",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "8eabde77-1ffe-40f5-b8af-c42bc5024d8e",
  "sourceToolAssistantUUID": "8ebfd6a7-c06b-46b6-b46a-22ab1f050c3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-23T10:20:47.136Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XvUsRC2YGv85uHhLCxggF3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/atlas_v2/edd_analysis.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8eabde77-1ffe-40f5-b8af-c42bc5024d8e",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLFQ2zzHSNBMqeG5G3U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2756fe86-b8e6-4757-90e7-cfb74a3c7666",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mu47ZN7phteVNu7Bps2Mee",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9391,
      "cache_read_input_tokens": 82040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9391,
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

_source line 57 · 2026-05-23T10:20:47.148Z_

<details><summary>↩ Tool result · `toolu_01XvUsRC2YGv85uHhLCxggF3`</summary>

```text
1	{
2	  "pythia_nucleus": {
3	    "edd": null,
4	    "saturated": false,
5	    "adjacent_aucs": {
6	      "depth0_vs_depth1": 0.9975,
7	      "depth1_vs_depth2": 0.8607,
8	      "depth2_vs_depth3": 0.8005
9	    },
10	    "threshold": 0.7,
11	    "interpretation": "Signal persists through depth 3 (no saturation within measured range)"
12	  },
13	  "pythia_temp09": {
14	    "edd": null,
15	    "saturated": false,
16	    "adjacent_aucs": {
17	      "depth0_vs_depth1": 0.9968,
18	      "depth1_vs_depth2": 0.8327,
19	      "depth2_vs_depth3": 0.7928
20	    },
21	    "threshold": 0.7,
22	    "interpretation": "Signal persists through depth 3 (no saturation within measured range)"
23	  },
24	  "pythia_topk50": {
25	    "edd": 3,
26	    "saturated": true,
27	    "adjacent_aucs": {
28	      "depth0_vs_depth1": 0.9927,
29	      "depth1_vs_depth2": 0.7518,
30	      "depth2_vs_depth3": 0.6918
31	    },
32	    "threshold": 0.7,
33	    "interpretation": "Signal saturates at depth 3"
34	  },
35	  "olmo_nucleus": {
36	    "edd": null,
37	    "saturated": false,
38	    "adjacent_aucs": {
39	      "depth0_vs_depth1": 0.9834,
40	      "depth1_vs_depth2": 0.8673,
41	      "depth2_vs_depth3": 0.8124
42	    },
43	    "threshold": 0.7,
44	    "interpretation": "Signal persists through depth 3 (no saturation within measured range)"
45	  },
46	  "olmo_temp09": {
47	    "edd": null,
48	    "saturated": false,
49	    "adjacent_aucs": {
50	      "depth0_vs_depth1": 0.996,
51	      "depth1_vs_depth2": 0.901,
52	      "depth2_vs_depth3": 0.8214
53	    },
54	    "threshold": 0.7,
55	    "interpretation": "Signal persists through depth 3 (no saturation within measured range)"
56	  },
57	  "gpt2xl_nucleus": {
58	    "edd": null,
59	    "saturated": false,
60	    "adjacent_aucs": {
61	      "depth0_vs_depth1": 0.9941,
62	      "depth1_vs_depth2": 0.9131,
63	      "depth2_vs_depth3": 0.8829
64	    },
65	    "threshold": 0.7,
66	    "interpretation": "Signal persists through depth 3 (no saturation within measured range)"
67	  },
68	  "gpt2xl_temp09": {
69	    "edd": null,
70	    "saturated": false,
71	    "adjacent_aucs": {
72	      "depth0_vs_depth1": 0.9963,
73	      "depth1_vs_depth2": 0.9367,
74	      "depth2_vs_depth3": 0.8815
75	    },
76	    "threshold": 0.7,
77	    "interpretation": "Signal persists through depth 3 (no saturation within measured range)"
78	  }
79	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2756fe86-b8e6-4757-90e7-cfb74a3c7666",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "e0cf27e6-3b59-4023-b772-1ebb0e1aa175",
  "sourceToolAssistantUUID": "2756fe86-b8e6-4757-90e7-cfb74a3c7666",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-23T10:20:47.623Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Hasbs7P9Wxom8zKszuaGKz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/atlas_v2/jaccard_matrix.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0cf27e6-3b59-4023-b772-1ebb0e1aa175",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLFQ2zzHSNBMqeG5G3U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad875e6d-5065-45d5-966a-200a2cfa49c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mu47ZN7phteVNu7Bps2Mee",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9391,
      "cache_read_input_tokens": 82040,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9391
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 82040,
          "cache_creation_input_tokens": 9391,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9391,
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

_source line 59 · 2026-05-23T10:20:47.631Z_

<details><summary>↩ Tool result · `toolu_01Hasbs7P9Wxom8zKszuaGKz`</summary>

```text
1	{
2	  "Pythia-1.4B": {
3	    "strategy_features": {
4	      "Nucleus p=0.95": [
5	        "mean_ppl",
6	        "mean_surprisal",
7	        "p75_ppl",
8	        "p90_ppl",
9	        "var_surprisal"
10	      ],
11	      "Temp τ=0.9": [
12	        "mean_ppl",
13	        "mean_surprisal",
14	        "p75_ppl",
15	        "p90_ppl",
16	        "var_surprisal"
17	      ],
18	      "Top-k k=50": [
19	        "mean_ppl",
20	        "mean_surprisal",
21	        "p75_ppl",
22	        "p90_ppl",
23	        "var_surprisal"
24	      ]
25	    },
26	    "pairwise_jaccard": {
27	      "Nucleus p=0.95 vs Temp τ=0.9": {
28	        "jaccard": 1.0,
29	        "overlap": [
30	          "mean_ppl",
31	          "mean_surprisal",
32	          "p75_ppl",
33	          "p90_ppl",
34	          "var_surprisal"
35	        ],
36	        "only_first": [],
37	        "only_second": []
38	      },
39	      "Nucleus p=0.95 vs Top-k k=50": {
40	        "jaccard": 1.0,
41	        "overlap": [
42	          "mean_ppl",
43	          "mean_surprisal",
44	          "p75_ppl",
45	          "p90_ppl",
46	          "var_surprisal"
47	        ],
48	        "only_first": [],
49	        "only_second": []
50	      },
51	      "Temp τ=0.9 vs Top-k k=50": {
52	        "jaccard": 1.0,
53	        "overlap": [
54	          "mean_ppl",
55	          "mean_surprisal",
56	          "p75_ppl",
57	          "p90_ppl",
58	          "var_surprisal"
59	        ],
60	        "only_first": [],
61	        "only_second": []
62	      }
63	    }
64	  },
65	  "OLMo-1B": {
66	    "strategy_features": {
67	      "Nucleus p=0.95": [
68	        "mean_surprisal",
69	        "p75_ppl",
70	        "p90_ppl",
71	        "type_token_ratio",
72	        "var_surprisal"
73	      ],
74	      "Temp τ=0.9": [
75	        "mean_surprisal",
76	        "p50_ppl",
77	        "p75_ppl",
78	        "p90_ppl",
79	        "var_surprisal"
80	      ]
81	    },
82	    "pairwise_jaccard": {
83	      "Nucleus p=0.95 vs Temp τ=0.9": {
84	        "jaccard": 0.6667,
85	        "overlap": [
86	          "mean_surprisal",
87	          "p75_ppl",
88	          "p90_ppl",
89	          "var_surprisal"
90	        ],
91	        "only_first": [
92	          "type_token_ratio"
93	        ],
94	        "only_second": [
95	          "p50_ppl"
96	        ]
97	      }
98	    }
99	  },
100	  "GPT-2-XL": {
101	    "strategy_features": {
102	      "Nucleus p=0.95": [
103	        "mean_ppl",
104	        "mean_surprisal",
105	        "p75_ppl",
106	        "p90_ppl",
107	        "var_surprisal"
108	      ],
109	      "Temp τ=0.9": [
110	        "mean_surprisal",
111	        "p50_ppl",
112	        "p75_ppl",
113	        "p90_ppl",
114	        "var_surprisal"
115	      ]
116	    },
117	    "pairwise_jaccard": {
118	      "Nucleus p=0.95 vs Temp τ=0.9": {
119	        "jaccard": 0.6667,
120	        "overlap": [
121	          "mean_surprisal",
122	          "p75_ppl",
123	          "p90_ppl",
124	          "var_surprisal"
125	        ],
126	        "only_first": [
127	          "mean_ppl"
128	        ],
129	        "only_second": [
130	          "p50_ppl"
131	        ]
132	      }
133	    }
134	  }
135	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad875e6d-5065-45d5-966a-200a2cfa49c8",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "ae29a96b-424e-40ca-a864-a3eec7d4b14c",
  "sourceToolAssistantUUID": "ad875e6d-5065-45d5-966a-200a2cfa49c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-23T10:20:50.095Z_

Let me get the remaining appendix sections and a few more artifact files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae29a96b-424e-40ca-a864-a3eec7d4b14c",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLFs4CoSjAbDuoUWPZU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0f410e6-f748-4e59-b3f4-fb063de4db0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vRXJCJqS9dY8jrBfW1phc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8746,
      "cache_read_input_tokens": 91431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8746,
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

_source line 61 · 2026-05-23T10:20:52.418Z_

<details open><summary>🔧 Tool call — Read · `toolu_015ggHSz5UUGZm5CrSUS4BEB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": 1000,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0f410e6-f748-4e59-b3f4-fb063de4db0f",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLFs4CoSjAbDuoUWPZU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "985a6e57-8ddf-453a-b19d-ba2b85ca17a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vRXJCJqS9dY8jrBfW1phc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8746,
      "cache_read_input_tokens": 91431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8746,
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

### Tool result

_source line 62 · 2026-05-23T10:20:52.426Z_

<details><summary>↩ Tool result · `toolu_015ggHSz5UUGZm5CrSUS4BEB`</summary>

```text
1000	\begin{tabular}{@{}lcccc c@{}}
1001	\toprule
1002	Cell & 6-overlap & 19-feat & Bino-11 & Merged & $\Delta$ \\
1003	\midrule
1004	Pythia nucleus & 76.7 & 78.7 & --- & 83.5 & +4.8 \\
1005	Pythia temp09 & 73.9 & 76.8 & --- & 81.5 & +4.7 \\
1006	Pythia top-$k$50 & 65.3 & 68.9 & --- & 71.2 & +2.3 \\
1007	OLMo nucleus & 76.4 & 78.9 & --- & 84.2 & +5.3 \\
1008	OLMo temp09 & 81.0 & 82.3 & --- & 88.3 & +6.0 \\
1009	OLMo top-$k$50 & 72.5 & 74.4 & --- & 78.4 & +4.0 \\
1010	GPT-2~XL nucleus & 81.7 & 84.3 & --- & 88.8 & +4.5 \\
1011	GPT-2~XL temp09 & 84.0 & 85.9 & --- & 88.5 & +2.6 \\
1012	GPT-2~XL top-$k$50 & 72.1 & 75.8 & --- & 79.1 & +3.3 \\
1013	\midrule
1014	\textbf{9-cell mean} & \textbf{75.9} & \textbf{78.4} & \textbf{78.1} & \textbf{82.6} & \textbf{+4.2} \\
1015	\bottomrule
1016	\end{tabular}}
1017	\end{table}
1018	
1019	\paragraph{Strategy-dependent complementarity.}
1020	The merged improvement varies by decoding strategy: nucleus and temperature cells gain +4.7\,pp on average, while top-k cells gain +3.2\,pp.
1021	Top-k sampling truncates the token distribution to the $k$ highest-probability tokens, producing text with reduced distributional diversity; this limits the information available to cross-model divergence features, which rely on disagreement between observer and performer predictions.
1022	Merged improvement also varies by generator family: OLMo cells (observer-dissimilar) gain +5.1\,pp on average, compared to +3.9\,pp for Pythia (observer-similar) and +3.5\,pp for GPT-2~XL, suggesting cross-model divergence features contribute more when observer and generator architectures differ.
1023	
1024	\paragraph{Cross-scale Binoculars ablation (14B).}
1025	We evaluate Binoculars cross-scale on two representative strategies (temperature, top-$k$); the nucleus cell was used for the main 14B pipeline and its GPU hours were allocated to generation rather than Binoculars evaluation.
1026	At 14B, when only 1--1.5B reference models are available for cross-perplexity computation (Pythia-1.4B observer analyzing Qwen2.5-14B text), Binoculars features degrade substantially (Table~\ref{tab:bino_14b_ablation}).
1027	Self-reference statistical features (19-feat) outperform Binoculars (11-feat) by 8--11\,pp, reversing the near-parity observed at 1--1.5B.
1028	Merging all 30 features yields a consistent +3.6--3.7\,pp gain over the self-reference baseline across both tested strategies, confirming that cross-perplexity features retain complementary signal even under the 10$\times$ scale gap, though the gain is attenuated relative to +4.2\,pp at 1--1.5B.
1029	
1030	\begin{table}[h]
1031	\centering
1032	\small
1033	\caption{Feature ablation at 14B (Qwen2.5-14B, self-reference$^\dagger$). Binoculars: observer=Pythia-1.4B, performer=Pythia-410M. $\Delta$: merged minus main-pipeline stat-only accuracy (Method~A alignment). Chance = 25\%.}
1034	\label{tab:bino_14b_ablation}
1035	\begin{tabular}{@{}lcccc@{}}
1036	\toprule
1037	Strategy & Bino-11 & Stat-19$^\dagger$ & Merged-30 & $\Delta$ \\
1038	\midrule
1039	temp09 & 42.6 & 50.5 & 54.2 & +3.7 \\
1040	top-$k$50 & 37.7 & 47.9 & 51.5 & +3.6 \\
1041	\bottomrule
1042	\end{tabular}
1043	\end{table}
1044	
1045	The Binoculars degradation reflects a practical deployment constraint: the 10$\times$ scale gap between observer (1.4B) and generator (14B) causes cross-perplexity features to lose sensitivity, not a fundamental limitation of the cross-model divergence channel.
1046	Self-reference features are more robust across scales because they avoid the observer--generator mismatch.
1047	The accuracy difference between self-reference (50.8\%) and Binoculars stat-only (40.1\% mean) may therefore partially reflect observer capacity limitations rather than feature design differences.
1048	
1049	\subsection{Prompted Generation Results}
1050	\label{app:prompted_gen}
1051	
1052	Table~\ref{tab:prompted_gen} reports depth estimation performance under topic-seeded (prompted) generation using GPT-2~XL with nucleus sampling ($p{=}0.95$, depths 0--3).
1053	Generation is conditioned on Wikipedia topic prompts rather than a bare BOS token, a more ecologically valid test of depth signal persistence.
1054	
1055	\begin{table}[h]
1056	\centering
1057	\small
1058	\caption{Prompted generation (GPT-2~XL, nucleus $p{=}0.95$, topic-seeded). BOS baseline re-evaluated within the prompted-generation pipeline for matched comparison. 5-fold CV accuracy and pairwise AUC. Chance = 25\%.}
1059	\label{tab:prompted_gen}
1060	\begin{tabular}{@{}lc@{}}
1061	\toprule
1062	Metric & Value \\
1063	\midrule
1064	4-class accuracy (\%) & 69.52 $[68.9, 70.2]$ \\
1065	BOS-seeded baseline (\%) & 83.3 \\
1066	$\Delta$ (prompted $-$ BOS) & $-$13.78\,pp \\
1067	\midrule
1068	AUC d0v1 & 0.916 \\
1069	AUC d1v2 & 0.782 \\
1070	AUC d2v3 & 0.744 \\
1071	\midrule
1072	Top-1 feature & \texttt{p90\_ppl} \\
1073	Top-2 feature & \texttt{var\_surprisal} \\
1074	Top-3 feature & \texttt{p75\_ppl} \\
1075	\bottomrule
1076	\end{tabular}
1077	\end{table}
1078	
1079	The 13.8\,pp drop relative to BOS-seeded generation is expected: topic prompts constrain the output distribution, reducing the variance that distinguishes depths.
1080	Nevertheless, accuracy remains $2.8\times$ chance and pairwise AUC decays monotonically (0.916, 0.782, 0.744); the depth signal is therefore not an artifact of unconstrained generation.
1081	Top features are identical to BOS-seeded (\texttt{p90\_ppl} first); the same perplexity tail erosion mechanism operates under prompted conditions.
1082	
1083	\subsection{Extended Discussion}
1084	\label{app:extended_discussion}
1085	
1086	\paragraph{Cross-strategy conditional decomposition.}
1087	The two-stage pipeline (strategy identification followed by depth classification) recovers 11.5\,pp over the na\"ive pooled classifier.
1088	Under correct strategy routing, four-class accuracy reaches 72.6\% vs.\ 68.0\% under misrouting ($N{=}103{,}498$ / $76{,}502$), a gap of 4.6\,pp; d0 accuracy remains near-ceiling (${\sim}99.6$\%) regardless of routing, confirming that the d0 signal is strategy-invariant.
1089	Even the worst routing yields a floor of 67.6\% ($2.7\times$ chance), and the 31.5\,pp d1--d3 gap between correct and wrong routing confirms feature-space misalignment rather than uniform noise.
1090	End-to-end PLMs lag RF by ${\sim}20$\,pp, suggesting that current pretrained representations do not capture the distributional tail statistics that drive depth discrimination.
1091	
1092	\paragraph{Depth-graduated curation (inconclusive).}
1093	Initial curation experiments remain inconclusive: RF-vs-unfiltered is not significant ($p>0.4$; Appendix~\ref{app:curation_poc}).
1094	
1095	\paragraph{Toward a provenance toolkit.}
1096	Depth estimation complements existing provenance methods along orthogonal axes.
1097	Watermarking \cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.
1098	Source attribution \cite{uchendu2020_attribution} identifies the generating model but not the generation history.
1099	Depth estimation characterizes \emph{iterative reuse} regardless of generator cooperation or identity.
1100	A layered provenance system combining these three signals (watermark presence, source model, and recursive generation depth) could support more nuanced data auditing than any single method.
1101	
1102	\subsection{Computational Resources and Reproducibility}
1103	\label{app:compute}
1104	
1105	\paragraph{Hardware.}
1106	All experiments were conducted on 2$\times$ NVIDIA RTX PRO 6000 (48\,GB) GPUs locally and 2$\times$ NVIDIA RTX PRO 6000 (48\,GB) on cloud instances.
1107	Total computation is approximately 200 GPU$\cdot$hours, covering the $3 \times 3$ generation matrix (LoRA fine-tuning + sampling at each depth), feature extraction, depth extension to d5, 7--14B cross-scale experiments, and all ablations.
1108	
1109	\paragraph{Software.}
1110	Key library versions: PyTorch 2.10.0+cu128, Transformers 5.8.1, PEFT 0.7.1, scikit-learn 1.8.0.
1111	Additional dependencies: Accelerate 1.13.0, Datasets 4.8.4, XGBoost 3.2.0, NumPy 2.2.6 (Python 3.12.3, CUDA 12.8).
1112	
1113	\paragraph{Hyperparameters.}
1114	LoRA hyperparameters ($r{=}16$, $\alpha{=}32$, dropout $0.05$, lr $2{\times}10^{-4}$, batch size 8, 3 epochs) follow \citet{hu2022lora}.
1115	The Random Forest classifier uses 200 trees, Gini criterion, and no max depth, without hyperparameter search; all reported results use 5-fold stratified cross-validation.
1116	
1117	\paragraph{Inference cost.}
1118	Feature extraction requires a single forward pass of the reference model.
1119	On a single GPU this takes approximately 2 minutes for 5{,}000 passages; a CPU-only alternative requires approximately 50 minutes on server-grade hardware.
1120	RF classification adds negligible overhead ($<$1\,s).
1121	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "985a6e57-8ddf-453a-b19d-ba2b85ca17a3",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "8d8f114d-990a-43c4-af95-29b400a58da7",
  "sourceToolAssistantUUID": "985a6e57-8ddf-453a-b19d-ba2b85ca17a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-23T10:20:53.395Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BtMM8wWUEpP6PGH4WkeGgN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/data/baseline_unified_comparison.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d8f114d-990a-43c4-af95-29b400a58da7",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLFs4CoSjAbDuoUWPZU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a957321-acf1-42f8-8649-72f539c195a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vRXJCJqS9dY8jrBfW1phc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8746,
      "cache_read_input_tokens": 91431,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8746
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 221,
          "cache_read_input_tokens": 91431,
          "cache_creation_input_tokens": 8746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8746,
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

_source line 64 · 2026-05-23T10:20:53.400Z_

<details><summary>↩ Tool result · `toolu_01BtMM8wWUEpP6PGH4WkeGgN`</summary>

```text
1	Unified Baseline Comparison (70/15/15 split, same test set)
2	
3	| Method | 4-class Acc | 95% CI | 3-class Acc | MAE |
4	|--------|------------|--------|-------------|-----|
5	| CE-MLP (DCOL ablation) | **0.7897** | [0.774, 0.804] | **0.7204** | 0.2280 |
6	| DivEye (XGBoost) | 0.7817 | [0.766, 0.797] | 0.7098 | 0.2363 |
7	| Random Forest | 0.7813 | [0.766, 0.797] | 0.7093 | 0.2387 |
8	| CORAL Ordinal | 0.7807 | [0.765, 0.795] | 0.7089 | **0.2273** |
9	| Logistic Regression | 0.7497 | [0.734, 0.765] | 0.6671 | 0.2767 |
10	| PPL Regression (multi) | 0.6223 | [0.605, 0.640] | 0.5200 | 0.3890 |
11	| PPL Regression (single) | 0.2513 | [0.237, 0.267] | 0.3351 | 0.9440 |
12	
13	RF 80/20 split (0.7815) vs 70/15/15 split (0.7813): Δ=0.0002, negligible → prior results reliable.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a957321-acf1-42f8-8649-72f539c195a0",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "87627c66-8440-476f-b96e-5bcd45e6e14d",
  "sourceToolAssistantUUID": "6a957321-acf1-42f8-8649-72f539c195a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-23T10:20:56.576Z_

Now let me look for additional data sources referenced in the paper, particularly around cross-model transfer, feature importance, and specific numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87627c66-8440-476f-b96e-5bcd45e6e14d",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLGJD3A95FdZFXE8tKk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86ace2ce-6fd0-4ad5-a4f9-183fef7f8cd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MqFZnK1wTSfbBTrbW6ipzW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3910,
      "cache_read_input_tokens": 100177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3910,
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

_source line 66 · 2026-05-23T10:20:58.896Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Fg2ss8ose8TJGBhW59edV9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/cross_model_loo_v1/data/cross_model_loo_results.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86ace2ce-6fd0-4ad5-a4f9-183fef7f8cd1",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLGJD3A95FdZFXE8tKk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a925cfcd-f034-4970-a240-75dbc698555b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MqFZnK1wTSfbBTrbW6ipzW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3910,
      "cache_read_input_tokens": 100177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3910,
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

_source line 67 · 2026-05-23T10:20:58.903Z_

<details><summary>↩ Tool result · `toolu_01Fg2ss8ose8TJGBhW59edV9`</summary>

```text
1	Hold-out Pythia: acc=0.6242 [0.6206,0.6282] d1v2=0.5617 d2v3=0.6534 recall: d0=1.0 d1=0.493 d2=0.2677 d3=0.7363
2	Hold-out OLMo: acc=0.6921 [0.6886,0.6959] d1v2=0.7687 d2v3=0.6862 recall: d0=0.9925 d1=0.7549 d2=0.4327 d3=0.5883
3	Hold-out GPT-2 XL: acc=0.6756 [0.6719,0.6792] d1v2=0.8157 d2v3=0.6639 recall: d0=0.9853 d1=0.7465 d2=0.5255 d3=0.445
4	Mean 4-class acc: 0.664. Full JSON at server: /root/autodl-tmp/recursive_gen_depth_est/results/cross_model_loo.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a925cfcd-f034-4970-a240-75dbc698555b",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "06af43d7-9ec1-4d78-acb7-5fd0b89535ae",
  "sourceToolAssistantUUID": "a925cfcd-f034-4970-a240-75dbc698555b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-23T10:20:59.357Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BcFg8dMkHZkVATEF8wVzdf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/feature_importance_consistency_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06af43d7-9ec1-4d78-acb7-5fd0b89535ae",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLGJD3A95FdZFXE8tKk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9cec8cf5-a61a-4a9c-bffd-e1fe25771d70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MqFZnK1wTSfbBTrbW6ipzW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3910,
      "cache_read_input_tokens": 100177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3910,
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

_source line 69 · 2026-05-23T10:20:59.362Z_

<details><summary>↩ Tool result · `toolu_01BcFg8dMkHZkVATEF8wVzdf`</summary>

```text
1	# Cross-Experiment Feature Importance Consistency Analysis
2	
3	**Date**: 2026-05-14
4	**Experiments**: 6 (3 models × 2-3 decoding strategies)
5	
6	## Experiments Covered
7	
8	| ID | Model | Strategy | Source |
9	|----|-------|----------|--------|
10	| Pythia_nuc | Pythia-1.4B | nucleus (p=0.95) | results/feature_importance.json |
11	| Pythia_t09 | Pythia-1.4B | temperature=0.9 | results/pythia_temp09/ |
12	| Pythia_k50 | Pythia-1.4B | top-k=50 | results/pythia_topk50/ |
13	| OLMo_nuc | OLMo-1B | nucleus (p=0.95) | results/olmo/ |
14	| GPT2XL_nuc | GPT-2 XL | nucleus (p=0.95) | results/gpt2xl/ |
15	| GPT2XL_t09 | GPT-2 XL | temperature=0.9 | results/gpt2xl_temp09/ |
16	
17	## Full Feature Importance Table
18	
19	| Feature | Pythia_nuc | Pythia_t09 | Pythia_k50 | OLMo_nuc | GPT2XL_nuc | GPT2XL_t09 | Mean | CV |
20	|---------|-----------|-----------|-----------|---------|-----------|-----------|------|-----|
21	| var_surprisal | 0.169 (R1) | 0.178 (R1) | 0.176 (R1) | 0.161 (R2) | 0.208 (R2) | 0.121 (R4) | 0.169 | 0.17 |
22	| p90_ppl | 0.158 (R2) | 0.150 (R2) | 0.135 (R2) | 0.180 (R1) | 0.208 (R1) | 0.263 (R1) | 0.182 | 0.25 |
23	| mean_ppl | 0.120 (R3) | 0.114 (R3) | 0.112 (R3) | 0.040 (R8) | 0.064 (R5) | ~0 (R18) | 0.075 | 0.64 |
24	| mean_surprisal | 0.088 (R4) | 0.089 (R4) | 0.070 (R4) | 0.084 (R4) | 0.082 (R4) | 0.148 (R2) | 0.094 | 0.29 |
25	| p75_ppl | 0.067 (R5) | 0.069 (R5) | 0.061 (R5) | 0.111 (R3) | 0.103 (R3) | 0.146 (R3) | 0.093 | 0.36 |
26	| type_token_ratio | 0.034 (R10) | 0.036 (R6) | 0.042 (R6) | 0.061 (R5) | 0.046 (R6) | 0.030 (R6) | 0.041 | 0.26 |
27	| hapax_ratio | 0.032 (R11) | 0.035 (R7) | 0.042 (R7) | 0.044 (R6) | 0.028 (R10) | 0.025 (R9) | 0.034 | 0.21 |
28	| p50_ppl | 0.037 (R7) | 0.039 (R8) | 0.039 (R8) | 0.041 (R7) | 0.035 (R7) | 0.057 (R5) | 0.041 | 0.18 |
29	| entropy_of_surprisal | 0.035 (R8) | 0.034 (R10) | 0.037 (R10) | 0.027 (R14) | 0.035 (R8) | 0.030 (R8) | 0.033 | 0.11 |
30	| p25_ppl | 0.031 (R12) | 0.031 (R9) | 0.037 (R9) | 0.036 (R9) | 0.032 (R9) | 0.030 (R7) | 0.033 | 0.09 |
31	| skewness_ppl | 0.039 (R6) | 0.027 (R14) | 0.033 (R14) | 0.025 (R16) | 0.022 (R11) | 0.017 (R16) | 0.027 | 0.29 |
32	| kurtosis_ppl | 0.034 (R9) | 0.027 (R15) | 0.032 (R15) | 0.026 (R15) | 0.021 (R13) | 0.017 (R17) | 0.026 | 0.24 |
33	| bigram_entropy | 0.029 (R13) | 0.031 (R11) | 0.035 (R11) | 0.023 (R17) | 0.018 (R16) | 0.017 (R15) | 0.026 | 0.27 |
34	| trigram_entropy | 0.026 (R15) | 0.030 (R12) | 0.033 (R12) | 0.023 (R18) | 0.018 (R17) | 0.019 (R13) | 0.025 | 0.23 |
35	| p10_ppl | 0.025 (R16) | 0.027 (R13) | 0.033 (R13) | 0.029 (R11) | 0.021 (R12) | 0.021 (R11) | 0.026 | 0.17 |
36	| rep_2gram | 0.027 (R14) | 0.028 (R16) | 0.030 (R16) | 0.028 (R13) | 0.020 (R14) | 0.022 (R10) | 0.026 | 0.15 |
37	| rep_4gram | 0.024 (R17) | 0.029 (R17) | 0.028 (R17) | 0.029 (R12) | 0.019 (R15) | 0.018 (R14) | 0.025 | 0.19 |
38	| rep_3gram | 0.022 (R18) | 0.025 (R18) | 0.026 (R18) | 0.029 (R10) | 0.017 (R18) | 0.020 (R12) | 0.023 | 0.18 |
39	| var_ppl | 0.001 (R19) | 0.002 (R19) | 0.001 (R19) | 0.004 (R19) | 0.001 (R19) | 0.000 (R19) | 0.002 | 0.73 |
40	
41	## Spearman Rank Correlation Matrix (all 19 features)
42	
43	|  | Pyth_nuc | Pyth_t09 | Pyth_k50 | OLMo_nuc | GPT2_nuc | GPT2_t09 |
44	|---|---|---|---|---|---|---|
45	| Pyth_nuc | 1.000 | 0.849 | 0.849 | 0.647 | 0.904 | 0.518 |
46	| Pyth_t09 | — | 1.000 | **1.000** | 0.800 | 0.916 | 0.672 |
47	| Pyth_k50 | — | — | 1.000 | 0.800 | 0.916 | 0.672 |
48	| OLMo_nuc | — | — | — | 1.000 | 0.853 | 0.814 |
49	| GPT2_nuc | — | — | — | — | 1.000 | 0.739 |
50	| GPT2_t09 | — | — | — | — | — | 1.000 |
51	
52	All correlations p < 0.01 (n=19).
53	
54	## Cross-Strategy vs Cross-Model Consistency
55	
56	| Comparison Type | Pairs | Mean ρ |
57	|----------------|-------|--------|
58	| **Same model, different strategy** | Pyth nuc-t09 (0.849), nuc-k50 (0.849), t09-k50 (1.000), GPT2 nuc-t09 (0.739) | **0.859** |
59	| **Same strategy (nucleus), different model** | Pyth-OLMo (0.647), Pyth-GPT2 (0.904), OLMo-GPT2 (0.853) | **0.801** |
60	| **All cross-model pairs** | 11 pairs | **0.774** |
61	
62	Cross-strategy consistency (0.859) > cross-model consistency (0.801). Feature importance rankings are more stable across decoding strategies than across model architectures, but both are significantly correlated.
63	
64	## Universal Core Features
65	
66	**4 features appear in ALL 6 experiments' top-5:**
67	
68	| Feature | Rank Range | Importance Range | Interpretation |
69	|---------|-----------|-----------------|----------------|
70	| var_surprisal | 1–4 | 0.121–0.208 | Token-level surprise variance — the strongest single signal |
71	| p90_ppl | 1–2 | 0.135–0.263 | Extreme perplexity — captures worst-case confusion |
72	| mean_surprisal | 2–4 | 0.070–0.148 | Average token surprise level |
73	| p75_ppl | 3–5 | 0.061–0.146 | High-percentile perplexity |
74	
75	These 4 features account for **44–68%** of total importance across experiments:
76	- Pythia (3 strategies): 44–50%
77	- OLMo: 54%
78	- GPT-2 XL nucleus: 60%
79	- GPT-2 XL temp09: 68%
80	
81	**Near-universal (5/6):** mean_ppl (drops out in OLMo rank 8 and GPT2XL_t09 rank 18)
82	
83	## Notable Anomalies
84	
85	1. **mean_ppl collapse in GPT2XL_t09**: importance ≈ 0, rank 18. Likely due to collinearity with p90_ppl/p75_ppl — tree model redistributes importance among correlated features differently depending on data distribution.
86	
87	2. **Pythia t09 ≡ Pythia k50 (ρ=1.000)**: Identical rank orderings despite different decoding strategies. The temperature=0.9 and top-k=50 strategies produce nearly indistinguishable feature importance profiles on Pythia.
88	
89	3. **type_token_ratio enters OLMo top-5** (rank 5, 0.061) but stays at rank 6 in most others. OLMo may produce more distinctive vocabulary patterns at different depths.
90	
91	4. **var_ppl universally last** (rank 19 in all 6 experiments, importance < 0.004). This feature carries essentially no signal.
92	
93	## Tier Classification
94	
95	| Tier | Features | Avg Importance | Characterization |
96	|------|----------|---------------|------------------|
97	| **Tier 1: Core** | var_surprisal, p90_ppl | 0.169, 0.182 | Always top-2, dominant signal |
98	| **Tier 2: Strong** | mean_surprisal, p75_ppl | 0.094, 0.093 | Always top-5 |
99	| **Tier 3: Moderate** | mean_ppl, type_token_ratio, p50_ppl, hapax_ratio, entropy_of_surprisal, p25_ppl | 0.033–0.075 | Mid-range, some model-dependent |
100	| **Tier 4: Weak** | skewness/kurtosis_ppl, n-gram entropy, repetition metrics, p10_ppl | 0.023–0.027 | Low, noisy |
101	| **Tier 5: Null** | var_ppl | 0.002 | No signal |
102	
103	## Paper Figure Recommendations
104	
105	1. **Heatmap (recommended primary figure)**: 6 columns × 19 rows, rows sorted by mean importance. The "hot stripe" at the top visually demonstrates consistency. Add Spearman ρ annotations.
106	
107	2. **Rank stability bump chart**: x-axis = 6 experiments, y-axis = rank (1-19, inverted). Each feature is a line. Core features form stable parallel lines at top; weak features cross chaotically at bottom.
108	
109	3. **Top-4 bar chart (supplementary)**: Grouped bars showing core 4 features' importance across 6 experiments. Clean, focused on the key claim.
110	
111	## Key Takeaways for Paper
112	
113	1. **Surprise-based features dominate universally**: var_surprisal and p90_ppl are the two most important features in every experiment, regardless of model or strategy.
114	
115	2. **Feature importance is robust**: mean Spearman ρ across all 15 pairs = 0.79 (range 0.52–1.00). This is strong evidence that the signal is not an artifact of any specific model or decoding configuration.
116	
117	3. **Cross-strategy > cross-model stability**: supports the claim that recursive generation depth produces a model-general statistical signature, though decoding strategy has even less effect.
118	
119	4. **Perplexity distribution > lexical diversity**: the top features are all perplexity/surprisal-based. Lexical features (type_token_ratio, hapax_ratio, n-gram entropy, repetition) contribute <5% each.
120	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9cec8cf5-a61a-4a9c-bffd-e1fe25771d70",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "44d2fc47-6de4-4fcf-84e3-5afa75f88405",
  "sourceToolAssistantUUID": "9cec8cf5-a61a-4a9c-bffd-e1fe25771d70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Assistant

_source line 70 · 2026-05-23T10:21:02.717Z_

Now let me check the Pythia top-5 features from the paper's Table 2 vs data, and look for the GPT-2 XL temperature p90_ppl median values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44d2fc47-6de4-4fcf-84e3-5afa75f88405",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLGjeEpLNsGMrjc6B6D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10c48523-1f2b-477b-9caf-44707d24bf87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XW4YEhev4VXcetQAmNTN4U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4499,
      "cache_read_input_tokens": 104087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4499,
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

_source line 71 · 2026-05-23T10:21:04.740Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ug64yComPpWPWvvojZRuCV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/atlas_v2/feature_trajectory_summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10c48523-1f2b-477b-9caf-44707d24bf87",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLGjeEpLNsGMrjc6B6D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d46c7755-d1d2-4ad1-86b0-d4326fa9978d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XW4YEhev4VXcetQAmNTN4U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4499,
      "cache_read_input_tokens": 104087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4499,
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

_source line 72 · 2026-05-23T10:21:04.746Z_

<details><summary>↩ Tool result · `toolu_01Ug64yComPpWPWvvojZRuCV`</summary>

```text
1	{
2	  "pythia_nucleus": {
3	    "available": true,
4	    "feature_changes_d0_to_d3": {
5	      "p90_ppl": {
6	        "d0": 483.738,
7	        "d3": 18.152,
8	        "pct_change": -0.9625,
9	        "direction": "decrease"
10	      },
11	      "mean_surprisal": {
12	        "d0": 2.292,
13	        "d3": 0.951,
14	        "pct_change": -0.5851,
15	        "direction": "decrease"
16	      },
17	      "var_surprisal": {
18	        "d0": 6.497,
19	        "d3": 1.509,
20	        "pct_change": -0.7677,
21	        "direction": "decrease"
22	      },
23	      "p75_ppl": {
24	        "d0": 39.281,
25	        "d3": 5.064,
26	        "pct_change": -0.8711,
27	        "direction": "decrease"
28	      },
29	      "mean_ppl": {
30	        "d0": 25063.789,
31	        "d3": 2418.228,
32	        "pct_change": -0.9035,
33	        "direction": "decrease"
34	      },
35	      "type_token_ratio": {
36	        "d0": 0.508,
37	        "d3": 0.313,
38	        "pct_change": -0.3839,
39	        "direction": "decrease"
40	      },
41	      "rep_2gram": {
42	        "d0": 0.166,
43	        "d3": 0.443,
44	        "pct_change": 1.6687,
45	        "direction": "increase"
46	      },
47	      "rep_3gram": {
48	        "d0": 0.07,
49	        "d3": 0.326,
50	        "pct_change": 3.6571,
51	        "direction": "increase"
52	      },
53	      "rep_4gram": {
54	        "d0": 0.033,
55	        "d3": 0.261,
56	        "pct_change": 6.9091,
57	        "direction": "increase"
58	      }
59	    },
60	    "strongest_decrease": "p90_ppl",
61	    "strongest_increase": "rep_4gram"
62	  },
63	  "pythia_temp09": {
64	    "available": true,
65	    "feature_changes_d0_to_d3": {
66	      "p90_ppl": {
67	        "d0": 483.738,
68	        "d3": 17.394,
69	        "pct_change": -0.964,
70	        "direction": "decrease"
71	      },
72	      "mean_surprisal": {
73	        "d0": 2.292,
74	        "d3": 0.927,
75	        "pct_change": -0.5955,
76	        "direction": "decrease"
77	      },
78	      "var_surprisal": {
79	        "d0": 6.497,
80	        "d3": 1.598,
81	        "pct_change": -0.754,
82	        "direction": "decrease"
83	      },
84	      "p75_ppl": {
85	        "d0": 39.281,
86	        "d3": 4.442,
87	        "pct_change": -0.8869,
88	        "direction": "decrease"
89	      },
90	      "mean_ppl": {
91	        "d0": 25063.789,
92	        "d3": 6395.753,
93	        "pct_change": -0.7448,
94	        "direction": "decrease"
95	      },
96	      "type_token_ratio": {
97	        "d0": 0.508,
98	        "d3": 0.302,
99	        "pct_change": -0.4055,
100	        "direction": "decrease"
101	      },
102	      "rep_2gram": {
103	        "d0": 0.166,
104	        "d3": 0.44,
105	        "pct_change": 1.6506,
106	        "direction": "increase"
107	      },
108	      "rep_3gram": {
109	        "d0": 0.07,
110	        "d3": 0.325,
111	        "pct_change": 3.6429,
112	        "direction": "increase"
113	      },
114	      "rep_4gram": {
115	        "d0": 0.033,
116	        "d3": 0.254,
117	        "pct_change": 6.697,
118	        "direction": "increase"
119	      }
120	    },
121	    "strongest_decrease": "p90_ppl",
122	    "strongest_increase": "rep_4gram"
123	  },
124	  "pythia_topk50": {
125	    "available": false
126	  },
127	  "olmo_nucleus": {
128	    "available": true,
129	    "feature_changes_d0_to_d3": {
130	      "p90_ppl": {
131	        "d0": 483.738,
132	        "d3": 42.682,
133	        "pct_change": -0.9118,
134	        "direction": "decrease"
135	      },
136	      "mean_surprisal": {
137	        "d0": 2.292,
138	        "d3": 1.364,
139	        "pct_change": -0.4049,
140	        "direction": "decrease"
141	      },
142	      "var_surprisal": {
143	        "d0": 6.497,
144	        "d3": 2.487,
145	        "pct_change": -0.6172,
146	        "direction": "decrease"
147	      },
148	      "p75_ppl": {
149	        "d0": 39.281,
150	        "d3": 9.023,
151	        "pct_change": -0.7703,
152	        "direction": "decrease"
153	      },
154	      "mean_ppl": {
155	        "d0": 25063.789,
156	        "d3": 569854.183,
157	        "pct_change": 21.7362,
158	        "direction": "increase"
159	      },
160	      "type_token_ratio": {
161	        "d0": 0.508,
162	        "d3": 0.305,
163	        "pct_change": -0.3996,
164	        "direction": "decrease"
165	      },
166	      "rep_2gram": {
167	        "d0": 0.166,
168	        "d3": 0.432,
169	        "pct_change": 1.6024,
170	        "direction": "increase"
171	      },
172	      "rep_3gram": {
173	        "d0": 0.07,
174	        "d3": 0.316,
175	        "pct_change": 3.5143,
176	        "direction": "increase"
177	      },
178	      "rep_4gram": {
179	        "d0": 0.033,
180	        "d3": 0.253,
181	        "pct_change": 6.6667,
182	        "direction": "increase"
183	      }
184	    },
185	    "strongest_decrease": "p90_ppl",
186	    "strongest_increase": "mean_ppl"
187	  },
188	  "olmo_temp09": {
189	    "available": false
190	  },
191	  "gpt2xl_nucleus": {
192	    "available": true,
193	    "feature_changes_d0_to_d3": {
194	      "p90_ppl": {
195	        "d0": 483.738,
196	        "d3": 57.643,
197	        "pct_change": -0.8808,
198	        "direction": "decrease"
199	      },
200	      "mean_surprisal": {
201	        "d0": 2.292,
202	        "d3": 1.487,
203	        "pct_change": -0.3512,
204	        "direction": "decrease"
205	      },
206	      "var_surprisal": {
207	        "d0": 6.497,
208	        "d3": 2.473,
209	        "pct_change": -0.6194,
210	        "direction": "decrease"
211	      },
212	      "p75_ppl": {
213	        "d0": 39.281,
214	        "d3": 10.823,
215	        "pct_change": -0.7245,
216	        "direction": "decrease"
217	      },
218	      "mean_ppl": {
219	        "d0": 25063.789,
220	        "d3": 1076268.162,
221	        "pct_change": 41.9412,
222	        "direction": "increase"
223	      },
224	      "type_token_ratio": {
225	        "d0": 0.508,
226	        "d3": 0.376,
227	        "pct_change": -0.2598,
228	        "direction": "decrease"
229	      },
230	      "rep_2gram": {
231	        "d0": 0.166,
232	        "d3": 0.316,
233	        "pct_change": 0.9036,
234	        "direction": "increase"
235	      },
236	      "rep_3gram": {
237	        "d0": 0.07,
238	        "d3": 0.199,
239	        "pct_change": 1.8429,
240	        "direction": "increase"
241	      },
242	      "rep_4gram": {
243	        "d0": 0.033,
244	        "d3": 0.141,
245	        "pct_change": 3.2727,
246	        "direction": "increase"
247	      }
248	    },
249	    "strongest_decrease": "p90_ppl",
250	    "strongest_increase": "mean_ppl"
251	  },
252	  "gpt2xl_temp09": {
253	    "available": false
254	  }
255	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d46c7755-d1d2-4ad1-86b0-d4326fa9978d",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "212fcddc-7933-4ff7-ae30-b9a9ab870b52",
  "sourceToolAssistantUUID": "d46c7755-d1d2-4ad1-86b0-d4326fa9978d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-23T10:21:05.352Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CxBKo5d5pgMEnvGx7ii5Ev`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/matrix_3x3_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "212fcddc-7933-4ff7-ae30-b9a9ab870b52",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLGjeEpLNsGMrjc6B6D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50ab7dbc-695d-4bc4-ae2f-7fc7b68a77be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XW4YEhev4VXcetQAmNTN4U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4499,
      "cache_read_input_tokens": 104087,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4499
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 104087,
          "cache_creation_input_tokens": 4499,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4499,
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

_source line 74 · 2026-05-23T10:21:05.359Z_

<details><summary>↩ Tool result · `toolu_01CxBKo5d5pgMEnvGx7ii5Ev`</summary>

```text
1	# 3×3 递归生成深度估计矩阵综合分析
2	
3	> 生成日期: 2026-05-15 | 完成格子: 8/9 (gpt2xl_topk50 仍在运行)
4	
5	---
6	
7	## 1. 完整 3×3 矩阵
8	
9	### 1.1 4-class RF Accuracy (%)
10	
11	| 模型 | nucleus p=0.95 | temp τ=0.9 | top-k k=50 | 跨策略均值 |
12	|------|:-:|:-:|:-:|:-:|
13	| **Pythia-1.4B** | 78.2 `mvp_pipeline_pythia_002` | 76.3 `pythia_temp09_001` | 69.6 `pythia_topk50_001` | 74.7 |
14	| **OLMo-1B** | 78.8 `cross_model_olmo_002` | 82.0 `olmo_temp09_001` | 74.2 `olmo_topk50_001` | 78.3 |
15	| **GPT-2 XL** | 83.3 `cross_model_gpt2xl_001` | 85.4 `gpt2xl_temp09_001` | 🔄 `gpt2xl_topk50_001` | 84.4† |
16	| **跨模型均值** | 80.1 | 81.2 | 71.9† | — |
17	
18	> † GPT-2 XL 行均值仅含 2 格; topk50 列均值仅含 2 格。所有数值为 RF classifier，chance = 25%。
19	
20	### 1.2 Pairwise d1v2 AUC (RF)
21	
22	| 模型 | nucleus p=0.95 | temp τ=0.9 | top-k k=50 |
23	|------|:-:|:-:|:-:|
24	| **Pythia-1.4B** | 0.861 `mvp_pipeline_pythia_002` | 0.833 `pythia_temp09_001` | 0.752 `pythia_topk50_001` |
25	| **OLMo-1B** | 0.867 `cross_model_olmo_002` | 0.901 `olmo_temp09_001` | 0.831 `olmo_topk50_001` |
26	| **GPT-2 XL** | 0.913 `cross_model_gpt2xl_001` | 0.937 `gpt2xl_temp09_001` | 🔄 |
27	
28	### 1.3 3-class Filtered Accuracy (RF, %)
29	
30	| 模型 | nucleus p=0.95 | temp τ=0.9 | top-k k=50 |
31	|------|:-:|:-:|:-:|
32	| **Pythia-1.4B** | 74.7 `mvp_pipeline_pythia_002` | 72.5 `pythia_temp09_001` | 61.3 `pythia_topk50_001` |
33	| **OLMo-1B** | 74.4* `cross_model_olmo_002` | 77.6 `olmo_temp09_001` | 67.0 `olmo_topk50_001` |
34	| **GPT-2 XL** | 79.3* `cross_model_gpt2xl_001` | 81.5 `gpt2xl_temp09_001` | 🔄 |
35	
36	> \* OLMo nucleus 和 GPT-2 XL nucleus 使用 unfiltered 3-class accuracy 作为近似值（两者 code contamination 均 <3%，filtered 与 unfiltered 差异极小）。
37	
38	---
39	
40	## 2. 模型效应分析
41	
42	跨策略平均（RF 4-class accuracy）:
43	
44	| 模型 | 均值 | 相对 Pythia | 参数量 |
45	|------|------|-------------|--------|
46	| Pythia-1.4B | 74.7% | — | 1.4B |
47	| OLMo-1B | 78.3% | +3.6pp | 1B |
48	| GPT-2 XL | 84.4%† | +9.7pp | 1.5B |
49	
50	**关键发现:**
51	
52	1. **GPT-2 XL 全面领先**：在每个策略上均为最高分（nucleus +4.5pp vs OLMo, temp09 +3.4pp, d1v2 AUC 最高均 >0.91），说明模型架构/预训练数据对深度信号的影响远大于模型规模（GPT-2 XL 1.5B vs OLMo 1B 参数量差异有限但性能差距显著）。
53	
54	2. **OLMo 优于 Pythia 但差距较小**：跨策略仅 +3.6pp，且两者在 nucleus 策略上几乎持平（78.8% vs 78.2%，仅 +0.6pp），差异主要来自 temp09（+5.8pp）。
55	
56	3. **模型效应 > 策略效应**：模型维度的跨策略均值极差 = 9.7pp（84.4 − 74.7），而策略维度的跨模型均值极差 = 9.3pp（81.2 − 71.9），两者量级相当，但模型效应在排除 topk50（仅 2 格）后更稳定。
57	
58	---
59	
60	## 3. 策略效应分析
61	
62	跨模型平均（RF 4-class accuracy）:
63	
64	| 策略 | 均值 | 相对 nucleus | 特点 |
65	|------|------|-------------|------|
66	| nucleus p=0.95 | 80.1% | — | 基准策略 |
67	| temp τ=0.9 | 81.2% | +1.1pp | 部分模型优于 nucleus |
68	| top-k k=50 | 71.9%† | −8.2pp | 系统性最弱 |
69	
70	**关键发现:**
71	
72	1. **top-k 系统性削弱深度信号**：相比 nucleus，Pythia −8.6pp，OLMo −4.6pp。top-k 的硬截断采样将概率分布截断到固定 k 个 token，可能丢失了分布尾部携带的深度相关信号。
73	
74	2. **temperature 与 nucleus 几乎等效**：跨模型均值仅差 1.1pp，且方向不一致——Pythia temp09 < nucleus（−1.9pp），OLMo 和 GPT-2 XL temp09 > nucleus（+3.2pp, +2.1pp）。温度缩放保留了完整分布形状，只改变了锐度。
75	
76	3. **策略效应的模型依赖性**：同一策略变化在不同模型上方向相反（Pythia temp09 降，OLMo/GPT-2 XL temp09 升），说明策略效应不是纯粹的采样特性，而是与模型内部表征交互的结果。
77	
78	---
79	
80	## 4. 交互效应分析
81	
82	将每个格子的 RF accuracy 分解为 模型均值 + 策略均值 + 残差（交互项）:
83	
84	| 模型×策略 | 实际 | 预期† | 残差 | 解读 |
85	|-----------|------|-------|------|------|
86	| Pythia × nucleus | 78.2 | 77.4 | +0.8 | 略高于预期 |
87	| Pythia × temp09 | 76.3 | 77.9 | −1.6 | temp09 对 Pythia 不利 |
88	| Pythia × topk50 | 69.6 | 68.8 | +0.8 | 符合预期 |
89	| OLMo × nucleus | 78.8 | 80.7 | −1.9 | nucleus 未充分发挥 OLMo 潜力 |
90	| OLMo × temp09 | 82.0 | 81.2 | +0.8 | temp09 对 OLMo 微弱正交互 |
91	| OLMo × topk50 | 74.2 | 72.4 | +1.8 | topk50 对 OLMo 影响小于预期 |
92	| GPT-2 XL × nucleus | 83.3 | 82.5 | +0.8 | 符合预期 |
93	| GPT-2 XL × temp09 | 85.4 | 83.6 | +1.8 | temp09 对 GPT-2 XL 最有利 |
94	
95	> † 预期值 = grand mean + (模型偏差) + (策略偏差)，基于加法模型。Grand mean = 78.5%（8格均值）。
96	
97	**异常组合:**
98	
99	- **GPT-2 XL × temp09 (+1.8pp residual)**：温度缩放对 GPT-2 XL 有增强效应。可能原因：GPT-2 XL 的预训练分布在 τ=0.9 下产生更多样化但仍有结构性的文本，增强了深度间的统计差异。
100	- **OLMo × nucleus (−1.9pp residual)**：OLMo 在 nucleus 下表现低于其在其他策略下的相对优势。top-p truncation 可能对 OLMo 的 logit 分布有不利影响。
101	- **Pythia × temp09 (−1.6pp residual)**：Pythia 是唯一在 temp09 下低于 nucleus 的模型，与 OLMo/GPT-2 XL 方向相反。
102	
103	---
104	
105	## 5. Feature Importance 稳定性分析
106	
107	Top-5 features 在 8 个实验中的出现情况:
108	
109	| Feature | 出现次数 (8格中) | 平均排名 | 出现实验 |
110	|---------|:-:|:-:|---------|
111	| **p90_ppl** | 8/8 | 1.5 | 所有 |
112	| **var_surprisal** | 8/8 | 1.8 | 所有 |
113	| **p75_ppl** | 8/8 | 3.1 | 所有 |
114	| **mean_surprisal** | 7/8 | 4.0 | 除 OLMo temp09（仅报告 top-3）|
115	| **mean_ppl** | 5/8 | 3.8 | Pythia 全部 3 格 + GPT-2 XL nucleus + GPT-2 XL temp09 |
116	| p25_ppl | 1/8 | 5.0 | OLMo topk50 |
117	| type_token_ratio | 1/8 | 5.0 | OLMo nucleus |
118	
119	**稳定性评估:**
120	
121	- **核心三特征 (p90_ppl, var_surprisal, p75_ppl)** 在全部 8 格出现，Jaccard 一致性 = 1.0。这三个特征是递归生成深度信号的核心载体，反映了困惑度分布的上尾和变异性。
122	- **前 4 特征**在 7/8 格一致（mean_surprisal 在 OLMo temp09 中未被明确报告但可能位于 rank 4-5）。
123	- **第 5 位特征模型依赖**：Pythia 偏好 mean_ppl，OLMo 偏好 type_token_ratio 或 p25_ppl。GPT-2 XL 偏好 mean_ppl。
124	- **跨模型/策略的特征重要性高度稳定**，支持「深度信号来自同一统计模式」的假设——不同模型/策略的递归生成都导致困惑度分布的类似退化。
125	
126	### 代表性 importance 权重对比
127	
128	| Feature | Pythia nuc | OLMo nuc | GPT-2 XL nuc |
129	|---------|:-:|:-:|:-:|
130	| p90_ppl | 0.158 | 0.180 | 0.208 |
131	| var_surprisal | 0.169 | 0.160 | 0.208 |
132	| p75_ppl | 0.067 | 0.110 | 0.103 |
133	
134	GPT-2 XL 的 top-2 特征权重更高（0.208 vs 0.158/0.180），说明深度信号在更大模型中更集中于少数关键特征。
135	
136	---
137	
138	## 6. Code Contamination 模式分析
139	
140	### 6.1 按模型的 narrow contamination rate (%)
141	
142	| 模型 | d0 | d1 | d2 | d3 | d3 趋势 |
143	|------|:-:|:-:|:-:|:-:|---------|
144	| **Pythia-1.4B** (nucleus) | — | 5.0 | 9.0 | 12.0 | 递增 ↑ |
145	| **Pythia-1.4B** (temp09) | 0.4 | 7.7 | 11.6 | 13.6 | 递增 ↑ |
146	| **Pythia-1.4B** (topk50) | 0.4 | 7.7 | 12.3 | 13.1 | 递增 ↑ |
147	| **OLMo-1B** (nucleus) | 0.5 | 2.7 | 0.7 | 0.8 | 极低, 平稳 |
148	| **OLMo-1B** (temp09) | — | ≤0.7 | ≤0.7 | ≤0.7 | 极低 |
149	| **OLMo-1B** (topk50) | 0.4 | 0.8 | 0.3 | 0.4 | 极低, 平稳 |
150	| **GPT-2 XL** (nucleus) | 0.5 | 0.5 | 1.3 | 0.7 | 极低, 平稳 |
151	| **GPT-2 XL** (temp09) | 0.4 | 0.8 | 1.6 | 1.5 | 低, 微增 |
152	
153	### 6.2 关键模式
154	
155	1. **Pythia 是 contamination 热点**：d3 contamination 达 12-14%，显著高于 OLMo（<1%）和 GPT-2 XL（<2%）。原因：Pythia 预训练于 The Pile（含 ~3.3% 代码），递归 finetune 逐深度放大代码模式。
156	
157	2. **模型效应远大于策略效应**：Pythia 三种策略的 contamination 模式高度一致（d3: 12.0% / 13.6% / 13.1%），说明 contamination 主要由预训练数据决定，与解码策略无关。
158	
159	3. **OLMo 和 GPT-2 XL 几乎无 contamination**：所有深度的 narrow rate <3%，filtered 与 unfiltered 性能差异 <1pp。
160	
161	4. **Pythia 的 contamination 未驱动分类性能**：Pythia topk50 有最高 contamination（d3=13.1%），但分类性能最低（69.6%）。移除 contaminated 样本后（filtered 3-class），性能反而微升（61.3% vs 59.2% unfiltered 3-class），确认深度信号非代码混入的伪影。
162	
163	---
164	
165	## 7. 关键 Findings 摘要（论文可用）
166	
167	### Finding 1: 递归生成深度信号是跨模型、跨策略的普遍现象
168	所有 8 个完成的模型-策略组合均显著优于 chance（25%），4-class accuracy 范围 69.6%–85.4%，d1v2 AUC 范围 0.752–0.937。深度信号不依赖于特定模型或采样策略。
169	
170	### Finding 2: 模型效应显著——GPT-2 XL 全面优于小模型
171	GPT-2 XL 跨策略均值 84.4%，高出 Pythia-1.4B +9.7pp、OLMo-1B +6.1pp。更大/更强的模型在递归 finetune 中产生更强的深度退化信号，可能因为其分布更复杂，每轮递归的信息损失更可量化。
172	
173	### Finding 3: 采样策略对信号强度有显著但非均匀影响
174	Top-k (k=50) 系统性地削弱深度信号（跨模型均值 71.9% vs nucleus 80.1%，−8.2pp），而 temperature (τ=0.9) 与 nucleus (p=0.95) 效果接近（81.2% vs 80.1%）。关键差异：top-k 硬截断分布尾部，而 temperature 和 nucleus 保留完整分布形状，后者保留了更多深度相关的统计信息。
175	
176	### Finding 4: 深度信号由高度稳定的特征组集载体
177	p90_ppl、var_surprisal、p75_ppl 在全部 8 格中均为 top-3 特征（Jaccard = 1.0）。递归生成导致困惑度分布的上尾收缩和变异性降低——这一退化模式跨模型、跨策略完全一致。
178	
179	### Finding 5: Code contamination 是模型特异的，不驱动分类性能
180	Pythia-1.4B 在 d3 有 12-14% 代码混入（The Pile 代码占比高），而 OLMo-1B 和 GPT-2 XL 均 <2%。但 contamination 与分类性能无正相关——Pythia 性能最低而 contamination 最高。过滤后性能无显著下降，确认深度信号来自语言统计模式而非域混淆。
181	
182	---
183	
184	## 附录 A: 完整 pairwise AUC 矩阵 (RF)
185	
186	### Pythia-1.4B nucleus `mvp_pipeline_pythia_002`
187	| pair | AUC |
188	|------|-----|
189	| d0v1 | 0.9975 |
190	| d0v2 | — |
191	| d0v3 | — |
192	| d1v2 | 0.8607 |
193	| d1v3 | 0.9569 |
194	| d2v3 | 0.8005 |
195	
196	### Pythia-1.4B temp09 `pythia_temp09_001`
197	| pair | AUC |
198	|------|-----|
199	| d0v1 | 0.9968 |
200	| d1v2 | 0.8327 |
201	| d1v3 | 0.9590 |
202	| d2v3 | 0.7928 |
203	
204	### Pythia-1.4B topk50 `pythia_topk50_001`
205	| pair | AUC |
206	|------|-----|
207	| d0v1 | 0.9927 |
208	| d0v2 | 0.9983 |
209	| d0v3 | 0.9978 |
210	| d1v2 | 0.7518 |
211	| d1v3 | 0.9176 |
212	| d2v3 | 0.6918 |
213	
214	### OLMo-1B nucleus `cross_model_olmo_002`
215	| pair | AUC |
216	|------|-----|
217	| d0v1 | 0.9834 |
218	| d0v2 | 0.9949 |
219	| d0v3 | 0.9989 |
220	| d1v2 | 0.8673 |
221	| d1v3 | 0.9806 |
222	| d2v3 | 0.8124 |
223	
224	### OLMo-1B temp09 `olmo_temp09_001`
225	| pair | AUC |
226	|------|-----|
227	| d1v2 | 0.901 |
228	
229	### OLMo-1B topk50 `olmo_topk50_001`
230	| pair | AUC |
231	|------|-----|
232	| d0v1 | 0.9930 |
233	| d0v2 | 0.9983 |
234	| d0v3 | 0.9991 |
235	| d1v2 | 0.8305 |
236	| d1v3 | 0.9591 |
237	| d2v3 | 0.7357 |
238	
239	### GPT-2 XL nucleus `cross_model_gpt2xl_001`
240	| pair | AUC |
241	|------|-----|
242	| d0v1 | 0.9941 |
243	| d0v2 | 0.9965 |
244	| d0v3 | 0.9988 |
245	| d1v2 | 0.9131 |
246	| d1v3 | 0.9857 |
247	| d2v3 | 0.8829 |
248	
249	### GPT-2 XL temp09 `gpt2xl_temp09_001`
250	| pair | AUC (RF) |
251	|------|-----|
252	| d0v1 | 0.9963 |
253	| d0v2 | 0.9992 |
254	| d0v3 | 1.0000 |
255	| d1v2 | 0.9367 |
256	| d1v3 | 0.9947 |
257	| d2v3 | 0.8815 |
258	
259	---
260	
261	## 附录 B: Finetune Loss 趋势
262	
263	| 模型×策略 | d0→d1 loss | d1→d2 loss | d2→d3 loss |
264	|-----------|:-:|:-:|:-:|
265	| Pythia nucleus | 2.241 → 1.389 | 1.389 → 1.025 | — |
266	| Pythia temp09 | 2.222 → 1.370 | 1.370 → 1.006 | — |
267	| Pythia topk50 | 2.241 → 1.670 | 1.670 → 1.437 | — |
268	| OLMo nucleus | 2.269 → 1.650 | 1.650 → 1.226 | — |
269	| OLMo temp09 | 2.270 → 1.630 | 1.630 → 1.180 | — |
270	| OLMo topk50 | — → 1.946 | 1.946 → 1.726 | — |
271	| GPT-2 XL nucleus | 2.550 → 1.715 | 1.715 → 1.342 | — |
272	| GPT-2 XL temp09 | 2.550 → 1.697 | 1.697 → 1.292 | — |
273	
274	所有配置均呈单调递减——每轮递归 finetune 后模型更容易学习下一轮生成的文本，支持「深度增加 → 分布收敛」假设。
275	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50ab7dbc-695d-4bc4-ae2f-7fc7b68a77be",
  "isSidechain": true,
  "promptId": "87a0d0ac-6dea-4b97-8983-2e9d026c330c",
  "agentId": "a563e433f634db794",
  "type": "user",
  "uuid": "82fb92dc-fd54-4713-932f-be9eeb73bcee",
  "sourceToolAssistantUUID": "50ab7dbc-695d-4bc4-ae2f-7fc7b68a77be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle"
}
```

</details>

---

### Assistant

_source line 75 · 2026-05-23T10:24:30.075Z_

Now I have comprehensive data from all the tex files and artifact sources. Let me compile the full audit report by cross-referencing every numerical claim in the main text against the source data.

Here is the complete numerical audit:

---

## DATA CONSISTENCY AUDIT REPORT

### METHODOLOGY
Every specific numerical claim in the 8 main-text .tex files was extracted and traced to its source in appendix tables or artifact data files (`matrix_data.json`, `edd_threshold_sensitivity.json`, `cross_model_loo_results.txt`, `cross_strategy_loo_results.md`, etc.).

---

### 1. abstract.tex

| Line | Claim | Source | Status |
|------|-------|--------|--------|
| 3 | "180K cell-instances (140K unique passages)" | method.tex L30: 5000 samples x 4 depths x 9 cells = 180K; d0 shared across cells = 140K unique | **MATCH** |
| 3 | "three model families, three decoding strategies, and four depths" | matrix_data.json grid: 3 models x 3 strategies x 4 depths | **MATCH** |
| 4 | "19 statistical features" | method.tex Table 3: 9+3+4+3=19 | **MATCH** |
| 4 | "d1-d3 balanced accuracy of 59-82%" | Table 1: range 58.9% (Pythia top-k) to 81.5% (GPT-2 XL temp). Abstract says "59-82%", table says 58.9-81.5% | **MISMATCH** (minor rounding: 58.9 rounds to 59, but 81.5 rounds to 82 only loosely) |
| 4 | "EDD_0.70 = 3 in 8/9 cells" | edd_threshold_sensitivity.json: at T=0.70, edd3_count = 8 | **MATCH** |
| 5 | "14B cross-reference accuracy ~44%" | appendix tab:cross_ref_14b: mean cross-ref = 44.1% | **MATCH** |
| 5 | "EDD_0.70=2 for nucleus and temperature, 0 for top-k" | appendix tab:cross_ref_14b: nucleus EDD=2, temp EDD=2, top-k EDD=0 | **MATCH** |
| 5 | "reference-model choice shifting accuracy by ~7 pp" | appendix tab:cross_ref_14b: mean delta = -6.8 pp. Abstract says "~7 pp" | **MATCH** (6.8 rounds to ~7) |
| 6 | "+11.5 pp under cross-strategy transfer" | generalization.tex L75: "70.5%, +11.5 pp" | **MATCH** (internally consistent) |
| 7 | "DetectGPT, 28.8%" and "Min-K% Prob, 33.2%" | Table baselines: DetectGPT 28.8%, Min-K% 33.2% | **MATCH** |

---

### 2. introduction.tex

| Line | Claim | Source | Status |
|------|-------|--------|--------|
| 16 | "convergence of four classifiers within 0.8 pp" | appendix tab:learned_estimator: RF 66.4, XGBoost 67.2, Ord MLP 66.7, Prototypical 66.6 => spread = 67.2-66.4 = 0.8 pp | **MATCH** |
| 17 | "effective dimensionality ~4-5 due to multicollinearity" | atlas.tex L43: "VIF>10 for 14-16 of 19 features" | **MATCH** (qualitative) |
| 18 | "180K cell-instances" | Consistent with above | **MATCH** |
| 29 | "180K cell-instance benchmark (3 model families x 3 strategies x 4 depths; 140K unique passages)" | Same as abstract | **MATCH** |
| 31 | "EDD_0.70=3 in 8/9 cells" | edd_threshold_sensitivity.json | **MATCH** |
| 31 | "4 under nucleus depth extension" | appendix tab:cross_scale: nucleus EDD_0.70 = 4 for all three 1-1.5B models | **MATCH** |
| 31 | "validated by 5-class extension (71-81%)" | appendix sec:depth4_ext: 71.3% (Pythia), 74.0% (GPT-2 XL), 80.5% (OLMo). Range = 71.3-80.5%. Claim "71-81%" | **MATCH** (80.5 rounds to ~81) |
| 31 | "feature group ablation confirms perplexity tail dominance (76.6% alone vs. 78.4% full set)" | appendix tab:feature_ablation_indist: Perplexity only 76.6%, Full 78.4% | **MATCH** |
| 33 | "25-50% synthetic mixing, EDD_0.70=3 is preserved in 5/6 cells" | appendix tab:accum_auc: 5/6 cells have all AUCs >= 0.70 (GPT-2 XL 50% fails at d2v3=0.695) | **MATCH** |
| 33 | "-8-15 pp accuracy attenuation" | **UNVERIFIED** -- the accumulation appendix reports AUC values but not 4-class accuracy attenuation directly. The "-8-15 pp" claim needs explicit source data. |
| 35 | "cross-model transfer reaches 66.4%" | cross_model_loo_results.txt: mean = 0.664 | **MATCH** |
| 35 | "cross-domain (arXiv) 74.1%" | appendix sec:cross_boundary L682: "74.1% +/- 2.0%" | **MATCH** |
| 35 | "at 14B, cross-reference EDD_0.70=2" | appendix tab:cross_ref_14b: nucleus=2, temp=2 (top-k=0) | **MATCH** (for nucleus/temp; top-k is 0, not mentioned in this bullet) |
| 35 | "cross-strategy (d1-d3: 45.9%)" | generalization.tex L74 | **MATCH** (internally consistent; source artifact: cross_strategy_loo_results.md does not report d1-d3 directly) |
| 35 | "two-stage routing (+11.5 pp)" | Consistent with abstract and generalization.tex | **MATCH** |

---

### 3. theory.tex

| Line | Claim | Source | Status |
|------|-------|--------|--------|
| 10 | "AUC-excess contraction ratio 0.80 at d1v2->d2v3, 0.69 at d3v4->d4v5" | Pythia nucleus: d1v2 AUC excess = 0.8607-0.5 = 0.3607; d2v3 excess = 0.8005-0.5 = 0.3005; ratio = 0.3005/0.3607 = 0.833. Paper says 0.80. For depth extension (d3v4, d4v5), values from AUC decay figure. | **UNVERIFIED** (the 0.80 ratio doesn't exactly match the d0-d3 data available; this may come from the d0-d5 extension data on the server) |
| 11 | "5-class extensions to d4 (71-81%, chance = 20%)" | appendix sec:depth4_ext: 71.3-80.5% | **MATCH** |
| 15 | "Qwen2.5-14B d0-vs-d1 AUC drops to 0.643 (vs. >0.99 at 1-1.5B)" | appendix tab:cross_scale_auc: 14B nucleus d0v1 = 0.643. matrix_data.json: all 1-1.5B d0v1 > 0.98 (not >0.99 for OLMo = 0.9834) | **MINOR MISMATCH** -- OLMo d0v1 = 0.9834, which is >0.98 but not >0.99. Paper says ">0.99". |
| 20 | "temperature d1 median p90_ppl (92.2) matches the nucleus d2 median (92.3)" | **UNVERIFIED** -- these are median values from the server-side data, not available in local artifacts (local data has mean values, not medians). The matrix_data.json feature_trajectory contains means, not medians. GPT-2 XL is claimed here but values would need raw feature data. |
| 21 | "top-k cells yield the lowest accuracy (68.9-75.8%)" | Table 1: Pythia top-k = 68.9, GPT-2 XL top-k = 75.8. OLMo top-k = 74.4. Range = 68.9-75.8% | **MATCH** |

---

### 4. atlas.tex

| Line | Claim | Source | Status |
|------|-------|--------|--------|
| 12 | "Accuracy ranges from 68.9% (Pythia, top-k) to 85.9% (GPT-2 XL, temperature)" | matrix_data.json: pythia_topk50 = 0.696 (69.6%), gpt2xl_temp09 = 0.8542 (85.4%). **Table 1 in paper says 68.9 and 85.9.** | **MISMATCH** -- matrix_data.json has Pythia top-k at 69.6% and GPT-2 XL temp at 85.42%. The paper table reports 68.9 and 85.9. These appear to be **different numbers from the underlying data**. See detailed analysis below. |
| 12 | "d1-d3 balanced: 58.9-81.5%" | Table 1 parenthesized values | **INTERNALLY CONSISTENT** but artifact data only has 3-class acc for some cells (see below) |
| 14 | "GPT-2 XL (75.8-85.9%)" | Table 1 values | Same caveat as above |
| 14 | "OLMo (74.4-82.3%)" | matrix_data.json: olmo_nucleus=0.788 (78.8%), olmo_temp09=0.8203 (82.0%). Paper says 82.3%. | **MISMATCH** -- matrix_data.json has OLMo temp at 82.03%, paper Table 1 says 82.3% |
| 14 | "Pythia (68.9-78.7%)" | matrix_data.json: pythia_nucleus=0.782 (78.2%), paper says 78.7% | **MISMATCH** |
| 16 | "mean within-model strategy gap is 9.3 pp" | From Table 1 values (paper): GPT-2 XL range = 85.9-75.8 = 10.1; OLMo range = 82.3-74.4 = 7.9; Pythia range = 78.7-68.9 = 9.8. Mean = (10.1+7.9+9.8)/3 = 9.27 pp | **MATCH** (rounds to 9.3) |
| 16 | "7.2 pp mean within-strategy model gap" | From Table 1: nucleus range = 84.3-78.7 = 5.6; temp range = 85.9-76.8 = 9.1; top-k range = 75.8-68.9 = 6.9. Mean = (5.6+9.1+6.9)/3 = 7.2 | **MATCH** |
| 36 | "Depth-0 recall exceeds 97% in all 9 cells" | appendix tab:per_class_recall: minimum d0 = 97.8% (OLMo nuc) | **MATCH** |
| 37 | "d2 consistently yields the lowest recall (44-73%)" | appendix tab:per_class_recall: d2 range = 44.2% (Pythia top-k) to 73.0% (GPT-2 XL temp) | **MATCH** |
| 43 | "VIF>10 for 14-16 of 19 features" | Claimed consistently | **INTERNALLY CONSISTENT** |
| 44 | "17.1 pp accuracy spread" | 85.9 - 68.9 = 17.0, not 17.1. If using paper Table 1 values: 85.9 - 68.9 = 17.0 | **MINOR MISMATCH** (17.0 vs 17.1) |
| 45 | "Kendall's W=0.90, p<0.005" | Reported in appendix permutation section | **MATCH** |
| 46 | "bootstrap rank 1.4 and 1.7" | appendix tab:conditional_pi: var_surprisal avg rank = 1.4, p90_ppl avg rank = 1.7 | **MATCH** |
| 49 | "Spearman rho = 0.868 ([0.619, 0.954])" | feature_consistency.json: Pythia-GPT2XL rho=0.904, OLMo-GPT2XL rho=0.853, Pythia-OLMo rho=0.647. Mean of **nucleus only** = (0.904+0.853+0.647)/3 = 0.801. Paper claims 0.868. | **MISMATCH** -- The mean of the three nucleus-only correlations from the local artifact is 0.801, not 0.868. The paper may be averaging across all strategies (6 experiments), where the feature_importance_consistency_analysis.md shows "All cross-model pairs" mean = 0.774 and "same strategy (nucleus)" mean = 0.801. Neither matches 0.868. Possible source: could be the "same model, different strategy" mean = 0.859, but that's cross-strategy not cross-model. |
| 50 | "Top-k yields the highest cross-model rank correlation (rho = 0.811)" | **UNVERIFIED** -- only 2 complete top-k cells in local data. Cannot verify. |
| 52 | "top-5 features achieve 97.6% of full accuracy (76.5% vs. 78.4%)" | 76.5/78.4 = 0.9758 = 97.6%. Appendix tab:feature_ablation reports p90_ppl single feature at 58.3% and full cross-model at 66.4%. But in-distribution: full = 78.4%. The 76.5% for top-5 is not directly in the appendix tables. | **UNVERIFIED** (76.5% top-5 number not found in appendix tables; only group ablations are tabulated) |
| 52 | "perplexity features alone reach 76.6%, surprisal 73.2%, lexical diversity <=47%, and repetition <=44%" | appendix tab:feature_ablation_indist: Perplexity 76.6%, Surprisal 73.2%, Lexical 46.1%, Repetition 43.7%. Claims "<=47%" and "<=44%" | **MATCH** (46.1 < 47, 43.7 < 44) |
| 52 | "Best single feature (p90_ppl) achieves 58.3%" | appendix tab:feature_ablation (cross-model): p90_ppl only = 58.3% | **MATCH** |
| 52 | "mean perplexity (25.1%)" | generalization.tex L19: "mean perplexity (25.1%)" | **MATCH** (internally consistent) |
| 93 | "Spearman rho = -1.0 for perplexity tail statistics" | monotonicity_scores.json: actual Spearman rho values are -0.82 to -0.89, NOT -1.0 | **MISMATCH** -- The paper claims Spearman rho = -1.0 for perplexity tail statistics. The artifact data shows rho values of -0.824 to -0.887 for p90_ppl and -0.832 to -0.874 for var_surprisal. These are the per-sample correlations. The paper may mean across depth-level means (4 points, all decreasing => rho = -1.0), which is a different calculation. If so, this should be clarified. |
| 93 | "d0-vs-d1 AUC >0.99 in all 9 cells" | edd_threshold_sensitivity.json: minimum d0v1 = 0.9906 (gpt2xl_topk50). 0.9906 > 0.99? Yes. But OLMo nucleus d0v1 = 0.9834 which is < 0.99. | **MISMATCH** -- OLMo nucleus d0v1 = 0.9834, which is NOT > 0.99. |
| 93 | "d2-vs-d3: 0.69-0.89" | edd_threshold_sensitivity.json: d2v3 ranges from 0.6918 (Pythia top-k) to 0.8829 (GPT-2 XL nucleus). Range = 0.69-0.88, not 0.69-0.89. | **MINOR MISMATCH** (0.8829 rounds to 0.88, not 0.89) |
| 100 | "AUC decays monotonically from 0.999 (d0v1) to 0.683 (d4v5)" for Pythia nucleus | matrix_data.json: d0v1 = 0.9975. Paper says 0.999. | **MINOR MISMATCH** (0.9975 vs 0.999) |
| 101 | "d3-vs-d4 AUC: Pythia 0.784, OLMo 0.765, GPT-2 XL 0.750" | appendix depth4_ext L728: "d3v4 AUC: Pythia 0.784, OLMo 0.765, GPT-2 XL 0.750" | **MATCH** (internally consistent) |
| 101 | "d4-vs-d5 converges to 0.681-0.684, range 0.003" | **UNVERIFIED** -- d4v5 data is on server only |
| 102 | "Bootstrap p = 0.001 (Pythia), 0.091 (OLMo), 0.505 (GPT-2 XL)" | **UNVERIFIED** -- bootstrap test results not in local artifacts |
| 105 | "at T=0.65, all cells achieve EDD=3" | edd_threshold_sensitivity.json: T=0.65 count = 9 | **MATCH** |
| 105 | "at T=0.70, 8/9 cells" | edd_threshold_sensitivity.json: T=0.70 count = 8 | **MATCH** |
| 105 | "at T=0.75, 7/9" | edd_threshold_sensitivity.json: T=0.75 count = 7 | **MATCH** |
| 105 | "at T=0.80, 5/9" | edd_threshold_sensitivity.json: T=0.80 count = 5 | **MATCH** |
| 106 | "Pythia top-k at T=0.70, OLMo top-k at T=0.75" | edd_threshold_sensitivity.json: cells_that_drop at 0.70 = ["pythia_topk50"], at 0.75 = ["olmo_topk50"] | **MATCH** |
| 120 | "GPT-2 XL 85.9%, OLMo 82.3%" (temperature) | Paper Table 1 values. matrix_data.json: 85.42% and 82.03% | **MISMATCH** (see Table 1 analysis below) |
| 121 | "68.9-75.8%" (top-k range) | Paper Table 1 values | **MATCH** (with Table 1) |
| 122 | "strategy effect (9.3 pp range)" | Computed from Table 1 as shown above | **MATCH** |
| 122 | "model effect (7.2 pp)" | Computed from Table 1 as shown above | **MATCH** |

---

### 5. generalization.tex

| Line | Claim | Source | Status |
|------|-------|--------|--------|
| 4 | "68.9-85.9% four-class; d1-d3: 58.9-81.5%" | Table 1 values | Same caveats as above |
| 10 | "0.8 pp under cross-model transfer" | appendix tab:learned_estimator: spread = 67.2-66.4 = 0.8 | **MATCH** |
| 13 | "DeBERTa-v3-base (LoRA, 53-61%)" | Table baselines: 53.1-60.6% and appendix tab:e2e_detail: 58.3% | **MATCH** |
| 13 | "RoBERTa-DCOL (ordinal contrastive, 64.5%)" | Table baselines and appendix tab:dcol_iterations v6 | **MATCH** |
| 13 | "lag RF by 14-33 pp" | RF = 78.7% (Pythia nuc). DeBERTa = 53.1-60.6 => gap = 18.1-25.6 pp. If RF = 78.4 (mean): gap from 53.1 = 25.3, from 64.5 = 13.9. Paper says "14-33 pp" | **MISMATCH** -- Maximum gap is about 25 pp (78.7 - 53.1), not 33 pp. The 33 pp gap would require either a lower baseline or higher RF. Even 78.4 - 53.1 = 25.3. To get 33 pp: 86 - 53 = 33 (maybe comparing best cell GPT-2 XL temp 85.9 vs DeBERTa 53.1). If so, this is misleading because it compares best-cell RF vs worst DeBERTa. |
| 16 | "DetectGPT, 28.8%; Min-K% Prob, 33.2%" | Table baselines | **MATCH** |
| 16 | "Binoculars d1v2 AUC=0.50-0.53 vs. RF 0.93" | appendix tab:detector_pairwise_auc: Binoculars d1v2 = 0.529, 0.509, 0.502 across 3 cells. RF d1v2 = 0.930, 0.934, 0.958. "0.50-0.53" and "0.93" | **MATCH** (0.93 is approximate for 0.930) |
| 19 | "mean perplexity (25.1%)" | Table baselines and appendix feature_ablation | **MATCH** |
| 19 | "zero-shot LLMs (best 36.2%)" | Table baselines | **MATCH** |
| 31 | "RF 19-feature: 78.4%" (Table baselines) | This is the 9-cell mean. matrix_data.json: Available 7 cells mean = (78.2+76.25+69.6+78.8+82.03+83.3+85.42)/7 = 79.1%. With all 9 cells (need OLMo top-k and GPT-2 XL top-k): paper Table 1 values (78.7+76.8+68.9+78.9+82.3+74.4+84.3+85.9+75.8)/9 = 78.44% | **MATCH** (from paper's own Table 1 values, the mean is 78.44%, which rounds to 78.4%) |
| 33 | "Merged (30 feat): 82.6%" | appendix tab:bino_ablation: merged 9-cell mean = 82.6% | **MATCH** |
| 34 | "Binoculars threshold: 69.8%" | Table baselines | **UNVERIFIED** (no separate artifact) |
| 35 | "Binoculars RF (1 feat): 63.7%" | Table baselines | **UNVERIFIED** |
| 69 | "Mean transfer accuracy 66.4% (d1-d3: 55.4%, 2.7x chance)" | cross_model_loo_results.txt: mean 4-class = 0.664. d1-d3 = 55.4% claimed; 55.4/33.3 = 1.66x, not 2.7x. But 55.4/20 = 2.77x (chance for d1-d3 3-class is 33.3%, not 20%). 55.4% / 33.3% = 1.66x. | **MISMATCH** -- "2.7x chance" is incorrect. For d1-d3 balanced accuracy, chance = 33.3%. 55.4/33.3 = 1.66x. The "2.7x" claim appears wrong. Unless they mean 66.4/25 = 2.66x for the 4-class metric. The sentence structure "66.4% ... d1-d3: 55.4%, 2.7x chance" seems to attach 2.7x to 55.4%, which would be wrong. |
| 69 | "d2 worst case 26.8% (Pythia holdout)" | cross_model_loo_results.txt: Pythia holdout d2 recall = 0.2677 = 26.8% | **MATCH** |
| 74 | "d1-d3 balanced accuracy drops to 45.9% (four-class: 59.1%)" | cross_strategy_loo_results.md: mean 4-class = 0.5908 = 59.1%. d1-d3 = 45.9% (claimed, not directly in artifact) | **MATCH** for 4-class (59.08% rounds to 59.1%). d1-d3 45.9% is **UNVERIFIED** from artifacts. |
| 75 | "two-stage pipeline: 70.5%, +11.5 pp; oracle: 78.3%" | 59.1 + 11.5 = 70.6, not 70.5. But the base for the +11.5 may be from d1-d3 (45.9 + 11.5 = 57.4? No). Or 59.0 + 11.5 = 70.5. | **INTERNALLY CONSISTENT** (if base = 59.0) |
| 82 | "self-reference yields 50.8% (2x chance, EDD_0.70=0)" | appendix tab:cross_scale: 14B mean = 50.8. 50.8/25 = 2.03x | **MATCH** |
| 82 | "cross-reference (Pythia-1.4B) shifts accuracy by -6.8 pp to 44.1%" | appendix tab:cross_ref_14b: mean cross-ref = 44.1%, delta = -6.8 pp | **MATCH** |
| 82 | "EDD_0.70 to 2 for nucleus and temperature" | appendix tab:cross_ref_14b: nucleus=2, temp=2 | **MATCH** |
| 83 | "Cross-domain transfer to arXiv: 74.1%" | appendix L682: 74.1% +/- 2.0% | **MATCH** |

---

### 6. discussion.tex

| Line | Claim | Source | Status |
|------|-------|--------|--------|
| 5 | "Binoculars-derived features independently reach 78.1%, not statistically distinguishable from 78.4% (permutation p>0.05; merged: 82.6%)" | appendix tab:bino_ablation | **MATCH** |
| 6 | "CORAL ordinal regression yields only marginal improvement (+0.3 pp)" | baseline_unified_comparison.md: CORAL = 0.7807, RF = 0.7813. Delta = -0.0006, i.e., CORAL is 0.06 pp LOWER. But the paper's +0.3 pp may refer to cross-model setting. | **UNVERIFIED** -- The in-distribution comparison shows CORAL is essentially equal to RF. The +0.3 pp claim is not directly substantiated. |
| 9 | "End-to-end classifiers lag RF by 14-33 pp" | Same issue as generalization.tex L13 | **MISMATCH** (same as above -- max gap is ~25 pp, not 33) |
| 9 | "d2 recall as low as 8%" | appendix tab:e2e_detail: DeBERTa d2 F1 = 0.247. This is F1, not recall. 8% recall is not in the appendix data. | **UNVERIFIED** -- The paper claims "d2 recall as low as 8%" but appendix reports F1=0.247. Recall could be lower than F1 in some cases, but no direct evidence for 8%. |
| 15 | "strategy effect (9.3 pp) exceeding the model effect (7.2 pp)" | Verified above | **MATCH** |
| 16 | "cross-architecture alternatives degrading by 4-11 pp" | appendix tab:ref_ablation: Self 78.6%, OLMo-cross 74.5% (-4.1 pp), GPT-2 XL-cross 67.3% (-11.3 pp). Range = 4.1-11.3 pp | **MATCH** (4-11 is approximate for 4.1-11.3) |
| 17 | "self-reference probe at 7B (52.1%, EDD_0.70=0)" | appendix sec:qwen7b_selfref: 52.1% 4-class, EDD_0.70=0 | **MATCH** |
| 17 | "8 pp below the cross-reference baseline (60.1%)" | appendix tab:cross_scale: Qwen2.5-7B cross-ref = 60.1%. Delta = 60.1-52.1 = 8.0 pp | **MATCH** |
| 22 | "EDD_0.70=3 preserved in 5/6 cells" (accumulation) | appendix tab:accum_auc: 5/6 cells EDD=3 | **MATCH** |
| 22 | "Cross-boundary chains (A->B->C) maintain 84.8% accuracy" | appendix sec:cross_boundary L664: "84.75% accuracy". Paper says 84.8%. | **MATCH** (84.75 rounds to 84.8) |

---

### 7. conclusion.tex (within discussion.tex section)

| Line | Claim | Source | Status |
|------|-------|--------|--------|
| 12 | "BOS-seeded generation differs from prompted generation by 13.8 pp" | appendix tab:prompted_gen: delta = -13.78 pp | **MATCH** |
| 13 | "pooled-classifier raw false-positive rates range from 15% (RedPajama) to 34% (C4)" | appendix sec:calibration L409: FineWeb 17.2%, RedPajama 15.5%, C4 34.0%. Range = 15.5-34.0%. Paper says "15% (RedPajama) to 34% (C4)" | **MATCH** (15.5 rounds to ~15) |
| 13 | "reducible to <=7% via posterior-threshold calibration" | appendix L410: FineWeb 0.1%, RedPajama 7.0%. "<=7%" | **MATCH** |

---

### 8. method.tex

| Line | Claim | Source | Status |
|------|-------|--------|--------|
| 30 | "5,000 samples per depth per cell (180K cell-instances; 140K unique passages)" | 5000 x 4 x 9 = 180K. d0 shared: 9 cells share 5000 d0 samples => 5000 x 1 + 5000 x 3 x 9 = 5000 + 135000 = 140000 unique | **MATCH** |
| 34 | "LoRA r=16, alpha=32, lr 2e-4, effective batch 16, 3 epochs, dropout 0.05" | appendix tab:lora_protocol | **MATCH** |
| 36 | "prompted-generation validation confirms signal persistence albeit attenuated (-13.8 pp)" | appendix tab:prompted_gen | **MATCH** |
| 41 | "4-11 pp self-reference advantage" | appendix tab:ref_ablation: 78.6 vs 74.5 = 4.1 pp, vs 67.3 = 11.3 pp | **MATCH** |
| 42 | "Alternative references yield 67-79%, all exceeding 2.5x chance" | tab:ref_ablation: 67.3-78.6%. 67.3/25 = 2.69x | **MATCH** |
| 47 | "top 5 achieve 97.6% of full-set performance" | As computed above: 76.5/78.4 = 97.6% | **MATCH** (internally consistent, though 76.5% top-5 is not independently verified) |
| 47 | "VIF>10 for 14-16 features; effective independent dimensionality ~4-5" | Consistent throughout | **MATCH** |
| 102 | "8/9 cells achieve EDD_0.70 >= 3" | edd_threshold_sensitivity.json | **MATCH** |
| 106 | "98.2% of errors fall on adjacent depths (|delta| <= 1)" | Table 1 caption | **UNVERIFIED** from artifacts |
| 106 | "QWK = 0.89" | Table 1 caption | **UNVERIFIED** from artifacts |

---

### CRITICAL ISSUE: Table 1 vs matrix_data.json

The paper's Table 1 reports accuracy values that differ from `matrix_data.json`:

| Cell | Paper Table 1 | matrix_data.json | Delta |
|------|---------------|------------------|-------|
| Pythia nucleus | 78.7% | 78.2% | +0.5 |
| Pythia temp | 76.8% | 76.25% | +0.55 |
| Pythia top-k | 68.9% | 69.6% | -0.7 |
| OLMo nucleus | 78.9% | 78.8% | +0.1 |
| OLMo temp | 82.3% | 82.03% | +0.27 |
| OLMo top-k | 74.4% | N/A (placeholder) | -- |
| GPT-2 XL nucleus | 84.3% | 83.3% | +1.0 |
| GPT-2 XL temp | 85.9% | 85.42% | +0.48 |
| GPT-2 XL top-k | 75.8% | N/A (placeholder) | -- |

The `matrix_data.json` was generated on 2026-05-15, and only 7/9 cells were complete at that time (OLMo top-k and GPT-2 XL top-k were still running). The paper Table 1 likely uses final results that were computed later. The discrepancies for completed cells (GPT-2 XL nucleus: 84.3% vs 83.3%, a full 1.0 pp difference) are concerning and suggest either the paper was updated with newer runs or the artifact is stale.

---

### SUMMARY OF ALL ISSUES

**MISMATCHES (requiring correction or verification):**

1. **atlas.tex L93**: "d0-vs-d1 AUC >0.99 in all 9 cells" -- OLMo nucleus d0v1 = 0.9834, which is NOT >0.99. Should say ">0.98" or "near 1.0".

2. **generalization.tex L13 / discussion.tex L9**: "lag RF by 14-33 pp" -- Maximum gap is ~25-26 pp (85.9 - 60.6 or 78.7 - 53.1). The 33 pp figure is not substantiated. Should be "14-26 pp" or similar.

3. **generalization.tex L69**: "2.7x chance" attached to d1-d3 metric -- For d1-d3, chance = 33.3%. 55.4/33.3 = 1.66x, not 2.7x. The 2.7x applies to the 4-class metric (66.4/25=2.66). The sentence structure is ambiguous/incorrect.

4. **Table 1 vs matrix_data.json**: Multiple cells differ by 0.1-1.0 pp. GPT-2 XL nucleus shows the largest gap (84.3% in paper vs 83.3% in artifact). The artifact may be stale.

5. **atlas.tex L49**: "Spearman rho = 0.868 ([0.619, 0.954])" -- Local artifact data gives cross-model (nucleus) mean rho = 0.801 and all-pairs mean = 0.774. Neither matches 0.868.

6. **atlas.tex L44**: "17.1 pp accuracy spread" -- From Table 1: 85.9 - 68.9 = 17.0 pp, not 17.1.

7. **theory.tex L15**: "d0-vs-d1 AUC >0.99 at 1-1.5B" -- Same issue; OLMo d0v1 = 0.9834.

8. **atlas.tex L93**: "d2-vs-d3: 0.69-0.89" -- Actual range from data is 0.6918-0.8829 = "0.69-0.88".

**UNVERIFIED claims (source data not in local artifacts, likely on server):**

1. introduction.tex L33: "-8-15 pp accuracy attenuation" under accumulation
2. theory.tex L10: AUC-excess contraction ratios 0.80 and 0.69 (needs d0-d5 data)
3. theory.tex L20: GPT-2 XL temperature d1 median p90_ppl = 92.2, nucleus d2 median = 92.3 (median values not in local artifacts)
4. atlas.tex L52: "top-5 features achieve 97.6% of full accuracy (76.5%)" -- the 76.5% figure is not in appendix tables
5. atlas.tex L100-101: d0v1=0.999 and d4v5 values (need d0-d5 extension data from server)
6. discussion.tex L6: "CORAL +0.3 pp" -- local data shows CORAL essentially equal or slightly below RF
7. discussion.tex L9: "d2 recall as low as 8%" -- appendix shows F1=0.247, not recall=8%
8. method.tex L106: "98.2% errors at |delta|<=1, QWK=0.89" -- not verified from artifacts

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82fb92dc-fd54-4713-932f-be9eeb73bcee",
  "isSidechain": true,
  "agentId": "a563e433f634db794",
  "requestId": "req_011CbKLHB3xNUkzUs1fuuaDc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dba611df-d445-463f-910c-7d53ec0e6f33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "30b280da-923f-435b-b3db-f1fde842ae75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "misty-knitting-candle",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWkHeFZGCJ14SBB8r477n5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10099,
      "cache_read_input_tokens": 108586,
      "output_tokens": 10179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10099
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10179,
          "cache_read_input_tokens": 108586,
          "cache_creation_input_tokens": 10099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10099,
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
