# Research conversation: Read all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/ and extr

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a02c88d2dafcf0406.jsonl`
- **Structured JSON:** [`38f6f05d16f6e6a3e0e3.json`](../../sessions/38/38f6f05d16f6e6a3e0e3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

41 recorded events

### User

_source line 1 · 2026-05-23T19:22:21.157Z_

Read all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/ and extract every numerical value mentioned. The files are: main.tex, abstract.tex, introduction.tex, method.tex, theory.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex, related_work.tex

For each number found, record:
1. The filename
2. The line number
3. The exact number (with units like %, ×, etc.)
4. The surrounding context sentence

Focus on these types:
- Percentages (e.g., 93.5%, 14.9%, 92%)
- Decimal metrics (e.g., R²=0.994, RMSE=0.089, |Bias|=0.008)
- Integers that represent counts or configurations (e.g., 520 configs, 13 LLM combinations, 100 MC runs)
- Multipliers (e.g., 7.4×, 2.86×, 5-7×)
- Inequalities (e.g., ≥93.5%, ≤1.25, <5%)

Be thorough - read each file completely. Output the complete list organized by file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "6cf57537-06f3-4cf0-afda-b2f017032e87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-23T19:22:21.163Z_

```json
{
  "parentUuid": "6cf57537-06f3-4cf0-afda-b2f017032e87",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
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
      "mcp__agent-ml-research__register_artifact"
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
      "mcp__agent-ml-research__register_artifact"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f6ede9a4-4dd7-4320-9b11-c6594bdebe52",
  "timestamp": "2026-05-23T19:22:21.163Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-23T19:22:23.380Z_



I'll read all the .tex files systematically to extract every numerical value. Let me start by reading all files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6ede9a4-4dd7-4320-9b11-c6594bdebe52",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3Z6ogphcidA7462ncp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3cfb03b9-80b5-4eb1-a53b-445a66fdd3e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaawH9tFnppryWcn8UcbTw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9114,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9114,
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

_source line 4 · 2026-05-23T19:22:23.870Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MD6kY4zgk7H6Aw4wVBjh8x`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cfb03b9-80b5-4eb1-a53b-445a66fdd3e4",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3Z6ogphcidA7462ncp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96ddcef1-3694-409b-9270-aed7c8757ea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaawH9tFnppryWcn8UcbTw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9114,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9114,
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

_source line 5 · 2026-05-23T19:22:23.903Z_

<details><summary>↩ Tool result · `toolu_01MD6kY4zgk7H6Aw4wVBjh8x`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	
10	\usepackage{amsmath,amssymb,amsthm}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{enumitem}
16	\usepackage{algorithm}
17	\usepackage{algpseudocode}
18	
19	\newtheorem{theorem}{Theorem}
20	\newtheorem{corollary}[theorem]{Corollary}
21	\newtheorem{proposition}[theorem]{Proposition}
22	\newtheorem{remark}[theorem]{Remark}
23	
24	\title{Error-Corrected Heterogeneous Treatment Effects:\\When LLM Annotation Debiasing Hurts}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	
35	\input{related_work}
36	
37	\input{theory}
38	
39	\input{method}
40	
41	\input{experiments}
42	
43	\input{conclusion}
44	
45	\input{limitations}
46	
47	\bibliography{references}
48	
49	\appendix
50	\input{appendix}
51	
52	%\input{checklist}
53	
54	\end{document}
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96ddcef1-3694-409b-9270-aed7c8757ea2",
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "efa2e22d-8912-43db-80b5-13e26656247c",
  "sourceToolAssistantUUID": "96ddcef1-3694-409b-9270-aed7c8757ea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-23T19:22:24.837Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q13yXaTQhSN8v2AKNYMYuo`</summary>

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
  "parentUuid": "efa2e22d-8912-43db-80b5-13e26656247c",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3Z6ogphcidA7462ncp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70366f5c-5e35-4f95-af6e-06b31c2e576d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaawH9tFnppryWcn8UcbTw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9114,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9114,
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

_source line 7 · 2026-05-23T19:22:24.868Z_

<details><summary>↩ Tool result · `toolu_01Q13yXaTQhSN8v2AKNYMYuo`</summary>

```text
1	\begin{abstract}
2	Standard confusion-matrix correction for noisy annotations assumes uniform error rates.
3	When this assumption fails, correction can increase rather than decrease bias in heterogeneous treatment effect (HTE) estimates, reversing the sign of estimated effect heterogeneity.
4	LLMs, now widely used as proxy classifiers in computational social science, are the leading practical instance, with error rates varying by up to $5\times$ across demographic subgroups.
5	We derive the first exact bias decomposition for this setting: global correction introduces subgroup-level bias with a product form factoring into each subgroup's deviation from the pooled error rate, the treatment effect heterogeneity, and an amplification factor from matrix inversion.
6	This is not a bound but a population-level identity; global correction can reverse the sign of estimated CATE---concluding a beneficial treatment is harmful---in 14.9\% of configurations, and amplifies bias in all eight real LLMs tested.
7	The decomposition yields a diagnostic that predicts harmful correction from per-subgroup error rates alone (AUC $= 1.0$ on subgroups with non-zero effect heterogeneity).
8	Error-Corrected Heterogeneous Treatment Effects (EC-HTE), the per-subgroup correction prescribed by the decomposition, reduces $|\text{bias}|$ by $7.4\times$ under extreme heterogeneity with coverage $\geq 0.90$ via hierarchical Bayesian estimation; the advantage requires sufficient error heterogeneity and expert budget.
9	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70366f5c-5e35-4f95-af6e-06b31c2e576d",
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "49214013-506b-437c-aa4d-43137e2a27b1",
  "sourceToolAssistantUUID": "70366f5c-5e35-4f95-af6e-06b31c2e576d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-23T19:22:25.306Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KhEhPtcSkrkrMXLiBPLCsA`</summary>

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
  "parentUuid": "49214013-506b-437c-aa4d-43137e2a27b1",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3Z6ogphcidA7462ncp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcd7e35d-9b25-471a-9620-adc1e7261455",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaawH9tFnppryWcn8UcbTw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9114,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9114,
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

_source line 9 · 2026-05-23T19:22:25.315Z_

<details><summary>↩ Tool result · `toolu_01KhEhPtcSkrkrMXLiBPLCsA`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	Consider estimating whether a content moderation policy reduces hate speech differently across demographic groups, using GPT-4 to classify thousands of posts.
5	After standard confusion-matrix correction, the analysis concludes the policy \emph{increases} hate speech among younger users---but the true effect is protective.
6	This sign reversal is not an edge case.
7	
8	Large language models (LLMs) now routinely replace human annotators in computational social science (CSS), producing labels for sentiment, hate speech, stance, and political discourse at costs orders of magnitude below manual coding~\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp}.
9	When these labels serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, the standard correction protocol\footnote{Throughout, ``debiasing'' refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing.} is straightforward: validate a sample against expert annotations, estimate a confusion matrix, and apply its inverse uniformly to correct conditional average treatment effect (CATE) estimates.
10	Yet LLM annotations are not uniformly accurate: \citet{ashwin2025bias} document misclassification rates varying by up to 5$\times$ across demographic subgroups defined by refugee status, gender, and education level; in our pilot study, GPT-4.1 achieves 85.8\% accuracy on TweetEval sentiment, but error rates range from 10.2\% to 20.0\% across text-feature subgroups ($\Delta\pi = 0.098$).
11	
12	We show that this standard correction can make things worse.
13	In 14.9\% of our synthetic configurations (across a grid of $\Delta\pi$ and $\tau(0)$ values; $\tau(0) = 0.03$), global correction reverses the sign of estimated CATE---a protective treatment ($\tau = +0.03$) appears harmful ($\hat{\tau} = -0.059$)---rising to 31\% at $\tau(0) = 0.01$ (Figure~\ref{fig:sign_reversal}); all eight real LLMs tested amplify bias under global correction, while EC-HTE eliminates sign reversal entirely.
14	Global correction amplifies bias by up to 5.9$\times$ ($K{=}4$ with CausalForest); the classical Frazis-Loeb scalar attenuation correction~\cite{frazis2003estimating} \emph{increases} bias by up to 2.9$\times$.
15	The mechanism is over-correction: for subgroups with near-zero misclassification, the naive estimator is nearly unbiased, yet pooled correction calibrated for the average error rate introduces substantial bias precisely where labels were most trustworthy.
16	
17	We derive an exact bias identity explaining when and why this occurs (Theorem~\ref{thm:bias_identity}): the correction-induced bias in each subgroup factors into three independently estimable components, verified empirically at $R^2 \geq 0.97$ on synthetic grids and $R^2 = 0.975$ across 11 real LLM confusion matrices spanning open-source and proprietary model families.
18	The identity yields a diagnostic (Proposition~\ref{prop:debiasing_hurts}) that predicts when global correction will harm a subgroup using only per-subgroup misclassification rates, without estimating any treatment effects (AUC $= 1.0$ on subgroups with non-zero effect heterogeneity; Section~\ref{sec:diagnostic}).
19	
20	Error-Corrected Heterogeneous Treatment Effects (EC-HTE), the per-subgroup correction prescribed by the identity, reduces $|\text{bias}|$ from 0.059 to 0.008 under extreme heterogeneity ($K{=}2$) via hierarchical Bayesian confusion matrix estimation.
21	EC-HTE's advantage is conditional on sufficient error heterogeneity and expert budget; when $\Delta\pi$ is small, the variance cost of stratification outweighs its bias benefit.
22	
23	Existing corrections---PPI~\cite{angelopoulos2023ppi}, DSL~\cite{egami2024dsl}, PPCI~\cite{sui2026ppci}, arm-specific PPI~\cite{mozer2026ppi}, ForestIV~\cite{bu2023forestiv}---assume homogeneous prediction error; none addresses effect modifier misclassification (Section~\ref{sec:related}).
24	
25	\begin{figure*}[t]
26	\centering
27	\includegraphics[width=\textwidth]{figures/fig1_sign_reversal.pdf}
28	\caption{CATE sign reversal under global correction ($K{=}2$, $\tau(0) = 0.03$). (A) Naive vs.\ global-corrected CATE; red triangles mark sign reversals (7.5\% of subgroup estimates). (B) Extreme case: true $\tau = +0.03$, estimated $\hat{\tau} = -0.059$. (C) 14.9\% of configurations exhibit sign reversal; all 8 real LLMs amplify bias; EC-HTE: 0\% reversal.}
29	\label{fig:sign_reversal}
30	\end{figure*}
31	
32	Our contributions are:
33	\begin{itemize}
34	    \item A demonstration that standard confusion-matrix correction---the default in PPI, DSL, and CSS practice---can reverse the sign of estimated CATE in 14.9\% of configurations ($\tau(0) = 0.03$; 31\% at $\tau(0) = 0.01$), amplifying bias in all eight real LLMs tested; we derive the first exact finite-population bias decomposition (Theorem~\ref{thm:bias_identity}) explaining when and why, with multiplicative structure $\delta_s \cdot \Delta\tau / (1-2\bar{\pi})$, verified at $R^2 \geq 0.97$ on synthetic grids and 11 real LLM confusion matrices (Sections~\ref{sec:theory},~\ref{sec:bias_mechanism}).
35	    \item An actionable diagnostic derived from the decomposition (Proposition~\ref{prop:debiasing_hurts}): a condition on per-subgroup misclassification rates alone predicts when global correction increases bias, achieving AUC $= 1.0$ on subgroups with non-zero effect heterogeneity---independently useful without adopting EC-HTE (Section~\ref{sec:diagnostic}).
36	    \item EC-HTE, an end-to-end correction pipeline: the bias decomposition identifies the correction target, the diagnostic flags when correction is needed, and hierarchical Bayesian confusion matrix estimation executes per-subgroup correction---compatible with difference-in-means, CausalForest, and R-learner, and composable with PPCI for joint covariate/outcome error (Sections~\ref{sec:method}--\ref{sec:diagnostic}; Appendix~\ref{sec:budget}).
37	\end{itemize}
38	While we develop EC-HTE for LLM annotation, the bias identity applies to any proxy classifier with subgroup-varying error rates---survey coding, medical diagnosis, and satellite imagery classification all share this structure.
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcd7e35d-9b25-471a-9620-adc1e7261455",
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "445c6006-474f-40c3-aeca-f43857fcce7b",
  "sourceToolAssistantUUID": "bcd7e35d-9b25-471a-9620-adc1e7261455",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-23T19:22:25.778Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FwrkjQeuJvzhnB8pgZj72J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "445c6006-474f-40c3-aeca-f43857fcce7b",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3Z6ogphcidA7462ncp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81f84cbe-d719-4655-9440-8c5abd356d91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaawH9tFnppryWcn8UcbTw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9114,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9114,
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

_source line 11 · 2026-05-23T19:22:25.795Z_

<details><summary>↩ Tool result · `toolu_01FwrkjQeuJvzhnB8pgZj72J`</summary>

```text
1	\section{EC-HTE: Error-Corrected Heterogeneous Treatment Effects}
2	\label{sec:method}
3	
4	Theorem~\ref{thm:bias_identity} identifies per-subgroup misclassification deviation as the bias source; the natural correction is per-subgroup confusion matrix inversion.
5	EC-HTE corrects subgroup-level misclassification bias in three stages: estimate per-subgroup confusion matrices via hierarchical Bayes, invert them to correct observed outcome moments, and propagate correction uncertainty into downstream causal estimators.
6	The complete procedure is summarized in Algorithm~\ref{alg:echte} (Appendix~\ref{app:algorithm}).
7	
8	\subsection{Hierarchical Bayes Confusion Matrix Estimation}
9	
10	We place a Dirichlet-Multinomial hierarchical model over the confusion matrices $\{C_s\}_{s=1}^K$.
11	For each subgroup $s$, row $j$ of $C_s$ has a Dirichlet prior centered at the global pooled confusion matrix $\hat{C}_{\text{global}}$: $\text{Dir}(\alpha_0 \cdot \hat{C}_{\text{global},j})$, where $\hat{C}_{\text{global},j}$ is the $j$-th row of the pooled CM and $\alpha_0 > 0$ is a shared concentration parameter estimated via empirical Bayes (marginal likelihood maximization).
12	Large $\alpha_0$ pulls subgroup estimates toward $\hat{C}_{\text{global}}$ (global correction), while small $\alpha_0$ allows subgroup-specific rates to dominate (stratified correction).
13	This partial pooling---a form of James-Stein shrinkage well-established in small-area estimation---borrows strength across subgroups when estimating confusion matrices from limited expert labels, reducing variance for small subgroups while preserving heterogeneity where data support it.
14	
15	Posterior inference uses centered empirical Bayes optimization ($<$5ms for $K{=}4$, $N{=}5{,}000$); a full Gibbs MCMC alternative requires $\sim$5s (convergence diagnostics in Appendix~\ref{app:algorithm}).
16	Bootstrap SE ($B{=}100$) adds $\sim$0.4s.
17	HB estimation outperforms stratified MLE in 87.5\% of configurations (21 of 24) across the experimental grid (Section~\ref{sec:ec_hte_eval}), with the largest gains when $n_{\text{expert}} / K < 100$.
18	The advantage requires $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$ per subgroup; below this threshold, stratified MLE is preferred because the hierarchical model lacks sufficient observations for stable shrinkage.
19	At $n_{\text{expert}} \geq 1000$, HB and stratified MLE converge to within 0.5\% on all metrics.
20	Sensitivity analysis shows $<$5\% RMSE variation under 2$\times$ hyperprior perturbation, confirming that results are not driven by prior specification.
21	
22	\subsection{Subgroup-Stratified Correction}
23	
24	Given posterior mean confusion matrices $\hat{C}_s$, we correct observed outcome moments per subgroup by matrix inversion:
25	\begin{equation}
26	\tilde{\boldsymbol{\mu}}_s = \hat{C}_s^{-1} \cdot \hat{\boldsymbol{\mu}}_s,
27	\end{equation}
28	where $\hat{\boldsymbol{\mu}}_s = [\hat{\tau}_{\text{obs}}(0, s),\, \hat{\tau}_{\text{obs}}(1, s)]^\top$ collects the observed conditional outcome moments in subgroup $s$.
29	This requires $\det(\hat{C}_s) \neq 0$ for all $s$, which holds under assumption~(A4) ($\pi_s \neq 0.5$) but may fail in finite samples when error rates approach degeneracy.
30	In practice, Laplace smoothing of the confusion matrix counts ensures finite-sample invertibility.
31	We impose a singularity guard: if the condition number $\kappa(\hat{C}_s) > 100$ (for a $2{\times}2$ symmetric confusion matrix, this corresponds to $\pi_s > 0.495$, i.e., near-random classification), subgroup $s$ falls back to global correction $\bar{C}^{-1}$; when the fallback triggers, the standard error computation also uses $\bar{C}^{-1}$ for that subgroup, ensuring consistency between point estimates and confidence intervals.
32	This hard guard prevents numerical catastrophe; $\kappa \leq 1.25$ is a sufficient condition for strongest bias reduction (Appendix~\ref{sec:budget}), though EC-HTE maintains calibrated coverage ($\geq$93\%) across the wider $\kappa \in [1.4, 3.0]$ range observed in practice (Appendix~\ref{app:kappa_analysis}).
33	
34	The contrast with global correction is direct.
35	Global correction applies $\bar{C}^{-1}$ uniformly to all subgroups, introducing the $\delta_s \cdot \Delta\tau$ bias identified in Theorem~\ref{thm:bias_identity}.
36	Subgroup-stratified correction eliminates this bias by matching each subgroup's correction to its own misclassification structure, at the cost of higher variance from estimating $K$ separate confusion matrices (Appendix~\ref{sec:budget}).
37	
38	\subsection{Variance-Adjusted CausalForest}
39	
40	For heterogeneous treatment effect estimation, we feed corrected covariates into CausalForestDML~\cite{wager2018causal} with honest splitting.
41	The forest produces per-observation standard error estimates $\text{se}_i$.
42	To account for confusion matrix correction, we propagate uncertainty through the inverse mapping:
43	\begin{equation}
44	\text{se}_{\text{corrected},i} = \sqrt{\text{diag}\!\left(\hat{C}_{S_i}^{-1}\, \text{diag}(\text{se}_i^2)\, \hat{C}_{S_i}^{-\top}\right)}.
45	\end{equation}
46	This plug-in SE conditions on $\hat{C}_s$, neglecting CM estimation uncertainty; at $n_{\text{expert}} \geq 100$ this is negligible, but below this threshold a full bootstrap ($B{=}100$; re-estimate CM and re-fit per replicate) maintains $\geq$95\% coverage across all budgets tested ($n_{\text{expert}} \in \{25, 50, 75, 100, 200\}$); even plug-in SE achieves $\geq$91\% at $n_{\text{expert}}{=}25$ (Appendix~\ref{app:bootstrap_se}).
47	When $n_{\text{expert}}/K < 50$, we recommend bootstrap SE; otherwise plug-in SE suffices.
48	
49	\paragraph{Diagnostic criterion.}
50	Proposition~\ref{prop:debiasing_hurts} provides a $\Delta\tau$-free diagnostic: global correction harms subgroup $s$ if and only if $|\delta_s| / ((1-2\bar{\pi}) \cdot \pi_s) > 1$, a condition depending only on per-subgroup misclassification rates estimable from a pilot sample.
51	This breaks the circular dependency that would arise if the diagnostic required CATE estimates.
52	A threshold classifier achieves AUC~=~0.86 at the subgroup level, reaching 1.0 when restricted to subgroups with $\tau_s > 0$ (Section~\ref{sec:diagnostic}).
53	
54	\paragraph{Composition with PPCI.}
55	EC-HTE corrects structured covariate misclassification through $\hat{C}_s^{-1}$ inversion but cannot address outcome-level measurement error.
56	PPCI~\cite{sui2026ppci} corrects residual outcome bias using a debiasing estimator but assumes correct covariate labels.
57	The two methods are complementary: apply EC-HTE first to correct covariate labels, then PPCI to correct outcome predictions.
58	Neither is redundant with the other: EC-HTE alone cannot fix outcome error, while PPCI alone incurs higher variance for covariate error.
59	Under both error types simultaneously, the composition reduces $|\text{bias}|$ from 0.179 to 0.007 (Appendix~\ref{sec:ppci}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81f84cbe-d719-4655-9440-8c5abd356d91",
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "535561f7-047b-4b8c-a548-24e6038bc7d5",
  "sourceToolAssistantUUID": "81f84cbe-d719-4655-9440-8c5abd356d91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-23T19:22:26.264Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Gzw3ATrJ1DsjaMZpMavRbi`</summary>

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
  "parentUuid": "535561f7-047b-4b8c-a548-24e6038bc7d5",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3Z6ogphcidA7462ncp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5eebcd3e-6fba-4d9c-9868-9d1d6cdbc79d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaawH9tFnppryWcn8UcbTw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9114,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9114,
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

_source line 13 · 2026-05-23T19:22:26.271Z_

<details><summary>↩ Tool result · `toolu_01Gzw3ATrJ1DsjaMZpMavRbi`</summary>

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
48	For comparison with classical scalar attenuation~\citep{frazis2003estimating}, see Section~\ref{sec:related}.
49	
50	\paragraph{Relationship to classical scalar attenuation.}
51	Classical scalar attenuation~\citep{frazis2003estimating} gives $\beta^* = \beta(1 - 2\pi)$; dividing by $(1 - 2\bar{\pi})$ removes this bias under homogeneous errors, but Theorem~\ref{thm:bias_identity} characterizes a structurally distinct quantity: \emph{correction-induced} bias from applying $M_{\mathrm{global}}^{-1}$ to heterogeneous $M_s$.
52	F-L scalar correction (dividing $\hat{\tau}(z)$ by $1 - 2\bar{\pi}$) over-corrects low-error and under-corrects high-error subgroups---the same mechanism as global CM correction but restricted to a scalar ignoring the mixing structure between $z$-levels.
53	When $\pi_s \to 0.5$, $(1 - 2\pi_s) \to 0$ and the F-L per-subgroup correction diverges; EC-HTE's $\kappa$-guard (Section~\ref{sec:method}) avoids this singularity.
54	Table~\ref{tab:main_results} confirms: under extreme heterogeneity ($K{=}2$), the classical F-L scalar correction \emph{increases} $|\text{bias}|$ from 0.058 to 0.122 ($2.1\times$ naive), and F-L per-subgroup to 0.168 ($2.9\times$)---the textbook attenuation correction systematically amplifies bias when subgroup error rates differ.
55	
56	\begin{remark}
57	Theorem~\ref{thm:bias_identity} does not require assumption~(A2).
58	For arbitrary asymmetric confusion matrices ($\mathrm{FPR}_s \neq \mathrm{FNR}_s$),
59	the product form $\mathrm{bias}(z, s) = \Delta\tau \cdot [B_s]_{z,1}$ holds exactly,
60	where $B_s = M_{\mathrm{global}}^{-1} M_s - I$, because $B_s \mathbf{1} = \mathbf{0}$
61	follows from stochasticity of $M_s$ and $M_{\mathrm{global}}$ alone.
62	Assumption~(A2) simplifies $[B_s]_{z,1}$ to the scalar
63	$\pm \delta_s / (1 - 2\bar{\pi})$ but is not necessary for the product structure.
64	Under asymmetric errors, the diagnostic (Proposition~\ref{prop:debiasing_hurts}) requires evaluating $[B_s]_{z,1}$ cell-by-cell rather than via a single scalar threshold; the AUC decreases from 0.86 to 0.66 (Appendix~\ref{app:asymmetric}), reflecting the additional complexity of cell-specific error rates.
65	For binary effect modifiers ($|\mathcal{Z}|{=}2$), the asymmetric score $|[B_s]_{z,1}|$ reduces to a monotone transform of the symmetric score $|\delta_s|/((1{-}2\bar{\pi})\pi_s)$, because column-stochastic $M$ forces $|B_s[0,1]|{=}|B_s[1,1]|$; practitioners may use the simpler symmetric formula without loss.
66	See Appendix~\ref{app:asymmetric} for the full derivation and empirical verification
67	($R^2 = 0.991$).
68	\end{remark}
69	
70	\begin{remark}[Assumption (A5) is not necessary]
71	(A5) simplifies $\Delta\tau_s$ to a scalar $\Delta\tau$, but the identity is exact without it: when treatment effects vary across subgroups, the bias is $+\delta_s \cdot \Delta\tau_s / (1 - 2\bar{\pi})$ at $z{=}0$ and $-\delta_s \cdot \Delta\tau_s / (1 - 2\bar{\pi})$ at $z{=}1$, where $\Delta\tau_s = \tau_s(1) - \tau_s(0)$ (Corollary~\ref{cor:a5_relaxation}).
72	The proof is immediate: the bias matrix $B_s = M_{\mathrm{global}}^{-1} M_s - I$ depends only on the confusion matrices, not on $\tau$.
73	The diagnostic (Proposition~\ref{prop:debiasing_hurts}) also extends without (A5): $\Delta\tau_s$ cancels in the comparison $|\mathrm{bias}_{\mathrm{global}}| \gtrless |\mathrm{bias}_{\mathrm{naive}}|$, so condition~\eqref{eq:hurts_condition} remains $\Delta\tau$-free.
74	EC-HTE's correction does not depend on (A5): each $\hat{C}_s^{-1}$ corrects the local misclassification structure regardless of whether $\Delta\tau$ varies; under both positive and negative $\Delta\tau_s$--$\delta_s$ correlation, EC-HTE maintains $\geq$93\% coverage while global correction degrades to 74--82\% (Appendix~\ref{app:a5_violation}).
75	\end{remark}
76	
77	The identity extends to $K > 2$ subgroups with $J$ effect-modifier levels; the multi-class bias retains the same product structure with modified amplification terms (Corollary~\ref{cor:multiclass} in Appendix~\ref{app:multiclass}).
78	
79	Assumption~(A3) ensures $M_s = C_s$; when $P(Z{=}1) \neq 0.5$, the mixing matrices acquire asymmetric entries, but the product structure persists with modified coefficients (Appendix~\ref{app:derivation}).
80	Empirical verification under class imbalance (Appendix~\ref{app:classimbalance}) shows $R^2 \geq 0.976$ even at $P(Z{=}1) = 0.1$ for $K{=}2$, though EC-HTE's RMSE ratio relative to global correction increases to 1.06--1.68 as imbalance grows.
81	Empirical verification (Section~\ref{sec:bias_mechanism}) yields $R^2 = 0.994$ for $K{=}2$ and $R^2 = 0.974$ for $K{=}4$, closing the theory-practice gap to essentially zero; the residual variance reflects Monte Carlo noise, not model misspecification.
82	
83	\paragraph{Sensitivity to (A1).}
84	Assumption~(A1) is not empirically testable.
85	If misclassification correlates with potential outcomes ($\gamma = \mathrm{Corr}(\mathbb{1}[\hat{Z} {\neq} Z],\, Y(1){-}Y(0) \mid Z, S) \neq 0$), Theorem~\ref{thm:bias_identity} gains an $O(\gamma)$ perturbation; in NLP settings, this is plausible when LLM accuracy varies with outcome magnitude.
86	Sensitivity analysis frameworks~\cite{lash2009applying,dorn2022sharp,cinelli2020making} can bound the degradation (Section~\ref{sec:limitations}).
87	
88	\paragraph{Finite-sample remainder.}
89	Theorem~\ref{thm:bias_identity} is a population-level identity.
90	In practice, confusion matrices are estimated from $n_{\text{expert}}$ expert labels with $\hat{C}_s = C_s + E_s$, $\|E_s\| = O_p(n_{\text{expert}}^{-1/2})$; the resulting remainder is therefore $R_n = O_p(n_{\text{expert}}^{-1/2} \cdot \kappa(C_s))$, motivating the singularity guard ($\kappa > 100 \to$ fallback) in Section~\ref{sec:method}.
91	
92	\begin{proposition}[Debiasing Can Increase Bias]
93	\label{prop:debiasing_hurts}
94	Under \textnormal{(A1)--(A5)}, global correction produces larger absolute bias than the naive estimator ($|\mathrm{bias}_{\mathrm{global}}| > |\mathrm{bias}_{\mathrm{naive}}|$) in subgroup $s$ if and only if
95	\begin{equation}
96	\frac{|\delta_s|}{(1 - 2\bar{\pi}) \cdot \pi_s} > 1.
97	\label{eq:hurts_condition}
98	\end{equation}
99	\end{proposition}
100	
101	Equation~\eqref{eq:hurts_condition} partitions subgroups into two regimes:
102	\begin{itemize}
103	    \item \textit{High-error} ($\pi_s > \bar{\pi}$): the condition reduces to $\pi_s > 0.5$, excluded by~(A4); global correction always reduces bias.
104	    \item \textit{Low-error} ($\pi_s < \bar{\pi}$): the condition holds whenever $\pi_s < \bar{\pi} / (2(1 - \bar{\pi}))$---easily satisfied: when $\bar{\pi} = 0.15$, any subgroup with $\pi_s < 0.088$ is harmed by global correction.
105	\end{itemize}
106	The mechanism is over-correction: for subgroups with near-zero misclassification ($\pi_s \approx 0$), the naive estimator is nearly unbiased, yet global inversion calibrated for $\bar{\pi}$ creates substantial bias---debiasing is worse than doing nothing, and can reverse bias sign across subgroups.
107	
108	In our experiments (Section~\ref{sec:bias_mechanism}), global correction increases bias in 50\% of $K{=}2$ configurations (260/520), with amplification reaching $2.86\times$ ($K{=}2$) and $2.41\times$ ($K{=}4$); Figure~\ref{fig:heatmap} visualizes the full parameter grid.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5eebcd3e-6fba-4d9c-9868-9d1d6cdbc79d",
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "06b607cc-49b3-4644-bda3-ccfac6aea9f9",
  "sourceToolAssistantUUID": "5eebcd3e-6fba-4d9c-9868-9d1d6cdbc79d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-23T19:22:26.713Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Wbs4DGMhemntVEE32WEEXR`</summary>

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
  "parentUuid": "06b607cc-49b3-4644-bda3-ccfac6aea9f9",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3Z6ogphcidA7462ncp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a97d91a-4747-4083-b25c-f89e2a181a9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaawH9tFnppryWcn8UcbTw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9114,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9114,
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

_source line 15 · 2026-05-23T19:22:26.718Z_

