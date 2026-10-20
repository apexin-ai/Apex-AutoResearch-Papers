# Research conversation: I received a paper quality audit report for a LaTeX paper. Many of the "critical" findings may be based on stale file re

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ae011bee35620c3ee.jsonl`
- **Structured JSON:** [`6a3961ec32e15dfd786e.json`](../../sessions/6a/6a3961ec32e15dfd786e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-25T14:27:19.588Z_

I received a paper quality audit report for a LaTeX paper. Many of the "critical" findings may be based on stale file reads. I need you to verify the current state of the paper files to determine which issues are real and which are false positives.

The paper is at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/

Check these specific claims from the audit:

1. **[CRITICAL] Introduction C4 "ongoing work"**: Read `sections/introduction.tex` and check if contribution #4 still says cross-model validation is ongoing/incomplete, or if it's been updated with actual results.

2. **[CRITICAL] Missing figure definitions**: Read `sections/analysis.tex` and `sections/experiments.tex` fully. The audit claims fig:gate-shift, fig:training-pcgrad, fig:steering-recovery are referenced but never defined with \begin{figure}/\label. Check if these labels exist.

3. **[CRITICAL] Missing appendix**: The audit claims appendix .tex files don't exist. Check if `sections/appendix.tex` exists and contains appendix sections A, B, etc. Also check main.tex for \input{sections/appendix}.

4. **[CRITICAL] Only 1 \includegraphics**: Count ALL \includegraphics commands in the main text files (introduction.tex, method.tex, experiments.tex, analysis.tex, discussion.tex, conclusion.tex) — how many figures are actually in the main text?

5. **[CRITICAL] $\sigma_\text{min}$ undefined**: Read `sections/method.tex` — is $\sigma_\text{min}$ defined with a specific numerical value?

6. **[WARNING] fig1_overview still used as main figure**: Check what figure is used as Figure 1 / the headline figure. Is it fig1_overview.pdf or fig1_headline.pdf?

7. **[WARNING] Limitations too long**: Read `sections/limitations.tex` — count paragraphs and limitation points.

8. **[WARNING] experiments.tex references Appendix~A**: Check experiments.tex for appendix references and verify those appendix sections exist in appendix.tex.

For each finding, report: TRUE (issue exists), FALSE (issue is a false positive), or PARTIAL (partially true). Be precise and cite line numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7335ce9b-d729-4c25-828e-fb66579eb012",
  "agentId": "ae011bee35620c3ee",
  "type": "user",
  "uuid": "c614842e-1738-440a-90da-017c9f29f957",
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

_source line 2 · 2026-05-25T14:27:19.592Z_

```json
{
  "parentUuid": "c614842e-1738-440a-90da-017c9f29f957",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
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
  "uuid": "f6b19026-e2d1-43da-8ca1-8c6679834662",
  "timestamp": "2026-05-25T14:27:19.592Z",
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

_source line 3 · 2026-05-25T14:27:22.192Z_



I'll read all the relevant files in parallel to verify each claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6b19026-e2d1-43da-8ca1-8c6679834662",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
  "requestId": "req_011CbPSg5SigiNK6RisZcR2N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60520b88-472f-4be7-af19-fbfbc506db2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jH4DZc8ktoZq4adc2FcBA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34693,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34693,
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

_source line 4 · 2026-05-25T14:27:22.684Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BJm5i6Y6zGvwMoGpWhhCdm`</summary>

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
  "parentUuid": "60520b88-472f-4be7-af19-fbfbc506db2c",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
  "requestId": "req_011CbPSg5SigiNK6RisZcR2N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffe837ae-6cae-4843-9484-bc1ed7095b6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jH4DZc8ktoZq4adc2FcBA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34693,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34693,
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

_source line 5 · 2026-05-25T14:27:22.708Z_

<details><summary>↩ Tool result · `toolu_01BJm5i6Y6zGvwMoGpWhhCdm`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is central to how large language models are deployed---from customer service to tutoring to long-form reasoning. Yet a persistent failure accompanies even the most fluent generation: as conversations grow longer, models pay progressively less attention to the system-prompt goals that define their task. \citet{dongre2026attention} measured significant Goal Accessibility Ratio (GAR) decline across 12 models over extended conversations; in our own evaluation, goal attention drops by over 70\% within just five turns. Crucially, this is not a representation problem---residual stream probes confirm that goal information persists (AUC\,=\,0.98). The model retains the knowledge of what it should attend to; it simply stops attending.
4	
5	Existing remedies address this decay at inference time. Split-softmax \citep{li2024measuring} separates instruction from conversation tokens; StreamingLLM \citep{xiao2024streaming} retains anchor tokens; Gated Attention \citep{qiu2025gated} applies per-head sigmoid gates within a single forward pass. A natural alternative is to intervene during training: optimize goal attention directly through auxiliary losses trained alongside next-token prediction (NTP). Yet this strategy rests on an untested assumption---that attention patterns learned under teacher forcing (TF) transfer to autoregressive (AR) generation. Classical exposure bias research \citep{bengio2015scheduled,lamb2016professor} has shown that TF creates a training--inference distribution mismatch for RNN sequence models, but whether this mismatch extends to auxiliary attention objectives in multi-turn transformers remains unknown.
6	
7	We test this assumption and find it fails. We introduce a controlled five-way testbed---ThreadGate, +PCGrad, Uniform Gate, LoRA-only, and Base---designed not as competing solutions but as a causal exclusion chain (\S\ref{sec:comparison-design}), where each adjacent pair isolates one candidate failure mechanism. The result is unambiguous: every variant converges to target GAR under teacher forcing, yet goal attention collapses by an order of magnitude once the model generates its own context (Figure~\ref{fig:headline}). The exclusion chain traces this collapse to exposure bias---the training--inference distribution mismatch---ruling out gradient direction conflict (PCGrad removes conflict yet \emph{worsens} AR GAR), gating mechanism (Uniform Gate matches ThreadGate), and parameter capacity (LoRA-only shows the same pattern). Inference-time $\beta$-steering confirms that the collapse reflects attention misallocation rather than representation degradation; scheduled sampling bridges the gap by exposing the model to its own generations during training.
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
18	    \item \textbf{Exposure bias characterization.} The first empirical demonstration that exposure bias collapses auxiliary attention objectives in multi-turn transformers, with an order-of-magnitude TF--AR gap reproduced across two architectures (Qwen-2.5-7B, Llama-3.1-8B) and model scales (1.5B--8B).
19	    \item \textbf{Causal exclusion testbed.} A five-way diagnostic design, informed by seven loss-formulation iterations, that isolates the failure mechanism via causal exclusion---including a PCGrad \emph{modus tollens} argument ruling out gradient direction conflict ($p$\,=\,0.002, effect reverses).
20	    \item \textbf{Attention misallocation diagnosis.} Inference-time $\beta$-steering recovers goal attention with modest perplexity cost, confirming that the collapse is an attention routing failure, not a representational one.
21	    \item \textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\sim}$1.3$\times$ on Qwen and ${\sim}$2.9$\times$ on Llama with no perplexity degradation, robust across three seeds.
22	\end{enumerate}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffe837ae-6cae-4843-9484-bc1ed7095b6f",
  "isSidechain": true,
  "promptId": "7335ce9b-d729-4c25-828e-fb66579eb012",
  "agentId": "ae011bee35620c3ee",
  "type": "user",
  "uuid": "89d88f60-2cd1-4e76-8186-428198968298",
  "sourceToolAssistantUUID": "ffe837ae-6cae-4843-9484-bc1ed7095b6f",
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

_source line 6 · 2026-05-25T14:27:23.154Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LEox7qE66Jyv1ZAMmszAQ9`</summary>

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
  "parentUuid": "89d88f60-2cd1-4e76-8186-428198968298",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
  "requestId": "req_011CbPSg5SigiNK6RisZcR2N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4cd92c5-8b66-4bdb-bde7-0fb77a5910f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jH4DZc8ktoZq4adc2FcBA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34693,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34693,
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

_source line 7 · 2026-05-25T14:27:23.161Z_

<details><summary>↩ Tool result · `toolu_01LEox7qE66Jyv1ZAMmszAQ9`</summary>

```text
1	\section{Analysis}\label{sec:analysis}
2	
3	Each subsection kills one alternative hypothesis via causal exclusion: \S\ref{subsec:gate-conditioning}~turn conditioning, \S\ref{subsec:pcgrad}~gradient direction conflict, leaving exposure bias as the primary remaining explanation consistent with current evidence (\S\ref{subsec:dist-shift}). \S\ref{subsec:mechanism-specificity} confirms selectivity; \S\ref{subsec:cross-model} confirms cross-architecture generalization.
4	
5	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
6	
7	We compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\% attenuation; Table~\ref{tab:four-way}; full gate profiles in Appendix~\ref{sec:appendix-gate-profile}; training dynamics in Appendix~\ref{sec:appendix-training-ext}). The Uniform Gate learns comparable per-layer variation (L3\,=\,0.777, L27\,=\,1.000) despite lacking turn conditioning, confirming the structure arises from LoRA$+$GAR pressure (Figure~\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?
8	
9	\subsection{PCGrad Gradient Direction Conflict Exclusion}\label{subsec:pcgrad}
10	
11	NTP and GAR gradients oppose in 68--79\% of layers (cosine similarity $-$0.089$\to$$-$0.042 across epochs), with NTP magnitude dominance growing from 7.5$\times$ to 14.7$\times$ (full gradient statistics in Appendix~\ref{sec:appendix-gradient}). If this direction conflict prevents GAR convergence, eliminating it via PCGrad \citep{yu2020pcgrad}, which projects conflicting gradients onto the other's normal plane, should prevent the collapse. To our knowledge, this is the first application of PCGrad as a \emph{diagnostic} tool rather than an optimization method.
12	
13	PCGrad shifts cosine similarity to oscillate around zero, yet TF metrics are unchanged. AR GAR \emph{worsens}: 0.064$\to$0.030 ($p$\,=\,0.002; Figure~\ref{fig:training-pcgrad}b in Appendix~\ref{sec:appendix-gradient}). By \emph{modus tollens}: removing gradient direction conflict does not prevent collapse; therefore it is not the primary cause. PCGrad eliminates direction conflict but does not address magnitude imbalance (NTP dominates GAR by 7.5--14.7$\times$); the worsening under PCGrad may partly reflect projection side-effects rather than confirming that direction conflict is entirely absent as a factor. Cross-model analysis confirms this pattern: Llama-3.1-8B gradients are near-orthogonal (cos\,=\,+0.005) with 25.7$\times$ NTP magnitude dominance (Table~\ref{tab:gradient-crossmodel}).
14	
15	\subsection{Distribution Shift Analysis}\label{subsec:dist-shift}
16	
17	The TF-AR GAR gap persists across all variants (Table~\ref{tab:four-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, confirming that the shift selectively destroys concentrated last-token attention. The mechanism is exposure bias \citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. GAR optimizes a distributional property with no autoregressive counterpart, explaining why TF GAR-ours remains near $\tau$\,=\,0.5 while AR GAR collapses (77--87\% per-turn decay; Figure~\ref{fig:attention-heatmap}; per-configuration AR trajectories in Appendix~\ref{sec:appendix-ar-gar-dynamics}; scaling analysis in Appendix~\ref{sec:appendix-eb-scaling}).
18	
19	\subsection{Mechanism Specificity}\label{subsec:mechanism-specificity}
20	
21	We test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed), confirming exposure bias disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\times$) and Qwen (1.28$\times$) vs.\ the order-of-magnitude GAR-ours collapse.
22	
23	\begin{figure}[H]
24	  \centering
25	  \includegraphics[width=\columnwidth]{fig_ss_multiseed.pdf}
26	  \caption{Multi-seed AR GAR under scheduled sampling ($\beta$\,=\,0 and $\beta$\,=\,5, three seeds). Steering nearly eliminates seed variance (std: 0.047$\to$0.001).}
27	  \label{fig:ss-multiseed}
28	\end{figure}
29	
30	\subsection{Cross-Model Replication}\label{subsec:cross-model}
31	
32	We replicate on Llama-3.1-8B-Instruct \citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\,=\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\,$>$\,100\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\times$ and 26$\times$ (Figure~\ref{fig:crossmodel}a in Appendix~\ref{sec:appendix-llama}; per-turn values in Appendix~\ref{sec:appendix-perturn-detail}). Gate profiles differ qualitatively (Figure~\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\,=\,0.793) while Llama dips at late layers (L25\,=\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.
33	
34	Scheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\sim}$27$\times$ to 2.9$\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\sim}$1.3$\times$ likely due to fewer training epochs (2 vs.\ 3). The phase transition is architecture-dependent: $\beta$\,=\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\beta$\,=\,5 (GAR 0.791, exceeding Qwen SS 0.717; Appendix~\ref{sec:appendix-llama-ss}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern (79.8\% GAR decay, $\beta$-steering recovery to 0.715; Appendix~\ref{sec:appendix-1.5b}).
35	
36	\begin{figure}[H]
37	  \centering
38	  \includegraphics[width=\columnwidth]{fig3_gate_shift.pdf}
39	  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift ($N$\,=\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\times$) exceed final $N$\,=\,50 estimates (8--17$\times$; Table~\ref{tab:four-way}) due to smaller sample size.}
40	  \label{fig:gate-shift}
41	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4cd92c5-8b66-4bdb-bde7-0fb77a5910f8",
  "isSidechain": true,
  "promptId": "7335ce9b-d729-4c25-828e-fb66579eb012",
  "agentId": "ae011bee35620c3ee",
  "type": "user",
  "uuid": "3bd62e93-698d-4591-a113-56503c9d3b81",
  "sourceToolAssistantUUID": "b4cd92c5-8b66-4bdb-bde7-0fb77a5910f8",
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

_source line 8 · 2026-05-25T14:27:23.633Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Kyf8Lnw8TbUpnvDRjn3AgZ`</summary>

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
  "parentUuid": "3bd62e93-698d-4591-a113-56503c9d3b81",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
  "requestId": "req_011CbPSg5SigiNK6RisZcR2N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a3603ce-6493-462b-9f9c-77d9cf3cb706",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jH4DZc8ktoZq4adc2FcBA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34693,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34693,
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

_source line 9 · 2026-05-25T14:27:23.640Z_

<details><summary>↩ Tool result · `toolu_01Kyf8Lnw8TbUpnvDRjn3AgZ`</summary>

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
10	Table~\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\leq$2\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\leq$1\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, confirming that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\S\ref{subsec:ss}).
11	
12	Under AR generation ($N$\,=\,50), GAR-ours drops to 0.019--0.064, an 8--17$\times$ gap (Figure~\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\ LoRA-only is significant ($p$\,=\,0.004; Appendices~\ref{sec:appendix-stats} and~\ref{sec:appendix-stats-ext}), yet the gap remains 7.8$\times$. A second seed confirms TF stability ($0.504\pm0.001$). MMLU 5-shot accuracy remains within 0.8\,pp across all variants (per-category breakdown in Appendix~\ref{sec:appendix-mmlu-ext}). We analyze this distribution shift in \S\ref{sec:analysis}.
13	
14	\subsection{Inference-Time Attention Steering}\label{subsec:steering}
15	
16	\begin{figure}[t]
17	  \centering
18	  \includegraphics[width=\columnwidth]{fig5_attention_steering.pdf}
19	  \caption{Inference-time $\beta$-steering recovers GAR from 0.064 to 0.727, confirming attention misallocation as a proximal cause (9\% PPL cost at $\beta$\,=\,3; phase transition at $\beta \in [2, 3]$).}
20	  \label{fig:steering-recovery}
21	\end{figure}
22	
23	All training-time interventions leave the exposure bias gap intact. If the collapse is caused by attention misallocation rather than representation degradation, then directly correcting attention should recover GAR. We test this by adding a constant bias $\beta$ to pre-softmax attention logits for goal-token positions during generation:
24	\begin{equation}
25	  \tilde{A}_{i,j}^{(\ell,h)} = A_{i,j}^{(\ell,h)} + \beta \cdot \mathbf{1}[j \in \mathcal{G}],
26	\end{equation}
27	where $\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\beta \in [0, 2]$ yields marginal improvement, then $\beta = 3$ triggers a phase transition to GAR\,=\,0.556 (9\% PPL cost). At $\beta$\,=\,5, GAR reaches 0.727$\pm$0.061 (PPL 1.77); the operating region $\beta \in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\ref{fig:steering-recovery}; full results in Appendix~\ref{sec:appendix-steering}; per-$\beta$ turn-level trajectories in Appendix~\ref{sec:appendix-steering-viz}). GAR recovery under steering is partly by construction: boosting attention logits toward goal tokens mechanically increases the attention-based metric. The stronger evidence is the counterfactual: if the collapse were due to hidden-state drift rather than attention misallocation, reweighting could not recover GAR, yet it does---consistent with attention misallocation as a proximal cause (qualitative examples in Appendix~\ref{sec:appendix-examples}). Downstream, steering ($\beta$\,=\,3) raises late-turn instruction compliance by +11.1\,pp, though this effect does not reach conventional significance ($p$\,=\,0.077; content-constrained tasks benefit most, +23.8\,pp; Appendix~\ref{sec:appendix-ir}).
28	
29	\subsection{Scheduled Sampling Compresses the TF--AR Gap}\label{subsec:ss}
30	
31	\begin{figure}[H]
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
  "parentUuid": "1a3603ce-6493-462b-9f9c-77d9cf3cb706",
  "isSidechain": true,
  "promptId": "7335ce9b-d729-4c25-828e-fb66579eb012",
  "agentId": "ae011bee35620c3ee",
  "type": "user",
  "uuid": "8fb61086-b523-4081-bd88-156d17bd9ab0",
  "sourceToolAssistantUUID": "1a3603ce-6493-462b-9f9c-77d9cf3cb706",
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

