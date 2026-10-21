# paper fix eq1 ci definition

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_paper_fix-eq1-ci-definition_20260519T062703.log`
- **Structured JSON:** [`999f9b69c606769d3235.json`](../../sessions/99/999f9b69c606769d3235.json)

## Before a recorded user message

48 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
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
  "uuid": "0328f8cf-02c1-4bc9-aa1d-d5b05b0529d3",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/memory/"
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
    "resetsAt": 1779172800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6c279a9e-9bd3-4b6e-9cbd-0cb72fdc6ac3",
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81"
}
```

---

### Assistant

_source line 4_

Let me start by reading the current method.tex to find Eq.1 and understand the existing definition.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "c8a978b1-be46-4862-9047-319f5a65b3dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SU81nUynyYuxEYdWwetao4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13092,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13092
      },
      "output_tokens": 2,
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_015tiSNtDtQLYfwBSgM3eD2D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "9d625f35-5052-4279-a407-36c3771a46ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SU81nUynyYuxEYdWwetao4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13092,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13092
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-19T06:27:12.891Z_

<details><summary>↩ Tool result · `toolu_015tiSNtDtQLYfwBSgM3eD2D`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: the original signal degrades monotonically.
17	Together with Markov chain convergence, this motivates (under mild regularity conditions, e.g., bounded per-step generation divergence) a finite $\Ktheory$ beyond which adjacent generations become indistinguishable.
18	
19	We define the operational lower bound:
20	\begin{equation}
21	  \Kempirical = \max\{k \geq 1 : \auc_{k-1,k} > \theta\},
22	  \label{eq:kstar}
23	\end{equation}
24	where $\auc_{k-1,k}$ is the point-estimate pairwise AUC (Area Under the ROC Curve) and $\theta = 0.60$ is a post-hoc operational threshold (motivated below).
25	Bootstrap 95\% confidence intervals (CIs; 1{,}000 resamples\footnote{Boundary-pair results in Table~\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\theta$ and non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
26	
27	\paragraph{Threshold choice.}
28	We set $\theta{=}0.60$ as a post-hoc operational threshold, chosen at the empirical discontinuity in the AUC distribution (Figure~\ref{fig:kstar_theta}).
29	A 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\,0.55$ and $p < 0.002$ for all boundary comparisons, placing $\theta{=}0.60$ well above the empirical null.
30	$\Kempirical{=}2$ is stable across $\theta \in [0.55, 0.65]$ for all but two marginal configurations (Table~\ref{tab:kstar_ci_extended}): 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, creating a ${\sim}$5--11\,pp discontinuity.
31	Only at extremes does $\Kempirical$ shift: $\theta{=}0.55$ yields $\Kempirical{=}3$ for two Qwen configurations; $\theta{=}0.70$ yields $\Kempirical{=}1$ across all configurations.
32	The downstream filtering evaluation (Section~\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\theta$, avoiding circularity.
33	A leave-one-family-out (LOFO) cross-validation on C4 independently validates this choice: each of five folds derives $\hat{\theta}$ from the gap midpoint between $\min(\auc_{1v2})$ and $\max(\auc_{2v3})$ over the remaining families, yielding $\hat{\theta} \in [0.5725, 0.6004]$; $\theta{=}0.60$ falls within this range, and 8/9 held-out predictions match the original $\Kempirical$ (the single mismatch is the borderline rewrite-mode configuration; Table~\ref{tab:theta_lofo}).
34	ArXiv corroborates with 6/6 LOFO agreement; Wikipedia is underdetermined because most models produce near-chance 1v2 AUC, invalidating the gap-based derivation (Appendix~\ref{sec:theta_lofo}).
35	
36	
37	\subsection{Features and Classifier}
38	\label{sec:features}
39	
40	Each document is characterized by a 15-dimensional feature vector spanning four groups: \emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).
41	All features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\ref{tab:s5_features}, Appendix).
42	Self-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.
43	Removing self-BLEU reduces mean $\auc_{1v2}$ by $< 1$\,pp across all models (14D $\Kempirical = 2$ for all 4 configurations; bootstrap CIs in Table~\ref{tab:selfbleu_ablation}); in deployment where depth labels are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted with minimal performance loss.
44	Hand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.
45	
46	We use \emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\text{depth} > k \mid \mathbf{x})$ via LightGBM~\cite{ke2017lightgbm} (hyperparameters in Table~\ref{tab:s6_lgbm_params}).
47	OBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\auc$ (mean 0.6095 vs.\ 0.4883 for ordinal logistic regression).
48	
49	\subsection{Experimental Setup}
50	\label{sec:experimental_setup}
51	
52	We evaluate nine configurations spanning five architecture families (Table~\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B, Qwen2.5-14B, Pythia-1.4B, OLMo-1B, LLaMA-3.1-8B, and Mistral-7B (all continuation except Qwen-rw).
53	Each uses 5{,}000 C4 seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).
54	Default decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.
55	Continuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.
56	Evaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\auc$ as primary metric.
57	
58	\begin{table}[t]
59	\centering
60	\small
61	\caption{Experimental configurations for depth-chain generation. \textbf{Config}: shorthand identifier; \textbf{Model}: architecture and parameter count; \textbf{Mode}: generation strategy (continuation or rewrite); $N$: number of seed documents per depth level.}
62	\label{tab:setup}
63	\resizebox{\columnwidth}{!}{%
64	\begin{tabular}{llcc}
65	\toprule
66	\textbf{Config} & \textbf{Model} & \textbf{Mode} & $N$ \\
67	\midrule
68	Qwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\
69	Qwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\
70	Qwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\
71	Pythia    & Pythia-1.4B            & Continuation & 5{,}000 \\
72	OLMo      & OLMo-1B               & Continuation & 5{,}000 \\
73	Qwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\
74	Qwen-14B  & Qwen2.5-14B           & Continuation & 5{,}000 \\
75	LLaMA-8B  & LLaMA-3.1-8B          & Continuation & 5{,}000 \\
76	Mistral   & Mistral-7B            & Continuation & 5{,}000 \\
77	\bottomrule
78	\end{tabular}}
79	\end{table}
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "9f7f9ab2-703c-447f-a021-e11613c41dbc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/pipeline.pdf}\n\\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}\n\\label{fig:pipeline}\n\\end{figure*}\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nA generation operator $G_\\delta$ (LLM + decoding strategy $\\delta$) produces successive generations $X \\to Y_1 \\to \\cdots \\to Y_K$, where $Y_k = G_\\delta(Y_{k-1})$ and $Y_0 \\triangleq X$ (Figure~\\ref{fig:pipeline}).\nThis sequence forms a Markov chain.\nBy the Data Processing Inequality, $I(X; Y_1) \\geq I(X; Y_2) \\geq \\cdots \\geq 0$: the original signal degrades monotonically.\nTogether with Markov chain convergence, this motivates (under mild regularity conditions, e.g., bounded per-step generation divergence) a finite $\\Ktheory$ beyond which adjacent generations become indistinguishable.\n\nWe define the operational lower bound:\n\\begin{equation}\n  \\Kempirical = \\max\\{k \\geq 1 : \\auc_{k-1,k} > \\theta\\},\n  \\label{eq:kstar}\n\\end{equation}\nwhere $\\auc_{k-1,k}$ is the point-estimate pairwise AUC (Area Under the ROC Curve) and $\\theta = 0.60$ is a post-hoc operational threshold (motivated below).\nBootstrap 95\\% confidence intervals (CIs; 1{,}000 resamples\\footnote{Boundary-pair results in Table~\\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\\theta$ and non-boundary-pair CI upper bounds fall below $\\theta$ (Section~\\ref{sec:kstar_boundary}).\n\n\\paragraph{Threshold choice.}\nWe set $\\theta{=}0.60$ as a post-hoc operational threshold, chosen at the empirical discontinuity in the AUC distribution (Figure~\\ref{fig:kstar_theta}).\nA 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\\,0.55$ and $p < 0.002$ for all boundary comparisons, placing $\\theta{=}0.60$ well above the empirical null.\n$\\Kempirical{=}2$ is stable across $\\theta \\in [0.55, 0.65]$ for all but two marginal configurations (Table~\\ref{tab:kstar_ci_extended}): 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, creating a ${\\sim}$5--11\\,pp discontinuity.\nOnly at extremes does $\\Kempirical$ shift: $\\theta{=}0.55$ yields $\\Kempirical{=}3$ for two Qwen configurations; $\\theta{=}0.70$ yields $\\Kempirical{=}1$ across all configurations.\nThe downstream filtering evaluation (Section~\\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\\theta$, avoiding circularity.\nA leave-one-family-out (LOFO) cross-validation on C4 independently validates this choice: each of five folds derives $\\hat{\\theta}$ from the gap midpoint between $\\min(\\auc_{1v2})$ and $\\max(\\auc_{2v3})$ over the remaining families, yielding $\\hat{\\theta} \\in [0.5725, 0.6004]$; $\\theta{=}0.60$ falls within this range, and 8/9 held-out predictions match the original $\\Kempirical$ (the single mismatch is the borderline rewrite-mode configuration; Table~\\ref{tab:theta_lofo}).\nArXiv corroborates with 6/6 LOFO agreement; Wikipedia is underdetermined because most models produce near-chance 1v2 AUC, invalidating the gap-based derivation (Appendix~\\ref{sec:theta_lofo}).\n\n\n\\subsection{Features and Classifier}\n\\label{sec:features}\n\nEach document is characterized by a 15-dimensional feature vector spanning four groups: \\emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \\emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \\emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \\emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).\nAll features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\\ref{tab:s5_features}, Appendix).\nSelf-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \\#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.\nRemoving self-BLEU reduces mean $\\auc_{1v2}$ by $< 1$\\,pp across all models (14D $\\Kempirical = 2$ for all 4 configurations; bootstrap CIs in Table~\\ref{tab:selfbleu_ablation}); in deployment where depth labels are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted with minimal performance loss.\nHand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.\n\nWe use \\emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\\text{depth} > k \\mid \\mathbf{x})$ via LightGBM~\\cite{ke2017lightgbm} (hyperparameters in Table~\\ref{tab:s6_lgbm_params}).\nOBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\\auc$ (mean 0.6095 vs.\\ 0.4883 for ordinal logistic regression).\n\n\\subsection{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate nine configurations spanning five architecture families (Table~\\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B, Qwen2.5-14B, Pythia-1.4B, OLMo-1B, LLaMA-3.1-8B, and Mistral-7B (all continuation except Qwen-rw).\nEach uses 5{,}000 C4 seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).\nDefault decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.\nContinuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.\nEvaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\\auc$ as primary metric.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Experimental configurations for depth-chain generation. \\textbf{Config}: shorthand identifier; \\textbf{Model}: architecture and parameter count; \\textbf{Mode}: generation strategy (continuation or rewrite); $N$: number of seed documents per depth level.}\n\\label{tab:setup}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Config} & \\textbf{Model} & \\textbf{Mode} & $N$ \\\\\n\\midrule\nQwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\\\\nQwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\\\\nQwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\\\\nPythia    & Pythia-1.4B            & Continuation & 5{,}000 \\\\\nOLMo      & OLMo-1B               & Continuation & 5{,}000 \\\\\nQwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\\\\nQwen-14B  & Qwen2.5-14B           & Continuation & 5{,}000 \\\\\nLLaMA-8B  & LLaMA-3.1-8B          & Continuation & 5{,}000 \\\\\nMistral   & Mistral-7B            & Continuation & 5{,}000 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 80
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

````text
Now I understand the current state of Eq.1 (line 20-23). Let me analyze the issue:

Current Eq.1 (line 20-23):
```latex
\Kempirical = \max\{k \geq 1 : \auc_{k-1,k} > \theta\},
```
where $\auc_{k-1,k}$ is the "point-estimate pairwise AUC" and $\theta = 0.60$.

Then on line 25, it says: "we verify that boundary-pair CI lower bounds exceed $\theta$ and non-boundary-pair CI upper bounds fall below $\theta$"
 
I see the core problem now: the equation uses point-estimate AUC values, but the actual verification procedure relies on confidence interval lower bounds instead. Plan A would align the equation with what's actually being done in practice by replacing the point estimate with the CI lower bound in the definition itself. I see the issue now - the equation uses a point estimate for AUC, but the verification step relies on confidence interval lower bounds. I need to make the formal definition match the actual procedure by updating the equation to use the CI lower bound directly instead of the point estimate. Let me revise the LaTeX to replace the point-estimate AUC notation with the confidence interval lower bound notation, and adjust the surrounding text to reflect this change consistently. The lower bound of the confidence interval must exceed the threshold to consider adjacent depths distinguishable, and I should verify that non-boundary pairs have upper bounds falling below this same threshold to ensure the boundary is properly validated. I'm defining the operational lower bound as the maximum depth where the pairwise AUC exceeds the threshold, which gives us a statistically grounded way to distinguish between adjacent depth levels.

Now I need to explain how bootstrap confidence intervals validate this boundary: we check that the CI lower bounds for boundary pairs stay above the threshold while non-boundary pairs have upper bounds below it, using 1,000 resamples for the main analysis and 10,000 for tighter margins where needed.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "8775fb67-fd5c-4e8b-90d9-ae992a64cc3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LeByrNJ61rWEzYQuZstQBE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2794,
      "cache_read_input_tokens": 24933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2794
      },
      "output_tokens": 10,
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

_source line 8_

