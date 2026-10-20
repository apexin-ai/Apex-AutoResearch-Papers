# Research conversation: Two files to create for the simgate-modular-routing project ### File 1: artifacts/paper_patch_draft.md Create `/home/ubu

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a9d6419e05e089045.jsonl`
- **Structured JSON:** [`1373f664d338bff940b9.json`](../../sessions/13/1373f664d338bff940b9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

16 recorded events

### User

_source line 1 · 2026-05-20T07:37:45.921Z_

## Two files to create for the simgate-modular-routing project

### File 1: artifacts/paper_patch_draft.md

Create `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/paper_patch_draft.md` with two paper patch drafts using [TBD] placeholders for pending data.

First, read these files to understand current paper content:
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex` — find the ALFWorld section (around L75-85) and the cross-model table
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex` — find the cross-model appendix section

Then write the draft file with:

**Section 2a: ALFWorld Subsection Expansion**

Current ALFWorld is just one paragraph. Draft an expanded version that:
- Keeps existing Qwen data (135 games, 25.9% det-preferred, 1.5% int-preferred, 72.6% no-pref)
- Adds Llama cross-model row with [TBD] placeholders
- Adds formal DAF=0% explanation (no death mechanism → all routing signal from information asymmetry)
- Frames it as "framework correctly diagnoses different mechanisms in different environments"

Write in academic LaTeX style, ready to paste. Example format:
```latex
% ALFWorld subsection expansion
\paragraph{Cross-environment validation: ALFWorld.}
ALFWorld~\citep{alfworld-2020} provides a complementary test...
[existing Qwen data]...
Cross-model replication with Llama-3.1-8B yields [TBD]% det-preferred...
```

**Section 2b: Cross-model Table Expansion**

Draft an expanded cross-model table:
```latex
\begin{table}[t]
\centering
\small
\begin{tabular}{llccccc}
\toprule
Model & Environment & $n$ & Int DR & Det DR & $\Delta$DR & DAF \\
\midrule
Qwen2.5-7B & ScienceWorld & 245 & 42.9\% & 16.3\% & +26.5 & 90.4\% \\
Llama-3.1-8B & ScienceWorld & 220 & 41.4\% & 11.4\% & +30.0 & 88.2\% \\
Gemma-2-9B & ScienceWorld & [TBD] & [TBD] & [TBD] & [TBD] & [TBD] \\
Qwen2.5-72B & ScienceWorld & 255 & 30.6\% & 2.75\% & +27.8 & 92.4\% \\
\midrule
Qwen2.5-7B & ALFWorld & 135 & 0\% & 0\% & 0 & 0\% \\
Llama-3.1-8B & ALFWorld & [TBD] & [TBD] & [TBD] & [TBD] & [TBD] \\
\midrule
Qwen2.5-7B & MATH & 300 & N/A & N/A & N/A & N/A \\
\bottomrule
\end{tabular}
\caption{Cross-model and cross-environment replication...}
\label{tab:cross-model-env}
\end{table}
```

### File 2: artifacts/result_scenarios.md

Create `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/result_scenarios.md` with scenario analysis:

```markdown
# Result Scenario Analysis

Pre-analysis of how pending experimental results affect paper claims.

## Scenarios

| Scenario | Gemma ScienceWorld | Llama ALFWorld | Paper Impact |
|----------|-------------------|----------------|-------------|
| **Best** | Death dominance confirmed (DAF > 80%, ΔDR > 20pp) | Information asymmetry confirmed (~25% det-pref, 0% death labels) | Upgrade C1 to "3 model families"; upgrade C3 to "cross-model × cross-environment"; Discussion adds "framework generalizes across both axes" |
| **Median** | Death dominance directionally consistent but weaker (DAF 50-80%, ΔDR 10-20pp) | Information asymmetry confirmed | C1 unchanged ("2+ families"), Gemma as "supporting evidence with reduced effect size" in Appendix; C3 upgrade for ALFWorld cross-model |
| **Worst** | No death dominance or reversed direction | Results inconsistent with Qwen | Discuss model-dependency as limitation; reduce C1 claim strength but add depth analyzing why Gemma differs; if ALFWorld also inconsistent, add "model-specific" caveat to C3 |

## Response Plans

### Best case actions
- Expand cross-model table to 3×2 matrix (3 models × 2 environments)
- Strengthen Abstract/Intro language: "across three independent model families"
- Add Gemma row to Table 3 in main text (not just appendix)

### Median case actions  
- Add Gemma to Appendix cross-model table with effect size discussion
- Main text mentions "two primary + one supporting model family"
- ALFWorld subsection gets Llama cross-model data

