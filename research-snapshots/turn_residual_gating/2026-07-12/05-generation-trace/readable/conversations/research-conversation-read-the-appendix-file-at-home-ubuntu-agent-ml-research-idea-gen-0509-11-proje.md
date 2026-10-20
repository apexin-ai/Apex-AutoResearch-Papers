# Research conversation: Read the appendix file at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 10
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a2a601b3381d36eca.jsonl`
- **Structured JSON:** [`0c15ed8dcc872c91d52c.json`](../../sessions/0c/0c15ed8dcc872c91d52c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

10 recorded events

### User

_source line 1 · 2026-05-25T19:41:05.109Z_

Read the appendix file at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex and extract EVERY number that appears. This includes:
- Numbers in tables (hyperparameter tables, extended results, etc.)
- Numbers in figure captions
- Numbers in running text
- Dataset statistics
- All numerical values

For each number, record:
1. Approximate line number
2. The exact number and its context
3. What it refers to

Be EXHAUSTIVE.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "06680b7d-c294-4388-addf-d95914654fbd",
  "agentId": "a2a601b3381d36eca",
  "type": "user",
  "uuid": "6c5786bb-ce22-43d2-89c9-437f23e96871",
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

_source line 2 · 2026-05-25T19:41:05.112Z_

```json
{
  "parentUuid": "6c5786bb-ce22-43d2-89c9-437f23e96871",
  "isSidechain": true,
  "agentId": "a2a601b3381d36eca",
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
  "uuid": "01aff932-c440-4341-b52e-109f41d8190d",
  "timestamp": "2026-05-25T19:41:05.112Z",
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

_source line 3 · 2026-05-25T19:41:08.720Z_

I'll read the appendix file and extract every number systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01aff932-c440-4341-b52e-109f41d8190d",
  "isSidechain": true,
  "agentId": "a2a601b3381d36eca",
  "requestId": "req_011CbPrbnTCRRtvSLzyFTfjp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c76ad0a-eeae-4652-917a-84c80b7c3f0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01F7cuZj4Sh27Y4qkQUqPxL6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24921,
      "cache_read_input_tokens": 8308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24921,
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

_source line 4 · 2026-05-25T19:41:09.562Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T4EzYFj59um5ZLi2ceuHWx`</summary>

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
  "parentUuid": "9c76ad0a-eeae-4652-917a-84c80b7c3f0c",
  "isSidechain": true,
  "agentId": "a2a601b3381d36eca",
  "requestId": "req_011CbPrbnTCRRtvSLzyFTfjp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cecb798a-23d4-4fbb-90e3-4584e5e1274b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01F7cuZj4Sh27Y4qkQUqPxL6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24921,
      "cache_read_input_tokens": 8308,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24921
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 105,
          "cache_read_input_tokens": 8308,
          "cache_creation_input_tokens": 24921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24921,
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

_source line 5 · 2026-05-25T19:41:09.883Z_

<details><summary>↩ Tool result · reported error · `toolu_01T4EzYFj59um5ZLi2ceuHWx`</summary>

```text
File content (26122 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cecb798a-23d4-4fbb-90e3-4584e5e1274b",
  "isSidechain": true,
  "promptId": "06680b7d-c294-4388-addf-d95914654fbd",
  "agentId": "a2a601b3381d36eca",
  "type": "user",
  "uuid": "09b5a60b-3789-4532-bd56-b06d40272a02",
  "toolUseResult": "Error: File content (26122 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "cecb798a-23d4-4fbb-90e3-4584e5e1274b",
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

_source line 6 · 2026-05-25T19:41:12.250Z_

<details open><summary>🔧 Tool call — Read · `toolu_014FkNHErHejShWfrfdjZtBM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "limit": 400,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09b5a60b-3789-4532-bd56-b06d40272a02",
  "isSidechain": true,
  "agentId": "a2a601b3381d36eca",
  "requestId": "req_011CbPrc8nZtkRst5wacqnHQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72389110-efe5-440b-b4ac-c635b3bbb9fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018Pq3HF3LTxyYQKPXqP4xU3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 33229,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1006
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 33229,
          "cache_creation_input_tokens": 1006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1006,
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

_source line 7 · 2026-05-25T19:41:12.744Z_

<details><summary>↩ Tool result · `toolu_014FkNHErHejShWfrfdjZtBM`</summary>

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
106	The main results (Table~\ref{tab:five-way}) report AR GAR from $N$\,=\,50 held-out conversations with a mean of 3.6 user turns. Table~\ref{tab:n5-ar} presents complementary results on $N$\,=\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.
107	
108	\paragraph{Gating advantage vanishes at length.} In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. ThreadGate's advantage over LoRA-only shrinks from 1.7$\times$ (0.064 vs.\ 0.037 in the $N$\,=\,50 evaluation) to 0.64$\times$ (0.016 vs.\ 0.025), actually reversing the ordering. This reversal is not statistically robust given the small sample ($N$\,=\,5) but directionally suggests that architectural modifications provide diminishing returns as conversation length increases and exposure bias accumulates.
109	
110	\paragraph{Convergence to base.} By turn~10, all fine-tuned variants converge to within 2$\times$ of the base model's GAR, compared to 3.4$\times$ at turn~1 in the shorter evaluation. This convergence is consistent with exposure bias compounding multiplicatively over turns: each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn~10 the accumulated drift overwhelms any gating or LoRA signal, leaving only the base model's intrinsic attention patterns.
111	
112	\paragraph{Caveats.} The $N$\,=\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.
113	
114	\begin{table}[t]
115	\centering\small
116	\caption{AR GAR-ours on $N$\,=\,5 ten-turn conversations. The gating advantage observed in Table~\ref{tab:five-way} ($N$\,=\,50, mean 3.6 turns) diminishes with conversation length.}
117	\label{tab:n5-ar}
118	\begin{tabular}{lcc}
119	\toprule
120	\textbf{Configuration} & \textbf{AR GAR-O} & \textbf{$\Delta$ vs.\ Table~\ref{tab:five-way}} \\
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
138	\paragraph{Bootstrap confidence intervals.} The 95\% CIs in Table~\ref{tab:five-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.
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
261	Figure~\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\% from turn 1 to turn 10; Llama base drops 90\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\ref{tab:five-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.
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
272	Figure~\ref{fig:bootstrap-ci} shows the bootstrap resampling distributions underlying the 95\% CIs reported in Table~\ref{tab:five-way}.
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72389110-efe5-440b-b4ac-c635b3bbb9fb",
  "isSidechain": true,
  "promptId": "06680b7d-c294-4388-addf-d95914654fbd",
  "agentId": "a2a601b3381d36eca",
  "type": "user",
  "uuid": "b68b9992-ee17-4394-95b2-16d9042996be",
  "sourceToolAssistantUUID": "72389110-efe5-440b-b4ac-c635b3bbb9fb",
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

_source line 8 · 2026-05-25T19:41:16.177Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QqJFzuUsTrfArPxmr4za4d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "limit": 200,
  "offset": 399
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b68b9992-ee17-4394-95b2-16d9042996be",
  "isSidechain": true,
  "agentId": "a2a601b3381d36eca",
  "requestId": "req_011CbPrcM1mssG5BLqcKGsag",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c09b05b2-b383-47f9-a431-397fc46d4a6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Cho1Zakg4D9qNCWnBsHtWL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11831,
      "cache_read_input_tokens": 34235,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11831
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 34235,
          "cache_creation_input_tokens": 11831,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11831,
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

_source line 9 · 2026-05-25T19:41:16.182Z_

<details><summary>↩ Tool result · `toolu_01QqJFzuUsTrfArPxmr4za4d`</summary>

```text
399	\;+\,PCGrad & 4.3M & 8.0 & 43\,GB & $+$33\% \\
400	Uniform Gate & 4.3M & 6.0 & 43\,GB & $+$57K \\
401	SS (s42) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
402	SS (s123) & 4.3M & 10.8 & 43\,GB & $+$80\% \\
403	SS (s456) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
404	\midrule
405	\multicolumn{5}{l}{\emph{Llama-3.1-8B-Instruct}} \\
406	LoRA-only & 4.2M & 7.0 & 45\,GB & baseline \\
407	ThreadGate & 4.3M & 7.3 & 46\,GB & $+$65K \\
408	\bottomrule
409	\end{tabular}}
410	\end{table}
411	
412	\paragraph{Parameter overhead.} ThreadGate adds ${\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\times$ 2K per gate MLP) and ${\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.
413	
414	\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 6.0--7.3 hours. PCGrad adds ${\sim}$33\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\% (6.5h) due to efficient batched generation, while seed 123 adds 80\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.
415	
416	\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\to$64$\to$1 MLP forward pass per layer adds $<$0.1\% latency. $\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.
417	
418	\section{Qualitative Steering Examples}\label{sec:appendix-examples}
419	
420	Table~\ref{tab:examples} illustrates the effect of $\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''
421	
422	\begin{table*}[t]
423	\centering\small
424	\caption{Qualitative effect of $\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}
425	\label{tab:examples}
426	\begin{tabular}{c p{5.5cm} p{5.5cm}}
427	\toprule
428	\textbf{Turn} & \textbf{$\beta$\,=\,0 (unsteered)} & \textbf{$\beta$\,=\,3 (steered)} \\
429	\midrule
430	1 & \checkmark~Three bullet points, on-topic & \checkmark~Three bullet points, on-topic \\
431	2 & \checkmark~Three bullet points, relevant & \checkmark~Three bullet points, relevant \\
432	3 & $\sim$~Four bullet points, partially on-topic & \checkmark~Three bullet points, on-topic \\
433	4 & \texttimes~Free-form paragraph, no bullets & \checkmark~Three bullet points, on-topic \\
434	\bottomrule
435	\end{tabular}
436	\end{table*}
437	
438	The pattern is consistent with the GAR decay analysis (\S\ref{sec:analysis}): unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. The per-category breakdown in Table~\ref{tab:ir-results} shows that content constraints benefit most from this effect.
439	
440	\section{Gradient Conflict Analysis}\label{sec:appendix-gradient}
441	
442	\begin{figure}[t]
443	  \centering
444	  \includegraphics[width=\columnwidth,height=0.42\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}
445	  \caption{(a)~Training GAR convergence to target ($\tau$\,=\,0.5). (b)~PCGrad removes gradient conflict but $\mathcal{L}_\text{GAR}$ still collapses, confirming that gradient direction conflict is not the primary cause (\S\ref{subsec:pcgrad}).}
446	  \label{fig:training-pcgrad}
447	\end{figure}
448	
449	This section provides extended gradient interaction analysis supporting the PCGrad exclusion argument in \S\ref{subsec:pcgrad}. We measure per-layer cosine similarity between NTP and GAR gradients, gradient magnitude ratios, and the effect of PCGrad projection on these quantities.
450	
451	\paragraph{Gradient direction analysis.} Figure~\ref{fig:gradient-heatmap} visualizes the per-layer cosine similarity between NTP and GAR gradients across training epochs for both standard ThreadGate and PCGrad training. Under standard training, 79\% of layers show negative cosine similarity (gradient conflict) at epoch~0, declining to 68\% by epoch~2 as GAR loss converges to near-zero. This decline reflects diminishing GAR gradient magnitude rather than alignment improvement---as GAR loss approaches zero, the GAR gradient shrinks proportionally, making cosine similarity measurements less reliable (small gradients produce noisy direction estimates). Under PCGrad training, the conflict percentage decreases more slowly (79\%$\to$71\%), consistent with PCGrad projecting conflicting gradients onto the other's normal plane but not eliminating the underlying gradient conflict.
452	
453	\paragraph{Spatial patterns.} The early layers (L0--L5) and output-adjacent layers (L24--L27) show the strongest conflict, corresponding to the layers where gate values deviate most from identity (Figure~\ref{fig:gate-heatmap}). This spatial correlation is not causal: removing gradient conflict via PCGrad does not improve AR GAR, and gates at high-conflict layers are not systematically different from gates at low-conflict layers (Spearman $\rho$\,=\,$-$0.12, $p$\,=\,0.54 between gate value and conflict magnitude).
454	
455	\paragraph{Magnitude dominance.} NTP gradient magnitude dominates GAR by 7.5$\times$ at epoch~0 and 14.7$\times$ by epoch~2, as GAR loss converges while NTP loss remains at $\sim$0.93. This growing dominance means that even when directions oppose, the effective update direction is determined almost entirely by NTP. PCGrad addresses gradient conflict but not magnitude dominance---it projects conflicting gradients onto the other's normal plane (changing direction) but preserves relative magnitudes. The 7.5--14.7$\times$ magnitude ratio means that even after PCGrad projection, GAR contributes $<$7\% of the effective update magnitude, explaining why PCGrad is ineffective.
456	
457	\paragraph{Cross-model consistency.} Table~\ref{tab:gradient-crossmodel} confirms the pattern on Llama-3.1-8B: gradients are near-orthogonal (mean cosine $+$0.005, essentially zero) rather than systematically conflicting, with 25.7$\times$ NTP dominance. The Llama result is particularly informative because it shows that even without systematic gradient conflict (53\% negative layers, near chance), the same TF-AR gap persists. This cross-model evidence strengthens the \textit{modus tollens} argument: if gradient conflict were the cause, it should be present on both architectures; it is absent on Llama, yet the gap persists; therefore gradient direction conflict is not the primary cause.
458	
459	\begin{figure*}[t]
460	\centering
461	\includegraphics[width=0.95\textwidth]{fig_gradient_conflict_heatmap.pdf}
462	\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\% to 68\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\%$\to$71\%) but does not improve AR GAR, ruling out gradient direction conflict as the primary cause (\S\ref{subsec:pcgrad}).}
463	\label{fig:gradient-heatmap}
464	\end{figure*}
465	
466	\section{Training Data Characteristics}\label{sec:appendix-data}
467	
468	All experiments use 8,000 multi-turn conversations sampled from the UltraChat \citep{ding2023ultrachat} training split. Table~\ref{tab:data-stats} summarizes the dataset characteristics. Conversations are truncated to 2,048 tokens; conversations shorter than 3 user turns are excluded to ensure sufficient multi-turn structure for GAR computation. The held-out evaluation sets use separate non-overlapping samples: $N$\,=\,50 conversations (mean 3.6 user turns) for the primary AR evaluation and $N$\,=\,5 conversations (10 turns each) for the long-conversation analysis (Appendix~\ref{sec:appendix-n5}).
469	
470	\begin{table}[t]
471	\centering\small
472	\caption{Training and evaluation data characteristics. All data from UltraChat \citep{ding2023ultrachat}.}
473	\label{tab:data-stats}
474	\begin{tabular}{lcc}
475	\toprule
476	\textbf{Property} & \textbf{Train} & \textbf{Eval (primary)} \\
477	\midrule
478	Conversations & 8,000 & 50 \\
479	Min user turns & 3 & 3 \\
480	Max sequence length & 2,048 & 2,048 \\
481	Source & UltraChat train & UltraChat train \\
482	Overlap & --- & non-overlapping \\
483	\bottomrule
484	\end{tabular}
485	\end{table}
486	
487	\section{Exposure Bias Scaling}\label{sec:appendix-eb-scaling}
488	
489	Figure~\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).
490	
491	\paragraph{Cross-variant gaps.} On Qwen, ThreadGate achieves the smallest gap among standard variants (7.8$\times$) while PCGrad shows the largest (16.7$\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\sim}$1.3$\times$, the only variant approaching parity. The ordering of gap ratios (SS $\ll$ TG $<$ LoRA $<$ UG $<$ PCGrad) differs from the ordering of TF GAR (all $\approx$ 0.50), confirming that training-time optimization success does not predict inference-time robustness. On Llama, both ThreadGate and LoRA-only show $\sim$27$\times$ gaps (by median), larger than any Qwen variant. The consistently larger Llama gaps may reflect its deeper architecture (32 vs.\ 28 layers), which provides more layers for distributional drift to compound through.
492	
493	\paragraph{Length-dependent compounding.} Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\,=\,50), ThreadGate's gap is 8$\times$; at 10 turns ($N$\,=\,5), it widens to 31$\times$. The relationship is approximately linear in the number of turns on a log scale, suggesting that the per-turn drift contribution is roughly multiplicative. Extrapolating this trend suggests that at 20 turns the gap would exceed 100$\times$, making any training-time attention signal essentially undetectable. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.
494	
495	\paragraph{Implications for deployment.} These scaling results have practical implications: (1)~for applications requiring sustained attention over many turns (e.g., long-form tutoring, multi-step reasoning), architectural modifications alone are insufficient---distributional robustification or inference-time intervention is necessary; (2)~the near-parity of scheduled sampling (${\sim}$1.3$\times$ gap) suggests that bridging the training-inference distribution gap is both necessary and sufficient for maintaining attention; (3)~the $\beta$-steering approach provides a complementary inference-time solution, but its effectiveness also depends on conversation length (Appendix~\ref{sec:appendix-steering-viz}).
496	
497	\begin{figure}[t]
498	\centering
499	\includegraphics[width=\columnwidth]{fig_eb_scaling.pdf}
500	\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\sim}$1.3$\times$) is the only variant near parity. Llama gaps ($\sim$27$\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\times$ (3.6 turns) to 31$\times$ (10 turns).}
501	\label{fig:eb-scaling}
502	\end{figure}
503	
504	\section{Per-Turn AR GAR Dynamics}\label{sec:appendix-ar-gar-dynamics}
505	
506	To characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.
507	
508	All six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\ref{tab:five-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\S\ref{subsec:ss}).}
509	
510	\begin{figure}[t]
511	\centering
512	\includegraphics[width=\columnwidth]{fig_kl_ar_gar_curves.pdf}
513	\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}
514	\label{fig:kl_ar_gar_curves}
515	\end{figure}
516	
517	\begin{figure}[t]
518	\centering
519	\includegraphics[width=\columnwidth]{fig_kl_ar_gar_bar.pdf}
520	\caption{Mid-turn AR GAR comparison across six training configurations. Ranking from highest to lowest: Scheduled Sampling (0.423), ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), Base (0.019).}
521	\label{fig:kl_ar_gar_bar}
522	\end{figure}
523	
524	This pattern contrasts with teacher-forced evaluation, where GAR remains relatively stable across turns for all configurations. Under teacher forcing, the model conditions on ground-truth context at each turn, preventing the distributional drift that causes GAR erosion in AR mode. The divergence between TF stability and AR decay provides turn-level evidence for the exposure bias mechanism described in \S\ref{sec:analysis}: training-time attention patterns are optimized for a distribution that AR generation progressively departs from.
525	
526	\section{Per-Head KL Divergence Analysis}\label{sec:appendix-kl}
527	
528	To test whether exposure bias selectively disrupts goal-attending heads rather than uniformly affecting all attention patterns, we compute per-head TF vs.\ AR attention divergence on 30 held-out conversations. For each of the 28 attention heads per layer (784 heads total), we measure the KL divergence $D_\text{KL}(p_\text{TF} \| p_\text{AR})$ between teacher-forced and autoregressive attention distributions, and the absolute GAR shift $\Delta\text{GAR} = |\text{GAR}_\text{TF} - \text{GAR}_\text{AR}|$. This head-level analysis provides diagnostic evidence for the exposure bias interpretation beyond the aggregate TF-AR gap.
529	
530	\begin{table}[t]
531	\centering\small
532	\caption{Per-head TF-AR divergence statistics for Base and ThreadGate (Qwen-2.5-7B, 30 conversations). TG trains more concentrated goal attention under TF, but these high-GAR heads shift most under AR ($r$\,=\,0.743).}
533	\label{tab:kl-perhead}
534	\begin{tabular}{lcc}
535	\toprule
536	\textbf{Metric} & \textbf{Base} & \textbf{TG} \\
537	\midrule
538	Mean $\Delta$GAR & 0.012 & 0.016 \\
539	Mean KL & 0.043 & 0.054 \\
540	Corr(TF\_GAR, $\Delta$GAR) & 0.673 & 0.743 \\
541	\bottomrule
542	\end{tabular}
543	\end{table}
544	
545	\paragraph{Selective disruption.} ThreadGate exhibits 35\% larger mean $\Delta$GAR (0.016 vs.\ 0.012) and 26\% larger mean KL (0.054 vs.\ 0.043) than Base. This is counterintuitive: the auxiliary GAR loss successfully trains more concentrated goal attention (higher TF GAR per head), but these very same heads shift more under AR generation. The correlation between per-head TF GAR and $\Delta$GAR is strong for both models ($r$\,=\,0.673 for Base, 0.743 for TG), confirming that heads with higher goal attention under teacher forcing are disproportionately disrupted under autoregressive generation. This selectivity is a hallmark of exposure bias: the training-time optimization succeeds at creating a specific attention pattern (concentrated goal attention), but precisely this pattern has no autoregressive counterpart because it depends on conditioning on ground-truth context.
546	
547	\paragraph{Layer-depth dependence.} The highest-KL heads concentrate at output-adjacent layers (L23--L27, KL\,$>$\,0.077) and L9 (KL\,$\approx$\,0.068). Output-adjacent layers participate most directly in next-token prediction, so their attention distributions are most sensitive to changes in the conditioning context. L9's elevated KL may reflect a ``routing layer'' phenomenon observed in multi-layer transformers, where specific intermediate layers specialize in long-range information routing. The depth dependence is consistent with cumulative error propagation: distributional drift from model-generated tokens accumulates as information flows through successive layers, producing the largest attention shifts at the deepest layers.
548	
549	\paragraph{Gate--KL independence.} Gate magnitude does not predict per-layer exposure bias severity: Spearman correlation between gate value and per-layer KL is 0.061 ($p$\,=\,0.757). The highest KL values concentrate at deep layers (L22--L27) where gates are near identity ($\approx$1.0), while the lowest-gate layers show below-average KL (0.041 vs.\ 0.056 for highest-gate layers). This independence confirms that the gating mechanism and the exposure bias phenomenon operate on different axes: gates modulate the magnitude of residual contributions, while exposure bias disrupts the direction (attention distribution) of those contributions. Even a ``perfect'' gate that could fully attenuate certain layers' residuals would not address the fundamental distributional mismatch that causes the attention shift.
550	
551	\section{GAR Definition Robustness}\label{sec:appendix-gar-robust}
552	
553	To assess whether our conclusions depend on the specific GAR definition, we evaluate four alternative token-position variants on 50 held-out conversations (Table~\ref{tab:gar-robust}): (1)~\emph{ours} (last-token): attention from the last token to goal tokens (standard GAR-ours); (2)~\emph{all-token}: average attention from all tokens to goal tokens; (3)~\emph{first-token}: attention from the first assistant token to goal tokens; (4)~\emph{goal-only}: attention from the last token to system-prompt-only tokens (excluding conversation content).
554	
555	\begin{table}[t]
556	\centering\small
557	\caption{Mid-turn GAR under four alternative definitions ($N$\,=\,50 conversations). ThreadGate only improves query-position-specific definitions (last-token, goal-only); Scheduled Sampling raises all four definitions above 0.36.}
558	\label{tab:gar-robust}
559	\begin{tabular}{lccc}
560	\toprule
561	\textbf{Definition} & \textbf{Base} & \textbf{TG} & \textbf{SS} \\
562	\midrule
563	Ours (last-token) & 0.015 & \textbf{0.325} & \textbf{0.458} \\
564	All-token & 0.015 & 0.025 & \textbf{0.366} \\
565	First-token & 0.022 & 0.039 & \textbf{0.412} \\
566	Goal-only & 0.005 & \textbf{0.310} & \textbf{0.444} \\
567	\bottomrule
568	\end{tabular}
569	\end{table}
570	
571	ThreadGate improvements are query-position-specific: the two definitions using the last token as query (ours: $0.015 \to 0.325$; goal-only: $0.005 \to 0.310$) show large gains, while all-token ($0.025$) and first-token ($0.039$) remain near base levels. This is expected: the GAR loss optimizes attention at the last-token position, so the learned routing does not generalize to other query positions.
572	
573	Scheduled Sampling raises all four definitions above 0.36, with no definition falling below Base-relative gains. This confirms that SS builds a broad goal-attention pattern across token positions, rather than overfitting to the specific position targeted by the GAR loss. The pattern holds regardless of GAR definition: both the exposure bias diagnosis and the SS mitigation are robust to metric choice.
574	
575	\section{General Capability Preservation (MMLU)}\label{sec:appendix-mmlu}
576	
577	To confirm that auxiliary GAR losses and attention steering do not degrade general language understanding, we evaluate all six Qwen-2.5-7B variants on MMLU 5-shot \citep{hendrycks2021measuring} ($N$\,=\,14{,}042 questions).
578	
579	\begin{table}[t]
580	\centering\small
581	\caption{MMLU 5-shot accuracy on Qwen-2.5-7B-Instruct. All fine-tuned variants remain within 0.8\,pp of the base LoRA-only checkpoint.}
582	\label{tab:mmlu}
583	\begin{tabular}{lcc}
584	\toprule
585	\textbf{Model} & \textbf{Acc (\%)} & \textbf{$\Delta$ vs Base} \\
586	\midrule
587	Base (LoRA-only) & 74.23 & --- \\
588	PCGrad & 73.86 & $-$0.38 \\
589	SS & 73.75 & $-$0.48 \\
590	LoRA-only & 73.57 & $-$0.66 \\
591	ThreadGate & 73.47 & $-$0.77 \\
592	Uniform Gate & 73.46 & $-$0.78 \\
593	\bottomrule
594	\end{tabular}
595	\end{table}
596	
597	All variants degrade by $<$0.8\,pp, confirming that attention steering and auxiliary GAR losses do not harm general language understanding. The ordering does not track GAR performance (e.g., PCGrad shows the smallest MMLU drop despite the worst AR GAR), consistent with GAR and NTP occupying largely orthogonal subspaces.
598	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c09b05b2-b383-47f9-a431-397fc46d4a6b",
  "isSidechain": true,
  "promptId": "06680b7d-c294-4388-addf-d95914654fbd",
  "agentId": "a2a601b3381d36eca",
  "type": "user",
  "uuid": "b274cce7-895d-43a9-84e3-3bea5d4b7b0f",
  "sourceToolAssistantUUID": "c09b05b2-b383-47f9-a431-397fc46d4a6b",
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

