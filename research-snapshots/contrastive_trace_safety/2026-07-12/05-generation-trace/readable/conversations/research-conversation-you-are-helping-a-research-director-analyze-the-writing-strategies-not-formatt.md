# Research conversation: You are helping a research director analyze the writing strategies (not formatting) of papers related to their project o

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 1
- **Tool calls:** 29
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a2c3ecdd6397fb570.jsonl`
- **Structured JSON:** [`d3ecd8bd6df8cecb6d15.json`](../../sessions/d3/d3ecd8bd6df8cecb6d15.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

67 recorded events

### User

_source line 1 · 2026-05-18T13:48:25.874Z_

You are helping a research director analyze the writing strategies (not formatting) of papers related to their project on hidden-state probing for LLM safety.

## Task
Read the paper's related work and literature map to identify the most relevant/influential papers. Then use WebSearch to find and analyze 5-8 key papers, focusing on:

1. **Narrative structure**: How do they open? What's their "hook"? How do they transition from problem → method → results?
2. **Framing strategy for negative/mixed results**: How do characterization studies or papers with partial negative results frame their contribution? (This is especially important - our paper is a characterization study with mixed results)
3. **How probing papers position themselves**: Papers like Hewitt & Manning 2019, Belinkov 2022, Burns et al. 2023 - how do they frame the value of probing analysis?
4. **How "sensitivity analysis" or "methodological finding" papers sell their contribution**: Our primary contribution is a methodological finding (layer selection sensitivity). How do similar papers make such findings compelling?
5. **Evidence presentation**: How do they handle "works on some models but not others" or "depends on hyperparameter X"?

## Key papers to look at (from our references)
- Hewitt & Manning 2019 "A Structural Probe for Finding Syntax in Word Representations" (control task methodology - our paper's closest analogy)
- Belinkov 2022 "Probing Classifiers" survey
- Burns et al. 2023 "Discovering Latent Knowledge" (CCS)
- Azaria & Mitchell 2023 "The Internal State of an LLM Knows When It's Lying"
- Li et al. 2024 "Inference-Time Intervention" (ITI)
- Any recent LLM safety monitoring papers (SafeThink, HarmThoughts, etc.)

## Files to read first
1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/related_work.tex` - our related work section
2. Try reading literature_map.yaml: use the MCP tool `mcp__agent-ml-research__read_project_file` with project="contrastive_trace_safety", file="literature_map.yaml"

## Output format
Write a structured analysis (800-1200 words) in Chinese, organized by writing strategy pattern, with specific examples from papers. Focus on actionable insights for rewriting our paper's Introduction/Abstract/Discussion. Do NOT give formatting advice - only narrative strategy.

The analysis should be directly useful for a paper rewrite where:
- Primary contribution is a methodological finding (layer selection sensitivity)
- Secondary contribution is empirical (HS > text, but encoder-conditional)
- Paper has extensive negative results (7 methods fail)
- Results are model-dependent (not universally clean)
- Target venue: EMNLP 2026 Findings

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "8a8ad4a9-5cd6-46aa-a848-05ad4c49dd3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T13:48:25.881Z_

```json
{
  "parentUuid": "8a8ad4a9-5cd6-46aa-a848-05ad4c49dd3c",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
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
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
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
  "uuid": "be5807e8-e31c-4d6a-b5f0-693b9cacc2a9",
  "timestamp": "2026-05-18T13:48:25.881Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T13:48:34.878Z_



I'll start by reading our related work section and literature map, then search for key papers to analyze their writing strategies.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be5807e8-e31c-4d6a-b5f0-693b9cacc2a9",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA93dxkkiHmhp2Rc1xfs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d16e9a6-b858-4652-ac73-cf0ec33ca523",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HP6gxnfuBAWESr7zfdwsdy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32139,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32139,
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

_source line 4 · 2026-05-18T13:48:35.877Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H7tBfmzzehiZUeLuHC6UsF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d16e9a6-b858-4652-ac73-cf0ec33ca523",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA93dxkkiHmhp2Rc1xfs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97c09aa5-17b7-4c93-a913-9b6e770699d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HP6gxnfuBAWESr7zfdwsdy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32139,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32139,
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

_source line 5 · 2026-05-18T13:48:35.912Z_

<details><summary>↩ Tool result · reported error · `toolu_01H7tBfmzzehiZUeLuHC6UsF`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97c09aa5-17b7-4c93-a913-9b6e770699d9",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "ca69ed67-f8d9-43bd-b43b-c341f7199a86",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27.",
  "sourceToolAssistantUUID": "97c09aa5-17b7-4c93-a913-9b6e770699d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T13:48:35.958Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RYF2c1mFubCxuGh2z1BN7M`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca69ed67-f8d9-43bd-b43b-c341f7199a86",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA93dxkkiHmhp2Rc1xfs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53befb35-84c1-47a9-90e2-d6cc2e7df7dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HP6gxnfuBAWESr7zfdwsdy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32139,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32139,
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

_source line 7 · 2026-05-18T13:48:35.962Z_

<details><summary>↩ Tool result · `toolu_01RYF2c1mFubCxuGh2z1BN7M`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53befb35-84c1-47a9-90e2-d6cc2e7df7dc",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "0771504e-72db-4042-8dde-d21e3ca615de",
  "sourceToolAssistantUUID": "53befb35-84c1-47a9-90e2-d6cc2e7df7dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-18T13:48:38.932Z_



Let me read the literature map and find the related work file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0771504e-72db-4042-8dde-d21e3ca615de",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA94PHycqQGBpSETzBe9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3229105-fef0-43c6-b6a5-0fa50d698412",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUQ6819ad8CCmc852V7JV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 32139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1464,
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