### Worst case actions
- Reframe as "model-dependent phenomenon" — still a valid diagnostic finding
- Add analysis: what about Gemma's architecture/training makes it different?
- Consider whether Gemma's behavior reveals a limitation of the framework or of the model
- Do NOT suppress negative results — present them honestly with analysis
```

Write both files. Confirm paths when done.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "87127d5f-9fda-46aa-9632-72943c579a6b",
  "agentId": "a9d6419e05e089045",
  "type": "user",
  "uuid": "2e56f822-9b09-4548-9f8c-409a5d6eab7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T07:37:45.927Z_

```json
{
  "parentUuid": "2e56f822-9b09-4548-9f8c-409a5d6eab7d",
  "isSidechain": true,
  "agentId": "a9d6419e05e089045",
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
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
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
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "46da5dcc-d528-4701-a6b6-a23d1a8594b2",
  "timestamp": "2026-05-20T07:37:45.927Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

---

### Assistant

_source line 3 · 2026-05-20T07:37:48.292Z_



I'll read the paper files first to understand the current content, then create both artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46da5dcc-d528-4701-a6b6-a23d1a8594b2",
  "isSidechain": true,
  "agentId": "a9d6419e05e089045",
  "requestId": "req_011CbDSQ4jZzAxwPZdTA1u53",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed304634-0745-471b-8d03-e51fff60c073",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PidFvsJYSdV3piXvrTmkhg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21907,
      "cache_read_input_tokens": 8264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21907,
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

_source line 4 · 2026-05-20T07:37:49.262Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E4BvkaFqXNVNFnijEtnPrS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed304634-0745-471b-8d03-e51fff60c073",
  "isSidechain": true,
  "agentId": "a9d6419e05e089045",
  "requestId": "req_011CbDSQ4jZzAxwPZdTA1u53",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e12564f-1896-4eb3-ab55-cb20a06ad1dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PidFvsJYSdV3piXvrTmkhg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21907,
      "cache_read_input_tokens": 8264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21907,
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

_source line 5 · 2026-05-20T07:37:49.283Z_

<details><summary>↩ Tool result · `toolu_01E4BvkaFqXNVNFnijEtnPrS`</summary>

```text
1	\section{Experiments}
2	
3	We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types (63\%) lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). This scope limits generalizability: conclusions apply to the included subset, not to all ScienceWorld tasks. An anti-cherry-picking analysis confirms that death dominance holds in 18 of these 19 types, with a mean $\Delta\text{DR} = +38.2$\,pp exceeding the included tasks' $+28.7$\,pp (Appendix~\ref{app:per-task}). Extended validation at $n{=}20$ on five representative excluded tasks confirms this direction ($\overline{\Delta\text{DR}} = +32.0$\,pp; Appendix~\ref{app:extended-validation}). A reasoning-depth ablation ($n{=}120$) found no significant difference between internal strategy variants ($p > 0.26$; Appendix~\ref{app:ablations}).
4	
5	\subsection{Death Avoidance Decomposition}
6	\label{sec:death-decomp}
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=0.85\columnwidth]{figures/fig1_daf_scatter.pdf}
11	\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$ (Spearman's $\rho = 0.986$; Appendix~\ref{app:per-task}), $p < 10^{-6}$, $n = 11$ task types. Since $\Delta_{\text{full}} \approx \delta P + \Delta_{\text{nd}}$ with $P$ constant, $r \to 1$ as DAF $\to 1$; the near-perfect correlation is a structural consequence of death dominance, not an independent finding (\S\ref{sec:death-decomp}).}
12	\label{fig:decomposition}
13	\end{figure}
14	
15	Of the 95 non-tie routing labels, 75 (78.9\%) arise from death asymmetry: the internal strategy triggers a catastrophic $-100$ penalty while the deterministic strategy survives. This penalty-independent label fraction is the primary diagnostic metric. Of these 75, 54 are sole-signal labels (both strategies score zero without death, so death avoidance was the \emph{sole} discriminating signal). At $P{=}0$, the 54 sole-signal labels reduce to ties, leaving 41 non-tie labels of which 21 (51.2\%) still involve death asymmetry; the labeling function itself is penalty-independent (Algorithm~\ref{alg:labeling}), but the practical routing value of death avoidance requires $P > 0$.
16	
17	Of 245 episodes, 150 (61.2\%) are ties---neither strategy outperforms the other---indicating that routing is relevant in only 38.8\% of episodes. Among these, death avoidance dominates. The Death Avoidance Factor, a derived penalty-dependent measure, quantifies death's contribution to the total performance gap: DAF $= 90.4\%$ at $P{=}100$ ($\Delta_{\text{full}} = +29.60$, $\Delta_{\text{nd}} = +2.84$; 95\% CI: $[81.1\%, 99.0\%]$, episode-level bootstrap, $B{=}10{,}000$). DAF varies with penalty magnitude ($50.4\%$ at $P{=}10$; $82.6\%$ at $P{=}50$; Appendix~\ref{app:penalty}), confirming that the 78.9\% label fraction provides the more robust characterization. When $\Delta_{\text{nd}} \to 0$, DAF $\to 1$ is algebraic necessity regardless of actual death dominance; conversely, when $\Delta_{\text{nd}} < 0$ (as in Reflexion $N{\geq}3$; \S\ref{sec:agent-improvement}), DAF exceeds 100\%, reflecting that death asymmetry more than accounts for the full gap.
18	
19	\paragraph{Per-task correlation structure.}
20	The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic (2.6$\times$), consistent with the internal strategy's reliance on self-generated observations that compound prediction errors across steps. Per-task, death rate differential correlates with $\Delta_{\text{full}}$ ($r = 0.97$, $p < 10^{-6}$; Figure~\ref{fig:decomposition}; Appendix~\ref{app:correlation}). Since $P$ is constant across all task types, $\Delta_{\text{full}} = P \cdot \delta + \Delta_{\text{nd}}$ makes $\Delta_{\text{full}}$ a linear function of $\delta$ with residual $\Delta_{\text{nd}}$; when DAF $\rightarrow 1$, this residual vanishes and $r \rightarrow 1$ by construction. The near-perfect correlation is therefore a mathematical consequence of death dominance, not an independent empirical finding. We retain it as an internal consistency check. The correlation drops below significance at $P \leq 25$ (Appendix~\ref{app:penalty}). Of 245 episodes, 86 are \texttt{det\_preferred}, 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preference}.
21	
22	\paragraph{Signal concentration and binary structure.}
23	The Signal Concentration Index (SCI $= 0.2147$; Appendix~\ref{app:sci}) confirms low concentration: the top-3 task types account for only $39.8\%$ of total death-rate differential. The aggregate 78.9\% reflects a per-task binary structure: all 10 death-prone task types produce 100\% death-asymmetry labels, while \texttt{find-non-living-thing} (zero deaths, $\Delta = +9.58$ from non-death scores) produces 0\%. The framework thus diagnoses a binary property (``is this environment death-dominated?'') rather than a continuous routing signal. Removing \texttt{find-non-living-thing} raises the label fraction to 100\% and DAF to 96.8\% (Appendix~\ref{app:loto-daf}).
24	
25	\paragraph{Sensitivity and seed robustness.}
26	Non-clustered episode-level bootstrap ($B = 10{,}000$) yields 95\% CI $[81.1\%, 99.0\%]$ for DAF, independent of cluster assumptions, with Cohen's $d = 3.02$ (interpret cautiously given $K{=}11$ task types). Leave-one-task-out analysis confirms stability (label fraction range: 75.9\%--78.9\%; Appendix~\ref{app:loto-daf}); an independent seed replication ($N{=}220$) yields DAF $= 89.7\%$, within 0.7~pp (Appendix~\ref{app:seed-robustness}). As a conservative check, wild cluster bootstrap treating each task type as a cluster yields $p = 0.002$; however, with $K{=}11$ clusters this test falls below the $K{\geq}20$--$40$ threshold recommended for reliable inference~\citep{cameron-2008,webb-2023}, so we rely on the non-clustered bootstrap as primary. All 28 death-prone tasks share the same direction (Appendices~\ref{app:wild-cluster}--\ref{app:per-task-ci}).
27	
28	\subsection{Multi-Model Validation}
29	\label{sec:cross-model}
30	
31	A Llama-3.1-8B-Instruct~\citep{llama3-2024} cross-model replication across all 11 task types ($N{=}220$) confirms that death dominance replicates across model families: internal death rate $41.4\%$ vs.\ deterministic $11.4\%$ (death-rate differential $+30.0$~pp), DAF $= 88.2\%$ ($\Delta_{\text{full}} = +33.17$, $\Delta_{\text{nd}} = +3.9$), with direction consistency 10/10 on death-prone tasks, 83 deterministic-preferred, 3 internal-preferred (1.4\%, all death-asymmetry reversals), and 134 no-preference labels.
32	Both models exhibit nearly identical internal vulnerability (${\sim}$42\%: Qwen $42.9\%$, Llama $41.4\%$), confirming that death-prone failure is structurally determined; the differential magnitude varies ($+26.5$~pp Qwen, $+30.0$~pp Llama) because deterministic strategy safety is model-dependent ($16.3\%$ vs.\ $11.4\%$).
33	\texttt{identify-life-stages-1} shows cross-model precision matching ($55\%$/$10\%$/$+45$~pp in both models).
34	\texttt{find-non-living-thing} shows zero deaths in both models, consistent with its majority-class answer distribution (\S\ref{sec:discussion}). Cross-model routing transfer is vacuously correct: Llama produces zero internal-preferred episodes, so Qwen-derived routing rules (always-deterministic) trivially match, confirming that routing signal is environment-determined rather than model-specific.
35	Both models are in the 7--8B range; $10{\times}$ scaling (\S\ref{sec:agent-improvement}) confirms that death dominance persists across capability levels (Appendix~\ref{app:cross-model}).
36	
37	\subsection{Agent Improvement Baselines}
38	\label{sec:agent-improvement}
39	
40	\begin{table}[t]
41	\centering
42	\small
43	\begin{tabular}{@{}lrr@{}}
44	\toprule
45	Condition & Death\% & $N$ \\
46	\midrule
47	Single-trial baseline & 42.9 & 245 \\
48	Reflexion ($3{\times}$) & 31.4 & 220 \\
49	Qwen2.5-72B ($10{\times}$) & 30.6 & 255 \\
50	Deterministic baseline & 16.3 & 245 \\
51	\midrule
52	\multicolumn{3}{@{}l}{\textit{10 death-prone tasks only:}} \\
53	Death-prone baseline & 48.0 & 200 \\
54	Retry ($5{\times}$) & 43.5 & 200 \\
55	\bottomrule
56	\end{tabular}
57	\caption{Internal-strategy death rates under agent improvement methods. Top: all 11 tasks (72B: independently collected at both internal and deterministic). Bottom: 10 death-prone tasks (\texttt{find-non-living-thing} excluded, 0\% death at all scales). All interventions reduce death rate but none approaches deterministic-level safety.}
58	\label{tab:agent-improvement}
59	\end{table}
60	
61	We test whether agent-level improvement reduces death dominance (Table~\ref{tab:agent-improvement}). Retry ($N{=}5$ attempts without self-correction) yields marginal reduction on death-prone tasks ($43.5\%$ vs.\ $48.0\%$ baseline, $\Delta = -4.5$~pp). Reflexion~\citep{reflexion-2023} (verbal self-reflection between trials) reduces death to 31.4\% across all 11 tasks by rescuing 29.3\% of first-trial deaths, but the gap to deterministic remains 15.1~pp; on the 10 death-prone tasks, Reflexion achieves ${\sim}$35\%. Under Reflexion ($N{=}3$, matched-episode analysis), $\Delta_{\text{nd}} = -0.47$, yielding DAF $> 100\%$: the deterministic advantage is entirely attributable to death avoidance, and in non-death episodes the self-correcting agent slightly outperforms the deterministic baseline. Scaling to Qwen2.5-72B ($10{\times}$ parameters; both internal and deterministic strategies independently collected at 72B, 255 episodes across all 11 task types) reduces death rate to $30.6\%$. The 72B deterministic strategy achieves $2.75\%$ death rate ($\Delta\text{DR} = +27.8$~pp), and $\Delta_{\text{nd}} = +2.28$, yielding DAF $= 92.4\%$ (7B: $90.4\%$); scaling lowers death rate but leaves death dominance intact.
62	
63	\paragraph{Dose-response analysis.}
64	We extend both interventions to $N{=}5$ trials on death-prone tasks ($n{=}200$; Figure~\ref{fig:dose-response}). Retry is nearly flat ($48.0\% \to 43.5\%$, $\Delta = -4.5$~pp over five trials). Reflexion drops steeply to $34.0\%$ at $N{=}3$ ($\Delta = -13.5$~pp, $z = 2.75$, $p = 0.003$) then plateaus ($34$--$36.5\%$ for $N \geq 3$, pairwise $p > 0.5$). With $n{=}200$ paired episodes, the minimum detectable effect is ${\sim}8$~pp ($\alpha = 0.05$, 80\% power): the key $N{=}1{\to}3$ decline is well-powered; the plateau claim ($N{=}3{\to}5$, $+1.0$~pp) is also supported, since a ${\geq}8$~pp improvement would be detected. We characterize this as suggestive evidence of a Reflexion ceiling rather than a conclusive demonstration. Retry's per-trial conditional death rate stays constant at ${\sim}48\%$; Reflexion's declines to ${\sim}31\%$ by Trial~3 (per-task breakdown in Appendix~\ref{app:dose-response}).
65	
66	\begin{figure}[t]
67	\centering
68	\includegraphics[width=\columnwidth]{figures/dose_response.pdf}
69	\caption{Death rate as a function of trial count ($N$) for Retry and Reflexion on 10 death-prone tasks ($n{=}200$). Retry (blue) is nearly flat; Reflexion (red) drops steeply through $N{=}3$ then plateaus. Horizontal lines: 72B scaling baseline ($30.6\%$, all 11 tasks) and deterministic baseline ($16.3\%$). Error bands: Wilson 95\% CIs.}
70	\label{fig:dose-response}
71	\end{figure}
72	
73	\subsection{Cross-Environment Boundary Probes}
74	\label{sec:math-contrast}
75	\label{sec:cross-env}
76	
77	We examine MATH and ALFWorld as boundary probes---not cross-domain validation---testing framework applicability across environments that instantiate ``deterministic computation'' differently (oracle simulator, code interpreter, admissible-action enumeration).
78	
79	\paragraph{MATH.} On MATH Level~4--5~\citep{math-2021} ($N{=}795$, code interpreter), internal reasoning and code interpretation achieve near-identical accuracy ($73.5\%$ vs.\ $73.0\%$, McNemar $p = 0.81$), with 74.6\% no-preference. Without catastrophic failure, no routing signal emerges.
80	
81	\paragraph{ALFWorld.} ALFWorld~\citep{alfworld-2021} (6 task types, 135 games) provides the deterministic strategy with admissible actions---an information asymmetry rather than a computation mode switch. Of 37 non-tie labels, 35 (94.6\%) favor the information-advantaged strategy, a one-directional dominance driven by information asymmetry rather than catastrophic failure (per-task-type breakdown in Appendix~\ref{app:cross-env-details}, Table~\ref{tab:alfworld-pertask}). The framework diagnoses this qualitatively different mechanism without modification.
82	
83	\subsection{Baselines}
84	\label{sec:baselines}
85	
86	\begin{table}[t]
87	\centering
88	\small
89	\resizebox{\columnwidth}{!}{%
90	\begin{tabular}{@{}lccc@{}}
91	\toprule
92	Strategy & Score & 95\% CI & Death \% \\
93	\midrule
94	Always-Internal & $-39.07$ & [$-46.40$, $-32.27$] & 42.9 \\
95	Always-Deterministic & $-9.47$ & [$-14.71$, $-4.29$] & 16.3 \\
96	Random & $-22.38$ & [$-28.67$, $-15.75$] & 27.8 \\
97	Oracle & $-6.58$ & [$-11.54$, $-1.70$] & 14.3 \\
98	\midrule
99	Trained Router$^\dagger$ & $-10.70$ & [$-16.33$, $-5.27$] & 17.6 \\
100	\bottomrule
101	\end{tabular}}
102	\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 20--40 episodes per type, 245 total). $\dagger$\,Single random seed (42) per episode pair; see Appendix~\ref{app:seed-robustness} for 8-seed robustness analysis.}
103	\label{tab:baselines}
104	\end{table}
105	
106	Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points. The oracle improves only to $-6.58$, with 96.3\% of decisions matching always-deterministic---an \emph{oracle degeneracy} where an always-deterministic lookup achieves 90.5\% of non-tie oracle decisions (balanced accuracy 50.0\%: perfect deterministic recall, zero internal recall).
107	
108	\subsection{Router Training: A Negative Result}
109	\label{sec:router-diagnostic}
110	
111	We probe whether counterfactual labels can train a step-level router, as a diagnostic of label informativeness. The oracle margin (2.89 points) caps routing upside. The near-chance step-level accuracy admits two interpretations: (A)~episode-level labels projected onto steps create ${\sim}$88\% uninformative signal (60.3\% pre-event neutral, 27.4\% post-event), drowning learnable patterns in noise; (B)~routing signal is genuinely task-type-level---there is no step-level pattern to learn. Directional conflict is only 0.3\% of 2{,}040 training steps (labels are directionally correct in 99.7\% of informative steps), but the granularity mismatch leaves minimal signal for the router. The data scaling ablation (25\%--800\%, no improvement) and the extreme class imbalance of death-asymmetry episodes (86/95 $= 90.5\%$ deterministic-preferred) point to extreme class imbalance in routing labels. The convergence of data scaling, class imbalance, and structural arguments favors Interpretation~B (non-learnability): routing signal is genuinely task-type-level, not step-level learnable---though we cannot definitively rule out Interpretation~A.
112	
113	An implicit router (Qwen3, LoRA; Appendix~\ref{app:router-details}) trained at three scales (0.6B, 1.7B, 4B) shows flat step-level balanced accuracy ($56$--$59\%$). At episode level, only 4B exceeds always-deterministic ($59.0 \pm 1.9\%$, $p < 0.005$); 0.6B and 1.7B remain at chance. Episode-level independent evaluation yields $47.1 \pm 2.2\%$, below the majority-vote baseline of 50.0\%; this independent set includes held-out task types, so the below-chance result reflects cross-task transfer failure rather than overall router incompetence. Training uses episode-level splits (Appendix~\ref{app:router-details}), ensuring no within-episode leakage. The high uninformative rate connects to noisy-label learning~\citep{natarajan2013learning}: standard ERM on labels with ${\sim}$88\% noise yields near-chance classifiers, consistent with our results.
114	
115	\paragraph{End-to-end deployment.} The 4B router deployed end-to-end ($N{=}245$) scores $-12.03$ (95\% CI: $[-17.82, -6.45]$), not exceeding always-deterministic ($-9.47$). Paraphrase-based augmentation ($25\%$--$800\%$) provides no improvement; the $3.7\%$ internal-preferred base rate makes real-data collection expensive (Appendices~\ref{app:seed-robustness}--\ref{app:ablations}).
116	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e12564f-1896-4eb3-ab55-cb20a06ad1dd",
  "isSidechain": true,
  "promptId": "87127d5f-9fda-46aa-9632-72943c579a6b",
  "agentId": "a9d6419e05e089045",
  "type": "user",
  "uuid": "8586c87f-3c58-4d97-98a7-50b43c6a8b3e",
  "sourceToolAssistantUUID": "4e12564f-1896-4eb3-ab55-cb20a06ad1dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T07:37:49.423Z_

<details open><summary>🔧 Tool call — Read · `toolu_013J5Jdwy81FaejccJUkdPYg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8586c87f-3c58-4d97-98a7-50b43c6a8b3e",
  "isSidechain": true,
  "agentId": "a9d6419e05e089045",
  "requestId": "req_011CbDSQ4jZzAxwPZdTA1u53",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "239b6808-8cf1-4bfa-8b28-7cbe92c45842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PidFvsJYSdV3piXvrTmkhg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21907,
      "cache_read_input_tokens": 8264,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 21907
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 181,
          "cache_read_input_tokens": 8264,
          "cache_creation_input_tokens": 21907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 21907,
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

_source line 7 · 2026-05-20T07:37:49.699Z_

<details><summary>↩ Tool result · `toolu_013J5Jdwy81FaejccJUkdPYg`</summary>

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
11	\graphicspath{{figures/}}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{algorithm}
16	\usepackage{algorithmic}
17	
18	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	\input{introduction}
27	\input{method}
28	\input{experiments}
29	\input{related_work}
30	\input{discussion}
31	\input{conclusion}
32	
33	\section*{Limitations}
34	
35	\paragraph{Environmental scope.}
36	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct), though extended validation of representative excluded tasks confirms the pattern (Appendix~\ref{app:extended-validation}). The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface non-death-dominated signal that our current setup does not capture. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:cross-env}, \S\ref{sec:discussion}) provide preliminary supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct cross-model replication (11 task types, $N{=}220$; \S\ref{sec:cross-model}) shows death dominance replicates with direction consistency 10/10 while vulnerability magnitude varies ($+30.0$~pp vs.\ Qwen $+26.5$~pp), though both models are in the 7--8B parameter range; Qwen2.5-72B ($10{\times}$ scale) reduces death rate but does not eliminate death dominance (\S\ref{sec:agent-improvement}); validation beyond 72B remains future work. Our quantitative results (DAF $= 90.4\%$, label fractions) are specific to ScienceWorld; the framework's generality claim is methodological (the diagnostic procedure applies to any environment with asymmetric fatal outcomes), not empirical (the specific percentages may differ across environments).
37	
38	\paragraph{Methodological constraints.}
39	Our internal-reasoning baseline uses single-pass ReAct~\citep{react-2023}. Reflexion~\citep{reflexion-2023} reduces death rate from 42.9\% to 31.4\% (\S\ref{sec:agent-improvement}), but more aggressive self-correction or Tree-of-Thought backtracking~\citep{tot-2023} may further reduce internal death rates. Episode-level labels assign a single routing preference to entire episodes, which may be suboptimal for individual steps (particularly those preceding death events). However, of 2{,}040 training steps only 0.3\% exhibit strict directional conflict (step-level oracle opposite to episode label); the remaining apparent mislabeling consists of episode labels applied to steps where neither strategy has a step-level advantage (60.3\% pre-event neutral). The issue is granularity mismatch---applying correct-direction labels to uninformative steps---not directional error. Training on pure-strategy trajectories also introduces distribution shift at deployment~\citep{dagger-2011}. Under mixed-strategy routing with oracle death prediction, switching to deterministic at the step before death could reduce the internal death rate; even under optimistic assumptions (perfect step-level death prediction), a residual gap of ${>}10$~pp between strategies is expected, as fatal trajectories involve cumulative hallucination errors preceding the death event. More broadly, projecting episode-level labels onto 10--50 sequential steps with path-dependent state introduces compounding error: early routing decisions alter the state trajectory, potentially invalidating later labels derived from the episode outcome.
40	
41	\paragraph{Statistical limitations.}
42	Episodes within the same task type are not fully independent because they share environment dynamics, though they use different random seeds. Cluster bootstrap with $K{=}11$ task-type clusters yields wider CIs ($[73.0\%, 100\%]$); with $K < 40$ clusters, these should be interpreted cautiously~\citep{cameron-2008,webb-2023}. A wild cluster bootstrap ($K{=}11$, $p < 0.001$; Appendix~\ref{app:wild-cluster}) and 100\% directional consistency across all 28 death-prone tasks (Appendix~\ref{app:per-task-ci}) mitigate this concern.
43	
44	\section*{Ethics Statement}
45	
46	This work uses ScienceWorld \cite{scienceworld-2022}, a publicly available text-based simulation environment, and does not involve human subjects or private data. All evaluation environments (ScienceWorld, ALFWorld, MATH) are released under permissive open-source licenses (Apache 2.0 / MIT). All models used (Qwen2.5 family, Llama-3.1-8B) are publicly available for research use. All language models are accessed via standard APIs or publicly released weights. Experiments were conducted on 2$\times$ NVIDIA RTX 5090 (32GB) and 4$\times$ NVIDIA RTX 6000 PRO (96GB), totaling approximately 200 GPU-hours for data collection, router training, and evaluation. Code and data will be released upon acceptance.
47	
48	\bibliography{references}
49	
50	\appendix
51	
52	\noindent\textbf{Appendix Overview.}
53	\hyperref[app:sci]{A.~Signal Concentration Index} $\cdot$
54	\hyperref[app:labeling]{B.~Labeling Quality Audit} $\cdot$
55	\hyperref[app:per-task]{C.~Per-Task Decomposition} $\cdot$
56	\hyperref[app:correlation]{D.~Correlation Robustness} $\cdot$
57	\hyperref[app:wild-cluster]{E.~Wild Cluster Bootstrap} $\cdot$
58	\hyperref[app:per-task-ci]{F.~Per-Task CIs} $\cdot$
59	\hyperref[app:loto-daf]{G.~Leave-One-Task-Out DAF} $\cdot$
60	\hyperref[app:dose-response]{H.~Dose-Response Breakdown} $\cdot$
61	\hyperref[app:router-details]{I.~Router Training Details} $\cdot$
62	\hyperref[app:seed-robustness]{J.~Seed Robustness} $\cdot$
63	\hyperref[app:penalty]{K.~Penalty Sensitivity} $\cdot$
64	\hyperref[app:cross-env-details]{L.~Cross-Environment Details} $\cdot$
65	\hyperref[app:cross-model]{M.~Cross-Model Verification} $\cdot$
66	\hyperref[app:failure-modes]{N.~Failure Mode Analysis} $\cdot$
67	\hyperref[app:grounding-ablation]{O.~Grounding Ablation} $\cdot$
68	\hyperref[app:ablations]{P.~Ablation Studies} $\cdot$
69	\hyperref[sec:threshold-routing]{Q.~Threshold Routing} $\cdot$
70	\hyperref[app:decision-framework]{R.~Decision Framework} $\cdot$
71	\hyperref[app:extended-validation]{S.~Extended Validation}
72	
73	\section{Signal Concentration Index}
74	\label{app:sci}
75	
76	Let $K$ denote the number of task types and $c_k$ the contribution of task type $k$ to the aggregate routing signal, defined as the fraction of total death-rate differential attributable to task $k$:
77	\begin{equation}
78	    c_k = \frac{n_k \cdot \delta_k}{\sum_{j=1}^{K} n_j \cdot \delta_j}
79	\end{equation}
80	where $n_k$ is the number of episodes and $\delta_k = d_k^{\tt int} - d_k^{\tt det}$ is the per-task death-rate differential. The SCI is the Gini coefficient over $\{c_1, \ldots, c_K\}$:
81	\begin{equation}
82	    \text{SCI} = \frac{\sum_{i=1}^K \sum_{j=1}^K |c_i - c_j|}{2K \sum_{k=1}^K c_k}
83	\end{equation}
84	
85	\section{Labeling Quality Audit}
86	\label{app:labeling}
87	
88	\begin{algorithm}[t]
89	\caption{Episode-Level Counterfactual Labeling}
90	\label{alg:labeling}
91	\begin{algorithmic}[1]
92	\REQUIRE Task instance $t$, modalities $\mathcal{M} = \{{\tt int}, {\tt det}\}$
93	\ENSURE Label $\ell \in \{{\tt det\text{-}pref}, {\tt int\text{-}pref}, {\tt no\text{-}pref}\}$
94	\FOR{each $m \in \mathcal{M}$}
95	    \STATE Run episode $\tau_m$ with pure-strategy $m$
96	    \STATE Record score $s_m$ and death indicator $d_m$
97	\ENDFOR
98	\IF{$d_{\tt int} = 1$ \AND $d_{\tt det} = 0$}
99	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{death asymmetry}
100	\ELSIF{$d_{\tt int} = 0$ \AND $d_{\tt det} = 1$}
101	    \STATE $\ell \leftarrow {\tt int\text{-}pref}$ \COMMENT{death asymmetry}
102	\ELSIF{$d_{\tt int} = d_{\tt det} = 1$}
103	    \STATE $\ell \leftarrow {\tt no\text{-}pref}$ \COMMENT{both dead}
104	\ELSIF{$s_{\tt det} > s_{\tt int}$}
105	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{score comparison}
106	\ELSIF{$s_{\tt int} > s_{\tt det}$}
107	    \STATE $\ell \leftarrow {\tt int\text{-}pref}$ \COMMENT{score comparison}
108	\ELSE
109	    \STATE $\ell \leftarrow {\tt no\text{-}pref}$ \COMMENT{tied alive}
110	\ENDIF
111	\RETURN $\ell$
112	\end{algorithmic}
113	\end{algorithm}
114	
115	A potential concern is oracle circularity: whether episode-level labels reflect tie-breaking artifacts rather than genuine computation mode differences. We audit all 245 labels. Of the 150 \texttt{no\_preference} labels (61.2\%), 115 (46.9\%) are both-alive ties and 35 (14.3\%) are both-dead, all excluded from router training. The remaining 95 training labels are entirely genuine: 75 from death asymmetry (70 deterministic-preferred, 5 internal-preferred) and 20 from score comparison with both strategies surviving (16 deterministic-preferred, 4 internal-preferred). Zero labels depend on tie-breaking. Retraining the router using only death-asymmetry labels yields step-level balanced accuracy of 57.3\%, within 1$\sigma$ of the full-label retrain (57.6 $\pm$ 0.5\%, step-level Trainer evaluation); score-comparison labels contribute negligible additional signal. (Step-level metrics are used here for the relative comparison; as shown in \S\ref{sec:router-diagnostic}, absolute generalization to new episodes is near chance.) The 97.4\% step-level tie rate (\S\ref{sec:collection}) further motivates episode-level over step-level labeling.
116	
117	\section{Per-Task Decomposition}
118	\label{app:per-task}
119	We select 11 of ScienceWorld's 30 task types for analysis. Types are excluded when they were used for pipeline development (5 tasks, standard hold-out practice), are taxonomically redundant with a retained family representative (7 tasks), or exhibit near-zero task progress under both strategies (7 tasks, agent capability floor).\footnote{Excluded tasks exhibit even stronger death dominance than included tasks ($\Delta\text{DR} = +38.2$\,pp vs.\ $+28.7$\,pp; Table~\ref{tab:excluded-death}).}
120	
121	\begin{table}[h]
122	\centering
123	\scriptsize
124	\setlength{\tabcolsep}{2.5pt}
125	\begin{tabular}{@{}lrrccc@{}}
126	\toprule
127	Task & $n$ & $\Delta_\text{full}$ & D\%\textsubscript{int} & D\%\textsubscript{det} & D / I / N \\
128	\midrule
129	id-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\
130	lifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\
131	lifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\
132	inclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\
133	freeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\
134	meas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\
135	id-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\
136	find-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\
137	grow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\
138	chem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\
139	\midrule
140	find-non-living-thing$^\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\
141	\midrule
142	\textbf{All (11 tasks)} & \textbf{245} & $\mathbf{+29.60}$ & \textbf{42.9} & \textbf{16.3} & \textbf{86 / 9 / 150} \\
143	\bottomrule
144	\end{tabular}
145	\caption{Per-task decomposition of the death avoidance effect. D\%: death rate for internal (int) and deterministic (det) strategies. D/I/N: episode labels (det-preferred / internal-preferred / no-preference). Sorted by $\Delta_{\text{full}}$ descending. The \textit{All} row is an episode-weighted aggregate across 245 episodes. $\dagger$\,Only task with zero deaths under both strategies; $n{=}40$ because data was collected in two batches, with the second batch adding 20 episodes to increase statistical power for this zero-death outlier.}
146	\label{tab:per-task}
147	\end{table}
148	
149	\paragraph{Task selection and anti-cherry-picking.}
150	Eighteen of the 19 excluded task types (95\%) exhibit death-asymmetric patterns (Table~\ref{tab:excluded-death}): internal-reasoning death rates range from 40\% to 60\% (mean 53.9\%), while deterministic death rates range from 0\% to 40\% (mean 15.8\%), yielding a mean death-rate differential of $+38.2$\,pp, exceeding the $+28.7$\,pp for included tasks. The included subset is thus \emph{less} death-asymmetric than the excluded subset, the opposite of what a cherry-picking hypothesis would predict. The sole exception is \texttt{grow-plant}, an intrinsically safe task with zero deaths under both strategies, paralleling \texttt{find-non-living-thing} in the included set. The 19 excluded tasks fall into three independently motivated categories: five used during pipeline development (standard hold-out practice), seven taxonomically redundant with included family representatives (deduplication), and seven where the 7B backbone achieves near-zero task progress regardless of strategy (agent capability floor). In no case was a task excluded because death dominance was absent. Exclusion is driven by absence of non-death routing signal ($\Delta_{\text{nd}} = 0$ for 53\% of excluded tasks) and standard deduplication practices. \texttt{find-non-living-thing} serves as an internal counterexample: zero deaths under both strategies yet included because it exhibits non-death routing signal ($\Delta_{\text{full}} = +9.58$ entirely from score differences), and deterministic is not always preferred (4 of 20 non-tie labels favor internal).
151	
152	\begin{table}[t]
153	\centering
154	\scriptsize
155	\setlength{\tabcolsep}{2pt}
156	\begin{tabular}{@{}llrcccl@{}}
157	\toprule
158	Task & Grp & $n$ & D\%\textsubscript{int} & D\%\textsubscript{det} & $\Delta$DR & Excl.\ reason \\
159	\midrule
160	boil                          & A & 20 & 50 & 20 & $+30$ & dev set \\
161	change-state-of-matter        & A & 20 & 55 & 15 & $+40$ & dev set \\
162	chem-mix-paint-secondary      & A & 20 & 45 & 10 & $+35$ & dev set \\
163	grow-plant                    & A & 20 &  0 &  0 & $\phantom{+}0$  & dev set \\
164	melt                          & A & 20 & 55 & 15 & $+40$ & dev set \\
165	\midrule
166	chem-mix-paint-tertiary       & B &  5 & 40 & 20 & $+20$ & family redundancy \\
167	find-living-thing             & B &  5 & 60 & 20 & $+40$ & family redundancy \\
168	find-plant                    & B &  5 & 60 &  0 & $+60$ & family redundancy \\
169	inclined-friction-named       & B &  5 & 60 & 20 & $+40$ & family redundancy \\
170	inclined-friction-unnamed     & B &  5 & 60 &  0 & $+60$ & family redundancy \\
171	lifespan-shortest             & B &  5 & 60 & 40 & $+20$ & family redundancy \\
172	measure-melt-known            & B &  5 & 60 &  0 & $+60$ & family redundancy \\
173	\midrule
174	mendelian-known               & C &  5 & 60 & 20 & $+40$ & agent floor \\
175	mendelian-unknown             & C &  5 & 60 & 40 & $+20$ & agent floor \\
176	power-component               & C &  5 & 60 & 20 & $+40$ & agent floor \\
177	power-renewable               & C &  5 & 60 &  0 & $+60$ & agent floor \\
178	test-conductivity             & C &  5 & 60 & 20 & $+40$ & agent floor \\
179	test-conductivity-unknown     & C &  5 & 60 & 20 & $+40$ & agent floor \\
180	use-thermometer               & C &  5 & 60 & 20 & $+40$ & agent floor \\
181	\midrule
182	\textbf{Mean (19 excluded)}   &   &    & \textbf{53.9} & \textbf{15.8} & $\mathbf{+38.2}$ & \\
183	\textit{cf.\ included (11)}   &   &    & \textit{46.5} & \textit{17.8} & $\textit{+28.7}$ & \\
184	\bottomrule
185	\end{tabular}
186	\caption{Death-rate analysis of all 19 excluded task types. D\%: death rate (score $\leq -100$). $\Delta$DR = D\%\textsubscript{int} $-$ D\%\textsubscript{det}. 18 of 19 excluded tasks (95\%) exhibit positive death asymmetry ($\Delta$DR $\geq +20$\,pp). Exclusion groups: A = development set (excluded to prevent circular evaluation), B = taxonomically redundant with an included family representative, C = agent-floor tasks (backbone achieves near-zero progress regardless of strategy). The mean $\Delta$DR among excluded tasks ($+38.2$\,pp) exceeds that of included tasks ($+28.7$\,pp), confirming that task selection does not bias toward death-prone tasks. Group B--C estimates are based on $n{=}5$ prescreening episodes per task and should be interpreted as directional evidence rather than precise rate estimates.}
187	\label{tab:excluded-death}
188	\end{table}
189	
190	\section{Correlation Robustness}
191	\label{app:correlation}
192	
193	The Pearson $r = 0.9698$ reported in \S\ref{sec:death-decomp} is robust across multiple diagnostics. Spearman rank correlation is $\rho = 0.986$ ($p = 2.4 \times 10^{-8}$); the relationship is not driven by outliers or non-linearity. A nonparametric bootstrap (10{,}000 resamples) yields 95\% CI $[0.952, 0.995]$.
194	
195	\begin{table}[h]
196	\centering
197	\small
198	\begin{tabular}{@{}lr@{}}
199	\toprule
200	Task removed & $r_{\text{LOO}}$ \\
201	\midrule
202	id-life-stages-1       & 0.963 \\
203	lifespan-long          & 0.969 \\
204	lifespan-l-then-s      & 0.976 \\
205	inclined-plane         & 0.969 \\
206	freeze                 & 0.971 \\
207	meas-melt-point        & 0.972 \\
208	id-life-stages-2       & 0.972 \\
209	find-animal            & 0.970 \\
210	grow-fruit             & 0.973 \\
211	chem-mix               & 0.969 \\
212	find-non-living-thing  & 0.980 \\
213	\bottomrule
214	\end{tabular}
215	\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\ $\Delta_{\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}
216	\label{tab:loo}
217	\end{table}
218	
219	\section{Wild Cluster Bootstrap}
220	\label{app:wild-cluster}
221	
222	Episodes within the same task type share environment dynamics, raising the concern that the effective sample size is closer to $K$ (task types) than $N$ (episodes). We address this with cluster-robust inference treating each task type as a cluster ($K{=}11$, all 11 included task types, 245 episodes).
223	
224	\begin{table}[h]
225	\centering
226	\small
227	\begin{tabular}{@{}lcc@{}}
228	\toprule
229	Method & $p$-value & 95\% CI \\
230	\midrule
231	Cluster-robust $t$-test ($t{=}10.0$, df$=$10) & $< 0.001$ & $[0.73, 1.00]$ \\
232	Wild cluster bootstrap ($B{=}9{,}999$) & $< 0.001$ & $[0.73, 1.00]$ \\
233	Exact permutation ($2{,}048$ perms) & $0.002$ & --- \\
234	Sign test & $< 0.001$ & --- \\
235	\bottomrule
236	\end{tabular}
237	\caption{Cluster-level tests of death-rate asymmetry ($K{=}11$ task clusters, 245 episodes). 10 of 11 clusters show internal DR $>$ deterministic DR; the sole exception (\texttt{find-non-living-thing}) has zero deaths under both strategies. Cohen's $d = 3.02$. The exact permutation $p = 0.002$ ($4/2{,}048$) reflects the near-unanimous directional consistency.}
238	\label{tab:wild-cluster}
239	\end{table}
240	
241	\noindent All methods confirm significance with $p < 0.01$, and the 95\% CI $[0.73, 1.00]$ excludes zero by a wide margin. The $K{=}11$ analysis uses the same clusters as the main analysis, providing a direct robustness check on the primary results.
242	
243	\section{Per-Task Death Rate Confidence Intervals}
244	\label{app:per-task-ci}
245	
246	We compute bootstrap 95\% CIs for the death-rate differential ($\Delta\text{DR} = \text{DR}_{\text{int}} - \text{DR}_{\text{det}}$) for all 30 ScienceWorld task types. Of 30 tasks, 28 are death-prone (at least one death under either strategy); the remaining 2 (\texttt{grow-plant}, \texttt{find-non-living-thing}) have zero deaths under both strategies.
247	
248	Across all 28 death-prone tasks, internal DR exceeds deterministic DR without exception (100\% directional consistency). The pooled death-rate differential is $+37.3\%$ (95\% CI: $[29.7\%, 44.4\%]$). Fifteen of 28 tasks are individually significant (CI excludes zero); the 13 non-significant tasks all have $n{=}5$ prescreening episodes, where statistical power is insufficient to detect even large effects (e.g., a task with $\Delta\text{DR} = +40$\,pp at $n{=}5$ has a CI of $\pm 43$\,pp). The universal directional consistency, combined with the pooled significance, confirms that death asymmetry is not driven by a subset of outlier tasks.
249	
250	\section{Leave-One-Task-Out DAF Sensitivity}
251	\label{app:loto-daf}
252	
253	\begin{table}[h]
254	\centering
255	\small
256	\caption{Leave-one-task-out DAF sensitivity (penalty-independent label fraction). Among the 10 death-prone tasks, removing any single task changes DAF by at most 3.0\,pp (range: 75.9\%--78.9\%). Removing \emph{Find Non-Living Thing}, the sole death-free task that contributes all 20 score-comparison episodes, raises DAF to 100\% by construction.}
257	\label{tab:loto-daf}
258	\begin{tabular}{lrrr}
259	\toprule
260	Removed Task & $N_\text{rem}$ & DAF (\%) & $\Delta$ (pp) \\
261	\midrule
262	(none, full) & 245 & 78.9 & --- \\
263	\midrule
264	Find Non-Living$^\dagger$ & 205 & 100.0 & +21.1 \\
265	Lifespan Longest & 220 & 75.9 & $-$3.0 \\
266	Life Stages 1 & 225 & 76.7 & $-$2.2 \\
267	Lifespan Long+Short & 225 & 76.7 & $-$2.2 \\
268	Chemistry Mix & 225 & 77.0 & $-$1.9 \\
269	Grow Fruit & 225 & 77.3 & $-$1.7 \\
270	Inclined Plane Angle & 225 & 77.3 & $-$1.7 \\
271	Freeze & 225 & 77.5 & $-$1.4 \\
272	Life Stages 2 & 225 & 77.5 & $-$1.4 \\
273	Melt Pt Unknown & 225 & 77.5 & $-$1.4 \\
274	Find Animal & 225 & 77.8 & $-$1.2 \\
275	\bottomrule
276	\end{tabular}
277	
278	\vspace{2pt}
279	{\footnotesize $^\dagger$Only death-free task; contributes all score-comparison labels. Sorted by $|\Delta|$ descending.}
280	\end{table}
281	
282	\section{Per-Task Dose-Response Breakdown}
283	\label{app:dose-response}
284	
285	Table~\ref{tab:dose-response-detail} reports per-task death rates for Reflexion at $N{=}3$, 4, and 5 on the 10 death-prone tasks ($n{=}20$ episodes per task). Per-task variance is high (up to 25\,pp range for \texttt{measure-melting-point}), but the aggregate smooths to a 2.5\,pp band, confirming that the plateau conclusion is robust at the aggregate level despite task-level noise. \texttt{freeze} is consistently the hardest task (50--60\% DR across all $N$).
286	
287	\begin{table}[h]
288	\centering
289	\small
290	\caption{Per-task death rates (\%) for Reflexion at $N{=}3$, 4, 5 on 10 death-prone tasks ($n{=}20$ per task). Aggregate death rates confirm the plateau at $N \geq 3$ (range: $34.0$--$36.5\%$).}
291	\label{tab:dose-response-detail}
292	\begin{tabular}{@{}lrrr@{}}
293	\toprule
294	Task & $N{=}3$ & $N{=}4$ & $N{=}5$ \\
295	\midrule
296	chemistry-mix & 25.0 & 35.0 & 20.0 \\
297	find-animal & 45.0 & 30.0 & 45.0 \\
298	freeze & 50.0 & 50.0 & 60.0 \\
299	grow-fruit & 30.0 & 25.0 & 25.0 \\
300	identify-life-stages-1 & 35.0 & 35.0 & 35.0 \\
301	identify-life-stages-2 & 25.0 & 25.0 & 30.0 \\
302	inclined-plane-angle & 20.0 & 30.0 & 35.0 \\
303	lifespan-longest & 45.0 & 40.0 & 40.0 \\
304	lifespan-long+short & 30.0 & 45.0 & 35.0 \\
305	measure-melting-pt & 35.0 & 50.0 & 25.0 \\
306	\midrule
307	\textbf{Aggregate} & \textbf{34.0} & \textbf{36.5} & \textbf{35.0} \\
308	\bottomrule
309	\end{tabular}
310	\end{table}
311	
312	\section{Router Training Details}
313	\label{app:router-details}
314	
315	We use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.
316	
317	With gradient accumulation of 1 (effective batch size 4), routing performance is highly sensitive to the evaluation split; this suggests overfitting to specific train/validation partition boundaries. With gradient accumulation of 8 (effective batch size 32), step-level performance stabilizes across splits (${\sim}54\%$ balanced accuracy). All reported results use gradient accumulation 8.
318	
319	Under step-level evaluation with a fixed data split, cross-seed balanced accuracy ranges from 52.7\% to 58.1\%, but internal recall varies from 51.5\% to 81.8\%, which reflects threshold sensitivity. However, episode-level evaluation reveals that this apparent discrimination does not generalize: balanced accuracy drops to $47.1 \pm 2.2\%$ across 8 cross-split seeds (Appendix~\ref{app:seed-robustness}). Deployed end-to-end, the trained router allocates 97.0\% of episodes to deterministic computation with 17.6\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.
320	
321	\paragraph{Evaluation methods.} All results use \emph{generation-based evaluation}: the model generates a routing label as text (\texttt{enable\_thinking=False}), parsed for classification. We evaluate at two granularities: \emph{step-level} (steps from the same episode may appear in both train and validation sets) and \emph{episode-level} (entire episodes held out). Step-level accuracy ($54.1 \pm 5.4\%$) exceeds chance (the router captures some signal), but episode-level accuracy ($47.1 \pm 2.2\%$, below chance) shows this does not generalize to unseen episodes. Augmentation-based data scaling (Appendix~\ref{app:seed-robustness}) provides no improvement; real-data scaling remains open. Always-deterministic is trivially near-optimal given DAF $= 90.4\%$. The main text (\S\ref{sec:router-diagnostic}) reports controlled 4-seed results at three scales; the model-size ablation (Appendix~\ref{app:ablations}) provides further detail.
322	
323	\begin{table}[h]
324	\centering
325	\small
326	\resizebox{\columnwidth}{!}{%
327	\begin{tabular}{@{}lcc@{}}
328	\toprule
329	Hyperparameter & Classification Head & Implicit Router \\
330	\midrule
331	Base model & Qwen3-1.7B & Qwen3-1.7B \\
332	Architecture & Linear + LoRA & SFT + LoRA \\
333	LoRA $r$ / $\alpha$ & 16 / 32 & 16 / 32 \\
334	Learning rate & 2e-5 & 2e-4 \\
335	Optimizer & AdamW & AdamW \\
336	Epochs & 3 & 3 \\
337	Batch size (per device) & 4 & 4 \\
338	Gradient accumulation & 8 & 8 \\
339	Warmup ratio & 0.1 & 0.1 \\
340	Weight decay & 0.01 & 0.01 \\
341	Max sequence length & 512 & 512 \\
342	Seeds & \{42\} & \{42, 123, 456, 789\} \\
343	\bottomrule
344	\end{tabular}}
345	\caption{Router training hyperparameters. Both architectures use the same base model with LoRA adaptation. The classification head degenerates across all configurations; the implicit router results are reported as 4-seed mean$\pm$std.}
346	\label{tab:hyperparams}
347	\end{table}
348	
349	\section{Seed Robustness}
350	\label{app:seed-robustness}
351	
352	We assess router generalization at two evaluation granularities: \emph{step-level}, where steps from the same episode may appear in both train and validation sets, and \emph{episode-level}, where entire episodes are held out. Both use cross-split evaluation (seeds $\{42, \ldots, 49\}$, 8 seeds total), where the data partition and training seed both vary. Table~\ref{tab:seed-robustness} reports per-seed results.
353	
354	\begin{table}[h]
355	\centering
356	\small
357	\begin{tabular}{@{}llcc@{}}
358	\toprule
359	Eval.\ Granularity & Seed & Bal.\ Acc.\ (\%) \\
360	\midrule
361	Step-level & 42 & 57.06 \\
362	(same-episode & 43 & 63.99 \\
363	leakage) & 44 & 55.43 \\
364	 & 45 & 56.14 \\
365	 & 46 & 55.45 \\
366	 & 47 & 50.08 \\
367	 & 48 & 48.03 \\
368	 & 49 & 59.30 \\
369	\cmidrule{2-3}
370	 & Mean$\pm$std & $54.1 \pm 5.4$ \\
371	\midrule
372	Episode-level & 42 & 48.1 \\
373	(held-out & 43 & 47.9 \\
374	episodes) & 44 & 49.6 \\
375	 & 45 & 49.4 \\
376	 & 46 & 48.5 \\
377	 & 47 & 43.1 \\
378	 & 48 & 45.4 \\
379	 & 49 & 44.8 \\
380	\cmidrule{2-3}
381	 & Mean$\pm$std & $47.1 \pm 2.2$ \\
382	\midrule
383	\multicolumn{2}{@{}l}{Always-det (= majority-vote)} & 50.0 \\
384	\bottomrule
385	\end{tabular}
386	\caption{Per-seed router performance under cross-split evaluation (8 seeds, generation-based, \texttt{enable\_thinking=False}). Step-level evaluation allows steps from the same episode in both train and validation sets (same-episode leakage). Episode-level evaluation holds out entire episodes; the resulting $47.1 \pm 2.2\%$ is below the 50\% chance baseline. A data scaling ablation (Table~\ref{tab:data-scaling}) confirms this failure persists under the current data distribution and augmentation regime.}
387	\label{tab:seed-robustness}
388	\end{table}
389	
390	The contrast between step-level ($54.1 \pm 5.4\%$) and episode-level ($47.1 \pm 2.2\%$) evaluation reveals a generalization gap: the step-level signal likely reflects memorization of episode-specific context (enabled by same-episode leakage) rather than extraction of generalizable routing features. At episode level, the router performs below chance across all 8 seeds (range: 43.1\%--49.6\%). Augmentation-based data scaling (Table~\ref{tab:data-scaling}) from 25\% to 800\% ($32{\times}$ range) provides no improvement, converging to the always-deterministic baseline ($50\%$). However, paraphrase augmentation inflates the majority class without generating novel routing patterns; real-data scaling remains an open question. With DAF $= 90.4\%$ and all task types deterministic-majority (86:9 label ratio), always-deterministic trivially solves the episode-level routing problem, leaving no learnable signal for a step-level router.
391	
392	\paragraph{Data scaling ablation.} To test whether the episode-level generalization failure stems from data scarcity, we vary training set size from 25\% to 800\% of the original via paraphrase-based data augmentation (synonym substitution + template variation on step observations), holding the episode-level validation set fixed. Table~\ref{tab:data-scaling} reports the results.
393	
394	\begin{table}[h]
395	\centering
396	\small
397	\begin{tabular}{@{}rccc@{}}
398	\toprule
399	Scale & Samples & Det\% & Ep.\ Bal.\ Acc.\ (\%) \\
400	\midrule
401	25\% & 433 & ${\sim}90$ & $49.5 \pm 0.3$ \\
402	50\% & 867 & ${\sim}90$ & $51.5$ \\
403	100\% & 1{,}735 & 89.6 & $49.9 \pm 0.1$ \\
404	200\% & 3{,}470 & 94.2 & $50.0 \pm 0.0$ \\
405	800\% & 13{,}880 & ${\sim}97.7$ & $51.0 \pm 1.1$ \\
406	\midrule
407	Always-det & --- & --- & 50.0 \\
408	\bottomrule
409	\end{tabular}
410	\caption{Data scaling ablation: episode-level balanced accuracy across training set sizes (25\%--800\% of original, $32{\times}$ range). Internal recall $= 0.0$ at all scales (complete majority-class collapse). Det\%: fraction of deterministic-preferred labels in training data. The 50\% scale is a single seed; all others report mean$\pm$std across seeds.}
411	\label{tab:data-scaling}
412	\end{table}
413	
414	All scales hover at ${\sim}50\%$ episode-level balanced accuracy (equivalent to the always-deterministic baseline), with no monotonic improvement as data increases. Augmentation-based scaling provides no improvement at any scale; however, episode-level minority-class diversity remains a potential confound that cannot be resolved without collecting more internal-preferred episodes. The ground-truth internal-preferred rate (9/245 $= 3.7\%$) means collecting 50 internal-preferred episodes would require approximately 1{,}350 paired episodes at current environment dynamics, a $5.5{\times}$ expansion with diminishing return on a $9.6\%$ signal. The failure points to a limitation of the current data distribution: when DAF $= 90.4\%$ and all task types are deterministic-majority (86:9 label ratio), the episode-level routing problem is trivially solved by always choosing deterministic, leaving no learnable signal for a step-level router to exploit.
415	
416	Augmentation disproportionately increases the majority (deterministic) class: Det\% rises from 89.6\% at 100\% to 94.2\% at 200\% and ${\sim}97.7\%$ at 800\%. However, the complete collapse to majority-class prediction (internal recall $= 0.0$) occurs even at the smallest unaugmented scale (25\%, ${\sim}90\%$ det); this is not an augmentation artifact. Balanced accuracy corrects for class imbalance by averaging per-class recall, so the metric itself is not biased by the skew.
417	
418	Decomposition metrics are stable under bootstrap resampling ($B{=}10{,}000$ resamples of the 245-episode dataset): DAF $= 90.4\% \pm 4.2\%$ (95\% CI $[81.1\%, 99.0\%]$); Pearson $r = 0.975 \pm 0.011$ (95\% CI $[0.952, 0.995]$). The death avoidance dominance finding is robust to both resampling and split perturbation.
419	
420	\paragraph{Per-task-type evaluation breakdown.} To test whether the router learns transferable routing strategies or merely task-type classification, we evaluate existing checkpoints (8 seeds) separately on each of the 11 task types. Of the 11 task types, 7 have \emph{all-deterministic} labels (no internal-preferred episodes exist), making balanced accuracy undefined; the router has nothing to learn beyond the trivial always-deterministic default. For the remaining 4 task types where both classes are present, balanced accuracy ranges from 50.0\% to 73.0\%, but this apparent signal does not indicate cross-task-type routing transfer: the router is effectively classifying task types (which correlate with death risk) rather than extracting a generalizable routing strategy. This complements the data scaling ablation: routing signal does not transfer across task types because the signal \emph{is} the task type, i.e., whether a given task carries death risk. The 4B capacity scaling result (Appendix~\ref{app:ablations}) suggests capacity is one factor, but even 4B's $59.0\%$ episode-level accuracy does not demonstrate cross-task-type transfer.
421	
422	\section{Penalty Sensitivity Analysis}
423	\label{app:penalty}
424	
425	\begin{table}[h]
426	\centering
427	\small
428	\begin{tabular}{@{}rrr@{}}
429	\toprule
430	$P$ & DAF($P$) & 95\% CI \\
431	\midrule
432	0 & 7.4\% & [$-39.4$, $82.5$] \\
433	1 & 14.8\% & [$-28.6$, $89.6$] \\
434	5 & 35.4\% & [$-1.8$, $92.7$] \\
435	10 & 50.4\% & [$18.5$, $93.3$] \\
436	25 & 70.7\% & [$48.0$, $96.3$] \\
437	50 & 82.6\% & [$67.2$, $98.2$] \\
438	100\textsuperscript{*} & 90.4\% & [$81.1$, $99.0$] \\
439	200 & 94.9\% & [$89.9$, $99.5$] \\
440	500 & 97.9\% & [$95.7$, $99.8$] \\
441	\bottomrule
442	\end{tabular}
443	\caption{Sensitivity of DAF to death penalty magnitude $P$. DAF$(P) = 1 - \Delta_{\text{nd}} / \Delta_{\text{full}}(P)$, where $\Delta_{\text{full}}(P) \approx \delta \cdot P + \Delta_{\text{nd}}$, $\delta = 0.2653$ is the death-rate differential, and $\Delta_{\text{nd}} = 2.84$ (strict neither-died filtering). Recomputed from 245 episode-level data; bootstrap 95\% CIs ($B{=}10{,}000$). \textsuperscript{*}Default setting.}
444	\label{tab:penalty-sensitivity}
445	\end{table}
446	
447	The non-death score gap $\Delta_{\text{nd}} = 2.84$ is invariant across penalty levels; it depends only on surviving-episode performance, not on $P$. As $P$ increases, $\Delta_{\text{full}}$ grows ($16.33$ at $P{=}50$, $29.60$ at $P{=}100$, $56.13$ at $P{=}200$) while $\Delta_{\text{nd}}$ remains fixed, mechanically increasing DAF.
448	
449	\paragraph{Mechanism boundary: death specificity.}
450	The $r = 0.97$ correlation between per-task death-rate differential and $\Delta_{\text{full}}$ is specific to catastrophic death (score $= -100$). Broader failure definitions dissolve the correlation entirely: defining ``failure'' as any non-positive score ($T{=}0$) yields $r = -0.13$ ($p = 0.70$), because non-death episodes show near-zero performance differential between strategies ($\Delta_{\text{nd}} = 2.84$). Table~\ref{tab:penalty-correlation} quantifies this specificity across penalty magnitudes.
451	
452	\begin{table}[h]
453	\centering
454	\small
455	\begin{tabular}{@{}rccl@{}}
456	\toprule
457	$P$ & $r$ & $p$ & Sig.\ ($\alpha{=}0.05$) \\
458	\midrule
459	1 & $-0.44$ & $0.178$ & No \\
460	5 & $-0.29$ & $0.382$ & No \\
461	10 & $-0.08$ & $0.813$ & No \\
462	25 & $0.51$ & $0.108$ & No \\
463	50 & $0.86$ & $0.0006$ & Yes \\
464	100\textsuperscript{*} & $0.97$ & $8 \times 10^{-7}$ & Yes \\
465	200 & $0.99$ & $1 \times 10^{-9}$ & Yes \\
466	\bottomrule
467	\end{tabular}
468	\caption{Pearson $r$ between per-task death-rate differential and $\Delta_{\text{full}}(P)$ across penalty magnitudes. The correlation is non-significant at low penalties and emerges at $P \geq 50$, which reflects the transition from non-death-dominated to death-dominated score gaps. \textsuperscript{*}Default ScienceWorld setting.}
469	\label{tab:penalty-correlation}
470	\end{table}
471	
472	This sharpens our central finding: death is not merely the dominant component of routing signal; it is effectively the \emph{only} component that generates differential routing signal in ScienceWorld. At low penalties, the death contribution is small and $\Delta_{\text{full}}$ reduces to $\Delta_{\text{nd}} \approx 2.84$, which is near-uniform across task types ($\text{mean non-death gap} = -1.19$ excluding the \texttt{find-non-living-thing} outlier); consequently, death-rate differential has no predictive power. As $P$ increases, the death term dominates $\Delta_{\text{full}}$, and the correlation sharpens because death rates \emph{are} the performance gap. The DAF values in Table~\ref{tab:penalty-sensitivity} increase monotonically with $P$, but this is a mathematical consequence of the decomposition ($\text{DAF} = \delta P / (\delta P + \Delta_{\text{nd}})$), not evidence of mechanism robustness.
473	
474	\section{Cross-Environment Details}
475	\label{app:cross-env-details}
476	
477	Figure~\ref{fig:signal-reversal} and Table~\ref{tab:cross-env} summarize the label distributions across all three environments.
478	
479	\begin{figure}[h]
480	\centering
481	\includegraphics[width=\columnwidth]{figures/signal_reversal.pdf}
482	\caption{Cross-environment label distributions. ScienceWorld and ALFWorld both show deterministic preference, but through different mechanisms: death avoidance (ScienceWorld) vs.\ information asymmetry from admissible-action access (ALFWorld). MATH shows balanced labels, confirming no routing signal without catastrophic failure.}
483	\label{fig:signal-reversal}
484	\end{figure}
485	
486	\begin{table}[h]
487	\centering
488	\small
489	\resizebox{\columnwidth}{!}{%
490	\begin{tabular}{@{}lccccc@{}}
491	\toprule
492	Environment & $N$ & Det\% & Int\% & NoPref\% & Death? \\
493	\midrule
494	ScienceWorld & 245 & 35.1 & 3.7 & 61.2 & Yes ($-100$) \\
495	MATH & 795 & 12.0 & 13.5 & 74.6 & No \\
496	ALFWorld & 135 & 25.9 & 1.5 & 72.6 & No\textsuperscript{$\dagger$} \\
497	\bottomrule
498	\end{tabular}}
499	\caption{Cross-environment label distribution. ``Deterministic'' denotes qualitatively different computation modes: ScienceWorld = oracle simulator with ground-truth state; MATH = Python code interpreter; ALFWorld = admissible-action enumeration. $\dagger$\,ALFWorld's deterministic advantage stems from information asymmetry, not death avoidance.}
500	\label{tab:cross-env}
501	\end{table}
502	
503	Table~\ref{tab:alfworld-pertask} provides the per-task-type breakdown for ALFWorld. Unlike ScienceWorld, ALFWorld has no death mechanism ($\delta = 0$, DAF $= 0\%$); the entire performance gap $\Delta_{\text{full}}$ reflects information asymmetry from admissible-action access. \texttt{pick\_and\_place} shows the strongest effect ($\Delta = 0.563$, 18 of 32 episodes det-preferred), while \texttt{pick\_two\_obj\_and\_place} shows the weakest ($\Delta = 0.087$), consistent with multi-object tasks requiring more sequential reasoning that admissible actions alone cannot resolve. Only \texttt{pick\_heat\_then\_place} has a 95\% CI crossing zero ($n{=}16$).
504	
505	\begin{table}[h]
506	\centering
507	\scriptsize
508	\setlength{\tabcolsep}{2.5pt}
509	\begin{tabular}{@{}lrcccc@{}}
510	\toprule
511	Task Type & $n$ & Succ\%\textsubscript{int} & Succ\%\textsubscript{det} & D / I / N & $\Delta_{\text{full}}$ \\
512	\midrule
513	pick\_and\_place       & 32 & 0.0  & 56.3 & 18 / 0 / 14 & $+0.563$ \\
514	look\_at\_obj\_in\_light & 13 & 15.4 & 38.5 & 3 / 0 / 10  & $+0.231$ \\
515	pick\_cool\_then\_place & 24 & 0.0  & 16.7 & 4 / 0 / 20  & $+0.167$ \\
516	pick\_clean\_then\_place & 27 & 3.7  & 18.5 & 5 / 1 / 21  & $+0.148$ \\
517	pick\_heat\_then\_place & 16 & 6.3  & 18.8 & 3 / 1 / 12  & $+0.125$ \\
518	pick\_two\_obj\_and\_place & 23 & 0.0 & 8.7  & 2 / 0 / 21  & $+0.087$ \\
519	\midrule
520	\textbf{All (6 types)} & \textbf{135} & \textbf{3.0} & \textbf{27.4} & \textbf{35 / 2 / 98} & $\mathbf{+0.244}$ \\
521	\bottomrule
522	\end{tabular}
523	\caption{Per-task-type decomposition for ALFWorld (135 games, Qwen2.5-7B-Instruct). D/I/N: deterministic-preferred / internal-preferred / no-preference. No death mechanism exists; $\Delta_{\text{full}}$ is driven entirely by information asymmetry from admissible-action access. Sorted by $\Delta_{\text{full}}$ descending.}
524	\label{tab:alfworld-pertask}
525	\end{table}
526	
527	\section{Cross-Model Verification}
528	\label{app:cross-model}
529	
530	We replicate the counterfactual analysis with Llama-3.1-8B-Instruct across all 11 task types ($N{=}220$ episode pairs, 20 per type; Table~\ref{tab:cross-model-detail}).
531	The internal strategy dies in $41.4\%$ of episodes versus $11.4\%$ for deterministic (death-rate differential $+30.0$~pp), with 83 deterministic-preferred, 3 internal-preferred (1.4\%, all death-asymmetry reversals), and 134 no-preference labels.
532	Both models exhibit nearly identical internal vulnerability (${\sim}$42\%: Qwen $42.9\%$, Llama $41.4\%$), confirming that death-prone failure is structurally determined. The differential magnitude varies ($+26.5$~pp Qwen, $+30.0$~pp Llama) because deterministic strategy safety is model-dependent ($16.3\%$ vs.\ $11.4\%$), but directional consistency is 100\% (10/10 death-prone tasks in both models).
533	\texttt{identify-life-stages-1} shows cross-model precision matching ($55\%$/$10\%$/$+45$~pp in both models).
534	\texttt{find-non-living-thing} shows zero deaths in both models, consistent with its majority-class answer distribution.
535	
536	\begin{table}[h]
537	\centering
538	\small
539	\begin{tabular}{@{}lrrrl@{}}
540	\toprule
541	Task & Int\% & Det\% & $\Delta$\,pp & D / I / N \\
542	\midrule
543	identify-life-stages-1 & 55 & 10 & +45 & 9 / 0 / 11 \\
544	freeze & 45 & 0 & +45 & 9 / 0 / 11 \\
545	grow-fruit & 45 & 5 & +40 & 8 / 0 / 12 \\
546	identify-life-stages-2 & 45 & 5 & +40 & 8 / 0 / 12 \\
547	measure-melting-point & 50 & 15 & +35 & 9 / 0 / 11 \\
548	lifespan-longest & 35 & 5 & +30 & 7 / 1 / 12 \\
549	lifespan-l-then-s & 50 & 20 & +30 & 6 / 0 / 14 \\
550	chemistry-mix & 45 & 20 & +25 & 5 / 0 / 15 \\
551	inclined-plane & 45 & 20 & +25 & 6 / 0 / 14 \\
552	find-animal & 40 & 25 & +15 & 6 / 2 / 12 \\
553	find-non-living-thing & 0 & 0 & 0 & 10 / 0 / 10 \\
554	\midrule
555	\textbf{Aggregate} & \textbf{41.4} & \textbf{11.4} & \textbf{+30.0} & \textbf{83 / 3 / 134} \\
556	\bottomrule
557	\end{tabular}
558	\caption{Per-task Llama-3.1-8B cross-model replication ($N{=}20$ per task). D/I/N: deterministic-preferred / internal-preferred / no-preference. Sorted by $\Delta$ DR descending.}
559	\label{tab:cross-model-detail}
560	\end{table}
561	
562	\section{Failure Mode Analysis}
563	\label{app:failure-modes}
564	
565	All 105 internal-strategy deaths (100\%) are triggered by the same action pattern: \texttt{focus on [object]}. In ScienceWorld, \texttt{focus on} is the answer-submission action (equivalent to ``this is my final answer''); the LLM agent systematically misuses it as a general interaction or exploration command, and applies it to irrelevant targets (rooms, doors, inventory items). Each such execution submits an incorrect answer and triggers the $-100$ death penalty. Within death episodes, both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40 for deterministic) reflects how often each strategy enters catastrophic states, not different action selection within those states.
566	
567	Manual inspection identifies four failure categories: (A) no task awareness, where the agent executes \texttt{focus on} without reading the task; (B) task-aware but lacking action grounding, where the agent correctly identifies the objective but cannot map it to valid action primitives; (D) genuine attempts with execution failure; and (E) initial progress wasted by early errors. Category B dominates: agents demonstrate task comprehension but systematically fail to translate it into correct ScienceWorld actions. This taxonomy was produced by a single annotator; no inter-annotator agreement was computed. The categories are intended as qualitative illustrations, not as formal labels with reliability guarantees.
568	\label{tab:death-taxonomy}
569	
570	\paragraph{Representative examples.}
571	\emph{Category A} (no task awareness): In a \texttt{chemistry-mix} episode, the agent immediately executes \texttt{focus on kitchen}, \texttt{focus on door}, \texttt{focus on inventory} without reading the task, dying on the first \texttt{focus on} call. \emph{Category B} (comprehension without grounding): In a \texttt{lifespan-longest-lived} episode, the agent correctly identifies that it must compare animal lifespans and reasons about which animal lives longest, but then executes \texttt{focus on oak tree} (a non-animal object in the room) instead of navigating to find the target animal, triggering death.
572	
573	\paragraph{Action distribution analysis.}
574	Figure~\ref{fig:death-action-dist} shows the action distribution in death versus non-death episodes for the internal strategy; both are dominated by \texttt{connect} actions, with \texttt{focus on} moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$). Crucially, Figure~\ref{fig:death-comparison} reveals that within death episodes, internal and deterministic strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$). The survival gap (105 vs.\ 40 deaths) therefore reflects how often each strategy enters catastrophic states, not how it behaves within those states. Among fatal \texttt{focus on} targets, \texttt{workshop} remains the most frequent (20.0\%), followed by \texttt{inventory} (17.1\%) and \texttt{kitchen} (10.5\%), indicating a systematic object bias rather than random exploration. Figure~\ref{fig:death-timeline} visualizes the temporal pattern: agents execute long sequences of \texttt{connect} actions before a terminal \texttt{focus on} triggers death, typically in the final 1--3 steps.
575	
576	\begin{figure}[h]
577	\centering
578	\includegraphics[width=\columnwidth]{figures/death_action_distribution.pdf}
579	\caption{Action distribution for the internal (LLM) strategy in death ($n{=}105$) vs.\ non-death ($n{=}140$) episodes. Left: full distribution (both dominated by \texttt{connect}). Right: non-\texttt{connect} actions zoomed. \texttt{focus on} is moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$), while non-death episodes show higher rates of observation and object interaction.}
580	\label{fig:death-action-dist}
581	\end{figure}
582	
583	\begin{figure}[h]
584	\centering
585	\includegraphics[width=\columnwidth]{figures/death_action_timeline.pdf}
586	\caption{Step-by-step action sequences for 6 representative death episodes. The fatal \texttt{focus on} action (marked with arrow) consistently appears in the final steps after long \texttt{connect} sequences, and illustrates the ``connect loop $\to$ fatal focus'' pattern. Examples are drawn from the full 30-task dataset for task-type diversity; the pattern is identical in the 11-task analysis subset.}
587	\label{fig:death-timeline}
588	\end{figure}
589	
590	\begin{figure}[h]
591	\centering
592	\includegraphics[width=\columnwidth]{figures/death_action_comparison.pdf}
593	\caption{Non-\texttt{connect} action distribution comparison between internal (left) and deterministic (right) strategies. Within death episodes, both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not different action selection within those states.}
594	\label{fig:death-comparison}
595	\end{figure}
596	
597	\section{Grounding Ablation}
598	\label{app:grounding-ablation}
599	
600	We test whether directly intervening on the dominant death action (\texttt{focus on}) eliminates death vulnerability on the 10 death-prone tasks (baseline 48.0\%, $n{=}200$).
601	
602	\paragraph{Prompt warning.} Adding an explicit system prompt (``use \texttt{focus on} only for final answers'') reduces aggregate death rate to 37.0\% ($\Delta = -11$~pp). Both identification tasks exhibit ironic effects (\texttt{identify-life-stages-1}: 35\%$\to$50\%; \texttt{identify-life-stages-2}: 25\%$\to$70\%), where explicit mention of the dangerous action may have increased its salience.
603	
604	\paragraph{Action-space filtering.} Blocking \texttt{focus on} during the exploration phase yields 379 blocks across 200 episodes with zero leaks and zero passthroughs (the agent never persisted in retrying blocked actions), reducing death rate to 29.0\% ($\Delta = -19$~pp). The zero-passthrough rate suggests \texttt{focus on} use is a shallow behavioral pattern rather than a deliberate strategy.
605	
606	\paragraph{Per-task variation.} Under filtering, \texttt{identify-life-stages} and \texttt{inclined-plane} approach deterministic-level safety (${\sim}$15--20\% DR), while \texttt{chemistry-mix} and \texttt{find-animal} remain at 35--40\%. Residual deaths occur during the answer-submission window, where the filter is inactive and agents submit \texttt{focus on} to incorrect objects.
607	
608	\section{Ablation Studies}
609	\label{app:ablations}
610	
611	\paragraph{Capacity scaling.} We scale the implicit router from Qwen3-0.6B to Qwen3-4B and evaluate at both step and episode level (Table~\ref{tab:capacity}).
612	
613	\begin{table}[h]
614	\centering
615	\small
616	\begin{tabular}{@{}lcc@{}}
617	\toprule
618	Model & Step Bal.\ Acc.\ (\%) & Ep.\ Bal.\ Acc.\ (\%) \\
619	\midrule
620	Qwen3-0.6B & $56.4 \pm 3.5$ & $50.7 \pm 2.6$ \\
621	Qwen3-1.7B & $58.2 \pm 4.0$ & $43.1 \pm 1.0$ \\
622	Qwen3-4B & $59.2 \pm 3.5$ & $\mathbf{59.0 \pm 1.9}$ \\
623	\midrule
624	Always-det & 50.0 & 50.0 \\
625	\bottomrule
626	\end{tabular}
627	\caption{Capacity scaling: step-level and episode-level balanced accuracy (4 seeds, identical configuration across all scales). Step-level accuracy is flat ($56$--$59\%$, within seed variance). At episode level, only 4B breaks the random baseline ($59.0\%$, $p < 0.005$).}
628	\label{tab:capacity}
629	\end{table}
630	
631	Step-level balanced accuracy is flat across scales ($56$--$59\%$, within seed variance); step-level discrimination is not capacity-sensitive. At episode level, only 4B breaks the random baseline ($59.0 \pm 1.9\%$, $p < 0.005$); 0.6B and 1.7B remain at or below chance. The 1.7B model's below-chance episode-level accuracy ($43.1\%$) may reflect overfitting to spurious step-level correlations that anti-correlate with episode outcomes; without per-class confusion matrices at this scale, this remains a hypothesis. The dominant explanation across scales is that death avoidance constitutes a task-type-level binary signal that a step-level router cannot exploit efficiently.
632	
633	\paragraph{Generative router.} A generative routing model trained with explicit routing labels achieves balanced accuracy of 46.7\%, confirming that the routing bottleneck is signal-limited, not architecture-limited.
634	
635	\paragraph{Leave-one-task-type-out routing.} Under leave-one-task-type-out evaluation, blind routing collapses to always-deterministic (balanced accuracy 50.0\%); a keyword-based variant achieves 62.9\% only through task-identity leakage, not genuine routing signal.
636	
637	\paragraph{Reasoning depth.} An ablation comparing chain-of-thought reasoning against direct-answer generation on 6 task types ($n{=}120$ episodes per condition, 6 tasks $\times$ 20 episodes per task) found no significant difference (Mann--Whitney $p > 0.26$, $|d| \leq 0.31$) and near-identical death rates (41.8\% vs.\ 42.5\%); reasoning depth does not meaningfully alter internal-mode outcomes.
638	
639	\section{Threshold Routing Analysis}
640	\label{sec:threshold-routing}
641	
642	Given per-task death risk knowledge, we test whether a simple threshold routing strategy can outperform always-deterministic. For each threshold $t \in [0, 1]$, we route to internal if the per-task internal death rate $\leq t$, otherwise to deterministic, and sweep all thresholds to find the optimal.
643	
644	\begin{table}[h]
645	\centering
646	\small
647	\begin{tabular}{lccc}
648	\toprule
649	Strategy & Mean Score & Death Rate & $\Delta$ vs Det \\
650	\midrule
651	Always-det & $-9.47$ & $0.163$ & $0.00$ \\
652	Optimal threshold ($t{=}0$) & $-11.03$ & $0.155$ & $-1.56$ \\
653	Always-internal & $-39.07$ & $0.429$ & $-29.60$ \\
654	\bottomrule
655	\end{tabular}
656	\caption{Death-risk threshold routing analysis on 245 episodes. The optimal threshold routes only \texttt{find-non-living-thing} (the sole zero-death task) to internal, with all other tasks routed to deterministic. Bootstrap 95\% CI for the difference: $[-8.87, +5.92]$.}
657	\label{tab:threshold-routing}
658	\end{table}
659	
660	Even with perfect per-task death risk knowledge, threshold routing cannot outperform always-deterministic. The sole zero-death task achieves higher scores under deterministic (+28.5) than internal (+18.9), leaving no room for a beneficial mixed strategy.
661	
662	\section{Practitioner Decision Framework}
663	\label{app:decision-framework}
664	
665	Given a new interactive environment, the following three-stage procedure diagnoses whether learned routing adds value over a fixed deterministic strategy.
666	
667	\paragraph{Stage 1: Pilot collection (${\sim}$50 episodes).}
668	Run pure-internal and pure-deterministic strategies on a representative sample (${\sim}$50 episode pairs). Compute the death-rate differential $\Delta\text{DR} = \text{DR}_{\text{int}} - \text{DR}_{\text{det}}$.
669	
670	\paragraph{Stage 2: Death dominance check.}
671	If $\Delta\text{DR} > 15$~pp, death asymmetry is likely the dominant routing signal. Compute the death-label fraction $f_{\text{death}}$: the proportion of non-tie routing labels where exactly one strategy dies.
672	
673	\paragraph{Stage 3: Decision.}
674	If $f_{\text{death}} > 75\%$, the routing signal is death-dominated; a fixed deterministic strategy will match or exceed any learned router. If $f_{\text{death}} < 50\%$, diverse routing signals may justify a learned router. Between 50\%--75\%, collect additional episodes to reduce estimation noise before committing to router development.
675	
676	\paragraph{Retrospective validation.}
677	All four experimental conditions in this paper are correctly classified:
678	
679	\begin{table}[h]
680	\centering
681	\small
682	\begin{tabular}{@{}lrrll@{}}
683	\toprule
684	Condition & $\Delta$DR & $f_{\text{death}}$ & Prediction & Actual \\
685	\midrule
686	Qwen-7B & +26.5 & 78.9\% & det-fixed & det wins \\
687	Llama-8B & +30.0 & $>$75\% & det-fixed & det wins \\
688	Qwen-72B & +27.8 & $>$75\% & det-fixed & det wins \\
689	MATH & +0.5 & 0\% & router viable & no signal \\
690	\bottomrule
691	\end{tabular}
692	\caption{Retrospective validation of the decision framework. All four conditions are correctly classified (4/4).}
693	\label{tab:decision-framework}
694	\end{table}
695	
696	The framework also predicts the inverted-U relationship between capability and death risk: below ${\sim}$0.5B parameters, agents rarely reach dangerous states (13.3\% death rate in a 15-episode pilot), so $\Delta\text{DR}$ is low and the framework would not recommend fixed-deterministic. Above ${\sim}$7B, agents are capable enough to enter catastrophic states but not capable enough to avoid them, producing high $\Delta\text{DR}$.
697	
698	\paragraph{Threshold calibration.} The thresholds above (15~pp, 75\%, 50\%) are illustrative, derived from a single-environment analysis. Practitioners should calibrate these boundaries for their specific environment and reward structure.
699	
700	\section{Extended Validation of Excluded Tasks}
701	\label{app:extended-validation}
702	
703	To verify that task exclusion does not bias toward death-prone tasks, we collect $n{=}20$ episodes for five representative excluded tasks spanning all exclusion categories (Table~\ref{tab:extended-val}).
704	
705	\begin{table}[h]
706	\centering
707	\small
708	\begin{tabular}{lcrrrrc}
709	\toprule
710	Task & Category & $n$ & Int DR & Det DR & $\Delta$DR & D/I/N \\
711	\midrule
712	boil & dev-set & 20 & 55\% & 25\% & +30\,pp & 6/0/14 \\
713	melt & dev-set & 20 & 45\% & 20\% & +25\,pp & 7/2/11 \\
714	find-living-thing & taxonomic & 20 & 55\% & 15\% & +40\,pp & 10/0/10 \\
715	use-thermometer & agent-floor & 20 & 50\% & 20\% & +30\,pp & 7/1/12 \\
716	power-component & agent-floor & 20 & 50\% & 15\% & +35\,pp & 7/0/13 \\
717	\midrule
718	\textit{Mean (5 tasks)} & & 100 & 51.0\% & 19.0\% & +32.0\,pp & 37/3/60 \\
719	\bottomrule
720	\end{tabular}
721	\caption{Extended validation ($n{=}20$) of representative excluded task types. All five tasks confirm death asymmetry; mean $\Delta$DR $= +32.0$\,pp is consistent with the $n{=}5$ prescreening estimate for these same tasks (Table~\ref{tab:excluded-death}).}
722	\label{tab:extended-val}
723	\end{table}
724	
725	Notably, the excluded-task aggregate DAF (0.991) exceeds the included-task DAF (0.904; Table~\ref{tab:per-task}), indicating that excluded tasks are \emph{more} death-dominated than included tasks---the opposite of a cherry-picking bias.
726	
727	\input{responsibleNLPchecklist}
728	
729	\end{document}
730	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "239b6808-8cf1-4bfa-8b28-7cbe92c45842",
  "isSidechain": true,
  "promptId": "87127d5f-9fda-46aa-9632-72943c579a6b",
  "agentId": "a9d6419e05e089045",
  "type": "user",
  "uuid": "60de154b-4d25-461a-b966-d79da46834a2",
  "sourceToolAssistantUUID": "239b6808-8cf1-4bfa-8b28-7cbe92c45842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-20T07:37:52.719Z_

