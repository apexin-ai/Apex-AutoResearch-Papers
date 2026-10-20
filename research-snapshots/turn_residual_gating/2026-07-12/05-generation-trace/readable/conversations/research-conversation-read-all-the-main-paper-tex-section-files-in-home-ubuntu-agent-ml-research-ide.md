# Research conversation: Read all the main paper .tex section files in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_ga

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a5748595957c992d4.jsonl`
- **Structured JSON:** [`f8453c6d849e579ca6d9.json`](../../sessions/f8/f8453c6d849e579ca6d9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-25T19:41:02.210Z_

Read all the main paper .tex section files in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/ and extract EVERY number that appears. This includes:
- Numbers in running text (percentages, multipliers, counts, p-values, etc.)
- Numbers in figure captions
- Numbers in table cells
- Hyperparameters mentioned
- Dataset sizes
- Any numerical claim

For each number, record:
1. Which file and approximate line
2. The exact number and its context (the sentence or phrase it appears in)
3. What it refers to (e.g., "GAR-ours for ThreadGate under AR", "learning rate", "dataset size")

Files to read: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, analysis.tex, discussion.tex, conclusion.tex, limitations.tex

Organize the output by section. Be EXHAUSTIVE - do not skip any number, no matter how small.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "06680b7d-c294-4388-addf-d95914654fbd",
  "agentId": "a5748595957c992d4",
  "type": "user",
  "uuid": "43f6b175-5b48-4d95-bf5d-63a4a5c30fc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T19:41:02.215Z_

```json
{
  "parentUuid": "43f6b175-5b48-4d95-bf5d-63a4a5c30fc1",
  "isSidechain": true,
  "agentId": "a5748595957c992d4",
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
  "uuid": "b64a234f-7bbe-4033-8506-6161906aa948",
  "timestamp": "2026-05-25T19:41:02.215Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

---

### Assistant

_source line 3 · 2026-05-25T19:41:04.264Z_

I'll systematically read all the section files and extract every number.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b64a234f-7bbe-4033-8506-6161906aa948",
  "isSidechain": true,
  "agentId": "a5748595957c992d4",
  "requestId": "req_011CbPrba3KyX4HM2xRTqSLD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05a16239-0a90-462f-9993-8c31e78cf305",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01N3XTyzM7h6Qde4QcxMQTwD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33338,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33338,
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

_source line 4 · 2026-05-25T19:41:04.812Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RxKYTgS9a9CWsfW6XnPidG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05a16239-0a90-462f-9993-8c31e78cf305",
  "isSidechain": true,
  "agentId": "a5748595957c992d4",
  "requestId": "req_011CbPrba3KyX4HM2xRTqSLD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06fb8cf8-032e-4a1b-ae48-749748f45c49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01N3XTyzM7h6Qde4QcxMQTwD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33338,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33338,
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

_source line 5 · 2026-05-25T19:41:04.821Z_

<details><summary>↩ Tool result · `toolu_01RxKYTgS9a9CWsfW6XnPidG`</summary>

```text
1	\begin{abstract}
2	As multi-turn conversations grow longer, large language models progressively lose attention to the system-prompt goals that define their task, even when the underlying goal representations remain intact. Existing remedies operate at inference time, leaving a natural but untested alternative: training auxiliary attention losses alongside next-token prediction to directly optimize goal attention. This strategy assumes that attention patterns learned under teacher forcing will transfer to autoregressive generation, an assumption that classical exposure bias research has challenged for sequence models but that has never been examined for auxiliary attention objectives in multi-turn transformers.
3	We show this assumption fails. On a controlled five-way testbed spanning two architectures (Qwen-2.5-7B, Llama-3.1-8B), goal attention optimized to target under teacher forcing collapses by an order of magnitude under autoregressive generation. A causal exclusion chain traces the failure to exposure bias, ruling out gradient conflict, gating mechanism, and parameter capacity as primary causes. Inference-time attention steering confirms that the collapse reflects attention misallocation rather than representation loss. Scheduled sampling, applied here for the first time to auxiliary attention objectives in multi-turn transformers, compresses the training--inference gap to near parity on Qwen and substantially on Llama, with no perplexity cost\footnote{Code and data are available at \url{https://anonymous.4open.science/r/turn_residual_gating-8703/}.}.
4	\end{abstract}
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06fb8cf8-032e-4a1b-ae48-749748f45c49",
  "isSidechain": true,
  "promptId": "06680b7d-c294-4388-addf-d95914654fbd",
  "agentId": "a5748595957c992d4",
  "type": "user",
  "uuid": "b9afaea5-ced7-4ef8-a98a-9987e5c17b5d",
  "sourceToolAssistantUUID": "06fb8cf8-032e-4a1b-ae48-749748f45c49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-25T19:41:05.205Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KaC8bYvKUtjpwfKR8x5XXx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9afaea5-ced7-4ef8-a98a-9987e5c17b5d",
  "isSidechain": true,
  "agentId": "a5748595957c992d4",
  "requestId": "req_011CbPrba3KyX4HM2xRTqSLD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "defd994e-ac13-4c0d-8293-03b35b562049",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01N3XTyzM7h6Qde4QcxMQTwD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33338,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33338,
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

_source line 7 · 2026-05-25T19:41:05.209Z_

<details><summary>↩ Tool result · `toolu_01KaC8bYvKUtjpwfKR8x5XXx`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is central to how large language models are deployed, from customer service to tutoring to long-form reasoning. Yet a persistent failure accompanies even the most fluent generation: as conversations grow longer, models pay progressively less attention to the system-prompt goals that define their task. \citet{dongre2026attention} measured significant Goal Accessibility Ratio (GAR) decline across 12 models over extended conversations; in our own evaluation, goal attention drops by over 70\% within just five turns. Crucially, this is not a representation problem: residual stream probes confirm that goal information persists (AUC\,=\,0.98). The model retains the knowledge of what it should attend to; it simply stops attending.
4	
5	Existing remedies address this decay at inference time. Split-softmax \citep{li2024measuring} separates instruction from conversation tokens; StreamingLLM \citep{xiao2024streaming} retains anchor tokens; Gated Attention \citep{qiu2025gated} applies per-head sigmoid gates within a single forward pass. A natural alternative is to intervene during training: optimize goal attention directly through auxiliary losses trained alongside next-token prediction (NTP). Yet this strategy rests on an untested assumption: attention patterns learned under teacher forcing (TF) transfer to autoregressive (AR) generation. Classical exposure bias research \citep{bengio2015scheduled,lamb2016professor} has shown that TF creates a training--inference distribution mismatch for RNN sequence models, but whether this mismatch extends to auxiliary attention objectives in multi-turn transformers remains unknown.
6	
7	We test this assumption and find it fails. We introduce a controlled five-way testbed (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, and Base) designed not as competing solutions but as a causal exclusion chain (\S\ref{sec:comparison-design}), where each adjacent pair isolates one candidate failure mechanism. The result is unambiguous: every variant converges to target GAR under teacher forcing, yet goal attention collapses by an order of magnitude once the model generates its own context (Figure~\ref{fig:headline}). The exclusion chain traces this collapse to exposure bias, the training--inference distribution mismatch, ruling out gradient direction conflict (PCGrad removes conflict yet \emph{worsens} AR GAR), gating mechanism (Uniform Gate matches ThreadGate), and parameter capacity (LoRA-only shows the same pattern). Inference-time $\beta$-steering confirms that the collapse reflects attention misallocation rather than representation degradation; scheduled sampling bridges the gap by exposing the model to its own generations during training.
8	
9	\begin{figure*}[!ht]
10	  \centering
11	  \includegraphics[width=\textwidth]{fig1_headline.pdf}
12	  \caption{Exposure bias collapses auxiliary attention losses. \textbf{(a)}~Goal attention decays 85--90\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \textbf{(b)}~Under TF evaluation all variants reach GAR$\approx$0.50, but AR generation collapses GAR by 8--17$\times$ (log scale). \textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.8$\times$ to 1.3$\times$ (Qwen) and ${\sim}$27$\times$ to 2.9$\times$ (Llama).}
13	  \label{fig:headline}
14	\end{figure*}
15	
16	Our contributions are:
17	\begin{enumerate}\raggedright
18	    \item \textbf{Exposure bias characterization.} To our knowledge, the first empirical demonstration that exposure bias collapses auxiliary attention objectives in multi-turn transformers, with an order-of-magnitude TF--AR gap reproduced across two architectures (Qwen-2.5-7B, Llama-3.1-8B) and model scales (1.5B--8B).
19	    \item \textbf{Causal exclusion testbed.} A five-way diagnostic design, informed by seven loss-formulation iterations, that isolates the failure mechanism via causal exclusion, including a PCGrad \emph{modus tollens} argument ruling out gradient direction conflict ($p$\,=\,0.002, effect reverses).
20	    \item \textbf{Attention misallocation diagnosis.} Inference-time $\beta$-steering recovers goal attention with modest perplexity cost, evidence that the collapse is an attention routing failure, not a representational one.
21	    \item \textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\sim}$1.3$\times$ on Qwen and ${\sim}$2.9$\times$ on Llama with no perplexity degradation, robust across three seeds.
22	\end{enumerate}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "defd994e-ac13-4c0d-8293-03b35b562049",
  "isSidechain": true,
  "promptId": "06680b7d-c294-4388-addf-d95914654fbd",
  "agentId": "a5748595957c992d4",
  "type": "user",
  "uuid": "b2c41bdf-daa0-41f6-8bbb-84ddc3c2769d",
  "sourceToolAssistantUUID": "defd994e-ac13-4c0d-8293-03b35b562049",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-25T19:41:09.158Z_

<details open><summary>🔧 Tool call — Read · `toolu_019kQbA3YgHzWVeQqVZBg8Vr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2c41bdf-daa0-41f6-8bbb-84ddc3c2769d",
  "isSidechain": true,
  "agentId": "a5748595957c992d4",
  "requestId": "req_011CbPrbo5egv25mU7LcXxvU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2c75c7f-86f4-4cdd-a336-943b47cbc102",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QRWrVh5exZpR3kQZNEhGM9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2649,
      "cache_read_input_tokens": 33338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2649,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 9 · 2026-05-25T19:41:09.163Z_

<details><summary>↩ Tool result · `toolu_019kQbA3YgHzWVeQqVZBg8Vr`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Multi-turn dialogue and attention decay.}
4	Multi-turn coherence has been a persistent challenge from early dialogue systems \citep{li2016persona,roller2021recipes,zhang2020dialogpt} through modern long-context models \citep{xu2022goldfish}, with benchmarks such as MT-Bench \citep{zheng2024judging} and MT-Bench-101 \citep{bai2024mtbench101} continuing to expose quality gaps at later turns \citep{laban2025lost,liu2026intent}. Most relevant to our work, \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) and showed that attention to goal tokens decays 27--48\% across 12 models while residual probes retain goal information (AUC\,=\,0.98). We observe a steeper 70.8\% decline on Qwen-2.5-7B. \citet{li2024measuring} independently quantified instruction instability and proposed split-softmax as an inference-time remedy. Our work differs in scope: we diagnose \emph{why} training-time attention optimization fails to transfer to inference, and provide the first training-time mitigation.
5	
6	\paragraph{Gating and attention manipulation.}
7	Residual gating spans highway networks \citep{srivastava2015highway}, ReZero \citep{bachlechner2021rezero}, layer pruning \citep{gromov2024unreasonable,fan2020layerdrop}, and adaptive depth \citep{schuster2022calm,raposo2024mixture}. Most relevant is Gated Attention \citep{qiu2025gated}: per-head sigmoid gates achieving MMLU \citep{hendrycks2021measuring} $+$2.03 at 15B scale; ThreadGate differs in conditioning on turn position. On the analysis side, head specialization \citep{clark2019what,voita2019analyzing,kovaleva2019revealing}, positional bias calibration \citep{liu2024lost,xiao2024streaming}, and attention steering (PASTA; \citealp{zhang2024tell}) address inference behavior; our $\beta$-steering serves a diagnostic role. PCGrad \citep{yu2020pcgrad} and CAGrad \citep{liu2021cagrad} treat gradient conflict as the root cause; we show direction conflict is a symptom, not the primary cause.
8	
9	\paragraph{Exposure bias in sequence models.}
10	Teacher forcing creates a distributional mismatch between training and inference \citep{wiseman2016sequence,arora2022exposure}. Scheduled sampling \citep{bengio2015scheduled} introduced curriculum-based mixing; subsequent work proposed sequence-level objectives \citep{ranzato2016sequence}, adversarial regularization \citep{lamb2016professor}, self-recovery analysis \citep{he2019exposure}, bridging strategies for neural machine translation (NMT; \citealp{zhang2019bridging}), and search-based training \citep{leblond2018searnn}. \citet{mihaylova2019scheduled} extended scheduled sampling to transformers for single-turn NMT. \citet{dou2019attention} proposed attention forcing (supervising cross-attention during NMT), and \citet{dou2022parallel} extended it with KL-divergence switching. Our work differs: (i)~time-scheduled sampling (linearly increasing $\rho$), not data-dependent; (ii)~self-attention in multi-turn dialogue, not cross-attention in NMT; (iii)~auxiliary attention objectives, not primary translation loss. No prior work examines exposure bias on \emph{auxiliary} attention objectives or provides multi-turn transformer mitigation; we fill both gaps.
11	
12	\begin{table*}[!t]
13	\centering
14	\small
15	\caption{Five-way comparison on Qwen-2.5-7B-Instruct. TF evaluation uses IID UltraChat and 50 held-out conversations; AR evaluation uses $N$\,=\,50 held-out conversations (mean 3.6 user turns). All fine-tuned variants converge under TF ($\leq$2\,pp spread); the 8--17$\times$ TF-AR gap persists across all configurations. $\bar{g}\!\pm\!\sigma_g$: learned gate mean and std across 28 layers (LoRA-only has no gates). GAR-O = GAR-ours; GAR-D = GAR-Dongre \citep{dongre2026attention}.}
16	\label{tab:five-way}
17	\begin{tabular}{l ccc ccc cc c}
18	\toprule
19	& \multicolumn{3}{c}{\textbf{IID (TF)}} & \multicolumn{3}{c}{\textbf{Held-out (TF)}} & \multicolumn{2}{c}{\textbf{AR ($N$\,=\,50)}} & \\
20	\cmidrule(lr){2-4} \cmidrule(lr){5-7} \cmidrule(lr){8-9}
21	\textbf{Configuration} & GAR-O & GAR-D & PPL & GAR-O & GAR-D & PPL & GAR-O & 95\% CI & $\bar{g}\!\pm\!\sigma_g$ \\
22	\midrule
23	\multicolumn{10}{l}{\emph{Baseline}} \\
24	Base              & 0.01 & 0.00 & 4.23 & 0.01 & 0.00 & 4.34 & 0.019 & {\scriptsize[.014,\,.024]} & --- \\
25	\midrule
26	\multicolumn{10}{l}{\emph{Gated variants}} \\
27	ThreadGate        & 0.50 & \textbf{0.02} & 2.78 & 0.50 & \textbf{0.02} & 2.78 & \textbf{0.064} & {\scriptsize[.041,\,.091]} & .93\,{\scriptsize$\pm$\,.05} \\
28	\;+\,PCGrad       & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.030 & {\scriptsize[.023,\,.038]} & --- \\
29	Uniform Gate      & 0.49 & 0.01 & 2.78 & \textbf{0.51} & 0.01 & 2.78 & 0.033 & {\scriptsize[.025,\,.043]} & .96\,{\scriptsize$\pm$\,.05} \\
30	\midrule
31	\multicolumn{10}{l}{\emph{Ungated}} \\
32	LoRA-only         & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.037 & {\scriptsize[.027,\,.050]} & 1.00 \\
33	\bottomrule
34	\end{tabular}
35	\end{table*}
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2c75c7f-86f4-4cdd-a336-943b47cbc102",
  "isSidechain": true,
  "promptId": "06680b7d-c294-4388-addf-d95914654fbd",
  "agentId": "a5748595957c992d4",
  "type": "user",
  "uuid": "ebf2468a-2dea-429f-8ac8-64c1a9ecae53",
  "sourceToolAssistantUUID": "e2c75c7f-86f4-4cdd-a336-943b47cbc102",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T19:41:09.324Z_

