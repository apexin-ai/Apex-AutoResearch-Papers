# Research conversation: Check ALL figures and tables in the paper for number consistency. The paper files are at `/home/ubuntu/.agent-ml-researc

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a13f9f1b8ad8fec76.jsonl`
- **Structured JSON:** [`e8a9ec91cea02a18ba30.json`](../../sessions/e8/e8a9ec91cea02a18ba30.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-19T18:15:22.983Z_

Check ALL figures and tables in the paper for number consistency. The paper files are at `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/`.

Main files: `main.tex`, `experiments.tex`, `method.tex`, `discussion.tex`, `introduction.tex`, `abstract.tex`, `conclusion.tex`, `related.tex`

Check each item thoroughly:

1. **Table 1 (baselines, in experiments.tex)**: Find the table with Always-Internal, Always-Deterministic, Random, Oracle, Trained Router scores. Verify every number matches what §3.5 (baselines section) text says. Key numbers: Always-det = -9.47, Always-int = -39.07, Oracle = -6.58, oracle improvement = 2.89 points, 96.3% oracle matches always-det.

2. **Table 2 (agent improvement, in experiments.tex)**: Death rates for Single-trial (42.9%), Reflexion 3x (31.4%), 72B (30.6%), Deterministic (16.3%). Cross-check with §3.3 text. Verify 72B specifics: det DR=2.75%, ΔDR=+27.8pp, Δ_nd=+2.28, DAF=92.4%. Check if the text says 30.6% everywhere for 72B (not 31.4%).

3. **Figure 1 (scatter plot)**: Read the caption in experiments.tex. Check if it includes a "structural consequence" caveat about the near-perfect correlation being mathematically implied by the decomposition (not an independent empirical finding). This was required by R18 reviewer feedback (m1).

4. **Figure 2 (dose-response)**: Check caption and surrounding text. Verify MDE value mentioned, N=200 per group. Check if text says "p < 0.005" for Reflexion N=3.

5. **Appendix cross-references**: Check penalty sensitivity table (Appendix K) numbers match §3.1. Check per-task table numbers match §3.1. Check cross-model (Appendix M) Llama numbers match §3.2. Check 72B appendix numbers match §3.3.

6. **Abstract and Introduction**: Check any specific numbers cited (DAF=90.4%, death rates, correlation r=0.97) match the experiments section.

For each item, report:
- File, line number
- What the number is
- Whether it matches or conflicts
- If conflict: what the correct value should be

Be exhaustive - read every table and every text reference to that table's data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "44bc2991-8df5-496d-9b2e-d19feb4a03d2",
  "agentId": "a13f9f1b8ad8fec76",
  "type": "user",
  "uuid": "91b03338-d9fe-44c1-851d-6c4fe021c394",
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

_source line 2 · 2026-05-19T18:15:22.988Z_

```json
{
  "parentUuid": "91b03338-d9fe-44c1-851d-6c4fe021c394",
  "isSidechain": true,
  "agentId": "a13f9f1b8ad8fec76",
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
  "uuid": "24540c4e-0a23-43cc-92a2-31c7d048c456",
  "timestamp": "2026-05-19T18:15:22.988Z",
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

### Tool call

_source line 3 · 2026-05-19T18:15:27.803Z_

<details open><summary>🔧 Tool call — Read · `toolu_012MRHSGiYVuqNtGijrZiNq8`</summary>

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
  "parentUuid": "24540c4e-0a23-43cc-92a2-31c7d048c456",
  "isSidechain": true,
  "agentId": "a13f9f1b8ad8fec76",
  "requestId": "req_011CbCPDEyohhnb2tEPQprvg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88590018-e57f-444e-ba8b-cf16a7cdae82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dz8SPafdD69GBBwBpp1EVD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29190,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29190,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 55,
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

_source line 4 · 2026-05-19T18:15:27.812Z_

<details><summary>↩ Tool result · `toolu_012MRHSGiYVuqNtGijrZiNq8`</summary>

```text
1	\section{Experiments}
2	
3	We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types (63\%) lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). This scope limits generalizability: conclusions apply to the included subset, not to all ScienceWorld tasks. An anti-cherry-picking analysis confirms that death dominance holds in 18 of these 19 types, with a mean $\Delta\text{DR} = +38.2$\,pp exceeding the included tasks' $+28.7$\,pp (Appendix~\ref{app:per-task}).
4	
5	\subsection{Death Avoidance Decomposition}
6	\label{sec:death-decomp}
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=0.85\columnwidth]{figures/fig1_daf_scatter.pdf}
11	\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$ (Spearman's $\rho = 0.975$; Appendix~\ref{app:per-task}), $p < 10^{-6}$, $n = 11$ task types. Since $\Delta_{\text{full}} \approx \delta P + \Delta_{\text{nd}}$ with $P$ constant, $r \to 1$ as DAF $\to 1$; the near-perfect correlation is a structural consequence of death dominance, not an independent finding (\S\ref{sec:death-decomp}).}
12	\label{fig:decomposition}
13	\end{figure}
14	
15	Of the 95 non-tie routing labels, 75 (78.9\%) arise from death asymmetry: the internal strategy triggers a catastrophic $-100$ penalty while the deterministic strategy survives. This penalty-independent label fraction is the primary diagnostic metric. Of these 75, 54 are sole-signal labels (both strategies score zero without death, so death avoidance was the \emph{sole} discriminating signal). At $P{=}0$, the 54 sole-signal labels reduce to ties, leaving 41 non-tie labels of which 21 (51.2\%) still involve death asymmetry; the labeling function itself is penalty-independent (Algorithm~\ref{alg:labeling}), but the practical routing value of death avoidance requires $P > 0$.
16	
17	Of 245 episodes, 150 (61.2\%) are ties---neither strategy outperforms the other---indicating that routing is relevant in only 38.8\% of episodes. Among these, death avoidance dominates. The Death Avoidance Factor, a derived penalty-dependent measure, quantifies death's contribution to the total performance gap: DAF $= 90.4\%$ at $P{=}100$ ($\Delta_{\text{full}} = +29.60$, $\Delta_{\text{nd}} = +2.84$; 95\% CI: $[81.6\%, 98.8\%]$, episode-level bootstrap, $B{=}10{,}000$). DAF varies with penalty magnitude ($50.4\%$ at $P{=}10$; $82.6\%$ at $P{=}50$; Appendix~\ref{app:penalty}), confirming that the 78.9\% label fraction provides the more robust characterization. When $\Delta_{\text{nd}} \to 0$, DAF $\to 1$ is algebraic necessity regardless of actual death dominance; conversely, when $\Delta_{\text{nd}} < 0$ (as in Reflexion $N{\geq}3$; \S\ref{sec:agent-improvement}), DAF exceeds 100\%, reflecting that death asymmetry more than accounts for the full gap.
18	
19	\paragraph{Per-task correlation structure.}
20	The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic (2.6$\times$), consistent with the internal strategy's reliance on self-generated observations that compound prediction errors across steps. Per-task, death rate differential correlates with $\Delta_{\text{full}}$ ($r = 0.97$, $p < 10^{-6}$; Figure~\ref{fig:decomposition}). Since $P$ is constant across all task types, $\Delta_{\text{full}} = P \cdot \delta + \Delta_{\text{nd}}$ makes $\Delta_{\text{full}}$ a linear function of $\delta$ with residual $\Delta_{\text{nd}}$; when DAF $\rightarrow 1$, this residual vanishes and $r \rightarrow 1$ by construction. The near-perfect correlation is therefore a mathematical consequence of death dominance, not an independent empirical finding. We retain it as an internal consistency check. The correlation drops below significance at $P \leq 25$ (Appendix~\ref{app:penalty}). Of 245 episodes, 86 are \texttt{det\_preferred}, 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preference}.
21	
22	\paragraph{Signal concentration and binary structure.}
23	The Signal Concentration Index (SCI $= 0.2147$; Appendix~\ref{app:sci}) confirms low concentration: the top-3 task types account for only $39.8\%$ of total death-rate differential. The aggregate 78.9\% reflects a per-task binary structure: all 10 death-prone task types produce 100\% death-asymmetry labels, while \texttt{find-non-living-thing} (zero deaths, $\Delta = +9.58$ from non-death scores) produces 0\%. The framework thus diagnoses a binary property (``is this environment death-dominated?'') rather than a continuous routing signal. Removing \texttt{find-non-living-thing} raises the label fraction to 100\% and DAF to 96.8\% (Appendix~\ref{app:loto-daf}).
24	
25	\paragraph{Sensitivity and seed robustness.}
26	Non-clustered episode-level bootstrap ($B = 10{,}000$) yields 95\% CI $[81.6\%, 98.8\%]$ for the death-avoidance label fraction, independent of cluster assumptions, with Cohen's $d = 3.02$ (interpret cautiously given $K{=}11$ task types). Leave-one-task-out analysis confirms stability (label fraction range: 75.9\%--78.9\%; Appendix~\ref{app:loto-daf}); an independent seed replication ($N{=}220$) yields DAF $= 89.7\%$, within 0.7~pp (Appendix~\ref{app:seed-robustness}). As a conservative check, wild cluster bootstrap treating each task type as a cluster yields $p = 0.002$; however, with $K{=}11$ clusters this test falls below the $K{\geq}20$--$40$ threshold recommended for reliable inference~\citep{cameron-2008,webb-2023}, so we rely on the non-clustered bootstrap as primary. All 28 death-prone tasks share the same direction (Appendices~\ref{app:wild-cluster}--\ref{app:per-task-ci}).
27	
28	\subsection{Multi-Model Validation}
29	\label{sec:cross-model}
30	
31	A Llama-3.1-8B-Instruct~\citep{llama3-2024} cross-model replication across all 11 task types ($N{=}220$) confirms that death dominance replicates across model families: internal death rate $41.4\%$ vs.\ deterministic $11.4\%$ (death-rate differential $+30.0$~pp), DAF $= 88.2\%$ ($\Delta_{\text{full}} = +33.17$, $\Delta_{\text{nd}} = +3.9$), with direction consistency 10/10 on death-prone tasks, 83 deterministic-preferred, 3 internal-preferred (1.4\%, all death-asymmetry reversals), and 134 no-preference labels.
32	Both models exhibit nearly identical internal vulnerability (${\sim}$42\%: Qwen $42.9\%$, Llama $41.4\%$), confirming that death-prone failure is structurally determined; the differential magnitude varies ($+26.5$~pp Qwen, $+30.0$~pp Llama) because deterministic strategy safety is model-dependent ($16.3\%$ vs.\ $11.4\%$).
33	\texttt{identify-life-stages-1} shows cross-model precision matching ($55\%$/$10\%$/$+45$~pp in both models).
34	\texttt{find-non-living-thing} shows zero deaths in both models, consistent with its majority-class answer distribution (\S\ref{sec:discussion}). Both models are in the 7--8B range; $10{\times}$ scaling (\S\ref{sec:agent-improvement}) confirms that death dominance persists across capability levels (Appendix~\ref{app:cross-model}).
35	
36	\subsection{Agent Improvement Baselines}
37	\label{sec:agent-improvement}
38	
39	\begin{table}[t]
40	\centering
41	\small
42	\begin{tabular}{@{}lrr@{}}
43	\toprule
44	Condition & Death\% & $N$ \\
45	\midrule
46	Single-trial baseline & 42.9 & 245 \\
47	Reflexion ($3{\times}$) & 31.4 & 220 \\
48	Qwen2.5-72B ($10{\times}$) & 30.6 & 255 \\
49	Deterministic baseline & 16.3 & 245 \\
50	\midrule
51	\multicolumn{3}{@{}l}{\textit{10 death-prone tasks only:}} \\
52	Death-prone baseline & 48.0 & 200 \\
53	Retry ($5{\times}$) & 43.5 & 200 \\
54	\bottomrule
55	\end{tabular}
56	\caption{Internal-strategy death rates under agent improvement methods. Top: all 11 tasks (72B: independently collected at both internal and deterministic). Bottom: 10 death-prone tasks (\texttt{find-non-living-thing} excluded, 0\% death at all scales). All interventions reduce death rate but none approaches deterministic-level safety.}
57	\label{tab:agent-improvement}
58	\end{table}
59	
60	We test whether agent-level improvement reduces death dominance (Table~\ref{tab:agent-improvement}). Retry ($N{=}5$ attempts without self-correction) yields marginal reduction on death-prone tasks ($43.5\%$ vs.\ $48.0\%$ baseline, $\Delta = -4.5$~pp). Reflexion~\citep{reflexion-2023} (verbal self-reflection between trials) reduces death to 31.4\% across all 11 tasks by rescuing 29.3\% of first-trial deaths, but the gap to deterministic remains 15.1~pp; on the 10 death-prone tasks, Reflexion achieves ${\sim}$35\%. Under Reflexion ($N{=}3$, matched-episode analysis), $\Delta_{\text{nd}} = -0.47$, yielding DAF $> 100\%$: the deterministic advantage is entirely attributable to death avoidance, and in non-death episodes the self-correcting agent slightly outperforms the deterministic baseline. Scaling to Qwen2.5-72B ($10{\times}$ parameters; both internal and deterministic strategies independently collected at 72B, 255 episodes across all 11 task types) reduces death rate to $30.6\%$. The 72B deterministic strategy achieves $2.75\%$ death rate ($\Delta\text{DR} = +27.8$~pp), and $\Delta_{\text{nd}} = +2.28$, yielding DAF $= 92.4\%$ (7B: $90.4\%$); scaling lowers death rate but leaves death dominance intact.
61	
62	\paragraph{Dose-response analysis.}
63	We extend both interventions to $N{=}5$ trials on death-prone tasks ($n{=}200$; Figure~\ref{fig:dose-response}). Retry is nearly flat ($48.0\% \to 43.5\%$, $\Delta = -4.5$~pp over five trials). Reflexion drops steeply to $34.0\%$ at $N{=}3$ ($\Delta = -13.5$~pp, $z = 2.75$, $p = 0.003$) then plateaus ($34$--$36.5\%$ for $N \geq 3$, pairwise $p > 0.5$). With $n{=}200$ paired episodes, the minimum detectable effect is ${\sim}8$~pp ($\alpha = 0.05$, 80\% power): the key $N{=}1{\to}3$ decline is well-powered; the plateau claim ($N{=}3{\to}5$, $+1.0$~pp) is also supported, since a ${\geq}8$~pp improvement would be detected. We characterize this as suggestive evidence of a Reflexion ceiling rather than a conclusive demonstration. Retry's per-trial conditional death rate stays constant at ${\sim}48\%$; Reflexion's declines to ${\sim}31\%$ by Trial~3 (per-task breakdown in Appendix~\ref{app:dose-response}).
64	
65	\begin{figure}[t]
66	\centering
67	\includegraphics[width=\columnwidth]{figures/dose_response.pdf}
68	\caption{Death rate as a function of trial count ($N$) for Retry and Reflexion on 10 death-prone tasks ($n{=}200$). Retry (blue) is nearly flat; Reflexion (red) drops steeply through $N{=}3$ then plateaus. Horizontal lines: 72B scaling baseline ($30.6\%$, all 11 tasks) and deterministic baseline ($16.3\%$). Error bands: Wilson 95\% CIs.}
69	\label{fig:dose-response}
70	\end{figure}
71	
72	\subsection{Cross-Environment Boundary Probes}
73	\label{sec:math-contrast}
74	\label{sec:cross-env}
75	
76	We examine MATH and ALFWorld as boundary probes---not cross-domain validation---testing framework applicability across environments that instantiate ``deterministic computation'' differently (oracle simulator, code interpreter, admissible-action enumeration).
77	
78	\paragraph{MATH.} On MATH Level~4--5~\citep{math-2021} ($N{=}795$, code interpreter), internal reasoning and code interpretation achieve near-identical accuracy ($73.5\%$ vs.\ $73.0\%$, McNemar $p = 0.81$), with 74.6\% no-preference. Without catastrophic failure, no routing signal emerges.
79	
80	\paragraph{ALFWorld.} ALFWorld~\citep{alfworld-2021} (6 task types, 135 games) provides the deterministic strategy with admissible actions---an information asymmetry rather than a computation mode switch. Of 37 non-tie labels, 35 (94.6\%) favor the information-advantaged strategy, a one-directional dominance driven by information asymmetry rather than catastrophic failure. The framework diagnoses this qualitatively different mechanism without modification.
81	
82	\subsection{Baselines}
83	\label{sec:baselines}
84	
85	\begin{table}[t]
86	\centering
87	\small
88	\resizebox{\columnwidth}{!}{%
89	\begin{tabular}{@{}lccc@{}}
90	\toprule
91	Strategy & Score & 95\% CI & Death \% \\
92	\midrule
93	Always-Internal & $-39.07$ & [$-46.40$, $-32.27$] & 42.9 \\
94	Always-Deterministic & $-9.47$ & [$-14.71$, $-4.29$] & 16.3 \\
95	Random & $-22.38$ & [$-28.67$, $-15.75$] & 27.8 \\
96	Oracle & $-6.58$ & [$-11.54$, $-1.70$] & 14.3 \\
97	\midrule
98	Trained Router$^\dagger$ & $-10.70$ & [$-16.33$, $-5.27$] & 17.6 \\
99	\bottomrule
100	\end{tabular}}
101	\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 20--40 episodes per type, 245 total). $\dagger$\,Single random seed (42) per episode pair; see Appendix~\ref{app:seed-robustness} for 8-seed robustness analysis.}
102	\label{tab:baselines}
103	\end{table}
104	
105	Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points. The oracle improves only to $-6.58$, with 96.3\% of decisions matching always-deterministic---an \emph{oracle degeneracy} where an always-deterministic lookup achieves 90.5\% of non-tie oracle decisions (balanced accuracy 50.0\%: perfect deterministic recall, zero internal recall).
106	
107	\subsection{Router Training: A Negative Result}
108	\label{sec:router-diagnostic}
109	
110	We probe whether counterfactual labels can train a step-level router, as a diagnostic of label informativeness. The oracle margin (2.89 points) caps routing upside. The near-chance step-level accuracy admits two interpretations: (A)~episode-level labels projected onto steps create ${\sim}$88\% uninformative signal (60.3\% pre-event neutral, 27.4\% post-event), drowning learnable patterns in noise; (B)~routing signal is genuinely task-type-level---there is no step-level pattern to learn. Directional conflict is only 0.3\% of 2{,}040 training steps (labels are directionally correct in 99.7\% of informative steps), but the granularity mismatch leaves minimal signal for the router. The data scaling ablation (25\%--800\%, no improvement) and the extreme class imbalance of death-asymmetry episodes (86/95 $= 90.5\%$ deterministic-preferred) together favor Interpretation~B: routing signal is genuinely task-type-level, not step-level learnable. Definitive attribution between label noise and fundamental non-learnability remains an open question.
111	
112	An implicit router (Qwen3, LoRA; Appendix~\ref{app:router-details}) trained at three scales (0.6B, 1.7B, 4B) shows flat step-level balanced accuracy ($56$--$59\%$). At episode level, only 4B exceeds always-deterministic ($59.0 \pm 1.9\%$, $p < 0.005$); 0.6B and 1.7B remain at chance. Episode-level independent evaluation yields $47.1 \pm 2.2\%$, below the majority-vote baseline of 50.0\%. Training uses episode-level splits (Appendix~\ref{app:router-details}), ensuring no within-episode leakage. The high uninformative rate connects to noisy-label learning~\citep{natarajan2013learning}: standard ERM on labels with ${\sim}$88\% noise yields near-chance classifiers, consistent with our results.
113	
114	\paragraph{End-to-end deployment.} The 4B router deployed end-to-end ($N{=}245$) scores $-12.03$ (95\% CI: $[-17.82, -6.45]$), not exceeding always-deterministic ($-9.47$). Paraphrase-based augmentation ($25\%$--$800\%$) provides no improvement; the $3.7\%$ internal-preferred base rate makes real-data collection expensive (Appendices~\ref{app:seed-robustness}--\ref{app:ablations}).
115	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88590018-e57f-444e-ba8b-cf16a7cdae82",
  "isSidechain": true,
  "promptId": "44bc2991-8df5-496d-9b2e-d19feb4a03d2",
  "agentId": "a13f9f1b8ad8fec76",
  "type": "user",
  "uuid": "ec81ed62-dcc5-471f-a84e-ca65683f4d85",
  "sourceToolAssistantUUID": "88590018-e57f-444e-ba8b-cf16a7cdae82",
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

_source line 5 · 2026-05-19T18:15:28.280Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LDqSdoYfYUa9597cjgD3zJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec81ed62-dcc5-471f-a84e-ca65683f4d85",
  "isSidechain": true,
  "agentId": "a13f9f1b8ad8fec76",
  "requestId": "req_011CbCPDEyohhnb2tEPQprvg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25ef0746-eb8c-4437-9289-95bd39e9577f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dz8SPafdD69GBBwBpp1EVD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29190,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29190,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 55,
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

_source line 6 · 2026-05-19T18:15:28.285Z_

<details><summary>↩ Tool result · `toolu_01LDqSdoYfYUa9597cjgD3zJ`</summary>

```text
1	\begin{abstract}
2	Per-step oracle comparison degenerates under sparse rewards---in ScienceWorld, 97.4\% of steps yield identical scores regardless of computation mode. We introduce an episode-level counterfactual diagnostic framework that overcomes this degeneracy by decomposing routing signal into death-avoidance and non-death components via paired pure-strategy episodes. Applying this framework to ScienceWorld (11 task types, 245 episodes, Qwen2.5-7B-Instruct), we find that \textbf{78.9\% of non-tie routing labels} stem from death asymmetry---a penalty-independent result; a derived measure (DAF) reaches 90.4\% at $P{=}100$. Cross-model replication (Llama-3.1-8B, DAF${=}88.2\%$), four intervention axes (retry, self-correction, $10{\times}$ scaling, action-space restriction), and boundary probes against contrasting environments (MATH, ALFWorld) confirm the framework's diagnostic utility and the robustness of this finding. The framework diagnoses when catastrophic failure makes routing signal degenerate, enabling practitioners to assess routing value before investing in router training.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25ef0746-eb8c-4437-9289-95bd39e9577f",
  "isSidechain": true,
  "promptId": "44bc2991-8df5-496d-9b2e-d19feb4a03d2",
  "agentId": "a13f9f1b8ad8fec76",
  "type": "user",
  "uuid": "8819d772-bf61-40eb-a3a0-492c9781fa3f",
  "sourceToolAssistantUUID": "25ef0746-eb8c-4437-9289-95bd39e9577f",
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

_source line 7 · 2026-05-19T18:15:28.745Z_

<details open><summary>🔧 Tool call — Read · `toolu_016nKBAm3Snag2gcQZKVHXuM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8819d772-bf61-40eb-a3a0-492c9781fa3f",
  "isSidechain": true,
  "agentId": "a13f9f1b8ad8fec76",
  "requestId": "req_011CbCPDEyohhnb2tEPQprvg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a85c2cf3-a3ab-4bbf-bcc6-d3346a848983",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dz8SPafdD69GBBwBpp1EVD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29190,
      "cache_read_input_tokens": 0,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 29190
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 234,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 29190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 29190,
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

_source line 8 · 2026-05-19T18:15:28.750Z_

<details><summary>↩ Tool result · `toolu_016nKBAm3Snag2gcQZKVHXuM`</summary>

```text
1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	In ScienceWorld \cite{scienceworld-2022}, a text-based science simulation, internal reasoning is error-prone---the model may hallucinate state changes (e.g., that water has boiled when the stove was never activated)---while deterministic external computation eliminates such errors via exact state transitions. The practical question: \emph{when should an agent route computation externally versus internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision: Toolformer \cite{toolformer-2023} inserts API calls by perplexity reduction; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects heterogeneous modules per subtask; adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026} or model tiers \cite{mtrouter-2026}; concurrent analyses further presuppose diverse routing signals~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026}. The shared assumption---that routing signal stems from diverse sources and a learned router can exploit it---has not been tested: no prior work has decomposed what drives routing decisions in interactive environments.
7	
8	We propose a \emph{diagnostic framework} comprising (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95), a penalty-independent finding. Under ScienceWorld's penalty ($P{=}100$), DAF reaches $90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$). The internal strategy's hallucination-induced failures trigger catastrophic death ($-100$ penalty); once death episodes are removed, the gap collapses to $\Delta_{\text{nd}} = +2.84$ (\S\ref{sec:death-decomp}).
9	
10	This addresses a methodological gap: per-step oracle comparison degenerates under sparse rewards (97.4\% tie rate; \S\ref{sec:collection}), and keyword-based heuristics fail structurally (\S\ref{sec:baselines}). Our approach runs complete episodes under pure-internal (ReAct \cite{react-2023}) and pure-deterministic strategies, comparing episode outcomes.
11	
12	Cross-context checks probe specificity: MATH Level~4--5 ($N{=}795$, code interpreter) shows no routing signal without catastrophic failure ($73.5\%$ vs.\ $73.0\%$, $p = 0.81$); Llama-3.1-8B replication ($N{=}220$) confirms death dominance across model families (direction consistency 10/10; \S\ref{sec:cross-model}). Four intervention axes (retry, Reflexion~\citep{reflexion-2023}, $10{\times}$ scaling, action-space restriction) reduce death rates but none closes the gap to deterministic safety, with ${\geq}$12~pp residual gaps (\S\ref{sec:agent-improvement}).
13	An exploratory router (Qwen3 LoRA, 0.6B--4B) yields flat step-level balanced accuracy ($56$--$59\%$); at episode level, only 4B exceeds the always-deterministic baseline (\S\ref{sec:router-diagnostic}).
14	
15	Our contributions: (1)~an \textbf{episode-level counterfactual diagnostic framework} that overcomes per-step oracle degeneracy (97.4\% tie rate) in sparse-reward environments, enabling routing signal decomposition (\S\ref{sec:collection}--\ref{sec:daf}); (2)~applying this framework to ScienceWorld, we find that \textbf{78.9\% of non-tie routing labels} stem from death asymmetry---a single mechanism dominates routing signal (\S\ref{sec:death-decomp}--\ref{sec:agent-improvement}); (3)~\textbf{cross-model validation} (Llama-3.1-8B, DAF${=}88.2\%$), four intervention axes, and cross-environment boundary probes (MATH, ALFWorld) confirm the framework's diagnostic utility and the robustness of the finding (\S\ref{sec:math-contrast}--\ref{sec:cross-model}).
16	
17	
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a85c2cf3-a3ab-4bbf-bcc6-d3346a848983",
  "isSidechain": true,
  "promptId": "44bc2991-8df5-496d-9b2e-d19feb4a03d2",
  "agentId": "a13f9f1b8ad8fec76",
  "type": "user",
  "uuid": "6d69bbc8-2fa7-4dfa-8a09-3b47147db4f4",
  "sourceToolAssistantUUID": "a85c2cf3-a3ab-4bbf-bcc6-d3346a848983",
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

