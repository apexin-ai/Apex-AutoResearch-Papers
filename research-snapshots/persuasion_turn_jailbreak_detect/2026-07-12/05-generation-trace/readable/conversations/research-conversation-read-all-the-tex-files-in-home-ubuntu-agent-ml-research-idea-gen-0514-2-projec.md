# Research conversation: Read all the .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/doc

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aa90fb53a2c1faac3.jsonl`
- **Structured JSON:** [`a29a17bf84027d722277.json`](../../sessions/a2/a29a17bf84027d722277.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-24T18:24:44.480Z_

Read all the .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/ and list every abbreviation/acronym used in the paper. For each one, note:
1. The abbreviation itself
2. Whether it's defined (full form given) at first use
3. The file and approximate line where it first appears
4. Whether it appears in the abstract

Focus on: method names (DAPT, DisPeD, BiGRU, etc.), model names (DeBERTa, RoBERTa, LLM, etc.), dataset names (OOD, IID, etc.), metric names (F1, FPR, ECE, etc.), technique names (MLM, TOST, SVD, CKA, etc.), and any other acronyms.

Read these files: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex

Report a complete inventory in a structured format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "270ab91c-e9b9-4a39-b092-16a4d85348b6",
  "agentId": "aa90fb53a2c1faac3",
  "type": "user",
  "uuid": "556b3c7f-1ec5-403a-93ed-1612394daa3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-24T18:24:44.491Z_

```json
{
  "parentUuid": "556b3c7f-1ec5-403a-93ed-1612394daa3f",
  "isSidechain": true,
  "agentId": "aa90fb53a2c1faac3",
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
  "uuid": "02d54390-063f-4971-90f7-a6ef85f792ba",
  "timestamp": "2026-05-24T18:24:44.491Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch"
}
```

---

### Assistant

_source line 3 · 2026-05-24T18:24:48.633Z_



I'll read all the .tex files to inventory every abbreviation/acronym used in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02d54390-063f-4971-90f7-a6ef85f792ba",
  "isSidechain": true,
  "agentId": "aa90fb53a2c1faac3",
  "requestId": "req_011CbMryDE3MYBwmpcc1ZK28",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "255e0d81-8cdb-4cb4-b4a9-9a0966528393",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xP4szykNX75u7CCZHPgSP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33137,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33137,
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

_source line 4 · 2026-05-24T18:24:48.941Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PsF8VwRHdXEwj3JBGMwACo`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "255e0d81-8cdb-4cb4-b4a9-9a0966528393",
  "isSidechain": true,
  "agentId": "aa90fb53a2c1faac3",
  "requestId": "req_011CbMryDE3MYBwmpcc1ZK28",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91fd7ba4-e8ce-446d-9108-2afa3b4a8a78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xP4szykNX75u7CCZHPgSP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33137,
      "cache_read_input_tokens": 0,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 33137
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 130,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 33137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 33137,
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

_source line 5 · 2026-05-24T18:24:49.002Z_

<details><summary>↩ Tool result · `toolu_01PsF8VwRHdXEwj3JBGMwACo`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91fd7ba4-e8ce-446d-9108-2afa3b4a8a78",
  "isSidechain": true,
  "promptId": "270ab91c-e9b9-4a39-b092-16a4d85348b6",
  "agentId": "aa90fb53a2c1faac3",
  "type": "user",
  "uuid": "16b994f5-ff46-4515-815f-2b6ed2e30ee7",
  "sourceToolAssistantUUID": "91fd7ba4-e8ce-446d-9108-2afa3b4a8a78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-24T18:24:51.579Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FPj7rTcmCAzN3VwgARp1DV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16b994f5-ff46-4515-815f-2b6ed2e30ee7",
  "isSidechain": true,
  "agentId": "aa90fb53a2c1faac3",
  "requestId": "req_011CbMryYTviM1hjLkYd9Z8f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b37cfdfb-8511-4ab8-9a01-a8ae9b25cd32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Babp6vAuESryiSZyYAC283",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1362,
      "cache_read_input_tokens": 33137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1362,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 7 · 2026-05-24T18:24:51.590Z_

<details><summary>↩ Tool result · `toolu_01FPj7rTcmCAzN3VwgARp1DV`</summary>

