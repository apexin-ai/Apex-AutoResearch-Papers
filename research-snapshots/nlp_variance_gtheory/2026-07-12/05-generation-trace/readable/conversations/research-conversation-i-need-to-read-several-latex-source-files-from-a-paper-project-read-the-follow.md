# Research conversation: I need to read several LaTeX source files from a paper project. Read the following files in full: 1. /home/ubuntu/.agent

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-abb0722481ef06c45.jsonl`
- **Structured JSON:** [`e1ea232a502a52350320.json`](../../sessions/e1/e1ea232a502a52350320.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-25T14:53:52.855Z_

I need to read several LaTeX source files from a paper project. Read the following files in full:

1. /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/anon_repo/nlp_variance_gtheory/paper/introduction.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/anon_repo/nlp_variance_gtheory/paper/related_work.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/anon_repo/nlp_variance_gtheory/paper/main.tex (just the structure/includes)
4. /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/anon_repo/nlp_variance_gtheory/paper/conclusion.tex
5. /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/anon_repo/nlp_variance_gtheory/paper/appendix.tex

Report the full content of each file, especially:
- The current contributions list in introduction.tex (how many, what they say)
- The structure of related_work.tex (subsections, figure placements)
- What's in the appendix that could potentially be moved to main text
- The overall \input structure in main.tex


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8b560695-79c9-4a5e-b619-2b065d2ef63a",
  "agentId": "abb0722481ef06c45",
  "type": "user",
  "uuid": "248bb9b1-9eb5-40f3-a85b-ec828d74b28d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "6e659a43-3c04-4e3a-bdbf-8c0ba0d43717",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T14:53:54.904Z_

I'll read all five LaTeX files for you. Let me retrieve them in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "248bb9b1-9eb5-40f3-a85b-ec828d74b28d",
  "isSidechain": true,
  "agentId": "abb0722481ef06c45",
  "requestId": "req_011CbPUhXCHCDGfRoKJHD8Jk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8231bea9-a875-4677-83cd-000390ec3b6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "6e659a43-3c04-4e3a-bdbf-8c0ba0d43717",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Vem3BemLVxtHjxaaPp4uRT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 39900,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39900,
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

_source line 3 · 2026-05-25T14:53:55.109Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NB56xVwDTdPpN2RXy8RZpC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/anon_repo/nlp_variance_gtheory/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8231bea9-a875-4677-83cd-000390ec3b6d",
  "isSidechain": true,
  "agentId": "abb0722481ef06c45",
  "requestId": "req_011CbPUhXCHCDGfRoKJHD8Jk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dbfaf1a8-1440-4d2b-9d96-fcd44f45dd6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "6e659a43-3c04-4e3a-bdbf-8c0ba0d43717",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Vem3BemLVxtHjxaaPp4uRT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 39900,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39900,
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

_source line 4 · 2026-05-25T14:53:55.119Z_

<details><summary>↩ Tool result · `toolu_01NB56xVwDTdPpN2RXy8RZpC`</summary>

```text
1	\begin{figure*}[t]
2	\centering
3	\includegraphics[width=\textwidth]{fig_overview_pipeline}
4	\caption{Overview of the G-theory evaluation pipeline. A factorial design crossing seven facets across eight models and five benchmarks produces 2.3M binary records. G-study variance decomposition via Henderson Method~I reveals that model$\times$item interaction accounts for up to 36\% of variance. D-study projections translate variance components into design-dependent item budgets: a 3-prompt $\times$ 3-seed design achieves $G \geq 0.80$ with 178 items (3.1$\times$ reduction). Two contributions emerge: reproducibility budgets (C1) and format-associated variance patterns (C2).}
5	\label{fig:overview}
6	\end{figure*}
7	
8	\section{Introduction}
9	\label{sec:introduction}
10	
11	LLM benchmark scores are increasingly used for model selection and deployment decisions, but their reliability depends on choices that are rarely reported or controlled. Prompt formatting alone can shift accuracy by up to 76 percentage points \citep{sclar2024formatting, brittlebench2026}. Answer ordering \citep{pezeshkpour2024ordering}, numerical precision \citep{yuan2025layercast}, and random seeds \citep{dodge2020finetuning, bui2025seeds} each introduce further variation. These studies examine one source at a time, leaving a fundamental question open: when all sources vary simultaneously, which ones dominate, and does the answer depend on the benchmark format?
12	
13	The piecemeal approach cannot capture interactions between variance sources or track how their relative importance shifts across benchmarks. \citet{bouthillier2021accounting} established variance decomposition for ML reproducibility via ANOVA but did not address LLM evaluation. \citet{messing2026hidden} applied G-theory to LLM evaluation across five methodology facets on a single benchmark but excluded infrastructure facets and cross-benchmark comparison. Item Response Theory (IRT) approaches \citep{polo2024tinybenchmarks, lalor2019irt, zhou2026irt} optimize item selection but treat prompt, seed, and ordering as fixed. Three gaps remain: no study has (a)~crossed infrastructure and methodology facets in a unified factorial design, (b)~compared variance structures across benchmark formats, or (c)~translated variance components into design-dependent reproducibility budgets.
14	
15	We address these gaps with a G-theory study \citep{shavelson1991generalizability, brennan2001generalizability} crossing up to seven facets across eight open-weight 7--9B parameter models and five benchmarks (Figure~\ref{fig:overview}), totaling approximately 2.3 million binary evaluation records. Our central finding is that the variance structure of LLM evaluation is format-conditional. On multiple-choice benchmarks, item-related factors (item difficulty and model-specific item difficulty) account for 68--72\% of total variance; on free-form reasoning benchmarks, this concentration drops below 42\%, with variance distributed across items, models, and prompts. The model$\times$item interaction, at 30--36\% across benchmarks, reveals that models differ primarily in which items they find difficult rather than in overall ability. D-study projections show that multi-facet designs need an order of magnitude fewer items than single-condition designs for reliable measurement (Figure~\ref{fig:teaser}).
16	
17	Our contributions:
18	\begin{enumerate}
19	    \item \textbf{Design-dependent reproducibility budgets.} Multi-facet designs that vary prompts and seeds require dramatically fewer items for reliable measurement. A 3-prompt $\times$ 3-seed design reduces item requirements by 3.1$\times$ on MMLU; cross-benchmark projections yield multi-facet budgets of 93--128 items versus 1,078--2,768 single-condition (Table~\ref{tab:dstudy_cross}). IRT item selection and G-theory protocol optimization are orthogonal and complementary (Table~\ref{tab:dstudy}).
20	
21	    \item \textbf{Format-associated variance patterns (exploratory).} Item-related variance concentrates in multiple-choice benchmarks (68--72\%) and disperses in free-form benchmarks (31--41\%), driven by item difficulty heterogeneity ($\rho = 0.82$ within MMLU subjects). This exploratory observation ($n = 5$ benchmarks, $p = 0.10$) warrants confirmation with broader benchmark samples.
22	\end{enumerate}
23	We release an open-source G-theory pipeline and D-study budget calculator for evaluation design optimization.
24	
25	\begin{figure}[t]
26	\centering
27	\includegraphics[width=\columnwidth]{fig0_teaser_dstudy}
28	\caption{D-study projections for MMLU (single-model baseline). A recommended 3-prompt $\times$ 3-seed design reduces the budget from 552 to 178 items for $G \geq 0.80$; the full multi-facet design reduces further to 55 items.}
29	\label{fig:teaser}
30	\end{figure}
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbfaf1a8-1440-4d2b-9d96-fcd44f45dd6c",
  "isSidechain": true,
  "promptId": "8b560695-79c9-4a5e-b619-2b065d2ef63a",
  "agentId": "abb0722481ef06c45",
  "type": "user",
  "uuid": "3a1b24c5-abcc-44cf-9625-1d5f470fba9a",
  "sourceToolAssistantUUID": "dbfaf1a8-1440-4d2b-9d96-fcd44f45dd6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "6e659a43-3c04-4e3a-bdbf-8c0ba0d43717",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T14:53:55.537Z_