_source line 9 · 2026-05-19T18:15:37.820Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L1NK9i33tMix2yShkVPN5V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d69bbc8-2fa7-4dfa-8a09-3b47147db4f4",
  "isSidechain": true,
  "agentId": "a13f9f1b8ad8fec76",
  "requestId": "req_011CbCPDfoo9eeVdBQ7xy3Co",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db2b3fe7-ae26-4ae1-9d75-611d8b96f647",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VT88bpvpRTgkMvpKgnVjq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37064,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37064,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T18:15:37.834Z_

<details><summary>↩ Tool result · `toolu_01L1NK9i33tMix2yShkVPN5V`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically (Appendix~\ref{app:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
5	
6	\subsection{Problem Setup}
7	\label{sec:problem-setup}
8	
9	Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\cite{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic} (${\tt det}$), where the agent receives ground-truth observations from the environment simulator at each step. A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \mathcal{M}$ selects which computation mode to use at each step; our analysis investigates what signal is available to learn $\rho$. A reasoning-depth ablation ($n{=}120$) found no significant difference ($p > 0.26$; Appendix~\ref{app:ablations}).
10	
11	\subsection{Counterfactual Episode Collection}
12	\label{sec:collection}
13	
14	Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation mode. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \cite{scienceworld-2022}, 97.4\% of steps produce identical intermediate scores regardless of computation mode (5{,}726 of 5{,}878 steps across 11 prescreened task types), yielding no per-step routing signal. The 97.4\% tie rate arises because ScienceWorld assigns rewards only at episode termination; intermediate steps update environment state but do not change the score, so a per-step oracle can only distinguish strategies through downstream consequences visible at episode end. Episode-level comparison is therefore the principled granularity for sparse-reward environments, not a fallback from per-step analysis: it directly measures whether one strategy produces better terminal outcomes than the other, bypassing the uninformative intermediate steps entirely.
15	
16	\paragraph{Pure-strategy trajectories.}
17	For a task instance $t$ and computation mode $m \in \mathcal{M}$, a \emph{pure-strategy trajectory} is the complete episode obtained by applying mode $m$ at every step:
18	\begin{equation}
19	    \tau_m^{(t)} = (o_1, a_1, o_2, a_2, \ldots, o_T, a_T)
20	\end{equation}
21	where $T \leq T_{\max}$ is the episode length (capped at $T_{\max} = 30$ steps). Both trajectories $\tau_{\tt int}^{(t)}$ and $\tau_{\tt det}^{(t)}$ are executed under identical initial conditions (same random seed, same task variation), so performance differences arise solely from the computation mode choice.
22	
23	Each trajectory $\tau$ yields a terminal score $s(\tau) \in \mathbb{Z}$ and a death indicator $d(\tau) \in \{0, 1\}$. When the agent dies ($d = 1$), the environment imposes a penalty: $s(\tau) = -P$ where $P > 0$ ($P = 100$ in ScienceWorld). The episode pair produces a tuple:
24	\begin{multline}
25	    \bigl(s^{\tt int}, s^{\tt det}, d^{\tt int}, d^{\tt det}\bigr) \triangleq \\
26	    \bigl(s(\tau_{\tt int}),\, s(\tau_{\tt det}),\, d(\tau_{\tt int}),\, d(\tau_{\tt det})\bigr)
27	\end{multline}
28	
29	We use Qwen2.5-7B-Instruct~\citep{qwen25-2024} (vLLM) on ScienceWorld \cite{scienceworld-2022}, a text-based environment spanning 30 task types with a $-100$ death penalty. After prescreening, we collect 245 episode pairs across 11 task types (20--40 per type). The framework is applicable to any environment where paired episodes under two computation modes can be collected with binary success/failure indicators. We apply it unchanged to ALFWorld and MATH in \S\ref{sec:math-contrast}--\ref{sec:cross-env}.
30	
31	\subsection{Episode-Level Labeling}
32	\label{sec:labeling}
33	
34	We define a labeling function $L$ that maps a counterfactual pair to a routing preference:
35	\begin{multline}
36	    L\!\bigl(\tau_{\tt int}^{(t)}, \tau_{\tt det}^{(t)}\bigr) \;\rightarrow \\
37	    \ell \in \{{\tt det\text{-}pref},\; {\tt int\text{-}pref},\; {\tt no\text{-}pref}\}
38	\end{multline}
39	
40	The labeling function is \emph{death-aware}: it prioritizes survival over score, then compares scores among same-status episodes (Algorithm~\ref{alg:labeling}; Appendix~\ref{app:labeling}). ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. Figure~\ref{fig:pipeline} illustrates the overall pipeline; label distributions are reported in \S\ref{sec:death-decomp}.
41	
42	\begin{figure}[t]
43	\centering
44	\includegraphics[width=\columnwidth]{figures/pipeline_overview.pdf}
45	\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\ref{alg:labeling}.}
46	\label{fig:pipeline}
47	\end{figure}
48	
49	\subsection{Death Avoidance Factor}
50	\label{sec:daf}
51	
52	To quantify the contribution of death avoidance to routing signal, we decompose the mean score gap between strategies. Let $\delta = \mathbb{E}[d^{\tt int}] - \mathbb{E}[d^{\tt det}]$ denote the death-rate differential and $\Delta_{\text{nd}}$ the mean score gap restricted to episodes where neither strategy dies. Partitioning episodes by death status, death-asymmetric episodes (where only one strategy dies) contribute a per-episode gap of $P + \bar{s}_{\text{surv}}$, where $\bar{s}_{\text{surv}}$ is the surviving strategy's mean score; when $\bar{s}_{\text{surv}} \ll P$ (in our data, $\bar{s}_{\text{surv}} = 0.87$, or $0.9\%$ of $P$), these episodes contribute ${\approx}\,\delta P$ in aggregate. The full gap thus decomposes as:
53	\begin{equation}
54	    \Delta_{\text{full}} \approx \underbrace{\delta \cdot P}_{\text{death contribution}} + \Delta_{\text{nd}}
55	\end{equation}
56	The approximation residual is $29.60 - 29.37 = 0.23$ ($0.8\%$ of $\Delta_{\text{full}}$).
57	
58	We define the Death Avoidance Factor (DAF) as the fraction of the full score gap attributable to death avoidance:
59	\begin{equation}
60	    \text{DAF} = 1 - \frac{\Delta_{\text{nd}}}{\Delta_{\text{full}}} \approx \frac{\delta P}{\delta P + \Delta_{\text{nd}}}
61	\end{equation}%
62	\footnote{When $\Delta_{\text{nd}} < 0$ (deterministic strategy scores lower than internal on non-death episodes), DAF exceeds 1; death avoidance then overcompensates for a non-death disadvantage.}
63	
64	Since DAF $= \delta P / (\delta P + \Delta_{\text{nd}})$, it increases monotonically with $P$, a mathematical consequence rather than an empirical finding. We therefore report both DAF at the environment default ($P{=}100$) and the penalty-independent death-asymmetry label fraction as complementary metrics. In ScienceWorld, $P$ affects only post-hoc score calculation; the agent's policy (ReAct prompting) does not include $P$ in its observation, so death rates and $\Delta_{\text{nd}}$ are $P$-invariant by design (Appendix~\ref{app:penalty}).
65	
66	\paragraph{Statistical inference.}
67	We quantify uncertainty via episode-level bootstrap resampling ($B = 10{,}000$). Each resample draws $N = 245$ episodes with replacement, recomputes all metrics, and derives percentile-based 95\% CIs. We resample at the episode level (not the step level) because the episode is the unit of counterfactual comparison. Penalty sensitivity analysis across hypothetical $P$ values is in Appendix~\ref{app:penalty}.
68	
69	We also measure whether death-avoidance signal is concentrated in a few task types via a Signal Concentration Index (SCI $\in [0, 1]$; Appendix~\ref{app:sci}), reported in \S\ref{sec:death-decomp}.
70	
71	\paragraph{Scope of episode-level analysis.}
72	At step level, 97.4\% of oracle comparisons yield ties (\S\ref{sec:collection}); of 2{,}040 training steps, only 0.3\% exhibit strict directional conflict with episode labels, with 60.3\% pre-event neutral (neither strategy advantaged). Episode labels thus apply correct direction to uninformative steps---a granularity mismatch, not label error---explaining why step-level router training approaches chance performance (\S\ref{sec:router-diagnostic}).
73	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db2b3fe7-ae26-4ae1-9d75-611d8b96f647",
  "isSidechain": true,
  "promptId": "44bc2991-8df5-496d-9b2e-d19feb4a03d2",
  "agentId": "a13f9f1b8ad8fec76",
  "type": "user",
  "uuid": "5e493c6f-6394-4079-84ce-cdec407db95d",
  "sourceToolAssistantUUID": "db2b3fe7-ae26-4ae1-9d75-611d8b96f647",
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

_source line 11 · 2026-05-19T18:15:38.325Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ADH9B1kjyFNgz9nYhiY9xA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e493c6f-6394-4079-84ce-cdec407db95d",
  "isSidechain": true,
  "agentId": "a13f9f1b8ad8fec76",
  "requestId": "req_011CbCPDfoo9eeVdBQ7xy3Co",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fddabdbb-5ee4-4311-81ea-8471d3a3e937",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VT88bpvpRTgkMvpKgnVjq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37064,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37064,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T18:15:38.330Z_

<details><summary>↩ Tool result · `toolu_01ADH9B1kjyFNgz9nYhiY9xA`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Why the router fails: task-type-level signal.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property (10/11 types carry death risk), but step-level features correlate weakly because death risk depends on multi-step trajectories. The 4B router improves at episode level ($59.0\%$) without step-level gains ($56$--$59\%$), confirming task-type classification; cross-task-type transfer yields chance accuracy (49.2\%; Appendix~\ref{app:ablations}).
6	
7	\paragraph{Non-triviality of death dominance.}
8	While death dominance follows from the penalty structure (\S\ref{sec:daf}), its practical implications were not predictable a priori. Existing routing work (Toolformer, CogRouter, ART, When2Tool, RouteLLM) implicitly assumes diverse signals; our finding that 78.9\% of labels trace to a single mechanism contradicts this assumption. Intervention resistance confirms non-triviality: all four axes fail to eliminate death dominance (72B DAF${}= 92.4\%$; Reflexion DAF${}>100\%$ with $\Delta_{\text{nd}} = -0.47$; action filtering leaves ${\geq}12$~pp residual gap; threshold routing with perfect death knowledge cannot outperform always-deterministic). Cross-model stability (Qwen $+26.5$~pp, Llama $+30.0$~pp, both ${\sim}42\%$ internal DR) suggests death vulnerability is a task-environment property, not model-specific. Precise quantification (78.9\%, not ``most'') enables principled deployment decisions; more aggressive interventions remain untested, so we characterize a ceiling, not a universal bound.
9	
10	\paragraph{Anatomy of catastrophic failure.}
11	All 105 internal-strategy deaths trace to misuse of \texttt{focus on [object]}, the answer-submission action, as a general interaction command (Appendix~\ref{app:failure-modes}). The root cause is grounding failure: agents parse task descriptions correctly but cannot map understanding to valid primitives. The internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not different within-episode behavior (${\sim}5\%$ \texttt{focus on} rate in both); lethality depends jointly on misuse rate and answer distribution (\texttt{find-non-living-thing}: zero deaths despite high submission rate). Direct grounding interventions reduce but do not eliminate vulnerability ($48.0\% \to 29.0\%$; Appendix~\ref{app:grounding-ablation}).
12	
13	\paragraph{Practical value of routing.}
14	The framework reveals that 96.3\% of oracle decisions favor always-deterministic, with 61.2\% of episodes showing no strategy preference---routing is nearly unnecessary on ScienceWorld. This diagnostic finding matters because it prevents wasted computation: a ${\sim}$50-episode pilot (Appendix~\ref{app:decision-framework}) correctly predicts outcomes for all four conditions, while our router training consumed ${\sim}$200 GPU-hours without exceeding the always-deterministic baseline.
15	
16	\paragraph{Framework applicability.}
17	The penalty-independent label fraction (78.9\%) is the primary diagnostic; DAF increases monotonically with $P$ (Appendix~\ref{app:penalty}). Preliminary pilots on MiniHack~\citep{minihack-2021} (0\% death) and Crafter~\citep{crafter-2022} (100\% death, both strategies) produced no death asymmetry, illustrating two boundary conditions: no death mechanism yields no signal; universal death lacks exploitable asymmetry. NetHack~\citep{nethack-2020} combat tasks remain the most direct replication target \citep{balrog-2025,netplay-2024}.
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fddabdbb-5ee4-4311-81ea-8471d3a3e937",
  "isSidechain": true,
  "promptId": "44bc2991-8df5-496d-9b2e-d19feb4a03d2",
  "agentId": "a13f9f1b8ad8fec76",
  "type": "user",
  "uuid": "3f5312e2-7d8d-4409-87ce-4c43bafe760d",
  "sourceToolAssistantUUID": "fddabdbb-5ee4-4311-81ea-8471d3a3e937",
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

_source line 13 · 2026-05-19T18:15:38.814Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AXB1fbLD125q52BpHkBHqu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f5312e2-7d8d-4409-87ce-4c43bafe760d",
  "isSidechain": true,
  "agentId": "a13f9f1b8ad8fec76",
  "requestId": "req_011CbCPDfoo9eeVdBQ7xy3Co",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "177ab253-6b07-410f-b2e6-e478021c7781",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VT88bpvpRTgkMvpKgnVjq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37064,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37064,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T18:15:38.821Z_

<details><summary>↩ Tool result · `toolu_01AXB1fbLD125q52BpHkBHqu`</summary>

```text
1	\section{Conclusion}
2	
3	We introduced an episode-level counterfactual diagnostic framework for decomposing routing signal in modular LLM agents, overcoming per-step oracle degeneracy (97.4\% tie rate) through paired pure-strategy comparison with penalty-independent (label fraction) and penalty-dependent (DAF) metrics. Applied to ScienceWorld, 78.9\% of non-tie routing labels stem from death asymmetry---robust across four intervention axes, cross-model replication (Llama-3.1-8B, DAF${=}88.2\%$), and boundary probes (MATH, ALFWorld). The diagnostic value is practical: our 200 GPU-hour router training could not outperform the always-deterministic baseline, an outcome a 50-episode pilot would have predicted.
4	
5	The framework applies to any environment with episode-level evaluation and binary catastrophic outcomes. Future work should target intermediate death regimes (NetHack combat tasks), develop methods to disentangle label noise from fundamental non-learnability in step-level routing, and extend to mixed-strategy routing and stronger backbones.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "177ab253-6b07-410f-b2e6-e478021c7781",
  "isSidechain": true,
  "promptId": "44bc2991-8df5-496d-9b2e-d19feb4a03d2",
  "agentId": "a13f9f1b8ad8fec76",
  "type": "user",
  "uuid": "6a48a987-d5ea-4ad4-adef-e5b1a5bb5551",
  "sourceToolAssistantUUID": "177ab253-6b07-410f-b2e6-e478021c7781",
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

_source line 15 · 2026-05-19T18:15:39.719Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CubVauz5iZQDBxF2uxR6Qv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a48a987-d5ea-4ad4-adef-e5b1a5bb5551",
  "isSidechain": true,
  "agentId": "a13f9f1b8ad8fec76",
  "requestId": "req_011CbCPDfoo9eeVdBQ7xy3Co",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1921f209-185f-4beb-b8d0-0b38fe5ee882",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VT88bpvpRTgkMvpKgnVjq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37064,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37064,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T18:15:39.752Z_

<details><summary>↩ Tool result · reported error · `toolu_01CubVauz5iZQDBxF2uxR6Qv`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1921f209-185f-4beb-b8d0-0b38fe5ee882",
  "isSidechain": true,
  "promptId": "44bc2991-8df5-496d-9b2e-d19feb4a03d2",
  "agentId": "a13f9f1b8ad8fec76",
  "type": "user",
  "uuid": "666268e2-5347-45a8-8929-34b055def506",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01.",
  "sourceToolAssistantUUID": "1921f209-185f-4beb-b8d0-0b38fe5ee882",
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

_source line 17 · 2026-05-19T18:15:45.354Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01VL7xuiCM2Pnqhvzq6ZTp7X`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "666268e2-5347-45a8-8929-34b055def506",
  "isSidechain": true,
  "agentId": "a13f9f1b8ad8fec76",
  "requestId": "req_011CbCPEUpXWA6E6g48rpAh8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48bda8ef-97cd-42e1-9d02-9b1bbe1b5c10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3XxSZYTe6xQY42tUoTQio",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4480,
      "cache_read_input_tokens": 37064,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4480
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 37064,
          "cache_creation_input_tokens": 4480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4480,
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

_source line 18 · 2026-05-19T18:15:45.373Z_

<details><summary>↩ Tool result · `toolu_01VL7xuiCM2Pnqhvzq6ZTp7X`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/responsibleNLPchecklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48bda8ef-97cd-42e1-9d02-9b1bbe1b5c10",
  "isSidechain": true,
  "promptId": "44bc2991-8df5-496d-9b2e-d19feb4a03d2",
  "agentId": "a13f9f1b8ad8fec76",
  "type": "user",
  "uuid": "5aeafad9-67b4-4d89-9a84-da1228086fb0",
  "sourceToolAssistantUUID": "48bda8ef-97cd-42e1-9d02-9b1bbe1b5c10",
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

_source line 19 · 2026-05-19T18:15:50.789Z_

<details open><summary>🔧 Tool call — Read · `toolu_018i3GjDWS6fMt4bnXv4VZCM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5aeafad9-67b4-4d89-9a84-da1228086fb0",
  "isSidechain": true,
  "agentId": "a13f9f1b8ad8fec76",
  "requestId": "req_011CbCPEtqACJD43NJwy65dB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8edf512-1ab3-41ad-a335-bb19c69a4309",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WR1vKzPX6sN7aY6aJtk2cs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 41544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 464,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
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

_source line 20 · 2026-05-19T18:15:50.800Z_

<details><summary>↩ Tool result · `toolu_018i3GjDWS6fMt4bnXv4VZCM`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}, spanning several functional categories.
5	\emph{Self-supervised} approaches learn tool invocation from loss signals: Toolformer \cite{toolformer-2023} inserts API calls filtered by perplexity reduction; ToolACE \cite{toolace-2025} curates synthetic data for function-calling accuracy.
6	\emph{Token-level} methods embed tools into the model vocabulary: ToolkenGPT \cite{toolkengpt-2023} represents tools as special tokens resolved at inference.
7	\emph{Task-level} decomposition routes subtasks to specialized modules: ART \cite{art-2023} generates tool-augmented programs; Chameleon \cite{chameleon-2023} composes heterogeneous modules per subtask.
8	\emph{RL-based} methods learn routing policies from reward: ReTool \cite{retool-2025} discovers when code execution is preferable to chain-of-thought.
9	All focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
10	Concurrent work examines \emph{when} to invoke tools: \citet{tool-overuse-illusion-2026} find tool overuse correlates with model uncertainty; \citet{when2tool-2026} show tool-call decisions are encoded in hidden states; \citet{tool-use-tax-2026} quantify a ``tool-use tax''; \citet{to-call-or-not-2026} propose a necessity-utility-affordability framework. Our decomposition provides environment-grounded evidence: in ScienceWorld, 78.9\% of routing labels trace to catastrophic-failure prevention.
11	
12	\paragraph{Adaptive Computation and Routing.}
13	Adaptive routing traces back to learned halting policies \citep{graves2016act}. In the LLM era, CogRouter \cite{cogrouter-2026} adapts reasoning depth per step, ARES \cite{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \cite{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \cite{mtrouter-2026} addresses multi-turn routing.
14	RouteLLM \citep{routellm-2024} learns routers from preference data to select between strong and weak models.
15	These optimize \emph{how} to route; we reveal \emph{why} routing helps: in interactive environments, the dominant signal is catastrophic-failure avoidance.
16	
17	\paragraph{Counterfactual Evaluation in RL.}
18	Prior work generates counterfactual explanations for RL agents by perturbing individual actions within a fixed policy \citep{olson2021counterfactual, gajcin2023counterfactual, amitai2024explaining}.
19	Our approach differs in both purpose and granularity: we execute two complete episodes under different routing strategies, producing prospective paired comparisons that isolate routing signal \emph{before} any router is trained.
20	
21	\paragraph{LLM Agent Environments and Reasoning.}
22	ScienceWorld \cite{scienceworld-2022} serves as our primary testbed; ALFWorld \cite{alfworld-2021} provides a complementary household environment; AgentBench \cite{agentbench-2024} offers systematic evaluation. \citet{zhou2024webarena} document common failure modes (premature termination, hallucinated actions) in web-based agents, consistent with our finding that state hallucination is the primary failure mechanism. ReAct \cite{react-2023} serves as our internal baseline; Reflexion \cite{reflexion-2023} extends this with verbal self-reflection; LATS \cite{lats-2024} adds tree search.
23	
24	\paragraph{Safe RL.}
25	Death avoidance as an implicit routing signal connects to safe RL. Constrained MDPs \citep{altman1999constrained} formalize safety through state or cost constraints; our mechanism can be viewed as an implicit absorbing-state constraint. Risk-sensitive RL \citep{mihatsch2002risk} optimizes CVaR-type objectives; our framework diagnoses when such risk-sensitivity emerges rather than prescribing it. Classical methods \citep{garcia2015comprehensive,tamar2015cvar,achiam2017cpo,crpo-2021,moldovan2012safe} require explicit constraint specification; our routing achieves safety implicitly through computation mode selection. \citet{ruan2024failures} provide a taxonomy of LM agent failures identifying catastrophic actions as a distinct category, consistent with our finding. SafeRoute \citep{saferoute-2025} applies adaptive model selection for safety guardrails.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8edf512-1ab3-41ad-a335-bb19c69a4309",
  "isSidechain": true,
  "promptId": "44bc2991-8df5-496d-9b2e-d19feb4a03d2",
  "agentId": "a13f9f1b8ad8fec76",
  "type": "user",
  "uuid": "a7c6605a-d892-4f8a-8af9-2034a60aac32",
  "sourceToolAssistantUUID": "f8edf512-1ab3-41ad-a335-bb19c69a4309",
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

_source line 21 · 2026-05-19T18:15:51.141Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BsqQGmuGZS8R9oEneSj5sy`</summary>

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
  "parentUuid": "a7c6605a-d892-4f8a-8af9-2034a60aac32",
  "isSidechain": true,
  "agentId": "a13f9f1b8ad8fec76",
  "requestId": "req_011CbCPEtqACJD43NJwy65dB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6eed4b47-eb81-4d72-b96e-8c4545f563cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WR1vKzPX6sN7aY6aJtk2cs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 41544,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 464
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 41544,
          "cache_creation_input_tokens": 464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 464,
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

_source line 22 · 2026-05-19T18:15:51.419Z_

<details><summary>↩ Tool result · `toolu_01BsqQGmuGZS8R9oEneSj5sy`</summary>

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
36	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct); generalization requires further validation. The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface non-death-dominated signal that our current setup does not capture. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:cross-env}, \S\ref{sec:discussion}) provide preliminary supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct cross-model replication (11 task types, $N{=}220$; \S\ref{sec:cross-model}) shows death dominance replicates with direction consistency 10/10 while vulnerability magnitude varies ($+30.0$~pp vs.\ Qwen $+26.5$~pp), though both models are in the 7--8B parameter range; Qwen2.5-72B ($10{\times}$ scale) reduces death rate but does not eliminate death dominance (\S\ref{sec:agent-improvement}); validation beyond 72B remains future work. Our quantitative results (DAF $= 90.4\%$, label fractions) are specific to ScienceWorld; the framework's generality claim is methodological (the diagnostic procedure applies to any environment with asymmetric fatal outcomes), not empirical (the specific percentages may differ across environments).
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
70	\hyperref[app:decision-framework]{R.~Decision Framework}
71	
72	\section{Signal Concentration Index}
73	\label{app:sci}
74	
75	Let $K$ denote the number of task types and $c_k$ the contribution of task type $k$ to the aggregate routing signal, defined as the fraction of total death-rate differential attributable to task $k$:
76	\begin{equation}
77	    c_k = \frac{n_k \cdot \delta_k}{\sum_{j=1}^{K} n_j \cdot \delta_j}
78	\end{equation}
79	where $n_k$ is the number of episodes and $\delta_k = d_k^{\tt int} - d_k^{\tt det}$ is the per-task death-rate differential. The SCI is the Gini coefficient over $\{c_1, \ldots, c_K\}$:
80	\begin{equation}
81	    \text{SCI} = \frac{\sum_{i=1}^K \sum_{j=1}^K |c_i - c_j|}{2K \sum_{k=1}^K c_k}
82	\end{equation}
83	
84	\section{Labeling Quality Audit}
85	\label{app:labeling}
86	
87	\begin{algorithm}[t]
88	\caption{Episode-Level Counterfactual Labeling}
89	\label{alg:labeling}
90	\begin{algorithmic}[1]
91	\REQUIRE Task instance $t$, modalities $\mathcal{M} = \{{\tt int}, {\tt det}\}$
92	\ENSURE Label $\ell \in \{{\tt det\text{-}pref}, {\tt int\text{-}pref}, {\tt no\text{-}pref}\}$
93	\FOR{each $m \in \mathcal{M}$}
94	    \STATE Run episode $\tau_m$ with pure-strategy $m$
95	    \STATE Record score $s_m$ and death indicator $d_m$
96	\ENDFOR
97	\IF{$d_{\tt int} = 1$ \AND $d_{\tt det} = 0$}
98	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{death asymmetry}
99	\ELSIF{$d_{\tt int} = 0$ \AND $d_{\tt det} = 1$}
100	    \STATE $\ell \leftarrow {\tt int\text{-}pref}$ \COMMENT{death asymmetry}
101	\ELSIF{$d_{\tt int} = d_{\tt det} = 1$}
102	    \STATE $\ell \leftarrow {\tt no\text{-}pref}$ \COMMENT{both dead}
103	\ELSIF{$s_{\tt det} > s_{\tt int}$}
104	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{score comparison}
105	\ELSIF{$s_{\tt int} > s_{\tt det}$}
106	    \STATE $\ell \leftarrow {\tt int\text{-}pref}$ \COMMENT{score comparison}
107	\ELSE
108	    \STATE $\ell \leftarrow {\tt no\text{-}pref}$ \COMMENT{tied alive}
109	\ENDIF
110	\RETURN $\ell$
111	\end{algorithmic}
112	\end{algorithm}
113	
114	A potential concern is oracle circularity: whether episode-level labels reflect tie-breaking artifacts rather than genuine computation mode differences. We audit all 245 labels. Of the 150 \texttt{no\_preference} labels (61.2\%), 115 (46.9\%) are both-alive ties and 35 (14.3\%) are both-dead, all excluded from router training. The remaining 95 training labels are entirely genuine: 75 from death asymmetry (70 deterministic-preferred, 5 internal-preferred) and 20 from score comparison with both strategies surviving (16 deterministic-preferred, 4 internal-preferred). Zero labels depend on tie-breaking. Retraining the router using only death-asymmetry labels yields step-level balanced accuracy of 57.3\%, within 1$\sigma$ of the full-label retrain (57.6 $\pm$ 0.5\%, step-level Trainer evaluation); score-comparison labels contribute negligible additional signal. (Step-level metrics are used here for the relative comparison; as shown in \S\ref{sec:router-diagnostic}, absolute generalization to new episodes is near chance.) The 97.4\% step-level tie rate (\S\ref{sec:collection}) further motivates episode-level over step-level labeling.
115	
116	\section{Per-Task Decomposition}
117	\label{app:per-task}
118	We select 11 of ScienceWorld's 30 task types for analysis. Types are excluded when they were used for pipeline development (5 tasks, standard hold-out practice), are taxonomically redundant with a retained family representative (7 tasks), or exhibit near-zero task progress under both strategies (7 tasks, agent capability floor).\footnote{Excluded tasks exhibit even stronger death dominance than included tasks ($\Delta\text{DR} = +38.2$\,pp vs.\ $+28.7$\,pp; Table~\ref{tab:excluded-death}).}
119	
120	\begin{table}[h]
121	\centering
122	\scriptsize
123	\setlength{\tabcolsep}{2.5pt}
124	\begin{tabular}{@{}lrrccc@{}}
125	\toprule
126	Task & $n$ & $\Delta_\text{full}$ & D\%\textsubscript{int} & D\%\textsubscript{det} & D / I / N \\
127	\midrule
128	id-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\
129	lifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\
130	lifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\
131	inclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\
132	freeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\
133	meas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\
134	id-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\
135	find-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\
136	grow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\
137	chem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\
138	\midrule
139	find-non-living-thing$^\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\
140	\midrule
141	\textbf{All (11 tasks)} & \textbf{245} & $\mathbf{+29.60}$ & \textbf{42.9} & \textbf{16.3} & \textbf{86 / 9 / 150} \\
142	\bottomrule
143	\end{tabular}
144	\caption{Per-task decomposition of the death avoidance effect. D\%: death rate for internal (int) and deterministic (det) strategies. D/I/N: episode labels (det-preferred / internal-preferred / no-preference). Sorted by $\Delta_{\text{full}}$ descending. $\dagger$\,Only task with zero deaths under both strategies; $n{=}40$ because data was collected in two batches, with the second batch adding 20 episodes to increase statistical power for this zero-death outlier.}
145	\label{tab:per-task}
146	\end{table}
147	
148	\paragraph{Task selection and anti-cherry-picking.}
149	Eighteen of the 19 excluded task types (95\%) exhibit death-asymmetric patterns (Table~\ref{tab:excluded-death}): internal-reasoning death rates range from 40\% to 60\% (mean 53.9\%), while deterministic death rates range from 0\% to 40\% (mean 15.8\%), yielding a mean death-rate differential of $+38.2$\,pp, exceeding the $+28.7$\,pp for included tasks. The included subset is thus \emph{less} death-asymmetric than the excluded subset, the opposite of what a cherry-picking hypothesis would predict. The sole exception is \texttt{grow-plant}, an intrinsically safe task with zero deaths under both strategies, paralleling \texttt{find-non-living-thing} in the included set. The 19 excluded tasks fall into three independently motivated categories: five used during pipeline development (standard hold-out practice), seven taxonomically redundant with included family representatives (deduplication), and seven where the 7B backbone achieves near-zero task progress regardless of strategy (agent capability floor). In no case was a task excluded because death dominance was absent. Exclusion is driven by absence of non-death routing signal ($\Delta_{\text{nd}} = 0$ for 53\% of excluded tasks) and standard deduplication practices. \texttt{find-non-living-thing} serves as an internal counterexample: zero deaths under both strategies yet included because it exhibits non-death routing signal ($\Delta_{\text{full}} = +9.58$ entirely from score differences), and deterministic is not always preferred (4 of 20 non-tie labels favor internal).
150	
151	\begin{table}[t]
152	\centering
153	\scriptsize
154	\setlength{\tabcolsep}{2pt}
155	\begin{tabular}{@{}llrcccl@{}}
156	\toprule
157	Task & Grp & $n$ & D\%\textsubscript{int} & D\%\textsubscript{det} & $\Delta$DR & Excl.\ reason \\
158	\midrule
159	boil                          & A & 20 & 50 & 20 & $+30$ & dev set \\
160	change-state-of-matter        & A & 20 & 55 & 15 & $+40$ & dev set \\
161	chem-mix-paint-secondary      & A & 20 & 45 & 10 & $+35$ & dev set \\
162	grow-plant                    & A & 20 &  0 &  0 & $\phantom{+}0$  & dev set \\
163	melt                          & A & 20 & 55 & 15 & $+40$ & dev set \\
164	\midrule
165	chem-mix-paint-tertiary       & B &  5 & 40 & 20 & $+20$ & family redundancy \\
166	find-living-thing             & B &  5 & 60 & 20 & $+40$ & family redundancy \\
167	find-plant                    & B &  5 & 60 &  0 & $+60$ & family redundancy \\
168	inclined-friction-named       & B &  5 & 60 & 20 & $+40$ & family redundancy \\
169	inclined-friction-unnamed     & B &  5 & 60 &  0 & $+60$ & family redundancy \\
170	lifespan-shortest             & B &  5 & 60 & 40 & $+20$ & family redundancy \\
171	measure-melt-known            & B &  5 & 60 &  0 & $+60$ & family redundancy \\
172	\midrule
173	mendelian-known               & C &  5 & 60 & 20 & $+40$ & agent floor \\
174	mendelian-unknown             & C &  5 & 60 & 40 & $+20$ & agent floor \\
175	power-component               & C &  5 & 60 & 20 & $+40$ & agent floor \\
176	power-renewable               & C &  5 & 60 &  0 & $+60$ & agent floor \\
177	test-conductivity             & C &  5 & 60 & 20 & $+40$ & agent floor \\
178	test-conductivity-unknown     & C &  5 & 60 & 20 & $+40$ & agent floor \\
179	use-thermometer               & C &  5 & 60 & 20 & $+40$ & agent floor \\
180	\midrule
181	\textbf{Mean (19 excluded)}   &   &    & \textbf{53.9} & \textbf{15.8} & $\mathbf{+38.2}$ & \\
182	\textit{cf.\ included (11)}   &   &    & \textit{46.5} & \textit{17.8} & $\textit{+28.7}$ & \\
183	\bottomrule
184	\end{tabular}
185	\caption{Death-rate analysis of all 19 excluded task types. D\%: death rate (score $\leq -100$). $\Delta$DR = D\%\textsubscript{int} $-$ D\%\textsubscript{det}. 18 of 19 excluded tasks (95\%) exhibit positive death asymmetry ($\Delta$DR $\geq +20$\,pp). Exclusion groups: A = development set (excluded to prevent circular evaluation), B = taxonomically redundant with an included family representative, C = agent-floor tasks (backbone achieves near-zero progress regardless of strategy). The mean $\Delta$DR among excluded tasks ($+38.2$\,pp) exceeds that of included tasks ($+28.7$\,pp), confirming that task selection does not bias toward death-prone tasks. Group B--C estimates are based on $n{=}5$ prescreening episodes per task and should be interpreted as directional evidence rather than precise rate estimates.}
186	\label{tab:excluded-death}
187	\end{table}
188	
189	\section{Correlation Robustness}
190	\label{app:correlation}
191	
192	The Pearson $r = 0.9698$ reported in \S\ref{sec:death-decomp} is robust across multiple diagnostics. Spearman rank correlation is $\rho = 0.986$ ($p = 2.4 \times 10^{-8}$); the relationship is not driven by outliers or non-linearity. A nonparametric bootstrap (10{,}000 resamples) yields 95\% CI $[0.952, 0.995]$.
193	
194	\begin{table}[h]
195	\centering
196	\small
197	\begin{tabular}{@{}lr@{}}
198	\toprule
199	Task removed & $r_{\text{LOO}}$ \\
200	\midrule
201	id-life-stages-1       & 0.963 \\
202	lifespan-long          & 0.969 \\
203	lifespan-l-then-s      & 0.976 \\
204	inclined-plane         & 0.969 \\
205	freeze                 & 0.971 \\
206	meas-melt-point        & 0.972 \\
207	id-life-stages-2       & 0.972 \\
208	find-animal            & 0.970 \\
209	grow-fruit             & 0.973 \\
210	chem-mix               & 0.969 \\
211	find-non-living-thing  & 0.980 \\
212	\bottomrule
213	\end{tabular}
214	\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\ $\Delta_{\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}
215	\label{tab:loo}
216	\end{table}
217	
218	\section{Wild Cluster Bootstrap}
219	\label{app:wild-cluster}
220	
221	Episodes within the same task type share environment dynamics, raising the concern that the effective sample size is closer to $K$ (task types) than $N$ (episodes). We address this with cluster-robust inference treating each task type as a cluster ($K{=}11$, all 11 included task types, 245 episodes).
222	
223	\begin{table}[h]
224	\centering
225	\small
226	\begin{tabular}{@{}lcc@{}}
227	\toprule
228	Method & $p$-value & 95\% CI \\
229	\midrule
230	Cluster-robust $t$-test ($t{=}10.0$, df$=$10) & $< 0.001$ & $[0.73, 1.00]$ \\
231	Wild cluster bootstrap ($B{=}9{,}999$) & $< 0.001$ & $[0.73, 1.00]$ \\
232	Exact permutation ($2{,}048$ perms) & $0.002$ & --- \\
233	Sign test & $< 0.001$ & --- \\
234	\bottomrule
235	\end{tabular}
236	\caption{Cluster-level tests of death-rate asymmetry ($K{=}11$ task clusters, 245 episodes). 10 of 11 clusters show internal DR $>$ deterministic DR; the sole exception (\texttt{find-non-living-thing}) has zero deaths under both strategies. Cohen's $d = 3.02$. The exact permutation $p = 0.002$ ($4/2{,}048$) reflects the near-unanimous directional consistency.}
237	\label{tab:wild-cluster}
238	\end{table}
239	
240	\noindent All methods confirm significance with $p < 0.01$, and the 95\% CI $[0.73, 1.00]$ excludes zero by a wide margin. The $K{=}11$ analysis uses the same clusters as the main analysis, providing a direct robustness check on the primary results.
241	
242	\section{Per-Task Death Rate Confidence Intervals}
243	\label{app:per-task-ci}
244	
245	We compute bootstrap 95\% CIs for the death-rate differential ($\Delta\text{DR} = \text{DR}_{\text{int}} - \text{DR}_{\text{det}}$) for all 30 ScienceWorld task types. Of 30 tasks, 28 are death-prone (at least one death under either strategy); the remaining 2 (\texttt{grow-plant}, \texttt{find-non-living-thing}) have zero deaths under both strategies.
246	
247	Across all 28 death-prone tasks, internal DR exceeds deterministic DR without exception (100\% directional consistency). The pooled death-rate differential is $+37.3\%$ (95\% CI: $[29.7\%, 44.4\%]$). Fifteen of 28 tasks are individually significant (CI excludes zero); the 13 non-significant tasks all have $n{=}5$ prescreening episodes, where statistical power is insufficient to detect even large effects (e.g., a task with $\Delta\text{DR} = +40$\,pp at $n{=}5$ has a CI of $\pm 43$\,pp). The universal directional consistency, combined with the pooled significance, confirms that death asymmetry is not driven by a subset of outlier tasks.
248	
249	\section{Leave-One-Task-Out DAF Sensitivity}
250	\label{app:loto-daf}
251	
252	\begin{table}[h]
253	\centering
254	\small
255	\caption{Leave-one-task-out DAF sensitivity (penalty-independent label fraction). Among the 10 death-prone tasks, removing any single task changes DAF by at most 3.0\,pp (range: 75.9\%--78.9\%). Removing \emph{Find Non-Living Thing}, the sole death-free task that contributes all 20 score-comparison episodes, raises DAF to 100\% by construction.}
256	\label{tab:loto-daf}
257	\begin{tabular}{lrrr}
258	\toprule
259	Removed Task & $N_\text{rem}$ & DAF (\%) & $\Delta$ (pp) \\
260	\midrule
261	(none, full) & 245 & 78.9 & --- \\
262	\midrule
263	Find Non-Living$^\dagger$ & 205 & 100.0 & +21.1 \\
264	Lifespan Longest & 220 & 75.9 & $-$3.0 \\
265	Life Stages 1 & 225 & 76.7 & $-$2.2 \\
266	Lifespan Long+Short & 225 & 76.7 & $-$2.2 \\
267	Chemistry Mix & 225 & 77.0 & $-$1.9 \\
268	Grow Fruit & 225 & 77.3 & $-$1.7 \\
269	Inclined Plane Angle & 225 & 77.3 & $-$1.7 \\
270	Freeze & 225 & 77.5 & $-$1.4 \\
271	Life Stages 2 & 225 & 77.5 & $-$1.4 \\
272	Melt Pt Unknown & 225 & 77.5 & $-$1.4 \\
273	Find Animal & 225 & 77.8 & $-$1.2 \\
274	\bottomrule
275	\end{tabular}
276	
277	\vspace{2pt}
278	{\footnotesize $^\dagger$Only death-free task; contributes all score-comparison labels. Sorted by $|\Delta|$ descending.}
279	\end{table}
280	
281	\section{Per-Task Dose-Response Breakdown}
282	\label{app:dose-response}
283	
284	Table~\ref{tab:dose-response-detail} reports per-task death rates for Reflexion at $N{=}3$, 4, and 5 on the 10 death-prone tasks ($n{=}20$ episodes per task). Per-task variance is high (up to 25\,pp range for \texttt{measure-melting-point}), but the aggregate smooths to a 2.5\,pp band, confirming that the plateau conclusion is robust at the aggregate level despite task-level noise. \texttt{freeze} is consistently the hardest task (50--60\% DR across all $N$).
285	
286	\begin{table}[h]
287	\centering
288	\small
289	\caption{Per-task death rates (\%) for Reflexion at $N{=}3$, 4, 5 on 10 death-prone tasks ($n{=}20$ per task). Aggregate death rates confirm the plateau at $N \geq 3$ (range: $34.0$--$36.5\%$).}
290	\label{tab:dose-response-detail}
291	\begin{tabular}{@{}lrrr@{}}
292	\toprule
293	Task & $N{=}3$ & $N{=}4$ & $N{=}5$ \\
294	\midrule
295	chemistry-mix & 25.0 & 35.0 & 20.0 \\
296	find-animal & 45.0 & 30.0 & 45.0 \\
297	freeze & 50.0 & 50.0 & 60.0 \\
298	grow-fruit & 30.0 & 25.0 & 25.0 \\
299	identify-life-stages-1 & 35.0 & 35.0 & 35.0 \\
300	identify-life-stages-2 & 25.0 & 25.0 & 30.0 \\
301	inclined-plane-angle & 20.0 & 30.0 & 35.0 \\
302	lifespan-longest & 45.0 & 40.0 & 40.0 \\
303	lifespan-long+short & 30.0 & 45.0 & 35.0 \\
304	measure-melting-pt & 35.0 & 50.0 & 25.0 \\
305	\midrule
306	\textbf{Aggregate} & \textbf{34.0} & \textbf{36.5} & \textbf{35.0} \\
307	\bottomrule
308	\end{tabular}
309	\end{table}
310	
311	\section{Router Training Details}
312	\label{app:router-details}
313	
314	We use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.
315	
316	With gradient accumulation of 1 (effective batch size 4), routing performance is highly sensitive to the evaluation split; this suggests overfitting to specific train/validation partition boundaries. With gradient accumulation of 8 (effective batch size 32), step-level performance stabilizes across splits (${\sim}54\%$ balanced accuracy). All reported results use gradient accumulation 8.
317	
318	Under step-level evaluation with a fixed data split, cross-seed balanced accuracy ranges from 52.7\% to 58.1\%, but internal recall varies from 51.5\% to 81.8\%, which reflects threshold sensitivity. However, episode-level evaluation reveals that this apparent discrimination does not generalize: balanced accuracy drops to $47.1 \pm 2.2\%$ across 8 cross-split seeds (Appendix~\ref{app:seed-robustness}). Deployed end-to-end, the trained router allocates 97.0\% of episodes to deterministic computation with 17.6\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.
319	
320	\paragraph{Evaluation methods.} All results use \emph{generation-based evaluation}: the model generates a routing label as text (\texttt{enable\_thinking=False}), parsed for classification. We evaluate at two granularities: \emph{step-level} (steps from the same episode may appear in both train and validation sets) and \emph{episode-level} (entire episodes held out). Step-level accuracy ($54.1 \pm 5.4\%$) exceeds chance (the router captures some signal), but episode-level accuracy ($47.1 \pm 2.2\%$, below chance) shows this does not generalize to unseen episodes. Augmentation-based data scaling (Appendix~\ref{app:seed-robustness}) provides no improvement; real-data scaling remains open. Always-deterministic is trivially near-optimal given DAF $= 90.4\%$. The main text (\S\ref{sec:router-diagnostic}) reports controlled 4-seed results at three scales; the model-size ablation (Appendix~\ref{app:ablations}) provides further detail.
321	
322	\begin{table}[h]
323	\centering
324	\small
325	\resizebox{\columnwidth}{!}{%
326	\begin{tabular}{@{}lcc@{}}
327	\toprule
328	Hyperparameter & Classification Head & Implicit Router \\
329	\midrule
330	Base model & Qwen3-1.7B & Qwen3-1.7B \\
331	Architecture & Linear + LoRA & SFT + LoRA \\
332	LoRA $r$ / $\alpha$ & 16 / 32 & 16 / 32 \\
333	Learning rate & 2e-5 & 2e-4 \\
334	Optimizer & AdamW & AdamW \\
335	Epochs & 3 & 3 \\
336	Batch size (per device) & 4 & 4 \\
337	Gradient accumulation & 8 & 8 \\
338	Warmup ratio & 0.1 & 0.1 \\
339	Weight decay & 0.01 & 0.01 \\
340	Max sequence length & 512 & 512 \\
341	Seeds & \{42\} & \{42, 123, 456, 789\} \\
342	\bottomrule
343	\end{tabular}}
344	\caption{Router training hyperparameters. Both architectures use the same base model with LoRA adaptation. The classification head degenerates across all configurations; the implicit router results are reported as 4-seed mean$\pm$std.}
345	\label{tab:hyperparams}
346	\end{table}
347	
348	\section{Seed Robustness}
349	\label{app:seed-robustness}
350	
351	We assess router generalization at two evaluation granularities: \emph{step-level}, where steps from the same episode may appear in both train and validation sets, and \emph{episode-level}, where entire episodes are held out. Both use cross-split evaluation (seeds $\{42, \ldots, 49\}$, 8 seeds total), where the data partition and training seed both vary. Table~\ref{tab:seed-robustness} reports per-seed results.
352	
353	\begin{table}[h]
354	\centering
355	\small
356	\begin{tabular}{@{}llcc@{}}
357	\toprule
358	Eval.\ Granularity & Seed & Bal.\ Acc.\ (\%) \\
359	\midrule
360	Step-level & 42 & 57.06 \\
361	(same-episode & 43 & 63.99 \\
362	leakage) & 44 & 55.43 \\
363	 & 45 & 56.14 \\
364	 & 46 & 55.45 \\
365	 & 47 & 50.08 \\
366	 & 48 & 48.03 \\
367	 & 49 & 59.30 \\
368	\cmidrule{2-3}
369	 & Mean$\pm$std & $54.1 \pm 5.4$ \\
370	\midrule
371	Episode-level & 42 & 48.1 \\
372	(held-out & 43 & 47.9 \\
373	episodes) & 44 & 49.6 \\
374	 & 45 & 49.4 \\
375	 & 46 & 48.5 \\
376	 & 47 & 43.1 \\
377	 & 48 & 45.4 \\
378	 & 49 & 44.8 \\
379	\cmidrule{2-3}
380	 & Mean$\pm$std & $47.1 \pm 2.2$ \\
381	\midrule
382	\multicolumn{2}{@{}l}{Always-det (= majority-vote)} & 50.0 \\
383	\bottomrule
384	\end{tabular}
385	\caption{Per-seed router performance under cross-split evaluation (8 seeds, generation-based, \texttt{enable\_thinking=False}). Step-level evaluation allows steps from the same episode in both train and validation sets (same-episode leakage). Episode-level evaluation holds out entire episodes; the resulting $47.1 \pm 2.2\%$ is below the 50\% chance baseline. A data scaling ablation (Table~\ref{tab:data-scaling}) confirms this failure persists under the current data distribution and augmentation regime.}
386	\label{tab:seed-robustness}
387	\end{table}
388	
389	The contrast between step-level ($54.1 \pm 5.4\%$) and episode-level ($47.1 \pm 2.2\%$) evaluation reveals a generalization gap: the step-level signal likely reflects memorization of episode-specific context (enabled by same-episode leakage) rather than extraction of generalizable routing features. At episode level, the router performs below chance across all 8 seeds (range: 43.1\%--49.6\%). Augmentation-based data scaling (Table~\ref{tab:data-scaling}) from 25\% to 800\% ($32{\times}$ range) provides no improvement, converging to the always-deterministic baseline ($50\%$). However, paraphrase augmentation inflates the majority class without generating novel routing patterns; real-data scaling remains an open question. With DAF $= 90.4\%$ and all task types deterministic-majority (86:9 label ratio), always-deterministic trivially solves the episode-level routing problem, leaving no learnable signal for a step-level router.
390	
391	\paragraph{Data scaling ablation.} To test whether the episode-level generalization failure stems from data scarcity, we vary training set size from 25\% to 800\% of the original via paraphrase-based data augmentation (synonym substitution + template variation on step observations), holding the episode-level validation set fixed. Table~\ref{tab:data-scaling} reports the results.
392	
393	\begin{table}[h]
394	\centering
395	\small
396	\begin{tabular}{@{}rccc@{}}
397	\toprule
398	Scale & Samples & Det\% & Ep.\ Bal.\ Acc.\ (\%) \\
399	\midrule
400	25\% & 433 & ${\sim}90$ & $49.5 \pm 0.3$ \\
401	50\% & 867 & ${\sim}90$ & $51.5$ \\
402	100\% & 1{,}735 & 89.6 & $49.9 \pm 0.1$ \\
403	200\% & 3{,}470 & 94.2 & $50.0 \pm 0.0$ \\
404	800\% & 13{,}880 & ${\sim}97.7$ & $51.0 \pm 1.1$ \\
405	\midrule
406	Always-det & --- & --- & 50.0 \\
407	\bottomrule
408	\end{tabular}
409	\caption{Data scaling ablation: episode-level balanced accuracy across training set sizes (25\%--800\% of original, $32{\times}$ range). Internal recall $= 0.0$ at all scales (complete majority-class collapse). Det\%: fraction of deterministic-preferred labels in training data. The 50\% scale is a single seed; all others report mean$\pm$std across seeds.}
410	\label{tab:data-scaling}
411	\end{table}
412	
413	All scales hover at ${\sim}50\%$ episode-level balanced accuracy (equivalent to the always-deterministic baseline), with no monotonic improvement as data increases. Augmentation-based scaling provides no improvement at any scale; however, episode-level minority-class diversity remains a potential confound that cannot be resolved without collecting more internal-preferred episodes. The ground-truth internal-preferred rate (9/245 $= 3.7\%$) means collecting 50 internal-preferred episodes would require approximately 1{,}350 paired episodes at current environment dynamics, a $5.5{\times}$ expansion with diminishing return on a $9.6\%$ signal. The failure points to a limitation of the current data distribution: when DAF $= 90.4\%$ and all task types are deterministic-majority (86:9 label ratio), the episode-level routing problem is trivially solved by always choosing deterministic, leaving no learnable signal for a step-level router to exploit.
414	
415	Augmentation disproportionately increases the majority (deterministic) class: Det\% rises from 89.6\% at 100\% to 94.2\% at 200\% and ${\sim}97.7\%$ at 800\%. However, the complete collapse to majority-class prediction (internal recall $= 0.0$) occurs even at the smallest unaugmented scale (25\%, ${\sim}90\%$ det); this is not an augmentation artifact. Balanced accuracy corrects for class imbalance by averaging per-class recall, so the metric itself is not biased by the skew.
416	
417	Decomposition metrics are stable under bootstrap resampling (1{,}000 resamples of the 245-episode dataset): DAF $= 90.6\% \pm 4.2\%$ (95\% CI $[81.6\%, 98.8\%]$); Pearson $r = 0.975 \pm 0.011$ (95\% CI $[0.952, 0.995]$). The death avoidance dominance finding is robust to both resampling and split perturbation.
418	
419	\paragraph{Per-task-type evaluation breakdown.} To test whether the router learns transferable routing strategies or merely task-type classification, we evaluate existing checkpoints (8 seeds) separately on each of the 11 task types. Of the 11 task types, 7 have \emph{all-deterministic} labels (no internal-preferred episodes exist), making balanced accuracy undefined; the router has nothing to learn beyond the trivial always-deterministic default. For the remaining 4 task types where both classes are present, balanced accuracy ranges from 50.0\% to 73.0\%, but this apparent signal does not indicate cross-task-type routing transfer: the router is effectively classifying task types (which correlate with death risk) rather than extracting a generalizable routing strategy. This complements the data scaling ablation: routing signal does not transfer across task types because the signal \emph{is} the task type, i.e., whether a given task carries death risk. The 4B capacity scaling result (Appendix~\ref{app:ablations}) suggests capacity is one factor, but even 4B's $59.0\%$ episode-level accuracy does not demonstrate cross-task-type transfer.
420	
421	\section{Penalty Sensitivity Analysis}
422	\label{app:penalty}
423	
424	\begin{table}[h]
425	\centering
426	\small
427	\begin{tabular}{@{}rrr@{}}
428	\toprule
429	$P$ & DAF($P$) & 95\% CI \\
430	\midrule
431	0 & 7.5\% & [$-36.7$, $83.1$] \\
432	10 & 50.4\% & [$19.8$, $94.5$] \\
433	25 & 70.8\% & [$48.5$, $97.1$] \\
434	50 & 82.6\% & [$67.6$, $98.4$] \\
435	100\textsuperscript{*} & 90.4\% & [$81.5$, $99.1$] \\
436	200 & 95.0\% & [$90.0$, $99.5$] \\
437	500 & 97.9\% & [$95.8$, $99.8$] \\
438	\bottomrule
439	\end{tabular}
440	\caption{Sensitivity of DAF to death penalty magnitude $P$. DAF$(P) = 1 - \Delta_{\text{nd}} / \Delta_{\text{full}}(P)$, where $\Delta_{\text{full}}(P) \approx \delta \cdot P + \Delta_{\text{nd}}$, $\delta = 0.2653$ is the death-rate differential, and $\Delta_{\text{nd}} = 2.84$ (strict neither-died filtering). Bootstrap 95\% CIs from 1{,}000 resamples. \textsuperscript{*}Default setting.}
441	\label{tab:penalty-sensitivity}
442	\end{table}
443	
444	The non-death score gap $\Delta_{\text{nd}} = 2.84$ is invariant across penalty levels; it depends only on surviving-episode performance, not on $P$. As $P$ increases, $\Delta_{\text{full}}$ grows ($16.33$ at $P{=}50$, $29.60$ at $P{=}100$, $56.13$ at $P{=}200$) while $\Delta_{\text{nd}}$ remains fixed, mechanically increasing DAF.
445	
446	\paragraph{Mechanism boundary: death specificity.}
447	The $r = 0.97$ correlation between per-task death-rate differential and $\Delta_{\text{full}}$ is specific to catastrophic death (score $= -100$). Broader failure definitions dissolve the correlation entirely: defining ``failure'' as any non-positive score ($T{=}0$) yields $r = -0.13$ ($p = 0.70$), because non-death episodes show near-zero performance differential between strategies ($\Delta_{\text{nd}} = 2.84$). Table~\ref{tab:penalty-correlation} quantifies this specificity across penalty magnitudes.
448	
449	\begin{table}[h]
450	\centering
451	\small
452	\begin{tabular}{@{}rccl@{}}
453	\toprule
454	$P$ & $r$ & $p$ & Sig.\ ($\alpha{=}0.05$) \\
455	\midrule
456	10 & $-0.08$ & $0.813$ & No \\
457	25 & $0.51$ & $0.108$ & No \\
458	50 & $0.86$ & $0.0006$ & Yes \\
459	100\textsuperscript{*} & $0.97$ & $8 \times 10^{-7}$ & Yes \\
460	200 & $0.99$ & $1 \times 10^{-9}$ & Yes \\
461	\bottomrule
462	\end{tabular}
463	\caption{Pearson $r$ between per-task death-rate differential and $\Delta_{\text{full}}(P)$ across penalty magnitudes. The correlation is non-significant at low penalties and emerges at $P \geq 50$, which reflects the transition from non-death-dominated to death-dominated score gaps. \textsuperscript{*}Default ScienceWorld setting.}
464	\label{tab:penalty-correlation}
465	\end{table}
466	
467	This sharpens our central finding: death is not merely the dominant component of routing signal; it is effectively the \emph{only} component that generates differential routing signal in ScienceWorld. At low penalties, the death contribution is small and $\Delta_{\text{full}}$ reduces to $\Delta_{\text{nd}} \approx 2.84$, which is near-uniform across task types ($\text{mean non-death gap} = -1.19$ excluding the \texttt{find-non-living-thing} outlier); consequently, death-rate differential has no predictive power. As $P$ increases, the death term dominates $\Delta_{\text{full}}$, and the correlation sharpens because death rates \emph{are} the performance gap. The DAF values in Table~\ref{tab:penalty-sensitivity} increase monotonically with $P$, but this is a mathematical consequence of the decomposition ($\text{DAF} = \delta P / (\delta P + \Delta_{\text{nd}})$), not evidence of mechanism robustness.
468	
469	\section{Cross-Environment Details}
470	\label{app:cross-env-details}
471	
472	Figure~\ref{fig:signal-reversal} and Table~\ref{tab:cross-env} summarize the label distributions across all three environments.
473	
474	\begin{figure}[h]
475	\centering
476	\includegraphics[width=\columnwidth]{figures/signal_reversal.pdf}
477	\caption{Cross-environment label distributions. ScienceWorld and ALFWorld both show deterministic preference, but through different mechanisms: death avoidance (ScienceWorld) vs.\ information asymmetry from admissible-action access (ALFWorld). MATH shows balanced labels, confirming no routing signal without catastrophic failure.}
478	\label{fig:signal-reversal}
479	\end{figure}
480	
481	\begin{table}[h]
482	\centering
483	\small
484	\resizebox{\columnwidth}{!}{%
485	\begin{tabular}{@{}lccccc@{}}
486	\toprule
487	Environment & $N$ & Det\% & Int\% & NoPref\% & Death? \\
488	\midrule
489	ScienceWorld & 245 & 35.1 & 3.7 & 61.2 & Yes ($-100$) \\
490	MATH & 795 & 12.0 & 13.5 & 74.6 & No \\
491	ALFWorld & 135 & 25.9 & 1.5 & 72.6 & No\textsuperscript{$\dagger$} \\
492	\bottomrule
493	\end{tabular}}
494	\caption{Cross-environment label distribution. ``Deterministic'' denotes qualitatively different computation modes: ScienceWorld = oracle simulator with ground-truth state; MATH = Python code interpreter; ALFWorld = admissible-action enumeration. $\dagger$\,ALFWorld's deterministic advantage stems from information asymmetry, not death avoidance.}
495	\label{tab:cross-env}
496	\end{table}
497	
498	\section{Cross-Model Verification}
499	\label{app:cross-model}
500	
501	We replicate the counterfactual analysis with Llama-3.1-8B-Instruct across all 11 task types ($N{=}220$ episode pairs, 20 per type; Table~\ref{tab:cross-model-detail}).
502	The internal strategy dies in $41.4\%$ of episodes versus $11.4\%$ for deterministic (death-rate differential $+30.0$~pp), with 83 deterministic-preferred, 3 internal-preferred (1.4\%, all death-asymmetry reversals), and 134 no-preference labels.
503	Both models exhibit nearly identical internal vulnerability (${\sim}$42\%: Qwen $42.9\%$, Llama $41.4\%$), confirming that death-prone failure is structurally determined. The differential magnitude varies ($+26.5$~pp Qwen, $+30.0$~pp Llama) because deterministic strategy safety is model-dependent ($16.3\%$ vs.\ $11.4\%$), but directional consistency is 100\% (10/10 death-prone tasks in both models).
504	\texttt{identify-life-stages-1} shows cross-model precision matching ($55\%$/$10\%$/$+45$~pp in both models).
505	\texttt{find-non-living-thing} shows zero deaths in both models, consistent with its majority-class answer distribution.
506	
507	\begin{table}[h]
508	\centering
509	\small
510	\begin{tabular}{@{}lrrrl@{}}
511	\toprule
512	Task & Int\% & Det\% & $\Delta$\,pp & D / I / N \\
513	\midrule
514	identify-life-stages-1 & 55 & 10 & +45 & 9 / 0 / 11 \\
515	freeze & 45 & 0 & +45 & 9 / 0 / 11 \\
516	grow-fruit & 45 & 5 & +40 & 8 / 0 / 12 \\
517	identify-life-stages-2 & 45 & 5 & +40 & 8 / 0 / 12 \\
518	measure-melting-point & 50 & 15 & +35 & 9 / 0 / 11 \\
519	lifespan-longest & 35 & 5 & +30 & 7 / 1 / 12 \\
520	lifespan-l-then-s & 50 & 20 & +30 & 6 / 0 / 14 \\
521	chemistry-mix & 45 & 20 & +25 & 5 / 0 / 15 \\
522	inclined-plane & 45 & 20 & +25 & 6 / 0 / 14 \\
523	find-animal & 40 & 25 & +15 & 6 / 2 / 12 \\
524	find-non-living-thing & 0 & 0 & 0 & 10 / 0 / 10 \\
525	\midrule
526	\textbf{Aggregate} & \textbf{41.4} & \textbf{11.4} & \textbf{+30.0} & \textbf{83 / 3 / 134} \\
527	\bottomrule
528	\end{tabular}
529	\caption{Per-task Llama-3.1-8B cross-model replication ($N{=}20$ per task). D/I/N: deterministic-preferred / internal-preferred / no-preference. Sorted by $\Delta$ DR descending.}
530	\label{tab:cross-model-detail}
531	\end{table}
532	
533	\section{Failure Mode Analysis}
534	\label{app:failure-modes}
535	
536	All 105 internal-strategy deaths (100\%) are triggered by the same action pattern: \texttt{focus on [object]}. In ScienceWorld, \texttt{focus on} is the answer-submission action (equivalent to ``this is my final answer''); the LLM agent systematically misuses it as a general interaction or exploration command, and applies it to irrelevant targets (rooms, doors, inventory items). Each such execution submits an incorrect answer and triggers the $-100$ death penalty. Within death episodes, both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40 for deterministic) reflects how often each strategy enters catastrophic states, not different action selection within those states.
537	
538	Manual inspection identifies four failure categories: (A) no task awareness, where the agent executes \texttt{focus on} without reading the task; (B) task-aware but lacking action grounding, where the agent correctly identifies the objective but cannot map it to valid action primitives; (D) genuine attempts with execution failure; and (E) initial progress wasted by early errors. Category B dominates: agents demonstrate task comprehension but systematically fail to translate it into correct ScienceWorld actions. This taxonomy was produced by a single annotator; no inter-annotator agreement was computed. The categories are intended as qualitative illustrations, not as formal labels with reliability guarantees.
539	\label{tab:death-taxonomy}
540	
541	\paragraph{Representative examples.}
542	\emph{Category A} (no task awareness): In a \texttt{chemistry-mix} episode, the agent immediately executes \texttt{focus on kitchen}, \texttt{focus on door}, \texttt{focus on inventory} without reading the task, dying on the first \texttt{focus on} call. \emph{Category B} (comprehension without grounding): In a \texttt{lifespan-longest-lived} episode, the agent correctly identifies that it must compare animal lifespans and reasons about which animal lives longest, but then executes \texttt{focus on oak tree} (a non-animal object in the room) instead of navigating to find the target animal, triggering death.
543	
544	\paragraph{Action distribution analysis.}
545	Figure~\ref{fig:death-action-dist} shows the action distribution in death versus non-death episodes for the internal strategy; both are dominated by \texttt{connect} actions, with \texttt{focus on} moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$). Crucially, Figure~\ref{fig:death-comparison} reveals that within death episodes, internal and deterministic strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$). The survival gap (105 vs.\ 40 deaths) therefore reflects how often each strategy enters catastrophic states, not how it behaves within those states. Among fatal \texttt{focus on} targets, \texttt{workshop} remains the most frequent (20.0\%), followed by \texttt{inventory} (17.1\%) and \texttt{kitchen} (10.5\%), indicating a systematic object bias rather than random exploration. Figure~\ref{fig:death-timeline} visualizes the temporal pattern: agents execute long sequences of \texttt{connect} actions before a terminal \texttt{focus on} triggers death, typically in the final 1--3 steps.
546	
547	\begin{figure}[h]
548	\centering
549	\includegraphics[width=\columnwidth]{figures/death_action_distribution.pdf}
550	\caption{Action distribution for the internal (LLM) strategy in death ($n{=}105$) vs.\ non-death ($n{=}140$) episodes. Left: full distribution (both dominated by \texttt{connect}). Right: non-\texttt{connect} actions zoomed. \texttt{focus on} is moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$), while non-death episodes show higher rates of observation and object interaction.}
551	\label{fig:death-action-dist}
552	\end{figure}
553	
554	\begin{figure}[h]
555	\centering
556	\includegraphics[width=\columnwidth]{figures/death_action_timeline.pdf}
557	\caption{Step-by-step action sequences for 6 representative death episodes. The fatal \texttt{focus on} action (marked with arrow) consistently appears in the final steps after long \texttt{connect} sequences, and illustrates the ``connect loop $\to$ fatal focus'' pattern. Examples are drawn from the full 30-task dataset for task-type diversity; the pattern is identical in the 11-task analysis subset.}
558	\label{fig:death-timeline}
559	\end{figure}
560	
561	\begin{figure}[h]
562	\centering
563	\includegraphics[width=\columnwidth]{figures/death_action_comparison.pdf}
564	\caption{Non-\texttt{connect} action distribution comparison between internal (left) and deterministic (right) strategies. Within death episodes, both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not different action selection within those states.}
565	\label{fig:death-comparison}
566	\end{figure}
567	
568	\section{Grounding Ablation}
569	\label{app:grounding-ablation}
570	
571	We test whether directly intervening on the dominant death action (\texttt{focus on}) eliminates death vulnerability on the 10 death-prone tasks (baseline 48.0\%, $n{=}200$).
572	
573	\paragraph{Prompt warning.} Adding an explicit system prompt (``use \texttt{focus on} only for final answers'') reduces aggregate death rate to 37.0\% ($\Delta = -11$~pp). Both identification tasks exhibit ironic effects (\texttt{identify-life-stages-1}: 35\%$\to$50\%; \texttt{identify-life-stages-2}: 25\%$\to$70\%), where explicit mention of the dangerous action may have increased its salience.
574	
575	\paragraph{Action-space filtering.} Blocking \texttt{focus on} during the exploration phase yields 379 blocks across 200 episodes with zero leaks and zero passthroughs (the agent never persisted in retrying blocked actions), reducing death rate to 29.0\% ($\Delta = -19$~pp). The zero-passthrough rate suggests \texttt{focus on} use is a shallow behavioral pattern rather than a deliberate strategy.
576	
577	\paragraph{Per-task variation.} Under filtering, \texttt{identify-life-stages} and \texttt{inclined-plane} approach deterministic-level safety (${\sim}$15--20\% DR), while \texttt{chemistry-mix} and \texttt{find-animal} remain at 35--40\%. Residual deaths occur during the answer-submission window, where the filter is inactive and agents submit \texttt{focus on} to incorrect objects.
578	
579	\section{Ablation Studies}
580	\label{app:ablations}
581	
582	\paragraph{Capacity scaling.} We scale the implicit router from Qwen3-0.6B to Qwen3-4B and evaluate at both step and episode level (Table~\ref{tab:capacity}).
583	
584	\begin{table}[h]
585	\centering
586	\small
587	\begin{tabular}{@{}lcc@{}}
588	\toprule
589	Model & Step Bal.\ Acc.\ (\%) & Ep.\ Bal.\ Acc.\ (\%) \\
590	\midrule
591	Qwen3-0.6B & $56.4 \pm 3.5$ & $50.7 \pm 2.6$ \\
592	Qwen3-1.7B & $58.2 \pm 4.0$ & $43.1 \pm 1.0$ \\
593	Qwen3-4B & $59.2 \pm 3.5$ & $\mathbf{59.0 \pm 1.9}$ \\
594	\midrule
595	Always-det & 50.0 & 50.0 \\
596	\bottomrule
597	\end{tabular}
598	\caption{Capacity scaling: step-level and episode-level balanced accuracy (4 seeds, identical configuration across all scales). Step-level accuracy is flat ($56$--$59\%$, within seed variance). At episode level, only 4B breaks the random baseline ($59.0\%$, $p < 0.005$).}
599	\label{tab:capacity}
600	\end{table}
601	
602	Step-level balanced accuracy is flat across scales ($56$--$59\%$, within seed variance); step-level discrimination is not capacity-sensitive. At episode level, only 4B breaks the random baseline ($59.0 \pm 1.9\%$, $p < 0.005$); 0.6B and 1.7B remain at or below chance. The 1.7B model's below-chance episode-level accuracy ($43.1\%$) may reflect overfitting to spurious step-level correlations that anti-correlate with episode outcomes; without per-class confusion matrices at this scale, this remains a hypothesis. The dominant explanation across scales is that death avoidance constitutes a task-type-level binary signal that a step-level router cannot exploit efficiently.
603	
604	\paragraph{Generative router.} A generative routing model trained with explicit routing labels achieves balanced accuracy of 46.7\%, confirming that the routing bottleneck is signal-limited, not architecture-limited.
605	
606	\paragraph{Leave-one-task-type-out routing.} Under leave-one-task-type-out evaluation, blind routing collapses to always-deterministic (balanced accuracy 50.0\%); a keyword-based variant achieves 62.9\% only through task-identity leakage, not genuine routing signal.
607	
608	\paragraph{Reasoning depth.} An ablation comparing chain-of-thought reasoning against direct-answer generation on 6 task types ($n{=}120$ episodes per condition, 6 tasks $\times$ 20 episodes per task) found no significant difference (Mann--Whitney $p > 0.26$, $|d| \leq 0.31$) and near-identical death rates (41.8\% vs.\ 42.5\%); reasoning depth does not meaningfully alter internal-mode outcomes.
609	
610	\section{Threshold Routing Analysis}
611	\label{sec:threshold-routing}
612	
613	Given per-task death risk knowledge, we test whether a simple threshold routing strategy can outperform always-deterministic. For each threshold $t \in [0, 1]$, we route to internal if the per-task internal death rate $\leq t$, otherwise to deterministic, and sweep all thresholds to find the optimal.
614	
615	\begin{table}[h]
616	\centering
617	\small
618	\begin{tabular}{lccc}
619	\toprule
620	Strategy & Mean Score & Death Rate & $\Delta$ vs Det \\
621	\midrule
622	Always-det & $-9.47$ & $0.163$ & $0.00$ \\
623	Optimal threshold ($t{=}0$) & $-11.03$ & $0.155$ & $-1.56$ \\
624	Always-internal & $-39.07$ & $0.429$ & $-29.60$ \\
625	\bottomrule
626	\end{tabular}
627	\caption{Death-risk threshold routing analysis on 245 episodes. The optimal threshold routes only \texttt{find-non-living-thing} (the sole zero-death task) to internal, with all other tasks routed to deterministic. Bootstrap 95\% CI for the difference: $[-8.87, +5.92]$.}
628	\label{tab:threshold-routing}
629	\end{table}
630	
631	Even with perfect per-task death risk knowledge, threshold routing cannot outperform always-deterministic. The sole zero-death task achieves higher scores under deterministic (+28.5) than internal (+18.9), leaving no room for a beneficial mixed strategy.
632	
633	\section{Practitioner Decision Framework}
634	\label{app:decision-framework}
635	
636	Given a new interactive environment, the following three-stage procedure diagnoses whether learned routing adds value over a fixed deterministic strategy.
637	
638	\paragraph{Stage 1: Pilot collection (${\sim}$50 episodes).}
639	Run pure-internal and pure-deterministic strategies on a representative sample (${\sim}$50 episode pairs). Compute the death-rate differential $\Delta\text{DR} = \text{DR}_{\text{int}} - \text{DR}_{\text{det}}$.
640	
641	\paragraph{Stage 2: Death dominance check.}
642	If $\Delta\text{DR} > 15$~pp, death asymmetry is likely the dominant routing signal. Compute the death-label fraction $f_{\text{death}}$: the proportion of non-tie routing labels where exactly one strategy dies.
643	
644	\paragraph{Stage 3: Decision.}
645	If $f_{\text{death}} > 75\%$, the routing signal is death-dominated; a fixed deterministic strategy will match or exceed any learned router. If $f_{\text{death}} < 50\%$, diverse routing signals may justify a learned router. Between 50\%--75\%, collect additional episodes to reduce estimation noise before committing to router development.
646	
647	\paragraph{Retrospective validation.}
648	All four experimental conditions in this paper are correctly classified:
649	
650	\begin{table}[h]
651	\centering
652	\small
653	\begin{tabular}{@{}lrrll@{}}
654	\toprule
655	Condition & $\Delta$DR & $f_{\text{death}}$ & Prediction & Actual \\
656	\midrule
657	Qwen-7B & +26.5 & 78.9\% & det-fixed & det wins \\
658	Llama-8B & +30.0 & $>$75\% & det-fixed & det wins \\
659	Qwen-72B & +27.8 & $>$75\% & det-fixed & det wins \\
660	MATH & +0.5 & 0\% & router viable & no signal \\
661	\bottomrule
662	\end{tabular}
663	\caption{Retrospective validation of the decision framework. All four conditions are correctly classified (4/4).}
664	\label{tab:decision-framework}
665	\end{table}
666	
667	The framework also predicts the inverted-U relationship between capability and death risk: below ${\sim}$0.5B parameters, agents fail to reach dangerous states at all (13.3\% death rate in a 15-episode pilot), so $\Delta\text{DR}$ is low and the framework would not recommend fixed-deterministic. Above ${\sim}$7B, agents are capable enough to enter catastrophic states but not capable enough to avoid them, producing high $\Delta\text{DR}$.
668	
669	\paragraph{Threshold calibration.} The thresholds above (15~pp, 75\%, 50\%) are illustrative, derived from a single-environment analysis. Practitioners should calibrate these boundaries for their specific environment and reward structure.
670	
671	\input{responsibleNLPchecklist}
672	
673	\end{document}
674	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6eed4b47-eb81-4d72-b96e-8c4545f563cd",
  "isSidechain": true,
  "promptId": "44bc2991-8df5-496d-9b2e-d19feb4a03d2",
  "agentId": "a13f9f1b8ad8fec76",
  "type": "user",
  "uuid": "8ac820fd-5b9b-4ea0-8fcf-d31cefab31a0",
  "sourceToolAssistantUUID": "6eed4b47-eb81-4d72-b96e-8c4545f563cd",
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