<details open><summary>🔧 Tool call — Read · `toolu_012pwr6Pro1TNEyinVECB7gb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebf2468a-2dea-429f-8ac8-64c1a9ecae53",
  "isSidechain": true,
  "agentId": "a5748595957c992d4",
  "requestId": "req_011CbPrbo5egv25mU7LcXxvU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a1298ee-b1f0-446b-8d70-45f75f11c484",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QRWrVh5exZpR3kQZNEhGM9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2649,
      "cache_read_input_tokens": 33338,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2649
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 33338,
          "cache_creation_input_tokens": 2649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2649,
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

_source line 11 · 2026-05-25T19:41:09.329Z_

<details><summary>↩ Tool result · `toolu_012pwr6Pro1TNEyinVECB7gb`</summary>

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
  "parentUuid": "2a1298ee-b1f0-446b-8d70-45f75f11c484",
  "isSidechain": true,
  "promptId": "06680b7d-c294-4388-addf-d95914654fbd",
  "agentId": "a5748595957c992d4",
  "type": "user",
  "uuid": "c955b2aa-12d5-4b10-8415-82a2979e58a8",
  "sourceToolAssistantUUID": "2a1298ee-b1f0-446b-8d70-45f75f11c484",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T19:41:13.917Z_

<details open><summary>🔧 Tool call — Read · `toolu_016pbaa92jVMfhqriFQGopc8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c955b2aa-12d5-4b10-8415-82a2979e58a8",
  "isSidechain": true,
  "agentId": "a5748595957c992d4",
  "requestId": "req_011CbPrc6vhP6gEWMbxxg7uj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6971fa20-e27c-496a-a475-ae59a0320e03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0166RGuk1ypSRNb6gdrnqefo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4710,
      "cache_read_input_tokens": 35987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4710,
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

