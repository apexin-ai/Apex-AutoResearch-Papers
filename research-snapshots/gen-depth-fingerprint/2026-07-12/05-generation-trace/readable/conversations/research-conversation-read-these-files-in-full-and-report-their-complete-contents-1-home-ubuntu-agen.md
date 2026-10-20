# Research conversation: Read these files in full and report their complete contents: 1. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a59633b679c2ca02e.jsonl`
- **Structured JSON:** [`6796750b71b725389bf8.json`](../../sessions/67/6796750b71b725389bf8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-25T08:30:47.127Z_

Read these files in full and report their complete contents:
1. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex (just the first 80 lines to find the abstract)
2. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex (full file)
3. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/generation.tex (full file if exists)
4. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/features.tex (full file if exists)
5. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/evaluation.tex (full file if exists)

Report ALL numbers, statistics, F1 scores, effect sizes, model counts, dataset sizes, etc. found in each file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b1f1579c-3a08-4738-a0d2-62cdbce4d803",
  "agentId": "a59633b679c2ca02e",
  "type": "user",
  "uuid": "593afb0e-ffd6-425f-95fe-7a75968d1f02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T08:30:48.785Z_

I'll read these files for you. Let me start by checking which files exist and then reading them.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "593afb0e-ffd6-425f-95fe-7a75968d1f02",
  "isSidechain": true,
  "agentId": "a59633b679c2ca02e",
  "requestId": "req_011CbNyV9T83rdysvEnk5zth",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0b8e2aed-c678-44a5-9ff1-cb5bfb358fd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DSgJbLRWjrAFnMJEYTgVxa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39802,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39802,
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

_source line 3 · 2026-05-25T08:30:49.211Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VwhFjV4jsUHReW4v9juMWW`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b8e2aed-c678-44a5-9ff1-cb5bfb358fd7",
  "isSidechain": true,
  "agentId": "a59633b679c2ca02e",
  "requestId": "req_011CbNyV9T83rdysvEnk5zth",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5a8fe1be-82c3-4e5a-b992-ef224544cb49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DSgJbLRWjrAFnMJEYTgVxa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39802,
      "cache_read_input_tokens": 0,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 39802
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 121,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 39802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 39802,
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

_source line 4 · 2026-05-25T08:30:49.351Z_

<details><summary>↩ Tool result · `toolu_01VwhFjV4jsUHReW4v9juMWW`</summary>

```text
total 16052
drwxr-xr-x  8 ubuntu ubuntu    4096 May 25 08:21 .
drwxr-xr-x 12 ubuntu ubuntu    4096 May 20 06:45 ..
drwxr-xr-x  2 ubuntu ubuntu    4096 May 17 12:26 _pdf_images_r8
drwxr-xr-x  2 ubuntu ubuntu    4096 May 17 13:24 _pdf_images_r9
drwxr-xr-x  2 ubuntu ubuntu    4096 May 17 13:28 _pdf_images_r9b
drwxr-xr-x  2 ubuntu ubuntu    4096 May 19 12:50 _visual_check
-rw-r--r--  1 ubuntu ubuntu    1481 May 24 23:44 abstract.tex
-rw-r--r--  1 ubuntu ubuntu   11615 May 15 04:58 acl.sty
-rw-r--r--  1 ubuntu ubuntu   45186 May 15 04:58 acl_natbib.bst
-rw-r--r--  1 ubuntu ubuntu    4967 May 25 08:07 appendix_9gen_scale.tex
-rw-r--r--  1 ubuntu ubuntu     713 May 22 15:30 appendix_ablation.tex
-rw-r--r--  1 ubuntu ubuntu     246 May 25 04:19 appendix_ai_assistants.tex
-rw-r--r--  1 ubuntu ubuntu    6752 May 22 15:30 appendix_classifier.tex
-rw-r--r--  1 ubuntu ubuntu    2268 May 22 15:30 appendix_confusion_matrix.tex
-rw-r--r--  1 ubuntu ubuntu     690 May 23 07:36 appendix_convergence.tex
-rw-r--r--  1 ubuntu ubuntu    1707 May 22 15:30 appendix_cross_model_detail.tex
-rw-r--r--  1 ubuntu ubuntu    2591 May 22 15:30 appendix_cross_temp.tex
-rw-r--r--  1 ubuntu ubuntu    2625 May 22 15:30 appendix_dataset_stats.tex
-rw-r--r--  1 ubuntu ubuntu    4039 May 22 15:30 appendix_ddr_causality.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a8fe1be-82c3-4e5a-b992-ef224544cb49",
  "isSidechain": true,
  "promptId": "b1f1579c-3a08-4738-a0d2-62cdbce4d803",
  "agentId": "a59633b679c2ca02e",
  "type": "user",
  "uuid": "635945b3-fe34-4bbf-8778-b0e1eb286069",
  "sourceToolAssistantUUID": "5a8fe1be-82c3-4e5a-b992-ef224544cb49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-25T08:30:50.634Z_

Now let me read the specific files you requested:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "635945b3-fe34-4bbf-8778-b0e1eb286069",
  "isSidechain": true,
  "agentId": "a59633b679c2ca02e",
  "requestId": "req_011CbNyVJttmEsrDjrvvCEwY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0e2fae68-7869-4f33-b52e-dc6899fd5170",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014X11N5QgkheCQ7GsKzqEJd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1596,
      "cache_read_input_tokens": 39802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1596,
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

_source line 6 · 2026-05-25T08:30:51.936Z_

<details open><summary>🔧 Tool call — Read · `toolu_01961JBLu6MjD2DH5g9YWwFC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e2fae68-7869-4f33-b52e-dc6899fd5170",
  "isSidechain": true,
  "agentId": "a59633b679c2ca02e",
  "requestId": "req_011CbNyVJttmEsrDjrvvCEwY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "48841157-4750-4722-9a13-6f1b88779183",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014X11N5QgkheCQ7GsKzqEJd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1596,
      "cache_read_input_tokens": 39802,
      "output_tokens": 264,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1596
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 264,
          "cache_read_input_tokens": 39802,
          "cache_creation_input_tokens": 1596,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1596,
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

### Tool call

_source line 7 · 2026-05-25T08:30:51.943Z_

<details open><summary>🔧 Tool call — Read · `toolu_015Xu2Ch3dnceYoksNE9XQTQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48841157-4750-4722-9a13-6f1b88779183",
  "isSidechain": true,
  "agentId": "a59633b679c2ca02e",
  "requestId": "req_011CbNyVJttmEsrDjrvvCEwY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f4614384-f666-42b2-8d6b-3464738d4cf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014X11N5QgkheCQ7GsKzqEJd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1596,
      "cache_read_input_tokens": 39802,
      "output_tokens": 264,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1596
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 264,
          "cache_read_input_tokens": 39802,
          "cache_creation_input_tokens": 1596,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1596,
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

_source line 8 · 2026-05-25T08:30:51.947Z_

<details><summary>↩ Tool result · `toolu_01961JBLu6MjD2DH5g9YWwFC`</summary>

```text
1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{graphicx}
10	\usepackage{booktabs}
11	\usepackage{enumitem}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{placeins}
15	\usepackage{multirow}
16	\usepackage{float}
17	\usepackage{stfloats}
18	\usepackage{alphalph}
19	\usepackage{tcolorbox}
20	\tcbuselibrary{breakable}
21	
22	\graphicspath{{../chart/}}
23	
24	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
25	\setlength{\floatsep}{8pt plus 2pt minus 2pt}
26	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
27	
28	\title{Depth Profiling: Classifying Recursive Generation Depth\\in Base-Model LLM Text}
29	
30	\author{Anonymous}
31	
32	\begin{document}
33	\raggedbottom
34	\maketitle
35	
36	\input{abstract}
37	
38	\input{introduction}
39	\input{related_work}
40	\input{method}
41	\input{results}
42	
43	\input{discussion}
44	\input{conclusion}
45	\input{limitations}
46	\bibliography{references}
47	
48	\appendix
49	\renewcommand{\thesection}{\alphalph{\value{section}}}
50	
51	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
52	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
53	
54	\input{appendix_dataset_stats}
55	
56	\section{Length Confound Analysis}
57	\label{app:length}
58	\input{appendix_length}
59	
60	\section{Prompt Type Generalization}
61	\label{app:prompt-type}
62	\input{appendix_prompt_type}
63	\FloatBarrier
64	
65	\section{Finer-Grained Depth Classification}
66	\label{app:finer-depth}
67	\input{appendix_finer_depth}
68	\FloatBarrier
69	
70	\section{End-to-End Depth Classification (QLoRA)}
71	\label{app:qlora}
72	\input{appendix_qlora}
73	\FloatBarrier
74	
75	\section{Leave-One-Feature-Out Analysis}
76	\label{app:lofo}
77	\input{appendix_lofo}
78	\FloatBarrier
79	
80	\subsection{Candidate Feature Screening}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48841157-4750-4722-9a13-6f1b88779183",
  "isSidechain": true,
  "promptId": "b1f1579c-3a08-4738-a0d2-62cdbce4d803",
  "agentId": "a59633b679c2ca02e",
  "type": "user",
  "uuid": "c9be4efd-9d3a-43af-aaed-d5c282b4d4f9",
  "sourceToolAssistantUUID": "48841157-4750-4722-9a13-6f1b88779183",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-25T08:30:51.949Z_

<details><summary>↩ Tool result · `toolu_015Xu2Ch3dnceYoksNE9XQTQ`</summary>

```text
1	\vspace{-1mm}
2	\section{Method}
3	\label{sec:method}
4	
5	\begin{table}[t!]
6	\centering
7	\footnotesize
8	\caption{Seven distributional features. ``Entropy'' features are per-token NLL under Pythia-410M (\S\ref{sec:features}); surface features require no reference model. DDR analysis (\S\ref{sec:results-differential}) reveals entropy mean, TTR, and hapax ratio drift with depth while entropy max, min, and tail decay remain near-stationary; entropy std is intermediate.}
9	\label{tab:features}
10	\setlength{\tabcolsep}{4pt}
11	\begin{tabular}{@{}llp{3.0cm}@{}}
12	\toprule
13	\textbf{Feature} & \textbf{Source} & \textbf{Measures} \\
14	\midrule
15	\texttt{entropy\_mean} \textit{\scriptsize(NLL)} & Ref.\ NLL & Central tendency of token surprise \\
16	\texttt{entropy\_std} \textit{\scriptsize(NLL)}  & Ref.\ NLL & Spread of token surprise \\
17	\texttt{entropy\_max} \textit{\scriptsize(NLL)}  & Ref.\ NLL & Maximum token surprise \\
18	\texttt{entropy\_min} \textit{\scriptsize(NLL)}  & Ref.\ NLL & Minimum token surprise \\
19	\texttt{tail\_decay}   & Ref.\ NLL & Log-prob decay slope (ranks 100--1K) \\
20	\midrule
21	\texttt{ttr}           & Surface & Type-token ratio \\
22	\texttt{hapax\_ratio}  & Surface & Proportion of hapax legomena \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	\begin{figure*}[t]
28	\centering
29	\includegraphics[width=\textwidth]{fig2_framework.pdf}
30	\caption{Depth profiling pipeline. (a)~Human seeds are iteratively fed through generator $G$ to produce chains of increasing depth. (b)~Seven features extracted from NLL distributions group into three DDR zones: drifting (red), intermediate (purple), near-stationary (blue). (c)~LOGO evaluation holds out one generator for testing.}
31	\label{fig:framework}
32	\end{figure*}
33	
34	\subsection{Task Formulation}
35	\label{sec:task}
36	
37	Given a text $x$, we predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$: human-written ($d{=}0$), first-generation LLM output ($d{=}1$), or text produced by two or more recursive LLM generations ($d{=}2{+}$).
38	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$ (human corpus), $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic autoregressive generation.
39	Depths beyond 2 are merged into $2{+}$ because feature convergence compresses inter-class margins at deeper levels (\S\ref{sec:results-differential}).
40	
41	\subsection{Generation Chain Construction}
42	\label{sec:generation}
43	
44	\looseness=-1 We construct generation chains using eight generators spanning five model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}, \textbf{Llama} (Llama-3.2-3B) \cite{llama3}, and \textbf{Mistral} (Mistral-7B-v0.3) \cite{mistral7b}.
45	\looseness=-1 These span a 13$\times$ parameter range (0.6B--8B) across five architectures; Qwen's overrepresentation (3/8) is a limitation mitigated by LOFO (F1\,=\,0.686; \S\ref{sec:results-classification}).
46	
47	\looseness=-1 For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
48	The same seed pool serves as gen-0 for all generators, controlling for input content; in LOGO evaluation this creates a potential train--test overlap for gen-0, addressed by our binary evaluation excluding gen-0 entirely (\S\ref{sec:results-baselines}).
49	Each seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\texttt{Continue the following text: \{text\}}''.
50	We generate up to depth~4 to empirically confirm convergence: 5-class analysis shows adjacent depths 2--4 become indistinguishable (F1\,$\approx$\,0.27; Appendix~\ref{app:finer-depth}), motivating the gen-2+ class collapse.
51	All generation uses temperature $\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.
52	After filtering chain breaks and passages too short for feature extraction, 37{,}058 texts remain across all depths (Appendix~\ref{app:dataset-stats}); depths 2--4 are collapsed into $2{+}$.
53	
54	\subsection{Feature Extraction}
55	\label{sec:features}
56	
57	\paragraph{Terminology.} Throughout this paper, we refer to per-token cross-entropy loss under a fixed reference model as ``entropy'' for conciseness; these are reference-model NLL values, not true information-theoretic entropy of the generating distribution.
58	
59	We use interpretable distributional statistics so that the DDR partition remains transparent; end-to-end neural features improve classification ($+$10.0\,pp; Appendix~\ref{app:qlora}) but obscure the decomposition (LOFO confirms both feature groups contribute independently; Appendix~\ref{app:lofo}).
60	
61	\looseness=-1 We extract seven distributional features per text (Table~\ref{tab:features}), covering the NLL distribution's location, spread, extremes, and tail structure, plus two reference-free surface diversity measures; six additional NLL statistics were rejected for redundancy ($|r| > 0.65$, $\Delta$F1\,$\leq$\,$-0.011$; Appendix~\ref{app:feature-candidate}).
62	
63	\paragraph{Reference-model features.}
64	\looseness=-1 A held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.
65	Cross-family reference validation (Appendix~\ref{app:cross-ref}) shows F1 spread of only 0.013 across Pythia, OLMo, and Qwen references, confirming DDR is reference-model agnostic; however, all tested references are causal LMs.
66	From the resulting NLL sequence, we extract five statistics: mean, standard deviation, maximum, and minimum of the token-level NLL, plus tail\_decay---the slope of the vocabulary-level averaged log-probability distribution in ranks 100--1000, capturing the power-law regime where depth-induced compression is most detectable.
67	
68	\paragraph{Surface features.}
69	Two features capture lexical diversity without requiring a reference model: type-token ratio (TTR) and the proportion of words appearing exactly once (hapax\_ratio).
70	
71	\paragraph{Feature complementarity.}
72	These features exhibit a \emph{differential depth response} (DDR), separating into drifting and non-drifting groups (\S\ref{sec:results-differential}; pairwise correlations in Appendix~\ref{sec:appendix-feature-correlation}).
73	TTR and hapax ratio are strongly correlated ($r = 0.97$); both are retained for marginal LOFO gains.
74	
75	\subsection{Evaluation Protocol}
76	\label{sec:evaluation}
77	
78	\paragraph{Cross-validation.}
79	\looseness=-1 We evaluate generalization via \textbf{Leave-One-Generator-Out (LOGO)} cross-validation: each fold holds out one generator entirely, so the classifier must generalize to a generator absent from training---the strictest per-model protocol for assessing deployment against previously unseen generators.
80	LOGO does not isolate family-level effects; \textbf{Leave-One-Family-Out (LOFO)} addresses this by holding out entire model families (binary F1\,=\,0.686; \S\ref{sec:results-classification}).
81	Generator subsets vary across experiments (Appendix~\ref{app:gen-subsets-section}).
82	
83	\paragraph{Classifier.}
84	\looseness=-1 We use XGBoost \cite{xgboost} throughout ($n\_\text{estimators}{=}200$, $\max\_\text{depth}{=}6$, learning rate $0.1$; fixed without tuning), with identical hyperparameters across all methods in Table~\ref{tab:baselines}.
85	Alternative classifiers (CORAL \cite{coral_ordinal}, CORN \cite{corn_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) yield comparable performance (Appendix~\ref{app:classifier}); hyperparameter sensitivity (max\_depth sweep) shows F1 variation $\leq$2.0\,pp, confirming discriminative power resides in the features, not the classifier.
86	
87	\paragraph{Metrics and statistical testing.}
88	The primary metric is \textbf{macro-averaged F1} over the three depth classes, with 95\% bootstrap confidence intervals (CIs; $n{=}1{,}000$).
89	All $p$-values are two-sided with Bonferroni correction within each family of simultaneous tests.
90	
91	\paragraph{Baselines.}
92	We compare the 7-feature ensemble against four single-score detection methods repurposed as depth predictors: Avg-LogProb, FastDetectGPT \cite{fast_detectgpt}, Binoculars \cite{binoculars}, and LD-Score \cite{ld_score}.
93	Each baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation to ensure a controlled comparison.
94	
95	\paragraph{Length confound control.}
96	Since TTR and hapax\_ratio are mechanically length-dependent, we verify depth signal is not a length artifact via length-matched subsampling that equalizes length distributions across depth classes (\S\ref{sec:results-classification}; Appendix~\ref{app:length}).
97	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4614384-f666-42b2-8d6b-3464738d4cf5",
  "isSidechain": true,
  "promptId": "b1f1579c-3a08-4738-a0d2-62cdbce4d803",
  "agentId": "a59633b679c2ca02e",
  "type": "user",
  "uuid": "7e085509-7f1b-43aa-8754-bcb3c5f7c353",
  "sourceToolAssistantUUID": "f4614384-f666-42b2-8d6b-3464738d4cf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T08:30:51.967Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PUCAKUdzDPHQ3s4E8h1Q9C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/evaluation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e085509-7f1b-43aa-8754-bcb3c5f7c353",
  "isSidechain": true,
  "agentId": "a59633b679c2ca02e",
  "requestId": "req_011CbNyVJttmEsrDjrvvCEwY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ebbc63fd-d33b-48f1-81a2-da880e760f48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014X11N5QgkheCQ7GsKzqEJd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1596,
      "cache_read_input_tokens": 39802,
      "output_tokens": 264,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1596
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 264,
          "cache_read_input_tokens": 39802,
          "cache_creation_input_tokens": 1596,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1596,
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

_source line 11 · 2026-05-25T08:30:51.974Z_

<details><summary>↩ Tool result · reported error · `toolu_01PUCAKUdzDPHQ3s4E8h1Q9C`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebbc63fd-d33b-48f1-81a2-da880e760f48",
  "isSidechain": true,
  "promptId": "b1f1579c-3a08-4738-a0d2-62cdbce4d803",
  "agentId": "a59633b679c2ca02e",
  "type": "user",
  "uuid": "d004be9a-2c97-43f6-a96b-6af23d847dd2",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f.",
  "sourceToolAssistantUUID": "ebbc63fd-d33b-48f1-81a2-da880e760f48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-25T08:30:53.448Z_

Let me check for the evaluation file and other files that might exist:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d004be9a-2c97-43f6-a96b-6af23d847dd2",
  "isSidechain": true,
  "agentId": "a59633b679c2ca02e",
  "requestId": "req_011CbNyVW7LNmmESACWhq7dG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9d87da88-fea7-47ed-849b-f59d079ed4c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UsnLsg5EXF72P2Smxojmk2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4176,
      "cache_read_input_tokens": 41398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4176,
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

_source line 13 · 2026-05-25T08:30:53.916Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01X7hULWmxw7oCFzo7MiRL4C`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/*.tex | grep -E \"(generation|features|evaluation|results)\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d87da88-fea7-47ed-849b-f59d079ed4c6",
  "isSidechain": true,
  "agentId": "a59633b679c2ca02e",
  "requestId": "req_011CbNyVW7LNmmESACWhq7dG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fd427fa6-fc7e-4f78-ae9d-2487e7cc154f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UsnLsg5EXF72P2Smxojmk2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4176,
      "cache_read_input_tokens": 41398,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4176
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 116,
          "cache_read_input_tokens": 41398,
          "cache_creation_input_tokens": 4176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4176,
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

_source line 14 · 2026-05-25T08:30:53.973Z_

<details><summary>↩ Tool result · `toolu_01X7hULWmxw7oCFzo7MiRL4C`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd427fa6-fc7e-4f78-ae9d-2487e7cc154f",
  "isSidechain": true,
  "promptId": "b1f1579c-3a08-4738-a0d2-62cdbce4d803",
  "agentId": "a59633b679c2ca02e",
  "type": "user",
  "uuid": "c385d218-00f5-44cb-a8eb-1dcb92ef3360",
  "sourceToolAssistantUUID": "fd427fa6-fc7e-4f78-ae9d-2487e7cc154f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-25T08:30:55.406Z_

Let me read the results file and the abstract:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c385d218-00f5-44cb-a8eb-1dcb92ef3360",
  "isSidechain": true,
  "agentId": "a59633b679c2ca02e",
  "requestId": "req_011CbNyVez8WciePZVMJA8PD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dd4706df-25ac-4154-98c6-754b7d272e93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Aqpqb5zJ6b2JDoei6Lh6T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 166,
      "cache_read_input_tokens": 45574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 166,
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

_source line 16 · 2026-05-25T08:30:55.873Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YFNATuZLPPYyu7CxYjS1UM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd4706df-25ac-4154-98c6-754b7d272e93",
  "isSidechain": true,
  "agentId": "a59633b679c2ca02e",
  "requestId": "req_011CbNyVez8WciePZVMJA8PD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2dbec7dd-0782-435f-a54c-75ac4345d244",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Aqpqb5zJ6b2JDoei6Lh6T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 166,
      "cache_read_input_tokens": 45574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 166,
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

### Tool result

_source line 17 · 2026-05-25T08:30:55.879Z_

<details><summary>↩ Tool result · `toolu_01YFNATuZLPPYyu7CxYjS1UM`</summary>

```text
1	% Abstract — Depth Profiling of Recursive LLM Generation Chains
2	\begin{abstract}
3	As large language model (LLM) outputs re-enter training corpora and seed further generation, understanding how recursive generation reshapes text distributions is critical for data provenance and corpus curation---yet existing detectors answer only the binary human-or-machine question, ignoring \emph{generation depth}: we introduce \emph{depth profiling} to address this gap.
4	We decompose distributional drift under recursive generation into location and shape components, revealing an asymmetry we term \emph{differential depth response} (DDR): across eight base-model generators from five families, negative log-likelihood (NLL) location features drift monotonically with depth (effect size $d{=}0.74$--$1.05$) while three shape features remain near-stationary ($d < 0.10$), with entropy std intermediate ($d{=}0.46$)---a ${\geq}8{\times}$ effect-size gap.
5	Prior work documents \emph{what converges}; the central finding here is \emph{what is approximately preserved}: shape stability complements location drift for ordinal depth grading without per-generator calibration, achieving leak-free binary F1\,=\,0.694 (gen-1 vs.\ gen-2+), cross-model binary F1\,=\,0.830, and 3-class F1\,=\,0.762 under leave-one-generator-out evaluation (gen-0 seeds shared across generators; \S\ref{sec:generation}).
6	Instruction tuning compresses DDR, bounding current applicability to base models.
7	\end{abstract}
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2dbec7dd-0782-435f-a54c-75ac4345d244",
  "isSidechain": true,
  "promptId": "b1f1579c-3a08-4738-a0d2-62cdbce4d803",
  "agentId": "a59633b679c2ca02e",
  "type": "user",
  "uuid": "8809a416-029b-4420-aa46-b67c92e58d2f",
  "sourceToolAssistantUUID": "2dbec7dd-0782-435f-a54c-75ac4345d244",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-25T08:30:55.998Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Wev2eEWARPzVtRSRmVdQcQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8809a416-029b-4420-aa46-b67c92e58d2f",
  "isSidechain": true,
  "agentId": "a59633b679c2ca02e",
  "requestId": "req_011CbNyVez8WciePZVMJA8PD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d21a0715-9552-46d6-8f70-264bfcc7bc5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Aqpqb5zJ6b2JDoei6Lh6T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 166,
      "cache_read_input_tokens": 45574,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 166
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 174,
          "cache_read_input_tokens": 45574,
          "cache_creation_input_tokens": 166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 166,
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

_source line 19 · 2026-05-25T08:30:56.015Z_

<details><summary>↩ Tool result · `toolu_01Wev2eEWARPzVtRSRmVdQcQ`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{fig_transfer_heatmap.pdf}
7	\caption{Cross-generator $8{\times}8$ transfer matrix (binary F1, gen-1 vs.\ gen-2+). Mean cross-generator F1\,=\,0.810 [95\% CI: 0.796, 0.822]; uniformly high off-diagonal values confirm depth signal transfers across five families without calibration.}
8	\label{fig:transfer-heatmap}
9	\end{figure}
10	
11	\subsection{Depth Classification Performance}
12	\label{sec:results-classification}
13	
14	\looseness=-1 The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}), with cross-generator F1 spread of 9.1\,pp capturing generator selection uncertainty.
15	This 3-class metric is inflated by shared gen-0 seeds (per-class gen-0 F1\,$\approx$\,0.94; \S\ref{sec:generation}); we therefore report \textbf{leak-free binary F1} (gen-1 vs.\ gen-2+)\,=\,0.694 (CI [0.688, 0.700]) throughout, excluding gen-0 entirely.
16	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B; std.\ dev.\ 0.028), with the primary difficulty at the gen-1\,/\,gen-2+ boundary (Appendix~\ref{app:confusion}).
17	
18	\paragraph{Cross-model generalization.}
19	\looseness=-1 Cross-model chains (randomly selected generator per step) yield binary F1\,=\,0.830 (95\% CI [.818, .841]; Appendix~\ref{app:cross-model-detail}) under 5-generator LOGO.\footnote{Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B; generator-level LOGO with bootstrap CIs ($n$\,=\,1{,}000).}
20	Single-generator transfer confirms the signal is not a mixed-chain artifact (mean transfer F1\,=\,0.810, Figure~\ref{fig:transfer-heatmap}; LOFO\,=\,0.686); analysis of variance (ANOVA) confirms generator identity contributes ${<}1$\% of feature variance ($\eta^2_{\text{gen}} \leq 0.009$; Appendix~\ref{app:cross-model-detail}).
21	A scale effect emerges: smaller models achieve higher F1 (Pythia-2.8B: 0.724 vs.\ Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference (spread $\leq$0.013; \S\ref{sec:results-differential}).
22	An end-to-end QLoRA classifier reaches 3-class F1\,=\,0.905 (within-model 5-fold CV; $+$10.0\,pp; Appendix~\ref{app:qlora}), confirming additional depth signal in token-level representations; on instruct data, QLoRA recovers to 0.89--0.91 (within-model; Appendix~\ref{app:instruct}), establishing the decomposition as DDR's primary contribution.
23	
24	\paragraph{Confound controls.}
25	\looseness=-1 Length-matched subsampling yields binary F1\,=\,0.724 (vs.\ 0.770; Appendix~\ref{app:length}); independent-seed evaluation with disjoint pools (F1\,=\,0.680; Appendix~\ref{app:seed-control}) confirms the classifier captures generative degradation, not seed-specific content.
26	
27	\paragraph{Error analysis.}
28	\looseness=-1 The gen-1\,/\,gen-2+ boundary is the primary failure point: depth-2 samples---the shallowest within the 2+ class---exhibit the highest error rate (48.4\%), decreasing monotonically to 20.3\% at depth-4 (Appendix~\ref{app:error-analysis}), reflecting insufficient accumulated drift beyond the large gen-0$\to$gen-1 distributional shift.
29	Error rates decrease monotonically at deeper generations ($\leq$29.2\% at gen-3+), confirming that DDR signal strengthens with chain length; the DDR decomposition is the primary analytical contribution.
30	
31	\begin{table}[t]
32	\centering
33	\footnotesize
34	\caption{8-generator LOGO macro-F1 (bootstrap 95\% CIs, $n$\,=\,1{,}000). Binary F1 excludes gen-0. $^{\dagger}$3-class F1 has upward bias from shared gen-0 seeds; independent-seed controls confirm the signal (F1\,=\,0.680; Appendix~\ref{app:seed-control}).}
35	\label{tab:logo-results}
36	\resizebox{\columnwidth}{!}{%
37	\begin{tabular}{@{}llcccc@{}}
38	\toprule
39	\textbf{Model} & \textbf{Family} & \textbf{Params} & \textbf{Bin F1} & \textbf{95\% CI} & \textbf{3-class F1}$^{\dagger}$ \\
40	\midrule
41	Pythia-2.8B     & Pythia  & 2.8B & \textbf{0.724} & [.707, .742] & 0.798 \\
42	Pythia-1B       & Pythia  & 1.0B & 0.718 & [.700, .735] & \textbf{0.806} \\
43	Qwen3-1.7B     & Qwen    & 1.7B & 0.709 & [.693, .726] & 0.772 \\
44	Llama-3.2-3B   & Llama   & 3.2B & 0.697 & [.680, .713] & 0.775 \\
45	OLMo-2-1B      & OLMo    & 1.5B & 0.695 & [.679, .711] & 0.781 \\
46	Qwen3-8B       & Qwen    & 8.2B & 0.692 & [.674, .708] & 0.714 \\
47	Qwen3-0.6B     & Qwen    & 0.6B & 0.691 & [.673, .709] & 0.780 \\
48	Mistral-7B     & Mistral & 7.0B & 0.633 & [.617, .648] & 0.682 \\
49	\midrule
50	\multicolumn{3}{l}{\textbf{Average (8-gen LOGO)}} & \textbf{0.694} & [.688, .700] & \textbf{0.762} \\
51	\multicolumn{3}{l}{\textbf{LOFO (family-level)}} & 0.686 & --- & --- \\
52	\bottomrule
53	\end{tabular}}
54	\end{table}
55	
56	\subsection{Differential Depth Response}
57	\label{sec:results-differential}
58	
59	\paragraph{Formal definition.}
60	\looseness=-1 For feature $f$ measured across depths $d \in \{0,1,2{+}\}$, we define its \emph{depth sensitivity} as $\text{DDR}(f) = |\rho(\text{depth}, f)|$, where $\rho$ is Spearman correlation over all per-text measurements.
61	A feature is classified as \emph{drifting} if Cohen's $d > 0.50$ between adjacent depths, or \emph{stationary} if $d < 0.15$; the two-cluster structure is robust across $\varepsilon \in [0.10, 0.75]$ ($k$-means silhouette\,=\,0.660, $p{=}0.030$; exhaustive split enumeration ranks this partition first; independent replication in all eight generators; Appendix~\ref{app:ddr-validation}).
62	\looseness=-1 Recursive inputs grow increasingly self-typical~\citep{markovian_chains}, predicting location drift with shape invariance (confirmed across nucleus, greedy, and top-$k$ strategies; Appendix~\ref{app:decoding-strategy}).
63	
64	\looseness=-1 Figure~\ref{fig:ddr-trajectory} reveals the dichotomy: central-tendency features (entropy mean, TTR, hapax ratio) decline monotonically with depth, while shape features (entropy max, tail decay, entropy min) remain flat (per-feature distributions: Appendix~\ref{app:feature-distributions}; qualitative chain example: Appendix~\ref{app:qualitative}).
65	The partition is binary ($k{=}2$; silhouette\,=\,0.660), with entropy std as the sole \emph{intermediate} member ($d{=}0.46$, $|\rho|{=}0.16$), distinct from three near-stationary features ($d < 0.10$; Appendix~\ref{app:ddr-validation}).
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=\columnwidth]{fig1_differential_response.pdf}
70	\caption{Differential depth response (DDR). Drifting features (red; $|\rho| > 0.60$, effect size $d{=}0.74$--$1.05$) shift monotonically with generation depth; near-stationary features (blue; $d \leq 0.10$) are approximately preserved; entropy std (purple; $d{=}0.46$) is intermediate. Diamonds: cross-generator means; dots: per-generator values.}
71	\label{fig:feature-drift}
72	\end{figure}
73	
74	\looseness=-1 Pooled Spearman correlations corroborate the split: drifting features show $|\rho| > 0.60$ (hapax ratio $-0.64$, TTR $-0.62$, entropy mean $-0.60$) vs.\ $|\rho| \leq 0.16$ for entropy max and tail decay; entropy min reaches $|\rho|{=}0.40$ due to its gen-0/gen-1 boundary sensitivity (discussed below)---a persistent magnitude gap defining the DDR partition (Figure~\ref{fig:feature-drift}).
75	
76	\paragraph{Quantification.}
77	\looseness=-1 Cohen's $d$ shows a ${\geq}8{\times}$ gap between drifting ($d{=}0.74$--$1.05$) and near-stationary ($d < 0.10$); KS, Glass's $\Delta$, Cliff's $\delta$ corroborate (Appendix~\ref{app:ddr-validation}).
78	Entropy min and tail decay are \emph{boundary features}: entropy min is near-stationary for gen-1/gen-2+ ($d{=}0.016$) but sensitive at gen-0/gen-1; tail decay passes two one-sided tests (TOST) equivalence (Appendix~\ref{app:tost}) for only 4/8 generators ($|d|{=}0.10$--$0.22$).
79	\paragraph{Validation.}
80	\looseness=-1 Each hold-out generator independently recovers the identical partition (silhouette 0.505--0.760); TOST confirms near-stationarity for entropy min (8/8) and entropy max (6/8); permutation testing confirms the split as non-random ($p{=}0.030$). Per-feature convergence dynamics (Figure~\ref{fig:convergence}) and per-family DDR consistency appear in Appendices~\ref{app:ddr-validation}--\ref{app:convergence}.
81	
82	\begin{figure}[t]
83	\centering
84	\includegraphics[width=\columnwidth]{fig_convergence_dynamics.pdf}
85	\caption{Feature convergence dynamics. Drifting features (red): $|d| > 1$ by gen-2+; near-stationary features (blue): $|d| < 0.25$ at all depths, confirming shape stability persists across chain lengths.}
86	\label{fig:convergence}
87	\end{figure}
88	
89	\paragraph{Feature complementarity.}
90	\looseness=-1 The full 7-feature set (F1\,=\,0.773, 10-fold stratified cross-validation) outperforms surface-only (0.688) and reference-only (0.713; McNemar $p \approx 0$; Appendix~\ref{app:ablation-table}).
91	Group ablation confirms complementarity: 3-class F1 gains $+$5.3\,pp when non-drifting features are added (drifting-only 0.716, all-7 0.769), while binary detection is already saturated by location drift alone (drifting-only 0.697 vs.\ all-7 0.700)---shape stability contributes to depth \emph{grading}, not detection.
92	TTR and hapax ratio ($r = 0.97$) are retained for marginal LOFO gains (Appendix~\ref{app:lofo}).
93	
94	\paragraph{Cross-family reference models.}
95	\looseness=-1 Alternative references (OLMo-2-1B, Qwen3-0.6B) yield F1 spread of only 0.013 (Appendix~\ref{app:cross-ref}); same-family proximity may inflate Pythia F1 by up to 1.2\,pp, but the DDR partition is preserved.
96	
97	\paragraph{Temperature and prompt-type sensitivity.}
98	\looseness=-1 All four tested generators degrade at $t{=}0.9$ ($-$9.3 to $-$26.0\,pp binary F1; Appendix~\ref{app:sampling-sensitivity}); continuation chains show the strongest drift (F1\,=\,0.781; Appendix~\ref{app:prompt-type}).
99	The DDR partition hierarchy is preserved across temperatures (Appendix~\ref{app:ddr-temp-stability}), including cross-temperature transfer (Appendix~\ref{app:cross-temp}); random word replacement at 10\% degrades binary F1 by only 8\,pp (Appendix~\ref{app:human-edit}).
100	
101	
102	\subsection{Comparison with Detection Baselines}
103	\label{sec:results-baselines}
104	
105	\begin{figure}[t]
106	\centering
107	\includegraphics[width=\columnwidth]{fig3_baseline_comparison.pdf}
108	\caption{LOGO binary F1 vs.\ inference cost (8-gen pooled). The 7-feature ensemble (one 410M model) matches multi-detector ensembles (1.4B total) at ${\sim}2.4\times$ lower cost. RTX 5090 timings.}
109	\label{fig:baseline-ci}
110	\end{figure}
111	
112	\begin{table}[t]
113	\centering
114	\footnotesize
115	\caption{Depth classification (8-gen LOGO, pooled). 7-feature: one 410M model; 4-det ensembles: two models, 1.4B. QLoRA (\S\ref{sec:results-classification}) uses full token sequences (within-model 5-fold CV, not LOGO)---an information-asymmetric ceiling.}
116	\label{tab:baselines}
117	\resizebox{\columnwidth}{!}{%
118	\begin{tabular}{lcccc}
119	\toprule
120	\textbf{Method} & \textbf{Feat.} & \textbf{3-class F1} & \textbf{Bin F1} & \textbf{ms/text} \\
121	\midrule
122	4-det.\ + surface     & 6 & \textbf{0.795} & \textbf{0.708} & 22.8 \\
123	4-detector ens.\      & 4 & 0.785 & 0.700 & 22.8 \\
124	7-feature (ours)      & 7 & 0.774 & 0.705 & \textbf{9.7} \\
125	\midrule
126	Avg-LogProb           & 1 & 0.707 & 0.673 & --- \\
127	FastDetectGPT         & 1 & 0.660 & 0.569 & --- \\
128	LD-Score              & 1 & 0.630 & 0.675 & --- \\
129	Binoculars            & 1 & 0.411 & 0.539 & --- \\
130	\bottomrule
131	\end{tabular}}
132	\end{table}
133	
134	\looseness=-1 We next ask whether existing detection methods---designed for binary real-vs-synthetic classification---incidentally capture depth structure, repurposing four detection scores as ordinal depth predictors under identical XGBoost and LOGO conditions (Table~\ref{tab:baselines}).
135	The strongest baseline is a 4-detector + surface feature ensemble (binary F1\,=\,0.708), which pools four detection scores with TTR and hapax ratio; among individual detectors, Avg-LogProb provides the most meaningful single-feature comparison.
136	
137	\looseness=-1 The 7-feature ensemble matches the 4-detector+surface ensemble on binary F1 (0.705 vs.\ 0.708; Figure~\ref{fig:baseline-ci}) at ${\sim}2.4\times$ lower cost, though the latter leads by 2.1\,pp on 3-class F1 (0.795 vs.\ 0.774); both surpass individual detectors by 3.0--16.6\,pp.
138	The DDR decomposition explains why depth discrimination is achievable---location features carry the signal, shape features enable cross-generator transfer (\S\ref{sec:discussion})---with a single 410M reference model; ordinal-specific methods (CORAL, Frank-Hall) yield comparable F1 (Appendix~\ref{app:classifier}).
139	Among individual detectors, LD-Score and Avg-LogProb best capture depth structure (binary F1\,=\,0.675 and 0.673); FastDetectGPT captures 3-class ordering (F1\,=\,0.660) but struggles with binary depth separation (F1\,=\,0.569); Binoculars is least informative (binary F1\,=\,0.539).
140	Concurrent iterative-generation studies use different chain operators, precluding direct inclusion as depth baselines (Appendix~\ref{app:iterative-comparison}).
141	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d21a0715-9552-46d6-8f70-264bfcc7bc5d",
  "isSidechain": true,
  "promptId": "b1f1579c-3a08-4738-a0d2-62cdbce4d803",
  "agentId": "a59633b679c2ca02e",
  "type": "user",
  "uuid": "a384bc94-e619-46eb-bdc5-d62d4be8108b",
  "sourceToolAssistantUUID": "d21a0715-9552-46d6-8f70-264bfcc7bc5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-25T08:31:31.600Z_