_source line 10 · 2026-05-25T19:44:20.595Z_

Now I have the complete file. Let me compile the exhaustive list of every number found.

Here is the exhaustive extraction of every number in `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex`:

---

## Section: Training Configuration (lines 0–32)

| Line | Number | Context |
|------|--------|---------|
| 2 | 10× | Gate parameter learning rate multiplier |
| 2 | 1.5 | Gate bias initialization value |
| 2 | 0.82 | σ(1.5) ≈ 0.82, gate init sigmoid value |
| 2 | ~57K | Gate MLP parameters per variant |
| 2 | <0.001% | Fraction of 7B parameters |
| 2 | 7B | Base model parameter count (Qwen-2.5-7B) |
| 2 | 0 | SS model-generated context ratio start |
| 2 | 0.5 | SS model-generated context ratio end |
| 2 | 3 | Epochs over which ratio increases |
| 2 | 29.7% | SS effective usage lower bound |
| 2 | 37.1% | SS effective usage upper bound |
| 2 | 96 GB | GPU VRAM (RTX PRO 6000) |
| 2 | 6 h | Training time lower bound per variant |
| 2 | 8 h | Training time upper bound per variant |
| 13 | 16 | LoRA rank |
| 13 | 32 | LoRA alpha |
| 15 | 0.9 | AdamW β₁ |
| 15 | 0.999 | AdamW β₂ |
| 16 | 2×10⁻⁴ | Learning rate |
| 17 | 10× | Gate LR multiplier (table row) |
| 18 | 1 | Batch size |
| 18 | 8 | Gradient accumulation steps |
| 18 | 8 | Effective batch size |
| 19 | 3 | Epochs |
| 20 | 2048 | Max sequence length |
| 21 | 8K | Training data size (UltraChat convs) |
| 22 | 42 | Random seed (primary) |
| 22 | 123 | Additional seed (for TG, SS) |
| 23 | 1.0 | λ_GAR |
| 23 | 1.0 | λ_div |
| 24 | 0.5 | GAR target τ |
| 25 | 1.5 | Gate init bias (table row) |
| 25 | 0.82 | σ ≈ 0.82 (table row) |
| 26 | 64 | Gate hidden dimension |
| 27 | 16 | Turn embed dimension |
| 28 | 96 GB | GPU VRAM (table row) |
| 29 | 6 h | Training time lower (table row) |
| 29 | 8 h | Training time upper (table row) |