<details open><summary>🔧 Tool call — Read · `toolu_0125yXrysU8wQ7kNf2LZU6Uk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/anon_repo/nlp_variance_gtheory/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a1b24c5-abcc-44cf-9625-1d5f470fba9a",
  "isSidechain": true,
  "agentId": "abb0722481ef06c45",
  "requestId": "req_011CbPUhXCHCDGfRoKJHD8Jk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1d95b632-5268-4e1f-aee6-a6425cf9fc1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "6e659a43-3c04-4e3a-bdbf-8c0ba0d43717",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Vem3BemLVxtHjxaaPp4uRT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 39900,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39900,
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

_source line 6 · 2026-05-25T14:53:55.544Z_

<details><summary>↩ Tool result · `toolu_0125yXrysU8wQ7kNf2LZU6Uk`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=0.85\columnwidth]{fig_method_comparison}
7	\caption{Scope comparison with prior multi-facet variance studies. Our work uniquely combines broad facet crossing, multi-benchmark coverage, and D-study budget projections.}
8	\label{fig:method_comparison}
9	\end{figure}
10	
11	\paragraph{Variance Sources in LLM Evaluation.}
12	\citet{bouthillier2021accounting} introduced ANOVA-based variance decomposition for ML reproducibility, establishing that design choices account for a substantial share of benchmark variance. Subsequent work isolated individual sources: \citet{yuan2025layercast} documented up to 9\% accuracy variation from numerical precision; \citet{sclar2024formatting} and BrittleBench \citep{brittlebench2026} found 50--76\% accuracy swings from prompt formatting; \citet{pezeshkpour2024ordering} and \citet{bui2025seeds} documented ordering and seed sensitivity. \citet{messina2026background} formalized CUDA nondeterminism from floating-point non-associativity. Each study holds other factors fixed, precluding interaction estimation. \citet{madaan2024quantifying} proposed per-factor metrics without crossing factors; holistic evaluation frameworks \citep{liang2023helm, gao2024lmeval} reduce implementation variance but do not decompose it. Our work crosses seven facets simultaneously, enabling interaction estimation and cross-format comparison (Figure~\ref{fig:method_comparison}).
13	
14	\paragraph{IRT and Efficient Benchmarking.}
15	IRT models item difficulty and discrimination to optimize benchmark efficiency \citep{lalor2019irt, rodriguez2021leaderboards}. \citet{polo2024tinybenchmarks} and \citet{zhou2026irt} developed IRT-based subsampling for efficient evaluation; \citet{perlitz2023efficient} and \citet{kipnis2025metabench} explored related compression strategies. These approaches optimize item selection but do not model variance from prompt, seed, or ordering facets. IRT-selected items under a single methodological condition can therefore underestimate required item counts---our results show IRT's 116 items yield $G = 0.457$ single-condition but $G = 0.895$ multi-facet, demonstrating that item selection and protocol optimization are orthogonal.
16	
17	\paragraph{G-Theory and Positioning.}
18	G-theory \cite{shavelson1991generalizability, brennan2001generalizability} provides the canonical framework for multi-facet reliability analysis, with extensions to binary data \cite{mushquash2006gtheory, jiang2018bayesian}. We operationalize differential item functioning \citep{holland1993dif, clauser1998dif} as model$\times$item interaction. Recent psychometric perspectives on LLM evaluation address construct validity \cite{kearns2026construct} and measurement properties \cite{ye2025psychometrics}. Closest to our work, \citet{messing2026hidden} applied G-theory to LLM evaluation, decomposing five methodology facets on a single benchmark (judge identity: 43.8\%). We extend this in three directions: (i) replacing judge identity with infrastructure facets and additional methodology facets; (ii) crossing facets across five benchmarks for cross-format comparison; and (iii) translating variance components into reproducibility budgets via D-study projections. Table~\ref{tab:positioning} summarizes these distinctions.
19	
20	\begin{table}[t]
21	\centering
22	\caption{Positioning relative to prior multi-facet variance studies. ``--'' = not addressed.}
23	\label{tab:positioning}
24	\scriptsize
25	\begin{tabular*}{\columnwidth}{@{\extracolsep{\fill}}lccc@{}}
26	\toprule
27	 & \citet{bouthillier2021accounting} & \citet{messing2026hidden} & Ours \\
28	\midrule
29	Facets crossed & 4 & 5 & 7 \\
30	Design & Factorial & Factorial & Factorial \\
31	Method & ANOVA & G-theory & G-theory \\
32	D-study budgets & -- & -- & \checkmark \\
33	Models & ML models & 6 LLMs & 8 LLMs \\
34	Benchmarks & 3 & 1 & 5 \\
35	Cross-format & -- & -- & MC+FF \\
36	\bottomrule
37	\end{tabular*}
38	\end{table}
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d95b632-5268-4e1f-aee6-a6425cf9fc1c",
  "isSidechain": true,
  "promptId": "8b560695-79c9-4a5e-b619-2b065d2ef63a",
  "agentId": "abb0722481ef06c45",
  "type": "user",
  "uuid": "00b67403-9be6-4ed6-b344-5d3144c446a2",
  "sourceToolAssistantUUID": "1d95b632-5268-4e1f-aee6-a6425cf9fc1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "6e659a43-3c04-4e3a-bdbf-8c0ba0d43717",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T14:53:55.742Z_

<details open><summary>🔧 Tool call — Read · `toolu_018yX7WJoXBWCWczy6qRiiry`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/anon_repo/nlp_variance_gtheory/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00b67403-9be6-4ed6-b344-5d3144c446a2",
  "isSidechain": true,
  "agentId": "abb0722481ef06c45",
  "requestId": "req_011CbPUhXCHCDGfRoKJHD8Jk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0366daed-0b34-4e3d-88e0-254f2f209ace",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "6e659a43-3c04-4e3a-bdbf-8c0ba0d43717",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Vem3BemLVxtHjxaaPp4uRT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 39900,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39900,
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

_source line 8 · 2026-05-25T14:53:55.749Z_

<details><summary>↩ Tool result · `toolu_018yX7WJoXBWCWczy6qRiiry`</summary>

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
10	
11	\usepackage{graphicx}
12	\usepackage{amsmath,amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	
17	\graphicspath{{figures/}}
18	
19	\title{Reproducibility Budgets for Open-Weight LLM Evaluation:\\A Generalizability Theory Study of 7--9B Instruction-Tuned Models}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	\input{abstract}
28	\end{abstract}
29	
30	% === INTRODUCTION ===
31	\input{introduction}
32	
33	% === RELATED WORK ===
34	\input{related_work}
35	
36	% === METHOD ===
37	\input{method}
38	
39	% === EXPERIMENTS ===
40	\input{experiments}
41	
42	% === CONCLUSION ===
43	\input{conclusion}
44	
45	% === LIMITATIONS ===
46	\input{limitations}
47	
48	\bibliography{references}
49	
50	% === APPENDIX ===
51	\input{appendix}
52	
53	\end{document}
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0366daed-0b34-4e3d-88e0-254f2f209ace",
  "isSidechain": true,
  "promptId": "8b560695-79c9-4a5e-b619-2b065d2ef63a",
  "agentId": "abb0722481ef06c45",
  "type": "user",
  "uuid": "32fa5d9d-2fe5-4e48-b860-eceaf5af203e",
  "sourceToolAssistantUUID": "0366daed-0b34-4e3d-88e0-254f2f209ace",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "6e659a43-3c04-4e3a-bdbf-8c0ba0d43717",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T14:53:55.964Z_

<details open><summary>🔧 Tool call — Read · `toolu_011vTuCZWGHEnSHcUmje11cT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/anon_repo/nlp_variance_gtheory/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32fa5d9d-2fe5-4e48-b860-eceaf5af203e",
  "isSidechain": true,
  "agentId": "abb0722481ef06c45",
  "requestId": "req_011CbPUhXCHCDGfRoKJHD8Jk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9eb8ec48-5f0e-427e-8425-52b4ae33097d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "6e659a43-3c04-4e3a-bdbf-8c0ba0d43717",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Vem3BemLVxtHjxaaPp4uRT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 39900,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39900,
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