Now I have a thorough understanding of the paper content. Let me check the artifacts directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60de154b-4d25-461a-b966-d79da46834a2",
  "isSidechain": true,
  "agentId": "a9d6419e05e089045",
  "requestId": "req_011CbDSQLsRYcnME9brTScwn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f89e4fb-da07-49d4-9e92-baa0d2cef292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CCYtd9bgy9rJFRM4XjBWj2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26992,
      "cache_read_input_tokens": 30171,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26992,
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

_source line 9 · 2026-05-20T07:37:53.976Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QohvrX6ZmsJtFgNXtUGAhX`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f89e4fb-da07-49d4-9e92-baa0d2cef292",
  "isSidechain": true,
  "agentId": "a9d6419e05e089045",
  "requestId": "req_011CbDSQLsRYcnME9brTScwn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd683968-c547-41a6-a6e1-ed407306c2c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CCYtd9bgy9rJFRM4XjBWj2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26992,
      "cache_read_input_tokens": 30171,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 26992
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 30171,
          "cache_creation_input_tokens": 26992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 26992,
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

_source line 10 · 2026-05-20T07:37:54.158Z_

<details><summary>↩ Tool result · `toolu_01QohvrX6ZmsJtFgNXtUGAhX`</summary>

```text
14838_diagnosis.md
70b_progress_check.md
72b_canonical_death_rate.md
72b_daf_decomposition.md
72b_data_status.md
72b_death_rate_analysis.md
7b_main_per_task_death_rate.md
7b_per_task_death_rate.md
_project
alfworld_cf_diagnosis.md
appendix
appendix_promotion_plan.md
arr_submission_checklist.md
backbone-scaling-70b
backbone-scaling-70b-analysis.md
bootstrap_95ci.json
cross-model-guided-router-eval
cross-split-robustness-8seed
death-proximal-labeling-router
death_aware_labeling.py
death_failure_taxonomy_245eps.md
deep_vs_fast_analysis.md
diagnosis_mvp-p1-gpu1-v2.md
dose_response_figure.pdf
dream_reports
excluded_tasks_analysis.md
experiment_tables.md
extended-task-validation
extended_task_validation_results.md
fig1_daf_scatter_verify.jpg
framework_diagnostic_summary.md
gpu_cleanup_dual_restart_report.md
grounding-prompt-ablation
leave-one-tasktype-out
literature_survey_death_avoidance.md
long_paper_figures_tables.md
long_paper_results_summary.md
loto-guided-router-eval
main_v122_r8fixed.pdf
manifest.yaml
math-counterfactual-dryrun
math-negative-contrast
method_recovery_and_decision_framework.md
minihack-cross-env-pilot
minihack_det_agent.py
minihack_episode_runner.py
minihack_feasibility_report.md
minihack_negative_contrast.md
multi-model-pilot
paper_audit_report.md
paper_completeness_audit.md
paper_data_tables.md
paper_number_audit.md
penalty_sensitivity.json
penalty_sensitivity_table.tex
permadeath_env_feasibility.md
phase1_progress_report.md
plan-002-generative-v1-analysis.md
plan-003-bootstrap-95ci
plan-003-e2e-ablation-b
plan-003-eval-implicit
plan-004-ablation-b
plan-004-v5
plan-005-routing-patterns
plan-006-deep-internal
plan-008-router-size-v3
plan-010-cross-task-v2
plan-012-decomposition
plan-012-full
plan-012-penalty-curve
plan-012-penalty-sensitivity
plan-012-step-tie-rate
plan-013
plan-013-labeling-quality
plan005_routing_analysis.md
plan005_routing_patterns_v2.md
plan_001b_revised_proposal.md
plan_001b_task_selection.md
prescreening_final_summary.json
r18_mislabel_distribution.md
rebuttal_drafts.md
reflexion-dose-response-n345
reflexion_prep_report.md
related_work_draft.md
retry-dose-response
review_issues.yaml
review_reports
router_sft_train.py
running_experiments_check.md
scienceworld-data-consolidation
seed-123-replication
seed-robustness-core
w1_cluster_bootstrap_k11.md
w3_confusion_matrix.md
worker_output_diagnose_llama_full.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd683968-c547-41a6-a6e1-ed407306c2c0",
  "isSidechain": true,
  "promptId": "87127d5f-9fda-46aa-9632-72943c579a6b",
  "agentId": "a9d6419e05e089045",
  "type": "user",
  "uuid": "0cda9b20-4d5f-404f-a081-9c9031b539a0",
  "sourceToolAssistantUUID": "fd683968-c547-41a6-a6e1-ed407306c2c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T07:37:56.364Z_