---

## Section: Loss Formulation Search (lines 34–63)

| Line | Number | Context |
|------|--------|---------|
| 36 | 7 | Number of loss iterations |
| 36 | 4 | Number of loss families |
| 38 | 28 | Number of per-layer terms in cumulative product |
| 40 | 0.025 | Gate diversity std collapse threshold (std < 0.025) |
| 40 | 2 | λ for v3 (Maximize loss) |
| 40 | 100 | Steps within which gates froze for v3 |
| 40 | 10 | λ for v3b |
| 40 | 1 | λ for v5 |
| 56 | 2 | λ=2, v3 table row |
| 57 | 10 | λ=10, v3b table row |
| 58 | 1 | λ=1, v5 table row |
| 60 | 0.50 | GAR-ours for converged v7 |
| 60 | 2.78 | PPL for converged v7 |

---

## Section: Instruction Retention Details (lines 65–102)

| Line | Number | Context |
|------|--------|---------|
| 67 | 18 | Number of system-prompt constraint types |
| 67 | 3 | β=3 steering value |
| 67 | 200 | N=200 held-out conversations |
| 69 | 18 | Constraint types in McNemar analysis |
| 69 | 54 | Paired evaluations (18 types × 3 conversations) |
| 69 | 3 | Conversations per type |
| 71 | +23.8 pp | Content constraints improvement |
| 71 | +6.7 pp | Position constraints improvement |
| 72 | 0.200 | GAR-compliance Pearson r |
| 72 | 0.007 | GAR-compliance p-value |
| 72 | 0.077 | McNemar's test p-value |
| 72 | 18 | Constraint types (McNemar sample size) |
| 80 | 3 | β=3 in figure caption |
| 80 | +23.8 pp | Content constraint gain in caption |
| 88 | 3 | β=3 in table caption |
| 92 | 0 (β=0) | Column header: unsteered |
| 92 | 3 (β=3) | Column header: steered |
| 94 | 61.9% | Content β=0 compliance rate |
| 94 | 85.7% | Content β=3 compliance rate |
| 94 | +23.8 pp | Content Δ |
| 95 | 66.7% | Position β=0 compliance rate |
| 95 | 73.3% | Position β=3 compliance rate |
| 95 | +6.7 pp | Position Δ |
| 96 | 100% | Count β=0 compliance rate |
| 96 | 100% | Count β=3 compliance rate |
| 96 | 0 | Count Δ |
| 97 | 100% | Format β=0 compliance rate |
| 97 | 100% | Format β=3 compliance rate |
| 97 | 0 | Format Δ |
| 99 | 75.9% | Overall β=0 compliance rate |
| 99 | 87.0% | Overall β=3 compliance rate |
| 99 | +11.1 pp | Overall Δ |

