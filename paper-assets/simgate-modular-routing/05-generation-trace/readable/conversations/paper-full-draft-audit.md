# paper full draft audit

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 0
- **Tool calls:** 29
- **Original source:** `logs/chats/worker_paper_full-draft-audit_20260514T144747.jsonl`
- **Structured JSON:** [`caa3eaf56c0b1762bed0.json`](../../sessions/ca/caa3eaf56c0b1762bed0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

59 recorded events

### Tool call

_source line 1 · 2026-05-14T14:54:32.668190+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/",
  "description": "List latex files in artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/",
    "description": "List latex files in artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T14:54:32.668586+00:00_

total 408
drwxr-xr-x 2 ubuntu ubuntu   4096 May 14 14:45 .
drwxr-xr-x 3 ubuntu ubuntu   4096 May 14 14:45 ..
-rw-r--r-- 1 ubuntu ubuntu    935 May 14 13:02 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu  11615 May 14 14:44 acl.sty
-rw-r--r-- 1 ubuntu ubuntu  45186 May 14 14:44 acl_natbib.bst
-rw-r--r-- 1 ubuntu ubuntu    688 May 14 14:42 conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu   1669 May 14 14:38 discussion.tex
-rw-r--r-- 1 ubuntu ubuntu   5381 May 14 14:42 experiments.tex
-rw-r--r-- 1 ubuntu ubuntu  31407 May 14 14:44 fig1_daf_scatter.pdf
-rw-r--r-- 1 ubuntu ubuntu   3001 May 14 14:42 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu  11468 May 14 14:45 main.aux
-rw-r--r-- 1 ubuntu ubuntu   3918 May 14 14:45 main.bbl
-rw-r--r-- 1 ubuntu ubuntu   1281 May 14 14:45 main.blg
-rw-r--r-- 1 ubuntu ubuntu  26198 May 14 14:45 main.log
-rw-r--r-- 1 ubuntu ubuntu   1734 May 14 14:45 main.out
-rw-r--r-- 1 ubuntu ubuntu 211813 May 14 14:45 main.pdf
-rw-r--r-- 1 ubuntu ubuntu   2425 May 14 14:38 main.tex
-rw-r--r-- 1 ubuntu ubuntu   6144 May 14 13:01 main.tex.part1
-rw-r--r-- 1 ubuntu ubuntu   2843 May 14 14:42 method.tex
-rw-r--r-- 1 ubuntu ubuntu   3755 May 14 12:20 references.bib
-rw-r--r-- 1 ubuntu ubuntu   2008 May 14 13:30 related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T14:54:32.668798+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/",
  "description": "List latex files in docs directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/",
    "description": "List latex files in docs directory"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T14:54:32.668966+00:00_

total 416
drwxr-xr-x 4 ubuntu ubuntu   4096 May 14 14:42 .
drwxr-xr-x 4 ubuntu ubuntu   4096 May 13 05:45 ..
-rw-r--r-- 1 ubuntu ubuntu    715 May 14 11:28 SETUP_NOTES.md
drwxr-xr-x 2 ubuntu ubuntu   4096 May 14 12:20 _pdf_images
-rw-r--r-- 1 ubuntu ubuntu   1427 May 14 14:42 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu  11615 May 14 11:41 acl.sty
-rw-r--r-- 1 ubuntu ubuntu  45186 May 14 11:41 acl_natbib.bst
-rw-r--r-- 1 ubuntu ubuntu   1942 May 14 14:42 conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu   7822 May 14 14:42 experiments.tex
drwxr-xr-x 2 ubuntu ubuntu   4096 May 14 11:47 figures
-rw-r--r-- 1 ubuntu ubuntu   2913 May 14 14:42 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu  11243 May 14 12:24 main.aux
-rw-r--r-- 1 ubuntu ubuntu   4032 May 14 12:23 main.bbl
-rw-r--r-- 1 ubuntu ubuntu   1281 May 14 12:23 main.blg
-rw-r--r-- 1 ubuntu ubuntu  16485 May 14 12:12 main.fdb_latexmk
-rw-r--r-- 1 ubuntu ubuntu  17608 May 14 12:12 main.fls
-rw-r--r-- 1 ubuntu ubuntu  24819 May 14 12:24 main.log
-rw-r--r-- 1 ubuntu ubuntu   1713 May 14 12:24 main.out
-rw-r--r-- 1 ubuntu ubuntu 211754 May 14 12:24 main.pdf
-rw-r--r-- 1 ubuntu ubuntu    521 May 14 12:12 main.tex
-rw-r--r-- 1 ubuntu ubuntu   3903 May 14 14:42 method.tex
-rw-r--r-- 1 ubuntu ubuntu   3588 May 14 12:06 references.bib
-rw-r--r-- 1 ubuntu ubuntu   1659 May 14 11:44 related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T14:54:32.669199+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T14:54:32.669357+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T14:54:32.669537+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T14:54:32.669721+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	
10	\title{Death Avoidance Accounts for 90\% of the Routing Signal in LLM Agent Tool Use}
11	
12	\author{Anonymous ACL submission}
13	
14	\begin{document}
15	\maketitle
16	\input{abstract}
17	\input{introduction}
18	\input{method}
19	\input{experiments}
20	\input{related_work}
21	\input{discussion}
22	\input{conclusion}
23	
24	\section*{Limitations}
25	
26	Our analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. The $-100$ death penalty may amplify DAF; environments with less catastrophic penalties could exhibit lower DAF, though the qualitative finding may still hold. Step-level labeling with denser rewards is a natural extension. The logit--generation gap in the implicit router warrants further investigation.
27	
28	\paragraph{Labeling quality.}
29	A potential concern is oracle circularity: whether episode-level labels reflect tie-breaking artifacts rather than genuine modality differences. We audit all 245 labels. Of the 150 \texttt{no\_preference} labels (61.2\%), 115 (46.9\%) are both-alive ties and 35 (14.3\%) are both-dead---all excluded from router training. The remaining 95 training labels are entirely genuine: 75 from death asymmetry (70 deterministic-preferred, 5 internal-preferred) and 20 from score comparison with both strategies surviving (16 deterministic-preferred, 4 internal-preferred). Zero labels depend on tie-breaking. Retraining the router using only death-asymmetry labels yields balanced accuracy of 57.3\%, within 1$\sigma$ of the full-label retrain (57.6 $\pm$ 0.5\%), confirming that score-comparison labels contribute negligible additional signal. The 97.4\% step-level tie rate (\S\ref{sec:collection}) furth
…[truncated 530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T14:54:32.669890+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T14:54:32.670093+00:00_

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
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	
14	\title{Death Avoidance Dominates Routing Signal\\in LLM Agent Computation}
15	
16	\author{Anonymous}
17	
18	\begin{document}
19	\maketitle
20	
21	\input{abstract}
22	\input{introduction}
23	\input{method}
24	\input{experiments}
25	\input{related_work}
26	\input{conclusion}
27	
28	\bibliography{references}
29	
30	\end{document}
31	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T14:54:32.670272+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "simgate-modular-routing",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "simgate-modular-routing",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T14:54:32.670902+00:00_

Error: result (104,898 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/51870e0b-e7be-4f0d-82f1-db4a37356f5f/tool-results/mcp-agent-ml-research-read_registry-1778770085071.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/51870e0b-e7be-4f0d-82f1-db4a37356f5f/tool-results/mcp-agent-ml-research-read_registry-1778770085071.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T14:54:32.671173+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T14:54:32.671336+00:00_

1	\begin{abstract}
2	Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 97.4\% of steps yield tied outcomes, rendering step-level analysis uninformative. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to derive per-episode routing labels. Across 245 episodes with a Qwen2.5-7B-Instruct backbone, death avoidance accounts for approximately 90\% of the routing signal (Death Avoidance Factor), with near-perfect cross-task correlation ($r = 0.97$). These results indicate that deterministic computation's value is concentrated in catastrophic failure prevention rather than positive task guidance.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T14:54:32.671485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T14:54:32.671658+00:00_

1	\section{Introduction}
2	
3	When a Qwen2.5-7B-Instruct agent attempts to boil water in ScienceWorld \cite{scienceworld-2022}, it must track temperature thresholds, container states, and heat source interactions across dozens of steps. Internal LLM reasoning hallucinates these state transitions---predicting water has boiled when the stove was never activated---triggering agent death with a $-100$ penalty. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations by executing exact state transitions. The natural question: when should an agent route computation externally versus reasoning internally?
4	
5	Existing routing approaches \cite{toolformer-2024,art-2023,chameleon-2024} frame tool selection as a capability or efficiency decision---matching subtasks to tools that can solve them. This framing ignores a potentially dominant signal: routing to \emph{avoid catastrophic failure}. Understanding what routing actually learns requires counterfactual analysis, but the standard per-step oracle approach degenerates under sparse rewards. On ScienceWorld, where non-zero reward arrives only at episode termination, 97.4\% of steps produce tied intermediate scores under both strategies across 245 episodes---no step-level signal exists to train a router (\S\ref{sec:collection}).
6	
7	We propose \emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct~\cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\S\ref{sec:collection}). Across 11 ScienceWorld task types (245 episodes), the full deterministic advantage is $\Delta_{\text{full}} = +29.60$ points. Excluding death episodes, this gap collapses to $\Delta_{\text{nd}} = +2.84$---a Death Avoidance Factor (DAF; \S\ref{sec:daf}) of 90.41\%. The per-task correlation between death rate differential and performance gap is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$), confirming death avoidan
…[truncated 1034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T14:54:32.671831+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T14:54:32.672016+00:00_

1	\section{Method}
2	
3	\subsection{Counterfactual Episode Collection}
4	\label{sec:collection}
5	
6	Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each modality. Under sparse terminal rewards, this degenerates: on ScienceWorld \cite{scienceworld-2022}, 97.4\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.
7	
8	For each task instance, we execute two complete episodes under identical initial conditions. The \emph{pure-internal} episode follows the ReAct paradigm \cite{react-2023}, where the LLM interleaves chain-of-thought reasoning with environment actions. The \emph{pure-deterministic} episode uses the environment simulator to compute exact state transitions. In both cases the LLM selects which action to take; deterministic computation replaces only the state-transition prediction---equivalent to giving the agent a perfect world model.
9	
10	Each episode pair produces a tuple $(s^{\text{int}}, s^{\text{det}}, d^{\text{int}}, d^{\text{det}})$, where $s$ denotes the terminal score and $d \in \{0,1\}$ indicates agent death. Episodes are capped at 30 steps. The LLM backbone is Qwen2.5-7B-Instruct served via vLLM. ScienceWorld spans 30 task types with a $-100$ death penalty; after prescreening, we collect 245 episode pairs across 11 task types (20--40 per type).
11	
12	\subsection{Death-Aware Labeling}
13	\label{sec:labeling}
14	
15	Each counterfactual pair receives an episode-level routing label based on $(s^{\text{int}}, s^{\text{det}}, d^{\text{int}}, d^{\text{det}})$. Scores are integer-valued, so we use exact (in)equality. The label is assigned by four mutually exclusive cases:
16	
17	\begin{enumerate}
18	    \item \textbf{Death asymmetry}: $d^{\text{int}} \neq d^{\text{det}}$ $\rightarrow$ surviving strategy preferred.
19	    \item \textbf{Both dead}: $d^{\text{int}} = d^{\text{det}} = 1$ $\rightarrow$ \texttt{no\_p
…[truncated 930 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T14:54:32.672197+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T14:54:32.672382+00:00_

1	\section{Experiments}
2	
3	\subsection{Setup}
4	\label{sec:exp-setup}
5	
6	We evaluate on ScienceWorld \cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ death penalty. Using the methodology in \S\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 per type). The LLM backbone is Qwen2.5-7B-Instruct served via vLLM with episodes capped at 30 steps.
7	
8	\subsection{Death Avoidance Decomposition}
9	\label{sec:death-decomp}
10	
11	\begin{figure}[t]
12	\centering
13	\includegraphics[width=\columnwidth]{fig1_daf_scatter.pdf}
14	\caption{Per-task death rate differential (internal minus deterministic) vs.\ $\Delta_{\text{full}}$. Each point represents one of 11 task types. Regression: $r = 0.9698$ ($p = 8.12 \times 10^{-7}$).}
15	\label{fig:decomposition}
16	\end{figure}
17	
18	The full performance gap between deterministic and internal strategies across 245 episodes is $\Delta_{\text{full}} = +29.60$ points. Excluding all episodes where either strategy results in death, the gap collapses to $\Delta_{\text{nd}} = +2.84$. The resulting DAF (\S\ref{sec:daf}) is 90.41\%: approximately 90\% of the deterministic strategy's advantage is attributable to death avoidance.
19	
20	This concentration is consistent across task types. The Pearson correlation between per-task death rate differential and $\Delta_{\text{full}}$ is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$; Figure~\ref{fig:decomposition}). The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic---a 2.6$\times$ ratio driving the bulk of the score difference.
21	
22	The label distribution reflects this asymmetry: 86 \texttt{det\_preferred}, 9 \texttt{internal\_preferred}, 150 \texttt{no\_preference}. When internal reasoning does not cause death, it performs comparably to deterministic computation.
23	
24	One task reveals residual non-death signal: \texttt{find-non-living-thing} ($n=40$) has ze
…[truncated 3564 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T14:54:32.672544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T14:54:32.672717+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool-Use Learning.}
4	Toolformer \cite{toolformer-2024} inserts API calls via self-supervised filtering;
5	ART \cite{art-2023} delegates tool selection to LLM reasoning chains;
6	Chameleon \cite{chameleon-2024} composes modules under LLM-as-planner orchestration;
7	ReTool \cite{retool-2026} applies RL for implicit code-interpreter invocation.
8	These methods learn \emph{which tool} to use but do not analyze what signal drives routing.
9	We generate labels via \emph{episode-level counterfactual analysis} and diagnose what the signal encodes---revealing ${\sim}90\%$ is death avoidance.
10	
11	\paragraph{Adaptive Computation.}
12	CogRouter \cite{cogrouter-2026} achieves 82.3\% on ScienceWorld (success rate, different evaluation protocol) via cognitive depth routing.
13	ARES \cite{ares-2026} reduces token cost by 52.7\% with per-step reasoning effort selection.
14	Mixture-of-Recursions \cite{mixture-of-recursions-2025} applies adaptive depth via per-token recursive routing.
15	These route \emph{how much} to reason; we route \emph{which modality}. None quantify routing signal composition.
16	
17	\paragraph{World Model Routing.}
18	ITP \cite{itp-2026} augments agents with LLM-based world model lookahead;
19	Dyna-Think \cite{dynathink-2025} integrates world model simulation into reasoning, matching 685B performance with 32B at half the token cost.
20	Both route to \emph{approximate} world models inheriting LLM hallucinations.
21	Our deterministic modality provides \emph{exact} state transitions; counterfactual analysis shows this exactness matters almost exclusively for death avoidance.
22	
23	\paragraph{Agent Frameworks.}
24	ReAct \cite{react-2023} interleaves reasoning and acting and serves as our internal-reasoning baseline.
25	MTRouter \cite{mtrouter-2026} routes between LLMs for cost optimization on ScienceWorld.
26	Our work asks what a learned router captures---the answer is dominated by catastrophic-failure prevention, sugges
…[truncated 80 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T14:54:32.672884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T14:54:32.673057+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Cross-environment evidence.}
5	The death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? A preliminary 50-problem pilot on MATH Level~4--5, using code interpreter as the deterministic modality, suggests not. Internal reasoning achieved 80\% accuracy versus 72\% for code interpreter, with 88\% of problems showing no modality preference (label distribution: 1 deterministic-preferred, 5 internal-preferred, 44 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld. A larger-scale replication with improved code execution (addressing sandbox limitations in the pilot) is in progress.
6	
7	% TODO: Replace pilot-50 numbers with math-200-fixed results when available
8	
9	\paragraph{Scope and future directions.}
10	Our analysis is grounded in a single interactive environment with a specific failure mode (the $-100$ death penalty). Extending the counterfactual methodology to environments with graded failure costs, embodied agents with continuous action spaces, or multi-turn dialogue systems would clarify how broadly death avoidance---or analogous catastrophic-failure avoidance---accounts for apparent routing signal. Step-level counterfactual labeling, rather than episode-level, is a complementary direction that could reveal finer-grained routing structure masked by our current aggregation.
11	
12	% TODO: ALFWorld results pending; add cross-environment comparison if signal emerges
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T14:54:32.673220+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T14:54:32.673362+00:00_

1	\section{Conclusion}
2	
3	We presented episode-level counterfactual analysis for diagnosing routing behavior in modular LLM agents. Applied to 245 episodes across 11 ScienceWorld task types, death avoidance accounts for 90.41\% of the routing signal ($\Delta_{\text{full}}$ = +29.60 vs.\ $\Delta_{\text{nd}}$ = +2.84), corroborated by near-perfect cross-task correlation ($r$ = 0.9698), oracle degeneracy (96.3\% agreement with always-deterministic), and near-random trained-router accuracy (58.1\%). Preliminary cross-environment evidence (\S\ref{sec:discussion}) suggests this finding reflects a structural property of catastrophic-failure environments rather than a ScienceWorld artifact.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T14:54:32.673507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T14:54:32.673686+00:00_

1	@inproceedings{scienceworld-2022,
2	  title={ScienceWorld: Is Your Agent Smarter Than a 5th Grader?},
3	  author={Wang, Ruoyao and Jansen, Peter and C{\^o}t{\'e}, Marc-Alexandre and Ammanabrolu, Prithviraj},
4	  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
5	  year={2022}
6	}
7	
8	@inproceedings{toolformer-2024,
9	  title={Toolformer: Language Models Can Teach Themselves to Use Tools},
10	  author={Schick, Timo and Dwivedi-Yu, Jane and Dess{\`i}, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},
11	  booktitle={Advances in Neural Information Processing Systems},
12	  year={2023}
13	}
14	
15	@inproceedings{art-2023,
16	  title={{ART}: Automatic Multi-step Reasoning and Tool-use for Large Language Models},
17	  author={Paranjape, Bhargavi and Lundberg, Scott and Singh, Sameer and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Ribeiro, Marco Tulio},
18	  booktitle={arXiv preprint arXiv:2303.09014},
19	  year={2023}
20	}
21	
22	@inproceedings{chameleon-2024,
23	  title={Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models},
24	  author={Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei and Wu, Ying Nian and Zhu, Song-Chun and Gao, Jianfeng},
25	  booktitle={Advances in Neural Information Processing Systems},
26	  year={2023}
27	}
28	
29	@inproceedings{retool-2026,
30	  title={{ReTool}: Reinforcement Learning for Strategic Tool Use in {LLM}s},
31	  author={Feng, Yutong and Qian, Shengjie and Luo, Boyu and Shi, Yibo and Yang, Ke and Ma, Liang and Zheng, Ling},
32	  booktitle={arXiv preprint arXiv:2504.11536},
33	  year={2025}
34	}
35	
36	@inproceedings{react-2023,
37	  title={{ReAct}: Synergizing Reasoning and Acting in Language Models},
38	  author={Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
39	  booktitle={Internati
…[truncated 2019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T14:54:32.673851+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/51870e0b-e7be-4f0d-82f1-db4a37356f5f/tool-results/mcp-agent-ml-research-read_registry-1778770085071.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nfor exp in result:\n    eid = exp.get('id','')\n    # Filter to relevant experiments\n    if any(k in eid for k in ['plan-003','plan-004','plan-012','plan-013','math-pilot','tie-rate']):\n        print(f\\\"=== {eid} ===\\\")\n        print(f\\\"  status: {exp.get('status')}\\\")\n        print(f\\\"  conclusion: {exp.get('conclusion','')[:500]}\\\")\n        m = exp.get('metrics',{})\n        if m: print(f\\\"  metrics: {json.dumps(m, indent=2)[:800]}\\\")\n        n = exp.get('notes','')\n        if n: print(f\\\"  notes: {str(n)[:800]}\\\")\n        print()\n\" 2>&1 | head -300",
  "description": "Extract relevant experiment data from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/51870e0b-e7be-4f0d-82f1-db4a37356f5f/tool-results/mcp-agent-ml-research-read_registry-1778770085071.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nfor exp in result:\n    eid = exp.get('id','')\n    # Filter to relevant experiments\n    if any(k in eid for k in ['plan-003','plan-004','plan-012','plan-013','math-pilot','tie-rate']):\n        print(f\\\"=== {eid} ===\\\")\n        print(f\\\"  status: {exp.get('status')}\\\")\n        print(f\\\"  conclusion: {exp.get('conclusion','')[:500]}\\\")\n        m = exp.get('metrics',{})\n        if m: print(f\\\"  metrics: {json.dumps(m, indent=2)[:800]}\\\")\n        n = exp.get('notes','')\n        if n: print(f\\\"  notes: {str(n)[:800]}\\\")\n        print()\n\" 2>&1 | head -300",
    "description": "Extract relevant experiment data from registry"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T14:54:32.674052+00:00_

Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
    eid = exp.get('id','')
          ^^^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T14:54:32.674256+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -200 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/51870e0b-e7be-4f0d-82f1-db4a37356f5f/tool-results/mcp-agent-ml-research-read_registry-1778770085071.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\ndata = json.loads(raw)\nresult_str = data['result']\n# Check type\nprint(type(result_str))\nprint(result_str[:500])\n\"",
  "description": "Inspect registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Bash",
  "tool_args": {
    "command": "head -200 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/51870e0b-e7be-4f0d-82f1-db4a37356f5f/tool-results/mcp-agent-ml-research-read_registry-1778770085071.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\ndata = json.loads(raw)\nresult_str = data['result']\n# Check type\nprint(type(result_str))\nprint(result_str[:500])\n\"",
    "description": "Inspect registry data structure"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T14:54:32.674418+00:00_

&lt;class 'str'>
{"success": true, "data": {"experiments": {"math-200-fixed": {"status": "DONE", "retry_count": 0, "created_at": "2026-05-14T14:27:17.496Z", "updated_at": "2026-05-14T14:47:45.881Z", "spec": {"hypothesis": "MATH 200 题（Level 4-5，offset=50 跳过 pilot）counterfactual 收集，使用修复后的 code_sandbox.py（auto_print_last_expr 修复裸表达式 output 为空 bug）", "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python src/math_counterfactual.py --n_problems 200 --offset

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T14:54:32.674584+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/51870e0b-e7be-4f0d-82f1-db4a37356f5f/tool-results/mcp-agent-ml-research-read_registry-1778770085071.txt') as f:\n    data = json.loads(f.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\ntargets = ['plan-003','plan-004','plan-012','plan-013','math-pilot','tie-rate']\nfor eid, exp in exps.items():\n    if any(k in eid for k in targets):\n        print(f'=== {eid} ===')\n        print(f'  status: {exp.get(\\\"status\\\")}')\n        c = exp.get('conclusion','')\n        if c: print(f'  conclusion: {str(c)[:600]}')\n        m = exp.get('metrics',{})\n        if m: print(f'  metrics: {json.dumps(m, indent=2)[:600]}')\n        n = exp.get('notes','')\n        if n: print(f'  notes: {str(n)[:600]}')\n        print()\n\" 2>&1",
  "description": "Extract relevant experiment data from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/51870e0b-e7be-4f0d-82f1-db4a37356f5f/tool-results/mcp-agent-ml-research-read_registry-1778770085071.txt') as f:\n    data = json.loads(f.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\ntargets = ['plan-003','plan-004','plan-012','plan-013','math-pilot','tie-rate']\nfor eid, exp in exps.items():\n    if any(k in eid for k in targets):\n        print(f'=== {eid} ===')\n        print(f'  status: {exp.get(\\\"status\\\")}')\n        c = exp.get('conclusion','')\n        if c: print(f'  conclusion: {str(c)[:600]}')\n        m = exp.get('metrics',{})\n        if m: print(f'  metrics: {json.dumps(m, indent=2)[:600]}')\n        n = exp.get('notes','')\n        if n: print(f'  notes: {str(n)[:600]}')\n        print()\n\" 2>&1",
    "description": "Extract relevant experiment data from registry"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T14:54:32.674906+00:00_

=== math-pilot-50 ===
  status: DONE
  conclusion: success
  metrics: {
  "n_problems": 50,
  "code_execution_rate": 0.82,
  "code_exec_count": 41,
  "no_code_count": 9,
  "internal_accuracy": 0.8,
  "codeinterp_accuracy": 0.72,
  "labels": {
    "det_preferred": 1,
    "internal_preferred": 5,
    "no_preference": 44
  },
  "filtered_labels": {
    "det_preferred": 1,
    "internal_preferred": 5,
    "no_preference": 44
  },
  "code_rounds_dist": {
    "0_rounds": 9,
    "1_round": 36,
    "2_rounds": 5
  },
  "avg_time_per_problem_s": 12,
  "total_time_s": 599,
  "gate": "PASS",
  "critical_finding": "Internal reasoning (80%) outperforms code interpreter (72%)
  notes: ⚠️ Sandbox bug: 34.1% (14/41) code executions have empty output due to bare expressions without print(). Clean CodeInterp accuracy (Category A, output non-empty) is 88.9%, not the reported 72%. Category B (output empty) accuracy drops to 28.6%. Fix in progress: ast auto-wrap bare expressions. 200-problem run (unauthorized, dirty data) killed.

=== plan-012-penalty-sensitivity ===
  status: DONE
  conclusion: success
  metrics: {
  "N": 245,
  "n_only_int_dies": 70,
  "n_only_det_dies": 5,
  "n_both_die": 35,
  "n_neither_die": 135,
  "delta": 0.2653,
  "delta_nd": 3.07,
  "delta_full_100": 29.6,
  "DAF_P10": 46.4,
  "DAF_P25": 68.4,
  "DAF_P50": 81.2,
  "DAF_P100": 89.6,
  "DAF_P200": 94.5
}

=== plan-003-bootstrap-95ci ===
  status: DONE
  conclusion: success
  metrics: {
  "always-internal": {
    "mean": -39.07,
    "ci95": [
      -46.4,
      -32.27
    ]
  },
  "always-deterministic": {
    "mean": -9.47,
    "ci95": [
      -14.71,
      -4.29
    ]
  },
  "oracle": {
    "mean": -6.58,
    "ci95": [
      -11.54,
      -1.7
    ]
  },
  "random": {
    "mean": -22.38,
    "ci95": [
      -28.67,
      -15.75
    ]
  },
  "trained-router": {
    "mean": -10.7,
    "ci95": [
      -16.33,
      -5.27
    ]
  }
}

=== plan-013-labeling-quality ===
  status: DONE
  conclusion: success
  metrics:
…[truncated 13485 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T14:54:32.675250+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "for f in abstract.tex conclusion.tex experiments.tex introduction.tex method.tex; do\n  a=\"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/$f\"\n  b=\"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/$f\"\n  if [ -f \"$a\" ] && [ -f \"$b\" ]; then\n    echo \"=== $f ===\"\n    echo \"  artifacts: $(wc -c < \"$a\") bytes, $(stat -c %Y \"$a\")\"\n    echo \"  docs:      $(wc -c < \"$b\") bytes, $(stat -c %Y \"$b\")\"\n    diff -q \"$a\" \"$b\" 2>/dev/null || true\n    echo\n  fi\ndone",
  "description": "Compare file sizes and timestamps between two directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Bash",
  "tool_args": {
    "command": "for f in abstract.tex conclusion.tex experiments.tex introduction.tex method.tex; do\n  a=\"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/$f\"\n  b=\"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/$f\"\n  if [ -f \"$a\" ] && [ -f \"$b\" ]; then\n    echo \"=== $f ===\"\n    echo \"  artifacts: $(wc -c < \"$a\") bytes, $(stat -c %Y \"$a\")\"\n    echo \"  docs:      $(wc -c < \"$b\") bytes, $(stat -c %Y \"$b\")\"\n    diff -q \"$a\" \"$b\" 2>/dev/null || true\n    echo\n  fi\ndone",
    "description": "Compare file sizes and timestamps between two directories"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T14:54:32.675430+00:00_

=== abstract.tex ===
  artifacts: 935 bytes, 1778763730
  docs:      1427 bytes, 1778769746
Files /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/abstract.tex and /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex differ

=== conclusion.tex ===
  artifacts: 688 bytes, 1778769746
  docs:      1942 bytes, 1778769750
Files /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/conclusion.tex and /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex differ

=== experiments.tex ===
  artifacts: 5381 bytes, 1778769746
  docs:      7822 bytes, 1778769749
Files /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/experiments.tex and /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex differ

=== introduction.tex ===
  artifacts: 3001 bytes, 1778769741
  docs:      2913 bytes, 1778769747
Files /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/introduction.tex and /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex differ

=== method.tex ===
  artifacts: 2843 bytes, 1778769742
  docs:      3903 bytes, 1778769748
Files /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/method.tex and /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex differ

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T14:54:32.675637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T14:54:32.675798+00:00_

1	\begin{abstract}
2	LLM agents in rule-governed interactive environments face catastrophic failures when internal reasoning hallucinates state transitions. Deterministic external computation (environment simulators, code interpreters) can prevent such failures, but what does routing between these modalities actually learn? Per-step oracle labeling degenerates under sparse rewards---on ScienceWorld, 97.4\% of steps produce identical scores regardless of modality. We propose episode-level counterfactual analysis: running complete episodes under pure-internal and pure-deterministic strategies to generate routing labels from episode outcomes. Across 11 ScienceWorld task types (245 episodes), we find that death avoidance accounts for 90.41\% of the routing signal between Qwen2.5-7B-Instruct internal reasoning and deterministic computation ($\Delta_{\text{full}} = +29.60$, $\Delta_{\text{nd}} = +2.84$; Pearson $r = 0.9698$, $p = 8.12 \times 10^{-7}$ across task types). When neither strategy causes agent death, the performance gap is small but non-negligible ($\Delta_{\text{nd}} = +2.84$, 9.6\% of the total gap). A trained router does not significantly outperform an unconditional always-deterministic strategy ($-10.70$ vs.\ $-9.47$), confirming that the value of deterministic computation in this environment is concentrated in preventing catastrophic failures, not in providing positive task guidance.
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T14:54:32.675950+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T14:54:32.676134+00:00_

1	\section{Conclusion}
2	
3	We introduce episode-level counterfactual analysis for understanding routing between LLM internal reasoning and deterministic computation, overcoming per-step oracle degeneracy (97.4\% tie rate) in sparse-reward settings. On 11 ScienceWorld task types (245 episodes), death avoidance accounts for 90.41\% of routing signal ($\Delta_{\text{full}} = +29.60 \rightarrow \Delta_{\text{nd}} = +2.84$; $r = 0.9698$, $p = 8.12 \times 10^{-7}$). The value of deterministic computation is predominantly concentrated in preventing catastrophic failures.
4	
5	\paragraph{Labeling Quality.} Episode-level ties (61.2\% of pairs: 46.9\% both-alive, 14.3\% both-died) are excluded as \texttt{no\_preference} with no tie-breaking, so all 95 training labels reflect genuine outcome asymmetries (70 death-asymmetry det-preferred, 16 score-comparison det-preferred, 5 death-asymmetry internal-preferred, 4 score-comparison internal-preferred). A strict-only retrain excluding any potentially ambiguous labels yields balanced accuracy 0.5729, within $1\sigma$ of the full-label ablation (0.5761$\pm$0.005), confirming that oracle circularity does not inflate routing performance.
6	
7	\paragraph{Limitations and Future Work.} Our analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct). ScienceWorld's $-100$ death penalty may amplify the death avoidance signal; environments with less catastrophic failure modes could exhibit lower DAF values. Our counterfactual labels operate at episode granularity, limiting router training resolution. Cross-seed instability in internal recall (51.5--81.8\%) warrants further investigation. Step-level labeling with denser rewards (e.g., DAgger-style \cite{dagger-2011} imitation learning) could improve both decomposition and router training. Extension to code-interpreter routing and multi-LLM evaluation would test generalization beyond simulator-based environments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T14:54:32.676348+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T14:54:32.676683+00:00_

1	\section{Experiments}
2	
3	\subsection{Death Avoidance Decomposition}
4	\label{sec:death-decomp}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{figures/fig1_daf_scatter.pdf}
9	\caption{Per-task scatter plot: death rate differential (internal minus deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). Pearson $r = 0.9698$ ($p = 8.12 \times 10^{-7}$). Each point is one of 11 ScienceWorld task types.}
10	\label{fig:decomposition}
11	\end{figure}
12	
13	The full performance gap between deterministic and internal strategies across 245 episodes is $\Delta_{\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\Delta_{\text{nd}} = +2.84$. The resulting Death Avoidance Factor (\S\ref{sec:daf}) is 90.41\%: approximately 90\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.
14	
15	This concentration is consistent across task types. The Pearson correlation between per-task death rate differential (internal minus deterministic) and $\Delta_{\text{full}}$ is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$), as shown in Figure~\ref{fig:decomposition}. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\% of episodes compared to 16.3\% for deterministic computation---a 2.6$\times$ ratio that drives the bulk of the observed score difference.
16	
17	The episode-level label distribution reflects this asymmetry: of 245 episodes, 86 are \texttt{det\_preferred}, only 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preference}---when internal reasoning does not cause death, it performs comparably to deterministic computation.
18	
19	One task reveals the residual non-death signal. \texttt{find-non-living-thing} ($n=40$) has zero deaths under both s
…[truncated 5999 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T14:54:32.677042+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T14:54:32.677404+00:00_

1	\section{Method}
2	
3	\subsection{Counterfactual Episode Collection}
4	\label{sec:collection}
5	
6	Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \cite{scienceworld-2022}, 97.4\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.
7	
8	For each task instance, we execute two complete episodes under identical initial conditions (same random seed, same task variation). The \emph{pure-internal} episode follows the ReAct paradigm \cite{react-2023}, where the LLM interleaves chain-of-thought reasoning with environment actions. The \emph{pure-deterministic} episode uses the environment simulator to compute exact state transitions for each action. In both cases the LLM selects which action to take; deterministic computation replaces only the state-transition prediction, not action selection---equivalent to giving the agent access to a perfect world model.
9	
10	Each episode pair produces a tuple $(s^{\text{int}}, s^{\text{det}}, d^{\text{int}}, d^{\text{det}})$, where $s$ denotes the terminal score and $d \in \{0,1\}$ indicates agent death. We use Qwen2.5-7B-Instruct (vLLM) on ScienceWorld \cite{scienceworld-2022}, a text-based environment spanning 30 task types with a $-100$ death penalty, with episodes capped at 30 steps. After prescreening, we collect 245 episode pairs across 11 task types (20--40 per type).
11	
12	\subsection{Death-Aware Labeling}
13	\label{sec:labeling}
14	
15	Each counterfactual pair receives an episode-level routing label based on $(s^{\text{int}}, s^{\text{det}}, d^{\text{int}}, d^{\text{det}})$. ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. The label is assigned by one of four mutually exclusive cases:
16	
17	\begin{enumerate}
18	    \item \textbf{Death asymmetry
…[truncated 2014 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T14:54:32.677606+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T14:54:32.677776+00:00_

1	\section{Introduction}
2	
3	When a Qwen2.5-7B-Instruct agent attempts to boil water in ScienceWorld \cite{scienceworld-2022}, it must track temperature thresholds and container states across dozens of steps. Internal reasoning hallucinates these transitions---predicting water has boiled when the stove was never activated---triggering agent death with a $-100$ penalty. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The natural question: when should an agent route computation externally versus reasoning internally?
4	
5	Existing routing approaches \cite{toolformer-2024,art-2023,chameleon-2024} frame tool selection as a capability or efficiency decision---matching subtasks to tools that can solve them. This framing ignores a potentially dominant signal: routing to \emph{avoid catastrophic failure}. Understanding what routing actually learns requires counterfactual analysis, but the standard per-step oracle approach degenerates under sparse rewards. On ScienceWorld, where non-zero reward arrives only at episode termination, 97.4\% of steps produce identical scores regardless of modality---no step-level signal exists to train a router (\S\ref{sec:collection}). Keyword-based heuristics (\S\ref{sec:rule}) also fail structurally: ScienceWorld actions use generic verbs (\texttt{pour}, \texttt{move}, \texttt{activate}) rather than science-specific terminology, providing no lexical basis for routing decisions.
6	
7	We propose \emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct~\cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\S\ref{sec:collection}). Across 11 ScienceWorld task types (245 episodes), the full deterministic advantage is $\Delta_{\text{full}} = +29.60$ points. Excluding episodes where either strategy causes agent death, this gap collapses to $\Delta_{\text{nd}} = +2.8
…[truncated 931 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T14:54:32.677945+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -rn 'TODO\\|FIXME\\|XXX\\|PLACEHOLDER\\|TBD' /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/*.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/*.tex 2>/dev/null",
  "description": "Find all TODO/FIXME markers in both directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -rn 'TODO\\|FIXME\\|XXX\\|PLACEHOLDER\\|TBD' /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/*.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/*.tex 2>/dev/null",
    "description": "Find all TODO/FIXME markers in both directories"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T14:54:32.678200+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/discussion.tex:7:% TODO: Replace pilot-50 numbers with math-200-fixed results when available
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/discussion.tex:12:% TODO: ALFWorld results pending; add cross-environment comparison if signal emerges

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T14:54:32.678481+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T14:54:32.678790+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool-Use Learning.}
4	Toolformer \cite{toolformer-2024} inserts API calls via self-supervised filtering; ART \cite{art-2023} and Chameleon \cite{chameleon-2024} compose tools under LLM orchestration; ReTool \cite{retool-2026} applies RL for code-interpreter invocation.
5	We differ by generating routing labels via \emph{episode-level counterfactual analysis}, framing routing as \emph{catastrophic failure prevention}, and training an explicit lightweight router for diagnostic analysis.
6	
7	\paragraph{Adaptive Computation.}
8	CogRouter \cite{cogrouter-2026} routes among cognitive depth levels on ScienceWorld; ARES \cite{ares-2026} selects per-step reasoning effort; Mixture-of-Recursions \cite{mixture-of-recursions-2025} applies adaptive depth at the architecture level.
9	MTRouter \cite{mtrouter-2026} routes among LLMs to optimize cost-quality tradeoffs.
10	These methods route \emph{how much} or \emph{which model}; we route \emph{which modality} and find that death avoidance accounts for ${\sim}90\%$ of the routing signal.
11	
12	\paragraph{World Model Routing.}
13	ITP \cite{itp-2026} and Dyna-Think \cite{dynathink-2025} route to approximate LLM-based world models that inherit hallucination failures.
14	Our deterministic modality provides exact state transitions, and our analysis reveals that this exactness matters almost exclusively for death avoidance.
15	
16	\paragraph{Agent Frameworks.}
17	ReAct \cite{react-2023} interleaves reasoning and acting and serves as our internal-reasoning baseline. We analyze \emph{when} reasoning should yield to deterministic computation, finding the answer concentrated in catastrophic failure scenarios.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T14:54:32.679163+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/51870e0b-e7be-4f0d-82f1-db4a37356f5f/tool-results/mcp-agent-ml-research-read_registry-1778770085071.txt') as f:\n    data = json.loads(f.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor eid in ['math-200-fixed']:\n    exp = exps.get(eid, {})\n    if exp:\n        print(f'=== {eid} ===')\n        print(f'  status: {exp.get(\\\"status\\\")}')\n        c = exp.get('conclusion','')\n        if c: print(f'  conclusion: {c[:500]}')\n        m = exp.get('metrics',{})\n        if m: print(f'  metrics: {json.dumps(m, indent=2)[:1000]}')\n        n = exp.get('notes','')\n        if n: print(f'  notes: {str(n)[:800]}')\n\" 2>&1",
  "description": "Check math-200-fixed experiment status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/51870e0b-e7be-4f0d-82f1-db4a37356f5f/tool-results/mcp-agent-ml-research-read_registry-1778770085071.txt') as f:\n    data = json.loads(f.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor eid in ['math-200-fixed']:\n    exp = exps.get(eid, {})\n    if exp:\n        print(f'=== {eid} ===')\n        print(f'  status: {exp.get(\\\"status\\\")}')\n        c = exp.get('conclusion','')\n        if c: print(f'  conclusion: {c[:500]}')\n        m = exp.get('metrics',{})\n        if m: print(f'  metrics: {json.dumps(m, indent=2)[:1000]}')\n        n = exp.get('notes','')\n        if n: print(f'  notes: {str(n)[:800]}')\n\" 2>&1",
    "description": "Check math-200-fixed experiment status"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T14:54:32.679402+00:00_

=== math-200-fixed ===
  status: DONE
  conclusion: failed
  notes: Crashed at problem 56/200 with HTTP 400 from vLLM (localhost:8000). Partial results: 55/200 completed. Internal acc 44/55=80.0%, CodeInterp acc 41/55=74.5%, code exec rate 44/55=80.0% (11 had 0 code rounds). Labels: no-preference 45, internal-preferred 7, det-preferred 3. 11 FILTERED. 0 sandbox empty output issues (auto_print_last_expr fix effective). Need to investigate vLLM 400 error on problem 56 and resume from offset.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T14:54:32.679661+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i 'undefined\\|multiply\\|Warning.*ref' /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/main.log 2>/dev/null | head -20",
  "description": "Check for undefined references in LaTeX log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -i 'undefined\\|multiply\\|Warning.*ref' /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/main.log 2>/dev/null | head -20",
    "description": "Check for undefined references in LaTeX log"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T14:54:32.679869+00:00_

Package lineno Warning: Line number reference failed, re-run to get it right.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T14:54:32.680202+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/paper_audit_report.md",
  "content": "# Paper Full-Number Audit & Structural Integrity Report\n\n**Date**: 2026-05-14  \n**Paper**: \"Death Avoidance Accounts for 90% of the Routing Signal in LLM Agent Tool Use\"  \n**Target**: EMNLP 2026 ARR short paper (4 pages + refs), DDL 2026-05-25\n\n---\n\n## 1. Canonical Directory Determination\n\n**Canonical**: `artifacts/_project/paper/latex/` (8 .tex files)  \n**Non-canonical**: `docs/paper/` (7 .tex files, no discussion.tex)\n\n### Evidence\n\n| Criterion | artifacts/ | docs/paper/ |\n|-----------|-----------|-------------|\n| `\\input{discussion}` in main.tex | ✅ Yes | ❌ No |\n| discussion.tex exists | ✅ Yes | ❌ No |\n| Limitations section | ✅ In main.tex | ❌ Absent |\n| Ethics Statement | ✅ In main.tex | ❌ Absent |\n| Compiled PDF timestamp | 14:45 (latest) | 12:24 |\n| CI level | **95%** (from plan-003-bootstrap-95ci) | 90% (from older baseline) |\n\n### ⚠️ CRITICAL: Directory Divergence\n\n**The two directories are divergent — neither is a superset of the other.** `docs/paper/` contains significant content NOT present in `artifacts/`:\n\n| Content | artifacts/ | docs/paper/ |\n|---------|-----------|-------------|\n| Abstract | 935 bytes, briefer | **1427 bytes**, includes Δ_full, Δ_nd, router score numbers |\n| Method: Rule-Based Baseline (§rule) | ❌ Missing subsection | ✅ Has `\\subsection{Rule-Based Baseline}` with 3 keyword lists |\n| Experiments: Labeling quality ¶ | ❌ Not in experiments | ✅ Full paragraph in §router-diagnostic |\n| Conclusion: Labeling Quality ¶ | ❌ Not in conclusion | ✅ Detailed paragraph |\n| Conclusion: Limitations & Future Work ¶ | ❌ Not in conclusion | ✅ Full paragraph with DAgger cite |\n| Router diagnostic detail | Shorter, seed table in notes | **Longer**: logit-gen gap analysis, 3 observations paragraph |\n| Table 1 CI level | 95% Bootstrap CI | 90% CI |\n\n**Recommendation**: Merge content from `docs/paper/` into `artifacts/` before submission. Specifically:\n1. Use the longer abstract from `docs/`\n2. Add Rule-Based Baseline subsection to method.tex\n3. Consider whether labeling quality belongs in Conclusion (docs/) or Limitations (artifacts/) — currently duplicated across directories\n4. The 95% CI in artifacts/ is correct (matches experiment name `plan-003-bootstrap-95ci`)\n5. After merge, **deprecate** `docs/paper/` to avoid future divergence\n\n---\n\n## 2. Number Audit (Canonical: artifacts/)\n\n### Table 1 — Baselines\n\n| Strategy | Paper Score | Registry Source | Paper CI | Registry CI | Paper Death% | ✅/❌ |\n|----------|-------------|----------------|----------|-------------|-------------|-------|\n| Always-Internal | -39.07 | plan-003-bootstrap-95ci: -39.07 | [-46.40, -32.27] | [-46.4, -32.27] | 42.9 | ✅ |\n| Always-Det. | -9.47 | plan-003-bootstrap-95ci: -9.47 | [-14.71, -4.29] | [-14.71, -4.29] | 16.3 | ✅ |\n| Random | -22.38 | plan-003-bootstrap-95ci: -22.38 | [-28.67, -15.75] | [-28.67, -15.75] | 27.8 | ✅ |\n| Oracle | -6.58 | plan-003-bootstrap-95ci: -6.58 | [-11.54, -1.70] | [-11.54, -1.7] | 14.3 | ✅ |\n| Trained Router | -10.70 | plan-003-bootstrap-95ci: -10.7 | [-16.33, -5.27] | [-16.33, -5.27] | 17.6 | ✅ |\n\n**Trained Router source**: ✅ Correctly uses -10.70 from `plan-003-e2e-ablation-b-correct` (ablation-b seed42 checkpoint). NOT -12.84 (that's `plan-003-eval-implicit` / wrong checkpoint).\n\n**Note**: `plan-003-e2e-ablation-b-correct` raw CI is [-15.25, -6.38], while `plan-003-bootstrap-95ci` reports [-16.33, -5.27]. The bootstrap CI is wider because it's 95% vs. possibly 90% in the raw experiment. Paper correctly uses the bootstrap-95ci values.\n\n### DAF Decomposition\n\n| Metric | Paper Value | Registry Source | Registry Value | ✅/❌ |\n|--------|------------|----------------|---------------|-------|\n| DAF | 90.41% | plan-012-full | 0.9041 | ✅ |\n| Δ_full | +29.60 | plan-012-full | 29.6 | ✅ |\n| Δ_nd | +2.84 | plan-012-full | 2.84 | ✅ |\n| Δ_nd/Δ_full | 9.6% | computed | 2.84/29.60 = 0.09595 | ✅ |\n| DAF check | 1 - 2.84/29.60 | computed | 0.90405 → 90.41% | ✅ |\n| Pearson r | 0.9698 | plan-012-full | 0.9698 | ✅ |\n| Pearson p | 8.12e-07 | plan-012-full | 8.12e-07 | ✅ |\n| Death rate internal | 42.9% | plan-012-full | 0.429 | ✅ |\n| Death rate det | 16.3% | plan-012-full | 0.163 | ✅ |\n| Death ratio | 2.6× | computed | 42.9/16.3 = 2.63 | ✅ |\n\n### Label Distribution\n\n| Metric | Paper Value | Registry Source | Registry Value | ✅/❌ |\n|--------|------------|----------------|---------------|-------|\n| det_preferred | 86 | plan-012-full | 86 | ✅ |\n| internal_preferred | 9 | plan-012-full | 9 | ✅ |\n| no_preference | 150 | plan-012-full | 150 | ✅ |\n| Oracle matches always-det | 96.3% | computed | (86+150)/245 = 96.3% | ✅ |\n\n### Step-Level Tie Rate\n\n| Metric | Paper Value | Registry Source | Registry Value | ✅/❌ |\n|--------|------------|----------------|---------------|-------|\n| Tie rate | 97.4% | plan-012-step-tie-rate | 0.9739 → 97.39% | ✅ |\n| NOT 98.2% | ✅ Correct | plan-012-step-tie-rate notes | \"Delta from old MVP = -0.78pp (97.39% vs 98.2%)\" | ✅ |\n\n### Router Diagnostic\n\n| Metric | Paper Value | Registry Source | Registry Value | ✅/❌ |\n|--------|------------|----------------|---------------|-------|\n| 4-seed balanced_acc | 58.1±0.8% | plan-004-ablation-b notes | Seeds: 59.27, 57.36, 57.48, 58.31 → mean 58.1, std 0.8 | ✅ |\n| GA=8 seed42 generation acc | 65.4% | plan-004-ablation-b | 0.6536 | ✅ |\n| GA=8 seed42 internal recall | 51.5% | plan-004-ablation-b | 0.5152 | ✅ |\n| GA=1 logit accuracy | 74.5% | plan-004-v5 | 0.7451 | ✅ |\n| GA=1 logit balanced_acc | 79% | plan-004-v5 | 0.7905 → ~79% | ✅ |\n| GA=1 generation accuracy | 53.3% | plan-004-v5 | 0.5333 | ✅ |\n| GA=1 generation internal recall | 26.7% | plan-004-v5 | 0.2667 | ✅ |\n| Logit-gen gap | 21.2pp | computed | 74.5 - 53.3 = 21.2 | ✅ |\n| Sim invocation ratio | 97.0% | plan-003-e2e-ablation-b-correct | 0.9703 | ✅ |\n| Internal recall range | 51.5%–81.8% | plan-004 seeds | 51.52, 57.58, 75.76, 81.82 | ✅ |\n| \"8 points above chance\" | 58.1 - 50 = 8.1 | computed | ✅ | ✅ |\n\n### Labeling Quality (Limitations section)\n\n| Metric | Paper Value | Registry Source | Registry Value | ✅/❌ |\n|--------|------------|----------------|---------------|-------|\n| Total labels | 245 | plan-013-labeling-quality | N/A (consistent with 245 eps) | ✅ |\n| no_preference | 150 (61.2%) | plan-013 | tie_rate=0.612 → 150/245 | ✅ |\n| Both-alive ties | 115 (46.9%) | plan-013 | tie_rate_both_alive=0.469 → 114.9≈115 | ✅ |\n| Both-dead | 35 (14.3%) | plan-013 | tie_rate_both_died=0.143 → 35.0 | ✅ |\n| Genuine training labels | 95 | plan-013 notes | 70+16+5+4=95 | ✅ |\n| Death asymmetry det-pref | 70 | plan-013 | det_preferred_death_asymmetry=70 | ✅ |\n| Score comparison det-pref | 16 | plan-013 | det_preferred_score_comparison=16 | ✅ |\n| Death asymmetry int-pref | 5 | plan-013 notes | 5 | ✅ |\n| Score comparison int-pref | 4 | plan-013 notes | 4 | ✅ |\n| Tie-break fraction | 0% | plan-013 | tiebreak_det_fraction=0 | ✅ |\n| Strict retrain balanced_acc | 57.3% | plan-013 | 0.5729 | ✅ |\n| Full-label ablation | 57.6±0.5% | plan-013 | 0.5761±0.0047 | ✅ |\n\n### MATH Pilot (Discussion section)\n\n| Metric | Paper Value | Registry Source | Registry Value | ✅/❌ |\n|--------|------------|----------------|---------------|-------|\n| N problems | 50 | math-pilot-50 | n_problems=50 | ✅ |\n| Internal accuracy | 80% | math-pilot-50 | 0.80 | ✅ |\n| Code interpreter accuracy | 72% | math-pilot-50 | 0.72 | ✅ |\n| No-preference rate | 88% | math-pilot-50 | 44/50=0.88 | ✅ |\n| det-preferred | 1 | math-pilot-50 | 1 | ✅ |\n| internal-preferred | 5 | math-pilot-50 | 5 | ✅ |\n| no-preference | 44 | math-pilot-50 | 44 | ✅ |\n\n⚠️ **Caveat**: math-pilot-50 notes flag a sandbox bug: 34.1% of code executions had empty output. Clean code-interpreter accuracy (non-empty output only) is 88.9%, not 72%. The discussion.tex acknowledges \"sandbox limitations\" but uses the raw 72% as the headline. The `math-200-fixed` experiment (with sandbox fix) crashed at problem 56/200, showing 74.5% code-interpreter accuracy on 55 problems — directionally consistent but incomplete.\n\n### Abstract Numbers\n\n| Number | Paper Value | Cross-check | ✅/❌ |\n|--------|------------|-------------|-------|\n| 97.4% step tie rate | ✅ | plan-012-step-tie-rate | ✅ |\n| 245 episodes | ✅ | plan-012-full | ✅ |\n| ~90% DAF | ✅ | 90.41% in body | ✅ |\n| r = 0.97 | ✅ | 0.9698 rounded | ✅ |\n\n### Internal Consistency Across Sections\n\nAll numbers are consistent across abstract, introduction, method, experiments, discussion, conclusion, and limitations. No contradictions found between sections.\n\n**Overall number audit: 100% PASS (all numbers verified against registry)**\n\n---\n\n## 3. Structural Integrity Check\n\n### Section Substance\n\n| Section | File | Substantive? | Notes |\n|---------|------|-------------|-------|\n| Abstract | abstract.tex | ✅ | Complete but shorter than docs/ version |\n| Introduction | introduction.tex | ✅ | Complete with contributions |\n| Method | method.tex | ✅ | 3 subsections (collection, labeling, DAF) |\n| Experiments | experiments.tex | ✅ | 4 subsections (setup, decomp, baselines, router) |\n| Related Work | related_work.tex | ✅ | 4 paragraphs |\n| Discussion | discussion.tex | ✅ | 2 paragraphs + 2 TODOs |\n| Conclusion | conclusion.tex | ✅ | Single paragraph |\n| Limitations | main.tex | ✅ | 2 paragraphs (general + labeling quality) |\n| Ethics | main.tex | ✅ | Single paragraph |\n\n### Related Work Coverage\n\nRequired references (from paper_framing.md):\n\n| Reference | Present? | Location |\n|-----------|----------|----------|\n| Toolformer | ✅ | Tool-Use Learning ¶ |\n| ART | ✅ | Tool-Use Learning ¶ |\n| Chameleon | ✅ | Tool-Use Learning ¶ |\n| CogRouter | ✅ | Adaptive Computation ¶ |\n| ARES | ✅ | Adaptive Computation ¶ |\n| ITP (ITP-R) | ✅ | World Model Routing ¶ |\n| ReAct | ✅ | Agent Frameworks ¶ |\n\nAdditional: ReTool, Mixture-of-Recursions, Dyna-Think, MTRouter — good coverage.\n\n### TODO/FIXME Comments\n\n| File | Line | Content | Status |\n|------|------|---------|--------|\n| discussion.tex | 7 | `% TODO: Replace pilot-50 numbers with math-200-fixed results when available` | ⚠️ math-200-fixed crashed at 56/200, incomplete |\n| discussion.tex | 12 | `% TODO: ALFWorld results pending; add cross-environment comparison if signal emerges` | ⚠️ No ALFWorld experiment in registry |\n\n### Discussion Section\n\n- ✅ MATH pilot paragraph present with correct numbers\n- ✅ ALFWorld placeholder as TODO comment (no data yet)\n- ✅ \"Scope and future directions\" paragraph present\n\n### Conclusion: Labeling Quality\n\n- ❌ **Labeling quality paragraph is NOT in conclusion.tex** — it is in the Limitations section of main.tex\n- The `docs/paper/conclusion.tex` version DOES include it (Labeling Quality ¶ + Limitations & Future Work ¶)\n- **Decision needed**: Should labeling quality be in Conclusion (as in docs/) or Limitations (as in artifacts/)? Current artifacts/ placement in Limitations is defensible but the user mentioned \"plan-013 入 conclusion\" as a today task\n\n---\n\n## 4. Issues List (Priority Order)\n\n### P0 — Must Fix Before Submission\n\n1. **Directory divergence**: Two divergent paper directories with non-overlapping content. Must merge `docs/paper/` improvements into `artifacts/` and deprecate `docs/paper/`. Key missing content in artifacts/:\n   - Longer, more specific abstract\n   - Rule-Based Baseline subsection in method.tex\n   - Labeling quality paragraph in experiments.tex\n   - More detailed router diagnostic analysis\n   - DAgger citation in conclusion/limitations\n\n2. **Two TODO comments in discussion.tex**: Lines 7 and 12. Either resolve or remove before submission. math-200-fixed is incomplete (crashed at 56/200) so pilot-50 numbers may need to stand.\n\n### P1 — Should Fix\n\n3. **Labeling quality placement**: User intended \"plan-013 入 conclusion\" but artifacts/ has it in Limitations. Verify intended placement. The docs/ version places it in Conclusion — if that was the intent, move it.\n\n4. **MATH pilot 72% accuracy caveat**: Known sandbox bug inflates the performance gap (clean accuracy is ~89% vs 72% reported). The TODO to replace with math-200-fixed cannot be resolved yet (experiment crashed). Consider adding a footnote about the sandbox limitation's impact on the 72% number.\n\n### P2 — Nice to Have\n\n5. **Abstract completeness**: artifacts/ abstract (935 bytes) is sparse compared to docs/ version (1427 bytes). The docs/ abstract includes Δ_full, Δ_nd, router comparison numbers which strengthen the abstract. Consider adopting the longer version.\n\n6. **Conclusion brevity**: artifacts/ conclusion is a single paragraph (688 bytes). The docs/ version (1942 bytes) includes labeling quality and future work, making it more complete for a short paper where space is tight but reviewers want to see awareness of limitations.\n\n7. **`toolformer-2024` bib key**: Year in key (2024) doesn't match year field (2023). Cosmetic but could confuse contributors.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/paper_audit_report.md",
    "content": "# Paper Full-Number Audit & Structural Integrity Report\n\n**Date**: 2026-05-14  \n**Paper**: \"Death Avoidance Accounts for 90% of the Routing Signal in LLM Agent Tool Use\"  \n**Target**: EMNLP 2026 ARR short paper (4 pages + refs), DDL 2026-05-25\n\n---\n\n## 1. Canonical Directory Determination\n\n**Canonical**: `artifacts/_project/paper/latex/` (8 .tex files)  \n**Non-canonical**: `docs/paper/` (7 .tex files, no discussion.tex)\n\n### Evidence\n\n| Criterion | artifacts/ | docs/paper/ |\n|-----------|-----------|-------------|\n| `\\input{discussion}` in main.tex | ✅ Yes | ❌ No |\n| discussion.tex exists | ✅ Yes | ❌ No |\n| Limitations section | ✅ In main.tex | ❌ Absent |\n| Ethics Statement | ✅ In main.tex | ❌ Absent |\n| Compiled PDF timestamp | 14:45 (latest) | 12:24 |\n| CI level | **95%** (from plan-003-bootstrap-95ci) | 90% (from older baseline) |\n\n### ⚠️ CRITICAL: Directory Divergence\n\n**The two directories are divergent — neither is a superset of the other.** `docs/paper/` contains significant content NOT present in `artifacts/`:\n\n| Content | artifacts/ | docs/paper/ |\n|---------|-----------|-------------|\n| Abstract | 935 bytes, briefer | **1427 bytes**, includes Δ_full, Δ_nd, router score numbers |\n| Method: Rule-Based Baseline (§rule) | ❌ Missing subsection | ✅ Has `\\subsection{Rule-Based Baseline}` with 3 keyword lists |\n| Experiments: Labeling quality ¶ | ❌ Not in experiments | ✅ Full paragraph in §router-diagnostic |\n| Conclusion: Labeling Quality ¶ | ❌ Not in conclusion | ✅ Detailed paragraph |\n| Conclusion: Limitations & Future Work ¶ | ❌ Not in conclusion | ✅ Full paragraph with DAgger cite |\n| Router diagnostic detail | Shorter, seed table in notes | **Longer**: logit-gen gap analysis, 3 observations paragraph |\n| Table 1 CI level | 95% Bootstrap CI | 90% CI |\n\n**Recommendation**: Merge content from `docs/paper/` into `artifacts/` before submission. Specifically:\n1. Use the longer abstract from `docs/`\n2. Add Rule-Based Baseline subsection to method.tex\n3. Consider whether labeling quality belongs in Conclusion (docs/) or Limitations (artifacts/) — currently duplicated across directories\n4. The 95% CI in artifacts/ is correct (matches experiment name `plan-003-bootstrap-95ci`)\n5. After merge, **deprecate** `docs/paper/` to avoid future divergence\n\n---\n\n## 2. Number Audit (Canonical: artifacts/)\n\n### Table 1 — Baselines\n\n| Strategy | Paper Score | Registry Source | Paper CI | Registry CI | Paper Death% | ✅/❌ |\n|----------|-------------|----------------|----------|-------------|-------------|-------|\n| Always-Internal | -39.07 | plan-003-bootstrap-95ci: -39.07 | [-46.40, -32.27] | [-46.4, -32.27] | 42.9 | ✅ |\n| Always-Det. | -9.47 | plan-003-bootstrap-95ci: -9.47 | [-14.71, -4.29] | [-14.71, -4.29] | 16.3 | ✅ |\n| Random | -22.38 | plan-003-bootstrap-95ci: -22.38 | [-28.67, -15.75] | [-28.67, -15.75] | 27.8 | ✅ |\n| Oracle | -6.58 | plan-003-bootstrap-95ci: -6.58 | [-11.54, -1.70] | [-11.54, -1.7] | 14.3 | ✅ |\n| Trained Router | -10.70 | plan-003-bootstrap-95ci: -10.7 | [-16.33, -5.27] | [-16.33, -5.27] | 17.6 | ✅ |\n\n**Trained Router source**: ✅ Correctly uses -10.70 from `plan-003-e2e-ablation-b-correct` (ablation-b seed42 checkpoint). NOT -12.84 (that's `plan-003-eval-implicit` / wrong checkpoint).\n\n**Note**: `plan-003-e2e-ablation-b-correct` raw CI is [-15.25, -6.38], while `plan-003-bootstrap-95ci` reports [-16.33, -5.27]. The bootstrap CI is wider because it's 95% vs. possibly 90% in the raw experiment. Paper correctly uses the bootstrap-95ci values.\n\n### DAF Decomposition\n\n| Metric | Paper Value | Registry Source | Registry Value | ✅/❌ |\n|--------|------------|----------------|---------------|-------|\n| DAF | 90.41% | plan-012-full | 0.9041 | ✅ |\n| Δ_full | +29.60 | plan-012-full | 29.6 | ✅ |\n| Δ_nd | +2.84 | plan-012-full | 2.84 | ✅ |\n| Δ_nd/Δ_full | 9.6% | computed | 2.84/29.60 = 0.09595 | ✅ |\n| DAF check | 1 - 2.84/29.60 | computed | 0.90405 → 90.41% | ✅ |\n| Pearson r | 0.9698 | plan-012-full | 0.9698 | ✅ |\n| Pearson p | 8.12e-07 | plan-012-full | 8.12e-07 | ✅ |\n| Death rate internal | 42.9% | plan-012-full | 0.429 | ✅ |\n| Death rate det | 16.3% | plan-012-full | 0.163 | ✅ |\n| Death ratio | 2.6× | computed | 42.9/16.3 = 2.63 | ✅ |\n\n### Label Distribution\n\n| Metric | Paper Value | Registry Source | Registry Value | ✅/❌ |\n|--------|------------|----------------|---------------|-------|\n| det_preferred | 86 | plan-012-full | 86 | ✅ |\n| internal_preferred | 9 | plan-012-full | 9 | ✅ |\n| no_preference | 150 | plan-012-full | 150 | ✅ |\n| Oracle matches always-det | 96.3% | computed | (86+150)/245 = 96.3% | ✅ |\n\n### Step-Level Tie Rate\n\n| Metric | Paper Value | Registry Source | Registry Value | ✅/❌ |\n|--------|------------|----------------|---------------|-------|\n| Tie rate | 97.4% | plan-012-step-tie-rate | 0.9739 → 97.39% | ✅ |\n| NOT 98.2% | ✅ Correct | plan-012-step-tie-rate notes | \"Delta from old MVP = -0.78pp (97.39% vs 98.2%)\" | ✅ |\n\n### Router Diagnostic\n\n| Metric | Paper Value | Registry Source | Registry Value | ✅/❌ |\n|--------|------------|----------------|---------------|-------|\n| 4-seed balanced_acc | 58.1±0.8% | plan-004-ablation-b notes | Seeds: 59.27, 57.36, 57.48, 58.31 → mean 58.1, std 0.8 | ✅ |\n| GA=8 seed42 generation acc | 65.4% | plan-004-ablation-b | 0.6536 | ✅ |\n| GA=8 seed42 internal recall | 51.5% | plan-004-ablation-b | 0.5152 | ✅ |\n| GA=1 logit accuracy | 74.5% | plan-004-v5 | 0.7451 | ✅ |\n| GA=1 logit balanced_acc | 79% | plan-004-v5 | 0.7905 → ~79% | ✅ |\n| GA=1 generation accuracy | 53.3% | plan-004-v5 | 0.5333 | ✅ |\n| GA=1 generation internal recall | 26.7% | plan-004-v5 | 0.2667 | ✅ |\n| Logit-gen gap | 21.2pp | computed | 74.5 - 53.3 = 21.2 | ✅ |\n| Sim invocation ratio | 97.0% | plan-003-e2e-ablation-b-correct | 0.9703 | ✅ |\n| Internal recall range | 51.5%–81.8% | plan-004 seeds | 51.52, 57.58, 75.76, 81.82 | ✅ |\n| \"8 points above chance\" | 58.1 - 50 = 8.1 | computed | ✅ | ✅ |\n\n### Labeling Quality (Limitations section)\n\n| Metric | Paper Value | Registry Source | Registry Value | ✅/❌ |\n|--------|------------|----------------|---------------|-------|\n| Total labels | 245 | plan-013-labeling-quality | N/A (consistent with 245 eps) | ✅ |\n| no_preference | 150 (61.2%) | plan-013 | tie_rate=0.612 → 150/245 | ✅ |\n| Both-alive ties | 115 (46.9%) | plan-013 | tie_rate_both_alive=0.469 → 114.9≈115 | ✅ |\n| Both-dead | 35 (14.3%) | plan-013 | tie_rate_both_died=0.143 → 35.0 | ✅ |\n| Genuine training labels | 95 | plan-013 notes | 70+16+5+4=95 | ✅ |\n| Death asymmetry det-pref | 70 | plan-013 | det_preferred_death_asymmetry=70 | ✅ |\n| Score comparison det-pref | 16 | plan-013 | det_preferred_score_comparison=16 | ✅ |\n| Death asymmetry int-pref | 5 | plan-013 notes | 5 | ✅ |\n| Score comparison int-pref | 4 | plan-013 notes | 4 | ✅ |\n| Tie-break fraction | 0% | plan-013 | tiebreak_det_fraction=0 | ✅ |\n| Strict retrain balanced_acc | 57.3% | plan-013 | 0.5729 | ✅ |\n| Full-label ablation | 57.6±0.5% | plan-013 | 0.5761±0.0047 | ✅ |\n\n### MATH Pilot (Discussion section)\n\n| Metric | Paper Value | Registry Source | Registry Value | ✅/❌ |\n|--------|------------|----------------|---------------|-------|\n| N problems | 50 | math-pilot-50 | n_problems=50 | ✅ |\n| Internal accuracy | 80% | math-pilot-50 | 0.80 | ✅ |\n| Code interpreter accuracy | 72% | math-pilot-50 | 0.72 | ✅ |\n| No-preference rate | 88% | math-pilot-50 | 44/50=0.88 | ✅ |\n| det-preferred | 1 | math-pilot-50 | 1 | ✅ |\n| internal-preferred | 5 | math-pilot-50 | 5 | ✅ |\n| no-preference | 44 | math-pilot-50 | 44 | ✅ |\n\n⚠️ **Caveat**: math-pilot-50 notes flag a sandbox bug: 34.1% of code executions had empty output. Clean code-interpreter accuracy (non-empty output only) is 88.9%, not 72%. The discussion.tex acknowledges \"sandbox limitations\" but uses the raw 72% as the headline. The `math-200-fixed` experiment (with sandbox fix) crashed at problem 56/200, showing 74.5% code-interpreter accuracy on 55 problems — directionally consistent but incomplete.\n\n### Abstract Numbers\n\n| Number | Paper Value | Cross-check | ✅/❌ |\n|--------|------------|-------------|-------|\n| 97.4% step tie rate | ✅ | plan-012-step-tie-rate | ✅ |\n| 245 episodes | ✅ | plan-012-full | ✅ |\n| ~90% DAF | ✅ | 90.41% in body | ✅ |\n| r = 0.97 | ✅ | 0.9698 rounded | ✅ |\n\n### Internal Consistency Across Sections\n\nAll numbers are consistent across abstract, introduction, method, experiments, discussion, conclusion, and limitations. No contradictions found between sections.\n\n**Overall number audit: 100% PASS (all numbers verified against registry)**\n\n---\n\n## 3. Structural Integrity Check\n\n### Section Substance\n\n| Section | File | Substantive? | Notes |\n|---------|------|-------------|-------|\n| Abstract | abstract.tex | ✅ | Complete but shorter than docs/ version |\n| Introduction | introduction.tex | ✅ | Complete with contributions |\n| Method | method.tex | ✅ | 3 subsections (collection, labeling, DAF) |\n| Experiments | experiments.tex | ✅ | 4 subsections (setup, decomp, baselines, router) |\n| Related Work | related_work.tex | ✅ | 4 paragraphs |\n| Discussion | discussion.tex | ✅ | 2 paragraphs + 2 TODOs |\n| Conclusion | conclusion.tex | ✅ | Single paragraph |\n| Limitations | main.tex | ✅ | 2 paragraphs (general + labeling quality) |\n| Ethics | main.tex | ✅ | Single paragraph |\n\n### Related Work Coverage\n\nRequired references (from paper_framing.md):\n\n| Reference | Present? | Location |\n|-----------|----------|----------|\n| Toolformer | ✅ | Tool-Use Learning ¶ |\n| ART | ✅ | Tool-Use Learning ¶ |\n| Chameleon | ✅ | Tool-Use Learning ¶ |\n| CogRouter | ✅ | Adaptive Computation ¶ |\n| ARES | ✅ | Adaptive Computation ¶ |\n| ITP (ITP-R) | ✅ | World Model Routing ¶ |\n| ReAct | ✅ | Agent Frameworks ¶ |\n\nAdditional: ReTool, Mixture-of-Recursions, Dyna-Think, MTRouter — good coverage.\n\n### TODO/FIXME Comments\n\n| File | Line | Content | Status |\n|------|------|---------|--------|\n| discussion.tex | 7 | `% TODO: Replace pilot-50 numbers with math-200-fixed results when available` | ⚠️ math-200-fixed crashed at 56/200, incomplete |\n| discussion.tex | 12 | `% TODO: ALFWorld results pending; add cross-environment comparison if signal emerges` | ⚠️ No ALFWorld experiment in registry |\n\n### Discussion Section\n\n- ✅ MATH pilot paragraph present with correct numbers\n- ✅ ALFWorld placeholder as TODO comment (no data yet)\n- ✅ \"Scope and future directions\" paragraph present\n\n### Conclusion: Labeling Quality\n\n- ❌ **Labeling quality paragraph is NOT in conclusion.tex** — it is in the Limitations section of main.tex\n- The `docs/paper/conclusion.tex` version DOES include it (Labeling Quality ¶ + Limitations & Future Work ¶)\n- **Decision needed**: Should labeling quality be in Conclusion (as in docs/) or Limitations (as in artifacts/)? Current artifacts/ placement in Limitations is defensible but the user mentioned \"plan-013 入 conclusion\" as a today task\n\n---\n\n## 4. Issues List (Priority Order)\n\n### P0 — Must Fix Before Submission\n\n1. **Directory divergence**: Two divergent paper directories with non-overlapping content. Must merge `docs/paper/` improvements into `artifacts/` and deprecate `docs/paper/`. Key missing content in artifacts/:\n   - Longer, more specific abstract\n   - Rule-Based Baseline subsection in method.tex\n   - Labeling quality paragraph in experiments.tex\n   - More detailed router diagnostic analysis\n   - DAgger citation in conclusion/limitations\n\n2. **Two TODO comments in discussion.tex**: Lines 7 and 12. Either resolve or remove before submission. math-200-fixed is incomplete (crashed at 56/200) so pilot-50 numbers may need to stand.\n\n### P1 — Should Fix\n\n3. **Labeling quality placement**: User intended \"plan-013 入 conclusion\" but artifacts/ has it in Limitations. Verify intended placement. The docs/ version places it in Conclusion — if that was the intent, move it.\n\n4. **MATH pilot 72% accuracy caveat**: Known sandbox bug inflates the performance gap (clean accuracy is ~89% vs 72% reported). The TODO to replace with math-200-fixed cannot be resolved yet (experiment crashed). Consider adding a footnote about the sandbox limitation's impact on the 72% number.\n\n### P2 — Nice to Have\n\n5. **Abstract completeness**: artifacts/ abstract (935 bytes) is sparse compared to docs/ version (1427 bytes). The docs/ abstract includes Δ_full, Δ_nd, router comparison numbers which strengthen the abstract. Consider adopting the longer version.\n\n6. **Conclusion brevity**: artifacts/ conclusion is a single paragraph (688 bytes). The docs/ version (1942 bytes) includes labeling quality and future work, making it more complete for a short paper where space is tight but reviewers want to see awareness of limitations.\n\n7. **`toolformer-2024` bib key**: Year in key (2024) doesn't match year field (2023). Cosmetic but could confuse contributors.\n"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T14:54:32.680717+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/paper_audit_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T14:54:32.680901+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "paper_audit_report",
  "type": "report",
  "description": "Full-number audit and structural integrity check for EMNLP 2026 paper. Covers canonical directory determination, all numerical claims vs registry, structural completeness, and prioritized issue list.",
  "project": "simgate-modular-routing",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/paper_audit_report.md",
  "tags": "['paper', 'audit', 'emnlp2026']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "paper_audit_report",
    "type": "report",
    "description": "Full-number audit and structural integrity check for EMNLP 2026 paper. Covers canonical directory determination, all numerical claims vs registry, structural completeness, and prioritized issue list.",
    "project": "simgate-modular-routing",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/paper_audit_report.md",
    "tags": "['paper', 'audit', 'emnlp2026']"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-14T14:54:32.681142+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_32a263\", \"name\": \"paper_audit_report\", \"type\": \"report\", \"description\": \"Full-number audit and structural integrity check for EMNLP 2026 paper. Covers canonical directory determination, all numerical claims vs registry, structural completeness, and prioritized issue list.\", \"path\": \"projects/simgate-modular-routing/artifacts/_project/report/paper_audit_report.md\", \"url\": null, \"project\": \"simgate-modular-routing\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T14:54:22.263935+00:00\", \"tags\": [\"paper\", \"audit\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_full-draft-audit_20260514T144747",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-14T14:54:32.681355+00:00_

审计报告已写入并注册。核心结论：

**数字审计：100% 通过** — artifacts/ 目录中所有数字（Table 1、DAF、r/p、tie rate、router accuracy、labeling quality、MATH pilot）均与 registry 一致。trained-router 正确使用 -10.70（非 -12.84），tie rate 正确为 97.4%（非 98.2%）。

**关键问题（P0）**：
1. **两个目录严重分叉** — `docs/paper/` 有大量内容不在 `artifacts/` 中（更完整的 abstract、Rule-Based Baseline 子节、experiments 中 labeling quality 段、更详细的 router 分析）。两者用了不同 CI level（95% vs 90%）。需要合并后废弃 docs/。
2. **discussion.tex 有 2 个 TODO 注释**（pilot-50→math-200-fixed 替换、ALFWorld 结果），math-200-fixed 在 56/200 处崩溃，暂无法替换。

**P1 问题**：
3. plan-013 labeling quality 在 Limitations 里而非 Conclusion（用户意图是"入 conclusion"）
4. MATH pilot 72% 受 sandbox bug 影响（clean accuracy ~89%）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_full-draft-audit_20260514T144747"
}
```

</details>

---