Now let me check the macro definitions and find all related files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "eef3f71f-8f89-4d44-85e9-1b8b55999b48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LeByrNJ61rWEzYQuZstQBE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2794,
      "cache_read_input_tokens": 24933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2794
      },
      "output_tokens": 10,
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

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_01XMKWCRYzbqCBpEeJRDPosG`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "6fe305dc-e873-4b1c-b4c5-98e9272a4ab1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LeByrNJ61rWEzYQuZstQBE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2794,
      "cache_read_input_tokens": 24933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2794
      },
      "output_tokens": 10,
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

_source line 10 · 2026-05-19T06:27:42.962Z_

<details><summary>↩ Tool result · `toolu_01XMKWCRYzbqCBpEeJRDPosG`</summary>

```text
docs/paper/tables/tab_filtering_main.tex
docs/paper/tables/tab_alpha_sweep.tex
docs/paper/tables/tab_pairwise_significance.tex
docs/paper/tables/tab_crossscorer.tex
docs/paper/tables/tab_domain_model_kstar.tex
docs/paper/tables/tab_domain_model_kstar_full.tex
docs/paper/experiments_c3.tex
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/appendix.tex
docs/paper/experiments_c1.tex
docs/paper/introduction.tex
docs/paper/main.tex
docs/paper/discussion.tex
docs/paper/conclusion.tex
docs/paper/appendix_extended.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "b25949b7-6826-4a47-b043-e585df3ae933",
  "tool_use_result": {
    "filenames": [
      "docs/paper/tables/tab_filtering_main.tex",
      "docs/paper/tables/tab_alpha_sweep.tex",
      "docs/paper/tables/tab_pairwise_significance.tex",
      "docs/paper/tables/tab_crossscorer.tex",
      "docs/paper/tables/tab_domain_model_kstar.tex",
      "docs/paper/tables/tab_domain_model_kstar_full.tex",
      "docs/paper/experiments_c3.tex",
      "docs/paper/related_work.tex",
      "docs/paper/method.tex",
      "docs/paper/appendix.tex",
      "docs/paper/experiments_c1.tex",
      "docs/paper/introduction.tex",
      "docs/paper/main.tex",
      "docs/paper/discussion.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/appendix_extended.tex"
    ],
    "durationMs": 24,
    "numFiles": 16,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Grep · `toolu_01HrsCtyx33rZp3HHrRXRcDd`</summary>

```json
{
  "pattern": "\\\\newcommand.*auc|\\\\newcommand.*Kempirical|\\\\newcommand.*Ktheory|\\\\DeclareMathOperator.*auc",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
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
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "f84d25ec-46a6-4be6-9056-10a31a3fe4fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LeByrNJ61rWEzYQuZstQBE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2794,
      "cache_read_input_tokens": 24933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2794
      },
      "output_tokens": 10,
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

_source line 12 · 2026-05-19T06:27:43.790Z_

<details><summary>↩ Tool result · `toolu_01HrsCtyx33rZp3HHrRXRcDd`</summary>

```text
docs/paper/main.tex:23:\newcommand{\Kempirical}{{K^*_{\text{empirical}}}}
docs/paper/main.tex:24:\newcommand{\Ktheory}{{K^*_{\text{theory}}}}
docs/paper/main.tex:25:\newcommand{\auc}{\text{AUC}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "a6bfe858-3b08-46d9-b6fa-004ce9ce2016",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/main.tex:23:\\newcommand{\\Kempirical}{{K^*_{\\text{empirical}}}}\ndocs/paper/main.tex:24:\\newcommand{\\Ktheory}{{K^*_{\\text{theory}}}}\ndocs/paper/main.tex:25:\\newcommand{\\auc}{\\text{AUC}}",
    "numLines": 3
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I know the macros:
- `\Kempirical` = K*_empirical
- `\Ktheory` = K*_theory
- `\auc` = AUC

Now let me do the consistency check across all files. Let me grep for theta/CI-related mentions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "12436641-f566-42f0-b71e-1baa350ee47b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZg9AhdmiqXBnMXkLwmx23",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2642,
      "cache_read_input_tokens": 27727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2642
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

_source line 14_

Let me grep for all θ/CI references across the paper files to understand the consistency landscape before making changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "3d8e28a9-ed3e-4351-92a9-a5a77d4eee44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZg9AhdmiqXBnMXkLwmx23",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2642,
      "cache_read_input_tokens": 27727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2642
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

_source line 15_

<details open><summary>🔧 Tool call — Grep · `toolu_014HNFyqYw3eKZVEzgcaj8JQ`</summary>

```json
{
  "pattern": "theta|\\\\theta|0\\.60|CI.*lower|lower.*CI|CI_\\{|\\\\mathrm\\{CI\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex",
  "head_limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "5923d604-d5d9-406f-b1b5-0137bd884ddd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZg9AhdmiqXBnMXkLwmx23",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2642,
      "cache_read_input_tokens": 27727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2642
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

_source line 16 · 2026-05-19T06:27:49.858Z_

<details><summary>↩ Tool result · `toolu_014HNFyqYw3eKZVEzgcaj8JQ`</summary>

```text
docs/paper/appendix_extended.tex:39:The two models exhibit different decay profiles: Pythia achieves higher early-pair AUC (1v2: 0.947 vs.\ 0.897) but drops more steeply at deeper pairs (4v5: 0.691 vs.\ 0.746), yet both converge to $\Kempirical{=}7$ (6v7: Qwen 0.641, Pythia 0.634; both CI lower bounds $> \theta$).
docs/paper/appendix_extended.tex:42:Extrapolating yields 7v8 $\approx 0.57 < \theta$ for both models, suggesting $\Kempirical{=}7$ is near the ceiling.
docs/paper/appendix_extended.tex:48:\caption{Retrain-chain pairwise $\auc$ with 5-fold CV 95\% CIs. Both models yield $\Kempirical{=}7$; all CI lower bounds $> \theta{=}0.60$. Retrain-chain CIs use fold-level estimates (Section~\ref{sec:retrain_ci_note}).}
docs/paper/appendix_extended.tex:74:Table~\ref{tab:theta_sensitivity} reports $\Kempirical$ across $\theta \in [0.55, 0.70]$ for representative configurations including arXiv and cross-scorer conditions.
docs/paper/appendix_extended.tex:75:Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp; all ten boundary comparisons yield permutation $p < 0.001$.
docs/paper/appendix_extended.tex:80:\caption{$\Kempirical$ as a function of $\theta$ across conditions. The \textbf{domain ordering} (arXiv $>$ web $\geq$ cross-scorer) and \textbf{bounded range} ($\Kempirical{\leq}4$) are preserved across $\theta \in [0.55, 0.70]$. The headline result (web $\Kempirical{=}2$, arXiv $\Kempirical{=}3$) holds for $\theta \in [0.575, 0.625]$.}
docs/paper/appendix_extended.tex:81:\label{tab:theta_sensitivity}
docs/paper/appendix_extended.tex:85:\textbf{Condition} & \textbf{Config} & $\theta{=}0.55$ & $\theta{=}0.60$ & $\theta{=}0.625$ & $\theta{=}0.70$ \\
docs/paper/appendix_extended.tex:105:\includegraphics[width=\columnwidth]{figures/fig_theta_sensitivity.pdf}
docs/paper/appendix_extended.tex:106:\caption{$\Kempirical$ as a function of $\theta$ across all model $\times$ domain configurations (three panels: C4, arXiv, Wikipedia). The domain ordering (Wikipedia $\Kempirical{\leq}1$ $<$ C4 $\Kempirical{\leq}2$ $<$ arXiv $\Kempirical{\leq}3$) is preserved across the full $\theta \in [0.55, 0.70]$ range. Within each domain, inter-model variation is small relative to inter-domain differences, confirming that source domain rather than model identity governs $\Kempirical$.}
docs/paper/appendix_extended.tex:107:\label{fig:theta_sensitivity}
docs/paper/appendix_extended.tex:132:\caption{MMLU and HellaSwag by contamination ratio and filtering strategy (5 seeds, mean $\pm$ std). Base model MMLU: 0.6018. Binary filtering retains a significant advantage on HellaSwag across all ratios ($p \leq 0.004$, Holm-Bonferroni corrected).}
docs/paper/appendix_extended.tex:148:At all tested ratios (10--50\%), no-filter MMLU remains above the base model (0.6018), synthetic data at these proportions is therefore net-beneficial rather than harmful.
docs/paper/appendix_extended.tex:187:\caption{1v2 $\auc$ by feature subset size (Pythia-1.4B). $\Kempirical{=}2$ ($\auc > \theta{=}0.60$) is robust at $\geq$8 features.}
docs/paper/appendix_extended.tex:195:8D         & 5 & 5 & 0.6056 & 0.6159 \\
docs/paper/appendix_extended.tex:202:$\Kempirical{=}2$ holds for all subsets of size $\geq$8 (10/10 pass, min $\auc = 0.6056$), becomes fragile at 5D (2/5 pass), and fails at 3D (top-3 surprisal features alone: $\auc = 0.5871 < \theta$).
docs/paper/appendix_extended.tex:264:For Qwen-1.5B, cross-family scoring (Pythia-1.4B) yields $\auc$(1v2) $= 0.5994$, with per-fold values $[0.596, 0.606, 0.600, 0.603, 0.592]$ (2/5 folds marginally above $\theta = 0.60$).
docs/paper/appendix_extended.tex:265:The aggregate mean falls below $\theta$, confirming $\Kempirical{=}1$.
docs/paper/appendix_extended.tex:274:\caption{Bootstrap 95\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}
docs/paper/appendix_extended.tex:279:\textbf{Generator} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & \textbf{CI lower $> \theta$} \\
docs/paper/appendix_extended.tex:282:LLaMA-3.1-8B & 0.620 & $[0.605,\,0.636]$ & Yes (0.5\,pp margin) \\
docs/paper/appendix_extended.tex:283:Mistral-7B   & 0.608 & $[0.593,\,0.622]$ & No \\
docs/paper/appendix_extended.tex:306:\caption{Retrain-chain AUC decay across 7 generation pairs (Qwen2.5-1.5B LoRA). Unlike prompt-chain (sharp cliff at 0v1$\to$1v2), retrain-chain AUC decays gradually from 0.984 to 0.641, with all pairs above $\theta{=}0.60$. Error bars: 95\% CI from 5-fold CV. Dashed line: $\theta{=}0.60$; extrapolated 7v8 $\approx 0.57$ (below $\theta$), suggesting $\Kempirical{=}7$ is near the ceiling.}
docs/paper/appendix_extended.tex:313:Of 9 tested model configurations on C4, 8 yield $\Kempirical{=}2$; Mistral-7B is the only sub-2 exception ($\Kempirical{=}1$; 1v2 $\auc = 0.594$, CI $[0.584, 0.603]$), validating $\theta{=}0.60$ as an effective discriminator (gap: $0.594$ vs.\ $0.611$--$0.696$).
docs/paper/appendix_extended.tex:314:Mistral's cross-domain profile reinforces the domain-governed interpretation: despite $\Kempirical{=}1$ on both C4 and Wikipedia, it yields $\Kempirical{=}3$ on arXiv (1v2 $\auc = 0.820$, 2v3 $= 0.628$), and this profile persists under cross-scorer validation (Pythia-1.4B scorer: C4 $\Kempirical{=}1$, arXiv $\Kempirical{=}3$ (2v3 $\auc = 0.608$, CI $[0.593, 0.622]$)), domain lexical diversity can therefore rescue even web-text one-wash generators (Table~\ref{tab:domain_kstar}).
docs/paper/appendix_extended.tex:319:As a sample-size control, subsampling C4 to $n{=}2{,}200$ (matching arXiv) yields $\Kempirical{=}1$ (1v2 $\auc = 0.601$, CI $[0.586, 0.616]$).
docs/paper/appendix_extended.tex:330:\caption{arXiv pairwise $\auc$ with and without LaTeX markup (Qwen-1.5B continuation). Removing formatting reduces 2v3 by ${\sim}$1.8\,pp but $\Kempirical$ remains at 3 (CI lower $> \theta$). LaTeX stripping fraction increases with depth (0.6\% at depth 0, 4.6\% at depth 5), deeper generations therefore produce proportionally more formatting tokens.}
docs/paper/appendix_extended.tex:358:\caption{Subsampling power analysis for $\Kempirical{=}2$ determination (C4, Qwen-1.5B-base, 10 resamples per $n$). Detection probability: fraction of resamples where 1v2 $\auc > \theta{=}0.60$.}
docs/paper/appendix_extended.tex:377:\caption{$\Kempirical{=}2$ detection rate (left axis, blue) and mean 1v2 $\auc$ (right axis, green) as a function of sample size $n$. Detection rate reaches 100\% at $n{=}2{,}000$; the 80\% power threshold (dotted purple) is crossed between $n{=}1{,}000$ and $n{=}2{,}000$. Error bars: $\pm$1 std over 10 resamples. The dashed red line marks $\theta{=}0.60$.}
docs/paper/appendix_extended.tex:383:The sharp transition reflects the proximity of the 1v2 AUC to $\theta$: small increases in $n$ reduce variance sufficiently to move all resamples above the threshold.
docs/paper/appendix_extended.tex:410:Surprisal (base) & 0.597 & 0.809 & 0.581 & 0.601 ($-$0.007) & 0.828 ($-$0.031) & 0.616 ($-$0.003) \\
docs/paper/appendix_extended.tex:412:Lexical diversity & 0.550 & 0.691 & 0.557 & 0.608 ($-$0.001) & 0.855 ($-$0.005) & 0.614 ($-$0.005) \\
docs/paper/appendix_extended.tex:413:Freq. distribution & 0.533 & 0.684 & 0.564 & 0.604 ($-$0.005) & 0.851 ($-$0.009) & 0.612 ($-$0.007) \\
docs/paper/appendix_extended.tex:415:Full (15D) & 0.609 & 0.860 & 0.619 & \multicolumn{3}{c}{---} \\
docs/paper/appendix_extended.tex:506:\label{sec:theta_lofo}
docs/paper/appendix_extended.tex:508:To validate $\theta{=}0.60$ without circular reasoning, we perform leave-one-family-out (LOFO) cross-validation: each fold removes one architecture family, derives $\hat{\theta}$ as the midpoint between $\min(\auc_{1v2})$ and $\max(\auc_{2v3})$ over the remaining families, then predicts $\Kempirical$ for the held-out models.
docs/paper/appendix_extended.tex:509:Table~\ref{tab:theta_lofo} reports results across all three domains.
docs/paper/appendix_extended.tex:511:On C4, 8/9 held-out predictions agree with the original $\Kempirical$ assignment at $\theta{=}0.60$ (agreement: 89\%).
docs/paper/appendix_extended.tex:512:The single mismatch is Qwen-1.5B-RW (rewrite mode), whose 2v3 AUC of 0.5893 lies above the LOFO-derived $\hat{\theta}{=}0.5725$ but below the global $\theta{=}0.60$; this configuration is also the sole rewrite-mode model, the discrepancy is therefore attributable to mode rather than threshold instability.
docs/paper/appendix_extended.tex:513:The derived $\hat{\theta}$ values span $[0.5725, 0.6004]$, and $\theta{=}0.60$ falls within this range.
docs/paper/appendix_extended.tex:515:ArXiv corroborates with 6/6 agreement (100\%), though the wide $\hat{\theta}$ range $[0.5735, 0.7296]$ reflects OLMo-1B's near-chance performance ($\auc_{1v2}{=}0.503$), which inflates the gap midpoint when OLMo is included in the training fold.
docs/paper/appendix_extended.tex:519:Wikipedia's $\Kempirical{=}1$ assignment is independently confirmed by the global $\theta{=}0.60$ criterion (Section~\ref{sec:cross_domain}); LOFO simply cannot validate this because the method requires a clear AUC discontinuity between boundary and non-boundary pairs.
docs/paper/appendix_extended.tex:524:\caption{Leave-One-Family-Out (LOFO) cross-validation of $\theta$ across three domains. Each fold holds out one architecture family, derives $\hat{\theta}$ as the midpoint between $\min(\text{AUC}_{1\text{v}2})$ and $\max(\text{AUC}_{2\text{v}3})$ over the remaining families, and predicts $K^*$ for held-out models. C4 (primary): 8/9 agreement (89\%). arXiv: 6/6 (100\%). Wikipedia: 1/6 (17\%, see text).}
docs/paper/appendix_extended.tex:525:\label{tab:theta_lofo}
docs/paper/appendix_extended.tex:528:Domain & Held-out & Model & $\text{AUC}_{1\text{v}2}$ & $\text{AUC}_{2\text{v}3}$ & $\hat{\theta}$ & $K^*_{\hat{\theta}}$ & $K^*_{0.60}$ & Match \\
docs/paper/appendix_extended.tex:538: & Mistral & Mistral-7B & 0.5935 & 0.5402 & 0.6004 & 1 & 1 & \cmark \\
docs/paper/appendix_extended.tex:540: & \multicolumn{7}{l}{$\hat{\theta}$ $\in$ [0.5725, 0.6004], agreement: 8/9 (89\%)} \\
docs/paper/appendix_extended.tex:549: & \multicolumn{7}{l}{$\hat{\theta}$ $\in$ [0.5735, 0.7296], agreement: 6/6 (100\%)} \\
docs/paper/appendix_extended.tex:558: & \multicolumn{7}{l}{$\hat{\theta}$ $\in$ [0.5215, 0.5557], agreement: 1/6 (17\%)} \\
docs/paper/appendix_extended.tex:569:\caption{Code domain (Python, CodeSearchNet~\cite{husain2019codesearchnet}) pairwise AUC for Qwen2.5-1.5B. $\Kempirical{=}2$: 1v2 exceeds $\theta{=}0.60$; 2v3 drops to chance. JSD ratio (1v2/2v3) $= 11.7\times$, comparable to C4's cliff structure.}
docs/paper/appendix_extended.tex:581:\multicolumn{4}{l}{$\Kempirical = 2$ ($\theta = 0.60$)} \\
docs/paper/appendix_extended.tex:589:\caption{Code domain (Python, CodeSearchNet) cross-model pairwise AUC with 5-fold cross-validated 95\% CIs. Qwen2.5-1.5B yields $\Kempirical{=}2$; Pythia-1.4B yields borderline $\Kempirical{=}1$ (1v2 CI upper $= 0.603 > \theta$). Additional models pending completion.}
docs/paper/appendix_extended.tex:605:\multicolumn{5}{@{}p{\linewidth}@{}}{\footnotesize $^*$Permutation $p < 0.001$. $K^*$: max $k$ where $k$v$(k{+}1)$ AUC $\geq \theta = 0.60$.}
docs/paper/appendix_extended.tex:636:Below $\theta$ & Mistral-7B & 0.594 & surp\_std (13), freq\_entropy (9), surp\_d1\_skew (9) & 0.112 & $-$0.086 \\
docs/paper/main.tex:40:Across five architecture families (1B--14B), four source domains (three text, one code), and four decoding strategies at $\theta{=}0.60$ (AUC decision threshold), $\Kempirical{=}2$ for general web text (8/9 model configurations), $\Kempirical{=}1$--$2$ for code (Python, model-dependent), and $\Kempirical{=}3$ for structured academic text (arXiv).
docs/paper/main.tex:72:[Omitted long matching line]
docs/paper/main.tex:74:(3)~\emph{Threshold}: $\Kempirical$ ranges from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; 8/9 configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (Mistral-7B: $\Kempirical{=}1$).
docs/paper/main.tex:75:(4)~\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.002; cross-scorer validation drops this to $\Kempirical{=}1$ (Section~\ref{sec:transfer}). LLaMA-3.1-8B represents the most marginal $\Kempirical{=}2$ assignment, with the 1v2 CI lower bound within 0.3 percentage points of $\theta$.
docs/paper/main.tex:77:(6)~\emph{Segment length}: $\Kempirical{=}2$ confirmed for 128 and 256 tokens (CI lower $> \theta$); 512 tokens yields point estimate $\Kempirical{=}2$ but CI lower marginally below $\theta$ ($0.5979$); the boundary weakens at longer generation lengths.
docs/paper/experiments_c1.tex:16:$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
docs/paper/experiments_c1.tex:39:\caption{Pairwise $\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\theta = 0.60$.}
docs/paper/experiments_c1.tex:43:Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show $\Kempirical \leq 2$ across all 9 model configurations: 8/9 yield $\Kempirical{=}2$ (1v2 $\auc$ range: 0.6112--0.6955; all CI lower bounds $> \theta$; permutation $p < 0.001$), while Mistral-7B is the only exception ($\Kempirical{=}1$; 1v2 $\auc = 0.594$, below $\theta$; Section~\ref{sec:boundary_cases}).
docs/paper/experiments_c1.tex:44:LLaMA-3.1-8B yields $\Kempirical{=}2$ (0v1 $\auc = 0.9225$, 1v2 $\auc = 0.6123$, 95\% CI $[0.603, 0.622]$; borderline: 1/5 folds falls below $\theta$; Table~\ref{tab:kstar_ci_extended}).
docs/paper/experiments_c1.tex:49:$\Kempirical{=}2$ persists from 1.5B through 14B: Qwen-14B (1v2 $\auc = 0.621$ $[0.612, 0.630]$), Qwen-7B ($0.6168$ $[0.608, 0.626]$), and LLaMA-3.1-8B ($0.6123$) all exceed $\theta$, despite progressively reduced 0v1 signal (0.960 at 14B, 0.964 at 7B, 0.923 at 8B vs.\ $> 0.99$ at $\leq$1.5B).
docs/paper/experiments_c1.tex:54:\includegraphics[width=\columnwidth]{figures/fig_kstar_theta.pdf}
docs/paper/experiments_c1.tex:55:\caption{$\Kempirical(\theta)$ sensitivity curve for six configurations. $\Kempirical$: maximum discriminable depth; $\theta$: AUC decision threshold. All configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (dashed line). At $\theta{=}0.70$, all drop to $\Kempirical{=}1$.}
docs/paper/experiments_c1.tex:56:\label{fig:kstar_theta}
docs/paper/experiments_c1.tex:59:Figure~\ref{fig:kstar_theta} shows $\Kempirical$ as a function of $\theta$: web text $\Kempirical{=}2$ is stable across a 5\,pp window ($\theta \in [0.575, 0.625]$), with a gradual transition to $\Kempirical{=}3$ at $\theta{=}0.55$ (two Qwen configurations) and $\Kempirical{=}1$ at $\theta{=}0.70$.
docs/paper/experiments_c1.tex:60:The domain ordering (arXiv $>$ web $\geq$ cross-scorer) is preserved across the full $\theta$ range (Table~\ref{tab:theta_sensitivity}; Figure~\ref{fig:theta_sensitivity} in Appendix shows the complete model $\times$ domain $\theta$ sensitivity).
docs/paper/experiments_c1.tex:61:All four decoding strategies likewise yield $\Kempirical = 2$ at $\theta{=}0.60$ (1v2 $\auc \in [0.687, 0.704]$; Table~\ref{tab:s2_decoding}).
docs/paper/experiments_c1.tex:79:$\Kempirical$ is largely robust to scorer choice: across 22 cross-scorer configurations on C4 and arXiv, $\Kempirical$ was preserved in 20 cases; the two exceptions (Qwen-cont scored by Pythia on C4, Qwen-7B cross-scored on arXiv) are borderline, with AUC within 0.002 of $\theta$.
docs/paper/experiments_c1.tex:80:Qwen-cont is the most scorer-sensitive continuation-mode configuration: its self-scored 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp (Table~\ref{tab:kstar_ci}), and cross-family scoring pushes it below $\theta$.
docs/paper/experiments_c1.tex:81:For arXiv, cross-scoring with Pythia-1.4B preserves $\Kempirical{=}3$ for three of four generators (Qwen-1.5B, LLaMA-8B, Mistral-7B; 2v3 $\auc$ range: 0.608--0.632).
docs/paper/experiments_c1.tex:82:Qwen-7B exhibits a borderline decrease to $\Kempirical{=}2$ (2v3 $\auc = 0.599$ vs.\ $0.626$ self-scored, $\Delta = -2.7$\,pp; 3/5 folds above $\theta$), consistent with the Qwen family's scorer sensitivity observed on C4 and Wikipedia.
docs/paper/experiments_c1.tex:83:Bootstrap CIs (10{,}000 resamples) confirm $\Kempirical{=}3$ for Qwen-1.5B (CI lower $= 0.617$) and LLaMA-8B (CI lower $= 0.605$); for Mistral-7B (CI: $[0.593, 0.622]$) and Qwen-7B (CI: $[0.584, 0.613]$), the CI straddles $\theta$; their $\Kempirical{=}3$ assignment is sensitive to resampling variance (Table~\ref{tab:arxiv_crossscorer_ci}).
docs/paper/experiments_c1.tex:107:\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $\Kempirical^{\text{neural}}$: maximum depth where AUC exceeds $\theta = 0.60$.}
docs/paper/experiments_c1.tex:115:Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
docs/paper/experiments_c1.tex:129:All five domain-competent models yield $\Kempirical{=}3$ on arXiv, with boundary-pair $\auc$ (2v3) ranging from 0.6215 to 0.6545, all exceeding $\theta$.
docs/paper/experiments_c1.tex:131:Removing LaTeX markup reduces 2v3 AUC by ${\sim}$1.8\,pp but preserves $\Kempirical{=}3$ (CI lower $= 0.610 > \theta$; Table~\ref{tab:latex_ablation}); content-level properties dominate.
docs/paper/experiments_c1.tex:136:With scorer confound controlled (Pythia-1.4B for Qwen generators; Qwen-1.5B, itself cross-family, for all others), all six models yield $\Kempirical{=}1$ on Wikipedia: 1v2 $\auc$ ranges from 0.499 (OLMo) to 0.595 (LLaMA), all below $\theta$.

[Showing results with pagination = limit: 80]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "34a38d6e-2682-4263-927e-75f39e21ae81",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/appendix_extended.tex:39:The two models exhibit different decay profiles: Pythia achieves higher early-pair AUC (1v2: 0.947 vs.\\ 0.897) but drops more steeply at deeper pairs (4v5: 0.691 vs.\\ 0.746), yet both converge to $\\Kempirical{=}7$ (6v7: Qwen 0.641, Pythia 0.634; both CI lower bounds $> \\theta$).\ndocs/paper/appendix_extended.tex:42:Extrapolating yields 7v8 $\\approx 0.57 < \\theta$ for both models, suggesting $\\Kempirical{=}7$ is near the ceiling.\ndocs/paper/appendix_extended.tex:48:\\caption{Retrain-chain pairwise $\\auc$ with 5-fold CV 95\\% CIs. Both models yield $\\Kempirical{=}7$; all CI lower bounds $> \\theta{=}0.60$. Retrain-chain CIs use fold-level estimates (Section~\\ref{sec:retrain_ci_note}).}\ndocs/paper/appendix_extended.tex:74:Table~\\ref{tab:theta_sensitivity} reports $\\Kempirical$ across $\\theta \\in [0.55, 0.70]$ for representative configurations including arXiv and cross-scorer conditions.\ndocs/paper/appendix_extended.tex:75:Qwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp; all ten boundary comparisons yield permutation $p < 0.001$.\ndocs/paper/appendix_extended.tex:80:\\caption{$\\Kempirical$ as a function of $\\theta$ across conditions. The \\textbf{domain ordering} (arXiv $>$ web $\\geq$ cross-scorer) and \\textbf{bounded range} ($\\Kempirical{\\leq}4$) are preserved across $\\theta \\in [0.55, 0.70]$. The headline result (web $\\Kempirical{=}2$, arXiv $\\Kempirical{=}3$) holds for $\\theta \\in [0.575, 0.625]$.}\ndocs/paper/appendix_extended.tex:81:\\label{tab:theta_sensitivity}\ndocs/paper/appendix_extended.tex:85:\\textbf{Condition} & \\textbf{Config} & $\\theta{=}0.55$ & $\\theta{=}0.60$ & $\\theta{=}0.625$ & $\\theta{=}0.70$ \\\\\ndocs/paper/appendix_extended.tex:105:\\includegraphics[width=\\columnwidth]{figures/fig_theta_sensitivity.pdf}\ndocs/paper/appendix_extended.tex:106:\\caption{$\\Kempirical$ as a function of $\\theta$ across all model $\\times$ domain configurations (three panels: C4, arXiv, Wikipedia). The domain ordering (Wikipedia $\\Kempirical{\\leq}1$ $<$ C4 $\\Kempirical{\\leq}2$ $<$ arXiv $\\Kempirical{\\leq}3$) is preserved across the full $\\theta \\in [0.55, 0.70]$ range. Within each domain, inter-model variation is small relative to inter-domain differences, confirming that source domain rather than model identity governs $\\Kempirical$.}\ndocs/paper/appendix_extended.tex:107:\\label{fig:theta_sensitivity}\ndocs/paper/appendix_extended.tex:132:\\caption{MMLU and HellaSwag by contamination ratio and filtering strategy (5 seeds, mean $\\pm$ std). Base model MMLU: 0.6018. Binary filtering retains a significant advantage on HellaSwag across all ratios ($p \\leq 0.004$, Holm-Bonferroni corrected).}\ndocs/paper/appendix_extended.tex:148:At all tested ratios (10--50\\%), no-filter MMLU remains above the base model (0.6018), synthetic data at these proportions is therefore net-beneficial rather than harmful.\ndocs/paper/appendix_extended.tex:187:\\caption{1v2 $\\auc$ by feature subset size (Pythia-1.4B). $\\Kempirical{=}2$ ($\\auc > \\theta{=}0.60$) is robust at $\\geq$8 features.}\ndocs/paper/appendix_extended.tex:195:8D         & 5 & 5 & 0.6056 & 0.6159 \\\\\ndocs/paper/appendix_extended.tex:202:$\\Kempirical{=}2$ holds for all subsets of size $\\geq$8 (10/10 pass, min $\\auc = 0.6056$), becomes fragile at 5D (2/5 pass), and fails at 3D (top-3 surprisal features alone: $\\auc = 0.5871 < \\theta$).\ndocs/paper/appendix_extended.tex:264:For Qwen-1.5B, cross-family scoring (Pythia-1.4B) yields $\\auc$(1v2) $= 0.5994$, with per-fold values $[0.596, 0.606, 0.600, 0.603, 0.592]$ (2/5 folds marginally above $\\theta = 0.60$).\ndocs/paper/appendix_extended.tex:265:The aggregate mean falls below $\\theta$, confirming $\\Kempirical{=}1$.\ndocs/paper/appendix_extended.tex:274:\\caption{Bootstrap 95\\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}\ndocs/paper/appendix_extended.tex:279:\\textbf{Generator} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & \\textbf{CI lower $> \\theta$} \\\\\ndocs/paper/appendix_extended.tex:282:LLaMA-3.1-8B & 0.620 & $[0.605,\\,0.636]$ & Yes (0.5\\,pp margin) \\\\\ndocs/paper/appendix_extended.tex:283:Mistral-7B   & 0.608 & $[0.593,\\,0.622]$ & No \\\\\ndocs/paper/appendix_extended.tex:306:\\caption{Retrain-chain AUC decay across 7 generation pairs (Qwen2.5-1.5B LoRA). Unlike prompt-chain (sharp cliff at 0v1$\\to$1v2), retrain-chain AUC decays gradually from 0.984 to 0.641, with all pairs above $\\theta{=}0.60$. Error bars: 95\\% CI from 5-fold CV. Dashed line: $\\theta{=}0.60$; extrapolated 7v8 $\\approx 0.57$ (below $\\theta$), suggesting $\\Kempirical{=}7$ is near the ceiling.}\ndocs/paper/appendix_extended.tex:313:Of 9 tested model configurations on C4, 8 yield $\\Kempirical{=}2$; Mistral-7B is the only sub-2 exception ($\\Kempirical{=}1$; 1v2 $\\auc = 0.594$, CI $[0.584, 0.603]$), validating $\\theta{=}0.60$ as an effective discriminator (gap: $0.594$ vs.\\ $0.611$--$0.696$).\ndocs/paper/appendix_extended.tex:314:Mistral's cross-domain profile reinforces the domain-governed interpretation: despite $\\Kempirical{=}1$ on both C4 and Wikipedia, it yields $\\Kempirical{=}3$ on arXiv (1v2 $\\auc = 0.820$, 2v3 $= 0.628$), and this profile persists under cross-scorer validation (Pythia-1.4B scorer: C4 $\\Kempirical{=}1$, arXiv $\\Kempirical{=}3$ (2v3 $\\auc = 0.608$, CI $[0.593, 0.622]$)), domain lexical diversity can therefore rescue even web-text one-wash generators (Table~\\ref{tab:domain_kstar}).\ndocs/paper/appendix_extended.tex:319:As a sample-size control, subsampling C4 to $n{=}2{,}200$ (matching arXiv) yields $\\Kempirical{=}1$ (1v2 $\\auc = 0.601$, CI $[0.586, 0.616]$).\ndocs/paper/appendix_extended.tex:330:\\caption{arXiv pairwise $\\auc$ with and without LaTeX markup (Qwen-1.5B continuation). Removing formatting reduces 2v3 by ${\\sim}$1.8\\,pp but $\\Kempirical$ remains at 3 (CI lower $> \\theta$). LaTeX stripping fraction increases with depth (0.6\\% at depth 0, 4.6\\% at depth 5), deeper generations therefore produce proportionally more formatting tokens.}\ndocs/paper/appendix_extended.tex:358:\\caption{Subsampling power analysis for $\\Kempirical{=}2$ determination (C4, Qwen-1.5B-base, 10 resamples per $n$). Detection probability: fraction of resamples where 1v2 $\\auc > \\theta{=}0.60$.}\ndocs/paper/appendix_extended.tex:377:\\caption{$\\Kempirical{=}2$ detection rate (left axis, blue) and mean 1v2 $\\auc$ (right axis, green) as a function of sample size $n$. Detection rate reaches 100\\% at $n{=}2{,}000$; the 80\\% power threshold (dotted purple) is crossed between $n{=}1{,}000$ and $n{=}2{,}000$. Error bars: $\\pm$1 std over 10 resamples. The dashed red line marks $\\theta{=}0.60$.}\ndocs/paper/appendix_extended.tex:383:The sharp transition reflects the proximity of the 1v2 AUC to $\\theta$: small increases in $n$ reduce variance sufficiently to move all resamples above the threshold.\ndocs/paper/appendix_extended.tex:410:Surprisal (base) & 0.597 & 0.809 & 0.581 & 0.601 ($-$0.007) & 0.828 ($-$0.031) & 0.616 ($-$0.003) \\\\\ndocs/paper/appendix_extended.tex:412:Lexical diversity & 0.550 & 0.691 & 0.557 & 0.608 ($-$0.001) & 0.855 ($-$0.005) & 0.614 ($-$0.005) \\\\\ndocs/paper/appendix_extended.tex:413:Freq. distribution & 0.533 & 0.684 & 0.564 & 0.604 ($-$0.005) & 0.851 ($-$0.009) & 0.612 ($-$0.007) \\\\\ndocs/paper/appendix_extended.tex:415:Full (15D) & 0.609 & 0.860 & 0.619 & \\multicolumn{3}{c}{---} \\\\\ndocs/paper/appendix_extended.tex:506:\\label{sec:theta_lofo}\ndocs/paper/appendix_extended.tex:508:To validate $\\theta{=}0.60$ without circular reasoning, we perform leave-one-family-out (LOFO) cross-validation: each fold removes one architecture family, derives $\\hat{\\theta}$ as the midpoint between $\\min(\\auc_{1v2})$ and $\\max(\\auc_{2v3})$ over the remaining families, then predicts $\\Kempirical$ for the held-out models.\ndocs/paper/appendix_extended.tex:509:Table~\\ref{tab:theta_lofo} reports results across all three domains.\ndocs/paper/appendix_extended.tex:511:On C4, 8/9 held-out predictions agree with the original $\\Kempirical$ assignment at $\\theta{=}0.60$ (agreement: 89\\%).\ndocs/paper/appendix_extended.tex:512:The single mismatch is Qwen-1.5B-RW (rewrite mode), whose 2v3 AUC of 0.5893 lies above the LOFO-derived $\\hat{\\theta}{=}0.5725$ but below the global $\\theta{=}0.60$; this configuration is also the sole rewrite-mode model, the discrepancy is therefore attributable to mode rather than threshold instability.\ndocs/paper/appendix_extended.tex:513:The derived $\\hat{\\theta}$ values span $[0.5725, 0.6004]$, and $\\theta{=}0.60$ falls within this range.\ndocs/paper/appendix_extended.tex:515:ArXiv corroborates with 6/6 agreement (100\\%), though the wide $\\hat{\\theta}$ range $[0.5735, 0.7296]$ reflects OLMo-1B's near-chance performance ($\\auc_{1v2}{=}0.503$), which inflates the gap midpoint when OLMo is included in the training fold.\ndocs/paper/appendix_extended.tex:519:Wikipedia's $\\Kempirical{=}1$ assignment is independently confirmed by the global $\\theta{=}0.60$ criterion (Section~\\ref{sec:cross_domain}); LOFO simply cannot validate this because the method requires a clear AUC discontinuity between boundary and non-boundary pairs.\ndocs/paper/appendix_extended.tex:524:\\caption{Leave-One-Family-Out (LOFO) cross-validation of $\\theta$ across three domains. Each fold holds out one architecture family, derives $\\hat{\\theta}$ as the midpoint between $\\min(\\text{AUC}_{1\\text{v}2})$ and $\\max(\\text{AUC}_{2\\text{v}3})$ over the remaining families, and predicts $K^*$ for held-out models. C4 (primary): 8/9 agreement (89\\%). arXiv: 6/6 (100\\%). Wikipedia: 1/6 (17\\%, see text).}\ndocs/paper/appendix_extended.tex:525:\\label{tab:theta_lofo}\ndocs/paper/appendix_extended.tex:528:Domain & Held-out & Model & $\\text{AUC}_{1\\text{v}2}$ & $\\text{AUC}_{2\\text{v}3}$ & $\\hat{\\theta}$ & $K^*_{\\hat{\\theta}}$ & $K^*_{0.60}$ & Match \\\\\ndocs/paper/appendix_extended.tex:538: & Mistral & Mistral-7B & 0.5935 & 0.5402 & 0.6004 & 1 & 1 & \\cmark \\\\\ndocs/paper/appendix_extended.tex:540: & \\multicolumn{7}{l}{$\\hat{\\theta}$ $\\in$ [0.5725, 0.6004], agreement: 8/9 (89\\%)} \\\\\ndocs/paper/appendix_extended.tex:549: & \\multicolumn{7}{l}{$\\hat{\\theta}$ $\\in$ [0.5735, 0.7296], agreement: 6/6 (100\\%)} \\\\\ndocs/paper/appendix_extended.tex:558: & \\multicolumn{7}{l}{$\\hat{\\theta}$ $\\in$ [0.5215, 0.5557], agreement: 1/6 (17\\%)} \\\\\ndocs/paper/appendix_extended.tex:569:\\caption{Code domain (Python, CodeSearchNet~\\cite{husain2019codesearchnet}) pairwise AUC for Qwen2.5-1.5B. $\\Kempirical{=}2$: 1v2 exceeds $\\theta{=}0.60$; 2v3 drops to chance. JSD ratio (1v2/2v3) $= 11.7\\times$, comparable to C4's cliff structure.}\ndocs/paper/appendix_extended.tex:581:\\multicolumn{4}{l}{$\\Kempirical = 2$ ($\\theta = 0.60$)} \\\\\ndocs/paper/appendix_extended.tex:589:\\caption{Code domain (Python, CodeSearchNet) cross-model pairwise AUC with 5-fold cross-validated 95\\% CIs. Qwen2.5-1.5B yields $\\Kempirical{=}2$; Pythia-1.4B yields borderline $\\Kempirical{=}1$ (1v2 CI upper $= 0.603 > \\theta$). Additional models pending completion.}\ndocs/paper/appendix_extended.tex:605:\\multicolumn{5}{@{}p{\\linewidth}@{}}{\\footnotesize $^*$Permutation $p < 0.001$. $K^*$: max $k$ where $k$v$(k{+}1)$ AUC $\\geq \\theta = 0.60$.}\ndocs/paper/appendix_extended.tex:636:Below $\\theta$ & Mistral-7B & 0.594 & surp\\_std (13), freq\\_entropy (9), surp\\_d1\\_skew (9) & 0.112 & $-$0.086 \\\\\ndocs/paper/main.tex:40:Across five architecture families (1B--14B), four source domains (three text, one code), and four decoding strategies at $\\theta{=}0.60$ (AUC decision threshold), $\\Kempirical{=}2$ for general web text (8/9 model configurations), $\\Kempirical{=}1$--$2$ for code (Python, model-dependent), and $\\Kempirical{=}3$ for structured academic text (arXiv).\ndocs/paper/main.tex:72:[Omitted long matching line]\ndocs/paper/main.tex:74:(3)~\\emph{Threshold}: $\\Kempirical$ ranges from 2--3 at $\\theta{=}0.55$ to 1 at $\\theta{=}0.70$; 8/9 configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (Mistral-7B: $\\Kempirical{=}1$).\ndocs/paper/main.tex:75:(4)~\\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.002; cross-scorer validation drops this to $\\Kempirical{=}1$ (Section~\\ref{sec:transfer}). LLaMA-3.1-8B represents the most marginal $\\Kempirical{=}2$ assignment, with the 1v2 CI lower bound within 0.3 percentage points of $\\theta$.\ndocs/paper/main.tex:77:(6)~\\emph{Segment length}: $\\Kempirical{=}2$ confirmed for 128 and 256 tokens (CI lower $> \\theta$); 512 tokens yields point estimate $\\Kempirical{=}2$ but CI lower marginally below $\\theta$ ($0.5979$); the boundary weakens at longer generation lengths.\ndocs/paper/experiments_c1.tex:16:$\\Kempirical = 2$ requires 1v2 $\\auc > \\theta{=}0.60$ and 2v3 $\\auc < \\theta$; CIs quantify boundary uncertainty.\ndocs/paper/experiments_c1.tex:39:\\caption{Pairwise $\\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\\theta = 0.60$.}\ndocs/paper/experiments_c1.tex:43:Table~\\ref{tab:kstar_ci} and Figure~\\ref{fig:auc_decay} show $\\Kempirical \\leq 2$ across all 9 model configurations: 8/9 yield $\\Kempirical{=}2$ (1v2 $\\auc$ range: 0.6112--0.6955; all CI lower bounds $> \\theta$; permutation $p < 0.001$), while Mistral-7B is the only exception ($\\Kempirical{=}1$; 1v2 $\\auc = 0.594$, below $\\theta$; Section~\\ref{sec:boundary_cases}).\ndocs/paper/experiments_c1.tex:44:LLaMA-3.1-8B yields $\\Kempirical{=}2$ (0v1 $\\auc = 0.9225$, 1v2 $\\auc = 0.6123$, 95\\% CI $[0.603, 0.622]$; borderline: 1/5 folds falls below $\\theta$; Table~\\ref{tab:kstar_ci_extended}).\ndocs/paper/experiments_c1.tex:49:$\\Kempirical{=}2$ persists from 1.5B through 14B: Qwen-14B (1v2 $\\auc = 0.621$ $[0.612, 0.630]$), Qwen-7B ($0.6168$ $[0.608, 0.626]$), and LLaMA-3.1-8B ($0.6123$) all exceed $\\theta$, despite progressively reduced 0v1 signal (0.960 at 14B, 0.964 at 7B, 0.923 at 8B vs.\\ $> 0.99$ at $\\leq$1.5B).\ndocs/paper/experiments_c1.tex:54:\\includegraphics[width=\\columnwidth]{figures/fig_kstar_theta.pdf}\ndocs/paper/experiments_c1.tex:55:\\caption{$\\Kempirical(\\theta)$ sensitivity curve for six configurations. $\\Kempirical$: maximum discriminable depth; $\\theta$: AUC decision threshold. All configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (dashed line). At $\\theta{=}0.70$, all drop to $\\Kempirical{=}1$.}\ndocs/paper/experiments_c1.tex:56:\\label{fig:kstar_theta}\ndocs/paper/experiments_c1.tex:59:Figure~\\ref{fig:kstar_theta} shows $\\Kempirical$ as a function of $\\theta$: web text $\\Kempirical{=}2$ is stable across a 5\\,pp window ($\\theta \\in [0.575, 0.625]$), with a gradual transition to $\\Kempirical{=}3$ at $\\theta{=}0.55$ (two Qwen configurations) and $\\Kempirical{=}1$ at $\\theta{=}0.70$.\ndocs/paper/experiments_c1.tex:60:The domain ordering (arXiv $>$ web $\\geq$ cross-scorer) is preserved across the full $\\theta$ range (Table~\\ref{tab:theta_sensitivity}; Figure~\\ref{fig:theta_sensitivity} in Appendix shows the complete model $\\times$ domain $\\theta$ sensitivity).\ndocs/paper/experiments_c1.tex:61:All four decoding strategies likewise yield $\\Kempirical = 2$ at $\\theta{=}0.60$ (1v2 $\\auc \\in [0.687, 0.704]$; Table~\\ref{tab:s2_decoding}).\ndocs/paper/experiments_c1.tex:79:$\\Kempirical$ is largely robust to scorer choice: across 22 cross-scorer configurations on C4 and arXiv, $\\Kempirical$ was preserved in 20 cases; the two exceptions (Qwen-cont scored by Pythia on C4, Qwen-7B cross-scored on arXiv) are borderline, with AUC within 0.002 of $\\theta$.\ndocs/paper/experiments_c1.tex:80:Qwen-cont is the most scorer-sensitive continuation-mode configuration: its self-scored 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp (Table~\\ref{tab:kstar_ci}), and cross-family scoring pushes it below $\\theta$.\ndocs/paper/experiments_c1.tex:81:For arXiv, cross-scoring with Pythia-1.4B preserves $\\Kempirical{=}3$ for three of four generators (Qwen-1.5B, LLaMA-8B, Mistral-7B; 2v3 $\\auc$ range: 0.608--0.632).\ndocs/paper/experiments_c1.tex:82:Qwen-7B exhibits a borderline decrease to $\\Kempirical{=}2$ (2v3 $\\auc = 0.599$ vs.\\ $0.626$ self-scored, $\\Delta = -2.7$\\,pp; 3/5 folds above $\\theta$), consistent with the Qwen family's scorer sensitivity observed on C4 and Wikipedia.\ndocs/paper/experiments_c1.tex:83:Bootstrap CIs (10{,}000 resamples) confirm $\\Kempirical{=}3$ for Qwen-1.5B (CI lower $= 0.617$) and LLaMA-8B (CI lower $= 0.605$); for Mistral-7B (CI: $[0.593, 0.622]$) and Qwen-7B (CI: $[0.584, 0.613]$), the CI straddles $\\theta$; their $\\Kempirical{=}3$ assignment is sensitive to resampling variance (Table~\\ref{tab:arxiv_crossscorer_ci}).\ndocs/paper/experiments_c1.tex:107:\\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\\ $d{+}1$ text. $\\Kempirical^{\\text{neural}}$: maximum depth where AUC exceeds $\\theta = 0.60$.}\ndocs/paper/experiments_c1.tex:115:Pythia-1.4B & 0.5963 & $[0.589,\\,0.603]$ & 2 \\\\\ndocs/paper/experiments_c1.tex:129:All five domain-competent models yield $\\Kempirical{=}3$ on arXiv, with boundary-pair $\\auc$ (2v3) ranging from 0.6215 to 0.6545, all exceeding $\\theta$.\ndocs/paper/experiments_c1.tex:131:Removing LaTeX markup reduces 2v3 AUC by ${\\sim}$1.8\\,pp but preserves $\\Kempirical{=}3$ (CI lower $= 0.610 > \\theta$; Table~\\ref{tab:latex_ablation}); content-level properties dominate.\ndocs/paper/experiments_c1.tex:136:With scorer confound controlled (Pythia-1.4B for Qwen generators; Qwen-1.5B, itself cross-family, for all others), all six models yield $\\Kempirical{=}1$ on Wikipedia: 1v2 $\\auc$ ranges from 0.499 (OLMo) to 0.595 (LLaMA), all below $\\theta$.",
    "numLines": 80,
    "appliedLimit": 80
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good picture. Let me understand what needs to change:

1. **Eq.1 in method.tex (lines 19-25)**: The equation uses point-estimate AUC but the text says they verify with CI lower bounds. Need to make these consistent.

2. Looking at how the paper actually uses the criterion:
   - experiments_c1.tex line 16: "K* = 2 requires 1v2 AUC > θ=0.60 and 2v3 AUC < θ; CIs quantify boundary uncertainty."
   - experiments_c1.tex line 43: "all CI lower bounds > θ"
   - Various places mention CI lower bounds > θ as the actual criterion

The inconsistency is clear: Eq.1 says point-estimate AUC, but everywhere else uses CI lower bounds. I need to fix the equation to use CI lower bounds instead, but I want to keep the notation clean and readable rather than overly complex.

I'm considering a few options: using an underline notation like $\underline{\auc}_{k-1,k}$, a simple $\ell_{k-1,k}$ for the lower bound, or something more explicit like $\mathrm{CI}^{-}(\auc_{k-1,k})$. The cleanest approach seems to be defining $\ell_{k-1,k}$ as the lower bound of the 95% bootstrap CI and using that in the equation, which keeps things concise while still being clear about what we're measuring. I'm settling on using $\mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k})$ in the equation since it's clearer and aligns with how they already present confidence intervals. Now I need to update the surrounding text to explain what $\mathrm{CI}_{\mathrm{low}}$ means and adjust the description of the AUC estimates, plus I should check whether the example in experiments_c1.tex needs updating since it currently uses point-estimate language.

Looking through the other files, I see appendix_extended.tex also has similar language that should be consistent. Let me plan out which sections need edits: the main equation and text in method.tex, the example in experiments_c1.tex, and the definition in appendix_extended.tex. I'm noticing there are actually two different evaluation approaches in the codebase: the formal K* determination relies on CI lower bounds, while some secondary analyses like the feature ablation just use point estimates. The feature ablation context is different enough that it doesn't need the same CI treatment, so I'll focus on updating the main K* definitions where CI lower bounds should be explicitly mentioned.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "75b3261e-7a78-4f5e-a84f-af1a1eb063fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQr8wj9UHwkRnU3r8rnepU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7445,
      "cache_read_input_tokens": 30369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7445
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

_source line 18_

Let me read the specific context around the appendix line 605 and experiments_c1 line 16.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "52e51135-00b1-42bc-994b-14af18f63fb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQr8wj9UHwkRnU3r8rnepU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7445,
      "cache_read_input_tokens": 30369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7445
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

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01B7EBhnnTh5dv3wBh8hGqYe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "offset": 12,
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
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "fce15682-546a-4d54-8dba-c276c9a64ed5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQr8wj9UHwkRnU3r8rnepU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7445,
      "cache_read_input_tokens": 30369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7445
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

_source line 20 · 2026-05-19T06:28:24.214Z_

<details><summary>↩ Tool result · `toolu_01B7EBhnnTh5dv3wBh8hGqYe`</summary>

```text
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
17	Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
18	\label{tab:kstar_ci}
19	\begin{tabular}{lcccccccccc}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "7e40ec2a-78a5-4398-b4b9-5566efaa6e1e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
      "content": "\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Pairwise $\\auc$ for adjacent depth pairs with bootstrap 95\\% CIs and permutation $p$-values for boundary rows.\n$\\Kempirical = 2$ requires 1v2 $\\auc > \\theta{=}0.60$ and 2v3 $\\auc < \\theta$; CIs quantify boundary uncertainty.\nExtended results (all models) in Table~\\ref{tab:kstar_ci_extended}.}\n\\label{tab:kstar_ci}\n\\begin{tabular}{lcccccccccc}",
      "numLines": 8,
      "startLine": 12,
      "totalLines": 176
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01RAFjFo8GgtTHWmt1LzWZsR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": 600,
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
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "3ad758b5-c1de-447d-86f6-d317447499f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQr8wj9UHwkRnU3r8rnepU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7445,
      "cache_read_input_tokens": 30369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7445
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

_source line 22 · 2026-05-19T06:28:25.018Z_

<details><summary>↩ Tool result · `toolu_01RAFjFo8GgtTHWmt1LzWZsR`</summary>

```text
600	3v4 & .5022 & --- & .5152 & --- \\
601	4v5 & .5219 & --- & .5046 & --- \\
602	\midrule
603	$K^*$ & \multicolumn{2}{c}{\textbf{2}} & \multicolumn{2}{c}{1} \\
604	\bottomrule
605	\multicolumn{5}{@{}p{\linewidth}@{}}{\footnotesize $^*$Permutation $p < 0.001$. $K^*$: max $k$ where $k$v$(k{+}1)$ AUC $\geq \theta = 0.60$.}
606	\end{tabular}
607	\end{table}
608	
609	\subsection{Borderline Feature Analysis}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "6755e811-f3fb-4eba-8c6a-a0b676d4f6aa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
      "content": "3v4 & .5022 & --- & .5152 & --- \\\\\n4v5 & .5219 & --- & .5046 & --- \\\\\n\\midrule\n$K^*$ & \\multicolumn{2}{c}{\\textbf{2}} & \\multicolumn{2}{c}{1} \\\\\n\\bottomrule\n\\multicolumn{5}{@{}p{\\linewidth}@{}}{\\footnotesize $^*$Permutation $p < 0.001$. $K^*$: max $k$ where $k$v$(k{+}1)$ AUC $\\geq \\theta = 0.60$.}\n\\end{tabular}\n\\end{table}\n\n\\subsection{Borderline Feature Analysis}",
      "numLines": 10,
      "startLine": 600,
      "totalLines": 670
    }
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