<details><summary>↩ Tool result · `toolu_01Wbs4DGMhemntVEE32WEEXR`</summary>

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
10	Robustness validation covers hate speech, six OpenAI models, subgroup misspecification, asymmetric confusion matrices, confounded treatment, outcome-dependent misclassification (all $\geq$93.5\% coverage), and treatment-dependent misclassification ($\approx$90\% at $\gamma_T \leq 0.05$; Appendices~\ref{app:hatespeech}--\ref{app:treatment_dep}).
11	
12	\subsection{Empirical Validation of the Bias Identity}
13	\label{sec:bias_mechanism}
14	
15	We verify Theorem~\ref{thm:bias_identity} on a $K{=}2$ grid (520 configurations, $\Delta\pi \in [0, 0.25]$, $\Delta\tau \in (0, 0.50]$) and a $K{=}4$ grid (Appendix~\ref{app:dgp}).
16	Regressing observed subgroup bias on $\delta_s \cdot \Delta\tau / (1{-}2\bar{\pi})$ yields $R^2 = 0.994$ ($K{=}2$) and $0.974$ ($K{=}4$); residual variance reflects MC noise ($R^2 \geq 0.976$ even at $P(Z{=}1) = 0.1$; Appendix~\ref{app:classimbalance}).
17	Global correction worsens bias in 50\% of $K{=}2$ configurations (260/520, excluding $\Delta\pi{=}0$), with amplification reaching 2.86$\times$ ($K{=}2$) and 2.41$\times$ ($K{=}4$); Figure~\ref{fig:heatmap} visualizes the amplification surface.
18	Beyond amplification, global correction reverses the sign of estimated CATE---concluding a protective treatment is harmful---in 14.9\% of configurations at $\tau(0) = 0.03$ (31\% at $\tau(0) = 0.01$; critical threshold $\tau(0) < 0.089$, matching Theorem~\ref{thm:bias_identity}), with all eight real LLMs amplifying bias under global correction; EC-HTE eliminates sign reversal entirely (Figure~\ref{fig:sign_reversal}; Appendix~\ref{app:policy_reversal}).
19	
20	\subsection{EC-HTE Evaluation}
21	\label{sec:ec_hte_eval}
22	
23	Table~\ref{tab:main_results} presents the main results across representative configurations.
24	In the $K{=}2$ extreme row, global correction \emph{increases} $|\text{bias}|$ relative to naive (0.059 vs.\ 0.058), confirming the over-correction mechanism of Theorem~\ref{thm:bias_identity}.
25	F-L scalar correction increases $|\text{bias}|$ to 0.122 (coverage 0.68); F-L per-subgroup to 0.168 as $(1{-}2\pi_s) \to 0$---both worse than naive (Table~\ref{tab:main_results}).
26	HB EC-HTE reduces $|\text{bias}|$ from 0.059 to 0.008 (7.4$\times$) at $K{=}2$ and from 0.056 to 0.012 (4.7$\times$) at $K{=}4$, maintaining near-nominal coverage (0.94--0.96) with lower RMSE than stratified MLE.
27	Under moderate heterogeneity and in TweetEval ($K{=}4$), methods converge ($p > 0.05$); EC-HTE incurs higher RMSE when $\Delta\pi$ is small (Table~\ref{tab:main_supp}).
28	At $K{=}8$ ($n_{\text{expert}}/K{=}31$), coverage remains $\geq$95.6\% but RMSE increases; we recommend $n_{\text{expert}}/K \geq 50$ (Appendix~\ref{app:k8_subgroups}).
29	
30	\paragraph{CausalForest.}
31	Theorem~\ref{thm:bias_identity} applies to any estimator whose inputs pass through a confusion matrix; CausalForest~\cite{wager2018causal} with a noisy effect modifier $\hat{Z}$ inherits the same $M_{\text{global}}^{-1} M_s$ structure.
32	With CausalForest ($K{=}4$, extreme, $n{=}500$), EC-HTE reduces $|\text{bias}|$ from 0.191 to 0.039 (4.9$\times$) with coverage 0.90; global amplifies bias up to 5.9$\times$ (Table~\ref{tab:main_results}; bootstrap SE in Appendix~\ref{app:bootstrap_se}).
33	
34	\begin{table}[t]
35	\centering
36	\caption{Main results (extreme heterogeneity). Metrics averaged over subgroups, $z$-levels, 100 MC runs. Bold: lowest $|\text{bias}|$. $^\dagger$RMSE exceeds Global. F-L Scalar: $\hat{\tau}/(1{-}2\bar{\pi})$~\cite{frazis2003estimating}; F-L Per-sub.: per-subgroup variant (binary $Z$ only). Moderate/TweetEval in Table~\ref{tab:main_supp}; MC SEs in Appendix~\ref{app:mcse}.}
37	\label{tab:main_results}
38	\resizebox{\columnwidth}{!}{%
39	\begin{tabular}{ll ccc}
40	\toprule
41	Configuration & Method & $|\text{Bias}|$ & RMSE & 95\% CI Cov. \\
42	\midrule
43	\multirow{6}{*}{\shortstack[l]{DIM\\$K{=}2$, $n{=}250$}}
44	 & Naive & 0.058 & 0.090 & 0.82 \\
45	 & Global & 0.059 & 0.099 & 0.87 \\
46	 & F-L Scalar & 0.122 & 0.159 & 0.68 \\
47	 & F-L Per-sub. & 0.168 & 0.220 & 0.65 \\
48	 & Strat.\ MLE & 0.012 & 0.094 & 0.95 \\
49	 & HB EC-HTE & \textbf{0.008} & 0.089 & 0.94 \\
50	\midrule
51	\multirow{4}{*}{\shortstack[l]{DIM\\$K{=}4$, $n{=}500$}}
52	 & Naive & 0.062 & 0.113 & 0.88 \\
53	 & Global & 0.056 & 0.125 & 0.91 \\
54	 & Strat.\ MLE & \textbf{0.010} & 0.127$^\dagger$ & 0.95 \\
55	 & HB EC-HTE & 0.012 & 0.120 & 0.96 \\
56	\midrule
57	\multirow{3}{*}{\shortstack[l]{CausalForest\\$K{=}4$, $n{=}500$}}
58	 & Naive & 0.208 & 0.231 & 0.44 \\
59	 & Global & 0.191 & 0.244 & 0.58 \\
60	 & EC-HTE Forest & \textbf{0.039} & 0.180 & 0.90 \\
61	\bottomrule
62	\end{tabular}}
63	\end{table}
64	
65	\subsection{Actionable Diagnostic Without EC-HTE}
66	\label{sec:diagnostic}
67	
68	Proposition~\ref{prop:debiasing_hurts} provides a $\Delta\tau$-free diagnostic: global correction increases bias in subgroup $s$ iff $|\delta_s| / ((1-2\bar{\pi}) \cdot \pi_s) > 1$, computable from a pilot sample without estimating treatment effects.
69	The diagnostic achieves AUC $= 0.63$ across 16 real LLM--dataset combinations; restricting to subgroups with $\Delta\tau > 0$ recovers AUC $= 1.0$ ($0.86$ on synthetic grids; Figure~\ref{fig:roc}, Appendix~\ref{app:screening}).
70	For $K{=}2$, $|\delta_0|{=}|\delta_1|$ limits discrimination; a meta-criterion ($\max_s \mathrm{score}(s) > 1$) recovers reliability for $K{\geq}4$ (Appendix~\ref{app:screening}).
71	
72	The condition number $\kappa(\hat{C}_s)$ provides a practical guard: $\kappa > 100$ triggers fallback; all 13 tested LLM--dataset combinations fall in $\kappa \in (1.25, 3]$ with calibrated coverage $\geq$93\% (Appendix~\ref{app:kappa_analysis}).
73	Budget crossover, $K{=}8$ scalability, and multi-LLM validation ($R^2 = 0.975$) appear in Appendices~\ref{sec:budget}--\ref{app:multilm}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a97d91a-4747-4083-b25c-f89e2a181a9a",
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "a4e4549a-02d4-4134-8416-edc0525b5f9b",
  "sourceToolAssistantUUID": "7a97d91a-4747-4083-b25c-f89e2a181a9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-23T19:22:27.293Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JNtiai8BAQKcSYYRnWUXVF`</summary>

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
  "parentUuid": "a4e4549a-02d4-4134-8416-edc0525b5f9b",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3Z6ogphcidA7462ncp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ccec596-e503-4c62-8ce4-e72f76e834da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaawH9tFnppryWcn8UcbTw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9114,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9114,
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

_source line 17 · 2026-05-23T19:22:27.299Z_

<details><summary>↩ Tool result · `toolu_01JNtiai8BAQKcSYYRnWUXVF`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We derived an exact bias identity (Theorem~\ref{thm:bias_identity}): global confusion-matrix correction introduces bias proportional to $\delta_s \cdot \Delta\tau / (1 - 2\bar{\pi})$, reversing CATE signs in 14.9\% of configurations and amplifying bias in all eight real LLMs tested.
4	EC-HTE eliminates sign reversal via hierarchical Bayesian per-subgroup correction; the diagnostic (Proposition~\ref{prop:debiasing_hurts}; AUC $= 1.0$) flags harmful correction from error rates alone, given sufficient $\Delta\pi$ and expert budget.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ccec596-e503-4c62-8ce4-e72f76e834da",
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "a9841333-3bbf-4ece-97b5-9cb5f108f75f",
  "sourceToolAssistantUUID": "9ccec596-e503-4c62-8ce4-e72f76e834da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-23T19:22:27.707Z_

<details open><summary>🔧 Tool call — Read · `toolu_0148xdTksrc4WTmP21SkCp1u`</summary>

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
  "parentUuid": "a9841333-3bbf-4ece-97b5-9cb5f108f75f",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3Z6ogphcidA7462ncp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34261395-15c5-42fe-bb73-458a9b517958",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaawH9tFnppryWcn8UcbTw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9114,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9114,
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

_source line 19 · 2026-05-23T19:22:27.714Z_

<details><summary>↩ Tool result · `toolu_0148xdTksrc4WTmP21SkCp1u`</summary>

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
11	The hierarchical prior implicitly performs soft merging---subgroups with insufficient data are shrunk toward the global estimate---but explicit hierarchical subgroup merging or adaptive budget allocation may extend the applicability frontier beyond $K{=}8$; we leave these extensions to future work.
12	
13	Assumption~(A1) (conditional independence of misclassification and potential outcomes) is not empirically testable.
14	When LLM accuracy correlates with outcome magnitude---e.g., extreme sentiment is both easier to classify and associated with larger treatment effects---Theorem~\ref{thm:bias_identity} acquires an $O(\gamma)$ perturbation (Section~\ref{sec:theory}).
15	Sensitivity simulation (Appendix~\ref{app:a1_sensitivity}) shows that EC-HTE maintains near-nominal coverage ($\geq$93.5\%) under outcome-dependent misclassification up to $\gamma = 0.2$, with bias increasing only 13.7\%; developing a formal closed-form bound for the $O(\gamma)$ perturbation remains a natural extension~\cite{lash2009applying,dorn2022sharp}.
16	Treatment-dependent misclassification ($P(\hat{Z} \mid Z, T) \neq P(\hat{Z} \mid Z)$), where LLM accuracy varies with treatment status, violates (A1) analogously; EC-HTE maintains $\geq$89.7\% coverage at $\gamma_T \leq 0.05$ but degrades rapidly beyond ($\gamma_T = 0.10$: 75\% coverage; Appendix~\ref{app:treatment_dep}).
17	
18	Oracle experiments confirm CausalForest plug-in SE is well-calibrated (94--96\% coverage with true $Z$ labels); EC-HTE plug-in SE achieves 93.8\% aggregate coverage under standard hyperparameters ($n_{\text{estimators}}{=}200$), with residual under-coverage concentrated in high-error subgroups due to asymmetric $M^{-1}$ SE propagation.
19	A full bootstrap procedure ($B{=}100$; re-estimate CM and re-fit per replicate) recovers $\geq$95\% coverage across all expert budgets tested ($n_{\text{expert}} \in \{25, 50, 75, 100, 200\}$; Appendix~\ref{app:bootstrap_se}); even plug-in SE achieves $\geq$91\% at $n_{\text{expert}}{=}25$.
20	For the DIM estimator, plug-in SE achieves $\geq$95\% coverage across all budgets.
21	
22	The diagnostic (Proposition~\ref{prop:debiasing_hurts}) achieves AUC $= 0.86$ under synthetic symmetric errors but degrades to $0.63$ on real LLM confusion matrices (pooled across 16 model--dataset combinations; Appendix~\ref{app:screening}).
23	For $K{=}2$, the diagnostic anti-predicts because $|\delta_0|{=}|\delta_1|$ forces score differentiation onto $1/\pi_s$ alone, which inversely correlates with actual harm; for binary $Z$, the asymmetric $B_s$-based formulation (Remark~2) is algebraically equivalent and offers no improvement.
24	Performance is strongest for $K{\geq}4$ with moderate asymmetry (AUC $= 0.66$; Appendix~\ref{app:asymmetric}).
25	The diagnostic remains a theoretically grounded criterion---the bias identity's product structure ensures it correctly identifies the \emph{direction} of bias amplification---but should be paired with $R^2$ validation of the bias identity rather than used as a standalone screening rule.
26	
27	All main experiments use symmetric error rates and additive CATE injection ($Y(1) = Y(0) + \tau(Z)$).
28	The bias identity (Theorem~\ref{thm:bias_identity}) generalizes to asymmetric confusion matrices (Appendix~\ref{app:asymmetric}, $R^2 = 0.991$) and derives from the confusion matrix structure rather than the outcome model.
29	While our main experiments use additive CATE injection, a supplementary experiment with multiplicative effects ($Y(1) = Y(0) \times \exp(\tau(Z))$) yields comparable bias reduction (52\%) and nominal coverage (0.955; Appendix~\ref{app:rlearner}), confirming robustness to the functional form of treatment effects.
30	EC-HTE further requires discrete, pre-defined subgroups; subgroup definitions should be pre-specified based on domain knowledge, as data-driven subgroup discovery risks overfitting the confusion matrix structure to sample-specific noise. Continuous effect modifiers or latent subgroup discovery settings require different approaches; discretizing a continuous modifier introduces grouping bias whose magnitude depends on bin width, and intersectional subgroups with many levels may exceed the $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$ budget threshold.
31	Our experiments define subgroups by text features (hashtag presence, text length); demographic subgroups---where prior work documents the most concerning disparities \citep{ashwin2025bias}---require sensitive data access beyond the scope of this study.
32	EC-HTE's correction mechanism is agnostic to subgroup definition: it corrects any per-subgroup confusion-matrix heterogeneity, whether defined by text features, demographics, or other covariates.
33	Ground-truth subgroup CATEs are unavailable in public datasets; classic causal inference benchmarks (e.g., LaLonde, IHDP) lack the LLM annotation step that creates the measurement error our method corrects, precluding direct application. We use synthetic CATE injection on real text features and real LLM annotations.
34	We leave full real-data validation---on a dataset combining RCT design, ground-truth CATEs, and LLM annotations---to future work as suitable public benchmarks become available.
35	Code and data generation scripts will be released upon acceptance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34261395-15c5-42fe-bb73-458a9b517958",
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "d378d81d-fc98-4e18-a740-b2939aaec80e",
  "sourceToolAssistantUUID": "34261395-15c5-42fe-bb73-458a9b517958",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-23T19:22:28.604Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WWzaDFHcLh3RH25aVgcpSm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d378d81d-fc98-4e18-a740-b2939aaec80e",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3Z6ogphcidA7462ncp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d3af63a-db99-42ae-88df-82d63a26d5b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaawH9tFnppryWcn8UcbTw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9114,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9114,
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

_source line 21 · 2026-05-23T19:22:28.667Z_

<details open><summary>🔧 Tool call — Read · `toolu_0187TtpakYwECVQhznDaySRF`</summary>

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
  "parentUuid": "6d3af63a-db99-42ae-88df-82d63a26d5b1",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3Z6ogphcidA7462ncp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20206cd8-b26d-42f9-8e98-95189077c866",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaawH9tFnppryWcn8UcbTw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9114,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9114,
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

_source line 22 · 2026-05-23T19:22:28.673Z_

<details><summary>↩ Tool result · `toolu_0187TtpakYwECVQhznDaySRF`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Measurement error and annotation models.}
5	Classical measurement error theory shows that correction via estimated error models can amplify MSE when the error structure is misspecified~\cite{fuller1987measurement,carroll2006measurement}; Bayesian approaches require informative priors when identification is weak~\cite{gustafson2003measurement}, and nonparametric methods use repeated measurements or instruments to recover the true distribution~\cite{hu2008nonparametric}.
6	
7	Three distinctions separate our contribution from prior measurement error analyses.
8	First, we study effect modifier misclassification---the mismeasured variable defines the CATE function itself---rather than regressor~\cite{frazis2003estimating,carroll2006measurement} or confounder~\cite{ogburn2012nondifferential,greenland1980effect} error, where attenuation is the primary concern.
9	Second, Theorem~\ref{thm:bias_identity} derives a bias identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.
10	Concretely, \citet{frazis2003estimating} derive scalar attenuation for the uncorrected estimator under homogeneous misclassification; Theorem~\ref{thm:bias_identity} characterizes a structurally distinct quantity---correction-induced bias that is subgroup-specific, potentially sign-reversing, and absent from the uncorrected estimator.
11	The homogeneous-error setting ($K{=}1$, $\delta_s{=}0$) is a degenerate case recovering classical attenuation~\cite{blackwell2017unified}; empirically, F-L correction produces higher bias under heterogeneous misclassification, while EC-HTE achieves near-oracle performance (Appendix~\ref{app:fl_comparison}).
12	Third, the $\delta_s \cdot \Delta\tau$ product structure arises only under heterogeneous error rates; all homogeneous-error analyses~\cite{battistin2014treatment,fong2021machine} miss this interaction entirely.
13	In the annotation literature, \citet{dawid1979maximum} introduced confusion matrix estimation for multiple annotators, with extensions to item difficulty, annotator competence, and hierarchical priors~\cite{passonneau2014benefits,hovy2013learning,paun2018comparing}.
14	Our hierarchical estimator (Section~\ref{sec:method}) adapts this architecture from label aggregation to causal inference, tying the prior structure to the subgroup dimension that defines treatment effect heterogeneity.
15	
16	\paragraph{HTE estimation and LLM annotation error.}
17	Causal forests~\cite{athey2016recursive,wager2018causal}, double/debiased ML~\cite{chernozhukov2018dml,semenova2021debiased}, doubly-robust CATE estimators~\cite{kennedy2023dr}, and meta-learners~\cite{kunzel2019metalearners} all assume that covariates defining heterogeneity are observed without error; when the effect modifier is misclassified, CATE estimates conflate effects across groups.
18	EC-HTE provides upstream correction that restores valid inputs to any downstream estimator.
19	The corrected pseudo-outcomes are in principle compatible with other HTE estimators such as the R-learner~\citep{nie2021quasi}.
20	For broader perspectives on causal inference with text data, see \citet{feder2022causal} and \citet{keith2020text}; \citet{wang2020methods} study inference correction when outcomes are ML-predicted, a related but distinct problem from effect modifier misclassification.
21	LLMs now match crowd-worker accuracy on many classification tasks~\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,pangakis2023automated}, but \citet{ashwin2025bias} show that error rates vary by up to $5\times$ across demographic subgroups; \citet{cheng2024err} demonstrate that prompt optimization can reduce such error, a complementary preprocessing step.
22	This subgroup-varying error distorts the very contrasts that define the research question; prior work documents the pattern without correcting downstream causal estimands.
23	Concurrent work identifies variance-side LLM measurement error~\cite{messing2026hidden}; \citet{camuffo2025variance} characterize five variance sources in LLM annotation, complementary to our bias-side analysis.
24	Temperature or Platt scaling~\cite{guo2017calibration} reduces per-subgroup $\pi_s$ but does not eliminate heterogeneity $\Delta\pi$; EC-HTE corrects the residual $\delta_s$-driven bias that persists post-calibration (Appendix~\ref{app:calibration} empirically confirms this complementarity).
25	
26	\paragraph{Prediction-powered and design-based correction.}
27	PPI~\cite{angelopoulos2023ppi,zrnic2024cross} and DSL~\cite{egami2024dsl} correct population-level aggregates assuming homogeneous prediction error.
28	In our setting---binary effect modifier with known subgroup structure, a special case of the broader problems DSL addresses---DSL's measurement error correction reduces, under the confusion-matrix parameterization we adopt, to confusion matrix inversion: pooled DSL is equivalent to our Global baseline, and per-subgroup DSL to Stratified MLE (Section~\ref{sec:ec_hte_eval}; Appendix~\ref{app:ppi_comparison}).
29	EC-HTE adds hierarchical partial pooling across subgroups, borrowing strength to reduce variance---a mechanism outside the DSL framework.
30	\citet{audinet2025benchmarking} benchmark DSL and PPI debiasing for LLM-based parameter estimation, documenting bias-variance tradeoffs analogous to our findings; their analysis targets population-level parameters rather than subgroup-conditional estimands, leaving the $\delta_s \cdot \Delta\tau$ interaction we formalize unaddressed.
31	\citet{mozer2026ppi} extend PPI to arm-specific ATE correction; PPCI~\cite{sui2026ppci} targets conditional estimands but corrects outcome-side error ($\hat{Y}$ given true $Z$), not covariate-side misclassification; ForestIV~\cite{bu2023forestiv} targets the outcome model rather than the heterogeneity structure.
32	None corrects bias when the mismeasured variable is the effect modifier indexing the CATE function.
33	\citet{imai2010causal} study treatment misclassification via instrumental variables or partial identification; \citet{ura2015heterogeneous} extends this to HTE with mismeasured treatment via IV.
34	\citet{miao2018identifying} develop proximal causal inference for unmeasured confounders using proxy variables; our setting differs because $\hat{Z}$ is a moderator proxy rather than a confounder proxy, admitting confusion-matrix correction without the identification constraints of the proximal framework.
35	Extended discussion appears in Appendix~\ref{app:related}.
36	Our validation combines synthetic DGPs, semi-synthetic experiments, and real LLM confusion matrices, consistent with PPI and DSL evaluation methodology; Appendix~\ref{app:multilm} validates both $\Delta\pi$ heterogeneity and the bias identity itself ($R^2 = 0.975$) across 11 model--dataset combinations.
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20206cd8-b26d-42f9-8e98-95189077c866",
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "dbddbfaa-81c8-4a7e-a5f1-63a6c7b72f71",
  "sourceToolAssistantUUID": "20206cd8-b26d-42f9-8e98-95189077c866",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-23T19:22:28.926Z_

<details><summary>↩ Tool result · reported error · `toolu_01WWzaDFHcLh3RH25aVgcpSm`</summary>

```text
File content (39508 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d3af63a-db99-42ae-88df-82d63a26d5b1",
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "41bd00bc-5b90-4077-a4fa-79643ed88537",
  "toolUseResult": "Error: File content (39508 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "6d3af63a-db99-42ae-88df-82d63a26d5b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-23T19:22:31.180Z_

Now let me read the appendix file in chunks since it's too large.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41bd00bc-5b90-4077-a4fa-79643ed88537",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3ZfzicNL5fKgpwrhcZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93859ee4-87f1-4254-a592-5af6bbd8f6fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxEr7WCKWzaUUTRcvcS9ko",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1882,
      "cache_creation_input_tokens": 16288,
      "cache_read_input_tokens": 9114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16288,
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

_source line 25 · 2026-05-23T19:22:32.748Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SVzoCn9jVuj7GhRke7Jx5D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93859ee4-87f1-4254-a592-5af6bbd8f6fd",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3ZfzicNL5fKgpwrhcZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f121af8d-7c07-4598-8524-4f78269f748f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxEr7WCKWzaUUTRcvcS9ko",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1882,
      "cache_creation_input_tokens": 16288,
      "cache_read_input_tokens": 9114,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16288
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1882,
          "output_tokens": 124,
          "cache_read_input_tokens": 9114,
          "cache_creation_input_tokens": 16288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16288,
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

_source line 26 · 2026-05-23T19:22:32.754Z_

<details><summary>↩ Tool result · `toolu_01SVzoCn9jVuj7GhRke7Jx5D`</summary>

```text
1	\section{EC-HTE Procedure}
2	\label{app:algorithm}
3	
4	\begin{algorithm}[t]
5	\caption{EC-HTE: Error-Corrected Heterogeneous Treatment Effects}
6	\label{alg:echte}
7	\begin{algorithmic}[1]
8	\Require Observations $\{(Y_i, W_i, \hat{Z}_i, X_i)\}_{i=1}^N$; expert labels $\{Z_j^*\}_{j=1}^{n_{\text{expert}}}$; subgroup map $S: \mathcal{X} \to \{1,\ldots,K\}$
9	\Ensure Corrected CATE estimates $\hat{\tau}(z)$ with variance-adjusted CIs
10	\Statex
11	\State \textbf{Preconditions:} verify $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$ and $\max_s(\text{FPR}_s, \text{FNR}_s) < 0.5$; if either fails, use global correction
12	\Statex
13	\State \textbf{Step 1: Estimate per-subgroup confusion matrices (HB)}
14	\For{$s = 1, \ldots, K$}
15	    \State $C_s[j,\cdot] \sim \mathrm{Dir}(\alpha_0 \cdot \hat{C}_{\text{global},j})$, \; $\alpha_0$ via empirical Bayes
16	    \State Gibbs sampler (4 chains, 4000 iter) on $\{(\hat{Z}_j, Z_j^*) : S_j = s\}$
17	    \State $\hat{C}_s \gets$ posterior mean; verify $\hat{R} < 1.01$
18	\EndFor
19	\Statex
20	\State \textbf{Step 2: Correct observed outcome moments}
21	\For{$s = 1, \ldots, K$}
22	    \If{$\kappa(\hat{C}_s) > 100$} $\hat{C}_s \gets \bar{C}$ \Comment{singularity guard}
23	    \EndIf
24	    \State $\tilde{\boldsymbol{\mu}}_s \gets \hat{C}_s^{-1} \hat{\boldsymbol{\mu}}_s$
25	\EndFor
26	\Statex
27	\State \textbf{Step 3: CausalForestDML with variance-adjusted SEs}
28	\State Train CausalForest (honest splitting) on corrected outcome moments $\tilde{\boldsymbol{\mu}}_s$
29	\State $\mathrm{se}_{\mathrm{adj},i} \gets \sqrt{\mathrm{diag}(\hat{C}_{S_i}^{-1}\, \mathrm{diag}(\mathrm{se}_i^2)\, \hat{C}_{S_i}^{-\top})}$
30	\State \Return $\hat{\tau}(z)$ with 95\% CIs from $\mathrm{se}_{\mathrm{adj}}$
31	\end{algorithmic}
32	\end{algorithm}
33	
34	\subsection{Condition Number Guard Ablation}
35	\label{app:kappa_ablation}
36	
37	The singularity guard in Algorithm~\ref{alg:echte} (line~6) falls back to global correction when $\kappa(\hat{C}_s) > 100$.
38	We verify that this threshold is not load-bearing by sweeping $\kappa \in \{10, 25, 50, 100, 200, 500, 1000\}$ under the standard DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 100 MC runs).
39	Across all configurations, the maximum observed condition number is $\kappa_{\max} = 1.89$ (mean 1.45, p99 1.89), providing a $53{\times}$ safety margin below the $\kappa{=}100$ threshold.
40	Consequently, the guard never triggers at any tested threshold, and all $\kappa$ values produce identical RMSE (HB: 0.076, Global: 0.077) and zero numerical instability.
41	In a stress test with near-random labeling ($\pi_s \approx 0.4$--$0.5$, $n_{\text{expert}}{=}50$), the maximum condition number reaches 1{,}125, correctly triggering the $\kappa{=}100$ guard and preventing catastrophic inversion.
42	The adaptive formula $\kappa_{\text{adapt}} = 10 \sqrt{n_{\text{expert}} / K}$ recovers $\kappa{=}100$ for this regime and scales naturally with the estimation precision.
43	
44	\section{Full Proof of Theorem~\ref{thm:bias_identity}}
45	\label{app:derivation}
46	
47	\paragraph{Setup.}
48	Under assumptions (A1)--(A4), the observed CATE in subgroup $s$ at effect-modifier level $z$ is
49	\begin{equation}
50	\tau_{\text{obs}}(z, s) = \sum_{z'} M_s[z, z'] \cdot \tau(z'),
51	\end{equation}
52	where $M_s[z, z'] = P(Z{=}z' \mid \hat{Z}{=}z, S{=}s)$ is the mixing matrix.
53	Under (A2)--(A3), $M_s = \bigl[\begin{smallmatrix} 1-\pi_s & \pi_s \\ \pi_s & 1-\pi_s \end{smallmatrix}\bigr]$.
54	
55	\paragraph{Global correction.}
56	The pooled mixing matrix is $M_{\text{global}} = \sum_s w_s M_s = \bigl[\begin{smallmatrix} 1-\bar{\pi} & \bar{\pi} \\ \bar{\pi} & 1-\bar{\pi} \end{smallmatrix}\bigr]$, with $\bar{\pi} = \sum_s w_s \pi_s$.
57	
58	Global correction applies $M_{\text{global}}^{-1}$ to $\tau_{\text{obs}}(\cdot, s)$:
59	\begin{equation}
60	\hat{\tau}_{\text{global}}(z, s) = [M_{\text{global}}^{-1} M_s \cdot \boldsymbol{\tau}]_z,
61	\end{equation}
62	where $\boldsymbol{\tau} = [\tau(0), \tau(1)]^\top$.
63	
64	\paragraph{Bias computation.}
65	The bias is $\hat{\tau}_{\text{global}}(z, s) - \tau(z) = [(M_{\text{global}}^{-1} M_s - I) \boldsymbol{\tau}]_z$.
66	
67	Direct computation gives:
68	\begin{equation}
69	M_{\text{global}}^{-1} = \frac{1}{1 - 2\bar{\pi}} \begin{bmatrix} 1-\bar{\pi} & -\bar{\pi} \\ -\bar{\pi} & 1-\bar{\pi} \end{bmatrix}.
70	\end{equation}
71	Multiplying by $M_s$:
72	\begin{equation}
73	\resizebox{.88\columnwidth}{!}{$\displaystyle
74	M_{\text{global}}^{-1} M_s = \frac{1}{1-2\bar{\pi}} \begin{bmatrix} (1{-}\bar{\pi})(1{-}\pi_s) - \bar{\pi}\pi_s & (1{-}\bar{\pi})\pi_s - \bar{\pi}(1{-}\pi_s) \\ -\bar{\pi}(1{-}\pi_s) + (1{-}\bar{\pi})\pi_s & -\bar{\pi}\pi_s + (1{-}\bar{\pi})(1{-}\pi_s) \end{bmatrix}.
75	$}
76	\end{equation}
77	
78	Define $\delta_s = \pi_s - \bar{\pi}$. Substituting $\pi_s = \bar{\pi} + \delta_s$:
79	\begin{equation}
80	M_{\text{global}}^{-1} M_s - I = \frac{\delta_s}{1-2\bar{\pi}} \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}.
81	\end{equation}
82	
83	To verify: the $(1,1)$ entry of $M_{\text{global}}^{-1} M_s$ is
84	{\small
85	\begin{align}
86	&\frac{(1{-}\bar{\pi})(1{-}\bar{\pi}{-}\delta_s) - \bar{\pi}(\bar{\pi}{+}\delta_s)}{1-2\bar{\pi}} \nonumber\\
87	&= \frac{(1{-}\bar{\pi})^2 - (1{-}\bar{\pi})\delta_s - \bar{\pi}^2 - \bar{\pi}\delta_s}{1-2\bar{\pi}} \nonumber\\
88	&= \frac{1 - 2\bar{\pi} - \delta_s}{1-2\bar{\pi}} = 1 - \frac{\delta_s}{1-2\bar{\pi}}.
89	\end{align}
90	}
91	
92	Applying $(M_{\text{global}}^{-1} M_s - I)$ to $\boldsymbol{\tau}$:
93	{\small
94	\begin{align}
95	\text{bias}(z{=}0, s) &= \tfrac{\delta_s}{1-2\bar{\pi}}(-\tau(0) + \tau(1)) = +\tfrac{\delta_s \cdot \Delta\tau}{1-2\bar{\pi}}, \\
96	\text{bias}(z{=}1, s) &= \tfrac{\delta_s}{1-2\bar{\pi}}(\tau(0) - \tau(1)) = -\tfrac{\delta_s \cdot \Delta\tau}{1-2\bar{\pi}},
97	\end{align}
98	}
99	where $\Delta\tau = \tau(1) - \tau(0)$. \qed
100	
101	\section{Multi-class Extension and Proof}
102	\label{app:multiclass}
103	
104	\begin{corollary}[Multi-class Extension]
105	\label{cor:multiclass}
106	For $K > 2$ subgroups with $J$ effect-modifier levels and uniform off-diagonal misclassification (misclassified observations from class $j$ are distributed equally among the remaining $J{-}1$ classes), the subgroup bias of global correction generalizes to
107	\begin{equation}
108	\mathrm{bias}_{\mathrm{global}}(z, s) = \sum_{j=1}^{J} \bigl(\bar{\pi}_j - \pi_{s,j}\bigr) \cdot \bigl(\tau(j) - \bar{\tau}\bigr) \cdot g(\bar{\pi}),
109	\label{eq:multiclass}
110	\end{equation}
111	where $g(\bar{\pi})$ collects the matrix-inversion amplification terms.\footnote{For $J=3$ with symmetric misclassification (off-diagonal errors uniform), $g(\bar{\pi}) = 1/(1 - 3\bar{\pi}/2)$, generalizing the $J{=}2$ factor $1/(1-2\bar{\pi})$. In general, $g(\bar{\pi}) = 1/(1 - J\bar{\pi}/(J-1))$.}
112	The essential structure, $\sum_s w_s (\bar{\pi}_j - \pi_{s,j}) = 0$, ensures that bias redistributes across subgroups rather than vanishing in aggregate.
113	\end{corollary}
114	
115	\paragraph{Proof.}
116	For $K > 2$ subgroups with $J$ effect-modifier levels, the subgroup-specific mixing matrix $M_s$ is $J \times J$ with entries $M_s[j, j'] = P(Z{=}j' \mid \hat{Z}{=}j, S{=}s)$.
117	The global mixing matrix is $M_{\text{global}} = \sum_s w_s M_s$.
118	
119	The bias of global correction in subgroup $s$ at level $z$ is:
120	\begin{equation}
121	\text{bias}_{\text{global}}(z, s) = [(M_{\text{global}}^{-1} M_s - I) \boldsymbol{\tau}]_z.
122	\end{equation}
123	
124	Write $M_s = M_{\text{global}} + \Delta_s$ where $\Delta_s = M_s - M_{\text{global}}$ satisfies $\sum_s w_s \Delta_s = 0$.
125	Then $M_{\text{global}}^{-1} M_s = I + M_{\text{global}}^{-1} \Delta_s$, so:
126	\begin{equation}
127	\text{bias}_{\text{global}}(z, s) = [M_{\text{global}}^{-1} \Delta_s \cdot \boldsymbol{\tau}]_z.
128	\end{equation}
129	
130	For symmetric misclassification with per-class error rates $\pi_{s,j}$ and pooled rates $\bar{\pi}_j$, the entries of $\Delta_s$ have the form $\Delta_s[j,j'] = (\bar{\pi}_j - \pi_{s,j}) \cdot h(j, j')$ for a function $h$ determined by the off-diagonal redistribution pattern.
131	Expanding the matrix-vector product and collecting terms yields:
132	\begin{equation}
133	\text{bias}_{\text{global}}(z, s) = \sum_{j=1}^{J} (\bar{\pi}_j - \pi_{s,j}) \cdot (\tau(j) - \bar{\tau}) \cdot g(\bar{\pi}),
134	\end{equation}
135	where $g(\bar{\pi})$ collects the matrix-inversion amplification terms and $\bar{\tau} = \sum_j P(Z{=}j) \tau(j)$.
136	
137	The essential structure $\sum_s w_s (\bar{\pi}_j - \pi_{s,j}) = 0$ ensures that the weighted bias across subgroups sums to zero: global correction redistributes bias rather than creating or eliminating it in aggregate.
138	For non-uniform off-diagonal entries, the scalar amplification $g(\bar{\pi})$ generalizes to a cell-specific matrix; the product structure $B_s \cdot \Delta\tau$ persists but a closed-form amplification factor does not. \qed
139	
140	\section{Proof of Proposition~\ref{prop:debiasing_hurts}}
141	\label{app:debiasing_hurts}
142	
143	The naive estimator has bias $\tau_{\text{obs}}(z,s) - \tau(z)$.
144	Under (A2)--(A3), $\tau_{\text{obs}}(0,s) = (1-\pi_s)\tau(0) + \pi_s\tau(1)$, so $\text{bias}_{\text{naive}}(0,s) = \pi_s \cdot \Delta\tau$.
145	
146	Global correction produces larger absolute bias when $|\text{bias}_{\text{global}}(0,s)| > |\text{bias}_{\text{naive}}(0,s)|$:
147	\begin{equation}
148	\frac{|\delta_s| \cdot |\Delta\tau|}{|1-2\bar{\pi}|} > \pi_s \cdot |\Delta\tau|.
149	\end{equation}
150	Since $\Delta\tau \neq 0$ (otherwise both biases are zero), dividing through gives:
151	\begin{equation}
152	\frac{|\delta_s|}{(1-2\bar{\pi}) \cdot \pi_s} > 1,
153	\end{equation}
154	where we use $1-2\bar{\pi} > 0$ from (A4).
155	
156	For high-error subgroups ($\pi_s > \bar{\pi}$, so $\delta_s > 0$): the condition becomes $(\pi_s - \bar{\pi}) / ((1-2\bar{\pi})\pi_s) > 1$, which simplifies to $\pi_s(1 - 1 + 2\bar{\pi}) > \bar{\pi}$, i.e., $2\bar{\pi}\pi_s > \bar{\pi}$, i.e., $\pi_s > 0.5$.
157	This is excluded by (A4), so global correction always reduces bias in high-error subgroups.
158	
159	For low-error subgroups ($\pi_s < \bar{\pi}$, so $\delta_s < 0$): the condition becomes $(\bar{\pi} - \pi_s) / ((1-2\bar{\pi})\pi_s) > 1$, which gives $\pi_s < \bar{\pi} / (1 - 2\bar{\pi} + 1) = \bar{\pi} / (2(1-\bar{\pi}))$.
160	When $\bar{\pi} = 0.15$, any subgroup with $\pi_s < 0.088$ experiences increased bias from global correction. \qed
161	
162	\paragraph{Extension to asymmetric misclassification.}
163	Proposition~\ref{prop:debiasing_hurts} assumes symmetric error rates (A2).
164	Under asymmetric misclassification ($\mathrm{FPR}_s \neq \mathrm{FNR}_s$), the naive bias becomes $\mathrm{bias}_{\mathrm{naive}}(0,s) = \mathrm{FPR}_s \cdot \tau(1) + (1 - \mathrm{FPR}_s - 1)\tau(0)$ and the global correction bias depends on the full $2 \times 2$ structure of $B_s = M_{\mathrm{global}}^{-1} M_s - I$ (Remark~1 in Section~\ref{sec:theory}).
165	A sufficient condition for global correction to increase bias is
166	\begin{equation}
167	\|B_s\|_\infty > \max(\mathrm{FPR}_s, \mathrm{FNR}_s),
168	\end{equation}
169	which reduces to Equation~\eqref{eq:hurts_condition} when $\mathrm{FPR}_s = \mathrm{FNR}_s = \pi_s$.
170	In the asymmetric experiments (Appendix~\ref{app:asymmetric}), the symmetric diagnostic still achieves AUC $= 0.66$ when applied with $\pi_s = (\mathrm{FPR}_s + \mathrm{FNR}_s)/2$, suggesting practical robustness.
171	A fully general asymmetric diagnostic that accounts for the separate roles of FPR and FNR in each entry of $B_s$ is left to future work.
172	
173	\section{Semi-Synthetic Data Generating Process}
174	\label{app:dgp}
175	
176	\paragraph{Synthetic DGP (Sections~\ref{sec:bias_mechanism}--\ref{sec:diagnostic} and Appendix~\ref{sec:budget}).}
177	We generate $N = 5000$ observations.
178	Each observation belongs to one of $K \in \{2, 4\}$ subgroups $S \in \{1, \ldots, K\}$ with equal weights $w_s = 1/K$.
179	The binary effect modifier $Z \in \{0, 1\}$ is drawn with $P(Z{=}1) = 0.5$.
180	Treatment assignment is $T \sim \text{Bernoulli}(0.5)$, independent of $Z$ and $S$.
181	
182	The outcome is generated as:
183	\begin{equation}
184	Y = \tau(Z) \cdot T + \eta, \quad \eta \sim \mathcal{N}(0, 1),
185	\end{equation}
186	where the CATE function is $\tau(z) = \bar{\tau} + \Delta\tau \cdot (z - 0.5)$ with $\bar{\tau} = 0.5$.
187	The CATE heterogeneity $\Delta\tau \in \{0, 0.2, 0.5, 1.0\}$ controls the strength of treatment effect variation across levels of $Z$.
188	
189	Misclassification is symmetric: $\hat{Z} \neq Z$ with probability $\pi_s$ depending on subgroup.
190	For $K{=}2$: $\pi_1 = \bar{\pi} - \Delta_c/2$, $\pi_2 = \bar{\pi} + \Delta_c/2$, with $\bar{\pi} \in \{0.1, 0.2\}$ and $\Delta_c \in \{0, 0.05, 0.1, 0.15\}$.
191	For $K{=}4$, extreme regime: $\pi \in \{0.05, 0.10, 0.15, 0.25\}$; moderate regime: $\pi \in \{0.08, 0.12, 0.16, 0.20\}$.
192	
193	Expert labels are drawn as a simple random sample of size $n_{\text{expert}} \in \{50, 100, 250, 500, 1000, 2000\}$ from the full dataset, with true $Z$ observed for these observations.
194	
195	\paragraph{Semi-synthetic DGP (Section~\ref{sec:ec_hte_eval}).}
196	We sample $N = 5000$ tweets from the TweetEval sentiment corpus ($N_{\text{pool}} = 57{,}899$).
197	Subgroups are defined by crossing \texttt{has\_hashtag} $\times$ \texttt{text\_length\_bin} (short/medium/long), yielding $K = 4$ subgroups with empirical sizes: $S_0 \approx 38\%$, $S_1 \approx 38\%$, $S_2 \approx 12\%$, $S_3 \approx 12\%$.
198	Misclassification rates in the extreme regime are $\pi_{S_0} = 0.05$, $\pi_{S_1} = 0.10$, $\pi_{S_2} = 0.15$, $\pi_{S_3} = 0.25$, reflecting empirical evidence that hashtag-heavy text degrades LLM classifier accuracy.
199	The outcome DGP follows the same structure as the synthetic case, with CATE injected onto the real text-derived subgroup structure.
200	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f121af8d-7c07-4598-8524-4f78269f748f",
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "aebb698b-e5fa-4c5b-bf49-3dc9b7e06836",
  "sourceToolAssistantUUID": "f121af8d-7c07-4598-8524-4f78269f748f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T19:22:36.991Z_

