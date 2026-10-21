# latex swap fig1 fig2

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_latex_swap-fig1-fig2_20260524T165903.log`
- **Structured JSON:** [`4ba01198a89bc03f2996.json`](../../sessions/4b/4ba01198a89bc03f2996.json)

## Before a recorded user message

23 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
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
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
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
  "uuid": "691adff8-f93f-4a15-ada5-a27b85d2cc96",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias/memory/"
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
    "resetsAt": 1779643800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "df08c999-f5ef-470b-946d-f3a970b78393",
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the relevant LaTeX files to understand the current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "f93d2c91-2dc7-44e8-8ec6-1a5520498c03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2BYc36ocGsJ9yEnioMHxx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12712,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12712
      },
      "output_tokens": 22,
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

读取相关 LaTeX 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "a18013b2-73d5-44c2-b922-1aa3e417ff1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2BYc36ocGsJ9yEnioMHxx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12712,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12712
      },
      "output_tokens": 22,
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

<details open><summary>🔧 Tool call — Read · `toolu_01HsjmAs7XbgjqXmdRUFwZJ4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "a13946ed-874b-4938-a091-c1318275b6dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2BYc36ocGsJ9yEnioMHxx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12712,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12712
      },
      "output_tokens": 22,
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

_source line 7 · 2026-05-24T16:59:17.009Z_

<details><summary>↩ Tool result · `toolu_01HsjmAs7XbgjqXmdRUFwZJ4`</summary>

```text
1	\section{Confounding in LLM Evaluation}
2	\label{sec:confounding}
3	
4	The Many-Facet Rasch Model (MFRM) extends classical Rasch measurement to settings with multiple rater facets \citep{linacre1989mfrm, linacre1994mfrm}. Originating in educational measurement, the model treats rater variation as a nuisance facet to be estimated and removed rather than a source of noise to be averaged over. In the LLM evaluation context, where $J$ judges score $N$ models across $I$ items, the MFRM specifies
5	%
6	\begin{equation}
7	\label{eq:mfrm}
8	\log \frac{P(Y_{nij} \geq k \mid \theta_n, b_i, d_j, \tau_k)}{P(Y_{nij} < k \mid \theta_n, b_i, d_j, \tau_k)} = \theta_n - b_i - d_j - \tau_k,
9	\end{equation}
10	%
11	where $Y_{nij}$ is the ordinal rating by judge $j$ for model $n$ on item $i$, $\theta_n$ is the ability of model $n$ ($n = 1, \ldots, N$), $b_i$ is the difficulty of item $i$ ($i = 1, \ldots, I$), $d_j$ is the severity of judge $j$ ($j = 1, \ldots, J$), and $\tau_k$ is the threshold for category $k$. All facets reside on a common logit scale, so model ability is directly comparable after adjustment for item difficulty and judge severity. \citet{jiao2025mfrm_llm} applied this framework to compare ten LLM raters with human experts, showing that MFRM separates genuine ability from systematic judge effects in multi-judge panels.
12	
13	However, standard MFRM assumes that all systematic sources of score variation are captured by the modeled facets. This assumption breaks down when some models have been exposed to benchmark items during training \citep{dcr2025}. Such contamination inflates scores on exposed items through memorization rather than genuine ability. We represent this effect as an interaction $c_n \cdot e_i$, where $c_n \geq 0$ is the contamination susceptibility of model $n$ and $e_i \in [0, 1]$ is the exposure level of item $i$. The complete data-generating process becomes
14	%
15	\begin{equation}
16	\label{eq:full}
17	\eta_{nijk} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i.
18	\end{equation}
19	%
20	When a practitioner fits the standard MFRM (Eq.~\ref{eq:mfrm}) to data generated by Eq.~\ref{eq:full}, the contamination term is absent from the estimated model. Its influence does not vanish but is absorbed into the estimated parameters $\tilde{\theta}_n$, $\tilde{b}_i$, and $\tilde{d}_j$, which distorts all downstream inferences.
21	
22	The consequence of this omission can be stated precisely.
23	
24	\begin{observation}[Omitted Variable Bias in MFRM]
25	\label{obs:ovb}
26	Let the full model be $\eta_{nijk} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i$ and the short model omit the contamination term: $\tilde{\eta}_{nijk} = \tilde{\theta}_n - \tilde{b}_i - \tilde{d}_j - \tau_k$. Under a linear approximation to the ordinal logit link \citep{wooldridge2010, angrist2009mostly},\footnote{The OVB formula is exact for linear models. We apply it to the MFRM linear predictor $\eta$, which is an approximation. Synthetic validation confirms the approximation quality: the Pearson correlation between the predicted bias direction and empirical bias reaches $r = 0.86$ ($p < 0.001$), indicating that the linear result accurately characterizes bias direction and relative magnitude.}
27	\begin{equation}
28	\label{eq:ovb}
29	\mathrm{plim}(\tilde{\theta}_n - \theta_n) = \gamma_n \cdot c_n,
30	\end{equation}
31	where $\gamma_n$ depends on the projection of the exposure vector $(e_i)$ onto the design matrix of the short model (explicit form in Appendix~\ref{app:gamma}). The bias is non-zero whenever $\mathrm{Cov}(d_j,\, c_n \cdot e_i) \neq 0$. This captures the confounding component; in the nonlinear MFRM, a specification bias from omitting $c_n \cdot e_i$ persists even at zero covariance (Section~\ref{sec:experiments}).
32	\end{observation}
33	
34	The linear approximation in Observation~\ref{obs:ovb} ($r = 0.86$) serves solely as directional motivation for the bias structure; G-MFRM's Stage~3 inference (Eq.~\ref{eq:gmfrm}) uses the full nonlinear ordinal logistic likelihood and does not depend on this approximation. The bias combines a specification component from omitting $c_n \cdot e_i$, which persists regardless of confounding, with a confounding component from non-orthogonality between $d_j$ and $c_n \cdot e_i$. Monte Carlo simulation confirms that bias magnitude is approximately constant across confounding levels $\rho \in \{0, 0.3, 0.6, 0.9\}$, indicating that the omission of $c_n \cdot e_i$---not its correlation with $d_j$---is the primary driver (Figure~\ref{fig:bias_vs_rho}).
35	
36	This confounding undermines both sequential estimation strategies. A bias-first approach, as in CyclicJudge \citep{cyclicjudge2026}, calibrates $d_j$ before estimating ability, but the resulting $\hat{\theta}$ is already inflated for contaminated models because the omitted $c_n \cdot e_i$ term has been absorbed into the ability estimates. A contamination-first approach, as in DCR \citep{dcr2025}, adjusts for contamination before addressing judge effects, but judge severity is then misattributed as contamination signal. Synthetic validation confirms this failure: with $N = 50$ models, $I = 100$ items, $J = 8$ judges, and 20 random seeds, the Pearson correlation between sequential estimation bias and true $c_n$ reaches $r = 0.86$ ($p < 0.001$). As illustrated in Figure~\ref{fig:ovb_bias}, the bias is not random but directional: contaminated models are systematically overestimated under both sequential orderings.
37	
38	\begin{figure}[t]
39	\centering
40	\includegraphics[width=\columnwidth]{fig2_ovb_bias}
41	\caption{Sequential estimation bias ($\hat{\theta}_{\mathrm{seq}} - \theta_{\mathrm{true}}$) versus true contamination susceptibility $c_n$. Pearson $r = 0.86$ ($p < 0.001$) confirms systematic overestimation of contaminated models. Synthetic data ($N = 50$, $I = 100$, $J = 8$, 20 seeds).}
42	\label{fig:ovb_bias}
43	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "3e6e6ede-45da-43fd-acb3-8d0fbd42c2db",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex",
      "content": "\\section{Confounding in LLM Evaluation}\n\\label{sec:confounding}\n\nThe Many-Facet Rasch Model (MFRM) extends classical Rasch measurement to settings with multiple rater facets \\citep{linacre1989mfrm, linacre1994mfrm}. Originating in educational measurement, the model treats rater variation as a nuisance facet to be estimated and removed rather than a source of noise to be averaged over. In the LLM evaluation context, where $J$ judges score $N$ models across $I$ items, the MFRM specifies\n%\n\\begin{equation}\n\\label{eq:mfrm}\n\\log \\frac{P(Y_{nij} \\geq k \\mid \\theta_n, b_i, d_j, \\tau_k)}{P(Y_{nij} < k \\mid \\theta_n, b_i, d_j, \\tau_k)} = \\theta_n - b_i - d_j - \\tau_k,\n\\end{equation}\n%\nwhere $Y_{nij}$ is the ordinal rating by judge $j$ for model $n$ on item $i$, $\\theta_n$ is the ability of model $n$ ($n = 1, \\ldots, N$), $b_i$ is the difficulty of item $i$ ($i = 1, \\ldots, I$), $d_j$ is the severity of judge $j$ ($j = 1, \\ldots, J$), and $\\tau_k$ is the threshold for category $k$. All facets reside on a common logit scale, so model ability is directly comparable after adjustment for item difficulty and judge severity. \\citet{jiao2025mfrm_llm} applied this framework to compare ten LLM raters with human experts, showing that MFRM separates genuine ability from systematic judge effects in multi-judge panels.\n\nHowever, standard MFRM assumes that all systematic sources of score variation are captured by the modeled facets. This assumption breaks down when some models have been exposed to benchmark items during training \\citep{dcr2025}. Such contamination inflates scores on exposed items through memorization rather than genuine ability. We represent this effect as an interaction $c_n \\cdot e_i$, where $c_n \\geq 0$ is the contamination susceptibility of model $n$ and $e_i \\in [0, 1]$ is the exposure level of item $i$. The complete data-generating process becomes\n%\n\\begin{equation}\n\\label{eq:full}\n\\eta_{nijk} = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i.\n\\end{equation}\n%\nWhen a practitioner fits the standard MFRM (Eq.~\\ref{eq:mfrm}) to data generated by Eq.~\\ref{eq:full}, the contamination term is absent from the estimated model. Its influence does not vanish but is absorbed into the estimated parameters $\\tilde{\\theta}_n$, $\\tilde{b}_i$, and $\\tilde{d}_j$, which distorts all downstream inferences.\n\nThe consequence of this omission can be stated precisely.\n\n\\begin{observation}[Omitted Variable Bias in MFRM]\n\\label{obs:ovb}\nLet the full model be $\\eta_{nijk} = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$ and the short model omit the contamination term: $\\tilde{\\eta}_{nijk} = \\tilde{\\theta}_n - \\tilde{b}_i - \\tilde{d}_j - \\tau_k$. Under a linear approximation to the ordinal logit link \\citep{wooldridge2010, angrist2009mostly},\\footnote{The OVB formula is exact for linear models. We apply it to the MFRM linear predictor $\\eta$, which is an approximation. Synthetic validation confirms the approximation quality: the Pearson correlation between the predicted bias direction and empirical bias reaches $r = 0.86$ ($p < 0.001$), indicating that the linear result accurately characterizes bias direction and relative magnitude.}\n\\begin{equation}\n\\label{eq:ovb}\n\\mathrm{plim}(\\tilde{\\theta}_n - \\theta_n) = \\gamma_n \\cdot c_n,\n\\end{equation}\nwhere $\\gamma_n$ depends on the projection of the exposure vector $(e_i)$ onto the design matrix of the short model (explicit form in Appendix~\\ref{app:gamma}). The bias is non-zero whenever $\\mathrm{Cov}(d_j,\\, c_n \\cdot e_i) \\neq 0$. This captures the confounding component; in the nonlinear MFRM, a specification bias from omitting $c_n \\cdot e_i$ persists even at zero covariance (Section~\\ref{sec:experiments}).\n\\end{observation}\n\nThe linear approximation in Observation~\\ref{obs:ovb} ($r = 0.86$) serves solely as directional motivation for the bias structure; G-MFRM's Stage~3 inference (Eq.~\\ref{eq:gmfrm}) uses the full nonlinear ordinal logistic likelihood and does not depend on this approximation. The bias combines a specification component from omitting $c_n \\cdot e_i$, which persists regardless of confounding, with a confounding component from non-orthogonality between $d_j$ and $c_n \\cdot e_i$. Monte Carlo simulation confirms that bias magnitude is approximately constant across confounding levels $\\rho \\in \\{0, 0.3, 0.6, 0.9\\}$, indicating that the omission of $c_n \\cdot e_i$---not its correlation with $d_j$---is the primary driver (Figure~\\ref{fig:bias_vs_rho}).\n\nThis confounding undermines both sequential estimation strategies. A bias-first approach, as in CyclicJudge \\citep{cyclicjudge2026}, calibrates $d_j$ before estimating ability, but the resulting $\\hat{\\theta}$ is already inflated for contaminated models because the omitted $c_n \\cdot e_i$ term has been absorbed into the ability estimates. A contamination-first approach, as in DCR \\citep{dcr2025}, adjusts for contamination before addressing judge effects, but judge severity is then misattributed as contamination signal. Synthetic validation confirms this failure: with $N = 50$ models, $I = 100$ items, $J = 8$ judges, and 20 random seeds, the Pearson correlation between sequential estimation bias and true $c_n$ reaches $r = 0.86$ ($p < 0.001$). As illustrated in Figure~\\ref{fig:ovb_bias}, the bias is not random but directional: contaminated models are systematically overestimated under both sequential orderings.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_ovb_bias}\n\\caption{Sequential estimation bias ($\\hat{\\theta}_{\\mathrm{seq}} - \\theta_{\\mathrm{true}}$) versus true contamination susceptibility $c_n$. Pearson $r = 0.86$ ($p < 0.001$) confirms systematic overestimation of contaminated models. Synthetic data ($N = 50$, $I = 100$, $J = 8$, 20 seeds).}\n\\label{fig:ovb_bias}\n\\end{figure}",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01G7hQP9PFyn9G3QYyi2jWby`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "3af288cf-ea93-463c-9983-7d811748857e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2BYc36ocGsJ9yEnioMHxx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12712,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12712
      },
      "output_tokens": 22,
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