Good, the directory exists. Now I'll create both files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cda9b20-4d5f-404f-a081-9c9031b539a0",
  "isSidechain": true,
  "agentId": "a9d6419e05e089045",
  "requestId": "req_011CbDSQftvDjVzhVhZmHzog",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f85ab0a-c29e-4887-9bb8-4921c24cbea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xt7XowtZ1Tw5aot6nZW2Md",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 998,
      "cache_read_input_tokens": 57163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 998,
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

_source line 12 · 2026-05-20T07:38:37.450Z_

<details open><summary>🔧 Tool call — Write · `toolu_013aj4BMXoF5GDXtx5TiMaA1`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/paper_patch_draft.md",
  "content": "# Paper Patch Drafts\n\nPre-drafted LaTeX patches for pending experimental results. [TBD] placeholders mark data from Gemma-2-9B ScienceWorld and Llama-3.1-8B ALFWorld experiments.\n\n---\n\n## Section 2a: ALFWorld Subsection Expansion\n\nCurrent ALFWorld coverage is a single paragraph in Section 4.4 (Cross-Environment Boundary Probes). This draft expands it to incorporate cross-model replication and formal DAF=0% explanation.\n\n```latex\n\\paragraph{Cross-environment validation: ALFWorld.}\nALFWorld~\\citep{alfworld-2021} (6 task types, 135 games) provides a complementary test environment where the deterministic strategy receives admissible-action enumeration---an information asymmetry rather than a computation mode switch.\nUnlike ScienceWorld, ALFWorld has no death mechanism: $\\delta = 0$ and DAF $= 0\\%$ by construction.\nThe entire routing signal arises from information asymmetry: the admissible-action oracle eliminates exploration errors that the internal strategy must resolve through trial-and-error interaction.\n\nWith Qwen2.5-7B-Instruct, 35 of 37 non-tie labels (94.6\\%) favor the information-advantaged strategy, with 25.9\\% det-preferred, 1.5\\% int-preferred, and 72.6\\% no-preference across 135 episodes.\nThe per-task-type breakdown (Appendix~\\ref{app:cross-env-details}, Table~\\ref{tab:alfworld-pertask}) reveals that \\texttt{pick\\_and\\_place} shows the strongest effect ($\\Delta = 0.563$), while multi-object tasks requiring sequential reasoning show weaker effects, consistent with admissible actions providing less advantage when planning depth matters.\n\nCross-model replication with Llama-3.1-8B-Instruct ([TBD] games) yields [TBD]\\% det-preferred, [TBD]\\% int-preferred, and [TBD]\\% no-preference, with [TBD] of [TBD] non-tie labels favoring the information-advantaged strategy ([TBD]\\%).\nThe information-asymmetry mechanism replicates across model families: both models show zero death labels and one-directional dominance driven by admissible-action access rather than catastrophic failure.\n\nThis cross-environment contrast is diagnostic: the framework correctly identifies qualitatively different mechanisms---death avoidance in ScienceWorld (DAF $= 90.4\\%$) versus information asymmetry in ALFWorld (DAF $= 0\\%$)---without modification.\nThe DAF $= 0\\%$ result is not a failure of the framework but a correct diagnosis: when no death mechanism exists, all routing signal must originate from non-death performance differences, and the framework quantifies this distinction.\n```\n\n---\n\n## Section 2b: Cross-Model and Cross-Environment Table Expansion\n\nCurrent cross-model data is spread across Section 4.2 (Llama ScienceWorld) and Section 4.3 (72B scaling). This draft consolidates into a unified table spanning models and environments.\n\n```latex\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Environment & $n$ & Int DR & Det DR & $\\Delta$DR & DAF \\\\\n\\midrule\nQwen2.5-7B & ScienceWorld & 245 & 42.9\\% & 16.3\\% & +26.5 & 90.4\\% \\\\\nLlama-3.1-8B & ScienceWorld & 220 & 41.4\\% & 11.4\\% & +30.0 & 88.2\\% \\\\\nGemma-2-9B & ScienceWorld & [TBD] & [TBD] & [TBD] & [TBD] & [TBD] \\\\\nQwen2.5-72B & ScienceWorld & 255 & 30.6\\% & 2.75\\% & +27.8 & 92.4\\% \\\\\n\\midrule\nQwen2.5-7B & ALFWorld & 135 & 0\\% & 0\\% & 0 & 0\\% \\\\\nLlama-3.1-8B & ALFWorld & [TBD] & [TBD] & [TBD] & [TBD] & [TBD] \\\\\n\\midrule\nQwen2.5-7B & MATH & 300 & N/A & N/A & N/A & N/A \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model and cross-environment replication of the counterfactual routing analysis. \\textbf{ScienceWorld}: death dominance replicates across three model families (7--9B range) and persists under $10{\\times}$ scaling (72B); internal vulnerability is structurally similar (${\\sim}$41--43\\% at 7--9B), while the differential magnitude varies with deterministic strategy safety. \\textbf{ALFWorld}: DAF $= 0\\%$ by construction (no death mechanism); routing signal arises from information asymmetry via admissible-action access. \\textbf{MATH}: near-identical accuracy between strategies; no routing signal emerges without catastrophic failure. DR = death rate; $\\Delta$DR = internal DR $-$ deterministic DR; DAF = Death Avoidance Factor at $P{=}100$.}\n\\label{tab:cross-model-env}\n\\end{table}\n```\n\n### Notes on table placement\n\n- **If Gemma confirms death dominance (DAF > 80%)**: promote this table to main text (replace or supplement current Table 3 in Section 4.3), adding a row count of \"3 model families\" in the caption.\n- **If Gemma is weaker (DAF 50-80%)**: keep the table in the appendix (Appendix M), reference from main text with a sentence like \"A third model family (Gemma-2-9B) shows directionally consistent but attenuated death dominance (Appendix~\\ref{app:cross-model}).\"\n- **If Gemma reverses**: table still goes in appendix, but caption and surrounding text must discuss the model-dependency finding honestly.\n\n### Integration with existing text\n\nThe current Section 4.2 (Multi-Model Validation) text about Llama remains valid. The expanded table consolidates data that is currently scattered across:\n- Section 4.2: Llama-3.1-8B ScienceWorld data\n- Section 4.3: Qwen2.5-72B data (currently in Table 2, agent improvement context)\n- Section 4.4: ALFWorld Qwen data\n- Appendix L: ALFWorld per-task breakdown\n- Appendix M: Llama per-task breakdown\n\nThe MATH row uses N/A for death-related metrics because MATH episodes use a code interpreter with no death mechanism; the 795-episode dataset is referenced in Section 4.4 but death rates are not applicable.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f85ab0a-c29e-4887-9bb8-4921c24cbea3",
  "isSidechain": true,
  "agentId": "a9d6419e05e089045",
  "requestId": "req_011CbDSQftvDjVzhVhZmHzog",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f726ed1d-ed5d-423d-9ccb-95a67b433fff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xt7XowtZ1Tw5aot6nZW2Md",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 998,
      "cache_read_input_tokens": 57163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 998,
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

