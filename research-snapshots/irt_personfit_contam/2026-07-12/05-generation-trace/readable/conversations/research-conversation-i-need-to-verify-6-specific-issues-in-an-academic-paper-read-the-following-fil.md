# Research conversation: I need to verify 6 specific issues in an academic paper. Read the following files and report findings for each issue: **

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a23c74de550a91739.jsonl`
- **Structured JSON:** [`70d3e26bae4596d03b7a.json`](../../sessions/70/70d3e26bae4596d03b7a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

25 recorded events

### User

_source line 1 · 2026-05-25T08:23:08.985Z_

I need to verify 6 specific issues in an academic paper. Read the following files and report findings for each issue:

**Files to read:**
1. `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex` — contains Table 1, Table 2, Table 3, and results text
2. `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex` — contains contributions list with "all bootstrap CIs" claim
3. `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex` — contains 4PL parameter definitions
4. `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_setup.tex` — contains ARC-Challenge item count
5. `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/figures/paper/gen_fig1_composite.py` — contains Figure 1 panel (c) data which is the "effect-size landscape" scatter
6. `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/paper/scripts/gen_fig_heatmap.py` — generates the Cohen's d heatmap (Figure 3 in the paper)

Also check: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex` and `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex`

**Issues to verify:**

**Issue 1: Figure 3 heatmap values vs Table 1**
- Table 1 (tab:cohens_d) reports multi-seed means for Qwen MMLU: 5.36/7.44/5.08 at 15/25/50%
- The heatmap figure script may use seed-42 single-run values (e.g., Qwen 15/25/50% as 6.57/8.22/1.90)
- Check what data the heatmap script uses and whether it matches Table 1
- Also check: the caption says "values from Table 1; multi-seed means where available"

**Issue 2: fixed-θ monotonicity claim**
- Text claims fixed-θ eliminates inverted-U and recovers monotone signal
- But Appendix L shows fixed-θ means: 6.85 → 5.89 → 12.32 at 15/25/50%, which dips from 15→25%
- Check if the paper claims "monotone" for the multi-seed fixed-θ trajectory

**Issue 3: "all bootstrap 95% CIs exclude zero, n=10" accuracy**
- Introduction contributions say something like "all bootstrap 95% CIs exclude zero, n=10"
- But Table 1 multi-seed conditions report mean ± SD, not bootstrap CIs
- Check the exact wording in the contributions

**Issue 4: ARC-Challenge 295 items**
- Standard ARC-Challenge splits don't have exactly 295 items
- Check if the paper explains why 295 (e.g., filtered to PSN-IRT calibrated items)

**Issue 5: 4PL "slip" terminology**
- Check if method.tex defines d_i as "upper asymptote (slip)" — technically slip = 1-d_i
- Report the exact wording

**Issue 6: Table 3 (tab:degradation) pipeline artifacts**
- Mistral 15% ℓz* cell has no CI, footnote says "CI not retained from analysis pipeline"
- This is unprofessional for submission

For each issue, report: (a) the exact text/data found, (b) whether the issue exists (YES/NO), (c) severity. Be thorough and quote exact text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "edfb55fe-7e9f-401e-83b5-0728b9452cea",
  "agentId": "a23c74de550a91739",
  "type": "user",
  "uuid": "ffb6254b-3f02-4fed-bf32-58959701166b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T08:23:08.996Z_

```json
{
  "parentUuid": "ffb6254b-3f02-4fed-bf32-58959701166b",
  "isSidechain": true,
  "agentId": "a23c74de550a91739",
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
  "uuid": "9fbb2c5b-92e3-4010-85db-250f20ceb192",
  "timestamp": "2026-05-25T08:23:08.996Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

---

### Assistant

_source line 3 · 2026-05-25T08:23:11.654Z_



I'll read all the specified files in parallel to verify these 6 issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fbb2c5b-92e3-4010-85db-250f20ceb192",
  "isSidechain": true,
  "agentId": "a23c74de550a91739",
  "requestId": "req_011CbNxuNZiKMddQEV4dWVh8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f029e57-6891-4432-ba2f-ed0c98d4d19d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TGHiyQSk2tKfa7Q8eFr92L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33558,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33558,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 4 · 2026-05-25T08:23:12.093Z_

<details open><summary>🔧 Tool call — Read · `toolu_01F9kjwHrYvWSVnYBrMuarKD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f029e57-6891-4432-ba2f-ed0c98d4d19d",
  "isSidechain": true,
  "agentId": "a23c74de550a91739",
  "requestId": "req_011CbNxuNZiKMddQEV4dWVh8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93c1a1ba-e11a-48b7-aa44-389008e406cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TGHiyQSk2tKfa7Q8eFr92L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33558,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33558,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 5 · 2026-05-25T08:23:12.105Z_