---

## Section: Long-Conversation AR Evaluation (lines 104–130)

| Line | Number | Context |
|------|--------|---------|
| 106 | 50 | N=50 held-out conversations (main results) |
| 106 | 3.6 | Mean user turns (N=50 set) |
| 106 | 5 | N=5 long-conversation evaluation |
| 106 | 10 | Turns per conversation (long-conv) |
| 108 | 0.015 | AR GAR-ours lower bound, fine-tuned variants (long conv) |
| 108 | 0.025 | AR GAR-ours upper bound, fine-tuned variants (long conv) |
| 108 | 0.030 | AR GAR lower bound, shorter eval |
| 108 | 0.064 | AR GAR upper bound, shorter eval |
| 108 | 1.7× | TG advantage over LoRA-only (N=50) |
| 108 | 0.064 | TG AR GAR (N=50) |
| 108 | 0.037 | LoRA-only AR GAR (N=50) |
| 108 | 0.64× | TG vs LoRA-only ratio (N=5) |
| 108 | 0.016 | TG AR GAR (N=5) |
| 108 | 0.025 | LoRA-only AR GAR (N=5) |
| 108 | 5 | N=5 sample size |
| 110 | 10 | Turn number where all variants converge |
| 110 | 2× | Factor of base model's GAR at turn 10 |
| 110 | 3.4× | Factor difference at turn 1 in shorter eval |
| 112 | 5 | N=5 sample size caveat |
| 112 | 10 | 10-turn conversations |
| 112 | 3 | Minimum turns |
| 112 | 5 | Maximum turns in training distribution |
| 116 | 5 | N=5 in table caption |
| 116 | 10 | Ten-turn conversations in caption |
| 116 | 50 | N=50 in caption reference |
| 116 | 3.6 | Mean turns in caption |
| 122 | 0.012 | Base AR GAR-O (N=5) |
| 122 | −0.007 | Base Δ vs Table five-way |
| 124 | 0.016 | ThreadGate AR GAR-O (N=5) |
| 124 | −0.048 | ThreadGate Δ vs Table five-way |
| 125 | 0.015 | +PCGrad AR GAR-O (N=5) |
| 125 | −0.015 | +PCGrad Δ vs Table five-way |
| 126 | 0.015 | Uniform Gate AR GAR-O (N=5) |
| 126 | −0.018 | Uniform Gate Δ vs Table five-way |
| 127 | 0.025 | LoRA-only AR GAR-O (N=5) |
| 127 | −0.012 | LoRA-only Δ vs Table five-way |