_source line 9 · 2026-05-18T13:48:39.905Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CxEtBcnfVmHFFS6XSo3VGs`</summary>

```json
{
  "project": "contrastive_trace_safety",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3229105-fef0-43c6-b6a5-0fa50d698412",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA94PHycqQGBpSETzBe9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b24a64f-367b-467a-b2f9-ae594d64bb7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUQ6819ad8CCmc852V7JV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 32139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1464,
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

### Tool result

_source line 10 · 2026-05-18T13:48:39.917Z_

<details><summary>↩ Tool result · `toolu_01CxEtBcnfVmHFFS6XSo3VGs`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'contrastive_trace_safety'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b24a64f-367b-467a-b2f9-ae594d64bb7f",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "1f4efc9b-c882-42c3-a953-7ec53f451bec",
  "sourceToolAssistantUUID": "6b24a64f-367b-467a-b2f9-ae594d64bb7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T13:48:40.390Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01985ufbLsekVbzVeMa4Wais`</summary>

```json
{
  "pattern": "**/related_work.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f4efc9b-c882-42c3-a953-7ec53f451bec",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA94PHycqQGBpSETzBe9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8e60637-b716-470a-849b-ae03892e35bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUQ6819ad8CCmc852V7JV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 32139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1464,
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

### Tool result

_source line 12 · 2026-05-18T13:48:40.427Z_

<details><summary>↩ Tool result · `toolu_01985ufbLsekVbzVeMa4Wais`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8e60637-b716-470a-849b-ae03892e35bb",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "02fb8aa2-e69f-4a8a-9d5c-4f070eb4050d",
  "sourceToolAssistantUUID": "e8e60637-b716-470a-849b-ae03892e35bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T13:48:40.919Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01G8pgT1FAFHG1AKDTg87MK5`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02fb8aa2-e69f-4a8a-9d5c-4f070eb4050d",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA94PHycqQGBpSETzBe9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c947e5d-2d44-4a76-a56a-dfae2671c151",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUQ6819ad8CCmc852V7JV4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 32139,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1464
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 293,
          "cache_read_input_tokens": 32139,
          "cache_creation_input_tokens": 1464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1464,
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

_source line 14 · 2026-05-18T13:48:40.949Z_

<details><summary>↩ Tool result · `toolu_01G8pgT1FAFHG1AKDTg87MK5`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T194646/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T194646/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T194646/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T203948/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T203948/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/_project/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/_project/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/exp_gru256_multilayer/per_seed_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c947e5d-2d44-4a76-a56a-dfae2671c151",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "69446f2c-0123-4043-87f6-2e70c55fe37a",
  "sourceToolAssistantUUID": "4c947e5d-2d44-4a76-a56a-dfae2671c151",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-18T13:48:44.569Z_

Now let me read the related work, introduction, and abstract to understand our paper's current framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69446f2c-0123-4043-87f6-2e70c55fe37a",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA94kKX94ABjAwAqzwEh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "231527b1-0730-49f9-870c-8a07bcd96540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bXKUzQqLxoSS21yeGekpn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 33603,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1457,
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

_source line 16 · 2026-05-18T13:48:45.053Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VgJrnFhUyL632pnXn9QrLi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "231527b1-0730-49f9-870c-8a07bcd96540",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA94kKX94ABjAwAqzwEh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5be1c030-b08b-4308-bb96-a3d5e7bf0abf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bXKUzQqLxoSS21yeGekpn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 33603,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1457,
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

_source line 17 · 2026-05-18T13:48:45.060Z_

<details><summary>↩ Tool result · `toolu_01VgJrnFhUyL632pnXn9QrLi`</summary>

```text
1	\section{Related Work}\label{sec:related-work}
2	
3	\paragraph{Safety in Reasoning Models.}
4	Reasoning models introduce a qualitatively new failure mode: the model's own chain of thought can transition from safety-aware deliberation to harmful generation without adversarial input modification~\cite{wang2025lrmsafety}.
5	
6	\textit{Attack characterization.} Self-jailbreak has been documented with step-level annotations~\cite{harmthoughts}, with longer chains increasing circumvention probability~\cite{selfjailbreak}. Reasoning models can autonomously jailbreak other LLMs with 97\% success~\cite{hagendorff2026lrm_jailbreak}. H-CoT~\cite{hcot2025} shows reasoning chains can be externally hijacked. Unfaithful reasoning~\cite{chen2025unfaithful} further motivates hidden-state monitoring that bypasses text. Safety-aligned models maintain refusal intentions during thinking but experience a sharp drop at output generation~\cite{yin2025refusal_cliff}, a phenomenon our temporal probes target. Refusal dynamics in standard LLMs~\cite{hu2026refusal_dynamics} and information leakage in traces~\cite{ahrend2026safer_traces} provide additional context.
7	
8	\textit{Detection.} CoT monitoring can detect reward hacking but optimization pressure promotes obfuscation~\cite{baker2025monitoring}. CoT monitorability is valuable but fragile~\cite{korbak2025cot_monitorability}. GuardReasoner~\cite{xiang2025guardreasoner} trains a dedicated reasoning-based guard model.
9	
10	\textit{Mitigation.} SafeThink~\cite{safethink} steers early reasoning toward safety, SafeRemind~\cite{saferemind} inserts entropy-triggered reminders, and Chain-of-Guardrails~\cite{mao2025selfjailbreak_reasoning} proposes guardrail insertion during reasoning. None of these conducts a systematic modality comparison for commitment detection.
11	
12	\paragraph{Hidden-State Safety Detection.}
13	Internal activations can detect safety violations in standard LLMs. \citet{zhou2024alignment} show safety-relevant information distributes across layers, while \citet{qi2025shallow_alignment} find that alignment operates primarily over early output tokens. \citet{arditi2024refusal} identify a single refusal direction, but \citet{zhao2025harmfulness} show harmfulness and refusal are encoded separately. \citet{joad2026refusal_multi} reveal eleven category-specific refusal directions, and \citet{wollschlager2025geometry} formalize multi-dimensionality through concept cones, consistent with our finding that single-direction methods are insufficient. TrajGuard~\cite{trajguard} uses Mahalanobis distance from safe trajectories; SafeSwitch~\cite{safeswitch} trains hidden-state classifiers; SIREN~\cite{siren} monitors internal representations during generation; SafeDream~\cite{safedream2026} proposes proactive world models for detection. These methods assume threats from external input manipulation and operate at the token level on instruction-tuned models. The self-jailbreak setting differs because transitions are internal and span multiple reasoning steps. \citet{kadali2025internal} decompose internal layer representations to separate jailbreak from benign prompts; their results confirm that layer-wise structure carries safety-relevant signal. We reproduce TrajGuard (\cref{sec:negative}) and find its geometric approach fails because discriminative signal resides in minor PCA components.
14	
15	\paragraph{Probing Methodology and Layer Selection.}
16	Causal abstraction~\cite{geiger2025causal} provides a theoretical foundation for mechanistic interpretability by formalizing when high-level causal models faithfully describe neural computation, grounding the use of internal representations for behavioral prediction. Linear probing has a long history from layer-wise classifiers~\cite{alain2017understanding} through sentence probing~\cite{conneau2018probing} to comprehensive surveys~\cite{belinkov2019analysis,belinkov2022probing}. Layer-wise analyses reveal hierarchical linguistic structure across depth~\cite{jawahar2019bert,liu2019linguistic}, and information-theoretic formulations address probe complexity~\cite{voita2020information,pimentel2020information}. \citet{hewitt2019control} introduce control tasks to distinguish structure from memorization, which we adopt (\cref{app:control}). \citet{belrose2023leace} establish theoretical limits on linear probe extraction; \citet{elazar2021amnesic} test whether probed information is causally used. \citet{tenney2019bert} show syntactic information in middle layers and semantics in deeper layers. \citet{zhang2025probing_selfverify} apply hidden-state probing to self-verification in reasoning models, a complementary perspective on what reasoning-model representations encode. Concurrent work by \citet{alvarez2026transport_geometry} uses hidden-state geometry for step-level hallucination detection; the approach shares our temporal probing framework but targets a different phenomenon. \citet{boxo2025linear_probes} show that linear probes can rely on textual evidence rather than deeper representations, which motivates our comparison of hidden-state probes against text-based monitors. Despite this foundation, layer selection remains underexamined: most studies select by a single metric without sensitivity analysis. We demonstrate that this practice can reverse a study's central conclusion (\cref{sec:layer-results}).
17	
18	\paragraph{Change-Point Detection.}
19	BOCPD~\cite{adams2007bayesian} detects abrupt distributional shifts; CCS~\cite{burns2023discovering} discovers latent truth directions via consistency constraints; RepE~\cite{zou2023representation} identifies concept directions through mean differences. We adapt all three to temporal commitment detection (\cref{sec:negative}). BOCPD and CUSUM fail because commitment is gradual. CCS provides no gain because its consistency objective misaligns with temporal structure. RepE shows inconsistent performance across models (0.756 on QwQ, 0.559 on R1-32B). These failures motivate supervised probes with principled layer selection as the minimal effective methodology.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5be1c030-b08b-4308-bb96-a3d5e7bf0abf",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "72eb08a0-9e73-46ec-8236-4809767962c6",
  "sourceToolAssistantUUID": "5be1c030-b08b-4308-bb96-a3d5e7bf0abf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T13:48:45.525Z_

<details open><summary>🔧 Tool call — Read · `toolu_013ytRMzT2ebBnAU2voe5ej2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72eb08a0-9e73-46ec-8236-4809767962c6",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA94kKX94ABjAwAqzwEh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c71b28e3-aaba-4829-b72f-0e61eab92d20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bXKUzQqLxoSS21yeGekpn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 33603,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1457,
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

_source line 19 · 2026-05-18T13:48:45.531Z_

<details><summary>↩ Tool result · `toolu_013ytRMzT2ebBnAU2voe5ej2`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Reasoning models such as DeepSeek-R1~\cite{deepseekr1} and QwQ~\cite{qwq} scale inference-time computation through extended chains of thought (CoT). Recent work documents that these models can ``self-jailbreak'': without adversarial input modification, the CoT transitions from safety-aware deliberation to committed harmful generation~\cite{harmthoughts,selfjailbreak}. We define the first reasoning step after which safety deliberation permanently ceases as the \textbf{Safety Commitment Point} (CP). This failure mode differs qualitatively from adversarial jailbreaks on standard LLMs because the harmful transition originates within the model's own reasoning. Before building production detectors, a prior question must be answered: can current probing methods reliably distinguish pre-CP from post-CP reasoning steps, and under what conditions? This paper provides a systematic characterization of what hidden-state and text-based probes can and cannot detect.
4	
5	Existing safety detectors target fundamentally different problems. Hidden-state (HS) methods such as TrajGuard~\cite{trajguard} and SafeSwitch~\cite{safeswitch} classify adversarial inputs at the token level, while text monitors like SafeRemind~\cite{saferemind} scan generated reasoning for explicit violations. Neither tracks the gradual, multi-step commitment process. A fundamental question remains: should a monitoring system read the model's hidden states or its generated text? This comparison has never been conducted under controlled conditions. Na\"ive reasoning suggests HS features (up to 5120 dimensions) should dominate text embeddings (384d sentence encoder), but no prior work tests this systematically. A further complication is that HS probes require selecting which transformer layer to monitor, a choice rarely scrutinized but potentially decisive.
6	
7	We present the first systematic evaluation across four reasoning models spanning two architectures (Llama, Qwen) and two scales (7--8B, 32B). Our central finding is methodological: the choice of layer selection metric entirely determines whether an HS advantage is observed. A composite metric (balanced accuracy $\times$ crossing rate) selects shallow layers for 32B models because shallow representations are highly compressed (inter-step cosine distances 1.4--2.7$\times$ smaller than at deep layers), so a linear probe operates near the noise floor and threshold crossings reflect noise rather than semantic transitions. At these layers, only the two 7--8B models show significant HS advantage. Threshold-dependent metrics excluding crossing rate consistently select deep layers (\cref{tab:layer_selection}), where all four models show significant HS advantage (Holm-Bonferroni corrected, \cref{sec:evaluation}; precision +15.4 to +32.5pp over 384d sentence embeddings; \cref{tab:hs_vs_text}).
8	
9	Our contributions are:
10	\begin{itemize}
11	    \item \textbf{Layer selection sensitivity.} We identify a systematic bias in composite metrics that reverses HS probe conclusions at 32B scale. A five-metric ablation establishes principled selection criteria (\cref{sec:layer-results}).
12	
13	    \item \textbf{Encoder-conditional directional advantage.} Against MiniLM-384d, all four models show significant HS precision gains (+15.4 to +32.5pp, Holm-Bonferroni corrected). PCA reduction to matched 384d dimensionality (79--92\% variance retained) preserves significance on all four models (+16.8 to +23.1pp), ruling out capacity gap as the sole explanation. Against BGE-large-1024d, all four models retain directional advantage but only 1/4 survives Holm-Bonferroni (\cref{fig:forest_precision}). The advantage has two separable components: a robust modality effect (survives dimensionality matching) and an encoder-dependent magnitude (narrows with stronger baselines). At 7--8B scale (moderate samples, robust across 5 seeds), evidence is strong; at 32B ($n{=}19$--$20$ test traces, sample-limited), model-specific caveats apply (\cref{sec:32b-analysis}).
14	
15	    \item \textbf{Negative results define method boundaries.} No alternative method consistently matches supervised probing across all four models (\cref{tab:negative}): BOCPD/CUSUM fail on gradual transitions; Mahalanobis distance finds near-zero separation; RepE achieves competitive balanced accuracy on QwQ-32B (0.756 vs.\ supervised 0.778) but at substantially lower precision (0.512 vs.\ 0.700), a metric-dependent discrepancy; cross-model transfer fails under PCA alignment. Control task selectivity (12.5--19.7pp above chance; \cref{app:control}) confirms genuine safety structure.
16	\end{itemize}
17	
18	\noindent Our results characterize the safety commitment phenomenon rather than constitute production detectors: false positive rates remain 39--52\%, and the 85.5\% oracle gap (\cref{sec:discussion}) underscores how much room remains for improvement.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c71b28e3-aaba-4829-b72f-0e61eab92d20",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "2c159452-bdaa-4d8a-82b0-437a970f0ca4",
  "sourceToolAssistantUUID": "c71b28e3-aaba-4829-b72f-0e61eab92d20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T13:48:45.980Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VpXbceEXSAnQjPv12BenF8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c159452-bdaa-4d8a-82b0-437a970f0ca4",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA94kKX94ABjAwAqzwEh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03f52ceb-774f-47fe-a22d-cc491d1dbe2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bXKUzQqLxoSS21yeGekpn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 33603,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1457,
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

_source line 21 · 2026-05-18T13:48:45.984Z_

<details><summary>↩ Tool result · `toolu_01VpXbceEXSAnQjPv12BenF8`</summary>

```text
1	Reasoning models with chain-of-thought can self-jailbreak: their reasoning traces transition from safe deliberation to committed harmful generation without adversarial input. We present the first systematic comparison of hidden-state (HS) probes and text-based monitors for detecting this safety commitment, evaluated across four reasoning models spanning two architectures and two scales (7--8B, 32B).
2	
3	Our central finding is methodological: the choice of layer selection metric can reverse a study's conclusions. A composite metric that incorporates crossing rate (the frequency of threshold crossings) systematically selects shallow layers at 32B scale and masks the HS advantage entirely. With principled layer selection, HS probes achieve precision gains of +15.4 to +32.5 percentage points over 384d sentence embeddings across all four models (Holm-Bonferroni corrected). PCA dimensionality matching to 384d preserves the advantage (all four models pass Holm-Bonferroni), ruling out a pure capacity explanation. Against a competitive 1024d encoder, all four models retain directional HS advantage but only 1/4 survives Holm-Bonferroni correction. The advantage has two separable components: a robust modality effect that survives dimensionality matching, and an encoder-dependent magnitude that narrows with stronger text baselines. At 32B ($n{=}19$--$20$, sample-limited), model-specific caveats further qualify the results.
4	
5	Our results characterize the safety commitment phenomenon rather than constitute production detectors: false positive rates remain 39--52\%, and no alternative method consistently matches supervised probing. Layer selection methodology is a critical, underexamined researcher degree of freedom in the probing literature.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03f52ceb-774f-47fe-a22d-cc491d1dbe2d",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "f408925f-c0f1-4409-8485-caab07faf4dc",
  "sourceToolAssistantUUID": "03f52ceb-774f-47fe-a22d-cc491d1dbe2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T13:48:46.560Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Lj96thA4ZbPZsSVQpPzET6`</summary>

```json
{
  "project": "contrastive_trace_safety",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f408925f-c0f1-4409-8485-caab07faf4dc",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA94kKX94ABjAwAqzwEh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d038182-2117-4e7a-be95-1f81e707c49e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bXKUzQqLxoSS21yeGekpn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 33603,
      "output_tokens": 357,
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
          "input_tokens": 1,
          "output_tokens": 357,
          "cache_read_input_tokens": 33603,
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

_source line 23 · 2026-05-18T13:48:46.571Z_

<details><summary>↩ Tool result · `toolu_01Lj96thA4ZbPZsSVQpPzET6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/paper_framing.md\", \"content\": \"# Paper Framing — contrastive_trace_safety\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (LLM Security Track)\\n- Deadline: ARR submission May 25, 2026\\n\\n## Core Claims (D031: layer selection as primary contribution, 4 models)\\n\\n**Contribution structure (D031)**:\\n- **Primary (methodological)**: Layer selection metric sensitivity — biased metrics reverse conclusions\\n- **Secondary (empirical)**: HS advantage at correct layers, qualified by scale; temporal improvement universal\\n- **Tertiary (negative results)**: 6 alternative methods fail, establishing what doesn't work\\n\\n1. **Temporal context universally improves probe accuracy across both modalities** (D014 + D023 nuanced) — Temporal context is the most robust improvement across all 4 models and both modalities. Text probes benefit consistently from larger windows across all models. HS probes benefit in 3/4 models; OT-7B HS peaks at W=3 and declines at larger W (confirmed on both layer 0 and layer 16).\\n\\n   **HS temporal gains** (W=1→best, 3 original models): accuracy +3pp (77.8%→81.0%), precision +13pp (69.3%→82.2%), FPR halved (9.65%→4.83%).\\n   **OT-7B HS temporal** (layer 16): bal_acc peaks at W=3 (68.8%), declines to 65.9% at W=25 (-2.9pp). BUT precision and FPR continue improving (prec 42.8%→49.4%, FPR 12.0%→7.5%). Temporal saturation is bal_acc-specific; larger W trades bal_acc for better precision/FPR. Confirmed on both layer 0 and layer 16 — genuine OT-7B characteristic.\\n   **Text temporal gains** (all 4 models, W=1→best): universally +3-12pp bal_acc, +8-23pp precision, FPR reduced.\\n\\n   **IMPORTANT: coverage direction depends on detection criterion K.** K=1 (single crossing): coverage DECREASES with W. K=5 (consecutive crossings): coverage may INCREASE with W. Claim 1 is about accuracy/precision improvement, NOT coverage.\\n\\n   The core insight: \\\"Temporal context universally improves text probes across all 4 models. For HS probes, 3/4 models benefit from larger temporal windows, while OT-7B shows early saturation (W=3 peak).\\\"\\n\\n2. **HS probes outperform text probes at correctly selected layers, with strong evidence at 7-8B and model-specific patterns at 32B** (D031: qualified from D030 \\\"universal\\\") —\\n\\n   **KEY FINDING (D029)**: The apparent \\\"scale-dependent\\\" HS advantage (significant at 7-8B, absent at 32B) was an artifact of the layer selection metric `bal_acc × crossing_rate`, which systematically selects shallow layers for 32B models. At correctly selected deep layers, HS outperforms text on all 4 models, but the NATURE of the advantage differs by scale.\\n\\n   **Layer selection metric bias (D028, refined D036)**: `bal_acc × crossing_rate` selects shallow layers because shallow layers have higher crossing rates (more trigger-happy probes). 3/4 non-biased threshold-dependent metrics (precision, pre_cp_fpr, composite) converge on deep layers; pure bal_acc (threshold-free) selects middle layers (L30/L47). Deployment-relevant metric consensus selects L60/L63 for 32B models.\\n\\n   **7-8B models: HS significantly outperforms text (2/2 models) — UNCHANGED**\\n\\n   **R1-8B (Llama-8B, R1-distilled, n=43):**\\n   - Precision: 69.7% vs 47.2% (+22.4pp, p<0.001, **Holm-Bonferroni ✅**)\\n   - Accuracy: 81.3% vs 72.9% (+8.2pp, p=0.005, **Holm-Bonferroni ✅**)\\n   - Pre-CP FPR: 14.8% vs 22.2% (-7.4pp, p=0.044, **Holm-Bonferroni ✅** — rank 12/12, threshold=0.0500)\\n\\n   **OT-7B (Qwen-7B, STILL-trained, n=47, layer 16, matched W=3) — D026 M001 corrected:**\\n   - Bal Acc: 68.8% vs 58.1% (+10.7pp, p<0.001, **Holm-Bonferroni ✅**)\\n   - Precision: 46.6% vs 24.7% (+21.9pp, p<0.001, **Holm-Bonferroni ✅**)\\n   - Pre-CP FPR: 10.0% vs 27.1% (-17.1pp, p<0.001, **Holm-Bonferroni ✅**)\\n   - **3/3 metrics significant — OT-7B cleanest single-model evidence**\\n\\n   **32B models: HS outperforms text at CORRECTED LAYERS but with model-specific caveats (D029+D031)**\\n\\n   **QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 corrected from L2):**\\n   - Bal Acc: +11-22pp across all 15 window sizes, all p<0.005 (bootstrap, null-centered)\\n   - 15/15 W values show significant HS advantage\\n   - **CRITICAL CAVEAT (D031)**: HS lead time NEGATIVE (-1.2 to 1.9 steps vs text 3.7-12.3). HS is \\\"more accurate but detects later.\\\" Position baseline bal_acc=0.746 > HS=0.740. In safety deployment, detecting 8-12 steps earlier may outweigh higher accuracy.\\n   - W=3: bal_acc +15.4pp, precision +23.6pp, FPR -9.8pp — **3/3 Holm-Bonferroni ✅**\\n\\n   **R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 corrected from L10):**\\n   - W=1: bal_acc +18.7pp (0.826 vs 0.639), p=0.000; precision +15.4pp (0.603 vs 0.448), p=0.000; FPR -14.6pp (0.235 vs 0.380), p=0.007 — **3/3 Bonferroni ✅**\\n   - W=3: bal_acc +11.2pp p=0.020, precision p=0.032, FPR p=0.077 — **0/3 Bonferroni** (v2 null-centered)\\n   - W=5-15: all NS\\n   - **CRITICAL CAVEAT (D031)**: Only W=1 passes Bonferroni, coverage=25% (5/20 traces). Evidence statistically narrow.\\n   - **POSITIVE**: Lead time +11.7-13.3 steps (excellent early warning). HS >> Position (+14.2pp).\\n   - **NOTE**: L10 vs L63 at W=10: L10=0.795 vs L63=0.754 — L10 slightly better. \\\"Scheme B选错层\\\" narrative weaker for R1-32B.\\n   - ✅ P-VALUE UNIFIED: null-centered two-sided, consistent with QwQ.\\n\\n   **32B cross-model divergence (D031 key finding for Discussion):**\\n   | Dimension | R1-32B L63 | QwQ L60 |\\n   |-----------|-----------|---------|\\n   | Bonferroni | W=1 only (3/3) | All 15 W (3/3) |\\n   | Lead time | +11.7 to +13.3 (excellent) | -1.2 to +1.9 (poor) |\\n   | HS vs Position | HS >> Pos (+14.2pp) | HS < Pos (-0.6pp) |\\n   | Coverage (W=1) | 25% | 74% |\\n   Paper MUST discuss this divergence per-model, not unify into single narrative.\\n\\n   **OLD 32B results at BIASED layers (L2/L10) — RETRACTED as metric artifact:**\\n   - R1-32B L10: precision +9.4pp (p=0.064), accuracy +6.2pp (p=0.13)\\n   - QwQ-32B L2: precision +5.8pp (p=0.35), accuracy +0.9pp (p=0.83)\\n   - These non-significant results were caused by the biased `bal_acc × crossing_rate` metric selecting layers where HS signal is weak.\\n\\n   **Holm-Bonferroni COMPLETE (D032): 12/12 ALL PASS**\\n   Previously 5/12 (biased layers). With corrected layers: **12/12** step-down pass (α=0.05).\\n\\n   | Rank | Model | Metric | p-value | Threshold | Pass |\\n   |------|-------|--------|---------|-----------|------|\\n   | 1 | R1-8B | precision | <0.001 | 0.0042 | ✅ |\\n   | 2 | OT-7B | bal_acc | <0.001 | 0.0045 | ✅ |\\n   | 3 | OT-7B | precision | <0.001 | 0.0050 | ✅ |\\n   | 4 | OT-7B | FPR | <0.001 | 0.0056 | ✅ |\\n   | 5 | QwQ | bal_acc | <0.001 | 0.0063 | ✅ |\\n   | 6 | QwQ | precision | <0.001 | 0.0071 | ✅ |\\n   | 7 | R1-32B | bal_acc | <0.001 | 0.0083 | ✅ |\\n   | 8 | R1-32B | precision | <0.001 | 0.0100 | ✅ |\\n   | 9 | QwQ | FPR | 0.004 | 0.0125 | ✅ |\\n   | 10 | R1-8B | bal_acc | 0.005 | 0.0167 | ✅ |\\n   | 11 | R1-32B | FPR | 0.007 | 0.0250 | ✅ |\\n   | 12 | R1-8B | FPR | 0.044 | 0.0500 | ✅ |\\n\\n   **Caveats**: Different W per model (R1-8B W=15, OT-7B/QwQ W=3, R1-32B W=1). Tests measure \\\"HS > text at each model's best setting,\\\" not \\\"at uniform W.\\\" R1-32B W=1 has 25% coverage. Paper must state these conditions.\\n\\n   **FPR dual reporting**: Step-level (r1-8b: HS 8.8%, text 20.5%) vs trace-level (HS 14.8%, text 22.2%). Both reported.\\n\\n   **FPR reversal RESOLVED (D026)**: OT-7B HS FPR@L16 (10.0%) < Text FPR at ANY window (16.1%). HS dominates on FPR at 7-8B.\\n\\n   **Effect size consistency**: Precision advantage across all 4 models at corrected layers: R1-8B +22.4pp, OT-7B +21.2pp, QwQ +23.6pp, R1-32B +15.4pp. Remarkably consistent +15-24pp range.\\n\\n   Paper recommended claim (D032): \\\"At correctly selected layers, HS probes significantly outperform text probes on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp). The layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers, entirely masking this advantage at 32B scale. Practical implications differ by model: 7-8B models show strong HS advantage with comparable timing; R1-32B shows excellent lead time (+13 steps) but narrow coverage at the significant window; QwQ shows robust statistical significance but HS detects later than text.\\\"\\n\\n3. **HS and text monitoring exhibit different detection timing profiles** (narrowed from old Claim 3, now 4/4 models with GRU) — On r1-8b: HS temporal LR detects AT the commitment point (lead ~0) while text detects ~10 steps earlier. GRU achieves modest positive lead (+4.5+-3.0, worst seed +0.9). BOCPD/CUSUM fail to improve over simple thresholds. The oracle's +31-step advantage shows hidden states encode current safety state but poorly predict future trajectory. On 32B models: timing profiles vary (QwQ GRU lead +15.9, R1-32B +8.8) but FPR differences are non-significant. OT-7B GRU (layer 16, multi-layer L13-19, 3 seeds): bal_acc 74.6+-1.3%, coverage 64.5+-7.0%, lead +33.6+-4.8, FPR 27.4+-6.1%. GRU trades higher FPR for longer lead (consistent with R1-8B pattern). NOTE: OT-7B absolute lead times are inflated by long traces (~80 sentences vs ~30). Paper should normalize or explicitly caveat trace length differences when comparing across models.\\n\\n   NOTE: 32B timing profiles should be RE-EVALUATED at corrected layers (L60/L63) — current GRU results used old biased layers.\\n\\n## Methodological Contribution: Layer Selection Sensitivity (D028, elevated from RETRACTED Claim 4)\\n\\nThe layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers because shallow layers have higher crossing rates (more frequently crossing the detection threshold). This bias is especially problematic for 32B models, where it selects layers at 3-16% depth instead of deep layers selected by threshold-dependent metrics.\\n\\n**Ablation evidence (4 models × 5 metrics) — UPDATED D036**:\\n- `bal_acc × crossing_rate`: selects L2 (QwQ), L10 (R1-32B) — shallow, biased\\n- Pure `bal_acc`: selects **middle layers** for 32B — L30 (QwQ, 47%), L47 (R1-32B, 73%); deep for 7-8B (agrees with other metrics). Threshold-free metric, behaves like AUROC.\\n- `precision`: selects deep layers for all models (L60/L63 for 32B)\\n- `pre_cp_fpr`: selects deep layers for all models\\n- `composite` (additive): selects deep layers for all models\\n- **Pattern**: Threshold-FREE metrics (bal_acc, AUROC) → middle layers; threshold-DEPENDENT metrics (precision, FPR, composite) → deep layers. Crossing_rate-contaminated metrics → shallow layers.\\n\\n**LOO-CV stability (D036)**: Under LOO-CV, the dominant layer is selected in 65-68% of folds regardless of metric. QwQ L30 selected 13/19 folds (bal_acc), R1-32B L47 selected 13/20 folds (bal_acc). Selection is robust to val set composition.\\n\\n**Corrected layer definition (D036)**: \\\"Corrected layers\\\" = consensus of threshold-dependent metrics (precision, inverse FPR, additive composite) — 3 of 4 non-biased metrics, not all 4. Pure bal_acc selects middle layers (L30/L47) with higher step-level accuracy (0.75/0.83 vs 0.71/0.76 at deep layers), but deployment-relevant metrics (precision, FPR) favor deep layers where all 4 models achieve HB-significant HS advantage.\\n\\n**Impact**: Incorrect layer selection entirely masked the HS advantage at 32B scale, leading to the false conclusion that HS advantage is scale-dependent. Even among unbiased metrics, metric choice affects optimal layer depth — threshold-free vs threshold-dependent is a second dimension of researcher degrees of freedom beyond the crossing_rate bias.\\n\\n**Anti-circular-reasoning defense (D031, refined D036)**: The claim that deep layers are \\\"correct\\\" for deployment rests on: (1) `crossing_rate` has a MECHANISTIC bias — shallow layers have compressed representations (1.4-2.7× smaller cosine distances) generating noise-driven crossings; (2) threshold-dependent metrics (precision, FPR) directly measure deployment-relevant properties; (3) at deep layers, all 4 models show significant HS advantage (HB corrected); (4) LOO-CV confirms selection stability. The paper presents layer selection as a \\\"researcher degree of freedom\\\" with systematic audit via sensitivity analysis.\\n\\n**Paper treatment**: Dedicated subsection in Method + Table showing metric × model → selected layer + downstream HS-text comparison. Frame as sensitivity analysis, not \\\"correct vs incorrect.\\\"\\n\\n## Story Spine\\n\\n- **Problem**: Reasoning models exhibit \\\"self-jailbreak\\\" — safety reasoning and harmful execution interleave throughout extended CoT, culminating in a \\\"commitment point\\\" where safety reasoning permanently ceases. Existing hidden-state detectors (TrajGuard, SafeSwitch, SIREN) target adversarial INPUT attacks on instruction-tuned models; they have never been evaluated on reasoning-model self-jailbreak where the threat is the model's OWN reasoning process.\\n\\n- **Existing approaches & gaps**: Hidden-state detectors achieve 95% defense on standard LLMs (TrajGuard) but operate at token-level. Reasoning-model safety analysis (Self-Jailbreaking, HarmThoughts) characterizes the phenomenon without providing deployable detectors. Text-level CoT monitors (SafeRemind, SafeThink) are vulnerable to pathological CoT. No prior work systematically compares detection modalities for reasoning-model self-jailbreak.\\n\\n- **Our framing**: We provide the first systematic evaluation of detection methods for reasoning-model safety commitment across **4 models, 2 architectures (Llama + Qwen), 2 training methods (R1-distilled + STILL), and 2 scales (7-8B + 32B)**, comparing hidden-state probes, text-based probes, sequence models (GRU), change-point detection (BOCPD/CUSUM), unsupervised methods (Mahalanobis, RepE direction, CCS), and nonlinear probes (MLP). We discover that: (a) temporal context is the most robust improvement, benefiting both modalities universally; (b) HS probes universally outperform text at correctly selected layers, with a critical sensitivity to layer selection methodology; (c) existing methods designed for other settings (TrajGuard, BOCPD, CCS, RepE) fail on reasoning model commitment; (d) linear probes are sufficient (MLP adds no value); (e) safety representations are model-specific (cross-transfer fails entirely), validated by control task (selectivity 7.5-18.5pp).\\n\\n- **Headline result (D032)**: \\\"Hidden-state probes significantly outperform text probes for safety commitment detection on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp), but this advantage is entirely invisible under biased layer selection metrics. The composite metric `bal_acc × crossing_rate` systematically selects shallow layers at 32B scale, masking the HS signal and producing false negatives. This methodological finding, together with model-specific practical trade-offs at 32B (early detection vs broad coverage) and the comprehensive failure of 6 alternative methods, establishes that supervised temporal probing with principled layer selection is the most effective and robust approach for monitoring reasoning-model safety commitment.\\\"\\n\\n## Key Evidence Summary\\n\\n### R1-8B (Llama-8B, R1-distilled, n=43 test, class_weight=balanced, 60/20/20 split — CANONICAL)\\n\\nBest layer: 14 (45% depth). Full sweep layers 0-24 confirmed: layer 12 marginally better (+0.4pp bal_acc), no practical difference.\\n\\n| Method | Coverage | Lead Time | Pre-CP FPR | Safe FPR |\\n|--------|----------|-----------|------------|----------|\\n| HS Static LR L14 | — | -2.0 | **9.7%** | — |\\n| HS Temporal W=5 | — | +0.6 | **10.2%** | — |\\n| HS Temporal W=15 | — | **-0.1** | **8.8%** | — |\\n| Text Temporal W=15 | — | +10.3* | 20.5% | — |\\n| GRU Multi-7L (3-seed) | 72.9+-4.0% | +4.5+-3.0 | 16.5+-4.1% | — |\\n\\n*Text lead time inflated by high pre-CP FPR (trigger-happy detection)\\nNOTE: HS LR lead time collapsed to ~0 with balanced weights — HS detects AT commitment, not before. Only GRU achieves positive lead (+4.5, worst seed +0.9).\\n\\n### OT-7B (Qwen-7B, STILL-trained, n=47 test, 228 total traces) — D026 CORRECTED to layer 16\\n\\nBest layer: **16 (57% depth)**. M001 corrected: layer 0 was selected by bal_acc x crossing_rate bug; layer 16 selected by bal_acc.\\n\\n| Method | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |\\n|--------|---------|-----------|----------|-----------|------|\\n| HS Temporal W=3 L16 (best) | **68.8%** | **46.6%** | 53.2% | **10.0%** | — |\\n| Text Temporal W=25 (best) | 61.4% | 32.9% | 66.0% | 16.1% | 45.5 |\\n| Text Temporal W=3 (matched) | 57.9% | 25.4% | — | 27.1% | — |\\n\\nBootstrap (layer 16, matched W=3, 1000 resamples):\\n   bal_acc +10.7pp, 95% CI [4.9, 16.3], p<0.001 ✅\\n   precision +21.9pp, 95% CI [14.0, 29.6], p<0.001 ✅\\n   FPR -17.1pp, 95% CI [-22.2, -12.2], p<0.001 ✅ — **3/3 Holm-Bonferroni**\\nSelectivity: 18.3pp (real=0.688, random=0.505) — highest across all models\\n\\n### 32B Cross-Architecture — D029 CORRECTED LAYERS\\n\\n**QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 — corrected from L2)**\\n- HS vs Text bootstrap (null-centered, 1000 resamples):\\n  - Bal Acc: +11-22pp across W=1-15, ALL 15/15 significant (p<0.005)\\n  - W=3 (matched): bal_acc +15.4pp (p<0.001 ✅), precision +23.6pp (p<0.001 ✅), FPR -9.8pp (p=0.004 ✅) — **3/3 Holm-Bonferroni**\\n- Caveats: HS lead time poor (-1.2 to 1.9 steps vs text 3.7-12.3), position baseline competitive\\n- Layer selection: `bal_acc × crossing_rate` selected L2 (3.1%); threshold-dependent metrics consensus selects L60 (94%); pure `bal_acc` selects L30 (47%, bal_acc=0.7513 vs L60=0.7101) (D036)\\n\\n**R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 — corrected from L10)**\\n- W=1: bal_acc +18.7pp, p<0.001 ✅\\n- W≥5: NS (dimensionality: 51200 × W features for n=20)\\n- W=1: 3/3 Holm-Bonferroni ✅; W=3: 0/3 Bonferroni (null-centered v2); W≥5: NS\\n- Layer selection: `bal_acc × crossing_rate` selected L10 (15.6%); threshold-dependent metrics consensus selects L63 (98%); pure `bal_acc` selects L47 (73%, bal_acc=0.8290 vs L63=0.7585) (D036)\\n\\n**OLD biased-layer results (RETRACTED as metric artifact):**\\n| Model | Biased Layer | Corrected Layer | Biased p-value | Corrected p-value |\\n|-------|-------------|----------------|----------------|-------------------|\\n| R1-32B | L10 (16%) | L63 (98%) | 0.064-0.13 (NS) | <0.001 (W=1) ✅ |\\n| QwQ-32B | L2 (3%) | L60 (94%) | 0.35-0.83 (NS) | <0.005 (all W) ✅ |\\n\\n### 4-Model Holm-Bonferroni Summary (D032 — COMPLETE: 12/12 ✅)\\n\\n| Model | Arch | Training | Scale | Layer | W | bal_acc | precision | FPR | Selectivity |\\n|-------|------|----------|-------|-------|---|--------|-----------|-----|-------------|\\n| R1-8B | Llama | R1-distilled | 8B | L14 (45%) | 15 | +8.2pp ✅ | +22.4pp ✅ | -7.4pp ✅ | 12.5pp |\\n| OT-7B | Qwen | STILL | 7B | L16 (57%) | 3 | +10.7pp ✅ | +21.9pp ✅ | -17.1pp ✅ | 18.3pp |\\n| QwQ-32B | Qwen | native | 32B | L60 (94%) | 3 | +15.4pp ✅ | +23.6pp ✅ | -9.8pp ✅ | 15.3pp |\\n| R1-32B | Qwen | R1-distilled | 32B | L63 (98%) | 1 | +18.7pp ✅ | +15.4pp ✅ | -14.6pp ✅ | 7.5pp |\\n\\n**12/12 all pass Holm-Bonferroni step-down (α=0.05)**. Previously 5/12 with biased layers.\\nPrecision advantage remarkably consistent: +15.4 to +23.6pp across all 4 models.\\nCaveats: Different W per model; R1-32B W=1 coverage=25%; QwQ lead time negative.\\n\\n### Position Mediation Analysis (D038 → D039 corrected)\\n\\n**Universal finding**: Position (relative step t/T) is a significant component of probe performance across all models. Residualizing out position reduces HS BA by 12-18pp at optimal W, but all models retain substantial non-positional signal.\\n\\n| Model | Optimal W | Original HS BA | Residualized HS BA | Drop | Residualized Text BA | HS-Text Residual Gap |\\n|-------|-----------|----------------|-------------------|------|---------------------|---------------------|\\n| R1-8B | W=15 | 0.834 | 0.669 | 16.5pp | 0.605 | +6.4pp |\\n| R1-8B | W=3 | 0.813 | 0.571 | 24.3pp | 0.534 | +3.7pp |\\n| QwQ-32B | W=3 | 0.796 | 0.619 | 17.7pp | — | — |\\n| OT-7B | W=3 | 0.732 | 0.609 | 12.3pp | 0.540 | +6.9pp |\\n\\nPosition-only BA = 0.706 (consistent, W-independent). All residualized p < 0.001.\\n\\n**D039 correction**: D038 concluded \\\"7-8B more position-dependent than 32B\\\" based on R1-8B W=3 (drop 24.3pp vs QwQ 17.7pp). This was wrong — W=3 is not R1-8B's optimal W. At optimal W, drops are comparable across scales (12-18pp). No scale-dependent position mediation difference.\\n\\n**Key implications for paper**:\\n1. Position is a significant but partial component (12-18pp drop) — universal across models\\n2. All models retain substantial non-positional signal (residualized BA 0.61-0.67, all p < 0.001)\\n3. HS residualized > text residualized (+3.7 to +6.9pp) — HS advantage persists after position removal\\n4. Temporal windowing preserves non-positional signal: larger W reduces position dependence (R1-8B: 24pp drop@W=3 → 16pp@W=15)\\n5. Paper should NOT say \\\"position-independent\\\" or \\\"predominantly position-mediated\\\" — say \\\"position is a significant component but probes capture substantial additional signal\\\"\\n\\n**Residualized precision**: Not tested (Reviewer recommendation: scope to BA, leave precision residualization as future work).\\n\\n### Negative Results (expanded with R3 supplementary experiments)\\n- **BOCPD/CUSUM (4/4 models)**: R1-8B BOCPD 93% detection but lead +3.5 < threshold +4.9; OT-7B/R1-32B/QwQ all 0% detection across all λ. CUSUM worse than threshold on all models.\\n- **Mahalanobis (4/4 models confirmed negative)**: R1-8B (+0.07), OT-7B (+0.031), R1-32B (+0.148), QwQ (+0.204) — all separation ≈ 0. Signal in minor PCA components, not principal directions.\\n- **RepE direction probing (4/4 models, corrected layers confirmed)**: Direction-based supervised method (needs CP labels). Results highly layer-dependent and model-specific:\\n  - R1-32B L63 (corrected): bal_acc=0.559 (near-random), FPR=49.9% — **direction vector fails at deep layer** where supervised LR excels (0.826). Train-test gap 13.3pp shows poor generalization.\\n  - QwQ L60 (corrected): bal_acc=0.756, precision=0.512, FPR=0.309 — **improves** from L2 (0.666), narrows gap with supervised LR W=1 (0.740 bal_acc), but still inferior in precision/FPR.\\n  - R1-8B L14: bal_acc=0.749, OT-7B L16: bal_acc=0.642\\n  - **Key insight**: Supervised LR is necessary — mean-difference direction cannot decode safety commitment at deep layers for R1-32B (discriminative training finds signal that simple direction averaging misses). Layer selection sensitivity applies to RepE too, but in model-specific ways (R1-32B: shallow better for RepE; QwQ: deep better for both).\\n- **MLP nonlinear probe (4/4 models)**: 3/4 models worse than LR. Linear probes sufficient; nonlinearity adds no value.\\n- **CCS-adapted (Burns et al. 2023, 4/4 models)**: WEAKLY SUPERVISED (needs CP labels for pair construction, not truly unsupervised). R1-8B bal_acc=0.777 (between supervised LR 0.817 and RepE 0.749). R1-32B FPR=0.410 (near-chance). OT-7B precision=0.319 (near-chance, high lead=20.5 is artifact of high FPR). Uses scheme B layers (biased). Paper must: (a) label as \\\"weakly supervised\\\" not \\\"unsupervised\\\"; (b) disclose pair construction differs from Burns et al.; (c) note scheme B layer limitation.\\n- **Cross-model transfer (exp-003)**: All directions fail entirely (best: 58.3% acc, 40.7% crossing).\\n\\n## Venue Fit Risks\\n\\n- **EMNLP LLM Security track fit**: Strong — defense/detection evaluation for reasoning model jailbreak.\\n- **Method simplicity risk**: Mitigate: frame as empirical study. Contribution is systematic evaluation + layer selection sensitivity discovery + comprehensive negative results.\\n- **Statistical power**: With corrected layers, **12/12** tests pass Holm-Bonferroni across ALL 4 models (up from 5/12 with biased layers).\\n- **HS advantage universal**: UPGRADED from \\\"scale-dependent\\\" — layer selection is the true moderator, not scale. Cleaner story.\\n- **Trace vs step FPR**: Both reported with explanation.\\n- **High safe FPR risk**: All methods 39-62% safe FPR. Frame as diagnostic tool limitation.\\n- **32B caveats**: HS advantage exists but is more sensitive to window size (R1-32B W=1 only) and affected by dimensionality (51200-d at large W with n=20). Lead times shorter than 7-8B. These are honest limitations, not disqualifiers.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. \\\"Method novelty?\\\" → Empirical study + systematic method comparison + layer selection sensitivity as methodological contribution + comprehensive negative results (6 methods fail).\\n2. \\\"Only one model family?\\\" → **RESOLVED**: 4 models, 2 architectures (Llama + Qwen), 2 training methods, 2 scales. ALL showing significant HS advantage at corrected layers.\\n3. \\\"GRU unstable?\\\" → 3-seed reporting with worst-seed bounds. R1-32B GRU at L10 was unstable; needs re-evaluation at L63.\\n4. \\\"Too few traces?\\\" → Cross-model validation + control task selectivity 7.5-18.5pp.\\n5. \\\"Fine-grained taxonomy?\\\" → Out of scope for current study.\\n6. \\\"HS doesn't beat text?\\\" → **QUALIFIED REBUTTAL (D031)**: HS outperforms text at correct layers with STRONG evidence at 7-8B (precision +22pp, Holm-Bonf) and QUALIFIED evidence at 32B (R1-32B: significant W=1 but narrow; QwQ: significant all W but late detection). 32B non-significance at OLD layers was artifact. Layer selection sensitivity analysis shows this is a methodological issue, not absence of signal.\\n7. \\\"Commitment point circular?\\\" → Cross-model consistency + control task selectivity argues against artifact.\\n8. \\\"Missing related work?\\\" → Expansion to 30+ citations.\\n9. \\\"No FPR analysis?\\\" → RESOLVED: both trace-level and step-level FPR reported.\\n10. \\\"High safe FPR?\\\" → Limitation acknowledged.\\n11. \\\"Control task / position confound?\\\" → RESOLVED (C2, D011): selectivity 7.5-18.5pp, HS FPR < position-only FPR.\\n12. \\\"Multiple testing correction?\\\" → **RESOLVED**: 12/12 Holm-Bonferroni step-down (α=0.05) across all 4 models (up from 5/12 with biased layers).\\n13. \\\"Trace vs step FPR?\\\" → Both reported with explanation.\\n14. \\\"Layer selection is just hyperparameter tuning?\\\" → No — we show a systematic bias in a commonly used composite metric. The ablation across 5 metrics × 4 models is a reproducible methodological finding, not a one-off parameter choice.\\n15. \\\"Why not just use the best layer for each model?\\\" → We do. The point is that the METRIC for selecting \\\"best\\\" matters. Biased metrics produce systematically wrong selections, masking real effects.\\n16. \\\"32B results are marginal / only W=1 significant for R1-32B?\\\" → Dimensionality constraint (51200 × W > n=20 at W≥5). QwQ L60 significant at ALL W values. R1-32B L63 significant at W=1. Both confirm HS advantage exists; practical deployment would use W=1-3 for 32B models.\\n\\n## Title Candidates (D031)\\n- \\\"Layer Selection Matters: How Metric Choice Determines Hidden-State Probe Effectiveness for Safety Monitoring\\\"\\n- \\\"Temporal Probing for Safety Commitment Detection in Reasoning Models: A Comprehensive Evaluation\\\"\\n- \\\"What Detects Safety Commitment in Reasoning Models? A Systematic Comparison of Probe-Based Methods\\\"\\n- \\\"Hidden-State vs Text Monitoring for Reasoning Model Safety: Layer Selection as the Missing Variable\\\"\\n\", \"total_chars\": 26683, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d038182-2117-4e7a-be95-1f81e707c49e",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "84ed1890-8d81-43c9-87e4-17b44de7d3bf",
  "sourceToolAssistantUUID": "4d038182-2117-4e7a-be95-1f81e707c49e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-18T13:48:51.517Z_

Now let me read the discussion section for additional context, and then search for the key papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84ed1890-8d81-43c9-87e4-17b44de7d3bf",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA95ATqPbNQsVfzmr1YQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a297bc7-a652-4f32-b040-bafa8736b2ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSb8qwZ3ZSsxspA4SNkB4S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13631,
      "cache_read_input_tokens": 35060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13631,
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

_source line 25 · 2026-05-18T13:48:53.572Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BfvZp9wcQpmuhKBXrWdvnh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a297bc7-a652-4f32-b040-bafa8736b2ee",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA95ATqPbNQsVfzmr1YQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a06490bb-fa41-417a-9a34-03896049795b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSb8qwZ3ZSsxspA4SNkB4S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13631,
      "cache_read_input_tokens": 35060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13631,
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

_source line 26 · 2026-05-18T13:48:53.585Z_

<details><summary>↩ Tool result · `toolu_01BfvZp9wcQpmuhKBXrWdvnh`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Layer selection as researcher degree of freedom.}
4	Layer selection is an underexamined methodological choice in the probing literature that can silently determine a study's conclusions. Our five-metric ablation (\cref{sec:layer-results}) demonstrates that a single metric component, the crossing rate, reverses the central finding: at biased layers, the HS advantage appears scale-dependent; at corrected layers, all four models are significant (\cref{sec:evaluation}). The mechanism is representation compression at shallow layers (\cref{app:cosine_volatility}), which pushes a linear probe to the noise floor and inflates crossing rate independently of discriminative power. Any composite metric that incorporates crossing rate is susceptible to this bias, and we hypothesize the effect generalizes beyond safety probing to any threshold-based detection study. We recommend that probing studies report results under at least two complementary layer selection criteria and that multi-metric ablations become standard practice.
5	
6	\paragraph{Temporal context and modality choice.}
7	Both temporal context and modality choice improve detection, but their relative magnitudes differ by scale: at 7--8B, the modality advantage exceeds temporal improvement (\cref{sec:temporal}); at 32B, relative magnitudes are model-dependent. Temporal windowing ($W{=}3$ to $15$) provides consistent improvement regardless of modality, while modality choice requires principled layer selection.
8	
9	\paragraph{Encoder-conditional advantage.}
10	Part of the observed advantage may reflect text encoder quality rather than hidden-state informational superiority. At matched 384d dimensionality via PCA (79--92\% variance retained), the precision advantage persists on all four models (+16.8 to +23.1pp, all four model-level precision tests pass Holm-Bonferroni), eliminating capacity gap as the sole explanation. A stronger 1024d encoder closes most of the significance gap (1/4 HB-significant), suggesting a continuum rather than a binary modality distinction. The HS advantage has two separable components: a robust modality effect that survives dimensionality matching, and an encoder-dependent magnitude component that narrows with stronger baselines.
11	
12	\paragraph{Cross-model divergence and design implications.}
13	R1-32B and QwQ-32B share architecture but present opposite detection profiles (\cref{tab:32b_divergence}), with training method (distillation vs.\ native reasoning) as the likely differentiator; per-model validation is essential. If future work achieves acceptable false positive rates, our results suggest temporal windowing ($W{=}3$--$15$) with principled layer selection as a starting configuration. At 7--8B, HS probes Pareto-dominate text probes, robust across 5 seeds (precision std ${<}8$pp); at 32B ($n{=}19$--$20$), higher variance (R1-32B std $= 12.8$pp) warrants sample-limited interpretation (\cref{sec:32b-analysis}). Safe-trace FPR of 39--52\% and the 85.5\% oracle gap (\cref{sec:oracle}) confirm that current probes characterize the commitment phenomenon rather than provide operational detection. PCA capacity control, control task selectivity, and position residualization (HS retains +3.7 to +6.9pp more non-positional signal than text; \cref{app:position_residual}) provide converging evidence that the HS advantage reflects genuine safety representations; direct erasure methods (LEACE; \citealp{belrose2023leace}) remain untested.
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a06490bb-fa41-417a-9a34-03896049795b",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "ffe56457-5886-4239-ae15-ed9fa1929404",
  "sourceToolAssistantUUID": "a06490bb-fa41-417a-9a34-03896049795b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T13:48:53.669Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011XZt3Ax7UKiyGkparfvq65`</summary>

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
  "parentUuid": "ffe56457-5886-4239-ae15-ed9fa1929404",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA95ATqPbNQsVfzmr1YQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21048b64-e7ac-479e-ab4a-3fe7259d0b93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSb8qwZ3ZSsxspA4SNkB4S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13631,
      "cache_read_input_tokens": 35060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13631,
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