_source line 23 · 2026-05-19T18:17:39.455Z_

Now I have all the paper content. Let me systematically check each item.

## Check 1: Table 1 (Baselines, Tab. `tab:baselines`)

**Table values** (experiments.tex lines 93-98):
- Always-Internal: -39.07, Death% 42.9
- Always-Deterministic: -9.47, Death% 16.3
- Random: -22.38, Death% 27.8
- Oracle: -6.58, Death% 14.3
- Trained Router: -10.70, Death% 17.6

**Text in §3.5** (experiments.tex line 105):
> "Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points. The oracle improves only to $-6.58$, with 96.3\% of decisions matching always-deterministic"

Checks:
- Always-det = -9.47: **MATCH** (table line 94, text line 105)
- Always-int = -39.07: **MATCH** (table line 93, text line 105)
- Oracle = -6.58: **MATCH** (table line 96, text line 105)
- Improvement from always-det to oracle: -6.58 - (-9.47) = 2.89 points. Text in §3.6 (line 110) says "oracle margin (2.89 points)": **MATCH**
- 96.3% oracle matches always-det: text line 105 says "96.3%": **MATCH**
- 29.60 points gap: -9.47 - (-39.07) = 29.60: **MATCH** (also matches §3.1 line 17 "$\Delta_{\text{full}} = +29.60$")