_source line 13 · 2026-05-25T19:41:13.923Z_

<details><summary>↩ Tool result · `toolu_016pbaa92jVMfhqriFQGopc8`</summary>

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
  "parentUuid": "6971fa20-e27c-496a-a475-ae59a0320e03",
  "isSidechain": true,
  "promptId": "06680b7d-c294-4388-addf-d95914654fbd",
  "agentId": "a5748595957c992d4",
  "type": "user",
  "uuid": "0924d436-3439-4d9f-a0a5-002290ad662b",
  "sourceToolAssistantUUID": "6971fa20-e27c-496a-a475-ae59a0320e03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T19:41:14.416Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BZjA1EdMS2cksrJF84sH7o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0924d436-3439-4d9f-a0a5-002290ad662b",
  "isSidechain": true,
  "agentId": "a5748595957c992d4",
  "requestId": "req_011CbPrc6vhP6gEWMbxxg7uj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6584dde1-e0a9-4949-9545-490da4573d6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0166RGuk1ypSRNb6gdrnqefo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4710,
      "cache_read_input_tokens": 35987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4710,
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

_source line 15 · 2026-05-25T19:41:14.420Z_

<details><summary>↩ Tool result · `toolu_01BZjA1EdMS2cksrJF84sH7o`</summary>

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
10	Each subsection kills one alternative hypothesis via causal exclusion: \S\ref{subsec:gate-conditioning}~turn conditioning, \S\ref{subsec:pcgrad}~gradient direction conflict, leaving exposure bias as the primary remaining explanation consistent with current evidence (\S\ref{subsec:dist-shift}). \S\ref{subsec:mechanism-specificity} confirms selectivity; \S\ref{subsec:cross-model} confirms cross-architecture generalization.
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
  "parentUuid": "6584dde1-e0a9-4949-9545-490da4573d6e",
  "isSidechain": true,
  "promptId": "06680b7d-c294-4388-addf-d95914654fbd",
  "agentId": "a5748595957c992d4",
  "type": "user",
  "uuid": "23364bb5-f4a4-46ff-a933-2eede709988b",
  "sourceToolAssistantUUID": "6584dde1-e0a9-4949-9545-490da4573d6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T19:41:17.772Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JYgsETySnVC1QriFaANZdj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23364bb5-f4a4-46ff-a933-2eede709988b",
  "isSidechain": true,
  "agentId": "a5748595957c992d4",
  "requestId": "req_011CbPrcUt3f8dnEeimLCQNC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09f250d2-7075-4030-911d-26727e5238b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0147UwDD5X64ySE95VgRbqWu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4671,
      "cache_read_input_tokens": 40697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4671,
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

