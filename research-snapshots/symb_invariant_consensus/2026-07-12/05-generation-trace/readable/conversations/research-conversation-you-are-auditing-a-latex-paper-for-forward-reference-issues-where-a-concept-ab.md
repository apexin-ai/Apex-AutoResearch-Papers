# Research conversation: You are auditing a LaTeX paper for "forward reference" issues — where a concept/abbreviation/symbol/method/metric is USE

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-af8784ad3137a4fe6.jsonl`
- **Structured JSON:** [`c4aceaddf352108d02a7.json`](../../sessions/c4/c4aceaddf352108d02a7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

35 recorded events

### User

_source line 1 · 2026-05-26T08:18:55.499Z_

You are auditing a LaTeX paper for "forward reference" issues — where a concept/abbreviation/symbol/method/metric is USED before it is DEFINED. 

Read ALL the following .tex files in this exact order (which is the paper's reading order):
1. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex
5. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex
6. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex
7. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex
8. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex
9. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex
10. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex

For EACH file, read it completely. Then produce a detailed report of every forward reference issue found. Specifically check:

1. **Abbreviations**: First use must include full form + abbreviation in parentheses. E.g., "Self-Consistency (SC)" before just "SC".
2. **Custom terms**: Terms the paper invents (like "symbolic confirmation bias", "SICA", "bias ratio", etc.) — first use must have a definition or at minimum a brief explanation.
3. **Math symbols**: Every variable in an equation must be explained at or before its first appearance.
4. **Method components**: Named modules/steps/phases must be introduced before being referenced.
5. **Metrics**: Custom evaluation metrics must be defined before appearing in tables or results.
6. **Dataset/setting names**: Internal names for experimental configurations must be explained before use.

For each issue found, report:
- The term/symbol/abbreviation
- WHERE it is first used (file + line number)
- WHERE it is first defined (file + line number), or "never defined" if applicable
- Severity: HIGH (reader would be confused), MEDIUM (reader can infer from context), LOW (standard ML term most readers know)

IMPORTANT: Standard well-known abbreviations (LLM, NLP, CoT, etc.) that are universally understood in the ML community are LOW severity at most. Focus on terms/symbols specific to THIS paper.

Also check: Does the abstract use terms that are only defined later? The abstract is special — it should be self-contained, so brief inline explanations of custom terms are expected.

Read every file completely — do not skim or skip sections. Be thorough and precise with line numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ed43d146-c225-42c6-832a-351ecc310242",
  "agentId": "af8784ad3137a4fe6",
  "type": "user",
  "uuid": "3503a6a2-a960-4e31-8605-b91c5450052c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-26T08:18:55.508Z_

```json
{
  "parentUuid": "3503a6a2-a960-4e31-8605-b91c5450052c",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
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
  "uuid": "4cd98d15-8c38-4842-ae66-18b159b98778",
  "timestamp": "2026-05-26T08:18:55.508Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

---

### Assistant

_source line 3 · 2026-05-26T08:18:58.596Z_



I'll read all 10 files in order. Let me start by reading them in parallel batches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cd98d15-8c38-4842-ae66-18b159b98778",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
  "requestId": "req_011CbQrPbs8aZR5cBHPMtGJV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2277108-84fe-4cc0-829b-8c20fd489628",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Q5j6zYG7JzuSt1MWtGUgA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33672,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33672,
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

_source line 4 · 2026-05-26T08:18:59.063Z_

<details open><summary>🔧 Tool call — Read · `toolu_019rxZjRrohYynYtW2QPG4mr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2277108-84fe-4cc0-829b-8c20fd489628",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
  "requestId": "req_011CbQrPbs8aZR5cBHPMtGJV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07aec6cb-d3e1-45a5-b98d-d2a58624f28e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Q5j6zYG7JzuSt1MWtGUgA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33672,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33672,
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

### Tool result

_source line 5 · 2026-05-26T08:18:59.082Z_

<details><summary>↩ Tool result · `toolu_019rxZjRrohYynYtW2QPG4mr`</summary>

```text
1	\begin{abstract}
2	Self-Consistency (SC) improves large language model (LLM) reasoning by majority voting over chain-of-thought traces. A natural extension extracts formal logical constraints from traces and aggregates them with a symbolic solver, but we show this is a \emph{symbolic mirage}. We test this through Symbolic Invariant Consensus Aggregation (SICA), which extracts first-order logic constraints under zero-shot prompting and solves weighted partial MAX-SAT. Self-extracted constraints systematically confirm their source trace's answer rather than providing independent verification, a phenomenon we term \emph{symbolic confirmation bias} (SCB). Formally, when nearly all constraints pass satisfiability checking, constraint-based aggregation degenerates to majority voting. This bias persists across nine models from 7B to frontier scale, with bias ratios of $1.66$--$4.97\times$. Twenty-seven training-free remediation strategies fail to break this bottleneck; a persistent independence--accuracy trade-off emerges where methods that reduce trace correlation also destroy accuracy. Among training-free approaches, only a structurally independent cross-architecture verifier restores corrective signal; the bottleneck lies in self-extraction itself, not model capability. We provide three lightweight diagnostics that predict failure modes from a pilot run\footnote{Code and data are available at \url{https://anonymous.4open.science/r/symb_invariant_consensus-2E1F/}.}.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07aec6cb-d3e1-45a5-b98d-d2a58624f28e",
  "isSidechain": true,
  "promptId": "ed43d146-c225-42c6-832a-351ecc310242",
  "agentId": "af8784ad3137a4fe6",
  "type": "user",
  "uuid": "094cdd8e-2f36-4882-8a19-a7c85aca4ac6",
  "sourceToolAssistantUUID": "07aec6cb-d3e1-45a5-b98d-d2a58624f28e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T08:19:00.024Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XJ7uuRxGudtQipt5f4gEqk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "094cdd8e-2f36-4882-8a19-a7c85aca4ac6",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
  "requestId": "req_011CbQrPbs8aZR5cBHPMtGJV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d6c9da5-d7a7-4d30-a44b-17e237ce32a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Q5j6zYG7JzuSt1MWtGUgA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33672,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33672,
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

### Tool result

_source line 7 · 2026-05-26T08:19:00.041Z_

<details><summary>↩ Tool result · `toolu_01XJ7uuRxGudtQipt5f4gEqk`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	\looseness=-1
4	Self-Consistency (SC) \citep{wang2023sc} selects the majority answer across $K$ chain-of-thought traces, a strategy grounded in the Condorcet Jury Theorem: independent voters converge to truth \citep{condorcet1785, ladha1992correlated}. In practice, SC's gains plateau for strong models \citep{loo2025reevaluating, byerly2025selfconsistency}, and correlated LLM errors \citep{kim2025correlated} reduce the effective ensemble size \citep{dietterich2000ensemble}. A natural remedy is to move beyond simple vote-counting: extract logical constraints from the traces, as in neuro-symbolic approaches \citep{pan2023logiclm, olausson2023linc, ye2024satlm}, and let a provably sound solver adjudicate. If the solver can filter contradictions and enforce logical consistency, it should recover information that raw majority voting discards.
5	
6	\begin{figure*}[t!]
7	\centering
8	\includegraphics[width=0.88\textwidth]{figures/fig1_pipeline_v11.pdf}
9	\caption{The SICA pipeline. SC selects the majority answer from $K$ traces. SICA extracts logical constraints, deduplicates, and solves MAX-SAT via Z3. Red dashed box: the independence bottleneck. Dashed arrow: oracle variant with gold FOL.}
10	\label{fig:pipeline}
11	\end{figure*}
12	
13	\looseness=-1
14	We test this intuition through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces, deduplicates them, and selects answers via weighted partial MAX-SAT (\S\ref{sec:pipeline}; Figure~\ref{fig:pipeline}). Across six models (7B--32B), four benchmarks, and multi-seed replication, SICA produces answers identical to majority voting on most problems; no condition shows a significant positive effect after FDR control (Table~\ref{tab:main_results}). The failure lies not in the solver but in the constraints it operates on: self-extracted constraints systematically support the model's majority answer, a robust empirical regularity we term \emph{symbolic confirmation bias} (\S\ref{sec:confirmation-bias}), distinct from trace-level unfaithfulness \citep{turpin2023language, wan2025unveiling}. Because each trace determines both an answer and its constraints, the formal verification channel approximately reduces to a weighted echo of the majority vote under the degeneration condition (Observation~1).
15	
16	\looseness=-1
17	This bias is not confined to a single model or task. Symbolic confirmation bias holds across nine models from 7B to frontier scale, and 27 training-free remediation strategies spanning four categories (prompt diversity, constraint filtering, multi-agent debate, and cross-model extraction) all produce neutral-to-negative results (\S\ref{sec:remediation}). A persistent independence--accuracy trade-off emerges: methods that break trace correlation (e.g., multi-agent debate; \citealp{liang2023encouraging, du2023improving}) destroy accuracy, while methods that preserve accuracy fail to achieve independence. Prior work demonstrates that LLMs cannot self-correct reasoning without external feedback \citep{huang2024selfcorrect, kamoi2024selfcorrect}; our analysis provides a concrete mechanism for these findings via the $M{\to}T{\to}(A,C)$ generation structure, where constraints are downstream of the same generative process that produces the answers they are meant to check.
18	
19	\looseness=-1
20	The bottleneck lies in self-extraction itself, not in solver capability or model scale. Cross-architecture verification provides preliminary evidence of escape ($n{=}6$ generator--verifier pairs, exploratory): a structurally independent verifier yields significant gains when it exceeds the generator's accuracy, with benefit governed by a capability-gap pattern between verifier and generator (\S\ref{sec:cross-arch}). This result parallels test-time compute scaling \citep{snell2025scaling}, where additional inference budget faces diminishing returns once effective ensemble diversity saturates. Three lightweight diagnostics derived from a pilot run enable practitioners to predict a priori whether a self-extraction-based aggregation method will improve over SC (\S\ref{sec:diagnostic-framework}).
21	
22	Our contributions are:
23	\begin{enumerate}[nosep,leftmargin=*]
24	\item \textbf{The symbolic mirage.} Provably sound Z3 verification becomes vacuous under self-extraction. We diagnose the underlying mechanism: self-extracted constraints inherit the generating model's distributional prior (symbolic confirmation bias), reducing SICA to majority vote under source-attribution scoring (Observation~1). The pattern holds across nine models and 27 training-free variants (\S\ref{sec:confirmation-bias}, \S\ref{sec:remediation}).
25	
26	\item \textbf{Diagnostic framework.} Three lightweight diagnostics characterize failure modes across all tested conditions within the self-extraction paradigm, with prospective validation on held-out model families; these give practitioners a priori failure-mode diagnosis from a pilot run (\S\ref{sec:diagnostic-framework}).
27	
28	\item \textbf{Cross-architecture escape.} Preliminary evidence ($n{=}6$ generator--verifier pairs) that structurally independent verification can break the bottleneck, with gain governed by an exploratory capability-gap pattern between verifier and generator (\S\ref{sec:cross-arch}).
29	\end{enumerate}
30	
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d6c9da5-d7a7-4d30-a44b-17e237ce32a8",
  "isSidechain": true,
  "promptId": "ed43d146-c225-42c6-832a-351ecc310242",
  "agentId": "af8784ad3137a4fe6",
  "type": "user",
  "uuid": "d51081dd-158e-4188-84b0-5f69c015f128",
  "sourceToolAssistantUUID": "3d6c9da5-d7a7-4d30-a44b-17e237ce32a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T08:19:00.504Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FvwhgqZV2UCRv7HeZSiVyd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d51081dd-158e-4188-84b0-5f69c015f128",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
  "requestId": "req_011CbQrPbs8aZR5cBHPMtGJV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2531ad9a-eb20-411b-8fc9-95b68eb141b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Q5j6zYG7JzuSt1MWtGUgA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33672,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33672,
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

### Tool result

_source line 9 · 2026-05-26T08:19:00.512Z_

<details><summary>↩ Tool result · `toolu_01FvwhgqZV2UCRv7HeZSiVyd`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\looseness=-1
5	\paragraph{Self-consistency and ensemble theory.}
6	Self-consistency (SC) selects the majority answer across chain-of-thought traces \citep{wang2023sc}, with extensions for free-form generation \citep{chen2024usc}, confidence weighting \citep{taubenfeld2025cisc}, diverse prompting \citep{li2023diverse}, and reasoning-aware filtering \citep{wan2024rasc, toh2024notallvotes, kim2026reasc}. SC gains plateau early \citep{loo2025reevaluating, byerly2025selfconsistency}. The Condorcet Jury Theorem \citep{condorcet1785} guarantees majority-vote convergence under independence; ensemble theory \citep{dietterich2000ensemble, krogh1994neural} requires error diversity. \citet{ladha1992correlated} show correlated voters reduce effective ensemble size; our $K_\text{eff}$ adapts Fleiss' $\kappa$ from diversity metrics \citep{kuncheva2003measures, brown2005diversity} to quantify this (\S\ref{sec:pipeline}). \citet{kim2025correlated} demonstrate correlated LLM errors; \citet{kuai2026independent} propose cross-model independence auditing.
7	
8	\looseness=-1
9	\paragraph{Neuro-symbolic reasoning.}
10	Three paradigms exist: \emph{specification-generation} \citep{pan2023logiclm, olausson2023linc, ye2024satlm} and \emph{program-generation} \citep{gao2023pal, chen2023program, lyu2023faithful} formalize before answer generation; \emph{trace-extraction} (this work) operates post-hoc, inheriting confirmation bias (\S\ref{sec:confirmation-bias}). Recent work extends symbolic planning and verified reasoning \citep{ryu2025clover, xu2026dylos, xu2025aristotle, pei2025fover, singh2026verge, luo2025logicagent, miya2025eidoku}; \citet{amonkar2025realitycheck} show formalization quality degrades with complexity; \citet{chan2026position} argue logical soundness alone is unreliable. Prior studies note high formalization error rates but treat them as quality problems; we show they are \emph{systematically biased} toward the model's answer (Observation~1). This reveals a mechanism underlying \citet{huang2024selfcorrect}'s finding that LLMs cannot self-correct without external feedback: we formalize the failure via the $M{\to}T{\to}(A,C)$ generation structure and provide three lightweight diagnostics that predict failure modes before deployment. Our symbolic confirmation bias (SCB) is distinct from CoT-level confirmation bias \citep{wan2025unveiling, turpin2023language, jhaveri2026failing}: CoT bias concerns trace-level faithfulness, while SCB shows the \emph{collection} of self-extracted constraints mirrors the answer distribution even when individual traces are locally faithful.
11	
12	\looseness=-1
13	\paragraph{Verification and test-time scaling.}
14	Scaling test-time compute via additional traces \citep{snell2025scaling}, structured search \citep{yao2023tree}, or extended reasoning \citep{guo2025deepseekr1, qwen2024qwq} faces the same correlation challenge when traces share a model's biases. Self-verification methods, including multi-agent debate \citep{liang2023encouraging, du2023improving}, self-evaluation \citep{xie2023selfevaluation, weng2023selfverification, madaan2023selfrefine, dhuliawala2023chainofverification}, iterative improvement \citep{shinn2023reflexion, zhou2023lats}, tool-augmented critique \citep{gou2024critic}, formal CoT verification \citep{feng2025vericot, chen2025sets}, and multi-agent verification \citep{lifshitz2025mav}, report gains but none tests self-extracted constraints under formal solvers \citep[cf.][]{kamoi2024selfcorrect}; the bottleneck lies in constraint extraction, not verification (\S\ref{sec:confirmation-bias}). Trained verifiers can escape this bottleneck through external reward signals: outcome and process reward models \citep{cobbe2021gsm8k, lightman2024prm, wang2024mathshepherd}, discriminator-guided decoding \citep{khalifa2023grace}, RL-based self-verification \citep{zeng2025s2r}, dual preference optimization \citep{dupo2025}, and execution-based filtering \citep{li2022alphacode, chen2023codet}. These operate outside Observation~1's pipeline and may overcome the information-theoretic bottleneck. The failure modes differ: SICA's bottleneck is extraction fidelity, whereas PRM/ORM's is reward model generalization \citep{wang2024mathshepherd}.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2531ad9a-eb20-411b-8fc9-95b68eb141b5",
  "isSidechain": true,
  "promptId": "ed43d146-c225-42c6-832a-351ecc310242",
  "agentId": "af8784ad3137a4fe6",
  "type": "user",
  "uuid": "e0b5139a-7448-454b-a4e7-ef5572150ca4",
  "sourceToolAssistantUUID": "2531ad9a-eb20-411b-8fc9-95b68eb141b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T08:19:00.974Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E3Eof5a6bce2Vrei34QoQ9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0b5139a-7448-454b-a4e7-ef5572150ca4",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
  "requestId": "req_011CbQrPbs8aZR5cBHPMtGJV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3783d5c9-1d71-4cc5-b806-e7b83435f760",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Q5j6zYG7JzuSt1MWtGUgA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33672,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33672,
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

### Tool result

_source line 11 · 2026-05-26T08:19:00.981Z_

<details><summary>↩ Tool result · `toolu_01E3Eof5a6bce2Vrei34QoQ9`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	\label{sec:pipeline}
4	\label{sec:condorcet}
5	\label{sec:effective-k}
6	
7	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. Under correlated traces (Fleiss' $\kappa$ \citep{fleiss1971kappa}), the effective ensemble size $K_\text{eff}$ is
8	\begin{equation}
9	\label{eq:effk}
10	K_{\text{eff}} = K \,/\, [1 + (K{-}1) \cdot \kappa]
11	\end{equation}
12	(following \citet{ladha1992correlated}). Intuitively, $K_\text{eff}$ measures how many effectively independent votes $K$ correlated traces contribute; e.g., $K{=}12$ traces with $\kappa{=}0.69$ yield $K_\text{eff} \approx 1.4$, meaning twelve correlated traces carry no more independent information than 1.4 uncorrelated ones. This motivates constraint-based aggregation.
13	
14	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\ref{fig:pipeline}).
15	
16	\begin{table*}[t]
17	\centering
18	\small
19	\caption{SICA vs.\ SC across all non-degenerate self-extraction conditions (sorted by SC). Two conditions show significant degradation after BH correction ($m{=}6$ confirmatory; remaining exploratory); no condition shows a significant gain. $\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \textbf{bold}: $p < 0.05$; {*}\,BH adj.\ $p = 0.042$; $^{3s}$\,3-seed aggregate; $^{4s}$\,4-seed confirmatory aggregate; $^\dagger$\,4-seed replication in Table~\ref{tab:multi-seed} (unmarked: single-seed exploratory; s123/s456/s789 are individual seed runs). All conditions have McNemar power $< 80\%$ for $|\Delta| = 2$\,pp (Appendix~\ref{app:power}). Degenerate conditions ($C_0 < 5\%$: QwQ-32B AIME$^\ddagger$ $n{=}22$, Qwen2.5-14B GSM8K$^\ddagger$ $n{=}30$) yield $\Delta = 0$ and are reported separately in Appendix~\ref{app:oracle}. $^\ddagger$Pilot conditions ($n{\leq}30$); included for coverage, not confirmatory evidence. Single-seed conditions use seed 123 (not selected post hoc).}
20	\label{tab:main_results}
21	\begin{tabular}{@{}llrrrrl@{}}
22	\toprule
23	Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & $p$ \\
24	\midrule
25	\multicolumn{7}{l}{\textit{Type C: error amplification (SC $\leq$ 40\%)}} \\
26	Mistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\mathbf{-2.83}$ & 0.014{*} \\
27	\midrule
28	\multicolumn{7}{l}{\textit{Intermediate SC (SC $\sim$50--60\%, Mistral-7B only)}} \\
29	Mistral-7B & LogiQA & 200 & 50.00 & 51.50 & $+$1.50 & 0.581 \\
30	Mistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\
31	Mistral-7B$^{3s}$ & FOLIO & 204 & 56.53 & 56.70 & $+$0.16 & 1.000 \\
32	Mistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\
33	Mistral-7B & FOLIO (s789) & 204 & 59.31 & 56.86 & $-$2.45 & 0.267 \\
34	\midrule
35	\multicolumn{7}{l}{\textit{Type A: confirmation bias (SC $\geq$ 60\%)}} \\
36	LLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\
37	LLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\
38	\addlinespace
39	Qwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\
40	Qwen2.5-14B & PW-D5 & 600 & 74.00 & 71.50 & $\mathbf{-2.50}$ & 0.011{*} \\
41	Qwen2.5-14B$^{4s}$ & FOLIO & 204 & 75.01 & 73.78 & $-$1.24 & 1.000 \\
42	Qwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\
43	Qwen2.5-14B & LogiQA & 200 & 79.00 & 78.00 & $-$1.00 & 0.625 \\
44	\addlinespace
45	Qwen3-14B & FOLIO & 204 & 83.33 & 84.80 & $+$1.47 & 1.000 \\
46	Qwen3-14B$^\dagger$ & PW-D5 & 600 & 85.83 & 85.67 & $-$0.17 & 1.000 \\
47	Qwen3-14B (think) & FOLIO & 204 & 86.27 & 86.76 & $+$0.49 & 1.000 \\
48	\bottomrule
49	\end{tabular}
50	\end{table*}
51	
52	\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\{t_1, \ldots, t_K\}$ at temperature $T = 0.7$. Each trace $t_i$ yields answer $a_i$.
53	
54	\looseness=-1
55	\paragraph{Constraint extraction.}\label{sec:constraint-extraction} The same LLM extracts logical constraints from each trace at $T_{\text{ext}} = 0.3$. The extraction prompt requests JSON output with constraint type, expression, and Z3-compatible formula (Appendix~\ref{app:prompts}); in practice, 99.0\% of extracted constraints are propositional at the Z3 level, with only 1.0\% using true quantifiers. The \emph{extraction rate} is the fraction of traces yielding at least one parseable constraint.
56	
57	\paragraph{Deduplication and MAX-SAT.} Constraints are deduplicated by syntactic equivalence (global average deduplication ratio: 46.0\%); each unique constraint $c_m$ receives weight $w_m$ equal to the number of source traces. The objective finds the largest-weight satisfiable subset:
58	\begin{equation}
59	\label{eq:maxsat}
60	\mathcal{C}^* = \arg\max_{\mathcal{S} \subseteq \mathcal{C}} \sum_{c \in \mathcal{S}} w_c \quad \text{s.t.} \quad \mathcal{S} \text{ is satisfiable.}
61	\end{equation}
62	Z3 \citep{demoura2008z3} solves this with a 10-second timeout (Algorithm~\ref{alg:maxsat}; Appendix~\ref{app:z3-pseudocode}). Answer assertion constraints ($\texttt{answer\_a} == \texttt{True}$, weight 1) ensure every candidate receives a nonzero base score; SICA is thus a strict generalization of SC.
63	
64	\paragraph{Scoring.} Let $\mathcal{C}^{\setminus} = \mathcal{C} \setminus \mathcal{C}^*$. Each candidate $a$ is scored by:
65	\begin{equation}
66	\label{eq:score}
67	\text{score}(a) = \sum_{c \in \mathcal{C}^*} w_c \cdot \sigma(c, a) - \alpha \sum_{c \in \mathcal{C}^{\setminus}} w_c \cdot \sigma(c, a),
68	\end{equation}
69	where $\sigma(c, a) = 1$ if $c$ was extracted from any trace producing answer $a$, and $\alpha = 0.5$. The selected answer is $a^* = \arg\max_{a} \text{score}(a)$.
70	
71	\paragraph{Degeneration condition.} If self-extracted constraints are coupled to their source answer, MAX-SAT retains nearly all ($|\mathcal{C}^{\setminus}| \approx 0$), and scoring degenerates to:
72	\begin{equation}
73	\label{eq:degenerate}
74	\text{score}(a) \approx \sum_{\substack{c \in \mathcal{C}^* \\ \text{source}(c) \to a}} w_c,
75	\end{equation}
76	equivalent to majority voting. We show in \S\ref{sec:confirmation-bias} that this degeneration occurs in practice.
77	
78	\paragraph{The $C_0$ diagnostic.} The multi-candidate rate $C_0 = |\{q : |\mathcal{A}(q)| > 1\}| / |\mathcal{Q}|$ is a lightweight diagnostic computable from pilot traces: $C_0 < 5\%$ means SICA reduces to SC. $\alpha = 0.5$ is not critical (${\pm}0.49$\,pp across $\alpha \in [0, 1]$).
79	
80	\paragraph{Bias ratio.} We quantify extraction bias via the \emph{bias ratio} (BR):
81	\begin{equation}\label{eq:mirage}
82	\text{BR}(M,T) = \frac{P(c \text{ supports } a_M \mid a_M \neq a^*)}{P(c \text{ supports } a^* \mid a_M \neq a^*)},
83	\end{equation}
84	where $c$ is a self-extracted constraint, $a_M$ the model's majority answer, and $a^*$ the ground truth. BR quantifies the degree of extraction degeneration under source-attribution scoring (Observation~1): values above 1 reflect the trace-count base rate inherent to source-attributed constraints. $\text{BR} = 1$ indicates no coupling beyond chance. We validate this metric empirically in \S\ref{sec:confirmation-bias}.
85	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3783d5c9-1d71-4cc5-b806-e7b83435f760",
  "isSidechain": true,
  "promptId": "ed43d146-c225-42c6-832a-351ecc310242",
  "agentId": "af8784ad3137a4fe6",
  "type": "user",
  "uuid": "16b7b0c0-f7cb-4c57-9d05-4ef04a8365bd",
  "sourceToolAssistantUUID": "3783d5c9-1d71-4cc5-b806-e7b83435f760",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T08:19:01.256Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GDKmZohkdQkePo1a1UYWPz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16b7b0c0-f7cb-4c57-9d05-4ef04a8365bd",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
  "requestId": "req_011CbQrPbs8aZR5cBHPMtGJV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab9ea322-78ba-46ee-9428-4a85244f7210",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Q5j6zYG7JzuSt1MWtGUgA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33672,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33672,
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

### Tool result

_source line 13 · 2026-05-26T08:19:01.264Z_

<details><summary>↩ Tool result · `toolu_01GDKmZohkdQkePo1a1UYWPz`</summary>

```text
1	\section{Experiments}
2	\label{sec:results}
3	\label{sec:main-results}
4	
5	\begin{figure}[t]
6	\centering
7	\includegraphics[width=\columnwidth]{f2_regime_scatter_v2}
8	\caption{SICA $\Delta$ (pp) vs.\ SC baseline. Color: model family; shape: dataset (\scalebox{0.7}{$\blacksquare$}\,PW, \scalebox{0.7}{$\blacktriangle$}\,FOLIO, \scalebox{0.7}{$\bullet$}\,LogiQA). Circled: significant ($p < .05$). Grey band: $\pm 2$\,pp equivalence zone. Three regimes emerge: Type~C (error amplification), intermediate, and Type~A (confirmation bias).}
9	\label{fig:regime-scatter}
10	\end{figure}
11	
12	\subsection{Experimental Setup}
13	\label{sec:exp-setup}
14	
15	\looseness=-1
16	\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen3-14B (non-thinking mode)~\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\citep{dubey2024llama3}, and QwQ-32B~\citep{qwen2024qwq} (7B--32B). We also evaluate the universality of symbolic confirmation bias on six additional models: gpt-4o uses self-extraction via API; four frontier models (gpt-4.1, gpt-5.5, o3, Gemini-2.5-Pro) use cross-model extraction where Mistral-7B extracts constraints from target traces; DeepSeek-R1-Distill-Qwen-8B likewise uses Mistral-7B cross-extraction (Table~\ref{tab:frontier-scb}).
17	
18	\paragraph{Datasets.} FOLIO~\citep{han2022folio} ($n{=}204$, gold logical annotations), ProofWriter depth-5~\citep{tafjord2021proofwriter} ($n{=}600$), LogiQA~\citep{liu2020logiqa} ($n{=}200$), StrategyQA~\citep{geva2021strategyqa} ($n{=}200$). GSM8K ($n{=}30$) and AIME 2024 ($n{=}22$) probe the degenerate regime ($C_0 < 5\%$).
19	
20	\paragraph{Parameters.} $K{=}12$ traces at $T{=}0.7$, extraction at $T_{\text{ext}}{=}0.3$, $\alpha{=}0.5$, Z3 timeout 10s (K-sensitivity and extraction-temperature analysis in Appendix~\ref{app:sensitivity}). McNemar exact test ($\alpha{=}0.05$); 95\% bootstrap CIs ($10{,}000$ resamples; Appendix~\ref{app:bootstrap}) for $n \geq 200$. SICA incurs $4.5{\times}$ SC wall-clock; extraction accounts for 76\% of overhead.
21	
22	\subsection{Main Results}
23	
24	\looseness=-1 Table~\ref{tab:main_results} reports accuracy across all non-degenerate self-extraction conditions sorted by SC baseline. Two confirmatory conditions show significant degradation after Benjamini--Hochberg (BH) FDR control ($m{=}6$; multi-seed aggregates and extensions are exploratory): Mistral-7B on ProofWriter ($-2.83$\,pp, raw $p = 0.014$, adj.\ $p = 0.042$) and Qwen2.5-14B on ProofWriter ($-2.50$\,pp, raw $p = 0.011$, adj.\ $p = 0.042$). No condition shows a significant positive effect. An aggregate sign test yields 8 positive and 7 negative $\Delta$ values ($p = 1.00$, two-sided). When SICA and SC disagree, SC selects the correct answer $2.6\times$ more often (139 vs.\ 53 across conditions); constraint-based reweighting thus introduces noise rather than corrective signal (representative cases in Appendix~\ref{app:case-studies}; Appendix~\ref{app:subpopulation}).
25	
26	\begin{figure}[t]
27	\centering
28	\includegraphics[width=\columnwidth]{figures/fig3_causal_dag_v12.pdf}
29	\caption{Causal DAG of the self-extraction pipeline. Traces $T$ produce both answers $A$ and constraints $C$; under degeneration (Observation~1), $C$ is determined by $A$ (dashed arrow), yielding $I(C;Y) \leq I(A;Y)$.}
30	\label{fig:causal-dag}
31	\end{figure}
32	
33	\looseness=-1 Figure~\ref{fig:regime-scatter} reveals regime structure across SC baselines. Three regimes emerge: Type~C (SC $\leq 40\%$), where low accuracy causes error amplification; an intermediate band (50--60\%), containing the only positive trends; and Type~A (SC $\geq 60\%$), where symbolic confirmation bias dominates. Fleiss' $\kappa$ ranges from 0.19 to 0.82, yielding $K_{\text{eff}} = 1.20\text{--}3.94$ at $K = 12$ (Table~\ref{tab:independence}; Appendix~\ref{app:cross-model-kappa}). Seed-level noise is substantial: across three Mistral-7B seeds, $\Delta$ ranges from $+2.94$ to $-2.45$\,pp despite $\kappa \in [0.45, 0.46]$. We trace the mechanism in \S\ref{sec:analysis}.
34	
35	\looseness=-1 We use TOST equivalence tests \citep{lakens2017equivalence} with margin $\pm 2$\,pp, justified on four grounds: (1)~on FOLIO ($n{=}204$), $\pm$2\,pp corresponds to ${\sim}$4 problems, near single-item influence; (2)~multi-seed SC variability $\sigma_{\text{SC}} = 1.67$--$2.51$\,pp on FOLIO, with $\sigma_\Delta$ up to 2.70\,pp (Table~\ref{tab:multi-seed}), placing $\pm$2\,pp within natural noise; (3)~the observed $|\Delta|$ median across 11 conditions is 1.47\,pp, so $\pm$2\,pp captures the central tendency; (4)~sensitivity analysis confirms $\pm$2\,pp as the narrowest discriminating window ($\pm$1\,pp: zero conditions pass; $\pm$3\,pp: all pass; Appendix~\ref{app:tost}). Four of 11 conditions pass TOST equivalence (minimum detectable effect (MDE) $\leq 2$\,pp); the remaining seven are underpowered (MDE $4.6$--$4.8$\,pp) but provide consistent directional evidence ($|\Delta| \leq 4.41$\,pp, none significant; Appendix~\ref{app:power}). Multi-seed replication: mean $\Delta = +0.16 \pm 2.70$\,pp across three Mistral-7B seeds (Table~\ref{tab:multi-seed}); four Qwen2.5-14B seeds yield $\Delta \in [0.00, -2.01]$\,pp; four Qwen3-14B seeds yield $\Delta = +0.92 \pm 1.14$\,pp (n.s.; Appendix~\ref{app:single-trace}). Oracle controls confirm the MAX-SAT mechanism is sound ($+29.90$/$+13.73$\,pp FOLIO, $+17.17$\,pp ProofWriter; $p < 0.001$), yet self-extraction captures only ${\sim}12\%$ of this ceiling (Appendix~\ref{app:oracle}; Appendix~\ref{app:pw-oracle-subtype}).
36	
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab9ea322-78ba-46ee-9428-4a85244f7210",
  "isSidechain": true,
  "promptId": "ed43d146-c225-42c6-832a-351ecc310242",
  "agentId": "af8784ad3137a4fe6",
  "type": "user",
  "uuid": "6e8bbb75-b999-4f5d-877e-a7c382f9d364",
  "sourceToolAssistantUUID": "ab9ea322-78ba-46ee-9428-4a85244f7210",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T08:19:05.903Z_

<details open><summary>🔧 Tool call — Read · `toolu_0166cs4gSuGW5fDQECT31JzE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
  "offset": 37
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e8bbb75-b999-4f5d-877e-a7c382f9d364",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
  "requestId": "req_011CbQrQ2zjT3hZR5m4McRNk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "766c11b2-c14a-4742-b2a6-8285442dfac7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLyRaGoDMveQ6TZKBZDDgT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9620,
      "cache_read_input_tokens": 33672,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9620,
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

_source line 15 · 2026-05-26T08:19:05.911Z_

<details><summary>↩ Tool result · `toolu_0166cs4gSuGW5fDQECT31JzE`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (37). The file has 37 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "766c11b2-c14a-4742-b2a6-8285442dfac7",
  "isSidechain": true,
  "promptId": "ed43d146-c225-42c6-832a-351ecc310242",
  "agentId": "af8784ad3137a4fe6",
  "type": "user",
  "uuid": "df1cb31f-2c66-41de-ab58-1da3d0e37bd9",
  "sourceToolAssistantUUID": "766c11b2-c14a-4742-b2a6-8285442dfac7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-26T08:19:06.440Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TRg33btWZyGFNVjSLFCnqm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df1cb31f-2c66-41de-ab58-1da3d0e37bd9",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
  "requestId": "req_011CbQrQ2zjT3hZR5m4McRNk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "acd069f3-8e98-48ce-8620-f5c54708b125",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLyRaGoDMveQ6TZKBZDDgT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9620,
      "cache_read_input_tokens": 33672,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9620,
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

_source line 17 · 2026-05-26T08:19:06.450Z_

<details><summary>↩ Tool result · `toolu_01TRg33btWZyGFNVjSLFCnqm`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Symbolic Confirmation Bias}
5	\label{sec:confirmation-bias}
6	
7	\looseness=-1 Self-extracted constraints systematically align with the model's majority answer. On Mistral-7B FOLIO, when SICA errs, 83.3\% of constraints support the incorrect answer (bias ratio $4.97\times$; Table~\ref{tab:cross-model-bias}), and 94\% of errors overlap with SC. Z3 rejects only 3.4\% of constraints, and MAX-SAT produces answers identical to count-only aggregation on ${\geq}99\%$ of problems (Table~\ref{tab:alpha-ablation}); the formal verification layer is thus vacuous (Eq.~\ref{eq:degenerate}). A permutation test confirms BR reflects trace-count geometry, not extraction bias (Appendix~\ref{app:br-permutation}); controls rule out answer leakage (Appendix~\ref{app:per-trace-separation}).
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Symbolic confirmation bias across nine models on FOLIO ($n{=}204$). BR: mean per-problem bias ratio. All models exhibit $\text{BR} > 1$. Ext.: $^a$self-extraction; $^b$cross-model (Mistral-7B extracts FOL from target traces). $^*$Interim ($n{=}95$). $^\dagger$$n{=}196$ (8 API failures excluded). $^\ddagger$$n{=}161$ (43 API failures excluded).}
13	\label{tab:frontier-scb}
14	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}llrrrr@{}}
15	\toprule
16	Model & Ext. & SC (\%) & $n_\text{err}$ & BR & $\Delta$ (pp) \\
17	\midrule
18	Mistral-7B & $^a$ & 55.88 & 90 & 4.97 & 0.00 \\
19	LLaMA-3.1-8B & $^a$ & --- & --- & 3.87 & --- \\
20	Qwen2.5-14B & $^a$ & 75.98 & 49 & 3.93 & $-$0.49 \\
21	\addlinespace
22	R1-Distill-8B & $^b$ & 74.51 & 52 & 2.92 & $+$2.45 \\
23	gpt-4o$^\ddagger$ & $^a$ & 73.91 & 42 & 2.94 & $-$1.86 \\
24	gpt-4.1 & $^b$ & 82.84 & 35 & 2.70 & $-$1.47 \\
25	gpt-5.5 & $^b$ & 84.31 & 32 & 3.48 & $+$0.49 \\
26	o3$^\dagger$ & $^b$ & 82.65 & 34 & 1.66 & 0.00 \\
27	Gemini-2.5-Pro$^*$ & $^b$ & 87.37 & 12 & 2.79 & $-$1.05 \\
28	\bottomrule
29	\end{tabular}}
30	\end{table}
31	
32	\looseness=-1 The pattern generalizes beyond locally-run models. Table~\ref{tab:frontier-scb} reports SCB across nine models spanning 7B open-source to frontier closed-source, all exhibiting $\text{BR} > 1$ ($1.66$--$4.97\times$). Open-source models use self-extraction; frontier models use cross-model extraction (Mistral-7B extracts FOL from target traces). The bias also holds across all cells of a $2{\times}2$ generator${\times}$extractor matrix (Appendix~\ref{app:2x2}).
33	
34	\smallskip\noindent
35	\textbf{Observation 1} \textit{(Argmax Preservation).}\;%
36	Let $t_1, \ldots, t_K \overset{\mathrm{i.i.d.}}{\sim} P_M(\cdot \mid q)$ with trace-determined answers $a_i = h(t_i)$ and $n_a = |\{i : a_i = a\}|$.
37	Under (i)~the degeneration condition $|\mathcal{C}^{\setminus}| \approx 0$ (Eq.~\ref{eq:degenerate}), (ii)~source-attribution scoring where $\sigma(c,a) {=} 1$ iff $c$ originates from a trace producing $a$ (Eq.~\ref{eq:score}), and (iii)~approximately uniform constraint yield per trace, SICA reduces to majority vote: $\arg\max_a \operatorname{score}(a) = \arg\max_a n_a$.
38	
39	\smallskip\noindent
40	\textit{Empirical support.}\;%
41	Z3 rejection rate $|\mathcal{C}^{\setminus}|/|\mathcal{C}| \approx 0.034$ confirms $|\mathcal{C}^{\setminus}| \approx 0$. Per-trace yield averages $5.6$--$6.0$ constraints across answer groups (CV${=}0.26$; Appendix~\ref{app:yield-cv}); weight is thus proportional to $n_a$. SICA and majority vote agree on 96.1\% of problems for Qwen2.5-14B ($n{=}804$; Table~\ref{tab:ablation}) and over 90\% across all conditions. Per-trace separation analysis confirms the extraction function is neutral (constraint density and quality are balanced across answer groups), and source-attribution scoring is the sole mechanism transmitting CoT correlation into verification (Appendix~\ref{app:per-trace-separation}).
42	
43	\looseness=-1 A representative discordant case illustrates the mechanism. On a ProofWriter chaining problem (White$\to$Round$\to$Young), SC correctly breaks a 6:6 vote tie to the gold label. SICA extracts 17 constraints; MAX-SAT excludes 2 that capture correct intermediate derivations present \emph{only} in correct-answer traces, penalizing the complete reasoning chain and selecting the wrong answer. Of 31 discordant problems ($n{=}804$), all occur at exact or near vote ties (entropy $\geq 0.92$), and constraint exclusion tips the balance in either direction with no systematic corrective tendency (Appendix~\ref{app:case-studies}).
44	
45	\begin{figure}[t]
46	\centering
47	\includegraphics[width=0.85\columnwidth]{figures/fig3_process_kappa_scatter.pdf}
48	\caption{Answer agreement vs.\ CoT cosine similarity (Mistral-7B, FOLIO, $n{=}204$). Flat regression ($r = -0.06$, $p = 0.36$): process and answer independence are uncorrelated.}
49	\label{fig:process-kappa}
50	\end{figure}
51	
52	\label{sec:process-kappa}
53	\looseness=-1 The $M{\to}T{\to}(A,C)$ generation structure provides empirical motivation \citep{cover2006elements}: under degeneration (Observation~1), constraints carry no more task-relevant information than answers alone, i.e., $I(C;\, Y) \leq I(A;\, Y)$ (Figure~\ref{fig:causal-dag}). Process-level overlap compounds the bottleneck: mean reasoning similarity reaches $0.69$, far exceeding answer-level $\kappa$ ($0.41$--$0.51$; Figure~\ref{fig:process-kappa}), and SICA gain decreases monotonically with process similarity ($\rho = -1.0$, $p = 0.0083$; Appendix~\ref{app:cil}).
54	
55	\subsection{Why Remediation Fails}
56	\label{sec:remediation}
57	\label{sec:interventions}
58	
59	\looseness=-1 All 27 training-free variants spanning four categories produce neutral-to-negative results (Figure~\ref{fig:kappa-accuracy}; Appendices~\ref{app:extraction}--\ref{app:entropy}); a persistent independence--accuracy trade-off emerges. Diversity-seeking strategies shift $K_\text{eff}$ by $< 0.5$; constraint-level interventions leave degeneration intact; debate ($\kappa = 0.15$, $\Delta = -18.63$\,pp) breaks correlation but collapses accuracy (Appendix~\ref{app:error-categorization}); cross-model extraction achieves the lowest non-destructive $\kappa$ (${\approx}0.40$--$0.47$) but remains above the independence threshold ($+0.49$\,pp, n.s.; Appendix~\ref{app:intervention-individual}).
60	
61	\looseness=-1 The root cause is \emph{variable isolation}: each trace generates constraints with its own variable names, so Z3 treats identically-intended propositions from different traces as unrelated symbols. Among cross-answer constraint pairs, 56.4\% share zero Z3 variables, making them trivially jointly satisfiable. Consequently, although 91.8\% of constraints are technically discriminative (producing different satisfiability outcomes for different candidate answers), this discrimination merely mirrors the model's answer distribution rather than providing independent corrective signal (Appendix~\ref{app:extraction}).
62	
63	\begin{table}[t]
64	\centering
65	\small
66	\caption{Cross-generator NLI escape with DeBERTa-large-mnli verifier (55.00\% standalone, ProofWriter $n{=}600$). Combo gain decreases monotonically with generator capability.}
67	\label{tab:cross_generator_nli}
68	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}llcccc@{}}
69	\toprule
70	Generator & Family & SC & Gap & Combo $\Delta$ ($w{=}3$) & $p$ \\
71	\midrule
72	Mistral-7B & Mistral & 39.33\% & $+$15.67 & $+$6.67\,pp & $<$0.001 \\
73	LLaMA-3.1-8B & LLaMA & 72.50\% & $-$17.50 & $+$0.83\,pp & 0.665 \\
74	Qwen2.5-14B & Qwen & 74.00\% & $-$19.00 & $+$0.67\,pp & 0.503 \\
75	Qwen3-14B & Qwen & 85.83\% & $-$30.83 & $+$0.50\,pp & 0.453 \\
76	\bottomrule
77	\end{tabular}}
78	\end{table}
79	
80	\subsection{Diagnostic Framework}
81	\label{sec:diagnostic-framework}
82	\label{sec:diagnostics}
83	
84	\looseness=-1 Three lightweight diagnostics predict the outcome of any self-extraction-based aggregation from a $K{=}12$ pilot run: (1)~degenerate-regime indicator $C_0 < 5\%$ (SICA reduces to SC); (2)~diversity floor $K_\text{eff} \leq 1.30$ (insufficient vote diversity); (3)~bias ratio BR combined with SC regime. These boundaries correctly characterize failure modes across all 60 tested conditions within the self-extraction paradigm (Appendix~\ref{app:failure-modes}).
85	
86	\looseness=-1 Three distinct failure modes correspond to these regimes. \textbf{Type~A} (SC $\geq 60\%$): strong models produce consistent traces whose constraints mirror the answer distribution; MAX-SAT excludes few clauses ($|\mathcal{C}^{\setminus}| \approx 0$) and scoring degenerates to weighted vote counting (Eq.~\ref{eq:degenerate}). \textbf{Type~C} (SC $\leq 40\%$): the majority of traces reach incorrect answers; constraints extracted from wrong traces encode incorrect reasoning as formal rules, and Z3 preferentially satisfies these wrong constraints, amplifying errors ($-2.83$\,pp for Mistral-7B on ProofWriter). An intermediate band (40--60\% SC) contains the only positive trends, but none reach significance. Entropy decomposition confirms this structure: on low-entropy problems (majority count $\geq 9/12$), $\Delta \approx 0$\,pp uniformly---constraints carry no information beyond the majority vote. On high-entropy problems (majority $\leq 8$), the effect direction depends on the SC regime: intermediate-SC yields $\Delta$ up to $+12.8$\,pp, while Type~A and Type~C produce negative effects ($-8.2$ and $-4.9$\,pp; Appendix~\ref{app:entropy}).
87	
88	\looseness=-1 Decision boundaries were derived from Mistral-7B and Qwen2.5-14B and validated prospectively on held-out generators (LLaMA-3.1-8B, Qwen3-14B), correctly predicting Type~A bias ($\Delta = -4.41$\,pp) and non-significance ($\Delta \leq +1.47$\,pp). Conversely, when diagnostics detect sufficient capability gap (\S\ref{sec:cross-arch}), the framework correctly predicts positive gain ($+6.67$\,pp for Mistral-7B on ProofWriter). The three diagnostics thus enable practitioners to rule out self-extraction pipelines before full-scale deployment (Appendix~\ref{app:diagnostic-toolkit}).
89	
90	\subsection{Cross-Architecture Escape}
91	\label{sec:cross-arch}
92	
93	\looseness=-1 No training-free self-extraction method escapes the distributional prior (\S\ref{sec:remediation}). We test whether a structurally independent verifier can break the bottleneck using DeBERTa-large \citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \citep{williams2018mnli} for natural language inference (NLI). Each NLI-supporting vote counts $w$ times alongside SC's $K$ votes.
94	
95	\looseness=-1 DeBERTa alone achieves 49.51\% on FOLIO and 55.00\% on ProofWriter. Combo $w{=}3$ yields $+6.67$\,pp on ProofWriter for Mistral-7B ($p < 0.001$, significant after BH correction) and $+2.94$\,pp on FOLIO (n.s.); all generators with SC $\geq 72\%$ show no significant improvement ($\Delta \leq +1.47$\,pp). Same-model SICA \emph{degrades} ProofWriter ($-2.83$\,pp; Table~\ref{tab:main_results}); corrective signal must therefore originate outside the model's distribution. The escape generalizes across NLI architectures: three verifiers (DeBERTa, RoBERTa \citep{liu2019roberta}, BART \citep{lewis2020bart}, all fine-tuned on MultiNLI) produce significant gains at $w{=}3$ ($+6.67$, $+4.17$, $+5.17$\,pp; 10 of 15 verifier${\times}$weight conditions survive BH correction; Appendix~\ref{app:multi-nli}), confirming that structural independence, not model-specific properties, drives the effect.
96	
97	\begin{figure}[t]
98	\centering
99	\includegraphics[width=0.85\columnwidth]{figures/capability_gap_scatter}
100	\caption{Combo gain vs.\ capability gap (verifier standalone $-$ generator SC) at $w{=}3$ across three NLI architectures. Significant gains occur only when the generator falls below the verifier's standalone accuracy. Stars: domain-adapted DeBERTa (Appendix~\ref{app:finetuned-nli}).}
101	\label{fig:capability-gap}
102	\end{figure}
103	
104	\looseness=-1 Across 108 conditions, gain decreases monotonically with generator accuracy (Table~\ref{tab:cross_generator_nli}; Figure~\ref{fig:capability-gap}), a preliminary \emph{capability-gap pattern} ($\rho = 1.0$, $p = 0.003$; exploratory, $n{=}6$). Fine-tuning extends gains to generators with SC up to ${\sim}$72\% (Appendix~\ref{app:finetuned-nli}). Cross-model LLM voting degrades strong generators while NLI never does; structural independence drives the escape (Appendices~\ref{app:cross-model-ablation},~\ref{app:drc}).
105	
106	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acd069f3-8e98-48ce-8620-f5c54708b125",
  "isSidechain": true,
  "promptId": "ed43d146-c225-42c6-832a-351ecc310242",
  "agentId": "af8784ad3137a4fe6",
  "type": "user",
  "uuid": "3918c0b0-df8a-494c-8d2d-d6d18f270857",
  "sourceToolAssistantUUID": "acd069f3-8e98-48ce-8620-f5c54708b125",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-26T08:19:06.772Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FANJmSWDSUDV2n8LqBkrJf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3918c0b0-df8a-494c-8d2d-d6d18f270857",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
  "requestId": "req_011CbQrQ2zjT3hZR5m4McRNk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6c62244-81ad-4032-8b30-b550f0240860",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLyRaGoDMveQ6TZKBZDDgT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9620,
      "cache_read_input_tokens": 33672,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9620
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 250,
          "cache_read_input_tokens": 33672,
          "cache_creation_input_tokens": 9620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9620,
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

_source line 19 · 2026-05-26T08:19:06.781Z_

<details><summary>↩ Tool result · `toolu_01FANJmSWDSUDV2n8LqBkrJf`</summary>

```text
1	% Cross-architecture escape content merged into analysis.tex §5.4
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6c62244-81ad-4032-8b30-b550f0240860",
  "isSidechain": true,
  "promptId": "ed43d146-c225-42c6-832a-351ecc310242",
  "agentId": "af8784ad3137a4fe6",
  "type": "user",
  "uuid": "f710a251-9f8c-4dab-adcc-f92461f0f583",
  "sourceToolAssistantUUID": "d6c62244-81ad-4032-8b30-b550f0240860",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-26T08:19:10.980Z_

<details open><summary>🔧 Tool call — Read · `toolu_019BHrRJbkFYapBvFzHNQsYe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f710a251-9f8c-4dab-adcc-f92461f0f583",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
  "requestId": "req_011CbQrQSKRtWrJgLXWUXvww",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f5812da-d97e-4dae-8d14-5ffd70bae829",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBioEinniowEdni6MyUKT5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4848,
      "cache_read_input_tokens": 43292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4848,
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

_source line 21 · 2026-05-26T08:19:10.989Z_

<details><summary>↩ Tool result · `toolu_019BHrRJbkFYapBvFzHNQsYe`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	\label{sec:conclusion}
4	
5	\looseness=-1
6	Formal verification's value depends on the \emph{independence} of its inputs, not the soundness of its logic. SICA reduces to majority vote under source-attribution scoring (Observation~1), and 27 training-free variants fail to escape; symbolic confirmation bias holds across nine models (7B to frontier). Three lightweight diagnostics predict failure from a $K{=}12$ pilot (\S\ref{sec:diagnostic-framework}).
7	
8	\looseness=-1
9	For the broader neuro-symbolic community, our results expose a structural limitation of self-extraction pipelines: when the same model generates both reasoning and formal constraints, the symbolic layer inherits the model's distributional prior rather than providing an independent check. This limitation is not specific to logical constraint extraction; it applies to any self-verification paradigm where the verifier shares the generator's knowledge boundary \citep{huang2024selfcorrect}.
10	
11	\begin{figure}[t]
12	\centering
13	\includegraphics[width=\columnwidth]{figures/f6_kappa_accuracy_scatter}
14	\caption{Independence--accuracy trade-off across 27 remediation strategies on FOLIO ($n = 204$). Dashed line: Mistral-7B SC baseline.}
15	\label{fig:kappa-accuracy}
16	\end{figure}
17	
18	\looseness=-1
19	We formalize the link between these findings via the \emph{Conditional Correction Ratio}: $\text{CCR}(V, G) = \log \frac{P(V \text{ correct} \mid G \text{ wrong})}{P(V \text{ correct} \mid G \text{ correct})}$. All same-model SICA conditions yield $\text{CCR} < 0$ (shared bias), while cross-architecture NLI pairs achieve $\text{CCR} > 0$ (preferential error correction); CCR correlates with combo gain ($\rho = 0.84$, $p = 0.014$; Appendix~\ref{app:cil}).
20	
21	\looseness=-1
22	Cross-architecture verification escapes only when the verifier exceeds generator accuracy (\S\ref{sec:cross-arch}); this points to \emph{architectural diversity} over scale as the key design principle. Trained verifiers (PRM \citep{lightman2024prm,wang2024mathshepherd}, ORM \citep{cobbe2021gsm8k}) succeed precisely because they break the $M{\to}T{\to}(A,C)$ generation structure with independently supervised signal; our NLI escape instantiates this principle without task-specific training ($+6.67$\,pp). For test-time compute scaling \citep{snell2025scaling}, our findings imply that allocating additional inference budget to self-consistent sampling yields diminishing returns once $K_\text{eff}$ saturates; redirecting compute toward structurally independent verification offers a more efficient path. Lightweight trained verification is a natural next step (Appendix~\ref{app:extended-discussion}).
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f5812da-d97e-4dae-8d14-5ffd70bae829",
  "isSidechain": true,
  "promptId": "ed43d146-c225-42c6-832a-351ecc310242",
  "agentId": "af8784ad3137a4fe6",
  "type": "user",
  "uuid": "56441d4f-0765-458c-b5a1-5b9f7b99bf6c",
  "sourceToolAssistantUUID": "4f5812da-d97e-4dae-8d14-5ffd70bae829",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-26T08:19:12.300Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WreW7np6rYhKf23VXxY1oV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56441d4f-0765-458c-b5a1-5b9f7b99bf6c",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
  "requestId": "req_011CbQrQSKRtWrJgLXWUXvww",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7bb97c87-72f8-4bad-b8c6-5f03eeec55c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBioEinniowEdni6MyUKT5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4848,
      "cache_read_input_tokens": 43292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4848,
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

### Tool call

_source line 23 · 2026-05-26T08:19:12.308Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C31S2fP431fBuppZT2rvYb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bb97c87-72f8-4bad-b8c6-5f03eeec55c1",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
  "requestId": "req_011CbQrQSKRtWrJgLXWUXvww",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cad7e16b-2a93-45c9-9210-2784eb95f286",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBioEinniowEdni6MyUKT5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4848,
      "cache_read_input_tokens": 43292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4848,
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

_source line 24 · 2026-05-26T08:19:12.314Z_

<details><summary>↩ Tool result · `toolu_01WreW7np6rYhKf23VXxY1oV`</summary>

```text
1	\looseness=-1 Our locally-run models range from 7B to 32B; frontier coverage relies on cross-model extraction, so we cannot confirm identical SCB patterns at frontier scale. All benchmarks are English logical reasoning; FOLIO and ProofWriter represent a best-case for symbolic verification, and the observed bias ratios likely represent a lower bound on SCB in less structured domains. We do not evaluate trained extractors or few-shot extraction, which could potentially break the self-extraction bound by introducing external signal. Our separation of SCB from trace-level unfaithfulness relies on indirect controls rather than a direct experimental isolation.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bb97c87-72f8-4bad-b8c6-5f03eeec55c1",
  "isSidechain": true,
  "promptId": "ed43d146-c225-42c6-832a-351ecc310242",
  "agentId": "af8784ad3137a4fe6",
  "type": "user",
  "uuid": "df87cfac-39cb-4ba3-812a-d202ad4d9cc4",
  "sourceToolAssistantUUID": "7bb97c87-72f8-4bad-b8c6-5f03eeec55c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-26T08:19:12.647Z_

<details><summary>↩ Tool result · reported error · `toolu_01C31S2fP431fBuppZT2rvYb`</summary>

```text
File content (40156 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cad7e16b-2a93-45c9-9210-2784eb95f286",
  "isSidechain": true,
  "promptId": "ed43d146-c225-42c6-832a-351ecc310242",
  "agentId": "af8784ad3137a4fe6",
  "type": "user",
  "uuid": "7f02eb05-f69f-4ad6-a29e-414dfdc6369b",
  "toolUseResult": "Error: File content (40156 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "cad7e16b-2a93-45c9-9210-2784eb95f286",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-26T08:19:15.151Z_

The appendix is very large. Let me read it in chunks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f02eb05-f69f-4ad6-a29e-414dfdc6369b",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
  "requestId": "req_011CbQrQs9vLXA3FcohekgBC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28e0e394-52fc-4f45-9024-50167a417576",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SAMpxems9dyP2JFozoNBfL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1283,
      "cache_read_input_tokens": 48140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1283,
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

_source line 27 · 2026-05-26T08:19:15.797Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GpFK9uqJ8TUfVSrjKw3tud`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28e0e394-52fc-4f45-9024-50167a417576",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
  "requestId": "req_011CbQrQs9vLXA3FcohekgBC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58dbc798-a90d-4e0d-b8bf-e90872095862",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SAMpxems9dyP2JFozoNBfL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1283,
      "cache_read_input_tokens": 48140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1283,
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

_source line 28 · 2026-05-26T08:19:16.063Z_

<details><summary>↩ Tool result · `toolu_01GpFK9uqJ8TUfVSrjKw3tud`</summary>

```text
1	\section{Prompt Templates}
2	\label{app:prompts}
3	
4	SICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).
5	
6	\paragraph{System Prompt.}\leavevmode
7	
8	\begin{lstlisting}
9	You are a constraint extraction tool. Output ONLY valid JSON. Do NOT solve problems, reason about correctness, or think step-by-step. Extract constraints from the given trace exactly as stated.
10	\end{lstlisting}
11	
12	\paragraph{Mathematical Constraint Extraction (EXTRACTION\_PROMPT).}
13	
14	Used for GSM8K and AIME datasets. The placeholder \texttt{\{trace\}} is replaced with the reasoning trace at runtime.
15	
16	\begin{lstlisting}
17	Extract mathematical constraints from this reasoning trace as a JSON object.
18	
19	Rules:
20	- type: "equation", "inequality", or "predicate"
21	- expression: human-readable, e.g. "x + y == 14"
22	- z3_formula: a single comparison expression in Python Z3 syntax
23	- source_step: step number where the constraint appears
24	- Use variable names from the trace
25	
26	z3_formula MUST follow these rules:
27	- Allowed operators: ==, !=, <, >, <=, >=, +, -, *, /, **, %
28	- Use individual named variables: a1, a2, a3... NOT arrays a[1] or sets A
29	- Expand all sums explicitly: "a1 + a2 + a3 == 55" NOT "sum([a1,a2,a3])"
30	- NO Python builtins: sum(), len(), max(), min(), list(), set(), range(), int()
31	- Each z3_formula must be exactly ONE comparison (==, !=, <, >, <=, >=)
32	- For multiple values, write separate constraints for each
33	
34	Output ONLY the JSON below, nothing else:
35	{"constraints": [{"type": "equation", "expression": "x + y == 14", "z3_formula": "x + y == 14", "source_step": 1}], "answer": "final_answer", "variables": ["x", "y"]}
36	
37	Trace:
38	{trace}
39	\end{lstlisting}
40	
41	\paragraph{Logical Constraint Extraction (LOGIC\_EXTRACTION\_PROMPT).}
42	
43	Used for ProofWriter and FOLIO datasets.
44	
45	\begin{lstlisting}
46	IMPORTANT: You are an EXTRACTION tool, NOT a problem solver.
47	- Do NOT re-solve or re-reason about the problem.
48	- Do NOT verify whether the trace's reasoning is correct.
49	- ONLY extract the logical constraints that are explicitly stated or used in the trace below.
50	- Output ONLY the JSON object, nothing else.
51	
52	Extract logical constraints from this reasoning trace about a logic problem.
53	
54	The problem has facts (base assertions), rules (grounded implications), and derived conclusions. Convert each into a Z3 boolean formula.
55	
56	Variable naming:
57	- Unary property: property_entity (e.g., kind_anne, red_charlie, round_fiona)
58	- Binary relation: relation_subject_object (e.g., eats_bear_squirrel, likes_lion_cat)
59	- Use lowercase with underscores only
60	
61	Constraint types:
62	- "fact": a given assertion, e.g., kind_anne == True
63	- "rule": a grounded implication over specific entities, e.g., Implies(kind_anne, nice_anne)
64	- "derived": an inferred conclusion from facts + rules, e.g., nice_anne == True
65	
66	Z3 operators:
67	- Implies(a, b) for if-then rules
68	- And(a, b, ...) for conjunctive conditions
69	- Or(a, b, ...) for disjunctive conditions
70	- Not(a) for negation
71	- == True / == False for boolean assertions
72	
73	Output ONLY the JSON below, nothing else:
74	{"constraints": [{"type": "fact", "expression": "kind(anne)", "z3_formula": "kind_anne == True", "source_step": 1}], "answer": "True or False or Unknown", "variables": ["kind_anne"]}
75	
76	Trace:
77	{trace}
78	\end{lstlisting}
79	
80	\paragraph{Output Schema.}
81	
82	Both prompts produce a JSON object with the following structure:
83	
84	\begin{lstlisting}
85	{
86	  "constraints": [
87	    {
88	      "type": "&lt;equation|inequality|predicate>
89	               or &lt;fact|rule|derived>",
90	      "expression": "&lt;human-readable description>",
91	      "z3_formula": "&lt;Z3-compatible expression>",
92	      "source_step": &lt;integer>
93	    }
94	  ],
95	  "answer": "&lt;final answer string>",
96	  "variables": ["&lt;var1>", "&lt;var2>", "..."]
97	}
98	\end{lstlisting}
99	
100	The pipeline additionally injects an \texttt{answer\_assertion} constraint per trace (not produced by the LLM):
101	
102	\begin{lstlisting}
103	{"type": "answer_assertion",
104	 "expression": "answer is &lt;ans>",
105	 "z3_formula": "__sica_answer_&lt;ans> == True",
106	 "source_step": -1}
107	\end{lstlisting}
108	
109	\paragraph{Prompt Selection Logic.}
110	
111	Domain assignment is determined by dataset: FOLIO and ProofWriter use \textsc{Logic\_Extraction\_Prompt}; GSM8K, AIME, StrategyQA, and ARC-Challenge use \textsc{Extraction\_Prompt}. StrategyQA and ARC-Challenge are assigned to the mathematical prompt because their reasoning structure does not involve formal logic predicates or implications, despite StrategyQA producing boolean answers.
112	
113	
114	\section{Z3 MaxSAT Evaluation Pseudocode}
115	\label{app:z3-pseudocode}
116	
117	Algorithm~\ref{alg:maxsat} describes the Z3 MaxSAT solving procedure. Algorithm~\ref{alg:scorer} describes the source-trace attribution scoring.
118	
119	Domain constraint variables (e.g., \texttt{x + y == 14}) and answer assertion variables (e.g., \texttt{\_\_sica\_answer\_42 == True}) are logically independent in the Z3 formulation. Discriminative signal arises solely from conflicts among domain constraints: when traces supporting different answers produce mutually contradictory constraints, the solver excludes the lower-weight subset, and the scorer penalizes the corresponding answers.
120	
121	\begin{algorithm}[h]
122	\caption{Z3 Weighted Partial MAX-SAT}
123	\label{alg:maxsat}
124	\begin{algorithmic}[1]
125	\Require Deduplicated constraint set $\mathcal{C} = \{(c_m, w_m, S_m)\}_{m=1}^M$ where $c_m$ is a Z3 formula, $w_m$ is weight, $S_m$ is the set of source trace indices
126	\Ensure Partition $(\mathcal{C}^*, \mathcal{C}^{\setminus})$ where $\mathcal{C}^*$ is the max-weight satisfiable subset
127	\State $\textit{opt} \gets \textsc{Z3.Optimize()}$
128	\For{$m = 1, \ldots, M$}
129	    \State $b_m \gets$ fresh Boolean indicator
130	    \State $\textit{opt}.\textsc{Add}(b_m \Rightarrow c_m)$ \Comment{soft clause guarded by indicator}
131	    \State $\textit{opt}.\textsc{AddSoft}(b_m,\; \text{weight}=w_m)$
132	\EndFor
133	\State $\textit{result} \gets \textit{opt}.\textsc{Check}()$
134	\State $\textit{model} \gets \textit{opt}.\textsc{Model}()$
135	\State $\mathcal{C}^* \gets \{(c_m, w_m, S_m) : \textit{model}(b_m) = \top\}$
136	\State $\mathcal{C}^{\setminus} \gets \mathcal{C} \setminus \mathcal{C}^*$
137	\State \Return $(\mathcal{C}^*, \mathcal{C}^{\setminus})$
138	\end{algorithmic}
139	\end{algorithm}
140	
141	\begin{algorithm}[h]
142	\caption{Source-Trace Attribution Scoring}
143	\label{alg:scorer}
144	\begin{algorithmic}[1]
145	\Require Satisfied set $\mathcal{C}^*$, excluded set $\mathcal{C}^{\setminus}$, candidate answers $\mathcal{A}$, trace-answer mapping $\tau: \text{trace\_idx} \to a$, penalty weight $\alpha$
146	\Ensure Score $s(a)$ for each $a \in \mathcal{A}$
147	\For{each $a \in \mathcal{A}$}
148	    \State $T_a \gets \{i : \tau(i) = a\}$ \Comment{trace indices producing answer $a$}
149	    \State $\textit{pos}(a) \gets \sum_{(c,w,S) \in \mathcal{C}^*} w \cdot \mathbf{1}[S \cap T_a \neq \emptyset]$
150	    \State $\textit{neg}(a) \gets \sum_{(c,w,S) \in \mathcal{C}^{\setminus}} w \cdot \mathbf{1}[S \cap T_a \neq \emptyset]$
151	    \State $s(a) \gets \textit{pos}(a) - \alpha \cdot \textit{neg}(a)$
152	\EndFor
153	\State \Return $a^* = \arg\max_{a \in \mathcal{A}} s(a)$
154	\end{algorithmic}
155	\end{algorithm}
156	
157	
158	\section{Capability-Accuracy Constraint Diagnostics}
159	\label{app:diagnostics}
160	\label{app:cil}
161	
162	\paragraph{Conditional Correction Ratio.}
163	We define the \textit{Conditional Correction Ratio} (CCR) to summarize verifier--generator complementarity:
164	\begin{equation}
165	\label{eq:cil}
166	\text{CCR}(V, G) = \log \frac{P(V \text{ correct} \mid G \text{ wrong})}{P(V \text{ correct} \mid G \text{ correct})}.
167	\end{equation}
168	$\text{CCR} > 0$ means $V$ preferentially corrects $G$'s errors; $\text{CCR} < 0$ indicates shared bias. CCR links our findings: (1)~SCB corresponds to $\text{CCR}(\text{self}, G) \approx 0$; (2)~Finding~2 predicts $\text{CCR}(V, G) > 0$ when $V$ is independent and capable.
169	
170	\paragraph{Empirical CCR across verifier--generator pairs.}
171	Table~\ref{tab:cil_empirical} reports CCR for eight verifier--generator--dataset conditions, sorted by CCR descending. All three cross-architecture NLI pairs on ProofWriter yield $\text{CCR} > 0$ (verifier preferentially corrects generator errors), while all three same-model SICA conditions yield $\text{CCR} < 0$ (shared bias). CCR correlates with combo gain: Spearman $\rho = 0.839$, 95\% bootstrap CI $[0.338, 0.990]$; LOO-robust (min $p = 0.014$). Four of eight conditions share the DeBERTa verifier, yielding effective $n < 10$; results should be interpreted as a consistent pattern rather than a precise effect size.
172	
173	\begin{table}[h]
174	\centering
175	\small
176	\caption{Empirical CCR across eight verifier--generator conditions (sorted by CCR descending). $\text{CCR} > 0$: cross-architecture NLI verifiers on ProofWriter. $\text{CCR} < 0$: same-model SICA or mismatched capability gap.}
177	\label{tab:cil_empirical}
178	\resizebox{\columnwidth}{!}{%
179	\begin{tabular}{@{}lllrr@{}}
180	\toprule
181	Generator & Verifier & Dataset & CCR & $\Delta$ (pp) \\
182	\midrule
183	Mistral-7B & BART-MNLI & PW-600 & $+$1.86 & $+$5.17 \\
184	Mistral-7B & DeBERTa-MNLI & PW-600 & $+$1.67 & $+$6.67 \\
185	Mistral-7B & RoBERTa-MNLI & PW-600 & $+$1.42 & $+$4.17 \\
186	\addlinespace
187	Qwen2.5-14B & DeBERTa-MNLI & PW-600 & $-$0.21 & $+$0.33 \\
188	Mistral-7B & DeBERTa-MNLI & FOLIO-204 & $-$0.47 & $+$2.94 \\
189	\addlinespace
190	Mistral-7B & SICA & FOLIO-204 & $-$2.93 & $+$3.43 \\
191	Qwen2.5-14B & SICA & PW-600 & $-$4.21 & $-$2.50 \\
192	Mistral-7B & SICA & PW-600 & $-$4.61 & $-$2.83 \\
193	\bottomrule
194	\end{tabular}}
195	\end{table}
196	
197	\paragraph{Per-condition diagnostics.}
198	Table~\ref{tab:capability_trap} reports per-condition diagnostic metrics referenced in \S\ref{sec:entropy}.
199	
200	\begin{table}[h]
201	\centering
202	\small
203	\resizebox{\columnwidth}{!}{%
204	\begin{tabular}{@{}llrrrr@{}}
205	\toprule
206	Model & Domain & $C_0$ (\%) & Extr.\ Rate & Contr.\ Rate & $\Delta$ (pp) \\
207	\midrule
208	Qwen2.5-14B & FOLIO & 35.3 & 0.89 & 0.022 & 0.00 \\
209	Qwen2.5-14B & ProofWriter & 39.2 & 0.89 & 0.022 & $+$0.33 \\
210	Qwen2.5-14B & StrategyQA$^\dagger$ & 10.0 & 0.70 & --- & $+$3.33 \\
211	Qwen2.5-14B & ARC-Chall.$^\dagger$ & 5.0 & 1.00 & --- & $-$1.67 \\
212	Qwen2.5-7B & FOLIO+PW$^\dagger$ & 42.1 & 0.94 & 0.027 & 0.00 \\
213	Mistral-7B & FOLIO+PW$^\dagger$ & 50.0 & 0.88 & 0.056 & 0.00 \\
214	LLaMA-3.1-8B & StrategyQA & 41.0 & --- & --- & $+$2.00 \\
215	LLaMA-3.1-8B & FOLIO & 61.8 & 0.94 & 0.062 & $-$4.41 \\
216	DeepSeek-R1-7B & FOLIO+PW$^\dagger$ & 58.3 & 0.84 & 0.037 & $-$3.33 \\
217	QwQ-32B & Combined$^\dagger$ & 2.6 & --- & --- & 0.00 \\
218	Qwen2.5-14B & GSM8K$^\dagger$ & 13.3 & 0.15 & --- & 0.00 \\
219	\bottomrule
220	\end{tabular}}
221	\caption{Capability-accuracy constraint diagnostics. $C_0$: fraction of questions with multiple distinct candidate answers across $K=12$ traces. Extraction rate: fraction of traces yielding at least one parseable logical constraint. Contradiction rate: fraction of extracted constraint sets with internal contradictions. $\Delta$: SICA$-$SC gap (pp). $\dagger$: $n \leq 60$. Dashes indicate conditions where extraction diagnostics were not computed (StrategyQA uses boolean answers without symbolic extraction; QwQ-32B Combined had near-zero $C_0$, making extraction analysis uninformative). This table includes additional exploratory conditions not reported in Table~\ref{tab:main_results}.}
222	\label{tab:capability_trap}
223	\end{table}
224	
225	
226	\section{Statistical Power Analysis}
227	\label{app:power}
228	
229	We compute the minimum detectable effect (MDE) for each condition at $\alpha = 0.05$ and 80\% power using exact binomial power calculations over McNemar discordant pairs. Table~\ref{tab:power} reports three grouped conditions with $n \geq 200$ (Qwen2.5-14B FOLIO and ProofWriter are pooled into a single $n{=}804$ analysis, corresponding to four Table~\ref{tab:main_results} rows), which constitute our confirmatory analyses. The remaining seven conditions ($n \leq 60$) yield infinite MDE due to insufficient discordant pairs and serve only as regime characterization.
230	
231	\begin{table}[h]
232	\centering
233	\small
234	\resizebox{\columnwidth}{!}{%
235	\begin{tabular}{lrrrrr}
236	\toprule
237	\textbf{Condition} & $n$ & \textbf{MDE} & \textbf{Obs.\ $\Delta$} & \textbf{Obs.\ Pow.} \\
238	\midrule
239	Qwen-14B FOLIO+PW   & 804 & 1.86pp & $+$0.25pp & 5.7\%  \\
240	LLaMA-8B StrategyQA  & 200 & 4.64pp & $+$2.00pp & 20.6\% \\
241	LLaMA-8B FOLIO       & 204 & 4.84pp & $-$4.41pp & 18.6\% \\
242	\bottomrule
243	\end{tabular}}
244	\caption{Power analysis for confirmatory conditions ($n \geq 200$). MDE = minimum detectable effect at 80\% power. All observed effects fall below their respective MDEs, and observed power remains below 21\% in every case.}
245	\label{tab:power}
246	\end{table}
247	
248	The largest study (Qwen-14B, $n{=}804$, 30 discordant pairs) can detect effects as small as 1.86pp, yet the observed $\Delta$ of $+$0.25pp is an order of magnitude smaller. The two LLaMA-8B conditions require effects of 4.64pp and 4.84pp to reach significance; neither observed $\Delta$ approaches these thresholds. All three conditions are consistent with the null hypothesis that SICA provides no accuracy gain over self-consistency.
249	
250	
251	\section{Bootstrap Confidence Intervals}
252	\label{app:bootstrap}
253	
254	We compute 95\% confidence intervals for $\Delta(\text{SICA} - \text{SC})$ via 10{,}000 bootstrap resamples (percentile method, seed 42). Table~\ref{tab:bootstrap} reports the results for the three confirmatory conditions.
255	
256	\begin{table}[h]
257	\centering
258	\small
259	\resizebox{\columnwidth}{!}{%
260	\begin{tabular}{lrrl}
261	\toprule
262	\textbf{Condition} & $n$ & \textbf{Obs.\ $\Delta$} & \textbf{95\% CI} \\
263	\midrule
264	Qwen-14B FOLIO+PW   & 804 & $+$0.25pp & [$-$1.12, $+$1.62] \\
265	LLaMA-8B StrategyQA  & 200 & $+$2.00pp & [$-$1.50, $+$5.50] \\
266	LLaMA-8B FOLIO       & 204 & $-$4.41pp & [$-$5.88, $+$0.98] \\
267	\bottomrule
268	\end{tabular}}
269	\caption{Bootstrap 95\% confidence intervals for $\Delta(\text{SICA} - \text{SC})$ in percentage points. All intervals include zero, consistent with no reliable accuracy difference.}
270	\label{tab:bootstrap}
271	\end{table}
272	
273	All three intervals contain zero. The narrowest interval (Qwen-14B, [$-$1.12, $+$1.62]) rules out practically meaningful gains ($>$2pp) even in the most favorable case. The widest interval (LLaMA-8B FOLIO, [$-$5.88, $+$0.98]) skews negative, indicating that SICA may slightly hurt accuracy in this condition. These results corroborate the McNemar tests and power analysis: no condition provides evidence that logical constraint aggregation improves over majority voting.
274	
275	
276	\section{Case Studies: Discordant Predictions}
277	\label{app:case-studies}
278	
279	Among 804 problems, SICA and SC agree on 773 (96.1\%). The 31 discordant cases comprise 16 SICA wins (SICA correct, SC wrong), 14 SC wins (SC correct, SICA wrong), and 1 where both select different wrong answers. All 31 occur at exact ties (entropy${=}1.0$, 6:6 vote split) or near-ties (entropy${\geq}0.9183$, 8:4 at most), since SICA can differ from SC only when constraint weights shift the majority away from SC's tiebreak choice. We present three representative cases that illustrate the mechanism behind capability-accuracy constraint failures.
280	
281	\paragraph{Case 1: SICA Wins (folio\_134, FOLIO).}
282	
283	\emph{Premises}: Some mammals have teeth. Platypus have no teeth. Platypus are mammals. Humans have teeth. \emph{Conclusion}: Humans are mammals. \emph{Gold}: Unknown.
284	
285	The premises state that \emph{some} mammals have teeth and that humans have teeth, but ``having teeth'' is not sufficient for ``being a mammal'' under open-world semantics. SC produces a 6:6 split (Unknown:6, True:6) and tiebreaks alphabetically to True (wrong). SICA extracts 7 constraints; MaxSAT excludes 1 constraint inconsistent with the rest, reducing the weighted score for True-voting traces and tipping the aggregation to Unknown (correct). The excluded constraint likely captured an incorrect inference step (e.g., affirming the consequent) present only in True-voting traces. While SICA succeeds here, the success is coincidental: the excluded constraint happens to anti-correlate with the correct answer.
286	
287	\paragraph{Case 2: SC Wins (ProofWriter-1066\_Q6, ProofWriter).}
288	
289	\emph{Key chain}: White(Bob)$\to$Round(Bob) [white things are round] $\to$ Young(Bob) [all round things are young]. \emph{Conclusion}: ``Bob is not young.'' \emph{Gold}: False (Bob IS young).
290	
291	SC produces a 6:6 split (False:6, True:6) and tiebreaks to False (correct). SICA extracts 17 constraints; MaxSAT excludes 2 that appear preferentially in False-voting traces. These excluded constraints likely captured correct intermediate derivations (e.g., \texttt{young\_bob == True}) that appeared only in traces completing the full deduction chain. By excluding them, MaxSAT removes evidence supporting the correct answer. SICA selects True (wrong). This case illustrates how self-extracted constraints can systematically mislead: correct reasoning steps become discriminative signals that the solver mistakenly penalizes.
292	
293	\paragraph{Case 3: Non-discriminative Constraints (ProofWriter-903\_Q6, ProofWriter).}
294	
295	\emph{Key chain}: Nice(Mouse)$\to$Cold(Mouse) [all nice people are cold] $\to$ Chases(Mouse,Mouse) [nice and cold $\to$ chase mouse]. \emph{Conclusion}: ``The mouse does not chase the mouse.'' \emph{Gold}: False.
296	
297	SC produces a 6:6 split (False:6, Unknown:6) and tiebreaks to False (correct). SICA extracts 44 constraints but excludes only 1 (2.3\%). The remaining 43 are domain facts and grounded rules (\texttt{nice\_mouse == True}, \texttt{Implies(nice\_mouse, cold\_mouse)}, etc.) that Z3 satisfies identically regardless of the final answer. Both False-voting and Unknown-voting traces share the same premises and grounded rules; they differ only in whether the trace completed the full derivation chain. The single excluded constraint carries negligible weight against 43 shared constraints, so SICA collapses to SC.
298	
299	\paragraph{Pattern.}
300	
301	These cases exemplify the general pattern across the 773 agreeing problems: the vast majority of extracted constraints encode shared domain structure rather than answer-specific reasoning, and MaxSAT aggregation degenerates to majority vote. Table~\ref{tab:case_summary} summarizes.
302	
303	\begin{table}[h]
304	\centering
305	\small
306	\caption{Summary of three representative discordant cases. All occur at exact 6:6 vote ties. Constraint exclusion can break ties in either direction (Cases 1--2) or have no effect (Case 3).}
307	\label{tab:case_summary}
308	\resizebox{\columnwidth}{!}{%
309	\begin{tabular}{@{}lllcccc@{}}
310	\toprule
311	Case & ID & Gold & SC & SICA & \#Constr. & Excl.\ (\%) \\
312	\midrule
313	1 (SICA win) & folio\_134 & Unknown & True $\times$ & Unknown $\checkmark$ & 7 & 1 (14.3\%) \\
314	2 (SC win) & PW-1066\_Q6 & False & False $\checkmark$ & True $\times$ & 17 & 2 (11.8\%) \\
315	3 (Non-disc.) & PW-903\_Q6 & False & False $\checkmark$ & False $\checkmark$ & 44 & 1 (2.3\%) \\
316	\bottomrule
317	\end{tabular}}
318	\end{table}
319	
320	
321	\section{Oracle Control}
322	\label{app:oracle}
323	\label{sec:oracle}
324	\label{app:pw-oracle-subtype}
325	
326	Replacing self-extracted constraints with gold annotations (FOLIO logical formulae, ProofWriter DSL), Oracle-SICA yields $+29.90$\,pp on Mistral-7B FOLIO ($p < 10^{-13}$), $+13.73$\,pp on Qwen2.5-14B FOLIO ($p = 2.0 \times 10^{-7}$), and $+17.17$\,pp on ProofWriter ($p < 10^{-14}$). Z3 agrees with gold labels on 95.1\% (FOLIO) and 97.1\% (ProofWriter). The MAX-SAT mechanism is sound; Mistral-7B's best self-extracted $\Delta$ ($+3.43$\,pp) captures only 11.5\% of its oracle ceiling. For Qwen2.5-14B on ProofWriter, the gap is wider still: self-extraction degrades accuracy ($-2.50$\,pp) against an oracle ceiling of $+17.17$\,pp, indicating that stronger models do not self-extract more effectively.
327	
328	\paragraph{ProofWriter per-subtype analysis.} ProofWriter problems encode deductive rules as Domain-Specific Language (DSL) logic programs. Each problem uses one of four predicate subtypes: attribute predicates with or without negation (AttNeg, AttNoneg), and relation predicates with or without negation (RelNeg, RelNoneg). Relation predicates involve binary relations between entities (e.g., \texttt{eats(bear, squirrel)}), while attribute predicates assign unary properties (e.g., \texttt{kind(anne)}).
329	
330	The oracle pipeline parses these DSL annotations deterministically into Z3 formulas without any LLM involvement. Of the 600 ProofWriter problems, 594 (99.0\%) produce valid Z3 parses; the remaining 6 fail due to unsupported DSL constructs. Across all 7{,}128 trace-problem pairs submitted to Z3, the solver returns a result in every case (0\% solver errors). Z3 evaluations agree with ground-truth labels on 577 of 594 parseable problems (97.14\%), confirming that the deterministic DSL-to-Z3 translation faithfully preserves problem semantics.
331	
332	Table~\ref{tab:pw_oracle_subtype} reports the per-subtype breakdown. Relation-predicate subtypes show substantially larger gains than attribute-predicate subtypes: RelNeg improves by $+28.58$~pp and RelNoneg by $+23.29$~pp, compared to $+10.00$~pp for AttNeg and $+8.44$~pp for AttNoneg. Relation predicates involve longer reasoning chains with more intermediate entities, producing greater answer diversity across traces ($C_0$) and more opportunities for oracle constraints to correct errors.
333	
334	\begin{table}[h]
335	\centering
336	\caption{ProofWriter oracle experiment per-subtype breakdown. Oracle-SICA uses gold DSL annotations parsed deterministically to Z3 for consistency checking. Relation-predicate subtypes (RelNeg, RelNoneg) show larger gains than attribute-predicate subtypes; relation subtypes involve longer reasoning chains and benefit more from oracle constraints. Bold indicates best accuracy per row.}
337	\label{tab:pw_oracle_subtype}
338	\resizebox{\columnwidth}{!}{%
339	\begin{tabular}{lcccc}
340	\toprule
341	Subtype & $n$ & SC Acc (\%) & Oracle Acc (\%) & $\Delta$ (pp) \\
342	\midrule
343	AttNoneg & 154 & 90.26 & \textbf{98.70} & +8.44 \\
344	AttNeg & 160 & 81.88 & \textbf{91.88} & +10.00 \\
345	RelNoneg & 146 & 60.96 & \textbf{84.25} & +23.29 \\
346	RelNeg & 140 & 60.71 & \textbf{89.29} & +28.58 \\
347	\midrule
348	Overall & 600 & 74.00 & \textbf{91.17} & +17.17 \\
349	\bottomrule
350	\end{tabular}}
351	\end{table}
352	
353	
354	\section{Constraint Ablation Details}
355	\label{app:ablation}
356	\label{sec:ablation}
357	
358	\begin{table}[h]
359	\centering
360	\small
361	\caption{Constraint ablation (Qwen2.5-14B, $n = 804$). Agreement: predictions identical to SC. MAX-SAT and count-only produce nearly identical predictions, confirming that self-extracted constraints carry no signal beyond vote counts.}
362	\label{tab:ablation}
363	\begin{tabular}{@{}lrc@{}}
364	\toprule
365	Aggregation & Acc.\ (\%) & Agreement w/ SC \\
366	\midrule
367	SC (majority vote) & 76.24 & --- \\
368	SICA (MAX-SAT) & 76.49 & 773\,/\,804 \\
369	Count-only & 76.62 & 774\,/\,804 \\
370	Random-weight & 75.87 & 764\,/\,804 \\
371	\bottomrule
372	\end{tabular}
373	\end{table}
374	
375	\begin{table}[h]
376	\centering
377	\small
378	\caption{MAX-SAT vs.\ count-only agreement across constraint weight $\alpha \in [0,1]$ on FOLIO ($n = 204$). Mistral-7B (BR $= 4.97\times$, seed 42); Qwen2.5-14B (BR $= 3.93\times$, seed 123). $\alpha{=}0$: pure Z3 satisfiability (no source-attribution); $\alpha{=}1$: full source-attribution penalty. Agreement $\geq 99\%$ at all $\alpha$ including endpoints, confirming vacuity is weight-insensitive.}
379	\label{tab:alpha-ablation}
380	\begin{tabular}{@{}crr@{}}
381	\toprule
382	$\alpha$ & Mistral Agr.\ (\%) & Qwen2.5 Agr.\ (\%) \\
383	\midrule
384	0.0 & 100 & 100 \\
385	0.1 & 100 & 100 \\
386	0.3 & 100 & 100 \\
387	0.5 & 100 & 100 \\
388	0.7 & 99 & 100 \\
389	0.9 & 99 & 100 \\
390	1.0 & 99 & 100 \\
391	\bottomrule
392	\end{tabular}
393	\end{table}
394	
395	
396	\section{Remediation Strategy Details}
397	\label{app:remediation}
398	
399	Table~\ref{tab:remediation} reports nine prompt-level strategies; Table~\ref{tab:method_interventions} reports three method-level interventions. Figure~\ref{fig:interventions-summary} visualizes all 27 strategies.
400	
401	\begin{figure*}[t]
402	\centering
403	\includegraphics[width=0.82\textwidth]{figures/fig2_interventions_compact.pdf}
404	\caption{Twenty-three of 27 training-free strategies across four categories (four additional strategies tested but omitted for clarity). All produce neutral-to-negative $\Delta$ vs.\ SC. Grey band: $\pm 1$\,pp noise zone.}
405	\label{fig:interventions-summary}
406	\end{figure*}
407	
408	\begin{table}[h]
409	\centering
410	\small
411	\caption{Nine prompt-level remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.98\%$, $\Delta = -0.49$\,pp. None reaches significance. Three method-level strategies are reported in Table~\ref{tab:method_interventions}.}
412	\label{tab:remediation}
413	\resizebox{\columnwidth}{!}{%
414	\begin{tabular}{@{}llrl@{}}
415	\toprule
416	Strategy & Target & $\Delta$ (pp) & Key finding \\
417	\midrule
418	Contrastive$^a$ & Prompt & $-$1.10 & non-disc.\ 6.0\% ($\downarrow$ from 8.2\%) \\
419	Cross-model$^b$ & Architecture & 0.00 & disc.\ 0\% (weak$\to$strong); $\pm$1\,pp (strong$\to$weak) \\
420	Qwen3-14B$^c$ & Capability & $-$0.49 & $p = 0.655$ \\
421	Z3 feedback & Solver & --- & 0.9\% UNSAT trigger \\
422	Cons.\ filtering & Noise & 0.00 & $T{\geq}4 \to$ SC \\
423	Cross-trace UNSAT & Independence & --- & 56.4\% $\emptyset$ vars \\
424	$T{=}1.0$$^d$ & Diversity & 0.00 & isolated peak at $T{=}0.7$ only \\
425	Multi-temp$^e$ & Diversity & 0.00 & $b{=}5$, $c{=}5$ (balanced) \\
426	Disc.\ filtering$^f$ & Filtering & 0.00 & 803/804 agree w/ SICA \\
427	\bottomrule
428	\end{tabular}}\\[2pt]
429	{\footnotesize $^a$\,$n{=}182$ (extraction failures excluded). $^b$\,Weak$\to$strong: Mistral-7B extracts from Qwen2.5-14B traces. Strong$\to$weak: Qwen3-14B (60.29\%) and Qwen2.5-14B (58.33\%) extract from Mistral-7B FOLIO traces ($n{=}204$); self-extraction baseline 59.31\%. $^c$\,$n{=}204$, SC $= 83.33\%$. $^d$\,Mistral-7B FOLIO, $n{=}204$. $^e$\,Mistral-7B FOLIO, $T \in \{0.3, 0.7, 1.2\}$, 4 traces each, $n{=}204$. $^f$\,Qwen2.5-14B, $n{=}804$; removing non-discriminative constraints.}
430	\end{table}
431	
432	
433	\begin{table}[h]
434	\centering
435	\small
436	\caption{Method-level interventions on Mistral-7B with McNemar's paired test. All produce neutral-to-catastrophic results. ICG shows two FOLIO seeds; $p$ for the first. {*}{*}{*}\,$p < 0.001$; {*}{*}\,$p < 0.01$.}
437	\label{tab:method_interventions}
438	\resizebox{\columnwidth}{!}{%
439	\begin{tabular}{@{}ll rc rc@{}}
440	\toprule
441	& & \multicolumn{2}{c}{FOLIO ($n = 204$)} & \multicolumn{2}{c}{LogiQA ($n = 200$)} \\
442	\cmidrule(lr){3-4} \cmidrule(lr){5-6}
443	Method & Target & $\Delta$ (pp) & $p$ & $\Delta$ (pp) & $p$ \\
444	\midrule
445	SC baseline & --- & 0.00 & --- & 0.00 & --- \\
446	ICG & Trace coupling & $-$1.96\,/\,$+$1.47 & .206 & $-$0.50 & .706 \\
447	Contrastive & Scoring bias & $\mathbf{-9.31}$ & .007 & $-$4.50 & .160 \\
448	Debate & Role diversity & $\mathbf{-18.63}$ & ${<}.001$ & $\mathbf{-23.00}$ & ${<}.001$ \\
449	\bottomrule
450	\end{tabular}}
451	\end{table}
452	
453	\section{Additional Intervention Results}
454	\label{app:additional-interventions}
455	
456	Table~\ref{tab:additional_interventions} reports the remaining 15 strategies beyond the 12 in Appendix~\ref{app:remediation}.
457	
458	\begin{table*}[h]
459	\centering
460	\small
461	\caption{Additional intervention results beyond the nine prompt-level and three method-level strategies reported in the main text. All produce neutral-to-negative results, completing the exhaustive remediation analysis across 27 distinct approaches.}
462	\label{tab:additional_interventions}
463	\begin{tabular}{@{}llllrl@{}}
464	\toprule
465	\# & Method & Type & Target & $\Delta$ (pp) & Key Finding \\
466	\midrule
467	13 & PROVE (code verif.) & Paradigm & Formal proof & $-$1.9 & 15.2\% compilable; conclusive acc.\ = 50\% \\
468	14 & CEGIS (iterative) & Multi-round & Consistency & 0.0$^\dagger$ & R1 $+$3.43\,pp then oscillates \\
469	15 & DeepConf (logprob) & Filtering & Confidence & 0.0 & $\Delta_{\text{logprob}} = 0.006$ (no separation) \\
470	16 & Cross-model SICA & Cross-model & Independence & $-$0.49 & $\kappa_{\text{cross}}{=}0.42$ vs $\kappa_{\text{within}}{=}0.53$ \\
471	17 & Problem perturbation & Input diversity & Trace diversity & $<$0 & $\kappa$ \emph{increased} to 0.70 (anti-effect) \\
472	18 & MIN-UNSAT & Solver objective & Constraint sel.\ & $-$6.5 & Mean excluded constraints $= 1.3$ \\
473	19 & $\kappa$-aware SC & Voting rule & Weighted voting & 0.0 & 11/11 conditions $\Delta = 0$ \\
474	20 & Z3 trace filter & Trace filtering & Quality & $-$0.49 & Precision 49.1\%, 7 questions affected \\
475	21 & Bootstrapped gold & Iterative & Self-improvement & 0.0$^\dagger$ & R1 $+$2.45\,pp then oscillates \\
476	22 & Selective abstention & Diagnostic & Confidence & $+$4.4$^*$ & AUROC $= 0.673$, at 80\% coverage \\
477	23 & ASCII perturbation & Input diversity & Format diversity & 0.0 & $\kappa$: $0.39 \to 0.36$ (negligible) \\
478	\addlinespace
479	24 & Atom pipeline & Paradigm & Decomposition & $-$10.0 & Atomic extraction degrades \\
480	25 & Premise-only filter & Constraint sel.\ & Bias isolation & $+$2.45 & $p = 0.359$; halves conclusion-bias \\
481	26 & DPP trace selection & Trace diversity & Determinantal & $+$1.47 & $p = 0.629$; $K_{\text{sel}}{=}8$ \\
482	27 & Z3 strict-mode & Solver config & UNSAT filtering & 0.0 & McNemar $b{=}1, c{=}1$; 63\% UNSAT \\
483	\bottomrule
484	\end{tabular}\\[2pt]
485	{\footnotesize All experiments on Mistral-7B FOLIO ($n{=}204$) unless noted. $^\dagger$\,Oscillates without convergence; net effect $\approx 0$. $^*$\,Accuracy gain only at reduced coverage (diagnostic value, not a general improvement). Methods 1--12 are reported in Table~\ref{tab:remediation} and Table~\ref{tab:method_interventions}.}
486	\end{table*}
487	
488	Figure~\ref{fig:process-kappa} (main text) visualizes the process--answer independence gap.
489	
490	
491	\section{Extraction Error Taxonomy}
492	\label{app:extraction}
493	\label{sec:extraction-taxonomy}
494	
495	Constraints must discriminate between candidate answers for MAX-SAT to produce a ranking different from majority vote. We measure discriminative power at two levels on Qwen2.5-14B across FOLIO and ProofWriter ($n = 804$). At the source-trace level, 39.2\% of total constraint weight originates from traces whose answer differs from the plurality, but only 12.1\% of individual constraints fall into this minority category. At the Z3 semantic level, 91.8\% of constraints [95\% CI: 91.2, 92.4] are technically discriminative, producing different satisfiability outcomes when evaluated against different candidate answers. Only 8.2\% are non-discriminative.
496	
497	The high discriminative rate does not translate into accuracy gains because discrimination mirrors the model's own answer distribution. Each trace produces constraints with its own variable names, so Z3 treats identically-intended propositions as unrelated symbols; among cross-answer constraint pairs, 56.4\% share zero Z3 variables. This variable isolation means constraints from different traces are trivially jointly satisfiable, and MAX-SAT retains nearly all of them regardless of source answer. Removing the 8.2\% non-discriminative constraints yields zero accuracy improvement. The discriminative majority does not provide independent signal; it reinforces the majority answer that SC would already select. This confirmation bias, not a lack of discrimination, explains why SICA degenerates to majority voting (Appendix~\ref{app:ablation}).
498	
499	
500	\section{Hyperparameter Sensitivity}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58dbc798-a90d-4e0d-b8bf-e90872095862",
  "isSidechain": true,
  "promptId": "ed43d146-c225-42c6-832a-351ecc310242",
  "agentId": "af8784ad3137a4fe6",
  "type": "user",
  "uuid": "a8222c74-4c93-48eb-8dfc-5b59e0046fa3",
  "sourceToolAssistantUUID": "58dbc798-a90d-4e0d-b8bf-e90872095862",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-26T08:19:20.320Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JqqTHeb9u8fQ31emYxE18u`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "offset": 500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8222c74-4c93-48eb-8dfc-5b59e0046fa3",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
  "requestId": "req_011CbQrR7kFkbbrMULx68oKP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5876b96e-4384-40f0-a335-df55d8211548",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C1wGxm4MtvEyZ5yoDcvqtG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12416,
      "cache_read_input_tokens": 49423,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12416
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 49423,
          "cache_creation_input_tokens": 12416,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12416,
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

_source line 30 · 2026-05-26T08:19:20.605Z_

<details><summary>↩ Tool result · `toolu_01JqqTHeb9u8fQ31emYxE18u`</summary>

```text
500	\section{Hyperparameter Sensitivity}
501	\label{app:sensitivity}
502	\label{sec:k-sensitivity}
503	\label{sec:t-sensitivity}
504	
505	\subsection{K Sensitivity}
506	
507	Figure~\ref{fig:k-sensitivity} shows SICA $\Delta$ as a function of the number of sampled traces $K$ for Mistral-7B on FOLIO ($n = 204$, no fixed seed). The relationship is non-monotonic: $K = 4$ yields $\Delta = -1.47$\,pp, $K = 8$ yields $\Delta = -1.96$\,pp, $K = 12$ reaches $\Delta = +3.43$\,pp, $K = 16$ drops to $\Delta = +1.47$\,pp, and $K = 20$ partially recovers to $\Delta = +1.96$\,pp. The recovery at $K = 20$ rules out a simple peaked pattern, but $K = 12$ remains the only setting with $\Delta > 2$\,pp ($p = 0.092$, marginal).
508	
509	The apparent $\Delta$ peak at $K = 12$ is confounded with SC baseline. SICA absolute accuracy plateaus at 59.31\% (121/204) for $K \geq 12$: identical at $K = 12$ and $K = 20$. The $\Delta$ variation across these settings is driven primarily by SC fluctuations rather than by SICA improvement. $K = 12$ produces a relatively low SC (55.88\%), placing it in the intermediate-SC region; $K = 8$ (SC $= 58.33\%$) and $K = 20$ (SC $= 57.35\%$) have higher baselines, compressing $\Delta$ even though SICA accuracy does not change for $K \geq 12$. Additional traces beyond $K = 12$ provide no benefit to SICA absolute performance, consistent with the constraint quality bottleneck. The $K = 12$ $\Delta$ captures only 25.0\% of the oracle ceiling ($+13.73$\,pp).
510	
511	\begin{figure*}[t]
512	\centering
513	\includegraphics[width=0.75\textwidth]{f3_k_sensitivity}
514	\caption{SICA $\Delta$ (pp) vs.\ number of traces $K$ for Mistral-7B on FOLIO ($n = 204$, default seed, $T = 0.7$). Non-monotonic pattern: SICA accuracy plateaus at 59.31\% for $K \geq 12$; the apparent $\Delta$ peak at $K = 12$ partly reflects a relatively low SC baseline (55.88\%) at that point. Error bars: 95\% bootstrap CI.}
515	\label{fig:k-sensitivity}
516	\end{figure*}
517	
518	\subsection{Temperature Sensitivity}
519	
520	Temperature sensitivity on Mistral-7B FOLIO ($n = 204$, default seed) reveals a sharp isolated peak rather than a smooth trend. Across four temperature settings, only $T = 0.7$ produces a positive effect: $T = 0.3$ yields $\Delta = -1.47$\,pp (SC $= 58.33\%$), $T = 0.5$ yields $\Delta = -0.98$\,pp (SC $= 58.33\%$), $T = 0.7$ yields $\Delta = +3.43$\,pp (SC $= 55.88\%$), and $T = 1.0$ yields $\Delta = 0.00$\,pp (SC $= 55.39\%$). All other temperatures yield negative or null effects, and the single positive result at $T = 0.7$ is confounded with SC baseline. Combined with the seed sensitivity (0 of 4 seeds reaching $p < 0.05$ at $T = 0.7$), the positive trend depends on a specific combination of temperature, seed, and baseline accuracy that same-model sampling rarely achieves.
521	
522	The parallel between $K$ and $T$ sensitivity points to a common underlying variable. In both sweeps, the setting that produces the largest SICA gain also produces a relatively low SC baseline (55.88\%), which places it in the intermediate-SC region. The hyperparameters themselves ($K$, $T$) are not the causal driver; they modulate SC level, and it is the SC level that determines whether SICA has operating room.
523	
524	
525	\section{Entropy Decomposition}
526	\label{app:entropy}
527	\label{sec:entropy}
528	
529	We partition problems by trace agreement: high-entropy (majority count $\leq 8$ out of $K = 12$) and low-entropy (majority count $\geq 9$). Table~\ref{tab:entropy} reports SICA $\Delta$ within each partition across eight model-dataset conditions.
530	
531	\begin{table}[h]
532	\centering
533	\small
534	\caption{Entropy decomposition of SICA $\Delta$ (pp). High-entropy: majority count $\leq 8$; low-entropy: majority count $\geq 9$. $^\dagger$Partial data (180/600). Pre-tiebreaking SC values; pattern robust to BH correction.}
535	\label{tab:entropy}
536	\setlength{\tabcolsep}{3.5pt}
537	\begin{tabular}{@{}llrrrr@{}}
538	\toprule
539	Model & Dataset & \multicolumn{2}{c}{High-entropy} & \multicolumn{2}{c}{Low-entropy} \\
540	\cmidrule(lr){3-4} \cmidrule(lr){5-6}
541	 & & $n$ & $\Delta$ & $n$ & $\Delta$ \\
542	\midrule
543	Mistral-7B & FOLIO & 78 & $\mathbf{+12.8}$ & 126 & 0.0 \\
544	Mistral-7B (s123) & FOLIO & 77 & $\mathbf{+9.1}$ & 127 & 0.0 \\
545	Mistral-7B (s456) & FOLIO & 75 & $-$1.3 & 129 & 0.0 \\
546	Mistral-7B & PW-D5 & 267 & $-$4.9 & 333 & $-$1.2 \\
547	Qwen2.5-14B & FOLIO & 37 & $-$8.2 & 167 & $-$0.6 \\
548	Qwen2.5-14B & LogiQA & 23 & $-$4.3 & 177 & 0.0 \\
549	Qwen2.5-7B & FOLIO & 47 & $-$2.1 & 157 & 0.0 \\
550	LLaMA-3.1-8B$^\dagger$ & PW-D5 & 76 & $-$3.9 & 104 & $-$1.9 \\
551	\bottomrule
552	\end{tabular}
553	\end{table}
554	
555	Two patterns emerge. First, low-entropy problems produce $\Delta \approx 0$\,pp across all eight conditions: when traces agree, constraints carry no information beyond the majority vote.
556	
557	Second, the direction of SICA's effect on high-entropy problems depends on the accuracy regime, not on entropy alone. In the intermediate-SC region (Mistral-7B on FOLIO, default-seed and seed-123 runs), high-entropy $\Delta$ reaches $+12.8$ and $+9.1$\,pp: traces genuinely disagree, and constraints from correct-answer traces provide discriminative signal that resolves the disagreement. In Type~A conditions (Qwen2.5-14B on FOLIO, $\Delta = -8.2$\,pp), high-entropy problems represent rare deviations from a strong model's consensus; constraints inherit the model's confirmation bias. In Type~C (Mistral-7B on ProofWriter, $\Delta = -4.9$\,pp), high-entropy problems reflect systematic errors. The mechanism is not entropy per se but the interaction of entropy with model capability.
558	
559	
560	\section{Failure Mode Analysis}
561	\label{app:failure-modes}
562	\label{sec:failure-modes}
563	
564	The regime-dependent pattern in Table~\ref{tab:main_results} reflects three distinct failure modes of self-extracted logical constraints.
565	
566	\paragraph{Type A: confirmation bias (SC $\geq$ $\sim$60\%).} Strong models produce consistent reasoning traces, and constraints extracted from those traces mirror the answer distribution. When most constraints support the same candidate, MAX-SAT excludes few clauses ($|\mathcal{C}^{\setminus}| \approx 0$), the penalty term in Eq.~\ref{eq:score} vanishes, and the scoring function degenerates to weighted vote counting (Eq.~\ref{eq:degenerate}). SICA and SC then produce identical predictions. The ablation in Appendix~\ref{app:ablation} confirms this empirically: on Qwen2.5-14B (FOLIO + ProofWriter, $n = 804$), MAX-SAT and count-only baselines agree on 803 of 804 predictions.
567	
568	\paragraph{Type B: non-formalizable domains.} LogiQA problems require pragmatic and contextual reasoning that resists clean logical formalization. Qwen2.5-14B on LogiQA achieves an extraction rate of 86.4\%, but the resulting constraints have a contradiction rate of only 0.8\%: extracted formulas rarely conflict across traces, leaving MAX-SAT with no logical tension to exploit. Mistral-7B on LogiQA sits in the same SC range (50.00\%) yet produces $\Delta = +1.50$\,pp ($p = 0.581$); Qwen2.5-14B on the same domain yields $\Delta = -1.00$\,pp ($p = 0.625$). Neither model benefits, confirming that the right accuracy regime is necessary but not sufficient when the domain resists formalization.
569	
570	\paragraph{Type C: error amplification (SC $\leq$ $\sim$40\%).} When model accuracy is low, the majority of traces reach incorrect answers. Constraints extracted from wrong traces encode incorrect reasoning as formal rules. Z3 treats these rules as soft clauses with weight proportional to their frequency, so the solver preferentially satisfies the wrong constraints and penalizes traces that happen to reach the correct answer. Mistral-7B on ProofWriter ($\Delta = -2.83$\,pp, raw $p = 0.014$; BH adj.\ $p = 0.042$) demonstrates this effect: SICA converts a weak positive signal in trace diversity into a net negative by formalizing the errors.
571	
572	
573	\section{Cross-Model Confirmation Bias}
574	\label{app:cross-model-bias}
575	
576	Table~\ref{tab:cross-model-bias} reports MaxSAT-weighted confirmation bias metrics across three model families on FOLIO ($n = 204$). Weighted bias ratio and wrong-supporting constraint percentage both decrease with model capability, while SICA's accuracy effect shifts from positive (Mistral, intermediate-SC regime) to negative (LLaMA, high-SC regime). Raw bias ratios ($4.97\times$, $3.93\times$, $3.87\times$) are reported in \S\ref{sec:confirmation-bias}. LLaMA raw BR CI: [3.11, 4.98] (4/12 traces).
577	
578	\begin{table}[h]
579	\centering
580	\small
581	\caption{Cross-model confirmation bias on FOLIO ($n = 204$, $K = 12$). BR (wtd.): MaxSAT-weighted ratio of error-supporting constraints on incorrect vs.\ correct problems. Wrong \%: weighted fraction of constraints supporting the incorrect majority on error problems. $\Delta$: SICA $-$ SC (pp).}
582	\label{tab:cross-model-bias}
583	\begin{tabular}{@{}lrrr@{}}
584	\toprule
585	Model & BR (wtd.) & Wrong (\%) & $\Delta$ (pp) \\
586	\midrule
587	Mistral-7B & $4.24\times$ & 80.9 & $+$4.90 \\
588	Qwen2.5-14B & $3.69\times$ & 78.7 & $-$0.98 \\
589	LLaMA-3.1-8B & $2.66\times$ & 72.7 & $-$4.41 \\
590	\bottomrule
591	\end{tabular}
592	\end{table}
593	
594	\paragraph{Frontier model universality.}
595	\label{app:frontier-scb}
596	Table~\ref{tab:frontier-scb} (main text) reports confirmation bias across nine models spanning 7B open-source to frontier closed-source. All models exhibit $\text{BR} > 1$ ($1.66$--$4.97\times$). Open-source models use self-extraction; frontier models use cross-model extraction (Mistral-7B extracts FOL from target traces), as closed-source APIs do not expose internal representations suitable for direct symbolic extraction. BR estimates for high-accuracy models ($n_\text{err} < 40$) have wider confidence intervals; Gemini ($n_\text{err} \approx 12$) should be interpreted with particular caution. Process-level similarity ($\kappa_{\text{proc}}$) ranges from $0.25$ (R1-Distill) to $0.79$ (gpt-4o/4.1/Gemini); see Table~\ref{tab:cross-model-process}.
597	
598	\paragraph{ProcessSim definition.}
599	\label{app:process-sim}
600	Process similarity is the mean pairwise cosine similarity of TF-IDF trace representations:
601	\begin{equation}
602	\label{eq:process-sim}
603	\text{ProcessSim}(q) = \frac{2}{K(K{-}1)} \sum_{i < j} \cos(\mathbf{v}_i^q, \mathbf{v}_j^q),
604	\end{equation}
605	where $\mathbf{v}_i^q$ is the TF-IDF vector of trace $t_i$ for question $q$.
606	
607	\paragraph{Process-$\kappa$ gradient.}
608	\label{app:process-gradient}
609	Under cross-model extraction (Mistral-7B extracts FOL from other models' traces), SICA gain decreases monotonically with process-level cosine similarity (Table~\ref{tab:process-gradient}; Spearman $\rho = -1.0$, $n = 5$, one-tailed $p = 0.0083$). Gain requires two conditions: diverse traces (low $\kappa_{\text{proc}}$) \emph{and} substantial self-bias (high BR). R1-Distill-8B satisfies both ($\kappa_{\text{proc}} = 0.248$, $\text{BR} = 2.92$) and gains $+2.45$\,pp; o3 has moderate trace diversity ($\kappa_{\text{proc}} = 0.596$) but near-minimal bias ($\text{BR} = 1.66$, exhibiting a bimodal error pattern: 82\% of error problems have $\text{BR} = \infty$ but low finite-BR), yielding $\Delta = 0$.
610	
611	\begin{table}[h]
612	\centering
613	\small
614	\caption{Process-$\kappa$ gradient under cross-model extraction (Mistral-7B $\rightarrow$ target model traces, FOLIO). $\kappa_{\text{proc}}$: process-level cosine similarity. $\Delta$: SICA $-$ SC (pp). Spearman $\rho(\kappa_{\text{proc}} \rightarrow \Delta) = -1.0$, $p = 0.0083$. $^*$Interim ($n = 95/204$).}
615	\label{tab:process-gradient}
616	\begin{tabular}{@{}lrrr@{}}
617	\toprule
618	Model & $\kappa_{\text{proc}}$ & $\Delta$ (pp) & BR \\
619	\midrule
620	R1-Distill-8B & 0.248 & $+$2.45 & 2.92 \\
621	gpt-5.5 & 0.563 & $+$0.49 & 3.48 \\
622	o3 & 0.596 & 0.00 & 1.66 \\
623	Gemini-2.5-Pro$^*$ & 0.790 & $-$1.05 & 2.79 \\
624	gpt-4.1 & 0.792 & $-$1.47 & 2.70 \\
625	\bottomrule
626	\end{tabular}
627	\end{table}
628	
629	
630	\section{Independence-Accuracy Scatter Plot}
631	\label{app:kappa-scatter}
632	
633	The independence-accuracy scatter plot is presented in Figure~\ref{fig:kappa-accuracy} in the main text.
634	
635	\begin{table}[h]
636	\centering
637	\small
638	\caption{Independence-accuracy trade-off (FOLIO, $n = 204$). Top: aggregation methods on Mistral-7B; bottom: SC across three model families. All families produce $\kappa \geq 0.41$, confirming an architecture-independent ceiling. $\kappa$: Fleiss' kappa on raw answers.}
639	\label{tab:kappa_generalization}
640	\resizebox{\columnwidth}{!}{%
641	\begin{tabular}{@{}llccrr@{}}
642	\toprule
643	Model & Aggregation & $\kappa$ & Eff-$K$ & $K$ & Acc.\ (\%) \\
644	\midrule
645	Mistral-7B & Debate & 0.15 & 4.44 & 12 & 38.24 \\
646	& Diverse-Prompt & 0.40 & 2.21 & 12 & 54.41 \\
647	& Self-Consistency & 0.44 & 2.02 & 10 & 56.86 \\
648	& ICG & 0.47 & 1.93 & 10 & 51.96 \\
649	\addlinespace
650	LLaMA-3.1-8B & Self-Consistency & 0.41 & 2.17 & 12 & 66.18 \\
651	Qwen2.5-7B & Self-Consistency & 0.66 & 1.46 & 12 & 75.98 \\
652	Qwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.98 \\
653	\bottomrule
654	\end{tabular}}
655	\end{table}
656	
657	\paragraph{Trace independence metrics.}
658	\label{app:trace-independence}
659	
660	Table~\ref{tab:independence} reports the full 15-condition breakdown of Fleiss' $\kappa$ and Effective-K at $K = 12$, referenced in \S\ref{sec:effective-k}.
661	
662	\begin{table}[h]
663	\centering
664	\small
665	\caption{Trace independence metrics ($K = 12$, sorted by $\kappa$ descending). $\kappa$: Fleiss' Kappa. $K_{\text{eff}}$: Effective-K (Eq.~\ref{eq:effk}). SC: Self-Consistency baseline. $\Delta$: SICA $-$ SC (pp). {*}\,$p < 0.05$ (uncorrected; BH adj.\ $p = 0.042$, $m{=}6$); positive $\Delta$ values do not reach significance. multi-T $= T \in \{0.3, 0.7, 1.2\}$, 4 traces each. $^{\dag}$\,$\kappa$ computed in an earlier pipeline run; all other rows recomputed from per-problem vote distributions with answer labels normalized to canonical categories.}
666	\label{tab:independence}
667	\resizebox{\columnwidth}{!}{%
668	\begin{tabular}{@{}llccrr@{}}
669	\toprule
670	Model & Condition & $\kappa$ & $K_{\text{eff}}$ & SC (\%) & $\Delta$ (pp) \\
671	\midrule
672	Qwen3 (think) & FOLIO & 0.91$^{\dag}$ & 1.09 & 86.27 & $+$0.49 \\
673	Qwen2.5-14B & LogiQA & 0.82 & 1.20 & 79.00 & $-$1.00 \\
674	Qwen3 & FOLIO & 0.79 & 1.24 & 83.33 & $+$1.47 \\
675	Qwen2.5-14B & FOLIO & 0.74 & 1.31 & 75.98 & $-$0.49 \\
676	Qwen2.5-7B & FOLIO & 0.66$^{\dag}$ & 1.46 & 75.98 & $+$0.49 \\
677	\addlinespace
678	Mistral-7B ($T{=}0.3$) & FOLIO & 0.53$^{\dag}$ & 1.77 & 58.33 & $-$1.47 \\
679	Mistral-7B ($T{=}0.5$) & FOLIO & 0.52$^{\dag}$ & 1.80 & 58.33 & $-$0.98 \\
680	Mistral-7B & LogiQA & 0.51 & 1.81 & 50.00 & $+$1.50 \\
681	Mistral-7B ($T{=}1.0$) & FOLIO & 0.48$^{\dag}$ & 1.91 & 55.39 & 0.00 \\
682	Mistral-7B & FOLIO & 0.46 & 1.98 & 55.88 & $+$3.43 \\
683	Mistral-7B (s123) & FOLIO & 0.46 & 1.99 & 54.41 & $+$2.94 \\
684	Mistral-7B (s456) & FOLIO & 0.46 & 1.99 & 55.88 & 0.00 \\
685	Mistral-7B (s789) & FOLIO & 0.45 & 2.03 & 59.31 & $-$2.45 \\
686	Mistral-7B (multi-T) & FOLIO & 0.43 & 2.11 & 57.84 & 0.00 \\
687	Mistral-7B & PW-D5 & 0.19 & 3.94 & 39.33 & $\mathbf{-2.83}${*} \\
688	\bottomrule
689	\end{tabular}}
690	\end{table}
691	
692	\section{Cross-Model Kappa Analysis}
693	\label{app:cross-model-kappa}
694	
695	Table~\ref{tab:cross_model_kappa} compares trace independence across three model families on the same benchmarks. On FOLIO ($n = 204$), all four models produce $\kappa \geq 0.41$: LLaMA-3.1-8B ($\kappa = 0.41$), Mistral-7B ($\kappa = 0.46$), Qwen2.5-7B ($\kappa = 0.66$), and Qwen2.5-14B ($\kappa = 0.74$). The bottleneck is architecture-independent; no family escapes the correlation floor. Within the Qwen family, $\kappa$ increases from 0.66 (7B) to 0.74 (14B), but Mistral-7B (7B) and LLaMA-3.1-8B (8B) differ by $\Delta\kappa = 0.05$ despite belonging to different families, suggesting that cross-family variation ($\Delta\kappa$ up to 0.20 at similar scale) exceeds within-family scale effects ($\Delta\kappa = 0.08$). Disentangling scale from architecture requires controlled same-family experiments across $\geq$3 scales.
696	
697	\begin{table}[h]
698	\centering
699	\small
700	\caption{Cross-model trace independence ($K = 12$, SC aggregation, FOLIO + ProofWriter). Higher $\kappa$ indicates stronger correlation and lower effective sample size.}
701	\label{tab:cross_model_kappa}
702	\begin{tabular}{@{}llccr@{}}
703	\toprule
704	Model & Dataset & $\kappa$ & $K_{\text{eff}}$ & SC (\%) \\
705	\midrule
706	Qwen2.5-14B & FOLIO & 0.74 & 1.32 & 75.98 \\
707	Qwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 \\
708	Mistral-7B & FOLIO & 0.46 & 1.98 & 55.88 \\
709	LLaMA-3.1-8B & FOLIO & 0.41 & 2.17 & 66.18 \\
710	\addlinespace
711	Qwen2.5-14B & PW-D5 & 0.62 & 1.54 & --- \\
712	Mistral-7B & PW-D5 & 0.19 & 3.94 & 39.33 \\
713	\bottomrule
714	\end{tabular}
715	\end{table}
716	
717	
718	\section{Cross-Model Process-Level Independence}
719	\label{app:cross-model-process}
720	
721	Table~\ref{tab:cross-model-process} extends the process-level independence analysis (\S\ref{sec:process-kappa}) to four model families on FOLIO ($n = 204$). Mean pairwise cosine similarity of TF-IDF trace representations exceeds answer-level $\kappa$ in every family, but the gap is model-strength dependent: it narrows from $0.31$ (LLaMA) and $0.23$ (Mistral) to $0.02$ (Qwen-14B). For weaker models ($r \approx 0$), answer diversity does not reflect reasoning diversity; process-convergent but answer-divergent trace pairs constitute 9.5\% of all pairs on Mistral-7B versus 2.5--3.2\% on other families. For stronger models ($r \approx 0.23$, $p \leq 0.001$), process and answer agreement align, and answer-level $\kappa$ already captures the bottleneck. Process-$\kappa$ thus provides a crucial additional diagnostic specifically for weaker models, where answer-level metrics underestimate reasoning homogeneity.
722	
723	\begin{table}[h]
724	\centering
725	\small
726	\caption{Cross-model process-level independence on FOLIO ($n = 204$, $K = 12$). Mean Cosine: mean pairwise TF-IDF cosine similarity of reasoning traces (Eq.~\ref{eq:process-sim}). Answer $\kappa$: per-question answer agreement. Gap: Cosine $-$ $\kappa$. $r$: Pearson correlation between ProcessSim and answer agreement. Conv.: fraction of process-convergent but answer-divergent trace pairs. {*}{*}\,$p < 0.01$; {*}{*}{*}\,$p < 0.001$.}
727	\label{tab:cross-model-process}
728	\resizebox{\columnwidth}{!}{%
729	\begin{tabular}{@{}lcccrlr@{}}
730	\toprule
731	Model & Mean Cos. & Ans.\ $\kappa$ & Gap & $r$ & $p$ & Conv.\ (\%) \\
732	\midrule
733	Mistral-7B & 0.690 & 0.460 & 0.230 & $-$0.064 & 0.362 & 9.5 \\
734	LLaMA-3.1-8B & 0.759 & 0.447 & 0.312 & $-$0.001 & 0.985 & 3.2 \\
735	Qwen2.5-7B & 0.790 & 0.658 & 0.132 & $+$0.226 & 0.001{*}{*} & 2.8 \\
736	Qwen2.5-14B & 0.766 & 0.744 & 0.022 & $+$0.244 & ${<}$0.001{*}{*}{*} & 2.5 \\
737	\bottomrule
738	\end{tabular}}
739	\end{table}
740	
741	\paragraph{Representation robustness.} Replacing TF-IDF with SBERT embeddings (all-MiniLM-L6-v2) yields ProcessSim $= 0.91$ (vs.\ TF-IDF $0.74$), widening the gap over answer-level $\kappa = 0.55$. The process homogeneity finding is robust to representation choice.
742	
743	\section{Constraint Quality Across Methods}
744	\label{app:constraint-quality}
745	
746	Table~\ref{tab:constraint_quality} compares constraint quality metrics across the three method-level interventions on Mistral-7B FOLIO ($n = 204$). Standard SICA extracts from reasoning traces and achieves the highest parse rate (97.1\%) but also the highest redundancy (42.9\%): nearly half of all constraints are syntactic duplicates across the 12 traces, quantifying the co-sourcing effect of same-model generation. ICG generates constraints directly from the problem statement without trace conditioning. Its lower parse rate (74.6\%) reflects the difficulty of standalone formalization at the 7B scale, though successfully parsed constraints compile at a higher rate (99.4\% vs.\ 96.5\%). ICG produces fewer unique constraints per question (24.9 vs.\ 39.3) with lower redundancy (32.3\%), consistent with the absence of trace-level repetition. Contrastive scoring generates pro and con constraint sets for each candidate answer. The format yields far fewer unique constraints per question (9.2) with zero redundancy (each pro/con pair is structurally distinct), but 62.7\% of constraints are trivially satisfied by Z3; they impose no logical tension and cannot discriminate between candidates. Only 51.0\% of Contrastive constraints are discriminative, compared to 81.4\% for standard SICA and 77.0\% for ICG.
747	
748	\begin{table}[h]
749	\centering
750	\small
751	\caption{Constraint quality metrics across method-level interventions (Mistral-7B, FOLIO, $n = 204$). Parse: fraction of extraction attempts yielding valid JSON. Z3 Compile: fraction compiling to Z3 formulas. Unique/q: mean unique constraints per question. Redundancy: fraction of constraints duplicated across traces. Disc.: fraction discriminative (different Z3 outcome per candidate). Triv.\ Sat.: fraction trivially satisfied (no logical tension).}
752	\label{tab:constraint_quality}
753	\resizebox{\columnwidth}{!}{%
754	\begin{tabular}{@{}l rrrrrr@{}}
755	\toprule
756	Method & Parse & Z3 & Uniq/q & Redund. & Disc. & Triv.\ Sat. \\
757	\midrule
758	Standard SICA & 97.1\% & 96.5\% & 39.3 & 42.9\% & 81.4\% & --- \\
759	ICG & 74.6\% & 99.4\% & 24.9 & 32.3\% & 77.0\% & --- \\
760	Contrastive & 74.0\% & 94.4\% & 9.2 & 0.0\% & 51.0\% & 62.7\% \\
761	\bottomrule
762	\end{tabular}}
763	\end{table}
764	
765	\paragraph{Per-trace constraint yield uniformity.}
766	\label{app:yield-cv}
767	
768	Observation~1 assumes approximately uniform constraint yield per trace within each answer group. We verify this on Mistral-7B FOLIO ($K{=}12$, $n{=}204$). Per-problem yield CV (coefficient of variation across traces within each problem) has median $0.257$ and mean $0.319$; 64.2\% of problems fall below $\text{CV} = 0.3$, and 91.2\% below $0.5$, supporting the uniformity assumption (Figure~\ref{fig:cv-distribution}). Majority-answer traces average $5.61$ constraints and minority-answer traces $6.04$ (Mann--Whitney $p = 5.2 \times 10^{-6}$); correct-answer traces average $5.41$ and incorrect $6.05$ ($p = 5.3 \times 10^{-11}$). Although statistically significant, the absolute difference (${\sim}0.6$ constraints, $< 12\%$) is insufficient to alter the argmax-preservation result: SICA and SC select the same answer on ${>}96\%$ of problems regardless of yield variation. On the 18 problems with CV${>}0.5$, SICA and SC select the same answer on 18/18 (100\%), confirming that yield non-uniformity does not alter the degeneration pattern.
769	
770	\begin{figure}[h]
771	\centering
772	\includegraphics[width=0.8\columnwidth]{figures/fig_cv_distribution.pdf}
773	\caption{Distribution of per-problem within-group CV for constraint yield (Mistral-7B, FOLIO, $n{=}204$). Median CV${=}0.26$ (red dashed); 64\% of problems have CV${\leq}0.3$. Five problems with CV${>}1.0$ (max $3.46$) are clipped for readability.}
774	\label{fig:cv-distribution}
775	\end{figure}
776	
777	\section{Error Categorization of Method-Level Interventions}
778	\label{app:error-categorization}
779	
780	We categorize discordant predictions (where the method and SC disagree) for Debate and Contrastive on FOLIO ($n = 204$) to understand why these interventions degrade accuracy.
781	
782	\paragraph{Debate discordant analysis.} Debate produces 60 correct$\to$wrong flips and 22 wrong$\to$correct flips on FOLIO. Answer-type breakdown reveals that False-labeled questions are most vulnerable: 82.8\% of False questions that SC answers correctly are flipped by Debate, compared to 63.9\% for True and 25.5\% for Unknown. Counterintuitively, failures concentrate not where debate breaks down but where it succeeds most thoroughly: discordant questions average 2.93 effective debate rounds (proposer-critic exchanges producing substantive updates) versus 2.52 for concordant ones. More extensive same-model debate produces more confident but incorrect constraints, consistent with the independence limitation: the critic draws on the same model distribution as the proposer, reinforcing shared biases rather than correcting them.
783	
784	\paragraph{Contrastive discordant analysis.} Contrastive produces 34 discordant questions on FOLIO. All 34 produced non-degenerate scores (both pro and con constraint sets non-empty), compared to 20.1\% degenerate scores in the full sample. This indicates that scoring failures on discordant questions stem from systematic pro-bias rather than missing constraints. Among discordant questions, 97.1\% contain negation words in the problem statement versus 76.5\% in the full sample, suggesting that negation-bearing problems are particularly susceptible to pro-constraint imbalance. The average pro/con score ratio is 1.0 for discordant questions versus 0.68 for the full sample: the method generates balanced-looking scores that mask directional errors.
785	
786	\paragraph{Cross-method overlap.} Of the 79 unique questions on which either method disagrees with SC, only 15 overlap between Debate and Contrastive (Jaccard index $= 0.19$). All 15 shared discordant questions contain negation words. The low overlap confirms that the two methods attack different vulnerability types (Debate through extended same-model argumentation that amplifies confident errors, Contrastive through pro-bias in constraint generation) while sharing a common root cause in correlated same-model voting: both methods rely on the same model's output distribution and cannot introduce genuinely independent signal.
787	
788	
789	\section{TOST Equivalence Tests}
790	\label{app:tost}
791	
792	We apply two one-sided tests (TOST) \citep{lakens2017equivalence} with equivalence margin $\pm 2$\,pp to all 16 non-degenerate SICA--SC comparisons, classifying each condition as \emph{equivalent} (TOST significant), \emph{genuinely different} (McNemar $p < 0.05$ and TOST not significant), or \emph{underpowered} (neither test significant). Four conditions are equivalent, confirming that SICA and SC produce statistically indistinguishable accuracy. Two conditions show genuine differences, both negative: Mistral-7B ProofWriter ($-2.83$\,pp, $p = 0.014$) and Qwen2.5-14B ProofWriter ($-2.50$\,pp, $p = 0.011$). The remaining ten conditions are underpowered, reflecting the limited statistical power at $n{=}200$--$204$ for detecting $|\Delta| \leq 2$\,pp effects.
793	
794	\paragraph{Margin sensitivity.} Table~\ref{tab:tost-sensitivity} shows that the classification is robust across margins: regardless of the chosen margin, no condition shows a significant positive SICA effect.
795	
796	\begin{table}[h]
797	\centering
798	\small
799	\caption{TOST classification sensitivity across equivalence margins (16 non-degenerate conditions).}
800	\label{tab:tost-sensitivity}
801	\begin{tabular}{@{}lccc@{}}
802	\toprule
803	Margin & Equivalent & Different & Underpowered \\
804	\midrule
805	$\pm 1$\,pp & 0 & 2 & 14 \\
806	$\pm 2$\,pp & 4 & 2 & 10 \\
807	$\pm 3$\,pp & 10 & 0 & 6 \\
808	\bottomrule
809	\end{tabular}
810	\end{table}
811	
812	\paragraph{Relative-margin TOST.}
813	\label{app:relative_tost}
814	The absolute $\pm 2$\,pp margin is more stringent at high baselines ($\pm 2.4\%$ relative at SC $= 85\%$) than low ones ($\pm 5.1\%$ at SC $= 39\%$). A relative $\pm 5\%$ of SC margin addresses this asymmetry: 8 conditions are equivalent, 2 genuinely different (both negative), and 6 underpowered. The additional four equivalent conditions are all high-SC ($\geq 75\%$), where the wider relative band captures practical indistinguishability. No condition shows a significant positive effect under either margin.
815	
816	\paragraph{Conditional Correction Ratio data.}
817	\label{app:cil-data}
818	
819	\begin{table}[h]
820	\centering
821	\small
822	\setlength{\tabcolsep}{3pt}
823	\caption{Conditional Correction Ratio across eight verifier--generator conditions. $\text{CCR} > 0$: cross-arch NLI on ProofWriter. $\text{CCR} < 0$: same-model SICA or weak capability gap.}
824	\label{tab:cil_main}
825	\begin{tabular}{@{}llrr@{}}
826	\toprule
827	Generator--Verifier & Dataset & CCR & $\Delta$ (pp) \\
828	\midrule
829	Mistral $\times$ BART-NLI & PW & $+$1.86 & $+$5.17 \\
830	Mistral $\times$ DeBERTa-NLI & PW & $+$1.67 & $+$6.67 \\
831	Mistral $\times$ RoBERTa-NLI & PW & $+$1.42 & $+$4.17 \\
832	\addlinespace
833	Qwen-14B $\times$ DeBERTa-NLI & PW & $-$0.21 & $+$0.33 \\
834	Mistral $\times$ DeBERTa-NLI & FOLIO & $-$0.47 & $+$2.94 \\
835	\addlinespace
836	Mistral $\times$ SICA & FOLIO & $-$2.93 & $+$3.43 \\
837	Qwen-14B $\times$ SICA & PW & $-$4.21 & $-$2.50 \\
838	Mistral $\times$ SICA & PW & $-$4.61 & $-$2.83 \\
839	\bottomrule
840	\end{tabular}
841	\end{table}
842	
843	\paragraph{Disagreement-Routed Cascade details.}
844	\label{app:drc}
845	DRC invokes NLI only when SC consensus falls below threshold $\tau$, avoiding unnecessary verifier calls on high-agreement problems. Gains concentrate on weak generators (SC $< 40\%$), consistent with the capability-gap hypothesis (\S\ref{sec:cross-arch}). Regime-dependent bottleneck analysis appears in Appendix~\ref{app:2x2}.
846	
847	\begin{table}[h]
848	\centering
849	\small
850	\caption{DRC on Mistral-7B ($K{=}12$, DeBERTa-large-mnli, $w{=}3$). $\tau{=}0.7$ recovers 83--90\% of full-combo gain at ${\sim}35\%$ NLI cost across both datasets.}
851	\label{tab:drc}
852	\resizebox{\columnwidth}{!}{%
853	\begin{tabular}{@{}llcccc@{}}
854	\toprule
855	Dataset & Method & Acc.\ & NLI Calls & Cost & Recovery \\
856	\midrule
857	\multirow{3}{*}{PW-D5} & SC only & 39.33\% & 0/600 & 0\% & --- \\
858	& \textbf{DRC $\tau{=}0.7$} & \textbf{45.33\%} & \textbf{207/600} & \textbf{34.5\%} & \textbf{90.0\%} \\
859	& Full combo & 46.00\% & 600/600 & 100\% & 100\% \\
860	\midrule
861	\multirow{3}{*}{FOLIO} & SC only & 55.88\% & 0/204 & 0\% & --- \\
862	& \textbf{DRC $\tau{=}0.7$} & \textbf{58.33\%} & \textbf{71/204} & \textbf{34.8\%} & \textbf{83.3\%} \\
863	& Full combo & 58.82\% & 204/204 & 100\% & 100\% \\
864	\bottomrule
865	\end{tabular}}
866	\end{table}
867	
868	\section{Multi-Verifier NLI Results}
869	\label{app:multi-nli}
870	
871	\begin{table}[h]
872	\centering
873	\small
874	\caption{Cross-architecture NLI combo on ProofWriter depth-5 ($n{=}600$, Mistral-7B traces, SC $= 39.33\%$). Three NLI verifiers $\times$ three weight settings. {*}\,$p < 0.05$;\enspace{**}\,$p < 0.01$;\enspace{***}\,$p < 0.001$ (McNemar).}
875	\label{tab:multi-nli}
876	\setlength{\tabcolsep}{3pt}
877	\begin{tabular}{@{}llrrl@{}}
878	\toprule
879	Verifier & Standalone & $w$ & $\Delta$ (pp) & $p$ \\
880	\midrule
881	DeBERTa-MNLI & 55.00\% & 1 & $+$0.83 & n.s. \\
882	 & & 3 & $+$6.67 & ${<}0.001${***} \\
883	 & & 5 & $+$11.00 & ${<}0.001${***} \\
884	\addlinespace
885	RoBERTa-MNLI & 37.67\% & 1 & $-$0.17 & n.s. \\
886	 & & 3 & $+$4.17 & 0.003{**} \\
887	 & & 5 & $+$4.33 & 0.037{*} \\
888	\addlinespace
889	BART-MNLI & 46.17\% & 1 & 0.00 & n.s. \\
890	 & & 3 & $+$5.17 & ${<}0.001${***} \\
891	 & & 5 & $+$6.33 & 0.003{**} \\
892	\bottomrule
893	\end{tabular}\\[2pt]
894	{\footnotesize All verifiers fine-tuned on MultiNLI. Unknown recall ${<}3.5\%$ across all verifiers.}
895	\end{table}
896	
897	\paragraph{Three-verifier BH correction.}
898	\label{app:3verifier-bh}
899	Table~\ref{tab:3verifier-bh} applies Benjamini--Hochberg correction across all 15 Mistral-7B verifier--weight conditions ($m{=}15$, $\alpha{=}0.05$; distinct from the $m{=}12$ cross-generator analysis in \S\ref{sec:cross-arch}). Ten of 15 conditions remain significant after correction, confirming that multi-verifier NLI gains are robust to multiple testing.
900	
901	\begin{table}[h]
902	\centering
903	\small
904	\caption{BH correction across 3 verifiers $\times$ 5 weights on Mistral-7B ProofWriter ($n{=}600$, $m{=}15$). \checkmark: $p_{\text{BH}} < 0.05$.}
905	\label{tab:3verifier-bh}
906	\setlength{\tabcolsep}{4pt}
907	\begin{tabular}{@{}lcccccc@{}}
908	\toprule
909	Verifier & $w{=}1$ & $w{=}2$ & $w{=}3$ & $w{=}4$ & $w{=}5$ \\
910	\midrule
911	DeBERTa-MNLI & & \checkmark & \checkmark & \checkmark & \checkmark \\
912	RoBERTa-MNLI & & & \checkmark & \checkmark & \checkmark \\
913	BART-MNLI & & & \checkmark & \checkmark & \checkmark \\
914	\bottomrule
915	\end{tabular}\\[2pt]
916	{\footnotesize 10/15 significant at $\alpha{=}0.05$ after BH correction. All $w{=}1$ conditions and RoBERTa $w{=}2$ are non-significant.}
917	\end{table}
918	
919	\section{Capability Gap Data Points}
920	\label{app:capability-gap}
921	
922	Figure~\ref{fig:capability-gap} (main text) visualizes the capability-gap pattern. Table~\ref{tab:cross_generator_nli} reports the controlled cross-generator comparison with DeBERTa-large-mnli on ProofWriter ($n{=}600$). We extend this analysis by pairing Mistral-7B with two additional NLI architectures: BART-large-mnli (46.17\% standalone, combo $+5.17$\,pp, $p = 0.0002$) and RoBERTa-large-mnli (37.67\% standalone, combo $+4.17$\,pp, $p = 0.003$). All three NLI architectures produce significant gains on Mistral-7B at $w \geq 3$.
923	
924	Across all six ProofWriter verifier-generator pairs at $w{=}3$ (three verifiers $\times$ Mistral-7B plus three negative-gap generators $\times$ DeBERTa), combo gain decreases monotonically with the capability gap (Spearman $\rho = 1.0$, exact permutation $p = 0.003$, $n = 6$; however, four of six conditions share the DeBERTa verifier, which may reduce effective degrees of freedom; see Limitations; Figure~\ref{fig:capability-gap}). Significant $w{=}3$ gains are observed only for Mistral-7B (SC 39.33\%, below the verifier); the three above-verifier generators show no significant improvement at any $w$. After BH correction ($m{=}12$), two of twelve conditions survive: Mistral-7B $w{=}3$ (adj.\ $p = 6.78 \times 10^{-5}$) and $w{=}5$ (adj.\ $p = 7.41 \times 10^{-6}$).
925	
926	\paragraph{Robustness check.} Including all nine conditions (three verifiers $\times$ three weight levels on Mistral-7B) yields Spearman $\rho = 0.836$ (exact permutation $p = 0.007$, $n = 9$), confirming that the monotonic trend is robust to the choice of weight parameter.
927	
928	\begin{table}[h]
929	\centering
930	\small
931	\caption{Full cross-generator NLI combo results on ProofWriter depth-5 ($n{=}600$) with Benjamini--Hochberg correction ($m{=}12$, $\alpha{=}0.05$). All conditions use DeBERTa-large-mnli verifier (55.00\% standalone). Two of twelve conditions survive correction (Mistral-7B $w{=}3$ and $w{=}5$). {***}\,$p_{\text{BH}} < 0.001$.}
932	\label{tab:nli-combo-full}
933	\setlength{\tabcolsep}{3.5pt}
934	\resizebox{\columnwidth}{!}{%
935	\begin{tabular}{@{}llrrrrl@{}}
936	\toprule
937	Generator & $w$ & Combo (\%) & $\Delta$ (pp) & $p_{\text{raw}}$ & $p_{\text{BH}}$ & \\
938	\midrule
939	\multirow{3}{*}{\shortstack[l]{Mistral-7B\\{\scriptsize SC\,39.33\%, gap\,$+$15.67}}}
940	  & 1 & 40.17 & $+$0.83 & .359 & .721 & \\
941	  & 3 & 46.00 & $+$6.67 & $1.13{\times}10^{-5}$ & $6.78{\times}10^{-5}$ & {***} \\
942	  & 5 & 50.33 & $+$11.00 & $6.18{\times}10^{-7}$ & $7.41{\times}10^{-6}$ & {***} \\
943	\addlinespace
944	\multirow{3}{*}{\shortstack[l]{LLaMA-3.1-8B\\{\scriptsize SC\,72.50\%, gap\,$-$17.50}}}
945	  & 1 & 73.33 & $+$0.83 & .359 & .721 & \\
946	  & 3 & 73.33 & $+$0.83 & .665 & .886 & \\
947	  & 5 & 72.00 & $-$0.50 & .871 & 1.000 & \\
948	\addlinespace
949	\multirow{3}{*}{\shortstack[l]{Qwen2.5-14B\\{\scriptsize SC\,74.00\%, gap\,$-$19.00}}}
950	  & 1 & 74.17 & $+$0.17 & 1.000 & 1.000 & \\
951	  & 3 & 74.67 & $+$0.67 & .503 & .755 & \\
952	  & 5 & 75.17 & $+$1.17 & .360 & .721 & \\
953	\addlinespace
954	\multirow{3}{*}{\shortstack[l]{Qwen3-14B\\{\scriptsize SC\,85.83\%, gap\,$-$30.83}}}
955	  & 1 & 86.00 & $+$0.17 & 1.000 & 1.000 & \\
956	  & 3 & 86.33 & $+$0.50 & .453 & .755 & \\
957	  & 5 & 87.00 & $+$1.17 & .210 & .721 & \\
958	\bottomrule
959	\end{tabular}}
960	\end{table}
961	
962	\begin{table}[h]
963	\centering
964	\small
965	\caption{Cross-generator NLI combo with BART-large-mnli verifier (46.17\% standalone) on ProofWriter depth-5 ($n{=}600$, $w{=}3$). Only Mistral-7B (below the verifier) gains significantly after BH correction.}
966	\label{tab:bart-combo-full}
967	\resizebox{\columnwidth}{!}{%
968	\begin{tabular}{@{}lccrl@{}}
969	\toprule
970	Generator & SC (\%) & Combo (\%) & $\Delta$ (pp) & $p_{\text{BH}}$ \\
971	\midrule
972	Mistral-7B {\scriptsize (gap $+$6.84)} & 39.33 & 44.50 & $+$5.17 & .003{*} \\
973	LLaMA-3.1-8B {\scriptsize (gap $-$26.33)} & 72.50 & 72.50 & $\pm$0.00 & --- \\
974	Qwen2.5-14B {\scriptsize (gap $-$27.83)} & 74.00 & 75.50 & $+$1.50 & n.s. \\
975	Qwen3-14B {\scriptsize (gap $-$39.66)} & 85.83 & 86.50 & $+$0.67 & n.s. \\
976	\bottomrule
977	\end{tabular}}
978	\end{table}
979	
980	\begin{table}[h]
981	\centering
982	\small
983	\caption{Cross-generator NLI combo with RoBERTa-large-mnli verifier (37.67\% standalone) on ProofWriter depth-5 ($n{=}600$, $w{=}3$). Only Mistral-7B (marginally above the verifier) gains significantly after BH correction.}
984	\label{tab:roberta-combo-full}
985	\resizebox{\columnwidth}{!}{%
986	\begin{tabular}{@{}lccrl@{}}
987	\toprule
988	Generator & SC (\%) & Combo (\%) & $\Delta$ (pp) & $p_{\text{BH}}$ \\
989	\midrule
990	Mistral-7B {\scriptsize (gap $-$1.66)} & 39.33 & 43.50 & $+$4.17 & .016{*} \\
991	LLaMA-3.1-8B {\scriptsize (gap $-$34.83)} & 72.50 & 71.33 & $-$1.17 & n.s. \\
992	Qwen2.5-14B {\scriptsize (gap $-$36.33)} & 74.00 & 74.17 & $+$0.17 & n.s. \\
993	Qwen3-14B {\scriptsize (gap $-$48.16)} & 85.83 & 86.50 & $+$0.67 & n.s. \\
994	\bottomrule
995	\end{tabular}}
996	\end{table}
997	
998	\begin{table}[h]
999	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5876b96e-4384-40f0-a335-df55d8211548",
  "isSidechain": true,
  "promptId": "ed43d146-c225-42c6-832a-351ecc310242",
  "agentId": "af8784ad3137a4fe6",
  "type": "user",
  "uuid": "e9953c31-0dfa-41b0-b4c4-fa4b1e5745d5",
  "sourceToolAssistantUUID": "5876b96e-4384-40f0-a335-df55d8211548",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-26T08:19:24.777Z_

<details open><summary>🔧 Tool call — Read · `toolu_01M7Mm2VNzEy1zPFUUh2Jxta`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "offset": 999,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9953c31-0dfa-41b0-b4c4-fa4b1e5745d5",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
  "requestId": "req_011CbQrRTAZbRotNtG5d7uLv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6083c230-ea46-4917-b9ce-1d8e1df18879",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyQwXuoNctmWzAu172sgc4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15344,
      "cache_read_input_tokens": 61839,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15344
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 61839,
          "cache_creation_input_tokens": 15344,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15344,
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

_source line 32 · 2026-05-26T08:19:25.062Z_

<details><summary>↩ Tool result · `toolu_01M7Mm2VNzEy1zPFUUh2Jxta`</summary>

```text
999	\centering
1000	\small
1001	\caption{NLI combo on FOLIO ($n{=}204$) with DeBERTa-large-mnli verifier (49.51\% standalone). No condition reaches significance; all generators exceed the verifier's standalone accuracy, consistent with the capability-gap pattern. SC baselines match the cross-model ablation traces (Table~\ref{tab:cross-model-ablation}).}
1002	\label{tab:folio-nli-deberta}
1003	\setlength{\tabcolsep}{3pt}
1004	\begin{tabular}{@{}lcccrl@{}}
1005	\toprule
1006	Generator & $w$ & SC (\%) & Combo (\%) & $\Delta$ (pp) & $p$ \\
1007	\midrule
1008	\multirow{3}{*}{Mistral-7B} & 1 & \multirow{3}{*}{55.88} & 56.37 & $+$0.49 & n.s. \\
1009	 & 3 & & 58.82 & $+$2.94 & n.s. \\
1010	 & 5 & & 59.80 & $+$3.92 & n.s. \\
1011	\addlinespace
1012	\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \multirow{3}{*}{66.18} & 65.69 & $-$0.49 & n.s. \\
1013	 & 3 & & 65.20 & $-$0.98 & n.s. \\
1014	 & 5 & & 64.22 & $-$1.96 & n.s. \\
1015	\addlinespace
1016	\multirow{3}{*}{Qwen2.5-14B} & 1 & \multirow{3}{*}{75.98} & 76.96 & $+$0.98 & n.s. \\
1017	 & 3 & & 75.49 & $-$0.49 & n.s. \\
1018	 & 5 & & 73.53 & $-$2.45 & n.s. \\
1019	\addlinespace
1020	\multirow{3}{*}{Qwen3-14B} & 1 & \multirow{3}{*}{83.33} & 83.33 & $\pm$0.00 & n.s. \\
1021	 & 3 & & 84.80 & $+$1.47 & n.s. \\
1022	 & 5 & & 83.33 & $\pm$0.00 & n.s. \\
1023	\bottomrule
1024	\end{tabular}
1025	\end{table}
1026	
1027	\begin{table}[h]
1028	\centering
1029	\small
1030	\caption{NLI combo on FOLIO ($n{=}204$) with BART-large-mnli verifier (47.06\% standalone). No positive improvement reaches significance; for Qwen2.5-14B the weak verifier produces a significant \emph{degradation} at $w{=}5$ ($p{=}.039$), consistent with the capability-gap pattern.}
1031	\label{tab:folio-nli-bart}
1032	\setlength{\tabcolsep}{3pt}
1033	\begin{tabular}{@{}lcccrl@{}}
1034	\toprule
1035	Generator & $w$ & SC (\%) & Combo (\%) & $\Delta$ (pp) & $p$ \\
1036	\midrule
1037	\multirow{3}{*}{Mistral-7B} & 1 & \multirow{3}{*}{55.88} & 54.90 & $-$0.98 & n.s. \\
1038	 & 3 & & 56.37 & $+$0.49 & n.s. \\
1039	 & 5 & & 56.86 & $+$0.98 & n.s. \\
1040	\addlinespace
1041	\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \multirow{3}{*}{66.18} & 67.65 & $+$1.47 & n.s. \\
1042	 & 3 & & 67.65 & $+$1.47 & n.s. \\
1043	 & 5 & & 64.71 & $-$1.47 & n.s. \\
1044	\addlinespace
1045	\multirow{3}{*}{Qwen2.5-14B} & 1 & \multirow{3}{*}{75.98} & 76.47 & $+$0.49 & n.s. \\
1046	 & 3 & & 75.00 & $-$0.98 & n.s. \\
1047	 & 5 & & 72.55 & $-$3.43 & .039{*} \\
1048	\addlinespace
1049	\multirow{3}{*}{Qwen3-14B} & 1 & \multirow{3}{*}{83.33} & 83.33 & $\pm$0.00 & n.s. \\
1050	 & 3 & & 84.31 & $+$0.98 & n.s. \\
1051	 & 5 & & 82.84 & $-$0.49 & n.s. \\
1052	\bottomrule
1053	\end{tabular}
1054	\end{table}
1055	
1056	\begin{table}[h]
1057	\centering
1058	\small
1059	\caption{NLI combo on FOLIO ($n{=}204$) with RoBERTa-large-mnli verifier (46.57\% standalone). Cross-verifier consistency: no positive gain reaches significance, and Qwen2.5-14B shows a significant \emph{degradation} at $w{=}5$ ($p{=}.012$), the same capability-gap signature as BART.}
1060	\label{tab:folio-nli-roberta}
1061	\setlength{\tabcolsep}{3pt}
1062	\begin{tabular}{@{}lcccrl@{}}
1063	\toprule
1064	Generator & $w$ & SC (\%) & Combo (\%) & $\Delta$ (pp) & $p$ \\
1065	\midrule
1066	\multirow{3}{*}{Mistral-7B} & 1 & \multirow{3}{*}{55.88} & 56.37 & $+$0.49 & n.s. \\
1067	 & 3 & & 57.84 & $+$1.96 & n.s. \\
1068	 & 5 & & 58.82 & $+$2.94 & n.s. \\
1069	\addlinespace
1070	\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \multirow{3}{*}{66.18} & 65.69 & $-$0.49 & n.s. \\
1071	 & 3 & & 66.67 & $+$0.49 & n.s. \\
1072	 & 5 & & 64.22 & $-$1.96 & n.s. \\
1073	\addlinespace
1074	\multirow{3}{*}{Qwen2.5-14B} & 1 & \multirow{3}{*}{75.98} & 75.98 & $\pm$0.00 & n.s. \\
1075	 & 3 & & 75.00 & $-$0.98 & n.s. \\
1076	 & 5 & & 71.57 & $-$4.41 & .012{*} \\
1077	\addlinespace
1078	\multirow{3}{*}{Qwen3-14B} & 1 & \multirow{3}{*}{83.33} & 83.33 & $\pm$0.00 & n.s. \\
1079	 & 3 & & 84.31 & $+$0.98 & n.s. \\
1080	 & 5 & & 83.82 & $+$0.49 & n.s. \\
1081	\bottomrule
1082	\end{tabular}
1083	\end{table}
1084	
1085	\begin{table}[h]
1086	\centering
1087	\small
1088	\caption{NLI combo on LogiQA ($n{=}200$) with DeBERTa-large-mnli verifier (26.50\% standalone, near the 25\% random baseline for 4-way classification). No condition reaches significance.}
1089	\label{tab:logiqa-nli-deberta}
1090	\setlength{\tabcolsep}{3pt}
1091	\begin{tabular}{@{}lcccrl@{}}
1092	\toprule
1093	Generator & $w$ & SC (\%) & Combo (\%) & $\Delta$ (pp) & $p$ \\
1094	\midrule
1095	\multirow{3}{*}{Mistral-7B} & 1 & \multirow{3}{*}{53.00} & 54.00 & $+$1.00 & n.s. \\
1096	 & 3 & & 54.00 & $+$1.00 & n.s. \\
1097	 & 5 & & 53.50 & $+$0.50 & n.s. \\
1098	\addlinespace
1099	\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \multirow{3}{*}{59.50} & 58.50 & $-$1.00 & n.s. \\
1100	 & 3 & & 58.00 & $-$1.50 & n.s. \\
1101	 & 5 & & 58.00 & $-$1.50 & n.s. \\
1102	\addlinespace
1103	\multirow{3}{*}{Qwen2.5-14B} & 1 & \multirow{3}{*}{79.00} & 78.50 & $-$0.50 & n.s. \\
1104	 & 3 & & 78.00 & $-$1.00 & n.s. \\
1105	 & 5 & & 78.00 & $-$1.00 & n.s. \\
1106	\addlinespace
1107	\multirow{3}{*}{Qwen3-14B} & 1 & \multirow{3}{*}{81.00} & 81.00 & $\pm$0.00 & n.s. \\
1108	 & 3 & & 80.50 & $-$0.50 & n.s. \\
1109	 & 5 & & 80.50 & $-$0.50 & n.s. \\
1110	\bottomrule
1111	\end{tabular}
1112	\end{table}
1113	
1114	\begin{table}[h]
1115	\centering
1116	\small
1117	\caption{NLI combo on LogiQA ($n{=}200$) with BART-large-mnli verifier (33.00\% standalone). Near-random NLI accuracy yields no significant combo improvements.}
1118	\label{tab:logiqa-nli-bart}
1119	\setlength{\tabcolsep}{3pt}
1120	\begin{tabular}{@{}lcccrl@{}}
1121	\toprule
1122	Generator & $w$ & SC (\%) & Combo (\%) & $\Delta$ (pp) & $p$ \\
1123	\midrule
1124	\multirow{3}{*}{Mistral-7B} & 1 & \multirow{3}{*}{53.00} & 53.50 & $+$0.50 & n.s. \\
1125	 & 3 & & 53.50 & $+$0.50 & n.s. \\
1126	 & 5 & & 52.50 & $-$0.50 & n.s. \\
1127	\addlinespace
1128	\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \multirow{3}{*}{59.50} & 59.50 & $\pm$0.00 & n.s. \\
1129	 & 3 & & 59.50 & $\pm$0.00 & n.s. \\
1130	 & 5 & & 58.50 & $-$1.00 & n.s. \\
1131	\addlinespace
1132	\multirow{3}{*}{Qwen2.5-14B} & 1 & \multirow{3}{*}{79.00} & 78.50 & $-$0.50 & n.s. \\
1133	 & 3 & & 78.50 & $-$0.50 & n.s. \\
1134	 & 5 & & 77.50 & $-$1.50 & n.s. \\
1135	\addlinespace
1136	\multirow{3}{*}{Qwen3-14B} & 1 & \multirow{3}{*}{81.00} & 81.50 & $+$0.50 & n.s. \\
1137	 & 3 & & 81.00 & $\pm$0.00 & n.s. \\
1138	 & 5 & & 81.50 & $+$0.50 & n.s. \\
1139	\bottomrule
1140	\end{tabular}
1141	\end{table}
1142	
1143	\begin{table}[h]
1144	\centering
1145	\small
1146	\caption{NLI combo on LogiQA ($n{=}200$) with RoBERTa-large-mnli verifier (31.50\% standalone). All three NLI verifiers produce the same null result on LogiQA.}
1147	\label{tab:logiqa-nli-roberta}
1148	\setlength{\tabcolsep}{3pt}
1149	\begin{tabular}{@{}lcccrl@{}}
1150	\toprule
1151	Generator & $w$ & SC (\%) & Combo (\%) & $\Delta$ (pp) & $p$ \\
1152	\midrule
1153	\multirow{3}{*}{Mistral-7B} & 1 & \multirow{3}{*}{53.00} & 54.00 & $+$1.00 & n.s. \\
1154	 & 3 & & 53.50 & $+$0.50 & n.s. \\
1155	 & 5 & & 53.50 & $+$0.50 & n.s. \\
1156	\addlinespace
1157	\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \multirow{3}{*}{59.50} & 59.00 & $-$0.50 & n.s. \\
1158	 & 3 & & 58.50 & $-$1.00 & n.s. \\
1159	 & 5 & & 58.50 & $-$1.00 & n.s. \\
1160	\addlinespace
1161	\multirow{3}{*}{Qwen2.5-14B} & 1 & \multirow{3}{*}{79.00} & 78.50 & $-$0.50 & n.s. \\
1162	 & 3 & & 78.50 & $-$0.50 & n.s. \\
1163	 & 5 & & 77.50 & $-$1.50 & n.s. \\
1164	\addlinespace
1165	\multirow{3}{*}{Qwen3-14B} & 1 & \multirow{3}{*}{81.00} & 81.00 & $\pm$0.00 & n.s. \\
1166	 & 3 & & 80.50 & $-$0.50 & n.s. \\
1167	 & 5 & & 81.00 & $\pm$0.00 & n.s. \\
1168	\bottomrule
1169	\end{tabular}
1170	\end{table}
1171	
1172	\paragraph{Domain-adapted verifier results.}
1173	\label{app:finetuned-nli}
1174	
1175	\begin{table}[h]
1176	\centering
1177	\small
1178	\caption{Domain-adapted NLI combo on ProofWriter depth-5 ($n{=}600$). DeBERTa-large fine-tuned on ProofWriter OWA (99.67\% standalone). All $p < 0.0001$. Complementarity: ratio of NLI-correct$\cap$SC-incorrect to SC-correct$\cap$NLI-incorrect.}
1179	\label{tab:finetuned-nli}
1180	\setlength{\tabcolsep}{3.5pt}
1181	\begin{tabular}{@{}lrrrrc@{}}
1182	\toprule
1183	Generator & $w$ & Combo (\%) & $\Delta$ (pp) & Compl.\ ratio \\
1184	\midrule
1185	\multirow{3}{*}{\shortstack[l]{Mistral-7B\\{\scriptsize SC\,39.33\%}}}
1186	  & 1 & 42.17 & $+$2.83 & \multirow{3}{*}{364:2} \\
1187	  & 3 & 52.00 & $+$12.67 & \\
1188	  & 5 & 65.50 & $+$26.17 & \\
1189	\addlinespace
1190	\multirow{3}{*}{\shortstack[l]{LLaMA-3.1-8B\\{\scriptsize SC\,72.50\%}}}
1191	  & 1 & 76.00 & $+$3.50 & \multirow{3}{*}{164:1} \\
1192	  & 3 & 84.17 & $+$11.67 & \\
1193	  & 5 & 91.67 & $+$19.17 & \\
1194	\bottomrule
1195	\end{tabular}
1196	\end{table}
1197	
1198	\paragraph{Cross-model voting ablation.}
1199	\label{app:cross-model-ablation}
1200	
1201	\begin{table}[h]
1202	\centering
1203	\small
1204	\caption{Cross-model voting ablation ($w \in \{3,5\}$). ``Cross LLM'' replaces the NLI verifier with a second LLM's SC votes at weight $w$; ``NLI'' uses DeBERTa-large-mnli (55.00\% standalone) at $w{=}3$. On ProofWriter, cross-model SC with a weak voter (Mistral-7B) degrades all strong generators (worsening at higher $w$), while NLI combo does not, indicating that structural independence, not merely model diversity, drives the escape.}
1205	\label{tab:cross-model-ablation}
1206	\setlength{\tabcolsep}{3pt}
1207	\resizebox{\columnwidth}{!}{%
1208	\begin{tabular}{@{}llcccrl@{}}
1209	\toprule
1210	Generator & Voter/Verifier & $w$ & SC (\%) & Combo (\%) & $\Delta$ (pp) & $p$ \\
1211	\midrule
1212	\multicolumn{7}{@{}l}{\textit{ProofWriter ($n{=}600$)}} \\
1213	\addlinespace
1214	\multirow{3}{*}{Mistral-7B}
1215	  & \multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 39.33 & 47.67 & $+$8.33 & $<$.001 \\
1216	  & & 5 & 39.33 & 55.33 & $+$16.00 & $<$.001 \\
1217	  & DeBERTa NLI & 3 & 39.33 & 46.00 & $+$6.67 & $<$.001 \\
1218	\addlinespace
1219	\multirow{5}{*}{LLaMA-3.1-8B}
1220	  & \multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 72.50 & 75.33 & $+$2.83 & .060 \\
1221	  & & 5 & 72.50 & 75.33 & $+$2.83 & .125 \\
1222	  & \multirow{2}{*}{Mistral-7B (cross)} & 3 & 72.50 & 63.17 & $-$9.33 & $<$.001 \\
1223	  & & 5 & 72.50 & 56.17 & $-$16.33 & $<$.001 \\
1224	  & DeBERTa NLI & 3 & 72.50 & 73.33 & $+$0.83 & .665 \\
1225	\addlinespace
1226	\multirow{5}{*}{Qwen2.5-14B}
1227	  & \multirow{2}{*}{LLaMA-8B (cross)} & 3 & 74.00 & 74.50 & $+$0.50 & .664 \\
1228	  & & 5 & 74.00 & 76.00 & $+$2.00 & .096 \\
1229	  & \multirow{2}{*}{Mistral-7B (cross)} & 3 & 74.00 & 71.67 & $-$2.33 & .020 \\
1230	  & & 5 & 74.00 & 69.67 & $-$4.33 & .002 \\
1231	  & DeBERTa NLI & 3 & 74.00 & 74.67 & $+$0.67 & .503 \\
1232	\addlinespace
1233	\multirow{5}{*}{Qwen3-14B}
1234	  & \multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 85.83 & 84.67 & $-$1.17 & .143 \\
1235	  & & 5 & 85.83 & 83.33 & $-$2.50 & .006 \\
1236	  & \multirow{2}{*}{Mistral-7B (cross)} & 3 & 85.83 & 83.17 & $-$2.67 & .002 \\
1237	  & & 5 & 85.83 & 81.17 & $-$4.67 & $<$.001 \\
1238	  & DeBERTa NLI & 3 & 85.83 & 86.33 & $+$0.50 & .453 \\
1239	\midrule
1240	\multicolumn{7}{@{}l}{\textit{FOLIO ($n{=}204$)}} \\
1241	\addlinespace
1242	\multirow{3}{*}{Mistral-7B}
1243	  & \multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 55.88 & 63.73 & $+$7.84 & .002 \\
1244	  & & 5 & 55.88 & 68.63 & $+$12.75 & $<$.001 \\
1245	  & DeBERTa NLI & 3 & 55.88 & 58.82 & $+$2.94 & .210 \\
1246	\addlinespace
1247	\multirow{3}{*}{LLaMA-3.1-8B}
1248	  & \multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 66.18 & 70.10 & $+$3.92 & .134 \\
1249	  & & 5 & 66.18 & 73.53 & $+$7.35 & .014 \\
1250	  & DeBERTa NLI & 3 & 66.18 & 65.20 & $-$0.98 & .824 \\
1251	\addlinespace
1252	\multirow{3}{*}{Qwen2.5-14B}
1253	  & \multirow{2}{*}{LLaMA-8B (cross)} & 3 & 75.98 & 76.96 & $+$0.98 & .727 \\
1254	  & & 5 & 75.98 & 79.41 & $+$3.43 & .143 \\
1255	  & DeBERTa NLI & 3 & 75.98 & 75.49 & $-$0.49 & 1.00 \\
1256	\addlinespace
1257	\multirow{3}{*}{Qwen3-14B}
1258	  & \multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 83.33 & 85.78 & $+$2.45 & .125 \\
1259	  & & 5 & 83.33 & 86.76 & $+$3.43 & .039 \\
1260	  & DeBERTa NLI & 3 & 83.33 & 84.80 & $+$1.47 & .250 \\
1261	\bottomrule
1262	\end{tabular}}
1263	\end{table}
1264	
1265	\paragraph{Generator$\times$Extractor 2$\times$2 Matrix.}
1266	\label{app:2x2}
1267	
1268	Table~\ref{tab:2x2-folio} reports the full $2{\times}2$ generator${\times}$extractor matrix on FOLIO ($n{=}204$). The generator dominates accuracy (row difference ${\sim}25$\,pp vs.\ column difference ${\sim}3$\,pp), contrasting with ProofWriter where the extractor dominates ($\Delta$ range ${\pm}40$--$50$\,pp). Cross-extractor McNemar tests: Mistral-7B gen, $\Delta = +2.94$\,pp, $p = 0.143$ (n.s.); Qwen3-14B gen, $\Delta = +2.94$\,pp, $p = 0.021$ (statistically significant but practically small: 6/204 problems changed). The identical net $\Delta$ is coincidental; the two generators have different discordant-pair distributions that happen to yield the same net advantage. BR $> 1$ in all eight cells across both datasets (range $1.94$--$2.70$), confirming SCB universality under cross-model extraction.
1269	
1270	\begin{table}[h]
1271	\centering
1272	\small
1273	\caption{FOLIO $2{\times}2$ generator${\times}$extractor matrix ($n{=}204$). SC: Self-Consistency baseline. $\kappa$: answer-level Fleiss' kappa. BR: bias ratio.}
1274	\label{tab:2x2-folio}
1275	\setlength{\tabcolsep}{3pt}
1276	\begin{tabular}{@{}llcccc@{}}
1277	\toprule
1278	Generator & Extractor & SC (\%) & SICA (\%) & $\Delta$ (pp) & BR \\
1279	\midrule
1280	\multirow{2}{*}{\shortstack[l]{Mistral-7B\\{\scriptsize $\kappa{=}0.46$}}}
1281	  & Mistral & 55.88 & 56.86 & $+$0.98 & 2.70 \\
1282	  & Qwen3 & 55.88 & 59.80 & $+$3.92 & 1.94 \\
1283	\addlinespace
1284	\multirow{2}{*}{\shortstack[l]{Qwen3-14B\\{\scriptsize $\kappa{=}0.79$}}}
1285	  & Qwen3 & 83.33 & 84.80 & $+$1.47 & 2.35 \\
1286	  & Mistral & 83.33 & 81.86 & $-$1.47 & 2.66 \\
1287	\bottomrule
1288	\end{tabular}
1289	\end{table}
1290	
1291	\section{Single-Trace and Aggregation Statistics}
1292	\label{app:single-trace}
1293	
1294	\begin{table}[h]
1295	\centering
1296	\small
1297	\caption{Single-trace accuracy (mean $\pm$ std over $K{=}12$ traces) and SC@12 majority vote on FOLIO ($n{=}204$). Aggregation gain = SC@12 $-$ single-trace mean. SC@12 uses alphabetical tiebreaking (consistent with Table~\ref{tab:main_results}).}
1298	\label{tab:single-trace-stats}
1299	\resizebox{\columnwidth}{!}{%
1300	\begin{tabular}{@{}lrrrr@{}}
1301	\toprule
1302	Model & Single (\%) & Std & SC@12 (\%) & Gain (pp) \\
1303	\midrule
1304	Mistral-7B & 46.41 & 2.80 & 55.88 & $+$9.47 \\
1305	Qwen3-14B & 79.37 & 1.98 & 84.80 & $+$5.43 \\
1306	Qwen3-14B (think) & 85.42 & 0.99 & 86.27 & $+$0.86 \\
1307	\bottomrule
1308	\end{tabular}}\\[2pt]
1309	{\footnotesize Inter-trace standard deviation shrinks $2.8\times$ from Mistral-7B to Qwen3-14B thinking mode, reflecting the diversity compression that underlies the aggregation ceiling (\S\ref{sec:cross-arch}).}
1310	\end{table}
1311	
1312	\paragraph{Extraction temperature sensitivity.}
1313	\label{app:text-sensitivity}
1314	
1315	\begin{table}[h]
1316	\centering
1317	\small
1318	\caption{Effect of extraction temperature $T_{\text{ext}}$ on SICA accuracy (Mistral-7B, FOLIO $n{=}204$). $^\dagger$\,Uses a different trace set (SC $= 54.41\%$); all other conditions share the same traces (SC $= 55.88\%$).}
1319	\label{tab:text-sensitivity}
1320	\begin{tabular}{@{}cccr@{}}
1321	\toprule
1322	$T_{\text{ext}}$ & SICA (\%) & $\Delta$ vs.\ SC (pp) & Avg.\ \#Constr. \\
1323	\midrule
1324	0.1 & 57.35 & $+$1.47 & 69.3 \\
1325	$0.3^\dagger$ & 59.31 & $+$3.43 & 68.8 \\
1326	0.5 & 56.37 & $+$0.49 & 68.2 \\
1327	0.7 & 53.43 & $-$2.45 & 67.3 \\
1328	1.0 & 55.39 & $-$0.49 & 65.2 \\
1329	\bottomrule
1330	\end{tabular}
1331	\end{table}
1332	
1333	Controlling for the trace set (excluding $T_{\text{ext}} = 0.3$, which uses a different seed), all conditions yield $\Delta \leq +1.47$\,pp (n.s.), indicating that extraction temperature has no significant effect on SICA accuracy. This supports the structural nature of symbolic confirmation bias: the bottleneck is what gets extracted, not the temperature at which extraction occurs.
1334	
1335	\paragraph{Multi-seed replication.}
1336	\label{app:multi-seed}
1337	
1338	\begin{table}[t!]
1339	\centering
1340	\small
1341	\caption{Multi-seed replication results across six model$\times$dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\times$FOLIO shows directionally unstable $\Delta$ ($+0.16 \pm 2.70$\,pp). Mistral-7B, LLaMA-8B, and Qwen2.5-14B show consistently negative $\Delta$ on ProofWriter ($p < .001$ for LLaMA-8B and Mistral-7B); Qwen3-14B shows negligible mixed-sign $\Delta$ ($+0.92 \pm 1.14$\,pp, all n.s.), consistent with its high SC baseline minimizing correctable errors (\S\ref{sec:discussion}).}
1342	\label{tab:multi-seed}
1343	\resizebox{\columnwidth}{!}{%
1344	\begin{tabular}{@{}lrrrr@{}}
1345	\toprule
1346	Seed & SC (\%) & SICA (\%) & $\Delta$ (pp) \\
1347	\midrule
1348	\multicolumn{4}{@{}l}{\textit{Mistral-7B $\times$ FOLIO ($n{=}204$)\textsuperscript{a}}} \\
1349	123 & 54.41 & 57.35 & $+$2.94 \\
1350	456 & 55.88 & 55.88 & 0.00 \\
1351	789 & 59.31 & 56.86 & $-$2.45 \\
1352	\midrule
1353	Mean $\pm$ SD & 56.53 $\pm$ 2.51 & 56.70 $\pm$ 0.75 & $+$0.16 $\pm$ 2.70 \\
1354	\midrule
1355	\multicolumn{4}{@{}l}{\textit{Qwen2.5-14B $\times$ FOLIO ($n{=}204$)}} \\
1356	42 & 77.50 & 75.49 & $-$2.01 \\
1357	123 & 74.51 & 73.04 & $-$1.47 \\
1358	456 & 74.02 & 74.02 & 0.00 \\
1359	789 & 74.02 & 72.55 & $-$1.47 \\
1360	\midrule
1361	Mean $\pm$ SD & 75.01 $\pm$ 1.67 & 73.78 $\pm$ 1.30 & $-$1.24 $\pm$ 0.86 \\
1362	\midrule
1363	\multicolumn{4}{@{}l}{\textit{Mistral-7B $\times$ ProofWriter ($n{=}600$)}} \\
1364	42  & 39.33 & 36.50 & $-$2.83 \\
1365	123 & 40.83 & 37.50 & $-$3.33 \\
1366	456 & 39.83 & 38.50 & $-$1.33 \\
1367	789 & 38.83 & 37.17 & $-$1.67 \\
1368	\midrule
1369	Mean $\pm$ SD & 39.70 $\pm$ 0.85 & 37.42 $\pm$ 0.83 & $-$2.29 $\pm$ 0.95 \\
1370	\midrule
1371	\multicolumn{4}{@{}l}{\textit{LLaMA-3.1-8B $\times$ ProofWriter ($n{=}600$)}} \\
1372	42  & 72.50 & 65.00 & $-$7.50 \\
1373	123 & 71.33 & 64.00 & $-$7.33 \\
1374	456 & 71.67 & 66.17 & $-$5.50 \\
1375	789 & 71.17 & 66.50 & $-$4.67 \\
1376	\midrule
1377	Mean $\pm$ SD & 71.67 $\pm$ 0.59 & 65.42 $\pm$ 1.14 & $-$6.25 $\pm$ 1.34 \\
1378	\midrule
1379	\multicolumn{4}{@{}l}{\textit{Qwen2.5-14B $\times$ ProofWriter ($n{=}600$)}} \\
1380	42  & 74.00 & 71.50 & $-$2.50 \\
1381	123 & 72.33 & 70.83 & $-$1.50 \\
1382	456 & 73.00 & 72.17 & $-$0.83 \\
1383	789 & 73.50 & 71.50 & $-$2.00 \\
1384	\midrule
1385	Mean $\pm$ SD & 73.21 $\pm$ 0.71 & 71.50 $\pm$ 0.55 & $-$1.71 $\pm$ 0.71 \\
1386	\midrule
1387	\multicolumn{4}{@{}l}{\textit{Qwen3-14B $\times$ ProofWriter ($n{=}600$)}} \\
1388	42  & 85.83 & 85.67 & $-$0.17 \\
1389	123 & 85.17 & 86.50 & $+$1.33 \\
1390	456 & 84.50 & 86.83 & $+$2.33 \\
1391	789 & 85.50 & 85.67 & $+$0.17 \\
1392	\midrule
1393	Mean $\pm$ SD & 85.25 $\pm$ 0.57 & 86.17 $\pm$ 0.59 & $+$0.92 $\pm$ 1.14 \\
1394	\bottomrule
1395	\end{tabular}}
1396	\vspace{2pt}
1397	{\footnotesize \textsuperscript{a}Original baseline used no fixed seed and is excluded from seed statistics.}
1398	\end{table}
1399	
1400	On ProofWriter, all twelve Mistral-7B, LLaMA-8B, and Qwen2.5-14B seeds yield negative $\Delta$ (range $-0.83$ to $-7.50$\,pp), with all LLaMA-8B McNemar tests reaching $p < .001$. The results reveal a capability-dependent gradient: LLaMA-8B $\Delta{=}-6.25$ $\to$ Mistral-7B $\Delta{=}-2.29$ $\to$ Qwen2.5-14B $\Delta{=}-1.71$ $\to$ Qwen3-14B $\Delta{=}+0.92$\,pp. Qwen3-14B is the sole exception: its 4-seed mean $\Delta$ is slightly positive ($+0.92 \pm 1.14$\,pp, all n.s.; 95\% CI includes zero), reflecting the capability-modulated pattern discussed in \S\ref{sec:discussion}: models with SC baselines above 85\% leave few correctable errors for SICA to exploit. The consistency across seeds confirms that the sign of $\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity. SC ties are broken alphabetically; across 2{,}400 ProofWriter problems ($4 \times 600$), zero SC--SICA answer differences were attributable to tiebreaking, confirming that ties are too rare at $\kappa \approx 0.78$ to affect $\Delta$.
1401	
1402	\subsection{Sub-population Analysis}
1403	\label{app:subpopulation}
1404	
1405	\begin{table}[t!]
1406	\centering
1407	\small
1408	\caption{SICA vs.\ SC accuracy by gold-label type (Mistral-7B). Corrected SC baseline uses alphabetical tiebreaking. $\Delta$\,pp = SICA $-$ SC. $p$-values from exact McNemar test (two-sided).}
1409	\label{tab:subpop-answer-type}
1410	\resizebox{\columnwidth}{!}{%
1411	\begin{tabular}{ll rrr rr}
1412	\toprule
1413	\textbf{Dataset} & \textbf{Label} & $n$ & \textbf{SC} & \textbf{SICA} & $\Delta$\,pp & $p$ \\
1414	\midrule
1415	\multirow{4}{*}{FOLIO-204}
1416	 & True    &  72 & 56.9 & 62.5 & $+$5.6 & .125 \\
1417	 & False   &  63 & 42.9 & 42.9 & $\pm$0.0 & 1.0\hphantom{00} \\
1418	 & Unknown &  69 & 66.7 & 71.0 & $+$4.3 & .250 \\
1419	 & \textit{Overall} & 204 & 55.9 & 59.3 & $+$3.4 & .092 \\
1420	\midrule
1421	\multirow{4}{*}{PW-600}
1422	 & True    & 200 &  8.5 &  6.0 & $-$2.5 & .063 \\
1423	 & False   & 200 & 19.5 & 14.5 & $-$5.0 & .076 \\
1424	 & Unknown & 200 & 90.0 & 89.0 & $-$1.0 & .774 \\
1425	 & \textit{Overall} & 600 & 39.3 & 36.5 & $-$2.8 & .014\rlap{*} \\
1426	\bottomrule
1427	\end{tabular}}
1428	\end{table}
1429	
1430	\begin{table}[t!]
1431	\centering
1432	\small
1433	\caption{SICA vs.\ SC accuracy by extracted constraint count tertile (Mistral-7B). Corrected SC baseline (alphabetical tiebreaking). Constraint counts are unique deduplicated constraints per problem.}
1434	\label{tab:subpop-constraint}
1435	\resizebox{\columnwidth}{!}{%
1436	\begin{tabular}{ll rr rrr rr}
1437	\toprule
1438	\textbf{Dataset} & \textbf{Tertile} & $n$ & $\bar{c}$ & \textbf{SC} & \textbf{SICA} & $\Delta$\,pp & $p$ \\
1439	\midrule
1440	\multirow{3}{*}{FOLIO-204}
1441	 & Low \scriptsize{[0--32]}   &  74 & 21.7 & 62.2 & 63.5 & $+$1.4 & 1.0\hphantom{00} \\
1442	 & Mid \scriptsize{[33--47]}  &  64 & 39.7 & 50.0 & 59.4 & $+$9.4 & .031\rlap{*} \\
1443	 & High \scriptsize{[48--83]} &  66 & 58.7 & 54.5 & 54.5 & $\pm$0.0 & 1.0\hphantom{00} \\
1444	\midrule
1445	\multirow{3}{*}{PW-600}
1446	 & Low \scriptsize{[0--39]}   & 212 & 28.8 & 43.9 & 39.6 & $-$4.3 & .078 \\
1447	 & Mid \scriptsize{[40--52]}  & 196 & 45.8 & 40.8 & 37.2 & $-$3.6 & .143 \\
1448	 & High \scriptsize{[53--99]} & 192 & 63.7 & 32.8 & 32.3 & $-$0.5 & 1.0\hphantom{00} \\
1449	\bottomrule
1450	\end{tabular}}
1451	\end{table}
1452	
1453	On FOLIO-204 with the corrected SC baseline (alphabetical tiebreaking), SICA improves over SC by $+$3.4\,pp overall (55.9\% $\to$ 59.3\%), though the aggregate McNemar test is marginally non-significant ($p{=}.092$).
1454	The gain concentrates in the mid-constraint tertile ($+$9.4\,pp, $p{=}.031$), where sufficient symbolic evidence exists for MaxSAT to meaningfully re-rank answers; in the low- and high-constraint groups the methods perform comparably.
1455	On ProofWriter-600, SICA shows a small uniform degradation consistent with the main results, attenuating in the high-constraint tertile ($\Delta{=}{-}0.5$\,pp, $p{=}1.0$).
1456	We note that with six subgroup tests, one significant result at $\alpha{=}0.05$ is expected by chance; the mid-constraint finding should be interpreted as exploratory.
1457	
1458	\paragraph{Individual intervention significance.}
1459	\label{app:intervention-individual}
1460	Of the 27 training-free remediation strategies (Figure~\ref{fig:interventions-summary}), the two largest positive effects are Cross-model Qwen3$\to$Mistral ($+0.98$\,pp) and Generational ($+0.49$\,pp); neither approaches statistical significance ($p > 0.5$ for both). The largest negative effects are LLM-Debate ($-18.6$\,pp, $p < 0.001$) and Contrastive Scoring ($-9.3$\,pp, $p < 0.001$). After BH correction across all 27 comparisons, only these two negative results remain significant. No strategy produces a significant positive effect under any correction procedure.
1461	
1462	\section{Extended Discussion}
1463	\label{app:extended-discussion}
1464	\label{app:limitations-extended}
1465	\label{app:per-trace-separation}
1466	
1467	\paragraph{Per-trace separation analysis.}
1468	On Mistral-7B FOLIO (166/204 non-unanimous problems), per-trace constraint density is balanced between majority and minority answer groups ($6.0$ vs.\ $5.9$ constraints/trace) and MAX-SAT exclusion rates are comparable ($0.185$ vs.\ $0.172$); the extraction function $f$ produces constraints of equal quality regardless of answer group (\emph{extraction neutrality}).
1469	The majority of unique formulas (${\sim}$74\%) are minority-exclusive, yet ${\sim}$26\% are shared across answer groups; under source-attribution, shared formulas vote for each side in proportion to trace count, providing zero discriminative signal (\emph{formula undirectedness}). Full semantic direction testing is precluded by variable isolation (56.4\% zero overlap).
1470	Each constraint votes exclusively for its source trace's answer; volume amplification is ${\approx}1.0\times$. On 82.4\% of problems where the minority vote is correct, SICA still follows the majority (correction rate 17.6\%). SCB is therefore a transparency property: source-attribution scoring faithfully transmits the CoT trace distribution into verification without adding or removing information.
1471	
1472	\paragraph{Answer-leakage controls.}
1473	Two controls rule out answer contamination: (1)~BR is uniform across reasoning steps (Fisher $p = 0.71$); (2)~removing answer sentences before extraction yields no BR decrease (Wilcoxon $p \geq 0.12$) despite accuracy loss (McNemar $p < 0.013$). The bias reflects a distributional prior embedded throughout reasoning.
1474	
1475	\paragraph{SCB versus CoT unfaithfulness.}
1476	SCB is distinct from CoT unfaithfulness \citep{turpin2023language} and CoT-level confirmation bias \citep{wan2025unveiling, jhaveri2026failing}. CoT unfaithfulness concerns whether stated reasoning reflects actual computation; SCB concerns whether \emph{self-extracted formal constraints} mirror the model's answer distribution. Even if traces were perfectly faithful, self-extraction would still inherit the distributional bias: the constraint $P(\text{answer\_A})$ reflects vote share, not logical validity. The shuffle control (\S\ref{sec:confirmation-bias}) confirms this: randomizing constraint--answer associations preserves BR, showing the bias is in the trace-count distribution, not in extraction-specific errors. However, if traces are unfaithful, the mirage may be worse than our measurements suggest, because constraints would reflect not the model's reasoning but its post-hoc rationalization.
1477	
1478	\paragraph{Implications for neuro-symbolic practitioners.}
1479	Our results do not imply that neuro-symbolic methods are inherently flawed; they imply that \emph{self-extracted} constraints cannot provide independent verification. The key distinction is \emph{when} formalization occurs relative to answer generation. Specification-generation approaches (e.g., SatLM \citep{ye2024satlm}, Logic-LM \citep{pan2023logiclm}) formalize the problem \emph{before} generating candidate answers, avoiding the extraction bottleneck; SatLM's success confirms that the formal verification mechanism is sound when constraints are independently derived. Trace-extraction (this work) operates post-hoc on reasoning traces that already contain candidates, inheriting the distributional prior that generates SCB. When post-hoc verification is unavoidable, practitioners should employ external verifiers from a different architecture family (\S\ref{sec:cross-arch}) and use the diagnostic framework in \S\ref{sec:discussion} to assess feasibility before deployment. The SCB diagnostic toolkit (below) provides detailed computation methods and threshold recommendations.
1480	
1481	\paragraph{Test-time scaling implications.}
1482	Vote diversity decreases with model capability: $K_\text{eff}$ drops from 3.94 (Mistral-7B on ProofWriter) to 1.09 (Qwen3-14B thinking mode). This creates a fundamental tension for o1/R1-style scaling \citep{guo2025deepseekr1}: longer reasoning chains produce more coherent but less diverse traces, reducing the marginal value of additional samples. Our Process-$\kappa$ analysis (\S\ref{sec:process-kappa}) reveals that this homogenization operates at the reasoning-process level, not just answer level; traces that disagree on final answers still share 69\% of their reasoning structure. Cross-architecture ensembles offer a path forward, but the capability-gap condition (\S\ref{sec:cross-arch}) implies that the verifier must be genuinely complementary, not just different.
1483	
1484	\paragraph{Semantic evaluation remark.}
1485	\label{app:semantic-remark}
1486	Observation~1 assumes degeneration and source attribution. Under \emph{semantic} evaluation, the equivalence additionally requires \emph{answer alignment}: $P(c_i \text{ supports } a_i) \geq P(c_i \text{ supports } a')$ for $a' \neq a_i$, which is structurally motivated and empirically validated ($\mathrm{BR} \in [1.66,\, 4.97]$; Table~\ref{tab:frontier-scb}), but could fail if $f$ systematically extracted premises contradicting their source trace's conclusion.
1487	Since Observation~1 shows SICA reduces to majority vote under degeneration, $\mathrm{BR} \geq 1$ follows from the trace-count geometry; the empirical BR consistently exceeds this floor ($1.66\times$--$4.97\times$; Table~\ref{tab:frontier-scb}), reflecting both base-rate effects and extraction alignment.
1488	
1489	\paragraph{SCB diagnostic toolkit.}
1490	\label{app:diagnostic-toolkit}
1491	We recommend four lightweight diagnostics, computable from sampled traces alone, to predict whether symbolic self-verification will help or hurt before deployment.
1492	\emph{Bias Ratio} (BR; \S\ref{sec:confirmation-bias}): for each problem, compute the fraction of constraints supporting the majority answer, divided by majority vote share. $\text{BR} > 1$ indicates constraints are biased toward the majority; $\text{BR} \gg 2$ (as in all nine models tested; Table~\ref{tab:frontier-scb}) signals that extraction amplifies rather than checks the model's prior. Report as mean $\pm$ bootstrap 95\% CI.
1493	\emph{Effective-K} ($K_\text{eff}$; Eq.~\ref{eq:effk}): compute Fleiss' $\kappa$ across $K$ traces, then $K_\text{eff} = K / [1 + (K-1)\kappa]$. Threshold: $K_\text{eff} \leq 1.30$ never improves in our experiments; aggregation collapses to majority voting. $K_\text{eff} > 1.8$ is a necessary (not sufficient) condition for gain.
1494	\emph{Degenerate Consensus} ($C_0$; \S\ref{sec:condorcet}): the fraction of problems where all $K$ traces agree. $C_0 > 95\%$ renders aggregation moot; $C_0 < 5\%$ means the model is maximally uncertain and constraints tend to amplify noise.
1495	\emph{ProcessSim} (Eq.~\ref{eq:process-sim}): mean pairwise cosine similarity of TF-IDF trace vectors. $\text{ProcessSim} > 0.6$ indicates homogeneous reasoning; combined with $\text{BR} > 2$, this predicts SCB will dominate.
1496	A practitioner should compute all four on a held-out sample ($n \geq 50$). If $K_\text{eff} \leq 1.30$ or $C_0 > 95\%$ or ($\text{BR} > 2$ and $\text{ProcessSim} > 0.6$), symbolic self-verification is unlikely to help.
1497	
1498	\paragraph{BR permutation null model.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6083c230-ea46-4917-b9ce-1d8e1df18879",
  "isSidechain": true,
  "promptId": "ed43d146-c225-42c6-832a-351ecc310242",
  "agentId": "af8784ad3137a4fe6",
  "type": "user",
  "uuid": "3992b194-383b-4bd2-9675-aa94b5fc9b51",
  "sourceToolAssistantUUID": "6083c230-ea46-4917-b9ce-1d8e1df18879",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-26T08:19:29.471Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JyZrBUCS7BcrToSYDHCSYL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "offset": 1498,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3992b194-383b-4bd2-9675-aa94b5fc9b51",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
  "requestId": "req_011CbQrRnEmjZNsFswnyG4Dw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47ff89a4-f5e3-4b2e-8160-a4d8cfe60df8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9Uk5oBhKhYoCaaq8pHkcy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14979,
      "cache_read_input_tokens": 77183,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14979
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 77183,
          "cache_creation_input_tokens": 14979,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14979,
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

_source line 34 · 2026-05-26T08:19:29.484Z_

<details><summary>↩ Tool result · `toolu_01JyZrBUCS7BcrToSYDHCSYL`</summary>

```text
1498	\paragraph{BR permutation null model.}
1499	\label{app:br-permutation}
1500	The permutation test referenced in \S\ref{sec:confirmation-bias} proceeds as follows:
1501	\begin{enumerate}[nosep,leftmargin=*]
1502	\item For each problem $p$ with extracted constraints $\{c_1, \ldots, c_M\}$ and source answers $\{a_1, \ldots, a_M\}$:
1503	\item Randomly permute constraint-to-answer assignments within $p$ (preserving per-trace constraint counts).
1504	\item Compute $\text{BR}_\text{null}$ from the permuted assignments.
1505	\item Repeat $10{,}000$ times to obtain the null distribution.
1506	\item Compute $p$-value $= |\{r : \text{BR}_\text{null}^{(r)} \geq \text{BR}_\text{obs}\}| / 10{,}000$.
1507	\end{enumerate}
1508	Across all tested conditions, $\text{BR}_\text{null} \approx \text{BR}_\text{obs}$ ($p > 0.7$), confirming that the observed bias ratio is fully explained by trace-count geometry under source-attribution scoring (Observation~1), not by an independent extraction bias.
1509	
1510	\paragraph{Future directions: trained extractors and beyond.}
1511	\label{app:future-directions}
1512	Our oracle controls reveal that perfect extraction would yield $+29.90$\,pp over SC on Mistral-7B FOLIO; self-extraction captures only ${\sim}12\%$ of this ceiling. This gap motivates several future directions.
1513	\emph{Trained constraint extractors}: fine-tuning a small model (e.g., encoder-only) on human-annotated FOL from logic benchmarks could produce genuinely discriminative constraints that break the distributional prior. The key design constraint is structural independence: the extractor should not share training data or architecture with the generator, mirroring the cross-architecture NLI escape (\S\ref{sec:cross-arch}).
1514	\emph{Multi-model ensembles}: rather than single cross-architecture pairs, combining $M$ structurally independent verifiers could further reduce correlated errors. The capability-gap condition (\S\ref{sec:cross-arch}) predicts that each verifier must exceed the generator on the target task to contribute positively; empirical verification across heterogeneous verifier pools is needed.
1515	\emph{External knowledge grounding}: connecting to knowledge bases (Wikidata, domain ontologies) could inject verification signal absent from any model's parameters. This avoids SCB entirely by grounding constraints in external facts rather than self-generated traces.
1516	\emph{SCB-aware aggregation}: current MAX-SAT aggregation treats all constraints equally. Weighting constraints by estimated independence (e.g., inverse ProcessSim with other traces' constraints) or by discriminative power (e.g., cross-validation on held-out traces) could partially mitigate SCB without requiring external verifiers.
1517	
1518	\paragraph{SCB as an evaluation framework.}
1519	\label{app:scb-evaluation}
1520	The SCB metrics (BR, $K_\text{eff}$, ProcessSim, and CCR) can serve as a general evaluation framework for self-improvement methods beyond SICA. Any method that extracts structured representations from a model's own outputs (self-verification \citep{huang2024selfcorrect}, self-refinement \citep{madaan2023selfrefine}, chain-of-verification \citep{dhuliawala2023chainofverification}, self-consistency \citep{wang2023sc}) faces the distributional prior that generates SCB. We propose that future work on self-improvement methods report: (1)~BR on error cases (does the method's verification signal correlate with the model's majority answer, or does it provide independent information?); (2)~$K_\text{eff}$ or an analogous diversity metric (does the method generate genuinely diverse candidates, or does it amplify a single mode?); (3)~CCR (does the method preferentially correct errors, or does it preferentially confirm them?). A method with $\text{BR} < 1$, high $K_\text{eff}$, and $\text{CCR} > 0$ demonstrates genuine self-improvement; $\text{BR} > 1$ with $\text{CCR} < 0$ indicates that the method suffers from SCB regardless of aggregate accuracy gains, which may reflect favorable base rates rather than corrective signal.
1521	
1522	\paragraph{Additional scope considerations.}
1523	
1524	Beyond the limitations discussed in the main text, several additional constraints bound our conclusions. Seven of our eleven model-domain conditions have $n \leq 60$, providing insufficient statistical power for confirmatory claims; power analysis shows that the minimum detectable effect exceeds 5\,pp for these conditions (Table~\ref{tab:power}), so they serve as regime characterization rather than definitive tests. Our extraction prompts use a single zero-shot template per domain; alternative prompting strategies (few-shot exemplars, chain-of-thought extraction, or iterative refinement) might yield higher-quality constraints, though the oracle gap suggests the bottleneck is structural rather than prompt-specific. The constraint quality analysis (91.8\% discriminative rate, 39.2\% source-trace minority weight) covers Qwen2.5-14B on FOLIO + ProofWriter ($N = 804$); other model-domain combinations may exhibit different characteristics. Constraint extraction uses $T_{\text{ext}} = 0.3$ while trace sampling uses $T = 0.7$; alternative extraction temperatures might yield different results. Although we prompt for first-order logic formalizations, 99.0\% of extracted constraints are propositional at the Z3 level, with only 1.0\% using true quantifiers ($\forall$/$\exists$); whether models capable of genuine quantified reasoning would yield higher discriminative rates is untested. Deduplication uses syntactic equivalence (global average dedup ratio: 46.0\%), so semantically equivalent constraints with different surface forms receive separate weights; Z3-based semantic deduplication removes an additional ${\sim}$10\% of constraints and yields a small but significant improvement over no deduplication ($p = 0.013$), suggesting room for better dedup strategies. The GSM8K pilot ($n = 30$) illustrates the constraint-absent regime and should not be interpreted as confirmatory evidence.
1525	
1526	\section{Use of AI Assistance}
1527	We used Claude for coding, code drafting, debugging, and language polishing.
1528	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47ff89a4-f5e3-4b2e-8160-a4d8cfe60df8",
  "isSidechain": true,
  "promptId": "ed43d146-c225-42c6-832a-351ecc310242",
  "agentId": "af8784ad3137a4fe6",
  "type": "user",
  "uuid": "fa932a60-396c-4618-90ec-949bc79f7a78",
  "sourceToolAssistantUUID": "47ff89a4-f5e3-4b2e-8160-a4d8cfe60df8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-26T08:21:15.964Z_

Now I have read all files completely. Let me compile the forward reference audit.

---

## Forward Reference Audit Report

### ABSTRACT (abstract.tex)

The abstract is expected to be self-contained. It introduces several custom terms with sufficient inline context:

1. **"Self-Consistency (SC)"** -- line 2: properly defined with full name + abbreviation. OK.
2. **"Symbolic Invariant Consensus Aggregation (SICA)"** -- line 2: properly defined with full name + abbreviation. OK.
3. **"symbolic confirmation bias" (SCB)** -- line 2: introduced with brief explanation ("constraints systematically confirm their source trace's answer rather than providing independent verification"). The abbreviation "SCB" is NOT used in the abstract. OK.
4. **"symbolic mirage"** -- line 2: used but only as a descriptive phrase ("this is a symbolic mirage"), not formally defined. Acceptable in abstract context.
5. **"bias ratios"** -- line 2: used ("bias ratios of 1.66--4.97x") but not defined as a metric. The reader would not know what a "bias ratio" precisely measures from the abstract alone.
   - **First defined**: method.tex line 80-84
   - **Severity**: MEDIUM -- The abstract gives numerical values for "bias ratios" without explaining what the ratio measures. A reader can infer it relates to bias magnitude but not the precise definition.

6. **"first-order logic constraints"** -- line 2: standard term. OK.
7. **"weighted partial MAX-SAT"** -- line 2: standard CS term. OK.
8. **"zero-shot prompting"** -- line 2: standard ML term. OK.
9. **"satisfiability checking"** -- line 2: standard CS term. OK.
10. **"independence--accuracy trade-off"** -- line 2: descriptive phrase, self-explanatory in context. OK.
11. **"cross-architecture verifier"** -- line 2: descriptive, understandable. OK.

### INTRODUCTION (introduction.tex)

12. **"FDR control"** -- line 14: "no condition shows a significant positive effect after FDR control".
    - FDR (False Discovery Rate) is never expanded anywhere in the paper. In the experiments section (line 24), "BH FDR control" appears but "FDR" itself is never given its full form.
    - **Severity**: LOW -- Standard statistical term, but the abbreviation is never explicitly expanded. Most ML readers will know it.

13. **"Observation~1"** -- line 14: referenced as "(Observation~1)".
    - **First defined**: analysis.tex lines 35-37.
    - This is a forward reference to a numbered observation that appears much later.
    - **Severity**: MEDIUM -- The reader encounters "Observation~1" without knowing its content. The surrounding text provides some context ("reduces to a weighted echo of the majority vote under the degeneration condition"), but it is a forward reference to a formal statement.

14. **"$M{\to}T{\to}(A,C)$ generation structure"** -- line 17: used as notation for the causal structure.
    - **First defined**: Never explicitly defined with variable meanings. The notation appears in introduction.tex line 17, related_work.tex line 10, analysis.tex line 53, and discussion.tex line 22. The causal DAG figure (experiments.tex lines 28-31) labels "Traces T produce both answers A and constraints C" but the variable $M$ (model) is never explicitly defined in the notation.
    - **Severity**: HIGH -- $M$, $T$, $A$, $C$ in this notation are never formally introduced. While $T$ (traces), $A$ (answers), $C$ (constraints) can be inferred, $M$ (model) is ambiguous -- it could be confused with $M$ used for number of constraints in the method section.

15. **"$K_\text{eff}$"** -- introduction.tex line 17: used as "effective ensemble size".
    - **First defined**: method.tex line 7-12 (Eq. 1).
    - This is used in the introduction descriptively without the formula but the concept is explained in related_work.tex line 6.
    - **Severity**: LOW -- Forward reference but the concept (effective ensemble size) is explained in words.

16. **"Type~A", "Type~C"** -- These regime names appear first in experiments.tex (Table 1, method.tex line 25-35 in the table), and are defined in analysis.tex lines 86 (diagnostic framework section).
    - Actually, "Type C" and "Type A" labels first appear in Table 1 captions in method.tex lines 25, 35.
    - **First defined with explanation**: analysis.tex lines 86 (diagnostic framework) and appendix lines 560-571 (failure mode analysis). Brief labels in Table 1 ("error amplification" for Type C, "confirmation bias" for Type A) serve as inline definitions.
    - **Severity**: LOW -- The table provides brief inline descriptions.

### RELATED WORK (related_work.tex)

17. **"SCB"** abbreviation -- line 10: "Our symbolic confirmation bias (SCB) is distinct from..."
    - This is the first use of the abbreviation "SCB". The full term was introduced in introduction.tex line 14 but the abbreviation was not given there -- only the full italicized term "symbolic confirmation bias" appeared.
    - **Severity**: LOW -- The abbreviation is given in parentheses right after the full term here in related_work.tex line 10, which is the proper way to introduce it. However, this is technically the first time the abbreviation form is established, and it is then used later.

18. **"Finding~2"** -- appendix.tex line 168: referenced as "Finding~2 predicts CCR(V,G) > 0".
    - **Never defined** anywhere in the paper. No "Finding 2" is formally stated.
    - **Severity**: HIGH -- A formal reference to "Finding 2" that does not exist in the paper.

### METHOD (method.tex)

19. **"$\sigma(c, a)$"** -- line 67-68: defined inline in the scoring equation. OK.
20. **"$\alpha = 0.5$"** -- line 68: defined as penalty weight. OK.
21. **"$C_0$ diagnostic"** -- line 78: properly defined. OK.
22. **"BR" (bias ratio)** -- line 80-84: properly defined with equation. OK.
23. **"$a_M$"** -- line 82: defined as "the model's majority answer" in line 83. OK.
24. **"$a^*$"** -- line 82: defined as "the ground truth" in line 83. Note: $a^*$ is also used in line 69 to mean $\arg\max_a \text{score}(a)$ (the selected answer), which is NOT the same as ground truth. This is an inconsistency, not a forward reference issue.
    - **Severity**: HIGH -- $a^*$ has two conflicting definitions: in line 69 it means "selected answer" ($a^* = \arg\max_a \text{score}(a)$) and in line 83 it means "ground truth". These are different things.

25. **"$\mathcal{C}^{\setminus}$"** -- line 64: defined inline. OK.
26. **"Fleiss' $\kappa$"** -- line 7: cited with reference. Standard statistical term. OK.

### EXPERIMENTS (experiments.tex)

27. **"PW-D5"** and **"PW"** -- experiments.tex line 8 (figure caption uses "PW"), and method.tex table line 26 uses "PW-D5".
    - "PW" or "PW-D5" is never explicitly defined as an abbreviation for "ProofWriter depth-5" before its first use in Table 1 (method.tex line 26). ProofWriter is introduced by name in experiments.tex line 18.
    - **First use**: method.tex line 26 (Table 1: "PW-D5").
    - **First full form**: experiments.tex line 18: "ProofWriter depth-5 ($n{=}600$)".
    - **Severity**: MEDIUM -- "PW-D5" appears in Table 1 (which is in method.tex, before the experiments section where ProofWriter is named). The table is the first encounter of this abbreviation. Readers seeing Table 1 have to look ahead to understand "PW-D5" = ProofWriter depth-5.

28. **"BH" correction** -- experiments.tex line 24: "Benjamini--Hochberg (BH) FDR control" -- properly defined here with full form. But "BH correction" was already used in method.tex Table 1 caption (line 19): "BH adj. p = 0.042" without expansion.
    - **First use without expansion**: method.tex line 19 (Table 1 caption).
    - **First expansion**: experiments.tex line 24.
    - **Severity**: MEDIUM -- Table 1 (in method.tex) uses "BH adj." and "BH correction" before the abbreviation is expanded in experiments.tex.

29. **"TOST equivalence tests"** -- experiments.tex line 35: cited with reference. "TOST" is never expanded to "Two One-Sided Tests".
    - **Severity**: LOW -- A standard statistical method, cited with reference. Not expanding is acceptable but not ideal.

30. **"MDE" (minimum detectable effect)** -- experiments.tex line 35: first use is "minimum detectable effect (MDE)", properly expanded. OK.

31. **"$\sigma_\Delta$"** -- experiments.tex line 35: used in "with $\sigma_\Delta$ up to 2.70 pp".
    - Not explicitly defined. Context implies standard deviation of delta.
    - **Severity**: LOW -- Standard notation for standard deviation, context is clear.

32. **"$\sigma_{\text{SC}}$"** -- experiments.tex line 35: used in "multi-seed SC variability $\sigma_{\text{SC}} = 1.67$--$2.51$ pp".
    - Same as above.
    - **Severity**: LOW.

### ANALYSIS (analysis.tex)

33. **"$I(C;Y)$" and "$I(A;Y)$"** -- analysis.tex line 53: "under degeneration (Observation~1), constraints carry no more task-relevant information than answers alone, i.e., $I(C;\, Y) \leq I(A;\, Y)$".
    - $I(\cdot;\cdot)$ is mutual information notation. $Y$ is never defined (presumably the ground truth label).
    - **Severity**: MEDIUM -- $Y$ is used without definition. While $I$ as mutual information is standard notation, $Y$ as the ground truth / target variable is not introduced.

34. **"Combo"** -- analysis.tex line 66 (Table caption) and throughout: "Combo gain", "Combo $\Delta$".
    - **Never formally defined**. It appears to mean the combined SC + NLI verifier score. First used in Table caption at analysis.tex line 66.
    - **Severity**: MEDIUM -- "Combo" is used as a method name throughout the cross-architecture section without a formal definition. The reader must infer it means the combined SC+verifier approach.

35. **"NLI"** -- analysis.tex line 93: "natural language inference (NLI)" -- properly introduced with full form. OK.

36. **"$w$"** (weight parameter for NLI votes) -- analysis.tex line 93: "Each NLI-supporting vote counts $w$ times alongside SC's $K$ votes" -- defined. OK.

37. **"CCR" (Conditional Correction Ratio)** -- discussion.tex line 19: first use in main text, defined with formula.
    - Actually first defined in discussion.tex line 19 and also in appendix.tex line 162-168. In discussion.tex it is introduced with formula and name. OK.

38. **"DRC" (Disagreement-Routed Cascade)** -- appendix.tex line 843-845: first appearance is "DRC invokes NLI only when SC consensus falls below threshold $\tau$".
    - The abbreviation "DRC" is used in appendix.tex but never expanded in full.
    - **Severity**: LOW -- Appendix-only term. The description explains what it does, but "Disagreement-Routed Cascade" is never written out.

39. **"ICG"** -- method.tex Table 1 uses "gold ICL" (line 19: "$^b$gold ICL"). In the method intervention tables (appendix line 446-449), "ICG" is used as a method name meaning "Independent Constraint Generation".
    - **First use**: appendix line 446 (Table: "ICG -- Trace coupling").
    - **Never fully expanded**: "ICG" is never written as "Independent Constraint Generation" anywhere in the paper.
    - **Severity**: HIGH -- ICG appears multiple times in tables and text (appendix lines 446, 648, 746-759) but is never defined. The reader has no way to know what this abbreviation stands for.

40. **"ICL"** -- method.tex Table 1 line 19: "$^b$gold ICL". ICL presumably means "In-Context Learning" but is never expanded.
    - **Severity**: LOW -- Standard ML abbreviation.

41. **"ProcessSim"** -- appendix.tex line 600-605: defined with formula (Eq. in appendix). Used in discussion.tex line 22 area and appendix line 1495. First mention in main text: analysis.tex line 53 area does not use "ProcessSim" by name; it appears in the appendix and diagnostic toolkit. Not used in the main body.
    - **Severity**: LOW -- Appendix-only defined metric.

42. **"$n_\text{err}$"** -- analysis.tex Table line 16: column header in Table, meaning number of error problems.
    - **Never formally defined** beyond appearing as a column header.
    - **Severity**: LOW -- Inferable from context (number of errors).

### DISCUSSION (discussion.tex)

43. **"$\kappa_{\text{proc}}$"** -- appendix.tex line 608: used in "Process-$\kappa$ gradient". 
    - Not formally defined in main text. Used as a shorthand for process-level kappa/cosine similarity.
    - **Severity**: LOW -- Appendix-only.

### APPENDIX (appendix.tex)

44. **"DSL"** -- appendix.tex line 328: "Domain-Specific Language (DSL)" -- properly introduced. OK.

45. **"CV" (coefficient of variation)** -- appendix.tex line 768: "Per-problem yield CV (coefficient of variation...)" -- properly introduced. OK.

46. **"OWA"** -- appendix.tex line 1178: "ProofWriter OWA" -- never expanded (likely "Open World Assumption").
    - **Severity**: LOW -- Appendix context, domain-specific.

47. **"SBERT"** -- appendix.tex line 741: "Replacing TF-IDF with SBERT embeddings (all-MiniLM-L6-v2)".
    - Never expanded (Sentence-BERT).
    - **Severity**: LOW -- Well-known model.

---

## Summary of Issues by Severity

### HIGH (reader would be confused)

| # | Term/Symbol | First Used | First Defined | Issue |
|---|-------------|-----------|---------------|-------|
| 1 | `$M{\to}T{\to}(A,C)$` notation | introduction.tex line 17 | Never formally defined | Variables $M$, $T$, $A$, $C$ in this causal notation are never introduced. $M$ especially ambiguous (also used for constraint count). |
| 2 | `$a^*$` conflicting definitions | method.tex line 69 vs line 83 | Two conflicting defs | Line 69: $a^* = \arg\max_a \text{score}(a)$ (selected answer). Line 83: "$a^*$ the ground truth". These are different things. |
| 3 | `Finding~2` | appendix.tex line 168 | Never defined | "Finding~2 predicts CCR(V,G) > 0" -- no Finding 2 exists anywhere in the paper. |
| 4 | `ICG` abbreviation | appendix.tex line 446 | Never expanded | Used repeatedly in tables/text but "Independent Constraint Generation" (or whatever it stands for) is never written out. |

### MEDIUM (reader can likely infer but should not have to)

| # | Term/Symbol | First Used | First Defined | Issue |
|---|-------------|-----------|---------------|-------|
| 5 | "bias ratios" in abstract | abstract.tex line 2 | method.tex line 80 | Abstract gives numerical bias ratio values without explaining what the ratio measures. |
| 6 | `Observation~1` | introduction.tex line 14 | analysis.tex line 35 | Forward reference to a formal observation stated 3 sections later. |
| 7 | `PW-D5` / `PW` | method.tex Table 1 line 26 | experiments.tex line 18 | Table abbreviation used before the dataset name "ProofWriter" is introduced. |
| 8 | `BH` (Benjamini-Hochberg) | method.tex Table 1 caption line 19 | experiments.tex line 24 | Table uses "BH adj." before the abbreviation is expanded. |
| 9 | `$Y$` in `$I(C;Y)$` | analysis.tex line 53 | Never defined | Ground-truth label variable used in information-theoretic notation without introduction. |
| 10 | "Combo" as method name | analysis.tex line 66 | Never formally defined | Used throughout cross-architecture section without definition. Appears to mean SC + external verifier ensemble. |

### LOW (standard terms or appendix-only)

| # | Term | Note |
|---|------|------|
| 11 | FDR | Never expanded (False Discovery Rate). Standard statistical term. |
| 12 | TOST | Never expanded (Two One-Sided Tests). Cited with reference. |
| 13 | ICL | Never expanded (In-Context Learning). Standard ML term. |
| 14 | DRC | Appendix only, never expanded (Disagreement-Routed Cascade). |
| 15 | OWA | Appendix only, never expanded (Open World Assumption). |
| 16 | SBERT | Never expanded (Sentence-BERT). Well-known. |
| 17 | SCB abbreviation | Introduced properly in related_work.tex line 10, used thereafter. Minor: not introduced in introduction where the full term first appears. |
| 18 | $K_\text{eff}$ | Forward-referenced in introduction but explained in words. Formally defined in method.tex. |
| 19 | $\sigma_\Delta$, $\sigma_\text{SC}$ | Standard deviation notation, clear from context. |
| 20 | $n_\text{err}$ | Table column header, inferable. |
| 21 | $\kappa_\text{proc}$ | Appendix-only shorthand. |

### Key Recommendations (HIGH priority fixes)

1. **Define `$M{\to}T{\to}(A,C)$`** explicitly where first used (introduction.tex line 17) -- e.g., "where $M$ denotes the model, $T$ the reasoning trace, $A$ the answer, and $C$ the extracted constraints."

2. **Resolve `$a^*$` conflict** in method.tex -- use a different symbol for ground truth (e.g., $a^\dagger$ or $y$) in the bias ratio definition (line 82-83), since $a^*$ already means the SICA-selected answer (line 69).

3. **Remove or define "Finding~2"** in appendix.tex line 168 -- this reference points to nothing. Either define it or replace with a description.

4. **Expand "ICG"** on first use in the appendix -- write "Independent Constraint Generation (ICG)" (or whatever it stands for).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa932a60-396c-4618-90ec-949bc79f7a78",
  "isSidechain": true,
  "agentId": "af8784ad3137a4fe6",
  "requestId": "req_011CbQrS7Ni1CypaS1cihzxV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "222f70c4-c348-4f9c-ab24-17de394243d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/director_909d512a",
  "sessionId": "8f3db67b-bd86-4ccb-8f1e-4ba0a20486fe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "humming-wondering-willow",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Y33JTZtntSnf3ceoGqVWD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1774,
      "cache_read_input_tokens": 92162,
      "output_tokens": 5011,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1774
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5011,
          "cache_read_input_tokens": 92162,
          "cache_creation_input_tokens": 1774,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1774,
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