_source line 10 · 2026-05-25T14:27:24.097Z_

<details open><summary>🔧 Tool call — Read · `toolu_015F8CQWFmR5BPQa1gK11ZUs`</summary>

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
  "parentUuid": "8fb61086-b523-4081-bd88-156d17bd9ab0",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
  "requestId": "req_011CbPSg5SigiNK6RisZcR2N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a19e1f1e-f321-4739-a5d2-8369ccc2e543",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jH4DZc8ktoZq4adc2FcBA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34693,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34693,
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

_source line 11 · 2026-05-25T14:27:24.104Z_

<details><summary>↩ Tool result · `toolu_015F8CQWFmR5BPQa1gK11ZUs`</summary>

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
13	\textbf{GAR-Dongre} is the original definition (Eq.~\ref{eq:gar}), averaging over all response tokens. However, averaging dilutes the signal with intermediate positions that may legitimately attend to local context rather than the system prompt. The last token of each assistant turn is where the model aggregates information for the next continuation---attention at this position most directly reflects the model's awareness of task specifications. \textbf{GAR-ours} restricts the measurement accordingly:
14	\begin{equation}\label{eq:gar-ours}
15	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
16	\end{equation}
17	where $t_\tau$ is the last token index at turn $\tau$. Attention at this position reflects the information drawn upon for continuation; we use GAR-ours as the optimization target for $\mathcal{L}_\text{GAR}$ (\S\ref{sec:loss}). Empirically, GAR-Dongre is diluted by NTP attention patterns to ${\sim}$0.01--0.02 in multi-turn settings, losing discriminative power across configurations; GAR-ours retains an order-of-magnitude range (0.019--0.50). The contrast itself is informative: goal attention concentrates at the last-token position, and only this concentrated pattern is vulnerable to distribution shift (\S\ref{sec:analysis}). Throughout this work, GAR serves primarily as a \emph{diagnostic probe}: it measures whether auxiliary attention training transfers to autoregressive generation, rather than being an end-to-end optimization objective whose increase directly improves downstream task performance (the correlation with instruction retention is weak; $r$\,=\,0.200, $p$\,=\,0.007; \S\ref{sec:discussion}).
18	
19	\subsection{ThreadGate Architecture}
20	
21	\begin{figure}[H]
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
47	$\mathcal{L}_\text{NTP}$ is the standard next-token prediction loss. For $\mathcal{L}_\text{GAR}$, we use MSE rather than cross-entropy because GAR is a continuous ratio and MSE provides \emph{bidirectional} pressure---penalizing both under- and over-attention, preventing identity collapse (Appendix~\ref{sec:appendix-loss}):
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
  "parentUuid": "a19e1f1e-f321-4739-a5d2-8369ccc2e543",
  "isSidechain": true,
  "promptId": "7335ce9b-d729-4c25-828e-fb66579eb012",
  "agentId": "ae011bee35620c3ee",
  "type": "user",
  "uuid": "365d9901-348c-463e-9d5f-3796306007e1",
  "sourceToolAssistantUUID": "a19e1f1e-f321-4739-a5d2-8369ccc2e543",
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