_source line 17 · 2026-05-25T19:41:17.776Z_

<details><summary>↩ Tool result · `toolu_01JYgsETySnVC1QriFaANZdj`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\looseness=-1 NTP self-recovers because prediction is the same task at both regimes \citep{he2019exposure}; GAR optimizes a \emph{global property} (attention allocation to goal tokens) with no autoregressive counterpart. The collapse is selective: GAR-ours collapses by an order of magnitude while GAR-Dongre shows negligible shift (${\leq}$1.3$\times$). Per-head analysis confirms selectivity: heads with higher TF GAR shift most under AR ($r$\,=\,0.743; Appendix~\ref{sec:appendix-kl}). Any auxiliary attention objective targeting distributional properties rather than prediction itself should face the same barrier under teacher forcing.
4	
5	\looseness=-1 Our exclusion identifies exposure bias as a primary contributing factor, but cannot fully rule out KV cache drift (\S\ref{sec:limitations}). The PCGrad exclusion rules out direction conflict but not magnitude imbalance (7.5--25.7$\times$ NTP dominance; \citealp{chen2018gradnorm}). The GAR--compliance correlation is weak ($r$\,=\,0.200; Appendix~\ref{sec:appendix-ir}), reinforcing GAR's role as a diagnostic probe. Our $\beta$-steering is likewise a \emph{diagnostic}, distinct from inference-time remedies such as split-softmax \citep{li2024measuring} and Rhea \citep{hong2025rhea}. SS and inference-time fixes are complementary: SS modifies representations without inference cost; inference-time methods cannot recover patterns never learned. At $\beta$\,=\,5 the two converge (SS\,=\,0.717 vs.\ TG\,=\,0.727).
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09f250d2-7075-4030-911d-26727e5238b6",
  "isSidechain": true,
  "promptId": "06680b7d-c294-4388-addf-d95914654fbd",
  "agentId": "a5748595957c992d4",
  "type": "user",
  "uuid": "3ff62bc2-2572-4293-b48b-a4946b4a233b",
  "sourceToolAssistantUUID": "09f250d2-7075-4030-911d-26727e5238b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-25T19:41:18.324Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LFob4qMGn5yg8osfhjoLeJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ff62bc2-2572-4293-b48b-a4946b4a233b",
  "isSidechain": true,
  "agentId": "a5748595957c992d4",
  "requestId": "req_011CbPrcUt3f8dnEeimLCQNC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07b66d8a-4c9e-47e8-ab74-835dff835c37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0147UwDD5X64ySE95VgRbqWu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4671,
      "cache_read_input_tokens": 40697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4671,
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

_source line 19 · 2026-05-25T19:41:18.328Z_

<details><summary>↩ Tool result · `toolu_01LFob4qMGn5yg8osfhjoLeJ`</summary>

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
  "parentUuid": "07b66d8a-4c9e-47e8-ab74-835dff835c37",
  "isSidechain": true,
  "promptId": "06680b7d-c294-4388-addf-d95914654fbd",
  "agentId": "a5748595957c992d4",
  "type": "user",
  "uuid": "afe29f64-b4e8-4268-bee4-273ca7a3790b",
  "sourceToolAssistantUUID": "07b66d8a-4c9e-47e8-ab74-835dff835c37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-25T19:41:18.719Z_

<details open><summary>🔧 Tool call — Read · `toolu_0129j3Li9mM9dSUpGqibkezi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afe29f64-b4e8-4268-bee4-273ca7a3790b",
  "isSidechain": true,
  "agentId": "a5748595957c992d4",
  "requestId": "req_011CbPrcUt3f8dnEeimLCQNC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "343389c9-1a67-429c-baa4-ff024aa971cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0147UwDD5X64ySE95VgRbqWu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4671,
      "cache_read_input_tokens": 40697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4671,
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

_source line 21 · 2026-05-25T19:41:18.726Z_

<details><summary>↩ Tool result · `toolu_0129j3Li9mM9dSUpGqibkezi`</summary>

```text
1	\section*{Limitations}\label{sec:limitations}
2	
3	Our findings are demonstrated on two model families (Qwen-2.5-7B and Llama-3.1-8B) and a single dataset (UltraChat, 8K conversations); generalization to other architectures and domains (e.g., code, reasoning) is untested. Most configurations use a single seed (scheduled sampling validated on three seeds; \S\ref{subsec:ss}), and quality assessment relies on PPL rather than comprehensive benchmarks \citep{hendrycks2021measuring,lin2022truthfulqa}. We test only one auxiliary loss family (GAR with MSE target $\tau$\,=\,0.5); head-specific or layer-specific losses may exhibit different sensitivity to exposure bias. Our causal exclusion identifies exposure bias as a primary factor but does not rule out KV cache drift as a contributing mechanism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "343389c9-1a67-429c-baa4-ff024aa971cc",
  "isSidechain": true,
  "promptId": "06680b7d-c294-4388-addf-d95914654fbd",
  "agentId": "a5748595957c992d4",
  "type": "user",
  "uuid": "7e178ee0-fa1f-4156-9c53-65f585e75ca2",
  "sourceToolAssistantUUID": "343389c9-1a67-429c-baa4-ff024aa971cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-25T19:43:42.950Z_

Now I have all the content. Let me compile the exhaustive number extraction:

---

## Exhaustive Number Extraction by Section

---

### abstract.tex

| Line | Number | Context | What it refers to |
|------|--------|---------|-------------------|
| 3 | **5** | "a controlled five-way testbed" | Number of conditions in the testbed |
| 3 | **2** | "spanning two architectures" | Number of architectures tested |
| 3 | "order of magnitude" | "collapses by an order of magnitude" | Magnitude of AR GAR collapse (~10×) |

---

### introduction.tex

| Line | Number | Context | What it refers to |
|------|--------|---------|-------------------|
| 3 | **12** | "GAR decline across 12 models" | Number of models in Dongre et al. evaluation |
| 3 | **70%** | "goal attention drops by over 70% within just five turns" | GAR decline in authors' own evaluation |
| 3 | **5** | "within just five turns" | Number of turns for 70%+ drop |
| 3 | **0.98** | "AUC = 0.98" | Residual stream probe AUC for goal information persistence |
| 12 | **85–90%** | "Goal attention decays 85–90% across turns under AR generation" | AR GAR decay range across turns (figure caption) |
| 12 | **0.50** | "all variants reach GAR ≈ 0.50" | TF GAR for all variants (figure caption) |
| 12 | **8–17×** | "AR generation collapses GAR by 8–17×" | TF-AR collapse ratio (figure caption, log scale) |
| 12 | **7.8×** | "TF–AR gap from 7.8×" | Pre-SS gap for Qwen (figure caption) |
| 12 | **1.3×** | "to 1.3×" | Post-SS gap for Qwen (figure caption) |
| 12 | **~27×** | "~27× to 2.9×" | Pre-SS gap for Llama (figure caption) |
| 12 | **2.9×** | "~27× to 2.9×" | Post-SS gap for Llama (figure caption) |
| 18 | **2** | "two architectures (Qwen-2.5-7B, Llama-3.1-8B)" | Number of architectures for order-of-magnitude gap |
| 18 | **1.5B–8B** | "model scales (1.5B–8B)" | Model scale range tested |
| 19 | **5** | "five-way diagnostic design" | Number of conditions in causal exclusion testbed |
| 19 | **7** | "informed by seven loss-formulation iterations" | Number of loss design iterations |
| 19 | **0.002** | "p = 0.002, effect reverses" | p-value for PCGrad modus tollens |
| 21 | **~1.3×** | "compressing the TF–AR gap to ~1.3× on Qwen" | Post-SS gap for Qwen |
| 21 | **~2.9×** | "~2.9× on Llama" | Post-SS gap for Llama |
| 21 | **3** | "robust across three seeds" | Number of seeds for SS robustness |

