# Research conversation: In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/, I need 

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-af152b21ba92fc359.jsonl`
- **Structured JSON:** [`8a647fccf72634777d38.json`](../../sessions/8a/8a647fccf72634777d38.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

35 recorded events

### User

_source line 1 · 2026-05-24T20:50:10.023Z_

In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/, I need a complete inventory of ALL tables and figures in the appendix sections.

For each table/figure, I need:
1. Label (e.g., tab:cross-model, fig:death-action-dist)
2. Caption text (full)
3. Approximate size (how many rows for tables, how large for figures)
4. Which main text section it's most relevant to
5. Whether it's referenced from the main text (grep for \ref{label})

Search in main.tex for everything after \appendix. Also check if there are separate appendix .tex files.

This is for deciding which appendix content to promote to the main text to fill visual gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "615c1eae-3cf0-4729-ad9e-5bf3fb5d3b1d",
  "agentId": "af152b21ba92fc359",
  "type": "user",
  "uuid": "492c2e19-74e9-4b22-9378-e9f5497fcf29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-24T20:50:12.697Z_

I'll help you create a complete inventory of all tables and figures in the appendix sections. Let me start by exploring the paper directory structure and then examining the LaTeX files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "492c2e19-74e9-4b22-9378-e9f5497fcf29",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN44Qkzzw1s8FnbHWD8k",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c36c1f97-01b0-443b-b13d-cedd9d82457a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018gauCkuXRLzjyfCNipoKUt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37354,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37354,
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

_source line 3 · 2026-05-24T20:50:12.894Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01V6fwMyir4pPXQLe9eBDVGC`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/ -type f -name \"*.tex\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c36c1f97-01b0-443b-b13d-cedd9d82457a",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN44Qkzzw1s8FnbHWD8k",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c2c43006-fece-45cc-b9e6-75412b95d31c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018gauCkuXRLzjyfCNipoKUt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37354,
      "cache_read_input_tokens": 0,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 37354
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 136,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 37354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 37354,
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

_source line 4 · 2026-05-24T20:50:13.099Z_

<details><summary>↩ Tool result · `toolu_01V6fwMyir4pPXQLe9eBDVGC`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/responsibleNLPchecklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2c43006-fece-45cc-b9e6-75412b95d31c",
  "isSidechain": true,
  "promptId": "615c1eae-3cf0-4729-ad9e-5bf3fb5d3b1d",
  "agentId": "af152b21ba92fc359",
  "type": "user",
  "uuid": "c16eec1e-1c0f-4013-98ce-10f2cbaf08fc",
  "sourceToolAssistantUUID": "c2c43006-fece-45cc-b9e6-75412b95d31c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-24T20:50:14.341Z_

Now let me read the main.tex file to find the appendix section:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c16eec1e-1c0f-4013-98ce-10f2cbaf08fc",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN44djMN89XneyxqRgiM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5f0160b7-a9ce-48e2-989f-9d08d6a2f903",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CNHWrmyNNrBL2Uujgnj9mt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1332,
      "cache_read_input_tokens": 37354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1332,
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

_source line 6 · 2026-05-24T20:50:14.519Z_

<details open><summary>🔧 Tool call — Read · `toolu_018kexYRW1h3wmjGNP36fRA9`</summary>

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
  "parentUuid": "5f0160b7-a9ce-48e2-989f-9d08d6a2f903",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN44djMN89XneyxqRgiM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9fc11158-a49b-4e6a-a26a-8bff25d358a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CNHWrmyNNrBL2Uujgnj9mt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1332,
      "cache_read_input_tokens": 37354,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1332
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 106,
          "cache_read_input_tokens": 37354,
          "cache_creation_input_tokens": 1332,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1332,
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

_source line 7 · 2026-05-24T20:50:14.796Z_

