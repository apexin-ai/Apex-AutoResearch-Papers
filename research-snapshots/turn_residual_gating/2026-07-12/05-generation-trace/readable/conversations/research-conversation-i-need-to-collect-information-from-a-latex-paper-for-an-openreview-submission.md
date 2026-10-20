# Research conversation: I need to collect information from a LaTeX paper for an OpenReview submission form. Please read the following files and 

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-adf0b047ae89c464e.jsonl`
- **Structured JSON:** [`d86c8237c4b35958c54a.json`](../../sessions/d8/d86c8237c4b35958c54a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

49 recorded events

### User

_source line 1 · 2026-05-26T03:40:25.112Z_

I need to collect information from a LaTeX paper for an OpenReview submission form. Please read the following files and report back their contents:

1. The title (from \title{}) and abstract (the text inside \begin{abstract}...\end{abstract}) from the main paper file. Check these locations:
   - /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.tex
   - If the abstract is in a separate file, find and read it

2. The Limitations section content - find where it is and what it says

3. The Appendix structure - list all \section{} titles in the appendix, especially confirm "Use of AI Assistance" exists and its exact content

4. Check what datasets, models, and packages are used (look at the method/experiment sections)

5. Check if hyperparameters, model sizes, GPU details, computational budget are reported

6. Check if there are any statistics reported (error bars, confidence intervals, mean/std)

7. Find the PDF file path - check if /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.pdf exists

Report all findings verbatim (especially title and abstract - exact text, no paraphrasing).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "baf8129c-bc28-412d-9baf-f7e253a00603",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-26T03:40:25.118Z_

```json
{
  "parentUuid": "baf8129c-bc28-412d-9baf-f7e253a00603",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
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
  "uuid": "675375c8-241f-4cf5-86e5-7b753f9ddefb",
  "timestamp": "2026-05-26T03:40:25.118Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-26T03:40:27.740Z_



I'll read all the relevant files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "675375c8-241f-4cf5-86e5-7b753f9ddefb",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQV9oq8ec4shaDkJVxVf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8566f36a-e8a4-436d-8955-ef2c30fddf0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYPdyS6proNRLi3GKxVbsN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34421,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34421,
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

_source line 4 · 2026-05-26T03:40:28.329Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DcsUd8dFx39vUTUDHRyhLw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8566f36a-e8a4-436d-8955-ef2c30fddf0d",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQV9oq8ec4shaDkJVxVf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a22f701-8105-4851-ab59-fc36e46c52ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYPdyS6proNRLi3GKxVbsN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34421,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34421,
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

_source line 5 · 2026-05-26T03:40:28.342Z_

<details><summary>↩ Tool result · `toolu_01DcsUd8dFx39vUTUDHRyhLw`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{placeins}
17	\usepackage{float}
18	\usepackage{alphalph}
19	\usepackage{etoolbox}
20	\AtBeginEnvironment{figure}{\nolinenumbers}
21	\AfterEndEnvironment{figure}{\linenumbers}
22	\AtBeginEnvironment{figure*}{\nolinenumbers}
23	\AfterEndEnvironment{figure*}{\linenumbers}
24	\AtBeginEnvironment{table}{\nolinenumbers}
25	\AfterEndEnvironment{table}{\linenumbers}
26	\AtBeginEnvironment{table*}{\nolinenumbers}
27	\AfterEndEnvironment{table*}{\linenumbers}
28	
29	\graphicspath{{../figures/paper/}{../artifacts/}}
30	
31	\title{Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue}
32	
33	\author{Anonymous}
34	
35	\begin{document}
36	\maketitle
37	
38	\input{sections/abstract}
39	\input{sections/introduction}
40	\input{sections/related_work}
41	\input{sections/method}
42	\input{sections/experiments}
43	\input{sections/analysis}
44	\FloatBarrier
45	\input{sections/discussion}
46	\input{sections/conclusion}
47	\input{sections/limitations}
48	
49	\bibliography{references}
50	
51	\raggedbottom
52	\appendix
53	\renewcommand{\thesection}{\AlphAlph{\value{section}}}
54	\input{sections/appendix}
55	
56	\end{document}
57	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a22f701-8105-4851-ab59-fc36e46c52ee",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "e2bf5604-30d2-496c-8f77-dc7c437a1593",
  "sourceToolAssistantUUID": "1a22f701-8105-4851-ab59-fc36e46c52ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T03:40:29.571Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01M3nRn6iCFAPYKT3Ei21Ujj`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2bf5604-30d2-496c-8f77-dc7c437a1593",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQV9oq8ec4shaDkJVxVf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c658723-cf21-46b5-bd29-1f3fb676ac28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYPdyS6proNRLi3GKxVbsN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34421,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34421,
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

_source line 7 · 2026-05-26T03:40:29.591Z_

<details><summary>↩ Tool result · `toolu_01M3nRn6iCFAPYKT3Ei21Ujj`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c658723-cf21-46b5-bd29-1f3fb676ac28",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "32950af9-29e0-4c9c-a26e-595abc0aab5f",
  "sourceToolAssistantUUID": "7c658723-cf21-46b5-bd29-1f3fb676ac28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T03:40:30.164Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DNUxaofseTUsQpLHkXpMKY`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.pdf 2>/dev/null && echo \"PDF EXISTS\" || echo \"PDF NOT FOUND\"",
  "description": "Check if main.pdf exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32950af9-29e0-4c9c-a26e-595abc0aab5f",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQV9oq8ec4shaDkJVxVf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "126a5a62-f00d-4a13-b74d-56d4f3afd86a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYPdyS6proNRLi3GKxVbsN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34421,
      "cache_read_input_tokens": 0,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 34421
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 303,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 34421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 34421,
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

_source line 9 · 2026-05-26T03:40:30.326Z_

<details><summary>↩ Tool result · `toolu_01DNUxaofseTUsQpLHkXpMKY`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 1037744 May 25 21:10 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.pdf
PDF EXISTS
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "126a5a62-f00d-4a13-b74d-56d4f3afd86a",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "7add036c-d6bd-4ffb-8a1f-c090a7a8859b",
  "sourceToolAssistantUUID": "126a5a62-f00d-4a13-b74d-56d4f3afd86a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-26T03:40:32.679Z_

Now let me read the abstract, limitations, appendix, experiments, method, and analysis sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7add036c-d6bd-4ffb-8a1f-c090a7a8859b",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVAC4btEzpS9HBfoQob",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5ad09c2-d4c5-4089-b7a0-36a5c3f34859",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLWqM7r2jc5YLp95s2pTC5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2707,
      "cache_read_input_tokens": 34421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2707,
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

_source line 11 · 2026-05-26T03:40:33.257Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YJX8oP6we6kwoQoXWpzWpW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5ad09c2-d4c5-4089-b7a0-36a5c3f34859",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVAC4btEzpS9HBfoQob",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1995fdba-0555-41d2-836f-ef24fa7c602e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLWqM7r2jc5YLp95s2pTC5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2707,
      "cache_read_input_tokens": 34421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2707,
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

_source line 12 · 2026-05-26T03:40:33.273Z_

<details><summary>↩ Tool result · `toolu_01YJX8oP6we6kwoQoXWpzWpW`</summary>

```text
1	\begin{abstract}
2	As multi-turn conversations grow longer, large language models progressively lose attention to the system-prompt goals that define their task, even when the underlying goal representations remain intact. Existing remedies operate at inference time, leaving a natural but untested alternative: training auxiliary attention losses alongside next-token prediction to directly optimize goal attention. This strategy assumes that attention patterns learned under teacher forcing will transfer to autoregressive generation, an assumption that classical exposure bias research has challenged for sequence models but that has never been examined for auxiliary attention objectives in multi-turn transformers.
3	We show this assumption fails. On a controlled five-way testbed spanning two architectures (Qwen-2.5-7B, Llama-3.1-8B), goal attention optimized to target under teacher forcing collapses by an order of magnitude under autoregressive generation. A diagnostic exclusion chain traces the failure to exposure bias, ruling out gradient conflict, gating mechanism, and parameter capacity as primary causes. Inference-time attention steering confirms that the collapse reflects attention misallocation rather than representation loss. Scheduled sampling, applied here for the first time to auxiliary attention objectives in multi-turn transformers, compresses the training--inference gap to near parity on Qwen and from ${\sim}$27$\times$ to 2.9$\times$ on Llama, with no perplexity cost\footnote{Code and data are available at \url{https://anonymous.4open.science/r/turn_residual_gating-8703/}.}.
4	\end{abstract}
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1995fdba-0555-41d2-836f-ef24fa7c602e",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "f2de8f6a-9620-405c-91e9-d169eb3dd611",
  "sourceToolAssistantUUID": "1995fdba-0555-41d2-836f-ef24fa7c602e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T03:40:33.645Z_

<details open><summary>🔧 Tool call — Read · `toolu_014T375wQJZa5yYdWs7LBxp9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2de8f6a-9620-405c-91e9-d169eb3dd611",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVAC4btEzpS9HBfoQob",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35e606fb-b255-4d49-928b-6cb0a4e5472e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLWqM7r2jc5YLp95s2pTC5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2707,
      "cache_read_input_tokens": 34421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2707,
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

_source line 14 · 2026-05-26T03:40:33.653Z_

<details><summary>↩ Tool result · `toolu_014T375wQJZa5yYdWs7LBxp9`</summary>

```text
1	\section*{Limitations}\label{sec:limitations}
2	
3	Our findings are demonstrated on two model families (Qwen-2.5-7B and Llama-3.1-8B) and a single dataset (UltraChat, 8K conversations). Although UltraChat spans 18 dialogue categories providing reasonable domain diversity, cross-dataset validation (e.g., ShareGPT, LMSYS-Chat) remains future work; generalization to other architectures and domains (e.g., code, reasoning) is likewise untested. All experiments use LoRA (rank 16); full fine-tuning may exhibit different sensitivity to the TF-AR gap, and the LoRA capacity constraint could confound the capacity exclusion step (LoRA-only vs.\ Base comparison in \S\ref{subsec:five-way}). Most configurations use a single seed (scheduled sampling validated on three seeds; \S\ref{subsec:ss}), and quality assessment relies on PPL rather than comprehensive benchmarks \citep{hendrycks2021measuring,lin2022truthfulqa}. Our diagnostic exclusion identifies exposure bias as a primary factor but does not rule out KV cache drift as a contributing mechanism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35e606fb-b255-4d49-928b-6cb0a4e5472e",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "a47b80a5-ee46-45e2-b6c7-a70af579d63a",
  "sourceToolAssistantUUID": "35e606fb-b255-4d49-928b-6cb0a4e5472e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T03:40:34.616Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AsLVwrnRheyBKfVrSD5VBC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a47b80a5-ee46-45e2-b6c7-a70af579d63a",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVAC4btEzpS9HBfoQob",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb8dd137-7e9a-49fa-9f63-7da1499e1740",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLWqM7r2jc5YLp95s2pTC5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2707,
      "cache_read_input_tokens": 34421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2707,
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

_source line 16 · 2026-05-26T03:40:35.171Z_

<details open><summary>🔧 Tool call — Read · `toolu_015KefTs4rmJrEtTQKP3B7CW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb8dd137-7e9a-49fa-9f63-7da1499e1740",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVAC4btEzpS9HBfoQob",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f794685-121e-4942-8f11-16612cf9b7bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLWqM7r2jc5YLp95s2pTC5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2707,
      "cache_read_input_tokens": 34421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2707,
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

_source line 17 · 2026-05-26T03:40:35.272Z_

<details><summary>↩ Tool result · reported error · `toolu_01AsLVwrnRheyBKfVrSD5VBC`</summary>

```text
File content (26306 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb8dd137-7e9a-49fa-9f63-7da1499e1740",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "db54e97c-6f2d-45e9-9492-71b4da58760d",
  "toolUseResult": "Error: File content (26306 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "cb8dd137-7e9a-49fa-9f63-7da1499e1740",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T03:40:35.180Z_

<details><summary>↩ Tool result · `toolu_015KefTs4rmJrEtTQKP3B7CW`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct with LoRA \citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; training costs in Appendix~\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\ref{sec:appendix-hyper}; dataset statistics in Appendices~\ref{sec:appendix-data} and~\ref{sec:appendix-dataset-ext}; the controlled comparison design is described in \S\ref{sec:comparison-design}. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \citep{dongre2026attention}, and perplexity (PPL).
7	
8	\subsection{Main Results}
9	
10	Table~\ref{tab:five-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\leq$2\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\leq$1\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, indicating that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\S\ref{subsec:ss}).
11	
12	Under AR generation ($N$\,=\,50), GAR-ours drops to 0.019--0.064, an 8--17$\times$ gap (Figure~\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\ LoRA-only is significant ($p$\,=\,0.004; Appendices~\ref{sec:appendix-stats} and~\ref{sec:appendix-stats-ext}), yet the gap remains 7.8$\times$. A second seed confirms TF stability ($0.504\pm0.001$). MMLU 5-shot accuracy remains within 0.8\,pp across all variants (per-category breakdown in Appendix~\ref{sec:appendix-mmlu-ext}). We analyze this distribution shift in \S\ref{sec:analysis}.
13	
14	\begin{figure*}[!t]
15	  \centering
16	  \includegraphics[width=\textwidth]{fig5_attention_steering.pdf}
17	  \caption{Inference-time $\beta$-steering recovers GAR from 0.064 to 0.727, consistent with attention misallocation as a proximal cause (9\% PPL cost at $\beta$\,=\,3; phase transition at $\beta \in [2, 3]$).}
18	  \label{fig:steering-recovery}
19	\end{figure*}
20	
21	\subsection{Inference-Time Attention Steering}\label{subsec:steering}
22	
23	All training-time interventions leave the exposure bias gap intact. If the collapse is caused by attention misallocation rather than representation degradation, then directly correcting attention should recover GAR. We test this by adding a constant bias $\beta$ to pre-softmax attention logits for goal-token positions during generation:
24	\begin{equation}
25	  \tilde{A}_{i,j}^{(\ell,h)} = A_{i,j}^{(\ell,h)} + \beta \cdot \mathbf{1}[j \in \mathcal{G}],
26	\end{equation}
27	where $\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\beta \in [0, 2]$ yields marginal improvement, then $\beta = 3$ triggers a phase transition to GAR\,=\,0.556 (9\% PPL cost). At $\beta$\,=\,5, GAR reaches 0.727$\pm$0.061 (PPL 1.77); the operating region $\beta \in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\ref{fig:steering-recovery}; full results in Appendix~\ref{sec:appendix-steering}; per-$\beta$ turn-level trajectories in Appendix~\ref{sec:appendix-steering-viz}). GAR recovery under steering is partly by construction: boosting attention logits toward goal tokens mechanically increases the attention-based metric. The stronger evidence is the counterfactual: if the collapse were due to hidden-state drift rather than attention misallocation, reweighting could not recover GAR, yet it does, consistent with attention misallocation as a proximal cause (qualitative examples in Appendix~\ref{sec:appendix-examples}). Downstream, steering ($\beta$\,=\,3) raises late-turn instruction compliance by +11.1\,pp, though this effect does not reach conventional significance ($p$\,=\,0.077; content-constrained tasks benefit most, +23.8\,pp; Appendix~\ref{sec:appendix-ir}).
28	
29	\subsection{Scheduled Sampling Compresses the TF--AR Gap}\label{subsec:ss}
30	
31	\begin{figure}[t]
32	  \centering
33	  \includegraphics[width=\columnwidth]{fig_ss_gap_compression.pdf}
34	  \caption{Scheduled sampling compresses the TF-AR gap from 7.8$\times$ to ${\sim}$1.3$\times$, the only variant approaching parity across five training conditions.}
35	  \label{fig:ss-gap}
36	\end{figure}
37	
38	Scheduled sampling (SS; \citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\pm0.047$, compressing the gap from 7.8$\times$ to ${\sim}$1.3$\times$ (TF GAR $0.498\pm0.004$) with no PPL cost ($1.441\pm0.001$; Figure~\ref{fig:ss-gap}; per-seed details in Appendix~\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\beta$\,=\,5: $0.717\pm0.001$, std 0.047$\to$0.001; Figure~\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\ref{sec:appendix-gar-robust}; extended robustness in Appendix~\ref{sec:appendix-gar-ext}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\sim}$27$\times$ to 2.9$\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\ 3; \S\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.
39	
40	
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f794685-121e-4942-8f11-16612cf9b7bb",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "c9d838ff-03ce-4289-b443-62e791be3366",
  "sourceToolAssistantUUID": "3f794685-121e-4942-8f11-16612cf9b7bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T03:40:35.541Z_

<details open><summary>🔧 Tool call — Read · `toolu_0129A9sT1U8x1sPfmWCt9Ypv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9d838ff-03ce-4289-b443-62e791be3366",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVAC4btEzpS9HBfoQob",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ea1db27-b529-4a2d-b7ec-e379e7bf1f28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLWqM7r2jc5YLp95s2pTC5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2707,
      "cache_read_input_tokens": 34421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2707,
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

_source line 20 · 2026-05-26T03:40:35.546Z_

<details><summary>↩ Tool result · `toolu_0129A9sT1U8x1sPfmWCt9Ypv`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Preliminaries}\label{sec:background}
4	
5	\paragraph{Goal Accessibility Ratio.}
6	Standard metrics such as perplexity and attention entropy capture generation quality but not \emph{what} the model attends to. In multi-turn dialogue, a model may generate fluent text while progressively ignoring task specifications in the system prompt. We need a metric that directly measures whether goal-relevant context receives attention. To formalize this, we denote the task specification tokens in the system prompt as \emph{goal tokens} $\mathcal{G}$. \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\tau$ as
7	\begin{equation}\label{eq:gar}
8	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
9	\end{equation}
10	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$.
11	
12	\paragraph{Two GAR variants.}
13	\textbf{GAR-Dongre} is the original definition (Eq.~\ref{eq:gar}), averaging over all response tokens. However, averaging dilutes the signal with intermediate positions that may legitimately attend to local context rather than the system prompt. The last token of each assistant turn is where the model aggregates information for the next continuation; attention at this position most directly reflects the model's awareness of task specifications. \textbf{GAR-ours} restricts the measurement accordingly:
14	\begin{equation}\label{eq:gar-ours}
15	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
16	\end{equation}
17	where $t_\tau$ is the last token index at turn $\tau$. Attention at this position reflects the information drawn upon for continuation; we use GAR-ours as the optimization target for $\mathcal{L}_\text{GAR}$ (\S\ref{sec:loss}). Empirically, GAR-Dongre is diluted by NTP attention patterns to ${\sim}$0.01--0.02 in multi-turn settings, losing discriminative power across configurations; GAR-ours retains an order-of-magnitude range (0.019--0.50). The contrast itself is informative: goal attention concentrates at the last-token position, and only this concentrated pattern is vulnerable to distribution shift (\S\ref{sec:analysis}). Throughout this work, GAR serves primarily as a \emph{diagnostic probe}: it measures whether auxiliary attention training transfers to autoregressive generation, rather than being an end-to-end optimization objective whose increase directly improves downstream task performance (the correlation with instruction retention is weak; $r$\,=\,0.200, $p$\,=\,0.007; \S\ref{sec:discussion}).
18	
19	\subsection{ThreadGate Architecture}
20	
21	\begin{figure}[t]
22	  \centering
23	  \includegraphics[width=\columnwidth]{fig4_attention_heatmap.pdf}
24	  \caption{Per-turn GAR-ours under AR generation ($N$\,=\,5 conversations, 10 turns). All fine-tuned variants cluster together (77--81\% decay; $\Delta$\,=\,3.3\,pp between ThreadGate and LoRA-only); Base decays 87.5\%. Gating adds zero incremental effect.}
25	  \label{fig:attention-heatmap}
26	\end{figure}
27	
28	Different transformer layers serve different roles: early layers capture local syntax while later layers integrate long-range context \citep{gromov2024unreasonable}. A global intervention would uniformly scale all layers, but goal attention decay is layer-dependent: some layers contribute more to cross-turn information routing than others. ThreadGate therefore adds a \emph{per-layer} gating mechanism to the residual stream, allowing the model to learn which layers to modulate. At each layer $l$, the residual update is scaled by a scalar gate:
29	\begin{equation}
30	  x_{l+1} = x_l + g_l \cdot f_l(x_l),
31	\end{equation}
32	where $f_l$ denotes the sublayer computation (self-attention or feed-forward network, FFN). Since residual networks can be viewed as ensembles of shallow paths \citep{veit2016residual}, per-layer gating selectively modulates individual paths within this ensemble. This resembles ReZero \citep{bachlechner2021rezero}, which initializes a single trainable scalar at zero to stabilize deep network training, but ThreadGate differs in three ways: (i)~gates are \emph{content-conditioned}, a function of the hidden state rather than a fixed scalar; (ii)~gates are \emph{turn-conditioned}, incorporating conversation-position features; (iii)~gates are initialized near identity ($\sigma(1.5) \approx 0.82$) rather than zero, preserving the pretrained model's computation.
33	
34	Concretely, each gate $g_l$ is produced by a two-layer MLP that takes both content and turn features as input:
35	\begin{align}\label{eq:gate}
36	  g_l = \sigma\bigl(W_2\,\text{ReLU}(&W_1\,[\text{proj}(x_l);\;\text{emb}(t_d, t_i)] \notag\\
37	  &+ b_1) + b_2\bigr),
38	\end{align}
39	where $\text{proj}(\cdot)$ reduces the hidden dimension to 16, and $\text{emb}(t_d, t_i)$ provides a 16-dimensional turn embedding encoding turn distance $t_d$ (turns since system prompt) and turn index $t_i$ via learned lookup tables. The 32-dimensional input passes through a 64-unit hidden layer to a scalar gate in $(0, 1)$ via sigmoid. For Qwen-2.5-7B ($L\!=\!28$), this adds ${\sim}$57K parameters ($<$0.001\% of 7B). To isolate the contribution of turn conditioning, the \textbf{Uniform Gate} ablation replaces $\text{emb}(\cdot)$ with a learnable constant, removing turn awareness while retaining content-conditioned gating. To preserve pretrained behavior, gate biases are initialized to 1.5 (${\sim}$82\% pass-through) rather than zero as in ReZero, and gate parameters receive a $10\times$ learning rate multiplier to accelerate adaptation.
40	
41	\subsection{Training Objective}\label{sec:loss}
42	
43	Next-token prediction alone provides no gradient signal for attention allocation; a model can achieve low perplexity while distributing attention arbitrarily. The auxiliary GAR loss provides explicit pressure to maintain goal-token attention, while a diversity regularizer prevents gate collapse. The training objective combines three terms:
44	\begin{equation}
45	  \mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\,\mathcal{L}_\text{GAR} + \lambda_\text{div}\,\mathcal{L}_\text{div}.
46	\end{equation}
47	$\mathcal{L}_\text{NTP}$ is the standard next-token prediction loss. For $\mathcal{L}_\text{GAR}$, we use MSE rather than cross-entropy because GAR is a continuous ratio and MSE provides \emph{bidirectional} pressure, penalizing both under- and over-attention and preventing identity collapse (Appendix~\ref{sec:appendix-loss}):
48	\begin{equation}
49	  \mathcal{L}_\text{GAR} = \text{MSE}(\text{GAR\text{-}ours}, \tau),
50	\end{equation}
51	where $\tau = 0.5$ targets allocating half of the last token's attention to goal tokens. Without diversity pressure, all gates converge near 1.0; the gate diversity loss prevents this:
52	\begin{equation}
53	  \mathcal{L}_\text{div} = \text{ReLU}(\sigma_\text{min} - \text{std}(\mathbf{g})),
54	\end{equation}
55	where $\mathbf{g} = [g_1, \ldots, g_L]$ and $\sigma_\text{min} = 0.05$ is a minimum standard deviation threshold ($\lambda_\text{GAR} = \lambda_\text{div} = 1.0$). This formulation emerged from seven iterations spanning four loss families (Appendix~\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity; only MSE provides the bidirectional pressure needed to prevent identity collapse.
56	
57	\subsection{Controlled Comparison Design}\label{sec:comparison-design}
58	
59	We design a five-way comparison where each adjacent pair isolates one factor: \textbf{ThreadGate (TG) vs.\ Uniform Gate (UG)} (turn conditioning), \textbf{TG vs.\ LoRA-only} (gating mechanism), \textbf{ThreadGate vs.\ +PCGrad} (gradient conflict via gradient surgery \citep{yu2020pcgrad}), and \textbf{Fine-tuned vs.\ Base} (LoRA adaptation). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed (Appendix~\ref{sec:appendix-hyper}).
60	
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ea1db27-b529-4a2d-b7ec-e379e7bf1f28",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "4a386207-d242-49f0-908f-9edd4cdf4cb0",
  "sourceToolAssistantUUID": "9ea1db27-b529-4a2d-b7ec-e379e7bf1f28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-26T03:40:35.852Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HHEPQbtMEC9tohBcLPnW3o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a386207-d242-49f0-908f-9edd4cdf4cb0",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVAC4btEzpS9HBfoQob",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57996b97-5368-4ab2-bc67-fce7a3ea2e5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLWqM7r2jc5YLp95s2pTC5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2707,
      "cache_read_input_tokens": 34421,
      "output_tokens": 483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2707
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 483,
          "cache_read_input_tokens": 34421,
          "cache_creation_input_tokens": 2707,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2707,
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

_source line 22 · 2026-05-26T03:40:35.864Z_

<details><summary>↩ Tool result · `toolu_01HHEPQbtMEC9tohBcLPnW3o`</summary>

```text
1	\section{Analysis}\label{sec:analysis}
2	
3	\begin{figure*}[!t]
4	  \centering
5	  \includegraphics[width=\textwidth]{fig3_gate_shift.pdf}
6	  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift ($N$\,=\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\times$) exceed final $N$\,=\,50 estimates (8--17$\times$; Table~\ref{tab:five-way}) due to smaller sample size.}
7	  \label{fig:gate-shift}
8	\end{figure*}
9	
10	Each subsection kills one alternative hypothesis via diagnostic exclusion: \S\ref{subsec:gate-conditioning}~turn conditioning, \S\ref{subsec:pcgrad}~gradient direction conflict, leaving exposure bias as the primary remaining explanation consistent with current evidence (\S\ref{subsec:dist-shift}). \S\ref{subsec:mechanism-specificity} confirms selectivity; \S\ref{subsec:cross-model} confirms cross-architecture generalization.
11	
12	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
13	
14	We compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\% attenuation; Table~\ref{tab:five-way}; full gate profiles in Appendix~\ref{sec:appendix-gate-profile}; training dynamics in Appendix~\ref{sec:appendix-training-ext}). The Uniform Gate learns comparable per-layer variation (L3\,=\,0.777, L27\,=\,1.000) despite lacking turn conditioning; the structure thus arises from LoRA$+$GAR pressure (Figure~\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?
15	
16	\subsection{PCGrad Gradient Direction Conflict Exclusion}\label{subsec:pcgrad}
17	
18	NTP and GAR gradients oppose in 68--79\% of layers (cosine similarity $-$0.089$\to$$-$0.042 across epochs), with NTP magnitude dominance growing from 7.5$\times$ to 14.7$\times$ (full gradient statistics in Appendix~\ref{sec:appendix-gradient}). If this direction conflict prevents GAR convergence, eliminating it via PCGrad \citep{yu2020pcgrad}, which projects conflicting gradients onto the other's normal plane, should prevent the collapse. To our knowledge, this is the first application of PCGrad as a \emph{diagnostic} tool rather than an optimization method.
19	
20	PCGrad shifts cosine similarity to oscillate around zero, yet TF metrics are unchanged. AR GAR \emph{worsens}: 0.064$\to$0.030 ($p$\,=\,0.002; Figure~\ref{fig:training-pcgrad}b in Appendix~\ref{sec:appendix-gradient}). By \emph{modus tollens}: removing gradient direction conflict does not prevent collapse; therefore it is not the primary cause. PCGrad eliminates direction conflict but does not address magnitude imbalance (NTP dominates GAR by 7.5--14.7$\times$); the worsening under PCGrad may partly reflect projection side-effects rather than confirming that direction conflict is entirely absent as a factor. Cross-model analysis confirms this pattern: Llama-3.1-8B gradients are near-orthogonal (cos\,=\,+0.005) with 25.7$\times$ NTP magnitude dominance (Table~\ref{tab:gradient-crossmodel}).
21	
22	\subsection{Distribution Shift Analysis}\label{subsec:dist-shift}
23	
24	The TF-AR GAR gap persists across all variants (Table~\ref{tab:five-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, evidence that the shift selectively destroys concentrated last-token attention. The mechanism is exposure bias \citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. GAR optimizes a distributional property with no autoregressive counterpart, explaining why TF GAR-ours remains near $\tau$\,=\,0.5 while AR GAR collapses (77--87\% per-turn decay; Figure~\ref{fig:attention-heatmap}; per-configuration AR trajectories in Appendix~\ref{sec:appendix-ar-gar-dynamics}; scaling analysis in Appendix~\ref{sec:appendix-eb-scaling}).
25	
26	\subsection{Mechanism Specificity}\label{subsec:mechanism-specificity}
27	
28	We test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed); exposure bias thus disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\times$) and Qwen (1.28$\times$) vs.\ the order-of-magnitude GAR-ours collapse.
29	
30	\begin{figure}[t]
31	  \centering
32	  \includegraphics[width=\columnwidth]{fig_ss_multiseed.pdf}
33	  \caption{Multi-seed AR GAR under scheduled sampling ($\beta$\,=\,0 and $\beta$\,=\,5, three seeds). Steering nearly eliminates seed variance (std: 0.047$\to$0.001).}
34	  \label{fig:ss-multiseed}
35	\end{figure}
36	
37	\subsection{Cross-Model Replication}\label{subsec:cross-model}
38	
39	We replicate on Llama-3.1-8B-Instruct \citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\,=\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\,$>$\,100\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\times$ and 26$\times$ (Figure~\ref{fig:crossmodel}a in Appendix~\ref{sec:appendix-llama}; per-turn values in Appendix~\ref{sec:appendix-perturn-detail}). Gate profiles differ qualitatively (Figure~\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\,=\,0.793) while Llama dips at late layers (L25\,=\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.
40	
41	Scheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\sim}$27$\times$ to 2.9$\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\sim}$1.3$\times$ likely due to fewer training epochs (2 vs.\ 3). The phase transition is architecture-dependent: $\beta$\,=\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\beta$\,=\,5 (GAR 0.791, exceeding Qwen SS 0.717; Appendix~\ref{sec:appendix-llama-ss}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern (79.8\% GAR decay, $\beta$-steering recovery to 0.715; Appendix~\ref{sec:appendix-1.5b}).
42	
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57996b97-5368-4ab2-bc67-fce7a3ea2e5d",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "4aa651c7-5337-4d2e-9600-ee81b65fde52",
  "sourceToolAssistantUUID": "57996b97-5368-4ab2-bc67-fce7a3ea2e5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-26T03:40:39.678Z_

Now let me read the appendix in chunks to get the section titles and check for "Use of AI Assistance".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4aa651c7-5337-4d2e-9600-ee81b65fde52",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVAbzmHeUF69VZhrg9F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f2fbcd2-50a2-47e9-b75b-68bcce7693ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DU3yo3nKhWT9wceUU3eBQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8507,
      "cache_read_input_tokens": 37128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8507,
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

_source line 24 · 2026-05-26T03:40:41.940Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DNHPF3xtimt4DP9Pb3YULf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f2fbcd2-50a2-47e9-b75b-68bcce7693ed",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVAbzmHeUF69VZhrg9F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f26b8a4-f6cb-4f49-a65c-56975d1de6d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DU3yo3nKhWT9wceUU3eBQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8507,
      "cache_read_input_tokens": 37128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8507,
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

_source line 25 · 2026-05-26T03:40:41.947Z_

<details><summary>↩ Tool result · `toolu_01DNHPF3xtimt4DP9Pb3YULf`</summary>

```text
1	\section{Training Configuration}\label{sec:appendix-hyper}
2	
3	Table~\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\times$ learning rate multiplier and are initialized with bias 1.5 ($\sigma(1.5) \approx 0.82$); the gate MLP adds ${\sim}$57K parameters per variant ($<$0.001\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.5 over 3 epochs (29.7--37.1\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB VRAM), requiring 6--8 hours per variant.
4	
5	\begin{table}[t]
6	\centering\small
7	\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\dagger$ apply only to ThreadGate and its ablations.}
8	\label{tab:hyperparams}
9	\begin{tabular}{l@{\hspace{8pt}}l}
10	\toprule
11	\textbf{Parameter} & \textbf{Value} \\
12	\midrule
13	Base model & Qwen-2.5-7B-Instruct \\
14	LoRA rank / $\alpha$ & 16 / 32 \\
15	LoRA targets & \texttt{q\_proj}, \texttt{v\_proj} \\
16	Optimizer & AdamW ($\beta_1$\!=\!0.9, $\beta_2$\!=\!0.999) \\
17	Learning rate & $2 \times 10^{-4}$ \\
18	Gate LR mult.$^\dagger$ & $10\times$ \\
19	Batch / grad accum & 1 / 8 (eff.\ 8) \\
20	Epochs & 3 \\
21	Max seq length & 2048 \\
22	Training data & 8K UltraChat convs \\
23	Seed & 42 (+123 for TG, SS) \\
24	$\lambda_\text{GAR}$/$\lambda_\text{div}$ & 1.0 / 1.0 \\
25	GAR target $\tau$ & 0.5 \\
26	Gate init bias$^\dagger$ & 1.5 ($\sigma\!\approx\!0.82$) \\
27	Gate hidden dim$^\dagger$ & 64 \\
28	Turn embed dim$^\dagger$ & 16 \\
29	GPU & RTX PRO 6000 (96\,GB) \\
30	Training time & 6--8 h / variant \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Loss Formulation Search}\label{sec:appendix-loss}
36	
37	The final MSE + gate diversity loss (\S\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.
38	
39	\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.
40	
41	\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\text{mean}(\text{GAR})$). The unbounded objective rewards full pass-through ($g \to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\lambda$=2 (v3), gates froze within 100 steps; at $\lambda$=10 (v3b), convergence to identity accelerated; at $\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.
42	
43	\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.
44	
45	\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\tau$ incurs the same penalty as GAR below $\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\mathcal{L}_\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).
46	
47	\begin{table*}[t]
48	\centering\footnotesize
49	\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}
50	\label{tab:loss-iterations}
51	\begin{tabular}{l l l p{5.8cm} c c}
52	\toprule
53	 & \textbf{Loss Family} & \textbf{Status} & \textbf{Failure Mechanism} & \textbf{GAR} & \textbf{PPL} \\
54	\midrule
55	v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\
56	v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & Numerical instability from cumulative product; $\varepsilon$-stabilization insufficient & ---  & ---  \\
57	v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\
58	v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & Higher $\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\
59	v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\
60	v6  & Smooth saturation       & \texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\
61	v7  & MSE + gate div          & \checkmark~\textbf{converged}  & \textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\
62	\bottomrule
63	\end{tabular}
64	\end{table*}
65	
66	\paragraph{Overfitting caveat.} All nine iterations (v1--v7) were developed and evaluated on UltraChat, creating a risk of overfitting the loss design to a single data distribution. However, the core finding---the TF-AR gap---appears in every variant including the simplest LoRA-only baseline that uses no auxiliary loss at all, suggesting it is a structural consequence of exposure bias rather than an artifact of a particular loss formulation. The final configuration (v7) uses a standard MSE objective with no dataset-specific tricks, mitigating concerns about over-engineering to a single benchmark.
67	
68	\section{Instruction Retention Details}\label{sec:appendix-ir}
69	
70	To evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\beta$\,=\,3 steering on $N$\,=\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.
71	
72	\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\,=\,54 paired evaluations (18 types $\times$ 3 conversations per type) for the McNemar analysis.
73	
74	\paragraph{Per-category results.} Table~\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.
75	
76	\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\,=\,0.200, $p$\,=\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\,=\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.
77	
78	Figure~\ref{fig:ir-bar} visualizes the per-category breakdown.
79	
80	\begin{figure}[t]
81	  \centering
82	  \includegraphics[width=\columnwidth]{fig_instruction_retention.pdf}
83	  \caption{Instruction retention by constraint category under $\beta$\,=\,3 steering. Content constraints benefit most (+23.8\,pp); format and count constraints are unaffected.}
84	  \label{fig:ir-bar}
85	\end{figure}
86	
87	\FloatBarrier
88	
89	\begin{table}[t]
90	\centering\small
91	\caption{Instruction retention by constraint category ($\beta$\,=\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}
92	\label{tab:ir-results}
93	\begin{tabular}{lccc}
94	\toprule
95	\textbf{Category} & $\beta$\,=\,0 & $\beta$\,=\,3 & $\Delta$ \\
96	\midrule
97	Content    & 61.9\% & 85.7\% & +23.8\,pp \\
98	Position   & 66.7\% & 73.3\% & +6.7\,pp \\
99	Count      & 100\%  & 100\%  & 0 \\
100	Format     & 100\%  & 100\%  & 0 \\
101	\midrule
102	\textbf{Overall} & 75.9\% & 87.0\% & +11.1\,pp \\
103	\bottomrule
104	\end{tabular}
105	\end{table}
106	
107	\section{Long-Conversation AR Evaluation}\label{sec:appendix-n5}
108	
109	The main results (Table~\ref{tab:five-way}) report AR GAR from $N$\,=\,50 held-out conversations with a mean of 3.6 user turns. Table~\ref{tab:n5-ar} presents complementary results on $N$\,=\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.
110	
111	\paragraph{Gating advantage vanishes at length.} In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. ThreadGate's advantage over LoRA-only shrinks from 1.7$\times$ (0.064 vs.\ 0.037 in the $N$\,=\,50 evaluation) to 0.64$\times$ (0.016 vs.\ 0.025), actually reversing the ordering. This reversal is not statistically robust given the small sample ($N$\,=\,5) but directionally suggests that architectural modifications provide diminishing returns as conversation length increases and exposure bias accumulates.
112	
113	\paragraph{Convergence to base.} By turn~10, all fine-tuned variants converge to within 2$\times$ of the base model's GAR, compared to 3.4$\times$ at turn~1 in the shorter evaluation. This convergence is consistent with exposure bias compounding multiplicatively over turns: each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn~10 the accumulated drift overwhelms any gating or LoRA signal, leaving only the base model's intrinsic attention patterns.
114	
115	\paragraph{Caveats.} The $N$\,=\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.
116	
117	\begin{table}[t]
118	\centering\small
119	\caption{AR GAR-ours on $N$\,=\,5 ten-turn conversations. The gating advantage observed in Table~\ref{tab:five-way} ($N$\,=\,50, mean 3.6 turns) diminishes with conversation length.}
120	\label{tab:n5-ar}
121	\begin{tabular}{lcc}
122	\toprule
123	\textbf{Configuration} & \textbf{AR GAR-O} & \textbf{$\Delta$ vs.\ Table~\ref{tab:five-way}} \\
124	\midrule
125	Base & 0.012 & $-$0.007 \\
126	\midrule
127	ThreadGate & 0.016 & $-$0.048 \\
128	\;+\,PCGrad & 0.015 & $-$0.015 \\
129	Uniform Gate & 0.015 & $-$0.018 \\
130	LoRA-only & 0.025 & $-$0.012 \\
131	\bottomrule
132	\end{tabular}
133	\end{table}
134	
135	\section{Statistical Test Details}\label{sec:appendix-stats}
136	
137	All statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\ref{tab:stat-tests} consolidates the full results.
138	
139	\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\ LoRA-only comparison ($p$\,=\,0.004, $r$\,=\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\ +PCGrad comparison ($p$\,=\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.
140	
141	\paragraph{Bootstrap confidence intervals.} The 95\% CIs in Table~\ref{tab:five-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.
142	
143	\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \leq r < 0.5$ is medium, and $r \geq 0.5$ is large. The TG vs.\ LoRA-only effect ($r$\,=\,0.454) is medium, and TG vs.\ Base ($r$\,=\,0.802) is large.
144	
145	\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific diagnostic exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \leq 0.004$) survive this correction.
146	
147	\begin{table}[t]
148	\centering\small
149	\caption{Consolidated statistical tests. All AR comparisons use $N$\,=\,50 conversations (39 with $\geq$3 turns); gate conditioning uses 28 layers.}
150	\label{tab:stat-tests}
151	\begin{tabular}{llcc}
152	\toprule
153	\textbf{Comparison} & \textbf{Test} & $p$ & $r$ \\
154	\midrule
155	\multicolumn{4}{l}{\emph{AR GAR-ours ($\beta$\,=\,0)}} \\
156	TG vs.\ Base & Wilcoxon & $<$0.001 & 0.802 \\
157	TG vs.\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\
158	TG vs.\ +PCGrad & Wilcoxon & 0.002 & --- \\
159	SS vs.\ TG & Wilcoxon & $<$0.001 & 0.869 \\
160	\midrule
161	\multicolumn{4}{l}{\emph{Gate conditioning (28 layers)}} \\
162	Turn 1 vs.\ Turn 21 & Wilcoxon & $3.7\!\times\!10^{-8}$ & 0.975 \\
163	\midrule
164	\multicolumn{4}{l}{\emph{Instruction retention}} \\
165	$\beta$\,=\,0 vs.\ $\beta$\,=\,3 & McNemar & 0.077 & --- \\
166	GAR--compliance & Pearson & 0.007 & 0.200 \\
167	\bottomrule
168	\end{tabular}
169	\end{table}
170	
171	\section{Llama-3.1-8B Complete Results}\label{sec:appendix-llama}
172	
173	Table~\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \S\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.
174	
175	\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\ 0.50).
176	
177	\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\,=\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\% for ThreadGate (mean 0.043, std 0.100), and 5\% of turn-level measurements exhibit sporadic attention spikes (GAR $\geq$ 0.4). We therefore report both mean and median.
178	
179	\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719, L24\,=\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\times$ by median for Llama vs.\ 8--17$\times$ for Qwen).
180	
181	\begin{table}[t]
182	\centering\small
183	\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\,=\,50); AR: autoregressive ($N$\,=\,20 for Base/TG/LoRA-only, $N$\,=\,50 for SS). Median is more representative due to heavy-tailed AR distributions (SS uses mean only).}
184	\label{tab:llama-full}
185	\resizebox{\columnwidth}{!}{%
186	\begin{tabular}{lcccc}
187	\toprule
188	& \multicolumn{2}{c}{\textbf{TF}} & \multicolumn{2}{c}{\textbf{AR}} \\
189	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
190	& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\
191	\midrule
192	Base & 0.017 & 3.45 & 0.009 & 0.009 \\
193	ThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\
194	LoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\
195	\textbf{SS} & 0.477 & 2.82 & \textbf{0.166} & --- \\
196	\bottomrule
197	\end{tabular}}
198	\end{table}
199	
200	\FloatBarrier
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f26b8a4-f6cb-4f49-a65c-56975d1de6d3",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "66febe71-9926-468f-8824-7bc92b580b0b",
  "sourceToolAssistantUUID": "9f26b8a4-f6cb-4f49-a65c-56975d1de6d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-26T03:40:43.268Z_