---

### related_work.tex

| Line | Number | Context | What it refers to |
|------|--------|---------|-------------------|
| 4 | **27–48%** | "attention to goal tokens decays 27–48% across 12 models" | GAR decline range in Dongre et al. |
| 4 | **12** | "across 12 models" | Number of models in Dongre et al. |
| 4 | **0.98** | "AUC = 0.98" | Residual probes goal information retention (Dongre) |
| 4 | **70.8%** | "70.8% decline on Qwen-2.5-7B" | Authors' observed GAR decline on Qwen |
| 7 | **+2.03** | "MMLU +2.03 at 15B scale" | MMLU improvement from Gated Attention (Qiu et al.) |
| 7 | **15B** | "at 15B scale" | Model scale for Gated Attention MMLU result |
| 15 | **50** | "50 held-out conversations" | Held-out set size for AR evaluation (table caption) |
| 15 | **3.6** | "mean 3.6 user turns" | Mean user turns per held-out conversation (table caption) |
| 15 | **2 pp** | "≤2 pp spread" | TF GAR-ours spread under TF (table caption) |
| 15 | **8–17×** | "8–17× TF-AR gap" | TF-AR gap across all configurations (table caption) |
| 15 | **28** | "across 28 layers" | Number of layers for gate mean/std (table caption) |
| 24 | **0.01** | "Base: GAR-O 0.01" | Base model GAR-ours IID TF |
| 24 | **0.00** | "Base: GAR-D 0.00" | Base model GAR-Dongre IID TF |
| 24 | **4.23** | "Base: PPL 4.23" | Base model perplexity IID TF |
| 24 | **0.01** | "Base: GAR-O 0.01" | Base model GAR-ours held-out TF |
| 24 | **0.00** | "Base: GAR-D 0.00" | Base model GAR-Dongre held-out TF |
| 24 | **4.34** | "Base: PPL 4.34" | Base model perplexity held-out TF |
| 24 | **0.019** | "Base: GAR-O 0.019" | Base model GAR-ours AR |
| 24 | **[.014, .024]** | "95% CI [.014, .024]" | Base model AR GAR-ours 95% CI |
| 27 | **0.50** | "ThreadGate: GAR-O 0.50" | ThreadGate GAR-ours IID TF |
| 27 | **0.02** | "ThreadGate: GAR-D 0.02" | ThreadGate GAR-Dongre IID TF |
| 27 | **2.78** | "ThreadGate: PPL 2.78" | ThreadGate perplexity IID TF |
| 27 | **0.50** | "ThreadGate: GAR-O 0.50" | ThreadGate GAR-ours held-out TF |
| 27 | **0.02** | "ThreadGate: GAR-D 0.02" | ThreadGate GAR-Dongre held-out TF |
| 27 | **2.78** | "ThreadGate: PPL 2.78" | ThreadGate perplexity held-out TF |
| 27 | **0.064** | "ThreadGate: GAR-O 0.064" | ThreadGate GAR-ours AR |
| 27 | **[.041, .091]** | "95% CI [.041, .091]" | ThreadGate AR GAR-ours 95% CI |
| 27 | **.93 ± .05** | "ḡ ± σ_g = .93 ± .05" | ThreadGate gate mean ± std across 28 layers |
| 28 | **0.50** | "+PCGrad: GAR-O 0.50" | +PCGrad GAR-ours IID TF |
| 28 | **0.01** | "+PCGrad: GAR-D 0.01" | +PCGrad GAR-Dongre IID TF |
| 28 | **2.78** | "+PCGrad: PPL 2.78" | +PCGrad perplexity IID TF |
| 28 | **0.50** | "+PCGrad: GAR-O 0.50" | +PCGrad GAR-ours held-out TF |
| 28 | **0.01** | "+PCGrad: GAR-D 0.01" | +PCGrad GAR-Dongre held-out TF |
| 28 | **2.78** | "+PCGrad: PPL 2.78" | +PCGrad perplexity held-out TF |
| 28 | **0.030** | "+PCGrad: GAR-O 0.030" | +PCGrad GAR-ours AR |
| 28 | **[.023, .038]** | "95% CI [.023, .038]" | +PCGrad AR GAR-ours 95% CI |
| 29 | **0.49** | "Uniform Gate: GAR-O 0.49" | Uniform Gate GAR-ours IID TF |
| 29 | **0.01** | "Uniform Gate: GAR-D 0.01" | Uniform Gate GAR-Dongre IID TF |
| 29 | **2.78** | "Uniform Gate: PPL 2.78" | Uniform Gate perplexity IID TF |
| 29 | **0.51** | "Uniform Gate: GAR-O 0.51" | Uniform Gate GAR-ours held-out TF (highest) |
| 29 | **0.01** | "Uniform Gate: GAR-D 0.01" | Uniform Gate GAR-Dongre held-out TF |
| 29 | **2.78** | "Uniform Gate: PPL 2.78" | Uniform Gate perplexity held-out TF |
| 29 | **0.033** | "Uniform Gate: GAR-O 0.033" | Uniform Gate GAR-ours AR |
| 29 | **[.025, .043]** | "95% CI [.025, .043]" | Uniform Gate AR GAR-ours 95% CI |
| 29 | **.96 ± .05** | "ḡ ± σ_g = .96 ± .05" | Uniform Gate gate mean ± std across 28 layers |
| 32 | **0.50** | "LoRA-only: GAR-O 0.50" | LoRA-only GAR-ours IID TF |
| 32 | **0.01** | "LoRA-only: GAR-D 0.01" | LoRA-only GAR-Dongre IID TF |
| 32 | **2.78** | "LoRA-only: PPL 2.78" | LoRA-only perplexity IID TF |
| 32 | **0.50** | "LoRA-only: GAR-O 0.50" | LoRA-only GAR-ours held-out TF |
| 32 | **0.01** | "LoRA-only: GAR-D 0.01" | LoRA-only GAR-Dongre held-out TF |
| 32 | **2.78** | "LoRA-only: PPL 2.78" | LoRA-only perplexity held-out TF |
| 32 | **0.037** | "LoRA-only: GAR-O 0.037" | LoRA-only GAR-ours AR |
| 32 | **[.027, .050]** | "95% CI [.027, .050]" | LoRA-only AR GAR-ours 95% CI |
| 32 | **1.00** | "LoRA-only: ḡ = 1.00" | LoRA-only gate mean (no gates, fixed at 1.00) |