_source line 13 · 2026-05-20T07:38:37.474Z_

<details><summary>↩ Tool result · `toolu_013aj4BMXoF5GDXtx5TiMaA1`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/paper_patch_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f726ed1d-ed5d-423d-9ccb-95a67b433fff",
  "isSidechain": true,
  "promptId": "87127d5f-9fda-46aa-9632-72943c579a6b",
  "agentId": "a9d6419e05e089045",
  "type": "user",
  "uuid": "bec145b3-d6a7-46df-a371-905941c38169",
  "sourceToolAssistantUUID": "f726ed1d-ed5d-423d-9ccb-95a67b433fff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T07:38:50.935Z_

<details open><summary>🔧 Tool call — Write · `toolu_01FFMNbtMdSizNVHKXkgBkji`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/result_scenarios.md",
  "content": "# Result Scenario Analysis\n\nPre-analysis of how pending experimental results affect paper claims.\n\n## Scenarios\n\n| Scenario | Gemma ScienceWorld | Llama ALFWorld | Paper Impact |\n|----------|-------------------|----------------|-------------|\n| **Best** | Death dominance confirmed (DAF > 80%, ΔDR > 20pp) | Information asymmetry confirmed (~25% det-pref, 0% death labels) | Upgrade C1 to \"3 model families\"; upgrade C3 to \"cross-model × cross-environment\"; Discussion adds \"framework generalizes across both axes\" |\n| **Median** | Death dominance directionally consistent but weaker (DAF 50-80%, ΔDR 10-20pp) | Information asymmetry confirmed | C1 unchanged (\"2+ families\"), Gemma as \"supporting evidence with reduced effect size\" in Appendix; C3 upgrade for ALFWorld cross-model |\n| **Worst** | No death dominance or reversed direction | Results inconsistent with Qwen | Discuss model-dependency as limitation; reduce C1 claim strength but add depth analyzing why Gemma differs; if ALFWorld also inconsistent, add \"model-specific\" caveat to C3 |\n\n## Response Plans\n\n### Best case actions\n- Expand cross-model table to 3x2 matrix (3 models x 2 environments)\n- Strengthen Abstract/Intro language: \"across three independent model families\"\n- Add Gemma row to Table 3 in main text (not just appendix)\n\n### Median case actions\n- Add Gemma to Appendix cross-model table with effect size discussion\n- Main text mentions \"two primary + one supporting model family\"\n- ALFWorld subsection gets Llama cross-model data\n\n### Worst case actions\n- Reframe as \"model-dependent phenomenon\" -- still a valid diagnostic finding\n- Add analysis: what about Gemma's architecture/training makes it different?\n- Consider whether Gemma's behavior reveals a limitation of the framework or of the model\n- Do NOT suppress negative results -- present them honestly with analysis\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bec145b3-d6a7-46df-a371-905941c38169",
  "isSidechain": true,
  "agentId": "a9d6419e05e089045",
  "requestId": "req_011CbDSQftvDjVzhVhZmHzog",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2800e0f-53b9-4efc-bcc2-5633987850ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xt7XowtZ1Tw5aot6nZW2Md",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 998,
      "cache_read_input_tokens": 57163,
      "output_tokens": 2438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 998
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2438,
          "cache_read_input_tokens": 57163,
          "cache_creation_input_tokens": 998,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 998,
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