Perfect! Now I have all the main content files. Let me compile the complete report with all numbers, statistics, and metrics found:

## Complete Report: Depth Profiling Paper Contents and Metrics

### FILE 1: main.tex (First 80 lines - Abstract extraction point)
The document is formatted for EMNLP 2026 ARR Submission using ACL 2023 template. It includes sections on introduction, related work, method, results, discussion, conclusion, and limitations, plus multiple appendices.

---

### FILE 2: abstract.tex (FULL FILE)
**Title:** "Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text"

**Key metrics from abstract:**
- **Effect sizes (Cohen's d):**
  - Location features: d = 0.74–1.05 (monotonic drift with depth)
  - Shape features: d < 0.10 (near-stationary)
  - Entropy std: d = 0.46 (intermediate)
  - Effect size gap: ≥8× between location and shape

- **Performance metrics:**
  - Leak-free binary F1 = 0.694 (gen-1 vs. gen-2+)
  - Cross-model binary F1 = 0.830
  - 3-class F1 = 0.762 (under leave-one-generator-out evaluation)

- **Dataset note:** gen-0 seeds shared across generators (controlled)

- **Key finding:** Instruction tuning compresses DDR, limiting applicability to base models

---

### FILE 3: method.tex (FULL FILE)

**Table 1: Seven Distributional Features**
Features extract from NLL distributions under Pythia-410M reference model:

**NLL-based features:**
- entropy_mean (measures central tendency of token surprise)
- entropy_std (spread of token surprise)
- entropy_max (maximum token surprise)
- entropy_min (minimum token surprise)
- tail_decay (log-prob decay slope, ranks 100–1000)

**Surface features:**
- ttr (type-token ratio)
- hapax_ratio (proportion of hapax legomena)

**Generation setup:**
- **Number of generators:** 8 total
- **Model families:** 5 (Pythia, OLMo, Qwen, Llama, Mistral)
- **Generator specifications:**
  - Pythia: 2.8B, 1B
  - OLMo: OLMo-2-1B
  - Qwen: Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base
  - Llama: Llama-3.2-3B
  - Mistral: Mistral-7B-v0.3
- **Parameter range:** 13× (0.6B–8B)
- **Qwen overrepresentation:** 3/8 generators
- **LOFO performance:** F1 = 0.686 (with Qwen overrepresentation acknowledged)

**Dataset construction:**
- **Seed passages:** approximately 1,000 from English Wikipedia per generator
- **Chain depth:** depth 4 (gen-0 through gen-4)
- **Prompt:** "Continue the following text: {text}"
- **Sampling parameters:**
  - Temperature τ = 0.7
  - Nucleus sampling p = 0.9
  - Maximum length: 256 new tokens
- **5-class analysis result:** F1 ≈ 0.27 (adjacent depths 2–4 indistinguishable, motivating gen-2+ collapse)
- **Final dataset size:** 37,058 texts across all depths
- **Depths 2–4:** Collapsed into 2+ class

**Feature extraction details:**
- Reference model: Pythia-410M (smaller than all generators)
- **Feature redundancy screening:** 6 additional NLL statistics rejected (|r| > 0.65, ΔF1 ≤ −0.011)
- **Cross-family reference validation:** F1 spread = 0.013 (Pythia, OLMo, Qwen references)
- **Feature correlation:** TTR and hapax ratio correlation r = 0.97 (strongly correlated, retained for marginal LOFO gains)

**Evaluation protocol:**
- **Primary metric:** Macro-averaged F1 over three depth classes
- **Confidence intervals:** 95% bootstrap (n = 1,000)
- **Bonferroni correction:** Applied within each family of simultaneous tests
- **Classifier:** XGBoost
  - n_estimators = 200
  - max_depth = 6
  - learning rate = 0.1
  - Hyperparameter sensitivity: F1 variation ≤ 2.0 pp

**Baselines compared:**
1. Avg-LogProb
2. FastDetectGPT
3. Binoculars
4. LD-Score

---

### FILE 4: results.tex (FULL FILE)

**Figure: Cross-generator 8×8 transfer matrix (binary F1, gen-1 vs. gen-2+)**
- **Mean cross-generator F1:** 0.810
- **95% CI:** [0.796, 0.822]
- Uniform high off-diagonal values confirm depth signal transfers across five families

**Classification Performance (Section 3-class LOGO):**
- **8-generator LOGO F1:** 0.762
- **95% CI:** [0.758, 0.766]
- **Dataset size N:** 37,058
- **Cross-generator F1 spread:** 9.1 pp
- **Per-class gen-0 F1:** ≈0.94 (shared gen-0 seeds bias)
- **Leak-free binary F1** (gen-1 vs. gen-2+, excluding gen-0): 0.694
- **Binary F1 CI:** [0.688, 0.700]

**Per-generator binary F1 results:**
- Pythia-2.8B: 0.724 [.707, .742] – highest; 3-class: 0.798
- Pythia-1B: 0.718 [.700, .735]; 3-class: 0.806 (best 3-class)
- Qwen3-1.7B: 0.709 [.693, .726]; 3-class: 0.772
- Llama-3.2-3B: 0.697 [.680, .713]; 3-class: 0.775
- OLMo-2-1B: 0.695 [.679, .711]; 3-class: 0.781
- Qwen3-8B: 0.692 [.674, .708]; 3-class: 0.714
- Qwen3-0.6B: 0.691 [.673, .709]; 3-class: 0.780
- Mistral-7B: 0.633 [.617, .648] – lowest; 3-class: 0.682
- **Per-generator std. dev.:** 0.028
- **Primary difficulty:** gen-1/gen-2+ boundary

**Cross-model generalization:**
- **Cross-model chains binary F1:** 0.830
- **95% CI:** [.818, .841]
- **LOGO setup:** 5-generator (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B)
- **Single-generator transfer mean F1:** 0.810 (Figure 1)
- **LOFO (family-level):** F1 = 0.686
- **ANOVA generator variance:** η²_gen ≤ 0.009 (<1% of feature variance)
- **Model size effect:**
  - Pythia-2.8B: 0.724 (smaller models perform better)
  - Mistral-7B: 0.633 (larger model lower)
  - Same-family affinity with Pythia-410M reference spread ≤ 0.013

**End-to-end neural classifier (QLoRA):**
- **3-class F1:** 0.905
- **Improvement:** +10.0 pp over distributional features
- **Setup:** Within-model 5-fold CV
- **On instruct data:** QLoRA recovers to 0.89–0.91 (within-model)

**Confound controls:**
- **Length-matched subsampling binary F1:** 0.724 (vs. 0.770 without matching)
- **Independent-seed evaluation (disjoint pools):** F1 = 0.680

**Error analysis:**
- **Depth-2 error rate (highest):** 48.4%
- **Depth-4 error rate:** 20.3% (monotonic decrease)
- **Depth-3+ error rates:** ≤29.2%
- **Primary failure:** gen-1/gen-2+ boundary

**Differential Depth Response (DDR) Definition:**
- **Depth sensitivity:** DDR(f) = |ρ(depth, f)| using Spearman correlation
- **Drifting threshold:** Cohen's d > 0.50 between adjacent depths
- **Stationary threshold:** d < 0.15
- **k-means silhouette score:** 0.660
- **Silhouette p-value:** 0.030
- **Robustness range:** ε ∈ [0.10, 0.75]

**Feature drift patterns:**
- **Drifting features (Spearman |ρ|):**
  - hapax_ratio: ρ = -0.64
  - TTR: ρ = -0.62
  - entropy_mean: ρ = -0.60
- **Near-stationary features:**
  - entropy_max: |ρ| ≤ 0.16
  - tail_decay: |ρ| ≤ 0.16
  - entropy_min: |ρ| = 0.40 (boundary feature, sensitive at gen-0/gen-1)
- **Magnitude gap:** ≥8×

**Cohen's d effect sizes:**
- **Drifting features:** d = 0.74–1.05
- **Near-stationary features:** d < 0.10
- **Gap factor:** ≥8×
- **Entropy std:** d = 0.46 (intermediate)

**Boundary feature analysis:**
- **Entropy min:** d = 0.016 (near-stationary for gen-1/gen-2+)
- **Tail decay TOST equivalence:** 4/8 generators (|d| = 0.10–0.22)

**Validation statistics:**
- **Per-generator hold-out silhouette:** 0.505–0.760
- **TOST entropy min:** 8/8 generators confirmed near-stationary
- **TOST entropy max:** 6/8 generators confirmed
- **Permutation testing p-value:** 0.030 (partition non-random)

**Feature complementarity ablations:**
- **Full 7-feature set (10-fold stratified CV):** F1 = 0.773
- **Surface-only:** F1 = 0.688
- **Reference-only:** F1 = 0.713
- **McNemar p-value:** ≈ 0
- **3-class F1 gains from non-drifting features:** +5.3 pp
  - Drifting-only: F1 = 0.716
  - All-7: F1 = 0.769
- **Binary detection (drifting-only):** F1 = 0.697
- **Binary detection (all-7):** F1 = 0.700 (already saturated)

**Cross-family reference models:**
- **Alternative references F1 spread:** 0.013 (OLMo-2-1B, Qwen3-0.6B)
- **Same-family Pythia F1 inflation:** Up to 1.2 pp

**Temperature and prompt sensitivity:**
- **Temperature t = 0.9 degradation:** −9.3 to −26.0 pp binary F1
- **Continuation chains F1:** 0.781 (strongest drift)
- **Random word replacement (10%) degradation:** −8 pp binary F1

**Baseline comparison (8-gen LOGO, pooled):**
- **4-detector + surface (6 features):**
  - 3-class F1: 0.795
  - Binary F1: 0.708
  - Inference: 22.8 ms/text
- **4-detector ensemble (4 features):**
  - 3-class F1: 0.785
  - Binary F1: 0.700
  - Inference: 22.8 ms/text
- **7-feature ensemble (ours):**
  - 3-class F1: 0.774
  - Binary F1: 0.705
  - Inference: 9.7 ms/text (2.4× faster)
  - One 410M model vs. 1.4B total for ensembles

**Individual detector performance:**
- **Avg-LogProb:** 3-class F1 = 0.707, binary F1 = 0.673
- **FastDetectGPT:** 3-class F1 = 0.660, binary F1 = 0.569
- **LD-Score:** 3-class F1 = 0.630, binary F1 = 0.675
- **Binoculars:** 3-class F1 = 0.411, binary F1 = 0.539

**Performance differences:**
- 4-detector+surface vs. 7-feature: 0.708 vs. 0.705 binary F1 (3 pp difference)
- 4-detector+surface vs. 7-feature: 0.795 vs. 0.774 3-class F1 (2.1 pp difference)
- Individual vs. ensemble: 3.0–16.6 pp improvement

---

## Summary of All Key Statistics:

**Dataset:** 37,058 texts, 8 generators, 5 families, 0.6B–8B parameter range

**Primary metrics:**
- Binary F1 = 0.694 [0.688, 0.700] (leak-free, main result)
- 3-class F1 = 0.762 [0.758, 0.766]
- Cross-model binary F1 = 0.830 [0.818, 0.841]

**Effect sizes:** ≥8× gap between drifting (d=0.74–1.05) and stationary (d<0.10) features

**Reference model:** Pythia-410M

**Classifier:** XGBoost (n_estimators=200, max_depth=6, lr=0.1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a384bc94-e619-46eb-bdc5-d62d4be8108b",
  "isSidechain": true,
  "agentId": "a59633b679c2ca02e",
  "requestId": "req_011CbNyVoQtRUbe2vpTxF6gM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1289cd9b-e4f9-4cfa-8cd9-437465022da1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CLrrnnnALNAXfZ5CHeN87t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5774,
      "cache_read_input_tokens": 45740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5774,
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
