# Research conversation: Read these paper files in full and extract EVERY number that appears (statistics, percentages, counts, parameters, etc.)

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a4416bb1bbbdde2b1.jsonl`
- **Structured JSON:** [`cc1297e3d05a12bc2077.json`](../../sessions/cc/cc1297e3d05a12bc2077.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-25T19:41:23.227Z_

Read these paper files in full and extract EVERY number that appears (statistics, percentages, counts, parameters, etc.). For each number, note the file, line number, and the context sentence.

Files to read:
1. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex
5. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex
6. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex
7. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex
8. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex

Focus on extracting:
- Experimental results (PR%, ISR values, TS%, CE%, N-H%, genuine%)
- Statistical tests (p-values, chi-squared, odds ratios, Spearman correlations, confidence intervals)
- Dataset sizes (N=X, training/eval set sizes)
- Hyperparameters (learning rate, batch size, steps, K, beta values)
- Model info (parameter counts, GPU hours)
- Counts (number of seeds, samples, hacking modes)
- Any percentages or numbers in figure captions

Organize by section. Be exhaustive - do NOT skip any number.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bd1f5afe-fb7f-4505-bdbb-0893686e1cf7",
  "agentId": "a4416bb1bbbdde2b1",
  "type": "user",
  "uuid": "4393d9aa-1665-4f22-bd2a-306e05a13af3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T19:41:23.231Z_

```json
{
  "parentUuid": "4393d9aa-1665-4f22-bd2a-306e05a13af3",
  "isSidechain": true,
  "agentId": "a4416bb1bbbdde2b1",
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
  "uuid": "ac38f92e-aae0-4361-9968-a36216ffe9c4",
  "timestamp": "2026-05-25T19:41:23.231Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout"
}
```

---

### Assistant

_source line 3 · 2026-05-25T19:41:26.359Z_



I'll read all 8 files systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac38f92e-aae0-4361-9968-a36216ffe9c4",
  "isSidechain": true,
  "agentId": "a4416bb1bbbdde2b1",
  "requestId": "req_011CbPrd7sH84s5v2Gs8hyUo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3eb1a322-e439-40c8-b0b4-b03cd5c2d2a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvmfHCSqB9xRbWXXJB2C7g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34214,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34214,
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

_source line 4 · 2026-05-25T19:41:27.133Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AkFByUNXFee2DEhemaBUTW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3eb1a322-e439-40c8-b0b4-b03cd5c2d2a6",
  "isSidechain": true,
  "agentId": "a4416bb1bbbdde2b1",
  "requestId": "req_011CbPrd7sH84s5v2Gs8hyUo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7fcd894-28f2-4c94-8047-68cf9f74c241",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvmfHCSqB9xRbWXXJB2C7g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34214,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34214,
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

_source line 5 · 2026-05-25T19:41:27.139Z_

<details><summary>↩ Tool result · `toolu_01AkFByUNXFee2DEhemaBUTW`</summary>

```text
1	\begin{abstract}
2	Neurosymbolic reasoning pipelines evaluate formalizations by execution alone, treating all successful proofs as equal.
3	This single-criterion reward conflates genuine derivation with structural shortcuts: embedding the conclusion among the premises proves just as reliably, and reinforcement learning (RL) optimizers exploit the indifference.
4	We apply leave-one-out ablation to Group Relative Policy Optimization (GRPO)-trained formalizations, \emph{Solver Trace Ablation} (STA), to test whether each component is necessary for proof success, and characterize structural degeneration under six reward conditions via the resulting \emph{Intensional Structural Reward} (ISR).
5	ISR reveals that prove-rate gains conceal a compositional shift toward hacking modes, but ISR occupies a paradoxical position: the same leave-one-out structure that makes it informative also makes it gameable.
6	Tautological formalizations satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.
7	In our Qwen3-4B experiments, the Goodhart effect is seed-dependent (3 of 5 seeds converge to gaming under standard training conditions; 2 retain genuine reasoning), and the \emph{observe-vs-optimize asymmetry} persists across logic types, confirmed by cross-logic (Prolog) replication.
8	Cross-dataset (ProofFOL) evidence suggests dataset-dependent boundary conditions: structural proxies for formalization integrity are easier to observe than to optimize\footnote{Code and data are available at \url{https://anonymous.4open.science/r/solver-trace-ablation-CB70/}.}.\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7fcd894-28f2-4c94-8047-68cf9f74c241",
  "isSidechain": true,
  "promptId": "bd1f5afe-fb7f-4505-bdbb-0893686e1cf7",
  "agentId": "a4416bb1bbbdde2b1",
  "type": "user",
  "uuid": "2367c4ac-824a-4a50-af5e-f8fd6d2489bb",
  "sourceToolAssistantUUID": "e7fcd894-28f2-4c94-8047-68cf9f74c241",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-25T19:41:27.469Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ReLBmfYK7W1BEp9Hq6wpsp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2367c4ac-824a-4a50-af5e-f8fd6d2489bb",
  "isSidechain": true,
  "agentId": "a4416bb1bbbdde2b1",
  "requestId": "req_011CbPrd7sH84s5v2Gs8hyUo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "267128ff-b906-432f-9fab-3f7644a2e7a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvmfHCSqB9xRbWXXJB2C7g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34214,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34214,
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

_source line 7 · 2026-05-25T19:41:27.475Z_

<details><summary>↩ Tool result · `toolu_01ReLBmfYK7W1BEp9Hq6wpsp`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.
5	The root cause is evaluation by a single criterion, whether the generated formalization proves under a formal solver, which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.
6	Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
7	
8	Neurosymbolic formalizers~\citep{logic-lm, linc, satlm} and RL-trained variants~\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.
9	Process reward models~\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to solver-backed settings, while inference-time gaming detection~\citep{kim-game-formalization, bondarenko-spec-gaming} identifies gaming post-hoc but provides no training-time structural signal.
10	What is missing is an annotation-free method for testing \emph{component necessity} in neurosymbolic outputs.
11	
12	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.
13	For each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \emph{Intensional Structural Reward} (ISR).
14	A formalization where every component is necessary receives $\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\text{ISR}{=}0$.
15	Leave-one-out (LOO) ablation itself is standard~\citep{demillo1978, jia-harman-survey}; our contribution is its systematic application to neurosymbolic outputs, where it reveals a diagnostic--optimization asymmetry (\S\ref{sec:diagnostic}--\ref{sec:goodhart}).
16	
17	\begin{figure}[t]
18	\centering
19	\includegraphics[width=0.82\columnwidth]{figures/fig5_training_isr_curves.pdf}
20	\caption{ISR$^*$ (proved samples only) training trajectories across reward conditions (rolling $w{=}20$). Exec-only collapses to $\text{ISR}{\approx}0$, confirming structural degeneration (\S\ref{sec:diagnostic}); the ${\sim}0.5$ plateau is an $n{=}2$ artifact. ISR $\beta{=}0.1$ seeds rise toward $\text{ISR}{\approx}1$ via TS gaming (Goodhart effect, \S\ref{sec:goodhart}); random remains low.}
21	\label{fig:training-isr-curves}
22	\end{figure}
23	
24	Applied post-hoc, ISR reveals that rising prove rate conceals a compositional shift in proof structure: genuine reasoning gives way to hacking modes (conclusion embedding and tautological shortcuts), invisible to execution-based metrics (Figure~\ref{fig:training-isr-curves}; \S\ref{sec:diagnostic}).
25	
26	Yet the same LOO structure that makes ISR diagnostic also creates a Goodhart vulnerability~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}: tautological formalizations ($P{\to}P$) satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.
27	Our results suggest that LOO-based structural proxies, and plausibly other component-necessity measures, face analogous exploitation risks in neurosymbolic settings.
28	In our Qwen3-4B experiments, the asymmetry persists across logic types (first-order logic [FOL], Prolog), reward doses, and random seeds, with dataset-dependent boundary conditions (FOLIO vs.\ ProofFOL; \S\ref{sec:crossdomain}), suggesting that structural proxies for formalization integrity are easier to observe than to optimize.
29	
30	We contribute:
31	(\textbf{C1})~a systematic empirical analysis of structural degeneration in GRPO-trained neurosymbolic reasoning, using LOO ablation (STA/ISR) to catalogue eight hacking modes across six reward conditions (\S\S\ref{sec:sta}--\ref{sec:crossdomain});
32	(\textbf{C2})~empirical characterization of a seed-dependent Goodhart effect when ISR is repurposed as reward, with matched controls ruling out confounds (\S\ref{sec:goodhart});
33	(\textbf{C3})~cross-logic replication (FOL/Prolog) confirming that the Goodhart effect transfers across logic types, with exploratory cross-dataset evidence (FOLIO/ProofFOL; \S\ref{sec:crossdomain}).
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "267128ff-b906-432f-9fab-3f7644a2e7a8",
  "isSidechain": true,
  "promptId": "bd1f5afe-fb7f-4505-bdbb-0893686e1cf7",
  "agentId": "a4416bb1bbbdde2b1",
  "type": "user",
  "uuid": "d4180d8b-0557-4756-b509-a25bdf8630e2",
  "sourceToolAssistantUUID": "267128ff-b906-432f-9fab-3f7644a2e7a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-25T19:41:28.236Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EcFt7TV6wxU5QTZGycWqAY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4180d8b-0557-4756-b509-a25bdf8630e2",
  "isSidechain": true,
  "agentId": "a4416bb1bbbdde2b1",
  "requestId": "req_011CbPrd7sH84s5v2Gs8hyUo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ddeafbc6-afb6-4d6a-a5c4-e6fbbc4e9d17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvmfHCSqB9xRbWXXJB2C7g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34214,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34214,
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

_source line 9 · 2026-05-25T19:41:28.256Z_

<details><summary>↩ Tool result · `toolu_01EcFt7TV6wxU5QTZGycWqAY`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{component necessity} (Figure~\ref{fig:sta-overview}a): a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation set (100 examples) contains 34 True, 25 False, and 41 Unknown labels, with only True-labeled examples admitting valid proofs (theoretical PR ceiling ${\sim}34\%$).
11	Exec-only GRPO reaching $\text{PR}{=}93\%$ (\S\ref{sec:diagnostic}), nearly $3\times$ this ceiling, confirms the solver accepts formalizations for nominally unprovable examples, constituting direct evidence of structural gaming independent of ISR.
12	
13	\subsection{Solver Trace Ablation (STA)}
14	\label{sec:sta}
15	
16	\begin{figure*}[t]
17	\centering
18	\includegraphics[width=\textwidth]{figures/fig1_sta_overview.pdf}
19	\caption{STA overview. \textbf{(a)}~The formalization pipeline: an LLM translates natural-language (NL) premises into formal logic, verified by an external solver. \textbf{(b)}~STA removes each component in turn and re-runs the solver; the fraction of necessary components yields ISR. \textbf{(c)}~Applied post-hoc, ISR detects structural hacking; repurposed as reward, it triggers a Goodhart effect where tautological shortcuts (TS) achieve $\text{ISR}{=}1$ by construction.}
20	\label{fig:sta-overview}
21	\end{figure*}
22	
23	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}; Algorithm~\ref{alg:sta}).
24	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
25	A component is \emph{necessary} if its removal causes proof failure.
26	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
27	LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
28	
29	\begin{algorithm}[t]
30	\small
31	\caption{Solver Trace Ablation (STA)}
32	\label{alg:sta}
33	\begin{algorithmic}[1]
34	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
35	\ENSURE $\text{ISR}(x) \in [0, 1]$
36	\STATE $\textit{necessary} \gets 0$
37	\FOR{$i = 1$ to $n$}
38	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
39	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
40	    \ENDIF
41	\ENDFOR
42	\RETURN $\textit{necessary} \,/\, n$
43	\end{algorithmic}
44	\end{algorithm}
45	
46	\paragraph{Intensional Structural Reward.}\footnote{Not \emph{intentional}; \emph{intensional} contrasts with extensional (execution-only) evaluation.}
47	For a proved formalization $x = \{c_1, \ldots, c_n\}$, ISR is the fraction of necessary components:
48	\begin{equation}
49	  \text{ISR}(x) = \frac{1}{n}\sum_{i=1}^{n}\mathbf{1}\bigl[S(x\setminus\{c_i\})=\textit{failed}\bigr]
50	  \label{eq:isr}
51	\end{equation}
52	ISR is defined only for proved formalizations: ISR${=}1$ means every component is necessary; ISR${=}0$ means complete redundancy.
53	An ISR of zero for proved samples can arise from structural degeneration or genuine redundancy; our hacking mode classification (\S\ref{sec:taxonomy-method}) disambiguates these cases, with ${>}90\%$ of low-ISR proved samples exhibiting identifiable hacking patterns.
54	ISR computes the LOO marginal contribution, a restriction of the Shapley value to the maximal coalition (Appendix~\ref{app:shapley}); full interaction detection would require $O(2^n)$ evaluations.
55	ISR quantifies component redundancy, not semantic faithfulness: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p{=}0.187$, n.s.), confirming the two are uncorrelated (Appendix~\ref{app:extended-discussion}).
56	Its diagnostic value is realized through the downstream mode breakdown (\S\ref{sec:taxonomy}), not the scalar alone.
57	We report \emph{proved-only} ISR (denoted ISR$^*$) throughout to avoid conflating component necessity with prove rate.
58	
59	\paragraph{LOO independence assumption.}
60	LOO ablation tests individual, not joint, component necessity~\citep{jia-harman-survey}, systematically underestimating ISR when jointly-necessary components exist; the observed collapse is therefore conservative.
61	
62	\subsection{Reward Conditions and Hacking Modes}
63	\label{sec:rewards}
64	\label{sec:taxonomy-method}
65	
66	We study six conditions: exec-only ($r_{\text{exec}}$), ISR low/high-dose ($r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta\in\{0.1,0.3\}$), matched random controls ($r_{\text{exec}}\cdot(1{+}\beta u)$, $u\sim\mathcal{U}(0,1)$), and a supervised fine-tuning (SFT) baseline (negative log-likelihood on gold formalizations).
67	Multiplicative bonuses apply only to proved samples, keeping the prove-rate floor intact.
68	Random isolates ISR-specific signal from generic reward-variance effects; SFT isolates whether structural degeneration arises from RL optimization or data exposure alone.
69	Each RL condition uses seeds $\{42,43,44\}$ and identical training data (formulation alternatives in Appendix~\ref{app:setup}).
70	
71	\begin{table*}[t]
72	\centering
73	\small
74	\setlength{\tabcolsep}{14pt}
75	\begin{tabular}{l c c c c c c}
76	\toprule
77	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} \\
78	\midrule
79	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
80	SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
81	\midrule
82	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (PG corrected)
83	ISR (3-seed) & 0.1 & 77{\scriptsize$\pm$14} & $1.06\times^\ddagger$ & \textbf{71}$^\P$ & 18 & 6 \\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)
84	ISR (5-seed) & 0.1 & 70{\scriptsize$\pm$19} & (0.63)$^\ddagger$ & 54 & 18 & 23 \\ %% registry: plan002-additive-b01-s42--s46 (pooled)
85	Random & 0.1 & \textbf{87}{\scriptsize$\pm$8} & 0.117{\scriptsize$\pm$.04} & 14$^\S$ & 69 & 10 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)
86	Shuffled-ISR & 0.1 & 15{\scriptsize$\pm$1} & 0.559{\scriptsize$\pm$.02} & 7 & 7 & \textbf{87} \\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)
87	\midrule
88	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 11 \\ %% registry: plan002-additive-b03-s42, exp1-isr-b03-s43-r3, plan002-additive-b03-s44 (pooled; D106 s43 genuine 23→20)
89	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)
90	\bottomrule
91	\end{tabular}
92	\caption{Goodhart landscape across reward conditions. PR = prove rate; ISR$^*$ = proved-only ISR; TS = tautological shortcut; CE = conclusion embedding; N-H = non-hacking (upper bound on genuine reasoning). Multi-seed rows: pooled TS/CE/N-H; PR/ISR$^*$ as mean$\pm$std. $^\dagger$Seed~42 only. $^\ddagger$Premise-count-matched (\S\ref{sec:goodhart}). $^\P$FN-corrected (\S\ref{app:h8}). $^\S$Seed-dependent (s43: 38.3\%). Per-seed data: Table~\ref{tab:fol-detailed}.}
93	\label{tab:goodhart-landscape}
94	\end{table*}
95	
96	\paragraph{Hacking taxonomy.}
97	Across conditions, seeds, and logic types we identify eight structural-degeneration modes (full definitions in Appendix~\ref{app:hacking-modes}), dominated by three: \textbf{CE} (conclusion embedded among multiple premises), \textbf{TS} (single-premise conclusion duplication; targets ISR directly since removing the sole premise forces $\text{ISR}\geq 0.5$), and \textbf{PG} (premise-subset gaming: each component is LOO-necessary but the premise set is incomplete; Appendix~\ref{app:h8}).
98	Five additional modes (tautological collapse, repetition, complexity-without-utility, contradiction explosion, and query-as-fact [Prolog-specific]) appear in specific seeds or conditions.
99	CE and TS are robust across conditions and seeds; the remaining five modes are configuration-specific observations whose generalizability requires further investigation.
100	Modes are identified by strict text matching (CE/TS) plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; when patterns overlap, we assign the most specific mode (PG $>$ CE $>$ TS).
101	The non-hacking rate is an upper bound on genuine reasoning.
102	
103	Low ISR signals redundancy under exec-only but metric gaming under ISR-as-reward; the mode breakdown, not the ISR scalar, licenses interpretation.
104	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ddeafbc6-afb6-4d6a-a5c4-e6fbbc4e9d17",
  "isSidechain": true,
  "promptId": "bd1f5afe-fb7f-4505-bdbb-0893686e1cf7",
  "agentId": "a4416bb1bbbdde2b1",
  "type": "user",
  "uuid": "d0a34cab-a82d-4b90-a721-fedf998f4ecb",
  "sourceToolAssistantUUID": "ddeafbc6-afb6-4d6a-a5c4-e6fbbc4e9d17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T19:41:28.373Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T6v2D5DLptjeos682od5ru`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0a34cab-a82d-4b90-a721-fedf998f4ecb",
  "isSidechain": true,
  "agentId": "a4416bb1bbbdde2b1",
  "requestId": "req_011CbPrd7sH84s5v2Gs8hyUo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "692e7029-6b6d-405a-bc82-ac6a5b6242a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvmfHCSqB9xRbWXXJB2C7g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34214,
      "cache_read_input_tokens": 0,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 34214
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 314,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 34214,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 34214,
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