---

## Section: Statistical Test Details (lines 132–166)

| Line | Number | Context |
|------|--------|---------|
| 136 | 0.004 | p-value, TG vs LoRA-only Wilcoxon |
| 136 | 0.454 | r effect size, TG vs LoRA-only |
| 136 | 0.002 | p-value, TG vs +PCGrad Wilcoxon |
| 136 | 28 | Layers, gate turn conditioning unpaired test |
| 138 | 95% | Confidence interval level |
| 138 | 10,000 | Bootstrap resamples |
| 138 | 2 | Start of mid-turn range (turns 2–T) |
| 140 | 0.3 | Small effect size threshold (r < 0.3) |
| 140 | 0.3 | Medium effect size lower bound (0.3 ≤ r < 0.5) |
| 140 | 0.5 | Large effect size threshold (r ≥ 0.5) |
| 140 | 0.454 | TG vs LoRA-only effect size (medium) |
| 140 | 0.802 | TG vs Base effect size (large) |
| 142 | 4 | Number of primary AR comparisons (Bonferroni) |
| 142 | 0.0125 | Bonferroni-adjusted significance threshold |
| 142 | 0.004 | Significance threshold after correction |
| 146 | 50 | N=50 conversations in table caption |
| 146 | 39 | Conversations with ≥3 turns |
| 146 | 28 | Layers for gate conditioning |
| 153 | <0.001 | p-value, TG vs Base |
| 153 | 0.802 | r, TG vs Base |
| 154 | 0.004 | p-value, TG vs LoRA-only |
| 154 | 0.454 | r, TG vs LoRA-only |
| 155 | 0.002 | p-value, TG vs +PCGrad |
| 156 | <0.001 | p-value, SS vs TG |
| 156 | 0.869 | r, SS vs TG |
| 159 | 3.7×10⁻⁸ | p-value, Turn 1 vs Turn 21 gate conditioning |
| 159 | 0.975 | r, Turn 1 vs Turn 21 |
| 163 | 0.077 | p-value, β=0 vs β=3 McNemar |
| 163 | 0.007 | p-value (Pearson), GAR–compliance |
| 163 | 0.200 | r (Pearson), GAR–compliance |

---

## Section: Llama-3.1-8B Complete Results (lines 168–214)

| Line | Number | Context |
|------|--------|---------|
| 170 | 8K | UltraChat training size |
| 170 | 3 | Epochs |
| 170 | 16 | LoRA rank |
| 170 | 7.0 h | Training time lower bound (Llama) |
| 170 | 7.3 h | Training time upper bound (Llama) |
| 172 | 0.484 | TF GAR-ours, TG (Llama) |
| 172 | 0.481 | TF GAR-ours, LoRA-only (Llama) |
| 172 | 0.50 | TF GAR for both (Qwen, for comparison) |
| 174 | 20 | N=20 mid-turn AR conversations (Llama) |
| 174 | 3 | Turns 3–T (first two excluded) |
| 174 | 100% | Coefficient of variation exceeds (for TG mean) |
| 174 | 0.043 | Mean AR GAR-ours, TG (Llama) |
| 174 | 0.100 | Std AR GAR-ours, TG (Llama) |
| 174 | 5% | Fraction of turn-level measurements with spikes |
| 174 | 0.4 | GAR spike threshold |
| 176 | 0.793 | Qwen gate value, L1 (minimum early-layer) |
| 176 | 0.797 | Qwen gate value, L5 |
| 176 | 0.719 | Llama gate value, L25 (V-valley minimum) |
| 176 | 0.809 | Llama gate value, L24 |
| 176 | 27× | TF-AR gap by median, Llama TG |
| 176 | 8× | TF-AR gap lower bound, Qwen |
| 176 | 17× | TF-AR gap upper bound, Qwen |
| 180 | 50 | N=50 TF evaluation |
| 180 | 20 | N=20 for Base/TG/LoRA-only |
| 180 | 50 | N=50 for SS |
| 189 | 0.017 | Base TF GAR-O (Llama) |
| 189 | 3.45 | Base PPL (Llama) |
| 189 | 0.009 | Base AR GAR-O mean (Llama) |
| 189 | 0.009 | Base AR GAR-O median (Llama) |
| 190 | 0.484 | ThreadGate TF GAR-O (Llama) |
| 190 | 2.57 | ThreadGate PPL (Llama) |
| 190 | 0.043 | ThreadGate AR GAR-O mean (Llama) |
| 190 | 0.018 | ThreadGate AR GAR-O median (Llama) |
| 191 | 0.481 | LoRA-only TF GAR-O (Llama) |
| 191 | 2.60 | LoRA-only PPL (Llama) |
| 191 | 0.028 | LoRA-only AR GAR-O mean (Llama) |
| 191 | 0.018 | LoRA-only AR GAR-O median (Llama) |
| 192 | 0.477 | SS TF GAR-O (Llama) |
| 192 | 2.82 | SS PPL (Llama) |
| 192 | 0.166 | SS AR GAR-O mean (Llama) |
| 202 | 27× | TF-AR gap by median (Llama), figure caption |
| 202 | 8× | Qwen gap reference in caption |
| 206 | 27× | TG gap by median (Llama) cross-model summary |
| 206 | 11.2× | Llama mean-based gap lower bound |
| 206 | 17.2× | Llama mean-based gap upper bound |
| 206 | 7.9× | Qwen gap lower bound |
| 206 | 13.5× | Qwen gap upper bound |
| 206 | 32 | Llama layer count |
| 206 | 28 | Qwen layer count |
| 210 | 1.002× | GAR-Dongre AR/TF ratio on Llama |
| 210 | 1.28× | GAR-Dongre AR/TF ratio on Qwen |
| 212 | 8K | UltraChat conversations |
| 212 | 16 | LoRA rank |
| 212 | 3 | Epochs |
| 212 | 0.929 | Training loss (LoRA-only, Llama) |
| 212 | 0.934 | Training loss (ThreadGate, Llama) |
| 212 | 7.0 h | Wall-clock time (LoRA-only, Llama) |
| 212 | 7.3 h | Wall-clock time (ThreadGate, Llama) |
| 212 | 17% | Longer than Qwen due to layer count |
| 212 | 32 | Llama layer count |
| 212 | 28 | Qwen layer count |
| 214 | 0.026 | Base Llama GAR at turn 1 |
| 214 | 0.003 | Base Llama GAR at turn 10 |
| 214 | 90% | Decline in Llama base GAR (turn 1→10) |
| 214 | 70.8% | Decline in Qwen base GAR |
| 214 | 32 | Llama KV head count |
| 214 | 28 | Qwen KV head count |