_source line 12 · 2026-05-25T14:27:24.526Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TQf1SQALiFEE9vkdMftewi`</summary>

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
  "parentUuid": "365d9901-348c-463e-9d5f-3796306007e1",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
  "requestId": "req_011CbPSg5SigiNK6RisZcR2N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3cac4d4-916b-4c2c-855d-01722ee45008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jH4DZc8ktoZq4adc2FcBA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34693,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34693,
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

_source line 13 · 2026-05-25T14:27:24.532Z_

<details><summary>↩ Tool result · `toolu_01TQf1SQALiFEE9vkdMftewi`</summary>

```text
1	\section{Limitations}\label{sec:limitations}
2	
3	Our findings are demonstrated on two model families (Qwen-2.5-7B and Llama-3.1-8B) and a single dataset (UltraChat, 8K conversations); generalization to other architectures and domains (e.g., code, reasoning) is untested. Most configurations use a single seed (scheduled sampling validated on three seeds; \S\ref{subsec:ss}), and quality assessment relies on PPL rather than comprehensive benchmarks \citep{hendrycks2021measuring,lin2022truthfulqa}. We test only one auxiliary loss family (GAR with MSE target $\tau$\,=\,0.5); head-specific or layer-specific losses may exhibit different sensitivity to exposure bias.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3cac4d4-916b-4c2c-855d-01722ee45008",
  "isSidechain": true,
  "promptId": "7335ce9b-d729-4c25-828e-fb66579eb012",
  "agentId": "ae011bee35620c3ee",
  "type": "user",
  "uuid": "d53b5e0c-a1e3-47f6-aa8d-d76aafe05ac9",
  "sourceToolAssistantUUID": "c3cac4d4-916b-4c2c-855d-01722ee45008",
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

_source line 14 · 2026-05-25T14:27:25.518Z_

