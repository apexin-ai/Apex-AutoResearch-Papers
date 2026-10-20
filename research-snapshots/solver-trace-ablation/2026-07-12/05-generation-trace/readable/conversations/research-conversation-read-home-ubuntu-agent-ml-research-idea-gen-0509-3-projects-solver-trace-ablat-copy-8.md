# Research conversation: Read /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex around li

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a940a94944178e51d.jsonl`
- **Structured JSON:** [`08160c6d3571555e27cb.json`](../../sessions/08/08160c6d3571555e27cb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-20T12:48:57.484Z_

Read /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex around line 83 where β=0.2 results are mentioned ("3/3 seeds converge to TS with 0% non-hacking"). 

The audit says: method.tex defines 6 reward conditions with β∈{0.1,0.3} only, but experiments.tex:83 mentions β=0.2 results without clarifying it's supplementary. Add a brief parenthetical like "(supplementary dose, not among the six primary conditions)" after the β=0.2 mention to eliminate the implicit contradiction with "6 reward conditions".

Make the minimal edit needed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "cf93f0c0-d9e5-4859-adb7-f9e7e35a2a64",
  "agentId": "a940a94944178e51d",
  "type": "user",
  "uuid": "b3f5ddd4-71cd-47c0-af88-de159c468a5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "0c26dac2-d587-4d13-aafa-ac5d38ece842",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fizzy-singing-rose"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T12:48:57.490Z_

```json
{
  "parentUuid": "b3f5ddd4-71cd-47c0-af88-de159c468a5b",
  "isSidechain": true,
  "agentId": "a940a94944178e51d",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
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
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
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
  "uuid": "d10bb277-ef67-4b75-ace5-227b5f4452cc",
  "timestamp": "2026-05-20T12:48:57.490Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "0c26dac2-d587-4d13-aafa-ac5d38ece842",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fizzy-singing-rose"
}
```

---

### Assistant

_source line 3 · 2026-05-20T12:49:00.849Z_



Let me read the relevant sections first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d10bb277-ef67-4b75-ace5-227b5f4452cc",
  "isSidechain": true,
  "agentId": "a940a94944178e51d",
  "requestId": "req_011CbDr8RhV9KowwPRqSYekk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66fafc45-8767-464c-babb-99a76563840b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "0c26dac2-d587-4d13-aafa-ac5d38ece842",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fizzy-singing-rose",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBWYLyixL3AFU3qPFz9WT8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31717,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31717,
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

_source line 4 · 2026-05-20T12:49:01.796Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RnGAxRRq3BhXK3zv1Sp8ua`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "offset": 75,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66fafc45-8767-464c-babb-99a76563840b",
  "isSidechain": true,
  "agentId": "a940a94944178e51d",
  "requestId": "req_011CbDr8RhV9KowwPRqSYekk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25fcd84b-3221-4751-a74d-4e16e0acd3ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "0c26dac2-d587-4d13-aafa-ac5d38ece842",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fizzy-singing-rose",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBWYLyixL3AFU3qPFz9WT8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31717,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31717,
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

_source line 5 · 2026-05-20T12:49:01.815Z_

<details><summary>↩ Tool result · `toolu_01RnGAxRRq3BhXK3zv1Sp8ua`</summary>