_source line 28 · 2026-05-18T13:48:53.676Z_

<details><summary>↩ Tool result · `toolu_011XZt3Ax7UKiyGkparfvq65`</summary>

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
  "parentUuid": "21048b64-e7ac-479e-ab4a-3fe7259d0b93",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "c856828c-e6c0-41bc-aacd-d63c33d442e5",
  "sourceToolAssistantUUID": "21048b64-e7ac-479e-ab4a-3fe7259d0b93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-18T13:48:57.454Z_



Now let me search for the key papers to analyze their writing strategies.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c856828c-e6c0-41bc-aacd-d63c33d442e5",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA95i76UEAYHKkWUEuAU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "516d3c25-449b-4cad-9df4-5b2a826874b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TndHRkur5rAFSvG2FycnB4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1615,
      "cache_read_input_tokens": 48691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1615,
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

_source line 30 · 2026-05-18T13:48:58.410Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013QEHgfmQxNpGoB99tJDTKA`</summary>

```json
{
  "query": "Hewitt Manning 2019 \"structural probe\" finding syntax word representations narrative framing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "516d3c25-449b-4cad-9df4-5b2a826874b8",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA95i76UEAYHKkWUEuAU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d046419f-f89e-4832-bb6e-af9bbf3c2daa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TndHRkur5rAFSvG2FycnB4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1615,
      "cache_read_input_tokens": 48691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1615,
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

_source line 31 · 2026-05-18T13:48:58.875Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DyGsKq7QBrfpBJXmZPcJor`</summary>

```json
{
  "query": "Belinkov 2022 \"probing classifiers\" survey probing methodology framing contribution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d046419f-f89e-4832-bb6e-af9bbf3c2daa",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA95i76UEAYHKkWUEuAU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5347b229-6ba1-48f6-8663-4e80c575eb84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TndHRkur5rAFSvG2FycnB4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1615,
      "cache_read_input_tokens": 48691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1615,
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

_source line 32 · 2026-05-18T13:48:59.891Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018HyRNqWbaawy52GSUQUojy`</summary>

```json
{
  "query": "Burns et al 2023 \"Discovering Latent Knowledge\" CCS paper abstract introduction framing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5347b229-6ba1-48f6-8663-4e80c575eb84",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA95i76UEAYHKkWUEuAU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "099530f9-5f80-4021-abf9-ed9729056541",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TndHRkur5rAFSvG2FycnB4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1615,
      "cache_read_input_tokens": 48691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1615,
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

_source line 33 · 2026-05-18T13:49:00.610Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TMATo9ca76DguxyA4UBnba`</summary>

```json
{
  "query": "Azaria Mitchell 2023 \"Internal State LLM Knows When Lying\" paper framing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "099530f9-5f80-4021-abf9-ed9729056541",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA95i76UEAYHKkWUEuAU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d828f651-230d-4a27-9ea0-89579256f01b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TndHRkur5rAFSvG2FycnB4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1615,
      "cache_read_input_tokens": 48691,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1615
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 254,
          "cache_read_input_tokens": 48691,
          "cache_creation_input_tokens": 1615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1615,
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

_source line 34 · 2026-05-18T13:49:02.532Z_

<details><summary>↩ Tool result · `toolu_013QEHgfmQxNpGoB99tJDTKA`</summary>

```text
Web search results for query: "Hewitt Manning 2019 "structural probe" finding syntax word representations narrative framing"

Links: [{"title":"A Structural Probe for Finding Syntax in Word Representations - ACL Anthology","url":"https://aclanthology.org/N19-1419/"},{"title":"A Structural Probe for Finding Syntax in Word Representations","url":"https://nlp.stanford.edu/pubs/hewitt2019structural.pdf"},{"title":"GitHub - john-hewitt/structural-probes: Codebase for testing whether hidden states of neural networks encode discrete structures. · GitHub","url":"https://github.com/john-hewitt/structural-probes"},{"title":"[PDF] A Structural Probe for Finding Syntax in Word Representations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Structural-Probe-for-Finding-Syntax-in-Word-Hewitt-Manning/455a8838cde44f288d456d01c76ede95b56dc675"},{"title":"A Structural Probe for Finding Syntax in Word ...","url":"https://www.cs.columbia.edu/~johnhew/public/hewitt2019structural_slides.pdf"},{"title":"A Structural Probe for Finding Syntax in Word Representations John Hewitt","url":"https://www-nlp.stanford.edu/pubs/hewitt2019structural.pdf"},{"title":"Finding Syntax with Structural Probes · John Hewitt","url":"https://www.cs.columbia.edu/~johnhew//structural-probe.html"},{"title":"A Structural Probe for Finding Syntax in Word Representations - Ethan Kim","url":"https://ethankim00.github.io/paper_review/AStructuralProbeforFindingSyntaxinWordRepresentations/"},{"title":"A Structural Probe for Finding Syntax in Word Representations","url":"https://bibbase.org/network/publication/hewitt-manning-astructuralprobeforfindingsyntaxinwordrepresentations-2019"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=A+structural+probe+for+finding+syntax+in+word+representations&amp=&author=J.+Hewitt&amp=&author=C.+D.+Manning&amp=&publication_year=2019&amp=&pages=4129-4138"}]

I found the paper! Here's what the search revealed:

## Hewitt & Manning 2019: A Structural Probe for Finding Syntax in Word Representations

The paper proposes a structural probe that evaluates whether syntax trees are embedded in a linear transformation of a neural network's word representation space. The probe identifies a linear transformation under which squared L2 distance encodes the distance between words in the parse tree, and one in which squared L2 norm encodes depth in the parse tree.

The researchers show that such transformations exist for both ELMo and BERT but not in baselines, providing evidence that entire syntax trees are embedded implicitly in deep models' vector geometry.

The method finds tree structures in these vector spaces and shows the surprising extent to which ELMo and BERT encode human-like parse trees.

The paper was published at NAACL 2019 (short papers) and has become influential in understanding how neural language models implicitly encode syntactic information in their learned representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d046419f-f89e-4832-bb6e-af9bbf3c2daa",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "228ee9bb-f680-4e7b-8251-7fa0b68eb56b",
  "sourceToolAssistantUUID": "d046419f-f89e-4832-bb6e-af9bbf3c2daa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-18T13:49:04.869Z_

<details><summary>↩ Tool result · `toolu_01DyGsKq7QBrfpBJXmZPcJor`</summary>

```text
Web search results for query: "Belinkov 2022 "probing classifiers" survey probing methodology framing contribution"

Links: [{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - ACL Anthology","url":"https://aclanthology.org/2022.cl-1.7/"},{"title":"(PDF) Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://www.researchgate.net/publication/355072709_Probing_Classifiers_Promises_Shortcomings_and_Advances"},{"title":"[2102.12452] Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://arxiv.org/abs/2102.12452"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://aclanthology.org/2022.cl-1.7.pdf"},{"title":"Yonatan Belinkov | publications","url":"https://belinkov.com/publications/publicationstype/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and"},{"title":"[PDF] Probing Classifiers: Promises, Shortcomings, and Advances | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Probing-Classifiers:-Promises,-Shortcomings,-and-Belinkov/3dcfa05a1c162e6cab927c5b08d0444f7b6691f4"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/article/view/1936"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"@article{belinkov-2022-probing,","url":"https://aclanthology.org/2022.cl-1.7.bib"}]

Based on the search results, here's information about Belinkov's 2022 paper on probing classifiers:

## Overview

Probing classifiers have emerged as one of the prominent methodologies for interpreting and analyzing deep neural network models of natural language processing. The basic idea is simple—a classifier is trained to predict some linguistic property from a model's representations—and has been used to examine a wide variety of models and properties.

## The Paper's Contribution

This squib critically reviews the probing classifiers framework, highlighting their promises, shortcomings, and advances. Recent studies have demonstrated various methodological limitations of this approach.

## Publication Details

The article was published in Computational Linguistics, 48(1):207–219 in March 2022.

## Probing Methodology Framework

The paper frames probing classifiers as involving multiple components and design choices. The probing classifiers framework is composed of multiple concepts and components. The choice of each such component, and the interactions between them, lead to non-trivial questions regarding the design and implementation of any probing classifier experiment.

## Key Methodological Insight

An important distinction the paper makes concerns probe complexity: A linear probing classifier is thought to reveal features that are used by the original model, while a more complex probe "bears the risk that the classifier infers features that are not actually used by the network".


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5347b229-6ba1-48f6-8663-4e80c575eb84",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "131a33ea-d169-48fe-91ef-88b9db54d862",
  "sourceToolAssistantUUID": "5347b229-6ba1-48f6-8663-4e80c575eb84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T13:49:07.497Z_

<details><summary>↩ Tool result · `toolu_018HyRNqWbaawy52GSUQUojy`</summary>

```text
Web search results for query: "Burns et al 2023 "Discovering Latent Knowledge" CCS paper abstract introduction framing"

Links: [{"title":"[2212.03827] Discovering Latent Knowledge in Language Models Without Supervision","url":"https://arxiv.org/abs/2212.03827"},{"title":"Article Review: Discovering Latent Knowledge (Burns, Ye, et al)","url":"https://aizi.substack.com/p/article-review-discovering-latent"},{"title":"Discovering Latent Knowledge (Burns, Ye, et al)","url":"https://www.lesswrong.com/posts/WtKGLJQfjCWTm7tFK/article-review-discovering-latent-knowledge-burns-ye-et-al"},{"title":"How \"Discovering Latent Knowledge in Language Models ...","url":"https://www.lesswrong.com/posts/L4anhrxjv8j2yRKKp/how-discovering-latent-knowledge-in-language-models-without"},{"title":"Discovering Latent Knowledge in Language Models Without Supervision | Request PDF","url":"https://www.researchgate.net/publication/366092688_Discovering_Latent_Knowledge_in_Language_Models_Without_Supervision"},{"title":"Discovering Latent Knowledge in Language Models Without Supervision","url":"https://samuelalbanie.substack.com/p/discovering-latent-knowledge-in-language"},{"title":"My Reservations about Discovering Latent Knowledge (Burns, Ye, et al) - LessWrong 2.0 viewer","url":"https://www.greaterwrong.com/posts/C53REQuzSk3TTfqgT/my-reservations-about-discovering-latent-knowledge-burns-ye"},{"title":"DISCOVERING LATENT KNOWLEDGE IN LANGUAGE MODELS WITHOUT SUPERVISION","url":"https://openreview.net/pdf?id=ETKGuby0hcs"},{"title":"GitHub - collin-burns/discovering_latent_knowledge · GitHub","url":"https://github.com/collin-burns/discovering_latent_knowledge"},{"title":"A new AI lie detector reveals their “inner thoughts”","url":"https://www.freethink.com/robots-ai/ai-lie-detector"}]

Based on the search results, here is the abstract and introduction framing of the Burns et al. 2023 paper "Discovering Latent Knowledge in Language Models Without Supervision":

## Abstract

Existing techniques for training language models can be misaligned with the truth: if we train models with imitation learning, they may reproduce errors that humans make; if we train them to generate text that humans rate highly, they may output errors that human evaluators can't detect. The authors propose circumventing this issue by directly finding latent knowledge inside the internal activations of a language model in a purely unsupervised way. Specifically, they introduce a method for accurately answering yes-no questions given only unlabeled model activations. It works by finding a direction in activation space that satisfies logical consistency properties, such as that a statement and its negation have opposite truth values. They show that despite using no supervision and no model outputs, their method can recover diverse knowledge represented in large language models: across 6 models and 10 question-answering datasets, it outperforms zero-shot accuracy by 4% on average.

## Key Framing

The paper frames the core problem around a fundamental challenge: standard training approaches can be misaligned with truth, whether through imitation learning reproducing human errors or through reinforcement learning from human feedback capturing errors that evaluators cannot detect. The proposed solution leverages a method called Contrast-Consistent Search (CCS), which learns a linear projection of the hidden states that is consistent across negations.

The paper was published at ICLR 2023, and it represents a foundational contribution to the problem of eliciting latent knowledge from language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "099530f9-5f80-4021-abf9-ed9729056541",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "623a2067-a506-4622-a68d-0ea1e2b875b7",
  "sourceToolAssistantUUID": "099530f9-5f80-4021-abf9-ed9729056541",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-18T13:49:07.620Z_

<details><summary>↩ Tool result · `toolu_01TMATo9ca76DguxyA4UBnba`</summary>

```text
Web search results for query: "Azaria Mitchell 2023 "Internal State LLM Knows When Lying" paper framing"

Links: [{"title":"[2304.13734] The Internal State of an LLM Knows When It's Lying","url":"https://arxiv.org/abs/2304.13734"},{"title":"The Internal State of an LLM Knows When It’s Lying - ACL Anthology","url":"https://aclanthology.org/2023.findings-emnlp.68/"},{"title":"Paper page - The Internal State of an LLM Knows When its Lying","url":"https://huggingface.co/papers/2304.13734"},{"title":"GitHub - sisinflab/HidingInTheHiddenStates · GitHub","url":"https://github.com/sisinflab/HidingInTheHiddenStates"},{"title":"(PDF) The Internal State of an LLM Knows When its Lying","url":"https://www.researchgate.net/publication/370338601_The_Internal_State_of_an_LLM_Knows_When_its_Lying"},{"title":"The Internal State of an LLM Knows When It's Lying - Ariel University","url":"https://cris.ariel.ac.il/en/publications/the-internal-state-of-an-llm-knows-when-its-lying/"},{"title":"The Internal State of an LLM Knows When It’s Lying | Request PDF","url":"https://www.researchgate.net/publication/376393711_The_Internal_State_of_an_LLM_Knows_When_It's_Lying"},{"title":"The Internal State of an LLM Knows When It's Lying - Israeli Research Community Portal","url":"https://cris.iucc.ac.il/en/publications/the-internal-state-of-an-llm-knows-when-its-lying"},{"title":"The Internal State of an LLM Knows When It's Lying | OpenReview","url":"https://openreview.net/forum?id=y2V6YgLaW7"},{"title":"The Internal State of an LLM Knows When It's Lying","url":"https://aclanthology.org/2023.findings-emnlp.68.pdf"}]

Based on the search results, here's information about the Azaria and Mitchell 2023 paper on internal states of LLMs and truthfulness:

## Paper Framing

The paper addresses a key drawback of Large Language Models: their tendency to generate inaccurate or false information with a confident tone. The core framing is that the LLM's internal state can be used to reveal the truthfulness of statements.

## Key Approach

The researchers trained a classifier that outputs the probability that a statement is truthful, based on the hidden layer activations of the LLM as it reads or generates the statement. This approach applies to both statements provided to the LLM and statements that the LLM itself generates.

## Results and Findings

Experiments demonstrated that given a set of test sentences with half true and half false, the trained classifier achieved an average of 71% to 83% accuracy in labeling which sentences are true versus false, depending on the LLM base model.

While LLM-assigned sentence probability is related to sentence truthfulness, this probability is also dependent on sentence length and word frequency, with the trained classifier providing a more reliable approach to detecting truthfulness.

## Publication

The paper was authored by Amos Azaria and Tom Mitchell and published in December 2023 in the Findings of the Association for Computational Linguistics: EMNLP 2023.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d828f651-230d-4a27-9ea0-89579256f01b",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "d58686a0-3022-43ae-8642-fc814e798d0e",
  "sourceToolAssistantUUID": "d828f651-230d-4a27-9ea0-89579256f01b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-18T13:49:12.403Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PTb26KXVbFV2Brz43CwN1z`</summary>

```json
{
  "query": "Li et al 2024 \"Inference-Time Intervention\" ITI truthful language model hidden states paper framing contribution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d58686a0-3022-43ae-8642-fc814e798d0e",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA96iL28QaoFY45HGpz1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a06e12ef-2497-4b2b-9999-0f5d62324d66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkZM3qAJdzNEDQtsBXwoFs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3920,
      "cache_read_input_tokens": 50306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3920,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 39 · 2026-05-18T13:49:12.880Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ThbMxTKVRm3eR8dxxVTpem`</summary>

```json
{
  "query": "\"sensitivity analysis\" \"methodological finding\" NLP paper framing negative results contribution strategy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a06e12ef-2497-4b2b-9999-0f5d62324d66",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA96iL28QaoFY45HGpz1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c30a6417-9765-4f38-8ecb-5a099678d592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkZM3qAJdzNEDQtsBXwoFs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3920,
      "cache_read_input_tokens": 50306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3920,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 40 · 2026-05-18T13:49:13.811Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018NEBAte8qpJNkHccaNZKgC`</summary>

```json
{
  "query": "probing study \"negative results\" \"mixed results\" NLP paper framing strategy contribution EMNLP ACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c30a6417-9765-4f38-8ecb-5a099678d592",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA96iL28QaoFY45HGpz1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03fc0585-9bcb-4502-858b-74ebbbe20686",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkZM3qAJdzNEDQtsBXwoFs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3920,
      "cache_read_input_tokens": 50306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3920,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 41 · 2026-05-18T13:49:14.263Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A3NLLqJdorAeJ6n9MTmab1`</summary>

```json
{
  "query": "\"researcher degrees of freedom\" NLP probing methodology paper framing contribution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03fc0585-9bcb-4502-858b-74ebbbe20686",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA96iL28QaoFY45HGpz1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42bfeae4-8011-4094-b91b-0436bde25e19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkZM3qAJdzNEDQtsBXwoFs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3920,
      "cache_read_input_tokens": 50306,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3920
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 50306,
          "cache_creation_input_tokens": 3920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3920,
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

_source line 42 · 2026-05-18T13:49:17.459Z_

<details><summary>↩ Tool result · `toolu_01PTb26KXVbFV2Brz43CwN1z`</summary>

```text
Web search results for query: "Li et al 2024 "Inference-Time Intervention" ITI truthful language model hidden states paper framing contribution"

Links: [{"title":"[2306.03341] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://arxiv.org/abs/2306.03341"},{"title":"GitHub - likenneth/honest_llama: Inference-Time Intervention: Eliciting Truthful Answers from a Language Model · GitHub","url":"https://github.com/likenneth/honest_llama"},{"title":"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model | OpenReview","url":"https://openreview.net/forum?id=aLLuYpn83y"},{"title":"[PDF] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Inference-Time-Intervention:-Eliciting-Truthful-a-Li-Patel/405f8f5f1c6df1b3343c812832479aad5180b65f"},{"title":"Inference-time intervention: eliciting truthful answers from ...","url":"https://dl.acm.org/doi/10.5555/3666122.3667919"},{"title":"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://arxiv.org/pdf/2306.03341"},{"title":"Inference-Time Intervention (ITI)","url":"https://www.emergentmind.com/topics/inference-time-intervention-iti"},{"title":"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/81b8390039b7302c909cb769f8b6cd93-Abstract-Conference.html"},{"title":"Inference-Time Intervention: Eliciting Truthful Answers from ...","url":"https://www.lesswrong.com/posts/kuQfnotjkQA4Kkfou/inference-time-intervention-eliciting-truthful-answers-from"},{"title":"(PDF) Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://www.researchgate.net/publication/371347185_Inference-Time_Intervention_Eliciting_Truthful_Answers_from_a_Language_Model"}]

Based on the search results, I found the Li et al 2024 paper on "Inference-Time Intervention" (ITI). Here's what the research presents:

## Core Contribution

The paper introduces Inference-Time Intervention (ITI), a technique designed to enhance the "truthfulness" of large language models (LLMs) by shifting model activations during inference, following a learned set of directions across a limited number of attention heads.

## Key Framing and Findings

The paper's central framing revolves around the idea that LLMs may have an internal representation of the likelihood of something being true, even as they produce falsehoods on the surface. This suggests that models possess latent knowledge of truthfulness that can be accessed through activation engineering.

## Performance Results

On an instruction-finetuned LLaMA called Alpaca, ITI improves its truthfulness from 32.5% to 65.1%. This intervention significantly improves the performance of LLaMA models on the TruthfulQA benchmark.

## Key Contributions

ITI is minimally invasive and computationally inexpensive, with the technique being data efficient: while approaches like RLHF require extensive annotations, ITI locates truthful directions using only few hundred examples. Additionally, the researchers identify a tradeoff between truthfulness and helpfulness and demonstrate how to balance it by tuning the intervention strength.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a06e12ef-2497-4b2b-9999-0f5d62324d66",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "a653c019-8951-4755-96ab-566cd6840e38",
  "sourceToolAssistantUUID": "a06e12ef-2497-4b2b-9999-0f5d62324d66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-18T13:49:19.788Z_

<details><summary>↩ Tool result · `toolu_01ThbMxTKVRm3eR8dxxVTpem`</summary>

```text
Web search results for query: ""sensitivity analysis" "methodological finding" NLP paper framing negative results contribution strategy"

Links: [{"title":"Sensitivity analysis for parametric nonlinear programming: A tutorial","url":"https://arxiv.org/html/2504.15851v1"},{"title":"Sensitivity analysis - Wikipedia","url":"https://en.wikipedia.org/wiki/Sensitivity_analysis"},{"title":"Comprehensive Sensitivity Analysis in NLP Models in PSE Applications Using Space-Filling DOE Strategy | Chemical Engineering Transactions","url":"https://www.cetjournal.it/index.php/cet/article/view/CET1545088"},{"title":"1 Why So Many Published Sensitivity Analyses Are False.","url":"https://arxiv.org/pdf/1711.11359"},{"title":"Workshop on Insights from Negative Results | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-insights-negative-results"},{"title":"The Third Workshop on Insights from Negative Results in NLP | ACL Member Portal","url":"https://www.aclweb.org/portal/content/third-workshop-insights-negative-results-nlp-0"},{"title":"Generalized Sensitivity Analysis of Nonlinear Programs using a Sequence of","url":"https://jaschke.folk.ntnu.no/preprints/2019/Stechlinski_GeneralizedDerivatives/NLP_SequentialQPs_secondsubmission_blackfont.pdf"},{"title":"Workshop on Insights from Negative Results in NLP | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-insights-negative-results-nlp"},{"title":"SENSITIVITY ANALYSIS FOR PARAMETRIC NONLINEAR PROGRAMMING: A TUTORIAL","url":"https://optimization-online.org/wp-content/uploads/2025/04/main-1.pdf"},{"title":"Sensitivity Analysis Ø A few concepts – Impulse-Response","url":"https://sbrg.ucsd.edu/sites/sbrg.ucsd.edu/files/Attachments/Images/classes/convex_presentations/SensitivityAnalysis.pdf"}]

Based on the search results, I found relevant information about negative results in NLP papers. Here's what the search revealed:

## Key Findings on Framing Negative Results in NLP

The NLP research community recognizes that negative results can highlight methodological issues with existing approaches and point out pervasive misunderstandings or bad practices.

### Contribution Strategies for Negative Results Papers

A successful negative results paper can contribute through experiments on instability of previously published results due to hardware or random initializations, and through ablation studies of components in previously proposed models, showing that their contributions differ from initially reported findings.

### Publication Challenges

Publishing negative results is challenging partly because authors must prove something truly doesn't work rather than that results are caused by a bug. Additionally, when revisiting published papers that cannot be reproduced, irreproducibility often comes down to general methodological problems.

### Community Support

The goal of negative results workshops is to stimulate meaningful community-wide discussion of deep issues in NLP methodology.

The search results indicate that sensitivity analyses and methodological rigor are important considerations when framing negative results as contributions to NLP research, though the results don't contain specific papers directly addressing all the combined elements of your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c30a6417-9765-4f38-8ecb-5a099678d592",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "9a48b517-ccd3-4a3a-9f33-84051d05e01c",
  "sourceToolAssistantUUID": "c30a6417-9765-4f38-8ecb-5a099678d592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-18T13:49:21.223Z_

<details><summary>↩ Tool result · `toolu_01A3NLLqJdorAeJ6n9MTmab1`</summary>

```text
Web search results for query: ""researcher degrees of freedom" NLP probing methodology paper framing contribution"

Links: [{"title":"Frontiers | Degrees of Freedom in Planning, Running, Analyzing, and Reporting Psychological Studies: A Checklist to Avoid p-Hacking","url":"https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.01832/full"},{"title":"Designing and Interpreting Probes · John Hewitt","url":"https://nlp.stanford.edu/~johnhew/interpreting-probes.html"},{"title":"Overview of the different researcher degrees of freedom. All in all 48... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Overview-of-the-different-researcher-degrees-of-freedom-All-in-all-48-specifications_fig1_382331101"},{"title":"[2401.11537] Addressing researcher degrees of freedom through minP adjustment","url":"https://arxiv.org/abs/2401.11537"},{"title":"Addressing researcher degrees of freedom through minP adjustment - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11253496/"},{"title":"(DOC) Reporte (1)","url":"https://www.academia.edu/12313893/Reporte_1_"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and"},{"title":"Nonlinear Optimization with Many Degrees of Freedom in Process Engineering | Industrial & Engineering Chemistry Research","url":"https://pubs.acs.org/doi/abs/10.1021/ie0341000"},{"title":"Linguistics Wisdom of NLP Models | Towards Data Science","url":"https://towardsdatascience.com/linguistics-wisdom-of-nlp-models-8c8554bc8c66/"},{"title":"[2305.15130] On Degrees of Freedom in Defining and Testing Natural Language Understanding","url":"https://arxiv.org/abs/2305.15130"}]

Based on the search results, I found relevant information about researcher degrees of freedom in NLP, particularly related to probing methodology and NLU evaluation:

## Key Findings

**General Concept of Researcher Degrees of Freedom:**
When different researchers study the same research question using the same dataset they may obtain different and potentially even conflicting results, because there is often substantial flexibility in researchers' analytical choices, referred to as "researcher degrees of freedom". Combined with selective reporting of the smallest p-value or largest effect, researcher degrees of freedom may lead to an increased rate of false positive and overoptimistic results.

**Application to NLP Probing Methodology:**
Probing classifiers have emerged as one of the prominent methodologies for interpreting and analyzing deep neural network models of natural language processing, where a classifier is trained to predict some linguistic property from a model's representations, but recent studies have demonstrated various methodological limitations of this approach. Critiques have been made about comparative baselines, metrics, the choice of classifier, and the correlational nature of the method.

**Degrees of Freedom in NLU Definition and Testing:**
A position paper identifies two types of researcher degrees of freedom in NLU testing, indicating that an NLU test merely provides inductive evidence rather than an operational definition, allowing stakeholders to arbitrarily define NLU through their objectives.

These findings highlight how researcher degrees of freedom manifest in NLP methodology, from the design of probing classifiers to how NLU itself is conceptualized and evaluated.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42bfeae4-8011-4094-b91b-0436bde25e19",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "51d54d1e-01a3-4449-a21b-df1f2958a526",
  "sourceToolAssistantUUID": "42bfeae4-8011-4094-b91b-0436bde25e19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-18T13:49:26.453Z_

<details><summary>↩ Tool result · `toolu_018NEBAte8qpJNkHccaNZKgC`</summary>

```text
Web search results for query: "probing study "negative results" "mixed results" NLP paper framing strategy contribution EMNLP ACL"

Links: [{"title":"Call For Papers: The Second Workshop on Insights from Negative Results (EMNLP 2021) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-second-workshop-insights-negative-results-emnlp-2021-0"},{"title":"Workshop on Insights from Negative Results | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-insights-negative-results"},{"title":"Workshop on Insights from Negative Results in NLP | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-insights-negative-results-nlp"},{"title":"CFP | Insights 2024","url":"https://insights-workshop.github.io/2021/cfp/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"The Third Workshop on Insights from Negative Results in NLP | ACL Member Portal","url":"https://aclweb.org/portal/content/third-workshop-insights-negative-results-nlp"},{"title":"Insights 2024 | Workshop on Insights from Negative Results in NLP","url":"https://insights-workshop.github.io/"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"4 NLP Papers from Bloomberg Researchers Published in \"Findings of the ACL: EMNLP 2021\" & Conference Workshop | Bloomberg LP","url":"https://www.bloomberg.com/company/stories/4-nlp-papers-from-bloomberg-researchers-published-in-findings-of-acl-emnlp-2021-workshops/"},{"title":"Guest Post: Reproducibility at EMNLP 2020","url":"https://2020.emnlp.org/blog/2020-05-20-reproducibility/"}]

I found search results related to the "Insights from Negative Results" workshop at EMNLP/ACL, which addresses publication challenges with negative results in NLP research. However, the results don't specifically contain papers about probing studies with mixed or negative results and their framing strategies. Let me search more specifically for papers on this topic.

Links: [{"title":"Probing as Quantifying Inductive Bias Alexander Immer∗,","url":"https://arxiv.org/pdf/2110.08388"},{"title":"Topic aware probing: From sentence length prediction to idiom identification how reliant are neural language models on topic? | Natural Language Processing | Cambridge Core","url":"https://resolve.cambridge.org/core/journals/natural-language-processing/article/topic-aware-probing-from-sentence-length-prediction-to-idiom-identification-how-reliant-are-neural-language-models-on-topic/0FFF33B18E284DAB8FE8DCF69A963A30"},{"title":"The Nature of NLP: Analyzing Contributions in NLP Papers - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1224/"},{"title":"Study365","url":"https://www.study365.co.uk/wp-content/uploads/2018/08/NLP-Module-6-Frames-and-Reframing.pdf"},{"title":"The Nature of NLP: Analyzing Contributions in NLP Papers","url":"https://arxiv.org/html/2409.19505v1"},{"title":"Designing and Interpreting Probes · John Hewitt","url":"https://nlp.stanford.edu/~johnhew/interpreting-probes.html"},{"title":"Predicting Fine-Tuning Performance with Probing","url":"https://aclanthology.org/2022.emnlp-main.793.pdf"},{"title":"GitHub - MichiganNLP/Scalable-VLM-Probing: Probe Vision-Language Models · GitHub","url":"https://github.com/MichiganNLP/Scalable-VLM-Probing"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and"},{"title":"Probing Language Models on Their Knowledge Source","url":"https://arxiv.org/html/2410.05817v1"}]

Let me search more specifically for papers on how probing studies handle or frame negative/mixed findings.

No links found.

Based on my web search results, I can provide you with information about the landscape of research on negative results in NLP and probing methodology:

## Key Findings:

**Negative Results in NLP Publishing:**
Publication of negative results is difficult in most fields, but in NLP the problem is exacerbated by the near-universal focus on improvements in benchmarks. This situation implicitly discourages hypothesis-driven research, and it turns creation and fine-tuning of NLP models into art rather than science.

This challenge led to the establishment of a dedicated conference workshop. The Workshop on Insights from Negative Results invites both practical and theoretical unexpected or negative results that have important implications for future research, highlight methodological issues with existing approaches, and/or point out pervasive misunderstandings or bad practices.

**Recent Changes in EMNLP/ACL Standards:**
EMNLP 2026 has a goal of curating a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

**Probing Methodology Concerns:**
Recent studies have demonstrated various methodological limitations of this approach. This squib critically reviews the probing classifiers framework, highlighting their promises, shortcomings, and advances.

While my search found relevant contextual information about negative results in NLP and probing methodology critiques, it did not locate specific papers that explicitly analyze framing strategies for mixed/negative probing results. To find such papers, you may want to search ACL/EMNLP archives directly for papers discussing "probing" with terms like "reframing," "contribution," or methodological critique.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03fc0585-9bcb-4502-858b-74ebbbe20686",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "c0bad819-ed32-4694-8679-ad9a5ba161a6",
  "sourceToolAssistantUUID": "03fc0585-9bcb-4502-858b-74ebbbe20686",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-18T13:49:33.432Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XT2GnqUZyct7gYRy4CXpn6`</summary>

```json
{
  "query": "Hewitt Manning 2019 structural probe abstract introduction \"we find\" \"we show\" framing methodology",
  "allowed_domains": [
    "arxiv.org",
    "aclanthology.org",
    "nlp.stanford.edu"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0bad819-ed32-4694-8679-ad9a5ba161a6",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA986p9mKjm4vVUADtnG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff0d84b4-1d3a-4c71-b661-53d519dfdf9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WKWGHhcTuLg1eAUC9yXmUX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 926,
      "cache_creation_input_tokens": 3778,
      "cache_read_input_tokens": 54226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3778,
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

### Tool call

_source line 47 · 2026-05-18T13:49:34.899Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V1MmtHD6GrAiFVSuop8B4Q`</summary>

```json
{
  "query": "Burns 2023 CCS \"discovering latent knowledge\" introduction \"we propose\" \"our key insight\" narrative structure ICLR",
  "allowed_domains": [
    "arxiv.org",
    "openreview.net"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff0d84b4-1d3a-4c71-b661-53d519dfdf9f",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA986p9mKjm4vVUADtnG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2308b9b1-a2a6-4897-8c44-bf3f1eca9a24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WKWGHhcTuLg1eAUC9yXmUX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 926,
      "cache_creation_input_tokens": 3778,
      "cache_read_input_tokens": 54226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3778,
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

### Tool call

_source line 48 · 2026-05-18T13:49:36.301Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JGbYryidQJwbvP3pocSnGf`</summary>

```json
{
  "query": "Voita Titov 2020 \"information-theoretic probing\" control tasks abstract introduction framing contribution methodology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2308b9b1-a2a6-4897-8c44-bf3f1eca9a24",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA986p9mKjm4vVUADtnG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d97c44ef-c6c5-4cd7-83f2-012cfe69722f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WKWGHhcTuLg1eAUC9yXmUX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 926,
      "cache_creation_input_tokens": 3778,
      "cache_read_input_tokens": 54226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3778,
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

### Tool call

_source line 49 · 2026-05-18T13:49:37.007Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cn9qDCHcUX9dsiMsrwo66j`</summary>

```json
{
  "query": "SafeThink HarmThoughts reasoning model safety detection 2025 paper abstract introduction framing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d97c44ef-c6c5-4cd7-83f2-012cfe69722f",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA986p9mKjm4vVUADtnG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a7ce471-225d-4df6-a80d-340eb27e2116",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WKWGHhcTuLg1eAUC9yXmUX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 926,
      "cache_creation_input_tokens": 3778,
      "cache_read_input_tokens": 54226,
      "output_tokens": 323,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3778
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 926,
          "output_tokens": 323,
          "cache_read_input_tokens": 54226,
          "cache_creation_input_tokens": 3778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3778,
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

_source line 50 · 2026-05-18T13:49:39.529Z_

<details><summary>↩ Tool result · `toolu_01XT2GnqUZyct7gYRy4CXpn6`</summary>

```text
Web search results for query: "Hewitt Manning 2019 structural probe abstract introduction "we find" "we show" framing methodology"

Links: [{"title":"A Structural Probe for Finding Syntax in Word Representations - ACL Anthology","url":"https://aclanthology.org/N19-1419/"},{"title":"A Structural Probe for Finding Syntax in Word Representations","url":"https://nlp.stanford.edu/pubs/hewitt2019structural.pdf"},{"title":"[2105.10185] A Non-Linear Structural Probe","url":"https://arxiv.org/abs/2105.10185"},{"title":"Introducing Orthogonal Constraint in Structural Probes","url":"https://arxiv.org/pdf/2012.15228"},{"title":"UNDERSTANDING LANGUAGE MODELS THROUGH DISCOVERY AND BY DESIGN A DISSERTATION","url":"https://nlp.stanford.edu/~manning/dissertations/HewittThesis-augmented.pdf"},{"title":"[2012.15228] Introducing Orthogonal Constraint in Structural Probes","url":"https://arxiv.org/abs/2012.15228"},{"title":"A Tale of a Probe and a Parser","url":"https://arxiv.org/pdf/2005.01641"},{"title":"[2005.01641] A Tale of a Probe and a Parser","url":"https://arxiv.org/abs/2005.01641"},{"title":"Finding Universal Grammatical Relations in Multilingual BERT","url":"https://arxiv.org/pdf/2005.04511"},{"title":"Finding Syntax with Structural Probes · John Hewitt","url":"https://nlp.stanford.edu/~johnhew/structural-probe.html"}]

I found the Hewitt and Manning (2019) paper on structural probes. Based on the search results, here's information about the paper:

**Title:** A Structural Probe for Finding Syntax in Word Representations

**Authors and Publication:** John Hewitt and Christopher D. Manning, published in 2019 at the Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies.

**Abstract/Introduction Content:**

The work notes that current methods for detecting syntactic knowledge do not test whether syntax trees are represented in their entirety, and proposes a structural probe, which evaluates whether syntax trees are embedded in a linear transformation of a neural network's word representation space.

**Methodology:** The probe identifies a linear transformation under which squared L2 distance encodes the distance between words in the parse tree, and one in which squared L2 norm encodes depth in the parse tree.

**Key Finding:** Using their probe, they show that such transformations exist for both ELMo and BERT but not in baselines, providing evidence that entire syntax trees are embedded implicitly in deep models' vector geometry.

The paper is available at the ACL Anthology and Stanford NLP resources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff0d84b4-1d3a-4c71-b661-53d519dfdf9f",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "e6f2e1b7-997d-4cb2-8e6f-ce4be6b07561",
  "sourceToolAssistantUUID": "ff0d84b4-1d3a-4c71-b661-53d519dfdf9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-18T13:49:41.990Z_

<details><summary>↩ Tool result · `toolu_01JGbYryidQJwbvP3pocSnGf`</summary>

```text
Web search results for query: "Voita Titov 2020 "information-theoretic probing" control tasks abstract introduction framing contribution methodology"

Links: [{"title":"Information-Theoretic Probing with Minimum Description Length - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.14/"},{"title":"Notes on: Information-Theoretic Probing with Minimum Description Length by Voita, E., & Titov, I. (2020) - Hugo Cisneros","url":"https://hugocisneros.com/notes/voitainformationtheoreticprobingminimum2020/"},{"title":"dblp: Elena Voita","url":"https://dblp.org/pid/220/4162.html"},{"title":"[2003.12298] Information-Theoretic Probing with Minimum Description Length","url":"https://arxiv.org/abs/2003.12298"},{"title":"[PDF] Information-Theoretic Probing with Minimum Description Length | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Information-Theoretic-Probing-with-Minimum-Length-Voita-Titov/f4b585c9a79dfce0807b445a09036ea0f9cbcdce"},{"title":"Information-Theoretic Probing with Minimum Description Length | Request PDF","url":"https://www.researchgate.net/publication/347232984_Information-Theoretic_Probing_with_Minimum_Description_Length"},{"title":"Information-Theoretic Probing with Minimum Description Length - ACL Anthology","url":"https://www.aclweb.org/anthology/2020.emnlp-main.14/"},{"title":"[Quick Review] Information-Theoretic Probing with Minimum Description Length","url":"https://liner.com/review/informationtheoretic-probing-with-minimum-description-length"},{"title":"Information-Theoretic Probing with MDL","url":"https://lena-voita.github.io/posts/mdl_probes.html"},{"title":"Information-Theoretic Probing with Minimum Description Length","url":"https://www.researchgate.net/publication/340271374_Information-Theoretic_Probing_with_Minimum_Description_Length"}]

I found the Voita and Titov 2020 paper on information-theoretic probing. Here's a summary of the key sections you requested:

## Abstract and Introduction

The paper addresses how to measure how well pretrained representations encode linguistic properties, noting that it is common to use accuracy of a probe—a classifier trained to predict the property from the representations. Despite widespread adoption of probes, differences in their accuracy fail to adequately reflect differences in representations; for example, they do not substantially favour pretrained representations over randomly initialized ones, and their accuracy can be similar when probing for genuine linguistic labels and probing for random synthetic tasks.

## Contribution and Framing

The authors propose information-theoretic probing with minimum description length (MDL) as an alternative to standard probes, where training a probe to predict labels is recast as teaching it to effectively transmit the data, changing the measure of interest from probe accuracy to the description length of labels given representations.

## Methodology

In addition to probe quality, the description length evaluates "the amount of effort" needed to achieve the quality, which characterizes either the size of a probing model or the amount of data needed to achieve high quality. The authors consider two methods for estimating MDL which can be easily implemented on top of standard probing pipelines: variational coding and online coding, showing that these methods are more informative and stable than standard probes.

The paper was published at EMNLP 2020.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d97c44ef-c6c5-4cd7-83f2-012cfe69722f",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "37017868-3a82-4e69-b08c-62cc06dc5db7",
  "sourceToolAssistantUUID": "d97c44ef-c6c5-4cd7-83f2-012cfe69722f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-18T13:49:42.125Z_

<details><summary>↩ Tool result · `toolu_01V1MmtHD6GrAiFVSuop8B4Q`</summary>

```text
Web search results for query: "Burns 2023 CCS "discovering latent knowledge" introduction "we propose" "our key insight" narrative structure ICLR"

Links: [{"title":"[2212.03827] Discovering Latent Knowledge in Language Models Without Supervision","url":"https://arxiv.org/abs/2212.03827"},{"title":"Discovering Latent Knowledge in Language Models Without Supervision | OpenReview","url":"https://openreview.net/forum?id=ETKGuby0hcs"},{"title":"Published as a conference paper at ICLR 2022 ELICITING LATENT KNOWLEDGE FROM","url":"https://openreview.net/pdf?id=Z1531QeqAQ"},{"title":"2023-12-19 Challenges with unsupervised LLM knowledge discovery","url":"https://arxiv.org/pdf/2312.10029"},{"title":"Discovering Latent Knowledge in Language Models Without Supervision","url":"https://arxiv.org/html/2212.03827v2"},{"title":"DISCOVERING LATENT KNOWLEDGE IN LANGUAGE MODELS WITHOUT SUPERVISION","url":"https://openreview.net/pdf?id=ETKGuby0hcs"},{"title":"Preprint Eliciting Latent Knowledge from “Quirky” Language Models","url":"https://arxiv.org/pdf/2312.01037"},{"title":"[2312.10029] Challenges with unsupervised LLM knowledge discovery","url":"https://ar5iv.labs.arxiv.org/html/2312.10029"},{"title":"Published as a conference paper at COLM 2025","url":"https://arxiv.org/pdf/2404.18865"},{"title":"Eliciting Latent Knowledge from “Quirky” Language Models","url":"https://arxiv.org/html/2312.01037v3"}]

I found the paper! Based on the search results, here's what I found about the Burns 2023 "Discovering Latent Knowledge" paper:

## Paper Details

The paper "Discovering Latent Knowledge in Language Models Without Supervision" was published at ICLR 2023, authored by Collin Burns and co-authors.

## Introduction and Key Proposal

The introduction frames the problem: "Existing techniques for training language models can be misaligned with the truth: if we train models with imitation learning, they may reproduce errors that humans make; if we train them to generate text that humans rate highly, they may output errors that human evaluators can't detect."

The key insight and proposal is stated as: "We propose circumventing this issue by directly finding latent knowledge inside the internal activations of a language model in a purely unsupervised way."

## The Method

The paper introduces "Contrast-Consistent Search (CCS), a method that learns a linear projection of the hidden states that is consistent across negations." It works by finding "a direction in activation space that satisfies logical consistency properties, such as that a statement and its negation have opposite truth values."

## Key Results

The paper demonstrates that "despite its simplicity and despite not having access to any labels or model outputs, CCS can accurately recover knowledge from model representations: evaluated across 6 models and 10 question-answering datasets, CCS outperforms the accuracy of strong zero-shot baselines by 4% on average."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2308b9b1-a2a6-4897-8c44-bf3f1eca9a24",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "065fae16-4367-45dd-a0e7-e31c2c82b866",
  "sourceToolAssistantUUID": "2308b9b1-a2a6-4897-8c44-bf3f1eca9a24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-18T13:49:44.945Z_

<details><summary>↩ Tool result · `toolu_01Cn9qDCHcUX9dsiMsrwo66j`</summary>

```text
Web search results for query: "SafeThink HarmThoughts reasoning model safety detection 2025 paper abstract introduction framing"

Links: [{"title":"Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away","url":"https://itsvaibhav01.github.io/SafeThink-web/"},{"title":"SafeThink: A Key to Safety in Multi-Modal Large Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=ssbwLWPeSy"},{"title":"When Safety Fails Before the Answer: Benchmarking Harmful Behavior Detection in Reasoning Chains","url":"https://arxiv.org/html/2604.19001v1"},{"title":"SafeThink: A Key to Safety in Multi-Modal Large Reasoning ...","url":"https://openreview.net/pdf/43fa3ab6a1125420c0570a063700066ad13f777f.pdf"},{"title":"[Quick Review] THINKSAFE: Self-Generated Safety Alignment for Reasoning Models","url":"https://liner.com/review/thinksafe-selfgenerated-safety-alignment-for-reasoning-models"},{"title":"SafeThinker: Reasoning about Risk to Deepen Safety Beyond Shallow Alignment","url":"https://arxiv.org/pdf/2601.16506"},{"title":"[2601.23143] THINKSAFE: Self-Generated Safety Alignment for Reasoning Models","url":"https://arxiv.org/abs/2601.23143"},{"title":"Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety","url":"https://arxiv.org/pdf/2507.11473"},{"title":"[2505.06538] Think in Safety: Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model","url":"https://arxiv.org/abs/2505.06538"},{"title":"SAFECHAIN: Safety of Language Models with Long Chain- ...","url":"https://aclanthology.org/2025.findings-acl.1197.pdf"}]

Based on the web search results, I found information about both **SafeThink** and **HarmThoughts**, which appear to be two related but distinct research projects focused on safety in reasoning models:

## SafeThink

SafeThink addresses the problem that multi-modal large language models (MLLMs) being fine-tuned with reinforcement learning to improve reasoning experience weakened safety alignment, making models far more vulnerable to jailbreak attacks.

**Framing:** The work traces this vulnerability to a misspecified objective: RL fine-tuning maximizes task accuracy while ignoring safety constraints. SafeThink proposes a lightweight inference-time defense that treats safety recovery as a satisficing constraint rather than a maximization objective, monitoring the evolving reasoning trace with a safety reward model and conditionally injecting an optimized short corrective prefix ("Wait, think safely") only when the safety threshold is violated.

## HarmThoughts

HarmThoughts captures how harm emerges through intermediate reasoning steps, unlike prior safety benchmarks that focus on whether an output is harmful.

**Abstract/Introduction Framing:** HarmThoughts is a benchmark of 1,018 jailbroken reasoning traces from four model families, annotated with 16 sentence-level behavioral labels. Each sentence is annotated using a taxonomy of 16 labels spanning three functional groups—harmful, harmless, and neutral—enabling fine-grained analysis of harm propagation in reasoning.

Both papers address the challenge of safety in advanced reasoning models, with SafeThink focusing on inference-time mitigation and HarmThoughts providing a structured dataset for understanding how harmful behavior develops within reasoning chains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a7ce471-225d-4df6-a80d-340eb27e2116",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "bede4d01-04ae-4e41-828f-68ea909b54c8",
  "sourceToolAssistantUUID": "8a7ce471-225d-4df6-a80d-340eb27e2116",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-18T13:49:49.199Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014TL19nrsJsuAghMWAf2dC1`</summary>

```json
{
  "query": "Hewitt Manning 2019 \"control tasks\" probing designing interpreting probes blog post methodology",
  "allowed_domains": [
    "nlp.stanford.edu"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bede4d01-04ae-4e41-828f-68ea909b54c8",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA99TuBtW8DmqDvPCFQf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8ac8eff-71ad-4452-acf1-c2ab7c4b2d9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M7JJUaEVLxy4mNGdBQMyit",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4650,
      "cache_read_input_tokens": 58004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4650,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 55 · 2026-05-18T13:49:50.203Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VACuTwzLkMwqCwqFqo2bmk`</summary>

```json
{
  "query": "\"characterization study\" \"empirical study\" machine learning NLP paper framing mixed results contribution strategy top venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8ac8eff-71ad-4452-acf1-c2ab7c4b2d9e",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA99TuBtW8DmqDvPCFQf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4321f170-f276-4d5f-b05c-18e58ce9c7ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M7JJUaEVLxy4mNGdBQMyit",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4650,
      "cache_read_input_tokens": 58004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4650,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 56 · 2026-05-18T13:49:50.611Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0114F6QNQ35Rri1gGweD1B4o`</summary>

```json
{
  "query": "Conneau et al 2018 \"probing sentence embeddings\" abstract introduction framing contribution what linguistic knowledge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4321f170-f276-4d5f-b05c-18e58ce9c7ed",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA99TuBtW8DmqDvPCFQf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d8d4b5e-2604-47d5-9ede-058bc001198c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M7JJUaEVLxy4mNGdBQMyit",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4650,
      "cache_read_input_tokens": 58004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4650,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 57 · 2026-05-18T13:49:51.464Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EAyapMbMv6WLvnJ1WciuNe`</summary>

```json
{
  "query": "Zou 2023 \"representation engineering\" RepE abstract introduction contribution framing hidden states"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d8d4b5e-2604-47d5-9ede-058bc001198c",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA99TuBtW8DmqDvPCFQf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7be6360a-470e-4af8-ae83-d518349fa7a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M7JJUaEVLxy4mNGdBQMyit",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4650,
      "cache_read_input_tokens": 58004,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4650
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 58004,
          "cache_creation_input_tokens": 4650,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4650,
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

_source line 58 · 2026-05-18T13:49:55.209Z_

<details><summary>↩ Tool result · `toolu_014TL19nrsJsuAghMWAf2dC1`</summary>

```text
Web search results for query: "Hewitt Manning 2019 "control tasks" probing designing interpreting probes blog post methodology"

Links: [{"title":"Designing and Interpreting Probes with Control Tasks John Hewitt","url":"https://nlp.stanford.edu/pubs/hewitt2019control.pdf"},{"title":"Designing and Interpreting Probes · John Hewitt","url":"https://nlp.stanford.edu/~johnhew/interpreting-probes.html"},{"title":"UNDERSTANDING LANGUAGE MODELS THROUGH DISCOVERY AND BY DESIGN A DISSERTATION","url":"https://nlp.stanford.edu/~manning/dissertations/HewittThesis-augmented.pdf"},{"title":"A Structural Probe for Finding Syntax in Word Representations","url":"https://nlp.stanford.edu/pubs/hewitt2019structural.pdf"},{"title":"Finding Syntax with Structural Probes · John Hewitt","url":"https://nlp.stanford.edu/~johnhew/structural-probe.html"},{"title":"John Hewitt · Language & Machine Learning - Columbia CS","url":"https://nlp.stanford.edu/~johnhew/"},{"title":"Conditional Probing and Usable Information · John Hewitt","url":"https://nlp.stanford.edu/~johnhew/conditional-probing.html"},{"title":"Redirecting...","url":"https://nlp.stanford.edu/~johnhew/structural-probe.html?amp="},{"title":"2 The term vocabulary and postings - lists - Stanford NLP Group","url":"https://nlp.stanford.edu/IR-book/pdf/02voc.pdf"},{"title":"Online edition (c) 2009 Cambridge UP","url":"https://nlp.stanford.edu/IR-book/pdf/11prob.pdf"}]

I found relevant results for your query. Here's what I found:

The search retrieved a paper titled "Designing and Interpreting Probes with Control Tasks" by John Hewitt, along with related academic materials. This work (Hewitt and Manning 2019) showed that neural language models—particularly BERT—learn to encode a simple representation of linguistic syntax, with most of the interest being in the methodological development.

Around 2019, NLP scientists running probing studies were using expressive mappings like multiple-layer neural networks, and Hewitt and Liang (2019) provided evidence that such methods could lead researchers astray. At its core was a fake task—basically memorizing which randomly chosen categories each word in a vocabulary belongs to—which could be reasonably convincing via a held-out test set that a representation has knowledge it definitely doesn't have.

The primary sources include the academic paper from Stanford NLP (available as a PDF) and materials from Hewitt's dissertation, which discusses the methodological contributions around designing and interpreting probes with control tasks as a way to validate what properties neural language models have actually learned.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8ac8eff-71ad-4452-acf1-c2ab7c4b2d9e",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "ab3f9fc4-3027-4de8-bd2b-b638ff3d683d",
  "sourceToolAssistantUUID": "a8ac8eff-71ad-4452-acf1-c2ab7c4b2d9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-18T13:49:57.283Z_

<details><summary>↩ Tool result · `toolu_0114F6QNQ35Rri1gGweD1B4o`</summary>

```text
Web search results for query: "Conneau et al 2018 "probing sentence embeddings" abstract introduction framing contribution what linguistic knowledge"

Links: [{"title":"What you can cram into a single $&!#* vector: Probing sentence embeddings for linguistic properties - ACL Anthology","url":"https://aclanthology.org/P18-1198/"},{"title":"SentEval/data/probing/README.md at main · facebookresearch/SentEval","url":"https://github.com/facebookresearch/SentEval/blob/main/data/probing/README.md"},{"title":"[1805.01070] What you can cram into a single vector: Probing sentence embeddings for linguistic properties","url":"https://arxiv.org/abs/1805.01070"},{"title":"READING NOTES: Sentence embeddings for linguistic properties (Conneau et al., 2018) - WENYAN LI","url":"https://lyan62.github.io/papernotes-sentence-embeddings-for-linguistic-properties/"},{"title":"What you can cram into a single $&!#* vector: Probing sentence embeddings for linguistic properties | Request PDF","url":"https://www.researchgate.net/publication/334115550_What_you_can_cram_into_a_single_vector_Probing_sentence_embeddings_for_linguistic_properties"},{"title":"Tracking linguistic information in transformer-based sentence embeddings through targeted sparsification","url":"https://arxiv.org/html/2407.18119"},{"title":"Probing sentence embeddings for linguistic properties","url":"https://loicbarrault.github.io/papers/conneau_acl2018.pdf"},{"title":"A Comprehensive Survey of Sentence Representations: From the BERT Epoch to the ChatGPT Era and Beyond","url":"https://arxiv.org/html/2305.12641v3"},{"title":"GitHub - facebookresearch/SentEval: A python tool for evaluating the quality of sentence embeddings. · GitHub","url":"https://github.com/facebookresearch/SentEval"},{"title":"[1805.01070] What you can cram into a single $&!#⁢* vector: Probing sentence embeddings for linguistic properties","url":"https://ar5iv.labs.arxiv.org/html/1805.01070"}]

Based on the search results, here's information about the Conneau et al. 2018 paper on probing sentence embeddings:

## Abstract and Framing

The paper states that although much effort has been devoted to training high-quality sentence embeddings, there is still poor understanding of what they are capturing. "Downstream" tasks, often based on sentence classification, are commonly used to evaluate sentence representations, but the complexity of these tasks makes it difficult to infer what kind of information is present in the representations.

## Contribution and Methodology

The key contribution is introducing 10 probing tasks designed to capture simple linguistic features of sentences, which are used to study embeddings generated by three different encoders trained in eight distinct ways, uncovering properties of both encoders and training methods.

## Linguistic Knowledge Examined

The paper probes for various linguistic properties. The study explored linguistic attributes including part-of-speech tags, verb tense, and named entity recognition. Based on the detailed task descriptions in the search results, the 10 probing tasks include sentence length, word recovery, bigram shift detection, top constituent structure, tense classification, subject number agreement, and semantic properties, among others.

The paper's title references Ray Mooney's skepticism about compressing sentence meaning into a vector, and the work systematically investigates what linguistic knowledge is actually captured in sentence embeddings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d8d4b5e-2604-47d5-9ede-058bc001198c",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "fe44ecdc-d338-4790-83b5-42a7f6ae103b",
  "sourceToolAssistantUUID": "1d8d4b5e-2604-47d5-9ede-058bc001198c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-18T13:49:58.210Z_

<details><summary>↩ Tool result · `toolu_01EAyapMbMv6WLvnJ1WciuNe`</summary>

```text
Web search results for query: "Zou 2023 "representation engineering" RepE abstract introduction contribution framing hidden states"

Links: [{"title":"[2310.01405] Representation Engineering: A Top-Down Approach to AI Transparency","url":"https://arxiv.org/abs/2310.01405"},{"title":"GitHub - andyzoujm/representation-engineering: Representation Engineering: A Top-Down Approach to AI Transparency · GitHub","url":"https://github.com/andyzoujm/representation-engineering"},{"title":"Representation Engineering (RepE)","url":"https://www.emergentmind.com/topics/representation-engineering-repe"},{"title":"GitHub - chrisliu298/awesome-representation-engineering: A resource repository for representation engineering in large language models · GitHub","url":"https://github.com/chrisliu298/awesome-representation-engineering"},{"title":"[PDF] Representation Engineering: A Top-Down Approach to AI Transparency | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Representation-Engineering:-A-Top-Down-Approach-to-Zou-Phan/aac3469581061cd5b46440c3eeca91c385d54ccf"},{"title":"Turning Knobs Inside LLMs: A Review of Representation Engineering — A Top-Down Approach to AI Transparency (2023) | by GlitchQ | Glitch Q | Medium","url":"https://medium.com/glitch-q/turning-knobs-inside-llms-a-review-of-representation-engineering-a-top-down-approach-to-ai-f850a0be7ad5"},{"title":"Representation Engineering: A Top-Down Approach to AI Transparency | Montreal AI Ethics Institute","url":"https://montrealethics.ai/representation-engineering-a-top-down-approach-to-ai-transparency/"},{"title":"Representation Engineering in AI Systems","url":"https://www.emergentmind.com/topics/representation-engineering"},{"title":"Representation Engineering — AI Safety 東京","url":"https://aisafety.tokyo/benkyoukai/representation-engineering"},{"title":"Representation Engineering: A Top-Down Approach to AI Transparency","url":"https://arxiv.org/html/2310.01405v4"}]

Based on the search results, here's information about the Zou 2023 paper on Representation Engineering (RepE):

## Abstract and Introduction

The paper identifies and characterizes representation engineering (RepE), an approach to enhancing the transparency of AI systems that draws on insights from cognitive neuroscience.

## Key Contribution to Framing

RepE places population-level representations, rather than neurons or circuits, at the center of analysis, equipping us with novel methods for monitoring and manipulating high-level cognitive phenomena in deep neural networks (DNNs).

## Core Contributions

The paper provides baselines and an initial analysis of RepE techniques, showing that they offer simple yet effective solutions for improving our understanding and control of large language models. Additionally, the methods can provide traction on a wide range of safety-relevant problems, including honesty, harmlessness, power-seeking, and more, demonstrating the promise of top-down transparency research.

## Hidden States and Representation Analysis

Representation reading seeks to locate emergent representations for high-level concepts and functions within a network, and building on the insights gained from Representation Reading, Representation Control seeks to modify or control the internal representations of concepts and functions.

The paper was submitted on 2 Oct 2023 and proposes foundational techniques for working with neural network hidden states to understand and control high-level cognitive phenomena.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7be6360a-470e-4af8-ae83-d518349fa7a4",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "3c04b1cd-2099-43f2-b83b-6a8f524f80c9",
  "sourceToolAssistantUUID": "7be6360a-470e-4af8-ae83-d518349fa7a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-18T13:49:58.675Z_

<details><summary>↩ Tool result · `toolu_01VACuTwzLkMwqCwqFqo2bmk`</summary>

```text
Web search results for query: ""characterization study" "empirical study" machine learning NLP paper framing mixed results contribution strategy top venue"

Links: [{"title":"The Nature of NLP: Analyzing Contributions in NLP Papers","url":"https://arxiv.org/html/2409.19505v1"},{"title":"Natural Language Processing and Machine Learning Methods to Characterize Unstructured Patient-Reported Outcomes: Validation Study - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC8600437/"},{"title":"Use of deep learning-based NLP models for full-text data elements extraction for systematic literature review tasks | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-03979-5"},{"title":"Announcing the NeurIPS 2025 Best Paper Awards – NeurIPS Blog","url":"https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/"},{"title":"Empowering text classification with NLP and explainable AI for enhanced interpretability | Journal of Electrical Systems and Information Technology | Springer Nature Link","url":"https://link.springer.com/article/10.1186/s43067-025-00273-2"},{"title":"Efficient Methods for Natural Language Processing: A Survey | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00577/116725/Efficient-Methods-for-Natural-Language-Processing"},{"title":"An Empirical Study of Testing Machine Learning in the Wild | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3680463"},{"title":"Natural language processing: state of the art, current trends and challenges | Multimedia Tools and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11042-022-13428-4"},{"title":"NLP Reproducibility For All: Understanding Experiences of ...","url":"https://aclanthology.org/2023.acl-long.568.pdf"},{"title":"Journal of Medical Internet Research - Machine Learning and Natural Language Processing in Mental Health: Systematic Review","url":"https://www.jmir.org/2021/5/e15708/"}]

Based on my search results, I found relevant information about how NLP and machine learning research is framed in academic venues. Here are some key findings:

## NLP Contributions and Paper Framing

Researchers have created a dataset of nearly 2,000 research paper abstracts expertly annotated to identify scientific contributions and classify their types according to a taxonomy. This systematic analysis reveals important patterns in how NLP research is structured and presented.

## Venue Differences and Contributions

The EMNLP conference, originally established to focus on empirical findings, has shown growing similarity to ACL in terms of contribution types. Over time, a common publication norm has emerged across conferences, leading to a more institutionalized standard in NLP research.

## Methodological Trends

Research focusing on language and people has waned since the early nineties, while contributions to developing methods, mainly using machine learning tools, have risen. However, recently, post-2020, there has been a revived interest in sociolinguistics and the application of NLP within social sciences, suggesting a broadening of research focus.

## Handling Mixed Results

For papers with mixed or complex results, a principled way to characterize trade-offs is to identify Pareto-optimal solutions (those for which no other system reaches better or equal task performance with lower resource consumption), and as there may be several Pareto-optimal solutions, final choice depends on the application context, with both a small, average-quality model and a large, higher-quality model potentially being optimal. Advancing NLP by pushing Pareto barriers is an established practice.

This framing strategy allows papers with mixed empirical results to still make meaningful contributions by demonstrating improvements in specific dimensions or contexts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4321f170-f276-4d5f-b05c-18e58ce9c7ed",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "3faec2fe-f9b3-48d7-b5dc-4de34963f7ca",
  "sourceToolAssistantUUID": "4321f170-f276-4d5f-b05c-18e58ce9c7ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-18T13:50:02.026Z_

Now let me search for a few more specific examples of how papers handle model-dependent or conditional results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3faec2fe-f9b3-48d7-b5dc-4de34963f7ca",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA9AUn3r88KTYEEwYwaE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2964c255-ee85-4351-afdc-3c2f56c13138",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tw71jJWxjVqbLS2znxgWvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1808,
      "cache_creation_input_tokens": 1985,
      "cache_read_input_tokens": 62654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1985,
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

_source line 63 · 2026-05-18T13:50:02.974Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015nE1suFHXBbxEzDh6ww1jA`</summary>

```json
{
  "query": "\"works on some models but not others\" \"model-dependent\" probing interpretability paper framing handling inconsistent results across models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2964c255-ee85-4351-afdc-3c2f56c13138",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA9AUn3r88KTYEEwYwaE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2713e36e-8118-4ee3-a253-1e89bddd929e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tw71jJWxjVqbLS2znxgWvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1808,
      "cache_creation_input_tokens": 1985,
      "cache_read_input_tokens": 62654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1985,
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

_source line 64 · 2026-05-18T13:50:03.741Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CTBuoxHgCiu625yP41ZZG2`</summary>

```json
{
  "query": "Hewitt Liang 2019 \"designing interpreting probes\" control tasks EMNLP abstract contribution framing methodology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2713e36e-8118-4ee3-a253-1e89bddd929e",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA9AUn3r88KTYEEwYwaE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59af639e-fd19-4ba7-9ff6-718162914403",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tw71jJWxjVqbLS2znxgWvb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1808,
      "cache_creation_input_tokens": 1985,
      "cache_read_input_tokens": 62654,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1985
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1808,
          "output_tokens": 163,
          "cache_read_input_tokens": 62654,
          "cache_creation_input_tokens": 1985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1985,
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

_source line 65 · 2026-05-18T13:50:10.291Z_

<details><summary>↩ Tool result · `toolu_015nE1suFHXBbxEzDh6ww1jA`</summary>

```text
Web search results for query: ""works on some models but not others" "model-dependent" probing interpretability paper framing handling inconsistent results across models"

Links: [{"title":"Do We Know What LLMs Don’t Know? A Study of Consistency in Knowledge Probing","url":"https://arxiv.org/html/2505.21701v2"},{"title":"Probing Ranking LLMs: Mechanistic Interpretability in Information Retrieval","url":"https://arxiv.org/html/2410.18527v1"},{"title":"Understanding Mechanistic Interpretability in AI Models | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"},{"title":"Understanding Mechanistic Interpretability in AI Models 8/16/2025 • 40 min read","url":"https://intuitionlabs.ai/pdfs/understanding-mechanistic-interpretability-in-ai-models.pdf"},{"title":"Rethinking Interpretability in the Era of Large Language Models","url":"https://arxiv.org/html/2402.01761v1"},{"title":"Designing an Interpretability-Based Model to Explain the Artificial Intelligence Algorithms in Healthcare - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9319389/"},{"title":"Transparent AI: The Case for Interpretability and Explainability","url":"https://arxiv.org/html/2507.23535v1"},{"title":"Explainability for Large Language Models: A Survey | ACM Transactions on Intelligent Systems and Technology","url":"https://dl.acm.org/doi/10.1145/3639372"},{"title":"Interpretability Methods in Machine Learning: A Brief Survey - Two Sigma","url":"https://www.twosigma.com/articles/interpretability-methods-in-machine-learning-a-brief-survey/"},{"title":"Challenging the Performance-Interpretability Trade-Off: An Evaluation of Interpretable Machine Learning Models | Business & Information Systems Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s12599-024-00922-2"}]

Based on the web search results, I found several papers and resources relevant to your query about probing interpretability and handling inconsistent results across models. Here are the key findings:

## Knowledge Probing Consistency Across Models

The first major result shows that while overall probing performance metrics appear stable, the actual rejection decisions vary considerably across prompts, revealing a key discrepancy in current probing methods. The instability appears to be not due to the model itself, but rather the probe's failure to reliably capture the model's underlying uncertainty.

If probing signals are themselves unstable or inconsistent across variants and architectures, then the rejection behavior becomes inherently unreliable. This is particularly problematic because current refusal mechanisms often rely heavily on the output of the probing methods to decide whether a model "knows" an answer.

## Model-Dependence in Probing Methods

The insights gained from probing are heavily dependent on the dataset used for probing, and if the dataset is not representative of the model's typical input, the results may not accurately reflect the model's general behavior.

## Research Recommendations

Researchers recommend that future work on knowledge probing explicitly consider the consistency of probing methods and routinely report consistency metrics. The papers emphasize the importance of understanding when and why probing methods fail across different models and conditions.

The most relevant paper appears to be "Do We Know What LLMs Don't Know? A Study of Consistency in Knowledge Probing," which directly addresses the inconsistency problem in probing across models and proposes consistency metrics for evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2713e36e-8118-4ee3-a253-1e89bddd929e",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "6adc0d01-1590-424a-a63f-a16eba7da14a",
  "sourceToolAssistantUUID": "2713e36e-8118-4ee3-a253-1e89bddd929e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-18T13:50:11.536Z_

<details><summary>↩ Tool result · `toolu_01CTBuoxHgCiu625yP41ZZG2`</summary>

```text
Web search results for query: "Hewitt Liang 2019 "designing interpreting probes" control tasks EMNLP abstract contribution framing methodology"

Links: [{"title":"Designing and Interpreting Probes · John Hewitt","url":"https://www.cs.columbia.edu/~johnhew/interpreting-probes.html"},{"title":"Designing and Interpreting Probes with Control Tasks - ACL Anthology","url":"https://aclanthology.org/D19-1275/"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://bibbase.org/network/publication/hewitt-liang-designingandinterpretingprobeswithcontroltasks-2019"},{"title":"[1909.03368] Designing and Interpreting Probes with Control Tasks","url":"https://arxiv.org/abs/1909.03368"},{"title":"dblp: John Hewitt","url":"https://dblp.org/pid/205/9025.html"},{"title":"Designing and Interpreting Probes with Control Tasks - ACL Anthology","url":"https://www.aclweb.org/anthology/D19-1275/"},{"title":"Designing and Interpreting Probes with Control Tasks | papers_we_read","url":"https://vlgiitr.github.io/papers_we_read/summaries/control_tasks.html"},{"title":"Designing and Interpreting Probes with Control Tasks. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/1c7c8f6e4720c00cfb0b395c4827d7155"},{"title":"[PDF] Designing and Interpreting Probes with Control Tasks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Designing-and-Interpreting-Probes-with-Control-Hewitt-Liang/199ff73d2f728e997f860b62a2322823d3e3d9e8"},{"title":"Designing and Interpreting Probes with Control Tasks John Hewitt","url":"https://nlp.stanford.edu/pubs/hewitt2019control.pdf"}]

Based on the web search results, here's comprehensive information about the Hewitt & Liang 2019 paper on designing and interpreting probes:

## Paper Overview

The paper "Designing and Interpreting Probes with Control Tasks" is a 2019 EMNLP publication by John Hewitt and Percy Liang.

## Abstract & Core Contribution

The paper addresses probes—supervised models trained to predict properties (like parts-of-speech) from representations (like ELMo)—and asks whether high accuracy means the representations encode linguistic structure or just that the probe has learned the linguistic task.

The key methodological contribution is proposing control tasks, which associate word types with random outputs to complement linguistic tasks. By construction, these tasks can only be learned by the probe itself.

## Methodology

A good probe should be selective, achieving high linguistic task accuracy and low control task accuracy. Selectivity puts linguistic task accuracy in context with the probe's capacity to memorize from word types.

The authors construct control tasks for English part-of-speech tagging and dependency edge prediction, and show that popular probes on ELMo representations are not selective.

## Key Findings

The paper finds that dropout, commonly used to control probe complexity, is ineffective for improving selectivity of MLPs, but other forms of regularization are effective.

While probes on the first layer of ELMo yield slightly better part-of-speech tagging accuracy than the second, probes on the second layer are substantially more selective, which raises the question of which layer better represents parts-of-speech.

The paper received the Best Paper Runner Up Award at EMNLP 2019.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59af639e-fd19-4ba7-9ff6-718162914403",
  "isSidechain": true,
  "promptId": "51aec0ec-c1f3-4044-8610-81e71aa7f83f",
  "agentId": "a2c3ecdd6397fb570",
  "type": "user",
  "uuid": "b881125d-bc06-41e3-abf2-b6e4d6a29480",
  "sourceToolAssistantUUID": "59af639e-fd19-4ba7-9ff6-718162914403",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-18T13:51:17.524Z_

I now have enough material to write the analysis. Let me compile my findings.

---

## 关键论文写作策略分析：面向论文重写的叙事洞察

### 一、"先建立方法论危机，再提出解决框架"的开场策略

最值得借鉴的叙事模式来自 **Hewitt & Liang 2019 (Control Tasks)** 和 **Voita & Titov 2020 (MDL Probing)**。两篇论文的核心贡献都是方法论发现而非新任务/新模型，它们的共同策略是：**开篇直接质疑现有实践的可靠性，将"大家都在做但没人验证"的盲区转化为紧迫问题。**

Hewitt & Liang 的 hook 是：probing accuracy 高是否真的意味着表征编码了语言结构？他们用一个 "control task"（随机标签预测）证明高表达力的 probe 能在完全无意义的任务上取得看似合理的准确率。Voita & Titov 的 hook 更直接：probe accuracy 作为指标本身就是有缺陷的，随机初始化和预训练表征的差异在 accuracy 上几乎无法区分。

**对我们论文的启示**：当前 Introduction 的 hook 是 self-jailbreak 现象本身，这偏向"应用问题"而非"方法论危机"。考虑到我们的主贡献是 layer selection sensitivity，更有效的开场应该是：**"隐藏状态 probing 被广泛用于安全检测，但一个从未被审查的选择——用什么指标选层——可以完全逆转结论。"** 先建立方法论危机感，再引入 self-jailbreak 作为揭示这个问题的测试场景。

### 二、Characterization Study 的贡献定位策略

**Burns et al. 2023 (CCS)** 和 **Conneau et al. 2018 (Sentence Probing)** 提供了两种不同但都有效的定位方式：

Burns 的策略是 **"绕过现有范式"**：现有训练方式（模仿学习、RLHF）都可能与真相不对齐，因此提出直接从内部激活中发现潜在知识。这个 framing 把一个技术贡献（找到一个线性方向）包装成一个范式级洞察（模型内部"知道"的比它"说"的多）。

Conneau 的策略是 **"系统性审计"**：title 本身就是一个问题（"你能塞进一个向量里什么？"），贡献不是提出新方法，而是设计一套诊断工具来回答一个社区关心的问题。10 个 probing task 的设计本身就是贡献。

**对我们论文的启示**：我们的论文更接近 Conneau 的审计模式。当前 framing 试图同时讲"self-jailbreak 检测"和"layer selection 方法论"两个故事，导致主线不够清晰。更有效的定位是：**"我们提供了一套系统性审计框架，用于评估 probing 方法在推理模型安全监控中的可靠性，核心发现是层选择方法论本身是一个被忽视的关键变量。"** HS vs text 和负面结果都服务于这个审计叙事。

### 三、负面/混合结果的价值化策略

分析的 8 篇论文中，处理负面结果最成功的是 **Hewitt & Liang 2019** 和 **Voita & Titov 2020**。它们的共同模式是：**负面结果不是"失败"，而是"发现现有方法的边界条件"。**

Hewitt & Liang 发现 ELMo 第一层的 POS tagging accuracy 略高于第二层，但 selectivity 反过来。他们没有把这当作困惑，而是转化为一个有价值的问题："哪一层才真正代表词性？"——这正好证明了 control task 的必要性。

Voita & Titov 展示 probe accuracy 在预训练和随机表征之间差异极小，这个"负面结果"（accuracy 不能区分）直接构成了 MDL 方法的动机。

**RepE (Zou et al. 2023)** 的策略不同：它承认方法在某些概念上效果好、某些上不好，但通过"population-level representation"的框架统一了这些差异，将不一致性解释为不同概念在表征空间中编码方式的差异，而非方法的失败。

**对我们论文的启示**：当前论文列出 7 种方法失败，但 framing 倾向于"它们不行，所以用我们的"。更有说服力的 framing 是：**每个负面结果揭示了一个关于安全承诺表征性质的具体洞察。** BOCPD/CUSUM 失败 → 承诺是渐进过程而非突变；Mahalanobis 失败 → 判别信号在 PCA 次要成分中；RepE 不一致 → 安全表征是模型特异的，不存在通用方向。将负面结果从"方法 X 不行"转化为"通过方法 X 的失败我们学到了 Y"。

### 四、模型依赖性结果的呈现策略

**Li et al. 2024 (ITI)** 提供了一个有用的参考：ITI 在 truthfulness 和 helpfulness 之间存在 trade-off，效果因模型和干预强度而异。他们的处理方式是 **将不一致性转化为设计空间的维度**：不同模型/设置对应不同的操作点，用户可以根据部署需求选择。这比"方法在所有模型上都有效"更实际。

**Azaria & Mitchell 2023** 在 EMNLP Findings 发表，accuracy 范围 71-83%——明显不是"干净"的结果。他们的 framing 是：**内部状态确实编码了真实性信息，但编码程度取决于模型。** 这个 framing 的关键是把"模型依赖"从"弱点"转化为"发现"。

**对我们论文的启示**：QwQ 和 R1-32B 的检测 profile 完全相反（lead time、coverage、position baseline）。当前 Discussion 已经提到了 training method 作为可能的解释。可以进一步强化：**将跨模型分歧本身作为核心发现之一，而非需要辩解的弱点。** "蒸馏训练和原生推理训练产生质性不同的安全表征几何结构"——这本身就是一个有价值的实证贡献，比"4/4 模型都显著"更有信息量。

### 五、"Researcher Degrees of Freedom"作为贡献框架

心理学领域的 "researcher degrees of freedom" 概念（Simmons et al. 2011）已经被 NLP 社区接受。Hewitt & Liang 的 selectivity 和 Voita & Titov 的 MDL 本质上都在揭示 probing 研究中的 researcher degrees of freedom。但**没有人将"层选择指标"明确框架为 researcher degree of freedom**——这是我们论文的独特定位机会。

当前 Discussion 已经使用了这个术语，但可以更前置。**建议在 Abstract 的第二句话就引入这个概念**，作为连接方法论贡献和经验发现的桥梁："layer selection is an underexamined researcher degree of freedom" 这句话应该出现在 Abstract 而非仅在 Discussion。

### 六、对 Abstract/Introduction/Discussion 重写的具体建议

**Abstract 叙事线调整**：
当前顺序：现象 → HS vs text → layer selection → 负面结果。
建议顺序：方法论危机（probing 被广泛使用但层选择从未被审查）→ 揭示问题的测试场景（self-jailbreak 检测）→ 核心发现（指标选择逆转结论）→ 在正确条件下的经验发现（HS 优势 + 边界条件）。

**Introduction hook 调整**：
当前 hook：self-jailbreak 现象（第 1 段）。
建议 hook：Hidden-state probing 被越来越多用于安全监控，但其结论对一个从未被系统检查的选择——如何选择监控哪一层——高度敏感。用 1-2 句话建立方法论紧迫性，然后引入 self-jailbreak 作为高风险测试场景（"如果在安全攸关的场景中 probing 结论取决于一个任意的方法论选择，这个问题就不能被忽视"）。

**Discussion 的"what we learned from failures"框架**：
为每个负面结果提炼一句"表征性质洞察"，集中在一个小节中呈现，而非散布在 negative results table 的描述中。这将负面结果从"附录级材料"提升为"核心叙事的组成部分"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b881125d-bc06-41e3-abf2-b6e4d6a29480",
  "isSidechain": true,
  "agentId": "a2c3ecdd6397fb570",
  "requestId": "req_011CbA9BRabLpLvRZK7QYAon",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d69ca0fa-c997-4008-b93b-e8484db42971",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "54906428-5b2d-4c42-a329-f968ec1b79dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJxvhWqTewqHLekhvtPJ37",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3940,
      "cache_read_input_tokens": 64639,
      "output_tokens": 2721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3940
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2721,
          "cache_read_input_tokens": 64639,
          "cache_creation_input_tokens": 3940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3940,
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