<details open><summary>🔧 Tool call — Grep · `toolu_015jhMVnndb1J56xfLGgV3iH`</summary>

```json
{
  "pattern": "\\\\section\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66febe71-9926-468f-8824-7bc92b580b0b",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVAbzmHeUF69VZhrg9F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad1fa871-9de2-45b4-aa83-e9f11f550060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DU3yo3nKhWT9wceUU3eBQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8507,
      "cache_read_input_tokens": 37128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8507,
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

_source line 27 · 2026-05-26T03:40:43.297Z_

<details><summary>↩ Tool result · `toolu_015jhMVnndb1J56xfLGgV3iH`</summary>

```text
1:\section{Training Configuration}\label{sec:appendix-hyper}
35:\section{Loss Formulation Search}\label{sec:appendix-loss}
68:\section{Instruction Retention Details}\label{sec:appendix-ir}
107:\section{Long-Conversation AR Evaluation}\label{sec:appendix-n5}
135:\section{Statistical Test Details}\label{sec:appendix-stats}
171:\section{Llama-3.1-8B Complete Results}\label{sec:appendix-llama}
236:\section{Additional Visualizations}\label{sec:appendix-viz}
340:\section{Per-Layer Gate Profile}\label{sec:appendix-gate-profile}
370:\section{Scheduled Sampling Implementation}\label{sec:appendix-ss}
387:\section{Computational Cost Analysis}\label{sec:appendix-cost}
420:\section{Qualitative Steering Examples}\label{sec:appendix-examples}
442:\section{Gradient Conflict Analysis}\label{sec:appendix-gradient}
468:\section{Training Data Characteristics}\label{sec:appendix-data}
489:\section{Exposure Bias Scaling}\label{sec:appendix-eb-scaling}
506:\section{Per-Turn AR GAR Dynamics}\label{sec:appendix-ar-gar-dynamics}
528:\section{Per-Head KL Divergence Analysis}\label{sec:appendix-kl}
553:\section{GAR Definition Robustness}\label{sec:appendix-gar-robust}
577:\section{General Capability Preservation (MMLU)}\label{sec:appendix-mmlu}
601:\section{Cross-Scale Validation (Qwen-2.5-1.5B)}\label{sec:appendix-1.5b}
631:\section{Per-Seed Detailed Results}\label{sec:appendix-perseed}
645:\section{Per-Turn GAR Decay Analysis}\label{sec:appendix-perturn-detail}
675:\section{Extended Dataset Statistics}\label{sec:appendix-dataset-ext}
687:\section{Extended GAR Robustness Analysis}\label{sec:appendix-gar-ext}
704:\section{MMLU Category Breakdown}\label{sec:appendix-mmlu-ext}
723:\section{Extended Cross-Scale Results (Qwen-2.5-1.5B)}\label{sec:appendix-1.5b-ext}
737:\section{Extended Statistical Analysis}\label{sec:appendix-stats-ext}
753:\section{Extended Training Dynamics}\label{sec:appendix-training-ext}
770:\section{Per-$\beta$ Steering Visualization}\label{sec:appendix-steering-viz}
791:\section{Llama-3.1-8B Scheduled Sampling Details}\label{sec:appendix-llama-ss}
841:\section{Use of AI Assistance}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad1fa871-9de2-45b4-aa83-e9f11f550060",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "fbf071e3-9167-4178-b10c-312328ebdad8",
  "sourceToolAssistantUUID": "ad1fa871-9de2-45b4-aa83-e9f11f550060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-26T03:40:43.653Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RTCoMQaGmf8vVkanh89dNk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbf071e3-9167-4178-b10c-312328ebdad8",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVAbzmHeUF69VZhrg9F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95691c47-7f03-46b8-940c-c044f760607d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DU3yo3nKhWT9wceUU3eBQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8507,
      "cache_read_input_tokens": 37128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8507,
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