<details open><summary>🔧 Tool call — Read · `toolu_013zw4jaWH64A2n39C6pWgzY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 200,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aebb698b-e5fa-4c5b-bf49-3dc9b7e06836",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3ZxhoNLZJkYLGccgdT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b4329f7-b5d8-4c52-bd63-7a5b948b8bd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1r7SHtr9HsMve4XeAMiY5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8126,
      "cache_read_input_tokens": 25402,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8126
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 25402,
          "cache_creation_input_tokens": 8126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8126,
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

_source line 28 · 2026-05-23T19:22:36.998Z_

<details><summary>↩ Tool result · `toolu_013zw4jaWH64A2n39C6pWgzY`</summary>

```text
200	
201	\paragraph{PPCI DGPs (Appendix~\ref{sec:ppci}).}
202	Four DGPs isolate error types: (A) covariate error only ($\sigma_{\text{outcome}} = 0$), (B) outcome error only ($\sigma_{\text{outcome}} = 0.5$), (C) both errors ($\sigma_{\text{outcome}} = 0.5$), (D) no error ($\sigma_{\text{outcome}} = 0$).
203	Outcome-side error is additive Gaussian noise on $Y$.
204	
205	\paragraph{CausalForestDML hyperparameters.}
206	All CausalForest experiments use \texttt{econml.dml.CausalForestDML} with honest splitting, $n_{\text{estimators}} = 48$, $\texttt{min\_samples\_leaf} = 20$, \texttt{model\_y} = \texttt{LassoCV}(cv=3), and \texttt{model\_t} = \texttt{LogisticRegressionCV}.
207	These defaults were held constant across all configurations; no hyperparameter tuning was performed.
208	
209	\begin{figure*}[t]
210	\centering
211	\includegraphics[width=\textwidth]{figures/fig2_heatmap.pdf}
212	\caption{Bias amplification under global correction ($K{=}2$). (a) Low-error subgroup: correction always helps. (b) High-error subgroup: correction \emph{increases} bias when $\Delta\pi > 0.12$ (hatched), reaching 2.86$\times$.}
213	\label{fig:heatmap}
214	\end{figure*}
215	
216	\section{Extended Related Work}
217	\label{app:related}
218	
219	\paragraph{Measurement error details.}
220	\citet{fuller1987measurement} establish the foundational theory showing that naive regression with mismeasured covariates yields attenuated coefficient estimates.
221	\citet{carroll2006measurement} extend this to nonlinear models.
222	\citet{gustafson2003measurement} develops Bayesian treatments modeling measurement jointly with outcomes.
223	\citet{hu2008nonparametric} provide nonparametric identification using repeated measurements or instruments.
224	
225	\paragraph{Annotation model extensions.}
226	Beyond the foundational \citet{dawid1979maximum} model, \citet{passonneau2014benefits} incorporate item difficulty, \citet{hovy2013learning} learn annotator competence, and \citet{paun2018comparing} introduce hierarchical priors sharing information across annotators with varying expertise.
227	
228	\paragraph{PPI extensions and text-as-data methods.}
229	\citet{zrnic2024cross} extend PPI via cross-prediction; their active inference framework~\citep{zrnic2024active} achieves $>$80\% expert budget savings through adaptive allocation, complementary to our fixed-budget analysis.
230	\citet{grimmer2022text} provide methodological guidance for text-as-data pipelines.
231	\citet{audinet2025benchmarking} systematically benchmark DSL and PPI methods for LLM-based parameter estimation, finding that debiasing can increase MSE when prediction error is heterogeneous---a population-level analogue of the subgroup-conditional bias amplification we formalize in Theorem~\ref{thm:bias_identity}.
232	
233	\paragraph{Treatment vs.\ effect-modifier misclassification.}
234	\citet{imai2010causal} study treatment misclassification where errors change which arm a unit is assigned to, requiring instrumental variables or partial identification because the fundamental treated-vs-control contrast is corrupted.
235	Our problem preserves the treatment contrast ($T$ is observed correctly) but corrupts the heterogeneity structure ($\hat{Z} \neq Z$).
236	The ATE remains identified; only conditional effects are biased, which makes exact correction through confusion matrix inversion feasible.
237	
238	\paragraph{Econometrics of binary misclassification.}
239	\citet{bound2001measurement} survey measurement error in survey data, establishing that binary misclassification attenuates regression coefficients.
240	\citet{frazis2003estimating} derive exact bias formulas for OLS with a misclassified binary regressor, showing attenuation proportional to the misclassification rate---analogous to our Theorem~\ref{thm:bias_identity} but restricted to average effects without subgroup heterogeneity.
241	\citet{black2000racial} demonstrate that racial misclassification in administrative data can substantially bias estimates of racial disparities.
242	\citet{mahajan2006identification} and \citet{lewbel2007estimation} develop instrumental variable approaches to identify models with misclassified binary regressors, requiring exclusion restrictions unavailable when the mismeasured variable is an LLM annotation.
243	Our setting differs in three respects: (i) the mismeasured variable is an effect modifier indexing the CATE function, not a standard regressor; (ii) misclassification rates vary across subgroups, creating the $\delta_s \times \Delta\tau$ product amplification absent from homogeneous-error analyses; and (iii) expert labels provide a direct calibration sample, enabling confusion matrix estimation without instruments.
244	
245	\section{MCMC Convergence Diagnostics}
246	\label{app:mcmc}
247	
248	Table~\ref{tab:mcmc} reports convergence diagnostics for the hierarchical Bayesian confusion matrix estimator across all experimental configurations.
249	All runs use 4 chains with 4000 iterations (2000 warmup).
250	Main experiments (Table~\ref{tab:main_results}) use a Dirichlet prior centered on $\hat{C}_{\text{global}}$ with concentration $\alpha_0$ estimated via empirical Bayes (marginal likelihood).
251	Appendix robustness experiments use a fixed Dirichlet prior ($\alpha{=}3$); since fixed-$\alpha$ partial pooling is weakly dominated by the adaptive variant, these results are conservative.
252	This budget is sufficient for the $2{\times}2$ Dirichlet-Multinomial posterior; all runs achieve $\hat{R} < 1.0034$ and ESS $> 1618$, confirming convergence with substantial margin.
253	
254	\begin{table}[h]
255	\centering
256	\small
257	\begin{tabular}{lcc}
258	\toprule
259	Diagnostic & Threshold & Achieved \\
260	\midrule
261	$\hat{R}$ (max across all params) & $< 1.01$ & $< 1.0034$ \\
262	ESS (min across all params) & $> 845$ & $> 1618$ \\
263	Divergent transitions & $= 0$ & $0$ \\
264	Singularity guard triggers & --- & extreme/$n{=}50$ only \\
265	\bottomrule
266	\end{tabular}
267	\caption{MCMC convergence diagnostics for the hierarchical Bayesian estimator. All configurations satisfy convergence criteria with substantial margin.}
268	\label{tab:mcmc}
269	\end{table}
270	
271	\paragraph{Hyperprior sensitivity.}
272	Scaling the $\text{Gamma}(3, 1)$ hyperprior by factors of $0.5\times$ to $2\times$ produces $<$1\% RMSE variation for $K{=}2$ and $\sim$4--5\% for $K{=}4$.
273	Coverage remains invariant across the sensitivity range.
274	These results confirm that the hierarchical estimator is robust to prior specification within a reasonable range.
275	
276	\section{Diagnostic ROC Curves}
277	\label{app:roc}
278	
279	\begin{figure}[t]
280	\centering
281	\includegraphics[width=\columnwidth]{figures/fig4_roc.png}
282	\caption{ROC curves for the $\Delta\tau$-free diagnostic (Proposition~\ref{prop:debiasing_hurts}): $|\delta_s|/((1{-}2\bar\pi)\cdot\pi_s)>1$. (A)~Setting-level ROC (AUC $= 0.89$), compared with the $|\Delta\pi \times \Delta\tau|$ product (AUC $= 0.89$) and $\mathrm{CV}(\pi_s)$ (AUC $= 0.97$). (B)~Subgroup-level ROC: the $\Delta\pi$-only condition (AUC $= 0.86$) substantially outperforms the $|\Delta\pi \times \Delta\tau|$ product (AUC $= 0.73$). The $\Delta\tau$-free diagnostic depends only on estimable misclassification rates, breaking the circular dependency that would arise if CATE heterogeneity were required.}
283	\label{fig:roc}
284	\end{figure}
285	
286	\paragraph{Cost-asymmetric diagnostic thresholds.}
287	In practice, the cost of a false negative (failing to detect that global correction increases bias) exceeds the cost of a false positive (unnecessarily applying EC-HTE when global correction would suffice), because the former propagates systematic bias into CATE estimates while the latter only incurs additional estimation variance.
288	Practitioners in high-stakes settings (e.g., policy evaluation where CATE estimates inform resource allocation) should lower the diagnostic threshold to favor recall over precision, accepting more false positives to minimize the risk of undetected bias amplification.
289	
290	\section{Expert Budget Crossover Curves}
291	\label{app:budget}
292	\label{sec:budget}
293	
294	The crossover point at which EC-HTE achieves lower RMSE than global correction is $n_{\text{expert}} = 250$ for $K{=}2$/extreme and $n_{\text{expert}} = 1000$ for $K{=}4$/extreme (Figure~\ref{fig:budget}).
295	Under moderate heterogeneity ($K{=}2$), EC-HTE never achieves lower RMSE than global at any budget.
296	HB partial pooling improves over stratified MLE in 21 of 24 configurations, with the two estimators converging by $n_{\text{expert}} \geq 1000$.
297	
298	\begin{figure*}[t]
299	\centering
300	\includegraphics[width=\textwidth]{figures/fig3_budget.pdf}
301	\caption{RMSE vs.\ expert budget ($n_{\text{expert}}$) across four regime$\times K$ combinations. Dashed vertical lines mark crossover points where EC-HTE achieves lower RMSE than global correction: $n{=}250$ ($K{=}2$, extreme), $n{=}1000$ ($K{=}4$, extreme). Under moderate heterogeneity ($K{=}2$), global correction dominates at all budgets. Shaded bands show $\pm 1$ SD across subgroups within each configuration.}
302	\label{fig:budget}
303	\end{figure*}
304	
305	\subsection{Budget Sensitivity: HB vs.\ Stratified MLE}
306	\label{app:budget_sensitivity}
307	
308	Hierarchical Bayes (HB) partial pooling borrows strength across subgroups, which should matter most when per-subgroup expert labels are scarce.
309	We sweep $n_{\text{expert}} \in \{25, 50, 75, 100, 150, 250\}$ under extreme heterogeneity ($\Delta\tau{=}0.3$, 100 MC runs, $N{=}5{,}000$).
310	Table~\ref{tab:budget_sensitivity} reports aggregate RMSE for global correction, stratified MLE, and HB EC-HTE.
311	
312	\begin{table}[h]
313	\centering
314	\caption{RMSE across expert budgets under extreme heterogeneity.
315	HB crossover (first budget where HB $<$ MLE) occurs at approximately 10 expert labels per subgroup-cell:
316	$n_{\text{expert}}{=}50$ for $K{=}2$ and $n_{\text{expert}}{=}75$ for $K{=}4$.}
317	\label{tab:budget_sensitivity}
318	\small
319	\begin{tabular}{crrrrc}
320	\toprule
321	$K$ & $n_{\text{expert}}$ & Global & Strat.\ MLE & HB EC-HTE & HB vs.\ MLE \\
322	\midrule
323	2 & 25 & \textbf{0.101} & 0.256 & 0.269 & $+4.9\%$ \\
324	2 & 50 & \textbf{0.088} & 0.275 & 0.231 & $\mathbf{-16.1\%}$ \\
325	2 & 75 & 0.084 & 0.091 & \textbf{0.089} & $-1.9\%$ \\
326	2 & 100 & 0.083 & 0.085 & \textbf{0.084} & $-0.8\%$ \\
327	2 & 150 & 0.081 & 0.077 & \textbf{0.077} & $-0.4\%$ \\
328	2 & 250 & 0.080 & 0.075 & \textbf{0.074} & $-0.1\%$ \\
329	\midrule
330	4 & 25 & \textbf{0.129} & 0.401 & 0.612 & $+52.5\%$ \\
331	4 & 50 & \textbf{0.117} & 0.380 & 0.470 & $+23.8\%$ \\
332	4 & 75 & \textbf{0.112} & 0.221 & 0.211 & $\mathbf{-4.4\%}$ \\
333	4 & 100 & \textbf{0.112} & 0.215 & 0.212 & $-1.3\%$ \\
334	4 & 150 & \textbf{0.109} & 0.157 & 0.152 & $-3.6\%$ \\
335	4 & 250 & \textbf{0.108} & 0.127 & 0.126 & $-1.0\%$ \\
336	\bottomrule
337	\end{tabular}
338	\end{table}
339	
340	Three regimes emerge.
341	At very low budgets ($n_{\text{expert}} < 50$ for $K{=}2$, $< 75$ for $K{=}4$), per-subgroup counts are insufficient for reliable confusion matrix estimation; global pooling dominates because the variance cost of stratification overwhelms any bias reduction.
342	HB degrades substantially in this regime because the Gibbs posterior, while better regularized than MLE, still cannot overcome the fundamental sample-size constraint with $\sim$6--12 labels per subgroup.
343	At moderate budgets ($n_{\text{expert}} = 50$--$250$ for $K{=}2$, $75$--$250$ for $K{=}4$), HB partial pooling provides consistent RMSE improvement over stratified MLE ($-0.4\%$ to $-16.1\%$), with the largest gains near the crossover point.
344	At high budgets ($n_{\text{expert}} \geq 250$), both estimators converge as subgroup-level data becomes sufficient for reliable MLE; the HB advantage diminishes to $< 1\%$.
345	Coverage remains $\geq 0.88$ for both methods across all budget levels.
346	
347	\subsection{Scalability to $K{=}8$ Subgroups}
348	\label{app:k8_subgroups}
349	
350	We test EC-HTE at $K{=}8$ to identify the scalability boundary of hierarchical Bayesian partial pooling under fixed expert budget.
351	
352	\paragraph{Setup.}
353	$N{=}5{,}000$, $K{=}8$ (equal-weight subgroups), $n_{\text{expert}}{=}250$ (${\approx}31$ labels per subgroup), 100 MC replications.
354	Misclassification rates are uniformly spread: $\pi_s \in \{0.05, 0.09, 0.13, 0.18, 0.22, 0.26, 0.30, 0.35\}$.
355	Treatment effects depend on $Z$ (not subgroup): $\tau(Z{=}0){=}0$, $\tau(Z{=}1){=}0.3$.
356	
357	\begin{table}[h]
358	\centering
359	\caption{EC-HTE at $K{=}8$ ($n_{\text{expert}}{=}250$, ${\approx}31$ labels/subgroup, 100 MC).}
360	\label{tab:k8_subgroups}
361	\small
362	\begin{tabular}{lccc}
363	\toprule
364	Method & Coverage & RMSE & $|\text{Bias}|$ \\
365	\midrule
366	Oracle       & 0.944 & 0.113 & 0.090 \\
367	Global       & 0.951 & 0.168 & 0.135 \\
368	HB EC-HTE    & 0.956 & 0.340 & 0.183 \\
369	Strat MLE    & 0.953 & 0.638 & 0.219 \\
370	Naive        & 0.913 & 0.133 & 0.107 \\
371	\bottomrule
372	\end{tabular}
373	\end{table}
374	
375	All CM-aware methods achieve nominal coverage at $K{=}8$: HB EC-HTE 95.6\%, Strat MLE 95.3\%, Global 95.1\%.
376	HB partial pooling achieves a 47\% RMSE reduction over stratified MLE (0.340 vs.\ 0.638), confirming that hierarchical shrinkage provides substantial regularization.
377	However, HB RMSE (0.340) exceeds global correction (0.168), indicating that ${\approx}31$ expert labels per subgroup are insufficient for per-subgroup CM estimation to outweigh variance inflation.
378	
379	\paragraph{Per-subgroup breakdown.}
380	Table~\ref{tab:k8_per_subgroup} decomposes RMSE by subgroup.
381	
382	\begin{table}[h]
383	\centering
384	\caption{Per-subgroup RMSE at $K{=}8$. HB improvement over MLE is largest in high-$\pi$ subgroups but does not close the gap with Global.}
385	\label{tab:k8_per_subgroup}
386	\small
387	\begin{tabular}{cccccc}
388	\toprule
389	Subgroup & $\pi_s$ & HB RMSE & MLE RMSE & Global RMSE & HB Cov \\
390	\midrule
391	$s_0$ & 0.050 & 0.136 & 0.134 & \textbf{0.181} & 0.950 \\
392	$s_1$ & 0.093 & 0.133 & 0.132 & \textbf{0.154} & 0.970 \\
393	$s_2$ & 0.136 & 0.154 & 0.154 & 0.161 & 0.975 \\
394	$s_3$ & 0.179 & 0.178 & 0.182 & \textbf{0.159} & 0.945 \\
395	$s_4$ & 0.221 & 0.263 & 0.343 & \textbf{0.163} & 0.940 \\
396	$s_5$ & 0.264 & 0.421 & 0.711 & \textbf{0.164} & 0.965 \\
397	$s_6$ & 0.307 & 0.634 & 1.375 & \textbf{0.177} & 0.940 \\
398	$s_7$ & 0.350 & 0.432 & 0.809 & \textbf{0.183} & 0.960 \\
399	\bottomrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b4329f7-b5d8-4c52-bd63-7a5b948b8bd1",
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "b8aa5b88-a10a-4de8-a6c2-a7b91050dd74",
  "sourceToolAssistantUUID": "8b4329f7-b5d8-4c52-bd63-7a5b948b8bd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T19:22:40.709Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XYXGfsqPqTdfD8V3SE156p`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 400,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8aa5b88-a10a-4de8-a6c2-a7b91050dd74",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3aGvRdZ8Xn4VXnaCHA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84d8a185-da4a-435d-bc0d-829c32e3d5cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxMtST8KWy3hxaXvaoVwxS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5481,
      "cache_read_input_tokens": 33528,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5481
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 33528,
          "cache_creation_input_tokens": 5481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5481,
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

_source line 30 · 2026-05-23T19:22:40.726Z_

<details><summary>↩ Tool result · `toolu_01XYXGfsqPqTdfD8V3SE156p`</summary>