_source line 15 · 2026-05-20T07:38:50.958Z_

<details><summary>↩ Tool result · `toolu_01FFMNbtMdSizNVHKXkgBkji`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/result_scenarios.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2800e0f-53b9-4efc-bcc2-5633987850ab",
  "isSidechain": true,
  "promptId": "87127d5f-9fda-46aa-9632-72943c579a6b",
  "agentId": "a9d6419e05e089045",
  "type": "user",
  "uuid": "227abef7-93c0-4317-8590-4fede564cbfb",
  "sourceToolAssistantUUID": "c2800e0f-53b9-4efc-bcc2-5633987850ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-20T07:38:56.210Z_

Two files created:

- `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/paper_patch_draft.md` -- contains Section 2a (ALFWorld subsection expansion with Qwen data preserved + Llama [TBD] placeholders + formal DAF=0% explanation + cross-environment diagnostic framing) and Section 2b (unified cross-model x cross-environment table with Gemma [TBD] row, Llama ALFWorld [TBD] row, plus placement guidance for best/median/worst outcomes).

- `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/result_scenarios.md` -- contains the three-scenario analysis table (best/median/worst) and concrete response plans for each case.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "227abef7-93c0-4317-8590-4fede564cbfb",
  "isSidechain": true,
  "agentId": "a9d6419e05e089045",
  "requestId": "req_011CbDSUrrLewnrUjaD8oYkn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c1ea22d-2268-458a-a3a6-7e2e240d5eeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SK72XfMAxE6P5fUb4jVnys",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2583,
      "cache_read_input_tokens": 58161,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2583
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 58161,
          "cache_creation_input_tokens": 2583,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2583,
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