_source line 10 · 2026-05-25T14:53:55.969Z_

<details><summary>↩ Tool result · `toolu_011vTuCZWGHEnSHcUmje11cT`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:conclusion}
3	
4	The dominant model$\times$item interaction (30--36\%) means model rankings are partly item-dependent, reinforcing calls for item-level reporting \cite{polo2024tinybenchmarks}. The exploratory format-associated pattern---MC benchmarks concentrating 68--72\% in item-related components versus 31--41\% for FF ($p = 0.10$)---suggests per-format budget calibration, pending broader confirmation. A 3-prompt $\times$ 3-seed design reduces items from 552 to 178 ($G \geq 0.80$, MMLU); cross-model projections yield 93--128 items versus 1,078--2,768 single-condition (Table~\ref{tab:dstudy_cross}). We recommend multi-facet validation as standard practice.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9eb8ec48-5f0e-427e-8425-52b4ae33097d",
  "isSidechain": true,
  "promptId": "8b560695-79c9-4a5e-b619-2b065d2ef63a",
  "agentId": "abb0722481ef06c45",
  "type": "user",
  "uuid": "20b7a003-4861-4e1c-ad76-5eaef75ba5d3",
  "sourceToolAssistantUUID": "9eb8ec48-5f0e-427e-8425-52b4ae33097d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "6e659a43-3c04-4e3a-bdbf-8c0ba0d43717",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T14:53:56.227Z_