---

### method.tex

| Line | Number | Context | What it refers to |
|------|--------|---------|-------------------|
| 17 | **~0.01–0.02** | "GAR-Dongre is diluted…to ~0.01–0.02 in multi-turn settings" | GAR-Dongre value range in multi-turn, low discriminative power |
| 17 | "order-of-magnitude" | "GAR-ours retains an order-of-magnitude range (0.019–0.50)" | Range of GAR-ours across configurations |
| 17 | **0.019–0.50** | "order-of-magnitude range (0.019–0.50)" | GAR-ours range across all variants |
| 17 | **0.200** | "correlation…is weak; r = 0.200" | Pearson r between GAR and instruction retention |
| 17 | **0.007** | "p = 0.007" | p-value for GAR–compliance correlation |
| 24 | **5** | "N = 5 conversations, 10 turns" | Number of conversations for per-turn GAR plot (figure caption) |
| 24 | **10** | "N = 5 conversations, 10 turns" | Number of turns in per-turn GAR plot (figure caption) |
| 24 | **77–81%** | "77–81% decay" | Decay range for fine-tuned variants under AR (figure caption) |
| 24 | **3.3 pp** | "Δ = 3.3 pp between ThreadGate and LoRA-only" | Difference between best and worst fine-tuned variants (figure caption) |
| 24 | **87.5%** | "Base decays 87.5%" | Base model per-turn GAR decay under AR (figure caption) |
| 32 | **σ(1.5) ≈ 0.82** | "initialized near identity (σ(1.5) ≈ 0.82)" | Gate initialization value (sigmoid of 1.5 bias) |
| 32 | **3** | "three ways" | Number of differences between ThreadGate and ReZero |
| 34 | **16** | "proj(·) reduces the hidden dimension to 16" | Projection output dim in gate MLP |
| 34 | **16** | "16-dimensional turn embedding" | Turn embedding dimensionality |
| 34 | **32** | "32-dimensional input" | Gate MLP input size (16 + 16) |
| 34 | **64** | "64-unit hidden layer" | Gate MLP hidden layer size |
| 34 | **28** | "For Qwen-2.5-7B (L = 28)" | Number of layers in Qwen-2.5-7B |
| 34 | **~57K** | "adds ~57K parameters" | Total new parameters added by ThreadGate |
| 34 | **<0.001%** | "<0.001% of 7B" | ThreadGate parameters as fraction of model |
| 34 | **1.5** | "gate biases are initialized to 1.5" | Gate bias initialization value |
| 34 | **~82%** | "(~82% pass-through)" | Gate pass-through rate at initialization |
| 34 | **10×** | "gate parameters receive a 10× learning rate multiplier" | LR multiplier for gate parameters |
| 51 | **0.5** | "τ = 0.5 targets allocating half of the last token's attention" | GAR optimization target |
| 53 | **0.05** | "σ_min = 0.05 is a minimum standard deviation threshold" | Gate diversity loss threshold |
| 55 | **1.0** | "λ_GAR = λ_div = 1.0" | Loss weights for GAR and diversity terms |
| 55 | **7** | "seven iterations spanning four loss families" | Number of loss design iterations |
| 55 | **4** | "four loss families" | Number of loss families explored |
| 55 | **v1–v2, v3–v6** | "cumulative (v1–v2) and maximize (v3–v6)" | Loss version numbering |

---

### experiments.tex

| Line | Number | Context | What it refers to |
|------|--------|---------|-------------------|
| 6 | **8K** | "8K multi-turn conversations from the UltraChat" | Training set size |
| 6 | **3** | "Training uses 3 epochs" | Number of training epochs |
| 6 | **2 × 10⁻⁴** | "lr = 2 × 10⁻⁴" | Learning rate |
| 6 | **1** | "batch size 1" | Batch size |
| 6 | **8** | "gradient accumulation 8" | Gradient accumulation steps |
| 6 | **42** | "seed 42" | Primary training seed |
| 6 | **123** | "seed 123" | Secondary training seed (ThreadGate) |
| 6 | **~6 hours** | "approximately 6 hours" | Training time per variant |
| 6 | **96 GB** | "96 GB" | GPU VRAM (NVIDIA RTX PRO 6000 Blackwell) |
| 6 | **50** | "50 non-overlapping conversations" | Held-out evaluation set size |
| 10 | **0.49–0.51** | "GAR-ours spans 0.49–0.51" | TF GAR-ours range across fine-tuned variants |
| 10 | **≤2 pp** | "≤2 pp" | TF GAR-ours spread |
| 10 | **2.78** | "PPL is 2.78 for all" | Perplexity for all fine-tuned variants under TF |
| 10 | **≤1 pp** | "held-out GAR-ours differs by ≤1 pp" | IID vs held-out GAR difference |
| 10 | **0.01–0.02** | "GAR-Dongre remains low (0.01–0.02)" | GAR-Dongre range under TF |
| 12 | **50** | "AR generation (N = 50)" | Number of AR evaluation conversations |
| 12 | **0.019–0.064** | "GAR-ours drops to 0.019–0.064" | AR GAR-ours range |
| 12 | **8–17×** | "8–17× gap" | TF-AR collapse ratio under AR |
| 12 | **0.064** | "ThreadGate 0.064" | ThreadGate AR GAR-ours |
| 12 | **0.037** | "LoRA-only 0.037" | LoRA-only AR GAR-ours |
| 12 | **0.033** | "Uniform Gate 0.033" | Uniform Gate AR GAR-ours |
| 12 | **0.030** | "PCGrad 0.030" | +PCGrad AR GAR-ours |
| 12 | **0.019** | "Base 0.019" | Base model AR GAR-ours |
| 12 | **0.004** | "p = 0.004" | p-value for ThreadGate vs. LoRA-only AR difference |
| 12 | **7.8×** | "the gap remains 7.8×" | TF-AR gap after ThreadGate training |
| 12 | **0.504 ± 0.001** | "second seed confirms TF stability (0.504 ± 0.001)" | Second-seed TF GAR-ours mean ± std |
| 12 | **0.8 pp** | "MMLU 5-shot accuracy remains within 0.8 pp" | MMLU accuracy change across variants |
| 17 | **0.064** | "recovering GAR from 0.064" | ThreadGate AR GAR-ours (steering starting point) |
| 17 | **0.727** | "to 0.727" | GAR after β-steering at β=5 |
| 17 | **9%** | "9% PPL cost" | PPL cost at β=3 (figure caption) |
| 17 | **3** | "phase transition at β ∈ [2, 3]" | β range for phase transition |
| 17 | **2** | "β ∈ [2, 3]" | Lower bound of phase transition range |
| 27 | **β = 3** | "β = 3 triggers a phase transition" | β value at phase transition |
| 27 | **0.556** | "GAR = 0.556 (9% PPL cost)" | GAR after β=3 phase transition |
| 27 | **9%** | "(9% PPL cost)" | PPL cost at β=3 |
| 27 | **β = 5** | "At β = 5" | β value for maximum steering |
| 27 | **0.727 ± 0.061** | "GAR reaches 0.727 ± 0.061" | GAR at β=5 (mean ± std) |
| 27 | **1.77** | "PPL 1.77" | Perplexity at β=5 |
| 27 | **[3, 5]** | "operating region β ∈ [3, 5]" | Useful β range |
| 27 | **1.8** | "PPL remains below 1.8" | PPL upper bound in operating region |
| 27 | **+11.1 pp** | "raises late-turn instruction compliance by +11.1 pp" | Instruction compliance improvement from β=3 steering |
| 27 | **0.077** | "p = 0.077" | p-value for steering instruction compliance (not significant) |
| 27 | **+23.8 pp** | "content-constrained tasks benefit most, +23.8 pp" | Instruction compliance improvement for content-constrained tasks |
| 38 | **7.8×** | "gap from 7.8×" | Pre-SS gap for Qwen (figure caption) |
| 38 | **~1.3×** | "to ~1.3×" | Post-SS gap for Qwen (figure caption) |
| 38 | **0.401 ± 0.047** | "AR GAR-ours rises to 0.401 ± 0.047" | SS AR GAR-ours mean ± std (three seeds) |
| 38 | **7.8×** | "compressing the gap from 7.8×" | Pre-SS gap |
| 38 | **~1.3×** | "to ~1.3×" | Post-SS gap for Qwen |
| 38 | **0.498 ± 0.004** | "TF GAR 0.498 ± 0.004" | SS TF GAR-ours mean ± std |
| 38 | **1.441 ± 0.001** | "PPL cost (1.441 ± 0.001)" | SS PPL mean ± std |
| 38 | **β = 5** | "Steering on SS models…β = 5" | β value for SS steering |
| 38 | **0.717 ± 0.001** | "0.717 ± 0.001" | SS + β=5 steering GAR mean ± std |
| 38 | **0.047 → 0.001** | "std 0.047 → 0.001" | Seed variance before/after steering |
| 38 | **0.36** | "mid-turn GAR above 0.36 for all token-position variants" | SS mid-turn GAR lower bound |
| 38 | **~27×** | "gap from ~27×" | Pre-SS gap for Llama |
| 38 | **2.9×** | "to 2.9×" | Post-SS gap for Llama |
| 38 | **2 vs. 3** | "fewer training epochs (2 vs. 3)" | Llama vs. Qwen training epochs |
| 38 | **3** | "across three seeds" | Number of seeds for SS |