```text
400	\end{tabular}
401	\end{table}
402	
403	RMSE degradation is concentrated in high-$\pi$ subgroups ($s_4$--$s_7$, $\pi \geq 0.22$), where confusion matrix inversion amplifies estimation noise ($r = 0.87$, $p = 0.005$ for correlation between $\pi_s$ and HB RMSE).
404	Low-error subgroups ($s_0$--$s_1$) benefit from stratification, with HB RMSE 14--25\% below global correction.
405	HB partial pooling reduces MLE RMSE by 24--54\% in the high-$\pi$ regime ($s_4$--$s_7$), confirming that hierarchical shrinkage provides meaningful regularization even when per-subgroup labels are scarce.
406	Coverage remains $\geq$0.94 across all subgroups for HB EC-HTE, indicating that variance inflation does not compromise inference validity.
407	Adaptive shrinkage---increasing the prior strength for high-$\pi$ subgroups where CM estimation is least reliable---is a natural extension that may close the RMSE gap with global correction at larger $K$.
408	
409	We explored adaptive shrinkage ($\alpha{=}10$ for high-$\pi$ subgroups vs.\ default $\alpha{=}3$), which reduces aggregate RMSE from 0.340 to 0.216 (35\% improvement) by attenuating estimation noise in high-$\pi$ subgroups.
410	However, RMSE remains 30\% above global correction (0.166), confirming that the bottleneck is per-subgroup sample size (${\sim}$31 expert labels) rather than the shrinkage method itself.
411	This establishes $K{=}8$ at $n_{\text{expert}}{=}250$ as a boundary condition: all correction methods provide valid inference (coverage $\geq$94\%), but per-subgroup stratification requires proportionally larger expert budgets---approximately $n_{\text{expert}} \geq 500$ (${\approx}60$ labels/subgroup)---to achieve RMSE parity with global correction.
412	
413	\section{Asymmetric Misclassification Extension}
414	\label{app:asymmetric}
415	
416	Assumption~(A2) imposes symmetric misclassification ($\text{FPR}_s = \text{FNR}_s = \pi_s$), which simplifies the bias decomposition but is not necessary for it.
417	Real LLM annotators typically exhibit asymmetric confusion patterns; we show here that the product structure generalizes.
418	
419	\paragraph{General bias formula.}
420	For asymmetric confusion matrices $C_s = \bigl(\begin{smallmatrix} 1{-}\text{FPR}_s & \text{FPR}_s \\ \text{FNR}_s & 1{-}\text{FNR}_s \end{smallmatrix}\bigr)$, define the mixing matrix $M_s$ via Bayesian inversion and the residual matrix $B_s = M_{\text{global}}^{-1} M_s - I$.
421	Since both $M_s$ and $M_{\text{global}}$ are row-stochastic, $B_s \mathbf{1} = \mathbf{0}$.
422	Decomposing $\boldsymbol{\tau} = \tau(0)\mathbf{1} + \Delta\tau \, \mathbf{e}_1$ gives:
423	\begin{equation}
424	\text{bias}(z, s) = \Delta\tau \cdot [B_s]_{z,1},
425	\end{equation}
426	where $[B_s]_{z,1}$ depends only on $\{\text{FPR}_k, \text{FNR}_k, w_k\}$, not on $\Delta\tau$.
427	Under~(A2), this reduces to $\delta_s \Delta\tau / (1 - 2\bar{\pi})$ (Theorem~\ref{thm:bias_identity}).
428	
429	\paragraph{Empirical validation.}
430	We test three asymmetric configurations ($K{=}2$, $n_{\text{expert}}{=}250$, 100 MC runs each): \emph{Cross} (FPR/FNR = 0.10/0.20 vs.\ 0.25/0.10), \emph{Co-directional} (0.05/0.15 vs.\ 0.20/0.30), and \emph{Extreme} (0.03/0.25 vs.\ 0.30/0.05).
431	Regressing analytic predictions on MC bias yields $R^2 = 0.991$ across all configurations, confirming the product structure under asymmetry.
432	Table~\ref{tab:asymmetric} reports correction performance averaged over subgroups, $z$-levels, and $\Delta\tau \in \{0.1, \ldots, 0.5\}$.
433	EC-HTE reduces $|\text{bias}|$ from 0.025 (global) to 0.006, a $4\times$ improvement, with lower RMSE (0.033 vs.\ 0.040) and substantially better coverage (0.90 vs.\ 0.78).
434	
435	\begin{table}[t]
436	\centering
437	\caption{Asymmetric misclassification results ($K{=}2$, $n_{\text{expert}}{=}250$, 100 MC runs). Values averaged over subgroups, $z$-levels, and $\Delta\tau$.}
438	\label{tab:asymmetric}
439	\small
440	\begin{tabular}{l ccc}
441	\toprule
442	Method & $|\text{Bias}| \downarrow$ & RMSE $\downarrow$ & Coverage $\uparrow$ \\
443	\midrule
444	Naive & 0.047 & 0.053 & 0.48 \\
445	Global & 0.025 & 0.040 & 0.78 \\
446	HB EC-HTE & \textbf{0.006} & \textbf{0.033} & \textbf{0.90} \\
447	\bottomrule
448	\end{tabular}
449	\end{table}
450	
451	\section{Supplementary Main Results}
452	\label{app:main_supp}
453	
454	\begin{table}[t]
455	\centering
456	\caption{Additional configurations from the main experiment. $|\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and 100 MC runs. $^\dagger$RMSE exceeds Global.}
457	\label{tab:main_supp}
458	\small
459	\begin{tabular}{ll ccc}
460	\toprule
461	Configuration & Method & $|\text{Bias}|$ & RMSE & Cov. \\
462	\midrule
463	\multirow{4}{*}{\shortstack[l]{Synthetic DIM\\$K{=}2$, moderate, $n{=}250$}}
464	 & Naive & 0.018 & 0.064 & 0.95 \\
465	 & Global & 0.009 & 0.074 & 0.96 \\
466	 & Strat.\ MLE & \textbf{0.005} & 0.075$^\dagger$ & 0.97 \\
467	 & HB EC-HTE & \textbf{0.005} & 0.075$^\dagger$ & 0.97 \\
468	\midrule
469	\multirow{4}{*}{\shortstack[l]{Semi-synthetic\\TweetEval, extreme, $n{=}250$}}
470	 & Naive & 0.027 & 0.103 & 0.93 \\
471	 & Global & \textbf{0.023} & 0.124 & 0.92 \\
472	 & Strat.\ MLE & 0.032 & 0.248$^\dagger$ & 0.91 \\
473	 & HB EC-HTE & 0.027 & 0.225$^\dagger$ & 0.91 \\
474	\bottomrule
475	\end{tabular}
476	\end{table}
477	
478	\section{PPCI Complementarity Results}
479	\label{app:ppci}
480	\label{sec:ppci}
481	
482	EC-HTE composes with PPCI~\cite{sui2026ppci} for settings where both covariate misclassification and outcome model error are present: EC-HTE+PPCI reduces $|\text{bias}|$ from 0.179 to 0.007 ($z{=}0$, DGP~C), and the corrected pseudo-outcomes are compatible with other CATE estimators (R-learner bias reduction: 89\%; Appendix~\ref{app:rlearner}).
483	
484	\begin{table*}[t]
485	\centering
486	\caption{PPCI complementarity experiment ($K{=}2$, extreme, $n_{\text{expert}}{=}250$). DGP~A: covariate error only; B: outcome error only ($\sigma{=}0.5$); C: both errors; D: no error. Values are $|\text{bias}|$ and RMSE averaged over two subgroups. $^\star$EC-HTE+PPCI achieves near-zero bias when both error types are present.}
487	\label{tab:ppci}
488	\small
489	\begin{tabular}{ll cccc}
490	\toprule
491	DGP & Method & $|\text{Bias}|_{z=0}$ & $|\text{Bias}|_{z=1}$ & RMSE$_{z=0}$ & RMSE$_{z=1}$ \\
492	\midrule
493	\multirow{5}{*}{A: Covariate}
494	 & Naive & 0.053 & 0.063 & 0.087 & 0.093 \\
495	 & Global & 0.063 & 0.055 & 0.101 & 0.102 \\
496	 & EC-HTE & 0.017 & \textbf{0.013} & 0.097 & 0.108 \\
497	 & PPCI & \textbf{0.015} & 0.020 & 0.162 & 0.168 \\
498	 & EC-HTE+PPCI & 0.017 & \textbf{0.013} & 0.097 & 0.108 \\
499	\midrule
500	\multirow{5}{*}{B: Outcome}
501	 & Naive & 0.189 & 0.197 & 0.206 & 0.212 \\
502	 & Global & 0.185 & 0.208 & 0.204 & 0.228 \\
503	 & EC-HTE & 0.181 & 0.215 & 0.202 & 0.237 \\
504	 & PPCI & 0.015 & \textbf{0.020} & 0.171 & 0.176 \\
505	 & EC-HTE+PPCI & \textbf{0.012} & 0.023 & 0.171 & 0.186 \\
506	\midrule
507	\multirow{5}{*}{C: Both}
508	 & Naive & 0.251 & 0.135 & 0.267 & 0.155 \\
509	 & Global & 0.182 & 0.209 & 0.233 & 0.235 \\
510	 & EC-HTE & 0.179 & 0.216 & 0.224 & 0.262 \\
511	 & PPCI & 0.017 & 0.007 & 0.241 & 0.232 \\
512	 & EC-HTE+PPCI$^\star$ & \textbf{0.007} & \textbf{0.008} & 0.209 & 0.223 \\
513	\midrule
514	\multirow{5}{*}{D: None}
515	 & Naive & \textbf{0.007} & 0.003 & 0.060 & 0.065 \\
516	 & Global & 0.010 & \textbf{0.002} & 0.061 & 0.071 \\
517	 & EC-HTE & 0.013 & 0.007 & 0.062 & 0.079 \\
518	 & PPCI & \textbf{0.007} & \textbf{0.003} & 0.060 & 0.065 \\
519	 & EC-HTE+PPCI & 0.013 & 0.007 & 0.062 & 0.079 \\
520	\bottomrule
521	\end{tabular}
522	\end{table*}
523	
524	The complementarity of EC-HTE and PPCI follows from the distinct error sources they correct: EC-HTE addresses misclassification in the effect modifier $Z$ (covariate space), while PPCI corrects specification error in the outcome model $f(X)$ (prediction space).
525	Since covariate misclassification and outcome model error are algebraically independent in the potential outcomes framework, their corrections compose without interference---confirmed by the 4-DGP orthogonal design (Table~\ref{tab:ppci}), where DGP~C (both errors present) yields the largest bias reduction from the combined approach.
526	Under covariate error only, PPCI adds nothing; under no error, all methods perform equivalently.
527	
528	\section{Real-Data Case Study: Hate Speech Detection}
529	\label{app:hatespeech}
530	
531	We apply EC-HTE to the UC Berkeley Measuring Hate Speech corpus~\cite{kennedy2020constructing}, annotating 2{,}496 comments for dehumanization using GPT-4.1.
532	Four text-feature subgroups are defined by crossing platform (Reddit/Gab vs.\ Twitter/YouTube) and text length (above/below median), yielding balanced groups ($n \approx 624$ each).
533	
534	\paragraph{Positive finding: real-world heterogeneity.}
535	Per-subgroup misclassification rates range from 0.266 to 0.383, confirming heterogeneity ($\Delta\pi = 0.117$) in a real annotation setting.
536	At the error-type level, FPR ranges from 8.5\% to 21.3\% across text-feature subgroups, demonstrating that subgroup-varying misclassification is not an artifact of synthetic design but arises naturally in real NLP annotation tasks.
537	
538	\paragraph{Boundary condition: statistical power at extreme FNR.}
539	Correction results are inconclusive: all corrected confidence intervals contain zero, and point estimate differences between methods are not statistically significant.
540	The high baseline FNR (53.3\%) amplifies variance through matrix inversion (variance amplification factor up to 15.7$\times$), rendering the comparison underpowered.
541	When $P(\hat{Z}{=}1 \mid Z{=}1) \approx 0.5$, the confusion matrix approaches singularity, and inversion amplifies estimation noise regardless of stratification strategy.
542	This complements the expert budget threshold identified in Appendix~\ref{sec:budget}: EC-HTE requires \emph{both} sufficient expert labels \emph{and} sufficient baseline classifier quality.
543	
544	\paragraph{Diagnostic connection.}
545	The diagnostic criterion ($\Delta\pi \times \Delta\tau$, Section~\ref{sec:diagnostic}) identifies when correction is worthwhile under moderate baseline accuracy.
546	This case study illustrates that even when $\Delta\pi$ is large, extreme baseline error renders correction underpowered rather than beneficial.
547	A practical prerequisite is that the per-subgroup confusion matrix condition number $\kappa(\hat{C}_s)$ remain moderate; when $\kappa > 50$, as observed here, practitioners should prioritize improving annotation quality before applying any matrix-inversion-based correction.
548	
549	\section{Cross-Model Consistency}
550	\label{app:multilm}
551	
552	We evaluate whether misclassification heterogeneity is model-specific by annotating 500 TweetEval sentiment tweets with six OpenAI models spanning three generations.
553	Six text-feature subgroups are defined by crossing hashtag presence and text length.
554	Spearman rank correlations of per-subgroup error rates across all six subgroups range from $\rho = 0.82$ to $1.00$, indicating that the subgroup error structure is consistent across architectures.
555	Two subgroups with $n \leq 6$ exhibit zero misclassification across all models; excluding these yields four-point correlations that are directionally consistent but underpowered.%
556	\footnote{The filtered $\Delta\pi$ values in Table~\ref{tab:multilm} serve as a robustness check independent of rank-order testing: all six models exceed $\Delta\pi > 0.05$ on the four retained subgroups.}
557	
558	\begin{table}[t]
559	\centering
560	\caption{Effective misclassification heterogeneity ($\Delta\pi$) across six OpenAI models on TweetEval sentiment (500 tweets, filtered to 4 subgroups with $n \geq 10$).}
561	\label{tab:multilm}
562	\small
563	\begin{tabular}{lcc}
564	\toprule
565	Model & Effective $\Delta\pi$ & $> 0.05$? \\
566	\midrule
567	GPT-3.5-Turbo & 0.198 & \checkmark \\
568	GPT-4-Turbo & 0.149 & \checkmark \\
569	GPT-4o-mini & 0.136 & \checkmark \\
570	GPT-5.4 & 0.114 & \checkmark \\
571	GPT-4.1 & 0.098 & \checkmark \\
572	GPT-4o & 0.080 & \checkmark \\
573	\bottomrule
574	\end{tabular}
575	\end{table}
576	
577	All six models exhibit effective $\Delta\pi > 0.05$ on the four retained subgroups (Table~\ref{tab:multilm}), and 5 of 6 share the same worst subgroup (\texttt{True\_medium}: tweets with hashtags and medium text length).
578	Newer models reduce absolute error rates but do not eliminate subgroup heterogeneity: GPT-5.4 achieves $\Delta\pi = 0.114$ compared to GPT-3.5-Turbo's $0.198$.
579	These results were obtained with a single API provider; open-source model validation appears in Appendix~\ref{app:multilm_opensource}.
580	
581	\section{Open-Source Multi-LLM Validation}
582	\label{app:multilm_opensource}
583	
584	We evaluate four open-source LLMs (7B--9B parameter range) on 490 TweetEval sentiment tweets with $K{=}4$ subgroups defined by crossing hashtag presence and text length.
585	Table~\ref{tab:multilm_cm} reports the confusion matrix heterogeneity profile.
586	All four models exhibit $\Delta\pi > 0.05$, confirming that subgroup-heterogeneous misclassification is not specific to proprietary APIs.
587	Subgroup error rankings are consistent across architectures: \texttt{True\_short} (short tweets with hashtags) has the lowest $\pi_s$ in 3 of 4 models, while \texttt{False\_medium} (medium tweets without hashtags) has the highest.
588	
589	\begin{table}[t]
590	\centering
591	\caption{Confusion matrix heterogeneity across four open-source LLMs ($K{=}4$, $N{=}490$ TweetEval tweets). $\Delta\pi$: max--min per-subgroup misclassification rate. Prop2: number of subgroups where the $\Delta\tau$-free diagnostic (Proposition~\ref{prop:debiasing_hurts}) triggers.}
592	\label{tab:multilm_cm}
593	\small
594	\begin{tabular}{lcccl}
595	\toprule
596	Model & Acc.\ & $\Delta\pi$ & Prop2 & Strongest \\
597	\midrule
598	Llama-3.1-8B & 0.755 & 0.141 & 1/4 & True\_short \\
599	Qwen-2.5-7B & 0.798 & 0.165 & 1/4 & True\_short \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84d8a185-da4a-435d-bc0d-829c32e3d5cb",
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "9b784934-bc11-4d1d-ba04-e0094a5294d9",
  "sourceToolAssistantUUID": "84d8a185-da4a-435d-bc0d-829c32e3d5cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T19:22:50.169Z_

<details open><summary>🔧 Tool call — Read · `toolu_0181TCWMsoq1GBKgHL1udzq3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 600,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b784934-bc11-4d1d-ba04-e0094a5294d9",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3auxt4R4CxndA8d6sY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce7cd414-ab27-4ee7-8115-2cf982691af9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMqgjNc5AetPK7fekV9FKk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5588,
      "cache_read_input_tokens": 39009,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5588
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 39009,
          "cache_creation_input_tokens": 5588,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5588,
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

_source line 32 · 2026-05-23T19:22:50.198Z_

<details><summary>↩ Tool result · `toolu_0181TCWMsoq1GBKgHL1udzq3`</summary>

```text
600	Gemma-2-9B & 0.763 & 0.125 & 4/4 & True\_medium \\
601	Mistral-7B & 0.802 & 0.134 & 0/4 & --- \\
602	\bottomrule
603	\end{tabular}
604	\end{table}
605	
606	\paragraph{Semi-synthetic budget sweep.}
607	We run the full EC-HTE pipeline with $K{=}2$ subgroups and $\Delta\tau{=}0.3$, using each model's empirical confusion matrices.
608	Table~\ref{tab:multilm_budget} reports coverage and RMSE crossover points.
609	EC-HTE restores near-nominal coverage from 0.714 (naive average) to 0.939 ($+$22.5 percentage points) at $n_{\text{expert}}{=}1{,}000$, consistent across all four models.
610	Global correction achieves comparable or lower RMSE than HB at all budgets under these moderate $\Delta\pi$ values, and the $K{=}4$ RMSE crossover never occurs---confirming the budget guidelines in Appendix~\ref{sec:budget}.
611	
612	\begin{table}[t]
613	\centering
614	\caption{Semi-synthetic budget sweep ($K{=}2$, $\Delta\tau{=}0.3$, 50 MC runs; see Appendix~\ref{app:mcse} for MC tier justification). Coverage at selected expert budgets; RMSE crossover denotes the minimum expert budget at which HB EC-HTE achieves lower RMSE than the naive (uncorrected) estimator.}
615	\label{tab:multilm_budget}
616	\small
617	\begin{tabular}{lcccc}
618	\toprule
619	Model & $\Delta\pi_{K{=}2}$ & Naive Cov.\ & HB Cov.\ ($n{=}1000$) & Crossover \\
620	\midrule
621	Llama-3.1-8B & 0.051 & 0.675 & 0.940 & $n{=}1000$ \\
622	Qwen-2.5-7B & 0.080 & 0.715 & 0.925 & $n{=}1000$ \\
623	Gemma-2-9B & 0.100 & 0.705 & 0.945 & $n{=}1000$ \\
624	Mistral-7B & 0.070 & 0.760 & 0.945 & $n{=}1000$ \\
625	\midrule
626	\textit{Average} & --- & \textit{0.714} & \textit{0.939} & --- \\
627	\bottomrule
628	\end{tabular}
629	\end{table}
630	
631	\paragraph{Gemma boundary case.}
632	Gemma-2-9B triggers the Proposition~\ref{prop:debiasing_hurts} diagnostic in all four $K{=}4$ subgroups due to extreme FPR--FNR asymmetry (\texttt{False\_medium} FNR $= 0.437$).
633	At small budgets ($K{=}4$, $n{=}100$), EC-HTE RMSE reaches 1.229 ($3.1\times$ naive), illustrating the budget guideline from Appendix~\ref{sec:budget}: when per-subgroup cell counts fall below 25, the variance cost of stratified correction dominates.
634	At $n \geq 500$, EC-HTE coverage recovers to $>$0.90, consistent with the synthetic experiments.
635	
636	\paragraph{Heterogeneous-$\tau$ DGP.}
637	To assess whether the constant-$\tau$ DGP understates EC-HTE's advantage, we run a supplementary experiment using Llama's empirical confusion matrices with heterogeneous treatment effects across subgroups ($\Delta\tau \in [0.1, 0.6]$, $K{=}2$, 50 MC runs).
638	EC-HTE achieves lower $|\text{bias}|$ than global correction at all budgets ($n{=}500$: 0.010 vs.\ 0.031, a 68\% reduction).
639	In the high-$\Delta\tau$ subgroup (\texttt{True\_short}, $\Delta\tau{=}0.6$), EC-HTE also achieves lower RMSE ($n{=}1{,}000$: 0.212 vs.\ 0.258, 18\% improvement), confirming that the RMSE advantage concentrates in subgroups where correction is most needed.
640	Aggregate RMSE remains comparable to global correction because low-$\Delta\tau$ subgroups incur stratification variance without commensurate bias reduction, consistent with the budget guidelines in Appendix~\ref{sec:budget}.
641	
642	\section{Robustness to Subgroup Misspecification}
643	\label{app:robustness}
644	
645	EC-HTE requires pre-defined subgroup labels, which may be noisy in practice.
646	We test robustness by randomly flipping each observation's subgroup assignment with probability $p_{\text{flip}} \in \{0, 0.10, 0.25, 0.50\}$, across $K \in \{2, 4\}$ (extreme regime, $n_{\text{expert}} = 500$, $\Delta\tau = 0.3$, 100 MC runs).
647	
648	\begin{table}[t]
649	\centering
650	\caption{95\% CI coverage under subgroup misspecification noise. EC-HTE maintains near-nominal coverage across all noise levels.}
651	\label{tab:robustness}
652	\small
653	\begin{tabular}{lcccc}
654	\toprule
655	& \multicolumn{4}{c}{$p_{\text{flip}}$} \\
656	\cmidrule(lr){2-5}
657	Method & 0.00 & 0.10 & 0.25 & 0.50 \\
658	\midrule
659	\multicolumn{5}{l}{\textit{$K{=}2$, extreme}} \\
660	\quad Naive & 0.875 & 0.877 & 0.890 & 0.897 \\
661	\quad Global & 0.925 & 0.935 & 0.932 & 0.945 \\
662	\quad HB EC-HTE & 0.958 & 0.948 & 0.950 & 0.945 \\
663	\midrule
664	\multicolumn{5}{l}{\textit{$K{=}4$, extreme}} \\
665	\quad Naive & 0.904 & 0.916 & 0.909 & 0.919 \\
666	\quad Global & 0.930 & 0.953 & 0.948 & 0.944 \\
667	\quad HB EC-HTE & 0.956 & 0.958 & 0.960 & 0.946 \\
668	\bottomrule
669	\end{tabular}
670	\end{table}
671	
672	EC-HTE maintains coverage $\geq 0.945$ across all configurations (Table~\ref{tab:robustness}), while the naive estimator is systematically below nominal (0.875--0.919).
673	At $p_{\text{flip}} = 0.50$, subgroup structure is effectively destroyed; EC-HTE converges to global correction (coverage and RMSE within 0.1\%), confirming that hierarchical Bayesian shrinkage provides a built-in safety mechanism.
674	For $K{=}4$ at $p_{\text{flip}} = 0.50$, a small residual RMSE gap persists ($p < 0.01$), reflecting the variance cost of estimating four confusion matrices even when they carry no signal.
675	
676	\section{Monte Carlo Standard Errors}
677	\label{app:mcse}
678	
679	All main-text and most appendix experiments use 100 independent Monte Carlo replications per configuration; computationally intensive analyses (R-learner, multiplicative DGP, budget sweeps) use 50, and bootstrap experiments use 20 due to the $B{\times}$CF cost per seed.
680	The median RMSE variation between 50-seed and 100-seed estimates is below 3.2\%, confirming that 50-run results are stable.
681	We report Monte Carlo standard errors to assess whether observed differences between methods are statistically reliable.
682	For exp-001 (synthetic DGP, no per-seed pairing across methods), we use conservative two-sample $z$-tests on the 100-run means.
683	For exp-003 (semi-synthetic TweetEval, shared seeds across methods), we use paired $t$-tests, which are more powerful because they control for seed-level variation.
684	
685	Table~\ref{tab:mcse} reports paired comparisons for representative configurations.
686	Of 1{,}020 total pairwise comparisons across all configurations, 742 (72.7\%) are statistically significant at $\alpha = 0.05$.
687	
688	\begin{table}[t]
689	\centering
690	\caption{Paired comparisons for representative configurations. $\Delta$ = method A $-$ method B (negative favors A for $|\text{bias}|$). Two-sample $z$-tests for synthetic (exp-001); paired $t$-tests for semi-synthetic (exp-003). Bold $p$-values indicate significance at $\alpha = 0.05$.}
691	\label{tab:mcse}
692	\small
693	\begin{tabular}{llrr}
694	\toprule
695	Configuration & Comparison & $\Delta$ & $p$ \\
696	\midrule
697	\multicolumn{4}{l}{\textit{HB EC-HTE vs.\ Global ($|\text{bias}|$)}} \\
698	\quad $K{=}2$/ext/$n{=}500$ & & $-0.046$ & $\mathbf{<0.001}$ \\
699	\quad $K{=}4$/ext/$n{=}500$ & & $-0.078$ & $\mathbf{<0.001}$ \\
700	\quad $K{=}4$/mod/$n{=}250$ & & $-0.017$ & $0.288$ \\
701	\quad TweetEval/ext/$n{=}250$ & & $+0.001$ & $0.395$ \\
702	\midrule
703	\multicolumn{4}{l}{\textit{HB EC-HTE vs.\ Global (RMSE)}} \\
704	\quad $K{=}2$/ext/$n{=}500$ & & $+0.015$ & $0.179$ \\
705	\quad $K{=}4$/ext/$n{=}500$ & & $+0.048$ & $\mathbf{0.011}$ \\
706	\midrule
707	\multicolumn{4}{l}{\textit{HB EC-HTE vs.\ Naive ($|\text{bias}|$)}} \\
708	\quad $K{=}2$/ext/$n{=}500$ & & $-0.089$ & $\mathbf{<0.001}$ \\
709	\quad $K{=}4$/ext/$n{=}500$ & & $-0.113$ & $\mathbf{<0.001}$ \\
710	\quad $K{=}4$/mod/$n{=}250$ & & $-0.031$ & $\mathbf{0.038}$ \\
711	\quad TweetEval/ext/$n{=}250$ & & $+0.005$ & $\mathbf{0.030}$ \\
712	\bottomrule
713	\end{tabular}
714	\end{table}
715	
716	Under extreme heterogeneity, HB EC-HTE's bias advantage over global correction is highly significant ($p < 0.001$ for both $K{=}2$ and $K{=}4$).
717	The RMSE penalty of stratification is not significant at $K{=}2$ ($p = 0.179$) but reaches significance at $K{=}4$ ($p = 0.011$), consistent with the higher variance cost of estimating four confusion matrices.
718	Under moderate heterogeneity ($K{=}4$, $n{=}250$), the bias difference between HB and global is not significant ($p = 0.288$), confirming that EC-HTE's advantage requires sufficient error heterogeneity.
719	In the semi-synthetic TweetEval experiment, HB EC-HTE does not significantly improve over global ($p = 0.395$), consistent with moderate $\Delta\pi$ and unbalanced subgroup sizes.
720	The HB vs.\ naive comparison in TweetEval is significant ($p = 0.030$) but favors naive, reflecting the variance cost of stratification when bias reduction is marginal.
721	
722	\section{Semi-Real Confusion Matrix Validation}
723	\label{app:semireal}
724	
725	We test EC-HTE with empirical asymmetric confusion matrices from the GPT-4.1 TweetEval pilot.
726	Four text-feature subgroups ($K{=}4$) retain the real per-subgroup FPR and FNR from pilot annotations (Table~\ref{tab:semireal_cm}); CATE heterogeneity is injected synthetically ($\tau(z{=}0,s) = 0.3 + 0.1s$, $\tau(z{=}1,s) = 0.8 - 0.15s$).
727	$N{=}5{,}000$, $P(Z{=}1){=}0.18$, 100 MC seeds per $n_{\text{expert}}$ level.
728	
729	\begin{table}[t]
730	\centering
731	\caption{Empirical confusion matrices from GPT-4.1 TweetEval pilot.
732	S0 exhibits FNR $= 0.526$, approaching chance-level classification.}
733	\label{tab:semireal_cm}
734	\small
735	\begin{tabular}{lcccc}
736	\toprule
737	Subgroup & Weight & FPR & FNR & $\kappa(\hat{C}_s)$ \\
738	\midrule
739	S0 & 0.38 & 0.054 & 0.526 & high \\
740	S1 & 0.22 & 0.101 & 0.300 & moderate \\
741	S2 & 0.14 & 0.143 & 0.308 & moderate \\
742	S3 & 0.25 & 0.194 & 0.222 & low \\
743	\bottomrule
744	\end{tabular}
745	\end{table}
746	
747	\begin{table}[t]
748	\centering
749	\caption{Semi-real confusion matrix results. RMSE and coverage averaged over subgroups and $z$-levels (100 MC runs). HB EC-HTE underperforms global at all budgets; S0's near-chance FNR drives the failure.}
750	\label{tab:semireal}
751	\small
752	\begin{tabular}{llcc}
753	\toprule
754	$n_{\text{expert}}$ & Method & RMSE $\downarrow$ & Coverage $\uparrow$ \\
755	\midrule
756	\multirow{4}{*}{100}
757	 & Oracle & 0.101 & 0.957 \\
758	 & Naive & 0.123 & 0.879 \\
759	 & Global & 0.263 & 0.885 \\
760	 & HB EC-HTE & 0.784 & 0.744 \\
761	\midrule
762	\multirow{4}{*}{250}
763	 & Oracle & 0.101 & 0.957 \\
764	 & Naive & 0.123 & 0.879 \\
765	 & Global & 0.232 & 0.909 \\
766	 & HB EC-HTE & 0.411 & 0.834 \\
767	\midrule
768	\multirow{4}{*}{500}
769	 & Oracle & 0.101 & 0.957 \\
770	 & Naive & 0.123 & 0.879 \\
771	 & Global & 0.196 & 0.922 \\
772	 & HB EC-HTE & 0.260 & 0.890 \\
773	\bottomrule
774	\end{tabular}
775	\end{table}
776	
777	HB EC-HTE produces higher RMSE and lower coverage than global correction at all expert budgets (Table~\ref{tab:semireal}).
778	The root cause is S0's FNR $= 0.526$: when a confusion matrix row approaches a uniform distribution ($P(\hat{Z}{=}1 \mid Z{=}1) \approx 0.5$), inversion amplifies estimation noise regardless of the expert budget.
779	This converges with the hate speech case study (Appendix~\ref{app:hatespeech}, FNR $= 53.3$\%) and confirms that EC-HTE requires \emph{both} sufficient expert labels \emph{and} sufficient baseline classifier quality per subgroup.
780	The singularity guard ($\kappa > 100$, Section~\ref{sec:method}) mitigates catastrophic failure by falling back to global correction for near-degenerate subgroups, but does not recover the bias reduction that motivates stratification.
781	For a $2 \times 2$ symmetric confusion matrix, $\kappa = 1/|1-2\pi|$; $\kappa > 100$ corresponds to $\pi \in (0.495, 0.505)$, so the guard triggers only when the classifier performs within $0.5\%$ of random guessing.
782	At $n_{\text{expert}} = 500$, HB EC-HTE narrows the gap (RMSE 0.260 vs.\ 0.196) as confusion matrix estimates stabilize for the three well-classified subgroups, but the S0 bottleneck persists.
783	
784	A second semi-real experiment using GPT-3.5-Turbo confusion matrices (worst-subgroup FPR $= 0.39$, FNR $= 0.21$) yields similar results: HB RMSE exceeds global by 1.3--3.5$\times$ at all budgets.
785	Here the failure stems from high false-positive rates compounded by class imbalance ($P(Z{=}1) = 0.18$), which leaves insufficient expert observations in the positive class for reliable per-subgroup confusion matrix estimation.
786	Together, these experiments identify three applicability conditions for EC-HTE: (1)~sufficient effective expert budget ($n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$), (2)~no near-chance subgroup error rate ($\max(\text{FPR}_s, \text{FNR}_s) < 0.5$), and (3)~adequate class balance in the effect modifier.
787	
788	\paragraph{Diagnostic rule.}
789	A logistic regression over all 368 semi-real experiment--budget cells (dependent variable: HB EC-HTE $<$ Global RMSE) identifies two sufficient statistics: the worst-subgroup confusion matrix condition number $\kappa(\hat{M}_s) \leq 1.25$ and the effective minority-class expert count $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$.
790	When both conditions hold, HB outperforms global in 93.3\% of cells; when either is violated, global is preferred in 94.7\% of cells.
791	Both exp-015 ($\kappa = 2.38$, effective $n = 2.5$) and exp-016 ($\kappa = 1.55$, effective $n = 2.5$) violate both conditions, and the diagnostic correctly predicts 100\% of their failure cells.
792	Subgroup-average metrics can mask cell-level heterogeneity: in exp-015, HB EC-HTE substantially reduces bias for the three well-classified subgroups (S1--S3) but amplifies variance in the near-degenerate subgroup (S0, FNR $= 0.526$), and the S0 penalty dominates the aggregate RMSE.
793	
794	\begin{figure}[t]
795	\centering
796	\includegraphics[width=\columnwidth]{figures/applicability_frontier.pdf}
797	\caption{Applicability frontier of EC-HTE. Green region: EC-HTE reduces bias vs.\ global correction. Yellow: comparable performance. Red: EC-HTE underperforms. Dashed lines mark the expert budget threshold ($n_{\text{expert}}/K = 25$) and classifier quality threshold (worst-subgroup error rate $= 0.5$). Red diamonds show semi-real experiments with actual GPT-4.1 and GPT-3.5-Turbo confusion matrices.}
798	\label{fig:applicability}
799	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce7cd414-ab27-4ee7-8115-2cf982691af9",
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "71771dac-cf3e-416b-bd5d-5b44c0ebf622",
  "sourceToolAssistantUUID": "ce7cd414-ab27-4ee7-8115-2cf982691af9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T19:22:53.946Z_

<details open><summary>🔧 Tool call — Read · `toolu_013xNzH3HcAbCqPMKVjyYGoT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 800,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71771dac-cf3e-416b-bd5d-5b44c0ebf622",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3bFRueLhKt57SKXh6H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58cef109-49c8-404b-91f0-2e0bb29b117b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkJt8pwaWsTqiaNsdMmE1r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5680,
      "cache_read_input_tokens": 44597,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5680
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 44597,
          "cache_creation_input_tokens": 5680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5680,
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

_source line 34 · 2026-05-23T19:22:53.954Z_

<details><summary>↩ Tool result · `toolu_013xNzH3HcAbCqPMKVjyYGoT`</summary>