---

## Section: Cross-model gradient analysis (lines 216–231)

| Line | Number | Context |
|------|--------|---------|
| 216 | 0 | Cosine similarity ≈ 0 (near-orthogonal) |
| 216 | −0.042 | Qwen mean cosine similarity |
| 216 | +0.005 | Llama mean cosine similarity |
| 216 | 14.7× | Qwen NTP/GAR gradient magnitude ratio |
| 216 | 25.7× | Llama NTP/GAR gradient magnitude ratio |
| 226 | −0.042 | Mean cos sim, Qwen (table) |
| 226 | +0.005 | Mean cos sim, Llama (table) |
| 227 | 67.9% | Neg-layer %, Qwen |
| 227 | 53.1% | Neg-layer %, Llama |
| 228 | 14.7× | NTP/GAR magnitude ratio, Qwen (table) |
| 228 | 25.7× | NTP/GAR magnitude ratio, Llama (table) |

---

## Section: Additional Visualizations (lines 233–301)

| Line | Number | Context |
|------|--------|---------|
| 239 | 28 | Qwen layers (gate profile heatmap) |
| 239 | 32 | Llama layers |
| 244 | 28 | Qwen layers × 5 conditions (caption) |
| 244 | 32 | Llama layers × 1 condition (caption) |
| 250 | 0.793 | Qwen L1 gate value |
| 250 | 0.797 | Qwen L5 gate value |
| 250 | 0.719 | Llama L25 gate value |
| 255 | 0.793 | Qwen L1 gate value (figure caption) |
| 255 | 0.797 | Qwen L5 gate value (caption) |
| 255 | 0.719 | Llama L25 gate value (caption) |
| 261 | 85% | Qwen base GAR drop (turn 1→10) |
| 261 | 90% | Llama base GAR drop (turn 1→10) |
| 266 | 85% | Qwen base drop (figure caption) |
| 266 | 90% | Llama base drop (figure caption) |
| 277 | 95% | CI level |
| 277 | 50 | N=50 |
| 277 | 10K | Bootstrap resamples |
| 277 | 0.454 | Effect size r |
| 283 | 0.94 | Gate value distribution mean lower |
| 283 | 0.96 | Gate value distribution mean upper |
| 283 | 0.9 | Gate distribution lower concentration |
| 283 | 1.0 | Gate distribution upper cutoff |
| 288 | 0.94 | Mean gate value lower (caption) |
| 288 | 0.96 | Mean gate value upper (caption) |
| 294 | 1 | Epoch within which GAR collapses |
| 294 | 0.93 | NTP loss convergence at epoch 3 |

---

## Section: Full Attention Steering Results (lines 303–335)

| Line | Number | Context |
|------|--------|---------|
| 308 | 5 | β=5, operating point cited in main text |
| 313 | 5 | N=5, Gen |
| 313 | 50 | N=50, Gen |
| 313 | 200 | N=200, TF |
| 317 | 0 | β=0 |
| 317 | .028 | β=0, N=5 GAR |
| 317 | 1.41 | β=0, N=5 PPL |
| 317 | .064 | β=0, N=50 GAR |
| 317 | .081 | β=0, N=50 GAR std |
| 317 | 1.43 | β=0, N=50 PPL |
| 317 | .10 | β=0, N=50 PPL std |
| 317 | .535 | β=0, N=200 TF GAR |
| 317 | 2.62 | β=0, N=200 PPL |
| 318 | 0.5 | β=0.5 |
| 318 | .029 | β=0.5, N=5 GAR |
| 318 | 1.39 | β=0.5, N=5 PPL |
| 319 | 1 | β=1 |
| 319 | .035 | β=1, N=5 GAR |
| 319 | 1.36 | β=1, N=5 PPL |
| 320 | 2 | β=2 |
| 320 | .062 | β=2, N=5 GAR |
| 320 | 1.41 | β=2, N=5 PPL |
| 320 | .128 | β=2, N=50 GAR |
| 320 | .110 | β=2, N=50 GAR std |
| 320 | 1.48 | β=2, N=50 PPL |
| 320 | .14 | β=2, N=50 PPL std |
| 320 | .611 | β=2, N=200 TF GAR |
| 320 | 2.69 | β=2, N=200 PPL |
| 322 | 3 | β=3 |
| 322 | .556 | β=3, N=50 GAR |
| 322 | .060 | β=3, N=50 GAR std |
| 322 | 1.56 | β=3, N=50 PPL |
| 322 | .17 | β=3, N=50 PPL std |
| 322 | .788 | β=3, N=200 TF GAR |
| 322 | 2.93 | β=3, N=200 PPL |
| 323 | 4 | β=4 |
| 323 | .644 | β=4, N=50 GAR |
| 323 | .061 | β=4, N=50 GAR std |
| 323 | 1.67 | β=4, N=50 PPL |
| 323 | .22 | β=4, N=50 PPL std |
| 323 | .817 | β=4, N=200 TF GAR |
| 323 | 3.49 | β=4, N=200 PPL |
| 324 | 5 | β=5 (bold, operating point) |
| 324 | .680 | β=5, N=5 GAR |
| 324 | 1.91 | β=5, N=5 PPL |
| 324 | .727 | β=5, N=50 GAR |
| 324 | .061 | β=5, N=50 GAR std |
| 324 | 1.77 | β=5, N=50 PPL |
| 324 | .27 | β=5, N=50 PPL std |
| 324 | .833 | β=5, N=200 TF GAR |
| 324 | 6.15 | β=5, N=200 PPL |
| 325 | 10 | β=10 |
| 325 | .959 | β=10, N=5 GAR |
| 325 | 4.22 | β=10, N=5 PPL |
| 325 | .961 | β=10, N=50 GAR |
| 325 | .015 | β=10, N=50 GAR std |
| 325 | 3.45 | β=10, N=50 PPL |
| 325 | 1.78 | β=10, N=50 PPL std |
| 325 | .977 | β=10, N=200 TF GAR |
| 325 | 505.2 | β=10, N=200 PPL |
| 333 | 50 | N=50, figure caption |
| 333 | 3 | β=3 operating point |
| 333 | 9% | PPL cost at β=3 |
| 333 | 8.7× | GAR recovery at β=3 |

---

## Section: Per-Layer Gate Profile (lines 337–365)

| Line | Number | Context |
|------|--------|---------|
| 339 | 123 | Seed for ThreadGate gate profile |
| 339 | 28 | Qwen-2.5-7B layer count |
| 339 | 1 | Layer 1 (lowest gate) |
| 339 | 5 | Layer 5 (lowest gate) |
| 339 | 0.793 | L1 gate value |
| 339 | 0.797 | L5 gate value |
| 339 | 26 | Layer 26 converges to ≥0.988 |
| 339 | 27 | Layer 27 |
| 339 | 0.988 | Gate value at L26–27 |
| 339 | 0.947 | Mean gate value across all layers |
| 339 | 0.051 | σ (std) of gate values |
| 349 | .883 | L0 gate value |
| 349 | .793 | L1 gate value |
| 349 | .996 | L2 gate value |
| 349 | .988 | L3 gate value |
| 349 | .984 | L4 gate value |
| 349 | .797 | L5 gate value |
| 349 | .961 | L6 gate value |
| 349 | .918 | L7 gate value |
| 351 | .965 | L8 gate value |
| 351 | .934 | L9 gate value |
| 351 | .969 | L10 gate value |
| 351 | .918 | L11 gate value |
| 351 | .926 | L12 gate value |
| 351 | .941 | L13 gate value |
| 351 | .930 | L14 gate value |
| 351 | .965 | L15 gate value |
| 354 | .941 | L16 gate value |
| 354 | .910 | L17 gate value |
| 354 | .961 | L18 gate value |
| 354 | .965 | L19 gate value |
| 354 | .973 | L20 gate value |
| 354 | .988 | L21 gate value |
| 354 | .969 | L22 gate value |
| 354 | .980 | L23 gate value |
| 357 | .980 | L24 gate value |
| 357 | .984 | L25 gate value |
| 357 | .988 | L26 gate value |
| 357 | 1.00 | L27 gate value |
| 358 | .947 | Mean gate value (table summary) |
| 358 | .051 | σ of gate values (table summary) |
| 363 | 1 | L1 bimodal dip |
| 363 | 5 | L5 bimodal dip |
| 363 | 17 | Monotonic increase starts at L17 |
| 363 | 27 | Monotonic increase ends at L27 |
| 363 | 0.934 | Seed 42 profile mean gate value |
| 363 | 3 | Seed 42 min at L3 |
| 363 | 5 | Seed 42 min at L5 |