````text
Now I have a clear picture of all the changes needed. Let me make them:

1. **method.tex lines 19-25**: Fix Eq.1 to use CI lower bound
2. **experiments_c1.tex line 16**: Fix table caption to use CI lower bound language
3. **appendix_extended.tex line 605**: Fix table footnote to use CI lower bound language

Let me craft each edit carefully.

### Edit 1: method.tex (lines 19-25)

Current:
```
We define the operational lower bound:
\begin{equation}
  \Kempirical = \max\{k \geq 1 : \auc_{k-1,k} > \theta\},
  \label{eq:kstar}
\end{equation}
where $\auc_{k-1,k}$ is the point-estimate pairwise AUC (Area Under the ROC Curve) and $\theta = 0.60$ is a post-hoc operational threshold (motivated below).
Bootstrap 95\% confidence intervals (CIs; 1{,}000 resamples\footnote{Boundary-pair results in Table~\ref{tab:kstar_ci} use
```

I need to replace the point-estimate AUC reference with the CI lower bound, so the equation and description should reference the lower confidence bound instead of the raw point estimate.

```
\Kempirical = \max\{k \geq 1 : \mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k}) > \theta\},
  \label{eq:kstar}
\end{equation}
where $\mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k})$ is the lower bound of a 95\% bootstrap confidence interval (1{,}000 resamples for boundary pairs, 10{,}000 for tighter margins on cross-scorer results) and $\theta = 0.60$ is the operational threshold. This approach provides uncertainty quantification by ensuring boundary-pair lower bounds exceed the threshold while non-boundary-pair upper bounds fall below it.
``` I'm double-checking the writing constraints here—making sure there are no em-dashes or en-dashes, and that I'm not ending phrases with -ing participles. The sentence about K* reflecting discriminability rather than sampling noise checks out; "sampling noise" is a standard noun phrase, not a participial ending. The flow and conciseness look good too.