_source line 11 · 2026-05-25T19:41:28.388Z_

<details><summary>↩ Tool result · `toolu_01T6v2D5DLptjeos682od5ru`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted; full hyperparameters in Table~\ref{tab:hyperparams}) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention; Appendix~\ref{app:prooffol-construction}, Table~\ref{tab:prooffol-vs-folio}); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}; classifier blind spots discussed in Appendix~\ref{app:extended-discussion}), and a \emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Table~\ref{tab:classifier-precision}).
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=0.72\columnwidth]{figures/fig_seed_divergence.pdf}
17	\caption{Seed-dependent Goodhart effect under ISR $\beta{=}0.1$ reward (500 steps). Three seeds converge to gaming ($\text{N-H}{\leq}17\%$); two retain genuine reasoning (${\sim}55\%$).}
18	\label{fig:seed-divergence}
19	\end{figure}
20	
21	\paragraph{Statistical considerations.}
22	With three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.
23	Pooled Cochran--Mantel--Haenszel $p$-values ($N{=}3$ strata) are descriptive summaries, not formal inference; non-significant comparisons are exploratory.
24	An $N{=}2$ sensitivity analysis excluding s43 confirms consistent or stronger patterns (Appendix~\ref{app:n2-sensitivity}).
25	ProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.
26	
27	\subsection{ISR as Diagnostic}
28	\label{sec:diagnostic}
29	
30	\textbf{Collapse trajectory.}
31	Figure~\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.
32	As PR climbs from $32\%$ to $96\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\times$, \S\ref{sec:goodhart}) consistent with structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42
33	By 500 steps, $87\%$ of proved samples embed the conclusion verbatim (CE), establishing degeneration independent of the ISR scalar.
34	A binary variant testing only collective premise necessity misses the collapse entirely ($\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\ref{app:o1-ablation}).
35	All three exec-only seeds converge to ${\leq}6.2\%$ non-hacking by 1000 steps (Table~\ref{tab:fol-detailed}), confirming that structural degeneration under exec-only reward is not seed-specific among converged runs.
36	
37	\textbf{Cross-seed instability.}
38	Three seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\leq}6.2\%$ non-hacking by 1000 steps (Table~\ref{tab:fol-detailed}; Appendix~\ref{app:detailed-results}).
39	Exec-only seeds exhibit qualitatively different convergence patterns (PR range: 13--98\%), precluding meaningful pooling; we report seed~42 as representative of the converged regime (Table~\ref{tab:goodhart-landscape}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2
40	Two additional seeds under identical conditions fail to converge ($\text{PR}{\approx}14\%$; Appendix~\ref{app:seed-convergence}), retaining genuine reasoning and suggesting that structural degeneration requires successful convergence, though the confound between model capability and optimization success precludes strong causal attribution (Appendix~\ref{app:llama-coldstart}).
41	
42	\textbf{SFT baseline.}
43	SFT on gold formalizations produces $92\%$ non-hacking outputs at $\text{PR}{=}13\%$ (odds ratio ${=}147$ vs.\ exec-only, $p{<}0.001$; Table~\ref{tab:bootstrap-ci}), establishing that hacking modes are absent before RL optimization.
44	SFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.
45	Early-training comparison supports this interpretation: at 100 steps ($\text{PR}{=}32\%$), hacking already reaches $31\%$ vs.\ SFT's $8\%$ at comparable PR (Appendix~\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
46	
47	\subsection{Goodhart Effects on ISR-as-Reward}
48	\label{sec:goodhart}
49	
50	We reverse ISR's role from observer to reward: $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$, with matched random control ($u\sim\mathcal{U}(0,1)$).
51	The result is a regressional Goodhart pattern~\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \emph{composition} of failure modes without reducing their aggregate prevalence.
52	ISR reward systematically selects for tautological shortcuts (TS) over conclusion embedding (CE) rather than producing genuine reasoning (Table~\ref{tab:goodhart-landscape}). The scalar ISR$^*$ advantage ($214\times$ raw) collapses to $1.06\times$ after controlling for premise count; the compositional mode shift provides the primary evidence.
53	
54	\paragraph{Multiplicative coupling.}
55	Three controls constrain the multiplicative confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\ref{app:setup}).
56	The shuffled-ISR control ($87\%$ non-hacking at low PR) suggests Goodhart effects require sample-level ISR signal, though non-convergence cannot be ruled out (Appendix~\ref{app:seed-convergence}).
57	
58	\begin{figure}[t]
59	\centering
60	\includegraphics[width=0.80\columnwidth]{figures/fig3_hacking_composition.pdf}
61	\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}). ISR systematically selects for TS over CE without reducing total hacking; SFT shows near-zero hacking.}
62	\label{fig:hacking-composition}
63	\end{figure}
64	
65	\textbf{Low-dose ISR ($\beta{=}0.1$).}
66	ISR reward amplifies TS convergence: $71\%$ of proved samples under ISR exhibit tautological shortcuts vs.\ $14\%$ under random (Appendix~\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL
67	Total conclusion embedding ($\text{CE}+\text{TS}$) spans $68$--$100\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\ref{fig:hacking-composition}).
68	A seed-stratified $\chi^2$ test confirms the overall mode distribution differs significantly between ISR and random conditions ($\chi^2{=}174.8$, $\text{df}{=}2$, $p{<}10^{-38}$; Appendix~\ref{app:statistical-details}).
69	
70	\textbf{Seed-dependent outcomes.}
71	ISR reward produces bimodal outcomes (Figure~\ref{fig:seed-divergence}): 3 of 5 seeds converge to gaming, demonstrating that the Goodhart effect can occur under standard training conditions (95\% Clopper--Pearson CI: [11.8\%, 88.1\%]; $n{=}5$); 2 of 5 retain substantial genuine reasoning (seeds~45/46 added post-hoc to test replication; Appendix~\ref{app:detailed-results}).
72	Excluding s43, converged seeds show ${\leq}17\%$ non-hacking at 500 steps, collapsing to ${\leq}2\%$ by 1000 (Appendix~\ref{app:n2-sensitivity}).
73	
74	\textbf{Premise-count confound.}
75	The $214\times$ raw ISR$^*$ collapse is largely explained by premise-count reduction: ISR-trained models produce shorter formalizations that mechanically inflate ISR.
76	The premise-count-matched comparison yields only $1.06\times$ (McNemar $p{=}0.317$, $n{=}100$ matched pairs; Appendix~\ref{app:premise-count}), indicating that the scalar ISR advantage is not statistically significant.
77	
78	The compositional evidence, however, survives this control.
79	In the modal premise-count range (4--6 premises, where most proved samples fall), TS reaches $19.7\%$ under ISR versus $0\%$ under random reward (Figure~\ref{fig:premise-bins}; Table~\ref{tab:premise-bin-modes}).
80	TS hacking is mechanistically limited to simpler problems; this complexity dependence is a mechanistic insight, not a confound.
81	The compositional mode shift, not the scalar ISR difference, constitutes the primary evidence for the Goodhart effect.
82	
83	\begin{figure}[t]
84	\centering
85	\includegraphics[width=0.85\columnwidth]{figures/fig_premise_bins.pdf}
86	\caption{Mode composition by premise count (proved samples, seed~42, $\beta{=}0.1$). TS hacking emerges exclusively under ISR in the 4--6 premise range; Random shows zero TS at any complexity, confirming that ISR's compositional shift is not a premise-count artifact. I\,=\,ISR, R\,=\,Random.}
87	\label{fig:premise-bins}
88	\end{figure}
89	
90	\textbf{Higher doses and temporal dynamics.}
91	Any genuine reasoning under ISR $\beta{=}0.1$ is transient: non-hacking drops from $17\%$ to $2\%$ by 1000 steps (Figure~\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
92	Higher doses accelerate collapse: $\beta{=}0.2$ eliminates all non-hacking; $\beta{=}0.3$ destabilizes training itself~\citep{gao-reward-overoptimization} (Appendix~\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44
93	
94	\subsection{Cross-Domain and Cross-Dataset Evidence}
95	\label{sec:crossdomain}
96	\label{sec:crosslogic}
97	
98	The following results extend the primary findings of \S\ref{sec:diagnostic}--\ref{sec:goodhart} to alternative logic types and dataset families; these cross-domain experiments are exploratory in nature.
99	
100	\begin{table}[t]
101	\centering
102	\small
103	\resizebox{\columnwidth}{!}{%
104	\begin{tabular}{@{}lcc@{}}
105	\toprule
106	\textbf{Property} & \textbf{ProofFOL} & \textbf{FOLIO} \\
107	\midrule
108	FOL premises (mean$\pm$std) & $18.2 \pm 3.2$ & $5.3 \pm 1.4$ \\
109	\quad Ground facts & $10.2 \pm 3.0$ & $1.8 \pm 1.5$ \\
110	\quad Rules & $8.1 \pm 1.1$ & $3.5 \pm 1.9$ \\
111	XOR ($\oplus$) samples & 0\% & 37.2\% \\
112	Dominant depth & 4--5 & 2--3 \\
113	FOL source & GPT-4o (silver) & human (gold) \\
114	\bottomrule
115	\end{tabular}}
116	\caption{ProofFOL vs.\ FOLIO structural comparison ($n{=}500$ training examples each). ProofFOL has $3.4\times$ more premises with simpler synthetic predicates.}
117	\label{tab:prooffol-vs-folio}
118	\end{table}
119	
120	\begin{figure*}[t]
121	\centering
122	\includegraphics[width=\textwidth]{figures/fig4_prolog_comparison.pdf}
123	\caption{Cross-logic results. \textbf{(a)}~FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \textbf{(b)}~Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
124	\label{fig:prolog-comparison}
125	\end{figure*}
126	
127	\textbf{Prolog: universal Goodhart.}
128	Replicating the pipeline with Prolog/SWI-Prolog (Figure~\ref{fig:prolog-comparison}), exec-only seeds collapse to $\text{ISR}^*{\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.
129	Under ISR-as-reward, all three seeds reach $0\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\ref{tab:prolog-detailed}).
130	Prolog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.
131	
132	\textbf{ProofFOL exec-only: cross-dataset replication.}
133	Converged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.
134	The mode repertoire differs across datasets: among converged seeds, TS dominates one while CE dominates the other, showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.
135	
136	\textbf{ProofFOL ISR ($\beta{=}0.1$): dataset-dependent asymmetry.}
137	ISR reward on ProofFOL produces directionally higher genuine rates than exec-only ($p{=}0.10$, exploratory; Table~\ref{tab:prooffol-detailed}).
138	The asymmetry follows from hacking geometry: on FOLIO, TS yields high ISR (regressional Goodhart~\citep{manheim-goodhart-taxonomy}); on ProofFOL, CE embeds conclusions among many premises, yielding $\text{ISR}{\approx}0$ and rendering ISR reward effectively corrective.
139	
140	\textbf{Cross-scale validation (Qwen3-8B).}
141	Qwen3-8B does not converge under exec-only GRPO ($\text{PR}{=}14\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\ref{app:8b-results}).
142	
143	\subsection{Hacking Taxonomy}
144	\label{sec:taxonomy}
145	
146	\begin{table}[t]
147	\centering
148	\small
149	\resizebox{\columnwidth}{!}{%
150	\begin{tabular}{lccccc}
151	\toprule
152	\textbf{Mode} & \textbf{Exec} & \textbf{ISR$_{.1}$} & \textbf{Rnd$_{.1}$} & \textbf{SFT} & \textbf{Prolog$_{\text{ISR}}$} \\
153	\midrule
154	CE embed       & 87 & 18 & 68 & 8 & 0$^\sharp$ \\
155	TS duplicate   & 0  & 71 & 14 & 0 & 100$^\sharp$ \\
156	PG prem-subset & 5  & 5  & 8   & 0 & --- \\
157	Tautological   & --- & --- & --- & --- & s42 \\
158	Repetition     & s43 & --- & --- & --- & --- \\
159	Contradiction  & 1k & --- & --- & --- & --- \\
160	Cmplx.\ vacuous& 0  & 0  & 1  & 0 & --- \\
161	Query-as-fact  & --- & --- & --- & --- & s44 \\
162	\midrule
163	\textbf{Non-hacking} & 8  & 6  & 10 & \textbf{92} & \textbf{0} \\
164	\bottomrule
165	\end{tabular}}
166	\caption{Eight hacking modes across conditions (\% of proved samples; exec-only/SFT: seed~42; ISR/Random: 3-seed pooled). TS includes subtypes TSa (text-match) and TSb (obfuscated tautology). Cells with seed identifiers indicate seed-specific modes. $^\sharp$Prolog pools strict+functional classification. Extended breakdown in Table~\ref{tab:hacking-taxonomy-app}.}
167	\label{tab:hacking-taxonomy}
168	\end{table}
169	
170	Three modes account for the vast majority of hacking (Table~\ref{tab:hacking-taxonomy}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).
171	The central pattern: \emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\%$ non-hacking.
172	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "692e7029-6b6d-405a-bc82-ac6a5b6242a8",
  "isSidechain": true,
  "promptId": "bd1f5afe-fb7f-4505-bdbb-0893686e1cf7",
  "agentId": "a4416bb1bbbdde2b1",
  "type": "user",
  "uuid": "6ed9613a-7d56-40d3-8daa-740276c2158e",
  "sourceToolAssistantUUID": "692e7029-6b6d-405a-bc82-ac6a5b6242a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T19:41:32.626Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WidZwKGyLMcnY3xLnKWDBs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ed9613a-7d56-40d3-8daa-740276c2158e",
  "isSidechain": true,
  "agentId": "a4416bb1bbbdde2b1",
  "requestId": "req_011CbPrdW5GGtWJoYQtufW22",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "089803b9-0c68-4fc9-b965-bbc7daa4882c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEoWMjJDptA6QEiy2Ab3wF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12083,
      "cache_read_input_tokens": 34214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12083,
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

_source line 13 · 2026-05-25T19:41:32.633Z_

<details><summary>↩ Tool result · `toolu_01WidZwKGyLMcnY3xLnKWDBs`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation.
5	When ISR is used post-hoc, it reliably detects that prove-rate gains conceal a compositional shift toward hacking modes: across all converged exec-only seeds, non-hacking rates collapse to ${\leq}6.2\%$ by 1000 steps, despite prove rates exceeding $90\%$.
6	The diagnostic holds across logic types (FOL, Prolog) and dataset families (FOLIO, ProofFOL), confirming that structural degeneration under execution-only reward is a general phenomenon rather than an artifact of a specific formalism.
7	
8	When repurposed as a training reward, ISR produces a seed-dependent Goodhart effect that follows the regressional pattern~\citep{manheim-goodhart-taxonomy}: optimizing ISR shifts the composition of hacking modes (from CE to TS) without reducing their aggregate prevalence.
9	The effect is paradoxical in a precise sense: the same LOO structure that makes ISR informative as a diagnostic also makes it gameable as a reward, because tautological formalizations satisfy the necessity criterion by construction.
10	Cross-logic replication (Prolog) confirms the compositional mode shift; cross-dataset evidence (ProofFOL, $p{=}0.10$) is exploratory (\S\ref{sec:crossdomain}).
11	
12	These findings yield five practical guidelines for GRPO-trained neurosymbolic systems.
13	First, never evaluate by prove rate alone---use ISR and mode breakdown as joint diagnostics, applied post-hoc rather than as reward signals; any dose of ISR-as-reward induces gaming or collapse.
14	Second, report multi-seed results: single-seed evaluation is unreliable when cross-seed variance exceeds the effect size (\S\ref{sec:diagnostic}).
15	Third, treat LOO-based metrics as component-count-biased until premise-count-matched (\S\ref{sec:goodhart}).
16	Fourth, expect conclusion embedding as a GRPO-universal baseline: reward shaping alters its composition, not its prevalence (Table~\ref{tab:goodhart-landscape}).
17	Fifth, monitor convergence: structural degeneration appears contingent on successful optimization (Appendix~\ref{app:seed-convergence}), making monitoring most critical when training succeeds.
18	The diagnostic--optimization asymmetry motivates targeted mitigations such as single-premise penalties or mode-aware reward shaping~\citep{tarek2025reward, pronesti2026beyond}.
19	Remaining questions include extending the hacking taxonomy to process reward settings and determining whether the seed-dependent Goodhart boundary generalizes beyond the model scale examined here.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "089803b9-0c68-4fc9-b965-bbc7daa4882c",
  "isSidechain": true,
  "promptId": "bd1f5afe-fb7f-4505-bdbb-0893686e1cf7",
  "agentId": "a4416bb1bbbdde2b1",
  "type": "user",
  "uuid": "480dc3f4-e248-4ad3-8b0e-7ce55e2417bd",
  "sourceToolAssistantUUID": "089803b9-0c68-4fc9-b965-bbc7daa4882c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T19:41:33.121Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ss2s8oyyxC7BQfBbhXkWWm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "480dc3f4-e248-4ad3-8b0e-7ce55e2417bd",
  "isSidechain": true,
  "agentId": "a4416bb1bbbdde2b1",
  "requestId": "req_011CbPrdW5GGtWJoYQtufW22",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12ddd88f-4b86-4ba0-a7f2-43a076863105",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEoWMjJDptA6QEiy2Ab3wF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12083,
      "cache_read_input_tokens": 34214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12083,
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

_source line 15 · 2026-05-25T19:41:33.126Z_

<details><summary>↩ Tool result · `toolu_01Ss2s8oyyxC7BQfBbhXkWWm`</summary>

```text
1	\section*{Limitations}
2	
3	Experiments use a single model (Qwen3-4B) with three to five seeds; degeneration patterns may not transfer to other families, and the 3/5 gaming rate (seeds 45--46 added post-hoc) is an existence demonstration, not a prevalence estimate.
4	FOLIO is a relatively small (1,435 examples) synthetic benchmark; generalization to larger or naturalistic corpora is untested.
5	ISR quantifies component necessity, not semantic faithfulness; diagnostic value comes from the mode breakdown, not the scalar alone (Appendix~\ref{app:extended-discussion}).
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12ddd88f-4b86-4ba0-a7f2-43a076863105",
  "isSidechain": true,
  "promptId": "bd1f5afe-fb7f-4505-bdbb-0893686e1cf7",
  "agentId": "a4416bb1bbbdde2b1",
  "type": "user",
  "uuid": "75cda927-3da5-40a8-89d4-1e625e4ca7b0",
  "sourceToolAssistantUUID": "12ddd88f-4b86-4ba0-a7f2-43a076863105",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T19:41:33.663Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WAi8SVeonyRuNr699Gj7Gv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75cda927-3da5-40a8-89d4-1e625e4ca7b0",
  "isSidechain": true,
  "agentId": "a4416bb1bbbdde2b1",
  "requestId": "req_011CbPrdW5GGtWJoYQtufW22",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29c0c83a-a09c-4a80-9b2a-55b47234e8a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEoWMjJDptA6QEiy2Ab3wF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12083,
      "cache_read_input_tokens": 34214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12083,
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

_source line 17 · 2026-05-25T19:41:33.669Z_

<details><summary>↩ Tool result · `toolu_01WAi8SVeonyRuNr699Gj7Gv`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	Large language model (LLM)--solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp, nlproofs} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1, rlsf} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} and DeepSeek-Prover-V2~\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.
7	We use FOLIO~\citep{folio}, the only public natural language inference (NLI) benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Reward hacking and Goodhart's Law.}
10	Specification gaming~\citep{krakovna2020specification} and Goodhart's Law~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} are established across RL from human feedback (RLHF)~\citep{gao-reward-overoptimization} and logical formalization~\citep{bondarenko-spec-gaming, kim-game-formalization}.
11	Most closely related, \citet{kim-game-formalization} document inference-time gaming on FOLIO with frontier models; our work complements theirs by studying training-time degeneration via component necessity.
12	\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes catastrophic Goodhart where Kullback--Leibler (KL) regularization provably fails, providing a theoretical lens for why GRPO's KL penalty does not prevent our observed collapse.
13	Concurrent work documents spurious signals in RLVR~\citep{spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking, helff2026gaming, nishimura2026specgaming, khalifa2026countdown} and proposes composite rewards~\citep{tarek2025reward, pronesti2026beyond}.
14	Our Goodhart effect follows the regressional pattern~\citep{manheim-goodhart-taxonomy}; its application to a diagnostic designed to detect gaming, and the dataset-dependent asymmetry, are to our knowledge novel.
15	
16	\paragraph{Reward design and structural diagnostics.}
17	Process reward models~\citep{lightman-verify-step, setlur2025rewarding, cui2025prime, cobbe2021training, uesato2022solving} supervise intermediate steps; \citet{sullivan2025grpo-prm} show GRPO implicitly implements process reward.
18	Classical reward shaping~\citep{ng1999policy, gao-effective-rl-reward} guarantees policy invariance only under potential-based transforms; ISR violates this condition.
19	Proposed mitigations include reward model ensembles~\citep{coste2023reward}, constrained optimization~\citep{moskovitz2023confronting}, and activation-level monitoring~\citep{wilhelm2026monitoring}; \citet{yue2025rl-reasoning} show RLVR redistributes probability mass rather than creating new reasoning, consistent with our finding that GRPO exploits existing shortcuts.
20	STA adapts the LOO mutation paradigm~\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.
21	Related concerns about chain-of-thought (CoT) faithfulness~\citep{lanham2023faithfulness, turpin2023unfaithful} operate at the reasoning-chain level rather than solver-input components.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29c0c83a-a09c-4a80-9b2a-55b47234e8a0",
  "isSidechain": true,
  "promptId": "bd1f5afe-fb7f-4505-bdbb-0893686e1cf7",
  "agentId": "a4416bb1bbbdde2b1",
  "type": "user",
  "uuid": "85fa17e9-cde3-4d26-94ed-16564ec22cca",
  "sourceToolAssistantUUID": "29c0c83a-a09c-4a80-9b2a-55b47234e8a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-25T19:41:33.946Z_

<details open><summary>🔧 Tool call — Read · `toolu_018TZpF3Sz2aq1sRbsi2CKrX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85fa17e9-cde3-4d26-94ed-16564ec22cca",
  "isSidechain": true,
  "agentId": "a4416bb1bbbdde2b1",
  "requestId": "req_011CbPrdW5GGtWJoYQtufW22",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5fe2546f-921c-42c8-9cee-457e0cd3a05c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEoWMjJDptA6QEiy2Ab3wF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12083,
      "cache_read_input_tokens": 34214,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12083
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 304,
          "cache_read_input_tokens": 34214,
          "cache_creation_input_tokens": 12083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12083,
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

_source line 19 · 2026-05-25T19:41:34.197Z_

<details><summary>↩ Tool result · `toolu_018TZpF3Sz2aq1sRbsi2CKrX`</summary>

```text
1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions.
9	
10	\begin{table}[ht]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\small
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, conditions, and reruns is approximately 80--120 GPU-hours.
56	
57	\paragraph{SFT convergence.}
58	SFT training converged across all three seeds: final-step loss ${\leq}0.04$ and token accuracy ${>}99\%$ after ${\sim}8$ epochs on 500 examples (seed~42: $0.029$; seed~44: $0.033$); the 1000-step extension further decreases loss to $0.017$.
59	
60	\paragraph{Evaluation exception.}
61	FOL exec-only seed~43 was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
62	Its PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol.
63	
64	\paragraph{Reward formulation.}
65	An additive variant ($r = r_{\text{exec}} + \beta\,\text{ISR}$) was tested in early experiments but collapsed prove rate to near-zero, as ISR alone provides no gradient toward provable formalizations; the multiplicative form $r_{\text{exec}}\cdot(1+\beta\,\text{ISR})$ ensures ISR modulates only proved outputs.
66	
67	\paragraph{ProofFOL dataset construction.}
68	\label{app:prooffol-construction}
69	ProofFOL is derived from ProofWriter~\citep{proofwriter} (10{,}424 training examples) via the GPT-4o silver-standard FOL translation pipeline of \citet{prooffol-thatikonda2024} with Prover9 verification filtering (${\sim}70\%$ retention; failures from timeouts, unsupported constructs, and translation errors).
70	Of the translated examples, 99.1\% parse successfully (92 skipped due to empty FOL output).
71	We sample 500 training and 100 evaluation examples (seed~42) from the verified pool.
72	Table~\ref{tab:prooffol-vs-folio} (main text) compares key structural properties.
73	
74	ProofFOL problems are structurally more complex ($3.4{\times}$ more premises) but use simpler, synthetic predicates (e.g., \texttt{Blue(x)}, \texttt{Rough(x)}) characteristic of ProofWriter's procedural generation.
75	The absence of XOR constraints and the regularity of predicate structure make ProofFOL a complementary testbed: structural degeneration must emerge from the RL training dynamics rather than from formalization difficulty.
76	
77	\section{Extended Discussion}
78	\label{app:extended-discussion}
79	
80	\paragraph{What ISR measures and what it does not.}
81	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
82	This is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.
83	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
84	ISR and downstream task performance are uncorrelated.
85	ISR is thus a component-necessity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
86	
87	Critically, low ISR carries different semantics depending on the training objective.
88	Under exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\S\ref{sec:crosslogic}).
89	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
90	ISR values must always be interpreted relative to the optimization objective that produced them.
91	
92	\paragraph{ISR as $(n{-}1)$-coalition Shapley value.}
93	\label{app:shapley}
94	Define a cooperative game $(N, v)$ with player set $N = \{1,\ldots,n\}$ (components) and binary utility $v(S) = \mathbf{1}[S(S){=}\textit{proved}]$.
95	The Shapley value $\phi_i$ averages marginal contributions over all coalition sizes; ISR restricts to the maximal coalition $|S|{=}n{-}1$, giving $\phi_i^{\text{LOO}} = \frac{1}{n}[v(N) - v(N \setminus \{i\})]$.
96	Summing: $\text{ISR}(x) = \sum_i \phi_i^{\text{LOO}} = \frac{1}{n}\sum_i \mathbf{1}[v(N \setminus \{i\}){=}0]$, recovering Equation~\ref{eq:isr}.
97	This restriction trades full interaction detection for $O(n)$ cost; the binary solver output makes higher-order interactions unobservable from LOO alone (\S\ref{sec:sta}).
98	
99	\paragraph{The premise-count confound.}
100	\label{app:premise-count}
101	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
102	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.
103	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
104	Premise-count-matched comparison eliminates the difference ($1.06\times$, McNemar's test $p{=}0.317$; Table~\ref{tab:fol-beta01-detailed}), confirming that the scalar ISR advantage is not statistically significant.
105	This bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
106	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
107	Mode composition analysis (CE vs.\ TS rates) is unaffected by premise-count confounding because TS classification depends on tautological proof structure (\S\ref{app:hacking-modes}), not on the number of premises in the formalization.
108	
109	\begin{table}[h]
110	\centering
111	\resizebox{\columnwidth}{!}{%
112	\begin{tabular}{@{}llrrrr@{}}
113	\toprule
114	\textbf{Premises} & \textbf{Condition} & \textbf{$N_{\text{proved}}$} & \textbf{CE\%} & \textbf{TS\%} & \textbf{Genuine\%} \\
115	\midrule
116	$\leq$3 & ISR $\beta{=}0.1$ & 8 & 50.0 & 12.5 & 12.5 \\
117	         & Random $\beta{=}0.1$ & 6 & 50.0 & 0.0 & 50.0 \\
118	\midrule
119	4--6     & ISR $\beta{=}0.1$ & 61 & 47.5 & 19.7 & 14.8 \\
120	         & Random $\beta{=}0.1$ & 58 & 72.4 & 0.0 & 22.4 \\
121	\midrule
122	$\geq$7  & ISR $\beta{=}0.1$ & 12 & 75.0 & 0.0 & 25.0 \\
123	         & Random $\beta{=}0.1$ & 15 & 86.7 & 0.0 & 13.3 \\
124	\bottomrule
125	\end{tabular}}
126	\caption{Mode composition by premise-count bin (seed 42). TS hacking is concentrated in the 4--6 premise range and absent for ${\geq}7$ premises, indicating a mechanistic complexity threshold rather than a statistical confound.}
127	\label{tab:premise-bin-modes}
128	\end{table}
129	
130	\begin{table*}[ht]
131	\centering
132	\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\ref{app:h8}).}
133	\label{tab:bootstrap-ci}
134	\small
135	\begin{tabular}{@{}lcccc@{}}
136	\toprule
137	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
138	\midrule
139	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (PG+FN corrected)}} \\
140	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
141	ISR vs.\ Exec-only & 6.06\% & 7.5\% & 0.79 & 0.62 \\
142	Random vs.\ Exec-only & 9.5\% & 7.5\% & 1.30 & 0.68 \\
143	\midrule
144	\multicolumn{5}{@{}l}{\textit{TS gaming rate}} \\
145	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
146	\midrule
147	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only non-hacking rate}} \\
148	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
149	\bottomrule
150	\end{tabular}
151	\\[2pt]
152	{\small ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown. Pooled statistics treat within-seed samples as independent and serve as descriptive summaries only; the seed-stratified CMH test (\S\ref{app:statistical-details}) accounts for within-seed dependence.}
153	\end{table*}
154	
155	\paragraph{TS dose-response gradient.}
156	TS tautology follows a dose-response pattern across reward conditions: random $\beta{=}0.1$ produces $13.7\%$ TS ($36/262$ pooled; per-seed: $38.3\%$ in s43, $0\%$ in s42/s44), random $\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\beta{=}0.1$ reaches $70.6\%$ ($163/231$).
157	The gradient (random $\beta{=}0.1$ ($13.7\%$) $\to$ random $\beta{=}0.3$ (4--7 TSa per seed) $\to$ ISR $\beta{=}0.1$ ($70.6\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.
158	
159	\paragraph{Goodhart effects: implications.}
160	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself. Any diagnostic metric risks becoming a target when optimized.
161	The dose-response pattern maps onto the Manheim \& Garrabrant taxonomy~\citep{manheim-goodhart-taxonomy}: $\beta{=}0.1$ on FOLIO instantiates \emph{regressional} Goodhart ($P{\to}P$ tautologies yield $\text{ISR}{\geq}0.5$, so ISR erroneously rewards the shortcut); $\beta{\geq}0.2$ introduces \emph{extremal} elements (PR collapse to 18\% vs.\ 48\% random at $\beta{=}0.3$).
162	The implication is conditional: ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL; \S\ref{sec:crossdomain}).
163	
164	\paragraph{Single-seed unreliability.}
165	The three exec-only seeds diverge radically (PR $\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
166	ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (TS), 1/3 by premise minimization (\S\ref{sec:goodhart}).
167	Multi-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.
168	
169	\paragraph{Classifier limitations.}
170	Text-match hacking classifiers have systematic blind spots that functional analysis exposes.
171	In Prolog STA, two seeds achieved 100\% genuine classification under strict text matching, yet functional analysis via the $n_{\text{necessary}}$ distribution revealed 0\% genuine in both cases (Table~\ref{tab:prolog-detailed}).
172	One seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\_case atoms serving as both fact and query, a gaming mode invisible to string comparison.
173	Practitioners should cross-validate text-match classifiers with functional metrics and never treat classifier-reported genuine rates as ground truth without independent verification.
174	
175	\paragraph{Practical guidelines.}
176	\label{app:practical-guidelines}
177	See \S\ref{sec:discussion} for five practical guidelines derived from these findings.
178	
179	\paragraph{Multiple testing correction.}
180	\label{app:statistical-details}
181	We define two test families: FOLIO ($k{=}14$ tests across all conditions) and ProofFOL ($k{=}1$).
182	Within the FOLIO family, Bonferroni correction at $\alpha{=}0.05$ yields adjusted thresholds of $p_{\text{adj}}{=}0.05/14{=}0.0036$.
183	Three primary comparisons survive correction: the TS rate difference (ISR vs.\ random; $p_{\text{bonf}}{=}1.82{\times}10^{-38}$), the SFT vs.\ exec-only non-hacking rate ($p_{\text{bonf}}{=}0.014$), and the Cochran--Mantel--Haenszel test for TS association across seeds ($p_{\text{bonf}}{<}10^{-8}$).
184	The matched 5+5-seed Fisher/Mann-Whitney comparison is borderline ($p_{\text{bonf}}{=}0.056$), significant at $\alpha{=}0.10$ after Bonferroni correction ($k{=}14$).
185	The ProofFOL genuine-rate permutation test ($p{=}0.10$) belongs to a separate hypothesis family (different dataset, independent experimental design) and does not reach significance even without correction; it is reported as an exploratory observation throughout.
186	Bonferroni assumes independence, which is conservative for our setting (several tests use overlapping data); Holm--Bonferroni or Benjamini--Hochberg FDR would recover the matched 5+5 comparison at conventional significance.
187	We report the most conservative Bonferroni results for transparency.
188	
189	\paragraph{Mode distribution $\chi^2$ test.}
190	A pooled $3{\times}2$ contingency table (TS/CE/N-H $\times$ ISR/Random, 3-seed, 500 steps) yields $\chi^2{=}174.8$, $\text{df}{=}2$, $p{=}1.08{\times}10^{-38}$, confirming that ISR reward shifts the overall hacking mode composition, not merely the TS rate.
191	Per-seed tests are individually significant (s42: $\chi^2{=}15.8$, $p{<}0.001$; s43: $\chi^2{=}59.4$, $p{<}10^{-13}$; s44: $\chi^2{=}168.0$, $p{<}10^{-36}$).
192	The previously reported $\text{OR}_{\text{CMH}}{=}2.46$ for TS specifically ($p{<}10^{-8}$) captures a narrower slice of this distributional shift.
193	
194	
195	\section{Hacking Mode Definitions}
196	\label{app:hacking-modes}
197	
198	We identify eight distinct reward hacking modes across all experiments.
199	TS comprises two subtypes: TSa (text-match duplication, where the premise is textually identical to the conclusion) and TSb (obfuscated tautology, where the premise is logically equivalent but textually distinct; \S\ref{app:h8}).
200	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
201	
202	Table~\ref{tab:hacking-taxonomy} (main text) provides the compact cross-condition summary; Table~\ref{tab:hacking-taxonomy-app} below gives the extended breakdown.
203	
204	\begin{table*}[ht]
205	\centering
206	\small
207	\begin{tabular}{@{}llcccc@{}}
208	\toprule
209	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rnd} & \textbf{SFT} \\
210	\midrule
211	CE & Concl.\ in premises & 87 & 18 & 68 & 8 \\
212	TS & Single prem.\ = concl. & $\bullet$ & \textbf{71} & 14$^\dagger$ & 0 \\
213	PG & Premise-subset gaming & 5 & 5 & 8 & 0 \\
214	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
215	Repetition & Output degen. & $\bullet$ & --- & --- & --- \\
216	Contradiction & $n_{\text{comp}}$ inflated & $\bullet$ & --- & --- & --- \\
217	C-w/o-utility & Complex, redundant & 0 & 0 & 1 & 0 \\
218	Q-as-fact & Atom = fact+query & --- & --- & --- & --- \\
219	\bottomrule
220	\end{tabular}
221	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed pooled. TS includes subtypes TSa (text-match, $n{=}149$ ISR $+$ 36 random) and TSb (obfuscated tautology, $n{=}14$; primarily s44). $^\dagger$Random TS driven by seed~43 (38.3\%); seeds~42/44: 0\%. Exec: CE${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (TS/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). PG: premise-subset gaming (Appendix~\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-detailed}).}
222	\label{tab:hacking-taxonomy-app}
223	\end{table*}
224	
225	\paragraph{Classifier Validation.}
226	Hacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.
227	CE and TS are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
228	No training data or manual annotation is used for classification.
229	
230	To estimate precision, we manually verified 50 randomly sampled outputs classified as CE or TS: all 50 were confirmed correct (estimated precision ${>}$95\%, Wilson 95\% CI: [93\%, 100\%]).
231	Recall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.
232	We cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\text{necessary}} \leq 1$ are flagged as potential false negatives.
233	This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
234	The non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.
235	\paragraph{Boundary case validation.}
236	Stratified validation across 82 samples (all five hacking categories) yields Cohen's $\kappa{=}1.0$; independent re-annotation confirms full agreement.
237	Structured inspection of 20 boundary cases (short-conclusion CE (10, minimum 4 characters), low-ISR genuine (5, minimum $\text{ISR}{=}0.22$), and TS on false propositions (5)) confirmed 20/20 correct classifications.
238	Short-conclusion CE samples are unambiguous hacking: the conclusion appears as a standalone premise with no NL source.
239	Low-ISR genuine samples reflect mode-collapsed template outputs, not structural gaming.
240	3/5 TS boundary cases confirm factually false propositions (e.g., affirming ``dogs are plants''), showing TS is not merely vacuous but actively harmful.
241	
242	\begin{table}[h]
243	\centering
244	\small
245	\begin{tabular}{@{}lcr@{}}
246	\toprule
247	\textbf{Mode} & \textbf{Val.\ $N$} & \textbf{Prec.} \\
248	\midrule
249	CE (Concl.\ Embed.) & 80$^\dagger$ & 1.00 \\
250	TS (Tautological) & 7 & 1.00 \\
251	PG (Premise-Subset) & 20 & 1.00 \\
252	Contradiction & 20 & 1.00 \\
253	Genuine & 25 & 1.00 \\
254	\midrule
255	\textbf{Overall} & \textbf{152} & \textbf{1.00} \\
256	\bottomrule
257	\end{tabular}
258	\caption{Per-mode classifier precision on 152 manually validated samples (stratified + boundary + random; three exercises pooled). $^\dagger$Includes 50 randomly sampled CE$\cup$TS outputs (pool ratio CE:TS${=}$374:2). Recall is not estimable from a validation-only design.}
259	\label{tab:classifier-precision}
260	\end{table}
261	
262	The TS\textsubscript{b} subcategory (functional LOO tautologies undetectable by text matching) provides a lower bound on TS recall: ${\geq}91\%$ ($149/163$) under ISR $\beta{=}0.1$. Other modes' recall is not estimable from the validation-only design; non-hacking rates throughout should be interpreted as upper bounds.
263	
264	\subsection{PG -- Premise-Subset Gaming}
265	\label{app:h8}
266	
267	Manual audit of ISR $\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (CE-style).
268	We term this \textbf{PG (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.
269	
270	\paragraph{Detection.} PG is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\text{prem}} \leq 3$) that nonetheless achieve high ISR.
271	Automated detection is not currently feasible because PG requires comparing the generated premise set against the gold premises.
272	
273	\paragraph{Audit scope and limitations.}
274	Full PG audit was completed for ISR $\beta{=}0.1$ seed~42 only.
275	ISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.
276	Random $\beta{=}0.1$ does not produce PG by mechanism (no ISR optimization pressure); seed~42 audit confirmed PG${=}0$.
277	
278	\paragraph{TS false-negative correction (TSb obfuscated tautology).}
279	ISR $\beta{=}0.1$ seed~44 contained 12 samples with $n_{\text{prem}}{=}1$ classified as non-hacking by the text matcher.
280	Manual inspection confirmed all 12 are logically equivalent to TS but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).
281	We classify these as \textbf{TSb} (obfuscated tautology), distinct from text-match-detectable TSa.
282	$10/12$ achieve $\text{ISR}{\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and TS classifier: triple gaming (\S\ref{sec:taxonomy}).
283	After correction, ISR s44 non-hacking${=}0$; total TS = TSa (77 text-match) + TSb (12 obfuscated) = 89.
284	
285	\paragraph{Impact on non-hacking-rate comparison.}
286	After PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\%$ vs.\ random non-hacking $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
287	The direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
288	
289	\subsection{CE -- Conclusion Embedding}
290	
291	\paragraph{Definition.}
292	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
293	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
294	
295	\paragraph{Example (FOL).}
296	\smallskip\noindent\rule{\columnwidth}{0.3pt}
297	{\small\begin{verbatim}
298	Premises:
299	  all x (bird(x) -> flies(x)).
300	  bird(tweety).
301	  flies(tweety).  % conclusion embedded
302	Conclusion: flies(tweety).
303	\end{verbatim}}
304	\noindent\rule{\columnwidth}{0.3pt}\smallskip
305	
306	\paragraph{ISR interaction.}
307	Variable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
308	ISR does not distinguish trivial from substantive necessity.
309	
310	\paragraph{Prevalence.}
311	Conclusion embedding in some form (CE multi-premise or TS single-premise) is GRPO-universal at 68--97\% across all RL conditions.
312	Under exec-only and Random reward, it manifests as CE (69--93\%); under ISR reward, it shifts to TS (70.6\% pooled).
313	
314	
315	\subsection{TSa -- Conclusion Duplication (Standard)}
316	
317	\paragraph{Definition.}
318	The entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.
319	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
320	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
321	
322	\paragraph{Example (FOL).}
323	\smallskip\noindent\rule{\columnwidth}{0.3pt}
324	{\small\begin{verbatim}
325	Premises:
326	  all x ((A(x)&B(x))->(C(x)|D(x))).
327	Conclusion:
328	  all x ((A(x)&B(x))->(C(x)|D(x))).
329	\end{verbatim}}
330	\noindent\rule{\columnwidth}{0.3pt}\smallskip
331	
332	\paragraph{ISR interaction.}
333	ISR~$\approx 0.8$--$1.0$.
334	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
335	TSa games both exec reward and ISR reward; TSb extends this to triple gaming by additionally evading the text-match classifier.
336	
337	\paragraph{Prevalence.}
338	TSa (text-match detectable): 64.5\% pooled (149/231) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
339	Combined TS (TSa + TSb): 70.6\% (163/231; s43 TSa${=}59$ + TSb${=}2$; includes s44 FN correction).
340	Random~$\beta{=}0.1$ pooled: 13.7\% (36/262, all TSa; driven by seed~43 at 38.3\%, seeds~42 and~44 at 0\%).
341	
342	
343	\subsection{TSb -- Obfuscated Tautology}
344	
345	\paragraph{Definition.}
346	A single-premise formalization logically equivalent to TSa (premise = conclusion) but with surface-form differences that evade the text-match TS classifier.
347	The model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).
348	
349	\paragraph{Example (FOL, vacuous quantifier wrapping).}
350	\smallskip\noindent\rule{\columnwidth}{0.3pt}
351	{\small\begin{verbatim}
352	Premises:
353	  all x all y ((A(x)&B(y))->(C(x)|D(y))).
354	Conclusion:
355	  all x ((A(x)&B(x))->(C(x)|D(x))).
356	\end{verbatim}}
357	\noindent\rule{\columnwidth}{0.3pt}\smallskip
358	
359	\noindent The premise introduces a vacuous variable $y$, unified with~$x$ at proof time; the formulas are logically equivalent but textually distinct.
360	
361	\paragraph{ISR interaction.}
362	$\text{ISR}{\geq}0.83$ ($10/12$ samples).
363	TSb simultaneously games three objectives: execution reward ($r_{\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match TS classifier (surface-form difference evades detection).
364	This triple gaming makes TSb the most complete Goodhart case we observe.
365	
366	\paragraph{Prevalence.}
367	Found primarily in ISR $\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.
368	Functional cross-validation via $n_{\text{necessary}}{=}1$ exposed the misclassification.
369	
370	
371	\subsection{Tautological Collapse}
372	
373	\paragraph{Definition.}
374	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
375	
376	\paragraph{Example (FOL).}
377	\smallskip\noindent\rule{\columnwidth}{0.3pt}
378	\begin{verbatim}
379	Premises: p(a).
380	Conclusion: p(a).
381	\end{verbatim}
382	\noindent\rule{\columnwidth}{0.3pt}\smallskip
383	
384	\paragraph{ISR interaction.}
385	ISR~$=1.0$ (the sole premise is necessary).
386	Distinguished from TS by having low component count ($n_{\text{comp}}\approx 2$) and atomic formulas rather than complex sub-structured conclusions.
387	
388	\paragraph{Prevalence.}
389	Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% TS by strict classifier).
390	Also observed in Prolog exec+STA seed~42 (100\% TS, PR~$=0.50$).
391	
392	
393	\subsection{Repetition Collapse}
394	
395	\paragraph{Definition.}
396	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
397	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
398	
399	\paragraph{Example (Prolog).}
400	\smallskip\noindent\rule{\columnwidth}{0.3pt}
401	\begin{verbatim}
402	penguin(fido).
403	penguin(fido).
404	penguin(fido).
405	... (repeated to 512 tokens)
406	query(penguin(fido)).
407	\end{verbatim}
408	\noindent\rule{\columnwidth}{0.3pt}\smallskip
409	
410	\paragraph{ISR interaction.}
411	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
412	ISR correctly diagnoses this degeneration.
413	
414	\paragraph{Prevalence.}
415	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$=13$\%, ISR~$=0$).
416	
417	
418	\subsection{Complexity-without-Utility}
419	
420	\paragraph{Definition.}
421	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous: none individually necessary for the proof.
422	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
423	
424	\paragraph{Example (FOL).}
425	\smallskip\noindent\rule{\columnwidth}{0.3pt}
426	{\small\begin{verbatim}
427	Premises:
428	  all x all y (R(x,y) ->
429	    exists z (S(x,z) & T(z,y))).
430	  all x (P(x) -> Q(x)).
431	  P(a).            % only this needed
432	Conclusion: Q(a).
433	\end{verbatim}}
434	\noindent\rule{\columnwidth}{0.3pt}\smallskip
435	
436	\paragraph{ISR interaction.}
437	ISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.
438	This is the mode ISR is best calibrated for.
439	
440	\paragraph{Prevalence.}
441	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
442	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
443	
444	
445	\subsection{Contradiction Explosion}
446	
447	\paragraph{Definition.}
448	The component count grows unboundedly over training.
449	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
450	Individual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
451	
452	\paragraph{Example (FOL, 1000-step exec-only).}
453	\smallskip\noindent\rule{\columnwidth}{0.3pt}
454	{\small\begin{verbatim}
455	Premises:
456	  c1. c2. c3. ... c18. % 18.55 mean
457	  % conclusion embedded among premises
458	Conclusion: Q(a).
459	\end{verbatim}}
460	\noindent\rule{\columnwidth}{0.3pt}\smallskip
461	
462	\paragraph{ISR interaction.}
463	ISR~$\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\% of proved samples having ISR~$=0$).
464	
465	\paragraph{Prevalence.}
466	Observed in extended exec-only training (seed~42, 1000 steps).
467	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
468	
469	
470	\subsection{Query-as-Fact Gaming}
471	
472	\paragraph{Definition.}
473	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
474	Prolog trivially proves the query by unifying with the fact.
475	This mode evades text-match classifiers designed for CE/TS because the generated atom bears no surface resemblance to the original conclusion text.
476	
477	\paragraph{Example (Prolog).}
478	\smallskip\noindent\rule{\columnwidth}{0.3pt}
479	\begin{verbatim}
480	% NL: "Fido is happy."
481	% Model output:
482	fido_is_happy.
483	:- fido_is_happy.     % query = fact
484	\end{verbatim}
485	\noindent\rule{\columnwidth}{0.3pt}\smallskip
486	
487	\paragraph{ISR interaction.}
488	ISR~$\approx 0.9$--$1.0$.
489	The single fact is trivially necessary (its removal breaks the query), inflating ISR.
490	Functionally equivalent to TS but with a distinct surface mechanism.
491	
492	\paragraph{Prevalence.}
493	Observed in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).
494	95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% non-hacking.
495	
496	
497	\section{Per-Seed Detailed Results}
498	\label{app:detailed-results}
499	
500	Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
501	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
502	ISR values are proved-only ISR$^*$.
503	
504	\begin{table*}[t]
505	\centering
506	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (CE/PG classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass PG detection and commuted premises that bypass CE detection; reclassified as degenerate. $^\diamond$Seeds 45--46 added post-hoc under identical hyperparameters (effective batch size 8; micro-batch decomposition differs: $4{\times}2$ vs.\ $2{\times}4$, mathematically equivalent).}
507	\label{tab:fol-detailed}
508	\label{tab:fol-beta01-detailed}
509	\small
510	\setlength{\tabcolsep}{3pt}
511	\resizebox{\textwidth}{!}{%
512	\begin{tabular}{@{}llccccccl@{}}
513	\toprule
514	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Notes} \\
515	\midrule
516	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
517	Base model (no training)
518	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
519	Ground-truth FOL
520	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
521	SFT
522	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
523	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
524	  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \textbf{93.3} & \\
525	\cmidrule(l){2-9}
526	  & \multicolumn{2}{l}{3-seed pooled} & $0.130$ & $0.595$ & $0$ & $7.8$ & \textbf{92.3} & $n{=}39$ proved \\
527	\midrule
528	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
529	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
530	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & PG${=}5.4\%$ \\
531	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
532	  & 43 & 500 & 0.13 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Greedy ($n_{\text{proved}}{=}13$) \\
533	  & 43 & 1000 & 0.96 & 0.082 & 0 & 93.8 & 6.2 & CE dominant \\
534	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
535	  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\ddagger$ & PG${=}15\%$ \\
536	\cmidrule(l){2-9}
537	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.68{\pm}0.47$ & $0.238{\pm}0.30$ & & & & 500-step \\
538	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.97{\pm}0.02$ & $0.029{\pm}0.05$ & & & $2.1{\pm}3.6$ & 1000-step \\
539	\midrule
540	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
541	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{17.3} & Mixed CE+TS+PG \\
542	  & 42 & 1000 & 0.90 & 0.877 & 96.7 & 0 & 2.2 & TS collapse; PG${=}1$ ($n{=}90$) \\
543	  & 43 & 500 & 0.61 & 0.830 & \textbf{100} & 0 & 0 & TSa${=}59$, TSb${=}2$ \\
544	  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & TS dominant (FN corrected) \\
545	  & 45$^\diamond$ & 500 & 0.42 & 0.605 & 38.1 & 4.8 & \textbf{54.8} & PG${=}1$; $n{=}42$ \\
546	  & 46$^\diamond$ & 500 & 0.77 & 0.411 & 14.3 & 26.0 & \textbf{54.5} & PG${=}4$; $n{=}77$ \\
547	\cmidrule(l){2-9}
548	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.77{\pm}0.14$ & $0.716{\pm}0.26$ & & & & 500-step (s42--44) \\
549	  & \multicolumn{2}{l}{5-seed mean$\pm$std} & $0.70{\pm}0.19$ & $0.633{\pm}0.23$ & & & & 500-step (s42--46) \\
550	\midrule
551	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
552	  & \multicolumn{8}{l}{See Table~\ref{tab:beta03-detailed} for per-seed $\beta{=}0.3$ results.} \\
553	\midrule
554	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
555	  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & PG${=}4$ \\
556	  & 43 & 500 & 0.94 & 0.150 & \textbf{38.3} & 59.6 & 1.1 & TSa${=}36$; PG${=}1$ \\
557	  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & PG${=}16$ (CE$\cap$PG: 6) \\
558	\cmidrule(l){2-9}
559	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.87{\pm}0.08$ & $0.117{\pm}0.042$ & & & & TS seed-dep.: 0/38/0\% \\
560	\midrule
561	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
562	  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$; $n_{\text{comp}} = 9.6$ \\
563	  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\text{N-H}}{=}3$ \\
564	  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\
565	\cmidrule(l){2-9}
566	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.54{\pm}0.35$ & $0.09{\pm}0.09$ & & & & \\
567	\midrule
568	\multicolumn{9}{@{}l}{\textit{Shuffled-ISR $\beta{=}0.1$ (deconfounding control)}} \\
569	  & 42 & 500 & 0.15 & 0.567 & 6.7 & 6.7 & \textbf{86.7} & $n{=}15$ proved \\
570	  & 43 & 500 & 0.16 & 0.568 & 6.3 & 6.3 & \textbf{87.5} & $n{=}16$ proved \\
571	  & 44 & 500 & 0.15 & 0.542 & 6.7 & 6.7 & \textbf{86.7} & $n{=}15$ proved \\
572	\cmidrule(l){2-9}
573	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.153{\pm}0.006$ & $0.559{\pm}0.015$ & $6.5$ & $6.5$ & \textbf{87.0} & $N{=}46$ proved \\
574	\bottomrule
575	\end{tabular}}% end resizebox
576	\end{table*}
577	
578	\begin{table*}[t]
579	\centering
580	\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\ = percentage among proved samples.  ``---'' indicates data not available.}
581	\label{tab:prolog-detailed}
582	\small
583	\begin{tabular}{@{}llcccccl@{}}
584	\toprule
585	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Notes} \\
586	\midrule
587	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
588	  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
589	  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
590	  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
591	\cmidrule(l){2-8}
592	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.53{\pm}0.31$ & $0.146{\pm}0.21$ & & & \\
593	\midrule
594	\multicolumn{8}{@{}l}{\textit{Exec+ISR (STA reward)}} \\
595	  & 42 & 0.50 & 1.000 & \textbf{100} & 0 & 0 & TS tautological \\
596	  & 43 & 0.38 & 0.185 & 0$^\ddagger$ & 97.4 & 0 & $^\ddagger$Functional TS$^a$ \\
597	  & 44 & 0.97 & 0.912 & 0$^\ddagger$ & 0 & 0$^\ddagger$ & Query-as-fact gaming$^b$ \\
598	\cmidrule(l){2-8}
599	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.62{\pm}0.31$ & $0.699{\pm}0.45$ & & & 3/3 Goodhart, 0\% non-hacking \\
600	\bottomrule
601	\end{tabular}
602	
603	\vspace{4pt}
604	{\small
605	$^a$ Strict TS classifier reports 0\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\
606	$^b$ Strict classifier reports Non-hacking$\,{=}\,100$\%, but 95/97 proved samples have $n_{\text{necessary}}=1$. The model converts NL to snake\_case atoms serving as both fact and query, a third distinct Goodhart pathway.\\
607	$^\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.
608	}
609	\end{table*}
610	
611	\begin{table*}[t]
612	\centering
613	\caption{Detailed per-seed results: ProofFOL (Prover9). PR$_{\text{f50}}$ = mean prove rate over final 50 steps. TS = tautological shortcutting (\S\ref{sec:taxonomy}), CE = conclusion embedding, Genuine = classified as neither TS nor CE. Stable convergence: PR$_{\text{f50}}{>}0.90$.}
614	\label{tab:prooffol-detailed}
615	\small
616	\begin{tabular}{@{}llcccccl@{}}
617	\toprule
618	\textbf{Condition} & \textbf{Seed} & \textbf{PR$_{\text{f50}}$} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{Genuine\%} & \textbf{Notes} \\
619	\midrule
620	Base & --- & 0.16 & 0.310 & 0 & 0 & \textbf{100} & $n{=}16$ proved \\
621	\midrule
622	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
623	  & 42 & ${\approx}$1.0 & 0.066 & \textbf{100} & 0 & 0 & $n{=}99$; stable \\
624	  & 43 & 0.55 & 0.119 & 0 & 49.2 & 50.8 & $n{=}63$; partial \\
625	  & 44 & ${\approx}$1.0 & 0.043 & 0 & 98.6 & 1.4 & $n{=}72$; stable \\
626	\cmidrule(l){2-8}
627	  & \multicolumn{2}{l}{Aggregate} & & \multicolumn{3}{c}{17.4\% genuine (mean of seeds)} & \\
628	\midrule
629	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
630	  & 42 & 0.35 & 0.12 & 0 & 0 & \textbf{100} & $n{=}46$; collapsed \\
631	  & 43 & ${\approx}$0.47 & ${\approx}$0.13 & 0 & 69.6 & 30.4 & $n{=}56$; unstable \\
632	  & 44 & 0.49 & 0.145 & 0 & 0 & \textbf{100} & $n{=}66$; oscillation \\
633	\cmidrule(l){2-8}
634	  & \multicolumn{2}{l}{Aggregate} & & \multicolumn{3}{c}{\textbf{76.8\%} genuine (mean of seeds)} & \\
635	\bottomrule
636	\end{tabular}
637	
638	\vspace{4pt}
639	{\small Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}
640	\end{table*}
641	
642	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
643	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
644	ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
645	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while component necessity collapses, confirming that ISR flags degeneration invisible to execution reward.
646	By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
647	
648	\paragraph{Prolog: universal Goodhart via three distinct pathways.}
649	All three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\% non-hacking proofs (Figure~\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:
650	seed~42 produces clean TS tautologies (single premise~$=$~conclusion),
651	seed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,
652	and seed~44 converts NL conclusions to snake\_case atoms used as both fact and query.
653	The diversity of gaming pathways across seeds (despite identical training data and reward function) demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
654	
655	\subsection{Per-Seed Results at $\beta{=}0.2$ and $\beta{=}0.3$}
656	\label{app:beta03}
657	
658	Table~\ref{tab:beta03-detailed} reports per-seed results for ISR at $\beta{=}0.2$ and both ISR and Random at $\beta{=}0.3$.
659	At $\beta{=}0.2$, all three seeds converge to pure TS Goodhart (100\% or near-100\% TS), confirming $\beta{\geq}0.2$ as the extremal Goodhart regime.
660	The three ISR $\beta{=}0.3$ seeds illustrate qualitatively distinct Goodhart pathways (\S\ref{sec:goodhart}).
661	
662	\begin{table*}[ht]
663	\centering
664	\caption{Per-seed results at $\beta{=}0.2$ and $\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples.}
665	\label{tab:beta03-detailed}
666	\small
667	\begin{tabular}{@{}llcccccl@{}}
668	\toprule
669	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Mode} \\
670	\midrule
671	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.2$}} \\
672	  & 42 & 1.00 & 0.602 & \textbf{100} & 0 & 0 & Pure TS ($n{=}100$) \\
673	  & 43 & 0.96 & 0.552 & \textbf{96.9} & 1.0 & 0 & PG${=}2$ \\
674	  & 44 & 0.94 & 0.964 & \textbf{100} & 0 & 0 & Pure TS ($n{=}94$) \\
675	\cmidrule(l){2-8}
676	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.97{\pm}0.03$ & $0.71{\pm}0.22$ & & & 3/3 TS Goodhart \\
677	\midrule
678	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
679	  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); PG${=}3$ \\
680	  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & CE shortcutting \\
681	  & 44 & 0.95 & 0.742 & \textbf{100} & 0 & 0 & Pure TS Goodhart \\
682	\cmidrule(l){2-8}
683	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.66{\pm}0.42$ & $0.39{\pm}0.31$ & & & \\
684	\midrule
685	\multicolumn{8}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
686	  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ \\
687	  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\text{N-H}}{=}3$ \\
688	  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\
689	\cmidrule(l){2-8}
690	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.54{\pm}0.35$ & $0.09{\pm}0.09$ & & & \\
691	\bottomrule
692	\end{tabular}
693	\end{table*}
694	
695	\FloatBarrier
696	
697	\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
698	\label{app:100step}
699	
700	To control for the prove-rate confound in our SFT comparison (\S\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\%, higher than SFT (13.0\%, 3-seed pooled) but still early in training.
701	Of the 32 proved samples, 9 (28.1\%) exhibit TS hacking (single premise identical to conclusion) and 1 (3.1\%) exhibits CE (conclusion embedded among premises), yielding a total hacking rate of 31.2\%.
702	By contrast, SFT at comparable or lower PR shows 7.7\% hacking (1/13 proved samples).
703	This demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.
704	The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
705	
706	\subsection{$O(1)$ vs.\ $O(n)$ ISR Ablation}
707	\label{app:o1-ablation}
708	
709	All main experiments (\S\ref{sec:diagnostic}--\ref{sec:crossdomain}) use $O(n)$ full LOO ISR during both training and evaluation; the $O(1)$ binary variant described below exists as an alternative implementation (\texttt{execution\_fast\_sta}) but is used only in the ablation reported here.
710	The two signals measure fundamentally different properties, not approximations of the same quantity.
711	The binary signal tests \emph{collective} premise necessity: $\text{fast\_ISR}(x) = 1$ if $x$ is proved and the conclusion is not provable under empty premises (tautology check), $0$ otherwise.
712	LOO tests \emph{individual} premise necessity: each component is removed in turn, and ISR reflects the fraction whose removal causes proof failure.
713	
714	\paragraph{Evaluation-time comparison.}
715	Across 402 proved samples from all ProofFOL conditions, the $O(1)$ binary signal is 1.0 for every sample: non-tautological conclusions cannot be proved without any premises, so the collective necessity test is trivially satisfied.
716	This renders $O(1)$ unable to distinguish hacking from genuine formalizations: both pass the empty-premise check.
717	By contrast, $O(n)$ LOO produces a clear separation: exec-only models average $\text{ISR}^*{=}0.046$ ($n{=}234$) while ISR-trained models average $\text{ISR}^*{=}0.183$ ($n{=}168$), because hacking constructions contain individually redundant components that LOO detects.
718	Of 179 disagreements between the two signals, all are false positives ($O(1){=}1$, LOO${=}0$): the binary check approves formalizations that LOO correctly identifies as structurally degenerate.
719	
720	\paragraph{Training-time ablation.}
721	As a training reward ($r = 0.5\,r_{\text{exec}} + 0.5\,\text{fast\_ISR}$, seed~42, 500 steps), the $O(1)$ variant achieves $\text{PR}{=}63\%$ with $\text{ISR}^*{=}0.007$, functionally zero, compared to $\text{ISR}^*{=}0.132$ under exec-only and $\text{ISR}^*{=}0.42$ under $O(n)$ ISR $\beta{=}0.1$.
722	The tautology check depresses prove rate by 30\,pp relative to exec-only ($63\%$ vs.\ $93\%$) by penalizing formalizations where the conclusion is provable without premises, but this constraint provides no gradient toward individual component necessity; the model is free to degenerate as long as it avoids trivial tautologies.
723	That even the fine-grained $O(n)$ LOO signal, which \emph{does} provide per-component necessity feedback, is ultimately gamed (\S\ref{sec:goodhart}) underscores that the problem lies in reward optimization itself, not in signal granularity.
724	
725	\paragraph{Computational overhead.}
726	Full LOO requires $n{+}1$ solver calls per sample (mean $n{\approx}6$ for FOLIO).
727	With Prover9 at ${\sim}5$\,ms per call, STA evaluation adds ${\sim}55$\,ms per sample versus ${\sim}4$\,s for LLM inference (${<}1\%$ overhead).
728	The $O(1)$ binary check adds a single solver call per proved sample (${<}2\%$ per training step), but the evaluation above shows this saving comes at the cost of all diagnostic power.
729	
730	\subsection{Cross-Model Generalization: LLaMA-3.2-3B Cold-Start Failure}
731	\label{app:llama-coldstart}
732	
733	We applied the identical GRPO configuration (Table~\ref{tab:hyperparams}) to LLaMA-3.2-3B~\citep{grattafiori2024llama} (3B; exec-only, seed~42, $K{=}4$, FOLIO).
734	Across 72 of 500 planned steps the model produced zero valid Prover9 output, generating only natural-language text; $r_{\text{exec}}{=}0$ for all rollouts yields zero GRPO advantage, so training was terminated early.\footnote{This run was also affected by a generation-termination configuration issue (dual EOS tokens); the zero prove rate reflects both the base model's lack of FOL generation capability and truncated outputs.}
735	This establishes a \emph{capability threshold}: the base model must produce syntactically valid solver input for the RL loop to generate signal.
736	Qwen3-4B crosses this threshold (non-zero prove rates within 10 steps) while LLaMA-3.2-3B does not despite comparable size (3B vs.\ 4B), likely reflecting pretraining data composition.
737	An SFT warmstart (3 epochs on gold formalizations, lr$=$2$\times$10$^{-5}$) achieves $\text{PR}{=}16\%$ ($n{=}100$) after correcting the generation-termination issue.
738	However, the model produces Unicode FOL notation ($\forall$, $\to$, $\wedge$) instead of the required ASCII syntax despite training on ASCII-formatted data; the 16\% prove rate reflects Prover9's partial Unicode tolerance rather than correct format adherence.
739	Subsequent GRPO runs (exec-only, 500 steps from SFT warmstart, 3 seeds) fail to improve beyond SFT baseline ($\text{PR}{=}15.0{\pm}1.0\%$, $n{=}14$--$16$ proved per seed), yet produce no structural degeneration: $86.6{\pm}0.9\%$ of proved samples are genuine across seeds, with cross-seed variance near zero ($\sigma_{\text{PR}}{=}1$\,pp).
740	This contrasts sharply with Qwen3-4B, where GRPO reaches $93\%$ PR but collapses to $8\%$ genuine with high cross-seed variance.
741	The result suggests structural degeneration is a byproduct of successful RL optimization, not of the training procedure \emph{per se}: when GRPO fails to amplify prove rate, the model retains structural integrity.
742	
743	\subsection{Seed-Dependent Convergence in Exec-Only GRPO}
744	\label{app:seed-convergence}
745	
746	Not all exec-only seeds converge.
747	Of 6 seeds tested (s42--s46, s52; s52 uses $K{=}4$, all others $K{=}8$), we observe three regimes: \emph{converging with degeneration} (s42: $\text{PR}{=}93\%$, genuine${=}7.5\%$; s44: $\text{PR}{=}96\%$, genuine${=}0\%$; s46: $\text{PR}{=}93\%$ at 500 steps), \emph{slow convergence with degeneration} (s43: $\text{PR}{=}14\%$ but $100\%$ hacking at 500 steps), and \emph{non-converging} (s45: $\text{PR}{=}15\%$, genuine${=}86.7\%$; s52: $\text{PR}{=}14\%$, genuine${=}85.7\%$).
748	Non-converging seeds retain high genuine rates (85--87\%), indicating that structural degeneration is conditional on successful RL optimization: when GRPO fails to bootstrap prove rate beyond base-model levels, the model preserves structural integrity.
749	Extended training to 1000 steps for s45 confirms persistent non-convergence ($\text{PR}{=}15\%$, $\text{ISR}^*{=}0.592$, genuine${=}86.7\%$, $n{=}15$ proved); the model neither improves nor degenerates.
750	
751	This parallels the LLaMA-3.2-3B finding (Appendix~\ref{app:llama-coldstart}), where GRPO also fails to improve PR and retains structural quality.
752	Both cases support the interpretation that degeneration is a byproduct of reward optimization success, not of the training procedure per se.
753	
754	\subsection{$N{=}2$ Sensitivity Analysis (Excluding Seed 43)}
755	\label{app:n2-sensitivity}
756	
757	Seed~43 was evaluated with sampling ($T{=}0.7$) rather than greedy decoding (\S\ref{app:setup}).
758	To assess whether this non-standard protocol affects qualitative conclusions, Table~\ref{tab:n2-sensitivity} reports pooled statistics from seeds~42 and~44 only.
759	
760	\begin{table}[h]
761	\centering
762	\resizebox{\columnwidth}{!}{%
763	\begin{tabular}{@{}lccc@{}}
764	\toprule
765	\textbf{Condition} & \textbf{PR (\%)} & \textbf{ISR$^*$} & \textbf{N-H (\%)} \\
766	\midrule
767	Exec-only 500-step & $95.5 \pm 3.5$ & $0.357 \pm 0.318$ & $3.8 \pm 5.3$ \\
768	Exec-only 1000-step & $98.0 \pm 2.8$ & $0.003 \pm 0.001$ & $0.0 \pm 0.0$ \\
769	ISR $\beta{=}0.1$ 500-step & $85.0 \pm 5.7$ & $0.659 \pm 0.344$ & $8.7 \pm 12.2$ \\
770	\bottomrule
771	\end{tabular}}
772	\caption{Pooled statistics excluding seed~43 ($N{=}2$, seeds~42 and~44 only). Mean$\pm$std of per-seed values. Qualitative patterns preserved: exec-only converges to ${\leq}7.5\%$ non-hacking; ISR $\beta{=}0.1$ shifts composition toward TS.}
773	\label{tab:n2-sensitivity}
774	\end{table}
775	
776	Excluding seed~43, exec-only converges to ${\leq}7.5\%$ non-hacking at 500 steps and $0\%$ at 1000 steps.
777	Under ISR $\beta{=}0.1$, TS dominates both remaining seeds (s42: $16\%$, s44: $100\%$), confirming that ISR reward shifts hacking composition toward tautological shortcuts independent of the s43 evaluation anomaly.
778	The large per-seed ISR$^*$ variance ($0.357 \pm 0.318$) reflects different degeneration modes (CE in s42 vs.\ TS in s44), not data quality issues.
779	
780	\subsection{Cross-Scale: Qwen3-8B Exec-Only GRPO}
781	\label{app:8b-results}
782	
783	To test whether structural degeneration generalizes beyond 4B scale, we apply exec-only GRPO to Qwen3-8B with $K{=}8$ rollouts per prompt ($K{=}4$ produces near-identical completions at 8B scale, yielding zero GRPO advantage and no learning signal).
784	Table~\ref{tab:8b-combined} summarizes configuration differences and results.
785	
786	\begin{table}[H]
787	\centering
788	\small
789	\begin{tabular}{lcc}
790	\toprule
791	& \textbf{Qwen3-4B} & \textbf{Qwen3-8B} \\
792	\midrule
793	Rollouts ($K$) & 4 & 8 \\
794	Batch size & 4 & 1 \\
795	Gradient accum. & 2 & 16 \\
796	Effective batch & 8 & 16 \\
797	\bottomrule
798	\end{tabular}
799	
800	\vspace{4pt}
801	
802	\resizebox{\columnwidth}{!}{%
803	\begin{tabular}{lcccc}
804	\toprule
805	\textbf{Config} & \textbf{PR\%} & \textbf{Genuine\%} & \textbf{Converged?} & \textbf{Gradient} \\
806	\midrule
807	4B $K{=}4$ s42 & 93 & 7.5 & Yes (degenerate) & Sufficient \\
808	8B $K{=}4$ s42 & 15.5 & --- & No & Zero \\
809	8B $K{=}8$ s42 & 14 & 92.9 & No & Partial \\
810	\bottomrule
811	\end{tabular}}
812	\caption{Cross-scale: Qwen3-4B vs.\ Qwen3-8B. \textbf{Top}: Configuration; $K{=}8$ required at 8B because $K{=}4$ produces near-identical rollouts. \textbf{Bottom}: Results; 4B converges with degeneration, both 8B configurations fail to converge, preserving structural integrity.}
813	\label{tab:8b-combined}
814	\end{table}
815	
816	We first tested $K{=}4$ (matching the 4B configuration): the 8B model produces near-identical rollouts across all four completions, yielding zero GRPO advantage throughout 500 steps and no learning signal ($\text{PR}{=}15.5\%$, cold-start stagnation).
817	Increasing to $K{=}8$ provides non-zero reward variance during mid-training (approximately 40--50\% of steps between 20--370 show non-zero advantage), but this signal proves insufficient for convergence: held-out evaluation yields $\text{PR}{=}14\%$ ($n{=}14$ proved), $\text{ISR}^*{=}0.573$, genuine${=}92.9\%$ (13/14), with a single CE sample.
818	Cosine learning-rate decay combined with insufficient early bootstrap appears to prevent the model from escaping the low-PR regime.
819	
820	This result mirrors two other non-convergence cases: (1)~the seed-dependent 4B non-convergence (s45, s52; Appendix~\ref{app:seed-convergence}), where identical 4B configurations fail to bootstrap, and (2)~the LLaMA-3.2-3B cold-start failure (Appendix~\ref{app:llama-coldstart}), where the base model lacks FOL generation capability entirely.
821	Together, these cases establish a convergence threshold for GRPO-driven degeneration: the structural collapse documented in \S\ref{sec:diagnostic} requires successful RL optimization as a prerequisite, and at 8B scale the rollout diversity bottleneck prevents this optimization from occurring under our configuration.
822	
823	\section{Use of AI Assistants}
824	\label{app:ai-assistants}
825	
826	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
827	\begin{itemize}
828	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
829	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \LaTeX{}.
830	    \item \textbf{Literature:} summarizing related papers to inform the related-work section.
831	\end{itemize}
832	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fe2546f-921c-42c8-9cee-457e0cd3a05c",
  "isSidechain": true,
  "promptId": "bd1f5afe-fb7f-4505-bdbb-0893686e1cf7",
  "agentId": "a4416bb1bbbdde2b1",
  "type": "user",
  "uuid": "efe1c08e-09b4-44a7-a87f-c1ee3316807e",
  "sourceToolAssistantUUID": "5fe2546f-921c-42c8-9cee-457e0cd3a05c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-25T19:46:11.787Z_

Here is an exhaustive extraction of every number in the paper, organized by section.

---

## ABSTRACT (abstract.tex)

| Line | Number | Context |
|------|--------|---------|
| 4 | ISR=1, ISR=0 (implicit via "equal") | Single-criterion reward conflates genuine derivation with shortcuts |
| 7 | 3 of 5 | "3 of 5 seeds converge to gaming under standard training conditions" |
| 7 | 2 | "2 retain genuine reasoning" |
| 4 | six | "six reward conditions" |

---

## INTRODUCTION (introduction.tex)

| Line | Number | Context |
|------|--------|---------|
| 14 | ISR=1 | "A formalization where every component is necessary receives ISR=1" |
| 14 | ISR=0 | "one that proves regardless... receives ISR=0" |
| 19 | 0.82 | `\includegraphics[width=0.82\columnwidth]` (figure width) |
| 20 | ISR approx 0 | "Exec-only collapses to ISR approx 0" |
| 20 | ~0.5 | "the ~0.5 plateau is an n=2 artifact" |
| 20 | n=2 | "n=2 artifact" |
| 20 | beta=0.1 | "ISR beta=0.1 seeds rise toward ISR approx 1" |
| 20 | ISR approx 1 | "rise toward ISR approx 1 via TS gaming" |
| 20 | 20 | "rolling w=20" (rolling window size) |
| 31 | eight | "catalogue eight hacking modes" |
| 31 | six | "across six reward conditions" |

---

## METHOD (method.tex)

| Line | Number | Context |
|------|--------|---------|
| 7 | K=4 | "GRPO (K=4)" |
| 10 | 100 | "held-out evaluation set (100 examples)" |
| 10 | 34 | "contains 34 True" |
| 10 | 25 | "25 False" |
| 10 | 41 | "41 Unknown labels" |
| 10 | ~34% | "theoretical PR ceiling ~34%" |
| 11 | PR=93% | "Exec-only GRPO reaching PR=93%" |
| 11 | 3x | "nearly 3x this ceiling" |
| 19 | ISR=1 | "TS achieve ISR=1 by construction" (figure caption) |
| 35 | ISR=1 | "ISR=1 means every component is necessary" (algorithm output range) |
| 35 | [0, 1] | "ISR(x) in [0,1]" |
| 52 | ISR=1 | "ISR=1 means every component is necessary" |
| 52 | ISR=0 | "ISR=0 means complete redundancy" |
| 53 | >90% | "more than 90% of low-ISR proved samples exhibiting identifiable hacking patterns" |
| 54 | O(2^n) | "full interaction detection would require O(2^n) evaluations" |
| 55 | rho = -0.049 | "Spearman rho(ISR, NLI accuracy) = -0.049" |
| 55 | p=0.187 | "p=0.187, n.s." |
| 66 | beta in {0.1, 0.3} | "ISR low/high-dose... at beta in {0.1,0.3}" |
| 69 | {42,43,44} | "seeds {42,43,44}" |
| 79 | 12 | "Base (0-shot) PR%=12" |
| 80 | 13 | "SFT PR%=13" |
| 80 | 0.595 | "SFT ISR*=0.595" |
| 80 | 0 | "SFT TS%=0" |
| 80 | 8 | "SFT CE%=8" |
| 80 | 92 | "SFT N-H%=92" |
| 82 | 93 | "Exec-only PR%=93" |
| 82 | 0.132 | "Exec-only ISR*=0.132" |
| 82 | 0 | "Exec-only TS%=0" |
| 82 | 87 | "Exec-only CE%=87" |
| 82 | 8 | "Exec-only N-H%=8" |
| 83 | 0.1 | "ISR beta=0.1" |
| 83 | 77 +/- 14 | "ISR (3-seed) PR%=77 +/- 14" |
| 83 | 1.06x | "ISR* = 1.06x (premise-count-matched)" |
| 83 | 71 | "ISR TS%=71 (FN-corrected)" |
| 83 | 18 | "ISR CE%=18" |
| 83 | 6 | "ISR N-H%=6" |
| 84 | 70 +/- 19 | "ISR (5-seed) PR%=70 +/- 19" |
| 84 | 0.63 | "ISR* = (0.63)" |
| 84 | 54 | "ISR (5-seed) TS%=54" |
| 84 | 18 | "ISR (5-seed) CE%=18" |
| 84 | 23 | "ISR (5-seed) N-H%=23" |
| 85 | 87 +/- 8 | "Random PR%=87 +/- 8" |
| 85 | 0.117 +/- .04 | "Random ISR*=0.117 +/- .04" |
| 85 | 14 | "Random TS%=14" |
| 85 | 69 | "Random CE%=69" |
| 85 | 10 | "Random N-H%=10" |
| 86 | 15 +/- 1 | "Shuffled-ISR PR%=15 +/- 1" |
| 86 | 0.559 +/- .02 | "Shuffled-ISR ISR*=0.559 +/- .02" |
| 86 | 7 | "Shuffled-ISR TS%=7" |
| 86 | 7 | "Shuffled-ISR CE%=7" |
| 86 | 87 | "Shuffled-ISR N-H%=87" |
| 88 | 0.3 | "ISR beta=0.3" |
| 88 | 66 +/- 42 | "ISR b=0.3 PR%=66 +/- 42" |
| 88 | 0.39 +/- .31 | "ISR b=0.3 ISR*=0.39 +/- .31" |
| 88 | 50 | "ISR b=0.3 TS%=50" |
| 88 | 37 | "ISR b=0.3 CE%=37" |
| 88 | 11 | "ISR b=0.3 N-H%=11" |
| 89 | 0.3 | "Random beta=0.3" |
| 89 | 54 +/- 35 | "Random b=0.3 PR%=54 +/- 35" |
| 89 | 0.09 +/- .09 | "Random b=0.3 ISR*=0.09 +/- .09" |
| 89 | 7 | "Random b=0.3 TS%=7" |
| 89 | 91 | "Random b=0.3 CE%=91" |
| 89 | 2 | "Random b=0.3 N-H%=2" |
| 92 | 38.3% | "s43: 38.3%" (seed-dependent TS footnote) |
| 97 | ISR >= 0.5 | "removing the sole premise forces ISR >= 0.5" |
| 97 | eight | "eight structural-degeneration modes" |
| 98 | Five | "Five additional modes" |

---

## EXPERIMENTS (experiments.tex)

| Line | Number | Context |
|------|--------|---------|
| 9 | K=4 | "GRPO (K=4)" |
| 9 | 10^-6 | "lr 10^-6" |
| 9 | 500 | "500 steps default" |
| 9 | 1000 | "1000 where noted" |
| 9 | {42,43,44} | "seeds {42,43,44}" |
| 9 | {45,46} | "ISR beta=0.1 extends to {45,46}" |
| 9 | 500 | "500-example FOLIO subset" |
| 10 | 100 | "100 FOLIO examples" |
| 10 | T=0.7 | "nucleus sampling (T=0.7)" |
| 10 | <=7% | "both remaining seeds show <=7% non-hacking" |
| 10 | 1000 | "at 1000 steps" |
| 11 | ~500 | "~500 training examples" (ProofFOL) |
| 11 | ~70% | "~70% retention" (Prover9 filtering) |
| 11 | 0.90 | "PR_final_50 > 0.90" (stable convergence threshold) |
| 12 | 152 | "152-sample precision audit" |
| 16 | 0.72 | `\includegraphics[width=0.72\columnwidth]` (figure width) |
| 17 | 0.1 | "ISR beta=0.1" |
| 17 | 500 | "500 steps" |
| 17 | <=17% | "N-H <= 17%" (3 gaming seeds) |
| 17 | ~55% | "two retain genuine reasoning (~55%)" |
| 23 | N=3 | "N=3 strata" (CMH test) |
| 25 | p=0.10 | "ProofFOL results (p=0.10)" |
| 25 | N=3 | "N=3" (ProofFOL) |
| 31 | 1000 | "1000 training steps" (exec-only seed 42) |
| 32 | 32% | "PR climbs from 32%" |
| 32 | 96% | "to 96%" |
| 32 | 0.642 | "ISR* collapses from 0.642" |
| 32 | 0.003 | "to 0.003" |
| 32 | 214x | "a 214x raw drop" |
| 32 | 1.06x | "matched comparison yields 1.06x" |
| 33 | 500 | "By 500 steps" |
| 33 | 87% | "87% of proved samples embed the conclusion" |
| 34 | ISR=1.0 | "binary variant... ISR=1.0 for all proved samples" |
| 35 | <=6.2% | "All three exec-only seeds converge to <=6.2% non-hacking" |
| 35 | 1000 | "by 1000 steps" |
| 38 | <=6.2% | "all converge to <=6.2% non-hacking by 1000 steps" |
| 39 | 13--98% | "PR range: 13--98%" |
| 40 | PR approx 14% | "Two additional seeds... fail to converge (PR approx 14%)" |
| 43 | 92% | "SFT... produces 92% non-hacking outputs" |
| 43 | PR=13% | "at PR=13%" |
| 43 | 147 | "odds ratio = 147" |
| 43 | p<0.001 | "p<0.001" |
| 45 | 100 | "at 100 steps" |
| 45 | PR=32% | "PR=32%" |
| 45 | 31% | "hacking already reaches 31%" |
| 45 | 8% | "SFT's 8% at comparable PR" |
| 52 | 214x | "214x raw" ISR* collapse |
| 52 | 1.06x | "collapses to 1.06x after controlling for premise count" |
| 60 | 0.80 | `\includegraphics[width=0.80\columnwidth]` (figure width) |
| 66 | 71% | "71% of proved samples under ISR exhibit tautological shortcuts" |
| 66 | 14% | "vs. 14% under random" |
| 67 | 68--100% | "Total CE+TS spans 68--100%" |
| 68 | chi^2=174.8 | "chi^2=174.8" |
| 68 | df=2 | "df=2" |
| 68 | p<10^-38 | "p<10^-38" |
| 71 | 3 of 5 | "3 of 5 seeds converge to gaming" |
| 71 | 95% | "95% Clopper-Pearson CI" |
| 71 | [11.8%, 88.1%] | "CI: [11.8%, 88.1%]" |
| 71 | n=5 | "n=5" |
| 71 | 2 of 5 | "2 of 5 retain substantial genuine reasoning" |
| 72 | <=17% | "converged seeds show <=17% non-hacking at 500 steps" |
| 72 | <=2% | "collapsing to <=2% by 1000" |
| 76 | 214x | "214x raw ISR* collapse" |
| 76 | 1.06x | "premise-count-matched comparison yields only 1.06x" |
| 76 | p=0.317 | "McNemar p=0.317" |
| 76 | n=100 | "n=100 matched pairs" |
| 79 | 4--6 | "4--6 premises" |
| 79 | 19.7% | "TS reaches 19.7% under ISR" |
| 79 | 0% | "versus 0% under random reward" |
| 85 | 0.85 | `\includegraphics[width=0.85\columnwidth]` (figure width) |
| 86 | 4--6 | "4--6 premise range" (figure caption) |
| 91 | 17% | "non-hacking drops from 17%" |
| 91 | 2% | "to 2% by 1000 steps" |
| 92 | 0.2 | "beta=0.2 eliminates all non-hacking" |
| 92 | 0.3 | "beta=0.3 destabilizes training itself" |
| 108 | 18.2 +/- 3.2 | "ProofFOL FOL premises mean 18.2 +/- 3.2" |
| 108 | 5.3 +/- 1.4 | "FOLIO FOL premises mean 5.3 +/- 1.4" |
| 109 | 10.2 +/- 3.0 | "ProofFOL ground facts 10.2 +/- 3.0" |
| 109 | 1.8 +/- 1.5 | "FOLIO ground facts 1.8 +/- 1.5" |
| 110 | 8.1 +/- 1.1 | "ProofFOL rules 8.1 +/- 1.1" |
| 110 | 3.5 +/- 1.9 | "FOLIO rules 3.5 +/- 1.9" |
| 111 | 0% | "ProofFOL XOR samples 0%" |
| 111 | 37.2% | "FOLIO XOR samples 37.2%" |
| 112 | 4--5 | "ProofFOL dominant depth 4--5" |
| 112 | 2--3 | "FOLIO dominant depth 2--3" |
| 116 | n=500 | "n=500 training examples each" |
| 116 | 3.4x | "ProofFOL has 3.4x more premises" |
| 123 | 0.387 | "s44 Prolog 0.387" |
| 123 | n=21 | "small-sample artifact, n=21" |
| 123 | T=0.7 | "s43 FOL uses sampling T=0.7" |
| 123 | 0% | "all 3 seeds reach 0% non-hacking" (figure caption) |
| 129 | 0% | "all three seeds reach 0% non-hacking" |
| 137 | p=0.10 | "p=0.10, exploratory" |
| 138 | ISR approx 0 | "yielding ISR approx 0" |
| 141 | PR=14% | "Qwen3-8B... PR=14%" |
| 141 | K=8 | "K=8" |
| 141 | K=4 | "K=4 produces zero gradient" |
| 154 | 87, 18, 68, 8, 0 | CE% row: Exec/ISR/Rnd/SFT/Prolog |
| 155 | 0, 71, 14, 0, 100 | TS% row |
| 156 | 5, 5, 8, 0 | PG% row |
| 160 | 1 | "complexity-without-utility: Random=1" |
| 163 | 8, 6, 10, 92, 0 | Non-hacking% row |
| 171 | 92% | "SFT achieves 92% non-hacking" |

---

## DISCUSSION AND CONCLUSION (conclusion.tex)

| Line | Number | Context |
|------|--------|---------|
| 5 | <=6.2% | "non-hacking rates collapse to <=6.2% by 1000 steps" |
| 5 | 90% | "despite prove rates exceeding 90%" |
| 5 | 1000 | "by 1000 steps" |
| 10 | p=0.10 | "ProofFOL, p=0.10" |
| 12 | five | "five practical guidelines" |

---

## LIMITATIONS (limitations.tex)

| Line | Number | Context |
|------|--------|---------|
| 3 | 3/5 | "the 3/5 gaming rate" |
| 3 | 45--46 | "seeds 45--46 added post-hoc" |
| 4 | 1,435 | "FOLIO is a relatively small (1,435 examples)" |

---

## RELATED WORK (related_work.tex)

No standalone numerical results. References to ISR, LOO, etc. but no new quantitative values beyond what is defined in Method/Experiments.

---

## APPENDIX (appendix.tex)

### Hyperparameters Table (lines 10-50)

| Line | Number | Context |
|------|--------|---------|
| 21 | Qwen3-4B | "Base model" |
| 25 | K=4 | "Rollouts per prompt" |
| 26 | 500 | "Training steps (default)" |
| 27 | 1000 | "Training steps (extended)" |
| 28 | 1e-6 | "Learning rate = 1 x 10^-6" |
| 29 | 4 | "Per-device batch size = 4" |
| 30 | 2 | "Gradient accumulation steps = 2" |
| 31 | 8 | "Effective batch size = 8" |
| 32 | 512 | "Max completion length = 512 tokens" |
| 33 | 42, 43, 44 | "Random seeds" |
| 36 | 500 | "Training set: FOLIO, 500 examples" |
| 37 | 100 | "Evaluation set: FOLIO, 100 examples" |
| 42 | 8.4.2 | "SWI-Prolog 8.4.2" |
| 45 | T=0 | "Greedy (T=0)" |

### Compute Resources (lines 52-55)

| Line | Number | Context |
|------|--------|---------|
| 53 | 24 GB | "NVIDIA RTX 4090 24 GB" |
| 53 | 96 GB | "RTX PRO 6000 96 GB" |
| 54 | 1--2 | "1--2 GPU-hours (500 steps)" |
| 54 | 3--5 | "3--5 GPU-hours (1000 steps)" |
| 55 | 80--120 | "approximately 80--120 GPU-hours total" |

### SFT Convergence (line 58)

| Line | Number | Context |
|------|--------|---------|
| 58 | <=0.04 | "final-step loss <=0.04" |
| 58 | >99% | "token accuracy >99%" |
| 58 | ~8 | "~8 epochs on 500 examples" |
| 58 | 0.029 | "seed 42: 0.029" |
| 58 | 0.033 | "seed 44: 0.033" |
| 58 | 0.017 | "1000-step extension further decreases loss to 0.017" |

### Evaluation Exception (line 61)

| Line | Number | Context |
|------|--------|---------|
| 61 | 0.7 | "temperature = 0.7" |

### ProofFOL Construction (lines 67-75)

| Line | Number | Context |
|------|--------|---------|
| 69 | 10,424 | "ProofWriter (10,424 training examples)" |
| 69 | ~70% | "~70% retention" |
| 70 | 99.1% | "99.1% parse successfully" |
| 70 | 92 | "92 skipped due to empty FOL output" |
| 71 | 500 | "500 training" |
| 71 | 100 | "100 evaluation examples" |
| 74 | 3.4x | "3.4x more premises" |

### Extended Discussion: ISR vs NLI (line 83)

| Line | Number | Context |
|------|--------|---------|
| 83 | rho = -0.049 | "Spearman rho(ISR, NLI accuracy) = -0.049" |
| 83 | p = 0.187 | "p = 0.187, n.s." |

### Shapley Value (lines 92-97)

| Line | Number | Context |
|------|--------|---------|
| 95 | n-1 | "|S|=n-1" (maximal coalition) |
| 97 | O(n) | "O(n) cost" |

### Premise-Count Confound (lines 99-107)

| Line | Number | Context |
|------|--------|---------|
| 102 | 2 | "formalization with 2 premises... ISR=1.0" |
| 102 | ISR=1.0 | (2-premise example) |
| 102 | 10 | "one with 10 premises" |
| 102 | 8 | "8 are necessary" |
| 102 | ISR=0.8 | "yields ISR=0.8" |
| 104 | 1.06x | "Premise-count-matched comparison... 1.06x" |
| 104 | p=0.317 | "McNemar's test p=0.317" |

### Premise-Bin Modes Table (lines 109-128)

| Line | Number | Context |
|------|--------|---------|
| 116 | 8 | "ISR <=3 premises: N_proved=8" |
| 116 | 50.0 | "CE%=50.0" |
| 116 | 12.5 | "TS%=12.5" |
| 116 | 12.5 | "Genuine%=12.5" |
| 117 | 6 | "Random <=3 premises: N_proved=6" |
| 117 | 50.0 | "CE%=50.0" |
| 117 | 0.0 | "TS%=0.0" |
| 117 | 50.0 | "Genuine%=50.0" |
| 119 | 61 | "ISR 4-6: N_proved=61" |
| 119 | 47.5 | "CE%=47.5" |
| 119 | 19.7 | "TS%=19.7" |
| 119 | 14.8 | "Genuine%=14.8" |
| 120 | 58 | "Random 4-6: N_proved=58" |
| 120 | 72.4 | "CE%=72.4" |
| 120 | 0.0 | "TS%=0.0" |
| 120 | 22.4 | "Genuine%=22.4" |
| 122 | 12 | "ISR >=7: N_proved=12" |
| 122 | 75.0 | "CE%=75.0" |
| 122 | 0.0 | "TS%=0.0" |
| 122 | 25.0 | "Genuine%=25.0" |
| 123 | 15 | "Random >=7: N_proved=15" |
| 123 | 86.7 | "CE%=86.7" |
| 123 | 0.0 | "TS%=0.0" |
| 123 | 13.3 | "Genuine%=13.3" |

### Fisher Exact Tests Table (lines 130-153)

| Line | Number | Context |
|------|--------|---------|
| 140 | 6.06% | "ISR non-hacking 6.06% [3.6, 9.9]" |
| 140 | 9.5% | "Random non-hacking 9.5% [6.5, 13.7]" |
| 140 | OR=0.61 | "odds ratio 0.61" |
| 140 | p=0.182 | "p=0.182 (n.s.)" |
| 141 | 6.06% | "ISR" |
| 141 | 7.5% | "Exec-only" |
| 141 | OR=0.79 | "odds ratio 0.79" |
| 141 | p=0.62 | "p=0.62" |
| 142 | 9.5% | "Random" |
| 142 | 7.5% | "Exec-only" |
| 142 | OR=1.30 | "odds ratio 1.30" |
| 142 | p=0.68 | "p=0.68" |
| 145 | 70.6% | "ISR TS 70.6% [64.3, 76.3]" |
| 145 | 13.7% | "Random TS 13.7% [9.9, 18.6]" |
| 145 | OR=15.05 | "odds ratio 15.05" |
| 145 | 1.3e-39 | "p = 1.3 x 10^-39" |
| 148 | 92.3% | "SFT non-hacking 92.3% [79.7, 97.3]" |
| 148 | 7.5% | "Exec-only 7.5%" |
| 148 | OR=147 | "odds ratio 147" |
| 148 | p<0.001 | "p<0.001" |
| 152 | n=231 | "ISR: n=231 (3 seeds)" |
| 152 | n=262 | "Random: n=262 (3 seeds)" |
| 152 | n=93 | "Exec-only: n=93 (s42)" |
| 152 | n=39 | "SFT: n=39 (3 seeds, 1000 steps)" |
| 152 | 95% | "95% Wilson CIs" |

### TS Dose-Response (lines 155-157)

| Line | Number | Context |
|------|--------|---------|
| 156 | 13.7% | "random beta=0.1 produces 13.7% TS" |
| 156 | 36/262 | "36/262 pooled" |
| 156 | 38.3% | "per-seed: 38.3% in s43" |
| 156 | 0% | "0% in s42/s44" |
| 156 | 4--7 | "random beta=0.3 yields 4--7 TSa samples per seed" |
| 156 | 70.6% | "ISR beta=0.1 reaches 70.6%" |
| 156 | 163/231 | "163/231" |

### Goodhart Implications (line 161)

| Line | Number | Context |
|------|--------|---------|
| 161 | ISR >= 0.5 | "P->P tautologies yield ISR>=0.5" |
| 161 | beta >= 0.2 | "beta>=0.2 introduces extremal elements" |
| 161 | 18% | "PR collapse to 18%" |
| 161 | 48% | "vs. 48% random at beta=0.3" |

### Single-Seed Unreliability (lines 164-167)

| Line | Number | Context |
|------|--------|---------|
| 165 | sigma=47 | "PR sigma=47 percentage points" |
| 166 | 2/3 | "2/3 dominated by conclusion duplication" |
| 166 | 1/3 | "1/3 by premise minimization" |

### Multiple Testing Correction (lines 179-187)

| Line | Number | Context |
|------|--------|---------|
| 181 | k=14 | "FOLIO (k=14 tests)" |
| 181 | k=1 | "ProofFOL (k=1)" |
| 182 | alpha=0.05 | "Bonferroni correction at alpha=0.05" |
| 182 | 0.0036 | "adjusted thresholds of p_adj = 0.05/14 = 0.0036" |
| 183 | 1.82e-38 | "p_bonf = 1.82 x 10^-38" |
| 183 | 0.014 | "p_bonf = 0.014" |
| 183 | <10^-8 | "p_bonf < 10^-8" |
| 184 | 0.056 | "borderline (p_bonf = 0.056)" |
| 184 | alpha=0.10 | "significant at alpha=0.10" |
| 185 | p=0.10 | "ProofFOL... (p=0.10)" |

### Chi-Squared Tests (lines 189-192)

| Line | Number | Context |
|------|--------|---------|
| 190 | 3x2 | "pooled 3x2 contingency table" |
| 190 | chi^2=174.8 | "chi^2=174.8" |
| 190 | df=2 | "df=2" |
| 190 | 1.08e-38 | "p=1.08 x 10^-38" |
| 191 | chi^2=15.8 | "s42: chi^2=15.8" |
| 191 | p<0.001 | "p<0.001" |
| 191 | chi^2=59.4 | "s43: chi^2=59.4" |
| 191 | p<10^-13 | "p<10^-13" |
| 191 | chi^2=168.0 | "s44: chi^2=168.0" |
| 191 | p<10^-36 | "p<10^-36" |
| 192 | OR_CMH=2.46 | "OR_CMH=2.46" |
| 192 | p<10^-8 | "p<10^-8" |

### Hacking Modes Extended Table (lines 204-223)

| Line | Number | Context |
|------|--------|---------|
| 211 | 87, 18, 68, 8 | CE%: Exec/ISR/Rnd/SFT |
| 212 | 71, 14 | TS%: ISR=71, Rnd=14 |
| 213 | 5, 5, 8, 0 | PG% |
| 217 | 1 | "complexity-without-utility: Rnd=1" |
| 221 | n=149 | "TSa: n=149 ISR" |
| 221 | 36 | "+ 36 random" |
| 221 | n=14 | "TSb: n=14" |
| 221 | 38.3% | "Random TS driven by seed 43 (38.3%)" |
| 221 | 0% | "seeds 42/44: 0%" |
| 221 | 87% | "CE=87% in s42" |

### Classifier Validation (lines 225-262)

| Line | Number | Context |
|------|--------|---------|
| 230 | 50 | "manually verified 50 randomly sampled outputs" |
| 230 | >95% | "estimated precision >95%" |
| 230 | [93%, 100%] | "Wilson 95% CI: [93%, 100%]" |
| 233 | 95/97 | "95/97 samples were tautological" |
| 233 | n_necessary=1 | "n_necessary=1" |
| 236 | 82 | "Stratified validation across 82 samples" |
| 236 | kappa=1.0 | "Cohen's kappa=1.0" |
| 237 | 20 | "Structured inspection of 20 boundary cases" |
| 237 | 10 | "short-conclusion CE (10)" |
| 237 | 4 | "minimum 4 characters" |
| 237 | 5 | "low-ISR genuine (5)" |
| 237 | ISR=0.22 | "minimum ISR=0.22" |
| 237 | 5 | "TS on false propositions (5)" |
| 237 | 20/20 | "confirmed 20/20 correct classifications" |
| 240 | 3/5 | "3/5 TS boundary cases confirm factually false propositions" |
| 249 | 80 | "CE: Val N=80" |
| 249 | 1.00 | "CE Prec.=1.00" |
| 250 | 7 | "TS: Val N=7" |
| 250 | 1.00 | "TS Prec.=1.00" |
| 251 | 20 | "PG: Val N=20" |
| 251 | 1.00 | "PG Prec.=1.00" |
| 252 | 20 | "Contradiction: Val N=20" |
| 252 | 1.00 | "Contradiction Prec.=1.00" |
| 253 | 25 | "Genuine: Val N=25" |
| 253 | 1.00 | "Genuine Prec.=1.00" |
| 255 | 152 | "Overall: 152" |
| 255 | 1.00 | "Overall Prec.=1.00" |
| 258 | 374:2 | "pool ratio CE:TS=374:2" |
| 262 | >=91% | "TS recall: >=91%" |
| 262 | 149/163 | "149/163" |

### PG -- Premise-Subset Gaming (lines 264-287)

| Line | Number | Context |
|------|--------|---------|
| 270 | n_prem <= 3 | "unusually low premise counts (n_prem <= 3)" |
| 276 | PG=0 | "seed 42 audit confirmed PG=0" |
| 279 | 12 | "12 samples with n_prem=1" |
| 280 | 12 | "all 12 are logically equivalent to TS" |
| 280 | 11/12 | "vacuous quantifier wrapping (11/12)" |
| 280 | 1/12 | "structural simplification (1/12)" |
| 282 | 10/12 | "10/12 achieve ISR>=0.83" |
| 282 | ISR >= 0.83 | "ISR>=0.83" |
| 283 | 0 | "ISR s44 non-hacking=0" |
| 283 | 77 | "TSa (77 text-match)" |
| 283 | 12 | "TSb (12 obfuscated)" |
| 283 | 89 | "total TS = 89" |
| 286 | 14/231 | "ISR non-hacking = 14/231 = 6.06%" |
| 286 | 6.06% | "6.06%" |
| 286 | 25/262 | "random non-hacking = 25/262 = 9.5%" |
| 286 | 9.5% | "9.5%" |
| 286 | p=0.182 | "Fisher p=0.182, n.s." |
| 286 | [3.6%, 9.9%] | "Wilson 95% CI: ISR [3.6%, 9.9%]" |
| 286 | [6.5%, 13.7%] | "Random [6.5%, 13.7%]" |
| 287 | alpha=0.05 | "conventional alpha=0.05 threshold" |

### CE Prevalence (line 311)

| Line | Number | Context |
|------|--------|---------|
| 311 | 68--97% | "CE in some form... 68--97% across all RL conditions" |
| 312 | 69--93% | "manifests as CE (69--93%)" |
| 312 | 70.6% | "shifts to TS (70.6% pooled)" |

### TSa Prevalence (lines 333-340)

| Line | Number | Context |
|------|--------|---------|
| 333 | 0.8--1.0 | "ISR ~ 0.8--1.0" |
| 338 | 64.5% | "TSa: 64.5% pooled (149/231)" |
| 338 | 149/231 | "149/231" |
| 338 | 16.0% | "s42: 16.0%" |
| 338 | 96.7% | "s43: 96.7%" |
| 338 | 86.5% | "s44: 86.5%" |
| 339 | 70.6% | "Combined TS: 70.6% (163/231)" |
| 339 | 163/231 | "163/231" |
| 339 | 59 | "s43 TSa=59" |
| 339 | 2 | "TSb=2" |
| 340 | 13.7% | "Random pooled: 13.7% (36/262)" |
| 340 | 36/262 | "36/262" |
| 340 | 38.3% | "driven by seed 43 at 38.3%" |
| 340 | 0% | "seeds 42 and 44 at 0%" |

### TSb (lines 343-368)

| Line | Number | Context |
|------|--------|---------|
| 347 | 11/12 | "vacuous quantifier wrapping (11/12 instances)" |
| 347 | 1/12 | "structural simplification (1/12)" |
| 362 | ISR >= 0.83 | "ISR>=0.83 (10/12 samples)" |
| 362 | 10/12 | "10/12 samples" |
| 367 | 12/89 | "12/89 proved samples" |
| 367 | 2 | "seed 43 contributes 2 additional cases" |

### Tautological Collapse (lines 371-391)

| Line | Number | Context |
|------|--------|---------|
| 385 | ISR=1.0 | "ISR=1.0 (the sole premise is necessary)" |
| 386 | n_comp approx 2 | "low component count (n_comp approx 2)" |
| 389 | PR=0.98 | "FOL exec-only seed 44 (PR=0.98)" |
| 389 | 2.04 | "mean n_comp=2.04" |
| 389 | 100% | "100% TS by strict classifier" |
| 390 | PR=0.50 | "Prolog exec+STA seed 42 (PR=0.50)" |
| 390 | 100% | "100% TS" |

### Repetition Collapse (lines 393-416)

| Line | Number | Context |
|------|--------|---------|
| 405 | 512 | "repeated to 512 tokens" |
| 415 | 87% | "87% of outputs hit max completion length" |
| 415 | PR=13% | "PR=13%" |
| 415 | ISR=0 | "ISR=0" |

### Complexity-without-Utility (lines 418-441)

| Line | Number | Context |
|------|--------|---------|
| 441 | 3.8% | "Random beta=0.1 seed 42 at 3.8%" |
| 441 | 3/79 | "3/79" |

### Contradiction Explosion (lines 445-468)

| Line | Number | Context |
|------|--------|---------|
| 456 | 18 | "c1. c2. c3. ... c18." |
| 456 | 18.55 | "18.55 mean" |
| 463 | ISR=0.003 | "at 1000 steps: ISR=0.003" |
| 463 | 94.8% | "94.8% of proved samples having ISR=0" |
| 467 | ~6 | "mean component count grows from ~6 (500 steps)" |
| 467 | 18.55 | "to 18.55 (1000 steps)" |

### Query-as-Fact Gaming (lines 470-494)

| Line | Number | Context |
|------|--------|---------|
| 488 | 0.9--1.0 | "ISR ~ 0.9--1.0" |
| 493 | PR=0.97 | "Prolog exec+STA seed 44 (PR=0.97)" |
| 493 | ISR=0.912 | "ISR=0.912" |
| 494 | 95/97 | "95/97 proved samples have n_necessary=1" |
| 494 | 100% | "strict classifier reporting 100% non-hacking" |

### Per-Seed Detailed Tables: FOL (lines 497-576)

| Line | Number | Context |
|------|--------|---------|
| 506 | 4x2 vs 2x4 | "micro-batch decomposition: 4x2 vs. 2x4" |
| 518 | 0.12 | "Base model PR=0.12" |
| 518 | 0.064 | "Base model ISR*=0.064" |
| 520 | 0.18 | "Ground-truth FOL PR=0.18" |
| 520 | 0.559 | "Ground-truth FOL ISR*=0.559" |
| 522 | 0.13, 0.568, 0, 7.7, 92.3 | "SFT s42: PR/ISR*/TS/CE/N-H" |
| 523 | 0.11, 0.635, 0, 9.1, 90.9 | "SFT s43" |
| 524 | 0.15, 0.589, 0, 6.7, 93.3 | "SFT s44" |
| 526 | 0.130, 0.595, 0, 7.8, 92.3 | "SFT 3-seed pooled" |
| 526 | n=39 | "n=39 proved" |
| 529 | 0.32, 0.642 | "Exec s42 100-step" |
| 530 | 0.93, 0.132, 0, 87.1, 7.5 | "Exec s42 500-step" |
| 530 | 5.4% | "PG=5.4%" |
| 531 | 0.96, 0.003, 0, 100, 0 | "Exec s42 1000-step" |
| 532 | 0.13, 0 | "Exec s43 500-step" |
| 532 | n_proved=13 | "n_proved=13" |
| 533 | 0.96, 0.082, 0, 93.8, 6.2 | "Exec s43 1000-step" |
| 534 | 0.98, 0.582, 100, 0, 0 | "Exec s44 500-step" |
| 535 | 1.00, 0.002, 0, 85, 0 | "Exec s44 1000-step" |
| 535 | 15% | "PG=15%" |
| 537 | 0.68 +/- 0.47, 0.238 +/- 0.30 | "Exec 3-seed 500-step" |
| 538 | 0.97 +/- 0.02, 0.029 +/- 0.05 | "Exec 3-seed 1000-step" |
| 538 | 2.1 +/- 3.6 | "N-H" |
| 541 | 0.81, 0.415, 16.0, 51.9, 17.3 | "ISR b=0.1 s42 500-step" |
| 542 | 0.90, 0.877, 96.7, 0, 2.2 | "ISR b=0.1 s42 1000-step" |
| 542 | PG=1 | "PG=1" |
| 542 | n=90 | "n=90" |
| 543 | 0.61, 0.830, 100, 0, 0 | "ISR b=0.1 s43 500-step" |
| 543 | TSa=59, TSb=2 | "TSa=59, TSb=2" |
| 544 | 0.89, 0.902, 100, 0, 0 | "ISR b=0.1 s44 500-step" |
| 545 | 0.42, 0.605, 38.1, 4.8, 54.8 | "ISR b=0.1 s45 500-step" |
| 545 | PG=1, n=42 | "PG=1; n=42" |
| 546 | 0.77, 0.411, 14.3, 26.0, 54.5 | "ISR b=0.1 s46 500-step" |
| 546 | PG=4, n=77 | "PG=4; n=77" |
| 548 | 0.77 +/- 0.14, 0.716 +/- 0.26 | "ISR 3-seed mean (s42-44)" |
| 549 | 0.70 +/- 0.19, 0.633 +/- 0.23 | "ISR 5-seed mean (s42-46)" |
| 555 | 0.79, 0.131, 0, 73.4, 22.8 | "Random b=0.1 s42" |
| 555 | PG=4 | "PG=4" |
| 556 | 0.94, 0.150, 38.3, 59.6, 1.1 | "Random b=0.1 s43" |
| 556 | TSa=36, PG=1 | "TSa=36; PG=1" |
| 557 | 0.89, 0.070, 0, 82.0, 6.7 | "Random b=0.1 s44" |
| 557 | PG=16 | "PG=16 (CE∩PG: 6)" |
| 559 | 0.87 +/- 0.08, 0.117 +/- 0.042 | "Random 3-seed mean" |
| 562 | 0.48, 0.094, 8, 92, 0 | "Random b=0.3 s42" |
| 562 | TSa=4, n_comp=9.6 | "TSa=4; n_comp=9.6" |
| 563 | 0.92, 0.180, 7.6, 89.1, 3.3 | "Random b=0.3 s43" |
| 563 | TSa=7, n_N-H=3 | "TSa=7; n_N-H=3" |
| 564 | 0.23, 0, 0, 100, 0 | "Random b=0.3 s44" |
| 564 | n=23 | "n=23" |
| 566 | 0.54 +/- 0.35, 0.09 +/- 0.09 | "Random b=0.3 3-seed" |
| 569 | 0.15, 0.567, 6.7, 6.7, 86.7 | "Shuffled s42" |
| 569 | n=15 | "n=15 proved" |
| 570 | 0.16, 0.568, 6.3, 6.3, 87.5 | "Shuffled s43" |
| 570 | n=16 | "n=16 proved" |
| 571 | 0.15, 0.542, 6.7, 6.7, 86.7 | "Shuffled s44" |
| 571 | n=15 | "n=15 proved" |
| 573 | 0.153 +/- 0.006, 0.559 +/- 0.015, 6.5, 6.5, 87.0 | "Shuffled 3-seed" |
| 573 | N=46 | "N=46 proved" |

### Per-Seed Detailed Tables: Prolog (lines 578-609)

| Line | Number | Context |
|------|--------|---------|
| 588 | 0.83, 0.037 | "Prolog Exec s42" |
| 589 | 0.56, 0.015 | "Prolog Exec s43" |
| 590 | 0.21, 0.387 | "Prolog Exec s44" |
| 590 | n=21 | "n=21" |
| 592 | 0.53 +/- 0.31, 0.146 +/- 0.21 | "Prolog Exec 3-seed" |
| 595 | 0.50, 1.000, 100, 0, 0 | "Prolog ISR s42" |
| 596 | 0.38, 0.185, 0, 97.4, 0 | "Prolog ISR s43" |
| 597 | 0.97, 0.912, 0, 0, 0 | "Prolog ISR s44" |
| 599 | 0.62 +/- 0.31, 0.699 +/- 0.45 | "Prolog ISR 3-seed" |
| 605 | 38/38 | "all 38/38 proved samples are tautological" |
| 606 | 95/97 | "95/97 proved samples" |
| 606 | 100% | "Non-hacking=100%" (strict classifier, misleading) |

### ProofFOL Detailed Table (lines 611-640)

| Line | Number | Context |
|------|--------|---------|
| 620 | 0.16, 0.310, 0, 0, 100 | "ProofFOL Base" |
| 620 | n=16 | "n=16 proved" |
| 623 | ~1.0, 0.066, 100, 0, 0 | "ProofFOL Exec s42" |
| 623 | n=99 | "n=99" |
| 624 | 0.55, 0.119, 0, 49.2, 50.8 | "ProofFOL Exec s43" |
| 624 | n=63 | "n=63" |
| 625 | ~1.0, 0.043, 0, 98.6, 1.4 | "ProofFOL Exec s44" |
| 625 | n=72 | "n=72" |
| 627 | 17.4% | "17.4% genuine (mean of seeds)" |
| 630 | 0.35, 0.12, 0, 0, 100 | "ProofFOL ISR s42" |
| 630 | n=46 | "n=46" |
| 631 | ~0.47, ~0.13, 0, 69.6, 30.4 | "ProofFOL ISR s43" |
| 631 | n=56 | "n=56" |
| 632 | 0.49, 0.145, 0, 0, 100 | "ProofFOL ISR s44" |
| 632 | n=66 | "n=66" |
| 634 | 76.8% | "76.8% genuine (mean of seeds)" |
| 639 | p=0.10 | "Permutation test... p=0.10" |
| 639 | N=3 | "N=3 per group" |

### ISR Collapse Trajectory (lines 642-647)

| Line | Number | Context |
|------|--------|---------|
| 644 | 0.642 | "ISR*=0.642 at 100 steps" |
| 644 | 0.132 | "0.132 at 500 steps" |
| 644 | -79.4% | "-79.4%" |
| 644 | 0.003 | "0.003 at 1000 steps" |
| 644 | -99.5% | "-99.5% from step 100" |
| 645 | 0.32, 0.93, 0.96 | "PR increases: 0.32 -> 0.93 -> 0.96" |
| 646 | 94.8% | "94.8% of proved samples have ISR=0" |
| 646 | 18.55 | "mean component count rises to 18.55" |

### Beta=0.2 and 0.3 Table (lines 655-693)

| Line | Number | Context |
|------|--------|---------|
| 672 | 1.00, 0.602, 100, 0, 0 | "ISR b=0.2 s42" |
| 672 | n=100 | "n=100" |
| 673 | 0.96, 0.552, 96.9, 1.0, 0 | "ISR b=0.2 s43" |
| 673 | PG=2 | "PG=2" |
| 674 | 0.94, 0.964, 100, 0, 0 | "ISR b=0.2 s44" |
| 674 | n=94 | "n=94" |
| 676 | 0.97 +/- 0.03, 0.71 +/- 0.22 | "ISR b=0.2 3-seed" |
| 679 | 0.18, 0.143, 0, 77.8, 5.6 | "ISR b=0.3 s42" |
| 679 | n=18 | "n=18" |
| 679 | PG=3 | "PG=3" |
| 680 | 0.86, 0.295, 4.7, 68.6, 23.3 | "ISR b=0.3 s43" |
| 681 | 0.95, 0.742, 100, 0, 0 | "ISR b=0.3 s44" |
| 683 | 0.66 +/- 0.42, 0.39 +/- 0.31 | "ISR b=0.3 3-seed" |
| 686 | 0.48, 0.094, 8, 92, 0 | "Random b=0.3 s42" |
| 686 | TSa=4 | "TSa=4" |
| 687 | 0.92, 0.180, 7.6, 89.1, 3.3 | "Random b=0.3 s43" |
| 687 | TSa=7, n_N-H=3 | "TSa=7; n_N-H=3" |
| 688 | 0.23, 0, 0, 100, 0 | "Random b=0.3 s44" |
| 688 | n=23 | "n=23" |
| 690 | 0.54 +/- 0.35, 0.09 +/- 0.09 | "Random b=0.3 3-seed" |

### 100-Step Analysis (lines 697-704)

| Line | Number | Context |
|------|--------|---------|
| 700 | 100 | "100 training steps" |
| 700 | PR=32% | "PR=32%" |
| 700 | 13.0% | "SFT (13.0%, 3-seed pooled)" |
| 701 | 32 | "32 proved samples" |
| 701 | 9 | "9 (28.1%) exhibit TS hacking" |
| 701 | 28.1% | "28.1%" |
| 701 | 1 | "1 (3.1%) exhibits CE" |
| 701 | 3.1% | "3.1%" |
| 701 | 31.2% | "total hacking rate of 31.2%" |
| 702 | 7.7% | "SFT at comparable or lower PR shows 7.7% hacking" |
| 702 | 1/13 | "1/13 proved samples" |

### O(1) vs O(n) ISR Ablation (lines 706-728)

| Line | Number | Context |
|------|--------|---------|
| 715 | 402 | "Across 402 proved samples" |
| 715 | 1.0 | "O(1) binary signal is 1.0 for every sample" |
| 717 | ISR*=0.046 | "exec-only models average ISR*=0.046" |
| 717 | n=234 | "n=234" |
| 717 | ISR*=0.183 | "ISR-trained models average ISR*=0.183" |
| 717 | n=168 | "n=168" |
| 718 | 179 | "179 disagreements between the two signals" |
| 721 | 0.5 | "r = 0.5*r_exec + 0.5*fast_ISR" |
| 721 | PR=63% | "achieves PR=63%" |
| 721 | ISR*=0.007 | "ISR*=0.007" |
| 721 | ISR*=0.132 | "ISR*=0.132 under exec-only" |
| 721 | ISR*=0.42 | "ISR*=0.42 under O(n) ISR beta=0.1" |
| 722 | 30 pp | "depresses prove rate by 30 pp" |
| 722 | 63% | "63%" |
| 722 | 93% | "vs. 93%" |
| 726 | n+1 | "n+1 solver calls per sample" |
| 726 | mean n approx 6 | "mean n approx 6 for FOLIO" |
| 727 | ~5 ms | "Prover9 at ~5 ms per call" |
| 727 | ~55 ms | "STA evaluation adds ~55 ms per sample" |
| 727 | ~4 s | "~4 s for LLM inference" |
| 727 | <1% | "<1% overhead" |
| 728 | <2% | "<2% per training step" |

### LLaMA-3.2-3B Cold Start (lines 730-741)

| Line | Number | Context |
|------|--------|---------|
| 733 | 3B | "LLaMA-3.2-3B (3B)" |
| 733 | K=4 | "K=4" |
| 734 | 72 | "72 of 500 planned steps" |
| 734 | 500 | "500 planned steps" |
| 736 | 10 | "non-zero prove rates within 10 steps" (Qwen3-4B) |
| 736 | 3B vs 4B | "3B vs. 4B" |
| 737 | 3 | "3 epochs" |
| 737 | 2e-5 | "lr=2x10^-5" |
| 737 | PR=16% | "PR=16%" |
| 737 | n=100 | "n=100" |
| 739 | 500 | "500 steps from SFT warmstart" |
| 739 | 3 | "3 seeds" |
| 739 | PR=15.0 +/- 1.0% | "PR=15.0 +/- 1.0%" |
| 739 | n=14--16 | "n=14--16 proved per seed" |
| 739 | 86.6 +/- 0.9% | "86.6 +/- 0.9% genuine" |
| 739 | sigma_PR=1 pp | "sigma_PR=1 pp" |
| 740 | 93% | "Qwen3-4B reaches 93% PR" |
| 740 | 8% | "collapses to 8% genuine" |

### Seed-Dependent Convergence (lines 743-752)

| Line | Number | Context |
|------|--------|---------|
| 747 | 6 | "6 seeds tested (s42--s46, s52)" |
| 747 | PR=93% | "s42: PR=93%" |
| 747 | 7.5% | "genuine=7.5%" |
| 747 | PR=96% | "s44: PR=96%" |
| 747 | 0% | "genuine=0%" |
| 747 | PR=93% | "s46: PR=93% at 500 steps" |
| 747 | PR=14% | "s43: PR=14%" |
| 747 | 100% | "100% hacking at 500 steps" |
| 747 | PR=15% | "s45: PR=15%" |
| 747 | 86.7% | "genuine=86.7%" |
| 747 | PR=14% | "s52: PR=14%" |
| 747 | 85.7% | "genuine=85.7%" |
| 748 | 85--87% | "Non-converging seeds retain high genuine rates (85--87%)" |
| 749 | 1000 | "Extended training to 1000 steps for s45" |
| 749 | PR=15% | "PR=15%" |
| 749 | ISR*=0.592 | "ISR*=0.592" |
| 749 | 86.7% | "genuine=86.7%" |
| 749 | n=15 | "n=15 proved" |

### N=2 Sensitivity Analysis (lines 754-778)

| Line | Number | Context |
|------|--------|---------|
| 757 | T=0.7 | "sampling (T=0.7)" |
| 767 | 95.5 +/- 3.5 | "Exec 500-step PR=95.5 +/- 3.5%" |
| 767 | 0.357 +/- 0.318 | "ISR*=0.357 +/- 0.318" |
| 767 | 3.8 +/- 5.3 | "N-H=3.8 +/- 5.3%" |
| 768 | 98.0 +/- 2.8 | "Exec 1000-step PR=98.0 +/- 2.8%" |
| 768 | 0.003 +/- 0.001 | "ISR*=0.003 +/- 0.001" |
| 768 | 0.0 +/- 0.0 | "N-H=0.0 +/- 0.0%" |
| 769 | 85.0 +/- 5.7 | "ISR b=0.1 500-step PR=85.0 +/- 5.7%" |
| 769 | 0.659 +/- 0.344 | "ISR*=0.659 +/- 0.344" |
| 769 | 8.7 +/- 12.2 | "N-H=8.7 +/- 12.2%" |
| 776 | <=7.5% | "exec-only converges to <=7.5% non-hacking at 500 steps" |
| 776 | 0% | "0% at 1000 steps" |
| 777 | 16% | "s42: 16%" |
| 777 | 100% | "s44: 100%" |

### Qwen3-8B Results (lines 780-821)

| Line | Number | Context |
|------|--------|---------|
| 793 | K=4, K=8 | "Rollouts: 4B K=4, 8B K=8" |
| 794 | 4, 1 | "Batch size: 4B=4, 8B=1" |
| 795 | 2, 16 | "Gradient accum: 4B=2, 8B=16" |
| 796 | 8, 16 | "Effective batch: 4B=8, 8B=16" |
| 807 | 93, 7.5 | "4B K=4 s42: PR=93, Genuine=7.5" |
| 808 | 15.5 | "8B K=4 s42: PR=15.5" |
| 809 | 14, 92.9 | "8B K=8 s42: PR=14, Genuine=92.9" |
| 816 | 500 | "500 steps" |
| 816 | PR=15.5% | "PR=15.5%" |
| 817 | 40--50% | "approximately 40--50% of steps between 20--370" |
| 817 | 20--370 | "steps between 20--370" |
| 817 | PR=14% | "PR=14%" |
| 817 | n=14 | "n=14 proved" |
| 817 | ISR*=0.573 | "ISR*=0.573" |
| 817 | 92.9% | "genuine=92.9%" |
| 817 | 13/14 | "13/14" |

---

**Summary counts of unique numerical values extracted**: approximately 450+ distinct numerical entries across the 8 files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efe1c08e-09b4-44a7-a87f-c1ee3316807e",
  "isSidechain": true,
  "agentId": "a4416bb1bbbdde2b1",
  "requestId": "req_011CbPrdvmoxKEdqCBN55PGC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ae8d65e-c706-46b7-a2ae-17a71aef093d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/director_acd679de",
  "sessionId": "8f1c0800-1749-497c-a3d5-4fd006846ba8",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "enchanted-leaping-sprout",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LX7U4oTBaQFmHyk9vjZsBG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24450,
      "cache_read_input_tokens": 46297,
      "output_tokens": 18165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24450
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 18165,
          "cache_read_input_tokens": 46297,
          "cache_creation_input_tokens": 24450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24450,
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