## Check 2: Table 2 (Agent Improvement, Tab. `tab:agent-improvement`)

**Table values** (experiments.tex lines 46-53):
- Single-trial baseline: 42.9%, N=245
- Reflexion (3x): 31.4%, N=220
- Qwen2.5-72B (10x): 30.6%, N=255
- Deterministic baseline: 16.3%, N=245
- Death-prone baseline: 48.0%, N=200
- Retry (5x): 43.5%, N=200

**Text in §3.3** (experiments.tex line 60):
> "Reflexion reduces death to 31.4% across all 11 tasks"
> "Scaling to Qwen2.5-72B...reduces death rate to $30.6\%$"
> "The 72B deterministic strategy achieves $2.75\%$ death rate ($\Delta\text{DR} = +27.8$~pp), and $\Delta_{\text{nd}} = +2.28$, yielding DAF $= 92.4\%$"

Checks:
- Single-trial 42.9%: **MATCH** (table line 46, text §3.1 line 20 "internal strategy dies in 42.9%")
- Reflexion 3x = 31.4%: **MATCH** (table line 47, text line 60)
- 72B = 30.6%: **MATCH** (table line 48, text line 60)
- Deterministic = 16.3%: **MATCH** (table line 49, text §3.1 line 20 "16.3% for deterministic")
- 72B det DR = 2.75%: mentioned in text line 60: **MATCH** (not in table, but stated in text)
- 72B ΔDR = +27.8pp: 30.6% - 2.75% = 27.85pp ≈ +27.8pp: **MATCH**
- 72B Δ_nd = +2.28: mentioned in text line 60: **consistent internally**
- 72B DAF = 92.4%: text line 60: **MATCH**

