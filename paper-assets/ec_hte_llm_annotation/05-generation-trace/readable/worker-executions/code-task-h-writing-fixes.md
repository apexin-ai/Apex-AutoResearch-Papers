# code task h writing fixes

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 96
- **Recorded user turns:** 0
- **Tool calls:** 37
- **Original source:** `logs/workers/worker_code_task-h-writing-fixes_20260523T092318.log`
- **Structured JSON:** [`6de590c5d558c52a98ad.json`](../../sessions/6d/6de590c5d558c52a98ad.json)

## Before a recorded user message

96 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
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
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "41b53e8a-07aa-4e6c-b90e-feaa910a7761",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779541800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "27337621-4b8f-43bc-98fa-6db374e04339",
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the relevant files to understand the current state of the paper, then execute all 8 fixes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "3fbc05be-263b-45bc-a8b3-142cc9b4b2ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxbidNY9Li64EvqEmWDDgD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14179,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14179
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 5_

I'll start by reading all the relevant files in parallel to understand the current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "d7cff08b-f802-481d-829d-bad32b2bd7fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxbidNY9Li64EvqEmWDDgD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14179,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14179
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01EuLzEhjRgxvNHjauGmPVZX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "b09b7bda-1cdb-4c0d-b6a2-e3f13eb79ba3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxbidNY9Li64EvqEmWDDgD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14179,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14179
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-23T09:23:28.234Z_

<details><summary>↩ Tool result · `toolu_01EuLzEhjRgxvNHjauGmPVZX`</summary>

```text
1	\begin{abstract}
2	Proxy classifiers---including LLMs now widely used to replace human coders---exhibit misclassification rates that vary across subgroups by up to 5$\times$, yet standard practice corrects annotation error using a single pooled confusion matrix.
3	We show that this global correction introduces structured bias into subgroup-level treatment effect estimates; in our LLM annotation experiments, global correction worsens bias in 50\% of configurations, with amplification up to 5.9$\times$.
4	We derive an exact bias identity showing that this correction-induced bias factors into each subgroup's deviation from the pooled error rate times the treatment effect heterogeneity---a finite-population identity, not a bound.
5	The identity yields a diagnostic that flags harmful correction using only per-subgroup error rates, without estimating treatment effects: on subgroups with non-zero effect heterogeneity, the diagnostic achieves perfect separation (AUC $= 1.0$); the lower aggregate AUC on real LLM confusion matrices is driven by subgroups where correction is unnecessary.
6	We provide EC-HTE, the per-subgroup correction prescribed by the identity via hierarchical Bayes, reducing $|\text{bias}|$ by 7.4$\times$ under extreme heterogeneity with nominal coverage ($\geq$0.90); validated across 520 synthetic configurations, eight LLMs, and two NLP datasets, the advantage is conditional on sufficient error heterogeneity and expert budget.
7	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "7e71d4aa-77ce-4db8-a538-7ea533cc127e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nProxy classifiers---including LLMs now widely used to replace human coders---exhibit misclassification rates that vary across subgroups by up to 5$\\times$, yet standard practice corrects annotation error using a single pooled confusion matrix.\nWe show that this global correction introduces structured bias into subgroup-level treatment effect estimates; in our LLM annotation experiments, global correction worsens bias in 50\\% of configurations, with amplification up to 5.9$\\times$.\nWe derive an exact bias identity showing that this correction-induced bias factors into each subgroup's deviation from the pooled error rate times the treatment effect heterogeneity---a finite-population identity, not a bound.\nThe identity yields a diagnostic that flags harmful correction using only per-subgroup error rates, without estimating treatment effects: on subgroups with non-zero effect heterogeneity, the diagnostic achieves perfect separation (AUC $= 1.0$); the lower aggregate AUC on real LLM confusion matrices is driven by subgroups where correction is unnecessary.\nWe provide EC-HTE, the per-subgroup correction prescribed by the identity via hierarchical Bayes, reducing $|\\text{bias}|$ by 7.4$\\times$ under extreme heterogeneity with nominal coverage ($\\geq$0.90); validated across 520 synthetic configurations, eight LLMs, and two NLP datasets, the advantage is conditional on sufficient error heterogeneity and expert budget.\n\\end{abstract}",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01K8KEcdqfdhCHEb8gU28qL7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "ca2002ad-1ece-459f-b012-7b166ee395a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxbidNY9Li64EvqEmWDDgD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14179,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14179
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-23T09:23:28.719Z_

<details><summary>↩ Tool result · `toolu_01K8KEcdqfdhCHEb8gU28qL7`</summary>

```text
1	% Requires preamble: \usepackage{amsthm,amsmath,amssymb}
2	% and: \newtheorem{theorem}{Theorem}
3	%      \newtheorem{corollary}[theorem]{Corollary}
4	%      \newtheorem{proposition}[theorem]{Proposition}
5	
6	\section{Bias Decomposition: When Debiasing Hurts}
7	\label{sec:theory}
8	
9	We formalize the bias that global misclassification correction introduces when subgroup error rates are heterogeneous.
10	Consider estimating the conditional average treatment effect (CATE) $\tau(z) = \mathbb{E}[Y(1) - Y(0) \mid Z = z]$, where $Z \in \{0, 1\}$ is a binary effect modifier observed only through a noisy annotation $\hat{Z}$.
11	The population consists of $K$ subgroups $S \in \{1, \ldots, K\}$ with weights $w_s = P(S{=}s)$, each characterized by a $2 \times 2$ confusion matrix $C_s$ with symmetric error rate $\pi_s = P(\hat{Z} \neq Z \mid S{=}s)$.
12	Standard practice estimates a single confusion matrix $\bar{C} = \sum_s w_s C_s$ from expert annotations and applies its inverse uniformly to all observations, with pooled error rate $\bar{\pi} = \sum_s w_s \pi_s$.
13	We show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.
14	
15	We state five assumptions maintained throughout.
16	%
17	\begin{itemize}
18	\item[\textbf{(A1)}] \textit{Conditional independence:} misclassification depends only on the true label $Z$ and subgroup $S$, not on potential outcomes $Y(0), Y(1)$.
19	\item[\textbf{(A2)}] \textit{Symmetric misclassification:} $P(\hat{Z}{=}1 \mid Z{=}0, S{=}s) = P(\hat{Z}{=}0 \mid Z{=}1, S{=}s) = \pi_s$ for all $s$ (diagnostic only; see Remark~2).
20	\item[\textbf{(A3)}] \textit{Balanced effect modifier:} $P(Z{=}0) = P(Z{=}1) = 0.5$. This simplifies the exposition; we discuss relaxation below.
21	\item[\textbf{(A4)}] \textit{Non-degeneracy:} $\pi_s \neq 0.5$ for all $s$, ensuring each $C_s$ is invertible.
22	\item[\textbf{(A5)}] \textit{Homogeneous treatment effects across subgroups:} $\tau(z, s) = \tau(z)$ for all $s$, so $\Delta\tau = \tau(1) - \tau(0)$ is a scalar.
23	\end{itemize}
24	
25	Under (A2)--(A3), the Bayesian mixing matrix $M_s$ (entries $M_s[\hat{z}, z] = P(Z{=}z \mid \hat{Z}{=}\hat{z}, S{=}s)$) coincides with $C_s$.
26	The global mixing matrix is $M_{\text{global}} = \sum_s w_s M_s$.
27	
28	\begin{theorem}[Bias Decomposition Identity]
29	\label{thm:bias_identity}
30	Under \textnormal{(A1)--(A5)}, the bias of global correction in subgroup $s$ at effect-modifier level $z$ is
31	\begin{align}
32	\mathrm{bias}_{\mathrm{global}}(z{=}0, s) &= +\frac{\delta_s \cdot \Delta\tau}{1 - 2\bar{\pi}}, \label{eq:bias_z0} \\
33	\mathrm{bias}_{\mathrm{global}}(z{=}1, s) &= -\frac{\delta_s \cdot \Delta\tau}{1 - 2\bar{\pi}}, \label{eq:bias_z1}
34	\end{align}
35	where $\delta_s = \pi_s - \bar{\pi}$ is the subgroup deviation from the pooled error rate and $\Delta\tau = \tau(1) - \tau(0)$ is the CATE heterogeneity.
36	\end{theorem}
37	
38	Equations~\eqref{eq:bias_z0}--\eqref{eq:bias_z1} constitute an exact finite-population identity, not an asymptotic approximation or bound.
39	The bias factors into three interpretable components: $\delta_s$ captures how much subgroup $s$ deviates from the average misclassification rate, $\Delta\tau$ captures treatment effect heterogeneity across levels of $Z$, and $1/(1 - 2\bar{\pi})$ is an amplification factor from matrix inversion.
40	Bias vanishes when either source of variation is absent ($\delta_s = 0$ or $\Delta\tau = 0$), and arises only through their interaction.
41	Theorem~\ref{thm:bias_identity} implies that global correction trades one source of confounding for another: it removes attenuation from label noise but introduces a new bias from error-rate heterogeneity.
42	
43	\paragraph{Proof sketch.}
44	Global correction applies $M_{\text{global}}^{-1}$ to the subgroup-specific observed CATE $\tau_{\text{obs}}(\cdot, s) = M_s \cdot \tau_{\text{true}}$, yielding bias $(M_{\text{global}}^{-1} M_s - I) \cdot \tau_{\text{true}}$.
45	Direct computation shows $M_{\text{global}}^{-1} M_s - I = \frac{\delta_s}{1-2\bar{\pi}} \bigl[\begin{smallmatrix} -1 & 1 \\ 1 & -1 \end{smallmatrix}\bigr]$.
46	Applying this matrix to $[\tau(0),\, \tau(1)]^\top$ produces the product form.
47	The full derivation appears in Appendix~\ref{app:derivation}.
48	
49	\begin{remark}
50	Theorem~\ref{thm:bias_identity} does not require assumption~(A2).
51	For arbitrary asymmetric confusion matrices ($\mathrm{FPR}_s \neq \mathrm{FNR}_s$),
52	the product form $\mathrm{bias}(z, s) = \Delta\tau \cdot [B_s]_{z,1}$ holds exactly,
53	where $B_s = M_{\mathrm{global}}^{-1} M_s - I$, because $B_s \mathbf{1} = \mathbf{0}$
54	follows from stochasticity of $M_s$ and $M_{\mathrm{global}}$ alone.
55	Assumption~(A2) simplifies $[B_s]_{z,1}$ to the scalar
56	$\pm \delta_s / (1 - 2\bar{\pi})$ but is not necessary for the product structure.
57	Under asymmetric errors, the diagnostic (Proposition~\ref{prop:debiasing_hurts}) requires evaluating $[B_s]_{z,1}$ cell-by-cell rather than via a single scalar threshold; the AUC decreases from 0.86 to 0.82 (Appendix~\ref{app:asymmetric}), reflecting the additional complexity of cell-specific error rates.
58	For binary effect modifiers ($|\mathcal{Z}|{=}2$), the asymmetric score $|[B_s]_{z,1}|$ reduces to a monotone transform of the symmetric score $|\delta_s|/((1{-}2\bar{\pi})\pi_s)$, because column-stochastic $M$ forces $|B_s[0,1]|{=}|B_s[1,1]|$; practitioners may use the simpler symmetric formula without loss.
59	See Appendix~\ref{app:asymmetric} for the full derivation and empirical verification
60	($R^2 = 0.991$).
61	\end{remark}
62	
63	Assumption~(A5) simplifies exposition; the identity generalizes to subgroup-specific $\Delta\tau_s$ (Corollary~\ref{cor:a5_relaxation}, Appendix~\ref{app:a5_violation}).
64	EC-HTE's correction does not depend on (A5): each $\hat{C}_s^{-1}$ corrects the local misclassification structure regardless of whether $\Delta\tau$ varies; under both positive and negative $\Delta\tau_s$--$\delta_s$ correlation, EC-HTE maintains $\geq$93\% coverage while global correction degrades to 74--82\% (Appendix~\ref{app:a5_violation}).
65	
66	The identity extends to $K > 2$ subgroups with $J$ effect-modifier levels; the multi-class bias retains the same product structure with modified amplification terms (Corollary~\ref{cor:multiclass} in Appendix~\ref{app:multiclass}).
67	
68	Assumption~(A3) ensures $M_s = C_s$; when $P(Z{=}1) \neq 0.5$, the mixing matrices acquire asymmetric entries, but the product structure persists with modified coefficients (Appendix~\ref{app:derivation}).
69	Empirical verification under class imbalance (Appendix~\ref{app:classimbalance}) shows that the bias identity maintains $R^2 \geq 0.976$ even at $P(Z{=}1) = 0.1$ for $K{=}2$, though EC-HTE's RMSE ratio relative to global correction increases to 1.06--1.68 as class imbalance grows.
70	In practice, NLP classification tasks often exhibit substantial class imbalance (e.g., hate speech prevalence $\ll 50\%$), and practitioners should verify that the per-subgroup expert budget threshold remains satisfied under the actual class distribution.
71	Empirical verification (Section~\ref{sec:bias_mechanism}) yields $R^2 = 0.994$ for $K{=}2$ and $R^2 = 0.974$ for $K{=}4$; the residual variance reflects finite-sample Monte Carlo noise, not model misspecification.
72	
73	\paragraph{Sensitivity to (A1).}
74	Assumption~(A1) is not empirically testable.
75	If misclassification correlates with potential outcomes ($\gamma = \mathrm{Corr}(\mathbb{1}[\hat{Z} {\neq} Z],\, Y(1){-}Y(0) \mid Z, S) \neq 0$), Theorem~\ref{thm:bias_identity} gains an $O(\gamma)$ perturbation; in NLP settings, this is plausible when LLM accuracy varies with outcome magnitude.
76	Sensitivity analysis frameworks~\cite{lash2009applying,dorn2022sharp} can bound the degradation (Section~\ref{sec:limitations}).
77	
78	\paragraph{Finite-sample remainder.}
79	Theorem~\ref{thm:bias_identity} is an exact population identity.
80	In practice, confusion matrices are estimated from $n_{\text{expert}}$ expert labels with $\hat{C}_s = C_s + E_s$, $\|E_s\| = O_p(n_{\text{expert}}^{-1/2})$; the resulting remainder is therefore $R_n = O_p(n_{\text{expert}}^{-1/2} \cdot \kappa(C_s))$, motivating the singularity guard ($\kappa > 100 \to$ fallback) in Section~\ref{sec:method}.
81	
82	\begin{proposition}[Debiasing Can Increase Bias]
83	\label{prop:debiasing_hurts}
84	Under \textnormal{(A1)--(A5)}, global correction produces larger absolute bias than the naive estimator ($|\mathrm{bias}_{\mathrm{global}}| > |\mathrm{bias}_{\mathrm{naive}}|$) in subgroup $s$ if and only if
85	\begin{equation}
86	\frac{|\delta_s|}{(1 - 2\bar{\pi}) \cdot \pi_s} > 1.
87	\label{eq:hurts_condition}
88	\end{equation}
89	\end{proposition}
90	
91	Equation~\eqref{eq:hurts_condition} partitions subgroups into two regimes.
92	For high-error subgroups ($\pi_s > \bar{\pi}$), the condition reduces to $\pi_s > 0.5$, excluded by~(A4).
93	For low-error subgroups ($\pi_s < \bar{\pi}$), it holds whenever $\pi_s < \bar{\pi} / (2(1 - \bar{\pi}))$---easily satisfied: when $\bar{\pi} = 0.15$, any subgroup with $\pi_s < 0.088$ is harmed.
94	The mechanism is over-correction: global inversion applies a correction calibrated for the average error rate, so low-error subgroups are overcorrected (the correction overshoots and reverses bias sign) while high-error subgroups are under-corrected.
95	For subgroups with near-zero misclassification ($\pi_s \approx 0$), the naive estimator is nearly unbiased, yet global correction creates substantial bias---debiasing can be worse than doing nothing.
96	
97	In our experiments (Section~\ref{sec:bias_mechanism}), global correction increases bias in 50\% of $K{=}2$ configurations across our parameter grid (260 of 520, excluding cases where $\Delta\pi{=}0$).
98	With the difference-in-means estimator, maximum amplification reaches $2.86\times$ for $K{=}2$ and $2.41\times$ for $K{=}4$; the mechanism operates across estimator types, with nonlinear estimators amplifying the effect further (Section~\ref{sec:ec_hte_eval}).
99	Figure~\ref{fig:heatmap} visualizes the amplification across the full $\Delta\pi \times \Delta\tau$ parameter grid.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "9817b23d-5915-4033-a324-2e6a621ce975",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
      "content": "% Requires preamble: \\usepackage{amsthm,amsmath,amssymb}\n% and: \\newtheorem{theorem}{Theorem}\n%      \\newtheorem{corollary}[theorem]{Corollary}\n%      \\newtheorem{proposition}[theorem]{Proposition}\n\n\\section{Bias Decomposition: When Debiasing Hurts}\n\\label{sec:theory}\n\nWe formalize the bias that global misclassification correction introduces when subgroup error rates are heterogeneous.\nConsider estimating the conditional average treatment effect (CATE) $\\tau(z) = \\mathbb{E}[Y(1) - Y(0) \\mid Z = z]$, where $Z \\in \\{0, 1\\}$ is a binary effect modifier observed only through a noisy annotation $\\hat{Z}$.\nThe population consists of $K$ subgroups $S \\in \\{1, \\ldots, K\\}$ with weights $w_s = P(S{=}s)$, each characterized by a $2 \\times 2$ confusion matrix $C_s$ with symmetric error rate $\\pi_s = P(\\hat{Z} \\neq Z \\mid S{=}s)$.\nStandard practice estimates a single confusion matrix $\\bar{C} = \\sum_s w_s C_s$ from expert annotations and applies its inverse uniformly to all observations, with pooled error rate $\\bar{\\pi} = \\sum_s w_s \\pi_s$.\nWe show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.\n\nWe state five assumptions maintained throughout.\n%\n\\begin{itemize}\n\\item[\\textbf{(A1)}] \\textit{Conditional independence:} misclassification depends only on the true label $Z$ and subgroup $S$, not on potential outcomes $Y(0), Y(1)$.\n\\item[\\textbf{(A2)}] \\textit{Symmetric misclassification:} $P(\\hat{Z}{=}1 \\mid Z{=}0, S{=}s) = P(\\hat{Z}{=}0 \\mid Z{=}1, S{=}s) = \\pi_s$ for all $s$ (diagnostic only; see Remark~2).\n\\item[\\textbf{(A3)}] \\textit{Balanced effect modifier:} $P(Z{=}0) = P(Z{=}1) = 0.5$. This simplifies the exposition; we discuss relaxation below.\n\\item[\\textbf{(A4)}] \\textit{Non-degeneracy:} $\\pi_s \\neq 0.5$ for all $s$, ensuring each $C_s$ is invertible.\n\\item[\\textbf{(A5)}] \\textit{Homogeneous treatment effects across subgroups:} $\\tau(z, s) = \\tau(z)$ for all $s$, so $\\Delta\\tau = \\tau(1) - \\tau(0)$ is a scalar.\n\\end{itemize}\n\nUnder (A2)--(A3), the Bayesian mixing matrix $M_s$ (entries $M_s[\\hat{z}, z] = P(Z{=}z \\mid \\hat{Z}{=}\\hat{z}, S{=}s)$) coincides with $C_s$.\nThe global mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s$.\n\n\\begin{theorem}[Bias Decomposition Identity]\n\\label{thm:bias_identity}\nUnder \\textnormal{(A1)--(A5)}, the bias of global correction in subgroup $s$ at effect-modifier level $z$ is\n\\begin{align}\n\\mathrm{bias}_{\\mathrm{global}}(z{=}0, s) &= +\\frac{\\delta_s \\cdot \\Delta\\tau}{1 - 2\\bar{\\pi}}, \\label{eq:bias_z0} \\\\\n\\mathrm{bias}_{\\mathrm{global}}(z{=}1, s) &= -\\frac{\\delta_s \\cdot \\Delta\\tau}{1 - 2\\bar{\\pi}}, \\label{eq:bias_z1}\n\\end{align}\nwhere $\\delta_s = \\pi_s - \\bar{\\pi}$ is the subgroup deviation from the pooled error rate and $\\Delta\\tau = \\tau(1) - \\tau(0)$ is the CATE heterogeneity.\n\\end{theorem}\n\nEquations~\\eqref{eq:bias_z0}--\\eqref{eq:bias_z1} constitute an exact finite-population identity, not an asymptotic approximation or bound.\nThe bias factors into three interpretable components: $\\delta_s$ captures how much subgroup $s$ deviates from the average misclassification rate, $\\Delta\\tau$ captures treatment effect heterogeneity across levels of $Z$, and $1/(1 - 2\\bar{\\pi})$ is an amplification factor from matrix inversion.\nBias vanishes when either source of variation is absent ($\\delta_s = 0$ or $\\Delta\\tau = 0$), and arises only through their interaction.\nTheorem~\\ref{thm:bias_identity} implies that global correction trades one source of confounding for another: it removes attenuation from label noise but introduces a new bias from error-rate heterogeneity.\n\n\\paragraph{Proof sketch.}\nGlobal correction applies $M_{\\text{global}}^{-1}$ to the subgroup-specific observed CATE $\\tau_{\\text{obs}}(\\cdot, s) = M_s \\cdot \\tau_{\\text{true}}$, yielding bias $(M_{\\text{global}}^{-1} M_s - I) \\cdot \\tau_{\\text{true}}$.\nDirect computation shows $M_{\\text{global}}^{-1} M_s - I = \\frac{\\delta_s}{1-2\\bar{\\pi}} \\bigl[\\begin{smallmatrix} -1 & 1 \\\\ 1 & -1 \\end{smallmatrix}\\bigr]$.\nApplying this matrix to $[\\tau(0),\\, \\tau(1)]^\\top$ produces the product form.\nThe full derivation appears in Appendix~\\ref{app:derivation}.\n\n\\begin{remark}\nTheorem~\\ref{thm:bias_identity} does not require assumption~(A2).\nFor arbitrary asymmetric confusion matrices ($\\mathrm{FPR}_s \\neq \\mathrm{FNR}_s$),\nthe product form $\\mathrm{bias}(z, s) = \\Delta\\tau \\cdot [B_s]_{z,1}$ holds exactly,\nwhere $B_s = M_{\\mathrm{global}}^{-1} M_s - I$, because $B_s \\mathbf{1} = \\mathbf{0}$\nfollows from stochasticity of $M_s$ and $M_{\\mathrm{global}}$ alone.\nAssumption~(A2) simplifies $[B_s]_{z,1}$ to the scalar\n$\\pm \\delta_s / (1 - 2\\bar{\\pi})$ but is not necessary for the product structure.\nUnder asymmetric errors, the diagnostic (Proposition~\\ref{prop:debiasing_hurts}) requires evaluating $[B_s]_{z,1}$ cell-by-cell rather than via a single scalar threshold; the AUC decreases from 0.86 to 0.82 (Appendix~\\ref{app:asymmetric}), reflecting the additional complexity of cell-specific error rates.\nFor binary effect modifiers ($|\\mathcal{Z}|{=}2$), the asymmetric score $|[B_s]_{z,1}|$ reduces to a monotone transform of the symmetric score $|\\delta_s|/((1{-}2\\bar{\\pi})\\pi_s)$, because column-stochastic $M$ forces $|B_s[0,1]|{=}|B_s[1,1]|$; practitioners may use the simpler symmetric formula without loss.\nSee Appendix~\\ref{app:asymmetric} for the full derivation and empirical verification\n($R^2 = 0.991$).\n\\end{remark}\n\nAssumption~(A5) simplifies exposition; the identity generalizes to subgroup-specific $\\Delta\\tau_s$ (Corollary~\\ref{cor:a5_relaxation}, Appendix~\\ref{app:a5_violation}).\nEC-HTE's correction does not depend on (A5): each $\\hat{C}_s^{-1}$ corrects the local misclassification structure regardless of whether $\\Delta\\tau$ varies; under both positive and negative $\\Delta\\tau_s$--$\\delta_s$ correlation, EC-HTE maintains $\\geq$93\\% coverage while global correction degrades to 74--82\\% (Appendix~\\ref{app:a5_violation}).\n\nThe identity extends to $K > 2$ subgroups with $J$ effect-modifier levels; the multi-class bias retains the same product structure with modified amplification terms (Corollary~\\ref{cor:multiclass} in Appendix~\\ref{app:multiclass}).\n\nAssumption~(A3) ensures $M_s = C_s$; when $P(Z{=}1) \\neq 0.5$, the mixing matrices acquire asymmetric entries, but the product structure persists with modified coefficients (Appendix~\\ref{app:derivation}).\nEmpirical verification under class imbalance (Appendix~\\ref{app:classimbalance}) shows that the bias identity maintains $R^2 \\geq 0.976$ even at $P(Z{=}1) = 0.1$ for $K{=}2$, though EC-HTE's RMSE ratio relative to global correction increases to 1.06--1.68 as class imbalance grows.\nIn practice, NLP classification tasks often exhibit substantial class imbalance (e.g., hate speech prevalence $\\ll 50\\%$), and practitioners should verify that the per-subgroup expert budget threshold remains satisfied under the actual class distribution.\nEmpirical verification (Section~\\ref{sec:bias_mechanism}) yields $R^2 = 0.994$ for $K{=}2$ and $R^2 = 0.974$ for $K{=}4$; the residual variance reflects finite-sample Monte Carlo noise, not model misspecification.\n\n\\paragraph{Sensitivity to (A1).}\nAssumption~(A1) is not empirically testable.\nIf misclassification correlates with potential outcomes ($\\gamma = \\mathrm{Corr}(\\mathbb{1}[\\hat{Z} {\\neq} Z],\\, Y(1){-}Y(0) \\mid Z, S) \\neq 0$), Theorem~\\ref{thm:bias_identity} gains an $O(\\gamma)$ perturbation; in NLP settings, this is plausible when LLM accuracy varies with outcome magnitude.\nSensitivity analysis frameworks~\\cite{lash2009applying,dorn2022sharp} can bound the degradation (Section~\\ref{sec:limitations}).\n\n\\paragraph{Finite-sample remainder.}\nTheorem~\\ref{thm:bias_identity} is an exact population identity.\nIn practice, confusion matrices are estimated from $n_{\\text{expert}}$ expert labels with $\\hat{C}_s = C_s + E_s$, $\\|E_s\\| = O_p(n_{\\text{expert}}^{-1/2})$; the resulting remainder is therefore $R_n = O_p(n_{\\text{expert}}^{-1/2} \\cdot \\kappa(C_s))$, motivating the singularity guard ($\\kappa > 100 \\to$ fallback) in Section~\\ref{sec:method}.\n\n\\begin{proposition}[Debiasing Can Increase Bias]\n\\label{prop:debiasing_hurts}\nUnder \\textnormal{(A1)--(A5)}, global correction produces larger absolute bias than the naive estimator ($|\\mathrm{bias}_{\\mathrm{global}}| > |\\mathrm{bias}_{\\mathrm{naive}}|$) in subgroup $s$ if and only if\n\\begin{equation}\n\\frac{|\\delta_s|}{(1 - 2\\bar{\\pi}) \\cdot \\pi_s} > 1.\n\\label{eq:hurts_condition}\n\\end{equation}\n\\end{proposition}\n\nEquation~\\eqref{eq:hurts_condition} partitions subgroups into two regimes.\nFor high-error subgroups ($\\pi_s > \\bar{\\pi}$), the condition reduces to $\\pi_s > 0.5$, excluded by~(A4).\nFor low-error subgroups ($\\pi_s < \\bar{\\pi}$), it holds whenever $\\pi_s < \\bar{\\pi} / (2(1 - \\bar{\\pi}))$---easily satisfied: when $\\bar{\\pi} = 0.15$, any subgroup with $\\pi_s < 0.088$ is harmed.\nThe mechanism is over-correction: global inversion applies a correction calibrated for the average error rate, so low-error subgroups are overcorrected (the correction overshoots and reverses bias sign) while high-error subgroups are under-corrected.\nFor subgroups with near-zero misclassification ($\\pi_s \\approx 0$), the naive estimator is nearly unbiased, yet global correction creates substantial bias---debiasing can be worse than doing nothing.\n\nIn our experiments (Section~\\ref{sec:bias_mechanism}), global correction increases bias in 50\\% of $K{=}2$ configurations across our parameter grid (260 of 520, excluding cases where $\\Delta\\pi{=}0$).\nWith the difference-in-means estimator, maximum amplification reaches $2.86\\times$ for $K{=}2$ and $2.41\\times$ for $K{=}4$; the mechanism operates across estimator types, with nonlinear estimators amplifying the effect further (Section~\\ref{sec:ec_hte_eval}).\nFigure~\\ref{fig:heatmap} visualizes the amplification across the full $\\Delta\\pi \\times \\Delta\\tau$ parameter grid.",
      "numLines": 99,
      "startLine": 1,
      "totalLines": 99
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_013dJyABj2s7uB4VaaNy4mjc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "01c2e00d-0d47-4793-9c8c-a568848d387b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxbidNY9Li64EvqEmWDDgD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14179,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14179
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-23T09:23:29.127Z_

<details><summary>↩ Tool result · `toolu_013dJyABj2s7uB4VaaNy4mjc`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	Large language models (LLMs) now routinely replace human annotators in computational social science (CSS), producing labels for sentiment, hate speech, stance, and political discourse at costs orders of magnitude below manual coding~\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp}.
5	Yet these annotations are not uniformly accurate.
6	\citet{ashwin2025bias} document that LLM misclassification rates vary by up to 5$\times$ across demographic subgroups defined by refugee status, gender, and education level.
7	In a pilot study, GPT-4.1 achieves 85.8\% binary accuracy on TweetEval sentiment, but error rates range from 10.2\% to 20.0\% across text-feature subgroups ($\Delta\pi = 0.098$).
8	When such annotations serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, subgroup-specific errors propagate directly into conditional average treatment effect (CATE) estimates.
9	The resulting bias is not random noise that averages out; it is structured by the same demographic axes that define the research question.
10	Standard correction procedures\footnote{Throughout, ``debiasing'' refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing.}, which estimate a single confusion matrix and apply its inverse uniformly, cannot account for this heterogeneity.
11	
12	We formalize this problem and derive an exact bias identity for the correction-induced error.
13	When a pooled confusion matrix is applied to correct subgroup CATEs, it misattributes error across subgroups with an exact product form: the bias in subgroup $s$ equals $\delta_s \cdot \Delta\tau / (1 - 2\bar{\pi})$, where $\delta_s$ is the deviation from the pooled error rate and $\Delta\tau$ is the CATE heterogeneity (Theorem~\ref{thm:bias_identity}).
14	This is not a bound but an exact population-level identity, verified empirically with $R^2 = 0.994$ ($K{=}2$) and $R^2 = 0.974$ ($K{=}4$) on synthetic grids, and $R^2 = 0.975$ across 11 real LLM confusion matrices spanning open-source and proprietary model families.
15	A direct consequence is that global correction can be worse than no correction at all: global correction worsens CATE bias in 50\% of $K{=}2$ configurations (260/520) across our parameter grid---concentrated in regimes where $\Delta\pi > 0.10$ and per-subgroup expert samples exceed 25---with amplification reaching 2.86$\times$ ($K{=}2$) and 5.9$\times$ ($K{=}4$ with CausalForest).
16	The bias identity also yields a $\Delta\tau$-free diagnostic (Proposition~\ref{prop:debiasing_hurts}): a condition on per-subgroup misclassification rates alone predicts when global correction will increase bias, achieving AUC $= 1.0$ on subgroups with non-zero effect heterogeneity (Section~\ref{sec:diagnostic})---independently useful even without adopting EC-HTE, since practitioners can flag harmful correction from a pilot sample before estimating any treatment effects.
17	Error-Corrected Heterogeneous Treatment Effects (EC-HTE), the per-subgroup correction prescribed by the identity, reduces $|\text{bias}|$ from 0.059 to 0.008 under extreme heterogeneity ($K{=}2$) via hierarchical Bayesian confusion matrix estimation.
18	EC-HTE's advantage is conditional on sufficient error heterogeneity and expert budget; when $\Delta\pi$ is small, the variance cost of stratification outweighs its bias benefit---the expected bias-variance tradeoff of any subgroup-stratified correction (Figure~\ref{fig:bias_mechanism}).
19	
20	Subgroup CATEs inform resource allocation---e.g., whether a policy reduces toxicity more in long-form versus short-form posts---and biased estimates can reverse the sign of apparent heterogeneity, directing resources away from communities that benefit most.
21	The failure mode is subtle: correcting for annotation noise using a pooled confusion matrix may introduce more bias than doing nothing, precisely in the low-error subgroups where labels were most trustworthy.
22	
23	Existing corrections---PPI~\cite{angelopoulos2023ppi}, DSL~\cite{egami2024dsl}, PPCI~\cite{sui2026ppci}, arm-specific PPI~\cite{mozer2026ppi}, ForestIV~\cite{bu2023forestiv}---address population-level or outcome-side measurement error but assume homogeneous prediction error across subgroups; none corrects bias when the mismeasured variable is the effect modifier indexing the CATE function (Section~\ref{sec:related}).
24	
25	\begin{figure}[t]
26	\centering
27	\includegraphics[width=\columnwidth]{figures/fig1_bias_mechanism.pdf}
28	\caption{Bias mechanism under global vs.\ subgroup-stratified correction. Global correction applies the pooled error rate $\bar{\pi}$ uniformly, over-correcting low-error subgroups (introducing bias where none existed) and under-correcting high-error subgroups. EC-HTE matches each subgroup's correction to its own misclassification rate.}
29	\label{fig:bias_mechanism}
30	\end{figure}
31	
32	Our contributions are:
33	\begin{itemize}
34	    \item An exact bias identity (Theorem~\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup CATE bias proportional to each subgroup's misclassification deviation times the treatment effect heterogeneity---an exact finite-population identity with independent diagnostic value, verified at $R^2 \geq 0.97$ on synthetic grids and 11 real LLM confusion matrices (Sections~\ref{sec:theory},~\ref{sec:bias_mechanism}).
35	    \item A $\Delta\tau$-free diagnostic (Proposition~\ref{prop:debiasing_hurts}) derived from the identity: a condition on per-subgroup misclassification rates alone predicts when global correction increases bias, achieving AUC $= 1.0$ on subgroups with non-zero effect heterogeneity---independently actionable without EC-HTE (Section~\ref{sec:diagnostic}).
36	    \item EC-HTE, the per-subgroup correction prescribed by the bias structure via hierarchical Bayesian confusion matrix estimation, compatible with difference-in-means, CausalForest, and R-learner, and composable with PPCI for joint covariate/outcome error; we characterize applicability conditions and crossover budgets (Sections~\ref{sec:method}--\ref{sec:diagnostic}; Appendix~\ref{sec:budget}).
37	\end{itemize}
38	While we develop the theory and experiments for LLM annotation---the leading practical case---the bias identity applies whenever any proxy classifier with subgroup-varying error rates is used to construct effect modifiers for causal inference.
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "f3053d5a-9ac8-4e51-90a9-01e0ae989794",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models (LLMs) now routinely replace human annotators in computational social science (CSS), producing labels for sentiment, hate speech, stance, and political discourse at costs orders of magnitude below manual coding~\\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp}.\nYet these annotations are not uniformly accurate.\n\\citet{ashwin2025bias} document that LLM misclassification rates vary by up to 5$\\times$ across demographic subgroups defined by refugee status, gender, and education level.\nIn a pilot study, GPT-4.1 achieves 85.8\\% binary accuracy on TweetEval sentiment, but error rates range from 10.2\\% to 20.0\\% across text-feature subgroups ($\\Delta\\pi = 0.098$).\nWhen such annotations serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, subgroup-specific errors propagate directly into conditional average treatment effect (CATE) estimates.\nThe resulting bias is not random noise that averages out; it is structured by the same demographic axes that define the research question.\nStandard correction procedures\\footnote{Throughout, ``debiasing'' refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing.}, which estimate a single confusion matrix and apply its inverse uniformly, cannot account for this heterogeneity.\n\nWe formalize this problem and derive an exact bias identity for the correction-induced error.\nWhen a pooled confusion matrix is applied to correct subgroup CATEs, it misattributes error across subgroups with an exact product form: the bias in subgroup $s$ equals $\\delta_s \\cdot \\Delta\\tau / (1 - 2\\bar{\\pi})$, where $\\delta_s$ is the deviation from the pooled error rate and $\\Delta\\tau$ is the CATE heterogeneity (Theorem~\\ref{thm:bias_identity}).\nThis is not a bound but an exact population-level identity, verified empirically with $R^2 = 0.994$ ($K{=}2$) and $R^2 = 0.974$ ($K{=}4$) on synthetic grids, and $R^2 = 0.975$ across 11 real LLM confusion matrices spanning open-source and proprietary model families.\nA direct consequence is that global correction can be worse than no correction at all: global correction worsens CATE bias in 50\\% of $K{=}2$ configurations (260/520) across our parameter grid---concentrated in regimes where $\\Delta\\pi > 0.10$ and per-subgroup expert samples exceed 25---with amplification reaching 2.86$\\times$ ($K{=}2$) and 5.9$\\times$ ($K{=}4$ with CausalForest).\nThe bias identity also yields a $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}): a condition on per-subgroup misclassification rates alone predicts when global correction will increase bias, achieving AUC $= 1.0$ on subgroups with non-zero effect heterogeneity (Section~\\ref{sec:diagnostic})---independently useful even without adopting EC-HTE, since practitioners can flag harmful correction from a pilot sample before estimating any treatment effects.\nError-Corrected Heterogeneous Treatment Effects (EC-HTE), the per-subgroup correction prescribed by the identity, reduces $|\\text{bias}|$ from 0.059 to 0.008 under extreme heterogeneity ($K{=}2$) via hierarchical Bayesian confusion matrix estimation.\nEC-HTE's advantage is conditional on sufficient error heterogeneity and expert budget; when $\\Delta\\pi$ is small, the variance cost of stratification outweighs its bias benefit---the expected bias-variance tradeoff of any subgroup-stratified correction (Figure~\\ref{fig:bias_mechanism}).\n\nSubgroup CATEs inform resource allocation---e.g., whether a policy reduces toxicity more in long-form versus short-form posts---and biased estimates can reverse the sign of apparent heterogeneity, directing resources away from communities that benefit most.\nThe failure mode is subtle: correcting for annotation noise using a pooled confusion matrix may introduce more bias than doing nothing, precisely in the low-error subgroups where labels were most trustworthy.\n\nExisting corrections---PPI~\\cite{angelopoulos2023ppi}, DSL~\\cite{egami2024dsl}, PPCI~\\cite{sui2026ppci}, arm-specific PPI~\\cite{mozer2026ppi}, ForestIV~\\cite{bu2023forestiv}---address population-level or outcome-side measurement error but assume homogeneous prediction error across subgroups; none corrects bias when the mismeasured variable is the effect modifier indexing the CATE function (Section~\\ref{sec:related}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig1_bias_mechanism.pdf}\n\\caption{Bias mechanism under global vs.\\ subgroup-stratified correction. Global correction applies the pooled error rate $\\bar{\\pi}$ uniformly, over-correcting low-error subgroups (introducing bias where none existed) and under-correcting high-error subgroups. EC-HTE matches each subgroup's correction to its own misclassification rate.}\n\\label{fig:bias_mechanism}\n\\end{figure}\n\nOur contributions are:\n\\begin{itemize}\n    \\item An exact bias identity (Theorem~\\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup CATE bias proportional to each subgroup's misclassification deviation times the treatment effect heterogeneity---an exact finite-population identity with independent diagnostic value, verified at $R^2 \\geq 0.97$ on synthetic grids and 11 real LLM confusion matrices (Sections~\\ref{sec:theory},~\\ref{sec:bias_mechanism}).\n    \\item A $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}) derived from the identity: a condition on per-subgroup misclassification rates alone predicts when global correction increases bias, achieving AUC $= 1.0$ on subgroups with non-zero effect heterogeneity---independently actionable without EC-HTE (Section~\\ref{sec:diagnostic}).\n    \\item EC-HTE, the per-subgroup correction prescribed by the bias structure via hierarchical Bayesian confusion matrix estimation, compatible with difference-in-means, CausalForest, and R-learner, and composable with PPCI for joint covariate/outcome error; we characterize applicability conditions and crossover budgets (Sections~\\ref{sec:method}--\\ref{sec:diagnostic}; Appendix~\\ref{sec:budget}).\n\\end{itemize}\nWhile we develop the theory and experiments for LLM annotation---the leading practical case---the bias identity applies whenever any proxy classifier with subgroup-varying error rates is used to construct effect modifiers for causal inference.\n",
      "numLines": 39,
      "startLine": 1,
      "totalLines": 39
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01PhvvMeCUTiHCD6B7KGSp66`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "9da62e6f-1e6b-4abe-a820-64c0eabff782",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxbidNY9Li64EvqEmWDDgD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14179,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14179
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-23T09:23:29.623Z_

<details><summary>↩ Tool result · `toolu_01PhvvMeCUTiHCD6B7KGSp66`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Measurement error and annotation models.}
5	Classical measurement error theory shows that correction via estimated error models can amplify MSE when the error structure is misspecified~\cite{fuller1987measurement,carroll2006measurement}; Bayesian approaches require informative priors when identification is weak~\cite{gustafson2003measurement}, and nonparametric methods use repeated measurements or instruments to recover the true distribution~\cite{hu2008nonparametric}.
6	
7	Three distinctions separate our contribution from prior measurement error analyses.
8	First, we study effect modifier misclassification---the mismeasured variable defines the CATE function itself---rather than regressor~\cite{frazis2003estimating,carroll2006measurement} or confounder~\cite{ogburn2012nondifferential,greenland1980effect} error, where attenuation is the primary concern.
9	Second, Theorem~\ref{thm:bias_identity} derives an exact identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.
10	Concretely, \citet{frazis2003estimating} derive scalar attenuation $\tilde{\beta} = \beta(1 - \pi_0 - \pi_1)$ for the uncorrected estimator under homogeneous misclassification; Theorem~\ref{thm:bias_identity} characterizes a structurally distinct quantity---correction-induced bias $\delta_s \cdot \Delta\tau / (1 - 2\bar{\pi})$---that is subgroup-specific, potentially sign-reversing, and absent from the uncorrected estimator.
11	The homogeneous-error setting is a degenerate case: with $K{=}1$, $\delta_s{=}0$ and correction-induced bias vanishes, recovering the classical attenuation result.
12	The algebraic mechanisms also differ: OLS attenuation under misclassified regressors~\cite{frazis2003estimating,blackwell2017unified} versus confusion matrix inversion that redistributes error across subgroups with heterogeneous rates.
13	We empirically verify this distinction: F-L correction---even when applied per subgroup---produces higher bias than the naive estimator under heterogeneous misclassification, whereas EC-HTE achieves near-oracle performance (Appendix~\ref{app:fl_comparison}).
14	Third, the $\delta_s \cdot \Delta\tau$ product structure arises only under heterogeneous error rates; all homogeneous-error analyses~\cite{battistin2014treatment,fong2021machine} miss this interaction entirely.
15	In the annotation literature, \citet{dawid1979maximum} introduced confusion matrix estimation for multiple annotators, with extensions to item difficulty, annotator competence, and hierarchical priors~\cite{passonneau2014benefits,hovy2013learning,paun2018comparing}.
16	Our hierarchical estimator (Section~\ref{sec:method}) adapts this architecture from label aggregation to causal inference, tying the prior structure to the subgroup dimension that defines treatment effect heterogeneity.
17	
18	\paragraph{HTE estimation and LLM annotation error.}
19	Causal forests~\cite{athey2016recursive,wager2018causal}, double/debiased ML~\cite{chernozhukov2018dml,semenova2021debiased}, doubly-robust CATE estimators~\cite{kennedy2023dr}, and meta-learners~\cite{kunzel2019metalearners} all assume that covariates defining heterogeneity are observed without error; when the effect modifier is misclassified, CATE estimates conflate effects across groups.
20	EC-HTE provides upstream correction that restores valid inputs to any downstream estimator.
21	The corrected pseudo-outcomes are in principle compatible with other HTE estimators such as the R-learner~\citep{nie2021quasi}.
22	For broader perspectives on causal inference with text data, see \citet{feder2022causal} and \citet{keith2020text}; \citet{wang2020methods} study inference correction when outcomes are ML-predicted, a related but distinct problem from effect modifier misclassification.
23	LLMs now match crowd-worker accuracy on many classification tasks~\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,pangakis2023automated}, but \citet{ashwin2025bias} show that error rates vary by up to $5\times$ across demographic subgroups.
24	This subgroup-varying error is the failure mode we address: it distorts the very contrasts that define the research question, and prior work documents the pattern without providing a correction mechanism for downstream causal estimands.
25	Concurrent work identifies variance-side measurement error from LLM pipeline design choices~\cite{messing2026hidden}; our framework addresses the complementary bias-side problem from heterogeneous misclassification rates across subgroups.
26	Temperature or Platt scaling~\cite{guo2017calibration} reduces per-subgroup $\pi_s$ but does not eliminate heterogeneity $\Delta\pi$; EC-HTE corrects the residual $\delta_s$-driven bias that persists post-calibration (Appendix~\ref{app:calibration} empirically confirms this complementarity).
27	
28	\paragraph{Prediction-powered and design-based correction.}
29	PPI~\cite{angelopoulos2023ppi,zrnic2024cross} and DSL~\cite{egami2024dsl} correct population-level aggregates assuming homogeneous prediction error.
30	In our setting---binary effect modifier with known subgroup structure, a special case of the broader problems DSL addresses---DSL's measurement error correction reduces, under the confusion-matrix parameterization we adopt, to confusion matrix inversion: pooled DSL is equivalent to our Global baseline, and per-subgroup DSL to Stratified MLE (Section~\ref{sec:ec_hte_eval}; Appendix~\ref{app:ppi_comparison}).
31	EC-HTE adds hierarchical partial pooling across subgroups, borrowing strength to reduce variance---a mechanism outside the DSL framework.
32	\citet{audinet2025benchmarking} benchmark DSL and PPI debiasing for LLM-based parameter estimation, documenting bias-variance tradeoffs analogous to our findings; their analysis targets population-level parameters rather than subgroup-conditional estimands, leaving the $\delta_s \cdot \Delta\tau$ interaction we formalize unaddressed.
33	\citet{mozer2026ppi} extend PPI to arm-specific ATE correction; PPCI~\cite{sui2026ppci} targets conditional estimands but corrects outcome-side error ($\hat{Y}$ given true $Z$), not covariate-side misclassification; ForestIV~\cite{bu2023forestiv} targets the outcome model rather than the heterogeneity structure.
34	None corrects bias when the mismeasured variable is the effect modifier indexing the CATE function.
35	\citet{imai2010causal} study treatment misclassification, requiring instrumental variables or partial identification; our problem is structurally distinct because the treatment is observed correctly but the effect modifier is misclassified, admitting exact correction through confusion matrices rather than bounds.
36	Extended discussion of these distinctions appears in Appendix~\ref{app:related}.
37	Our validation combines synthetic DGPs, semi-synthetic experiments, and real LLM confusion matrices, consistent with PPI and DSL evaluation methodology; Appendix~\ref{app:multilm} validates both $\Delta\pi$ heterogeneity and the bias identity itself ($R^2 = 0.975$) across 11 model--dataset combinations.
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "b167cce9-f58e-48a3-bc7a-59c67194b099",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Measurement error and annotation models.}\nClassical measurement error theory shows that correction via estimated error models can amplify MSE when the error structure is misspecified~\\cite{fuller1987measurement,carroll2006measurement}; Bayesian approaches require informative priors when identification is weak~\\cite{gustafson2003measurement}, and nonparametric methods use repeated measurements or instruments to recover the true distribution~\\cite{hu2008nonparametric}.\n\nThree distinctions separate our contribution from prior measurement error analyses.\nFirst, we study effect modifier misclassification---the mismeasured variable defines the CATE function itself---rather than regressor~\\cite{frazis2003estimating,carroll2006measurement} or confounder~\\cite{ogburn2012nondifferential,greenland1980effect} error, where attenuation is the primary concern.\nSecond, Theorem~\\ref{thm:bias_identity} derives an exact identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.\nConcretely, \\citet{frazis2003estimating} derive scalar attenuation $\\tilde{\\beta} = \\beta(1 - \\pi_0 - \\pi_1)$ for the uncorrected estimator under homogeneous misclassification; Theorem~\\ref{thm:bias_identity} characterizes a structurally distinct quantity---correction-induced bias $\\delta_s \\cdot \\Delta\\tau / (1 - 2\\bar{\\pi})$---that is subgroup-specific, potentially sign-reversing, and absent from the uncorrected estimator.\nThe homogeneous-error setting is a degenerate case: with $K{=}1$, $\\delta_s{=}0$ and correction-induced bias vanishes, recovering the classical attenuation result.\nThe algebraic mechanisms also differ: OLS attenuation under misclassified regressors~\\cite{frazis2003estimating,blackwell2017unified} versus confusion matrix inversion that redistributes error across subgroups with heterogeneous rates.\nWe empirically verify this distinction: F-L correction---even when applied per subgroup---produces higher bias than the naive estimator under heterogeneous misclassification, whereas EC-HTE achieves near-oracle performance (Appendix~\\ref{app:fl_comparison}).\nThird, the $\\delta_s \\cdot \\Delta\\tau$ product structure arises only under heterogeneous error rates; all homogeneous-error analyses~\\cite{battistin2014treatment,fong2021machine} miss this interaction entirely.\nIn the annotation literature, \\citet{dawid1979maximum} introduced confusion matrix estimation for multiple annotators, with extensions to item difficulty, annotator competence, and hierarchical priors~\\cite{passonneau2014benefits,hovy2013learning,paun2018comparing}.\nOur hierarchical estimator (Section~\\ref{sec:method}) adapts this architecture from label aggregation to causal inference, tying the prior structure to the subgroup dimension that defines treatment effect heterogeneity.\n\n\\paragraph{HTE estimation and LLM annotation error.}\nCausal forests~\\cite{athey2016recursive,wager2018causal}, double/debiased ML~\\cite{chernozhukov2018dml,semenova2021debiased}, doubly-robust CATE estimators~\\cite{kennedy2023dr}, and meta-learners~\\cite{kunzel2019metalearners} all assume that covariates defining heterogeneity are observed without error; when the effect modifier is misclassified, CATE estimates conflate effects across groups.\nEC-HTE provides upstream correction that restores valid inputs to any downstream estimator.\nThe corrected pseudo-outcomes are in principle compatible with other HTE estimators such as the R-learner~\\citep{nie2021quasi}.\nFor broader perspectives on causal inference with text data, see \\citet{feder2022causal} and \\citet{keith2020text}; \\citet{wang2020methods} study inference correction when outcomes are ML-predicted, a related but distinct problem from effect modifier misclassification.\nLLMs now match crowd-worker accuracy on many classification tasks~\\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,pangakis2023automated}, but \\citet{ashwin2025bias} show that error rates vary by up to $5\\times$ across demographic subgroups.\nThis subgroup-varying error is the failure mode we address: it distorts the very contrasts that define the research question, and prior work documents the pattern without providing a correction mechanism for downstream causal estimands.\nConcurrent work identifies variance-side measurement error from LLM pipeline design choices~\\cite{messing2026hidden}; our framework addresses the complementary bias-side problem from heterogeneous misclassification rates across subgroups.\nTemperature or Platt scaling~\\cite{guo2017calibration} reduces per-subgroup $\\pi_s$ but does not eliminate heterogeneity $\\Delta\\pi$; EC-HTE corrects the residual $\\delta_s$-driven bias that persists post-calibration (Appendix~\\ref{app:calibration} empirically confirms this complementarity).\n\n\\paragraph{Prediction-powered and design-based correction.}\nPPI~\\cite{angelopoulos2023ppi,zrnic2024cross} and DSL~\\cite{egami2024dsl} correct population-level aggregates assuming homogeneous prediction error.\nIn our setting---binary effect modifier with known subgroup structure, a special case of the broader problems DSL addresses---DSL's measurement error correction reduces, under the confusion-matrix parameterization we adopt, to confusion matrix inversion: pooled DSL is equivalent to our Global baseline, and per-subgroup DSL to Stratified MLE (Section~\\ref{sec:ec_hte_eval}; Appendix~\\ref{app:ppi_comparison}).\nEC-HTE adds hierarchical partial pooling across subgroups, borrowing strength to reduce variance---a mechanism outside the DSL framework.\n\\citet{audinet2025benchmarking} benchmark DSL and PPI debiasing for LLM-based parameter estimation, documenting bias-variance tradeoffs analogous to our findings; their analysis targets population-level parameters rather than subgroup-conditional estimands, leaving the $\\delta_s \\cdot \\Delta\\tau$ interaction we formalize unaddressed.\n\\citet{mozer2026ppi} extend PPI to arm-specific ATE correction; PPCI~\\cite{sui2026ppci} targets conditional estimands but corrects outcome-side error ($\\hat{Y}$ given true $Z$), not covariate-side misclassification; ForestIV~\\cite{bu2023forestiv} targets the outcome model rather than the heterogeneity structure.\nNone corrects bias when the mismeasured variable is the effect modifier indexing the CATE function.\n\\citet{imai2010causal} study treatment misclassification, requiring instrumental variables or partial identification; our problem is structurally distinct because the treatment is observed correctly but the effect modifier is misclassified, admitting exact correction through confusion matrices rather than bounds.\nExtended discussion of these distinctions appears in Appendix~\\ref{app:related}.\nOur validation combines synthetic DGPs, semi-synthetic experiments, and real LLM confusion matrices, consistent with PPI and DSL evaluation methodology; Appendix~\\ref{app:multilm} validates both $\\Delta\\pi$ heterogeneity and the bias identity itself ($R^2 = 0.975$) across 11 model--dataset combinations.\n",
      "numLines": 38,
      "startLine": 1,
      "totalLines": 38
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01Q8Q2jQ9LjY7Y5ssRmNgvez`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "4706e760-da8a-447b-895d-120686b89501",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxbidNY9Li64EvqEmWDDgD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14179,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14179
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-23T09:23:30.087Z_

<details><summary>↩ Tool result · `toolu_01Q8Q2jQ9LjY7Y5ssRmNgvez`</summary>

```text
1	\section{Experiments}
2	
3	\subsection{Setup}
4	
5	We test on synthetic ($N{=}5{,}000$, $K \in \{2, 4\}$, controlled $\Delta\tau$ and $\Delta\pi$, 100 MC runs) and semi-synthetic (TweetEval sentiment~\cite{barbieri2020tweeteval}, $K{=}4$ unbalanced subgroups, $\pi \in \{0.05, 0.10, 0.15, 0.25\}$) DGPs; full specifications in Appendix~\ref{app:dgp}.
6	
7	We compare: (1) \textit{Naive} (no correction), (2) \textit{Global} (pooled confusion matrix, equivalent to PPI/DSL~\cite{angelopoulos2023ppi,egami2024dsl} with homogeneous error), (3) \textit{Stratified MLE} (per-subgroup DSL without shrinkage), (4) \textit{HB EC-HTE} (our method), (5) \textit{PPCI}~\cite{sui2026ppci}, and (6) \textit{EC-HTE+PPCI}.
8	For CausalForest~\cite{wager2018causal}, we compare naive, global, and EC-HTE variants.
9	Primary metrics are $|\text{bias}|$, RMSE, and 95\% CI coverage, averaged across subgroups and 100 MC runs.
10	Robustness validation covers hate speech, six OpenAI models, subgroup misspecification, asymmetric confusion matrices, confounded treatment, and outcome-dependent misclassification (all $\geq$93.5\% coverage; Appendices~\ref{app:hatespeech}--\ref{app:a1_sensitivity}).
11	
12	\subsection{Empirical Validation of the Bias Identity}
13	\label{sec:bias_mechanism}
14	
15	We verify Theorem~\ref{thm:bias_identity} on a $K{=}2$ grid (520 configurations, $\Delta\pi \in [0, 0.25]$, $\Delta\tau \in (0, 0.50]$) and a $K{=}4$ grid (Appendix~\ref{app:dgp}).
16	Regressing observed subgroup bias on $\delta_s \cdot \Delta\tau / (1{-}2\bar{\pi})$ yields $R^2 = 0.994$ ($K{=}2$) and $0.974$ ($K{=}4$); residual variance reflects MC noise ($R^2 \geq 0.976$ even at $P(Z{=}1) = 0.1$; Appendix~\ref{app:classimbalance}).
17	Global correction worsens bias in 50\% of $K{=}2$ configurations (260/520, excluding $\Delta\pi{=}0$), with amplification reaching 2.86$\times$ ($K{=}2$) and 2.41$\times$ ($K{=}4$); Figure~\ref{fig:heatmap} visualizes the amplification surface.
18	
19	\begin{figure*}[t]
20	\centering
21	\includegraphics[width=\textwidth]{figures/fig2_heatmap.pdf}
22	\caption{Bias amplification under global correction ($K{=}2$). (a) Low-error subgroup: correction always helps. (b) High-error subgroup: correction \emph{increases} bias when $\Delta\pi > 0.12$ (hatched), reaching 2.86$\times$.}
23	\label{fig:heatmap}
24	\end{figure*}
25	
26	\subsection{EC-HTE Evaluation}
27	\label{sec:ec_hte_eval}
28	
29	Table~\ref{tab:main_results} presents the main results across representative configurations.
30	Notably, in the $K{=}2$ extreme row, global correction \emph{increases} $|\text{bias}|$ relative to naive (0.059 vs.\ 0.058)---a direct manifestation of Theorem~\ref{thm:bias_identity}: pooled correction overshoots in low-error subgroups.
31	HB EC-HTE reduces $|\text{bias}|$ from 0.059 to 0.008 (7.4$\times$) at $K{=}2$ and from 0.056 to 0.012 (4.7$\times$) at $K{=}4$, maintaining near-nominal coverage (0.94--0.96) with lower RMSE than stratified MLE.
32	Under moderate heterogeneity ($K{=}2$), methods converge: EC-HTE and global achieve comparable bias ($p > 0.05$; Table~\ref{tab:main_supp}).
33	In the semi-synthetic TweetEval experiment ($K{=}4$, $n_{\text{expert}}{=}250$), EC-HTE and Global achieve comparable $|\text{bias}|$ ($p{=}0.395$; Table~\ref{tab:main_supp}), but EC-HTE incurs higher RMSE (0.225 vs.\ 0.124), driven by moderate $\Delta\pi{=}0.20$ and unbalanced subgroups receiving ${\sim}30$ expert labels each.
34	When $\Delta\pi$ or per-subgroup budget is marginal, global correction is competitive on aggregate RMSE.
35	
36	\paragraph{CausalForest.}
37	With CausalForest~\cite{wager2018causal} ($K{=}4$, extreme, $n{=}500$), EC-HTE reduces $|\text{bias}|$ from 0.191 to 0.039 (4.9$\times$), improving coverage from 0.58 to 0.90; global correction amplifies naive bias up to 5.9$\times$ because the forest magnifies label errors (Table~\ref{tab:main_results}).
38	The residual coverage gap (90\% vs.\ oracle 94--96\%) reflects asymmetric $M^{-1}$ SE propagation rather than CM estimation error; a full bootstrap SE can improve coverage calibration (Appendix~\ref{app:bootstrap_se}).
39	
40	\begin{table}[t]
41	\centering
42	\caption{Main results (extreme heterogeneity). Metrics averaged over subgroups, $z$-levels, 100 MC runs. Bold: lowest $|\text{bias}|$. $^\dagger$RMSE exceeds Global. Moderate heterogeneity and TweetEval results---where methods converge and EC-HTE RMSE exceeds Global---in Table~\ref{tab:main_supp}; MC SEs in Appendix~\ref{app:mcse}.}
43	\label{tab:main_results}
44	\resizebox{\columnwidth}{!}{%
45	\begin{tabular}{ll ccc}
46	\toprule
47	Configuration & Method & $|\text{Bias}|$ & RMSE & Cov. \\
48	\midrule
49	\multirow{4}{*}{\shortstack[l]{DIM\\$K{=}2$, $n{=}250$}}
50	 & Naive & 0.058 & 0.090 & 0.82 \\
51	 & Global & 0.059 & 0.099 & 0.87 \\
52	 & Strat.\ MLE & 0.012 & 0.094 & 0.95 \\
53	 & HB EC-HTE & \textbf{0.008} & 0.089 & 0.94 \\
54	\midrule
55	\multirow{4}{*}{\shortstack[l]{DIM\\$K{=}4$, $n{=}500$}}
56	 & Naive & 0.062 & 0.113 & 0.88 \\
57	 & Global & 0.056 & 0.125 & 0.91 \\
58	 & Strat.\ MLE & \textbf{0.010} & 0.127$^\dagger$ & 0.95 \\
59	 & HB EC-HTE & 0.012 & 0.120 & 0.96 \\
60	\midrule
61	\multirow{3}{*}{\shortstack[l]{CausalForest\\$K{=}4$, $n{=}500$}}
62	 & Naive & 0.208 & 0.231 & 0.44 \\
63	 & Global & 0.191 & 0.244 & 0.58 \\
64	 & EC-HTE Forest & \textbf{0.039} & 0.180 & 0.90 \\
65	\bottomrule
66	\end{tabular}}
67	\end{table}
68	
69	\subsection{Actionable Diagnostic Without EC-HTE}
70	\label{sec:diagnostic}
71	
72	Proposition~\ref{prop:debiasing_hurts} provides a $\Delta\tau$-free diagnostic: global correction increases bias in subgroup $s$ iff $|\delta_s| / ((1-2\bar{\pi}) \cdot \pi_s) > 1$, computable from a pilot sample without estimating treatment effects.
73	A threshold classifier achieves AUC = 0.86 at the subgroup level (Figure~\ref{fig:roc}, Appendix).
74	On real LLM confusion matrices (16 combinations; Appendix~\ref{app:screening}), AUC decreases to 0.63, primarily from subgroups with $\tau_s \approx 0$ where both naive and corrected bias are near zero, making the ground-truth harm label indeterminate; on subgroups with $\tau_s > 0$, AUC reaches 1.0.
75	For $K{=}2$, $|\delta_0|{=}|\delta_1|$ forces ranking by $1/\pi_s$ alone, which can anti-predict harm; reliability is strongest for $K{\geq}4$.
76	A computable meta-criterion recovers reliability: when $\max_s \mathrm{score}(s) > 1$, the diagnostic achieves AUC $\geq 0.75$ across all 16 combinations; when $\max_s \mathrm{score}(s) \leq 1$, AUC drops to 0.0--0.67 (Appendix~\ref{app:screening}).
77	
78	A recommended practitioner workflow and budget crossover curves appear in Appendices~\ref{sec:budget}--\ref{app:screening}.
79	At $K{=}8$ with $n_{\text{expert}}{=}250$, EC-HTE maintains nominal coverage (95.6\%) but RMSE exceeds global correction, establishing a practical scalability boundary (Appendix~\ref{app:k8_subgroups}).
80	The bias identity further validates across eight LLMs spanning 11 model--dataset combinations ($R^2 = 0.975$; Appendix~\ref{app:multilm}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "27fe6bb9-482b-4e6e-8658-0fcc7a32a81f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\n\\subsection{Setup}\n\nWe test on synthetic ($N{=}5{,}000$, $K \\in \\{2, 4\\}$, controlled $\\Delta\\tau$ and $\\Delta\\pi$, 100 MC runs) and semi-synthetic (TweetEval sentiment~\\cite{barbieri2020tweeteval}, $K{=}4$ unbalanced subgroups, $\\pi \\in \\{0.05, 0.10, 0.15, 0.25\\}$) DGPs; full specifications in Appendix~\\ref{app:dgp}.\n\nWe compare: (1) \\textit{Naive} (no correction), (2) \\textit{Global} (pooled confusion matrix, equivalent to PPI/DSL~\\cite{angelopoulos2023ppi,egami2024dsl} with homogeneous error), (3) \\textit{Stratified MLE} (per-subgroup DSL without shrinkage), (4) \\textit{HB EC-HTE} (our method), (5) \\textit{PPCI}~\\cite{sui2026ppci}, and (6) \\textit{EC-HTE+PPCI}.\nFor CausalForest~\\cite{wager2018causal}, we compare naive, global, and EC-HTE variants.\nPrimary metrics are $|\\text{bias}|$, RMSE, and 95\\% CI coverage, averaged across subgroups and 100 MC runs.\nRobustness validation covers hate speech, six OpenAI models, subgroup misspecification, asymmetric confusion matrices, confounded treatment, and outcome-dependent misclassification (all $\\geq$93.5\\% coverage; Appendices~\\ref{app:hatespeech}--\\ref{app:a1_sensitivity}).\n\n\\subsection{Empirical Validation of the Bias Identity}\n\\label{sec:bias_mechanism}\n\nWe verify Theorem~\\ref{thm:bias_identity} on a $K{=}2$ grid (520 configurations, $\\Delta\\pi \\in [0, 0.25]$, $\\Delta\\tau \\in (0, 0.50]$) and a $K{=}4$ grid (Appendix~\\ref{app:dgp}).\nRegressing observed subgroup bias on $\\delta_s \\cdot \\Delta\\tau / (1{-}2\\bar{\\pi})$ yields $R^2 = 0.994$ ($K{=}2$) and $0.974$ ($K{=}4$); residual variance reflects MC noise ($R^2 \\geq 0.976$ even at $P(Z{=}1) = 0.1$; Appendix~\\ref{app:classimbalance}).\nGlobal correction worsens bias in 50\\% of $K{=}2$ configurations (260/520, excluding $\\Delta\\pi{=}0$), with amplification reaching 2.86$\\times$ ($K{=}2$) and 2.41$\\times$ ($K{=}4$); Figure~\\ref{fig:heatmap} visualizes the amplification surface.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig2_heatmap.pdf}\n\\caption{Bias amplification under global correction ($K{=}2$). (a) Low-error subgroup: correction always helps. (b) High-error subgroup: correction \\emph{increases} bias when $\\Delta\\pi > 0.12$ (hatched), reaching 2.86$\\times$.}\n\\label{fig:heatmap}\n\\end{figure*}\n\n\\subsection{EC-HTE Evaluation}\n\\label{sec:ec_hte_eval}\n\nTable~\\ref{tab:main_results} presents the main results across representative configurations.\nNotably, in the $K{=}2$ extreme row, global correction \\emph{increases} $|\\text{bias}|$ relative to naive (0.059 vs.\\ 0.058)---a direct manifestation of Theorem~\\ref{thm:bias_identity}: pooled correction overshoots in low-error subgroups.\nHB EC-HTE reduces $|\\text{bias}|$ from 0.059 to 0.008 (7.4$\\times$) at $K{=}2$ and from 0.056 to 0.012 (4.7$\\times$) at $K{=}4$, maintaining near-nominal coverage (0.94--0.96) with lower RMSE than stratified MLE.\nUnder moderate heterogeneity ($K{=}2$), methods converge: EC-HTE and global achieve comparable bias ($p > 0.05$; Table~\\ref{tab:main_supp}).\nIn the semi-synthetic TweetEval experiment ($K{=}4$, $n_{\\text{expert}}{=}250$), EC-HTE and Global achieve comparable $|\\text{bias}|$ ($p{=}0.395$; Table~\\ref{tab:main_supp}), but EC-HTE incurs higher RMSE (0.225 vs.\\ 0.124), driven by moderate $\\Delta\\pi{=}0.20$ and unbalanced subgroups receiving ${\\sim}30$ expert labels each.\nWhen $\\Delta\\pi$ or per-subgroup budget is marginal, global correction is competitive on aggregate RMSE.\n\n\\paragraph{CausalForest.}\nWith CausalForest~\\cite{wager2018causal} ($K{=}4$, extreme, $n{=}500$), EC-HTE reduces $|\\text{bias}|$ from 0.191 to 0.039 (4.9$\\times$), improving coverage from 0.58 to 0.90; global correction amplifies naive bias up to 5.9$\\times$ because the forest magnifies label errors (Table~\\ref{tab:main_results}).\nThe residual coverage gap (90\\% vs.\\ oracle 94--96\\%) reflects asymmetric $M^{-1}$ SE propagation rather than CM estimation error; a full bootstrap SE can improve coverage calibration (Appendix~\\ref{app:bootstrap_se}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results (extreme heterogeneity). Metrics averaged over subgroups, $z$-levels, 100 MC runs. Bold: lowest $|\\text{bias}|$. $^\\dagger$RMSE exceeds Global. Moderate heterogeneity and TweetEval results---where methods converge and EC-HTE RMSE exceeds Global---in Table~\\ref{tab:main_supp}; MC SEs in Appendix~\\ref{app:mcse}.}\n\\label{tab:main_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll ccc}\n\\toprule\nConfiguration & Method & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{DIM\\\\$K{=}2$, $n{=}250$}}\n & Naive & 0.058 & 0.090 & 0.82 \\\\\n & Global & 0.059 & 0.099 & 0.87 \\\\\n & Strat.\\ MLE & 0.012 & 0.094 & 0.95 \\\\\n & HB EC-HTE & \\textbf{0.008} & 0.089 & 0.94 \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{DIM\\\\$K{=}4$, $n{=}500$}}\n & Naive & 0.062 & 0.113 & 0.88 \\\\\n & Global & 0.056 & 0.125 & 0.91 \\\\\n & Strat.\\ MLE & \\textbf{0.010} & 0.127$^\\dagger$ & 0.95 \\\\\n & HB EC-HTE & 0.012 & 0.120 & 0.96 \\\\\n\\midrule\n\\multirow{3}{*}{\\shortstack[l]{CausalForest\\\\$K{=}4$, $n{=}500$}}\n & Naive & 0.208 & 0.231 & 0.44 \\\\\n & Global & 0.191 & 0.244 & 0.58 \\\\\n & EC-HTE Forest & \\textbf{0.039} & 0.180 & 0.90 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Actionable Diagnostic Without EC-HTE}\n\\label{sec:diagnostic}\n\nProposition~\\ref{prop:debiasing_hurts} provides a $\\Delta\\tau$-free diagnostic: global correction increases bias in subgroup $s$ iff $|\\delta_s| / ((1-2\\bar{\\pi}) \\cdot \\pi_s) > 1$, computable from a pilot sample without estimating treatment effects.\nA threshold classifier achieves AUC = 0.86 at the subgroup level (Figure~\\ref{fig:roc}, Appendix).\nOn real LLM confusion matrices (16 combinations; Appendix~\\ref{app:screening}), AUC decreases to 0.63, primarily from subgroups with $\\tau_s \\approx 0$ where both naive and corrected bias are near zero, making the ground-truth harm label indeterminate; on subgroups with $\\tau_s > 0$, AUC reaches 1.0.\nFor $K{=}2$, $|\\delta_0|{=}|\\delta_1|$ forces ranking by $1/\\pi_s$ alone, which can anti-predict harm; reliability is strongest for $K{\\geq}4$.\nA computable meta-criterion recovers reliability: when $\\max_s \\mathrm{score}(s) > 1$, the diagnostic achieves AUC $\\geq 0.75$ across all 16 combinations; when $\\max_s \\mathrm{score}(s) \\leq 1$, AUC drops to 0.0--0.67 (Appendix~\\ref{app:screening}).\n\nA recommended practitioner workflow and budget crossover curves appear in Appendices~\\ref{sec:budget}--\\ref{app:screening}.\nAt $K{=}8$ with $n_{\\text{expert}}{=}250$, EC-HTE maintains nominal coverage (95.6\\%) but RMSE exceeds global correction, establishing a practical scalability boundary (Appendix~\\ref{app:k8_subgroups}).\nThe bias identity further validates across eight LLMs spanning 11 model--dataset combinations ($R^2 = 0.975$; Appendix~\\ref{app:multilm}).",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 80
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01QuyhLtixm5feR4TmQGCNdo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "ecd82984-a81c-40d4-97c0-38dcf386814f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxbidNY9Li64EvqEmWDDgD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14179,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14179
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-23T09:23:30.574Z_

<details><summary>↩ Tool result · `toolu_01QuyhLtixm5feR4TmQGCNdo`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	EC-HTE requires $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$ per subgroup for stable hierarchical Bayesian estimation.
5	For $K{=}2$, EC-HTE remains effective even at $P(Z{=}1) = 0.1$ (Appendix~\ref{app:classimbalance}); for $K{=}4$, $P(Z{=}1) \geq 0.3$ is needed to approach breakeven with global correction at $n_{\text{expert}}{=}250$.
6	Even above this threshold, stratification incurs a variance cost: at $K{=}4$, extreme heterogeneity, and $n_{\text{expert}} \leq 100$, CausalForest RMSE reaches 3.5$\times$ that of the naive estimator.
7	The method also requires moderate baseline classifier accuracy per subgroup; when any subgroup's FNR or FPR approaches 0.5, the confusion matrix row approaches a uniform distribution and inversion amplifies noise (Appendix~\ref{app:semireal}), as confirmed independently in the hate speech case study (Appendix~\ref{app:hatespeech}).
8	These failure modes interact: high per-subgroup error-rate variance combined with low minority prevalence $P(Z{=}1)$ jointly reduces effective per-subgroup expert labels for the positive class, compounding both sources of estimation error.
9	Additionally, our main semi-synthetic experiments use constant treatment effects across subgroups; a supplementary heterogeneous-$\tau$ DGP (Appendix~\ref{app:multilm_opensource}) shows that EC-HTE achieves targeted bias and RMSE improvement in subgroups with large $\Delta\tau$, though aggregate RMSE remains comparable to global correction.
10	At $K{=}8$ with $n_{\text{expert}}{=}250$ (${\approx}31$ labels/subgroup), EC-HTE maintains nominal coverage (95.6\%) but RMSE exceeds global correction, establishing $K{=}8$ as a scalability boundary under fixed budget (Appendix~\ref{app:k8_subgroups}).
11	Hierarchical pooling of confusion matrices across related subgroups may relax the per-subgroup budget requirement; we leave this extension to future work.
12	
13	Assumption~(A1) (conditional independence of misclassification and potential outcomes) is not empirically testable.
14	When LLM accuracy correlates with outcome magnitude---e.g., extreme sentiment is both easier to classify and associated with larger treatment effects---Theorem~\ref{thm:bias_identity} acquires an $O(\gamma)$ perturbation (Section~\ref{sec:theory}).
15	Sensitivity simulation (Appendix~\ref{app:a1_sensitivity}) shows that EC-HTE maintains near-nominal coverage ($\geq$93.5\%) under outcome-dependent misclassification up to $\gamma = 0.2$, with bias increasing only 13.7\%; developing a formal closed-form bound for the $O(\gamma)$ perturbation remains a natural extension~\cite{lash2009applying,dorn2022sharp}.
16	
17	Oracle experiments confirm CausalForest plug-in SE is well-calibrated (94--96\% coverage with true $Z$ labels); EC-HTE plug-in SE achieves 93.8\% aggregate coverage under standard hyperparameters ($n_{\text{estimators}}{=}200$), with residual under-coverage concentrated in high-error subgroups due to asymmetric $M^{-1}$ SE propagation.
18	A full bootstrap procedure ($B{=}100$; re-estimate CM and re-fit the forest per replicate) recovers exact nominal coverage (95.0\%) at a computational cost of ${\sim}1.5$ minutes per dataset (Appendix~\ref{app:bootstrap_se}).
19	For the DIM estimator, plug-in SE achieves $\geq$95\% coverage across all budgets.
20	
21	The diagnostic (Proposition~\ref{prop:debiasing_hurts}) achieves AUC $= 0.86$ under synthetic symmetric errors but degrades to $0.63$ on real LLM confusion matrices (pooled across 16 model--dataset combinations; Appendix~\ref{app:screening}).
22	For $K{=}2$, the diagnostic anti-predicts because $|\delta_0|{=}|\delta_1|$ forces score differentiation onto $1/\pi_s$ alone, which inversely correlates with actual harm; for binary $Z$, the asymmetric $B_s$-based formulation (Remark~2) is algebraically equivalent and offers no improvement.
23	Performance is strongest for $K{\geq}4$ with moderate asymmetry (AUC $= 0.82$; Appendix~\ref{app:asymmetric}).
24	The diagnostic remains a theoretically grounded criterion---the bias identity's product structure ensures it correctly identifies the \emph{direction} of bias amplification---but should be paired with $R^2$ validation of the bias identity rather than used as a standalone screening rule.
25	
26	All main experiments use symmetric error rates and additive CATE injection ($Y(1) = Y(0) + \tau(Z)$).
27	The bias identity (Theorem~\ref{thm:bias_identity}) generalizes to asymmetric confusion matrices (Appendix~\ref{app:asymmetric}, $R^2 = 0.991$) and derives from the confusion matrix structure rather than the outcome model.
28	While our main experiments use additive CATE injection, a supplementary experiment with multiplicative effects ($Y(1) = Y(0) \times \exp(\tau(Z))$) yields comparable bias reduction (52\%) and nominal coverage (0.955; Appendix~\ref{app:rlearner}), confirming robustness to the functional form of treatment effects.
29	EC-HTE further requires discrete, pre-defined subgroups; subgroup definitions should be pre-specified based on domain knowledge, as data-driven subgroup discovery risks overfitting the confusion matrix structure to sample-specific noise. Continuous effect modifiers or latent subgroup discovery settings require different approaches, and intersectional subgroups with many levels may exceed the $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$ budget threshold.
30	Our experiments define subgroups by text features (hashtag presence, text length); demographic subgroups---where prior work documents the most concerning disparities \citep{ashwin2025bias}---require sensitive data access beyond the scope of this study.
31	EC-HTE's correction mechanism is agnostic to subgroup definition: it corrects any per-subgroup confusion-matrix heterogeneity, whether defined by text features, demographics, or other covariates.
32	Ground-truth subgroup CATEs are unavailable in public datasets; classic causal inference benchmarks (e.g., LaLonde, IHDP) lack the LLM annotation step that creates the measurement error our method corrects, precluding direct application. We use synthetic CATE injection on real text features and real LLM annotations.
33	We leave full real-data validation---on a dataset combining RCT design, ground-truth CATEs, and LLM annotations---to future work as suitable public benchmarks become available.
34	Code and data generation scripts will be released upon acceptance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "8c75619e-583c-4d14-9f4d-659f48f377fb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex",
      "content": "\\section*{Limitations}\n\\label{sec:limitations}\n\nEC-HTE requires $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$ per subgroup for stable hierarchical Bayesian estimation.\nFor $K{=}2$, EC-HTE remains effective even at $P(Z{=}1) = 0.1$ (Appendix~\\ref{app:classimbalance}); for $K{=}4$, $P(Z{=}1) \\geq 0.3$ is needed to approach breakeven with global correction at $n_{\\text{expert}}{=}250$.\nEven above this threshold, stratification incurs a variance cost: at $K{=}4$, extreme heterogeneity, and $n_{\\text{expert}} \\leq 100$, CausalForest RMSE reaches 3.5$\\times$ that of the naive estimator.\nThe method also requires moderate baseline classifier accuracy per subgroup; when any subgroup's FNR or FPR approaches 0.5, the confusion matrix row approaches a uniform distribution and inversion amplifies noise (Appendix~\\ref{app:semireal}), as confirmed independently in the hate speech case study (Appendix~\\ref{app:hatespeech}).\nThese failure modes interact: high per-subgroup error-rate variance combined with low minority prevalence $P(Z{=}1)$ jointly reduces effective per-subgroup expert labels for the positive class, compounding both sources of estimation error.\nAdditionally, our main semi-synthetic experiments use constant treatment effects across subgroups; a supplementary heterogeneous-$\\tau$ DGP (Appendix~\\ref{app:multilm_opensource}) shows that EC-HTE achieves targeted bias and RMSE improvement in subgroups with large $\\Delta\\tau$, though aggregate RMSE remains comparable to global correction.\nAt $K{=}8$ with $n_{\\text{expert}}{=}250$ (${\\approx}31$ labels/subgroup), EC-HTE maintains nominal coverage (95.6\\%) but RMSE exceeds global correction, establishing $K{=}8$ as a scalability boundary under fixed budget (Appendix~\\ref{app:k8_subgroups}).\nHierarchical pooling of confusion matrices across related subgroups may relax the per-subgroup budget requirement; we leave this extension to future work.\n\nAssumption~(A1) (conditional independence of misclassification and potential outcomes) is not empirically testable.\nWhen LLM accuracy correlates with outcome magnitude---e.g., extreme sentiment is both easier to classify and associated with larger treatment effects---Theorem~\\ref{thm:bias_identity} acquires an $O(\\gamma)$ perturbation (Section~\\ref{sec:theory}).\nSensitivity simulation (Appendix~\\ref{app:a1_sensitivity}) shows that EC-HTE maintains near-nominal coverage ($\\geq$93.5\\%) under outcome-dependent misclassification up to $\\gamma = 0.2$, with bias increasing only 13.7\\%; developing a formal closed-form bound for the $O(\\gamma)$ perturbation remains a natural extension~\\cite{lash2009applying,dorn2022sharp}.\n\nOracle experiments confirm CausalForest plug-in SE is well-calibrated (94--96\\% coverage with true $Z$ labels); EC-HTE plug-in SE achieves 93.8\\% aggregate coverage under standard hyperparameters ($n_{\\text{estimators}}{=}200$), with residual under-coverage concentrated in high-error subgroups due to asymmetric $M^{-1}$ SE propagation.\nA full bootstrap procedure ($B{=}100$; re-estimate CM and re-fit the forest per replicate) recovers exact nominal coverage (95.0\\%) at a computational cost of ${\\sim}1.5$ minutes per dataset (Appendix~\\ref{app:bootstrap_se}).\nFor the DIM estimator, plug-in SE achieves $\\geq$95\\% coverage across all budgets.\n\nThe diagnostic (Proposition~\\ref{prop:debiasing_hurts}) achieves AUC $= 0.86$ under synthetic symmetric errors but degrades to $0.63$ on real LLM confusion matrices (pooled across 16 model--dataset combinations; Appendix~\\ref{app:screening}).\nFor $K{=}2$, the diagnostic anti-predicts because $|\\delta_0|{=}|\\delta_1|$ forces score differentiation onto $1/\\pi_s$ alone, which inversely correlates with actual harm; for binary $Z$, the asymmetric $B_s$-based formulation (Remark~2) is algebraically equivalent and offers no improvement.\nPerformance is strongest for $K{\\geq}4$ with moderate asymmetry (AUC $= 0.82$; Appendix~\\ref{app:asymmetric}).\nThe diagnostic remains a theoretically grounded criterion---the bias identity's product structure ensures it correctly identifies the \\emph{direction} of bias amplification---but should be paired with $R^2$ validation of the bias identity rather than used as a standalone screening rule.\n\nAll main experiments use symmetric error rates and additive CATE injection ($Y(1) = Y(0) + \\tau(Z)$).\nThe bias identity (Theorem~\\ref{thm:bias_identity}) generalizes to asymmetric confusion matrices (Appendix~\\ref{app:asymmetric}, $R^2 = 0.991$) and derives from the confusion matrix structure rather than the outcome model.\nWhile our main experiments use additive CATE injection, a supplementary experiment with multiplicative effects ($Y(1) = Y(0) \\times \\exp(\\tau(Z))$) yields comparable bias reduction (52\\%) and nominal coverage (0.955; Appendix~\\ref{app:rlearner}), confirming robustness to the functional form of treatment effects.\nEC-HTE further requires discrete, pre-defined subgroups; subgroup definitions should be pre-specified based on domain knowledge, as data-driven subgroup discovery risks overfitting the confusion matrix structure to sample-specific noise. Continuous effect modifiers or latent subgroup discovery settings require different approaches, and intersectional subgroups with many levels may exceed the $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$ budget threshold.\nOur experiments define subgroups by text features (hashtag presence, text length); demographic subgroups---where prior work documents the most concerning disparities \\citep{ashwin2025bias}---require sensitive data access beyond the scope of this study.\nEC-HTE's correction mechanism is agnostic to subgroup definition: it corrects any per-subgroup confusion-matrix heterogeneity, whether defined by text features, demographics, or other covariates.\nGround-truth subgroup CATEs are unavailable in public datasets; classic causal inference benchmarks (e.g., LaLonde, IHDP) lack the LLM annotation step that creates the measurement error our method corrects, precluding direct application. We use synthetic CATE injection on real text features and real LLM annotations.\nWe leave full real-data validation---on a dataset combining RCT design, ground-truth CATEs, and LLM annotations---to future work as suitable public benchmarks become available.\nCode and data generation scripts will be released upon acceptance.",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01GhifHGJdAz7dz9HxvetAmd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "81da687d-4fd7-4458-bfee-e0478840ab16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxbidNY9Li64EvqEmWDDgD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14179,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14179
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-23T09:23:31.045Z_

<details><summary>↩ Tool result · `toolu_01GhifHGJdAz7dz9HxvetAmd`</summary>

```text
1	% === Datasets ===
2	
3	@inproceedings{borkan2019nuanced,
4	  title={Nuanced Metrics for Measuring Unintended Bias with Real Data for Text Classification},
5	  author={Borkan, Daniel and Dixon, Lucas and Sorensen, Jeffrey and Thain, Nithum and Vasserman, Lucy},
6	  booktitle={Companion Proceedings of The 2019 World Wide Web Conference},
7	  pages={491--500},
8	  year={2019}
9	}
10	
11	% === Econometrics of Binary Misclassification ===
12	
13	@incollection{bound2001measurement,
14	  title={Measurement Error in Survey Data},
15	  author={Bound, John and Brown, Charles and Mathiowetz, Nancy},
16	  booktitle={Handbook of Econometrics},
17	  volume={5},
18	  pages={3705--3843},
19	  year={2001},
20	  publisher={Elsevier}
21	}
22	
23	@article{greenland1980effect,
24	  title={The Effect of Misclassification in the Presence of Covariates},
25	  author={Greenland, Sander},
26	  journal={American Journal of Epidemiology},
27	  volume={112},
28	  number={4},
29	  pages={564--569},
30	  year={1980}
31	}
32	
33	@article{frazis2003estimating,
34	  title={Estimating Linear Regressions with Mismeasured, Possibly Endogenous, Binary Explanatory Variables},
35	  author={Frazis, Harley and Loewenstein, Mark A.},
36	  journal={Journal of Econometrics},
37	  volume={117},
38	  number={1},
39	  pages={151--178},
40	  year={2003}
41	}
42	
43	@article{black2000racial,
44	  title={The Impact of Economic Conditions on Participation in Disability Programs: Evidence from the Coal Boom and Bust},
45	  author={Black, Dan and Daniel, Kermit and Sanders, Seth},
46	  journal={American Economic Review},
47	  volume={90},
48	  number={1},
49	  pages={27--50},
50	  year={2000}
51	}
52	
53	@article{mahajan2006identification,
54	  title={Identification and Estimation of Regression Models with Misclassification},
55	  author={Mahajan, Aprajit},
56	  journal={Econometrica},
57	  volume={74},
58	  number={3},
59	  pages={631--665},
60	  year={2006}
61	}
62	
63	@article{lewbel2007estimation,
64	  title={Estimation of Average Treatment Effects with Misclassification},
65	  author={Lewbel, Arthur},
66	  journal={Econometrica},
67	  volume={75},
68	  number={2},
69	  pages={537--551},
70	  year={2007}
71	}
72	
73	% === Classical Measurement Error ===
74	
75	@article{blackwell2017unified,
76	  title={A Unified Approach to Measurement Error and Missing Data: Overview and Applications},
77	  author={Blackwell, Matthew and Honaker, James and King, Gary},
78	  journal={Sociological Methods \& Research},
79	  volume={46},
80	  number={3},
81	  pages={303--341},
82	  year={2017},
83	  doi={10.1177/0049124115585360}
84	}
85	
86	@book{fuller1987measurement,
87	  title={Measurement Error Models},
88	  author={Fuller, Wayne A.},
89	  year={1987},
90	  publisher={Wiley},
91	  address={New York}
92	}
93	
94	@book{carroll2006measurement,
95	  title={Measurement Error in Nonlinear Models: A Modern Perspective},
96	  author={Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu, Ciprian M.},
97	  year={2006},
98	  edition={2nd},
99	  publisher={Chapman \& Hall/CRC},
100	  address={Boca Raton, FL}
101	}
102	
103	@book{gustafson2003measurement,
104	  title={Measurement Error and Misclassification in Statistics and Epidemiology: Impacts and Bayesian Adjustments},
105	  author={Gustafson, Paul},
106	  year={2003},
107	  publisher={Chapman \& Hall/CRC},
108	  address={Boca Raton, FL},
109	  doi={10.1201/9780203502761}
110	}
111	
112	@article{hu2008nonparametric,
113	  title={Instrumental Variable Treatment of Nonclassical Measurement Error Models},
114	  author={Hu, Yingyao and Schennach, Susanne M.},
115	  journal={Econometrica},
116	  volume={76},
117	  number={1},
118	  pages={195--216},
119	  year={2008},
120	  doi={10.1111/j.0012-9682.2008.00823.x}
121	}
122	
123	% === Bayesian Annotation Models ===
124	
125	@article{dawid1979maximum,
126	  title={Maximum Likelihood Estimation of Observer Error-Rates Using the {EM} Algorithm},
127	  author={Dawid, A. Philip and Skene, Allan M.},
128	  journal={Applied Statistics},
129	  volume={28},
130	  number={1},
131	  pages={20--28},
132	  year={1979},
133	  doi={10.2307/2346806}
134	}
135	
136	@article{passonneau2014benefits,
137	  title={The Benefits of a Model of Annotation},
138	  author={Passonneau, Rebecca J. and Carpenter, Bob},
139	  journal={Transactions of the Association for Computational Linguistics},
140	  volume={2},
141	  pages={311--326},
142	  year={2014},
143	  doi={10.1162/tacl_a_00185}
144	}
145	
146	@inproceedings{hovy2013learning,
147	  title={Learning Whom to Trust with {MACE}},
148	  author={Hovy, Dirk and Berg-Kirkpatrick, Taylor and Vaswani, Ashish and Hovy, Eduard},
149	  booktitle={Proceedings of NAACL-HLT},
150	  pages={1120--1130},
151	  year={2013}
152	}
153	
154	@article{paun2018comparing,
155	  title={Comparing {B}ayesian Models of Annotation},
156	  author={Paun, Silviu and Carpenter, Bob and Chamberlain, Jon and Hovy, Dirk and Kruschwitz, Udo and Poesio, Massimo},
157	  journal={Transactions of the Association for Computational Linguistics},
158	  volume={6},
159	  pages={571--585},
160	  year={2018},
161	  doi={10.1162/tacl_a_00040}
162	}
163	
164	% === Causal Inference & HTE ===
165	
166	@article{athey2016recursive,
167	  title={Recursive Partitioning for Heterogeneous Causal Effects},
168	  author={Athey, Susan and Imbens, Guido},
169	  journal={Proceedings of the National Academy of Sciences},
170	  volume={113},
171	  number={27},
172	  pages={7353--7360},
173	  year={2016},
174	  doi={10.1073/pnas.1510489113}
175	}
176	
177	@article{wager2018causal,
178	  title={Estimation and Inference of Heterogeneous Treatment Effects using Random Forests},
179	  author={Wager, Stefan and Athey, Susan},
180	  journal={Journal of the American Statistical Association},
181	  volume={113},
182	  number={523},
183	  pages={1228--1242},
184	  year={2018},
185	  doi={10.1080/01621459.2017.1319839}
186	}
187	
188	@article{chernozhukov2018dml,
189	  title={Double/Debiased Machine Learning for Treatment and Structural Parameters},
190	  author={Chernozhukov, Victor and Chetverikov, Denis and Demirer, Mert and Duflo, Esther and Hansen, Christian and Newey, Whitney and Robins, James},
191	  journal={The Econometrics Journal},
192	  volume={21},
193	  number={1},
194	  pages={C1--C68},
195	  year={2018},
196	  doi={10.1111/ectj.12097}
197	}
198	
199	@article{kennedy2023dr,
200	  title={Towards Optimal Doubly Robust Estimation of Heterogeneous Causal Effects},
201	  author={Kennedy, Edward H.},
202	  journal={Electronic Journal of Statistics},
203	  volume={17},
204	  number={2},
205	  pages={3008--3049},
206	  year={2023},
207	  doi={10.1214/23-EJS2157}
208	}
209	
210	@article{kunzel2019metalearners,
211	  title={Metalearners for Estimating Heterogeneous Treatment Effects Using Machine Learning},
212	  author={K{\"u}nzel, S{\"o}ren R. and Sekhon, Jasjeet S. and Bickel, Peter J. and Yu, Bin},
213	  journal={Proceedings of the National Academy of Sciences},
214	  volume={116},
215	  number={10},
216	  pages={4156--4165},
217	  year={2019},
218	  doi={10.1073/pnas.1804597116}
219	}
220	
221	@article{imai2010causal,
222	  title={Causal Inference with Differential Measurement Error: Nonparametric Identification and Sensitivity Analysis},
223	  author={Imai, Kosuke and Yamamoto, Teppei},
224	  journal={American Journal of Political Science},
225	  volume={54},
226	  number={4},
227	  pages={926--943},
228	  year={2010},
229	  doi={10.1111/j.1540-5907.2010.00446.x}
230	}
231	
232	% === LLMs as Annotators ===
233	
234	@article{gilardi2023chatgpt,
235	  title={{ChatGPT} Outperforms Crowd-Workers for Text-Annotation Tasks},
236	  author={Gilardi, Fabrizio and Alizadeh, Meysam and Kubli, Ma{\"e}l},
237	  journal={Proceedings of the National Academy of Sciences},
238	  volume={120},
239	  number={30},
240	  pages={e2305016120},
241	  year={2023},
242	  doi={10.1073/pnas.2305016120}
243	}
244	
245	@article{tornberg2024chatgpt,
246	  title={Large Language Models Outperform Expert Coders and Supervised Classifiers at Annotating Political Social Media Messages},
247	  author={T{\"o}rnberg, Petter},
248	  journal={Social Science Computer Review},
249	  year={2025},
250	  doi={10.1177/08944393241286471},
251	  publisher={SAGE Publications}
252	}
253	
254	@article{ziems2024nlp,
255	  title={Can Large Language Models Transform Computational Social Science?},
256	  author={Ziems, Caleb and Held, William and Shaikh, Omar and Chen, Jiaao and Zhang, Zhehao and Yang, Diyi},
257	  journal={Computational Linguistics},
258	  volume={50},
259	  number={1},
260	  pages={237--291},
261	  year={2024},
262	  doi={10.1162/coli_a_00502}
263	}
264	
265	@article{pangakis2023automated,
266	  title={Automated Annotation with Generative {AI} Requires Validation},
267	  author={Pangakis, Nicholas and Wolken, Samuel and Fasching, Neil},
268	  journal={arXiv preprint arXiv:2306.00176},
269	  year={2023}
270	}
271	
272	@article{ashwin2025bias,
273	  title={Using Large Language Models for Qualitative Analysis can Introduce Serious Bias},
274	  author={Ashwin, Aditya and Swanson, Becca and Blair, Robert and Samii, Cyrus},
275	  journal={Sociological Methods \& Research},
276	  year={2025},
277	  doi={10.1177/00491241251313793}
278	}
279	
280	% === PPI / DSL / Correction Methods ===
281	
282	@article{angelopoulos2023ppi,
283	  title={Prediction-Powered Inference},
284	  author={Angelopoulos, Anastasios N. and Bates, Stephen and Cand{\`e}s, Emmanuel J. and Jordan, Michael I. and Lei, Lihua},
285	  journal={Science},
286	  volume={382},
287	  number={6671},
288	  pages={669--674},
289	  year={2023},
290	  doi={10.1126/science.adi6000}
291	}
292	
293	@article{messing2026hidden,
294	  title={Hidden Measurement Error in {LLM} Pipelines Distorts Annotation, Evaluation, and Benchmarking},
295	  author={Messing, Solomon},
296	  journal={arXiv preprint arXiv:2604.11581},
297	  year={2026}
298	}
299	
300	@article{zrnic2024cross,
301	  title={Cross-Prediction-Powered Inference},
302	  author={Zrnic, Tijana and Cand{\`e}s, Emmanuel J.},
303	  journal={Proceedings of the National Academy of Sciences},
304	  volume={121},
305	  number={15},
306	  pages={e2322083121},
307	  year={2024},
308	  doi={10.1073/pnas.2322083121}
309	}
310	
311	@inproceedings{zrnic2024active,
312	  title={Active Statistical Inference},
313	  author={Zrnic, Tijana and Cand{\`e}s, Emmanuel J.},
314	  booktitle={Proceedings of the 41st International Conference on Machine Learning (ICML)},
315	  series={PMLR},
316	  volume={235},
317	  year={2024}
318	}
319	
320	@inproceedings{egami2024dsl,
321	  title={Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models},
322	  author={Egami, Naoki and Hinck, Musashi and Stewart, Brandon and Wei, Hanying},
323	  booktitle={Advances in Neural Information Processing Systems},
324	  volume={37},
325	  year={2024}
326	}
327	
328	@article{mozer2026ppi,
329	  title={{PPI} is the Difference Estimator: Recognizing the Survey Sampling Roots of Prediction-Powered Inference},
330	  author={Mozer, Reagan},
331	  journal={arXiv preprint arXiv:2603.19160},
332	  year={2026}
333	}
334	
335	@article{sui2026ppci,
336	  title={Prediction-Powered Conditional Inference},
337	  author={Sui, Yijun and Cand{\`e}s, Emmanuel J.},
338	  journal={arXiv preprint arXiv:2603.05575},
339	  year={2026}
340	}
341	
342	@article{bu2023forestiv,
343	  title={Achieving Reliable Causal Inference with Data-Mined Variables: A Random Forest Approach to the Measurement Error Problem},
344	  author={Bu, Zhexin and Almond, David and Bhatt, Siddhartha and Goldsmith-Pinkham, Paul},
345	  journal={INFORMS Journal on Data Science},
346	  volume={2},
347	  number={2},
348	  pages={110--129},
349	  year={2023},
350	  doi={10.1287/ijds.2023.0026}
351	}
352	
353	@article{fong2021machine,
354	  title={Machine Learning Predictions as Regression Covariates},
355	  author={Fong, Christian and Tyler, Matthew},
356	  journal={Political Analysis},
357	  volume={29},
358	  number={1},
359	  pages={48--64},
360	  year={2021},
361	  doi={10.1017/pan.2020.11}
362	}
363	
364	% === CSS Methodology ===
365	
366	@book{grimmer2022text,
367	  title={Text as Data: A New Framework for Machine Learning and the Social Sciences},
368	  author={Grimmer, Justin and Roberts, Margaret E. and Stewart, Brandon M.},
369	  year={2022},
370	  publisher={Princeton University Press},
371	  address={Princeton, NJ}
372	}
373	
374	@article{audinet2025benchmarking,
375	  title={Benchmarking Debiasing Methods for {LLM}-based Parameter Estimates},
376	  author={Audinet de Pieuchon, Josias and Egami, Naoki and Alizadeh, Meysam and Gilardi, Fabrizio},
377	  journal={Proceedings of EMNLP},
378	  year={2025}
379	}
380	
381	% === Semi-synthetic Data Source ===
382	
383	@inproceedings{barbieri2020tweeteval,
384	  title={{TweetEval}: Unified Benchmark and Comparative Evaluation for Tweet Classification},
385	  author={Barbieri, Francesco and Camacho-Collados, Jose and Espinosa-Anke, Luis and Neves, Leonardo},
386	  booktitle={Findings of EMNLP},
387	  pages={1644--1650},
388	  year={2020},
389	  doi={10.18653/v1/2020.findings-emnlp.148}
390	}
391	
392	@article{wang2020methods,
393	  title={Methods for Correcting Inference Based on Outcomes Predicted by Machine Learning},
394	  author={Wang, Siruo and McCormick, Tyler H. and Leek, Jeffrey T.},
395	  journal={Proceedings of the National Academy of Sciences},
396	  volume={117},
397	  number={48},
398	  pages={30266--30275},
399	  year={2020}
400	}
401	
402	@article{feder2022causal,
403	  title={Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond},
404	  author={Feder, Amir and Keith, Katherine A. and Manzoor, Emaad and Pryzant, Reid and Sridhar, Dhanya and Wood-Doughty, Zach and Eisenstein, Jacob and Grimmer, Justin and Reichart, Roi and Roberts, Margaret E. and Stewart, Brandon M. and Veitch, Victor and Yang, Diyi},
405	  journal={Transactions of the Association for Computational Linguistics},
406	  volume={10},
407	  pages={1171--1197},
408	  year={2022}
409	}
410	
411	@inproceedings{keith2020text,
412	  title={Text and Causal Inference: A Review of Using Text to Remove Confounding from Causal Estimates},
413	  author={Keith, Katherine A. and Jensen, David and O'Connor, Brendan},
414	  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
415	  pages={5332--5344},
416	  year={2020}
417	}
418	
419	% === HTE Estimation ===
420	
421	@article{semenova2021debiased,
422	  title={Debiased Machine Learning of Conditional Average Treatment Effects and Other Causal Functions},
423	  author={Semenova, Vira and Chernozhukov, Victor},
424	  journal={The Econometrics Journal},
425	  volume={24},
426	  number={2},
427	  pages={264--289},
428	  year={2021},
429	  doi={10.1093/ectj/utaa027}
430	}
431	
432	@article{nie2021quasi,
433	  title={Quasi-Oracle Estimation of Heterogeneous Treatment Effects},
434	  author={Nie, Xinkun and Wager, Stefan},
435	  journal={Biometrika},
436	  volume={108},
437	  number={2},
438	  pages={299--319},
439	  year={2021},
440	  doi={10.1093/biomet/asaa076}
441	}
442	
443	% === Sensitivity Analysis for Misclassification ===
444	
445	@book{lash2009applying,
446	  title={Applying Quantitative Bias Analysis to Epidemiologic Data},
447	  author={Lash, Timothy L. and Fox, Matthew P. and Fink, Aliza K.},
448	  publisher={Springer},
449	  address={New York},
450	  year={2009},
451	  doi={10.1007/978-0-387-87959-8}
452	}
453	
454	@article{dorn2022sharp,
455	  title={Sharp Sensitivity Analysis for Inverse Propensity Weighting via Quantile Balancing},
456	  author={Dorn, Jacob and Guo, Kevin and Kallus, Nathan},
457	  journal={Journal of the American Statistical Association},
458	  volume={118},
459	  number={544},
460	  pages={2645--2657},
461	  year={2023},
462	  doi={10.1080/01621459.2022.2064774}
463	}
464	
465	% === Treatment Effects + Measurement Error ===
466	
467	@article{ogburn2012nondifferential,
468	  title={On the Nondifferential Misclassification of a Binary Confounder},
469	  author={Ogburn, Elizabeth L. and VanderWeele, Tyler J.},
470	  journal={Epidemiology},
471	  volume={23},
472	  number={3},
473	  pages={433--439},
474	  year={2012},
475	  doi={10.1097/EDE.0b013e31824d1f63}
476	}
477	
478	@article{battistin2014treatment,
479	  title={Treatment Effect Estimation with Covariate Measurement Error},
480	  author={Battistin, Erich and Chesher, Andrew},
481	  journal={Journal of Econometrics},
482	  volume={178},
483	  number={2},
484	  pages={707--714},
485	  year={2014},
486	  doi={10.1016/j.jeconom.2013.10.006}
487	}
488	
489	% === Real-Data Datasets ===
490	
491	@article{kennedy2020constructing,
492	  title={Constructing Interval Variables via Faceted {Rasch} Measurement and Multitask Deep Learning: A Hate Speech Application},
493	  author={Kennedy, Chris J. and Bacon, Geoff and Sahn, Alexander and von Vacano, Claudia},
494	  journal={arXiv preprint arXiv:2009.10277},
495	  year={2020}
496	}
497	
498	@inproceedings{guo2017calibration,
499	  title={On Calibration of Modern Neural Networks},
500	  author={Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},
501	  booktitle={Proceedings of the 34th International Conference on Machine Learning},
502	  pages={1321--1330},
503	  year={2017}
504	}
505	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "cbad043a-81a2-4e1c-be9a-188cc2bdf2d9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib",
      "content": "% === Datasets ===\n\n@inproceedings{borkan2019nuanced,\n  title={Nuanced Metrics for Measuring Unintended Bias with Real Data for Text Classification},\n  author={Borkan, Daniel and Dixon, Lucas and Sorensen, Jeffrey and Thain, Nithum and Vasserman, Lucy},\n  booktitle={Companion Proceedings of The 2019 World Wide Web Conference},\n  pages={491--500},\n  year={2019}\n}\n\n% === Econometrics of Binary Misclassification ===\n\n@incollection{bound2001measurement,\n  title={Measurement Error in Survey Data},\n  author={Bound, John and Brown, Charles and Mathiowetz, Nancy},\n  booktitle={Handbook of Econometrics},\n  volume={5},\n  pages={3705--3843},\n  year={2001},\n  publisher={Elsevier}\n}\n\n@article{greenland1980effect,\n  title={The Effect of Misclassification in the Presence of Covariates},\n  author={Greenland, Sander},\n  journal={American Journal of Epidemiology},\n  volume={112},\n  number={4},\n  pages={564--569},\n  year={1980}\n}\n\n@article{frazis2003estimating,\n  title={Estimating Linear Regressions with Mismeasured, Possibly Endogenous, Binary Explanatory Variables},\n  author={Frazis, Harley and Loewenstein, Mark A.},\n  journal={Journal of Econometrics},\n  volume={117},\n  number={1},\n  pages={151--178},\n  year={2003}\n}\n\n@article{black2000racial,\n  title={The Impact of Economic Conditions on Participation in Disability Programs: Evidence from the Coal Boom and Bust},\n  author={Black, Dan and Daniel, Kermit and Sanders, Seth},\n  journal={American Economic Review},\n  volume={90},\n  number={1},\n  pages={27--50},\n  year={2000}\n}\n\n@article{mahajan2006identification,\n  title={Identification and Estimation of Regression Models with Misclassification},\n  author={Mahajan, Aprajit},\n  journal={Econometrica},\n  volume={74},\n  number={3},\n  pages={631--665},\n  year={2006}\n}\n\n@article{lewbel2007estimation,\n  title={Estimation of Average Treatment Effects with Misclassification},\n  author={Lewbel, Arthur},\n  journal={Econometrica},\n  volume={75},\n  number={2},\n  pages={537--551},\n  year={2007}\n}\n\n% === Classical Measurement Error ===\n\n@article{blackwell2017unified,\n  title={A Unified Approach to Measurement Error and Missing Data: Overview and Applications},\n  author={Blackwell, Matthew and Honaker, James and King, Gary},\n  journal={Sociological Methods \\& Research},\n  volume={46},\n  number={3},\n  pages={303--341},\n  year={2017},\n  doi={10.1177/0049124115585360}\n}\n\n@book{fuller1987measurement,\n  title={Measurement Error Models},\n  author={Fuller, Wayne A.},\n  year={1987},\n  publisher={Wiley},\n  address={New York}\n}\n\n@book{carroll2006measurement,\n  title={Measurement Error in Nonlinear Models: A Modern Perspective},\n  author={Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu, Ciprian M.},\n  year={2006},\n  edition={2nd},\n  publisher={Chapman \\& Hall/CRC},\n  address={Boca Raton, FL}\n}\n\n@book{gustafson2003measurement,\n  title={Measurement Error and Misclassification in Statistics and Epidemiology: Impacts and Bayesian Adjustments},\n  author={Gustafson, Paul},\n  year={2003},\n  publisher={Chapman \\& Hall/CRC},\n  address={Boca Raton, FL},\n  doi={10.1201/9780203502761}\n}\n\n@article{hu2008nonparametric,\n  title={Instrumental Variable Treatment of Nonclassical Measurement Error Models},\n  author={Hu, Yingyao and Schennach, Susanne M.},\n  journal={Econometrica},\n  volume={76},\n  number={1},\n  pages={195--216},\n  year={2008},\n  doi={10.1111/j.0012-9682.2008.00823.x}\n}\n\n% === Bayesian Annotation Models ===\n\n@article{dawid1979maximum,\n  title={Maximum Likelihood Estimation of Observer Error-Rates Using the {EM} Algorithm},\n  author={Dawid, A. Philip and Skene, Allan M.},\n  journal={Applied Statistics},\n  volume={28},\n  number={1},\n  pages={20--28},\n  year={1979},\n  doi={10.2307/2346806}\n}\n\n@article{passonneau2014benefits,\n  title={The Benefits of a Model of Annotation},\n  author={Passonneau, Rebecca J. and Carpenter, Bob},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={2},\n  pages={311--326},\n  year={2014},\n  doi={10.1162/tacl_a_00185}\n}\n\n@inproceedings{hovy2013learning,\n  title={Learning Whom to Trust with {MACE}},\n  author={Hovy, Dirk and Berg-Kirkpatrick, Taylor and Vaswani, Ashish and Hovy, Eduard},\n  booktitle={Proceedings of NAACL-HLT},\n  pages={1120--1130},\n  year={2013}\n}\n\n@article{paun2018comparing,\n  title={Comparing {B}ayesian Models of Annotation},\n  author={Paun, Silviu and Carpenter, Bob and Chamberlain, Jon and Hovy, Dirk and Kruschwitz, Udo and Poesio, Massimo},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={6},\n  pages={571--585},\n  year={2018},\n  doi={10.1162/tacl_a_00040}\n}\n\n% === Causal Inference & HTE ===\n\n@article{athey2016recursive,\n  title={Recursive Partitioning for Heterogeneous Causal Effects},\n  author={Athey, Susan and Imbens, Guido},\n  journal={Proceedings of the National Academy of Sciences},\n  volume={113},\n  number={27},\n  pages={7353--7360},\n  year={2016},\n  doi={10.1073/pnas.1510489113}\n}\n\n@article{wager2018causal,\n  title={Estimation and Inference of Heterogeneous Treatment Effects using Random Forests},\n  author={Wager, Stefan and Athey, Susan},\n  journal={Journal of the American Statistical Association},\n  volume={113},\n  number={523},\n  pages={1228--1242},\n  year={2018},\n  doi={10.1080/01621459.2017.1319839}\n}\n\n@article{chernozhukov2018dml,\n  title={Double/Debiased Machine Learning for Treatment and Structural Parameters},\n  author={Chernozhukov, Victor and Chetverikov, Denis and Demirer, Mert and Duflo, Esther and Hansen, Christian and Newey, Whitney and Robins, James},\n  journal={The Econometrics Journal},\n  volume={21},\n  number={1},\n  pages={C1--C68},\n  year={2018},\n  doi={10.1111/ectj.12097}\n}\n\n@article{kennedy2023dr,\n  title={Towards Optimal Doubly Robust Estimation of Heterogeneous Causal Effects},\n  author={Kennedy, Edward H.},\n  journal={Electronic Journal of Statistics},\n  volume={17},\n  number={2},\n  pages={3008--3049},\n  year={2023},\n  doi={10.1214/23-EJS2157}\n}\n\n@article{kunzel2019metalearners,\n  title={Metalearners for Estimating Heterogeneous Treatment Effects Using Machine Learning},\n  author={K{\\\"u}nzel, S{\\\"o}ren R. and Sekhon, Jasjeet S. and Bickel, Peter J. and Yu, Bin},\n  journal={Proceedings of the National Academy of Sciences},\n  volume={116},\n  number={10},\n  pages={4156--4165},\n  year={2019},\n  doi={10.1073/pnas.1804597116}\n}\n\n@article{imai2010causal,\n  title={Causal Inference with Differential Measurement Error: Nonparametric Identification and Sensitivity Analysis},\n  author={Imai, Kosuke and Yamamoto, Teppei},\n  journal={American Journal of Political Science},\n  volume={54},\n  number={4},\n  pages={926--943},\n  year={2010},\n  doi={10.1111/j.1540-5907.2010.00446.x}\n}\n\n% === LLMs as Annotators ===\n\n@article{gilardi2023chatgpt,\n  title={{ChatGPT} Outperforms Crowd-Workers for Text-Annotation Tasks},\n  author={Gilardi, Fabrizio and Alizadeh, Meysam and Kubli, Ma{\\\"e}l},\n  journal={Proceedings of the National Academy of Sciences},\n  volume={120},\n  number={30},\n  pages={e2305016120},\n  year={2023},\n  doi={10.1073/pnas.2305016120}\n}\n\n@article{tornberg2024chatgpt,\n  title={Large Language Models Outperform Expert Coders and Supervised Classifiers at Annotating Political Social Media Messages},\n  author={T{\\\"o}rnberg, Petter},\n  journal={Social Science Computer Review},\n  year={2025},\n  doi={10.1177/08944393241286471},\n  publisher={SAGE Publications}\n}\n\n@article{ziems2024nlp,\n  title={Can Large Language Models Transform Computational Social Science?},\n  author={Ziems, Caleb and Held, William and Shaikh, Omar and Chen, Jiaao and Zhang, Zhehao and Yang, Diyi},\n  journal={Computational Linguistics},\n  volume={50},\n  number={1},\n  pages={237--291},\n  year={2024},\n  doi={10.1162/coli_a_00502}\n}\n\n@article{pangakis2023automated,\n  title={Automated Annotation with Generative {AI} Requires Validation},\n  author={Pangakis, Nicholas and Wolken, Samuel and Fasching, Neil},\n  journal={arXiv preprint arXiv:2306.00176},\n  year={2023}\n}\n\n@article{ashwin2025bias,\n  title={Using Large Language Models for Qualitative Analysis can Introduce Serious Bias},\n  author={Ashwin, Aditya and Swanson, Becca and Blair, Robert and Samii, Cyrus},\n  journal={Sociological Methods \\& Research},\n  year={2025},\n  doi={10.1177/00491241251313793}\n}\n\n% === PPI / DSL / Correction Methods ===\n\n@article{angelopoulos2023ppi,\n  title={Prediction-Powered Inference},\n  author={Angelopoulos, Anastasios N. and Bates, Stephen and Cand{\\`e}s, Emmanuel J. and Jordan, Michael I. and Lei, Lihua},\n  journal={Science},\n  volume={382},\n  number={6671},\n  pages={669--674},\n  year={2023},\n  doi={10.1126/science.adi6000}\n}\n\n@article{messing2026hidden,\n  title={Hidden Measurement Error in {LLM} Pipelines Distorts Annotation, Evaluation, and Benchmarking},\n  author={Messing, Solomon},\n  journal={arXiv preprint arXiv:2604.11581},\n  year={2026}\n}\n\n@article{zrnic2024cross,\n  title={Cross-Prediction-Powered Inference},\n  author={Zrnic, Tijana and Cand{\\`e}s, Emmanuel J.},\n  journal={Proceedings of the National Academy of Sciences},\n  volume={121},\n  number={15},\n  pages={e2322083121},\n  year={2024},\n  doi={10.1073/pnas.2322083121}\n}\n\n@inproceedings{zrnic2024active,\n  title={Active Statistical Inference},\n  author={Zrnic, Tijana and Cand{\\`e}s, Emmanuel J.},\n  booktitle={Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  series={PMLR},\n  volume={235},\n  year={2024}\n}\n\n@inproceedings{egami2024dsl,\n  title={Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models},\n  author={Egami, Naoki and Hinck, Musashi and Stewart, Brandon and Wei, Hanying},\n  booktitle={Advances in Neural Information Processing Systems},\n  volume={37},\n  year={2024}\n}\n\n@article{mozer2026ppi,\n  title={{PPI} is the Difference Estimator: Recognizing the Survey Sampling Roots of Prediction-Powered Inference},\n  author={Mozer, Reagan},\n  journal={arXiv preprint arXiv:2603.19160},\n  year={2026}\n}\n\n@article{sui2026ppci,\n  title={Prediction-Powered Conditional Inference},\n  author={Sui, Yijun and Cand{\\`e}s, Emmanuel J.},\n  journal={arXiv preprint arXiv:2603.05575},\n  year={2026}\n}\n\n@article{bu2023forestiv,\n  title={Achieving Reliable Causal Inference with Data-Mined Variables: A Random Forest Approach to the Measurement Error Problem},\n  author={Bu, Zhexin and Almond, David and Bhatt, Siddhartha and Goldsmith-Pinkham, Paul},\n  journal={INFORMS Journal on Data Science},\n  volume={2},\n  number={2},\n  pages={110--129},\n  year={2023},\n  doi={10.1287/ijds.2023.0026}\n}\n\n@article{fong2021machine,\n  title={Machine Learning Predictions as Regression Covariates},\n  author={Fong, Christian and Tyler, Matthew},\n  journal={Political Analysis},\n  volume={29},\n  number={1},\n  pages={48--64},\n  year={2021},\n  doi={10.1017/pan.2020.11}\n}\n\n% === CSS Methodology ===\n\n@book{grimmer2022text,\n  title={Text as Data: A New Framework for Machine Learning and the Social Sciences},\n  author={Grimmer, Justin and Roberts, Margaret E. and Stewart, Brandon M.},\n  year={2022},\n  publisher={Princeton University Press},\n  address={Princeton, NJ}\n}\n\n@article{audinet2025benchmarking,\n  title={Benchmarking Debiasing Methods for {LLM}-based Parameter Estimates},\n  author={Audinet de Pieuchon, Josias and Egami, Naoki and Alizadeh, Meysam and Gilardi, Fabrizio},\n  journal={Proceedings of EMNLP},\n  year={2025}\n}\n\n% === Semi-synthetic Data Source ===\n\n@inproceedings{barbieri2020tweeteval,\n  title={{TweetEval}: Unified Benchmark and Comparative Evaluation for Tweet Classification},\n  author={Barbieri, Francesco and Camacho-Collados, Jose and Espinosa-Anke, Luis and Neves, Leonardo},\n  booktitle={Findings of EMNLP},\n  pages={1644--1650},\n  year={2020},\n  doi={10.18653/v1/2020.findings-emnlp.148}\n}\n\n@article{wang2020methods,\n  title={Methods for Correcting Inference Based on Outcomes Predicted by Machine Learning},\n  author={Wang, Siruo and McCormick, Tyler H. and Leek, Jeffrey T.},\n  journal={Proceedings of the National Academy of Sciences},\n  volume={117},\n  number={48},\n  pages={30266--30275},\n  year={2020}\n}\n\n@article{feder2022causal,\n  title={Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond},\n  author={Feder, Amir and Keith, Katherine A. and Manzoor, Emaad and Pryzant, Reid and Sridhar, Dhanya and Wood-Doughty, Zach and Eisenstein, Jacob and Grimmer, Justin and Reichart, Roi and Roberts, Margaret E. and Stewart, Brandon M. and Veitch, Victor and Yang, Diyi},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={10},\n  pages={1171--1197},\n  year={2022}\n}\n\n@inproceedings{keith2020text,\n  title={Text and Causal Inference: A Review of Using Text to Remove Confounding from Causal Estimates},\n  author={Keith, Katherine A. and Jensen, David and O'Connor, Brendan},\n  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},\n  pages={5332--5344},\n  year={2020}\n}\n\n% === HTE Estimation ===\n\n@article{semenova2021debiased,\n  title={Debiased Machine Learning of Conditional Average Treatment Effects and Other Causal Functions},\n  author={Semenova, Vira and Chernozhukov, Victor},\n  journal={The Econometrics Journal},\n  volume={24},\n  number={2},\n  pages={264--289},\n  year={2021},\n  doi={10.1093/ectj/utaa027}\n}\n\n@article{nie2021quasi,\n  title={Quasi-Oracle Estimation of Heterogeneous Treatment Effects},\n  author={Nie, Xinkun and Wager, Stefan},\n  journal={Biometrika},\n  volume={108},\n  number={2},\n  pages={299--319},\n  year={2021},\n  doi={10.1093/biomet/asaa076}\n}\n\n% === Sensitivity Analysis for Misclassification ===\n\n@book{lash2009applying,\n  title={Applying Quantitative Bias Analysis to Epidemiologic Data},\n  author={Lash, Timothy L. and Fox, Matthew P. and Fink, Aliza K.},\n  publisher={Springer},\n  address={New York},\n  year={2009},\n  doi={10.1007/978-0-387-87959-8}\n}\n\n@article{dorn2022sharp,\n  title={Sharp Sensitivity Analysis for Inverse Propensity Weighting via Quantile Balancing},\n  author={Dorn, Jacob and Guo, Kevin and Kallus, Nathan},\n  journal={Journal of the American Statistical Association},\n  volume={118},\n  number={544},\n  pages={2645--2657},\n  year={2023},\n  doi={10.1080/01621459.2022.2064774}\n}\n\n% === Treatment Effects + Measurement Error ===\n\n@article{ogburn2012nondifferential,\n  title={On the Nondifferential Misclassification of a Binary Confounder},\n  author={Ogburn, Elizabeth L. and VanderWeele, Tyler J.},\n  journal={Epidemiology},\n  volume={23},\n  number={3},\n  pages={433--439},\n  year={2012},\n  doi={10.1097/EDE.0b013e31824d1f63}\n}\n\n@article{battistin2014treatment,\n  title={Treatment Effect Estimation with Covariate Measurement Error},\n  author={Battistin, Erich and Chesher, Andrew},\n  journal={Journal of Econometrics},\n  volume={178},\n  number={2},\n  pages={707--714},\n  year={2014},\n  doi={10.1016/j.jeconom.2013.10.006}\n}\n\n% === Real-Data Datasets ===\n\n@article{kennedy2020constructing,\n  title={Constructing Interval Variables via Faceted {Rasch} Measurement and Multitask Deep Learning: A Hate Speech Application},\n  author={Kennedy, Chris J. and Bacon, Geoff and Sahn, Alexander and von Vacano, Claudia},\n  journal={arXiv preprint arXiv:2009.10277},\n  year={2020}\n}\n\n@inproceedings{guo2017calibration,\n  title={On Calibration of Modern Neural Networks},\n  author={Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle={Proceedings of the 34th International Conference on Machine Learning},\n  pages={1321--1330},\n  year={2017}\n}\n",
      "numLines": 505,
      "startLine": 1,
      "totalLines": 505
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the files read. Let me also search for "exact identity", "exact, not", "not a bound", "not an approximation", "exact finite-population" across all .tex files for H2, and search for "orthogonal" for H5.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "4abaeb80-f0f4-49fe-824b-162ff6d2d0dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PSypfxP9dYfkSWkJ8ghDSZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19808,
      "cache_read_input_tokens": 26020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19808
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 21_

Now let me scan for the patterns needed for H2 and H5 across all tex files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "e61e06fd-fd5b-45ec-a498-27bbce4bee89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PSypfxP9dYfkSWkJ8ghDSZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19808,
      "cache_read_input_tokens": 26020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19808
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Grep · `toolu_013HYs5UPKw63af9Uv6mtqJT`</summary>

```json
{
  "pattern": "exact identity|exact,? not|not a bound|not an approximation|exact finite.population",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "8c80b918-6d52-4ed2-af42-e42295f9deb2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PSypfxP9dYfkSWkJ8ghDSZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19808,
      "cache_read_input_tokens": 26020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19808
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-23T09:23:43.484Z_

<details><summary>↩ Tool result · `toolu_013HYs5UPKw63af9Uv6mtqJT`</summary>

```text
docs/paper/related_work.tex:9:Second, Theorem~\ref{thm:bias_identity} derives an exact identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.
docs/paper/theory.tex:38:Equations~\eqref{eq:bias_z0}--\eqref{eq:bias_z1} constitute an exact finite-population identity, not an asymptotic approximation or bound.
docs/paper/abstract.tex:4:We derive an exact bias identity showing that this correction-induced bias factors into each subgroup's deviation from the pooled error rate times the treatment effect heterogeneity---a finite-population identity, not a bound.
docs/paper/introduction.tex:14:This is not a bound but an exact population-level identity, verified empirically with $R^2 = 0.994$ ($K{=}2$) and $R^2 = 0.974$ ($K{=}4$) on synthetic grids, and $R^2 = 0.975$ across 11 real LLM confusion matrices spanning open-source and proprietary model families.
docs/paper/introduction.tex:34:    \item An exact bias identity (Theorem~\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup CATE bias proportional to each subgroup's misclassification deviation times the treatment effect heterogeneity---an exact finite-population identity with independent diagnostic value, verified at $R^2 \geq 0.97$ on synthetic grids and 11 real LLM confusion matrices (Sections~\ref{sec:theory},~\ref{sec:bias_mechanism}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "d13f8b39-659d-4686-98c9-cf177e3f83cb",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:9:Second, Theorem~\\ref{thm:bias_identity} derives an exact identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.\ndocs/paper/theory.tex:38:Equations~\\eqref{eq:bias_z0}--\\eqref{eq:bias_z1} constitute an exact finite-population identity, not an asymptotic approximation or bound.\ndocs/paper/abstract.tex:4:We derive an exact bias identity showing that this correction-induced bias factors into each subgroup's deviation from the pooled error rate times the treatment effect heterogeneity---a finite-population identity, not a bound.\ndocs/paper/introduction.tex:14:This is not a bound but an exact population-level identity, verified empirically with $R^2 = 0.994$ ($K{=}2$) and $R^2 = 0.974$ ($K{=}4$) on synthetic grids, and $R^2 = 0.975$ across 11 real LLM confusion matrices spanning open-source and proprietary model families.\ndocs/paper/introduction.tex:34:    \\item An exact bias identity (Theorem~\\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup CATE bias proportional to each subgroup's misclassification deviation times the treatment effect heterogeneity---an exact finite-population identity with independent diagnostic value, verified at $R^2 \\geq 0.97$ on synthetic grids and 11 real LLM confusion matrices (Sections~\\ref{sec:theory},~\\ref{sec:bias_mechanism}).",
    "numLines": 5
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Grep · `toolu_01DRbgN9CEkAQUYSukH1rKBB`</summary>

```json
{
  "pattern": "orthogonal",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "bb58fb34-dd0e-4d4c-bf51-5e6260515c98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PSypfxP9dYfkSWkJ8ghDSZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19808,
      "cache_read_input_tokens": 26020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19808
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-23T09:23:45.171Z_

<details><summary>↩ Tool result · `toolu_01DRbgN9CEkAQUYSukH1rKBB`</summary>

```text
docs/paper/appendix.tex:517:The orthogonality of EC-HTE and PPCI follows from the distinct error sources they correct: EC-HTE addresses misclassification in the effect modifier $Z$ (covariate space), while PPCI corrects specification error in the outcome model $f(X)$ (prediction space).
docs/paper/appendix.tex:518:Since covariate misclassification and outcome model error are algebraically independent in the potential outcomes framework, their corrections compose without interference---confirmed by the 4-DGP orthogonal design (Table~\ref{tab:ppci}), where DGP~C (both errors present) yields the largest bias reduction from the combined approach.
docs/paper/appendix.tex:1236:\caption{EC-HTE coverage across confounding strengths and propensity sources. The logistic regression propensity model is correctly specified; propensity misspecification is an orthogonal concern addressed by the IPW literature.}
docs/paper/appendix.tex:1349:Calibrated + EC-HTE achieves the highest coverage (96.5\%), demonstrating that calibration and EC-HTE address orthogonal error sources: calibration reduces per-subgroup $\pi_s$ while EC-HTE corrects the residual $\delta_s$-driven bias from heterogeneity that persists post-calibration.
docs/paper/appendix.tex:1350:Propensity estimation robustness under model misspecification is an orthogonal concern addressed by the IPW literature; EC-HTE as a downstream correction layer does not alter IPW behavior.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "6566a0ff-40c6-458a-8a00-6019c4665468",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/appendix.tex:517:The orthogonality of EC-HTE and PPCI follows from the distinct error sources they correct: EC-HTE addresses misclassification in the effect modifier $Z$ (covariate space), while PPCI corrects specification error in the outcome model $f(X)$ (prediction space).\ndocs/paper/appendix.tex:518:Since covariate misclassification and outcome model error are algebraically independent in the potential outcomes framework, their corrections compose without interference---confirmed by the 4-DGP orthogonal design (Table~\\ref{tab:ppci}), where DGP~C (both errors present) yields the largest bias reduction from the combined approach.\ndocs/paper/appendix.tex:1236:\\caption{EC-HTE coverage across confounding strengths and propensity sources. The logistic regression propensity model is correctly specified; propensity misspecification is an orthogonal concern addressed by the IPW literature.}\ndocs/paper/appendix.tex:1349:Calibrated + EC-HTE achieves the highest coverage (96.5\\%), demonstrating that calibration and EC-HTE address orthogonal error sources: calibration reduces per-subgroup $\\pi_s$ while EC-HTE corrects the residual $\\delta_s$-driven bias from heterogeneity that persists post-calibration.\ndocs/paper/appendix.tex:1350:Propensity estimation robustness under model misspecification is an orthogonal concern addressed by the IPW literature; EC-HTE as a downstream correction layer does not alter IPW behavior.",
    "numLines": 5
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Grep · `toolu_0147619BmXFU9VQ3CURvFNGf`</summary>

```json
{
  "pattern": "tornberg|Törnberg",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "736363a5-5112-4855-bdc3-1ef1a85063c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PSypfxP9dYfkSWkJ8ghDSZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19808,
      "cache_read_input_tokens": 26020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19808
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-23T09:23:46.097Z_

<details><summary>↩ Tool result · `toolu_0147619BmXFU9VQ3CURvFNGf`</summary>

```text
245:@article{tornberg2024chatgpt,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "15bfd9da-875b-4210-b605-1461c882b14c",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "245:@article{tornberg2024chatgpt,",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze all findings:

**H1. Abstract**: Need to remove "5$\times$" (line 2), "5.9$\times$" (line 3), keep: "50\%", "7.4$\times$", "AUC $= 1.0$", "$\geq$0.90". Also need to remove other numbers. Let me re-read the abstract carefully:

Line 2: "by up to 5$\times$" - REMOVE
Line 3: "50\% of configurations" - KEEP
Line 3: "amplification up to 5.9$\times$" - REMOVE


Line 4: "exact bias identity" - keep
Line 5: "AUC $= 1.0$" - KEEP
Line 6: "7.4$\times$" - KEEP
Line 6: "$\geq$0.90" - KEEP
Line 6: "520 synthetic configurations" - REMOVE
Line 6: "eight LLMs" - REMOVE since the task specifies keeping only 4 numbers total

**H2. Checking "exact identity" locations**

Now I'm going through where "exact identity" appears across the files. In related_work.tex, I should shift from "exact identity for correction-induced bias" to "bias decomposition identity" to be more precise. Theorem 1 in theory.tex keeps the exact phrasing since that's a core theoretical result. For the abstract, I'll drop "exact" and focus on the decomposition aspect—showing how correction-induced bias factors into subgroup deviations and treatment effect heterogeneity. The introduction's statement about this being a population-level identity rather than a bound stays as is.

But I need to catch the other instances too. Line 34 in introduction.tex should become "a bias identity with independent diagnostic value" instead of "exact finite-population identity." And theory.tex line 79 where it says the theorem is an exact population identity—that needs to change to just "bias identity" since we're only keeping the exact language in the Theorem 1 statement itself. I need to check if "exact population identity" on line 79 matches the search patterns—it has "exact" and "identity" but with "population" in between, so it might not have shown up in my grep. Let me verify whether this variant needs to be included in the replacements.

Looking through theory.tex more carefully, I'm finding several instances of "exact" that need review: line 13 has "exact product form" which is fine as mathematical terminology, line 38 has the full phrase "exact finite-population identity, not an asymptotic approximation or bound" which definitely needs changing, line 52 says "holds exactly" which is acceptable, and line 79 with "exact population identity" should probably be changed. The abstract also has "exact bias identity" on line 4 that needs attention, and intro.tex line 12 has another instance I should examine more closely.

Going through intro.tex, line 12 states "We formalize this problem and derive an exact bias identity for the correction-induced error" which should be changed, while line 14 says "This is not a bound but an exact population-level identity" which I should keep as the first mention. Line 34 has both "exact bias identity" and "exact finite-population identity" that need changing, and related_work.tex line 9 has "exact identity" that should go.

Wait, I need to reconsider the actual task constraints. The instructions say to keep only 2 instances: the Theorem 1 formal statement in theory.tex and the first mention around line 14 in introduction.tex. So theory.tex line 38 near Theorem 1 stays, introduction.tex line 14 stays, and everything else gets changed.

Now I'm going through the specific replacements: abstract.tex line 4 changes "exact bias identity" to "bias identity" and removes "not a bound"; introduction.tex line 12 drops "exact" from "exact bias identity"; line 34 changes both instances to just "bias identity"; related_work.tex line 9 changes "exact identity" to "bias identity"; and theory.tex line 79 changes "exact population identity" to either "population-level identity" or "bias identity".

For the "not a bound" expressions, I'm keeping only two instances total—abstract.tex line 4 gets it removed, while theory.tex line 38 keeps "not an asymptotic approximation or bound".

I also need to add three bibliography entries and three sentences to related_work.tex, plus a cross-reference line in theory.tex after the proof sketch that cites frazis2003estimating.

For the orthogonal → complementary changes, appendix.tex line 517 changes "orthogonality of EC-HTE and PPCI" to "complementarity of EC-HTE and PPCI", while line 518's "4-DGP orthogonal design" is about experimental design factors being orthogonal, so that one might need different handling.

At line 1236, "orthogonal concern" describes propensity misspecification as an independent issue—I'm changing this to "complementary concern" since the task specifies replacing method-relationship uses with complementary forms, even though "separate concern" might be more precise semantically.

For line 1349, "orthogonal error sources" becomes "complementary error sources," and line 1350's "an orthogonal concern" becomes "a complementary concern" to indicate the IPW literature addresses a related but distinct issue.

I've verified that related_work.tex already uses "complementary" appropriately and doesn't contain other "orthogonal" instances that need changing. Now I'm checking the Table 1 header in experiments.tex around line 46.

Generating markdown table...

I'm noticing the Törnberg entry has a mismatch—the citation key says "tornberg2024chatgpt" but the year field is set to 2025, when it should be 2024 based on the original publication. Looking at the DOI structure and the citation key, there's a discrepancy between the year field showing 2025 and the key indicating 2024. Since the task specifies the correct year should be 2024, I'll update that field accordingly.

Now I need to check the appendix.tex file for the orthogonal replacement lines that need to be modified.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "9922e4d2-f838-4215-b7bb-026d46c048a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ENjutZQwnUW6T1r5yVhKYs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1545,
      "cache_read_input_tokens": 45828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1545
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 29_

Let me also check for more "exact" patterns and read the appendix lines for the orthogonal replacements.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "edbd4b46-e162-49ee-bcb6-27355d64ef94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ENjutZQwnUW6T1r5yVhKYs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1545,
      "cache_read_input_tokens": 45828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1545
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Grep · `toolu_01JsLAJMAJjso1R5C1ANUip9`</summary>

```json
{
  "pattern": "\\bexact\\b",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "8ee55984-442c-48d1-9c38-7f6f243af865",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ENjutZQwnUW6T1r5yVhKYs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1545,
      "cache_read_input_tokens": 45828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1545
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-23T09:25:07.826Z_

<details><summary>↩ Tool result · `toolu_01JsLAJMAJjso1R5C1ANUip9`</summary>

```text
docs/paper/related_work.tex:9:Second, Theorem~\ref{thm:bias_identity} derives an exact identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.
docs/paper/related_work.tex:35:\citet{imai2010causal} study treatment misclassification, requiring instrumental variables or partial identification; our problem is structurally distinct because the treatment is observed correctly but the effect modifier is misclassified, admitting exact correction through confusion matrices rather than bounds.
docs/paper/conclusion.tex:3:We derived an exact bias identity (Theorem~\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup-level bias proportional to $\delta_s \cdot \Delta\tau$, worsening CATE estimates in 50\% of $K{=}2$ configurations.
docs/paper/theory.tex:13:We show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.
docs/paper/theory.tex:38:Equations~\eqref{eq:bias_z0}--\eqref{eq:bias_z1} constitute an exact finite-population identity, not an asymptotic approximation or bound.
docs/paper/theory.tex:79:Theorem~\ref{thm:bias_identity} is an exact population identity.
docs/paper/limitations.tex:18:A full bootstrap procedure ($B{=}100$; re-estimate CM and re-fit the forest per replicate) recovers exact nominal coverage (95.0\%) at a computational cost of ${\sim}1.5$ minutes per dataset (Appendix~\ref{app:bootstrap_se}).
docs/paper/abstract.tex:4:We derive an exact bias identity showing that this correction-induced bias factors into each subgroup's deviation from the pooled error rate times the treatment effect heterogeneity---a finite-population identity, not a bound.
docs/paper/appendix.tex:229:The ATE remains identified; only conditional effects are biased, which makes exact correction through confusion matrix inversion feasible.
docs/paper/appendix.tex:233:\citet{frazis2003estimating} derive exact bias formulas for OLS with a misclassified binary regressor, showing attenuation proportional to the misclassification rate---analogous to our Theorem~\ref{thm:bias_identity} but restricted to average effects without subgroup heterogeneity.
docs/paper/appendix.tex:1062:The computational cost is substantial ($B \times$ CF fits per MC run), but the approach is straightforward when exact nominal coverage is required.
docs/paper/introduction.tex:12:We formalize this problem and derive an exact bias identity for the correction-induced error.
docs/paper/introduction.tex:13:When a pooled confusion matrix is applied to correct subgroup CATEs, it misattributes error across subgroups with an exact product form: the bias in subgroup $s$ equals $\delta_s \cdot \Delta\tau / (1 - 2\bar{\pi})$, where $\delta_s$ is the deviation from the pooled error rate and $\Delta\tau$ is the CATE heterogeneity (Theorem~\ref{thm:bias_identity}).
docs/paper/introduction.tex:14:This is not a bound but an exact population-level identity, verified empirically with $R^2 = 0.994$ ($K{=}2$) and $R^2 = 0.974$ ($K{=}4$) on synthetic grids, and $R^2 = 0.975$ across 11 real LLM confusion matrices spanning open-source and proprietary model families.
docs/paper/introduction.tex:34:    \item An exact bias identity (Theorem~\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup CATE bias proportional to each subgroup's misclassification deviation times the treatment effect heterogeneity---an exact finite-population identity with independent diagnostic value, verified at $R^2 \geq 0.97$ on synthetic grids and 11 real LLM confusion matrices (Sections~\ref{sec:theory},~\ref{sec:bias_mechanism}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "54bc9bd0-34c5-4a6b-923c-707f5023b18c",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:9:Second, Theorem~\\ref{thm:bias_identity} derives an exact identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.\ndocs/paper/related_work.tex:35:\\citet{imai2010causal} study treatment misclassification, requiring instrumental variables or partial identification; our problem is structurally distinct because the treatment is observed correctly but the effect modifier is misclassified, admitting exact correction through confusion matrices rather than bounds.\ndocs/paper/conclusion.tex:3:We derived an exact bias identity (Theorem~\\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup-level bias proportional to $\\delta_s \\cdot \\Delta\\tau$, worsening CATE estimates in 50\\% of $K{=}2$ configurations.\ndocs/paper/theory.tex:13:We show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.\ndocs/paper/theory.tex:38:Equations~\\eqref{eq:bias_z0}--\\eqref{eq:bias_z1} constitute an exact finite-population identity, not an asymptotic approximation or bound.\ndocs/paper/theory.tex:79:Theorem~\\ref{thm:bias_identity} is an exact population identity.\ndocs/paper/limitations.tex:18:A full bootstrap procedure ($B{=}100$; re-estimate CM and re-fit the forest per replicate) recovers exact nominal coverage (95.0\\%) at a computational cost of ${\\sim}1.5$ minutes per dataset (Appendix~\\ref{app:bootstrap_se}).\ndocs/paper/abstract.tex:4:We derive an exact bias identity showing that this correction-induced bias factors into each subgroup's deviation from the pooled error rate times the treatment effect heterogeneity---a finite-population identity, not a bound.\ndocs/paper/appendix.tex:229:The ATE remains identified; only conditional effects are biased, which makes exact correction through confusion matrix inversion feasible.\ndocs/paper/appendix.tex:233:\\citet{frazis2003estimating} derive exact bias formulas for OLS with a misclassified binary regressor, showing attenuation proportional to the misclassification rate---analogous to our Theorem~\\ref{thm:bias_identity} but restricted to average effects without subgroup heterogeneity.\ndocs/paper/appendix.tex:1062:The computational cost is substantial ($B \\times$ CF fits per MC run), but the approach is straightforward when exact nominal coverage is required.\ndocs/paper/introduction.tex:12:We formalize this problem and derive an exact bias identity for the correction-induced error.\ndocs/paper/introduction.tex:13:When a pooled confusion matrix is applied to correct subgroup CATEs, it misattributes error across subgroups with an exact product form: the bias in subgroup $s$ equals $\\delta_s \\cdot \\Delta\\tau / (1 - 2\\bar{\\pi})$, where $\\delta_s$ is the deviation from the pooled error rate and $\\Delta\\tau$ is the CATE heterogeneity (Theorem~\\ref{thm:bias_identity}).\ndocs/paper/introduction.tex:14:This is not a bound but an exact population-level identity, verified empirically with $R^2 = 0.994$ ($K{=}2$) and $R^2 = 0.974$ ($K{=}4$) on synthetic grids, and $R^2 = 0.975$ across 11 real LLM confusion matrices spanning open-source and proprietary model families.\ndocs/paper/introduction.tex:34:    \\item An exact bias identity (Theorem~\\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup CATE bias proportional to each subgroup's misclassification deviation times the treatment effect heterogeneity---an exact finite-population identity with independent diagnostic value, verified at $R^2 \\geq 0.97$ on synthetic grids and 11 real LLM confusion matrices (Sections~\\ref{sec:theory},~\\ref{sec:bias_mechanism}).",
    "numLines": 15
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01VSVSQCu7NqyEknfV8P8Tt2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 514,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "e6223b77-8ac5-4f58-9d4d-a70f641cdabd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ENjutZQwnUW6T1r5yVhKYs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1545,
      "cache_read_input_tokens": 45828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1545
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-23T09:25:08.815Z_

<details><summary>↩ Tool result · `toolu_01VSVSQCu7NqyEknfV8P8Tt2`</summary>

```text
514	\end{tabular}
515	\end{table*}
516	
517	The orthogonality of EC-HTE and PPCI follows from the distinct error sources they correct: EC-HTE addresses misclassification in the effect modifier $Z$ (covariate space), while PPCI corrects specification error in the outcome model $f(X)$ (prediction space).
518	Since covariate misclassification and outcome model error are algebraically independent in the potential outcomes framework, their corrections compose without interference---confirmed by the 4-DGP orthogonal design (Table~\ref{tab:ppci}), where DGP~C (both errors present) yields the largest bias reduction from the combined approach.
519	Under covariate error only, PPCI adds nothing; under no error, all methods perform equivalently.
520	
521	\section{Real-Data Case Study: Hate Speech Detection}
522	\label{app:hatespeech}
523	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "11e1a8b9-14f0-4638-890b-99bc5209bf96",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
      "content": "\\end{tabular}\n\\end{table*}\n\nThe orthogonality of EC-HTE and PPCI follows from the distinct error sources they correct: EC-HTE addresses misclassification in the effect modifier $Z$ (covariate space), while PPCI corrects specification error in the outcome model $f(X)$ (prediction space).\nSince covariate misclassification and outcome model error are algebraically independent in the potential outcomes framework, their corrections compose without interference---confirmed by the 4-DGP orthogonal design (Table~\\ref{tab:ppci}), where DGP~C (both errors present) yields the largest bias reduction from the combined approach.\nUnder covariate error only, PPCI adds nothing; under no error, all methods perform equivalently.\n\n\\section{Real-Data Case Study: Hate Speech Detection}\n\\label{app:hatespeech}\n",
      "numLines": 10,
      "startLine": 514,
      "totalLines": 1351
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01YDiKCTFo1oEoqWGnpD1S2e`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 1233,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "9a139a08-2ebb-405b-96a1-ba58fc45d5c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ENjutZQwnUW6T1r5yVhKYs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1545,
      "cache_read_input_tokens": 45828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1545
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-23T09:25:09.752Z_

<details><summary>↩ Tool result · `toolu_01YDiKCTFo1oEoqWGnpD1S2e`</summary>

```text
1233	
1234	\begin{table}[h]
1235	\centering
1236	\caption{EC-HTE coverage across confounding strengths and propensity sources. The logistic regression propensity model is correctly specified; propensity misspecification is an orthogonal concern addressed by the IPW literature.}
1237	\label{tab:confounded_sweep}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "6174b56d-620c-4a2a-9619-cb755ef982c6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
      "content": "\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE coverage across confounding strengths and propensity sources. The logistic regression propensity model is correctly specified; propensity misspecification is an orthogonal concern addressed by the IPW literature.}\n\\label{tab:confounded_sweep}",
      "numLines": 5,
      "startLine": 1233,
      "totalLines": 1351
    }
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01JwYYbwB9ueRKLLQj8o9EJJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 1346,
  "limit": 8
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "2d25b2b2-3445-4ace-b02c-9afe0817c253",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ENjutZQwnUW6T1r5yVhKYs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1545,
      "cache_read_input_tokens": 45828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1545
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-23T09:25:10.323Z_

<details><summary>↩ Tool result · `toolu_01JwYYbwB9ueRKLLQj8o9EJJ`</summary>

```text
1346	\end{table}
1347	
1348	Calibration alone improves naive coverage from 84.0\% to 91.3\% but does not reach the nominal 95\%.
1349	Calibrated + EC-HTE achieves the highest coverage (96.5\%), demonstrating that calibration and EC-HTE address orthogonal error sources: calibration reduces per-subgroup $\pi_s$ while EC-HTE corrects the residual $\delta_s$-driven bias from heterogeneity that persists post-calibration.
1350	Propensity estimation robustness under model misspecification is an orthogonal concern addressed by the IPW literature; EC-HTE as a downstream correction layer does not alter IPW behavior.
1351	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "390c9bc4-e644-4a35-9cb0-3c56ffef317b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
      "content": "\\end{table}\n\nCalibration alone improves naive coverage from 84.0\\% to 91.3\\% but does not reach the nominal 95\\%.\nCalibrated + EC-HTE achieves the highest coverage (96.5\\%), demonstrating that calibration and EC-HTE address orthogonal error sources: calibration reduces per-subgroup $\\pi_s$ while EC-HTE corrects the residual $\\delta_s$-driven bias from heterogeneity that persists post-calibration.\nPropensity estimation robustness under model misspecification is an orthogonal concern addressed by the IPW literature; EC-HTE as a downstream correction layer does not alter IPW behavior.\n",
      "numLines": 6,
      "startLine": 1346,
      "totalLines": 1351
    }
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture. Let me also read conclusion.tex since it has an "exact" mention.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "77a63f1b-5b99-469b-bf84-d4b6c0d8b070",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjXAieUHD4ntPVQYG5UQax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5628,
      "cache_read_input_tokens": 47373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5628
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 39_

Let me read the conclusion file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "c34e02b6-24cf-4a67-a0e1-ece1e5670a14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjXAieUHD4ntPVQYG5UQax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5628,
      "cache_read_input_tokens": 47373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5628
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01RgHTc7gLC9MFPk9xWGdD5s`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "b5ea0cb2-3062-4f04-8c4d-aa8b459a3d7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjXAieUHD4ntPVQYG5UQax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5628,
      "cache_read_input_tokens": 47373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5628
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-23T09:25:14.515Z_

<details><summary>↩ Tool result · `toolu_01RgHTc7gLC9MFPk9xWGdD5s`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We derived an exact bias identity (Theorem~\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup-level bias proportional to $\delta_s \cdot \Delta\tau$, worsening CATE estimates in 50\% of $K{=}2$ configurations.
4	EC-HTE provides subgroup-stratified correction via hierarchical Bayes; the companion diagnostic (Proposition~\ref{prop:debiasing_hurts}; AUC $= 1.0$ on subgroups with $\tau_s > 0$) flags harmful correction using only per-subgroup misclassification rates.
5	EC-HTE's advantage requires sufficient $\Delta\pi$ and expert budget; more broadly, the bias identity applies whenever any proxy classifier with subgroup-varying error rates serves as an effect modifier in causal inference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "7b95b064-686e-4ea3-9f31-297765707d34",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe derived an exact bias identity (Theorem~\\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup-level bias proportional to $\\delta_s \\cdot \\Delta\\tau$, worsening CATE estimates in 50\\% of $K{=}2$ configurations.\nEC-HTE provides subgroup-stratified correction via hierarchical Bayes; the companion diagnostic (Proposition~\\ref{prop:debiasing_hurts}; AUC $= 1.0$ on subgroups with $\\tau_s > 0$) flags harmful correction using only per-subgroup misclassification rates.\nEC-HTE's advantage requires sufficient $\\Delta\\pi$ and expert budget; more broadly, the bias identity applies whenever any proxy classifier with subgroup-varying error rates serves as an effect modifier in causal inference.",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 5
    }
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

````text
Now I have everything. Let me plan all edits systematically.

**H1. Abstract** - abstract.tex
Current:
```
\begin{abstract}
Proxy classifiers---including LLMs now widely used to replace human coders---exhibit misclassification rates that vary across subgroups by up to 5$\times$, yet standard practice corrects annotation error using a single pooled confusion matrix.
We show that this global correction introduces structured bias into subgroup-level treatment effect estimates; in our LLM annotation experiments, global correction worsens bias in 50\% of configurations, with amplification up to 5.9$\times$.


```

I derive an exact bias identity that decomposes the correction-induced bias into each subgroup's deviation from the pooled error rate multiplied by treatment effect heterogeneity—a finite-population result, not just a bound. This identity gives us a diagnostic tool that can flag when correction is harmful using only per-subgroup error rates, achieving perfect separation on subgroups with heterogeneous effects but lower aggregate performance on real LLM confusion matrices where correction isn't needed. I then introduce EC-HTE, a per-subgroup correction method derived from this identity using hierarchical Bayes, which reduces the bias.

Continuing with the empirical validation... a single pooled confusion matrix. We show that this global correction introduces structured bias into subgroup-level treatment effect estimates; in our LLM annotation experiments, global correction worsens bias in 50% of configurations. We derive a bias identity showing that this correction-induced bias factors into each subgroup's deviation from the pooled error rate times the treatment effect heterogeneity. The identity yields a diagnostic that flags harmful correction using only per-subgroup error rates, without estimating treatment effects: on subgroups with non-zero effect heterogeneity, the diagnostic achieves perfect separation (AUC = 1.0). We provide EC-HTE, the per-subgroup correction prescribed by the identity via hierarchical Bayes, reducing bias by 7.4× under extreme heterogeneity with nominal coverage, and validate it across synthetic and real LLM configurations—though the advantage depends on having sufficient error heterogeneity and adequate expert budget. 我需要更保守地处理这个任务。关键是只删除数字，保持5句结构不变。对于第1句，把"up to 5×"改成更温和的表述；第2句删除"amplification up to 5.9×"；第4句处理那些具体的数字细节，比如"520 synthetic configurations, eight LLMs, and two NLP datasets"。保留的数字只有50%、7.4×和AUC=1.0这几个关键指标。 I'm working through the abstract edits systematically—removing numerical specifics like "5×", "5.9×", and "520" while keeping the structural integrity intact. For sentence three, I'll simplify "an exact bias identity" to just "a bias identity" and strip out the "not a bound" qualifier. Sentence five needs the most work: replacing "520 synthetic configurations, eight LLMs, and two NLP datasets" with language that conveys scale without explicit numbers, something like "synthetic and semi-synthetic experiments across multiple LLMs and datasets." Now I'm drafting the revised abstract with these changes applied throughout. Now I'm planning the edits to standardize language around the identity concept. I need to keep two instances that emphasize it's exact and finite-population, while simplifying the phrasing elsewhere—removing redundant qualifiers like "not a bound" and replacing awkward constructions with cleaner alternatives like "closed-form product structure." Now I'm refining my approach to focus on the specific patterns mentioned in the task: "exact identity" variations, "exact, not", "not a bound", "not an approximation", and "exact finite-population". I'll keep instances where "exact" is used in mathematical or statistical contexts like "exact correction", "exact bias formulas", "exact nominal coverage" since those don't match the target patterns. Let me verify each change against these specific criteria to ensure I'm only modifying the right instances. I'm continuing through the document to identify all instances that need updating. Lines 38 and 79 in theory.tex both contain the target phrases and should be kept. The conclusion also has an instance to modify. Now I'm clarifying the actual replacements needed—I should remove the "exact" qualifier and the "not a bound" phrase entirely, keeping just "bias identity" or "finite-population identity" depending on context. I'm going through the document systematically to remove "exact" from various descriptions of identities and replace them with simpler language—changing "exact bias identity" to just "bias identity," "exact population identity" to "population-level identity," and so on across the introduction, theory, and conclusion sections. Now I need to add three new references to the bibliography and incorporate three sentences about them into the related work section. I'm working through where to place these three citations in the related work section. Camuffo should go after the Messing citation in the HTE and annotation error paragraph, but I need to be careful not to duplicate the variance-side framing that's already there. Cheng fits better in the LLM annotation quality discussion following Ashwin's bias work. Ura belongs in the measurement error paragraph where we discuss treatment misclassification and structural approaches. Let me figure out the exact sentence integrations for each placement. I'm working through where to integrate these additional citations while maintaining the space budget. For the Cheng reference, I could slot it right after the Ashwin discussion about subgroup error variation—it fits naturally as a complementary preprocessing approach. The Ura citation belongs in the measurement error section where I'm distinguishing our setup from prior work on treatment misclassification, since their instrumental variables approach addresses a different structural problem than ours.

Now I'm reviewing the related work section more carefully to find where I can trim. The classical measurement error theory discussion around line 5-6 is dense with multiple citations covering correction amplification, Bayesian approaches, and nonparametric methods—I could compress that into a tighter statement about why standard approaches don't directly apply here, then use the space freed up for the new citations.

The Frazis comparison around line 10-11 is the key distinction I need to keep sharp, but I can tighten the language. Instead of spelling out both the scalar attenuation formula and the full characterization of correction-induced bias, I could reference Frazis's homogeneous misclassification result more briefly, then emphasize that our structural bias term is fundamentally different—subgroup-specific and potentially sign-reversing—without reproducing all the notation.

For lines 11-12, the homogeneous case ($K=1$) is a useful degenerate check that recovers classical attenuation, but I don't need to dwell on it. I can mention it as a sanity check and then pivot to the algebraic mechanisms that distinguish our approach from standard OLS attenuation results.

For line 21, that compatibility note with the R-learner is redundant—I've already flagged it elsewhere, so I'll drop it.

For line 24, the core point is that subgroup-varying error distorts the contrasts we care about, and existing work documents the problem without offering a solution. I can compress that into a single sentence.

So the targeted edits: remove the R-learner line entirely, tighten the homogeneous case to one sentence, and condense the failure-mode description to emphasize that prior work identifies the pattern but lacks a correction mechanism. bias that is subgroup-specific, potentially sign-reversing, and absent from the uncorrected estimator. This subgroup-varying error distorts the contrasts central to the research question, and while prior work documents the pattern, it lacks a correction mechanism for downstream causal estimands. I'm planning where to insert new material: after the related work section, I'll note that F-L correction produces higher bias than the naive estimator under heterogeneous misclassification, whereas EC-HTE achieves near-oracle performance. I'm working through how to integrate these citations more smoothly into the existing text. The key insight is that LLMs achieve parity with human annotators on many tasks, but they fail systematically across demographic groups—error rates can swing by five-fold depending on subgroup. This is the core problem I'm addressing: these heterogeneous misclassification rates corrupt the contrasts we care about in causal inference, and while prior work documents this pattern, nobody's provided a correction mechanism. I need to position my bias-focused framework against concurrent work that tackles the variance side of measurement error from pipeline design choices. I'm noting that Ashwin and colleagues document substantial variation in error rates across demographic groups—up to a five-fold difference—which undermines the core contrasts we're trying to measure. While prior work has identified this pattern, they haven't corrected for how it propagates into causal estimates downstream. Cheng's work on prompt optimization offers a complementary preprocessing approach, whereas my framework tackles the bias side of the problem by accounting for these heterogeneous misclassification rates across subgroups. I should also acknowledge that concurrent work by Messing and Camuffo examines variance sources in LLM annotation pipelines, which is orthogonal to the bias heterogeneity I'm addressing. I'm refining the comparison to Imai's work on treatment misclassification—adding Ura's extension to heterogeneous treatment effects with mismeasured treatment via instrumental variables, then clarifying that our setup differs fundamentally: we observe treatment correctly but the effect modifier itself is misclassified, which allows direct correction through confusion matrices rather than requiring bounds or instrumental variables. Looking at the next thinking, I see I'm reconsidering the edits to related_work.tex and need to be mindful of space constraints. The original passage spans three sentences covering LLM accuracy on classification tasks, the subgroup-varying error problem we're addressing, and concurrent work on measurement error. I'm measuring the text carefully to ensure my revisions don't expand the section unnecessarily while still capturing the key points about how our framework tackles the bias-side problem from heterogeneous misclassification. I'm clarifying the distinction from prior work on treatment misclassification—Imai requires instrumental variables, but our setup is different because the treatment itself is measured correctly and only the effect modifier has misclassification, which we can correct directly through confusion matrices. I'm also removing the R-learner compatibility line to make room for other content. I need to verify whether the nie2021quasi citation is actually used elsewhere in the document before removing it. The introduction mentions R-learner but doesn't cite it there, so the only citation appears to be in related_work.tex. If I remove that sentence, I should add the citation to the introduction instead to keep the reference.

Let me try compressing the Frazis discussion instead—I can condense those lines about attenuation and correction-induced bias into a more concise explanation that captures the key distinction without the technical details. When $K=1$ and $\delta_s=0$, the correction-induced bias disappears and we recover the classical attenuation result. The key difference from prior work is structural: instead of OLS attenuation under misclassified regressors, we're using confusion matrix inversion that redistributes error across subgroups with heterogeneous rates. Empirically, this matters—F-L correction even applied per subgroup produces higher bias than the naive estimator under heterogeneous misclassification, while our approach achieves near-oracle performance.

Now I'm planning the targeted edits across the paper files. For the abstract, I'll remove quantitative specificity where possible—replacing "by up to 5×" with "substantially," dropping the "5.9×" amplification mention, and simplifying "exact bias identity" to just "bias identity" throughout. The experimental description gets condensed from the full breakdown to a more general statement about synthetic and semi-synthetic experiments with multiple LLMs. Similar changes propagate through the introduction and theory sections, consistently replacing "exact" with simpler language and removing finite-population qualifiers that add technical precision but consume space.

In the related work section, I need to compress existing passages to create room for new citations—specifically adding Cheng and Camuffo to the discussion around line 23-25, and incorporating Ura's work at line 35. The experiments section gets a minor label clarification for the coverage metric, and I'll add a cross-reference after the proof sketch in theory.tex. Finally, I'm adding three new bibliography entries to support these citations.

For the appendix, I'm reconsidering the terminology changes around "orthogonal design"—this appears to be a statistical/experimental design term rather than a mathematical usage, so it likely should stay as is. I also need to fix a year discrepancy in the references and update the conclusion to match the revised phrasing about bias identity. I'm working through the orthogonal-to-complementary replacements systematically. I've identified the key instances: the 4-DGP orthogonal design should stay as-is since it's standard statistical terminology, but the other uses—like "orthogonal concern" and "orthogonal error sources"—need to become "complementary" forms. The task is clear that all replacements should use complementary/complementarity. Now I'm ready to execute the edits across the files, starting with the compressions and additions in related_work.tex, then moving through the other files to make all the necessary substitutions. I'm establishing that under homogeneous misclassification, the uncorrected estimator exhibits scalar attenuation, while Theorem~\ref{thm:bias_identity} identifies a structurally different correction-induced bias that's subgroup-specific and potentially sign-reversing. When $K=1$ and $\delta_s=0$, this reduces to the classical attenuation case, but empirically F-L correction actually increases bias under heterogeneous misclassification whereas EC-HTE approaches oracle performance.

LLMs have reached parity with human annotators on many classification benchmarks, yet error rates diverge substantially across demographic groups—up to a 5-fold difference. This subgroup-varying error is precisely the failure mode I'm addressing, since it corrupts the contrasts central to the research question itself. While concurrent work examines variance-side measurement error from LLM design choices, my framework tackles the complementary bias-side problem arising from heterogeneous misclassification rates across subgroups.

For the treatment misclassification comparison, the key distinction is that prior work addresses scenarios where the treatment itself is mismeasured, requiring instrumental variables or partial identification bounds. My setting is structurally different: the treatment is observed correctly, but the effect modifier is misclassified, which allows for exact correction via confusion matrices rather than relying on bounds. I'm distinguishing our approach from prior work on measurement error in treatment effects—Ura's framework handles mismeasured treatment via instrumental variables, but we're addressing a different problem where the treatment itself is correctly observed but the effect modifier gets misclassified, which we can correct using confusion matrices. Now I need to integrate these new bibliography entries into the document, placing them thematically: the LLM annotation papers near related work on annotation quality, and the treatment effects paper near the measurement error section. I'll batch these edits together and also handle the Törnberg year correction while I'm at it.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "a877cbff-a250-440a-8bbe-5f0fa71a448c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ej86nXZny8D22LgdS358EU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 53001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 43_

I have a complete picture of all changes needed. Let me execute all 8 fixes now.

Starting with H1 (abstract), H2 (exact identity replacements), H5 (orthogonal→complementary), H6 (table header), H8 (Törnberg year), and the bib additions for H3/H4 — all independent edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "835da325-aad1-47a7-a386-1a4651c67e0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ej86nXZny8D22LgdS358EU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 53001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Edit · `toolu_01BTYny4rTutgDSGZFfKJvaj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex",
  "old_string": "Proxy classifiers---including LLMs now widely used to replace human coders---exhibit misclassification rates that vary across subgroups by up to 5$\\times$, yet standard practice corrects annotation error using a single pooled confusion matrix.\nWe show that this global correction introduces structured bias into subgroup-level treatment effect estimates; in our LLM annotation experiments, global correction worsens bias in 50\\% of configurations, with amplification up to 5.9$\\times$.\nWe derive an exact bias identity showing that this correction-induced bias factors into each subgroup's deviation from the pooled error rate times the treatment effect heterogeneity---a finite-population identity, not a bound.\nThe identity yields a diagnostic that flags harmful correction using only per-subgroup error rates, without estimating treatment effects: on subgroups with non-zero effect heterogeneity, the diagnostic achieves perfect separation (AUC $= 1.0$); the lower aggregate AUC on real LLM confusion matrices is driven by subgroups where correction is unnecessary.\nWe provide EC-HTE, the per-subgroup correction prescribed by the identity via hierarchical Bayes, reducing $|\\text{bias}|$ by 7.4$\\times$ under extreme heterogeneity with nominal coverage ($\\geq$0.90); validated across 520 synthetic configurations, eight LLMs, and two NLP datasets, the advantage is conditional on sufficient error heterogeneity and expert budget.",
  "new_string": "Proxy classifiers---including LLMs now widely used to replace human coders---exhibit misclassification rates that vary substantially across subgroups, yet standard practice corrects annotation error using a single pooled confusion matrix.\nWe show that this global correction introduces structured bias into subgroup-level treatment effect estimates; in our LLM annotation experiments, global correction worsens bias in 50\\% of configurations.\nWe derive a bias identity showing that this correction-induced bias factors into each subgroup's deviation from the pooled error rate times the treatment effect heterogeneity.\nThe identity yields a diagnostic that flags harmful correction using only per-subgroup error rates, without estimating treatment effects: on subgroups with non-zero effect heterogeneity, the diagnostic achieves perfect separation (AUC $= 1.0$); the lower aggregate AUC on real LLM confusion matrices is driven by subgroups where correction is unnecessary.\nWe provide EC-HTE, the per-subgroup correction prescribed by the identity via hierarchical Bayes, reducing $|\\text{bias}|$ by 7.4$\\times$ under extreme heterogeneity with nominal coverage ($\\geq$0.90); validated across synthetic and semi-synthetic experiments with multiple LLMs, the advantage is conditional on sufficient error heterogeneity and expert budget."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "2f19e02e-8abc-42ad-95bc-5803e71c7e7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ej86nXZny8D22LgdS358EU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 53001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-23T09:28:46.252Z_

<details><summary>↩ Tool result · `toolu_01BTYny4rTutgDSGZFfKJvaj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "85d8def4-2269-4ee9-bbbb-a8e00fad7494",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex",
    "oldString": "Proxy classifiers---including LLMs now widely used to replace human coders---exhibit misclassification rates that vary across subgroups by up to 5$\\times$, yet standard practice corrects annotation error using a single pooled confusion matrix.\nWe show that this global correction introduces structured bias into subgroup-level treatment effect estimates; in our LLM annotation experiments, global correction worsens bias in 50\\% of configurations, with amplification up to 5.9$\\times$.\nWe derive an exact bias identity showing that this correction-induced bias factors into each subgroup's deviation from the pooled error rate times the treatment effect heterogeneity---a finite-population identity, not a bound.\nThe identity yields a diagnostic that flags harmful correction using only per-subgroup error rates, without estimating treatment effects: on subgroups with non-zero effect heterogeneity, the diagnostic achieves perfect separation (AUC $= 1.0$); the lower aggregate AUC on real LLM confusion matrices is driven by subgroups where correction is unnecessary.\nWe provide EC-HTE, the per-subgroup correction prescribed by the identity via hierarchical Bayes, reducing $|\\text{bias}|$ by 7.4$\\times$ under extreme heterogeneity with nominal coverage ($\\geq$0.90); validated across 520 synthetic configurations, eight LLMs, and two NLP datasets, the advantage is conditional on sufficient error heterogeneity and expert budget.",
    "newString": "Proxy classifiers---including LLMs now widely used to replace human coders---exhibit misclassification rates that vary substantially across subgroups, yet standard practice corrects annotation error using a single pooled confusion matrix.\nWe show that this global correction introduces structured bias into subgroup-level treatment effect estimates; in our LLM annotation experiments, global correction worsens bias in 50\\% of configurations.\nWe derive a bias identity showing that this correction-induced bias factors into each subgroup's deviation from the pooled error rate times the treatment effect heterogeneity.\nThe identity yields a diagnostic that flags harmful correction using only per-subgroup error rates, without estimating treatment effects: on subgroups with non-zero effect heterogeneity, the diagnostic achieves perfect separation (AUC $= 1.0$); the lower aggregate AUC on real LLM confusion matrices is driven by subgroups where correction is unnecessary.\nWe provide EC-HTE, the per-subgroup correction prescribed by the identity via hierarchical Bayes, reducing $|\\text{bias}|$ by 7.4$\\times$ under extreme heterogeneity with nominal coverage ($\\geq$0.90); validated across synthetic and semi-synthetic experiments with multiple LLMs, the advantage is conditional on sufficient error heterogeneity and expert budget.",
    "originalFile": "\\begin{abstract}\nProxy classifiers---including LLMs now widely used to replace human coders---exhibit misclassification rates that vary across subgroups by up to 5$\\times$, yet standard practice corrects annotation error using a single pooled confusion matrix.\nWe show that this global correction introduces structured bias into subgroup-level treatment effect estimates; in our LLM annotation experiments, global correction worsens bias in 50\\% of configurations, with amplification up to 5.9$\\times$.\nWe derive an exact bias identity showing that this correction-induced bias factors into each subgroup's deviation from the pooled error rate times the treatment effect heterogeneity---a finite-population identity, not a bound.\nThe identity yields a diagnostic that flags harmful correction using only per-subgroup error rates, without estimating treatment effects: on subgroups with non-zero effect heterogeneity, the diagnostic achieves perfect separation (AUC $= 1.0$); the lower aggregate AUC on real LLM confusion matrices is driven by subgroups where correction is unnecessary.\nWe provide EC-HTE, the per-subgroup correction prescribed by the identity via hierarchical Bayes, reducing $|\\text{bias}|$ by 7.4$\\times$ under extreme heterogeneity with nominal coverage ($\\geq$0.90); validated across 520 synthetic configurations, eight LLMs, and two NLP datasets, the advantage is conditional on sufficient error heterogeneity and expert budget.\n\\end{abstract}",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 7,
        "newStart": 1,
        "newLines": 7,
        "lines": [
          " \\begin{abstract}",
          "-Proxy classifiers---including LLMs now widely used to replace human coders---exhibit misclassification rates that vary across subgroups by up to 5$\\times$, yet standard practice corrects annotation error using a single pooled confusion matrix.",
          "-We show that this global correction introduces structured bias into subgroup-level treatment effect estimates; in our LLM annotation experiments, global correction worsens bias in 50\\% of configurations, with amplification up to 5.9$\\times$.",
          "-We derive an exact bias identity showing that this correction-induced bias factors into each subgroup's deviation from the pooled error rate times the treatment effect heterogeneity---a finite-population identity, not a bound.",
          "+Proxy classifiers---including LLMs now widely used to replace human coders---exhibit misclassification rates that vary substantially across subgroups, yet standard practice corrects annotation error using a single pooled confusion matrix.",
          "+We show that this global correction introduces structured bias into subgroup-level treatment effect estimates; in our LLM annotation experiments, global correction worsens bias in 50\\% of configurations.",
          "+We derive a bias identity showing that this correction-induced bias factors into each subgroup's deviation from the pooled error rate times the treatment effect heterogeneity.",
          " The identity yields a diagnostic that flags harmful correction using only per-subgroup error rates, without estimating treatment effects: on subgroups with non-zero effect heterogeneity, the diagnostic achieves perfect separation (AUC $= 1.0$); the lower aggregate AUC on real LLM confusion matrices is driven by subgroups where correction is unnecessary.",
          "-We provide EC-HTE, the per-subgroup correction prescribed by the identity via hierarchical Bayes, reducing $|\\text{bias}|$ by 7.4$\\times$ under extreme heterogeneity with nominal coverage ($\\geq$0.90); validated across 520 synthetic configurations, eight LLMs, and two NLP datasets, the advantage is conditional on sufficient error heterogeneity and expert budget.",
          "+We provide EC-HTE, the per-subgroup correction prescribed by the identity via hierarchical Bayes, reducing $|\\text{bias}|$ by 7.4$\\times$ under extreme heterogeneity with nominal coverage ($\\geq$0.90); validated across synthetic and semi-synthetic experiments with multiple LLMs, the advantage is conditional on sufficient error heterogeneity and expert budget.",
          " \\end{abstract}",
          "\\ No newline at end of file"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Edit · `toolu_01GdNyfvZ13m42W7NWJGm1QV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex",
  "old_string": "We formalize this problem and derive an exact bias identity for the correction-induced error.",
  "new_string": "We formalize this problem and derive a bias identity for the correction-induced error."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "c50655e2-3803-46b7-8452-a6c0e2642a9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ej86nXZny8D22LgdS358EU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 53001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-23T09:28:47.401Z_

<details><summary>↩ Tool result · `toolu_01GdNyfvZ13m42W7NWJGm1QV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "55d13542-3e43-4a56-8b27-ee7db592d456",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex",
    "oldString": "We formalize this problem and derive an exact bias identity for the correction-induced error.",
    "newString": "We formalize this problem and derive a bias identity for the correction-induced error.",
    "originalFile": "\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models (LLMs) now routinely replace human annotators in computational social science (CSS), producing labels for sentiment, hate speech, stance, and political discourse at costs orders of magnitude below manual coding~\\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp}.\nYet these annotations are not uniformly accurate.\n\\citet{ashwin2025bias} document that LLM misclassification rates vary by up to 5$\\times$ across demographic subgroups defined by refugee status, gender, and education level.\nIn a pilot study, GPT-4.1 achieves 85.8\\% binary accuracy on TweetEval sentiment, but error rates range from 10.2\\% to 20.0\\% across text-feature subgroups ($\\Delta\\pi = 0.098$).\nWhen such annotations serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, subgroup-specific errors propagate directly into conditional average treatment effect (CATE) estimates.\nThe resulting bias is not random noise that averages out; it is structured by the same demographic axes that define the research question.\nStandard correction procedures\\footnote{Throughout, ``debiasing'' refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing.}, which estimate a single confusion matrix and apply its inverse uniformly, cannot account for this heterogeneity.\n\nWe formalize this problem and derive an exact bias identity for the correction-induced error.\nWhen a pooled confusion matrix is applied to correct subgroup CATEs, it misattributes error across subgroups with an exact product form: the bias in subgroup $s$ equals $\\delta_s \\cdot \\Delta\\tau / (1 - 2\\bar{\\pi})$, where $\\delta_s$ is the deviation from the pooled error rate and $\\Delta\\tau$ is the CATE heterogeneity (Theorem~\\ref{thm:bias_identity}).\nThis is not a bound but an exact population-level identity, verified empirically with $R^2 = 0.994$ ($K{=}2$) and $R^2 = 0.974$ ($K{=}4$) on synthetic grids, and $R^2 = 0.975$ across 11 real LLM confusion matrices spanning open-source and proprietary model families.\nA direct consequence is that global correction can be worse than no correction at all: global correction worsens CATE bias in 50\\% of $K{=}2$ configurations (260/520) across our parameter grid---concentrated in regimes where $\\Delta\\pi > 0.10$ and per-subgroup expert samples exceed 25---with amplification reaching 2.86$\\times$ ($K{=}2$) and 5.9$\\times$ ($K{=}4$ with CausalForest).\nThe bias identity also yields a $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}): a condition on per-subgroup misclassification rates alone predicts when global correction will increase bias, achieving AUC $= 1.0$ on subgroups with non-zero effect heterogeneity (Section~\\ref{sec:diagnostic})---independently useful even without adopting EC-HTE, since practitioners can flag harmful correction from a pilot sample before estimating any treatment effects.\nError-Corrected Heterogeneous Treatment Effects (EC-HTE), the per-subgroup correction prescribed by the identity, reduces $|\\text{bias}|$ from 0.059 to 0.008 under extreme heterogeneity ($K{=}2$) via hierarchical Bayesian confusion matrix estimation.\nEC-HTE's advantage is conditional on sufficient error heterogeneity and expert budget; when $\\Delta\\pi$ is small, the variance cost of stratification outweighs its bias benefit---the expected bias-variance tradeoff of any subgroup-stratified correction (Figure~\\ref{fig:bias_mechanism}).\n\nSubgroup CATEs inform resource allocation---e.g., whether a policy reduces toxicity more in long-form versus short-form posts---and biased estimates can reverse the sign of apparent heterogeneity, directing resources away from communities that benefit most.\nThe failure mode is subtle: correcting for annotation noise using a pooled confusion matrix may introduce more bias than doing nothing, precisely in the low-error subgroups where labels were most trustworthy.\n\nExisting corrections---PPI~\\cite{angelopoulos2023ppi}, DSL~\\cite{egami2024dsl}, PPCI~\\cite{sui2026ppci}, arm-specific PPI~\\cite{mozer2026ppi}, ForestIV~\\cite{bu2023forestiv}---address population-level or outcome-side measurement error but assume homogeneous prediction error across subgroups; none corrects bias when the mismeasured variable is the effect modifier indexing the CATE function (Section~\\ref{sec:related}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig1_bias_mechanism.pdf}\n\\caption{Bias mechanism under global vs.\\ subgroup-stratified correction. Global correction applies the pooled error rate $\\bar{\\pi}$ uniformly, over-correcting low-error subgroups (introducing bias where none existed) and under-correcting high-error subgroups. EC-HTE matches each subgroup's correction to its own misclassification rate.}\n\\label{fig:bias_mechanism}\n\\end{figure}\n\nOur contributions are:\n\\begin{itemize}\n    \\item An exact bias identity (Theorem~\\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup CATE bias proportional to each subgroup's misclassification deviation times the treatment effect heterogeneity---an exact finite-population identity with independent diagnostic value, verified at $R^2 \\geq 0.97$ on synthetic grids and 11 real LLM confusion matrices (Sections~\\ref{sec:theory},~\\ref{sec:bias_mechanism}).\n    \\item A $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}) derived from the identity: a condition on per-subgroup misclassification rates alone predicts when global correction increases bias, achieving AUC $= 1.0$ on subgroups with non-zero effect heterogeneity---independently actionable without EC-HTE (Section~\\ref{sec:diagnostic}).\n    \\item EC-HTE, the per-subgroup correction prescribed by the bias structure via hierarchical Bayesian confusion matrix estimation, compatible with difference-in-means, CausalForest, and R-learner, and composable with PPCI for joint covariate/outcome error; we characterize applicability conditions and crossover budgets (Sections~\\ref{sec:method}--\\ref{sec:diagnostic}; Appendix~\\ref{sec:budget}).\n\\end{itemize}\nWhile we develop the theory and experiments for LLM annotation---the leading practical case---the bias identity applies whenever any proxy classifier with subgroup-varying error rates is used to construct effect modifiers for causal inference.\n",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " The resulting bias is not random noise that averages out; it is structured by the same demographic axes that define the research question.",
          " Standard correction procedures\\footnote{Throughout, ``debiasing'' refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing.}, which estimate a single confusion matrix and apply its inverse uniformly, cannot account for this heterogeneity.",
          " ",
          "-We formalize this problem and derive an exact bias identity for the correction-induced error.",
          "+We formalize this problem and derive a bias identity for the correction-induced error.",
          " When a pooled confusion matrix is applied to correct subgroup CATEs, it misattributes error across subgroups with an exact product form: the bias in subgroup $s$ equals $\\delta_s \\cdot \\Delta\\tau / (1 - 2\\bar{\\pi})$, where $\\delta_s$ is the deviation from the pooled error rate and $\\Delta\\tau$ is the CATE heterogeneity (Theorem~\\ref{thm:bias_identity}).",
          " This is not a bound but an exact population-level identity, verified empirically with $R^2 = 0.994$ ($K{=}2$) and $R^2 = 0.974$ ($K{=}4$) on synthetic grids, and $R^2 = 0.975$ across 11 real LLM confusion matrices spanning open-source and proprietary model families.",
          " A direct consequence is that global correction can be worse than no correction at all: global correction worsens CATE bias in 50\\% of $K{=}2$ configurations (260/520) across our parameter grid---concentrated in regimes where $\\Delta\\pi > 0.10$ and per-subgroup expert samples exceed 25---with amplification reaching 2.86$\\times$ ($K{=}2$) and 5.9$\\times$ ($K{=}4$ with CausalForest)."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Edit · `toolu_0142cm4XNhcB5ga5f66QymSJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex",
  "old_string": "    \\item An exact bias identity (Theorem~\\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup CATE bias proportional to each subgroup's misclassification deviation times the treatment effect heterogeneity---an exact finite-population identity with independent diagnostic value, verified at $R^2 \\geq 0.97$ on synthetic grids and 11 real LLM confusion matrices (Sections~\\ref{sec:theory},~\\ref{sec:bias_mechanism}).",
  "new_string": "    \\item A bias identity (Theorem~\\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup CATE bias proportional to each subgroup's misclassification deviation times the treatment effect heterogeneity---a bias decomposition with independent diagnostic value, verified at $R^2 \\geq 0.97$ on synthetic grids and 11 real LLM confusion matrices (Sections~\\ref{sec:theory},~\\ref{sec:bias_mechanism})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "001723a7-8c9e-435c-a78a-c714b253ea4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ej86nXZny8D22LgdS358EU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 53001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-23T09:28:52.142Z_

<details><summary>↩ Tool result · `toolu_0142cm4XNhcB5ga5f66QymSJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "268bdb9a-3408-4246-86f6-df19d0799af7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex",
    "oldString": "    \\item An exact bias identity (Theorem~\\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup CATE bias proportional to each subgroup's misclassification deviation times the treatment effect heterogeneity---an exact finite-population identity with independent diagnostic value, verified at $R^2 \\geq 0.97$ on synthetic grids and 11 real LLM confusion matrices (Sections~\\ref{sec:theory},~\\ref{sec:bias_mechanism}).",
    "newString": "    \\item A bias identity (Theorem~\\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup CATE bias proportional to each subgroup's misclassification deviation times the treatment effect heterogeneity---a bias decomposition with independent diagnostic value, verified at $R^2 \\geq 0.97$ on synthetic grids and 11 real LLM confusion matrices (Sections~\\ref{sec:theory},~\\ref{sec:bias_mechanism}).",
    "originalFile": "\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models (LLMs) now routinely replace human annotators in computational social science (CSS), producing labels for sentiment, hate speech, stance, and political discourse at costs orders of magnitude below manual coding~\\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp}.\nYet these annotations are not uniformly accurate.\n\\citet{ashwin2025bias} document that LLM misclassification rates vary by up to 5$\\times$ across demographic subgroups defined by refugee status, gender, and education level.\nIn a pilot study, GPT-4.1 achieves 85.8\\% binary accuracy on TweetEval sentiment, but error rates range from 10.2\\% to 20.0\\% across text-feature subgroups ($\\Delta\\pi = 0.098$).\nWhen such annotations serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, subgroup-specific errors propagate directly into conditional average treatment effect (CATE) estimates.\nThe resulting bias is not random noise that averages out; it is structured by the same demographic axes that define the research question.\nStandard correction procedures\\footnote{Throughout, ``debiasing'' refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing.}, which estimate a single confusion matrix and apply its inverse uniformly, cannot account for this heterogeneity.\n\nWe formalize this problem and derive a bias identity for the correction-induced error.\nWhen a pooled confusion matrix is applied to correct subgroup CATEs, it misattributes error across subgroups with an exact product form: the bias in subgroup $s$ equals $\\delta_s \\cdot \\Delta\\tau / (1 - 2\\bar{\\pi})$, where $\\delta_s$ is the deviation from the pooled error rate and $\\Delta\\tau$ is the CATE heterogeneity (Theorem~\\ref{thm:bias_identity}).\nThis is not a bound but an exact population-level identity, verified empirically with $R^2 = 0.994$ ($K{=}2$) and $R^2 = 0.974$ ($K{=}4$) on synthetic grids, and $R^2 = 0.975$ across 11 real LLM confusion matrices spanning open-source and proprietary model families.\nA direct consequence is that global correction can be worse than no correction at all: global correction worsens CATE bias in 50\\% of $K{=}2$ configurations (260/520) across our parameter grid---concentrated in regimes where $\\Delta\\pi > 0.10$ and per-subgroup expert samples exceed 25---with amplification reaching 2.86$\\times$ ($K{=}2$) and 5.9$\\times$ ($K{=}4$ with CausalForest).\nThe bias identity also yields a $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}): a condition on per-subgroup misclassification rates alone predicts when global correction will increase bias, achieving AUC $= 1.0$ on subgroups with non-zero effect heterogeneity (Section~\\ref{sec:diagnostic})---independently useful even without adopting EC-HTE, since practitioners can flag harmful correction from a pilot sample before estimating any treatment effects.\nError-Corrected Heterogeneous Treatment Effects (EC-HTE), the per-subgroup correction prescribed by the identity, reduces $|\\text{bias}|$ from 0.059 to 0.008 under extreme heterogeneity ($K{=}2$) via hierarchical Bayesian confusion matrix estimation.\nEC-HTE's advantage is conditional on sufficient error heterogeneity and expert budget; when $\\Delta\\pi$ is small, the variance cost of stratification outweighs its bias benefit---the expected bias-variance tradeoff of any subgroup-stratified correction (Figure~\\ref{fig:bias_mechanism}).\n\nSubgroup CATEs inform resource allocation---e.g., whether a policy reduces toxicity more in long-form versus short-form posts---and biased estimates can reverse the sign of apparent heterogeneity, directing resources away from communities that benefit most.\nThe failure mode is subtle: correcting for annotation noise using a pooled confusion matrix may introduce more bias than doing nothing, precisely in the low-error subgroups where labels were most trustworthy.\n\nExisting corrections---PPI~\\cite{angelopoulos2023ppi}, DSL~\\cite{egami2024dsl}, PPCI~\\cite{sui2026ppci}, arm-specific PPI~\\cite{mozer2026ppi}, ForestIV~\\cite{bu2023forestiv}---address population-level or outcome-side measurement error but assume homogeneous prediction error across subgroups; none corrects bias when the mismeasured variable is the effect modifier indexing the CATE function (Section~\\ref{sec:related}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig1_bias_mechanism.pdf}\n\\caption{Bias mechanism under global vs.\\ subgroup-stratified correction. Global correction applies the pooled error rate $\\bar{\\pi}$ uniformly, over-correcting low-error subgroups (introducing bias where none existed) and under-correcting high-error subgroups. EC-HTE matches each subgroup's correction to its own misclassification rate.}\n\\label{fig:bias_mechanism}\n\\end{figure}\n\nOur contributions are:\n\\begin{itemize}\n    \\item An exact bias identity (Theorem~\\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup CATE bias proportional to each subgroup's misclassification deviation times the treatment effect heterogeneity---an exact finite-population identity with independent diagnostic value, verified at $R^2 \\geq 0.97$ on synthetic grids and 11 real LLM confusion matrices (Sections~\\ref{sec:theory},~\\ref{sec:bias_mechanism}).\n    \\item A $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}) derived from the identity: a condition on per-subgroup misclassification rates alone predicts when global correction increases bias, achieving AUC $= 1.0$ on subgroups with non-zero effect heterogeneity---independently actionable without EC-HTE (Section~\\ref{sec:diagnostic}).\n    \\item EC-HTE, the per-subgroup correction prescribed by the bias structure via hierarchical Bayesian confusion matrix estimation, compatible with difference-in-means, CausalForest, and R-learner, and composable with PPCI for joint covariate/outcome error; we characterize applicability conditions and crossover budgets (Sections~\\ref{sec:method}--\\ref{sec:diagnostic}; Appendix~\\ref{sec:budget}).\n\\end{itemize}\nWhile we develop the theory and experiments for LLM annotation---the leading practical case---the bias identity applies whenever any proxy classifier with subgroup-varying error rates is used to construct effect modifiers for causal inference.\n",
    "structuredPatch": [
      {
        "oldStart": 31,
        "oldLines": 7,
        "newStart": 31,
        "newLines": 7,
        "lines": [
          " ",
          " Our contributions are:",
          " \\begin{itemize}",
          "-    \\item An exact bias identity (Theorem~\\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup CATE bias proportional to each subgroup's misclassification deviation times the treatment effect heterogeneity---an exact finite-population identity with independent diagnostic value, verified at $R^2 \\geq 0.97$ on synthetic grids and 11 real LLM confusion matrices (Sections~\\ref{sec:theory},~\\ref{sec:bias_mechanism}).",
          "+    \\item A bias identity (Theorem~\\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup CATE bias proportional to each subgroup's misclassification deviation times the treatment effect heterogeneity---a bias decomposition with independent diagnostic value, verified at $R^2 \\geq 0.97$ on synthetic grids and 11 real LLM confusion matrices (Sections~\\ref{sec:theory},~\\ref{sec:bias_mechanism}).",
          "     \\item A $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}) derived from the identity: a condition on per-subgroup misclassification rates alone predicts when global correction increases bias, achieving AUC $= 1.0$ on subgroups with non-zero effect heterogeneity---independently actionable without EC-HTE (Section~\\ref{sec:diagnostic}).",
          "     \\item EC-HTE, the per-subgroup correction prescribed by the bias structure via hierarchical Bayesian confusion matrix estimation, compatible with difference-in-means, CausalForest, and R-learner, and composable with PPCI for joint covariate/outcome error; we characterize applicability conditions and crossover budgets (Sections~\\ref{sec:method}--\\ref{sec:diagnostic}; Appendix~\\ref{sec:budget}).",
          " \\end{itemize}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Edit · `toolu_014r7Mg7HxuJKgC9K1zjHwKU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
  "old_string": "Theorem~\\ref{thm:bias_identity} is an exact population identity.",
  "new_string": "Theorem~\\ref{thm:bias_identity} is a population-level identity."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "a8eb9692-4528-401d-b4ee-c2d28c2310bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ej86nXZny8D22LgdS358EU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 53001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-23T09:28:53.135Z_

<details><summary>↩ Tool result · `toolu_014r7Mg7HxuJKgC9K1zjHwKU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "d8d8d8a4-b8cb-49b0-a5d9-586e2bc9052e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
    "oldString": "Theorem~\\ref{thm:bias_identity} is an exact population identity.",
    "newString": "Theorem~\\ref{thm:bias_identity} is a population-level identity.",
    "originalFile": "% Requires preamble: \\usepackage{amsthm,amsmath,amssymb}\n% and: \\newtheorem{theorem}{Theorem}\n%      \\newtheorem{corollary}[theorem]{Corollary}\n%      \\newtheorem{proposition}[theorem]{Proposition}\n\n\\section{Bias Decomposition: When Debiasing Hurts}\n\\label{sec:theory}\n\nWe formalize the bias that global misclassification correction introduces when subgroup error rates are heterogeneous.\nConsider estimating the conditional average treatment effect (CATE) $\\tau(z) = \\mathbb{E}[Y(1) - Y(0) \\mid Z = z]$, where $Z \\in \\{0, 1\\}$ is a binary effect modifier observed only through a noisy annotation $\\hat{Z}$.\nThe population consists of $K$ subgroups $S \\in \\{1, \\ldots, K\\}$ with weights $w_s = P(S{=}s)$, each characterized by a $2 \\times 2$ confusion matrix $C_s$ with symmetric error rate $\\pi_s = P(\\hat{Z} \\neq Z \\mid S{=}s)$.\nStandard practice estimates a single confusion matrix $\\bar{C} = \\sum_s w_s C_s$ from expert annotations and applies its inverse uniformly to all observations, with pooled error rate $\\bar{\\pi} = \\sum_s w_s \\pi_s$.\nWe show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.\n\nWe state five assumptions maintained throughout.\n%\n\\begin{itemize}\n\\item[\\textbf{(A1)}] \\textit{Conditional independence:} misclassification depends only on the true label $Z$ and subgroup $S$, not on potential outcomes $Y(0), Y(1)$.\n\\item[\\textbf{(A2)}] \\textit{Symmetric misclassification:} $P(\\hat{Z}{=}1 \\mid Z{=}0, S{=}s) = P(\\hat{Z}{=}0 \\mid Z{=}1, S{=}s) = \\pi_s$ for all $s$ (diagnostic only; see Remark~2).\n\\item[\\textbf{(A3)}] \\textit{Balanced effect modifier:} $P(Z{=}0) = P(Z{=}1) = 0.5$. This simplifies the exposition; we discuss relaxation below.\n\\item[\\textbf{(A4)}] \\textit{Non-degeneracy:} $\\pi_s \\neq 0.5$ for all $s$, ensuring each $C_s$ is invertible.\n\\item[\\textbf{(A5)}] \\textit{Homogeneous treatment effects across subgroups:} $\\tau(z, s) = \\tau(z)$ for all $s$, so $\\Delta\\tau = \\tau(1) - \\tau(0)$ is a scalar.\n\\end{itemize}\n\nUnder (A2)--(A3), the Bayesian mixing matrix $M_s$ (entries $M_s[\\hat{z}, z] = P(Z{=}z \\mid \\hat{Z}{=}\\hat{z}, S{=}s)$) coincides with $C_s$.\nThe global mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s$.\n\n\\begin{theorem}[Bias Decomposition Identity]\n\\label{thm:bias_identity}\nUnder \\textnormal{(A1)--(A5)}, the bias of global correction in subgroup $s$ at effect-modifier level $z$ is\n\\begin{align}\n\\mathrm{bias}_{\\mathrm{global}}(z{=}0, s) &= +\\frac{\\delta_s \\cdot \\Delta\\tau}{1 - 2\\bar{\\pi}}, \\label{eq:bias_z0} \\\\\n\\mathrm{bias}_{\\mathrm{global}}(z{=}1, s) &= -\\frac{\\delta_s \\cdot \\Delta\\tau}{1 - 2\\bar{\\pi}}, \\label{eq:bias_z1}\n\\end{align}\nwhere $\\delta_s = \\pi_s - \\bar{\\pi}$ is the subgroup deviation from the pooled error rate and $\\Delta\\tau = \\tau(1) - \\tau(0)$ is the CATE heterogeneity.\n\\end{theorem}\n\nEquations~\\eqref{eq:bias_z0}--\\eqref{eq:bias_z1} constitute an exact finite-population identity, not an asymptotic approximation or bound.\nThe bias factors into three interpretable components: $\\delta_s$ captures how much subgroup $s$ deviates from the average misclassification rate, $\\Delta\\tau$ captures treatment effect heterogeneity across levels of $Z$, and $1/(1 - 2\\bar{\\pi})$ is an amplification factor from matrix inversion.\nBias vanishes when either source of variation is absent ($\\delta_s = 0$ or $\\Delta\\tau = 0$), and arises only through their interaction.\nTheorem~\\ref{thm:bias_identity} implies that global correction trades one source of confounding for another: it removes attenuation from label noise but introduces a new bias from error-rate heterogeneity.\n\n\\paragraph{Proof sketch.}\nGlobal correction applies $M_{\\text{global}}^{-1}$ to the subgroup-specific observed CATE $\\tau_{\\text{obs}}(\\cdot, s) = M_s \\cdot \\tau_{\\text{true}}$, yielding bias $(M_{\\text{global}}^{-1} M_s - I) \\cdot \\tau_{\\text{true}}$.\nDirect computation shows $M_{\\text{global}}^{-1} M_s - I = \\frac{\\delta_s}{1-2\\bar{\\pi}} \\bigl[\\begin{smallmatrix} -1 & 1 \\\\ 1 & -1 \\end{smallmatrix}\\bigr]$.\nApplying this matrix to $[\\tau(0),\\, \\tau(1)]^\\top$ produces the product form.\nThe full derivation appears in Appendix~\\ref{app:derivation}.\n\n\\begin{remark}\nTheorem~\\ref{thm:bias_identity} does not require assumption~(A2).\nFor arbitrary asymmetric confusion matrices ($\\mathrm{FPR}_s \\neq \\mathrm{FNR}_s$),\nthe product form $\\mathrm{bias}(z, s) = \\Delta\\tau \\cdot [B_s]_{z,1}$ holds exactly,\nwhere $B_s = M_{\\mathrm{global}}^{-1} M_s - I$, because $B_s \\mathbf{1} = \\mathbf{0}$\nfollows from stochasticity of $M_s$ and $M_{\\mathrm{global}}$ alone.\nAssumption~(A2) simplifies $[B_s]_{z,1}$ to the scalar\n$\\pm \\delta_s / (1 - 2\\bar{\\pi})$ but is not necessary for the product structure.\nUnder asymmetric errors, the diagnostic (Proposition~\\ref{prop:debiasing_hurts}) requires evaluating $[B_s]_{z,1}$ cell-by-cell rather than via a single scalar threshold; the AUC decreases from 0.86 to 0.82 (Appendix~\\ref{app:asymmetric}), reflecting the additional complexity of cell-specific error rates.\nFor binary effect modifiers ($|\\mathcal{Z}|{=}2$), the asymmetric score $|[B_s]_{z,1}|$ reduces to a monotone transform of the symmetric score $|\\delta_s|/((1{-}2\\bar{\\pi})\\pi_s)$, because column-stochastic $M$ forces $|B_s[0,1]|{=}|B_s[1,1]|$; practitioners may use the simpler symmetric formula without loss.\nSee Appendix~\\ref{app:asymmetric} for the full derivation and empirical verification\n($R^2 = 0.991$).\n\\end{remark}\n\nAssumption~(A5) simplifies exposition; the identity generalizes to subgroup-specific $\\Delta\\tau_s$ (Corollary~\\ref{cor:a5_relaxation}, Appendix~\\ref{app:a5_violation}).\nEC-HTE's correction does not depend on (A5): each $\\hat{C}_s^{-1}$ corrects the local misclassification structure regardless of whether $\\Delta\\tau$ varies; under both positive and negative $\\Delta\\tau_s$--$\\delta_s$ correlation, EC-HTE maintains $\\geq$93\\% coverage while global correction degrades to 74--82\\% (Appendix~\\ref{app:a5_violation}).\n\nThe identity extends to $K > 2$ subgroups with $J$ effect-modifier levels; the multi-class bias retains the same product structure with modified amplification terms (Corollary~\\ref{cor:multiclass} in Appendix~\\ref{app:multiclass}).\n\nAssumption~(A3) ensures $M_s = C_s$; when $P(Z{=}1) \\neq 0.5$, the mixing matrices acquire asymmetric entries, but the product structure persists with modified coefficients (Appendix~\\ref{app:derivation}).\nEmpirical verification under class imbalance (Appendix~\\ref{app:classimbalance}) shows that the bias identity maintains $R^2 \\geq 0.976$ even at $P(Z{=}1) = 0.1$ for $K{=}2$, though EC-HTE's RMSE ratio relative to global correction increases to 1.06--1.68 as class imbalance grows.\nIn practice, NLP classification tasks often exhibit substantial class imbalance (e.g., hate speech prevalence $\\ll 50\\%$), and practitioners should verify that the per-subgroup expert budget threshold remains satisfied under the actual class distribution.\nEmpirical verification (Section~\\ref{sec:bias_mechanism}) yields $R^2 = 0.994$ for $K{=}2$ and $R^2 = 0.974$ for $K{=}4$; the residual variance reflects finite-sample Monte Carlo noise, not model misspecification.\n\n\\paragraph{Sensitivity to (A1).}\nAssumption~(A1) is not empirically testable.\nIf misclassification correlates with potential outcomes ($\\gamma = \\mathrm{Corr}(\\mathbb{1}[\\hat{Z} {\\neq} Z],\\, Y(1){-}Y(0) \\mid Z, S) \\neq 0$), Theorem~\\ref{thm:bias_identity} gains an $O(\\gamma)$ perturbation; in NLP settings, this is plausible when LLM accuracy varies with outcome magnitude.\nSensitivity analysis frameworks~\\cite{lash2009applying,dorn2022sharp} can bound the degradation (Section~\\ref{sec:limitations}).\n\n\\paragraph{Finite-sample remainder.}\nTheorem~\\ref{thm:bias_identity} is an exact population identity.\nIn practice, confusion matrices are estimated from $n_{\\text{expert}}$ expert labels with $\\hat{C}_s = C_s + E_s$, $\\|E_s\\| = O_p(n_{\\text{expert}}^{-1/2})$; the resulting remainder is therefore $R_n = O_p(n_{\\text{expert}}^{-1/2} \\cdot \\kappa(C_s))$, motivating the singularity guard ($\\kappa > 100 \\to$ fallback) in Section~\\ref{sec:method}.\n\n\\begin{proposition}[Debiasing Can Increase Bias]\n\\label{prop:debiasing_hurts}\nUnder \\textnormal{(A1)--(A5)}, global correction produces larger absolute bias than the naive estimator ($|\\mathrm{bias}_{\\mathrm{global}}| > |\\mathrm{bias}_{\\mathrm{naive}}|$) in subgroup $s$ if and only if\n\\begin{equation}\n\\frac{|\\delta_s|}{(1 - 2\\bar{\\pi}) \\cdot \\pi_s} > 1.\n\\label{eq:hurts_condition}\n\\end{equation}\n\\end{proposition}\n\nEquation~\\eqref{eq:hurts_condition} partitions subgroups into two regimes.\nFor high-error subgroups ($\\pi_s > \\bar{\\pi}$), the condition reduces to $\\pi_s > 0.5$, excluded by~(A4).\nFor low-error subgroups ($\\pi_s < \\bar{\\pi}$), it holds whenever $\\pi_s < \\bar{\\pi} / (2(1 - \\bar{\\pi}))$---easily satisfied: when $\\bar{\\pi} = 0.15$, any subgroup with $\\pi_s < 0.088$ is harmed.\nThe mechanism is over-correction: global inversion applies a correction calibrated for the average error rate, so low-error subgroups are overcorrected (the correction overshoots and reverses bias sign) while high-error subgroups are under-corrected.\nFor subgroups with near-zero misclassification ($\\pi_s \\approx 0$), the naive estimator is nearly unbiased, yet global correction creates substantial bias---debiasing can be worse than doing nothing.\n\nIn our experiments (Section~\\ref{sec:bias_mechanism}), global correction increases bias in 50\\% of $K{=}2$ configurations across our parameter grid (260 of 520, excluding cases where $\\Delta\\pi{=}0$).\nWith the difference-in-means estimator, maximum amplification reaches $2.86\\times$ for $K{=}2$ and $2.41\\times$ for $K{=}4$; the mechanism operates across estimator types, with nonlinear estimators amplifying the effect further (Section~\\ref{sec:ec_hte_eval}).\nFigure~\\ref{fig:heatmap} visualizes the amplification across the full $\\Delta\\pi \\times \\Delta\\tau$ parameter grid.",
    "structuredPatch": [
      {
        "oldStart": 76,
        "oldLines": 7,
        "newStart": 76,
        "newLines": 7,
        "lines": [
          " Sensitivity analysis frameworks~\\cite{lash2009applying,dorn2022sharp} can bound the degradation (Section~\\ref{sec:limitations}).",
          " ",
          " \\paragraph{Finite-sample remainder.}",
          "-Theorem~\\ref{thm:bias_identity} is an exact population identity.",
          "+Theorem~\\ref{thm:bias_identity} is a population-level identity.",
          " In practice, confusion matrices are estimated from $n_{\\text{expert}}$ expert labels with $\\hat{C}_s = C_s + E_s$, $\\|E_s\\| = O_p(n_{\\text{expert}}^{-1/2})$; the resulting remainder is therefore $R_n = O_p(n_{\\text{expert}}^{-1/2} \\cdot \\kappa(C_s))$, motivating the singularity guard ($\\kappa > 100 \\to$ fallback) in Section~\\ref{sec:method}.",
          " ",
          " \\begin{proposition}[Debiasing Can Increase Bias]"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Edit · `toolu_01GUxySGi8nByTFnqiX6ak2K`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex",
  "old_string": "Second, Theorem~\\ref{thm:bias_identity} derives an exact identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.",
  "new_string": "Second, Theorem~\\ref{thm:bias_identity} derives a bias identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "e1faf7c3-c58c-4d47-b398-dc4aba3f98c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ej86nXZny8D22LgdS358EU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 53001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-23T09:28:57.945Z_

<details><summary>↩ Tool result · `toolu_01GUxySGi8nByTFnqiX6ak2K`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "e2b3542a-d2df-4ca9-8566-e4cef7224157",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex",
    "oldString": "Second, Theorem~\\ref{thm:bias_identity} derives an exact identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.",
    "newString": "Second, Theorem~\\ref{thm:bias_identity} derives a bias identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.",
    "originalFile": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Measurement error and annotation models.}\nClassical measurement error theory shows that correction via estimated error models can amplify MSE when the error structure is misspecified~\\cite{fuller1987measurement,carroll2006measurement}; Bayesian approaches require informative priors when identification is weak~\\cite{gustafson2003measurement}, and nonparametric methods use repeated measurements or instruments to recover the true distribution~\\cite{hu2008nonparametric}.\n\nThree distinctions separate our contribution from prior measurement error analyses.\nFirst, we study effect modifier misclassification---the mismeasured variable defines the CATE function itself---rather than regressor~\\cite{frazis2003estimating,carroll2006measurement} or confounder~\\cite{ogburn2012nondifferential,greenland1980effect} error, where attenuation is the primary concern.\nSecond, Theorem~\\ref{thm:bias_identity} derives an exact identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.\nConcretely, \\citet{frazis2003estimating} derive scalar attenuation $\\tilde{\\beta} = \\beta(1 - \\pi_0 - \\pi_1)$ for the uncorrected estimator under homogeneous misclassification; Theorem~\\ref{thm:bias_identity} characterizes a structurally distinct quantity---correction-induced bias $\\delta_s \\cdot \\Delta\\tau / (1 - 2\\bar{\\pi})$---that is subgroup-specific, potentially sign-reversing, and absent from the uncorrected estimator.\nThe homogeneous-error setting is a degenerate case: with $K{=}1$, $\\delta_s{=}0$ and correction-induced bias vanishes, recovering the classical attenuation result.\nThe algebraic mechanisms also differ: OLS attenuation under misclassified regressors~\\cite{frazis2003estimating,blackwell2017unified} versus confusion matrix inversion that redistributes error across subgroups with heterogeneous rates.\nWe empirically verify this distinction: F-L correction---even when applied per subgroup---produces higher bias than the naive estimator under heterogeneous misclassification, whereas EC-HTE achieves near-oracle performance (Appendix~\\ref{app:fl_comparison}).\nThird, the $\\delta_s \\cdot \\Delta\\tau$ product structure arises only under heterogeneous error rates; all homogeneous-error analyses~\\cite{battistin2014treatment,fong2021machine} miss this interaction entirely.\nIn the annotation literature, \\citet{dawid1979maximum} introduced confusion matrix estimation for multiple annotators, with extensions to item difficulty, annotator competence, and hierarchical priors~\\cite{passonneau2014benefits,hovy2013learning,paun2018comparing}.\nOur hierarchical estimator (Section~\\ref{sec:method}) adapts this architecture from label aggregation to causal inference, tying the prior structure to the subgroup dimension that defines treatment effect heterogeneity.\n\n\\paragraph{HTE estimation and LLM annotation error.}\nCausal forests~\\cite{athey2016recursive,wager2018causal}, double/debiased ML~\\cite{chernozhukov2018dml,semenova2021debiased}, doubly-robust CATE estimators~\\cite{kennedy2023dr}, and meta-learners~\\cite{kunzel2019metalearners} all assume that covariates defining heterogeneity are observed without error; when the effect modifier is misclassified, CATE estimates conflate effects across groups.\nEC-HTE provides upstream correction that restores valid inputs to any downstream estimator.\nThe corrected pseudo-outcomes are in principle compatible with other HTE estimators such as the R-learner~\\citep{nie2021quasi}.\nFor broader perspectives on causal inference with text data, see \\citet{feder2022causal} and \\citet{keith2020text}; \\citet{wang2020methods} study inference correction when outcomes are ML-predicted, a related but distinct problem from effect modifier misclassification.\nLLMs now match crowd-worker accuracy on many classification tasks~\\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,pangakis2023automated}, but \\citet{ashwin2025bias} show that error rates vary by up to $5\\times$ across demographic subgroups.\nThis subgroup-varying error is the failure mode we address: it distorts the very contrasts that define the research question, and prior work documents the pattern without providing a correction mechanism for downstream causal estimands.\nConcurrent work identifies variance-side measurement error from LLM pipeline design choices~\\cite{messing2026hidden}; our framework addresses the complementary bias-side problem from heterogeneous misclassification rates across subgroups.\nTemperature or Platt scaling~\\cite{guo2017calibration} reduces per-subgroup $\\pi_s$ but does not eliminate heterogeneity $\\Delta\\pi$; EC-HTE corrects the residual $\\delta_s$-driven bias that persists post-calibration (Appendix~\\ref{app:calibration} empirically confirms this complementarity).\n\n\\paragraph{Prediction-powered and design-based correction.}\nPPI~\\cite{angelopoulos2023ppi,zrnic2024cross} and DSL~\\cite{egami2024dsl} correct population-level aggregates assuming homogeneous prediction error.\nIn our setting---binary effect modifier with known subgroup structure, a special case of the broader problems DSL addresses---DSL's measurement error correction reduces, under the confusion-matrix parameterization we adopt, to confusion matrix inversion: pooled DSL is equivalent to our Global baseline, and per-subgroup DSL to Stratified MLE (Section~\\ref{sec:ec_hte_eval}; Appendix~\\ref{app:ppi_comparison}).\nEC-HTE adds hierarchical partial pooling across subgroups, borrowing strength to reduce variance---a mechanism outside the DSL framework.\n\\citet{audinet2025benchmarking} benchmark DSL and PPI debiasing for LLM-based parameter estimation, documenting bias-variance tradeoffs analogous to our findings; their analysis targets population-level parameters rather than subgroup-conditional estimands, leaving the $\\delta_s \\cdot \\Delta\\tau$ interaction we formalize unaddressed.\n\\citet{mozer2026ppi} extend PPI to arm-specific ATE correction; PPCI~\\cite{sui2026ppci} targets conditional estimands but corrects outcome-side error ($\\hat{Y}$ given true $Z$), not covariate-side misclassification; ForestIV~\\cite{bu2023forestiv} targets the outcome model rather than the heterogeneity structure.\nNone corrects bias when the mismeasured variable is the effect modifier indexing the CATE function.\n\\citet{imai2010causal} study treatment misclassification, requiring instrumental variables or partial identification; our problem is structurally distinct because the treatment is observed correctly but the effect modifier is misclassified, admitting exact correction through confusion matrices rather than bounds.\nExtended discussion of these distinctions appears in Appendix~\\ref{app:related}.\nOur validation combines synthetic DGPs, semi-synthetic experiments, and real LLM confusion matrices, consistent with PPI and DSL evaluation methodology; Appendix~\\ref{app:multilm} validates both $\\Delta\\pi$ heterogeneity and the bias identity itself ($R^2 = 0.975$) across 11 model--dataset combinations.\n",
    "structuredPatch": [
      {
        "oldStart": 6,
        "oldLines": 7,
        "newStart": 6,
        "newLines": 7,
        "lines": [
          " ",
          " Three distinctions separate our contribution from prior measurement error analyses.",
          " First, we study effect modifier misclassification---the mismeasured variable defines the CATE function itself---rather than regressor~\\cite{frazis2003estimating,carroll2006measurement} or confounder~\\cite{ogburn2012nondifferential,greenland1980effect} error, where attenuation is the primary concern.",
          "-Second, Theorem~\\ref{thm:bias_identity} derives an exact identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.",
          "+Second, Theorem~\\ref{thm:bias_identity} derives a bias identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.",
          " Concretely, \\citet{frazis2003estimating} derive scalar attenuation $\\tilde{\\beta} = \\beta(1 - \\pi_0 - \\pi_1)$ for the uncorrected estimator under homogeneous misclassification; Theorem~\\ref{thm:bias_identity} characterizes a structurally distinct quantity---correction-induced bias $\\delta_s \\cdot \\Delta\\tau / (1 - 2\\bar{\\pi})$---that is subgroup-specific, potentially sign-reversing, and absent from the uncorrected estimator.",
          " The homogeneous-error setting is a degenerate case: with $K{=}1$, $\\delta_s{=}0$ and correction-induced bias vanishes, recovering the classical attenuation result.",
          " The algebraic mechanisms also differ: OLS attenuation under misclassified regressors~\\cite{frazis2003estimating,blackwell2017unified} versus confusion matrix inversion that redistributes error across subgroups with heterogeneous rates."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Edit · `toolu_01HbL3DtPLakTSpJXoUqNXpd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex",
  "old_string": "We derived an exact bias identity (Theorem~\\ref{thm:bias_identity})",
  "new_string": "We derived a bias identity (Theorem~\\ref{thm:bias_identity})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "1175226d-698e-4494-b199-9a45d4398509",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ej86nXZny8D22LgdS358EU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 53001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-23T09:28:58.096Z_

<details><summary>↩ Tool result · `toolu_01HbL3DtPLakTSpJXoUqNXpd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "11fd1cbc-7fa7-4c42-962a-8b3fdd0406c8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex",
    "oldString": "We derived an exact bias identity (Theorem~\\ref{thm:bias_identity})",
    "newString": "We derived a bias identity (Theorem~\\ref{thm:bias_identity})",
    "originalFile": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe derived an exact bias identity (Theorem~\\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup-level bias proportional to $\\delta_s \\cdot \\Delta\\tau$, worsening CATE estimates in 50\\% of $K{=}2$ configurations.\nEC-HTE provides subgroup-stratified correction via hierarchical Bayes; the companion diagnostic (Proposition~\\ref{prop:debiasing_hurts}; AUC $= 1.0$ on subgroups with $\\tau_s > 0$) flags harmful correction using only per-subgroup misclassification rates.\nEC-HTE's advantage requires sufficient $\\Delta\\pi$ and expert budget; more broadly, the bias identity applies whenever any proxy classifier with subgroup-varying error rates serves as an effect modifier in causal inference.",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\section{Conclusion}\\label{sec:conclusion}",
          " ",
          "-We derived an exact bias identity (Theorem~\\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup-level bias proportional to $\\delta_s \\cdot \\Delta\\tau$, worsening CATE estimates in 50\\% of $K{=}2$ configurations.",
          "+We derived a bias identity (Theorem~\\ref{thm:bias_identity}): global confusion-matrix correction introduces subgroup-level bias proportional to $\\delta_s \\cdot \\Delta\\tau$, worsening CATE estimates in 50\\% of $K{=}2$ configurations.",
          " EC-HTE provides subgroup-stratified correction via hierarchical Bayes; the companion diagnostic (Proposition~\\ref{prop:debiasing_hurts}; AUC $= 1.0$ on subgroups with $\\tau_s > 0$) flags harmful correction using only per-subgroup misclassification rates.",
          " EC-HTE's advantage requires sufficient $\\Delta\\pi$ and expert budget; more broadly, the bias identity applies whenever any proxy classifier with subgroup-varying error rates serves as an effect modifier in causal inference.",
          "\\ No newline at end of file"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Edit · `toolu_01Rzrwgwmw3w91NWE9Xvwb5i`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex",
  "old_string": "Configuration & Method & $|\\text{Bias}|$ & RMSE & Cov. \\\\",
  "new_string": "Configuration & Method & $|\\text{Bias}|$ & RMSE & 95\\% CI Cov. \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "03b6fb54-f5da-47d5-bbbc-65c62d52011c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ej86nXZny8D22LgdS358EU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 53001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-23T09:28:58.779Z_

<details><summary>↩ Tool result · `toolu_01Rzrwgwmw3w91NWE9Xvwb5i`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "429b7d66-d132-44f1-ba16-2e6d3b11218c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex",
    "oldString": "Configuration & Method & $|\\text{Bias}|$ & RMSE & Cov. \\\\",
    "newString": "Configuration & Method & $|\\text{Bias}|$ & RMSE & 95\\% CI Cov. \\\\",
    "originalFile": "\\section{Experiments}\n\n\\subsection{Setup}\n\nWe test on synthetic ($N{=}5{,}000$, $K \\in \\{2, 4\\}$, controlled $\\Delta\\tau$ and $\\Delta\\pi$, 100 MC runs) and semi-synthetic (TweetEval sentiment~\\cite{barbieri2020tweeteval}, $K{=}4$ unbalanced subgroups, $\\pi \\in \\{0.05, 0.10, 0.15, 0.25\\}$) DGPs; full specifications in Appendix~\\ref{app:dgp}.\n\nWe compare: (1) \\textit{Naive} (no correction), (2) \\textit{Global} (pooled confusion matrix, equivalent to PPI/DSL~\\cite{angelopoulos2023ppi,egami2024dsl} with homogeneous error), (3) \\textit{Stratified MLE} (per-subgroup DSL without shrinkage), (4) \\textit{HB EC-HTE} (our method), (5) \\textit{PPCI}~\\cite{sui2026ppci}, and (6) \\textit{EC-HTE+PPCI}.\nFor CausalForest~\\cite{wager2018causal}, we compare naive, global, and EC-HTE variants.\nPrimary metrics are $|\\text{bias}|$, RMSE, and 95\\% CI coverage, averaged across subgroups and 100 MC runs.\nRobustness validation covers hate speech, six OpenAI models, subgroup misspecification, asymmetric confusion matrices, confounded treatment, and outcome-dependent misclassification (all $\\geq$93.5\\% coverage; Appendices~\\ref{app:hatespeech}--\\ref{app:a1_sensitivity}).\n\n\\subsection{Empirical Validation of the Bias Identity}\n\\label{sec:bias_mechanism}\n\nWe verify Theorem~\\ref{thm:bias_identity} on a $K{=}2$ grid (520 configurations, $\\Delta\\pi \\in [0, 0.25]$, $\\Delta\\tau \\in (0, 0.50]$) and a $K{=}4$ grid (Appendix~\\ref{app:dgp}).\nRegressing observed subgroup bias on $\\delta_s \\cdot \\Delta\\tau / (1{-}2\\bar{\\pi})$ yields $R^2 = 0.994$ ($K{=}2$) and $0.974$ ($K{=}4$); residual variance reflects MC noise ($R^2 \\geq 0.976$ even at $P(Z{=}1) = 0.1$; Appendix~\\ref{app:classimbalance}).\nGlobal correction worsens bias in 50\\% of $K{=}2$ configurations (260/520, excluding $\\Delta\\pi{=}0$), with amplification reaching 2.86$\\times$ ($K{=}2$) and 2.41$\\times$ ($K{=}4$); Figure~\\ref{fig:heatmap} visualizes the amplification surface.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig2_heatmap.pdf}\n\\caption{Bias amplification under global correction ($K{=}2$). (a) Low-error subgroup: correction always helps. (b) High-error subgroup: correction \\emph{increases} bias when $\\Delta\\pi > 0.12$ (hatched), reaching 2.86$\\times$.}\n\\label{fig:heatmap}\n\\end{figure*}\n\n\\subsection{EC-HTE Evaluation}\n\\label{sec:ec_hte_eval}\n\nTable~\\ref{tab:main_results} presents the main results across representative configurations.\nNotably, in the $K{=}2$ extreme row, global correction \\emph{increases} $|\\text{bias}|$ relative to naive (0.059 vs.\\ 0.058)---a direct manifestation of Theorem~\\ref{thm:bias_identity}: pooled correction overshoots in low-error subgroups.\nHB EC-HTE reduces $|\\text{bias}|$ from 0.059 to 0.008 (7.4$\\times$) at $K{=}2$ and from 0.056 to 0.012 (4.7$\\times$) at $K{=}4$, maintaining near-nominal coverage (0.94--0.96) with lower RMSE than stratified MLE.\nUnder moderate heterogeneity ($K{=}2$), methods converge: EC-HTE and global achieve comparable bias ($p > 0.05$; Table~\\ref{tab:main_supp}).\nIn the semi-synthetic TweetEval experiment ($K{=}4$, $n_{\\text{expert}}{=}250$), EC-HTE and Global achieve comparable $|\\text{bias}|$ ($p{=}0.395$; Table~\\ref{tab:main_supp}), but EC-HTE incurs higher RMSE (0.225 vs.\\ 0.124), driven by moderate $\\Delta\\pi{=}0.20$ and unbalanced subgroups receiving ${\\sim}30$ expert labels each.\nWhen $\\Delta\\pi$ or per-subgroup budget is marginal, global correction is competitive on aggregate RMSE.\n\n\\paragraph{CausalForest.}\nWith CausalForest~\\cite{wager2018causal} ($K{=}4$, extreme, $n{=}500$), EC-HTE reduces $|\\text{bias}|$ from 0.191 to 0.039 (4.9$\\times$), improving coverage from 0.58 to 0.90; global correction amplifies naive bias up to 5.9$\\times$ because the forest magnifies label errors (Table~\\ref{tab:main_results}).\nThe residual coverage gap (90\\% vs.\\ oracle 94--96\\%) reflects asymmetric $M^{-1}$ SE propagation rather than CM estimation error; a full bootstrap SE can improve coverage calibration (Appendix~\\ref{app:bootstrap_se}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results (extreme heterogeneity). Metrics averaged over subgroups, $z$-levels, 100 MC runs. Bold: lowest $|\\text{bias}|$. $^\\dagger$RMSE exceeds Global. Moderate heterogeneity and TweetEval results---where methods converge and EC-HTE RMSE exceeds Global---in Table~\\ref{tab:main_supp}; MC SEs in Appendix~\\ref{app:mcse}.}\n\\label{tab:main_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll ccc}\n\\toprule\nConfiguration & Method & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{DIM\\\\$K{=}2$, $n{=}250$}}\n & Naive & 0.058 & 0.090 & 0.82 \\\\\n & Global & 0.059 & 0.099 & 0.87 \\\\\n & Strat.\\ MLE & 0.012 & 0.094 & 0.95 \\\\\n & HB EC-HTE & \\textbf{0.008} & 0.089 & 0.94 \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{DIM\\\\$K{=}4$, $n{=}500$}}\n & Naive & 0.062 & 0.113 & 0.88 \\\\\n & Global & 0.056 & 0.125 & 0.91 \\\\\n & Strat.\\ MLE & \\textbf{0.010} & 0.127$^\\dagger$ & 0.95 \\\\\n & HB EC-HTE & 0.012 & 0.120 & 0.96 \\\\\n\\midrule\n\\multirow{3}{*}{\\shortstack[l]{CausalForest\\\\$K{=}4$, $n{=}500$}}\n & Naive & 0.208 & 0.231 & 0.44 \\\\\n & Global & 0.191 & 0.244 & 0.58 \\\\\n & EC-HTE Forest & \\textbf{0.039} & 0.180 & 0.90 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Actionable Diagnostic Without EC-HTE}\n\\label{sec:diagnostic}\n\nProposition~\\ref{prop:debiasing_hurts} provides a $\\Delta\\tau$-free diagnostic: global correction increases bias in subgroup $s$ iff $|\\delta_s| / ((1-2\\bar{\\pi}) \\cdot \\pi_s) > 1$, computable from a pilot sample without estimating treatment effects.\nA threshold classifier achieves AUC = 0.86 at the subgroup level (Figure~\\ref{fig:roc}, Appendix).\nOn real LLM confusion matrices (16 combinations; Appendix~\\ref{app:screening}), AUC decreases to 0.63, primarily from subgroups with $\\tau_s \\approx 0$ where both naive and corrected bias are near zero, making the ground-truth harm label indeterminate; on subgroups with $\\tau_s > 0$, AUC reaches 1.0.\nFor $K{=}2$, $|\\delta_0|{=}|\\delta_1|$ forces ranking by $1/\\pi_s$ alone, which can anti-predict harm; reliability is strongest for $K{\\geq}4$.\nA computable meta-criterion recovers reliability: when $\\max_s \\mathrm{score}(s) > 1$, the diagnostic achieves AUC $\\geq 0.75$ across all 16 combinations; when $\\max_s \\mathrm{score}(s) \\leq 1$, AUC drops to 0.0--0.67 (Appendix~\\ref{app:screening}).\n\nA recommended practitioner workflow and budget crossover curves appear in Appendices~\\ref{sec:budget}--\\ref{app:screening}.\nAt $K{=}8$ with $n_{\\text{expert}}{=}250$, EC-HTE maintains nominal coverage (95.6\\%) but RMSE exceeds global correction, establishing a practical scalability boundary (Appendix~\\ref{app:k8_subgroups}).\nThe bias identity further validates across eight LLMs spanning 11 model--dataset combinations ($R^2 = 0.975$; Appendix~\\ref{app:multilm}).",
    "structuredPatch": [
      {
        "oldStart": 44,
        "oldLines": 7,
        "newStart": 44,
        "newLines": 7,
        "lines": [
          " \\resizebox{\\columnwidth}{!}{%",
          " \\begin{tabular}{ll ccc}",
          " \\toprule",
          "-Configuration & Method & $|\\text{Bias}|$ & RMSE & Cov. \\\\",
          "+Configuration & Method & $|\\text{Bias}|$ & RMSE & 95\\% CI Cov. \\\\",
          " \\midrule",
          " \\multirow{4}{*}{\\shortstack[l]{DIM\\\\$K{=}2$, $n{=}250$}}",
          "  & Naive & 0.058 & 0.090 & 0.82 \\\\"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Edit · `toolu_019LBzWD72snw42CjtFjXGDu`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib",
  "old_string": "  year={2025},\n  doi={10.1177/08944393241286471},\n  publisher={SAGE Publications}\n}",
  "new_string": "  year={2024},\n  doi={10.1177/08944393241286471},\n  publisher={SAGE Publications}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "5c5d4144-483a-4c86-a70a-ac8933288ed3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ej86nXZny8D22LgdS358EU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 53001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-23T09:29:00.280Z_

<details><summary>↩ Tool result · `toolu_019LBzWD72snw42CjtFjXGDu`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "e057ca60-2f76-46e3-89b4-d8b0887fe640",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib",
    "oldString": "  year={2025},\n  doi={10.1177/08944393241286471},\n  publisher={SAGE Publications}\n}",
    "newString": "  year={2024},\n  doi={10.1177/08944393241286471},\n  publisher={SAGE Publications}\n}",
    "originalFile": "% === Datasets ===\n\n@inproceedings{borkan2019nuanced,\n  title={Nuanced Metrics for Measuring Unintended Bias with Real Data for Text Classification},\n  author={Borkan, Daniel and Dixon, Lucas and Sorensen, Jeffrey and Thain, Nithum and Vasserman, Lucy},\n  booktitle={Companion Proceedings of The 2019 World Wide Web Conference},\n  pages={491--500},\n  year={2019}\n}\n\n% === Econometrics of Binary Misclassification ===\n\n@incollection{bound2001measurement,\n  title={Measurement Error in Survey Data},\n  author={Bound, John and Brown, Charles and Mathiowetz, Nancy},\n  booktitle={Handbook of Econometrics},\n  volume={5},\n  pages={3705--3843},\n  year={2001},\n  publisher={Elsevier}\n}\n\n@article{greenland1980effect,\n  title={The Effect of Misclassification in the Presence of Covariates},\n  author={Greenland, Sander},\n  journal={American Journal of Epidemiology},\n  volume={112},\n  number={4},\n  pages={564--569},\n  year={1980}\n}\n\n@article{frazis2003estimating,\n  title={Estimating Linear Regressions with Mismeasured, Possibly Endogenous, Binary Explanatory Variables},\n  author={Frazis, Harley and Loewenstein, Mark A.},\n  journal={Journal of Econometrics},\n  volume={117},\n  number={1},\n  pages={151--178},\n  year={2003}\n}\n\n@article{black2000racial,\n  title={The Impact of Economic Conditions on Participation in Disability Programs: Evidence from the Coal Boom and Bust},\n  author={Black, Dan and Daniel, Kermit and Sanders, Seth},\n  journal={American Economic Review},\n  volume={90},\n  number={1},\n  pages={27--50},\n  year={2000}\n}\n\n@article{mahajan2006identification,\n  title={Identification and Estimation of Regression Models with Misclassification},\n  author={Mahajan, Aprajit},\n  journal={Econometrica},\n  volume={74},\n  number={3},\n  pages={631--665},\n  year={2006}\n}\n\n@article{lewbel2007estimation,\n  title={Estimation of Average Treatment Effects with Misclassification},\n  author={Lewbel, Arthur},\n  journal={Econometrica},\n  volume={75},\n  number={2},\n  pages={537--551},\n  year={2007}\n}\n\n% === Classical Measurement Error ===\n\n@article{blackwell2017unified,\n  title={A Unified Approach to Measurement Error and Missing Data: Overview and Applications},\n  author={Blackwell, Matthew and Honaker, James and King, Gary},\n  journal={Sociological Methods \\& Research},\n  volume={46},\n  number={3},\n  pages={303--341},\n  year={2017},\n  doi={10.1177/0049124115585360}\n}\n\n@book{fuller1987measurement,\n  title={Measurement Error Models},\n  author={Fuller, Wayne A.},\n  year={1987},\n  publisher={Wiley},\n  address={New York}\n}\n\n@book{carroll2006measurement,\n  title={Measurement Error in Nonlinear Models: A Modern Perspective},\n  author={Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu, Ciprian M.},\n  year={2006},\n  edition={2nd},\n  publisher={Chapman \\& Hall/CRC},\n  address={Boca Raton, FL}\n}\n\n@book{gustafson2003measurement,\n  title={Measurement Error and Misclassification in Statistics and Epidemiology: Impacts and Bayesian Adjustments},\n  author={Gustafson, Paul},\n  year={2003},\n  publisher={Chapman \\& Hall/CRC},\n  address={Boca Raton, FL},\n  doi={10.1201/9780203502761}\n}\n\n@article{hu2008nonparametric,\n  title={Instrumental Variable Treatment of Nonclassical Measurement Error Models},\n  author={Hu, Yingyao and Schennach, Susanne M.},\n  journal={Econometrica},\n  volume={76},\n  number={1},\n  pages={195--216},\n  year={2008},\n  doi={10.1111/j.0012-9682.2008.00823.x}\n}\n\n% === Bayesian Annotation Models ===\n\n@article{dawid1979maximum,\n  title={Maximum Likelihood Estimation of Observer Error-Rates Using the {EM} Algorithm},\n  author={Dawid, A. Philip and Skene, Allan M.},\n  journal={Applied Statistics},\n  volume={28},\n  number={1},\n  pages={20--28},\n  year={1979},\n  doi={10.2307/2346806}\n}\n\n@article{passonneau2014benefits,\n  title={The Benefits of a Model of Annotation},\n  author={Passonneau, Rebecca J. and Carpenter, Bob},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={2},\n  pages={311--326},\n  year={2014},\n  doi={10.1162/tacl_a_00185}\n}\n\n@inproceedings{hovy2013learning,\n  title={Learning Whom to Trust with {MACE}},\n  author={Hovy, Dirk and Berg-Kirkpatrick, Taylor and Vaswani, Ashish and Hovy, Eduard},\n  booktitle={Proceedings of NAACL-HLT},\n  pages={1120--1130},\n  year={2013}\n}\n\n@article{paun2018comparing,\n  title={Comparing {B}ayesian Models of Annotation},\n  author={Paun, Silviu and Carpenter, Bob and Chamberlain, Jon and Hovy, Dirk and Kruschwitz, Udo and Poesio, Massimo},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={6},\n  pages={571--585},\n  year={2018},\n  doi={10.1162/tacl_a_00040}\n}\n\n% === Causal Inference & HTE ===\n\n@article{athey2016recursive,\n  title={Recursive Partitioning for Heterogeneous Causal Effects},\n  author={Athey, Susan and Imbens, Guido},\n  journal={Proceedings of the National Academy of Sciences},\n  volume={113},\n  number={27},\n  pages={7353--7360},\n  year={2016},\n  doi={10.1073/pnas.1510489113}\n}\n\n@article{wager2018causal,\n  title={Estimation and Inference of Heterogeneous Treatment Effects using Random Forests},\n  author={Wager, Stefan and Athey, Susan},\n  journal={Journal of the American Statistical Association},\n  volume={113},\n  number={523},\n  pages={1228--1242},\n  year={2018},\n  doi={10.1080/01621459.2017.1319839}\n}\n\n@article{chernozhukov2018dml,\n  title={Double/Debiased Machine Learning for Treatment and Structural Parameters},\n  author={Chernozhukov, Victor and Chetverikov, Denis and Demirer, Mert and Duflo, Esther and Hansen, Christian and Newey, Whitney and Robins, James},\n  journal={The Econometrics Journal},\n  volume={21},\n  number={1},\n  pages={C1--C68},\n  year={2018},\n  doi={10.1111/ectj.12097}\n}\n\n@article{kennedy2023dr,\n  title={Towards Optimal Doubly Robust Estimation of Heterogeneous Causal Effects},\n  author={Kennedy, Edward H.},\n  journal={Electronic Journal of Statistics},\n  volume={17},\n  number={2},\n  pages={3008--3049},\n  year={2023},\n  doi={10.1214/23-EJS2157}\n}\n\n@article{kunzel2019metalearners,\n  title={Metalearners for Estimating Heterogeneous Treatment Effects Using Machine Learning},\n  author={K{\\\"u}nzel, S{\\\"o}ren R. and Sekhon, Jasjeet S. and Bickel, Peter J. and Yu, Bin},\n  journal={Proceedings of the National Academy of Sciences},\n  volume={116},\n  number={10},\n  pages={4156--4165},\n  year={2019},\n  doi={10.1073/pnas.1804597116}\n}\n\n@article{imai2010causal,\n  title={Causal Inference with Differential Measurement Error: Nonparametric Identification and Sensitivity Analysis},\n  author={Imai, Kosuke and Yamamoto, Teppei},\n  journal={American Journal of Political Science},\n  volume={54},\n  number={4},\n  pages={926--943},\n  year={2010},\n  doi={10.1111/j.1540-5907.2010.00446.x}\n}\n\n% === LLMs as Annotators ===\n\n@article{gilardi2023chatgpt,\n  title={{ChatGPT} Outperforms Crowd-Workers for Text-Annotation Tasks},\n  author={Gilardi, Fabrizio and Alizadeh, Meysam and Kubli, Ma{\\\"e}l},\n  journal={Proceedings of the National Academy of Sciences},\n  volume={120},\n  number={30},\n  pages={e2305016120},\n  year={2023},\n  doi={10.1073/pnas.2305016120}\n}\n\n@article{tornberg2024chatgpt,\n  title={Large Language Models Outperform Expert Coders and Supervised Classifiers at Annotating Political Social Media Messages},\n  author={T{\\\"o}rnberg, Petter},\n  journal={Social Science Computer Review},\n  year={2025},\n  doi={10.1177/08944393241286471},\n  publisher={SAGE Publications}\n}\n\n@article{ziems2024nlp,\n  title={Can Large Language Models Transform Computational Social Science?},\n  author={Ziems, Caleb and Held, William and Shaikh, Omar and Chen, Jiaao and Zhang, Zhehao and Yang, Diyi},\n  journal={Computational Linguistics},\n  volume={50},\n  number={1},\n  pages={237--291},\n  year={2024},\n  doi={10.1162/coli_a_00502}\n}\n\n@article{pangakis2023automated,\n  title={Automated Annotation with Generative {AI} Requires Validation},\n  author={Pangakis, Nicholas and Wolken, Samuel and Fasching, Neil},\n  journal={arXiv preprint arXiv:2306.00176},\n  year={2023}\n}\n\n@article{ashwin2025bias,\n  title={Using Large Language Models for Qualitative Analysis can Introduce Serious Bias},\n  author={Ashwin, Aditya and Swanson, Becca and Blair, Robert and Samii, Cyrus},\n  journal={Sociological Methods \\& Research},\n  year={2025},\n  doi={10.1177/00491241251313793}\n}\n\n% === PPI / DSL / Correction Methods ===\n\n@article{angelopoulos2023ppi,\n  title={Prediction-Powered Inference},\n  author={Angelopoulos, Anastasios N. and Bates, Stephen and Cand{\\`e}s, Emmanuel J. and Jordan, Michael I. and Lei, Lihua},\n  journal={Science},\n  volume={382},\n  number={6671},\n  pages={669--674},\n  year={2023},\n  doi={10.1126/science.adi6000}\n}\n\n@article{messing2026hidden,\n  title={Hidden Measurement Error in {LLM} Pipelines Distorts Annotation, Evaluation, and Benchmarking},\n  author={Messing, Solomon},\n  journal={arXiv preprint arXiv:2604.11581},\n  year={2026}\n}\n\n@article{zrnic2024cross,\n  title={Cross-Prediction-Powered Inference},\n  author={Zrnic, Tijana and Cand{\\`e}s, Emmanuel J.},\n  journal={Proceedings of the National Academy of Sciences},\n  volume={121},\n  number={15},\n  pages={e2322083121},\n  year={2024},\n  doi={10.1073/pnas.2322083121}\n}\n\n@inproceedings{zrnic2024active,\n  title={Active Statistical Inference},\n  author={Zrnic, Tijana and Cand{\\`e}s, Emmanuel J.},\n  booktitle={Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  series={PMLR},\n  volume={235},\n  year={2024}\n}\n\n@inproceedings{egami2024dsl,\n  title={Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models},\n  author={Egami, Naoki and Hinck, Musashi and Stewart, Brandon and Wei, Hanying},\n  booktitle={Advances in Neural Information Processing Systems},\n  volume={37},\n  year={2024}\n}\n\n@article{mozer2026ppi,\n  title={{PPI} is the Difference Estimator: Recognizing the Survey Sampling Roots of Prediction-Powered Inference},\n  author={Mozer, Reagan},\n  journal={arXiv preprint arXiv:2603.19160},\n  year={2026}\n}\n\n@article{sui2026ppci,\n  title={Prediction-Powered Conditional Inference},\n  author={Sui, Yijun and Cand{\\`e}s, Emmanuel J.},\n  journal={arXiv preprint arXiv:2603.05575},\n  year={2026}\n}\n\n@article{bu2023forestiv,\n  title={Achieving Reliable Causal Inference with Data-Mined Variables: A Random Forest Approach to the Measurement Error Problem},\n  author={Bu, Zhexin and Almond, David and Bhatt, Siddhartha and Goldsmith-Pinkham, Paul},\n  journal={INFORMS Journal on Data Science},\n  volume={2},\n  number={2},\n  pages={110--129},\n  year={2023},\n  doi={10.1287/ijds.2023.0026}\n}\n\n@article{fong2021machine,\n  title={Machine Learning Predictions as Regression Covariates},\n  author={Fong, Christian and Tyler, Matthew},\n  journal={Political Analysis},\n  volume={29},\n  number={1},\n  pages={48--64},\n  year={2021},\n  doi={10.1017/pan.2020.11}\n}\n\n% === CSS Methodology ===\n\n@book{grimmer2022text,\n  title={Text as Data: A New Framework for Machine Learning and the Social Sciences},\n  author={Grimmer, Justin and Roberts, Margaret E. and Stewart, Brandon M.},\n  year={2022},\n  publisher={Princeton University Press},\n  address={Princeton, NJ}\n}\n\n@article{audinet2025benchmarking,\n  title={Benchmarking Debiasing Methods for {LLM}-based Parameter Estimates},\n  author={Audinet de Pieuchon, Josias and Egami, Naoki and Alizadeh, Meysam and Gilardi, Fabrizio},\n  journal={Proceedings of EMNLP},\n  year={2025}\n}\n\n% === Semi-synthetic Data Source ===\n\n@inproceedings{barbieri2020tweeteval,\n  title={{TweetEval}: Unified Benchmark and Comparative Evaluation for Tweet Classification},\n  author={Barbieri, Francesco and Camacho-Collados, Jose and Espinosa-Anke, Luis and Neves, Leonardo},\n  booktitle={Findings of EMNLP},\n  pages={1644--1650},\n  year={2020},\n  doi={10.18653/v1/2020.findings-emnlp.148}\n}\n\n@article{wang2020methods,\n  title={Methods for Correcting Inference Based on Outcomes Predicted by Machine Learning},\n  author={Wang, Siruo and McCormick, Tyler H. and Leek, Jeffrey T.},\n  journal={Proceedings of the National Academy of Sciences},\n  volume={117},\n  number={48},\n  pages={30266--30275},\n  year={2020}\n}\n\n@article{feder2022causal,\n  title={Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond},\n  author={Feder, Amir and Keith, Katherine A. and Manzoor, Emaad and Pryzant, Reid and Sridhar, Dhanya and Wood-Doughty, Zach and Eisenstein, Jacob and Grimmer, Justin and Reichart, Roi and Roberts, Margaret E. and Stewart, Brandon M. and Veitch, Victor and Yang, Diyi},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={10},\n  pages={1171--1197},\n  year={2022}\n}\n\n@inproceedings{keith2020text,\n  title={Text and Causal Inference: A Review of Using Text to Remove Confounding from Causal Estimates},\n  author={Keith, Katherine A. and Jensen, David and O'Connor, Brendan},\n  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},\n  pages={5332--5344},\n  year={2020}\n}\n\n% === HTE Estimation ===\n\n@article{semenova2021debiased,\n  title={Debiased Machine Learning of Conditional Average Treatment Effects and Other Causal Functions},\n  author={Semenova, Vira and Chernozhukov, Victor},\n  journal={The Econometrics Journal},\n  volume={24},\n  number={2},\n  pages={264--289},\n  year={2021},\n  doi={10.1093/ectj/utaa027}\n}\n\n@article{nie2021quasi,\n  title={Quasi-Oracle Estimation of Heterogeneous Treatment Effects},\n  author={Nie, Xinkun and Wager, Stefan},\n  journal={Biometrika},\n  volume={108},\n  number={2},\n  pages={299--319},\n  year={2021},\n  doi={10.1093/biomet/asaa076}\n}\n\n% === Sensitivity Analysis for Misclassification ===\n\n@book{lash2009applying,\n  title={Applying Quantitative Bias Analysis to Epidemiologic Data},\n  author={Lash, Timothy L. and Fox, Matthew P. and Fink, Aliza K.},\n  publisher={Springer},\n  address={New York},\n  year={2009},\n  doi={10.1007/978-0-387-87959-8}\n}\n\n@article{dorn2022sharp,\n  title={Sharp Sensitivity Analysis for Inverse Propensity Weighting via Quantile Balancing},\n  author={Dorn, Jacob and Guo, Kevin and Kallus, Nathan},\n  journal={Journal of the American Statistical Association},\n  volume={118},\n  number={544},\n  pages={2645--2657},\n  year={2023},\n  doi={10.1080/01621459.2022.2064774}\n}\n\n% === Treatment Effects + Measurement Error ===\n\n@article{ogburn2012nondifferential,\n  title={On the Nondifferential Misclassification of a Binary Confounder},\n  author={Ogburn, Elizabeth L. and VanderWeele, Tyler J.},\n  journal={Epidemiology},\n  volume={23},\n  number={3},\n  pages={433--439},\n  year={2012},\n  doi={10.1097/EDE.0b013e31824d1f63}\n}\n\n@article{battistin2014treatment,\n  title={Treatment Effect Estimation with Covariate Measurement Error},\n  author={Battistin, Erich and Chesher, Andrew},\n  journal={Journal of Econometrics},\n  volume={178},\n  number={2},\n  pages={707--714},\n  year={2014},\n  doi={10.1016/j.jeconom.2013.10.006}\n}\n\n% === Real-Data Datasets ===\n\n@article{kennedy2020constructing,\n  title={Constructing Interval Variables via Faceted {Rasch} Measurement and Multitask Deep Learning: A Hate Speech Application},\n  author={Kennedy, Chris J. and Bacon, Geoff and Sahn, Alexander and von Vacano, Claudia},\n  journal={arXiv preprint arXiv:2009.10277},\n  year={2020}\n}\n\n@inproceedings{guo2017calibration,\n  title={On Calibration of Modern Neural Networks},\n  author={Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle={Proceedings of the 34th International Conference on Machine Learning},\n  pages={1321--1330},\n  year={2017}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 246,
        "oldLines": 7,
        "newStart": 246,
        "newLines": 7,
        "lines": [
          "   title={Large Language Models Outperform Expert Coders and Supervised Classifiers at Annotating Political Social Media Messages},",
          "   author={T{\\\"o}rnberg, Petter},",
          "   journal={Social Science Computer Review},",
          "-  year={2025},",
          "+  year={2024},",
          "   doi={10.1177/08944393241286471},",
          "   publisher={SAGE Publications}",
          " }"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 60_

<details><summary>Logged reasoning block</summary>

```text
Good, the basic edits are done. Now let me do:
1. H3: Add 3 bib entries + related_work.tex edits (compress + add citations)
2. H4: Add cross-reference in theory.tex
3. H5: Orthogonal → complementary in appendix.tex

Let me do these now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "7c1208b6-52ba-40ff-af0b-a899ba033860",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfTCbq1mJavYLkU3D8YAFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14448,
      "cache_read_input_tokens": 53368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14448
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 61_

Now H3 (add references + related_work edits), H4 (theory cross-reference), and H5 (orthogonal→complementary in appendix).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "5a575a8b-1a6c-463c-85e2-77278d7dfb39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfTCbq1mJavYLkU3D8YAFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14448,
      "cache_read_input_tokens": 53368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14448
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Edit · `toolu_01LDhtWmiVpEXgdjTvFYtLJe`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib",
  "old_string": "@inproceedings{guo2017calibration,\n  title={On Calibration of Modern Neural Networks},\n  author={Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle={Proceedings of the 34th International Conference on Machine Learning},\n  pages={1321--1330},\n  year={2017}\n}",
  "new_string": "@inproceedings{guo2017calibration,\n  title={On Calibration of Modern Neural Networks},\n  author={Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle={Proceedings of the 34th International Conference on Machine Learning},\n  pages={1321--1330},\n  year={2017}\n}\n\n@article{camuffo2025variance,\n  title={Variance-Aware {LLM} Annotation for Strategy Research},\n  author={Camuffo, Matteo and Gambardella, Alfonso and Kazemi, Maryam and Malachowski, Daniel and Pandey, Alok},\n  journal={arXiv preprint arXiv:2601.02370},\n  year={2025}\n}\n\n@article{cheng2024err,\n  title={To Err Is Human; To Annotate, {SILICON}?},\n  author={Cheng, Myeongjun and Mayya, Rachit and Sedoc, Jo\\~{a}o},\n  journal={arXiv preprint arXiv:2412.14461},\n  year={2024}\n}\n\n@article{ura2015heterogeneous,\n  title={Heterogeneous Treatment Effects with Mismeasured Endogenous Treatment},\n  author={Ura, Takuya},\n  journal={arXiv preprint arXiv:1511.04162},\n  year={2015}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "8755d7ba-4141-47f1-be8c-4cd5cb7c3539",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfTCbq1mJavYLkU3D8YAFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14448,
      "cache_read_input_tokens": 53368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14448
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-23T09:29:14.094Z_

<details><summary>↩ Tool result · `toolu_01LDhtWmiVpEXgdjTvFYtLJe`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "2a980d60-8ca2-48ca-aa24-dd9a7bf77b0e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib",
    "oldString": "@inproceedings{guo2017calibration,\n  title={On Calibration of Modern Neural Networks},\n  author={Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle={Proceedings of the 34th International Conference on Machine Learning},\n  pages={1321--1330},\n  year={2017}\n}",
    "newString": "@inproceedings{guo2017calibration,\n  title={On Calibration of Modern Neural Networks},\n  author={Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle={Proceedings of the 34th International Conference on Machine Learning},\n  pages={1321--1330},\n  year={2017}\n}\n\n@article{camuffo2025variance,\n  title={Variance-Aware {LLM} Annotation for Strategy Research},\n  author={Camuffo, Matteo and Gambardella, Alfonso and Kazemi, Maryam and Malachowski, Daniel and Pandey, Alok},\n  journal={arXiv preprint arXiv:2601.02370},\n  year={2025}\n}\n\n@article{cheng2024err,\n  title={To Err Is Human; To Annotate, {SILICON}?},\n  author={Cheng, Myeongjun and Mayya, Rachit and Sedoc, Jo\\~{a}o},\n  journal={arXiv preprint arXiv:2412.14461},\n  year={2024}\n}\n\n@article{ura2015heterogeneous,\n  title={Heterogeneous Treatment Effects with Mismeasured Endogenous Treatment},\n  author={Ura, Takuya},\n  journal={arXiv preprint arXiv:1511.04162},\n  year={2015}\n}",
    "originalFile": "% === Datasets ===\n\n@inproceedings{borkan2019nuanced,\n  title={Nuanced Metrics for Measuring Unintended Bias with Real Data for Text Classification},\n  author={Borkan, Daniel and Dixon, Lucas and Sorensen, Jeffrey and Thain, Nithum and Vasserman, Lucy},\n  booktitle={Companion Proceedings of The 2019 World Wide Web Conference},\n  pages={491--500},\n  year={2019}\n}\n\n% === Econometrics of Binary Misclassification ===\n\n@incollection{bound2001measurement,\n  title={Measurement Error in Survey Data},\n  author={Bound, John and Brown, Charles and Mathiowetz, Nancy},\n  booktitle={Handbook of Econometrics},\n  volume={5},\n  pages={3705--3843},\n  year={2001},\n  publisher={Elsevier}\n}\n\n@article{greenland1980effect,\n  title={The Effect of Misclassification in the Presence of Covariates},\n  author={Greenland, Sander},\n  journal={American Journal of Epidemiology},\n  volume={112},\n  number={4},\n  pages={564--569},\n  year={1980}\n}\n\n@article{frazis2003estimating,\n  title={Estimating Linear Regressions with Mismeasured, Possibly Endogenous, Binary Explanatory Variables},\n  author={Frazis, Harley and Loewenstein, Mark A.},\n  journal={Journal of Econometrics},\n  volume={117},\n  number={1},\n  pages={151--178},\n  year={2003}\n}\n\n@article{black2000racial,\n  title={The Impact of Economic Conditions on Participation in Disability Programs: Evidence from the Coal Boom and Bust},\n  author={Black, Dan and Daniel, Kermit and Sanders, Seth},\n  journal={American Economic Review},\n  volume={90},\n  number={1},\n  pages={27--50},\n  year={2000}\n}\n\n@article{mahajan2006identification,\n  title={Identification and Estimation of Regression Models with Misclassification},\n  author={Mahajan, Aprajit},\n  journal={Econometrica},\n  volume={74},\n  number={3},\n  pages={631--665},\n  year={2006}\n}\n\n@article{lewbel2007estimation,\n  title={Estimation of Average Treatment Effects with Misclassification},\n  author={Lewbel, Arthur},\n  journal={Econometrica},\n  volume={75},\n  number={2},\n  pages={537--551},\n  year={2007}\n}\n\n% === Classical Measurement Error ===\n\n@article{blackwell2017unified,\n  title={A Unified Approach to Measurement Error and Missing Data: Overview and Applications},\n  author={Blackwell, Matthew and Honaker, James and King, Gary},\n  journal={Sociological Methods \\& Research},\n  volume={46},\n  number={3},\n  pages={303--341},\n  year={2017},\n  doi={10.1177/0049124115585360}\n}\n\n@book{fuller1987measurement,\n  title={Measurement Error Models},\n  author={Fuller, Wayne A.},\n  year={1987},\n  publisher={Wiley},\n  address={New York}\n}\n\n@book{carroll2006measurement,\n  title={Measurement Error in Nonlinear Models: A Modern Perspective},\n  author={Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu, Ciprian M.},\n  year={2006},\n  edition={2nd},\n  publisher={Chapman \\& Hall/CRC},\n  address={Boca Raton, FL}\n}\n\n@book{gustafson2003measurement,\n  title={Measurement Error and Misclassification in Statistics and Epidemiology: Impacts and Bayesian Adjustments},\n  author={Gustafson, Paul},\n  year={2003},\n  publisher={Chapman \\& Hall/CRC},\n  address={Boca Raton, FL},\n  doi={10.1201/9780203502761}\n}\n\n@article{hu2008nonparametric,\n  title={Instrumental Variable Treatment of Nonclassical Measurement Error Models},\n  author={Hu, Yingyao and Schennach, Susanne M.},\n  journal={Econometrica},\n  volume={76},\n  number={1},\n  pages={195--216},\n  year={2008},\n  doi={10.1111/j.0012-9682.2008.00823.x}\n}\n\n% === Bayesian Annotation Models ===\n\n@article{dawid1979maximum,\n  title={Maximum Likelihood Estimation of Observer Error-Rates Using the {EM} Algorithm},\n  author={Dawid, A. Philip and Skene, Allan M.},\n  journal={Applied Statistics},\n  volume={28},\n  number={1},\n  pages={20--28},\n  year={1979},\n  doi={10.2307/2346806}\n}\n\n@article{passonneau2014benefits,\n  title={The Benefits of a Model of Annotation},\n  author={Passonneau, Rebecca J. and Carpenter, Bob},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={2},\n  pages={311--326},\n  year={2014},\n  doi={10.1162/tacl_a_00185}\n}\n\n@inproceedings{hovy2013learning,\n  title={Learning Whom to Trust with {MACE}},\n  author={Hovy, Dirk and Berg-Kirkpatrick, Taylor and Vaswani, Ashish and Hovy, Eduard},\n  booktitle={Proceedings of NAACL-HLT},\n  pages={1120--1130},\n  year={2013}\n}\n\n@article{paun2018comparing,\n  title={Comparing {B}ayesian Models of Annotation},\n  author={Paun, Silviu and Carpenter, Bob and Chamberlain, Jon and Hovy, Dirk and Kruschwitz, Udo and Poesio, Massimo},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={6},\n  pages={571--585},\n  year={2018},\n  doi={10.1162/tacl_a_00040}\n}\n\n% === Causal Inference & HTE ===\n\n@article{athey2016recursive,\n  title={Recursive Partitioning for Heterogeneous Causal Effects},\n  author={Athey, Susan and Imbens, Guido},\n  journal={Proceedings of the National Academy of Sciences},\n  volume={113},\n  number={27},\n  pages={7353--7360},\n  year={2016},\n  doi={10.1073/pnas.1510489113}\n}\n\n@article{wager2018causal,\n  title={Estimation and Inference of Heterogeneous Treatment Effects using Random Forests},\n  author={Wager, Stefan and Athey, Susan},\n  journal={Journal of the American Statistical Association},\n  volume={113},\n  number={523},\n  pages={1228--1242},\n  year={2018},\n  doi={10.1080/01621459.2017.1319839}\n}\n\n@article{chernozhukov2018dml,\n  title={Double/Debiased Machine Learning for Treatment and Structural Parameters},\n  author={Chernozhukov, Victor and Chetverikov, Denis and Demirer, Mert and Duflo, Esther and Hansen, Christian and Newey, Whitney and Robins, James},\n  journal={The Econometrics Journal},\n  volume={21},\n  number={1},\n  pages={C1--C68},\n  year={2018},\n  doi={10.1111/ectj.12097}\n}\n\n@article{kennedy2023dr,\n  title={Towards Optimal Doubly Robust Estimation of Heterogeneous Causal Effects},\n  author={Kennedy, Edward H.},\n  journal={Electronic Journal of Statistics},\n  volume={17},\n  number={2},\n  pages={3008--3049},\n  year={2023},\n  doi={10.1214/23-EJS2157}\n}\n\n@article{kunzel2019metalearners,\n  title={Metalearners for Estimating Heterogeneous Treatment Effects Using Machine Learning},\n  author={K{\\\"u}nzel, S{\\\"o}ren R. and Sekhon, Jasjeet S. and Bickel, Peter J. and Yu, Bin},\n  journal={Proceedings of the National Academy of Sciences},\n  volume={116},\n  number={10},\n  pages={4156--4165},\n  year={2019},\n  doi={10.1073/pnas.1804597116}\n}\n\n@article{imai2010causal,\n  title={Causal Inference with Differential Measurement Error: Nonparametric Identification and Sensitivity Analysis},\n  author={Imai, Kosuke and Yamamoto, Teppei},\n  journal={American Journal of Political Science},\n  volume={54},\n  number={4},\n  pages={926--943},\n  year={2010},\n  doi={10.1111/j.1540-5907.2010.00446.x}\n}\n\n% === LLMs as Annotators ===\n\n@article{gilardi2023chatgpt,\n  title={{ChatGPT} Outperforms Crowd-Workers for Text-Annotation Tasks},\n  author={Gilardi, Fabrizio and Alizadeh, Meysam and Kubli, Ma{\\\"e}l},\n  journal={Proceedings of the National Academy of Sciences},\n  volume={120},\n  number={30},\n  pages={e2305016120},\n  year={2023},\n  doi={10.1073/pnas.2305016120}\n}\n\n@article{tornberg2024chatgpt,\n  title={Large Language Models Outperform Expert Coders and Supervised Classifiers at Annotating Political Social Media Messages},\n  author={T{\\\"o}rnberg, Petter},\n  journal={Social Science Computer Review},\n  year={2024},\n  doi={10.1177/08944393241286471},\n  publisher={SAGE Publications}\n}\n\n@article{ziems2024nlp,\n  title={Can Large Language Models Transform Computational Social Science?},\n  author={Ziems, Caleb and Held, William and Shaikh, Omar and Chen, Jiaao and Zhang, Zhehao and Yang, Diyi},\n  journal={Computational Linguistics},\n  volume={50},\n  number={1},\n  pages={237--291},\n  year={2024},\n  doi={10.1162/coli_a_00502}\n}\n\n@article{pangakis2023automated,\n  title={Automated Annotation with Generative {AI} Requires Validation},\n  author={Pangakis, Nicholas and Wolken, Samuel and Fasching, Neil},\n  journal={arXiv preprint arXiv:2306.00176},\n  year={2023}\n}\n\n@article{ashwin2025bias,\n  title={Using Large Language Models for Qualitative Analysis can Introduce Serious Bias},\n  author={Ashwin, Aditya and Swanson, Becca and Blair, Robert and Samii, Cyrus},\n  journal={Sociological Methods \\& Research},\n  year={2025},\n  doi={10.1177/00491241251313793}\n}\n\n% === PPI / DSL / Correction Methods ===\n\n@article{angelopoulos2023ppi,\n  title={Prediction-Powered Inference},\n  author={Angelopoulos, Anastasios N. and Bates, Stephen and Cand{\\`e}s, Emmanuel J. and Jordan, Michael I. and Lei, Lihua},\n  journal={Science},\n  volume={382},\n  number={6671},\n  pages={669--674},\n  year={2023},\n  doi={10.1126/science.adi6000}\n}\n\n@article{messing2026hidden,\n  title={Hidden Measurement Error in {LLM} Pipelines Distorts Annotation, Evaluation, and Benchmarking},\n  author={Messing, Solomon},\n  journal={arXiv preprint arXiv:2604.11581},\n  year={2026}\n}\n\n@article{zrnic2024cross,\n  title={Cross-Prediction-Powered Inference},\n  author={Zrnic, Tijana and Cand{\\`e}s, Emmanuel J.},\n  journal={Proceedings of the National Academy of Sciences},\n  volume={121},\n  number={15},\n  pages={e2322083121},\n  year={2024},\n  doi={10.1073/pnas.2322083121}\n}\n\n@inproceedings{zrnic2024active,\n  title={Active Statistical Inference},\n  author={Zrnic, Tijana and Cand{\\`e}s, Emmanuel J.},\n  booktitle={Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  series={PMLR},\n  volume={235},\n  year={2024}\n}\n\n@inproceedings{egami2024dsl,\n  title={Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models},\n  author={Egami, Naoki and Hinck, Musashi and Stewart, Brandon and Wei, Hanying},\n  booktitle={Advances in Neural Information Processing Systems},\n  volume={37},\n  year={2024}\n}\n\n@article{mozer2026ppi,\n  title={{PPI} is the Difference Estimator: Recognizing the Survey Sampling Roots of Prediction-Powered Inference},\n  author={Mozer, Reagan},\n  journal={arXiv preprint arXiv:2603.19160},\n  year={2026}\n}\n\n@article{sui2026ppci,\n  title={Prediction-Powered Conditional Inference},\n  author={Sui, Yijun and Cand{\\`e}s, Emmanuel J.},\n  journal={arXiv preprint arXiv:2603.05575},\n  year={2026}\n}\n\n@article{bu2023forestiv,\n  title={Achieving Reliable Causal Inference with Data-Mined Variables: A Random Forest Approach to the Measurement Error Problem},\n  author={Bu, Zhexin and Almond, David and Bhatt, Siddhartha and Goldsmith-Pinkham, Paul},\n  journal={INFORMS Journal on Data Science},\n  volume={2},\n  number={2},\n  pages={110--129},\n  year={2023},\n  doi={10.1287/ijds.2023.0026}\n}\n\n@article{fong2021machine,\n  title={Machine Learning Predictions as Regression Covariates},\n  author={Fong, Christian and Tyler, Matthew},\n  journal={Political Analysis},\n  volume={29},\n  number={1},\n  pages={48--64},\n  year={2021},\n  doi={10.1017/pan.2020.11}\n}\n\n% === CSS Methodology ===\n\n@book{grimmer2022text,\n  title={Text as Data: A New Framework for Machine Learning and the Social Sciences},\n  author={Grimmer, Justin and Roberts, Margaret E. and Stewart, Brandon M.},\n  year={2022},\n  publisher={Princeton University Press},\n  address={Princeton, NJ}\n}\n\n@article{audinet2025benchmarking,\n  title={Benchmarking Debiasing Methods for {LLM}-based Parameter Estimates},\n  author={Audinet de Pieuchon, Josias and Egami, Naoki and Alizadeh, Meysam and Gilardi, Fabrizio},\n  journal={Proceedings of EMNLP},\n  year={2025}\n}\n\n% === Semi-synthetic Data Source ===\n\n@inproceedings{barbieri2020tweeteval,\n  title={{TweetEval}: Unified Benchmark and Comparative Evaluation for Tweet Classification},\n  author={Barbieri, Francesco and Camacho-Collados, Jose and Espinosa-Anke, Luis and Neves, Leonardo},\n  booktitle={Findings of EMNLP},\n  pages={1644--1650},\n  year={2020},\n  doi={10.18653/v1/2020.findings-emnlp.148}\n}\n\n@article{wang2020methods,\n  title={Methods for Correcting Inference Based on Outcomes Predicted by Machine Learning},\n  author={Wang, Siruo and McCormick, Tyler H. and Leek, Jeffrey T.},\n  journal={Proceedings of the National Academy of Sciences},\n  volume={117},\n  number={48},\n  pages={30266--30275},\n  year={2020}\n}\n\n@article{feder2022causal,\n  title={Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond},\n  author={Feder, Amir and Keith, Katherine A. and Manzoor, Emaad and Pryzant, Reid and Sridhar, Dhanya and Wood-Doughty, Zach and Eisenstein, Jacob and Grimmer, Justin and Reichart, Roi and Roberts, Margaret E. and Stewart, Brandon M. and Veitch, Victor and Yang, Diyi},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={10},\n  pages={1171--1197},\n  year={2022}\n}\n\n@inproceedings{keith2020text,\n  title={Text and Causal Inference: A Review of Using Text to Remove Confounding from Causal Estimates},\n  author={Keith, Katherine A. and Jensen, David and O'Connor, Brendan},\n  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},\n  pages={5332--5344},\n  year={2020}\n}\n\n% === HTE Estimation ===\n\n@article{semenova2021debiased,\n  title={Debiased Machine Learning of Conditional Average Treatment Effects and Other Causal Functions},\n  author={Semenova, Vira and Chernozhukov, Victor},\n  journal={The Econometrics Journal},\n  volume={24},\n  number={2},\n  pages={264--289},\n  year={2021},\n  doi={10.1093/ectj/utaa027}\n}\n\n@article{nie2021quasi,\n  title={Quasi-Oracle Estimation of Heterogeneous Treatment Effects},\n  author={Nie, Xinkun and Wager, Stefan},\n  journal={Biometrika},\n  volume={108},\n  number={2},\n  pages={299--319},\n  year={2021},\n  doi={10.1093/biomet/asaa076}\n}\n\n% === Sensitivity Analysis for Misclassification ===\n\n@book{lash2009applying,\n  title={Applying Quantitative Bias Analysis to Epidemiologic Data},\n  author={Lash, Timothy L. and Fox, Matthew P. and Fink, Aliza K.},\n  publisher={Springer},\n  address={New York},\n  year={2009},\n  doi={10.1007/978-0-387-87959-8}\n}\n\n@article{dorn2022sharp,\n  title={Sharp Sensitivity Analysis for Inverse Propensity Weighting via Quantile Balancing},\n  author={Dorn, Jacob and Guo, Kevin and Kallus, Nathan},\n  journal={Journal of the American Statistical Association},\n  volume={118},\n  number={544},\n  pages={2645--2657},\n  year={2023},\n  doi={10.1080/01621459.2022.2064774}\n}\n\n% === Treatment Effects + Measurement Error ===\n\n@article{ogburn2012nondifferential,\n  title={On the Nondifferential Misclassification of a Binary Confounder},\n  author={Ogburn, Elizabeth L. and VanderWeele, Tyler J.},\n  journal={Epidemiology},\n  volume={23},\n  number={3},\n  pages={433--439},\n  year={2012},\n  doi={10.1097/EDE.0b013e31824d1f63}\n}\n\n@article{battistin2014treatment,\n  title={Treatment Effect Estimation with Covariate Measurement Error},\n  author={Battistin, Erich and Chesher, Andrew},\n  journal={Journal of Econometrics},\n  volume={178},\n  number={2},\n  pages={707--714},\n  year={2014},\n  doi={10.1016/j.jeconom.2013.10.006}\n}\n\n% === Real-Data Datasets ===\n\n@article{kennedy2020constructing,\n  title={Constructing Interval Variables via Faceted {Rasch} Measurement and Multitask Deep Learning: A Hate Speech Application},\n  author={Kennedy, Chris J. and Bacon, Geoff and Sahn, Alexander and von Vacano, Claudia},\n  journal={arXiv preprint arXiv:2009.10277},\n  year={2020}\n}\n\n@inproceedings{guo2017calibration,\n  title={On Calibration of Modern Neural Networks},\n  author={Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle={Proceedings of the 34th International Conference on Machine Learning},\n  pages={1321--1330},\n  year={2017}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 502,
        "oldLines": 3,
        "newStart": 502,
        "newLines": 24,
        "lines": [
          "   pages={1321--1330},",
          "   year={2017}",
          " }",
          "+",
          "+@article{camuffo2025variance,",
          "+  title={Variance-Aware {LLM} Annotation for Strategy Research},",
          "+  author={Camuffo, Matteo and Gambardella, Alfonso and Kazemi, Maryam and Malachowski, Daniel and Pandey, Alok},",
          "+  journal={arXiv preprint arXiv:2601.02370},",
          "+  year={2025}",
          "+}",
          "+",
          "+@article{cheng2024err,",
          "+  title={To Err Is Human; To Annotate, {SILICON}?},",
          "+  author={Cheng, Myeongjun and Mayya, Rachit and Sedoc, Jo\\~{a}o},",
          "+  journal={arXiv preprint arXiv:2412.14461},",
          "+  year={2024}",
          "+}",
          "+",
          "+@article{ura2015heterogeneous,",
          "+  title={Heterogeneous Treatment Effects with Mismeasured Endogenous Treatment},",
          "+  author={Ura, Takuya},",
          "+  journal={arXiv preprint arXiv:1511.04162},",
          "+  year={2015}",
          "+}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Edit · `toolu_01ESEpJTJ1v9KxHaUxg3w8Kd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex",
  "old_string": "Concretely, \\citet{frazis2003estimating} derive scalar attenuation $\\tilde{\\beta} = \\beta(1 - \\pi_0 - \\pi_1)$ for the uncorrected estimator under homogeneous misclassification; Theorem~\\ref{thm:bias_identity} characterizes a structurally distinct quantity---correction-induced bias $\\delta_s \\cdot \\Delta\\tau / (1 - 2\\bar{\\pi})$---that is subgroup-specific, potentially sign-reversing, and absent from the uncorrected estimator.\nThe homogeneous-error setting is a degenerate case: with $K{=}1$, $\\delta_s{=}0$ and correction-induced bias vanishes, recovering the classical attenuation result.\nThe algebraic mechanisms also differ: OLS attenuation under misclassified regressors~\\cite{frazis2003estimating,blackwell2017unified} versus confusion matrix inversion that redistributes error across subgroups with heterogeneous rates.\nWe empirically verify this distinction: F-L correction---even when applied per subgroup---produces higher bias than the naive estimator under heterogeneous misclassification, whereas EC-HTE achieves near-oracle performance (Appendix~\\ref{app:fl_comparison}).",
  "new_string": "Concretely, \\citet{frazis2003estimating} derive scalar attenuation for the uncorrected estimator under homogeneous misclassification; Theorem~\\ref{thm:bias_identity} characterizes a structurally distinct quantity---correction-induced bias that is subgroup-specific, potentially sign-reversing, and absent from the uncorrected estimator.\nThe homogeneous-error setting ($K{=}1$, $\\delta_s{=}0$) is a degenerate case recovering classical attenuation~\\cite{blackwell2017unified}; empirically, F-L correction produces higher bias under heterogeneous misclassification, while EC-HTE achieves near-oracle performance (Appendix~\\ref{app:fl_comparison})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "6819f666-65b0-4c92-b98a-2819301a930a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfTCbq1mJavYLkU3D8YAFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14448,
      "cache_read_input_tokens": 53368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14448
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-23T09:29:25.832Z_

<details><summary>↩ Tool result · `toolu_01ESEpJTJ1v9KxHaUxg3w8Kd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "a708a30e-ae9f-4741-84a4-59240879611b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex",
    "oldString": "Concretely, \\citet{frazis2003estimating} derive scalar attenuation $\\tilde{\\beta} = \\beta(1 - \\pi_0 - \\pi_1)$ for the uncorrected estimator under homogeneous misclassification; Theorem~\\ref{thm:bias_identity} characterizes a structurally distinct quantity---correction-induced bias $\\delta_s \\cdot \\Delta\\tau / (1 - 2\\bar{\\pi})$---that is subgroup-specific, potentially sign-reversing, and absent from the uncorrected estimator.\nThe homogeneous-error setting is a degenerate case: with $K{=}1$, $\\delta_s{=}0$ and correction-induced bias vanishes, recovering the classical attenuation result.\nThe algebraic mechanisms also differ: OLS attenuation under misclassified regressors~\\cite{frazis2003estimating,blackwell2017unified} versus confusion matrix inversion that redistributes error across subgroups with heterogeneous rates.\nWe empirically verify this distinction: F-L correction---even when applied per subgroup---produces higher bias than the naive estimator under heterogeneous misclassification, whereas EC-HTE achieves near-oracle performance (Appendix~\\ref{app:fl_comparison}).",
    "newString": "Concretely, \\citet{frazis2003estimating} derive scalar attenuation for the uncorrected estimator under homogeneous misclassification; Theorem~\\ref{thm:bias_identity} characterizes a structurally distinct quantity---correction-induced bias that is subgroup-specific, potentially sign-reversing, and absent from the uncorrected estimator.\nThe homogeneous-error setting ($K{=}1$, $\\delta_s{=}0$) is a degenerate case recovering classical attenuation~\\cite{blackwell2017unified}; empirically, F-L correction produces higher bias under heterogeneous misclassification, while EC-HTE achieves near-oracle performance (Appendix~\\ref{app:fl_comparison}).",
    "originalFile": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Measurement error and annotation models.}\nClassical measurement error theory shows that correction via estimated error models can amplify MSE when the error structure is misspecified~\\cite{fuller1987measurement,carroll2006measurement}; Bayesian approaches require informative priors when identification is weak~\\cite{gustafson2003measurement}, and nonparametric methods use repeated measurements or instruments to recover the true distribution~\\cite{hu2008nonparametric}.\n\nThree distinctions separate our contribution from prior measurement error analyses.\nFirst, we study effect modifier misclassification---the mismeasured variable defines the CATE function itself---rather than regressor~\\cite{frazis2003estimating,carroll2006measurement} or confounder~\\cite{ogburn2012nondifferential,greenland1980effect} error, where attenuation is the primary concern.\nSecond, Theorem~\\ref{thm:bias_identity} derives a bias identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.\nConcretely, \\citet{frazis2003estimating} derive scalar attenuation $\\tilde{\\beta} = \\beta(1 - \\pi_0 - \\pi_1)$ for the uncorrected estimator under homogeneous misclassification; Theorem~\\ref{thm:bias_identity} characterizes a structurally distinct quantity---correction-induced bias $\\delta_s \\cdot \\Delta\\tau / (1 - 2\\bar{\\pi})$---that is subgroup-specific, potentially sign-reversing, and absent from the uncorrected estimator.\nThe homogeneous-error setting is a degenerate case: with $K{=}1$, $\\delta_s{=}0$ and correction-induced bias vanishes, recovering the classical attenuation result.\nThe algebraic mechanisms also differ: OLS attenuation under misclassified regressors~\\cite{frazis2003estimating,blackwell2017unified} versus confusion matrix inversion that redistributes error across subgroups with heterogeneous rates.\nWe empirically verify this distinction: F-L correction---even when applied per subgroup---produces higher bias than the naive estimator under heterogeneous misclassification, whereas EC-HTE achieves near-oracle performance (Appendix~\\ref{app:fl_comparison}).\nThird, the $\\delta_s \\cdot \\Delta\\tau$ product structure arises only under heterogeneous error rates; all homogeneous-error analyses~\\cite{battistin2014treatment,fong2021machine} miss this interaction entirely.\nIn the annotation literature, \\citet{dawid1979maximum} introduced confusion matrix estimation for multiple annotators, with extensions to item difficulty, annotator competence, and hierarchical priors~\\cite{passonneau2014benefits,hovy2013learning,paun2018comparing}.\nOur hierarchical estimator (Section~\\ref{sec:method}) adapts this architecture from label aggregation to causal inference, tying the prior structure to the subgroup dimension that defines treatment effect heterogeneity.\n\n\\paragraph{HTE estimation and LLM annotation error.}\nCausal forests~\\cite{athey2016recursive,wager2018causal}, double/debiased ML~\\cite{chernozhukov2018dml,semenova2021debiased}, doubly-robust CATE estimators~\\cite{kennedy2023dr}, and meta-learners~\\cite{kunzel2019metalearners} all assume that covariates defining heterogeneity are observed without error; when the effect modifier is misclassified, CATE estimates conflate effects across groups.\nEC-HTE provides upstream correction that restores valid inputs to any downstream estimator.\nThe corrected pseudo-outcomes are in principle compatible with other HTE estimators such as the R-learner~\\citep{nie2021quasi}.\nFor broader perspectives on causal inference with text data, see \\citet{feder2022causal} and \\citet{keith2020text}; \\citet{wang2020methods} study inference correction when outcomes are ML-predicted, a related but distinct problem from effect modifier misclassification.\nLLMs now match crowd-worker accuracy on many classification tasks~\\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,pangakis2023automated}, but \\citet{ashwin2025bias} show that error rates vary by up to $5\\times$ across demographic subgroups.\nThis subgroup-varying error is the failure mode we address: it distorts the very contrasts that define the research question, and prior work documents the pattern without providing a correction mechanism for downstream causal estimands.\nConcurrent work identifies variance-side measurement error from LLM pipeline design choices~\\cite{messing2026hidden}; our framework addresses the complementary bias-side problem from heterogeneous misclassification rates across subgroups.\nTemperature or Platt scaling~\\cite{guo2017calibration} reduces per-subgroup $\\pi_s$ but does not eliminate heterogeneity $\\Delta\\pi$; EC-HTE corrects the residual $\\delta_s$-driven bias that persists post-calibration (Appendix~\\ref{app:calibration} empirically confirms this complementarity).\n\n\\paragraph{Prediction-powered and design-based correction.}\nPPI~\\cite{angelopoulos2023ppi,zrnic2024cross} and DSL~\\cite{egami2024dsl} correct population-level aggregates assuming homogeneous prediction error.\nIn our setting---binary effect modifier with known subgroup structure, a special case of the broader problems DSL addresses---DSL's measurement error correction reduces, under the confusion-matrix parameterization we adopt, to confusion matrix inversion: pooled DSL is equivalent to our Global baseline, and per-subgroup DSL to Stratified MLE (Section~\\ref{sec:ec_hte_eval}; Appendix~\\ref{app:ppi_comparison}).\nEC-HTE adds hierarchical partial pooling across subgroups, borrowing strength to reduce variance---a mechanism outside the DSL framework.\n\\citet{audinet2025benchmarking} benchmark DSL and PPI debiasing for LLM-based parameter estimation, documenting bias-variance tradeoffs analogous to our findings; their analysis targets population-level parameters rather than subgroup-conditional estimands, leaving the $\\delta_s \\cdot \\Delta\\tau$ interaction we formalize unaddressed.\n\\citet{mozer2026ppi} extend PPI to arm-specific ATE correction; PPCI~\\cite{sui2026ppci} targets conditional estimands but corrects outcome-side error ($\\hat{Y}$ given true $Z$), not covariate-side misclassification; ForestIV~\\cite{bu2023forestiv} targets the outcome model rather than the heterogeneity structure.\nNone corrects bias when the mismeasured variable is the effect modifier indexing the CATE function.\n\\citet{imai2010causal} study treatment misclassification, requiring instrumental variables or partial identification; our problem is structurally distinct because the treatment is observed correctly but the effect modifier is misclassified, admitting exact correction through confusion matrices rather than bounds.\nExtended discussion of these distinctions appears in Appendix~\\ref{app:related}.\nOur validation combines synthetic DGPs, semi-synthetic experiments, and real LLM confusion matrices, consistent with PPI and DSL evaluation methodology; Appendix~\\ref{app:multilm} validates both $\\Delta\\pi$ heterogeneity and the bias identity itself ($R^2 = 0.975$) across 11 model--dataset combinations.\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 10,
        "newStart": 7,
        "newLines": 8,
        "lines": [
          " Three distinctions separate our contribution from prior measurement error analyses.",
          " First, we study effect modifier misclassification---the mismeasured variable defines the CATE function itself---rather than regressor~\\cite{frazis2003estimating,carroll2006measurement} or confounder~\\cite{ogburn2012nondifferential,greenland1980effect} error, where attenuation is the primary concern.",
          " Second, Theorem~\\ref{thm:bias_identity} derives a bias identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.",
          "-Concretely, \\citet{frazis2003estimating} derive scalar attenuation $\\tilde{\\beta} = \\beta(1 - \\pi_0 - \\pi_1)$ for the uncorrected estimator under homogeneous misclassification; Theorem~\\ref{thm:bias_identity} characterizes a structurally distinct quantity---correction-induced bias $\\delta_s \\cdot \\Delta\\tau / (1 - 2\\bar{\\pi})$---that is subgroup-specific, potentially sign-reversing, and absent from the uncorrected estimator.",
          "-The homogeneous-error setting is a degenerate case: with $K{=}1$, $\\delta_s{=}0$ and correction-induced bias vanishes, recovering the classical attenuation result.",
          "-The algebraic mechanisms also differ: OLS attenuation under misclassified regressors~\\cite{frazis2003estimating,blackwell2017unified} versus confusion matrix inversion that redistributes error across subgroups with heterogeneous rates.",
          "-We empirically verify this distinction: F-L correction---even when applied per subgroup---produces higher bias than the naive estimator under heterogeneous misclassification, whereas EC-HTE achieves near-oracle performance (Appendix~\\ref{app:fl_comparison}).",
          "+Concretely, \\citet{frazis2003estimating} derive scalar attenuation for the uncorrected estimator under homogeneous misclassification; Theorem~\\ref{thm:bias_identity} characterizes a structurally distinct quantity---correction-induced bias that is subgroup-specific, potentially sign-reversing, and absent from the uncorrected estimator.",
          "+The homogeneous-error setting ($K{=}1$, $\\delta_s{=}0$) is a degenerate case recovering classical attenuation~\\cite{blackwell2017unified}; empirically, F-L correction produces higher bias under heterogeneous misclassification, while EC-HTE achieves near-oracle performance (Appendix~\\ref{app:fl_comparison}).",
          " Third, the $\\delta_s \\cdot \\Delta\\tau$ product structure arises only under heterogeneous error rates; all homogeneous-error analyses~\\cite{battistin2014treatment,fong2021machine} miss this interaction entirely.",
          " In the annotation literature, \\citet{dawid1979maximum} introduced confusion matrix estimation for multiple annotators, with extensions to item difficulty, annotator competence, and hierarchical priors~\\cite{passonneau2014benefits,hovy2013learning,paun2018comparing}.",
          " Our hierarchical estimator (Section~\\ref{sec:method}) adapts this architecture from label aggregation to causal inference, tying the prior structure to the subgroup dimension that defines treatment effect heterogeneity."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Edit · `toolu_01XcXatLywwzC9Jq7jkSxu2x`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex",
  "old_string": "LLMs now match crowd-worker accuracy on many classification tasks~\\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,pangakis2023automated}, but \\citet{ashwin2025bias} show that error rates vary by up to $5\\times$ across demographic subgroups.\nThis subgroup-varying error is the failure mode we address: it distorts the very contrasts that define the research question, and prior work documents the pattern without providing a correction mechanism for downstream causal estimands.\nConcurrent work identifies variance-side measurement error from LLM pipeline design choices~\\cite{messing2026hidden}; our framework addresses the complementary bias-side problem from heterogeneous misclassification rates across subgroups.",
  "new_string": "LLMs now match crowd-worker accuracy on many classification tasks~\\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,pangakis2023automated}, but \\citet{ashwin2025bias} show that error rates vary by up to $5\\times$ across demographic subgroups; \\citet{cheng2024err} demonstrate that prompt optimization can reduce such error, a complementary preprocessing step.\nThis subgroup-varying error distorts the very contrasts that define the research question; prior work documents the pattern without correcting downstream causal estimands.\nConcurrent work identifies variance-side LLM measurement error~\\cite{messing2026hidden}; \\citet{camuffo2025variance} characterize five variance sources in LLM annotation, complementary to our bias-side analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "d103ee16-e0b7-406e-9923-9fba5d37118c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfTCbq1mJavYLkU3D8YAFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14448,
      "cache_read_input_tokens": 53368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14448
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-23T09:29:35.239Z_

<details><summary>↩ Tool result · `toolu_01XcXatLywwzC9Jq7jkSxu2x`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "b0c4616f-960c-4a83-9bec-64f3805471b3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex",
    "oldString": "LLMs now match crowd-worker accuracy on many classification tasks~\\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,pangakis2023automated}, but \\citet{ashwin2025bias} show that error rates vary by up to $5\\times$ across demographic subgroups.\nThis subgroup-varying error is the failure mode we address: it distorts the very contrasts that define the research question, and prior work documents the pattern without providing a correction mechanism for downstream causal estimands.\nConcurrent work identifies variance-side measurement error from LLM pipeline design choices~\\cite{messing2026hidden}; our framework addresses the complementary bias-side problem from heterogeneous misclassification rates across subgroups.",
    "newString": "LLMs now match crowd-worker accuracy on many classification tasks~\\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,pangakis2023automated}, but \\citet{ashwin2025bias} show that error rates vary by up to $5\\times$ across demographic subgroups; \\citet{cheng2024err} demonstrate that prompt optimization can reduce such error, a complementary preprocessing step.\nThis subgroup-varying error distorts the very contrasts that define the research question; prior work documents the pattern without correcting downstream causal estimands.\nConcurrent work identifies variance-side LLM measurement error~\\cite{messing2026hidden}; \\citet{camuffo2025variance} characterize five variance sources in LLM annotation, complementary to our bias-side analysis.",
    "originalFile": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Measurement error and annotation models.}\nClassical measurement error theory shows that correction via estimated error models can amplify MSE when the error structure is misspecified~\\cite{fuller1987measurement,carroll2006measurement}; Bayesian approaches require informative priors when identification is weak~\\cite{gustafson2003measurement}, and nonparametric methods use repeated measurements or instruments to recover the true distribution~\\cite{hu2008nonparametric}.\n\nThree distinctions separate our contribution from prior measurement error analyses.\nFirst, we study effect modifier misclassification---the mismeasured variable defines the CATE function itself---rather than regressor~\\cite{frazis2003estimating,carroll2006measurement} or confounder~\\cite{ogburn2012nondifferential,greenland1980effect} error, where attenuation is the primary concern.\nSecond, Theorem~\\ref{thm:bias_identity} derives a bias identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.\nConcretely, \\citet{frazis2003estimating} derive scalar attenuation for the uncorrected estimator under homogeneous misclassification; Theorem~\\ref{thm:bias_identity} characterizes a structurally distinct quantity---correction-induced bias that is subgroup-specific, potentially sign-reversing, and absent from the uncorrected estimator.\nThe homogeneous-error setting ($K{=}1$, $\\delta_s{=}0$) is a degenerate case recovering classical attenuation~\\cite{blackwell2017unified}; empirically, F-L correction produces higher bias under heterogeneous misclassification, while EC-HTE achieves near-oracle performance (Appendix~\\ref{app:fl_comparison}).\nThird, the $\\delta_s \\cdot \\Delta\\tau$ product structure arises only under heterogeneous error rates; all homogeneous-error analyses~\\cite{battistin2014treatment,fong2021machine} miss this interaction entirely.\nIn the annotation literature, \\citet{dawid1979maximum} introduced confusion matrix estimation for multiple annotators, with extensions to item difficulty, annotator competence, and hierarchical priors~\\cite{passonneau2014benefits,hovy2013learning,paun2018comparing}.\nOur hierarchical estimator (Section~\\ref{sec:method}) adapts this architecture from label aggregation to causal inference, tying the prior structure to the subgroup dimension that defines treatment effect heterogeneity.\n\n\\paragraph{HTE estimation and LLM annotation error.}\nCausal forests~\\cite{athey2016recursive,wager2018causal}, double/debiased ML~\\cite{chernozhukov2018dml,semenova2021debiased}, doubly-robust CATE estimators~\\cite{kennedy2023dr}, and meta-learners~\\cite{kunzel2019metalearners} all assume that covariates defining heterogeneity are observed without error; when the effect modifier is misclassified, CATE estimates conflate effects across groups.\nEC-HTE provides upstream correction that restores valid inputs to any downstream estimator.\nThe corrected pseudo-outcomes are in principle compatible with other HTE estimators such as the R-learner~\\citep{nie2021quasi}.\nFor broader perspectives on causal inference with text data, see \\citet{feder2022causal} and \\citet{keith2020text}; \\citet{wang2020methods} study inference correction when outcomes are ML-predicted, a related but distinct problem from effect modifier misclassification.\nLLMs now match crowd-worker accuracy on many classification tasks~\\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,pangakis2023automated}, but \\citet{ashwin2025bias} show that error rates vary by up to $5\\times$ across demographic subgroups.\nThis subgroup-varying error is the failure mode we address: it distorts the very contrasts that define the research question, and prior work documents the pattern without providing a correction mechanism for downstream causal estimands.\nConcurrent work identifies variance-side measurement error from LLM pipeline design choices~\\cite{messing2026hidden}; our framework addresses the complementary bias-side problem from heterogeneous misclassification rates across subgroups.\nTemperature or Platt scaling~\\cite{guo2017calibration} reduces per-subgroup $\\pi_s$ but does not eliminate heterogeneity $\\Delta\\pi$; EC-HTE corrects the residual $\\delta_s$-driven bias that persists post-calibration (Appendix~\\ref{app:calibration} empirically confirms this complementarity).\n\n\\paragraph{Prediction-powered and design-based correction.}\nPPI~\\cite{angelopoulos2023ppi,zrnic2024cross} and DSL~\\cite{egami2024dsl} correct population-level aggregates assuming homogeneous prediction error.\nIn our setting---binary effect modifier with known subgroup structure, a special case of the broader problems DSL addresses---DSL's measurement error correction reduces, under the confusion-matrix parameterization we adopt, to confusion matrix inversion: pooled DSL is equivalent to our Global baseline, and per-subgroup DSL to Stratified MLE (Section~\\ref{sec:ec_hte_eval}; Appendix~\\ref{app:ppi_comparison}).\nEC-HTE adds hierarchical partial pooling across subgroups, borrowing strength to reduce variance---a mechanism outside the DSL framework.\n\\citet{audinet2025benchmarking} benchmark DSL and PPI debiasing for LLM-based parameter estimation, documenting bias-variance tradeoffs analogous to our findings; their analysis targets population-level parameters rather than subgroup-conditional estimands, leaving the $\\delta_s \\cdot \\Delta\\tau$ interaction we formalize unaddressed.\n\\citet{mozer2026ppi} extend PPI to arm-specific ATE correction; PPCI~\\cite{sui2026ppci} targets conditional estimands but corrects outcome-side error ($\\hat{Y}$ given true $Z$), not covariate-side misclassification; ForestIV~\\cite{bu2023forestiv} targets the outcome model rather than the heterogeneity structure.\nNone corrects bias when the mismeasured variable is the effect modifier indexing the CATE function.\n\\citet{imai2010causal} study treatment misclassification, requiring instrumental variables or partial identification; our problem is structurally distinct because the treatment is observed correctly but the effect modifier is misclassified, admitting exact correction through confusion matrices rather than bounds.\nExtended discussion of these distinctions appears in Appendix~\\ref{app:related}.\nOur validation combines synthetic DGPs, semi-synthetic experiments, and real LLM confusion matrices, consistent with PPI and DSL evaluation methodology; Appendix~\\ref{app:multilm} validates both $\\Delta\\pi$ heterogeneity and the bias identity itself ($R^2 = 0.975$) across 11 model--dataset combinations.\n",
    "structuredPatch": [
      {
        "oldStart": 18,
        "oldLines": 9,
        "newStart": 18,
        "newLines": 9,
        "lines": [
          " EC-HTE provides upstream correction that restores valid inputs to any downstream estimator.",
          " The corrected pseudo-outcomes are in principle compatible with other HTE estimators such as the R-learner~\\citep{nie2021quasi}.",
          " For broader perspectives on causal inference with text data, see \\citet{feder2022causal} and \\citet{keith2020text}; \\citet{wang2020methods} study inference correction when outcomes are ML-predicted, a related but distinct problem from effect modifier misclassification.",
          "-LLMs now match crowd-worker accuracy on many classification tasks~\\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,pangakis2023automated}, but \\citet{ashwin2025bias} show that error rates vary by up to $5\\times$ across demographic subgroups.",
          "-This subgroup-varying error is the failure mode we address: it distorts the very contrasts that define the research question, and prior work documents the pattern without providing a correction mechanism for downstream causal estimands.",
          "-Concurrent work identifies variance-side measurement error from LLM pipeline design choices~\\cite{messing2026hidden}; our framework addresses the complementary bias-side problem from heterogeneous misclassification rates across subgroups.",
          "+LLMs now match crowd-worker accuracy on many classification tasks~\\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,pangakis2023automated}, but \\citet{ashwin2025bias} show that error rates vary by up to $5\\times$ across demographic subgroups; \\citet{cheng2024err} demonstrate that prompt optimization can reduce such error, a complementary preprocessing step.",
          "+This subgroup-varying error distorts the very contrasts that define the research question; prior work documents the pattern without correcting downstream causal estimands.",
          "+Concurrent work identifies variance-side LLM measurement error~\\cite{messing2026hidden}; \\citet{camuffo2025variance} characterize five variance sources in LLM annotation, complementary to our bias-side analysis.",
          " Temperature or Platt scaling~\\cite{guo2017calibration} reduces per-subgroup $\\pi_s$ but does not eliminate heterogeneity $\\Delta\\pi$; EC-HTE corrects the residual $\\delta_s$-driven bias that persists post-calibration (Appendix~\\ref{app:calibration} empirically confirms this complementarity).",
          " ",
          " \\paragraph{Prediction-powered and design-based correction.}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Edit · `toolu_01CcxH9TYFf28Uek9QfrQyvJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex",
  "old_string": "\\citet{imai2010causal} study treatment misclassification, requiring instrumental variables or partial identification; our problem is structurally distinct because the treatment is observed correctly but the effect modifier is misclassified, admitting exact correction through confusion matrices rather than bounds.",
  "new_string": "\\citet{imai2010causal} study treatment misclassification via instrumental variables or partial identification; \\citet{ura2015heterogeneous} extends this to HTE with mismeasured treatment via IV.\nOur problem is structurally distinct: the treatment is observed correctly but the effect modifier is misclassified, admitting correction through confusion matrices."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "c04e36eb-897a-4f56-94dc-9b9cd76a882c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfTCbq1mJavYLkU3D8YAFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14448,
      "cache_read_input_tokens": 53368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14448
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-23T09:29:39.465Z_

<details><summary>↩ Tool result · `toolu_01CcxH9TYFf28Uek9QfrQyvJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "1622b685-69dd-4934-932e-44f158a12d7b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex",
    "oldString": "\\citet{imai2010causal} study treatment misclassification, requiring instrumental variables or partial identification; our problem is structurally distinct because the treatment is observed correctly but the effect modifier is misclassified, admitting exact correction through confusion matrices rather than bounds.",
    "newString": "\\citet{imai2010causal} study treatment misclassification via instrumental variables or partial identification; \\citet{ura2015heterogeneous} extends this to HTE with mismeasured treatment via IV.\nOur problem is structurally distinct: the treatment is observed correctly but the effect modifier is misclassified, admitting correction through confusion matrices.",
    "originalFile": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Measurement error and annotation models.}\nClassical measurement error theory shows that correction via estimated error models can amplify MSE when the error structure is misspecified~\\cite{fuller1987measurement,carroll2006measurement}; Bayesian approaches require informative priors when identification is weak~\\cite{gustafson2003measurement}, and nonparametric methods use repeated measurements or instruments to recover the true distribution~\\cite{hu2008nonparametric}.\n\nThree distinctions separate our contribution from prior measurement error analyses.\nFirst, we study effect modifier misclassification---the mismeasured variable defines the CATE function itself---rather than regressor~\\cite{frazis2003estimating,carroll2006measurement} or confounder~\\cite{ogburn2012nondifferential,greenland1980effect} error, where attenuation is the primary concern.\nSecond, Theorem~\\ref{thm:bias_identity} derives a bias identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.\nConcretely, \\citet{frazis2003estimating} derive scalar attenuation for the uncorrected estimator under homogeneous misclassification; Theorem~\\ref{thm:bias_identity} characterizes a structurally distinct quantity---correction-induced bias that is subgroup-specific, potentially sign-reversing, and absent from the uncorrected estimator.\nThe homogeneous-error setting ($K{=}1$, $\\delta_s{=}0$) is a degenerate case recovering classical attenuation~\\cite{blackwell2017unified}; empirically, F-L correction produces higher bias under heterogeneous misclassification, while EC-HTE achieves near-oracle performance (Appendix~\\ref{app:fl_comparison}).\nThird, the $\\delta_s \\cdot \\Delta\\tau$ product structure arises only under heterogeneous error rates; all homogeneous-error analyses~\\cite{battistin2014treatment,fong2021machine} miss this interaction entirely.\nIn the annotation literature, \\citet{dawid1979maximum} introduced confusion matrix estimation for multiple annotators, with extensions to item difficulty, annotator competence, and hierarchical priors~\\cite{passonneau2014benefits,hovy2013learning,paun2018comparing}.\nOur hierarchical estimator (Section~\\ref{sec:method}) adapts this architecture from label aggregation to causal inference, tying the prior structure to the subgroup dimension that defines treatment effect heterogeneity.\n\n\\paragraph{HTE estimation and LLM annotation error.}\nCausal forests~\\cite{athey2016recursive,wager2018causal}, double/debiased ML~\\cite{chernozhukov2018dml,semenova2021debiased}, doubly-robust CATE estimators~\\cite{kennedy2023dr}, and meta-learners~\\cite{kunzel2019metalearners} all assume that covariates defining heterogeneity are observed without error; when the effect modifier is misclassified, CATE estimates conflate effects across groups.\nEC-HTE provides upstream correction that restores valid inputs to any downstream estimator.\nThe corrected pseudo-outcomes are in principle compatible with other HTE estimators such as the R-learner~\\citep{nie2021quasi}.\nFor broader perspectives on causal inference with text data, see \\citet{feder2022causal} and \\citet{keith2020text}; \\citet{wang2020methods} study inference correction when outcomes are ML-predicted, a related but distinct problem from effect modifier misclassification.\nLLMs now match crowd-worker accuracy on many classification tasks~\\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,pangakis2023automated}, but \\citet{ashwin2025bias} show that error rates vary by up to $5\\times$ across demographic subgroups; \\citet{cheng2024err} demonstrate that prompt optimization can reduce such error, a complementary preprocessing step.\nThis subgroup-varying error distorts the very contrasts that define the research question; prior work documents the pattern without correcting downstream causal estimands.\nConcurrent work identifies variance-side LLM measurement error~\\cite{messing2026hidden}; \\citet{camuffo2025variance} characterize five variance sources in LLM annotation, complementary to our bias-side analysis.\nTemperature or Platt scaling~\\cite{guo2017calibration} reduces per-subgroup $\\pi_s$ but does not eliminate heterogeneity $\\Delta\\pi$; EC-HTE corrects the residual $\\delta_s$-driven bias that persists post-calibration (Appendix~\\ref{app:calibration} empirically confirms this complementarity).\n\n\\paragraph{Prediction-powered and design-based correction.}\nPPI~\\cite{angelopoulos2023ppi,zrnic2024cross} and DSL~\\cite{egami2024dsl} correct population-level aggregates assuming homogeneous prediction error.\nIn our setting---binary effect modifier with known subgroup structure, a special case of the broader problems DSL addresses---DSL's measurement error correction reduces, under the confusion-matrix parameterization we adopt, to confusion matrix inversion: pooled DSL is equivalent to our Global baseline, and per-subgroup DSL to Stratified MLE (Section~\\ref{sec:ec_hte_eval}; Appendix~\\ref{app:ppi_comparison}).\nEC-HTE adds hierarchical partial pooling across subgroups, borrowing strength to reduce variance---a mechanism outside the DSL framework.\n\\citet{audinet2025benchmarking} benchmark DSL and PPI debiasing for LLM-based parameter estimation, documenting bias-variance tradeoffs analogous to our findings; their analysis targets population-level parameters rather than subgroup-conditional estimands, leaving the $\\delta_s \\cdot \\Delta\\tau$ interaction we formalize unaddressed.\n\\citet{mozer2026ppi} extend PPI to arm-specific ATE correction; PPCI~\\cite{sui2026ppci} targets conditional estimands but corrects outcome-side error ($\\hat{Y}$ given true $Z$), not covariate-side misclassification; ForestIV~\\cite{bu2023forestiv} targets the outcome model rather than the heterogeneity structure.\nNone corrects bias when the mismeasured variable is the effect modifier indexing the CATE function.\n\\citet{imai2010causal} study treatment misclassification, requiring instrumental variables or partial identification; our problem is structurally distinct because the treatment is observed correctly but the effect modifier is misclassified, admitting exact correction through confusion matrices rather than bounds.\nExtended discussion of these distinctions appears in Appendix~\\ref{app:related}.\nOur validation combines synthetic DGPs, semi-synthetic experiments, and real LLM confusion matrices, consistent with PPI and DSL evaluation methodology; Appendix~\\ref{app:multilm} validates both $\\Delta\\pi$ heterogeneity and the bias identity itself ($R^2 = 0.975$) across 11 model--dataset combinations.\n",
    "structuredPatch": [
      {
        "oldStart": 30,
        "oldLines": 6,
        "newStart": 30,
        "newLines": 7,
        "lines": [
          " \\citet{audinet2025benchmarking} benchmark DSL and PPI debiasing for LLM-based parameter estimation, documenting bias-variance tradeoffs analogous to our findings; their analysis targets population-level parameters rather than subgroup-conditional estimands, leaving the $\\delta_s \\cdot \\Delta\\tau$ interaction we formalize unaddressed.",
          " \\citet{mozer2026ppi} extend PPI to arm-specific ATE correction; PPCI~\\cite{sui2026ppci} targets conditional estimands but corrects outcome-side error ($\\hat{Y}$ given true $Z$), not covariate-side misclassification; ForestIV~\\cite{bu2023forestiv} targets the outcome model rather than the heterogeneity structure.",
          " None corrects bias when the mismeasured variable is the effect modifier indexing the CATE function.",
          "-\\citet{imai2010causal} study treatment misclassification, requiring instrumental variables or partial identification; our problem is structurally distinct because the treatment is observed correctly but the effect modifier is misclassified, admitting exact correction through confusion matrices rather than bounds.",
          "+\\citet{imai2010causal} study treatment misclassification via instrumental variables or partial identification; \\citet{ura2015heterogeneous} extends this to HTE with mismeasured treatment via IV.",
          "+Our problem is structurally distinct: the treatment is observed correctly but the effect modifier is misclassified, admitting correction through confusion matrices.",
          " Extended discussion of these distinctions appears in Appendix~\\ref{app:related}.",
          " Our validation combines synthetic DGPs, semi-synthetic experiments, and real LLM confusion matrices, consistent with PPI and DSL evaluation methodology; Appendix~\\ref{app:multilm} validates both $\\Delta\\pi$ heterogeneity and the bias identity itself ($R^2 = 0.975$) across 11 model--dataset combinations."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Edit · `toolu_0183JEhNxAiwRj2UWyyWwNAd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
  "old_string": "The full derivation appears in Appendix~\\ref{app:derivation}.\n\n\\begin{remark}",
  "new_string": "The full derivation appears in Appendix~\\ref{app:derivation}.\nFor comparison with classical scalar attenuation~\\citep{frazis2003estimating}, see Section~\\ref{sec:related}.\n\n\\begin{remark}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "0b86bc7c-1680-4854-99a9-6beb80eb84ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfTCbq1mJavYLkU3D8YAFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14448,
      "cache_read_input_tokens": 53368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14448
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-23T09:29:41.880Z_

<details><summary>↩ Tool result · `toolu_0183JEhNxAiwRj2UWyyWwNAd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "f390be6e-43a3-49e1-beed-7ba9ac2b6653",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
    "oldString": "The full derivation appears in Appendix~\\ref{app:derivation}.\n\n\\begin{remark}",
    "newString": "The full derivation appears in Appendix~\\ref{app:derivation}.\nFor comparison with classical scalar attenuation~\\citep{frazis2003estimating}, see Section~\\ref{sec:related}.\n\n\\begin{remark}",
    "originalFile": "% Requires preamble: \\usepackage{amsthm,amsmath,amssymb}\n% and: \\newtheorem{theorem}{Theorem}\n%      \\newtheorem{corollary}[theorem]{Corollary}\n%      \\newtheorem{proposition}[theorem]{Proposition}\n\n\\section{Bias Decomposition: When Debiasing Hurts}\n\\label{sec:theory}\n\nWe formalize the bias that global misclassification correction introduces when subgroup error rates are heterogeneous.\nConsider estimating the conditional average treatment effect (CATE) $\\tau(z) = \\mathbb{E}[Y(1) - Y(0) \\mid Z = z]$, where $Z \\in \\{0, 1\\}$ is a binary effect modifier observed only through a noisy annotation $\\hat{Z}$.\nThe population consists of $K$ subgroups $S \\in \\{1, \\ldots, K\\}$ with weights $w_s = P(S{=}s)$, each characterized by a $2 \\times 2$ confusion matrix $C_s$ with symmetric error rate $\\pi_s = P(\\hat{Z} \\neq Z \\mid S{=}s)$.\nStandard practice estimates a single confusion matrix $\\bar{C} = \\sum_s w_s C_s$ from expert annotations and applies its inverse uniformly to all observations, with pooled error rate $\\bar{\\pi} = \\sum_s w_s \\pi_s$.\nWe show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.\n\nWe state five assumptions maintained throughout.\n%\n\\begin{itemize}\n\\item[\\textbf{(A1)}] \\textit{Conditional independence:} misclassification depends only on the true label $Z$ and subgroup $S$, not on potential outcomes $Y(0), Y(1)$.\n\\item[\\textbf{(A2)}] \\textit{Symmetric misclassification:} $P(\\hat{Z}{=}1 \\mid Z{=}0, S{=}s) = P(\\hat{Z}{=}0 \\mid Z{=}1, S{=}s) = \\pi_s$ for all $s$ (diagnostic only; see Remark~2).\n\\item[\\textbf{(A3)}] \\textit{Balanced effect modifier:} $P(Z{=}0) = P(Z{=}1) = 0.5$. This simplifies the exposition; we discuss relaxation below.\n\\item[\\textbf{(A4)}] \\textit{Non-degeneracy:} $\\pi_s \\neq 0.5$ for all $s$, ensuring each $C_s$ is invertible.\n\\item[\\textbf{(A5)}] \\textit{Homogeneous treatment effects across subgroups:} $\\tau(z, s) = \\tau(z)$ for all $s$, so $\\Delta\\tau = \\tau(1) - \\tau(0)$ is a scalar.\n\\end{itemize}\n\nUnder (A2)--(A3), the Bayesian mixing matrix $M_s$ (entries $M_s[\\hat{z}, z] = P(Z{=}z \\mid \\hat{Z}{=}\\hat{z}, S{=}s)$) coincides with $C_s$.\nThe global mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s$.\n\n\\begin{theorem}[Bias Decomposition Identity]\n\\label{thm:bias_identity}\nUnder \\textnormal{(A1)--(A5)}, the bias of global correction in subgroup $s$ at effect-modifier level $z$ is\n\\begin{align}\n\\mathrm{bias}_{\\mathrm{global}}(z{=}0, s) &= +\\frac{\\delta_s \\cdot \\Delta\\tau}{1 - 2\\bar{\\pi}}, \\label{eq:bias_z0} \\\\\n\\mathrm{bias}_{\\mathrm{global}}(z{=}1, s) &= -\\frac{\\delta_s \\cdot \\Delta\\tau}{1 - 2\\bar{\\pi}}, \\label{eq:bias_z1}\n\\end{align}\nwhere $\\delta_s = \\pi_s - \\bar{\\pi}$ is the subgroup deviation from the pooled error rate and $\\Delta\\tau = \\tau(1) - \\tau(0)$ is the CATE heterogeneity.\n\\end{theorem}\n\nEquations~\\eqref{eq:bias_z0}--\\eqref{eq:bias_z1} constitute an exact finite-population identity, not an asymptotic approximation or bound.\nThe bias factors into three interpretable components: $\\delta_s$ captures how much subgroup $s$ deviates from the average misclassification rate, $\\Delta\\tau$ captures treatment effect heterogeneity across levels of $Z$, and $1/(1 - 2\\bar{\\pi})$ is an amplification factor from matrix inversion.\nBias vanishes when either source of variation is absent ($\\delta_s = 0$ or $\\Delta\\tau = 0$), and arises only through their interaction.\nTheorem~\\ref{thm:bias_identity} implies that global correction trades one source of confounding for another: it removes attenuation from label noise but introduces a new bias from error-rate heterogeneity.\n\n\\paragraph{Proof sketch.}\nGlobal correction applies $M_{\\text{global}}^{-1}$ to the subgroup-specific observed CATE $\\tau_{\\text{obs}}(\\cdot, s) = M_s \\cdot \\tau_{\\text{true}}$, yielding bias $(M_{\\text{global}}^{-1} M_s - I) \\cdot \\tau_{\\text{true}}$.\nDirect computation shows $M_{\\text{global}}^{-1} M_s - I = \\frac{\\delta_s}{1-2\\bar{\\pi}} \\bigl[\\begin{smallmatrix} -1 & 1 \\\\ 1 & -1 \\end{smallmatrix}\\bigr]$.\nApplying this matrix to $[\\tau(0),\\, \\tau(1)]^\\top$ produces the product form.\nThe full derivation appears in Appendix~\\ref{app:derivation}.\n\n\\begin{remark}\nTheorem~\\ref{thm:bias_identity} does not require assumption~(A2).\nFor arbitrary asymmetric confusion matrices ($\\mathrm{FPR}_s \\neq \\mathrm{FNR}_s$),\nthe product form $\\mathrm{bias}(z, s) = \\Delta\\tau \\cdot [B_s]_{z,1}$ holds exactly,\nwhere $B_s = M_{\\mathrm{global}}^{-1} M_s - I$, because $B_s \\mathbf{1} = \\mathbf{0}$\nfollows from stochasticity of $M_s$ and $M_{\\mathrm{global}}$ alone.\nAssumption~(A2) simplifies $[B_s]_{z,1}$ to the scalar\n$\\pm \\delta_s / (1 - 2\\bar{\\pi})$ but is not necessary for the product structure.\nUnder asymmetric errors, the diagnostic (Proposition~\\ref{prop:debiasing_hurts}) requires evaluating $[B_s]_{z,1}$ cell-by-cell rather than via a single scalar threshold; the AUC decreases from 0.86 to 0.82 (Appendix~\\ref{app:asymmetric}), reflecting the additional complexity of cell-specific error rates.\nFor binary effect modifiers ($|\\mathcal{Z}|{=}2$), the asymmetric score $|[B_s]_{z,1}|$ reduces to a monotone transform of the symmetric score $|\\delta_s|/((1{-}2\\bar{\\pi})\\pi_s)$, because column-stochastic $M$ forces $|B_s[0,1]|{=}|B_s[1,1]|$; practitioners may use the simpler symmetric formula without loss.\nSee Appendix~\\ref{app:asymmetric} for the full derivation and empirical verification\n($R^2 = 0.991$).\n\\end{remark}\n\nAssumption~(A5) simplifies exposition; the identity generalizes to subgroup-specific $\\Delta\\tau_s$ (Corollary~\\ref{cor:a5_relaxation}, Appendix~\\ref{app:a5_violation}).\nEC-HTE's correction does not depend on (A5): each $\\hat{C}_s^{-1}$ corrects the local misclassification structure regardless of whether $\\Delta\\tau$ varies; under both positive and negative $\\Delta\\tau_s$--$\\delta_s$ correlation, EC-HTE maintains $\\geq$93\\% coverage while global correction degrades to 74--82\\% (Appendix~\\ref{app:a5_violation}).\n\nThe identity extends to $K > 2$ subgroups with $J$ effect-modifier levels; the multi-class bias retains the same product structure with modified amplification terms (Corollary~\\ref{cor:multiclass} in Appendix~\\ref{app:multiclass}).\n\nAssumption~(A3) ensures $M_s = C_s$; when $P(Z{=}1) \\neq 0.5$, the mixing matrices acquire asymmetric entries, but the product structure persists with modified coefficients (Appendix~\\ref{app:derivation}).\nEmpirical verification under class imbalance (Appendix~\\ref{app:classimbalance}) shows that the bias identity maintains $R^2 \\geq 0.976$ even at $P(Z{=}1) = 0.1$ for $K{=}2$, though EC-HTE's RMSE ratio relative to global correction increases to 1.06--1.68 as class imbalance grows.\nIn practice, NLP classification tasks often exhibit substantial class imbalance (e.g., hate speech prevalence $\\ll 50\\%$), and practitioners should verify that the per-subgroup expert budget threshold remains satisfied under the actual class distribution.\nEmpirical verification (Section~\\ref{sec:bias_mechanism}) yields $R^2 = 0.994$ for $K{=}2$ and $R^2 = 0.974$ for $K{=}4$; the residual variance reflects finite-sample Monte Carlo noise, not model misspecification.\n\n\\paragraph{Sensitivity to (A1).}\nAssumption~(A1) is not empirically testable.\nIf misclassification correlates with potential outcomes ($\\gamma = \\mathrm{Corr}(\\mathbb{1}[\\hat{Z} {\\neq} Z],\\, Y(1){-}Y(0) \\mid Z, S) \\neq 0$), Theorem~\\ref{thm:bias_identity} gains an $O(\\gamma)$ perturbation; in NLP settings, this is plausible when LLM accuracy varies with outcome magnitude.\nSensitivity analysis frameworks~\\cite{lash2009applying,dorn2022sharp} can bound the degradation (Section~\\ref{sec:limitations}).\n\n\\paragraph{Finite-sample remainder.}\nTheorem~\\ref{thm:bias_identity} is a population-level identity.\nIn practice, confusion matrices are estimated from $n_{\\text{expert}}$ expert labels with $\\hat{C}_s = C_s + E_s$, $\\|E_s\\| = O_p(n_{\\text{expert}}^{-1/2})$; the resulting remainder is therefore $R_n = O_p(n_{\\text{expert}}^{-1/2} \\cdot \\kappa(C_s))$, motivating the singularity guard ($\\kappa > 100 \\to$ fallback) in Section~\\ref{sec:method}.\n\n\\begin{proposition}[Debiasing Can Increase Bias]\n\\label{prop:debiasing_hurts}\nUnder \\textnormal{(A1)--(A5)}, global correction produces larger absolute bias than the naive estimator ($|\\mathrm{bias}_{\\mathrm{global}}| > |\\mathrm{bias}_{\\mathrm{naive}}|$) in subgroup $s$ if and only if\n\\begin{equation}\n\\frac{|\\delta_s|}{(1 - 2\\bar{\\pi}) \\cdot \\pi_s} > 1.\n\\label{eq:hurts_condition}\n\\end{equation}\n\\end{proposition}\n\nEquation~\\eqref{eq:hurts_condition} partitions subgroups into two regimes.\nFor high-error subgroups ($\\pi_s > \\bar{\\pi}$), the condition reduces to $\\pi_s > 0.5$, excluded by~(A4).\nFor low-error subgroups ($\\pi_s < \\bar{\\pi}$), it holds whenever $\\pi_s < \\bar{\\pi} / (2(1 - \\bar{\\pi}))$---easily satisfied: when $\\bar{\\pi} = 0.15$, any subgroup with $\\pi_s < 0.088$ is harmed.\nThe mechanism is over-correction: global inversion applies a correction calibrated for the average error rate, so low-error subgroups are overcorrected (the correction overshoots and reverses bias sign) while high-error subgroups are under-corrected.\nFor subgroups with near-zero misclassification ($\\pi_s \\approx 0$), the naive estimator is nearly unbiased, yet global correction creates substantial bias---debiasing can be worse than doing nothing.\n\nIn our experiments (Section~\\ref{sec:bias_mechanism}), global correction increases bias in 50\\% of $K{=}2$ configurations across our parameter grid (260 of 520, excluding cases where $\\Delta\\pi{=}0$).\nWith the difference-in-means estimator, maximum amplification reaches $2.86\\times$ for $K{=}2$ and $2.41\\times$ for $K{=}4$; the mechanism operates across estimator types, with nonlinear estimators amplifying the effect further (Section~\\ref{sec:ec_hte_eval}).\nFigure~\\ref{fig:heatmap} visualizes the amplification across the full $\\Delta\\pi \\times \\Delta\\tau$ parameter grid.",
    "structuredPatch": [
      {
        "oldStart": 45,
        "oldLines": 6,
        "newStart": 45,
        "newLines": 7,
        "lines": [
          " Direct computation shows $M_{\\text{global}}^{-1} M_s - I = \\frac{\\delta_s}{1-2\\bar{\\pi}} \\bigl[\\begin{smallmatrix} -1 & 1 \\\\ 1 & -1 \\end{smallmatrix}\\bigr]$.",
          " Applying this matrix to $[\\tau(0),\\, \\tau(1)]^\\top$ produces the product form.",
          " The full derivation appears in Appendix~\\ref{app:derivation}.",
          "+For comparison with classical scalar attenuation~\\citep{frazis2003estimating}, see Section~\\ref{sec:related}.",
          " ",
          " \\begin{remark}",
          " Theorem~\\ref{thm:bias_identity} does not require assumption~(A2)."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Edit · `toolu_01W7XnyaVbxh7Pfa7DsEGKHb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "old_string": "The orthogonality of EC-HTE and PPCI follows from the distinct error sources they correct",
  "new_string": "The complementarity of EC-HTE and PPCI follows from the distinct error sources they correct"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "02301c36-15a9-4819-9346-dd16e3e6a270",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfTCbq1mJavYLkU3D8YAFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14448,
      "cache_read_input_tokens": 53368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14448
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-23T09:29:43.940Z_

<details><summary>↩ Tool result · `toolu_01W7XnyaVbxh7Pfa7DsEGKHb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "bb8c4d83-3057-496d-a1e3-6815d64468f1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
    "oldString": "The orthogonality of EC-HTE and PPCI follows from the distinct error sources they correct",
    "newString": "The complementarity of EC-HTE and PPCI follows from the distinct error sources they correct",
    "originalFile": "\\section{EC-HTE Procedure}\n\\label{app:algorithm}\n\n\\begin{algorithm}[t]\n\\caption{EC-HTE: Error-Corrected Heterogeneous Treatment Effects}\n\\label{alg:echte}\n\\begin{algorithmic}[1]\n\\Require Observations $\\{(Y_i, W_i, \\hat{Z}_i, X_i)\\}_{i=1}^N$; expert labels $\\{Z_j^*\\}_{j=1}^{n_{\\text{expert}}}$; subgroup map $S: \\mathcal{X} \\to \\{1,\\ldots,K\\}$\n\\Ensure Corrected CATE estimates $\\hat{\\tau}(z)$ with variance-adjusted CIs\n\\Statex\n\\State \\textbf{Preconditions:} verify $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$ and $\\max_s(\\text{FPR}_s, \\text{FNR}_s) < 0.5$; if either fails, use global correction\n\\Statex\n\\State \\textbf{Step 1: Estimate per-subgroup confusion matrices (HB)}\n\\For{$s = 1, \\ldots, K$}\n    \\State $C_s[j,\\cdot] \\sim \\mathrm{Dir}(\\alpha_0 \\cdot \\hat{C}_{\\text{global},j})$, \\; $\\alpha_0$ via empirical Bayes\n    \\State Gibbs sampler (4 chains, 4000 iter) on $\\{(\\hat{Z}_j, Z_j^*) : S_j = s\\}$\n    \\State $\\hat{C}_s \\gets$ posterior mean; verify $\\hat{R} < 1.01$\n\\EndFor\n\\Statex\n\\State \\textbf{Step 2: Correct observed outcome moments}\n\\For{$s = 1, \\ldots, K$}\n    \\If{$\\kappa(\\hat{C}_s) > 100$} $\\hat{C}_s \\gets \\bar{C}$ \\Comment{singularity guard}\n    \\EndIf\n    \\State $\\tilde{\\boldsymbol{\\mu}}_s \\gets \\hat{C}_s^{-1} \\hat{\\boldsymbol{\\mu}}_s$\n\\EndFor\n\\Statex\n\\State \\textbf{Step 3: CausalForestDML with variance-adjusted SEs}\n\\State Train CausalForest (honest splitting) on corrected outcome moments $\\tilde{\\boldsymbol{\\mu}}_s$\n\\State $\\mathrm{se}_{\\mathrm{adj},i} \\gets \\sqrt{\\mathrm{diag}(\\hat{C}_{S_i}^{-1}\\, \\mathrm{diag}(\\mathrm{se}_i^2)\\, \\hat{C}_{S_i}^{-\\top})}$\n\\State \\Return $\\hat{\\tau}(z)$ with 95\\% CIs from $\\mathrm{se}_{\\mathrm{adj}}$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\subsection{Condition Number Guard Ablation}\n\\label{app:kappa_ablation}\n\nThe singularity guard in Algorithm~\\ref{alg:echte} (line~6) falls back to global correction when $\\kappa(\\hat{C}_s) > 100$.\nWe verify that this threshold is not load-bearing by sweeping $\\kappa \\in \\{10, 25, 50, 100, 200, 500, 1000\\}$ under the standard DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 100 MC runs).\nAcross all configurations, the maximum observed condition number is $\\kappa_{\\max} = 1.89$ (mean 1.45, p99 1.89), providing a $53{\\times}$ safety margin below the $\\kappa{=}100$ threshold.\nConsequently, the guard never triggers at any tested threshold, and all $\\kappa$ values produce identical RMSE (HB: 0.076, Global: 0.077) and zero numerical instability.\nIn a stress test with near-random labeling ($\\pi_s \\approx 0.4$--$0.5$, $n_{\\text{expert}}{=}50$), the maximum condition number reaches 1{,}125, correctly triggering the $\\kappa{=}100$ guard and preventing catastrophic inversion.\nThe adaptive formula $\\kappa_{\\text{adapt}} = 10 \\sqrt{n_{\\text{expert}} / K}$ recovers $\\kappa{=}100$ for this regime and scales naturally with the estimation precision.\n\n\\section{Full Proof of Theorem~\\ref{thm:bias_identity}}\n\\label{app:derivation}\n\n\\paragraph{Setup.}\nUnder assumptions (A1)--(A4), the observed CATE in subgroup $s$ at effect-modifier level $z$ is\n\\begin{equation}\n\\tau_{\\text{obs}}(z, s) = \\sum_{z'} M_s[z, z'] \\cdot \\tau(z'),\n\\end{equation}\nwhere $M_s[z, z'] = P(Z{=}z' \\mid \\hat{Z}{=}z, S{=}s)$ is the mixing matrix.\nUnder (A2)--(A3), $M_s = \\bigl[\\begin{smallmatrix} 1-\\pi_s & \\pi_s \\\\ \\pi_s & 1-\\pi_s \\end{smallmatrix}\\bigr]$.\n\n\\paragraph{Global correction.}\nThe pooled mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s = \\bigl[\\begin{smallmatrix} 1-\\bar{\\pi} & \\bar{\\pi} \\\\ \\bar{\\pi} & 1-\\bar{\\pi} \\end{smallmatrix}\\bigr]$, with $\\bar{\\pi} = \\sum_s w_s \\pi_s$.\n\nGlobal correction applies $M_{\\text{global}}^{-1}$ to $\\tau_{\\text{obs}}(\\cdot, s)$:\n\\begin{equation}\n\\hat{\\tau}_{\\text{global}}(z, s) = [M_{\\text{global}}^{-1} M_s \\cdot \\boldsymbol{\\tau}]_z,\n\\end{equation}\nwhere $\\boldsymbol{\\tau} = [\\tau(0), \\tau(1)]^\\top$.\n\n\\paragraph{Bias computation.}\nThe bias is $\\hat{\\tau}_{\\text{global}}(z, s) - \\tau(z) = [(M_{\\text{global}}^{-1} M_s - I) \\boldsymbol{\\tau}]_z$.\n\nDirect computation gives:\n\\begin{equation}\nM_{\\text{global}}^{-1} = \\frac{1}{1 - 2\\bar{\\pi}} \\begin{bmatrix} 1-\\bar{\\pi} & -\\bar{\\pi} \\\\ -\\bar{\\pi} & 1-\\bar{\\pi} \\end{bmatrix}.\n\\end{equation}\nMultiplying by $M_s$:\n\\begin{equation}\n\\resizebox{.88\\columnwidth}{!}{$\\displaystyle\nM_{\\text{global}}^{-1} M_s = \\frac{1}{1-2\\bar{\\pi}} \\begin{bmatrix} (1{-}\\bar{\\pi})(1{-}\\pi_s) - \\bar{\\pi}\\pi_s & (1{-}\\bar{\\pi})\\pi_s - \\bar{\\pi}(1{-}\\pi_s) \\\\ -\\bar{\\pi}(1{-}\\pi_s) + (1{-}\\bar{\\pi})\\pi_s & -\\bar{\\pi}\\pi_s + (1{-}\\bar{\\pi})(1{-}\\pi_s) \\end{bmatrix}.\n$}\n\\end{equation}\n\nDefine $\\delta_s = \\pi_s - \\bar{\\pi}$. Substituting $\\pi_s = \\bar{\\pi} + \\delta_s$:\n\\begin{equation}\nM_{\\text{global}}^{-1} M_s - I = \\frac{\\delta_s}{1-2\\bar{\\pi}} \\begin{bmatrix} -1 & 1 \\\\ 1 & -1 \\end{bmatrix}.\n\\end{equation}\n\nTo verify: the $(1,1)$ entry of $M_{\\text{global}}^{-1} M_s$ is\n{\\small\n\\begin{align}\n&\\frac{(1{-}\\bar{\\pi})(1{-}\\bar{\\pi}{-}\\delta_s) - \\bar{\\pi}(\\bar{\\pi}{+}\\delta_s)}{1-2\\bar{\\pi}} \\nonumber\\\\\n&= \\frac{(1{-}\\bar{\\pi})^2 - (1{-}\\bar{\\pi})\\delta_s - \\bar{\\pi}^2 - \\bar{\\pi}\\delta_s}{1-2\\bar{\\pi}} \\nonumber\\\\\n&= \\frac{1 - 2\\bar{\\pi} - \\delta_s}{1-2\\bar{\\pi}} = 1 - \\frac{\\delta_s}{1-2\\bar{\\pi}}.\n\\end{align}\n}\n\nApplying $(M_{\\text{global}}^{-1} M_s - I)$ to $\\boldsymbol{\\tau}$:\n{\\small\n\\begin{align}\n\\text{bias}(z{=}0, s) &= \\tfrac{\\delta_s}{1-2\\bar{\\pi}}(-\\tau(0) + \\tau(1)) = +\\tfrac{\\delta_s \\cdot \\Delta\\tau}{1-2\\bar{\\pi}}, \\\\\n\\text{bias}(z{=}1, s) &= \\tfrac{\\delta_s}{1-2\\bar{\\pi}}(\\tau(0) - \\tau(1)) = -\\tfrac{\\delta_s \\cdot \\Delta\\tau}{1-2\\bar{\\pi}},\n\\end{align}\n}\nwhere $\\Delta\\tau = \\tau(1) - \\tau(0)$. \\qed\n\n\\section{Multi-class Extension and Proof}\n\\label{app:multiclass}\n\n\\begin{corollary}[Multi-class Extension]\n\\label{cor:multiclass}\nFor $K > 2$ subgroups with $J$ effect-modifier levels and uniform off-diagonal misclassification (misclassified observations from class $j$ are distributed equally among the remaining $J{-}1$ classes), the subgroup bias of global correction generalizes to\n\\begin{equation}\n\\mathrm{bias}_{\\mathrm{global}}(z, s) = \\sum_{j=1}^{J} \\bigl(\\bar{\\pi}_j - \\pi_{s,j}\\bigr) \\cdot \\bigl(\\tau(j) - \\bar{\\tau}\\bigr) \\cdot g(\\bar{\\pi}),\n\\label{eq:multiclass}\n\\end{equation}\nwhere $g(\\bar{\\pi})$ collects the matrix-inversion amplification terms.\\footnote{For $J=3$ with symmetric misclassification (off-diagonal errors uniform), $g(\\bar{\\pi}) = 1/(1 - 3\\bar{\\pi}/2)$, generalizing the $J{=}2$ factor $1/(1-2\\bar{\\pi})$. In general, $g(\\bar{\\pi}) = 1/(1 - J\\bar{\\pi}/(J-1))$.}\nThe essential structure, $\\sum_s w_s (\\bar{\\pi}_j - \\pi_{s,j}) = 0$, ensures that bias redistributes across subgroups rather than vanishing in aggregate.\n\\end{corollary}\n\n\\paragraph{Proof.}\nFor $K > 2$ subgroups with $J$ effect-modifier levels, the subgroup-specific mixing matrix $M_s$ is $J \\times J$ with entries $M_s[j, j'] = P(Z{=}j' \\mid \\hat{Z}{=}j, S{=}s)$.\nThe global mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s$.\n\nThe bias of global correction in subgroup $s$ at level $z$ is:\n\\begin{equation}\n\\text{bias}_{\\text{global}}(z, s) = [(M_{\\text{global}}^{-1} M_s - I) \\boldsymbol{\\tau}]_z.\n\\end{equation}\n\nWrite $M_s = M_{\\text{global}} + \\Delta_s$ where $\\Delta_s = M_s - M_{\\text{global}}$ satisfies $\\sum_s w_s \\Delta_s = 0$.\nThen $M_{\\text{global}}^{-1} M_s = I + M_{\\text{global}}^{-1} \\Delta_s$, so:\n\\begin{equation}\n\\text{bias}_{\\text{global}}(z, s) = [M_{\\text{global}}^{-1} \\Delta_s \\cdot \\boldsymbol{\\tau}]_z.\n\\end{equation}\n\nFor symmetric misclassification with per-class error rates $\\pi_{s,j}$ and pooled rates $\\bar{\\pi}_j$, the entries of $\\Delta_s$ have the form $\\Delta_s[j,j'] = (\\bar{\\pi}_j - \\pi_{s,j}) \\cdot h(j, j')$ for a function $h$ determined by the off-diagonal redistribution pattern.\nExpanding the matrix-vector product and collecting terms yields:\n\\begin{equation}\n\\text{bias}_{\\text{global}}(z, s) = \\sum_{j=1}^{J} (\\bar{\\pi}_j - \\pi_{s,j}) \\cdot (\\tau(j) - \\bar{\\tau}) \\cdot g(\\bar{\\pi}),\n\\end{equation}\nwhere $g(\\bar{\\pi})$ collects the matrix-inversion amplification terms and $\\bar{\\tau} = \\sum_j P(Z{=}j) \\tau(j)$.\n\nThe essential structure $\\sum_s w_s (\\bar{\\pi}_j - \\pi_{s,j}) = 0$ ensures that the weighted bias across subgroups sums to zero: global correction redistributes bias rather than creating or eliminating it in aggregate.\nFor non-uniform off-diagonal entries, the scalar amplification $g(\\bar{\\pi})$ generalizes to a cell-specific matrix; the product structure $B_s \\cdot \\Delta\\tau$ persists but a closed-form amplification factor does not. \\qed\n\n\\section{Proof of Proposition~\\ref{prop:debiasing_hurts}}\n\\label{app:debiasing_hurts}\n\nThe naive estimator has bias $\\tau_{\\text{obs}}(z,s) - \\tau(z)$.\nUnder (A2)--(A3), $\\tau_{\\text{obs}}(0,s) = (1-\\pi_s)\\tau(0) + \\pi_s\\tau(1)$, so $\\text{bias}_{\\text{naive}}(0,s) = \\pi_s \\cdot \\Delta\\tau$.\n\nGlobal correction produces larger absolute bias when $|\\text{bias}_{\\text{global}}(0,s)| > |\\text{bias}_{\\text{naive}}(0,s)|$:\n\\begin{equation}\n\\frac{|\\delta_s| \\cdot |\\Delta\\tau|}{|1-2\\bar{\\pi}|} > \\pi_s \\cdot |\\Delta\\tau|.\n\\end{equation}\nSince $\\Delta\\tau \\neq 0$ (otherwise both biases are zero), dividing through gives:\n\\begin{equation}\n\\frac{|\\delta_s|}{(1-2\\bar{\\pi}) \\cdot \\pi_s} > 1,\n\\end{equation}\nwhere we use $1-2\\bar{\\pi} > 0$ from (A4).\n\nFor high-error subgroups ($\\pi_s > \\bar{\\pi}$, so $\\delta_s > 0$): the condition becomes $(\\pi_s - \\bar{\\pi}) / ((1-2\\bar{\\pi})\\pi_s) > 1$, which simplifies to $\\pi_s(1 - 1 + 2\\bar{\\pi}) > \\bar{\\pi}$, i.e., $2\\bar{\\pi}\\pi_s > \\bar{\\pi}$, i.e., $\\pi_s > 0.5$.\nThis is excluded by (A4), so global correction always reduces bias in high-error subgroups.\n\nFor low-error subgroups ($\\pi_s < \\bar{\\pi}$, so $\\delta_s < 0$): the condition becomes $(\\bar{\\pi} - \\pi_s) / ((1-2\\bar{\\pi})\\pi_s) > 1$, which gives $\\pi_s < \\bar{\\pi} / (1 - 2\\bar{\\pi} + 1) = \\bar{\\pi} / (2(1-\\bar{\\pi}))$.\nWhen $\\bar{\\pi} = 0.15$, any subgroup with $\\pi_s < 0.088$ experiences increased bias from global correction. \\qed\n\n\\paragraph{Extension to asymmetric misclassification.}\nProposition~\\ref{prop:debiasing_hurts} assumes symmetric error rates (A2).\nUnder asymmetric misclassification ($\\mathrm{FPR}_s \\neq \\mathrm{FNR}_s$), the naive bias becomes $\\mathrm{bias}_{\\mathrm{naive}}(0,s) = \\mathrm{FPR}_s \\cdot \\tau(1) + (1 - \\mathrm{FPR}_s - 1)\\tau(0)$ and the global correction bias depends on the full $2 \\times 2$ structure of $B_s = M_{\\mathrm{global}}^{-1} M_s - I$ (Remark~1 in Section~\\ref{sec:theory}).\nA sufficient condition for global correction to increase bias is\n\\begin{equation}\n\\|B_s\\|_\\infty > \\max(\\mathrm{FPR}_s, \\mathrm{FNR}_s),\n\\end{equation}\nwhich reduces to Equation~\\eqref{eq:hurts_condition} when $\\mathrm{FPR}_s = \\mathrm{FNR}_s = \\pi_s$.\nIn the asymmetric experiments (Appendix~\\ref{app:asymmetric}), the symmetric diagnostic still achieves AUC $= 0.82$ when applied with $\\pi_s = (\\mathrm{FPR}_s + \\mathrm{FNR}_s)/2$, suggesting practical robustness.\nA fully general asymmetric diagnostic that accounts for the separate roles of FPR and FNR in each entry of $B_s$ is left to future work.\n\n\\section{Semi-Synthetic Data Generating Process}\n\\label{app:dgp}\n\n\\paragraph{Synthetic DGP (Sections~\\ref{sec:bias_mechanism}--\\ref{sec:diagnostic} and Appendix~\\ref{sec:budget}).}\nWe generate $N = 5000$ observations.\nEach observation belongs to one of $K \\in \\{2, 4\\}$ subgroups $S \\in \\{1, \\ldots, K\\}$ with equal weights $w_s = 1/K$.\nThe binary effect modifier $Z \\in \\{0, 1\\}$ is drawn with $P(Z{=}1) = 0.5$.\nTreatment assignment is $T \\sim \\text{Bernoulli}(0.5)$, independent of $Z$ and $S$.\n\nThe outcome is generated as:\n\\begin{equation}\nY = \\tau(Z) \\cdot T + \\varepsilon, \\quad \\varepsilon \\sim \\mathcal{N}(0, 1),\n\\end{equation}\nwhere the CATE function is $\\tau(z) = \\bar{\\tau} + \\Delta\\tau \\cdot (z - 0.5)$ with $\\bar{\\tau} = 0.5$.\nThe CATE heterogeneity $\\Delta\\tau \\in \\{0, 0.2, 0.5, 1.0\\}$ controls the strength of treatment effect variation across levels of $Z$.\n\nMisclassification is symmetric: $\\hat{Z} \\neq Z$ with probability $\\pi_s$ depending on subgroup.\nFor $K{=}2$: $\\pi_1 = \\bar{\\pi} - \\Delta_c/2$, $\\pi_2 = \\bar{\\pi} + \\Delta_c/2$, with $\\bar{\\pi} \\in \\{0.1, 0.2\\}$ and $\\Delta_c \\in \\{0, 0.05, 0.1, 0.15\\}$.\nFor $K{=}4$, extreme regime: $\\pi \\in \\{0.05, 0.10, 0.15, 0.25\\}$; moderate regime: $\\pi \\in \\{0.08, 0.12, 0.16, 0.20\\}$.\n\nExpert labels are drawn as a simple random sample of size $n_{\\text{expert}} \\in \\{50, 100, 250, 500, 1000, 2000\\}$ from the full dataset, with true $Z$ observed for these observations.\n\n\\paragraph{Semi-synthetic DGP (Section~\\ref{sec:ec_hte_eval}).}\nWe sample $N = 5000$ tweets from the TweetEval sentiment corpus ($N_{\\text{pool}} = 57{,}899$).\nSubgroups are defined by crossing \\texttt{has\\_hashtag} $\\times$ \\texttt{text\\_length\\_bin} (short/medium/long), yielding $K = 4$ subgroups with empirical sizes: $S_0 \\approx 38\\%$, $S_1 \\approx 38\\%$, $S_2 \\approx 12\\%$, $S_3 \\approx 12\\%$.\nMisclassification rates in the extreme regime are $\\pi_{S_0} = 0.05$, $\\pi_{S_1} = 0.10$, $\\pi_{S_2} = 0.15$, $\\pi_{S_3} = 0.25$, reflecting empirical evidence that hashtag-heavy text degrades LLM classifier accuracy.\nThe outcome DGP follows the same structure as the synthetic case, with CATE injected onto the real text-derived subgroup structure.\n\n\\paragraph{PPCI DGPs (Appendix~\\ref{sec:ppci}).}\nFour DGPs isolate error types: (A) covariate error only ($\\sigma_{\\text{outcome}} = 0$), (B) outcome error only ($\\sigma_{\\text{outcome}} = 0.5$), (C) both errors ($\\sigma_{\\text{outcome}} = 0.5$), (D) no error ($\\sigma_{\\text{outcome}} = 0$).\nOutcome-side error is additive Gaussian noise on $Y$.\n\n\\paragraph{CausalForestDML hyperparameters.}\nAll CausalForest experiments use \\texttt{econml.dml.CausalForestDML} with honest splitting, $n_{\\text{estimators}} = 48$, $\\texttt{min\\_samples\\_leaf} = 20$, \\texttt{model\\_y} = \\texttt{LassoCV}(cv=3), and \\texttt{model\\_t} = \\texttt{LogisticRegressionCV}.\nThese defaults were held constant across all configurations; no hyperparameter tuning was performed.\n\n\\section{Extended Related Work}\n\\label{app:related}\n\n\\paragraph{Measurement error details.}\n\\citet{fuller1987measurement} establish the foundational theory showing that naive regression with mismeasured covariates yields attenuated coefficient estimates.\n\\citet{carroll2006measurement} extend this to nonlinear models.\n\\citet{gustafson2003measurement} develops Bayesian treatments modeling measurement jointly with outcomes.\n\\citet{hu2008nonparametric} provide nonparametric identification using repeated measurements or instruments.\n\n\\paragraph{Annotation model extensions.}\nBeyond the foundational \\citet{dawid1979maximum} model, \\citet{passonneau2014benefits} incorporate item difficulty, \\citet{hovy2013learning} learn annotator competence, and \\citet{paun2018comparing} introduce hierarchical priors sharing information across annotators with varying expertise.\n\n\\paragraph{PPI extensions and text-as-data methods.}\n\\citet{zrnic2024cross} extend PPI via cross-prediction; their active inference framework~\\citep{zrnic2024active} achieves $>$80\\% expert budget savings through adaptive allocation, complementary to our fixed-budget analysis.\n\\citet{grimmer2022text} provide methodological guidance for text-as-data pipelines.\n\\citet{audinet2025benchmarking} systematically benchmark DSL and PPI methods for LLM-based parameter estimation, finding that debiasing can increase MSE when prediction error is heterogeneous---a population-level analogue of the subgroup-conditional bias amplification we formalize in Theorem~\\ref{thm:bias_identity}.\n\n\\paragraph{Treatment vs.\\ effect-modifier misclassification.}\n\\citet{imai2010causal} study treatment misclassification where errors change which arm a unit is assigned to, requiring instrumental variables or partial identification because the fundamental treated-vs-control contrast is corrupted.\nOur problem preserves the treatment contrast ($T$ is observed correctly) but corrupts the heterogeneity structure ($\\hat{Z} \\neq Z$).\nThe ATE remains identified; only conditional effects are biased, which makes exact correction through confusion matrix inversion feasible.\n\n\\paragraph{Econometrics of binary misclassification.}\n\\citet{bound2001measurement} survey measurement error in survey data, establishing that binary misclassification attenuates regression coefficients.\n\\citet{frazis2003estimating} derive exact bias formulas for OLS with a misclassified binary regressor, showing attenuation proportional to the misclassification rate---analogous to our Theorem~\\ref{thm:bias_identity} but restricted to average effects without subgroup heterogeneity.\n\\citet{black2000racial} demonstrate that racial misclassification in administrative data can substantially bias estimates of racial disparities.\n\\citet{mahajan2006identification} and \\citet{lewbel2007estimation} develop instrumental variable approaches to identify models with misclassified binary regressors, requiring exclusion restrictions unavailable when the mismeasured variable is an LLM annotation.\nOur setting differs in three respects: (i) the mismeasured variable is an effect modifier indexing the CATE function, not a standard regressor; (ii) misclassification rates vary across subgroups, creating the $\\delta_s \\times \\Delta\\tau$ product amplification absent from homogeneous-error analyses; and (iii) expert labels provide a direct calibration sample, enabling confusion matrix estimation without instruments.\n\n\\section{MCMC Convergence Diagnostics}\n\\label{app:mcmc}\n\nTable~\\ref{tab:mcmc} reports convergence diagnostics for the hierarchical Bayesian confusion matrix estimator across all experimental configurations.\nAll runs use 4 chains with 4000 iterations (2000 warmup).\nMain experiments (Table~\\ref{tab:main_results}) use a Dirichlet prior centered on $\\hat{C}_{\\text{global}}$ with concentration $\\alpha_0$ estimated via empirical Bayes (marginal likelihood).\nAppendix robustness experiments use a fixed Dirichlet prior ($\\alpha{=}3$); since fixed-$\\alpha$ partial pooling is weakly dominated by the adaptive variant, these results are conservative.\nThis budget is sufficient for the $2{\\times}2$ Dirichlet-Multinomial posterior; all runs achieve $\\hat{R} < 1.0034$ and ESS $> 1618$, confirming convergence with substantial margin.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nDiagnostic & Threshold & Achieved \\\\\n\\midrule\n$\\hat{R}$ (max across all params) & $< 1.01$ & $< 1.0034$ \\\\\nESS (min across all params) & $> 845$ & $> 1618$ \\\\\nDivergent transitions & $= 0$ & $0$ \\\\\nSingularity guard triggers & --- & extreme/$n{=}50$ only \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{MCMC convergence diagnostics for the hierarchical Bayesian estimator. All configurations satisfy convergence criteria with substantial margin.}\n\\label{tab:mcmc}\n\\end{table}\n\n\\paragraph{Hyperprior sensitivity.}\nScaling the $\\text{Gamma}(3, 1)$ hyperprior by factors of $0.5\\times$ to $2\\times$ produces $<$1\\% RMSE variation for $K{=}2$ and $\\sim$4--5\\% for $K{=}4$.\nCoverage remains invariant across the sensitivity range.\nThese results confirm that the hierarchical estimator is robust to prior specification within a reasonable range.\n\n\\section{Diagnostic ROC Curves}\n\\label{app:roc}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_roc.png}\n\\caption{ROC curves for the $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}): $|\\delta_s|/((1{-}2\\bar\\pi)\\cdot\\pi_s)>1$. (A)~Setting-level ROC (AUC $= 0.89$), compared with the $|\\Delta\\pi \\times \\Delta\\tau|$ product (AUC $= 0.89$) and $\\mathrm{CV}(\\pi_s)$ (AUC $= 0.97$). (B)~Subgroup-level ROC: the $\\Delta\\pi$-only condition (AUC $= 0.86$) substantially outperforms the $|\\Delta\\pi \\times \\Delta\\tau|$ product (AUC $= 0.73$). The $\\Delta\\tau$-free diagnostic depends only on estimable misclassification rates, breaking the circular dependency that would arise if CATE heterogeneity were required.}\n\\label{fig:roc}\n\\end{figure}\n\n\\paragraph{Cost-asymmetric diagnostic thresholds.}\nIn practice, the cost of a false negative (failing to detect that global correction increases bias) exceeds the cost of a false positive (unnecessarily applying EC-HTE when global correction would suffice), because the former propagates systematic bias into CATE estimates while the latter only incurs additional estimation variance.\nPractitioners in high-stakes settings (e.g., policy evaluation where CATE estimates inform resource allocation) should lower the diagnostic threshold to favor recall over precision, accepting more false positives to minimize the risk of undetected bias amplification.\n\n\\section{Expert Budget Crossover Curves}\n\\label{app:budget}\n\\label{sec:budget}\n\nThe crossover point at which EC-HTE achieves lower RMSE than global correction is $n_{\\text{expert}} = 250$ for $K{=}2$/extreme and $n_{\\text{expert}} = 1000$ for $K{=}4$/extreme (Figure~\\ref{fig:budget}).\nUnder moderate heterogeneity ($K{=}2$), EC-HTE never achieves lower RMSE than global at any budget.\nHB partial pooling improves over stratified MLE in 21 of 24 configurations, with the two estimators converging by $n_{\\text{expert}} \\geq 1000$.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig3_budget.pdf}\n\\caption{RMSE vs.\\ expert budget ($n_{\\text{expert}}$) across four regime$\\times K$ combinations. Dashed vertical lines mark crossover points where EC-HTE achieves lower RMSE than global correction: $n{=}250$ ($K{=}2$, extreme), $n{=}1000$ ($K{=}4$, extreme). Under moderate heterogeneity ($K{=}2$), global correction dominates at all budgets. Shaded bands show $\\pm 1$ SD across subgroups within each configuration.}\n\\label{fig:budget}\n\\end{figure*}\n\n\\subsection{Budget Sensitivity: HB vs.\\ Stratified MLE}\n\\label{app:budget_sensitivity}\n\nHierarchical Bayes (HB) partial pooling borrows strength across subgroups, which should matter most when per-subgroup expert labels are scarce.\nWe sweep $n_{\\text{expert}} \\in \\{25, 50, 75, 100, 150, 250\\}$ under extreme heterogeneity ($\\Delta\\tau{=}0.3$, 100 MC runs, $N{=}5{,}000$).\nTable~\\ref{tab:budget_sensitivity} reports aggregate RMSE for global correction, stratified MLE, and HB EC-HTE.\n\n\\begin{table}[h]\n\\centering\n\\caption{RMSE across expert budgets under extreme heterogeneity.\nHB crossover (first budget where HB $<$ MLE) occurs at approximately 10 expert labels per subgroup-cell:\n$n_{\\text{expert}}{=}50$ for $K{=}2$ and $n_{\\text{expert}}{=}75$ for $K{=}4$.}\n\\label{tab:budget_sensitivity}\n\\small\n\\begin{tabular}{crrrrc}\n\\toprule\n$K$ & $n_{\\text{expert}}$ & Global & Strat.\\ MLE & HB EC-HTE & HB vs.\\ MLE \\\\\n\\midrule\n2 & 25 & \\textbf{0.101} & 0.256 & 0.269 & $+4.9\\%$ \\\\\n2 & 50 & \\textbf{0.088} & 0.275 & 0.231 & $\\mathbf{-16.1\\%}$ \\\\\n2 & 75 & 0.084 & 0.091 & \\textbf{0.089} & $-1.9\\%$ \\\\\n2 & 100 & 0.083 & 0.085 & \\textbf{0.084} & $-0.8\\%$ \\\\\n2 & 150 & 0.081 & 0.077 & \\textbf{0.077} & $-0.4\\%$ \\\\\n2 & 250 & 0.080 & 0.075 & \\textbf{0.074} & $-0.1\\%$ \\\\\n\\midrule\n4 & 25 & \\textbf{0.129} & 0.401 & 0.612 & $+52.5\\%$ \\\\\n4 & 50 & \\textbf{0.117} & 0.380 & 0.470 & $+23.8\\%$ \\\\\n4 & 75 & \\textbf{0.112} & 0.221 & 0.211 & $\\mathbf{-4.4\\%}$ \\\\\n4 & 100 & \\textbf{0.112} & 0.215 & 0.212 & $-1.3\\%$ \\\\\n4 & 150 & \\textbf{0.109} & 0.157 & 0.152 & $-3.6\\%$ \\\\\n4 & 250 & \\textbf{0.108} & 0.127 & 0.126 & $-1.0\\%$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree regimes emerge.\nAt very low budgets ($n_{\\text{expert}} < 50$ for $K{=}2$, $< 75$ for $K{=}4$), per-subgroup counts are insufficient for reliable confusion matrix estimation; global pooling dominates because the variance cost of stratification overwhelms any bias reduction.\nHB degrades substantially in this regime because the Gibbs posterior, while better regularized than MLE, still cannot overcome the fundamental sample-size constraint with $\\sim$6--12 labels per subgroup.\nAt moderate budgets ($n_{\\text{expert}} = 50$--$250$ for $K{=}2$, $75$--$250$ for $K{=}4$), HB partial pooling provides consistent RMSE improvement over stratified MLE ($-0.4\\%$ to $-16.1\\%$), with the largest gains near the crossover point.\nAt high budgets ($n_{\\text{expert}} \\geq 250$), both estimators converge as subgroup-level data becomes sufficient for reliable MLE; the HB advantage diminishes to $< 1\\%$.\nCoverage remains $\\geq 0.88$ for both methods across all budget levels.\n\n\\subsection{Scalability to $K{=}8$ Subgroups}\n\\label{app:k8_subgroups}\n\nWe test EC-HTE at $K{=}8$ to identify the scalability boundary of hierarchical Bayesian partial pooling under fixed expert budget.\n\n\\paragraph{Setup.}\n$N{=}5{,}000$, $K{=}8$ (equal-weight subgroups), $n_{\\text{expert}}{=}250$ (${\\approx}31$ labels per subgroup), 100 MC replications.\nMisclassification rates are uniformly spread: $\\pi_s \\in \\{0.05, 0.09, 0.13, 0.18, 0.22, 0.26, 0.30, 0.35\\}$.\nTreatment effects depend on $Z$ (not subgroup): $\\tau(Z{=}0){=}0$, $\\tau(Z{=}1){=}0.3$.\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE at $K{=}8$ ($n_{\\text{expert}}{=}250$, ${\\approx}31$ labels/subgroup, 100 MC).}\n\\label{tab:k8_subgroups}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Coverage & RMSE & $|\\text{Bias}|$ \\\\\n\\midrule\nOracle       & 0.944 & 0.113 & 0.090 \\\\\nGlobal       & 0.951 & 0.168 & 0.135 \\\\\nHB EC-HTE    & 0.956 & 0.340 & 0.183 \\\\\nStrat MLE    & 0.953 & 0.638 & 0.219 \\\\\nNaive        & 0.913 & 0.133 & 0.107 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll CM-aware methods achieve nominal coverage at $K{=}8$: HB EC-HTE 95.6\\%, Strat MLE 95.3\\%, Global 95.1\\%.\nHB partial pooling achieves a 47\\% RMSE reduction over stratified MLE (0.340 vs.\\ 0.638), confirming that hierarchical shrinkage provides substantial regularization.\nHowever, HB RMSE (0.340) exceeds global correction (0.168), indicating that ${\\approx}31$ expert labels per subgroup are insufficient for per-subgroup CM estimation to outweigh variance inflation.\n\n\\paragraph{Per-subgroup breakdown.}\nTable~\\ref{tab:k8_per_subgroup} decomposes RMSE by subgroup.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-subgroup RMSE at $K{=}8$. HB improvement over MLE is largest in high-$\\pi$ subgroups but does not close the gap with Global.}\n\\label{tab:k8_per_subgroup}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\nSubgroup & $\\pi_s$ & HB RMSE & MLE RMSE & Global RMSE & HB Cov \\\\\n\\midrule\n$s_0$ & 0.050 & 0.136 & 0.134 & \\textbf{0.181} & 0.950 \\\\\n$s_1$ & 0.093 & 0.133 & 0.132 & \\textbf{0.154} & 0.970 \\\\\n$s_2$ & 0.136 & 0.154 & 0.154 & 0.161 & 0.975 \\\\\n$s_3$ & 0.179 & 0.178 & 0.182 & \\textbf{0.159} & 0.945 \\\\\n$s_4$ & 0.221 & 0.263 & 0.343 & \\textbf{0.163} & 0.940 \\\\\n$s_5$ & 0.264 & 0.421 & 0.711 & \\textbf{0.164} & 0.965 \\\\\n$s_6$ & 0.307 & 0.634 & 1.375 & \\textbf{0.177} & 0.940 \\\\\n$s_7$ & 0.350 & 0.432 & 0.809 & \\textbf{0.183} & 0.960 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRMSE degradation is concentrated in high-$\\pi$ subgroups ($s_4$--$s_7$, $\\pi \\geq 0.22$), where confusion matrix inversion amplifies estimation noise ($r = 0.87$, $p = 0.005$ for correlation between $\\pi_s$ and HB RMSE).\nLow-error subgroups ($s_0$--$s_1$) benefit from stratification, with HB RMSE 14--25\\% below global correction.\nHB partial pooling reduces MLE RMSE by 24--54\\% in the high-$\\pi$ regime ($s_4$--$s_7$), confirming that hierarchical shrinkage provides meaningful regularization even when per-subgroup labels are scarce.\nCoverage remains $\\geq$0.94 across all subgroups for HB EC-HTE, indicating that variance inflation does not compromise inference validity.\nAdaptive shrinkage---increasing the prior strength for high-$\\pi$ subgroups where CM estimation is least reliable---is a natural extension that may close the RMSE gap with global correction at larger $K$.\n\nWe explored adaptive shrinkage ($\\alpha{=}10$ for high-$\\pi$ subgroups vs.\\ default $\\alpha{=}3$), which reduces aggregate RMSE from 0.340 to 0.216 (35\\% improvement) by attenuating estimation noise in high-$\\pi$ subgroups.\nHowever, RMSE remains 30\\% above global correction (0.166), confirming that the bottleneck is per-subgroup sample size (${\\sim}$31 expert labels) rather than the shrinkage method itself.\nThis establishes $K{=}8$ at $n_{\\text{expert}}{=}250$ as a boundary condition: all correction methods provide valid inference (coverage $\\geq$94\\%), but per-subgroup stratification requires proportionally larger expert budgets---approximately $n_{\\text{expert}} \\geq 500$ (${\\approx}60$ labels/subgroup)---to achieve RMSE parity with global correction.\n\n\\section{Asymmetric Misclassification Extension}\n\\label{app:asymmetric}\n\nAssumption~(A2) imposes symmetric misclassification ($\\text{FPR}_s = \\text{FNR}_s = \\pi_s$), which simplifies the bias decomposition but is not necessary for it.\nReal LLM annotators typically exhibit asymmetric confusion patterns; we show here that the product structure generalizes.\n\n\\paragraph{General bias formula.}\nFor asymmetric confusion matrices $C_s = \\bigl(\\begin{smallmatrix} 1{-}\\text{FPR}_s & \\text{FPR}_s \\\\ \\text{FNR}_s & 1{-}\\text{FNR}_s \\end{smallmatrix}\\bigr)$, define the mixing matrix $M_s$ via Bayesian inversion and the residual matrix $B_s = M_{\\text{global}}^{-1} M_s - I$.\nSince both $M_s$ and $M_{\\text{global}}$ are row-stochastic, $B_s \\mathbf{1} = \\mathbf{0}$.\nDecomposing $\\boldsymbol{\\tau} = \\tau(0)\\mathbf{1} + \\Delta\\tau \\, \\mathbf{e}_1$ gives:\n\\begin{equation}\n\\text{bias}(z, s) = \\Delta\\tau \\cdot [B_s]_{z,1},\n\\end{equation}\nwhere $[B_s]_{z,1}$ depends only on $\\{\\text{FPR}_k, \\text{FNR}_k, w_k\\}$, not on $\\Delta\\tau$.\nUnder~(A2), this reduces to $\\delta_s \\Delta\\tau / (1 - 2\\bar{\\pi})$ (Theorem~\\ref{thm:bias_identity}).\n\n\\paragraph{Empirical validation.}\nWe test three asymmetric configurations ($K{=}2$, $n_{\\text{expert}}{=}250$, 100 MC runs each): \\emph{Cross} (FPR/FNR = 0.10/0.20 vs.\\ 0.25/0.10), \\emph{Co-directional} (0.05/0.15 vs.\\ 0.20/0.30), and \\emph{Extreme} (0.03/0.25 vs.\\ 0.30/0.05).\nRegressing analytic predictions on MC bias yields $R^2 = 0.991$ across all configurations, confirming the product structure under asymmetry.\nTable~\\ref{tab:asymmetric} reports correction performance averaged over subgroups, $z$-levels, and $\\Delta\\tau \\in \\{0.1, \\ldots, 0.5\\}$.\nEC-HTE reduces $|\\text{bias}|$ from 0.025 (global) to 0.006, a $4\\times$ improvement, with lower RMSE (0.033 vs.\\ 0.040) and substantially better coverage (0.90 vs.\\ 0.78).\n\n\\begin{table}[t]\n\\centering\n\\caption{Asymmetric misclassification results ($K{=}2$, $n_{\\text{expert}}{=}250$, 100 MC runs). Values averaged over subgroups, $z$-levels, and $\\Delta\\tau$.}\n\\label{tab:asymmetric}\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\nMethod & $|\\text{Bias}| \\downarrow$ & RMSE $\\downarrow$ & Coverage $\\uparrow$ \\\\\n\\midrule\nNaive & 0.047 & 0.053 & 0.48 \\\\\nGlobal & 0.025 & 0.040 & 0.78 \\\\\nHB EC-HTE & \\textbf{0.006} & \\textbf{0.033} & \\textbf{0.90} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Supplementary Main Results}\n\\label{app:main_supp}\n\n\\begin{table}[t]\n\\centering\n\\caption{Additional configurations from the main experiment. $|\\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and 100 MC runs. $^\\dagger$RMSE exceeds Global.}\n\\label{tab:main_supp}\n\\small\n\\begin{tabular}{ll ccc}\n\\toprule\nConfiguration & Method & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Synthetic DIM\\\\$K{=}2$, moderate, $n{=}250$}}\n & Naive & 0.018 & 0.064 & 0.95 \\\\\n & Global & 0.009 & 0.074 & 0.96 \\\\\n & Strat.\\ MLE & \\textbf{0.005} & 0.075$^\\dagger$ & 0.97 \\\\\n & HB EC-HTE & \\textbf{0.005} & 0.075$^\\dagger$ & 0.97 \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Semi-synthetic\\\\TweetEval, extreme, $n{=}250$}}\n & Naive & 0.027 & 0.103 & 0.93 \\\\\n & Global & \\textbf{0.023} & 0.124 & 0.92 \\\\\n & Strat.\\ MLE & 0.032 & 0.248$^\\dagger$ & 0.91 \\\\\n & HB EC-HTE & 0.027 & 0.225$^\\dagger$ & 0.91 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{PPCI Complementarity Results}\n\\label{app:ppci}\n\\label{sec:ppci}\n\nEC-HTE composes with PPCI~\\cite{sui2026ppci} for settings where both covariate misclassification and outcome model error are present: EC-HTE+PPCI reduces $|\\text{bias}|$ from 0.179 to 0.007 ($z{=}0$, DGP~C), and the corrected pseudo-outcomes are compatible with other CATE estimators (R-learner bias reduction: 89\\%; Appendix~\\ref{app:rlearner}).\n\n\\begin{table*}[t]\n\\centering\n\\caption{PPCI complementarity experiment ($K{=}2$, extreme, $n_{\\text{expert}}{=}250$). DGP~A: covariate error only; B: outcome error only ($\\sigma{=}0.5$); C: both errors; D: no error. Values are $|\\text{bias}|$ and RMSE averaged over two subgroups. $^\\star$EC-HTE+PPCI achieves near-zero bias when both error types are present.}\n\\label{tab:ppci}\n\\small\n\\begin{tabular}{ll cccc}\n\\toprule\nDGP & Method & $|\\text{Bias}|_{z=0}$ & $|\\text{Bias}|_{z=1}$ & RMSE$_{z=0}$ & RMSE$_{z=1}$ \\\\\n\\midrule\n\\multirow{5}{*}{A: Covariate}\n & Naive & 0.053 & 0.063 & 0.087 & 0.093 \\\\\n & Global & 0.063 & 0.055 & 0.101 & 0.102 \\\\\n & EC-HTE & 0.017 & \\textbf{0.013} & 0.097 & 0.108 \\\\\n & PPCI & \\textbf{0.015} & 0.020 & 0.162 & 0.168 \\\\\n & EC-HTE+PPCI & 0.017 & \\textbf{0.013} & 0.097 & 0.108 \\\\\n\\midrule\n\\multirow{5}{*}{B: Outcome}\n & Naive & 0.189 & 0.197 & 0.206 & 0.212 \\\\\n & Global & 0.185 & 0.208 & 0.204 & 0.228 \\\\\n & EC-HTE & 0.181 & 0.215 & 0.202 & 0.237 \\\\\n & PPCI & 0.015 & \\textbf{0.020} & 0.171 & 0.176 \\\\\n & EC-HTE+PPCI & \\textbf{0.012} & 0.023 & 0.171 & 0.186 \\\\\n\\midrule\n\\multirow{5}{*}{C: Both}\n & Naive & 0.251 & 0.135 & 0.267 & 0.155 \\\\\n & Global & 0.182 & 0.209 & 0.233 & 0.235 \\\\\n & EC-HTE & 0.179 & 0.216 & 0.224 & 0.262 \\\\\n & PPCI & 0.017 & 0.007 & 0.241 & 0.232 \\\\\n & EC-HTE+PPCI$^\\star$ & \\textbf{0.007} & \\textbf{0.008} & 0.209 & 0.223 \\\\\n\\midrule\n\\multirow{5}{*}{D: None}\n & Naive & \\textbf{0.007} & 0.003 & 0.060 & 0.065 \\\\\n & Global & 0.010 & \\textbf{0.002} & 0.061 & 0.071 \\\\\n & EC-HTE & 0.013 & 0.007 & 0.062 & 0.079 \\\\\n & PPCI & \\textbf{0.007} & \\textbf{0.003} & 0.060 & 0.065 \\\\\n & EC-HTE+PPCI & 0.013 & 0.007 & 0.062 & 0.079 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe orthogonality of EC-HTE and PPCI follows from the distinct error sources they correct: EC-HTE addresses misclassification in the effect modifier $Z$ (covariate space), while PPCI corrects specification error in the outcome model $f(X)$ (prediction space).\nSince covariate misclassification and outcome model error are algebraically independent in the potential outcomes framework, their corrections compose without interference---confirmed by the 4-DGP orthogonal design (Table~\\ref{tab:ppci}), where DGP~C (both errors present) yields the largest bias reduction from the combined approach.\nUnder covariate error only, PPCI adds nothing; under no error, all methods perform equivalently.\n\n\\section{Real-Data Case Study: Hate Speech Detection}\n\\label{app:hatespeech}\n\nWe apply EC-HTE to the UC Berkeley Measuring Hate Speech corpus~\\cite{kennedy2020constructing}, annotating 2{,}496 comments for dehumanization using GPT-4.1.\nFour text-feature subgroups are defined by crossing platform (Reddit/Gab vs.\\ Twitter/YouTube) and text length (above/below median), yielding balanced groups ($n \\approx 624$ each).\n\n\\paragraph{Positive finding: real-world heterogeneity.}\nPer-subgroup misclassification rates range from 0.266 to 0.383, confirming heterogeneity ($\\Delta\\pi = 0.117$) in a real annotation setting.\nAt the error-type level, FPR ranges from 8.5\\% to 21.3\\% across text-feature subgroups, demonstrating that subgroup-varying misclassification is not an artifact of synthetic design but arises naturally in real NLP annotation tasks.\n\n\\paragraph{Boundary condition: statistical power at extreme FNR.}\nCorrection results are inconclusive: all corrected confidence intervals contain zero, and point estimate differences between methods are not statistically significant.\nThe high baseline FNR (53.3\\%) amplifies variance through matrix inversion (variance amplification factor up to 15.7$\\times$), rendering the comparison underpowered.\nWhen $P(\\hat{Z}{=}1 \\mid Z{=}1) \\approx 0.5$, the confusion matrix approaches singularity, and inversion amplifies estimation noise regardless of stratification strategy.\nThis complements the expert budget threshold identified in Appendix~\\ref{sec:budget}: EC-HTE requires \\emph{both} sufficient expert labels \\emph{and} sufficient baseline classifier quality.\n\n\\paragraph{Diagnostic connection.}\nThe diagnostic criterion ($\\Delta\\pi \\times \\Delta\\tau$, Section~\\ref{sec:diagnostic}) identifies when correction is worthwhile under moderate baseline accuracy.\nThis case study illustrates that even when $\\Delta\\pi$ is large, extreme baseline error renders correction underpowered rather than beneficial.\nA practical prerequisite is that the per-subgroup confusion matrix condition number $\\kappa(\\hat{C}_s)$ remain moderate; when $\\kappa > 50$, as observed here, practitioners should prioritize improving annotation quality before applying any matrix-inversion-based correction.\n\n\\section{Cross-Model Consistency}\n\\label{app:multilm}\n\nWe evaluate whether misclassification heterogeneity is model-specific by annotating 500 TweetEval sentiment tweets with six OpenAI models spanning three generations.\nSix text-feature subgroups are defined by crossing hashtag presence and text length.\nSpearman rank correlations of per-subgroup error rates across all six subgroups range from $\\rho = 0.82$ to $1.00$, indicating that the subgroup error structure is consistent across architectures.\nTwo subgroups with $n \\leq 6$ exhibit zero misclassification across all models; excluding these yields four-point correlations that are directionally consistent but underpowered.%\n\\footnote{The filtered $\\Delta\\pi$ values in Table~\\ref{tab:multilm} serve as a robustness check independent of rank-order testing: all six models exceed $\\Delta\\pi > 0.05$ on the four retained subgroups.}\n\n\\begin{table}[t]\n\\centering\n\\caption{Effective misclassification heterogeneity ($\\Delta\\pi$) across six OpenAI models on TweetEval sentiment (500 tweets, filtered to 4 subgroups with $n \\geq 10$).}\n\\label{tab:multilm}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nModel & Effective $\\Delta\\pi$ & $> 0.05$? \\\\\n\\midrule\nGPT-3.5-Turbo & 0.198 & \\checkmark \\\\\nGPT-4-Turbo & 0.149 & \\checkmark \\\\\nGPT-4o-mini & 0.136 & \\checkmark \\\\\nGPT-5.4 & 0.114 & \\checkmark \\\\\nGPT-4.1 & 0.098 & \\checkmark \\\\\nGPT-4o & 0.080 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll six models exhibit effective $\\Delta\\pi > 0.05$ on the four retained subgroups (Table~\\ref{tab:multilm}), and 5 of 6 share the same worst subgroup (\\texttt{True\\_medium}: tweets with hashtags and medium text length).\nNewer models reduce absolute error rates but do not eliminate subgroup heterogeneity: GPT-5.4 achieves $\\Delta\\pi = 0.114$ compared to GPT-3.5-Turbo's $0.198$.\nThese results were obtained with a single API provider; open-source model validation appears in Appendix~\\ref{app:multilm_opensource}.\n\n\\section{Open-Source Multi-LLM Validation}\n\\label{app:multilm_opensource}\n\nWe evaluate four open-source LLMs (7B--9B parameter range) on 490 TweetEval sentiment tweets with $K{=}4$ subgroups defined by crossing hashtag presence and text length.\nTable~\\ref{tab:multilm_cm} reports the confusion matrix heterogeneity profile.\nAll four models exhibit $\\Delta\\pi > 0.05$, confirming that subgroup-heterogeneous misclassification is not specific to proprietary APIs.\nSubgroup error rankings are consistent across architectures: \\texttt{True\\_short} (short tweets with hashtags) has the lowest $\\pi_s$ in 3 of 4 models, while \\texttt{False\\_medium} (medium tweets without hashtags) has the highest.\n\n\\begin{table}[t]\n\\centering\n\\caption{Confusion matrix heterogeneity across four open-source LLMs ($K{=}4$, $N{=}490$ TweetEval tweets). $\\Delta\\pi$: max--min per-subgroup misclassification rate. Prop2: number of subgroups where the $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}) triggers.}\n\\label{tab:multilm_cm}\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\nModel & Acc.\\ & $\\Delta\\pi$ & Prop2 & Strongest \\\\\n\\midrule\nLlama-3.1-8B & 0.755 & 0.141 & 1/4 & True\\_short \\\\\nQwen-2.5-7B & 0.798 & 0.165 & 1/4 & True\\_short \\\\\nGemma-2-9B & 0.763 & 0.125 & 4/4 & True\\_medium \\\\\nMistral-7B & 0.802 & 0.134 & 0/4 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Semi-synthetic budget sweep.}\nWe run the full EC-HTE pipeline with $K{=}2$ subgroups and $\\Delta\\tau{=}0.3$, using each model's empirical confusion matrices.\nTable~\\ref{tab:multilm_budget} reports coverage and RMSE crossover points.\nEC-HTE restores near-nominal coverage from 0.714 (naive average) to 0.939 ($+$22.5 percentage points) at $n_{\\text{expert}}{=}1{,}000$, consistent across all four models.\nGlobal correction achieves comparable or lower RMSE than HB at all budgets under these moderate $\\Delta\\pi$ values, and the $K{=}4$ RMSE crossover never occurs---confirming the budget guidelines in Appendix~\\ref{sec:budget}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Semi-synthetic budget sweep ($K{=}2$, $\\Delta\\tau{=}0.3$, 50 MC runs\\protect\\footnote{Appendix experiments use 50 MC replications unless otherwise noted; all main-text results use 100.}). Coverage at selected expert budgets; RMSE crossover denotes the minimum expert budget at which HB EC-HTE achieves lower RMSE than the naive (uncorrected) estimator.}\n\\label{tab:multilm_budget}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nModel & $\\Delta\\pi_{K{=}2}$ & Naive Cov.\\ & HB Cov.\\ ($n{=}1000$) & Crossover \\\\\n\\midrule\nLlama-3.1-8B & 0.051 & 0.675 & 0.940 & $n{=}1000$ \\\\\nQwen-2.5-7B & 0.080 & 0.715 & 0.925 & $n{=}1000$ \\\\\nGemma-2-9B & 0.100 & 0.705 & 0.945 & $n{=}1000$ \\\\\nMistral-7B & 0.070 & 0.760 & 0.945 & $n{=}1000$ \\\\\n\\midrule\n\\textit{Average} & --- & \\textit{0.714} & \\textit{0.939} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Gemma boundary case.}\nGemma-2-9B triggers the Proposition~\\ref{prop:debiasing_hurts} diagnostic in all four $K{=}4$ subgroups due to extreme FPR--FNR asymmetry (\\texttt{False\\_medium} FNR $= 0.437$).\nAt small budgets ($K{=}4$, $n{=}100$), EC-HTE RMSE reaches 1.229 ($3.1\\times$ naive), illustrating the budget guideline from Appendix~\\ref{sec:budget}: when per-subgroup cell counts fall below 25, the variance cost of stratified correction dominates.\nAt $n \\geq 500$, EC-HTE coverage recovers to $>$0.90, consistent with the synthetic experiments.\n\n\\paragraph{Heterogeneous-$\\tau$ DGP.}\nTo assess whether the constant-$\\tau$ DGP understates EC-HTE's advantage, we run a supplementary experiment using Llama's empirical confusion matrices with heterogeneous treatment effects across subgroups ($\\Delta\\tau \\in [0.1, 0.6]$, $K{=}2$, 50 MC runs).\nEC-HTE achieves lower $|\\text{bias}|$ than global correction at all budgets ($n{=}500$: 0.010 vs.\\ 0.031, a 68\\% reduction).\nIn the high-$\\Delta\\tau$ subgroup (\\texttt{True\\_short}, $\\Delta\\tau{=}0.6$), EC-HTE also achieves lower RMSE ($n{=}1{,}000$: 0.212 vs.\\ 0.258, 18\\% improvement), confirming that the RMSE advantage concentrates in subgroups where correction is most needed.\nAggregate RMSE remains comparable to global correction because low-$\\Delta\\tau$ subgroups incur stratification variance without commensurate bias reduction, consistent with the budget guidelines in Appendix~\\ref{sec:budget}.\n\n\\section{Robustness to Subgroup Misspecification}\n\\label{app:robustness}\n\nEC-HTE requires pre-defined subgroup labels, which may be noisy in practice.\nWe test robustness by randomly flipping each observation's subgroup assignment with probability $p_{\\text{flip}} \\in \\{0, 0.10, 0.25, 0.50\\}$, across $K \\in \\{2, 4\\}$ (extreme regime, $n_{\\text{expert}} = 500$, $\\Delta\\tau = 0.3$, 100 MC runs).\n\n\\begin{table}[t]\n\\centering\n\\caption{95\\% CI coverage under subgroup misspecification noise. EC-HTE maintains near-nominal coverage across all noise levels.}\n\\label{tab:robustness}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{4}{c}{$p_{\\text{flip}}$} \\\\\n\\cmidrule(lr){2-5}\nMethod & 0.00 & 0.10 & 0.25 & 0.50 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{$K{=}2$, extreme}} \\\\\n\\quad Naive & 0.875 & 0.877 & 0.890 & 0.897 \\\\\n\\quad Global & 0.925 & 0.935 & 0.932 & 0.945 \\\\\n\\quad HB EC-HTE & 0.958 & 0.948 & 0.950 & 0.945 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{$K{=}4$, extreme}} \\\\\n\\quad Naive & 0.904 & 0.916 & 0.909 & 0.919 \\\\\n\\quad Global & 0.930 & 0.953 & 0.948 & 0.944 \\\\\n\\quad HB EC-HTE & 0.956 & 0.958 & 0.960 & 0.946 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE maintains coverage $\\geq 0.945$ across all configurations (Table~\\ref{tab:robustness}), while the naive estimator is systematically below nominal (0.875--0.919).\nAt $p_{\\text{flip}} = 0.50$, subgroup structure is effectively destroyed; EC-HTE converges to global correction (coverage and RMSE within 0.1\\%), confirming that hierarchical Bayesian shrinkage provides a built-in safety mechanism.\nFor $K{=}4$ at $p_{\\text{flip}} = 0.50$, a small residual RMSE gap persists ($p < 0.01$), reflecting the variance cost of estimating four confusion matrices even when they carry no signal.\n\n\\section{Monte Carlo Standard Errors}\n\\label{app:mcse}\n\nAll experiments use 100 independent Monte Carlo replications per configuration.\nAll simulation results were verified with 100 MC seeds; the median RMSE variation between 50-seed and 100-seed estimates is below 3.2\\%, confirming the stability of reported figures.\nWe report Monte Carlo standard errors to assess whether observed differences between methods are statistically reliable.\nFor exp-001 (synthetic DGP, no per-seed pairing across methods), we use conservative two-sample $z$-tests on the 100-run means.\nFor exp-003 (semi-synthetic TweetEval, shared seeds across methods), we use paired $t$-tests, which are more powerful because they control for seed-level variation.\n\nTable~\\ref{tab:mcse} reports paired comparisons for representative configurations.\nOf 1{,}020 total pairwise comparisons across all configurations, 742 (72.7\\%) are statistically significant at $\\alpha = 0.05$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Paired comparisons for representative configurations. $\\Delta$ = method A $-$ method B (negative favors A for $|\\text{bias}|$). Two-sample $z$-tests for synthetic (exp-001); paired $t$-tests for semi-synthetic (exp-003). Bold $p$-values indicate significance at $\\alpha = 0.05$.}\n\\label{tab:mcse}\n\\small\n\\begin{tabular}{llrr}\n\\toprule\nConfiguration & Comparison & $\\Delta$ & $p$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{HB EC-HTE vs.\\ Global ($|\\text{bias}|$)}} \\\\\n\\quad $K{=}2$/ext/$n{=}500$ & & $-0.046$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/ext/$n{=}500$ & & $-0.078$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/mod/$n{=}250$ & & $-0.017$ & $0.288$ \\\\\n\\quad TweetEval/ext/$n{=}250$ & & $+0.001$ & $0.395$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{HB EC-HTE vs.\\ Global (RMSE)}} \\\\\n\\quad $K{=}2$/ext/$n{=}500$ & & $+0.015$ & $0.179$ \\\\\n\\quad $K{=}4$/ext/$n{=}500$ & & $+0.048$ & $\\mathbf{0.011}$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{HB EC-HTE vs.\\ Naive ($|\\text{bias}|$)}} \\\\\n\\quad $K{=}2$/ext/$n{=}500$ & & $-0.089$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/ext/$n{=}500$ & & $-0.113$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/mod/$n{=}250$ & & $-0.031$ & $\\mathbf{0.038}$ \\\\\n\\quad TweetEval/ext/$n{=}250$ & & $+0.005$ & $\\mathbf{0.030}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder extreme heterogeneity, HB EC-HTE's bias advantage over global correction is highly significant ($p < 0.001$ for both $K{=}2$ and $K{=}4$).\nThe RMSE penalty of stratification is not significant at $K{=}2$ ($p = 0.179$) but reaches significance at $K{=}4$ ($p = 0.011$), consistent with the higher variance cost of estimating four confusion matrices.\nUnder moderate heterogeneity ($K{=}4$, $n{=}250$), the bias difference between HB and global is not significant ($p = 0.288$), confirming that EC-HTE's advantage requires sufficient error heterogeneity.\nIn the semi-synthetic TweetEval experiment, HB EC-HTE does not significantly improve over global ($p = 0.395$), consistent with moderate $\\Delta\\pi$ and unbalanced subgroup sizes.\nThe HB vs.\\ naive comparison in TweetEval is significant ($p = 0.030$) but favors naive, reflecting the variance cost of stratification when bias reduction is marginal.\n\n\\section{Semi-Real Confusion Matrix Validation}\n\\label{app:semireal}\n\nWe test EC-HTE with empirical asymmetric confusion matrices from the GPT-4.1 TweetEval pilot.\nFour text-feature subgroups ($K{=}4$) retain the real per-subgroup FPR and FNR from pilot annotations (Table~\\ref{tab:semireal_cm}); CATE heterogeneity is injected synthetically ($\\tau(z{=}0,s) = 0.3 + 0.1s$, $\\tau(z{=}1,s) = 0.8 - 0.15s$).\n$N{=}5{,}000$, $P(Z{=}1){=}0.18$, 100 MC seeds per $n_{\\text{expert}}$ level.\n\n\\begin{table}[t]\n\\centering\n\\caption{Empirical confusion matrices from GPT-4.1 TweetEval pilot.\nS0 exhibits FNR $= 0.526$, approaching chance-level classification.}\n\\label{tab:semireal_cm}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSubgroup & Weight & FPR & FNR & $\\kappa(\\hat{C}_s)$ \\\\\n\\midrule\nS0 & 0.38 & 0.054 & 0.526 & high \\\\\nS1 & 0.22 & 0.101 & 0.300 & moderate \\\\\nS2 & 0.14 & 0.143 & 0.308 & moderate \\\\\nS3 & 0.25 & 0.194 & 0.222 & low \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Semi-real confusion matrix results. RMSE and coverage averaged over subgroups and $z$-levels (100 MC runs). HB EC-HTE underperforms global at all budgets; S0's near-chance FNR drives the failure.}\n\\label{tab:semireal}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n$n_{\\text{expert}}$ & Method & RMSE $\\downarrow$ & Coverage $\\uparrow$ \\\\\n\\midrule\n\\multirow{4}{*}{100}\n & Oracle & 0.101 & 0.957 \\\\\n & Naive & 0.123 & 0.879 \\\\\n & Global & 0.263 & 0.885 \\\\\n & HB EC-HTE & 0.784 & 0.744 \\\\\n\\midrule\n\\multirow{4}{*}{250}\n & Oracle & 0.101 & 0.957 \\\\\n & Naive & 0.123 & 0.879 \\\\\n & Global & 0.232 & 0.909 \\\\\n & HB EC-HTE & 0.411 & 0.834 \\\\\n\\midrule\n\\multirow{4}{*}{500}\n & Oracle & 0.101 & 0.957 \\\\\n & Naive & 0.123 & 0.879 \\\\\n & Global & 0.196 & 0.922 \\\\\n & HB EC-HTE & 0.260 & 0.890 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHB EC-HTE produces higher RMSE and lower coverage than global correction at all expert budgets (Table~\\ref{tab:semireal}).\nThe root cause is S0's FNR $= 0.526$: when a confusion matrix row approaches a uniform distribution ($P(\\hat{Z}{=}1 \\mid Z{=}1) \\approx 0.5$), inversion amplifies estimation noise regardless of the expert budget.\nThis converges with the hate speech case study (Appendix~\\ref{app:hatespeech}, FNR $= 53.3$\\%) and confirms that EC-HTE requires \\emph{both} sufficient expert labels \\emph{and} sufficient baseline classifier quality per subgroup.\nThe singularity guard ($\\kappa > 100$, Section~\\ref{sec:method}) mitigates catastrophic failure by falling back to global correction for near-degenerate subgroups, but does not recover the bias reduction that motivates stratification.\nFor a $2 \\times 2$ symmetric confusion matrix, $\\kappa = 1/|1-2\\pi|$; $\\kappa > 100$ corresponds to $\\pi \\in (0.495, 0.505)$, so the guard triggers only when the classifier performs within $0.5\\%$ of random guessing.\nAt $n_{\\text{expert}} = 500$, HB EC-HTE narrows the gap (RMSE 0.260 vs.\\ 0.196) as confusion matrix estimates stabilize for the three well-classified subgroups, but the S0 bottleneck persists.\n\nA second semi-real experiment using GPT-3.5-Turbo confusion matrices (worst-subgroup FPR $= 0.39$, FNR $= 0.21$) yields similar results: HB RMSE exceeds global by 1.3--3.5$\\times$ at all budgets.\nHere the failure stems from high false-positive rates compounded by class imbalance ($P(Z{=}1) = 0.18$), which leaves insufficient expert observations in the positive class for reliable per-subgroup confusion matrix estimation.\nTogether, these experiments identify three applicability conditions for EC-HTE: (1)~sufficient effective expert budget ($n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$), (2)~no near-chance subgroup error rate ($\\max(\\text{FPR}_s, \\text{FNR}_s) < 0.5$), and (3)~adequate class balance in the effect modifier.\n\n\\paragraph{Diagnostic rule.}\nA logistic regression over all 368 semi-real experiment--budget cells (dependent variable: HB EC-HTE $<$ Global RMSE) identifies two sufficient statistics: the worst-subgroup confusion matrix condition number $\\kappa(\\hat{M}_s) \\leq 1.25$ and the effective minority-class expert count $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$.\nWhen both conditions hold, HB outperforms global in 93.3\\% of cells; when either is violated, global is preferred in 94.7\\% of cells.\nBoth exp-015 ($\\kappa = 2.38$, effective $n = 2.5$) and exp-016 ($\\kappa = 1.55$, effective $n = 2.5$) violate both conditions, and the diagnostic correctly predicts 100\\% of their failure cells.\nSubgroup-average metrics can mask cell-level heterogeneity: in exp-015, HB EC-HTE substantially reduces bias for the three well-classified subgroups (S1--S3) but amplifies variance in the near-degenerate subgroup (S0, FNR $= 0.526$), and the S0 penalty dominates the aggregate RMSE.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/applicability_frontier.pdf}\n\\caption{Applicability frontier of EC-HTE. Green region: EC-HTE reduces bias vs.\\ global correction. Yellow: comparable performance. Red: EC-HTE underperforms. Dashed lines mark the expert budget threshold ($n_{\\text{expert}}/K = 25$) and classifier quality threshold (worst-subgroup error rate $= 0.5$). Red diamonds show semi-real experiments with actual GPT-4.1 and GPT-3.5-Turbo confusion matrices.}\n\\label{fig:applicability}\n\\end{figure}\n\n\\section{Robustness: Estimator Choice and Treatment Effect Specification}\n\\label{app:rlearner}\n\nWe verify that EC-HTE's corrected pseudo-outcomes are compatible with downstream estimators beyond CausalForest by replacing it with the R-learner~\\citep{nie2021quasi}.\nThe experiment uses $K{=}2$, extreme heterogeneity, $n_{\\text{expert}} = 500$, and 50 MC seeds; the R-learner uses 5-fold cross-fitting with gradient-boosted trees as the base learner.\n\n\\begin{table}[t]\n\\centering\n\\caption{R-learner vs.\\ CausalForest with EC-HTE correction ($K{=}2$, extreme, $n{=}500$). $|\\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and seeds.}\n\\label{tab:rlearner}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nEstimator & Correction & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\n\\multirow{4}{*}{R-learner}\n & Oracle & 0.006 & 0.056 & 0.94 \\\\\n & Naive & 0.121 & 0.139 & 0.47 \\\\\n & Global & 0.098 & 0.123 & 0.72 \\\\\n & EC-HTE & \\textbf{0.013} & 0.080 & 0.92 \\\\\n\\midrule\n\\multirow{2}{*}{CausalForest}\n & Naive & 0.058 & 0.090 & 0.82 \\\\\n & EC-HTE & \\textbf{0.010} & 0.093 & 0.95 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE reduces R-learner $|\\text{bias}|$ by 89\\% (0.121 $\\to$ 0.013) and restores coverage from 0.47 to 0.92 (Table~\\ref{tab:rlearner}).\nThe bias reduction and coverage gains are comparable to those achieved with CausalForest, confirming that EC-HTE is compatible with a range of HTE estimators.\n\n\\paragraph{Multiplicative treatment effects.}\nWe further test robustness to the functional form of treatment effects by replacing the additive DGP with a multiplicative specification: $Y(1) = Y(0) \\times \\exp(\\tau(Z))$, using $K{=}2$, extreme heterogeneity, $n_{\\text{expert}} = 500$, and 50 MC seeds.\n\n\\begin{table}[t]\n\\centering\n\\caption{Multiplicative DGP results ($K{=}2$, extreme, $n{=}500$, 50 seeds). EC-HTE achieves comparable bias reduction and nominal coverage under non-additive treatment effects.}\n\\label{tab:multiplicative}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\nOracle & 0.003 & 0.038 & 0.96 \\\\\nNaive & 0.135 & 0.142 & 0.44 \\\\\nGlobal & 0.110 & 0.124 & 0.54 \\\\\nEC-HTE & \\textbf{0.054} & 0.068 & 0.955 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE reduces RMSE by 52\\% relative to naive (0.068 vs.\\ 0.142) and restores coverage to the nominal level (0.955; Table~\\ref{tab:multiplicative}).\nEC-HTE's bias correction operates at the confusion matrix level, independent of the downstream CATE estimator and functional form of treatment effects.\n\n\\section{Robustness to Class Imbalance}\n\\label{app:classimbalance}\n\nAssumption (A3) requires $P(Z{=}1) = 0.5$, but real-world effect modifiers are often imbalanced.\nWe sweep $P(Z{=}1) \\in \\{0.1, 0.2, 0.3, 0.4, 0.5\\}$ with $K \\in \\{2,4\\}$, extreme misclassification heterogeneity, $n_{\\text{expert}}{=}250$, and 100 MC seeds (Table~\\ref{tab:pz1_sweep}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Robustness to class imbalance ($n_{\\text{expert}}{=}250$, extreme heterogeneity). R$^2$: Theorem~\\ref{thm:bias_identity} fit. Ratio: HB/Global RMSE ($<1$ = HB wins). Cov.: HB EC-HTE 95\\% CI coverage.}\n\\label{tab:pz1_sweep}\n\\small\n\\begin{tabular}{cc ccc}\n\\toprule\n$P(Z{=}1)$ & $K$ & R$^2$ & Ratio & Cov. \\\\\n\\midrule\n0.1 & 2 & 0.998 & 0.92 & 0.94 \\\\\n0.2 & 2 & 0.989 & 0.76 & 0.94 \\\\\n0.3 & 2 & 0.994 & 0.78 & 0.94 \\\\\n0.4 & 2 & 0.995 & 0.87 & 0.94 \\\\\n0.5 & 2 & 0.995 & 0.86 & 0.93 \\\\\n\\midrule\n0.1 & 4 & 0.984 & 1.54 & 0.92 \\\\\n0.2 & 4 & 0.976 & 1.68 & 0.93 \\\\\n0.3 & 4 & 0.985 & 1.12 & 0.92 \\\\\n0.4 & 4 & 0.984 & 1.08 & 0.93 \\\\\n0.5 & 4 & 0.992 & 1.06 & 0.92 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTheorem~\\ref{thm:bias_identity}'s product form remains accurate across all imbalance levels: $R^2 \\geq 0.976$ even at $P(Z{=}1) = 0.1$, confirming that the bias identity derives from confusion matrix structure rather than class balance.\nFor $K{=}2$, EC-HTE outperforms global correction at all $P(Z{=}1)$ levels (RMSE ratio 0.76--0.92), degrading gracefully under severe imbalance.\nFor $K{=}4$, EC-HTE underperforms global at $n_{\\text{expert}}{=}250$ (ratio 1.06--1.68), consistent with the budget threshold $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$: at $P(Z{=}1){=}0.1$, $K{=}4$, each subgroup receives only ${\\sim}6$ minority-class labels.\nThe gap narrows as $P(Z{=}1)$ increases (1.54 $\\to$ 1.06), and coverage remains stable at 0.92--0.94 across all configurations.\n\n\\section{Comparison with PPI Correction}\n\\label{app:ppi_comparison}\n\nPPI~\\cite{angelopoulos2023ppi} constructs confidence intervals by combining a large set of ML predictions with a smaller set of gold-standard labels, using the gold labels to debias the ML-based estimator.\nApplied to our setting, PPI treats the LLM-annotated effect modifier as the ML prediction and the expert labels as the gold standard.\nTwo variants arise naturally: \\emph{PPI-global} pools all expert labels to estimate a single rectifier (analogous to our Global baseline), and \\emph{PPI-subgroup} estimates per-subgroup rectifiers (analogous to Stratified MLE).\n\nUnder the confusion-matrix parameterization we adopt, DSL's measurement error correction reduces to confusion matrix inversion.\nPooled DSL applies a single estimated confusion matrix to all subgroups, producing the same corrected label distribution as our Global baseline; per-subgroup DSL estimates a separate confusion matrix for each subgroup and inverts it independently, equivalent to our Stratified MLE.\nEC-HTE's contribution over both PPI-subgroup and per-subgroup DSL is hierarchical partial pooling: rather than estimating each subgroup's confusion matrix in isolation, EC-HTE places a shared prior across subgroups, borrowing strength to reduce variance while preserving subgroup-specific bias correction.\nThis mechanism is outside both the PPI and DSL frameworks.\n\nThe key difference between PPI and confusion-matrix inversion is that PPI does not invert the confusion matrix; instead, it uses the gold labels to directly debias the estimand.\nThis avoids the matrix inversion step that can amplify noise at small $n_{\\text{expert}}$, but it also means PPI cannot exploit the structure of the misclassification process to reduce bias.\nPPI-global inherits the same $\\Delta\\pi \\times \\Delta\\tau$ bias amplification as Global correction (Theorem~\\ref{thm:bias_identity}), confirming that the ``debiasing hurts'' mechanism operates regardless of the inference framework.\n\n\\section{Civil Comments Validation}\n\\label{app:civilcomments}\n\nTo verify that subgroup-heterogeneous misclassification generalizes beyond TweetEval, we annotate $N{=}3{,}000$ stratified samples (30\\% toxic) from Civil Comments~\\cite{borkan2019nuanced}, a toxicity detection dataset.\nSubgroups are defined by \\texttt{text\\_length\\_bin} $\\times$ \\texttt{has\\_question} ($K{=}4$): S0 (long, no question, 38.8\\%), S1 (long, question, 11.4\\%), S2 (short, no question, 33.7\\%), S3 (short, question, 16.1\\%).\nSubgroup features were chosen a priori based on observable text properties; no feature search was performed.\nThree proprietary LLMs annotate each sample via an OpenAI-compatible API, yielding 800--900 valid annotations per model.\n\nTable~\\ref{tab:civil_cm} reports per-subgroup FPR and FNR.\nWe define $\\Delta\\pi = \\max_s \\pi_s - \\min_s \\pi_s$, where $\\pi_s$ is the overall misclassification rate for subgroup $s$.\nAll three models exhibit $\\Delta\\pi > 0.05$, with overall heterogeneity $\\Delta\\pi \\in [0.113, 0.160]$---comparable to the $\\Delta\\pi \\in [0.125, 0.165]$ observed across four open-source LLMs on TweetEval (Appendix~\\ref{app:multilm_opensource}).\nGPT-4o-mini and GPT-3.5-turbo show pronounced FPR/FNR asymmetry (e.g., GPT-4o-mini FPR $\\in [0.42, 0.61]$ vs.\\ FNR $\\in [0.05, 0.16]$), indicating systematic over-prediction of toxicity; their FPR approaches 0.5, placing them in the ill-conditioned regime where confusion matrix inversion amplifies noise (consistent with the classifier quality threshold discussed in the Limitations section).\nThe consistent presence of $\\Delta\\pi$ heterogeneity across two NLP tasks, seven LLMs spanning open-source (7B--9B) and proprietary families, and two distinct subgroup definitions confirms that this phenomenon is a structural property of LLM annotation rather than an artifact of a specific dataset or model.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-subgroup misclassification rates on Civil Comments ($K{=}4$). $\\Delta$ denotes max $-$ min across subgroups.}\n\\label{tab:civil_cm}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Metric & S0 & S1 & S2 & S3 & $\\Delta$ \\\\\n\\midrule\nGPT-4o & FPR & 0.249 & 0.157 & 0.213 & 0.341 & 0.184 \\\\\n       & FNR & 0.160 & 0.263 & 0.308 & 0.328 & 0.168 \\\\\n\\midrule\nGPT-4o-mini & FPR & 0.517 & 0.541 & 0.419 & 0.610 & 0.191 \\\\\n            & FNR & 0.052 & 0.105 & 0.074 & 0.160 & 0.108 \\\\\n\\midrule\nGPT-3.5-turbo & FPR & 0.400 & 0.473 & 0.374 & 0.468 & 0.099 \\\\\n              & FNR & 0.139 & 0.211 & 0.173 & 0.240 & 0.101 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Bias Identity Validation with Real Confusion Matrices}\n\\label{app:realcm_bias}\n\nTheorem~\\ref{thm:bias_identity} is derived under symmetric misclassification (A2); real LLM confusion matrices are asymmetric (FPR $\\neq$ FNR).\nWe verify that the generalized identity $\\mathrm{bias}(z,s) = \\Delta\\tau \\cdot [B_s]_{z,1}$ (Remark~\\ref{thm:bias_identity}) holds under real annotation error structures by running semi-synthetic simulations ($N{=}5{,}000$, $K{=}4$, $\\Delta\\tau{=}0.30$, 100 MC runs) with confusion matrices drawn from 11 LLM--dataset combinations: eight models on TweetEval (GPT-4-turbo, GPT-4o, GPT-4.1, GPT-4o-mini, GPT-3.5-turbo, Qwen2.5-7B, Mistral-7B, Gemma-2-9B) and three on Civil Comments (GPT-4o, GPT-4o-mini, GPT-3.5-turbo).\n\nTable~\\ref{tab:realcm_r2} reports per-model $R^2$ from regressing observed subgroup bias on the predicted value $\\Delta\\tau \\cdot [B_s]_{z,1}$.\nThe aggregate $R^2 = 0.975$; 10 of 11 combinations achieve $R^2 \\geq 0.93$.\nThe single outlier (GPT-4o-mini on Civil Comments, $R^2{=}0.76$) has near-homogeneous subgroup error rates ($\\max|[B_s]_{z,1}| = 0.089$), so predicted biases are small and Monte Carlo noise dominates the regression.\n$R^2$ correlates strongly with $\\max|[B_s]_{z,1}|$: models with more heterogeneous per-subgroup error rates produce larger bias signals that are easier to verify empirically.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bias identity $R^2$ with real LLM confusion matrices ($K{=}4$, 100 MC runs).}\n\\label{tab:realcm_r2}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nModel & Dataset & $R^2$ & $\\max|[B_s]_{z,1}|$ \\\\\n\\midrule\nGPT-4-turbo  & TweetEval & 0.993 & 0.328 \\\\\nQwen2.5-7B   & TweetEval & 0.990 & 0.272 \\\\\nMistral-7B   & TweetEval & 0.990 & 0.242 \\\\\nGemma-2-9B   & TweetEval & 0.982 & 0.185 \\\\\nGPT-4o       & Civil Comments & 0.979 & 0.198 \\\\\nGPT-4o       & TweetEval & 0.975 & 0.240 \\\\\nGPT-4.1      & TweetEval & 0.969 & 0.139 \\\\\nGPT-3.5-turbo & TweetEval & 0.948 & 0.087 \\\\\nGPT-3.5-turbo & Civil Comments & 0.935 & 0.170 \\\\\nGPT-4o-mini  & TweetEval & 0.929 & 0.170 \\\\\nGPT-4o-mini  & Civil Comments & 0.756 & 0.089 \\\\\n\\midrule\n\\multicolumn{2}{l}{All (pooled)} & 0.975 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Applicability Screening with Real LLM Confusion Matrices}\n\\label{app:screening}\n\nWe apply the diagnostic conditions from Proposition~\\ref{prop:debiasing_hurts} and Section~\\ref{sec:method} to 16 LLM--dataset--$K$ combinations spanning seven LLMs (four open-source, three proprietary) across TweetEval and Civil Comments.\nTable~\\ref{tab:screening} summarizes which conditions each combination satisfies.\n\n\\begin{table}[h]\n\\centering\n\\caption{Diagnostic screening of 16 LLM--dataset--$K$ combinations. Columns report whether all subgroups satisfy each condition. Budget assumes $n_{\\text{expert}}{=}500$.}\n\\label{tab:screening}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Dataset & $K$ & $\\kappa{\\leq}1.25$ & $\\max{\\leq}0.5$ & Budget & Pass all \\\\\n\\midrule\nGemma-2-9B   & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nLlama-3.1-8B & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nMistral-7B   & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nQwen2.5-7B   & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGemma-2-9B   & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nLlama-3.1-8B & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nMistral-7B   & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nQwen2.5-7B   & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-3.5-turbo & CivilComm. & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-3.5-turbo & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4-turbo  & TweetEval & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4.1      & TweetEval & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o       & CivilComm. & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o       & TweetEval & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o-mini  & CivilComm. & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o-mini  & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nNo combination passes all three conditions; the bottleneck is $\\kappa(C_s) \\leq 1.25$, which requires $\\mathrm{FPR}_s + \\mathrm{FNR}_s \\lesssim 0.20$ for all subgroups---a threshold no current LLM achieves uniformly.\nThe closest are Qwen2.5-7B True\\_short ($\\kappa{=}1.23$) and Mistral-7B True\\_short ($\\kappa{=}1.27$).\n\nUnder a relaxed ``oracle screening'' that excludes near-degenerate subgroups ($\\max(\\mathrm{FPR}_s, \\mathrm{FNR}_s) \\geq 0.4$), we run semi-synthetic CATE estimation ($N{=}5{,}000$, $\\Delta\\tau{=}0.3$, 100 MC runs, $n_{\\text{expert}} \\in \\{250, 500\\}$) with each LLM's real per-subgroup confusion matrix.\nEC-HTE (HB) achieves lower RMSE than global correction in 41 of 52 comparisons (79\\%) and lower RMSE than stratified MLE in 52 of 52 comparisons (100\\%).\nThe four open-source LLMs on TweetEval show the strongest EC-HTE advantage (32/32 comparisons, RMSE reduction 0.001--0.008), while GPT-3.5-turbo/TweetEval (high FPR asymmetry, $\\mathrm{FPR}_{\\max}{=}0.39$) and GPT-4o/Civil Comments (low minority prevalence $P(Z{=}1){=}0.3$) show degradation.\nThe diagnostic correctly identifies the strict applicability regime; under relaxed conditions excluding near-degenerate subgroups, EC-HTE improves RMSE in 79\\% of comparisons.\n\n\\paragraph{Diagnostic Applicability Analysis.}\nThe diagnostic (Proposition~\\ref{prop:debiasing_hurts}) degrades on real LLM confusion matrices (pooled AUC $= 0.63$) because the failure mode is systematic: subgroups where the true CATE heterogeneity $\\tau_s \\approx 0$ are hurt by global correction (since $\\delta_s \\neq 0$ still introduces bias), yet these subgroups produce low diagnostic scores---the diagnostic ranks them as safe precisely when they are most vulnerable to overcorrection.\n\nA simple meta-criterion recovers reliability: compute $\\max_s |\\delta_s| / ((1 - 2\\bar{\\pi}) \\cdot \\pi_s)$ across subgroups.\nWhen $\\max_s \\mathrm{score}(s) > 1$, at least one subgroup is definitively harmed by global correction, and the diagnostic achieves AUC $\\geq 0.75$ across all 5 model--dataset combinations satisfying this condition (AUC range: 0.75--1.0).\nWhen $\\max_s \\mathrm{score}(s) \\leq 1$, global correction may or may not hurt depending on unobservable $\\Delta\\tau$; the diagnostic achieves AUC only 0.0--0.67 across the remaining 7 combinations (4 of 7 have AUC $< 0.5$, indicating anti-prediction).\nThis threshold perfectly separates reliable from unreliable diagnostic regimes across all 16 real LLM--dataset combinations evaluated.\n\nWe recommend the following practical protocol: (i) estimate per-subgroup confusion matrices from expert labels; (ii) compute $\\max_s \\mathrm{score}(s)$; (iii) if $> 1$, the diagnostic reliably identifies which subgroups are harmed by global correction---apply EC-HTE; (iv) if $\\leq 1$, the diagnostic is unreliable and practitioners should either default to EC-HTE as a conservative choice or evaluate correction strategies using held-out expert labels.\n\n\\section{Plug-in Standard Error Validation}\n\\label{app:bootstrap_se}\n\nA natural concern is whether the plug-in standard error adequately captures estimation uncertainty, particularly the additional variance introduced by confusion matrix estimation.\nWe verify this for the difference-in-means (DIM) estimator via Monte Carlo simulation ($K{=}2$, $n_{\\text{expert}} \\in \\{50, 100, 250, 500\\}$, 50 replications per budget level).\nAt each budget, we compute the plug-in 95\\% confidence interval and record empirical coverage.\nAcross all expert budgets, the plug-in SE yields coverage $\\geq 0.96$ (0.970, 0.960, 0.970, 0.970 for $n_{\\text{expert}} = 50, 100, 250, 500$), confirming that the analytic variance estimate is well-calibrated for the DIM estimator.\nThis self-calibration arises because the same noise in $\\hat{M}^{-1}$ that inflates point-estimate variance also inflates the plug-in SE, producing conservative intervals that maintain nominal coverage.\n\n\\paragraph{CausalForestDML.}\nUnder $K{=}2$ extreme heterogeneity ($\\pi{=}[0.05, 0.25]$, $n_{\\text{expert}}{=}250$, $n_{\\text{estimators}}{=}200$, 20 MC runs), EC-HTE plug-in SE achieves 93.8\\% aggregate coverage---close to the 94--96\\% oracle coverage (Table~\\ref{tab:cf_oracle}).\nThe high-error subgroup ($s_1$, $\\pi{=}0.25$) shows slightly lower plug-in coverage (92.5\\%) than the low-error subgroup ($s_0$: 95.0\\%), reflecting the larger $M^{-1}$ amplification of estimation uncertainty in subgroups with higher misclassification rates.\nBy contrast, the DIM plug-in SE achieves $\\geq$95\\% coverage in the same DGP, confirming that the analytic confusion matrix propagation formula is adequate for simpler estimators.\n\n\\paragraph{Full bootstrap SE.}\nA \\emph{full} bootstrap---resampling all $N$ observations and re-estimating both the confusion matrix and CausalForest per bootstrap replicate ($B{=}100$, $n_{\\text{estimators}}{=}200$, 20 MC runs)---confirms that plug-in SE is already near-nominal under standard hyperparameters.\nUnder $K{=}2$ extreme heterogeneity ($\\pi{=}[0.05, 0.25]$, $n_{\\text{expert}}{=}250$), plug-in SE achieves 93.8\\% aggregate coverage; the full bootstrap improves this to exactly 95.0\\% ($+$1.2pp).\nTable~\\ref{tab:bootstrap_se} reports per-subgroup results.\n\n\\begin{table}[h]\n\\centering\n\\caption{CausalForest coverage: plug-in SE vs.\\ full bootstrap SE ($B{=}100$, $n_{\\text{estimators}}{=}200$, 20 MC runs). Bootstrap SE is ${\\sim}1.15\\times$ plug-in.}\n\\label{tab:bootstrap_se}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nSubgroup & Plugin Cov. & Boot.\\ Cov. & Oracle Cov. & Plugin SE & Boot.\\ SE \\\\\n\\midrule\n$s_0$ ($\\pi{=}0.05$) & 0.950 & 0.925 & 0.925 & 0.059 & 0.063 \\\\\n$s_1$ ($\\pi{=}0.25$) & 0.925 & \\textbf{0.975} & 0.875 & 0.087 & 0.103 \\\\\n\\midrule\nAggregate & 0.938 & \\textbf{0.950} & 0.900 & 0.073 & 0.083 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe high-error subgroup ($s_1$) benefits most: coverage rises from 92.5\\% to 97.5\\% ($+$5.0pp), because the bootstrap captures the additional variance from $M^{-1}$ amplification.\nOracle coverage (90.0\\%) is consistent with the 94\\% reported in the oracle decomposition (Table~\\ref{tab:cf_oracle}), with the difference attributable to MC sampling noise at 20 runs.\nThe computational cost is substantial ($B \\times$ CF fits per MC run), but the approach is straightforward when exact nominal coverage is required.\n\n\\paragraph{Finite-sample remainder.}\nBy first-order matrix perturbation, $\\hat{C}_s^{-1} = C_s^{-1} - C_s^{-1} E_s C_s^{-1} + O(\\|E_s\\|^2)$, where $E_s = \\hat{C}_s - C_s$ satisfies $\\|E_s\\| = O_p(n_{\\text{expert}}^{-1/2})$.\nThe remainder in the corrected CATE is therefore $R_n = O_p(n_{\\text{expert}}^{-1/2} \\cdot \\|C_s^{-1}\\|^2) = O_p(n_{\\text{expert}}^{-1/2} \\cdot \\kappa(C_s))$, since $\\|C_s^{-1}\\| = O(\\kappa(C_s))$ for stochastic matrices.\nThis motivates the $\\kappa > 100$ singularity guard (Section~\\ref{sec:method}).\n\n\\subsection{CausalForest Oracle Coverage Decomposition}\n\\label{app:cf_oracle}\n\nTo isolate the source of CausalForest under-coverage, we compare six estimation strategies that progressively remove sources of uncertainty: (1)~Oracle (true $Z$, no correction), (2)~EC-HTE with true $C_s$, (3)~EC-HTE with estimated $\\hat{C}_s$ (HB), (4)~Global with true $\\bar{C}$, (5)~Global with estimated $\\hat{\\bar{C}}$, and (6)~Naive.\nTable~\\ref{tab:cf_oracle} reports coverage, $|\\text{bias}|$, and RMSE across three DGP configurations (100 MC runs each).\n\n\\begin{table}[h]\n\\centering\n\\caption{CausalForest oracle coverage decomposition. Coverage averaged over subgroups and $z$-levels.}\n\\label{tab:cf_oracle}\n\\small\n\\begin{tabular}{ll ccc}\n\\toprule\nDGP & Method & Cov.\\ (\\%) & $|\\text{Bias}|$ & RMSE \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{$K{=}4$, extreme\\\\$n{=}500$}}\n & Oracle (true $Z$)       & 94.5 & 0.006 & 0.078 \\\\\n & EC-HTE true $C_s$       & 92.5 & 0.008 & 0.114 \\\\\n & EC-HTE est.\\ $\\hat{C}_s$ & 93.1 & 0.015 & 0.121 \\\\\n & Global true $\\bar{C}$   & 91.3 & 0.037 & 0.110 \\\\\n & Global est.\\ $\\hat{\\bar{C}}$ & 91.1 & 0.038 & 0.111 \\\\\n & Naive                    & 88.3 & 0.045 & 0.095 \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{$K{=}2$, extreme\\\\$n{=}250$}}\n & Oracle (true $Z$)       & 94.0 & 0.002 & 0.056 \\\\\n & EC-HTE true $C_s$       & 94.0 & 0.003 & 0.073 \\\\\n & EC-HTE est.\\ $\\hat{C}_s$ & 92.5 & 0.004 & 0.079 \\\\\n & Global true $\\bar{C}$   & 88.5 & 0.045 & 0.083 \\\\\n & Global est.\\ $\\hat{\\bar{C}}$ & 88.3 & 0.045 & 0.085 \\\\\n & Naive                    & 82.8 & 0.046 & 0.077 \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{$K{=}2$, MF2 DGP\\\\$\\tau{=}(0.10,0.40)$}}\n & Oracle (true $Z$)       & 96.0 & 0.077 & 0.091 \\\\\n & EC-HTE true $C_s$       & 91.3 & 0.103 & 0.112 \\\\\n & EC-HTE est.\\ $\\hat{C}_s$ & 92.3 & 0.100 & 0.111 \\\\\n & Global true $\\bar{C}$   & 95.0 & 0.107 & 0.114 \\\\\n & Global est.\\ $\\hat{\\bar{C}}$ & 94.3 & 0.105 & 0.114 \\\\\n & Naive                    & 77.3 & 0.120 & 0.125 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree findings emerge.\nFirst, oracle coverage is 94--96\\% across all DGPs, confirming that CausalForest plug-in SE is well-calibrated when labels are correct.\nSecond, EC-HTE with true $C_s$ achieves 91--94\\% coverage---a 0--5pp gap from oracle (configuration-dependent), reflecting $M^{-1}$ SE propagation asymmetry across DGPs rather than confusion matrix estimation error.\nThird, the gap between true and estimated $C_s$ is ${\\leq}$1.5pp ($K{=}2$) and $<$1pp ($K{=}4$), confirming that CM estimation uncertainty contributes negligibly at $n_{\\text{expert}} \\geq 250$.\n\n\\section{Robustness to Assumption Violations}\n\\label{app:a5_violation}\n\n\\subsection{Assumption (A5): Subgroup-Specific Treatment Effects}\n\n\\begin{corollary}[Subgroup-Specific Treatment Effect Heterogeneity]\n\\label{cor:a5_relaxation}\nWhen $\\Delta\\tau$ varies across subgroups ($\\Delta\\tau_s = \\tau_s(1) - \\tau_s(0)$), the bias of global correction in subgroup $s$ at level $z{=}0$ is $+\\delta_s \\cdot \\Delta\\tau_s / (1 - 2\\bar{\\pi})$, and at level $z{=}1$ is $-\\delta_s \\cdot \\Delta\\tau_s / (1 - 2\\bar{\\pi})$.\n\\end{corollary}\nThe proof follows directly from Theorem~\\ref{thm:bias_identity} with $\\tau_s$ replacing $\\tau$.\n\nOur main analysis assumes that subgroup misclassification rates $\\delta_s$ and subgroup CATE magnitudes $\\Delta\\tau_s$ are independent (Assumption A5).\nIn practice, both may depend on text features that define subgroups, introducing correlation.\nWe test robustness under two configurations with the DIM estimator ($K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 50 MC replications, $\\pi = [0.05, 0.25]$):\n\\emph{aligned} (positive $\\delta_s$--$\\Delta\\tau_s$ correlation: high-error S1 has the larger treatment effect, $\\Delta\\tau = [0.30, 0.70]$) and\n\\emph{adversarial} (negative correlation: high-error S1 has the smaller effect, $\\Delta\\tau = [0.70, 0.30]$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Coverage and $|\\text{bias}|$ under A5 violation ($K{=}2$, $n_{\\text{expert}}{=}250$, 50 MC). Target coverage: 0.95.}\n\\label{tab:a5_violation}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nConfig & Method & S0 cov & S1 cov & S0 $|\\text{bias}|$ & S1 $|\\text{bias}|$ \\\\\n\\midrule\n\\multirow{4}{*}{Aligned}\n & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\\\\n & Naive         & 0.93 & 0.25 & 0.022 & 0.174 \\\\\n & Global        & 0.93 & 0.82 & 0.036 & 0.094 \\\\\n & EC-HTE (EB)   & 0.95 & 0.95 & 0.005 & 0.017 \\\\\n\\midrule\n\\multirow{4}{*}{Adversarial}\n & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\\\\n & Naive         & 0.90 & 0.78 & 0.042 & 0.074 \\\\\n & Global        & 0.74 & 0.93 & 0.098 & 0.040 \\\\\n & EC-HTE (EB)   & 0.94 & 0.96 & 0.002 & 0.007 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn the aligned configuration, the $\\delta_s \\times \\Delta\\tau_s$ product is maximized in the high-error subgroup, causing naive S1 coverage to collapse to 0.25.\nGlobal correction improves S1 but cannot fully correct without subgroup-specific error rates.\nIn the adversarial configuration, global correction overcorrects the low-error subgroup (S0 coverage 0.74).\nEC-HTE (EB) maintains $\\geq 0.94$ coverage across both subgroups in both configurations, with bias comparable to the oracle.\nResults at $n_{\\text{expert}}{=}500$ are consistent (all EC-HTE coverages $\\in [0.93, 0.99]$).\n\n\\subsection{Assumption (A1): Sensitivity to Outcome-Dependent Misclassification}\n\\label{app:a1_sensitivity}\n\nWe assess EC-HTE's robustness when misclassification depends on potential outcomes, violating~(A1).\nWe modify the synthetic DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$) so that misclassification probability becomes outcome-dependent: $P(\\hat{Z}{\\neq}Z \\mid Z, S, Y) = \\mathrm{clamp}(\\pi_s + \\gamma \\cdot (Y - \\mu_Y)/\\sigma_Y,\\, 0,\\, 1)$, where $\\gamma \\in \\{0, 0.05, 0.10, 0.15, 0.20\\}$ controls the strength of violation.\nTable~\\ref{tab:a1_sensitivity} reports results averaged over 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{Sensitivity to Assumption~(A1) violation. Coverage and $|\\text{bias}|$ under outcome-dependent misclassification ($\\gamma > 0$).}\n\\label{tab:a1_sensitivity}\n\\small\n\\begin{tabular}{lccc ccc}\n\\toprule\n& \\multicolumn{3}{c}{Coverage (\\%)} & \\multicolumn{3}{c}{$|\\text{Bias}|$} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n$\\gamma$ & EC-HTE & Global & Naive & EC-HTE & Global & Naive \\\\\n\\midrule\n0.00 & 95.5 & 92.7 & 87.7 & 0.060 & 0.065 & 0.061 \\\\\n0.05 & 95.5 & 93.5 & 83.8 & 0.059 & 0.064 & 0.064 \\\\\n0.10 & 95.3 & 93.8 & 83.5 & 0.063 & 0.064 & 0.067 \\\\\n0.15 & 94.8 & 94.3 & 79.2 & 0.065 & 0.064 & 0.070 \\\\\n0.20 & 93.5 & 94.0 & 79.5 & 0.068 & 0.063 & 0.073 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE maintains near-nominal coverage ($\\geq$93.5\\%) across the full $\\gamma$ range, with $|\\text{bias}|$ increasing only 13.7\\% from $\\gamma{=}0$ to $\\gamma{=}0.2$.\nAll correction methods (Global, Stratified MLE, HB) maintain $\\geq$90\\% coverage, indicating that moderate (A1) violations do not catastrophically degrade confusion-matrix-based correction.\nThe naive estimator degrades most rapidly (coverage $-$8.2pp), consistent with outcome-dependent misclassification compounding the uncorrected label noise.\n\n\\subsection{Extension to Confounded Treatment Assignment}\n\\label{app:confounded_dgp}\n\nEC-HTE's confusion matrix correction operates on estimated CATEs regardless of how those estimates are produced.\nTo verify compatibility with observational (non-RCT) designs, we pair EC-HTE with an inverse probability weighted difference-in-means (IPW-DIM) estimator under confounded treatment assignment.\n\n\\paragraph{DGP.}\n$N{=}5{,}000$, $K{=}2$, $\\pi = [0.05, 0.25]$, $n_{\\text{expert}}{=}250$, 100 MC replications.\nA covariate $X \\sim \\mathcal{N}(0,1)$ confounds both treatment and outcome:\n$T \\sim \\text{Bernoulli}(\\sigma(\\beta X))$ with $\\beta{=}0.5$ (moderate confounding; propensity range $[0.38, 0.62]$),\n$Y = 1 + 0.5 Z + 0.3 X + \\tau(Z) \\cdot T + \\varepsilon$, $\\varepsilon \\sim \\mathcal{N}(0,1)$.\nTreatment effects are $\\tau(Z{=}0){=}0$, $\\tau(Z{=}1){=}0.3$.\nThe IPW-DIM estimator uses \\emph{oracle propensity} $e(X) = \\sigma(\\beta X)$, with propensity scores clipped to $[0.05, 0.95]$.\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE under confounded treatment assignment (IPW-DIM with oracle propensity, $\\beta{=}0.5$, 100 MC).}\n\\label{tab:confounded_dgp}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Coverage & RMSE & $|\\text{Bias}|$ \\\\\n\\midrule\nOracle (true $Z$ + IPW) & 0.943 & 0.061 & 0.048 \\\\\nHB EC-HTE              & 0.950 & 0.086 & 0.068 \\\\\nGlobal                  & 0.930 & 0.087 & 0.071 \\\\\nStrat MLE               & 0.950 & 0.087 & 0.069 \\\\\nNaive                   & 0.863 & 0.083 & 0.066 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE achieves 95.0\\% coverage, within 0.7pp of the oracle (94.3\\%), confirming that confusion matrix correction and propensity weighting compose without interference.\nThe improvement is most pronounced in the high-error subgroup ($\\pi{=}0.25$): EC-HTE coverage is 96.0\\% vs.\\ naive 78.5\\% ($+$17.5pp).\nGlobal coverage (93.0\\%) falls below the correction methods (95.0\\%), consistent with the cost of ignoring subgroup-level error heterogeneity even in the confounded setting.\n\n\\paragraph{Sensitivity to confounding strength and propensity estimation.}\nWe sweep $\\beta \\in \\{0.25, 0.5, 1.0, 2.0\\}$ and compare oracle propensity ($e(X) = \\sigma(\\beta X)$) with estimated propensity (logistic regression fit on $(X, T)$), yielding 8 configurations (100 MC each).\nTable~\\ref{tab:confounded_sweep} reports HB EC-HTE and naive coverage.\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE coverage across confounding strengths and propensity sources. The logistic regression propensity model is correctly specified; propensity misspecification is an orthogonal concern addressed by the IPW literature.}\n\\label{tab:confounded_sweep}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n$\\beta$ & Propensity & HB Coverage & Naive Coverage \\\\\n\\midrule\n0.25 & Oracle    & 0.963 & 0.848 \\\\\n0.25 & Estimated & 0.973 & 0.845 \\\\\n0.50 & Oracle    & 0.950 & 0.863 \\\\\n0.50 & Estimated & 0.958 & 0.858 \\\\\n1.00 & Oracle    & 0.958 & 0.898 \\\\\n1.00 & Estimated & 0.960 & 0.883 \\\\\n2.00 & Oracle    & 0.945 & 0.858 \\\\\n2.00 & Estimated & 0.948 & 0.858 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE maintains coverage $\\geq$94.5\\% across all 8 configurations, including strong confounding ($\\beta{=}2.0$, propensity range $[0.12, 0.88]$).\nThe oracle--estimated gap is $\\leq$1pp, confirming that propensity estimation error does not meaningfully degrade EC-HTE when the propensity model is correctly specified.\nThis validates that EC-HTE is robust to confounded treatment assignment when the propensity model is correctly specified.\n\n\\subsection{Empirical Comparison with Frazis--Loewenstein Correction}\n\\label{app:fl_comparison}\n\nWe empirically compare EC-HTE's confusion matrix inversion against the scalar attenuation correction of \\citet{frazis2003estimating} (F-L).\nThe F-L correction rescales the observed estimate as $\\hat{\\tau}_{\\text{FL}} = \\hat{\\tau}_{\\text{obs}} / (1 - 2\\bar{\\pi})$, where $\\bar{\\pi}$ is the (global or per-subgroup) misclassification rate.\nWe test two variants: F-L \\emph{scalar} (single global $\\bar{\\pi}$) and F-L \\emph{per-subgroup} ($\\pi_s$-specific rescaling).\nSetup: $K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, $\\pi{=}[0.05, 0.25]$ (extreme heterogeneity), $\\tau(z{=}0){=}0$, $\\tau(z{=}1){=}0.3$, 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{F-L correction vs.\\ EC-HTE under heterogeneous misclassification ($\\Delta\\pi{=}0.20$). Both F-L variants produce \\emph{higher} aggregate bias than the uncorrected estimator.}\n\\label{tab:fl_comparison}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Coverage \\\\\n\\midrule\nOracle         & 0.045 & 0.056 & 0.943 \\\\\nNaive          & 0.062 & 0.077 & 0.858 \\\\\nGlobal (CM inv)& 0.064 & 0.081 & 0.938 \\\\\nHB EC-HTE      & 0.064 & 0.086 & \\textbf{0.953} \\\\\nF-L Scalar     & 0.091 & 0.116 & 0.850 \\\\\nF-L Per-Subgroup & 0.112 & 0.158 & 0.838 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth F-L variants produce \\emph{higher} bias and RMSE than the naive estimator (F-L per-subgroup $|\\text{bias}|{=}0.112$ vs.\\ naive $0.062$), demonstrating that scalar attenuation cannot substitute for confusion matrix inversion under subgroup-heterogeneous misclassification.\nThe per-subgroup bias direction reveals the mechanism: F-L scalar over-corrects the low-error subgroup ($s_0$: mean bias ${=}+0.073$ vs.\\ naive $+0.005$, a $14.6\\times$ amplification), while F-L per-subgroup dramatically over-corrects the high-error subgroup ($s_1$: mean bias ${=}+0.160$).\nEC-HTE achieves near-zero per-subgroup bias ($s_0{:}\\,{+}0.006$, $s_1{:}\\,{+}0.001$) with nominal coverage (95.3\\%).\nThe root cause is structural: F-L's $1/(1{-}2\\pi)$ scaling amplifies each $z$-level estimate independently, whereas CM inversion simultaneously redistributes the cross-contamination between misclassified and correctly classified observations.\n\n\\subsection{End-to-End Validation with Asymmetric Confusion Matrices}\n\\label{app:asymmetric_endtoend}\n\nWe validate EC-HTE under strongly asymmetric confusion matrices ($\\text{FPR}/\\text{FNR}$ ratio up to $7{:}1$), simulating the error profile of GPT-4.1 on Civil Comments.\nSetup: $K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$; $s_0$: $\\text{FPR}{=}0.05$, $\\text{FNR}{=}0.02$ (low error); $s_1$: $\\text{FPR}{=}0.38$, $\\text{FNR}{=}0.054$ ($7{:}1$ ratio); 100 MC runs.\nWe compare EC-HTE using the full $2{\\times}2$ asymmetric CM (Remark~2) against the symmetric assumption ($\\text{FPR}{=}\\text{FNR}{=}\\pi_s$).\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE under asymmetric misclassification ($\\text{FPR}/\\text{FNR}$ up to $7{:}1$). The asymmetric formula improves coverage by $+1.5$pp and RMSE by $11.5\\%$.}\n\\label{tab:asymmetric_endtoend}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Coverage \\\\\n\\midrule\nOracle              & 0.045 & 0.056 & 0.943 \\\\\nEC-HTE (asymmetric) & 0.057 & 0.074 & \\textbf{0.945} \\\\\nNaive               & 0.059 & 0.073 & 0.870 \\\\\nGlobal (asymmetric) & 0.061 & 0.076 & 0.915 \\\\\nEC-HTE (symmetric)  & 0.062 & 0.083 & 0.930 \\\\\nGlobal (symmetric)  & 0.063 & 0.078 & 0.915 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE with the asymmetric formula achieves 94.5\\% coverage versus 93.0\\% under the symmetric assumption ($+1.5$pp), with RMSE improved from 0.083 to 0.074 ($-11.5\\%$).\nThe improvement concentrates in the high-error subgroup ($s_1$): asymmetric coverage is 93.0\\% vs.\\ symmetric 91.0\\%.\nPractitioners should estimate full $2 \\times 2$ confusion matrices rather than assuming symmetric misclassification, particularly when FPR and FNR differ substantially.\n\n\\subsection{Complementarity with LLM Calibration}\n\\label{app:calibration}\n\nTemperature or Platt scaling~\\cite{guo2017calibration} can reduce per-subgroup misclassification rates, but does not eliminate heterogeneity $\\Delta\\pi$.\nWe simulate calibration by shrinking per-subgroup rates from $\\pi{=}[0.05, 0.25]$ ($\\Delta\\pi{=}0.20$) to $\\pi{=}[0.08, 0.15]$ ($\\Delta\\pi{=}0.07$), testing whether EC-HTE remains necessary post-calibration.\nSetup: $K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{Calibration reduces $\\Delta\\pi$ but does not eliminate it; EC-HTE corrects the residual bias. Best coverage is achieved by combining both.}\n\\label{tab:calibration}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Coverage \\\\\n\\midrule\nOracle                    & 0.043 & 0.053 & 0.963 \\\\\nCalibrated + EC-HTE       & 0.055 & 0.069 & \\textbf{0.965} \\\\\nCalibrated + Global       & 0.055 & 0.068 & 0.963 \\\\\nCalibrated + Naive        & 0.051 & 0.064 & 0.913 \\\\\nUncalibrated + EC-HTE     & 0.064 & 0.084 & 0.938 \\\\\nUncalibrated + Global     & 0.069 & 0.085 & 0.920 \\\\\nUncalibrated + Naive      & 0.063 & 0.079 & 0.840 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCalibration alone improves naive coverage from 84.0\\% to 91.3\\% but does not reach the nominal 95\\%.\nCalibrated + EC-HTE achieves the highest coverage (96.5\\%), demonstrating that calibration and EC-HTE address orthogonal error sources: calibration reduces per-subgroup $\\pi_s$ while EC-HTE corrects the residual $\\delta_s$-driven bias from heterogeneity that persists post-calibration.\nPropensity estimation robustness under model misspecification is an orthogonal concern addressed by the IPW literature; EC-HTE as a downstream correction layer does not alter IPW behavior.\n",
    "structuredPatch": [
      {
        "oldStart": 514,
        "oldLines": 7,
        "newStart": 514,
        "newLines": 7,
        "lines": [
          " \\end{tabular}",
          " \\end{table*}",
          " ",
          "-The orthogonality of EC-HTE and PPCI follows from the distinct error sources they correct: EC-HTE addresses misclassification in the effect modifier $Z$ (covariate space), while PPCI corrects specification error in the outcome model $f(X)$ (prediction space).",
          "+The complementarity of EC-HTE and PPCI follows from the distinct error sources they correct: EC-HTE addresses misclassification in the effect modifier $Z$ (covariate space), while PPCI corrects specification error in the outcome model $f(X)$ (prediction space).",
          " Since covariate misclassification and outcome model error are algebraically independent in the potential outcomes framework, their corrections compose without interference---confirmed by the 4-DGP orthogonal design (Table~\\ref{tab:ppci}), where DGP~C (both errors present) yields the largest bias reduction from the combined approach.",
          " Under covariate error only, PPCI adds nothing; under no error, all methods perform equivalently.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Edit · `toolu_01CWPKFB7GDsV7YnfxocAYMv`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "old_string": "propensity misspecification is an orthogonal concern addressed by the IPW literature.}",
  "new_string": "propensity misspecification is a complementary concern addressed by the IPW literature.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "75ca0c55-ad14-4bed-ba40-167d9d236c40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfTCbq1mJavYLkU3D8YAFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14448,
      "cache_read_input_tokens": 53368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14448
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-23T09:29:45.780Z_

<details><summary>↩ Tool result · `toolu_01CWPKFB7GDsV7YnfxocAYMv`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "e205252d-1d66-4eb9-af94-e345fb910158",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
    "oldString": "propensity misspecification is an orthogonal concern addressed by the IPW literature.}",
    "newString": "propensity misspecification is a complementary concern addressed by the IPW literature.}",
    "originalFile": "\\section{EC-HTE Procedure}\n\\label{app:algorithm}\n\n\\begin{algorithm}[t]\n\\caption{EC-HTE: Error-Corrected Heterogeneous Treatment Effects}\n\\label{alg:echte}\n\\begin{algorithmic}[1]\n\\Require Observations $\\{(Y_i, W_i, \\hat{Z}_i, X_i)\\}_{i=1}^N$; expert labels $\\{Z_j^*\\}_{j=1}^{n_{\\text{expert}}}$; subgroup map $S: \\mathcal{X} \\to \\{1,\\ldots,K\\}$\n\\Ensure Corrected CATE estimates $\\hat{\\tau}(z)$ with variance-adjusted CIs\n\\Statex\n\\State \\textbf{Preconditions:} verify $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$ and $\\max_s(\\text{FPR}_s, \\text{FNR}_s) < 0.5$; if either fails, use global correction\n\\Statex\n\\State \\textbf{Step 1: Estimate per-subgroup confusion matrices (HB)}\n\\For{$s = 1, \\ldots, K$}\n    \\State $C_s[j,\\cdot] \\sim \\mathrm{Dir}(\\alpha_0 \\cdot \\hat{C}_{\\text{global},j})$, \\; $\\alpha_0$ via empirical Bayes\n    \\State Gibbs sampler (4 chains, 4000 iter) on $\\{(\\hat{Z}_j, Z_j^*) : S_j = s\\}$\n    \\State $\\hat{C}_s \\gets$ posterior mean; verify $\\hat{R} < 1.01$\n\\EndFor\n\\Statex\n\\State \\textbf{Step 2: Correct observed outcome moments}\n\\For{$s = 1, \\ldots, K$}\n    \\If{$\\kappa(\\hat{C}_s) > 100$} $\\hat{C}_s \\gets \\bar{C}$ \\Comment{singularity guard}\n    \\EndIf\n    \\State $\\tilde{\\boldsymbol{\\mu}}_s \\gets \\hat{C}_s^{-1} \\hat{\\boldsymbol{\\mu}}_s$\n\\EndFor\n\\Statex\n\\State \\textbf{Step 3: CausalForestDML with variance-adjusted SEs}\n\\State Train CausalForest (honest splitting) on corrected outcome moments $\\tilde{\\boldsymbol{\\mu}}_s$\n\\State $\\mathrm{se}_{\\mathrm{adj},i} \\gets \\sqrt{\\mathrm{diag}(\\hat{C}_{S_i}^{-1}\\, \\mathrm{diag}(\\mathrm{se}_i^2)\\, \\hat{C}_{S_i}^{-\\top})}$\n\\State \\Return $\\hat{\\tau}(z)$ with 95\\% CIs from $\\mathrm{se}_{\\mathrm{adj}}$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\subsection{Condition Number Guard Ablation}\n\\label{app:kappa_ablation}\n\nThe singularity guard in Algorithm~\\ref{alg:echte} (line~6) falls back to global correction when $\\kappa(\\hat{C}_s) > 100$.\nWe verify that this threshold is not load-bearing by sweeping $\\kappa \\in \\{10, 25, 50, 100, 200, 500, 1000\\}$ under the standard DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 100 MC runs).\nAcross all configurations, the maximum observed condition number is $\\kappa_{\\max} = 1.89$ (mean 1.45, p99 1.89), providing a $53{\\times}$ safety margin below the $\\kappa{=}100$ threshold.\nConsequently, the guard never triggers at any tested threshold, and all $\\kappa$ values produce identical RMSE (HB: 0.076, Global: 0.077) and zero numerical instability.\nIn a stress test with near-random labeling ($\\pi_s \\approx 0.4$--$0.5$, $n_{\\text{expert}}{=}50$), the maximum condition number reaches 1{,}125, correctly triggering the $\\kappa{=}100$ guard and preventing catastrophic inversion.\nThe adaptive formula $\\kappa_{\\text{adapt}} = 10 \\sqrt{n_{\\text{expert}} / K}$ recovers $\\kappa{=}100$ for this regime and scales naturally with the estimation precision.\n\n\\section{Full Proof of Theorem~\\ref{thm:bias_identity}}\n\\label{app:derivation}\n\n\\paragraph{Setup.}\nUnder assumptions (A1)--(A4), the observed CATE in subgroup $s$ at effect-modifier level $z$ is\n\\begin{equation}\n\\tau_{\\text{obs}}(z, s) = \\sum_{z'} M_s[z, z'] \\cdot \\tau(z'),\n\\end{equation}\nwhere $M_s[z, z'] = P(Z{=}z' \\mid \\hat{Z}{=}z, S{=}s)$ is the mixing matrix.\nUnder (A2)--(A3), $M_s = \\bigl[\\begin{smallmatrix} 1-\\pi_s & \\pi_s \\\\ \\pi_s & 1-\\pi_s \\end{smallmatrix}\\bigr]$.\n\n\\paragraph{Global correction.}\nThe pooled mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s = \\bigl[\\begin{smallmatrix} 1-\\bar{\\pi} & \\bar{\\pi} \\\\ \\bar{\\pi} & 1-\\bar{\\pi} \\end{smallmatrix}\\bigr]$, with $\\bar{\\pi} = \\sum_s w_s \\pi_s$.\n\nGlobal correction applies $M_{\\text{global}}^{-1}$ to $\\tau_{\\text{obs}}(\\cdot, s)$:\n\\begin{equation}\n\\hat{\\tau}_{\\text{global}}(z, s) = [M_{\\text{global}}^{-1} M_s \\cdot \\boldsymbol{\\tau}]_z,\n\\end{equation}\nwhere $\\boldsymbol{\\tau} = [\\tau(0), \\tau(1)]^\\top$.\n\n\\paragraph{Bias computation.}\nThe bias is $\\hat{\\tau}_{\\text{global}}(z, s) - \\tau(z) = [(M_{\\text{global}}^{-1} M_s - I) \\boldsymbol{\\tau}]_z$.\n\nDirect computation gives:\n\\begin{equation}\nM_{\\text{global}}^{-1} = \\frac{1}{1 - 2\\bar{\\pi}} \\begin{bmatrix} 1-\\bar{\\pi} & -\\bar{\\pi} \\\\ -\\bar{\\pi} & 1-\\bar{\\pi} \\end{bmatrix}.\n\\end{equation}\nMultiplying by $M_s$:\n\\begin{equation}\n\\resizebox{.88\\columnwidth}{!}{$\\displaystyle\nM_{\\text{global}}^{-1} M_s = \\frac{1}{1-2\\bar{\\pi}} \\begin{bmatrix} (1{-}\\bar{\\pi})(1{-}\\pi_s) - \\bar{\\pi}\\pi_s & (1{-}\\bar{\\pi})\\pi_s - \\bar{\\pi}(1{-}\\pi_s) \\\\ -\\bar{\\pi}(1{-}\\pi_s) + (1{-}\\bar{\\pi})\\pi_s & -\\bar{\\pi}\\pi_s + (1{-}\\bar{\\pi})(1{-}\\pi_s) \\end{bmatrix}.\n$}\n\\end{equation}\n\nDefine $\\delta_s = \\pi_s - \\bar{\\pi}$. Substituting $\\pi_s = \\bar{\\pi} + \\delta_s$:\n\\begin{equation}\nM_{\\text{global}}^{-1} M_s - I = \\frac{\\delta_s}{1-2\\bar{\\pi}} \\begin{bmatrix} -1 & 1 \\\\ 1 & -1 \\end{bmatrix}.\n\\end{equation}\n\nTo verify: the $(1,1)$ entry of $M_{\\text{global}}^{-1} M_s$ is\n{\\small\n\\begin{align}\n&\\frac{(1{-}\\bar{\\pi})(1{-}\\bar{\\pi}{-}\\delta_s) - \\bar{\\pi}(\\bar{\\pi}{+}\\delta_s)}{1-2\\bar{\\pi}} \\nonumber\\\\\n&= \\frac{(1{-}\\bar{\\pi})^2 - (1{-}\\bar{\\pi})\\delta_s - \\bar{\\pi}^2 - \\bar{\\pi}\\delta_s}{1-2\\bar{\\pi}} \\nonumber\\\\\n&= \\frac{1 - 2\\bar{\\pi} - \\delta_s}{1-2\\bar{\\pi}} = 1 - \\frac{\\delta_s}{1-2\\bar{\\pi}}.\n\\end{align}\n}\n\nApplying $(M_{\\text{global}}^{-1} M_s - I)$ to $\\boldsymbol{\\tau}$:\n{\\small\n\\begin{align}\n\\text{bias}(z{=}0, s) &= \\tfrac{\\delta_s}{1-2\\bar{\\pi}}(-\\tau(0) + \\tau(1)) = +\\tfrac{\\delta_s \\cdot \\Delta\\tau}{1-2\\bar{\\pi}}, \\\\\n\\text{bias}(z{=}1, s) &= \\tfrac{\\delta_s}{1-2\\bar{\\pi}}(\\tau(0) - \\tau(1)) = -\\tfrac{\\delta_s \\cdot \\Delta\\tau}{1-2\\bar{\\pi}},\n\\end{align}\n}\nwhere $\\Delta\\tau = \\tau(1) - \\tau(0)$. \\qed\n\n\\section{Multi-class Extension and Proof}\n\\label{app:multiclass}\n\n\\begin{corollary}[Multi-class Extension]\n\\label{cor:multiclass}\nFor $K > 2$ subgroups with $J$ effect-modifier levels and uniform off-diagonal misclassification (misclassified observations from class $j$ are distributed equally among the remaining $J{-}1$ classes), the subgroup bias of global correction generalizes to\n\\begin{equation}\n\\mathrm{bias}_{\\mathrm{global}}(z, s) = \\sum_{j=1}^{J} \\bigl(\\bar{\\pi}_j - \\pi_{s,j}\\bigr) \\cdot \\bigl(\\tau(j) - \\bar{\\tau}\\bigr) \\cdot g(\\bar{\\pi}),\n\\label{eq:multiclass}\n\\end{equation}\nwhere $g(\\bar{\\pi})$ collects the matrix-inversion amplification terms.\\footnote{For $J=3$ with symmetric misclassification (off-diagonal errors uniform), $g(\\bar{\\pi}) = 1/(1 - 3\\bar{\\pi}/2)$, generalizing the $J{=}2$ factor $1/(1-2\\bar{\\pi})$. In general, $g(\\bar{\\pi}) = 1/(1 - J\\bar{\\pi}/(J-1))$.}\nThe essential structure, $\\sum_s w_s (\\bar{\\pi}_j - \\pi_{s,j}) = 0$, ensures that bias redistributes across subgroups rather than vanishing in aggregate.\n\\end{corollary}\n\n\\paragraph{Proof.}\nFor $K > 2$ subgroups with $J$ effect-modifier levels, the subgroup-specific mixing matrix $M_s$ is $J \\times J$ with entries $M_s[j, j'] = P(Z{=}j' \\mid \\hat{Z}{=}j, S{=}s)$.\nThe global mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s$.\n\nThe bias of global correction in subgroup $s$ at level $z$ is:\n\\begin{equation}\n\\text{bias}_{\\text{global}}(z, s) = [(M_{\\text{global}}^{-1} M_s - I) \\boldsymbol{\\tau}]_z.\n\\end{equation}\n\nWrite $M_s = M_{\\text{global}} + \\Delta_s$ where $\\Delta_s = M_s - M_{\\text{global}}$ satisfies $\\sum_s w_s \\Delta_s = 0$.\nThen $M_{\\text{global}}^{-1} M_s = I + M_{\\text{global}}^{-1} \\Delta_s$, so:\n\\begin{equation}\n\\text{bias}_{\\text{global}}(z, s) = [M_{\\text{global}}^{-1} \\Delta_s \\cdot \\boldsymbol{\\tau}]_z.\n\\end{equation}\n\nFor symmetric misclassification with per-class error rates $\\pi_{s,j}$ and pooled rates $\\bar{\\pi}_j$, the entries of $\\Delta_s$ have the form $\\Delta_s[j,j'] = (\\bar{\\pi}_j - \\pi_{s,j}) \\cdot h(j, j')$ for a function $h$ determined by the off-diagonal redistribution pattern.\nExpanding the matrix-vector product and collecting terms yields:\n\\begin{equation}\n\\text{bias}_{\\text{global}}(z, s) = \\sum_{j=1}^{J} (\\bar{\\pi}_j - \\pi_{s,j}) \\cdot (\\tau(j) - \\bar{\\tau}) \\cdot g(\\bar{\\pi}),\n\\end{equation}\nwhere $g(\\bar{\\pi})$ collects the matrix-inversion amplification terms and $\\bar{\\tau} = \\sum_j P(Z{=}j) \\tau(j)$.\n\nThe essential structure $\\sum_s w_s (\\bar{\\pi}_j - \\pi_{s,j}) = 0$ ensures that the weighted bias across subgroups sums to zero: global correction redistributes bias rather than creating or eliminating it in aggregate.\nFor non-uniform off-diagonal entries, the scalar amplification $g(\\bar{\\pi})$ generalizes to a cell-specific matrix; the product structure $B_s \\cdot \\Delta\\tau$ persists but a closed-form amplification factor does not. \\qed\n\n\\section{Proof of Proposition~\\ref{prop:debiasing_hurts}}\n\\label{app:debiasing_hurts}\n\nThe naive estimator has bias $\\tau_{\\text{obs}}(z,s) - \\tau(z)$.\nUnder (A2)--(A3), $\\tau_{\\text{obs}}(0,s) = (1-\\pi_s)\\tau(0) + \\pi_s\\tau(1)$, so $\\text{bias}_{\\text{naive}}(0,s) = \\pi_s \\cdot \\Delta\\tau$.\n\nGlobal correction produces larger absolute bias when $|\\text{bias}_{\\text{global}}(0,s)| > |\\text{bias}_{\\text{naive}}(0,s)|$:\n\\begin{equation}\n\\frac{|\\delta_s| \\cdot |\\Delta\\tau|}{|1-2\\bar{\\pi}|} > \\pi_s \\cdot |\\Delta\\tau|.\n\\end{equation}\nSince $\\Delta\\tau \\neq 0$ (otherwise both biases are zero), dividing through gives:\n\\begin{equation}\n\\frac{|\\delta_s|}{(1-2\\bar{\\pi}) \\cdot \\pi_s} > 1,\n\\end{equation}\nwhere we use $1-2\\bar{\\pi} > 0$ from (A4).\n\nFor high-error subgroups ($\\pi_s > \\bar{\\pi}$, so $\\delta_s > 0$): the condition becomes $(\\pi_s - \\bar{\\pi}) / ((1-2\\bar{\\pi})\\pi_s) > 1$, which simplifies to $\\pi_s(1 - 1 + 2\\bar{\\pi}) > \\bar{\\pi}$, i.e., $2\\bar{\\pi}\\pi_s > \\bar{\\pi}$, i.e., $\\pi_s > 0.5$.\nThis is excluded by (A4), so global correction always reduces bias in high-error subgroups.\n\nFor low-error subgroups ($\\pi_s < \\bar{\\pi}$, so $\\delta_s < 0$): the condition becomes $(\\bar{\\pi} - \\pi_s) / ((1-2\\bar{\\pi})\\pi_s) > 1$, which gives $\\pi_s < \\bar{\\pi} / (1 - 2\\bar{\\pi} + 1) = \\bar{\\pi} / (2(1-\\bar{\\pi}))$.\nWhen $\\bar{\\pi} = 0.15$, any subgroup with $\\pi_s < 0.088$ experiences increased bias from global correction. \\qed\n\n\\paragraph{Extension to asymmetric misclassification.}\nProposition~\\ref{prop:debiasing_hurts} assumes symmetric error rates (A2).\nUnder asymmetric misclassification ($\\mathrm{FPR}_s \\neq \\mathrm{FNR}_s$), the naive bias becomes $\\mathrm{bias}_{\\mathrm{naive}}(0,s) = \\mathrm{FPR}_s \\cdot \\tau(1) + (1 - \\mathrm{FPR}_s - 1)\\tau(0)$ and the global correction bias depends on the full $2 \\times 2$ structure of $B_s = M_{\\mathrm{global}}^{-1} M_s - I$ (Remark~1 in Section~\\ref{sec:theory}).\nA sufficient condition for global correction to increase bias is\n\\begin{equation}\n\\|B_s\\|_\\infty > \\max(\\mathrm{FPR}_s, \\mathrm{FNR}_s),\n\\end{equation}\nwhich reduces to Equation~\\eqref{eq:hurts_condition} when $\\mathrm{FPR}_s = \\mathrm{FNR}_s = \\pi_s$.\nIn the asymmetric experiments (Appendix~\\ref{app:asymmetric}), the symmetric diagnostic still achieves AUC $= 0.82$ when applied with $\\pi_s = (\\mathrm{FPR}_s + \\mathrm{FNR}_s)/2$, suggesting practical robustness.\nA fully general asymmetric diagnostic that accounts for the separate roles of FPR and FNR in each entry of $B_s$ is left to future work.\n\n\\section{Semi-Synthetic Data Generating Process}\n\\label{app:dgp}\n\n\\paragraph{Synthetic DGP (Sections~\\ref{sec:bias_mechanism}--\\ref{sec:diagnostic} and Appendix~\\ref{sec:budget}).}\nWe generate $N = 5000$ observations.\nEach observation belongs to one of $K \\in \\{2, 4\\}$ subgroups $S \\in \\{1, \\ldots, K\\}$ with equal weights $w_s = 1/K$.\nThe binary effect modifier $Z \\in \\{0, 1\\}$ is drawn with $P(Z{=}1) = 0.5$.\nTreatment assignment is $T \\sim \\text{Bernoulli}(0.5)$, independent of $Z$ and $S$.\n\nThe outcome is generated as:\n\\begin{equation}\nY = \\tau(Z) \\cdot T + \\varepsilon, \\quad \\varepsilon \\sim \\mathcal{N}(0, 1),\n\\end{equation}\nwhere the CATE function is $\\tau(z) = \\bar{\\tau} + \\Delta\\tau \\cdot (z - 0.5)$ with $\\bar{\\tau} = 0.5$.\nThe CATE heterogeneity $\\Delta\\tau \\in \\{0, 0.2, 0.5, 1.0\\}$ controls the strength of treatment effect variation across levels of $Z$.\n\nMisclassification is symmetric: $\\hat{Z} \\neq Z$ with probability $\\pi_s$ depending on subgroup.\nFor $K{=}2$: $\\pi_1 = \\bar{\\pi} - \\Delta_c/2$, $\\pi_2 = \\bar{\\pi} + \\Delta_c/2$, with $\\bar{\\pi} \\in \\{0.1, 0.2\\}$ and $\\Delta_c \\in \\{0, 0.05, 0.1, 0.15\\}$.\nFor $K{=}4$, extreme regime: $\\pi \\in \\{0.05, 0.10, 0.15, 0.25\\}$; moderate regime: $\\pi \\in \\{0.08, 0.12, 0.16, 0.20\\}$.\n\nExpert labels are drawn as a simple random sample of size $n_{\\text{expert}} \\in \\{50, 100, 250, 500, 1000, 2000\\}$ from the full dataset, with true $Z$ observed for these observations.\n\n\\paragraph{Semi-synthetic DGP (Section~\\ref{sec:ec_hte_eval}).}\nWe sample $N = 5000$ tweets from the TweetEval sentiment corpus ($N_{\\text{pool}} = 57{,}899$).\nSubgroups are defined by crossing \\texttt{has\\_hashtag} $\\times$ \\texttt{text\\_length\\_bin} (short/medium/long), yielding $K = 4$ subgroups with empirical sizes: $S_0 \\approx 38\\%$, $S_1 \\approx 38\\%$, $S_2 \\approx 12\\%$, $S_3 \\approx 12\\%$.\nMisclassification rates in the extreme regime are $\\pi_{S_0} = 0.05$, $\\pi_{S_1} = 0.10$, $\\pi_{S_2} = 0.15$, $\\pi_{S_3} = 0.25$, reflecting empirical evidence that hashtag-heavy text degrades LLM classifier accuracy.\nThe outcome DGP follows the same structure as the synthetic case, with CATE injected onto the real text-derived subgroup structure.\n\n\\paragraph{PPCI DGPs (Appendix~\\ref{sec:ppci}).}\nFour DGPs isolate error types: (A) covariate error only ($\\sigma_{\\text{outcome}} = 0$), (B) outcome error only ($\\sigma_{\\text{outcome}} = 0.5$), (C) both errors ($\\sigma_{\\text{outcome}} = 0.5$), (D) no error ($\\sigma_{\\text{outcome}} = 0$).\nOutcome-side error is additive Gaussian noise on $Y$.\n\n\\paragraph{CausalForestDML hyperparameters.}\nAll CausalForest experiments use \\texttt{econml.dml.CausalForestDML} with honest splitting, $n_{\\text{estimators}} = 48$, $\\texttt{min\\_samples\\_leaf} = 20$, \\texttt{model\\_y} = \\texttt{LassoCV}(cv=3), and \\texttt{model\\_t} = \\texttt{LogisticRegressionCV}.\nThese defaults were held constant across all configurations; no hyperparameter tuning was performed.\n\n\\section{Extended Related Work}\n\\label{app:related}\n\n\\paragraph{Measurement error details.}\n\\citet{fuller1987measurement} establish the foundational theory showing that naive regression with mismeasured covariates yields attenuated coefficient estimates.\n\\citet{carroll2006measurement} extend this to nonlinear models.\n\\citet{gustafson2003measurement} develops Bayesian treatments modeling measurement jointly with outcomes.\n\\citet{hu2008nonparametric} provide nonparametric identification using repeated measurements or instruments.\n\n\\paragraph{Annotation model extensions.}\nBeyond the foundational \\citet{dawid1979maximum} model, \\citet{passonneau2014benefits} incorporate item difficulty, \\citet{hovy2013learning} learn annotator competence, and \\citet{paun2018comparing} introduce hierarchical priors sharing information across annotators with varying expertise.\n\n\\paragraph{PPI extensions and text-as-data methods.}\n\\citet{zrnic2024cross} extend PPI via cross-prediction; their active inference framework~\\citep{zrnic2024active} achieves $>$80\\% expert budget savings through adaptive allocation, complementary to our fixed-budget analysis.\n\\citet{grimmer2022text} provide methodological guidance for text-as-data pipelines.\n\\citet{audinet2025benchmarking} systematically benchmark DSL and PPI methods for LLM-based parameter estimation, finding that debiasing can increase MSE when prediction error is heterogeneous---a population-level analogue of the subgroup-conditional bias amplification we formalize in Theorem~\\ref{thm:bias_identity}.\n\n\\paragraph{Treatment vs.\\ effect-modifier misclassification.}\n\\citet{imai2010causal} study treatment misclassification where errors change which arm a unit is assigned to, requiring instrumental variables or partial identification because the fundamental treated-vs-control contrast is corrupted.\nOur problem preserves the treatment contrast ($T$ is observed correctly) but corrupts the heterogeneity structure ($\\hat{Z} \\neq Z$).\nThe ATE remains identified; only conditional effects are biased, which makes exact correction through confusion matrix inversion feasible.\n\n\\paragraph{Econometrics of binary misclassification.}\n\\citet{bound2001measurement} survey measurement error in survey data, establishing that binary misclassification attenuates regression coefficients.\n\\citet{frazis2003estimating} derive exact bias formulas for OLS with a misclassified binary regressor, showing attenuation proportional to the misclassification rate---analogous to our Theorem~\\ref{thm:bias_identity} but restricted to average effects without subgroup heterogeneity.\n\\citet{black2000racial} demonstrate that racial misclassification in administrative data can substantially bias estimates of racial disparities.\n\\citet{mahajan2006identification} and \\citet{lewbel2007estimation} develop instrumental variable approaches to identify models with misclassified binary regressors, requiring exclusion restrictions unavailable when the mismeasured variable is an LLM annotation.\nOur setting differs in three respects: (i) the mismeasured variable is an effect modifier indexing the CATE function, not a standard regressor; (ii) misclassification rates vary across subgroups, creating the $\\delta_s \\times \\Delta\\tau$ product amplification absent from homogeneous-error analyses; and (iii) expert labels provide a direct calibration sample, enabling confusion matrix estimation without instruments.\n\n\\section{MCMC Convergence Diagnostics}\n\\label{app:mcmc}\n\nTable~\\ref{tab:mcmc} reports convergence diagnostics for the hierarchical Bayesian confusion matrix estimator across all experimental configurations.\nAll runs use 4 chains with 4000 iterations (2000 warmup).\nMain experiments (Table~\\ref{tab:main_results}) use a Dirichlet prior centered on $\\hat{C}_{\\text{global}}$ with concentration $\\alpha_0$ estimated via empirical Bayes (marginal likelihood).\nAppendix robustness experiments use a fixed Dirichlet prior ($\\alpha{=}3$); since fixed-$\\alpha$ partial pooling is weakly dominated by the adaptive variant, these results are conservative.\nThis budget is sufficient for the $2{\\times}2$ Dirichlet-Multinomial posterior; all runs achieve $\\hat{R} < 1.0034$ and ESS $> 1618$, confirming convergence with substantial margin.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nDiagnostic & Threshold & Achieved \\\\\n\\midrule\n$\\hat{R}$ (max across all params) & $< 1.01$ & $< 1.0034$ \\\\\nESS (min across all params) & $> 845$ & $> 1618$ \\\\\nDivergent transitions & $= 0$ & $0$ \\\\\nSingularity guard triggers & --- & extreme/$n{=}50$ only \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{MCMC convergence diagnostics for the hierarchical Bayesian estimator. All configurations satisfy convergence criteria with substantial margin.}\n\\label{tab:mcmc}\n\\end{table}\n\n\\paragraph{Hyperprior sensitivity.}\nScaling the $\\text{Gamma}(3, 1)$ hyperprior by factors of $0.5\\times$ to $2\\times$ produces $<$1\\% RMSE variation for $K{=}2$ and $\\sim$4--5\\% for $K{=}4$.\nCoverage remains invariant across the sensitivity range.\nThese results confirm that the hierarchical estimator is robust to prior specification within a reasonable range.\n\n\\section{Diagnostic ROC Curves}\n\\label{app:roc}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_roc.png}\n\\caption{ROC curves for the $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}): $|\\delta_s|/((1{-}2\\bar\\pi)\\cdot\\pi_s)>1$. (A)~Setting-level ROC (AUC $= 0.89$), compared with the $|\\Delta\\pi \\times \\Delta\\tau|$ product (AUC $= 0.89$) and $\\mathrm{CV}(\\pi_s)$ (AUC $= 0.97$). (B)~Subgroup-level ROC: the $\\Delta\\pi$-only condition (AUC $= 0.86$) substantially outperforms the $|\\Delta\\pi \\times \\Delta\\tau|$ product (AUC $= 0.73$). The $\\Delta\\tau$-free diagnostic depends only on estimable misclassification rates, breaking the circular dependency that would arise if CATE heterogeneity were required.}\n\\label{fig:roc}\n\\end{figure}\n\n\\paragraph{Cost-asymmetric diagnostic thresholds.}\nIn practice, the cost of a false negative (failing to detect that global correction increases bias) exceeds the cost of a false positive (unnecessarily applying EC-HTE when global correction would suffice), because the former propagates systematic bias into CATE estimates while the latter only incurs additional estimation variance.\nPractitioners in high-stakes settings (e.g., policy evaluation where CATE estimates inform resource allocation) should lower the diagnostic threshold to favor recall over precision, accepting more false positives to minimize the risk of undetected bias amplification.\n\n\\section{Expert Budget Crossover Curves}\n\\label{app:budget}\n\\label{sec:budget}\n\nThe crossover point at which EC-HTE achieves lower RMSE than global correction is $n_{\\text{expert}} = 250$ for $K{=}2$/extreme and $n_{\\text{expert}} = 1000$ for $K{=}4$/extreme (Figure~\\ref{fig:budget}).\nUnder moderate heterogeneity ($K{=}2$), EC-HTE never achieves lower RMSE than global at any budget.\nHB partial pooling improves over stratified MLE in 21 of 24 configurations, with the two estimators converging by $n_{\\text{expert}} \\geq 1000$.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig3_budget.pdf}\n\\caption{RMSE vs.\\ expert budget ($n_{\\text{expert}}$) across four regime$\\times K$ combinations. Dashed vertical lines mark crossover points where EC-HTE achieves lower RMSE than global correction: $n{=}250$ ($K{=}2$, extreme), $n{=}1000$ ($K{=}4$, extreme). Under moderate heterogeneity ($K{=}2$), global correction dominates at all budgets. Shaded bands show $\\pm 1$ SD across subgroups within each configuration.}\n\\label{fig:budget}\n\\end{figure*}\n\n\\subsection{Budget Sensitivity: HB vs.\\ Stratified MLE}\n\\label{app:budget_sensitivity}\n\nHierarchical Bayes (HB) partial pooling borrows strength across subgroups, which should matter most when per-subgroup expert labels are scarce.\nWe sweep $n_{\\text{expert}} \\in \\{25, 50, 75, 100, 150, 250\\}$ under extreme heterogeneity ($\\Delta\\tau{=}0.3$, 100 MC runs, $N{=}5{,}000$).\nTable~\\ref{tab:budget_sensitivity} reports aggregate RMSE for global correction, stratified MLE, and HB EC-HTE.\n\n\\begin{table}[h]\n\\centering\n\\caption{RMSE across expert budgets under extreme heterogeneity.\nHB crossover (first budget where HB $<$ MLE) occurs at approximately 10 expert labels per subgroup-cell:\n$n_{\\text{expert}}{=}50$ for $K{=}2$ and $n_{\\text{expert}}{=}75$ for $K{=}4$.}\n\\label{tab:budget_sensitivity}\n\\small\n\\begin{tabular}{crrrrc}\n\\toprule\n$K$ & $n_{\\text{expert}}$ & Global & Strat.\\ MLE & HB EC-HTE & HB vs.\\ MLE \\\\\n\\midrule\n2 & 25 & \\textbf{0.101} & 0.256 & 0.269 & $+4.9\\%$ \\\\\n2 & 50 & \\textbf{0.088} & 0.275 & 0.231 & $\\mathbf{-16.1\\%}$ \\\\\n2 & 75 & 0.084 & 0.091 & \\textbf{0.089} & $-1.9\\%$ \\\\\n2 & 100 & 0.083 & 0.085 & \\textbf{0.084} & $-0.8\\%$ \\\\\n2 & 150 & 0.081 & 0.077 & \\textbf{0.077} & $-0.4\\%$ \\\\\n2 & 250 & 0.080 & 0.075 & \\textbf{0.074} & $-0.1\\%$ \\\\\n\\midrule\n4 & 25 & \\textbf{0.129} & 0.401 & 0.612 & $+52.5\\%$ \\\\\n4 & 50 & \\textbf{0.117} & 0.380 & 0.470 & $+23.8\\%$ \\\\\n4 & 75 & \\textbf{0.112} & 0.221 & 0.211 & $\\mathbf{-4.4\\%}$ \\\\\n4 & 100 & \\textbf{0.112} & 0.215 & 0.212 & $-1.3\\%$ \\\\\n4 & 150 & \\textbf{0.109} & 0.157 & 0.152 & $-3.6\\%$ \\\\\n4 & 250 & \\textbf{0.108} & 0.127 & 0.126 & $-1.0\\%$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree regimes emerge.\nAt very low budgets ($n_{\\text{expert}} < 50$ for $K{=}2$, $< 75$ for $K{=}4$), per-subgroup counts are insufficient for reliable confusion matrix estimation; global pooling dominates because the variance cost of stratification overwhelms any bias reduction.\nHB degrades substantially in this regime because the Gibbs posterior, while better regularized than MLE, still cannot overcome the fundamental sample-size constraint with $\\sim$6--12 labels per subgroup.\nAt moderate budgets ($n_{\\text{expert}} = 50$--$250$ for $K{=}2$, $75$--$250$ for $K{=}4$), HB partial pooling provides consistent RMSE improvement over stratified MLE ($-0.4\\%$ to $-16.1\\%$), with the largest gains near the crossover point.\nAt high budgets ($n_{\\text{expert}} \\geq 250$), both estimators converge as subgroup-level data becomes sufficient for reliable MLE; the HB advantage diminishes to $< 1\\%$.\nCoverage remains $\\geq 0.88$ for both methods across all budget levels.\n\n\\subsection{Scalability to $K{=}8$ Subgroups}\n\\label{app:k8_subgroups}\n\nWe test EC-HTE at $K{=}8$ to identify the scalability boundary of hierarchical Bayesian partial pooling under fixed expert budget.\n\n\\paragraph{Setup.}\n$N{=}5{,}000$, $K{=}8$ (equal-weight subgroups), $n_{\\text{expert}}{=}250$ (${\\approx}31$ labels per subgroup), 100 MC replications.\nMisclassification rates are uniformly spread: $\\pi_s \\in \\{0.05, 0.09, 0.13, 0.18, 0.22, 0.26, 0.30, 0.35\\}$.\nTreatment effects depend on $Z$ (not subgroup): $\\tau(Z{=}0){=}0$, $\\tau(Z{=}1){=}0.3$.\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE at $K{=}8$ ($n_{\\text{expert}}{=}250$, ${\\approx}31$ labels/subgroup, 100 MC).}\n\\label{tab:k8_subgroups}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Coverage & RMSE & $|\\text{Bias}|$ \\\\\n\\midrule\nOracle       & 0.944 & 0.113 & 0.090 \\\\\nGlobal       & 0.951 & 0.168 & 0.135 \\\\\nHB EC-HTE    & 0.956 & 0.340 & 0.183 \\\\\nStrat MLE    & 0.953 & 0.638 & 0.219 \\\\\nNaive        & 0.913 & 0.133 & 0.107 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll CM-aware methods achieve nominal coverage at $K{=}8$: HB EC-HTE 95.6\\%, Strat MLE 95.3\\%, Global 95.1\\%.\nHB partial pooling achieves a 47\\% RMSE reduction over stratified MLE (0.340 vs.\\ 0.638), confirming that hierarchical shrinkage provides substantial regularization.\nHowever, HB RMSE (0.340) exceeds global correction (0.168), indicating that ${\\approx}31$ expert labels per subgroup are insufficient for per-subgroup CM estimation to outweigh variance inflation.\n\n\\paragraph{Per-subgroup breakdown.}\nTable~\\ref{tab:k8_per_subgroup} decomposes RMSE by subgroup.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-subgroup RMSE at $K{=}8$. HB improvement over MLE is largest in high-$\\pi$ subgroups but does not close the gap with Global.}\n\\label{tab:k8_per_subgroup}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\nSubgroup & $\\pi_s$ & HB RMSE & MLE RMSE & Global RMSE & HB Cov \\\\\n\\midrule\n$s_0$ & 0.050 & 0.136 & 0.134 & \\textbf{0.181} & 0.950 \\\\\n$s_1$ & 0.093 & 0.133 & 0.132 & \\textbf{0.154} & 0.970 \\\\\n$s_2$ & 0.136 & 0.154 & 0.154 & 0.161 & 0.975 \\\\\n$s_3$ & 0.179 & 0.178 & 0.182 & \\textbf{0.159} & 0.945 \\\\\n$s_4$ & 0.221 & 0.263 & 0.343 & \\textbf{0.163} & 0.940 \\\\\n$s_5$ & 0.264 & 0.421 & 0.711 & \\textbf{0.164} & 0.965 \\\\\n$s_6$ & 0.307 & 0.634 & 1.375 & \\textbf{0.177} & 0.940 \\\\\n$s_7$ & 0.350 & 0.432 & 0.809 & \\textbf{0.183} & 0.960 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRMSE degradation is concentrated in high-$\\pi$ subgroups ($s_4$--$s_7$, $\\pi \\geq 0.22$), where confusion matrix inversion amplifies estimation noise ($r = 0.87$, $p = 0.005$ for correlation between $\\pi_s$ and HB RMSE).\nLow-error subgroups ($s_0$--$s_1$) benefit from stratification, with HB RMSE 14--25\\% below global correction.\nHB partial pooling reduces MLE RMSE by 24--54\\% in the high-$\\pi$ regime ($s_4$--$s_7$), confirming that hierarchical shrinkage provides meaningful regularization even when per-subgroup labels are scarce.\nCoverage remains $\\geq$0.94 across all subgroups for HB EC-HTE, indicating that variance inflation does not compromise inference validity.\nAdaptive shrinkage---increasing the prior strength for high-$\\pi$ subgroups where CM estimation is least reliable---is a natural extension that may close the RMSE gap with global correction at larger $K$.\n\nWe explored adaptive shrinkage ($\\alpha{=}10$ for high-$\\pi$ subgroups vs.\\ default $\\alpha{=}3$), which reduces aggregate RMSE from 0.340 to 0.216 (35\\% improvement) by attenuating estimation noise in high-$\\pi$ subgroups.\nHowever, RMSE remains 30\\% above global correction (0.166), confirming that the bottleneck is per-subgroup sample size (${\\sim}$31 expert labels) rather than the shrinkage method itself.\nThis establishes $K{=}8$ at $n_{\\text{expert}}{=}250$ as a boundary condition: all correction methods provide valid inference (coverage $\\geq$94\\%), but per-subgroup stratification requires proportionally larger expert budgets---approximately $n_{\\text{expert}} \\geq 500$ (${\\approx}60$ labels/subgroup)---to achieve RMSE parity with global correction.\n\n\\section{Asymmetric Misclassification Extension}\n\\label{app:asymmetric}\n\nAssumption~(A2) imposes symmetric misclassification ($\\text{FPR}_s = \\text{FNR}_s = \\pi_s$), which simplifies the bias decomposition but is not necessary for it.\nReal LLM annotators typically exhibit asymmetric confusion patterns; we show here that the product structure generalizes.\n\n\\paragraph{General bias formula.}\nFor asymmetric confusion matrices $C_s = \\bigl(\\begin{smallmatrix} 1{-}\\text{FPR}_s & \\text{FPR}_s \\\\ \\text{FNR}_s & 1{-}\\text{FNR}_s \\end{smallmatrix}\\bigr)$, define the mixing matrix $M_s$ via Bayesian inversion and the residual matrix $B_s = M_{\\text{global}}^{-1} M_s - I$.\nSince both $M_s$ and $M_{\\text{global}}$ are row-stochastic, $B_s \\mathbf{1} = \\mathbf{0}$.\nDecomposing $\\boldsymbol{\\tau} = \\tau(0)\\mathbf{1} + \\Delta\\tau \\, \\mathbf{e}_1$ gives:\n\\begin{equation}\n\\text{bias}(z, s) = \\Delta\\tau \\cdot [B_s]_{z,1},\n\\end{equation}\nwhere $[B_s]_{z,1}$ depends only on $\\{\\text{FPR}_k, \\text{FNR}_k, w_k\\}$, not on $\\Delta\\tau$.\nUnder~(A2), this reduces to $\\delta_s \\Delta\\tau / (1 - 2\\bar{\\pi})$ (Theorem~\\ref{thm:bias_identity}).\n\n\\paragraph{Empirical validation.}\nWe test three asymmetric configurations ($K{=}2$, $n_{\\text{expert}}{=}250$, 100 MC runs each): \\emph{Cross} (FPR/FNR = 0.10/0.20 vs.\\ 0.25/0.10), \\emph{Co-directional} (0.05/0.15 vs.\\ 0.20/0.30), and \\emph{Extreme} (0.03/0.25 vs.\\ 0.30/0.05).\nRegressing analytic predictions on MC bias yields $R^2 = 0.991$ across all configurations, confirming the product structure under asymmetry.\nTable~\\ref{tab:asymmetric} reports correction performance averaged over subgroups, $z$-levels, and $\\Delta\\tau \\in \\{0.1, \\ldots, 0.5\\}$.\nEC-HTE reduces $|\\text{bias}|$ from 0.025 (global) to 0.006, a $4\\times$ improvement, with lower RMSE (0.033 vs.\\ 0.040) and substantially better coverage (0.90 vs.\\ 0.78).\n\n\\begin{table}[t]\n\\centering\n\\caption{Asymmetric misclassification results ($K{=}2$, $n_{\\text{expert}}{=}250$, 100 MC runs). Values averaged over subgroups, $z$-levels, and $\\Delta\\tau$.}\n\\label{tab:asymmetric}\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\nMethod & $|\\text{Bias}| \\downarrow$ & RMSE $\\downarrow$ & Coverage $\\uparrow$ \\\\\n\\midrule\nNaive & 0.047 & 0.053 & 0.48 \\\\\nGlobal & 0.025 & 0.040 & 0.78 \\\\\nHB EC-HTE & \\textbf{0.006} & \\textbf{0.033} & \\textbf{0.90} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Supplementary Main Results}\n\\label{app:main_supp}\n\n\\begin{table}[t]\n\\centering\n\\caption{Additional configurations from the main experiment. $|\\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and 100 MC runs. $^\\dagger$RMSE exceeds Global.}\n\\label{tab:main_supp}\n\\small\n\\begin{tabular}{ll ccc}\n\\toprule\nConfiguration & Method & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Synthetic DIM\\\\$K{=}2$, moderate, $n{=}250$}}\n & Naive & 0.018 & 0.064 & 0.95 \\\\\n & Global & 0.009 & 0.074 & 0.96 \\\\\n & Strat.\\ MLE & \\textbf{0.005} & 0.075$^\\dagger$ & 0.97 \\\\\n & HB EC-HTE & \\textbf{0.005} & 0.075$^\\dagger$ & 0.97 \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Semi-synthetic\\\\TweetEval, extreme, $n{=}250$}}\n & Naive & 0.027 & 0.103 & 0.93 \\\\\n & Global & \\textbf{0.023} & 0.124 & 0.92 \\\\\n & Strat.\\ MLE & 0.032 & 0.248$^\\dagger$ & 0.91 \\\\\n & HB EC-HTE & 0.027 & 0.225$^\\dagger$ & 0.91 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{PPCI Complementarity Results}\n\\label{app:ppci}\n\\label{sec:ppci}\n\nEC-HTE composes with PPCI~\\cite{sui2026ppci} for settings where both covariate misclassification and outcome model error are present: EC-HTE+PPCI reduces $|\\text{bias}|$ from 0.179 to 0.007 ($z{=}0$, DGP~C), and the corrected pseudo-outcomes are compatible with other CATE estimators (R-learner bias reduction: 89\\%; Appendix~\\ref{app:rlearner}).\n\n\\begin{table*}[t]\n\\centering\n\\caption{PPCI complementarity experiment ($K{=}2$, extreme, $n_{\\text{expert}}{=}250$). DGP~A: covariate error only; B: outcome error only ($\\sigma{=}0.5$); C: both errors; D: no error. Values are $|\\text{bias}|$ and RMSE averaged over two subgroups. $^\\star$EC-HTE+PPCI achieves near-zero bias when both error types are present.}\n\\label{tab:ppci}\n\\small\n\\begin{tabular}{ll cccc}\n\\toprule\nDGP & Method & $|\\text{Bias}|_{z=0}$ & $|\\text{Bias}|_{z=1}$ & RMSE$_{z=0}$ & RMSE$_{z=1}$ \\\\\n\\midrule\n\\multirow{5}{*}{A: Covariate}\n & Naive & 0.053 & 0.063 & 0.087 & 0.093 \\\\\n & Global & 0.063 & 0.055 & 0.101 & 0.102 \\\\\n & EC-HTE & 0.017 & \\textbf{0.013} & 0.097 & 0.108 \\\\\n & PPCI & \\textbf{0.015} & 0.020 & 0.162 & 0.168 \\\\\n & EC-HTE+PPCI & 0.017 & \\textbf{0.013} & 0.097 & 0.108 \\\\\n\\midrule\n\\multirow{5}{*}{B: Outcome}\n & Naive & 0.189 & 0.197 & 0.206 & 0.212 \\\\\n & Global & 0.185 & 0.208 & 0.204 & 0.228 \\\\\n & EC-HTE & 0.181 & 0.215 & 0.202 & 0.237 \\\\\n & PPCI & 0.015 & \\textbf{0.020} & 0.171 & 0.176 \\\\\n & EC-HTE+PPCI & \\textbf{0.012} & 0.023 & 0.171 & 0.186 \\\\\n\\midrule\n\\multirow{5}{*}{C: Both}\n & Naive & 0.251 & 0.135 & 0.267 & 0.155 \\\\\n & Global & 0.182 & 0.209 & 0.233 & 0.235 \\\\\n & EC-HTE & 0.179 & 0.216 & 0.224 & 0.262 \\\\\n & PPCI & 0.017 & 0.007 & 0.241 & 0.232 \\\\\n & EC-HTE+PPCI$^\\star$ & \\textbf{0.007} & \\textbf{0.008} & 0.209 & 0.223 \\\\\n\\midrule\n\\multirow{5}{*}{D: None}\n & Naive & \\textbf{0.007} & 0.003 & 0.060 & 0.065 \\\\\n & Global & 0.010 & \\textbf{0.002} & 0.061 & 0.071 \\\\\n & EC-HTE & 0.013 & 0.007 & 0.062 & 0.079 \\\\\n & PPCI & \\textbf{0.007} & \\textbf{0.003} & 0.060 & 0.065 \\\\\n & EC-HTE+PPCI & 0.013 & 0.007 & 0.062 & 0.079 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe complementarity of EC-HTE and PPCI follows from the distinct error sources they correct: EC-HTE addresses misclassification in the effect modifier $Z$ (covariate space), while PPCI corrects specification error in the outcome model $f(X)$ (prediction space).\nSince covariate misclassification and outcome model error are algebraically independent in the potential outcomes framework, their corrections compose without interference---confirmed by the 4-DGP orthogonal design (Table~\\ref{tab:ppci}), where DGP~C (both errors present) yields the largest bias reduction from the combined approach.\nUnder covariate error only, PPCI adds nothing; under no error, all methods perform equivalently.\n\n\\section{Real-Data Case Study: Hate Speech Detection}\n\\label{app:hatespeech}\n\nWe apply EC-HTE to the UC Berkeley Measuring Hate Speech corpus~\\cite{kennedy2020constructing}, annotating 2{,}496 comments for dehumanization using GPT-4.1.\nFour text-feature subgroups are defined by crossing platform (Reddit/Gab vs.\\ Twitter/YouTube) and text length (above/below median), yielding balanced groups ($n \\approx 624$ each).\n\n\\paragraph{Positive finding: real-world heterogeneity.}\nPer-subgroup misclassification rates range from 0.266 to 0.383, confirming heterogeneity ($\\Delta\\pi = 0.117$) in a real annotation setting.\nAt the error-type level, FPR ranges from 8.5\\% to 21.3\\% across text-feature subgroups, demonstrating that subgroup-varying misclassification is not an artifact of synthetic design but arises naturally in real NLP annotation tasks.\n\n\\paragraph{Boundary condition: statistical power at extreme FNR.}\nCorrection results are inconclusive: all corrected confidence intervals contain zero, and point estimate differences between methods are not statistically significant.\nThe high baseline FNR (53.3\\%) amplifies variance through matrix inversion (variance amplification factor up to 15.7$\\times$), rendering the comparison underpowered.\nWhen $P(\\hat{Z}{=}1 \\mid Z{=}1) \\approx 0.5$, the confusion matrix approaches singularity, and inversion amplifies estimation noise regardless of stratification strategy.\nThis complements the expert budget threshold identified in Appendix~\\ref{sec:budget}: EC-HTE requires \\emph{both} sufficient expert labels \\emph{and} sufficient baseline classifier quality.\n\n\\paragraph{Diagnostic connection.}\nThe diagnostic criterion ($\\Delta\\pi \\times \\Delta\\tau$, Section~\\ref{sec:diagnostic}) identifies when correction is worthwhile under moderate baseline accuracy.\nThis case study illustrates that even when $\\Delta\\pi$ is large, extreme baseline error renders correction underpowered rather than beneficial.\nA practical prerequisite is that the per-subgroup confusion matrix condition number $\\kappa(\\hat{C}_s)$ remain moderate; when $\\kappa > 50$, as observed here, practitioners should prioritize improving annotation quality before applying any matrix-inversion-based correction.\n\n\\section{Cross-Model Consistency}\n\\label{app:multilm}\n\nWe evaluate whether misclassification heterogeneity is model-specific by annotating 500 TweetEval sentiment tweets with six OpenAI models spanning three generations.\nSix text-feature subgroups are defined by crossing hashtag presence and text length.\nSpearman rank correlations of per-subgroup error rates across all six subgroups range from $\\rho = 0.82$ to $1.00$, indicating that the subgroup error structure is consistent across architectures.\nTwo subgroups with $n \\leq 6$ exhibit zero misclassification across all models; excluding these yields four-point correlations that are directionally consistent but underpowered.%\n\\footnote{The filtered $\\Delta\\pi$ values in Table~\\ref{tab:multilm} serve as a robustness check independent of rank-order testing: all six models exceed $\\Delta\\pi > 0.05$ on the four retained subgroups.}\n\n\\begin{table}[t]\n\\centering\n\\caption{Effective misclassification heterogeneity ($\\Delta\\pi$) across six OpenAI models on TweetEval sentiment (500 tweets, filtered to 4 subgroups with $n \\geq 10$).}\n\\label{tab:multilm}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nModel & Effective $\\Delta\\pi$ & $> 0.05$? \\\\\n\\midrule\nGPT-3.5-Turbo & 0.198 & \\checkmark \\\\\nGPT-4-Turbo & 0.149 & \\checkmark \\\\\nGPT-4o-mini & 0.136 & \\checkmark \\\\\nGPT-5.4 & 0.114 & \\checkmark \\\\\nGPT-4.1 & 0.098 & \\checkmark \\\\\nGPT-4o & 0.080 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll six models exhibit effective $\\Delta\\pi > 0.05$ on the four retained subgroups (Table~\\ref{tab:multilm}), and 5 of 6 share the same worst subgroup (\\texttt{True\\_medium}: tweets with hashtags and medium text length).\nNewer models reduce absolute error rates but do not eliminate subgroup heterogeneity: GPT-5.4 achieves $\\Delta\\pi = 0.114$ compared to GPT-3.5-Turbo's $0.198$.\nThese results were obtained with a single API provider; open-source model validation appears in Appendix~\\ref{app:multilm_opensource}.\n\n\\section{Open-Source Multi-LLM Validation}\n\\label{app:multilm_opensource}\n\nWe evaluate four open-source LLMs (7B--9B parameter range) on 490 TweetEval sentiment tweets with $K{=}4$ subgroups defined by crossing hashtag presence and text length.\nTable~\\ref{tab:multilm_cm} reports the confusion matrix heterogeneity profile.\nAll four models exhibit $\\Delta\\pi > 0.05$, confirming that subgroup-heterogeneous misclassification is not specific to proprietary APIs.\nSubgroup error rankings are consistent across architectures: \\texttt{True\\_short} (short tweets with hashtags) has the lowest $\\pi_s$ in 3 of 4 models, while \\texttt{False\\_medium} (medium tweets without hashtags) has the highest.\n\n\\begin{table}[t]\n\\centering\n\\caption{Confusion matrix heterogeneity across four open-source LLMs ($K{=}4$, $N{=}490$ TweetEval tweets). $\\Delta\\pi$: max--min per-subgroup misclassification rate. Prop2: number of subgroups where the $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}) triggers.}\n\\label{tab:multilm_cm}\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\nModel & Acc.\\ & $\\Delta\\pi$ & Prop2 & Strongest \\\\\n\\midrule\nLlama-3.1-8B & 0.755 & 0.141 & 1/4 & True\\_short \\\\\nQwen-2.5-7B & 0.798 & 0.165 & 1/4 & True\\_short \\\\\nGemma-2-9B & 0.763 & 0.125 & 4/4 & True\\_medium \\\\\nMistral-7B & 0.802 & 0.134 & 0/4 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Semi-synthetic budget sweep.}\nWe run the full EC-HTE pipeline with $K{=}2$ subgroups and $\\Delta\\tau{=}0.3$, using each model's empirical confusion matrices.\nTable~\\ref{tab:multilm_budget} reports coverage and RMSE crossover points.\nEC-HTE restores near-nominal coverage from 0.714 (naive average) to 0.939 ($+$22.5 percentage points) at $n_{\\text{expert}}{=}1{,}000$, consistent across all four models.\nGlobal correction achieves comparable or lower RMSE than HB at all budgets under these moderate $\\Delta\\pi$ values, and the $K{=}4$ RMSE crossover never occurs---confirming the budget guidelines in Appendix~\\ref{sec:budget}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Semi-synthetic budget sweep ($K{=}2$, $\\Delta\\tau{=}0.3$, 50 MC runs\\protect\\footnote{Appendix experiments use 50 MC replications unless otherwise noted; all main-text results use 100.}). Coverage at selected expert budgets; RMSE crossover denotes the minimum expert budget at which HB EC-HTE achieves lower RMSE than the naive (uncorrected) estimator.}\n\\label{tab:multilm_budget}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nModel & $\\Delta\\pi_{K{=}2}$ & Naive Cov.\\ & HB Cov.\\ ($n{=}1000$) & Crossover \\\\\n\\midrule\nLlama-3.1-8B & 0.051 & 0.675 & 0.940 & $n{=}1000$ \\\\\nQwen-2.5-7B & 0.080 & 0.715 & 0.925 & $n{=}1000$ \\\\\nGemma-2-9B & 0.100 & 0.705 & 0.945 & $n{=}1000$ \\\\\nMistral-7B & 0.070 & 0.760 & 0.945 & $n{=}1000$ \\\\\n\\midrule\n\\textit{Average} & --- & \\textit{0.714} & \\textit{0.939} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Gemma boundary case.}\nGemma-2-9B triggers the Proposition~\\ref{prop:debiasing_hurts} diagnostic in all four $K{=}4$ subgroups due to extreme FPR--FNR asymmetry (\\texttt{False\\_medium} FNR $= 0.437$).\nAt small budgets ($K{=}4$, $n{=}100$), EC-HTE RMSE reaches 1.229 ($3.1\\times$ naive), illustrating the budget guideline from Appendix~\\ref{sec:budget}: when per-subgroup cell counts fall below 25, the variance cost of stratified correction dominates.\nAt $n \\geq 500$, EC-HTE coverage recovers to $>$0.90, consistent with the synthetic experiments.\n\n\\paragraph{Heterogeneous-$\\tau$ DGP.}\nTo assess whether the constant-$\\tau$ DGP understates EC-HTE's advantage, we run a supplementary experiment using Llama's empirical confusion matrices with heterogeneous treatment effects across subgroups ($\\Delta\\tau \\in [0.1, 0.6]$, $K{=}2$, 50 MC runs).\nEC-HTE achieves lower $|\\text{bias}|$ than global correction at all budgets ($n{=}500$: 0.010 vs.\\ 0.031, a 68\\% reduction).\nIn the high-$\\Delta\\tau$ subgroup (\\texttt{True\\_short}, $\\Delta\\tau{=}0.6$), EC-HTE also achieves lower RMSE ($n{=}1{,}000$: 0.212 vs.\\ 0.258, 18\\% improvement), confirming that the RMSE advantage concentrates in subgroups where correction is most needed.\nAggregate RMSE remains comparable to global correction because low-$\\Delta\\tau$ subgroups incur stratification variance without commensurate bias reduction, consistent with the budget guidelines in Appendix~\\ref{sec:budget}.\n\n\\section{Robustness to Subgroup Misspecification}\n\\label{app:robustness}\n\nEC-HTE requires pre-defined subgroup labels, which may be noisy in practice.\nWe test robustness by randomly flipping each observation's subgroup assignment with probability $p_{\\text{flip}} \\in \\{0, 0.10, 0.25, 0.50\\}$, across $K \\in \\{2, 4\\}$ (extreme regime, $n_{\\text{expert}} = 500$, $\\Delta\\tau = 0.3$, 100 MC runs).\n\n\\begin{table}[t]\n\\centering\n\\caption{95\\% CI coverage under subgroup misspecification noise. EC-HTE maintains near-nominal coverage across all noise levels.}\n\\label{tab:robustness}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{4}{c}{$p_{\\text{flip}}$} \\\\\n\\cmidrule(lr){2-5}\nMethod & 0.00 & 0.10 & 0.25 & 0.50 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{$K{=}2$, extreme}} \\\\\n\\quad Naive & 0.875 & 0.877 & 0.890 & 0.897 \\\\\n\\quad Global & 0.925 & 0.935 & 0.932 & 0.945 \\\\\n\\quad HB EC-HTE & 0.958 & 0.948 & 0.950 & 0.945 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{$K{=}4$, extreme}} \\\\\n\\quad Naive & 0.904 & 0.916 & 0.909 & 0.919 \\\\\n\\quad Global & 0.930 & 0.953 & 0.948 & 0.944 \\\\\n\\quad HB EC-HTE & 0.956 & 0.958 & 0.960 & 0.946 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE maintains coverage $\\geq 0.945$ across all configurations (Table~\\ref{tab:robustness}), while the naive estimator is systematically below nominal (0.875--0.919).\nAt $p_{\\text{flip}} = 0.50$, subgroup structure is effectively destroyed; EC-HTE converges to global correction (coverage and RMSE within 0.1\\%), confirming that hierarchical Bayesian shrinkage provides a built-in safety mechanism.\nFor $K{=}4$ at $p_{\\text{flip}} = 0.50$, a small residual RMSE gap persists ($p < 0.01$), reflecting the variance cost of estimating four confusion matrices even when they carry no signal.\n\n\\section{Monte Carlo Standard Errors}\n\\label{app:mcse}\n\nAll experiments use 100 independent Monte Carlo replications per configuration.\nAll simulation results were verified with 100 MC seeds; the median RMSE variation between 50-seed and 100-seed estimates is below 3.2\\%, confirming the stability of reported figures.\nWe report Monte Carlo standard errors to assess whether observed differences between methods are statistically reliable.\nFor exp-001 (synthetic DGP, no per-seed pairing across methods), we use conservative two-sample $z$-tests on the 100-run means.\nFor exp-003 (semi-synthetic TweetEval, shared seeds across methods), we use paired $t$-tests, which are more powerful because they control for seed-level variation.\n\nTable~\\ref{tab:mcse} reports paired comparisons for representative configurations.\nOf 1{,}020 total pairwise comparisons across all configurations, 742 (72.7\\%) are statistically significant at $\\alpha = 0.05$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Paired comparisons for representative configurations. $\\Delta$ = method A $-$ method B (negative favors A for $|\\text{bias}|$). Two-sample $z$-tests for synthetic (exp-001); paired $t$-tests for semi-synthetic (exp-003). Bold $p$-values indicate significance at $\\alpha = 0.05$.}\n\\label{tab:mcse}\n\\small\n\\begin{tabular}{llrr}\n\\toprule\nConfiguration & Comparison & $\\Delta$ & $p$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{HB EC-HTE vs.\\ Global ($|\\text{bias}|$)}} \\\\\n\\quad $K{=}2$/ext/$n{=}500$ & & $-0.046$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/ext/$n{=}500$ & & $-0.078$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/mod/$n{=}250$ & & $-0.017$ & $0.288$ \\\\\n\\quad TweetEval/ext/$n{=}250$ & & $+0.001$ & $0.395$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{HB EC-HTE vs.\\ Global (RMSE)}} \\\\\n\\quad $K{=}2$/ext/$n{=}500$ & & $+0.015$ & $0.179$ \\\\\n\\quad $K{=}4$/ext/$n{=}500$ & & $+0.048$ & $\\mathbf{0.011}$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{HB EC-HTE vs.\\ Naive ($|\\text{bias}|$)}} \\\\\n\\quad $K{=}2$/ext/$n{=}500$ & & $-0.089$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/ext/$n{=}500$ & & $-0.113$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/mod/$n{=}250$ & & $-0.031$ & $\\mathbf{0.038}$ \\\\\n\\quad TweetEval/ext/$n{=}250$ & & $+0.005$ & $\\mathbf{0.030}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder extreme heterogeneity, HB EC-HTE's bias advantage over global correction is highly significant ($p < 0.001$ for both $K{=}2$ and $K{=}4$).\nThe RMSE penalty of stratification is not significant at $K{=}2$ ($p = 0.179$) but reaches significance at $K{=}4$ ($p = 0.011$), consistent with the higher variance cost of estimating four confusion matrices.\nUnder moderate heterogeneity ($K{=}4$, $n{=}250$), the bias difference between HB and global is not significant ($p = 0.288$), confirming that EC-HTE's advantage requires sufficient error heterogeneity.\nIn the semi-synthetic TweetEval experiment, HB EC-HTE does not significantly improve over global ($p = 0.395$), consistent with moderate $\\Delta\\pi$ and unbalanced subgroup sizes.\nThe HB vs.\\ naive comparison in TweetEval is significant ($p = 0.030$) but favors naive, reflecting the variance cost of stratification when bias reduction is marginal.\n\n\\section{Semi-Real Confusion Matrix Validation}\n\\label{app:semireal}\n\nWe test EC-HTE with empirical asymmetric confusion matrices from the GPT-4.1 TweetEval pilot.\nFour text-feature subgroups ($K{=}4$) retain the real per-subgroup FPR and FNR from pilot annotations (Table~\\ref{tab:semireal_cm}); CATE heterogeneity is injected synthetically ($\\tau(z{=}0,s) = 0.3 + 0.1s$, $\\tau(z{=}1,s) = 0.8 - 0.15s$).\n$N{=}5{,}000$, $P(Z{=}1){=}0.18$, 100 MC seeds per $n_{\\text{expert}}$ level.\n\n\\begin{table}[t]\n\\centering\n\\caption{Empirical confusion matrices from GPT-4.1 TweetEval pilot.\nS0 exhibits FNR $= 0.526$, approaching chance-level classification.}\n\\label{tab:semireal_cm}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSubgroup & Weight & FPR & FNR & $\\kappa(\\hat{C}_s)$ \\\\\n\\midrule\nS0 & 0.38 & 0.054 & 0.526 & high \\\\\nS1 & 0.22 & 0.101 & 0.300 & moderate \\\\\nS2 & 0.14 & 0.143 & 0.308 & moderate \\\\\nS3 & 0.25 & 0.194 & 0.222 & low \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Semi-real confusion matrix results. RMSE and coverage averaged over subgroups and $z$-levels (100 MC runs). HB EC-HTE underperforms global at all budgets; S0's near-chance FNR drives the failure.}\n\\label{tab:semireal}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n$n_{\\text{expert}}$ & Method & RMSE $\\downarrow$ & Coverage $\\uparrow$ \\\\\n\\midrule\n\\multirow{4}{*}{100}\n & Oracle & 0.101 & 0.957 \\\\\n & Naive & 0.123 & 0.879 \\\\\n & Global & 0.263 & 0.885 \\\\\n & HB EC-HTE & 0.784 & 0.744 \\\\\n\\midrule\n\\multirow{4}{*}{250}\n & Oracle & 0.101 & 0.957 \\\\\n & Naive & 0.123 & 0.879 \\\\\n & Global & 0.232 & 0.909 \\\\\n & HB EC-HTE & 0.411 & 0.834 \\\\\n\\midrule\n\\multirow{4}{*}{500}\n & Oracle & 0.101 & 0.957 \\\\\n & Naive & 0.123 & 0.879 \\\\\n & Global & 0.196 & 0.922 \\\\\n & HB EC-HTE & 0.260 & 0.890 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHB EC-HTE produces higher RMSE and lower coverage than global correction at all expert budgets (Table~\\ref{tab:semireal}).\nThe root cause is S0's FNR $= 0.526$: when a confusion matrix row approaches a uniform distribution ($P(\\hat{Z}{=}1 \\mid Z{=}1) \\approx 0.5$), inversion amplifies estimation noise regardless of the expert budget.\nThis converges with the hate speech case study (Appendix~\\ref{app:hatespeech}, FNR $= 53.3$\\%) and confirms that EC-HTE requires \\emph{both} sufficient expert labels \\emph{and} sufficient baseline classifier quality per subgroup.\nThe singularity guard ($\\kappa > 100$, Section~\\ref{sec:method}) mitigates catastrophic failure by falling back to global correction for near-degenerate subgroups, but does not recover the bias reduction that motivates stratification.\nFor a $2 \\times 2$ symmetric confusion matrix, $\\kappa = 1/|1-2\\pi|$; $\\kappa > 100$ corresponds to $\\pi \\in (0.495, 0.505)$, so the guard triggers only when the classifier performs within $0.5\\%$ of random guessing.\nAt $n_{\\text{expert}} = 500$, HB EC-HTE narrows the gap (RMSE 0.260 vs.\\ 0.196) as confusion matrix estimates stabilize for the three well-classified subgroups, but the S0 bottleneck persists.\n\nA second semi-real experiment using GPT-3.5-Turbo confusion matrices (worst-subgroup FPR $= 0.39$, FNR $= 0.21$) yields similar results: HB RMSE exceeds global by 1.3--3.5$\\times$ at all budgets.\nHere the failure stems from high false-positive rates compounded by class imbalance ($P(Z{=}1) = 0.18$), which leaves insufficient expert observations in the positive class for reliable per-subgroup confusion matrix estimation.\nTogether, these experiments identify three applicability conditions for EC-HTE: (1)~sufficient effective expert budget ($n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$), (2)~no near-chance subgroup error rate ($\\max(\\text{FPR}_s, \\text{FNR}_s) < 0.5$), and (3)~adequate class balance in the effect modifier.\n\n\\paragraph{Diagnostic rule.}\nA logistic regression over all 368 semi-real experiment--budget cells (dependent variable: HB EC-HTE $<$ Global RMSE) identifies two sufficient statistics: the worst-subgroup confusion matrix condition number $\\kappa(\\hat{M}_s) \\leq 1.25$ and the effective minority-class expert count $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$.\nWhen both conditions hold, HB outperforms global in 93.3\\% of cells; when either is violated, global is preferred in 94.7\\% of cells.\nBoth exp-015 ($\\kappa = 2.38$, effective $n = 2.5$) and exp-016 ($\\kappa = 1.55$, effective $n = 2.5$) violate both conditions, and the diagnostic correctly predicts 100\\% of their failure cells.\nSubgroup-average metrics can mask cell-level heterogeneity: in exp-015, HB EC-HTE substantially reduces bias for the three well-classified subgroups (S1--S3) but amplifies variance in the near-degenerate subgroup (S0, FNR $= 0.526$), and the S0 penalty dominates the aggregate RMSE.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/applicability_frontier.pdf}\n\\caption{Applicability frontier of EC-HTE. Green region: EC-HTE reduces bias vs.\\ global correction. Yellow: comparable performance. Red: EC-HTE underperforms. Dashed lines mark the expert budget threshold ($n_{\\text{expert}}/K = 25$) and classifier quality threshold (worst-subgroup error rate $= 0.5$). Red diamonds show semi-real experiments with actual GPT-4.1 and GPT-3.5-Turbo confusion matrices.}\n\\label{fig:applicability}\n\\end{figure}\n\n\\section{Robustness: Estimator Choice and Treatment Effect Specification}\n\\label{app:rlearner}\n\nWe verify that EC-HTE's corrected pseudo-outcomes are compatible with downstream estimators beyond CausalForest by replacing it with the R-learner~\\citep{nie2021quasi}.\nThe experiment uses $K{=}2$, extreme heterogeneity, $n_{\\text{expert}} = 500$, and 50 MC seeds; the R-learner uses 5-fold cross-fitting with gradient-boosted trees as the base learner.\n\n\\begin{table}[t]\n\\centering\n\\caption{R-learner vs.\\ CausalForest with EC-HTE correction ($K{=}2$, extreme, $n{=}500$). $|\\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and seeds.}\n\\label{tab:rlearner}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nEstimator & Correction & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\n\\multirow{4}{*}{R-learner}\n & Oracle & 0.006 & 0.056 & 0.94 \\\\\n & Naive & 0.121 & 0.139 & 0.47 \\\\\n & Global & 0.098 & 0.123 & 0.72 \\\\\n & EC-HTE & \\textbf{0.013} & 0.080 & 0.92 \\\\\n\\midrule\n\\multirow{2}{*}{CausalForest}\n & Naive & 0.058 & 0.090 & 0.82 \\\\\n & EC-HTE & \\textbf{0.010} & 0.093 & 0.95 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE reduces R-learner $|\\text{bias}|$ by 89\\% (0.121 $\\to$ 0.013) and restores coverage from 0.47 to 0.92 (Table~\\ref{tab:rlearner}).\nThe bias reduction and coverage gains are comparable to those achieved with CausalForest, confirming that EC-HTE is compatible with a range of HTE estimators.\n\n\\paragraph{Multiplicative treatment effects.}\nWe further test robustness to the functional form of treatment effects by replacing the additive DGP with a multiplicative specification: $Y(1) = Y(0) \\times \\exp(\\tau(Z))$, using $K{=}2$, extreme heterogeneity, $n_{\\text{expert}} = 500$, and 50 MC seeds.\n\n\\begin{table}[t]\n\\centering\n\\caption{Multiplicative DGP results ($K{=}2$, extreme, $n{=}500$, 50 seeds). EC-HTE achieves comparable bias reduction and nominal coverage under non-additive treatment effects.}\n\\label{tab:multiplicative}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\nOracle & 0.003 & 0.038 & 0.96 \\\\\nNaive & 0.135 & 0.142 & 0.44 \\\\\nGlobal & 0.110 & 0.124 & 0.54 \\\\\nEC-HTE & \\textbf{0.054} & 0.068 & 0.955 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE reduces RMSE by 52\\% relative to naive (0.068 vs.\\ 0.142) and restores coverage to the nominal level (0.955; Table~\\ref{tab:multiplicative}).\nEC-HTE's bias correction operates at the confusion matrix level, independent of the downstream CATE estimator and functional form of treatment effects.\n\n\\section{Robustness to Class Imbalance}\n\\label{app:classimbalance}\n\nAssumption (A3) requires $P(Z{=}1) = 0.5$, but real-world effect modifiers are often imbalanced.\nWe sweep $P(Z{=}1) \\in \\{0.1, 0.2, 0.3, 0.4, 0.5\\}$ with $K \\in \\{2,4\\}$, extreme misclassification heterogeneity, $n_{\\text{expert}}{=}250$, and 100 MC seeds (Table~\\ref{tab:pz1_sweep}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Robustness to class imbalance ($n_{\\text{expert}}{=}250$, extreme heterogeneity). R$^2$: Theorem~\\ref{thm:bias_identity} fit. Ratio: HB/Global RMSE ($<1$ = HB wins). Cov.: HB EC-HTE 95\\% CI coverage.}\n\\label{tab:pz1_sweep}\n\\small\n\\begin{tabular}{cc ccc}\n\\toprule\n$P(Z{=}1)$ & $K$ & R$^2$ & Ratio & Cov. \\\\\n\\midrule\n0.1 & 2 & 0.998 & 0.92 & 0.94 \\\\\n0.2 & 2 & 0.989 & 0.76 & 0.94 \\\\\n0.3 & 2 & 0.994 & 0.78 & 0.94 \\\\\n0.4 & 2 & 0.995 & 0.87 & 0.94 \\\\\n0.5 & 2 & 0.995 & 0.86 & 0.93 \\\\\n\\midrule\n0.1 & 4 & 0.984 & 1.54 & 0.92 \\\\\n0.2 & 4 & 0.976 & 1.68 & 0.93 \\\\\n0.3 & 4 & 0.985 & 1.12 & 0.92 \\\\\n0.4 & 4 & 0.984 & 1.08 & 0.93 \\\\\n0.5 & 4 & 0.992 & 1.06 & 0.92 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTheorem~\\ref{thm:bias_identity}'s product form remains accurate across all imbalance levels: $R^2 \\geq 0.976$ even at $P(Z{=}1) = 0.1$, confirming that the bias identity derives from confusion matrix structure rather than class balance.\nFor $K{=}2$, EC-HTE outperforms global correction at all $P(Z{=}1)$ levels (RMSE ratio 0.76--0.92), degrading gracefully under severe imbalance.\nFor $K{=}4$, EC-HTE underperforms global at $n_{\\text{expert}}{=}250$ (ratio 1.06--1.68), consistent with the budget threshold $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$: at $P(Z{=}1){=}0.1$, $K{=}4$, each subgroup receives only ${\\sim}6$ minority-class labels.\nThe gap narrows as $P(Z{=}1)$ increases (1.54 $\\to$ 1.06), and coverage remains stable at 0.92--0.94 across all configurations.\n\n\\section{Comparison with PPI Correction}\n\\label{app:ppi_comparison}\n\nPPI~\\cite{angelopoulos2023ppi} constructs confidence intervals by combining a large set of ML predictions with a smaller set of gold-standard labels, using the gold labels to debias the ML-based estimator.\nApplied to our setting, PPI treats the LLM-annotated effect modifier as the ML prediction and the expert labels as the gold standard.\nTwo variants arise naturally: \\emph{PPI-global} pools all expert labels to estimate a single rectifier (analogous to our Global baseline), and \\emph{PPI-subgroup} estimates per-subgroup rectifiers (analogous to Stratified MLE).\n\nUnder the confusion-matrix parameterization we adopt, DSL's measurement error correction reduces to confusion matrix inversion.\nPooled DSL applies a single estimated confusion matrix to all subgroups, producing the same corrected label distribution as our Global baseline; per-subgroup DSL estimates a separate confusion matrix for each subgroup and inverts it independently, equivalent to our Stratified MLE.\nEC-HTE's contribution over both PPI-subgroup and per-subgroup DSL is hierarchical partial pooling: rather than estimating each subgroup's confusion matrix in isolation, EC-HTE places a shared prior across subgroups, borrowing strength to reduce variance while preserving subgroup-specific bias correction.\nThis mechanism is outside both the PPI and DSL frameworks.\n\nThe key difference between PPI and confusion-matrix inversion is that PPI does not invert the confusion matrix; instead, it uses the gold labels to directly debias the estimand.\nThis avoids the matrix inversion step that can amplify noise at small $n_{\\text{expert}}$, but it also means PPI cannot exploit the structure of the misclassification process to reduce bias.\nPPI-global inherits the same $\\Delta\\pi \\times \\Delta\\tau$ bias amplification as Global correction (Theorem~\\ref{thm:bias_identity}), confirming that the ``debiasing hurts'' mechanism operates regardless of the inference framework.\n\n\\section{Civil Comments Validation}\n\\label{app:civilcomments}\n\nTo verify that subgroup-heterogeneous misclassification generalizes beyond TweetEval, we annotate $N{=}3{,}000$ stratified samples (30\\% toxic) from Civil Comments~\\cite{borkan2019nuanced}, a toxicity detection dataset.\nSubgroups are defined by \\texttt{text\\_length\\_bin} $\\times$ \\texttt{has\\_question} ($K{=}4$): S0 (long, no question, 38.8\\%), S1 (long, question, 11.4\\%), S2 (short, no question, 33.7\\%), S3 (short, question, 16.1\\%).\nSubgroup features were chosen a priori based on observable text properties; no feature search was performed.\nThree proprietary LLMs annotate each sample via an OpenAI-compatible API, yielding 800--900 valid annotations per model.\n\nTable~\\ref{tab:civil_cm} reports per-subgroup FPR and FNR.\nWe define $\\Delta\\pi = \\max_s \\pi_s - \\min_s \\pi_s$, where $\\pi_s$ is the overall misclassification rate for subgroup $s$.\nAll three models exhibit $\\Delta\\pi > 0.05$, with overall heterogeneity $\\Delta\\pi \\in [0.113, 0.160]$---comparable to the $\\Delta\\pi \\in [0.125, 0.165]$ observed across four open-source LLMs on TweetEval (Appendix~\\ref{app:multilm_opensource}).\nGPT-4o-mini and GPT-3.5-turbo show pronounced FPR/FNR asymmetry (e.g., GPT-4o-mini FPR $\\in [0.42, 0.61]$ vs.\\ FNR $\\in [0.05, 0.16]$), indicating systematic over-prediction of toxicity; their FPR approaches 0.5, placing them in the ill-conditioned regime where confusion matrix inversion amplifies noise (consistent with the classifier quality threshold discussed in the Limitations section).\nThe consistent presence of $\\Delta\\pi$ heterogeneity across two NLP tasks, seven LLMs spanning open-source (7B--9B) and proprietary families, and two distinct subgroup definitions confirms that this phenomenon is a structural property of LLM annotation rather than an artifact of a specific dataset or model.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-subgroup misclassification rates on Civil Comments ($K{=}4$). $\\Delta$ denotes max $-$ min across subgroups.}\n\\label{tab:civil_cm}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Metric & S0 & S1 & S2 & S3 & $\\Delta$ \\\\\n\\midrule\nGPT-4o & FPR & 0.249 & 0.157 & 0.213 & 0.341 & 0.184 \\\\\n       & FNR & 0.160 & 0.263 & 0.308 & 0.328 & 0.168 \\\\\n\\midrule\nGPT-4o-mini & FPR & 0.517 & 0.541 & 0.419 & 0.610 & 0.191 \\\\\n            & FNR & 0.052 & 0.105 & 0.074 & 0.160 & 0.108 \\\\\n\\midrule\nGPT-3.5-turbo & FPR & 0.400 & 0.473 & 0.374 & 0.468 & 0.099 \\\\\n              & FNR & 0.139 & 0.211 & 0.173 & 0.240 & 0.101 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Bias Identity Validation with Real Confusion Matrices}\n\\label{app:realcm_bias}\n\nTheorem~\\ref{thm:bias_identity} is derived under symmetric misclassification (A2); real LLM confusion matrices are asymmetric (FPR $\\neq$ FNR).\nWe verify that the generalized identity $\\mathrm{bias}(z,s) = \\Delta\\tau \\cdot [B_s]_{z,1}$ (Remark~\\ref{thm:bias_identity}) holds under real annotation error structures by running semi-synthetic simulations ($N{=}5{,}000$, $K{=}4$, $\\Delta\\tau{=}0.30$, 100 MC runs) with confusion matrices drawn from 11 LLM--dataset combinations: eight models on TweetEval (GPT-4-turbo, GPT-4o, GPT-4.1, GPT-4o-mini, GPT-3.5-turbo, Qwen2.5-7B, Mistral-7B, Gemma-2-9B) and three on Civil Comments (GPT-4o, GPT-4o-mini, GPT-3.5-turbo).\n\nTable~\\ref{tab:realcm_r2} reports per-model $R^2$ from regressing observed subgroup bias on the predicted value $\\Delta\\tau \\cdot [B_s]_{z,1}$.\nThe aggregate $R^2 = 0.975$; 10 of 11 combinations achieve $R^2 \\geq 0.93$.\nThe single outlier (GPT-4o-mini on Civil Comments, $R^2{=}0.76$) has near-homogeneous subgroup error rates ($\\max|[B_s]_{z,1}| = 0.089$), so predicted biases are small and Monte Carlo noise dominates the regression.\n$R^2$ correlates strongly with $\\max|[B_s]_{z,1}|$: models with more heterogeneous per-subgroup error rates produce larger bias signals that are easier to verify empirically.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bias identity $R^2$ with real LLM confusion matrices ($K{=}4$, 100 MC runs).}\n\\label{tab:realcm_r2}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nModel & Dataset & $R^2$ & $\\max|[B_s]_{z,1}|$ \\\\\n\\midrule\nGPT-4-turbo  & TweetEval & 0.993 & 0.328 \\\\\nQwen2.5-7B   & TweetEval & 0.990 & 0.272 \\\\\nMistral-7B   & TweetEval & 0.990 & 0.242 \\\\\nGemma-2-9B   & TweetEval & 0.982 & 0.185 \\\\\nGPT-4o       & Civil Comments & 0.979 & 0.198 \\\\\nGPT-4o       & TweetEval & 0.975 & 0.240 \\\\\nGPT-4.1      & TweetEval & 0.969 & 0.139 \\\\\nGPT-3.5-turbo & TweetEval & 0.948 & 0.087 \\\\\nGPT-3.5-turbo & Civil Comments & 0.935 & 0.170 \\\\\nGPT-4o-mini  & TweetEval & 0.929 & 0.170 \\\\\nGPT-4o-mini  & Civil Comments & 0.756 & 0.089 \\\\\n\\midrule\n\\multicolumn{2}{l}{All (pooled)} & 0.975 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Applicability Screening with Real LLM Confusion Matrices}\n\\label{app:screening}\n\nWe apply the diagnostic conditions from Proposition~\\ref{prop:debiasing_hurts} and Section~\\ref{sec:method} to 16 LLM--dataset--$K$ combinations spanning seven LLMs (four open-source, three proprietary) across TweetEval and Civil Comments.\nTable~\\ref{tab:screening} summarizes which conditions each combination satisfies.\n\n\\begin{table}[h]\n\\centering\n\\caption{Diagnostic screening of 16 LLM--dataset--$K$ combinations. Columns report whether all subgroups satisfy each condition. Budget assumes $n_{\\text{expert}}{=}500$.}\n\\label{tab:screening}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Dataset & $K$ & $\\kappa{\\leq}1.25$ & $\\max{\\leq}0.5$ & Budget & Pass all \\\\\n\\midrule\nGemma-2-9B   & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nLlama-3.1-8B & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nMistral-7B   & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nQwen2.5-7B   & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGemma-2-9B   & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nLlama-3.1-8B & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nMistral-7B   & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nQwen2.5-7B   & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-3.5-turbo & CivilComm. & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-3.5-turbo & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4-turbo  & TweetEval & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4.1      & TweetEval & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o       & CivilComm. & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o       & TweetEval & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o-mini  & CivilComm. & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o-mini  & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nNo combination passes all three conditions; the bottleneck is $\\kappa(C_s) \\leq 1.25$, which requires $\\mathrm{FPR}_s + \\mathrm{FNR}_s \\lesssim 0.20$ for all subgroups---a threshold no current LLM achieves uniformly.\nThe closest are Qwen2.5-7B True\\_short ($\\kappa{=}1.23$) and Mistral-7B True\\_short ($\\kappa{=}1.27$).\n\nUnder a relaxed ``oracle screening'' that excludes near-degenerate subgroups ($\\max(\\mathrm{FPR}_s, \\mathrm{FNR}_s) \\geq 0.4$), we run semi-synthetic CATE estimation ($N{=}5{,}000$, $\\Delta\\tau{=}0.3$, 100 MC runs, $n_{\\text{expert}} \\in \\{250, 500\\}$) with each LLM's real per-subgroup confusion matrix.\nEC-HTE (HB) achieves lower RMSE than global correction in 41 of 52 comparisons (79\\%) and lower RMSE than stratified MLE in 52 of 52 comparisons (100\\%).\nThe four open-source LLMs on TweetEval show the strongest EC-HTE advantage (32/32 comparisons, RMSE reduction 0.001--0.008), while GPT-3.5-turbo/TweetEval (high FPR asymmetry, $\\mathrm{FPR}_{\\max}{=}0.39$) and GPT-4o/Civil Comments (low minority prevalence $P(Z{=}1){=}0.3$) show degradation.\nThe diagnostic correctly identifies the strict applicability regime; under relaxed conditions excluding near-degenerate subgroups, EC-HTE improves RMSE in 79\\% of comparisons.\n\n\\paragraph{Diagnostic Applicability Analysis.}\nThe diagnostic (Proposition~\\ref{prop:debiasing_hurts}) degrades on real LLM confusion matrices (pooled AUC $= 0.63$) because the failure mode is systematic: subgroups where the true CATE heterogeneity $\\tau_s \\approx 0$ are hurt by global correction (since $\\delta_s \\neq 0$ still introduces bias), yet these subgroups produce low diagnostic scores---the diagnostic ranks them as safe precisely when they are most vulnerable to overcorrection.\n\nA simple meta-criterion recovers reliability: compute $\\max_s |\\delta_s| / ((1 - 2\\bar{\\pi}) \\cdot \\pi_s)$ across subgroups.\nWhen $\\max_s \\mathrm{score}(s) > 1$, at least one subgroup is definitively harmed by global correction, and the diagnostic achieves AUC $\\geq 0.75$ across all 5 model--dataset combinations satisfying this condition (AUC range: 0.75--1.0).\nWhen $\\max_s \\mathrm{score}(s) \\leq 1$, global correction may or may not hurt depending on unobservable $\\Delta\\tau$; the diagnostic achieves AUC only 0.0--0.67 across the remaining 7 combinations (4 of 7 have AUC $< 0.5$, indicating anti-prediction).\nThis threshold perfectly separates reliable from unreliable diagnostic regimes across all 16 real LLM--dataset combinations evaluated.\n\nWe recommend the following practical protocol: (i) estimate per-subgroup confusion matrices from expert labels; (ii) compute $\\max_s \\mathrm{score}(s)$; (iii) if $> 1$, the diagnostic reliably identifies which subgroups are harmed by global correction---apply EC-HTE; (iv) if $\\leq 1$, the diagnostic is unreliable and practitioners should either default to EC-HTE as a conservative choice or evaluate correction strategies using held-out expert labels.\n\n\\section{Plug-in Standard Error Validation}\n\\label{app:bootstrap_se}\n\nA natural concern is whether the plug-in standard error adequately captures estimation uncertainty, particularly the additional variance introduced by confusion matrix estimation.\nWe verify this for the difference-in-means (DIM) estimator via Monte Carlo simulation ($K{=}2$, $n_{\\text{expert}} \\in \\{50, 100, 250, 500\\}$, 50 replications per budget level).\nAt each budget, we compute the plug-in 95\\% confidence interval and record empirical coverage.\nAcross all expert budgets, the plug-in SE yields coverage $\\geq 0.96$ (0.970, 0.960, 0.970, 0.970 for $n_{\\text{expert}} = 50, 100, 250, 500$), confirming that the analytic variance estimate is well-calibrated for the DIM estimator.\nThis self-calibration arises because the same noise in $\\hat{M}^{-1}$ that inflates point-estimate variance also inflates the plug-in SE, producing conservative intervals that maintain nominal coverage.\n\n\\paragraph{CausalForestDML.}\nUnder $K{=}2$ extreme heterogeneity ($\\pi{=}[0.05, 0.25]$, $n_{\\text{expert}}{=}250$, $n_{\\text{estimators}}{=}200$, 20 MC runs), EC-HTE plug-in SE achieves 93.8\\% aggregate coverage---close to the 94--96\\% oracle coverage (Table~\\ref{tab:cf_oracle}).\nThe high-error subgroup ($s_1$, $\\pi{=}0.25$) shows slightly lower plug-in coverage (92.5\\%) than the low-error subgroup ($s_0$: 95.0\\%), reflecting the larger $M^{-1}$ amplification of estimation uncertainty in subgroups with higher misclassification rates.\nBy contrast, the DIM plug-in SE achieves $\\geq$95\\% coverage in the same DGP, confirming that the analytic confusion matrix propagation formula is adequate for simpler estimators.\n\n\\paragraph{Full bootstrap SE.}\nA \\emph{full} bootstrap---resampling all $N$ observations and re-estimating both the confusion matrix and CausalForest per bootstrap replicate ($B{=}100$, $n_{\\text{estimators}}{=}200$, 20 MC runs)---confirms that plug-in SE is already near-nominal under standard hyperparameters.\nUnder $K{=}2$ extreme heterogeneity ($\\pi{=}[0.05, 0.25]$, $n_{\\text{expert}}{=}250$), plug-in SE achieves 93.8\\% aggregate coverage; the full bootstrap improves this to exactly 95.0\\% ($+$1.2pp).\nTable~\\ref{tab:bootstrap_se} reports per-subgroup results.\n\n\\begin{table}[h]\n\\centering\n\\caption{CausalForest coverage: plug-in SE vs.\\ full bootstrap SE ($B{=}100$, $n_{\\text{estimators}}{=}200$, 20 MC runs). Bootstrap SE is ${\\sim}1.15\\times$ plug-in.}\n\\label{tab:bootstrap_se}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nSubgroup & Plugin Cov. & Boot.\\ Cov. & Oracle Cov. & Plugin SE & Boot.\\ SE \\\\\n\\midrule\n$s_0$ ($\\pi{=}0.05$) & 0.950 & 0.925 & 0.925 & 0.059 & 0.063 \\\\\n$s_1$ ($\\pi{=}0.25$) & 0.925 & \\textbf{0.975} & 0.875 & 0.087 & 0.103 \\\\\n\\midrule\nAggregate & 0.938 & \\textbf{0.950} & 0.900 & 0.073 & 0.083 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe high-error subgroup ($s_1$) benefits most: coverage rises from 92.5\\% to 97.5\\% ($+$5.0pp), because the bootstrap captures the additional variance from $M^{-1}$ amplification.\nOracle coverage (90.0\\%) is consistent with the 94\\% reported in the oracle decomposition (Table~\\ref{tab:cf_oracle}), with the difference attributable to MC sampling noise at 20 runs.\nThe computational cost is substantial ($B \\times$ CF fits per MC run), but the approach is straightforward when exact nominal coverage is required.\n\n\\paragraph{Finite-sample remainder.}\nBy first-order matrix perturbation, $\\hat{C}_s^{-1} = C_s^{-1} - C_s^{-1} E_s C_s^{-1} + O(\\|E_s\\|^2)$, where $E_s = \\hat{C}_s - C_s$ satisfies $\\|E_s\\| = O_p(n_{\\text{expert}}^{-1/2})$.\nThe remainder in the corrected CATE is therefore $R_n = O_p(n_{\\text{expert}}^{-1/2} \\cdot \\|C_s^{-1}\\|^2) = O_p(n_{\\text{expert}}^{-1/2} \\cdot \\kappa(C_s))$, since $\\|C_s^{-1}\\| = O(\\kappa(C_s))$ for stochastic matrices.\nThis motivates the $\\kappa > 100$ singularity guard (Section~\\ref{sec:method}).\n\n\\subsection{CausalForest Oracle Coverage Decomposition}\n\\label{app:cf_oracle}\n\nTo isolate the source of CausalForest under-coverage, we compare six estimation strategies that progressively remove sources of uncertainty: (1)~Oracle (true $Z$, no correction), (2)~EC-HTE with true $C_s$, (3)~EC-HTE with estimated $\\hat{C}_s$ (HB), (4)~Global with true $\\bar{C}$, (5)~Global with estimated $\\hat{\\bar{C}}$, and (6)~Naive.\nTable~\\ref{tab:cf_oracle} reports coverage, $|\\text{bias}|$, and RMSE across three DGP configurations (100 MC runs each).\n\n\\begin{table}[h]\n\\centering\n\\caption{CausalForest oracle coverage decomposition. Coverage averaged over subgroups and $z$-levels.}\n\\label{tab:cf_oracle}\n\\small\n\\begin{tabular}{ll ccc}\n\\toprule\nDGP & Method & Cov.\\ (\\%) & $|\\text{Bias}|$ & RMSE \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{$K{=}4$, extreme\\\\$n{=}500$}}\n & Oracle (true $Z$)       & 94.5 & 0.006 & 0.078 \\\\\n & EC-HTE true $C_s$       & 92.5 & 0.008 & 0.114 \\\\\n & EC-HTE est.\\ $\\hat{C}_s$ & 93.1 & 0.015 & 0.121 \\\\\n & Global true $\\bar{C}$   & 91.3 & 0.037 & 0.110 \\\\\n & Global est.\\ $\\hat{\\bar{C}}$ & 91.1 & 0.038 & 0.111 \\\\\n & Naive                    & 88.3 & 0.045 & 0.095 \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{$K{=}2$, extreme\\\\$n{=}250$}}\n & Oracle (true $Z$)       & 94.0 & 0.002 & 0.056 \\\\\n & EC-HTE true $C_s$       & 94.0 & 0.003 & 0.073 \\\\\n & EC-HTE est.\\ $\\hat{C}_s$ & 92.5 & 0.004 & 0.079 \\\\\n & Global true $\\bar{C}$   & 88.5 & 0.045 & 0.083 \\\\\n & Global est.\\ $\\hat{\\bar{C}}$ & 88.3 & 0.045 & 0.085 \\\\\n & Naive                    & 82.8 & 0.046 & 0.077 \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{$K{=}2$, MF2 DGP\\\\$\\tau{=}(0.10,0.40)$}}\n & Oracle (true $Z$)       & 96.0 & 0.077 & 0.091 \\\\\n & EC-HTE true $C_s$       & 91.3 & 0.103 & 0.112 \\\\\n & EC-HTE est.\\ $\\hat{C}_s$ & 92.3 & 0.100 & 0.111 \\\\\n & Global true $\\bar{C}$   & 95.0 & 0.107 & 0.114 \\\\\n & Global est.\\ $\\hat{\\bar{C}}$ & 94.3 & 0.105 & 0.114 \\\\\n & Naive                    & 77.3 & 0.120 & 0.125 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree findings emerge.\nFirst, oracle coverage is 94--96\\% across all DGPs, confirming that CausalForest plug-in SE is well-calibrated when labels are correct.\nSecond, EC-HTE with true $C_s$ achieves 91--94\\% coverage---a 0--5pp gap from oracle (configuration-dependent), reflecting $M^{-1}$ SE propagation asymmetry across DGPs rather than confusion matrix estimation error.\nThird, the gap between true and estimated $C_s$ is ${\\leq}$1.5pp ($K{=}2$) and $<$1pp ($K{=}4$), confirming that CM estimation uncertainty contributes negligibly at $n_{\\text{expert}} \\geq 250$.\n\n\\section{Robustness to Assumption Violations}\n\\label{app:a5_violation}\n\n\\subsection{Assumption (A5): Subgroup-Specific Treatment Effects}\n\n\\begin{corollary}[Subgroup-Specific Treatment Effect Heterogeneity]\n\\label{cor:a5_relaxation}\nWhen $\\Delta\\tau$ varies across subgroups ($\\Delta\\tau_s = \\tau_s(1) - \\tau_s(0)$), the bias of global correction in subgroup $s$ at level $z{=}0$ is $+\\delta_s \\cdot \\Delta\\tau_s / (1 - 2\\bar{\\pi})$, and at level $z{=}1$ is $-\\delta_s \\cdot \\Delta\\tau_s / (1 - 2\\bar{\\pi})$.\n\\end{corollary}\nThe proof follows directly from Theorem~\\ref{thm:bias_identity} with $\\tau_s$ replacing $\\tau$.\n\nOur main analysis assumes that subgroup misclassification rates $\\delta_s$ and subgroup CATE magnitudes $\\Delta\\tau_s$ are independent (Assumption A5).\nIn practice, both may depend on text features that define subgroups, introducing correlation.\nWe test robustness under two configurations with the DIM estimator ($K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 50 MC replications, $\\pi = [0.05, 0.25]$):\n\\emph{aligned} (positive $\\delta_s$--$\\Delta\\tau_s$ correlation: high-error S1 has the larger treatment effect, $\\Delta\\tau = [0.30, 0.70]$) and\n\\emph{adversarial} (negative correlation: high-error S1 has the smaller effect, $\\Delta\\tau = [0.70, 0.30]$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Coverage and $|\\text{bias}|$ under A5 violation ($K{=}2$, $n_{\\text{expert}}{=}250$, 50 MC). Target coverage: 0.95.}\n\\label{tab:a5_violation}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nConfig & Method & S0 cov & S1 cov & S0 $|\\text{bias}|$ & S1 $|\\text{bias}|$ \\\\\n\\midrule\n\\multirow{4}{*}{Aligned}\n & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\\\\n & Naive         & 0.93 & 0.25 & 0.022 & 0.174 \\\\\n & Global        & 0.93 & 0.82 & 0.036 & 0.094 \\\\\n & EC-HTE (EB)   & 0.95 & 0.95 & 0.005 & 0.017 \\\\\n\\midrule\n\\multirow{4}{*}{Adversarial}\n & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\\\\n & Naive         & 0.90 & 0.78 & 0.042 & 0.074 \\\\\n & Global        & 0.74 & 0.93 & 0.098 & 0.040 \\\\\n & EC-HTE (EB)   & 0.94 & 0.96 & 0.002 & 0.007 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn the aligned configuration, the $\\delta_s \\times \\Delta\\tau_s$ product is maximized in the high-error subgroup, causing naive S1 coverage to collapse to 0.25.\nGlobal correction improves S1 but cannot fully correct without subgroup-specific error rates.\nIn the adversarial configuration, global correction overcorrects the low-error subgroup (S0 coverage 0.74).\nEC-HTE (EB) maintains $\\geq 0.94$ coverage across both subgroups in both configurations, with bias comparable to the oracle.\nResults at $n_{\\text{expert}}{=}500$ are consistent (all EC-HTE coverages $\\in [0.93, 0.99]$).\n\n\\subsection{Assumption (A1): Sensitivity to Outcome-Dependent Misclassification}\n\\label{app:a1_sensitivity}\n\nWe assess EC-HTE's robustness when misclassification depends on potential outcomes, violating~(A1).\nWe modify the synthetic DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$) so that misclassification probability becomes outcome-dependent: $P(\\hat{Z}{\\neq}Z \\mid Z, S, Y) = \\mathrm{clamp}(\\pi_s + \\gamma \\cdot (Y - \\mu_Y)/\\sigma_Y,\\, 0,\\, 1)$, where $\\gamma \\in \\{0, 0.05, 0.10, 0.15, 0.20\\}$ controls the strength of violation.\nTable~\\ref{tab:a1_sensitivity} reports results averaged over 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{Sensitivity to Assumption~(A1) violation. Coverage and $|\\text{bias}|$ under outcome-dependent misclassification ($\\gamma > 0$).}\n\\label{tab:a1_sensitivity}\n\\small\n\\begin{tabular}{lccc ccc}\n\\toprule\n& \\multicolumn{3}{c}{Coverage (\\%)} & \\multicolumn{3}{c}{$|\\text{Bias}|$} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n$\\gamma$ & EC-HTE & Global & Naive & EC-HTE & Global & Naive \\\\\n\\midrule\n0.00 & 95.5 & 92.7 & 87.7 & 0.060 & 0.065 & 0.061 \\\\\n0.05 & 95.5 & 93.5 & 83.8 & 0.059 & 0.064 & 0.064 \\\\\n0.10 & 95.3 & 93.8 & 83.5 & 0.063 & 0.064 & 0.067 \\\\\n0.15 & 94.8 & 94.3 & 79.2 & 0.065 & 0.064 & 0.070 \\\\\n0.20 & 93.5 & 94.0 & 79.5 & 0.068 & 0.063 & 0.073 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE maintains near-nominal coverage ($\\geq$93.5\\%) across the full $\\gamma$ range, with $|\\text{bias}|$ increasing only 13.7\\% from $\\gamma{=}0$ to $\\gamma{=}0.2$.\nAll correction methods (Global, Stratified MLE, HB) maintain $\\geq$90\\% coverage, indicating that moderate (A1) violations do not catastrophically degrade confusion-matrix-based correction.\nThe naive estimator degrades most rapidly (coverage $-$8.2pp), consistent with outcome-dependent misclassification compounding the uncorrected label noise.\n\n\\subsection{Extension to Confounded Treatment Assignment}\n\\label{app:confounded_dgp}\n\nEC-HTE's confusion matrix correction operates on estimated CATEs regardless of how those estimates are produced.\nTo verify compatibility with observational (non-RCT) designs, we pair EC-HTE with an inverse probability weighted difference-in-means (IPW-DIM) estimator under confounded treatment assignment.\n\n\\paragraph{DGP.}\n$N{=}5{,}000$, $K{=}2$, $\\pi = [0.05, 0.25]$, $n_{\\text{expert}}{=}250$, 100 MC replications.\nA covariate $X \\sim \\mathcal{N}(0,1)$ confounds both treatment and outcome:\n$T \\sim \\text{Bernoulli}(\\sigma(\\beta X))$ with $\\beta{=}0.5$ (moderate confounding; propensity range $[0.38, 0.62]$),\n$Y = 1 + 0.5 Z + 0.3 X + \\tau(Z) \\cdot T + \\varepsilon$, $\\varepsilon \\sim \\mathcal{N}(0,1)$.\nTreatment effects are $\\tau(Z{=}0){=}0$, $\\tau(Z{=}1){=}0.3$.\nThe IPW-DIM estimator uses \\emph{oracle propensity} $e(X) = \\sigma(\\beta X)$, with propensity scores clipped to $[0.05, 0.95]$.\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE under confounded treatment assignment (IPW-DIM with oracle propensity, $\\beta{=}0.5$, 100 MC).}\n\\label{tab:confounded_dgp}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Coverage & RMSE & $|\\text{Bias}|$ \\\\\n\\midrule\nOracle (true $Z$ + IPW) & 0.943 & 0.061 & 0.048 \\\\\nHB EC-HTE              & 0.950 & 0.086 & 0.068 \\\\\nGlobal                  & 0.930 & 0.087 & 0.071 \\\\\nStrat MLE               & 0.950 & 0.087 & 0.069 \\\\\nNaive                   & 0.863 & 0.083 & 0.066 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE achieves 95.0\\% coverage, within 0.7pp of the oracle (94.3\\%), confirming that confusion matrix correction and propensity weighting compose without interference.\nThe improvement is most pronounced in the high-error subgroup ($\\pi{=}0.25$): EC-HTE coverage is 96.0\\% vs.\\ naive 78.5\\% ($+$17.5pp).\nGlobal coverage (93.0\\%) falls below the correction methods (95.0\\%), consistent with the cost of ignoring subgroup-level error heterogeneity even in the confounded setting.\n\n\\paragraph{Sensitivity to confounding strength and propensity estimation.}\nWe sweep $\\beta \\in \\{0.25, 0.5, 1.0, 2.0\\}$ and compare oracle propensity ($e(X) = \\sigma(\\beta X)$) with estimated propensity (logistic regression fit on $(X, T)$), yielding 8 configurations (100 MC each).\nTable~\\ref{tab:confounded_sweep} reports HB EC-HTE and naive coverage.\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE coverage across confounding strengths and propensity sources. The logistic regression propensity model is correctly specified; propensity misspecification is an orthogonal concern addressed by the IPW literature.}\n\\label{tab:confounded_sweep}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n$\\beta$ & Propensity & HB Coverage & Naive Coverage \\\\\n\\midrule\n0.25 & Oracle    & 0.963 & 0.848 \\\\\n0.25 & Estimated & 0.973 & 0.845 \\\\\n0.50 & Oracle    & 0.950 & 0.863 \\\\\n0.50 & Estimated & 0.958 & 0.858 \\\\\n1.00 & Oracle    & 0.958 & 0.898 \\\\\n1.00 & Estimated & 0.960 & 0.883 \\\\\n2.00 & Oracle    & 0.945 & 0.858 \\\\\n2.00 & Estimated & 0.948 & 0.858 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE maintains coverage $\\geq$94.5\\% across all 8 configurations, including strong confounding ($\\beta{=}2.0$, propensity range $[0.12, 0.88]$).\nThe oracle--estimated gap is $\\leq$1pp, confirming that propensity estimation error does not meaningfully degrade EC-HTE when the propensity model is correctly specified.\nThis validates that EC-HTE is robust to confounded treatment assignment when the propensity model is correctly specified.\n\n\\subsection{Empirical Comparison with Frazis--Loewenstein Correction}\n\\label{app:fl_comparison}\n\nWe empirically compare EC-HTE's confusion matrix inversion against the scalar attenuation correction of \\citet{frazis2003estimating} (F-L).\nThe F-L correction rescales the observed estimate as $\\hat{\\tau}_{\\text{FL}} = \\hat{\\tau}_{\\text{obs}} / (1 - 2\\bar{\\pi})$, where $\\bar{\\pi}$ is the (global or per-subgroup) misclassification rate.\nWe test two variants: F-L \\emph{scalar} (single global $\\bar{\\pi}$) and F-L \\emph{per-subgroup} ($\\pi_s$-specific rescaling).\nSetup: $K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, $\\pi{=}[0.05, 0.25]$ (extreme heterogeneity), $\\tau(z{=}0){=}0$, $\\tau(z{=}1){=}0.3$, 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{F-L correction vs.\\ EC-HTE under heterogeneous misclassification ($\\Delta\\pi{=}0.20$). Both F-L variants produce \\emph{higher} aggregate bias than the uncorrected estimator.}\n\\label{tab:fl_comparison}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Coverage \\\\\n\\midrule\nOracle         & 0.045 & 0.056 & 0.943 \\\\\nNaive          & 0.062 & 0.077 & 0.858 \\\\\nGlobal (CM inv)& 0.064 & 0.081 & 0.938 \\\\\nHB EC-HTE      & 0.064 & 0.086 & \\textbf{0.953} \\\\\nF-L Scalar     & 0.091 & 0.116 & 0.850 \\\\\nF-L Per-Subgroup & 0.112 & 0.158 & 0.838 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth F-L variants produce \\emph{higher} bias and RMSE than the naive estimator (F-L per-subgroup $|\\text{bias}|{=}0.112$ vs.\\ naive $0.062$), demonstrating that scalar attenuation cannot substitute for confusion matrix inversion under subgroup-heterogeneous misclassification.\nThe per-subgroup bias direction reveals the mechanism: F-L scalar over-corrects the low-error subgroup ($s_0$: mean bias ${=}+0.073$ vs.\\ naive $+0.005$, a $14.6\\times$ amplification), while F-L per-subgroup dramatically over-corrects the high-error subgroup ($s_1$: mean bias ${=}+0.160$).\nEC-HTE achieves near-zero per-subgroup bias ($s_0{:}\\,{+}0.006$, $s_1{:}\\,{+}0.001$) with nominal coverage (95.3\\%).\nThe root cause is structural: F-L's $1/(1{-}2\\pi)$ scaling amplifies each $z$-level estimate independently, whereas CM inversion simultaneously redistributes the cross-contamination between misclassified and correctly classified observations.\n\n\\subsection{End-to-End Validation with Asymmetric Confusion Matrices}\n\\label{app:asymmetric_endtoend}\n\nWe validate EC-HTE under strongly asymmetric confusion matrices ($\\text{FPR}/\\text{FNR}$ ratio up to $7{:}1$), simulating the error profile of GPT-4.1 on Civil Comments.\nSetup: $K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$; $s_0$: $\\text{FPR}{=}0.05$, $\\text{FNR}{=}0.02$ (low error); $s_1$: $\\text{FPR}{=}0.38$, $\\text{FNR}{=}0.054$ ($7{:}1$ ratio); 100 MC runs.\nWe compare EC-HTE using the full $2{\\times}2$ asymmetric CM (Remark~2) against the symmetric assumption ($\\text{FPR}{=}\\text{FNR}{=}\\pi_s$).\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE under asymmetric misclassification ($\\text{FPR}/\\text{FNR}$ up to $7{:}1$). The asymmetric formula improves coverage by $+1.5$pp and RMSE by $11.5\\%$.}\n\\label{tab:asymmetric_endtoend}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Coverage \\\\\n\\midrule\nOracle              & 0.045 & 0.056 & 0.943 \\\\\nEC-HTE (asymmetric) & 0.057 & 0.074 & \\textbf{0.945} \\\\\nNaive               & 0.059 & 0.073 & 0.870 \\\\\nGlobal (asymmetric) & 0.061 & 0.076 & 0.915 \\\\\nEC-HTE (symmetric)  & 0.062 & 0.083 & 0.930 \\\\\nGlobal (symmetric)  & 0.063 & 0.078 & 0.915 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE with the asymmetric formula achieves 94.5\\% coverage versus 93.0\\% under the symmetric assumption ($+1.5$pp), with RMSE improved from 0.083 to 0.074 ($-11.5\\%$).\nThe improvement concentrates in the high-error subgroup ($s_1$): asymmetric coverage is 93.0\\% vs.\\ symmetric 91.0\\%.\nPractitioners should estimate full $2 \\times 2$ confusion matrices rather than assuming symmetric misclassification, particularly when FPR and FNR differ substantially.\n\n\\subsection{Complementarity with LLM Calibration}\n\\label{app:calibration}\n\nTemperature or Platt scaling~\\cite{guo2017calibration} can reduce per-subgroup misclassification rates, but does not eliminate heterogeneity $\\Delta\\pi$.\nWe simulate calibration by shrinking per-subgroup rates from $\\pi{=}[0.05, 0.25]$ ($\\Delta\\pi{=}0.20$) to $\\pi{=}[0.08, 0.15]$ ($\\Delta\\pi{=}0.07$), testing whether EC-HTE remains necessary post-calibration.\nSetup: $K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{Calibration reduces $\\Delta\\pi$ but does not eliminate it; EC-HTE corrects the residual bias. Best coverage is achieved by combining both.}\n\\label{tab:calibration}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Coverage \\\\\n\\midrule\nOracle                    & 0.043 & 0.053 & 0.963 \\\\\nCalibrated + EC-HTE       & 0.055 & 0.069 & \\textbf{0.965} \\\\\nCalibrated + Global       & 0.055 & 0.068 & 0.963 \\\\\nCalibrated + Naive        & 0.051 & 0.064 & 0.913 \\\\\nUncalibrated + EC-HTE     & 0.064 & 0.084 & 0.938 \\\\\nUncalibrated + Global     & 0.069 & 0.085 & 0.920 \\\\\nUncalibrated + Naive      & 0.063 & 0.079 & 0.840 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCalibration alone improves naive coverage from 84.0\\% to 91.3\\% but does not reach the nominal 95\\%.\nCalibrated + EC-HTE achieves the highest coverage (96.5\\%), demonstrating that calibration and EC-HTE address orthogonal error sources: calibration reduces per-subgroup $\\pi_s$ while EC-HTE corrects the residual $\\delta_s$-driven bias from heterogeneity that persists post-calibration.\nPropensity estimation robustness under model misspecification is an orthogonal concern addressed by the IPW literature; EC-HTE as a downstream correction layer does not alter IPW behavior.\n",
    "structuredPatch": [
      {
        "oldStart": 1233,
        "oldLines": 7,
        "newStart": 1233,
        "newLines": 7,
        "lines": [
          " ",
          " \\begin{table}[h]",
          " \\centering",
          "-\\caption{EC-HTE coverage across confounding strengths and propensity sources. The logistic regression propensity model is correctly specified; propensity misspecification is an orthogonal concern addressed by the IPW literature.}",
          "+\\caption{EC-HTE coverage across confounding strengths and propensity sources. The logistic regression propensity model is correctly specified; propensity misspecification is a complementary concern addressed by the IPW literature.}",
          " \\label{tab:confounded_sweep}",
          " \\small",
          " \\begin{tabular}{cccc}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Edit · `toolu_01Mat8KkeYd3CFvV9HQrstHG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "old_string": "demonstrating that calibration and EC-HTE address orthogonal error sources",
  "new_string": "demonstrating that calibration and EC-HTE address complementary error sources"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "d94a0987-cc13-4d9e-9419-b227b95d61cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfTCbq1mJavYLkU3D8YAFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14448,
      "cache_read_input_tokens": 53368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14448
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-23T09:29:47.179Z_

<details><summary>↩ Tool result · `toolu_01Mat8KkeYd3CFvV9HQrstHG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "5ca9ee2c-a540-4405-a313-10b2334593d9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
    "oldString": "demonstrating that calibration and EC-HTE address orthogonal error sources",
    "newString": "demonstrating that calibration and EC-HTE address complementary error sources",
    "originalFile": "\\section{EC-HTE Procedure}\n\\label{app:algorithm}\n\n\\begin{algorithm}[t]\n\\caption{EC-HTE: Error-Corrected Heterogeneous Treatment Effects}\n\\label{alg:echte}\n\\begin{algorithmic}[1]\n\\Require Observations $\\{(Y_i, W_i, \\hat{Z}_i, X_i)\\}_{i=1}^N$; expert labels $\\{Z_j^*\\}_{j=1}^{n_{\\text{expert}}}$; subgroup map $S: \\mathcal{X} \\to \\{1,\\ldots,K\\}$\n\\Ensure Corrected CATE estimates $\\hat{\\tau}(z)$ with variance-adjusted CIs\n\\Statex\n\\State \\textbf{Preconditions:} verify $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$ and $\\max_s(\\text{FPR}_s, \\text{FNR}_s) < 0.5$; if either fails, use global correction\n\\Statex\n\\State \\textbf{Step 1: Estimate per-subgroup confusion matrices (HB)}\n\\For{$s = 1, \\ldots, K$}\n    \\State $C_s[j,\\cdot] \\sim \\mathrm{Dir}(\\alpha_0 \\cdot \\hat{C}_{\\text{global},j})$, \\; $\\alpha_0$ via empirical Bayes\n    \\State Gibbs sampler (4 chains, 4000 iter) on $\\{(\\hat{Z}_j, Z_j^*) : S_j = s\\}$\n    \\State $\\hat{C}_s \\gets$ posterior mean; verify $\\hat{R} < 1.01$\n\\EndFor\n\\Statex\n\\State \\textbf{Step 2: Correct observed outcome moments}\n\\For{$s = 1, \\ldots, K$}\n    \\If{$\\kappa(\\hat{C}_s) > 100$} $\\hat{C}_s \\gets \\bar{C}$ \\Comment{singularity guard}\n    \\EndIf\n    \\State $\\tilde{\\boldsymbol{\\mu}}_s \\gets \\hat{C}_s^{-1} \\hat{\\boldsymbol{\\mu}}_s$\n\\EndFor\n\\Statex\n\\State \\textbf{Step 3: CausalForestDML with variance-adjusted SEs}\n\\State Train CausalForest (honest splitting) on corrected outcome moments $\\tilde{\\boldsymbol{\\mu}}_s$\n\\State $\\mathrm{se}_{\\mathrm{adj},i} \\gets \\sqrt{\\mathrm{diag}(\\hat{C}_{S_i}^{-1}\\, \\mathrm{diag}(\\mathrm{se}_i^2)\\, \\hat{C}_{S_i}^{-\\top})}$\n\\State \\Return $\\hat{\\tau}(z)$ with 95\\% CIs from $\\mathrm{se}_{\\mathrm{adj}}$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\subsection{Condition Number Guard Ablation}\n\\label{app:kappa_ablation}\n\nThe singularity guard in Algorithm~\\ref{alg:echte} (line~6) falls back to global correction when $\\kappa(\\hat{C}_s) > 100$.\nWe verify that this threshold is not load-bearing by sweeping $\\kappa \\in \\{10, 25, 50, 100, 200, 500, 1000\\}$ under the standard DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 100 MC runs).\nAcross all configurations, the maximum observed condition number is $\\kappa_{\\max} = 1.89$ (mean 1.45, p99 1.89), providing a $53{\\times}$ safety margin below the $\\kappa{=}100$ threshold.\nConsequently, the guard never triggers at any tested threshold, and all $\\kappa$ values produce identical RMSE (HB: 0.076, Global: 0.077) and zero numerical instability.\nIn a stress test with near-random labeling ($\\pi_s \\approx 0.4$--$0.5$, $n_{\\text{expert}}{=}50$), the maximum condition number reaches 1{,}125, correctly triggering the $\\kappa{=}100$ guard and preventing catastrophic inversion.\nThe adaptive formula $\\kappa_{\\text{adapt}} = 10 \\sqrt{n_{\\text{expert}} / K}$ recovers $\\kappa{=}100$ for this regime and scales naturally with the estimation precision.\n\n\\section{Full Proof of Theorem~\\ref{thm:bias_identity}}\n\\label{app:derivation}\n\n\\paragraph{Setup.}\nUnder assumptions (A1)--(A4), the observed CATE in subgroup $s$ at effect-modifier level $z$ is\n\\begin{equation}\n\\tau_{\\text{obs}}(z, s) = \\sum_{z'} M_s[z, z'] \\cdot \\tau(z'),\n\\end{equation}\nwhere $M_s[z, z'] = P(Z{=}z' \\mid \\hat{Z}{=}z, S{=}s)$ is the mixing matrix.\nUnder (A2)--(A3), $M_s = \\bigl[\\begin{smallmatrix} 1-\\pi_s & \\pi_s \\\\ \\pi_s & 1-\\pi_s \\end{smallmatrix}\\bigr]$.\n\n\\paragraph{Global correction.}\nThe pooled mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s = \\bigl[\\begin{smallmatrix} 1-\\bar{\\pi} & \\bar{\\pi} \\\\ \\bar{\\pi} & 1-\\bar{\\pi} \\end{smallmatrix}\\bigr]$, with $\\bar{\\pi} = \\sum_s w_s \\pi_s$.\n\nGlobal correction applies $M_{\\text{global}}^{-1}$ to $\\tau_{\\text{obs}}(\\cdot, s)$:\n\\begin{equation}\n\\hat{\\tau}_{\\text{global}}(z, s) = [M_{\\text{global}}^{-1} M_s \\cdot \\boldsymbol{\\tau}]_z,\n\\end{equation}\nwhere $\\boldsymbol{\\tau} = [\\tau(0), \\tau(1)]^\\top$.\n\n\\paragraph{Bias computation.}\nThe bias is $\\hat{\\tau}_{\\text{global}}(z, s) - \\tau(z) = [(M_{\\text{global}}^{-1} M_s - I) \\boldsymbol{\\tau}]_z$.\n\nDirect computation gives:\n\\begin{equation}\nM_{\\text{global}}^{-1} = \\frac{1}{1 - 2\\bar{\\pi}} \\begin{bmatrix} 1-\\bar{\\pi} & -\\bar{\\pi} \\\\ -\\bar{\\pi} & 1-\\bar{\\pi} \\end{bmatrix}.\n\\end{equation}\nMultiplying by $M_s$:\n\\begin{equation}\n\\resizebox{.88\\columnwidth}{!}{$\\displaystyle\nM_{\\text{global}}^{-1} M_s = \\frac{1}{1-2\\bar{\\pi}} \\begin{bmatrix} (1{-}\\bar{\\pi})(1{-}\\pi_s) - \\bar{\\pi}\\pi_s & (1{-}\\bar{\\pi})\\pi_s - \\bar{\\pi}(1{-}\\pi_s) \\\\ -\\bar{\\pi}(1{-}\\pi_s) + (1{-}\\bar{\\pi})\\pi_s & -\\bar{\\pi}\\pi_s + (1{-}\\bar{\\pi})(1{-}\\pi_s) \\end{bmatrix}.\n$}\n\\end{equation}\n\nDefine $\\delta_s = \\pi_s - \\bar{\\pi}$. Substituting $\\pi_s = \\bar{\\pi} + \\delta_s$:\n\\begin{equation}\nM_{\\text{global}}^{-1} M_s - I = \\frac{\\delta_s}{1-2\\bar{\\pi}} \\begin{bmatrix} -1 & 1 \\\\ 1 & -1 \\end{bmatrix}.\n\\end{equation}\n\nTo verify: the $(1,1)$ entry of $M_{\\text{global}}^{-1} M_s$ is\n{\\small\n\\begin{align}\n&\\frac{(1{-}\\bar{\\pi})(1{-}\\bar{\\pi}{-}\\delta_s) - \\bar{\\pi}(\\bar{\\pi}{+}\\delta_s)}{1-2\\bar{\\pi}} \\nonumber\\\\\n&= \\frac{(1{-}\\bar{\\pi})^2 - (1{-}\\bar{\\pi})\\delta_s - \\bar{\\pi}^2 - \\bar{\\pi}\\delta_s}{1-2\\bar{\\pi}} \\nonumber\\\\\n&= \\frac{1 - 2\\bar{\\pi} - \\delta_s}{1-2\\bar{\\pi}} = 1 - \\frac{\\delta_s}{1-2\\bar{\\pi}}.\n\\end{align}\n}\n\nApplying $(M_{\\text{global}}^{-1} M_s - I)$ to $\\boldsymbol{\\tau}$:\n{\\small\n\\begin{align}\n\\text{bias}(z{=}0, s) &= \\tfrac{\\delta_s}{1-2\\bar{\\pi}}(-\\tau(0) + \\tau(1)) = +\\tfrac{\\delta_s \\cdot \\Delta\\tau}{1-2\\bar{\\pi}}, \\\\\n\\text{bias}(z{=}1, s) &= \\tfrac{\\delta_s}{1-2\\bar{\\pi}}(\\tau(0) - \\tau(1)) = -\\tfrac{\\delta_s \\cdot \\Delta\\tau}{1-2\\bar{\\pi}},\n\\end{align}\n}\nwhere $\\Delta\\tau = \\tau(1) - \\tau(0)$. \\qed\n\n\\section{Multi-class Extension and Proof}\n\\label{app:multiclass}\n\n\\begin{corollary}[Multi-class Extension]\n\\label{cor:multiclass}\nFor $K > 2$ subgroups with $J$ effect-modifier levels and uniform off-diagonal misclassification (misclassified observations from class $j$ are distributed equally among the remaining $J{-}1$ classes), the subgroup bias of global correction generalizes to\n\\begin{equation}\n\\mathrm{bias}_{\\mathrm{global}}(z, s) = \\sum_{j=1}^{J} \\bigl(\\bar{\\pi}_j - \\pi_{s,j}\\bigr) \\cdot \\bigl(\\tau(j) - \\bar{\\tau}\\bigr) \\cdot g(\\bar{\\pi}),\n\\label{eq:multiclass}\n\\end{equation}\nwhere $g(\\bar{\\pi})$ collects the matrix-inversion amplification terms.\\footnote{For $J=3$ with symmetric misclassification (off-diagonal errors uniform), $g(\\bar{\\pi}) = 1/(1 - 3\\bar{\\pi}/2)$, generalizing the $J{=}2$ factor $1/(1-2\\bar{\\pi})$. In general, $g(\\bar{\\pi}) = 1/(1 - J\\bar{\\pi}/(J-1))$.}\nThe essential structure, $\\sum_s w_s (\\bar{\\pi}_j - \\pi_{s,j}) = 0$, ensures that bias redistributes across subgroups rather than vanishing in aggregate.\n\\end{corollary}\n\n\\paragraph{Proof.}\nFor $K > 2$ subgroups with $J$ effect-modifier levels, the subgroup-specific mixing matrix $M_s$ is $J \\times J$ with entries $M_s[j, j'] = P(Z{=}j' \\mid \\hat{Z}{=}j, S{=}s)$.\nThe global mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s$.\n\nThe bias of global correction in subgroup $s$ at level $z$ is:\n\\begin{equation}\n\\text{bias}_{\\text{global}}(z, s) = [(M_{\\text{global}}^{-1} M_s - I) \\boldsymbol{\\tau}]_z.\n\\end{equation}\n\nWrite $M_s = M_{\\text{global}} + \\Delta_s$ where $\\Delta_s = M_s - M_{\\text{global}}$ satisfies $\\sum_s w_s \\Delta_s = 0$.\nThen $M_{\\text{global}}^{-1} M_s = I + M_{\\text{global}}^{-1} \\Delta_s$, so:\n\\begin{equation}\n\\text{bias}_{\\text{global}}(z, s) = [M_{\\text{global}}^{-1} \\Delta_s \\cdot \\boldsymbol{\\tau}]_z.\n\\end{equation}\n\nFor symmetric misclassification with per-class error rates $\\pi_{s,j}$ and pooled rates $\\bar{\\pi}_j$, the entries of $\\Delta_s$ have the form $\\Delta_s[j,j'] = (\\bar{\\pi}_j - \\pi_{s,j}) \\cdot h(j, j')$ for a function $h$ determined by the off-diagonal redistribution pattern.\nExpanding the matrix-vector product and collecting terms yields:\n\\begin{equation}\n\\text{bias}_{\\text{global}}(z, s) = \\sum_{j=1}^{J} (\\bar{\\pi}_j - \\pi_{s,j}) \\cdot (\\tau(j) - \\bar{\\tau}) \\cdot g(\\bar{\\pi}),\n\\end{equation}\nwhere $g(\\bar{\\pi})$ collects the matrix-inversion amplification terms and $\\bar{\\tau} = \\sum_j P(Z{=}j) \\tau(j)$.\n\nThe essential structure $\\sum_s w_s (\\bar{\\pi}_j - \\pi_{s,j}) = 0$ ensures that the weighted bias across subgroups sums to zero: global correction redistributes bias rather than creating or eliminating it in aggregate.\nFor non-uniform off-diagonal entries, the scalar amplification $g(\\bar{\\pi})$ generalizes to a cell-specific matrix; the product structure $B_s \\cdot \\Delta\\tau$ persists but a closed-form amplification factor does not. \\qed\n\n\\section{Proof of Proposition~\\ref{prop:debiasing_hurts}}\n\\label{app:debiasing_hurts}\n\nThe naive estimator has bias $\\tau_{\\text{obs}}(z,s) - \\tau(z)$.\nUnder (A2)--(A3), $\\tau_{\\text{obs}}(0,s) = (1-\\pi_s)\\tau(0) + \\pi_s\\tau(1)$, so $\\text{bias}_{\\text{naive}}(0,s) = \\pi_s \\cdot \\Delta\\tau$.\n\nGlobal correction produces larger absolute bias when $|\\text{bias}_{\\text{global}}(0,s)| > |\\text{bias}_{\\text{naive}}(0,s)|$:\n\\begin{equation}\n\\frac{|\\delta_s| \\cdot |\\Delta\\tau|}{|1-2\\bar{\\pi}|} > \\pi_s \\cdot |\\Delta\\tau|.\n\\end{equation}\nSince $\\Delta\\tau \\neq 0$ (otherwise both biases are zero), dividing through gives:\n\\begin{equation}\n\\frac{|\\delta_s|}{(1-2\\bar{\\pi}) \\cdot \\pi_s} > 1,\n\\end{equation}\nwhere we use $1-2\\bar{\\pi} > 0$ from (A4).\n\nFor high-error subgroups ($\\pi_s > \\bar{\\pi}$, so $\\delta_s > 0$): the condition becomes $(\\pi_s - \\bar{\\pi}) / ((1-2\\bar{\\pi})\\pi_s) > 1$, which simplifies to $\\pi_s(1 - 1 + 2\\bar{\\pi}) > \\bar{\\pi}$, i.e., $2\\bar{\\pi}\\pi_s > \\bar{\\pi}$, i.e., $\\pi_s > 0.5$.\nThis is excluded by (A4), so global correction always reduces bias in high-error subgroups.\n\nFor low-error subgroups ($\\pi_s < \\bar{\\pi}$, so $\\delta_s < 0$): the condition becomes $(\\bar{\\pi} - \\pi_s) / ((1-2\\bar{\\pi})\\pi_s) > 1$, which gives $\\pi_s < \\bar{\\pi} / (1 - 2\\bar{\\pi} + 1) = \\bar{\\pi} / (2(1-\\bar{\\pi}))$.\nWhen $\\bar{\\pi} = 0.15$, any subgroup with $\\pi_s < 0.088$ experiences increased bias from global correction. \\qed\n\n\\paragraph{Extension to asymmetric misclassification.}\nProposition~\\ref{prop:debiasing_hurts} assumes symmetric error rates (A2).\nUnder asymmetric misclassification ($\\mathrm{FPR}_s \\neq \\mathrm{FNR}_s$), the naive bias becomes $\\mathrm{bias}_{\\mathrm{naive}}(0,s) = \\mathrm{FPR}_s \\cdot \\tau(1) + (1 - \\mathrm{FPR}_s - 1)\\tau(0)$ and the global correction bias depends on the full $2 \\times 2$ structure of $B_s = M_{\\mathrm{global}}^{-1} M_s - I$ (Remark~1 in Section~\\ref{sec:theory}).\nA sufficient condition for global correction to increase bias is\n\\begin{equation}\n\\|B_s\\|_\\infty > \\max(\\mathrm{FPR}_s, \\mathrm{FNR}_s),\n\\end{equation}\nwhich reduces to Equation~\\eqref{eq:hurts_condition} when $\\mathrm{FPR}_s = \\mathrm{FNR}_s = \\pi_s$.\nIn the asymmetric experiments (Appendix~\\ref{app:asymmetric}), the symmetric diagnostic still achieves AUC $= 0.82$ when applied with $\\pi_s = (\\mathrm{FPR}_s + \\mathrm{FNR}_s)/2$, suggesting practical robustness.\nA fully general asymmetric diagnostic that accounts for the separate roles of FPR and FNR in each entry of $B_s$ is left to future work.\n\n\\section{Semi-Synthetic Data Generating Process}\n\\label{app:dgp}\n\n\\paragraph{Synthetic DGP (Sections~\\ref{sec:bias_mechanism}--\\ref{sec:diagnostic} and Appendix~\\ref{sec:budget}).}\nWe generate $N = 5000$ observations.\nEach observation belongs to one of $K \\in \\{2, 4\\}$ subgroups $S \\in \\{1, \\ldots, K\\}$ with equal weights $w_s = 1/K$.\nThe binary effect modifier $Z \\in \\{0, 1\\}$ is drawn with $P(Z{=}1) = 0.5$.\nTreatment assignment is $T \\sim \\text{Bernoulli}(0.5)$, independent of $Z$ and $S$.\n\nThe outcome is generated as:\n\\begin{equation}\nY = \\tau(Z) \\cdot T + \\varepsilon, \\quad \\varepsilon \\sim \\mathcal{N}(0, 1),\n\\end{equation}\nwhere the CATE function is $\\tau(z) = \\bar{\\tau} + \\Delta\\tau \\cdot (z - 0.5)$ with $\\bar{\\tau} = 0.5$.\nThe CATE heterogeneity $\\Delta\\tau \\in \\{0, 0.2, 0.5, 1.0\\}$ controls the strength of treatment effect variation across levels of $Z$.\n\nMisclassification is symmetric: $\\hat{Z} \\neq Z$ with probability $\\pi_s$ depending on subgroup.\nFor $K{=}2$: $\\pi_1 = \\bar{\\pi} - \\Delta_c/2$, $\\pi_2 = \\bar{\\pi} + \\Delta_c/2$, with $\\bar{\\pi} \\in \\{0.1, 0.2\\}$ and $\\Delta_c \\in \\{0, 0.05, 0.1, 0.15\\}$.\nFor $K{=}4$, extreme regime: $\\pi \\in \\{0.05, 0.10, 0.15, 0.25\\}$; moderate regime: $\\pi \\in \\{0.08, 0.12, 0.16, 0.20\\}$.\n\nExpert labels are drawn as a simple random sample of size $n_{\\text{expert}} \\in \\{50, 100, 250, 500, 1000, 2000\\}$ from the full dataset, with true $Z$ observed for these observations.\n\n\\paragraph{Semi-synthetic DGP (Section~\\ref{sec:ec_hte_eval}).}\nWe sample $N = 5000$ tweets from the TweetEval sentiment corpus ($N_{\\text{pool}} = 57{,}899$).\nSubgroups are defined by crossing \\texttt{has\\_hashtag} $\\times$ \\texttt{text\\_length\\_bin} (short/medium/long), yielding $K = 4$ subgroups with empirical sizes: $S_0 \\approx 38\\%$, $S_1 \\approx 38\\%$, $S_2 \\approx 12\\%$, $S_3 \\approx 12\\%$.\nMisclassification rates in the extreme regime are $\\pi_{S_0} = 0.05$, $\\pi_{S_1} = 0.10$, $\\pi_{S_2} = 0.15$, $\\pi_{S_3} = 0.25$, reflecting empirical evidence that hashtag-heavy text degrades LLM classifier accuracy.\nThe outcome DGP follows the same structure as the synthetic case, with CATE injected onto the real text-derived subgroup structure.\n\n\\paragraph{PPCI DGPs (Appendix~\\ref{sec:ppci}).}\nFour DGPs isolate error types: (A) covariate error only ($\\sigma_{\\text{outcome}} = 0$), (B) outcome error only ($\\sigma_{\\text{outcome}} = 0.5$), (C) both errors ($\\sigma_{\\text{outcome}} = 0.5$), (D) no error ($\\sigma_{\\text{outcome}} = 0$).\nOutcome-side error is additive Gaussian noise on $Y$.\n\n\\paragraph{CausalForestDML hyperparameters.}\nAll CausalForest experiments use \\texttt{econml.dml.CausalForestDML} with honest splitting, $n_{\\text{estimators}} = 48$, $\\texttt{min\\_samples\\_leaf} = 20$, \\texttt{model\\_y} = \\texttt{LassoCV}(cv=3), and \\texttt{model\\_t} = \\texttt{LogisticRegressionCV}.\nThese defaults were held constant across all configurations; no hyperparameter tuning was performed.\n\n\\section{Extended Related Work}\n\\label{app:related}\n\n\\paragraph{Measurement error details.}\n\\citet{fuller1987measurement} establish the foundational theory showing that naive regression with mismeasured covariates yields attenuated coefficient estimates.\n\\citet{carroll2006measurement} extend this to nonlinear models.\n\\citet{gustafson2003measurement} develops Bayesian treatments modeling measurement jointly with outcomes.\n\\citet{hu2008nonparametric} provide nonparametric identification using repeated measurements or instruments.\n\n\\paragraph{Annotation model extensions.}\nBeyond the foundational \\citet{dawid1979maximum} model, \\citet{passonneau2014benefits} incorporate item difficulty, \\citet{hovy2013learning} learn annotator competence, and \\citet{paun2018comparing} introduce hierarchical priors sharing information across annotators with varying expertise.\n\n\\paragraph{PPI extensions and text-as-data methods.}\n\\citet{zrnic2024cross} extend PPI via cross-prediction; their active inference framework~\\citep{zrnic2024active} achieves $>$80\\% expert budget savings through adaptive allocation, complementary to our fixed-budget analysis.\n\\citet{grimmer2022text} provide methodological guidance for text-as-data pipelines.\n\\citet{audinet2025benchmarking} systematically benchmark DSL and PPI methods for LLM-based parameter estimation, finding that debiasing can increase MSE when prediction error is heterogeneous---a population-level analogue of the subgroup-conditional bias amplification we formalize in Theorem~\\ref{thm:bias_identity}.\n\n\\paragraph{Treatment vs.\\ effect-modifier misclassification.}\n\\citet{imai2010causal} study treatment misclassification where errors change which arm a unit is assigned to, requiring instrumental variables or partial identification because the fundamental treated-vs-control contrast is corrupted.\nOur problem preserves the treatment contrast ($T$ is observed correctly) but corrupts the heterogeneity structure ($\\hat{Z} \\neq Z$).\nThe ATE remains identified; only conditional effects are biased, which makes exact correction through confusion matrix inversion feasible.\n\n\\paragraph{Econometrics of binary misclassification.}\n\\citet{bound2001measurement} survey measurement error in survey data, establishing that binary misclassification attenuates regression coefficients.\n\\citet{frazis2003estimating} derive exact bias formulas for OLS with a misclassified binary regressor, showing attenuation proportional to the misclassification rate---analogous to our Theorem~\\ref{thm:bias_identity} but restricted to average effects without subgroup heterogeneity.\n\\citet{black2000racial} demonstrate that racial misclassification in administrative data can substantially bias estimates of racial disparities.\n\\citet{mahajan2006identification} and \\citet{lewbel2007estimation} develop instrumental variable approaches to identify models with misclassified binary regressors, requiring exclusion restrictions unavailable when the mismeasured variable is an LLM annotation.\nOur setting differs in three respects: (i) the mismeasured variable is an effect modifier indexing the CATE function, not a standard regressor; (ii) misclassification rates vary across subgroups, creating the $\\delta_s \\times \\Delta\\tau$ product amplification absent from homogeneous-error analyses; and (iii) expert labels provide a direct calibration sample, enabling confusion matrix estimation without instruments.\n\n\\section{MCMC Convergence Diagnostics}\n\\label{app:mcmc}\n\nTable~\\ref{tab:mcmc} reports convergence diagnostics for the hierarchical Bayesian confusion matrix estimator across all experimental configurations.\nAll runs use 4 chains with 4000 iterations (2000 warmup).\nMain experiments (Table~\\ref{tab:main_results}) use a Dirichlet prior centered on $\\hat{C}_{\\text{global}}$ with concentration $\\alpha_0$ estimated via empirical Bayes (marginal likelihood).\nAppendix robustness experiments use a fixed Dirichlet prior ($\\alpha{=}3$); since fixed-$\\alpha$ partial pooling is weakly dominated by the adaptive variant, these results are conservative.\nThis budget is sufficient for the $2{\\times}2$ Dirichlet-Multinomial posterior; all runs achieve $\\hat{R} < 1.0034$ and ESS $> 1618$, confirming convergence with substantial margin.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nDiagnostic & Threshold & Achieved \\\\\n\\midrule\n$\\hat{R}$ (max across all params) & $< 1.01$ & $< 1.0034$ \\\\\nESS (min across all params) & $> 845$ & $> 1618$ \\\\\nDivergent transitions & $= 0$ & $0$ \\\\\nSingularity guard triggers & --- & extreme/$n{=}50$ only \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{MCMC convergence diagnostics for the hierarchical Bayesian estimator. All configurations satisfy convergence criteria with substantial margin.}\n\\label{tab:mcmc}\n\\end{table}\n\n\\paragraph{Hyperprior sensitivity.}\nScaling the $\\text{Gamma}(3, 1)$ hyperprior by factors of $0.5\\times$ to $2\\times$ produces $<$1\\% RMSE variation for $K{=}2$ and $\\sim$4--5\\% for $K{=}4$.\nCoverage remains invariant across the sensitivity range.\nThese results confirm that the hierarchical estimator is robust to prior specification within a reasonable range.\n\n\\section{Diagnostic ROC Curves}\n\\label{app:roc}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_roc.png}\n\\caption{ROC curves for the $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}): $|\\delta_s|/((1{-}2\\bar\\pi)\\cdot\\pi_s)>1$. (A)~Setting-level ROC (AUC $= 0.89$), compared with the $|\\Delta\\pi \\times \\Delta\\tau|$ product (AUC $= 0.89$) and $\\mathrm{CV}(\\pi_s)$ (AUC $= 0.97$). (B)~Subgroup-level ROC: the $\\Delta\\pi$-only condition (AUC $= 0.86$) substantially outperforms the $|\\Delta\\pi \\times \\Delta\\tau|$ product (AUC $= 0.73$). The $\\Delta\\tau$-free diagnostic depends only on estimable misclassification rates, breaking the circular dependency that would arise if CATE heterogeneity were required.}\n\\label{fig:roc}\n\\end{figure}\n\n\\paragraph{Cost-asymmetric diagnostic thresholds.}\nIn practice, the cost of a false negative (failing to detect that global correction increases bias) exceeds the cost of a false positive (unnecessarily applying EC-HTE when global correction would suffice), because the former propagates systematic bias into CATE estimates while the latter only incurs additional estimation variance.\nPractitioners in high-stakes settings (e.g., policy evaluation where CATE estimates inform resource allocation) should lower the diagnostic threshold to favor recall over precision, accepting more false positives to minimize the risk of undetected bias amplification.\n\n\\section{Expert Budget Crossover Curves}\n\\label{app:budget}\n\\label{sec:budget}\n\nThe crossover point at which EC-HTE achieves lower RMSE than global correction is $n_{\\text{expert}} = 250$ for $K{=}2$/extreme and $n_{\\text{expert}} = 1000$ for $K{=}4$/extreme (Figure~\\ref{fig:budget}).\nUnder moderate heterogeneity ($K{=}2$), EC-HTE never achieves lower RMSE than global at any budget.\nHB partial pooling improves over stratified MLE in 21 of 24 configurations, with the two estimators converging by $n_{\\text{expert}} \\geq 1000$.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig3_budget.pdf}\n\\caption{RMSE vs.\\ expert budget ($n_{\\text{expert}}$) across four regime$\\times K$ combinations. Dashed vertical lines mark crossover points where EC-HTE achieves lower RMSE than global correction: $n{=}250$ ($K{=}2$, extreme), $n{=}1000$ ($K{=}4$, extreme). Under moderate heterogeneity ($K{=}2$), global correction dominates at all budgets. Shaded bands show $\\pm 1$ SD across subgroups within each configuration.}\n\\label{fig:budget}\n\\end{figure*}\n\n\\subsection{Budget Sensitivity: HB vs.\\ Stratified MLE}\n\\label{app:budget_sensitivity}\n\nHierarchical Bayes (HB) partial pooling borrows strength across subgroups, which should matter most when per-subgroup expert labels are scarce.\nWe sweep $n_{\\text{expert}} \\in \\{25, 50, 75, 100, 150, 250\\}$ under extreme heterogeneity ($\\Delta\\tau{=}0.3$, 100 MC runs, $N{=}5{,}000$).\nTable~\\ref{tab:budget_sensitivity} reports aggregate RMSE for global correction, stratified MLE, and HB EC-HTE.\n\n\\begin{table}[h]\n\\centering\n\\caption{RMSE across expert budgets under extreme heterogeneity.\nHB crossover (first budget where HB $<$ MLE) occurs at approximately 10 expert labels per subgroup-cell:\n$n_{\\text{expert}}{=}50$ for $K{=}2$ and $n_{\\text{expert}}{=}75$ for $K{=}4$.}\n\\label{tab:budget_sensitivity}\n\\small\n\\begin{tabular}{crrrrc}\n\\toprule\n$K$ & $n_{\\text{expert}}$ & Global & Strat.\\ MLE & HB EC-HTE & HB vs.\\ MLE \\\\\n\\midrule\n2 & 25 & \\textbf{0.101} & 0.256 & 0.269 & $+4.9\\%$ \\\\\n2 & 50 & \\textbf{0.088} & 0.275 & 0.231 & $\\mathbf{-16.1\\%}$ \\\\\n2 & 75 & 0.084 & 0.091 & \\textbf{0.089} & $-1.9\\%$ \\\\\n2 & 100 & 0.083 & 0.085 & \\textbf{0.084} & $-0.8\\%$ \\\\\n2 & 150 & 0.081 & 0.077 & \\textbf{0.077} & $-0.4\\%$ \\\\\n2 & 250 & 0.080 & 0.075 & \\textbf{0.074} & $-0.1\\%$ \\\\\n\\midrule\n4 & 25 & \\textbf{0.129} & 0.401 & 0.612 & $+52.5\\%$ \\\\\n4 & 50 & \\textbf{0.117} & 0.380 & 0.470 & $+23.8\\%$ \\\\\n4 & 75 & \\textbf{0.112} & 0.221 & 0.211 & $\\mathbf{-4.4\\%}$ \\\\\n4 & 100 & \\textbf{0.112} & 0.215 & 0.212 & $-1.3\\%$ \\\\\n4 & 150 & \\textbf{0.109} & 0.157 & 0.152 & $-3.6\\%$ \\\\\n4 & 250 & \\textbf{0.108} & 0.127 & 0.126 & $-1.0\\%$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree regimes emerge.\nAt very low budgets ($n_{\\text{expert}} < 50$ for $K{=}2$, $< 75$ for $K{=}4$), per-subgroup counts are insufficient for reliable confusion matrix estimation; global pooling dominates because the variance cost of stratification overwhelms any bias reduction.\nHB degrades substantially in this regime because the Gibbs posterior, while better regularized than MLE, still cannot overcome the fundamental sample-size constraint with $\\sim$6--12 labels per subgroup.\nAt moderate budgets ($n_{\\text{expert}} = 50$--$250$ for $K{=}2$, $75$--$250$ for $K{=}4$), HB partial pooling provides consistent RMSE improvement over stratified MLE ($-0.4\\%$ to $-16.1\\%$), with the largest gains near the crossover point.\nAt high budgets ($n_{\\text{expert}} \\geq 250$), both estimators converge as subgroup-level data becomes sufficient for reliable MLE; the HB advantage diminishes to $< 1\\%$.\nCoverage remains $\\geq 0.88$ for both methods across all budget levels.\n\n\\subsection{Scalability to $K{=}8$ Subgroups}\n\\label{app:k8_subgroups}\n\nWe test EC-HTE at $K{=}8$ to identify the scalability boundary of hierarchical Bayesian partial pooling under fixed expert budget.\n\n\\paragraph{Setup.}\n$N{=}5{,}000$, $K{=}8$ (equal-weight subgroups), $n_{\\text{expert}}{=}250$ (${\\approx}31$ labels per subgroup), 100 MC replications.\nMisclassification rates are uniformly spread: $\\pi_s \\in \\{0.05, 0.09, 0.13, 0.18, 0.22, 0.26, 0.30, 0.35\\}$.\nTreatment effects depend on $Z$ (not subgroup): $\\tau(Z{=}0){=}0$, $\\tau(Z{=}1){=}0.3$.\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE at $K{=}8$ ($n_{\\text{expert}}{=}250$, ${\\approx}31$ labels/subgroup, 100 MC).}\n\\label{tab:k8_subgroups}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Coverage & RMSE & $|\\text{Bias}|$ \\\\\n\\midrule\nOracle       & 0.944 & 0.113 & 0.090 \\\\\nGlobal       & 0.951 & 0.168 & 0.135 \\\\\nHB EC-HTE    & 0.956 & 0.340 & 0.183 \\\\\nStrat MLE    & 0.953 & 0.638 & 0.219 \\\\\nNaive        & 0.913 & 0.133 & 0.107 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll CM-aware methods achieve nominal coverage at $K{=}8$: HB EC-HTE 95.6\\%, Strat MLE 95.3\\%, Global 95.1\\%.\nHB partial pooling achieves a 47\\% RMSE reduction over stratified MLE (0.340 vs.\\ 0.638), confirming that hierarchical shrinkage provides substantial regularization.\nHowever, HB RMSE (0.340) exceeds global correction (0.168), indicating that ${\\approx}31$ expert labels per subgroup are insufficient for per-subgroup CM estimation to outweigh variance inflation.\n\n\\paragraph{Per-subgroup breakdown.}\nTable~\\ref{tab:k8_per_subgroup} decomposes RMSE by subgroup.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-subgroup RMSE at $K{=}8$. HB improvement over MLE is largest in high-$\\pi$ subgroups but does not close the gap with Global.}\n\\label{tab:k8_per_subgroup}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\nSubgroup & $\\pi_s$ & HB RMSE & MLE RMSE & Global RMSE & HB Cov \\\\\n\\midrule\n$s_0$ & 0.050 & 0.136 & 0.134 & \\textbf{0.181} & 0.950 \\\\\n$s_1$ & 0.093 & 0.133 & 0.132 & \\textbf{0.154} & 0.970 \\\\\n$s_2$ & 0.136 & 0.154 & 0.154 & 0.161 & 0.975 \\\\\n$s_3$ & 0.179 & 0.178 & 0.182 & \\textbf{0.159} & 0.945 \\\\\n$s_4$ & 0.221 & 0.263 & 0.343 & \\textbf{0.163} & 0.940 \\\\\n$s_5$ & 0.264 & 0.421 & 0.711 & \\textbf{0.164} & 0.965 \\\\\n$s_6$ & 0.307 & 0.634 & 1.375 & \\textbf{0.177} & 0.940 \\\\\n$s_7$ & 0.350 & 0.432 & 0.809 & \\textbf{0.183} & 0.960 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRMSE degradation is concentrated in high-$\\pi$ subgroups ($s_4$--$s_7$, $\\pi \\geq 0.22$), where confusion matrix inversion amplifies estimation noise ($r = 0.87$, $p = 0.005$ for correlation between $\\pi_s$ and HB RMSE).\nLow-error subgroups ($s_0$--$s_1$) benefit from stratification, with HB RMSE 14--25\\% below global correction.\nHB partial pooling reduces MLE RMSE by 24--54\\% in the high-$\\pi$ regime ($s_4$--$s_7$), confirming that hierarchical shrinkage provides meaningful regularization even when per-subgroup labels are scarce.\nCoverage remains $\\geq$0.94 across all subgroups for HB EC-HTE, indicating that variance inflation does not compromise inference validity.\nAdaptive shrinkage---increasing the prior strength for high-$\\pi$ subgroups where CM estimation is least reliable---is a natural extension that may close the RMSE gap with global correction at larger $K$.\n\nWe explored adaptive shrinkage ($\\alpha{=}10$ for high-$\\pi$ subgroups vs.\\ default $\\alpha{=}3$), which reduces aggregate RMSE from 0.340 to 0.216 (35\\% improvement) by attenuating estimation noise in high-$\\pi$ subgroups.\nHowever, RMSE remains 30\\% above global correction (0.166), confirming that the bottleneck is per-subgroup sample size (${\\sim}$31 expert labels) rather than the shrinkage method itself.\nThis establishes $K{=}8$ at $n_{\\text{expert}}{=}250$ as a boundary condition: all correction methods provide valid inference (coverage $\\geq$94\\%), but per-subgroup stratification requires proportionally larger expert budgets---approximately $n_{\\text{expert}} \\geq 500$ (${\\approx}60$ labels/subgroup)---to achieve RMSE parity with global correction.\n\n\\section{Asymmetric Misclassification Extension}\n\\label{app:asymmetric}\n\nAssumption~(A2) imposes symmetric misclassification ($\\text{FPR}_s = \\text{FNR}_s = \\pi_s$), which simplifies the bias decomposition but is not necessary for it.\nReal LLM annotators typically exhibit asymmetric confusion patterns; we show here that the product structure generalizes.\n\n\\paragraph{General bias formula.}\nFor asymmetric confusion matrices $C_s = \\bigl(\\begin{smallmatrix} 1{-}\\text{FPR}_s & \\text{FPR}_s \\\\ \\text{FNR}_s & 1{-}\\text{FNR}_s \\end{smallmatrix}\\bigr)$, define the mixing matrix $M_s$ via Bayesian inversion and the residual matrix $B_s = M_{\\text{global}}^{-1} M_s - I$.\nSince both $M_s$ and $M_{\\text{global}}$ are row-stochastic, $B_s \\mathbf{1} = \\mathbf{0}$.\nDecomposing $\\boldsymbol{\\tau} = \\tau(0)\\mathbf{1} + \\Delta\\tau \\, \\mathbf{e}_1$ gives:\n\\begin{equation}\n\\text{bias}(z, s) = \\Delta\\tau \\cdot [B_s]_{z,1},\n\\end{equation}\nwhere $[B_s]_{z,1}$ depends only on $\\{\\text{FPR}_k, \\text{FNR}_k, w_k\\}$, not on $\\Delta\\tau$.\nUnder~(A2), this reduces to $\\delta_s \\Delta\\tau / (1 - 2\\bar{\\pi})$ (Theorem~\\ref{thm:bias_identity}).\n\n\\paragraph{Empirical validation.}\nWe test three asymmetric configurations ($K{=}2$, $n_{\\text{expert}}{=}250$, 100 MC runs each): \\emph{Cross} (FPR/FNR = 0.10/0.20 vs.\\ 0.25/0.10), \\emph{Co-directional} (0.05/0.15 vs.\\ 0.20/0.30), and \\emph{Extreme} (0.03/0.25 vs.\\ 0.30/0.05).\nRegressing analytic predictions on MC bias yields $R^2 = 0.991$ across all configurations, confirming the product structure under asymmetry.\nTable~\\ref{tab:asymmetric} reports correction performance averaged over subgroups, $z$-levels, and $\\Delta\\tau \\in \\{0.1, \\ldots, 0.5\\}$.\nEC-HTE reduces $|\\text{bias}|$ from 0.025 (global) to 0.006, a $4\\times$ improvement, with lower RMSE (0.033 vs.\\ 0.040) and substantially better coverage (0.90 vs.\\ 0.78).\n\n\\begin{table}[t]\n\\centering\n\\caption{Asymmetric misclassification results ($K{=}2$, $n_{\\text{expert}}{=}250$, 100 MC runs). Values averaged over subgroups, $z$-levels, and $\\Delta\\tau$.}\n\\label{tab:asymmetric}\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\nMethod & $|\\text{Bias}| \\downarrow$ & RMSE $\\downarrow$ & Coverage $\\uparrow$ \\\\\n\\midrule\nNaive & 0.047 & 0.053 & 0.48 \\\\\nGlobal & 0.025 & 0.040 & 0.78 \\\\\nHB EC-HTE & \\textbf{0.006} & \\textbf{0.033} & \\textbf{0.90} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Supplementary Main Results}\n\\label{app:main_supp}\n\n\\begin{table}[t]\n\\centering\n\\caption{Additional configurations from the main experiment. $|\\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and 100 MC runs. $^\\dagger$RMSE exceeds Global.}\n\\label{tab:main_supp}\n\\small\n\\begin{tabular}{ll ccc}\n\\toprule\nConfiguration & Method & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Synthetic DIM\\\\$K{=}2$, moderate, $n{=}250$}}\n & Naive & 0.018 & 0.064 & 0.95 \\\\\n & Global & 0.009 & 0.074 & 0.96 \\\\\n & Strat.\\ MLE & \\textbf{0.005} & 0.075$^\\dagger$ & 0.97 \\\\\n & HB EC-HTE & \\textbf{0.005} & 0.075$^\\dagger$ & 0.97 \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Semi-synthetic\\\\TweetEval, extreme, $n{=}250$}}\n & Naive & 0.027 & 0.103 & 0.93 \\\\\n & Global & \\textbf{0.023} & 0.124 & 0.92 \\\\\n & Strat.\\ MLE & 0.032 & 0.248$^\\dagger$ & 0.91 \\\\\n & HB EC-HTE & 0.027 & 0.225$^\\dagger$ & 0.91 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{PPCI Complementarity Results}\n\\label{app:ppci}\n\\label{sec:ppci}\n\nEC-HTE composes with PPCI~\\cite{sui2026ppci} for settings where both covariate misclassification and outcome model error are present: EC-HTE+PPCI reduces $|\\text{bias}|$ from 0.179 to 0.007 ($z{=}0$, DGP~C), and the corrected pseudo-outcomes are compatible with other CATE estimators (R-learner bias reduction: 89\\%; Appendix~\\ref{app:rlearner}).\n\n\\begin{table*}[t]\n\\centering\n\\caption{PPCI complementarity experiment ($K{=}2$, extreme, $n_{\\text{expert}}{=}250$). DGP~A: covariate error only; B: outcome error only ($\\sigma{=}0.5$); C: both errors; D: no error. Values are $|\\text{bias}|$ and RMSE averaged over two subgroups. $^\\star$EC-HTE+PPCI achieves near-zero bias when both error types are present.}\n\\label{tab:ppci}\n\\small\n\\begin{tabular}{ll cccc}\n\\toprule\nDGP & Method & $|\\text{Bias}|_{z=0}$ & $|\\text{Bias}|_{z=1}$ & RMSE$_{z=0}$ & RMSE$_{z=1}$ \\\\\n\\midrule\n\\multirow{5}{*}{A: Covariate}\n & Naive & 0.053 & 0.063 & 0.087 & 0.093 \\\\\n & Global & 0.063 & 0.055 & 0.101 & 0.102 \\\\\n & EC-HTE & 0.017 & \\textbf{0.013} & 0.097 & 0.108 \\\\\n & PPCI & \\textbf{0.015} & 0.020 & 0.162 & 0.168 \\\\\n & EC-HTE+PPCI & 0.017 & \\textbf{0.013} & 0.097 & 0.108 \\\\\n\\midrule\n\\multirow{5}{*}{B: Outcome}\n & Naive & 0.189 & 0.197 & 0.206 & 0.212 \\\\\n & Global & 0.185 & 0.208 & 0.204 & 0.228 \\\\\n & EC-HTE & 0.181 & 0.215 & 0.202 & 0.237 \\\\\n & PPCI & 0.015 & \\textbf{0.020} & 0.171 & 0.176 \\\\\n & EC-HTE+PPCI & \\textbf{0.012} & 0.023 & 0.171 & 0.186 \\\\\n\\midrule\n\\multirow{5}{*}{C: Both}\n & Naive & 0.251 & 0.135 & 0.267 & 0.155 \\\\\n & Global & 0.182 & 0.209 & 0.233 & 0.235 \\\\\n & EC-HTE & 0.179 & 0.216 & 0.224 & 0.262 \\\\\n & PPCI & 0.017 & 0.007 & 0.241 & 0.232 \\\\\n & EC-HTE+PPCI$^\\star$ & \\textbf{0.007} & \\textbf{0.008} & 0.209 & 0.223 \\\\\n\\midrule\n\\multirow{5}{*}{D: None}\n & Naive & \\textbf{0.007} & 0.003 & 0.060 & 0.065 \\\\\n & Global & 0.010 & \\textbf{0.002} & 0.061 & 0.071 \\\\\n & EC-HTE & 0.013 & 0.007 & 0.062 & 0.079 \\\\\n & PPCI & \\textbf{0.007} & \\textbf{0.003} & 0.060 & 0.065 \\\\\n & EC-HTE+PPCI & 0.013 & 0.007 & 0.062 & 0.079 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe complementarity of EC-HTE and PPCI follows from the distinct error sources they correct: EC-HTE addresses misclassification in the effect modifier $Z$ (covariate space), while PPCI corrects specification error in the outcome model $f(X)$ (prediction space).\nSince covariate misclassification and outcome model error are algebraically independent in the potential outcomes framework, their corrections compose without interference---confirmed by the 4-DGP orthogonal design (Table~\\ref{tab:ppci}), where DGP~C (both errors present) yields the largest bias reduction from the combined approach.\nUnder covariate error only, PPCI adds nothing; under no error, all methods perform equivalently.\n\n\\section{Real-Data Case Study: Hate Speech Detection}\n\\label{app:hatespeech}\n\nWe apply EC-HTE to the UC Berkeley Measuring Hate Speech corpus~\\cite{kennedy2020constructing}, annotating 2{,}496 comments for dehumanization using GPT-4.1.\nFour text-feature subgroups are defined by crossing platform (Reddit/Gab vs.\\ Twitter/YouTube) and text length (above/below median), yielding balanced groups ($n \\approx 624$ each).\n\n\\paragraph{Positive finding: real-world heterogeneity.}\nPer-subgroup misclassification rates range from 0.266 to 0.383, confirming heterogeneity ($\\Delta\\pi = 0.117$) in a real annotation setting.\nAt the error-type level, FPR ranges from 8.5\\% to 21.3\\% across text-feature subgroups, demonstrating that subgroup-varying misclassification is not an artifact of synthetic design but arises naturally in real NLP annotation tasks.\n\n\\paragraph{Boundary condition: statistical power at extreme FNR.}\nCorrection results are inconclusive: all corrected confidence intervals contain zero, and point estimate differences between methods are not statistically significant.\nThe high baseline FNR (53.3\\%) amplifies variance through matrix inversion (variance amplification factor up to 15.7$\\times$), rendering the comparison underpowered.\nWhen $P(\\hat{Z}{=}1 \\mid Z{=}1) \\approx 0.5$, the confusion matrix approaches singularity, and inversion amplifies estimation noise regardless of stratification strategy.\nThis complements the expert budget threshold identified in Appendix~\\ref{sec:budget}: EC-HTE requires \\emph{both} sufficient expert labels \\emph{and} sufficient baseline classifier quality.\n\n\\paragraph{Diagnostic connection.}\nThe diagnostic criterion ($\\Delta\\pi \\times \\Delta\\tau$, Section~\\ref{sec:diagnostic}) identifies when correction is worthwhile under moderate baseline accuracy.\nThis case study illustrates that even when $\\Delta\\pi$ is large, extreme baseline error renders correction underpowered rather than beneficial.\nA practical prerequisite is that the per-subgroup confusion matrix condition number $\\kappa(\\hat{C}_s)$ remain moderate; when $\\kappa > 50$, as observed here, practitioners should prioritize improving annotation quality before applying any matrix-inversion-based correction.\n\n\\section{Cross-Model Consistency}\n\\label{app:multilm}\n\nWe evaluate whether misclassification heterogeneity is model-specific by annotating 500 TweetEval sentiment tweets with six OpenAI models spanning three generations.\nSix text-feature subgroups are defined by crossing hashtag presence and text length.\nSpearman rank correlations of per-subgroup error rates across all six subgroups range from $\\rho = 0.82$ to $1.00$, indicating that the subgroup error structure is consistent across architectures.\nTwo subgroups with $n \\leq 6$ exhibit zero misclassification across all models; excluding these yields four-point correlations that are directionally consistent but underpowered.%\n\\footnote{The filtered $\\Delta\\pi$ values in Table~\\ref{tab:multilm} serve as a robustness check independent of rank-order testing: all six models exceed $\\Delta\\pi > 0.05$ on the four retained subgroups.}\n\n\\begin{table}[t]\n\\centering\n\\caption{Effective misclassification heterogeneity ($\\Delta\\pi$) across six OpenAI models on TweetEval sentiment (500 tweets, filtered to 4 subgroups with $n \\geq 10$).}\n\\label{tab:multilm}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nModel & Effective $\\Delta\\pi$ & $> 0.05$? \\\\\n\\midrule\nGPT-3.5-Turbo & 0.198 & \\checkmark \\\\\nGPT-4-Turbo & 0.149 & \\checkmark \\\\\nGPT-4o-mini & 0.136 & \\checkmark \\\\\nGPT-5.4 & 0.114 & \\checkmark \\\\\nGPT-4.1 & 0.098 & \\checkmark \\\\\nGPT-4o & 0.080 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll six models exhibit effective $\\Delta\\pi > 0.05$ on the four retained subgroups (Table~\\ref{tab:multilm}), and 5 of 6 share the same worst subgroup (\\texttt{True\\_medium}: tweets with hashtags and medium text length).\nNewer models reduce absolute error rates but do not eliminate subgroup heterogeneity: GPT-5.4 achieves $\\Delta\\pi = 0.114$ compared to GPT-3.5-Turbo's $0.198$.\nThese results were obtained with a single API provider; open-source model validation appears in Appendix~\\ref{app:multilm_opensource}.\n\n\\section{Open-Source Multi-LLM Validation}\n\\label{app:multilm_opensource}\n\nWe evaluate four open-source LLMs (7B--9B parameter range) on 490 TweetEval sentiment tweets with $K{=}4$ subgroups defined by crossing hashtag presence and text length.\nTable~\\ref{tab:multilm_cm} reports the confusion matrix heterogeneity profile.\nAll four models exhibit $\\Delta\\pi > 0.05$, confirming that subgroup-heterogeneous misclassification is not specific to proprietary APIs.\nSubgroup error rankings are consistent across architectures: \\texttt{True\\_short} (short tweets with hashtags) has the lowest $\\pi_s$ in 3 of 4 models, while \\texttt{False\\_medium} (medium tweets without hashtags) has the highest.\n\n\\begin{table}[t]\n\\centering\n\\caption{Confusion matrix heterogeneity across four open-source LLMs ($K{=}4$, $N{=}490$ TweetEval tweets). $\\Delta\\pi$: max--min per-subgroup misclassification rate. Prop2: number of subgroups where the $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}) triggers.}\n\\label{tab:multilm_cm}\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\nModel & Acc.\\ & $\\Delta\\pi$ & Prop2 & Strongest \\\\\n\\midrule\nLlama-3.1-8B & 0.755 & 0.141 & 1/4 & True\\_short \\\\\nQwen-2.5-7B & 0.798 & 0.165 & 1/4 & True\\_short \\\\\nGemma-2-9B & 0.763 & 0.125 & 4/4 & True\\_medium \\\\\nMistral-7B & 0.802 & 0.134 & 0/4 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Semi-synthetic budget sweep.}\nWe run the full EC-HTE pipeline with $K{=}2$ subgroups and $\\Delta\\tau{=}0.3$, using each model's empirical confusion matrices.\nTable~\\ref{tab:multilm_budget} reports coverage and RMSE crossover points.\nEC-HTE restores near-nominal coverage from 0.714 (naive average) to 0.939 ($+$22.5 percentage points) at $n_{\\text{expert}}{=}1{,}000$, consistent across all four models.\nGlobal correction achieves comparable or lower RMSE than HB at all budgets under these moderate $\\Delta\\pi$ values, and the $K{=}4$ RMSE crossover never occurs---confirming the budget guidelines in Appendix~\\ref{sec:budget}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Semi-synthetic budget sweep ($K{=}2$, $\\Delta\\tau{=}0.3$, 50 MC runs\\protect\\footnote{Appendix experiments use 50 MC replications unless otherwise noted; all main-text results use 100.}). Coverage at selected expert budgets; RMSE crossover denotes the minimum expert budget at which HB EC-HTE achieves lower RMSE than the naive (uncorrected) estimator.}\n\\label{tab:multilm_budget}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nModel & $\\Delta\\pi_{K{=}2}$ & Naive Cov.\\ & HB Cov.\\ ($n{=}1000$) & Crossover \\\\\n\\midrule\nLlama-3.1-8B & 0.051 & 0.675 & 0.940 & $n{=}1000$ \\\\\nQwen-2.5-7B & 0.080 & 0.715 & 0.925 & $n{=}1000$ \\\\\nGemma-2-9B & 0.100 & 0.705 & 0.945 & $n{=}1000$ \\\\\nMistral-7B & 0.070 & 0.760 & 0.945 & $n{=}1000$ \\\\\n\\midrule\n\\textit{Average} & --- & \\textit{0.714} & \\textit{0.939} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Gemma boundary case.}\nGemma-2-9B triggers the Proposition~\\ref{prop:debiasing_hurts} diagnostic in all four $K{=}4$ subgroups due to extreme FPR--FNR asymmetry (\\texttt{False\\_medium} FNR $= 0.437$).\nAt small budgets ($K{=}4$, $n{=}100$), EC-HTE RMSE reaches 1.229 ($3.1\\times$ naive), illustrating the budget guideline from Appendix~\\ref{sec:budget}: when per-subgroup cell counts fall below 25, the variance cost of stratified correction dominates.\nAt $n \\geq 500$, EC-HTE coverage recovers to $>$0.90, consistent with the synthetic experiments.\n\n\\paragraph{Heterogeneous-$\\tau$ DGP.}\nTo assess whether the constant-$\\tau$ DGP understates EC-HTE's advantage, we run a supplementary experiment using Llama's empirical confusion matrices with heterogeneous treatment effects across subgroups ($\\Delta\\tau \\in [0.1, 0.6]$, $K{=}2$, 50 MC runs).\nEC-HTE achieves lower $|\\text{bias}|$ than global correction at all budgets ($n{=}500$: 0.010 vs.\\ 0.031, a 68\\% reduction).\nIn the high-$\\Delta\\tau$ subgroup (\\texttt{True\\_short}, $\\Delta\\tau{=}0.6$), EC-HTE also achieves lower RMSE ($n{=}1{,}000$: 0.212 vs.\\ 0.258, 18\\% improvement), confirming that the RMSE advantage concentrates in subgroups where correction is most needed.\nAggregate RMSE remains comparable to global correction because low-$\\Delta\\tau$ subgroups incur stratification variance without commensurate bias reduction, consistent with the budget guidelines in Appendix~\\ref{sec:budget}.\n\n\\section{Robustness to Subgroup Misspecification}\n\\label{app:robustness}\n\nEC-HTE requires pre-defined subgroup labels, which may be noisy in practice.\nWe test robustness by randomly flipping each observation's subgroup assignment with probability $p_{\\text{flip}} \\in \\{0, 0.10, 0.25, 0.50\\}$, across $K \\in \\{2, 4\\}$ (extreme regime, $n_{\\text{expert}} = 500$, $\\Delta\\tau = 0.3$, 100 MC runs).\n\n\\begin{table}[t]\n\\centering\n\\caption{95\\% CI coverage under subgroup misspecification noise. EC-HTE maintains near-nominal coverage across all noise levels.}\n\\label{tab:robustness}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{4}{c}{$p_{\\text{flip}}$} \\\\\n\\cmidrule(lr){2-5}\nMethod & 0.00 & 0.10 & 0.25 & 0.50 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{$K{=}2$, extreme}} \\\\\n\\quad Naive & 0.875 & 0.877 & 0.890 & 0.897 \\\\\n\\quad Global & 0.925 & 0.935 & 0.932 & 0.945 \\\\\n\\quad HB EC-HTE & 0.958 & 0.948 & 0.950 & 0.945 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{$K{=}4$, extreme}} \\\\\n\\quad Naive & 0.904 & 0.916 & 0.909 & 0.919 \\\\\n\\quad Global & 0.930 & 0.953 & 0.948 & 0.944 \\\\\n\\quad HB EC-HTE & 0.956 & 0.958 & 0.960 & 0.946 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE maintains coverage $\\geq 0.945$ across all configurations (Table~\\ref{tab:robustness}), while the naive estimator is systematically below nominal (0.875--0.919).\nAt $p_{\\text{flip}} = 0.50$, subgroup structure is effectively destroyed; EC-HTE converges to global correction (coverage and RMSE within 0.1\\%), confirming that hierarchical Bayesian shrinkage provides a built-in safety mechanism.\nFor $K{=}4$ at $p_{\\text{flip}} = 0.50$, a small residual RMSE gap persists ($p < 0.01$), reflecting the variance cost of estimating four confusion matrices even when they carry no signal.\n\n\\section{Monte Carlo Standard Errors}\n\\label{app:mcse}\n\nAll experiments use 100 independent Monte Carlo replications per configuration.\nAll simulation results were verified with 100 MC seeds; the median RMSE variation between 50-seed and 100-seed estimates is below 3.2\\%, confirming the stability of reported figures.\nWe report Monte Carlo standard errors to assess whether observed differences between methods are statistically reliable.\nFor exp-001 (synthetic DGP, no per-seed pairing across methods), we use conservative two-sample $z$-tests on the 100-run means.\nFor exp-003 (semi-synthetic TweetEval, shared seeds across methods), we use paired $t$-tests, which are more powerful because they control for seed-level variation.\n\nTable~\\ref{tab:mcse} reports paired comparisons for representative configurations.\nOf 1{,}020 total pairwise comparisons across all configurations, 742 (72.7\\%) are statistically significant at $\\alpha = 0.05$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Paired comparisons for representative configurations. $\\Delta$ = method A $-$ method B (negative favors A for $|\\text{bias}|$). Two-sample $z$-tests for synthetic (exp-001); paired $t$-tests for semi-synthetic (exp-003). Bold $p$-values indicate significance at $\\alpha = 0.05$.}\n\\label{tab:mcse}\n\\small\n\\begin{tabular}{llrr}\n\\toprule\nConfiguration & Comparison & $\\Delta$ & $p$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{HB EC-HTE vs.\\ Global ($|\\text{bias}|$)}} \\\\\n\\quad $K{=}2$/ext/$n{=}500$ & & $-0.046$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/ext/$n{=}500$ & & $-0.078$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/mod/$n{=}250$ & & $-0.017$ & $0.288$ \\\\\n\\quad TweetEval/ext/$n{=}250$ & & $+0.001$ & $0.395$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{HB EC-HTE vs.\\ Global (RMSE)}} \\\\\n\\quad $K{=}2$/ext/$n{=}500$ & & $+0.015$ & $0.179$ \\\\\n\\quad $K{=}4$/ext/$n{=}500$ & & $+0.048$ & $\\mathbf{0.011}$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{HB EC-HTE vs.\\ Naive ($|\\text{bias}|$)}} \\\\\n\\quad $K{=}2$/ext/$n{=}500$ & & $-0.089$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/ext/$n{=}500$ & & $-0.113$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/mod/$n{=}250$ & & $-0.031$ & $\\mathbf{0.038}$ \\\\\n\\quad TweetEval/ext/$n{=}250$ & & $+0.005$ & $\\mathbf{0.030}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder extreme heterogeneity, HB EC-HTE's bias advantage over global correction is highly significant ($p < 0.001$ for both $K{=}2$ and $K{=}4$).\nThe RMSE penalty of stratification is not significant at $K{=}2$ ($p = 0.179$) but reaches significance at $K{=}4$ ($p = 0.011$), consistent with the higher variance cost of estimating four confusion matrices.\nUnder moderate heterogeneity ($K{=}4$, $n{=}250$), the bias difference between HB and global is not significant ($p = 0.288$), confirming that EC-HTE's advantage requires sufficient error heterogeneity.\nIn the semi-synthetic TweetEval experiment, HB EC-HTE does not significantly improve over global ($p = 0.395$), consistent with moderate $\\Delta\\pi$ and unbalanced subgroup sizes.\nThe HB vs.\\ naive comparison in TweetEval is significant ($p = 0.030$) but favors naive, reflecting the variance cost of stratification when bias reduction is marginal.\n\n\\section{Semi-Real Confusion Matrix Validation}\n\\label{app:semireal}\n\nWe test EC-HTE with empirical asymmetric confusion matrices from the GPT-4.1 TweetEval pilot.\nFour text-feature subgroups ($K{=}4$) retain the real per-subgroup FPR and FNR from pilot annotations (Table~\\ref{tab:semireal_cm}); CATE heterogeneity is injected synthetically ($\\tau(z{=}0,s) = 0.3 + 0.1s$, $\\tau(z{=}1,s) = 0.8 - 0.15s$).\n$N{=}5{,}000$, $P(Z{=}1){=}0.18$, 100 MC seeds per $n_{\\text{expert}}$ level.\n\n\\begin{table}[t]\n\\centering\n\\caption{Empirical confusion matrices from GPT-4.1 TweetEval pilot.\nS0 exhibits FNR $= 0.526$, approaching chance-level classification.}\n\\label{tab:semireal_cm}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSubgroup & Weight & FPR & FNR & $\\kappa(\\hat{C}_s)$ \\\\\n\\midrule\nS0 & 0.38 & 0.054 & 0.526 & high \\\\\nS1 & 0.22 & 0.101 & 0.300 & moderate \\\\\nS2 & 0.14 & 0.143 & 0.308 & moderate \\\\\nS3 & 0.25 & 0.194 & 0.222 & low \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Semi-real confusion matrix results. RMSE and coverage averaged over subgroups and $z$-levels (100 MC runs). HB EC-HTE underperforms global at all budgets; S0's near-chance FNR drives the failure.}\n\\label{tab:semireal}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n$n_{\\text{expert}}$ & Method & RMSE $\\downarrow$ & Coverage $\\uparrow$ \\\\\n\\midrule\n\\multirow{4}{*}{100}\n & Oracle & 0.101 & 0.957 \\\\\n & Naive & 0.123 & 0.879 \\\\\n & Global & 0.263 & 0.885 \\\\\n & HB EC-HTE & 0.784 & 0.744 \\\\\n\\midrule\n\\multirow{4}{*}{250}\n & Oracle & 0.101 & 0.957 \\\\\n & Naive & 0.123 & 0.879 \\\\\n & Global & 0.232 & 0.909 \\\\\n & HB EC-HTE & 0.411 & 0.834 \\\\\n\\midrule\n\\multirow{4}{*}{500}\n & Oracle & 0.101 & 0.957 \\\\\n & Naive & 0.123 & 0.879 \\\\\n & Global & 0.196 & 0.922 \\\\\n & HB EC-HTE & 0.260 & 0.890 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHB EC-HTE produces higher RMSE and lower coverage than global correction at all expert budgets (Table~\\ref{tab:semireal}).\nThe root cause is S0's FNR $= 0.526$: when a confusion matrix row approaches a uniform distribution ($P(\\hat{Z}{=}1 \\mid Z{=}1) \\approx 0.5$), inversion amplifies estimation noise regardless of the expert budget.\nThis converges with the hate speech case study (Appendix~\\ref{app:hatespeech}, FNR $= 53.3$\\%) and confirms that EC-HTE requires \\emph{both} sufficient expert labels \\emph{and} sufficient baseline classifier quality per subgroup.\nThe singularity guard ($\\kappa > 100$, Section~\\ref{sec:method}) mitigates catastrophic failure by falling back to global correction for near-degenerate subgroups, but does not recover the bias reduction that motivates stratification.\nFor a $2 \\times 2$ symmetric confusion matrix, $\\kappa = 1/|1-2\\pi|$; $\\kappa > 100$ corresponds to $\\pi \\in (0.495, 0.505)$, so the guard triggers only when the classifier performs within $0.5\\%$ of random guessing.\nAt $n_{\\text{expert}} = 500$, HB EC-HTE narrows the gap (RMSE 0.260 vs.\\ 0.196) as confusion matrix estimates stabilize for the three well-classified subgroups, but the S0 bottleneck persists.\n\nA second semi-real experiment using GPT-3.5-Turbo confusion matrices (worst-subgroup FPR $= 0.39$, FNR $= 0.21$) yields similar results: HB RMSE exceeds global by 1.3--3.5$\\times$ at all budgets.\nHere the failure stems from high false-positive rates compounded by class imbalance ($P(Z{=}1) = 0.18$), which leaves insufficient expert observations in the positive class for reliable per-subgroup confusion matrix estimation.\nTogether, these experiments identify three applicability conditions for EC-HTE: (1)~sufficient effective expert budget ($n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$), (2)~no near-chance subgroup error rate ($\\max(\\text{FPR}_s, \\text{FNR}_s) < 0.5$), and (3)~adequate class balance in the effect modifier.\n\n\\paragraph{Diagnostic rule.}\nA logistic regression over all 368 semi-real experiment--budget cells (dependent variable: HB EC-HTE $<$ Global RMSE) identifies two sufficient statistics: the worst-subgroup confusion matrix condition number $\\kappa(\\hat{M}_s) \\leq 1.25$ and the effective minority-class expert count $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$.\nWhen both conditions hold, HB outperforms global in 93.3\\% of cells; when either is violated, global is preferred in 94.7\\% of cells.\nBoth exp-015 ($\\kappa = 2.38$, effective $n = 2.5$) and exp-016 ($\\kappa = 1.55$, effective $n = 2.5$) violate both conditions, and the diagnostic correctly predicts 100\\% of their failure cells.\nSubgroup-average metrics can mask cell-level heterogeneity: in exp-015, HB EC-HTE substantially reduces bias for the three well-classified subgroups (S1--S3) but amplifies variance in the near-degenerate subgroup (S0, FNR $= 0.526$), and the S0 penalty dominates the aggregate RMSE.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/applicability_frontier.pdf}\n\\caption{Applicability frontier of EC-HTE. Green region: EC-HTE reduces bias vs.\\ global correction. Yellow: comparable performance. Red: EC-HTE underperforms. Dashed lines mark the expert budget threshold ($n_{\\text{expert}}/K = 25$) and classifier quality threshold (worst-subgroup error rate $= 0.5$). Red diamonds show semi-real experiments with actual GPT-4.1 and GPT-3.5-Turbo confusion matrices.}\n\\label{fig:applicability}\n\\end{figure}\n\n\\section{Robustness: Estimator Choice and Treatment Effect Specification}\n\\label{app:rlearner}\n\nWe verify that EC-HTE's corrected pseudo-outcomes are compatible with downstream estimators beyond CausalForest by replacing it with the R-learner~\\citep{nie2021quasi}.\nThe experiment uses $K{=}2$, extreme heterogeneity, $n_{\\text{expert}} = 500$, and 50 MC seeds; the R-learner uses 5-fold cross-fitting with gradient-boosted trees as the base learner.\n\n\\begin{table}[t]\n\\centering\n\\caption{R-learner vs.\\ CausalForest with EC-HTE correction ($K{=}2$, extreme, $n{=}500$). $|\\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and seeds.}\n\\label{tab:rlearner}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nEstimator & Correction & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\n\\multirow{4}{*}{R-learner}\n & Oracle & 0.006 & 0.056 & 0.94 \\\\\n & Naive & 0.121 & 0.139 & 0.47 \\\\\n & Global & 0.098 & 0.123 & 0.72 \\\\\n & EC-HTE & \\textbf{0.013} & 0.080 & 0.92 \\\\\n\\midrule\n\\multirow{2}{*}{CausalForest}\n & Naive & 0.058 & 0.090 & 0.82 \\\\\n & EC-HTE & \\textbf{0.010} & 0.093 & 0.95 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE reduces R-learner $|\\text{bias}|$ by 89\\% (0.121 $\\to$ 0.013) and restores coverage from 0.47 to 0.92 (Table~\\ref{tab:rlearner}).\nThe bias reduction and coverage gains are comparable to those achieved with CausalForest, confirming that EC-HTE is compatible with a range of HTE estimators.\n\n\\paragraph{Multiplicative treatment effects.}\nWe further test robustness to the functional form of treatment effects by replacing the additive DGP with a multiplicative specification: $Y(1) = Y(0) \\times \\exp(\\tau(Z))$, using $K{=}2$, extreme heterogeneity, $n_{\\text{expert}} = 500$, and 50 MC seeds.\n\n\\begin{table}[t]\n\\centering\n\\caption{Multiplicative DGP results ($K{=}2$, extreme, $n{=}500$, 50 seeds). EC-HTE achieves comparable bias reduction and nominal coverage under non-additive treatment effects.}\n\\label{tab:multiplicative}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\nOracle & 0.003 & 0.038 & 0.96 \\\\\nNaive & 0.135 & 0.142 & 0.44 \\\\\nGlobal & 0.110 & 0.124 & 0.54 \\\\\nEC-HTE & \\textbf{0.054} & 0.068 & 0.955 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE reduces RMSE by 52\\% relative to naive (0.068 vs.\\ 0.142) and restores coverage to the nominal level (0.955; Table~\\ref{tab:multiplicative}).\nEC-HTE's bias correction operates at the confusion matrix level, independent of the downstream CATE estimator and functional form of treatment effects.\n\n\\section{Robustness to Class Imbalance}\n\\label{app:classimbalance}\n\nAssumption (A3) requires $P(Z{=}1) = 0.5$, but real-world effect modifiers are often imbalanced.\nWe sweep $P(Z{=}1) \\in \\{0.1, 0.2, 0.3, 0.4, 0.5\\}$ with $K \\in \\{2,4\\}$, extreme misclassification heterogeneity, $n_{\\text{expert}}{=}250$, and 100 MC seeds (Table~\\ref{tab:pz1_sweep}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Robustness to class imbalance ($n_{\\text{expert}}{=}250$, extreme heterogeneity). R$^2$: Theorem~\\ref{thm:bias_identity} fit. Ratio: HB/Global RMSE ($<1$ = HB wins). Cov.: HB EC-HTE 95\\% CI coverage.}\n\\label{tab:pz1_sweep}\n\\small\n\\begin{tabular}{cc ccc}\n\\toprule\n$P(Z{=}1)$ & $K$ & R$^2$ & Ratio & Cov. \\\\\n\\midrule\n0.1 & 2 & 0.998 & 0.92 & 0.94 \\\\\n0.2 & 2 & 0.989 & 0.76 & 0.94 \\\\\n0.3 & 2 & 0.994 & 0.78 & 0.94 \\\\\n0.4 & 2 & 0.995 & 0.87 & 0.94 \\\\\n0.5 & 2 & 0.995 & 0.86 & 0.93 \\\\\n\\midrule\n0.1 & 4 & 0.984 & 1.54 & 0.92 \\\\\n0.2 & 4 & 0.976 & 1.68 & 0.93 \\\\\n0.3 & 4 & 0.985 & 1.12 & 0.92 \\\\\n0.4 & 4 & 0.984 & 1.08 & 0.93 \\\\\n0.5 & 4 & 0.992 & 1.06 & 0.92 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTheorem~\\ref{thm:bias_identity}'s product form remains accurate across all imbalance levels: $R^2 \\geq 0.976$ even at $P(Z{=}1) = 0.1$, confirming that the bias identity derives from confusion matrix structure rather than class balance.\nFor $K{=}2$, EC-HTE outperforms global correction at all $P(Z{=}1)$ levels (RMSE ratio 0.76--0.92), degrading gracefully under severe imbalance.\nFor $K{=}4$, EC-HTE underperforms global at $n_{\\text{expert}}{=}250$ (ratio 1.06--1.68), consistent with the budget threshold $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$: at $P(Z{=}1){=}0.1$, $K{=}4$, each subgroup receives only ${\\sim}6$ minority-class labels.\nThe gap narrows as $P(Z{=}1)$ increases (1.54 $\\to$ 1.06), and coverage remains stable at 0.92--0.94 across all configurations.\n\n\\section{Comparison with PPI Correction}\n\\label{app:ppi_comparison}\n\nPPI~\\cite{angelopoulos2023ppi} constructs confidence intervals by combining a large set of ML predictions with a smaller set of gold-standard labels, using the gold labels to debias the ML-based estimator.\nApplied to our setting, PPI treats the LLM-annotated effect modifier as the ML prediction and the expert labels as the gold standard.\nTwo variants arise naturally: \\emph{PPI-global} pools all expert labels to estimate a single rectifier (analogous to our Global baseline), and \\emph{PPI-subgroup} estimates per-subgroup rectifiers (analogous to Stratified MLE).\n\nUnder the confusion-matrix parameterization we adopt, DSL's measurement error correction reduces to confusion matrix inversion.\nPooled DSL applies a single estimated confusion matrix to all subgroups, producing the same corrected label distribution as our Global baseline; per-subgroup DSL estimates a separate confusion matrix for each subgroup and inverts it independently, equivalent to our Stratified MLE.\nEC-HTE's contribution over both PPI-subgroup and per-subgroup DSL is hierarchical partial pooling: rather than estimating each subgroup's confusion matrix in isolation, EC-HTE places a shared prior across subgroups, borrowing strength to reduce variance while preserving subgroup-specific bias correction.\nThis mechanism is outside both the PPI and DSL frameworks.\n\nThe key difference between PPI and confusion-matrix inversion is that PPI does not invert the confusion matrix; instead, it uses the gold labels to directly debias the estimand.\nThis avoids the matrix inversion step that can amplify noise at small $n_{\\text{expert}}$, but it also means PPI cannot exploit the structure of the misclassification process to reduce bias.\nPPI-global inherits the same $\\Delta\\pi \\times \\Delta\\tau$ bias amplification as Global correction (Theorem~\\ref{thm:bias_identity}), confirming that the ``debiasing hurts'' mechanism operates regardless of the inference framework.\n\n\\section{Civil Comments Validation}\n\\label{app:civilcomments}\n\nTo verify that subgroup-heterogeneous misclassification generalizes beyond TweetEval, we annotate $N{=}3{,}000$ stratified samples (30\\% toxic) from Civil Comments~\\cite{borkan2019nuanced}, a toxicity detection dataset.\nSubgroups are defined by \\texttt{text\\_length\\_bin} $\\times$ \\texttt{has\\_question} ($K{=}4$): S0 (long, no question, 38.8\\%), S1 (long, question, 11.4\\%), S2 (short, no question, 33.7\\%), S3 (short, question, 16.1\\%).\nSubgroup features were chosen a priori based on observable text properties; no feature search was performed.\nThree proprietary LLMs annotate each sample via an OpenAI-compatible API, yielding 800--900 valid annotations per model.\n\nTable~\\ref{tab:civil_cm} reports per-subgroup FPR and FNR.\nWe define $\\Delta\\pi = \\max_s \\pi_s - \\min_s \\pi_s$, where $\\pi_s$ is the overall misclassification rate for subgroup $s$.\nAll three models exhibit $\\Delta\\pi > 0.05$, with overall heterogeneity $\\Delta\\pi \\in [0.113, 0.160]$---comparable to the $\\Delta\\pi \\in [0.125, 0.165]$ observed across four open-source LLMs on TweetEval (Appendix~\\ref{app:multilm_opensource}).\nGPT-4o-mini and GPT-3.5-turbo show pronounced FPR/FNR asymmetry (e.g., GPT-4o-mini FPR $\\in [0.42, 0.61]$ vs.\\ FNR $\\in [0.05, 0.16]$), indicating systematic over-prediction of toxicity; their FPR approaches 0.5, placing them in the ill-conditioned regime where confusion matrix inversion amplifies noise (consistent with the classifier quality threshold discussed in the Limitations section).\nThe consistent presence of $\\Delta\\pi$ heterogeneity across two NLP tasks, seven LLMs spanning open-source (7B--9B) and proprietary families, and two distinct subgroup definitions confirms that this phenomenon is a structural property of LLM annotation rather than an artifact of a specific dataset or model.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-subgroup misclassification rates on Civil Comments ($K{=}4$). $\\Delta$ denotes max $-$ min across subgroups.}\n\\label{tab:civil_cm}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Metric & S0 & S1 & S2 & S3 & $\\Delta$ \\\\\n\\midrule\nGPT-4o & FPR & 0.249 & 0.157 & 0.213 & 0.341 & 0.184 \\\\\n       & FNR & 0.160 & 0.263 & 0.308 & 0.328 & 0.168 \\\\\n\\midrule\nGPT-4o-mini & FPR & 0.517 & 0.541 & 0.419 & 0.610 & 0.191 \\\\\n            & FNR & 0.052 & 0.105 & 0.074 & 0.160 & 0.108 \\\\\n\\midrule\nGPT-3.5-turbo & FPR & 0.400 & 0.473 & 0.374 & 0.468 & 0.099 \\\\\n              & FNR & 0.139 & 0.211 & 0.173 & 0.240 & 0.101 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Bias Identity Validation with Real Confusion Matrices}\n\\label{app:realcm_bias}\n\nTheorem~\\ref{thm:bias_identity} is derived under symmetric misclassification (A2); real LLM confusion matrices are asymmetric (FPR $\\neq$ FNR).\nWe verify that the generalized identity $\\mathrm{bias}(z,s) = \\Delta\\tau \\cdot [B_s]_{z,1}$ (Remark~\\ref{thm:bias_identity}) holds under real annotation error structures by running semi-synthetic simulations ($N{=}5{,}000$, $K{=}4$, $\\Delta\\tau{=}0.30$, 100 MC runs) with confusion matrices drawn from 11 LLM--dataset combinations: eight models on TweetEval (GPT-4-turbo, GPT-4o, GPT-4.1, GPT-4o-mini, GPT-3.5-turbo, Qwen2.5-7B, Mistral-7B, Gemma-2-9B) and three on Civil Comments (GPT-4o, GPT-4o-mini, GPT-3.5-turbo).\n\nTable~\\ref{tab:realcm_r2} reports per-model $R^2$ from regressing observed subgroup bias on the predicted value $\\Delta\\tau \\cdot [B_s]_{z,1}$.\nThe aggregate $R^2 = 0.975$; 10 of 11 combinations achieve $R^2 \\geq 0.93$.\nThe single outlier (GPT-4o-mini on Civil Comments, $R^2{=}0.76$) has near-homogeneous subgroup error rates ($\\max|[B_s]_{z,1}| = 0.089$), so predicted biases are small and Monte Carlo noise dominates the regression.\n$R^2$ correlates strongly with $\\max|[B_s]_{z,1}|$: models with more heterogeneous per-subgroup error rates produce larger bias signals that are easier to verify empirically.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bias identity $R^2$ with real LLM confusion matrices ($K{=}4$, 100 MC runs).}\n\\label{tab:realcm_r2}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nModel & Dataset & $R^2$ & $\\max|[B_s]_{z,1}|$ \\\\\n\\midrule\nGPT-4-turbo  & TweetEval & 0.993 & 0.328 \\\\\nQwen2.5-7B   & TweetEval & 0.990 & 0.272 \\\\\nMistral-7B   & TweetEval & 0.990 & 0.242 \\\\\nGemma-2-9B   & TweetEval & 0.982 & 0.185 \\\\\nGPT-4o       & Civil Comments & 0.979 & 0.198 \\\\\nGPT-4o       & TweetEval & 0.975 & 0.240 \\\\\nGPT-4.1      & TweetEval & 0.969 & 0.139 \\\\\nGPT-3.5-turbo & TweetEval & 0.948 & 0.087 \\\\\nGPT-3.5-turbo & Civil Comments & 0.935 & 0.170 \\\\\nGPT-4o-mini  & TweetEval & 0.929 & 0.170 \\\\\nGPT-4o-mini  & Civil Comments & 0.756 & 0.089 \\\\\n\\midrule\n\\multicolumn{2}{l}{All (pooled)} & 0.975 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Applicability Screening with Real LLM Confusion Matrices}\n\\label{app:screening}\n\nWe apply the diagnostic conditions from Proposition~\\ref{prop:debiasing_hurts} and Section~\\ref{sec:method} to 16 LLM--dataset--$K$ combinations spanning seven LLMs (four open-source, three proprietary) across TweetEval and Civil Comments.\nTable~\\ref{tab:screening} summarizes which conditions each combination satisfies.\n\n\\begin{table}[h]\n\\centering\n\\caption{Diagnostic screening of 16 LLM--dataset--$K$ combinations. Columns report whether all subgroups satisfy each condition. Budget assumes $n_{\\text{expert}}{=}500$.}\n\\label{tab:screening}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Dataset & $K$ & $\\kappa{\\leq}1.25$ & $\\max{\\leq}0.5$ & Budget & Pass all \\\\\n\\midrule\nGemma-2-9B   & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nLlama-3.1-8B & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nMistral-7B   & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nQwen2.5-7B   & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGemma-2-9B   & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nLlama-3.1-8B & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nMistral-7B   & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nQwen2.5-7B   & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-3.5-turbo & CivilComm. & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-3.5-turbo & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4-turbo  & TweetEval & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4.1      & TweetEval & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o       & CivilComm. & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o       & TweetEval & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o-mini  & CivilComm. & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o-mini  & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nNo combination passes all three conditions; the bottleneck is $\\kappa(C_s) \\leq 1.25$, which requires $\\mathrm{FPR}_s + \\mathrm{FNR}_s \\lesssim 0.20$ for all subgroups---a threshold no current LLM achieves uniformly.\nThe closest are Qwen2.5-7B True\\_short ($\\kappa{=}1.23$) and Mistral-7B True\\_short ($\\kappa{=}1.27$).\n\nUnder a relaxed ``oracle screening'' that excludes near-degenerate subgroups ($\\max(\\mathrm{FPR}_s, \\mathrm{FNR}_s) \\geq 0.4$), we run semi-synthetic CATE estimation ($N{=}5{,}000$, $\\Delta\\tau{=}0.3$, 100 MC runs, $n_{\\text{expert}} \\in \\{250, 500\\}$) with each LLM's real per-subgroup confusion matrix.\nEC-HTE (HB) achieves lower RMSE than global correction in 41 of 52 comparisons (79\\%) and lower RMSE than stratified MLE in 52 of 52 comparisons (100\\%).\nThe four open-source LLMs on TweetEval show the strongest EC-HTE advantage (32/32 comparisons, RMSE reduction 0.001--0.008), while GPT-3.5-turbo/TweetEval (high FPR asymmetry, $\\mathrm{FPR}_{\\max}{=}0.39$) and GPT-4o/Civil Comments (low minority prevalence $P(Z{=}1){=}0.3$) show degradation.\nThe diagnostic correctly identifies the strict applicability regime; under relaxed conditions excluding near-degenerate subgroups, EC-HTE improves RMSE in 79\\% of comparisons.\n\n\\paragraph{Diagnostic Applicability Analysis.}\nThe diagnostic (Proposition~\\ref{prop:debiasing_hurts}) degrades on real LLM confusion matrices (pooled AUC $= 0.63$) because the failure mode is systematic: subgroups where the true CATE heterogeneity $\\tau_s \\approx 0$ are hurt by global correction (since $\\delta_s \\neq 0$ still introduces bias), yet these subgroups produce low diagnostic scores---the diagnostic ranks them as safe precisely when they are most vulnerable to overcorrection.\n\nA simple meta-criterion recovers reliability: compute $\\max_s |\\delta_s| / ((1 - 2\\bar{\\pi}) \\cdot \\pi_s)$ across subgroups.\nWhen $\\max_s \\mathrm{score}(s) > 1$, at least one subgroup is definitively harmed by global correction, and the diagnostic achieves AUC $\\geq 0.75$ across all 5 model--dataset combinations satisfying this condition (AUC range: 0.75--1.0).\nWhen $\\max_s \\mathrm{score}(s) \\leq 1$, global correction may or may not hurt depending on unobservable $\\Delta\\tau$; the diagnostic achieves AUC only 0.0--0.67 across the remaining 7 combinations (4 of 7 have AUC $< 0.5$, indicating anti-prediction).\nThis threshold perfectly separates reliable from unreliable diagnostic regimes across all 16 real LLM--dataset combinations evaluated.\n\nWe recommend the following practical protocol: (i) estimate per-subgroup confusion matrices from expert labels; (ii) compute $\\max_s \\mathrm{score}(s)$; (iii) if $> 1$, the diagnostic reliably identifies which subgroups are harmed by global correction---apply EC-HTE; (iv) if $\\leq 1$, the diagnostic is unreliable and practitioners should either default to EC-HTE as a conservative choice or evaluate correction strategies using held-out expert labels.\n\n\\section{Plug-in Standard Error Validation}\n\\label{app:bootstrap_se}\n\nA natural concern is whether the plug-in standard error adequately captures estimation uncertainty, particularly the additional variance introduced by confusion matrix estimation.\nWe verify this for the difference-in-means (DIM) estimator via Monte Carlo simulation ($K{=}2$, $n_{\\text{expert}} \\in \\{50, 100, 250, 500\\}$, 50 replications per budget level).\nAt each budget, we compute the plug-in 95\\% confidence interval and record empirical coverage.\nAcross all expert budgets, the plug-in SE yields coverage $\\geq 0.96$ (0.970, 0.960, 0.970, 0.970 for $n_{\\text{expert}} = 50, 100, 250, 500$), confirming that the analytic variance estimate is well-calibrated for the DIM estimator.\nThis self-calibration arises because the same noise in $\\hat{M}^{-1}$ that inflates point-estimate variance also inflates the plug-in SE, producing conservative intervals that maintain nominal coverage.\n\n\\paragraph{CausalForestDML.}\nUnder $K{=}2$ extreme heterogeneity ($\\pi{=}[0.05, 0.25]$, $n_{\\text{expert}}{=}250$, $n_{\\text{estimators}}{=}200$, 20 MC runs), EC-HTE plug-in SE achieves 93.8\\% aggregate coverage---close to the 94--96\\% oracle coverage (Table~\\ref{tab:cf_oracle}).\nThe high-error subgroup ($s_1$, $\\pi{=}0.25$) shows slightly lower plug-in coverage (92.5\\%) than the low-error subgroup ($s_0$: 95.0\\%), reflecting the larger $M^{-1}$ amplification of estimation uncertainty in subgroups with higher misclassification rates.\nBy contrast, the DIM plug-in SE achieves $\\geq$95\\% coverage in the same DGP, confirming that the analytic confusion matrix propagation formula is adequate for simpler estimators.\n\n\\paragraph{Full bootstrap SE.}\nA \\emph{full} bootstrap---resampling all $N$ observations and re-estimating both the confusion matrix and CausalForest per bootstrap replicate ($B{=}100$, $n_{\\text{estimators}}{=}200$, 20 MC runs)---confirms that plug-in SE is already near-nominal under standard hyperparameters.\nUnder $K{=}2$ extreme heterogeneity ($\\pi{=}[0.05, 0.25]$, $n_{\\text{expert}}{=}250$), plug-in SE achieves 93.8\\% aggregate coverage; the full bootstrap improves this to exactly 95.0\\% ($+$1.2pp).\nTable~\\ref{tab:bootstrap_se} reports per-subgroup results.\n\n\\begin{table}[h]\n\\centering\n\\caption{CausalForest coverage: plug-in SE vs.\\ full bootstrap SE ($B{=}100$, $n_{\\text{estimators}}{=}200$, 20 MC runs). Bootstrap SE is ${\\sim}1.15\\times$ plug-in.}\n\\label{tab:bootstrap_se}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nSubgroup & Plugin Cov. & Boot.\\ Cov. & Oracle Cov. & Plugin SE & Boot.\\ SE \\\\\n\\midrule\n$s_0$ ($\\pi{=}0.05$) & 0.950 & 0.925 & 0.925 & 0.059 & 0.063 \\\\\n$s_1$ ($\\pi{=}0.25$) & 0.925 & \\textbf{0.975} & 0.875 & 0.087 & 0.103 \\\\\n\\midrule\nAggregate & 0.938 & \\textbf{0.950} & 0.900 & 0.073 & 0.083 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe high-error subgroup ($s_1$) benefits most: coverage rises from 92.5\\% to 97.5\\% ($+$5.0pp), because the bootstrap captures the additional variance from $M^{-1}$ amplification.\nOracle coverage (90.0\\%) is consistent with the 94\\% reported in the oracle decomposition (Table~\\ref{tab:cf_oracle}), with the difference attributable to MC sampling noise at 20 runs.\nThe computational cost is substantial ($B \\times$ CF fits per MC run), but the approach is straightforward when exact nominal coverage is required.\n\n\\paragraph{Finite-sample remainder.}\nBy first-order matrix perturbation, $\\hat{C}_s^{-1} = C_s^{-1} - C_s^{-1} E_s C_s^{-1} + O(\\|E_s\\|^2)$, where $E_s = \\hat{C}_s - C_s$ satisfies $\\|E_s\\| = O_p(n_{\\text{expert}}^{-1/2})$.\nThe remainder in the corrected CATE is therefore $R_n = O_p(n_{\\text{expert}}^{-1/2} \\cdot \\|C_s^{-1}\\|^2) = O_p(n_{\\text{expert}}^{-1/2} \\cdot \\kappa(C_s))$, since $\\|C_s^{-1}\\| = O(\\kappa(C_s))$ for stochastic matrices.\nThis motivates the $\\kappa > 100$ singularity guard (Section~\\ref{sec:method}).\n\n\\subsection{CausalForest Oracle Coverage Decomposition}\n\\label{app:cf_oracle}\n\nTo isolate the source of CausalForest under-coverage, we compare six estimation strategies that progressively remove sources of uncertainty: (1)~Oracle (true $Z$, no correction), (2)~EC-HTE with true $C_s$, (3)~EC-HTE with estimated $\\hat{C}_s$ (HB), (4)~Global with true $\\bar{C}$, (5)~Global with estimated $\\hat{\\bar{C}}$, and (6)~Naive.\nTable~\\ref{tab:cf_oracle} reports coverage, $|\\text{bias}|$, and RMSE across three DGP configurations (100 MC runs each).\n\n\\begin{table}[h]\n\\centering\n\\caption{CausalForest oracle coverage decomposition. Coverage averaged over subgroups and $z$-levels.}\n\\label{tab:cf_oracle}\n\\small\n\\begin{tabular}{ll ccc}\n\\toprule\nDGP & Method & Cov.\\ (\\%) & $|\\text{Bias}|$ & RMSE \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{$K{=}4$, extreme\\\\$n{=}500$}}\n & Oracle (true $Z$)       & 94.5 & 0.006 & 0.078 \\\\\n & EC-HTE true $C_s$       & 92.5 & 0.008 & 0.114 \\\\\n & EC-HTE est.\\ $\\hat{C}_s$ & 93.1 & 0.015 & 0.121 \\\\\n & Global true $\\bar{C}$   & 91.3 & 0.037 & 0.110 \\\\\n & Global est.\\ $\\hat{\\bar{C}}$ & 91.1 & 0.038 & 0.111 \\\\\n & Naive                    & 88.3 & 0.045 & 0.095 \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{$K{=}2$, extreme\\\\$n{=}250$}}\n & Oracle (true $Z$)       & 94.0 & 0.002 & 0.056 \\\\\n & EC-HTE true $C_s$       & 94.0 & 0.003 & 0.073 \\\\\n & EC-HTE est.\\ $\\hat{C}_s$ & 92.5 & 0.004 & 0.079 \\\\\n & Global true $\\bar{C}$   & 88.5 & 0.045 & 0.083 \\\\\n & Global est.\\ $\\hat{\\bar{C}}$ & 88.3 & 0.045 & 0.085 \\\\\n & Naive                    & 82.8 & 0.046 & 0.077 \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{$K{=}2$, MF2 DGP\\\\$\\tau{=}(0.10,0.40)$}}\n & Oracle (true $Z$)       & 96.0 & 0.077 & 0.091 \\\\\n & EC-HTE true $C_s$       & 91.3 & 0.103 & 0.112 \\\\\n & EC-HTE est.\\ $\\hat{C}_s$ & 92.3 & 0.100 & 0.111 \\\\\n & Global true $\\bar{C}$   & 95.0 & 0.107 & 0.114 \\\\\n & Global est.\\ $\\hat{\\bar{C}}$ & 94.3 & 0.105 & 0.114 \\\\\n & Naive                    & 77.3 & 0.120 & 0.125 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree findings emerge.\nFirst, oracle coverage is 94--96\\% across all DGPs, confirming that CausalForest plug-in SE is well-calibrated when labels are correct.\nSecond, EC-HTE with true $C_s$ achieves 91--94\\% coverage---a 0--5pp gap from oracle (configuration-dependent), reflecting $M^{-1}$ SE propagation asymmetry across DGPs rather than confusion matrix estimation error.\nThird, the gap between true and estimated $C_s$ is ${\\leq}$1.5pp ($K{=}2$) and $<$1pp ($K{=}4$), confirming that CM estimation uncertainty contributes negligibly at $n_{\\text{expert}} \\geq 250$.\n\n\\section{Robustness to Assumption Violations}\n\\label{app:a5_violation}\n\n\\subsection{Assumption (A5): Subgroup-Specific Treatment Effects}\n\n\\begin{corollary}[Subgroup-Specific Treatment Effect Heterogeneity]\n\\label{cor:a5_relaxation}\nWhen $\\Delta\\tau$ varies across subgroups ($\\Delta\\tau_s = \\tau_s(1) - \\tau_s(0)$), the bias of global correction in subgroup $s$ at level $z{=}0$ is $+\\delta_s \\cdot \\Delta\\tau_s / (1 - 2\\bar{\\pi})$, and at level $z{=}1$ is $-\\delta_s \\cdot \\Delta\\tau_s / (1 - 2\\bar{\\pi})$.\n\\end{corollary}\nThe proof follows directly from Theorem~\\ref{thm:bias_identity} with $\\tau_s$ replacing $\\tau$.\n\nOur main analysis assumes that subgroup misclassification rates $\\delta_s$ and subgroup CATE magnitudes $\\Delta\\tau_s$ are independent (Assumption A5).\nIn practice, both may depend on text features that define subgroups, introducing correlation.\nWe test robustness under two configurations with the DIM estimator ($K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 50 MC replications, $\\pi = [0.05, 0.25]$):\n\\emph{aligned} (positive $\\delta_s$--$\\Delta\\tau_s$ correlation: high-error S1 has the larger treatment effect, $\\Delta\\tau = [0.30, 0.70]$) and\n\\emph{adversarial} (negative correlation: high-error S1 has the smaller effect, $\\Delta\\tau = [0.70, 0.30]$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Coverage and $|\\text{bias}|$ under A5 violation ($K{=}2$, $n_{\\text{expert}}{=}250$, 50 MC). Target coverage: 0.95.}\n\\label{tab:a5_violation}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nConfig & Method & S0 cov & S1 cov & S0 $|\\text{bias}|$ & S1 $|\\text{bias}|$ \\\\\n\\midrule\n\\multirow{4}{*}{Aligned}\n & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\\\\n & Naive         & 0.93 & 0.25 & 0.022 & 0.174 \\\\\n & Global        & 0.93 & 0.82 & 0.036 & 0.094 \\\\\n & EC-HTE (EB)   & 0.95 & 0.95 & 0.005 & 0.017 \\\\\n\\midrule\n\\multirow{4}{*}{Adversarial}\n & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\\\\n & Naive         & 0.90 & 0.78 & 0.042 & 0.074 \\\\\n & Global        & 0.74 & 0.93 & 0.098 & 0.040 \\\\\n & EC-HTE (EB)   & 0.94 & 0.96 & 0.002 & 0.007 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn the aligned configuration, the $\\delta_s \\times \\Delta\\tau_s$ product is maximized in the high-error subgroup, causing naive S1 coverage to collapse to 0.25.\nGlobal correction improves S1 but cannot fully correct without subgroup-specific error rates.\nIn the adversarial configuration, global correction overcorrects the low-error subgroup (S0 coverage 0.74).\nEC-HTE (EB) maintains $\\geq 0.94$ coverage across both subgroups in both configurations, with bias comparable to the oracle.\nResults at $n_{\\text{expert}}{=}500$ are consistent (all EC-HTE coverages $\\in [0.93, 0.99]$).\n\n\\subsection{Assumption (A1): Sensitivity to Outcome-Dependent Misclassification}\n\\label{app:a1_sensitivity}\n\nWe assess EC-HTE's robustness when misclassification depends on potential outcomes, violating~(A1).\nWe modify the synthetic DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$) so that misclassification probability becomes outcome-dependent: $P(\\hat{Z}{\\neq}Z \\mid Z, S, Y) = \\mathrm{clamp}(\\pi_s + \\gamma \\cdot (Y - \\mu_Y)/\\sigma_Y,\\, 0,\\, 1)$, where $\\gamma \\in \\{0, 0.05, 0.10, 0.15, 0.20\\}$ controls the strength of violation.\nTable~\\ref{tab:a1_sensitivity} reports results averaged over 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{Sensitivity to Assumption~(A1) violation. Coverage and $|\\text{bias}|$ under outcome-dependent misclassification ($\\gamma > 0$).}\n\\label{tab:a1_sensitivity}\n\\small\n\\begin{tabular}{lccc ccc}\n\\toprule\n& \\multicolumn{3}{c}{Coverage (\\%)} & \\multicolumn{3}{c}{$|\\text{Bias}|$} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n$\\gamma$ & EC-HTE & Global & Naive & EC-HTE & Global & Naive \\\\\n\\midrule\n0.00 & 95.5 & 92.7 & 87.7 & 0.060 & 0.065 & 0.061 \\\\\n0.05 & 95.5 & 93.5 & 83.8 & 0.059 & 0.064 & 0.064 \\\\\n0.10 & 95.3 & 93.8 & 83.5 & 0.063 & 0.064 & 0.067 \\\\\n0.15 & 94.8 & 94.3 & 79.2 & 0.065 & 0.064 & 0.070 \\\\\n0.20 & 93.5 & 94.0 & 79.5 & 0.068 & 0.063 & 0.073 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE maintains near-nominal coverage ($\\geq$93.5\\%) across the full $\\gamma$ range, with $|\\text{bias}|$ increasing only 13.7\\% from $\\gamma{=}0$ to $\\gamma{=}0.2$.\nAll correction methods (Global, Stratified MLE, HB) maintain $\\geq$90\\% coverage, indicating that moderate (A1) violations do not catastrophically degrade confusion-matrix-based correction.\nThe naive estimator degrades most rapidly (coverage $-$8.2pp), consistent with outcome-dependent misclassification compounding the uncorrected label noise.\n\n\\subsection{Extension to Confounded Treatment Assignment}\n\\label{app:confounded_dgp}\n\nEC-HTE's confusion matrix correction operates on estimated CATEs regardless of how those estimates are produced.\nTo verify compatibility with observational (non-RCT) designs, we pair EC-HTE with an inverse probability weighted difference-in-means (IPW-DIM) estimator under confounded treatment assignment.\n\n\\paragraph{DGP.}\n$N{=}5{,}000$, $K{=}2$, $\\pi = [0.05, 0.25]$, $n_{\\text{expert}}{=}250$, 100 MC replications.\nA covariate $X \\sim \\mathcal{N}(0,1)$ confounds both treatment and outcome:\n$T \\sim \\text{Bernoulli}(\\sigma(\\beta X))$ with $\\beta{=}0.5$ (moderate confounding; propensity range $[0.38, 0.62]$),\n$Y = 1 + 0.5 Z + 0.3 X + \\tau(Z) \\cdot T + \\varepsilon$, $\\varepsilon \\sim \\mathcal{N}(0,1)$.\nTreatment effects are $\\tau(Z{=}0){=}0$, $\\tau(Z{=}1){=}0.3$.\nThe IPW-DIM estimator uses \\emph{oracle propensity} $e(X) = \\sigma(\\beta X)$, with propensity scores clipped to $[0.05, 0.95]$.\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE under confounded treatment assignment (IPW-DIM with oracle propensity, $\\beta{=}0.5$, 100 MC).}\n\\label{tab:confounded_dgp}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Coverage & RMSE & $|\\text{Bias}|$ \\\\\n\\midrule\nOracle (true $Z$ + IPW) & 0.943 & 0.061 & 0.048 \\\\\nHB EC-HTE              & 0.950 & 0.086 & 0.068 \\\\\nGlobal                  & 0.930 & 0.087 & 0.071 \\\\\nStrat MLE               & 0.950 & 0.087 & 0.069 \\\\\nNaive                   & 0.863 & 0.083 & 0.066 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE achieves 95.0\\% coverage, within 0.7pp of the oracle (94.3\\%), confirming that confusion matrix correction and propensity weighting compose without interference.\nThe improvement is most pronounced in the high-error subgroup ($\\pi{=}0.25$): EC-HTE coverage is 96.0\\% vs.\\ naive 78.5\\% ($+$17.5pp).\nGlobal coverage (93.0\\%) falls below the correction methods (95.0\\%), consistent with the cost of ignoring subgroup-level error heterogeneity even in the confounded setting.\n\n\\paragraph{Sensitivity to confounding strength and propensity estimation.}\nWe sweep $\\beta \\in \\{0.25, 0.5, 1.0, 2.0\\}$ and compare oracle propensity ($e(X) = \\sigma(\\beta X)$) with estimated propensity (logistic regression fit on $(X, T)$), yielding 8 configurations (100 MC each).\nTable~\\ref{tab:confounded_sweep} reports HB EC-HTE and naive coverage.\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE coverage across confounding strengths and propensity sources. The logistic regression propensity model is correctly specified; propensity misspecification is a complementary concern addressed by the IPW literature.}\n\\label{tab:confounded_sweep}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n$\\beta$ & Propensity & HB Coverage & Naive Coverage \\\\\n\\midrule\n0.25 & Oracle    & 0.963 & 0.848 \\\\\n0.25 & Estimated & 0.973 & 0.845 \\\\\n0.50 & Oracle    & 0.950 & 0.863 \\\\\n0.50 & Estimated & 0.958 & 0.858 \\\\\n1.00 & Oracle    & 0.958 & 0.898 \\\\\n1.00 & Estimated & 0.960 & 0.883 \\\\\n2.00 & Oracle    & 0.945 & 0.858 \\\\\n2.00 & Estimated & 0.948 & 0.858 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE maintains coverage $\\geq$94.5\\% across all 8 configurations, including strong confounding ($\\beta{=}2.0$, propensity range $[0.12, 0.88]$).\nThe oracle--estimated gap is $\\leq$1pp, confirming that propensity estimation error does not meaningfully degrade EC-HTE when the propensity model is correctly specified.\nThis validates that EC-HTE is robust to confounded treatment assignment when the propensity model is correctly specified.\n\n\\subsection{Empirical Comparison with Frazis--Loewenstein Correction}\n\\label{app:fl_comparison}\n\nWe empirically compare EC-HTE's confusion matrix inversion against the scalar attenuation correction of \\citet{frazis2003estimating} (F-L).\nThe F-L correction rescales the observed estimate as $\\hat{\\tau}_{\\text{FL}} = \\hat{\\tau}_{\\text{obs}} / (1 - 2\\bar{\\pi})$, where $\\bar{\\pi}$ is the (global or per-subgroup) misclassification rate.\nWe test two variants: F-L \\emph{scalar} (single global $\\bar{\\pi}$) and F-L \\emph{per-subgroup} ($\\pi_s$-specific rescaling).\nSetup: $K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, $\\pi{=}[0.05, 0.25]$ (extreme heterogeneity), $\\tau(z{=}0){=}0$, $\\tau(z{=}1){=}0.3$, 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{F-L correction vs.\\ EC-HTE under heterogeneous misclassification ($\\Delta\\pi{=}0.20$). Both F-L variants produce \\emph{higher} aggregate bias than the uncorrected estimator.}\n\\label{tab:fl_comparison}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Coverage \\\\\n\\midrule\nOracle         & 0.045 & 0.056 & 0.943 \\\\\nNaive          & 0.062 & 0.077 & 0.858 \\\\\nGlobal (CM inv)& 0.064 & 0.081 & 0.938 \\\\\nHB EC-HTE      & 0.064 & 0.086 & \\textbf{0.953} \\\\\nF-L Scalar     & 0.091 & 0.116 & 0.850 \\\\\nF-L Per-Subgroup & 0.112 & 0.158 & 0.838 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth F-L variants produce \\emph{higher} bias and RMSE than the naive estimator (F-L per-subgroup $|\\text{bias}|{=}0.112$ vs.\\ naive $0.062$), demonstrating that scalar attenuation cannot substitute for confusion matrix inversion under subgroup-heterogeneous misclassification.\nThe per-subgroup bias direction reveals the mechanism: F-L scalar over-corrects the low-error subgroup ($s_0$: mean bias ${=}+0.073$ vs.\\ naive $+0.005$, a $14.6\\times$ amplification), while F-L per-subgroup dramatically over-corrects the high-error subgroup ($s_1$: mean bias ${=}+0.160$).\nEC-HTE achieves near-zero per-subgroup bias ($s_0{:}\\,{+}0.006$, $s_1{:}\\,{+}0.001$) with nominal coverage (95.3\\%).\nThe root cause is structural: F-L's $1/(1{-}2\\pi)$ scaling amplifies each $z$-level estimate independently, whereas CM inversion simultaneously redistributes the cross-contamination between misclassified and correctly classified observations.\n\n\\subsection{End-to-End Validation with Asymmetric Confusion Matrices}\n\\label{app:asymmetric_endtoend}\n\nWe validate EC-HTE under strongly asymmetric confusion matrices ($\\text{FPR}/\\text{FNR}$ ratio up to $7{:}1$), simulating the error profile of GPT-4.1 on Civil Comments.\nSetup: $K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$; $s_0$: $\\text{FPR}{=}0.05$, $\\text{FNR}{=}0.02$ (low error); $s_1$: $\\text{FPR}{=}0.38$, $\\text{FNR}{=}0.054$ ($7{:}1$ ratio); 100 MC runs.\nWe compare EC-HTE using the full $2{\\times}2$ asymmetric CM (Remark~2) against the symmetric assumption ($\\text{FPR}{=}\\text{FNR}{=}\\pi_s$).\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE under asymmetric misclassification ($\\text{FPR}/\\text{FNR}$ up to $7{:}1$). The asymmetric formula improves coverage by $+1.5$pp and RMSE by $11.5\\%$.}\n\\label{tab:asymmetric_endtoend}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Coverage \\\\\n\\midrule\nOracle              & 0.045 & 0.056 & 0.943 \\\\\nEC-HTE (asymmetric) & 0.057 & 0.074 & \\textbf{0.945} \\\\\nNaive               & 0.059 & 0.073 & 0.870 \\\\\nGlobal (asymmetric) & 0.061 & 0.076 & 0.915 \\\\\nEC-HTE (symmetric)  & 0.062 & 0.083 & 0.930 \\\\\nGlobal (symmetric)  & 0.063 & 0.078 & 0.915 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE with the asymmetric formula achieves 94.5\\% coverage versus 93.0\\% under the symmetric assumption ($+1.5$pp), with RMSE improved from 0.083 to 0.074 ($-11.5\\%$).\nThe improvement concentrates in the high-error subgroup ($s_1$): asymmetric coverage is 93.0\\% vs.\\ symmetric 91.0\\%.\nPractitioners should estimate full $2 \\times 2$ confusion matrices rather than assuming symmetric misclassification, particularly when FPR and FNR differ substantially.\n\n\\subsection{Complementarity with LLM Calibration}\n\\label{app:calibration}\n\nTemperature or Platt scaling~\\cite{guo2017calibration} can reduce per-subgroup misclassification rates, but does not eliminate heterogeneity $\\Delta\\pi$.\nWe simulate calibration by shrinking per-subgroup rates from $\\pi{=}[0.05, 0.25]$ ($\\Delta\\pi{=}0.20$) to $\\pi{=}[0.08, 0.15]$ ($\\Delta\\pi{=}0.07$), testing whether EC-HTE remains necessary post-calibration.\nSetup: $K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{Calibration reduces $\\Delta\\pi$ but does not eliminate it; EC-HTE corrects the residual bias. Best coverage is achieved by combining both.}\n\\label{tab:calibration}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Coverage \\\\\n\\midrule\nOracle                    & 0.043 & 0.053 & 0.963 \\\\\nCalibrated + EC-HTE       & 0.055 & 0.069 & \\textbf{0.965} \\\\\nCalibrated + Global       & 0.055 & 0.068 & 0.963 \\\\\nCalibrated + Naive        & 0.051 & 0.064 & 0.913 \\\\\nUncalibrated + EC-HTE     & 0.064 & 0.084 & 0.938 \\\\\nUncalibrated + Global     & 0.069 & 0.085 & 0.920 \\\\\nUncalibrated + Naive      & 0.063 & 0.079 & 0.840 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCalibration alone improves naive coverage from 84.0\\% to 91.3\\% but does not reach the nominal 95\\%.\nCalibrated + EC-HTE achieves the highest coverage (96.5\\%), demonstrating that calibration and EC-HTE address orthogonal error sources: calibration reduces per-subgroup $\\pi_s$ while EC-HTE corrects the residual $\\delta_s$-driven bias from heterogeneity that persists post-calibration.\nPropensity estimation robustness under model misspecification is an orthogonal concern addressed by the IPW literature; EC-HTE as a downstream correction layer does not alter IPW behavior.\n",
    "structuredPatch": [
      {
        "oldStart": 1346,
        "oldLines": 5,
        "newStart": 1346,
        "newLines": 5,
        "lines": [
          " \\end{table}",
          " ",
          " Calibration alone improves naive coverage from 84.0\\% to 91.3\\% but does not reach the nominal 95\\%.",
          "-Calibrated + EC-HTE achieves the highest coverage (96.5\\%), demonstrating that calibration and EC-HTE address orthogonal error sources: calibration reduces per-subgroup $\\pi_s$ while EC-HTE corrects the residual $\\delta_s$-driven bias from heterogeneity that persists post-calibration.",
          "+Calibrated + EC-HTE achieves the highest coverage (96.5\\%), demonstrating that calibration and EC-HTE address complementary error sources: calibration reduces per-subgroup $\\pi_s$ while EC-HTE corrects the residual $\\delta_s$-driven bias from heterogeneity that persists post-calibration.",
          " Propensity estimation robustness under model misspecification is an orthogonal concern addressed by the IPW literature; EC-HTE as a downstream correction layer does not alter IPW behavior."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Edit · `toolu_01PvFrcFopZ8NTuAGvntZ19Y`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "old_string": "Propensity estimation robustness under model misspecification is an orthogonal concern addressed by the IPW literature",
  "new_string": "Propensity estimation robustness under model misspecification is a complementary concern addressed by the IPW literature"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "6b22c6f1-bcbc-4d4d-9d8a-1c7b0caf705a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfTCbq1mJavYLkU3D8YAFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14448,
      "cache_read_input_tokens": 53368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14448
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-23T09:29:48.410Z_

<details><summary>↩ Tool result · `toolu_01PvFrcFopZ8NTuAGvntZ19Y`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "a241eb5b-6e54-459f-be97-f7e1444fb040",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
    "oldString": "Propensity estimation robustness under model misspecification is an orthogonal concern addressed by the IPW literature",
    "newString": "Propensity estimation robustness under model misspecification is a complementary concern addressed by the IPW literature",
    "originalFile": "\\section{EC-HTE Procedure}\n\\label{app:algorithm}\n\n\\begin{algorithm}[t]\n\\caption{EC-HTE: Error-Corrected Heterogeneous Treatment Effects}\n\\label{alg:echte}\n\\begin{algorithmic}[1]\n\\Require Observations $\\{(Y_i, W_i, \\hat{Z}_i, X_i)\\}_{i=1}^N$; expert labels $\\{Z_j^*\\}_{j=1}^{n_{\\text{expert}}}$; subgroup map $S: \\mathcal{X} \\to \\{1,\\ldots,K\\}$\n\\Ensure Corrected CATE estimates $\\hat{\\tau}(z)$ with variance-adjusted CIs\n\\Statex\n\\State \\textbf{Preconditions:} verify $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$ and $\\max_s(\\text{FPR}_s, \\text{FNR}_s) < 0.5$; if either fails, use global correction\n\\Statex\n\\State \\textbf{Step 1: Estimate per-subgroup confusion matrices (HB)}\n\\For{$s = 1, \\ldots, K$}\n    \\State $C_s[j,\\cdot] \\sim \\mathrm{Dir}(\\alpha_0 \\cdot \\hat{C}_{\\text{global},j})$, \\; $\\alpha_0$ via empirical Bayes\n    \\State Gibbs sampler (4 chains, 4000 iter) on $\\{(\\hat{Z}_j, Z_j^*) : S_j = s\\}$\n    \\State $\\hat{C}_s \\gets$ posterior mean; verify $\\hat{R} < 1.01$\n\\EndFor\n\\Statex\n\\State \\textbf{Step 2: Correct observed outcome moments}\n\\For{$s = 1, \\ldots, K$}\n    \\If{$\\kappa(\\hat{C}_s) > 100$} $\\hat{C}_s \\gets \\bar{C}$ \\Comment{singularity guard}\n    \\EndIf\n    \\State $\\tilde{\\boldsymbol{\\mu}}_s \\gets \\hat{C}_s^{-1} \\hat{\\boldsymbol{\\mu}}_s$\n\\EndFor\n\\Statex\n\\State \\textbf{Step 3: CausalForestDML with variance-adjusted SEs}\n\\State Train CausalForest (honest splitting) on corrected outcome moments $\\tilde{\\boldsymbol{\\mu}}_s$\n\\State $\\mathrm{se}_{\\mathrm{adj},i} \\gets \\sqrt{\\mathrm{diag}(\\hat{C}_{S_i}^{-1}\\, \\mathrm{diag}(\\mathrm{se}_i^2)\\, \\hat{C}_{S_i}^{-\\top})}$\n\\State \\Return $\\hat{\\tau}(z)$ with 95\\% CIs from $\\mathrm{se}_{\\mathrm{adj}}$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\subsection{Condition Number Guard Ablation}\n\\label{app:kappa_ablation}\n\nThe singularity guard in Algorithm~\\ref{alg:echte} (line~6) falls back to global correction when $\\kappa(\\hat{C}_s) > 100$.\nWe verify that this threshold is not load-bearing by sweeping $\\kappa \\in \\{10, 25, 50, 100, 200, 500, 1000\\}$ under the standard DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 100 MC runs).\nAcross all configurations, the maximum observed condition number is $\\kappa_{\\max} = 1.89$ (mean 1.45, p99 1.89), providing a $53{\\times}$ safety margin below the $\\kappa{=}100$ threshold.\nConsequently, the guard never triggers at any tested threshold, and all $\\kappa$ values produce identical RMSE (HB: 0.076, Global: 0.077) and zero numerical instability.\nIn a stress test with near-random labeling ($\\pi_s \\approx 0.4$--$0.5$, $n_{\\text{expert}}{=}50$), the maximum condition number reaches 1{,}125, correctly triggering the $\\kappa{=}100$ guard and preventing catastrophic inversion.\nThe adaptive formula $\\kappa_{\\text{adapt}} = 10 \\sqrt{n_{\\text{expert}} / K}$ recovers $\\kappa{=}100$ for this regime and scales naturally with the estimation precision.\n\n\\section{Full Proof of Theorem~\\ref{thm:bias_identity}}\n\\label{app:derivation}\n\n\\paragraph{Setup.}\nUnder assumptions (A1)--(A4), the observed CATE in subgroup $s$ at effect-modifier level $z$ is\n\\begin{equation}\n\\tau_{\\text{obs}}(z, s) = \\sum_{z'} M_s[z, z'] \\cdot \\tau(z'),\n\\end{equation}\nwhere $M_s[z, z'] = P(Z{=}z' \\mid \\hat{Z}{=}z, S{=}s)$ is the mixing matrix.\nUnder (A2)--(A3), $M_s = \\bigl[\\begin{smallmatrix} 1-\\pi_s & \\pi_s \\\\ \\pi_s & 1-\\pi_s \\end{smallmatrix}\\bigr]$.\n\n\\paragraph{Global correction.}\nThe pooled mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s = \\bigl[\\begin{smallmatrix} 1-\\bar{\\pi} & \\bar{\\pi} \\\\ \\bar{\\pi} & 1-\\bar{\\pi} \\end{smallmatrix}\\bigr]$, with $\\bar{\\pi} = \\sum_s w_s \\pi_s$.\n\nGlobal correction applies $M_{\\text{global}}^{-1}$ to $\\tau_{\\text{obs}}(\\cdot, s)$:\n\\begin{equation}\n\\hat{\\tau}_{\\text{global}}(z, s) = [M_{\\text{global}}^{-1} M_s \\cdot \\boldsymbol{\\tau}]_z,\n\\end{equation}\nwhere $\\boldsymbol{\\tau} = [\\tau(0), \\tau(1)]^\\top$.\n\n\\paragraph{Bias computation.}\nThe bias is $\\hat{\\tau}_{\\text{global}}(z, s) - \\tau(z) = [(M_{\\text{global}}^{-1} M_s - I) \\boldsymbol{\\tau}]_z$.\n\nDirect computation gives:\n\\begin{equation}\nM_{\\text{global}}^{-1} = \\frac{1}{1 - 2\\bar{\\pi}} \\begin{bmatrix} 1-\\bar{\\pi} & -\\bar{\\pi} \\\\ -\\bar{\\pi} & 1-\\bar{\\pi} \\end{bmatrix}.\n\\end{equation}\nMultiplying by $M_s$:\n\\begin{equation}\n\\resizebox{.88\\columnwidth}{!}{$\\displaystyle\nM_{\\text{global}}^{-1} M_s = \\frac{1}{1-2\\bar{\\pi}} \\begin{bmatrix} (1{-}\\bar{\\pi})(1{-}\\pi_s) - \\bar{\\pi}\\pi_s & (1{-}\\bar{\\pi})\\pi_s - \\bar{\\pi}(1{-}\\pi_s) \\\\ -\\bar{\\pi}(1{-}\\pi_s) + (1{-}\\bar{\\pi})\\pi_s & -\\bar{\\pi}\\pi_s + (1{-}\\bar{\\pi})(1{-}\\pi_s) \\end{bmatrix}.\n$}\n\\end{equation}\n\nDefine $\\delta_s = \\pi_s - \\bar{\\pi}$. Substituting $\\pi_s = \\bar{\\pi} + \\delta_s$:\n\\begin{equation}\nM_{\\text{global}}^{-1} M_s - I = \\frac{\\delta_s}{1-2\\bar{\\pi}} \\begin{bmatrix} -1 & 1 \\\\ 1 & -1 \\end{bmatrix}.\n\\end{equation}\n\nTo verify: the $(1,1)$ entry of $M_{\\text{global}}^{-1} M_s$ is\n{\\small\n\\begin{align}\n&\\frac{(1{-}\\bar{\\pi})(1{-}\\bar{\\pi}{-}\\delta_s) - \\bar{\\pi}(\\bar{\\pi}{+}\\delta_s)}{1-2\\bar{\\pi}} \\nonumber\\\\\n&= \\frac{(1{-}\\bar{\\pi})^2 - (1{-}\\bar{\\pi})\\delta_s - \\bar{\\pi}^2 - \\bar{\\pi}\\delta_s}{1-2\\bar{\\pi}} \\nonumber\\\\\n&= \\frac{1 - 2\\bar{\\pi} - \\delta_s}{1-2\\bar{\\pi}} = 1 - \\frac{\\delta_s}{1-2\\bar{\\pi}}.\n\\end{align}\n}\n\nApplying $(M_{\\text{global}}^{-1} M_s - I)$ to $\\boldsymbol{\\tau}$:\n{\\small\n\\begin{align}\n\\text{bias}(z{=}0, s) &= \\tfrac{\\delta_s}{1-2\\bar{\\pi}}(-\\tau(0) + \\tau(1)) = +\\tfrac{\\delta_s \\cdot \\Delta\\tau}{1-2\\bar{\\pi}}, \\\\\n\\text{bias}(z{=}1, s) &= \\tfrac{\\delta_s}{1-2\\bar{\\pi}}(\\tau(0) - \\tau(1)) = -\\tfrac{\\delta_s \\cdot \\Delta\\tau}{1-2\\bar{\\pi}},\n\\end{align}\n}\nwhere $\\Delta\\tau = \\tau(1) - \\tau(0)$. \\qed\n\n\\section{Multi-class Extension and Proof}\n\\label{app:multiclass}\n\n\\begin{corollary}[Multi-class Extension]\n\\label{cor:multiclass}\nFor $K > 2$ subgroups with $J$ effect-modifier levels and uniform off-diagonal misclassification (misclassified observations from class $j$ are distributed equally among the remaining $J{-}1$ classes), the subgroup bias of global correction generalizes to\n\\begin{equation}\n\\mathrm{bias}_{\\mathrm{global}}(z, s) = \\sum_{j=1}^{J} \\bigl(\\bar{\\pi}_j - \\pi_{s,j}\\bigr) \\cdot \\bigl(\\tau(j) - \\bar{\\tau}\\bigr) \\cdot g(\\bar{\\pi}),\n\\label{eq:multiclass}\n\\end{equation}\nwhere $g(\\bar{\\pi})$ collects the matrix-inversion amplification terms.\\footnote{For $J=3$ with symmetric misclassification (off-diagonal errors uniform), $g(\\bar{\\pi}) = 1/(1 - 3\\bar{\\pi}/2)$, generalizing the $J{=}2$ factor $1/(1-2\\bar{\\pi})$. In general, $g(\\bar{\\pi}) = 1/(1 - J\\bar{\\pi}/(J-1))$.}\nThe essential structure, $\\sum_s w_s (\\bar{\\pi}_j - \\pi_{s,j}) = 0$, ensures that bias redistributes across subgroups rather than vanishing in aggregate.\n\\end{corollary}\n\n\\paragraph{Proof.}\nFor $K > 2$ subgroups with $J$ effect-modifier levels, the subgroup-specific mixing matrix $M_s$ is $J \\times J$ with entries $M_s[j, j'] = P(Z{=}j' \\mid \\hat{Z}{=}j, S{=}s)$.\nThe global mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s$.\n\nThe bias of global correction in subgroup $s$ at level $z$ is:\n\\begin{equation}\n\\text{bias}_{\\text{global}}(z, s) = [(M_{\\text{global}}^{-1} M_s - I) \\boldsymbol{\\tau}]_z.\n\\end{equation}\n\nWrite $M_s = M_{\\text{global}} + \\Delta_s$ where $\\Delta_s = M_s - M_{\\text{global}}$ satisfies $\\sum_s w_s \\Delta_s = 0$.\nThen $M_{\\text{global}}^{-1} M_s = I + M_{\\text{global}}^{-1} \\Delta_s$, so:\n\\begin{equation}\n\\text{bias}_{\\text{global}}(z, s) = [M_{\\text{global}}^{-1} \\Delta_s \\cdot \\boldsymbol{\\tau}]_z.\n\\end{equation}\n\nFor symmetric misclassification with per-class error rates $\\pi_{s,j}$ and pooled rates $\\bar{\\pi}_j$, the entries of $\\Delta_s$ have the form $\\Delta_s[j,j'] = (\\bar{\\pi}_j - \\pi_{s,j}) \\cdot h(j, j')$ for a function $h$ determined by the off-diagonal redistribution pattern.\nExpanding the matrix-vector product and collecting terms yields:\n\\begin{equation}\n\\text{bias}_{\\text{global}}(z, s) = \\sum_{j=1}^{J} (\\bar{\\pi}_j - \\pi_{s,j}) \\cdot (\\tau(j) - \\bar{\\tau}) \\cdot g(\\bar{\\pi}),\n\\end{equation}\nwhere $g(\\bar{\\pi})$ collects the matrix-inversion amplification terms and $\\bar{\\tau} = \\sum_j P(Z{=}j) \\tau(j)$.\n\nThe essential structure $\\sum_s w_s (\\bar{\\pi}_j - \\pi_{s,j}) = 0$ ensures that the weighted bias across subgroups sums to zero: global correction redistributes bias rather than creating or eliminating it in aggregate.\nFor non-uniform off-diagonal entries, the scalar amplification $g(\\bar{\\pi})$ generalizes to a cell-specific matrix; the product structure $B_s \\cdot \\Delta\\tau$ persists but a closed-form amplification factor does not. \\qed\n\n\\section{Proof of Proposition~\\ref{prop:debiasing_hurts}}\n\\label{app:debiasing_hurts}\n\nThe naive estimator has bias $\\tau_{\\text{obs}}(z,s) - \\tau(z)$.\nUnder (A2)--(A3), $\\tau_{\\text{obs}}(0,s) = (1-\\pi_s)\\tau(0) + \\pi_s\\tau(1)$, so $\\text{bias}_{\\text{naive}}(0,s) = \\pi_s \\cdot \\Delta\\tau$.\n\nGlobal correction produces larger absolute bias when $|\\text{bias}_{\\text{global}}(0,s)| > |\\text{bias}_{\\text{naive}}(0,s)|$:\n\\begin{equation}\n\\frac{|\\delta_s| \\cdot |\\Delta\\tau|}{|1-2\\bar{\\pi}|} > \\pi_s \\cdot |\\Delta\\tau|.\n\\end{equation}\nSince $\\Delta\\tau \\neq 0$ (otherwise both biases are zero), dividing through gives:\n\\begin{equation}\n\\frac{|\\delta_s|}{(1-2\\bar{\\pi}) \\cdot \\pi_s} > 1,\n\\end{equation}\nwhere we use $1-2\\bar{\\pi} > 0$ from (A4).\n\nFor high-error subgroups ($\\pi_s > \\bar{\\pi}$, so $\\delta_s > 0$): the condition becomes $(\\pi_s - \\bar{\\pi}) / ((1-2\\bar{\\pi})\\pi_s) > 1$, which simplifies to $\\pi_s(1 - 1 + 2\\bar{\\pi}) > \\bar{\\pi}$, i.e., $2\\bar{\\pi}\\pi_s > \\bar{\\pi}$, i.e., $\\pi_s > 0.5$.\nThis is excluded by (A4), so global correction always reduces bias in high-error subgroups.\n\nFor low-error subgroups ($\\pi_s < \\bar{\\pi}$, so $\\delta_s < 0$): the condition becomes $(\\bar{\\pi} - \\pi_s) / ((1-2\\bar{\\pi})\\pi_s) > 1$, which gives $\\pi_s < \\bar{\\pi} / (1 - 2\\bar{\\pi} + 1) = \\bar{\\pi} / (2(1-\\bar{\\pi}))$.\nWhen $\\bar{\\pi} = 0.15$, any subgroup with $\\pi_s < 0.088$ experiences increased bias from global correction. \\qed\n\n\\paragraph{Extension to asymmetric misclassification.}\nProposition~\\ref{prop:debiasing_hurts} assumes symmetric error rates (A2).\nUnder asymmetric misclassification ($\\mathrm{FPR}_s \\neq \\mathrm{FNR}_s$), the naive bias becomes $\\mathrm{bias}_{\\mathrm{naive}}(0,s) = \\mathrm{FPR}_s \\cdot \\tau(1) + (1 - \\mathrm{FPR}_s - 1)\\tau(0)$ and the global correction bias depends on the full $2 \\times 2$ structure of $B_s = M_{\\mathrm{global}}^{-1} M_s - I$ (Remark~1 in Section~\\ref{sec:theory}).\nA sufficient condition for global correction to increase bias is\n\\begin{equation}\n\\|B_s\\|_\\infty > \\max(\\mathrm{FPR}_s, \\mathrm{FNR}_s),\n\\end{equation}\nwhich reduces to Equation~\\eqref{eq:hurts_condition} when $\\mathrm{FPR}_s = \\mathrm{FNR}_s = \\pi_s$.\nIn the asymmetric experiments (Appendix~\\ref{app:asymmetric}), the symmetric diagnostic still achieves AUC $= 0.82$ when applied with $\\pi_s = (\\mathrm{FPR}_s + \\mathrm{FNR}_s)/2$, suggesting practical robustness.\nA fully general asymmetric diagnostic that accounts for the separate roles of FPR and FNR in each entry of $B_s$ is left to future work.\n\n\\section{Semi-Synthetic Data Generating Process}\n\\label{app:dgp}\n\n\\paragraph{Synthetic DGP (Sections~\\ref{sec:bias_mechanism}--\\ref{sec:diagnostic} and Appendix~\\ref{sec:budget}).}\nWe generate $N = 5000$ observations.\nEach observation belongs to one of $K \\in \\{2, 4\\}$ subgroups $S \\in \\{1, \\ldots, K\\}$ with equal weights $w_s = 1/K$.\nThe binary effect modifier $Z \\in \\{0, 1\\}$ is drawn with $P(Z{=}1) = 0.5$.\nTreatment assignment is $T \\sim \\text{Bernoulli}(0.5)$, independent of $Z$ and $S$.\n\nThe outcome is generated as:\n\\begin{equation}\nY = \\tau(Z) \\cdot T + \\varepsilon, \\quad \\varepsilon \\sim \\mathcal{N}(0, 1),\n\\end{equation}\nwhere the CATE function is $\\tau(z) = \\bar{\\tau} + \\Delta\\tau \\cdot (z - 0.5)$ with $\\bar{\\tau} = 0.5$.\nThe CATE heterogeneity $\\Delta\\tau \\in \\{0, 0.2, 0.5, 1.0\\}$ controls the strength of treatment effect variation across levels of $Z$.\n\nMisclassification is symmetric: $\\hat{Z} \\neq Z$ with probability $\\pi_s$ depending on subgroup.\nFor $K{=}2$: $\\pi_1 = \\bar{\\pi} - \\Delta_c/2$, $\\pi_2 = \\bar{\\pi} + \\Delta_c/2$, with $\\bar{\\pi} \\in \\{0.1, 0.2\\}$ and $\\Delta_c \\in \\{0, 0.05, 0.1, 0.15\\}$.\nFor $K{=}4$, extreme regime: $\\pi \\in \\{0.05, 0.10, 0.15, 0.25\\}$; moderate regime: $\\pi \\in \\{0.08, 0.12, 0.16, 0.20\\}$.\n\nExpert labels are drawn as a simple random sample of size $n_{\\text{expert}} \\in \\{50, 100, 250, 500, 1000, 2000\\}$ from the full dataset, with true $Z$ observed for these observations.\n\n\\paragraph{Semi-synthetic DGP (Section~\\ref{sec:ec_hte_eval}).}\nWe sample $N = 5000$ tweets from the TweetEval sentiment corpus ($N_{\\text{pool}} = 57{,}899$).\nSubgroups are defined by crossing \\texttt{has\\_hashtag} $\\times$ \\texttt{text\\_length\\_bin} (short/medium/long), yielding $K = 4$ subgroups with empirical sizes: $S_0 \\approx 38\\%$, $S_1 \\approx 38\\%$, $S_2 \\approx 12\\%$, $S_3 \\approx 12\\%$.\nMisclassification rates in the extreme regime are $\\pi_{S_0} = 0.05$, $\\pi_{S_1} = 0.10$, $\\pi_{S_2} = 0.15$, $\\pi_{S_3} = 0.25$, reflecting empirical evidence that hashtag-heavy text degrades LLM classifier accuracy.\nThe outcome DGP follows the same structure as the synthetic case, with CATE injected onto the real text-derived subgroup structure.\n\n\\paragraph{PPCI DGPs (Appendix~\\ref{sec:ppci}).}\nFour DGPs isolate error types: (A) covariate error only ($\\sigma_{\\text{outcome}} = 0$), (B) outcome error only ($\\sigma_{\\text{outcome}} = 0.5$), (C) both errors ($\\sigma_{\\text{outcome}} = 0.5$), (D) no error ($\\sigma_{\\text{outcome}} = 0$).\nOutcome-side error is additive Gaussian noise on $Y$.\n\n\\paragraph{CausalForestDML hyperparameters.}\nAll CausalForest experiments use \\texttt{econml.dml.CausalForestDML} with honest splitting, $n_{\\text{estimators}} = 48$, $\\texttt{min\\_samples\\_leaf} = 20$, \\texttt{model\\_y} = \\texttt{LassoCV}(cv=3), and \\texttt{model\\_t} = \\texttt{LogisticRegressionCV}.\nThese defaults were held constant across all configurations; no hyperparameter tuning was performed.\n\n\\section{Extended Related Work}\n\\label{app:related}\n\n\\paragraph{Measurement error details.}\n\\citet{fuller1987measurement} establish the foundational theory showing that naive regression with mismeasured covariates yields attenuated coefficient estimates.\n\\citet{carroll2006measurement} extend this to nonlinear models.\n\\citet{gustafson2003measurement} develops Bayesian treatments modeling measurement jointly with outcomes.\n\\citet{hu2008nonparametric} provide nonparametric identification using repeated measurements or instruments.\n\n\\paragraph{Annotation model extensions.}\nBeyond the foundational \\citet{dawid1979maximum} model, \\citet{passonneau2014benefits} incorporate item difficulty, \\citet{hovy2013learning} learn annotator competence, and \\citet{paun2018comparing} introduce hierarchical priors sharing information across annotators with varying expertise.\n\n\\paragraph{PPI extensions and text-as-data methods.}\n\\citet{zrnic2024cross} extend PPI via cross-prediction; their active inference framework~\\citep{zrnic2024active} achieves $>$80\\% expert budget savings through adaptive allocation, complementary to our fixed-budget analysis.\n\\citet{grimmer2022text} provide methodological guidance for text-as-data pipelines.\n\\citet{audinet2025benchmarking} systematically benchmark DSL and PPI methods for LLM-based parameter estimation, finding that debiasing can increase MSE when prediction error is heterogeneous---a population-level analogue of the subgroup-conditional bias amplification we formalize in Theorem~\\ref{thm:bias_identity}.\n\n\\paragraph{Treatment vs.\\ effect-modifier misclassification.}\n\\citet{imai2010causal} study treatment misclassification where errors change which arm a unit is assigned to, requiring instrumental variables or partial identification because the fundamental treated-vs-control contrast is corrupted.\nOur problem preserves the treatment contrast ($T$ is observed correctly) but corrupts the heterogeneity structure ($\\hat{Z} \\neq Z$).\nThe ATE remains identified; only conditional effects are biased, which makes exact correction through confusion matrix inversion feasible.\n\n\\paragraph{Econometrics of binary misclassification.}\n\\citet{bound2001measurement} survey measurement error in survey data, establishing that binary misclassification attenuates regression coefficients.\n\\citet{frazis2003estimating} derive exact bias formulas for OLS with a misclassified binary regressor, showing attenuation proportional to the misclassification rate---analogous to our Theorem~\\ref{thm:bias_identity} but restricted to average effects without subgroup heterogeneity.\n\\citet{black2000racial} demonstrate that racial misclassification in administrative data can substantially bias estimates of racial disparities.\n\\citet{mahajan2006identification} and \\citet{lewbel2007estimation} develop instrumental variable approaches to identify models with misclassified binary regressors, requiring exclusion restrictions unavailable when the mismeasured variable is an LLM annotation.\nOur setting differs in three respects: (i) the mismeasured variable is an effect modifier indexing the CATE function, not a standard regressor; (ii) misclassification rates vary across subgroups, creating the $\\delta_s \\times \\Delta\\tau$ product amplification absent from homogeneous-error analyses; and (iii) expert labels provide a direct calibration sample, enabling confusion matrix estimation without instruments.\n\n\\section{MCMC Convergence Diagnostics}\n\\label{app:mcmc}\n\nTable~\\ref{tab:mcmc} reports convergence diagnostics for the hierarchical Bayesian confusion matrix estimator across all experimental configurations.\nAll runs use 4 chains with 4000 iterations (2000 warmup).\nMain experiments (Table~\\ref{tab:main_results}) use a Dirichlet prior centered on $\\hat{C}_{\\text{global}}$ with concentration $\\alpha_0$ estimated via empirical Bayes (marginal likelihood).\nAppendix robustness experiments use a fixed Dirichlet prior ($\\alpha{=}3$); since fixed-$\\alpha$ partial pooling is weakly dominated by the adaptive variant, these results are conservative.\nThis budget is sufficient for the $2{\\times}2$ Dirichlet-Multinomial posterior; all runs achieve $\\hat{R} < 1.0034$ and ESS $> 1618$, confirming convergence with substantial margin.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nDiagnostic & Threshold & Achieved \\\\\n\\midrule\n$\\hat{R}$ (max across all params) & $< 1.01$ & $< 1.0034$ \\\\\nESS (min across all params) & $> 845$ & $> 1618$ \\\\\nDivergent transitions & $= 0$ & $0$ \\\\\nSingularity guard triggers & --- & extreme/$n{=}50$ only \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{MCMC convergence diagnostics for the hierarchical Bayesian estimator. All configurations satisfy convergence criteria with substantial margin.}\n\\label{tab:mcmc}\n\\end{table}\n\n\\paragraph{Hyperprior sensitivity.}\nScaling the $\\text{Gamma}(3, 1)$ hyperprior by factors of $0.5\\times$ to $2\\times$ produces $<$1\\% RMSE variation for $K{=}2$ and $\\sim$4--5\\% for $K{=}4$.\nCoverage remains invariant across the sensitivity range.\nThese results confirm that the hierarchical estimator is robust to prior specification within a reasonable range.\n\n\\section{Diagnostic ROC Curves}\n\\label{app:roc}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_roc.png}\n\\caption{ROC curves for the $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}): $|\\delta_s|/((1{-}2\\bar\\pi)\\cdot\\pi_s)>1$. (A)~Setting-level ROC (AUC $= 0.89$), compared with the $|\\Delta\\pi \\times \\Delta\\tau|$ product (AUC $= 0.89$) and $\\mathrm{CV}(\\pi_s)$ (AUC $= 0.97$). (B)~Subgroup-level ROC: the $\\Delta\\pi$-only condition (AUC $= 0.86$) substantially outperforms the $|\\Delta\\pi \\times \\Delta\\tau|$ product (AUC $= 0.73$). The $\\Delta\\tau$-free diagnostic depends only on estimable misclassification rates, breaking the circular dependency that would arise if CATE heterogeneity were required.}\n\\label{fig:roc}\n\\end{figure}\n\n\\paragraph{Cost-asymmetric diagnostic thresholds.}\nIn practice, the cost of a false negative (failing to detect that global correction increases bias) exceeds the cost of a false positive (unnecessarily applying EC-HTE when global correction would suffice), because the former propagates systematic bias into CATE estimates while the latter only incurs additional estimation variance.\nPractitioners in high-stakes settings (e.g., policy evaluation where CATE estimates inform resource allocation) should lower the diagnostic threshold to favor recall over precision, accepting more false positives to minimize the risk of undetected bias amplification.\n\n\\section{Expert Budget Crossover Curves}\n\\label{app:budget}\n\\label{sec:budget}\n\nThe crossover point at which EC-HTE achieves lower RMSE than global correction is $n_{\\text{expert}} = 250$ for $K{=}2$/extreme and $n_{\\text{expert}} = 1000$ for $K{=}4$/extreme (Figure~\\ref{fig:budget}).\nUnder moderate heterogeneity ($K{=}2$), EC-HTE never achieves lower RMSE than global at any budget.\nHB partial pooling improves over stratified MLE in 21 of 24 configurations, with the two estimators converging by $n_{\\text{expert}} \\geq 1000$.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig3_budget.pdf}\n\\caption{RMSE vs.\\ expert budget ($n_{\\text{expert}}$) across four regime$\\times K$ combinations. Dashed vertical lines mark crossover points where EC-HTE achieves lower RMSE than global correction: $n{=}250$ ($K{=}2$, extreme), $n{=}1000$ ($K{=}4$, extreme). Under moderate heterogeneity ($K{=}2$), global correction dominates at all budgets. Shaded bands show $\\pm 1$ SD across subgroups within each configuration.}\n\\label{fig:budget}\n\\end{figure*}\n\n\\subsection{Budget Sensitivity: HB vs.\\ Stratified MLE}\n\\label{app:budget_sensitivity}\n\nHierarchical Bayes (HB) partial pooling borrows strength across subgroups, which should matter most when per-subgroup expert labels are scarce.\nWe sweep $n_{\\text{expert}} \\in \\{25, 50, 75, 100, 150, 250\\}$ under extreme heterogeneity ($\\Delta\\tau{=}0.3$, 100 MC runs, $N{=}5{,}000$).\nTable~\\ref{tab:budget_sensitivity} reports aggregate RMSE for global correction, stratified MLE, and HB EC-HTE.\n\n\\begin{table}[h]\n\\centering\n\\caption{RMSE across expert budgets under extreme heterogeneity.\nHB crossover (first budget where HB $<$ MLE) occurs at approximately 10 expert labels per subgroup-cell:\n$n_{\\text{expert}}{=}50$ for $K{=}2$ and $n_{\\text{expert}}{=}75$ for $K{=}4$.}\n\\label{tab:budget_sensitivity}\n\\small\n\\begin{tabular}{crrrrc}\n\\toprule\n$K$ & $n_{\\text{expert}}$ & Global & Strat.\\ MLE & HB EC-HTE & HB vs.\\ MLE \\\\\n\\midrule\n2 & 25 & \\textbf{0.101} & 0.256 & 0.269 & $+4.9\\%$ \\\\\n2 & 50 & \\textbf{0.088} & 0.275 & 0.231 & $\\mathbf{-16.1\\%}$ \\\\\n2 & 75 & 0.084 & 0.091 & \\textbf{0.089} & $-1.9\\%$ \\\\\n2 & 100 & 0.083 & 0.085 & \\textbf{0.084} & $-0.8\\%$ \\\\\n2 & 150 & 0.081 & 0.077 & \\textbf{0.077} & $-0.4\\%$ \\\\\n2 & 250 & 0.080 & 0.075 & \\textbf{0.074} & $-0.1\\%$ \\\\\n\\midrule\n4 & 25 & \\textbf{0.129} & 0.401 & 0.612 & $+52.5\\%$ \\\\\n4 & 50 & \\textbf{0.117} & 0.380 & 0.470 & $+23.8\\%$ \\\\\n4 & 75 & \\textbf{0.112} & 0.221 & 0.211 & $\\mathbf{-4.4\\%}$ \\\\\n4 & 100 & \\textbf{0.112} & 0.215 & 0.212 & $-1.3\\%$ \\\\\n4 & 150 & \\textbf{0.109} & 0.157 & 0.152 & $-3.6\\%$ \\\\\n4 & 250 & \\textbf{0.108} & 0.127 & 0.126 & $-1.0\\%$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree regimes emerge.\nAt very low budgets ($n_{\\text{expert}} < 50$ for $K{=}2$, $< 75$ for $K{=}4$), per-subgroup counts are insufficient for reliable confusion matrix estimation; global pooling dominates because the variance cost of stratification overwhelms any bias reduction.\nHB degrades substantially in this regime because the Gibbs posterior, while better regularized than MLE, still cannot overcome the fundamental sample-size constraint with $\\sim$6--12 labels per subgroup.\nAt moderate budgets ($n_{\\text{expert}} = 50$--$250$ for $K{=}2$, $75$--$250$ for $K{=}4$), HB partial pooling provides consistent RMSE improvement over stratified MLE ($-0.4\\%$ to $-16.1\\%$), with the largest gains near the crossover point.\nAt high budgets ($n_{\\text{expert}} \\geq 250$), both estimators converge as subgroup-level data becomes sufficient for reliable MLE; the HB advantage diminishes to $< 1\\%$.\nCoverage remains $\\geq 0.88$ for both methods across all budget levels.\n\n\\subsection{Scalability to $K{=}8$ Subgroups}\n\\label{app:k8_subgroups}\n\nWe test EC-HTE at $K{=}8$ to identify the scalability boundary of hierarchical Bayesian partial pooling under fixed expert budget.\n\n\\paragraph{Setup.}\n$N{=}5{,}000$, $K{=}8$ (equal-weight subgroups), $n_{\\text{expert}}{=}250$ (${\\approx}31$ labels per subgroup), 100 MC replications.\nMisclassification rates are uniformly spread: $\\pi_s \\in \\{0.05, 0.09, 0.13, 0.18, 0.22, 0.26, 0.30, 0.35\\}$.\nTreatment effects depend on $Z$ (not subgroup): $\\tau(Z{=}0){=}0$, $\\tau(Z{=}1){=}0.3$.\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE at $K{=}8$ ($n_{\\text{expert}}{=}250$, ${\\approx}31$ labels/subgroup, 100 MC).}\n\\label{tab:k8_subgroups}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Coverage & RMSE & $|\\text{Bias}|$ \\\\\n\\midrule\nOracle       & 0.944 & 0.113 & 0.090 \\\\\nGlobal       & 0.951 & 0.168 & 0.135 \\\\\nHB EC-HTE    & 0.956 & 0.340 & 0.183 \\\\\nStrat MLE    & 0.953 & 0.638 & 0.219 \\\\\nNaive        & 0.913 & 0.133 & 0.107 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll CM-aware methods achieve nominal coverage at $K{=}8$: HB EC-HTE 95.6\\%, Strat MLE 95.3\\%, Global 95.1\\%.\nHB partial pooling achieves a 47\\% RMSE reduction over stratified MLE (0.340 vs.\\ 0.638), confirming that hierarchical shrinkage provides substantial regularization.\nHowever, HB RMSE (0.340) exceeds global correction (0.168), indicating that ${\\approx}31$ expert labels per subgroup are insufficient for per-subgroup CM estimation to outweigh variance inflation.\n\n\\paragraph{Per-subgroup breakdown.}\nTable~\\ref{tab:k8_per_subgroup} decomposes RMSE by subgroup.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-subgroup RMSE at $K{=}8$. HB improvement over MLE is largest in high-$\\pi$ subgroups but does not close the gap with Global.}\n\\label{tab:k8_per_subgroup}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\nSubgroup & $\\pi_s$ & HB RMSE & MLE RMSE & Global RMSE & HB Cov \\\\\n\\midrule\n$s_0$ & 0.050 & 0.136 & 0.134 & \\textbf{0.181} & 0.950 \\\\\n$s_1$ & 0.093 & 0.133 & 0.132 & \\textbf{0.154} & 0.970 \\\\\n$s_2$ & 0.136 & 0.154 & 0.154 & 0.161 & 0.975 \\\\\n$s_3$ & 0.179 & 0.178 & 0.182 & \\textbf{0.159} & 0.945 \\\\\n$s_4$ & 0.221 & 0.263 & 0.343 & \\textbf{0.163} & 0.940 \\\\\n$s_5$ & 0.264 & 0.421 & 0.711 & \\textbf{0.164} & 0.965 \\\\\n$s_6$ & 0.307 & 0.634 & 1.375 & \\textbf{0.177} & 0.940 \\\\\n$s_7$ & 0.350 & 0.432 & 0.809 & \\textbf{0.183} & 0.960 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRMSE degradation is concentrated in high-$\\pi$ subgroups ($s_4$--$s_7$, $\\pi \\geq 0.22$), where confusion matrix inversion amplifies estimation noise ($r = 0.87$, $p = 0.005$ for correlation between $\\pi_s$ and HB RMSE).\nLow-error subgroups ($s_0$--$s_1$) benefit from stratification, with HB RMSE 14--25\\% below global correction.\nHB partial pooling reduces MLE RMSE by 24--54\\% in the high-$\\pi$ regime ($s_4$--$s_7$), confirming that hierarchical shrinkage provides meaningful regularization even when per-subgroup labels are scarce.\nCoverage remains $\\geq$0.94 across all subgroups for HB EC-HTE, indicating that variance inflation does not compromise inference validity.\nAdaptive shrinkage---increasing the prior strength for high-$\\pi$ subgroups where CM estimation is least reliable---is a natural extension that may close the RMSE gap with global correction at larger $K$.\n\nWe explored adaptive shrinkage ($\\alpha{=}10$ for high-$\\pi$ subgroups vs.\\ default $\\alpha{=}3$), which reduces aggregate RMSE from 0.340 to 0.216 (35\\% improvement) by attenuating estimation noise in high-$\\pi$ subgroups.\nHowever, RMSE remains 30\\% above global correction (0.166), confirming that the bottleneck is per-subgroup sample size (${\\sim}$31 expert labels) rather than the shrinkage method itself.\nThis establishes $K{=}8$ at $n_{\\text{expert}}{=}250$ as a boundary condition: all correction methods provide valid inference (coverage $\\geq$94\\%), but per-subgroup stratification requires proportionally larger expert budgets---approximately $n_{\\text{expert}} \\geq 500$ (${\\approx}60$ labels/subgroup)---to achieve RMSE parity with global correction.\n\n\\section{Asymmetric Misclassification Extension}\n\\label{app:asymmetric}\n\nAssumption~(A2) imposes symmetric misclassification ($\\text{FPR}_s = \\text{FNR}_s = \\pi_s$), which simplifies the bias decomposition but is not necessary for it.\nReal LLM annotators typically exhibit asymmetric confusion patterns; we show here that the product structure generalizes.\n\n\\paragraph{General bias formula.}\nFor asymmetric confusion matrices $C_s = \\bigl(\\begin{smallmatrix} 1{-}\\text{FPR}_s & \\text{FPR}_s \\\\ \\text{FNR}_s & 1{-}\\text{FNR}_s \\end{smallmatrix}\\bigr)$, define the mixing matrix $M_s$ via Bayesian inversion and the residual matrix $B_s = M_{\\text{global}}^{-1} M_s - I$.\nSince both $M_s$ and $M_{\\text{global}}$ are row-stochastic, $B_s \\mathbf{1} = \\mathbf{0}$.\nDecomposing $\\boldsymbol{\\tau} = \\tau(0)\\mathbf{1} + \\Delta\\tau \\, \\mathbf{e}_1$ gives:\n\\begin{equation}\n\\text{bias}(z, s) = \\Delta\\tau \\cdot [B_s]_{z,1},\n\\end{equation}\nwhere $[B_s]_{z,1}$ depends only on $\\{\\text{FPR}_k, \\text{FNR}_k, w_k\\}$, not on $\\Delta\\tau$.\nUnder~(A2), this reduces to $\\delta_s \\Delta\\tau / (1 - 2\\bar{\\pi})$ (Theorem~\\ref{thm:bias_identity}).\n\n\\paragraph{Empirical validation.}\nWe test three asymmetric configurations ($K{=}2$, $n_{\\text{expert}}{=}250$, 100 MC runs each): \\emph{Cross} (FPR/FNR = 0.10/0.20 vs.\\ 0.25/0.10), \\emph{Co-directional} (0.05/0.15 vs.\\ 0.20/0.30), and \\emph{Extreme} (0.03/0.25 vs.\\ 0.30/0.05).\nRegressing analytic predictions on MC bias yields $R^2 = 0.991$ across all configurations, confirming the product structure under asymmetry.\nTable~\\ref{tab:asymmetric} reports correction performance averaged over subgroups, $z$-levels, and $\\Delta\\tau \\in \\{0.1, \\ldots, 0.5\\}$.\nEC-HTE reduces $|\\text{bias}|$ from 0.025 (global) to 0.006, a $4\\times$ improvement, with lower RMSE (0.033 vs.\\ 0.040) and substantially better coverage (0.90 vs.\\ 0.78).\n\n\\begin{table}[t]\n\\centering\n\\caption{Asymmetric misclassification results ($K{=}2$, $n_{\\text{expert}}{=}250$, 100 MC runs). Values averaged over subgroups, $z$-levels, and $\\Delta\\tau$.}\n\\label{tab:asymmetric}\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\nMethod & $|\\text{Bias}| \\downarrow$ & RMSE $\\downarrow$ & Coverage $\\uparrow$ \\\\\n\\midrule\nNaive & 0.047 & 0.053 & 0.48 \\\\\nGlobal & 0.025 & 0.040 & 0.78 \\\\\nHB EC-HTE & \\textbf{0.006} & \\textbf{0.033} & \\textbf{0.90} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Supplementary Main Results}\n\\label{app:main_supp}\n\n\\begin{table}[t]\n\\centering\n\\caption{Additional configurations from the main experiment. $|\\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and 100 MC runs. $^\\dagger$RMSE exceeds Global.}\n\\label{tab:main_supp}\n\\small\n\\begin{tabular}{ll ccc}\n\\toprule\nConfiguration & Method & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Synthetic DIM\\\\$K{=}2$, moderate, $n{=}250$}}\n & Naive & 0.018 & 0.064 & 0.95 \\\\\n & Global & 0.009 & 0.074 & 0.96 \\\\\n & Strat.\\ MLE & \\textbf{0.005} & 0.075$^\\dagger$ & 0.97 \\\\\n & HB EC-HTE & \\textbf{0.005} & 0.075$^\\dagger$ & 0.97 \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Semi-synthetic\\\\TweetEval, extreme, $n{=}250$}}\n & Naive & 0.027 & 0.103 & 0.93 \\\\\n & Global & \\textbf{0.023} & 0.124 & 0.92 \\\\\n & Strat.\\ MLE & 0.032 & 0.248$^\\dagger$ & 0.91 \\\\\n & HB EC-HTE & 0.027 & 0.225$^\\dagger$ & 0.91 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{PPCI Complementarity Results}\n\\label{app:ppci}\n\\label{sec:ppci}\n\nEC-HTE composes with PPCI~\\cite{sui2026ppci} for settings where both covariate misclassification and outcome model error are present: EC-HTE+PPCI reduces $|\\text{bias}|$ from 0.179 to 0.007 ($z{=}0$, DGP~C), and the corrected pseudo-outcomes are compatible with other CATE estimators (R-learner bias reduction: 89\\%; Appendix~\\ref{app:rlearner}).\n\n\\begin{table*}[t]\n\\centering\n\\caption{PPCI complementarity experiment ($K{=}2$, extreme, $n_{\\text{expert}}{=}250$). DGP~A: covariate error only; B: outcome error only ($\\sigma{=}0.5$); C: both errors; D: no error. Values are $|\\text{bias}|$ and RMSE averaged over two subgroups. $^\\star$EC-HTE+PPCI achieves near-zero bias when both error types are present.}\n\\label{tab:ppci}\n\\small\n\\begin{tabular}{ll cccc}\n\\toprule\nDGP & Method & $|\\text{Bias}|_{z=0}$ & $|\\text{Bias}|_{z=1}$ & RMSE$_{z=0}$ & RMSE$_{z=1}$ \\\\\n\\midrule\n\\multirow{5}{*}{A: Covariate}\n & Naive & 0.053 & 0.063 & 0.087 & 0.093 \\\\\n & Global & 0.063 & 0.055 & 0.101 & 0.102 \\\\\n & EC-HTE & 0.017 & \\textbf{0.013} & 0.097 & 0.108 \\\\\n & PPCI & \\textbf{0.015} & 0.020 & 0.162 & 0.168 \\\\\n & EC-HTE+PPCI & 0.017 & \\textbf{0.013} & 0.097 & 0.108 \\\\\n\\midrule\n\\multirow{5}{*}{B: Outcome}\n & Naive & 0.189 & 0.197 & 0.206 & 0.212 \\\\\n & Global & 0.185 & 0.208 & 0.204 & 0.228 \\\\\n & EC-HTE & 0.181 & 0.215 & 0.202 & 0.237 \\\\\n & PPCI & 0.015 & \\textbf{0.020} & 0.171 & 0.176 \\\\\n & EC-HTE+PPCI & \\textbf{0.012} & 0.023 & 0.171 & 0.186 \\\\\n\\midrule\n\\multirow{5}{*}{C: Both}\n & Naive & 0.251 & 0.135 & 0.267 & 0.155 \\\\\n & Global & 0.182 & 0.209 & 0.233 & 0.235 \\\\\n & EC-HTE & 0.179 & 0.216 & 0.224 & 0.262 \\\\\n & PPCI & 0.017 & 0.007 & 0.241 & 0.232 \\\\\n & EC-HTE+PPCI$^\\star$ & \\textbf{0.007} & \\textbf{0.008} & 0.209 & 0.223 \\\\\n\\midrule\n\\multirow{5}{*}{D: None}\n & Naive & \\textbf{0.007} & 0.003 & 0.060 & 0.065 \\\\\n & Global & 0.010 & \\textbf{0.002} & 0.061 & 0.071 \\\\\n & EC-HTE & 0.013 & 0.007 & 0.062 & 0.079 \\\\\n & PPCI & \\textbf{0.007} & \\textbf{0.003} & 0.060 & 0.065 \\\\\n & EC-HTE+PPCI & 0.013 & 0.007 & 0.062 & 0.079 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe complementarity of EC-HTE and PPCI follows from the distinct error sources they correct: EC-HTE addresses misclassification in the effect modifier $Z$ (covariate space), while PPCI corrects specification error in the outcome model $f(X)$ (prediction space).\nSince covariate misclassification and outcome model error are algebraically independent in the potential outcomes framework, their corrections compose without interference---confirmed by the 4-DGP orthogonal design (Table~\\ref{tab:ppci}), where DGP~C (both errors present) yields the largest bias reduction from the combined approach.\nUnder covariate error only, PPCI adds nothing; under no error, all methods perform equivalently.\n\n\\section{Real-Data Case Study: Hate Speech Detection}\n\\label{app:hatespeech}\n\nWe apply EC-HTE to the UC Berkeley Measuring Hate Speech corpus~\\cite{kennedy2020constructing}, annotating 2{,}496 comments for dehumanization using GPT-4.1.\nFour text-feature subgroups are defined by crossing platform (Reddit/Gab vs.\\ Twitter/YouTube) and text length (above/below median), yielding balanced groups ($n \\approx 624$ each).\n\n\\paragraph{Positive finding: real-world heterogeneity.}\nPer-subgroup misclassification rates range from 0.266 to 0.383, confirming heterogeneity ($\\Delta\\pi = 0.117$) in a real annotation setting.\nAt the error-type level, FPR ranges from 8.5\\% to 21.3\\% across text-feature subgroups, demonstrating that subgroup-varying misclassification is not an artifact of synthetic design but arises naturally in real NLP annotation tasks.\n\n\\paragraph{Boundary condition: statistical power at extreme FNR.}\nCorrection results are inconclusive: all corrected confidence intervals contain zero, and point estimate differences between methods are not statistically significant.\nThe high baseline FNR (53.3\\%) amplifies variance through matrix inversion (variance amplification factor up to 15.7$\\times$), rendering the comparison underpowered.\nWhen $P(\\hat{Z}{=}1 \\mid Z{=}1) \\approx 0.5$, the confusion matrix approaches singularity, and inversion amplifies estimation noise regardless of stratification strategy.\nThis complements the expert budget threshold identified in Appendix~\\ref{sec:budget}: EC-HTE requires \\emph{both} sufficient expert labels \\emph{and} sufficient baseline classifier quality.\n\n\\paragraph{Diagnostic connection.}\nThe diagnostic criterion ($\\Delta\\pi \\times \\Delta\\tau$, Section~\\ref{sec:diagnostic}) identifies when correction is worthwhile under moderate baseline accuracy.\nThis case study illustrates that even when $\\Delta\\pi$ is large, extreme baseline error renders correction underpowered rather than beneficial.\nA practical prerequisite is that the per-subgroup confusion matrix condition number $\\kappa(\\hat{C}_s)$ remain moderate; when $\\kappa > 50$, as observed here, practitioners should prioritize improving annotation quality before applying any matrix-inversion-based correction.\n\n\\section{Cross-Model Consistency}\n\\label{app:multilm}\n\nWe evaluate whether misclassification heterogeneity is model-specific by annotating 500 TweetEval sentiment tweets with six OpenAI models spanning three generations.\nSix text-feature subgroups are defined by crossing hashtag presence and text length.\nSpearman rank correlations of per-subgroup error rates across all six subgroups range from $\\rho = 0.82$ to $1.00$, indicating that the subgroup error structure is consistent across architectures.\nTwo subgroups with $n \\leq 6$ exhibit zero misclassification across all models; excluding these yields four-point correlations that are directionally consistent but underpowered.%\n\\footnote{The filtered $\\Delta\\pi$ values in Table~\\ref{tab:multilm} serve as a robustness check independent of rank-order testing: all six models exceed $\\Delta\\pi > 0.05$ on the four retained subgroups.}\n\n\\begin{table}[t]\n\\centering\n\\caption{Effective misclassification heterogeneity ($\\Delta\\pi$) across six OpenAI models on TweetEval sentiment (500 tweets, filtered to 4 subgroups with $n \\geq 10$).}\n\\label{tab:multilm}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nModel & Effective $\\Delta\\pi$ & $> 0.05$? \\\\\n\\midrule\nGPT-3.5-Turbo & 0.198 & \\checkmark \\\\\nGPT-4-Turbo & 0.149 & \\checkmark \\\\\nGPT-4o-mini & 0.136 & \\checkmark \\\\\nGPT-5.4 & 0.114 & \\checkmark \\\\\nGPT-4.1 & 0.098 & \\checkmark \\\\\nGPT-4o & 0.080 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll six models exhibit effective $\\Delta\\pi > 0.05$ on the four retained subgroups (Table~\\ref{tab:multilm}), and 5 of 6 share the same worst subgroup (\\texttt{True\\_medium}: tweets with hashtags and medium text length).\nNewer models reduce absolute error rates but do not eliminate subgroup heterogeneity: GPT-5.4 achieves $\\Delta\\pi = 0.114$ compared to GPT-3.5-Turbo's $0.198$.\nThese results were obtained with a single API provider; open-source model validation appears in Appendix~\\ref{app:multilm_opensource}.\n\n\\section{Open-Source Multi-LLM Validation}\n\\label{app:multilm_opensource}\n\nWe evaluate four open-source LLMs (7B--9B parameter range) on 490 TweetEval sentiment tweets with $K{=}4$ subgroups defined by crossing hashtag presence and text length.\nTable~\\ref{tab:multilm_cm} reports the confusion matrix heterogeneity profile.\nAll four models exhibit $\\Delta\\pi > 0.05$, confirming that subgroup-heterogeneous misclassification is not specific to proprietary APIs.\nSubgroup error rankings are consistent across architectures: \\texttt{True\\_short} (short tweets with hashtags) has the lowest $\\pi_s$ in 3 of 4 models, while \\texttt{False\\_medium} (medium tweets without hashtags) has the highest.\n\n\\begin{table}[t]\n\\centering\n\\caption{Confusion matrix heterogeneity across four open-source LLMs ($K{=}4$, $N{=}490$ TweetEval tweets). $\\Delta\\pi$: max--min per-subgroup misclassification rate. Prop2: number of subgroups where the $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}) triggers.}\n\\label{tab:multilm_cm}\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\nModel & Acc.\\ & $\\Delta\\pi$ & Prop2 & Strongest \\\\\n\\midrule\nLlama-3.1-8B & 0.755 & 0.141 & 1/4 & True\\_short \\\\\nQwen-2.5-7B & 0.798 & 0.165 & 1/4 & True\\_short \\\\\nGemma-2-9B & 0.763 & 0.125 & 4/4 & True\\_medium \\\\\nMistral-7B & 0.802 & 0.134 & 0/4 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Semi-synthetic budget sweep.}\nWe run the full EC-HTE pipeline with $K{=}2$ subgroups and $\\Delta\\tau{=}0.3$, using each model's empirical confusion matrices.\nTable~\\ref{tab:multilm_budget} reports coverage and RMSE crossover points.\nEC-HTE restores near-nominal coverage from 0.714 (naive average) to 0.939 ($+$22.5 percentage points) at $n_{\\text{expert}}{=}1{,}000$, consistent across all four models.\nGlobal correction achieves comparable or lower RMSE than HB at all budgets under these moderate $\\Delta\\pi$ values, and the $K{=}4$ RMSE crossover never occurs---confirming the budget guidelines in Appendix~\\ref{sec:budget}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Semi-synthetic budget sweep ($K{=}2$, $\\Delta\\tau{=}0.3$, 50 MC runs\\protect\\footnote{Appendix experiments use 50 MC replications unless otherwise noted; all main-text results use 100.}). Coverage at selected expert budgets; RMSE crossover denotes the minimum expert budget at which HB EC-HTE achieves lower RMSE than the naive (uncorrected) estimator.}\n\\label{tab:multilm_budget}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nModel & $\\Delta\\pi_{K{=}2}$ & Naive Cov.\\ & HB Cov.\\ ($n{=}1000$) & Crossover \\\\\n\\midrule\nLlama-3.1-8B & 0.051 & 0.675 & 0.940 & $n{=}1000$ \\\\\nQwen-2.5-7B & 0.080 & 0.715 & 0.925 & $n{=}1000$ \\\\\nGemma-2-9B & 0.100 & 0.705 & 0.945 & $n{=}1000$ \\\\\nMistral-7B & 0.070 & 0.760 & 0.945 & $n{=}1000$ \\\\\n\\midrule\n\\textit{Average} & --- & \\textit{0.714} & \\textit{0.939} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Gemma boundary case.}\nGemma-2-9B triggers the Proposition~\\ref{prop:debiasing_hurts} diagnostic in all four $K{=}4$ subgroups due to extreme FPR--FNR asymmetry (\\texttt{False\\_medium} FNR $= 0.437$).\nAt small budgets ($K{=}4$, $n{=}100$), EC-HTE RMSE reaches 1.229 ($3.1\\times$ naive), illustrating the budget guideline from Appendix~\\ref{sec:budget}: when per-subgroup cell counts fall below 25, the variance cost of stratified correction dominates.\nAt $n \\geq 500$, EC-HTE coverage recovers to $>$0.90, consistent with the synthetic experiments.\n\n\\paragraph{Heterogeneous-$\\tau$ DGP.}\nTo assess whether the constant-$\\tau$ DGP understates EC-HTE's advantage, we run a supplementary experiment using Llama's empirical confusion matrices with heterogeneous treatment effects across subgroups ($\\Delta\\tau \\in [0.1, 0.6]$, $K{=}2$, 50 MC runs).\nEC-HTE achieves lower $|\\text{bias}|$ than global correction at all budgets ($n{=}500$: 0.010 vs.\\ 0.031, a 68\\% reduction).\nIn the high-$\\Delta\\tau$ subgroup (\\texttt{True\\_short}, $\\Delta\\tau{=}0.6$), EC-HTE also achieves lower RMSE ($n{=}1{,}000$: 0.212 vs.\\ 0.258, 18\\% improvement), confirming that the RMSE advantage concentrates in subgroups where correction is most needed.\nAggregate RMSE remains comparable to global correction because low-$\\Delta\\tau$ subgroups incur stratification variance without commensurate bias reduction, consistent with the budget guidelines in Appendix~\\ref{sec:budget}.\n\n\\section{Robustness to Subgroup Misspecification}\n\\label{app:robustness}\n\nEC-HTE requires pre-defined subgroup labels, which may be noisy in practice.\nWe test robustness by randomly flipping each observation's subgroup assignment with probability $p_{\\text{flip}} \\in \\{0, 0.10, 0.25, 0.50\\}$, across $K \\in \\{2, 4\\}$ (extreme regime, $n_{\\text{expert}} = 500$, $\\Delta\\tau = 0.3$, 100 MC runs).\n\n\\begin{table}[t]\n\\centering\n\\caption{95\\% CI coverage under subgroup misspecification noise. EC-HTE maintains near-nominal coverage across all noise levels.}\n\\label{tab:robustness}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{4}{c}{$p_{\\text{flip}}$} \\\\\n\\cmidrule(lr){2-5}\nMethod & 0.00 & 0.10 & 0.25 & 0.50 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{$K{=}2$, extreme}} \\\\\n\\quad Naive & 0.875 & 0.877 & 0.890 & 0.897 \\\\\n\\quad Global & 0.925 & 0.935 & 0.932 & 0.945 \\\\\n\\quad HB EC-HTE & 0.958 & 0.948 & 0.950 & 0.945 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{$K{=}4$, extreme}} \\\\\n\\quad Naive & 0.904 & 0.916 & 0.909 & 0.919 \\\\\n\\quad Global & 0.930 & 0.953 & 0.948 & 0.944 \\\\\n\\quad HB EC-HTE & 0.956 & 0.958 & 0.960 & 0.946 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE maintains coverage $\\geq 0.945$ across all configurations (Table~\\ref{tab:robustness}), while the naive estimator is systematically below nominal (0.875--0.919).\nAt $p_{\\text{flip}} = 0.50$, subgroup structure is effectively destroyed; EC-HTE converges to global correction (coverage and RMSE within 0.1\\%), confirming that hierarchical Bayesian shrinkage provides a built-in safety mechanism.\nFor $K{=}4$ at $p_{\\text{flip}} = 0.50$, a small residual RMSE gap persists ($p < 0.01$), reflecting the variance cost of estimating four confusion matrices even when they carry no signal.\n\n\\section{Monte Carlo Standard Errors}\n\\label{app:mcse}\n\nAll experiments use 100 independent Monte Carlo replications per configuration.\nAll simulation results were verified with 100 MC seeds; the median RMSE variation between 50-seed and 100-seed estimates is below 3.2\\%, confirming the stability of reported figures.\nWe report Monte Carlo standard errors to assess whether observed differences between methods are statistically reliable.\nFor exp-001 (synthetic DGP, no per-seed pairing across methods), we use conservative two-sample $z$-tests on the 100-run means.\nFor exp-003 (semi-synthetic TweetEval, shared seeds across methods), we use paired $t$-tests, which are more powerful because they control for seed-level variation.\n\nTable~\\ref{tab:mcse} reports paired comparisons for representative configurations.\nOf 1{,}020 total pairwise comparisons across all configurations, 742 (72.7\\%) are statistically significant at $\\alpha = 0.05$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Paired comparisons for representative configurations. $\\Delta$ = method A $-$ method B (negative favors A for $|\\text{bias}|$). Two-sample $z$-tests for synthetic (exp-001); paired $t$-tests for semi-synthetic (exp-003). Bold $p$-values indicate significance at $\\alpha = 0.05$.}\n\\label{tab:mcse}\n\\small\n\\begin{tabular}{llrr}\n\\toprule\nConfiguration & Comparison & $\\Delta$ & $p$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{HB EC-HTE vs.\\ Global ($|\\text{bias}|$)}} \\\\\n\\quad $K{=}2$/ext/$n{=}500$ & & $-0.046$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/ext/$n{=}500$ & & $-0.078$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/mod/$n{=}250$ & & $-0.017$ & $0.288$ \\\\\n\\quad TweetEval/ext/$n{=}250$ & & $+0.001$ & $0.395$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{HB EC-HTE vs.\\ Global (RMSE)}} \\\\\n\\quad $K{=}2$/ext/$n{=}500$ & & $+0.015$ & $0.179$ \\\\\n\\quad $K{=}4$/ext/$n{=}500$ & & $+0.048$ & $\\mathbf{0.011}$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{HB EC-HTE vs.\\ Naive ($|\\text{bias}|$)}} \\\\\n\\quad $K{=}2$/ext/$n{=}500$ & & $-0.089$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/ext/$n{=}500$ & & $-0.113$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/mod/$n{=}250$ & & $-0.031$ & $\\mathbf{0.038}$ \\\\\n\\quad TweetEval/ext/$n{=}250$ & & $+0.005$ & $\\mathbf{0.030}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder extreme heterogeneity, HB EC-HTE's bias advantage over global correction is highly significant ($p < 0.001$ for both $K{=}2$ and $K{=}4$).\nThe RMSE penalty of stratification is not significant at $K{=}2$ ($p = 0.179$) but reaches significance at $K{=}4$ ($p = 0.011$), consistent with the higher variance cost of estimating four confusion matrices.\nUnder moderate heterogeneity ($K{=}4$, $n{=}250$), the bias difference between HB and global is not significant ($p = 0.288$), confirming that EC-HTE's advantage requires sufficient error heterogeneity.\nIn the semi-synthetic TweetEval experiment, HB EC-HTE does not significantly improve over global ($p = 0.395$), consistent with moderate $\\Delta\\pi$ and unbalanced subgroup sizes.\nThe HB vs.\\ naive comparison in TweetEval is significant ($p = 0.030$) but favors naive, reflecting the variance cost of stratification when bias reduction is marginal.\n\n\\section{Semi-Real Confusion Matrix Validation}\n\\label{app:semireal}\n\nWe test EC-HTE with empirical asymmetric confusion matrices from the GPT-4.1 TweetEval pilot.\nFour text-feature subgroups ($K{=}4$) retain the real per-subgroup FPR and FNR from pilot annotations (Table~\\ref{tab:semireal_cm}); CATE heterogeneity is injected synthetically ($\\tau(z{=}0,s) = 0.3 + 0.1s$, $\\tau(z{=}1,s) = 0.8 - 0.15s$).\n$N{=}5{,}000$, $P(Z{=}1){=}0.18$, 100 MC seeds per $n_{\\text{expert}}$ level.\n\n\\begin{table}[t]\n\\centering\n\\caption{Empirical confusion matrices from GPT-4.1 TweetEval pilot.\nS0 exhibits FNR $= 0.526$, approaching chance-level classification.}\n\\label{tab:semireal_cm}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSubgroup & Weight & FPR & FNR & $\\kappa(\\hat{C}_s)$ \\\\\n\\midrule\nS0 & 0.38 & 0.054 & 0.526 & high \\\\\nS1 & 0.22 & 0.101 & 0.300 & moderate \\\\\nS2 & 0.14 & 0.143 & 0.308 & moderate \\\\\nS3 & 0.25 & 0.194 & 0.222 & low \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Semi-real confusion matrix results. RMSE and coverage averaged over subgroups and $z$-levels (100 MC runs). HB EC-HTE underperforms global at all budgets; S0's near-chance FNR drives the failure.}\n\\label{tab:semireal}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n$n_{\\text{expert}}$ & Method & RMSE $\\downarrow$ & Coverage $\\uparrow$ \\\\\n\\midrule\n\\multirow{4}{*}{100}\n & Oracle & 0.101 & 0.957 \\\\\n & Naive & 0.123 & 0.879 \\\\\n & Global & 0.263 & 0.885 \\\\\n & HB EC-HTE & 0.784 & 0.744 \\\\\n\\midrule\n\\multirow{4}{*}{250}\n & Oracle & 0.101 & 0.957 \\\\\n & Naive & 0.123 & 0.879 \\\\\n & Global & 0.232 & 0.909 \\\\\n & HB EC-HTE & 0.411 & 0.834 \\\\\n\\midrule\n\\multirow{4}{*}{500}\n & Oracle & 0.101 & 0.957 \\\\\n & Naive & 0.123 & 0.879 \\\\\n & Global & 0.196 & 0.922 \\\\\n & HB EC-HTE & 0.260 & 0.890 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHB EC-HTE produces higher RMSE and lower coverage than global correction at all expert budgets (Table~\\ref{tab:semireal}).\nThe root cause is S0's FNR $= 0.526$: when a confusion matrix row approaches a uniform distribution ($P(\\hat{Z}{=}1 \\mid Z{=}1) \\approx 0.5$), inversion amplifies estimation noise regardless of the expert budget.\nThis converges with the hate speech case study (Appendix~\\ref{app:hatespeech}, FNR $= 53.3$\\%) and confirms that EC-HTE requires \\emph{both} sufficient expert labels \\emph{and} sufficient baseline classifier quality per subgroup.\nThe singularity guard ($\\kappa > 100$, Section~\\ref{sec:method}) mitigates catastrophic failure by falling back to global correction for near-degenerate subgroups, but does not recover the bias reduction that motivates stratification.\nFor a $2 \\times 2$ symmetric confusion matrix, $\\kappa = 1/|1-2\\pi|$; $\\kappa > 100$ corresponds to $\\pi \\in (0.495, 0.505)$, so the guard triggers only when the classifier performs within $0.5\\%$ of random guessing.\nAt $n_{\\text{expert}} = 500$, HB EC-HTE narrows the gap (RMSE 0.260 vs.\\ 0.196) as confusion matrix estimates stabilize for the three well-classified subgroups, but the S0 bottleneck persists.\n\nA second semi-real experiment using GPT-3.5-Turbo confusion matrices (worst-subgroup FPR $= 0.39$, FNR $= 0.21$) yields similar results: HB RMSE exceeds global by 1.3--3.5$\\times$ at all budgets.\nHere the failure stems from high false-positive rates compounded by class imbalance ($P(Z{=}1) = 0.18$), which leaves insufficient expert observations in the positive class for reliable per-subgroup confusion matrix estimation.\nTogether, these experiments identify three applicability conditions for EC-HTE: (1)~sufficient effective expert budget ($n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$), (2)~no near-chance subgroup error rate ($\\max(\\text{FPR}_s, \\text{FNR}_s) < 0.5$), and (3)~adequate class balance in the effect modifier.\n\n\\paragraph{Diagnostic rule.}\nA logistic regression over all 368 semi-real experiment--budget cells (dependent variable: HB EC-HTE $<$ Global RMSE) identifies two sufficient statistics: the worst-subgroup confusion matrix condition number $\\kappa(\\hat{M}_s) \\leq 1.25$ and the effective minority-class expert count $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$.\nWhen both conditions hold, HB outperforms global in 93.3\\% of cells; when either is violated, global is preferred in 94.7\\% of cells.\nBoth exp-015 ($\\kappa = 2.38$, effective $n = 2.5$) and exp-016 ($\\kappa = 1.55$, effective $n = 2.5$) violate both conditions, and the diagnostic correctly predicts 100\\% of their failure cells.\nSubgroup-average metrics can mask cell-level heterogeneity: in exp-015, HB EC-HTE substantially reduces bias for the three well-classified subgroups (S1--S3) but amplifies variance in the near-degenerate subgroup (S0, FNR $= 0.526$), and the S0 penalty dominates the aggregate RMSE.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/applicability_frontier.pdf}\n\\caption{Applicability frontier of EC-HTE. Green region: EC-HTE reduces bias vs.\\ global correction. Yellow: comparable performance. Red: EC-HTE underperforms. Dashed lines mark the expert budget threshold ($n_{\\text{expert}}/K = 25$) and classifier quality threshold (worst-subgroup error rate $= 0.5$). Red diamonds show semi-real experiments with actual GPT-4.1 and GPT-3.5-Turbo confusion matrices.}\n\\label{fig:applicability}\n\\end{figure}\n\n\\section{Robustness: Estimator Choice and Treatment Effect Specification}\n\\label{app:rlearner}\n\nWe verify that EC-HTE's corrected pseudo-outcomes are compatible with downstream estimators beyond CausalForest by replacing it with the R-learner~\\citep{nie2021quasi}.\nThe experiment uses $K{=}2$, extreme heterogeneity, $n_{\\text{expert}} = 500$, and 50 MC seeds; the R-learner uses 5-fold cross-fitting with gradient-boosted trees as the base learner.\n\n\\begin{table}[t]\n\\centering\n\\caption{R-learner vs.\\ CausalForest with EC-HTE correction ($K{=}2$, extreme, $n{=}500$). $|\\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and seeds.}\n\\label{tab:rlearner}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nEstimator & Correction & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\n\\multirow{4}{*}{R-learner}\n & Oracle & 0.006 & 0.056 & 0.94 \\\\\n & Naive & 0.121 & 0.139 & 0.47 \\\\\n & Global & 0.098 & 0.123 & 0.72 \\\\\n & EC-HTE & \\textbf{0.013} & 0.080 & 0.92 \\\\\n\\midrule\n\\multirow{2}{*}{CausalForest}\n & Naive & 0.058 & 0.090 & 0.82 \\\\\n & EC-HTE & \\textbf{0.010} & 0.093 & 0.95 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE reduces R-learner $|\\text{bias}|$ by 89\\% (0.121 $\\to$ 0.013) and restores coverage from 0.47 to 0.92 (Table~\\ref{tab:rlearner}).\nThe bias reduction and coverage gains are comparable to those achieved with CausalForest, confirming that EC-HTE is compatible with a range of HTE estimators.\n\n\\paragraph{Multiplicative treatment effects.}\nWe further test robustness to the functional form of treatment effects by replacing the additive DGP with a multiplicative specification: $Y(1) = Y(0) \\times \\exp(\\tau(Z))$, using $K{=}2$, extreme heterogeneity, $n_{\\text{expert}} = 500$, and 50 MC seeds.\n\n\\begin{table}[t]\n\\centering\n\\caption{Multiplicative DGP results ($K{=}2$, extreme, $n{=}500$, 50 seeds). EC-HTE achieves comparable bias reduction and nominal coverage under non-additive treatment effects.}\n\\label{tab:multiplicative}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\nOracle & 0.003 & 0.038 & 0.96 \\\\\nNaive & 0.135 & 0.142 & 0.44 \\\\\nGlobal & 0.110 & 0.124 & 0.54 \\\\\nEC-HTE & \\textbf{0.054} & 0.068 & 0.955 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE reduces RMSE by 52\\% relative to naive (0.068 vs.\\ 0.142) and restores coverage to the nominal level (0.955; Table~\\ref{tab:multiplicative}).\nEC-HTE's bias correction operates at the confusion matrix level, independent of the downstream CATE estimator and functional form of treatment effects.\n\n\\section{Robustness to Class Imbalance}\n\\label{app:classimbalance}\n\nAssumption (A3) requires $P(Z{=}1) = 0.5$, but real-world effect modifiers are often imbalanced.\nWe sweep $P(Z{=}1) \\in \\{0.1, 0.2, 0.3, 0.4, 0.5\\}$ with $K \\in \\{2,4\\}$, extreme misclassification heterogeneity, $n_{\\text{expert}}{=}250$, and 100 MC seeds (Table~\\ref{tab:pz1_sweep}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Robustness to class imbalance ($n_{\\text{expert}}{=}250$, extreme heterogeneity). R$^2$: Theorem~\\ref{thm:bias_identity} fit. Ratio: HB/Global RMSE ($<1$ = HB wins). Cov.: HB EC-HTE 95\\% CI coverage.}\n\\label{tab:pz1_sweep}\n\\small\n\\begin{tabular}{cc ccc}\n\\toprule\n$P(Z{=}1)$ & $K$ & R$^2$ & Ratio & Cov. \\\\\n\\midrule\n0.1 & 2 & 0.998 & 0.92 & 0.94 \\\\\n0.2 & 2 & 0.989 & 0.76 & 0.94 \\\\\n0.3 & 2 & 0.994 & 0.78 & 0.94 \\\\\n0.4 & 2 & 0.995 & 0.87 & 0.94 \\\\\n0.5 & 2 & 0.995 & 0.86 & 0.93 \\\\\n\\midrule\n0.1 & 4 & 0.984 & 1.54 & 0.92 \\\\\n0.2 & 4 & 0.976 & 1.68 & 0.93 \\\\\n0.3 & 4 & 0.985 & 1.12 & 0.92 \\\\\n0.4 & 4 & 0.984 & 1.08 & 0.93 \\\\\n0.5 & 4 & 0.992 & 1.06 & 0.92 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTheorem~\\ref{thm:bias_identity}'s product form remains accurate across all imbalance levels: $R^2 \\geq 0.976$ even at $P(Z{=}1) = 0.1$, confirming that the bias identity derives from confusion matrix structure rather than class balance.\nFor $K{=}2$, EC-HTE outperforms global correction at all $P(Z{=}1)$ levels (RMSE ratio 0.76--0.92), degrading gracefully under severe imbalance.\nFor $K{=}4$, EC-HTE underperforms global at $n_{\\text{expert}}{=}250$ (ratio 1.06--1.68), consistent with the budget threshold $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$: at $P(Z{=}1){=}0.1$, $K{=}4$, each subgroup receives only ${\\sim}6$ minority-class labels.\nThe gap narrows as $P(Z{=}1)$ increases (1.54 $\\to$ 1.06), and coverage remains stable at 0.92--0.94 across all configurations.\n\n\\section{Comparison with PPI Correction}\n\\label{app:ppi_comparison}\n\nPPI~\\cite{angelopoulos2023ppi} constructs confidence intervals by combining a large set of ML predictions with a smaller set of gold-standard labels, using the gold labels to debias the ML-based estimator.\nApplied to our setting, PPI treats the LLM-annotated effect modifier as the ML prediction and the expert labels as the gold standard.\nTwo variants arise naturally: \\emph{PPI-global} pools all expert labels to estimate a single rectifier (analogous to our Global baseline), and \\emph{PPI-subgroup} estimates per-subgroup rectifiers (analogous to Stratified MLE).\n\nUnder the confusion-matrix parameterization we adopt, DSL's measurement error correction reduces to confusion matrix inversion.\nPooled DSL applies a single estimated confusion matrix to all subgroups, producing the same corrected label distribution as our Global baseline; per-subgroup DSL estimates a separate confusion matrix for each subgroup and inverts it independently, equivalent to our Stratified MLE.\nEC-HTE's contribution over both PPI-subgroup and per-subgroup DSL is hierarchical partial pooling: rather than estimating each subgroup's confusion matrix in isolation, EC-HTE places a shared prior across subgroups, borrowing strength to reduce variance while preserving subgroup-specific bias correction.\nThis mechanism is outside both the PPI and DSL frameworks.\n\nThe key difference between PPI and confusion-matrix inversion is that PPI does not invert the confusion matrix; instead, it uses the gold labels to directly debias the estimand.\nThis avoids the matrix inversion step that can amplify noise at small $n_{\\text{expert}}$, but it also means PPI cannot exploit the structure of the misclassification process to reduce bias.\nPPI-global inherits the same $\\Delta\\pi \\times \\Delta\\tau$ bias amplification as Global correction (Theorem~\\ref{thm:bias_identity}), confirming that the ``debiasing hurts'' mechanism operates regardless of the inference framework.\n\n\\section{Civil Comments Validation}\n\\label{app:civilcomments}\n\nTo verify that subgroup-heterogeneous misclassification generalizes beyond TweetEval, we annotate $N{=}3{,}000$ stratified samples (30\\% toxic) from Civil Comments~\\cite{borkan2019nuanced}, a toxicity detection dataset.\nSubgroups are defined by \\texttt{text\\_length\\_bin} $\\times$ \\texttt{has\\_question} ($K{=}4$): S0 (long, no question, 38.8\\%), S1 (long, question, 11.4\\%), S2 (short, no question, 33.7\\%), S3 (short, question, 16.1\\%).\nSubgroup features were chosen a priori based on observable text properties; no feature search was performed.\nThree proprietary LLMs annotate each sample via an OpenAI-compatible API, yielding 800--900 valid annotations per model.\n\nTable~\\ref{tab:civil_cm} reports per-subgroup FPR and FNR.\nWe define $\\Delta\\pi = \\max_s \\pi_s - \\min_s \\pi_s$, where $\\pi_s$ is the overall misclassification rate for subgroup $s$.\nAll three models exhibit $\\Delta\\pi > 0.05$, with overall heterogeneity $\\Delta\\pi \\in [0.113, 0.160]$---comparable to the $\\Delta\\pi \\in [0.125, 0.165]$ observed across four open-source LLMs on TweetEval (Appendix~\\ref{app:multilm_opensource}).\nGPT-4o-mini and GPT-3.5-turbo show pronounced FPR/FNR asymmetry (e.g., GPT-4o-mini FPR $\\in [0.42, 0.61]$ vs.\\ FNR $\\in [0.05, 0.16]$), indicating systematic over-prediction of toxicity; their FPR approaches 0.5, placing them in the ill-conditioned regime where confusion matrix inversion amplifies noise (consistent with the classifier quality threshold discussed in the Limitations section).\nThe consistent presence of $\\Delta\\pi$ heterogeneity across two NLP tasks, seven LLMs spanning open-source (7B--9B) and proprietary families, and two distinct subgroup definitions confirms that this phenomenon is a structural property of LLM annotation rather than an artifact of a specific dataset or model.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-subgroup misclassification rates on Civil Comments ($K{=}4$). $\\Delta$ denotes max $-$ min across subgroups.}\n\\label{tab:civil_cm}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Metric & S0 & S1 & S2 & S3 & $\\Delta$ \\\\\n\\midrule\nGPT-4o & FPR & 0.249 & 0.157 & 0.213 & 0.341 & 0.184 \\\\\n       & FNR & 0.160 & 0.263 & 0.308 & 0.328 & 0.168 \\\\\n\\midrule\nGPT-4o-mini & FPR & 0.517 & 0.541 & 0.419 & 0.610 & 0.191 \\\\\n            & FNR & 0.052 & 0.105 & 0.074 & 0.160 & 0.108 \\\\\n\\midrule\nGPT-3.5-turbo & FPR & 0.400 & 0.473 & 0.374 & 0.468 & 0.099 \\\\\n              & FNR & 0.139 & 0.211 & 0.173 & 0.240 & 0.101 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Bias Identity Validation with Real Confusion Matrices}\n\\label{app:realcm_bias}\n\nTheorem~\\ref{thm:bias_identity} is derived under symmetric misclassification (A2); real LLM confusion matrices are asymmetric (FPR $\\neq$ FNR).\nWe verify that the generalized identity $\\mathrm{bias}(z,s) = \\Delta\\tau \\cdot [B_s]_{z,1}$ (Remark~\\ref{thm:bias_identity}) holds under real annotation error structures by running semi-synthetic simulations ($N{=}5{,}000$, $K{=}4$, $\\Delta\\tau{=}0.30$, 100 MC runs) with confusion matrices drawn from 11 LLM--dataset combinations: eight models on TweetEval (GPT-4-turbo, GPT-4o, GPT-4.1, GPT-4o-mini, GPT-3.5-turbo, Qwen2.5-7B, Mistral-7B, Gemma-2-9B) and three on Civil Comments (GPT-4o, GPT-4o-mini, GPT-3.5-turbo).\n\nTable~\\ref{tab:realcm_r2} reports per-model $R^2$ from regressing observed subgroup bias on the predicted value $\\Delta\\tau \\cdot [B_s]_{z,1}$.\nThe aggregate $R^2 = 0.975$; 10 of 11 combinations achieve $R^2 \\geq 0.93$.\nThe single outlier (GPT-4o-mini on Civil Comments, $R^2{=}0.76$) has near-homogeneous subgroup error rates ($\\max|[B_s]_{z,1}| = 0.089$), so predicted biases are small and Monte Carlo noise dominates the regression.\n$R^2$ correlates strongly with $\\max|[B_s]_{z,1}|$: models with more heterogeneous per-subgroup error rates produce larger bias signals that are easier to verify empirically.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bias identity $R^2$ with real LLM confusion matrices ($K{=}4$, 100 MC runs).}\n\\label{tab:realcm_r2}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nModel & Dataset & $R^2$ & $\\max|[B_s]_{z,1}|$ \\\\\n\\midrule\nGPT-4-turbo  & TweetEval & 0.993 & 0.328 \\\\\nQwen2.5-7B   & TweetEval & 0.990 & 0.272 \\\\\nMistral-7B   & TweetEval & 0.990 & 0.242 \\\\\nGemma-2-9B   & TweetEval & 0.982 & 0.185 \\\\\nGPT-4o       & Civil Comments & 0.979 & 0.198 \\\\\nGPT-4o       & TweetEval & 0.975 & 0.240 \\\\\nGPT-4.1      & TweetEval & 0.969 & 0.139 \\\\\nGPT-3.5-turbo & TweetEval & 0.948 & 0.087 \\\\\nGPT-3.5-turbo & Civil Comments & 0.935 & 0.170 \\\\\nGPT-4o-mini  & TweetEval & 0.929 & 0.170 \\\\\nGPT-4o-mini  & Civil Comments & 0.756 & 0.089 \\\\\n\\midrule\n\\multicolumn{2}{l}{All (pooled)} & 0.975 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Applicability Screening with Real LLM Confusion Matrices}\n\\label{app:screening}\n\nWe apply the diagnostic conditions from Proposition~\\ref{prop:debiasing_hurts} and Section~\\ref{sec:method} to 16 LLM--dataset--$K$ combinations spanning seven LLMs (four open-source, three proprietary) across TweetEval and Civil Comments.\nTable~\\ref{tab:screening} summarizes which conditions each combination satisfies.\n\n\\begin{table}[h]\n\\centering\n\\caption{Diagnostic screening of 16 LLM--dataset--$K$ combinations. Columns report whether all subgroups satisfy each condition. Budget assumes $n_{\\text{expert}}{=}500$.}\n\\label{tab:screening}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Dataset & $K$ & $\\kappa{\\leq}1.25$ & $\\max{\\leq}0.5$ & Budget & Pass all \\\\\n\\midrule\nGemma-2-9B   & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nLlama-3.1-8B & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nMistral-7B   & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nQwen2.5-7B   & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGemma-2-9B   & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nLlama-3.1-8B & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nMistral-7B   & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nQwen2.5-7B   & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-3.5-turbo & CivilComm. & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-3.5-turbo & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4-turbo  & TweetEval & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4.1      & TweetEval & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o       & CivilComm. & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o       & TweetEval & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o-mini  & CivilComm. & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o-mini  & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nNo combination passes all three conditions; the bottleneck is $\\kappa(C_s) \\leq 1.25$, which requires $\\mathrm{FPR}_s + \\mathrm{FNR}_s \\lesssim 0.20$ for all subgroups---a threshold no current LLM achieves uniformly.\nThe closest are Qwen2.5-7B True\\_short ($\\kappa{=}1.23$) and Mistral-7B True\\_short ($\\kappa{=}1.27$).\n\nUnder a relaxed ``oracle screening'' that excludes near-degenerate subgroups ($\\max(\\mathrm{FPR}_s, \\mathrm{FNR}_s) \\geq 0.4$), we run semi-synthetic CATE estimation ($N{=}5{,}000$, $\\Delta\\tau{=}0.3$, 100 MC runs, $n_{\\text{expert}} \\in \\{250, 500\\}$) with each LLM's real per-subgroup confusion matrix.\nEC-HTE (HB) achieves lower RMSE than global correction in 41 of 52 comparisons (79\\%) and lower RMSE than stratified MLE in 52 of 52 comparisons (100\\%).\nThe four open-source LLMs on TweetEval show the strongest EC-HTE advantage (32/32 comparisons, RMSE reduction 0.001--0.008), while GPT-3.5-turbo/TweetEval (high FPR asymmetry, $\\mathrm{FPR}_{\\max}{=}0.39$) and GPT-4o/Civil Comments (low minority prevalence $P(Z{=}1){=}0.3$) show degradation.\nThe diagnostic correctly identifies the strict applicability regime; under relaxed conditions excluding near-degenerate subgroups, EC-HTE improves RMSE in 79\\% of comparisons.\n\n\\paragraph{Diagnostic Applicability Analysis.}\nThe diagnostic (Proposition~\\ref{prop:debiasing_hurts}) degrades on real LLM confusion matrices (pooled AUC $= 0.63$) because the failure mode is systematic: subgroups where the true CATE heterogeneity $\\tau_s \\approx 0$ are hurt by global correction (since $\\delta_s \\neq 0$ still introduces bias), yet these subgroups produce low diagnostic scores---the diagnostic ranks them as safe precisely when they are most vulnerable to overcorrection.\n\nA simple meta-criterion recovers reliability: compute $\\max_s |\\delta_s| / ((1 - 2\\bar{\\pi}) \\cdot \\pi_s)$ across subgroups.\nWhen $\\max_s \\mathrm{score}(s) > 1$, at least one subgroup is definitively harmed by global correction, and the diagnostic achieves AUC $\\geq 0.75$ across all 5 model--dataset combinations satisfying this condition (AUC range: 0.75--1.0).\nWhen $\\max_s \\mathrm{score}(s) \\leq 1$, global correction may or may not hurt depending on unobservable $\\Delta\\tau$; the diagnostic achieves AUC only 0.0--0.67 across the remaining 7 combinations (4 of 7 have AUC $< 0.5$, indicating anti-prediction).\nThis threshold perfectly separates reliable from unreliable diagnostic regimes across all 16 real LLM--dataset combinations evaluated.\n\nWe recommend the following practical protocol: (i) estimate per-subgroup confusion matrices from expert labels; (ii) compute $\\max_s \\mathrm{score}(s)$; (iii) if $> 1$, the diagnostic reliably identifies which subgroups are harmed by global correction---apply EC-HTE; (iv) if $\\leq 1$, the diagnostic is unreliable and practitioners should either default to EC-HTE as a conservative choice or evaluate correction strategies using held-out expert labels.\n\n\\section{Plug-in Standard Error Validation}\n\\label{app:bootstrap_se}\n\nA natural concern is whether the plug-in standard error adequately captures estimation uncertainty, particularly the additional variance introduced by confusion matrix estimation.\nWe verify this for the difference-in-means (DIM) estimator via Monte Carlo simulation ($K{=}2$, $n_{\\text{expert}} \\in \\{50, 100, 250, 500\\}$, 50 replications per budget level).\nAt each budget, we compute the plug-in 95\\% confidence interval and record empirical coverage.\nAcross all expert budgets, the plug-in SE yields coverage $\\geq 0.96$ (0.970, 0.960, 0.970, 0.970 for $n_{\\text{expert}} = 50, 100, 250, 500$), confirming that the analytic variance estimate is well-calibrated for the DIM estimator.\nThis self-calibration arises because the same noise in $\\hat{M}^{-1}$ that inflates point-estimate variance also inflates the plug-in SE, producing conservative intervals that maintain nominal coverage.\n\n\\paragraph{CausalForestDML.}\nUnder $K{=}2$ extreme heterogeneity ($\\pi{=}[0.05, 0.25]$, $n_{\\text{expert}}{=}250$, $n_{\\text{estimators}}{=}200$, 20 MC runs), EC-HTE plug-in SE achieves 93.8\\% aggregate coverage---close to the 94--96\\% oracle coverage (Table~\\ref{tab:cf_oracle}).\nThe high-error subgroup ($s_1$, $\\pi{=}0.25$) shows slightly lower plug-in coverage (92.5\\%) than the low-error subgroup ($s_0$: 95.0\\%), reflecting the larger $M^{-1}$ amplification of estimation uncertainty in subgroups with higher misclassification rates.\nBy contrast, the DIM plug-in SE achieves $\\geq$95\\% coverage in the same DGP, confirming that the analytic confusion matrix propagation formula is adequate for simpler estimators.\n\n\\paragraph{Full bootstrap SE.}\nA \\emph{full} bootstrap---resampling all $N$ observations and re-estimating both the confusion matrix and CausalForest per bootstrap replicate ($B{=}100$, $n_{\\text{estimators}}{=}200$, 20 MC runs)---confirms that plug-in SE is already near-nominal under standard hyperparameters.\nUnder $K{=}2$ extreme heterogeneity ($\\pi{=}[0.05, 0.25]$, $n_{\\text{expert}}{=}250$), plug-in SE achieves 93.8\\% aggregate coverage; the full bootstrap improves this to exactly 95.0\\% ($+$1.2pp).\nTable~\\ref{tab:bootstrap_se} reports per-subgroup results.\n\n\\begin{table}[h]\n\\centering\n\\caption{CausalForest coverage: plug-in SE vs.\\ full bootstrap SE ($B{=}100$, $n_{\\text{estimators}}{=}200$, 20 MC runs). Bootstrap SE is ${\\sim}1.15\\times$ plug-in.}\n\\label{tab:bootstrap_se}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nSubgroup & Plugin Cov. & Boot.\\ Cov. & Oracle Cov. & Plugin SE & Boot.\\ SE \\\\\n\\midrule\n$s_0$ ($\\pi{=}0.05$) & 0.950 & 0.925 & 0.925 & 0.059 & 0.063 \\\\\n$s_1$ ($\\pi{=}0.25$) & 0.925 & \\textbf{0.975} & 0.875 & 0.087 & 0.103 \\\\\n\\midrule\nAggregate & 0.938 & \\textbf{0.950} & 0.900 & 0.073 & 0.083 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe high-error subgroup ($s_1$) benefits most: coverage rises from 92.5\\% to 97.5\\% ($+$5.0pp), because the bootstrap captures the additional variance from $M^{-1}$ amplification.\nOracle coverage (90.0\\%) is consistent with the 94\\% reported in the oracle decomposition (Table~\\ref{tab:cf_oracle}), with the difference attributable to MC sampling noise at 20 runs.\nThe computational cost is substantial ($B \\times$ CF fits per MC run), but the approach is straightforward when exact nominal coverage is required.\n\n\\paragraph{Finite-sample remainder.}\nBy first-order matrix perturbation, $\\hat{C}_s^{-1} = C_s^{-1} - C_s^{-1} E_s C_s^{-1} + O(\\|E_s\\|^2)$, where $E_s = \\hat{C}_s - C_s$ satisfies $\\|E_s\\| = O_p(n_{\\text{expert}}^{-1/2})$.\nThe remainder in the corrected CATE is therefore $R_n = O_p(n_{\\text{expert}}^{-1/2} \\cdot \\|C_s^{-1}\\|^2) = O_p(n_{\\text{expert}}^{-1/2} \\cdot \\kappa(C_s))$, since $\\|C_s^{-1}\\| = O(\\kappa(C_s))$ for stochastic matrices.\nThis motivates the $\\kappa > 100$ singularity guard (Section~\\ref{sec:method}).\n\n\\subsection{CausalForest Oracle Coverage Decomposition}\n\\label{app:cf_oracle}\n\nTo isolate the source of CausalForest under-coverage, we compare six estimation strategies that progressively remove sources of uncertainty: (1)~Oracle (true $Z$, no correction), (2)~EC-HTE with true $C_s$, (3)~EC-HTE with estimated $\\hat{C}_s$ (HB), (4)~Global with true $\\bar{C}$, (5)~Global with estimated $\\hat{\\bar{C}}$, and (6)~Naive.\nTable~\\ref{tab:cf_oracle} reports coverage, $|\\text{bias}|$, and RMSE across three DGP configurations (100 MC runs each).\n\n\\begin{table}[h]\n\\centering\n\\caption{CausalForest oracle coverage decomposition. Coverage averaged over subgroups and $z$-levels.}\n\\label{tab:cf_oracle}\n\\small\n\\begin{tabular}{ll ccc}\n\\toprule\nDGP & Method & Cov.\\ (\\%) & $|\\text{Bias}|$ & RMSE \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{$K{=}4$, extreme\\\\$n{=}500$}}\n & Oracle (true $Z$)       & 94.5 & 0.006 & 0.078 \\\\\n & EC-HTE true $C_s$       & 92.5 & 0.008 & 0.114 \\\\\n & EC-HTE est.\\ $\\hat{C}_s$ & 93.1 & 0.015 & 0.121 \\\\\n & Global true $\\bar{C}$   & 91.3 & 0.037 & 0.110 \\\\\n & Global est.\\ $\\hat{\\bar{C}}$ & 91.1 & 0.038 & 0.111 \\\\\n & Naive                    & 88.3 & 0.045 & 0.095 \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{$K{=}2$, extreme\\\\$n{=}250$}}\n & Oracle (true $Z$)       & 94.0 & 0.002 & 0.056 \\\\\n & EC-HTE true $C_s$       & 94.0 & 0.003 & 0.073 \\\\\n & EC-HTE est.\\ $\\hat{C}_s$ & 92.5 & 0.004 & 0.079 \\\\\n & Global true $\\bar{C}$   & 88.5 & 0.045 & 0.083 \\\\\n & Global est.\\ $\\hat{\\bar{C}}$ & 88.3 & 0.045 & 0.085 \\\\\n & Naive                    & 82.8 & 0.046 & 0.077 \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{$K{=}2$, MF2 DGP\\\\$\\tau{=}(0.10,0.40)$}}\n & Oracle (true $Z$)       & 96.0 & 0.077 & 0.091 \\\\\n & EC-HTE true $C_s$       & 91.3 & 0.103 & 0.112 \\\\\n & EC-HTE est.\\ $\\hat{C}_s$ & 92.3 & 0.100 & 0.111 \\\\\n & Global true $\\bar{C}$   & 95.0 & 0.107 & 0.114 \\\\\n & Global est.\\ $\\hat{\\bar{C}}$ & 94.3 & 0.105 & 0.114 \\\\\n & Naive                    & 77.3 & 0.120 & 0.125 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree findings emerge.\nFirst, oracle coverage is 94--96\\% across all DGPs, confirming that CausalForest plug-in SE is well-calibrated when labels are correct.\nSecond, EC-HTE with true $C_s$ achieves 91--94\\% coverage---a 0--5pp gap from oracle (configuration-dependent), reflecting $M^{-1}$ SE propagation asymmetry across DGPs rather than confusion matrix estimation error.\nThird, the gap between true and estimated $C_s$ is ${\\leq}$1.5pp ($K{=}2$) and $<$1pp ($K{=}4$), confirming that CM estimation uncertainty contributes negligibly at $n_{\\text{expert}} \\geq 250$.\n\n\\section{Robustness to Assumption Violations}\n\\label{app:a5_violation}\n\n\\subsection{Assumption (A5): Subgroup-Specific Treatment Effects}\n\n\\begin{corollary}[Subgroup-Specific Treatment Effect Heterogeneity]\n\\label{cor:a5_relaxation}\nWhen $\\Delta\\tau$ varies across subgroups ($\\Delta\\tau_s = \\tau_s(1) - \\tau_s(0)$), the bias of global correction in subgroup $s$ at level $z{=}0$ is $+\\delta_s \\cdot \\Delta\\tau_s / (1 - 2\\bar{\\pi})$, and at level $z{=}1$ is $-\\delta_s \\cdot \\Delta\\tau_s / (1 - 2\\bar{\\pi})$.\n\\end{corollary}\nThe proof follows directly from Theorem~\\ref{thm:bias_identity} with $\\tau_s$ replacing $\\tau$.\n\nOur main analysis assumes that subgroup misclassification rates $\\delta_s$ and subgroup CATE magnitudes $\\Delta\\tau_s$ are independent (Assumption A5).\nIn practice, both may depend on text features that define subgroups, introducing correlation.\nWe test robustness under two configurations with the DIM estimator ($K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 50 MC replications, $\\pi = [0.05, 0.25]$):\n\\emph{aligned} (positive $\\delta_s$--$\\Delta\\tau_s$ correlation: high-error S1 has the larger treatment effect, $\\Delta\\tau = [0.30, 0.70]$) and\n\\emph{adversarial} (negative correlation: high-error S1 has the smaller effect, $\\Delta\\tau = [0.70, 0.30]$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Coverage and $|\\text{bias}|$ under A5 violation ($K{=}2$, $n_{\\text{expert}}{=}250$, 50 MC). Target coverage: 0.95.}\n\\label{tab:a5_violation}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nConfig & Method & S0 cov & S1 cov & S0 $|\\text{bias}|$ & S1 $|\\text{bias}|$ \\\\\n\\midrule\n\\multirow{4}{*}{Aligned}\n & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\\\\n & Naive         & 0.93 & 0.25 & 0.022 & 0.174 \\\\\n & Global        & 0.93 & 0.82 & 0.036 & 0.094 \\\\\n & EC-HTE (EB)   & 0.95 & 0.95 & 0.005 & 0.017 \\\\\n\\midrule\n\\multirow{4}{*}{Adversarial}\n & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\\\\n & Naive         & 0.90 & 0.78 & 0.042 & 0.074 \\\\\n & Global        & 0.74 & 0.93 & 0.098 & 0.040 \\\\\n & EC-HTE (EB)   & 0.94 & 0.96 & 0.002 & 0.007 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn the aligned configuration, the $\\delta_s \\times \\Delta\\tau_s$ product is maximized in the high-error subgroup, causing naive S1 coverage to collapse to 0.25.\nGlobal correction improves S1 but cannot fully correct without subgroup-specific error rates.\nIn the adversarial configuration, global correction overcorrects the low-error subgroup (S0 coverage 0.74).\nEC-HTE (EB) maintains $\\geq 0.94$ coverage across both subgroups in both configurations, with bias comparable to the oracle.\nResults at $n_{\\text{expert}}{=}500$ are consistent (all EC-HTE coverages $\\in [0.93, 0.99]$).\n\n\\subsection{Assumption (A1): Sensitivity to Outcome-Dependent Misclassification}\n\\label{app:a1_sensitivity}\n\nWe assess EC-HTE's robustness when misclassification depends on potential outcomes, violating~(A1).\nWe modify the synthetic DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$) so that misclassification probability becomes outcome-dependent: $P(\\hat{Z}{\\neq}Z \\mid Z, S, Y) = \\mathrm{clamp}(\\pi_s + \\gamma \\cdot (Y - \\mu_Y)/\\sigma_Y,\\, 0,\\, 1)$, where $\\gamma \\in \\{0, 0.05, 0.10, 0.15, 0.20\\}$ controls the strength of violation.\nTable~\\ref{tab:a1_sensitivity} reports results averaged over 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{Sensitivity to Assumption~(A1) violation. Coverage and $|\\text{bias}|$ under outcome-dependent misclassification ($\\gamma > 0$).}\n\\label{tab:a1_sensitivity}\n\\small\n\\begin{tabular}{lccc ccc}\n\\toprule\n& \\multicolumn{3}{c}{Coverage (\\%)} & \\multicolumn{3}{c}{$|\\text{Bias}|$} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n$\\gamma$ & EC-HTE & Global & Naive & EC-HTE & Global & Naive \\\\\n\\midrule\n0.00 & 95.5 & 92.7 & 87.7 & 0.060 & 0.065 & 0.061 \\\\\n0.05 & 95.5 & 93.5 & 83.8 & 0.059 & 0.064 & 0.064 \\\\\n0.10 & 95.3 & 93.8 & 83.5 & 0.063 & 0.064 & 0.067 \\\\\n0.15 & 94.8 & 94.3 & 79.2 & 0.065 & 0.064 & 0.070 \\\\\n0.20 & 93.5 & 94.0 & 79.5 & 0.068 & 0.063 & 0.073 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE maintains near-nominal coverage ($\\geq$93.5\\%) across the full $\\gamma$ range, with $|\\text{bias}|$ increasing only 13.7\\% from $\\gamma{=}0$ to $\\gamma{=}0.2$.\nAll correction methods (Global, Stratified MLE, HB) maintain $\\geq$90\\% coverage, indicating that moderate (A1) violations do not catastrophically degrade confusion-matrix-based correction.\nThe naive estimator degrades most rapidly (coverage $-$8.2pp), consistent with outcome-dependent misclassification compounding the uncorrected label noise.\n\n\\subsection{Extension to Confounded Treatment Assignment}\n\\label{app:confounded_dgp}\n\nEC-HTE's confusion matrix correction operates on estimated CATEs regardless of how those estimates are produced.\nTo verify compatibility with observational (non-RCT) designs, we pair EC-HTE with an inverse probability weighted difference-in-means (IPW-DIM) estimator under confounded treatment assignment.\n\n\\paragraph{DGP.}\n$N{=}5{,}000$, $K{=}2$, $\\pi = [0.05, 0.25]$, $n_{\\text{expert}}{=}250$, 100 MC replications.\nA covariate $X \\sim \\mathcal{N}(0,1)$ confounds both treatment and outcome:\n$T \\sim \\text{Bernoulli}(\\sigma(\\beta X))$ with $\\beta{=}0.5$ (moderate confounding; propensity range $[0.38, 0.62]$),\n$Y = 1 + 0.5 Z + 0.3 X + \\tau(Z) \\cdot T + \\varepsilon$, $\\varepsilon \\sim \\mathcal{N}(0,1)$.\nTreatment effects are $\\tau(Z{=}0){=}0$, $\\tau(Z{=}1){=}0.3$.\nThe IPW-DIM estimator uses \\emph{oracle propensity} $e(X) = \\sigma(\\beta X)$, with propensity scores clipped to $[0.05, 0.95]$.\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE under confounded treatment assignment (IPW-DIM with oracle propensity, $\\beta{=}0.5$, 100 MC).}\n\\label{tab:confounded_dgp}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Coverage & RMSE & $|\\text{Bias}|$ \\\\\n\\midrule\nOracle (true $Z$ + IPW) & 0.943 & 0.061 & 0.048 \\\\\nHB EC-HTE              & 0.950 & 0.086 & 0.068 \\\\\nGlobal                  & 0.930 & 0.087 & 0.071 \\\\\nStrat MLE               & 0.950 & 0.087 & 0.069 \\\\\nNaive                   & 0.863 & 0.083 & 0.066 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE achieves 95.0\\% coverage, within 0.7pp of the oracle (94.3\\%), confirming that confusion matrix correction and propensity weighting compose without interference.\nThe improvement is most pronounced in the high-error subgroup ($\\pi{=}0.25$): EC-HTE coverage is 96.0\\% vs.\\ naive 78.5\\% ($+$17.5pp).\nGlobal coverage (93.0\\%) falls below the correction methods (95.0\\%), consistent with the cost of ignoring subgroup-level error heterogeneity even in the confounded setting.\n\n\\paragraph{Sensitivity to confounding strength and propensity estimation.}\nWe sweep $\\beta \\in \\{0.25, 0.5, 1.0, 2.0\\}$ and compare oracle propensity ($e(X) = \\sigma(\\beta X)$) with estimated propensity (logistic regression fit on $(X, T)$), yielding 8 configurations (100 MC each).\nTable~\\ref{tab:confounded_sweep} reports HB EC-HTE and naive coverage.\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE coverage across confounding strengths and propensity sources. The logistic regression propensity model is correctly specified; propensity misspecification is a complementary concern addressed by the IPW literature.}\n\\label{tab:confounded_sweep}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n$\\beta$ & Propensity & HB Coverage & Naive Coverage \\\\\n\\midrule\n0.25 & Oracle    & 0.963 & 0.848 \\\\\n0.25 & Estimated & 0.973 & 0.845 \\\\\n0.50 & Oracle    & 0.950 & 0.863 \\\\\n0.50 & Estimated & 0.958 & 0.858 \\\\\n1.00 & Oracle    & 0.958 & 0.898 \\\\\n1.00 & Estimated & 0.960 & 0.883 \\\\\n2.00 & Oracle    & 0.945 & 0.858 \\\\\n2.00 & Estimated & 0.948 & 0.858 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE maintains coverage $\\geq$94.5\\% across all 8 configurations, including strong confounding ($\\beta{=}2.0$, propensity range $[0.12, 0.88]$).\nThe oracle--estimated gap is $\\leq$1pp, confirming that propensity estimation error does not meaningfully degrade EC-HTE when the propensity model is correctly specified.\nThis validates that EC-HTE is robust to confounded treatment assignment when the propensity model is correctly specified.\n\n\\subsection{Empirical Comparison with Frazis--Loewenstein Correction}\n\\label{app:fl_comparison}\n\nWe empirically compare EC-HTE's confusion matrix inversion against the scalar attenuation correction of \\citet{frazis2003estimating} (F-L).\nThe F-L correction rescales the observed estimate as $\\hat{\\tau}_{\\text{FL}} = \\hat{\\tau}_{\\text{obs}} / (1 - 2\\bar{\\pi})$, where $\\bar{\\pi}$ is the (global or per-subgroup) misclassification rate.\nWe test two variants: F-L \\emph{scalar} (single global $\\bar{\\pi}$) and F-L \\emph{per-subgroup} ($\\pi_s$-specific rescaling).\nSetup: $K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, $\\pi{=}[0.05, 0.25]$ (extreme heterogeneity), $\\tau(z{=}0){=}0$, $\\tau(z{=}1){=}0.3$, 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{F-L correction vs.\\ EC-HTE under heterogeneous misclassification ($\\Delta\\pi{=}0.20$). Both F-L variants produce \\emph{higher} aggregate bias than the uncorrected estimator.}\n\\label{tab:fl_comparison}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Coverage \\\\\n\\midrule\nOracle         & 0.045 & 0.056 & 0.943 \\\\\nNaive          & 0.062 & 0.077 & 0.858 \\\\\nGlobal (CM inv)& 0.064 & 0.081 & 0.938 \\\\\nHB EC-HTE      & 0.064 & 0.086 & \\textbf{0.953} \\\\\nF-L Scalar     & 0.091 & 0.116 & 0.850 \\\\\nF-L Per-Subgroup & 0.112 & 0.158 & 0.838 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth F-L variants produce \\emph{higher} bias and RMSE than the naive estimator (F-L per-subgroup $|\\text{bias}|{=}0.112$ vs.\\ naive $0.062$), demonstrating that scalar attenuation cannot substitute for confusion matrix inversion under subgroup-heterogeneous misclassification.\nThe per-subgroup bias direction reveals the mechanism: F-L scalar over-corrects the low-error subgroup ($s_0$: mean bias ${=}+0.073$ vs.\\ naive $+0.005$, a $14.6\\times$ amplification), while F-L per-subgroup dramatically over-corrects the high-error subgroup ($s_1$: mean bias ${=}+0.160$).\nEC-HTE achieves near-zero per-subgroup bias ($s_0{:}\\,{+}0.006$, $s_1{:}\\,{+}0.001$) with nominal coverage (95.3\\%).\nThe root cause is structural: F-L's $1/(1{-}2\\pi)$ scaling amplifies each $z$-level estimate independently, whereas CM inversion simultaneously redistributes the cross-contamination between misclassified and correctly classified observations.\n\n\\subsection{End-to-End Validation with Asymmetric Confusion Matrices}\n\\label{app:asymmetric_endtoend}\n\nWe validate EC-HTE under strongly asymmetric confusion matrices ($\\text{FPR}/\\text{FNR}$ ratio up to $7{:}1$), simulating the error profile of GPT-4.1 on Civil Comments.\nSetup: $K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$; $s_0$: $\\text{FPR}{=}0.05$, $\\text{FNR}{=}0.02$ (low error); $s_1$: $\\text{FPR}{=}0.38$, $\\text{FNR}{=}0.054$ ($7{:}1$ ratio); 100 MC runs.\nWe compare EC-HTE using the full $2{\\times}2$ asymmetric CM (Remark~2) against the symmetric assumption ($\\text{FPR}{=}\\text{FNR}{=}\\pi_s$).\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE under asymmetric misclassification ($\\text{FPR}/\\text{FNR}$ up to $7{:}1$). The asymmetric formula improves coverage by $+1.5$pp and RMSE by $11.5\\%$.}\n\\label{tab:asymmetric_endtoend}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Coverage \\\\\n\\midrule\nOracle              & 0.045 & 0.056 & 0.943 \\\\\nEC-HTE (asymmetric) & 0.057 & 0.074 & \\textbf{0.945} \\\\\nNaive               & 0.059 & 0.073 & 0.870 \\\\\nGlobal (asymmetric) & 0.061 & 0.076 & 0.915 \\\\\nEC-HTE (symmetric)  & 0.062 & 0.083 & 0.930 \\\\\nGlobal (symmetric)  & 0.063 & 0.078 & 0.915 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE with the asymmetric formula achieves 94.5\\% coverage versus 93.0\\% under the symmetric assumption ($+1.5$pp), with RMSE improved from 0.083 to 0.074 ($-11.5\\%$).\nThe improvement concentrates in the high-error subgroup ($s_1$): asymmetric coverage is 93.0\\% vs.\\ symmetric 91.0\\%.\nPractitioners should estimate full $2 \\times 2$ confusion matrices rather than assuming symmetric misclassification, particularly when FPR and FNR differ substantially.\n\n\\subsection{Complementarity with LLM Calibration}\n\\label{app:calibration}\n\nTemperature or Platt scaling~\\cite{guo2017calibration} can reduce per-subgroup misclassification rates, but does not eliminate heterogeneity $\\Delta\\pi$.\nWe simulate calibration by shrinking per-subgroup rates from $\\pi{=}[0.05, 0.25]$ ($\\Delta\\pi{=}0.20$) to $\\pi{=}[0.08, 0.15]$ ($\\Delta\\pi{=}0.07$), testing whether EC-HTE remains necessary post-calibration.\nSetup: $K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{Calibration reduces $\\Delta\\pi$ but does not eliminate it; EC-HTE corrects the residual bias. Best coverage is achieved by combining both.}\n\\label{tab:calibration}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Coverage \\\\\n\\midrule\nOracle                    & 0.043 & 0.053 & 0.963 \\\\\nCalibrated + EC-HTE       & 0.055 & 0.069 & \\textbf{0.965} \\\\\nCalibrated + Global       & 0.055 & 0.068 & 0.963 \\\\\nCalibrated + Naive        & 0.051 & 0.064 & 0.913 \\\\\nUncalibrated + EC-HTE     & 0.064 & 0.084 & 0.938 \\\\\nUncalibrated + Global     & 0.069 & 0.085 & 0.920 \\\\\nUncalibrated + Naive      & 0.063 & 0.079 & 0.840 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCalibration alone improves naive coverage from 84.0\\% to 91.3\\% but does not reach the nominal 95\\%.\nCalibrated + EC-HTE achieves the highest coverage (96.5\\%), demonstrating that calibration and EC-HTE address complementary error sources: calibration reduces per-subgroup $\\pi_s$ while EC-HTE corrects the residual $\\delta_s$-driven bias from heterogeneity that persists post-calibration.\nPropensity estimation robustness under model misspecification is an orthogonal concern addressed by the IPW literature; EC-HTE as a downstream correction layer does not alter IPW behavior.\n",
    "structuredPatch": [
      {
        "oldStart": 1347,
        "oldLines": 4,
        "newStart": 1347,
        "newLines": 4,
        "lines": [
          " ",
          " Calibration alone improves naive coverage from 84.0\\% to 91.3\\% but does not reach the nominal 95\\%.",
          " Calibrated + EC-HTE achieves the highest coverage (96.5\\%), demonstrating that calibration and EC-HTE address complementary error sources: calibration reduces per-subgroup $\\pi_s$ while EC-HTE corrects the residual $\\delta_s$-driven bias from heterogeneity that persists post-calibration.",
          "-Propensity estimation robustness under model misspecification is an orthogonal concern addressed by the IPW literature; EC-HTE as a downstream correction layer does not alter IPW behavior.",
          "+Propensity estimation robustness under model misspecification is a complementary concern addressed by the IPW literature; EC-HTE as a downstream correction layer does not alter IPW behavior."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 80_

<details><summary>Logged reasoning block</summary>

```text
All edits done. Now let me compile to verify. But first, let me verify H7 - limitations.tex already has the "continuous effect modifier" mention, so no change needed. I confirmed this from the read.

Let me also do a quick verification that the appendix line 518 "orthogonal design" is being left alone (since it's a statistical design term, not a method relationship description).

Now let me compile.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "fe3b12ab-c3e7-4569-89b7-2a25dd456b4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ci9vJr1W766kabUERh3nKr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3722,
      "cache_read_input_tokens": 67816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3722
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 81_

All edits applied. H7 (continuous effect modifier) already present in limitations.tex line 29 — no change needed. Now compiling to verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "adc28eb2-6489-4d7b-9a5d-f3e6dbd3623b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ci9vJr1W766kabUERh3nKr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3722,
      "cache_read_input_tokens": 67816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3722
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 82_

<details open><summary>🔧 Tool call — Bash · `toolu_01VBakdVUqoJdD71RGRdCCuA`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper && latexmk -pdf -interaction=nonstopmode -g main.tex 2>&1 | tail -30",
  "description": "Compile LaTeX paper",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "49918b56-a4d7-4f46-916c-9ae216a475f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ci9vJr1W766kabUERh3nKr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3722,
      "cache_read_input_tokens": 67816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3722
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### System

_source line 83_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bper0e0br",
  "tool_use_id": "toolu_01VBakdVUqoJdD71RGRdCCuA",
  "description": "Compile LaTeX paper",
  "task_type": "local_bash",
  "uuid": "204a1873-2dfd-4b2c-b4ba-6548c4e47319",
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5"
}
```

---

### System

_source line 84_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bper0e0br",
  "tool_use_id": "toolu_01VBakdVUqoJdD71RGRdCCuA",
  "status": "completed",
  "output_file": "",
  "summary": "Compile LaTeX paper",
  "uuid": "e6eb8ac6-d8fa-40bd-bf48-80c5e5ba60a2",
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5"
}
```

---

### Tool result

_source line 85 · 2026-05-23T09:30:13.449Z_

<details><summary>↩ Tool result · `toolu_01VBakdVUqoJdD71RGRdCCuA`</summary>

```text
/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/u
hvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (29 pages, 762314 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Log file says output to 'main.pdf'
Latexmk: Using bibtex to make bibliography file(s).
  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "4059907f-3a81-4215-846b-db88c82ba1a8",
  "tool_use_result": {
    "stdout": "/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/u\nhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (29 pages, 762314 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 86_

<details><summary>Logged reasoning block</summary>

```text
The compilation succeeded. Let me now check for errors, undefined references, and the page where Conclusion appears.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "cfbcd843-bf6b-4e16-bfd7-cb0a389ec3e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016a7PCxyZMJCykHe5xqpDNG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1163,
      "cache_read_input_tokens": 71538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1163
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 87_

<details open><summary>🔧 Tool call — Bash · `toolu_01SLYoVmroaxacGNTBG9QuDJ`</summary>

```json
{
  "command": "grep -c \"^!\" main.log",
  "description": "Count LaTeX errors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "a36a884c-6313-46ed-b35b-19192935bfa3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016a7PCxyZMJCykHe5xqpDNG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1163,
      "cache_read_input_tokens": 71538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1163
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-23T09:30:18.294Z_

<details><summary>↩ Tool result · `toolu_01SLYoVmroaxacGNTBG9QuDJ`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "4e0aa99a-3059-486b-a558-9e121a6ae5e7",
  "tool_use_result": {
    "stdout": "0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Bash · `toolu_01SMuCXU3miMeq6EotdcC1dy`</summary>

```json
{
  "command": "grep -i \"undefined\" main.log | grep -v \"ifluatex\" | head -20",
  "description": "Check undefined references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "e7924867-8d1a-4857-a054-522d21bbe10d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016a7PCxyZMJCykHe5xqpDNG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1163,
      "cache_read_input_tokens": 71538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1163
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-23T09:30:19.265Z_

<details><summary>↩ Tool result · `toolu_01SMuCXU3miMeq6EotdcC1dy`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "26f42274-dd8b-477a-97b7-01eea68ffb7e",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 91_

<details open><summary>🔧 Tool call — Bash · `toolu_01DvTpniZNsZcG385DSk3P9H`</summary>

```json
{
  "command": "grep -i \"Warning.*Citation.*undefined\" main.log | head -10",
  "description": "Check undefined citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "4898e509-0ae5-42f7-9e01-55bd7803a9c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016a7PCxyZMJCykHe5xqpDNG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1163,
      "cache_read_input_tokens": 71538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1163
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-23T09:30:20.115Z_

<details><summary>↩ Tool result · `toolu_01DvTpniZNsZcG385DSk3P9H`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "178a63bb-a44e-4d24-bb64-5f8cfd98e133",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Bash · `toolu_01YQgYKNauUYLnYVJTMKEeDq`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\nlines = text.split('\\n')\nfor i, line in enumerate(lines):\n    if 'Conclusion' in line and 'Table of' not in line:\n        # Find page by counting form feeds\n        page = text[:text.index(line)].count('\\x0c') + 1\n        print(f'Conclusion found on page {page}: {line.strip()[:60]}')\n        break\n\"",
  "description": "Find Conclusion page number"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "05c8c6f4-0ba6-4738-a06d-e9fa2986cf05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0148r3JW5mv8N44HgZeEU6yv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 361,
      "cache_read_input_tokens": 72701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 361
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-23T09:30:27.147Z_

<details><summary>↩ Tool result · `toolu_01YQgYKNauUYLnYVJTMKEeDq`</summary>

```text
Conclusion found on page 8: Conclusion
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "5d712a51-6cf8-450d-ba48-53042a6d064d",
  "tool_use_result": {
    "stdout": "Conclusion found on page 8: Conclusion",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 95_

All checks pass:
- **0 errors**
- **0 undefined references**
- **Conclusion on page 8**

### 改动清单

| # | 项目 | 文件 | 改动 |
|---|------|------|------|
| H1 | Abstract 精简 | `abstract.tex` | 删除 5×、5.9×、520、eight、two；替换为定性描述；保留 50%、7.4×、AUC=1.0、≥0.90 |
| H2 | "exact identity" 缩减 | `abstract.tex`, `introduction.tex` (×2), `theory.tex`, `related_work.tex`, `conclusion.tex` | 6 处 "exact identity/finite-population identity, not a bound" → "bias identity/bias decomposition/population-level identity"；保留 theory.tex Thm 1 环境 + intro.tex 首次提及 |
| H3 | 补充 3 篇引用 | `references.bib`, `related_work.tex` | 添加 camuffo2025variance、cheng2024err、ura2015heterogeneous；related_work 各加 1 句讨论，同时压缩 Frazis 讨论段落保持净零 |
| H4 | theory.tex 交叉引用 | `theory.tex` | Proof sketch 后加 "For comparison with classical scalar attenuation, see Section related"；frazis2003estimating 已存在 |
| H5 | orthogonal→complementary | `appendix.tex` (×4) | 517: orthogonality→complementarity；1236, 1349, 1350: orthogonal→complementary；保留 518 "orthogonal design"（统计术语） |
| H6 | Table 1 header | `experiments.tex` | Cov. → 95% CI Cov.；$|\text{Bias}|$ 已正确 |
| H7 | Continuous effect modifier | `limitations.tex` | 已有 "Continuous effect modifiers or latent subgroup discovery settings require different approaches"，无需修改 |
| H8 | Törnberg 年份 | `references.bib` | year={2025} → year={2024} |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "uuid": "592ffe76-1600-4afa-a98b-cd7ed8cca58a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBxtwuX63VP7m9mGCy4vbT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 237,
      "cache_read_input_tokens": 73062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 237
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 96_

All checks pass:
- **0 errors**
- **0 undefined references**
- **Conclusion on page 8**

### 改动清单

| # | 项目 | 文件 | 改动 |
|---|------|------|------|
| H1 | Abstract 精简 | `abstract.tex` | 删除 5×、5.9×、520、eight、two；替换为定性描述；保留 50%、7.4×、AUC=1.0、≥0.90 |
| H2 | "exact identity" 缩减 | `abstract.tex`, `introduction.tex` (×2), `theory.tex`, `related_work.tex`, `conclusion.tex` | 6 处 "exact identity/finite-population identity, not a bound" → "bias identity/bias decomposition/population-level identity"；保留 theory.tex Thm 1 环境 + intro.tex 首次提及 |
| H3 | 补充 3 篇引用 | `references.bib`, `related_work.tex` | 添加 camuffo2025variance、cheng2024err、ura2015heterogeneous；related_work 各加 1 句讨论，同时压缩 Frazis 讨论段落保持净零 |
| H4 | theory.tex 交叉引用 | `theory.tex` | Proof sketch 后加 "For comparison with classical scalar attenuation, see Section related"；frazis2003estimating 已存在 |
| H5 | orthogonal→complementary | `appendix.tex` (×4) | 517: orthogonality→complementarity；1236, 1349, 1350: orthogonal→complementary；保留 518 "orthogonal design"（统计术语） |
| H6 | Table 1 header | `experiments.tex` | Cov. → 95% CI Cov.；$|\text{Bias}|$ 已正确 |
| H7 | Continuous effect modifier | `limitations.tex` | 已有 "Continuous effect modifiers or latent subgroup discovery settings require different approaches"，无需修改 |
| H8 | Törnberg 年份 | `references.bib` | year={2025} → year={2024} |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 440414,
  "duration_api_ms": 424046,
  "num_turns": 38,
  "stop_reason": "end_turn",
  "session_id": "43ad27ba-f674-4dfb-85c2-3efa15fcd6a5",
  "total_cost_usd": 1.2343294999999999,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 61458,
    "cache_read_input_tokens": 522548,
    "output_tokens": 23460,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 61458,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 592,
        "cache_read_input_tokens": 73062,
        "cache_creation_input_tokens": 237,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 237
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2288,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002388,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 23460,
      "cacheReadInputTokens": 522548,
      "cacheCreationInputTokens": 61458,
      "webSearchRequests": 0,
      "costUSD": 1.2319415,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8c0b77b3-5676-4073-960f-174bbd5ca268"
}
```

</details>

---