_source line 29 · 2026-05-26T03:40:43.661Z_

<details><summary>↩ Tool result · `toolu_01RTCoMQaGmf8vVkanh89dNk`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\looseness=-1 NTP self-recovers because prediction is the same task at both regimes \citep{he2019exposure}; GAR optimizes a \emph{global property} (attention allocation to goal tokens) with no autoregressive counterpart. The collapse is selective: GAR-ours collapses by an order of magnitude while GAR-Dongre shows negligible shift (${\leq}$1.3$\times$). Per-head analysis confirms selectivity: heads with higher TF GAR shift most under AR ($r$\,=\,0.743; Appendix~\ref{sec:appendix-kl}). Any auxiliary attention objective targeting distributional properties rather than prediction itself should face the same barrier under teacher forcing.
4	
5	\looseness=-1 Our diagnostic exclusion identifies exposure bias as a primary contributing factor, but cannot fully rule out KV cache drift (\S\ref{sec:limitations}). The PCGrad exclusion rules out direction conflict but not magnitude imbalance (7.5--25.7$\times$ NTP dominance; \citealp{chen2018gradnorm}). The GAR--compliance correlation is weak ($r$\,=\,0.200; Appendix~\ref{sec:appendix-ir}), reinforcing GAR's role as a diagnostic probe. Our $\beta$-steering is likewise a \emph{diagnostic}, distinct from inference-time remedies such as split-softmax \citep{li2024measuring} and Rhea \citep{hong2025rhea}. SS and inference-time fixes are complementary: SS modifies representations without inference cost; inference-time methods cannot recover patterns never learned. At $\beta$\,=\,5 the two converge (SS\,=\,0.717 vs.\ TG\,=\,0.727).
6	
7	\looseness=-1 Our findings resonate with the attention forcing framework \citep{dou2019attention,dou2022parallel}, which independently observed that attention patterns learned under teacher forcing degrade during autoregressive generation in NMT---a diagnosis consistent with the exposure bias mechanism we identify in multi-turn dialogue. Where attention forcing intervenes by supervising cross-attention to correct the training--inference mismatch, our work reveals that the mismatch persists even when auxiliary self-attention objectives are jointly optimized with NTP, suggesting that the teacher-forcing gap poses a structural obstacle beyond what single-task attention supervision addresses.
8	
9	\looseness=-1 Despite the weak GAR--compliance correlation ($r^2$\,=\,0.04), GAR retains independent diagnostic value: it directly quantifies how exposure bias reshapes attention allocation toward goal tokens, a mechanism invisible to surface-level compliance metrics. The downstream effect is category-dependent---content-constrained instructions benefit substantially (+23.8\,pp under $\beta$\,=\,3 steering) while format, count, and positional constraints show no change, suggesting that the attention shift GAR captures is necessary only for tasks requiring sustained reference to earlier context.
10	
11	\looseness=-1 We note that SS's benefit may partly reflect a curriculum learning effect---the linear schedule progressively increases difficulty by exposing more model-generated tokens---rather than a pure exposure bias correction. However, the core SS mechanism (substituting model generations for ground-truth prefixes) directly instantiates the definition of exposure bias mitigation, and the resulting gap compression is consistent across seeds and architectures.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95691c47-7f03-46b8-940c-c044f760607d",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "b5cf659f-d54d-47af-88f2-a55617b02164",
  "sourceToolAssistantUUID": "95691c47-7f03-46b8-940c-c044f760607d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-26T03:40:43.803Z_