---

## Section: Scheduled Sampling Implementation (lines 367–382)

| Line | Number | Context |
|------|--------|---------|
| 371 | 0 | Initial model-generated context ratio ρ |
| 371 | 0.3 | Final model-generated context ratio ρ |
| 371 | 3 | Epochs over which ρ increases |
| 371 | 29.7% | Effective usage lower bound |
| 371 | 37.1% | Effective usage upper bound |
| 375 | 0.932 | SS final NTP loss |
| 375 | 0.930 | Standard ThreadGate NTP loss |
| 375 | 0.953 | SS gate profile mean |
| 375 | 0.947 | TG gate profile mean |
| 375 | 4 (L4) | SS gate min layer |
| 375 | 1 (L1) | TG gate min layer |
| 375 | 8% | SS training overhead lower bound |
| 375 | 80% | SS training overhead upper bound |
| 375 | 6.5 h | SS training time (seed 42) |
| 375 | 10.8 h | SS training time (seed 123) |
| 375 | 6.5 h | SS training time (seed 456) |
| 375 | 6.0 h | Standard TG training time (Qwen) |
| 375 | 42 | Seed 42 |
| 375 | 123 | Seed 123 |
| 375 | 456 | Seed 456 |
| 380 | 0 | ρ start (figure caption) |
| 380 | 0.3 | ρ end (figure caption) |

---

## Section: Computational Cost Analysis (lines 384–416)

| Line | Number | Context |
|------|--------|---------|
| 396 | 4.2M | LoRA-only parameters (Qwen) |
| 396 | 6.0 h | LoRA-only training time (Qwen) |
| 396 | 42 GB | LoRA-only VRAM (Qwen) |
| 397 | 4.3M | ThreadGate parameters (Qwen) |
| 397 | 6.0 h | ThreadGate training time (Qwen) |
| 397 | 43 GB | ThreadGate VRAM (Qwen) |
| 397 | +57K | ThreadGate overhead |
| 398 | 4.3M | +PCGrad parameters (Qwen) |
| 398 | 8.0 h | +PCGrad training time (Qwen) |
| 398 | 43 GB | +PCGrad VRAM (Qwen) |
| 398 | +33% | +PCGrad overhead |
| 400 | 4.3M | Uniform Gate parameters (Qwen) |
| 400 | 6.0 h | Uniform Gate training time (Qwen) |
| 400 | 43 GB | Uniform Gate VRAM (Qwen) |
| 400 | +57K | Uniform Gate overhead |
| 401 | 4.3M | SS (s42) parameters |
| 401 | 6.5 h | SS (s42) training time |
| 401 | 43 GB | SS (s42) VRAM |
| 401 | +8% | SS (s42) overhead |
| 402 | 4.3M | SS (s123) parameters |
| 402 | 10.8 h | SS (s123) training time |
| 402 | 43 GB | SS (s123) VRAM |
| 402 | +80% | SS (s123) overhead |
| 403 | 4.3M | SS (s456) parameters |
| 403 | 6.5 h | SS (s456) training time |
| 403 | 43 GB | SS (s456) VRAM |
| 403 | +8% | SS (s456) overhead |
| 406 | 4.2M | LoRA-only parameters (Llama) |
| 406 | 7.0 h | LoRA-only training time (Llama) |
| 406 | 45 GB | LoRA-only VRAM (Llama) |
| 407 | 4.3M | ThreadGate parameters (Llama) |
| 407 | 7.3 h | ThreadGate training time (Llama) |
| 407 | 46 GB | ThreadGate VRAM (Llama) |
| 407 | +65K | ThreadGate overhead (Llama) |
| 412 | ~57K | Gate params, Qwen-2.5-7B |
| 412 | 28 | Qwen layers × 2K per gate MLP |
| 412 | 2K | Per-gate MLP parameters |
| 412 | ~65K | Gate params, Llama-3.1-8B |
| 412 | 32 | Llama layers |
| 412 | <0.001% | Fraction of base model params |
| 412 | 4.2M | LoRA adapter parameters (both archs) |
| 412 | 16 | LoRA rank |
| 414 | 6.0 h | Standard variants lower bound |
| 414 | 7.3 h | Standard variants upper bound |
| 414 | ~33% | PCGrad overhead |
| 414 | 8% | SS seed 42 overhead |
| 414 | 6.5 h | SS seed 42 time |
| 414 | 80% | SS seed 123 overhead |
| 414 | 10.8 h | SS seed 123 time |
| 416 | 32 | Gate MLP input dimension |
| 416 | 64 | Gate MLP hidden dimension |
| 416 | 1 | Gate MLP output dimension |
| 416 | <0.1% | Inference latency overhead |

---

## Section: Qualitative Steering Examples (lines 418–438)

| Line | Number | Context |
|------|--------|---------|
| 420 | 4 | 4-turn conversation |
| 421 | 3 | "exactly three bullet points" instruction |
| 424 | 4 | Table caption: 4-turn conversation |
| 428 | 0 | β=0 column header |
| 428 | 3 | β=3 column header |
| 430 | 1 | Turn 1 |
| 431 | 2 | Turn 2 |
| 432 | 3 | Turn 3 |
| 433 | 4 | Turn 4 |

---

## Section: Gradient Conflict Analysis (lines 440–464)

| Line | Number | Context |
|------|--------|---------|
| 445 | 0.5 | τ=0.5 GAR target (figure caption) |
| 451 | 79% | Layers with negative cosine similarity at epoch 0 (standard TG) |
| 451 | 68% | Layers with negative cosine similarity at epoch 2 (standard TG) |
| 451 | 0 | Epoch 0 |
| 451 | 2 | Epoch 2 |
| 451 | 79% | Conflict at epoch 0 (PCGrad) |
| 451 | 71% | Conflict at epoch 2 (PCGrad) |
| 453 | 0 | L0 (early layers) |
| 453 | 5 | L5 (early layers) |
| 453 | 24 | L24 (output-adjacent) |
| 453 | 27 | L27 (output-adjacent) |
| 453 | −0.12 | Spearman ρ between gate value and conflict magnitude |
| 453 | 0.54 | p-value for Spearman test |
| 455 | 7.5× | NTP/GAR magnitude ratio at epoch 0 |
| 455 | 14.7× | NTP/GAR magnitude ratio at epoch 2 |
| 455 | 0.93 | NTP loss convergence level |
| 455 | 7% | Max GAR contribution after PCGrad projection |
| 457 | +0.005 | Llama mean cosine similarity |
| 457 | 53% | Llama negative layers |
| 457 | 25.7× | Llama NTP dominance |
| 462 | 79% | Conflict at epoch 0 (caption, standard) |
| 462 | 68% | Conflict at epoch 2 (caption) |
| 462 | 79% | Conflict at epoch 0 (caption, PCGrad) |
| 462 | 71% | Conflict at epoch 2 (caption, PCGrad) |

---

## Section: Training Data Characteristics (lines 466–485)

| Line | Number | Context |
|------|--------|---------|
| 468 | 8,000 | Training conversations from UltraChat |
| 468 | 2,048 | Token truncation length |
| 468 | 3 | Minimum user turns (exclusion criterion) |
| 468 | 50 | N=50 primary AR evaluation |
| 468 | 3.6 | Mean user turns (primary eval) |
| 468 | 5 | N=5 long-conversation analysis |
| 468 | 10 | Turns per conversation (long-conv) |
| 478 | 8,000 | Conversations, Train (table) |
| 479 | 50 | Conversations, Eval primary (table) |
| 479 | 3 | Min user turns (table) |
| 480 | 2,048 | Max sequence length, Train (table) |
| 480 | 2,048 | Max sequence length, Eval (table) |