```text
1	% abstract.tex
2	\begin{abstract}
3	Llama Guard~3 detects only 1.8\% of multi-turn jailbreaks---attacks that distribute adversarial intent across individually benign conversation turns. We present DisPeD, a controlled ablation framework where seven encoder variants---differing solely in their pretraining objective---share the same frozen downstream classifier, enabling direct comparison across thirteen configurations (125--355M parameters) and three OOD attack families. Three findings emerge: (1)~classification-based domain adaptation recovers OOD detection (F1\,=\,0.97--1.0 vs.\ vanilla 0.26--0.31) while unsupervised pretraining collapses under mixed-LLM training; (2)~scrambled labels match correct labels for template-attack detection---the classification objective's structural role, not label semantics, drives generalization; and (3)~these advantages are condition-specific, as on human-authored single-turn data the hierarchy reverses (MLM F1\,=\,0.837 vs.\ classification 0.596). A 184M-parameter encoder with BiGRU achieves 24$\times$ inference speedup over LLM-as-judge baselines, and few-shot benign adaptation reduces false-positive rates from 68\% to 0\%.
4	\end{abstract}
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b37cfdfb-8511-4ab8-9a01-a8ae9b25cd32",
  "isSidechain": true,
  "promptId": "270ab91c-e9b9-4a39-b092-16a4d85348b6",
  "agentId": "aa90fb53a2c1faac3",
  "type": "user",
  "uuid": "31ae86e9-f334-49c8-ac5c-1a82d4e4d016",
  "sourceToolAssistantUUID": "b37cfdfb-8511-4ab8-9a01-a8ae9b25cd32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-24T18:24:52.064Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YBYPsu1YpL9fLHPJ92ihiY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31ae86e9-f334-49c8-ac5c-1a82d4e4d016",
  "isSidechain": true,
  "agentId": "aa90fb53a2c1faac3",
  "requestId": "req_011CbMryYTviM1hjLkYd9Z8f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45043c37-4dd6-4f11-b3b8-bb4de00e02f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Babp6vAuESryiSZyYAC283",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1362,
      "cache_read_input_tokens": 33137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1362,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 9 · 2026-05-24T18:24:52.074Z_

<details><summary>↩ Tool result · `toolu_01YBYPsu1YpL9fLHPJ92ihiY`</summary>

```text
1	% introduction.tex
2	
3	\section{Introduction}
4	
5	Multi-turn jailbreak attacks distribute adversarial intent across individually benign turns. Crescendo~\citep{russinovich2024crescendo}, Foot-in-the-Door~\citep{fitd2024}, and Deceptive Delight~\citep{deceptivedelight2024} all rely on persuasion as their core mechanism: \citet{zeng2024pap} catalogue 40 persuasion techniques across jailbreak families, and \citet{hagendorff2026reasoning} identify strategies in 97\% of successful attacks. Because individual attack turns occupy the same embedding region as benign text~\citep{bullwinkel2025repeng}, no single-turn filter can distinguish them from legitimate conversation.
6	
7	Existing defenses leave a critical gap. Production classifiers such as Llama Guard~\citep{inan2023llamaguard}, WildGuard~\citep{han2024wildguard}, and ShieldGemma~\citep{zeng2024shieldgemma} operate on individual turns and miss multi-turn manipulation; Llama Guard~3 detects only 1.8\% of multi-turn jailbreaks in our evaluation (Section~\ref{sec:decomposition}). Multi-turn defenses (DeepContext~\citep{deepcontext2026}, BIID~\citep{tong2025biid}, G-Guard~\citep{gguard2025}) model conversation-level structure but each evaluates on a single attack family. None answers the central question: \emph{what representation properties enable a detector to generalize across attack families it has never seen?} Pretrained language understanding alone does not suffice: vanilla DeBERTa-v3~\citep{he2021deberta} with temporal aggregation (cf.\ DeepContext) drops from F1\,=\,1.000 in-distribution to 0.312 on OOD Deceptive Delight, and GPT-5.5 reaches only 0.191--0.449 F1 (across prefix lengths) with 30--47\% unparseable responses (Appendix~\ref{sec:llm_judge}). The bottleneck is distributional: cross-attack generalization at base model scale benefits substantially from domain adaptation.
8	
9	\begin{figure*}[t]
10	\centering
11	\includegraphics[width=\textwidth]{figures/paper/fig1_architecture.pdf}
12	\caption{DisPeD architecture. Stage~1 adapts a DeBERTa encoder on jailbreak conversation text (seven variant objectives). Stage~2 aggregates frozen \texttt{[CLS]} embeddings via BiGRU for conversation-level jailbreak detection. Only user turns are processed.}
13	\label{fig:architecture}
14	\end{figure*}
15	
16	Our pipeline, \textbf{DisPeD} (Disentangled Persuasion Detection)\footnote{We use `disentangled' to describe our experimental methodology of isolating individual factors through controlled ablation, distinct from disentangled representation learning ($\beta$-VAE, InfoGAN).}, separates encoder adaptation (Stage~1) from temporal classification (Stage~2, a frozen BiGRU; Figure~\ref{fig:architecture}). Seven Stage~1 variants each isolate a single factor while holding all others constant (Section~\ref{sec:method}); the contribution is the decomposition, not the pipeline. Controlled ablation across DeBERTa-v3 and RoBERTa~\citep{liu2019roberta} on four attack families reveals three findings at base model scale: classification-based DAPT is the only variant that consistently recovers OOD detection (F1\,=\,0.97--1.0 vs.\ vanilla 0.26--0.31), even under mixed-LLM training where unsupervised pretraining collapses to vanilla level~\citep{gururangan2020dontstop}; scrambled labels match correct labels for template attacks, indicating the classification objective's structural role---not label semantics---drives generalization; yet this hierarchy reverses entirely on human-authored data (MLM 0.837 vs.\ classification 0.596), revealing condition-specific rather than universal advantages. At 355M parameters, capacity alone suffices: RoBERTa-large handles ActorAttack~\citep{ren2024actorattack} without adaptation.
17	
18	Our contributions:
19	\begin{itemize}[leftmargin=*, itemsep=2pt, topsep=4pt]
20	  \item \textbf{Systematic ablation of cross-attack generalization.} Thirteen encoder configurations at three scales (125--355M) decompose jailbreak detection into attack-side and benign-side factors---the first controlled factorial study in this domain. Classification DAPT recovers OOD detection (0.26--0.31 $\rightarrow$ 0.97--1.0) while unsupervised pretraining collapses under mixed-LLM training; 10--25 benign conversations reduce FPR from 58--68\% to 0--1.5\%.
21	
22	  \item \textbf{Partition sufficiency with a difficulty gradient.} Scrambled labels match correct labels for template-attack detection (TOST $|d| \leq 0.14$), but strategy-diverse attacks retain moderate label sensitivity ($d$\,=\,0.44). Domain-relevant partitioning---not label semantics---is the operative mechanism, consistent with \citet{zhang2021understanding}: compression localizes to 3 SVD dimensions in layers 8--12.
23	
24	  \item \textbf{Practical adaptation protocol.} A 184M-parameter encoder achieves 24.3$\times$ speedup over LLM-as-judge (43$\times$ fewer parameters; Table~\ref{tab:efficiency_main}); few-shot benign adaptation resolves deployment-blocking FPR without target-domain attack data.
25	\end{itemize}
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45043c37-4dd6-4f11-b3b8-bb4de00e02f3",
  "isSidechain": true,
  "promptId": "270ab91c-e9b9-4a39-b092-16a4d85348b6",
  "agentId": "aa90fb53a2c1faac3",
  "type": "user",
  "uuid": "dc841bf2-487e-4858-bd7f-9fd56c69a25d",
  "sourceToolAssistantUUID": "45043c37-4dd6-4f11-b3b8-bb4de00e02f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-24T18:24:53.002Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VwN1pkaQWCJXthoQ3ugPwt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc841bf2-487e-4858-bd7f-9fd56c69a25d",
  "isSidechain": true,
  "agentId": "aa90fb53a2c1faac3",
  "requestId": "req_011CbMryYTviM1hjLkYd9Z8f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "582b08f4-2de9-4b5d-8661-f36e730a97da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Babp6vAuESryiSZyYAC283",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1362,
      "cache_read_input_tokens": 33137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1362,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 11 · 2026-05-24T18:24:53.010Z_

<details><summary>↩ Tool result · `toolu_01VwN1pkaQWCJXthoQ3ugPwt`</summary>

```text
1	% related_work.tex
2	
3	\section{Related Work}
4	
5	\paragraph{Multi-turn jailbreak attacks.}
6	Multi-turn jailbreak families share a persuasion substrate~\citep{zeng2024pap,hagendorff2026reasoning,li2024mhj} but operationalize it differently---gradual escalation~\citep{russinovich2024crescendo}, commitment-consistency bias~\citep{fitd2024}, emotional manipulation~\citep{deceptivedelight2024}, persona steering~\citep{ren2024actorattack}, context poisoning~\citep{alobaid2026echochamber}---while automated methods~\citep{chao2023pair,mehrotra2024tap} iteratively refine adversarial prompts~\citep{perez2022redteaming}. Taxonomies~\citep{wei2023jailbroken} and benchmarks~\citep{mazeika2024harmbench,chao2024jailbreakbench,jiang2024redqueen,song2026multibreak} standardize evaluation. This shared substrate with diverse surface strategies defines our setting: a detector must generalize across families, not merely succeed on its training distribution.
7	
8	\paragraph{Multi-turn defenses and production safety.}
9	No existing defense evaluates cross-attack transfer. Recent conversation-level systems pair fine-tuned encoders with sequence aggregation~\citep{deepcontext2026,tong2025biid,gguard2025,safedream2026}, yet each evaluates on a single attack family; absent public implementations preclude direct comparison (Appendix~\ref{app:bert_proxy}). Representation-level approaches~\citep{lu2025xboundary,zhang2025jbshield,xie2024gradsafe,zou2024circuitbreakers,wu2025safeint,shen2024jailbreakantidote,yousefpour2025repbend,kulkarni2026latentadversarial,kadali2025internallayers,kadali2026trace,hua2026rcs} require white-box access and can be brittle under adaptive attacks~\citep{derya2026revisitingjbshield}. Per-turn classifiers~\citep{inan2023llamaguard,metallamaguard3_2024,zeng2024shieldgemma,han2024wildguard,anthropic2025constitutional} and production systems~\citep{markov2023holistic} cannot model multi-turn trajectories; perturbation-based~\citep{robey2024smoothllm} and decoding-based~\citep{xu2024safedecoding} defenses target single-turn attacks. Our ablation fills this gap: decomposition across thirteen configurations under OOD evaluation identifies domain exposure as the dominant factor behind cross-attack transfer.
10	
11	\paragraph{Computational persuasion and discourse.}
12	Discourse and persuasion frameworks~\citep{mann1988rst,prasad2008pdtb,stolcke2000dialogueact,austin1962speechacts,searle1969speechacts} offer interpretable vocabulary for attack strategies. Building on Cialdini's principles~\citep{cialdini2001influence}, PAP~\citep{zeng2024pap} identifies 40 persuasion techniques and \citet{hagendorff2026reasoning} find identifiable strategies in 97\% of successful attacks; propaganda analysis~\citep{dasanmartino2019fine,dasanmartino2020semeval} and persuasive dialogue~\citep{wang2019persuasion} apply similar classification. Our ablation disentangles these roles: the taxonomy enables strategy characterization, but detection operates through domain-adapted embeddings regardless of label correctness.
13	
14	\paragraph{Domain-adaptive pretraining.}
15	Continued pretraining on domain text yields consistent gains~\citep{gururangan2020dontstop,lee2020biobert,beltagy2019scibert,howard2018ulmfit}, yet this has not been disentangled for safety-critical generalization. Intermediate-task transfer~\citep{phang2018stilts} and multi-task learning~\citep{caruana1997multitask,liu2019mtdnn} confound domain exposure with supervised signal; our MLM control isolates the contribution. Dataset artifact analysis~\citep{gururangan2018artifacts,niven2019probing} motivates the TF-IDF baseline, adversarial NLP~\citep{jin2020textfooler,li2020bertattack,nasr2025attackermovessecond,andriushchenko2024adaptive} informs the perturbation protocol, and probing~\citep{conneau2018probing,hewitt2019structural} underpins CKA analysis.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "582b08f4-2de9-4b5d-8661-f36e730a97da",
  "isSidechain": true,
  "promptId": "270ab91c-e9b9-4a39-b092-16a4d85348b6",
  "agentId": "aa90fb53a2c1faac3",
  "type": "user",
  "uuid": "dc1ac1f2-5da5-4f29-9bd6-4c36928a5234",
  "sourceToolAssistantUUID": "582b08f4-2de9-4b5d-8661-f36e730a97da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-24T18:24:53.475Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EuHV1mHHhbsXsPYWUwfZba`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc1ac1f2-5da5-4f29-9bd6-4c36928a5234",
  "isSidechain": true,
  "agentId": "aa90fb53a2c1faac3",
  "requestId": "req_011CbMryYTviM1hjLkYd9Z8f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13b0837d-bcbc-4cf1-b513-d28d9c768e34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Babp6vAuESryiSZyYAC283",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1362,
      "cache_read_input_tokens": 33137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1362,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 13 · 2026-05-24T18:24:53.483Z_

<details><summary>↩ Tool result · `toolu_01EuHV1mHHhbsXsPYWUwfZba`</summary>

```text
1	% method.tex
2	
3	\section{Method}
4	\label{sec:method}
5	
6	Cross-attack generalization could stem from domain exposure, classification supervision, label correctness, label granularity, or domain specificity. Disentangling these factors demands an architecture where exactly one component varies across conditions. DisPeD separates encoder adaptation (Stage~1) from temporal classification (Stage~2). Seven Stage-1 variants share the same training data and downstream pipeline but differ solely in their pretraining objective; each isolates a single factor (Figure~\ref{fig:architecture}).
7	
8	\subsection{Problem Formulation}
9	
10	A conversation $C = \{u_1, a_1, \ldots, u_N, a_N\}$ alternates user turns $u_i$ and assistant responses $a_i$. Given a prefix of $K$ user turns, the model predicts $y \in \{0, 1\}$ (jailbreak vs.\ benign). We restrict input to user turns because adversarial intent resides in the attacker's messages. This formulation supports early detection from partial prefixes.
11	
12	\subsection{Stage 1: Turn-Level Encoder Adaptation}
13	
14	Each user turn $u_i$ is encoded by DeBERTa-v3-base~\citep{he2023debertav3}; the \texttt{[CLS]} embedding $h_i \in \mathbb{R}^D$ serves as the turn representation. Seven variants, summarized in Table~\ref{tab:variants}, share the same training data but differ in objective.
15	
16	\begin{table}[t]
17	\centering
18	\small
19	\caption{Stage-1 encoder variants. All operate on the same training conversations except Wikipedia MLM (matched token count on Wikipedia text).}
20	\label{tab:variants}
21	\begin{tabular}{@{}p{1.6cm}p{2.2cm}p{2.8cm}@{}}
22	\toprule
23	\textbf{Variant} & \textbf{Objective} & \textbf{Tests whether\ldots} \\
24	\midrule
25	9-class & 9-class persuasion + binary intent & full model \\
26	Binary & binary persuasion + binary intent & granularity matters \\
27	Scrambled & random 9-class + binary intent & label correctness matters \\
28	MLM-only & 15\% token masking & supervision is necessary \\
29	Topic & 5-class topic classif. & any task suffices \\
30	Wiki MLM & 15\% masking on Wikipedia & domain specificity matters \\
31	Vanilla & no training & Stage-2 alone suffices \\
32	\bottomrule
33	\end{tabular}
34	\end{table}
35	
36	The \textbf{9-class} variant uses two classification heads: 9-class persuasion strategy classification ($L_{\text{strategy}}$) and binary jailbreak intent ($L_{\text{intent}}$), with combined loss $L = L_{\text{strategy}} + \alpha \cdot L_{\text{intent}}$ ($\alpha = 0.3$, selected from $\{0, 0.3, 0.5, 2.0\}$; all values yield F1\,=\,1.0 on IID; Appendix~\ref{app:lambda}). The taxonomy comprises eight persuasion strategies (rapport building, authority appeal, emotional manipulation, logical reframing, role assignment, gradual escalation, obfuscation, direct request) plus a none category, grounded in PAP~\citep{zeng2024pap} and Cialdini's principles~\citep{cialdini2001influence}. Strategy annotations are produced by Qwen3-8B with structured prompting that includes definitions and examples for each category; inter-annotator agreement between model annotations and a human sample ($n$=50) yields Cohen's $\kappa$=0.78.
37	
38	The \textbf{binary} variant collapses the 9-class taxonomy into persuasive vs.\ non-persuasive, testing whether label granularity matters for detection or robustness.
39	The \textbf{scrambled} variant randomly permutes the 9-class labels across turns using a fixed random permutation (seed 42), preserving classification structure (cross-entropy loss, 9-class output space) while destroying label semantics. This isolates whether the classification objective provides representational benefits independent of label correctness. Robustness is verified across additional random permutations with consistent results (Appendix~\ref{app:random_partition}).
40	The \textbf{MLM-only} variant applies 15\% masked language modeling on the same jailbreak conversation text without any classification head, testing whether unsupervised domain exposure suffices.
41	The \textbf{topic} variant trains a 5-class topic classifier (technology, health, finance, education, general) on the same conversations, testing whether \emph{any} classification task provides the same benefit or whether task alignment matters. This comparison confounds domain relevance with label granularity (5 vs.\ 9 classes) and classification-head architecture; the Wiki-MLM vs.\ JB-MLM pair provides a cleaner isolation of domain effects (Section~\ref{sec:decomposition}).
42	The \textbf{Wikipedia MLM} variant applies the same MLM objective to a token-matched sample of Wikipedia text; this isolates domain-specific from general continued pretraining.
43	The \textbf{vanilla} baseline uses the pretrained DeBERTa-v3-base weights without any continued pretraining; it measures what Stage~2 alone can achieve.
44	
45	\subsection{Stage 2: Conversation-Level Classification}
46	
47	Turn embeddings $\{h_1, \ldots, h_K\}$ from the frozen Stage-1 encoder are aggregated by a 2-layer bidirectional GRU ($d_{\text{hidden}}$=256, dropout 0.3): $\bar{h} = [\overrightarrow{h_K};\; \overleftarrow{h_1}] \in \mathbb{R}^{512}$.
48	A two-layer MLP ($512 \to 256 \to 2$, ReLU activation) maps $\bar{h}$ to $\hat{y} \in \{0, 1\}$.
49	The Stage-1 encoder is frozen during Stage~2 to ensure ablation fairness across all seven variants.
50	We retain BiGRU as the default aggregator for its amenability to representation analysis (CKA, t-SNE), noting that mean pooling achieves comparable detection (Section~\ref{sec:decomposition}). Cross-architecture validation on RoBERTa (Section~\ref{sec:cross_encoder}) yields thirteen configurations across three scales.
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13b0837d-bcbc-4cf1-b513-d28d9c768e34",
  "isSidechain": true,
  "promptId": "270ab91c-e9b9-4a39-b092-16a4d85348b6",
  "agentId": "aa90fb53a2c1faac3",
  "type": "user",
  "uuid": "d062f360-4ff5-4c27-bf57-9d4f308f199d",
  "sourceToolAssistantUUID": "13b0837d-bcbc-4cf1-b513-d28d9c768e34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-24T18:24:53.945Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EDqoq8VfcmXtCtzvSws1WF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d062f360-4ff5-4c27-bf57-9d4f308f199d",
  "isSidechain": true,
  "agentId": "aa90fb53a2c1faac3",
  "requestId": "req_011CbMryYTviM1hjLkYd9Z8f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd6e1914-ed55-428f-ae4c-184be8052be1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Babp6vAuESryiSZyYAC283",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1362,
      "cache_read_input_tokens": 33137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1362,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 15 · 2026-05-24T18:24:53.952Z_

<details><summary>↩ Tool result · `toolu_01EDqoq8VfcmXtCtzvSws1WF`</summary>

```text
1	% experiments.tex
2	
3	\section{Experiments}
4	
5	\paragraph{Terminology.}
6	\emph{Cross-attack OOD}: evaluation on attack families unseen during training; benign distribution remains IID throughout (OOD reflects attack-side shift only). $K$: prefix length (number of conversation turns retained). \emph{DAPT}: all Stage-1 adaptations; we extend \citet{gururangan2020dontstop} to supervised variants. We refer to the performance ranking of DAPT variants across OOD conditions as the \emph{evidence hierarchy} (Section~\ref{sec:decomposition}).
7	
8	\subsection{Setup}
9	
10	\paragraph{Data.}
11	All synthetic data is generated by Qwen3-8B~\citep{qwen3_2025}.
12	The IID dataset contains 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 benign conversations, split into training (350), validation (74), and test (76) with balanced classes.
13	Stage~1 uses training + validation; Stage~2 trains on training, early-stops on validation.
14	OOD evaluation pairs 80 attack-specific conversations with 38 IID-test benign: FITD~\citep{fitd2024}, DD~\citep{deceptivedelight2024}, and ActorAttack~\citep{ren2024actorattack} (118 total each; no template overlap across families).
15	A paraphrased IID test set (BERTScore 0.92) serves as the robustness benchmark (Section~\ref{sec:perturbation}).
16	For human validation, we use ToxicChat~\citep{lin2023toxicchat} (204+204 from real LMSYS interactions).
17	
18	\paragraph{Models.}
19	Seven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method}).
20	Our vanilla DeBERTa+BiGRU configuration is architecturally equivalent to DeepContext~\citep{deepcontext2026} and differs only in encoder choice (DeBERTa-v3-base vs.\ BERT); it serves as our primary baseline.
21	For cross-encoder validation, we replicate vanilla, MLM, and 9-class variants on RoBERTa-base~\citep{liu2019roberta} (Section~\ref{sec:cross_encoder}).
22	We also compare TF-IDF LR, LLM-as-judge (Appendix~\ref{sec:llm_judge}), and Llama Guard~3~8B~\citep{metallamaguard3_2024} (zero-shot; evaluates last-response safety given conversation context), which detects only 1.8\% of multi-turn jailbreaks (5/278 pooled recall; Table~\ref{tab:evidence_hierarchy}).
23	
24	\paragraph{Metrics.}
25	F1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ in Appendix~\ref{sec:full_prefix}).
26	OOD results report 3-seed mean$\pm$std (seeds 42, 123, 456).
27	For pairwise comparisons, we report BCa bootstrap 95\% CIs (10,000 resamples; assumes cross-seed independence) and paired permutation tests; seed-level values confirm all conclusions hold at every seed (Appendix~\ref{app:seed_level}).
28	
29	\paragraph{Training.}
30	Stage-1: learning rate $2 \times 10^{-5}$, batch 16, 4 epochs, MLM masking 15\%.
31	Stage-2: two-layer MLP, 20 epochs.
32	
33	%----------------------------------------------------------------------
34	\subsection{Cross-Attack Generalization}
35	
36	\begin{table}[t]
37	\centering
38	\small
39	\caption{Cross-attack generalization (F1) at $K$=2 and full conversation length. IID: Crescendo; OOD: Deceptive Delight (DD). 3-seed mean$\pm$std where noted; full per-$K$ in Appendix~\ref{sec:full_prefix}.}
40	\label{tab:main_results}
41	\resizebox{\columnwidth}{!}{%
42	\begin{tabular}{@{}lcc|cc@{}}
43	\toprule
44	& \multicolumn{2}{c|}{\textit{IID (Cresc.)}} & \multicolumn{2}{c}{\textit{OOD (DD)}} \\
45	\textbf{Method} & $K$=2 & Full & $K$=2 & Full \\
46	\midrule
47	9-class & \textbf{1.000$\pm$.000} & \textbf{1.000$\pm$.000} & .981$\pm$.013 & \textbf{.997$\pm$.005} \\
48	MLM-only$^{\ddagger}$ & .974 & 1.000 & \textbf{.993$\pm$.009} & .914$\pm$.115 \\
49	Vanilla & .978$\pm$.016 & 1.000$\pm$.000 & .479$\pm$.038 & .312$\pm$.026 \\
50	TF-IDF LR$^{\S}$ & 1.000 & 1.000 & 1.000 & .961 \\
51	\bottomrule
52	\end{tabular}}
53	\vspace{-2pt}
54	{\footnotesize $^{\ddagger}$MLM-only IID reports single seed (42); OOD reports 3-seed. $^{\S}$TF-IDF is deterministic (no std).}
55	\end{table}
56	
57	Vanilla encoders collapse under cross-attack transfer; domain-adapted variants recover near-perfect detection (Table~\ref{tab:main_results}, Figure~\ref{fig:cross_attack_bar}).
58	On OOD DD, vanilla drops to F1\,=\,0.312$\pm$0.026 and worsens with more turns (0.628$\to$0.312 at Full), consistent with attack turns occupying benign embedding regions~\citep{bullwinkel2025repeng}. MLM recovers to $\geq$0.97 at $K \leq 5$ without labels but is unstable at full length (0.914$\pm$0.115); 9-class maintains 0.997$\pm$0.005.
59	On strategy-diverse ActorAttack, TF-IDF collapses (0.261) while 9-class maintains 0.972$\pm$0.026, a 71\,pp gap confirming domain-adapted representations capture beyond-lexical features.
60	Seed-level results confirm consistent separation (Table~\ref{tab:seed_level}; bootstrap CIs non-overlapping, permutation $p < 0.0001$). FITD is non-discriminative (all F1\,$\geq$\,0.990).
61	
62	\begin{figure}[t]
63	\centering
64	\includegraphics[width=\columnwidth]{figures/paper/fig2_cross_attack_bar.pdf}
65	\caption{Cross-attack overview (F1 at full conversation length). DisPeD (9-class) maintains near-perfect detection across IID and both OOD families; vanilla collapses on OOD DD. FITD is non-discriminative for all methods.}
66	\label{fig:cross_attack_bar}
67	\end{figure}
68	
69	Prefix-length analysis (Appendix Table~\ref{tab:full_prefix}) confirms 9-class stability across all prefixes (0.972--0.997) vs.\ MLM instability at full length (0.914$\pm$0.115) and vanilla degradation (0.628$\to$0.312).
70	
71	%----------------------------------------------------------------------
72	\subsection{Decomposing the Detection Mechanism}
73	\label{sec:decomposition}
74	
75	\begin{table}[t]
76	\centering
77	\small
78	\caption{Evidence hierarchy on OOD DD and ActorAttack (AA) at full conversation length (3-seed mean$\pm$std where available). OOD F1 reflects attack-side generalization only; benign samples are IID from training distribution (benign-side shift evaluated in Section~\ref{sec:benign_shift}). Bold indicates best per column. All variants share the same Stage-2 pipeline. Full per-prefix results in Appendix Tables~\ref{tab:full_prefix} and~\ref{tab:actorattack_full}. Bottom rows: full dual-OOD evaluation with WildChat benign replacing IID benign (Appendix~\ref{app:dual_ood}).}
79	\label{tab:evidence_hierarchy}
80	\resizebox{\columnwidth}{!}{%
81	\begin{tabular}{@{}lccc@{}}
82	\toprule
83	\textbf{Variant} & DD-Full & AA-Full & DD-$K$=2 \\
84	\midrule
85	9-class (full model) & .997$\pm$.005 & .972$\pm$.026 & .981$\pm$.013 \\
86	Binary (2-class) & \textbf{1.000$\pm$.000} & \textbf{.990$\pm$.008} & .994$\pm$.009 \\
87	Scrambled labels & .997$\pm$.005 & .951$\pm$.043 & .981$\pm$.026 \\
88	MLM-only$^{\ddagger}$ (no labels) & .914$\pm$.115 & .893$\pm$.080 & .993$\pm$.009 \\
89	Mean pooling$^{*}$ & .991$\pm$.013 & .962$\pm$.015 & .994$\pm$.009 \\
90	\midrule
91	Topic classif.\ (5-class) & .541$\pm$.207 & .625$\pm$.141 & .593$\pm$.166 \\
92	Wikipedia MLM & .904$\pm$.115 & .686$\pm$.297 & .911$\pm$.073 \\
93	Vanilla DeBERTa & .312$\pm$.026 & .258$\pm$.000 & .479$\pm$.038 \\
94	TF-IDF LR$^{\dagger}$ & .961 & .261 & \textbf{1.000} \\
95	Llama Guard~3$^{\P}$ & .024 & .000 & -- \\
96	\midrule
97	\multicolumn{4}{l}{\textit{Dual-OOD (WildChat benign; Section~\ref{sec:benign_shift})}} \\[2pt]
98	9-class (no adapt) & .855 & .842 & -- \\
99	9-class (+10-shot) & .994 & .981 & -- \\
100	\bottomrule
101	\end{tabular}}
102	\vspace{-2pt}
103	{\footnotesize $^{*}$9-class encoder with mean pooling replacing BiGRU. $^{\dagger}$Deterministic (no std). $^{\ddagger}$MLM-only IID (Table~\ref{tab:main_results}) is single-seed (42); all OOD values are 3-seed. $^{\P}$Zero-shot; no domain training.}
104	\end{table}
105	
106	A clear \emph{evidence hierarchy} emerges across seven variants on synthetic multi-turn data (Table~\ref{tab:evidence_hierarchy}, Figure~\ref{fig:evidence_hierarchy}), ordered by OOD detection at full conversation length: vanilla $<$ topic $\ll$ MLM $<$ classification-supervised ($\approx$\,1.0 on DD).
107	
108	\begin{figure}[t]
109	\centering
110	\includegraphics[width=\columnwidth]{figures/paper/fig3_evidence_hierarchy.pdf}
111	\caption{Evidence hierarchy across evaluation conditions. Classification-based DAPT outperforms MLM and vanilla on synthetic OOD attacks (DD, AA), but the hierarchy reverses on human-authored single-turn data (ToxicChat), where JB-MLM leads.}
112	\label{fig:evidence_hierarchy}
113	\end{figure}
114	
115	\paragraph{Domain exposure is the primary observed factor.}
116	MLM bridges $\sim$60\,pp from vanilla (0.312$\pm$0.026 $\to$ 0.914$\pm$0.115) without labels; this supports the DAPT interpretation~\citep{gururangan2020dontstop}. TF-IDF collapse on ActorAttack (0.261 vs.\ 9-class 0.972) confirms that domain-adapted representations capture features beyond lexical overlap.
117	All three classification-supervised variants converge to equivalent detection (F1 = 0.997--1.000); McNemar's ($p > 0.13$) and paired permutation tests ($p \geq 0.40$) provide descriptive evidence suggesting equivalence. Extended to $n$\,=\,10 seeds, TOST (margin = 5\,pp) confirms equivalence on DD ($p < 10^{-8}$, $d$\,=\,$-$0.14; Table~\ref{tab:tost_sensitivity}) and FITD ($p < 10^{-8}$, $d \approx 0$). Label quality and granularity are non-factors for template-attack detection (DD/FITD: $|d| \leq 0.14$), but strategy-diverse ActorAttack retains moderate label sensitivity ($d$\,=\,0.44, TOST $p$\,=\,0.183). For template attacks, any domain-relevant classification objective suffices; the objective's structural role---partitioning the representation space---matters more than label semantics. Strategy-diverse attacks mark a difficulty boundary for this sufficiency.
118	Classification supervision is associated with 3--23$\times$ lower cross-seed variance over MLM on synthetic OOD (std 0.005 vs.\ 0.115 on DD; 3 seeds; Appendix~\ref{app:ensemble}), though this reverses on human-authored data (Section~\ref{sec:human_data}).
119	
120	\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}
121	Wikipedia MLM (0.904$\pm$0.115) nearly matches jailbreak-domain MLM at full length (1\,pp gap), though jailbreak-domain text provides an 8\,pp advantage at early prefixes ($K$=2: 0.993 vs.\ 0.911).
122	Perturbation analysis (Section~\ref{sec:perturbation}) reveals a sharper domain specificity effect: Wikipedia MLM degrades by $\sim$12\,pp under adversarial paraphrasing while jailbreak-domain MLM degrades by only 2.6\,pp.
123	
124	\paragraph{Misaligned supervision destabilizes generalization.}
125	Topic classification's poor performance (0.541$\pm$0.207) is consistent with misaligned supervision; the cleaner test isolating domain exposure is Wiki-MLM vs.\ JB-MLM (Section~\ref{sec:decomposition}).
126	
127	\paragraph{Evidence hierarchy on strategy-diverse attacks.}
128	ActorAttack~\citep{ren2024actorattack} preserves the same hierarchy (Figure~\ref{fig:evidence_hierarchy}) with wider gaps: TF-IDF collapses (0.261) while classification variants converge (0.951--0.990, max gap 3.9\,pp); DAPT provides $\sim$71\,pp over vanilla (Appendix~\ref{sec:actorattack_full},~\ref{app:aa_error}).
129	
130	\paragraph{Temporal modeling.}
131	Mean pooling matches BiGRU (F1 gap $\leq$ 1\,pp; Appendix~\ref{app:temporal}) and turn-order shuffling is negligible ($|\Delta| < 1$\,pp), confirming detection relies on per-turn content rather than sequential patterns.
132	
133	%----------------------------------------------------------------------
134	\subsection{Cross-Encoder Validation}
135	\label{sec:cross_encoder}
136	
137	\begin{table}[t]
138	\centering
139	\footnotesize
140	\caption{Cross-encoder comparison on OOD Full (3-seed mean$\pm$std). DD = Deceptive Delight, AA = ActorAttack. Bold indicates best per encoder group.}
141	\label{tab:cross_encoder}
142	\begin{tabular}{@{}lcc@{}}
143	\toprule
144	\textbf{Variant} & DD & AA \\
145	\midrule
146	\multicolumn{3}{l}{\textit{DeBERTa-v3-base (184M)}} \\[2pt]
147	Vanilla & .312$\pm$.026 & .258$\pm$.000 \\
148	MLM & .914$\pm$.115 & .893$\pm$.080 \\
149	9-class & \textbf{.997$\pm$.005} & \textbf{.972$\pm$.026} \\
150	\midrule
151	\multicolumn{3}{l}{\textit{RoBERTa-base (125M)}} \\[2pt]
152	Vanilla & .981$\pm$.026 & .466$\pm$.163 \\
153	MLM & .987$\pm$.018 & .730$\pm$.201 \\
154	9-class & \textbf{.994$\pm$.005} & \textbf{.939$\pm$.046} \\
155	\midrule
156	\multicolumn{3}{l}{\textit{RoBERTa-large (355M)}} \\[2pt]
157	Vanilla & .927$\pm$.036 & \textbf{1.000$\pm$.000} \\
158	MLM & .884$\pm$.065 & .874$\pm$.014 \\
159	9-class & \textbf{.987$\pm$.004} & .946$\pm$.057 \\
160	\bottomrule
161	\end{tabular}
162	\end{table}
163	
164	To test whether the evidence hierarchy depends on encoder choice, we replicate vanilla, MLM, and 9-class on RoBERTa-base~\citep{liu2019roberta} (Table~\ref{tab:cross_encoder}).
165	On DD, RoBERTa-base vanilla already achieves 0.981$\pm$0.026 (vs.\ DeBERTa 0.312$\pm$0.026), so DAPT adds only 1.3\,pp. ActorAttack exposes this as DD's simplicity: RoBERTa-base vanilla collapses to 0.466$\pm$0.163, a 51.5\,pp drop, while domain-adapted variants recover (9-class: 0.939$\pm$0.046).
166	
167	RoBERTa-large (355M) reverses the DAPT advantage on ActorAttack (vanilla 1.000 vs.\ 9-class 0.946; Table~\ref{tab:roberta_large_lr}), revealing a difficulty threshold: base-scale encoders require DAPT for all attacks, while sufficient capacity renders it unnecessary. A BERT-base proxy confirms DAPT, not architecture, drives generalization (Appendix~\ref{app:bert_proxy}).
168	
169	%----------------------------------------------------------------------
170	\subsection{Mixed-LLM Training}
171	
172	All preceding experiments use single-source (Qwen3-8B) data. To test whether the evidence hierarchy transfers when training data mixes LLM sources, we train on 250 Qwen + 250 Llama-3.1-8B conversations (Table~\ref{tab:mixed_llm}).
173	Classification-based DAPT is the only variant that substantially outperforms vanilla: 9-class achieves DD OOD F1\,=\,0.818$\pm$0.096 (+53\,pp over vanilla 0.291$\pm$0.065), while MLM drops to vanilla level (0.289$\pm$0.101). On strategy-diverse ActorAttack, detection degrades to chance level (9-class F1\,=\,0.504$\pm$0.107, indistinguishable from majority baseline at $n$\,=\,3).
174	Classification supervision thus generalizes across LLM sources where unsupervised pretraining does not (Appendix~\ref{app:mixed_llm}).
175	
176	%----------------------------------------------------------------------
177	\subsection{Human Data Validation}
178	\label{sec:human_data}
179	
180	Since both training and OOD evaluation data are Qwen3-8B-generated, we validate on ToxicChat~\citep{lin2023toxicchat} (204 human-written jailbreak attempts + 204 benign conversations from real LMSYS interactions).
181	
182	\begin{table}[t]
183	\centering
184	\small
185	\caption{Human data validation on ToxicChat~\citep{lin2023toxicchat} (macro F1, 3-seed mean$\pm$std). Bold indicates best. Single-turn data from real LMSYS user interactions, independent of Qwen3-8B.}
186	\label{tab:human_data}
187	\begin{tabular}{@{}lc@{}}
188	\toprule
189	\textbf{Variant} & Macro F1 \\
190	\midrule
191	JB-MLM & \textbf{.837$\pm$.013} \\
192	Wiki-MLM & .791$\pm$.093 \\
193	Binary & .705$\pm$.072 \\
194	Scrambled & .616$\pm$.056 \\
195	9-class & .596$\pm$.087 \\
196	Topic & .496$\pm$.042 \\
197	\midrule
198	Vanilla & .413$\pm$.021 \\
199	\bottomrule
200	\end{tabular}
201	\end{table}
202	
203	The ordering reverses (Figure~\ref{fig:evidence_hierarchy}): JB-MLM leads (0.837$\pm$0.013) while 9-class ranks lower (0.596$\pm$0.087; $p < 0.001$). All jailbreak-domain DAPT variants exceed vanilla by 18--42\,pp, confirming transfer to human-written attacks. ToxicChat is single-turn, so the classification head provides no advantage.
204	
205	\begin{figure}[t]
206	\centering
207	\includegraphics[width=\columnwidth]{figures/paper/fig_hierarchy_reversal.pdf}
208	\caption{Condition-specific evidence hierarchy. On synthetic OOD (DD), classification DAPT dominates; on human-authored ToxicChat, unsupervised MLM leads---rank positions reverse entirely.}
209	\label{fig:hierarchy_reversal}
210	\end{figure}
211	
212	\begin{figure}[t]
213	\centering
214	\includegraphics[width=\columnwidth]{figures/paper/fig_fpr_adaptation.pdf}
215	\caption{Few-shot benign adaptation reduces FPR below the 5\% deployment threshold with 10--25 conversations across three platforms.}
216	\label{fig:fpr_adaptation}
217	\end{figure}
218	
219	%----------------------------------------------------------------------
220	\subsection{Robustness and Strategy Analysis}
221	\label{sec:perturbation}
222	
223	Under adversarial paraphrasing (BERTScore 0.92), classification variants achieve zero degradation on OOD DD while non-adapted models degrade by $\sim$12\,pp; on ActorAttack, DAPT degrades ($\Delta$\,=\,$-$20.4\,pp) but maintains 52\,pp over vanilla (Table~\ref{tab:ood_perturbation}; Appendices~\ref{sec:perturbation_full},~\ref{sec:strategy_full}). The 9-class taxonomy characterizes known attacks ($\kappa$\,=\,0.78) but degrades on OOD ($\kappa$\,=\,0.126; Appendix~\ref{app:strategy_pred}); detection operates through \texttt{[CLS]} embeddings, not strategy accuracy.
224	
225	%----------------------------------------------------------------------
226	\subsection{Benign Distribution Shift}
227	\label{sec:benign_shift}
228	
229	On WildChat benign conversations, 9-class FPR rises to 68.1\% (Appendix~\ref{app:wildchat_fpr}). Few-shot adaptation (encoder frozen, $N$ benign conversations) resolves this (Figure~\ref{fig:fpr_adaptation}): 10 WildChat conversations reduce FPR to 0\%, 25 OASST2 to 1.5\% (consistent across WildChat, OASST2, and ShareGPT; Appendix~\ref{app:oasst2}); dual-OOD F1 drops 13--14\,pp without adaptation but recovers within 0.3\,pp (Appendix~\ref{app:dual_ood}).
230	
231	%----------------------------------------------------------------------
232	\subsection{Efficiency and Data Requirements}
233	\label{sec:efficiency}
234	
235	\begin{table}[t]
236	\centering
237	\footnotesize
238	\caption{Inference efficiency (single A100). DeBERTa+BiGRU achieves real-time latency with 43$\times$ fewer parameters than LLM-as-judge. $^{\dagger}$LLM latency from OOD evaluation; cross-condition comparison is indicative.}
239	\label{tab:efficiency_main}
240	\resizebox{\columnwidth}{!}{%
241	\begin{tabular}{@{}lrcr@{}}
242	\toprule
243	\textbf{Method} & Latency (ms) & Params & VRAM \\
244	\midrule
245	TF-IDF+LR & 0.43$\pm$0.05 & $\sim$10K & CPU \\
246	DeBERTa+BiGRU (ours) & 12.1$\pm$1.2 & 186.7M & 862\,MB \\
247	Qwen3-8B 3-shot$^{\dagger}$ & $\sim$5{,}200 & 8B & $\sim$16\,GB \\
248	\bottomrule
249	\end{tabular}}
250	\end{table}
251	
252	DeBERTa+BiGRU processes a conversation in 12.1\,ms---24.3$\times$ faster than Qwen3-8B 3-shot under matched conditions (Table~\ref{tab:efficiency_main}; Appendix~\ref{app:efficiency})---with 43$\times$ fewer parameters and 862\,MB GPU memory, enabling deployment on consumer hardware. The speed gap over TF-IDF+LR (28$\times$) purchases +71\,pp on ActorAttack OOD (F1\,=\,0.972 vs.\ 0.261). Meanwhile, 9-class DAPT reaches near-saturation with only 50 training conversations (AA OOD F1\,$\geq$\,0.969; Appendix~\ref{app:data_efficiency}), requiring just 14\% of the full training set while exceeding vanilla at any training size by $\geq$48\,pp.
253	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd6e1914-ed55-428f-ae4c-184be8052be1",
  "isSidechain": true,
  "promptId": "270ab91c-e9b9-4a39-b092-16a4d85348b6",
  "agentId": "aa90fb53a2c1faac3",
  "type": "user",
  "uuid": "763ec69e-48fc-4c47-a344-fdca62c0e5a3",
  "sourceToolAssistantUUID": "cd6e1914-ed55-428f-ae4c-184be8052be1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-24T18:24:54.417Z_