**Cross-check with discussion.tex** (line 8):
> "72B DAF${}= 92.4\%$; Reflexion DAF${}>100\%$ with $\Delta_{\text{nd}} = -0.47$"

This matches experiments.tex line 60: "Under Reflexion ($N{=}3$, matched-episode analysis), $\Delta_{\text{nd}} = -0.47$, yielding DAF $> 100\%$": **MATCH**

**Cross-check Abstract** (abstract.tex line 2): mentions "DAF reaches 90.4% at $P{=}100$" — this is the 7B number, not 72B. **CORRECT** (different conditions).

## Check 3: Figure 1 (Scatter plot) — structural consequence caveat

**Figure 1 caption** (experiments.tex lines 11):
> "Since $\Delta_{\text{full}} \approx \delta P + \Delta_{\text{nd}}$ with $P$ constant, $r \to 1$ as DAF $\to 1$; the near-perfect correlation is a structural consequence of death dominance, not an independent finding"

**PRESENT and CORRECT.** The R18/m1 requirement for a "structural consequence" caveat is satisfied in the caption.

Also reinforced in text (line 20):
> "The near-perfect correlation is therefore a mathematical consequence of death dominance, not an independent empirical finding. We retain it as an internal consistency check."

**MATCH** — caveat is present in both caption and text.

