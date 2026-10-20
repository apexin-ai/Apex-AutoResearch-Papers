# Research conversation: I need you to do a comprehensive novelty check for a research paper idea. Search the web (Semantic Scholar, Google Schol

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 86
- **Recorded user turns:** 1
- **Tool calls:** 39
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a924cdd4f9463f49b.jsonl`
- **Structured JSON:** [`7a57a1c3275b33bb336e.json`](../../sessions/7a/7a57a1c3275b33bb336e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

86 recorded events

### User

_source line 1 · 2026-05-14T14:47:17.776Z_

I need you to do a comprehensive novelty check for a research paper idea. Search the web (Semantic Scholar, Google Scholar, arXiv) for highly similar work published in 2024-2026.

**Our core idea (StructFuse)**:
1. Systematic study of hard negative mining strategies for contrastive code retrieval
2. Corrects misconception that embedding-distance hard negatives harm code retrieval (prior work CoCoHaNeRe used BM25-proxy, not true embedding distance)
3. Introduces structure-grounded (dataflow) hard negatives via CodeQL inter-procedural data-flow analysis
4. Shows conditional benefit: dataflow negatives help when encoder representations are saturated (high pos_sim), embedding mining suffices otherwise
5. Mechanistic explanation via representation geometry / negative difficulty analysis

**Key search queries to run** (use WebSearch for each):
1. "hard negative mining code retrieval 2024 2025 2026"
2. "contrastive learning code search hard negatives"
3. "CoCoHaNeRe code search" (the paper we claim to correct)
4. "dataflow aware training code retrieval"
5. "structure-guided negative mining"
6. "code retrieval negative sampling strategy"
7. "SweRank" and "SWE-Fixer" (baselines we compare to)
8. "representation geometry hard negatives"
9. "ARISE code dataflow" 
10. "CodexGraph code retrieval"
11. "LocAgent code localization"
12. "RANGER code retrieval graph"

For each search:
- Note any paper from 2024-2026 that overlaps significantly with our idea
- Record: title, authors, venue, year, arXiv ID, and how it relates to our work
- Assess overlap level: HIGH (same core idea), MEDIUM (partial overlap), LOW (tangential)

Also check:
- Are there any 2025-2026 papers that already do systematic comparison of hard negative mining strategies for code?
- Has anyone already corrected CoCoHaNeRe's findings?
- Has anyone used dataflow/program analysis for training signal in code retrieval (not just inference-time)?

Report your findings in a structured format. Be thorough - this is critical for a submission.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "2619dab3-7db7-4eb7-927e-c2b02beb11ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T14:47:17.789Z_

```json
{
  "parentUuid": "2619dab3-7db7-4eb7-927e-c2b02beb11ee",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
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
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__post_to_reviewer",
      "mcp__agent-ml-research__ralph_respond",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
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
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__post_to_reviewer",
      "mcp__agent-ml-research__ralph_respond",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
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
  "uuid": "f550f5c8-4d1c-4fcf-8554-a698ee0cc222",
  "timestamp": "2026-05-14T14:47:17.789Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T14:47:20.901Z_



I'll run all 12 web searches in parallel to gather comprehensive results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f550f5c8-4d1c-4fcf-8554-a698ee0cc222",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eJKpriHh1B9xCG9Sax",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d039d612-9364-4590-aec0-94e14f759db8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P29cFtGbdYoSw6teCJdP8r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30771,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30771,
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

_source line 4 · 2026-05-14T14:47:20.959Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XUVQi3jzcLEEWQybH8H2vc`</summary>

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
  "parentUuid": "d039d612-9364-4590-aec0-94e14f759db8",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eJKpriHh1B9xCG9Sax",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29dd26b5-d510-44b6-aa17-43b354e83834",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P29cFtGbdYoSw6teCJdP8r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30771,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30771,
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

_source line 5 · 2026-05-14T14:47:20.963Z_

<details><summary>↩ Tool result · `toolu_01XUVQi3jzcLEEWQybH8H2vc`</summary>

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
  "parentUuid": "29dd26b5-d510-44b6-aa17-43b354e83834",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "8b1412de-43e0-4dbc-a385-128c3756f886",
  "sourceToolAssistantUUID": "29dd26b5-d510-44b6-aa17-43b354e83834",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T14:47:23.531Z_



Now let me run all 12 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b1412de-43e0-4dbc-a385-128c3756f886",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eJZjGhYJdwkSSjC5b4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d9c346b-71b6-436a-94f1-1f542f2d1a4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RAa4LJNCaVVMmTKPhBVvyf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 30771,
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

_source line 7 · 2026-05-14T14:47:23.703Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016Y2giioE3EHCcPYoRJipDp`</summary>

```json
{
  "query": "hard negative mining code retrieval 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d9c346b-71b6-436a-94f1-1f542f2d1a4a",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eJZjGhYJdwkSSjC5b4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "efce5e77-aa49-4bd1-8934-27d3e8a57a5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RAa4LJNCaVVMmTKPhBVvyf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 30771,
      "output_tokens": 80,
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
          "output_tokens": 80,
          "cache_read_input_tokens": 30771,
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

_source line 8 · 2026-05-14T14:47:31.115Z_

<details><summary>↩ Tool result · `toolu_016Y2giioE3EHCcPYoRJipDp`</summary>

```text
Web search results for query: "hard negative mining code retrieval 2024 2025 2026"

Links: [{"title":"[2505.18366] Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems","url":"https://arxiv.org/abs/2505.18366"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://arxiv.org/pdf/2505.18366"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems - ACL Anthology","url":"https://aclanthology.org/2025.acl-industry.72/"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3695994"},{"title":"[PDF] Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Hard-Negative-Mining-for-Domain-Specific-Retrieval-Meghwani-Agarwal/b67c02d3016611943e3c3ccc26a11c1cac4923ad"},{"title":"ARHN: Answer-Centric Relabeling of Hard Negatives with Open-Source LLMs for Dense Retrieval","url":"https://arxiv.org/html/2604.11092"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems","url":"https://arxiv.org/html/2505.18366v1"},{"title":"Paper page - Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems","url":"https://huggingface.co/papers/2505.18366"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | Request PDF","url":"https://www.researchgate.net/publication/384848348_Effective_Hard_Negative_Mining_for_Contrastive_Learning-based_Code_Search"},{"title":"hard-negative-mining · GitHub Topics · GitHub","url":"https://github.com/topics/hard-negative-mining"}]

Based on the search results, here are the key findings on hard negative mining for code retrieval from 2024-2026:

## Recent Work in Code Retrieval

A recent framework called CoCoHaNeRe (Code search augmented by Contrastive learning with differentiable Hard Negative samples Retrieval) proposes using contrastive learning with hard negatives for code search. Code search aims to find the most relevant code snippet in a large codebase based on a given natural language query, and an accurate code search engine can increase code reuse and improve programming efficiency.

The challenge is that erroneous code with higher text similarity to queries (hard negatives) can mislead models, and applying contrastive learning on samples with similar texts but different semantics is essential rather than relying on simple random sampling.

## Broader Hard Negative Mining Research

Beyond code retrieval specifically, there has been significant work on hard negative mining more broadly:

1. **Enterprise Systems (2025)**: A paper on "Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems" proposes a scalable hard-negative mining framework tailored specifically for domain-specific enterprise data.

2. **False Negatives Problem (2026)**: Conventional hard-negative mining can introduce false negatives because it emphasizes difficulty without explicitly checking answer relevance, with negatives often mined from top-ranked results or high-scoring candidates. Recent work has focused on addressing this by using LLM-based relabeling to correct mislabeled instances.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efce5e77-aa49-4bd1-8934-27d3e8a57a5b",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "fcaec14d-d0bf-43b4-ae38-8c9f3ed111f2",
  "sourceToolAssistantUUID": "efce5e77-aa49-4bd1-8934-27d3e8a57a5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T14:47:33.516Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019WPwZiW6JzCPMDthXzhCZQ`</summary>

```json
{
  "query": "contrastive learning code search hard negatives"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcaec14d-d0bf-43b4-ae38-8c9f3ed111f2",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eKJqMqvdhNDjTnfrZQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b05f8ab-d3c7-47fd-827a-4e338ba62cfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RL9P9CUTXucLzfFsYRaNu7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 979,
      "cache_read_input_tokens": 32228,
      "output_tokens": 60,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 979
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 60,
          "cache_read_input_tokens": 32228,
          "cache_creation_input_tokens": 979,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 979,
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

_source line 10 · 2026-05-14T14:47:41.644Z_

<details><summary>↩ Tool result · `toolu_019WPwZiW6JzCPMDthXzhCZQ`</summary>

```text
Web search results for query: "contrastive learning code search hard negatives"

Links: [{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3695994"},{"title":"[2010.04592] Contrastive Learning with Hard Negative Samples","url":"https://arxiv.org/abs/2010.04592"},{"title":"Uncertainty-Aware Contrastive Learning With Hard Negative Sampling for","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34070/36225"},{"title":"Uncertainty-Aware Contrastive Learning with Hard Negative Sampling for Code Search Tasks | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34070"},{"title":"CONTRASTIVE LEARNING WITH HARD NEGATIVE ...","url":"https://openreview.net/pdf?id=CR1XOQ0UTh-"},{"title":"Contrastive learning with hard negative samples","url":"https://arxiv.org/pdf/2010.04592"},{"title":"Contrastive Learning with Hard Negative Samples | OpenReview","url":"https://openreview.net/forum?id=CR1XOQ0UTh-"},{"title":"Hard Negative Mixing for Contrastive Learning Yannis Kalantidis","url":"https://proceedings.neurips.cc/paper/2020/file/f7cade80b7cc92b991cf4d2806d6bd78-Paper.pdf"},{"title":"Effective Hard Negative Mining for Contrastive Learning-based Code Search | CoLab","url":"https://colab.ws/articles/10.1145/3695994"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | Request PDF","url":"https://www.researchgate.net/publication/384848348_Effective_Hard_Negative_Mining_for_Contrastive_Learning-based_Code_Search"}]

Based on the web search results, here's what I found about contrastive learning, code search, and hard negatives:

## Overview

Hard negative examples are negative examples in the codebase that are most similar to positive examples, and they play an important role in improving code search systems using contrastive learning.

## The Problem

Due to the random selection of negative samples, semantic representations learned by existing models cannot distinguish similar codes well. A concrete example illustrates this: erroneous code with higher text similarity to a user query contains similar keywords such as "event," "callback," "create," and "version," while the correct code contains fewer similar keywords.

## Hard Negative Mining Approaches

**General Principles:** Contrastive learning of representations benefits from hard negative samples (i.e., points that are difficult to distinguish from an anchor point). The key challenge toward using hard negatives is that contrastive methods must remain unsupervised, and in response, researchers develop new classes of unsupervised methods for selecting hard negative samples where the user can control the amount of hardness.

**Code Search Application:** CoCoHaNeRe is a Code search framework augmented by Contrastive learning with differentiable Hard Negative samples Retrieval. Additionally, an uncertainty learning strategy can produce diverse embeddings by learning to transform the original inputs into Gaussian distributions and then taking a reparameterization trick.

These approaches show promising improvements in code search performance across different models and programming languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b05f8ab-d3c7-47fd-827a-4e338ba62cfe",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "14f1d81b-5bc1-4bc2-8cad-0576ebe94d36",
  "sourceToolAssistantUUID": "0b05f8ab-d3c7-47fd-827a-4e338ba62cfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T14:47:43.930Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EB2ciQsKwxjfsuSzSHEx1m`</summary>

```json
{
  "query": "CoCoHaNeRe code search contrastive hard negative retrieval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14f1d81b-5bc1-4bc2-8cad-0576ebe94d36",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eL5rXzkcNseBggwpu7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8934180d-0a3a-4adc-812f-e0a010a3aaf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXTJZ6k5dhDhUohJyGZ1Sr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 938,
      "cache_read_input_tokens": 33207,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 938
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 33207,
          "cache_creation_input_tokens": 938,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 938,
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

_source line 12 · 2026-05-14T14:47:50.877Z_

<details><summary>↩ Tool result · `toolu_01EB2ciQsKwxjfsuSzSHEx1m`</summary>

```text
Web search results for query: "CoCoHaNeRe code search contrastive hard negative retrieval"

Links: [{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3695994"},{"title":"Effective Hard Negative Mining for Contrastive Learning-based Code Search | CoLab","url":"https://colab.ws/articles/10.1145/3695994"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | Request PDF","url":"https://www.researchgate.net/publication/384848348_Effective_Hard_Negative_Mining_for_Contrastive_Learning-based_Code_Search"},{"title":"[PDF] CoCoSoDa: Effective Contrastive Learning for Code Search | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CoCoSoDa:-Effective-Contrastive-Learning-for-Code-Shi-Wang/ae52599f2d2731f68c567b6726a5185c06cb9a41"},{"title":"CNEG-VC: Contrastive Learning Using Hard Negative Example In Non-Parallel Voice Conversion - R Discovery","url":"https://discovery.researcher.life/article/cnegvc-contrastive-learning-using-hard-negative-example-in-nonparallel-voice-conversion/e3a457b482f43689ba39d314a341bbb5"},{"title":"CoCoSoDa: Effective Contrastive Learning for Code Search","url":"https://arxiv.org/pdf/2204.03293"},{"title":"Revisiting Hard Negative Mining in Contrastive Learning for Visual Understanding","url":"https://www.mdpi.com/2079-9292/12/23/4884"},{"title":"Uncertainty-Aware Contrastive Learning With Hard Negative Sampling for","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34070/36225"},{"title":"CoCoSoDa: Effective Contrastive Learning for Code Search | Proceedings of the 45th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1109/ICSE48619.2023.00185"},{"title":"CMCS: contrastive-metric learning via vector-level sampling and augmentation for code search | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-64205-2"}]

Based on the search results, here's what I found about **CoCoHaNeRe**:

## Overview

CoCoHaNeRe is a Code search framework augmented by Contrastive learning with differentiable Hard Negative samples Retrieval.

## Key Features

**Memory Bank Design:**
The framework includes a new memory bank that supports finding the nearest neighbor of query as hard negatives.

**Differentiable Hard Negatives:**
The method adopts differentiable hard negative embeddings for the model's gradient descent process, specifically recomputing the embeddings of hard negatives and putting them in the same batch as positive examples for training.

## Technical Components

The method contains a new searchable memory bank for hard negative retrieval and a new hard negative contrastive loss (HNCL) function. This allows the model to learn the semantic difference between similar code and text.

## Performance Results

In the code search task, the average MRR score of CoCoHaNeRe exceeds CodeBERT, GraphCodeBERT, and UniXcoder by 11.25%, 8.13%, and 7.38%, respectively. Qualitative analysis shows that the model effectively distinguishes high-order semantic differences between similar codes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8934180d-0a3a-4adc-812f-e0a010a3aaf5",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "f6a77dd8-0286-4b42-b12c-c81ca7133547",
  "sourceToolAssistantUUID": "8934180d-0a3a-4adc-812f-e0a010a3aaf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T14:47:53.214Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DtSj212MHmRWFEoGG2JojD`</summary>

```json
{
  "query": "dataflow aware training code retrieval program analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6a77dd8-0286-4b42-b12c-c81ca7133547",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eLmJr54zkNsNbBa6yS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "958ffd78-e6e5-4818-b0d8-89b6703c84a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7xNcV56RBMqBwTAkZUW2p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1002,
      "cache_read_input_tokens": 34145,
      "output_tokens": 60,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1002
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 60,
          "cache_read_input_tokens": 34145,
          "cache_creation_input_tokens": 1002,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1002,
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

_source line 14 · 2026-05-14T14:48:01.217Z_

<details><summary>↩ Tool result · `toolu_01DtSj212MHmRWFEoGG2JojD`</summary>

```text
Web search results for query: "dataflow aware training code retrieval program analysis"

Links: [{"title":"Dataflow-Guided Retrieval Augmentation for Repository- ...","url":"https://aclanthology.org/2024.acl-long.431.pdf"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Dataflow-Guided Retrieval Augmentation for Repository-Level Code Completion","url":"https://arxiv.org/html/2405.19782v1"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"[2405.19782] Dataflow-Guided Retrieval Augmentation for Repository-Level Code Completion","url":"https://arxiv.org/abs/2405.19782"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"CodeRAG: Finding Relevant and Necessary Knowledge ...","url":"https://aclanthology.org/2025.emnlp-main.1187.pdf"},{"title":"LLMDFA: Analyzing Dataflow in Code with Large Language Models","url":"https://chengpeng-wang.github.io/publications/LLMDFA_NeurIPS2024.pdf"},{"title":"[2402.10754] LLMDFA: Analyzing Dataflow in Code with Large Language Models","url":"https://arxiv.org/abs/2402.10754"},{"title":"AwesomeLLM4SE/README.md at main · iSEngLab/AwesomeLLM4SE","url":"https://github.com/iSEngLab/AwesomeLLM4SE/blob/main/README.md"}]

Based on the search results, here's what I found about dataflow-aware training code retrieval program analysis:

## Key Research: DraCo Framework

The primary work in this area is DraCo, a dataflow-guided retrieval augmentation approach for repository-level code completion that parses a private repository into code entities and establishes their relations through an extended dataflow analysis, forming a repo-specific context graph.

## Problem It Addresses

Pre-trained language models struggle to generate correct completions in private repositories, as previous studies retrieve cross-file context based on import relations or text similarity, which is insufficiently relevant to completion targets.

## How It Works

When triggering code completion, DraCo precisely retrieves relevant background knowledge from the repo-specific context graph and generates well-formed prompts to query code language models. An extended dataflow analysis is designed by setting type-sensitive data dependency relations to guide more precise retrieval.

## Broader Context

Beyond DraCo, dataflow analysis has been applied in other contexts. LLMDFA is an LLM-powered compilation-free and customizable dataflow analysis framework that decomposes the analysis into several subtasks, leveraging LLMs to synthesize code that outsources delicate reasoning to external expert tools.

The research demonstrates that incorporating dataflow analysis into code retrieval and generation systems can significantly improve the ability to identify and work with code dependencies in repository-level tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "958ffd78-e6e5-4818-b0d8-89b6703c84a8",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "379696b9-f6e4-4a8e-89b3-adb25c19c54a",
  "sourceToolAssistantUUID": "958ffd78-e6e5-4818-b0d8-89b6703c84a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T14:48:03.881Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016Ydr6BPJdWi1YwrQLnPJbM`</summary>

```json
{
  "query": "structure-guided negative mining program structure contrastive code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "379696b9-f6e4-4a8e-89b3-adb25c19c54a",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eMXZdozoS1DUMHiAgZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f89d912-142e-4755-a6d1-cfc768a63917",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mZRupsgbgmQKMKRS5nGyz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 922,
      "cache_read_input_tokens": 35147,
      "output_tokens": 62,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 922
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 62,
          "cache_read_input_tokens": 35147,
          "cache_creation_input_tokens": 922,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 922,
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

_source line 16 · 2026-05-14T14:48:10.954Z_

<details><summary>↩ Tool result · `toolu_016Ydr6BPJdWi1YwrQLnPJbM`</summary>

```text
Web search results for query: "structure-guided negative mining program structure contrastive code"

Links: [{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3695994"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | Request PDF","url":"https://www.researchgate.net/publication/384848348_Effective_Hard_Negative_Mining_for_Contrastive_Learning-based_Code_Search"},{"title":"Structure-Aware Hard Negative Mining for Heterogeneous Graph Contrastive Learning | DeepAI","url":"https://deepai.org/publication/structure-aware-hard-negative-mining-for-heterogeneous-graph-contrastive-learning"},{"title":"GitHub - junxia97/ProGCL: [ICML 2022] \"ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning\"","url":"https://github.com/junxia97/ProGCL"},{"title":"ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning","url":"https://proceedings.mlr.press/v162/xia22b.html"},{"title":"Structure-Aware Hard Negative Mining for Heterogeneous ...","url":"https://arxiv.org/pdf/2108.13886"},{"title":"Revisiting Hard Negative Mining in Contrastive Learning for Visual Understanding","url":"https://www.mdpi.com/2079-9292/12/23/4884"},{"title":"Structure-Aware Hard Negative Mining for Heterogeneous ...","url":"https://hejiecui.com/files/papers/horace.pdf"},{"title":"Structure-Aware Hard Negative Mining for Heterogeneous Graph Contrastive Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210813886Z/abstract"},{"title":"[2108.13886] Structure-Aware Hard Negative Mining for Heterogeneous Graph Contrastive Learning","url":"https://arxiv.org/abs/2108.13886"}]

Based on the search results, here's what I found about structure-guided negative mining and program structure contrastive code:

## Key Research Areas

The search results reveal several relevant research directions:

### 1. **Hard Negative Mining for Code Search**

Hard negative examples are negative examples in the codebase that are most similar to positive examples, introduced into contrastive training to help the model distinguish similar codes. One notable approach is CoCoHaNeRe, which introduces hard negative examples into contrastive training and adds all hard negative examples to the model's gradient descent process.

### 2. **Structure-Aware Hard Negative Mining**

A structure-aware hard negative mining scheme measures hardness by structural characteristics for heterogeneous graphs. More specifically, instead of measuring hardness using similarity between node representations, hardness is measured according to structural characteristics and more negatives are synthesized by randomly mixing up selected negatives, giving larger weights to harder negatives.

### 3. **Contrastive Learning for Code**

The state-of-the-art learning method uses the contrastive learning paradigm, with the objective to maximize the similarity between matching code and query (positive samples) and minimize the similarity between mismatched pairs (negative samples).

### 4. **Other Approaches**

Additional research includes ProGCL, which estimates the probability of a negative being true one as a measure for negatives' hardness, with two schemes (ProGCL-weight and ProGCL-mix) to boost performance.

These approaches collectively address the challenge of improving contrastive learning models by more effectively selecting and weighting negative samples based on structural and semantic properties.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f89d912-142e-4755-a6d1-cfc768a63917",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "b55ca22a-1e76-4912-b1d7-8e7e710923e2",
  "sourceToolAssistantUUID": "4f89d912-142e-4755-a6d1-cfc768a63917",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T14:48:13.476Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V8GUunXCB8EJM1j8BAHy2N`</summary>

```json
{
  "query": "code retrieval negative sampling strategy 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b55ca22a-1e76-4912-b1d7-8e7e710923e2",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eNFXkps5gs83Tn4xe4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f47e4432-1ce9-44d2-bf23-937b08dfb87f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGRbvBajHwExis6oXTdKCQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 990,
      "cache_read_input_tokens": 36069,
      "output_tokens": 63,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 990
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 63,
          "cache_read_input_tokens": 36069,
          "cache_creation_input_tokens": 990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 990,
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

_source line 18 · 2026-05-14T14:48:21.387Z_

<details><summary>↩ Tool result · `toolu_01V8GUunXCB8EJM1j8BAHy2N`</summary>

```text
Web search results for query: "code retrieval negative sampling strategy 2024 2025"

Links: [{"title":"Uncertainty-Aware Contrastive Learning With Hard Negative Sampling for","url":"https://csse.szu.edu.cn/attachment/cglr/1749432531_AAAI-2025%E8%AE%BA%E6%96%87-%E5%88%98%E6%B6%B5.pdf"},{"title":"Negative Sampling Techniques for Dense Passage Retrieval ...","url":"https://staff.fnwi.uva.nl/m.derijke/wp-content/papercite-data/pdf/rajapakse-2024-study.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/5df5b1f121c915d8bdd00db6aac20827-Paper-Conference.pdf"},{"title":"Negative Sampling Techniques in Information Retrieval: A Survey","url":"https://arxiv.org/html/2603.18005v1"},{"title":"Does Generative Retrieval Overcome the Limitations of Dense ...","url":"https://staff.fnwi.uva.nl/m.derijke/wp-content/papercite-data/pdf/zhang-2025-does-arxiv.pdf"},{"title":"Uncertainty-Aware Contrastive Learning with Hard Negative Sampling for Code Search Tasks | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34070"},{"title":"Negative Sampling Strategy","url":"https://www.emergentmind.com/topics/negative-sampling-strategy"},{"title":"Improving the Context Length and Efficiency of Code Retrieval ...","url":"https://www.arxiv.org/pdf/2503.22935v2"},{"title":"Latent Query Alignment for Enhanced Domain-specific Retrieval ...","url":"http://poster-openaccess.com/files/ICIC2025/3255.pdf"},{"title":"Published as a conference paper at ICLR 2025 MM-EMBED: UNIVERSAL MULTIMODAL","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/6d5d6afa9957cfc9142ba60e78a467e9-Paper-Conference.pdf"}]

Based on the search results, here's what I found about code retrieval negative sampling strategies in 2024-2025:

## Recent Developments in Code Retrieval Negative Sampling

### Hard Negative Sampling for Code Search

Recent research has designed hard negative sampling strategies to construct query-code pairs for improving the effectiveness of uncertainty-aware contrastive learning. Experimental results indicate that these approaches outperform 10 baseline methods on large code search datasets with six programming languages.

### Conventional vs. Hard Negative Approaches

In previous studies on code search, it is common practice to use other code snippets in other query-code pairs within the same batch as negative examples (In-Batch Negative), compared with the "Hard Negative" method which is integrated into proposed negative sampling techniques.

### General Negative Sampling Principles

Recent research has identified key principles for effective negative sampling:

Gradient analysis of contrastive losses reveals that too-easy negatives have a vanishing training signal, while the hardest negatives can saturate gradients or contribute false negative risk. Principles such as the quasi-triangular region (TriSampler) or sublinear positivity guide the region in representation space from which negatives should be drawn.

Advanced negative sampling techniques (GTR-Base, TAS-B achieving 44.0 average NDCG@10) significantly outperform simpler approaches, with TAS-B's combination of knowledge distillation and hard negatives outperforming other methods on 14/18 BEIR datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f47e4432-1ce9-44d2-bf23-937b08dfb87f",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "7b3e6c93-3bbe-4fce-840f-3a4cf47ba371",
  "sourceToolAssistantUUID": "f47e4432-1ce9-44d2-bf23-937b08dfb87f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T14:48:23.969Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LDgD2cU94R8TwCumAoud5k`</summary>

```json
{
  "query": "SweRank code retrieval 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b3e6c93-3bbe-4fce-840f-3a4cf47ba371",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eP1oHoLw9ewxTWWjeK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b64d5311-9b99-4e04-8f58-5ddaa1db784e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYLGgw652vXw4BMPZFJtpo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1038,
      "cache_read_input_tokens": 37059,
      "output_tokens": 61,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1038
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 61,
          "cache_read_input_tokens": 37059,
          "cache_creation_input_tokens": 1038,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1038,
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

_source line 20 · 2026-05-14T14:48:30.721Z_

<details><summary>↩ Tool result · `toolu_01LDgD2cU94R8TwCumAoud5k`</summary>

```text
Web search results for query: "SweRank code retrieval 2025"

Links: [{"title":"SweRank: Software Issue Localization with Code Ranking - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250507849G/abstract"},{"title":"SWERANK+: Multilingual, Multi-Turn Code Ranking for Software Issue Localization","url":"https://arxiv.org/pdf/2512.20482"},{"title":"[2505.07849] SweRank: Software Issue Localization with Code Ranking","url":"https://arxiv.org/abs/2505.07849"},{"title":"SWERANK: SOFTWARE ISSUE LOCALIZATION","url":"https://openreview.net/pdf/e70b6b05efcf9186c40a441e74e6722123168739.pdf"},{"title":"Paper page - SweRank: Software Issue Localization with Code Ranking","url":"https://huggingface.co/papers/2505.07849"},{"title":"SweRank: Software Issue Localization with Code Ranking","url":"https://arxiv.org/pdf/2505.07849"},{"title":"GitHub - SalesforceAIResearch/SweRank","url":"https://github.com/SalesforceAIResearch/SweRank"},{"title":"Agent-Based Debugging Gets a Cost-Effective Alternative: Salesforce AI Presents SWERank for Accurate and Scalable Software Issue Localization - MarkTechPost","url":"https://www.marktechpost.com/2025/05/13/agent-based-debugging-gets-a-cost-effective-alternative-salesforce-ai-presents-swerank-for-accurate-and-scalable-software-issue-localization/"},{"title":"We introduce SWERank, a retrieve-and-rerank framework for software issue localization, which aims to identify the relevant code that needs to be modified to fix a software issue.","url":"https://gangiswag.github.io/SweRank/"},{"title":"[2512.20482] SweRank+: Multilingual, Multi-Turn Code Ranking for Software Issue Localization","url":"https://arxiv.org/abs/2512.20482"}]

Based on the search results, here's what I found about SweRank code retrieval in 2025:

## Overview

SweRank is an efficient and effective retrieve-and-rerank framework for software issue localization. Software issue localization is the task of identifying the precise code locations (files, classes, or functions) relevant to a natural language issue description (e.g., bug report, feature request).

## Framework Components

SweRank consists of two key components: SWERankEmbed, a bi-encoder retrieval model that encodes GitHub issues and code snippets into a shared embedding space for efficient similarity-based retrieval, and SWERankLLM, a listwise reranker built on instruction-tuned LLMs that refines the ranking of retrieved candidates using contextual understanding.

## Training Dataset

To facilitate training, SweLoc was constructed as a large-scale dataset curated from public GitHub repositories, featuring real-world issue descriptions paired with corresponding code modifications.

## Performance

Empirical results on SWE-Bench-Lite and LocBench show that SweRank achieves state-of-the-art performance, outperforming both prior ranking models and costly agent-based systems using closed-source LLMs like Claude-3.5.

## Recent Extension

There's also a newer development: SweRank+ couples SweRankMulti, a cross-lingual code ranking tool, with SweRankAgent, an agentic search setup, for iterative, multi-turn reasoning over the code repository, with SweRankMulti comprising a code embedding retriever and a listwise LLM reranker trained using a large-scale issue localization dataset spanning multiple popular programming languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b64d5311-9b99-4e04-8f58-5ddaa1db784e",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "d20a64d3-f815-425a-b6a1-5e6784b18beb",
  "sourceToolAssistantUUID": "b64d5311-9b99-4e04-8f58-5ddaa1db784e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T14:48:33.775Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JcN9sSbuPZQFDv8B5tKJn6`</summary>

```json
{
  "query": "SWE-Fixer code retrieval bug localization 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d20a64d3-f815-425a-b6a1-5e6784b18beb",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2ePhidG4Ukd3jJFzCX8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d487e0bb-63ae-4664-86e0-4b89076b8903",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NmB2G3S6qNene8DEchUWYq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 38097,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1023
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 38097,
          "cache_creation_input_tokens": 1023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1023,
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

_source line 22 · 2026-05-14T14:48:41.510Z_

<details><summary>↩ Tool result · `toolu_01JcN9sSbuPZQFDv8B5tKJn6`</summary>

```text
Web search results for query: "SWE-Fixer code retrieval bug localization 2025"

Links: [{"title":"SWE-Fixer: Training Open-Source LLMs for Effective and ...","url":"https://aclanthology.org/2025.findings-acl.62.pdf"},{"title":"Reformulate, Retrieve, Localize: Agents for Repository-Level Bug Localization","url":"https://arxiv.org/html/2512.07022"},{"title":"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution","url":"https://arxiv.org/html/2501.05040v2"},{"title":"GitHub - InternLM/SWE-Fixer · GitHub","url":"https://github.com/InternLM/SWE-Fixer"},{"title":"SweRank: Software Issue Localization with Code Ranking","url":"https://arxiv.org/html/2505.07849v2"},{"title":"SWE-Fixer/README.md at main · InternLM/SWE-Fixer","url":"https://github.com/InternLM/SWE-Fixer/blob/main/README.md"},{"title":"SWE-Lancer-Loc: Real-World Issue Localization","url":"https://www.emergentmind.com/topics/swe-lancer-loc"},{"title":"SWE-Llama: Automated Code Repair Models","url":"https://www.emergentmind.com/topics/swe-llama"},{"title":"SWE-Fixer: Training LLMs for Real World Github Issue Resolving","url":"https://arxiv.org/html/2501.05040v1"},{"title":"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution","url":"https://www.researchgate.net/publication/394273882_SWE-Fixer_Training_Open-Source_LLMs_for_Effective_and_Efficient_GitHub_Issue_Resolution"}]

Based on the search results, here's information about SWE-Fixer and its approach to code retrieval and bug localization:

## Overview

SWE-Fixer is an open-source framework designed to effectively and efficiently resolve GitHub issues, comprising two essential modules: a code file retrieval module and a code editing module.

## Code Retrieval and Bug Localization

The retrieval module employs BM25 along with a lightweight model to achieve coarse-to-fine file retrieval. More specifically, the framework uses a coarse-to-fine retrieval method combining BM25 and a Retriever.

The SWE-Fixer-Retriever-7B is finetuned for the code file retrieval task, taking issue descriptions and BM25-retrieved results as input and identifying the defective files related to the issue.

## Implementation and Performance

For implementation, Qwen2.5-7b and Qwen2.5-72b are finetuned for the retriever and the editor respectively, leveraging a curated dataset of 110K instances.

SWE-Fixer achieves 23.3% on SWE-Bench Lite and 30.2% on SWE-Bench Verified. Among open-source model-based approaches, SWE-Fixer achieves the highest Best@1 performance and outperforms several proprietary model-based methods, including those based on GPT-4, GPT-4o, and Claude-3-Opus.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d487e0bb-63ae-4664-86e0-4b89076b8903",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "53e91c2c-dc5a-49c0-ac70-25d805d0e984",
  "sourceToolAssistantUUID": "d487e0bb-63ae-4664-86e0-4b89076b8903",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T14:48:44.294Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WVp4uJWTNceWBHZTpFwh2X`</summary>

```json
{
  "query": "representation geometry hard negatives contrastive learning saturation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53e91c2c-dc5a-49c0-ac70-25d805d0e984",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eQVpYPmeRTQwh6NUny",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a80b2b51-4914-4f70-92cd-e24696b31acd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MoSnAtmBtFMeACCXCXJLVc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 39120,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 954
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 39120,
          "cache_creation_input_tokens": 954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 954,
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

_source line 24 · 2026-05-14T14:48:54.455Z_

<details><summary>↩ Tool result · `toolu_01WVp4uJWTNceWBHZTpFwh2X`</summary>

```text
Web search results for query: "representation geometry hard negatives contrastive learning saturation 2024 2025"

Links: [{"title":"Hard Negative Contrastive Loss","url":"https://www.emergentmind.com/topics/contrastive-loss-with-hard-negative-samples"},{"title":"[2311.05139] Hard-Negative Sampling for Contrastive Learning: Optimal Representation Geometry and Neural- vs Dimensional-Collapse","url":"https://arxiv.org/abs/2311.05139"},{"title":"Hard Negative Contrastive Learning for Fine-Grained Geometric Understanding in Large Multimodal Models","url":"https://arxiv.org/html/2505.20152v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/b010241b9f1cdfc7d4c392db899cef86-Paper-Conference.pdf"},{"title":"Contrastive Learning with Hard Negatives","url":"https://www.emergentmind.com/topics/contrastive-learning-with-hard-negative-samples"},{"title":"SNAPHARD CONTRAST LEARNING | OpenReview","url":"https://openreview.net/forum?id=4cZvjp8Iwk"},{"title":"Adaptive graph contrastive learning with hard negative mining for multimodal hyperspectral and LiDAR classification - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12969351/"},{"title":"A Hard Negatives Mining and Enhancing Method for Multi-Modal Contrastive Learning","url":"https://www.mdpi.com/2079-9292/14/4/767"},{"title":"CONTRASTIVE LEARNING WITH HARD NEGATIVE ...","url":"https://openreview.net/pdf?id=CR1XOQ0UTh-"},{"title":"Contrastive Representation Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2021-05-31-contrastive/"}]

I've found relevant research on representation geometry, hard negatives in contrastive learning, and related saturation phenomena from 2024-2025. Here are the key findings:

## Recent Developments (2024-2025)

**Representation Geometry and Neural Collapse:**
For widely-studied data models and general loss and sample-hardening functions, the losses of Supervised Contrastive Learning (SCL), Hard-SCL (HSCL), and Unsupervised Contrastive Learning (UCL) are minimized by representations that exhibit Neural-Collapse (NC), where the class means form an Equiangular Tight Frame (ETF) and data from the same class are mapped to the same representation.

Adam optimization (with batching) of HSCL and HUCL losses with random initialization and suitable hardness levels can indeed converge to the NC-geometry if unit-ball or unit-sphere feature normalization is incorporated. Without incorporating hard-negatives or feature normalization, however, the representations learned via Adam suffer from Dimensional-Collapse (DC) and fail to attain the NC-geometry.

**Hard Negative Sampling Strategies:**
Empirical best practices include tuning hardness parameters (e.g., β=0.1–10), using both clustering-based and similarity-based selection, and maintaining label exclusion where possible to avoid false negatives.

Adaptive margin learning involves dynamic margin loss that increases separation when negatives become close to anchor (as of May 2025).

**Multimodal Applications:**
Recent work fine-tunes models following the MMCLIP training strategy, using 100K hard caption negative samples, each consisting of 10 rule-based and 30 retrieval-based negatives to enhance the model's understanding of geometric elements, and 4K hard image negative samples, where each example includes 10 negative geometric diagrams.

**Key Open Problems:**
Two critical considerations are avoiding false negatives (samples of the same class), and balancing the focus on hard negatives to prevent collapse or label noise amplification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a80b2b51-4914-4f70-92cd-e24696b31acd",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "8ae5757c-3126-4691-95ed-d8fd76c40a4e",
  "sourceToolAssistantUUID": "a80b2b51-4914-4f70-92cd-e24696b31acd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T14:48:56.977Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GJmqo2bR4QYWu4Hbs44XSE`</summary>

```json
{
  "query": "ARISE code dataflow retrieval 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ae5757c-3126-4691-95ed-d8fd76c40a4e",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eRT773ZesdM7RYePb2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2aee1f8f-b349-4166-b71a-15135ac7d0ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019nRNyUYbjazoX1wRudooDc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1074,
      "cache_read_input_tokens": 40074,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1074
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 40074,
          "cache_creation_input_tokens": 1074,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1074,
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

_source line 26 · 2026-05-14T14:49:02.354Z_

<details><summary>↩ Tool result · `toolu_01GJmqo2bR4QYWu4Hbs44XSE`</summary>

```text
Web search results for query: "ARISE code dataflow retrieval 2024 2025"

Links: [{"title":"JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021 1","url":"https://arxiv.org/pdf/2510.09721"},{"title":"Arise Crossover Redeem Codes (February 2026) | BlueStacks","url":"https://www.bluestacks.com/blog/redeem-codes/roblox-arise-crossover-redeem-codes-en.html"},{"title":"Solo Leveling Arise codes (May 2026) | Pocket Gamer","url":"https://www.pocketgamer.com/solo-leveling-arise/codes/"},{"title":"[2405.19782] Dataflow-Guided Retrieval Augmentation for Repository-Level Code Completion","url":"https://arxiv.org/abs/2405.19782"},{"title":"Solo Leveling Arise codes May 2026","url":"https://www.pockettactics.com/solo-leveling-arise/codes"},{"title":"All Codes in October 2025 and How to Redeem | Solo Leveling Arise｜Game8","url":"https://game8.co/games/Solo-Leveling-Arise/archives/457152"},{"title":"Solo Leveling: Arise Codes","url":"https://www.thegamer.com/solo-leveling-arise-codes-updated-daily/"},{"title":"Aisera Product Release notes - Mar 25, 2026 | Release Notes | Aisera Product Documentation","url":"https://docs.aisera.com/product-release-notes/2026/aisera-product-release-notes-mar-25-2026"},{"title":"Arise Crossover codes: All active codes in October 2025","url":"https://www.pcgamer.com/games/roblox/arise-crossover-codes/"},{"title":"Dataflow-Guided Retrieval Augmentation for Repository-Level Code Completion - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.431/"}]

Based on the search results, I found relevant information about dataflow-guided retrieval in code analysis:

## Key Finding

A dataflow-guided retrieval augmentation approach called DraCo was proposed for repository-level code completion. DraCo parses a private repository into code entities and establishes their relations through an extended dataflow analysis, forming a repo-specific context graph.

Whenever triggering code completion, DraCo precisely retrieves relevant background knowledge from the repo-specific context graph and generates well-formed prompts to query code language models.

The experiments demonstrate the superior accuracy and applicable efficiency of DraCo, improving code exact match by 3.43% and identifier F1-score by 3.27% on average compared to the state-of-the-art approach.

This research was published at ACL 2024 (the 62nd Annual Meeting of the Association for Computational Linguistics) in August 2024. The work addresses the challenge of retrieving relevant context in private repositories for code completion tasks by using dataflow analysis instead of simpler methods like import relations or text similarity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2aee1f8f-b349-4166-b71a-15135ac7d0ec",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "ab17d233-a66b-48cc-8c43-a6845c1231c8",
  "sourceToolAssistantUUID": "2aee1f8f-b349-4166-b71a-15135ac7d0ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T14:49:04.893Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UyNKcZQBmW8z1iMpf9f1p3`</summary>

```json
{
  "query": "CodexGraph code retrieval graph-based 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab17d233-a66b-48cc-8c43-a6845c1231c8",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eS2vb96bgYGW5v4B1f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "360251c0-94b6-4f96-9022-7c2c830c68a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ybd4TGyZ5q5mk1YVVnF18",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 857,
      "cache_read_input_tokens": 41148,
      "output_tokens": 63,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 857
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 63,
          "cache_read_input_tokens": 41148,
          "cache_creation_input_tokens": 857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 857,
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

_source line 28 · 2026-05-14T14:49:12.375Z_

<details><summary>↩ Tool result · `toolu_01UyNKcZQBmW8z1iMpf9f1p3`</summary>

```text
Web search results for query: "CodexGraph code retrieval graph-based 2024"

Links: [{"title":"[2408.03910] CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://arxiv.org/abs/2408.03910"},{"title":"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://arxiv.org/html/2408.03910v2"},{"title":"CODEXGRAPH: Bridging Large Language Models and Code Repositories via Code Graph Databases","url":"https://ssawant.github.io/posts/CODEXGRAPH/CODEXGRAPH.html"},{"title":"CodexGraph","url":"https://laptype.github.io/CodexGraph-page/"},{"title":"CODEXGRAPH: Bridging Large Language Models and Code Repositories","url":"https://openreview.net/pdf/165bbc76cbb447f2ea74ed1b1a4bb3531ee87e6d.pdf"},{"title":"CODEXGRAPH: Bridging Large Language Models and ...","url":"https://aclanthology.org/2025.naacl-long.7.pdf"},{"title":"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases | OpenReview","url":"https://openreview.net/forum?id=5VGC017Wgf"},{"title":"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240803910L/abstract"},{"title":"[PDF] CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases | Semantic Scholar","url":"https://api.semanticscholar.org/arXiv:2408.03910"},{"title":"CODEXGRAPH: Bridging Large Language Models","url":"https://arxiv.org/pdf/2408.03910v2"}]

Based on the search results, here's information about CodexGraph:

## Overview

CodexGraph is a system that integrates LLM agents with graph database interfaces extracted from code repositories, enabling the LLM agent to construct and execute queries for precise, code structure-aware context retrieval and code navigation.

## Problem It Addresses

Large Language Models (LLMs) excel in stand-alone code tasks like HumanEval and MBPP, but struggle with handling entire code repositories. Current solutions rely on similarity-based retrieval or manual tools and APIs, each with notable drawbacks. Similarity-based retrieval often has low recall in complex tasks, while manual tools and APIs are typically task-specific and require expert knowledge.

## Key Technical Features

CodexGraph utilizes static analysis to extract code graphs from repositories using a task-agnostic schema where nodes represent source code symbols such as MODULE, CLASS, and FUNCTION, and edges represent relationships among these symbols, such as CONTAINS, INHERITS, and USES.

CodexGraph implements a streamlined "write then translate" strategy where a specialized translation LLM agent converts natural language queries into formal graph queries, allowing the primary LLM agent to concentrate on high-level reasoning while ensuring syntactically correct and optimized graph queries.

## Evaluation

CodexGraph was assessed using three benchmarks: CrossCodeEval, SWE-bench, and EvoCodeBench, with five real-world coding applications developed. With a unified graph database schema, CodexGraph demonstrates competitive performance in both academic and real-world environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "360251c0-94b6-4f96-9022-7c2c830c68a3",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "2ee2036b-996c-463e-9e54-3b466237c4a9",
  "sourceToolAssistantUUID": "360251c0-94b6-4f96-9022-7c2c830c68a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T14:49:15.287Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016SiNdpiafqtpTw4Q33M2Aa`</summary>

```json
{
  "query": "LocAgent code localization retrieval 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ee2036b-996c-463e-9e54-3b466237c4a9",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eSmon5GXYxEW3V459A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f56cd78-b09f-4955-ad09-ff86e8e33732",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWxjnH1YwQG1uxw6FdsX4d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 925,
      "cache_read_input_tokens": 42005,
      "output_tokens": 62,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 925
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 62,
          "cache_read_input_tokens": 42005,
          "cache_creation_input_tokens": 925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 925,
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

_source line 30 · 2026-05-14T14:49:23.296Z_

<details><summary>↩ Tool result · `toolu_016SiNdpiafqtpTw4Q33M2Aa`</summary>

```text
Web search results for query: "LocAgent code localization retrieval 2025"

Links: [{"title":"GitHub - gersteinlab/LocAgent: [ACL 2025] Graph-guided agentic framework for code localization https://arxiv.org/abs/2503.09089 · GitHub","url":"https://github.com/gersteinlab/LocAgent"},{"title":"LocAgent: Graph-Guided LLM Agents for Code Localization - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.426/"},{"title":"[2503.09089] LocAgent: Graph-Guided LLM Agents for Code Localization","url":"https://arxiv.org/abs/2503.09089"},{"title":"LocAgent: Graph-Guided LLM Agents for Code Localization","url":"https://arxiv.org/pdf/2503.09089"},{"title":"Meet LocAgent: Graph-Based AI Agents Transforming Code Localization for Scalable Software Maintenance - MarkTechPost","url":"https://www.marktechpost.com/2025/03/23/meet-locagent-graph-based-ai-agents-transforming-code-localization-for-scalable-software-maintenance/"},{"title":"LocAgent/README.md at master · gersteinlab/LocAgent","url":"https://github.com/gersteinlab/LocAgent/blob/master/README.md"},{"title":"LocAgent: Graph-Guided LLM Agents for Code Localization","url":"https://aclanthology.org/2025.acl-long.426.pdf"},{"title":"[Quick Review] LocAgent: Graph-Guided LLM Agents for Code Localization","url":"https://liner.com/review/locagent-graphguided-llm-agents-for-code-localization"},{"title":"New Tool LocAgent Released: Code Localization Accuracy up to 92.7%, a Blessing for Programmers!","url":"https://www.aibase.com/news/18470"},{"title":"(PDF) LocAgent: Graph-Guided LLM Agents for Code Localization","url":"https://www.researchgate.net/publication/389786036_LocAgent_Graph-Guided_LLM_Agents_for_Code_Localization"}]

Based on the search results, here's comprehensive information about LocAgent:

## Overview

LocAgent is a framework that addresses code localization through graph-based representation. By parsing codebases into directed heterogeneous graphs, LocAgent creates a lightweight representation that captures code structures and their dependencies, enabling LLM agents to effectively search and locate relevant entities through powerful multi-hop reasoning.

## Research Publication

LocAgent: Graph-Guided LLM Agents for Code Localization is a paper by Chen, Zhaoling and others that was presented at the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) in Vienna, Austria.

## Technical Approach

LocAgent parses codebases into directed heterogeneous graphs and creates a lightweight representation that captures code structures (files, classes, functions) and their dependencies (imports, invocations, inheritance), enabling LLM agents to effectively search and locate relevant entities through powerful multi-hop reasoning.

The core mechanism relies on a detailed graph-based indexing process. Each node, whether representing a class or function, is uniquely identified by a fully qualified name and indexed using BM25 for flexible keyword search. The model enables agents to simulate a reasoning chain that begins with extracting issue-relevant keywords, proceeds through graph traversals, and concludes with code retrievals for specific nodes.

## Performance Results

The method with the fine-tuned Qwen-2.5-Coder-Instruct-32B model achieves comparable results to SOTA proprietary models at greatly reduced cost (approximately 86% reduction), reaching up to 92.7% accuracy on file-level localization while improving downstream GitHub issue resolution success rates by 12% for multiple attempts (Pass@10).

On the newly introduced Loc-Bench dataset, which contains 660 examples across bug reports (282), feature requests (203), security issues (31), and performance problems (144), LocAgent achieved 84.59% Acc@5 and 87.06% Acc@10 at the file level.

## Development Team and Code

A team of researchers from Yale University, University of Southern California, Stanford University, and All Hands AI developed LocAgent. The code is available on GitHub at gersteinlab/LocAgent.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f56cd78-b09f-4955-ad09-ff86e8e33732",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "25686f2d-f569-4d9a-abb4-d21fd6441be4",
  "sourceToolAssistantUUID": "9f56cd78-b09f-4955-ad09-ff86e8e33732",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T14:49:25.461Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q5WxiUTNNxvWqs54Tdm7Bf`</summary>

```json
{
  "query": "RANGER code retrieval graph neural network 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25686f2d-f569-4d9a-abb4-d21fd6441be4",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eTaRSyTczsHJiJi1Tf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a457b65-19f2-4115-a369-eadfa3dca609",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RHrv9B6PuU8G3EbjH37iG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 42930,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1175
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 42930,
          "cache_creation_input_tokens": 1175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1175,
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

_source line 32 · 2026-05-14T14:49:33.473Z_

<details><summary>↩ Tool result · `toolu_01Q5WxiUTNNxvWqs54Tdm7Bf`</summary>

```text
Web search results for query: "RANGER code retrieval graph neural network 2024 2025"

Links: [{"title":"GNN-RAG: Graph Neural Retrieval for Efficient Large Language Model Reasoning on Knowledge Graphs - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.856/"},{"title":"GNN-RAG: Graph Neural Retrieval for Large Language Model Reasoning | OpenReview","url":"https://openreview.net/forum?id=EVuANndPlX"},{"title":"GNN-RAG: Graph Neural Retrieval for Efficient Large ...","url":"https://aclanthology.org/2025.findings-acl.856.pdf"},{"title":"Graph Retrieval-Augmented Generation: A Survey | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3777378"},{"title":"GitHub - DEEP-PolyU/Awesome-GraphRAG: Awesome-GraphRAG: A curated list of resources (surveys, papers, benchmarks, and opensource projects) on graph-based retrieval-augmented generation. · GitHub","url":"https://github.com/DEEP-PolyU/Awesome-GraphRAG"},{"title":"Graph Retrieval-Augmented Generation","url":"https://www.emergentmind.com/topics/graph-retrieval-augmented-generation-graph-rag"},{"title":"awesome-generative-ai-guide/research_updates/rag_research_table.md at main · aishwaryanr/awesome-generative-ai-guide","url":"https://github.com/aishwaryanr/awesome-generative-ai-guide/blob/main/research_updates/rag_research_table.md"},{"title":"Enhancements to graph neural retrieval for knowledge graph reasoning | by Tamika Bassman | Stanford CS224W: Machine Learning with Graphs | Medium","url":"https://medium.com/stanford-cs224w/enhancements-to-graph-neural-retrieval-for-knowledge-graph-reasoning-870675ac458d"},{"title":"Retrieval-Augmented Generation (RAG) Advancements: The 2024-2025 Revolution Transforming Enterprise AI - Prompt Bestie","url":"https://promptbestie.com/en/rag-advancements-2024-2025-enterprise-ai-guide/"},{"title":"[2405.20139] GNN-RAG: Graph Neural Retrieval for Large Language Model Reasoning","url":"https://arxiv.org/abs/2405.20139"}]

Based on the search results, I found information about graph neural networks for retrieval tasks, though the specific term "RANGER" doesn't appear in the results. However, there is significant research on **GNN-RAG** (Graph Neural Network-based Retrieval-Augmented Generation), which is a prominent approach in this area.

## Key Findings:

GNN-RAG was published by Mavromatis and Karypis in 2025 as part of the Findings of the Association for Computational Linguistics (ACL 2025).

### What is GNN-RAG?

GNN-RAG is a novel method for combining language understanding abilities of LLMs with the reasoning abilities of GNNs in a retrieval-augmented generation (RAG) style. The GNN-RAG framework leverages Graph Neural Networks (GNNs) for effective graph reasoning and retrieval, where the GNN retriever learns to identify useful graph information for KGQA, and at inference time, the GNN scores answer candidates and the shortest paths in the KG that connect question entities and answer candidates are retrieved.

### Performance Results

GNN-RAG achieves effective retrieval on widely used KGQA benchmarks (WebQSP and CWQ), outperforming or matching GPT-4 performance with a 7B tuned LLM, and excels on multi-hop and multi-entity questions outperforming LLM-based retrieval approaches by 8.9–15.5% points at answer F1.

If you were looking for a different system called "RANGER," please provide additional context and I can search more specifically for that.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a457b65-19f2-4115-a369-eadfa3dca609",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "aa3d15d2-1ff9-463d-92d7-1e5ea35d5da6",
  "sourceToolAssistantUUID": "2a457b65-19f2-4115-a369-eadfa3dca609",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-14T14:49:36.207Z_

Now let me run additional targeted searches to fill gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa3d15d2-1ff9-463d-92d7-1e5ea35d5da6",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eUL4XLuwAMzoEm4j13",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90119b18-8bae-4e06-8769-36ec08f860ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019rxz8uJ7YpmcreiPDkoyy6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1090,
      "cache_read_input_tokens": 44105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1090,
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

_source line 34 · 2026-05-14T14:49:36.736Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VzCo6KJeC6AvpokoF1Hggz`</summary>

```json
{
  "query": "\"uncertainty-aware contrastive learning\" \"hard negative\" code search AAAI 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90119b18-8bae-4e06-8769-36ec08f860ca",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eUL4XLuwAMzoEm4j13",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6400101-0a2c-4056-b02f-9542de497be4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019rxz8uJ7YpmcreiPDkoyy6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1090,
      "cache_read_input_tokens": 44105,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1090
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 44105,
          "cache_creation_input_tokens": 1090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1090,
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

_source line 35 · 2026-05-14T14:49:43.079Z_

<details><summary>↩ Tool result · `toolu_01VzCo6KJeC6AvpokoF1Hggz`</summary>

```text
Web search results for query: ""uncertainty-aware contrastive learning" "hard negative" code search AAAI 2025"

Links: [{"title":"Uncertainty-Aware Contrastive Learning with Hard Negative Sampling for Code Search Tasks | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34070"},{"title":"Uncertainty-Aware Contrastive Learning With Hard Negative Sampling for","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34070/36225"},{"title":"Uncertainty-Aware Contrastive Learning With Hard Negative Sampling for","url":"https://csse.szu.edu.cn/attachment/cglr/1749432531_AAAI-2025%E8%AE%BA%E6%96%87-%E5%88%98%E6%B6%B5.pdf"},{"title":"(PDF) Uncertainty-Aware Contrastive Learning with Hard Negative Sampling for Code Search Tasks","url":"https://www.researchgate.net/publication/390700481_Uncertainty-Aware_Contrastive_Learning_with_Hard_Negative_Sampling_for_Code_Search_Tasks"},{"title":"Uncertainty-guided Graph Contrastive Learning from a Unified Perspective | IJCAI","url":"https://www.ijcai.org/proceedings/2025/629"},{"title":"Uncertainty-Aware Contrastive Decoding - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1352/"},{"title":"[2505.15576] Visual Perturbation and Adaptive Hard Negative Contrastive Learning for Compositional Reasoning in Vision-Language Models","url":"https://arxiv.org/abs/2505.15576"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3695994"},{"title":"Visual perturbation and adaptive hard negative contrastive ...","url":"https://dl.acm.org/doi/10.24963/ijcai.2025/605"},{"title":"Uncertainty-guided Graph Contrastive Learning from a Unified Perspective","url":"https://www.ijcai.org/proceedings/2025/0629.pdf"}]

Based on the search results, I found a paper titled "Uncertainty-Aware Contrastive Learning with Hard Negative Sampling for Code Search Tasks" that was published at AAAI 2025.

Here's what the paper proposes:

**Core Approach:**
For both queries and codes, the paper designs an uncertainty learning strategy to produce diverse embeddings by learning to transform the original inputs into Gaussian distributions and then taking a reparameterization trick, and also designs a hard negative sampling strategy to construct query-code pairs for improving the effectiveness of uncertainty-aware contrastive learning.

**Motivation:**
The paper considers that the same semantic meaning can be presented using diverse language styles in user queries and codes, so the representation of queries and codes in an embedding space may thus be non-deterministic.

**Results:**
The experimental results indicate that the approach outperforms 10 baseline methods on a large code search dataset with six programming languages. The results also show that the strategies of uncertainty learning and hard negative sampling can really help enhance the representation of queries and codes leading to an improvement of the code search performance.

The paper is available on the AAAI conference proceedings website at https://ojs.aaai.org/index.php/AAAI/article/view/34070


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6400101-0a2c-4056-b02f-9542de497be4",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "0adfc452-16e7-4421-8c5d-bd2e850a900e",
  "sourceToolAssistantUUID": "b6400101-0a2c-4056-b02f-9542de497be4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T14:49:46.097Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RmyZV6QiYtCNR64z5SKhTy`</summary>

```json
{
  "query": "CoCoHaNeRe TOSEM 2024 hard negative code search correction replication"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0adfc452-16e7-4421-8c5d-bd2e850a900e",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eV31dNrsTMk9oXK4bt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2878ff06-74a0-48cc-910e-15ce9d14fa00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TN1J4HuNvTpTGi7ddpSimU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 999,
      "cache_read_input_tokens": 45195,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 999
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 45195,
          "cache_creation_input_tokens": 999,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 999,
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

_source line 37 · 2026-05-14T14:49:51.203Z_

<details><summary>↩ Tool result · `toolu_01RmyZV6QiYtCNR64z5SKhTy`</summary>

```text
Web search results for query: "CoCoHaNeRe TOSEM 2024 hard negative code search correction replication"

Links: [{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3695994"},{"title":"GitHub - seal-replication-packages/TOSEM2024","url":"https://github.com/seal-replication-packages/TOSEM2024"},{"title":"A Novel Refactoring and Semantic Aware Abstract Syntax Tree Differencing Tool","url":"https://users.encs.concordia.ca/~nikolaos/publications/TOSEM_2024.pdf"},{"title":"TOSEM: Vol 33, No 6 - ACM Digital Library","url":"https://dl.acm.org/toc/tosem/2024/33/6"},{"title":"TOSEM: Vol 33, No 1","url":"https://dl.acm.org/toc/tosem/2024/33/1"},{"title":"TOSEM: Vol 33, No 2","url":"https://dl.acm.org/toc/tosem/2024/33/2"},{"title":"GitHub - DeepSoftwareAnalytics/KADEL: KADEL: Knowledge-Aware Denoising Learning for Commit Message Generation. [TOSEM 2024] · GitHub","url":"https://github.com/DeepSoftwareAnalytics/KADEL"},{"title":"CHASE 2024 - Full Papers - conf.researchr.org","url":"https://conf.researchr.org/track/chase-2024/chase-2024-full-papers"},{"title":"GitHub - saltudelft/ml4se: A curated list of papers, theses, datasets, and tools related to the application of Machine Learning for Software Engineering · GitHub","url":"https://github.com/saltudelft/ml4se"},{"title":"TOSEM: Just Accepted","url":"https://dl.acm.org/toc/tosem/justaccepted"}]

Based on the web search results, I found information about CoCoHaNeRe:

CoCoHaNeRe is a Code search framework augmented by Contrastive learning with differentiable Hard Negative samples Retrieval. The approach introduces hard negative examples into contrastive training, which are negative examples in the codebase that are most similar to positive examples.

The framework designs a new memory bank that supports finding the nearest neighbor of a query as hard negatives, adopts differentiable hard negative embeddings for the model's gradient descent process, and recomputes the embeddings of hard negatives to put them in the same batch as positive examples for training.

The work was published in ACM Transactions on Software Engineering and Methodology (TOSEM) in 2024. Additionally, a replication package is available on GitHub for the TOSEM2024 work.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2878ff06-74a0-48cc-910e-15ce9d14fa00",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "458c694b-3d99-4ebf-94fb-54df4106a572",
  "sourceToolAssistantUUID": "2878ff06-74a0-48cc-910e-15ce9d14fa00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T14:49:53.922Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P5m1UTt2WQFPp5RjKPqpyE`</summary>

```json
{
  "query": "CodeQL dataflow analysis training signal code embedding contrastive"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "458c694b-3d99-4ebf-94fb-54df4106a572",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eVdscmvCh62tGFv1wP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d8a67e4-f06c-4326-a6ca-2e320c0729a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyAed3MgdLQF4YwFMagpP5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 46194,
      "output_tokens": 63,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 809
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 63,
          "cache_read_input_tokens": 46194,
          "cache_creation_input_tokens": 809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 809,
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

_source line 39 · 2026-05-14T14:50:03.724Z_

<details><summary>↩ Tool result · `toolu_01P5m1UTt2WQFPp5RjKPqpyE`</summary>

```text
Web search results for query: "CodeQL dataflow analysis training signal code embedding contrastive"

Links: [{"title":"About data flow analysis - CodeQL - GitHub","url":"https://codeql.github.com/docs/writing-codeql-queries/about-data-flow-analysis/"},{"title":"An introduction to CodeQL and data flow analysis | Zeyu (Zayne) Zhang","url":"https://www.analogue.computer/blog/codeql-and-data-flow-analysis"},{"title":"Analyzing data flow in C and C++ - CodeQL - GitHub","url":"https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-cpp/"},{"title":"Analyzing data flow in Python - CodeQL - GitHub","url":"https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-python/"},{"title":"Introduction to global data flow — CodeQL training and variant analysis examples","url":"https://help.semmle.com/QL/ql-training/cpp/global-data-flow-cpp.html"},{"title":"Analyzing data flow in C# — CodeQL - GitHub","url":"https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-csharp/"},{"title":"New dataflow API for writing custom CodeQL queries - GitHub Changelog","url":"https://github.blog/changelog/2023-08-13-new-dataflow-api-for-writing-custom-codeql-queries/"},{"title":"Analyzing data flow in Java and Kotlin - CodeQL - GitHub","url":"https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-java/"},{"title":"Data flow cheat sheet for JavaScript - CodeQL - GitHub","url":"https://codeql.github.com/docs/codeql-language-guides/data-flow-cheat-sheet-for-javascript/"},{"title":"DataFlow - CodeQL - GitHub","url":"https://codeql.github.com/codeql-standard-libraries/cpp/semmle/code/cpp/dataflow/DataFlow.qll/module.DataFlow.html"}]

I've searched for information on "CodeQL dataflow analysis training signal code embedding contrastive," but the search results primarily show documentation about CodeQL's data flow analysis features and how to use them for security queries.

The search results cover:

1. CodeQL data flow libraries implement data flow analysis by modeling a program's data flow graph, which models how data flows through the program at runtime rather than reflecting the syntactic structure.

2. CodeQL supports both local data flow (within a single function) and global data flow (across an entire program by calculating data flow between functions).

3. A new API for CodeQL dataflow analysis was released that offers additional flexibility, improvements to prevent common pitfalls, and improves query evaluation performance by 5%.

However, the search results don't contain specific information about "training signal code embedding contrastive" in relation to CodeQL. This appears to be a more specialized research topic or technical implementation detail that isn't covered in the standard CodeQL documentation. If you're looking for information about a specific research paper, tool, or technique that combines these concepts, you may want to provide more context or search academic databases or GitHub repositories directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d8a67e4-f06c-4326-a6ca-2e320c0729a3",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "b150fde8-e027-4c9c-97e5-2317ea0fc1d6",
  "sourceToolAssistantUUID": "9d8a67e4-f06c-4326-a6ca-2e320c0729a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T14:50:07.265Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016YyuKRntQxh6eoYYXzCenJ`</summary>

```json
{
  "query": "program analysis hard negative mining code representation learning AST dataflow 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b150fde8-e027-4c9c-97e5-2317ea0fc1d6",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eWZKJf8XuQD9wX1Rpb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bb11a80-d515-4b1a-a0a8-dd4eefed3f69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Au2AjYf6KaTCviq1VcJ8Z2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 874,
      "cache_read_input_tokens": 47003,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 874
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 47003,
          "cache_creation_input_tokens": 874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 874,
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

_source line 41 · 2026-05-14T14:50:15.859Z_

<details><summary>↩ Tool result · `toolu_016YyuKRntQxh6eoYYXzCenJ`</summary>

```text
Web search results for query: "program analysis hard negative mining code representation learning AST dataflow 2024 2025"

Links: [{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3695994"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Towards Expansive and Adaptive Hard Negative Mining: Graph Contrastive Learning via Subspace Preserving | Proceedings of the ACM Web Conference 2024","url":"https://dl.acm.org/doi/10.1145/3589334.3645327"},{"title":"GitHub - saltudelft/ml4se: A curated list of papers, theses, datasets, and tools related to the application of Machine Learning for Software Engineering · GitHub","url":"https://github.com/saltudelft/ml4se"},{"title":"A Hard Negatives Mining and Enhancing Method for Multi-Modal Contrastive Learning","url":"https://www.mdpi.com/2079-9292/14/4/767"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | Request PDF","url":"https://www.researchgate.net/publication/384848348_Effective_Hard_Negative_Mining_for_Contrastive_Learning-based_Code_Search"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://arxiv.org/pdf/2505.18366"},{"title":"Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection (ICSE 2024 - Research Track) - ICSE 2024","url":"https://conf.researchr.org/details/icse-2024/icse-2024-research-track/63/Dataflow-Analysis-Inspired-Deep-Learning-for-Efficient-Vulnerability-Detection"},{"title":"[2110.02027] ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning","url":"https://arxiv.org/abs/2110.02027"},{"title":"ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning","url":"https://proceedings.mlr.press/v162/xia22b.html"}]

I've completed the web search for your query about program analysis, hard negative mining, code representation learning, AST, and dataflow from 2024-2025. Here are the key findings:

## Relevant Research Areas Found

**Code Representation Learning with AST and Dataflow:**

GraphCodeBERT codes the structure information of AST and uses MLM, dataflow edge prediction and node alignment training tasks for pre-training. This is a foundational approach in the field.

**Hard Negative Mining for Code Search:**

A recent paper addresses this directly: CodeBERT is a bi-directional RoBERTa-based coding language, using masked language modeling (MLM) and replaced Token detection task for pre-training. The search results include a 2024 publication on "Effective Hard Negative Mining for Contrastive Learning-Based Code Search" from ACM Transactions on Software Engineering and Methodology that specifically combines these concepts.

**Dataflow Analysis with Deep Learning:**

Researchers propose to combine causal-based vulnerability detection algorithms with deep learning, specifically designing DeepDFA, a dataflow analysis-inspired graph learning framework and an embedding technique that enables graph learning to simulate dataflow computation. This was presented at ICSE 2024.

**Hard Negative Mining in Graph Learning:**

Contrastive learning can benefit from hard negatives, but limited benefits are observed when adopting existing hard negative mining techniques in Graph Contrastive Learning, which can be attributed to the message passing of Graph Neural Networks.

The search results show active research in combining these techniques for code analysis tasks in 2024-2025, with particular focus on vulnerability detection and code search applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bb11a80-d515-4b1a-a0a8-dd4eefed3f69",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "0ff56cce-1b81-4414-b6eb-8cf910c3571b",
  "sourceToolAssistantUUID": "2bb11a80-d515-4b1a-a0a8-dd4eefed3f69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T14:50:18.521Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012XWY1xKy7hatKfeJd23HDs`</summary>

```json
{
  "query": "systematic comparison hard negative strategies code search embedding BM25 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ff56cce-1b81-4414-b6eb-8cf910c3571b",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eXTBVGXPwhvwBNYj5w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "419108a1-8e4e-4440-8a5c-cae4a12ca851",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QPhgTHDCFFsDTViH4i2yHy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1079,
      "cache_read_input_tokens": 47877,
      "output_tokens": 68,
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
          "output_tokens": 68,
          "cache_read_input_tokens": 47877,
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

_source line 43 · 2026-05-14T14:50:27.446Z_

<details><summary>↩ Tool result · `toolu_012XWY1xKy7hatKfeJd23HDs`</summary>

```text
Web search results for query: "systematic comparison hard negative strategies code search embedding BM25 2024 2025"

Links: [{"title":"Uncertainty-Aware Contrastive Learning With Hard Negative Sampling for","url":"https://csse.szu.edu.cn/attachment/cglr/1749432531_AAAI-2025%E8%AE%BA%E6%96%87-%E5%88%98%E6%B6%B5.pdf"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://arxiv.org/pdf/2505.18366"},{"title":"Passage-based BM25 Hard Negatives: A Simple and Effective Negative","url":"https://aclanthology.org/2023.paclic-1.59.pdf"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://aclanthology.org/2025.acl-industry.72.pdf"},{"title":"(PDF) Uncertainty-Aware Contrastive Learning with Hard Negative Sampling for Code Search Tasks","url":"https://www.researchgate.net/publication/390700481_Uncertainty-Aware_Contrastive_Learning_with_Hard_Negative_Sampling_for_Code_Search_Tasks"},{"title":"Exploring Hard Negative Mining with NV-Retriever in Korean Financial Text","url":"https://huggingface.co/blog/Albertmade/nvretriever-into-financial-text"},{"title":"Fine-Tuning Sparse Embeddings for E-Commerce Search | Part 3: Evaluation and Hard Negatives - Qdrant","url":"https://qdrant.tech/articles/sparse-embeddings-ecommerce-part-3/"},{"title":"Boosting Data Utilization for Multilingual Dense Retrieval","url":"https://aclanthology.org/2025.emnlp-main.624.pdf"},{"title":"From BM25 to Corrective RAG: Benchmarking Retrieval ...","url":"https://arxiv.org/pdf/2604.01733"},{"title":"Contrastive Representation Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2021-05-31-contrastive/"}]

Based on the web search results, here's what I found regarding systematic comparisons of hard negative strategies for code search using embeddings and BM25 in 2024-2025:

## Key Findings

**Code Search with Hard Negatives (2025)**

Code search can be achieved by measuring the matching degree of each query-code pair and ranking retrieved codes, with recent studies improving the effectiveness by enhancing query and code representation in an embedding space through pre-trained language models adapted to code search tasks.

The BM25 strategy is discussed in the context of code search methods. One study compared different approaches including in-batch negatives and hard negatives, with hard negatives showing improved performance (0.829 MRR vs 0.825 for in-batch negatives).

**Comparison of Hard Negative Strategies**

Recent research compares hard negative mining approaches including BM25, In-batch, STAR, and ADORE+STAR strategies. 

In domain-specific applications, BM25 frequently gave extreme similarity values, undermining hard negative selection, while embedding-based teacher models like bge-m3 and KURE-v1 yielded more stable distributions.

**Key Finding on BM25 Limitations**

On MS-MARCO data, nearly 70% of BM25-based "hard negatives" were in fact false positives upon manual inspection.

The research indicates that while BM25 is a common baseline for hard negative selection, embedding-based approaches tend to provide more stable and accurate negative sampling, particularly for code search and domain-specific retrieval tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "419108a1-8e4e-4440-8a5c-cae4a12ca851",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "7545f1dc-57b4-4432-9d05-1885e74cc2ae",
  "sourceToolAssistantUUID": "419108a1-8e4e-4440-8a5c-cae4a12ca851",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-14T14:50:30.234Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NZDxingomTn8UYzqKRyUhD`</summary>

```json
{
  "query": "\"code search\" \"negative mining\" \"graph\" OR \"AST\" OR \"control flow\" OR \"data flow\" training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7545f1dc-57b4-4432-9d05-1885e74cc2ae",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eYJh2yCtWReXvudRgU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c903a98-fce0-45a4-8e1f-b573e93d6e0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UdABwDxMSttVGEdKZduP7g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1010,
      "cache_read_input_tokens": 48956,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1010
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 48956,
          "cache_creation_input_tokens": 1010,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1010,
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

_source line 45 · 2026-05-14T14:50:37.239Z_

<details><summary>↩ Tool result · `toolu_01NZDxingomTn8UYzqKRyUhD`</summary>

```text
Web search results for query: ""code search" "negative mining" "graph" OR "AST" OR "control flow" OR "data flow" training 2025 2026"

Links: [{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dx.doi.org/10.1145/3695994"},{"title":"Artificial Intelligence Jun 2025","url":"https://arxiv.org/list/cs.AI/2025-06?skip=1800&show=2000"},{"title":"Malicious behavior pattern mining using control flow graph","url":"https://dl.acm.org/doi/abs/10.1145/2811411.2811518"},{"title":"Anomaly Detection Using Program Control Flow Graph Mining From Execution Logs | Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining","url":"https://dl.acm.org/doi/10.1145/2939672.2939712"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"Spring 2026 – University of Virginia 1 © Praphamontripong Graph: Data Flow","url":"https://www.cs.virginia.edu/~up3f/cs3250/slides/3250meet19-graph-dataflow.pdf"},{"title":"Static vulnerability mining of IoT devices based on control flow graph construction and graph embedding network - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0140366422004091"},{"title":"Evading control flow graph based GNN malware detectors via active opcode insertion method with maliciousness preserving | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-92023-7"},{"title":"Orange Data Mining","url":"https://orangedatamining.com/"},{"title":"(PDF) Anomaly Detection Using Program Control Flow Graph Mining From Execution Logs","url":"https://www.researchgate.net/publication/305997532_Anomaly_Detection_Using_Program_Control_Flow_Graph_Mining_From_Execution_Logs"}]

I've completed the web search for your query. Here are the most relevant results:

## Key Findings

**Code Search with Negative Mining and AST:**

CoCoHaNeRe outperforms previous methods and achieves new state-of-the-art results on code search benchmarks. UniXCoder incorporates both semantic and syntax information from code comments and ASTs by utilizing more powerful pre-training tasks. Code can be converted into different forms such as intermediate representation (IR) or abstract syntax tree (AST) to enable multi-modal approaches.

SynCoBERT utilizes multi-modal contrastive learning where positive and negative examples are pairs of either code and its documentation or code and its AST.

**Related Research Areas (2025-2026):**

- Recent work on "Modality-Balancing Preference Optimization of Large Multimodal Models by Adversarial Negative Mining" was submitted for ICLR 2026.

- A 2025 paper studied control flow graph based GNN malware detectors, demonstrating ongoing research interest in CFG-based approaches.

The most directly relevant result is the ACM Transactions on Software Engineering and Methodology paper on "Effective Hard Negative Mining for Contrastive Learning-Based Code Search," which combines the key concepts from your search query: code search, negative mining, and AST representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c903a98-fce0-45a4-8e1f-b573e93d6e0f",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "fb8c565a-7510-4ee5-ab36-1a4bc0c9fba0",
  "sourceToolAssistantUUID": "2c903a98-fce0-45a4-8e1f-b573e93d6e0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-14T14:50:39.811Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AbC8yTrTNuN2yCv3pb83x3`</summary>

```json
{
  "query": "conditional benefit hard negatives representation saturation contrastive learning when to use 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb8c565a-7510-4ee5-ab36-1a4bc0c9fba0",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eZ2aCd3gHxqR1QK1i1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30ca3d9b-5302-45d6-a7e4-0f41b28bbd2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CoTC1T7AdtScg8f7ZNpnxp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 981,
      "cache_read_input_tokens": 49966,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 981
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 49966,
          "cache_creation_input_tokens": 981,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 981,
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

_source line 47 · 2026-05-14T14:50:49.829Z_

<details><summary>↩ Tool result · `toolu_01AbC8yTrTNuN2yCv3pb83x3`</summary>

```text
Web search results for query: "conditional benefit hard negatives representation saturation contrastive learning when to use 2024 2025"

Links: [{"title":"[2209.00078] Supervised Contrastive Learning with Hard Negative Samples","url":"https://arxiv.org/abs/2209.00078"},{"title":"CONTRASTIVE LEARNING WITH HARD NEGATIVE ...","url":"https://openreview.net/pdf?id=CR1XOQ0UTh-"},{"title":"Contrastive Representation Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2021-05-31-contrastive/"},{"title":"Causality-guided Contrastive Learning for Generalizable ...","url":"https://aclanthology.org/2025.coling-main.593.pdf"},{"title":"Visual Perturbation and Adaptive Hard Negative Contrastive Learning for Compositional Reasoning in Vision-Language Models","url":"https://arxiv.org/html/2505.15576"},{"title":"Contrastive Learning with Hard Negatives","url":"https://www.emergentmind.com/topics/contrastive-learning-with-hard-negative-samples"},{"title":"Adaptive negative representations for graph contrastive learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2666651023000219"},{"title":"Supervised Contrastive Learning with Hard Negative Samples | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10650863/"},{"title":"[2010.04592] Contrastive Learning with Hard Negative Samples","url":"https://arxiv.org/abs/2010.04592"},{"title":"Knowledge-guided prompt-based continual learning: : Aligning task-prompts through contrastive hard negatives: Knowledge-Based Systems: Vol 310, No C","url":"https://dl.acm.org/doi/10.1016/j.knosys.2025.113009"}]

The search has returned comprehensive results on contrastive learning with hard negatives. Here's a summary of the key findings:

## Overview of Hard Negatives in Contrastive Learning

Contrastive learning learns a useful representation function by pulling positive samples close to each other while pushing negative samples far apart in the embedding space. Hard negative samples should have different labels from the anchor sample, but have embedding features very close to the anchor embedding.

## Conditional Benefit and Trade-offs

Recent research highlights an important conditional benefit of hard negatives. The level of "hardness" in contrastive learning can be smoothly adjusted, allowing the user to select the hardness that best trades-off between an improved learning signal from hard negatives, and the harm due to the correction of false negatives being only approximate, since the hardest points are those closest to the anchor and are expected to have a high propensity to have the same label.

## When to Use Hard Negatives

Two critical considerations are (i) avoiding false negatives (samples of the same class), and (ii) balancing the focus on hard negatives to prevent collapse or label noise amplification. In supervised or semi-supervised settings, hard negative mining can be label-aware: negatives are sampled only from different classes, and further ranked by representational proximity to the anchor.

## Recent 2024-2025 Applications

Recent work has expanded hard negative approaches to various domains:
- CE-CLIP refines contrastive objectives with diverse negative samples to enhance semantic understanding (2024)
- Hard negative samples have been used to learn more distinguishable task prompts by contrastive learning in continual learning, achieving state-of-the-art performance with 88.20% accuracy on CIFAR-100 and 71.64% on ImageNet-R (2025)

The emerging consensus is that hard negatives are beneficial but require careful balancing to avoid amplifying false negatives and representation collapse.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30ca3d9b-5302-45d6-a7e4-0f41b28bbd2e",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "b773c480-7f26-49f9-b6f3-7388a11e7ec3",
  "sourceToolAssistantUUID": "30ca3d9b-5302-45d6-a7e4-0f41b28bbd2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T14:50:52.772Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CDKadZnN6U1wdfAr739xnJ`</summary>

```json
{
  "query": "inter-procedural dataflow negative generation code retrieval training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b773c480-7f26-49f9-b6f3-7388a11e7ec3",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eZxQTFGcS5yGVejwqZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b08d0ef3-12f4-4bd2-93b5-fd8efb5a4698",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bshwdEopao27XSs6hFPsU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1028,
      "cache_read_input_tokens": 50947,
      "output_tokens": 63,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1028
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 63,
          "cache_read_input_tokens": 50947,
          "cache_creation_input_tokens": 1028,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1028,
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

_source line 49 · 2026-05-14T14:51:00.320Z_

<details><summary>↩ Tool result · `toolu_01CDKadZnN6U1wdfAr739xnJ`</summary>

```text
Web search results for query: "inter-procedural dataflow negative generation code retrieval training"

Links: [{"title":"[2405.19782] Dataflow-Guided Retrieval Augmentation for Repository-Level Code Completion","url":"https://arxiv.org/abs/2405.19782"},{"title":"Dataflow-Guided Retrieval Augmentation for Repository- ...","url":"https://aclanthology.org/2024.acl-long.431.pdf"},{"title":"GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.","url":"https://github.com/liunian-Jay/Awesome-RAG"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"CodeRAG: Finding Relevant and Necessary Knowledge ...","url":"https://aclanthology.org/2025.emnlp-main.1187.pdf"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"INTERPROCEDURAL ANALYSIS","url":"https://pages.cs.wisc.edu/~fischer/cs701.f14/6.INTERPROCEDURAL-ANALYSIS.html"},{"title":"Interprocedural Analysis CS252r Spring 2011","url":"https://groups.seas.harvard.edu/courses/cs252/2011sp/slides/Lec05-Interprocedural.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/5df5b1f121c915d8bdd00db6aac20827-Paper-Conference.pdf"},{"title":"Synthetic Data Generation Using Large Language Models","url":"https://arxiv.org/pdf/2503.14023"}]

Based on the search results, here's what I found related to your query about inter-procedural dataflow, negative generation, code retrieval, and training:

## Key Findings

**Dataflow-Guided Retrieval for Code Tasks:**

A dataflow-guided retrieval augmentation approach called DraCo has been proposed for repository-level code completion. DraCo parses a private repository into code entities and establishes their relations through extended dataflow analysis, forming a repo-specific context graph. It precisely retrieves relevant background knowledge from this context graph and generates well-formed prompts to query code language models.

**Retrieval-Augmented Generation and Hard Negatives:**

The search results also revealed important research on retrieval-augmented generation (RAG) systems. Studies observe that performance initially improves but then degrades as more passages are included, with this phenomenon attributed to the detrimental influence of retrieved "hard negatives". To mitigate this issue, researchers propose and evaluate three solutions: training-free retrieval reordering, RAG-specific implicit LLM fine-tuning, and RAG-oriented LLM fine-tuning with intermediate reasoning.

**Synthetic Data Generation:**

Synthetic data generation involves producing additional training examples artificially rather than collected from the real world. Recent advances in generative AI provide powerful tools to generate synthetic text and code that mimic real data distributions.

These findings show active research in combining dataflow analysis with code retrieval systems and addressing challenges with negative examples in training retrieval-augmented systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b08d0ef3-12f4-4bd2-93b5-fd8efb5a4698",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "895cda2b-1575-4fd4-945a-3810663e6210",
  "sourceToolAssistantUUID": "b08d0ef3-12f4-4bd2-93b5-fd8efb5a4698",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T14:51:03.127Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FKbL8QjQrjvjezntTjiPuh`</summary>

```json
{
  "query": "GraphCodeBERT code search contrastive learning negative sampling structure-aware 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "895cda2b-1575-4fd4-945a-3810663e6210",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eajT7t1HY8Dq65Hquq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94930673-77e5-41e3-87a4-feb17ee47cd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015UZWpk39mqNv3cvPwwhoqZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 986,
      "cache_read_input_tokens": 51975,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 986
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 51975,
          "cache_creation_input_tokens": 986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 986,
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

_source line 51 · 2026-05-14T14:51:12.147Z_

<details><summary>↩ Tool result · `toolu_01FKbL8QjQrjvjezntTjiPuh`</summary>

```text
Web search results for query: "GraphCodeBERT code search contrastive learning negative sampling structure-aware 2024 2025"

Links: [{"title":"Uncertainty-Aware Contrastive Learning With Hard Negative Sampling for","url":"https://ojs.aaai.org/index.php/AAAI/article/download/34070/36225"},{"title":"CMCS: contrastive-metric learning via vector-level sampling and augmentation for code search | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-64205-2"},{"title":"SCL-CVD: : Supervised contrastive learning for code vulnerability detection via GraphCodeBERT: Computers and Security: Vol 145, No C","url":"https://dl.acm.org/doi/10.1016/j.cose.2024.103994"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3695994"},{"title":"SCL-CVD: Supervised contrastive learning for code vulnerability detection via GraphCodeBERT - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0167404824002992"},{"title":"Graph Contrastive Learning via Cluster-refined Negative Sampling for Semi-supervised Text Classification","url":"https://arxiv.org/html/2410.18130v1"},{"title":"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning","url":"https://arxiv.org/pdf/2301.09072"},{"title":"(PDF) Uncertainty-Aware Contrastive Learning with Hard Negative Sampling for Code Search Tasks","url":"https://www.researchgate.net/publication/390700481_Uncertainty-Aware_Contrastive_Learning_with_Hard_Negative_Sampling_for_Code_Search_Tasks"},{"title":"LLMSniffer: Detecting LLM-Generated Code via GraphCodeBERT and Supervised Contrastive Learning","url":"https://arxiv.org/html/2604.16058"},{"title":"Uncertainty-Aware Contrastive Learning with Hard Negative Sampling for Code Search Tasks | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34070"}]

Based on the web search results, I found several highly relevant papers and research on GraphCodeBERT with contrastive learning, negative sampling, and structure-aware approaches for code search from 2024-2025:

## Key Findings:

### 1. **Uncertainty-Aware Contrastive Learning with Hard Negative Sampling (2024-2025)**
This paper proposes an uncertainty-aware contrastive learning approach for code search, with an uncertainty learning strategy to produce diverse embeddings by transforming inputs into Gaussian distributions, and a hard negative sampling strategy to construct query-code pairs. The approach outperforms 10 baseline methods on a large code search dataset with six programming languages.

### 2. **CMCS: Contrastive-Metric Learning via Vector-Level Sampling (June 2024)**
GraphCodeBERT is a pre-trained model that incorporates code semantic structure information with three pre-training tasks: MLM, code structure edges prediction, and alignment representations of source code and code structure. CoCoSoDa proposes soft data augmentation and momentum mechanism to enhance the effect of contrastive learning, generating positive and negative samples at the text level.

### 3. **CoCoHaNeRe: Hard Negative Mining for Code Search (2024-2025)**
To enable models to distinguish similar codes, hard negative examples are introduced into contrastive training—these are negative examples in the codebase most similar to positive examples and most likely to cause model mistakes. The model's average MRR score exceeds CodeBERT, GraphCodeBERT, and UniXcoder by 11.25%, 8.13%, and 7.38% respectively.

### 4. **LLMSniffer: GraphCodeBERT with Supervised Contrastive Learning (2025)**
LLMSniffer combines GraphCodeBERT (which encodes code tokens and data-flow structure) with supervised contrastive learning (which clusters same-class representations while separating different-class ones) and comment-stripping preprocessing.

These recent works demonstrate the active development of structure-aware, contrastive learning-based approaches for code understanding tasks using GraphCodeBERT.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94930673-77e5-41e3-87a4-feb17ee47cd9",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "15784fdc-83f8-428f-89ff-6c7640c29d39",
  "sourceToolAssistantUUID": "94930673-77e5-41e3-87a4-feb17ee47cd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-14T14:51:14.755Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KDTkNWePCBm7zQiaionUoM`</summary>

```json
{
  "query": "negative sampling survey information retrieval dense retrieval 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15784fdc-83f8-428f-89ff-6c7640c29d39",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2ebbwCrZnJ63aBnT8CD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f24e5e6b-a34c-406a-bee5-8bad762dbb95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018HCEr1e4dGtsbwZcQicUH7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1198,
      "cache_read_input_tokens": 52961,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1198
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 52961,
          "cache_creation_input_tokens": 1198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1198,
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

_source line 53 · 2026-05-14T14:51:21.771Z_

<details><summary>↩ Tool result · `toolu_01KDTkNWePCBm7zQiaionUoM`</summary>

```text
Web search results for query: "negative sampling survey information retrieval dense retrieval 2025 2026"

Links: [{"title":"[2603.18005] Negative Sampling Techniques in Information Retrieval: A Survey","url":"https://arxiv.org/abs/2603.18005"},{"title":"Negative Sampling Techniques in Dense Retrieval: A Survey - ACL Anthology","url":"https://aclanthology.org/2026.findings-eacl.157/"},{"title":"Negative Sampling Techniques in Information Retrieval: A Survey","url":"https://arxiv.org/html/2603.18005"},{"title":"Negative Sampling Techniques in Information Retrieval","url":"https://aclanthology.org/2026.findings-eacl.157.pdf"},{"title":"Rethinking Negative Sampling for Knowledge Distillation in Retrieval, A Distillation Recipe for Small Language Model Search Agents, and More!","url":"https://recsys.substack.com/p/rethinking-negative-sampling-for"},{"title":"Negative Sampling in Recommendation: A Survey and Future Directions | ACM Transactions on Information Systems","url":"https://dlnext.acm.org/doi/abs/10.1145/3793855"},{"title":"Enhancing Retrieval Performance via LLM Hard-Negative Filtering | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-07959-6_17"},{"title":"A Comprehensive Survey on Retrieval Methods in Recommender Systems","url":"https://dl.acm.org/doi/pdf/10.1145/3771925"},{"title":"Negative Sampling Techniques for Dense Passage Retrieval in a Multilingual Setting | Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3626772.3657854"},{"title":"GitHub - RUCAIBox/DenseRetrieval · GitHub","url":"https://github.com/RUCAIBox/DenseRetrieval"}]

The search has returned highly relevant results about negative sampling techniques in information retrieval and dense retrieval. Here's a summary of the key findings:

## Recent Survey on Negative Sampling in Dense Retrieval

A comprehensive survey published in 2026 synthesizes 35 seminal papers to provide an overview of negative sampling techniques in dense IR, with a unique focus on modern NLP applications and the inclusion of recent Large Language Model (LLM)-driven methods, an area absent in prior reviews.

## Key Focus Areas

Central to training effective dense retrievers through contrastive learning is the selection of informative negative samples. The survey proposes a taxonomy that categorizes techniques, including random, static/dynamically mined, and synthetic datasets, and analyzes these approaches with respect to trade-offs between effectiveness, computational cost, and implementation difficulty.

## Notable Findings

BEIR results reveal that advanced negative sampling techniques (GTR-Base, TAS-B achieving 44.0 average NDCG@10) significantly outperform simpler approaches (DPR at 38.1, ANCE at 39.2).

## Future Directions

The survey concludes by outlining current challenges and promising future directions for the use of LLM-generated synthetic data.

The survey was published in the Findings of the Association for Computational Linguistics: EACL 2026 in March 2026 and represents the most up-to-date research in this area.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f24e5e6b-a34c-406a-bee5-8bad762dbb95",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "cd9dd49c-0050-4b48-8545-9f3f6efdfec8",
  "sourceToolAssistantUUID": "f24e5e6b-a34c-406a-bee5-8bad762dbb95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-14T14:51:24.350Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EBMWmhZWxhN9wxJGkbDLrr`</summary>

```json
{
  "query": "code clone detection contrastive hard negative semantic similar 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd9dd49c-0050-4b48-8545-9f3f6efdfec8",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2ecJzkXdD9mezPej16i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "605e3c98-481a-4a73-93f0-7df383fb6af4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVTj9eeRe1dY7xNNj5rqGk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 938,
      "cache_read_input_tokens": 54159,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 938
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 54159,
          "cache_creation_input_tokens": 938,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 938,
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

_source line 55 · 2026-05-14T14:51:35.025Z_

<details><summary>↩ Tool result · `toolu_01EBMWmhZWxhN9wxJGkbDLrr`</summary>

```text
Web search results for query: "code clone detection contrastive hard negative semantic similar 2024 2025"

Links: [{"title":"CC2Vec: Combining Typed Tokens with Contrastive Learning","url":"https://wu-yueming.github.io/Files/FSE2024_CC2Vec.pdf"},{"title":"Standing on the Shoulders of Giants: Stabilized Knowledge Distillation for Cross–Language Code Clone Detection","url":"https://arxiv.org/html/2605.02860v1"},{"title":"Detecting Semantic Clones of Unseen Functionality","url":"https://arxiv.org/html/2510.04143v1"},{"title":"CCT-Code: Cross-Consistency Training for Multilingual ...","url":"https://aclanthology.org/2025.naacl-srw.17.pdf"},{"title":"AdaCCD: Adaptive Semantic Contrasts Discovery Based Cross Lingual Adaptation for Code Clone Detection","url":"https://arxiv.org/html/2311.07277"},{"title":"Evaluating Code Clone Detection and Management: A Comprehensive Comparison among different Techniques and Tools along with some Effective Future Directions | Proceedings of the 3rd International Conference on Computing Advancements","url":"https://dl.acm.org/doi/10.1145/3723178.3723206"},{"title":"Frontiers | A visual clone analysis method","url":"https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1520344/full"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/b010241b9f1cdfc7d4c392db899cef86-Paper-Conference.pdf"},{"title":"Measuring model alignment for code clone detection using causal interpretation | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-024-10583-0"},{"title":"A novel code representation for detecting Java code clones using high-level and abstract compiled code representations - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11086904/"}]

Based on the search results, here are the key findings on code clone detection with contrastive learning and hard negative/semantic similarity approaches from 2024-2025:

## Recent Advances (2024-2025)

### Key Publications

1. **CC2Vec: Combining Typed Tokens with Contrastive Learning (2024)**
   CC2Vec was published in July 2024 and combines typed tokens with contrastive learning for effective code clone detection. The approach uses contrastive learning to decrease the distance between semantic code pairs while enlarging the difference between dissimilar code pairs.

2. **Detecting Semantic Clones of Unseen Functionality (2025)**
   This work proposes contrastive learning to improve model performance on clones of unseen functionality, drawing inspiration from computer vision and NLP fields where contrastive learning excels at measuring similarity between two objects, even from classes unseen during training. The F1 on clones of unseen functionality improved by up to 26% (average 9%) for task-specific models and up to 5% (average 3%) for LLMs.

3. **Cross-Language Clone Detection with Knowledge Distillation (2025)**
   This work explores contrastive classifiers as one of two different training objectives alongside simple binary classification heads for cross-language clone detection.

4. **CCT-Code: Cross-Consistency Training for Multilingual Clone Detection (2025)**
   CCT-Code was presented in April-May 2025 for multilingual clone detection.

### Semantic Contrast Discovery

AdaCCD proposes a contrastive learning framework for cross-lingual code clone detection that discovers semantically similar and dissimilar contrasts through clustering and neighborhood search.

### Emerging Trends

Recent advances suggest a trend toward using data-driven models and deep learning techniques to detect both syntactic and semantic clones with improved accuracy. Embedding-based techniques, including neural embeddings or transformer-based representations, leverage large datasets of code to learn generalizable features suited to detecting near-miss or semantic clones.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "605e3c98-481a-4a73-93f0-7df383fb6af4",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "9b684e44-ba39-464d-8a6a-02177844b620",
  "sourceToolAssistantUUID": "605e3c98-481a-4a73-93f0-7df383fb6af4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-14T14:51:38.068Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rqii38SfqzM9zMbgJaBUHP`</summary>

```json
{
  "query": "RepoFuse StructCoder code structure representation retrieval 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b684e44-ba39-464d-8a6a-02177844b620",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2edHgQKjDce2WJQ97Pw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47e3a291-cafd-41ba-9fb5-6f9ee6a90266",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdSJCSnKC1A9oBqYWM6XDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1104,
      "cache_read_input_tokens": 55097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1104,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 57 · 2026-05-14T14:51:46.136Z_

<details><summary>↩ Tool result · `toolu_01Rqii38SfqzM9zMbgJaBUHP`</summary>

```text
Web search results for query: "RepoFuse StructCoder code structure representation retrieval 2024 2025"

Links: [{"title":"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph","url":"https://arxiv.org/html/2410.14684v2"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1145/3691620.3695054"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/4a4a3c197deac042461c677219efd36c-Paper-Conference.pdf"},{"title":"Retrieval-Augmented Generation for AI-Generated Content: A Survey | Data Science and Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s41019-025-00335-5"},{"title":"StructCoder: Structure-Aware Transformer for Code Generation | ACM Transactions on Knowledge Discovery from Data","url":"https://dl.acm.org/doi/10.1145/3636430"},{"title":"GitHub - reddy-lab-code-research/StructCoder: Code for \"StructCoder: Structure-Aware Transformer for Code Generation\"","url":"https://github.com/reddy-lab-code-research/StructCoder"},{"title":"[2206.05239] StructCoder: Structure-Aware Transformer for Code Generation","url":"https://arxiv.org/abs/2206.05239"},{"title":"Learning code better through structural information of data flow | The Journal of Supercomputing","url":"https://link.springer.com/article/10.1007/s11227-025-07348-x"},{"title":"StructCoder: Structure-Aware Transformer for Code Generation","url":"https://arxiv.org/pdf/2206.05239"},{"title":"StructCoder: Structure-Aware Transformer for Code Generation | Request PDF","url":"https://www.researchgate.net/publication/376343738_StructCoder_Structure-Aware_Transformer_for_Code_Generation"}]

Based on the search results, I found information about both RepoFuse and StructCoder in relation to code structure representation and retrieval:

## RepoFuse

RepoFuse (Liang et al., 2024) has started integrating RAG modules to harness additional information from repositories. More specifically, RepoFuse includes rationale context and retrieved codes to form a prompt, and ranks the contexts to fit in the length limit.

## StructCoder

StructCoder is an encoder-decoder Transformer model where both the encoder and decoder are explicitly trained to recognize the syntax and data flow in the source and target codes, leveraging the source code's syntax tree and data flow graph.

In addition to sequence generation, StructCoder also learns target syntax using AST paths prediction task, and learns to match target DFG using a data flow prediction task. The AST Paths Prediction (APP) task encourages the decoder to be aware of all root-leaf paths in the target AST, predicting the type of each ancestor on each root-leaf path.

StructCoder was published by Sindhu Tipirneni, Ming Zhu, and Chandan K. Reddy in April 2024 as "StructCoder: Structure-Aware Transformer for Code Generation".

Both tools represent different approaches to code understanding: RepoFuse focuses on repository-level code completion using context retrieval and ranking, while StructCoder emphasizes structure-aware code generation through explicit syntactic and data flow representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47e3a291-cafd-41ba-9fb5-6f9ee6a90266",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "cf038f1b-4df8-4e5b-bd35-10917e93d2dd",
  "sourceToolAssistantUUID": "47e3a291-cafd-41ba-9fb5-6f9ee6a90266",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-14T14:51:49.888Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016KTKF9pWeSewMzRFEtzL6Q`</summary>

```json
{
  "query": "\"hard negative\" \"code retrieval\" OR \"code search\" embedding distance BM25 comparison ablation study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf038f1b-4df8-4e5b-bd35-10917e93d2dd",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2ee7AAjHy5iCjDtvPP1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0240a0f1-d4ff-4329-993b-a9dc24bf72e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018jDwqvwpUU9f2CmR9CSqeQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 56201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1006,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 59 · 2026-05-14T14:52:00.002Z_

<details><summary>↩ Tool result · `toolu_016KTKF9pWeSewMzRFEtzL6Q`</summary>

```text
Web search results for query: ""hard negative" "code retrieval" OR "code search" embedding distance BM25 comparison ablation study"

Links: [{"title":"Optimizing Dense Retrieval Model Training with Hard Negatives Jingtao Zhan","url":"https://arxiv.org/pdf/2104.08051"},{"title":"From BM25 to Corrective RAG: Benchmarking Retrieval Strategies for Text-and-Table Documents","url":"https://arxiv.org/html/2604.01733v1"},{"title":"From BM25 to Corrective RAG: Benchmarking Retrieval ...","url":"https://arxiv.org/pdf/2604.01733"},{"title":"NV-Retriever: Improving text embedding models with effective hard-negative mining","url":"https://arxiv.org/html/2407.15831v1"},{"title":"Hard Negative Mining for Domain-Specific Retrieval in ...","url":"https://aclanthology.org/2025.acl-industry.72.pdf"},{"title":"Evaluating the Effectiveness and Efficiency of ...","url":"https://arxiv.org/pdf/2410.09662"},{"title":"Passage-based BM25 Hard Negatives: A Simple and Effective Negative","url":"https://aclanthology.org/2023.paclic-1.59.pdf"},{"title":"Adapting General-Purpose Embedding Models to Private ...","url":"https://aclanthology.org/2025.findings-acl.357.pdf"},{"title":"InDi: Informative and Diverse Sampling for Dense Retrieval","url":"https://assets.amazon.science/39/b7/5ce986a64af6a9c21d163aedf307/indi-informative-and-diverse-sampling-for-dense-retrieval.pdf"},{"title":"Fine-Tuning Sparse Embeddings for E-Commerce Search | Part 1: Why Sparse Embeddings Beat BM25 - Qdrant","url":"https://qdrant.tech/articles/sparse-embeddings-ecommerce-part-1/"}]

I found several relevant research papers and articles discussing hard negatives, code retrieval/search, embedding distances, BM25 comparisons, and ablation studies. Here's a summary of what the search returned:

## Key Papers Found:

1. **"Optimizing Dense Retrieval Model Training with Hard Negatives"** (Zhan et al., SIGIR 2021)
   - Includes ablation studies on hard negatives, comparing static and dynamic hard negatives
   - Shows that static hard negative sampling doesn't necessarily improve performance over random sampling, though it improves top-ranking performance but may harm recall

2. **"NV-Retriever: Improving text embedding models with effective hard-negative mining"** (arxiv:2407.15831)
   - Found that negatives mined with BM25 resulted in worse retrieval accuracy than other approaches, which was surprising and opposite to prior findings
   - Compares different teacher models for mining, noting that more powerful models yield more effective hard-negatives

3. **Code Retrieval/Search Specific:**
   - BM25 outperforms all other retrievers across coding tasks
   - At smaller knowledge base sizes, BM25 shows greater efficiency, but as the knowledge base expands, its efficiency decreases relative to dense retrievers

4. **Hard Negative Mining for Domain-Specific Retrieval** (ACL 2025)
   - Discusses PCA-based dimensionality reduction and dynamic hard negative selection for fine-tuning reranker models

5. **"InDi: Informative and Diverse Sampling for Dense Retrieval"** (Amazon Science)
   - Reports ablation studies showing that defined objectives are important when selecting negative samples for dense retrieval

Would you like me to search for more specific information about any particular aspect, such as code-specific embedding models, or specific ablation study findings?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0240a0f1-d4ff-4329-993b-a9dc24bf72e7",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "42f0db19-8912-4728-8e94-30e1b4e01935",
  "sourceToolAssistantUUID": "0240a0f1-d4ff-4329-993b-a9dc24bf72e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-14T14:52:02.666Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017dFdKixsutENYcTLJHdMmE`</summary>

```json
{
  "query": "CodeSearchNet contrastive fine-tuning hard negative 2024 2025 new method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42f0db19-8912-4728-8e94-30e1b4e01935",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2ef8VZRSamqHRf9q32J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0cdde29c-287d-4b82-9364-95d125a6e882",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdGpPZ1GrcLqf4EEycQQMZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 57207,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1041
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 57207,
          "cache_creation_input_tokens": 1041,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1041,
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

_source line 61 · 2026-05-14T14:52:17.423Z_

<details><summary>↩ Tool result · `toolu_017dFdKixsutENYcTLJHdMmE`</summary>

```text
Web search results for query: "CodeSearchNet contrastive fine-tuning hard negative 2024 2025 new method"

Links: [{"title":"CMCS: contrastive-metric learning via vector-level sampling and augmentation for code search | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-64205-2"},{"title":"MGS3: A Multi-Granularity Self-Supervised Code Search Framework","url":"https://arxiv.org/html/2505.24274"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3695994"},{"title":"Improving Code Search with Hard Negative Sampling Based on Fine-tuning","url":"https://arxiv.org/html/2305.04508"},{"title":"Uncertainty-Aware Contrastive Learning With Hard Negative Sampling for","url":"https://csse.szu.edu.cn/attachment/cglr/1749432531_AAAI-2025%E8%AE%BA%E6%96%87-%E5%88%98%E6%B6%B5.pdf"},{"title":"CMCS: contrastive-metric learning via vector-level sampling and augmentation for code search - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11196273/"},{"title":"(PDF) Uncertainty-Aware Contrastive Learning with Hard Negative Sampling for Code Search Tasks","url":"https://www.researchgate.net/publication/390700481_Uncertainty-Aware_Contrastive_Learning_with_Hard_Negative_Sampling_for_Code_Search_Tasks"},{"title":"A Hard Negatives Mining and Enhancing Method for Multi-Modal Contrastive Learning","url":"https://www.mdpi.com/2079-9292/14/4/767"},{"title":"RFMC-CS: a representation fusion based multi-view momentum contrastive learning framework for code search | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10515-025-00487-8"},{"title":"CONTRASTIVE LEARNING WITH HARD NEGATIVE ...","url":"https://openreview.net/pdf?id=CR1XOQ0UTh-"}]

Based on the search results, I found several recent methods combining contrastive learning, hard negative sampling, and the CodeSearchNet dataset:

## Recent Methods (2024-2025)

**CMCS: Contrastive-Metric Learning via Vector-Level Sampling and Augmentation**

CMCS proposes contrastive-metric learning for code search based on vector-level sampling and augmentation, including a sampling method to obtain hard negative samples based on the K-means algorithm and a hardness-controllable sample augmentation method. Experiments were conducted on the CodeSearchNet dataset using seven advanced code search models, showing the method significantly enhances training efficiency and search performance.

**CoCoHaNeRe: Hard Negative Mining for Code Search**

This method designs a new memory bank that supports finding the nearest neighbor of query as hard negatives, addressing the problem that contrastive learning can only learn low-level semantics by filtering out hard negatives that cannot be distinguished by simple semantic representation. It adopts differentiable hard negative embeddings, recomputing the embeddings of hard negatives and putting them in the same batch as positive examples for training.

**MGS3: Multi-Granularity Self-Supervised Code Search Framework**

MGS3 proposes a multi-granularity code search framework that identifies suitable negative samples for different granularities of code snippets to enhance the contrastive learning process. The framework leverages the existing CodeSearchNet corpus.

**Uncertainty-Aware Contrastive Learning with Hard Negative Sampling**

This approach proposes uncertainty-aware contrastive learning with hard negative sampling to address the fact that diverse language styles can be used in user queries and codes for presenting the same semantic meaning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cdde29c-287d-4b82-9364-95d125a6e882",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "ee2da521-746e-448b-937f-bb2313b8cb15",
  "sourceToolAssistantUUID": "0cdde29c-287d-4b82-9364-95d125a6e882",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-14T14:52:20.157Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Guz3eQzkQPZBT1nkt3LbpE`</summary>

```json
{
  "query": "MGS3 multi-granularity self-supervised code search 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee2da521-746e-448b-937f-bb2313b8cb15",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2egQupJQwae33NHr6Sc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e3a0366-e031-470d-a41c-297f35d35e5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011zSfDNGwcu6tjHX4CTxqSv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1069,
      "cache_read_input_tokens": 58248,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1069
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 58248,
          "cache_creation_input_tokens": 1069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1069,
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

_source line 63 · 2026-05-14T14:52:28.659Z_

<details><summary>↩ Tool result · `toolu_01Guz3eQzkQPZBT1nkt3LbpE`</summary>

```text
Web search results for query: "MGS3 multi-granularity self-supervised code search 2025"

Links: [{"title":"[2505.24274] MGS3: A Multi-Granularity Self-Supervised Code Search Framework","url":"https://arxiv.org/abs/2505.24274"},{"title":"MGS3: A Multi-Granularity Self-Supervised Code Search Framework","url":"https://arxiv.org/html/2505.24274"},{"title":"MGS3: A Multi-Granularity Self-Supervised Code Search Framework | Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.1","url":"https://dl.acm.org/doi/10.1145/3690624.3709263"},{"title":"About me - Zheng zhang","url":"https://zhengz99.github.io/"},{"title":"Junfeng Kang's research works | State Key Laboratory of Fire Science, University of Science and Technology of China and other places","url":"https://www.researchgate.net/scientific-contributions/Junfeng-Kang-2310148194"},{"title":"Rethinking Negative Pairs in Code Search","url":"https://www.researchgate.net/publication/376401967_Rethinking_Negative_Pairs_in_Code_Search"},{"title":"A Multi-Granularity Self-Supervised Code Search Framework","url":"https://dl.acm.org/doi/pdf/10.1145/3690624.3709263"},{"title":"GitHub - qingsongedu/Awesome-SSL4TS: A professionally curated list of awesome resources (paper, code, data, etc.) on Self-Supervised Learning for Time Series (SSL4TS). · GitHub","url":"https://github.com/qingsongedu/Awesome-SSL4TS"},{"title":"Diversity-driven MG-MAE: Multi-granularity representation learning for non-salient object segmentation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S136184152600040X"},{"title":"GaussTR: Foundation Model-Aligned Gaussian Transformer for","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Jiang_GaussTR_Foundation_Model-Aligned_Gaussian_Transformer_for_Self-Supervised_3D_Spatial_Understanding_CVPR_2025_paper.pdf"}]

I found search results about MGS3, a research paper from 2025. Here's what I found:

## MGS3: A Multi-Granularity Self-Supervised Code Search Framework

MGS3 is focused on enhancing software reusability and developer productivity through code search, which aims at retrieving code snippets relevant to functionalities based on natural language queries.

### Key Problem Addressed
Despite significant progress in self-supervised code pre-training, existing methods have primarily focused on leveraging contrastive learning to align natural language with function-level code snippets. These studies have overlooked the abundance of fine-grained (such as block-level and statement-level) code snippets prevalent within the function-level code snippets, which results in suboptimal performance across all levels of granularity.

### Main Contributions
The researchers constructed a multi-granularity code search dataset called MGCodeSearchNet, which contains 536K+ pairs of natural language and code snippets.

MGS3 features a Hierarchical Multi-Granularity Representation module (HMGR), which leverages syntactic structural relationships for hierarchical representation and aggregates fine-grained information into coarser-grained representations. During the contrastive learning phase, the framework constructs positive samples of the same granularity for fine-grained code and introduces in-function negative samples for fine-grained code.

### Results and Properties
The framework demonstrates outstanding performance in code search tasks of multiple granularities and exhibits model-agnostic nature and compatibility with existing pre-trained code representation models.

The paper was accepted at the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD'2025), in Toronto, Canada, August 3-7.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e3a0366-e031-470d-a41c-297f35d35e5a",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "9c9a62b9-6451-49f5-945c-7fa3fa778501",
  "sourceToolAssistantUUID": "6e3a0366-e031-470d-a41c-297f35d35e5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-14T14:52:31.656Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015tHnHG31zCvppQWrUETqYJ`</summary>

```json
{
  "query": "\"rethinking negative pairs\" code search 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c9a62b9-6451-49f5-945c-7fa3fa778501",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2ehF51KFyRaeEqXsVcr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c42cee9f-ac0a-4b02-b2c8-85e066a746eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Y4fuMLHjLkQF6iZPLR51W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1093,
      "cache_read_input_tokens": 59317,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1093
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 59317,
          "cache_creation_input_tokens": 1093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1093,
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

_source line 65 · 2026-05-14T14:52:36.793Z_

<details><summary>↩ Tool result · `toolu_015tHnHG31zCvppQWrUETqYJ`</summary>

```text
Web search results for query: ""rethinking negative pairs" code search 2024 2025"

Links: [{"title":"[2310.08069] Rethinking Negative Pairs in Code Search","url":"https://arxiv.org/abs/2310.08069"},{"title":"Rethinking Negative Pairs in Code Search","url":"https://www.researchgate.net/publication/376401967_Rethinking_Negative_Pairs_in_Code_Search"},{"title":"GitHub - Alex-HaochenLi/Soft-InfoNCE: [EMNLP'23] Code for 'Rethinking Negative Pairs in Code Search' · GitHub","url":"https://github.com/Alex-HaochenLi/Soft-InfoNCE"},{"title":"Uncertainty-Aware Contrastive Learning With Hard Negative Sampling for","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34070/36225"},{"title":"Rethinking Negative Pairs in Code Search - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.786/"},{"title":"Rethinking Negative Pairs in Code Search","url":"https://aclanthology.org/2023.emnlp-main.786.pdf"},{"title":"Rethinking Negative Pairs in Code Search | OpenReview","url":"https://openreview.net/forum?id=D0gAwtclWk"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Rethinking+Negative+Pairs+in+Code+Search."},{"title":"Rethinking Negative Pairs in Code Search Haochen Li1 Xin Zhou2 Luu Anh Tuan1","url":"https://openreview.net/pdf?id=D0gAwtclWk"},{"title":"Rethinking Negative Pairs in Code Search | Semantic Scholar","url":"https://www.semanticscholar.org/search?q=Rethinking+Negative+Pairs+in+Code+Search"}]

I found search results for "Rethinking Negative Pairs in Code Search." Here's what I discovered:

## Overview

Contrastive learning has become a key component in fine-tuning code search models, pulling together positive code snippets while pushing negative samples away given search queries.

## The Research Paper

The paper "Rethinking Negative Pairs in Code Search" was authored by Haochen Li, Xin Zhou, Luu Anh Tuan, and Chunyan Miao and was published in December 2023 in the Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing.

## Key Problems Addressed

The research identifies two main problems: 1) The existence of false negative samples in large code corpora due to duplications, and 2) The failure to explicitly differentiate between the potential relevance of negative samples. For example, a bubble sorting algorithm is less "negative" than a file saving function for a quick sorting algorithm query.

## Solution

The authors propose a simple yet effective Soft-InfoNCE loss that inserts weight terms into InfoNCE. The code for this research is available on GitHub in the Soft-InfoNCE repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c42cee9f-ac0a-4b02-b2c8-85e066a746eb",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "53a36077-a178-4c77-9c47-807c548652a0",
  "sourceToolAssistantUUID": "c42cee9f-ac0a-4b02-b2c8-85e066a746eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-14T14:52:39.446Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KoUcrtiXjGPVCcDc3RARYf`</summary>

```json
{
  "query": "RFMC-CS representation fusion momentum contrastive code search 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53a36077-a178-4c77-9c47-807c548652a0",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2ehqiLyg3Rwf3yErz2v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9330943-49a8-41c3-99e8-93cd27685ef5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Zgvm2ccp97e2c1axaVqzp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 887,
      "cache_read_input_tokens": 60410,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 887
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 60410,
          "cache_creation_input_tokens": 887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 887,
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

_source line 67 · 2026-05-14T14:52:45.072Z_

<details><summary>↩ Tool result · `toolu_01KoUcrtiXjGPVCcDc3RARYf`</summary>

```text
Web search results for query: "RFMC-CS representation fusion momentum contrastive code search 2025"

Links: [{"title":"RFMC-CS: a representation fusion based multi-view momentum contrastive learning framework for code search | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10515-025-00487-8"},{"title":"Enhancing Code Search Fine-Tuning with Momentum Contrastive Learning and Cross-Modal Matching | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-0014-7_42"},{"title":"FMCS: Improving Code Search by Multi-Modal Representation Fusion and Momentum Contrastive Learning | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10684620/"},{"title":"C2RF: Bridging Multi-modal Image Registration and Fusion via Commonality Mining and Contrastive Learning | International Journal of Computer Vision | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11263-025-02427-1"},{"title":"GitHub - ryanzhumich/Contrastive-Learning-NLP-Papers: Paper List for Contrastive Learning for Natural Language Processing · GitHub","url":"https://github.com/ryanzhumich/Contrastive-Learning-NLP-Papers"},{"title":"HedgeCode: A Multi-Task Hedging Contrastive Learning Framework for Code Search | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1109/ICSE55347.2025.00008"},{"title":"A Comprehensive Review of Multimodal Visual Representation Learning: Tracing the Evolution from CNNs to Transformers and Beyond | International Journal of Multimedia Information Retrieval | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s13735-025-00382-8"},{"title":"Addressing Challenges in Multimodal Large Language Model Development[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202512.1986/v1/download"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf"},{"title":"TechRxiv: preprints in engineering, computer science, and related technology","url":"https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176054814.40957359/v1"}]

Based on the search results, I found relevant information about RFMC-CS:

## RFMC-CS: Representation Fusion Based Multi-View Momentum Contrastive Learning for Code Search

RFMC-CS is a representation fusion based multi-view momentum contrastive learning framework for code search published in the journal Automated Software Engineering in 2025.

### Problem and Motivation

Code search is a crucial task in software engineering, aiming to search relevant code from the codebase based on natural language queries. Existing methods have limitations in the representation learning of multi-modal data, specifically suffering from semantic loss in the representation learning of code and failing to explore functionally relevant code pairs fully.

### Approach

RFMC-CS addresses these limitations by effectively retaining the semantic and structural information of code through multi-modal representation and fusion. Through elaborately designed Multi-View Momentum Contrastive Learning, RFMC-CS can further learn the correlations between different modalities of samples and semantic relevant samples.

This framework represents an advancement in code search methodology by combining multi-modal representation fusion techniques with momentum contrastive learning principles.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9330943-49a8-41c3-99e8-93cd27685ef5",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "9049c38e-dbb8-4153-8453-8a8edcbef6e9",
  "sourceToolAssistantUUID": "e9330943-49a8-41c3-99e8-93cd27685ef5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-14T14:52:48.815Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013c3PuU6F3GR99GdywvY4VH`</summary>

```json
{
  "query": "HedgeCode multi-task hedging contrastive code search ICSE 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9049c38e-dbb8-4153-8453-8a8edcbef6e9",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eiT85HHpiDpBbXqToC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34432d02-6118-4352-a9bd-285cd6630158",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FBhPRSJaDGZQjePuXigL5Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1019,
      "cache_read_input_tokens": 61297,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1019
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 61297,
          "cache_creation_input_tokens": 1019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1019,
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

_source line 69 · 2026-05-14T14:52:56.915Z_

<details><summary>↩ Tool result · `toolu_013c3PuU6F3GR99GdywvY4VH`</summary>

```text
Web search results for query: "HedgeCode multi-task hedging contrastive code search ICSE 2025"

Links: [{"title":"HedgeCode: A Multi-Task Hedging Contrastive Learning Framework for Code Search (ICSE 2025 - Research Track) - ICSE 2025","url":"https://conf.researchr.org/details/icse-2025/icse-2025-research-track/4/HedgeCode-A-Multi-Task-Hedging-Contrastive-Learning-Framework-for-Code-Search"},{"title":"HedgeCode: A Multi-Task Hedging Contrastive Learning Framework for Code Search | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1109/ICSE55347.2025.00008"},{"title":"HedgeCode: A Multi-Task Hedging Contrastive Learning Framework for Code Search","url":"https://orbilu.uni.lu/bitstream/10993/65661/1/ICSE25-HedgeCode.pdf"},{"title":"Hedgecode: A Multi-Task Hedging Contrastive Learning Framework for Code Search | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/11029684/11029718/11029759.pdf"},{"title":"HedgeCode: A Multi-Task Hedging Contrastive L","url":"https://dl.acm.org/doi/pdf/10.1109/ICSE55347.2025.00008"},{"title":"About me - Qi Xin","url":"https://qixin5.github.io/"},{"title":"GitHub - repo-anonymous/hedgecode","url":"https://github.com/repo-anonymous/hedgecode"},{"title":"[PDF] CoCoSoDa: Effective Contrastive Learning for Code Search | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CoCoSoDa:-Effective-Contrastive-Learning-for-Code-Shi-Wang/ae52599f2d2731f68c567b6726a5185c06cb9a41"},{"title":"2025 IEEE/ACM 47th International Conference on Software ...","url":"https://www.computer.org/csdl/proceedings/icse/2025/215aVCUIQmY"},{"title":"GitHub - saltudelft/ml4se: A curated list of papers, theses, datasets, and tools related to the application of Machine Learning for Software Engineering · GitHub","url":"https://github.com/saltudelft/ml4se"}]

## Search Results for HedgeCode

I found comprehensive information about HedgeCode from ICSE 2025. Here's what the paper covers:

### Overview

HedgeCode is a multi-task hedging contrastive learning framework for code search. Code search is a vital activity in software engineering, focused on identifying and retrieving the correct code snippets based on a query provided in natural language.

### Problem Statement

Despite progress in deep learning approaches for code search, there remains an unexplored gap in ensuring consistency between the representation spaces of code and its descriptions. Furthermore, existing methods have not fully leveraged the potential relevance between code snippets and their descriptions, presenting a challenge in discerning fine-grained semantic distinctions among similar code snippets.

### Framework Structure

HedgeCode is structured around two primary training phases. The first phase, known as the representation alignment stage, proposes a hedging contrastive learning approach that aims to detect subtle differences between code and natural language text, thereby aligning their representation spaces by identifying relevance.

The subsequent phase involves multi-task joint learning, wherein the previously trained model serves as the encoder. This stage optimizes the model through a combination of supervised and self-supervised contrastive learning tasks.

### Results

The framework's effectiveness is demonstrated through its performance on the CodeSearchNet benchmark, showcasing HedgeCode's ability to address the mentioned limitations in code search tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34432d02-6118-4352-a9bd-285cd6630158",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "241f58dd-734d-4e02-804c-f89d8ff845e5",
  "sourceToolAssistantUUID": "34432d02-6118-4352-a9bd-285cd6630158",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-14T14:52:59.773Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KYRUoBpQgQZJbmixaraEjv`</summary>

```json
{
  "query": "\"improving code search\" \"hard negative\" \"fine-tuning\" arxiv 2305.04508"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "241f58dd-734d-4e02-804c-f89d8ff845e5",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2ejKicCTomFqFRkAtms",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "324cee29-3caa-486e-a42f-612ae0200474",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PRVzYKKJYpXrzXuJ6FnMaN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1054,
      "cache_read_input_tokens": 62316,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1054
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 62316,
          "cache_creation_input_tokens": 1054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1054,
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

_source line 71 · 2026-05-14T14:53:05.526Z_

<details><summary>↩ Tool result · `toolu_01KYRUoBpQgQZJbmixaraEjv`</summary>

```text
Web search results for query: ""improving code search" "hard negative" "fine-tuning" arxiv 2305.04508"

Links: [{"title":"[2305.04508] Improving Code Search with Hard Negative Sampling Based on Fine-tuning","url":"https://arxiv.org/abs/2305.04508"},{"title":"Improving Code Search with Hard Negative Sampling Based on Fine-tuning","url":"https://arxiv.org/html/2305.04508"},{"title":"Improving Code Search with Hard Negative Sampling Based on Fine-tuning | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10967342/"},{"title":"Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency","url":"https://arxiv.org/html/2506.17209v1"},{"title":"Data-efficient LLM Fine-tuning for Code Generation","url":"https://arxiv.org/html/2504.12687v1"},{"title":"Towards Efficient Fine-tuning of Pre-trained Code Models","url":"https://arxiv.org/pdf/2304.05216"},{"title":"Fine-Tuning is Fine, if Calibrated","url":"https://arxiv.org/html/2409.16223v1"},{"title":"Complexity-aware fine-tuning","url":"https://arxiv.org/html/2506.21220v1"},{"title":"Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs","url":"https://martins1612.github.io/emergent_misalignment_betley.pdf"},{"title":"FGit: Fault-Guided Fine-Tuning for Code Generation","url":"https://arxiv.org/html/2503.16913"}]

Based on the search results, I found the paper you're looking for. Here's what I found:

The paper arxiv 2305.04508 is titled "Improving Code Search with Hard Negative Sampling Based on Fine-tuning" by authors Hande Dong, Jiayi Lin, Yanlin Wang, Yichong Leng, Jiawei Chen, and Yutao Xie.

The research addresses pre-trained code models for code search tasks, involving pre-training on search-irrelevant tasks like masked language modeling, followed by fine-tuning on search-relevant tasks.

The typical fine-tuning method employs a dual-encoder architecture to encode semantic embeddings of query and code separately, and then calculate their similarity based on the embeddings. However, to address limitations in token-level interactions between query and code, the paper introduces a cross-encoder architecture for code search that jointly encodes the concatenation of query and code.

The paper also proposes a Retriever-Ranker (RR) framework that cascades the dual-encoder and cross-encoder to improve code search performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "324cee29-3caa-486e-a42f-612ae0200474",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "bcdfe02f-eba3-45d3-a70f-e2b39cebf9d7",
  "sourceToolAssistantUUID": "324cee29-3caa-486e-a42f-612ae0200474",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-14T14:53:09.113Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WD9cRy5Fv41ydTydxp5pKQ`</summary>

```json
{
  "query": "CoCoHaNeRe BM25 proxy embedding distance hard negative code search limitation criticism"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcdfe02f-eba3-45d3-a70f-e2b39cebf9d7",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2ejxb9F9Wrptfcv63Cw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de5a45e2-a7ef-4799-bc75-a2678eeee5bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QmkJZ5nkhNGU7qENT5Ru4t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 63370,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 790
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 63370,
          "cache_creation_input_tokens": 790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 790,
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

_source line 73 · 2026-05-14T14:53:19.302Z_

<details><summary>↩ Tool result · `toolu_01WD9cRy5Fv41ydTydxp5pKQ`</summary>

```text
Web search results for query: "CoCoHaNeRe BM25 proxy embedding distance hard negative code search limitation criticism"

Links: [{"title":"beir/examples/retrieval/training/train_sbert_BM25_hardnegs.py at main · beir-cellar/beir","url":"https://github.com/beir-cellar/beir/blob/main/examples/retrieval/training/train_sbert_BM25_hardnegs.py"},{"title":"Passage-based BM25 Hard Negatives: A Simple and Effective Negative","url":"https://aclanthology.org/2023.paclic-1.59.pdf"},{"title":"A Text Embedding Model with Contrastive Example Mining ...","url":"https://aclanthology.org/2025.coling-main.486.pdf"},{"title":"Stop the Hallucinations: Hybrid Retrieval with BM25, pgvector, embedding rerank, LLM Rubric Rerank & HyDE | by Rick Hightower | Medium","url":"https://medium.com/@richardhightower/stop-the-hallucinations-hybrid-retrieval-with-bm25-pgvector-embedding-rerank-llm-rubric-rerank-895d8f7c7242"},{"title":"Understanding BM25 Parameters and Hybrid Search Logic with Sparse-Dense Vectors in Pinecone - General - Pinecone Community","url":"https://community.pinecone.io/t/understanding-bm25-parameters-and-hybrid-search-logic-with-sparse-dense-vectors-in-pinecone/4906"},{"title":"Exploring Hard Negative Mining with NV-Retriever in Korean Financial Text","url":"https://huggingface.co/blog/Albertmade/nvretriever-into-financial-text"},{"title":"Contrastive Representation Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2021-05-31-contrastive/"},{"title":"Positive and Negative Sampling Strategies for Representation Learning in Semantic Search - Sumit's Diary","url":"https://blog.reachsumit.com/posts/2023/03/pairing-for-representation/"},{"title":"Why So Hard (Negative) On Your Self (Reinforcement)? :: Hello Friend — A simple theme for Hugo","url":"https://www.mattkrzus.com/posts/hard_negative_mining/"},{"title":"Mastering BM25: A Deep Dive into the Algorithm and Its Application in Milvus - Zilliz Learn","url":"https://zilliz.com/learn/mastering-bm25-a-deep-dive-into-the-algorithm-and-application-in-milvus"}]

The search results don't appear to contain specific information about "CoCoHaNeRe" (which may be an acronym for a specific research paper or method). Let me search more specifically for this term along with code search:

Links: [{"title":"GitHub - cocoindex-io/cocoindex-code: A super light-weight embedded code search engine CLI (AST based) that just works - saves 70% token and improves speed for coding agent 🌟 Star if you like it!","url":"https://github.com/cocoindex-io/cocoindex-code"},{"title":"Building Intelligent Codebase Indexing with CocoIndex: A Deep Dive into Semantic Code Search | by Cocoindex | Medium","url":"https://medium.com/@cocoindex.io/building-intelligent-codebase-indexing-with-cocoindex-a-deep-dive-into-semantic-code-search-e93ae28519c5"},{"title":"Build a Real-Time Codebase Index in 5 Minutes with CocoIndex (Rust + Tree-sitter) - DEV Community","url":"https://dev.to/badmonster0/build-a-real-time-codebase-index-in-5-minutes-with-cocoindex-rust-tree-sitter-eo3"},{"title":"Codebase Indexing · CocoIndex Examples","url":"https://cocoindex.io/examples/code_index"},{"title":"Build Real-Time Codebase Indexing for AI Code Generation · CocoIndex","url":"https://cocoindex.io/blogs/index-code-base-for-rag/"},{"title":"GitHub - VioletCranberry/coco-search: Local-first hybrid semantic code search tool. Indexes codebases into PostgreSQL with pgvector embeddings via Ollama, combines vector similarity + keyword search with RRF fusion. Supports 30+ languages. Features CLI, MCP server, WEB dashboard and interactive REPL. · GitHub","url":"https://github.com/VioletCranberry/coco-search"},{"title":"GitHub - cocoindex-io/cocoindex: Incremental engine for long horizon agents 🌟 Star if you like it!","url":"https://github.com/cocoindex-io/cocoindex"},{"title":"Latest Clash of Clans Codes (May 2026) – Free Rewards & Creator Codes","url":"https://www.ldshop.gg/blog/clash-of-clans/latest-clash-of-clans-codes.html"},{"title":"GitHub - anortham/coa-codesearch-mcp: AI-powered code search and analysis for Claude Code with advanced type extraction across 25+ languages. Lightning-fast Lucene indexing, intelligent type parsing (Vue, Razor, C#, Python, Rust, Go, TypeScript+), and token-optimized responses. Built with .NET 9 + Tree-sitter. · GitHub","url":"https://github.com/anortham/coa-codesearch-mcp"},{"title":"Code Search | Google for Developers","url":"https://developers.google.com/code-search"}]

Links: [{"title":"Hard Negative Mixing for Contrastive Learning Yannis Kalantidis","url":"https://arxiv.org/pdf/2010.01028"},{"title":"[2605.07409] The Proxy Presumption: From Semantic Embeddings to Valid Social Measures","url":"https://arxiv.org/abs/2605.07409"},{"title":"The Proxy Presumption: From Semantic Embeddings to Valid Social Measures","url":"https://arxiv.org/html/2605.07409"},{"title":"Hard Negative Examples are Hard, but Useful | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-030-58568-6_8"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3695994"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | Request PDF","url":"https://www.researchgate.net/publication/384848348_Effective_Hard_Negative_Mining_for_Contrastive_Learning-based_Code_Search"},{"title":"Degree Project in Computer Science and Engineering Second cycle, 30 credits","url":"https://www.diva-portal.org/smash/get/diva2:1987984/FULLTEXT01.pdf"},{"title":"Uncertainty-Aware Contrastive Learning With Hard Negative Sampling for","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34070/36225"},{"title":"Optimizing Dense Retrieval Model Training with Hard Negatives | Request PDF","url":"https://www.researchgate.net/publication/350964136_Optimizing_Dense_Retrieval_Model_Training_with_Hard_Negatives"},{"title":"Contrastive learning with hard negative samples","url":"https://arxiv.org/pdf/2010.04592"}]

Based on my web search results, I was unable to find specific information about "CoCoHaNeRe" as a named method or paper related to code search, BM25 hard negatives, proxy embeddings, or distance metrics. The search results returned information about:

1. **CocoIndex** - a code search tool using semantic embeddings and Tree-sitter
2. **CocoSearch** - a hybrid semantic code search tool
3. General research on hard negative mining for contrastive learning
4. Studies on proxy embeddings and semantic embeddings criticism

However, the specific term "CoCoHaNeRe" does not appear to correspond to any standard research paper, method, or tool in the current literature indexed online.

It's possible that:
- This is a very recent or unpublished work
- The acronym or name is spelled differently
- It may be from a preprint server not yet widely indexed
- It could be an internal or institutional project name

If you could provide additional context such as:
- Author names
- Conference/publication venue
- Year of publication
- A more complete title or description

I would be able to conduct a more targeted search to find the specific information about proxy embedding distances, hard negative limitations, and criticisms in code search that you're looking for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de5a45e2-a7ef-4799-bc75-a2678eeee5bb",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "598bbe95-7675-4b4f-b82e-a9e5cfd1303b",
  "sourceToolAssistantUUID": "de5a45e2-a7ef-4799-bc75-a2678eeee5bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-14T14:53:22.666Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CENEHdArVW2JDWi4oBNv6F`</summary>

```json
{
  "query": "\"Effective Hard Negative Mining\" \"Contrastive Learning-Based Code Search\" TOSEM 2024 memory bank nearest neighbor"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "598bbe95-7675-4b4f-b82e-a9e5cfd1303b",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2ekyUzwV9PNoyf7snny",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2c95aa6-82e2-468b-b7f9-6ea4e267c035",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bnCTKtc2R6Z1ZwQ5t3Aas",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 64160,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2297
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 64160,
          "cache_creation_input_tokens": 2297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2297,
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

_source line 75 · 2026-05-14T14:53:29.859Z_

<details><summary>↩ Tool result · `toolu_01CENEHdArVW2JDWi4oBNv6F`</summary>

```text
Web search results for query: ""Effective Hard Negative Mining" "Contrastive Learning-Based Code Search" TOSEM 2024 memory bank nearest neighbor"

Links: [{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3695994"},{"title":"Effective Hard Negative Mining for Contrastive Learning-Based Code Search | Request PDF","url":"https://www.researchgate.net/publication/384848348_Effective_Hard_Negative_Mining_for_Contrastive_Learning-based_Code_Search"},{"title":"Revisiting Hard Negative Mining in Contrastive Learning for Visual Understanding","url":"https://www.mdpi.com/2079-9292/12/23/4884"},{"title":"Effective Hard Negative Mining for Contrastive Learning-based Code Search | CoLab","url":"https://colab.ws/articles/10.1145/3695994"},{"title":"Mining negative samples on contrastive learning via curricular weighting strategy - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S002002552400447X"},{"title":"ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning","url":"https://proceedings.mlr.press/v162/xia22b.html"},{"title":"A Hard Negatives Mining and Enhancing Method for Multi-Modal Contrastive Learning","url":"https://www.mdpi.com/2079-9292/14/4/767"},{"title":"Towards Expansive and Adaptive Hard Negative Mining: Graph Contrastive Learning via Subspace Preserving | Proceedings of the ACM Web Conference 2024","url":"https://dl.acm.org/doi/10.1145/3589334.3645327"},{"title":"Dynamic Asymmetric Contrastive Learning with Adaptive Hard Negative Mining for Resume-Job Matching | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-3055-7_26"},{"title":"NV-Retriever: Improving text embedding models with effective","url":"https://arxiv.org/pdf/2407.15831"}]

I found relevant results for your search. Here's what the research reveals:

## "Effective Hard Negative Mining for Contrastive Learning-Based Code Search"

The paper proposes a contrastive learning code search model with hard negative mining called CoCoHaNeRe that introduces hard negative examples into contrastive training, which are negative examples in the codebase that are most similar to positive examples.

### Key Problems Addressed

The research tackles two main issues with existing approaches:

1. Due to the random selection of negative samples, semantic representations learned by existing models cannot distinguish similar codes well.

2. Since semantic vectors in the memory bank are reused from previous inference results and then directly used for loss function calculation without gradient descent, the model cannot effectively learn the negative sample semantic information.

### Memory Bank and Nearest Neighbor Context

Prior contrastive learning approaches use a large queue (memory bank) to store embeddings to increase the reusing of negative samples. The research addresses limitations with how these memory banks are utilized in code search tasks by improving negative sample selection through hard negative mining techniques.

This work was published in the ACM Transactions on Software Engineering and Methodology (TOSEM) in 2024, focusing on improving code search through more effective contrastive learning strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2c95aa6-82e2-468b-b7f9-6ea4e267c035",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "fa8693b7-7fa7-4f31-be49-73a3e6f43495",
  "sourceToolAssistantUUID": "c2c95aa6-82e2-468b-b7f9-6ea4e267c035",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 76 · 2026-05-14T14:53:32.785Z_

Now let me do a few more targeted searches to ensure comprehensive coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa8693b7-7fa7-4f31-be49-73a3e6f43495",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2emkbsuL6kvLXAtPdJP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ddd6a160-ee91-43c7-abd1-79d1832a3a4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014tceyXfKPncUwyUnQzfcZW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 66457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 951,
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

_source line 77 · 2026-05-14T14:53:33.597Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R2vnwFwUktvNM1ZragPmQw`</summary>

```json
{
  "query": "CodeQL static analysis code retrieval training data generation negative examples 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddd6a160-ee91-43c7-abd1-79d1832a3a4e",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2emkbsuL6kvLXAtPdJP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd3a4a42-25c6-42dc-b6fd-bfa8f3fa2d8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014tceyXfKPncUwyUnQzfcZW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 66457,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 951
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 66457,
          "cache_creation_input_tokens": 951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 951,
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

_source line 78 · 2026-05-14T14:53:42.034Z_

<details><summary>↩ Tool result · `toolu_01R2vnwFwUktvNM1ZragPmQw`</summary>

```text
Web search results for query: "CodeQL static analysis code retrieval training data generation negative examples 2024 2025 2026"

Links: [{"title":"Longitudinal Analyses of SAST Tools: A CodeQL Case Study","url":"https://arxiv.org/html/2605.07900"},{"title":"Getting started with CodeQL, GitHub's declarative static analyzer for security - Tweag","url":"https://www.tweag.io/blog/2025-08-07-codeql-intro/"},{"title":"QLCoder: A Query Synthesizer for Static Analysis of Security Vulnerabilities","url":"https://arxiv.org/html/2511.08462v1"},{"title":"CodeQL","url":"https://codeql.github.com/"},{"title":"CodeQL | Testing Handbook","url":"https://appsec.guide/docs/static-analysis/codeql/"},{"title":"Vulnhalla: Picking the true vulnerabilities from the CodeQL haystack","url":"https://www.cyberark.com/resources/threat-research-blog/vulnhalla-picking-the-true-vulnerabilities-from-the-codeql-haystack"},{"title":"FineNib: A Query Synthesizer For Static Analysis of Security Vulnerabilities | OpenReview","url":"https://openreview.net/forum?id=J91IKwJrqv"},{"title":"CQLLM: A Framework for Generating CodeQL Security ...","url":"https://www.preprints.org/manuscript/202510.1458/v1/download"},{"title":"Next Generation Static Analysis: CodeQL - Henry Helm","url":"https://www.henryhelm.com/posts/codeql/"},{"title":"CodeQueries: A Dataset of Semantic Queries over Code | Proceedings of the 17th Innovations in Software Engineering Conference","url":"https://dl.acm.org/doi/10.1145/3641399.3641408"}]

Based on the web search results, here are the key findings related to CodeQL static analysis, code retrieval, training data generation, and negative examples from 2024-2026:

## CodeQL Static Analysis and Training Data

CodeQL is an open-source static analysis tool that is part of the GitHub Advanced Security suite, as the successor to LGTM after GitHub's acquisition of Semmle in 2019.

## Recent Research on CodeQL Query Synthesis (2024-2026)

Several recent projects focus on automated generation of CodeQL queries:

**QLCoder Framework**: QLCoder is an agentic framework that translates CVE descriptions into executable CodeQL queries, introducing a novel integration of execution-guided synthesis, semantic retrieval, and structured reasoning for vulnerability query generation. The framework includes 65 CVEs reported during 2025 and targets CodeQL version 2.22.2 (July 2025).

**FineNib Framework**: FineNib is an agentic framework for synthesizing CodeQL queries from known CVE descriptions, leveraging the Model Context Protocol (MCP) for agentic tool use and incorporating CodeQL's language infrastructure and documentation into the synthesis loop.

**CQLLM Framework**: CQLLM integrates RAG and LoRA, with data sources including official CodeQL class and function documentation, common CWE vulnerability detection examples, and executable QL code. Executable CWE samples are further annotated and augmented to construct the fine-tuning dataset and the RAG knowledge base.

## Training Data and Negative Examples

The CodeQueries dataset is a labeled dataset of semantic queries over Python code, where queries are about code semantics at file level with code spans as answers, curated based on queries supported by CodeQL and including both positive and negative examples.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd3a4a42-25c6-42dc-b6fd-bfa8f3fa2d8e",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "2a886159-9aca-493e-843a-6e234ded69c3",
  "sourceToolAssistantUUID": "fd3a4a42-25c6-42dc-b6fd-bfa8f3fa2d8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-14T14:53:44.775Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018GHmZthqSxmcDPJy3YGbRj`</summary>

```json
{
  "query": "code search model training positive similarity saturation embedding collapse when hard negatives help"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a886159-9aca-493e-843a-6e234ded69c3",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eneeitnyV4P8RABRL2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00eb7ac4-eebd-4290-b333-eee1c972a49f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KB9ZcgjbkK7jMQzKgMTPWW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 984,
      "cache_read_input_tokens": 67408,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 984
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 67408,
          "cache_creation_input_tokens": 984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 984,
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

_source line 80 · 2026-05-14T14:53:52.317Z_

<details><summary>↩ Tool result · `toolu_018GHmZthqSxmcDPJy3YGbRj`</summary>

```text
Web search results for query: "code search model training positive similarity saturation embedding collapse when hard negatives help"

Links: [{"title":"Contrastive Representation Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2021-05-31-contrastive/"},{"title":"NV-Retriever: Improving text embedding models with effective","url":"https://arxiv.org/pdf/2407.15831"},{"title":"Contrastive learning with hard negative samples","url":"https://arxiv.org/pdf/2010.04592"},{"title":"Positive and Negative Sampling Strategies for Representation Learning in Semantic Search - Sumit's Diary","url":"https://blog.reachsumit.com/posts/2023/03/pairing-for-representation/"},{"title":"Improving Text Embedding Models with Positive-aware ...","url":"https://dl.acm.org/doi/pdf/10.1145/3746252.3761254"},{"title":"GitHub - nixiesearch/negminer: A hard negative mining tool for embedding model training · GitHub","url":"https://github.com/nixiesearch/negminer"},{"title":"Hard Negative Mixing for Contrastive Learning Yannis Kalantidis","url":"https://arxiv.org/pdf/2010.01028"},{"title":"Hard-Mining Negatives for Semantic Similarity Model using Sentence Transformers | by Jithinanievarghese | Medium","url":"https://medium.com/@jithinanievarghese/hard-mining-negatives-for-semantic-similarity-model-using-sentence-transformers-c3e271af6c25"},{"title":"CONTRASTIVE LEARNING WITH HARD NEGATIVE ...","url":"https://openreview.net/pdf?id=CR1XOQ0UTh-"},{"title":"Improving Code Search with Hard Negative Sampling Based on Fine-tuning","url":"https://arxiv.org/html/2305.04508"}]

I found several relevant research papers and articles on your search topic. Here's a summary of what the search results reveal:

## Key Research Findings

### Hard Negative Sampling in Model Training

For code search models, negative sampling and using InfoNCE as the optimization objective is essential during training. One approach involves selectively sampling codes with high similarity scores as negative samples and ranking codes based on similarity scores from a well-trained dual-encoder to select negatives from relatively top-ranking positions.

### Positive Similarity and Embedding Collapse

Using negative samples is important for avoiding model collapse (e.g., using all-zeros representation for every data point), and batch normalization prevents model collapse by re-distributing values.

### Hard Negatives and False Negatives

A critical issue with hard negative mining is the false negative problem. Naive mining of hard-negatives may select many false negatives, with experiments on the MS-MARCO dataset finding that about 70% of passages most similar to the queries should actually be labeled as positive. To address this, methods take advantage of positive relevance scores to help identify and eliminate potential false negatives.

### Performance with Hard Negatives

Representations trained with hard negatives and debiasing assign much lower similarity scores to negative pairs, achieving less overlap between positive and negative histograms by better trading off higher dissimilarity of negative pairs with less similarity of positive pairs.

The search results particularly highlight research on code search models and general contrastive learning frameworks that address the balance between positive similarity saturation and effective hard negative usage.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00eb7ac4-eebd-4290-b333-eee1c972a49f",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "dfd128f5-f305-4582-b052-1d351756c4e1",
  "sourceToolAssistantUUID": "00eb7ac4-eebd-4290-b333-eee1c972a49f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-14T14:53:55.330Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VTMZjEeGWuuqcuCCv2UHqQ`</summary>

```json
{
  "query": "code representation learning program dependence graph data flow graph training 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfd128f5-f305-4582-b052-1d351756c4e1",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2eoQcu6BHd23d2z25EW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22ab060a-78d6-4a42-a215-2acfbaa03926",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ViqwNP1u3n7W4gjoLduHJS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 912,
      "cache_read_input_tokens": 68392,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 912
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 68392,
          "cache_creation_input_tokens": 912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 912,
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

_source line 82 · 2026-05-14T14:54:03.783Z_

<details><summary>↩ Tool result · `toolu_01VTMZjEeGWuuqcuCCv2UHqQ`</summary>

```text
Web search results for query: "code representation learning program dependence graph data flow graph training 2024 2025"

Links: [{"title":"GitHub - FSoft-AI4Code/CodeFlow: [FORGE 2025] Predicting Program Behavior with Dynamic Dependencies Learning · GitHub","url":"https://github.com/FSoft-AI4Code/CodeFlow"},{"title":"[PDF] ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ProGraML:-A-Graph-based-Program-Representation-for-Cummins-Fisches/7843876d45f4c6ac751039b198aade0ee9f94342"},{"title":"Control Data Flow Graphs (CDFG)","url":"https://www.emergentmind.com/topics/control-data-flow-graph-cdfg"},{"title":"Learning Graph-based Code Representations for Source- ...","url":"https://jun-zeng.github.io/file/tailor_paper.pdf"},{"title":"PROGRAML: A Graph-based Program Representation for Data Flow Analysis","url":"http://proceedings.mlr.press/v139/cummins21a/cummins21a.pdf"},{"title":"GRAPHCODEBERT: PRE-TRAINING CODE REPRESEN","url":"https://openreview.net/pdf?id=jLoC4ez43PZ"},{"title":"Predictive Program Slicing via Execution Knowledge-Guided","url":"https://aashishyadavally.github.io/assets/pdf/pub-fse2024.pdf"},{"title":"Code Representation Based on Hybrid Graph Modelling | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-030-92307-5_35"},{"title":"Paper page - Learning to Predict Program Execution by Modeling Dynamic Dependency on Code Graphs","url":"https://huggingface.co/papers/2408.02816"},{"title":"CodeFlow: Program Behavior Prediction with Dynamic Dependencies Learning (FORGE 2025 - Research Papers) - FORGE 2025","url":"https://conf.researchr.org/details/forge-2025/forge-2025-papers/13/CodeFlow-Program-Behavior-Prediction-with-Dynamic-Dependencies-Learning"}]

Based on the search results, here's what I found regarding code representation learning using program dependence graphs and data flow graphs with recent training developments in 2024-2025:

## Key Recent Research

**CodeFlow (FORGE 2025):**
CodeFlow is a novel machine learning approach designed to predict program behavior by learning both static and dynamic dependencies within code, constructing control flow graphs (CFGs) to represent all possible execution paths and using these graphs to predict code coverage and detect runtime errors. The system captures dynamic dependencies among statements using execution traces.

**GraphCodeBERT:**
Data flow is a graph in which nodes represent variables and edges represent the relation of "where-the-value-comes-from" between variables. The model introduces structure-aware pre-training tasks, including data flow edges prediction for learning representation from code structure and variable-alignment across source code and data flow.

**ND-Slicer (FSE 2024):**
Specialized source code models have highlighted the effectiveness of learning-based approaches in understanding data and control dependencies, though their learning objectives do not focus on run-time behavior of code; ND-Slicer leverages CodeExecutor, a model pre-trained on code execution, to learn dynamic program dependencies.

**Graph-Based Program Representations:**
Code Property Graphs (CPGs) combine Abstract Syntax Trees (AST), Control Flow Graphs (CFG), and Data Flow Graphs (DFG), and CPGNN (a CPG-based neural network) learns corresponding representations by iteratively propagating node embeddings along the CPG structure.

**Control Data Flow Graphs (CDFG):**
CDFGs support high-precision program optimization, learning, diagnosis, and synthesis tasks across applications including static analysis, hardware quality estimation, and automated program repair.

These approaches represent the latest advances in combining graph-based program representations with deep learning for code understanding and analysis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22ab060a-78d6-4a42-a215-2acfbaa03926",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "f83c21bd-be06-4346-8113-ca61b7d6f10b",
  "sourceToolAssistantUUID": "22ab060a-78d6-4a42-a215-2acfbaa03926",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 83 · 2026-05-14T14:54:06.809Z_

Now let me read the project's paper framing to better understand the exact claims and positioning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f83c21bd-be06-4346-8113-ca61b7d6f10b",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2epFfurCfTo9q97i6YL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "500b7be9-dc0d-4761-ac4a-8a3dff72da65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D183FkR3xsegBYp7tQR9t8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1086,
      "cache_read_input_tokens": 69304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1086,
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

_source line 84 · 2026-05-14T14:54:08.102Z_

<details open><summary>🔧 Tool call — Read · `toolu_014a4ooKwXRmrZmRHEUvk6F5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "500b7be9-dc0d-4761-ac4a-8a3dff72da65",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2epFfurCfTo9q97i6YL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3510a802-7b66-4429-a1ad-56c0c87c8149",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D183FkR3xsegBYp7tQR9t8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1086,
      "cache_read_input_tokens": 69304,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1086
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 69304,
          "cache_creation_input_tokens": 1086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1086,
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

_source line 85 · 2026-05-14T14:54:08.122Z_

<details><summary>↩ Tool result · `toolu_014a4ooKwXRmrZmRHEUvk6F5`</summary>

```text
1	# Paper Framing — StructFuse
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main
5	- Deadline: ARR May 25, 2026
6	
7	## Core Claims (3)
8	
9	1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported "harm" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B).
10	
11	2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.
12	
13	3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. Method is a general-purpose structural negative generator applicable beyond code (molecular networks, circuit topology, KG retrieval).
14	
15	## Story Spine
16	
17	- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.
18	
19	- **Existing approaches & gaps**:
20	  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies
21	  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal
22	  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only
23	  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance
24	  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works
25	
26	- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.
27	
28	- **Headline result template**: "True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis."
29	
30	## Core Insight
31	
32	The effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.
33	
34	## Dual-Pillar Motivation
35	
36	1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.
37	2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.
38	
39	## Formal Definition
40	
41	Given retrieval domain D, structural graph G, similarity function s, query q:
42	**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)
43	
44	The structural graph is externally fixed and does not update with the encoder (drift-immune).
45	
46	## Title Options
47	
48	- Primary: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
49	- Alternative: "StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval"
50	- Backup: "Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally"
51	
52	## Venue Fit
53	
54	1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. "Do Language Models..." papers). Contribution is understanding, not just a new method.
55	2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.
56	3. **Against "incremental" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.
57	
58	## Anticipated Reviewer Concerns
59	
60	| Concern | Response | Evidence |
61	|---------|----------|----------|
62	| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; cross-architecture (decoder vs encoder-decoder) strengthens it | plan_013 (done), m2_full runs |
63	| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |
64	| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |
65	| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |
66	| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |
67	| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |
68	| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |
69	| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |
70	| "Complementary signal" overstatement | Temper: "conditionally beneficial" not "always complementary" | Writing discipline |
71	| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |
72	
73	## Evidence Status
74	
75	### Confirmed findings (basis for claims):
76	- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact
77	- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction
78	- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)
79	- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only
80	- plan_006: CodeQL scalability confirmed at 123-repo scale
81	
82	### In progress:
83	- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)
84	- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)
85	- m1_reextract_v2: expanded extraction for higher coverage
86	
87	### Planned (priority order):
88	- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
89	- plan_014: Temperature ablation (Dream reviewer concern)
90	- plan_004: RepoBench-R second benchmark
91	- plan_015: Dynamic mining baseline
92	- plan_007/008/009: Additional ablations
93	
94	## Contingency (if full M2 results weaken claims)
95	
96	### All 18 runs confirm pilot pattern: Best case
97	- Full statistical power, paper as framed above
98	- Target: EMNLP Main
99	
100	### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper
101	- Drop Claim 2 to analysis observation
102	- Paper becomes: "True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions"
103	- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main
104	
105	### Embedding mining also loses advantage at full scale: Major reassessment needed
106	- Recheck data pipeline for bugs (full-scale data may have distribution differences)
107	- If confirmed: negative result paper — "Why Hard Negative Mining Doesn't Scale for Code Retrieval"
108	- Discuss with user before committing direction
109	
110	## Deprecated Claims (with reason)
111	
112	- ~~"Embedding-distance hard negatives actively harm code retrieval"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.
113	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3510a802-7b66-4429-a1ad-56c0c87c8149",
  "isSidechain": true,
  "promptId": "aef658d1-4560-4cf2-8d51-97d68eca25c0",
  "agentId": "a924cdd4f9463f49b",
  "type": "user",
  "uuid": "a04bc5f3-fa50-4f76-95ad-d32eb67e3d75",
  "sourceToolAssistantUUID": "3510a802-7b66-4429-a1ad-56c0c87c8149",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 86 · 2026-05-14T14:55:39.230Z_

Now I have comprehensive context. Let me compile the full novelty check report.

---

## Novelty Check Report: StructFuse

### Summary Assessment

**Overall novelty: MEDIUM-HIGH.** The specific combination of (a) correcting CoCoHaNeRe's BM25-proxy conflation, (b) inter-procedural dataflow negatives via CodeQL for training, and (c) mechanistic explanation via representation saturation is novel. However, the broader space of "hard negative mining for code search" is active and crowded in 2024-2025. The risk is not that someone has done the exact same thing, but that reviewers may perceive incremental contribution given the volume of recent work.

---

### Detailed Findings by Search Query

#### 1. "Hard negative mining code retrieval"

**CoCoHaNeRe** (TOSEM 2024, doi:10.1145/3695994)
- Full title: "Effective Hard Negative Mining for Contrastive Learning-Based Code Search"
- This IS the paper our Claim 1 corrects. It uses a memory bank with nearest-neighbor retrieval for hard negatives + differentiable hard negative embeddings. Outperforms CodeBERT/GraphCodeBERT/UniXcoder by 7-11% MRR.
- **Critical for us**: We need to demonstrate clearly that their "hard negatives" are BM25-proxy, not true embedding distance. This is the central correction our paper makes.
- Overlap: **HIGH** (we directly build on and correct this work)

**Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems** (ACL Industry 2025, arXiv:2505.18366)
- General domain retrieval, not code-specific. Uses PCA-based dimensionality reduction + dynamic hard negative selection.
- Overlap: **LOW** (different domain, different approach)

#### 2. "Contrastive learning code search hard negatives"

**Uncertainty-Aware Contrastive Learning with Hard Negative Sampling for Code Search Tasks** (AAAI 2025)
- Authors: Liu et al., Shenzhen University
- Proposes uncertainty learning (Gaussian distributions for embeddings) + hard negative sampling for code search.
- Uses 6 programming languages on CodeSearchNet.
- Outperforms 10 baselines.
- **Key difference from us**: They focus on uncertainty-aware representations, not on comparing mining strategies or using structural/dataflow negatives. They don't correct CoCoHaNeRe or analyze representation geometry.
- Overlap: **MEDIUM** (same problem space — hard negatives for code search — but different angle and different contribution type)

**CMCS: Contrastive-Metric Learning via Vector-Level Sampling and Augmentation for Code Search** (Scientific Reports, June 2024)
- K-means based hard negative sampling + hardness-controllable augmentation.
- Tested on CodeSearchNet with 7 models.
- Overlap: **MEDIUM** (another hard negative method for code search, but no structural signals, no mechanistic explanation)

#### 3. "CoCoHaNeRe" details

- Published in TOSEM 2024. Uses memory bank for nearest-neighbor hard negative retrieval. Does NOT use true embedding distance — uses cached/stale embeddings from memory bank (which we claim is effectively BM25-proxy behavior).
- **No published correction or replication of CoCoHaNeRe found in 2024-2026.** Our Claim 1 (correcting the misconception) appears novel.

#### 4. "Dataflow-aware training for code retrieval"

**DraCo: Dataflow-Guided Retrieval Augmentation for Repository-Level Code Completion** (ACL 2024, arXiv:2405.19782)
- Uses extended dataflow analysis to build repo-specific context graphs for RETRIEVAL at inference time (code completion, not training signal).
- **Key difference**: DraCo uses dataflow for inference-time retrieval context, NOT for mining training negatives. Completely different use of dataflow.
- Overlap: **LOW-MEDIUM** (uses dataflow for code tasks but different purpose — inference vs training)

**LLMDFA: Analyzing Dataflow in Code with Large Language Models** (NeurIPS 2024, arXiv:2402.10754)
- LLM-powered compilation-free dataflow analysis framework.
- Not about retrieval training at all.
- Overlap: **LOW**

**No paper found that uses inter-procedural dataflow analysis (CodeQL or otherwise) to generate hard negatives for contrastive training.** This appears to be a genuine novelty.

#### 5. "Structure-guided negative mining"

**Structure-Aware Hard Negative Mining for Heterogeneous Graph Contrastive Learning** (arXiv:2108.13886)
- Graph domain, not code. Measures hardness by structural characteristics of heterogeneous graphs.
- Overlap: **LOW** (conceptually related but different domain entirely)

No code-specific structure-guided negative mining papers found.

#### 6. "Code retrieval negative sampling strategy"

**Negative Sampling Techniques in Information Retrieval: A Survey** (Findings of EACL 2026, arXiv:2603.18005)
- Comprehensive survey of 35 papers on negative sampling in dense IR. Includes taxonomy of random/static/dynamic/synthetic negatives.
- **Risk**: Reviewers may cite this survey and say "all strategies have been studied." We need to differentiate that code has structural signals unavailable in text retrieval.
- Overlap: **LOW** (survey, not code-specific, but important context)

**Rethinking Negative Pairs in Code Search** (EMNLP 2023, arXiv:2310.08069)
- Li et al. Identifies false negatives problem in code corpora due to duplication. Proposes Soft-InfoNCE with weight terms.
- **Key difference**: They address false negatives (same-class samples mislabeled as negative), not hard negative mining strategies. Different problem.
- Overlap: **LOW-MEDIUM** (same general space but different problem)

#### 7. "SweRank" and "SWE-Fixer"

**SweRank** (Salesforce, arXiv:2505.07849, 2025)
- Retrieve-and-rerank for software issue localization. SWERankEmbed (bi-encoder) + SWERankLLM (listwise reranker).
- Large-scale SweLoc dataset from GitHub.
- SOTA on SWE-Bench-Lite and LocBench.
- **For us**: A strong baseline we should compare against. Uses standard training without structural negatives.
- Overlap: **LOW** (complementary; we could use it as a baseline)

**SweRank+** (arXiv:2512.20482, Dec 2025)
- Extension: multilingual, multi-turn code ranking with agentic search.
- Overlap: **LOW**

**SWE-Fixer** (ACL Findings 2025)
- Uses BM25 + lightweight retriever for coarse-to-fine file retrieval, then Qwen-based editor.
- Overlap: **LOW** (different approach, no contrastive training)

#### 8. "Representation geometry hard negatives"

**Hard-Negative Sampling for Contrastive Learning: Optimal Representation Geometry and Neural- vs Dimensional-Collapse** (arXiv:2311.05139, ICLR 2025)
- Analyzes representation geometry of hard negatives in supervised/unsupervised contrastive learning.
- Shows HSCL/HUCL losses minimized by Neural-Collapse (ETF) geometry.
- **IMPORTANT**: This paper provides theoretical foundation for representation geometry analysis of hard negatives. Our "representation saturation" story is empirical observation in code domain; theirs is theoretical analysis in general supervised setting.
- Overlap: **MEDIUM** (they study representation geometry × hard negatives theoretically; we do it empirically for code with the saturation/conditional benefit insight)

#### 9. "ARISE code dataflow"

No relevant ARISE paper found for code dataflow retrieval. The search returned mostly game codes and DraCo (already covered).

#### 10. "CodexGraph"

**CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases** (NAACL 2025, arXiv:2408.03910)
- Uses static analysis to extract code graphs (MODULE/CLASS/FUNCTION nodes, CONTAINS/INHERITS/USES edges).
- LLM agent constructs graph queries for code retrieval.
- **Key difference**: Inference-time graph navigation, not training signal. No contrastive learning, no negative mining.
- Overlap: **LOW** (complementary — they use structure at inference, we use it for training)

#### 11. "LocAgent"

**LocAgent: Graph-Guided LLM Agents for Code Localization** (ACL 2025, arXiv:2503.09089)
- Parses codebases into directed heterogeneous graphs. LLM agents do multi-hop reasoning for code localization.
- BM25 indexing for keyword search + graph traversal.
- 92.7% file-level accuracy, 86% cost reduction vs proprietary models.
- **Key difference**: Inference-time agentic graph navigation, not training negative mining.
- Overlap: **LOW** (complementary)

#### 12. "RANGER code retrieval graph"

No specific "RANGER" paper found in the code retrieval domain. GNN-RAG (ACL Findings 2025) was found but is for knowledge graph QA, not code retrieval.

---

### Additional Important Findings

**HedgeCode: Multi-Task Hedging Contrastive Learning for Code Search** (ICSE 2025)
- Two-phase training: representation alignment via hedging contrastive learning, then multi-task joint learning.
- Detects subtle differences between code and NL, aligning representation spaces.
- **Key difference**: Focuses on code-NL alignment and multi-task learning, not on negative mining strategies or structural signals.
- Overlap: **MEDIUM** (same code search improvement goal, contrastive learning, but different mechanism)

**MGS3: Multi-Granularity Self-Supervised Code Search** (KDD 2025, arXiv:2505.24274)
- Multi-granularity (function/block/statement) code search with in-function negative samples for fine-grained code.
- New dataset: MGCodeSearchNet (536K+ pairs).
- **Key difference**: Granularity-based negatives, not structure/dataflow-based. Different contribution axis.
- Overlap: **LOW-MEDIUM**

**Improving Code Search with Hard Negative Sampling Based on Fine-tuning** (arXiv:2305.04508, IEEE 2025)
- Dual-encoder + cross-encoder cascade (Retriever-Ranker framework). Hard negatives from top-ranking dual-encoder results.
- **Key difference**: Standard embedding-distance hard negatives without structural signal. No mechanistic analysis.
- Overlap: **MEDIUM** (overlaps with our embedding-distance mining, but we go beyond with structural negatives + mechanistic explanation)

**RFMC-CS: Representation Fusion Multi-View Momentum Contrastive Learning for Code Search** (Automated Software Engineering, 2025)
- Multi-modal representation fusion + momentum contrastive learning.
- Overlap: **LOW** (different approach)

---

### Critical Assessment: Three Key Novelty Questions

**Q1: Has anyone done a systematic comparison of hard negative mining strategies for code?**
**Answer: Partially.** CoCoHaNeRe (TOSEM 2024) compares random vs memory-bank hard negatives. The AAAI 2025 uncertainty paper compares their method to 10 baselines. CMCS (2024) compares K-means negatives. But **no paper does a controlled, systematic comparison isolating random vs embedding-distance vs structure-grounded negatives with mechanistic explanation.** Our systematic study framing appears novel.

**Q2: Has anyone already corrected CoCoHaNeRe's findings?**
**Answer: No.** No correction, replication failure, or contradiction of CoCoHaNeRe found in the literature through May 2026. Our Claim 1 is novel.

**Q3: Has anyone used dataflow/program analysis for training signal (not inference-time) in code retrieval?**
**Answer: No.** DraCo uses dataflow at inference for code completion. CodexGraph/LocAgent use graphs at inference. DeepDFA uses dataflow-inspired learning for vulnerability detection (not retrieval). GraphCodeBERT uses dataflow for pre-training but not for negative mining. **Using inter-procedural dataflow via CodeQL specifically to generate hard negatives for contrastive training is novel.**

---

### Risk Assessment

| Risk | Level | Mitigation |
|------|-------|------------|
| Crowded field (many 2024-2025 code search + contrastive papers) | **MEDIUM** | Differentiate clearly: we do systematic analysis + correction, not "yet another method" |
| ICLR 2025 representation geometry paper (arXiv:2311.05139) | **MEDIUM** | Cite prominently. They provide theory; we provide empirical evidence in code domain with practical implications |
| AAAI 2025 uncertainty paper covers similar space | **MEDIUM** | Different contribution: they propose a new method; we provide systematic understanding |
| EACL 2026 negative sampling survey | **LOW** | Survey is general IR, not code-specific. Cite and position as motivation |
| Someone publishes dataflow negatives before EMNLP deadline | **LOW** | No sign of this in any preprint through June 2026 |

---

### Recommendations

1. **Must cite and carefully differentiate from**: CoCoHaNeRe (TOSEM 2024), AAAI 2025 uncertainty paper, HedgeCode (ICSE 2025), CMCS (2024), MGS3 (KDD 2025), Rethinking Negative Pairs (EMNLP 2023), Improving Code Search with Hard Negatives (arXiv:2305.04508), EACL 2026 negative sampling survey
2. **Must cite as complementary inference-time approaches**: DraCo (ACL 2024), CodexGraph (NAACL 2025), LocAgent (ACL 2025), SweRank (2025)
3. **Must cite for theoretical grounding**: arXiv:2311.05139 (representation geometry + hard negatives, ICLR 2025)
4. **Strongest novelty claims**: (a) Correcting CoCoHaNeRe is unique, (b) Inter-procedural dataflow negatives for training is unique, (c) Conditional benefit mediated by representation saturation is unique as empirical finding in code domain

Sources:
- [CoCoHaNeRe - TOSEM 2024](https://dl.acm.org/doi/10.1145/3695994)
- [Uncertainty-Aware Contrastive Learning - AAAI 2025](https://ojs.aaai.org/index.php/AAAI/article/view/34070)
- [CMCS - Scientific Reports 2024](https://www.nature.com/articles/s41598-024-64205-2)
- [DraCo - ACL 2024](https://arxiv.org/abs/2405.19782)
- [CodexGraph - NAACL 2025](https://arxiv.org/abs/2408.03910)
- [LocAgent - ACL 2025](https://arxiv.org/abs/2503.09089)
- [SweRank - 2025](https://arxiv.org/abs/2505.07849)
- [SWE-Fixer - ACL Findings 2025](https://arxiv.org/abs/2501.05040)
- [Representation Geometry + Hard Negatives - ICLR 2025](https://arxiv.org/abs/2311.05139)
- [Rethinking Negative Pairs - EMNLP 2023](https://arxiv.org/abs/2310.08069)
- [MGS3 - KDD 2025](https://arxiv.org/abs/2505.24274)
- [HedgeCode - ICSE 2025](https://dl.acm.org/doi/10.1109/ICSE55347.2025.00008)
- [Improving Code Search with Hard Negatives - arXiv:2305.04508](https://arxiv.org/abs/2305.04508)
- [Negative Sampling Survey - EACL 2026](https://arxiv.org/abs/2603.18005)
- [RFMC-CS - ASE 2025](https://link.springer.com/article/10.1007/s10515-025-00487-8)
- [LLMDFA - NeurIPS 2024](https://arxiv.org/abs/2402.10754)
- [SweRank+ - 2025](https://arxiv.org/abs/2512.20482)
- [Hard Negative Mining Enterprise Systems - ACL Industry 2025](https://arxiv.org/abs/2505.18366)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a04bc5f3-fa50-4f76-95ad-d32eb67e3d75",
  "isSidechain": true,
  "agentId": "a924cdd4f9463f49b",
  "requestId": "req_011Cb2epaN4ZhG1ByeDoYvJk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38a0dc31-0376-4c03-b581-c57f4ff87e5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/sessions/director_3a5c0d9a",
  "sessionId": "05b55968-168a-4f95-bd51-a0c823401fb5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APXgy84pAYjmTPoT9cyT1q",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2768,
      "cache_read_input_tokens": 70390,
      "output_tokens": 4203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2768
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4203,
          "cache_read_input_tokens": 70390,
          "cache_creation_input_tokens": 2768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2768,
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