<details open><summary>🔧 Tool call — Read · `toolu_019zQxkWBHSTTe34ju7ba811`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5cf659f-d54d-47af-88f2-a55617b02164",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVAbzmHeUF69VZhrg9F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67ba8988-a2ac-47a5-87ec-4b06ba0b1956",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DU3yo3nKhWT9wceUU3eBQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8507,
      "cache_read_input_tokens": 37128,
      "output_tokens": 395,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8507
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 395,
          "cache_read_input_tokens": 37128,
          "cache_creation_input_tokens": 8507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8507,
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

_source line 31 · 2026-05-26T03:40:43.815Z_

<details><summary>↩ Tool result · `toolu_019zQxkWBHSTTe34ju7ba811`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\,=\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\beta$-steering recovers GAR above the TF baseline, consistent with attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\sim}$1.3$\times$ (Qwen) and ${\sim}$2.9$\times$ (Llama), generalizing across architectures and seeds; to our knowledge, the first such transfer to auxiliary attention objectives in multi-turn transformers.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67ba8988-a2ac-47a5-87ec-4b06ba0b1956",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "7402471c-a102-466f-865f-4c305c559523",
  "sourceToolAssistantUUID": "67ba8988-a2ac-47a5-87ec-4b06ba0b1956",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-26T03:40:46.880Z_