Now I need to verify where the footnote for the 1,000 resamples should attach and whether I need to spell out "between depths k-1 and k" or if the subscript already makes that clear. Since the subscript notation already indicates the pair, I can keep this tighter without the extra explanation.

For the next part about the threshold θ = 0.60 and the verification step, I'm noting that this establishes the robustness criterion and mentions checking that non-boundary pairs stay below the threshold in a later section. I'm verifying the exact criteria for K*=2: the boundary pair (1v2) needs its CI lower bound exceeding θ=0.60 to show discriminability, while the non-boundary pair (2v3) requires its CI upper bound falling below θ to confirm non-discriminability. For the caption, I should use the full notation with CI subscripts to be precise. I'm refining the table caption to be more concise. The key constraint is that K* = 2 requires the lower confidence bound for the 1v2 comparison to exceed θ = 0.60, while the 2v3 lower bound must stay at or below that threshold, with an additional check that non-boundary upper bounds fall below θ as well. I'll strip away the extra detail and just state the essential requirement clearly. I'm checking the appendix for consistency in how K* is defined across different sections. The footnote at line 605 currently states the definition in terms of point-estimate AUC, but I need to update it to match the corrected definition using confidence interval lower bounds, just like I'm doing for the main text. I'm also scanning for other places where K* might be restated to ensure everything aligns with the fix.

Looking at the feature ablation results and cross-family scoring sections, those are using point estimates in their specific contexts—describing aggregate behavior over subsets or per-fold values—which is appropriate for those analyses and doesn't conflict with the formal K* criterion. The cross-family example actually supports the conclusion since if the mean falls below θ, the confidence interval lower bound would too.

Now I should check the discussion and conclusion sections, and also verify the specific files mentioned in the task.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "fef61eaa-f1a2-49c2-b25a-16758b42f1c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UsHNqeH5h6fLzjehpJKd73",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2468,
      "cache_read_input_tokens": 37814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2468
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

_source line 24_

Let me also check discussion.tex for any K*/θ criterion statements.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "9ce3bc0f-510d-4833-a44d-7bbf94e7d6f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UsHNqeH5h6fLzjehpJKd73",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2468,
      "cache_read_input_tokens": 37814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2468
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

_source line 25_

<details open><summary>🔧 Tool call — Grep · `toolu_019hp4nWHmjL4dKWobFdB4NU`</summary>