## Check 4: Figure 2 (Dose-response)

**Figure 2 caption** (experiments.tex lines 68):
> "Death rate as a function of trial count ($N$) for Retry and Reflexion on 10 death-prone tasks ($n{=}200$). Retry (blue) is nearly flat; Reflexion (red) drops steeply through $N{=}3$ then plateaus. Horizontal lines: 72B scaling baseline ($30.6\%$, all 11 tasks) and deterministic baseline ($16.3\%$)."

**Text §3.3 paragraph "Dose-response analysis"** (line 63):
> "We extend both interventions to $N{=}5$ trials on death-prone tasks ($n{=}200$)"
> "Reflexion drops steeply to $34.0\%$ at $N{=}3$ ($\Delta = -13.5$~pp, $z = 2.75$, $p = 0.003$)"
> "With $n{=}200$ paired episodes, the minimum detectable effect is ${\sim}8$~pp"

Checks:
- N=200 per group: **MATCH** (caption says $n{=}200$, text says $n{=}200$)
- MDE ~8pp: mentioned in line 63: **PRESENT**
- p-value: text says "p = 0.003" for the N=1→3 decline. The user asked about "p < 0.005" — text says "p = 0.003" which is indeed < 0.005. In Appendix P (line 598), "only 4B breaks the random baseline ($59.0 \pm 1.9\%$, $p < 0.005$)" — this is a different claim (router capacity). The dose-response text itself says p=0.003 specifically. **CONSISTENT**.