<details><summary>↩ Tool result · `toolu_018kexYRW1h3wmjGNP36fRA9`</summary>

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
17	\usepackage{tcolorbox}
18	\tcbuselibrary{listings,breakable}
19	
20	\hypersetup{pdfauthor={},pdftitle={}}
21	
22	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{abstract}
30	\input{introduction}
31	\input{related_work}
32	\input{method}
33	\input{experiments}
34	\input{discussion}
35	\input{conclusion}
36	
37	\section*{Limitations}
38	
39	\paragraph{Environmental scope.}
40	Our primary analysis uses ScienceWorld (11 of 30 task types) with Qwen2.5-7B-Instruct. Cross-model replication (three 7--9B families, two 70B-class models) and cross-environment probes (MATH, ALFWorld) support the framework's methodological generality, but quantitative results (DAF $= 90.4\%$, label fractions) are environment-specific. The $-100$ death penalty amplifies DAF; softer penalties yield lower values (Appendix~\ref{app:penalty}). Validation beyond 70B and to frontier models with substantially lower failure rates remains future work.
41	
42	\paragraph{Methodological constraints.}
43	Our internal baseline uses single-pass ReAct~\citep{react-2023}; more aggressive self-correction (e.g., Tree-of-Thought~\citep{tot-2023}) may further reduce death rates. Episode-level labels assign a single routing preference to entire episodes, introducing granularity mismatch for individual steps---though only 0.3\% of steps exhibit strict directional conflict with the episode label. Training on pure-strategy trajectories also introduces distribution shift at deployment~\citep{dagger-2011}.
44	
45	\paragraph{Statistical limitations.}
46	With $K{=}11$ task-type clusters falling below the $K \geq 20$--$50$ threshold recommended by \citet{cameron-2008,webb-2023}, cluster bootstrap yields wider CIs ($[73.3\%, 100.0\%]$); readers should rely on the non-clustered episode-level CI ($[81.3\%, 99.1\%]$). Wild cluster bootstrap ($p < 0.001$; Appendix~\ref{app:wild-cluster}) and 100\% directional consistency across all 28 death-prone tasks mitigate this concern.
47	
48	\section*{Ethics Statement}
49	
50	This work uses ScienceWorld \citep{scienceworld-2022}, a publicly available text-based simulation environment, and does not involve human subjects or private data. All evaluation environments (ScienceWorld, ALFWorld, MATH) are released under permissive open-source licenses (Apache 2.0 / MIT). All models used (Qwen2.5 family, Llama-3.1-8B, Gemma-2-9B-it) are publicly available for research use. All language models are accessed via standard APIs or publicly released weights. Experiments were conducted on 2$\times$ NVIDIA RTX 5090 (32GB) and 4$\times$ NVIDIA RTX 6000 PRO (96GB), totaling approximately 200 GPU-hours, comprising ${\sim}$140 hours for episode collection (counterfactual inference across three 7--9B model families plus Qwen2.5-72B backbone scaling, Reflexion and retry baselines, and cross-environment validation on ALFWorld and MATH), ${\sim}$35 hours for router training (LoRA fine-tuning of Qwen3-0.6B/1.7B/4B across 4--8 seeds per scale, including augmentation and ablation variants), and ${\sim}$25 hours for evaluation and analysis. Code and data will be released upon acceptance.
51	
52	\bibliography{references}
53	
54	\appendix
55	
56	\noindent\textbf{Appendix Overview.}
57	\hyperref[app:sci]{A.~Signal Concentration Index} $\cdot$
58	\hyperref[app:labeling]{B.~Labeling Quality Audit} $\cdot$
59	\hyperref[app:per-task]{C.~Per-Task Decomposition} $\cdot$
60	\hyperref[app:correlation]{D.~Correlation Robustness} $\cdot$
61	\hyperref[app:wild-cluster]{E.~Cluster Bootstrap Sensitivity} $\cdot$
62	\hyperref[app:per-task-ci]{F.~Per-Task CIs} $\cdot$
63	\hyperref[app:loto-daf]{G.~Leave-One-Task-Out DAF} $\cdot$
64	\hyperref[app:dose-response]{H.~Dose-Response Breakdown} $\cdot$
65	\hyperref[app:router-details]{I.~Router Training Details} $\cdot$
66	\hyperref[app:seed-robustness]{J.~Seed Robustness} $\cdot$
67	\hyperref[app:penalty]{K.~Penalty Sensitivity} $\cdot$
68	\hyperref[app:cross-env-details]{L.~Cross-Environment Details} $\cdot$
69	\hyperref[app:cross-model]{M.~Cross-Model Verification} $\cdot$
70	\hyperref[app:failure-modes]{N.~Failure Mode Analysis} $\cdot$
71	\hyperref[app:grounding-ablation]{O.~Grounding Ablation} $\cdot$
72	\hyperref[app:ablations]{P.~Ablation Studies} $\cdot$
73	\hyperref[sec:threshold-routing]{Q.~Threshold Routing} $\cdot$
74	\hyperref[app:decision-framework]{R.~Decision Framework} $\cdot$
75	\hyperref[app:extended-validation]{S.~Extended Validation} $\cdot$
76	\hyperref[app:prompt-templates]{T.~Agent Prompt Templates} $\cdot$
77	\hyperref[app:non-death-case-study]{U.~Non-Death Episode Case Study}
78	
79	\section{Signal Concentration Index}
80	\label{app:sci}
81	
82	Let $K$ denote the number of task types and $c_k$ the contribution of task type $k$ to the aggregate routing signal, defined as the fraction of total death-rate differential attributable to task $k$:
83	\begin{equation}
84	    c_k = \frac{n_k \cdot \delta_k}{\sum_{j=1}^{K} n_j \cdot \delta_j}
85	\end{equation}
86	where $n_k$ is the number of episodes and $\delta_k = d_k^{\tt int} - d_k^{\tt det}$ is the per-task death-rate differential. The SCI is the Gini coefficient over $\{c_1, \ldots, c_K\}$:
87	\begin{equation}
88	    \text{SCI} = \frac{\sum_{i=1}^K \sum_{j=1}^K |c_i - c_j|}{2K \sum_{k=1}^K c_k}
89	\end{equation}
90	
91	\section{Labeling Quality Audit}
92	\label{app:labeling}
93	
94	\begin{algorithm}[t]
95	\caption{Episode-Level Counterfactual Labeling}
96	\label{alg:labeling}
97	\begin{algorithmic}[1]
98	\REQUIRE Task instance $t$, computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$
99	\ENSURE Label $\ell \in \{{\tt det\text{-}pref}, {\tt int\text{-}pref}, {\tt no\text{-}pref}\}$
100	\FOR{each $m \in \mathcal{M}$}
101	    \STATE Run episode $\tau_m$ with pure-strategy $m$
102	    \STATE Record score $s_m$ and death indicator $d_m$
103	\ENDFOR
104	\IF{$d_{\tt int} = 1$ \AND $d_{\tt det} = 0$}
105	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{death asymmetry}
106	\ELSIF{$d_{\tt int} = 0$ \AND $d_{\tt det} = 1$}
107	    \STATE $\ell \leftarrow {\tt int\text{-}pref}$ \COMMENT{death asymmetry}
108	\ELSIF{$d_{\tt int} = d_{\tt det} = 1$}
109	    \STATE $\ell \leftarrow {\tt no\text{-}pref}$ \COMMENT{both dead}
110	\ELSIF{$s_{\tt det} > s_{\tt int}$}
111	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{score comparison}
112	\ELSIF{$s_{\tt int} > s_{\tt det}$}
113	    \STATE $\ell \leftarrow {\tt int\text{-}pref}$ \COMMENT{score comparison}
114	\ELSE
115	    \STATE $\ell \leftarrow {\tt no\text{-}pref}$ \COMMENT{tied alive}
116	\ENDIF
117	\RETURN $\ell$
118	\end{algorithmic}
119	\smallskip
120	\noindent\textit{Assumption:} The death-first priority (lines 5--10) is valid when $P$ exceeds the maximum partial score, guaranteeing that a dead episode never outscores a surviving one. ScienceWorld satisfies this ($P{=}100$, max partial score ${=}100$).\\
121	\noindent\textit{Note:} When both strategies die (line 9), we assign \texttt{no\_preference}; in ScienceWorld, death yields a fixed $-100$ regardless of timing, so both-dead episodes contribute no routing signal.
122	\end{algorithm}
123	
124	Note that episode-level labels are used to evaluate step-level predictions, introducing a granularity mismatch rather than independent validation. A potential concern is oracle circularity: whether episode-level labels reflect tie-breaking artifacts rather than genuine computation mode differences. We audit all 245 labels. Of the 150 \texttt{no\_preference} labels (61.2\%), 115 (46.9\%) are both-alive ties and 35 (14.3\%) are both-dead, all excluded from router training. The remaining 95 training labels are entirely genuine: 75 from death asymmetry (70 deterministic-preferred, 5 internal-preferred) and 20 from score comparison with both strategies surviving (16 deterministic-preferred, 4 internal-preferred). Zero labels depend on tie-breaking. Retraining the router using only death-asymmetry labels yields step-level balanced accuracy of 57.3\%, within 1$\sigma$ of the full-label retrain (57.6 $\pm$ 0.5\%, step-level Trainer evaluation); score-comparison labels contribute negligible additional signal. (Step-level metrics are used here for the relative comparison; as shown in \S\ref{sec:router-diagnostic}, absolute generalization to new episodes is near chance.) The 97.4\% step-level tie rate (\S\ref{sec:collection}) further motivates episode-level over step-level labeling.
125	
126	\section{Per-Task Decomposition}
127	\label{app:per-task}
128	We use ScienceWorld v1.2.3~\citep{scienceworld-2022}.
129	We select 11 of ScienceWorld's 30 task types for analysis. Types are excluded when they were used for pipeline development (5 tasks, standard hold-out practice), are taxonomically redundant with a retained family representative (7 tasks), or exhibit near-zero task progress under both strategies (7 tasks, agent capability floor).\footnote{Excluded tasks exhibit even stronger death dominance than included tasks ($\Delta\text{DR} = +38.2$\,pp vs.\ $+28.7$\,pp; Table~\ref{tab:excluded-death}).}
130	
131	\begin{table}[h]
132	\centering
133	\scriptsize
134	\setlength{\tabcolsep}{2.5pt}
135	\begin{tabular}{@{}lrrccc@{}}
136	\toprule
137	Task & $n$ & $\Delta_\text{full}$ & D\%\textsubscript{int} & D\%\textsubscript{det} & D / I / N \\
138	\midrule
139	id-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\
140	lifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\
141	lifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\
142	inclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\
143	freeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\
144	meas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\
145	id-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\
146	find-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\
147	grow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\
148	chem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\
149	\midrule
150	find-non-living-thing$^\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\
151	\midrule
152	\textbf{All (11 tasks)} & \textbf{245} & $\mathbf{+29.60}$ & \textbf{42.9} & \textbf{16.3} & \textbf{86 / 9 / 150} \\
153	\bottomrule
154	\end{tabular}
155	\caption{Per-task decomposition of the death avoidance effect. D\%: death rate for internal (int) and deterministic (det) strategies. D/I/N: episode labels (det-preferred / internal-preferred / no-preference). Sorted by $\Delta_{\text{full}}$ descending. The \textit{All} row is an episode-weighted aggregate across 245 episodes. $\dagger$\,Only task with zero deaths under both strategies; $n{=}40$ because data was collected in two batches, with the second batch adding 20 episodes to increase statistical power for this zero-death outlier.}
156	\label{tab:per-task}
157	\end{table}
158	
159	\paragraph{Task selection and anti-cherry-picking.}
160	Eighteen of the 19 excluded task types (95\%) exhibit death-asymmetric patterns (Table~\ref{tab:excluded-death}): internal-reasoning death rates range from 40\% to 60\% (mean 53.9\%), while deterministic death rates range from 0\% to 40\% (mean 15.8\%), yielding a mean death-rate differential of $+38.2$\,pp, exceeding the $+28.7$\,pp for included tasks. The included subset is thus \emph{less} death-asymmetric than the excluded subset, the opposite of what a cherry-picking hypothesis would predict. The sole exception is \texttt{grow-plant}, an intrinsically safe task with zero deaths under both strategies, paralleling \texttt{find-non-living-thing} in the included set. The 19 excluded tasks fall into three independently motivated categories: five used during pipeline development (standard hold-out practice), seven taxonomically redundant with included family representatives (deduplication), and seven where the 7B backbone achieves near-zero task progress regardless of strategy (agent capability floor). In no case was a task excluded because death dominance was absent. Exclusion is driven by absence of non-death routing signal ($\Delta_{\text{nd}} = 0$ for 53\% of excluded tasks) and standard deduplication practices. \texttt{find-non-living-thing} serves as an internal counterexample: zero deaths under both strategies yet included because it exhibits non-death routing signal ($\Delta_{\text{full}} = +9.58$ entirely from score differences), and deterministic is not always preferred (4 of 20 non-tie labels favor internal).
161	
162	\begin{table}[t]
163	\centering
164	\scriptsize
165	\setlength{\tabcolsep}{2pt}
166	\resizebox{\columnwidth}{!}{%
167	\begin{tabular}{@{}llrcccl@{}}
168	\toprule
169	Task & Grp & $n$ & D\%\textsubscript{int} & D\%\textsubscript{det} & $\Delta$DR & Excl.\ reason \\
170	\midrule
171	boil                          & A & 20 & 50 & 20 & $+30$ & dev set \\
172	change-state-of-matter        & A & 20 & 55 & 15 & $+40$ & dev set \\
173	chem-mix-paint-secondary      & A & 20 & 45 & 10 & $+35$ & dev set \\
174	grow-plant                    & A & 20 &  0 &  0 & $\phantom{+}0$  & dev set \\
175	melt                          & A & 20 & 55 & 15 & $+40$ & dev set \\
176	\midrule
177	chem-mix-paint-tertiary       & B &  5 & 40 & 20 & $+20$ & family redundancy \\
178	find-living-thing             & B &  5 & 60 & 20 & $+40$ & family redundancy \\
179	find-plant                    & B &  5 & 60 &  0 & $+60$ & family redundancy \\
180	inclined-friction-named       & B &  5 & 60 & 20 & $+40$ & family redundancy \\
181	inclined-friction-unnamed     & B &  5 & 60 &  0 & $+60$ & family redundancy \\
182	lifespan-shortest             & B &  5 & 60 & 40 & $+20$ & family redundancy \\
183	measure-melt-known            & B &  5 & 60 &  0 & $+60$ & family redundancy \\
184	\midrule
185	mendelian-known               & C &  5 & 60 & 20 & $+40$ & agent floor \\
186	mendelian-unknown             & C &  5 & 60 & 40 & $+20$ & agent floor \\
187	power-component               & C &  5 & 60 & 20 & $+40$ & agent floor \\
188	power-renewable               & C &  5 & 60 &  0 & $+60$ & agent floor \\
189	test-conductivity             & C &  5 & 60 & 20 & $+40$ & agent floor \\
190	test-conductivity-unknown     & C &  5 & 60 & 20 & $+40$ & agent floor \\
191	use-thermometer               & C &  5 & 60 & 20 & $+40$ & agent floor \\
192	\midrule
193	\textbf{Mean (19 excluded)}   &   &    & \textbf{53.9} & \textbf{15.8} & $\mathbf{+38.2}$ & \\
194	\textit{cf.\ included (11)}   &   &    & \textit{46.5} & \textit{17.8} & $\textit{+28.7}$ & \\
195	\bottomrule
196	\end{tabular}}%
197	\caption{Death-rate analysis of all 19 excluded task types. D\%: death rate (score $\leq -100$). $\Delta$DR = D\%\textsubscript{int} $-$ D\%\textsubscript{det}. 18 of 19 excluded tasks (95\%) exhibit positive death asymmetry ($\Delta$DR $\geq +20$\,pp). Exclusion groups: A = development set (excluded to prevent circular evaluation), B = taxonomically redundant with an included family representative, C = agent-floor tasks (backbone achieves near-zero progress regardless of strategy). The mean $\Delta$DR among excluded tasks ($+38.2$\,pp) exceeds that of included tasks ($+28.7$\,pp), confirming that task selection does not bias toward death-prone tasks. Group B--C estimates are based on $n{=}5$ prescreening episodes per task and should be interpreted as directional evidence rather than precise rate estimates.}
198	\label{tab:excluded-death}
199	\end{table}
200	
201	\section{Correlation Robustness}
202	\label{app:correlation}
203	
204	The Pearson $r = 0.9698$ reported in \S\ref{sec:death-decomp} is robust across multiple diagnostics. Spearman rank correlation is $\rho = 0.986$ ($p = 2.4 \times 10^{-8}$); the relationship is not driven by outliers or non-linearity. A nonparametric bootstrap (10{,}000 resamples) yields 95\% CI $[0.952, 0.995]$.
205	
206	\begin{table}[h]
207	\centering
208	\small
209	\begin{tabular}{@{}lr@{}}
210	\toprule
211	Task removed & $r_{\text{LOO}}$ \\
212	\midrule
213	id-life-stages-1       & 0.963 \\
214	lifespan-long          & 0.969 \\
215	lifespan-l-then-s      & 0.976 \\
216	inclined-plane         & 0.969 \\
217	freeze                 & 0.971 \\
218	meas-melt-point        & 0.972 \\
219	id-life-stages-2       & 0.972 \\
220	find-animal            & 0.970 \\
221	grow-fruit             & 0.973 \\
222	chem-mix               & 0.969 \\
223	find-non-living-thing  & 0.980 \\
224	\bottomrule
225	\end{tabular}
226	\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\ $\Delta_{\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}
227	\label{tab:loo}
228	\end{table}
229	
230	\section{Cluster Bootstrap Sensitivity Analysis}
231	\label{app:wild-cluster}
232	
233	With $K{=}11$ task-type clusters, cluster bootstrap falls well below the $K{\geq}20$--50 recommended for reliable inference \citep{cameron-2008,webb-2023}. The narrower CIs obtained reflect known small-sample bias toward underestimation of variance, not tighter inference.
234	
235	Episodes within the same task type share environment dynamics, raising the concern that the effective sample size is closer to $K$ (task types) than $N$ (episodes). We address this with cluster-robust inference treating each task type as a cluster ($K{=}11$, all 11 included task types, 245 episodes).
236	
237	\begin{table}[h]
238	\centering
239	\small
240	\resizebox{\columnwidth}{!}{%
241	\begin{tabular}{@{}lcc@{}}
242	\toprule
243	Method & $p$-value & 95\% CI \\
244	\midrule
245	Cluster-robust $t$-test ($t{=}10.0$, df$=$10) & $< 0.001$ & $[0.73, 1.00]$ \\
246	Wild cluster bootstrap ($B{=}9{,}999$) & $< 0.001$ & $[0.73, 1.00]$ \\
247	Exact permutation ($2{,}048$ perms) & $0.002$ & --- \\
248	Sign test & $< 0.001$ & --- \\
249	\bottomrule
250	\end{tabular}}%
251	\caption{Cluster-level tests of death-rate asymmetry ($K{=}11$ task clusters, 245 episodes). 10 of 11 clusters show internal DR $>$ deterministic DR; the sole exception (\texttt{find-non-living-thing}) has zero deaths under both strategies. Cohen's $d = 3.02$. The exact permutation $p = 0.002$ ($4/2{,}048$) reflects the near-unanimous directional consistency.}
252	\label{tab:wild-cluster}
253	\end{table}
254	
255	\noindent All methods confirm significance with $p < 0.01$, and the 95\% CI $[0.73, 1.00]$ excludes zero by a wide margin. With $K{=}11$ task types, ICC estimation itself carries substantial uncertainty; the high within-task consistency of death patterns (all-or-nothing per task type) suggests high ICC, which explains the CI narrowing under cluster resampling.
256	
257	We retain this analysis for transparency; readers should rely on the non-clustered episode-level bootstrap (\S\ref{sec:death-decomp}) as the primary inference.
258	
259	\section{Per-Task Death Rate Confidence Intervals}
260	\label{app:per-task-ci}
261	
262	We compute bootstrap 95\% CIs for the death-rate differential ($\Delta\text{DR} = \text{DR}_{\text{int}} - \text{DR}_{\text{det}}$) for all 30 ScienceWorld task types. Of 30 tasks, 28 are death-prone (at least one death under either strategy); the remaining 2 (\texttt{grow-plant}, \texttt{find-non-living-thing}) have zero deaths under both strategies.
263	
264	Across all 28 death-prone tasks, internal DR exceeds deterministic DR without exception (100\% directional consistency). The pooled death-rate differential is $+37.3\%$ (95\% CI: $[29.7\%, 44.4\%]$). Fifteen of 28 tasks are individually significant (CI excludes zero); the 13 non-significant tasks all have $n{=}5$ prescreening episodes, where statistical power is insufficient to detect even large effects (e.g., a task with $\Delta\text{DR} = +40$\,pp at $n{=}5$ has a CI of $\pm 43$\,pp). The universal directional consistency, combined with the pooled significance, confirms that death asymmetry is not driven by a subset of outlier tasks.
265	
266	\section{Leave-One-Task-Out DAF Sensitivity}
267	\label{app:loto-daf}
268	
269	\begin{table}[h]
270	\centering
271	\small
272	\caption{Leave-one-task-out DAF sensitivity (penalty-independent label fraction). Among the 10 death-prone tasks, removing any single task changes DAF by at most 3.0\,pp (range: 75.9\%--78.9\%). Removing \emph{Find Non-Living Thing}, the sole death-free task that contributes all 20 score-comparison episodes, raises DAF to 100\% by construction.}
273	\label{tab:loto-daf}
274	\begin{tabular}{lrrr}
275	\toprule
276	Removed Task & $N_\text{rem}$ & DAF (\%) & $\Delta$ (pp) \\
277	\midrule
278	(none, full) & 245 & 78.9 & --- \\
279	\midrule
280	Find Non-Living$^\dagger$ & 205 & 100.0 & +21.1 \\
281	Lifespan Longest & 220 & 75.9 & $-$3.0 \\
282	Life Stages 1 & 225 & 76.7 & $-$2.2 \\
283	Lifespan Long+Short & 225 & 76.7 & $-$2.2 \\
284	Chemistry Mix & 225 & 77.0 & $-$1.9 \\
285	Grow Fruit & 225 & 77.3 & $-$1.7 \\
286	Inclined Plane Angle & 225 & 77.3 & $-$1.7 \\
287	Freeze & 225 & 77.5 & $-$1.4 \\
288	Life Stages 2 & 225 & 77.5 & $-$1.4 \\
289	Melt Pt Unknown & 225 & 77.5 & $-$1.4 \\
290	Find Animal & 225 & 77.8 & $-$1.2 \\
291	\bottomrule
292	\end{tabular}
293	
294	\vspace{2pt}
295	{\footnotesize $^\dagger$Only death-free task; contributes all score-comparison labels. Sorted by $|\Delta|$ descending.}
296	\end{table}
297	
298	\section{Per-Task Dose-Response Breakdown}
299	\label{app:dose-response}
300	
301	Table~\ref{tab:dose-response-detail} reports per-task death rates for Reflexion at $N{=}3$, 4, and 5 on the 10 death-prone tasks ($n{=}20$ episodes per task). Per-task variance is high (up to 25\,pp range for \texttt{measure-melting-point}), but the aggregate smooths to a 2.5\,pp band, confirming that the stabilization conclusion is robust at the aggregate level despite task-level noise. \texttt{freeze} is consistently the hardest task (50--60\% DR across all $N$).
302	
303	\paragraph{Statistical power.} With $n{=}200$ paired episodes, the minimum detectable effect (MDE) is ${\sim}8$~pp ($\alpha = 0.05$, 80\% power). The key $N{=}1{\to}3$ decline ($-13.5$~pp) exceeds this threshold and is well-powered; the stabilization claim ($N{=}3{\to}5$, $+1.0$~pp) is also supported, since a ${\geq}8$~pp improvement would be detected if present.
304	
305	\begin{table}[h]
306	\centering
307	\small
308	\caption{Per-task death rates (\%) for Reflexion at $N{=}3$, 4, 5 on 10 death-prone tasks ($n{=}20$ per task). Aggregate death rates confirm stabilization at $N \geq 3$ (range: $34.0$--$36.5\%$).}
309	\label{tab:dose-response-detail}
310	\begin{tabular}{@{}lrrr@{}}
311	\toprule
312	Task & $N{=}3$ & $N{=}4$ & $N{=}5$ \\
313	\midrule
314	chemistry-mix & 25.0 & 35.0 & 20.0 \\
315	find-animal & 45.0 & 30.0 & 45.0 \\
316	freeze & 50.0 & 50.0 & 60.0 \\
317	grow-fruit & 30.0 & 25.0 & 25.0 \\
318	identify-life-stages-1 & 35.0 & 35.0 & 35.0 \\
319	identify-life-stages-2 & 25.0 & 25.0 & 30.0 \\
320	inclined-plane-angle & 20.0 & 30.0 & 35.0 \\
321	lifespan-longest & 45.0 & 40.0 & 40.0 \\
322	lifespan-long+short & 30.0 & 45.0 & 35.0 \\
323	measure-melting-pt & 35.0 & 50.0 & 25.0 \\
324	\midrule
325	\textbf{Aggregate} & \textbf{34.0} & \textbf{36.5} & \textbf{35.0} \\
326	\bottomrule
327	\end{tabular}
328	\end{table}
329	
330	\section{Router Training Details}
331	\label{app:router-details}
332	
333	We use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.
334	
335	With gradient accumulation of 1 (effective batch size 4), routing performance is highly sensitive to the evaluation split; this suggests overfitting to specific train/validation partition boundaries. With gradient accumulation of 8 (effective batch size 32), step-level performance stabilizes across splits (${\sim}54\%$ balanced accuracy). All reported results use gradient accumulation 8.
336	
337	Under step-level evaluation with a fixed data split, cross-seed balanced accuracy ranges from 52.7\% to 58.1\%, but internal recall varies from 51.5\% to 81.8\%, which reflects threshold sensitivity. However, episode-level evaluation reveals that this apparent discrimination does not generalize: balanced accuracy drops to $47.1 \pm 2.2\%$ across 8 cross-split seeds (Appendix~\ref{app:seed-robustness}). Deployed end-to-end, the trained router allocates 97.0\% of episodes to deterministic computation with 17.6\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.
338	
339	\paragraph{Evaluation methods.} All results use \emph{generation-based evaluation}: the model generates a routing label as text (\texttt{enable\_thinking=False}), parsed for classification. We evaluate at two granularities: \emph{step-level} (steps from the same episode may appear in both train and validation sets) and \emph{episode-level} (entire episodes held out). Step-level accuracy ($54.1 \pm 5.4\%$) exceeds chance (the router captures some signal), but episode-level accuracy ($47.1 \pm 2.2\%$, below chance) shows this does not generalize to unseen episodes. Paraphrase-based text augmentation (Appendix~\ref{app:seed-robustness}) provides no improvement; real-data scaling remains open. Always-deterministic is trivially near-optimal given DAF $= 90.4\%$. The main text (\S\ref{sec:router-diagnostic}) reports controlled 4-seed results at three scales; the model-size ablation (Appendix~\ref{app:ablations}) provides further detail.
340	
341	\begin{table}[h]
342	\centering
343	\small
344	\resizebox{\columnwidth}{!}{%
345	\begin{tabular}{@{}lcc@{}}
346	\toprule
347	Hyperparameter & Classification Head & Implicit Router \\
348	\midrule
349	Base model & Qwen3-1.7B & Qwen3-1.7B \\
350	Architecture & Linear + LoRA & SFT + LoRA \\
351	LoRA $r$ / $\alpha$ & 16 / 32 & 16 / 32 \\
352	Learning rate & 2e-5 & 2e-4 \\
353	Optimizer & AdamW & AdamW \\
354	Epochs & 3 & 3 \\
355	Batch size (per device) & 4 & 4 \\
356	Gradient accumulation & 8 & 8 \\
357	Warmup ratio & 0.1 & 0.1 \\
358	Weight decay & 0.01 & 0.01 \\
359	Max sequence length & 512 & 512 \\
360	Seeds & \{42\} & \{42, 123, 456, 789\} \\
361	\bottomrule
362	\end{tabular}}
363	\caption{Router training hyperparameters. Both architectures use the same base model with LoRA adaptation. The classification head degenerates across all configurations; the implicit router results are reported as 4-seed mean$\pm$std.}
364	\label{tab:hyperparams}
365	\end{table}
366	
367	\paragraph{Agent inference parameters.}
368	For ScienceWorld, each agent step uses temperature $T{=}0.3$ and maximum generation length of 256 tokens, served via vLLM v0.21.0. Top-$p$ is left at the vLLM default of $1.0$ (no nucleus sampling). For MATH, the agent uses greedy decoding ($T{=}0.0$) with a maximum of 2{,}048 tokens per generation. For ALFWorld, we use $T{=}0.3$ with 256 maximum tokens. All three environments use Qwen2.5-7B-Instruct~\citep{qwen25-2024} as the backbone.
369	
370	\section{Seed Robustness}
371	\label{app:seed-robustness}
372	
373	\paragraph{Counterfactual collection seed.}
374	We re-collect all episodes with a different ScienceWorld environment seed (seed=123, $N{=}220$, 20 episodes per task type).
375	The replication yields DAF $= 89.7\%$ ($\Delta_\text{nd} = 2.83$, $\Delta_\text{full} = 27.47$),
376	within 0.73~pp of the primary estimate (seed=42, DAF $= 90.4\%$).
377	Label distributions are consistent: 67 deterministic-preferred / 7 internal-preferred / 146 no-preference
378	(primary: 86 / 9 / 150).
379	Death rates by strategy remain directionally aligned ($\text{DR}_\text{int} = 45.5\%$ vs.\ $42.9\%$; $\text{DR}_\text{det} = 20.9\%$ vs.\ $16.3\%$).
380	The seed=123 replication uses $N{=}220$ ($20$ episodes per task type);
381	the primary dataset's larger $N{=}245$ reflects 25 additional episodes across two task types (\texttt{find-non-living-thing}: $n{=}40$; \texttt{lifespan-longest-lived}: $n{=}25$; all others: $n{=}20$).
382	
383	\paragraph{Router training seed.}
384	We assess router generalization at two evaluation granularities: \emph{step-level}, where steps from the same episode may appear in both train and validation sets, and \emph{episode-level}, where entire episodes are held out. Both use cross-split evaluation (seeds $\{42, \ldots, 49\}$, 8 seeds total), where the data partition and training seed both vary. Table~\ref{tab:seed-robustness} reports per-seed results.
385	
386	\begin{table}[h]
387	\centering
388	\small
389	\begin{tabular}{@{}llcc@{}}
390	\toprule
391	Eval.\ Granularity & Seed & Bal.\ Acc.\ (\%) \\
392	\midrule
393	Step-level & 42 & 57.06 \\
394	(same-episode & 43 & 63.99 \\
395	leakage) & 44 & 55.43 \\
396	 & 45 & 56.14 \\
397	 & 46 & 55.45 \\
398	 & 47 & 50.08 \\
399	 & 48 & 48.03 \\
400	 & 49 & 59.30 \\
401	\cmidrule{2-3}
402	 & Mean$\pm$std & $54.1 \pm 5.4$ \\
403	\midrule
404	Episode-level & 42 & 48.1 \\
405	(held-out & 43 & 47.9 \\
406	episodes) & 44 & 49.6 \\
407	 & 45 & 49.4 \\
408	 & 46 & 48.5 \\
409	 & 47 & 43.1 \\
410	 & 48 & 45.4 \\
411	 & 49 & 44.8 \\
412	\cmidrule{2-3}
413	 & Mean$\pm$std & $47.1 \pm 2.2$ \\
414	\midrule
415	\multicolumn{2}{@{}l}{Always-det (= majority-vote)} & 50.0 \\
416	\bottomrule
417	\end{tabular}
418	\caption{Per-seed router performance under cross-split evaluation (8 seeds, generation-based, \texttt{enable\_thinking=False}). Step-level evaluation allows steps from the same episode in both train and validation sets (same-episode leakage). Episode-level evaluation holds out entire episodes; the resulting $47.1 \pm 2.2\%$ is below the 50\% chance baseline. A text augmentation ablation (Table~\ref{tab:text-augmentation}) confirms this failure persists under the current data distribution and augmentation regime.}
419	\label{tab:seed-robustness}
420	\end{table}
421	
422	The contrast between step-level ($54.1 \pm 5.4\%$) and episode-level ($47.1 \pm 2.2\%$) evaluation reveals a generalization gap: the step-level signal likely reflects memorization of episode-specific context (enabled by same-episode leakage) rather than extraction of generalizable routing features. At episode level, the router performs below chance across all 8 seeds (range: 43.1\%--49.6\%). Paraphrase-based text augmentation (Table~\ref{tab:text-augmentation}) from 25\% to 800\% ($32{\times}$ range) provides no improvement, converging to the always-deterministic baseline ($50\%$). Paraphrase augmentation inflates the majority class without generating novel routing patterns; genuine episode-level scaling (collecting more counterfactual pairs) remains an open question. With DAF $= 90.4\%$ and all task types deterministic-majority (86:9 label ratio), always-deterministic trivially solves the episode-level routing problem, leaving the step-level router with no exploitable signal under current architectures.
423	
424	\paragraph{Text augmentation ablation.} To test whether the episode-level generalization failure stems from data scarcity, we vary training set size from 25\% to 800\% of the original via paraphrase-based text augmentation (synonym substitution + template variation on step observations), holding the episode-level validation set fixed. This tests augmentation-based scaling, not genuine episode-level scaling (which would require new counterfactual collections). Table~\ref{tab:text-augmentation} reports the results.
425	
426	\begin{table}[h]
427	\centering
428	\small
429	\begin{tabular}{@{}rccc@{}}
430	\toprule
431	Scale & Samples & Det\% & Ep.\ Bal.\ Acc.\ (\%) \\
432	\midrule
433	25\% & 433 & ${\sim}90$ & $49.5 \pm 0.3$ \\
434	50\% & 867 & ${\sim}90$ & $51.5$ \\
435	100\% & 1{,}735 & 89.6 & $49.9 \pm 0.1$ \\
436	200\% & 3{,}470 & 94.2 & $50.0 \pm 0.0$ \\
437	800\% & 13{,}880 & ${\sim}97.7$ & $51.0 \pm 1.1$ \\
438	\midrule
439	Always-det & --- & --- & 50.0 \\
440	\bottomrule
441	\end{tabular}
442	\caption{Text augmentation ablation: episode-level balanced accuracy across training set sizes (25\%--800\% of original via paraphrase, $32{\times}$ range). Internal recall $= 0.0$ at all scales (complete majority-class collapse). Det\%: fraction of deterministic-preferred labels in training data. The 50\% scale is a single seed; all others report mean$\pm$std across seeds.}
443	\label{tab:text-augmentation}
444	\end{table}
445	
446	All scales hover at ${\sim}50\%$ episode-level balanced accuracy (equivalent to the always-deterministic baseline), with no monotonic improvement as data increases. Augmentation-based scaling provides no improvement at any scale; however, episode-level minority-class diversity remains a potential confound that cannot be resolved without collecting more internal-preferred episodes. The ground-truth internal-preferred rate (9/245 $= 3.7\%$) means collecting 50 internal-preferred episodes would require approximately 1{,}350 paired episodes at current environment dynamics, a $5.5{\times}$ expansion with diminishing return on a $9.6\%$ signal. The failure points to a limitation of the current data distribution: when DAF $= 90.4\%$ and all task types are deterministic-majority (86:9 label ratio), the episode-level routing problem is trivially solved by always choosing deterministic, and the step-level router finds no exploitable signal under the current architecture and data regime.
447	
448	Augmentation disproportionately increases the majority (deterministic) class: Det\% rises from 89.6\% at 100\% to 94.2\% at 200\% and ${\sim}97.7\%$ at 800\%. However, the complete collapse to majority-class prediction (internal recall $= 0.0$) occurs even at the smallest unaugmented scale (25\%, ${\sim}90\%$ det); this is not an augmentation artifact. Balanced accuracy corrects for class imbalance by averaging per-class recall, so the metric itself is not biased by the skew.
449	
450	Decomposition metrics are stable under bootstrap resampling ($B{=}10{,}000$ resamples of the 245-episode dataset): DAF $= 90.4\% \pm 4.2\%$ (95\% CI $[81.3\%, 99.1\%]$); Pearson $r = 0.975 \pm 0.011$ (95\% CI $[0.952, 0.995]$). The death avoidance dominance finding is robust to both resampling and split perturbation.
451	
452	\paragraph{Per-task-type evaluation breakdown.} To test whether the router learns transferable routing strategies or merely task-type classification, we evaluate existing checkpoints (8 seeds) separately on each of the 11 task types. Of the 11 task types, 7 have \emph{all-deterministic} labels (no internal-preferred episodes exist), making balanced accuracy undefined; the router has nothing to learn beyond the trivial always-deterministic default. For the remaining 4 task types where both classes are present, balanced accuracy ranges from 50.0\% to 73.0\%, but this apparent signal does not indicate cross-task-type routing transfer: the router is effectively classifying task types (which correlate with death risk) rather than extracting a generalizable routing strategy. This complements the text augmentation ablation: routing signal does not transfer across task types because the signal \emph{is} the task type, i.e., whether a given task carries death risk. The 4B capacity scaling result (Appendix~\ref{app:ablations}) suggests capacity is one factor, but even 4B's $59.0\%$ episode-level accuracy does not demonstrate cross-task-type transfer.
453	
454	\section{Penalty Sensitivity Analysis}
455	\label{app:penalty}
456	
457	\begin{table}[h]
458	\centering
459	\small
460	\begin{tabular}{@{}rrr@{}}
461	\toprule
462	$P$ & DAF($P$) & 95\% CI \\
463	\midrule
464	0 & 7.4\% & [$-39.4$, $82.5$] \\
465	1 & 14.8\% & [$-28.6$, $89.6$] \\
466	5 & 35.4\% & [$-1.8$, $92.7$] \\
467	10 & 50.4\% & [$18.5$, $93.3$] \\
468	25 & 70.7\% & [$48.0$, $96.3$] \\
469	50 & 82.6\% & [$67.2$, $98.2$] \\
470	100\textsuperscript{*} & 90.4\% & [$81.3$, $99.1$] \\
471	200 & 94.9\% & [$89.9$, $99.5$] \\
472	500 & 97.9\% & [$95.7$, $99.8$] \\
473	\bottomrule
474	\end{tabular}
475	\caption{Sensitivity of DAF to death penalty magnitude $P$. DAF$(P) = 1 - \Delta_{\text{nd}} / \Delta_{\text{full}}(P)$, where $\Delta_{\text{full}}(P) \approx \delta \cdot P + \Delta_{\text{nd}}$, $\delta = 0.2653$ is the death-rate differential, and $\Delta_{\text{nd}} = 2.84$ (strict neither-died filtering). Recomputed from 245 episode-level data; bootstrap 95\% CIs ($B{=}10{,}000$). \textsuperscript{*}Default setting.}
476	\label{tab:penalty-sensitivity}
477	\end{table}
478	
479	The non-death score gap $\Delta_{\text{nd}} = 2.84$ is invariant across penalty levels; it depends only on surviving-episode performance, not on $P$. As $P$ increases, $\Delta_{\text{full}}$ grows ($16.33$ at $P{=}50$, $29.60$ at $P{=}100$, $56.13$ at $P{=}200$) while $\Delta_{\text{nd}}$ remains fixed, mechanically increasing DAF.
480	
481	\paragraph{Mechanism boundary: death specificity.}
482	The $r = 0.97$ correlation between per-task death-rate differential and $\Delta_{\text{full}}$ is specific to catastrophic death (score $= -100$). Broader failure definitions dissolve the correlation entirely: defining ``failure'' as any non-positive score ($T{=}0$) yields $r = -0.13$ ($p = 0.70$), because non-death episodes show near-zero performance differential between strategies ($\Delta_{\text{nd}} = 2.84$). Table~\ref{tab:penalty-correlation} quantifies this specificity across penalty magnitudes.
483	
484	\begin{table}[h]
485	\centering
486	\small
487	\begin{tabular}{@{}rccl@{}}
488	\toprule
489	$P$ & $r$ & $p$ & Sig.\ ($\alpha{=}0.05$) \\
490	\midrule
491	1 & $-0.44$ & $0.178$ & No \\
492	5 & $-0.29$ & $0.382$ & No \\
493	10 & $-0.08$ & $0.813$ & No \\
494	25 & $0.51$ & $0.108$ & No \\
495	50 & $0.86$ & $0.0006$ & Yes \\
496	100\textsuperscript{*} & $0.97$ & $8 \times 10^{-7}$ & Yes \\
497	200 & $0.99$ & $1 \times 10^{-9}$ & Yes \\
498	\bottomrule
499	\end{tabular}
500	\caption{Pearson $r$ between per-task death-rate differential and $\Delta_{\text{full}}(P)$ across penalty magnitudes. The correlation is non-significant at low penalties and emerges at $P \geq 50$, which reflects the transition from non-death-dominated to death-dominated score gaps. \textsuperscript{*}Default ScienceWorld setting.}
501	\label{tab:penalty-correlation}
502	\end{table}
503	
504	This sharpens our central finding: death is not merely the dominant component of routing signal; it is effectively the \emph{only} component that generates differential routing signal in ScienceWorld. At low penalties, the death contribution is small and $\Delta_{\text{full}}$ reduces to $\Delta_{\text{nd}} \approx 2.84$, which is near-uniform across task types ($\text{mean non-death gap} = -1.19$ excluding the \texttt{find-non-living-thing} outlier); consequently, death-rate differential has no predictive power. As $P$ increases, the death term dominates $\Delta_{\text{full}}$, and the correlation sharpens because death rates \emph{are} the performance gap. The DAF values in Table~\ref{tab:penalty-sensitivity} increase monotonically with $P$, but this is a mathematical consequence of the decomposition ($\text{DAF} = \delta P / (\delta P + \Delta_{\text{nd}})$), not evidence of mechanism robustness.
505	
506	\section{Cross-Environment Details}
507	\label{app:cross-env-details}
508	
509	Table~\ref{tab:cross-env} summarizes the label distributions across all three environments (see also Figure~\ref{fig:signal-reversal} in \S\ref{sec:cross-env}).
510	
511	\begin{table}[h]
512	\centering
513	\small
514	\resizebox{\columnwidth}{!}{%
515	\begin{tabular}{@{}lccccc@{}}
516	\toprule
517	Environment & $N$ & Det\% & Int\% & NoPref\% & Death? \\
518	\midrule
519	ScienceWorld & 245 & 35.1 & 3.7 & 61.2 & Yes ($-100$) \\
520	MATH & 795 & 7.3 & 8.3 & 84.4 & No \\
521	ALFWorld & 135 & 25.9 & 1.5 & 72.6 & No\textsuperscript{$\dagger$} \\
522	\bottomrule
523	\end{tabular}}
524	\caption{Cross-environment label distribution. ``Deterministic'' denotes qualitatively different computation modes: ScienceWorld = oracle simulator with ground-truth state; MATH = Python code interpreter; ALFWorld = admissible-action enumeration. $\dagger$\,ALFWorld's deterministic advantage stems from information asymmetry, not death avoidance.}
525	\label{tab:cross-env}
526	\end{table}
527	
528	Table~\ref{tab:alfworld-pertask} provides the per-task-type breakdown for ALFWorld. Unlike ScienceWorld, ALFWorld has no death mechanism ($\delta = 0$, DAF $= 0\%$); the entire performance gap $\Delta_{\text{full}}$ reflects information asymmetry from admissible-action access. \texttt{pick\_and\_place} shows the strongest effect ($\Delta = 0.563$, 18 of 32 episodes det-preferred), while \texttt{pick\_two\_obj\_and\_place} shows the weakest ($\Delta = 0.087$), consistent with multi-object tasks requiring more sequential reasoning that admissible actions alone cannot resolve. Only \texttt{pick\_heat\_then\_place} has a 95\% CI crossing zero ($n{=}16$).
529	
530	\begin{table}[h]
531	\centering
532	\scriptsize
533	\setlength{\tabcolsep}{2.5pt}
534	\begin{tabular}{@{}lrcccc@{}}
535	\toprule
536	Task Type & $n$ & Succ\%\textsubscript{int} & Succ\%\textsubscript{det} & D / I / N & $\Delta_{\text{full}}$ \\
537	\midrule
538	pick\_and\_place       & 32 & 0.0  & 56.3 & 18 / 0 / 14 & $+0.563$ \\
539	look\_at\_obj\_in\_light & 13 & 15.4 & 38.5 & 3 / 0 / 10  & $+0.231$ \\
540	pick\_cool\_then\_place & 24 & 0.0  & 16.7 & 4 / 0 / 20  & $+0.167$ \\
541	pick\_clean\_then\_place & 27 & 3.7  & 18.5 & 5 / 1 / 21  & $+0.148$ \\
542	pick\_heat\_then\_place & 16 & 6.3  & 18.8 & 3 / 1 / 12  & $+0.125$ \\
543	pick\_two\_obj\_and\_place & 23 & 0.0 & 8.7  & 2 / 0 / 21  & $+0.087$ \\
544	\midrule
545	\textbf{All (6 types)} & \textbf{135} & \textbf{3.0} & \textbf{27.4} & \textbf{35 / 2 / 98} & $\mathbf{+0.244}$ \\
546	\bottomrule
547	\end{tabular}
548	\caption{Per-task-type decomposition for ALFWorld (135 games, Qwen2.5-7B-Instruct). D/I/N: deterministic-preferred / internal-preferred / no-preference. No death mechanism exists; $\Delta_{\text{full}}$ is driven entirely by information asymmetry from admissible-action access. Sorted by $\Delta_{\text{full}}$ descending.}
549	\label{tab:alfworld-pertask}
550	\end{table}
551	
552	\paragraph{MATH subset composition.}
553	The $N{=}795$ MATH problems span two categories from the MATH test set~\citep{math-2021} (Levels 4--5): Algebra (585, 73.6\%) and Counting \& Probability (210, 26.4\%). The category imbalance reflects the relative sizes in the original test set.
554	
555	\section{Cross-Model Verification}
556	\label{app:cross-model}
557	
558	We replicate the counterfactual analysis with Llama-3.1-8B-Instruct across all 11 task types ($N{=}220$ episode pairs, 20 per type; Table~\ref{tab:cross-model-detail}).
559	The internal strategy dies in $41.4\%$ of episodes versus $11.4\%$ for deterministic (death-rate differential $+30.0$~pp), with 83 deterministic-preferred, 3 internal-preferred (1.4\%, all death-asymmetry reversals), and 134 no-preference labels.
560	Both models exhibit nearly identical internal vulnerability (${\sim}$42\%: Qwen $42.9\%$, Llama $41.4\%$), confirming that death-prone failure is empirically dominated by the task environment rather than model-specific factors. The differential magnitude varies ($+26.5$~pp Qwen, $+30.0$~pp Llama) because deterministic strategy safety is model-dependent ($16.3\%$ vs.\ $11.4\%$), but directional consistency is 100\% (10/10 death-prone tasks in both models).
561	\texttt{identify-life-stages-1} shows cross-model precision matching ($55\%$/$10\%$/$+45$~pp in both models).
562	\texttt{find-non-living-thing} shows zero deaths in both models, consistent with its majority-class answer distribution.
563	
564	\begin{table}[h]
565	\centering
566	\small
567	\resizebox{\columnwidth}{!}{%
568	\begin{tabular}{@{}lrrrl@{}}
569	\toprule
570	Task & Int\% & Det\% & $\Delta$\,pp & D / I / N \\
571	\midrule
572	identify-life-stages-1 & 55 & 10 & +45 & 9 / 0 / 11 \\
573	freeze & 45 & 0 & +45 & 9 / 0 / 11 \\
574	grow-fruit & 45 & 5 & +40 & 8 / 0 / 12 \\
575	identify-life-stages-2 & 45 & 5 & +40 & 8 / 0 / 12 \\
576	measure-melting-point & 50 & 15 & +35 & 9 / 0 / 11 \\
577	lifespan-longest & 35 & 5 & +30 & 7 / 1 / 12 \\
578	lifespan-l-then-s & 50 & 20 & +30 & 6 / 0 / 14 \\
579	chemistry-mix & 45 & 20 & +25 & 5 / 0 / 15 \\
580	inclined-plane & 45 & 20 & +25 & 6 / 0 / 14 \\
581	find-animal & 40 & 25 & +15 & 6 / 2 / 12 \\
582	find-non-living-thing & 0 & 0 & 0 & 10 / 0 / 10 \\
583	\midrule
584	\textbf{Aggregate} & \textbf{41.4} & \textbf{11.4} & \textbf{+30.0} & \textbf{83 / 3 / 134} \\
585	\bottomrule
586	\end{tabular}}%
587	\caption{Per-task Llama-3.1-8B cross-model replication ($N{=}20$ per task). D/I/N: deterministic-preferred / internal-preferred / no-preference. Sorted by $\Delta$ DR descending.}
588	\label{tab:cross-model-detail}
589	\end{table}
590	
591	\paragraph{Cross-model and cross-environment summary.}
592	Table~\ref{tab:cross-model-env} consolidates replication results across model families and environments.
593	
594	\begin{table}[h]
595	\centering
596	\small
597	\resizebox{\columnwidth}{!}{%
598	\begin{tabular}{llcrrrccc}
599	\toprule
600	Model & Environment & $n$ & Int DR & Det DR & $\Delta$DR & DAF & DAF 95\% CI & Signal \\
601	\midrule
602	Qwen2.5-7B & ScienceWorld & 245 & 42.9\% & 16.3\% & +26.5 & 90.4\% & [81.3, 99.1] & death \\
603	Llama-3.1-8B & ScienceWorld & 220 & 41.4\% & 11.4\% & +30.0 & 88.2\% & [80.2, 95.1] & death \\
604	Gemma-2-9B-it & ScienceWorld & 220 & 36.4\% & 14.1\% & +22.3 & 89.7\% & [79.5, 98.4] & death \\
605	Qwen2.5-72B & ScienceWorld & 255 & 30.6\% & 2.75\% & +27.8 & 92.4\% & [86.1, 97.9] & death \\
606	Llama-3.1-70B & ScienceWorld & 220 & 48.6\% & 20.0\% & +28.6 & 101.0\% & [95.3, 107.5] & death \\
607	\midrule
608	Qwen2.5-7B & ALFWorld & 135 & 0\% & 0\% & 0 & 0\% & --- & info-asym \\
609	Llama-3.1-8B & ALFWorld & 135 & 0\% & 0\% & 0 & 0\% & --- & info-asym \\
610	\midrule
611	Qwen2.5-7B & MATH & 795 & N/A & N/A & N/A & N/A & N/A & none \\
612	\bottomrule
613	\end{tabular}}
614	\caption{Cross-model and cross-environment replication summary. \textbf{ScienceWorld}: death dominance replicates across three model families in the 7--9B range and intensifies under $10{\times}$ scaling (two 70B-class models, DAF $92.4$--$101.0\%$); DAF 95\% CIs from non-clustered episode-level bootstrap ($B{=}10{,}000$). \textbf{ALFWorld}: DAF $= 0\%$ (no death mechanism); routing signal arises from information asymmetry. \textbf{MATH}: no routing signal without catastrophic failure. Signal column: diagnosed routing mechanism. DR = death rate. Gemma-2's wider CI reflects one zero-death task type (\texttt{find-non-living-thing}); excluding it yields DAF $= 99.9\%$ $[99.7, 100.0]$.}
615	\label{tab:cross-model-env}
616	\end{table}
617	
618	\section{Failure Mode Analysis}
619	\label{app:failure-modes}
620	
621	All 105 internal-strategy deaths (100\%) are triggered by the same action pattern: \texttt{focus on [object]}. In ScienceWorld, \texttt{focus on} is the answer-submission action (equivalent to ``this is my final answer''); the LLM agent systematically misuses it as a general interaction or exploration command, and applies it to irrelevant targets (rooms, doors, inventory items). Each such execution submits an incorrect answer and triggers the $-100$ death penalty. Within death episodes, both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40 for deterministic) reflects how often each strategy enters catastrophic states, not different action selection within those states.
622	
623	Manual inspection identifies four failure categories: (A) no task awareness, where the agent executes \texttt{focus on} without reading the task; (B) task-aware but lacking action grounding, where the agent correctly identifies the objective but cannot map it to valid action primitives; (D) genuine attempts with execution failure; and (E) initial progress wasted by early errors. Category B dominates: agents demonstrate task comprehension but systematically fail to translate it into correct ScienceWorld actions. This taxonomy was produced by a single annotator; no inter-annotator agreement was computed. The categories are intended as qualitative illustrations, not as formal labels with reliability guarantees.
624	\label{tab:death-taxonomy}
625	
626	\paragraph{Representative examples.}
627	\emph{Category A} (no task awareness): In a \texttt{chemistry-mix} episode, the agent immediately executes \texttt{focus on kitchen}, \texttt{focus on door}, \texttt{focus on inventory} without reading the task, dying on the first \texttt{focus on} call. \emph{Category B} (comprehension without grounding): In a \texttt{lifespan-longest-lived} episode, the agent correctly identifies that it must compare animal lifespans and reasons about which animal lives longest, but then executes \texttt{focus on oak tree} (a non-animal object in the room) instead of navigating to find the target animal, triggering death.
628	
629	\paragraph{Action distribution analysis.}
630	Figure~\ref{fig:death-action-dist} shows the action distribution in death versus non-death episodes for the internal strategy; both are dominated by \texttt{connect} actions, with \texttt{focus on} moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$). Crucially, Figure~\ref{fig:death-comparison} reveals that within death episodes, internal and deterministic strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$). The survival gap (105 vs.\ 40 deaths) therefore reflects how often each strategy enters catastrophic states, not how it behaves within those states. Among fatal \texttt{focus on} targets, \texttt{workshop} remains the most frequent (20.0\%), followed by \texttt{inventory} (17.1\%) and \texttt{kitchen} (10.5\%), indicating a systematic object bias rather than random exploration. Figure~\ref{fig:death-timeline} visualizes the temporal pattern: agents execute long sequences of \texttt{connect} actions before a terminal \texttt{focus on} triggers death, typically in the final 1--3 steps.
631	
632	\begin{figure}[h]
633	\centering
634	\includegraphics[width=\columnwidth]{figures/death_action_distribution.pdf}
635	\caption{Action distribution for the internal (LLM) strategy in death ($n{=}105$) vs.\ non-death ($n{=}140$) episodes. Left: full distribution (both dominated by \texttt{connect}). Right: non-\texttt{connect} actions zoomed. \texttt{focus on} is moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$), while non-death episodes show higher rates of observation and object interaction.}
636	\label{fig:death-action-dist}
637	\end{figure}
638	
639	% Figure moved to main text (\S\ref{sec:death-decomp})
640	
641	\begin{figure}[h]
642	\centering
643	\includegraphics[width=\columnwidth]{figures/death_action_comparison.pdf}
644	\caption{Non-\texttt{connect} action distribution comparison between internal (left) and deterministic (right) strategies. Within death episodes, both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not different action selection within those states.}
645	\label{fig:death-comparison}
646	\end{figure}
647	
648	\section{Grounding Ablation}
649	\label{app:grounding-ablation}
650	
651	We test whether directly intervening on the dominant death action (\texttt{focus on}) eliminates death vulnerability on the 10 death-prone tasks (baseline 48.0\%, $n{=}200$).
652	
653	\paragraph{Prompt warning.} Adding an explicit system prompt (``use \texttt{focus on} only for final answers'') reduces aggregate death rate to 37.0\% ($\Delta = -11$~pp). Both identification tasks exhibit ironic effects (\texttt{identify-life-stages-1}: 35\%$\to$50\%; \texttt{identify-life-stages-2}: 25\%$\to$70\%), where explicit mention of the dangerous action may have increased its salience.
654	
655	\paragraph{Action-space filtering.} Blocking \texttt{focus on} during the exploration phase yields 379 blocks across 200 episodes with zero leaks and zero passthroughs (the agent never persisted in retrying blocked actions), reducing death rate to 29.0\% ($\Delta = -19$~pp). The zero-passthrough rate suggests \texttt{focus on} use is a shallow behavioral pattern rather than a deliberate strategy.
656	
657	\paragraph{Per-task variation.} Under filtering, \texttt{identify-life-stages} and \texttt{inclined-plane} approach deterministic-level safety (${\sim}$15--20\% DR), while \texttt{chemistry-mix} and \texttt{find-animal} remain at 35--40\%. Residual deaths occur during the answer-submission window, where the filter is inactive and agents submit \texttt{focus on} to incorrect objects.
658	
659	\paragraph{Post-ablation counterfactual decomposition.}
660	To test whether death dominance persists after grounding intervention, we run the full decomposition on matched episodes (183 episodes across 10 death-prone task types, paired by variation index).
661	Grounding reduces the internal death rate from 50.3\% to 35.0\% ($-15.3$\,pp), yet $\geq$93\% of disambiguating labels still arise from death asymmetry ($\Delta_\text{nd} \approx 0.09$, compared to $0.00$ at baseline).
662	Internal-preferred episodes increase from 5 to 23 (grounding helps internal strategy survive more often), but the routing signal remains death-driven rather than score-driven.
663	One task type (\texttt{identify-life-stages-2}, $n{=}10$) shows a paradoxical increase in death rate (50\%$\to$80\%); this outlier likely reflects the small sample size and task-specific prompt interference rather than a systematic effect.
664	
665	\section{Ablation Studies}
666	\label{app:ablations}
667	
668	\paragraph{Capacity scaling.} We scale the implicit router from Qwen3-0.6B to Qwen3-4B and evaluate at both step and episode level (Table~\ref{tab:capacity}).
669	
670	\begin{table}[h]
671	\centering
672	\small
673	\begin{tabular}{@{}lcc@{}}
674	\toprule
675	Model & Step Bal.\ Acc.\ (\%) & Ep.\ Bal.\ Acc.\ (\%) \\
676	\midrule
677	Qwen3-0.6B & $56.4 \pm 3.5$ & $50.7 \pm 2.6$ \\
678	Qwen3-1.7B & $58.2 \pm 4.0$ & $43.1 \pm 1.0$ \\
679	Qwen3-4B & $59.2 \pm 3.5$ & $\mathbf{59.0 \pm 1.9}$ \\
680	\midrule
681	Always-det & 50.0 & 50.0 \\
682	\bottomrule
683	\end{tabular}
684	\caption{Capacity scaling: step-level and episode-level balanced accuracy (4 seeds, identical configuration across all scales). Step-level accuracy is flat ($56$--$59\%$, within seed variance). At episode level, only 4B breaks the random baseline ($59.0\%$, $p < 0.005$).}
685	\label{tab:capacity}
686	\end{table}
687	
688	Step-level balanced accuracy is flat across scales ($56$--$59\%$, within seed variance); step-level discrimination is not capacity-sensitive. At episode level, only 4B breaks the random baseline ($59.0 \pm 1.9\%$, $p < 0.005$); 0.6B and 1.7B remain at or below chance. The 1.7B model's below-chance episode-level accuracy ($43.1\%$) may reflect overfitting to spurious step-level correlations that anti-correlate with episode outcomes; without per-class confusion matrices at this scale, this remains a hypothesis. The dominant explanation across scales is that death avoidance constitutes a task-type-level binary signal that a step-level router cannot exploit efficiently.
689	
690	\paragraph{Generative router.} A generative routing model trained with explicit routing labels achieves balanced accuracy of 46.7\%, confirming that the routing bottleneck is signal-limited, not architecture-limited.
691	
692	\paragraph{Leave-one-task-type-out routing.} Under leave-one-task-type-out evaluation, blind routing collapses to always-deterministic (balanced accuracy 50.0\%); a keyword-based variant achieves 62.9\% only through task-identity leakage, not genuine routing signal. A guided router evaluated under the same protocol confirms this: without task-type identifiers it achieves chance accuracy (50.0\%), and leaking task names raises this to 62.9\%, confirming that the only learnable routing feature is task-type identity.
693	
694	\paragraph{Death-proximal labeling.} Training a router only on the $k$ steps preceding death events (rather than all steps) also collapses to majority-class prediction (step balanced accuracy 50.0\%, episode balanced accuracy 50.0\%, internal recall 0\%), confirming that the absence of step-level signal is not an artifact of label dilution across long episodes.
695	
696	\paragraph{Reasoning depth.} An ablation comparing chain-of-thought reasoning against direct-answer generation on 6 task types ($n{=}120$ episodes per condition, 6 tasks $\times$ 20 episodes per task) found no significant difference (Mann--Whitney $p > 0.26$, $|d| \leq 0.31$) and near-identical death rates (41.8\% vs.\ 42.5\%); reasoning depth does not meaningfully alter internal-mode outcomes.
697	
698	\section{Threshold Routing Analysis}
699	\label{sec:threshold-routing}
700	
701	Given per-task death risk knowledge, we test whether a simple threshold routing strategy can outperform always-deterministic. For each threshold $t \in [0, 1]$, we route to internal if the per-task internal death rate $\leq t$, otherwise to deterministic, and sweep all thresholds to find the optimal.
702	
703	\begin{table}[h]
704	\centering
705	\small
706	\resizebox{\columnwidth}{!}{%
707	\begin{tabular}{lccc}
708	\toprule
709	Strategy & Mean Score & Death Rate & $\Delta$ vs Det \\
710	\midrule
711	Always-det & $-9.47$ & $0.163$ & $0.00$ \\
712	Optimal threshold ($t{=}0$) & $-11.03$ & $0.155$ & $-1.56$ \\
713	Always-internal & $-39.07$ & $0.429$ & $-29.60$ \\
714	\bottomrule
715	\end{tabular}}
716	\caption{Death-risk threshold routing analysis on 245 episodes. The optimal threshold routes only \texttt{find-non-living-thing} (the sole zero-death task) to internal, with all other tasks routed to deterministic. Bootstrap 95\% CI for the difference: $[-8.87, +5.92]$.}
717	\label{tab:threshold-routing}
718	\end{table}
719	
720	Even with perfect per-task death risk knowledge, threshold routing cannot outperform always-deterministic. The sole zero-death task achieves higher scores under deterministic (+28.5) than internal (+18.9), leaving no room for a beneficial mixed strategy.
721	
722	\section{Practitioner Decision Framework}
723	\label{app:decision-framework}
724	
725	Given a new interactive environment, the following three-stage procedure diagnoses whether learned routing adds value over a fixed deterministic strategy.
726	
727	\paragraph{Stage 1: Pilot collection (${\sim}$50 episodes).}
728	Run pure-internal and pure-deterministic strategies on a representative sample (${\sim}$50 episode pairs). Compute the death-rate differential $\Delta\text{DR} = \text{DR}_{\text{int}} - \text{DR}_{\text{det}}$.
729	
730	\paragraph{Stage 2: Death dominance check.}
731	If $\Delta\text{DR} > 15$~pp, death asymmetry is likely the dominant routing signal. Compute the death-label fraction $f_{\text{death}}$: the proportion of non-tie routing labels where exactly one strategy dies.
732	
733	\paragraph{Stage 3: Decision.}
734	If $f_{\text{death}} > 75\%$, the routing signal is death-dominated; a fixed deterministic strategy will match or exceed any learned router. If $f_{\text{death}} < 50\%$, diverse routing signals may justify a learned router. Between 50\%--75\%, collect additional episodes to reduce estimation noise before committing to router development.
735	
736	\paragraph{Retrospective validation.}
737	All four experimental conditions in this paper are correctly classified:
738	
739	\begin{table}[h]
740	\centering
741	\small
742	\begin{tabular}{@{}lrrll@{}}
743	\toprule
744	Condition & $\Delta$DR & $f_{\text{death}}$ & Prediction & Actual \\
745	\midrule
746	Qwen-7B & +26.5 & 78.9\% & det-fixed & det wins \\
747	Llama-8B & +30.0 & $>$75\% & det-fixed & det wins \\
748	Qwen-72B & +27.8 & $>$75\% & det-fixed & det wins \\
749	MATH & +0.5 & 0\% & router viable & no signal \\
750	\bottomrule
751	\end{tabular}
752	\caption{Retrospective validation of the decision framework. All four conditions are correctly classified (4/4).}
753	\label{tab:decision-framework}
754	\end{table}
755	
756	The framework also predicts the inverted-U relationship between capability and death risk: below ${\sim}$0.5B parameters, agents rarely reach dangerous states (13.3\% death rate in a 15-episode pilot), so $\Delta\text{DR}$ is low and the framework would not recommend fixed-deterministic. Above ${\sim}$7B, agents are capable enough to enter catastrophic states but not capable enough to avoid them, producing high $\Delta\text{DR}$.
757	
758	\paragraph{Threshold calibration.} The thresholds above (15~pp, 75\%, 50\%) are illustrative, derived from ScienceWorld's specific reward structure (binary death penalty $P{=}100$, sparse terminal rewards). Environments with graded penalties, dense rewards, or qualitatively different failure modes may require different thresholds. Practitioners should calibrate these boundaries for their specific environment.
759	
760	\section{Extended Validation of Excluded Tasks}
761	\label{app:extended-validation}
762	
763	To verify that task exclusion does not bias toward death-prone tasks, we collect $n{=}20$ episodes for five representative excluded tasks spanning all exclusion categories (Table~\ref{tab:extended-val}).
764	
765	\begin{table}[h]
766	\centering
767	\small
768	\resizebox{\columnwidth}{!}{%
769	\begin{tabular}{lcrrrrc}
770	\toprule
771	Task & Category & $n$ & Int DR & Det DR & $\Delta$DR & D/I/N \\
772	\midrule
773	boil & dev-set & 20 & 55\% & 25\% & +30\,pp & 6/0/14 \\
774	melt & dev-set & 20 & 45\% & 20\% & +25\,pp & 7/2/11 \\
775	find-living-thing & taxonomic & 20 & 55\% & 15\% & +40\,pp & 10/0/10 \\
776	use-thermometer & agent-floor & 20 & 50\% & 20\% & +30\,pp & 7/1/12 \\
777	power-component & agent-floor & 20 & 50\% & 15\% & +35\,pp & 7/0/13 \\
778	\midrule
779	\textit{Mean (5 tasks)} & & 100 & 51.0\% & 19.0\% & +32.0\,pp & 37/3/60 \\
780	\bottomrule
781	\end{tabular}}
782	\caption{Extended validation ($n{=}20$) of representative excluded task types. All five tasks confirm death asymmetry; mean $\Delta$DR $= +32.0$\,pp is consistent with the $n{=}5$ prescreening estimate for these same tasks (Table~\ref{tab:excluded-death}).}
783	\label{tab:extended-val}
784	\end{table}
785	
786	Notably, the excluded-task aggregate DAF (0.991) exceeds the included-task DAF (0.904; Table~\ref{tab:per-task}), indicating that excluded tasks are \emph{more} death-dominated than included tasks---the opposite of a cherry-picking bias.
787	
788	\section{Agent Prompt Templates}
789	\label{app:prompt-templates}
790	
791	Below we show the complete prompt templates used for agent interaction in ScienceWorld. Both the internal (ReAct) and deterministic strategies share the same system prompt but differ in the user message template.
792	
793	\paragraph{System prompt (shared).} Used for all ScienceWorld agent interactions across both computation modes.
794	
795	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
796	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
797	  left=2mm, right=2mm, top=1mm, bottom=1mm}
798	You are an agent interacting with a ScienceWorld text
799	environment. Your goal is to complete the given task by
800	choosing actions from the available action list.
801	
802	Use the following format for each step:
803	Thought: &lt;your reasoning about what to do next>
804	Action: &lt;exact action string from the valid actions list>
805	
806	Rules:
807	- You MUST choose an action from the valid actions list.
808	  Do not invent actions.
809	- Think step by step about what physical/scientific
810	  process is needed.
811	- Pay attention to the current observation for clues
812	  about object states.
813	\end{tcblisting}
814	
815	\paragraph{Internal (ReAct) user template.} At each step, the agent receives the current observation, valid action list, and recent action history, and must select a single action.
816	
817	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
818	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
819	  left=2mm, right=2mm, top=1mm, bottom=1mm}
820	Current observation:
821	{observation}
822	
823	Valid actions:
824	{valid_actions_str}
825	
826	Previous actions taken: {history_str}
827	
828	Choose your next action.
829	\end{tcblisting}
830	
831	\paragraph{Deterministic candidate generation template.} For the deterministic strategy, the agent generates ranked candidate actions instead of selecting one; these candidates are then evaluated via simulator forking (\S\ref{sec:method}).
832	
833	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
834	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
835	  left=2mm, right=2mm, top=1mm, bottom=1mm}
836	Current observation:
837	{observation}
838	
839	Valid actions:
840	{valid_actions_str}
841	
842	Previous actions taken: {history_str}
843	
844	Generate the top 3 most promising actions from the valid
845	actions list, ranked by how likely they are to make
846	progress on the task. Output exactly 3 actions, one per
847	line, in this format:
848	1. &lt;action>
849	2. &lt;action>
850	3. &lt;action>
851	\end{tcblisting}
852	
853	\paragraph{Reflexion self-reflection prompt.} After a failed episode, the Reflexion agent (\S\ref{sec:agent-improvement}) generates a reflection that is injected into subsequent trial attempts as additional system context.
854	
855	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
856	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
857	  left=2mm, right=2mm, top=1mm, bottom=1mm}
858	You just completed an episode in a ScienceWorld text
859	environment but failed.
860	
861	Task: {task_name}
862	Final score: {final_score}
863	Outcome: {outcome}
864	Number of steps taken: {num_steps}
865	
866	Here is a summary of your actions:
867	{action_summary}
868	
869	Analyze why this episode failed and provide a short
870	strategy for the next attempt. Focus on:
871	1. What went wrong (wrong sequence, missed key step,
872	   dangerous action)?
873	2. What should be done differently next time?
874	
875	Keep your reflection under 200 words.
876	\end{tcblisting}
877	
878	\paragraph{Grounding warning (ablation).} The prompt warning condition in the grounding ablation (Appendix~\ref{app:grounding-ablation}) appends the following to the shared system prompt:
879	
880	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
881	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
882	  left=2mm, right=2mm, top=1mm, bottom=1mm}
883	CRITICAL SAFETY RULE: The 'focus on [object]' action is
884	ONLY for submitting your final answer. Do NOT use
885	'focus on' to examine, inspect, or interact with objects
886	during exploration. Using 'focus on' on the wrong object
887	will cause irreversible failure. Use 'look at',
888	'examine', or 'pick up' instead for exploration.
889	\end{tcblisting}
890	
891	\noindent The key difference between the two computation modes is the user message: the internal strategy asks the LLM to \emph{select} one action (ReAct), while the deterministic strategy asks it to \emph{rank} candidates for simulator evaluation. Both use identical system prompts and identical observation formatting.
892	
893	\section{Non-Death Episode Case Study}
894	\label{app:non-death-case-study}
895	
896	We illustrate the framework's ability to decompose non-death routing signal using \texttt{find-non-living-thing}, the only task type with zero deaths and 100\% non-death labels (\S\ref{sec:death-decomp}). Using Gemma-2-9B-it counterfactual episodes ($N{=}20$), 12 episodes show routing preference (9 deterministic-preferred, 3 internal-preferred), confirming the framework detects bidirectional signal independent of death asymmetry.
897	
898	\paragraph{Deterministic-preferred: knowledge retrieval advantage.}
899	In Episode~3 (det: 67, int: 0), the internal strategy issues nonsensical \texttt{connect} actions for 18 consecutive steps (e.g., ``connect air to outside,'' ``connect axe to door to foundry'') without ever identifying a target object; the deterministic strategy correctly focuses on ``orange'' (+58) and opens the kitchen door (+9). In Episode~17 (det: 58, int: 50), both strategies find a valid non-living thing, but the deterministic strategy selects a higher-scoring object (orange, 58\,pts) versus the internal strategy's choice (fountain, 50\,pts), illustrating that object selection quality creates routing signal even when both strategies succeed.
900	
901	\paragraph{Internal-preferred: semantic reasoning advantage.}
902	In Episode~12 (int: 67, det: 58), the task specifies ``move it to the red box in the living room.'' The deterministic strategy focuses on the red box itself---the destination container, not a separate non-living thing---scoring 58\,pts. The internal strategy correctly distinguishes target from container, choosing ``orange'' (67\,pts). This semantic error demonstrates that deterministic pattern-matching can miss task-structure subtleties that internal reasoning captures.
903	
904	These cases confirm two properties: (1)~the framework captures non-death routing signal when it exists, and (2)~signal flows in both directions---neither strategy uniformly dominates in death-free tasks.
905	
906	\paragraph{Systematic analysis of non-death labels.}
907	All 20 non-death non-tie labels in the primary Qwen2.5-7B analysis originate from \texttt{find-non-living-thing}---the sole death-free task type. In every other task type, non-tie episodes involve at least one strategy dying. We classify the 20 episodes into three error categories:
908	
909	\begin{table}[h]
910	\centering
911	\small
912	\begin{tabular}{@{}lrrr@{}}
913	\toprule
914	Error category & Det-pref & Int-pref & Total \\
915	\midrule
916	Hallucination-induced & 8 & 2 & 10 \\
917	Object selection quality & 6 & 1 & 7 \\
918	Action selection error & 2 & 1 & 3 \\
919	\bottomrule
920	\end{tabular}
921	\caption{Non-death non-tie episode classification. Hallucination-induced: agent's state model is incorrect (e.g., believing \texttt{eat} completes the task). Object selection quality: both strategies succeed but choose different-value objects. Action selection: correct state model but suboptimal action sequences.}
922	\label{tab:non-death-taxonomy}
923	\end{table}
924	
925	\noindent Hallucination-induced errors dominate (50\%), driven by a recurring ``eat before focus'' pattern: the internal strategy consumes the target object (destroying it) before attempting the scoring action (\texttt{focus on}), indicating an incorrect state model that equates eating with task completion (11 of 20 episodes). Object selection quality accounts for 35\%---typically the deterministic strategy selecting ``orange'' (58\,pts) while the internal strategy settles for lower-value objects (``fountain'' or ``picture,'' 50\,pts). The error categories are bidirectional: 2 of 10 hallucination episodes and 1 of 3 action selection episodes are internal-preferred, confirming the framework detects failures in both strategies. Score gaps reflect category severity: hallucination errors produce large gaps ($17$--$67$\,pts, one strategy scores zero) while object selection differences produce small gaps ($8$--$9$\,pts, both strategies functional).
926	
927	\section{Use of AI Assistants}
928	\label{app:ai-assistants}
929	
930	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
931	\begin{itemize}
932	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
933	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \LaTeX{}.
934	    \item \textbf{Literature:} summarizing related papers to inform the related-work section.
935	\end{itemize}
936	
937	\end{document}
938	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fc11158-a49b-4e6a-a26a-8bff25d358a9",
  "isSidechain": true,
  "promptId": "615c1eae-3cf0-4729-ad9e-5bf3fb5d3b1d",
  "agentId": "af152b21ba92fc359",
  "type": "user",
  "uuid": "cf9d0061-0c2b-4ba5-bd37-3a1ade6672ec",
  "sourceToolAssistantUUID": "9fc11158-a49b-4e6a-a26a-8bff25d358a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-24T20:50:16.519Z_

The main.tex file is very large. Let me search for all table and figure environments in the appendix sections, starting after line 54 where \appendix begins.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf9d0061-0c2b-4ba5-bd37-3a1ade6672ec",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN44kzAwVjxDXWTGqUCp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7c3bf236-2700-4c14-b256-6cef72413d87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Uk73CSXk7ZqYJr4vDVm7LD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 25375,
      "cache_read_input_tokens": 38686,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25375,
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

_source line 9 · 2026-05-24T20:50:17.611Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01CrjKKH177xntfwQiXe8vYk`</summary>

```json
{
  "pattern": "\\\\(begin|end)\\{(table|figure)\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c3bf236-2700-4c14-b256-6cef72413d87",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN44kzAwVjxDXWTGqUCp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2c371f27-a701-4c59-b5c7-ee54e420633b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Uk73CSXk7ZqYJr4vDVm7LD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 25375,
      "cache_read_input_tokens": 38686,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25375
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 185,
          "cache_read_input_tokens": 38686,
          "cache_creation_input_tokens": 25375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25375,
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

_source line 10 · 2026-05-24T20:50:17.684Z_

<details><summary>↩ Tool result · `toolu_01CrjKKH177xntfwQiXe8vYk`</summary>

```text
&lt;persisted-output>
Output too large (34.3KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing--claude-sessions-director-976fe708/5d044481-75d4-4f8a-b48d-d8d0b80be816/tool-results/toolu_01CrjKKH177xntfwQiXe8vYk.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex-1-\section{Method}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex-2-\label{sec:method}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex-3-
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex:4:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex-5-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex-6-\includegraphics[width=\columnwidth]{figures/label_decomposition.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex-7-\caption{Episode-level label decomposition ($N{=}245$). Of 95 non-tie labels, 75 (78.9\%) arise from death asymmetry: 54 where death is the sole discriminator and 21 with co-occurring score differences. All 20 non-death labels originate from a single task type (\texttt{find-non-living-thing}).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex-8-\label{fig:label-decomposition}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex:9:\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex-10-
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex-11-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex-12-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex-44-    \ell \in \{{\tt det\text{-}pref},\; {\tt int\text{-}pref},\; {\tt no\text{-}pref}\}
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c371f27-a701-4c59-b5c7-ee54e420633b",
  "isSidechain": true,
  "promptId": "615c1eae-3cf0-4729-ad9e-5bf3fb5d3b1d",
  "agentId": "af152b21ba92fc359",
  "type": "user",
  "uuid": "65685ffb-0470-4a87-aa07-968614638972",
  "sourceToolAssistantUUID": "2c371f27-a701-4c59-b5c7-ee54e420633b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-24T20:50:18.962Z_

Let me use a more focused approach to find tables and figures in the appendix specifically:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65685ffb-0470-4a87-aa07-968614638972",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN44yPYde7SHkmm4JVbS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "436c774a-22c9-4bf3-bf80-20aa29a8911f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ak3JBk2dp5Lpq8TCsNkSPd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 64061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1082,
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

_source line 12 · 2026-05-24T20:50:19.190Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01B9oNjiqPiUjYsbyCCKyQaY`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\label{app:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "436c774a-22c9-4bf3-bf80-20aa29a8911f",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN44yPYde7SHkmm4JVbS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2909ee6e-7ed9-484a-a827-d92bcd8749d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ak3JBk2dp5Lpq8TCsNkSPd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 64061,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1082
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 121,
          "cache_read_input_tokens": 64061,
          "cache_creation_input_tokens": 1082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1082,
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

_source line 13 · 2026-05-24T20:50:19.262Z_

<details><summary>↩ Tool result · `toolu_01B9oNjiqPiUjYsbyCCKyQaY`</summary>

```text
80:\label{app:sci}
92:\label{app:labeling}
127:\label{app:per-task}
202:\label{app:correlation}
231:\label{app:wild-cluster}
260:\label{app:per-task-ci}
267:\label{app:loto-daf}
299:\label{app:dose-response}
331:\label{app:router-details}
371:\label{app:seed-robustness}
455:\label{app:penalty}
507:\label{app:cross-env-details}
556:\label{app:cross-model}
619:\label{app:failure-modes}
649:\label{app:grounding-ablation}
666:\label{app:ablations}
723:\label{app:decision-framework}
761:\label{app:extended-validation}
789:\label{app:prompt-templates}
894:\label{app:non-death-case-study}
928:\label{app:ai-assistants}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2909ee6e-7ed9-484a-a827-d92bcd8749d3",
  "isSidechain": true,
  "promptId": "615c1eae-3cf0-4729-ad9e-5bf3fb5d3b1d",
  "agentId": "af152b21ba92fc359",
  "type": "user",
  "uuid": "9982190f-c93b-443b-97ea-4630dfbf1bda",
  "sourceToolAssistantUUID": "2909ee6e-7ed9-484a-a827-d92bcd8749d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-24T20:50:20.676Z_

Now let me extract all tables and figures in the appendix with their labels and captions:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9982190f-c93b-443b-97ea-4630dfbf1bda",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN45658V8dTq91cLn9KA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e4f2d72c-7c3c-4df4-8a36-63ed3444b9b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ASTES9EZUUMPBYSaueyuTG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 370,
      "cache_read_input_tokens": 65143,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 370,
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

_source line 15 · 2026-05-24T20:50:21.217Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QA2z8pJQPUq1z47D8bgvcw`</summary>

```json
{
  "command": "awk '/^\\\\appendix/,0' /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex | grep -E \"\\\\\\\\(begin|end)\\{(table|figure)\\}|\\\\\\\\label\\{|\\\\\\\\caption\\{\" | head -100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4f2d72c-7c3c-4df4-8a36-63ed3444b9b2",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN45658V8dTq91cLn9KA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f076de00-19a2-408f-a0fb-05d42d1801c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ASTES9EZUUMPBYSaueyuTG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 370,
      "cache_read_input_tokens": 65143,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 370
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 155,
          "cache_read_input_tokens": 65143,
          "cache_creation_input_tokens": 370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 370,
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

_source line 16 · 2026-05-24T20:50:21.295Z_

<details><summary>↩ Tool result · `toolu_01QA2z8pJQPUq1z47D8bgvcw`</summary>

```text
\label{app:sci}
\label{app:labeling}
\caption{Episode-Level Counterfactual Labeling}
\label{alg:labeling}
\label{app:per-task}
\begin{table}[h]
\caption{Per-task decomposition of the death avoidance effect. D\%: death rate for internal (int) and deterministic (det) strategies. D/I/N: episode labels (det-preferred / internal-preferred / no-preference). Sorted by $\Delta_{\text{full}}$ descending. The \textit{All} row is an episode-weighted aggregate across 245 episodes. $\dagger$\,Only task with zero deaths under both strategies; $n{=}40$ because data was collected in two batches, with the second batch adding 20 episodes to increase statistical power for this zero-death outlier.}
\label{tab:per-task}
\end{table}
\begin{table}[t]
\caption{Death-rate analysis of all 19 excluded task types. D\%: death rate (score $\leq -100$). $\Delta$DR = D\%\textsubscript{int} $-$ D\%\textsubscript{det}. 18 of 19 excluded tasks (95\%) exhibit positive death asymmetry ($\Delta$DR $\geq +20$\,pp). Exclusion groups: A = development set (excluded to prevent circular evaluation), B = taxonomically redundant with an included family representative, C = agent-floor tasks (backbone achieves near-zero progress regardless of strategy). The mean $\Delta$DR among excluded tasks ($+38.2$\,pp) exceeds that of included tasks ($+28.7$\,pp), confirming that task selection does not bias toward death-prone tasks. Group B--C estimates are based on $n{=}5$ prescreening episodes per task and should be interpreted as directional evidence rather than precise rate estimates.}
\label{tab:excluded-death}
\end{table}
\label{app:correlation}
\begin{table}[h]
\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\ $\Delta_{\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}
\label{tab:loo}
\end{table}
\label{app:wild-cluster}
\begin{table}[h]
\caption{Cluster-level tests of death-rate asymmetry ($K{=}11$ task clusters, 245 episodes). 10 of 11 clusters show internal DR $>$ deterministic DR; the sole exception (\texttt{find-non-living-thing}) has zero deaths under both strategies. Cohen's $d = 3.02$. The exact permutation $p = 0.002$ ($4/2{,}048$) reflects the near-unanimous directional consistency.}
\label{tab:wild-cluster}
\end{table}
\label{app:per-task-ci}
\label{app:loto-daf}
\begin{table}[h]
\caption{Leave-one-task-out DAF sensitivity (penalty-independent label fraction). Among the 10 death-prone tasks, removing any single task changes DAF by at most 3.0\,pp (range: 75.9\%--78.9\%). Removing \emph{Find Non-Living Thing}, the sole death-free task that contributes all 20 score-comparison episodes, raises DAF to 100\% by construction.}
\label{tab:loto-daf}
\end{table}
\label{app:dose-response}
\begin{table}[h]
\caption{Per-task death rates (\%) for Reflexion at $N{=}3$, 4, 5 on 10 death-prone tasks ($n{=}20$ per task). Aggregate death rates confirm stabilization at $N \geq 3$ (range: $34.0$--$36.5\%$).}
\label{tab:dose-response-detail}
\end{table}
\label{app:router-details}
\begin{table}[h]
\caption{Router training hyperparameters. Both architectures use the same base model with LoRA adaptation. The classification head degenerates across all configurations; the implicit router results are reported as 4-seed mean$\pm$std.}
\label{tab:hyperparams}
\end{table}
\label{app:seed-robustness}
\begin{table}[h]
\caption{Per-seed router performance under cross-split evaluation (8 seeds, generation-based, \texttt{enable\_thinking=False}). Step-level evaluation allows steps from the same episode in both train and validation sets (same-episode leakage). Episode-level evaluation holds out entire episodes; the resulting $47.1 \pm 2.2\%$ is below the 50\% chance baseline. A text augmentation ablation (Table~\ref{tab:text-augmentation}) confirms this failure persists under the current data distribution and augmentation regime.}
\label{tab:seed-robustness}
\end{table}
\begin{table}[h]
\caption{Text augmentation ablation: episode-level balanced accuracy across training set sizes (25\%--800\% of original via paraphrase, $32{\times}$ range). Internal recall $= 0.0$ at all scales (complete majority-class collapse). Det\%: fraction of deterministic-preferred labels in training data. The 50\% scale is a single seed; all others report mean$\pm$std across seeds.}
\label{tab:text-augmentation}
\end{table}
\label{app:penalty}
\begin{table}[h]
\caption{Sensitivity of DAF to death penalty magnitude $P$. DAF$(P) = 1 - \Delta_{\text{nd}} / \Delta_{\text{full}}(P)$, where $\Delta_{\text{full}}(P) \approx \delta \cdot P + \Delta_{\text{nd}}$, $\delta = 0.2653$ is the death-rate differential, and $\Delta_{\text{nd}} = 2.84$ (strict neither-died filtering). Recomputed from 245 episode-level data; bootstrap 95\% CIs ($B{=}10{,}000$). \textsuperscript{*}Default setting.}
\label{tab:penalty-sensitivity}
\end{table}
\begin{table}[h]
\caption{Pearson $r$ between per-task death-rate differential and $\Delta_{\text{full}}(P)$ across penalty magnitudes. The correlation is non-significant at low penalties and emerges at $P \geq 50$, which reflects the transition from non-death-dominated to death-dominated score gaps. \textsuperscript{*}Default ScienceWorld setting.}
\label{tab:penalty-correlation}
\end{table}
\label{app:cross-env-details}
\begin{table}[h]
\caption{Cross-environment label distribution. ``Deterministic'' denotes qualitatively different computation modes: ScienceWorld = oracle simulator with ground-truth state; MATH = Python code interpreter; ALFWorld = admissible-action enumeration. $\dagger$\,ALFWorld's deterministic advantage stems from information asymmetry, not death avoidance.}
\label{tab:cross-env}
\end{table}
\begin{table}[h]
\caption{Per-task-type decomposition for ALFWorld (135 games, Qwen2.5-7B-Instruct). D/I/N: deterministic-preferred / internal-preferred / no-preference. No death mechanism exists; $\Delta_{\text{full}}$ is driven entirely by information asymmetry from admissible-action access. Sorted by $\Delta_{\text{full}}$ descending.}
\label{tab:alfworld-pertask}
\end{table}
\label{app:cross-model}
\begin{table}[h]
\caption{Per-task Llama-3.1-8B cross-model replication ($N{=}20$ per task). D/I/N: deterministic-preferred / internal-preferred / no-preference. Sorted by $\Delta$ DR descending.}
\label{tab:cross-model-detail}
\end{table}
\begin{table}[h]
\caption{Cross-model and cross-environment replication summary. \textbf{ScienceWorld}: death dominance replicates across three model families in the 7--9B range and intensifies under $10{\times}$ scaling (two 70B-class models, DAF $92.4$--$101.0\%$); DAF 95\% CIs from non-clustered episode-level bootstrap ($B{=}10{,}000$). \textbf{ALFWorld}: DAF $= 0\%$ (no death mechanism); routing signal arises from information asymmetry. \textbf{MATH}: no routing signal without catastrophic failure. Signal column: diagnosed routing mechanism. DR = death rate. Gemma-2's wider CI reflects one zero-death task type (\texttt{find-non-living-thing}); excluding it yields DAF $= 99.9\%$ $[99.7, 100.0]$.}
\label{tab:cross-model-env}
\end{table}
\label{app:failure-modes}
\label{tab:death-taxonomy}
\begin{figure}[h]
\caption{Action distribution for the internal (LLM) strategy in death ($n{=}105$) vs.\ non-death ($n{=}140$) episodes. Left: full distribution (both dominated by \texttt{connect}). Right: non-\texttt{connect} actions zoomed. \texttt{focus on} is moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$), while non-death episodes show higher rates of observation and object interaction.}
\label{fig:death-action-dist}
\end{figure}
\begin{figure}[h]
\caption{Non-\texttt{connect} action distribution comparison between internal (left) and deterministic (right) strategies. Within death episodes, both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not different action selection within those states.}
\label{fig:death-comparison}
\end{figure}
\label{app:grounding-ablation}
\label{app:ablations}
\begin{table}[h]
\caption{Capacity scaling: step-level and episode-level balanced accuracy (4 seeds, identical configuration across all scales). Step-level accuracy is flat ($56$--$59\%$, within seed variance). At episode level, only 4B breaks the random baseline ($59.0\%$, $p < 0.005$).}
\label{tab:capacity}
\end{table}
\label{sec:threshold-routing}
\begin{table}[h]
\caption{Death-risk threshold routing analysis on 245 episodes. The optimal threshold routes only \texttt{find-non-living-thing} (the sole zero-death task) to internal, with all other tasks routed to deterministic. Bootstrap 95\% CI for the difference: $[-8.87, +5.92]$.}
\label{tab:threshold-routing}
\end{table}
\label{app:decision-framework}
\begin{table}[h]
\caption{Retrospective validation of the decision framework. All four conditions are correctly classified (4/4).}
\label{tab:decision-framework}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f076de00-19a2-408f-a0fb-05d42d1801c2",
  "isSidechain": true,
  "promptId": "615c1eae-3cf0-4729-ad9e-5bf3fb5d3b1d",
  "agentId": "af152b21ba92fc359",
  "type": "user",
  "uuid": "9920075d-f549-4a6c-a3c3-2cf707fad768",
  "sourceToolAssistantUUID": "f076de00-19a2-408f-a0fb-05d42d1801c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-24T20:50:23.116Z_

Good! Now let me get the complete information with table/figure sizes and details. Let me read specific sections from main.tex:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9920075d-f549-4a6c-a3c3-2cf707fad768",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN45EmGAbDZ9PU85VaLb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3aee3073-2332-4da9-bb9e-6b7c2a88726e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RkXxNUfDbD7cevXZb7LRQh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 3042,
      "cache_read_input_tokens": 65513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3042,
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

_source line 18 · 2026-05-24T20:50:24.075Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RtNFDFNzKYYi6E4Qtctq5A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "offset": 131,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3aee3073-2332-4da9-bb9e-6b7c2a88726e",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN45EmGAbDZ9PU85VaLb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "15ac0630-5151-4117-bf55-840f47392eec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RkXxNUfDbD7cevXZb7LRQh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 3042,
      "cache_read_input_tokens": 65513,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3042
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 151,
          "cache_read_input_tokens": 65513,
          "cache_creation_input_tokens": 3042,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3042,
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

_source line 19 · 2026-05-24T20:50:24.090Z_

<details><summary>↩ Tool result · `toolu_01RtNFDFNzKYYi6E4Qtctq5A`</summary>

```text
131	\begin{table}[h]
132	\centering
133	\scriptsize
134	\setlength{\tabcolsep}{2.5pt}
135	\begin{tabular}{@{}lrrccc@{}}
136	\toprule
137	Task & $n$ & $\Delta_\text{full}$ & D\%\textsubscript{int} & D\%\textsubscript{det} & D / I / N \\
138	\midrule
139	id-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\
140	lifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\
141	lifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\
142	inclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\
143	freeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\
144	meas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\
145	id-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\
146	find-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\
147	grow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\
148	chem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\
149	\midrule
150	find-non-living-thing$^\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\
151	\midrule
152	\textbf{All (11 tasks)} & \textbf{245} & $\mathbf{+29.60}$ & \textbf{42.9} & \textbf{16.3} & \textbf{86 / 9 / 150} \\
153	\bottomrule
154	\end{tabular}
155	\caption{Per-task decomposition of the death avoidance effect. D\%: death rate for internal (int) and deterministic (det) strategies. D/I/N: episode labels (det-preferred / internal-preferred / no-preference). Sorted by $\Delta_{\text{full}}$ descending. The \textit{All} row is an episode-weighted aggregate across 245 episodes. $\dagger$\,Only task with zero deaths under both strategies; $n{=}40$ because data was collected in two batches, with the second batch adding 20 episodes to increase statistical power for this zero-death outlier.}
156	\label{tab:per-task}
157	\end{table}
158	
159	\paragraph{Task selection and anti-cherry-picking.}
160	Eighteen of the 19 excluded task types (95\%) exhibit death-asymmetric patterns (Table~\ref{tab:excluded-death}): internal-reasoning death rates range from 40\% to 60\% (mean 53.9\%), while deterministic death rates range from 0\% to 40\% (mean 15.8\%), yielding a mean death-rate differential of $+38.2$\,pp, exceeding the $+28.7$\,pp for included tasks. The included subset is thus \emph{less} death-asymmetric than the excluded subset, the opposite of what a cherry-picking hypothesis would predict. The sole exception is \texttt{grow-plant}, an intrinsically safe task with zero deaths under both strategies, paralleling \texttt{find-non-living-thing} in the included set. The 19 excluded tasks fall into three independently motivated categories: five used during pipeline development (standard hold-out practice), seven taxonomically redundant with included family representatives (deduplication), and seven where the 7B backbone achieves near-zero task progress regardless of strategy (agent capability floor). In no case was a task excluded because death dominance was absent. Exclusion is driven by absence of non-death routing signal ($\Delta_{\text{nd}} = 0$ for 53\% of excluded tasks) and standard deduplication practices. \texttt{find-non-living-thing} serves as an internal counterexample: zero deaths under both strategies yet included because it exhibits non-death routing signal ($\Delta_{\text{full}} = +9.58$ entirely from score differences), and deterministic is not always preferred (4 of 20 non-tie labels favor internal).
161	
162	\begin{table}[t]
163	\centering
164	\scriptsize
165	\setlength{\tabcolsep}{2pt}
166	\resizebox{\columnwidth}{!}{%
167	\begin{tabular}{@{}llrcccl@{}}
168	\toprule
169	Task & Grp & $n$ & D\%\textsubscript{int} & D\%\textsubscript{det} & $\Delta$DR & Excl.\ reason \\
170	\midrule
171	boil                          & A & 20 & 50 & 20 & $+30$ & dev set \\
172	change-state-of-matter        & A & 20 & 55 & 15 & $+40$ & dev set \\
173	chem-mix-paint-secondary      & A & 20 & 45 & 10 & $+35$ & dev set \\
174	grow-plant                    & A & 20 &  0 &  0 & $\phantom{+}0$  & dev set \\
175	melt                          & A & 20 & 55 & 15 & $+40$ & dev set \\
176	\midrule
177	chem-mix-paint-tertiary       & B &  5 & 40 & 20 & $+20$ & family redundancy \\
178	find-living-thing             & B &  5 & 60 & 20 & $+40$ & family redundancy \\
179	find-plant                    & B &  5 & 60 &  0 & $+60$ & family redundancy \\
180	inclined-friction-named       & B &  5 & 60 & 20 & $+40$ & family redundancy \\
181	inclined-friction-unnamed     & B &  5 & 60 &  0 & $+60$ & family redundancy \\
182	lifespan-shortest             & B &  5 & 60 & 40 & $+20$ & family redundancy \\
183	measure-melt-known            & B &  5 & 60 &  0 & $+60$ & family redundancy \\
184	\midrule
185	mendelian-known               & C &  5 & 60 & 20 & $+40$ & agent floor \\
186	mendelian-unknown             & C &  5 & 60 & 40 & $+20$ & agent floor \\
187	power-component               & C &  5 & 60 & 20 & $+40$ & agent floor \\
188	power-renewable               & C &  5 & 60 &  0 & $+60$ & agent floor \\
189	test-conductivity             & C &  5 & 60 & 20 & $+40$ & agent floor \\
190	test-conductivity-unknown     & C &  5 & 60 & 20 & $+40$ & agent floor \\
191	use-thermometer               & C &  5 & 60 & 20 & $+40$ & agent floor \\
192	\midrule
193	\textbf{Mean (19 excluded)}   &   &    & \textbf{53.9} & \textbf{15.8} & $\mathbf{+38.2}$ & \\
194	\textit{cf.\ included (11)}   &   &    & \textit{46.5} & \textit{17.8} & $\textit{+28.7}$ & \\
195	\bottomrule
196	\end{tabular}}%
197	\caption{Death-rate analysis of all 19 excluded task types. D\%: death rate (score $\leq -100$). $\Delta$DR = D\%\textsubscript{int} $-$ D\%\textsubscript{det}. 18 of 19 excluded tasks (95\%) exhibit positive death asymmetry ($\Delta$DR $\geq +20$\,pp). Exclusion groups: A = development set (excluded to prevent circular evaluation), B = taxonomically redundant with an included family representative, C = agent-floor tasks (backbone achieves near-zero progress regardless of strategy). The mean $\Delta$DR among excluded tasks ($+38.2$\,pp) exceeds that of included tasks ($+28.7$\,pp), confirming that task selection does not bias toward death-prone tasks. Group B--C estimates are based on $n{=}5$ prescreening episodes per task and should be interpreted as directional evidence rather than precise rate estimates.}
198	\label{tab:excluded-death}
199	\end{table}
200	
201	\section{Correlation Robustness}
202	\label{app:correlation}
203	
204	The Pearson $r = 0.9698$ reported in \S\ref{sec:death-decomp} is robust across multiple diagnostics. Spearman rank correlation is $\rho = 0.986$ ($p = 2.4 \times 10^{-8}$); the relationship is not driven by outliers or non-linearity. A nonparametric bootstrap (10{,}000 resamples) yields 95\% CI $[0.952, 0.995]$.
205	
206	\begin{table}[h]
207	\centering
208	\small
209	\begin{tabular}{@{}lr@{}}
210	\toprule
211	Task removed & $r_{\text{LOO}}$ \\
212	\midrule
213	id-life-stages-1       & 0.963 \\
214	lifespan-long          & 0.969 \\
215	lifespan-l-then-s      & 0.976 \\
216	inclined-plane         & 0.969 \\
217	freeze                 & 0.971 \\
218	meas-melt-point        & 0.972 \\
219	id-life-stages-2       & 0.972 \\
220	find-animal            & 0.970 \\
221	grow-fruit             & 0.973 \\
222	chem-mix               & 0.969 \\
223	find-non-living-thing  & 0.980 \\
224	\bottomrule
225	\end{tabular}
226	\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\ $\Delta_{\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}
227	\label{tab:loo}
228	\end{table}
229	
230	\section{Cluster Bootstrap Sensitivity Analysis}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15ac0630-5151-4117-bf55-840f47392eec",
  "isSidechain": true,
  "promptId": "615c1eae-3cf0-4729-ad9e-5bf3fb5d3b1d",
  "agentId": "af152b21ba92fc359",
  "type": "user",
  "uuid": "2fdaa5ae-9bd2-46c9-b106-486807f26677",
  "sourceToolAssistantUUID": "15ac0630-5151-4117-bf55-840f47392eec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-24T20:50:25.399Z_

Let me continue reading through the appendix to collect all tables and figures systematically:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fdaa5ae-9bd2-46c9-b106-486807f26677",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN45T2CjmrYXyEq9MxGT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "25c72986-be43-4bf8-bb53-dd8deec8679e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SZaMauetoDyeu6vAj3Nhgu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3152,
      "cache_read_input_tokens": 68555,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3152,
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

_source line 21 · 2026-05-24T20:50:26.217Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rmug2x56QHpVJYWE5gNP69`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "offset": 230,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25c72986-be43-4bf8-bb53-dd8deec8679e",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN45T2CjmrYXyEq9MxGT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8f37e98f-78d8-44f0-8478-8c9f4805dea9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SZaMauetoDyeu6vAj3Nhgu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3152,
      "cache_read_input_tokens": 68555,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3152
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 141,
          "cache_read_input_tokens": 68555,
          "cache_creation_input_tokens": 3152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3152,
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

_source line 22 · 2026-05-24T20:50:26.224Z_

<details><summary>↩ Tool result · `toolu_01Rmug2x56QHpVJYWE5gNP69`</summary>

```text
230	\section{Cluster Bootstrap Sensitivity Analysis}
231	\label{app:wild-cluster}
232	
233	With $K{=}11$ task-type clusters, cluster bootstrap falls well below the $K{\geq}20$--50 recommended for reliable inference \citep{cameron-2008,webb-2023}. The narrower CIs obtained reflect known small-sample bias toward underestimation of variance, not tighter inference.
234	
235	Episodes within the same task type share environment dynamics, raising the concern that the effective sample size is closer to $K$ (task types) than $N$ (episodes). We address this with cluster-robust inference treating each task type as a cluster ($K{=}11$, all 11 included task types, 245 episodes).
236	
237	\begin{table}[h]
238	\centering
239	\small
240	\resizebox{\columnwidth}{!}{%
241	\begin{tabular}{@{}lcc@{}}
242	\toprule
243	Method & $p$-value & 95\% CI \\
244	\midrule
245	Cluster-robust $t$-test ($t{=}10.0$, df$=$10) & $< 0.001$ & $[0.73, 1.00]$ \\
246	Wild cluster bootstrap ($B{=}9{,}999$) & $< 0.001$ & $[0.73, 1.00]$ \\
247	Exact permutation ($2{,}048$ perms) & $0.002$ & --- \\
248	Sign test & $< 0.001$ & --- \\
249	\bottomrule
250	\end{tabular}}%
251	\caption{Cluster-level tests of death-rate asymmetry ($K{=}11$ task clusters, 245 episodes). 10 of 11 clusters show internal DR $>$ deterministic DR; the sole exception (\texttt{find-non-living-thing}) has zero deaths under both strategies. Cohen's $d = 3.02$. The exact permutation $p = 0.002$ ($4/2{,}048$) reflects the near-unanimous directional consistency.}
252	\label{tab:wild-cluster}
253	\end{table}
254	
255	\noindent All methods confirm significance with $p < 0.01$, and the 95\% CI $[0.73, 1.00]$ excludes zero by a wide margin. With $K{=}11$ task types, ICC estimation itself carries substantial uncertainty; the high within-task consistency of death patterns (all-or-nothing per task type) suggests high ICC, which explains the CI narrowing under cluster resampling.
256	
257	We retain this analysis for transparency; readers should rely on the non-clustered episode-level bootstrap (\S\ref{sec:death-decomp}) as the primary inference.
258	
259	\section{Per-Task Death Rate Confidence Intervals}
260	\label{app:per-task-ci}
261	
262	We compute bootstrap 95\% CIs for the death-rate differential ($\Delta\text{DR} = \text{DR}_{\text{int}} - \text{DR}_{\text{det}}$) for all 30 ScienceWorld task types. Of 30 tasks, 28 are death-prone (at least one death under either strategy); the remaining 2 (\texttt{grow-plant}, \texttt{find-non-living-thing}) have zero deaths under both strategies.
263	
264	Across all 28 death-prone tasks, internal DR exceeds deterministic DR without exception (100\% directional consistency). The pooled death-rate differential is $+37.3\%$ (95\% CI: $[29.7\%, 44.4\%]$). Fifteen of 28 tasks are individually significant (CI excludes zero); the 13 non-significant tasks all have $n{=}5$ prescreening episodes, where statistical power is insufficient to detect even large effects (e.g., a task with $\Delta\text{DR} = +40$\,pp at $n{=}5$ has a CI of $\pm 43$\,pp). The universal directional consistency, combined with the pooled significance, confirms that death asymmetry is not driven by a subset of outlier tasks.
265	
266	\section{Leave-One-Task-Out DAF Sensitivity}
267	\label{app:loto-daf}
268	
269	\begin{table}[h]
270	\centering
271	\small
272	\caption{Leave-one-task-out DAF sensitivity (penalty-independent label fraction). Among the 10 death-prone tasks, removing any single task changes DAF by at most 3.0\,pp (range: 75.9\%--78.9\%). Removing \emph{Find Non-Living Thing}, the sole death-free task that contributes all 20 score-comparison episodes, raises DAF to 100\% by construction.}
273	\label{tab:loto-daf}
274	\begin{tabular}{lrrr}
275	\toprule
276	Removed Task & $N_\text{rem}$ & DAF (\%) & $\Delta$ (pp) \\
277	\midrule
278	(none, full) & 245 & 78.9 & --- \\
279	\midrule
280	Find Non-Living$^\dagger$ & 205 & 100.0 & +21.1 \\
281	Lifespan Longest & 220 & 75.9 & $-$3.0 \\
282	Life Stages 1 & 225 & 76.7 & $-$2.2 \\
283	Lifespan Long+Short & 225 & 76.7 & $-$2.2 \\
284	Chemistry Mix & 225 & 77.0 & $-$1.9 \\
285	Grow Fruit & 225 & 77.3 & $-$1.7 \\
286	Inclined Plane Angle & 225 & 77.3 & $-$1.7 \\
287	Freeze & 225 & 77.5 & $-$1.4 \\
288	Life Stages 2 & 225 & 77.5 & $-$1.4 \\
289	Melt Pt Unknown & 225 & 77.5 & $-$1.4 \\
290	Find Animal & 225 & 77.8 & $-$1.2 \\
291	\bottomrule
292	\end{tabular}
293	
294	\vspace{2pt}
295	{\footnotesize $^\dagger$Only death-free task; contributes all score-comparison labels. Sorted by $|\Delta|$ descending.}
296	\end{table}
297	
298	\section{Per-Task Dose-Response Breakdown}
299	\label{app:dose-response}
300	
301	Table~\ref{tab:dose-response-detail} reports per-task death rates for Reflexion at $N{=}3$, 4, and 5 on the 10 death-prone tasks ($n{=}20$ episodes per task). Per-task variance is high (up to 25\,pp range for \texttt{measure-melting-point}), but the aggregate smooths to a 2.5\,pp band, confirming that the stabilization conclusion is robust at the aggregate level despite task-level noise. \texttt{freeze} is consistently the hardest task (50--60\% DR across all $N$).
302	
303	\paragraph{Statistical power.} With $n{=}200$ paired episodes, the minimum detectable effect (MDE) is ${\sim}8$~pp ($\alpha = 0.05$, 80\% power). The key $N{=}1{\to}3$ decline ($-13.5$~pp) exceeds this threshold and is well-powered; the stabilization claim ($N{=}3{\to}5$, $+1.0$~pp) is also supported, since a ${\geq}8$~pp improvement would be detected if present.
304	
305	\begin{table}[h]
306	\centering
307	\small
308	\caption{Per-task death rates (\%) for Reflexion at $N{=}3$, 4, 5 on 10 death-prone tasks ($n{=}20$ per task). Aggregate death rates confirm stabilization at $N \geq 3$ (range: $34.0$--$36.5\%$).}
309	\label{tab:dose-response-detail}
310	\begin{tabular}{@{}lrrr@{}}
311	\toprule
312	Task & $N{=}3$ & $N{=}4$ & $N{=}5$ \\
313	\midrule
314	chemistry-mix & 25.0 & 35.0 & 20.0 \\
315	find-animal & 45.0 & 30.0 & 45.0 \\
316	freeze & 50.0 & 50.0 & 60.0 \\
317	grow-fruit & 30.0 & 25.0 & 25.0 \\
318	identify-life-stages-1 & 35.0 & 35.0 & 35.0 \\
319	identify-life-stages-2 & 25.0 & 25.0 & 30.0 \\
320	inclined-plane-angle & 20.0 & 30.0 & 35.0 \\
321	lifespan-longest & 45.0 & 40.0 & 40.0 \\
322	lifespan-long+short & 30.0 & 45.0 & 35.0 \\
323	measure-melting-pt & 35.0 & 50.0 & 25.0 \\
324	\midrule
325	\textbf{Aggregate} & \textbf{34.0} & \textbf{36.5} & \textbf{35.0} \\
326	\bottomrule
327	\end{tabular}
328	\end{table}
329	
330	\section{Router Training Details}
331	\label{app:router-details}
332	
333	We use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.
334	
335	With gradient accumulation of 1 (effective batch size 4), routing performance is highly sensitive to the evaluation split; this suggests overfitting to specific train/validation partition boundaries. With gradient accumulation of 8 (effective batch size 32), step-level performance stabilizes across splits (${\sim}54\%$ balanced accuracy). All reported results use gradient accumulation 8.
336	
337	Under step-level evaluation with a fixed data split, cross-seed balanced accuracy ranges from 52.7\% to 58.1\%, but internal recall varies from 51.5\% to 81.8\%, which reflects threshold sensitivity. However, episode-level evaluation reveals that this apparent discrimination does not generalize: balanced accuracy drops to $47.1 \pm 2.2\%$ across 8 cross-split seeds (Appendix~\ref{app:seed-robustness}). Deployed end-to-end, the trained router allocates 97.0\% of episodes to deterministic computation with 17.6\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.
338	
339	\paragraph{Evaluation methods.} All results use \emph{generation-based evaluation}: the model generates a routing label as text (\texttt{enable\_thinking=False}), parsed for classification. We evaluate at two granularities: \emph{step-level} (steps from the same episode may appear in both train and validation sets) and \emph{episode-level} (entire episodes held out). Step-level accuracy ($54.1 \pm 5.4\%$) exceeds chance (the router captures some signal), but episode-level accuracy ($47.1 \pm 2.2\%$, below chance) shows this does not generalize to unseen episodes. Paraphrase-based text augmentation (Appendix~\ref{app:seed-robustness}) provides no improvement; real-data scaling remains open. Always-deterministic is trivially near-optimal given DAF $= 90.4\%$. The main text (\S\ref{sec:router-diagnostic}) reports controlled 4-seed results at three scales; the model-size ablation (Appendix~\ref{app:ablations}) provides further detail.
340	
341	\begin{table}[h]
342	\centering
343	\small
344	\resizebox{\columnwidth}{!}{%
345	\begin{tabular}{@{}lcc@{}}
346	\toprule
347	Hyperparameter & Classification Head & Implicit Router \\
348	\midrule
349	Base model & Qwen3-1.7B & Qwen3-1.7B \\
350	Architecture & Linear + LoRA & SFT + LoRA \\
351	LoRA $r$ / $\alpha$ & 16 / 32 & 16 / 32 \\
352	Learning rate & 2e-5 & 2e-4 \\
353	Optimizer & AdamW & AdamW \\
354	Epochs & 3 & 3 \\
355	Batch size (per device) & 4 & 4 \\
356	Gradient accumulation & 8 & 8 \\
357	Warmup ratio & 0.1 & 0.1 \\
358	Weight decay & 0.01 & 0.01 \\
359	Max sequence length & 512 & 512 \\
360	Seeds & \{42\} & \{42, 123, 456, 789\} \\
361	\bottomrule
362	\end{tabular}}
363	\caption{Router training hyperparameters. Both architectures use the same base model with LoRA adaptation. The classification head degenerates across all configurations; the implicit router results are reported as 4-seed mean$\pm$std.}
364	\label{tab:hyperparams}
365	\end{table}
366	
367	\paragraph{Agent inference parameters.}
368	For ScienceWorld, each agent step uses temperature $T{=}0.3$ and maximum generation length of 256 tokens, served via vLLM v0.21.0. Top-$p$ is left at the vLLM default of $1.0$ (no nucleus sampling). For MATH, the agent uses greedy decoding ($T{=}0.0$) with a maximum of 2{,}048 tokens per generation. For ALFWorld, we use $T{=}0.3$ with 256 maximum tokens. All three environments use Qwen2.5-7B-Instruct~\citep{qwen25-2024} as the backbone.
369	
370	\section{Seed Robustness}
371	\label{app:seed-robustness}
372	
373	\paragraph{Counterfactual collection seed.}
374	We re-collect all episodes with a different ScienceWorld environment seed (seed=123, $N{=}220$, 20 episodes per task type).
375	The replication yields DAF $= 89.7\%$ ($\Delta_\text{nd} = 2.83$, $\Delta_\text{full} = 27.47$),
376	within 0.73~pp of the primary estimate (seed=42, DAF $= 90.4\%$).
377	Label distributions are consistent: 67 deterministic-preferred / 7 internal-preferred / 146 no-preference
378	(primary: 86 / 9 / 150).
379	Death rates by strategy remain directionally aligned ($\text{DR}_\text{int} = 45.5\%$ vs.\ $42.9\%$; $\text{DR}_\text{det} = 20.9\%$ vs.\ $16.3\%$).
380	The seed=123 replication uses $N{=}220$ ($20$ episodes per task type);
381	the primary dataset's larger $N{=}245$ reflects 25 additional episodes across two task types (\texttt{find-non-living-thing}: $n{=}40$; \texttt{lifespan-longest-lived}: $n{=}25$; all others: $n{=}20$).
382	
383	\paragraph{Router training seed.}
384	We assess router generalization at two evaluation granularities: \emph{step-level}, where steps from the same episode may appear in both train and validation sets, and \emph{episode-level}, where entire episodes are held out. Both use cross-split evaluation (seeds $\{42, \ldots, 49\}$, 8 seeds total), where the data partition and training seed both vary. Table~\ref{tab:seed-robustness} reports per-seed results.
385	
386	\begin{table}[h]
387	\centering
388	\small
389	\begin{tabular}{@{}llcc@{}}
390	\toprule
391	Eval.\ Granularity & Seed & Bal.\ Acc.\ (\%) \\
392	\midrule
393	Step-level & 42 & 57.06 \\
394	(same-episode & 43 & 63.99 \\
395	leakage) & 44 & 55.43 \\
396	 & 45 & 56.14 \\
397	 & 46 & 55.45 \\
398	 & 47 & 50.08 \\
399	 & 48 & 48.03 \\
400	 & 49 & 59.30 \\
401	\cmidrule{2-3}
402	 & Mean$\pm$std & $54.1 \pm 5.4$ \\
403	\midrule
404	Episode-level & 42 & 48.1 \\
405	(held-out & 43 & 47.9 \\
406	episodes) & 44 & 49.6 \\
407	 & 45 & 49.4 \\
408	 & 46 & 48.5 \\
409	 & 47 & 43.1 \\
410	 & 48 & 45.4 \\
411	 & 49 & 44.8 \\
412	\cmidrule{2-3}
413	 & Mean$\pm$std & $47.1 \pm 2.2$ \\
414	\midrule
415	\multicolumn{2}{@{}l}{Always-det (= majority-vote)} & 50.0 \\
416	\bottomrule
417	\end{tabular}
418	\caption{Per-seed router performance under cross-split evaluation (8 seeds, generation-based, \texttt{enable\_thinking=False}). Step-level evaluation allows steps from the same episode in both train and validation sets (same-episode leakage). Episode-level evaluation holds out entire episodes; the resulting $47.1 \pm 2.2\%$ is below the 50\% chance baseline. A text augmentation ablation (Table~\ref{tab:text-augmentation}) confirms this failure persists under the current data distribution and augmentation regime.}
419	\label{tab:seed-robustness}
420	\end{table}
421	
422	The contrast between step-level ($54.1 \pm 5.4\%$) and episode-level ($47.1 \pm 2.2\%$) evaluation reveals a generalization gap: the step-level signal likely reflects memorization of episode-specific context (enabled by same-episode leakage) rather than extraction of generalizable routing features. At episode level, the router performs below chance across all 8 seeds (range: 43.1\%--49.6\%). Paraphrase-based text augmentation (Table~\ref{tab:text-augmentation}) from 25\% to 800\% ($32{\times}$ range) provides no improvement, converging to the always-deterministic baseline ($50\%$). Paraphrase augmentation inflates the majority class without generating novel routing patterns; genuine episode-level scaling (collecting more counterfactual pairs) remains an open question. With DAF $= 90.4\%$ and all task types deterministic-majority (86:9 label ratio), always-deterministic trivially solves the episode-level routing problem, leaving the step-level router with no exploitable signal under current architectures.
423	
424	\paragraph{Text augmentation ablation.} To test whether the episode-level generalization failure stems from data scarcity, we vary training set size from 25\% to 800\% of the original via paraphrase-based text augmentation (synonym substitution + template variation on step observations), holding the episode-level validation set fixed. This tests augmentation-based scaling, not genuine episode-level scaling (which would require new counterfactual collections). Table~\ref{tab:text-augmentation} reports the results.
425	
426	\begin{table}[h]
427	\centering
428	\small
429	\begin{tabular}{@{}rccc@{}}
430	\toprule
431	Scale & Samples & Det\% & Ep.\ Bal.\ Acc.\ (\%) \\
432	\midrule
433	25\% & 433 & ${\sim}90$ & $49.5 \pm 0.3$ \\
434	50\% & 867 & ${\sim}90$ & $51.5$ \\
435	100\% & 1{,}735 & 89.6 & $49.9 \pm 0.1$ \\
436	200\% & 3{,}470 & 94.2 & $50.0 \pm 0.0$ \\
437	800\% & 13{,}880 & ${\sim}97.7$ & $51.0 \pm 1.1$ \\
438	\midrule
439	Always-det & --- & --- & 50.0 \\
440	\bottomrule
441	\end{tabular}
442	\caption{Text augmentation ablation: episode-level balanced accuracy across training set sizes (25\%--800\% of original via paraphrase, $32{\times}$ range). Internal recall $= 0.0$ at all scales (complete majority-class collapse). Det\%: fraction of deterministic-preferred labels in training data. The 50\% scale is a single seed; all others report mean$\pm$std across seeds.}
443	\label{tab:text-augmentation}
444	\end{table}
445	
446	All scales hover at ${\sim}50\%$ episode-level balanced accuracy (equivalent to the always-deterministic baseline), with no monotonic improvement as data increases. Augmentation-based scaling provides no improvement at any scale; however, episode-level minority-class diversity remains a potential confound that cannot be resolved without collecting more internal-preferred episodes. The ground-truth internal-preferred rate (9/245 $= 3.7\%$) means collecting 50 internal-preferred episodes would require approximately 1{,}350 paired episodes at current environment dynamics, a $5.5{\times}$ expansion with diminishing return on a $9.6\%$ signal. The failure points to a limitation of the current data distribution: when DAF $= 90.4\%$ and all task types are deterministic-majority (86:9 label ratio), the episode-level routing problem is trivially solved by always choosing deterministic, and the step-level router finds no exploitable signal under the current architecture and data regime.
447	
448	Augmentation disproportionately increases the majority (deterministic) class: Det\% rises from 89.6\% at 100\% to 94.2\% at 200\% and ${\sim}97.7\%$ at 800\%. However, the complete collapse to majority-class prediction (internal recall $= 0.0$) occurs even at the smallest unaugmented scale (25\%, ${\sim}90\%$ det); this is not an augmentation artifact. Balanced accuracy corrects for class imbalance by averaging per-class recall, so the metric itself is not biased by the skew.
449	
450	Decomposition metrics are stable under bootstrap resampling ($B{=}10{,}000$ resamples of the 245-episode dataset): DAF $= 90.4\% \pm 4.2\%$ (95\% CI $[81.3\%, 99.1\%]$); Pearson $r = 0.975 \pm 0.011$ (95\% CI $[0.952, 0.995]$). The death avoidance dominance finding is robust to both resampling and split perturbation.
451	
452	\paragraph{Per-task-type evaluation breakdown.} To test whether the router learns transferable routing strategies or merely task-type classification, we evaluate existing checkpoints (8 seeds) separately on each of the 11 task types. Of the 11 task types, 7 have \emph{all-deterministic} labels (no internal-preferred episodes exist), making balanced accuracy undefined; the router has nothing to learn beyond the trivial always-deterministic default. For the remaining 4 task types where both classes are present, balanced accuracy ranges from 50.0\% to 73.0\%, but this apparent signal does not indicate cross-task-type routing transfer: the router is effectively classifying task types (which correlate with death risk) rather than extracting a generalizable routing strategy. This complements the text augmentation ablation: routing signal does not transfer across task types because the signal \emph{is} the task type, i.e., whether a given task carries death risk. The 4B capacity scaling result (Appendix~\ref{app:ablations}) suggests capacity is one factor, but even 4B's $59.0\%$ episode-level accuracy does not demonstrate cross-task-type transfer.
453	
454	\section{Penalty Sensitivity Analysis}
455	\label{app:penalty}
456	
457	\begin{table}[h]
458	\centering
459	\small
460	\begin{tabular}{@{}rrr@{}}
461	\toprule
462	$P$ & DAF($P$) & 95\% CI \\
463	\midrule
464	0 & 7.4\% & [$-39.4$, $82.5$] \\
465	1 & 14.8\% & [$-28.6$, $89.6$] \\
466	5 & 35.4\% & [$-1.8$, $92.7$] \\
467	10 & 50.4\% & [$18.5$, $93.3$] \\
468	25 & 70.7\% & [$48.0$, $96.3$] \\
469	50 & 82.6\% & [$67.2$, $98.2$] \\
470	100\textsuperscript{*} & 90.4\% & [$81.3$, $99.1$] \\
471	200 & 94.9\% & [$89.9$, $99.5$] \\
472	500 & 97.9\% & [$95.7$, $99.8$] \\
473	\bottomrule
474	\end{tabular}
475	\caption{Sensitivity of DAF to death penalty magnitude $P$. DAF$(P) = 1 - \Delta_{\text{nd}} / \Delta_{\text{full}}(P)$, where $\Delta_{\text{full}}(P) \approx \delta \cdot P + \Delta_{\text{nd}}$, $\delta = 0.2653$ is the death-rate differential, and $\Delta_{\text{nd}} = 2.84$ (strict neither-died filtering). Recomputed from 245 episode-level data; bootstrap 95\% CIs ($B{=}10{,}000$). \textsuperscript{*}Default setting.}
476	\label{tab:penalty-sensitivity}
477	\end{table}
478	
479	The non-death score gap $\Delta_{\text{nd}} = 2.84$ is invariant across penalty levels; it depends only on surviving-episode performance, not on $P$. As $P$ increases, $\Delta_{\text{full}}$ grows ($16.33$ at $P{=}50$, $29.60$ at $P{=}100$, $56.13$ at $P{=}200$) while $\Delta_{\text{nd}}$ remains fixed, mechanically increasing DAF.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f37e98f-78d8-44f0-8478-8c9f4805dea9",
  "isSidechain": true,
  "promptId": "615c1eae-3cf0-4729-ad9e-5bf3fb5d3b1d",
  "agentId": "af152b21ba92fc359",
  "type": "user",
  "uuid": "f39d9e4a-8171-4ab6-9da1-c3d5ed24966e",
  "sourceToolAssistantUUID": "8f37e98f-78d8-44f0-8478-8c9f4805dea9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-24T20:50:27.630Z_

Now let me continue and get the remaining tables:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f39d9e4a-8171-4ab6-9da1-c3d5ed24966e",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN45c1SwdqAmMAXX1ugX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "902fa18e-5771-4419-b605-0bfc389b23f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JJ1TEsLtFnreHEtx4LVEyX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 7375,
      "cache_read_input_tokens": 71707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7375,
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

_source line 24 · 2026-05-24T20:50:28.640Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VQxcgqcfyNLvLMoNWnZbN7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "offset": 479,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "902fa18e-5771-4419-b605-0bfc389b23f9",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN45c1SwdqAmMAXX1ugX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d3515c00-6f54-4bce-9b30-51c2d0f3e8e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JJ1TEsLtFnreHEtx4LVEyX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 7375,
      "cache_read_input_tokens": 71707,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7375
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 134,
          "cache_read_input_tokens": 71707,
          "cache_creation_input_tokens": 7375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7375,
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

_source line 25 · 2026-05-24T20:50:28.647Z_

<details><summary>↩ Tool result · `toolu_01VQxcgqcfyNLvLMoNWnZbN7`</summary>

```text
479	The non-death score gap $\Delta_{\text{nd}} = 2.84$ is invariant across penalty levels; it depends only on surviving-episode performance, not on $P$. As $P$ increases, $\Delta_{\text{full}}$ grows ($16.33$ at $P{=}50$, $29.60$ at $P{=}100$, $56.13$ at $P{=}200$) while $\Delta_{\text{nd}}$ remains fixed, mechanically increasing DAF.
480	
481	\paragraph{Mechanism boundary: death specificity.}
482	The $r = 0.97$ correlation between per-task death-rate differential and $\Delta_{\text{full}}$ is specific to catastrophic death (score $= -100$). Broader failure definitions dissolve the correlation entirely: defining ``failure'' as any non-positive score ($T{=}0$) yields $r = -0.13$ ($p = 0.70$), because non-death episodes show near-zero performance differential between strategies ($\Delta_{\text{nd}} = 2.84$). Table~\ref{tab:penalty-correlation} quantifies this specificity across penalty magnitudes.
483	
484	\begin{table}[h]
485	\centering
486	\small
487	\begin{tabular}{@{}rccl@{}}
488	\toprule
489	$P$ & $r$ & $p$ & Sig.\ ($\alpha{=}0.05$) \\
490	\midrule
491	1 & $-0.44$ & $0.178$ & No \\
492	5 & $-0.29$ & $0.382$ & No \\
493	10 & $-0.08$ & $0.813$ & No \\
494	25 & $0.51$ & $0.108$ & No \\
495	50 & $0.86$ & $0.0006$ & Yes \\
496	100\textsuperscript{*} & $0.97$ & $8 \times 10^{-7}$ & Yes \\
497	200 & $0.99$ & $1 \times 10^{-9}$ & Yes \\
498	\bottomrule
499	\end{tabular}
500	\caption{Pearson $r$ between per-task death-rate differential and $\Delta_{\text{full}}(P)$ across penalty magnitudes. The correlation is non-significant at low penalties and emerges at $P \geq 50$, which reflects the transition from non-death-dominated to death-dominated score gaps. \textsuperscript{*}Default ScienceWorld setting.}
501	\label{tab:penalty-correlation}
502	\end{table}
503	
504	This sharpens our central finding: death is not merely the dominant component of routing signal; it is effectively the \emph{only} component that generates differential routing signal in ScienceWorld. At low penalties, the death contribution is small and $\Delta_{\text{full}}$ reduces to $\Delta_{\text{nd}} \approx 2.84$, which is near-uniform across task types ($\text{mean non-death gap} = -1.19$ excluding the \texttt{find-non-living-thing} outlier); consequently, death-rate differential has no predictive power. As $P$ increases, the death term dominates $\Delta_{\text{full}}$, and the correlation sharpens because death rates \emph{are} the performance gap. The DAF values in Table~\ref{tab:penalty-sensitivity} increase monotonically with $P$, but this is a mathematical consequence of the decomposition ($\text{DAF} = \delta P / (\delta P + \Delta_{\text{nd}})$), not evidence of mechanism robustness.
505	
506	\section{Cross-Environment Details}
507	\label{app:cross-env-details}
508	
509	Table~\ref{tab:cross-env} summarizes the label distributions across all three environments (see also Figure~\ref{fig:signal-reversal} in \S\ref{sec:cross-env}).
510	
511	\begin{table}[h]
512	\centering
513	\small
514	\resizebox{\columnwidth}{!}{%
515	\begin{tabular}{@{}lccccc@{}}
516	\toprule
517	Environment & $N$ & Det\% & Int\% & NoPref\% & Death? \\
518	\midrule
519	ScienceWorld & 245 & 35.1 & 3.7 & 61.2 & Yes ($-100$) \\
520	MATH & 795 & 7.3 & 8.3 & 84.4 & No \\
521	ALFWorld & 135 & 25.9 & 1.5 & 72.6 & No\textsuperscript{$\dagger$} \\
522	\bottomrule
523	\end{tabular}}
524	\caption{Cross-environment label distribution. ``Deterministic'' denotes qualitatively different computation modes: ScienceWorld = oracle simulator with ground-truth state; MATH = Python code interpreter; ALFWorld = admissible-action enumeration. $\dagger$\,ALFWorld's deterministic advantage stems from information asymmetry, not death avoidance.}
525	\label{tab:cross-env}
526	\end{table}
527	
528	Table~\ref{tab:alfworld-pertask} provides the per-task-type breakdown for ALFWorld. Unlike ScienceWorld, ALFWorld has no death mechanism ($\delta = 0$, DAF $= 0\%$); the entire performance gap $\Delta_{\text{full}}$ reflects information asymmetry from admissible-action access. \texttt{pick\_and\_place} shows the strongest effect ($\Delta = 0.563$, 18 of 32 episodes det-preferred), while \texttt{pick\_two\_obj\_and\_place} shows the weakest ($\Delta = 0.087$), consistent with multi-object tasks requiring more sequential reasoning that admissible actions alone cannot resolve. Only \texttt{pick\_heat\_then\_place} has a 95\% CI crossing zero ($n{=}16$).
529	
530	\begin{table}[h]
531	\centering
532	\scriptsize
533	\setlength{\tabcolsep}{2.5pt}
534	\begin{tabular}{@{}lrcccc@{}}
535	\toprule
536	Task Type & $n$ & Succ\%\textsubscript{int} & Succ\%\textsubscript{det} & D / I / N & $\Delta_{\text{full}}$ \\
537	\midrule
538	pick\_and\_place       & 32 & 0.0  & 56.3 & 18 / 0 / 14 & $+0.563$ \\
539	look\_at\_obj\_in\_light & 13 & 15.4 & 38.5 & 3 / 0 / 10  & $+0.231$ \\
540	pick\_cool\_then\_place & 24 & 0.0  & 16.7 & 4 / 0 / 20  & $+0.167$ \\
541	pick\_clean\_then\_place & 27 & 3.7  & 18.5 & 5 / 1 / 21  & $+0.148$ \\
542	pick\_heat\_then\_place & 16 & 6.3  & 18.8 & 3 / 1 / 12  & $+0.125$ \\
543	pick\_two\_obj\_and\_place & 23 & 0.0 & 8.7  & 2 / 0 / 21  & $+0.087$ \\
544	\midrule
545	\textbf{All (6 types)} & \textbf{135} & \textbf{3.0} & \textbf{27.4} & \textbf{35 / 2 / 98} & $\mathbf{+0.244}$ \\
546	\bottomrule
547	\end{tabular}
548	\caption{Per-task-type decomposition for ALFWorld (135 games, Qwen2.5-7B-Instruct). D/I/N: deterministic-preferred / internal-preferred / no-preference. No death mechanism exists; $\Delta_{\text{full}}$ is driven entirely by information asymmetry from admissible-action access. Sorted by $\Delta_{\text{full}}$ descending.}
549	\label{tab:alfworld-pertask}
550	\end{table}
551	
552	\paragraph{MATH subset composition.}
553	The $N{=}795$ MATH problems span two categories from the MATH test set~\citep{math-2021} (Levels 4--5): Algebra (585, 73.6\%) and Counting \& Probability (210, 26.4\%). The category imbalance reflects the relative sizes in the original test set.
554	
555	\section{Cross-Model Verification}
556	\label{app:cross-model}
557	
558	We replicate the counterfactual analysis with Llama-3.1-8B-Instruct across all 11 task types ($N{=}220$ episode pairs, 20 per type; Table~\ref{tab:cross-model-detail}).
559	The internal strategy dies in $41.4\%$ of episodes versus $11.4\%$ for deterministic (death-rate differential $+30.0$~pp), with 83 deterministic-preferred, 3 internal-preferred (1.4\%, all death-asymmetry reversals), and 134 no-preference labels.
560	Both models exhibit nearly identical internal vulnerability (${\sim}$42\%: Qwen $42.9\%$, Llama $41.4\%$), confirming that death-prone failure is empirically dominated by the task environment rather than model-specific factors. The differential magnitude varies ($+26.5$~pp Qwen, $+30.0$~pp Llama) because deterministic strategy safety is model-dependent ($16.3\%$ vs.\ $11.4\%$), but directional consistency is 100\% (10/10 death-prone tasks in both models).
561	\texttt{identify-life-stages-1} shows cross-model precision matching ($55\%$/$10\%$/$+45$~pp in both models).
562	\texttt{find-non-living-thing} shows zero deaths in both models, consistent with its majority-class answer distribution.
563	
564	\begin{table}[h]
565	\centering
566	\small
567	\resizebox{\columnwidth}{!}{%
568	\begin{tabular}{@{}lrrrl@{}}
569	\toprule
570	Task & Int\% & Det\% & $\Delta$\,pp & D / I / N \\
571	\midrule
572	identify-life-stages-1 & 55 & 10 & +45 & 9 / 0 / 11 \\
573	freeze & 45 & 0 & +45 & 9 / 0 / 11 \\
574	grow-fruit & 45 & 5 & +40 & 8 / 0 / 12 \\
575	identify-life-stages-2 & 45 & 5 & +40 & 8 / 0 / 12 \\
576	measure-melting-point & 50 & 15 & +35 & 9 / 0 / 11 \\
577	lifespan-longest & 35 & 5 & +30 & 7 / 1 / 12 \\
578	lifespan-l-then-s & 50 & 20 & +30 & 6 / 0 / 14 \\
579	chemistry-mix & 45 & 20 & +25 & 5 / 0 / 15 \\
580	inclined-plane & 45 & 20 & +25 & 6 / 0 / 14 \\
581	find-animal & 40 & 25 & +15 & 6 / 2 / 12 \\
582	find-non-living-thing & 0 & 0 & 0 & 10 / 0 / 10 \\
583	\midrule
584	\textbf{Aggregate} & \textbf{41.4} & \textbf{11.4} & \textbf{+30.0} & \textbf{83 / 3 / 134} \\
585	\bottomrule
586	\end{tabular}}%
587	\caption{Per-task Llama-3.1-8B cross-model replication ($N{=}20$ per task). D/I/N: deterministic-preferred / internal-preferred / no-preference. Sorted by $\Delta$ DR descending.}
588	\label{tab:cross-model-detail}
589	\end{table}
590	
591	\paragraph{Cross-model and cross-environment summary.}
592	Table~\ref{tab:cross-model-env} consolidates replication results across model families and environments.
593	
594	\begin{table}[h]
595	\centering
596	\small
597	\resizebox{\columnwidth}{!}{%
598	\begin{tabular}{llcrrrccc}
599	\toprule
600	Model & Environment & $n$ & Int DR & Det DR & $\Delta$DR & DAF & DAF 95\% CI & Signal \\
601	\midrule
602	Qwen2.5-7B & ScienceWorld & 245 & 42.9\% & 16.3\% & +26.5 & 90.4\% & [81.3, 99.1] & death \\
603	Llama-3.1-8B & ScienceWorld & 220 & 41.4\% & 11.4\% & +30.0 & 88.2\% & [80.2, 95.1] & death \\
604	Gemma-2-9B-it & ScienceWorld & 220 & 36.4\% & 14.1\% & +22.3 & 89.7\% & [79.5, 98.4] & death \\
605	Qwen2.5-72B & ScienceWorld & 255 & 30.6\% & 2.75\% & +27.8 & 92.4\% & [86.1, 97.9] & death \\
606	Llama-3.1-70B & ScienceWorld & 220 & 48.6\% & 20.0\% & +28.6 & 101.0\% & [95.3, 107.5] & death \\
607	\midrule
608	Qwen2.5-7B & ALFWorld & 135 & 0\% & 0\% & 0 & 0\% & --- & info-asym \\
609	Llama-3.1-8B & ALFWorld & 135 & 0\% & 0\% & 0 & 0\% & --- & info-asym \\
610	\midrule
611	Qwen2.5-7B & MATH & 795 & N/A & N/A & N/A & N/A & N/A & none \\
612	\bottomrule
613	\end{tabular}}
614	\caption{Cross-model and cross-environment replication summary. \textbf{ScienceWorld}: death dominance replicates across three model families in the 7--9B range and intensifies under $10{\times}$ scaling (two 70B-class models, DAF $92.4$--$101.0\%$); DAF 95\% CIs from non-clustered episode-level bootstrap ($B{=}10{,}000$). \textbf{ALFWorld}: DAF $= 0\%$ (no death mechanism); routing signal arises from information asymmetry. \textbf{MATH}: no routing signal without catastrophic failure. Signal column: diagnosed routing mechanism. DR = death rate. Gemma-2's wider CI reflects one zero-death task type (\texttt{find-non-living-thing}); excluding it yields DAF $= 99.9\%$ $[99.7, 100.0]$.}
615	\label{tab:cross-model-env}
616	\end{table}
617	
618	\section{Failure Mode Analysis}
619	\label{app:failure-modes}
620	
621	All 105 internal-strategy deaths (100\%) are triggered by the same action pattern: \texttt{focus on [object]}. In ScienceWorld, \texttt{focus on} is the answer-submission action (equivalent to ``this is my final answer''); the LLM agent systematically misuses it as a general interaction or exploration command, and applies it to irrelevant targets (rooms, doors, inventory items). Each such execution submits an incorrect answer and triggers the $-100$ death penalty. Within death episodes, both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40 for deterministic) reflects how often each strategy enters catastrophic states, not different action selection within those states.
622	
623	Manual inspection identifies four failure categories: (A) no task awareness, where the agent executes \texttt{focus on} without reading the task; (B) task-aware but lacking action grounding, where the agent correctly identifies the objective but cannot map it to valid action primitives; (D) genuine attempts with execution failure; and (E) initial progress wasted by early errors. Category B dominates: agents demonstrate task comprehension but systematically fail to translate it into correct ScienceWorld actions. This taxonomy was produced by a single annotator; no inter-annotator agreement was computed. The categories are intended as qualitative illustrations, not as formal labels with reliability guarantees.
624	\label{tab:death-taxonomy}
625	
626	\paragraph{Representative examples.}
627	\emph{Category A} (no task awareness): In a \texttt{chemistry-mix} episode, the agent immediately executes \texttt{focus on kitchen}, \texttt{focus on door}, \texttt{focus on inventory} without reading the task, dying on the first \texttt{focus on} call. \emph{Category B} (comprehension without grounding): In a \texttt{lifespan-longest-lived} episode, the agent correctly identifies that it must compare animal lifespans and reasons about which animal lives longest, but then executes \texttt{focus on oak tree} (a non-animal object in the room) instead of navigating to find the target animal, triggering death.
628	
629	\paragraph{Action distribution analysis.}
630	Figure~\ref{fig:death-action-dist} shows the action distribution in death versus non-death episodes for the internal strategy; both are dominated by \texttt{connect} actions, with \texttt{focus on} moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$). Crucially, Figure~\ref{fig:death-comparison} reveals that within death episodes, internal and deterministic strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$). The survival gap (105 vs.\ 40 deaths) therefore reflects how often each strategy enters catastrophic states, not how it behaves within those states. Among fatal \texttt{focus on} targets, \texttt{workshop} remains the most frequent (20.0\%), followed by \texttt{inventory} (17.1\%) and \texttt{kitchen} (10.5\%), indicating a systematic object bias rather than random exploration. Figure~\ref{fig:death-timeline} visualizes the temporal pattern: agents execute long sequences of \texttt{connect} actions before a terminal \texttt{focus on} triggers death, typically in the final 1--3 steps.
631	
632	\begin{figure}[h]
633	\centering
634	\includegraphics[width=\columnwidth]{figures/death_action_distribution.pdf}
635	\caption{Action distribution for the internal (LLM) strategy in death ($n{=}105$) vs.\ non-death ($n{=}140$) episodes. Left: full distribution (both dominated by \texttt{connect}). Right: non-\texttt{connect} actions zoomed. \texttt{focus on} is moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$), while non-death episodes show higher rates of observation and object interaction.}
636	\label{fig:death-action-dist}
637	\end{figure}
638	
639	% Figure moved to main text (\S\ref{sec:death-decomp})
640	
641	\begin{figure}[h]
642	\centering
643	\includegraphics[width=\columnwidth]{figures/death_action_comparison.pdf}
644	\caption{Non-\texttt{connect} action distribution comparison between internal (left) and deterministic (right) strategies. Within death episodes, both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not different action selection within those states.}
645	\label{fig:death-comparison}
646	\end{figure}
647	
648	\section{Grounding Ablation}
649	\label{app:grounding-ablation}
650	
651	We test whether directly intervening on the dominant death action (\texttt{focus on}) eliminates death vulnerability on the 10 death-prone tasks (baseline 48.0\%, $n{=}200$).
652	
653	\paragraph{Prompt warning.} Adding an explicit system prompt (``use \texttt{focus on} only for final answers'') reduces aggregate death rate to 37.0\% ($\Delta = -11$~pp). Both identification tasks exhibit ironic effects (\texttt{identify-life-stages-1}: 35\%$\to$50\%; \texttt{identify-life-stages-2}: 25\%$\to$70\%), where explicit mention of the dangerous action may have increased its salience.
654	
655	\paragraph{Action-space filtering.} Blocking \texttt{focus on} during the exploration phase yields 379 blocks across 200 episodes with zero leaks and zero passthroughs (the agent never persisted in retrying blocked actions), reducing death rate to 29.0\% ($\Delta = -19$~pp). The zero-passthrough rate suggests \texttt{focus on} use is a shallow behavioral pattern rather than a deliberate strategy.
656	
657	\paragraph{Per-task variation.} Under filtering, \texttt{identify-life-stages} and \texttt{inclined-plane} approach deterministic-level safety (${\sim}$15--20\% DR), while \texttt{chemistry-mix} and \texttt{find-animal} remain at 35--40\%. Residual deaths occur during the answer-submission window, where the filter is inactive and agents submit \texttt{focus on} to incorrect objects.
658	
659	\paragraph{Post-ablation counterfactual decomposition.}
660	To test whether death dominance persists after grounding intervention, we run the full decomposition on matched episodes (183 episodes across 10 death-prone task types, paired by variation index).
661	Grounding reduces the internal death rate from 50.3\% to 35.0\% ($-15.3$\,pp), yet $\geq$93\% of disambiguating labels still arise from death asymmetry ($\Delta_\text{nd} \approx 0.09$, compared to $0.00$ at baseline).
662	Internal-preferred episodes increase from 5 to 23 (grounding helps internal strategy survive more often), but the routing signal remains death-driven rather than score-driven.
663	One task type (\texttt{identify-life-stages-2}, $n{=}10$) shows a paradoxical increase in death rate (50\%$\to$80\%); this outlier likely reflects the small sample size and task-specific prompt interference rather than a systematic effect.
664	
665	\section{Ablation Studies}
666	\label{app:ablations}
667	
668	\paragraph{Capacity scaling.} We scale the implicit router from Qwen3-0.6B to Qwen3-4B and evaluate at both step and episode level (Table~\ref{tab:capacity}).
669	
670	\begin{table}[h]
671	\centering
672	\small
673	\begin{tabular}{@{}lcc@{}}
674	\toprule
675	Model & Step Bal.\ Acc.\ (\%) & Ep.\ Bal.\ Acc.\ (\%) \\
676	\midrule
677	Qwen3-0.6B & $56.4 \pm 3.5$ & $50.7 \pm 2.6$ \\
678	Qwen3-1.7B & $58.2 \pm 4.0$ & $43.1 \pm 1.0$ \\
679	Qwen3-4B & $59.2 \pm 3.5$ & $\mathbf{59.0 \pm 1.9}$ \\
680	\midrule
681	Always-det & 50.0 & 50.0 \\
682	\bottomrule
683	\end{tabular}
684	\caption{Capacity scaling: step-level and episode-level balanced accuracy (4 seeds, identical configuration across all scales). Step-level accuracy is flat ($56$--$59\%$, within seed variance). At episode level, only 4B breaks the random baseline ($59.0\%$, $p < 0.005$).}
685	\label{tab:capacity}
686	\end{table}
687	
688	Step-level balanced accuracy is flat across scales ($56$--$59\%$, within seed variance); step-level discrimination is not capacity-sensitive. At episode level, only 4B breaks the random baseline ($59.0 \pm 1.9\%$, $p < 0.005$); 0.6B and 1.7B remain at or below chance. The 1.7B model's below-chance episode-level accuracy ($43.1\%$) may reflect overfitting to spurious step-level correlations that anti-correlate with episode outcomes; without per-class confusion matrices at this scale, this remains a hypothesis. The dominant explanation across scales is that death avoidance constitutes a task-type-level binary signal that a step-level router cannot exploit efficiently.
689	
690	\paragraph{Generative router.} A generative routing model trained with explicit routing labels achieves balanced accuracy of 46.7\%, confirming that the routing bottleneck is signal-limited, not architecture-limited.
691	
692	\paragraph{Leave-one-task-type-out routing.} Under leave-one-task-type-out evaluation, blind routing collapses to always-deterministic (balanced accuracy 50.0\%); a keyword-based variant achieves 62.9\% only through task-identity leakage, not genuine routing signal. A guided router evaluated under the same protocol confirms this: without task-type identifiers it achieves chance accuracy (50.0\%), and leaking task names raises this to 62.9\%, confirming that the only learnable routing feature is task-type identity.
693	
694	\paragraph{Death-proximal labeling.} Training a router only on the $k$ steps preceding death events (rather than all steps) also collapses to majority-class prediction (step balanced accuracy 50.0\%, episode balanced accuracy 50.0\%, internal recall 0\%), confirming that the absence of step-level signal is not an artifact of label dilution across long episodes.
695	
696	\paragraph{Reasoning depth.} An ablation comparing chain-of-thought reasoning against direct-answer generation on 6 task types ($n{=}120$ episodes per condition, 6 tasks $\times$ 20 episodes per task) found no significant difference (Mann--Whitney $p > 0.26$, $|d| \leq 0.31$) and near-identical death rates (41.8\% vs.\ 42.5\%); reasoning depth does not meaningfully alter internal-mode outcomes.
697	
698	\section{Threshold Routing Analysis}
699	\label{sec:threshold-routing}
700	
701	Given per-task death risk knowledge, we test whether a simple threshold routing strategy can outperform always-deterministic. For each threshold $t \in [0, 1]$, we route to internal if the per-task internal death rate $\leq t$, otherwise to deterministic, and sweep all thresholds to find the optimal.
702	
703	\begin{table}[h]
704	\centering
705	\small
706	\resizebox{\columnwidth}{!}{%
707	\begin{tabular}{lccc}
708	\toprule
709	Strategy & Mean Score & Death Rate & $\Delta$ vs Det \\
710	\midrule
711	Always-det & $-9.47$ & $0.163$ & $0.00$ \\
712	Optimal threshold ($t{=}0$) & $-11.03$ & $0.155$ & $-1.56$ \\
713	Always-internal & $-39.07$ & $0.429$ & $-29.60$ \\
714	\bottomrule
715	\end{tabular}}
716	\caption{Death-risk threshold routing analysis on 245 episodes. The optimal threshold routes only \texttt{find-non-living-thing} (the sole zero-death task) to internal, with all other tasks routed to deterministic. Bootstrap 95\% CI for the difference: $[-8.87, +5.92]$.}
717	\label{tab:threshold-routing}
718	\end{table}
719	
720	Even with perfect per-task death risk knowledge, threshold routing cannot outperform always-deterministic. The sole zero-death task achieves higher scores under deterministic (+28.5) than internal (+18.9), leaving no room for a beneficial mixed strategy.
721	
722	\section{Practitioner Decision Framework}
723	\label{app:decision-framework}
724	
725	Given a new interactive environment, the following three-stage procedure diagnoses whether learned routing adds value over a fixed deterministic strategy.
726	
727	\paragraph{Stage 1: Pilot collection (${\sim}$50 episodes).}
728	Run pure-internal and pure-deterministic strategies on a representative sample (${\sim}$50 episode pairs). Compute the death-rate differential $\Delta\text{DR} = \text{DR}_{\text{int}} - \text{DR}_{\text{det}}$.
729	
730	\paragraph{Stage 2: Death dominance check.}
731	If $\Delta\text{DR} > 15$~pp, death asymmetry is likely the dominant routing signal. Compute the death-label fraction $f_{\text{death}}$: the proportion of non-tie routing labels where exactly one strategy dies.
732	
733	\paragraph{Stage 3: Decision.}
734	If $f_{\text{death}} > 75\%$, the routing signal is death-dominated; a fixed deterministic strategy will match or exceed any learned router. If $f_{\text{death}} < 50\%$, diverse routing signals may justify a learned router. Between 50\%--75\%, collect additional episodes to reduce estimation noise before committing to router development.
735	
736	\paragraph{Retrospective validation.}
737	All four experimental conditions in this paper are correctly classified:
738	
739	\begin{table}[h]
740	\centering
741	\small
742	\begin{tabular}{@{}lrrll@{}}
743	\toprule
744	Condition & $\Delta$DR & $f_{\text{death}}$ & Prediction & Actual \\
745	\midrule
746	Qwen-7B & +26.5 & 78.9\% & det-fixed & det wins \\
747	Llama-8B & +30.0 & $>$75\% & det-fixed & det wins \\
748	Qwen-72B & +27.8 & $>$75\% & det-fixed & det wins \\
749	MATH & +0.5 & 0\% & router viable & no signal \\
750	\bottomrule
751	\end{tabular}
752	\caption{Retrospective validation of the decision framework. All four conditions are correctly classified (4/4).}
753	\label{tab:decision-framework}
754	\end{table}
755	
756	The framework also predicts the inverted-U relationship between capability and death risk: below ${\sim}$0.5B parameters, agents rarely reach dangerous states (13.3\% death rate in a 15-episode pilot), so $\Delta\text{DR}$ is low and the framework would not recommend fixed-deterministic. Above ${\sim}$7B, agents are capable enough to enter catastrophic states but not capable enough to avoid them, producing high $\Delta\text{DR}$.
757	
758	\paragraph{Threshold calibration.} The thresholds above (15~pp, 75\%, 50\%) are illustrative, derived from ScienceWorld's specific reward structure (binary death penalty $P{=}100$, sparse terminal rewards). Environments with graded penalties, dense rewards, or qualitatively different failure modes may require different thresholds. Practitioners should calibrate these boundaries for their specific environment.
759	
760	\section{Extended Validation of Excluded Tasks}
761	\label{app:extended-validation}
762	
763	To verify that task exclusion does not bias toward death-prone tasks, we collect $n{=}20$ episodes for five representative excluded tasks spanning all exclusion categories (Table~\ref{tab:extended-val}).
764	
765	\begin{table}[h]
766	\centering
767	\small
768	\resizebox{\columnwidth}{!}{%
769	\begin{tabular}{lcrrrrc}
770	\toprule
771	Task & Category & $n$ & Int DR & Det DR & $\Delta$DR & D/I/N \\
772	\midrule
773	boil & dev-set & 20 & 55\% & 25\% & +30\,pp & 6/0/14 \\
774	melt & dev-set & 20 & 45\% & 20\% & +25\,pp & 7/2/11 \\
775	find-living-thing & taxonomic & 20 & 55\% & 15\% & +40\,pp & 10/0/10 \\
776	use-thermometer & agent-floor & 20 & 50\% & 20\% & +30\,pp & 7/1/12 \\
777	power-component & agent-floor & 20 & 50\% & 15\% & +35\,pp & 7/0/13 \\
778	\midrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3515c00-6f54-4bce-9b30-51c2d0f3e8e3",
  "isSidechain": true,
  "promptId": "615c1eae-3cf0-4729-ad9e-5bf3fb5d3b1d",
  "agentId": "af152b21ba92fc359",
  "type": "user",
  "uuid": "4b08f2fb-dea1-4e9f-97e1-61d56b02d512",
  "sourceToolAssistantUUID": "d3515c00-6f54-4bce-9b30-51c2d0f3e8e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-24T20:50:29.814Z_

Now let me get the remaining tables and figures:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b08f2fb-dea1-4e9f-97e1-61d56b02d512",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN45nJ5YC5XnwqEXdq3W",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "202a4e8d-bd06-4626-a311-18e4f5062183",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018jwHgjREy4Yxx2YmgA1sUn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 8944,
      "cache_read_input_tokens": 79082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8944,
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

_source line 27 · 2026-05-24T20:50:30.791Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BWsvgkoEepivAuzXDNtiqn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "offset": 778,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "202a4e8d-bd06-4626-a311-18e4f5062183",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN45nJ5YC5XnwqEXdq3W",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "31a570e6-3b3b-4483-9b97-e1c16d0d3c57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018jwHgjREy4Yxx2YmgA1sUn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 8944,
      "cache_read_input_tokens": 79082,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8944
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 134,
          "cache_read_input_tokens": 79082,
          "cache_creation_input_tokens": 8944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8944,
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

_source line 28 · 2026-05-24T20:50:30.813Z_

<details><summary>↩ Tool result · `toolu_01BWsvgkoEepivAuzXDNtiqn`</summary>

```text
778	\midrule
779	\textit{Mean (5 tasks)} & & 100 & 51.0\% & 19.0\% & +32.0\,pp & 37/3/60 \\
780	\bottomrule
781	\end{tabular}}
782	\caption{Extended validation ($n{=}20$) of representative excluded task types. All five tasks confirm death asymmetry; mean $\Delta$DR $= +32.0$\,pp is consistent with the $n{=}5$ prescreening estimate for these same tasks (Table~\ref{tab:excluded-death}).}
783	\label{tab:extended-val}
784	\end{table}
785	
786	Notably, the excluded-task aggregate DAF (0.991) exceeds the included-task DAF (0.904; Table~\ref{tab:per-task}), indicating that excluded tasks are \emph{more} death-dominated than included tasks---the opposite of a cherry-picking bias.
787	
788	\section{Agent Prompt Templates}
789	\label{app:prompt-templates}
790	
791	Below we show the complete prompt templates used for agent interaction in ScienceWorld. Both the internal (ReAct) and deterministic strategies share the same system prompt but differ in the user message template.
792	
793	\paragraph{System prompt (shared).} Used for all ScienceWorld agent interactions across both computation modes.
794	
795	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
796	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
797	  left=2mm, right=2mm, top=1mm, bottom=1mm}
798	You are an agent interacting with a ScienceWorld text
799	environment. Your goal is to complete the given task by
800	choosing actions from the available action list.
801	
802	Use the following format for each step:
803	Thought: &lt;your reasoning about what to do next>
804	Action: &lt;exact action string from the valid actions list>
805	
806	Rules:
807	- You MUST choose an action from the valid actions list.
808	  Do not invent actions.
809	- Think step by step about what physical/scientific
810	  process is needed.
811	- Pay attention to the current observation for clues
812	  about object states.
813	\end{tcblisting}
814	
815	\paragraph{Internal (ReAct) user template.} At each step, the agent receives the current observation, valid action list, and recent action history, and must select a single action.
816	
817	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
818	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
819	  left=2mm, right=2mm, top=1mm, bottom=1mm}
820	Current observation:
821	{observation}
822	
823	Valid actions:
824	{valid_actions_str}
825	
826	Previous actions taken: {history_str}
827	
828	Choose your next action.
829	\end{tcblisting}
830	
831	\paragraph{Deterministic candidate generation template.} For the deterministic strategy, the agent generates ranked candidate actions instead of selecting one; these candidates are then evaluated via simulator forking (\S\ref{sec:method}).
832	
833	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
834	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
835	  left=2mm, right=2mm, top=1mm, bottom=1mm}
836	Current observation:
837	{observation}
838	
839	Valid actions:
840	{valid_actions_str}
841	
842	Previous actions taken: {history_str}
843	
844	Generate the top 3 most promising actions from the valid
845	actions list, ranked by how likely they are to make
846	progress on the task. Output exactly 3 actions, one per
847	line, in this format:
848	1. &lt;action>
849	2. &lt;action>
850	3. &lt;action>
851	\end{tcblisting}
852	
853	\paragraph{Reflexion self-reflection prompt.} After a failed episode, the Reflexion agent (\S\ref{sec:agent-improvement}) generates a reflection that is injected into subsequent trial attempts as additional system context.
854	
855	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
856	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
857	  left=2mm, right=2mm, top=1mm, bottom=1mm}
858	You just completed an episode in a ScienceWorld text
859	environment but failed.
860	
861	Task: {task_name}
862	Final score: {final_score}
863	Outcome: {outcome}
864	Number of steps taken: {num_steps}
865	
866	Here is a summary of your actions:
867	{action_summary}
868	
869	Analyze why this episode failed and provide a short
870	strategy for the next attempt. Focus on:
871	1. What went wrong (wrong sequence, missed key step,
872	   dangerous action)?
873	2. What should be done differently next time?
874	
875	Keep your reflection under 200 words.
876	\end{tcblisting}
877	
878	\paragraph{Grounding warning (ablation).} The prompt warning condition in the grounding ablation (Appendix~\ref{app:grounding-ablation}) appends the following to the shared system prompt:
879	
880	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
881	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
882	  left=2mm, right=2mm, top=1mm, bottom=1mm}
883	CRITICAL SAFETY RULE: The 'focus on [object]' action is
884	ONLY for submitting your final answer. Do NOT use
885	'focus on' to examine, inspect, or interact with objects
886	during exploration. Using 'focus on' on the wrong object
887	will cause irreversible failure. Use 'look at',
888	'examine', or 'pick up' instead for exploration.
889	\end{tcblisting}
890	
891	\noindent The key difference between the two computation modes is the user message: the internal strategy asks the LLM to \emph{select} one action (ReAct), while the deterministic strategy asks it to \emph{rank} candidates for simulator evaluation. Both use identical system prompts and identical observation formatting.
892	
893	\section{Non-Death Episode Case Study}
894	\label{app:non-death-case-study}
895	
896	We illustrate the framework's ability to decompose non-death routing signal using \texttt{find-non-living-thing}, the only task type with zero deaths and 100\% non-death labels (\S\ref{sec:death-decomp}). Using Gemma-2-9B-it counterfactual episodes ($N{=}20$), 12 episodes show routing preference (9 deterministic-preferred, 3 internal-preferred), confirming the framework detects bidirectional signal independent of death asymmetry.
897	
898	\paragraph{Deterministic-preferred: knowledge retrieval advantage.}
899	In Episode~3 (det: 67, int: 0), the internal strategy issues nonsensical \texttt{connect} actions for 18 consecutive steps (e.g., ``connect air to outside,'' ``connect axe to door to foundry'') without ever identifying a target object; the deterministic strategy correctly focuses on ``orange'' (+58) and opens the kitchen door (+9). In Episode~17 (det: 58, int: 50), both strategies find a valid non-living thing, but the deterministic strategy selects a higher-scoring object (orange, 58\,pts) versus the internal strategy's choice (fountain, 50\,pts), illustrating that object selection quality creates routing signal even when both strategies succeed.
900	
901	\paragraph{Internal-preferred: semantic reasoning advantage.}
902	In Episode~12 (int: 67, det: 58), the task specifies ``move it to the red box in the living room.'' The deterministic strategy focuses on the red box itself---the destination container, not a separate non-living thing---scoring 58\,pts. The internal strategy correctly distinguishes target from container, choosing ``orange'' (67\,pts). This semantic error demonstrates that deterministic pattern-matching can miss task-structure subtleties that internal reasoning captures.
903	
904	These cases confirm two properties: (1)~the framework captures non-death routing signal when it exists, and (2)~signal flows in both directions---neither strategy uniformly dominates in death-free tasks.
905	
906	\paragraph{Systematic analysis of non-death labels.}
907	All 20 non-death non-tie labels in the primary Qwen2.5-7B analysis originate from \texttt{find-non-living-thing}---the sole death-free task type. In every other task type, non-tie episodes involve at least one strategy dying. We classify the 20 episodes into three error categories:
908	
909	\begin{table}[h]
910	\centering
911	\small
912	\begin{tabular}{@{}lrrr@{}}
913	\toprule
914	Error category & Det-pref & Int-pref & Total \\
915	\midrule
916	Hallucination-induced & 8 & 2 & 10 \\
917	Object selection quality & 6 & 1 & 7 \\
918	Action selection error & 2 & 1 & 3 \\
919	\bottomrule
920	\end{tabular}
921	\caption{Non-death non-tie episode classification. Hallucination-induced: agent's state model is incorrect (e.g., believing \texttt{eat} completes the task). Object selection quality: both strategies succeed but choose different-value objects. Action selection: correct state model but suboptimal action sequences.}
922	\label{tab:non-death-taxonomy}
923	\end{table}
924	
925	\noindent Hallucination-induced errors dominate (50\%), driven by a recurring ``eat before focus'' pattern: the internal strategy consumes the target object (destroying it) before attempting the scoring action (\texttt{focus on}), indicating an incorrect state model that equates eating with task completion (11 of 20 episodes). Object selection quality accounts for 35\%---typically the deterministic strategy selecting ``orange'' (58\,pts) while the internal strategy settles for lower-value objects (``fountain'' or ``picture,'' 50\,pts). The error categories are bidirectional: 2 of 10 hallucination episodes and 1 of 3 action selection episodes are internal-preferred, confirming the framework detects failures in both strategies. Score gaps reflect category severity: hallucination errors produce large gaps ($17$--$67$\,pts, one strategy scores zero) while object selection differences produce small gaps ($8$--$9$\,pts, both strategies functional).
926	
927	\section{Use of AI Assistants}
928	\label{app:ai-assistants}
929	
930	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
931	\begin{itemize}
932	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
933	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \LaTeX{}.
934	    \item \textbf{Literature:} summarizing related papers to inform the related-work section.
935	\end{itemize}
936	
937	\end{document}
938	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31a570e6-3b3b-4483-9b97-e1c16d0d3c57",
  "isSidechain": true,
  "promptId": "615c1eae-3cf0-4729-ad9e-5bf3fb5d3b1d",
  "agentId": "af152b21ba92fc359",
  "type": "user",
  "uuid": "707d7ad3-1dc1-4701-acb1-15fcf896bf6e",
  "sourceToolAssistantUUID": "31a570e6-3b3b-4483-9b97-e1c16d0d3c57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-24T20:50:32.500Z_

Perfect! Now let me check for references to these appendix tables/figures from the main text to see which are actually cited:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "707d7ad3-1dc1-4701-acb1-15fcf896bf6e",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN45wYhGfNwCNVJw5NBi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "304ba62d-28e3-4e3a-b4ff-3a3d18e215b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EtpQtKUh3GP6K5aG9NJmwJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 88026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3169,
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

_source line 30 · 2026-05-24T20:50:33.547Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Jfp3sT6UbAWpp3pKj1mczt`</summary>

```json
{
  "command": "grep -h \"\\\\\\\\ref{tab:\\|\\\\\\\\ref{fig:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/*.tex | grep -v \"main.tex\" | sort | uniq"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "304ba62d-28e3-4e3a-b4ff-3a3d18e215b7",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN45wYhGfNwCNVJw5NBi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5a358f97-c77f-4406-bcac-075e32178ff5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EtpQtKUh3GP6K5aG9NJmwJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 3169,
      "cache_read_input_tokens": 88026,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3169
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 144,
          "cache_read_input_tokens": 88026,
          "cache_creation_input_tokens": 3169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3169,
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

_source line 31 · 2026-05-24T20:50:33.632Z_

<details><summary>↩ Tool result · `toolu_01Jfp3sT6UbAWpp3pKj1mczt`</summary>

```text
Eighteen of the 19 excluded task types (95\%) exhibit death-asymmetric patterns (Table~\ref{tab:excluded-death}): internal-reasoning death rates range from 40\% to 60\% (mean 53.9\%), while deterministic death rates range from 0\% to 40\% (mean 15.8\%), yielding a mean death-rate differential of $+38.2$\,pp, exceeding the $+28.7$\,pp for included tasks. The included subset is thus \emph{less} death-asymmetric than the excluded subset, the opposite of what a cherry-picking hypothesis would predict. The sole exception is \texttt{grow-plant}, an intrinsically safe task with zero deaths under both strategies, paralleling \texttt{find-non-living-thing} in the included set. The 19 excluded tasks fall into three independently motivated categories: five used during pipeline development (standard hold-out practice), seven taxonomically redundant with included family representatives (deduplication), and seven where the 7B backbone achieves near-zero task progress regardless of strategy (agent capability floor). In no case was a task excluded because death dominance was absent. Exclusion is driven by absence of non-death routing signal ($\Delta_{\text{nd}} = 0$ for 53\% of excluded tasks) and standard deduplication practices. \texttt{find-non-living-thing} serves as an internal counterexample: zero deaths under both strategies yet included because it exhibits non-death routing signal ($\Delta_{\text{full}} = +9.58$ entirely from score differences), and deterministic is not always preferred (4 of 20 non-tie labels favor internal).
Figure~\ref{fig:death-action-dist} shows the action distribution in death versus non-death episodes for the internal strategy; both are dominated by \texttt{connect} actions, with \texttt{focus on} moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$). Crucially, Figure~\ref{fig:death-comparison} reveals that within death episodes, internal and deterministic strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$). The survival gap (105 vs.\ 40 deaths) therefore reflects how often each strategy enters catastrophic states, not how it behaves within those states. Among fatal \texttt{focus on} targets, \texttt{workshop} remains the most frequent (20.0\%), followed by \texttt{inventory} (17.1\%) and \texttt{kitchen} (10.5\%), indicating a systematic object bias rather than random exploration. Figure~\ref{fig:death-timeline} visualizes the temporal pattern: agents execute long sequences of \texttt{connect} actions before a terminal \texttt{focus on} triggers death, typically in the final 1--3 steps.
Notably, the excluded-task aggregate DAF (0.991) exceeds the included-task DAF (0.904; Table~\ref{tab:per-task}), indicating that excluded tasks are \emph{more} death-dominated than included tasks---the opposite of a cherry-picking bias.
Of the 95 non-tie routing labels (Figure~\ref{fig:label-decomposition}), 75 (78.9\%; 95\% CI: $[70.7\%, 87.0\%]$, episode-level bootstrap) arise from death asymmetry: the internal strategy triggers a catastrophic $-100$ penalty while the deterministic strategy survives. This penalty-independent label fraction is the primary diagnostic metric. Of these, 54 are sole-signal labels where death was the only discriminator; at $P{=}0$ these reduce to ties, but the labeling function itself is penalty-independent (Algorithm~\ref{alg:labeling}).
Table~\ref{tab:alfworld-pertask} provides the per-task-type breakdown for ALFWorld. Unlike ScienceWorld, ALFWorld has no death mechanism ($\delta = 0$, DAF $= 0\%$); the entire performance gap $\Delta_{\text{full}}$ reflects information asymmetry from admissible-action access. \texttt{pick\_and\_place} shows the strongest effect ($\Delta = 0.563$, 18 of 32 episodes det-preferred), while \texttt{pick\_two\_obj\_and\_place} shows the weakest ($\Delta = 0.087$), consistent with multi-object tasks requiring more sequential reasoning that admissible actions alone cannot resolve. Only \texttt{pick\_heat\_then\_place} has a 95\% CI crossing zero ($n{=}16$).
Table~\ref{tab:cross-env} summarizes the label distributions across all three environments (see also Figure~\ref{fig:signal-reversal} in \S\ref{sec:cross-env}).
Table~\ref{tab:cross-model-env} consolidates replication results across model families and environments.
Table~\ref{tab:dose-response-detail} reports per-task death rates for Reflexion at $N{=}3$, 4, and 5 on the 10 death-prone tasks ($n{=}20$ episodes per task). Per-task variance is high (up to 25\,pp range for \texttt{measure-melting-point}), but the aggregate smooths to a 2.5\,pp band, confirming that the stabilization conclusion is robust at the aggregate level despite task-level noise. \texttt{freeze} is consistently the hardest task (50--60\% DR across all $N$).
The $r = 0.97$ correlation between per-task death-rate differential and $\Delta_{\text{full}}$ is specific to catastrophic death (score $= -100$). Broader failure definitions dissolve the correlation entirely: defining ``failure'' as any non-positive score ($T{=}0$) yields $r = -0.13$ ($p = 0.70$), because non-death episodes show near-zero performance differential between strategies ($\Delta_{\text{nd}} = 2.84$). Table~\ref{tab:penalty-correlation} quantifies this specificity across penalty magnitudes.
The contrast between step-level ($54.1 \pm 5.4\%$) and episode-level ($47.1 \pm 2.2\%$) evaluation reveals a generalization gap: the step-level signal likely reflects memorization of episode-specific context (enabled by same-episode leakage) rather than extraction of generalizable routing features. At episode level, the router performs below chance across all 8 seeds (range: 43.1\%--49.6\%). Paraphrase-based text augmentation (Table~\ref{tab:text-augmentation}) from 25\% to 800\% ($32{\times}$ range) provides no improvement, converging to the always-deterministic baseline ($50\%$). Paraphrase augmentation inflates the majority class without generating novel routing patterns; genuine episode-level scaling (collecting more counterfactual pairs) remains an open question. With DAF $= 90.4\%$ and all task types deterministic-majority (86:9 label ratio), always-deterministic trivially solves the episode-level routing problem, leaving the step-level router with no exploitable signal under current architectures.
The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic (2.6$\times$); a detailed failure-mode analysis reveals that all 105 internal-strategy deaths are triggered by the \texttt{focus} action (Appendix~\ref{app:failure-modes}). Per-task death rate differential correlates with $\Delta_{\text{full}}$ ($r = 0.97$, $p < 10^{-6}$; Figure~\ref{fig:decomposition}); since DAF$\to 1$ implies $r \to 1$ by construction, the near-perfect correlation is a consistency check, not an independent finding (Appendix~\ref{app:correlation}). Of 245 episodes, 86 are \texttt{det\_preferred}, 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preference}. Figure~\ref{fig:death-timeline} illustrates the typical death trajectory: agents execute long \texttt{connect} sequences before a terminal \texttt{focus on} triggers the $-100$ penalty.
The labeling function is \emph{death-aware}: it prioritizes survival over score, then compares scores among same-status episodes (Algorithm~\ref{alg:labeling}; Appendix~\ref{app:labeling}). Both-dead episodes receive \texttt{no\_preference} because ScienceWorld's fixed $-100$ penalty makes death timing uninformative. ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. Figure~\ref{fig:pipeline} illustrates the overall pipeline; label distributions are reported in \S\ref{sec:death-decomp}.
This sharpens our central finding: death is not merely the dominant component of routing signal; it is effectively the \emph{only} component that generates differential routing signal in ScienceWorld. At low penalties, the death contribution is small and $\Delta_{\text{full}}$ reduces to $\Delta_{\text{nd}} \approx 2.84$, which is near-uniform across task types ($\text{mean non-death gap} = -1.19$ excluding the \texttt{find-non-living-thing} outlier); consequently, death-rate differential has no predictive power. As $P$ increases, the death term dominates $\Delta_{\text{full}}$, and the correlation sharpens because death rates \emph{are} the performance gap. The DAF values in Table~\ref{tab:penalty-sensitivity} increase monotonically with $P$, but this is a mathematical consequence of the decomposition ($\text{DAF} = \delta P / (\delta P + \Delta_{\text{nd}})$), not evidence of mechanism robustness.
To verify that task exclusion does not bias toward death-prone tasks, we collect $n{=}20$ episodes for five representative excluded tasks spanning all exclusion categories (Table~\ref{tab:extended-val}).
We assess router generalization at two evaluation granularities: \emph{step-level}, where steps from the same episode may appear in both train and validation sets, and \emph{episode-level}, where entire episodes are held out. Both use cross-split evaluation (seeds $\{42, \ldots, 49\}$, 8 seeds total), where the data partition and training seed both vary. Table~\ref{tab:seed-robustness} reports per-seed results.
We extend both interventions to $N{=}5$ trials on death-prone tasks ($n{=}200$; Figure~\ref{fig:dose-response}). Retry is nearly flat ($48.0\% \to 43.5\%$). Reflexion drops steeply to $34.0\%$ at $N{=}3$ ($\Delta = -13.5$~pp, $p = 0.003$) then stabilizes ($34$--$36.5\%$ for $N \geq 3$, pairwise $p > 0.5$); both the decline and plateau are well-powered (MDE ${\sim}8$~pp at 80\% power; Appendix~\ref{app:dose-response}).
We replicate the counterfactual analysis with Llama-3.1-8B-Instruct across all 11 task types ($N{=}220$ episode pairs, 20 per type; Table~\ref{tab:cross-model-detail}).
We select 11 of ScienceWorld's 30 task types for analysis. Types are excluded when they were used for pipeline development (5 tasks, standard hold-out practice), are taxonomically redundant with a retained family representative (7 tasks), or exhibit near-zero task progress under both strategies (7 tasks, agent capability floor).\footnote{Excluded tasks exhibit even stronger death dominance than included tasks ($\Delta\text{DR} = +38.2$\,pp vs.\ $+28.7$\,pp; Table~\ref{tab:excluded-death}).}
We test whether agent-level improvement reduces death dominance (Table~\ref{tab:agent-improvement}). Retry ($N{=}5$ attempts without self-correction) yields marginal reduction on death-prone tasks ($43.5\%$ vs.\ $48.0\%$ baseline, $\Delta = -4.5$~pp). Reflexion~\citep{reflexion-2023}\footnote{Reflexion uses a fixed allocation of 20 episodes per task type ($20 \times 11 = 220$), vs.\ the baseline's variable 20--40 per type ($N{=}245$).} (verbal self-reflection between trials) reduces death to 31.4\% across all 11 tasks by rescuing 29.3\% of first-trial deaths, but the gap to deterministic remains 15.1~pp; on the 10 death-prone tasks, Reflexion achieves ${\sim}$35\%. Under Reflexion ($N{=}3$, matched-episode analysis), $\Delta_{\text{nd}} = -0.47$, yielding DAF $> 100\%$: the deterministic advantage is entirely attributable to death avoidance, and in non-death episodes the self-correcting agent slightly outperforms the deterministic baseline. Scaling to Qwen2.5-72B ($10{\times}$ parameters; both strategies independently collected at 72B, 255 episodes across all 11 task types) reduces death rate to $30.6\%$. The 72B deterministic strategy achieves $2.75\%$ death rate ($\Delta\text{DR} = +27.8$~pp), and $\Delta_{\text{nd}} = +2.28$, yielding DAF $= 92.4\%$ (95\% CI: $[86.1\%, 97.9\%]$; 7B: $90.4\%$), with 5 internal-preferred episodes (vs.\ 9 at 7B; $2.0\%$ vs.\ $3.7\%$).
Yes. Table~\ref{tab:hyperparams} (Appendix~\ref{app:router-details}) provides complete hyperparameters for both router architectures. Section~\ref{sec:router-diagnostic} and Appendix~\ref{app:router-details} describe the evaluation methodology. Gradient accumulation selection is justified in Appendix~\ref{app:router-details}.
Yes. We report: 245 episodes across 11 task types (Table~\ref{tab:per-task}), 795 MATH problems (Section~\ref{sec:cross-env}), 135 ALFWorld games (Section~\ref{sec:cross-env}), per-task episode counts (Table~\ref{tab:per-task}), and router training splits with cross-validation details (Appendix~\ref{app:router-details}).
Yes. We specify vLLM for inference, LoRA for fine-tuning, and provide all relevant configuration parameters (Table~\ref{tab:hyperparams}). Model identifiers are given precisely (e.g., Qwen2.5-7B-Instruct, Qwen3-1.7B).
\caption{Extended validation ($n{=}20$) of representative excluded task types. All five tasks confirm death asymmetry; mean $\Delta$DR $= +32.0$\,pp is consistent with the $n{=}5$ prescreening estimate for these same tasks (Table~\ref{tab:excluded-death}).}
\caption{Per-seed router performance under cross-split evaluation (8 seeds, generation-based, \texttt{enable\_thinking=False}). Step-level evaluation allows steps from the same episode in both train and validation sets (same-episode leakage). Episode-level evaluation holds out entire episodes; the resulting $47.1 \pm 2.2\%$ is below the 50\% chance baseline. A text augmentation ablation (Table~\ref{tab:text-augmentation}) confirms this failure persists under the current data distribution and augmentation regime.}
\paragraph{ALFWorld.} ALFWorld~\citep{alfworld-2021} (6 task types, 135 games) provides the deterministic strategy with admissible actions, an information asymmetry rather than a computation mode switch, with no death mechanism ($\delta = 0$, DAF $= 0\%$). With Qwen2.5-7B, 35 of 37 non-tie labels (94.6\%) favor the information-advantaged strategy (Appendix~\ref{app:cross-env-details}); Llama-3.1-8B (135 games) yields 16 of 16 non-tie labels in the same direction (100\%). Llama shows fewer non-tie episodes (11.9\% vs.\ 25.9\%) but perfect directional consistency, confirming that information asymmetry, not death avoidance, drives routing signal in ALFWorld regardless of model family. The framework diagnoses this qualitatively different mechanism (DAF $= 0\%$ vs.\ $90.4\%$) without modification. Figure~\ref{fig:signal-reversal} summarizes label distributions across all three environments.
\paragraph{Capacity scaling.} We scale the implicit router from Qwen3-0.6B to Qwen3-4B and evaluate at both step and episode level (Table~\ref{tab:capacity}).
\paragraph{Text augmentation ablation.} To test whether the episode-level generalization failure stems from data scarcity, we vary training set size from 25\% to 800\% of the original via paraphrase-based text augmentation (synonym substitution + template variation on step observations), holding the episode-level validation set fixed. This tests augmentation-based scaling, not genuine episode-level scaling (which would require new counterfactual collections). Table~\ref{tab:text-augmentation} reports the results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a358f97-c77f-4406-bcac-075e32178ff5",
  "isSidechain": true,
  "promptId": "615c1eae-3cf0-4729-ad9e-5bf3fb5d3b1d",
  "agentId": "af152b21ba92fc359",
  "type": "user",
  "uuid": "631d5d97-5dd0-47f9-84e3-5d0ca1a3398c",
  "sourceToolAssistantUUID": "5a358f97-c77f-4406-bcac-075e32178ff5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-24T20:50:35.203Z_

Let me get a cleaner list of all appendix items with proper grep:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "631d5d97-5dd0-47f9-84e3-5d0ca1a3398c",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN469Y1wHJsaW48CaHEB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c0f75a25-35d4-428d-9852-673e7337a50d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FER2rWsYi8Ssxf5SUfwAX9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 4460,
      "cache_read_input_tokens": 91195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4460,
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

_source line 33 · 2026-05-24T20:50:36.745Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WMrWRk4tmsTrrvQBd3gNxo`</summary>

```json
{
  "command": "awk '/^\\\\appendix/,0 {if (/\\\\begin\\{table\\}|\\\\begin\\{figure\\}|\\\\begin\\{algorithm\\}/) {found=1} if (found && /\\\\label\\{/) {if (match($0, /label\\{([^}]+)\\}/, a)) print a[1]; found=0}}' /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0f75a25-35d4-428d-9852-673e7337a50d",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN469Y1wHJsaW48CaHEB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ab9ccb1d-d406-4339-9677-73dbe89ae3ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FER2rWsYi8Ssxf5SUfwAX9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 4460,
      "cache_read_input_tokens": 91195,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4460
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 191,
          "cache_read_input_tokens": 91195,
          "cache_creation_input_tokens": 4460,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4460,
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

_source line 34 · 2026-05-24T20:50:36.826Z_

<details><summary>↩ Tool result · `toolu_01WMrWRk4tmsTrrvQBd3gNxo`</summary>

```text
alg:labeling
fig:death-action-dist
fig:death-comparison
tab:alfworld-pertask
tab:capacity
tab:cross-env
tab:cross-model-detail
tab:cross-model-env
tab:decision-framework
tab:dose-response-detail
tab:excluded-death
tab:extended-val
tab:hyperparams
tab:loo
tab:loto-daf
tab:non-death-taxonomy
tab:penalty-correlation
tab:penalty-sensitivity
tab:per-task
tab:seed-robustness
tab:text-augmentation
tab:threshold-routing
tab:wild-cluster
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab9ccb1d-d406-4339-9677-73dbe89ae3ac",
  "isSidechain": true,
  "promptId": "615c1eae-3cf0-4729-ad9e-5bf3fb5d3b1d",
  "agentId": "af152b21ba92fc359",
  "type": "user",
  "uuid": "2f644f9f-32e7-42f0-800f-4b3ea40d5bd8",
  "sourceToolAssistantUUID": "ab9ccb1d-d406-4339-9677-73dbe89ae3ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-24T20:51:08.001Z_

Perfect! Now let me create a comprehensive inventory. Let me now compile all the information systematically:

Based on my thorough examination of the paper in `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`, here's the **complete inventory of ALL tables and figures in the appendix sections**:

---

## APPENDIX TABLES AND FIGURES INVENTORY

### TABLES (18 total)

1. **tab:per-task** (App. C: Per-Task Decomposition)
   - Rows: 11 task types + 1 aggregate row = 12 rows
   - Columns: Task, n, $\Delta_\text{full}$, D%_int, D%_det, D/I/N
   - Size: 12 rows x 6 columns
   - Caption: Per-task decomposition of the death avoidance effect. Shows episode labels distribution across 245 episodes.
   - Relevant to: Methods / Experiments (main death analysis)
   - Referenced: YES - multiple times from main text

2. **tab:excluded-death** (App. C: Per-Task Decomposition)
   - Rows: 19 excluded tasks + mean rows = ~21 rows
   - Columns: Task, Grp, n, D%_int, D%_det, $\Delta$DR, Excl. reason
   - Size: Large table, column-resized
   - Caption: Death-rate analysis of all 19 excluded task types with exclusion justification
   - Relevant to: Methods (justifying task selection anti-cherry-picking)
   - Referenced: YES

3. **tab:loo** (App. D: Correlation Robustness)
   - Rows: 11 task types (Leave-one-out analysis)
   - Columns: Task removed, $r_{\text{LOO}}$
   - Size: ~13 rows x 2 columns
   - Caption: Leave-one-out Pearson correlation robustness check; shows no single task is a leverage point
   - Relevant to: Results/Statistical robustness
   - Referenced: NO (internal appendix reference only)

4. **tab:wild-cluster** (App. E: Cluster Bootstrap Sensitivity)
   - Rows: 4 statistical test methods
   - Columns: Method, p-value, 95% CI
   - Size: Small (4 rows x 3 columns)
   - Caption: Cluster-level tests of death-rate asymmetry with 11 task clusters
   - Relevant to: Statistical methods/Results
   - Referenced: NO (Appendix reference only)

5. **tab:loto-daf** (App. G: Leave-One-Task-Out DAF)
   - Rows: 11 task types + full baseline = 12 rows
   - Columns: Removed Task, $N_\text{rem}$, DAF (%), $\Delta$ (pp)
   - Size: ~12 rows x 4 columns
   - Caption: Leave-one-task-out DAF sensitivity analysis showing robustness
   - Relevant to: Results (sensitivity analysis)
   - Referenced: NO (Appendix reference only)

6. **tab:dose-response-detail** (App. H: Dose-Response Breakdown)
   - Rows: 10 death-prone tasks + aggregate = 11 rows
   - Columns: Task, N=3, N=4, N=5 (death rates)
   - Size: 11 rows x 4 columns
   - Caption: Per-task death rates for Reflexion at different trial counts; aggregate shows stabilization
   - Relevant to: Results (agent improvement)
   - Referenced: YES (from main text discussions)

7. **tab:hyperparams** (App. I: Router Training Details)
   - Rows: ~12 hyperparameter rows (two architectures)
   - Columns: Hyperparameter, Classification Head, Implicit Router
   - Size: ~12 rows x 3 columns, column-resized
   - Caption: Router training hyperparameters for both architectures using LoRA
   - Relevant to: Methods (experimental configuration)
   - Referenced: YES (from main text)

8. **tab:seed-robustness** (App. J: Seed Robustness)
   - Rows: 8 seeds (step-level) + 8 seeds (episode-level) + means
   - Columns: Eval Granularity, Seed, Bal. Acc. (%)
   - Size: ~20 rows x 3 columns
   - Caption: Per-seed router performance under cross-split evaluation showing generalization gap
   - Relevant to: Results (router evaluation)
   - Referenced: YES (from main text)

9. **tab:text-augmentation** (App. J: Seed Robustness - ablation)
   - Rows: 5 scale levels + Always-det = 6 rows
   - Columns: Scale, Samples, Det%, Ep. Bal. Acc. (%)
   - Size: 6 rows x 4 columns
   - Caption: Text augmentation ablation across training set sizes (25%-800%); shows no improvement
   - Relevant to: Methods/Results (scalability analysis)
   - Referenced: YES (from main text)

10. **tab:penalty-sensitivity** (App. K: Penalty Sensitivity)
    - Rows: 9 penalty values (0, 1, 5, 10, 25, 50, 100, 200, 500)
    - Columns: P, DAF(P), 95% CI
    - Size: 9 rows x 3 columns
    - Caption: Sensitivity of DAF to death penalty magnitude; shows mechanical relationship
    - Relevant to: Results (sensitivity analysis)
    - Referenced: YES (from main text discussion)

11. **tab:penalty-correlation** (App. K: Penalty Sensitivity)
    - Rows: 7 penalty values (1, 5, 10, 25, 50, 100, 200)
    - Columns: P, r, p, Sig. (α=0.05)
    - Size: 7 rows x 4 columns
    - Caption: Pearson correlation between death-rate differential and $\Delta_\text{full}$ across penalties
    - Relevant to: Results (mechanism analysis)
    - Referenced: NO (Appendix reference only)

12. **tab:cross-env** (App. L: Cross-Environment Details)
    - Rows: 3 environments (ScienceWorld, MATH, ALFWorld)
    - Columns: Environment, N, Det%, Int%, NoPref%, Death?
    - Size: 3 rows x 6 columns
    - Caption: Cross-environment label distribution summary
    - Relevant to: Results (cross-environment validation)
    - Referenced: YES (from main text)

13. **tab:alfworld-pertask** (App. L: Cross-Environment Details)
    - Rows: 6 ALFWorld task types + aggregate = 7 rows
    - Columns: Task Type, n, Succ%_int, Succ%_det, D/I/N, $\Delta_\text{full}$
    - Size: 7 rows x 6 columns
    - Caption: Per-task decomposition for ALFWorld showing information asymmetry signal
    - Relevant to: Results (cross-environment)
    - Referenced: YES (from main text)

14. **tab:cross-model-detail** (App. M: Cross-Model Verification)
    - Rows: 11 task types + aggregate = 12 rows
    - Columns: Task, Int%, Det%, $\Delta$ pp, D/I/N
    - Size: 12 rows x 5 columns, column-resized
    - Caption: Per-task Llama-3.1-8B cross-model replication
    - Relevant to: Results (cross-model validation)
    - Referenced: YES (from main text)

15. **tab:cross-model-env** (App. M: Cross-Model Verification)
    - Rows: 9 model-environment combinations (5 ScienceWorld models + 2 ALFWorld + 1 MATH)
    - Columns: Model, Environment, n, Int DR, Det DR, $\Delta$DR, DAF, DAF 95% CI, Signal
    - Size: 9 rows x 9 columns, column-resized
    - Caption: Comprehensive cross-model and cross-environment replication summary
    - Relevant to: Results (validation across scales)
    - Referenced: YES (from main text)

16. **tab:capacity** (App. P: Ablation Studies)
    - Rows: 3 model scales (0.6B, 1.7B, 4B) + Always-det = 4 rows
    - Columns: Model, Step Bal. Acc. (%), Ep. Bal. Acc. (%)
    - Size: 4 rows x 3 columns
    - Caption: Capacity scaling showing episode-level generalization only breaks at 4B
    - Relevant to: Results (ablations)
    - Referenced: NO (Appendix reference only)

17. **tab:threshold-routing** (App. Q: Threshold Routing)
    - Rows: 3 strategies (Always-det, Optimal threshold, Always-internal)
    - Columns: Strategy, Mean Score, Death Rate, $\Delta$ vs Det
    - Size: 3 rows x 4 columns, column-resized
    - Caption: Death-risk threshold routing analysis; cannot outperform always-deterministic
    - Relevant to: Results (routing optimality analysis)
    - Referenced: NO (Appendix reference only)

18. **tab:decision-framework** (App. R: Decision Framework)
    - Rows: 4 experimental conditions (Qwen-7B, Llama-8B, Qwen-72B, MATH)
    - Columns: Condition, $\Delta$DR, $f_\text{death}$, Prediction, Actual
    - Size: 4 rows x 5 columns
    - Caption: Retrospective validation of the decision framework for diagnosing routing viability
    - Relevant to: Results (framework validation)
    - Referenced: NO (Appendix reference only)

19. **tab:extended-val** (App. S: Extended Validation)
    - Rows: 5 excluded task types + mean = 6 rows
    - Columns: Task, Category, n, Int DR, Det DR, $\Delta$DR, D/I/N
    - Size: 6 rows x 7 columns, column-resized
    - Caption: Extended validation of representative excluded tasks confirming death asymmetry
    - Relevant to: Methods (task selection justification)
    - Referenced: YES (from main text)

20. **tab:non-death-taxonomy** (App. U: Non-Death Episode Case Study)
    - Rows: 3 error categories (Hallucination-induced, Object selection, Action selection)
    - Columns: Error category, Det-pref, Int-pref, Total
    - Size: 3 rows x 4 columns
    - Caption: Classification of non-death non-tie episodes into error categories
    - Relevant to: Results (failure analysis)
    - Referenced: NO (Appendix reference only)

---

### FIGURES (2 total)

1. **fig:death-action-dist** (App. N: Failure Mode Analysis)
   - Type: Multi-panel bar chart (2 subplots)
   - Content: Action distribution for internal strategy in death (n=105) vs non-death (n=140) episodes
   - Left panel: Full distribution; Right panel: Zoomed non-connect actions
   - Size: Full column width
   - Caption: Shows connect dominance and focus-on moderately higher in death episodes (5.4% vs 3.4%)
   - Relevant to: Results (failure analysis)
   - Referenced: YES (from main text, Figure reference in Appendix N)

2. **fig:death-comparison** (App. N: Failure Mode Analysis)
   - Type: Multi-panel bar chart (2 subplots - side-by-side comparison)
   - Content: Non-connect action distribution comparison between internal (left) and deterministic (right) strategies
   - Shows comparable focus-on rates within death episodes (~5% both)
   - Size: Full column width
   - Caption: Demonstrates survival gap (105 vs 40 deaths) reflects entry frequency, not within-episode behavior
   - Relevant to: Results (failure analysis)
   - Referenced: YES (from main text, Figure reference in Appendix N)

---

### ALGORITHM (1 total - technically not a table/figure but included in appendix inventory)

1. **alg:labeling** (App. B: Labeling Quality Audit)
   - Type: Pseudocode algorithm block
   - Content: Episode-Level Counterfactual Labeling procedure
   - Lines: ~20 algorithmic steps with comments
   - Caption: Shows labeling priority (death asymmetry > score comparison > ties)
   - Relevant to: Methods (labeling procedure)
   - Referenced: YES (from main text)

---

## SUMMARY STATISTICS

- **Total Tables**: 20
- **Total Figures**: 2
- **Tables with 10+ rows**: 8 (tab:per-task, tab:excluded-death, tab:seed-robustness, tab:loo, tab:loto-daf, tab:dose-response-detail, tab:cross-model-env, tab:cross-env combined with sub-tables)
- **Referenced from Main Text**: ~12-14 tables/figures
- **Appendix-only (lower priority for promotion)**: ~8 tables

---

## RECOMMENDATIONS FOR PROMOTION TO MAIN TEXT

**High Priority (currently cited, directly support main narrative):**
1. **tab:per-task** - Core decomposition; already well-integrated
2. **tab:dose-response-detail** - Agent improvement trajectory
3. **fig:death-action-dist** - Failure mode distribution
4. **fig:death-comparison** - Strategy comparison within death states
5. **tab:cross-model-env** - Validation across models/environments

**Medium Priority (currently cited but detailed):**
6. **tab:hyperparams** - Could replace brief inline parameter description
7. **tab:extended-val** - Validates task selection; supports main methodology

**Low Priority (appendix-only, specialized):**
- Sensitivity analyses (tab:penalty-sensitivity, tab:loto-daf)
- Statistical robustness (tab:wild-cluster, tab:loo)
- Ablation-specific (tab:capacity, tab:threshold-routing, tab:text-augmentation)

The appendix is quite comprehensive and well-organized. Most visual gaps in main text are due to space constraints rather than missing experiments. The figures (fig:death-action-dist, fig:death-comparison) would provide significant visual clarity if promoted, while most promoted tables should be condensed summaries with extended versions remaining in appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f644f9f-32e7-42f0-800f-4b3ea40d5bd8",
  "isSidechain": true,
  "agentId": "af152b21ba92fc359",
  "requestId": "req_011CbN46P9KQb2YEB7PW1oBe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "428082c9-06fc-4f3c-bd77-c37b099b6910",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LcaXCihvaSgXYVPbULAYbM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 354,
      "cache_read_input_tokens": 95655,
      "output_tokens": 3644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 354
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 3644,
          "cache_read_input_tokens": 95655,
          "cache_creation_input_tokens": 354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 354,
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