<details open><summary>🔧 Tool call — Read · `toolu_017pUUgZX6FvGT5ypUiTR6hL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "763ec69e-48fc-4c47-a344-fdca62c0e5a3",
  "isSidechain": true,
  "agentId": "aa90fb53a2c1faac3",
  "requestId": "req_011CbMryYTviM1hjLkYd9Z8f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e25eccef-d558-49bd-8307-6e5ed79b4ba3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Babp6vAuESryiSZyYAC283",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1362,
      "cache_read_input_tokens": 33137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1362,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 17 · 2026-05-24T18:24:54.425Z_

<details><summary>↩ Tool result · `toolu_017pUUgZX6FvGT5ypUiTR6hL`</summary>

```text
1	% conclusion.tex
2	
3	\section{Discussion}
4	\label{sec:discussion}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{figures/paper/fig4_svd_subspace.pdf}
9	\caption{Test representations projected onto top-2 SVD directions. 9-class DAPT produces clear cluster separation absent in vanilla.}
10	\label{fig:svd_subspace}
11	\end{figure}
12	
13	\paragraph{Discriminative compression and label equivalence.}
14	Three observations argue against a topic shortcut: unstable topic OOD (F1\,=\,0.541$\pm$0.207), scrambled labels within 3.9\,pp, and label-free MLM detection (F1\,$\geq$\,0.97).
15	Classification DAPT compresses features into few dimensions (participation ratio 3.7--9.4 vs.\ 25--32; Figure~\ref{fig:svd_subspace}; Appendices~\ref{app:representation}--\ref{app:tsne}), localizing to 3 SVD dimensions in layers 8--12 \citep{zhang2021understanding}; a probe confirms sufficiency, and removal degrades DD by 17\,pp (Appendices~\ref{app:discriminative_probe},~\ref{app:svd_necessity}).
16	
17	\paragraph{Cross-condition transfer and boundaries.}
18	ToxicChat (+18--42\,pp) and cross-LLM experiments (Appendix~\ref{app:cross_llm}) confirm transfer beyond single-LLM artifacts. On single-turn human-authored data the hierarchy reverses (MLM leads; Appendix~\ref{app:confidence}); truncated analysis localizes the reversal to distributional gap rather than detection mechanism (Appendix~\ref{app:truncated}). Mixed-LLM 9-class maintains 0.818 while MLM collapses; at 355M, DAPT becomes counterproductive (vanilla AA\,=\,1.000 vs.\ 9-class 0.946). WildChat FPR reaches 68.1\% (synthetic-to-real shift). Length-matched evaluation ($N$=155) shows negligible DD change ($\Delta$\,=\,$-$2.5\,pp; Appendices~\ref{app:length_independence},~\ref{app:length}); ActorAttack padding collapse ($-$57.9\,pp) reflects signal dilution (Appendix~\ref{app:truncated}).
19	
20	\paragraph{Deployment implications.}
21	Our findings suggest a capacity-aware deployment strategy. At base scale (125--184M), any domain-relevant classification objective recovers OOD detection---scrambled labels perform equivalently on template attacks, so practitioners need not invest in annotation quality for this regime. When facing strategy-diverse attacks (e.g., ActorAttack), the label effect resurfaces ($d$\,=\,0.44), favoring semantically meaningful taxonomies. At sufficient capacity ($\geq$355M), DAPT becomes unnecessary and potentially counterproductive; the decision to adapt should be conditioned on encoder scale. Independent of adaptation choice, few-shot benign calibration (10--25 conversations per deployment domain) resolves false-positive rates without requiring target-domain attack data, enabling deployment across platforms with minimal data collection. The 184M-parameter pipeline maintains 24.3$\times$ inference speedup over LLM-as-judge alternatives (43$\times$ fewer parameters; Table~\ref{tab:efficiency_main}), making it suitable for real-time monitoring at scale.
22	
23	\section{Conclusion}
24	
25	Classification DAPT recovers OOD detection at base scale (F1\,=\,0.97--1.0 vs.\ vanilla 0.26--0.31), though not under mixed-LLM training on diverse attacks (ActorAttack F1\,=\,0.504); on single-turn human-authored data, the hierarchy reverses (ToxicChat MLM 0.837 vs.\ classification 0.596)---condition-specific, counterproductive at 355M. Few-shot adaptation reduces FPR from 58--68\% to 0--1.5\%; this ablation framework provides a template for future controlled studies of domain adaptation in safety-critical NLP tasks.
26	
27	\section{Limitations}
28	\label{sec:limitations}
29	
30	\begin{itemize}[nosep,leftmargin=*]
31	\item \textbf{Synthetic data.} All findings derive from synthetic conversations (single LLM, Qwen3-8B; 350 training, 3 seeds); the hierarchy reverses on human single-turn data (ToxicChat), and no human-generated multi-turn jailbreak dataset exists.
32	\item \textbf{IID benign assumption.} OOD F1 assumes IID benign data; few-shot adaptation recovers performance but is validated on only two platforms ($n \leq 50$).
33	\item \textbf{Scope.} Only persuasion-mediated multi-turn attacks at base-to-large encoder scale (125--355M) are addressed; single-turn token-level attacks and non-text modalities are out of scope.
34	\end{itemize}
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e25eccef-d558-49bd-8307-6e5ed79b4ba3",
  "isSidechain": true,
  "promptId": "270ab91c-e9b9-4a39-b092-16a4d85348b6",
  "agentId": "aa90fb53a2c1faac3",
  "type": "user",
  "uuid": "8aac933a-a91f-4239-8638-fde59d4d9b84",
  "sourceToolAssistantUUID": "e25eccef-d558-49bd-8307-6e5ed79b4ba3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-24T18:24:54.887Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BCPEF8emj2mBZjRCNjeDxK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8aac933a-a91f-4239-8638-fde59d4d9b84",
  "isSidechain": true,
  "agentId": "aa90fb53a2c1faac3",
  "requestId": "req_011CbMryYTviM1hjLkYd9Z8f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "978651f3-c6ad-4df2-8338-d5bae1df2359",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Babp6vAuESryiSZyYAC283",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1362,
      "cache_read_input_tokens": 33137,
      "output_tokens": 552,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1362
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 552,
          "cache_read_input_tokens": 33137,
          "cache_creation_input_tokens": 1362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1362,
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

_source line 19 · 2026-05-24T18:24:55.191Z_

<details><summary>↩ Tool result · `toolu_01BCPEF8emj2mBZjRCNjeDxK`</summary>