```text
800	
801	\section{Robustness: Estimator Choice and Treatment Effect Specification}
802	\label{app:rlearner}
803	
804	We verify that EC-HTE's corrected pseudo-outcomes are compatible with downstream estimators beyond CausalForest by replacing it with the R-learner~\citep{nie2021quasi}.
805	The experiment uses $K{=}2$, extreme heterogeneity, $n_{\text{expert}} = 500$, and 50 MC seeds; the R-learner uses 5-fold cross-fitting with gradient-boosted trees as the base learner.
806	
807	\begin{table}[t]
808	\centering
809	\caption{R-learner vs.\ CausalForest with EC-HTE correction ($K{=}2$, extreme, $n{=}500$). $|\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and seeds.}
810	\label{tab:rlearner}
811	\small
812	\begin{tabular}{llccc}
813	\toprule
814	Estimator & Correction & $|\text{Bias}|$ & RMSE & Cov. \\
815	\midrule
816	\multirow{4}{*}{R-learner}
817	 & Oracle & 0.006 & 0.056 & 0.94 \\
818	 & Naive & 0.121 & 0.139 & 0.47 \\
819	 & Global & 0.098 & 0.123 & 0.72 \\
820	 & EC-HTE & \textbf{0.013} & 0.080 & 0.92 \\
821	\midrule
822	\multirow{2}{*}{CausalForest}
823	 & Naive & 0.058 & 0.090 & 0.82 \\
824	 & EC-HTE & \textbf{0.010} & 0.093 & 0.95 \\
825	\bottomrule
826	\end{tabular}
827	\end{table}
828	
829	EC-HTE reduces R-learner $|\text{bias}|$ by 89\% (0.121 $\to$ 0.013) and restores coverage from 0.47 to 0.92 (Table~\ref{tab:rlearner}).
830	The bias reduction and coverage gains are comparable to those achieved with CausalForest, confirming that EC-HTE is compatible with a range of HTE estimators.
831	
832	\paragraph{Multiplicative treatment effects.}
833	We further test robustness to the functional form of treatment effects by replacing the additive DGP with a multiplicative specification: $Y(1) = Y(0) \times \exp(\tau(Z))$, using $K{=}2$, extreme heterogeneity, $n_{\text{expert}} = 500$, and 50 MC seeds.
834	
835	\begin{table}[t]
836	\centering
837	\caption{Multiplicative DGP results ($K{=}2$, extreme, $n{=}500$, 50 seeds). EC-HTE achieves comparable bias reduction and nominal coverage under non-additive treatment effects.}
838	\label{tab:multiplicative}
839	\small
840	\begin{tabular}{lccc}
841	\toprule
842	Method & $|\text{Bias}|$ & RMSE & Cov. \\
843	\midrule
844	Oracle & 0.003 & 0.038 & 0.96 \\
845	Naive & 0.135 & 0.142 & 0.44 \\
846	Global & 0.110 & 0.124 & 0.54 \\
847	EC-HTE & \textbf{0.054} & 0.068 & 0.955 \\
848	\bottomrule
849	\end{tabular}
850	\end{table}
851	
852	EC-HTE reduces RMSE by 52\% relative to naive (0.068 vs.\ 0.142) and restores coverage to the nominal level (0.955; Table~\ref{tab:multiplicative}).
853	EC-HTE's bias correction operates at the confusion matrix level, independent of the downstream CATE estimator and functional form of treatment effects.
854	
855	\section{Robustness to Class Imbalance}
856	\label{app:classimbalance}
857	
858	Assumption (A3) requires $P(Z{=}1) = 0.5$, but real-world effect modifiers are often imbalanced.
859	We sweep $P(Z{=}1) \in \{0.1, 0.2, 0.3, 0.4, 0.5\}$ with $K \in \{2,4\}$, extreme misclassification heterogeneity, $n_{\text{expert}}{=}250$, and 100 MC seeds (Table~\ref{tab:pz1_sweep}).
860	
861	\begin{table}[t]
862	\centering
863	\caption{Robustness to class imbalance ($n_{\text{expert}}{=}250$, extreme heterogeneity). R$^2$: Theorem~\ref{thm:bias_identity} fit. Ratio: HB/Global RMSE ($<1$ = HB wins). Cov.: HB EC-HTE 95\% CI coverage.}
864	\label{tab:pz1_sweep}
865	\small
866	\begin{tabular}{cc ccc}
867	\toprule
868	$P(Z{=}1)$ & $K$ & R$^2$ & Ratio & Cov. \\
869	\midrule
870	0.1 & 2 & 0.998 & 0.92 & 0.94 \\
871	0.2 & 2 & 0.989 & 0.76 & 0.94 \\
872	0.3 & 2 & 0.994 & 0.78 & 0.94 \\
873	0.4 & 2 & 0.995 & 0.87 & 0.94 \\
874	0.5 & 2 & 0.995 & 0.86 & 0.93 \\
875	\midrule
876	0.1 & 4 & 0.984 & 1.54 & 0.92 \\
877	0.2 & 4 & 0.976 & 1.68 & 0.93 \\
878	0.3 & 4 & 0.985 & 1.12 & 0.92 \\
879	0.4 & 4 & 0.984 & 1.08 & 0.93 \\
880	0.5 & 4 & 0.992 & 1.06 & 0.92 \\
881	\bottomrule
882	\end{tabular}
883	\end{table}
884	
885	Theorem~\ref{thm:bias_identity}'s product form remains accurate across all imbalance levels: $R^2 \geq 0.976$ even at $P(Z{=}1) = 0.1$, confirming that the bias identity derives from confusion matrix structure rather than class balance.
886	For $K{=}2$, EC-HTE outperforms global correction at all $P(Z{=}1)$ levels (RMSE ratio 0.76--0.92), degrading gracefully under severe imbalance.
887	For $K{=}4$, EC-HTE underperforms global at $n_{\text{expert}}{=}250$ (ratio 1.06--1.68), consistent with the budget threshold $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$: at $P(Z{=}1){=}0.1$, $K{=}4$, each subgroup receives only ${\sim}6$ minority-class labels.
888	The gap narrows as $P(Z{=}1)$ increases (1.54 $\to$ 1.06), and coverage remains stable at 0.92--0.94 across all configurations.
889	
890	\section{Comparison with PPI Correction}
891	\label{app:ppi_comparison}
892	
893	PPI~\cite{angelopoulos2023ppi} constructs confidence intervals by combining a large set of ML predictions with a smaller set of gold-standard labels, using the gold labels to debias the ML-based estimator.
894	Applied to our setting, PPI treats the LLM-annotated effect modifier as the ML prediction and the expert labels as the gold standard.
895	Two variants arise naturally: \emph{PPI-global} pools all expert labels to estimate a single rectifier (analogous to our Global baseline), and \emph{PPI-subgroup} estimates per-subgroup rectifiers (analogous to Stratified MLE).
896	
897	Under the confusion-matrix parameterization we adopt, DSL's measurement error correction reduces to confusion matrix inversion.
898	Pooled DSL applies a single estimated confusion matrix to all subgroups, producing the same corrected label distribution as our Global baseline; per-subgroup DSL estimates a separate confusion matrix for each subgroup and inverts it independently, equivalent to our Stratified MLE.
899	EC-HTE's contribution over both PPI-subgroup and per-subgroup DSL is hierarchical partial pooling: rather than estimating each subgroup's confusion matrix in isolation, EC-HTE places a shared prior across subgroups, borrowing strength to reduce variance while preserving subgroup-specific bias correction.
900	This mechanism is outside both the PPI and DSL frameworks.
901	
902	The key difference between PPI and confusion-matrix inversion is that PPI does not invert the confusion matrix; instead, it uses the gold labels to directly debias the estimand.
903	This avoids the matrix inversion step that can amplify noise at small $n_{\text{expert}}$, but it also means PPI cannot exploit the structure of the misclassification process to reduce bias.
904	PPI-global inherits the same $\Delta\pi \times \Delta\tau$ bias amplification as Global correction (Theorem~\ref{thm:bias_identity}), confirming that the ``debiasing hurts'' mechanism operates regardless of the inference framework.
905	
906	\section{Civil Comments Validation}
907	\label{app:civilcomments}
908	
909	To verify that subgroup-heterogeneous misclassification generalizes beyond TweetEval, we annotate $N{=}3{,}000$ stratified samples (30\% toxic) from Civil Comments~\cite{borkan2019nuanced}, a toxicity detection dataset.
910	Subgroups are defined by \texttt{text\_length\_bin} $\times$ \texttt{has\_question} ($K{=}4$): S0 (long, no question, 38.8\%), S1 (long, question, 11.4\%), S2 (short, no question, 33.7\%), S3 (short, question, 16.1\%).
911	Subgroup features were chosen a priori based on observable text properties; no feature search was performed.
912	Three proprietary LLMs annotate each sample via an OpenAI-compatible API, yielding 800--900 valid annotations per model.
913	
914	Table~\ref{tab:civil_cm} reports per-subgroup FPR and FNR.
915	We define $\Delta\pi = \max_s \pi_s - \min_s \pi_s$, where $\pi_s$ is the overall misclassification rate for subgroup $s$.
916	All three models exhibit $\Delta\pi > 0.05$, with overall heterogeneity $\Delta\pi \in [0.113, 0.160]$---comparable to the $\Delta\pi \in [0.125, 0.165]$ observed across four open-source LLMs on TweetEval (Appendix~\ref{app:multilm_opensource}).
917	GPT-4o-mini and GPT-3.5-turbo show pronounced FPR/FNR asymmetry (e.g., GPT-4o-mini FPR $\in [0.42, 0.61]$ vs.\ FNR $\in [0.05, 0.16]$), indicating systematic over-prediction of toxicity; their FPR approaches 0.5, placing them in the ill-conditioned regime where confusion matrix inversion amplifies noise (consistent with the classifier quality threshold discussed in the Limitations section).
918	The consistent presence of $\Delta\pi$ heterogeneity across two NLP tasks, seven LLMs spanning open-source (7B--9B) and proprietary families, and two distinct subgroup definitions confirms that this phenomenon is a structural property of LLM annotation rather than an artifact of a specific dataset or model.
919	
920	\begin{table}[h]
921	\centering
922	\caption{Per-subgroup misclassification rates on Civil Comments ($K{=}4$). $\Delta$ denotes max $-$ min across subgroups.}
923	\label{tab:civil_cm}
924	\small
925	\begin{tabular}{llccccc}
926	\toprule
927	Model & Metric & S0 & S1 & S2 & S3 & $\Delta$ \\
928	\midrule
929	GPT-4o & FPR & 0.249 & 0.157 & 0.213 & 0.341 & 0.184 \\
930	       & FNR & 0.160 & 0.263 & 0.308 & 0.328 & 0.168 \\
931	\midrule
932	GPT-4o-mini & FPR & 0.517 & 0.541 & 0.419 & 0.610 & 0.191 \\
933	            & FNR & 0.052 & 0.105 & 0.074 & 0.160 & 0.108 \\
934	\midrule
935	GPT-3.5-turbo & FPR & 0.400 & 0.473 & 0.374 & 0.468 & 0.099 \\
936	              & FNR & 0.139 & 0.211 & 0.173 & 0.240 & 0.101 \\
937	\bottomrule
938	\end{tabular}
939	\end{table}
940	
941	\section{Bias Identity Validation with Real Confusion Matrices}
942	\label{app:realcm_bias}
943	
944	Theorem~\ref{thm:bias_identity} is derived under symmetric misclassification (A2); real LLM confusion matrices are asymmetric (FPR $\neq$ FNR).
945	We verify that the generalized identity $\mathrm{bias}(z,s) = \Delta\tau \cdot [B_s]_{z,1}$ (Remark~\ref{thm:bias_identity}) holds under real annotation error structures by running semi-synthetic simulations ($N{=}5{,}000$, $K{=}4$, $\Delta\tau{=}0.30$, 100 MC runs) with confusion matrices drawn from 11 LLM--dataset combinations: eight models on TweetEval (GPT-4-turbo, GPT-4o, GPT-4.1, GPT-4o-mini, GPT-3.5-turbo, Qwen2.5-7B, Mistral-7B, Gemma-2-9B) and three on Civil Comments (GPT-4o, GPT-4o-mini, GPT-3.5-turbo).
946	
947	Table~\ref{tab:realcm_r2} reports per-model $R^2$ from regressing observed subgroup bias on the predicted value $\Delta\tau \cdot [B_s]_{z,1}$.
948	The aggregate $R^2 = 0.975$; 10 of 11 combinations achieve $R^2 \geq 0.93$.
949	The single outlier (GPT-4o-mini on Civil Comments, $R^2{=}0.76$) has near-homogeneous subgroup error rates ($\max|[B_s]_{z,1}| = 0.089$), so predicted biases are small and Monte Carlo noise dominates the regression.
950	$R^2$ correlates strongly with $\max|[B_s]_{z,1}|$: models with more heterogeneous per-subgroup error rates produce larger bias signals that are easier to verify empirically.
951	
952	\begin{table}[h]
953	\centering
954	\caption{Bias identity $R^2$ with real LLM confusion matrices ($K{=}4$, 100 MC runs).}
955	\label{tab:realcm_r2}
956	\small
957	\begin{tabular}{llcc}
958	\toprule
959	Model & Dataset & $R^2$ & $\max|[B_s]_{z,1}|$ \\
960	\midrule
961	GPT-4-turbo  & TweetEval & 0.993 & 0.328 \\
962	Qwen2.5-7B   & TweetEval & 0.990 & 0.272 \\
963	Mistral-7B   & TweetEval & 0.990 & 0.242 \\
964	Gemma-2-9B   & TweetEval & 0.982 & 0.185 \\
965	GPT-4o       & Civil Comments & 0.979 & 0.198 \\
966	GPT-4o       & TweetEval & 0.975 & 0.240 \\
967	GPT-4.1      & TweetEval & 0.969 & 0.139 \\
968	GPT-3.5-turbo & TweetEval & 0.948 & 0.087 \\
969	GPT-3.5-turbo & Civil Comments & 0.935 & 0.170 \\
970	GPT-4o-mini  & TweetEval & 0.929 & 0.170 \\
971	GPT-4o-mini  & Civil Comments & 0.756 & 0.089 \\
972	\midrule
973	\multicolumn{2}{l}{All (pooled)} & 0.975 & --- \\
974	\bottomrule
975	\end{tabular}
976	\end{table}
977	
978	\section{Applicability Screening with Real LLM Confusion Matrices}
979	\label{app:screening}
980	
981	We apply the diagnostic conditions from Proposition~\ref{prop:debiasing_hurts} and Section~\ref{sec:method} to 16 LLM--dataset--$K$ combinations spanning seven LLMs (four open-source, three proprietary) across TweetEval and Civil Comments.
982	Table~\ref{tab:screening} summarizes which conditions each combination satisfies.
983	
984	\begin{table}[h]
985	\centering
986	\caption{Diagnostic screening of 16 LLM--dataset--$K$ combinations. Columns report whether all subgroups satisfy each condition. Budget assumes $n_{\text{expert}}{=}500$.}
987	\label{tab:screening}
988	\small
989	\begin{tabular}{llccccc}
990	\toprule
991	Model & Dataset & $K$ & $\kappa{\leq}1.25$ & $\max{\leq}0.5$ & Budget & Pass all \\
992	\midrule
993	Gemma-2-9B   & TweetEval & 2 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
994	Llama-3.1-8B & TweetEval & 2 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
995	Mistral-7B   & TweetEval & 2 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
996	Qwen2.5-7B   & TweetEval & 2 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
997	Gemma-2-9B   & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
998	Llama-3.1-8B & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
999	Mistral-7B   & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58cef109-49c8-404b-91f0-2e0bb29b117b",
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "c210485b-23ea-4f0d-81ca-9175d832b3f5",
  "sourceToolAssistantUUID": "58cef109-49c8-404b-91f0-2e0bb29b117b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T19:22:58.060Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K2RGGk4c24WzFvKYGdToHh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 1000,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c210485b-23ea-4f0d-81ca-9175d832b3f5",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3bX7yR7NNmmdqQFoCs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a25a4c0-1ece-49c5-bec6-6594ba1279b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3pbrdt73TB8VwQvGKaesg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5636,
      "cache_read_input_tokens": 50277,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5636,
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

_source line 36 · 2026-05-23T19:22:58.067Z_

<details><summary>↩ Tool result · `toolu_01K2RGGk4c24WzFvKYGdToHh`</summary>

```text
1000	Qwen2.5-7B   & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1001	GPT-3.5-turbo & CivilComm. & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1002	GPT-3.5-turbo & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1003	GPT-4-turbo  & TweetEval & 4 & {\small$\times$} & {\small$\times$} & {\small$\checkmark$} & {\small$\times$} \\
1004	GPT-4.1      & TweetEval & 4 & {\small$\times$} & {\small$\times$} & {\small$\checkmark$} & {\small$\times$} \\
1005	GPT-4o       & CivilComm. & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1006	GPT-4o       & TweetEval & 4 & {\small$\times$} & {\small$\times$} & {\small$\checkmark$} & {\small$\times$} \\
1007	GPT-4o-mini  & CivilComm. & 4 & {\small$\times$} & {\small$\times$} & {\small$\checkmark$} & {\small$\times$} \\
1008	GPT-4o-mini  & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1009	\bottomrule
1010	\end{tabular}
1011	\end{table}
1012	
1013	No combination passes all three conditions; the bottleneck is $\kappa(C_s) \leq 1.25$, which requires $\mathrm{FPR}_s + \mathrm{FNR}_s \lesssim 0.20$ for all subgroups---a threshold no current LLM achieves uniformly.
1014	The closest are Qwen2.5-7B True\_short ($\kappa{=}1.23$) and Mistral-7B True\_short ($\kappa{=}1.27$).
1015	
1016	Under a relaxed ``oracle screening'' that excludes near-degenerate subgroups ($\max(\mathrm{FPR}_s, \mathrm{FNR}_s) \geq 0.4$), we run semi-synthetic CATE estimation ($N{=}5{,}000$, $\Delta\tau{=}0.3$, 100 MC runs, $n_{\text{expert}} \in \{250, 500\}$) with each LLM's real per-subgroup confusion matrix.
1017	EC-HTE (HB) achieves lower RMSE than global correction in 41 of 52 comparisons (79\%) and lower RMSE than stratified MLE in 52 of 52 comparisons (100\%).
1018	The four open-source LLMs on TweetEval show the strongest EC-HTE advantage (32/32 comparisons, RMSE reduction 0.001--0.008), while GPT-3.5-turbo/TweetEval (high FPR asymmetry, $\mathrm{FPR}_{\max}{=}0.39$) and GPT-4o/Civil Comments (low minority prevalence $P(Z{=}1){=}0.3$) show degradation.
1019	The diagnostic correctly identifies the strict applicability regime; under relaxed conditions excluding near-degenerate subgroups, EC-HTE improves RMSE in 79\% of comparisons.
1020	
1021	\paragraph{Diagnostic Applicability Analysis.}
1022	The diagnostic (Proposition~\ref{prop:debiasing_hurts}) degrades on real LLM confusion matrices (pooled AUC $= 0.63$) because the failure mode is systematic: subgroups where the true CATE heterogeneity $\tau_s \approx 0$ are hurt by global correction (since $\delta_s \neq 0$ still introduces bias), yet these subgroups produce low diagnostic scores---the diagnostic ranks them as safe precisely when they are most vulnerable to overcorrection.
1023	
1024	A simple meta-criterion recovers reliability: compute $\max_s |\delta_s| / ((1 - 2\bar{\pi}) \cdot \pi_s)$ across subgroups.
1025	When $\max_s \mathrm{score}(s) > 1$, at least one subgroup is definitively harmed by global correction, and the diagnostic achieves AUC $\geq 0.75$ across all 5 model--dataset combinations satisfying this condition (AUC range: 0.75--1.0).
1026	When $\max_s \mathrm{score}(s) \leq 1$, global correction may or may not hurt depending on unobservable $\Delta\tau$; the diagnostic achieves AUC only 0.0--0.67 across the remaining 7 combinations (4 of 7 have AUC $< 0.5$, indicating anti-prediction).
1027	This threshold perfectly separates reliable from unreliable diagnostic regimes across all 16 real LLM--dataset combinations evaluated.
1028	
1029	We recommend the following practical protocol: (i) estimate per-subgroup confusion matrices from expert labels; (ii) compute $\max_s \mathrm{score}(s)$; (iii) if $> 1$, the diagnostic reliably identifies which subgroups are harmed by global correction---apply EC-HTE; (iv) if $\leq 1$, the diagnostic is unreliable and practitioners should either default to EC-HTE as a conservative choice or evaluate correction strategies using held-out expert labels.
1030	
1031	\subsection{$\kappa$ Stratification Analysis}
1032	\label{app:kappa_analysis}
1033	
1034	The condition number $\kappa(\hat{C}_s) = 1/|1 - \mathrm{FPR}_s - \mathrm{FNR}_s|$ quantifies confusion matrix invertibility and governs the bias-variance tradeoff of per-subgroup correction.
1035	The $\kappa \leq 1.25$ threshold identified in the diagnostic rule (Section~\ref{sec:budget}) is a \emph{sufficient condition} for strongest bias reduction, not a necessary condition: EC-HTE maintains calibrated inference across a substantially wider $\kappa$ range.
1036	
1037	\paragraph{Synthetic data.}
1038	Across all 520 synthetic configurations ($K{=}2$, $\pi_s \in [0.025, 0.275]$), the maximum per-config $\kappa$ falls in $[1.43, 2.22]$; none reaches $\kappa \leq 1.25$ because the pooled rate $\bar{\pi}{=}0.15$ sets a floor of $\kappa{=}1/(1{-}2 \cdot 0.15){=}1.43$.
1039	Table~\ref{tab:kappa_synth} shows a two-bin stratification at $\kappa{=}2$: EC-HTE achieves zero analytic bias in both bins, while global correction harms at least one subgroup in 100\% of $\kappa > 2$ configurations.
1040	Monte Carlo validation ($K{=}2$, $n_{\text{expert}}{=}500$) confirms EC-HTE dominance at $\kappa{=}2.0$: 86\% bias reduction, 10\% lower RMSE, and 95.5\% coverage vs.\ 88.3\% for Global.
1041	
1042	\begin{table}[h]
1043	\centering
1044	\caption{Synthetic $\kappa$ stratification ($K{=}2$, 520 configs). ``Debiasing hurts'' = global correction increases $|\text{bias}|$ for $\geq$1 subgroup.}
1045	\label{tab:kappa_synth}
1046	\small
1047	\begin{tabular}{lcccc}
1048	\toprule
1049	$\kappa$ bin & $n$ & EC-HTE bias & Debiasing hurts & Global $|\text{bias}|/|\text{bias}_{\text{naive}}|$ \\
1050	\midrule
1051	$\leq 2.0$ & 420 & 0 (exact) & 35.0\% & 0.152 \\
1052	$> 2.0$    & 100 & 0 (exact) & 100\% & 0.326 \\
1053	\bottomrule
1054	\end{tabular}
1055	\end{table}
1056	
1057	\paragraph{Real LLM confusion matrices.}
1058	All 13 real LLM--dataset combinations ($K{=}4$) have $\kappa \in [1.88, 2.99]$---none reaches $\kappa \leq 1.25$, because no current LLM achieves $\mathrm{FPR}_s + \mathrm{FNR}_s < 0.20$ uniformly across subgroups.
1059	Table~\ref{tab:kappa_real} reports performance stratified by $\kappa$ bin and expert budget.
1060	The key finding is that EC-HTE maintains calibrated coverage ($\geq$93\%) across all $\kappa$ bins at $n_{\text{expert}} \geq 250$, compared to 86--91\% for Global.
1061	At $n_{\text{expert}}{=}500$, EC-HTE also achieves competitive RMSE in the $\kappa \leq 2$ bin (ratio 1.01) and bias win rate of 75\%; at $n_{\text{expert}}{=}250$, the variance cost of per-subgroup estimation dominates, and Global achieves lower RMSE---consistent with the bias-variance tradeoff documented in the main text (Section~\ref{sec:ec_hte_eval}).
1062	
1063	\begin{table}[h]
1064	\centering
1065	\caption{Real LLM $\kappa$ stratification ($K{=}4$, MC validation). Ratios = EC-HTE / Global; values $<1$ favor EC-HTE. Coverage is EC-HTE absolute; Global coverage ranges 0.86--0.91 across bins.}
1066	\label{tab:kappa_real}
1067	\small
1068	\begin{tabular}{llcccc}
1069	\toprule
1070	$\kappa$ bin & $n_{\text{expert}}$ & Bias ratio & RMSE ratio & Bias win & Cov.\ (EC-HTE) \\
1071	\midrule
1072	\multirow{2}{*}{$\leq 2.0$ ($n{=}4$)}
1073	 & 500 & 0.99 & 1.01 & 75\% & 0.943 \\
1074	 & 250 & 1.09 & 1.13 & 0\%  & 0.932 \\
1075	\midrule
1076	\multirow{2}{*}{$> 2.0$ ($n{=}9$)}
1077	 & 500 & 1.11 & 1.22 & 22\% & 0.949 \\
1078	 & 250 & 1.26 & 1.43 & 0\%  & 0.940 \\
1079	\bottomrule
1080	\end{tabular}
1081	\end{table}
1082	
1083	The three-tier $\kappa$ structure is thus: (i)~$\kappa > 100$: near-random classification, singularity guard triggers automatic fallback to global correction; (ii)~$\kappa \leq 1.25$: strongest theoretical regime with guaranteed bias reduction and coverage; (iii)~$\kappa \in (1.25, {\sim}3]$: the practical operating range for current LLMs, where EC-HTE provides calibrated inference (coverage $\geq$93\%) and achieves RMSE gains when expert budget is sufficient ($n_{\text{expert}} \geq 500$).
1084	
1085	\section{Plug-in Standard Error Validation}
1086	\label{app:bootstrap_se}
1087	
1088	A natural concern is whether the plug-in standard error adequately captures estimation uncertainty, particularly the additional variance introduced by confusion matrix estimation.
1089	We verify this for the difference-in-means (DIM) estimator via Monte Carlo simulation ($K{=}2$, $n_{\text{expert}} \in \{50, 100, 250, 500\}$, 50 replications per budget level).
1090	At each budget, we compute the plug-in 95\% confidence interval and record empirical coverage.
1091	Across all expert budgets, the plug-in SE yields coverage $\geq 0.96$ (0.970, 0.960, 0.970, 0.970 for $n_{\text{expert}} = 50, 100, 250, 500$), confirming that the analytic variance estimate is well-calibrated for the DIM estimator.
1092	This self-calibration arises because the same noise in $\hat{M}^{-1}$ that inflates point-estimate variance also inflates the plug-in SE, producing conservative intervals that maintain nominal coverage.
1093	
1094	\paragraph{CausalForestDML.}
1095	Under $K{=}2$ extreme heterogeneity ($\pi{=}[0.05, 0.25]$, $n_{\text{expert}}{=}250$, $n_{\text{estimators}}{=}200$, 20 MC runs), EC-HTE plug-in SE achieves 93.8\% aggregate coverage---close to the 94--96\% oracle coverage (Table~\ref{tab:cf_oracle}).
1096	The high-error subgroup ($s_1$, $\pi{=}0.25$) shows slightly lower plug-in coverage (92.5\%) than the low-error subgroup ($s_0$: 95.0\%), reflecting the larger $M^{-1}$ amplification of estimation uncertainty in subgroups with higher misclassification rates.
1097	By contrast, the DIM plug-in SE achieves $\geq$95\% coverage in the same DGP, confirming that the analytic confusion matrix propagation formula is adequate for simpler estimators.
1098	
1099	\paragraph{Full bootstrap SE.}
1100	A \emph{full} bootstrap---resampling all $N$ observations and re-estimating both the confusion matrix and CausalForest per bootstrap replicate ($B{=}100$, $n_{\text{estimators}}{=}200$, 20 MC runs)---confirms that plug-in SE is already near-nominal under standard hyperparameters.
1101	Under $K{=}2$ extreme heterogeneity ($\pi{=}[0.05, 0.25]$, $n_{\text{expert}}{=}250$), plug-in SE achieves 93.8\% aggregate coverage; the full bootstrap improves this to exactly 95.0\% ($+$1.2pp).
1102	Table~\ref{tab:bootstrap_se} reports per-subgroup results.
1103	
1104	\begin{table}[h]
1105	\centering
1106	\caption{CausalForest coverage: plug-in SE vs.\ full bootstrap SE ($B{=}100$, $n_{\text{estimators}}{=}200$, 20 MC runs). Bootstrap SE is ${\sim}1.15\times$ plug-in.}
1107	\label{tab:bootstrap_se}
1108	\small
1109	\begin{tabular}{lccccc}
1110	\toprule
1111	Subgroup & Plugin Cov. & Boot.\ Cov. & Oracle Cov. & Plugin SE & Boot.\ SE \\
1112	\midrule
1113	$s_0$ ($\pi{=}0.05$) & 0.950 & 0.925 & 0.925 & 0.059 & 0.063 \\
1114	$s_1$ ($\pi{=}0.25$) & 0.925 & \textbf{0.975} & 0.875 & 0.087 & 0.103 \\
1115	\midrule
1116	Aggregate & 0.938 & \textbf{0.950} & 0.900 & 0.073 & 0.083 \\
1117	\bottomrule
1118	\end{tabular}
1119	\end{table}
1120	
1121	The high-error subgroup ($s_1$) benefits most: coverage rises from 92.5\% to 97.5\% ($+$5.0pp), because the bootstrap captures the additional variance from $M^{-1}$ amplification.
1122	Oracle coverage (90.0\%) is consistent with the 94\% reported in the oracle decomposition (Table~\ref{tab:cf_oracle}), with the difference attributable to MC sampling noise at 20 runs.
1123	The computational cost is substantial ($B \times$ CF fits per MC run), but the approach is straightforward when exact nominal coverage is required.
1124	
1125	\paragraph{Bootstrap coverage across expert budgets.}
1126	Table~\ref{tab:bootstrap_small_n} extends the analysis to $n_{\text{expert}} \in \{25, 50, 75, 100, 200\}$ using the DIM estimator with Centered EB confusion matrix estimation ($K{=}2$ extreme, $\pi{=}[0.05, 0.25]$, 20 MC runs, $B{=}100$).
1127	Bootstrap SE maintains $\geq$95\% coverage across all expert budgets, including $n_{\text{expert}}{=}25$ (${\approx}12$ labels per subgroup).
1128	Plug-in SE is already near-nominal ($\geq$91.2\%) at all budgets tested.
1129	
1130	\begin{table}[h]
1131	\centering
1132	\caption{HB EC-HTE coverage across expert budgets: plug-in vs.\ bootstrap SE (DIM, $K{=}2$ extreme, 20 MC, $B{=}100$).}
1133	\label{tab:bootstrap_small_n}
1134	\small
1135	\begin{tabular}{lcccc}
1136	\toprule
1137	$n_{\text{expert}}$ & Plugin Cov. & Boot.\ Cov. & SE Ratio & $|\text{Bias}|$ \\
1138	\midrule
1139	25 & 0.925 & \textbf{1.000} & 2.86 & 0.079 \\
1140	50 & 0.975 & 0.988 & 2.93 & 0.067 \\
1141	75 & 0.912 & \textbf{0.975} & 2.59 & 0.065 \\
1142	100 & 0.963 & 0.963 & 1.52 & 0.060 \\
1143	200 & 0.963 & 0.950 & 1.17 & 0.061 \\
1144	\bottomrule
1145	\end{tabular}
1146	\end{table}
1147	
1148	At small $n_{\text{expert}}$, bootstrap SE inflates confidence intervals by $2{-}3\times$ relative to plug-in (SE ratio column), guaranteeing nominal coverage but reducing statistical power.
1149	At $n_{\text{expert}} \geq 100$, the SE ratio converges to ${\sim}1.2{-}1.5\times$, and plug-in SE alone achieves $\geq$96\% coverage.
1150	For practical deployment, we recommend $n_{\text{expert}} \geq 50$: bootstrap maintains nominal coverage (98.8\%) with moderate SE inflation (2.9$\times$), and plug-in SE achieves 97.5\%---close to nominal without bootstrap overhead.
1151	
1152	\paragraph{Finite-sample remainder.}
1153	By first-order matrix perturbation, $\hat{C}_s^{-1} = C_s^{-1} - C_s^{-1} E_s C_s^{-1} + O(\|E_s\|^2)$, where $E_s = \hat{C}_s - C_s$ satisfies $\|E_s\| = O_p(n_{\text{expert}}^{-1/2})$.
1154	The remainder in the corrected CATE is therefore $R_n = O_p(n_{\text{expert}}^{-1/2} \cdot \|C_s^{-1}\|^2) = O_p(n_{\text{expert}}^{-1/2} \cdot \kappa(C_s))$, since $\|C_s^{-1}\| = O(\kappa(C_s))$ for stochastic matrices.
1155	This motivates the $\kappa > 100$ singularity guard (Section~\ref{sec:method}).
1156	
1157	\subsection{CausalForest Oracle Coverage Decomposition}
1158	\label{app:cf_oracle}
1159	
1160	To isolate the source of CausalForest under-coverage, we compare six estimation strategies that progressively remove sources of uncertainty: (1)~Oracle (true $Z$, no correction), (2)~EC-HTE with true $C_s$, (3)~EC-HTE with estimated $\hat{C}_s$ (HB), (4)~Global with true $\bar{C}$, (5)~Global with estimated $\hat{\bar{C}}$, and (6)~Naive.
1161	Table~\ref{tab:cf_oracle} reports coverage, $|\text{bias}|$, and RMSE across three DGP configurations (100 MC runs each).
1162	
1163	\begin{table}[h]
1164	\centering
1165	\caption{CausalForest oracle coverage decomposition. Coverage averaged over subgroups and $z$-levels.}
1166	\label{tab:cf_oracle}
1167	\small
1168	\begin{tabular}{ll ccc}
1169	\toprule
1170	DGP & Method & Cov.\ (\%) & $|\text{Bias}|$ & RMSE \\
1171	\midrule
1172	\multirow{6}{*}{\shortstack[l]{$K{=}4$, extreme\\$n{=}500$}}
1173	 & Oracle (true $Z$)       & 94.5 & 0.006 & 0.078 \\
1174	 & EC-HTE true $C_s$       & 92.5 & 0.008 & 0.114 \\
1175	 & EC-HTE est.\ $\hat{C}_s$ & 93.1 & 0.015 & 0.121 \\
1176	 & Global true $\bar{C}$   & 91.3 & 0.037 & 0.110 \\
1177	 & Global est.\ $\hat{\bar{C}}$ & 91.1 & 0.038 & 0.111 \\
1178	 & Naive                    & 88.3 & 0.045 & 0.095 \\
1179	\midrule
1180	\multirow{6}{*}{\shortstack[l]{$K{=}2$, extreme\\$n{=}250$}}
1181	 & Oracle (true $Z$)       & 94.0 & 0.002 & 0.056 \\
1182	 & EC-HTE true $C_s$       & 94.0 & 0.003 & 0.073 \\
1183	 & EC-HTE est.\ $\hat{C}_s$ & 92.5 & 0.004 & 0.079 \\
1184	 & Global true $\bar{C}$   & 88.5 & 0.045 & 0.083 \\
1185	 & Global est.\ $\hat{\bar{C}}$ & 88.3 & 0.045 & 0.085 \\
1186	 & Naive                    & 82.8 & 0.046 & 0.077 \\
1187	\midrule
1188	\multirow{6}{*}{\shortstack[l]{$K{=}2$, MF2 DGP\\$\tau{=}(0.10,0.40)$}}
1189	 & Oracle (true $Z$)       & 96.0 & 0.077 & 0.091 \\
1190	 & EC-HTE true $C_s$       & 91.3 & 0.103 & 0.112 \\
1191	 & EC-HTE est.\ $\hat{C}_s$ & 92.3 & 0.100 & 0.111 \\
1192	 & Global true $\bar{C}$   & 95.0 & 0.107 & 0.114 \\
1193	 & Global est.\ $\hat{\bar{C}}$ & 94.3 & 0.105 & 0.114 \\
1194	 & Naive                    & 77.3 & 0.120 & 0.125 \\
1195	\bottomrule
1196	\end{tabular}
1197	\end{table}
1198	
1199	Three findings emerge.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a25a4c0-1ece-49c5-bec6-6594ba1279b2",
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "7f0f5e35-7743-475f-a864-34d675f538e3",
  "sourceToolAssistantUUID": "6a25a4c0-1ece-49c5-bec6-6594ba1279b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T19:23:01.743Z_