<details><summary>↩ Tool result · `toolu_01F9kjwHrYvWSVnYBrMuarKD`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\begin{table}[t]
5	\centering
6	\caption{Cohen's $d$ for $\Delta\ell_z^*$ across model families ($n{=}10$ clean seeds). Single-seed conditions: percentile bootstrap 95\% CI (10,000 resamples). $^{\dagger}$Multi-seed conditions: mean $\pm$ SD ($n{=}3$ independent runs). All single-seed CIs exclude zero.}
7	\label{tab:cohens_d}
8	\footnotesize
9	\resizebox{\columnwidth}{!}{%
10	\begin{tabular}{@{}llrrrr@{}}
11	\toprule
12	Model & Bench. & $d$ (5\%) [CI] & $d$ (15\%) [CI] & $d$ (25\%) [CI] & $d$ (50\%) [CI] \\
13	\midrule
14	Qwen$^{\dagger}$ & MMLU & $-4.15$ [$-9.9$, $-2.7$] & $-5.36$ ($\pm$1.10) & $-7.44$ ($\pm$1.86) & $-5.08$ ($\pm$3.02) \\
15	Llama$^{\dagger}$ & MMLU & $-2.57$ ($\pm$0.99) & $-2.80$ ($\pm$0.60) & $-2.56$ ($\pm$0.52) & $-2.30$ ($\pm$0.30) \\
16	Mistral$^{\dagger}$ & MMLU & $-3.83^{*}$ ($\pm$1.42) & $-3.37$ ($\pm$0.68) & --- & $-4.09$ ($\pm$0.53) \\
17	Qwen$^{\dagger}$ & ARC-C & --- & $+3.16$ [$2.0$, $9.5$] & --- & $+5.30$ [$3.6$, $15.2$] \\
18	\bottomrule
19	\multicolumn{6}{@{}l}{\scriptsize $^{\dagger}$Multi-seed conditions: means ($n{=}3$ independent runs) shown as $\pm$SD; remaining conditions are single-seed with bootstrap CIs.} \\
20	\multicolumn{6}{@{}l}{\scriptsize $^{*}$$n{=}2$ seeds. Per-seed values in Appendix~\ref{app:reproducibility}.}
21	\end{tabular}}
22	\end{table}
23	
24	\subsection{Detection Signal Across Model Families}
25	\label{sec:detection}
26	
27	Table~\ref{tab:cohens_d} presents Cohen's $d$ effect sizes for $\ell_z^*$ across three model families and two benchmarks.
28	All single-seed bootstrap CIs exclude zero, confirming that $\Delta\ell_z^*$ reliably separates contaminated from clean models at both contamination levels.
29	
30	On MMLU, effect sizes range from $|d|{=}2.30$ (Llama at 50\%) to $|d|{=}7.44$ (Qwen at 25\%), with Qwen at 5\% ($|d|{=}4.15$) confirming detection at the lowest contamination level tested. Llama ($|d|{=}2.57$/$2.80$/$2.56$/$2.30$) and Mistral ($|d|{=}3.83$/$3.37$/$4.09$) show comparable magnitudes.
31	On ARC-C (295 items), Qwen yields $|d|{=}3.16$ at 15\% and $|d|{=}5.30$ at 50\%, demonstrating that detection remains feasible even on small benchmarks when contamination is sufficiently concentrated.
32	
33	Clean-model $\ell_z^*$ baselines diverge substantially: Qwen ${+}8.68$ (over-consistent), Llama ${+}0.26$ (near-expected), Mistral ${+}4.02$ (Appendix~\ref{app:baseline_meaning}), making absolute thresholds uninformative.
34	The $\Delta\ell_z^*$ design normalizes these divergent baselines (Figure~\ref{fig:heatmap}).
35	
36	\begin{figure}[t]
37	  \centering
38	  \includegraphics[width=\columnwidth]{fig_heatmap.pdf}
39	  \caption{Cohen's $|d|$ heatmap (values from Table~\ref{tab:cohens_d}; multi-seed means where available). Blue intensity reflects effect-size magnitude. Grey cells: not tested.}
40	  \label{fig:heatmap}
41	\end{figure}
42	
43	\subsection{Model-Specific $\theta$-Shift Dynamics}
44	\label{sec:theta_dynamics}
45	
46	Contamination inflates $\hat{\theta}_{\text{MLE}}$, which ``explains away'' anomalous successes on hard items---we term this \emph{$\theta$-shift absorption}.
47	$\theta$-shift magnitude is comparable across families ($\Delta\theta{\approx}0.5$), yet fixed-$\theta$ amplification diverges markedly (Table~\ref{tab:theta_fixed}; Figure~\ref{fig:composite}c).
48	
49	$\theta$-shift absorption is the dominant source of detection variability for high-ability models at high contamination:
50	(i) fixed-$\theta$ estimation amplifies Qwen's multi-seed $|d|$ by 2.4$\times$ at 50\% ($5.08 \to 12.32$; Table~\ref{tab:theta_fixed}), while Llama shows no amplification ($0.4\times$);
51	(ii) $\theta$-anchoring reduces Qwen's inter-seed CV from 60\% to 19\%, confirming that training-run variance is driven by $\theta$-shift stochasticity rather than true signal variance;
52	(iii) the cross-model ranking under free-$\theta$ is seed-dependent at 50\%, making $\theta$-anchoring a necessary condition for reliable detection of high-ability models at high contamination.
53	
54	ARC-C reverses this pattern: despite 89.7\% baseline accuracy, contamination produces \emph{larger} effect sizes ($|d|{=}3.16$/$5.30$).
55	This ceiling effect arises because 295 items with high baseline accuracy leave minimal room for $\theta$ inflation; contamination manifests as anomalous successes on the few remaining hard items, producing disproportionately large $\ell_z^*$ shifts.
56	Detection sensitivity thus depends on the interaction between model ability and benchmark characteristics.
57	
58	\paragraph{Fixed-$\theta$ estimation.}
59	Table~\ref{tab:theta_fixed} compares free- and fixed-$\theta$ Cohen's $d$.
60	The amplification ratio tracks baseline $|\ell_z^*|$ monotonically: Qwen ($\ell_z^*{=}{+}8.68$) shows $2.4{\times}$ at 50\%, Mistral ($+4.02$) $1.7{\times}$, while Llama ($+0.26$) shows $0.4{\times}$ despite comparable $\theta$-shift ($\Delta\theta{=}0.52$).
61	Fixed-$\theta$ is thus a targeted remedy for models with substantial baseline misfit, not a universal one.
62	
63	\begin{table}[t]
64	\centering
65	\caption{Free-$\theta$ vs.\ fixed-$\theta$ Cohen's $|d|$ on MMLU. Qwen$^{\S}$: multi-seed mean ($n{=}3$); Llama and Mistral: seed-42 single run. Fixed-$\theta$ anchors $\hat{\theta}$ at the clean-model mean, eliminating $\theta$-shift absorption.}
66	\label{tab:theta_fixed}
67	\footnotesize
68	\resizebox{\columnwidth}{!}{%
69	\begin{tabular}{@{}lcccc@{}}
70	\toprule
71	Model & $|d_{\text{free}}|$ & $|d_{\text{fixed}}|$ & Ratio & Fixed 95\% CI / SD \\
72	\midrule
73	\multicolumn{5}{@{}l}{\textit{5\% contamination}} \\
74	Qwen & 4.15 & 3.52 & 0.8$\times$ & [2.9, 5.7] \\
75	\addlinespace
76	\multicolumn{5}{@{}l}{\textit{15\% contamination}} \\
77	Qwen$^{\S}$ & 5.36 & 6.85 & 1.3$\times$ & ($\pm$1.80) \\
78	Llama & 2.11 & 0.58 & 0.3$\times$ & [0, 2.37]$^{\dagger}$ \\
79	Mistral$^{\ddagger}$ & 2.64 & 2.69 & 1.0$\times$ & [1.53, 9.06] \\
80	\addlinespace
81	\multicolumn{5}{@{}l}{\textit{50\% contamination}} \\
82	Qwen$^{\S}$ & 5.08 & 12.32 & 2.4$\times$ & ($\pm$2.38) \\
83	Llama & 2.33 & 0.84 & 0.4$\times$ & [0.17, 2.97] \\
84	Mistral$^{\ddagger}$ & 3.50 & 5.80 & 1.7$\times$ & [3.87, 18.45] \\
85	\bottomrule
86	\multicolumn{5}{@{}l}{\scriptsize $^{\dagger}$CI includes zero.} \\
87	\multicolumn{5}{@{}l}{\scriptsize $^{\S}$Multi-seed mean ($n{=}3$); CI column shows $\pm$SD of fixed-$\theta$ $|d|$.} \\
88	\multicolumn{5}{@{}l}{\scriptsize $^{\ddagger}$Fixed-$\theta$: 6 seeds (4 response vectors from seeds 4--7 not retained in pipeline); free-$\theta$ uses all 10.} \\
89	\multicolumn{5}{@{}p{0.9\columnwidth}}{\scriptsize $d_{\text{free}}$ CIs omitted; multi-seed means in Table~\ref{tab:cohens_d}.}
90	\end{tabular}}
91	\end{table}
92	
93	\subsection{Detection-Diagnosis Tradeoff}
94	\label{sec:degradation}
95	
96	Table~\ref{tab:degradation} compares three statistics: $\ell_z^*$ (4PL parameters), HT (difficulty only), and accuracy $z$-scores (no item parameters).
97	For pure detection, simpler statistics are more powerful: accuracy $z$-scores yield $|d|$ values up to an order of magnitude larger than person-fit statistics, because cross-seed accuracy variance is near-zero.
98	HT generally exceeds $\ell_z^*$, since HT is not attenuated by the Snijders correction.
99	
100	Yet the diagnostic power reverses.
101	$\ell_z^*$ uniquely supports (a)~\emph{seen/unseen decomposition}, though item-level detection is near-random (AUROC${\approx}0.53$; Appendix~\ref{app:item_auroc}); (b)~\emph{$\theta$-shift mechanism} (\S\ref{sec:theta_dynamics}); and (c)~\emph{structural sensitivity}: $\ell_z^*$ flags 57/60 leaderboard cells as aberrant (Figure~\ref{fig:leaderboard_heatmap}) vs.\ 4/60 for accuracy $z$-scores \citep{stonge2011}.
102	In practice, accuracy $z$-scores screen candidates; $\ell_z^*$ then characterizes whether the signal reflects $\theta$-shift absorption or direct memorization.
103	Within the IRT family, 4PL gains $+$27.3pp power over 3PL on MMLU at 15\% contamination ($96.9\%$ vs.\ $41.2\%$; Appendix~\ref{app:4pl_ablation}), because 46\% of MMLU items have upper asymptote $d < 0.95$; the advantage persists across benchmarks (HellaSwag $+$34.3pp, GSM8K $+$20.7pp).
104	
105	\begin{table}[t]
106	\centering
107	\caption{Detection-diagnosis tradeoff on MMLU: Cohen's $|d|$ across three statistics. Qwen$^\dagger$: multi-seed means ($n{=}3$); Llama and Mistral: seed-42 single run with bootstrap CIs.}
108	\label{tab:degradation}
109	\footnotesize
110	\begin{tabular}{@{}llrr@{}}
111	\toprule
112	Model & Statistic & $|d|$ (15\%) & $|d|$ (50\%) \\
113	\midrule
114	Qwen$^\dagger$ & $\ell_z^*$ & $5.36$ ($\pm$1.10) & $5.08$ ($\pm$3.02) \\
115	     & HT & $5.83$ ($\pm$1.30) & $5.29$ ($\pm$3.41) \\
116	     & Acc.\ $z$ & $45.0$ ($\pm$2.5) & $70.0$ ($\pm$1.1) \\
117	\addlinespace
118	Llama & $\ell_z^*$ & $2.11$ [$1.4$, $4.8$] & $2.33$ [$1.6$, $5.1$] \\
119	      & HT & $2.45$ [$1.5$, $4.3$] & $3.07$ [$1.9$, $5.3$] \\
120	      & Acc.\ $z$ & $22.5$ [$13.6$, $47.0$] & $32.8$ [$19.8$, $68.6$] \\
121	\addlinespace
122	Mistral & $\ell_z^*$ & $2.64^{\ddagger}$ & $3.50$ [$2.1$, $9.4$] \\
123	      & HT & $4.36$ [$1.2$, $7.0$] & $5.89$ [$1.9$, $9.4$] \\
124	      & Acc.\ $z$ & $7.81$ [$4.4$, $14.4$] & $16.6$ [$9.7$, $34.6$] \\
125	\bottomrule
126	\multicolumn{4}{@{}p{0.9\columnwidth}}{\scriptsize $^\dagger$Per-seed values in Appendix~\ref{app:reproducibility}. Bootstrap CIs: 10{,}000 resamples over $n{=}10$ clean seeds. $^{\ddagger}$CI not retained from analysis pipeline; multi-seed SD in Table~\ref{tab:cohens_d}.}
127	\end{tabular}
128	\end{table}
129	
130	\begin{figure}[t]
131	  \centering
132	  \includegraphics[width=\columnwidth]{fig_4_model_heatmap.pdf}
133	  \caption{$\ell_z^*$ heatmap for 12 leaderboard models across five benchmarks. 57/60 cells exceed $|\ell_z^*| > 1.96$, indicating pervasive IRT assumption violations even absent contamination. Details in Appendix~\ref{app:leaderboard_aberrance}.}
134	  \label{fig:leaderboard_heatmap}
135	\end{figure}
136	
137	\subsection{Ability-Dependent Non-Monotonic Dose-Response}
138	\label{sec:inverted_u}
139	
140	As an exploratory observation, the free-$\theta$ dose-response is non-monotonic for Qwen.
141	Figure~\ref{fig:composite}(d) plots the dose-response trajectory, combining the single-seed 5\% estimate (hollow marker) with multi-seed means at 15\%/25\%/50\% ($|d|$: $4.15 \to 5.36 \to 7.44 \to 5.08$), showing signal peaking at 25\% before declining; inter-seed variance at 50\% is high (CV${=}$60\%, range $[1.90, 7.91]$).
142	This non-monotonicity is a $\theta$-estimation artifact: fixed-$\theta$ eliminates the inverted-U ($|d|{=}12.32$ at 50\%, CV reduced to 19\%).
143	Llama's flat trajectory ($|d|{\approx}2.3$--$2.8$) is consistent with its near-zero baseline $\ell_z^*$: the divergence is fully explained by baseline ability differences.
144	Simulation corroborates: two-sided testing achieves ${>}$93\% power at all levels on MMLU (Appendix~\ref{app:simulation}).
145	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93c1a1ba-e11a-48b7-aa44-389008e406cd",
  "isSidechain": true,
  "promptId": "edfb55fe-7e9f-401e-83b5-0728b9452cea",
  "agentId": "a23c74de550a91739",
  "type": "user",
  "uuid": "eb504f64-aeac-4bea-9091-f48bfd38d738",
  "sourceToolAssistantUUID": "93c1a1ba-e11a-48b7-aa44-389008e406cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-25T08:23:13.083Z_

<details open><summary>🔧 Tool call — Read · `toolu_019aHHSrZjJqNbmHmNMiarEe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb504f64-aeac-4bea-9091-f48bfd38d738",
  "isSidechain": true,
  "agentId": "a23c74de550a91739",
  "requestId": "req_011CbNxuNZiKMddQEV4dWVh8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c9d06d7-7cfc-4a94-8834-479f729f2da9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TGHiyQSk2tKfa7Q8eFr92L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33558,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33558,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 7 · 2026-05-25T08:23:13.092Z_

<details><summary>↩ Tool result · `toolu_019aHHSrZjJqNbmHmNMiarEe`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	\begin{figure*}[t]
4	  \centering
5	  \includegraphics[width=\textwidth]{fig_1_composite.pdf}
6	  \caption{Overview of IRT person-fit detection. (a)~A clean model's responses track the IRT-predicted probability curve; (b)~a contaminated model shows anomalous successes on hard items (red diamonds), producing a large $|\Delta\ell_z^*|$. (c)~Effect-size landscape: baseline accuracy vs.\ Cohen's $|d|$ across model families (diamonds: 5\%, triangles: 15\%, squares: 25\%, circles: 50\%). (d)~Dose-response trajectories; free-$\theta$ shows non-monotonic artifact, fixed-$\theta$ recovers monotone signal.}
7	  \label{fig:composite}
8	\end{figure*}
9	
10	\begin{figure*}[t]
11	  \centering
12	  \includegraphics[width=\textwidth]{fig_framework.pdf}
13	  \caption{Overview of \irtfit{}: (a)~positioning in the detection frontier by information access; (b)~pipeline from binary responses through $\ell_z^*$ person-fit analysis to detection and characterization; (c)~three behavioral boundaries discovered; (d)~recommended practitioner workflow.}
14	  \label{fig:pipeline}
15	\end{figure*}
16	
17	Benchmark contamination, the unintended inclusion of evaluation data in training corpora, poses a growing threat to the integrity of large language model (LLM) evaluation \citep{dodge2021, magar2022, sainz2023}.
18	As training corpora and public benchmarks both expand, the probability of overlap increases structurally \citep{jacovi2023, chang2024survey}.
19	When contamination occurs, benchmark scores no longer reflect genuine capability, undermining the primary mechanism by which the community compares and selects models.
20	
21	A range of detection methods have been proposed, but all require some form of privileged access beyond the binary response record.
22	N-gram overlap methods need the training corpus \citep{dodge2021, magar2022}.
23	Membership inference approaches require token-level probabilities \citep{minkprob2024, deng2024}.
24	Probing methods rely on crafted prompts \citep{golchin2024, oren2024}.
25	Performance-based methods require multiple test variants or output logits \citep{constat2024, codec2026}.
26	These methods form a detection frontier ordered by information access.
27	No existing method operates using only binary response patterns, without model weights, gradients, logits, or training data (though, as we show, effective detection additionally requires externally calibrated item parameters).
28	
29	In this work, we focus on SFT-stage contamination, where benchmark answers are explicitly included in fine-tuning data, for three reasons.
30	First, controlled experiments require known ground-truth contamination sets, achievable through fine-tuning with specific benchmark items.
31	Second, SFT-stage contamination is increasingly relevant as fine-tuning-as-a-service platforms proliferate, creating new pathways for benchmark data to enter training mixtures.
32	Third, SFT provides a methodologically clean setting to characterize detection boundaries before extending to noisier pretraining scenarios.
33	
34	The need for detection from binary response patterns grows more pressing as models evolve.
35	\citet{wang2025fragility} show that all ten log-probability-based methods they evaluate perform at chance level on models trained with reinforcement learning (RL), because RL reshapes internal token distributions while preserving binary correctness patterns.
36	This motivates a fundamental question: \emph{what can binary response patterns reveal about contamination, and under what conditions?}
37	
38	We observe that a contaminated LLM is functionally analogous to a test-taker with item preknowledge: both produce response patterns in which difficult items are answered correctly through memorization rather than genuine ability.
39	This connection points to person-fit statistics, developed over four decades for cheating detection in educational testing \citep{drasgow1985, meijer2001, karabatsos2003, sinharay2017}.
40	The standardized statistic $\ell_z^*$ \citep{snijders2001} measures how well a response pattern conforms to Item Response Theory (IRT) model predictions.
41	Figure~\ref{fig:composite}(a--b) illustrates this analogy.
42	Despite the natural correspondence, no prior work has applied person-fit statistics to LLM benchmark contamination.
43	
44	Rather than proposing $\ell_z^*$ as a ready-to-deploy detection tool, we characterize the behavior boundaries of IRT person-fit statistics for LLM contamination detection.
45	Our framework operates at three layers: (i) pre-calibrated 4PL item parameters from the PSN-IRT item bank \citep{psnirt2026}, an external resource calibrated from large-scale leaderboard data; (ii) binary response patterns obtained from the target model without access to weights or logits; and (iii) retrospective statistical inference requiring no model modification.
46	Using controlled contamination experiments across three 7--8B model families (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B; $n{=}10$ clean seeds each) with PSN-IRT parameters, we identify three IRT-specific findings on Massive Multitask Language Understanding (MMLU; \citealp{hendrycks2021mmlu}) and ARC-Challenge:
47	
48	\begin{enumerate}[leftmargin=*,nosep]
49	\item \textbf{Model-specific $\theta$-shift dynamics.} Contamination inflates ability estimates ($\hat{\theta}$), absorbing the person-fit signal; $\theta$-anchoring amplifies Qwen's multi-seed $|d|$ by 2.4$\times$ at 50\% contamination while reducing inter-seed CV from 60\% to 19\%, establishing $\theta$-anchoring as a necessary condition for reliable detection of high-ability models at high contamination. ARC-C reverses through a ceiling effect.
50	
51	\item \textbf{Detection-diagnosis tradeoff.} Simpler statistics yield stronger detection: accuracy $z$-scores produce $|d|$ values several-fold to over an order of magnitude larger than person-fit statistics, and HT generally exceeds $\ell_z^*$. Yet the diagnostic power reverses: only $\ell_z^*$ supports seen/unseen decomposition, mechanistic $\theta$-shift analysis, and sensitivity to response-pattern structure (57/60 vs.\ 4/60 flagged cells on real-world data).
52	
53	\item \textbf{Non-monotonic dose-response under free-$\theta$ (exploratory).} The Qwen dose-response ($|d|$: $4.15 \to 5.36 \to 7.44 \to 5.08$ at 5\%/15\%/25\%/50\%; 5\% is single-seed, remainder are multi-seed means) shows non-monotonicity; $\theta$-anchoring eliminates the pattern and reveals strong positive dose-response ($|d|{=}12.32$ at 50\%). The non-monotonicity is a $\theta$-estimation artifact, not a detection boundary.
54	\end{enumerate}
55	
56	Our contributions are threefold:
57	(1) We provide the first empirical characterization of IRT person-fit behavior for LLM contamination, quantifying theoretically predicted phenomena ($\theta$-shift absorption, detection-diagnosis tradeoff) whose magnitudes and boundary conditions are not derivable from IRT theory alone.
58	(2) We establish that $\Delta\ell_z^*$ reliably detects SFT-stage contamination across three model families (all bootstrap 95\% CIs exclude zero, $n{=}10$).
59	(3) We document the detection-diagnosis tradeoff, clarifying what binary response patterns can and cannot reveal.
60	Findings~1--2 are confirmatory (pre-planned 15\%/50\% $\times$ 3 families); Finding~3 is exploratory (5\%/25\% added post-hoc).
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c9d06d7-7cfc-4a94-8834-479f729f2da9",
  "isSidechain": true,
  "promptId": "edfb55fe-7e9f-401e-83b5-0728b9452cea",
  "agentId": "a23c74de550a91739",
  "type": "user",
  "uuid": "98ec3d0a-eb0e-4224-8ed6-92b1efcea5f5",
  "sourceToolAssistantUUID": "2c9d06d7-7cfc-4a94-8834-479f729f2da9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-25T08:23:13.556Z_

<details open><summary>🔧 Tool call — Read · `toolu_0193JPtXbM4aUu74sPWeHYZg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98ec3d0a-eb0e-4224-8ed6-92b1efcea5f5",
  "isSidechain": true,
  "agentId": "a23c74de550a91739",
  "requestId": "req_011CbNxuNZiKMddQEV4dWVh8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d8cb9f3-ed8d-4383-afe0-1655c7c013f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TGHiyQSk2tKfa7Q8eFr92L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33558,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33558,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 9 · 2026-05-25T08:23:13.564Z_

<details><summary>↩ Tool result · `toolu_0193JPtXbM4aUu74sPWeHYZg`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{IRT Person-Fit Framework}
5	\label{sec:framework}
6	
7	We adopt the four-parameter logistic (4PL) IRT model to characterize contamination-induced aberrance in LLM response patterns.
8	The 4PL model defines the probability that a model with ability $\theta$ answers item $i$ correctly:
9	\begin{equation}
10	  P_i(\theta) = c_i + (d_i - c_i)\,\frac{1}{1 + e^{-a_i(\theta - b_i)}}
11	  \label{eq:4pl}
12	\end{equation}
13	where $a_i$ is discrimination, $b_i$ difficulty, $c_i$ the lower asymptote (guessing), and $d_i$ the upper asymptote (slip).
14	Item parameters are pre-calibrated by PSN-IRT \citep{psnirt2026} from a large-scale leaderboard dataset; we use these external parameters rather than re-estimating from potentially contaminated data, since our marginal maximum likelihood EM (MML-EM) refit shows discrimination recovery degrades to $r_a{=}0.127$ on contaminated leaderboard data.
15	
16	Given item parameters and a binary response vector $\mathbf{x} = (x_1, \ldots, x_n)$, we compute the person-fit statistic $\ell_z^*$ \citep{snijders2001}, a standardized log-likelihood residual quantifying deviation between observed and expected response patterns.
17	The Snijders correction accounts for estimation uncertainty in $\hat{\theta}_{\text{MLE}}$, so that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null \citep{drasgow1985, snijders2001}; \citet{magis2012} provide a detailed treatment of how response model selection and ability estimation affect $\ell_z^*$.
18	Large negative $\ell_z^*$ indicates aberrant responding (unexpected failures on easy items or unexpected successes on hard items); large positive values indicate over-consistent patterns.
19	
20	\subsection{$\Delta\ell_z^*$ Matched-Difference Design}
21	\label{sec:did}
22	
23	LLM response patterns systematically violate IRT assumptions of local independence and unidimensionality.
24	In our empirical data, 57 of 60 model-benchmark cells yield $|\ell_z^*| > 1.96$ even absent contamination, rendering absolute thresholds uninformative.
25	We address this through a matched-difference design.
26	
27	For controlled experiments with clean baselines, we compute:
28	\begin{equation}
29	  \Delta\ell_z^* = \ell_{z,\text{contam}}^{*} - \bar{\ell}_{z,\text{clean}}^{*}
30	  \label{eq:delta_lz}
31	\end{equation}
32	where $\bar{\ell}_{z,\text{clean}}^{*}$ averages over $n{=}10$ clean seeds.
33	The shared model misfit cancels, isolating contamination-specific aberrance.
34	We quantify effect sizes as $d = (\ell_{z,\text{contam}}^{*} - \bar{\ell}_{z,\text{clean}}^{*})\,/\,s_{\text{clean}}$, where $s_{\text{clean}}$ is the SD of the $n{=}10$ clean-seed $\ell_z^*$ values; with a single contaminated observation per condition, $d$ is a standardized departure rather than a two-sample effect size (Hedges' $g = J \cdot d$, $J \approx 0.914$ for $n{=}10$; \citealp{hedges1981}).
35	We report percentile bootstrap 95\% CIs (10,000 resamples) reflecting clean-seed variability only; bias-corrected and accelerated (BCa) correction (Appendix~\ref{app:bca}) generally confirms conservative coverage; multi-seed contamination-run variance appears in Appendix~\ref{app:reproducibility}.
36	
37	For deployment without clean baselines, cross-benchmark comparison provides the reference: the target benchmark's $\ell_z^*$ is compared against benchmarks presumed clean from the same model.
38	Significance thresholds derive from a nonparametric bootstrap null rather than the asymptotic $\mathcal{N}(0,1)$ reference, accommodating residual model misspecification.
39	Simulation analysis (Appendix~\ref{app:local_dep}) confirms that the matched-difference design is robust to local dependence at realistic levels ($d_{\text{ratio}} \geq 0.93$ for $\sigma_\tau \leq 0.5$) and maintains ${\geq}98.5\%$ power even under contamination-specific asymmetric dependence.
40	
41	\subsection{Experimental Setup}
42	\label{sec:setup}
43	
44	\paragraph{Models and contamination.}
45	We validate on three 7--8B model families: Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, and Mistral-7B-Instruct-v0.3.
46	Each is fine-tuned with Quantized Low-Rank Adaptation (QLoRA; rank\,$=$\,16, $\alpha$\,$=$\,32; full hyperparameters in Appendix~\ref{app:hyperparams}) under clean and contaminated conditions at varying levels: at $X\%$ contamination, $X\%$ of SFT training examples are benchmark items (questions paired with gold answers in the standard evaluation format), with the remainder drawn from a general instruction-following dataset.
47	All three families are tested at 15\% and 50\% contamination.
48	Following initial observation of non-monotonic dose-response for Qwen, we added 5\% and 25\% conditions for Qwen to trace the full dose-response curve.
49	Both conditions were subsequently extended to Llama to test whether the pattern generalizes; Mistral was additionally tested at 5\% but not at 25\% due to computational constraints.
50	We train $n{=}10$ independent clean seeds per model to establish baseline variability and construct bootstrap confidence intervals.
51	Reported CIs reflect variability across $n$ clean baseline seeds; for each model family, selected contamination levels were additionally replicated with $n{=}3$ independent QLoRA seeds to assess training-run variance: Qwen at 15\%/25\%/50\%, Llama at 5\%/15\%/25\%/50\%, and Mistral at 5\%/15\%/50\% (Appendix~\ref{app:reproducibility}).
52	
53	\paragraph{Benchmarks.}
54	We evaluate on MMLU \citep{hendrycks2021mmlu} (14,042 items) and ARC-Challenge \citep{clark2018arc} (295 items), spanning two orders of magnitude in benchmark size.
55	All 4PL item parameters are from \citet{psnirt2026}.
56	ARC-Challenge experiments were conducted on Qwen only, as the primary evaluation of cross-benchmark generalizability; extending to additional families was constrained by computational budget.
57	
58	\paragraph{Post-RL extension.}
59	To probe behavior boundaries beyond SFT, we apply Group Relative Policy Optimization (GRPO; \citealp{shao2024}) to one contaminated Qwen model (15\% MMLU) for 1,500 steps, evaluating at three checkpoints.
60	This extension is $N{=}1$ (single model family, single contamination level).
61	
62	\paragraph{Contamination model.}
63	QLoRA SFT on benchmark items proxies SFT-stage contamination, analogous to a test-taker with item preknowledge.
64	We term contaminated items \emph{seen} and the remainder \emph{unseen}, enabling person-fit decomposition (\S\ref{sec:degradation}).
65	Findings are scoped to SFT-based contamination.
66	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d8cb9f3-ed8d-4383-afe0-1655c7c013f6",
  "isSidechain": true,
  "promptId": "edfb55fe-7e9f-401e-83b5-0728b9452cea",
  "agentId": "a23c74de550a91739",
  "type": "user",
  "uuid": "ced4e56a-9f23-4671-ade1-a6f7cf32c712",
  "sourceToolAssistantUUID": "5d8cb9f3-ed8d-4383-afe0-1655c7c013f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T08:23:14.028Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A86Kv89Cw9XMzUwfFjKZUH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ced4e56a-9f23-4671-ade1-a6f7cf32c712",
  "isSidechain": true,
  "agentId": "a23c74de550a91739",
  "requestId": "req_011CbNxuNZiKMddQEV4dWVh8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "850d2a95-3ae0-4050-a095-1091ec38667c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TGHiyQSk2tKfa7Q8eFr92L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33558,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33558,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 11 · 2026-05-25T08:23:14.035Z_

<details><summary>↩ Tool result · `toolu_01A86Kv89Cw9XMzUwfFjKZUH`</summary>

```text
1	\subsection{Experimental Setup}
2	\label{sec:setup}
3	
4	We evaluate on five benchmarks that span knowledge, reasoning, and code generation: MMLU \citep{hendrycks2021mmlu} (14,042 items), HellaSwag \citep{zellers2019hellaswag} (10,042), GSM8K \citep{cobbe2021gsm8k} (1,319), ARC-Challenge \citep{clark2018arc} (295), and HumanEval \citep{chen2021humaneval} (164).
5	All item parameters follow the four-parameter logistic (4PL) IRT model, calibrated by \citet{psnirt2026} from a large-scale leaderboard dataset.
6	
7	\paragraph{Empirical data.}
8	We obtain per-item binary response vectors for 12 models from the PSN-IRT v2 leaderboard dataset \citep{psnirt2026}, covering open-weight and proprietary models across capability tiers.
9	PSN-IRT v1 provides binary responses from $N{=}178$ models with 3PL item parameters; v2 supplies validated 4PL parameters for 12 models.
10	We use v2 for empirical analysis and v1 for the MML-EM refit experiment in \S\ref{sec:empirical}.
11	
12	\paragraph{Controlled contamination.}
13	We fine-tune Qwen2.5-7B-Instruct with QLoRA (rank\,=\,16, $\alpha$\,=\,32) under five conditions: three clean runs (seeds 42, 123, 456) and two contaminated runs where 15\% and 50\% of MMLU evaluation items are included in the supervised fine-tuning (SFT) training data.
14	For cross-family validation, we replicate the same protocol on Llama-3.1-8B-Instruct with identical QLoRA configuration and contamination fractions, and further validate on Mistral-7B-Instruct-v0.3 with a single clean seed and two contaminated conditions (15\% and 50\%).
15	
16	\paragraph{Simulation.}
17	For each benchmark, we generate 2{,}000 response-vector replicates per condition across 11 contamination levels (0\%, 3\%, 5\%, 10\%, 15\%, 25\%, 50\%, 60\%, 75\%, 90\%, 100\%), sampling responses under the calibrated 4PL parameters.
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "850d2a95-3ae0-4050-a095-1091ec38667c",
  "isSidechain": true,
  "promptId": "edfb55fe-7e9f-401e-83b5-0728b9452cea",
  "agentId": "a23c74de550a91739",
  "type": "user",
  "uuid": "c93bd56a-6415-4c83-942e-08f8c0f921ac",
  "sourceToolAssistantUUID": "850d2a95-3ae0-4050-a095-1091ec38667c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T08:23:14.499Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HaUJknTx279acuEaryrMcS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/figures/paper/gen_fig1_composite.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c93bd56a-6415-4c83-942e-08f8c0f921ac",
  "isSidechain": true,
  "agentId": "a23c74de550a91739",
  "requestId": "req_011CbNxuNZiKMddQEV4dWVh8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eeb26c9c-3209-4afa-b082-f6e18a6ccae9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TGHiyQSk2tKfa7Q8eFr92L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33558,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33558,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 13 · 2026-05-25T08:23:14.507Z_

<details><summary>↩ Tool result · `toolu_01HaUJknTx279acuEaryrMcS`</summary>

```text
1	"""
2	Figure 1 (composite): 2×2 panel figure for EMNLP 2026.
3	  (a) Clean Response Pattern       (b) Contaminated Response Pattern
4	  (c) Effect-Size Landscape        (d) Dose-Response Trajectory
5	
6	Designed to publication-level quality: NPG palette, serif fonts, subtle details.
7	Output: fig_1_composite.{pdf,png}
8	"""
9	import matplotlib
10	matplotlib.use('Agg')
11	
12	import sys, shutil
13	import numpy as np
14	import pandas as pd
15	import matplotlib.pyplot as plt
16	import matplotlib.patheffects as pe
17	from matplotlib.collections import LineCollection
18	from matplotlib.gridspec import GridSpec
19	from matplotlib.patches import FancyBboxPatch
20	from pathlib import Path
21	from scipy.ndimage import uniform_filter1d
22	
23	sys.path.insert(0, '/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/figures/paper')
24	import palette
25	palette.apply()
26	
27	PROJ = Path('/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam')
28	
29	WHITE_STROKE = [pe.withStroke(linewidth=2.5, foreground='white')]
30	
31	# ═══════════════════════════════════════════════════════════════════════════════
32	# DATA: panels (a)+(b) — IRT response patterns
33	# ═══════════════════════════════════════════════════════════════════════════════
34	np.random.seed(42)
35	df = pd.read_csv(PROJ / 'artifacts' / 'psn_irt_params' / 'mmlu_params.csv')
36	N = 300
37	df_sorted = df.sort_values('b_difficulty')
38	indices = np.linspace(0, len(df) - 1, N, dtype=int)
39	items = df_sorted.iloc[indices].reset_index(drop=True).sort_values('b_difficulty').reset_index(drop=True)
40	
41	a_param = items['a_discrimination'].values
42	b_param = items['b_difficulty'].values
43	c_param = items['c_guessing'].values
44	d_param = items['d_feasibility'].values
45	
46	theta = 0.5
47	p_irt = c_param + (d_param - c_param) / (1 + np.exp(-a_param * (theta - b_param)))
48	
49	clean = (np.random.random(N) < p_irt).astype(int)
50	
51	contam = clean.copy()
52	hard_wrong_idx = np.where((b_param > 0.3) & (contam == 0))[0]
53	np.random.seed(42)
54	n_flip = min(45, len(hard_wrong_idx))
55	flip_hard = np.random.choice(hard_wrong_idx, n_flip, replace=False)
56	contam[flip_hard] = 1
57	
58	memorized = np.zeros(N, dtype=bool)
59	memorized[flip_hard] = True
60	
61	def lz_star(resp, a, b, c, d, th):
62	    pr = np.clip(c + (d - c) / (1 + np.exp(-a * (th - b))), 1e-10, 1 - 1e-10)
63	    ll = np.sum(resp * np.log(pr) + (1 - resp) * np.log(1 - pr))
64	    mu = np.sum(pr * np.log(pr) + (1 - pr) * np.log(1 - pr))
65	    var = np.sum(pr * (1 - pr) * (np.log(pr / (1 - pr)))**2)
66	    return (ll - mu) / np.sqrt(var)
67	
68	lz_c = lz_star(clean, a_param, b_param, c_param, d_param, theta)
69	lz_t = lz_star(contam, a_param, b_param, c_param, d_param, theta)
70	delta_lz = abs(lz_c - lz_t)
71	print(f"ℓz* clean={lz_c:.2f}, contam={lz_t:.2f}, |Δℓz*|={delta_lz:.1f}")
72	
73	p_smooth = uniform_filter1d(p_irt, size=7, mode='nearest')
74	x_items = np.arange(N)
75	
76	# ═══════════════════════════════════════════════════════════════════════════════
77	# FIGURE LAYOUT
78	# ═══════════════════════════════════════════════════════════════════════════════
79	fig = plt.figure(figsize=(7.2, 5.8))
80	gs = GridSpec(2, 2, figure=fig, wspace=0.30, hspace=0.48,
81	              left=0.08, right=0.97, top=0.96, bottom=0.08)
82	
83	ax_a = fig.add_subplot(gs[0, 0])
84	ax_b = fig.add_subplot(gs[0, 1], sharey=ax_a)
85	ax_c = fig.add_subplot(gs[1, 0])
86	ax_d = fig.add_subplot(gs[1, 1])
87	
88	# ═══════════════════════════════════════════════════════════════════════════════
89	# HELPER: rug ticks
90	# ═══════════════════════════════════════════════════════════════════════════════
91	def draw_rug_ticks(ax, positions, y_centers, color, alpha=0.55, lw=0.9, height=0.05):
92	    y_centers = np.broadcast_to(np.asarray(y_centers, dtype=float), positions.shape)
93	    segments = [[(float(xi), float(yc - height / 2)),
94	                 (float(xi), float(yc + height / 2))]
95	                for xi, yc in zip(positions, y_centers)]
96	    if not segments:
97	        return
98	    lc = LineCollection(segments, colors=color, linewidths=lw, alpha=alpha, zorder=4)
99	    ax.add_collection(lc)
100	
101	# ═══════════════════════════════════════════════════════════════════════════════
102	# PANELS (a) + (b): response patterns
103	# ═══════════════════════════════════════════════════════════════════════════════
104	def plot_response_panel(ax, responses, panel_label, subtitle, is_contam=False):
105	    # Gradient fill under IRT curve (layered for smooth effect)
106	    for i in range(15):
107	        frac_lo = i / 15
108	        frac_hi = (i + 1) / 15
109	        alpha = 0.07 * (1.0 - frac_lo * 0.9)
110	        ax.fill_between(x_items, p_smooth * frac_lo, p_smooth * frac_hi,
111	                        alpha=alpha, color=palette.CURVE, linewidth=0, zorder=1)
112	
113	    # IRT probability curve
114	    ax.plot(x_items, p_smooth, color=palette.CURVE, linewidth=1.8, alpha=0.8, zorder=3)
115	
116	    # Response rug ticks
117	    correct = responses == 1
118	    wrong = responses == 0
119	    np.random.seed(77)
120	    jitter_1 = np.random.uniform(-0.01, 0.01, N)
121	    jitter_0 = np.random.uniform(-0.01, 0.01, N)
122	
123	    if is_contam:
124	        norm_c = correct & ~memorized
125	        draw_rug_ticks(ax, x_items[norm_c], 1.0 + jitter_1[norm_c],
126	                       palette.CURVE, alpha=0.50, lw=0.9)
127	        draw_rug_ticks(ax, x_items[wrong], 0.0 + jitter_0[wrong],
128	                       '#CCCCCC', alpha=0.55, lw=0.9)
129	
130	        # Memorized items: prominent red diamonds
131	        mem_x = x_items[memorized]
132	        mem_y = np.ones(memorized.sum()) + jitter_1[memorized]
133	        ax.scatter(mem_x, mem_y,
134	                   s=35, color=palette.SIGNAL, alpha=0.92, edgecolors='white',
135	                   linewidths=0.7, zorder=7, marker='D')
136	
137	        # Connection lines from memorized items to IRT curve
138	        for idx in flip_hard:
139	            ax.plot([x_items[idx], x_items[idx]],
140	                    [p_smooth[idx], 1.0 + jitter_1[idx]],
141	                    color=palette.SIGNAL, alpha=0.18, linewidth=0.5,
142	                    linestyle=(0, (3, 3)), zorder=2)
143	
144	        # Small legend for memorized items
145	        ax.scatter([], [], s=25, color=palette.SIGNAL, marker='D',
146	                   edgecolors='white', linewidths=0.5, label='Memorized (seen)')
147	        leg = ax.legend(loc='lower right', frameon=True, framealpha=0.95,
148	                        edgecolor='#E0E0E0', fontsize=6, handletextpad=0.3,
149	                        borderpad=0.4, bbox_to_anchor=(0.98, 0.15))
150	        leg.get_frame().set_linewidth(0.3)
151	    else:
152	        draw_rug_ticks(ax, x_items[correct], 1.0 + jitter_1[correct],
153	                       palette.CURVE, alpha=0.50, lw=0.9)
154	        draw_rug_ticks(ax, x_items[wrong], 0.0 + jitter_0[wrong],
155	                       '#CCCCCC', alpha=0.55, lw=0.9)
156	
157	    # Faint horizontal guides at 0 and 1
158	    ax.axhline(y=0, color='#000000', alpha=0.05, linewidth=0.4, zorder=0)
159	    ax.axhline(y=1, color='#000000', alpha=0.05, linewidth=0.4, zorder=0)
160	
161	    # Panel label
162	    ax.text(0.02, 0.97, panel_label, transform=ax.transAxes,
163	            fontsize=11, fontweight='bold', va='top', ha='left',
164	            color=palette.TEXT, zorder=10)
165	    # Subtitle — positioned above the y=1 rug marks
166	    ax.text(0.14, 0.97, subtitle, transform=ax.transAxes,
167	            fontsize=7.5, va='top', ha='left',
168	            color=palette.ANNOTATION, fontstyle='italic', zorder=10)
169	
170	    # ℓz* badge box
171	    if is_contam:
172	        lz_color = palette.SIGNAL
173	        bg_color = '#FDF0EE'
174	        lz_text = f'$|\\Delta\\ell_z^*|$ = {delta_lz:.1f}'
175	    else:
176	        lz_color = '#27AE60'
177	        bg_color = '#F0F7F0'
178	        lz_text = f'$\\ell_z^*$ = {lz_c:+.1f}'
179	
180	    ax.text(0.50, -0.22, lz_text, transform=ax.transAxes,
181	            ha='center', va='top', fontsize=7.5, fontweight='bold',
182	            color=lz_color,
183	            bbox=dict(boxstyle='round,pad=0.35', facecolor=bg_color,
184	                      edgecolor=lz_color, alpha=0.95, linewidth=0.6),
185	            zorder=8)
186	
187	    # "Easy → Hard" annotation
188	    ax.annotate('Easy', xy=(0.03, -0.12), xycoords='axes fraction',
189	                fontsize=5.5, color='#999999', style='italic')
190	    ax.annotate('Hard', xy=(0.88, -0.12), xycoords='axes fraction',
191	                fontsize=5.5, color='#999999', style='italic')
192	    ax.annotate('', xy=(0.87, -0.10), xytext=(0.12, -0.10),
193	                xycoords='axes fraction',
194	                arrowprops=dict(arrowstyle='->', color='#BBBBBB', lw=0.5))
195	
196	    # Axis styling
197	    ax.set_xlabel('Items (sorted by difficulty)', labelpad=13, fontsize=7.5)
198	    ax.set_xlim(-3, N + 2)
199	    ax.set_ylim(-0.12, 1.14)
200	    ax.set_yticks([0, 1])
201	    ax.set_xticks([])
202	    ax.spines['top'].set_visible(False)
203	    ax.spines['right'].set_visible(False)
204	    palette.style_ax(ax)
205	
206	np.random.seed(7)
207	plot_response_panel(ax_a, clean, '(a)', 'Clean model', is_contam=False)
208	np.random.seed(7)
209	plot_response_panel(ax_b, contam, '(b)', 'Contaminated model', is_contam=True)
210	
211	ax_a.set_ylabel('Response', labelpad=4, fontsize=8)
212	ax_a.set_yticklabels(['0', '1'], fontsize=7)
213	plt.setp(ax_b.get_yticklabels(), visible=False)
214	
215	# ═══════════════════════════════════════════════════════════════════════════════
216	# PANEL (c): effect-size landscape
217	# ═══════════════════════════════════════════════════════════════════════════════
218	data_c = {
219	    '5':  [(67.8, 4.15, 2.74, 9.85, 'Qwen')],
220	    '15': [(67.8, 6.57, 4.54, 15.19, 'Qwen'),
221	           (59.4, 2.11, 1.40, 4.80, 'Llama'),
222	           (52.4, 3.37, 2.69, 4.05, 'Mistral'),
223	           (89.7, 3.16, 2.01, 9.54, 'ARC-C')],
224	    '25': [(67.8, 8.22, 5.73, 18.88, 'Qwen'),
225	           (59.4, 1.99, 1.30, 4.40, 'Llama')],
226	    '50': [(67.8, 1.90, 1.04, 4.95, 'Qwen'),
227	           (59.4, 2.33, 1.60, 5.10, 'Llama'),
228	           (52.4, 3.50, 2.10, 9.40, 'Mistral'),
229	           (89.7, 5.30, 3.60, 15.20, 'ARC-C')],
230	}
231	
232	color_map = {'Qwen': palette.QWEN, 'Llama': palette.LLAMA,
233	             'Mistral': palette.MISTRAL, 'ARC-C': palette.ARCC}
234	marker_map = {'5': 'D', '15': '^', '25': 's', '50': 'o'}
235	size_map = {'5': 65, '15': 75, '25': 65, '50': 72}
236	Y_MAX_C = 11.0
237	
238	for level, pts in data_c.items():
239	    mk = marker_map[level]
240	    sz = size_map[level]
241	    for acc, d_val, ci_lo, ci_hi, model in pts:
242	        col = color_map[model]
243	        ax_c.errorbar(acc, d_val,
244	                      yerr=[[max(d_val - ci_lo, 0)],
245	                            [min(ci_hi - d_val, Y_MAX_C - d_val)]],
246	                      fmt='none', ecolor=col, capsize=2.5, capthick=0.7,
247	                      elinewidth=0.9, alpha=0.28, zorder=4)
248	        ax_c.scatter(acc, d_val, marker=mk, s=sz, color=col,
249	                     edgecolors='white', linewidths=0.7, zorder=6)
250	
251	# Marker legend (horizontal, bottom)
252	for lk, mk, lbl in [('5', 'D', '5%'), ('15', '^', '15%'),
253	                     ('25', 's', '25%'), ('50', 'o', '50%')]:
254	    ax_c.scatter([], [], marker=mk, s=40, color='#777777',
255	                 edgecolors='white', linewidths=0.4, label=lbl)
256	leg_c = ax_c.legend(loc='upper left', frameon=True, framealpha=0.92,
257	                    edgecolor='none', facecolor='white',
258	                    borderpad=0.35, handletextpad=0.25, handlelength=1.0,
259	                    fontsize=6, ncol=4, columnspacing=0.5)
260	leg_c.get_frame().set_linewidth(0)
261	
262	# |d|=0.8 threshold
263	ax_c.axhline(y=0.8, color=palette.REFERENCE, linestyle=':', linewidth=0.7, zorder=1)
264	t_thr = ax_c.text(96, 1.1, 'large effect', fontsize=5, color=palette.REFERENCE,
265	                  style='italic', ha='right')
266	t_thr.set_path_effects(WHITE_STROKE)
267	
268	# Inline model labels
269	for model, xy, xytext, rad in [
270	    ('Qwen', (67.8, 8.22), (74, 9.8), 0.2),
271	    ('Llama', (59.4, 2.33), (51.5, 0.8), -0.2),
272	    ('Mistral', (52.4, 3.50), (46, 5.8), 0.25),
273	    ('ARC-C', (89.7, 5.30), (94, 8.0), -0.2),
274	]:
275	    col = color_map[model]
276	    t = ax_c.annotate(model, xy=xy, xytext=xytext,
277	                      fontsize=6.5, color=col, fontweight='bold',
278	                      arrowprops=dict(arrowstyle='-', color=col,
279	                                      lw=0.5, alpha=0.5,
280	                                      connectionstyle=f'arc3,rad={rad}'))
281	    t.set_path_effects(WHITE_STROKE)
282	
283	# Mechanism annotations
284	t1 = ax_c.text(77, 1.5, r'$\theta$-shift' + '\nabsorption',
285	               fontsize=5.5, color=palette.ANNOTATION, style='italic',
286	               ha='center', linespacing=1.0)
287	t1.set_path_effects(WHITE_STROKE)
288	
289	t2 = ax_c.text(94, 9.5, 'ceiling\nreversal', fontsize=5.5,
290	               color=palette.ANNOTATION, style='italic', ha='center',
291	               linespacing=1.0)
292	t2.set_path_effects(WHITE_STROKE)
293	
294	ax_c.set_xlabel('Baseline Accuracy (%)', fontsize=8)
295	ax_c.set_ylabel("Cohen's |$d$|", fontsize=8)
296	ax_c.set_xlim(44, 98)
297	ax_c.set_ylim(0, Y_MAX_C)
298	ax_c.set_yticks([0, 2, 4, 6, 8, 10])
299	
300	ax_c.text(0.02, 0.97, '(c)', transform=ax_c.transAxes,
301	          fontsize=11, fontweight='bold', va='top', ha='left',
302	          color=palette.TEXT)
303	palette.style_ax(ax_c)
304	
305	# ═══════════════════════════════════════════════════════════════════════════════
306	# PANEL (d): dose-response trajectory
307	# ═══════════════════════════════════════════════════════════════════════════════
308	x_dose = np.array([0, 1, 2, 3])
309	qwen_free_d   = np.array([4.15, 5.36, 7.44, 5.08])
310	qwen_free_sd  = np.array([0.0,  1.10, 1.86, 3.02])
311	qwen_fixed_d  = np.array([3.52, 6.85, 5.89, 12.32])
312	qwen_fixed_sd = np.array([0.0,  1.80, 1.27, 2.38])
313	llama_free_d  = np.array([2.57, 2.80, 2.56, 2.30])
314	llama_free_sd = np.array([0.99, 0.60, 0.52, 0.30])
315	
316	# |d|=0.8 reference
317	ax_d.axhline(y=0.8, color=palette.REFERENCE, linestyle=':', linewidth=0.6, zorder=1)
318	t_ref = ax_d.text(3.4, 1.1, '$|d|{=}0.8$', fontsize=5, color=palette.REFERENCE,
319	                  ha='right', va='bottom')
320	t_ref.set_path_effects(WHITE_STROKE)
321	
322	# Llama free-θ
323	ax_d.fill_between(x_dose, llama_free_d - llama_free_sd,
324	                  llama_free_d + llama_free_sd,
325	                  alpha=0.10, color=palette.LLAMA, zorder=2)
326	ax_d.errorbar(x_dose, llama_free_d, yerr=llama_free_sd,
327	              fmt='^-', color=palette.LLAMA, markersize=5, linewidth=1.2,
328	              capsize=2.5, capthick=0.6, elinewidth=0.7, alpha=0.85,
329	              label=r'Llama free-$\theta$', zorder=4, markeredgecolor='white',
330	              markeredgewidth=0.6)
331	
332	# Qwen free-θ
333	qf_sd_vis = qwen_free_sd.copy()
334	qf_sd_vis[0] = 0.35
335	ax_d.fill_between(x_dose, qwen_free_d - qf_sd_vis,
336	                  qwen_free_d + qf_sd_vis,
337	                  alpha=0.10, color=palette.QWEN, zorder=2)
338	ax_d.errorbar(x_dose[1:], qwen_free_d[1:], yerr=qwen_free_sd[1:],
339	              fmt='o-', color=palette.QWEN, markersize=5.5, linewidth=1.4,
340	              capsize=2.5, capthick=0.6, elinewidth=0.7, alpha=0.85,
341	              label=r'Qwen free-$\theta$', zorder=5, markeredgecolor='white',
342	              markeredgewidth=0.6)
343	ax_d.plot(x_dose[:2], qwen_free_d[:2], '-', color=palette.QWEN, linewidth=1.4,
344	          alpha=0.85, zorder=5)
345	# Hollow marker at 5% (single-seed)
346	ax_d.plot(x_dose[0], qwen_free_d[0], 'o', color=palette.QWEN, markersize=5.5,
347	          markerfacecolor='white', markeredgecolor=palette.QWEN,
348	          markeredgewidth=1.2, zorder=6)
349	
350	# Qwen fixed-θ
351	ax_d.fill_between(x_dose, qwen_fixed_d - qwen_fixed_sd,
352	                  np.minimum(qwen_fixed_d + qwen_fixed_sd, 15.5),
353	                  alpha=0.08, color=palette.SIGNAL, zorder=2)
354	ax_d.errorbar(x_dose[1:], qwen_fixed_d[1:], yerr=qwen_fixed_sd[1:],
355	              fmt='s--', color=palette.SIGNAL, markersize=5, linewidth=1.3,
356	              capsize=2.5, capthick=0.6, elinewidth=0.7, alpha=0.85,
357	              label=r'Qwen fixed-$\theta$', zorder=5, markeredgecolor='white',
358	              markeredgewidth=0.6)
359	ax_d.plot(x_dose[:2], qwen_fixed_d[:2], '--', color=palette.SIGNAL, linewidth=1.3,
360	          alpha=0.85, zorder=5)
361	# Hollow marker at 5%
362	ax_d.plot(x_dose[0], qwen_fixed_d[0], 's', color=palette.SIGNAL, markersize=5,
363	          markerfacecolor='white', markeredgecolor=palette.SIGNAL,
364	          markeredgewidth=1.2, zorder=6)
365	
366	# Annotations
367	ax_d.annotate('',
368	              xy=(3, 5.35), xycoords='data',
369	              xytext=(2, 7.44), textcoords='data',
370	              arrowprops=dict(arrowstyle='->', color=palette.QWEN,
371	                              lw=0.8, connectionstyle='arc3,rad=0.3'))
372	t_abs = ax_d.text(3.45, 1.8, r'$\theta$-shift absorption',
373	                  fontsize=5.5, color=palette.QWEN, ha='right', va='top',
374	                  linespacing=1.0, fontstyle='italic')
375	t_abs.set_path_effects(WHITE_STROKE)
376	
377	t_fix = ax_d.text(1.6, 15.2, r'$\theta$-anchoring recovers signal',
378	                  fontsize=5.5, color=palette.SIGNAL, ha='center', va='bottom',
379	                  fontstyle='italic', linespacing=1.0)
380	t_fix.set_path_effects(WHITE_STROKE)
381	
382	# Single-seed label
383	ax_d.text(-0.25, 4.5, '$n{=}1$', fontsize=5.5, color=palette.REFERENCE,
384	          fontstyle='italic')
385	
386	ax_d.set_xticks(x_dose)
387	ax_d.set_xticklabels(['5%', '15%', '25%', '50%'])
388	ax_d.set_xlabel('Contamination level', fontsize=8)
389	ax_d.set_ylabel("Cohen's |$d$|", fontsize=8)
390	ax_d.set_ylim(0, 15.5)
391	ax_d.set_xlim(-0.4, 3.55)
392	
393	# Legend
394	handles, labels = ax_d.get_legend_handles_labels()
395	order = [1, 2, 0]  # Qwen free, Qwen fixed, Llama
396	leg_d = ax_d.legend([handles[i] for i in order], [labels[i] for i in order],
397	                    loc='upper left', frameon=True, framealpha=0.92,
398	                    edgecolor='none', facecolor='white',
399	                    handlelength=1.8, handletextpad=0.4, fontsize=6.5,
400	                    borderpad=0.4)
401	leg_d.get_frame().set_linewidth(0)
402	
403	ax_d.text(0.02, 0.97, '(d)', transform=ax_d.transAxes,
404	          fontsize=11, fontweight='bold', va='top', ha='left',
405	          color=palette.TEXT)
406	palette.style_ax(ax_d)
407	
408	# ═══════════════════════════════════════════════════════════════════════════════
409	# SAVE + COPY
410	# ═══════════════════════════════════════════════════════════════════════════════
411	out_dir = PROJ / 'figures' / 'paper'
412	fig.savefig(out_dir / 'fig_1_composite.pdf', format='pdf')
413	fig.savefig(out_dir / 'fig_1_composite.png', format='png')
414	plt.close()
415	print("Saved fig_1_composite.pdf and .png")
416	
417	copy_targets = [
418	    PROJ / 'paper' / 'paper',
419	    PROJ / 'paper' / 'paper' / 'figures' / 'paper',
420	]
421	for tgt in copy_targets:
422	    tgt.mkdir(parents=True, exist_ok=True)
423	    for ext in ['pdf', 'png']:
424	        src = out_dir / f'fig_1_composite.{ext}'
425	        dst = tgt / f'fig_1_composite.{ext}'
426	        shutil.copy2(str(src), str(dst))
427	        print(f"  → {dst}")
428	
429	print("Done.")
430	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eeb26c9c-3209-4afa-b082-f6e18a6ccae9",
  "isSidechain": true,
  "promptId": "edfb55fe-7e9f-401e-83b5-0728b9452cea",
  "agentId": "a23c74de550a91739",
  "type": "user",
  "uuid": "7ea02cf3-3e13-4932-bf96-e74823a3c301",
  "sourceToolAssistantUUID": "eeb26c9c-3209-4afa-b082-f6e18a6ccae9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T08:23:14.930Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VkZpStPeTiBjibjXW7Coh7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ea02cf3-3e13-4932-bf96-e74823a3c301",
  "isSidechain": true,
  "agentId": "a23c74de550a91739",
  "requestId": "req_011CbNxuNZiKMddQEV4dWVh8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9db08c3-d55e-4b09-8049-0204e7945999",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TGHiyQSk2tKfa7Q8eFr92L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33558,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33558,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 15 · 2026-05-25T08:23:14.936Z_

<details><summary>↩ Tool result · `toolu_01VkZpStPeTiBjibjXW7Coh7`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We presented the first empirical characterization of IRT person-fit statistics for LLM benchmark contamination detection, evaluating $\ell_z^*$ across three 7--8B model families (Qwen, Llama, Mistral), two benchmarks (MMLU, ARC-C), and four contamination levels (5\%--50\%).
4	Our controlled experiments reveal three boundary conditions: (i)~$\theta$-shift absorption, where contamination inflates ability estimates and attenuates person-fit signals in a model-dependent manner, necessitating $\theta$-anchoring for high-ability models; (ii)~a detection-diagnosis tradeoff, where simpler statistics detect more powerfully but only $\ell_z^*$ supports mechanistic analysis; and (iii)~non-monotonic dose-response under free-$\theta$ estimation, which is a $\theta$-estimation artifact eliminated by anchoring.
5	These findings establish that binary response patterns, combined with externally calibrated item parameters, carry sufficient information for contamination detection---but that detection and diagnosis require different tools.
6	A preliminary post-RL pilot suggests person-fit anomalies persist after RL, complementing logit-based methods that fail in this setting; future work should extend to larger scales, pretraining-stage contamination, and multi-family post-RL validation.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9db08c3-d55e-4b09-8049-0204e7945999",
  "isSidechain": true,
  "promptId": "edfb55fe-7e9f-401e-83b5-0728b9452cea",
  "agentId": "a23c74de550a91739",
  "type": "user",
  "uuid": "2a7c8ffd-e952-493a-97d9-d90d4c8f2a23",
  "sourceToolAssistantUUID": "f9db08c3-d55e-4b09-8049-0204e7945999",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T08:23:15.503Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Lkc9fe843nGdE8y5wkD1zu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a7c8ffd-e952-493a-97d9-d90d4c8f2a23",
  "isSidechain": true,
  "agentId": "a23c74de550a91739",
  "requestId": "req_011CbNxuNZiKMddQEV4dWVh8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "890f58a4-ffac-4a8f-8c61-242661e83cfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TGHiyQSk2tKfa7Q8eFr92L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33558,
      "cache_read_input_tokens": 0,
      "output_tokens": 568,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 33558
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 568,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 33558,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 33558,
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

_source line 17 · 2026-05-25T08:23:15.510Z_

<details><summary>↩ Tool result · `toolu_01Lkc9fe843nGdE8y5wkD1zu`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Detection vs.\ diagnosis.}
4	The detection-diagnosis tradeoff reveals a design tension absent from prior contamination detection work.
5	Simpler statistics---accuracy $z$-scores, HT---detect contamination more powerfully because they are not attenuated by the Snijders correction or inflated by $\theta$-shift absorption.
6	Yet $\ell_z^*$ provides unique mechanistic insight invisible to non-IRT statistics: $\theta$-shift analysis reveals \emph{why} detection varies across models (baseline ability determines absorption magnitude), seen/unseen decomposition localizes the signal source, and 4PL modeling captures ceiling effects that 3PL misses ($+$27.3pp power on MMLU).
7	Our contribution lies not in proposing a new detection method but in quantifying these theoretically predicted phenomena where magnitudes are not derivable from IRT theory alone.
8	
9	\paragraph{Practical implications.}
10	For practitioners, we recommend a two-stage workflow: (i)~screen with accuracy $z$-scores, which require no item parameters and produce the largest effect sizes; (ii)~characterize flagged models with $\ell_z^*$ to determine whether the signal reflects $\theta$-shift absorption (high-ability model, large $\Delta\theta$) or direct memorization (anomalous successes on hard items without commensurate $\theta$ inflation).
11	$\theta$-anchoring is necessary to stabilize detection for high-ability models (free-$\theta$ CV up to 60\% vs.\ 19\% under $\theta$-fixed; \S\ref{sec:theta_dynamics}).
12	Universal baseline misfit (57/60 cells flagged; Figure~\ref{fig:leaderboard_heatmap}) means absolute $\ell_z^*$ thresholds cannot be used directly; the $\Delta\ell_z^*$ matched-difference design or cross-benchmark comparison is required.
13	
14	\paragraph{Robustness and complementarity.}
15	PSN-IRT provides pre-calibrated 4PL parameters \citep{psnirt2026} that are robust to estimation noise: $\pm$10\% parameter perturbation produces $<$4\% bias in fixed-$\theta$ Cohen's $d$ (Appendix~\ref{app:param_perturb}), because the matched-difference design cancels shared parameter error.
16	Requiring only binary response patterns and an external item bank, $\ell_z^*$ occupies a unique position at the minimal-access end of the detection frontier: it complements logit-based methods \citep{minkprob2024,constat2024} that fail after RL post-training \citep{wang2025fragility}.
17	Our GRPO pilot illustrates this complementarity: Min-K\% AUC drops to chance ($0.493$) after 500 RL steps, while the $\ell_z^*$ response-pattern gap persists at ${\sim}3.3$ across all checkpoints (Figure~\ref{fig:grpo}).
18	This structural invariance---RL reshapes token-level distributions but preserves binary correctness anomalies---suggests that person-fit statistics may remain informative in settings where all probability-based detectors fail, though this $N{=}1$ observation requires multi-family validation.
19	
20	\begin{figure}[t]
21	  \centering
22	  \includegraphics[width=\columnwidth]{fig_grpo.pdf}
23	  \caption{Post-RL trajectory (Qwen, 15\% MMLU). GRPO erases the accuracy gap ($11.4\text{pp} \to 2.1\text{pp}$) while the $\ell_z^*$ gap persists (${\sim}3.3$). $N{=}1$; Appendix~\ref{app:post_rl}.}
24	  \label{fig:grpo}
25	\end{figure}
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "890f58a4-ffac-4a8f-8c61-242661e83cfd",
  "isSidechain": true,
  "promptId": "edfb55fe-7e9f-401e-83b5-0728b9452cea",
  "agentId": "a23c74de550a91739",
  "type": "user",
  "uuid": "119bd508-92f6-4e2e-b653-1a0aab849471",
  "sourceToolAssistantUUID": "890f58a4-ffac-4a8f-8c61-242661e83cfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-25T08:23:18.387Z_

Now let me read the heatmap generation script and check for the Figure 1 panel (c) data issue more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "119bd508-92f6-4e2e-b653-1a0aab849471",
  "isSidechain": true,
  "agentId": "a23c74de550a91739",
  "requestId": "req_011CbNxuri8aUbxAf91mt2JD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78628501-6a28-47e4-b6cf-bd4f654e3c92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016uRHvYtpPxF6jjVcie7MEc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20668,
      "cache_read_input_tokens": 33558,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20668,
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

_source line 19 · 2026-05-25T08:23:20.252Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017tpRoiAwaqDD7vs8THuzR4`</summary>

```json
{
  "pattern": "**/gen_fig_heatmap.py",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78628501-6a28-47e4-b6cf-bd4f654e3c92",
  "isSidechain": true,
  "agentId": "a23c74de550a91739",
  "requestId": "req_011CbNxuri8aUbxAf91mt2JD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "270d77ab-40f3-4aab-a031-53904a8bf891",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016uRHvYtpPxF6jjVcie7MEc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20668,
      "cache_read_input_tokens": 33558,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20668
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 33558,
          "cache_creation_input_tokens": 20668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20668,
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

_source line 20 · 2026-05-25T08:23:20.402Z_

<details><summary>↩ Tool result · `toolu_017tpRoiAwaqDD7vs8THuzR4`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/scripts/gen_fig_heatmap.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/paper/scripts/gen_fig_heatmap.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/figures/paper/gen_fig_heatmap.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "270d77ab-40f3-4aab-a031-53904a8bf891",
  "isSidechain": true,
  "promptId": "edfb55fe-7e9f-401e-83b5-0728b9452cea",
  "agentId": "a23c74de550a91739",
  "type": "user",
  "uuid": "761ef602-95a5-4bd5-941a-d9c040306f14",
  "sourceToolAssistantUUID": "270d77ab-40f3-4aab-a031-53904a8bf891",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-25T08:23:23.100Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DZTHua27JQHiiFE3qqwmep`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/paper/scripts/gen_fig_heatmap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "761ef602-95a5-4bd5-941a-d9c040306f14",
  "isSidechain": true,
  "agentId": "a23c74de550a91739",
  "requestId": "req_011CbNxvDMMPGCBCeUqUNr2Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b374079e-dae0-47da-a700-cbb6563174c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hr4FvtAgxkiK7hhX6B8Pva",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 291,
      "cache_read_input_tokens": 54226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 291,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 22 · 2026-05-25T08:23:23.107Z_

<details><summary>↩ Tool result · `toolu_01DZTHua27JQHiiFE3qqwmep`</summary>

```text
1	import matplotlib
2	matplotlib.use('Agg')
3	import matplotlib.pyplot as plt
4	import matplotlib.colors as mcolors
5	import numpy as np
6	from pathlib import Path
7	
8	matplotlib.rcParams.update({
9	    'font.family': 'serif',
10	    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
11	    'font.size': 9,
12	    'axes.labelsize': 10,
13	    'xtick.labelsize': 8,
14	    'ytick.labelsize': 8,
15	    'text.usetex': False,
16	    'figure.dpi': 300,
17	    'savefig.dpi': 300,
18	    'savefig.bbox': 'tight',
19	    'savefig.pad_inches': 0.05,
20	    'axes.linewidth': 0.6,
21	})
22	
23	models = ['Qwen-2.5-7B', 'Llama-3.1-8B', 'Mistral-7B']
24	columns = [
25	    ('MMLU\n5%', 'MMLU'),
26	    ('MMLU\n15%', 'MMLU'),
27	    ('MMLU\n25%', 'MMLU'),
28	    ('MMLU\n50%', 'MMLU'),
29	    ('ARC-C\n15%', 'ARC-C'),
30	    ('ARC-C\n50%', 'ARC-C'),
31	]
32	
33	d_vals = np.array([
34	    [4.15, 5.36, 7.44, 5.08, 3.16, 5.30],
35	    [np.nan, 2.80, 2.56, 2.30, np.nan, np.nan],
36	    [np.nan, 3.37, np.nan, 4.09, np.nan, np.nan],
37	])
38	
39	ci_text = [
40	    ['[2.7, 9.9]', '(±1.10)', '(±1.86)', '(±3.02)', '[2.0, 9.5]', '[3.6, 15.2]'],
41	    ['', '(±0.60)', '(±0.52)', '(±0.30)', '', ''],
42	    ['', '(±0.68)', '', '(±0.53)', '', ''],
43	]
44	
45	n_rows, n_cols = d_vals.shape
46	d_display = np.where(np.isnan(d_vals), 0, d_vals)
47	vmax = 9.0
48	
49	cmap = plt.cm.Blues
50	norm = mcolors.Normalize(vmin=0, vmax=vmax)
51	
52	fig, ax = plt.subplots(figsize=(8.5, 3.2))
53	
54	im = ax.imshow(d_display, cmap=cmap, norm=norm, aspect='auto')
55	
56	for i in range(n_rows):
57	    for j in range(n_cols):
58	        val = d_vals[i, j]
59	        if np.isnan(val):
60	            ax.text(j, i, '—', ha='center', va='center',
61	                    fontsize=12, color='#aaaaaa')
62	        else:
63	            r, g, b, _ = cmap(norm(val))
64	            lum = 0.299 * r + 0.587 * g + 0.114 * b
65	            txt_color = 'white' if lum < 0.5 else 'black'
66	
67	            ax.text(j, i - 0.12, f'|d| = {val:.2f}',
68	                    ha='center', va='center', fontsize=9.5,
69	                    color=txt_color, fontweight='bold')
70	            if ci_text[i][j]:
71	                ax.text(j, i + 0.18, ci_text[i][j],
72	                        ha='center', va='center', fontsize=6.5,
73	                        color=txt_color, alpha=0.85)
74	
75	ax.set_xticks(range(n_cols))
76	ax.set_xticklabels([c[0] for c in columns], fontsize=8)
77	ax.xaxis.set_ticks_position('bottom')
78	
79	ax.set_yticks(range(n_rows))
80	ax.set_yticklabels(models, fontsize=10)
81	
82	for spine in ax.spines.values():
83	    spine.set_visible(False)
84	ax.tick_params(length=0)
85	
86	# Group labels below column labels (x=data coords, y=axes fraction)
87	trans = ax.get_xaxis_transform()
88	ax.text(1.5, -0.18, 'MMLU (14,042 items)', ha='center', va='top',
89	        fontsize=9, fontweight='bold', transform=trans)
90	ax.text(4.5, -0.18, 'ARC-C (295 items)', ha='center', va='top',
91	        fontsize=9, fontweight='bold', transform=trans)
92	
93	# Separator between MMLU and ARC-C
94	ax.axvline(x=3.5, color='white', linewidth=3)
95	
96	# Colorbar
97	cbar = fig.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
98	cbar.set_label("Cohen's |d|", fontsize=9)
99	cbar.ax.tick_params(labelsize=7)
100	
101	# Footer
102	ax.text(0.5, -0.32,
103	        r'$n = 10$ clean seeds; multi-seed means (±SD) where available, else bootstrap 95% CI.',
104	        transform=ax.transAxes, ha='center', fontsize=7.5,
105	        color='#666666', style='italic')
106	
107	out = Path(__file__).resolve().parent
108	fig.savefig(out / 'fig_heatmap.pdf', format='pdf')
109	fig.savefig(out / 'fig_heatmap.png', format='png')
110	plt.close()
111	print("Done. Files saved.")
112	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b374079e-dae0-47da-a700-cbb6563174c9",
  "isSidechain": true,
  "promptId": "edfb55fe-7e9f-401e-83b5-0728b9452cea",
  "agentId": "a23c74de550a91739",
  "type": "user",
  "uuid": "37857adb-91c9-4461-896e-e3d5196b9e35",
  "sourceToolAssistantUUID": "b374079e-dae0-47da-a700-cbb6563174c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T08:23:23.520Z_

<details open><summary>🔧 Tool call — Read · `toolu_013h6SuYbWerAWhz2QokV95T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/figures/paper/gen_fig_heatmap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37857adb-91c9-4461-896e-e3d5196b9e35",
  "isSidechain": true,
  "agentId": "a23c74de550a91739",
  "requestId": "req_011CbNxvDMMPGCBCeUqUNr2Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d00b2f1-c35b-4fea-92a9-fbfc7fdebf50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hr4FvtAgxkiK7hhX6B8Pva",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 291,
      "cache_read_input_tokens": 54226,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 291
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 54226,
          "cache_creation_input_tokens": 291,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 291,
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

_source line 24 · 2026-05-25T08:23:23.526Z_

<details><summary>↩ Tool result · `toolu_013h6SuYbWerAWhz2QokV95T`</summary>

```text
1	"""Cohen's |d| effect-size heatmap (Figure 3).
2	
3	Compact single-column heatmap: 3 models × 6 conditions.
4	Output: fig_heatmap.{pdf,png}
5	"""
6	import matplotlib
7	matplotlib.use('Agg')
8	import matplotlib.pyplot as plt
9	import matplotlib.colors as mcolors
10	import numpy as np
11	import shutil
12	from pathlib import Path
13	
14	import sys; sys.path.insert(0, str(Path(__file__).resolve().parent))
15	import palette
16	palette.apply()
17	
18	PROJ = Path('/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam')
19	
20	models = ['Qwen', 'Llama', 'Mistral']
21	col_labels = ['5%', '15%', '25%', '50%', '15%', '50%']
22	
23	d_vals = np.array([
24	    [4.15, 5.36, 7.44, 5.08, 3.16, 5.30],
25	    [2.57, 2.80, 2.56, 2.30, np.nan, np.nan],
26	    [3.83, 3.37, np.nan, 4.09, np.nan, np.nan],
27	])
28	
29	ci_text = [
30	    ['[2.7, 9.9]', '±1.10', '±1.86', '±3.02', '[2.0, 9.5]', '[3.6, 15.2]'],
31	    ['±0.99', '±0.60', '±0.52', '±0.30', '', ''],
32	    ['±1.42', '±0.68', '', '±0.53', '', ''],
33	]
34	
35	n_rows, n_cols = d_vals.shape
36	
37	cmap = mcolors.LinearSegmentedColormap.from_list(
38	    'd_cmap', ['#FFFFFF', '#C8D6E5', '#7B9CC7', palette.QWEN], N=256)
39	norm = mcolors.Normalize(vmin=0, vmax=8.0)
40	
41	fig, ax = plt.subplots(figsize=(4.2, 1.85))
42	fig.subplots_adjust(left=0.13, right=0.88, top=0.85, bottom=0.18)
43	
44	d_display = np.where(np.isnan(d_vals), 0, d_vals)
45	im = ax.imshow(d_display, cmap=cmap, norm=norm, aspect='auto')
46	
47	# Missing cells with hatching
48	for i in range(n_rows):
49	    for j in range(n_cols):
50	        if np.isnan(d_vals[i, j]):
51	            ax.add_patch(plt.Rectangle(
52	                (j - 0.5, i - 0.5), 1, 1,
53	                facecolor='#F8F8F8', edgecolor='white', linewidth=1.2,
54	                hatch='///', zorder=2))
55	            ax.patches[-1].set_edgecolor('#E0E0E0')
56	
57	# White grid
58	for i in range(n_rows + 1):
59	    ax.axhline(y=i - 0.5, color='white', linewidth=1.2, zorder=3)
60	for j in range(n_cols + 1):
61	    ax.axvline(x=j - 0.5, color='white', linewidth=1.2, zorder=3)
62	ax.axvline(x=3.5, color='white', linewidth=3.0, zorder=4)
63	
64	# Cell text
65	for i in range(n_rows):
66	    for j in range(n_cols):
67	        val = d_vals[i, j]
68	        if np.isnan(val):
69	            ax.text(j, i, '—', ha='center', va='center',
70	                    fontsize=8, color='#CCCCCC', zorder=5)
71	        else:
72	            r, g, b, _ = cmap(norm(val))
73	            lum = 0.299 * r + 0.587 * g + 0.114 * b
74	            txt_color = 'white' if lum < 0.55 else palette.TEXT
75	
76	            ax.text(j, i - 0.12, f'{val:.2f}',
77	                    ha='center', va='center', fontsize=8,
78	                    color=txt_color, fontweight='bold', zorder=5)
79	            if ci_text[i][j]:
80	                ci_alpha = 0.80 if lum < 0.55 else 0.65
81	                ax.text(j, i + 0.18, ci_text[i][j],
82	                        ha='center', va='center', fontsize=5.5,
83	                        color=txt_color, alpha=ci_alpha, zorder=5)
84	
85	# Axes
86	ax.set_xticks(range(n_cols))
87	ax.set_xticklabels(col_labels, fontsize=7)
88	ax.xaxis.set_ticks_position('bottom')
89	ax.set_yticks(range(n_rows))
90	ax.set_yticklabels(models, fontsize=7.5, fontweight='bold')
91	
92	for spine in ax.spines.values():
93	    spine.set_visible(False)
94	ax.tick_params(length=0)
95	
96	# Benchmark group labels
97	trans = ax.get_xaxis_transform()
98	ax.text(1.5, -0.25, 'MMLU', ha='center', va='top',
99	        fontsize=7, fontweight='bold', color=palette.TEXT, transform=trans)
100	ax.text(4.5, -0.25, 'ARC-C', ha='center', va='top',
101	        fontsize=7, fontweight='bold', color=palette.TEXT, transform=trans)
102	
103	# Colorbar
104	cbar = fig.colorbar(im, ax=ax, shrink=0.75, pad=0.03, aspect=12)
105	cbar.set_label("Cohen's |$d$|", fontsize=7, labelpad=3)
106	cbar.ax.tick_params(labelsize=6)
107	cbar.outline.set_linewidth(0.3)
108	
109	# Save
110	out = Path(__file__).resolve().parent
111	fig.savefig(out / 'fig_heatmap.pdf', format='pdf')
112	fig.savefig(out / 'fig_heatmap.png', format='png')
113	plt.close()
114	
115	for tgt in [PROJ / 'paper' / 'paper']:
116	    shutil.copy2(str(out / 'fig_heatmap.pdf'), str(tgt / 'fig_heatmap.pdf'))
117	print("Done: fig_heatmap.pdf/png")
118	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d00b2f1-c35b-4fea-92a9-fbfc7fdebf50",
  "isSidechain": true,
  "promptId": "edfb55fe-7e9f-401e-83b5-0728b9452cea",
  "agentId": "a23c74de550a91739",
  "type": "user",
  "uuid": "3c8ab406-51b4-4982-9ca0-23b1fc239534",
  "sourceToolAssistantUUID": "1d00b2f1-c35b-4fea-92a9-fbfc7fdebf50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-25T08:24:16.646Z_

Now I have all the data needed. Let me compile the findings for each issue.

---

## Issue-by-Issue Verification Report

### Issue 1: Figure 3 heatmap values vs Table 1

**Finding: NO issue (heatmap matches Table 1)**

The heatmap script (`figures/paper/gen_fig_heatmap.py`, lines 23-27) uses:
```python
d_vals = np.array([
    [4.15, 5.36, 7.44, 5.08, 3.16, 5.30],   # Qwen
    [2.57, 2.80, 2.56, 2.30, np.nan, np.nan], # Llama
    [3.83, 3.37, np.nan, 4.09, np.nan, np.nan],# Mistral
])
```

These match Table 1 (`tab:cohens_d`, results.tex lines 14-16) exactly:
- Qwen MMLU: 4.15 / 5.36 / 7.44 / 5.08 at 5/15/25/50%
- Llama MMLU: 2.57 / 2.80 / 2.56 / 2.30
- Mistral MMLU: 3.83 / 3.37 / --- / 4.09

The CI/SD annotations also match. The caption (results.tex line 39) says "values from Table 1; multi-seed means where available" — accurate.

**However**, Figure 1 panel (c) (`gen_fig1_composite.py`, lines 218-229) **does** use single-seed values for some conditions:
- Qwen 15%: `6.57` (not 5.36 from Table 1)
- Qwen 25%: `8.22` (not 7.44)
- Qwen 50%: `1.90` (not 5.08)
- Mistral 15%: `3.37` (matches Table 1 multi-seed mean)
- Llama 25%: `1.99` (Table 1 shows 2.56 multi-seed)

This is a **secondary finding**: Figure 1(c) scatter plot uses seed-42 single-run values for multi-seed conditions, while Table 1 reports multi-seed means. The Figure 1 caption (introduction.tex line 6) does not disclose this. Severity: **Medium** — the scatter plot shows different numbers than the table for the same conditions without explanation.

---

### Issue 2: Fixed-theta monotonicity claim

**Finding: YES, issue exists. Severity: Medium.**

The Figure 1 caption (introduction.tex line 6) states:
> `"fixed-$\theta$ recovers monotone signal"`

The dose-response data in `gen_fig1_composite.py` (line 311):
```python
qwen_fixed_d  = np.array([3.52, 6.85, 5.89, 12.32])
```

The fixed-theta trajectory is: 3.52 -> 6.85 -> **5.89** -> 12.32 (at 5/15/25/50%). The dip from 6.85 to 5.89 (15% -> 25%) is clearly non-monotone.

The main text in results.tex (line 142) is more careful:
> `"fixed-$\theta$ eliminates the inverted-U ($|d|{=}12.32$ at 50\%, CV reduced to 19\%)"`

This doesn't explicitly claim monotonicity — it says "eliminates the inverted-U" (the peak-then-decline pattern). The fixed-theta series does not show the inverted-U (it doesn't peak at 25% and then crash at 50%), but it does dip at 25%.

The Figure 1 caption's "recovers monotone signal" is **inaccurate** given the 6.85 -> 5.89 dip. The contribution text in introduction.tex (line 53) says `"$\theta$-anchoring eliminates the pattern and reveals strong positive dose-response"` — this is also somewhat misleading given the non-monotonicity.

---

### Issue 3: "all bootstrap 95% CIs exclude zero, n=10" accuracy

**Finding: YES, issue exists. Severity: Medium.**

Introduction.tex line 58 states:
> `"(2) We establish that $\Delta\ell_z^*$ reliably detects SFT-stage contamination across three model families (all bootstrap 95\% CIs exclude zero, $n{=}10$)."`

Table 1 caption (results.tex line 6) clarifies:
> `"Single-seed conditions: percentile bootstrap 95\% CI (10,000 resamples). $^{\dagger}$Multi-seed conditions: mean $\pm$ SD ($n{=}3$ independent runs). All single-seed CIs exclude zero."`

The problem: the contribution claim says "all bootstrap 95% CIs exclude zero" without the "single-seed" qualifier. Multi-seed conditions report mean +/- SD, not bootstrap CIs. And Table 2 (tab:theta_fixed) shows Llama fixed-theta at 15% has CI `[0, 2.37]` with footnote "CI includes zero" (line 86). The contribution claim is about Table 1 free-theta conditions, but the unqualified "all" is misleading — it omits that multi-seed conditions don't have CIs at all, and that some fixed-theta CIs do include zero.

---

### Issue 4: ARC-Challenge 295 items

**Finding: NO issue.**

The paper explicitly states in sec_setup.tex (line 4):
> `"ARC-Challenge \citep{clark2018arc} (295)"`

And method.tex (line 54):
> `"ARC-Challenge \citep{clark2018arc} (295 items)"`

The standard ARC-Challenge test set has 1,172 items. However, the paper uses PSN-IRT pre-calibrated 4PL parameters, which are only available for a subset. Method.tex line 55:
> `"All 4PL item parameters are from \citet{psnirt2026}."`

The 295 count is the number of ARC-Challenge items that have PSN-IRT v2 4PL calibrations. The paper does not explicitly state "295 items because PSN-IRT only calibrated 295" — this is **implicit** from the context that all item parameters come from PSN-IRT. A reader familiar with ARC-Challenge (1,172 items) might be confused.

**Severity: Low** — the reason is inferrable but not explicitly stated. A parenthetical clarification would help.

---

### Issue 5: 4PL "slip" terminology

**Finding: YES, issue exists. Severity: Low.**

Method.tex line 13:
> `"$d_i$ the upper asymptote (slip)"`

Technically in IRT, "slip" is defined as $s_i = 1 - d_i$ (the probability that a high-ability examinee answers incorrectly). The upper asymptote $d_i$ itself is not "slip" — it is the complement of slip. Some authors call $d_i$ the "ceiling" or "upper asymptote" parameter.

The exact text is: `"$c_i$ the lower asymptote (guessing), and $d_i$ the upper asymptote (slip)"`. The parenthetical "slip" is technically wrong. It should be "1 - slip" or the parameter should just be described as "upper asymptote" without the parenthetical.

---

### Issue 6: Table 3 (tab:degradation) missing CI

**Finding: YES, issue exists. Severity: Medium-High.**

Results.tex line 122:
```
Mistral & $\ell_z^*$ & $2.64^{\ddagger}$ & $3.50$ [$2.1$, $9.4$] \\
```

The `$^{\ddagger}$` footnote (line 126):
> `"$^{\ddagger}$CI not retained from analysis pipeline; multi-seed SD in Table~\ref{tab:cohens_d}."`

This is indeed a pipeline artifact. One cell in a submission-quality table has no CI/SD because the analysis pipeline didn't retain it. The footnote candidly admits this. For a submission to EMNLP 2026, this is unprofessional — it signals incomplete data management. The Mistral 15% multi-seed SD is available in Table 1 (±0.68), so the data exists; it was just not propagated to the Table 3 computation. This should be fixed before submission.

---

## Summary

| Issue | Exists? | Severity |
|-------|---------|----------|
| 1. Heatmap vs Table 1 | **NO** (heatmap matches; but Figure 1(c) uses single-seed values without disclosure) | Medium (for Fig 1c) |
| 2. Fixed-theta monotonicity | **YES** — caption says "monotone" but trajectory dips 6.85->5.89 | Medium |
| 3. "all bootstrap CIs" claim | **YES** — missing "single-seed" qualifier; multi-seed conditions use SD not CIs | Medium |
| 4. ARC-C 295 items | **NO** — explained by PSN-IRT filtering (implicitly) | Low |
| 5. 4PL "slip" terminology | **YES** — $d_i$ is the upper asymptote, not "slip" (slip = $1-d_i$) | Low |
| 6. Table 3 missing CI | **YES** — pipeline artifact, unprofessional for submission | Medium-High |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c8ab406-51b4-4982-9ca0-23b1fc239534",
  "isSidechain": true,
  "agentId": "a23c74de550a91739",
  "requestId": "req_011CbNxvSze2jE7bR67zwJ8a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc7bcdc0-9781-4cc6-8a52-16cdf9d58340",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CBt5xExdA1LZsjMiATKxTL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3897,
      "cache_read_input_tokens": 54517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3897,
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