```text
1	% appendix.tex — Supplementary material
2	
3	\appendix
4	
5	\section{LLM-as-Judge Baseline}
6	\label{sec:llm_judge}
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{LLM-as-judge jailbreak detection. IID: binary F1 (Crescendo test set); OOD: macro F1 (DD = Deceptive Delight, AA = ActorAttack). GPT-5.5 F1 values exclude unparseable responses and represent upper bounds.}
12	\label{tab:llm_judge}
13	\begin{tabular}{@{}lcccr@{}}
14	\toprule
15	\textbf{Method} & DD & AA & IID & Unparse. \\
16	\midrule
17	\multicolumn{5}{l}{\textit{Zero-shot}} \\[2pt]
18	GPT-5.5 & -- & -- & .383 & 30--47\% \\
19	Qwen3-8B & .244 & .244 & .100 & 0\% \\
20	\midrule
21	\multicolumn{5}{l}{\textit{3-shot}} \\[2pt]
22	Qwen3-8B & .566 & .652 & -- & 0\% \\
23	\midrule
24	\multicolumn{5}{l}{\textit{Trained classifier}} \\[2pt]
25	9-class (ours) & \textbf{.994} & \textbf{.972} & \textbf{1.000} & 0\% \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:llm_judge} reports LLM-as-judge performance on IID and OOD data.
31	On IID Crescendo, GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 = 0.383 on full conversations; 30--47\% of responses are unparseable.
32	Qwen3-8B performs worse (IID F1 = 0.100).
33	On OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 on both DD and ActorAttack by predicting nearly all conversations as benign.
34	Even with 3-shot prompting, Qwen3-8B reaches only 0.566 (DD) and 0.652 (AA), while DisPeD maintains macro F1 $\geq$ 0.972.
35	The poor performance of content-level reasoning on unseen attack families underscores the necessity of trained classifiers with domain-adapted representations.
36	
37	\section{Full Cross-Attack Results by Prefix}
38	\label{sec:full_prefix}
39	
40	\begin{table*}[t]
41	\centering
42	\small
43	\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\pm$std where available. ``--'' indicates insufficient conversation length for that prefix (FITD conversations contain 2--3 turns).}
44	\label{tab:full_prefix}
45	\begin{tabular}{@{}lccccc@{}}
46	\toprule
47	\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\
48	\midrule
49	\multicolumn{6}{l}{\textit{IID (Crescendo)}} \\[2pt]
50	9-class (ours) & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 \\
51	MLM-only & .960 & .974 & .987 & 1.000 & 1.000 \\
52	Vanilla DeBERTa & .968$\pm$.033 & .978$\pm$.016 & .987$\pm$.000 & .982$\pm$.014 & 1.000$\pm$.000 \\
53	TF-IDF LR & 1.000 & 1.000 & 1.000 & 1.000 & 1.000 \\
54	\midrule
55	\multicolumn{6}{l}{\textit{OOD (Deceptive Delight)}} \\[2pt]
56	9-class (ours) & .990$\pm$.013 & .981$\pm$.013 & .972$\pm$.026 & .997$\pm$.005 & .997$\pm$.005 \\
57	Binary & .994$\pm$.009 & .994$\pm$.009 & .984$\pm$.008 & 1.000$\pm$.000 & 1.000$\pm$.000 \\
58	Scrambled & .997$\pm$.005 & .981$\pm$.026 & .975$\pm$.029 & .997$\pm$.005 & .997$\pm$.005 \\
59	MLM-only & .973$\pm$.019 & .993$\pm$.009 & .997$\pm$.005 & .997$\pm$.005 & .914$\pm$.115 \\
60	Vanilla DeBERTa & .628$\pm$.038 & .479$\pm$.038 & .389$\pm$.027 & .351$\pm$.030 & .312$\pm$.026 \\
61	TF-IDF LR & 1.000 & 1.000 & .994 & 1.000 & .961 \\
62	\midrule
63	\multicolumn{6}{l}{\textit{OOD (FITD)}} \\[2pt]
64	9-class (ours) & 1.000$\pm$.000 & .997$\pm$.005 & -- & -- & 1.000$\pm$.000 \\
65	Vanilla DeBERTa & .954$\pm$.039 & .952$\pm$.061 & -- & -- & .994$\pm$.009 \\
66	TF-IDF LR & 1.000 & -- & -- & -- & 1.000 \\
67	\bottomrule
68	\end{tabular}
69	\end{table*}
70	
71	\section{ActorAttack Full Results}
72	\label{sec:actorattack_full}
73	
74	\begin{table*}[t]
75	\centering
76	\small
77	\caption{Full ActorAttack OOD results (F1) at all prefix lengths. 3-seed mean$\pm$std (Binary per-$K$ reports $n$=2; Full is 3-seed).}
78	\label{tab:actorattack_full}
79	\begin{tabular}{@{}lccccc@{}}
80	\toprule
81	\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\
82	\midrule
83	\multicolumn{6}{l}{\textit{DeBERTa-v3}} \\[2pt]
84	Binary & .788$\pm$.020 & \textbf{.935$\pm$.018} & \textbf{.976$\pm$.005} & \textbf{.995$\pm$.005} & \textbf{.990$\pm$.008} \\
85	9-class & .773$\pm$.041 & .855$\pm$.048 & .921$\pm$.046 & .966$\pm$.028 & .972$\pm$.026 \\
86	Scrambled & .652$\pm$.034 & .804$\pm$.053 & .854$\pm$.046 & .910$\pm$.052 & .951$\pm$.043 \\
87	MLM-only & .736$\pm$.150 & .909$\pm$.058 & .945$\pm$.039 & .929$\pm$.033 & .893$\pm$.080 \\
88	Wiki MLM & .656$\pm$.224 & .672$\pm$.252 & .693$\pm$.280 & .689$\pm$.285 & .686$\pm$.297 \\
89	Topic & .513$\pm$.077 & .580$\pm$.109 & .565$\pm$.100 & .615$\pm$.111 & .625$\pm$.141 \\
90	Vanilla & .337$\pm$.049 & .306$\pm$.026 & .284$\pm$.011 & .262$\pm$.006 & .258$\pm$.000 \\
91	TF-IDF LR & .633 & .730 & .571 & .242 & .261 \\
92	\midrule
93	\multicolumn{6}{l}{\textit{RoBERTa}} \\[2pt]
94	9-class & \textbf{.738$\pm$.033} & .805$\pm$.033 & .884$\pm$.066 & .925$\pm$.066 & .939$\pm$.046 \\
95	MLM & .633$\pm$.133 & .665$\pm$.150 & .713$\pm$.174 & .719$\pm$.184 & .730$\pm$.201 \\
96	Vanilla & .410$\pm$.126 & .425$\pm$.143 & .432$\pm$.144 & .466$\pm$.144 & .466$\pm$.163 \\
97	\bottomrule
98	\end{tabular}
99	\end{table*}
100	
101	Table~\ref{tab:actorattack_full} reveals three distinct prefix-length patterns. The 9-class model improves monotonically from $K$=1 to Full (+20\,pp), consistent with cumulative evidence accumulation across turns. Vanilla DeBERTa \emph{decreases} with more turns (0.337 at $K$=1 to 0.258 at Full), suggesting that additional attack turns push representations further into benign embedding regions. MLM peaks at $K$=3 (0.945) then declines to 0.893 at Full, indicating that unsupervised domain exposure captures early-turn patterns but is unstable under extended sequences.
102	
103	\subsection{Error Analysis}
104	\label{app:aa_error}
105	
106	Per-sample majority vote across 3 seeds yields 98.3\% accuracy on ActorAttack OOD (2 false negatives, 0 false positives). No sample is misclassified by all three seeds; all 7 seed-specific errors are false negatives concentrated in shorter conversations (3--6 turns). On these 7 error samples, vanilla achieves 0/3 correct votes per sample, while 9-class majority vote correctly classifies 5/7, confirming that domain adaptation provides robust per-sample coverage even where individual seeds fail.
107	
108	\section{Perturbation Robustness}
109	\label{sec:perturbation_full}
110	
111	\begin{table}[t]
112	\centering
113	\small
114	\caption{Perturbation behavior under adversarial paraphrasing on IID Crescendo ($n$=76). $\Delta$: F1 degradation (pp). Classification-supervised variants achieve zero degradation at full length; this pattern does not generalize to ActorAttack.}
115	\label{tab:perturbation}
116	\begin{tabular}{@{}lcccc@{}}
117	\toprule
118	\textbf{Method} & $\Delta$ Full & $\Delta$ $K$=1 & $\Delta$ $K$=2 & $\Delta$ $K$=3 \\
119	\midrule
120	9-class (ours) & \textbf{0.0} & \textbf{$-$2.6} & \textbf{0.0} & \textbf{0.0} \\
121	Scrambled & \textbf{0.0} & $-$5.3 & $-$2.6 & \textbf{0.0} \\
122	Binary & \textbf{0.0} & $-$9.2 & $-$2.6 & \textbf{0.0} \\
123	\midrule
124	TF-IDF LR & $-$1.3 & $-$9.6 & $-$4.1 & $-$1.3 \\
125	MLM-only & $-$2.6 & $-$9.2 & $-$4.0 & $-$4.0 \\
126	Topic (seed 42) & $-$4.0 & $-$2.7 & $-$2.7 & \textbf{0.0} \\
127	\midrule
128	Wikipedia MLM & $-$12.1 & $-$12.4 & $-$15.4 & $-$17.9 \\
129	Vanilla DeBERTa & $-$11.8 & $-$14.6 & $-$12.1 & $-$13.8 \\
130	\bottomrule
131	\end{tabular}
132	\end{table}
133	
134	Table~\ref{tab:perturbation} shows perturbation behavior on IID data.
135	Classification-supervised variants (9-class, binary, scrambled) achieve zero degradation at full conversation length regardless of label correctness.
136	Models without jailbreak-domain exposure (Wikipedia MLM, vanilla) degrade by $\sim$12\,pp.
137	McNemar's test finds no significant pairwise differences among classification-supervised variants (all $p > 0.13$), though with $\leq$7 discordant pairs, statistical power is limited.
138	
139	\begin{table}[t]
140	\centering
141	\small
142	\caption{Perturbation robustness on OOD Deceptive Delight ($n$=118). $\Delta$: F1 change (pp) from clean to paraphrased. 3-seed mean$\pm$std where available.}
143	\label{tab:ood_perturbation}
144	\resizebox{\columnwidth}{!}{%
145	\begin{tabular}{@{}lcccc@{}}
146	\toprule
147	\textbf{Variant} & Clean Full & Pert.\ Full & $\Delta$ Full & $\Delta$ $K$=1 \\
148	\midrule
149	9-class & .994$\pm$.005 & 1.000$\pm$.000 & +0.6 & +0.6 \\
150	Binary & 1.000$\pm$.000 & 1.000$\pm$.000 & 0.0 & +0.6 \\
151	Scrambled & .994$\pm$.005 & 1.000$\pm$.000 & +0.6 & $-$0.3 \\
152	\midrule
153	JB MLM & .914$\pm$.115 & .941 & +2.7 & 0.0 \\
154	Wiki MLM$^{*}$ & .904$\pm$.115 & .872 & $-$3.3 & $-$3.2 \\
155	Vanilla$^{\dagger}$ & .312$\pm$.026 & .339$\pm$.055 & +2.7 & $-$6.8$\pm$1.1 \\
156	\bottomrule
157	\end{tabular}}
158	\vspace{-2pt}
159	{\footnotesize $^{*}$Wiki MLM degradation is seed-driven: seed 42 accounts for $-$9.8\,pp; other seeds show 0.0\,pp change.\\$^{\dagger}$Vanilla $\Delta$ Full = +2.7\,pp reflects floor-effect noise (baseline 0.312, std 0.055), not meaningful improvement.}
160	\end{table}
161	
162	On OOD DD, the IID pattern replicates: classification-supervised variants show zero degradation while McNemar's test confirms 9-class vs.\ vanilla significance ($p < 0.001$, 49--78 discordant pairs).
163	On OOD ActorAttack, domain-adapted variants degrade substantially (9-class $\Delta$\,=\,$-$20.4$\pm$13.5\,pp, MLM $-$35.3\,pp), but perturbation narrows rather than closes the adapted vs.\ non-adapted gap: 9-class perturbed F1 = 0.768 vs.\ vanilla 0.248 (McNemar $p < 0.001$).
164	Domain specificity also manifests: Wikipedia MLM degrades by $\sim$12\,pp while jailbreak-domain MLM degrades by only 2.6\,pp.
165	
166	\section{Strategy Trajectory Analysis}
167	\label{sec:strategy_full}
168	
169	\begin{figure*}[t]
170	\centering
171	\includegraphics[width=\textwidth]{figures/paper/fig3_strategy_heatmap.pdf}
172	\caption{Persuasion strategy transition count matrices for three attack families, based on ground-truth intended strategy labels. Strategy labels validated on $n$=50 samples with a single annotator ($\kappa$=0.78); fine-grained trajectory patterns should be interpreted with this limitation. Crescendo exhibits broad coverage across all strategy categories, while FITD and DD concentrate transitions in smaller subsets. Row $i$, column $j$ counts transitions from strategy $i$ at turn $t$ to strategy $j$ at turn $t+1$.}
173	\label{fig:strategy_heatmap}
174	\end{figure*}
175	
176	Figure~\ref{fig:strategy_heatmap} shows transition count matrices for three attack families.
177	Crescendo conversations exhibit broad transition coverage across all nine strategy categories (1,818 total transitions), with the highest concentration in Role Assignment self-transitions (545); this reflects its gradual escalation design.
178	FITD conversations show a markedly sparser pattern (541 transitions), with Role$\to$Obfuscation (161) as the dominant transition, consistent with FITD's commitment-consistency exploitation~\citep{cialdini2001influence}.
179	DD conversations span 5 active source strategies (565 transitions), with Emotion$\to$Obfuscation (129) as the dominant transition, aligning with DD's design of embedding harmful content within emotionally engaging contexts~\citep{deceptivedelight2024}.
180	
181	\section{Centered CKA Heatmaps}
182	\label{sec:cka_heatmap}
183	
184	\begin{figure}[t]
185	\centering
186	\includegraphics[width=\columnwidth]{figures/paper/cka_heatmap.pdf}
187	\caption{Centered CKA similarity~\citep{kornblith2019cka} between encoder variants on IID and OOD data for DeBERTa-v3 and RoBERTa. Low off-diagonal values (vanilla vs.\ adapted variants) confirm that continued pretraining substantially reshapes representations; the MLM vs.\ 9-class block shows distinct geometries (CKA $\leq$ 0.2 on RoBERTa OOD).}
188	\label{fig:cka_heatmap}
189	\end{figure}
190	
191	\section{Embedding Space Visualization}
192	\label{app:tsne}
193	
194	Figure~\ref{fig:tsne} visualizes mean-pooled \texttt{[CLS]} embeddings via t-SNE for three representative variants (Vanilla, JB-MLM, 9-Class) on DD OOD and ActorAttack. Vanilla embeddings show dispersed jailbreak clusters with ambiguous decision boundaries, while domain-adapted variants (JB-MLM, 9-Class) produce tighter, more separable clusters. JB-MLM achieves the clearest bimodal separation on both evaluation sets, consistent with its superior detection performance.
195	
196	\begin{figure}[ht]
197	\centering
198	\includegraphics[width=\columnwidth]{figures/paper/embedding_tsne.pdf}
199	\caption{t-SNE visualization of mean-pooled \texttt{[CLS]} embeddings (perplexity=30) for Vanilla, JB-MLM, and 9-Class variants on DD OOD and ActorAttack (118 samples each; blue=benign, red=jailbreak).}
200	\label{fig:tsne}
201	\end{figure}
202	
203	\section{Cross-LLM Validation}
204	\label{app:cross_llm}
205	
206	\begin{table}[ht]
207	\centering
208	\footnotesize
209	\caption{Cross-LLM validation (F1, full conversation). All models are trained on Qwen3-8B data; conditions vary the source of jailbreak (JB) and benign (ben.) conversations at inference. Values are evaluated under a matched 50-sample subset protocol and differ from Table~\ref{tab:evidence_hierarchy}, which uses the full evaluation set.}
210	\label{tab:cross_llm}
211	\resizebox{\columnwidth}{!}{%
212	\begin{tabular}{@{}lcccccc@{}}
213	\toprule
214	& \multicolumn{3}{c}{\textit{DD Full}} & \multicolumn{3}{c}{\textit{AA Full}} \\
215	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
216	\textbf{Condition} & Van. & MLM & 9-cl. & Van. & MLM & 9-cl. \\
217	\midrule
218	Qwen JB + Qwen ben. & .312 & .914 & .997 & .258 & .893 & .972 \\
219	Llama JB + Llama ben. & .261 & .282 & .433 & .261 & .368 & .321 \\
220	Llama JB + Qwen ben. & .302 & .778$^{*}$ & 1.000 & .302 & .903 & .801 \\
221	\bottomrule
222	\end{tabular}}
223	\vspace{-2pt}
224	{\footnotesize $^{*}$High seed variance (std = 0.306): seed 456 outlier (F1 = 0.345); remaining two seeds achieve F1 $\geq$ 0.97.}
225	\end{table}
226	
227	Table~\ref{tab:cross_llm} shows three inference conditions. When both jailbreak and benign text come from Llama (row~2), all variants collapse (F1 = 0.26--0.43), but this conflates two sources of distribution shift: unfamiliar jailbreak patterns and unfamiliar benign text. Row~3 isolates jailbreak transferability by pairing Llama jailbreaks with the original Qwen benign distribution. Under this condition, 9-class recovers to F1 = 1.000 on DD and 0.801 on ActorAttack, and JB-MLM reaches 0.903 on ActorAttack. The contrast between rows~2 and~3 shows that the dominant failure mode in row~2 is benign distribution mismatch (false positives from unfamiliar benign text), not inability to recognize cross-LLM jailbreak patterns. Vanilla remains at 0.26--0.31 across all conditions, further confirming that encoders without DAPT lack OOD detection capability regardless of the LLM source. The residual degradation on ActorAttack (0.801 vs.\ 0.972) reflects genuine cross-LLM variation in structurally complex attack patterns.
228	
229	\begin{table}[ht]
230	\centering
231	\footnotesize
232	\caption{Error decomposition for DD Full cross-LLM conditions (matched 50-sample subsets). TP rate is identical across benign conditions; the F1 collapse in the Llama-only condition (Table~\ref{tab:cross_llm}, row~2) is driven entirely by false positives on unfamiliar benign text.}
233	\label{tab:cross_llm_error}
234	\begin{tabular}{@{}lccc@{}}
235	\toprule
236	\textbf{Metric} & Van. & MLM & 9-cl. \\
237	\midrule
238	TP rate (Llama JB) & 0.0\% & 68.0\% & 100.0\% \\
239	FP rate (Llama ben.) & 29.3\% & 88.0\% & 90.0\% \\
240	FP rate (Qwen ben.) & 0.0\% & 0.9\% & 0.0\% \\
241	\bottomrule
242	\end{tabular}
243	\end{table}
244	
245	Table~\ref{tab:cross_llm_error} decomposes DD Full F1 into true positive and false positive rates. TP rates are identical regardless of the benign source: domain-adapted models detect Llama-generated jailbreaks at the same rate whether evaluated against Qwen or Llama benign text. The F1 collapse in the full Llama condition (Table~\ref{tab:cross_llm}, row~2) is driven entirely by false positives on unfamiliar benign text (FP rate: 88--90\% on Llama vs.\ 0--0.9\% on Qwen for adapted variants). The model implicitly treats non-Qwen text style as a jailbreak indicator, a spurious correlation from single-LLM training data. This failure reflects a data diversity limitation, not a methodological one; mixed-LLM training (Table~\ref{tab:mixed_llm}) partially addresses this confound.
246	
247	\section{Mixed-LLM Training Results}
248	\label{app:mixed_llm}
249	
250	\begin{table}[ht]
251	\centering
252	\footnotesize
253	\caption{Mixed-LLM training (250 Qwen + 250 Llama conversations, 3-seed mean$\pm$std where available). ToxicChat evaluated on balanced set (408 conversations).}
254	\label{tab:mixed_llm}
255	\resizebox{\columnwidth}{!}{%
256	\begin{tabular}{@{}lccccc@{}}
257	\toprule
258	\textbf{Variant} & Mixed & DD OOD & AA OOD & FITD OOD & ToxicChat \\
259	\midrule
260	9-class & \textbf{.996$\pm$.006} & \textbf{.818$\pm$.096} & \textbf{.504$\pm$.107} & \textbf{.997$\pm$.005} & \textbf{.550$\pm$.052} \\
261	MLM & .681$\pm$.226 & .289$\pm$.101 & .258$\pm$.075 & .679$\pm$.188 & .256$\pm$.053 \\
262	Vanilla & .802$\pm$.010 & .291$\pm$.065 & .389$\pm$.073 & .867$\pm$.022 & .356$\pm$.009 \\
263	\bottomrule
264	\end{tabular}}
265	\end{table}
266	
267	Table~\ref{tab:mixed_llm} reports detection performance when training on a mixed corpus of Qwen3-8B and Llama-3.1-8B conversations. Classification-based DAPT (9-class) maintains the strongest DD OOD performance (0.818$\pm$0.096), outperforming both vanilla (0.291$\pm$0.065) and MLM (0.289$\pm$0.101) by 53\,pp. ActorAttack remains challenging under mixed-LLM conditions (9-class F1\,=\,0.504$\pm$0.107), suggesting structurally complex attacks require larger or more diverse training data. ToxicChat performance shows no significant improvement over single-source training (0.550$\pm$0.052 vs.\ 0.596$\pm$0.087; Section~\ref{sec:human_data}), consistent with ToxicChat being zero-shot single-turn transfer rather than a standard OOD benchmark.
268	
269	\section{Dataset Scale Validation}
270	\label{app:scale_validation}
271	
272	\begin{table}[ht]
273	\centering
274	\footnotesize
275	\caption{Dataset scale validation (1{,}000 Qwen conversations, 3-seed mean$\pm$std). IID results omitted due to train/test overlap (71\% of original test set present in expanded training data).}
276	\label{tab:scale_validation}
277	\begin{tabular}{@{}lcc@{}}
278	\toprule
279	\textbf{Variant} & DD OOD & AA OOD \\
280	\midrule
281	9-class & \textbf{.889$\pm$.041} & \textbf{.913$\pm$.041} \\
282	MLM & .338$\pm$.010 & .351$\pm$.018 \\
283	Vanilla & .326$\pm$.000 & .508$\pm$.085 \\
284	\bottomrule
285	\end{tabular}
286	\end{table}
287	
288	Table~\ref{tab:scale_validation} validates robustness to dataset scale by doubling the training corpus from 500 to 1{,}000 conversations with new topic seeds. The hierarchy 9-class $\gg$ MLM $\approx$ vanilla holds at 2$\times$ scale: classification-based DAPT maintains 40--56\,pp advantage over vanilla, while MLM provides no improvement over vanilla on either attack family (DD: 0.338 vs.\ 0.326; AA: 0.351 vs.\ 0.508).
289	
290	The performance decline at 1{,}000 conversations may reflect distributional heterogeneity introduced by diverse topic seeds: the additional conversations broaden the training distribution, potentially diluting the concentrated attack-relevant features that smaller, more homogeneous datasets preserve. IID evaluation was precluded by train/test overlap in the expanded dataset (71\%), limiting analysis to OOD metrics. Human-data validation also degrades under scaled training (ToxicChat F1: 0.596 $\to$ 0.341), suggesting the expanded distribution shifts representations away from features useful for both synthetic OOD and human data.
291	
292	\section{RoBERTa-large DAPT Learning Rate Control}
293	
294	\begin{table}[ht]
295	\centering
296	\footnotesize
297	\caption{RoBERTa-large (355M) DAPT learning rate control on OOD Full (3-seed mean$\pm$std). Reducing the learning rate worsens both DD and AA, ruling out over-adaptation as the cause of the regression in Table~\ref{tab:cross_encoder}.}
298	\label{tab:roberta_large_lr}
299	\begin{tabular}{@{}lcc@{}}
300	\toprule
301	\textbf{Config} & DD Full & AA Full \\
302	\midrule
303	Vanilla (no DAPT) & .927$\pm$.036 & 1.000$\pm$.000 \\
304	9-class, LR=$2 \times 10^{-5}$ & .987$\pm$.004 & .946$\pm$.057 \\
305	9-class, LR=$1 \times 10^{-5}$ & .948$\pm$.034 & .781$\pm$.054 \\
306	\bottomrule
307	\end{tabular}
308	\end{table}
309	
310	Reducing the DAPT learning rate from $2 \times 10^{-5}$ to $1 \times 10^{-5}$ worsens both DD and AA performance, which rules out over-adaptation as the cause of the regression observed in Table~\ref{tab:cross_encoder}. An MLM-only variant (without classification) produces the same pattern (AA Full = 0.874$\pm$0.014); representation drift from continued pretraining, not classification-specific bias, is the underlying cause. Domain-adaptive fine-tuning narrows the representation space of a sufficiently large encoder and reduces its inherent OOD generalization ability.
311	
312	\section{TOST Equivalence Sensitivity Analysis}
313	
314	\begin{table}[ht]
315	\centering
316	\footnotesize
317	\caption{TOST equivalence test (scrambled vs.\ 9-class, $\delta$=5\,pp, 10 seeds). $p < 0.05$ confirms equivalence within $\pm\delta$.}
318	\label{tab:tost_sensitivity}
319	\begin{tabular}{@{}lccc@{}}
320	\toprule
321	\textbf{Dataset} & $p$ & $d$ & Equivalent? \\
322	\midrule
323	DD OOD & $2.06 \times 10^{-9}$ & $-$0.136 & \checkmark \\
324	FITD OOD & $\approx 0$ & 0.000 & \checkmark \\
325	ActorAttack & .183 & 0.440 & -- \\
326	\bottomrule
327	\end{tabular}
328	\end{table}
329	
330	In our 80-sample test set, $\delta = 5$\,pp corresponds to $\approx$4 additional missed attacks. We choose $\delta$\,=\,5\,pp as a conservative threshold; equivalence holds even at $\delta$\,=\,3\,pp on DD ($p < 0.001$, $n$\,=\,10) and FITD ($p \approx 0$). With 10 seeds at $\delta$\,=\,5\,pp, DD and FITD confirm formal equivalence ($p < 10^{-8}$, $|d| \leq 0.14$), demonstrating that label correctness is not a detection factor for template attacks. On ActorAttack, the mean gap is 3.0\,pp with moderate effect size ($d$\,=\,0.44); TOST does not confirm equivalence ($p$\,=\,0.183), indicating that strategy-diverse attacks retain some sensitivity to label quality.
331	
332	\section{Partition Robustness and Topic Failure Analysis}
333	\label{app:random_partition}
334	\label{app:topic_failure}
335	
336	\subsection{Random Binary Partition Robustness}
337	
338	\begin{table}[ht]
339	\centering
340	\footnotesize
341	\caption{OOD F1 for 10 random binary partitions of the 9 strategy labels (each partition randomly assigns strategies to group A or B). All partitions use identical Stage-1 DAPT and Stage-2 GRU training; only the binary label mapping differs. Seed 42 (3 runs).}
342	\label{tab:random_partition}
343	\resizebox{\columnwidth}{!}{%
344	\begin{tabular}{@{}lcccc@{}}
345	\toprule
346	\textbf{Partition} & \textbf{Group A} & \textbf{IID} & \textbf{DD OOD} & \textbf{AA OOD} \\
347	\midrule
348	0 & \{0,2,4,5,7\} & 1.000 & 1.000 & 1.000 \\
349	1 & \{1,3,5,6,8\} & 1.000 & 1.000 & 1.000 \\
350	2 & \{0,1,3,7,8\} & 1.000 & 1.000 & 1.000 \\
351	3 & \{2,4,5,6,7\} & 1.000 & 1.000 & 1.000 \\
352	4 & \{0,1,2,6,8\} & 1.000 & 1.000 & 1.000 \\
353	5 & \{0,3,4,7,8\} & 1.000 & 1.000 & 1.000 \\
354	6 & \{1,2,3,5,6\} & 1.000 & 1.000 & 1.000 \\
355	7 & \{1,4,6,7\}   & 1.000 & 1.000 & 0.636 \\
356	8 & \{0,2,3,4,8\} & 1.000 & 1.000 & 1.000 \\
357	9 & \{0,1,5,7,8\} & 1.000 & 1.000 & 1.000 \\
358	\midrule
359	Mean$\pm$Std &  & 1.000$\pm$.000 & 1.000$\pm$.000 & 0.964$\pm$.109 \\
360	\bottomrule
361	\end{tabular}}
362	\end{table}
363	
364	All 10 partitions achieve perfect IID and DD OOD detection regardless of how the 9 strategy labels are split into two groups. On ActorAttack, 9/10 partitions achieve F1\,=\,1.000; the sole outlier (partition~7, AA F1\,=\,0.636) uses a 4/5 split that isolates a specific strategy cluster. The near-universal success confirms that domain-relevant binary classification---not specific label semantics---drives cross-attack generalization on template attacks. The AA outlier is consistent with the complexity-dependent boundary observed in Section~\ref{sec:decomposition}: structurally complex attacks are sensitive to specific partition choices while template attacks are not.
365	
366	\subsection{Topic Classification Failure Analysis}
367	
368	\begin{table}[ht]
369	\centering
370	\footnotesize
371	\caption{Per-turn Fisher ratio (mean across all dimensions) and silhouette score between jailbreak and benign turn embeddings (\texttt{[CLS]} representations). Higher values indicate greater per-turn separability.}
372	\label{tab:topic_failure}
373	\begin{tabular}{@{}llcc@{}}
374	\toprule
375	\textbf{Model} & \textbf{Dataset} & \textbf{Fisher (mean)} & \textbf{Silhouette} \\
376	\midrule
377	Vanilla  & IID test & 0.118 & 0.034 \\
378	Vanilla  & DD OOD  & 0.401 & 0.411 \\
379	Vanilla  & AA OOD  & 0.408 & 0.330 \\
380	\midrule
381	9-class DAPT & IID test & 0.073 & 0.048 \\
382	9-class DAPT & DD OOD  & 0.200 & 0.079 \\
383	9-class DAPT & AA OOD  & 0.832 & 0.301 \\
384	\midrule
385	Topic DAPT & IID test & 0.108 & 0.076 \\
386	Topic DAPT & DD OOD  & 0.653 & 0.274 \\
387	Topic DAPT & AA OOD  & 0.311 & 0.141 \\
388	\bottomrule
389	\end{tabular}
390	\end{table}
391	
392	Topic DAPT achieves \emph{higher} per-turn Fisher separability than 9-class DAPT on IID and DD (0.653 vs.\ 0.200 on DD) yet produces far worse conversation-level detection (F1\,=\,0.541 vs.\ 0.994). This rules out per-turn separability destruction as the failure mechanism. The 9-class model instead greatly expands the embedding space (centroid $L_2$ distance 7.5--27.6 vs.\ 0.9--1.1 for vanilla) while distributing both classes broadly, creating richer representation geometry that the downstream GRU exploits over the turn sequence. Topic classification teaches features that separate turns individually but are temporally inconsistent across a conversation---high per-turn separability does not guarantee that the GRU can learn a stable conversation-level decision boundary.
393	
394	\section{Reproducibility Details}
395	\label{sec:reproducibility}
396	
397	\paragraph{Stage-1 training.}
398	All variants use DeBERTa-v3-base (184M parameters) with learning rate $2 \times 10^{-5}$, AdamW optimizer ($\beta_1$=0.9, $\beta_2$=0.999, weight decay 0.01), linear warmup over the first 10\% of steps, batch size 16, and 4 epochs. MLM variants use 15\% random token masking. Training takes approximately 30 minutes per variant on a single NVIDIA A100 (40GB).
399	
400	\paragraph{Stage-2 training.}
401	The BiGRU has hidden dimension 256, 2 layers, and dropout 0.3 (bidirectional, so output dimension 512). The MLP classifier has layers $512 \to 256 \to 2$ with ReLU activation. Training uses learning rate $1 \times 10^{-3}$, Adam optimizer, batch size 32, and 20 epochs with early stopping (patience 5) on validation F1. Stage-2 training completes in under 5 minutes per variant.
402	
403	\paragraph{Data generation.}
404	Jailbreak conversations are generated using Qwen3-8B with attack-specific prompt templates. Crescendo conversations follow a 5--8 turn gradual escalation structure. FITD conversations use a 2--3 turn commitment-consistency structure. Deceptive Delight conversations embed harmful content within emotionally engaging 3--5 turn sequences. Benign conversations are generated with topic-anchored prompts across five domains (technology, health, finance, education, general) with matched turn counts.
405	
406	\paragraph{Strategy annotation.}
407	Each user turn is annotated by Qwen3-8B using a structured prompt that provides definitions and two examples for each of the nine strategy categories. The prompt instructs the model to output a single category label. We plan to release all generation and annotation prompts, the full dataset, and training code upon acceptance.
408	
409	\paragraph{Adversarial paraphrasing.}
410	The paraphrased test set is generated by instructing Qwen3-8B to rephrase each user turn while preserving the communicative intent. The resulting paraphrases have mean BERTScore 0.92 and mean lexical overlap 0.20 with the originals. These metrics confirm substantial surface-level variation.
411	
412	\paragraph{Cross-checkpoint variance.}
413	To disentangle Stage-1 from Stage-2 variance, we evaluate three independently trained 9-class DAPT checkpoints (seeds 42, 123, 456) with a fixed downstream BiGRU seed (42). Results: IID F1\,=\,1.000$\pm$0.000, DD OOD\,=\,0.926$\pm$0.026, AA OOD\,=\,0.935$\pm$0.013. Stage-1 training is stable (OOD std\,$\leq$\,2.6\,pp), confirming that the variance reported in the main paper is not dominated by Stage-1 initialization.
414	
415	\section{End-to-End Fine-Tuning Upper Bound}
416	\label{app:e2e}
417	
418	\begin{table}[ht]
419	\centering
420	\footnotesize
421	\caption{Frozen probing vs.\ end-to-end (E2E) fine-tuning for DeBERTa-v3-base 9-class (3-seed mean$\pm$std). E2E unfreezes the Stage-1 encoder during Stage-2 training. Frozen values use main-experiment checkpoints (matching Tables~\ref{tab:main_results}--\ref{tab:evidence_hierarchy}); Table~\ref{tab:frozen_verify} uses plan\_002 checkpoints, yielding higher frozen accuracy (DD\,=\,.997, AA\,=\,.972) and a narrower E2E gap ($\leq$2.5\,pp).}
422	\label{tab:e2e}
423	\begin{tabular}{@{}lccc@{}}
424	\toprule
425	\textbf{Config} & IID & DD OOD & AA OOD \\
426	\midrule
427	Frozen probing & 1.000$\pm$.000 & .994$\pm$.005 & .939$\pm$.047 \\
428	E2E fine-tuning & 1.000$\pm$.000 & 1.000$\pm$.000 & \textbf{.997$\pm$.005} \\
429	\midrule
430	$\Delta$ & .000 & +.006 & +.058 \\
431	\bottomrule
432	\end{tabular}
433	\end{table}
434	
435	End-to-end fine-tuning unfreezes the Stage-1 encoder during Stage-2 BiGRU training, allowing gradient flow through the full pipeline. On IID and OOD DD, the two configurations are indistinguishable; on structurally complex ActorAttack, E2E recovers +5.8\,pp. The modest gain confirms that frozen probing captures the vast majority of discriminative information encoded by Stage-1 DAPT, and that the remaining OOD gap in the frozen setting reflects downstream optimization constraints rather than missing representational capacity.
436	
437	\section{Real-World False Positive Rate}
438	\label{app:wildchat_fpr}
439	
440	\begin{table}[ht]
441	\centering
442	\footnotesize
443	\caption{False positive rate (\%) on 226 WildChat benign multi-turn conversations (GPT-3.5 users, avg 7.4 turns per conversation). All models trained on synthetic Qwen3-8B data (1{,}000-conversation scale). 3-seed mean$\pm$std.}
444	\label{tab:wildchat_fpr}
445	\begin{tabular}{@{}lcccc@{}}
446	\toprule
447	\textbf{Variant} & Seed 42 & Seed 123 & Seed 456 & Mean$\pm$Std \\
448	\midrule
449	9-class & 66.8 & 61.1 & 76.5 & 68.1$\pm$6.4 \\
450	MLM & 36.7 & 64.6 & 32.3 & 44.5$\pm$14.3 \\
451	Vanilla & 47.3 & 42.5 & 54.4 & 48.1$\pm$4.9 \\
452	\bottomrule
453	\end{tabular}
454	\end{table}
455	
456	Table~\ref{tab:wildchat_fpr} evaluates false positive rates on 226 WildChat benign multi-turn conversations from real GPT-3.5 users (avg 7.4 turns). All variants produce FPR far exceeding deployable thresholds: 9-class is worst at 68.1\%, followed by vanilla (48.1\%) and MLM (44.5\%). Domain adaptation \emph{increases} FPR relative to vanilla (+20\,pp for 9-class), indicating that continued pretraining amplifies dependence on the training benign distribution. This is consistent with the cross-LLM false positive spike (Table~\ref{tab:cross_llm_error}): models trained on synthetic Qwen3-8B benign text implicitly treat unfamiliar conversational styles as jailbreak indicators. High MLM seed variance (std\,=\,14.3\%) suggests that unsupervised pretraining is particularly unstable under benign distribution shift. Deployment requires per-domain benign calibration or mixed-source benign training data.
457	
458	\paragraph{Post-hoc calibration.}
459	ROC AUC\,=\,0.700$\pm$0.054 indicates insufficient discrimination between WildChat benign and jailbreak conversations at the representation level. At TPR$\geq$95\%, the optimal threshold still yields FPR\,=\,62.7\%, far above deployable levels. Temperature scaling cannot improve this trade-off, as ROC curves are invariant to monotonic score transforms. The AUC ceiling reflects genuine domain shift: WildChat benign and jailbreak representations overlap substantially, and no post-hoc calibration can overcome this; in-domain benign adaptation is required.
460	
461	\paragraph{Second benign source: OASST2.}
462	\label{app:oasst2}
463	
464	To test whether benign-side shift generalizes beyond WildChat, we evaluate on 200 benign multi-turn conversations from OpenAssistant OASST2~\citep{kopf2023openassistant}---a crowdsourced dataset of real human conversations, distinct from WildChat (GPT-3.5 user logs) in both authorship and topic distribution.
465	
466	\begin{table}[ht]
467	\centering
468	\footnotesize
469	\caption{OASST2 benign adaptation curve: FPR on 200 OASST2 benign conversations and OOD jailbreak detection F1 as a function of $N$ OASST2 conversations added to training. Seed 42. Compare WildChat (Table~\ref{tab:wildchat_fpr}): FPR reaches 0\% at $N$\,=\,10.}
470	\label{tab:oasst2_curve}
471	\begin{tabular}{@{}rccccc@{}}
472	\toprule
473	$N$ & FPR (\%) & IID F1 & DD F1 & AA F1 & FITD F1 \\
474	\midrule
475	0 & 57.5 & -- & -- & -- & -- \\
476	10 & 20.5 & 1.000 & 1.000 & 1.000 & 1.000 \\
477	25 & \textbf{1.5} & 1.000 & 1.000 & 0.953 & 1.000 \\
478	50 & \textbf{0.5} & 1.000 & 1.000 & 0.990 & 1.000 \\
479	\bottomrule
480	\end{tabular}
481	\end{table}
482	
483	Baseline FPR on OASST2 (57.5\%) is comparable to WildChat (68.1\%), confirming that benign-side shift is not source-specific but a general consequence of synthetic-only benign training. The adaptation curve follows the same pattern---monotonic FPR reduction with preserved OOD detection---but requires more samples: 25 conversations reduce FPR to 1.5\% (vs.\ 0\% at $N$\,=\,10 for WildChat), and 50 conversations reach 0.5\%. The slower convergence likely reflects greater distributional distance between crowdsourced OASST2 conversations and the synthetic training distribution compared to WildChat's GPT-3.5 user logs.
484	
485	\subsection{Estimated Dual-OOD Detection Performance}
486	\label{app:dual_ood}
487	
488	The OOD detection F1 reported in the main paper evaluates attack-side OOD with IID benign examples (FPR\,=\,0), providing an upper bound. To estimate performance when \emph{both} attack and benign inputs are OOD, we combine per-seed attack recall (from OOD evaluation) with per-seed benign FPR (from WildChat/OASST2 experiments), assuming independence between attack detection and benign false positives. For each seed, we compute binary detection F1 from the resulting TP, FP, FN counts on the OOD test composition (80 jailbreak + 38 benign).
489	
490	\begin{table}[ht]
491	\centering
492	\footnotesize
493	\caption{Estimated dual-OOD binary detection F1 under different benign conditions (3-seed mean$\pm$std). Attack recall held fixed from OOD evaluation; only benign FPR varies. IID row corresponds to the benign-IID upper bound (FPR\,=\,0).}
494	\label{tab:dual_ood}
495	\begin{tabular}{@{}lcc@{}}
496	\toprule
497	\textbf{Benign condition} & DD OOD F1 & AA OOD F1 \\
498	\midrule
499	IID (FPR\,=\,0) & .994$\pm$.009 & .981$\pm$.019 \\
500	WildChat, no adapt & .855$\pm$.020 & .842$\pm$.012 \\
501	OASST2, no adapt & .874$\pm$.009 & .861$\pm$.018 \\
502	WildChat + 10-shot & .994$\pm$.009 & .981$\pm$.019 \\
503	OASST2 + 25-shot & .991$\pm$.009 & .978$\pm$.018 \\
504	\bottomrule
505	\end{tabular}
506	\end{table}
507	
508	Without benign adaptation, dual-OOD F1 drops by 13--14\,pp (DD: $.994 \to .855$; AA: $.981 \to .842$), driven entirely by false positives on OOD benign inputs. After few-shot adaptation---10 WildChat or 25 OASST2 conversations---dual-OOD F1 recovers to within 0.3\,pp of the IID upper bound, confirming that the lightweight adaptation procedure (Section~\ref{sec:benign_shift}) effectively closes the benign distribution gap without compromising attack-side performance.
509	
510	\section{BERT-base Proxy Baseline}
511	\label{app:bert_proxy}
512	
513	\begin{table}[ht]
514	\centering
515	\footnotesize
516	\caption{BERT-base-uncased (110M) frozen probing without DAPT, matching DeepContext's encoder family~\citep{deepcontext2026}. 3-seed mean$\pm$std. DeBERTa-v3 results from Table~\ref{tab:cross_encoder} for comparison.}
517	\label{tab:bert_proxy}
518	\resizebox{\columnwidth}{!}{%
519	\begin{tabular}{@{}lccc@{}}
520	\toprule
521	\textbf{Encoder} & IID & DD OOD & AA OOD \\
522	\midrule
523	BERT-base (110M), no DAPT & .996$\pm$.006 & .318$\pm$.031 & .275$\pm$.027 \\
524	DeBERTa-v3 (184M), no DAPT & 1.000$\pm$.000 & .312$\pm$.043 & .258$\pm$.000 \\
525	DeBERTa-v3 (184M), 9-class & 1.000$\pm$.000 & .994$\pm$.005 & .939$\pm$.047 \\
526	\bottomrule
527	\end{tabular}}
528	\end{table}
529	
530	Table~\ref{tab:bert_proxy} compares BERT-base-uncased (110M parameters, matching DeepContext's encoder) against DeBERTa-v3-base (184M), both without domain-adaptive pretraining. The two vanilla encoders achieve comparable OOD performance (DD: 0.318 vs.\ 0.312; AA: 0.275 vs.\ 0.258), despite a 1.7$\times$ parameter difference and different pretraining procedures. Both collapse on OOD evaluation while 9-class DAPT recovers to 0.994 (DD) and 0.939 (AA). This confirms that cross-attack generalization is driven by domain adaptation, not encoder architecture or capacity at this scale.
531	
532	\section{Confidence Calibration}
533	\label{app:calibration}
534	
535	\begin{table}[ht]
536	\centering
537	\footnotesize
538	\caption{Expected calibration error (ECE, 10 bins) for 9-class and vanilla on IID and OOD evaluation (3-seed mean$\pm$std). Lower is better.}
539	\label{tab:calibration}
540	\begin{tabular}{@{}lccc@{}}
541	\toprule
542	\textbf{Variant} & IID & DD OOD & AA OOD \\
543	\midrule
544	9-class & $\approx$0.000 & 0.143$\pm$0.053 & 0.116$\pm$0.053 \\
545	Vanilla & 0.009$\pm$0.007 & 0.669$\pm$0.004 & 0.504$\pm$0.066 \\
546	\bottomrule
547	\end{tabular}
548	\end{table}
549	
550	The 9-class model achieves substantially lower ECE than vanilla on OOD data (0.12--0.14 vs.\ 0.50--0.67), indicating that domain adaptation improves not only discriminative performance but also confidence calibration. IID calibration is near-perfect for both variants. The residual OOD ECE (0.12--0.14) suggests that temperature scaling could further improve deployment reliability.
551	
552	\subsection{ToxicChat False Positive Confidence}
553	\label{app:confidence}
554	
555	On ToxicChat, 9-class false positives are overwhelmingly high-confidence: 70.2\% of majority-vote FPs exceed $p > 0.9$ (median 0.999), compared to 58.8\% for JB-MLM (median 0.933). Per-seed analysis is more extreme---94--98\% of single-model 9-class FPs are high-confidence (median 1.0), with the borderline fraction (25\%) in majority vote arising from cross-seed disagreement rather than individual model uncertainty. This confirms that the 9-class ToxicChat FPR reflects systematic feature misalignment---classification DAPT shifts benign text into the jailbreak region with high confidence---rather than boundary ambiguity.
556	
557	\section{Frozen Probing Verification}
558	\label{app:frozen_verify}
559	
560	\begin{table}[ht]
561	\centering
562	\footnotesize
563	\caption{Frozen probing vs.\ end-to-end (E2E) fine-tuning (3-seed mean$\pm$std). 9-class: plan\_002 checkpoints; MLM: plan\_017\_mlm\_control (matched training). Frozen probing trains only BiGRU+MLP on frozen DAPT embeddings.}
564	\label{tab:frozen_verify}
565	\resizebox{\columnwidth}{!}{%
566	\begin{tabular}{@{}lcccc@{}}
567	\toprule
568	\textbf{Config} & IID & DD OOD & AA OOD & FITD OOD \\
569	\midrule
570	Frozen 9-class & 1.000$\pm$.000 & .997$\pm$.005 & .972$\pm$.026 & 1.000$\pm$.000 \\
571	Frozen MLM & .982$\pm$.016 & .993$\pm$.009 & .941$\pm$.037 & .987$\pm$.009 \\
572	E2E 9-class & 1.000$\pm$.000 & 1.000$\pm$.000 & .997$\pm$.005 & --- \\
573	\bottomrule
574	\end{tabular}}
575	\end{table}
576	
577	Table~\ref{tab:frozen_verify} compares frozen probing across DAPT objectives and against end-to-end fine-tuning. On easy OOD (DD, FITD), frozen MLM and frozen 9-class representations perform comparably ($\Delta \leq 1.3$\,pp). On hard OOD (ActorAttack), 9-class retains a modest advantage (0.972 vs.\ 0.941, $\Delta$\,=\,3.1\,pp) with lower variance ($\sigma$\,=\,0.026 vs.\ 0.037). Both far exceed vanilla encoders ($\leq$0.318; Table~\ref{tab:bert_proxy}). The E2E advantage over frozen 9-class is $\leq$2.5\,pp, confirming that Stage-1 representation quality is the primary source of OOD generalization.
578	
579	A striking asymmetry emerges when comparing frozen probing to the full pipeline (Table~\ref{tab:evidence_hierarchy}): MLM frozen representations \emph{outperform} the full MLM pipeline on AA OOD (0.941 vs.\ 0.893), while 9-class frozen exactly matches its full pipeline (0.972 vs.\ 0.972). This indicates that MLM's cross-seed instability originates in Stage-2 BiGRU training rather than Stage-1 DAPT: the MLM encoder produces adequate representations that are then degraded by unstable downstream optimization. Classification DAPT, by contrast, produces representations that remain robust through Stage-2 training, explaining its consistently lower variance (Table~\ref{tab:evidence_hierarchy}).
580	
581	This two-level structure (DAPT vs.\ no-DAPT producing a representation quality leap of +70\,pp; classification vs.\ MLM DAPT producing a stability difference) is consistent with two further observations: $\lambda$=0 matches $\lambda > 0$ during E2E fine-tuning (Table~\ref{tab:lambda}), and mean pooling matches BiGRU under E2E (Table~\ref{tab:temporal}). Once DAPT representations are strong, downstream configuration details have minimal impact.
582	
583	\subsection{Single-Turn Truncation Analysis}
584	\label{app:truncated}
585	
586	To isolate whether the ToxicChat evidence-hierarchy reversal (Section~\ref{sec:discussion}) reflects multi-turn structural dependence, we truncate each synthetic test conversation to its last user turn and re-evaluate both 9-class and JB-MLM models (3-seed mean).
587	
588	\begin{table}[h]
589	\centering
590	\caption{Full-conversation vs.\ last-turn-only F1 (3-seed mean). Truncation widens the 9-class advantage, ruling out multi-turn structure as the driver of the ToxicChat reversal.}
591	\label{tab:truncated}
592	\begin{tabular}{@{}llcc@{}}
593	\toprule
594	\textbf{Dataset} & \textbf{Mode} & \textbf{9-class} & \textbf{JB-MLM} \\
595	\midrule
596	IID & Full & 1.000 & .983 \\
597	IID & Last turn & .991 & .894 \\
598	\midrule
599	DD OOD & Full & .997 & .993 \\
600	DD OOD & Last turn & .942 & .924 \\
601	\midrule
602	AA OOD & Full & .972 & .941 \\
603	AA OOD & Last turn & .978 & .927 \\
604	\midrule
605	FITD OOD & Full & 1.000 & .987 \\
606	FITD OOD & Last turn & 1.000 & .927 \\
607	\bottomrule
608	\end{tabular}
609	\vspace{-2pt}
610	{\footnotesize Mean $\Delta$ (9-class $-$ MLM): Full +1.6\,pp, Last turn +6.0\,pp. 9-class advantage widens under truncation across all families, indicating the reversal on ToxicChat is driven by distributional differences between synthetic and human text, not by multi-turn structural dependence.}
611	\end{table}
612	
613	\paragraph{Representation geometry analysis.}
614	\label{app:representation}
615	
616	To characterize the mechanism behind classification DAPT's robustness, we analyze Stage-1 representations across all seven DeBERTa-v3-base variants (seed 42). We extract \texttt{[CLS]} embeddings from 150 test conversations (50 IID + 50 DD OOD + 50 AA OOD) and compute three metrics.
617	
618	\begin{table}[ht]
619	\centering
620	\footnotesize
621	\caption{Representation geometry and class separability across Stage-1 variants. PR: participation ratio (effective dimensionality of the embedding space). Fisher ratio: inter-class distance$^2$ / sum of intra-class variances. Weight $\Delta$: L2 distance from pretrained weights (relative to pretrained norm).}
622	\label{tab:representation}
623	\begin{tabular}{@{}lccc@{}}
624	\toprule
625	\textbf{Variant} & \textbf{PR} & \textbf{Fisher} & \textbf{Wt.\ $\Delta$ (\%)} \\
626	\midrule
627	Vanilla & 31.9 & $<$0.001 & 0.000 \\
628	Wiki-MLM & 25.0 & $<$0.001 & 0.221 \\
629	JB-MLM & 24.6 & $<$0.001 & 0.256 \\
630	Topic & 14.5 & 0.012 & 0.371 \\
631	Scrambled & 7.8 & 2.60 & 0.283 \\
632	9-class & 9.4 & 4.47 & 0.303 \\
633	Binary & 3.7 & 19.7 & 0.239 \\
634	\bottomrule
635	\end{tabular}
636	\end{table}
637	
638	Classification variants compress representations into 2--9 effective dimensions (vs.\ 25--32 for MLM/vanilla) while increasing Fisher ratio by 3--5 orders of magnitude. Weight distances from pretrained are comparable across all variants ($\sim$0.2--0.4\%), indicating that the mechanism is representational restructuring rather than parameter-space regularization. Scrambled labels produce similar compression (PR\,=\,7.8, Fisher\,=\,2.6), confirming that the classification objective structure---not label semantics---drives discriminative compression.
639	
640	\paragraph{Layer-wise localization.}
641	\label{app:layerwise}
642	
643	To determine \emph{where} discriminative compression occurs, we compute PR and Fisher ratio at every DeBERTa-v3-base layer (0--12) for four variants (9-class, scrambled, JB-MLM, vanilla) using the same 236-sample evaluation set (seed 42).
644	
645	\begin{figure}[ht]
646	\centering
647	\includegraphics[width=\columnwidth]{figures/paper/fig_layerwise_representation.pdf}
648	\caption{Layer-wise representation analysis. (a)~Participation ratio: classification variants (9-class, scrambled) show sharp dimensional collapse at layers 9--10 (PR\,$\approx$\,1.5--2.9) while vanilla/JB-MLM maintain high dimensionality (PR\,$\approx$\,7--10). (b)~Fisher ratio (log scale): class separability diverges from layer 8, with 9-class peaking at 10.9 (layer 10) vs.\ vanilla 0.73 (15$\times$).}
649	\label{fig:layerwise}
650	\end{figure}
651	
652	Layers 0--7 show no systematic divergence across variants (Fisher\,$<$\,2.1 for all; PR tracks similar oscillation patterns), consistent with \citet{maennel2020random}'s finding that early layers learn label-independent features. From layer 8 onward, classification-supervised variants diverge sharply: 9-class Fisher rises from 3.2 (layer 8) to 10.9 (layer 10, peak), while vanilla remains below 1.5 throughout. Simultaneously, 9-class PR drops from 3.4 to 1.5 at layer 10---a 6.6$\times$ compression relative to vanilla (PR\,=\,9.7). JB-MLM tracks vanilla across all layers (Fisher\,$\leq$\,3.3, PR\,$\geq$\,1.4), confirming that MLM does not induce discriminative restructuring. Scrambled labels exhibit the same late-layer pattern (Fisher peaks at 7.9, layer 12; PR drops to 1.5, layer 12), reinforcing that any classification signal---regardless of label semantics---triggers late-layer compression.
653	
654	\paragraph{Discriminative subspace probe.}
655	\label{app:discriminative_probe}
656	
657	To test whether the compressed subspace is \emph{sufficient} for OOD detection, we project layer-10 \texttt{[CLS]} representations onto the top-$k$ SVD components and train a logistic regression probe (3 seeds, sklearn default). Controls: random $k$-dimensional projections (10 random bases, mean reported) and vanilla/MLM models under identical projection.
658	
659	\begin{table}[ht]
660	\centering
661	\footnotesize
662	\caption{Discriminative subspace probe: OOD F1 when projecting layer-10 representations onto top-$k$ SVD components vs.\ random $k$-dimensional projections. 9-class top-3 achieves perfect AA detection with 3/768 dimensions; MLM fails even with all 768.}
663	\label{tab:discriminative_probe}
664	\begin{tabular}{@{}llccc@{}}
665	\toprule
666	\textbf{Model} & \textbf{Projection} & DD & AA & FITD \\
667	\midrule
668	9-class & top-3 & 1.000 & \textbf{1.000} & 1.000 \\
669	9-class & top-5 & 1.000 & 1.000 & 1.000 \\
670	9-class & random-3 & 1.000 & 0.928$\pm$.129 & 1.000 \\
671	9-class & random-5 & 1.000 & 0.952 & 1.000 \\
672	9-class & full-768 & 1.000 & 1.000 & 1.000 \\
673	\midrule
674	scrambled & top-3 & 1.000 & 0.962 & 1.000 \\
675	scrambled & random-3 & 0.981 & 0.766 & 0.987 \\
676	\midrule
677	JB-MLM & top-3 & 1.000 & 0.618 & 1.000 \\
678	JB-MLM & full-768 & 1.000 & 0.636 & 1.000 \\
679	JB-MLM & random-5 & 0.685 & 0.584 & 0.744 \\
680	\bottomrule
681	\end{tabular}
682	\end{table}
683	
684	Three findings establish a link between compression and generalization (Table~\ref{tab:discriminative_probe}). First, 9-class top-3 achieves perfect ActorAttack detection (F1\,=\,1.000) using only 3 of 768 dimensions---all discriminative information resides in the compressed subspace. Second, random 3-dimensional projections degrade to 0.928 on AA, confirming that the specific SVD directions matter. Third, JB-MLM reaches only 0.636 on AA even with all 768 dimensions, demonstrating that without classification-induced compression, the representation lacks the structure needed for cross-attack generalization. DD and FITD are near-ceiling for all models, making ActorAttack the critical test.
685	SVD directions computed on IID training data only (without OOD test exposure) yield equal or higher F1 than all-data SVD (AA: 0.947 vs.\ 0.904), confirming the subspace is not an artifact of test-set leakage.
686	
687	\paragraph{SVD necessity ablation.}
688	\label{app:svd_necessity}
689	
690	The probe above establishes \emph{sufficiency}: 3 SVD dimensions carry enough information. To test \emph{necessity}, we project \emph{out} the top-3 SVD directions from full 768-dimensional 9-class \texttt{[CLS]} embeddings and re-run BiGRU classification on OOD data (3 seeds). A random-3 removal control verifies that the effect is specific to the discriminative subspace. The top-3 directions explain 89.8\% of training-set variance.
691	
692	\begin{table}[ht]
693	\centering
694	\footnotesize
695	\caption{SVD necessity ablation: OOD F1 after projecting out top-3 vs.\ random-3 SVD directions from 9-class layer-10 embeddings (3-seed mean$\pm$std).}
696	\label{tab:svd_necessity}
697	\resizebox{\columnwidth}{!}{%
698	\begin{tabular}{@{}lccc@{}}
699	\toprule
700	\textbf{Condition} & DD OOD & FITD OOD & AA OOD \\
701	\midrule
702	Original 768-dim & 1.000$\pm$.000 & 1.000$\pm$.000 & .994$\pm$.005 \\
703	Remove top-3 SVD & .831$\pm$.064 & 1.000$\pm$.000 & .938$\pm$.011 \\
704	Remove random-3 & 1.000$\pm$.000 & 1.000$\pm$.000 & .994$\pm$.005 \\
705	\bottomrule
706	\end{tabular}}
707	\end{table}
708	
709	Removing top-3 SVD directions degrades DD detection by 17\,pp (F1: $1.0 \to 0.831$) and AA by 5.6\,pp ($0.994 \to 0.938$), while random-3 removal has zero effect. FITD is unaffected by either ablation, indicating its discriminative information is more distributed. Combined with the sufficiency result (Table~\ref{tab:discriminative_probe}), the top-3 SVD directions are both sufficient and necessary for DD detection, sufficient but partially redundant for AA, and sufficient but not necessary for FITD.
710	
711	\section{Temporal Aggregation Comparison}
712	\label{app:temporal}
713	
714	\begin{table}[ht]
715	\centering
716	\footnotesize
717	\caption{Temporal aggregation comparison: mean pooling vs.\ BiGRU under frozen and end-to-end (E2E) settings (3-seed mean$\pm$std). Plan\_002 9-class checkpoints.}
718	\label{tab:temporal}
719	\begin{tabular}{@{}llccc@{}}
720	\toprule
721	\textbf{Setting} & \textbf{Aggregator} & DD OOD & AA OOD \\
722	\midrule
723	\multirow{2}{*}{Frozen} & BiGRU & .997$\pm$.005 & .972$\pm$.026 \\
724	& Mean pooling & .991$\pm$.013 & .962$\pm$.015 \\
725	\midrule
726	\multirow{2}{*}{E2E} & BiGRU & 1.000$\pm$.000 & .997$\pm$.005 \\
727	& Mean pooling & 1.000$\pm$.000 & 1.000$\pm$.000 \\
728	\bottomrule
729	\end{tabular}
730	\end{table}
731	
732	Table~\ref{tab:temporal} compares BiGRU and mean pooling under both frozen and E2E settings. Under frozen probing (the main paper's pipeline), BiGRU provides a marginal advantage on ActorAttack (+1.0\,pp) with overlapping confidence intervals, consistent with the main text finding that temporal order is not a core detection factor ($|\Delta| < 1$\,pp under turn shuffling; Section~\ref{sec:decomposition}). Under E2E fine-tuning, the difference vanishes entirely: mean pooling saturates all benchmarks at F1\,=\,1.000. The choice of frozen BiGRU in the main pipeline reflects a design trade-off: it enables representation-level analysis (CKA, t-SNE) that E2E would confound, while sacrificing $\leq$1\,pp on the hardest OOD set.
733	
734	\section{Length Stratification Analysis}
735	\label{app:length}
736	
737	\begin{table}[ht]
738	\centering
739	\footnotesize
740	\caption{Jailbreak recall by conversation length bin on OOD evaluation (3-seed majority vote). Benign conversations span 12--20 turns; jailbreak conversations span 3--10 turns.}
741	\label{tab:length}
742	\begin{tabular}{@{}llccc@{}}
743	\toprule
744	\textbf{Dataset} & \textbf{Variant} & 1--3 turns & 4--6 turns & 7--10 turns \\
745	\midrule
746	\multirow{2}{*}{DD OOD} & 9-class & --- & 100.0\% & 99.4\% \\
747	& Vanilla & --- & $\leq$2.6\% & $\leq$1.7\% \\
748	\midrule
749	\multirow{2}{*}{AA OOD} & 9-class & 93.3\% & 95.6\% & 100.0\% \\
750	& Vanilla & 0.0\% & $\leq$2.6\% & 0.0\% \\
751	\bottomrule
752	\end{tabular}
753	\end{table}
754	
755	Table~\ref{tab:length} stratifies jailbreak recall by conversation length. The 9-class model shows no systematic degradation: ActorAttack recall increases monotonically from 93.3\% (1--3 turns) to 100\% (7--10 turns), and DD recall is near-perfect across all bins.
756	
757	\paragraph{Length confound.}
758	Benign conversations (12--20 turns) and jailbreak conversations (3--10 turns) have zero length overlap in the OOD evaluation sets, raising the concern that the model discriminates by conversation length rather than content. Three observations argue against this interpretation:
759	(1)~Vanilla DeBERTa has access to identical length information via the BiGRU but achieves recall $\leq$2.6\% across all bins; length alone is insufficient without domain-adapted representations.
760	(2)~At prefix $K$=1, where all conversations are length-equalized, 9-class still achieves F1\,=\,0.773$\pm$0.041 on ActorAttack (Table~\ref{tab:actorattack_full}), demonstrating content-based detection independent of length.
761	(3)~The model is trained on IID data (Crescendo) and cannot learn OOD-specific length distributions; generalization to unseen length patterns must rely on content features that transfer across attack families.
762	
763	\paragraph{Direct empirical verification.}
764	\label{app:length_independence}
765	
766	\begin{table}[ht]
767	\centering
768	\footnotesize
769	\caption{Turn-count independence verification (9-class DeBERTa-v3-base, same checkpoint as Table~\ref{tab:main_results}, 3 seeds). Evaluated on the full OOD test set (80 jailbreak + 75 benign conversations) rather than the balanced subset used in Table~\ref{tab:main_results}. Part~A: FPR on test benign truncated to $K$ user turns (all seeds FPR\,=\,0). Part~B: WildChat FPR by turn-count bucket (mean$\pm$std). Part~C: jailbreak detection (F1) after padding with benign turns to 15+ total turns (mean$\pm$std where available).}
770	\label{tab:length_independence}
771	\resizebox{\columnwidth}{!}{%
772	\begin{tabular}{@{}llcc@{}}
773	\toprule
774	& \textbf{Condition} & \textbf{FPR / F1} & $n$ \\
775	\midrule
776	\multicolumn{4}{l}{\textit{Part A: Benign truncation (test set)}} \\[2pt]
777	& Original (12--20 turns) & FPR = .000 & 38 \\
778	& Truncated $K$=3 & FPR = .000 & 38 \\
779	& Truncated $K$=5 & FPR = .000 & 38 \\
780	& Truncated $K$=8 & FPR = .000 & 38 \\
781	& Truncated $K$=10$^{*}$ & FPR = .000 & 38 \\
782	\midrule
783	\multicolumn{4}{l}{\textit{Part B: WildChat FPR by turn count}} \\[2pt]
784	& Short (3--10 turns) & FPR = .770$\pm$.105 & 196 \\
785	& Medium (11--15 turns) & FPR = .942$\pm$.054 & 23 \\
786	& Long (16+ turns) & FPR = .857$\pm$.117 & 7 \\
787	\midrule
788	\multicolumn{4}{l}{\textit{Part C: Jailbreak padding to 15+ turns}} \\[2pt]
789	& DD original & F1 = .996 & 80 \\
790	& DD padded & F1 = .971 ($\Delta$=$-$2.5\,pp) & 80 \\
791	& AA original & F1 = .963 & 80 \\
792	& AA padded & F1 = .383$\pm$.261 ($\Delta$=$-$57.9\,pp) & 80 \\
793	\bottomrule
794	\end{tabular}}
795	\vspace{-2pt}
796	{\footnotesize $^{*}$$K$=10 did not truncate any conversation (test benign max $\sim$8 user turns).}
797	\end{table}
798	
799	Truncating benign conversations to match jailbreak turn counts (Part~A) produces zero false positives across all truncation levels and all 3 seeds, directly confirming that the model does not use conversation length as a detection shortcut. $K$=3 and $K$=5 are the effective control conditions where all 38 conversations were truncated; $K$=10 exceeds the maximum test benign length and serves as a no-op control.
800	
801	WildChat FPR by turn count (Part~B) provides complementary evidence: short conversations (3--10 turns, $n$=196) have \emph{lower} FPR than medium-length ones (11--15 turns, $n$=23), inconsistent with a ``short\,=\,jailbreak'' shortcut. Medium and long buckets have limited sample sizes and should be interpreted as directional evidence only.
802	
803	Padding jailbreak conversations with benign turns (Part~C) reveals an asymmetry: DD detection is resilient ($\Delta$=$-$2.5\,pp), but ActorAttack collapses ($\Delta$=$-$57.9\,pp). Padding experiments append benign turns \emph{after} the complete attack sequence; in practice, adversaries would not dilute their own successful attacks. The collapse nonetheless exposes BiGRU temporal aggregation as vulnerable to attention dilution on subtle attack signals, a limitation discussed in Section~\ref{sec:limitations}.
804	
805	\section{Inference Efficiency}
806	\label{app:efficiency}
807	
808	\begin{table}[ht]
809	\centering
810	\footnotesize
811	\caption{Inference efficiency comparison. DeBERTa+BiGRU and TF-IDF+LR measured on IID test (76 conversations, avg 8.3 turns, single A100). LLM latency from separate OOD evaluation (118 conversations); cross-condition comparison is indicative only.}
812	\label{tab:efficiency}
813	\resizebox{\columnwidth}{!}{%
814	\begin{tabular}{@{}lrcr@{}}
815	\toprule
816	\textbf{Method} & Latency (ms) & Params & VRAM \\
817	\midrule
818	TF-IDF+LR & 0.43$\pm$0.05 & $\sim$10K & CPU \\
819	DeBERTa+BiGRU (ours) & 12.1$\pm$1.2 & 186.7M & 862\,MB \\
820	Qwen3-8B 3-shot$^{\dagger}$ & $\sim$5{,}200 & 8B & $\sim$16\,GB \\
821	\bottomrule
822	\end{tabular}}
823	\vspace{-2pt}
824	{\footnotesize $^{\dagger}$Qwen3-8B latency from OOD evaluation (DD/AA, 118 conversations); not directly comparable to encoder latency measured on IID test.}
825	\end{table}
826	
827	Table~\ref{tab:efficiency} compares inference cost. On matched data (IID test), DeBERTa+BiGRU processes a conversation in 12.1\,ms, 28$\times$ slower than TF-IDF (0.43\,ms), but this speed gap purchases +71\,pp on ActorAttack (F1\,=\,0.972 vs.\ 0.261; Table~\ref{tab:evidence_hierarchy}). LLM-as-judge approaches are orders of magnitude slower ($\sim$5.2\,s per conversation for Qwen3-8B 3-shot) while achieving substantially lower OOD detection (DD\,=\,0.566, AA\,=\,0.652; Table~\ref{tab:llm_judge}). Zero-shot Qwen3-8B achieves F1\,=\,0.0 on DD OOD because it predicts all conversations as benign (Table~\ref{tab:llm_judge}). The full DeBERTa+BiGRU pipeline requires 862\,MB GPU memory, enabling deployment on consumer hardware. The 24.3$\times$ speedup reported in the main text derives from a matched-condition comparison (DisPeD 13.12\,ms vs.\ Qwen3-8B 318.53\,ms on the same GPU and data); the larger gap in Table~\ref{tab:efficiency} reflects different hardware conditions and evaluation sets.
828	
829	\section{Data Efficiency}
830	\label{app:data_efficiency}
831	
832	\begin{table}[ht]
833	\centering
834	\footnotesize
835	\caption{Data efficiency of 9-class DAPT (3-seed mean$\pm$std, sample std with $n{-}1$ divisor) and vanilla baseline (seed 42 only). $N$ = total training conversations (balanced jailbreak/benign).}
836	\label{tab:data_efficiency}
837	\begin{tabular}{@{}rlccc@{}}
838	\toprule
839	$N$ & \textbf{Variant} & IID & DD OOD & AA OOD \\
840	\midrule
841	50 & 9-class & 1.000$\pm$.000 & 1.000$\pm$.000 & .969$\pm$.037 \\
842	125 & 9-class & 1.000$\pm$.000 & 1.000$\pm$.000 & .975$\pm$.019 \\
843	250 & 9-class & 1.000$\pm$.000 & 1.000$\pm$.000 & .975$\pm$.035 \\
844	350 & 9-class & 1.000$\pm$.000 & .978$\pm$.030 & .972$\pm$.033 \\
845	\midrule
846	50 & Vanilla & .646 & .529 & .234 \\
847	125 & Vanilla & .532 & .244 & .244 \\
848	250 & Vanilla & .987 & .365 & .502 \\
849	350 & Vanilla & 1.000 & .360 & .489 \\
850	\bottomrule
851	\end{tabular}
852	\end{table}
853	
854	Table~\ref{tab:data_efficiency} shows that 9-class DAPT reaches near-saturation performance with as few as 50 conversations (25 jailbreak + 25 benign): AA OOD F1\,=\,0.969$\pm$0.037, already surpassing vanilla at full training size ($N$=350, AA\,=\,0.489) by 48\,pp using only 14\% of the data. DD OOD is perfectly solved at all training sizes. Vanilla performance is noisy across $N$ (single seed); the consistent pattern is that vanilla never exceeds DD\,=\,0.53 or AA\,=\,0.50 regardless of training size, while 9-class maintains AA\,$\geq$\,0.969 at all $N$. Seed 456 is systematically lower across all $N$ values, contributing most of the cross-seed variance; this is consistent with the initialization sensitivity observed in the main results.
855	
856	\section{Auxiliary Loss Weight Ablation}
857	\label{app:lambda}
858	
859	\begin{table}[ht]
860	\centering
861	\footnotesize
862	\caption{Effect of auxiliary persuasion loss weight $\lambda$ during Stage-2 E2E fine-tuning (seed 42). Stage-1 DAPT encoder is identical across all rows; only the Stage-2 loss $L = L_{\text{binary}} + \lambda \cdot L_{\text{strategy}}$ varies.}
863	\label{tab:lambda}
864	\begin{tabular}{@{}rcccc@{}}
865	\toprule
866	$\lambda$ & IID & DD OOD & FITD OOD & AA OOD \\
867	\midrule
868	0 & 1.000 & 1.000 & 1.000 & 1.000 \\
869	0.1 & 1.000 & 1.000 & 1.000 & .990 \\
870	0.5 & 1.000 & 1.000 & 1.000 & .981 \\
871	1.0 & 1.000 & 1.000 & 1.000 & .981 \\
872	2.0 & 1.000 & 1.000 & 1.000 & .944 \\
873	\bottomrule
874	\end{tabular}
875	\end{table}
876	
877	During Stage-2 E2E fine-tuning, the auxiliary persuasion loss weight $\lambda$ has limited impact on detection (Table~\ref{tab:lambda}): the maximum AA OOD gap across all $\lambda$ values is 5.6\,pp (single seed), comparable to the cross-seed variance ($\sim$6\,pp) observed in the main results. All configurations converge to perfect validation F1 within epoch 1, indicating that DAPT representations already encode sufficient discriminative features for downstream classification (Section~\ref{app:frozen_verify}). The value of persuasion strategy classification lies in Stage-1 DAPT, where it shapes encoder representations that transfer across attack families, not in the Stage-2 auxiliary loss.
878	
879	\section{OOD Strategy Prediction Analysis}
880	\label{app:strategy_pred}
881	
882	\begin{table}[ht]
883	\centering
884	\footnotesize
885	\caption{OOD strategy prediction accuracy (jailbreak turns only) and detection rate for the 9-class model (3-seed mean). $r$: Pearson correlation between per-strategy prediction accuracy and per-strategy detection rate.}
886	\label{tab:strategy_pred}
887	\resizebox{\columnwidth}{!}{%
888	\begin{tabular}{@{}lcccc@{}}
889	\toprule
890	\textbf{Dataset} & Strat.\ Acc.\ & Det.\ Rate & Missed (per seed) & $r$ \\
891	\midrule
892	DD OOD & 50.1\% & 99.6\% & 0 / 0 / 1 & $\sim$0.45 \\
893	AA OOD & 50.1\% & 96.2\% & 1 / 7 / 1 & $\sim$0.24 \\
894	\bottomrule
895	\end{tabular}}
896	\end{table}
897	
898	Table~\ref{tab:strategy_pred} reports OOD strategy prediction accuracy alongside detection rates. Strategy prediction accuracy is substantially above random (50.1\% vs.\ 11.1\% chance for 9 classes) and positively correlated with detection success ($r \approx 0.24$--0.45), but strategy prediction is not the detection mechanism: frozen probing with a randomly initialized strategy head (Appendix~\ref{app:frozen_verify}) achieves 97.2\% AA OOD detection, and $\lambda$=0 (no strategy loss) matches or exceeds $\lambda > 0$ during E2E fine-tuning (Table~\ref{tab:lambda}). The classification objective shapes representations during Stage-1 DAPT training; at inference, strategy predictions are a byproduct of those representations, not a driver of detection.
899	
900	\section{Cross-Seed Ensemble}
901	\label{app:ensemble}
902	
903	\begin{table}[ht]
904	\centering
905	\footnotesize
906	\caption{Majority vote ensemble (3 seeds) vs.\ single-seed mean on OOD Full. ``Fixed'' = samples corrected by ensemble; ``Broke'' = samples corrupted by ensemble.}
907	\label{tab:ensemble}
908	\resizebox{\columnwidth}{!}{%
909	\begin{tabular}{@{}lcccc@{}}
910	\toprule
911	\textbf{Variant} & DD single$\to$ens. & AA single$\to$ens. & Fixed & Broke \\
912	\midrule
913	9-class & .997$\to$\textbf{1.000} & .972$\to$\textbf{.981} & 5 & 0 \\
914	MLM & .914$\to$\textbf{1.000} & .897$\to$\textbf{.953} & 26 & 0 \\
915	Vanilla & .258$\to$.258 & .258$\to$.258 & 0 & 0 \\
916	\bottomrule
917	\end{tabular}}
918	\end{table}
919	
920	Table~\ref{tab:ensemble} shows that majority vote never corrupts correct predictions (Broke\,=\,0 for all variants). MLM benefits most from ensembling (+8.6\,pp DD, +6.0\,pp AA), because its per-seed errors are complementary: each seed fails on different samples, and the majority corrects these. This further exposes MLM's seed instability: its individual seeds are unreliable, but their errors are uncorrelated. By contrast, 9-class seeds are already highly consistent (std\,$\leq$\,0.026), leaving minimal room for ensemble improvement (+0.3--0.9\,pp). Vanilla errors are systematic (all seeds fail on the same OOD samples), so ensembling provides no benefit.
921	
922	\subsection{Seed-Level F1 Comparisons}
923	\label{app:seed_level}
924	
925	To verify that cross-seed pooling does not mask inconsistent pairwise orderings, Table~\ref{tab:seed_level} reports per-seed F1 for all variants on OOD DD and ActorAttack at full conversation length. The overall evidence hierarchy is maintained across seeds, with 9-class and binary consistently outperforming MLM; scrambled shows one reversal on AA (seed 42).
926	
927	\begin{table}[h]
928	\centering
929	\small
930	\caption{Per-seed F1 on OOD Full for key variants (seeds 42, 123, 456). The relative ordering is consistent across seeds.}
931	\label{tab:seed_level}
932	\resizebox{\columnwidth}{!}{%
933	\begin{tabular}{@{}lcccccc@{}}
934	\toprule
935	& \multicolumn{3}{c}{DD-Full} & \multicolumn{3}{c}{AA-Full} \\
936	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
937	\textbf{Variant} & s42 & s123 & s456 & s42 & s123 & s456 \\
938	\midrule
939	9-class & 1.000 & 1.000 & .990 & .990 & .935 & .990 \\
940	Binary & 1.000 & 1.000 & 1.000 & .981 & .990 & 1.000 \\
941	Scrambled & .990 & 1.000 & 1.000 & .891 & .990 & .971 \\
942	MLM-only & 1.000 & .990 & .751 & .971 & .925 & .784 \\
943	Vanilla & .285 & .305 & .348 & .258 & .258 & .258 \\
944	\bottomrule
945	\end{tabular}}
946	\end{table}
947	
948	\section*{Use of AI Assistants}
949	\label{app:ai-assistants}
950	
951	We used Claude (Anthropic) as an AI coding and writing assistant
952	throughout this work. Specifically:
953	\begin{itemize}
954	    \item \textbf{Code:} drafting experiment scripts, data-processing
955	    pipelines, and analysis utilities; debugging and refactoring.
956	    \item \textbf{Writing:} drafting and revising paper sections,
957	    polishing prose, and reformatting LaTeX.
958	    \item \textbf{Literature:} summarizing related papers to inform
959	    related-work section.
960	\end{itemize}
961	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "978651f3-c6ad-4df2-8338-d5bae1df2359",
  "isSidechain": true,
  "promptId": "270ab91c-e9b9-4a39-b092-16a4d85348b6",
  "agentId": "aa90fb53a2c1faac3",
  "type": "user",
  "uuid": "84329b29-2e99-42e1-86d0-91a73d1ac803",
  "sourceToolAssistantUUID": "978651f3-c6ad-4df2-8338-d5bae1df2359",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-24T18:25:00.250Z_

Now let me also check the main.tex for any additional acronyms defined there (e.g., in macros or the preamble).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84329b29-2e99-42e1-86d0-91a73d1ac803",
  "isSidechain": true,
  "agentId": "aa90fb53a2c1faac3",
  "requestId": "req_011CbMrz18oKxgAzJDZqxiTz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b8fc25d-d58e-4700-ad5f-65d1d2ce8658",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DvaRHDXcFuCKUC8ZLjBvHd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39905,
      "cache_read_input_tokens": 34499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39905,
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

_source line 21 · 2026-05-24T18:25:01.570Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WyqK11cmJaCPVCsH89Tfic`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b8fc25d-d58e-4700-ad5f-65d1d2ce8658",
  "isSidechain": true,
  "agentId": "aa90fb53a2c1faac3",
  "requestId": "req_011CbMrz18oKxgAzJDZqxiTz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82f44049-7aa1-49a6-9ab3-7cf845795be9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DvaRHDXcFuCKUC8ZLjBvHd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39905,
      "cache_read_input_tokens": 34499,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 39905
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 34499,
          "cache_creation_input_tokens": 39905,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 39905,
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