---

### analysis.tex

| Line | Number | Context | What it refers to |
|------|--------|---------|-------------------|
| 6 | **1 vs 21** | "turn 1 vs turn 21" | Turn indices for gate comparison (figure caption) |
| 6 | **27/28** | "27/28 layers" | Fraction of layers where gates approach 1.0 at late turns (figure caption) |
| 6 | **1.0** | "gates approach 1.0 at late turns" | Gate value at late turns (figure caption) |
| 6 | **3.73 × 10⁻⁸** | "p = 3.73 × 10⁻⁸" | Wilcoxon p-value for gate inversion (figure caption) |
| 6 | **5** | "N = 5 pilot" | Number of pilot conversations (figure caption) |
| 6 | **20–34×** | "Pilot gaps (20–34×)" | Pilot TF-AR gap estimates (figure caption) |
| 6 | **8–17×** | "vs. 8–17× (Table 1)" | Final N=50 TF-AR gap estimates (figure caption) |
| 14 | **1** | "turn 1 (early)" | Early turn index |
| 14 | **21** | "turn 21 (late)" | Late turn index |
| 14 | **28** | "across all 28 layers" | Number of Qwen layers |
| 14 | **27/28** | "in 27/28 layers" | Fraction of layers where gates are lower at turn 1 |
| 14 | **3.73 × 10⁻⁸** | "Wilcoxon p = 3.73 × 10⁻⁸" | p-value for gate turn conditioning inversion |
| 14 | **0.975** | "r = 0.975" | Effect size r for Wilcoxon test |
| 14 | **0.769** | "layer 23 shifts from 0.769" | Gate value at turn 1, layer 23 |
| 14 | **0.979** | "to 0.979" | Gate value at turn 21, layer 23 |
| 14 | **1.0** | "NTP pressure pushes gates toward 1.0" | Gate convergence value |
| 14 | **0.93–0.98** | "inference-time values of 0.93–0.98" | Gate value range at inference |
| 14 | **2–7%** | "(2–7% attenuation)" | Attenuation range from gates |
| 14 | **L3 = 0.777** | "L3 = 0.777" | Uniform Gate value at layer 3 |
| 14 | **L27 = 1.000** | "L27 = 1.000" | Uniform Gate value at layer 27 |
| 18 | **68–79%** | "NTP and GAR gradients oppose in 68–79% of layers" | Fraction of layers with opposing gradients |
| 18 | **−0.089 → −0.042** | "cosine similarity −0.089 → −0.042 across epochs" | Cosine similarity range over training |
| 18 | **7.5×** | "NTP magnitude dominance growing from 7.5×" | Early-epoch NTP/GAR gradient magnitude ratio |
| 18 | **14.7×** | "to 14.7×" | Late-epoch NTP/GAR gradient magnitude ratio |
| 20 | **0.064 → 0.030** | "AR GAR worsens: 0.064 → 0.030" | ThreadGate vs. +PCGrad AR GAR |
| 20 | **0.002** | "p = 0.002" | p-value for PCGrad AR GAR worsening |
| 20 | **7.5–14.7×** | "NTP dominates GAR by 7.5–14.7×" | NTP/GAR gradient magnitude range |
| 20 | **+0.005** | "Llama-3.1-8B gradients are near-orthogonal (cos = +0.005)" | Llama gradient cosine similarity |
| 20 | **25.7×** | "25.7× NTP magnitude dominance" | Llama NTP/GAR gradient magnitude ratio |
| 24 | **0.334/0.332** | "TF/AR TRC is 0.334/0.332 for ThreadGate" | ThreadGate TF/AR Turn-level Residual Coherence |
| 24 | **+0.002** | "(gap +0.002)" | TF-AR TRC gap for ThreadGate |
| 24 | **0.349/0.411** | "0.349/0.411 for LoRA-only" | LoRA-only TF/AR TRC |
| 24 | **−0.062** | "(gap −0.062, reversed)" | TF-AR TRC gap for LoRA-only (reversed direction) |
| 24 | **1.002×** | "GAR-Dongre shows negligible shift on both Llama (1.002×)" | Llama GAR-Dongre TF-AR shift |
| 24 | **1.28×** | "and Qwen (1.28×)" | Qwen GAR-Dongre TF-AR shift |
| 38 | **20** | "N = 20" | Number of conversations for Llama evaluation |
| 38 | **4** | "4 turns" | Number of turns per Llama conversation |
| 38 | **0.484** | "TF GAR-ours is 0.484 (TG)" | Llama ThreadGate TF GAR-ours |
| 38 | **0.481** | "0.481 (LoRA-only)" | Llama LoRA-only TF GAR-ours |
| 38 | **100%** | "coefficient of variation, CoV > 100%" | Llama AR distribution heavy-tailed indicator |
| 38 | **0.018** | "medians: 0.018 (TG and LoRA-only)" | Llama median AR GAR-ours for TG and LoRA-only |
| 38 | **0.009** | "0.009 (Base)" | Llama Base median AR GAR-ours |
| 38 | **27×** | "gaps of 27×" | Llama TG TF-AR gap |
| 38 | **26×** | "and 26×" | Llama LoRA-only TF-AR gap |
| 38 | **L1 = 0.793** | "Qwen attenuates early layers (L1 = 0.793)" | Qwen gate value at layer 1 |
| 38 | **L25 = 0.719** | "Llama dips at late layers (L25 = 0.719)" | Llama gate value at layer 25 |
| 41 | **~27×** | "Llama SS compresses the gap from ~27×" | Llama pre-SS gap |
| 41 | **2.9×** | "to 2.9×" | Llama post-SS gap |
| 41 | **0.477** | "TF GAR 0.477" | Llama SS TF GAR-ours |
| 41 | **0.166** | "AR GAR 0.166" | Llama SS AR GAR-ours |
| 41 | **~1.3×** | "weaker than Qwen's ~1.3×" | Qwen post-SS gap (reference) |
| 41 | **2 vs. 3** | "fewer training epochs (2 vs. 3)" | Llama vs. Qwen training epochs |
| 41 | **β = 3** | "β = 3 triggers recovery on Qwen SS" | β value for Qwen SS phase transition |
| 41 | **0.593** | "Qwen SS (0.593)" | Qwen SS GAR at β=3 |
| 41 | **0.173** | "not Llama SS (0.173)" | Llama SS GAR at β=3 (no phase transition) |
| 41 | **β = 5** | "Llama requires β = 5" | Llama SS β for phase transition |
| 41 | **0.791** | "GAR 0.791" | Llama SS GAR at β=5 |
| 41 | **0.717** | "exceeding Qwen SS 0.717" | Qwen SS GAR at β=5 (reference) |
| 41 | **79.8%** | "79.8% GAR decay" | Qwen-2.5-1.5B GAR decay under AR |
| 41 | **0.715** | "β-steering recovery to 0.715" | Qwen-2.5-1.5B GAR at β=5 steering |