---

## Section: Exposure Bias Scaling (lines 487–502)

| Line | Number | Context |
|------|--------|---------|
| 491 | 7.8× | ThreadGate TF/AR gap ratio (Qwen, smallest standard variant) |
| 491 | 16.7× | PCGrad gap ratio (Qwen, largest) |
| 491 | ~1.3× | SS gap ratio (near parity) |
| 491 | ~27× | Llama gap by median |
| 491 | 28 | Qwen layers |
| 491 | 32 | Llama layers |
| 493 | 3.6 | Mean turns for N=50 |
| 493 | 8× | ThreadGate gap at 3.6 turns |
| 493 | 10 | Turn count for N=5 |
| 493 | 31× | ThreadGate gap at 10 turns |
| 493 | 20 | Extrapolated turns (hypothetical) |
| 493 | 100× | Extrapolated gap at 20 turns |
| 495 | ~1.3× | SS gap near-parity reference |
| 500 | ~1.3× | SS gap caption |
| 500 | ~27× | Llama gaps caption |
| 500 | 8× | ThreadGate gap at 3.6 turns (caption) |
| 500 | 31× | ThreadGate gap at 10 turns (caption) |

---

## Section: Per-Turn AR GAR Dynamics (lines 504–524)

| Line | Number | Context |
|------|--------|---------|
| 506 | 6 | Number of Qwen-2.5-7B training configurations |
| 506 | 1 | Turn start |
| 506 | 5 | Turn end |
| 508 | 0.423 | SS mid-turn AR GAR |
| 508 | 0.064 | ThreadGate mid-turn AR GAR |
| 508 | 0.037 | LoRA-only mid-turn AR GAR |
| 508 | 0.033 | Uniform Gate mid-turn AR GAR |
| 508 | 0.030 | PCGrad mid-turn AR GAR |
| 508 | 0.019 | Base mid-turn AR GAR |
| 508 | 42 | Seed 42 (footnote) |
| 508 | 123 | Seed 123 (footnote) |
| 513 | 0.53 | SS GAR at turn 1 (figure caption) |
| 513 | 0.39 | SS GAR at turn 5 (figure caption) |
| 513 | 0.13 | Upper bound for remaining five variants (caption) |
| 520 | 0.423 | SS (bar chart caption) |
| 520 | 0.064 | ThreadGate (caption) |
| 520 | 0.037 | LoRA-only (caption) |
| 520 | 0.033 | Uniform Gate (caption) |
| 520 | 0.030 | PCGrad (caption) |
| 520 | 0.019 | Base (caption) |

---

## Section: Per-Head KL Divergence Analysis (lines 526–549)

| Line | Number | Context |
|------|--------|---------|
| 528 | 30 | Held-out conversations for KL analysis |
| 528 | 28 | Attention heads per layer |
| 528 | 784 | Total heads (28 heads × 28 layers) |
| 533 | 30 | 30 conversations (table caption) |
| 537 | 0.012 | Base mean ΔGAR |
| 537 | 0.016 | TG mean ΔGAR |
| 538 | 0.043 | Base mean KL |
| 538 | 0.054 | TG mean KL |
| 539 | 0.673 | Corr(TF_GAR, ΔGAR), Base |
| 539 | 0.743 | Corr(TF_GAR, ΔGAR), TG |
| 545 | 35% | TG larger mean ΔGAR vs Base |
| 545 | 0.016 | TG mean ΔGAR |
| 545 | 0.012 | Base mean ΔGAR |
| 545 | 26% | TG larger mean KL vs Base |
| 545 | 0.054 | TG mean KL |
| 545 | 0.043 | Base mean KL |
| 545 | 0.673 | r, Base TF_GAR vs ΔGAR |
| 545 | 0.743 | r, TG TF_GAR vs ΔGAR |
| 547 | 23 | L23 (output-adjacent, high KL) |
| 547 | 27 | L27 (output-adjacent) |
| 547 | 0.077 | KL > 0.077 at L23–L27 |
| 547 | 9 | L9 (elevated KL) |
| 547 | 0.068 | KL ≈ 0.068 at L9 |
| 549 | 0.061 | Spearman correlation, gate value vs per-layer KL |
| 549 | 0.757 | p-value, gate–KL Spearman |
| 549 | 22 | L22 (highest KL layers start) |
| 549 | 27 | L27 (highest KL layers end) |
| 549 | ~1.0 | Gate values at deep layers |
| 549 | 0.041 | Mean KL, lowest-gate layers |
| 549 | 0.056 | Mean KL, highest-gate layers |

---

## Section: GAR Definition Robustness (lines 551–573)

| Line | Number | Context |
|------|--------|---------|
| 552 | 4 | Four alternative token-position variants |
| 552 | 50 | N=50 held-out conversations |
| 557 | 50 | N=50 (table caption) |
| 563 | 0.015 | Base, ours (last-token) GAR |
| 563 | 0.325 | TG, ours (last-token) GAR |
| 563 | 0.458 | SS, ours (last-token) GAR |
| 564 | 0.015 | Base, all-token GAR |
| 564 | 0.025 | TG, all-token GAR |
| 564 | 0.366 | SS, all-token GAR |
| 565 | 0.022 | Base, first-token GAR |
| 565 | 0.039 | TG, first-token GAR |
| 565 | 0.412 | SS, first-token GAR |
| 566 | 0.005 | Base, goal-only GAR |
| 566 | 0.310 | TG, goal-only GAR |
| 566 | 0.444 | SS, goal-only GAR |
| 571 | 0.015 | Base last-token GAR (text reference) |
| 571 | 0.325 | TG last-token GAR (text) |
| 571 | 0.005 | Base goal-only GAR (text) |
| 571 | 0.310 | TG goal-only GAR (text) |
| 571 | 0.025 | TG all-token GAR (text) |
| 571 | 0.039 | TG first-token GAR (text) |
| 573 | 0.36 | SS threshold: all four definitions above 0.36 |

---

## Section: General Capability Preservation / MMLU (lines 575–598)

| Line | Number | Context |
|------|--------|---------|
| 577 | 6 | Six Qwen-2.5-7B variants |
| 577 | 5 | MMLU 5-shot |
| 577 | 14,042 | MMLU question count |
| 581 | 0.8 | All variants within 0.8 pp of base LoRA-only (caption) |
| 585 | 74.23% | Base (LoRA-only) MMLU accuracy |
| 586 | 73.86% | PCGrad MMLU accuracy |
| 586 | −0.38 | PCGrad Δ vs Base |
| 587 | 73.75% | SS MMLU accuracy |
| 587 | −0.48 | SS Δ vs Base |
| 588 | 73.57% | LoRA-only MMLU accuracy |
| 588 | −0.66 | LoRA-only Δ vs Base |
| 589 | 73.47% | ThreadGate MMLU accuracy |
| 589 | −0.77 | ThreadGate Δ vs Base |
| 590 | 73.46% | Uniform Gate MMLU accuracy |
| 590 | −0.78 | Uniform Gate Δ vs Base |
| 597 | <0.8 pp | All variants degrade by less than 0.8 pp |

---

**Total unique numerical values extracted: ~370+ distinct numbers** across all sections. The complete per-layer gate table (lines 349–358) alone contributes 28 individual layer gate values (L0–L27).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b274cce7-895d-43a9-84e3-3bea5d4b7b0f",
  "isSidechain": true,
  "agentId": "a2a601b3381d36eca",
  "requestId": "req_011CbPrcbzga3uSv3VVRXCQC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3add49c0-36ea-40e6-8d31-d323c663c47c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "455e639f-633c-4bc1-b9d3-0370dc425013",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "rippling-sauteeing-micali",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L9ZorK1KyT5kqmg2z7xZpH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6788,
      "cache_read_input_tokens": 46066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6788,
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