```text
75	
76	\textbf{Premise-count confound.}
77	The sole non-TS ISR seed (s42) shows raw $\text{ISR}^{*}{=}0.415$, $3.2\times$ random ($0.131$), a premise-minimization artifact ($n{=}5.58$ vs.\ $8.46$); matched comparison gives $1.06\times$ (Appendix~\ref{app:detailed-results}). %% D051 premise-count-matched analysis
78	After reclassifying PG and TS false negatives, non-hacking rates ($6.1\%$ ISR vs.\ $9.5\%$ random) are not significant ($p{=}0.182$; Appendix~\ref{app:h8}). %% D095 FINAL Fisher test
79	The key asymmetry is compositional: ISR converts stochastic TS into near-deterministic convergence ($2/3$ seeds ${\geq}97\%$), while random remains seed-dependent and CE-dominated.
80	
81	\textbf{Higher doses and temporal dynamics.}
82	ISR $\beta{=}0.1$ non-hacking is transient: seed~42 drops $17.3\%{\to}2.2\%$ by 1000 steps as TS escalates to $96.7\%$ (Figure~\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
83	At $\beta{=}0.2$, 3/3 seeds converge to TS with $0\%$ non-hacking. %% registry: plan002-additive-b02-s42/s43/s44
84	At $\beta{=}0.3$, both ISR ($\text{PR}{=}66{\pm}42\%$) and random ($54{\pm}35\%$) destabilize; ISR yields multi-modal failure~\citep{gao-reward-overoptimization}, random converges to CE ($91\%$; Appendix~\ref{app:beta03}). %% registry: plan002-additive-b03-s42/s43/s44
85	
86	\subsection{Cross-Domain Generalization}
87	\label{sec:crossdomain}
88	\label{sec:crosslogic}
89	\label{sec:crossdataset}
90	
91	\begin{figure}[t]
92	\centering
93	\includegraphics[width=\columnwidth]{figures/fig4_prolog_comparison.pdf}
94	\caption{Cross-logic results. \textbf{Top}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25fcd84b-3221-4751-a74d-4e16e0acd3ef",
  "isSidechain": true,
  "promptId": "cf93f0c0-d9e5-4859-adb7-f9e7e35a2a64",
  "agentId": "a940a94944178e51d",
  "type": "user",
  "uuid": "61913458-1591-4eaa-aeb1-78464e9a8a21",
  "sourceToolAssistantUUID": "25fcd84b-3221-4751-a74d-4e16e0acd3ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "0c26dac2-d587-4d13-aafa-ac5d38ece842",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fizzy-singing-rose"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T12:49:02.283Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QStqRoZkY4XdRoR8SebzLz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex",
  "offset": 1,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61913458-1591-4eaa-aeb1-78464e9a8a21",
  "isSidechain": true,
  "agentId": "a940a94944178e51d",
  "requestId": "req_011CbDr8RhV9KowwPRqSYekk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63b88435-3de8-4f5f-93e7-6f2dadc039ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "0c26dac2-d587-4d13-aafa-ac5d38ece842",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fizzy-singing-rose",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBWYLyixL3AFU3qPFz9WT8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31717,
      "cache_read_input_tokens": 0,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 31717
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 237,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 31717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 31717,
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

_source line 7 · 2026-05-20T12:49:02.290Z_

<details><summary>↩ Tool result · `toolu_01QStqRoZkY4XdRoR8SebzLz`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
11	
12	\subsection{Solver Trace Ablation (STA)}
13	\label{sec:sta}
14	
15	STA tests whether each component of a proved formalization is individually necessary for proof success (Algorithm~\ref{alg:sta}).
16	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
17	A component is \emph{necessary} if its removal causes proof failure.
18	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
19	LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
20	
21	\begin{algorithm}[t]
22	\caption{Solver Trace Ablation (STA)}
23	\label{alg:sta}
24	\begin{algorithmic}[1]
25	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
26	\ENSURE $\text{ISR}(x) \in [0, 1]$
27	\STATE $\textit{necessary} \gets 0$
28	\FOR{$i = 1$ to $n$}
29	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
30	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
31	    \ENDIF
32	\ENDFOR
33	\RETURN $\textit{necessary} \,/\, n$
34	\end{algorithmic}
35	\end{algorithm}
36	
37	\paragraph{Intensional Structural Reward.}
38	ISR is the fraction of necessary components:
39	\begin{equation}
40	  \text{ISR}(x) = \frac{1}{n}\sum_{i=1}^{n}\mathbf{1}\bigl[S(x\setminus\{c_i\})=\textit{failed}\bigr]
41	  \label{eq:isr}
42	\end{equation}
43	ISR is defined only for proved formalizations: ISR${=}1$ means every component is necessary; ISR${=}0$ means complete redundancy.
44	We report \emph{proved-only} ISR (denoted ISR$^*$) throughout to avoid conflating structural quality with prove rate.
45	
46	\paragraph{Limitations of ISR.}
47	ISR quantifies component necessity under LOO removal, not structural quality per se ($\rho{=}{-}0.049$ with NLI accuracy; Appendix~\ref{app:extended-discussion}); its diagnostic value is realized through the downstream mode breakdown (\S\ref{sec:taxonomy}), not the ISR scalar alone.
48	ISR is sensitive to component count ($n{=}2 \Rightarrow \text{ISR}{\geq}0.5$); we control for this via premise-count-matched analysis (\S\ref{sec:goodhart}).
49	In particular, TS ($P{\to}P$) achieves $\text{ISR}{\geq}0.5$ by construction since the sole premise is necessary for the trivial proof; we therefore combine ISR with text-match classifiers for complete hacking detection (\S\ref{sec:taxonomy-method}; $O(1)$ binary variant in Appendix~\ref{app:o1-ablation}).
50	
51	\paragraph{LOO independence assumption.}
52	LOO ablation tests individual, not joint, component necessity~\citep{jia-harman-survey}: LOO systematically underestimates ISR when jointly-necessary components exist (redundancy masking), making the observed collapse conservative; the true degradation is worse.
53	Tighter alternatives (Shapley values, pairwise ablation) are left to future work.
54	
55	\subsection{Reward Conditions and Hacking Modes}
56	\label{sec:rewards}
57	\label{sec:taxonomy-method}
58	
59	We study six conditions: exec-only ($r_{\text{exec}}$), ISR low/high-dose ($r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta\in\{0.1,0.3\}$), matched random controls ($r_{\text{exec}}\cdot(1{+}\beta u)$, $u\sim\mathcal{U}(0,1)$), and a supervised fine-tuning (SFT) baseline (negative log-likelihood on gold formalizations).
60	Multiplicative bonuses apply only to proved samples, keeping the prove-rate floor intact.
61	Random isolates ISR-specific signal from generic reward-variance effects; SFT isolates whether structural degeneration arises from RL optimization or data exposure alone.
62	Each RL condition uses seeds $\{42,43,44\}$ and identical training data.
63	An earlier convex formulation ($\alpha r_{\text{exec}} + \beta r_{\text{exec}}\text{ISR}$, $\alpha{+}\beta{=}1$) was discarded because $\text{ISR}{<}1$ always penalized relative to exec-only, collapsing PR (Appendix~\ref{app:setup}).
64	
65	\paragraph{Hacking taxonomy.}
66	Across conditions, seeds, and logic types we identify eight structural-degeneration modes (full definitions in Appendix~\ref{app:hacking-modes}):
67	\textbf{CE} (conclusion embedded among multiple premises),
68	\textbf{TS} (single-premise conclusion duplication, subtypes TSa standard and TSb obfuscated tautology; targets the ISR signal directly, since removing the sole premise forces $\text{ISR}\geq 0.5$),
69	\textbf{PG} (premise-subset gaming: each component is LOO-necessary but the premise set is a strict subset of what the problem requires, inflating ISR without faithful reasoning; Appendix~\ref{app:h8}),
70	\textbf{tautological collapse} (minimal two-component $P{\to}P$ without explicit ISR inflation),
71	\textbf{repetition collapse} (identical clauses repeated to inflate component count),
72	\textbf{complexity-without-utility} (elaborate but vacuous premises),
73	\textbf{contradiction explosion} (contradictory premises trivializing any conclusion via \emph{ex falso}), and
74	\textbf{query-as-fact gaming} (Prolog-specific: emit the NL question as an atom asserted as both fact and query; evades text-match classifiers).
75	Modes are identified by a two-stage procedure: strict normalized text matching (CE/TS) plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution (catches modes evading text matching).
76	We report both classifications in \S\ref{sec:experiments}.
77	
78	In interpreting ISR results, we distinguish two failure semantics that share a numerical signature: an exec-only \emph{low} ISR signals \emph{redundancy} (e.g., repeated ground facts in Prolog), whereas an ISR-rewarded \emph{high} ISR signals \emph{metric gaming} (TS-style constructions).
79	A bare ISR difference therefore does not translate directly into a reasoning-ability difference; the mode breakdown is what licenses such interpretation.
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63b88435-3de8-4f5f-93e7-6f2dadc039ec",
  "isSidechain": true,
  "promptId": "cf93f0c0-d9e5-4859-adb7-f9e7e35a2a64",
  "agentId": "a940a94944178e51d",
  "type": "user",
  "uuid": "0f52e67b-e0e0-402b-b672-7520ad8da195",
  "sourceToolAssistantUUID": "63b88435-3de8-4f5f-93e7-6f2dadc039ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "0c26dac2-d587-4d13-aafa-ac5d38ece842",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fizzy-singing-rose"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-20T12:49:06.352Z_

Line 59 of method.tex defines the six conditions with β∈{0.1,0.3} only. Line 83 of experiments.tex mentions β=0.2 without clarification. I'll add the parenthetical.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f52e67b-e0e0-402b-b672-7520ad8da195",
  "isSidechain": true,
  "agentId": "a940a94944178e51d",
  "requestId": "req_011CbDr8nU9ZBnAmnZwW1joc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecc70134-869e-4f54-a378-34a38afbf25f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "0c26dac2-d587-4d13-aafa-ac5d38ece842",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fizzy-singing-rose",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UwNEU5zmBceFsjKCJosJUJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4171,
      "cache_read_input_tokens": 31717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4171,
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

_source line 9 · 2026-05-20T12:49:07.947Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01NkBGBnWyZd3KTHKWJucwxN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "old_string": "At $\\beta{=}0.2$, 3/3 seeds converge to TS with $0\\%$ non-hacking.",
  "new_string": "At $\\beta{=}0.2$ (supplementary dose, not among the six primary conditions), 3/3 seeds converge to TS with $0\\%$ non-hacking."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecc70134-869e-4f54-a378-34a38afbf25f",
  "isSidechain": true,
  "agentId": "a940a94944178e51d",
  "requestId": "req_011CbDr8nU9ZBnAmnZwW1joc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63d7406d-7faa-4843-a659-072e18e32ce6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "0c26dac2-d587-4d13-aafa-ac5d38ece842",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fizzy-singing-rose",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UwNEU5zmBceFsjKCJosJUJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4171,
      "cache_read_input_tokens": 31717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4171,
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

_source line 10 · 2026-05-20T12:49:07.968Z_

<details><summary>↩ Tool result · `toolu_01NkBGBnWyZd3KTHKWJucwxN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63d7406d-7faa-4843-a659-072e18e32ce6",
  "isSidechain": true,
  "promptId": "cf93f0c0-d9e5-4859-adb7-f9e7e35a2a64",
  "agentId": "a940a94944178e51d",
  "type": "user",
  "uuid": "4b9ef19a-a47a-4684-82a7-4fba9ed3bd4d",
  "sourceToolAssistantUUID": "63d7406d-7faa-4843-a659-072e18e32ce6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "0c26dac2-d587-4d13-aafa-ac5d38ece842",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fizzy-singing-rose"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T12:49:12.572Z_

Done. Added the parenthetical "(supplementary dose, not among the six primary conditions)" after `β=0.2` on line 83 of `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex`. This clarifies that β=0.2 is outside the six conditions defined in method.tex (which use β∈{0.1, 0.3}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b9ef19a-a47a-4684-82a7-4fba9ed3bd4d",
  "isSidechain": true,
  "agentId": "a940a94944178e51d",
  "requestId": "req_011CbDr9CcDZ4UKmbioethtz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4460eaa-ecdb-4867-a9fe-8ebe452d2632",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "0c26dac2-d587-4d13-aafa-ac5d38ece842",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fizzy-singing-rose",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011NpVksrUkWSsbaS2LxZ7Eq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 329,
      "cache_read_input_tokens": 35888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 329,
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