Now let me read the "Use of AI Assistance" section from the appendix and check the computational cost section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7402471c-a102-466f-865f-4c305c559523",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVBBww8BsyLWf9ZXWYE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5022d62-5206-48df-af15-be9f5afe0cc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WcNrTgC34CzkJZBaEatpkc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8249,
      "cache_read_input_tokens": 45635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8249,
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

_source line 33 · 2026-05-26T03:40:48.921Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TQ6DUPYZjWUwoNiZ8QApCM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex",
  "offset": 841
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5022d62-5206-48df-af15-be9f5afe0cc3",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVBBww8BsyLWf9ZXWYE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80b6c785-1e93-4acf-ac32-31cfd8018bf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WcNrTgC34CzkJZBaEatpkc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8249,
      "cache_read_input_tokens": 45635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8249,
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

_source line 34 · 2026-05-26T03:40:48.928Z_

<details><summary>↩ Tool result · `toolu_01TQ6DUPYZjWUwoNiZ8QApCM`</summary>

```text
841	\section{Use of AI Assistance}
842	We used Claude for coding, code drafting, debugging, and language polishing.
843	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80b6c785-1e93-4acf-ac32-31cfd8018bf5",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "a543f968-bc0a-401d-a22b-a197ef9b30b0",
  "sourceToolAssistantUUID": "80b6c785-1e93-4acf-ac32-31cfd8018bf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-26T03:40:49.737Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NQZAT7XWsbGqzxHCr5UH8F`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex",
  "offset": 387,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a543f968-bc0a-401d-a22b-a197ef9b30b0",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVBBww8BsyLWf9ZXWYE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ba1b29c-51c9-4f40-b9e5-276eeb386863",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WcNrTgC34CzkJZBaEatpkc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8249,
      "cache_read_input_tokens": 45635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8249,
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

_source line 36 · 2026-05-26T03:40:49.744Z_

<details><summary>↩ Tool result · `toolu_01NQZAT7XWsbGqzxHCr5UH8F`</summary>