<details open><summary>🔧 Tool call — Read · `toolu_012oXrxuBpEzEqZGttqqxLBd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/anon_repo/nlp_variance_gtheory/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20b7a003-4861-4e1c-ad76-5eaef75ba5d3",
  "isSidechain": true,
  "agentId": "abb0722481ef06c45",
  "requestId": "req_011CbPUhXCHCDGfRoKJHD8Jk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "68c9aa9c-1a38-40ec-99bf-639487612aad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "6e659a43-3c04-4e3a-bdbf-8c0ba0d43717",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Vem3BemLVxtHjxaaPp4uRT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 39900,
      "cache_read_input_tokens": 0,
      "output_tokens": 464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 39900
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 464,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 39900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 39900,
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

_source line 12 · 2026-05-25T14:53:56.239Z_

<details><summary>↩ Tool result · `toolu_012oXrxuBpEzEqZGttqqxLBd`</summary>

```text
1	\appendix
2	
3	\section{Additional Robustness Analyses}
4	\label{app:robustness}
5	
6	We report nine robustness analyses that verify the stability of the variance decomposition under alternative analytical choices.
7	
8	\paragraph{GLMM complement.} A generalized linear mixed model (GLMM) with marginal logit link produces variance component rankings that perfectly preserve all seven grouped component orderings ($\rho = 1.0$) relative to Henderson Method~I \cite{jiang2018bayesian, tuerlinckx2006glmm}. This confirms that the linear variance decomposition is robust to the binary outcome distribution.
9	
10	\paragraph{Accuracy-range stability.} The \texttt{item\_id} variance share remains stable across subsets with mean accuracy from 0.62 to 0.72 ($r = -0.048$). This rules out distortion from binary floor or ceiling effects at observed accuracy levels.
11	
12	\paragraph{Estimator robustness.} We compare Henderson Method~I with restricted maximum likelihood (REML-EM, 500 iterations, practical convergence $\Delta < 0.003$ percentage points). All variance components differ by $<$0.5 percentage points between estimators. The largest discrepancy occurs on the residual component (0.47pp); all substantive components (item, model$\times$item, model) differ by $<$0.3pp. Henderson Method~I is preferred for our balanced designs because it produces unbiased estimates without distributional assumptions \cite[Ch.~12]{brennan2001generalizability}.
13	
14	\paragraph{Probit simulation.} A probit simulation matched to our 1,296-condition design confirms that Henderson Method~I recovers variance component rankings from dichotomized data (Spearman $\rho = 0.732$ between binary and continuous rankings, excluding residual; \texttt{item\_id} dominant in all 100 replications; top-5 ordering correct in 79\% of replications). Bias analysis by difficulty stratum shows $|\text{bias}| = 0.28$--$0.37$ for items with $p \in [0.5, 0.8]$, where the Bernoulli variance ceiling $p(1{-}p)$ is largest. This analysis covers the observed accuracy range ($p \in [0.3, 0.9]$); extreme-difficulty items ($p < 0.3$ or $p > 0.9$) are rare in our sample ($<$8\% of items) and may exhibit larger deviations. Henderson Method~I absorbs this Bernoulli-inherent variance into the residual, explaining inflated bias near medium difficulty; systematic component ordering is robustly recovered across all replications. Binary scoring inflates residual variance by absorbing the Bernoulli $p(1{-}p)$ ceiling, which enters $\sigma^2_\text{rel}$ and increases D-study item requirements. Within a matched probit simulation, binarization increases D-study budgets by approximately 36\% (99 $\to$ 135 items for $G \geq 0.80$), driven by residual inflation (16\% $\to$ 41\%) and item variance compression (50\% $\to$ 32\%). Facet$\times$item interactions---the components entering $\sigma^2_\text{rel}$---are best preserved under binarization (MAPE = 12.8\%, range 8.7--17.5\%), while residual variance inflates as expected from Bernoulli $p(1{-}p)$ noise (MAPE = 156\%). D-study budgets derived from binary data are therefore conservative: continuous-scored designs would require equal or fewer items for the same $G$ threshold. Null calibration (ratio $= 1.0008$) confirms that this conservatism does not distort relative component magnitudes.
15	
16	\paragraph{CI method comparison.} Bootstrap (1,000 item-level resamples with replacement) and delete-1 jackknife confidence intervals agree closely: width ratios range from 0.96 to 1.04 across all variance components. Bootstrap CIs capture item-sampling variability conditional on these 8 specific models; model-level stability is assessed separately via LOMO (below). The agreement indicates that the dependence structure introduced by item-level bootstrap resampling (which creates $\sim$127 unique items per 200-item resample) does not materially distort interval estimates. Stratified resampling by subject (10 subjects $\times$ 20 items) produces CIs within 4\% of simple item-level bootstrap, confirming that the within-subject dependence structure does not materially affect interval estimates.
17	
18	\paragraph{Facet specification sensitivity.} Treating temperature and ordering as fixed (rather than random) facets changes $G_\text{item}$ by only 0.37 percentage points (all-random: 0.820 vs.\ fixed temperature+ordering: 0.824). The small difference reflects the negligible temperature$\times$item (0.65\%) and ordering$\times$item (0.54\%) variance shares. The random-facet assumption is therefore robust to facet classification.
19	
20	\paragraph{Leave-one-model-out (LOMO).} Across all 40 leave-one-model-out subsets (8 models $\times$ 5 benchmarks), $G_\text{item}$ ranges from 0.833 to 0.919, with CV $\leq$ 1.25\% per benchmark. No single model removal changes $G$ by more than 0.030 (GSM8K, removing Gemma-2-9B). Item-related variance rankings are preserved in all 40 subsets. Table~\ref{tab:lomo_full} (main text) reports per-benchmark stability. This supports treating models as exchangeable within the target universe of 7--9B instruction-tuned models (\S\ref{sec:model_facet}).
21	
22	\paragraph{Inter-model agreement.} We computed pairwise Cohen's $\kappa$ and Fleiss' $\kappa$ across all model pairs on each benchmark. Mean pairwise $\kappa$ ranges from 0.326 (MATH) to 0.461 (MMLU); Fleiss' $\kappa$ ranges from 0.309 (GSM8K) to 0.456 (MMLU). HellaSwag uses six models ($\kappa = 0.332$) due to missing OLMo and Yi data. The fair-to-moderate agreement independently confirms that the model$\times$item interaction (30--36\% of variance) reflects genuine differential item functioning: models disagree substantially on which items are difficult, consistent with prior DIF findings in educational measurement \cite{holland1993dif, clauser1998dif}.
23	
24	\paragraph{Scoring metric sensitivity.}
25	\label{sec:partial_credit}
26	To probe metric conditionality, we compared binary correctness with step-level partial credit on GSM8K using the full 8-model crossed design (200 items, 2,304 conditions per item). Under partial credit, $G_\text{item}$ drops from 0.863 to 0.768, with residual variance rising from 39.9\% to 64.9\% and item variance falling from 16.9\% to 10.3\%. All eight models individually show $G_\text{partial} < G_\text{binary}$ (mean $\Delta G = -0.135$, range $-0.025$ to $-0.309$), with $\Delta G$ magnitude moderated by model accuracy: higher-accuracy models have fewer incorrect responses whose scores shift under partial credit (e.g., OLMo at 70.1\% accuracy shows $\Delta G = -0.025$, while Llama at 49.0\% shows $\Delta G = -0.309$). The mechanism is clear: 48.1\% of incorrect responses have numerically correct arithmetic steps but incorrect problem setup, receiving partial score $= 1.0$ despite binary score $= 0$---this compresses item discrimination and inflates residual variance. Binary scoring amplifies prompt sensitivity by collapsing reasoning quality into pass/fail, confirming that all findings in this paper are metric-conditional.
27	
28	\paragraph{Facet specification sensitivity: random vs.\ fixed model.} Table~\ref{tab:fixed_vs_random} reports per-benchmark generalizability coefficients under random and fixed model specifications. The consistent $\Delta G$ of 0.077--0.113 confirms that random-model budgets are strictly more conservative across all benchmarks.
29	
30	\begin{table}[h]
31	\centering
32	\caption{Generalizability coefficients under random vs.\ fixed model facet specification across five benchmarks.}
33	\label{tab:fixed_vs_random}
34	\scriptsize
35	\begin{tabular}{lrrr}
36	\toprule
37	Benchmark & $G_\text{random}$ & $G_\text{fixed}$ & $\Delta G$ \\
38	\midrule
39	MMLU & 0.896 & 0.984 & $+$0.088 \\
40	ARC & 0.892 & 0.990 & $+$0.098 \\
41	HellaSwag & 0.872 & 0.984 & $+$0.113 \\
42	GSM8K & 0.863 & 0.951 & $+$0.089 \\
43	MATH & 0.888 & 0.965 & $+$0.077 \\
44	\midrule
45	Mean & 0.882 & 0.975 & $+$0.093 \\
46	\bottomrule
47	\end{tabular}
48	\end{table}
49	
50	\paragraph{Null calibration.} We generate 100 Bernoulli-distributed datasets with item difficulties matched to the empirical distribution but no systematic facet effects. The observed-to-null variance ratio is 1.0008, confirming that Henderson Method~I does not introduce systematic bias when applied to binary outcomes. The null simulation also verifies that the item variance share (58.4\%) is not an artifact of the Bernoulli $p(1{-}p)$ ceiling: the null produces item variance of 0.08\%, three orders of magnitude below the observed value. Across all 100 replications, the same three components (item, model$\times$item, residual) emerge as the top three (set consistency 100\%), with Kendall's $\tau = 0.81$ between binary and continuous rankings.
51	
52	\paragraph{Reduced crossing validation.} To verify that the reduced crossing in exp-002 (BF16 only $\times$ 2 temperatures) does not introduce confounding, we extracted the corresponding subset from the fully crossed exp-001 design. The generalizability coefficient differs by only 0.0008 ($G = 0.9361$ vs.\ $0.9369$), and all non-precision variance components differ by less than 2 percentage points. The 10pp increase in item variance share (58.4\% $\to$ 68.5\%) is fully explained by the removal of precision-related components ($\sim$4.5\% total), which redistributes across remaining sources. This confirms that the exp-002 design preserves the variance structure of the full crossing.
53	
54	\section{Projection Validation Details}
55	\label{app:dstudy_cross}
56	
57	\paragraph{Internal consistency check.} Table~\ref{tab:forward_pred} reports consistency checks from four exp-001 models (DeepSeek, Llama, Mistral, Qwen3) to the full eight-model design across all five benchmarks. MC benchmarks show $|\Delta G| \leq 0.029$ ($<$3.5\% error), while FF benchmarks show larger deviations ($|\Delta G| \leq 0.065$, $\sim$7\%) due to limited model diversity in the four-model subset. FF predictions consistently underestimate actual $G$ (conservative); MC predictions show mixed directions with small deviations ($|\Delta G| \leq 0.029$).
58	
59	\begin{table}[h]
60	\centering
61	\caption{Internal consistency: four-model subset vs.\ eight-model $G_\text{item}$. FF subsets underestimate actual $G$ (conservative); MC shows mixed directions with small deviations.}
62	\label{tab:forward_pred}
63	\small
64	\begin{tabular}{lrrrr}
65	\toprule
66	Benchmark & Predicted $G$ & Actual $G$ & $|\Delta G|$ & Error\% \\
67	\midrule
68	\multicolumn{5}{l}{\textit{Multiple-choice}} \\
69	MMLU & 0.888 & 0.896 & 0.009 & 0.96 \\
70	ARC & 0.904 & 0.892 & 0.012 & 1.38 \\
71	HellaSwag & 0.901 & 0.872 & 0.029 & 3.33 \\
72	\midrule
73	\multicolumn{5}{l}{\textit{Free-form}} \\
74	GSM8K & 0.803 & 0.863 & 0.059 & 6.88 \\
75	MATH & 0.823 & 0.888 & 0.065 & 7.30 \\
76	\midrule
77	Mean & --- & --- & 0.035 & 3.97 \\
78	\bottomrule
79	\end{tabular}
80	\end{table}
81	
82	\begin{figure}[h]
83	\centering
84	\includegraphics[width=\columnwidth]{budget_sensitivity_band}
85	\caption{Effect of $|\Delta G| = 0.035$ estimation error on item budgets. The $\sim$23\% increase is consistent across benchmarks.}
86	\label{fig:budget_sensitivity}
87	\end{figure}
88	
89	\paragraph{Budget sensitivity to estimation error.}
90	\label{app:budget_sensitivity}
91	The effect of $|\Delta G| = 0.035$ estimation error on item budgets is shown in Figure~\ref{fig:budget_sensitivity}. The percentage increase is remarkably stable (23.0--24.5\%, mean 23.2\%), because the relative budget adjustment $\Delta n / n$ depends on the $G$-formula ratio rather than on absolute variance components. Absolute $\Delta n$ ranges from 13 (ARC) to 67 (GSM8K), scaling with the baseline budget.
92	
93	\paragraph{Cross-benchmark $G$ stability.}
94	\label{app:cross_benchmark_transfer}
95	$G_\text{item}$ values cluster in a narrow band across all five benchmarks (0.863--0.896, CV = 1.4\%), despite qualitatively different variance structures: MC benchmarks concentrate 68--72\% in item-related components while GSM8K disperses variance across item (17\%), model (11\%), and interaction (15\%) sources (Table~\ref{tab:cross_benchmark}). This stability implies that D-study budget recommendations calibrated on one benchmark provide reasonable order-of-magnitude guidance for others. However, the 0.033 range in $G_\text{item}$ translates to a 71--128 item range for multi-facet $G \geq 0.80$ (Table~\ref{tab:dstudy_cross}), and the variance compositions differ substantially---benchmark-specific G-studies remain necessary to identify dominant variance sources and optimize condition selection.
96	
97	\section{Format-Associated Variance: Per-Benchmark Details}
98	\label{app:format_details}
99	
100	This section supplements the compressed format-associated analysis in \S\ref{sec:format_conditional} with per-benchmark details.
101	
102	\paragraph{MC benchmark exceptions.} HellaSwag is the sole MC case where model$\times$item slightly exceeds item (36.0\% vs.\ 34.3\%), though their sum (70.3\%) remains in the MC range (68--72\%). Among MC benchmarks, ARC-Challenge shows an anomalously high model$\times$prompt interaction (8.0\% vs.\ $<$2\% for MMLU and HellaSwag), suggesting that science-domain items are differentially sensitive to option formatting across model families.
103	
104	\paragraph{FF benchmark patterns.} Free-form benchmarks differ markedly from MC. On GSM8K, variance distributes across item (16.9\%), model$\times$item (14.6\%), model (10.7\%), and model$\times$prompt (8.5\%); prompt main effect is 5.4\%. MATH shows an intermediate pattern: item leads at 24.0\% with model$\times$item at 17.3\%, but residual variance is substantially larger (43.9\%). Item-level regression reveals that FF residual variance is predominantly explained by the Bernoulli variance ceiling $p(1{-}p)$ ($R^2 = 0.47$--$0.86$; Appendix~\ref{app:ff_residual}): medium-difficulty items maximize binary outcome variance regardless of facet structure, so the elevated FF residuals reflect measurement resolution rather than unmodeled substantive sources.
105	
106	\paragraph{Difficulty dispersion as variance predictor.} Difficulty dispersion ($\text{std}(p_i)$) strongly predicts item variance share ($\rho = 0.82$, $n = 5$ benchmarks; Appendix~\ref{app:difficulty_scatter}; reasoning-heavy subjects show $G_\text{item}$ as low as 0.614, Appendix~\ref{app:subject_gstudy}). Format constrains the noise floor, but difficulty heterogeneity determines variance magnitude within it.
107	
108	\paragraph{Item-level bootstrap stability.} Bootstrap resampling (1,000 item resamples per benchmark) confirms that the MC--FF separation is robust to item selection: 95\% CIs for item-related variance (item + model$\times$item) are [65.2, 75.0]\% (MC) and [28.0, 44.2]\% (FF), with no overlap (minimum gap 21.0 percentage points).
109	
110	\section{Cross-Benchmark Difficulty Heterogeneity}
111	\label{app:difficulty_scatter}
112	
113	Item difficulty heterogeneity is shown in Figure~\ref{fig:difficulty_scatter} (main text). MC benchmarks cluster at higher dispersion ($0.27$--$0.31$) and higher item variance ($34$--$38\%$), while FF benchmarks occupy the lower-left region ($0.22$--$0.23$, $17$--$24\%$). The cross-benchmark Spearman $\rho = 0.82$ ($p = 0.089$, $n = 5$) is consistent in direction with the within-MMLU correlation ($\rho = 0.806$, $p = 0.005$, $n = 10$ subjects); these are independent analyses at different granularities (benchmarks vs.\ subjects within MMLU), providing multi-scale support for the item difficulty heterogeneity mechanism discussed in \S\ref{sec:format_conditional}.
114	
115	\section{MMLU Subject-Level Variance Decomposition}
116	\label{app:subject_gstudy}
117	
118	Table~\ref{tab:subject_gstudy} reports per-subject variance decomposition for 10 MMLU subjects (20 items each, 8 models, 2,304 conditions per item). $G_\text{item}$ ranges from 0.614 (\texttt{high\_school\_mathematics}) to 0.930 (\texttt{international\_law}), with mean 0.843. Knowledge-intensive subjects (\texttt{international\_law}, \texttt{clinical\_knowledge}, \texttt{world\_religions}) show \texttt{item\_id} $>$ 40\%, while reasoning-heavy subjects (\texttt{high\_school\_mathematics}, \texttt{abstract\_algebra}) show model$\times$item $>$ \texttt{item\_id}, consistent with models differing more in reasoning strategies than in factual recall. The \texttt{high\_school\_mathematics} \texttt{item\_id} of 10.4\% referenced in \S\ref{sec:format_conditional} is the lowest across all subjects, below even GSM8K (16.9\%).
119	
120	\begin{table}[h]
121	\centering
122	\caption{Subject-level variance decomposition within MMLU (20 items per subject, 8 models, 2,304 conditions per item). Sorted by $G_\text{item}$ descending.}
123	\label{tab:subject_gstudy}
124	\scriptsize
125	\begin{tabular}{lrrrr}
126	\toprule
127	Subject & Acc. & item\% & mod.$\times$it.\% & $G_\text{item}$ \\
128	\midrule
129	international\_law & .717 & 44.4 & 24.1 & .930 \\
130	clinical\_knowledge & .581 & 47.5 & 30.0 & .923 \\
131	world\_religions & .826 & 42.2 & 27.1 & .910 \\
132	computer\_security & .740 & 37.0 & 24.9 & .908 \\
133	college\_physics & .436 & 31.6 & 30.1 & .876 \\
134	philosophy & .782 & 33.0 & 36.1 & .868 \\
135	abstract\_algebra & .457 & 24.1 & 32.8 & .822 \\
136	us\_foreign\_policy & .864 & 20.4 & 36.9 & .802 \\
137	professional\_medicine & .671 & 19.9 & 41.7 & .778 \\
138	high\_school\_math & .385 & 10.4 & 41.9 & .614 \\
139	\midrule
140	Mean & --- & 31.1 & 32.6 & .843 \\
141	\bottomrule
142	\end{tabular}
143	\end{table}
144	
145	\section{FF Residual Variance Analysis}
146	\label{app:ff_residual}
147	
148	To investigate whether the elevated residual variance in free-form benchmarks (GSM8K 39.9\%, MATH 43.9\%) reflects unmodeled substantive sources or measurement properties of binary scoring, we regress item-level residual variance on item characteristics across all five benchmarks (Table~\ref{tab:ff_residual}).
149	
150	The dominant predictor is the quadratic difficulty effect ($p < 10^{-5}$ on all benchmarks): items near $p = 0.5$ show maximal residual variance, while items near the floor or ceiling show minimal residual. This inverted-U pattern directly mirrors the Bernoulli variance ceiling $p(1{-}p)$. Item content features (number of reasoning steps, answer length) are not significant predictors for GSM8K ($p > 0.38$), confirming that the difficulty--residual relationship is statistical rather than content-driven.
151	
152	FF benchmarks show substantially higher $R^2$ (mean 0.66) than MC benchmarks (mean 0.25), consistent with FF items spanning a wider difficulty range. The MC--FF contrast in residual magnitude is therefore a mathematical consequence of the difficulty distribution under binary scoring, not evidence of additional unmodeled variance sources in free-form evaluation.
153	
154	\begin{table}[h]
155	\centering
156	\caption{Item-level residual variance regression. Difficulty$^2$ = quadratic (inverted-U) term reflecting the Bernoulli $p(1{-}p)$ ceiling. GSM8K additionally tests n\_steps and answer\_length (both $p > 0.38$).}
157	\label{tab:ff_residual}
158	\scriptsize
159	\begin{tabular}{lrrr}
160	\toprule
161	Benchmark & $R^2$ (full) & $R^2$ (diff.\ only) & Diff.$^2$ $p$ \\
162	\midrule
163	\multicolumn{4}{l}{\textit{Multiple-choice}} \\
164	MMLU & 0.377 & 0.347 & $<$0.001 \\
165	ARC & 0.221 & 0.204 & $<$0.001 \\
166	HellaSwag & 0.156 & 0.140 & $<$0.001 \\
167	\midrule
168	\multicolumn{4}{l}{\textit{Free-form}} \\
169	GSM8K & 0.468 & 0.449 & $<$0.001 \\
170	MATH & 0.856 & 0.845 & $<$0.001 \\
171	\bottomrule
172	\end{tabular}
173	\end{table}
174	
175	\section{Model and Prompt Details}
176	\label{app:models}
177	
178	\paragraph{Models.} See Table~\ref{tab:model_ids} (main text) for the eight models. Full HuggingFace identifiers: \texttt{meta-llama/Llama-3.1-8B-Instruct}, \texttt{google/gemma-2-9b-it}, \texttt{mistralai/Mistral-7B-Instruct-v0.3}, \texttt{Qwen/Qwen3-8B}, \texttt{01-ai/Yi-1.5-9B-Chat}, \texttt{allenai/OLMo-2-1124-7B-Instruct}, \texttt{internlm/internlm2\_5-7b-chat}, \texttt{deepseek-ai/deepseek-llm-7b-chat}.
179	
180	\paragraph{Prompt templates.} Our six prompt templates follow a surface perturbation design inspired by BrittleBench \cite{brittlebench2026}. For multiple-choice benchmarks, templates vary along three dimensions: option layout (lettered vs.\ numbered), instruction wording (direct vs.\ contextual), and answer prompt cue. For free-form benchmarks, templates vary chain-of-thought elicitation strategy. All six templates are semantically equivalent---they request the same task with different surface forms---to isolate formatting effects from content effects. ARC-Challenge and HellaSwag use the same six surface patterns as MMLU with domain-appropriate system instructions; MATH mirrors the GSM8K pattern with \texttt{\textbackslash boxed\{\}} answer formatting.
181	
182	\smallskip\noindent\textit{MMLU templates (representative MC format):}
183	\begin{enumerate}\setlength{\itemsep}{0pt}\setlength{\parsep}{0pt}\setlength{\topsep}{0pt}
184	\item \texttt{The following are multiple choice questions (with answers) about \{subject\}.\textbackslash n\textbackslash n\{question\}\textbackslash nA. ... D. ...\textbackslash nAnswer:}
185	\item \texttt{Answer the following \{subject\} questions by selecting the correct option.\textbackslash nQuestion: \{question\}\textbackslash n(A) ... (B) ... (C) ... (D) ...\textbackslash nCorrect answer:}
186	\item \texttt{Below are \{subject\} multiple-choice problems. Pick the right letter.\textbackslash nQ: \{question\}\textbackslash n~~A) ... B) ... C) ... D) ...\textbackslash nA:}
187	\item \texttt{Answer the following \{subject\} question by selecting A, B, C, or D.\textbackslash n\{question\}\textbackslash n- A. ... - B. ... - C. ... - D. ...\textbackslash nAnswer:}
188	\item \texttt{Below is a \{subject\} exam question with four possible answers. Choose the correct one.\textbackslash n\{question\}\textbackslash nOption A: ... Option B: ... Option C: ... Option D: ...\textbackslash nCorrect:}
189	\item \texttt{Question (\{subject\}):\textbackslash n\{question\}\textbackslash nChoices: (A) ... (B) ... (C) ... (D) ...\textbackslash nYour answer:}
190	\end{enumerate}
191	
192	\smallskip\noindent\textit{GSM8K templates (representative FF format):}
193	\begin{enumerate}\setlength{\itemsep}{0pt}\setlength{\parsep}{0pt}\setlength{\topsep}{0pt}
194	\item \texttt{Solve the following math problem step by step.\textbackslash nQ: \{question\}\textbackslash nA: Let's think step by step.}
195	\item \texttt{Answer the following math word problem. Show your work.\textbackslash nQuestion: \{question\}\textbackslash nSolution:}
196	\item \texttt{Solve each problem below. Write your reasoning, then give the final answer after \#\#\#\#.\textbackslash nProblem: \{question\}\textbackslash nReasoning:}
197	\item \texttt{You are a math tutor. Solve the problem and show your steps.\textbackslash n\{question\}\textbackslash nSteps:}
198	\item \texttt{Work through this math question carefully.\textbackslash nQ: \{question\}\textbackslash nWork:}
199	\item \texttt{Math problem:\textbackslash n\{question\}\textbackslash nLet's solve this step by step.}
200	\end{enumerate}
201	
202	\section{Use of AI Assistants}
203	\label{app:ai-assistants}
204	
205	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
206	\begin{itemize}
207	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
208	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \LaTeX{}.
209	    \item \textbf{Literature:} summarizing related papers to inform related-work section.
210	\end{itemize}
211	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68c9aa9c-1a38-40ec-99bf-639487612aad",
  "isSidechain": true,
  "promptId": "8b560695-79c9-4a5e-b619-2b065d2ef63a",
  "agentId": "abb0722481ef06c45",
  "type": "user",
  "uuid": "5a819097-e05c-4915-8eb1-de77f431a0d7",
  "sourceToolAssistantUUID": "68c9aa9c-1a38-40ec-99bf-639487612aad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "6e659a43-3c04-4e3a-bdbf-8c0ba0d43717",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-25T14:54:19.108Z_

Perfect! I have successfully read all five LaTeX files. Here's a comprehensive report:

---

## **1. introduction.tex - Contributions Analysis**

The introduction contains **2 main contributions** (in an enumerate block):

1. **Design-dependent reproducibility budgets**: Multi-facet designs (varying prompts and seeds) require dramatically fewer items for reliable measurement. A 3-prompt × 3-seed design reduces item requirements by 3.1× on MMLU; cross-benchmark projections yield 93--128 items vs. 1,078--2,768 for single-condition designs. Notes that IRT item selection and G-theory protocol optimization are orthogonal and complementary.

2. **Format-associated variance patterns (exploratory)**: Item-related variance concentrates in multiple-choice benchmarks (68--72%) and disperses in free-form benchmarks (31--41%), driven by item difficulty heterogeneity (ρ = 0.82 within MMLU subjects). This is explicitly labeled as exploratory with n=5 benchmarks and p=0.10, warranting broader confirmation.

**Key structural elements**:
- Opens with Figure 1 (overview pipeline) at the top
- Central finding: model×item interaction dominates at 30--36% across benchmarks
- D-study projections are central to the contribution narrative
- Closes with Figure 2 (teaser D-study projections for MMLU)

---

## **2. related_work.tex - Structure and Figures**

**Three main paragraph sections** (not subsections):

1. **Variance Sources in LLM Evaluation** - Reviews prior work on prompt formatting, seeds, ordering, precision effects; notes piecemeal approaches; introduces the need for multi-facet factorial designs
   - **Figure 1** embedded here: `fig_method_comparison` showing scope comparison with prior studies

2. **IRT and Efficient Benchmarking** - Discusses Item Response Theory approaches (Polo et al., Zhou et al.) that optimize item selection but don't model variance from prompt/seed/ordering

3. **G-Theory and Positioning** - Establishes G-theory framework and closest prior work (Messing et al. 2026)
   - **Table 1** (`tab:positioning`) embedded here: Positioning table comparing Bouthillier, Messing, and current work across 7 dimensions (facets, design, method, D-study budgets, models, benchmarks, cross-format)

**No subsections**, only `\paragraph{}` headers. One figure and one table integrated seamlessly into the narrative.

---

## **3. main.tex - Document Structure**

The main document follows a standard ACL article template with these `\input` directives (in order):

```
\input{abstract}
\input{introduction}
\input{related_work}
\input{method}
\input{experiments}
\input{conclusion}
\input{limitations}
\bibliography{references}
\input{appendix}
```

**Key metadata**:
- Uses `acl` package with `[review]` option
- Title: "Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models"
- Graphs path set to `./figures/`
- Anonymous author

---

## **4. conclusion.tex - Condensed Discussion**

A single `\section{Discussion and Conclusion}` (very brief):

- Reiterates the model×item interaction dominance (30--36%) and calls for item-level reporting
- States the exploratory format-associated pattern (MC: 68--72%, FF: 31--41%, p=0.10)
- Quantifies the 3-prompt × 3-seed design benefit: 552 → 178 items for G ≥ 0.80 on MMLU
- Cross-model projection: 93--128 items (multi-facet) vs. 1,078--2,768 (single-condition)
- Recommends multi-facet validation as standard practice

**Length**: Only 5 lines in the source file.

---

## **5. appendix.tex - Content That Could Potentially Be Moved**

The appendix is comprehensive and contains **9 major sections**:

### **Robustness Analyses (most of appendix)**
- GLMM complement (validates linear decomposition)
- Accuracy-range stability analysis
- Estimator robustness (Henderson Method I vs. REML-EM)
- Probit simulation (validates binary scoring method)
- CI method comparison (bootstrap vs. jackknife)
- Facet specification sensitivity (random vs. fixed)
- Leave-one-model-out (LOMO) stability across 40 subsets
- Inter-model agreement (Cohen's κ, Fleiss' κ)
- Scoring metric sensitivity (binary vs. partial credit on GSM8K)
- Fixed vs. random model facet specification table

### **Projection Validation Details**
- Internal consistency checks (four-model subset vs. eight-model)
- Budget sensitivity to estimation error (Figure with 23% stability band)
- Cross-benchmark G stability analysis

### **Format-Associated Variance: Per-Benchmark Details**
- MC benchmark exceptions (HellaSwag anomaly)
- Free-form benchmark patterns (GSM8K distribution details)
- Difficulty dispersion as variance predictor (ρ = 0.82)
- Item-level bootstrap stability with 95% CIs

### **Cross-Benchmark Difficulty Heterogeneity**
- Figure scatter plot and Spearman correlation (ρ = 0.82, p = 0.089)

### **MMLU Subject-Level Variance Decomposition**
- Per-subject G-study table (10 MMLU subjects, 20 items each)
- Ranges from 0.614 (high school math) to 0.930 (international law)

### **Free-Form Residual Variance Analysis**
- Regression of item-level residual variance on item characteristics
- Demonstrates Bernoulli ceiling effect explains FF residuals

### **Model and Prompt Details**
- Full HuggingFace identifiers for 8 models
- All 6 MMLU prompt templates (representative MC)
- All 6 GSM8K prompt templates (representative FF)

### **Use of AI Assistants**
- Disclosure of Claude use for code, writing, and literature summarization

---

## **Key Moveable Content Analysis**

**Could be moved to main text**:
- Subject-level MMLU G-study table (Table in Section \ref{app:subject_gstudy}) — this granular per-subject breakdown directly supports the format-associated variance claim
- The prompt template examples (Section \ref{app:models}) — understanding the six surface perturbation patterns is methodologically important for reproducibility
- The LOMO stability results — key evidence for model exchangeability assumption

**Should stay in appendix**:
- All 9 robustness analyses (too technical, validate rather than drive narrative)
- Detailed projection validation (supporting analysis, not core contribution)
- Residual variance regression details (explains a null finding)
- Model and prompt full technical details

**Currently optimal**:
- The appendix is well-organized with clear motivation for each section
- Main text focuses correctly on the two contributions; appendix provides mathematical rigor

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a819097-e05c-4915-8eb1-de77f431a0d7",
  "isSidechain": true,
  "agentId": "abb0722481ef06c45",
  "requestId": "req_011CbPUhmjPu8A5vMvHeejM4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eff77283-3036-4a6c-b553-19074edfcb39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/director_754d9c1f",
  "sessionId": "6e659a43-3c04-4e3a-bdbf-8c0ba0d43717",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ata4Q1Vu5eRTLrMPgasTqk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 12285,
      "cache_read_input_tokens": 39900,
      "output_tokens": 1737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12285
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1737,
          "cache_read_input_tokens": 39900,
          "cache_creation_input_tokens": 12285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12285,
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