<details open><summary>🔧 Tool call — Read · `toolu_013gLMrd82E6XbuGcnKnWjkE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 1200,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f0f5e35-7743-475f-a864-34d675f538e3",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3bqDAFGkoQnXvqAiCz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a45793b2-2063-48c0-a6f7-b7ce181a12f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVnMbttr7LU9HoAQbzJtaZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6954,
      "cache_read_input_tokens": 55913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6954,
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

_source line 38 · 2026-05-23T19:23:01.749Z_

<details><summary>↩ Tool result · `toolu_013gLMrd82E6XbuGcnKnWjkE`</summary>

```text
1200	First, oracle coverage is 94--96\% across all DGPs, confirming that CausalForest plug-in SE is well-calibrated when labels are correct.
1201	Second, EC-HTE with true $C_s$ achieves 91--94\% coverage---a 0--5pp gap from oracle (configuration-dependent), reflecting $M^{-1}$ SE propagation asymmetry across DGPs rather than confusion matrix estimation error.
1202	Third, the gap between true and estimated $C_s$ is ${\leq}$1.5pp ($K{=}2$) and $<$1pp ($K{=}4$), confirming that CM estimation uncertainty contributes negligibly at $n_{\text{expert}} \geq 250$.
1203	
1204	\section{Robustness to Assumption Violations}
1205	\label{app:a5_violation}
1206	
1207	\subsection{Assumption (A5): Subgroup-Specific Treatment Effects}
1208	
1209	\begin{corollary}[Subgroup-Specific Treatment Effect Heterogeneity]
1210	\label{cor:a5_relaxation}
1211	When $\Delta\tau$ varies across subgroups ($\Delta\tau_s = \tau_s(1) - \tau_s(0)$), the bias of global correction in subgroup $s$ at level $z{=}0$ is $+\delta_s \cdot \Delta\tau_s / (1 - 2\bar{\pi})$, and at level $z{=}1$ is $-\delta_s \cdot \Delta\tau_s / (1 - 2\bar{\pi})$.
1212	\end{corollary}
1213	The proof follows directly from Theorem~\ref{thm:bias_identity} with $\tau_s$ replacing $\tau$.
1214	
1215	Our main analysis assumes that subgroup misclassification rates $\delta_s$ and subgroup CATE magnitudes $\Delta\tau_s$ are independent (Assumption A5).
1216	In practice, both may depend on text features that define subgroups, introducing correlation.
1217	We test robustness under two configurations with the DIM estimator ($K{=}2$, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 50 MC replications, $\pi = [0.05, 0.25]$):
1218	\emph{aligned} (positive $\delta_s$--$\Delta\tau_s$ correlation: high-error S1 has the larger treatment effect, $\Delta\tau = [0.30, 0.70]$) and
1219	\emph{adversarial} (negative correlation: high-error S1 has the smaller effect, $\Delta\tau = [0.70, 0.30]$).
1220	
1221	\begin{table}[h]
1222	\centering
1223	\caption{Coverage and $|\text{bias}|$ under A5 violation ($K{=}2$, $n_{\text{expert}}{=}250$, 50 MC). Target coverage: 0.95.}
1224	\label{tab:a5_violation}
1225	\small
1226	\begin{tabular}{llcccc}
1227	\toprule
1228	Config & Method & S0 cov & S1 cov & S0 $|\text{bias}|$ & S1 $|\text{bias}|$ \\
1229	\midrule
1230	\multirow{4}{*}{Aligned}
1231	 & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\
1232	 & Naive         & 0.93 & 0.25 & 0.022 & 0.174 \\
1233	 & Global        & 0.93 & 0.82 & 0.036 & 0.094 \\
1234	 & EC-HTE (EB)   & 0.95 & 0.95 & 0.005 & 0.017 \\
1235	\midrule
1236	\multirow{4}{*}{Adversarial}
1237	 & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\
1238	 & Naive         & 0.90 & 0.78 & 0.042 & 0.074 \\
1239	 & Global        & 0.74 & 0.93 & 0.098 & 0.040 \\
1240	 & EC-HTE (EB)   & 0.94 & 0.96 & 0.002 & 0.007 \\
1241	\bottomrule
1242	\end{tabular}
1243	\end{table}
1244	
1245	In the aligned configuration, the $\delta_s \times \Delta\tau_s$ product is maximized in the high-error subgroup, causing naive S1 coverage to collapse to 0.25.
1246	Global correction improves S1 but cannot fully correct without subgroup-specific error rates.
1247	In the adversarial configuration, global correction overcorrects the low-error subgroup (S0 coverage 0.74).
1248	EC-HTE (EB) maintains $\geq 0.94$ coverage across both subgroups in both configurations, with bias comparable to the oracle.
1249	Results at $n_{\text{expert}}{=}500$ are consistent (all EC-HTE coverages $\in [0.93, 0.99]$).
1250	
1251	\subsection{Assumption (A1): Sensitivity to Outcome-Dependent Misclassification}
1252	\label{app:a1_sensitivity}
1253	
1254	We assess EC-HTE's robustness when misclassification depends on potential outcomes, violating~(A1).
1255	We modify the synthetic DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\text{expert}}{=}250$) so that misclassification probability becomes outcome-dependent: $P(\hat{Z}{\neq}Z \mid Z, S, Y) = \mathrm{clamp}(\pi_s + \gamma \cdot (Y - \mu_Y)/\sigma_Y,\, 0,\, 1)$, where $\gamma \in \{0, 0.05, 0.10, 0.15, 0.20\}$ controls the strength of violation.
1256	Table~\ref{tab:a1_sensitivity} reports results averaged over 100 MC runs.
1257	
1258	\begin{table}[h]
1259	\centering
1260	\caption{Sensitivity to Assumption~(A1) violation. Coverage and $|\text{bias}|$ under outcome-dependent misclassification ($\gamma > 0$).}
1261	\label{tab:a1_sensitivity}
1262	\small
1263	\begin{tabular}{lccc ccc}
1264	\toprule
1265	& \multicolumn{3}{c}{Coverage (\%)} & \multicolumn{3}{c}{$|\text{Bias}|$} \\
1266	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
1267	$\gamma$ & EC-HTE & Global & Naive & EC-HTE & Global & Naive \\
1268	\midrule
1269	0.00 & 95.5 & 92.7 & 87.7 & 0.060 & 0.065 & 0.061 \\
1270	0.05 & 95.5 & 93.5 & 83.8 & 0.059 & 0.064 & 0.064 \\
1271	0.10 & 95.3 & 93.8 & 83.5 & 0.063 & 0.064 & 0.067 \\
1272	0.15 & 94.8 & 94.3 & 79.2 & 0.065 & 0.064 & 0.070 \\
1273	0.20 & 93.5 & 94.0 & 79.5 & 0.068 & 0.063 & 0.073 \\
1274	\bottomrule
1275	\end{tabular}
1276	\end{table}
1277	
1278	EC-HTE maintains near-nominal coverage ($\geq$93.5\%) across the full $\gamma$ range, with $|\text{bias}|$ increasing only 13.7\% from $\gamma{=}0$ to $\gamma{=}0.2$.
1279	All correction methods (Global, Stratified MLE, HB) maintain $\geq$90\% coverage, indicating that moderate (A1) violations do not catastrophically degrade confusion-matrix-based correction.
1280	The naive estimator degrades most rapidly (coverage $-$8.2pp), consistent with outcome-dependent misclassification compounding the uncorrected label noise.
1281	
1282	\subsection{Assumption (A1): Treatment-Dependent Misclassification}
1283	\label{app:treatment_dep}
1284	
1285	We extend the (A1) sensitivity analysis to the treatment-dependent case, where misclassification probability depends on treatment assignment $T$: $P(\hat{Z}{\neq}Z \mid Z, S, T) = \mathrm{clamp}(\pi_s + \gamma_T \cdot (2T - 1),\, 0,\, 1)$, with $\gamma_T \in \{0, 0.05, 0.10, 0.15, 0.20\}$.
1286	This scenario arises when LLM accuracy varies with treatment status---e.g., treated texts may be systematically harder to classify.
1287	Setup: $K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 100 MC runs.
1288	
1289	\begin{table}[h]
1290	\centering
1291	\caption{Sensitivity to treatment-dependent misclassification ($\gamma_T$). EC-HTE maintains $\geq$89.7\% coverage at $\gamma_T \leq 0.05$.}
1292	\label{tab:treatment_dep}
1293	\small
1294	\begin{tabular}{lcc}
1295	\toprule
1296	$\gamma_T$ & EC-HTE Coverage & EC-HTE RMSE \\
1297	\midrule
1298	0.00 & 0.945 & 0.075 \\
1299	0.05 & 0.897 & 0.092 \\
1300	0.10 & 0.750 & 0.133 \\
1301	0.15 & 0.525 & 0.177 \\
1302	0.20 & 0.370 & 0.224 \\
1303	\bottomrule
1304	\end{tabular}
1305	\end{table}
1306	
1307	EC-HTE is robust to small treatment-dependent violations ($\gamma_T \leq 0.05$), maintaining $\geq$89.7\% coverage with modest RMSE increase (0.075 to 0.092).
1308	At $\gamma_T = 0.10$, coverage drops to 75.0\%, establishing this as the approximate breakeven point.
1309	The degradation is steeper than for outcome-dependent violations (Table~\ref{tab:a1_sensitivity}), because treatment-dependent errors directly contaminate the treatment arm contrast.
1310	Figure~\ref{fig:treatment_dep} visualizes the coverage and RMSE trajectories.
1311	
1312	\begin{figure}[h]
1313	\centering
1314	\includegraphics[width=\columnwidth]{figures/treatment_dep_misclass.pdf}
1315	\caption{EC-HTE coverage and RMSE under treatment-dependent misclassification. Dashed line: 90\% coverage threshold. Breakeven at $\gamma_T \approx 0.10$.}
1316	\label{fig:treatment_dep}
1317	\end{figure}
1318	
1319	\subsection{Extension to Confounded Treatment Assignment}
1320	\label{app:confounded_dgp}
1321	
1322	EC-HTE's confusion matrix correction operates on estimated CATEs regardless of how those estimates are produced.
1323	To verify compatibility with observational (non-RCT) designs, we pair EC-HTE with an inverse probability weighted difference-in-means (IPW-DIM) estimator under confounded treatment assignment.
1324	
1325	\paragraph{DGP.}
1326	$N{=}5{,}000$, $K{=}2$, $\pi = [0.05, 0.25]$, $n_{\text{expert}}{=}250$, 100 MC replications.
1327	A covariate $X \sim \mathcal{N}(0,1)$ confounds both treatment and outcome:
1328	$T \sim \text{Bernoulli}(\sigma(\beta X))$ with $\beta{=}0.5$ (moderate confounding; propensity range $[0.38, 0.62]$),
1329	$Y = 1 + 0.5 Z + 0.3 X + \tau(Z) \cdot T + \eta$, $\eta \sim \mathcal{N}(0,1)$.
1330	Treatment effects are $\tau(Z{=}0){=}0$, $\tau(Z{=}1){=}0.3$.
1331	The IPW-DIM estimator uses \emph{oracle propensity} $e(X) = \sigma(\beta X)$, with propensity scores clipped to $[0.05, 0.95]$.
1332	
1333	\begin{table}[h]
1334	\centering
1335	\caption{EC-HTE under confounded treatment assignment (IPW-DIM with oracle propensity, $\beta{=}0.5$, 100 MC).}
1336	\label{tab:confounded_dgp}
1337	\small
1338	\begin{tabular}{lccc}
1339	\toprule
1340	Method & Coverage & RMSE & $|\text{Bias}|$ \\
1341	\midrule
1342	Oracle (true $Z$ + IPW) & 0.943 & 0.061 & 0.048 \\
1343	HB EC-HTE              & 0.950 & 0.086 & 0.068 \\
1344	Global                  & 0.930 & 0.087 & 0.071 \\
1345	Strat MLE               & 0.950 & 0.087 & 0.069 \\
1346	Naive                   & 0.863 & 0.083 & 0.066 \\
1347	\bottomrule
1348	\end{tabular}
1349	\end{table}
1350	
1351	EC-HTE achieves 95.0\% coverage, within 0.7pp of the oracle (94.3\%), confirming that confusion matrix correction and propensity weighting compose without interference.
1352	The improvement is most pronounced in the high-error subgroup ($\pi{=}0.25$): EC-HTE coverage is 96.0\% vs.\ naive 78.5\% ($+$17.5pp).
1353	Global coverage (93.0\%) falls below the correction methods (95.0\%), consistent with the cost of ignoring subgroup-level error heterogeneity even in the confounded setting.
1354	
1355	\paragraph{Sensitivity to confounding strength and propensity estimation.}
1356	We sweep $\beta \in \{0.25, 0.5, 1.0, 2.0\}$ and compare oracle propensity ($e(X) = \sigma(\beta X)$) with estimated propensity (logistic regression fit on $(X, T)$), yielding 8 configurations (100 MC each).
1357	Table~\ref{tab:confounded_sweep} reports HB EC-HTE and naive coverage.
1358	
1359	\begin{table}[h]
1360	\centering
1361	\caption{EC-HTE coverage across confounding strengths and propensity sources. The logistic regression propensity model is correctly specified; propensity misspecification is a complementary concern addressed by the IPW literature.}
1362	\label{tab:confounded_sweep}
1363	\small
1364	\begin{tabular}{cccc}
1365	\toprule
1366	$\beta$ & Propensity & HB Coverage & Naive Coverage \\
1367	\midrule
1368	0.25 & Oracle    & 0.963 & 0.848 \\
1369	0.25 & Estimated & 0.973 & 0.845 \\
1370	0.50 & Oracle    & 0.950 & 0.863 \\
1371	0.50 & Estimated & 0.958 & 0.858 \\
1372	1.00 & Oracle    & 0.958 & 0.898 \\
1373	1.00 & Estimated & 0.960 & 0.883 \\
1374	2.00 & Oracle    & 0.945 & 0.858 \\
1375	2.00 & Estimated & 0.948 & 0.858 \\
1376	\bottomrule
1377	\end{tabular}
1378	\end{table}
1379	
1380	EC-HTE maintains coverage $\geq$94.5\% across all 8 configurations, including strong confounding ($\beta{=}2.0$, propensity range $[0.12, 0.88]$).
1381	The oracle--estimated gap is $\leq$1pp, confirming that propensity estimation error does not meaningfully degrade EC-HTE when the propensity model is correctly specified.
1382	This validates that EC-HTE is robust to confounded treatment assignment when the propensity model is correctly specified.
1383	
1384	\subsection{Empirical Comparison with Frazis--Loewenstein Correction}
1385	\label{app:fl_comparison}
1386	
1387	We empirically compare EC-HTE's confusion matrix inversion against the scalar attenuation correction of \citet{frazis2003estimating} (F-L).
1388	The F-L correction rescales the observed estimate as $\hat{\tau}_{\text{FL}} = \hat{\tau}_{\text{obs}} / (1 - 2\bar{\pi})$, where $\bar{\pi}$ is the (global or per-subgroup) misclassification rate.
1389	We test two variants: F-L \emph{scalar} (single global $\bar{\pi}$) and F-L \emph{per-subgroup} ($\pi_s$-specific rescaling).
1390	Setup: $K{=}2$, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, $\pi{=}[0.05, 0.25]$ (extreme heterogeneity), $\tau(z{=}0){=}0$, $\tau(z{=}1){=}0.3$, 100 MC runs.
1391	
1392	\begin{table}[h]
1393	\centering
1394	\caption{F-L correction vs.\ EC-HTE under heterogeneous misclassification ($\Delta\pi{=}0.20$). Both F-L variants produce \emph{higher} aggregate bias than the uncorrected estimator.}
1395	\label{tab:fl_comparison}
1396	\small
1397	\begin{tabular}{lccc}
1398	\toprule
1399	Method & $|\text{Bias}|$ & RMSE & Coverage \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a45793b2-2063-48c0-a6f7-b7ce181a12f2",
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "99861545-d76f-4598-b3b8-c5ebe79b7296",
  "sourceToolAssistantUUID": "a45793b2-2063-48c0-a6f7-b7ce181a12f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T19:23:05.249Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BVGbwyLKfY3g6wLSmh95sM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 1400,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99861545-d76f-4598-b3b8-c5ebe79b7296",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3c6p1xNUB65g4iAuEK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e97e270-e8b1-4944-aece-ac6cc7c659e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Czo1P1ULCyS6mFuXYt4jUU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5350,
      "cache_read_input_tokens": 62867,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5350
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 62867,
          "cache_creation_input_tokens": 5350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5350,
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

_source line 40 · 2026-05-23T19:23:05.258Z_

<details><summary>↩ Tool result · `toolu_01BVGbwyLKfY3g6wLSmh95sM`</summary>