<details open><summary>🔧 Tool call — Read · `toolu_013YzgUiGWcwqZQZHENH3nSi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d53b5e0c-a1e3-47f6-aa8d-d76aafe05ac9",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
  "requestId": "req_011CbPSg5SigiNK6RisZcR2N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92285fd2-de11-4810-a608-041ebb4c1f8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jH4DZc8ktoZq4adc2FcBA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34693,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34693,
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

_source line 15 · 2026-05-25T14:27:25.813Z_

<details><summary>↩ Tool result · reported error · `toolu_013YzgUiGWcwqZQZHENH3nSi`</summary>

```text
File content (26122 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92285fd2-de11-4810-a608-041ebb4c1f8c",
  "isSidechain": true,
  "promptId": "7335ce9b-d729-4c25-828e-fb66579eb012",
  "agentId": "ae011bee35620c3ee",
  "type": "user",
  "uuid": "85b1a578-3c6b-40fe-b463-500c77907ef7",
  "toolUseResult": "Error: File content (26122 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "92285fd2-de11-4810-a608-041ebb4c1f8c",
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

_source line 16 · 2026-05-25T14:27:26.038Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KQS86PSvAoTHPqHamvnMG2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85b1a578-3c6b-40fe-b463-500c77907ef7",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
  "requestId": "req_011CbPSg5SigiNK6RisZcR2N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e30f6117-6a22-45a6-acc3-db6a44c0bdf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jH4DZc8ktoZq4adc2FcBA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34693,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34693,
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

_source line 17 · 2026-05-25T14:27:26.047Z_

<details><summary>↩ Tool result · `toolu_01KQS86PSvAoTHPqHamvnMG2`</summary>

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
15	\usepackage{url}
16	\usepackage{subcaption}
17	\usepackage{placeins}
18	\usepackage{float}
19	\usepackage{alphalph}
20	\usepackage{etoolbox}
21	\AtBeginEnvironment{figure}{\nolinenumbers}
22	\AfterEndEnvironment{figure}{\linenumbers}
23	\AtBeginEnvironment{figure*}{\nolinenumbers}
24	\AfterEndEnvironment{figure*}{\linenumbers}
25	\AtBeginEnvironment{table}{\nolinenumbers}
26	\AfterEndEnvironment{table}{\linenumbers}
27	\AtBeginEnvironment{table*}{\nolinenumbers}
28	\AfterEndEnvironment{table*}{\linenumbers}
29	
30	\graphicspath{{../figures/paper/}{../artifacts/}}
31	
32	\title{Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue}
33	
34	\author{Anonymous}
35	
36	\makeatletter
37	\def\section{\@startsection {section}{1}{\z@}{-2.0ex plus
38	    -0.1ex minus -.2ex}{1.5ex plus 0.05ex minus .2ex}{\large\bfseries\raggedright}}
39	\def\subsection{\@startsection{subsection}{2}{\z@}{-1.8ex plus
40	    -0.1ex minus -.2ex}{0.8ex plus 0.05ex}{\normalsize\bfseries\raggedright}}
41	\makeatother
42	
43	\begin{document}
44	\setlength{\parskip}{0pt plus 0.15ex}
45	\maketitle
46	
47	\input{sections/abstract}
48	\input{sections/introduction}
49	\input{sections/related_work}
50	\input{sections/method}
51	\input{sections/experiments}
52	\input{sections/analysis}
53	\input{sections/discussion}
54	\input{sections/conclusion}
55	\input{sections/limitations}
56	
57	\FloatBarrier
58	\bibliography{references}
59	
60	\raggedbottom
61	\appendix
62	\renewcommand{\thesection}{\AlphAlph{\value{section}}}
63	\input{sections/appendix}
64	
65	\end{document}
66	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e30f6117-6a22-45a6-acc3-db6a44c0bdf3",
  "isSidechain": true,
  "promptId": "7335ce9b-d729-4c25-828e-fb66579eb012",
  "agentId": "ae011bee35620c3ee",
  "type": "user",
  "uuid": "774ba1b5-00f2-47df-870c-a773c905bc88",
  "sourceToolAssistantUUID": "e30f6117-6a22-45a6-acc3-db6a44c0bdf3",
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

_source line 18 · 2026-05-25T14:27:26.511Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CM8BNjmPAv33wM5xZQs4gu`</summary>

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
  "parentUuid": "774ba1b5-00f2-47df-870c-a773c905bc88",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
  "requestId": "req_011CbPSg5SigiNK6RisZcR2N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87f33501-56a1-49be-9cfc-e142797d1d5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jH4DZc8ktoZq4adc2FcBA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34693,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34693,
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

_source line 19 · 2026-05-25T14:27:26.518Z_

<details><summary>↩ Tool result · `toolu_01CM8BNjmPAv33wM5xZQs4gu`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\looseness=-1 NTP self-recovers because prediction is the same task at both regimes \citep{he2019exposure}; GAR optimizes a \emph{global property}---attention allocation to goal tokens---with no autoregressive counterpart. The collapse is selective: GAR-ours collapses by an order of magnitude while GAR-Dongre shows negligible shift (${\leq}$1.3$\times$). Per-head analysis confirms selectivity: heads with higher TF GAR shift most under AR ($r$\,=\,0.743; Appendix~\ref{sec:appendix-kl}). Any auxiliary attention objective targeting distributional properties rather than prediction itself should face the same barrier under teacher forcing.
4	
5	\looseness=-1 Our exclusion identifies exposure bias as a primary contributing factor, but cannot fully rule out KV cache drift (\S\ref{sec:limitations}). The PCGrad exclusion rules out direction conflict but not magnitude imbalance (7.5--25.7$\times$ NTP dominance; \citealp{chen2018gradnorm}). The GAR--compliance correlation is weak ($r$\,=\,0.200; Appendix~\ref{sec:appendix-ir}), reinforcing GAR's role as a diagnostic probe. Our $\beta$-steering is likewise a \emph{diagnostic}, distinct from inference-time remedies such as split-softmax \citep{li2024measuring} and Rhea \citep{hong2025rhea}. SS and inference-time fixes are complementary: SS modifies representations without inference cost; inference-time methods cannot recover patterns never learned. At $\beta$\,=\,5 the two converge (SS\,=\,0.717 vs.\ TG\,=\,0.727).
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87f33501-56a1-49be-9cfc-e142797d1d5b",
  "isSidechain": true,
  "promptId": "7335ce9b-d729-4c25-828e-fb66579eb012",
  "agentId": "ae011bee35620c3ee",
  "type": "user",
  "uuid": "4971c956-fb8d-4841-a40d-bcaa8f40c942",
  "sourceToolAssistantUUID": "87f33501-56a1-49be-9cfc-e142797d1d5b",
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

_source line 20 · 2026-05-25T14:27:26.683Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Wpx7YX4hWmzhEhCR6NjfD1`</summary>

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
  "parentUuid": "4971c956-fb8d-4841-a40d-bcaa8f40c942",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
  "requestId": "req_011CbPSg5SigiNK6RisZcR2N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4764fb16-3aea-4d8b-b62b-b299ad5cd475",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jH4DZc8ktoZq4adc2FcBA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34693,
      "cache_read_input_tokens": 0,
      "output_tokens": 680,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 34693
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 680,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 34693,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 34693,
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

_source line 21 · 2026-05-25T14:27:26.690Z_

<details><summary>↩ Tool result · `toolu_01Wpx7YX4hWmzhEhCR6NjfD1`</summary>

```text
1	\enlargethispage{\baselineskip}
2	\section{Conclusion}\label{sec:conclusion}
3	
4	\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\,=\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\sim}$1.3$\times$ (Qwen) and ${\sim}$2.9$\times$ (Llama), generalizing across architectures and seeds---the first such transfer to auxiliary attention objectives in multi-turn transformers.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4764fb16-3aea-4d8b-b62b-b299ad5cd475",
  "isSidechain": true,
  "promptId": "7335ce9b-d729-4c25-828e-fb66579eb012",
  "agentId": "ae011bee35620c3ee",
  "type": "user",
  "uuid": "301bb39a-b28d-4ef3-8c23-811fc3b1a4c8",
  "sourceToolAssistantUUID": "4764fb16-3aea-4d8b-b62b-b299ad5cd475",
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

_source line 22 · 2026-05-25T14:27:28.954Z_

Now let me read the appendix file in chunks and count `\includegraphics` across all files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "301bb39a-b28d-4ef3-8c23-811fc3b1a4c8",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
  "requestId": "req_011CbPSgbrKP9Q8sfvrFDiZN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b522bea-e319-46d6-b1a6-ff8e3064add5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdGYsLRuYrYjjxH89MDZN4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11855,
      "cache_read_input_tokens": 34693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11855,
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

_source line 23 · 2026-05-25T14:27:30.879Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G9D5pvpL8YBo5RWGYfapM7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 0,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b522bea-e319-46d6-b1a6-ff8e3064add5",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
  "requestId": "req_011CbPSgbrKP9Q8sfvrFDiZN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76620b15-1422-4aaa-993a-19588ca35895",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdGYsLRuYrYjjxH89MDZN4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11855,
      "cache_read_input_tokens": 34693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11855,
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

_source line 24 · 2026-05-25T14:27:31.190Z_

<details><summary>↩ Tool result · `toolu_01G9D5pvpL8YBo5RWGYfapM7`</summary>

```text
0	\section{Training Configuration}\label{sec:appendix-hyper}
1	
2	Table~\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\times$ learning rate multiplier and are initialized with bias 1.5 ($\sigma(1.5) \approx 0.82$); the gate MLP adds ${\sim}$57K parameters per variant ($<$0.001\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.5 over 3 epochs (29.7--37.1\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB VRAM), requiring 6--8 hours per variant.
3	
4	\begin{table}[t]
5	\centering\small
6	\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\dagger$ apply only to ThreadGate and its ablations.}
7	\label{tab:hyperparams}
8	\begin{tabular}{l@{\hspace{8pt}}l}
9	\toprule
10	\textbf{Parameter} & \textbf{Value} \\
11	\midrule
12	Base model & Qwen-2.5-7B-Instruct \\
13	LoRA rank / $\alpha$ & 16 / 32 \\
14	LoRA targets & \texttt{q\_proj}, \texttt{v\_proj} \\
15	Optimizer & AdamW ($\beta_1$\!=\!0.9, $\beta_2$\!=\!0.999) \\
16	Learning rate & $2 \times 10^{-4}$ \\
17	Gate LR mult.$^\dagger$ & $10\times$ \\
18	Batch / grad accum & 1 / 8 (eff.\ 8) \\
19	Epochs & 3 \\
20	Max seq length & 2048 \\
21	Training data & 8K UltraChat convs \\
22	Seed & 42 (+123 for TG, SS) \\
23	$\lambda_\text{GAR}$/$\lambda_\text{div}$ & 1.0 / 1.0 \\
24	GAR target $\tau$ & 0.5 \\
25	Gate init bias$^\dagger$ & 1.5 ($\sigma\!\approx\!0.82$) \\
26	Gate hidden dim$^\dagger$ & 64 \\
27	Turn embed dim$^\dagger$ & 16 \\
28	GPU & RTX PRO 6000 (96\,GB) \\
29	Training time & 6--8 h / variant \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	
34	\section{Loss Formulation Search}\label{sec:appendix-loss}
35	
36	The final MSE + gate diversity loss (\S\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.
37	
38	\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.
39	
40	\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\text{mean}(\text{GAR})$). The unbounded objective rewards full pass-through ($g \to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\lambda$=2 (v3), gates froze within 100 steps; at $\lambda$=10 (v3b), convergence to identity accelerated; at $\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.
41	
42	\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.
43	
44	\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\tau$ incurs the same penalty as GAR below $\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\mathcal{L}_\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).
45	
46	\begin{table*}[t]
47	\centering\footnotesize
48	\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}
49	\label{tab:loss-iterations}
50	\begin{tabular}{l l l p{5.8cm} c c}
51	\toprule
52	 & \textbf{Loss Family} & \textbf{Status} & \textbf{Failure Mechanism} & \textbf{GAR} & \textbf{PPL} \\
53	\midrule
54	v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\
55	v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & Numerical instability from cumulative product; $\varepsilon$-stabilization insufficient & ---  & ---  \\
56	v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\
57	v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & Higher $\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\
58	v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\
59	v6  & Smooth saturation       & \texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\
60	v7  & MSE + gate div          & \checkmark~\textbf{converged}  & \textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\
61	\bottomrule
62	\end{tabular}
63	\end{table*}
64	
65	\section{Instruction Retention Details}\label{sec:appendix-ir}
66	
67	To evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\beta$\,=\,3 steering on $N$\,=\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.
68	
69	\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\,=\,54 paired evaluations (18 types $\times$ 3 conversations per type) for the McNemar analysis.
70	
71	\paragraph{Per-category results.} Table~\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.
72	
73	\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\,=\,0.200, $p$\,=\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\,=\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.
74	
75	Figure~\ref{fig:ir-bar} visualizes the per-category breakdown.
76	
77	\begin{figure}[t]
78	  \centering
79	  \includegraphics[width=\columnwidth]{fig_instruction_retention.pdf}
80	  \caption{Instruction retention by constraint category under $\beta$\,=\,3 steering. Content constraints benefit most (+23.8\,pp); format and count constraints are unaffected.}
81	  \label{fig:ir-bar}
82	\end{figure}
83	
84	\FloatBarrier
85	
86	\begin{table}[t]
87	\centering\small
88	\caption{Instruction retention by constraint category ($\beta$\,=\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}
89	\label{tab:ir-results}
90	\begin{tabular}{lccc}
91	\toprule
92	\textbf{Category} & $\beta$\,=\,0 & $\beta$\,=\,3 & $\Delta$ \\
93	\midrule
94	Content    & 61.9\% & 85.7\% & +23.8\,pp \\
95	Position   & 66.7\% & 73.3\% & +6.7\,pp \\
96	Count      & 100\%  & 100\%  & 0 \\
97	Format     & 100\%  & 100\%  & 0 \\
98	\midrule
99	\textbf{Overall} & 75.9\% & 87.0\% & +11.1\,pp \\
100	\bottomrule
101	\end{tabular}
102	\end{table}
103	
104	\section{Long-Conversation AR Evaluation}\label{sec:appendix-n5}
105	
106	The main results (Table~\ref{tab:four-way}) report AR GAR from $N$\,=\,50 held-out conversations with a mean of 3.6 user turns. Table~\ref{tab:n5-ar} presents complementary results on $N$\,=\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.
107	
108	\paragraph{Gating advantage vanishes at length.} In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. ThreadGate's advantage over LoRA-only shrinks from 1.7$\times$ (0.064 vs.\ 0.037 in the $N$\,=\,50 evaluation) to 0.64$\times$ (0.016 vs.\ 0.025), actually reversing the ordering. This reversal is not statistically robust given the small sample ($N$\,=\,5) but directionally suggests that architectural modifications provide diminishing returns as conversation length increases and exposure bias accumulates.
109	
110	\paragraph{Convergence to base.} By turn~10, all fine-tuned variants converge to within 2$\times$ of the base model's GAR, compared to 3.4$\times$ at turn~1 in the shorter evaluation. This convergence is consistent with exposure bias compounding multiplicatively over turns: each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn~10 the accumulated drift overwhelms any gating or LoRA signal, leaving only the base model's intrinsic attention patterns.
111	
112	\paragraph{Caveats.} The $N$\,=\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.
113	
114	\begin{table}[t]
115	\centering\small
116	\caption{AR GAR-ours on $N$\,=\,5 ten-turn conversations. The gating advantage observed in Table~\ref{tab:four-way} ($N$\,=\,50, mean 3.6 turns) diminishes with conversation length.}
117	\label{tab:n5-ar}
118	\begin{tabular}{lcc}
119	\toprule
120	\textbf{Configuration} & \textbf{AR GAR-O} & \textbf{$\Delta$ vs.\ Table~\ref{tab:four-way}} \\
121	\midrule
122	Base & 0.012 & $-$0.007 \\
123	\midrule
124	ThreadGate & 0.016 & $-$0.048 \\
125	\;+\,PCGrad & 0.015 & $-$0.015 \\
126	Uniform Gate & 0.015 & $-$0.018 \\
127	LoRA-only & 0.025 & $-$0.012 \\
128	\bottomrule
129	\end{tabular}
130	\end{table}
131	
132	\section{Statistical Test Details}\label{sec:appendix-stats}
133	
134	All statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\ref{tab:stat-tests} consolidates the full results.
135	
136	\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\ LoRA-only comparison ($p$\,=\,0.004, $r$\,=\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\ +PCGrad comparison ($p$\,=\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.
137	
138	\paragraph{Bootstrap confidence intervals.} The 95\% CIs in Table~\ref{tab:four-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.
139	
140	\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \leq r < 0.5$ is medium, and $r \geq 0.5$ is large. The TG vs.\ LoRA-only effect ($r$\,=\,0.454) is medium, and TG vs.\ Base ($r$\,=\,0.802) is large.
141	
142	\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \leq 0.004$) survive this correction.
143	
144	\begin{table}[t]
145	\centering\small
146	\caption{Consolidated statistical tests. All AR comparisons use $N$\,=\,50 conversations (39 with $\geq$3 turns); gate conditioning uses 28 layers.}
147	\label{tab:stat-tests}
148	\begin{tabular}{llcc}
149	\toprule
150	\textbf{Comparison} & \textbf{Test} & $p$ & $r$ \\
151	\midrule
152	\multicolumn{4}{l}{\emph{AR GAR-ours ($\beta$\,=\,0)}} \\
153	TG vs.\ Base & Wilcoxon & $<$0.001 & 0.802 \\
154	TG vs.\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\
155	TG vs.\ +PCGrad & Wilcoxon & 0.002 & --- \\
156	SS vs.\ TG & Wilcoxon & $<$0.001 & 0.869 \\
157	\midrule
158	\multicolumn{4}{l}{\emph{Gate conditioning (28 layers)}} \\
159	Turn 1 vs.\ Turn 21 & Wilcoxon & $3.7\!\times\!10^{-8}$ & 0.975 \\
160	\midrule
161	\multicolumn{4}{l}{\emph{Instruction retention}} \\
162	$\beta$\,=\,0 vs.\ $\beta$\,=\,3 & McNemar & 0.077 & --- \\
163	GAR--compliance & Pearson & 0.007 & 0.200 \\
164	\bottomrule
165	\end{tabular}
166	\end{table}
167	
168	\section{Llama-3.1-8B Complete Results}\label{sec:appendix-llama}
169	
170	Table~\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \S\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.
171	
172	\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\ 0.50).
173	
174	\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\,=\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\% for ThreadGate (mean 0.043, std 0.100), and 5\% of turn-level measurements exhibit sporadic attention spikes (GAR $\geq$ 0.4). We therefore report both mean and median.
175	
176	\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719, L24\,=\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\times$ by median for Llama vs.\ 8--17$\times$ for Qwen).
177	
178	\begin{table}[t]
179	\centering\small
180	\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\,=\,50); AR: autoregressive ($N$\,=\,20 for Base/TG/LoRA-only, $N$\,=\,50 for SS). Median is more representative due to heavy-tailed AR distributions (SS uses mean only).}
181	\label{tab:llama-full}
182	\resizebox{\columnwidth}{!}{%
183	\begin{tabular}{lcccc}
184	\toprule
185	& \multicolumn{2}{c}{\textbf{TF}} & \multicolumn{2}{c}{\textbf{AR}} \\
186	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
187	& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\
188	\midrule
189	Base & 0.017 & 3.45 & 0.009 & 0.009 \\
190	ThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\
191	LoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\
192	\textbf{SS} & 0.477 & 2.82 & \textbf{0.166} & --- \\
193	\bottomrule
194	\end{tabular}}
195	\end{table}
196	
197	\FloatBarrier
198	
199	\begin{figure}[t]
200	  \centering
201	  \includegraphics[width=\columnwidth]{fig_crossmodel.pdf}
202	  \caption{Cross-architecture validation. (a)~The TF-AR gap persists on Llama-3.1-8B (27$\times$ by median), exceeding Qwen's 8$\times$. (b)~Gate profiles on normalized depth: Qwen dips at early layers, Llama at late layers; architecture-dependent patterns, but both converge toward identity.}
203	  \label{fig:crossmodel}
204	\end{figure}
205	
206	\paragraph{Cross-model summary.} Table~\ref{tab:crossmodel-detail} consolidates the cross-model comparison, showing TF GAR, AR GAR, PPL, and gap ratios side by side for both architectures. The consistent pattern---TF GAR $\approx$ 0.5, AR GAR $\ll$ 0.1, gap $\geq$ 7.9$\times$---across two architectures with different layer counts, attention head configurations, and pre-training corpora provides strong evidence that exposure bias is architecture-independent. Notably, Llama's larger gaps (27$\times$ by median for TG; mean-based range 11.2--17.2$\times$) compared to Qwen's (7.9--13.5$\times$) may reflect its deeper architecture (32 vs.\ 28 layers), which allows more layers for distributional drift to compound through.
207	
208	\input{../artifacts/appendix_expansion/tab_crossmodel_detail.tex}
209	
210	\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\times$), compared to 1.28$\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.
211	
212	\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\% longer than Qwen due to Llama's larger layer count (32 vs.\ 28 layers).
213	
214	\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\% decline. This is steeper than Qwen's 70.8\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\ 28 KV heads).
215	
216	\paragraph{Cross-model gradient analysis.} Table~\ref{tab:gradient-crossmodel} compares NTP--GAR gradient interaction between the two architectures. Both models exhibit near-orthogonal gradients (cosine similarity $\approx$\,0), not systematic conflict: Qwen shows a slight negative mean ($-$0.042) while Llama is marginally positive (+0.005). NTP gradients dominate GAR by 14.7$\times$ on Qwen and 25.7$\times$ on Llama, indicating that the auxiliary signal is overwhelmed by magnitude rather than opposed by direction. The cross-model consistency---near-zero cosine similarity and order-of-magnitude NTP dominance on both architectures---reinforces the \emph{modus tollens} argument (\S\ref{subsec:pcgrad}): gradient direction conflict is not the primary cause of the TF-AR gap.
217	
218	\begin{table}[t]
219	\centering\small
220	\caption{Cross-model NTP--GAR gradient interaction. Gradients are near-orthogonal on both architectures; NTP magnitude dominates GAR by 15--26$\times$.}
221	\label{tab:gradient-crossmodel}
222	\begin{tabular}{lcc}
223	\toprule
224	\textbf{Metric} & \textbf{Qwen-7B} & \textbf{Llama-8B} \\
225	\midrule
226	Mean cos sim & $-$0.042 & +0.005 \\
227	Neg-layer \% & 67.9\% & 53.1\% \\
228	NTP/GAR mag ratio & 14.7$\times$ & 25.7$\times$ \\
229	\bottomrule
230	\end{tabular}
231	\end{table}
232	
233	\section{Additional Visualizations}\label{sec:appendix-viz}
234	
235	This section presents extended visualizations referenced in the main text. Each figure examines a different aspect of the gating behavior and its failure under autoregressive generation.
236	
237	\subsection{Gate Profile Heatmap}
238	
239	Figure~\ref{fig:gate-heatmap} shows the per-layer gate values across all training configurations for both Qwen-2.5-7B (28 layers) and Llama-3.1-8B (32 layers). The key observation is that early layers consistently receive the lowest gate values across all conditions, suggesting that these layers contribute more dispensable computations for the NTP objective. The pattern is remarkably consistent across ThreadGate, Uniform Gate, and PCGrad variants, indicating that gate-value allocation is driven primarily by the NTP loss landscape rather than the GAR auxiliary objective.
240	
241	\begin{figure}[H]
242	\centering
243	\includegraphics[width=\columnwidth]{fig_gate_profile_heatmap.pdf}
244	\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\times$ 5 conditions) and Llama-3.1-8B (32 layers $\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}
245	\label{fig:gate-heatmap}
246	\end{figure}
247	
248	\subsection{Cross-Model Gate Profile Comparison}
249	
250	Figure~\ref{fig:gate-crossmodel} compares gate profiles between the two architectures. Qwen-2.5-7B shows minimum gate values at early layers (L1\,=\,0.793, L5\,=\,0.797), suggesting these layers are most amenable to attenuation without disrupting NTP. Llama-3.1-8B instead shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719), indicating that architecturally distinct models learn different layer-importance hierarchies. Both profiles converge toward identity at their respective final layers, consistent with NTP gradient pressure dominating gate optimization at output-adjacent layers.
251	
252	\begin{figure}[H]
253	\centering
254	\includegraphics[width=\columnwidth]{fig_gate_profile_crossmodel.pdf}
255	\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}
256	\label{fig:gate-crossmodel}
257	\end{figure}
258	
259	\subsection{Per-Turn AR GAR Decay}
260	
261	Figure~\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\% from turn 1 to turn 10; Llama base drops 90\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\ref{tab:four-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.
262	
263	\begin{figure}[H]
264	\centering
265	\includegraphics[width=\columnwidth]{fig_ar_gar_perturn.pdf}
266	\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\% (turn 1$\to$10), Llama base drops 90\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}
267	\label{fig:ar-gar-perturn}
268	\end{figure}
269	
270	\subsection{Bootstrap Confidence Intervals}
271	
272	Figure~\ref{fig:bootstrap-ci} shows the bootstrap resampling distributions underlying the 95\% CIs reported in Table~\ref{tab:four-way}.
273	
274	\begin{figure}[H]
275	  \centering
276	  \includegraphics[width=\columnwidth]{fig_bootstrap_ci.pdf}
277	  \caption{Bootstrap CI distributions for AR GAR-ours (ThreadGate vs.\ LoRA-only, $N$\,=\,50, 10K resamples). Distributions overlap substantially, consistent with the modest effect size ($r$\,=\,0.454).}
278	  \label{fig:bootstrap-ci}
279	\end{figure}
280	
281	\subsection{Gate Value Distributions}
282	
283	Figure~\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.
284	
285	\begin{figure}[H]
286	\centering
287	\includegraphics[width=\columnwidth]{fig_gate_distribution.pdf}
288	\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}
289	\label{fig:gate-distribution}
290	\end{figure}
291	
292	\subsection{Training Loss Curves}
293	
294	Figure~\ref{fig:training-loss} shows the NTP, GAR, and total loss trajectories during training. GAR loss collapses to near-zero within the first epoch across all variants, indicating rapid convergence of the auxiliary objective under teacher forcing. NTP loss converges normally to ${\sim}$0.93 by epoch 3. The fast GAR convergence is not itself pathological---it indicates successful optimization under the training distribution. The pathology emerges only at the transition to autoregressive generation, where the learned attention patterns fail to transfer.
295	
296	\begin{figure}[H]
297	\centering
298	\includegraphics[width=\columnwidth]{fig_training_loss_curves.pdf}
299	\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}
300	\label{fig:training-loss}
301	\end{figure}
302	
303	\subsection{Full Attention Steering Results}\label{sec:appendix-steering}
304	
305	\begin{table*}[t]
306	\centering\small
307	\caption{Full attention steering results across evaluation settings.
308	\textbf{Bold} indicates the operating point cited in the main text ($\beta$\,=\,5).
309	A visual gap separates the phase-transition boundary: GAR jumps sharply between $\beta$\,=\,2 and $\beta$\,=\,3 across all settings.}
310	\label{tab:steering-full}
311	\begin{tabular}{r cc cc cc}
312	\toprule
313	 & \multicolumn{2}{c}{\textbf{$N$\,=\,5, Gen}} & \multicolumn{2}{c}{\textbf{$N$\,=\,50, Gen}} & \multicolumn{2}{c}{\textbf{$N$\,=\,200, TF}} \\
314	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
315	$\beta$ & GAR & PPL & GAR & PPL & GAR & PPL \\
316	\midrule
317	0   & .028 & 1.41 & $.064 \pm .081$ & $1.43 \pm .10$ & .535 & 2.62 \\
318	0.5 & .029 & 1.39 & ---             & ---             & ---  & ---  \\
319	1   & .035 & 1.36 & ---             & ---             & ---  & ---  \\
320	2   & .062 & 1.41 & $.128 \pm .110$ & $1.48 \pm .14$ & .611 & 2.69 \\
321	\addlinespace[3pt]
322	3   & ---  & ---  & $.556 \pm .060$ & $1.56 \pm .17$ & .788 & 2.93 \\
323	4   & ---  & ---  & $.644 \pm .061$ & $1.67 \pm .22$ & .817 & 3.49 \\
324	\textbf{5}  & \textbf{.680} & \textbf{1.91} & $\mathbf{.727 \pm .061}$ & $\mathbf{1.77 \pm .27}$ & \textbf{.833} & \textbf{6.15} \\
325	10  & .959 & 4.22 & $.961 \pm .015$ & $3.45 \pm 1.78$ & .977 & 505.2 \\
326	\bottomrule
327	\end{tabular}
328	\end{table*}
329	
330	\begin{figure}[t]
331	  \centering
332	  \includegraphics[width=\columnwidth]{fig_steering_standalone.pdf}
333	  \caption{Detailed $\beta$-steering trade-off ($N$\,=\,50). GAR-ours (top) increases monotonically with $\beta$; PPL (bottom) remains stable below $\beta$\,=\,3 (9\% cost), then rises sharply. The $\beta$\,=\,3 operating point (circled) achieves 8.7$\times$ GAR recovery while crossing the TF baseline, representing the optimal trade-off.}
334	  \label{fig:steering-standalone}
335	\end{figure}
336	
337	\section{Per-Layer Gate Profile}\label{sec:appendix-gate-profile}
338	
339	Table~\ref{tab:gate-profile} reports the final per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct (28 layers). Gate values are averaged across all tokens in the evaluation set. Layers 1 and 5 show the lowest gate values (0.793 and 0.797), indicating these layers are most amenable to attenuation without disrupting NTP. Layers 26--27 converge to $\geq$0.988, consistent with NTP gradient pressure dominating at output-adjacent layers. The mean across all layers is 0.947 ($\sigma$\,=\,0.051).
340	
341	\begin{table}[t]
342	\centering\small
343	\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}
344	\label{tab:gate-profile}
345	\resizebox{\columnwidth}{!}{%
346	\begin{tabular}{cccccccc}
347	\toprule
348	L0 & L1 & L2 & L3 & L4 & L5 & L6 & L7 \\
349	.883 & \textbf{.793} & .996 & .988 & .984 & \textbf{.797} & .961 & .918 \\
350	\midrule
351	L8 & L9 & L10 & L11 & L12 & L13 & L14 & L15 \\
352	.965 & .934 & .969 & .918 & .926 & .941 & .930 & .965 \\
353	\midrule
354	L16 & L17 & L18 & L19 & L20 & L21 & L22 & L23 \\
355	.941 & .910 & .961 & .965 & .973 & .988 & .969 & .980 \\
356	\midrule
357	L24 & L25 & L26 & L27 & \multicolumn{4}{c}{Summary} \\
358	.980 & .984 & .988 & 1.00 & \multicolumn{4}{c}{$\bar{g}$\,=\,.947, $\sigma$\,=\,.051} \\
359	\bottomrule
360	\end{tabular}}
361	\end{table}
362	
363	The gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.
364	
365	\paragraph{Cross-model comparison.} See \S\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.
366	
367	\section{Scheduled Sampling Implementation}\label{sec:appendix-ss}
368	
369	Our scheduled sampling implementation follows \citet{bengio2015scheduled} with modifications for multi-turn transformer training:
370	
371	\paragraph{Sampling schedule.} The model-generated context ratio $\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\%) is lower than the nominal schedule due to per-sample Bernoulli variance.
372	
373	\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.
374	
375	\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing (Figure~\ref{fig:ss-dynamics}). Gate profiles remain similar (mean 0.953 vs.\ 0.947, min at L4 vs.\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases by 8--80\% across seeds (seed-dependent; dominated by GAR forward pass overhead): 6.5h (seed 42), 10.8h (seed 123), and 6.5h (seed 456) vs.\ 6.0h for standard ThreadGate on Qwen. Seed 456 exhibits consistent training dynamics with seeds 42 and 123.
376	
377	\begin{figure}[t]
378	  \centering
379	  \includegraphics[width=\columnwidth]{fig_ss_training_dynamics.pdf}
380	  \caption{Scheduled sampling training dynamics: sampling ratio $\rho$ ramps linearly from 0 to 0.3 (left axis); GAR loss (right axis) shows higher early-epoch variance due to stochastic context mixing.}
381	  \label{fig:ss-dynamics}
382	\end{figure}
383	
384	\section{Computational Cost Analysis}\label{sec:appendix-cost}
385	
386	\begin{table}[t]
387	\centering\small
388	\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\,GB VRAM).}
389	\label{tab:cost}
390	\resizebox{\columnwidth}{!}{%
391	\begin{tabular}{lcccc}
392	\toprule
393	\textbf{Config} & \textbf{Params} & \textbf{Time (h)} & \textbf{VRAM} & \textbf{Overhead} \\
394	\midrule
395	\multicolumn{5}{l}{\emph{Qwen-2.5-7B-Instruct}} \\
396	LoRA-only & 4.2M & 6.0 & 42\,GB & baseline \\
397	ThreadGate & 4.3M & 6.0 & 43\,GB & $+$57K \\
398	\;+\,PCGrad & 4.3M & 8.0 & 43\,GB & $+$33\% \\
399	Uniform Gate & 4.3M & 6.0 & 43\,GB & $+$57K \\
400	SS (s42) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
401	SS (s123) & 4.3M & 10.8 & 43\,GB & $+$80\% \\
402	SS (s456) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
403	\midrule
404	\multicolumn{5}{l}{\emph{Llama-3.1-8B-Instruct}} \\
405	LoRA-only & 4.2M & 7.0 & 45\,GB & baseline \\
406	ThreadGate & 4.3M & 7.3 & 46\,GB & $+$65K \\
407	\bottomrule
408	\end{tabular}}
409	\end{table}
410	
411	\paragraph{Parameter overhead.} ThreadGate adds ${\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\times$ 2K per gate MLP) and ${\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.
412	
413	\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 6.0--7.3 hours. PCGrad adds ${\sim}$33\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\% (6.5h) due to efficient batched generation, while seed 123 adds 80\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.
414	
415	\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\to$64$\to$1 MLP forward pass per layer adds $<$0.1\% latency. $\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.
416	
417	\section{Qualitative Steering Examples}\label{sec:appendix-examples}
418	
419	Table~\ref{tab:examples} illustrates the effect of $\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''
420	
421	\begin{table*}[t]
422	\centering\small
423	\caption{Qualitative effect of $\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}
424	\label{tab:examples}
425	\begin{tabular}{c p{5.5cm} p{5.5cm}}
426	\toprule
427	\textbf{Turn} & \textbf{$\beta$\,=\,0 (unsteered)} & \textbf{$\beta$\,=\,3 (steered)} \\
428	\midrule
429	1 & \checkmark~Three bullet points, on-topic & \checkmark~Three bullet points, on-topic \\
430	2 & \checkmark~Three bullet points, relevant & \checkmark~Three bullet points, relevant \\
431	3 & $\sim$~Four bullet points, partially on-topic & \checkmark~Three bullet points, on-topic \\
432	4 & \texttimes~Free-form paragraph, no bullets & \checkmark~Three bullet points, on-topic \\
433	\bottomrule
434	\end{tabular}
435	\end{table*}
436	
437	The pattern is consistent with the GAR decay analysis (\S\ref{sec:analysis}): unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. The per-category breakdown in Table~\ref{tab:ir-results} shows that content constraints benefit most from this effect.
438	
439	\section{Gradient Conflict Analysis}\label{sec:appendix-gradient}
440	
441	\begin{figure}[t]
442	  \centering
443	  \includegraphics[width=\columnwidth,height=0.42\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}
444	  \caption{(a)~Training GAR convergence to target ($\tau$\,=\,0.5). (b)~PCGrad removes gradient conflict but $\mathcal{L}_\text{GAR}$ still collapses, confirming that gradient direction conflict is not the primary cause (\S\ref{subsec:pcgrad}).}
445	  \label{fig:training-pcgrad}
446	\end{figure}
447	
448	This section provides extended gradient interaction analysis supporting the PCGrad exclusion argument in \S\ref{subsec:pcgrad}. We measure per-layer cosine similarity between NTP and GAR gradients, gradient magnitude ratios, and the effect of PCGrad projection on these quantities.
449	
450	\paragraph{Gradient direction analysis.} Figure~\ref{fig:gradient-heatmap} visualizes the per-layer cosine similarity between NTP and GAR gradients across training epochs for both standard ThreadGate and PCGrad training. Under standard training, 79\% of layers show negative cosine similarity (gradient conflict) at epoch~0, declining to 68\% by epoch~2 as GAR loss converges to near-zero. This decline reflects diminishing GAR gradient magnitude rather than alignment improvement---as GAR loss approaches zero, the GAR gradient shrinks proportionally, making cosine similarity measurements less reliable (small gradients produce noisy direction estimates). Under PCGrad training, the conflict percentage decreases more slowly (79\%$\to$71\%), consistent with PCGrad projecting conflicting gradients onto the other's normal plane but not eliminating the underlying gradient conflict.
451	
452	\paragraph{Spatial patterns.} The early layers (L0--L5) and output-adjacent layers (L24--L27) show the strongest conflict, corresponding to the layers where gate values deviate most from identity (Figure~\ref{fig:gate-heatmap}). This spatial correlation is not causal: removing gradient conflict via PCGrad does not improve AR GAR, and gates at high-conflict layers are not systematically different from gates at low-conflict layers (Spearman $\rho$\,=\,$-$0.12, $p$\,=\,0.54 between gate value and conflict magnitude).
453	
454	\paragraph{Magnitude dominance.} NTP gradient magnitude dominates GAR by 7.5$\times$ at epoch~0 and 14.7$\times$ by epoch~2, as GAR loss converges while NTP loss remains at $\sim$0.93. This growing dominance means that even when directions oppose, the effective update direction is determined almost entirely by NTP. PCGrad addresses gradient conflict but not magnitude dominance---it projects conflicting gradients onto the other's normal plane (changing direction) but preserves relative magnitudes. The 7.5--14.7$\times$ magnitude ratio means that even after PCGrad projection, GAR contributes $<$7\% of the effective update magnitude, explaining why PCGrad is ineffective.
455	
456	\paragraph{Cross-model consistency.} Table~\ref{tab:gradient-crossmodel} confirms the pattern on Llama-3.1-8B: gradients are near-orthogonal (mean cosine $+$0.005, essentially zero) rather than systematically conflicting, with 25.7$\times$ NTP dominance. The Llama result is particularly informative because it shows that even without systematic gradient conflict (53\% negative layers, near chance), the same TF-AR gap persists. This cross-model evidence strengthens the \textit{modus tollens} argument: if gradient conflict were the cause, it should be present on both architectures; it is absent on Llama, yet the gap persists; therefore gradient direction conflict is not the primary cause.
457	
458	\begin{figure*}[t]
459	\centering
460	\includegraphics[width=0.95\textwidth]{fig_gradient_conflict_heatmap.pdf}
461	\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\% to 68\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\%$\to$71\%) but does not improve AR GAR, ruling out gradient direction conflict as the primary cause (\S\ref{subsec:pcgrad}).}
462	\label{fig:gradient-heatmap}
463	\end{figure*}
464	
465	\section{Training Data Characteristics}\label{sec:appendix-data}
466	
467	All experiments use 8,000 multi-turn conversations sampled from the UltraChat \citep{ding2023ultrachat} training split. Table~\ref{tab:data-stats} summarizes the dataset characteristics. Conversations are truncated to 2,048 tokens; conversations shorter than 3 user turns are excluded to ensure sufficient multi-turn structure for GAR computation. The held-out evaluation sets use separate non-overlapping samples: $N$\,=\,50 conversations (mean 3.6 user turns) for the primary AR evaluation and $N$\,=\,5 conversations (10 turns each) for the long-conversation analysis (Appendix~\ref{sec:appendix-n5}).
468	
469	\begin{table}[t]
470	\centering\small
471	\caption{Training and evaluation data characteristics. All data from UltraChat \citep{ding2023ultrachat}.}
472	\label{tab:data-stats}
473	\begin{tabular}{lcc}
474	\toprule
475	\textbf{Property} & \textbf{Train} & \textbf{Eval (primary)} \\
476	\midrule
477	Conversations & 8,000 & 50 \\
478	Min user turns & 3 & 3 \\
479	Max sequence length & 2,048 & 2,048 \\
480	Source & UltraChat train & UltraChat train \\
481	Overlap & --- & non-overlapping \\
482	\bottomrule
483	\end{tabular}
484	\end{table}
485	
486	\section{Exposure Bias Scaling}\label{sec:appendix-eb-scaling}
487	
488	Figure~\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).
489	
490	\paragraph{Cross-variant gaps.} On Qwen, ThreadGate achieves the smallest gap among standard variants (7.8$\times$) while PCGrad shows the largest (16.7$\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\sim}$1.3$\times$, the only variant approaching parity. The ordering of gap ratios (SS $\ll$ TG $<$ LoRA $<$ UG $<$ PCGrad) differs from the ordering of TF GAR (all $\approx$ 0.50), confirming that training-time optimization success does not predict inference-time robustness. On Llama, both ThreadGate and LoRA-only show $\sim$27$\times$ gaps (by median), larger than any Qwen variant. The consistently larger Llama gaps may reflect its deeper architecture (32 vs.\ 28 layers), which provides more layers for distributional drift to compound through.
491	
492	\paragraph{Length-dependent compounding.} Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\,=\,50), ThreadGate's gap is 8$\times$; at 10 turns ($N$\,=\,5), it widens to 31$\times$. The relationship is approximately linear in the number of turns on a log scale, suggesting that the per-turn drift contribution is roughly multiplicative. Extrapolating this trend suggests that at 20 turns the gap would exceed 100$\times$, making any training-time attention signal essentially undetectable. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.
493	
494	\paragraph{Implications for deployment.} These scaling results have practical implications: (1)~for applications requiring sustained attention over many turns (e.g., long-form tutoring, multi-step reasoning), architectural modifications alone are insufficient---distributional robustification or inference-time intervention is necessary; (2)~the near-parity of scheduled sampling (${\sim}$1.3$\times$ gap) suggests that bridging the training-inference distribution gap is both necessary and sufficient for maintaining attention; (3)~the $\beta$-steering approach provides a complementary inference-time solution, but its effectiveness also depends on conversation length (Appendix~\ref{sec:appendix-steering-viz}).
495	
496	\begin{figure}[t]
497	\centering
498	\includegraphics[width=\columnwidth]{fig_eb_scaling.pdf}
499	\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\sim}$1.3$\times$) is the only variant near parity. Llama gaps ($\sim$27$\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\times$ (3.6 turns) to 31$\times$ (10 turns).}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76620b15-1422-4aaa-993a-19588ca35895",
  "isSidechain": true,
  "promptId": "7335ce9b-d729-4c25-828e-fb66579eb012",
  "agentId": "ae011bee35620c3ee",
  "type": "user",
  "uuid": "7df58c59-55ac-444a-a79c-93f58fb42e1f",
  "sourceToolAssistantUUID": "76620b15-1422-4aaa-993a-19588ca35895",
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