```text
387	\section{Computational Cost Analysis}\label{sec:appendix-cost}
388	
389	\begin{table}[t]
390	\centering\small
391	\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\,GB VRAM).}
392	\label{tab:cost}
393	\resizebox{\columnwidth}{!}{%
394	\begin{tabular}{lcccc}
395	\toprule
396	\textbf{Config} & \textbf{Params} & \textbf{Time (h)} & \textbf{VRAM} & \textbf{Overhead} \\
397	\midrule
398	\multicolumn{5}{l}{\emph{Qwen-2.5-7B-Instruct}} \\
399	LoRA-only & 4.2M & 6.0 & 42\,GB & baseline \\
400	ThreadGate & 4.3M & 6.0 & 43\,GB & $+$57K \\
401	\;+\,PCGrad & 4.3M & 8.0 & 43\,GB & $+$33\% \\
402	Uniform Gate & 4.3M & 6.0 & 43\,GB & $+$57K \\
403	SS (s42) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
404	SS (s123) & 4.3M & 10.8 & 43\,GB & $+$80\% \\
405	SS (s456) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
406	\midrule
407	\multicolumn{5}{l}{\emph{Llama-3.1-8B-Instruct}} \\
408	LoRA-only & 4.2M & 7.0 & 45\,GB & baseline \\
409	ThreadGate & 4.3M & 7.3 & 46\,GB & $+$65K \\
410	\bottomrule
411	\end{tabular}}
412	\end{table}
413	
414	\paragraph{Parameter overhead.} ThreadGate adds ${\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\times$ 2K per gate MLP) and ${\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.
415	
416	\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 6.0--7.3 hours. PCGrad adds ${\sim}$33\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\% (6.5h) due to efficient batched generation, while seed 123 adds 80\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.
417	
418	\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\to$64$\to$1 MLP forward pass per layer adds $<$0.1\% latency. $\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.
419	
420	\section{Qualitative Steering Examples}\label{sec:appendix-examples}
421	
422	Table~\ref{tab:examples} illustrates the effect of $\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''
423	
424	\begin{table*}[t]
425	\centering\small
426	\caption{Qualitative effect of $\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}
427	\label{tab:examples}
428	\begin{tabular}{c p{5.5cm} p{5.5cm}}
429	\toprule
430	\textbf{Turn} & \textbf{$\beta$\,=\,0 (unsteered)} & \textbf{$\beta$\,=\,3 (steered)} \\
431	\midrule
432	1 & \checkmark~Three bullet points, on-topic & \checkmark~Three bullet points, on-topic \\
433	2 & \checkmark~Three bullet points, relevant & \checkmark~Three bullet points, relevant \\
434	3 & $\sim$~Four bullet points, partially on-topic & \checkmark~Three bullet points, on-topic \\
435	4 & \texttimes~Free-form paragraph, no bullets & \checkmark~Three bullet points, on-topic \\
436	\bottomrule
437	\end{tabular}
438	\end{table*}
439	
440	The pattern is consistent with the GAR decay analysis (\S\ref{sec:analysis}): unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. The per-category breakdown in Table~\ref{tab:ir-results} shows that content constraints benefit most from this effect.
441	
442	\section{Gradient Conflict Analysis}\label{sec:appendix-gradient}
443	
444	\begin{figure}[t]
445	  \centering
446	  \includegraphics[width=\columnwidth,height=0.42\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}
447	  \caption{(a)~Training GAR convergence to target ($\tau$\,=\,0.5). (b)~PCGrad removes gradient conflict but $\mathcal{L}_\text{GAR}$ still collapses, confirming that gradient direction conflict is not the primary cause (\S\ref{subsec:pcgrad}).}
448	  \label{fig:training-pcgrad}
449	\end{figure}
450	
451	This section provides extended gradient interaction analysis supporting the PCGrad exclusion argument in \S\ref{subsec:pcgrad}. We measure per-layer cosine similarity between NTP and GAR gradients, gradient magnitude ratios, and the effect of PCGrad projection on these quantities.
452	
453	\paragraph{Gradient direction analysis.} Figure~\ref{fig:gradient-heatmap} visualizes the per-layer cosine similarity between NTP and GAR gradients across training epochs for both standard ThreadGate and PCGrad training. Under standard training, 79\% of layers show negative cosine similarity (gradient conflict) at epoch~0, declining to 68\% by epoch~2 as GAR loss converges to near-zero. This decline reflects diminishing GAR gradient magnitude rather than alignment improvement---as GAR loss approaches zero, the GAR gradient shrinks proportionally, making cosine similarity measurements less reliable (small gradients produce noisy direction estimates). Under PCGrad training, the conflict percentage decreases more slowly (79\%$\to$71\%), consistent with PCGrad projecting conflicting gradients onto the other's normal plane but not eliminating the underlying gradient conflict.
454	
455	\paragraph{Spatial patterns.} The early layers (L0--L5) and output-adjacent layers (L24--L27) show the strongest conflict, corresponding to the layers where gate values deviate most from identity (Figure~\ref{fig:gate-heatmap}). This spatial correlation is not causal: removing gradient conflict via PCGrad does not improve AR GAR, and gates at high-conflict layers are not systematically different from gates at low-conflict layers (Spearman $\rho$\,=\,$-$0.12, $p$\,=\,0.54 between gate value and conflict magnitude).
456	
457	\paragraph{Magnitude dominance.} NTP gradient magnitude dominates GAR by 7.5$\times$ at epoch~0 and 14.7$\times$ by epoch~2, as GAR loss converges while NTP loss remains at $\sim$0.93. This growing dominance means that even when directions oppose, the effective update direction is determined almost entirely by NTP. PCGrad addresses gradient conflict but not magnitude dominance---it projects conflicting gradients onto the other's normal plane (changing direction) but preserves relative magnitudes. The 7.5--14.7$\times$ magnitude ratio means that even after PCGrad projection, GAR contributes $<$7\% of the effective update magnitude, explaining why PCGrad is ineffective.
458	
459	\paragraph{Cross-model consistency.} Table~\ref{tab:gradient-crossmodel} confirms the pattern on Llama-3.1-8B: gradients are near-orthogonal (mean cosine $+$0.005, essentially zero) rather than systematically conflicting, with 25.7$\times$ NTP dominance. The Llama result is particularly informative because it shows that even without systematic gradient conflict (53\% negative layers, near chance), the same TF-AR gap persists. This cross-model evidence strengthens the \textit{modus tollens} argument: if gradient conflict were the cause, it should be present on both architectures; it is absent on Llama, yet the gap persists; therefore gradient direction conflict is not the primary cause.
460	
461	\begin{figure*}[t]
462	\centering
463	\includegraphics[width=0.95\textwidth]{fig_gradient_conflict_heatmap.pdf}
464	\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\% to 68\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\%$\to$71\%) but does not improve AR GAR, ruling out gradient direction conflict as the primary cause (\S\ref{subsec:pcgrad}).}
465	\label{fig:gradient-heatmap}
466	\end{figure*}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ba1b29c-51c9-4f40-b9e5-276eeb386863",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "d32a888a-9e3b-492b-984b-ec818140fb07",
  "sourceToolAssistantUUID": "4ba1b29c-51c9-4f40-b9e5-276eeb386863",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-26T03:40:50.511Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AAY6rdkNyWCG9X5JMBtDpv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex",
  "offset": 236,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d32a888a-9e3b-492b-984b-ec818140fb07",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVBBww8BsyLWf9ZXWYE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42d0eb68-fe52-4fdd-92c5-319783c43998",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WcNrTgC34CzkJZBaEatpkc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8249,
      "cache_read_input_tokens": 45635,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8249
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 352,
          "cache_read_input_tokens": 45635,
          "cache_creation_input_tokens": 8249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8249,
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

_source line 38 · 2026-05-26T03:40:50.524Z_

<details><summary>↩ Tool result · `toolu_01AAY6rdkNyWCG9X5JMBtDpv`</summary>

```text
236	\section{Additional Visualizations}\label{sec:appendix-viz}
237	
238	This section presents extended visualizations referenced in the main text. Each figure examines a different aspect of the gating behavior and its failure under autoregressive generation.
239	
240	\subsection{Gate Profile Heatmap}
241	
242	Figure~\ref{fig:gate-heatmap} shows the per-layer gate values across all training configurations for both Qwen-2.5-7B (28 layers) and Llama-3.1-8B (32 layers). The key observation is that early layers consistently receive the lowest gate values across all conditions, suggesting that these layers contribute more dispensable computations for the NTP objective. The pattern is remarkably consistent across ThreadGate, Uniform Gate, and PCGrad variants, indicating that gate-value allocation is driven primarily by the NTP loss landscape rather than the GAR auxiliary objective.
243	
244	\begin{figure}[H]
245	\centering
246	\includegraphics[width=\columnwidth]{fig_gate_profile_heatmap.pdf}
247	\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\times$ 5 conditions) and Llama-3.1-8B (32 layers $\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}
248	\label{fig:gate-heatmap}
249	\end{figure}
250	
251	\subsection{Cross-Model Gate Profile Comparison}
252	
253	Figure~\ref{fig:gate-crossmodel} compares gate profiles between the two architectures. Qwen-2.5-7B shows minimum gate values at early layers (L1\,=\,0.793, L5\,=\,0.797), suggesting these layers are most amenable to attenuation without disrupting NTP. Llama-3.1-8B instead shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719), indicating that architecturally distinct models learn different layer-importance hierarchies. Both profiles converge toward identity at their respective final layers, consistent with NTP gradient pressure dominating gate optimization at output-adjacent layers.
254	
255	\begin{figure}[H]
256	\centering
257	\includegraphics[width=\columnwidth]{fig_gate_profile_crossmodel.pdf}
258	\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}
259	\label{fig:gate-crossmodel}
260	\end{figure}
261	
262	\subsection{Per-Turn AR GAR Decay}
263	
264	Figure~\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\% from turn 1 to turn 10; Llama base drops 90\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\ref{tab:five-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.
265	
266	\begin{figure}[H]
267	\centering
268	\includegraphics[width=\columnwidth]{fig_ar_gar_perturn.pdf}
269	\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\% (turn 1$\to$10), Llama base drops 90\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}
270	\label{fig:ar-gar-perturn}
271	\end{figure}
272	
273	\subsection{Bootstrap Confidence Intervals}
274	
275	Figure~\ref{fig:bootstrap-ci} shows the bootstrap resampling distributions underlying the 95\% CIs reported in Table~\ref{tab:five-way}.
276	
277	\begin{figure}[H]
278	  \centering
279	  \includegraphics[width=\columnwidth]{fig_bootstrap_ci.pdf}
280	  \caption{Bootstrap CI distributions for AR GAR-ours (ThreadGate vs.\ LoRA-only, $N$\,=\,50, 10K resamples). Distributions overlap substantially, consistent with the modest effect size ($r$\,=\,0.454).}
281	  \label{fig:bootstrap-ci}
282	\end{figure}
283	
284	\subsection{Gate Value Distributions}
285	
286	Figure~\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.
287	
288	\begin{figure}[H]
289	\centering
290	\includegraphics[width=\columnwidth]{fig_gate_distribution.pdf}
291	\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}
292	\label{fig:gate-distribution}
293	\end{figure}
294	
295	\subsection{Training Loss Curves}
296	
297	Figure~\ref{fig:training-loss} shows the NTP, GAR, and total loss trajectories during training. GAR loss collapses to near-zero within the first epoch across all variants, indicating rapid convergence of the auxiliary objective under teacher forcing. NTP loss converges normally to ${\sim}$0.93 by epoch 3. The fast GAR convergence is not itself pathological---it indicates successful optimization under the training distribution. The pathology emerges only at the transition to autoregressive generation, where the learned attention patterns fail to transfer.
298	
299	\begin{figure}[H]
300	\centering
301	\includegraphics[width=\columnwidth]{fig_training_loss_curves.pdf}
302	\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}
303	\label{fig:training-loss}
304	\end{figure}
305	
306	\subsection{Full Attention Steering Results}\label{sec:appendix-steering}
307	
308	\begin{table*}[t]
309	\centering\small
310	\caption{Full attention steering results across evaluation settings.
311	\textbf{Bold} indicates the operating point cited in the main text ($\beta$\,=\,5).
312	A visual gap separates the phase-transition boundary: GAR jumps sharply between $\beta$\,=\,2 and $\beta$\,=\,3 across all settings.}
313	\label{tab:steering-full}
314	\begin{tabular}{r cc cc cc}
315	\toprule
316	 & \multicolumn{2}{c}{\textbf{$N$\,=\,5, Gen}} & \multicolumn{2}{c}{\textbf{$N$\,=\,50, Gen}} & \multicolumn{2}{c}{\textbf{$N$\,=\,200, TF}} \\
317	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
318	$\beta$ & GAR & PPL & GAR & PPL & GAR & PPL \\
319	\midrule
320	0   & .028 & 1.41 & $.064 \pm .081$ & $1.43 \pm .10$ & .535 & 2.62 \\
321	0.5 & .029 & 1.39 & ---             & ---             & ---  & ---  \\
322	1   & .035 & 1.36 & ---             & ---             & ---  & ---  \\
323	2   & .062 & 1.41 & $.128 \pm .110$ & $1.48 \pm .14$ & .611 & 2.69 \\
324	\addlinespace[3pt]
325	3   & ---  & ---  & $.556 \pm .060$ & $1.56 \pm .17$ & .788 & 2.93 \\
326	4   & ---  & ---  & $.644 \pm .061$ & $1.67 \pm .22$ & .817 & 3.49 \\
327	\textbf{5}  & \textbf{.680} & \textbf{1.91} & $\mathbf{.727 \pm .061}$ & $\mathbf{1.77 \pm .27}$ & \textbf{.833} & \textbf{6.15} \\
328	10  & .959 & 4.22 & $.961 \pm .015$ & $3.45 \pm 1.78$ & .977 & 505.2 \\
329	\bottomrule
330	\end{tabular}
331	\end{table*}
332	
333	\begin{figure}[t]
334	  \centering
335	  \includegraphics[width=\columnwidth]{fig_steering_standalone.pdf}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42d0eb68-fe52-4fdd-92c5-319783c43998",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "fc4acdad-5c9b-4a24-9274-6ce4fac8624a",
  "sourceToolAssistantUUID": "42d0eb68-fe52-4fdd-92c5-319783c43998",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-26T03:40:54.705Z_