_source line 22 · 2026-05-24T18:25:01.594Z_

<details><summary>↩ Tool result · `toolu_01WyqK11cmJaCPVCsH89Tfic`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\graphicspath{{../../}}
12	\usepackage{amsmath}
13	\usepackage{booktabs}
14	\usepackage{enumitem}
15	\usepackage{amssymb}
16	\usepackage{multirow}
17	
18	\title{DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	
27	\input{introduction}
28	
29	\input{related_work}
30	
31	\input{method}
32	
33	\input{experiments}
34	
35	\input{conclusion}
36	
37	\bibliography{references}
38	
39	\clearpage
40	\input{appendix}
41	
42	% checklist removed — EMNLP 2026 ARR requires checklist in OpenReview form, not in PDF
43	
44	\end{document}
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82f44049-7aa1-49a6-9ab3-7cf845795be9",
  "isSidechain": true,
  "promptId": "270ab91c-e9b9-4a39-b092-16a4d85348b6",
  "agentId": "aa90fb53a2c1faac3",
  "type": "user",
  "uuid": "f5b2d3e6-203f-4780-a000-3f29dd798b93",
  "sourceToolAssistantUUID": "82f44049-7aa1-49a6-9ab3-7cf845795be9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-24T18:25:57.114Z_

Here is the complete abbreviation/acronym inventory for the paper.

---

## Complete Abbreviation/Acronym Inventory

### Method / System Names

| # | Abbreviation | Full Form Given? | First Appears | In Abstract? |
|---|---|---|---|---|
| 1 | **DisPeD** | Yes: "Disentangled Persuasion Detection" | abstract.tex ~L3 | Yes |
| 2 | **DAPT** | Partially: defined in experiments.tex L6 as "all Stage-1 adaptations" extending Gururangan et al.; also used throughout as "domain-adaptive pretraining" by context | abstract.tex ~L3 (implicit, via "classification-based domain adaptation") — explicitly as "DAPT" first in introduction.tex ~L16 | No (concept is present but the acronym "DAPT" is not in the abstract) |
| 3 | **BiGRU** | No explicit expansion given; used as a known term (bidirectional GRU) | abstract.tex ~L3 | Yes |
| 4 | **GRU** | No explicit expansion (assumed known: Gated Recurrent Unit) | method.tex ~L47 (in "bidirectional GRU") | No |
| 5 | **MLP** | No explicit expansion (assumed known: Multi-Layer Perceptron) | method.tex ~L48 | No |
| 6 | **TF-IDF** | No explicit expansion (assumed known: Term Frequency-Inverse Document Frequency) | experiments.tex ~L22 | No |
| 7 | **LR** | No explicit expansion; used as "LR" in "TF-IDF LR" (Logistic Regression) | experiments.tex ~L22 | No |
| 8 | **PAP** | Yes: cited as a named framework from Zeng et al. (40 persuasion techniques) | introduction.tex ~L5 | No |
| 9 | **E2E** | Yes: "end-to-end" defined at first use in appendix.tex ~L416 | appendix.tex ~L416 | No |

### Model / Architecture Names

| # | Abbreviation | Full Form Given? | First Appears | In Abstract? |
|---|---|---|---|---|
| 10 | **DeBERTa** / **DeBERTa-v3** | Yes: cited with reference \citep{he2021deberta} / \citep{he2023debertav3} | introduction.tex ~L7 (DeBERTa-v3); abstract.tex ~L3 does not name it | No |
| 11 | **RoBERTa** | Yes: cited with reference \citep{liu2019roberta} | introduction.tex ~L16 | No |
| 12 | **BERT** | No explicit expansion (assumed known); used in "BERT-base" | experiments.tex ~L20 ("architecturally equivalent to DeepContext") | No |
| 13 | **LLM** | No explicit expansion (assumed known: Large Language Model) | abstract.tex ~L3 ("mixed-LLM training") | Yes |
| 14 | **GPT-5.5** | No expansion needed (proper name) | introduction.tex ~L7 | No |
| 15 | **Qwen3-8B** | No expansion needed (proper name) | method.tex ~L36 | No |
| 16 | **Llama Guard** / **Llama Guard 3** | No expansion needed (proper name) | abstract.tex ~L3 | Yes (as "Llama Guard 3") |
| 17 | **Llama-3.1-8B** | No expansion needed (proper name) | experiments.tex ~L172 | No |

### Dataset / Evaluation Setting Names

| # | Abbreviation | Full Form Given? | First Appears | In Abstract? |
|---|---|---|---|---|
| 18 | **OOD** | Yes: defined in experiments.tex L6 as "Cross-attack OOD: evaluation on attack families unseen during training" | abstract.tex ~L3 | Yes |
| 19 | **IID** | Not explicitly expanded (in-distribution; used in contrast to OOD) | abstract.tex ~L3 (implicit via "vanilla 0.26--0.31"); explicitly "IID" in experiments.tex ~L12 | No (not as acronym) |
| 20 | **DD** | Yes: "Deceptive Delight (DD)" | experiments.tex ~L14 | No |
| 21 | **AA** | Yes: "ActorAttack (AA)" | experiments.tex ~L78 (in table caption) | No |
| 22 | **FITD** | Yes: cited as "Foot-in-the-Door" with \citep{fitd2024}; abbreviated "FITD" | experiments.tex ~L14 | No |
| 23 | **LMSYS** | No explicit expansion (Large Model Systems Organization; proper name) | experiments.tex ~L16 | No |
| 24 | **OASST2** | Yes: "OpenAssistant OASST2" | appendix.tex ~L462 | No |
| 25 | **WildChat** | No expansion needed (proper name) | experiments.tex ~L229 | No |
| 26 | **ShareGPT** | No expansion needed (proper name) | experiments.tex ~L229 | No |

### Metric / Statistical Test Names

| # | Abbreviation | Full Form Given? | First Appears | In Abstract? |
|---|---|---|---|---|
| 27 | **F1** | No explicit expansion (assumed known: F1 score) | abstract.tex ~L3 | Yes |
| 28 | **FPR** | No explicit expansion (false-positive rate; contextually clear) | abstract.tex ~L3 ("false-positive rates") | Yes (as "false-positive rates", not as "FPR") |
| 29 | **ECE** | Yes: "Expected calibration error (ECE, 10 bins)" | appendix.tex ~L538 | No |
| 30 | **TOST** | No explicit expansion at first use (Two One-Sided Tests); used in introduction.tex ~L22 without expansion | introduction.tex ~L22 | No |
| 31 | **CIs** | Yes: "BCa bootstrap 95% CIs" (confidence intervals) | experiments.tex ~L27 | No |
| 32 | **BCa** | No explicit expansion (bias-corrected and accelerated bootstrap) | experiments.tex ~L27 | No |
| 33 | **ROC AUC** | No explicit expansion (Receiver Operating Characteristic Area Under Curve) | appendix.tex ~L458 | No |
| 34 | **TPR** | No explicit expansion (True Positive Rate; contextually clear) | appendix.tex ~L458 | No |
| 35 | **TP / FP / FN** | No explicit expansion (True Positive / False Positive / False Negative) | appendix.tex ~L488 | No |

### Technique / Analysis Names

| # | Abbreviation | Full Form Given? | First Appears | In Abstract? |
|---|---|---|---|---|
| 36 | **MLM** | No explicit expansion at first use in abstract; later defined contextually as "masked language modeling" in method.tex ~L40 | abstract.tex ~L3 | Yes |
| 37 | **SVD** | No explicit expansion (Singular Value Decomposition; assumed known) | introduction.tex ~L22 | No |
| 38 | **CKA** | Yes: "Centered CKA similarity" with citation in appendix.tex ~L187; partially — "CKA analysis" in related_work.tex ~L15 without expansion, and "CKA" in method.tex ~L50 | method.tex ~L50 | No |
| 39 | **t-SNE** | No explicit expansion (t-distributed Stochastic Neighbor Embedding) | method.tex ~L50 | No |
| 40 | **PR** | Yes: "participation ratio" defined in appendix.tex ~L622 | appendix.tex ~L622 | No |
| 41 | **AdamW** | No expansion needed (proper name of optimizer) | appendix.tex ~L398 | No |

### Other Abbreviations

| # | Abbreviation | Full Form Given? | First Appears | In Abstract? |
|---|---|---|---|---|
| 42 | **NLP** | No explicit expansion (Natural Language Processing) | conclusion.tex ~L25 | No |
| 43 | **VRAM** | No explicit expansion (Video Random Access Memory) | experiments.tex ~L243 (table header) | No |
| 44 | **GPU** | No explicit expansion (Graphics Processing Unit) | experiments.tex ~L238 | No |
| 45 | **CPU** | No explicit expansion (Central Processing Unit) | experiments.tex ~L245 | No |
| 46 | **CLS** | Used as `[CLS]` token notation; no expansion needed (standard BERT terminology) | method.tex ~L14 (fig caption) | No |
| 47 | **LLM-as-judge** | Descriptive phrase, not an acronym per se | introduction.tex ~L7 | No |
| 48 | **pp** | No explicit expansion (percentage points; used throughout) | experiments.tex ~L59 | No |
| 49 | **std** | No explicit expansion (standard deviation) | experiments.tex ~L26 | No |
| 50 | **$\beta$-VAE** | Used in footnote, not core to paper | introduction.tex ~L16 (footnote) | No |
| 51 | **InfoGAN** | Used in footnote, not core to paper | introduction.tex ~L16 (footnote) | No |
| 52 | **RST** | Cited as a framework: \citep{mann1988rst} | related_work.tex ~L12 | No |
| 53 | **PDTB** | Cited: \citep{prasad2008pdtb} | related_work.tex ~L12 | No |
| 54 | **JB-MLM** / **JB** | Contextually defined: "jailbreak-domain MLM" vs "Wikipedia MLM" | experiments.tex ~L121 ("jailbreak-domain MLM") | No |
| 55 | **Wiki-MLM** | Contextually defined: "Wikipedia MLM" | experiments.tex ~L121 | No |

---

### Summary of Issues

**Abbreviations never formally expanded (potential concerns for reviewers)**:
- **BiGRU** (used in abstract, never expanded to "Bidirectional Gated Recurrent Unit")
- **MLM** (used in abstract, expanded only later in method.tex as "masked language modeling")
- **TOST** (first used in introduction.tex without expansion — "Two One-Sided Tests for Equivalence")
- **SVD** (never expanded — "Singular Value Decomposition")
- **CKA** (partially: "Centered CKA" in appendix but never "Centered Kernel Alignment")
- **t-SNE** (never expanded)
- **BCa** (never expanded — "Bias-Corrected and Accelerated")
- **FPR** (spelled out as "false-positive rates" in abstract but abbreviated form "FPR" used from introduction.tex ~L20 onward without separate definition)
- **IID** (never explicitly defined as "in-distribution" or "independent and identically distributed")
- **TF-IDF** (never expanded)
- **LR** (never expanded in "TF-IDF LR" context)
- **MLP** (never expanded)
- **NLP** (never expanded)
- **DAPT** appears in the abstract paragraph contextually ("classification-based domain adaptation") but the acronym "DAPT" itself first appears only in introduction.tex

**Abbreviations used in the abstract**: DisPeD, OOD, F1, LLM, MLM, BiGRU, Llama Guard 3, FPR (as words). Of these, only DisPeD and OOD get definitions (DisPeD in intro, OOD in experiments terminology section). MLM and BiGRU are used in the abstract without expansion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5b2d3e6-203f-4780-a000-3f29dd798b93",
  "isSidechain": true,
  "agentId": "aa90fb53a2c1faac3",
  "requestId": "req_011CbMrzUa3mMZ7B69jJe9Fi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a726a65-e3b6-4116-b4b9-b742ffbfedc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "snug-napping-finch",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBENJ22PR31zE6Zv4Dp93q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 517,
      "cache_read_input_tokens": 74404,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 517,
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