---

### discussion.tex

| Line | Number | Context | What it refers to |
|------|--------|---------|-------------------|
| 3 | "order of magnitude" | "GAR-ours collapses by an order of magnitude" | Magnitude of AR GAR collapse |
| 3 | **≤1.3×** | "GAR-Dongre shows negligible shift (≤1.3×)" | GAR-Dongre TF-AR shift upper bound |
| 3 | **0.743** | "r = 0.743" | Pearson r between per-head TF GAR and AR shift |
| 5 | **7.5–25.7×** | "magnitude imbalance (7.5–25.7× NTP dominance)" | NTP/GAR gradient magnitude ratio range |
| 5 | **0.200** | "GAR–compliance correlation is weak (r = 0.200)" | GAR-compliance correlation |
| 5 | **0.717** | "SS = 0.717" | SS + β=5 steering GAR (Qwen) |
| 5 | **0.727** | "vs. TG = 0.727" | ThreadGate + β=5 steering GAR |

---

### conclusion.tex

| Line | Number | Context | What it refers to |
|------|--------|---------|-------------------|
| 3 | **0.50** | "auxiliary attention losses converge under teacher forcing (GAR = 0.50)" | TF GAR target value |
| 3 | "order of magnitude" | "collapse by an order of magnitude under autoregressive generation" | AR GAR collapse magnitude |
| 3 | **2** | "on two architectures" | Number of architectures tested |
| 3 | **~1.3×** | "gap to ~1.3× (Qwen)" | Post-SS TF-AR gap for Qwen |
| 3 | **~2.9×** | "and ~2.9× (Llama)" | Post-SS TF-AR gap for Llama |

---

### limitations.tex

| Line | Number | Context | What it refers to |
|------|--------|---------|-------------------|
| 3 | **2** | "demonstrated on two model families" | Number of model families |
| 3 | **8K** | "a single dataset (UltraChat, 8K conversations)" | Training dataset size |
| 3 | **1** | "Most configurations use a single seed" | Number of seeds for most configs |
| 3 | **3** | "scheduled sampling validated on three seeds" | Seeds for SS validation |
| 3 | **0.5** | "GAR with MSE target τ = 0.5" | GAR loss target value |

---

## Summary: Key Numbers by Category

**Model sizes:** 7B, 8B, 1.5B, 15B  
**Dataset:** 8K training conversations, 50 held-out, N=20 (Llama eval), N=5 (pilot/heatmap), mean 3.6 user turns  
**Training HPs:** lr=2×10⁻⁴, batch=1, grad_accum=8, epochs=3 (Qwen)/2 (Llama), seeds 42/123, ~6h/run  
**Architecture HPs (ThreadGate):** proj_dim=16, turn_emb_dim=16, hidden=64, bias_init=1.5 (~82%), gate_lr_mult=10×, σ_min=0.05, λ_GAR=λ_div=1.0, τ=0.5, ~57K added params (<0.001%)  
**Core results:** TF GAR≈0.50; AR GAR 0.019–0.064; 8–17× collapse (Qwen), 27× (Llama); SS: Qwen ~1.3×, Llama 2.9×  
**Steering:** β=3 → GAR=0.556 (9% PPL), β=5 → GAR=0.727±0.061 (PPL 1.77), +11.1pp compliance (+23.8pp content-constrained), p=0.077  
**Statistical:** p=0.002 (PCGrad), p=0.004 (TG vs LoRA-only), p=0.077 (steering compliance), p=3.73×10⁻⁸ (gate Wilcoxon), r=0.200 (GAR-compliance), r=0.743 (per-head), AUC=0.98 (probes)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e178ee0-fa1f-4156-9c53-65f585e75ca2",
  "isSidechain": true,
  "agentId": "a5748595957c992d4",
  "requestId": "req_011CbPrcoBPDVYNQhuJ1XVCL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9ff9859-c8d7-47e0-9425-cf10e2585318",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0146QyXGJzwV1h5xkHC9FMph",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 45368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
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