```json
{
  "pattern": "theta|\\\\theta|0\\.60|CI.*lower|lower.*CI",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
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
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "3afe9511-675b-492c-8785-3b13432d292c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UsHNqeH5h6fLzjehpJKd73",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2468,
      "cache_read_input_tokens": 37814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2468
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

_source line 26 · 2026-05-19T06:29:15.739Z_

<details><summary>↩ Tool result · `toolu_019hp4nWHmjL4dKWobFdB4NU`</summary>

```text
18:For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$.
27:For web text, 2v3 $\auc < \theta$ across all configurations, so depth assignments beyond $d{=}2$ approximate random labels; the strategy ordering binary $>$ graduated aligns with $\Kempirical{=}2$ (on arXiv, graduated filtering similarly shows no improvement; Appendix~\ref{sec:extended_limitations}).
33:C4 yields $\Kempirical{=}2$ (8/9 configurations), Python code $\Kempirical{=}2$ for Qwen2.5-1.5B but borderline $\Kempirical{=}1$ for Pythia-1.4B (CI upper $= 0.603$; Section~\ref{sec:cross_domain}), arXiv $\Kempirical{=}3$ (five models, four families), and Wikipedia $\Kempirical{=}1$ (Appendix~\ref{sec:wiki_domain}); the ordering correlates with structural complexity (Table~\ref{tab:domain-ttr-entropy}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "1f4f7deb-9efc-41eb-a783-f235665d446a",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "18:For general web text, $\\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\\auc \\geq 0.92$), 1v2 drops by ${\\sim}$30\\,pp, and 2v3 falls below $\\theta$.\n27:For web text, 2v3 $\\auc < \\theta$ across all configurations, so depth assignments beyond $d{=}2$ approximate random labels; the strategy ordering binary $>$ graduated aligns with $\\Kempirical{=}2$ (on arXiv, graduated filtering similarly shows no improvement; Appendix~\\ref{sec:extended_limitations}).\n33:C4 yields $\\Kempirical{=}2$ (8/9 configurations), Python code $\\Kempirical{=}2$ for Qwen2.5-1.5B but borderline $\\Kempirical{=}1$ for Pythia-1.4B (CI upper $= 0.603$; Section~\\ref{sec:cross_domain}), arXiv $\\Kempirical{=}3$ (five models, four families), and Wikipedia $\\Kempirical{=}1$ (Appendix~\\ref{sec:wiki_domain}); the ordering correlates with structural complexity (Table~\\ref{tab:domain-ttr-entropy}).",
    "numLines": 3
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Looking at discussion.tex:
- Line 18: "2v3 falls below θ" — uses point-estimate language but the context is describing the AUC decay pattern, not restating the K* criterion. It's saying the AUC value falls below θ, which is a factual observation. This is fine.
- Line 27: "2v3 AUC < θ across all configurations" — similar, describing the observation.
- Line 33: mentions "CI upper = 0.603" for the borderline case. This is already using CI language where appropriate.


These observations are consistent whether I'm checking point estimates or CI bounds, since a point estimate below θ guarantees the CI lower bound is also below θ. I'll go ahead with the three edits now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "4bc5c398-3651-4118-b255-cedbfd465a1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1tQRxZZydE8v2TUenYcE1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3576,
      "cache_read_input_tokens": 40282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3576
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

_source line 28_

I have a clear picture of all changes needed. Three edits: Eq.1 in method.tex, the table caption in experiments_c1.tex, and the footnote in appendix_extended.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "2848be6a-b313-4aab-b570-75847a1e4e73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1tQRxZZydE8v2TUenYcE1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3576,
      "cache_read_input_tokens": 40282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3576
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

_source line 29_

<details open><summary>🔧 Tool call — Edit · `toolu_01EtZ1C8AK4tNV6SS8FcdF2r`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex",
  "old_string": "We define the operational lower bound:\n\\begin{equation}\n  \\Kempirical = \\max\\{k \\geq 1 : \\auc_{k-1,k} > \\theta\\},\n  \\label{eq:kstar}\n\\end{equation}\nwhere $\\auc_{k-1,k}$ is the point-estimate pairwise AUC (Area Under the ROC Curve) and $\\theta = 0.60$ is a post-hoc operational threshold (motivated below).\nBootstrap 95\\% confidence intervals (CIs; 1{,}000 resamples\\footnote{Boundary-pair results in Table~\\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\\theta$ and non-boundary-pair CI upper bounds fall below $\\theta$ (Section~\\ref{sec:kstar_boundary}).",
  "new_string": "We define the operational lower bound:\n\\begin{equation}\n  \\Kempirical = \\max\\{k \\geq 1 : \\mathrm{CI}_{\\mathrm{low}}(\\auc_{k-1,k}) > \\theta\\},\n  \\label{eq:kstar}\n\\end{equation}\nwhere $\\mathrm{CI}_{\\mathrm{low}}(\\auc_{k-1,k})$ is the lower bound of a 95\\% bootstrap confidence interval (1{,}000 resamples\\footnote{Boundary-pair results in Table~\\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) over the pairwise AUC (Area Under the ROC Curve) between depths $k{-}1$ and $k$, and $\\theta = 0.60$ is a post-hoc operational threshold (motivated below).\nThis criterion ensures that $\\Kempirical$ reflects statistically robust discriminability rather than sampling noise.\nWe additionally verify that non-boundary-pair CI upper bounds fall below $\\theta$ (Section~\\ref{sec:kstar_boundary})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "f3ea7200-1e3c-4b24-af39-6a0951239cb0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1tQRxZZydE8v2TUenYcE1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3576,
      "cache_read_input_tokens": 40282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3576
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

_source line 30 · 2026-05-19T06:29:28.010Z_

<details><summary>↩ Tool result · `toolu_01EtZ1C8AK4tNV6SS8FcdF2r`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "5385b97a-ef7f-4950-8289-91601371a282",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex",
    "oldString": "We define the operational lower bound:\n\\begin{equation}\n  \\Kempirical = \\max\\{k \\geq 1 : \\auc_{k-1,k} > \\theta\\},\n  \\label{eq:kstar}\n\\end{equation}\nwhere $\\auc_{k-1,k}$ is the point-estimate pairwise AUC (Area Under the ROC Curve) and $\\theta = 0.60$ is a post-hoc operational threshold (motivated below).\nBootstrap 95\\% confidence intervals (CIs; 1{,}000 resamples\\footnote{Boundary-pair results in Table~\\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\\theta$ and non-boundary-pair CI upper bounds fall below $\\theta$ (Section~\\ref{sec:kstar_boundary}).",
    "newString": "We define the operational lower bound:\n\\begin{equation}\n  \\Kempirical = \\max\\{k \\geq 1 : \\mathrm{CI}_{\\mathrm{low}}(\\auc_{k-1,k}) > \\theta\\},\n  \\label{eq:kstar}\n\\end{equation}\nwhere $\\mathrm{CI}_{\\mathrm{low}}(\\auc_{k-1,k})$ is the lower bound of a 95\\% bootstrap confidence interval (1{,}000 resamples\\footnote{Boundary-pair results in Table~\\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) over the pairwise AUC (Area Under the ROC Curve) between depths $k{-}1$ and $k$, and $\\theta = 0.60$ is a post-hoc operational threshold (motivated below).\nThis criterion ensures that $\\Kempirical$ reflects statistically robust discriminability rather than sampling noise.\nWe additionally verify that non-boundary-pair CI upper bounds fall below $\\theta$ (Section~\\ref{sec:kstar_boundary}).",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/pipeline.pdf}\n\\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}\n\\label{fig:pipeline}\n\\end{figure*}\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nA generation operator $G_\\delta$ (LLM + decoding strategy $\\delta$) produces successive generations $X \\to Y_1 \\to \\cdots \\to Y_K$, where $Y_k = G_\\delta(Y_{k-1})$ and $Y_0 \\triangleq X$ (Figure~\\ref{fig:pipeline}).\nThis sequence forms a Markov chain.\nBy the Data Processing Inequality, $I(X; Y_1) \\geq I(X; Y_2) \\geq \\cdots \\geq 0$: the original signal degrades monotonically.\nTogether with Markov chain convergence, this motivates (under mild regularity conditions, e.g., bounded per-step generation divergence) a finite $\\Ktheory$ beyond which adjacent generations become indistinguishable.\n\nWe define the operational lower bound:\n\\begin{equation}\n  \\Kempirical = \\max\\{k \\geq 1 : \\auc_{k-1,k} > \\theta\\},\n  \\label{eq:kstar}\n\\end{equation}\nwhere $\\auc_{k-1,k}$ is the point-estimate pairwise AUC (Area Under the ROC Curve) and $\\theta = 0.60$ is a post-hoc operational threshold (motivated below).\nBootstrap 95\\% confidence intervals (CIs; 1{,}000 resamples\\footnote{Boundary-pair results in Table~\\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\\theta$ and non-boundary-pair CI upper bounds fall below $\\theta$ (Section~\\ref{sec:kstar_boundary}).\n\n\\paragraph{Threshold choice.}\nWe set $\\theta{=}0.60$ as a post-hoc operational threshold, chosen at the empirical discontinuity in the AUC distribution (Figure~\\ref{fig:kstar_theta}).\nA 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\\,0.55$ and $p < 0.002$ for all boundary comparisons, placing $\\theta{=}0.60$ well above the empirical null.\n$\\Kempirical{=}2$ is stable across $\\theta \\in [0.55, 0.65]$ for all but two marginal configurations (Table~\\ref{tab:kstar_ci_extended}): 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, creating a ${\\sim}$5--11\\,pp discontinuity.\nOnly at extremes does $\\Kempirical$ shift: $\\theta{=}0.55$ yields $\\Kempirical{=}3$ for two Qwen configurations; $\\theta{=}0.70$ yields $\\Kempirical{=}1$ across all configurations.\nThe downstream filtering evaluation (Section~\\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\\theta$, avoiding circularity.\nA leave-one-family-out (LOFO) cross-validation on C4 independently validates this choice: each of five folds derives $\\hat{\\theta}$ from the gap midpoint between $\\min(\\auc_{1v2})$ and $\\max(\\auc_{2v3})$ over the remaining families, yielding $\\hat{\\theta} \\in [0.5725, 0.6004]$; $\\theta{=}0.60$ falls within this range, and 8/9 held-out predictions match the original $\\Kempirical$ (the single mismatch is the borderline rewrite-mode configuration; Table~\\ref{tab:theta_lofo}).\nArXiv corroborates with 6/6 LOFO agreement; Wikipedia is underdetermined because most models produce near-chance 1v2 AUC, invalidating the gap-based derivation (Appendix~\\ref{sec:theta_lofo}).\n\n\n\\subsection{Features and Classifier}\n\\label{sec:features}\n\nEach document is characterized by a 15-dimensional feature vector spanning four groups: \\emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \\emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \\emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \\emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).\nAll features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\\ref{tab:s5_features}, Appendix).\nSelf-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \\#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.\nRemoving self-BLEU reduces mean $\\auc_{1v2}$ by $< 1$\\,pp across all models (14D $\\Kempirical = 2$ for all 4 configurations; bootstrap CIs in Table~\\ref{tab:selfbleu_ablation}); in deployment where depth labels are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted with minimal performance loss.\nHand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.\n\nWe use \\emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\\text{depth} > k \\mid \\mathbf{x})$ via LightGBM~\\cite{ke2017lightgbm} (hyperparameters in Table~\\ref{tab:s6_lgbm_params}).\nOBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\\auc$ (mean 0.6095 vs.\\ 0.4883 for ordinal logistic regression).\n\n\\subsection{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate nine configurations spanning five architecture families (Table~\\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B, Qwen2.5-14B, Pythia-1.4B, OLMo-1B, LLaMA-3.1-8B, and Mistral-7B (all continuation except Qwen-rw).\nEach uses 5{,}000 C4 seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).\nDefault decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.\nContinuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.\nEvaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\\auc$ as primary metric.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Experimental configurations for depth-chain generation. \\textbf{Config}: shorthand identifier; \\textbf{Model}: architecture and parameter count; \\textbf{Mode}: generation strategy (continuation or rewrite); $N$: number of seed documents per depth level.}\n\\label{tab:setup}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Config} & \\textbf{Model} & \\textbf{Mode} & $N$ \\\\\n\\midrule\nQwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\\\\nQwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\\\\nQwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\\\\nPythia    & Pythia-1.4B            & Continuation & 5{,}000 \\\\\nOLMo      & OLMo-1B               & Continuation & 5{,}000 \\\\\nQwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\\\\nQwen-14B  & Qwen2.5-14B           & Continuation & 5{,}000 \\\\\nLLaMA-8B  & LLaMA-3.1-8B          & Continuation & 5{,}000 \\\\\nMistral   & Mistral-7B            & Continuation & 5{,}000 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 18,
        "oldLines": 11,
        "newStart": 18,
        "newLines": 12,
        "lines": [
          " ",
          " We define the operational lower bound:",
          " \\begin{equation}",
          "-  \\Kempirical = \\max\\{k \\geq 1 : \\auc_{k-1,k} > \\theta\\},",
          "+  \\Kempirical = \\max\\{k \\geq 1 : \\mathrm{CI}_{\\mathrm{low}}(\\auc_{k-1,k}) > \\theta\\},",
          "   \\label{eq:kstar}",
          " \\end{equation}",
          "-where $\\auc_{k-1,k}$ is the point-estimate pairwise AUC (Area Under the ROC Curve) and $\\theta = 0.60$ is a post-hoc operational threshold (motivated below).",
          "-Bootstrap 95\\% confidence intervals (CIs; 1{,}000 resamples\\footnote{Boundary-pair results in Table~\\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\\theta$ and non-boundary-pair CI upper bounds fall below $\\theta$ (Section~\\ref{sec:kstar_boundary}).",
          "+where $\\mathrm{CI}_{\\mathrm{low}}(\\auc_{k-1,k})$ is the lower bound of a 95\\% bootstrap confidence interval (1{,}000 resamples\\footnote{Boundary-pair results in Table~\\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) over the pairwise AUC (Area Under the ROC Curve) between depths $k{-}1$ and $k$, and $\\theta = 0.60$ is a post-hoc operational threshold (motivated below).",
          "+This criterion ensures that $\\Kempirical$ reflects statistically robust discriminability rather than sampling noise.",
          "+We additionally verify that non-boundary-pair CI upper bounds fall below $\\theta$ (Section~\\ref{sec:kstar_boundary}).",
          " ",
          " \\paragraph{Threshold choice.}",
          " We set $\\theta{=}0.60$ as a post-hoc operational threshold, chosen at the empirical discontinuity in the AUC distribution (Figure~\\ref{fig:kstar_theta})."
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

_source line 31_

<details open><summary>🔧 Tool call — Edit · `toolu_017C4c96sJducArpcyostBZJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "old_string": "$\\Kempirical = 2$ requires 1v2 $\\auc > \\theta{=}0.60$ and 2v3 $\\auc < \\theta$; CIs quantify boundary uncertainty.",
  "new_string": "$\\Kempirical = 2$ requires 1v2 CI lower bound $> \\theta{=}0.60$ and 2v3 CI lower bound $\\leq \\theta$ (Eq.~\\ref{eq:kstar})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "cbbf6fc2-6312-4a6d-8d38-918321afd79b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1tQRxZZydE8v2TUenYcE1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3576,
      "cache_read_input_tokens": 40282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3576
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

_source line 32 · 2026-05-19T06:29:29.763Z_

<details><summary>↩ Tool result · `toolu_017C4c96sJducArpcyostBZJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "c749f682-a0fe-4de6-af0d-edcced0a3918",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "oldString": "$\\Kempirical = 2$ requires 1v2 $\\auc > \\theta{=}0.60$ and 2v3 $\\auc < \\theta$; CIs quantify boundary uncertainty.",
    "newString": "$\\Kempirical = 2$ requires 1v2 CI lower bound $> \\theta{=}0.60$ and 2v3 CI lower bound $\\leq \\theta$ (Eq.~\\ref{eq:kstar}).",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate generational depth estimation on nine model configurations spanning five architecture families:\nPythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, Qwen2.5-14B, LLaMA-3.1-8B, and Mistral-7B, all in continuation mode except where noted.\nAll experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5; power analysis in Appendix~\\ref{sec:power_curve}).\n\n%% ====================================================================\n\\subsection{\\texorpdfstring{$\\Kempirical \\leq 2$}{K*<=2} Across Model Configurations (C4)}\n\\label{sec:kstar_boundary}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Pairwise $\\auc$ for adjacent depth pairs with bootstrap 95\\% CIs and permutation $p$-values for boundary rows.\n$\\Kempirical = 2$ requires 1v2 $\\auc > \\theta{=}0.60$ and 2v3 $\\auc < \\theta$; CIs quantify boundary uncertainty.\nExtended results (all models) in Table~\\ref{tab:kstar_ci_extended}.}\n\\label{tab:kstar_ci}\n\\begin{tabular}{lcccccccccc}\n\\toprule\n & \\multicolumn{2}{c}{Qwen-rw} & \\multicolumn{2}{c}{Pythia} & \\multicolumn{2}{c}{OLMo} & \\multicolumn{2}{c}{Qwen-cont} & \\multicolumn{2}{c}{Qwen-7B\\rlap{$^\\ddagger$}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\n & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n\\midrule\n0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\\,.967] \\\\\n1v2 & .6955 & [.686,\\,.704]\\rlap{$^*$} & .6539 & [.645,\\,.663]\\rlap{$^*$} & .6145 & [.605,\\,.625]\\rlap{$^*$} & .6112 & [.602,\\,.621]\\rlap{$^*$} & .6168 & [.608,\\,.626]\\rlap{$^*$} \\\\\n2v3 & .5893 & [.580,\\,.599] & .5514 & [.542,\\,.563] & .5496 & [.540,\\,.560] & .5609 & [.551,\\,.571] & .5492 & [.539,\\,.559] \\\\\n3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\\\\n4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & \\\\\n\\bottomrule\n\\multicolumn{11}{l}{\\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\\\\n\\multicolumn{11}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.}\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_auc_decay.pdf}\n\\caption{Pairwise $\\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\\theta = 0.60$.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:kstar_ci} and Figure~\\ref{fig:auc_decay} show $\\Kempirical \\leq 2$ across all 9 model configurations: 8/9 yield $\\Kempirical{=}2$ (1v2 $\\auc$ range: 0.6112--0.6955; all CI lower bounds $> \\theta$; permutation $p < 0.001$), while Mistral-7B is the only exception ($\\Kempirical{=}1$; 1v2 $\\auc = 0.594$, below $\\theta$; Section~\\ref{sec:boundary_cases}).\nLLaMA-3.1-8B yields $\\Kempirical{=}2$ (0v1 $\\auc = 0.9225$, 1v2 $\\auc = 0.6123$, 95\\% CI $[0.603, 0.622]$; borderline: 1/5 folds falls below $\\theta$; Table~\\ref{tab:kstar_ci_extended}).\nAll four decoding strategies likewise yield $\\Kempirical{=}2$ (Table~\\ref{tab:s2_decoding}).\nThe 1v2 spread due to generation mode ($\\Delta = 8.4$\\,pp within Qwen) exceeds the spread across models in continuation mode ($\\Delta = 3.9$\\,pp).\n\n\\paragraph{Scale and instruction-tuning invariance.}\n$\\Kempirical{=}2$ persists from 1.5B through 14B: Qwen-14B (1v2 $\\auc = 0.621$ $[0.612, 0.630]$), Qwen-7B ($0.6168$ $[0.608, 0.626]$), and LLaMA-3.1-8B ($0.6123$) all exceed $\\theta$, despite progressively reduced 0v1 signal (0.960 at 14B, 0.964 at 7B, 0.923 at 8B vs.\\ $> 0.99$ at $\\leq$1.5B).\nA base-vs.-instruct ablation at 1.5B likewise yields $\\Kempirical = 2$ (1v2 $\\auc = 0.626$); the boundary is not an instruction-tuning artifact.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_kstar_theta.pdf}\n\\caption{$\\Kempirical(\\theta)$ sensitivity curve for six configurations. $\\Kempirical$: maximum discriminable depth; $\\theta$: AUC decision threshold. All configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (dashed line). At $\\theta{=}0.70$, all drop to $\\Kempirical{=}1$.}\n\\label{fig:kstar_theta}\n\\end{figure}\n\nFigure~\\ref{fig:kstar_theta} shows $\\Kempirical$ as a function of $\\theta$: web text $\\Kempirical{=}2$ is stable across a 5\\,pp window ($\\theta \\in [0.575, 0.625]$), with a gradual transition to $\\Kempirical{=}3$ at $\\theta{=}0.55$ (two Qwen configurations) and $\\Kempirical{=}1$ at $\\theta{=}0.70$.\nThe domain ordering (arXiv $>$ web $\\geq$ cross-scorer) is preserved across the full $\\theta$ range (Table~\\ref{tab:theta_sensitivity}; Figure~\\ref{fig:theta_sensitivity} in Appendix shows the complete model $\\times$ domain $\\theta$ sensitivity).\nAll four decoding strategies likewise yield $\\Kempirical = 2$ at $\\theta{=}0.60$ (1v2 $\\auc \\in [0.687, 0.704]$; Table~\\ref{tab:s2_decoding}).\n\n%% ====================================================================\n\\subsection{Largely Generator-Independent Transfer}\n\\label{sec:transfer}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig3_transfer_heatmap.pdf}\n\\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\\leftrightarrow$OLMo: 90--92\\%; Qwen-rewrite$\\to$continuation: 61--63\\%.}\n\\label{fig:transfer_heatmap}\n\\end{figure}\n\nContinuation-mode classifiers transfer well across generators (Figure~\\ref{fig:transfer_heatmap}; full matrix in Table~\\ref{tab:s1_transfer}): Pythia$\\leftrightarrow$OLMo retains 90--92\\%, Qwen-cont$\\leftrightarrow$Pythia 84--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\% (0v1 cross-model $\\auc > 0.96$ for all pairs).\nQwen-rewrite classifiers transfer poorly (61--63\\%), consistent with reliance on mode-specific artifacts rather than generalizable depth features.\n\n\\paragraph{Cross-scorer validation.}\nReplacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\\rho > 0.90$; Table~\\ref{tab:crossscorer}).\n$\\Kempirical$ is largely robust to scorer choice: across 22 cross-scorer configurations on C4 and arXiv, $\\Kempirical$ was preserved in 20 cases; the two exceptions (Qwen-cont scored by Pythia on C4, Qwen-7B cross-scored on arXiv) are borderline, with AUC within 0.002 of $\\theta$.\nQwen-cont is the most scorer-sensitive continuation-mode configuration: its self-scored 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp (Table~\\ref{tab:kstar_ci}), and cross-family scoring pushes it below $\\theta$.\nFor arXiv, cross-scoring with Pythia-1.4B preserves $\\Kempirical{=}3$ for three of four generators (Qwen-1.5B, LLaMA-8B, Mistral-7B; 2v3 $\\auc$ range: 0.608--0.632).\nQwen-7B exhibits a borderline decrease to $\\Kempirical{=}2$ (2v3 $\\auc = 0.599$ vs.\\ $0.626$ self-scored, $\\Delta = -2.7$\\,pp; 3/5 folds above $\\theta$), consistent with the Qwen family's scorer sensitivity observed on C4 and Wikipedia.\nBootstrap CIs (10{,}000 resamples) confirm $\\Kempirical{=}3$ for Qwen-1.5B (CI lower $= 0.617$) and LLaMA-8B (CI lower $= 0.605$); for Mistral-7B (CI: $[0.593, 0.622]$) and Qwen-7B (CI: $[0.584, 0.613]$), the CI straddles $\\theta$; their $\\Kempirical{=}3$ assignment is sensitive to resampling variance (Table~\\ref{tab:arxiv_crossscorer_ci}).\nA three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair; $N{=}300$; Table~\\ref{tab:anova_crossscorer}) confirms that Depth-Pair dominates variance ($\\eta^2_p = 0.998$); Scorer is statistically significant ($p < .001$) but practically minor ($\\eta^2_p = 0.192$), consistent with a detectable but small scorer influence on absolute discriminability.\n\n%% ====================================================================\n\\subsection{Feature Ordering and Generation Mode}\n\\label{sec:feature_degradation}\n\\label{sec:generation_mode}\n\nAmong continuation-mode models, single-feature $\\auc$ rankings are highly correlated ($\\rho \\geq 0.85$; Table~\\ref{tab:top_features}).\nThe top-3 features (\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std}, \\texttt{surp\\_d2\\_std}) are shared across all three families: autoregressive generation progressively damps surprisal variability; however, no single feature subset of size ${<}8$ reliably sustains $\\Kempirical{=}2$ (Appendix~\\ref{sec:feature_subset}).\nA feature group ablation (Appendix~\\ref{sec:feature_ablation}) confirms that surprisal (base) dominates on arXiv (single AUC $= 0.809$, LOO $\\Delta = 0.031$); on C4 and Wikipedia, all LOO drops fall within fold variance ($\\leq 0.007$).\nQwen-rewrite diverges (\\texttt{freq\\_entropy} dominates), consistent with its poor cross-model transfer (61--63\\%).\nWithin Qwen, rewrite yields 1v2 $\\auc = 0.6955$ vs.\\ continuation's $0.6112$ ($\\Delta = +8.4$\\,pp); continuation mode is therefore recommended as the canonical condition.\n\n%% ====================================================================\n\\subsection{Neural Probe}\n\\label{sec:neural_probe}\n\nReplacing the 15D features with frozen encoder hidden states (MLP probe, 5{,}000 texts per depth; Table~\\ref{tab:neural_probe_crossmodel}), Qwen achieves $\\Kempirical^{\\text{neural}} = 3$ (2v3 $\\auc = 0.6159$), while Pythia and OLMo remain at $\\Kempirical^{\\text{neural}} = 2$ ($\\auc_{2v3}$: 0.5963, 0.5892).\nThe Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~\\ref{sec:transfer}); the 15D features yield consistent $\\Kempirical = 2$ across all families.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\footnotesize\n\\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\\ $d{+}1$ text. $\\Kempirical^{\\text{neural}}$: maximum depth where AUC exceeds $\\theta = 0.60$.}\n\\label{tab:neural_probe_crossmodel}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & $\\Kempirical^{\\text{neural}}$ \\\\\n\\midrule\nQwen-1.5B  & 0.6159 & $[0.610,\\,0.622]$ & 3 \\\\\nPythia-1.4B & 0.5963 & $[0.589,\\,0.603]$ & 2 \\\\\nOLMo-1B    & 0.5892 & $[0.582,\\,0.597]$ & 2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{minipage}\n\n%% ====================================================================\n\\subsection{Cross-Domain Variation}\n\\label{sec:cross_domain}\n\nThe preceding experiments use C4 (general web text).\nTo test whether $\\Kempirical$ reflects domain structure or model identity, we evaluate on arXiv abstracts ($n{=}2{,}200$ per model) and Wikipedia ($n{=}5{,}000$ per model) across six model configurations spanning four architecture families (Table~\\ref{tab:domain_kstar}).\n\n\\paragraph{arXiv ($\\Kempirical{=}3$): five-model cross-validation.}\nAll five domain-competent models yield $\\Kempirical{=}3$ on arXiv, with boundary-pair $\\auc$ (2v3) ranging from 0.6215 to 0.6545, all exceeding $\\theta$.\nThe elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\\ ${\\sim}0.01$ for C4): formulaic features (LaTeX formatting, citation patterns, mathematical notation) degrade slowly under autoregressive generation and supply persistent depth signal across four architecture families and 1.4B--8B parameters.\nRemoving LaTeX markup reduces 2v3 AUC by ${\\sim}$1.8\\,pp but preserves $\\Kempirical{=}3$ (CI lower $= 0.610 > \\theta$; Table~\\ref{tab:latex_ablation}); content-level properties dominate.\nOLMo-1B constitutes a capacity failure rather than a counter-example; its arXiv generations are entirely out-of-domain (0v1 JSD $= 0.33$, near-total information loss at the first step), yielding $\\Kempirical{=}1$.\nMistral-7B provides the strongest domain-dependence evidence: $\\Kempirical{=}1$ on C4 (Section~\\ref{sec:boundary_cases}) but $\\Kempirical{=}3$ on arXiv: domain structure alone can shift $\\Kempirical$ by two levels within the same model.\n\n\\paragraph{Wikipedia ($\\Kempirical{=}1$): single-generation saturation.}\nWith scorer confound controlled (Pythia-1.4B for Qwen generators; Qwen-1.5B, itself cross-family, for all others), all six models yield $\\Kempirical{=}1$ on Wikipedia: 1v2 $\\auc$ ranges from 0.499 (OLMo) to 0.595 (LLaMA), all below $\\theta$.\nWikipedia represents the simplest domain tested; its encyclopedic regularity provides minimal structural signal beyond the 0v1 boundary, and a single generation pass suffices for complete saturation.\nA same-family scorer confound inflates the apparent $\\Kempirical$ for Qwen generators: Qwen-1.5B scoring yields $\\Kempirical{=}2$ (1v2 $\\auc \\approx 0.61$--$0.62$), but cross-family scoring reduces 1v2 by 2.4\\,pp to below $\\theta$ (Appendix~\\ref{sec:wiki_domain}).\nThis +1 depth bias under same-family scoring is specific to Qwen generators on Wikipedia and does not affect C4 results (Section~\\ref{sec:transfer}).\n\n\\paragraph{Code ($\\Kempirical{=}1$--$2$): cross-modality confirmation.}\nPython functions from CodeSearchNet~\\cite{husain2019codesearchnet} ($n{=}5{,}000$) yield $\\Kempirical{=}2$ for Qwen2.5-1.5B (1v2 $\\auc = 0.738$, CI $[0.709, 0.767]$; 2v3 $\\auc = 0.530$; Table~\\ref{tab:code_domain_qwen}) and borderline $\\Kempirical{=}1$ for Pythia-1.4B (1v2 $\\auc = 0.598$, CI $[0.593, 0.603]$; Table~\\ref{tab:code_crossmodel_kstar}).\nQwen code matches C4 despite a different modality: higher 1v2 AUC (0.74 vs.\\ 0.61--0.70) but the same sharp 2v3 collapse (JSD ratio $11.7\\times$).\nPythia's code 1v2 falls just below $\\theta$ (CI upper $= 0.603$), consistent with its lower code-generation capacity relative to general web text.\n\n\\paragraph{Domain as the primary factor.}\nWith the scorer confound controlled, the domain ordering is: arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $\\geq$ Code ($\\Kempirical{=}1$--$2$) $\\geq$ Wikipedia ($\\Kempirical{=}1$).\nScale (1B--14B) and architecture do not alter the C4/arXiv/Wikipedia ordering; code shows model-dependent variation at the boundary, but domain structural complexity remains the primary determinant of $\\Kempirical$.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\footnotesize\n\\captionof{table}{Domain $\\times$ Model $\\Kempirical$ matrix (scorer-controlled). Wikipedia values use cross-family scorer (Pythia-1.4B). $^*$OLMo arXiv: capacity failure. $^\\dagger$Same-family scorer yields $\\Kempirical{=}2$; controlled value shown. $^\\ddagger$Borderline: 1v2 $\\auc = 0.598$, CI upper $= 0.603 > \\theta$.}\n\\label{tab:domain_kstar}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{C4} & \\textbf{Code} & \\textbf{arXiv} & \\textbf{Wikipedia} \\\\\n\\midrule\nQwen-1.5B    & 2 & 2 & 3 & 1$^\\dagger$ \\\\\nQwen-7B      & 2 & --- & 3 & 1$^\\dagger$ \\\\\nPythia-1.4B  & 2 & 1$^\\ddagger$ & 3 & 1 \\\\\nOLMo-1B      & 2 & --- & 1$^*$ & 1 \\\\\nLLaMA-3.1-8B & 2 & --- & 3 & 1 \\\\\nMistral-7B   & 1 & --- & 3 & 1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{minipage}\n\n%% ====================================================================\n\\subsection{Binary Detector Confidence}\n\\label{sec:binary_confidence}\n\nBinary detectors (DivEye~\\cite{basani2026diveye}, Binoculars~\\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\\rho| = 0.06$--$0.46$; Table~\\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\\leq 0.199$ vs.\\ 0.167 baseline), pairwise $\\auc$ yields $\\Kempirical^{\\text{binary}} \\leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.\nThe observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.\n",
    "structuredPatch": [
      {
        "oldStart": 13,
        "oldLines": 7,
        "newStart": 13,
        "newLines": 7,
        "lines": [
          " \\centering",
          " \\small",
          " \\caption{Pairwise $\\auc$ for adjacent depth pairs with bootstrap 95\\% CIs and permutation $p$-values for boundary rows.",
          "-$\\Kempirical = 2$ requires 1v2 $\\auc > \\theta{=}0.60$ and 2v3 $\\auc < \\theta$; CIs quantify boundary uncertainty.",
          "+$\\Kempirical = 2$ requires 1v2 CI lower bound $> \\theta{=}0.60$ and 2v3 CI lower bound $\\leq \\theta$ (Eq.~\\ref{eq:kstar}).",
          " Extended results (all models) in Table~\\ref{tab:kstar_ci_extended}.}",
          " \\label{tab:kstar_ci}",
          " \\begin{tabular}{lcccccccccc}"
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

_source line 33_

<details open><summary>🔧 Tool call — Edit · `toolu_01SrAi6mBFMxY3chR1DfghA4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "old_string": "$K^*$: max $k$ where $k$v$(k{+}1)$ AUC $\\geq \\theta = 0.60$.}",
  "new_string": "$K^*$: max $k$ where $k$v$(k{+}1)$ CI lower bound $> \\theta = 0.60$ (Eq.~\\ref{eq:kstar}).}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "0eff22c5-5e4f-4b5c-bc00-23f027214a0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1tQRxZZydE8v2TUenYcE1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3576,
      "cache_read_input_tokens": 40282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3576
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

_source line 34 · 2026-05-19T06:29:31.024Z_

<details><summary>↩ Tool result · `toolu_01SrAi6mBFMxY3chR1DfghA4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "016ad954-c501-401f-99cd-f596d570c487",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "oldString": "$K^*$: max $k$ where $k$v$(k{+}1)$ AUC $\\geq \\theta = 0.60$.}",
    "newString": "$K^*$: max $k$ where $k$v$(k{+}1)$ CI lower bound $> \\theta = 0.60$ (Eq.~\\ref{eq:kstar}).}",
    "originalFile": "\\section{Extended Analysis and Limitations}\n\\label{sec:extended_discussion}\n\nThis section provides supporting tables for cross-scorer validation (Tables~\\ref{tab:crossscorer}--\\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\rho > 0.90$) and rewrite-mode $\\Kempirical = 2$, but reduce continuation-mode $\\Kempirical$ from 2 to 1.}\n\\label{tab:crossscorer}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_crossscorer}}\n\\end{minipage}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair) on per-fold pairwise $\\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\\times$ 5 folds $\\times$ 5 depth-pairs; 3 generators $\\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\\eta^2_p = 0.19$) relative to Depth-Pair ($\\eta^2_p = 1.00$) and Generator ($\\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination (Scorer $\\eta^2_p$ is approximately 5$\\times$ smaller than Generator and dwarfed by Depth-Pair). Per-fold AUC values within the same generator share seed documents across folds and are not fully independent; we therefore rely on effect-size ratios rather than $p$-values for interpretation.}\n\\label{tab:anova_crossscorer}\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Source} & \\textbf{df} & $F$ & $p$ & $\\eta^2_p$ \\\\\n\\midrule\nGenerator     & 2  & 926.8  & ${<}.001$  & .885 \\\\\nScorer        & 3  & 19.02  & ${<}.001$  & .192 \\\\\nDepth-Pair    & 4  & 24736  & ${<}.001$  & .998 \\\\\nGen$\\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\\\\nGen$\\times$Depth  & 8 & 993.7 & ${<}.001$ & .971 \\\\\nScorer$\\times$Depth & 12 & 2.45 & .005 & .109 \\\\\nResidual      & 240 & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Extended Limitations}\n\\label{sec:extended_limitations}\n\n\\emph{Prompt-chain versus retrain-chain.}\nBoth Qwen2.5-1.5B and Pythia-1.4B yield $\\Kempirical{=}7$ under retrain-chain LoRA fine-tuning (Table~\\ref{tab:retrain_ci}), extending detectable depth by 5 additional generations beyond prompt-chain $\\Kempirical{=}2$.\nCumulative model-adaptation artifacts (vocabulary narrowing, repetition bias) make each retrained generation highly distinguishable.\nThe two models exhibit different decay profiles: Pythia achieves higher early-pair AUC (1v2: 0.947 vs.\\ 0.897) but drops more steeply at deeper pairs (4v5: 0.691 vs.\\ 0.746), yet both converge to $\\Kempirical{=}7$ (6v7: Qwen 0.641, Pythia 0.634; both CI lower bounds $> \\theta$).\nThis convergence despite differences in effective LoRA adaptation capacity (Pythia uses fused QKV attention with rank-16 vs.\\ Qwen's separate Q/K/V projections) indicates robustness to LoRA parameterization.\nThe extended discriminability under retraining aligns with theoretical analyses of iterative retraining instability on synthetic data~\\cite{bertrand2024stability, gerstgrasser2024model}, where each retraining cycle amplifies distributional artifacts beyond the text-intrinsic degradation observed in prompt-chains.\nExtrapolating yields 7v8 $\\approx 0.57 < \\theta$ for both models, suggesting $\\Kempirical{=}7$ is near the ceiling.\nPrompt-chain $\\Kempirical$ represents the operationally relevant boundary for data curation (text-intrinsic information loss); retrain-chain $\\Kempirical$ represents the upper bound achievable via model archaeology (known training pipeline).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Retrain-chain pairwise $\\auc$ with 5-fold CV 95\\% CIs. Both models yield $\\Kempirical{=}7$; all CI lower bounds $> \\theta{=}0.60$. Retrain-chain CIs use fold-level estimates (Section~\\ref{sec:retrain_ci_note}).}\n\\label{tab:retrain_ci}\n\\begin{tabular}{lcccc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{Qwen-1.5B}} & \\multicolumn{2}{c}{\\textbf{Pythia-1.4B}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\n\\textbf{Pair} & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n\\midrule\n0v1 & 0.9837 & $[.982,\\,.985]$ & 0.9844 & $[.983,\\,.986]$ \\\\\n1v2 & 0.8971 & $[.895,\\,.899]$ & 0.9470 & $[.942,\\,.952]$ \\\\\n2v3 & 0.8098 & $[.805,\\,.814]$ & 0.8891 & $[.882,\\,.896]$ \\\\\n3v4 & 0.7600 & $[.753,\\,.767]$ & 0.7999 & $[.795,\\,.805]$ \\\\\n4v5 & 0.7459 & $[.738,\\,.754]$ & 0.6907 & $[.688,\\,.693]$ \\\\\n5v6 & 0.7017 & $[.696,\\,.708]$ & 0.6497 & $[.643,\\,.657]$ \\\\\n6v7 & 0.6410 & $[.638,\\,.645]$ & 0.6340 & $[.628,\\,.641]$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{CI methodology note.}\n\\label{sec:retrain_ci_note}\nThe main pipeline reports bootstrap 95\\% CIs (1{,}000 or 10{,}000 resamples), which are valid because each bootstrap sample preserves the GroupKFold document structure: resampling operates on documents, and all depths of a given document remain together.\nIn the retrain-chain setting, each generation's training corpus is the \\emph{output} of the previous generation's fine-tuned model. This creates inter-generation dependencies that standard bootstrap resampling cannot preserve, and naive resampling would inflate AUC estimates.\nWe therefore report fold-based 95\\% CIs for retrain-chain experiments, computed as $\\bar{x} \\pm 1.96 \\cdot s / \\sqrt{K}$ from the $K{=}5$ GroupKFold AUC values.\n\n\\emph{Threshold sensitivity.}\nTable~\\ref{tab:theta_sensitivity} reports $\\Kempirical$ across $\\theta \\in [0.55, 0.70]$ for representative configurations including arXiv and cross-scorer conditions.\nQwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp; all ten boundary comparisons yield permutation $p < 0.001$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{$\\Kempirical$ as a function of $\\theta$ across conditions. The \\textbf{domain ordering} (arXiv $>$ web $\\geq$ cross-scorer) and \\textbf{bounded range} ($\\Kempirical{\\leq}4$) are preserved across $\\theta \\in [0.55, 0.70]$. The headline result (web $\\Kempirical{=}2$, arXiv $\\Kempirical{=}3$) holds for $\\theta \\in [0.575, 0.625]$.}\n\\label{tab:theta_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Config} & $\\theta{=}0.55$ & $\\theta{=}0.60$ & $\\theta{=}0.625$ & $\\theta{=}0.70$ \\\\\n\\midrule\nC4 (web) & Qwen-rw      & 3 & 2 & 2 & 1 \\\\\nC4 (web) & Pythia       & 2 & 2 & 2 & 1 \\\\\nC4 (web) & OLMo         & 2 & 2 & 1 & 1 \\\\\nC4 (web) & Qwen-cont    & 3 & 2 & 2 & 1 \\\\\nC4 (web) & Qwen-7B      & 2 & 2 & 2 & 1 \\\\\nC4 (web) & Mistral-7B   & 1 & 1 & 1 & 1 \\\\\n\\midrule\narXiv    & Qwen-1.5B-base (cont.) & 4 & 3 & 3 & 2 \\\\\narXiv    & Pythia-1.4B (cont.)    & 4 & 3 & 3 & 2 \\\\\n\\midrule\nCross-scorer & Qwen-cont/Pythia-scored & 2 & 1 & 1 & 1 \\\\\nCross-scorer & Qwen-cont/OLMo-scored   & 2 & 1 & 1 & 1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_theta_sensitivity.pdf}\n\\caption{$\\Kempirical$ as a function of $\\theta$ across all model $\\times$ domain configurations (three panels: C4, arXiv, Wikipedia). The domain ordering (Wikipedia $\\Kempirical{\\leq}1$ $<$ C4 $\\Kempirical{\\leq}2$ $<$ arXiv $\\Kempirical{\\leq}3$) is preserved across the full $\\theta \\in [0.55, 0.70]$ range. Within each domain, inter-model variation is small relative to inter-domain differences, confirming that source domain rather than model identity governs $\\Kempirical$.}\n\\label{fig:theta_sensitivity}\n\\end{figure}\n\n\\emph{Structural confound: token length.}\nIn continuation mode the generation prompt is discarded, so all depths $\\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\\ machine-generated prompt), not structural composition.\nDepth~0 texts average ${\\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\\ref{tab:token_length}).\nThis asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.\nWithin depths 1--5, mean token counts are stable (within-model range $\\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\\Kempirical{=}2$ are unaffected by length.\nEOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\\%, Pythia 34--36\\%, OLMo $<$1\\%, Qwen-continuation 17--20\\%, Qwen-7B 45--47\\%.\nModels with the highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\\ref{tab:kstar_ci}), EOS truncation therefore does not drive the boundary.\n\n\\emph{Graduated filtering.}\nAll $\\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\\alpha{=}0.1$: 0.5873; $\\alpha{=}0.9$: 0.5892 vs.\\ 0.5941); at $\\alpha{=}0.9$, HellaSwag matches exactly (0.6701).\nBinary-ours significantly outperforms all alternatives on MMLU ($p_{\\text{corr}} \\leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\\text{corr}} = 0.011$).\n\\label{tab:pairwise_significance}\n\n\\subsection{Dose-Response: Contamination Ratio Effect}\n\\label{sec:dose_response}\n\nThe main filtering experiments (Section~\\ref{sec:filtering}) use 100\\% synthetic data to maximize effect size.\nTo characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\\%, 30\\%, and 50\\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\\ref{tab:dose_response}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MMLU and HellaSwag by contamination ratio and filtering strategy (5 seeds, mean $\\pm$ std). Base model MMLU: 0.6018. Binary filtering retains a significant advantage on HellaSwag across all ratios ($p \\leq 0.004$, Holm-Bonferroni corrected).}\n\\label{tab:dose_response}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{10\\%}} & \\multicolumn{2}{c}{\\textbf{30\\%}} & \\multicolumn{2}{c}{\\textbf{50\\%}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\n\\textbf{Strategy} & MMLU & HellaSwag & MMLU & HellaSwag & MMLU & HellaSwag \\\\\n\\midrule\nNo-filter   & $.6058{\\pm}.0002$ & $.6689{\\pm}.0006$ & $.6069{\\pm}.0007$ & $.6664{\\pm}.0018$ & $.6063{\\pm}.0012$ & $.6680{\\pm}.0005$ \\\\\nBinary-ours & $\\mathbf{.6079{\\pm}.0004}$ & $\\mathbf{.6727{\\pm}.0007}$ & $\\mathbf{.6082{\\pm}.0011}$ & $\\mathbf{.6725{\\pm}.0006}$ & $\\mathbf{.6088{\\pm}.0009}$ & $\\mathbf{.6731{\\pm}.0004}$ \\\\\nGraduated   & $.6066{\\pm}.0010$ & $.6700{\\pm}.0014$ & $.6072{\\pm}.0008$ & $.6665{\\pm}.0012$ & $.6062{\\pm}.0008$ & $.6679{\\pm}.0001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt all tested ratios (10--50\\%), no-filter MMLU remains above the base model (0.6018), synthetic data at these proportions is therefore net-beneficial rather than harmful.\nBinary filtering consistently improves over no-filter, with HellaSwag differences significant across all ratios ($p \\leq 0.004$, Holm-Bonferroni corrected).\nMMLU differences are smaller and significant only at 10\\% after correction ($p = 0.001$).\nGraduated weighting is indistinguishable from no-filter at all ratios (MMLU $p \\geq 0.27$; HellaSwag $p \\geq 0.06$), depth assignments beyond $\\Kempirical$ therefore inject noise regardless of contamination severity.\nEffect sizes diminish 3--6$\\times$ relative to the 100\\% setting (Section~\\ref{sec:filtering}), but the strategy ordering (binary $>$ graduated $\\approx$ no-filter) is preserved.\n\n\\subsection{Cross-Model Filtering Replication}\n\\label{sec:pythia_filtering}\n\nTo test whether $\\Kempirical{=}2$ correctly predicts optimal curation granularity across architectures, we replicate the filtering experiment on Pythia-1.4B (LoRA rank 8, nucleus $p{=}0.9$, $T{=}1.0$, 3 seeds; Table~\\ref{tab:pythia_filtering}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pythia-1.4B filtering replication (3 seeds, mean $\\pm$ std). Strategy ordering matches Qwen (binary $>$ no-filter $>$ graduated on MMLU).}\n\\label{tab:pythia_filtering}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Strategy} & \\textbf{MMLU} & \\textbf{HellaSwag} \\\\\n\\midrule\nNo-filter & $.2568{\\pm}.0012$ & $.5250{\\pm}.0008$ \\\\\nBinary-ours & $\\mathbf{.2585{\\pm}.0004}$ & $.5251{\\pm}.0001$ \\\\\nGraduated$_{0.9}$ & $.2561{\\pm}.0009$ & $\\mathbf{.5253{\\pm}.0007}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe strategy ordering (binary $>$ no-filter $>$ graduated on MMLU) matches Qwen (Section~\\ref{sec:filtering}).\nThe small absolute differences reflect the model's near-chance MMLU baseline rather than filtering inefficacy; the consistent ordering across two architectures supports $\\Kempirical{=}2$'s predictive value for curation granularity.\nHellaSwag differences are negligible across all strategies.\n\n\\subsection{Feature Subset Stability}\n\\label{sec:feature_subset}\n\nTo test whether $\\Kempirical{=}2$ depends on the specific 15D feature combination, we evaluate random feature subsets of varying size on Pythia-1.4B prompt-chain data (Table~\\ref{tab:feature_subset}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{1v2 $\\auc$ by feature subset size (Pythia-1.4B). $\\Kempirical{=}2$ ($\\auc > \\theta{=}0.60$) is robust at $\\geq$8 features.}\n\\label{tab:feature_subset}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Subset} & \\textbf{Tested} & \\textbf{Pass} & \\textbf{Min $\\auc$} & \\textbf{Mean $\\auc$} \\\\\n\\midrule\n15D (full) & 1 & 1 & 0.6262 & 0.6262 \\\\\n10D        & 5 & 5 & 0.6153 & 0.6191 \\\\\n8D         & 5 & 5 & 0.6056 & 0.6159 \\\\\n5D         & 5 & 2 & 0.5856 & 0.5998 \\\\\n3D (top-3) & 1 & 0 & 0.5871 & 0.5871 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n$\\Kempirical{=}2$ holds for all subsets of size $\\geq$8 (10/10 pass, min $\\auc = 0.6056$), becomes fragile at 5D (2/5 pass), and fails at 3D (top-3 surprisal features alone: $\\auc = 0.5871 < \\theta$).\nThe boundary does not depend on any specific feature combination but requires sufficient dimensionality ($\\geq$8) to capture the multi-faceted distributional shift between generations 1 and 2.\n\n\\subsection{self\\_BLEU Feature Independence}\n\\label{sec:selfbleu_ablation}\n\nTo verify that $\\Kempirical$ does not depend on the self\\_BLEU feature (which may reflect stylistic repetition rather than depth-correlated degradation), we compare 15D and 14D (self\\_BLEU removed) classifiers across four model configurations (Table~\\ref{tab:selfbleu_ablation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{15D vs.\\ 14D (self\\_BLEU removed) 1v2 $\\auc$ with bootstrap 95\\% CIs. Removing self\\_BLEU does not change $\\Kempirical$ for any configuration. Maximum $|\\Delta\\auc| = 0.0031$, within bootstrap CI width (${\\sim}0.018$).}\n\\label{tab:selfbleu_ablation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & $\\Kempirical$ & \\textbf{15D $\\auc$ [CI]} & \\textbf{14D $\\auc$ [CI]} & $\\Delta$ \\\\\n\\midrule\nQwen-base   & 2/2 & $.6288$ $[.620,\\,.638]$ & $.6258$ $[.616,\\,.635]$ & $-.0031$ \\\\\nPythia-1.4B  & 2/2 & $.8840$ $[.878,\\,.890]$ & $.8830$ $[.876,\\,.889]$ & $-.0010$ \\\\\nLLaMA-8B     & 2/2 & $.6075$ $[.598,\\,.617]$ & $.6074$ $[.598,\\,.617]$ & $-.0001$ \\\\\nMistral-7B   & 1/1 & $.5902$ $[.580,\\,.600]$ & $.5903$ $[.580,\\,.600]$ & $+.0002$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAll four configurations preserve their $\\Kempirical$ under 14D, with negligible AUC change ($|\\Delta| \\leq 0.003$).\nThe self\\_BLEU feature contributes minimally to the depth boundary; $\\Kempirical{=}2$ is driven by surprisal and entropy features rather than lexical repetition statistics.\n\n\\subsection{Wikipedia Domain: Scorer Confound Resolution}\n\\label{sec:wiki_domain}\n\nUnder same-family scoring (Qwen-1.5B scorer), Wikipedia $\\Kempirical$ appeared to exhibit model-family dependence: Qwen generators (1.5B and 7B) yielded $\\Kempirical{=}2$, while all four non-Qwen models yielded $\\Kempirical{=}1$ (Table~\\ref{tab:wiki_domain}).\nA scorer confound ablation resolves this apparent split.\nRescoring the same Qwen-7B Wikipedia text with Pythia-1.4B reduces 1v2 $\\auc$ from $0.611$ to $0.587$ ($\\Delta = -2.4$\\,pp), dropping $\\Kempirical$ from 2 to 1.\nWith the scorer confound controlled, all six models yield $\\Kempirical{=}1$ on Wikipedia, and the domain ordering simplifies to: arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $>$ Wikipedia ($\\Kempirical{=}1$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Wikipedia pairwise $\\auc$ across 6 models. $^\\dagger$Qwen rows use same-family scorer (Qwen-1.5B); cross-family scoring (Pythia-1.4B) reduces Qwen-7B to $\\Kempirical{=}1$ ($\\Delta = -2.4$\\,pp), resolving the apparent family split.}\n\\label{tab:wiki_domain}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Family} & \\textbf{0v1} & \\textbf{1v2} & \\textbf{2v3} & $\\Kempirical$ & \\textbf{Scorer} \\\\\n\\midrule\nQwen-1.5B (base) & Qwen & ---  & .619 & .550 & 2$^\\dagger$ & Qwen-1.5B \\\\\nQwen-1.5B (base) & Qwen & ---  & .599 & ---  & 1 & Pythia-1.4B \\\\\nQwen-7B          & Qwen & .967 & .611 & .556 & 2$^\\dagger$ & Qwen-1.5B \\\\\nQwen-7B          & Qwen & ---  & .587 & ---  & 1 & Pythia-1.4B \\\\\n\\midrule\nPythia-1.4B   & non-Qwen & .975 & .585 & .545 & 1 & Qwen-1.5B \\\\\nOLMo-1B       & non-Qwen & .993 & .499 & .501 & 1 & Qwen-1.5B \\\\\nLLaMA-3.1-8B  & non-Qwen & .932 & .595 & .539 & 1 & Qwen-1.5B \\\\\nMistral-7B    & non-Qwen & .961 & .555 & .524 & 1 & Qwen-1.5B \\\\\n\\bottomrule\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$Same-family scorer; cross-family scoring yields $\\Kempirical{=}1$.}\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Per-fold transparency.}\nFor Qwen-1.5B, cross-family scoring (Pythia-1.4B) yields $\\auc$(1v2) $= 0.5994$, with per-fold values $[0.596, 0.606, 0.600, 0.603, 0.592]$ (2/5 folds marginally above $\\theta = 0.60$).\nThe aggregate mean falls below $\\theta$, confirming $\\Kempirical{=}1$.\nFor Qwen-7B, the corresponding $\\auc$ drops further to $0.587$.\n\n\\subsection{ArXiv Cross-Scorer Bootstrap CIs}\n\\label{sec:arxiv_crossscorer_ci}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}\n\\label{tab:arxiv_crossscorer_ci}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Generator} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & \\textbf{CI lower $> \\theta$} \\\\\n\\midrule\nQwen-1.5B    & 0.632 & $[0.617,\\,0.646]$ & Yes \\\\\nLLaMA-3.1-8B & 0.620 & $[0.605,\\,0.636]$ & Yes (0.5\\,pp margin) \\\\\nMistral-7B   & 0.608 & $[0.593,\\,0.622]$ & No \\\\\nQwen-7B      & 0.599 & $[0.584,\\,0.613]$ & No \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{JSD Decay Analysis}\n\\label{sec:jsd_extended}\n\nThe token-level JSD between adjacent generations reveals two distinct decay regimes (Figure~\\ref{fig:jsd_decay}).\nFor C4 web text, 0v1 JSD exceeds 1v2 by 6--56$\\times$ across all 8 models (1B--14B) with $\\Kempirical{=}2$ (median cliff ratio ${\\sim}$15$\\times$), and subsequent pairs converge to a noise floor of ${\\sim}$0.003--0.005.\nFitting $\\jsd(k, k{+}1) \\propto e^{-\\lambda k}$ yields $\\lambda \\approx 2.2$--$3.5$ for C4 (mean ${\\approx}\\,2.9$), consistent with rapid mixing of $G_\\delta$ toward its stationary distribution.\nThese decay rates represent qualitative characterizations from 5-point curves rather than precise estimates.\nThe empirical decay rate $\\lambda$ is consistent within each domain but varies across domains: C4 yields $\\lambda \\approx 2.9$, Wikipedia $\\lambda \\approx 3.1$ (excluding OLMo, whose $\\lambda = 6.3$ reflects a capacity-limited collapse: 0v1 $\\jsd = 0.169$ with near-complete information loss at the first step, the exponential fit is therefore unreliable), and arXiv $\\lambda \\approx 1.0$.\nThis cross-model consistency indicates that the contraction rate of $G_\\delta$ is governed primarily by the structure of the input domain rather than the model architecture.\nArXiv text decays ${\\sim}$3$\\times$ slower than C4 ($\\lambda \\approx 1.0$ vs.\\ $2.9$), with a correspondingly higher convergence floor (${\\sim}$0.007--0.009 vs.\\ ${\\sim}$0.003--0.004).\nFormulaic structural features (LaTeX formatting, citation patterns, section templates) degrade more slowly under autoregressive generation and supply persistent depth-distinguishing signal, this accounts for the elevated $\\Kempirical{=}3$.\nThe retrain-chain exhibits a fundamentally different profile: $\\lambda = 0.285$ with a cliff ratio of only 1.31$\\times$ and no sharp drop between adjacent pairs (Figure~\\ref{fig:retrain_decay}).\nThis gradual, sustained divergence reflects cumulative model-adaptation artifacts rather than text-intrinsic information loss, further supporting the distinction between prompt-chain and retrain-chain $\\Kempirical$ (Appendix~\\ref{sec:boundary_extended}).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_retrain_decay.png}\n\\caption{Retrain-chain AUC decay across 7 generation pairs (Qwen2.5-1.5B LoRA). Unlike prompt-chain (sharp cliff at 0v1$\\to$1v2), retrain-chain AUC decays gradually from 0.984 to 0.641, with all pairs above $\\theta{=}0.60$. Error bars: 95\\% CI from 5-fold CV. Dashed line: $\\theta{=}0.60$; extrapolated 7v8 $\\approx 0.57$ (below $\\theta$), suggesting $\\Kempirical{=}7$ is near the ceiling.}\n\\label{fig:retrain_decay}\n\\end{figure}\n\n\\subsection{Boundary Cases and Scale Effect}\n\\label{sec:boundary_extended}\n\nOf 9 tested model configurations on C4, 8 yield $\\Kempirical{=}2$; Mistral-7B is the only sub-2 exception ($\\Kempirical{=}1$; 1v2 $\\auc = 0.594$, CI $[0.584, 0.603]$), validating $\\theta{=}0.60$ as an effective discriminator (gap: $0.594$ vs.\\ $0.611$--$0.696$).\nMistral's cross-domain profile reinforces the domain-governed interpretation: despite $\\Kempirical{=}1$ on both C4 and Wikipedia, it yields $\\Kempirical{=}3$ on arXiv (1v2 $\\auc = 0.820$, 2v3 $= 0.628$), and this profile persists under cross-scorer validation (Pythia-1.4B scorer: C4 $\\Kempirical{=}1$, arXiv $\\Kempirical{=}3$ (2v3 $\\auc = 0.608$, CI $[0.593, 0.622]$)), domain lexical diversity can therefore rescue even web-text one-wash generators (Table~\\ref{tab:domain_kstar}).\nLarger models produce more human-like text, reducing 0v1 JSD: 0.16--0.29 at $\\leq$1.5B, 0.077--0.13 at 7--14B.\nHowever, Qwen-14B still yields $\\Kempirical{=}2$ (1v2 $\\auc = 0.621$, CI $[0.612, 0.630]$), with 0v1 $\\auc = 0.960$ comparable to Qwen-7B ($0.964$), scale in the 1B--14B range therefore does not shift the discrimination boundary.\n\n\\paragraph{Sample-size control.}\nAs a sample-size control, subsampling C4 to $n{=}2{,}200$ (matching arXiv) yields $\\Kempirical{=}1$ (1v2 $\\auc = 0.601$, CI $[0.586, 0.616]$).\nReduced sample size widens confidence intervals and produces more conservative $\\Kempirical$ estimates, arXiv's $\\Kempirical{=}3$ at the same sample size therefore reflects genuine domain signal rather than a statistical artifact of smaller training sets.\n\n\\subsection{LaTeX Markup Ablation (arXiv)}\n\\label{sec:latex_ablation}\n\nTo disentangle content-level depth signal from formatting artifacts on arXiv, we strip all LaTeX markup (commands, environments, inline math delimiters) and re-extract features from the plain-text residual (Qwen-1.5B continuation, $n{=}2{,}200$; Table~\\ref{tab:latex_ablation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{arXiv pairwise $\\auc$ with and without LaTeX markup (Qwen-1.5B continuation). Removing formatting reduces 2v3 by ${\\sim}$1.8\\,pp but $\\Kempirical$ remains at 3 (CI lower $> \\theta$). LaTeX stripping fraction increases with depth (0.6\\% at depth 0, 4.6\\% at depth 5), deeper generations therefore produce proportionally more formatting tokens.}\n\\label{tab:latex_ablation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccr}\n\\toprule\n\\textbf{Pair} & \\textbf{Original} & \\textbf{Stripped} & $\\Delta$ \\\\\n\\midrule\n0v1 & 0.9946 & 0.9948 & $+$0.0002 \\\\\n1v2 & 0.8580 & 0.8297 & $-$0.028 \\\\\n2v3 & 0.6427 $[0.628,\\,0.658]$ & 0.6248 $[0.610,\\,0.640]$ & $-$0.018 \\\\\n3v4 & 0.5437 & 0.5468 & $+$0.003 \\\\\n\\midrule\n$\\Kempirical$ & 3 & 3 & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nContent-level statistical properties (surprisal distribution, vocabulary diversity) account for the large majority of the depth signal; LaTeX formatting contributes a modest but measurable increment (${\\sim}$1.8\\,pp at the boundary pair).\nThe depth-correlated increase in LaTeX stripping fraction (depth 0: $-$0.6\\%, depth 5: $-$4.6\\%) indicates that autoregressive generation progressively introduces formatting tokens, consistent with mode-seeking behavior in structured text.\n\n\\subsection{Statistical Power Analysis}\n\\label{sec:power_curve}\n\nTo characterize the minimum sample size required for reliable $\\Kempirical$ determination, we subsample C4 at $n \\in \\{500, 1000, 2000, 3000, 4000, 5000\\}$ and measure 1v2 AUC stability across 10 resamples per size (Qwen-1.5B-base continuation, 5-fold GroupKFold; Table~\\ref{tab:power_curve}, Figure~\\ref{fig:power_curve}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Subsampling power analysis for $\\Kempirical{=}2$ determination (C4, Qwen-1.5B-base, 10 resamples per $n$). Detection probability: fraction of resamples where 1v2 $\\auc > \\theta{=}0.60$.}\n\\label{tab:power_curve}\n\\begin{tabular}{rccc}\n\\toprule\n$n$ & \\textbf{Mean 1v2 $\\auc$} & \\textbf{Std} & \\textbf{Detection Prob.} \\\\\n\\midrule\n500 & 0.581 & 0.018 & 20\\% \\\\\n1{,}000 & 0.591 & 0.014 & 30\\% \\\\\n2{,}000 & 0.610 & 0.009 & 100\\% \\\\\n3{,}000 & 0.617 & 0.005 & 100\\% \\\\\n4{,}000 & 0.622 & 0.004 & 100\\% \\\\\n5{,}000 & 0.629 & 0.000 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_power_curve.png}\n\\caption{$\\Kempirical{=}2$ detection rate (left axis, blue) and mean 1v2 $\\auc$ (right axis, green) as a function of sample size $n$. Detection rate reaches 100\\% at $n{=}2{,}000$; the 80\\% power threshold (dotted purple) is crossed between $n{=}1{,}000$ and $n{=}2{,}000$. Error bars: $\\pm$1 std over 10 resamples. The dashed red line marks $\\theta{=}0.60$.}\n\\label{fig:power_curve}\n\\end{figure}\n\nDetection rate jumps from 20\\% ($n{=}500$) to 100\\% ($n{=}2{,}000$), with the 80\\% power threshold crossed near $n{=}1{,}500$.\nAt $n{=}5{,}000$ (the sample size used in all main experiments), variance is zero across resamples, our results are therefore well above the minimum required for reliable boundary estimation.\nThe sharp transition reflects the proximity of the 1v2 AUC to $\\theta$: small increases in $n$ reduce variance sufficiently to move all resamples above the threshold.\n\n\\subsection{Feature Group Ablation}\n\\label{sec:feature_ablation}\n\nTo assess the relative contribution of each feature group to depth discrimination, we train a plain LightGBM classifier (\\texttt{n\\_estimators}$=$200, \\texttt{max\\_depth}$=$6; distinct from the OBD-LightGBM used in Section~\\ref{sec:method}) on the 1\\,vs.\\,2 task using (a) each feature group alone (\\emph{single}) and (b) the full 15D set minus one group (\\emph{leave-one-out}).\nRepresentative models per domain: LLaMA-3.1-8B (C4), Qwen-1.5B continuation (arXiv), and the domain ablation configuration (Wikipedia).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_feature_ablation.pdf}\n\\caption{Feature group ablation heatmap for 1\\,vs.\\,2 classification AUC. \\emph{Left}: single-group performance. \\emph{Right}: leave-one-out performance. Surprisal (base) features are the dominant signal on arXiv (single AUC $= 0.809$) but provide only weak marginal signal on C4 and Wikipedia.}\n\\label{fig:feature_ablation}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Feature group ablation for 1\\,vs.\\,2 classification (AUC). \\textbf{Single}: using only features from one group. \\textbf{Leave-one-out}: removing one group from the full 15D feature set. $\\Delta$ denotes the AUC drop from the full model. Classifier: plain LightGBM (\\texttt{n\\_estimators}$=$200, \\texttt{max\\_depth}$=$6), distinct from the OBD-LightGBM pipeline; AUC values are not directly comparable to Table~\\ref{tab:kstar_ci}.}\n\\label{tab:feature_ablation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{l ccc ccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Single Group}} & \\multicolumn{3}{c}{\\textbf{Leave-One-Out ($\\Delta$)}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nFeature Group & C4 & arXiv & Wiki & C4 & arXiv & Wiki \\\\\n\\midrule\nSurprisal (base) & 0.597 & 0.809 & 0.581 & 0.601 ($-$0.007) & 0.828 ($-$0.031) & 0.616 ($-$0.003) \\\\\nSurprisal (deriv.) & 0.590 & 0.789 & 0.590 & 0.612 (+0.003) & 0.856 ($-$0.003) & 0.623 (+0.004) \\\\\nLexical diversity & 0.550 & 0.691 & 0.557 & 0.608 ($-$0.001) & 0.855 ($-$0.005) & 0.614 ($-$0.005) \\\\\nFreq. distribution & 0.533 & 0.684 & 0.564 & 0.604 ($-$0.005) & 0.851 ($-$0.009) & 0.612 ($-$0.007) \\\\\n\\midrule\nFull (15D) & 0.609 & 0.860 & 0.619 & \\multicolumn{3}{c}{---} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nSurprisal (base) features dominate on arXiv (single-group AUC $= 0.809$; LOO drop $= 0.031$, the largest across all domain--group combinations), consistent with the persistent surprisal-distribution signal in structured academic text.\nOn C4 and Wikipedia, all LOO drops are small ($\\leq 0.007$, within cross-fold standard deviation), no single feature group is therefore individually critical for the weaker low-$\\Kempirical$ signal.\nRemoving surprisal derivatives increases AUC on C4 (+0.003) and Wikipedia (+0.004), suggesting partial redundancy with the base surprisal group in low-$\\Kempirical$ domains.\n\n\\subsection{Classifier Choice: McNemar Test}\n\\label{sec:mcnemar_baselines}\n\nTo verify that depth discriminability is driven by the 15D feature representation rather than classifier choice, we compare OBD-LightGBM against three baseline classifiers (logistic regression, linear SVC, random forest) on the depth-1 vs.\\ depth-2 binary classification task using McNemar's test with continuity correction on 5-fold GroupKFold out-of-fold predictions (Table~\\ref{tab:mcnemar_obd_baselines}).\nOf 36 comparisons, 31 are non-significant ($p \\geq 0.05$), and all five significant results concentrate in two model $\\times$ domain conditions.\nFor LLaMA-8B on C4, all three baselines significantly outperform OBD ($p \\leq 0.001$), likely reflecting LightGBM overfitting on the relatively noisy 8B-generated features rather than a systematic classifier advantage.\nFor Qwen-1.5B on Wikipedia, OBD outperforms both linear classifiers ($p < 0.001$) but not random forest ($p = 0.655$).\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{McNemar test $p$-values comparing OBD-LightGBM against baseline classifiers on the depth-1 vs.\\ depth-2 binary classification task (5-fold GroupKFold, out-of-fold predictions). Classifier accuracy shown in parentheses. Significant results ($p < 0.05$) are \\textbf{bold}; $^{*}p<0.05$, $^{**}p<0.01$, $^{***}p<0.001$.}\n\\label{tab:mcnemar_obd_baselines}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Domain} & \\textbf{OBD Acc.} & \\textbf{vs.\\ LogReg} & \\textbf{vs.\\ LinearSVC} & \\textbf{vs.\\ RandomForest} \\\\\n\\midrule\nQwen-1.5B-base & C4    & .592 & .232 (.598)            & .605 (.595)              & .271 (.597) \\\\\nPythia-1.4B     & C4    & .631 & $\\mathbf{.033^{*}}$ (.621) & .105 (.624)              & .451 (.628) \\\\\nLLaMA-8B        & C4    & .573 & $\\mathbf{6.2{\\times}10^{-5\\,***}}$ (.592) & $\\mathbf{1.1{\\times}10^{-4\\,***}}$ (.591) & $\\mathbf{.001^{**}}$ (.586) \\\\\n\\midrule\nQwen-1.5B      & Wiki  & .588 & $\\mathbf{9.4{\\times}10^{-4\\,***}}$ (.570) & $\\mathbf{2.3{\\times}10^{-4\\,***}}$ (.568) & .655 (.590) \\\\\nPythia          & Wiki  & .560 & .180 (.567)            & .540 (.564)              & .369 (.564) \\\\\nOLMo            & Wiki  & .500 & .868 (.502)            & .705 (.503)              & .751 (.502) \\\\\nLLaMA-8B        & Wiki  & .573 & .252 (.579)            & .270 (.579)              & .110 (.580) \\\\\n\\midrule\nQwen-1.5B      & arXiv & .781 & .156 (.774)            & .079 (.772)              & .364 (.777) \\\\\nPythia          & arXiv & .733 & .232 (.727)            & .384 (.728)              & .735 (.732) \\\\\nOLMo            & arXiv & .493 & .520 (.487)            & .681 (.489)              & .759 (.496) \\\\\nQwen-7B         & arXiv & .757 & .160 (.749)            & .327 (.751)              & .733 (.758) \\\\\nMistral-7B      & arXiv & .742 & .524 (.738)            & .633 (.739)              & .225 (.748) \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\n\\vspace{4pt}\n\\footnotesize\n36 comparisons total. 5/36 reach $p < 0.05$; 4/36 reach $p < 0.01$.\nThe predominance of non-significant results confirms that depth discriminability is feature-driven, not classifier-driven.\n\\end{table*}\n\n\\subsection{Domain Lexical Statistics}\n\\label{sec:domain_lexical_stats}\n\nTable~\\ref{tab:domain-ttr-entropy} reports type-token ratio (TTR) and vocabulary entropy across three domains and six depth levels.\nThe TTR ordering at depth 0 (arXiv $>$ C4 $>$ Wikipedia) aligns with the $\\Kempirical$ ordering, with large effect sizes (Cohen's $d = 1.52$ for arXiv vs.\\ Wikipedia).\nVocabulary entropy shows a partial reversal at depth 0: C4 ($H = 6.225$) falls below Wikipedia ($H = 6.408$), while arXiv remains highest ($H = 6.853$).\nThis reversal likely reflects C4's greater content heterogeneity (higher variance: $\\sigma = 0.706$ vs.\\ $0.284$), which inflates TTR but depresses mean entropy.\nAs depth increases, all domains converge, with arXiv exhibiting the steepest decline, consistent with its higher $\\Kempirical$ and slower convergence to the stationary distribution.\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{Type-Token Ratio (TTR) and vocabulary entropy across three domains and generation depths.\nAt depth~0 (original human text), arXiv exhibits the highest lexical diversity (TTR\\,=\\,0.755, $H$\\,=\\,6.853),\nfollowed by C4 and Wikipedia.\nAs depth increases, all domains converge, with arXiv showing the steepest decline.\nCohen's $d$ values are computed at depth~0 for pairwise domain comparisons.}\n\\label{tab:domain-ttr-entropy}\n\\begin{tabular}{ll rrr rrr}\n\\toprule\n& & \\multicolumn{3}{c}{\\textbf{TTR}} & \\multicolumn{3}{c}{\\textbf{Vocab Entropy ($H$)}} \\\\\n\\cmidrule(lr){3-5} \\cmidrule(lr){6-8}\n\\textbf{Depth} & $N$ & \\textbf{Wiki} & \\textbf{C4} & \\textbf{arXiv} & \\textbf{Wiki} & \\textbf{C4} & \\textbf{arXiv} \\\\\n\\midrule\n0 & 5k/5k/2.2k & .665\\tpm.061 & .720\\tpm.105 & \\textbf{.755}\\tpm.055 & 6.408\\tpm.284 & 6.225\\tpm.706 & \\textbf{6.853}\\tpm.295 \\\\\n1 &             & .655\\tpm.121 & .707\\tpm.149 & \\textbf{.732}\\tpm.098 & 5.932\\tpm.843 & 5.737\\tpm1.189 & \\textbf{6.113}\\tpm.655 \\\\\n2 &             & .647\\tpm.145 & .676\\tpm.159 & \\textbf{.677}\\tpm.131 & 5.784\\tpm.905 & 5.774\\tpm1.139 & \\textbf{5.998}\\tpm.967 \\\\\n3 &             & .645\\tpm.159 & \\textbf{.662}\\tpm.164 & .635\\tpm.134 & 5.664\\tpm1.085 & 5.743\\tpm1.161 & \\textbf{5.964}\\tpm.933 \\\\\n4 &             & .636\\tpm.164 & \\textbf{.647}\\tpm.169 & .621\\tpm.140 & 5.660\\tpm1.062 & 5.758\\tpm1.167 & \\textbf{5.898}\\tpm.942 \\\\\n5 &             & .632\\tpm.172 & \\textbf{.636}\\tpm.175 & .618\\tpm.150 & 5.593\\tpm1.130 & 5.772\\tpm1.141 & \\textbf{5.816}\\tpm.968 \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cohen's $d$ at depth 0 (positive $=$ second domain higher):}} \\\\\n\\multicolumn{2}{l}{C4 vs.\\ Wiki}   & \\multicolumn{3}{c}{$d = +0.65$} & \\multicolumn{3}{c}{$d = -0.34$} \\\\\n\\multicolumn{2}{l}{arXiv vs.\\ C4}  & \\multicolumn{3}{c}{$d = +0.37$} & \\multicolumn{3}{c}{$d = +1.03$} \\\\\n\\multicolumn{2}{l}{arXiv vs.\\ Wiki} & \\multicolumn{3}{c}{$d = +1.52$} & \\multicolumn{3}{c}{$d = +1.55$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Leave-One-Family-Out Threshold Validation}\n\\label{sec:theta_lofo}\n\nTo validate $\\theta{=}0.60$ without circular reasoning, we perform leave-one-family-out (LOFO) cross-validation: each fold removes one architecture family, derives $\\hat{\\theta}$ as the midpoint between $\\min(\\auc_{1v2})$ and $\\max(\\auc_{2v3})$ over the remaining families, then predicts $\\Kempirical$ for the held-out models.\nTable~\\ref{tab:theta_lofo} reports results across all three domains.\n\nOn C4, 8/9 held-out predictions agree with the original $\\Kempirical$ assignment at $\\theta{=}0.60$ (agreement: 89\\%).\nThe single mismatch is Qwen-1.5B-RW (rewrite mode), whose 2v3 AUC of 0.5893 lies above the LOFO-derived $\\hat{\\theta}{=}0.5725$ but below the global $\\theta{=}0.60$; this configuration is also the sole rewrite-mode model, the discrepancy is therefore attributable to mode rather than threshold instability.\nThe derived $\\hat{\\theta}$ values span $[0.5725, 0.6004]$, and $\\theta{=}0.60$ falls within this range.\n\nArXiv corroborates with 6/6 agreement (100\\%), though the wide $\\hat{\\theta}$ range $[0.5735, 0.7296]$ reflects OLMo-1B's near-chance performance ($\\auc_{1v2}{=}0.503$), which inflates the gap midpoint when OLMo is included in the training fold.\n\nWikipedia yields only 1/6 agreement (17\\%).\nThis failure is expected: most models produce near-chance 1v2 AUC on Wikipedia ($0.499$--$0.619$), so the gap between $\\min(\\auc_{1v2})$ and $\\max(\\auc_{2v3})$ is narrow or inverted, the gap-based threshold derivation is therefore invalid.\nWikipedia's $\\Kempirical{=}1$ assignment is independently confirmed by the global $\\theta{=}0.60$ criterion (Section~\\ref{sec:cross_domain}); LOFO simply cannot validate this because the method requires a clear AUC discontinuity between boundary and non-boundary pairs.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Leave-One-Family-Out (LOFO) cross-validation of $\\theta$ across three domains. Each fold holds out one architecture family, derives $\\hat{\\theta}$ as the midpoint between $\\min(\\text{AUC}_{1\\text{v}2})$ and $\\max(\\text{AUC}_{2\\text{v}3})$ over the remaining families, and predicts $K^*$ for held-out models. C4 (primary): 8/9 agreement (89\\%). arXiv: 6/6 (100\\%). Wikipedia: 1/6 (17\\%, see text).}\n\\label{tab:theta_lofo}\n\\begin{tabular}{l l l c c c c c c}\n\\toprule\nDomain & Held-out & Model & $\\text{AUC}_{1\\text{v}2}$ & $\\text{AUC}_{2\\text{v}3}$ & $\\hat{\\theta}$ & $K^*_{\\hat{\\theta}}$ & $K^*_{0.60}$ & Match \\\\\n\\midrule\nC4 & Pythia & Pythia-1.4B & 0.6539 & 0.5515 & 0.5914 & 2 & 2 & \\cmark \\\\\n & OLMo & OLMo-1B & 0.6146 & 0.5497 & 0.5914 & 2 & 2 & \\cmark \\\\\n & Qwen & Qwen-1.5B-RW & 0.6957 & 0.5893 & 0.5725 & 3 & 2 & \\xmark \\\\\n &  & Qwen-7B & 0.6178 & 0.5460 & 0.5725 & 2 & 2 & \\cmark \\\\\n &  & Qwen-1.5B-base & 0.6262 & 0.5496 & 0.5725 & 2 & 2 & \\cmark \\\\\n &  & Qwen-1.5B-cont & 0.6114 & 0.5609 & 0.5725 & 2 & 2 & \\cmark \\\\\n &  & Qwen-14B & 0.6210 & 0.5494 & 0.5725 & 2 & 2 & \\cmark \\\\\n & LLaMA & LLaMA-3.1-8B & 0.6123 & 0.5274 & 0.5914 & 2 & 2 & \\cmark \\\\\n & Mistral & Mistral-7B & 0.5935 & 0.5402 & 0.6004 & 1 & 1 & \\cmark \\\\\n\\cmidrule{2-9}\n & \\multicolumn{7}{l}{$\\hat{\\theta}$ $\\in$ [0.5725, 0.6004], agreement: 8/9 (89\\%)} \\\\\n\\midrule\narXiv & Pythia & Pythia-1.4B & 0.8047 & 0.6545 & 0.5735 & 3 & 3 & \\cmark \\\\\n & OLMo & OLMo-1B & 0.5034 & 0.5069 & 0.7296 & 1 & 1 & \\cmark \\\\\n & Qwen & Qwen-1.5B & 0.8581 & 0.6436 & 0.5789 & 3 & 3 & \\cmark \\\\\n &  & Qwen-7B & 0.8347 & 0.6255 & 0.5789 & 3 & 3 & \\cmark \\\\\n & LLaMA & LLaMA-3.1-8B & 0.8447 & 0.6215 & 0.5789 & 3 & 3 & \\cmark \\\\\n & Mistral & Mistral-7B & 0.8201 & 0.6275 & 0.5789 & 3 & 3 & \\cmark \\\\\n\\cmidrule{2-9}\n & \\multicolumn{7}{l}{$\\hat{\\theta}$ $\\in$ [0.5735, 0.7296], agreement: 6/6 (100\\%)} \\\\\n\\midrule\nWikipedia & Pythia & Pythia-1.4B & 0.5846 & 0.5445 & 0.5274 & 3 & 1 & \\xmark \\\\\n & OLMo & OLMo-1B & 0.4986 & 0.5012 & 0.5557 & 1 & 1 & \\cmark \\\\\n & Qwen & Qwen-1.5B & 0.6193 & 0.5498 & 0.5215 & 4 & 2 & \\xmark \\\\\n &  & Qwen-7B & 0.6108 & 0.5562 & 0.5215 & 4 & 2 & \\xmark \\\\\n & LLaMA & LLaMA-3.1-8B & 0.5954 & 0.5392 & 0.5274 & 3 & 1 & \\xmark \\\\\n & Mistral & Mistral-7B & 0.5552 & 0.5236 & 0.5274 & 2 & 1 & \\xmark \\\\\n\\cmidrule{2-9}\n & \\multicolumn{7}{l}{$\\hat{\\theta}$ $\\in$ [0.5215, 0.5557], agreement: 1/6 (17\\%)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Code Domain Results}\n\\label{sec:code_domain}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Code domain (Python, CodeSearchNet~\\cite{husain2019codesearchnet}) pairwise AUC for Qwen2.5-1.5B. $\\Kempirical{=}2$: 1v2 exceeds $\\theta{=}0.60$; 2v3 drops to chance. JSD ratio (1v2/2v3) $= 11.7\\times$, comparable to C4's cliff structure.}\n\\label{tab:code_domain_qwen}\n\\begin{tabular}{l c c c}\n\\toprule\nPair & AUC & 95\\% CI & JSD \\\\\n\\midrule\n0 vs 1 & 0.9388 & [0.929, 0.949] & 0.0814 \\\\\n1 vs 2 & 0.7382 & [0.709, 0.767] & 0.0443 \\\\\n2 vs 3 & 0.5300 & [0.514, 0.546] & 0.0038 \\\\\n3 vs 4 & 0.5022 & [0.486, 0.518] & 0.0033 \\\\\n4 vs 5 & 0.5219 & [0.510, 0.534] & 0.0030 \\\\\n\\midrule\n\\multicolumn{4}{l}{$\\Kempirical = 2$ ($\\theta = 0.60$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Code domain (Python, CodeSearchNet) cross-model pairwise AUC with 5-fold cross-validated 95\\% CIs. Qwen2.5-1.5B yields $\\Kempirical{=}2$; Pythia-1.4B yields borderline $\\Kempirical{=}1$ (1v2 CI upper $= 0.603 > \\theta$). Additional models pending completion.}\n\\label{tab:code_crossmodel_kstar}\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{Qwen2.5-1.5B} & \\multicolumn{2}{c}{Pythia-1.4B} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\n & AUC & 95\\% CI & AUC & 95\\% CI \\\\\n\\midrule\n0v1 & .9388 & [.929,\\,.949] & \\textbf{.9592} & [.956,\\,.963] \\\\\n1v2 & \\textbf{.7382} & [.709,\\,.767]\\rlap{$^*$} & .5983 & [.593,\\,.603] \\\\\n2v3 & .5300 & [.514,\\,.546] & .5215 & --- \\\\\n3v4 & .5022 & --- & .5152 & --- \\\\\n4v5 & .5219 & --- & .5046 & --- \\\\\n\\midrule\n$K^*$ & \\multicolumn{2}{c}{\\textbf{2}} & \\multicolumn{2}{c}{1} \\\\\n\\bottomrule\n\\multicolumn{5}{@{}p{\\linewidth}@{}}{\\footnotesize $^*$Permutation $p < 0.001$. $K^*$: max $k$ where $k$v$(k{+}1)$ AUC $\\geq \\theta = 0.60$.}\n\\end{tabular}\n\\end{table}\n\n\\subsection{Borderline Feature Analysis}\n\\label{sec:borderline_analysis}\n\nTo understand why Mistral-7B yields $\\Kempirical{=}1$ while other C4 models yield $\\Kempirical{=}2$, we compute per-feature Cohen's $d$ (depth-1 vs.\\ depth-2) and LightGBM feature importances across six C4 configurations spanning the full 1v2 AUC range (0.594--0.884).\n\nMistral-7B exhibits the lowest depth-0 mean surprisal (2.32 vs.\\ 2.90--3.02 for other models), the scorer model therefore already finds Mistral's output highly predictable.\nThis compressed baseline limits the dynamic range available for detecting inter-generational degradation: all 15 Cohen's $d$ values are weak ($\\bar{|d|} = 0.112$; Table~\\ref{tab:cohens_d_full}), and no single feature exceeds 13\\% of total classifier importance.\nThe borderline models (LLaMA-8B, Pythia at $T{=}1.2$) show a similar pattern at slightly higher effect sizes.\n\nGreedy decoding is qualitatively distinct: Pythia-greedy achieves 0.884 AUC via lexical collapse (hapax ratio $d = -1.056$, capturing 47\\% of importance), a signal absent under sampling-based generation where all non-greedy models rely on surprisal variability features.\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{Feature-level summary of C4 1v2 classification across model categories. Imp.\\ = normalized LightGBM gain importance (\\%). $\\bar{|d|}$ = mean absolute Cohen's $d$ over all 15 features. $\\Delta\\text{surp}_{1\\to2}$: change in mean surprisal from depth 1 to depth 2.}\n\\label{tab:borderline_features}\n\\begin{tabular}{@{}llc lcc@{}}\n\\toprule\nCategory & Model & AUC & Top-3 Features (Imp.\\%) & $\\bar{|d|}$ & $\\Delta\\text{surp}_{1\\to2}$ \\\\\n\\midrule\nStrong & Pythia-greedy & 0.884 & hapax\\_ratio (47), surp\\_mean (11), low\\_freq\\_ratio (8) & 0.365 & $-$0.160 \\\\\nStrong & Pythia-nuc09 & 0.677 & surp\\_std (20), freq\\_entropy (11), surp\\_d1\\_std (8) & 0.170 & $-$0.196 \\\\\nStrong & Qwen-1.5B-base & 0.626 & surp\\_std (13), freq\\_entropy (10), surp\\_mean (9) & 0.125 & $-$0.159 \\\\\n\\midrule\nBorderline & Pythia-$T{=}1.2$ & 0.617 & surp\\_std (15), freq\\_entropy (10), surp\\_kurt (8) & 0.112 & $-$0.059 \\\\\nBorderline & LLaMA-3.1-8B & 0.612 & surp\\_std (12), surp\\_d1\\_std (10), freq\\_entropy (9) & 0.137 & $-$0.215 \\\\\n\\midrule\nBelow $\\theta$ & Mistral-7B & 0.594 & surp\\_std (13), freq\\_entropy (9), surp\\_d1\\_skew (9) & 0.112 & $-$0.086 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[h]\n\\centering\n\\scriptsize\n\\caption{Cohen's $d$ (depth-1 vs.\\ depth-2) for all 15 features across six C4 models. \\textbf{Bold}: largest $|d|$ in each row. Greedy decoding produces qualitatively different effect sizes via lexical collapse (hapax\\_ratio, low\\_freq\\_ratio); under sampling, surprisal variability features (surp\\_std, surp\\_d1\\_std, surp\\_d2\\_std) carry the dominant signal.}\n\\label{tab:cohens_d_full}\n\\begin{tabular}{@{}lrrrrrr@{}}\n\\toprule\nFeature & \\rotatebox{60}{Pythia-greedy} & \\rotatebox{60}{Pythia-nuc09} & \\rotatebox{60}{Qwen-1.5B-base} & \\rotatebox{60}{Pythia-$T{=}1.2$} & \\rotatebox{60}{LLaMA-3.1-8B} & \\rotatebox{60}{Mistral-7B} \\\\\n\\midrule\nsurp\\_mean & \\textbf{$-$0.416} & $-$0.306 & $-$0.244 & $-$0.103 & $-$0.263 & $-$0.152 \\\\\nsurp\\_std & $-$0.301 & \\textbf{$-$0.370} & $-$0.229 & $-$0.268 & $-$0.316 & $-$0.190 \\\\\nsurp\\_skew & \\textbf{$+$0.468} & $+$0.086 & $+$0.085 & $-$0.217 & $+$0.049 & $+$0.103 \\\\\nsurp\\_kurt & \\textbf{$+$0.433} & $+$0.102 & $+$0.071 & $-$0.188 & $+$0.031 & $+$0.124 \\\\\nsurp\\_d1\\_mean & $+$0.028 & $+$0.031 & $-$0.024 & $+$0.026 & \\textbf{$+$0.080} & $+$0.026 \\\\\nsurp\\_d1\\_std & $-$0.318 & \\textbf{$-$0.342} & $-$0.236 & $-$0.228 & $-$0.306 & $-$0.212 \\\\\nsurp\\_d1\\_skew & \\textbf{$-$0.224} & $-$0.058 & $-$0.053 & $-$0.012 & $-$0.014 & $-$0.084 \\\\\nsurp\\_d2\\_mean & $+$0.004 & $+$0.001 & \\textbf{$+$0.034} & $-$0.015 & $-$0.030 & $+$0.012 \\\\\nsurp\\_d2\\_std & $-$0.312 & \\textbf{$-$0.332} & $-$0.247 & $-$0.209 & $-$0.292 & $-$0.207 \\\\\nttr & \\textbf{$-$0.404} & $-$0.212 & $-$0.123 & $-$0.115 & $-$0.203 & $-$0.135 \\\\\nhapax\\_ratio & \\textbf{$-$1.056} & $-$0.221 & $-$0.144 & $-$0.108 & $-$0.186 & $-$0.139 \\\\\nself\\_bleu & $-$0.056 & $+$0.031 & \\textbf{$+$0.140} & $+$0.058 & $+$0.118 & $+$0.127 \\\\\nfreq\\_kurtosis & $+$0.071 & \\textbf{$-$0.083} & $-$0.007 & $+$0.007 & $+$0.005 & $-$0.030 \\\\\nfreq\\_entropy & \\textbf{$-$0.350} & $-$0.158 & $-$0.104 & $-$0.021 & $+$0.031 & $-$0.044 \\\\\nlow\\_freq\\_ratio & \\textbf{$-$1.029} & $-$0.226 & $-$0.139 & $-$0.110 & $-$0.134 & $-$0.090 \\\\\n\\midrule\n$\\bar{|d|}$ & 0.365 & 0.170 & 0.125 & 0.112 & 0.137 & 0.112 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n",
    "structuredPatch": [
      {
        "oldStart": 602,
        "oldLines": 7,
        "newStart": 602,
        "newLines": 7,
        "lines": [
          " \\midrule",
          " $K^*$ & \\multicolumn{2}{c}{\\textbf{2}} & \\multicolumn{2}{c}{1} \\\\",
          " \\bottomrule",
          "-\\multicolumn{5}{@{}p{\\linewidth}@{}}{\\footnotesize $^*$Permutation $p < 0.001$. $K^*$: max $k$ where $k$v$(k{+}1)$ AUC $\\geq \\theta = 0.60$.}",
          "+\\multicolumn{5}{@{}p{\\linewidth}@{}}{\\footnotesize $^*$Permutation $p < 0.001$. $K^*$: max $k$ where $k$v$(k{+}1)$ CI lower bound $> \\theta = 0.60$ (Eq.~\\ref{eq:kstar}).}",
          " \\end{tabular}",
          " \\end{table}",
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

### Assistant

_source line 35_

All three edits applied. Let me verify the changes look correct and then compile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "40f7781e-0798-4b01-b0d0-1106e354d4fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KosnWmce7WDaDAdPGbSdFn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1645,
      "cache_read_input_tokens": 43858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1645
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

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01GR4DwNtiprR9gSAuTsPDqn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex",
  "offset": 19,
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
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "7350b6e0-0305-43b2-bf0d-f2c937f8d3ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KosnWmce7WDaDAdPGbSdFn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1645,
      "cache_read_input_tokens": 43858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1645
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

### Tool result

_source line 37 · 2026-05-19T06:29:35.369Z_

<details><summary>↩ Tool result · `toolu_01GR4DwNtiprR9gSAuTsPDqn`</summary>

```text
19	We define the operational lower bound:
20	\begin{equation}
21	  \Kempirical = \max\{k \geq 1 : \mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k}) > \theta\},
22	  \label{eq:kstar}
23	\end{equation}
24	where $\mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k})$ is the lower bound of a 95\% bootstrap confidence interval (1{,}000 resamples\footnote{Boundary-pair results in Table~\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) over the pairwise AUC (Area Under the ROC Curve) between depths $k{-}1$ and $k$, and $\theta = 0.60$ is a post-hoc operational threshold (motivated below).
25	This criterion ensures that $\Kempirical$ reflects statistically robust discriminability rather than sampling noise.
26	We additionally verify that non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
27	
28	\paragraph{Threshold choice.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "4cf979f7-4097-4248-969c-587811a6bb89",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex",
      "content": "We define the operational lower bound:\n\\begin{equation}\n  \\Kempirical = \\max\\{k \\geq 1 : \\mathrm{CI}_{\\mathrm{low}}(\\auc_{k-1,k}) > \\theta\\},\n  \\label{eq:kstar}\n\\end{equation}\nwhere $\\mathrm{CI}_{\\mathrm{low}}(\\auc_{k-1,k})$ is the lower bound of a 95\\% bootstrap confidence interval (1{,}000 resamples\\footnote{Boundary-pair results in Table~\\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) over the pairwise AUC (Area Under the ROC Curve) between depths $k{-}1$ and $k$, and $\\theta = 0.60$ is a post-hoc operational threshold (motivated below).\nThis criterion ensures that $\\Kempirical$ reflects statistically robust discriminability rather than sampling noise.\nWe additionally verify that non-boundary-pair CI upper bounds fall below $\\theta$ (Section~\\ref{sec:kstar_boundary}).\n\n\\paragraph{Threshold choice.}",
      "numLines": 10,
      "startLine": 19,
      "totalLines": 81
    }
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_01T6qDjeJxbgPeJmS37Vii9P`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
  "description": "First pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "a218c2af-90bf-419f-b8d7-0359ef50c7dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KosnWmce7WDaDAdPGbSdFn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1645,
      "cache_read_input_tokens": 43858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1645
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

### Tool result

_source line 39 · 2026-05-19T06:29:38.016Z_

<details><summary>↩ Tool result · `toolu_01T6qDjeJxbgPeJmS37Vii9P`</summary>

```text
/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/urw/zapfding/uzdr.pfb>
Output written on main.pdf (28 pages, 850610 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "908a0ef1-90b8-45f5-9631-e020e897197e",
  "tool_use_result": {
    "stdout": "/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/urw/zapfding/uzdr.pfb>\nOutput written on main.pdf (28 pages, 850610 bytes).\nTranscript written on main.log.",
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

_source line 40_

First pass compiled successfully (28 pages, 0 errors). Running second pass for cross-references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "e0a4d83f-5e56-41ca-b1f9-4c2a1a0355c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQTenhLfi6VjtZ7nKT7skp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 45503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 810
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

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_01LZJzxswS2bDVuik7RcAgoq`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
  "description": "Second pdflatex pass for cross-references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "efeeb019-d1e9-4f29-9777-bcc62d65096f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQTenhLfi6VjtZ7nKT7skp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 45503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 810
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

### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b5oe1ns1b",
  "tool_use_id": "toolu_01LZJzxswS2bDVuik7RcAgoq",
  "description": "Second pdflatex pass for cross-references",
  "task_type": "local_bash",
  "uuid": "a1fa7049-de7a-4115-a96c-dfe9deaf1d4b",
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81"
}
```

---

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b5oe1ns1b",
  "tool_use_id": "toolu_01LZJzxswS2bDVuik7RcAgoq",
  "status": "completed",
  "output_file": "",
  "summary": "Second pdflatex pass for cross-references",
  "uuid": "01700731-bfb0-4a48-8607-86db3290d891",
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81"
}
```

---

### Tool result

_source line 44 · 2026-05-19T06:29:45.838Z_

<details><summary>↩ Tool result · `toolu_01LZJzxswS2bDVuik7RcAgoq`</summary>

```text
/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/urw/zapfding/uzdr.pfb>
Output written on main.pdf (28 pages, 850563 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "019c960b-ea26-414d-a325-782591e7ae8a",
  "tool_use_result": {
    "stdout": "/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/urw/zapfding/uzdr.pfb>\nOutput written on main.pdf (28 pages, 850563 bytes).\nTranscript written on main.log.",
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

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_01U1x6YGbWJzTni34bBUNa4b`</summary>

```json
{
  "command": "grep -c \"^!\" /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.log",
  "description": "Count LaTeX errors in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "c7abbef9-aab5-4ef6-8db1-8e4ff03c1774",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sjk6pBmggKb1QXwME69v2a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 394,
      "cache_read_input_tokens": 46313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 394
      },
      "output_tokens": 43,
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

_source line 46 · 2026-05-19T06:29:48.901Z_

<details><summary>↩ Tool result · `toolu_01U1x6YGbWJzTni34bBUNa4b`</summary>

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
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "f56a6396-6223-4e09-b0d7-ac78d914aeeb",
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

### Assistant

_source line 47_

0 errors, 28 pages, two passes clean.

修改总结：

1. **method.tex Eq.1**：将 `\auc_{k-1,k} > \theta` 改为 `\mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k}) > \theta`，定义说明从 "point-estimate pairwise AUC" 改为 "lower bound of a 95% bootstrap confidence interval over the pairwise AUC"。新增一句说明该准则确保 K* 反映统计上稳健的可区分性。非边界对的 CI upper bound 验证保留为独立检查。

2. **experiments_c1.tex Table 1 caption**：将 "requires 1v2 AUC > θ" 改为 "requires 1v2 CI lower bound > θ"，并引用 Eq.1。

3. **appendix_extended.tex code domain table footnote**：同步修改 K* 定义为 CI lower bound 形式，引用 Eq.1。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "uuid": "704271a7-5510-44e3-878c-b57edb78b005",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FnbEdmBmACLsRsnaS9RGQ2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 128,
      "cache_read_input_tokens": 46707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 128
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

_source line 48_

0 errors, 28 pages, two passes clean.

修改总结：

1. **method.tex Eq.1**：将 `\auc_{k-1,k} > \theta` 改为 `\mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k}) > \theta`，定义说明从 "point-estimate pairwise AUC" 改为 "lower bound of a 95% bootstrap confidence interval over the pairwise AUC"。新增一句说明该准则确保 K* 反映统计上稳健的可区分性。非边界对的 CI upper bound 验证保留为独立检查。

2. **experiments_c1.tex Table 1 caption**：将 "requires 1v2 AUC > θ" 改为 "requires 1v2 CI lower bound > θ"，并引用 Eq.1。

3. **appendix_extended.tex code domain table footnote**：同步修改 K* 定义为 CI lower bound 形式，引用 Eq.1。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 165637,
  "duration_api_ms": 160653,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "a4bb2cb8-df91-4cb8-9876-54b5fd588f81",
  "total_cost_usd": 0.651062,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 34994,
    "cache_read_input_tokens": 355347,
    "output_tokens": 10126,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 34994,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 282,
        "cache_read_input_tokens": 46707,
        "cache_creation_input_tokens": 128,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 128
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1351,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001471,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 10126,
      "cacheReadInputTokens": 355347,
      "cacheCreationInputTokens": 34994,
      "webSearchRequests": 0,
      "costUSD": 0.649591,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "434b6645-4502-4f5e-b445-d0dcfdb67b53"
}
```

</details>

---
