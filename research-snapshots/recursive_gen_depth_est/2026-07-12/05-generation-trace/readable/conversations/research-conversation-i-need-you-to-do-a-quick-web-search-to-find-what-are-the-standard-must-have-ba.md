# Research conversation: I need you to do a quick web search to find what are the standard/must-have baselines and experiments in AI-generated te

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a2a1d57fccd36c618.jsonl`
- **Structured JSON:** [`b81faead69a8308d100c.json`](../../sessions/b8/b81faead69a8308d100c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-17T12:01:54.283Z_

I need you to do a quick web search to find what are the standard/must-have baselines and experiments in AI-generated text detection papers published at top NLP venues (EMNLP, ACL, NAACL, ICLR, NeurIPS) in 2024-2026. 

Context: We have a paper about "recursive generation depth estimation" — estimating how many times text has been recursively generated (depth 0=human, depth 1=1st gen, depth 2=2nd gen, etc.). It's an ordinal classification task, not binary detection.

We already have these baselines:
- Random Forest on 19 distributional features (our main method)
- Logistic Regression on same features
- CORAL ordinal regression
- DivEye
- CE-MLP (cross-entropy MLP)
- Perplexity regression (single + multi-feature)
- DeBERTa end-to-end fine-tuning
- DCOL (contrastive ordinal learning - failed)
- Binoculars (in progress)
- Fast-DetectGPT (in progress)
- MLP on 19 features (planned)

Questions I need answered:
1. Are there any other widely-cited AI text detection methods from 2024-2026 that reviewers would expect to see as baselines? (e.g., Ghostbuster, RADAR, DNA-GPT, etc.)
2. For ordinal classification specifically, are there standard methods we should include?
3. Is testing on instruction-tuned models considered a must-have in recent detection papers?
4. Any standard robustness tests (paraphrasing attack, text length sensitivity) that are expected?

Please search for recent survey papers or benchmark papers on AI text detection to get comprehensive coverage. Report in under 300 words with a prioritized list.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c224a726-e097-4493-9f8f-3f492f73d7f1",
  "agentId": "a2a1d57fccd36c618",
  "type": "user",
  "uuid": "5c88083a-60cf-44b0-b7dc-45566c5193f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T12:01:54.293Z_

```json
{
  "parentUuid": "5c88083a-60cf-44b0-b7dc-45566c5193f7",
  "isSidechain": true,
  "agentId": "a2a1d57fccd36c618",
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
      "mcp__agent-ml-research__dream_simulate",
      "mcp__agent-ml-research__feishu_read_chat_history",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__feishu_upload_file",
      "mcp__agent-ml-research__get_agent_queue_status",
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
      "mcp__agent-ml-research__dream_simulate",
      "mcp__agent-ml-research__feishu_read_chat_history",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__feishu_upload_file",
      "mcp__agent-ml-research__get_agent_queue_status",
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
  "uuid": "cebd170d-fa72-44cb-84cc-261c10c4a836",
  "timestamp": "2026-05-17T12:01:54.293Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-17T12:01:58.863Z_



I'll search for recent AI text detection baselines and standards from top venues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cebd170d-fa72-44cb-84cc-261c10c4a836",
  "isSidechain": true,
  "agentId": "a2a1d57fccd36c618",
  "requestId": "req_011Cb877a2FBFA6Psq2hzXP4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4122529-6f8e-40ff-87a4-c32dc3a0758d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013yCwKrnMeC1LPZRgxq7sMc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32489,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32489,
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

_source line 4 · 2026-05-17T12:01:59.246Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WkijNDY5h6RZMyK35bJoKG`</summary>

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
  "parentUuid": "d4122529-6f8e-40ff-87a4-c32dc3a0758d",
  "isSidechain": true,
  "agentId": "a2a1d57fccd36c618",
  "requestId": "req_011Cb877a2FBFA6Psq2hzXP4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04fdd0d7-e0ac-4efa-9823-ca4c87a7bfd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013yCwKrnMeC1LPZRgxq7sMc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32489,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32489,
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

_source line 5 · 2026-05-17T12:01:59.251Z_

<details><summary>↩ Tool result · `toolu_01WkijNDY5h6RZMyK35bJoKG`</summary>

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
  "parentUuid": "04fdd0d7-e0ac-4efa-9823-ca4c87a7bfd4",
  "isSidechain": true,
  "promptId": "c224a726-e097-4493-9f8f-3f492f73d7f1",
  "agentId": "a2a1d57fccd36c618",
  "type": "user",
  "uuid": "1cca0725-50cf-4492-b1e8-59139de9e916",
  "sourceToolAssistantUUID": "04fdd0d7-e0ac-4efa-9823-ca4c87a7bfd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-17T12:02:02.473Z_



Running parallel searches to cover all four questions comprehensively.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cca0725-50cf-4492-b1e8-59139de9e916",
  "isSidechain": true,
  "agentId": "a2a1d57fccd36c618",
  "requestId": "req_011Cb877wt92tPoPG5SyrqN8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5b2899f-e7c7-4bf0-bc12-09c2288af5a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZob3Crjbm8Mh2ijmxc39r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 32489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1457,
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

_source line 7 · 2026-05-17T12:02:02.952Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NFZ6AeKSFm8d1KWYVfWf27`</summary>

```json
{
  "query": "AI-generated text detection baselines survey 2024 2025 ACL EMNLP NeurIPS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5b2899f-e7c7-4bf0-bc12-09c2288af5a3",
  "isSidechain": true,
  "agentId": "a2a1d57fccd36c618",
  "requestId": "req_011Cb877wt92tPoPG5SyrqN8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6118fa4e-5828-4ed8-a898-e773e7af52a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZob3Crjbm8Mh2ijmxc39r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 32489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1457,
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

_source line 8 · 2026-05-17T12:02:03.426Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018MKpUUNmPJiYgnfHWVDmYu`</summary>

```json
{
  "query": "Ghostbuster RADAR DNA-GPT AI text detection benchmark comparison 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6118fa4e-5828-4ed8-a898-e773e7af52a0",
  "isSidechain": true,
  "agentId": "a2a1d57fccd36c618",
  "requestId": "req_011Cb877wt92tPoPG5SyrqN8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d143cb9-4e41-42e0-89c9-89bb1cc740f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZob3Crjbm8Mh2ijmxc39r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 32489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1457,
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

_source line 9 · 2026-05-17T12:02:03.896Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CN4tPLAcHszPTNsK6FSSax`</summary>

```json
{
  "query": "ordinal classification deep learning standard baselines methods 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d143cb9-4e41-42e0-89c9-89bb1cc740f5",
  "isSidechain": true,
  "agentId": "a2a1d57fccd36c618",
  "requestId": "req_011Cb877wt92tPoPG5SyrqN8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "225f2e91-2299-4b61-8311-65057f11e5fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZob3Crjbm8Mh2ijmxc39r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 32489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1457,
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

_source line 10 · 2026-05-17T12:02:04.353Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LBH6WEzzFKhcxquue7RPFV`</summary>

```json
{
  "query": "AI text detection robustness paraphrasing attack evaluation 2024 2025 survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "225f2e91-2299-4b61-8311-65057f11e5fb",
  "isSidechain": true,
  "agentId": "a2a1d57fccd36c618",
  "requestId": "req_011Cb877wt92tPoPG5SyrqN8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f3cc11c-1bcb-4b85-8f4d-bb59c9a4ae51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZob3Crjbm8Mh2ijmxc39r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 32489,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1457
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 249,
          "cache_read_input_tokens": 32489,
          "cache_creation_input_tokens": 1457,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1457,
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

_source line 11 · 2026-05-17T12:02:09.985Z_

<details><summary>↩ Tool result · `toolu_018MKpUUNmPJiYgnfHWVDmYu`</summary>

```text
Web search results for query: "Ghostbuster RADAR DNA-GPT AI text detection benchmark comparison 2024 2025"

Links: [{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.95/"},{"title":"GitHub - vivek3141/ghostbuster: Ghostbuster: Detecting Text Ghostwritten by Large Language Models (NAACL 2024) · GitHub","url":"https://github.com/vivek3141/ghostbuster"},{"title":"[2305.15047] Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/abs/2305.15047"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/html/2305.15047v3"},{"title":"Detecting Text Ghostwritten by Large Language Models","url":"https://aclanthology.org/2024.naacl-long.95.pdf"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/ghostbuster-detecting-text-ghostwritten-by-large-language"},{"title":"Ghostbuster: Unprecedented Accuracy in AI-Generated Text Detection | Mindplex","url":"https://magazine.mindplex.ai/post/ghostbuster-unprecedented-accuracy-in-ai-generated-text-detection"},{"title":"Ghostbuster: AI Text Detection","url":"https://www.emergentmind.com/papers/2305.15047"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/382631441_Ghostbuster_Detecting_Text_Ghostwritten_by_Large_Language_Models"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=DetectGPT"}]

Based on the search results, here's what I found regarding AI text detection methods:

## Ghostbuster Overview

Ghostbuster is a state-of-the-art system for detecting AI-generated text that works by passing documents through a series of weaker language models, running a structured search over possible combinations of their features, and then training a classifier on the selected features to predict whether documents are AI-generated.

## Performance Comparison

Ghostbuster achieves 99.0 F1 when evaluated across domains, which is 5.9 F1 higher than the best preexisting model. It was compared to several existing detectors, including DetectGPT and GPTZero, as well as a new RoBERTa baseline.

Ghostbuster outperforms all previous approaches in generalization across writing domains (+7.5 F1), prompting strategies (+2.1 F1), and language models (+4.4 F1).

## Key Advantages

Crucially, Ghostbuster does not require access to token probabilities from the target model, making it useful for detecting text generated by black-box or unknown models.

## Benchmarks

In conjunction with their model, the researchers released three new datasets of human- and AI-generated text as detection benchmarks in the domains of student essays, creative writing, and news articles.

**Note:** The search results focus primarily on Ghostbuster benchmarks from 2024. The search did not return specific information about RADAR, DNA-GPT, or newer 2025 benchmark comparisons.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d143cb9-4e41-42e0-89c9-89bb1cc740f5",
  "isSidechain": true,
  "promptId": "c224a726-e097-4493-9f8f-3f492f73d7f1",
  "agentId": "a2a1d57fccd36c618",
  "type": "user",
  "uuid": "1714647c-377e-4c53-9315-49ade43a6b46",
  "sourceToolAssistantUUID": "1d143cb9-4e41-42e0-89c9-89bb1cc740f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T12:02:11.848Z_

<details><summary>↩ Tool result · `toolu_01LBH6WEzzFKhcxquue7RPFV`</summary>

```text
Web search results for query: "AI text detection robustness paraphrasing attack evaluation 2024 2025 survey"

Links: [{"title":"Enhancing the Robustness of AI-Generated Text Detectors: A Survey","url":"https://www.mdpi.com/2227-7390/13/13/2145"},{"title":"Paraphrasing evades detectors of AI-generated text, but ...","url":"https://openreview.net/pdf?id=WbFhFvjjKj"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"Modeling the Attack: Detecting AI-Generated Text","url":"https://arxiv.org/pdf/2510.02319"},{"title":"generalized and robust AI-generated text detection via ...","url":"https://aclanthology.org/2025.naacl-long.446.pdf"},{"title":"A Survey on AI-Generated Text Detection: Methods, Challenges, and Future Directions","url":"https://www.researchgate.net/publication/400099134_A_Survey_on_AI-Generated_Text_Detection_Methods_Challenges_and_Future_Directions"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"PADBen: A Comprehensive Benchmark for Evaluating AI Text Detectors Against Paraphrase Attacks","url":"https://arxiv.org/html/2511.00416v1"},{"title":"(PDF) Enhancing the Robustness of AI-Generated Text Detectors: A Survey","url":"https://www.researchgate.net/publication/393219779_Enhancing_the_Robustness_of_AI-Generated_Text_Detectors_A_Survey"},{"title":"Paraphrasing Attack Resilience of Various AI-Generated Text Detection Methods","url":"https://arxiv.org/html/2605.14240"}]

Based on the search results, I found several recent comprehensive studies on AI text detection robustness against paraphrasing attacks from 2024-2025:

## Key Survey and Research Papers

**Recent Comprehensive Surveys:**

A 2025 survey provides a systematic overview of existing research on enhancing the robustness of AI-generated text (AIGT) detectors, categorizing the focus into three key areas: text perturbation robustness, out-of-distribution (OOD) robustness, and AI–human hybrid text detection robustness.

**Paraphrasing as a Vulnerability:**

Paraphrase is a key strategy for evading AIGT detection, with recursive paraphrase significantly reducing detection rates. By paraphrasing an AI-produced message, an attacker can dramatically change its statistical attributes while maintaining its fundamental semantic meaning, thus drastically lowering the accuracy of numerous detection tools.

**Evaluation Approaches:**

Research proposes a comprehensive five-type text taxonomy capturing attack categories, constructing five progressive detection tasks evaluating detector robustness across sentence-pair and single-sentence formats, with extensive evaluations of 11 state-of-the-art detectors revealing critical asymmetry: paraphrase attacks do not universally defeat detection systems—outcomes depend on text origin.

**Defense Mechanisms:**

Methods for enhancing text perturbation robustness are categorized into five main types: data-augmentation-based methods, adversarial-training-based methods, noise-filtering-based methods, text-correction-based methods, and text-paraphrase-based methods.

The search results show active research in 2024-2025 focusing on understanding and improving detection robustness against sophisticated paraphrasing attacks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f3cc11c-1bcb-4b85-8f4d-bb59c9a4ae51",
  "isSidechain": true,
  "promptId": "c224a726-e097-4493-9f8f-3f492f73d7f1",
  "agentId": "a2a1d57fccd36c618",
  "type": "user",
  "uuid": "8a7cd3ab-01eb-44f0-8618-879453ad02ee",
  "sourceToolAssistantUUID": "9f3cc11c-1bcb-4b85-8f4d-bb59c9a4ae51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T12:02:12.135Z_

<details><summary>↩ Tool result · `toolu_01NFZ6AeKSFm8d1KWYVfWf27`</summary>

```text
Web search results for query: "AI-generated text detection baselines survey 2024 2025 ACL EMNLP NeurIPS"

Links: [{"title":"A Survey on AI-Generated Text Detection: Methods, Challenges, and Future Directions","url":"https://www.researchgate.net/publication/400099134_A_Survey_on_AI-Generated_Text_Detection_Methods_Challenges_and_Future_Directions"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/51/1/275/127462/A-Survey-on-LLM-Generated-Text-Detection-Necessity"},{"title":"Enhancing the Robustness of AI-Generated Text Detectors: A Survey","url":"https://www.mdpi.com/2227-7390/13/13/2145"},{"title":"The Imitation Game revisited: A comprehensive survey on recent advances in AI-generated text detection - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417425003161"},{"title":"[2310.14724] A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/abs/2310.14724"},{"title":"A Survey on LLM-Generated Text Detection:","url":"https://aclanthology.org/2025.cl-1.8.pdf"},{"title":"A Comprehensive Survey of Machine-Generated Text Detection","url":"https://www.researchgate.net/publication/399324725_A_Comprehensive_Survey_of_Machine-Generated_Text_Detection"},{"title":"A Systematic Survey of AI-Generated Text Detection, Humanization, and Grammar Correction Techniques","url":"https://ijettjournal.org/archive/ijett-v74i3p104"},{"title":"AI-Generated Text Detection: A Comprehensive Review of Active and Passive Approaches - ScienceDirect","url":"https://www.sciencedirect.com/org/science/article/pii/S1546221826000482"}]

Based on the web search results, here's what I found regarding recent surveys on AI-generated text detection:

## Recent Surveys on AI-Generated Text Detection

Several comprehensive surveys have been published in 2024-2025:

**Survey Publications:**

1. A Survey on LLM-Generated Text Detection published in March 2025 covers the necessity and mechanisms for identifying LLM-generated text, which has become critical to mitigating misuse and safeguarding domains like artistic expression and social networks.

2. A survey on enhancing the robustness of AI-generated text detectors provides a systematic overview of existing research and methodically organizes relevant benchmark datasets, robustness evaluation methods, and metrics used to assess detectors' performance.

3. A comprehensive survey titled "The Imitation Game revisited" addresses limitations of previous surveys by providing a coherent and comprehensive framework for understanding the broader progress and trends in this field, given the rapidly evolving landscape of AI-powered text generation.

**Detection Methods Covered:**

Recent advances in this field stem from innovations in watermarking techniques, statistics-based detectors, and neural-based detectors. AIGT detection methods can be broadly categorized into three types: zero-shot detectors, training-based detectors, and watermarking detectors.

**Key Baselines Discussed:**

Various baselines are compared including both traditional statistical detectors and recent fine-tuned models, such as RADAR, LogRank, Entropy, FastDetectGPT, DetectLLM, Binoculars, and others, covering techniques from token-level likelihood-based ranking to transformer-based classification.

The search results indicate active research in this area through 2025, though I didn't find papers specifically from the ACL, EMNLP, and NeurIPS conferences mentioned in your query within these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6118fa4e-5828-4ed8-a898-e773e7af52a0",
  "isSidechain": true,
  "promptId": "c224a726-e097-4493-9f8f-3f492f73d7f1",
  "agentId": "a2a1d57fccd36c618",
  "type": "user",
  "uuid": "a6da5444-3854-4946-8c55-ffd62b29dbeb",
  "sourceToolAssistantUUID": "6118fa4e-5828-4ed8-a898-e773e7af52a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T12:02:15.550Z_

<details><summary>↩ Tool result · `toolu_01CN4tPLAcHszPTNsK6FSSax`</summary>

```text
Web search results for query: "ordinal classification deep learning standard baselines methods 2024 2025"

Links: [{"title":"Deep learning-based ordinal classification overcomes subjective assessment limitations in intraoral free flap monitoring | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-33637-9"},{"title":"Active learning for ordinal classification based on expected cost minimization | Scientific Reports","url":"https://www.nature.com/articles/s41598-022-26844-1"},{"title":"A novel deep ordinal classification approach for aesthetic quality control classification | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-022-07050-6"},{"title":"dlordinal: a Python package for deep ordinal classification","url":"https://arxiv.org/html/2407.17163v2"},{"title":"Deep Ordinal Classification in Forest Areas Using Light Detection and Ranging Point Clouds","url":"https://www.mdpi.com/1424-8220/24/7/2168"},{"title":"A Deep Learning Ordinal Classifier","url":"https://thesai.org/Publications/ViewPaper?Volume=16&Issue=3&Code=ijacsa&SerialNo=30"},{"title":"Advanced Deep Learning Systems: 2024/2025 — MASE 0.0.1 documentation","url":"https://deepwok.github.io/mase/modules/adls_2024.html"},{"title":"1 Introduction","url":"https://arxiv.org/html/2505.24595"},{"title":"Accurate predictions on small data with a tabular foundation model | Nature","url":"https://www.nature.com/articles/s41586-024-08328-6"},{"title":"Baseline Models: Your Guide For Model Building | Towards Data Science","url":"https://towardsdatascience.com/baseline-models-your-guide-for-model-building-1ec3aa244b8d/"}]

Based on the search results, I found several relevant sources on ordinal classification and deep learning approaches from 2024-2025:

## Key Resources and Methods

**Python Libraries and Unified Frameworks:**
dlordinal is a new Python library that unifies many recent deep ordinal classification methodologies and implements the top performing state-of-the-art deep learning techniques for ordinal classification problems using PyTorch as the underlying framework.

**Recent Deep Learning Approaches:**

One recent approach integrates TabNet (a deep learning framework) with ordinal constraints, leveraging a proportional odds model to better capture the ordinal structure and Beta cross-entropy as the loss function to enforce ordering during training.

Another 2025 study developed an ordinal classification model using a novel approach with dynamic triplet margin loss technique, achieving 0.9571 accuracy and significantly outperforming the baseline model (0.8847).

**Standard Baseline Methods:**

For comparison purposes, state-of-the-art ordinal deep learning methodologies include ordinal binary decomposition VGG-16 and CLM VGG-16 with weight kappa loss.

**Technical Approaches:**

An effective soft labeling technique based on a generalized exponential function has been applied to the PointNet network architecture for ordinal classification.

The recent literature shows an emphasis on methods that explicitly model ordinal relationships through specialized loss functions and regularization techniques, rather than treating ordinal classification as standard nominal classification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "225f2e91-2299-4b61-8311-65057f11e5fb",
  "isSidechain": true,
  "promptId": "c224a726-e097-4493-9f8f-3f492f73d7f1",
  "agentId": "a2a1d57fccd36c618",
  "type": "user",
  "uuid": "d7388065-e55c-4244-b720-6160d939d72a",
  "sourceToolAssistantUUID": "225f2e91-2299-4b61-8311-65057f11e5fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T12:02:20.341Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012VQM9HPA8y2EmHsJ38iC3u`</summary>

```json
{
  "query": "RADAR DNA-GPT RAIDAR LLM text detection method 2024 AAAI ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7388065-e55c-4244-b720-6160d939d72a",
  "isSidechain": true,
  "agentId": "a2a1d57fccd36c618",
  "requestId": "req_011Cb8798tT56Rai1MPpdmED",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "002bab85-f20f-4744-b09a-1415a0473ea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHv9EX1XnK153CYhjUBaUS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 930,
      "cache_creation_input_tokens": 3001,
      "cache_read_input_tokens": 33946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3001,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 16 · 2026-05-17T12:02:20.643Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016xEsuE4uKTrUTxsFYrxBoi`</summary>

```json
{
  "query": "AI text detection must-have baselines 2025 DetectLLM LogRank watermark benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "002bab85-f20f-4744-b09a-1415a0473ea2",
  "isSidechain": true,
  "agentId": "a2a1d57fccd36c618",
  "requestId": "req_011Cb8798tT56Rai1MPpdmED",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6462c6d-252f-4083-a4eb-6c93227a045d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHv9EX1XnK153CYhjUBaUS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 930,
      "cache_creation_input_tokens": 3001,
      "cache_read_input_tokens": 33946,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3001
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 930,
          "output_tokens": 136,
          "cache_read_input_tokens": 33946,
          "cache_creation_input_tokens": 3001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3001,
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

_source line 17 · 2026-05-17T12:02:28.725Z_

<details><summary>↩ Tool result · `toolu_012VQM9HPA8y2EmHsJ38iC3u`</summary>

```text
Web search results for query: "RADAR DNA-GPT RAIDAR LLM text detection method 2024 AAAI ICLR"

Links: [{"title":"GitHub - IBM/RADAR: Code for our NeurIPS2023 accepted paper: RADAR: Robust AI-Text Detection via Adversarial Learning. We tested RADAR on 8 LLMs including Vicuna and LLaMA. The results show that RADAR can attain good detection performance on LLM-generated AI-text while being robust against paraphrasing. · GitHub","url":"https://github.com/IBM/RADAR"},{"title":"GitHub - Xianjun-Yang/Awesome_papers_on_LLMs_detection: The lastest paper about detection of LLM-generated text and code · GitHub","url":"https://github.com/Xianjun-Yang/Awesome_papers_on_LLMs_detection"},{"title":"[2307.03838] RADAR: Robust AI-Text Detection via Adversarial Learning","url":"https://arxiv.org/abs/2307.03838"},{"title":"Raidar: geneRative AI Detection viA Rewriting","url":"https://arxiv.org/pdf/2401.12970"},{"title":"RAIDAR: GENERATIVE AI DETECTION VIA REWRIT","url":"https://www.cs.columbia.edu/~junfeng/papers/raidar-iclr24.pdf"},{"title":"[Quick Review] Raidar: geneRative AI Detection viA Rewriting","url":"https://liner.com/review/raidar-generative-ai-detection-via-rewriting"},{"title":"GitHub - cvlab-columbia/RaidarLLMDetect · GitHub","url":"https://github.com/cvlab-columbia/raidarllmdetect"},{"title":"Raidar: geneRative AI Detection viA Rewriting | OpenReview","url":"https://openreview.net/forum?id=bQWE2UqXmf"},{"title":"[PDF] RADAR: Robust AI-Text Detection via Adversarial Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RADAR:-Robust-AI-Text-Detection-via-Adversarial-Hu-Chen/ef3bdb9e805887a1a14e1e4cdb27145135591305"},{"title":"GENERALIZED DETECTION OF LLM-GENERATED TEXT","url":"https://openreview.net/pdf?id=wojnTvBXqt"}]

Based on the search results, I found information about the methods you mentioned:

## DNA-GPT

DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text is a method for detecting LLM-generated text. According to the search results, it was presented at The Twelfth International Conference on Learning Representations by Yang, Xianjun and colleagues.

## RADAR

RADAR is a paper on Robust AI-Text Detection via Adversarial Learning that was accepted at NeurIPS 2023 (not AAAI or ICLR). RADAR is based on adversarial training of a paraphraser and a detector, where the paraphraser's goal is to generate realistic content to evade AI-text detection. RADAR was tested on 8 LLMs including Vicuna and LLaMA, and the results show that RADAR can attain good detection performance on LLM-generated AI-text while being robust against paraphrasing.

## RAIDAR

RAIDAR is an ICLR 2024 paper describing a generative AI detection method using rewriting distance for black-box LLMs. The method finds that large language models are more likely to modify human-written text than AI-generated text when tasked with rewriting, as LLMs often perceive AI-generated text as high-quality, leading to fewer modifications, and it detects AI-generated content by prompting LLMs to rewrite text and calculating the editing distance of the output. RAIDAR significantly outperforms existing state-of-the-art methods including DetectGPT, Ghostbuster, and GPTZero, achieving F1 score improvements of up to 29 points in in-domain testing and up to 32 points in out-of-distribution scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "002bab85-f20f-4744-b09a-1415a0473ea2",
  "isSidechain": true,
  "promptId": "c224a726-e097-4493-9f8f-3f492f73d7f1",
  "agentId": "a2a1d57fccd36c618",
  "type": "user",
  "uuid": "549db530-0edd-4baa-a5d7-393f93fd7aff",
  "sourceToolAssistantUUID": "002bab85-f20f-4744-b09a-1415a0473ea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T12:02:31.455Z_

<details><summary>↩ Tool result · `toolu_016xEsuE4uKTrUTxsFYrxBoi`</summary>

```text
Web search results for query: "AI text detection must-have baselines 2025 DetectLLM LogRank watermark benchmark"

Links: [{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/51/1/275/127462/A-Survey-on-LLM-Generated-Text-Detection-Necessity"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"Beyond Easy Wins: A Text Hardness-Aware Benchmark for LLM-generated Text Detection","url":"https://arxiv.org/html/2507.15286v1"},{"title":"AI Text Detection Benchmarks 2025: Top Performance Metrics","url":"https://hastewire.com/blog/ai-text-detection-benchmarks-2025-top-performance-metrics"},{"title":"A Survey on LLM-Generated Text Detection:","url":"https://aclanthology.org/2025.cl-1.8.pdf"},{"title":"DetectLLM: Leveraging Log Rank Information for Zero-Shot Detection of Machine-Generated Text | Request PDF","url":"https://www.researchgate.net/publication/376393392_DetectLLM_Leveraging_Log_Rank_Information_for_Zero-Shot_Detection_of_Machine-Generated_Text"},{"title":"DetectRL: Benchmarking LLM-Generated Text Detection in Real-World Scenarios","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/b61bdf7e9f64c04ec75a26e781e2ad51-Paper-Datasets_and_Benchmarks_Track.pdf"},{"title":"BUST: Benchmark for the evaluation of detectors of LLM- ...","url":"https://aclanthology.org/2024.naacl-long.444.pdf"},{"title":"[PDF] A Survey on LLM-generated Text Detection: Necessity, Methods, and Future Directions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-on-LLM-generated-Text-Detection:-Methods,-Wu-Yang/a09d3686285f609b60b18b5935da64b29a5cce0f"},{"title":"PROFILER: Black-box AI-generated Text Origin Detection ...","url":"https://aclanthology.org/2025.emnlp-main.1265.pdf"}]

Based on the search results, I found relevant information about AI text detection methods, baselines, and benchmarks for 2025. Here are the key findings:

## Key Detection Methods and Baselines

Common detection baselines include RADAR, LogRank, Entropy, FastDetectGPT, DetectLLM, Binoculars, RAiDAR, OpenAI Detector, Longformer, and BiScope.

### DetectLLM and LogRank

DetectLLM leverages log rank information for zero-shot detection of machine-generated text. LogRank is a statistical/zero-shot detection method that works by leveraging LLM probability cues.

### Watermarking Baselines

Research shows that SWEET outperforms watermark baselines WLLM and EXP-EDIT as well as zero-shot methods including LogRank and DetectGPT.

## 2025 Benchmarks

Recent 2025 studies show marked improvements in detection rates for newer AI-generated content, with earlier detectors achieving only 70-75% accuracy on post-2024 AI text, while innovations in transformer-based classifiers and watermarking techniques have boosted rates to 90%+ for content from models like Llama 3.1 and Claude 3.5.

Notable benchmarks include RAID which systematically examines robustness across multiple decoding strategies, and MAGE which extends evaluation capabilities across a broader spectrum of LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6462c6d-252f-4083-a4eb-6c93227a045d",
  "isSidechain": true,
  "promptId": "c224a726-e097-4493-9f8f-3f492f73d7f1",
  "agentId": "a2a1d57fccd36c618",
  "type": "user",
  "uuid": "5dfe6b36-4b52-46d0-a215-98147a15519d",
  "sourceToolAssistantUUID": "b6462c6d-252f-4083-a4eb-6c93227a045d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-17T12:02:50.765Z_

Here is the prioritized summary:

---

**Q1: Missing high-citation detection baselines reviewers would expect**

Priority A (widely cited, reviewers will notice absence):
- **Ghostbuster** (NAACL 2024) — structured feature search over weaker LMs, no token-prob access needed. Directly comparable to your feature-based approach.
- **RADAR** (NeurIPS 2023) — adversarial-trained detector, robust to paraphrase. Standard baseline in recent papers.
- **DetectLLM / Log-Rank** (EMNLP 2023) — zero-shot log-rank method. Very commonly included.
- **DetectGPT** (ICML 2023) — perturbation-based, predecessor to Fast-DetectGPT (already in progress).

Priority B (good to have, strengthens paper):
- **RAIDAR** (ICLR 2024) — rewriting-distance detection, black-box.
- **DNA-GPT** (ICLR 2024) — divergent n-gram analysis, training-free.
- **RoBERTa-based detector** (OpenAI) — commonly used as a trained-classifier baseline alongside DeBERTa.

Since your task is ordinal (depth estimation), not binary, you can adapt binary detectors by using their confidence scores as regression features or training them per-depth. Mention this adaptation explicitly.

**Q2: Ordinal classification baselines**

Your CORAL is the standard. Add:
- **Ordinal Binary Decomposition** (cumulative link model) — classic, easy to implement.
- **SORD / Soft Labels** — soft ordinal encoding with KL-divergence loss. The `dlordinal` Python library implements many of these.
- Your CE-MLP already serves as the "ignore ordinal structure" ablation, which is correct.

**Q3: Instruction-tuned models**

Yes, testing on instruction-tuned / chat models (e.g., ChatGPT, Llama-3-Instruct, Claude) is now considered a must-have. Papers at NeurIPS 2024 (DetectRL benchmark) and NAACL 2024 (BUST benchmark) specifically evaluate across instruction-tuned models. Reviewers will flag if you only test on base models.

**Q4: Standard robustness tests**

Must-have (reviewers expect these):
1. **Paraphrasing attack** — DIPPER or back-translation paraphrase; PADBen benchmark (2025) is dedicated to this.
2. **Cross-model generalization** — train on model A, test on model B.
3. **Text length sensitivity** — short vs. long passages.

Good to have:
4. **Decoding strategy variation** — temperature, top-p, top-k.
5. **Domain transfer** — train on one domain, test on another.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5dfe6b36-4b52-46d0-a215-98147a15519d",
  "isSidechain": true,
  "agentId": "a2a1d57fccd36c618",
  "requestId": "req_011Cb87AJujhac1nHj84smFh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e65c3db9-4aac-4c11-8132-f15c2e56e87b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "88c9c515-067f-4d34-b23e-48bbf68a91f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RxRBmeKbtfqGmcGvkpQr6y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3157,
      "cache_read_input_tokens": 36947,
      "output_tokens": 688,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3157
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 688,
          "cache_read_input_tokens": 36947,
          "cache_creation_input_tokens": 3157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3157,
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