## Check 5: Appendix cross-references

**Appendix K (Penalty Sensitivity, line 435):** DAF at P=100: 90.4%, CI [81.5, 99.1]
**Main text §3.1 (line 17):** "DAF $= 90.4\%$ at $P{=}100$...95\% CI: $[81.6\%, 98.8\%]$"

**DISCREPANCY FOUND:** 
- Main text: 95% CI = [81.6%, 98.8%]
- Appendix K table: 95% CI = [81.5, 99.1]

These CIs don't match. Let me also check line 26: "Non-clustered episode-level bootstrap ($B = 10{,}000$) yields 95\% CI $[81.6\%, 98.8\%]$ for the death-avoidance label fraction"

Wait — line 26 says the CI [81.6%, 98.8%] is for the "death-avoidance label fraction" (78.9%), while line 17 says "95\% CI: $[81.6\%, 98.8\%]$" in the context of DAF. Let me re-read line 17 more carefully:

> "DAF $= 90.4\%$ at $P{=}100$ ($\Delta_{\text{full}} = +29.60$, $\Delta_{\text{nd}} = +2.84$; 95\% CI: $[81.6\%, 98.8\%]$, episode-level bootstrap, $B{=}10{,}000$)"

So line 17 applies CI [81.6%, 98.8%] to DAF. But Appendix K (line 435) gives DAF at P=100 CI = [81.5, 99.1]. And line 26 applies the same CI [81.6%, 98.8%] to the death-avoidance label fraction. Also, Appendix J (line 417) says "DAF $= 90.6\% \pm 4.2\%$ (95\% CI $[81.6\%, 98.8\%]$)". 