_source line 9 · 2026-05-24T16:59:17.503Z_

<details><summary>↩ Tool result · `toolu_01G7hQP9PFyn9G3QYyi2jWby`</summary>

```text
1	\section{The G-MFRM Framework}
2	\label{sec:method}
3	
4	Section~\ref{sec:confounding} established that omitting contamination from the measurement model produces directional bias in ability estimates (Observation~\ref{obs:ovb}). We now introduce the Gated Many-Facet Rasch Model (G-MFRM), which jointly estimates ability, judge severity, and contamination susceptibility within a single measurement framework. The key design choices, staged estimation with externally fixed exposure and a hierarchical HalfNormal prior for the contamination term, are motivated by the identifiability analysis in \S\ref{sec:identifiability} and the error propagation bounds in \S\ref{sec:error_prop}.
5	
6	\begin{figure*}[t]
7	\centering
8	\includegraphics[width=\textwidth]{fig1_framework_v2}
9	\caption{(a)~Sequential pipelines address judge bias and contamination independently; omitted variable bias confounds the unmodeled facet into ability estimates. (b)~G-MFRM three-stage joint calibration: Stage~1 fits a standard MFRM for initial estimates $(\hat{\theta}, \hat{b}, \hat{d})$; Stage~2 estimates per-item exposure $e_i$ from external evidence (reference model anchoring, cross-model agreement, and optionally LogProber); Stage~3 performs joint MCMC inference with $e_i$ fixed, recovering contamination-corrected ability $\tilde{\theta}_n$, contamination susceptibility $c_n$, and judge severity $d_j$.}
10	\label{fig:framework}
11	\end{figure*}
12	
13	\subsection{Model Specification}
14	\label{sec:model_spec}
15	
16	G-MFRM extends the standard MFRM \citep{linacre1989mfrm, linacre1994mfrm} by adding a multiplicative contamination gating term to the linear predictor (Eq.~\ref{eq:mfrm}):
17	%
18	\begin{equation}
19	\label{eq:gmfrm}
20	\log \frac{P(Y_{nij} \geq k)}{P(Y_{nij} < k)} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i,
21	\end{equation}
22	%
23	where all terms carry the definitions from Section~\ref{sec:confounding}. The gating structure $c_n \cdot e_i$ separates the model-specific and item-specific components of contamination: $c_n \geq 0$ captures how much model $n$ benefits from memorized benchmark content, while $e_i \in [0,1]$ quantifies how much of item $i$ has leaked into training corpora. When $c_n = 0$ (a clean model) or $e_i = 0$ (a novel item), the gating term vanishes and Eq.~\ref{eq:gmfrm} reduces to the standard MFRM. This graceful degradation ensures that G-MFRM imposes no distortion on uncontaminated model-item pairs.
24	
25	We enforce non-negativity and sparsity of $c_n$ through a hierarchical HalfNormal prior. A global shrinkage scale $\sigma_c \sim \text{HalfNormal}(1.0)$ controls the overall contamination level, and per-model raw effects $c^{\mathrm{raw}}_n \sim \text{HalfNormal}(1.0)$ are scaled to obtain $c_n = c^{\mathrm{raw}}_n \cdot \sigma_c$. The HalfNormal support restricts $c_n \geq 0$, and the hierarchical structure provides adaptive shrinkage: when the data support low overall contamination, $\sigma_c$ contracts toward zero, pulling all $c_n$ values down. Models with genuine contamination retain large $c^{\mathrm{raw}}_n$ relative to the group. The remaining priors are $\theta_n \sim \mathcal{N}(0, 1)$, $b_i \sim \mathcal{N}(0, 1)$, $d_j \sim \mathcal{N}(0, 0.5)$, and standard uniform on thresholds $\tau_k$.
26	
27	The closest antecedent is the Doubly-Gated IRT model of \citet{shu2013dgirt}, which introduced binary gating for item preknowledge in educational testing. Beyond extending DG-IRT to continuous exposure and multi-rater designs, G-MFRM's primary methodological contributions are analytical: the identifiability analysis (Propositions~\ref{prop:no_new}--\ref{prop:exposure_variation} and Theorem~\ref{thm:sufficient}) provides the first formal conditions under which gated IRT parameters are separable, and the Murphy--Topel error propagation framework (\S\ref{sec:error_prop}) quantifies how staged estimation uncertainty propagates to downstream parameter estimates---neither of which exists for DG-IRT or any prior gated measurement model.
28	
29	\subsection{Staged Estimation}
30	\label{sec:staged}
31	
32	Joint estimation of all parameters in Eq.~\ref{eq:gmfrm}, including $e_i$, would require identifying the bilinear product $c_n \cdot e_i$ from response data alone. This creates a fundamental non-identifiability (Proposition~\ref{prop:exposure_variation}). We resolve this through a three-stage procedure that fixes exposure externally before estimating the contamination parameters.
33	
34	\paragraph{Stage 1: Standard MFRM.} We fit the standard MFRM (Eq.~\ref{eq:mfrm}) via MCMC (NUTS) to obtain initial estimates $(\hat{\theta}, \hat{b}, \hat{d})$. These serve as warm-start values for the sampler in Stage~3 and improve convergence.
35	
36	\paragraph{Stage 2: Exposure estimation.} Per-item exposure $e_i$ is estimated from external evidence independent of the response data used in Stages~1 and~3. The primary signal is \emph{reference model anchoring}: using a fixed reference model (e.g., gpt-4-0314) as anchor, we compute win-rate residuals for each target model against difficulty-adjusted expectations; items where target models systematically outperform the anchor beyond what difficulty predicts are flagged as potentially exposed. The secondary signal is \emph{cross-model agreement}: items receiving uniformly high scores across architecturally diverse models suggest exposure rather than genuine easiness, quantified via $z$-score standardization of the inter-model agreement distribution. These signals are combined as a weighted composite (75\% anchoring, 25\% agreement), clipped to $[0, 1]$, and treated as fixed in Stage~3. Where model log-probabilities are accessible, LogProber can provide an additional gray-box memorization signal, though it is not used in our current experiments.
37	
38	\paragraph{Non-circularity.} Exposure estimation is not circular: $e_i$ is item-level (content leakage) while $c_n$ is model-level (susceptibility), testing a cross-level interaction. The primary signal (75\%) derives from reference anchoring independent of target models, and ablation with 100\% anchoring yields $\rho = 0.998$ (Appendix~\ref{app:weight_robustness}), confirming $e_i$ is robust to removing the cross-model component.
39	
40	\paragraph{Stage 3: Joint MCMC.} With $e_i$ fixed, we sample $(\theta_n, b_i, d_j, c_n)$ jointly via NUTS \citep{betancourt2015}. The priors are as specified in \S\ref{sec:model_spec}. The hierarchical contamination prior decomposes as
41	%
42	\begin{align}
43	\label{eq:contam_prior}
44	\sigma_c &\sim \text{HalfNormal}(1.0), \quad c^{\mathrm{raw}}_n \sim \text{HalfNormal}(1.0), \nonumber \\
45	c_n &= c^{\mathrm{raw}}_n \cdot \sigma_c,
46	\end{align}
47	%
48	where $\sigma_c$ is a shared global scale that governs the overall contamination magnitude. This non-centered parameterization improves sampler geometry by decoupling the global scale from the per-model effects.
49	
50	Convergence is assessed via rank-normalized split-$\hat{R}$ \citep{vehtari2021rhat} and bulk effective sample size (ESS), with thresholds $\hat{R} < 1.05$ and ESS$_{\mathrm{bulk}} > 100$ following standard practice \citep{gelman2013bda}.\footnote{Synthetic validation with $N = 50$, $I = 100$, $J = 8$ yields satisfactory convergence across all parameters (exp-012). Full diagnostic tables are reported in Section~\ref{sec:experiments}.}
51	
52	
53	\subsection{Identifiability}
54	\label{sec:identifiability}
55	
56	Adding a multiplicative term to a measurement model raises the question of whether the new parameters can be separated from the existing ones. We establish that fixing $e_i$ externally is both necessary and sufficient for identification. All proofs assume the standard location constraint $\sum_n \theta_n = 0$.
57	
58	\begin{proposition}[No New Indeterminacy]
59	\label{prop:no_new}
60	When $e_i$ is fixed externally, the gating term $c_n \cdot e_i$ introduces no additional location or scale indeterminacy beyond that already present in the standard MFRM.
61	\end{proposition}
62	
63	\begin{proof}
64	Suppose $c_n' = c_n + \delta$ preserves all response probabilities. Then $\delta \cdot e_i = 0$ for all items. Since $e_i \neq 0$ for at least one item by assumption, $\delta = 0$. The key observation is that fixing $e_i$ externally eliminates the bilinear ambiguity $c_n \cdot e_i = (\lambda c_n)(\lambda^{-1} e_i)$ that would otherwise render the decomposition non-unique.
65	\end{proof}
66	
67	\begin{proposition}[Exposure Variation Necessary]
68	\label{prop:exposure_variation}
69	If $e_i = e$ for all $i$ (constant exposure), then $c_n$ and $\theta_n$ are not separately identifiable.
70	\end{proposition}
71	
72	\begin{proof}
73	When exposure is constant, the linear predictor becomes $(\theta_n + c_n \cdot e) - b_i - d_j - \tau_k$, which is equivalent to a standard MFRM with reparameterized ability $\theta^*_n = \theta_n + c_n \cdot e$. No configuration of response data can distinguish $(\theta_n, c_n)$ from $(\theta_n + \epsilon, c_n - \epsilon/e)$ for any $\epsilon$.
74	\end{proof}
75	
76	\begin{corollary}
77	$\mathrm{Var}(e_i) > 0$ is a necessary condition for identifiability of $c_n$.
78	\end{corollary}
79	
80	\begin{theorem}[Sufficient Conditions for Local Identifiability]
81	\label{thm:sufficient}
82	The G-MFRM is locally identifiable, up to the standard location constraint, if the following conditions hold: (i) a connected observation design (each item is observed by at least one model--judge pair), (ii) $J \geq 2$ judges, (iii) for each model $n$, the set of observed items spans at least two distinct exposure values ($\mathrm{Var}(e_i) > 0$ over observed items), and (iv) standard normalization $\sum_n \theta_n = 0$.
83	\end{theorem}
84	
85	The proof, given in Appendix~\ref{app:proof}, follows \citet{rothenberg1971}: non-singularity of the Fisher information matrix is established via the Cauchy--Schwarz inequality on the $(\theta_n, c_n)$ submatrix determinant and a Schur complement argument for the remaining blocks. Conditions~(i) and~(ii) are standard multi-rater design requirements, satisfied by the connected design in our evaluation (XX.X\% fill rate; \S\ref{sec:setup}); condition~(iii) is the substantive constraint that each model's observed items include varying exposure levels.
86	
87	\subsection{Error Propagation}
88	\label{sec:error_prop}
89	
90	The staged procedure treats the Stage~2 exposure estimates $\hat{e}_i$ as fixed quantities in Stage~3. This is a generated regressors problem \citep{pagan1984}: measurement error in $\hat{e}_i$ propagates into the posterior of $(\theta_n, c_n)$. The multiplicative structure $c_n \cdot e_i$ makes this an errors-in-variables (EIV) problem \citep{fuller1987}, with a predictable attenuation pattern.
91	
92	Let $\hat{e}_i = e_i + \epsilon_i$ with $\epsilon_i \sim \mathcal{N}(0, \sigma^2)$ independent of all model parameters. The attenuation factor for the contamination coefficient is
93	%
94	\begin{equation}
95	\label{eq:attenuation}
96	\lambda(\sigma) = \frac{\mathrm{Var}(e_i)}{\mathrm{Var}(e_i) + \sigma^2},
97	\end{equation}
98	%
99	so attenuation reaches 50\% when $\sigma = \sqrt{\mathrm{Var}(e_i)}$. In the synthetic DGP ($\mathrm{Var}(e_i) \approx 0.04$), this corresponds to $\sigma \approx 0.2$.\footnote{The attenuation formula assumes that $\epsilon_i$ is independent of all model parameters, identically distributed, and Gaussian. In practice, exposure estimation errors may be correlated across items sharing the same source or heteroscedastic across difficulty levels. Table~\ref{tab:error_prop} provides empirical validation that $\hat{\theta}$ estimates remain robust under such departures (Section~\ref{sec:experiments}).}
100	
101	Table~\ref{tab:error_prop} shows the empirical degradation across noise levels (see also Figure~\ref{fig:error_prop} in the Appendix). Below the critical threshold ($\sigma \leq 0.2$), degradation is mild: $\theta$-RMSE increases by 5.9\% (from $0.128 \pm 0.018$ to $0.135 \pm 0.018$) and $c_n$-RMSE by 7.9\% (from $0.533 \pm 0.187$ to $0.575 \pm 0.198$). At $\sigma = 0.1$, the increases are only 1.4\% and 2.3\% respectively. Beyond the threshold ($\sigma = 0.5$), degradation becomes severe: $\theta$-RMSE rises 36.9\% and $c_n$-RMSE rises 57.9\%. Contamination estimates $c_n$ are more sensitive than ability estimates $\theta_n$ because $c_n$ enters the likelihood only through its product with $e_i$ (multiplicative coupling), while $\theta_n$ contributes additively and is anchored by all observations regardless of exposure.
102	
103	These bounds make the staged approximation falsifiable: if the noise level of the Stage~2 exposure estimates can be bounded below $\sigma_{\mathrm{crit}}$, the resulting ability estimates carry quantifiable error guarantees. For honest credible intervals that account for generated-regressor uncertainty, we apply the Murphy-Topel variance correction \citep{murphy1985} to inflate the Stage~3 posterior variance by the estimated Stage~2 sampling variability (Appendix~\ref{app:murphy_topel}).
104	
105	\subsection{Fair Scores and Diagnostics}
106	\label{sec:fair_scores}
107	
108	The Stage~3 posterior mean of $\theta_n$ provides a bias-and-contamination-corrected ``fair score'' for each model. The remaining parameters serve complementary diagnostic roles: per-model $c_n$ flags candidates for training data audit, per-judge $d_j$ informs judge calibration, and per-item $e_i$ identifies items for retirement or replacement.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "489b809f-4a3f-458a-a1db-a926e6536a50",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
      "content": "\\section{The G-MFRM Framework}\n\\label{sec:method}\n\nSection~\\ref{sec:confounding} established that omitting contamination from the measurement model produces directional bias in ability estimates (Observation~\\ref{obs:ovb}). We now introduce the Gated Many-Facet Rasch Model (G-MFRM), which jointly estimates ability, judge severity, and contamination susceptibility within a single measurement framework. The key design choices, staged estimation with externally fixed exposure and a hierarchical HalfNormal prior for the contamination term, are motivated by the identifiability analysis in \\S\\ref{sec:identifiability} and the error propagation bounds in \\S\\ref{sec:error_prop}.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_framework_v2}\n\\caption{(a)~Sequential pipelines address judge bias and contamination independently; omitted variable bias confounds the unmodeled facet into ability estimates. (b)~G-MFRM three-stage joint calibration: Stage~1 fits a standard MFRM for initial estimates $(\\hat{\\theta}, \\hat{b}, \\hat{d})$; Stage~2 estimates per-item exposure $e_i$ from external evidence (reference model anchoring, cross-model agreement, and optionally LogProber); Stage~3 performs joint MCMC inference with $e_i$ fixed, recovering contamination-corrected ability $\\tilde{\\theta}_n$, contamination susceptibility $c_n$, and judge severity $d_j$.}\n\\label{fig:framework}\n\\end{figure*}\n\n\\subsection{Model Specification}\n\\label{sec:model_spec}\n\nG-MFRM extends the standard MFRM \\citep{linacre1989mfrm, linacre1994mfrm} by adding a multiplicative contamination gating term to the linear predictor (Eq.~\\ref{eq:mfrm}):\n%\n\\begin{equation}\n\\label{eq:gmfrm}\n\\log \\frac{P(Y_{nij} \\geq k)}{P(Y_{nij} < k)} = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i,\n\\end{equation}\n%\nwhere all terms carry the definitions from Section~\\ref{sec:confounding}. The gating structure $c_n \\cdot e_i$ separates the model-specific and item-specific components of contamination: $c_n \\geq 0$ captures how much model $n$ benefits from memorized benchmark content, while $e_i \\in [0,1]$ quantifies how much of item $i$ has leaked into training corpora. When $c_n = 0$ (a clean model) or $e_i = 0$ (a novel item), the gating term vanishes and Eq.~\\ref{eq:gmfrm} reduces to the standard MFRM. This graceful degradation ensures that G-MFRM imposes no distortion on uncontaminated model-item pairs.\n\nWe enforce non-negativity and sparsity of $c_n$ through a hierarchical HalfNormal prior. A global shrinkage scale $\\sigma_c \\sim \\text{HalfNormal}(1.0)$ controls the overall contamination level, and per-model raw effects $c^{\\mathrm{raw}}_n \\sim \\text{HalfNormal}(1.0)$ are scaled to obtain $c_n = c^{\\mathrm{raw}}_n \\cdot \\sigma_c$. The HalfNormal support restricts $c_n \\geq 0$, and the hierarchical structure provides adaptive shrinkage: when the data support low overall contamination, $\\sigma_c$ contracts toward zero, pulling all $c_n$ values down. Models with genuine contamination retain large $c^{\\mathrm{raw}}_n$ relative to the group. The remaining priors are $\\theta_n \\sim \\mathcal{N}(0, 1)$, $b_i \\sim \\mathcal{N}(0, 1)$, $d_j \\sim \\mathcal{N}(0, 0.5)$, and standard uniform on thresholds $\\tau_k$.\n\nThe closest antecedent is the Doubly-Gated IRT model of \\citet{shu2013dgirt}, which introduced binary gating for item preknowledge in educational testing. Beyond extending DG-IRT to continuous exposure and multi-rater designs, G-MFRM's primary methodological contributions are analytical: the identifiability analysis (Propositions~\\ref{prop:no_new}--\\ref{prop:exposure_variation} and Theorem~\\ref{thm:sufficient}) provides the first formal conditions under which gated IRT parameters are separable, and the Murphy--Topel error propagation framework (\\S\\ref{sec:error_prop}) quantifies how staged estimation uncertainty propagates to downstream parameter estimates---neither of which exists for DG-IRT or any prior gated measurement model.\n\n\\subsection{Staged Estimation}\n\\label{sec:staged}\n\nJoint estimation of all parameters in Eq.~\\ref{eq:gmfrm}, including $e_i$, would require identifying the bilinear product $c_n \\cdot e_i$ from response data alone. This creates a fundamental non-identifiability (Proposition~\\ref{prop:exposure_variation}). We resolve this through a three-stage procedure that fixes exposure externally before estimating the contamination parameters.\n\n\\paragraph{Stage 1: Standard MFRM.} We fit the standard MFRM (Eq.~\\ref{eq:mfrm}) via MCMC (NUTS) to obtain initial estimates $(\\hat{\\theta}, \\hat{b}, \\hat{d})$. These serve as warm-start values for the sampler in Stage~3 and improve convergence.\n\n\\paragraph{Stage 2: Exposure estimation.} Per-item exposure $e_i$ is estimated from external evidence independent of the response data used in Stages~1 and~3. The primary signal is \\emph{reference model anchoring}: using a fixed reference model (e.g., gpt-4-0314) as anchor, we compute win-rate residuals for each target model against difficulty-adjusted expectations; items where target models systematically outperform the anchor beyond what difficulty predicts are flagged as potentially exposed. The secondary signal is \\emph{cross-model agreement}: items receiving uniformly high scores across architecturally diverse models suggest exposure rather than genuine easiness, quantified via $z$-score standardization of the inter-model agreement distribution. These signals are combined as a weighted composite (75\\% anchoring, 25\\% agreement), clipped to $[0, 1]$, and treated as fixed in Stage~3. Where model log-probabilities are accessible, LogProber can provide an additional gray-box memorization signal, though it is not used in our current experiments.\n\n\\paragraph{Non-circularity.} Exposure estimation is not circular: $e_i$ is item-level (content leakage) while $c_n$ is model-level (susceptibility), testing a cross-level interaction. The primary signal (75\\%) derives from reference anchoring independent of target models, and ablation with 100\\% anchoring yields $\\rho = 0.998$ (Appendix~\\ref{app:weight_robustness}), confirming $e_i$ is robust to removing the cross-model component.\n\n\\paragraph{Stage 3: Joint MCMC.} With $e_i$ fixed, we sample $(\\theta_n, b_i, d_j, c_n)$ jointly via NUTS \\citep{betancourt2015}. The priors are as specified in \\S\\ref{sec:model_spec}. The hierarchical contamination prior decomposes as\n%\n\\begin{align}\n\\label{eq:contam_prior}\n\\sigma_c &\\sim \\text{HalfNormal}(1.0), \\quad c^{\\mathrm{raw}}_n \\sim \\text{HalfNormal}(1.0), \\nonumber \\\\\nc_n &= c^{\\mathrm{raw}}_n \\cdot \\sigma_c,\n\\end{align}\n%\nwhere $\\sigma_c$ is a shared global scale that governs the overall contamination magnitude. This non-centered parameterization improves sampler geometry by decoupling the global scale from the per-model effects.\n\nConvergence is assessed via rank-normalized split-$\\hat{R}$ \\citep{vehtari2021rhat} and bulk effective sample size (ESS), with thresholds $\\hat{R} < 1.05$ and ESS$_{\\mathrm{bulk}} > 100$ following standard practice \\citep{gelman2013bda}.\\footnote{Synthetic validation with $N = 50$, $I = 100$, $J = 8$ yields satisfactory convergence across all parameters (exp-012). Full diagnostic tables are reported in Section~\\ref{sec:experiments}.}\n\n\n\\subsection{Identifiability}\n\\label{sec:identifiability}\n\nAdding a multiplicative term to a measurement model raises the question of whether the new parameters can be separated from the existing ones. We establish that fixing $e_i$ externally is both necessary and sufficient for identification. All proofs assume the standard location constraint $\\sum_n \\theta_n = 0$.\n\n\\begin{proposition}[No New Indeterminacy]\n\\label{prop:no_new}\nWhen $e_i$ is fixed externally, the gating term $c_n \\cdot e_i$ introduces no additional location or scale indeterminacy beyond that already present in the standard MFRM.\n\\end{proposition}\n\n\\begin{proof}\nSuppose $c_n' = c_n + \\delta$ preserves all response probabilities. Then $\\delta \\cdot e_i = 0$ for all items. Since $e_i \\neq 0$ for at least one item by assumption, $\\delta = 0$. The key observation is that fixing $e_i$ externally eliminates the bilinear ambiguity $c_n \\cdot e_i = (\\lambda c_n)(\\lambda^{-1} e_i)$ that would otherwise render the decomposition non-unique.\n\\end{proof}\n\n\\begin{proposition}[Exposure Variation Necessary]\n\\label{prop:exposure_variation}\nIf $e_i = e$ for all $i$ (constant exposure), then $c_n$ and $\\theta_n$ are not separately identifiable.\n\\end{proposition}\n\n\\begin{proof}\nWhen exposure is constant, the linear predictor becomes $(\\theta_n + c_n \\cdot e) - b_i - d_j - \\tau_k$, which is equivalent to a standard MFRM with reparameterized ability $\\theta^*_n = \\theta_n + c_n \\cdot e$. No configuration of response data can distinguish $(\\theta_n, c_n)$ from $(\\theta_n + \\epsilon, c_n - \\epsilon/e)$ for any $\\epsilon$.\n\\end{proof}\n\n\\begin{corollary}\n$\\mathrm{Var}(e_i) > 0$ is a necessary condition for identifiability of $c_n$.\n\\end{corollary}\n\n\\begin{theorem}[Sufficient Conditions for Local Identifiability]\n\\label{thm:sufficient}\nThe G-MFRM is locally identifiable, up to the standard location constraint, if the following conditions hold: (i) a connected observation design (each item is observed by at least one model--judge pair), (ii) $J \\geq 2$ judges, (iii) for each model $n$, the set of observed items spans at least two distinct exposure values ($\\mathrm{Var}(e_i) > 0$ over observed items), and (iv) standard normalization $\\sum_n \\theta_n = 0$.\n\\end{theorem}\n\nThe proof, given in Appendix~\\ref{app:proof}, follows \\citet{rothenberg1971}: non-singularity of the Fisher information matrix is established via the Cauchy--Schwarz inequality on the $(\\theta_n, c_n)$ submatrix determinant and a Schur complement argument for the remaining blocks. Conditions~(i) and~(ii) are standard multi-rater design requirements, satisfied by the connected design in our evaluation (XX.X\\% fill rate; \\S\\ref{sec:setup}); condition~(iii) is the substantive constraint that each model's observed items include varying exposure levels.\n\n\\subsection{Error Propagation}\n\\label{sec:error_prop}\n\nThe staged procedure treats the Stage~2 exposure estimates $\\hat{e}_i$ as fixed quantities in Stage~3. This is a generated regressors problem \\citep{pagan1984}: measurement error in $\\hat{e}_i$ propagates into the posterior of $(\\theta_n, c_n)$. The multiplicative structure $c_n \\cdot e_i$ makes this an errors-in-variables (EIV) problem \\citep{fuller1987}, with a predictable attenuation pattern.\n\nLet $\\hat{e}_i = e_i + \\epsilon_i$ with $\\epsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$ independent of all model parameters. The attenuation factor for the contamination coefficient is\n%\n\\begin{equation}\n\\label{eq:attenuation}\n\\lambda(\\sigma) = \\frac{\\mathrm{Var}(e_i)}{\\mathrm{Var}(e_i) + \\sigma^2},\n\\end{equation}\n%\nso attenuation reaches 50\\% when $\\sigma = \\sqrt{\\mathrm{Var}(e_i)}$. In the synthetic DGP ($\\mathrm{Var}(e_i) \\approx 0.04$), this corresponds to $\\sigma \\approx 0.2$.\\footnote{The attenuation formula assumes that $\\epsilon_i$ is independent of all model parameters, identically distributed, and Gaussian. In practice, exposure estimation errors may be correlated across items sharing the same source or heteroscedastic across difficulty levels. Table~\\ref{tab:error_prop} provides empirical validation that $\\hat{\\theta}$ estimates remain robust under such departures (Section~\\ref{sec:experiments}).}\n\nTable~\\ref{tab:error_prop} shows the empirical degradation across noise levels (see also Figure~\\ref{fig:error_prop} in the Appendix). Below the critical threshold ($\\sigma \\leq 0.2$), degradation is mild: $\\theta$-RMSE increases by 5.9\\% (from $0.128 \\pm 0.018$ to $0.135 \\pm 0.018$) and $c_n$-RMSE by 7.9\\% (from $0.533 \\pm 0.187$ to $0.575 \\pm 0.198$). At $\\sigma = 0.1$, the increases are only 1.4\\% and 2.3\\% respectively. Beyond the threshold ($\\sigma = 0.5$), degradation becomes severe: $\\theta$-RMSE rises 36.9\\% and $c_n$-RMSE rises 57.9\\%. Contamination estimates $c_n$ are more sensitive than ability estimates $\\theta_n$ because $c_n$ enters the likelihood only through its product with $e_i$ (multiplicative coupling), while $\\theta_n$ contributes additively and is anchored by all observations regardless of exposure.\n\nThese bounds make the staged approximation falsifiable: if the noise level of the Stage~2 exposure estimates can be bounded below $\\sigma_{\\mathrm{crit}}$, the resulting ability estimates carry quantifiable error guarantees. For honest credible intervals that account for generated-regressor uncertainty, we apply the Murphy-Topel variance correction \\citep{murphy1985} to inflate the Stage~3 posterior variance by the estimated Stage~2 sampling variability (Appendix~\\ref{app:murphy_topel}).\n\n\\subsection{Fair Scores and Diagnostics}\n\\label{sec:fair_scores}\n\nThe Stage~3 posterior mean of $\\theta_n$ provides a bias-and-contamination-corrected ``fair score'' for each model. The remaining parameters serve complementary diagnostic roles: per-model $c_n$ flags candidates for training data audit, per-judge $d_j$ informs judge calibration, and per-item $e_i$ identifies items for retirement or replacement.",
      "numLines": 108,
      "startLine": 1,
      "totalLines": 108
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01NVDDzdMPffiQwQMhtUmCf6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "be2306b9-ecec-46e6-820b-a1966ce8c47f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2BYc36ocGsJ9yEnioMHxx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12712,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12712
      },
      "output_tokens": 22,
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

_source line 11 · 2026-05-24T16:59:18.048Z_

<details><summary>↩ Tool result · `toolu_01NVDDzdMPffiQwQMhtUmCf6`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large Language Model (LLM) evaluation increasingly relies on LLM-as-a-judge protocols, where one or more LLM judges score model responses on structured benchmarks \citep{zheng2023mtbench}. Two well-documented sources of distortion affect these evaluations: \emph{judge bias}, where different judges assign systematically different scores to the same response, and \emph{benchmark contamination}, where models achieve inflated scores on items encountered during training. Both problems have received sustained research attention, producing separate toolkits for bias calibration and contamination detection. These toolkits treat the two distortions as independent phenomena, a separation that reflects their origins in different research communities rather than any principled argument for independence. Accurate ability ranking is essential for model selection, safety evaluation, and benchmark design; systematic distortion in estimated abilities undermines all three. Yet a practitioner who needs both corrections must apply them sequentially: first correct one source of distortion, then the other. This sequential approach produces unreliable ability estimates. In synthetic experiments with 50 models, 100 items, and 8 judges, sequential estimation yields ability root mean squared error (RMSE) of $0.254 \pm 0.045$, while joint estimation achieves $0.124 \pm 0.016$, a 51.2\% reduction (Wilcoxon $p < 0.001$). The gap does not arise from estimation noise or algorithmic limitations of individual methods; it reflects structural confounding between judge bias and contamination that no sequential pipeline can resolve.
5	
6	Existing methods address these distortions in isolation. Judge bias corrections---CyclicJudge \citep{cyclicjudge2026}, UDA \citep{uda2026}---remove systematic inter-judge differences without modeling contamination. Contamination detection tools---ConStat \citep{constat2024}, DCR \citep{dcr2025}, LogProber \citep{logprober2024}---adjust for memorization without accounting for judge effects (see Section~\ref{sec:related_work} for detailed review). A bias-first pipeline absorbs contamination-induced score inflation into ability estimates, because the bias model attributes all residual systematic variation to genuine ability. A contamination-first pipeline misattributes judge severity differences as contamination, because score elevation from a lenient judge is indistinguishable from elevation due to memorization without a joint model. In either ordering, the first correction stage produces estimates distorted by the unmodeled facet, and the second stage inherits this distortion.
7	
8	We formalize this confounding as an omitted variable bias (OVB) problem \citep{angrist2009mostly, chernozhukov2022ovb}. Within the Many-Facet Rasch Model (MFRM) framework \citep{linacre1989mfrm}, the complete data-generating process includes both judge severity $d_j$ and a contamination interaction $c_n \cdot e_i$. Fitting a specification that omits the contamination term produces biased parameter estimates: the omission of $c_n \cdot e_i$ induces a specification bias that persists regardless of confounding structure, with an additional directional component when judge severity and contamination are non-orthogonal. The OVB framework predicts that the bias magnitude scales with the contamination susceptibility $c_n$ of each model, so the most contaminated models receive the largest upward distortion in estimated ability. For practical benchmark evaluations, this means that the more a model's training data overlaps with the benchmark, the more its ability is overestimated, precisely the failure mode that contamination correction is designed to prevent. Synthetic validation confirms the predicted pattern: the Pearson correlation between sequential estimation bias and true $c_n$ reaches $r = 0.86$ ($p < 0.001$), which shows that contaminated models are systematically overestimated under both sequential orderings (Section~\ref{sec:confounding}).
9	
10	We propose the Gated Many-Facet Rasch Model (G-MFRM), which combines the multi-facet structure of MFRM \citep{linacre1989mfrm, jiao2025mfrm_llm} with the gating mechanism of Doubly-Gated Item Response Theory (DG-IRT) \citep{shu2013dgirt} to jointly estimate model ability, judge severity, and contamination susceptibility in a single measurement framework. G-MFRM extends the MFRM linear predictor with a multiplicative contamination gating term $c_n \cdot e_i$, where $c_n \geq 0$ captures model-specific contamination susceptibility and $e_i \in [0,1]$ quantifies per-item exposure. When $c_n = 0$ or $e_i = 0$, the gating term vanishes and the model reduces to standard MFRM, so uncontaminated model-item pairs incur no distortion. Because the bilinear product $c_n \cdot e_i$ cannot be uniquely decomposed from response data alone, G-MFRM employs a three-stage calibration procedure: (1) standard MFRM warm-start to obtain initial parameter estimates, (2) external per-item exposure estimation from evidence independent of the response data, and (3) joint Markov chain Monte Carlo (MCMC) sampling with $e_i$ fixed from Stage~2. We provide a formal identifiability analysis (Propositions~\ref{prop:no_new}--\ref{prop:exposure_variation} and Theorem~\ref{thm:sufficient}) that proves fixing $e_i$ externally is both necessary and sufficient for parameter separation under standard multi-judge designs (Section~\ref{sec:method}). A complementary error propagation analysis bounds the impact of Stage~2 measurement noise: when exposure estimation error satisfies $\sigma \leq 0.2$, ability RMSE degradation remains below 6\%. Figure~\ref{fig:framework} provides an overview of the complete framework.
11	
12	We begin by formalizing the confounding between judge severity and benchmark contamination as omitted variable bias within the MFRM framework (\S\ref{sec:confounding}, Figure~\ref{fig:ovb_bias}), motivating the joint calibration approach. Our contributions are:
13	\begin{enumerate}
14	    \item We propose the G-MFRM framework with formal identifiability guarantees (Propositions~\ref{prop:no_new}--\ref{prop:exposure_variation} and Theorem~\ref{thm:sufficient}) and quantified error propagation bounds for the staged estimation procedure (Section~\ref{sec:method}, Table~\ref{tab:error_prop}).
15	    \item Synthetic validation confirms that joint estimation reduces ability RMSE by 51.2\% relative to sequential estimation ($p < 0.001$), with Kendall rank correlation $\tau = 0.922$ versus $\tau = 0.839$ (Section~\ref{sec:experiments}).
16	    \item On Arena-Hard with 9 LLM judges and 8 target models, G-MFRM produces the first joint diagnostic of per-model contamination susceptibility and per-judge severity within a measurement-theoretic framework, with nominally improved rank agreement ($\tau = 0.857$ vs.\ $0.786$ for all seven baselines; Section~\ref{sec:experiments}).
17	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "a74815e6-a706-4e16-b269-93a9aedbb232",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLarge Language Model (LLM) evaluation increasingly relies on LLM-as-a-judge protocols, where one or more LLM judges score model responses on structured benchmarks \\citep{zheng2023mtbench}. Two well-documented sources of distortion affect these evaluations: \\emph{judge bias}, where different judges assign systematically different scores to the same response, and \\emph{benchmark contamination}, where models achieve inflated scores on items encountered during training. Both problems have received sustained research attention, producing separate toolkits for bias calibration and contamination detection. These toolkits treat the two distortions as independent phenomena, a separation that reflects their origins in different research communities rather than any principled argument for independence. Accurate ability ranking is essential for model selection, safety evaluation, and benchmark design; systematic distortion in estimated abilities undermines all three. Yet a practitioner who needs both corrections must apply them sequentially: first correct one source of distortion, then the other. This sequential approach produces unreliable ability estimates. In synthetic experiments with 50 models, 100 items, and 8 judges, sequential estimation yields ability root mean squared error (RMSE) of $0.254 \\pm 0.045$, while joint estimation achieves $0.124 \\pm 0.016$, a 51.2\\% reduction (Wilcoxon $p < 0.001$). The gap does not arise from estimation noise or algorithmic limitations of individual methods; it reflects structural confounding between judge bias and contamination that no sequential pipeline can resolve.\n\nExisting methods address these distortions in isolation. Judge bias corrections---CyclicJudge \\citep{cyclicjudge2026}, UDA \\citep{uda2026}---remove systematic inter-judge differences without modeling contamination. Contamination detection tools---ConStat \\citep{constat2024}, DCR \\citep{dcr2025}, LogProber \\citep{logprober2024}---adjust for memorization without accounting for judge effects (see Section~\\ref{sec:related_work} for detailed review). A bias-first pipeline absorbs contamination-induced score inflation into ability estimates, because the bias model attributes all residual systematic variation to genuine ability. A contamination-first pipeline misattributes judge severity differences as contamination, because score elevation from a lenient judge is indistinguishable from elevation due to memorization without a joint model. In either ordering, the first correction stage produces estimates distorted by the unmodeled facet, and the second stage inherits this distortion.\n\nWe formalize this confounding as an omitted variable bias (OVB) problem \\citep{angrist2009mostly, chernozhukov2022ovb}. Within the Many-Facet Rasch Model (MFRM) framework \\citep{linacre1989mfrm}, the complete data-generating process includes both judge severity $d_j$ and a contamination interaction $c_n \\cdot e_i$. Fitting a specification that omits the contamination term produces biased parameter estimates: the omission of $c_n \\cdot e_i$ induces a specification bias that persists regardless of confounding structure, with an additional directional component when judge severity and contamination are non-orthogonal. The OVB framework predicts that the bias magnitude scales with the contamination susceptibility $c_n$ of each model, so the most contaminated models receive the largest upward distortion in estimated ability. For practical benchmark evaluations, this means that the more a model's training data overlaps with the benchmark, the more its ability is overestimated, precisely the failure mode that contamination correction is designed to prevent. Synthetic validation confirms the predicted pattern: the Pearson correlation between sequential estimation bias and true $c_n$ reaches $r = 0.86$ ($p < 0.001$), which shows that contaminated models are systematically overestimated under both sequential orderings (Section~\\ref{sec:confounding}).\n\nWe propose the Gated Many-Facet Rasch Model (G-MFRM), which combines the multi-facet structure of MFRM \\citep{linacre1989mfrm, jiao2025mfrm_llm} with the gating mechanism of Doubly-Gated Item Response Theory (DG-IRT) \\citep{shu2013dgirt} to jointly estimate model ability, judge severity, and contamination susceptibility in a single measurement framework. G-MFRM extends the MFRM linear predictor with a multiplicative contamination gating term $c_n \\cdot e_i$, where $c_n \\geq 0$ captures model-specific contamination susceptibility and $e_i \\in [0,1]$ quantifies per-item exposure. When $c_n = 0$ or $e_i = 0$, the gating term vanishes and the model reduces to standard MFRM, so uncontaminated model-item pairs incur no distortion. Because the bilinear product $c_n \\cdot e_i$ cannot be uniquely decomposed from response data alone, G-MFRM employs a three-stage calibration procedure: (1) standard MFRM warm-start to obtain initial parameter estimates, (2) external per-item exposure estimation from evidence independent of the response data, and (3) joint Markov chain Monte Carlo (MCMC) sampling with $e_i$ fixed from Stage~2. We provide a formal identifiability analysis (Propositions~\\ref{prop:no_new}--\\ref{prop:exposure_variation} and Theorem~\\ref{thm:sufficient}) that proves fixing $e_i$ externally is both necessary and sufficient for parameter separation under standard multi-judge designs (Section~\\ref{sec:method}). A complementary error propagation analysis bounds the impact of Stage~2 measurement noise: when exposure estimation error satisfies $\\sigma \\leq 0.2$, ability RMSE degradation remains below 6\\%. Figure~\\ref{fig:framework} provides an overview of the complete framework.\n\nWe begin by formalizing the confounding between judge severity and benchmark contamination as omitted variable bias within the MFRM framework (\\S\\ref{sec:confounding}, Figure~\\ref{fig:ovb_bias}), motivating the joint calibration approach. Our contributions are:\n\\begin{enumerate}\n    \\item We propose the G-MFRM framework with formal identifiability guarantees (Propositions~\\ref{prop:no_new}--\\ref{prop:exposure_variation} and Theorem~\\ref{thm:sufficient}) and quantified error propagation bounds for the staged estimation procedure (Section~\\ref{sec:method}, Table~\\ref{tab:error_prop}).\n    \\item Synthetic validation confirms that joint estimation reduces ability RMSE by 51.2\\% relative to sequential estimation ($p < 0.001$), with Kendall rank correlation $\\tau = 0.922$ versus $\\tau = 0.839$ (Section~\\ref{sec:experiments}).\n    \\item On Arena-Hard with 9 LLM judges and 8 target models, G-MFRM produces the first joint diagnostic of per-model contamination susceptibility and per-judge severity within a measurement-theoretic framework, with nominally improved rank agreement ($\\tau = 0.857$ vs.\\ $0.786$ for all seven baselines; Section~\\ref{sec:experiments}).\n\\end{enumerate}",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Now I have the content of all three files. Let me search for hardcoded "Figure 1" or "Figure 2" references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "f67821b8-f25e-4732-b174-c3581df1c299",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KwoEActUSwLGNCBjs4QFf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8342,
      "cache_read_input_tokens": 24159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8342
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

_source line 13_

检查硬编码的 Figure 引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "dfe066ca-9df1-4d6c-bf80-6012b9225a91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KwoEActUSwLGNCBjs4QFf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8342,
      "cache_read_input_tokens": 24159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8342
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

_source line 14_

<details open><summary>🔧 Tool call — Grep · `toolu_01BtuKhVAPb4BNAt4vX6q5Qs`</summary>

```json
{
  "pattern": "Figure 1|Figure 2|Fig\\.~1|Fig\\.~2|Fig\\. 1|Fig\\. 2",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "7c440008-728d-4d43-92c2-c69b97c740c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KwoEActUSwLGNCBjs4QFf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8342,
      "cache_read_input_tokens": 24159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8342
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

_source line 15 · 2026-05-24T16:59:24.211Z_

<details><summary>↩ Tool result · `toolu_01BtuKhVAPb4BNAt4vX6q5Qs`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "9516a2b4-8b75-4248-8dec-5c8c09fdf12f",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
No hardcoded Figure 1/Figure 2 references. Now I need to:

1. Cut the `\begin{figure*}[t]...\end{figure*}` block from `method.tex` (lines 6-11)
2. Paste it into `background.tex` before the `\begin{figure}[t]` block for `fig:ovb_bias` (before line 38)

Let me do both edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "caab2053-4394-47b9-b643-eecb81136ad2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVsu1WWyteABdxtiBg3HRm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 237,
      "cache_read_input_tokens": 32501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 237
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

_source line 17_

没有硬编码的 Figure 引用，全部用的 `\ref`。现在执行移动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "82188900-f9e0-45bc-a9f9-2702b5cf7844",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVsu1WWyteABdxtiBg3HRm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 237,
      "cache_read_input_tokens": 32501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 237
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

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_015vjwDFssqt9RdwRPV2jG98`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
  "old_string": "\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_framework_v2}\n\\caption{(a)~Sequential pipelines address judge bias and contamination independently; omitted variable bias confounds the unmodeled facet into ability estimates. (b)~G-MFRM three-stage joint calibration: Stage~1 fits a standard MFRM for initial estimates $(\\hat{\\theta}, \\hat{b}, \\hat{d})$; Stage~2 estimates per-item exposure $e_i$ from external evidence (reference model anchoring, cross-model agreement, and optionally LogProber); Stage~3 performs joint MCMC inference with $e_i$ fixed, recovering contamination-corrected ability $\\tilde{\\theta}_n$, contamination susceptibility $c_n$, and judge severity $d_j$.}\n\\label{fig:framework}\n\\end{figure*}\n\n\\subsection{Model Specification}",
  "new_string": "\\subsection{Model Specification}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "cd50215f-850c-49f3-989f-b09aad9fdab9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVsu1WWyteABdxtiBg3HRm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 237,
      "cache_read_input_tokens": 32501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 237
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

_source line 19 · 2026-05-24T16:59:40.386Z_

<details><summary>↩ Tool result · `toolu_015vjwDFssqt9RdwRPV2jG98`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "697be47b-62e7-4333-81ad-7f1959f4d98c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
    "oldString": "\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_framework_v2}\n\\caption{(a)~Sequential pipelines address judge bias and contamination independently; omitted variable bias confounds the unmodeled facet into ability estimates. (b)~G-MFRM three-stage joint calibration: Stage~1 fits a standard MFRM for initial estimates $(\\hat{\\theta}, \\hat{b}, \\hat{d})$; Stage~2 estimates per-item exposure $e_i$ from external evidence (reference model anchoring, cross-model agreement, and optionally LogProber); Stage~3 performs joint MCMC inference with $e_i$ fixed, recovering contamination-corrected ability $\\tilde{\\theta}_n$, contamination susceptibility $c_n$, and judge severity $d_j$.}\n\\label{fig:framework}\n\\end{figure*}\n\n\\subsection{Model Specification}",
    "newString": "\\subsection{Model Specification}",
    "originalFile": "\\section{The G-MFRM Framework}\n\\label{sec:method}\n\nSection~\\ref{sec:confounding} established that omitting contamination from the measurement model produces directional bias in ability estimates (Observation~\\ref{obs:ovb}). We now introduce the Gated Many-Facet Rasch Model (G-MFRM), which jointly estimates ability, judge severity, and contamination susceptibility within a single measurement framework. The key design choices, staged estimation with externally fixed exposure and a hierarchical HalfNormal prior for the contamination term, are motivated by the identifiability analysis in \\S\\ref{sec:identifiability} and the error propagation bounds in \\S\\ref{sec:error_prop}.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_framework_v2}\n\\caption{(a)~Sequential pipelines address judge bias and contamination independently; omitted variable bias confounds the unmodeled facet into ability estimates. (b)~G-MFRM three-stage joint calibration: Stage~1 fits a standard MFRM for initial estimates $(\\hat{\\theta}, \\hat{b}, \\hat{d})$; Stage~2 estimates per-item exposure $e_i$ from external evidence (reference model anchoring, cross-model agreement, and optionally LogProber); Stage~3 performs joint MCMC inference with $e_i$ fixed, recovering contamination-corrected ability $\\tilde{\\theta}_n$, contamination susceptibility $c_n$, and judge severity $d_j$.}\n\\label{fig:framework}\n\\end{figure*}\n\n\\subsection{Model Specification}\n\\label{sec:model_spec}\n\nG-MFRM extends the standard MFRM \\citep{linacre1989mfrm, linacre1994mfrm} by adding a multiplicative contamination gating term to the linear predictor (Eq.~\\ref{eq:mfrm}):\n%\n\\begin{equation}\n\\label{eq:gmfrm}\n\\log \\frac{P(Y_{nij} \\geq k)}{P(Y_{nij} < k)} = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i,\n\\end{equation}\n%\nwhere all terms carry the definitions from Section~\\ref{sec:confounding}. The gating structure $c_n \\cdot e_i$ separates the model-specific and item-specific components of contamination: $c_n \\geq 0$ captures how much model $n$ benefits from memorized benchmark content, while $e_i \\in [0,1]$ quantifies how much of item $i$ has leaked into training corpora. When $c_n = 0$ (a clean model) or $e_i = 0$ (a novel item), the gating term vanishes and Eq.~\\ref{eq:gmfrm} reduces to the standard MFRM. This graceful degradation ensures that G-MFRM imposes no distortion on uncontaminated model-item pairs.\n\nWe enforce non-negativity and sparsity of $c_n$ through a hierarchical HalfNormal prior. A global shrinkage scale $\\sigma_c \\sim \\text{HalfNormal}(1.0)$ controls the overall contamination level, and per-model raw effects $c^{\\mathrm{raw}}_n \\sim \\text{HalfNormal}(1.0)$ are scaled to obtain $c_n = c^{\\mathrm{raw}}_n \\cdot \\sigma_c$. The HalfNormal support restricts $c_n \\geq 0$, and the hierarchical structure provides adaptive shrinkage: when the data support low overall contamination, $\\sigma_c$ contracts toward zero, pulling all $c_n$ values down. Models with genuine contamination retain large $c^{\\mathrm{raw}}_n$ relative to the group. The remaining priors are $\\theta_n \\sim \\mathcal{N}(0, 1)$, $b_i \\sim \\mathcal{N}(0, 1)$, $d_j \\sim \\mathcal{N}(0, 0.5)$, and standard uniform on thresholds $\\tau_k$.\n\nThe closest antecedent is the Doubly-Gated IRT model of \\citet{shu2013dgirt}, which introduced binary gating for item preknowledge in educational testing. Beyond extending DG-IRT to continuous exposure and multi-rater designs, G-MFRM's primary methodological contributions are analytical: the identifiability analysis (Propositions~\\ref{prop:no_new}--\\ref{prop:exposure_variation} and Theorem~\\ref{thm:sufficient}) provides the first formal conditions under which gated IRT parameters are separable, and the Murphy--Topel error propagation framework (\\S\\ref{sec:error_prop}) quantifies how staged estimation uncertainty propagates to downstream parameter estimates---neither of which exists for DG-IRT or any prior gated measurement model.\n\n\\subsection{Staged Estimation}\n\\label{sec:staged}\n\nJoint estimation of all parameters in Eq.~\\ref{eq:gmfrm}, including $e_i$, would require identifying the bilinear product $c_n \\cdot e_i$ from response data alone. This creates a fundamental non-identifiability (Proposition~\\ref{prop:exposure_variation}). We resolve this through a three-stage procedure that fixes exposure externally before estimating the contamination parameters.\n\n\\paragraph{Stage 1: Standard MFRM.} We fit the standard MFRM (Eq.~\\ref{eq:mfrm}) via MCMC (NUTS) to obtain initial estimates $(\\hat{\\theta}, \\hat{b}, \\hat{d})$. These serve as warm-start values for the sampler in Stage~3 and improve convergence.\n\n\\paragraph{Stage 2: Exposure estimation.} Per-item exposure $e_i$ is estimated from external evidence independent of the response data used in Stages~1 and~3. The primary signal is \\emph{reference model anchoring}: using a fixed reference model (e.g., gpt-4-0314) as anchor, we compute win-rate residuals for each target model against difficulty-adjusted expectations; items where target models systematically outperform the anchor beyond what difficulty predicts are flagged as potentially exposed. The secondary signal is \\emph{cross-model agreement}: items receiving uniformly high scores across architecturally diverse models suggest exposure rather than genuine easiness, quantified via $z$-score standardization of the inter-model agreement distribution. These signals are combined as a weighted composite (75\\% anchoring, 25\\% agreement), clipped to $[0, 1]$, and treated as fixed in Stage~3. Where model log-probabilities are accessible, LogProber can provide an additional gray-box memorization signal, though it is not used in our current experiments.\n\n\\paragraph{Non-circularity.} Exposure estimation is not circular: $e_i$ is item-level (content leakage) while $c_n$ is model-level (susceptibility), testing a cross-level interaction. The primary signal (75\\%) derives from reference anchoring independent of target models, and ablation with 100\\% anchoring yields $\\rho = 0.998$ (Appendix~\\ref{app:weight_robustness}), confirming $e_i$ is robust to removing the cross-model component.\n\n\\paragraph{Stage 3: Joint MCMC.} With $e_i$ fixed, we sample $(\\theta_n, b_i, d_j, c_n)$ jointly via NUTS \\citep{betancourt2015}. The priors are as specified in \\S\\ref{sec:model_spec}. The hierarchical contamination prior decomposes as\n%\n\\begin{align}\n\\label{eq:contam_prior}\n\\sigma_c &\\sim \\text{HalfNormal}(1.0), \\quad c^{\\mathrm{raw}}_n \\sim \\text{HalfNormal}(1.0), \\nonumber \\\\\nc_n &= c^{\\mathrm{raw}}_n \\cdot \\sigma_c,\n\\end{align}\n%\nwhere $\\sigma_c$ is a shared global scale that governs the overall contamination magnitude. This non-centered parameterization improves sampler geometry by decoupling the global scale from the per-model effects.\n\nConvergence is assessed via rank-normalized split-$\\hat{R}$ \\citep{vehtari2021rhat} and bulk effective sample size (ESS), with thresholds $\\hat{R} < 1.05$ and ESS$_{\\mathrm{bulk}} > 100$ following standard practice \\citep{gelman2013bda}.\\footnote{Synthetic validation with $N = 50$, $I = 100$, $J = 8$ yields satisfactory convergence across all parameters (exp-012). Full diagnostic tables are reported in Section~\\ref{sec:experiments}.}\n\n\n\\subsection{Identifiability}\n\\label{sec:identifiability}\n\nAdding a multiplicative term to a measurement model raises the question of whether the new parameters can be separated from the existing ones. We establish that fixing $e_i$ externally is both necessary and sufficient for identification. All proofs assume the standard location constraint $\\sum_n \\theta_n = 0$.\n\n\\begin{proposition}[No New Indeterminacy]\n\\label{prop:no_new}\nWhen $e_i$ is fixed externally, the gating term $c_n \\cdot e_i$ introduces no additional location or scale indeterminacy beyond that already present in the standard MFRM.\n\\end{proposition}\n\n\\begin{proof}\nSuppose $c_n' = c_n + \\delta$ preserves all response probabilities. Then $\\delta \\cdot e_i = 0$ for all items. Since $e_i \\neq 0$ for at least one item by assumption, $\\delta = 0$. The key observation is that fixing $e_i$ externally eliminates the bilinear ambiguity $c_n \\cdot e_i = (\\lambda c_n)(\\lambda^{-1} e_i)$ that would otherwise render the decomposition non-unique.\n\\end{proof}\n\n\\begin{proposition}[Exposure Variation Necessary]\n\\label{prop:exposure_variation}\nIf $e_i = e$ for all $i$ (constant exposure), then $c_n$ and $\\theta_n$ are not separately identifiable.\n\\end{proposition}\n\n\\begin{proof}\nWhen exposure is constant, the linear predictor becomes $(\\theta_n + c_n \\cdot e) - b_i - d_j - \\tau_k$, which is equivalent to a standard MFRM with reparameterized ability $\\theta^*_n = \\theta_n + c_n \\cdot e$. No configuration of response data can distinguish $(\\theta_n, c_n)$ from $(\\theta_n + \\epsilon, c_n - \\epsilon/e)$ for any $\\epsilon$.\n\\end{proof}\n\n\\begin{corollary}\n$\\mathrm{Var}(e_i) > 0$ is a necessary condition for identifiability of $c_n$.\n\\end{corollary}\n\n\\begin{theorem}[Sufficient Conditions for Local Identifiability]\n\\label{thm:sufficient}\nThe G-MFRM is locally identifiable, up to the standard location constraint, if the following conditions hold: (i) a connected observation design (each item is observed by at least one model--judge pair), (ii) $J \\geq 2$ judges, (iii) for each model $n$, the set of observed items spans at least two distinct exposure values ($\\mathrm{Var}(e_i) > 0$ over observed items), and (iv) standard normalization $\\sum_n \\theta_n = 0$.\n\\end{theorem}\n\nThe proof, given in Appendix~\\ref{app:proof}, follows \\citet{rothenberg1971}: non-singularity of the Fisher information matrix is established via the Cauchy--Schwarz inequality on the $(\\theta_n, c_n)$ submatrix determinant and a Schur complement argument for the remaining blocks. Conditions~(i) and~(ii) are standard multi-rater design requirements, satisfied by the connected design in our evaluation (XX.X\\% fill rate; \\S\\ref{sec:setup}); condition~(iii) is the substantive constraint that each model's observed items include varying exposure levels.\n\n\\subsection{Error Propagation}\n\\label{sec:error_prop}\n\nThe staged procedure treats the Stage~2 exposure estimates $\\hat{e}_i$ as fixed quantities in Stage~3. This is a generated regressors problem \\citep{pagan1984}: measurement error in $\\hat{e}_i$ propagates into the posterior of $(\\theta_n, c_n)$. The multiplicative structure $c_n \\cdot e_i$ makes this an errors-in-variables (EIV) problem \\citep{fuller1987}, with a predictable attenuation pattern.\n\nLet $\\hat{e}_i = e_i + \\epsilon_i$ with $\\epsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$ independent of all model parameters. The attenuation factor for the contamination coefficient is\n%\n\\begin{equation}\n\\label{eq:attenuation}\n\\lambda(\\sigma) = \\frac{\\mathrm{Var}(e_i)}{\\mathrm{Var}(e_i) + \\sigma^2},\n\\end{equation}\n%\nso attenuation reaches 50\\% when $\\sigma = \\sqrt{\\mathrm{Var}(e_i)}$. In the synthetic DGP ($\\mathrm{Var}(e_i) \\approx 0.04$), this corresponds to $\\sigma \\approx 0.2$.\\footnote{The attenuation formula assumes that $\\epsilon_i$ is independent of all model parameters, identically distributed, and Gaussian. In practice, exposure estimation errors may be correlated across items sharing the same source or heteroscedastic across difficulty levels. Table~\\ref{tab:error_prop} provides empirical validation that $\\hat{\\theta}$ estimates remain robust under such departures (Section~\\ref{sec:experiments}).}\n\nTable~\\ref{tab:error_prop} shows the empirical degradation across noise levels (see also Figure~\\ref{fig:error_prop} in the Appendix). Below the critical threshold ($\\sigma \\leq 0.2$), degradation is mild: $\\theta$-RMSE increases by 5.9\\% (from $0.128 \\pm 0.018$ to $0.135 \\pm 0.018$) and $c_n$-RMSE by 7.9\\% (from $0.533 \\pm 0.187$ to $0.575 \\pm 0.198$). At $\\sigma = 0.1$, the increases are only 1.4\\% and 2.3\\% respectively. Beyond the threshold ($\\sigma = 0.5$), degradation becomes severe: $\\theta$-RMSE rises 36.9\\% and $c_n$-RMSE rises 57.9\\%. Contamination estimates $c_n$ are more sensitive than ability estimates $\\theta_n$ because $c_n$ enters the likelihood only through its product with $e_i$ (multiplicative coupling), while $\\theta_n$ contributes additively and is anchored by all observations regardless of exposure.\n\nThese bounds make the staged approximation falsifiable: if the noise level of the Stage~2 exposure estimates can be bounded below $\\sigma_{\\mathrm{crit}}$, the resulting ability estimates carry quantifiable error guarantees. For honest credible intervals that account for generated-regressor uncertainty, we apply the Murphy-Topel variance correction \\citep{murphy1985} to inflate the Stage~3 posterior variance by the estimated Stage~2 sampling variability (Appendix~\\ref{app:murphy_topel}).\n\n\\subsection{Fair Scores and Diagnostics}\n\\label{sec:fair_scores}\n\nThe Stage~3 posterior mean of $\\theta_n$ provides a bias-and-contamination-corrected ``fair score'' for each model. The remaining parameters serve complementary diagnostic roles: per-model $c_n$ flags candidates for training data audit, per-judge $d_j$ informs judge calibration, and per-item $e_i$ identifies items for retirement or replacement.",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 13,
        "newStart": 3,
        "newLines": 6,
        "lines": [
          " ",
          " Section~\\ref{sec:confounding} established that omitting contamination from the measurement model produces directional bias in ability estimates (Observation~\\ref{obs:ovb}). We now introduce the Gated Many-Facet Rasch Model (G-MFRM), which jointly estimates ability, judge severity, and contamination susceptibility within a single measurement framework. The key design choices, staged estimation with externally fixed exposure and a hierarchical HalfNormal prior for the contamination term, are motivated by the identifiability analysis in \\S\\ref{sec:identifiability} and the error propagation bounds in \\S\\ref{sec:error_prop}.",
          " ",
          "-\\begin{figure*}[t]",
          "-\\centering",
          "-\\includegraphics[width=\\textwidth]{fig1_framework_v2}",
          "-\\caption{(a)~Sequential pipelines address judge bias and contamination independently; omitted variable bias confounds the unmodeled facet into ability estimates. (b)~G-MFRM three-stage joint calibration: Stage~1 fits a standard MFRM for initial estimates $(\\hat{\\theta}, \\hat{b}, \\hat{d})$; Stage~2 estimates per-item exposure $e_i$ from external evidence (reference model anchoring, cross-model agreement, and optionally LogProber); Stage~3 performs joint MCMC inference with $e_i$ fixed, recovering contamination-corrected ability $\\tilde{\\theta}_n$, contamination susceptibility $c_n$, and judge severity $d_j$.}",
          "-\\label{fig:framework}",
          "-\\end{figure*}",
          "-",
          " \\subsection{Model Specification}",
          " \\label{sec:model_spec}",
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

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_01D8iJK7bBUiQ81e9Li4QdrT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex",
  "old_string": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_ovb_bias}",
  "new_string": "\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_framework_v2}\n\\caption{(a)~Sequential pipelines address judge bias and contamination independently; omitted variable bias confounds the unmodeled facet into ability estimates. (b)~G-MFRM three-stage joint calibration: Stage~1 fits a standard MFRM for initial estimates $(\\hat{\\theta}, \\hat{b}, \\hat{d})$; Stage~2 estimates per-item exposure $e_i$ from external evidence (reference model anchoring, cross-model agreement, and optionally LogProber); Stage~3 performs joint MCMC inference with $e_i$ fixed, recovering contamination-corrected ability $\\tilde{\\theta}_n$, contamination susceptibility $c_n$, and judge severity $d_j$.}\n\\label{fig:framework}\n\\end{figure*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_ovb_bias}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "25fe3942-d38f-4565-9012-81fdc6cd2411",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVsu1WWyteABdxtiBg3HRm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 237,
      "cache_read_input_tokens": 32501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 237
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

_source line 21 · 2026-05-24T16:59:43.413Z_

<details><summary>↩ Tool result · `toolu_01D8iJK7bBUiQ81e9Li4QdrT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "32dabd6d-595d-4c6d-a921-a35babaf7529",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex",
    "oldString": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_ovb_bias}",
    "newString": "\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_framework_v2}\n\\caption{(a)~Sequential pipelines address judge bias and contamination independently; omitted variable bias confounds the unmodeled facet into ability estimates. (b)~G-MFRM three-stage joint calibration: Stage~1 fits a standard MFRM for initial estimates $(\\hat{\\theta}, \\hat{b}, \\hat{d})$; Stage~2 estimates per-item exposure $e_i$ from external evidence (reference model anchoring, cross-model agreement, and optionally LogProber); Stage~3 performs joint MCMC inference with $e_i$ fixed, recovering contamination-corrected ability $\\tilde{\\theta}_n$, contamination susceptibility $c_n$, and judge severity $d_j$.}\n\\label{fig:framework}\n\\end{figure*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_ovb_bias}",
    "originalFile": "\\section{Confounding in LLM Evaluation}\n\\label{sec:confounding}\n\nThe Many-Facet Rasch Model (MFRM) extends classical Rasch measurement to settings with multiple rater facets \\citep{linacre1989mfrm, linacre1994mfrm}. Originating in educational measurement, the model treats rater variation as a nuisance facet to be estimated and removed rather than a source of noise to be averaged over. In the LLM evaluation context, where $J$ judges score $N$ models across $I$ items, the MFRM specifies\n%\n\\begin{equation}\n\\label{eq:mfrm}\n\\log \\frac{P(Y_{nij} \\geq k \\mid \\theta_n, b_i, d_j, \\tau_k)}{P(Y_{nij} < k \\mid \\theta_n, b_i, d_j, \\tau_k)} = \\theta_n - b_i - d_j - \\tau_k,\n\\end{equation}\n%\nwhere $Y_{nij}$ is the ordinal rating by judge $j$ for model $n$ on item $i$, $\\theta_n$ is the ability of model $n$ ($n = 1, \\ldots, N$), $b_i$ is the difficulty of item $i$ ($i = 1, \\ldots, I$), $d_j$ is the severity of judge $j$ ($j = 1, \\ldots, J$), and $\\tau_k$ is the threshold for category $k$. All facets reside on a common logit scale, so model ability is directly comparable after adjustment for item difficulty and judge severity. \\citet{jiao2025mfrm_llm} applied this framework to compare ten LLM raters with human experts, showing that MFRM separates genuine ability from systematic judge effects in multi-judge panels.\n\nHowever, standard MFRM assumes that all systematic sources of score variation are captured by the modeled facets. This assumption breaks down when some models have been exposed to benchmark items during training \\citep{dcr2025}. Such contamination inflates scores on exposed items through memorization rather than genuine ability. We represent this effect as an interaction $c_n \\cdot e_i$, where $c_n \\geq 0$ is the contamination susceptibility of model $n$ and $e_i \\in [0, 1]$ is the exposure level of item $i$. The complete data-generating process becomes\n%\n\\begin{equation}\n\\label{eq:full}\n\\eta_{nijk} = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i.\n\\end{equation}\n%\nWhen a practitioner fits the standard MFRM (Eq.~\\ref{eq:mfrm}) to data generated by Eq.~\\ref{eq:full}, the contamination term is absent from the estimated model. Its influence does not vanish but is absorbed into the estimated parameters $\\tilde{\\theta}_n$, $\\tilde{b}_i$, and $\\tilde{d}_j$, which distorts all downstream inferences.\n\nThe consequence of this omission can be stated precisely.\n\n\\begin{observation}[Omitted Variable Bias in MFRM]\n\\label{obs:ovb}\nLet the full model be $\\eta_{nijk} = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$ and the short model omit the contamination term: $\\tilde{\\eta}_{nijk} = \\tilde{\\theta}_n - \\tilde{b}_i - \\tilde{d}_j - \\tau_k$. Under a linear approximation to the ordinal logit link \\citep{wooldridge2010, angrist2009mostly},\\footnote{The OVB formula is exact for linear models. We apply it to the MFRM linear predictor $\\eta$, which is an approximation. Synthetic validation confirms the approximation quality: the Pearson correlation between the predicted bias direction and empirical bias reaches $r = 0.86$ ($p < 0.001$), indicating that the linear result accurately characterizes bias direction and relative magnitude.}\n\\begin{equation}\n\\label{eq:ovb}\n\\mathrm{plim}(\\tilde{\\theta}_n - \\theta_n) = \\gamma_n \\cdot c_n,\n\\end{equation}\nwhere $\\gamma_n$ depends on the projection of the exposure vector $(e_i)$ onto the design matrix of the short model (explicit form in Appendix~\\ref{app:gamma}). The bias is non-zero whenever $\\mathrm{Cov}(d_j,\\, c_n \\cdot e_i) \\neq 0$. This captures the confounding component; in the nonlinear MFRM, a specification bias from omitting $c_n \\cdot e_i$ persists even at zero covariance (Section~\\ref{sec:experiments}).\n\\end{observation}\n\nThe linear approximation in Observation~\\ref{obs:ovb} ($r = 0.86$) serves solely as directional motivation for the bias structure; G-MFRM's Stage~3 inference (Eq.~\\ref{eq:gmfrm}) uses the full nonlinear ordinal logistic likelihood and does not depend on this approximation. The bias combines a specification component from omitting $c_n \\cdot e_i$, which persists regardless of confounding, with a confounding component from non-orthogonality between $d_j$ and $c_n \\cdot e_i$. Monte Carlo simulation confirms that bias magnitude is approximately constant across confounding levels $\\rho \\in \\{0, 0.3, 0.6, 0.9\\}$, indicating that the omission of $c_n \\cdot e_i$---not its correlation with $d_j$---is the primary driver (Figure~\\ref{fig:bias_vs_rho}).\n\nThis confounding undermines both sequential estimation strategies. A bias-first approach, as in CyclicJudge \\citep{cyclicjudge2026}, calibrates $d_j$ before estimating ability, but the resulting $\\hat{\\theta}$ is already inflated for contaminated models because the omitted $c_n \\cdot e_i$ term has been absorbed into the ability estimates. A contamination-first approach, as in DCR \\citep{dcr2025}, adjusts for contamination before addressing judge effects, but judge severity is then misattributed as contamination signal. Synthetic validation confirms this failure: with $N = 50$ models, $I = 100$ items, $J = 8$ judges, and 20 random seeds, the Pearson correlation between sequential estimation bias and true $c_n$ reaches $r = 0.86$ ($p < 0.001$). As illustrated in Figure~\\ref{fig:ovb_bias}, the bias is not random but directional: contaminated models are systematically overestimated under both sequential orderings.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_ovb_bias}\n\\caption{Sequential estimation bias ($\\hat{\\theta}_{\\mathrm{seq}} - \\theta_{\\mathrm{true}}$) versus true contamination susceptibility $c_n$. Pearson $r = 0.86$ ($p < 0.001$) confirms systematic overestimation of contaminated models. Synthetic data ($N = 50$, $I = 100$, $J = 8$, 20 seeds).}\n\\label{fig:ovb_bias}\n\\end{figure}",
    "structuredPatch": [
      {
        "oldStart": 35,
        "oldLines": 6,
        "newStart": 35,
        "newLines": 13,
        "lines": [
          " ",
          " This confounding undermines both sequential estimation strategies. A bias-first approach, as in CyclicJudge \\citep{cyclicjudge2026}, calibrates $d_j$ before estimating ability, but the resulting $\\hat{\\theta}$ is already inflated for contaminated models because the omitted $c_n \\cdot e_i$ term has been absorbed into the ability estimates. A contamination-first approach, as in DCR \\citep{dcr2025}, adjusts for contamination before addressing judge effects, but judge severity is then misattributed as contamination signal. Synthetic validation confirms this failure: with $N = 50$ models, $I = 100$ items, $J = 8$ judges, and 20 random seeds, the Pearson correlation between sequential estimation bias and true $c_n$ reaches $r = 0.86$ ($p < 0.001$). As illustrated in Figure~\\ref{fig:ovb_bias}, the bias is not random but directional: contaminated models are systematically overestimated under both sequential orderings.",
          " ",
          "+\\begin{figure*}[t]",
          "+\\centering",
          "+\\includegraphics[width=\\textwidth]{fig1_framework_v2}",
          "+\\caption{(a)~Sequential pipelines address judge bias and contamination independently; omitted variable bias confounds the unmodeled facet into ability estimates. (b)~G-MFRM three-stage joint calibration: Stage~1 fits a standard MFRM for initial estimates $(\\hat{\\theta}, \\hat{b}, \\hat{d})$; Stage~2 estimates per-item exposure $e_i$ from external evidence (reference model anchoring, cross-model agreement, and optionally LogProber); Stage~3 performs joint MCMC inference with $e_i$ fixed, recovering contamination-corrected ability $\\tilde{\\theta}_n$, contamination susceptibility $c_n$, and judge severity $d_j$.}",
          "+\\label{fig:framework}",
          "+\\end{figure*}",
          "+",
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=\\columnwidth]{fig2_ovb_bias}"
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

_source line 22_

完成。`fig:framework` 已从 `method.tex` 移至 `background.tex` 中 `fig:ovb_bias` 之前。LaTeX 编译后 framework 图将排为 Figure 1，OVB 散点图排为 Figure 2。所有引用均使用 `\ref`，无需修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "uuid": "27091028-be4f-4da4-a5d1-1f72e3181332",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lpb8KcQGcG6WSQrYXN4a89",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1078,
      "cache_read_input_tokens": 32738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1078
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

_source line 23_

完成。`fig:framework` 已从 `method.tex` 移至 `background.tex` 中 `fig:ovb_bias` 之前。LaTeX 编译后 framework 图将排为 Figure 1，OVB 散点图排为 Figure 2。所有引用均使用 `\ref`，无需修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 35839,
  "duration_api_ms": 37107,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "53ba42e6-2485-4f74-9067-b2e31a7e3c9b",
  "total_cost_usd": 0.22879775,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 22369,
    "cache_read_input_tokens": 100845,
    "output_tokens": 1483,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 22369,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 94,
        "cache_read_input_tokens": 32738,
        "cache_creation_input_tokens": 1078,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1078
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1369,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001469,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 1483,
      "cacheReadInputTokens": 100845,
      "cacheCreationInputTokens": 22369,
      "webSearchRequests": 0,
      "costUSD": 0.22732875,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "0610f31a-4a2b-47d8-bf79-76117d13b2b3"
}
```

</details>

---