Now let me check for the references/bibliography file and the main results table.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc4acdad-5c9b-4a24-9274-6ce4fac8624a",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVBgkHoEi4jfK1phS5p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7a3d1b5-b71e-4b72-a64b-ff8ee36b6c9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vb4KhER7KZzYTWSySydSaX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5594,
      "cache_read_input_tokens": 53884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5594,
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

_source line 40 · 2026-05-26T03:40:58.170Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01SLZLHVvaYM415hWDyNJ321`</summary>

```json
{
  "pattern": "\\\\begin\\{table|tab:five-way",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/experiments.tex",
  "output_mode": "content",
  "-A": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7a3d1b5-b71e-4b72-a64b-ff8ee36b6c9c",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVBgkHoEi4jfK1phS5p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7665595f-03f0-41c7-b264-e69adc96b26b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vb4KhER7KZzYTWSySydSaX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5594,
      "cache_read_input_tokens": 53884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5594,
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

_source line 41 · 2026-05-26T03:40:58.183Z_

<details><summary>↩ Tool result · `toolu_01SLZLHVvaYM415hWDyNJ321`</summary>

```text
10:[Omitted long matching line]
11-
12-[Omitted long context line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7665595f-03f0-41c7-b264-e69adc96b26b",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "458a31e3-c948-450a-9b27-35b0e0bad8ba",
  "sourceToolAssistantUUID": "7665595f-03f0-41c7-b264-e69adc96b26b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-26T03:40:58.753Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01NuzCFQroD7rLNMVA9AUXtB`</summary>

```json
{
  "pattern": "\\\\begin\\{table",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex",
  "output_mode": "content",
  "-A": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "458a31e3-c948-450a-9b27-35b0e0bad8ba",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVBgkHoEi4jfK1phS5p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0b093b8-a019-4f3f-a735-94cb8d72fc18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vb4KhER7KZzYTWSySydSaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5594,
      "cache_read_input_tokens": 53884,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5594
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 302,
          "cache_read_input_tokens": 53884,
          "cache_creation_input_tokens": 5594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5594,
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

_source line 43 · 2026-05-26T03:40:58.763Z_

<details><summary>↩ Tool result · `toolu_01NuzCFQroD7rLNMVA9AUXtB`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0b093b8-a019-4f3f-a735-94cb8d72fc18",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "940e9f5b-1922-40da-a157-bd750746a5ff",
  "sourceToolAssistantUUID": "a0b093b8-a019-4f3f-a735-94cb8d72fc18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-26T03:41:00.935Z_

Let me find the main results table (Table 1 / five-way).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "940e9f5b-1922-40da-a157-bd750746a5ff",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVCHu9DfF5q78hhWocz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44a6847a-9328-4c43-9b87-250f606ea10a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011JX8CcL2iqbcVCkei7ZGD8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 492,
      "cache_read_input_tokens": 59478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 492,
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

_source line 45 · 2026-05-26T03:41:02.676Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01DvMrBHYjwQXg6ovWa5mfyN`</summary>

```json
{
  "pattern": "tab:five-way|\\\\begin\\{table",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper",
  "glob": "**/method.tex",
  "output_mode": "content",
  "-C": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44a6847a-9328-4c43-9b87-250f606ea10a",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVCHu9DfF5q78hhWocz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd13ec8c-749b-458f-89ca-405198d7f488",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011JX8CcL2iqbcVCkei7ZGD8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 492,
      "cache_read_input_tokens": 59478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 492,
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

_source line 46 · 2026-05-26T03:41:02.698Z_

<details><summary>↩ Tool result · `toolu_01DvMrBHYjwQXg6ovWa5mfyN`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd13ec8c-749b-458f-89ca-405198d7f488",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "81b9be7c-4088-45b1-a69b-0bc7b8824561",
  "sourceToolAssistantUUID": "bd13ec8c-749b-458f-89ca-405198d7f488",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-26T03:41:03.361Z_

<details open><summary>🔧 Tool call — Grep · `toolu_018pNcyAQZi32ZZtawiUbHuY`</summary>

```json
{
  "pattern": "tab:five-way",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper",
  "output_mode": "content",
  "-C": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81b9be7c-4088-45b1-a69b-0bc7b8824561",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVCHu9DfF5q78hhWocz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39e87d73-e16a-41a3-9949-2843177eeab8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011JX8CcL2iqbcVCkei7ZGD8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 492,
      "cache_read_input_tokens": 59478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 492,
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

_source line 48 · 2026-05-26T03:41:03.377Z_

<details><summary>↩ Tool result · `toolu_018pNcyAQZi32ZZtawiUbHuY`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex-4-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex-5-  \includegraphics[width=\textwidth]{fig3_gate_shift.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex:6:  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift ($N$\,=\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\times$) exceed final $N$\,=\,50 estimates (8--17$\times$; Table~\ref{tab:five-way}) due to smaller sample size.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex-7-  \label{fig:gate-shift}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex-8-\end{figure*}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex-12-\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex-13-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex:14:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex-15-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex-16-\subsection{PCGrad Gradient Direction Conflict Exclusion}\label{subsec:pcgrad}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex-22-\subsection{Distribution Shift Analysis}\label{subsec:dist-shift}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex-23-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex:24:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex-25-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex-26-\subsection{Mechanism Specificity}\label{subsec:mechanism-specificity}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/related_work.tex-14-\small
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/related_work.tex-15-\caption{Five-way comparison on Qwen-2.5-7B-Instruct. TF evaluation uses IID UltraChat and 50 held-out conversations; AR evaluation uses $N$\,=\,50 held-out conversations (mean 3.6 user turns). All fine-tuned variants converge under TF ($\leq$2\,pp spread); the 8--17$\times$ TF-AR gap persists across all configurations. $\bar{g}\!\pm\!\sigma_g$: learned gate mean and std across 28 layers (LoRA-only has no gates). GAR-O = GAR-ours; GAR-D = GAR-Dongre \citep{dongre2026attention}.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/related_work.tex:16:\label{tab:five-way}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/related_work.tex-17-\begin{tabular}{l ccc ccc cc c}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/related_work.tex-18-\toprule
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/experiments.tex-8-\subsection{Main Results}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/experiments.tex-9-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/experiments.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/experiments.tex-11-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/experiments.tex-12-[Omitted long context line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-107-\section{Long-Conversation AR Evaluation}\label{sec:appendix-n5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-108-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex:109:The main results (Table~\ref{tab:five-way}) report AR GAR from $N$\,=\,50 held-out conversations with a mean of 3.6 user turns. Table~\ref{tab:n5-ar} presents complementary results on $N$\,=\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-110-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-111-[Omitted long context line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-117-\begin{table}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-118-\centering\small
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex:119:\caption{AR GAR-ours on $N$\,=\,5 ten-turn conversations. The gating advantage observed in Table~\ref{tab:five-way} ($N$\,=\,50, mean 3.6 turns) diminishes with conversation length.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-120-\label{tab:n5-ar}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-121-\begin{tabular}{lcc}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-122-\toprule
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex:123:\textbf{Configuration} & \textbf{AR GAR-O} & \textbf{$\Delta$ vs.\ Table~\ref{tab:five-way}} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-124-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-125-Base & 0.012 & $-$0.007 \\
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-139-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-140-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex:141:\paragraph{Bootstrap confidence intervals.} The 95\% CIs in Table~\ref{tab:five-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-142-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-143-\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \leq r < 0.5$ is medium, and $r \geq 0.5$ is large. The TG vs.\ LoRA-only effect ($r$\,=\,0.454) is medium, and TG vs.\ Base ($r$\,=\,0.802) is large.
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-262-\subsection{Per-Turn AR GAR Decay}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-263-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex:264:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-265-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-266-\begin{figure}[H]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-273-\subsection{Bootstrap Confidence Intervals}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-274-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex:275:Figure~\ref{fig:bootstrap-ci} shows the bootstrap resampling distributions underlying the 95\% CIs reported in Table~\ref{tab:five-way}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-276-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-277-\begin{figure}[H]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-508-To characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-509-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex:510:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-511-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-512-\begin{figure}[t]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-635-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-636-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex:637:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-638-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-639-[Omitted long context line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-645-\section{Per-Turn GAR Decay Analysis}\label{sec:appendix-perturn-detail}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-646-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex:647:Tables~\ref{tab:perturn-qwen} and~\ref{tab:perturn-llama} present per-turn AR GAR values for all configurations on both architectures, complementing the aggregate mid-turn GAR reported in the main text (Table~\ref{tab:five-way}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-648-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex-649-[Omitted long context line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux-236-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux-237-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux:238:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux-239-\@LN@col{1}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux-240-\@LN{181}{2}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux-527-\citation{yu2020pcgrad}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux-528-\citation{bengio2015scheduled,zhang2019bridging,arora2022exposure}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux:529:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux:530:\newlabel{fig:gate-shift}{{5}{7}{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift ($N$\,=\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\times $) exceed final $N$\,=\,50 estimates (8--17$\times $; Table~\ref {tab:five-way}) due to smaller sample size}{figure.caption.11}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux-531-\@LN@col{1}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux-532-\@LN{422}{6}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux-1172-\@LN{952}{12}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux-1173-\@LN@col{2}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux:1174:\@writefile{lot}{\contentsline {table}{\numberline {5}{\ignorespaces AR GAR-ours on $N$\,=\,5 ten-turn conversations. The gating advantage observed in Table~\ref {tab:five-way} ($N$\,=\,50, mean 3.6 turns) diminishes with conversation length.}}{13}{table.caption.29}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux:1175:\newlabel{tab:n5-ar}{{5}{13}{AR GAR-ours on $N$\,=\,5 ten-turn conversations. The gating advantage observed in Table~\ref {tab:five-way} ($N$\,=\,50, mean 3.6 turns) diminishes with conversation length}{table.caption.29}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux-1176-\@writefile{toc}{\contentsline {paragraph}{Wilcoxon signed-rank tests.}{13}{section*.30}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux-1177-\@LN{953}{12}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux-1963-\@LN{1581}{24}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux-1964-\@LN@col{1}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux:1965:\@writefile{lot}{\contentsline {table}{\numberline {20}{\ignorespaces Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct. TF evaluation uses 200 held-out conversations. AR evaluation uses extended-generation protocol ($N{=}5$, $T{=}10$ turns); under the gen-mode protocol ($N{=}50$) used in Table~\ref {tab:five-way}, seed 42 yields AR GAR 0.064 (gap 7.9$\times $); $N{=}50$ data for seed 123 is not available.}}{26}{table.caption.92}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux:1966:\newlabel{tab:perseed-tg}{{20}{26}{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct. TF evaluation uses 200 held-out conversations. AR evaluation uses extended-generation protocol ($N{=}5$, $T{=}10$ turns); under the gen-mode protocol ($N{=}50$) used in Table~\ref {tab:five-way}, seed 42 yields AR GAR 0.064 (gap 7.9$\times $); $N{=}50$ data for seed 123 is not available}{table.caption.92}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux-1967-\@writefile{toc}{\contentsline {paragraph}{Qwen per-turn dynamics.}{26}{section*.93}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.aux-1968-\@LN{1582}{25}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39e87d73-e16a-41a3-9949-2843177eeab8",
  "isSidechain": true,
  "promptId": "ae79effe-4fae-4a17-ad0d-1779d563e32c",
  "agentId": "adf0b047ae89c464e",
  "type": "user",
  "uuid": "a385f70e-06af-4fac-a0fb-3532eb0b3797",
  "sourceToolAssistantUUID": "39e87d73-e16a-41a3-9949-2843177eeab8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-26T03:42:07.302Z_

Here is the complete report of all findings:

---

## 1. Title and Abstract

**Title (exact):**
```
Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue
```

**Abstract (exact text):**
```
As multi-turn conversations grow longer, large language models progressively lose attention to the system-prompt goals that define their task, even when the underlying goal representations remain intact. Existing remedies operate at inference time, leaving a natural but untested alternative: training auxiliary attention losses alongside next-token prediction to directly optimize goal attention. This strategy assumes that attention patterns learned under teacher forcing will transfer to autoregressive generation, an assumption that classical exposure bias research has challenged for sequence models but that has never been examined for auxiliary attention objectives in multi-turn transformers.
We show this assumption fails. On a controlled five-way testbed spanning two architectures (Qwen-2.5-7B, Llama-3.1-8B), goal attention optimized to target under teacher forcing collapses by an order of magnitude under autoregressive generation. A diagnostic exclusion chain traces the failure to exposure bias, ruling out gradient conflict, gating mechanism, and parameter capacity as primary causes. Inference-time attention steering confirms that the collapse reflects attention misallocation rather than representation loss. Scheduled sampling, applied here for the first time to auxiliary attention objectives in multi-turn transformers, compresses the training--inference gap to near parity on Qwen and from ~27x to 2.9x on Llama, with no perplexity cost.
```
(Footnote in abstract: "Code and data are available at https://anonymous.4open.science/r/turn_residual_gating-8703/.")

---

## 2. Limitations Section

Located in `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/limitations.tex`

**Exact content:**
```
Our findings are demonstrated on two model families (Qwen-2.5-7B and Llama-3.1-8B) and a single dataset (UltraChat, 8K conversations). Although UltraChat spans 18 dialogue categories providing reasonable domain diversity, cross-dataset validation (e.g., ShareGPT, LMSYS-Chat) remains future work; generalization to other architectures and domains (e.g., code, reasoning) is likewise untested. All experiments use LoRA (rank 16); full fine-tuning may exhibit different sensitivity to the TF-AR gap, and the LoRA capacity constraint could confound the capacity exclusion step (LoRA-only vs. Base comparison in §5). Most configurations use a single seed (scheduled sampling validated on three seeds; §4.4), and quality assessment relies on PPL rather than comprehensive benchmarks (Hendrycks et al., Lin et al.). Our diagnostic exclusion identifies exposure bias as a primary factor but does not rule out KV cache drift as a contributing mechanism.
```

---

## 3. Appendix Structure

All appendix section titles (31 sections total):

| # | Section Title | Label |
|---|---|---|
| A | Training Configuration | `sec:appendix-hyper` |
| B | Loss Formulation Search | `sec:appendix-loss` |
| C | Instruction Retention Details | `sec:appendix-ir` |
| D | Long-Conversation AR Evaluation | `sec:appendix-n5` |
| E | Statistical Test Details | `sec:appendix-stats` |
| F | Llama-3.1-8B Complete Results | `sec:appendix-llama` |
| G | Additional Visualizations | `sec:appendix-viz` |
| H | Per-Layer Gate Profile | `sec:appendix-gate-profile` |
| I | Scheduled Sampling Implementation | `sec:appendix-ss` |
| J | Computational Cost Analysis | `sec:appendix-cost` |
| K | Qualitative Steering Examples | `sec:appendix-examples` |
| L | Gradient Conflict Analysis | `sec:appendix-gradient` |
| M | Training Data Characteristics | `sec:appendix-data` |
| N | Exposure Bias Scaling | `sec:appendix-eb-scaling` |
| O | Per-Turn AR GAR Dynamics | `sec:appendix-ar-gar-dynamics` |
| P | Per-Head KL Divergence Analysis | `sec:appendix-kl` |
| Q | GAR Definition Robustness | `sec:appendix-gar-robust` |
| R | General Capability Preservation (MMLU) | `sec:appendix-mmlu` |
| S | Cross-Scale Validation (Qwen-2.5-1.5B) | `sec:appendix-1.5b` |
| T | Per-Seed Detailed Results | `sec:appendix-perseed` |
| U | Per-Turn GAR Decay Analysis | `sec:appendix-perturn-detail` |
| V | Extended Dataset Statistics | `sec:appendix-dataset-ext` |
| W | Extended GAR Robustness Analysis | `sec:appendix-gar-ext` |
| X | MMLU Category Breakdown | `sec:appendix-mmlu-ext` |
| Y | Extended Cross-Scale Results (Qwen-2.5-1.5B) | `sec:appendix-1.5b-ext` |
| Z | Extended Statistical Analysis | `sec:appendix-stats-ext` |
| AA | Extended Training Dynamics | `sec:appendix-training-ext` |
| AB | Per-beta Steering Visualization | `sec:appendix-steering-viz` |
| AC | Llama-3.1-8B Scheduled Sampling Details | `sec:appendix-llama-ss` |
| (last) | **Use of AI Assistance** | (no label) |

**"Use of AI Assistance" exact content:**
```
We used Claude for coding, code drafting, debugging, and language polishing.
```

---

## 4. Datasets, Models, and Packages

**Datasets:**
- **UltraChat** (8K multi-turn conversations from training split; 18 dialogue categories)
- 50 non-overlapping held-out conversations for evaluation

**Models:**
- **Qwen-2.5-7B-Instruct** (primary, 28 layers)
- **Llama-3.1-8B-Instruct** (cross-model replication, 32 layers)
- **Qwen-2.5-1.5B** (cross-scale validation)
- GPT-4 used for content constraint evaluation (instruction retention)

**LaTeX Packages used:**
`acl` (review mode), `times`, `latexsym`, `fontenc` (T1), `inputenc` (utf8), `microtype`, `inconsolata`, `graphicx`, `amsmath`, `amssymb`, `booktabs`, `multirow`, `xcolor`, `subcaption`, `placeins`, `float`, `alphalph`, `etoolbox`

**ML methods/tools mentioned:**
- LoRA / QLoRA (PEFT fine-tuning)
- AdamW optimizer
- PCGrad (gradient surgery)
- Scheduled Sampling
- MMLU (5-shot evaluation)
- Bootstrap resampling (10,000 resamples)
- Wilcoxon signed-rank tests, McNemar's test, Pearson correlation

---

## 5. Hyperparameters, Model Sizes, GPU Details, Computational Budget

All reported:

**Hyperparameters** (Appendix A, Table 1):
- Base model: Qwen-2.5-7B-Instruct
- LoRA rank/alpha: 16/32, targets: q_proj, v_proj
- Optimizer: AdamW (beta1=0.9, beta2=0.999)
- Learning rate: 2e-4; Gate LR multiplier: 10x
- Batch size: 1, gradient accumulation: 8 (effective 8)
- Epochs: 3
- Max seq length: 2048
- Seeds: 42 (+123 for TG, SS)
- Lambda_GAR / Lambda_div: 1.0 / 1.0
- GAR target tau: 0.5
- Gate init bias: 1.5 (sigma approx 0.82)
- Gate hidden dim: 64, Turn embed dim: 16

**Model sizes:**
- LoRA-only: 4.2M trainable params
- ThreadGate: 4.3M trainable params (~57K gate params for Qwen, ~65K for Llama, <0.001% of 7B)

**GPU:**
- Single NVIDIA RTX PRO 6000 Blackwell Server Edition (96 GB VRAM)
- VRAM usage: 42-46 GB depending on config

**Computational budget** (Appendix J):
- 6.0-10.8 hours per variant (standard 6.0h, PCGrad 8.0h due to +33% overhead, SS seed 123 10.8h due to +80%)
- Llama: 7.0-7.3h per variant

---

## 6. Statistics (Error Bars, Confidence Intervals, Mean/Std)

Extensively reported:

- **Bootstrap 95% CIs**: Reported in Table 1 (five-way) via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages, percentile method
- **Standard deviations**: AR GAR-ours reported with +/- (e.g., 0.727 +/- 0.061 at beta=5; SS: 0.401 +/- 0.047 across 3 seeds)
- **Wilcoxon signed-rank p-values**: TG vs Base p<0.001 (r=0.802), TG vs LoRA-only p=0.004 (r=0.454), TG vs PCGrad p=0.002, SS vs TG p<0.001 (r=0.869), gate conditioning p=3.73e-8 (r=0.975)
- **McNemar's test**: Instruction retention beta=0 vs beta=3: p=0.077
- **Pearson correlation**: GAR-compliance r=0.200, p=0.007
- **Multiple comparisons**: Bonferroni correction discussed (threshold 0.0125); all significant results survive
- **Effect sizes**: Rank-biserial correlation r reported for all Wilcoxon tests
- **Multi-seed validation**: SS validated on 3 seeds (42, 123, 456); per-seed details in Appendix T
- **Coefficient of variation**: Reported for heavy-tailed Llama AR distributions (CoV > 100%)

---

## 7. PDF File Path

**PDF exists** at:
```
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/main.pdf
```
Size: 1,037,744 bytes (~1.0 MB), last modified: 2025-05-25 21:10.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a385f70e-06af-4fac-a0fb-3532eb0b3797",
  "isSidechain": true,
  "agentId": "adf0b047ae89c464e",
  "requestId": "req_011CbQVCfBJwb3UqeZn1EVXE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f8fc4c2-eef5-4a1e-a966-381c9c67a46c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "e025d39f-5fcc-4ef6-9d1b-afc6e0bdd79c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ENFmLH5ErsZcqTD7yoD7e4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6691,
      "cache_read_input_tokens": 59970,
      "output_tokens": 2721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6691
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2721,
          "cache_read_input_tokens": 59970,
          "cache_creation_input_tokens": 6691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6691,
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