```text
1400	\midrule
1401	Oracle         & 0.045 & 0.056 & 0.943 \\
1402	Naive          & 0.062 & 0.077 & 0.858 \\
1403	Global (CM inv)& 0.064 & 0.081 & 0.938 \\
1404	HB EC-HTE      & 0.064 & 0.086 & \textbf{0.953} \\
1405	F-L Scalar     & 0.091 & 0.116 & 0.850 \\
1406	F-L Per-Subgroup & 0.112 & 0.158 & 0.838 \\
1407	\bottomrule
1408	\end{tabular}
1409	\end{table}
1410	
1411	Both F-L variants produce \emph{higher} bias and RMSE than the naive estimator (F-L per-subgroup $|\text{bias}|{=}0.112$ vs.\ naive $0.062$), demonstrating that scalar attenuation cannot substitute for confusion matrix inversion under subgroup-heterogeneous misclassification.
1412	The per-subgroup bias direction reveals the mechanism: F-L scalar over-corrects the low-error subgroup ($s_0$: mean bias ${=}+0.073$ vs.\ naive $+0.005$, a $14.6\times$ amplification), while F-L per-subgroup dramatically over-corrects the high-error subgroup ($s_1$: mean bias ${=}+0.160$).
1413	EC-HTE achieves near-zero per-subgroup bias ($s_0{:}\,{+}0.006$, $s_1{:}\,{+}0.001$) with nominal coverage (95.3\%).
1414	The root cause is structural: F-L's $1/(1{-}2\pi)$ scaling amplifies each $z$-level estimate independently, whereas CM inversion simultaneously redistributes the cross-contamination between misclassified and correctly classified observations.
1415	
1416	\subsection{End-to-End Validation with Asymmetric Confusion Matrices}
1417	\label{app:asymmetric_endtoend}
1418	
1419	We validate EC-HTE under strongly asymmetric confusion matrices ($\text{FPR}/\text{FNR}$ ratio up to $7{:}1$), simulating the error profile of GPT-4.1 on Civil Comments.
1420	Setup: $K{=}2$, $N{=}5{,}000$, $n_{\text{expert}}{=}250$; $s_0$: $\text{FPR}{=}0.05$, $\text{FNR}{=}0.02$ (low error); $s_1$: $\text{FPR}{=}0.38$, $\text{FNR}{=}0.054$ ($7{:}1$ ratio); 100 MC runs.
1421	We compare EC-HTE using the full $2{\times}2$ asymmetric CM (Remark~2) against the symmetric assumption ($\text{FPR}{=}\text{FNR}{=}\pi_s$).
1422	
1423	\begin{table}[h]
1424	\centering
1425	\caption{EC-HTE under asymmetric misclassification ($\text{FPR}/\text{FNR}$ up to $7{:}1$). The asymmetric formula improves coverage by $+1.5$pp and RMSE by $11.5\%$.}
1426	\label{tab:asymmetric_endtoend}
1427	\small
1428	\begin{tabular}{lccc}
1429	\toprule
1430	Method & $|\text{Bias}|$ & RMSE & Coverage \\
1431	\midrule
1432	Oracle              & 0.045 & 0.056 & 0.943 \\
1433	EC-HTE (asymmetric) & 0.057 & 0.074 & \textbf{0.945} \\
1434	Naive               & 0.059 & 0.073 & 0.870 \\
1435	Global (asymmetric) & 0.061 & 0.076 & 0.915 \\
1436	EC-HTE (symmetric)  & 0.062 & 0.083 & 0.930 \\
1437	Global (symmetric)  & 0.063 & 0.078 & 0.915 \\
1438	\bottomrule
1439	\end{tabular}
1440	\end{table}
1441	
1442	EC-HTE with the asymmetric formula achieves 94.5\% coverage versus 93.0\% under the symmetric assumption ($+1.5$pp), with RMSE improved from 0.083 to 0.074 ($-11.5\%$).
1443	The improvement concentrates in the high-error subgroup ($s_1$): asymmetric coverage is 93.0\% vs.\ symmetric 91.0\%.
1444	Practitioners should estimate full $2 \times 2$ confusion matrices rather than assuming symmetric misclassification, particularly when FPR and FNR differ substantially.
1445	
1446	\subsection{Complementarity with LLM Calibration}
1447	\label{app:calibration}
1448	
1449	Temperature or Platt scaling~\cite{guo2017calibration} can reduce per-subgroup misclassification rates, but does not eliminate heterogeneity $\Delta\pi$.
1450	We simulate calibration by shrinking per-subgroup rates from $\pi{=}[0.05, 0.25]$ ($\Delta\pi{=}0.20$) to $\pi{=}[0.08, 0.15]$ ($\Delta\pi{=}0.07$), testing whether EC-HTE remains necessary post-calibration.
1451	Setup: $K{=}2$, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 100 MC runs.
1452	
1453	\begin{table}[h]
1454	\centering
1455	\caption{Calibration reduces $\Delta\pi$ but does not eliminate it; EC-HTE corrects the residual bias. Best coverage is achieved by combining both.}
1456	\label{tab:calibration}
1457	\small
1458	\begin{tabular}{lccc}
1459	\toprule
1460	Method & $|\text{Bias}|$ & RMSE & Coverage \\
1461	\midrule
1462	Oracle                    & 0.043 & 0.053 & 0.963 \\
1463	Calibrated + EC-HTE       & 0.055 & 0.069 & \textbf{0.965} \\
1464	Calibrated + Global       & 0.055 & 0.068 & 0.963 \\
1465	Calibrated + Naive        & 0.051 & 0.064 & 0.913 \\
1466	Uncalibrated + EC-HTE     & 0.064 & 0.084 & 0.938 \\
1467	Uncalibrated + Global     & 0.069 & 0.085 & 0.920 \\
1468	Uncalibrated + Naive      & 0.063 & 0.079 & 0.840 \\
1469	\bottomrule
1470	\end{tabular}
1471	\end{table}
1472	
1473	Calibration alone improves naive coverage from 84.0\% to 91.3\% but does not reach the nominal 95\%.
1474	Calibrated + EC-HTE achieves the highest coverage (96.5\%), demonstrating that calibration and EC-HTE address complementary error sources: calibration reduces per-subgroup $\pi_s$ while EC-HTE corrects the residual $\delta_s$-driven bias from heterogeneity that persists post-calibration.
1475	Propensity estimation robustness under model misspecification is a complementary concern addressed by the IPW literature; EC-HTE as a downstream correction layer does not alter IPW behavior.
1476	
1477	\subsection{Policy Reversal Zone Analysis}
1478	\label{app:policy_reversal}
1479	
1480	When the true treatment effect is small, global correction can reverse the sign of estimated CATE---concluding a beneficial treatment is harmful---creating a \emph{policy reversal zone}.
1481	We sweep $\tau(0) \in \{0.01, 0.02, 0.03, 0.05, 0.07, 0.10\}$ under the standard DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 100 MC runs; $\Delta\tau{=}0.30$).
1482	
1483	\begin{table}[h]
1484	\centering
1485	\caption{Policy reversal zone: fraction of configurations where global correction reverses the sign of estimated CATE.
1486	The naive estimator produces zero sign reversals across all $\tau(0)$ values; EC-HTE also achieves 0\% reversal.}
1487	\label{tab:policy_reversal}
1488	\small
1489	\begin{tabular}{ccc}
1490	\toprule
1491	$\tau(0)$ & Global reversal \% & Most extreme $\hat{\tau}_{\text{global}}$ \\
1492	\midrule
1493	0.01 & 31.0 & $-0.079$ \\
1494	0.02 & 21.6 & --- \\
1495	0.03 & 14.9 & $-0.059$ \\
1496	0.05 & 6.1  & $-0.039$ \\
1497	0.07 & 1.6  & --- \\
1498	$\geq$0.10 & 0 & --- \\
1499	\bottomrule
1500	\end{tabular}
1501	\end{table}
1502	
1503	The reversal rate increases monotonically as $\tau(0)$ decreases: at $\tau(0) = 0.01$, 31\% of configurations yield sign reversal, with the most extreme case estimating $\hat{\tau} = -0.079$ when the true effect is $\tau = +0.01$.
1504	The critical threshold is $\tau(0) < 0.089$, matching the closed-form prediction from Theorem~\ref{thm:bias_identity}: $|\delta_{\max} \cdot \Delta\tau_{\max}| / (1 - 2\bar{\pi}) = 0.125 \times 0.50 / 0.70 = 0.089$.
1505	The most dangerous combination ($\tau(0) = 0.01$, $\delta_{\text{misclass}} = 0.19$) reaches 42.9\% reversal rate.
1506	The naive estimator produces zero sign reversals across all $\tau(0)$ values, confirming that reversal is an artifact of global correction, not inherent estimation noise.
1507	
1508	Figure~\ref{fig:policy_reversal} visualizes the reversal zone across the $\Delta\pi \times \tau(0)$ parameter space.
1509	
1510	\begin{figure}[h]
1511	\centering
1512	\includegraphics[width=\columnwidth]{figures/policy_reversal_zone.pdf}
1513	\caption{Policy reversal zone: sign-reversal rate as a function of $\tau(0)$ and $\Delta\pi$. Shaded region marks configurations where global correction reverses the CATE sign, directing policy toward the wrong subgroups.}
1514	\label{fig:policy_reversal}
1515	\end{figure}
1516	
1517	\section*{Use of AI Assistants}
1518	\label{app:ai-assistants}
1519	
1520	We used Claude (Anthropic) as an AI coding and writing assistant
1521	throughout this work. Specifically:
1522	\begin{itemize}
1523	    \item \textbf{Code:} drafting experiment scripts, data-processing
1524	    pipelines, and analysis utilities; debugging and refactoring.
1525	    \item \textbf{Writing:} drafting and revising paper sections,
1526	    polishing prose, and reformatting LaTeX.
1527	    \item \textbf{Literature:} summarizing related papers to inform
1528	    the related-work section.
1529	\end{itemize}
1530	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e97e270-e8b1-4944-aece-ac6cc7c659e9",
  "isSidechain": true,
  "promptId": "10da1a5c-2ab8-4bfe-b0f4-685a8aea573e",
  "agentId": "a02c88d2dafcf0406",
  "type": "user",
  "uuid": "f7fdcdcb-9f3b-456e-be24-b68d046ac73e",
  "sourceToolAssistantUUID": "8e97e270-e8b1-4944-aece-ac6cc7c659e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-23T19:29:04.636Z_

Now I have read all the files completely. Let me compile the comprehensive list of numerical values organized by file.

---

## Complete Numerical Value Extraction by File

### 1. main.tex

| Line | Number | Context |
|------|--------|---------|
| 1 | 11pt | `\documentclass[11pt]{article}` |

No substantive numerical values in this file -- it is just the document skeleton.

---

### 2. abstract.tex

| Line | Number | Context |
|------|--------|---------|
| 4 | 5x | error rates varying by up to `$5\times$` across demographic subgroups |
| 6 | 14.9% | global correction can reverse the sign of estimated CATE in `14.9\%` of configurations |
| 7 | 1.0 | AUC `$= 1.0$` on subgroups with non-zero effect heterogeneity |
| 8 | 7.4x | reduces `$|\text{bias}|$` by `$7.4\times$` under extreme heterogeneity |
| 8 | >=0.90 | coverage `$\geq 0.90$` via hierarchical Bayesian estimation |

---

### 3. introduction.tex

| Line | Number | Context |
|------|--------|---------|
| 10 | 5x | misclassification rates varying by up to `5$\times$` across demographic subgroups |
| 10 | 85.8% | GPT-4.1 achieves `85.8\%` accuracy on TweetEval sentiment |
| 10 | 10.2% | error rates range from `10.2\%` to `20.0\%` |
| 10 | 20.0% | error rates range from 10.2% to `20.0\%` |
| 10 | 0.098 | `$\Delta\pi = 0.098$` |
| 13 | 14.9% | `14.9\%` of our synthetic configurations exhibit sign reversal |
| 13 | 0.03 | `$\tau(0) = 0.03$` |
| 13 | +0.03 | true `$\tau = +0.03$` |
| 13 | -0.059 | estimated `$\hat{\tau} = -0.059$` |
| 13 | 31% | rising to `31\%` at `$\tau(0) = 0.01$` |
| 13 | 0.01 | `$\tau(0) = 0.01$` |
| 13 | 8 | all `eight` real LLMs tested amplify bias |
| 14 | 5.9x | amplifies bias by up to `5.9$\times$` (`$K{=}4$` with CausalForest) |
| 14 | 4 | `$K{=}4$` |
| 14 | 2.9x | increases bias by up to `2.9$\times$` |
| 17 | 0.97 | `$R^2 \geq 0.97$` on synthetic grids |
| 17 | 0.975 | `$R^2 = 0.975$` across 11 real LLM confusion matrices |
| 17 | 11 | `11` real LLM confusion matrices |
| 18 | 1.0 | AUC `$= 1.0$` on subgroups with non-zero effect heterogeneity |
| 20 | 0.059 | reduces `$|\text{bias}|$` from `0.059` to `0.008` |
| 20 | 0.008 | reduces from 0.059 to `0.008` |
| 20 | 2 | `$K{=}2$` |
| 28 | 2 | `$K{=}2$` |
| 28 | 0.03 | `$\tau(0) = 0.03$` |
| 28 | 7.5% | sign reversals (`7.5\%` of subgroup estimates) |
| 28 | +0.03 | true `$\tau = +0.03$` |
| 28 | -0.059 | estimated `$\hat{\tau} = -0.059$` |
| 28 | 14.9% | `14.9\%` of configurations exhibit sign reversal |
| 28 | 8 | all `8` real LLMs amplify bias |
| 28 | 0% | EC-HTE: `0\%` reversal |
| 34 | 14.9% | reverse the sign of estimated CATE in `14.9\%` of configurations |
| 34 | 0.03 | `$\tau(0) = 0.03$` |
| 34 | 31% | `31\%` at `$\tau(0) = 0.01$` |
| 34 | 0.01 | `$\tau(0) = 0.01$` |
| 34 | 8 | all `eight` real LLMs tested |
| 34 | 0.97 | `$R^2 \geq 0.97$` |
| 34 | 11 | `11` real LLM confusion matrices |
| 35 | 1.0 | AUC `$= 1.0$` |

---

### 4. method.tex

| Line | Number | Context |
|------|--------|---------|
| 10 | K (from 1 to K) | confusion matrices `$\{C_s\}_{s=1}^K$` |
| 15 | 5ms | `$<$5ms` for `$K{=}4$`, `$N{=}5{,}000$` |
| 15 | 4 | `$K{=}4$` |
| 15 | 5,000 | `$N{=}5{,}000$` |
| 15 | 5s | full Gibbs MCMC alternative requires `$\sim$5s` |
| 16 | 100 | Bootstrap SE (`$B{=}100$`) |
| 16 | 0.4s | adds `$\sim$0.4s` |
| 17 | 87.5% | outperforms stratified MLE in `87.5\%` of configurations |
| 17 | 21 of 24 | (`21 of 24`) |
| 17 | 100 | `$n_{\text{expert}} / K < 100$` |
| 18 | 25 | `$\geq 25$` per subgroup |
| 19 | 1000 | At `$n_{\text{expert}} \geq 1000$` |
| 19 | 0.5% | converge to within `0.5\%` on all metrics |
| 20 | <5% | `$<$5\%` RMSE variation |
| 20 | 2x | `2$\times$` hyperprior perturbation |
| 31 | 100 | condition number `$\kappa(\hat{C}_s) > 100$` |
| 31 | 2x2 | a `$2{\times}2$` symmetric confusion matrix |
| 31 | 0.495 | `$\pi_s > 0.495$` |
| 32 | 1.25 | `$\kappa \leq 1.25$` |
| 32 | >=93% | coverage `($\geq$93\%)` |
| 32 | 1.4, 3.0 | `$\kappa \in [1.4, 3.0]$` range |
| 46 | 100 | `$n_{\text{expert}} \geq 100$` |
| 46 | 100 | bootstrap (`$B{=}100$`) |
| 46 | >=95% | maintains `$\geq$95\%` coverage |
| 46 | 25, 50, 75, 100, 200 | `$n_{\text{expert}} \in \{25, 50, 75, 100, 200\}$` |
| 46 | >=91% | even plug-in SE achieves `$\geq$91\%` |
| 46 | 25 | at `$n_{\text{expert}}{=}25$` |
| 47 | 50 | `$n_{\text{expert}}/K < 50$` |
| 52 | 0.86 | AUC `=` `0.86` at the subgroup level |
| 52 | 1.0 | reaching `1.0` when restricted to subgroups with `$\tau_s > 0$` |
| 59 | 0.179 | reduces `$|\text{bias}|$` from `0.179` to `0.007` |
| 59 | 0.007 | to `0.007` |

---

### 5. theory.tex

| Line | Number | Context |
|------|--------|---------|
| 10 | 2 | `$Z \in \{0, 1\}$` binary effect modifier |
| 11 | 2x2 | `$2 \times 2$` confusion matrix |
| 20 | 0.5 | `$P(Z{=}0) = P(Z{=}1) = 0.5$` |
| 54 | 2 | `$K{=}2$` |
| 54 | 0.058 | `$|\text{bias}|$` from `0.058` |
| 54 | 0.122 | to `0.122` (`$2.1\times$` naive) |
| 54 | 2.1x | `$2.1\times$` naive |
| 54 | 0.168 | F-L per-subgroup to `0.168` |
| 54 | 2.9x | `$2.9\times$` |
| 64 | 0.86 | AUC decreases from `0.86` to `0.66` |
| 64 | 0.66 | to `0.66` |
| 67 | 0.991 | `$R^2 = 0.991$` |
| 74 | >=93% | `$\geq$93\%` coverage |
| 74 | 74-82% | global correction degrades to `74--82\%` |
| 80 | 0.976 | `$R^2 \geq 0.976$` |
| 80 | 0.1 | even at `$P(Z{=}1) = 0.1$` |
| 80 | 2 | for `$K{=}2$` |
| 80 | 1.06-1.68 | RMSE ratio increases to `1.06--1.68` |
| 81 | 0.994 | `$R^2 = 0.994$` for `$K{=}2$` |
| 81 | 0.974 | `$R^2 = 0.974$` for `$K{=}4$` |
| 81 | 2 | `$K{=}2$` |
| 81 | 4 | `$K{=}4$` |
| 90 | 100 | `$\kappa > 100$` triggers fallback |
| 104 | 0.5 | `$\pi_s > 0.5$` excluded by (A4) |
| 104 | 0.15 | when `$\bar{\pi} = 0.15$` |
| 104 | 0.088 | any subgroup with `$\pi_s < 0.088$` is harmed |
| 108 | 50% | increases bias in `50\%` of `$K{=}2$` configurations |
| 108 | 260/520 | (`260/520`) |
| 108 | 520 | of 520 configurations |
| 108 | 2.86x | amplification reaching `$2.86\times$` (`$K{=}2$`) |
| 108 | 2.41x | `$2.41\times$` (`$K{=}4$`) |

---

### 6. experiments.tex

| Line | Number | Context |
|------|--------|---------|
| 4 | 5,000 | `$N{=}5{,}000$` |
| 4 | 2, 4 | `$K \in \{2, 4\}$` |
| 4 | 100 | `100 MC runs` |
| 4 | 4 | `$K{=}4$` unbalanced subgroups |
| 5 | 0.05, 0.10, 0.15, 0.25 | `$\pi \in \{0.05, 0.10, 0.15, 0.25\}$` |
| 9 | 95% | `95\% CI coverage` |
| 9 | 100 | `100 MC runs` |
| 10 | >=93.5% | all `$\geq$93.5\%` coverage |
| 10 | ~90% | `$\approx$90\%` at `$\gamma_T \leq 0.05$` |
| 10 | 0.05 | `$\gamma_T \leq 0.05$` |
| 15 | 520 | `520 configurations` |
| 15 | 0, 0.25 | `$\Delta\pi \in [0, 0.25]$` |
| 15 | 0, 0.50 | `$\Delta\tau \in (0, 0.50]$` |
| 16 | 0.994 | `$R^2 = 0.994$` (`$K{=}2$`) |
| 16 | 0.974 | `$0.974$` (`$K{=}4$`) |
| 16 | 0.976 | `$R^2 \geq 0.976$` even at `$P(Z{=}1) = 0.1$` |
| 16 | 0.1 | `$P(Z{=}1) = 0.1$` |
| 17 | 50% | worsens bias in `50\%` of `$K{=}2$` configurations |
| 17 | 260/520 | (`260/520`) |
| 17 | 2.86x | amplification reaching `2.86$\times$` |
| 17 | 2.41x | `2.41$\times$` |
| 18 | 14.9% | `14.9\%` of configurations at `$\tau(0) = 0.03$` |
| 18 | 0.03 | `$\tau(0) = 0.03$` |
| 18 | 31% | (`31\%` at `$\tau(0) = 0.01$`) |
| 18 | 0.01 | `$\tau(0) = 0.01$` |
| 18 | 0.089 | critical threshold `$\tau(0) < 0.089$` |
| 18 | 8 | all `eight` real LLMs |
| 24 | 0.059 | `$|\text{bias}|$` ... (`0.059` vs. `0.058`) |
| 24 | 0.058 | naive (`0.058`) |
| 25 | 0.122 | F-L scalar correction increases to `0.122` |
| 25 | 0.68 | coverage `0.68` |
| 25 | 0.168 | F-L per-subgroup to `0.168` |
| 26 | 0.059 | from `0.059` to `0.008` |
| 26 | 0.008 | to `0.008` |
| 26 | 7.4x | (`7.4$\times$`) |
| 26 | 0.056 | from `0.056` to `0.012` |
| 26 | 0.012 | to `0.012` |
| 26 | 4.7x | (`4.7$\times$`) |
| 26 | 0.94-0.96 | coverage (`0.94--0.96`) |
| 27 | 0.05 | (`$p > 0.05$`) |
| 28 | 8 | At `$K{=}8$` |
| 28 | 31 | `$n_{\text{expert}}/K{=}31$` |
| 28 | >=95.6% | coverage remains `$\geq$95.6\%` |
| 28 | 50 | `$n_{\text{expert}}/K \geq 50$` |
| 32 | 0.191 | from `0.191` to `0.039` |
| 32 | 0.039 | to `0.039` |
| 32 | 4.9x | (`4.9$\times$`) |
| 32 | 0.90 | coverage `0.90` |
| 32 | 5.9x | up to `5.9$\times$` |
| 32 | 500 | `$n{=}500$` |
| 44 | 0.058 | Naive: `0.058` |
| 44 | 0.090 | RMSE: `0.090` |
| 44 | 0.82 | Coverage: `0.82` |
| 45 | 0.059 | Global: `0.059` |
| 45 | 0.099 | RMSE: `0.099` |
| 45 | 0.87 | Coverage: `0.87` |
| 46 | 0.122 | F-L Scalar: `0.122` |
| 46 | 0.159 | RMSE: `0.159` |
| 46 | 0.68 | Coverage: `0.68` |
| 47 | 0.168 | F-L Per-sub.: `0.168` |
| 47 | 0.220 | RMSE: `0.220` |
| 47 | 0.65 | Coverage: `0.65` |
| 48 | 0.012 | Strat. MLE: `0.012` |
| 48 | 0.094 | RMSE: `0.094` |
| 48 | 0.95 | Coverage: `0.95` |
| 49 | 0.008 | HB EC-HTE: `0.008` |
| 49 | 0.089 | RMSE: `0.089` |
| 49 | 0.94 | Coverage: `0.94` |
| 52 | 0.062 | Naive: `0.062` |
| 52 | 0.113 | RMSE: `0.113` |
| 52 | 0.88 | Coverage: `0.88` |
| 53 | 0.056 | Global: `0.056` |
| 53 | 0.125 | RMSE: `0.125` |
| 53 | 0.91 | Coverage: `0.91` |
| 54 | 0.010 | Strat. MLE: `0.010` |
| 54 | 0.127 | RMSE: `0.127` |
| 54 | 0.95 | Coverage: `0.95` |
| 55 | 0.012 | HB EC-HTE: `0.012` |
| 55 | 0.120 | RMSE: `0.120` |
| 55 | 0.96 | Coverage: `0.96` |
| 58 | 0.208 | Naive: `0.208` |
| 58 | 0.231 | RMSE: `0.231` |
| 58 | 0.44 | Coverage: `0.44` |
| 59 | 0.191 | Global: `0.191` |
| 59 | 0.244 | RMSE: `0.244` |
| 59 | 0.58 | Coverage: `0.58` |
| 60 | 0.039 | EC-HTE Forest: `0.039` |
| 60 | 0.180 | RMSE: `0.180` |
| 60 | 0.90 | Coverage: `0.90` |
| 43 | 250 | `$n{=}250$` |
| 51 | 500 | `$n{=}500$` |
| 57 | 500 | `$n{=}500$` |
| 69 | 0.63 | AUC `$= 0.63$` across 16 real LLM-dataset combinations |
| 69 | 16 | `16` real LLM-dataset combinations |
| 69 | 1.0 | recovers AUC `$= 1.0$` |
| 69 | 0.86 | `$0.86$` on synthetic grids |
| 72 | 100 | `$\kappa > 100$` triggers fallback |
| 72 | 13 | all `13` tested LLM-dataset combinations |
| 72 | 1.25, 3 | `$\kappa \in (1.25, 3]$` |
| 72 | >=93% | coverage `$\geq$93\%` |
| 73 | 0.975 | `$R^2 = 0.975$` |

---

### 7. conclusion.tex

| Line | Number | Context |
|------|--------|---------|
| 3 | 14.9% | reversing CATE signs in `14.9\%` of configurations |
| 3 | 8 | all `eight` real LLMs tested |
| 4 | 1.0 | AUC `$= 1.0$` |

---

### 8. limitations.tex

| Line | Number | Context |
|------|--------|---------|
| 4 | 25 | `$\geq 25$` per subgroup |
| 5 | 0.1 | `$P(Z{=}1) = 0.1$` |
| 5 | 4 | `$K{=}4$` |
| 5 | 0.3 | `$P(Z{=}1) \geq 0.3$` |
| 5 | 250 | `$n_{\text{expert}}{=}250$` |
| 6 | 4 | `$K{=}4$` |
| 6 | 100 | `$n_{\text{expert}} \leq 100$` |
| 6 | 3.5x | RMSE reaches `3.5$\times$` that of the naive estimator |
| 7 | 0.5 | FNR or FPR approaches `0.5` |
| 10 | 8 | `$K{=}8$` |
| 10 | 250 | `$n_{\text{expert}}{=}250$` |
| 10 | 31 | `${\approx}31$` labels/subgroup |
| 10 | 95.6% | coverage (`95.6\%`) |
| 15 | >=93.5% | `$\geq$93.5\%` coverage |
| 15 | 0.2 | up to `$\gamma = 0.2$` |
| 15 | 13.7% | bias increasing only `13.7\%` |
| 16 | >=89.7% | `$\geq$89.7\%` coverage |
| 16 | 0.05 | `$\gamma_T \leq 0.05$` |
| 16 | 0.10 | `$\gamma_T = 0.10$` |
| 16 | 75% | `75\%` coverage |
| 18 | 94-96% | `94--96\%` coverage |
| 18 | 200 | `$n_{\text{estimators}}{=}200$` |
| 18 | 93.8% | `93.8\%` aggregate coverage |
| 19 | 100 | `$B{=}100$` |
| 19 | >=95% | `$\geq$95\%` coverage |
| 19 | 25, 50, 75, 100, 200 | `$n_{\text{expert}} \in \{25, 50, 75, 100, 200\}$` |
| 19 | >=91% | `$\geq$91\%` at `$n_{\text{expert}}{=}25$` |
| 19 | 25 | `$n_{\text{expert}}{=}25$` |
| 20 | >=95% | `$\geq$95\%` coverage |
| 22 | 0.86 | AUC `$= 0.86$` |
| 22 | 0.63 | degrades to `$0.63$` |
| 22 | 16 | `16` model-dataset combinations |
| 24 | 0.66 | AUC `$= 0.66$` |
| 28 | 0.991 | `$R^2 = 0.991$` |
| 29 | 52% | comparable bias reduction (`52\%`) |
| 29 | 0.955 | nominal coverage (`0.955`) |

---

### 9. related_work.tex

| Line | Number | Context |
|------|--------|---------|
| 21 | 5x | error rates vary by up to `$5\times$` across demographic subgroups |
| 29 | 80% | `$>$80\%` expert budget savings |
| 36 | 0.975 | `$R^2 = 0.975$` across 11 model-dataset combinations |
| 36 | 11 | `11` model-dataset combinations |

---

### 10. appendix.tex

This file contains the most numerical values. Organized by section:

**EC-HTE Procedure (lines 1-42)**
| Line | Number | Context |
|------|--------|---------|
| 17 | 1.01 | verify `$\hat{R} < 1.01$` |
| 16 | 4 chains, 4000 iter | Gibbs sampler (`4 chains, 4000 iter`) |
| 38 | 2 | `$K{=}2$` extreme heterogeneity |
| 38 | 5,000 | `$N{=}5{,}000$` |
| 38 | 250 | `$n_{\text{expert}}{=}250$` |
| 38 | 100 | `100 MC runs` |
| 38 | 10, 25, 50, 100, 200, 500, 1000 | `$\kappa \in \{10, 25, 50, 100, 200, 500, 1000\}$` |
| 39 | 1.89 | `$\kappa_{\max} = 1.89$` |
| 39 | 1.45 | mean `1.45` |
| 39 | 1.89 | p99 `1.89` |
| 39 | 53x | `$53{\times}$` safety margin |
| 39 | 100 | `$\kappa{=}100$` threshold |
| 40 | 0.076 | HB: `0.076` |
| 40 | 0.077 | Global: `0.077` |
| 41 | 0.4-0.5 | `$\pi_s \approx 0.4$--$0.5$` |
| 41 | 50 | `$n_{\text{expert}}{=}50$` |
| 41 | 1,125 | maximum condition number reaches `1{,}125` |
| 41 | 100 | `$\kappa{=}100$` guard |
| 42 | 100 | `$\kappa{=}100$` |

**Multiclass Extension (lines 101-138)**
| Line | Number | Context |
|------|--------|---------|
| 111 | 3 | For `$J=3$` |
| 111 | 2 | `$J{=}2$` factor |

**Proof of Proposition (lines 140-171)**
| Line | Number | Context |
|------|--------|---------|
| 156 | 0.5 | `$\pi_s > 0.5$` |
| 160 | 0.15 | `$\bar{\pi} = 0.15$` |
| 160 | 0.088 | `$\pi_s < 0.088$` |
| 170 | 0.66 | AUC `$= 0.66$` |

**Data Generating Process (lines 173-199)**
| Line | Number | Context |
|------|--------|---------|
| 177 | 5000 | `$N = 5000$` observations |
| 178 | 2, 4 | `$K \in \{2, 4\}$` |
| 179 | 0.5 | `$P(Z{=}1) = 0.5$` |
| 180 | 0.5 | `$T \sim \text{Bernoulli}(0.5)$` |
| 186 | 0.5 | `$\bar{\tau} = 0.5$` |
| 187 | 0, 0.2, 0.5, 1.0 | `$\Delta\tau \in \{0, 0.2, 0.5, 1.0\}$` |
| 190 | 0.1, 0.2 | `$\bar{\pi} \in \{0.1, 0.2\}$` |
| 190 | 0, 0.05, 0.1, 0.15 | `$\Delta_c \in \{0, 0.05, 0.1, 0.15\}$` |
| 191 | 0.05, 0.10, 0.15, 0.25 | extreme: `$\pi \in \{0.05, 0.10, 0.15, 0.25\}$` |
| 191 | 0.08, 0.12, 0.16, 0.20 | moderate: `$\pi \in \{0.08, 0.12, 0.16, 0.20\}$` |
| 193 | 50, 100, 250, 500, 1000, 2000 | `$n_{\text{expert}} \in \{50, 100, 250, 500, 1000, 2000\}$` |
| 196 | 5000 | `$N = 5000$` tweets |
| 196 | 57,899 | `$N_{\text{pool}} = 57{,}899$` |
| 197 | 4 | `$K = 4$` subgroups |
| 197 | 38% | `$S_0 \approx 38\%$` |
| 197 | 38% | `$S_1 \approx 38\%$` |
| 197 | 12% | `$S_2 \approx 12\%$` |
| 197 | 12% | `$S_3 \approx 12\%$` |
| 198 | 0.05, 0.10, 0.15, 0.25 | `$\pi_{S_0} = 0.05$`, `$\pi_{S_1} = 0.10$`, `$\pi_{S_2} = 0.15$`, `$\pi_{S_3} = 0.25$` |

**PPCI DGPs (lines 201-207)**
| Line | Number | Context |
|------|--------|---------|
| 202 | 0 | `$\sigma_{\text{outcome}} = 0$` |
| 202 | 0.5 | `$\sigma_{\text{outcome}} = 0.5$` |
| 206 | 48 | `$n_{\text{estimators}} = 48$` |
| 206 | 20 | `$\texttt{min\_samples\_leaf} = 20$` |
| 206 | 3 | `cv=3` |

**Heatmap figure caption (line 212)**
| Line | Number | Context |
|------|--------|---------|
| 212 | 0.12 | correction increases bias when `$\Delta\pi > 0.12$` |
| 212 | 2.86x | reaching `2.86$\times$` |

**Extended Related Work (lines 216-243)**
| Line | Number | Context |
|------|--------|---------|
| 229 | >80% | `$>$80\%` expert budget savings |

**MCMC Convergence (lines 245-274)**
| Line | Number | Context |
|------|--------|---------|
| 249 | 4 chains | `4 chains` with `4000 iterations` |
| 249 | 4000 | `4000` iterations |
| 249 | 2000 | (`2000` warmup) |
| 251 | 3 | fixed Dirichlet prior (`$\alpha{=}3$`) |
| 252 | 1.0034 | `$\hat{R} < 1.0034$` |
| 252 | 1618 | ESS `$> 1618$` |
| 261 | 1.01 | `$< 1.01$` |
| 261 | 1.0034 | `$< 1.0034$` |
| 262 | 845 | `$> 845$` |
| 262 | 1618 | `$> 1618$` |
| 263 | 0 | Divergent transitions `$= 0$` |
| 272 | 0.5x to 2x | factors of `$0.5\times$` to `$2\times$` |
| 272 | <1% | `$<$1\%` RMSE variation for `$K{=}2$` |
| 272 | 4-5% | `$\sim$4--5\%` for `$K{=}4$` |

**ROC Curves (lines 276-288)**
| Line | Number | Context |
|------|--------|---------|
| 282 | 0.89 | AUC `$= 0.89$` (setting-level) |
| 282 | 0.89 | `$|\Delta\pi \times \Delta\tau|$` product (AUC `$= 0.89$`) |
| 282 | 0.97 | `$\mathrm{CV}(\pi_s)$` (AUC `$= 0.97$`) |
| 282 | 0.86 | Subgroup-level: `$\Delta\pi$`-only condition (AUC `$= 0.86$`) |
| 282 | 0.73 | `$|\Delta\pi \times \Delta\tau|$` product (AUC `$= 0.73$`) |

**Budget Crossover (lines 290-345)**
| Line | Number | Context |
|------|--------|---------|
| 294 | 250 | crossover at `$n_{\text{expert}} = 250$` for `$K{=}2$` |
| 294 | 1000 | `$n_{\text{expert}} = 1000$` for `$K{=}4$` |
| 296 | 21 of 24 | `21 of 24` configurations |
| 296 | 1000 | converging by `$n_{\text{expert}} \geq 1000$` |
| 309 | 25, 50, 75, 100, 150, 250 | `$n_{\text{expert}} \in \{25, 50, 75, 100, 150, 250\}$` |
| 309 | 0.3 | `$\Delta\tau{=}0.3$` |
| 309 | 100 | `100 MC runs` |
| 309 | 5,000 | `$N{=}5{,}000$` |
| 323 | 0.101, 0.256, 0.269 | K=2, n=25: Global `0.101`, MLE `0.256`, HB `0.269` |
| 323 | +4.9% | HB vs MLE: `$+4.9\%$` |
| 324 | 0.088, 0.275, 0.231 | K=2, n=50: Global `0.088`, MLE `0.275`, HB `0.231` |
| 324 | -16.1% | `$\mathbf{-16.1\%}$` |
| 325 | 0.084, 0.091, 0.089 | K=2, n=75: `0.084`, `0.091`, `0.089` |
| 325 | -1.9% | `$-1.9\%$` |
| 326 | 0.083, 0.085, 0.084 | K=2, n=100: `0.083`, `0.085`, `0.084` |
| 326 | -0.8% | `$-0.8\%$` |
| 327 | 0.081, 0.077, 0.077 | K=2, n=150: `0.081`, `0.077`, `0.077` |
| 327 | -0.4% | `$-0.4\%$` |
| 328 | 0.080, 0.075, 0.074 | K=2, n=250: `0.080`, `0.075`, `0.074` |
| 328 | -0.1% | `$-0.1\%$` |
| 330 | 0.129, 0.401, 0.612 | K=4, n=25: Global `0.129`, MLE `0.401`, HB `0.612` |
| 330 | +52.5% | `$+52.5\%$` |
| 331 | 0.117, 0.380, 0.470 | K=4, n=50: `0.117`, `0.380`, `0.470` |
| 331 | +23.8% | `$+23.8\%$` |
| 332 | 0.112, 0.221, 0.211 | K=4, n=75: `0.112`, `0.221`, `0.211` |
| 332 | -4.4% | `$\mathbf{-4.4\%}$` |
| 333 | 0.112, 0.215, 0.212 | K=4, n=100: `0.112`, `0.215`, `0.212` |
| 333 | -1.3% | `$-1.3\%$` |
| 334 | 0.109, 0.157, 0.152 | K=4, n=150: `0.109`, `0.157`, `0.152` |
| 334 | -3.6% | `$-3.6\%$` |
| 335 | 0.108, 0.127, 0.126 | K=4, n=250: `0.108`, `0.127`, `0.126` |
| 335 | -1.0% | `$-1.0\%$` |
| 341 | 50 | `$n_{\text{expert}} < 50$` for K=2 |
| 341 | 75 | `$< 75$` for K=4 |
| 342 | 6-12 | `$\sim$6--12` labels per subgroup |
| 343 | 50-250 | `$n_{\text{expert}} = 50$--$250$` |
| 343 | 75-250 | `$75$--$250$` for K=4 |
| 343 | -0.4% to -16.1% | `$-0.4\%$` to `$-16.1\%$` |
| 344 | 250 | `$n_{\text{expert}} \geq 250$` |
| 344 | <1% | `$< 1\%$` |
| 345 | >=0.88 | Coverage remains `$\geq 0.88$` |

**K=8 Subgroups (lines 347-411)**
| Line | Number | Context |
|------|--------|---------|
| 353 | 5,000 | `$N{=}5{,}000$` |
| 353 | 8 | `$K{=}8$` |
| 353 | 250 | `$n_{\text{expert}}{=}250$` |
| 353 | 31 | `${\approx}31$` labels per subgroup |
| 353 | 100 | `100 MC replications` |
| 354 | 0.05, 0.09, 0.13, 0.18, 0.22, 0.26, 0.30, 0.35 | `$\pi_s \in \{0.05, 0.09, 0.13, ..., 0.35\}$` |
| 355 | 0 | `$\tau(Z{=}0){=}0$` |
| 355 | 0.3 | `$\tau(Z{=}1){=}0.3$` |
| 367 | 0.944, 0.113, 0.090 | Oracle: Coverage `0.944`, RMSE `0.113`, Bias `0.090` |
| 368 | 0.951, 0.168, 0.135 | Global: Coverage `0.951`, RMSE `0.168`, Bias `0.135` |
| 369 | 0.956, 0.340, 0.183 | HB EC-HTE: Coverage `0.956`, RMSE `0.340`, Bias `0.183` |
| 370 | 0.953, 0.638, 0.219 | Strat MLE: Coverage `0.953`, RMSE `0.638`, Bias `0.219` |
| 371 | 0.913, 0.133, 0.107 | Naive: Coverage `0.913`, RMSE `0.133`, Bias `0.107` |
| 375 | 95.6% | HB EC-HTE `95.6\%` |
| 375 | 95.3% | Strat MLE `95.3\%` |
| 375 | 95.1% | Global `95.1\%` |
| 376 | 47% | `47\%` RMSE reduction |
| 376 | 0.340 | `0.340` vs `0.638` |
| 376 | 0.638 | `0.638` |
| 377 | 0.340 | HB RMSE (`0.340`) exceeds global (`0.168`) |
| 377 | 0.168 | `0.168` |
| 377 | 31 | `${\approx}31$` expert labels |
| 391-398 | (many) | Per-subgroup table: pi_s values `0.050, 0.093, 0.136, 0.179, 0.221, 0.264, 0.307, 0.350`; RMSE values `0.136, 0.133, 0.154, 0.178, 0.263, 0.421, 0.634, 0.432` (HB); coverages `0.950, 0.970, 0.975, 0.945, 0.940, 0.965, 0.940, 0.960` |
| 403 | 0.87 | correlation `$r = 0.87$` |
| 403 | 0.005 | `$p = 0.005$` |
| 404 | 14-25% | HB RMSE `14--25\%` below global |
| 405 | 24-54% | reduces MLE RMSE by `24--54\%` |
| 406 | >=0.94 | Coverage remains `$\geq$0.94` |
| 409 | 10 | adaptive shrinkage (`$\alpha{=}10$`) vs default `$\alpha{=}3$` |
| 409 | 3 | default `$\alpha{=}3$` |
| 409 | 0.340 | from `0.340` to `0.216` |
| 409 | 0.216 | to `0.216` |
| 409 | 35% | `35\%` improvement |
| 410 | 30% | `30\%` above global |
| 410 | 0.166 | global (`0.166`) |
| 411 | >=94% | coverage `$\geq$94\%` |
| 411 | 500 | `$n_{\text{expert}} \geq 500$` |
| 411 | 60 | `${\approx}60$` labels/subgroup |

**Asymmetric Extension (lines 413-449)**
| Line | Number | Context |
|------|--------|---------|
| 430 | 0.10/0.20, 0.25/0.10 | Cross: FPR/FNR = `0.10/0.20` vs `0.25/0.10` |
| 430 | 0.05/0.15, 0.20/0.30 | Co-directional: `0.05/0.15` vs `0.20/0.30` |
| 430 | 0.03/0.25, 0.30/0.05 | Extreme: `0.03/0.25` vs `0.30/0.05` |
| 431 | 0.991 | `$R^2 = 0.991$` |
| 433 | 0.025 | from `0.025` (global) to `0.006` |
| 433 | 0.006 | to `0.006` |
| 433 | 4x | `$4\times$` improvement |
| 433 | 0.033 | RMSE `0.033` vs `0.040` |
| 433 | 0.040 | `0.040` |
| 433 | 0.90 | coverage `0.90` vs `0.78` |
| 433 | 0.78 | `0.78` |
| 444 | 0.047, 0.053, 0.48 | Naive: Bias `0.047`, RMSE `0.053`, Cov `0.48` |
| 445 | 0.025, 0.040, 0.78 | Global: `0.025`, `0.040`, `0.78` |
| 446 | 0.006, 0.033, 0.90 | HB EC-HTE: `0.006`, `0.033`, `0.90` |

**Supplementary Main Results (lines 451-476)**
| Line | Number | Context |
|------|--------|---------|
| 464 | 0.018, 0.064, 0.95 | Naive: `0.018`, `0.064`, `0.95` |
| 465 | 0.009, 0.074, 0.96 | Global: `0.009`, `0.074`, `0.96` |
| 466 | 0.005, 0.075, 0.97 | Strat MLE: `0.005`, `0.075`, `0.97` |
| 467 | 0.005, 0.075, 0.97 | HB EC-HTE: `0.005`, `0.075`, `0.97` |
| 470 | 0.027, 0.103, 0.93 | Naive (TweetEval): `0.027`, `0.103`, `0.93` |
| 471 | 0.023, 0.124, 0.92 | Global: `0.023`, `0.124`, `0.92` |
| 472 | 0.032, 0.248, 0.91 | Strat MLE: `0.032`, `0.248`, `0.91` |
| 473 | 0.027, 0.225, 0.91 | HB EC-HTE: `0.027`, `0.225`, `0.91` |

**PPCI Results (lines 478-527)**
| Line | Number | Context |
|------|--------|---------|
| 482 | 0.179 | from `0.179` to `0.007` |
| 482 | 0.007 | to `0.007` |
| 482 | 89% | R-learner bias reduction: `89\%` |
| 494-519 | (many) | Full PPCI table with bias/RMSE values per DGP (A-D) -- values include `0.053, 0.063, 0.087, 0.093, 0.063, 0.055, 0.101, 0.102, 0.017, 0.013, 0.097, 0.108, 0.015, 0.020, 0.162, 0.168, 0.189, 0.197, 0.206, 0.212, 0.185, 0.208, 0.204, 0.228, 0.181, 0.215, 0.202, 0.237, 0.171, 0.176, 0.012, 0.023, 0.171, 0.186, 0.251, 0.135, 0.267, 0.155, 0.182, 0.209, 0.233, 0.235, 0.179, 0.216, 0.224, 0.262, 0.017, 0.007, 0.241, 0.232, 0.007, 0.008, 0.209, 0.223, 0.007, 0.003, 0.060, 0.065, 0.010, 0.002, 0.061, 0.071, 0.013, 0.007, 0.062, 0.079` |

**Hate Speech Case Study (lines 528-548)**
| Line | Number | Context |
|------|--------|---------|
| 531 | 2,496 | `2{,}496` comments |
| 532 | 624 | `$n \approx 624$` each |
| 535 | 0.266 to 0.383 | rates range from `0.266` to `0.383` |
| 535 | 0.117 | `$\Delta\pi = 0.117$` |
| 536 | 8.5% | FPR ranges from `8.5\%` to `21.3\%` |
| 536 | 21.3% | to `21.3\%` |
| 540 | 53.3% | baseline FNR (`53.3\%`) |
| 540 | 15.7x | variance amplification factor up to `15.7$\times$` |
| 547 | 50 | `$\kappa > 50$` |

**Cross-Model Consistency (lines 549-579)**
| Line | Number | Context |
|------|--------|---------|
| 552 | 500 | annotating `500` TweetEval sentiment tweets |
| 552 | 6 | six OpenAI models |
| 554 | 0.82 to 1.00 | Spearman `$\rho = 0.82$` to `$1.00$` |
| 555 | 6 | `$n \leq 6$` |
| 556 | 0.05 | `$\Delta\pi > 0.05$` |
| 567 | 0.198 | GPT-3.5-Turbo: `0.198` |
| 568 | 0.149 | GPT-4-Turbo: `0.149` |
| 569 | 0.136 | GPT-4o-mini: `0.136` |
| 570 | 0.114 | GPT-5.4: `0.114` |
| 571 | 0.098 | GPT-4.1: `0.098` |
| 572 | 0.080 | GPT-4o: `0.080` |
| 577 | 5 of 6 | `5 of 6` share the same worst subgroup |
| 578 | 0.114 | GPT-5.4 achieves `$\Delta\pi = 0.114$` |
| 578 | 0.198 | vs GPT-3.5-Turbo's `$0.198$` |

**Open-Source Multi-LLM (lines 581-640)**
| Line | Number | Context |
|------|--------|---------|
| 584 | 7B-9B | `7B--9B` parameter range |
| 584 | 490 | `490` TweetEval tweets |
| 584 | 4 | `$K{=}4$` subgroups |
| 586 | 0.05 | `$\Delta\pi > 0.05$` |
| 598 | 0.755 | Llama-3.1-8B accuracy: `0.755` |
| 598 | 0.141 | `$\Delta\pi$`: `0.141` |
| 599 | 0.798 | Qwen-2.5-7B accuracy: `0.798` |
| 599 | 0.165 | `$\Delta\pi$`: `0.165` |
| 600 | 0.763 | Gemma-2-9B accuracy: `0.763` |
| 600 | 0.125 | `$\Delta\pi$`: `0.125` |
| 601 | 0.802 | Mistral-7B accuracy: `0.802` |
| 601 | 0.134 | `$\Delta\pi$`: `0.134` |
| 609 | 0.714 | from `0.714` (naive average) to `0.939` |
| 609 | 0.939 | to `0.939` |
| 609 | 22.5 | `$+$22.5` percentage points |
| 609 | 1,000 | at `$n_{\text{expert}}{=}1{,}000$` |
| 621 | 0.051 | Llama `$\Delta\pi_{K{=}2}$`: `0.051` |
| 621 | 0.675 | Naive Cov: `0.675` |
| 621 | 0.940 | HB Cov: `0.940` |
| 622 | 0.080 | Qwen: `0.080` |
| 622 | 0.715 | `0.715` |
| 622 | 0.925 | `0.925` |
| 623 | 0.100 | Gemma: `0.100` |
| 623 | 0.705 | `0.705` |
| 623 | 0.945 | `0.945` |
| 624 | 0.070 | Mistral: `0.070` |
| 624 | 0.760 | `0.760` |
| 624 | 0.945 | `0.945` |
| 632 | 0.437 | FNR `$= 0.437$` |
| 633 | 100 | `$n{=}100$` |
| 633 | 1.229 | RMSE reaches `1.229` |
| 633 | 3.1x | (`$3.1\times$` naive) |
| 633 | 25 | below `25` |
| 634 | 500 | `$n \geq 500$` |
| 634 | >0.90 | `$>$0.90` |
| 637 | 0.1, 0.6 | `$\Delta\tau \in [0.1, 0.6]$` |
| 637 | 2 | `$K{=}2$` |
| 637 | 50 | `50 MC runs` |
| 638 | 0.010 | `0.010` vs `0.031` |
| 638 | 0.031 | `0.031` |
| 638 | 68% | `68\%` reduction |
| 639 | 0.6 | `$\Delta\tau{=}0.6$` |
| 639 | 0.212 | `0.212` vs `0.258` |
| 639 | 0.258 | `0.258` |
| 639 | 18% | `18\%` improvement |

**Subgroup Misspecification (lines 642-674)**
| Line | Number | Context |
|------|--------|---------|
| 646 | 0, 0.10, 0.25, 0.50 | `$p_{\text{flip}} \in \{0, 0.10, 0.25, 0.50\}$` |
| 646 | 500 | `$n_{\text{expert}} = 500$` |
| 646 | 0.3 | `$\Delta\tau = 0.3$` |
| 646 | 100 | `100 MC runs` |
| 660-668 | (many) | Coverage values: Naive `0.875, 0.877, 0.890, 0.897`; Global `0.925, 0.935, 0.932, 0.945`; HB `0.958, 0.948, 0.950, 0.945` (K=2); Naive `0.904, 0.916, 0.909, 0.919`; Global `0.930, 0.953, 0.948, 0.944`; HB `0.956, 0.958, 0.960, 0.946` (K=4) |
| 672 | >=0.945 | EC-HTE maintains coverage `$\geq 0.945$` |
| 672 | 0.875-0.919 | naive: `0.875--0.919` |
| 673 | 0.50 | `$p_{\text{flip}} = 0.50$` |
| 673 | 0.1% | within `0.1\%` |
| 674 | 0.01 | `$p < 0.01$` |

**MC Standard Errors (lines 676-720)**
| Line | Number | Context |
|------|--------|---------|
| 679 | 100 | `100` MC replications |
| 679 | 50 | `50` replications for intensive analyses |
| 679 | 20 | `20` for bootstrap experiments |
| 680 | 3.2% | variation below `3.2\%` |
| 686 | 1,020 | Of `1{,}020` total pairwise comparisons |
| 686 | 742 | `742` (`72.7\%`) are statistically significant |
| 686 | 72.7% | `72.7\%` |
| 686 | 0.05 | `$\alpha = 0.05$` |
| 698 | -0.046 | `$-0.046$` |
| 698 | <0.001 | `$\mathbf{<0.001}$` |
| 699 | -0.078 | `$-0.078$` |
| 699 | <0.001 | `$\mathbf{<0.001}$` |
| 700 | -0.017 | `$-0.017$` |
| 700 | 0.288 | `$0.288$` |
| 701 | +0.001 | `$+0.001$` |
| 701 | 0.395 | `$0.395$` |
| 704 | +0.015 | `$+0.015$` |
| 704 | 0.179 | `$0.179$` |
| 705 | +0.048 | `$+0.048$` |
| 705 | 0.011 | `$\mathbf{0.011}$` |
| 708 | -0.089 | `$-0.089$` |
| 708 | <0.001 | `$\mathbf{<0.001}$` |
| 709 | -0.113 | `$-0.113$` |
| 709 | <0.001 | `$\mathbf{<0.001}$` |
| 710 | -0.031 | `$-0.031$` |
| 710 | 0.038 | `$\mathbf{0.038}$` |
| 711 | +0.005 | `$+0.005$` |
| 711 | 0.030 | `$\mathbf{0.030}$` |

**Semi-Real CM Validation (lines 722-798)**
| Line | Number | Context |
|------|--------|---------|
| 727 | 5,000 | `$N{=}5{,}000$` |
| 727 | 0.18 | `$P(Z{=}1){=}0.18$` |
| 727 | 100 | `100 MC seeds` |
| 732 | 0.526 | FNR `$= 0.526$` |
| 739 | 0.38 | S0 Weight: `0.38` |
| 739 | 0.054 | FPR: `0.054` |
| 739 | 0.526 | FNR: `0.526` |
| 740 | 0.22 | S1 Weight: `0.22` |
| 740 | 0.101 | FPR: `0.101` |
| 740 | 0.300 | FNR: `0.300` |
| 741 | 0.14 | S2 Weight: `0.14` |
| 741 | 0.143 | FPR: `0.143` |
| 741 | 0.308 | FNR: `0.308` |
| 742 | 0.25 | S3 Weight: `0.25` |
| 742 | 0.194 | FPR: `0.194` |
| 742 | 0.222 | FNR: `0.222` |
| 757-773 | (many) | Semi-real RMSE/Coverage: Oracle `0.101, 0.957`; Naive `0.123, 0.879`; Global `0.263/0.232/0.196, 0.885/0.909/0.922`; HB `0.784/0.411/0.260, 0.744/0.834/0.890` at n=100/250/500 |
| 779 | 53.3% | FNR `$= 53.3$\%` |
| 781 | 0.495, 0.505 | `$\pi \in (0.495, 0.505)$` |
| 781 | 0.5% | within `0.5\%` of random guessing |
| 782 | 500 | `$n_{\text{expert}} = 500$` |
| 782 | 0.260 | RMSE `0.260` vs `0.196` |
| 782 | 0.196 | `0.196` |
| 784 | 0.39 | worst-subgroup FPR `$= 0.39$` |
| 784 | 0.21 | FNR `$= 0.21$` |
| 784 | 1.3-3.5x | HB RMSE exceeds global by `1.3--3.5$\times$` |
| 785 | 0.18 | `$P(Z{=}1) = 0.18$` |
| 786 | 25 | `$\geq 25$` |
| 786 | 0.5 | `$< 0.5$` |
| 789 | 1.25 | `$\kappa(\hat{M}_s) \leq 1.25$` |
| 789 | 25 | `$\geq 25$` |
| 789 | 368 | `368` semi-real experiment-budget cells |
| 790 | 93.3% | HB outperforms global in `93.3\%` of cells |
| 790 | 94.7% | global preferred in `94.7\%` of cells |
| 791 | 2.38 | `$\kappa = 2.38$` |
| 791 | 2.5 | effective `$n = 2.5$` |
| 791 | 1.55 | `$\kappa = 1.55$` |
| 791 | 100% | correctly predicts `100\%` |

**Civil Comments (lines 906-938)**
| Line | Number | Context |
|------|--------|---------|
| 909 | 3,000 | `$N{=}3{,}000$` stratified samples |
| 909 | 30% | (`30\%` toxic) |
| 910 | 38.8% | S0: `38.8\%` |
| 910 | 11.4% | S1: `11.4\%` |
| 910 | 33.7% | S2: `33.7\%` |
| 910 | 16.1% | S3: `16.1\%` |
| 912 | 800-900 | `800--900` valid annotations per model |
| 916 | 0.05 | `$\Delta\pi > 0.05$` |
| 916 | 0.113, 0.160 | `$\Delta\pi \in [0.113, 0.160]$` |
| 916 | 0.125, 0.165 | `$\Delta\pi \in [0.125, 0.165]$` |
| 917 | 0.42, 0.61 | FPR `$\in [0.42, 0.61]$` |
| 917 | 0.05, 0.16 | FNR `$\in [0.05, 0.16]$` |
| 929-937 | (many) | FPR/FNR per model: GPT-4o FPR `0.249, 0.157, 0.213, 0.341` (delta `0.184`); FNR `0.160, 0.263, 0.308, 0.328` (delta `0.168`); GPT-4o-mini FPR `0.517, 0.541, 0.419, 0.610` (delta `0.191`); FNR `0.052, 0.105, 0.074, 0.160` (delta `0.108`); GPT-3.5-turbo FPR `0.400, 0.473, 0.374, 0.468` (delta `0.099`); FNR `0.139, 0.211, 0.173, 0.240` (delta `0.101`) |

**Real CM Bias Validation (lines 941-976)**
| Line | Number | Context |
|------|--------|---------|
| 945 | 5,000 | `$N{=}5{,}000$` |
| 945 | 4 | `$K{=}4$` |
| 945 | 0.30 | `$\Delta\tau{=}0.30$` |
| 945 | 100 | `100 MC runs` |
| 945 | 11 | `11` LLM-dataset combinations |
| 945 | 8 | `eight` models on TweetEval |
| 945 | 3 | `three` on Civil Comments |
| 948 | 0.975 | aggregate `$R^2 = 0.975$` |
| 948 | 10 of 11 | `10 of 11` achieve `$R^2 \geq 0.93$` |
| 948 | 0.93 | `$R^2 \geq 0.93$` |
| 949 | 0.76 | `$R^2{=}0.76$` |
| 949 | 0.089 | `$\max|[B_s]_{z,1}| = 0.089$` |
| 961-973 | (many) | Per-model R-squared: `0.993, 0.990, 0.990, 0.982, 0.979, 0.975, 0.969, 0.948, 0.935, 0.929, 0.756, 0.975` with max|B| values `0.328, 0.272, 0.242, 0.185, 0.198, 0.240, 0.139, 0.087, 0.170, 0.170, 0.089` |

**Screening and Kappa Analysis (lines 978-1083)**
| Line | Number | Context |
|------|--------|---------|
| 981 | 16 | `16` LLM-dataset-K combinations |
| 981 | 7 | `seven` LLMs |
| 986 | 500 | `$n_{\text{expert}}{=}500$` |
| 1013 | 1.25 | `$\kappa(C_s) \leq 1.25$` |
| 1013 | 0.20 | `$\lesssim 0.20$` |
| 1014 | 1.23 | `$\kappa{=}1.23$` |
| 1014 | 1.27 | `$\kappa{=}1.27$` |
| 1016 | 0.4 | `$\geq 0.4$` |
| 1016 | 5,000 | `$N{=}5{,}000$` |
| 1016 | 0.3 | `$\Delta\tau{=}0.3$` |
| 1016 | 100 | `100 MC runs` |
| 1016 | 250, 500 | `$n_{\text{expert}} \in \{250, 500\}$` |
| 1017 | 41 of 52 | `41 of 52` comparisons (`79\%`) |
| 1017 | 79% | `79\%` |
| 1017 | 52 of 52 | `52 of 52` (`100\%`) |
| 1017 | 100% | `100\%` |
| 1018 | 32/32 | `32/32` comparisons |
| 1018 | 0.001-0.008 | RMSE reduction `0.001--0.008` |
| 1018 | 0.39 | `$\mathrm{FPR}_{\max}{=}0.39$` |
| 1018 | 0.3 | `$P(Z{=}1){=}0.3$` |
| 1022 | 0.63 | pooled AUC `$= 0.63$` |
| 1025 | 0.75 | AUC `$\geq 0.75$` |
| 1025 | 0.75-1.0 | AUC range: `0.75--1.0` |
| 1026 | 0.0-0.67 | AUC `0.0--0.67` |
| 1026 | 7 | remaining `7` combinations |
| 1026 | 4 of 7 | `4 of 7` have AUC `$< 0.5$` |
| 1027 | 16 | all `16` real combinations |
| 1038 | 520 | `520` synthetic configurations |
| 1038 | 0.025, 0.275 | `$\pi_s \in [0.025, 0.275]$` |
| 1038 | 1.43, 2.22 | `$\kappa$ falls in $[1.43, 2.22]$` |
| 1038 | 1.25 | none reaches `$\kappa \leq 1.25$` |
| 1038 | 0.15 | `$\bar{\pi}{=}0.15$` |
| 1038 | 1.43 | `$\kappa{=}1/(1{-}2 \cdot 0.15){=}1.43$` |
| 1040 | 86% | `86\%` bias reduction |
| 1040 | 10% | `10\%` lower RMSE |
| 1040 | 95.5% | `95.5\%` coverage |
| 1040 | 88.3% | vs `88.3\%` for Global |
| 1040 | 2.0 | at `$\kappa{=}2.0$` |
| 1051 | 420 | `420` configs at `$\leq 2.0$` |
| 1051 | 35.0% | Debiasing hurts: `35.0\%` |
| 1051 | 0.152 | Global ratio: `0.152` |
| 1052 | 100 | `100` configs at `$> 2.0$` |
| 1052 | 100% | `100\%` |
| 1052 | 0.326 | Global ratio: `0.326` |
| 1058 | 13 | all `13` real combinations |
| 1058 | 1.88, 2.99 | `$\kappa \in [1.88, 2.99]$` |
| 1058 | 1.25 | none reaches `$\kappa \leq 1.25$` |
| 1058 | 0.20 | `$< 0.20$` |
| 1060 | >=93% | coverage `($\geq$93\%)` |
| 1060 | 250 | at `$n_{\text{expert}} \geq 250$` |
| 1060 | 86-91% | `86--91\%` for Global |
| 1061 | 500 | `$n_{\text{expert}}{=}500$` |
| 1061 | 1.01 | ratio `1.01` |
| 1061 | 75% | bias win rate of `75\%` |
| 1061 | 250 | `$n_{\text{expert}}{=}250$` |
| 1073 | 0.99, 1.01, 75%, 0.943 | kappa<=2, n=500: Bias ratio `0.99`, RMSE ratio `1.01`, win `75\%`, Cov `0.943` |
| 1074 | 1.09, 1.13, 0%, 0.932 | kappa<=2, n=250: `1.09`, `1.13`, `0\%`, `0.932` |
| 1077 | 1.11, 1.22, 22%, 0.949 | kappa>2, n=500: `1.11`, `1.22`, `22\%`, `0.949` |
| 1078 | 1.26, 1.43, 0%, 0.940 | kappa>2, n=250: `1.26`, `1.43`, `0\%`, `0.940` |
| 1083 | 100 | `$\kappa > 100$` |
| 1083 | 1.25 | `$\kappa \leq 1.25$` |
| 1083 | 1.25, 3 | `$\kappa \in (1.25, {\sim}3]$` |
| 1083 | >=93% | `$\geq$93\%` |
| 1083 | 500 | `$n_{\text{expert}} \geq 500$` |

**Bootstrap SE Validation (lines 1085-1155)**
| Line | Number | Context |
|------|--------|---------|
| 1089 | 50, 100, 250, 500 | `$n_{\text{expert}} \in \{50, 100, 250, 500\}$` |
| 1089 | 50 | `50` replications |
| 1091 | >=0.96 | coverage `$\geq 0.96$` |
| 1091 | 0.970, 0.960, 0.970, 0.970 | (`0.970, 0.960, 0.970, 0.970`) |
| 1095 | 0.05, 0.25 | `$\pi{=}[0.05, 0.25]$` |
| 1095 | 250 | `$n_{\text{expert}}{=}250$` |
| 1095 | 200 | `$n_{\text{estimators}}{=}200$` |
| 1095 | 20 | `20 MC runs` |
| 1095 | 93.8% | `93.8\%` aggregate coverage |
| 1095 | 94-96% | `94--96\%` oracle coverage |
| 1096 | 92.5% | (`92.5\%`) for high-error subgroup |
| 1096 | 95.0% | (`95.0\%`) for low-error subgroup |
| 1097 | >=95% | `$\geq$95\%` coverage |
| 1100 | 100 | `$B{=}100$` |
| 1100 | 200 | `$n_{\text{estimators}}{=}200$` |
| 1100 | 20 | `20 MC runs` |
| 1101 | 93.8% | `93.8\%` |
| 1101 | 95.0% | `95.0\%` |
| 1101 | 1.2pp | `$+$1.2pp` |
| 1106 | 1.15x | `${\sim}1.15\times$` plug-in |
| 1113 | 0.950, 0.925, 0.925, 0.059, 0.063 | s0 values |
| 1114 | 0.925, 0.975, 0.875, 0.087, 0.103 | s1 values |
| 1116 | 0.938, 0.950, 0.900, 0.073, 0.083 | Aggregate values |
| 1121 | 92.5% to 97.5% | from `92.5\%` to `97.5\%` |
| 1121 | 5.0pp | `$+$5.0pp` |
| 1122 | 90.0% | Oracle coverage (`90.0\%`) |
| 1122 | 94% | `94\%` |
| 1126 | 25, 50, 75, 100, 200 | `$n_{\text{expert}} \in \{25, 50, 75, 100, 200\}$` |
| 1126 | 100 | `$B{=}100$` |
| 1126 | 20 | `20 MC runs` |
| 1127 | >=95% | `$\geq$95\%` coverage |
| 1127 | 25 | `$n_{\text{expert}}{=}25$` |
| 1127 | 12 | `${\approx}12$` labels per subgroup |
| 1128 | >=91.2% | `$\geq$91.2\%` |
| 1139 | 0.925, 1.000, 2.86, 0.079 | n=25 values |
| 1140 | 0.975, 0.988, 2.93, 0.067 | n=50 values |
| 1141 | 0.912, 0.975, 2.59, 0.065 | n=75 values |
| 1142 | 0.963, 0.963, 1.52, 0.060 | n=100 values |
| 1143 | 0.963, 0.950, 1.17, 0.061 | n=200 values |
| 1148 | 2-3x | `$2{-}3\times$` |
| 1149 | 1.2-1.5x | `${\sim}1.2{-}1.5\times$` |
| 1149 | >=96% | `$\geq$96\%` |
| 1150 | >=50 | `$n_{\text{expert}} \geq 50$` |
| 1150 | 98.8% | (`98.8\%`) |
| 1150 | 2.9x | (`2.9$\times$`) |
| 1150 | 97.5% | `97.5\%` |

**CF Oracle Decomposition (lines 1157-1202)**
| Line | Number | Context |
|------|--------|---------|
| 1161 | 100 | `100 MC runs` |
| 1173-1194 | (many) | Oracle/EC-HTE/Global/Naive coverage/bias/RMSE across 3 DGPs (see table above, all values already catalogued) |
| 1201 | 0-5pp | `0--5pp` gap from oracle |
| 1202 | <=1.5pp | `${\leq}$1.5pp` |
| 1202 | <1pp | `$<$1pp` |
| 1202 | 250 | `$n_{\text{expert}} \geq 250$` |

**A5 Violation (lines 1204-1249)**
| Line | Number | Context |
|------|--------|---------|
| 1217 | 5,000 | `$N{=}5{,}000$` |
| 1217 | 250 | `$n_{\text{expert}}{=}250$` |
| 1217 | 50 | `50 MC` |
| 1217 | 0.05, 0.25 | `$\pi = [0.05, 0.25]$` |
| 1218 | 0.30, 0.70 | `$\Delta\tau = [0.30, 0.70]$` |
| 1219 | 0.70, 0.30 | `$\Delta\tau = [0.70, 0.30]$` |
| 1231-1240 | (many) | Coverage/bias: Aligned Oracle `0.94, 0.98, 0.003, 0.003`; Naive `0.93, 0.25, 0.022, 0.174`; Global `0.93, 0.82, 0.036, 0.094`; EC-HTE `0.95, 0.95, 0.005, 0.017`; Adversarial Oracle `0.94, 0.98, 0.003, 0.003`; Naive `0.90, 0.78, 0.042, 0.074`; Global `0.74, 0.93, 0.098, 0.040`; EC-HTE `0.94, 0.96, 0.002, 0.007` |
| 1245 | 0.25 | S1 coverage collapses to `0.25` |
| 1247 | 0.74 | S0 coverage `0.74` |
| 1248 | >=0.94 | `$\geq 0.94$` coverage |
| 1249 | 500 | `$n_{\text{expert}}{=}500$` |
| 1249 | 0.93, 0.99 | `$[0.93, 0.99]$` |

**A1 Sensitivity (lines 1251-1280)**
| Line | Number | Context |
|------|--------|---------|
| 1255 | 0, 0.05, 0.10, 0.15, 0.20 | `$\gamma \in \{0, 0.05, 0.10, 0.15, 0.20\}$` |
| 1269 | 95.5, 92.7, 87.7, 0.060, 0.065, 0.061 | gamma=0 values |
| 1270 | 95.5, 93.5, 83.8, 0.059, 0.064, 0.064 | gamma=0.05 values |
| 1271 | 95.3, 93.8, 83.5, 0.063, 0.064, 0.067 | gamma=0.10 values |
| 1272 | 94.8, 94.3, 79.2, 0.065, 0.064, 0.070 | gamma=0.15 values |
| 1273 | 93.5, 94.0, 79.5, 0.068, 0.063, 0.073 | gamma=0.20 values |
| 1278 | >=93.5% | `$\geq$93.5\%` |
| 1278 | 13.7% | `13.7\%` |
| 1279 | >=90% | `$\geq$90\%` |
| 1280 | -8.2pp | `$-$8.2pp` |

**Treatment-Dependent Misclass (lines 1282-1317)**
| Line | Number | Context |
|------|--------|---------|
| 1285 | 0, 0.05, 0.10, 0.15, 0.20 | `$\gamma_T \in \{0, 0.05, 0.10, 0.15, 0.20\}$` |
| 1298 | 0.945, 0.075 | gamma_T=0: Cov `0.945`, RMSE `0.075` |
| 1299 | 0.897, 0.092 | gamma_T=0.05: `0.897`, `0.092` |
| 1300 | 0.750, 0.133 | gamma_T=0.10: `0.750`, `0.133` |
| 1301 | 0.525, 0.177 | gamma_T=0.15: `0.525`, `0.177` |
| 1302 | 0.370, 0.224 | gamma_T=0.20: `0.370`, `0.224` |
| 1307 | >=89.7% | `$\geq$89.7\%` |
| 1308 | 75.0% | coverage drops to `75.0\%` |
| 1315 | 90% | `90\%` coverage threshold |
| 1315 | ~0.10 | breakeven at `$\gamma_T \approx 0.10$` |

**Confounded Treatment (lines 1319-1382)**
| Line | Number | Context |
|------|--------|---------|
| 1326 | 5,000 | `$N{=}5{,}000$` |
| 1326 | 0.05, 0.25 | `$\pi = [0.05, 0.25]$` |
| 1326 | 250 | `$n_{\text{expert}}{=}250$` |
| 1326 | 100 | `100 MC` |
| 1328 | 0.5 | `$\beta{=}0.5$` |
| 1328 | 0.38, 0.62 | propensity range `$[0.38, 0.62]$` |
| 1329 | 1, 0.5, 0.3 | `$Y = 1 + 0.5 Z + 0.3 X$` |
| 1330 | 0, 0.3 | `$\tau(Z{=}0){=}0$`, `$\tau(Z{=}1){=}0.3$` |
| 1331 | 0.05, 0.95 | propensity clipped to `$[0.05, 0.95]$` |
| 1342-1347 | (many) | Oracle `0.943, 0.061, 0.048`; HB `0.950, 0.086, 0.068`; Global `0.930, 0.087, 0.071`; Strat MLE `0.950, 0.087, 0.069`; Naive `0.863, 0.083, 0.066` |
| 1351 | 0.7pp | within `0.7pp` |
| 1352 | 96.0% | EC-HTE coverage `96.0\%` |
| 1352 | 78.5% | naive `78.5\%` |
| 1352 | +17.5pp | `$+$17.5pp` |
| 1353 | 93.0% | Global coverage (`93.0\%`) |
| 1353 | 95.0% | correction methods (`95.0\%`) |
| 1356 | 0.25, 0.5, 1.0, 2.0 | `$\beta \in \{0.25, 0.5, 1.0, 2.0\}$` |
| 1356 | 8 | `8` configurations |
| 1356 | 100 | `100 MC` each |
| 1368-1375 | (many) | Coverage table: HB `0.963, 0.973, 0.950, 0.958, 0.958, 0.960, 0.945, 0.948`; Naive `0.848, 0.845, 0.863, 0.858, 0.898, 0.883, 0.858, 0.858` |
| 1380 | >=94.5% | `$\geq$94.5\%` |
| 1380 | 2.0 | `$\beta{=}2.0$` |
| 1380 | 0.12, 0.88 | propensity range `$[0.12, 0.88]$` |
| 1381 | <=1pp | `$\leq$1pp` |

**F-L Comparison (lines 1384-1414)**
| Line | Number | Context |
|------|--------|---------|
| 1390 | 0.05, 0.25 | `$\pi{=}[0.05, 0.25]$` |
| 1390 | 0, 0.3 | `$\tau(z{=}0){=}0$`, `$\tau(z{=}1){=}0.3$` |
| 1390 | 100 | `100 MC runs` |
| 1401 | 0.045, 0.056, 0.943 | Oracle values |
| 1402 | 0.062, 0.077, 0.858 | Naive values |
| 1403 | 0.064, 0.081, 0.938 | Global values |
| 1404 | 0.064, 0.086, 0.953 | HB EC-HTE values |
| 1405 | 0.091, 0.116, 0.850 | F-L Scalar values |
| 1406 | 0.112, 0.158, 0.838 | F-L Per-Subgroup values |
| 1411 | 0.112, 0.062 | F-L per-subgroup `0.112` vs naive `0.062` |
| 1412 | +0.073 | S0 mean bias `$+0.073$` |
| 1412 | +0.005 | naive `$+0.005$` |
| 1412 | 14.6x | `$14.6\times$` amplification |
| 1412 | +0.160 | S1 mean bias `$+0.160$` |
| 1413 | +0.006, +0.001 | EC-HTE: S0 `$+0.006$`, S1 `$+0.001$` |
| 1413 | 95.3% | coverage (`95.3\%`) |

**Asymmetric End-to-End (lines 1416-1444)**
| Line | Number | Context |
|------|--------|---------|
| 1419 | 7:1 | FPR/FNR ratio up to `$7{:}1$` |
| 1420 | 0.05, 0.02 | s0: FPR `$0.05$`, FNR `$0.02$` |
| 1420 | 0.38, 0.054 | s1: FPR `$0.38$`, FNR `$0.054$` |
| 1420 | 100 | `100 MC runs` |
| 1425 | +1.5pp | `$+1.5$pp` |
| 1425 | 11.5% | `11.5\%` |
| 1432-1438 | (many) | Oracle `0.045, 0.056, 0.943`; EC-HTE asym `0.057, 0.074, 0.945`; Naive `0.059, 0.073, 0.870`; Global asym `0.061, 0.076, 0.915`; EC-HTE sym `0.062, 0.083, 0.930`; Global sym `0.063, 0.078, 0.915` |
| 1442 | 94.5% | `94.5\%` vs `93.0\%` |
| 1442 | 93.0% | `93.0\%` |
| 1442 | 0.083 | from `0.083` to `0.074` |
| 1442 | 0.074 | to `0.074` |
| 1442 | -11.5% | `$-11.5\%$` |
| 1443 | 93.0%, 91.0% | asym `93.0\%` vs sym `91.0\%` |

**Calibration (lines 1446-1475)**
| Line | Number | Context |
|------|--------|---------|
| 1450 | 0.05, 0.25 | from `$\pi{=}[0.05, 0.25]$` |
| 1450 | 0.20 | `$\Delta\pi{=}0.20$` |
| 1450 | 0.08, 0.15 | to `$\pi{=}[0.08, 0.15]$` |
| 1450 | 0.07 | `$\Delta\pi{=}0.07$` |
| 1462-1468 | (many) | Calibration table: Oracle `0.043, 0.053, 0.963`; Cal+EC-HTE `0.055, 0.069, 0.965`; Cal+Global `0.055, 0.068, 0.963`; Cal+Naive `0.051, 0.064, 0.913`; Uncal+EC-HTE `0.064, 0.084, 0.938`; Uncal+Global `0.069, 0.085, 0.920`; Uncal+Naive `0.063, 0.079, 0.840` |
| 1473 | 84.0% | from `84.0\%` to `91.3\%` |
| 1473 | 91.3% | to `91.3\%` |
| 1473 | 95% | nominal `95\%` |
| 1474 | 96.5% | (`96.5\%`) |

**Policy Reversal Zone (lines 1477-1515)**
| Line | Number | Context |
|------|--------|---------|
| 1481 | 0.01, 0.02, 0.03, 0.05, 0.07, 0.10 | `$\tau(0) \in \{0.01, 0.02, ..., 0.10\}$` |
| 1481 | 0.30 | `$\Delta\tau{=}0.30$` |
| 1493 | 0.01, 31.0%, -0.079 | tau=0.01: `31.0\%`, most extreme `$-0.079$` |
| 1494 | 0.02, 21.6% | tau=0.02: `21.6\%` |
| 1495 | 0.03, 14.9%, -0.059 | tau=0.03: `14.9\%`, `$-0.059$` |
| 1496 | 0.05, 6.1%, -0.039 | tau=0.05: `6.1\%`, `$-0.039$` |
| 1497 | 0.07, 1.6% | tau=0.07: `1.6\%` |
| 1498 | >=0.10, 0% | tau>=0.10: `0\%` |
| 1503 | 31% | `31\%` of configurations |
| 1503 | -0.079 | `$\hat{\tau} = -0.079$` |
| 1503 | +0.01 | true `$\tau = +0.01$` |
| 1504 | 0.089 | `$\tau(0) < 0.089$` |
| 1504 | 0.125 | `$0.125$` |
| 1504 | 0.50 | `$0.50$` |
| 1504 | 0.70 | `$0.70$` |
| 1504 | 0.089 | `$= 0.089$` |
| 1505 | 0.01 | `$\tau(0) = 0.01$` |
| 1505 | 0.19 | `$\delta_{\text{misclass}} = 0.19$` |
| 1505 | 42.9% | `42.9\%` reversal rate |

---

**Summary of key recurring numbers across the paper:**

- **14.9%** -- sign reversal rate at tau(0)=0.03 (appears in abstract, introduction, experiments, conclusion, appendix)
- **R^2 = 0.994** -- bias identity fit for K=2 (theory, experiments)
- **R^2 = 0.975** -- aggregate fit across 11 real LLM CMs (introduction, experiments, related work, appendix)
- **7.4x** -- bias reduction by EC-HTE at K=2 extreme (abstract, experiments)
- **AUC = 1.0** -- diagnostic on subgroups with nonzero effect heterogeneity (abstract, introduction, method, conclusion)
- **8 real LLMs** -- all amplify bias under global correction (abstract, introduction, experiments, conclusion)
- **0.008** -- EC-HTE best |bias| at K=2 extreme (introduction, experiments)
- **5x** -- cross-demographic error rate variation (abstract, introduction, related work)
- **>=93%** or **>=93.5%** -- EC-HTE coverage under various robustness tests (method, theory, experiments, limitations, appendix)
- **520 configs** -- size of K=2 synthetic grid (theory, experiments, appendix)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7fdcdcb-9f3b-456e-be24-b68d046ac73e",
  "isSidechain": true,
  "agentId": "a02c88d2dafcf0406",
  "requestId": "req_011CbL3cMX493ZWUFnsXnRSK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7312427-12c5-4f8e-a894-0d0c380ea307",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "d2276042-6def-465e-a6b6-36a2614bccb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1wrkt6bLSZpfoXycNJwLR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3446,
      "cache_read_input_tokens": 68217,
      "output_tokens": 26223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3446
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 26223,
          "cache_read_input_tokens": 68217,
          "cache_creation_input_tokens": 3446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3446,
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