_source line 25 · 2026-05-25T14:27:31.793Z_

<details open><summary>🔧 Tool call — Grep · `toolu_016WmSLrnAom6Z77uUuwm6Fj`</summary>

```json
{
  "pattern": "\\\\includegraphics",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7df58c59-55ac-444a-a79c-93f58fb42e1f",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
  "requestId": "req_011CbPSgbrKP9Q8sfvrFDiZN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b86dea34-4c4a-45c2-9fea-be890c548c49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdGYsLRuYrYjjxH89MDZN4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11855,
      "cache_read_input_tokens": 34693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11855,
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

_source line 26 · 2026-05-25T14:27:31.815Z_

<details><summary>↩ Tool result · `toolu_016WmSLrnAom6Z77uUuwm6Fj`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:25:  \includegraphics[width=\columnwidth]{fig_ss_multiseed.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:38:  \includegraphics[width=\columnwidth]{fig3_gate_shift.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex:18:  \includegraphics[width=\columnwidth]{fig5_attention_steering.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex:33:  \includegraphics[width=\columnwidth]{fig_ss_gap_compression.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex:23:  \includegraphics[width=\columnwidth]{fig4_attention_heatmap.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:80:  \includegraphics[width=\columnwidth]{fig_instruction_retention.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:202:  \includegraphics[width=\columnwidth]{fig_crossmodel.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:244:\includegraphics[width=\columnwidth]{fig_gate_profile_heatmap.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:255:\includegraphics[width=\columnwidth]{fig_gate_profile_crossmodel.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:266:\includegraphics[width=\columnwidth]{fig_ar_gar_perturn.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:277:  \includegraphics[width=\columnwidth]{fig_bootstrap_ci.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:288:\includegraphics[width=\columnwidth]{fig_gate_distribution.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:299:\includegraphics[width=\columnwidth]{fig_training_loss_curves.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:333:  \includegraphics[width=\columnwidth]{fig_steering_standalone.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:380:  \includegraphics[width=\columnwidth]{fig_ss_training_dynamics.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:444:  \includegraphics[width=\columnwidth,height=0.42\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:461:\includegraphics[width=0.95\textwidth]{fig_gradient_conflict_heatmap.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:499:\includegraphics[width=\columnwidth]{fig_eb_scaling.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:512:\includegraphics[width=\columnwidth]{fig_kl_ar_gar_curves.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:519:\includegraphics[width=\columnwidth]{fig_kl_ar_gar_bar.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:659:  \includegraphics[width=\columnwidth]{fig_perturn_qwen_detail.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:668:  \includegraphics[width=\columnwidth]{fig_perturn_llama_detail.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:697:  \includegraphics[width=\columnwidth]{fig_gar_robustness_grouped.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:716:  \includegraphics[width=\columnwidth]{fig_mmlu_comparison.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:763:  \includegraphics[width=0.75\textwidth]{fig_training_curves_6panel.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:784:  \includegraphics[width=\columnwidth]{fig_steering_perturn_4panel.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex:11:  \includegraphics[width=\textwidth]{fig1_headline.pdf}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b86dea34-4c4a-45c2-9fea-be890c548c49",
  "isSidechain": true,
  "promptId": "7335ce9b-d729-4c25-828e-fb66579eb012",
  "agentId": "ae011bee35620c3ee",
  "type": "user",
  "uuid": "341aa626-f816-48a2-a4d5-dcc1e8405a79",
  "sourceToolAssistantUUID": "b86dea34-4c4a-45c2-9fea-be890c548c49",
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

_source line 27 · 2026-05-25T14:27:32.512Z_

<details open><summary>🔧 Tool call — Grep · `toolu_011jsXt1YsQqmrpDHMyU9m8M`</summary>

```json
{
  "pattern": "\\\\label\\{fig:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "341aa626-f816-48a2-a4d5-dcc1e8405a79",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
  "requestId": "req_011CbPSgbrKP9Q8sfvrFDiZN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23c7f9ed-0bfa-44ca-bed8-2b5c8a11dc12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdGYsLRuYrYjjxH89MDZN4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11855,
      "cache_read_input_tokens": 34693,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11855
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 362,
          "cache_read_input_tokens": 34693,
          "cache_creation_input_tokens": 11855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11855,
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

_source line 28 · 2026-05-25T14:27:32.531Z_

<details><summary>↩ Tool result · `toolu_011jsXt1YsQqmrpDHMyU9m8M`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:27:  \label{fig:ss-multiseed}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:40:  \label{fig:gate-shift}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex:20:  \label{fig:steering-recovery}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex:35:  \label{fig:ss-gap}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex:25:  \label{fig:attention-heatmap}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:82:  \label{fig:ir-bar}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:204:  \label{fig:crossmodel}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:246:\label{fig:gate-heatmap}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:257:\label{fig:gate-crossmodel}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:268:\label{fig:ar-gar-perturn}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:279:  \label{fig:bootstrap-ci}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:290:\label{fig:gate-distribution}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:301:\label{fig:training-loss}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:335:  \label{fig:steering-standalone}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:382:  \label{fig:ss-dynamics}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:446:  \label{fig:training-pcgrad}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:463:\label{fig:gradient-heatmap}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:501:\label{fig:eb-scaling}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:514:\label{fig:kl_ar_gar_curves}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:521:\label{fig:kl_ar_gar_bar}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:661:  \label{fig:perturn-qwen-detail}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:670:  \label{fig:perturn-llama-detail}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:699:  \label{fig:gar-robust-grouped}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:718:  \label{fig:mmlu-comparison}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:765:  \label{fig:training-6panel}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:786:  \label{fig:steering-4panel}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex:13:  \label{fig:headline}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23c7f9ed-0bfa-44ca-bed8-2b5c8a11dc12",
  "isSidechain": true,
  "promptId": "7335ce9b-d729-4c25-828e-fb66579eb012",
  "agentId": "ae011bee35620c3ee",
  "type": "user",
  "uuid": "d5c3b85c-aa85-4f60-864d-2e3193466a54",
  "sourceToolAssistantUUID": "23c7f9ed-0bfa-44ca-bed8-2b5c8a11dc12",
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

_source line 29 · 2026-05-25T14:27:34.976Z_

Now let me also check the appendix section labels and verify the referenced appendix sections exist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5c3b85c-aa85-4f60-864d-2e3193466a54",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
  "requestId": "req_011CbPSh2hYTzTDfGSEZPvHh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "725a1ae3-ae90-4471-8ea1-1fa7675b36a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0135DssFkSJRz2vZUgGUSR7Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18800,
      "cache_read_input_tokens": 46548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18800,
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

_source line 30 · 2026-05-25T14:27:36.004Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01QR61zFZSiqsdTxhQfWqTYs`</summary>

```json
{
  "pattern": "\\\\label\\{sec:appendix",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "725a1ae3-ae90-4471-8ea1-1fa7675b36a1",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
  "requestId": "req_011CbPSh2hYTzTDfGSEZPvHh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "379b3c29-b0e2-44ec-8cd7-18b777573370",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0135DssFkSJRz2vZUgGUSR7Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18800,
      "cache_read_input_tokens": 46548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18800,
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

_source line 31 · 2026-05-25T14:27:36.028Z_

<details><summary>↩ Tool result · `toolu_01QR61zFZSiqsdTxhQfWqTYs`</summary>

```text
1:\section{Training Configuration}\label{sec:appendix-hyper}
35:\section{Loss Formulation Search}\label{sec:appendix-loss}
66:\section{Instruction Retention Details}\label{sec:appendix-ir}
105:\section{Long-Conversation AR Evaluation}\label{sec:appendix-n5}
133:\section{Statistical Test Details}\label{sec:appendix-stats}
169:\section{Llama-3.1-8B Complete Results}\label{sec:appendix-llama}
234:\section{Additional Visualizations}\label{sec:appendix-viz}
304:\subsection{Full Attention Steering Results}\label{sec:appendix-steering}
338:\section{Per-Layer Gate Profile}\label{sec:appendix-gate-profile}
368:\section{Scheduled Sampling Implementation}\label{sec:appendix-ss}
385:\section{Computational Cost Analysis}\label{sec:appendix-cost}
418:\section{Qualitative Steering Examples}\label{sec:appendix-examples}
440:\section{Gradient Conflict Analysis}\label{sec:appendix-gradient}
466:\section{Training Data Characteristics}\label{sec:appendix-data}
487:\section{Exposure Bias Scaling}\label{sec:appendix-eb-scaling}
504:\section{Per-Turn AR GAR Dynamics}\label{sec:appendix-ar-gar-dynamics}
526:\section{Per-Head KL Divergence Analysis}\label{sec:appendix-kl}
551:\section{GAR Definition Robustness}\label{sec:appendix-gar-robust}
575:\section{General Capability Preservation (MMLU)}\label{sec:appendix-mmlu}
599:\section{Cross-Scale Validation (Qwen-2.5-1.5B)}\label{sec:appendix-1.5b}
629:\section{Per-Seed Detailed Results}\label{sec:appendix-perseed}
643:\section{Per-Turn GAR Decay Analysis}\label{sec:appendix-perturn-detail}
673:\section{Extended Dataset Statistics}\label{sec:appendix-dataset-ext}
685:\section{Extended GAR Robustness Analysis}\label{sec:appendix-gar-ext}
702:\section{MMLU Category Breakdown}\label{sec:appendix-mmlu-ext}
721:\section{Extended Cross-Scale Results (Qwen-2.5-1.5B)}\label{sec:appendix-1.5b-ext}
735:\section{Extended Statistical Analysis}\label{sec:appendix-stats-ext}
751:\section{Extended Training Dynamics}\label{sec:appendix-training-ext}
768:\section{Per-$\beta$ Steering Visualization}\label{sec:appendix-steering-viz}
789:\section{Llama-3.1-8B Scheduled Sampling Details}\label{sec:appendix-llama-ss}
839:\section{Use of AI Assistants}\label{sec:appendix-ai}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "379b3c29-b0e2-44ec-8cd7-18b777573370",
  "isSidechain": true,
  "promptId": "7335ce9b-d729-4c25-828e-fb66579eb012",
  "agentId": "ae011bee35620c3ee",
  "type": "user",
  "uuid": "0befee5b-0f17-429a-b200-a862b7285d8b",
  "sourceToolAssistantUUID": "379b3c29-b0e2-44ec-8cd7-18b777573370",
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

_source line 32 · 2026-05-25T14:27:36.872Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Qqakx4dD5CVG5YbFcwedJs`</summary>

```json
{
  "pattern": "Appendix~\\\\ref",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0befee5b-0f17-429a-b200-a862b7285d8b",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
  "requestId": "req_011CbPSh2hYTzTDfGSEZPvHh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8271b71e-63bc-4e9b-9ce3-bf9198ec0664",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0135DssFkSJRz2vZUgGUSR7Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18800,
      "cache_read_input_tokens": 46548,
      "output_tokens": 264,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18800
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 264,
          "cache_read_input_tokens": 46548,
          "cache_creation_input_tokens": 18800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18800,
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

_source line 33 · 2026-05-25T14:27:36.889Z_

<details><summary>↩ Tool result · `toolu_01Qqakx4dD5CVG5YbFcwedJs`</summary>

```text
6:[Omitted long matching line]
12:[Omitted long matching line]
27:[Omitted long matching line]
38:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8271b71e-63bc-4e9b-9ce3-bf9198ec0664",
  "isSidechain": true,
  "promptId": "7335ce9b-d729-4c25-828e-fb66579eb012",
  "agentId": "ae011bee35620c3ee",
  "type": "user",
  "uuid": "3e5beb56-54b2-4cbd-8f60-e4f3146abef9",
  "sourceToolAssistantUUID": "8271b71e-63bc-4e9b-9ce3-bf9198ec0664",
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

_source line 34 · 2026-05-25T14:28:08.851Z_

I have all the information needed. Here is the verdict on each audit finding:

---

**1. [CRITICAL] Introduction C4 "ongoing work"** -- **FALSE (false positive)**

Introduction lines 17-22 list four contributions. C4 (line 21) reads: "The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ~1.3x on Qwen and ~2.9x on Llama with no perplexity degradation, robust across three seeds." There is no "ongoing work" or incomplete language. The contribution states concrete results with specific numbers.

---

**2. [CRITICAL] Missing figure definitions** -- **FALSE (false positive)**

All three labels exist with proper `\begin{figure}` + `\label{}`:
- `\label{fig:gate-shift}` -- `analysis.tex` line 40, inside a `\begin{figure}[H]` at line 36, includes `fig3_gate_shift.pdf`
- `\label{fig:training-pcgrad}` -- `appendix.tex` line 446, inside a figure environment at line 441, includes `fig2_training_pcgrad.pdf`
- `\label{fig:steering-recovery}` -- `experiments.tex` line 20, inside a `\begin{figure}[t]` at line 16, includes `fig5_attention_steering.pdf`

---

**3. [CRITICAL] Missing appendix** -- **FALSE (false positive)**

`sections/appendix.tex` exists and is substantial. `main.tex` line 63 includes it via `\input{sections/appendix}`. The appendix contains **30+ sections** (labeled `sec:appendix-hyper`, `sec:appendix-loss`, `sec:appendix-ir`, `sec:appendix-n5`, `sec:appendix-stats`, `sec:appendix-llama`, `sec:appendix-viz`, `sec:appendix-steering`, `sec:appendix-gate-profile`, `sec:appendix-ss`, `sec:appendix-cost`, `sec:appendix-examples`, `sec:appendix-gradient`, `sec:appendix-data`, `sec:appendix-eb-scaling`, `sec:appendix-ar-gar-dynamics`, `sec:appendix-kl`, `sec:appendix-gar-robust`, `sec:appendix-mmlu`, `sec:appendix-1.5b`, `sec:appendix-perseed`, `sec:appendix-perturn-detail`, `sec:appendix-dataset-ext`, `sec:appendix-gar-ext`, `sec:appendix-mmlu-ext`, `sec:appendix-1.5b-ext`, `sec:appendix-stats-ext`, `sec:appendix-training-ext`, `sec:appendix-steering-viz`, `sec:appendix-llama-ss`, `sec:appendix-ai`).

---

**4. [CRITICAL] Only 1 \includegraphics** -- **FALSE (false positive)**

Main text files contain **6** `\includegraphics` commands:
- `introduction.tex`: 1 (`fig1_headline.pdf`)
- `method.tex`: 1 (`fig4_attention_heatmap.pdf`)
- `experiments.tex`: 2 (`fig5_attention_steering.pdf`, `fig_ss_gap_compression.pdf`)
- `analysis.tex`: 2 (`fig_ss_multiseed.pdf`, `fig3_gate_shift.pdf`)
- `discussion.tex`: 0
- `conclusion.tex`: 0

The appendix has an additional **27** `\includegraphics` commands. Total across all `.tex` files: **33**.

---

**5. [CRITICAL] $\sigma_\text{min}$ undefined** -- **FALSE (false positive)**

`method.tex` line 55 explicitly defines it: `$\sigma_\text{min} = 0.05$ is a minimum standard deviation threshold`. The numerical value 0.05 is given inline within the loss formulation description.

---

**6. [WARNING] fig1_overview still used as main figure** -- **FALSE (false positive)**

`introduction.tex` line 11 uses `fig1_headline.pdf`, not `fig1_overview.pdf`. The headline figure is correctly in place as Figure 1.

---

**7. [WARNING] Limitations too long** -- **FALSE (false positive)**

`limitations.tex` is exactly **3 lines** of LaTeX (1 `\section` declaration + 1 paragraph of text). It covers 3 limitation points in a single compact paragraph: (1) two model families + single dataset, (2) mostly single seed + PPL-only quality assessment, (3) only one auxiliary loss family tested. This is appropriately brief.

---

**8. [WARNING] experiments.tex references Appendix~A** -- **PARTIAL (partially true, but not problematic)**

`experiments.tex` references multiple appendix sections (lines 6, 12, 27, 38). All referenced appendix labels exist in `appendix.tex`:
- `sec:appendix-cost` -- exists (line 385)
- `sec:appendix-hyper` -- exists (line 1)
- `sec:appendix-data` -- exists (line 466)
- `sec:appendix-dataset-ext` -- exists (line 673)
- `sec:appendix-stats` -- exists (line 133)
- `sec:appendix-stats-ext` -- exists (line 735)
- `sec:appendix-steering` -- exists (line 304)
- `sec:appendix-steering-viz` -- exists (line 768)
- `sec:appendix-ir` -- exists (line 66)
- `sec:appendix-ss` -- exists (line 368)
- `sec:appendix-perseed` -- exists (line 629)
- `sec:appendix-gar-robust` -- exists (line 551)
- `sec:appendix-gar-ext` -- exists (line 685)
- `sec:appendix-n5` -- exists (line 105)
- `sec:appendix-mmlu-ext` -- exists (line 702)

All appendix cross-references resolve correctly. The audit claim is a false positive; the references use `\ref{sec:appendix-...}` labels, not hardcoded "Appendix A" text, and all targets exist.

---

**Summary**: 7 out of 8 findings are **FALSE** (false positives). Finding #8 is technically **FALSE** as well -- all appendix references resolve. The audit was clearly reading stale file versions. The paper is in good shape on all checked points.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e5beb56-54b2-4cbd-8f60-e4f3146abef9",
  "isSidechain": true,
  "agentId": "ae011bee35620c3ee",
  "requestId": "req_011CbPShMPh8insWdR2LeVkz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87a7c368-f968-4c08-b2fb-1ac7efd70a86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWL9ok3rCRVGhpex5EBqeM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1095,
      "cache_read_input_tokens": 65348,
      "output_tokens": 1607,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1095
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1607,
          "cache_read_input_tokens": 65348,
          "cache_creation_input_tokens": 1095,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1095,
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