So there's a discrepancy between Appendix K's table (CI [81.5, 99.1]) and everywhere else (CI [81.6%, 98.8%]). This could be because Appendix K uses 1,000 resamples while the main text uses 10,000 resamples, or different filtering. The Appendix K caption says "Bootstrap 95\% CIs from 1{,}000 resamples" while main text says "$B{=}10{,}000$". This explains the minor difference but is still an inconsistency in the reported numbers.

**Per-task table (Appendix C, line 141):**
- All 11 tasks: Δ_full = +29.60, D%_int = 42.9, D%_det = 16.3, D/I/N = 86/9/150
- §3.1 text (line 20): "86 are det_preferred, 9 internal_preferred, and 150 no_preference": **MATCH**
- §3.1 text (line 17): "Δ_full = +29.60": **MATCH**

**Cross-model (Appendix M) vs §3.2:**
- Appendix M (line 502): internal 41.4%, deterministic 11.4%, DR differential +30.0pp, 83 det-pref, 3 int-pref, 134 no-pref
- §3.2 (line 31): "internal death rate $41.4\%$ vs.\ deterministic $11.4\%$ (death-rate differential $+30.0$~pp), DAF $= 88.2\%$...83 deterministic-preferred, 3 internal-preferred...134 no-preference labels"
- **MATCH**

**72B Appendix vs §3.3:**
The 72B numbers are only in §3.3 (line 60) and not in a separate appendix table. But Discussion (line 8) also says "72B DAF${}= 92.4\%$": **MATCH**.

## Check 6: Abstract and Introduction numbers

**Abstract** (abstract.tex line 2):
- "78.9% of non-tie routing labels": matches §3.1 (line 15: "75 (78.9%)")
- "DAF reaches 90.4% at P=100": matches §3.1 (line 17)
- "Llama-3.1-8B, DAF=88.2%": matches §3.2 (line 31)

**Introduction** (introduction.tex):
- Line 8: "78.9% of non-tie routing labels arise from death asymmetry (75 of 95)": **MATCH** with §3.1
- Line 8: "DAF reaches $90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$)": **MATCH** with §3.1 (same CI issue as above)
- Line 8: "$\Delta_{\text{nd}} = +2.84$": **MATCH** with §3.1
- Line 12: "Llama-3.1-8B replication ($N{=}220$) confirms death dominance across model families (direction consistency 10/10)": matches §3.2
- Line 12: "with ${\geq}$12~pp residual gaps": Let me check. The lowest residual gap: 72B has 30.6% - 16.3% = 14.3pp (but 72B det is 2.75%, so 30.6 - 2.75 = 27.85pp at 72B scale). Reflexion has 31.4% - 16.3% = 15.1pp gap. The intro says "≥12pp residual gaps" — the grounding ablation reduces to 29.0% vs baseline det 16.3%, gap = 12.7pp. Actually the text says "none closes the gap to deterministic safety, with ≥12pp residual gaps" — checking: Reflexion=31.4-16.3=15.1pp, 72B=30.6-16.3=14.3pp (but this uses 7B det baseline). Grounding ablation: 29.0% int vs maybe lower det? Let me check: grounding ablation (Appendix O, line 575) says "reducing death rate to 29.0%". That's compared to det baseline 16.3% (for 7B) = 12.7pp gap. So ≥12pp is correct. **MATCH**

**Introduction line 8**: "$r = 0.97$" — matches §3.1 line 20.

Now let me check one more potential issue. The Appendix D (line 192) says "Pearson $r = 0.9698$" and "Spearman rank correlation is $\rho = 0.986$". But Figure 1 caption (line 11) says "$r = 0.97$ (Spearman's $\rho = 0.975$)". 

**DISCREPANCY FOUND:**
- Appendix D (line 192): Spearman ρ = 0.986
- Figure 1 caption (line 11): Spearman's ρ = 0.975

These don't match. The Pearson r is consistent (0.97/0.9698 rounds to 0.97), but the Spearman ρ differs: 0.975 vs 0.986.

Let me also check the death-rate differential number:
- §3.2 (line 32): "the differential magnitude varies ($+26.5$~pp Qwen, $+30.0$~pp Llama)"
- Qwen: 42.9% - 16.3% = 26.6pp. Text says +26.5pp. 

**MINOR DISCREPANCY:** 42.9 - 16.3 = 26.6, but text says 26.5. This could be a rounding issue (if raw numbers are 42.86 - 16.33 = 26.53 ≈ 26.5). Borderline acceptable.

Let me also verify the "90.5% of non-tie oracle decisions" claim in §3.5 (line 105): "an always-deterministic lookup achieves 90.5% of non-tie oracle decisions". The oracle decisions: 86 det-preferred + 9 int-preferred = 95 non-tie. Always-det correctly captures 86/95 = 90.5%. **MATCH**.

**Conclusion** (conclusion.tex line 3):
- "78.9% of non-tie routing labels": **MATCH**
- "Llama-3.1-8B, DAF=88.2%": **MATCH**
- "200 GPU-hour router training": matches Ethics Statement (main.tex line 46): "approximately 200 GPU-hours": **MATCH**

**Limitations** (main.tex line 36):
- "DAF = 90.4%": **MATCH**
- line 38: "Reflexion reduces death rate from 42.9% to 31.4%": **MATCH** with §3.3

Let me double-check one more thing — the §3.5 line 105 says "96.3% of decisions matching always-deterministic". Oracle makes 86+9=95 non-tie decisions. Of these, 86 are det-preferred. 86/95 = 0.9053 = 90.5%. But it says "96.3%". Let me re-read:

> "The oracle improves only to $-6.58$, with 96.3\% of decisions matching always-deterministic"

This says 96.3% of **all** oracle decisions (including no-preference treated as det). Total episodes = 245. Oracle routes 150 no-pref + 86 det-pref to deterministic = 236. 236/245 = 96.3%. **MATCH** — the 96.3% counts all episodes where oracle would pick deterministic (no-pref defaults to det).

---

## Summary of Findings

### Confirmed Consistent:
1. **Table 1 numbers vs §3.5 text**: All match (Always-det -9.47, Always-int -39.07, Oracle -6.58, 29.60 gap, 96.3% oracle-det match, 2.89 oracle margin)
2. **Table 2 numbers vs §3.3 text**: All match (42.9%, 31.4%, 30.6%, 16.3%, 48.0%, 43.5%)
3. **72B specifics**: det DR=2.75%, ΔDR=+27.8pp, Δ_nd=+2.28, DAF=92.4% — consistent across §3.3 and Discussion
4. **Figure 1 caption**: Contains structural consequence caveat (R18/m1 satisfied)
5. **Figure 2**: N=200 per group confirmed, MDE ~8pp present, p=0.003 for N=1→3
6. **Per-task table**: Matches §3.1 (86/9/150, Δ_full=+29.60, 42.9%/16.3%)
7. **Cross-model (Appendix M)**: Matches §3.2 (41.4%/11.4%, +30.0pp, 83/3/134, DAF=88.2%)
8. **Abstract/Introduction/Conclusion**: All key numbers (78.9%, 90.4%, 88.2%, r=0.97) match experiments section

### Discrepancies Found:

**Discrepancy 1: DAF 95% CI mismatch**
- **experiments.tex line 17** (§3.1): CI = [81.6%, 98.8%] (B=10,000)
- **experiments.tex line 26** (§3.1): CI = [81.6%, 98.8%] (B=10,000) — for label fraction
- **introduction.tex line 8**: CI = [81.6%, 98.8%]
- **main.tex line 435** (Appendix K table): CI = [81.5, 99.1] (B=1,000)
- **main.tex line 417** (Appendix J): CI = [81.6%, 98.8%]

The Appendix K table reports [81.5, 99.1] while everywhere else says [81.6%, 98.8%]. This is likely due to different bootstrap sample sizes (1,000 vs 10,000), but the paper doesn't explain the discrepancy. The reader would expect these to be the same CI for the same quantity.

**Discrepancy 2: Spearman ρ value**
- **Figure 1 caption** (experiments.tex line 11): Spearman's ρ = 0.975
- **Appendix D** (main.tex line 192): Spearman rank correlation ρ = 0.986

These are reporting the same correlation (death rate differential vs Δ_full, n=11 tasks) but give different values: 0.975 vs 0.986.

**Discrepancy 3 (Minor): Qwen death-rate differential rounding**
- Computed from stated values: 42.9% - 16.3% = 26.6pp
- Text (§3.2, line 32): reports "+26.5 pp"

This is a 0.1pp rounding discrepancy — likely the underlying raw values round differently, but it's worth noting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ac820fd-5b9b-4ea0-8fcf-d31cefab31a0",
  "isSidechain": true,
  "agentId": "a13f9f1b8ad8fec76",
  "requestId": "req_011CbCPFLWF1i7dryMeP6pSU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6934cdd8-ca6f-4366-9e54-27ba58c12177",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_ae7c9c01",
  "sessionId": "6af3bb19-7b9e-4416-baf5-f01a654af672",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "lexical-churning-otter",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ejEJ3mU4yuj1bEWo7PjLE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20236,
      "cache_read_input_tokens": 42008,
      "output_tokens": 5219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20236
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5219,
          "cache_read_input_tokens": 42008,
          "cache_creation_input_tokens": 20236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20236,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---
